import hashlib
import json
from dataclasses import replace

import numpy as np
import pytest

from abm.disclosure.calibration import calibrate_book_csv, calibrate_csv, main
from abm.disclosure.config import MarketConfig, load_market_config
from abm.disclosure.domain import DomainSpec, load_domain
from abm.disclosure.game import AttributeState

ESG = load_domain("configs/domains/esg.json")


@pytest.fixture
def scores(tmp_path):
    source = tmp_path / "scores.csv"
    source.write_text("id,YEAR ,score\na,2023,0\nb,2023,0\nc,2023,10\nd,2023,20\ne,2023,\nf,2022,99\ng,,5\n", encoding="utf-8")
    return source


def fit(source, **changes):
    options = dict(value_column="score", year_column="YEAR ", year="2023", raw_lower=0.0, raw_upper=20.0,
                   direction=1, unit="observed social proxy points", name="social_proxy", attribute_label="Social observed proxy")
    options.update(changes)
    return calibrate_csv(source, ESG, **options)


def test_csv_selection_retains_zero_mass_and_reports_exclusions(scores):
    domain, report = fit(scores, raw_source=scores)
    assert domain.initial_empirical_distribution == ((0.0, 2), (10.0, 1), (20.0, 1))
    assert domain.initial_mean == 7.5
    assert domain.initial_sd == pytest.approx(np.std([0, 0, 10, 20]))
    assert report["selection"]["input_rows"] == 7
    assert report["selection"]["filtered_out_rows"] == 2
    assert report["selection"]["missing_year_rows"] == 1
    assert report["selection"]["selected_blank_value_rows"] == 1
    assert report["sample"]["zero_mass"] == .5
    assert report["sample"]["upper_bound_mass"] == .25
    assert report["upstream_raw_file"]["sha256"] == hashlib.sha256(scores.read_bytes()).hexdigest()
    assert domain.real_cost_scale == ESG.real_cost_scale
    assert "natural_decay" in report["unidentified_domain_parameters"]
    assert "baseline_audit_probability" in report["unidentified_domain_parameters"]
    assert "modeling assumption" in report["initialization"]["state_assumption"]
    assert domain.action_labels == {}
    assert DomainSpec.from_dict(domain.to_dict()) == domain


@pytest.mark.parametrize("direction", [1, -1])
def test_empirical_initialization_is_reproducible_discrete_and_signed(scores, direction):
    domain, _ = fit(scores, direction=direction)
    classes = np.zeros(10000, dtype=np.int64)
    first = AttributeState.initialize(domain, classes, np.random.default_rng(42))
    second = AttributeState.initialize(domain, classes, np.random.default_rng(42))
    np.testing.assert_array_equal(first.goodness, second.goodness)
    np.testing.assert_array_equal(first.cost_scale, second.cost_scale)
    support = domain.to_goodness(np.array([0.0, 10.0, 20.0]))
    assert np.isin(first.goodness, support).all()
    assert np.mean(first.goodness == support[0]) == pytest.approx(.5, abs=.02)
    np.testing.assert_allclose(domain.to_raw(support), [0, 10, 20])
    low, high = domain.goodness_bounds
    assert first.goodness.min() >= low and first.goodness.max() <= high
    assert (support[0] < support[-1]) == (direction == 1)
    assert domain.initial_sd == pytest.approx(np.std([0, 0, 10, 20]))
    assert np.count_nonzero(first.inflation) == 0


def test_default_normal_initialization_and_serialization_remain_compatible():
    assert "initial_empirical_distribution" not in ESG.to_dict()
    expected = [0.7511571621260598, -0.1536803503590459, 1.0726691186933262,
                0.5163604646743323, -1.3133911283994923]
    state = AttributeState.initialize(ESG, np.zeros(5, dtype=np.int64), np.random.default_rng(42))
    np.testing.assert_allclose(state.goodness, expected, atol=1e-14, rtol=0)


def test_explicit_unfiltered_selection_does_not_infer_years(scores):
    domain, report = fit(scores, year_column=None, year=None, raw_upper=100.0)
    assert sum(count for _, count in domain.initial_empirical_distribution) == 6
    assert report["selection"]["filtered_out_rows"] == 0
    assert report["selection"]["selected_blank_value_rows"] == 1
    assert report["selection"]["year_match"] == "all rows"


@pytest.mark.parametrize("changes", [
    {"value_column": "ESG"}, {"year_column": "YEAR"}, {"year": "2024"},
    {"year_column": None}, {"raw_upper": 15.0}, {"direction": 0}, {"unit": ""},
])
def test_wrong_columns_filters_bounds_and_direction_are_rejected(scores, changes):
    with pytest.raises(ValueError):
        fit(scores, **changes)


@pytest.mark.parametrize("bad_value", ["N/A", "nan", "inf", "-1", "21"])
def test_invalid_proxy_values_are_not_silently_dropped(scores, bad_value):
    scores.write_text(f"YEAR ,score\n2023,0\n2023,10\n2023,{bad_value}\n", encoding="utf-8")
    with pytest.raises(ValueError):
        fit(scores)


def test_duplicate_csv_headers_and_constant_cohorts_are_rejected(scores):
    scores.write_text("YEAR ,score,score\n2023,0,1\n2023,1,2\n", encoding="utf-8")
    with pytest.raises(ValueError, match="headers"):
        fit(scores)
    scores.write_text("YEAR ,score\n2023,0\n2023,0\n", encoding="utf-8")
    with pytest.raises(ValueError, match="distinct"):
        fit(scores)


@pytest.mark.parametrize("distribution", [((0.0, 1.5), (20.0, 1)), ((0.0, 0), (20.0, 1)),
                                           ((0.0, 1), (0.0, 1)), ((-1.0, 1), (20.0, 1))])
def test_empirical_domain_rejects_invalid_support_and_counts(scores, distribution):
    domain, _ = fit(scores)
    with pytest.raises(ValueError):
        replace(domain, initial_empirical_distribution=distribution)
    with pytest.raises(ValueError, match="moments"):
        replace(domain, initial_sd=domain.initial_sd * 2)


def test_cli_writes_a_loadable_domain_provenance_and_preserves_existing_files(scores, tmp_path):
    output, report = tmp_path / "domain.json", tmp_path / "report.json"
    arguments = ["--csv", str(scores), "--value-column", "score", "--year-column", "YEAR ", "--year", "2023",
                 "--raw-lower", "0", "--raw-upper", "20", "--direction", "1", "--unit", "social proxy points",
                 "--name", "social_proxy", "--attribute-label", "Social observed proxy", "--template", "configs/domains/esg.json",
                 "--output-domain", str(output), "--report", str(report)]
    assert main(arguments) == 0
    assert load_domain(output).initial_empirical_distribution == ((0.0, 2), (10.0, 1), (20.0, 1))
    data = json.loads(report.read_text(encoding="utf-8"))
    assert data["output_domain"]["sha256"] == hashlib.sha256(output.read_bytes()).hexdigest()
    assert data["upstream_raw_file"] is None
    before = output.read_bytes()
    with pytest.raises(SystemExit):
        main(arguments)
    assert output.read_bytes() == before


def test_wba_social_domain_uses_2023_observed_support_only():
    domain = load_domain("configs/domains/wba_social_2023.json")
    assert domain.raw_lower == 0 and domain.raw_upper == 20
    assert sum(count for _, count in domain.initial_empirical_distribution) == 1035
    assert domain.initial_empirical_distribution[0][0] == 0
    assert domain.initial_empirical_distribution[0][1] > 0
    assert "social" in domain.attribute_label.lower() and "proxy" in domain.attribute_label.lower()
    assert domain.initial_mean == pytest.approx(5.385507246376812)
    assert domain.initial_sd == pytest.approx(3.8592611002995967)


BOOK_HEADER = "issuer,cohort,currency,as_of,published,book\n"
BOOK_ROWS = ("a,P,CNY,2026-06-30,2026-08-27,100\nb,P,CNY,2026-06-30,2026-08-30,400\n"
             "c,P,CNY,2026-06-30,2026-08-31,1600\nd,Q,USD,2026-06-30,2026-12-01,-5\n"
             "e,P,CNY,2025-12-31,2026-03-30,7\n")


@pytest.fixture
def books(tmp_path):
    source = tmp_path / "books.csv"
    source.write_text(BOOK_HEADER + BOOK_ROWS, encoding="utf-8")
    return source


def fit_book(source, template=None, **changes):
    options = dict(issuer_column="issuer", value_column="book", cohort_column="cohort", cohort="P",
                   currency_column="currency", currency="CNY", as_of_column="as_of", as_of="2026-06-30",
                   publication_column="published", publication_cutoff="2026-10-09", unit="CNY yuan")
    options.update(changes)
    return calibrate_book_csv(source, template or MarketConfig(), **options)


def test_book_fit_matches_hand_computed_log_moments_and_changes_only_sigma(books):
    template = MarketConfig(intrinsic_value_log_sd=.25)
    config, report = fit_book(books, template)
    logs = np.log([100.0, 400.0, 1600.0])
    assert report["fit"]["mu"] == pytest.approx(logs.mean())
    assert config.intrinsic_value_log_sd == pytest.approx(np.std(logs))
    assert config.intrinsic_value_log_sd == pytest.approx(np.log(4) * np.sqrt(2 / 3))
    assert replace(config, intrinsic_value_log_sd=.25) == template
    assert report["selection"]["issuer_ids"] == ["a", "b", "c"]
    assert report["selection"]["filtered_out_cohort_rows"] == 1
    assert report["selection"]["filtered_out_as_of_rows"] == 1
    assert MarketConfig.from_dict(config.to_dict()) == config


def test_equal_book_values_permit_zero_sigma(books):
    books.write_text(BOOK_HEADER + "a,P,CNY,2026-06-30,2026-08-27,5\nb,P,CNY,2026-06-30,2026-08-27,5\n",
                     encoding="utf-8")
    config, _ = fit_book(books)
    assert config.intrinsic_value_log_sd == 0


@pytest.mark.parametrize("rows, match", [
    ("a,P,CNY,2026-06-30,2026-08-27,1\na,P,CNY,2026-06-30,2026-08-27,2\n", "duplicate"),
    ("a,P,CNY,2026-06-30,2026-08-27,1\nb,P,USD,2026-06-30,2026-08-27,2\n", "currency"),
    ("a,P,CNY,2026-06-30,2026-08-27,1\nb,P,CNY,2026-06-30,2026-10-10,2\n", "after cutoff"),
    ("a,P,CNY,2026-06-30,2026-08-27,1\nb,P,CNY,2026-06-30,2026-06-29,2\n", "before as_of"),
    ("a,P,CNY,2026-06-30,2026-08-27,1\nb,P,CNY,2026-06-30,,2\n", "publication date"),
    ("a,P,CNY,2026-06-30,2026-08-27,1\nb,P,CNY,2026-06-30,2026-08-27,0\n", "positive"),
    ("a,P,CNY,2026-06-30,2026-08-27,1\nb,P,CNY,2026-06-30,2026-08-27,nan\n", "positive"),
    ("a,P,CNY,2026-06-30,2026-08-27,1\nb,P,CNY,2026-06-30,2026-08-27,\n", "book value"),
    ("a,P,CNY,2026-06-30,2026-08-27,1\n", "at least two"),
])
def test_book_rejects_invalid_selected_rows(books, rows, match):
    books.write_text(BOOK_HEADER + rows, encoding="utf-8")
    with pytest.raises(ValueError, match=match):
        fit_book(books)


def test_book_cli_writes_reloadable_config_and_score_default_is_unchanged(books, scores, tmp_path):
    output, report = tmp_path / "market.json", tmp_path / "book_report.json"
    template = tmp_path / "template.json"
    template.write_text(json.dumps(MarketConfig().to_dict()), encoding="utf-8")
    arguments = ["--kind", "book", "--csv", str(books), "--value-column", "book", "--unit", "CNY yuan",
                 "--issuer-column", "issuer", "--cohort-column", "cohort", "--cohort", "P",
                 "--currency-column", "currency", "--currency", "CNY", "--as-of-column", "as_of",
                 "--as-of", "2026-06-30", "--publication-column", "published", "--publication-cutoff", "2026-10-09",
                 "--template", str(template), "--output-config", str(output), "--report", str(report)]
    assert main(arguments) == 0
    assert load_market_config(output).intrinsic_value_log_sd == pytest.approx(np.log(4) * np.sqrt(2 / 3))
    data = json.loads(report.read_text(encoding="utf-8"))
    assert data["output_config"]["sha256"] == hashlib.sha256(output.read_bytes()).hexdigest()
    with pytest.raises(SystemExit):
        main(arguments + ["--year", "2023"])
    score_output = tmp_path / "domain.json"
    assert main(["--csv", str(scores), "--value-column", "score", "--year-column", "YEAR ", "--year", "2023",
                 "--raw-lower", "0", "--raw-upper", "20", "--direction", "1", "--unit", "points",
                 "--name", "social_proxy", "--attribute-label", "Social observed proxy",
                 "--template", "configs/domains/esg.json", "--output-domain", str(score_output),
                 "--report", str(tmp_path / "score_report.json")]) == 0
    assert load_domain(score_output).initial_mean == 7.5


MID_RANK_SCORES = [-0.6744897501960817, 0.31863936396437515, 1.1503493803760079]


def test_quantile_link_uses_mid_ranks_and_saturates_at_an_observed_scale_end(scores):
    domain, report = fit(scores, observation_link="empirical_quantile")
    assert domain.goodness_bounds == (-6.0, 6.0)
    np.testing.assert_allclose(domain.to_goodness(np.array([0.0, 10.0, 20.0])), MID_RANK_SCORES, rtol=0, atol=1e-12)
    np.testing.assert_allclose(domain.to_raw(np.array(MID_RANK_SCORES)), [0, 10, 20], rtol=0, atol=1e-12)
    np.testing.assert_array_equal(domain.to_raw(np.array([2.0, 6.0, -6.0])), [20.0, 20.0, 0.0])
    assert "latent standard-normal" in report["initialization"]["state_assumption"]
    assert DomainSpec.from_dict(domain.to_dict()) == domain
    wide, _ = fit(scores, observation_link="empirical_quantile", raw_upper=100.0)
    assert wide.to_raw(np.array([6.0]))[0] == 100.0 and 20 < wide.to_raw(np.array([3.0]))[0] < 100
    lower, _ = fit(scores, observation_link="empirical_quantile", direction=-1)
    np.testing.assert_allclose(lower.to_goodness(np.array([0.0, 20.0])), [-MID_RANK_SCORES[0], -MID_RANK_SCORES[2]])
    np.testing.assert_allclose(lower.to_raw(lower.to_goodness(np.array([10.0]))), [10.0])


def test_default_domains_keep_their_serialization_and_reject_invalid_links(scores):
    assert "observation_link" not in ESG.to_dict() and "initial_size_rank_correlation" not in ESG.to_dict()
    domain, _ = fit(scores)
    for changes in ({"observation_link": "logit"}, {"initial_size_rank_correlation": .2},
                    {"observation_link": "empirical_quantile", "initial_size_rank_correlation": 1.0}):
        with pytest.raises(ValueError):
            replace(domain, **changes)
    with pytest.raises(ValueError, match="two empirical"):
        replace(ESG, observation_link="empirical_quantile")


def test_quantile_initialization_is_latent_normal_with_the_requested_size_copula(scores):
    domain, _ = fit(scores, observation_link="empirical_quantile")
    classes = np.zeros(20000, dtype=np.int64)
    state = AttributeState.initialize(domain, classes, np.random.default_rng(3))
    assert abs(state.goodness.mean()) < .03 and abs(state.goodness.std() - 1) < .03
    values = np.random.default_rng(4).lognormal(0, 1.3, classes.size)
    linked = replace(domain, initial_size_rank_correlation=.5)
    first = AttributeState.initialize(linked, classes, np.random.default_rng(5), intrinsic_value=values)
    second = AttributeState.initialize(linked, classes, np.random.default_rng(5), intrinsic_value=values)
    np.testing.assert_array_equal(first.goodness, second.goodness)
    assert np.corrcoef(first.goodness, np.log(values))[0, 1] == pytest.approx(.5, abs=.02)
    with pytest.raises(ValueError, match="intrinsic value"):
        AttributeState.initialize(linked, classes, np.random.default_rng(5))


def test_quantile_link_removes_the_mechanical_ceiling_on_the_latent_state(scores):
    domain, _ = fit(scores, observation_link="empirical_quantile")
    state = AttributeState(goodness=np.array([2.0]), inflation=np.zeros(1), cost_scale=np.ones(1))
    state.schedule(1, 0, np.array([0]), np.array([1.0]))
    state.schedule(1, 1, np.array([0]), np.array([.5]))
    state.advance(1, replace(domain, natural_decay=0.0))
    assert state.goodness[0] == 3.0 and state.inflation[0] == .5
    assert domain.to_raw(state.goodness)[0] == 20.0


def test_size_rank_correlation_is_fitted_through_the_gaussian_copula(tmp_path):
    source = tmp_path / "joint.csv"
    source.write_text("score,cap\n1,10\n2,30\n3,20\n4,40\n5,50\n", encoding="utf-8")
    options = dict(value_column="score", year_column=None, year=None, raw_lower=0.0, raw_upper=10.0, unit="points",
                   name="proxy", attribute_label="observed proxy", observation_link="empirical_quantile", size_column="cap")
    domain, report = calibrate_csv(source, ESG, direction=1, **options)
    spearman = .9
    assert report["initialization"]["size_dependence"]["spearman_raw_vs_log_size"] == pytest.approx(spearman)
    assert domain.initial_size_rank_correlation == pytest.approx(2 * np.sin(np.pi * spearman / 6))
    lower, _ = calibrate_csv(source, ESG, direction=-1, **options)
    assert lower.initial_size_rank_correlation == pytest.approx(-domain.initial_size_rank_correlation)
    with pytest.raises(ValueError, match="quantile"):
        calibrate_csv(source, ESG, direction=1, **dict(options, observation_link="linear"))
    source.write_text("score,cap\n1,10\n2,0\n", encoding="utf-8")
    with pytest.raises(ValueError, match="size"):
        calibrate_csv(source, ESG, direction=1, **options)


def test_market_cap_proxy_changes_only_the_provenance_label(books):
    book_config, book_report = fit_book(books)
    cap_config, cap_report = fit_book(books, proxy="market_cap")
    assert cap_config == book_config
    assert book_report["status"] == "book_proxy_lognormal_dispersion_only"
    assert cap_report["status"] == "market_cap_proxy_lognormal_dispersion_only" and cap_report["proxy"] == "market_cap"
    assert "P0=V0" in cap_report["initialization"]["state_assumption"]
    with pytest.raises(ValueError, match="proxy"):
        fit_book(books, proxy="assets")
