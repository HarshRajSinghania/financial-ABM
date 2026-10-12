import numpy as np
import pytest

from abm.baselines import (
    HAM_PARAMETER_SPACE,
    HamSimulator,
    fit_garch_t,
    fit_iid_t,
    garch_variance_path,
    simulate_ham_returns,
)
from abm.msm import MOMENT_NAMES

pytest.importorskip("scipy")

# Franke and Westerhoff (2012), DCA-HPM estimates.
FRANKE_WESTERHOFF = np.array([0.12, 1.50, 0.758, 2.087, -0.327, 1.79, 18.43])


def _garch_returns(alpha, beta, nu, volatility, size, seed):
    rng = np.random.default_rng(seed)
    shocks = rng.standard_t(nu, size) * np.sqrt((nu - 2.0) / nu)
    omega = volatility**2 * (1.0 - alpha - beta)
    returns = np.empty(size)
    variance, previous = volatility**2, 0.0
    for day in range(size):
        variance = omega + alpha * previous**2 + beta * variance
        previous = np.sqrt(variance) * shocks[day]
        returns[day] = previous
    return returns


def test_variance_filter_matches_explicit_recursion():
    residuals = np.random.default_rng(1).normal(0.0, 0.01, 300)
    omega, alpha, beta = 2e-6, 0.07, 0.9
    expected = np.empty_like(residuals)
    expected[0] = np.mean(residuals**2)
    for day in range(1, residuals.size):
        expected[day] = omega + alpha * residuals[day - 1] ** 2 + beta * expected[day - 1]
    np.testing.assert_allclose(garch_variance_path(residuals, omega, alpha, beta), expected)


def test_pooled_garch_mle_recovers_simulated_parameters():
    series = [
        _garch_returns(0.08, 0.9, 6.0, volatility, 4000, seed)
        for seed, volatility in enumerate((0.01, 0.015, 0.02))
    ]
    fitted = fit_garch_t([values - values.mean() for values in series])
    assert fitted["alpha"] == pytest.approx(0.08, abs=0.02)
    assert fitted["beta"] == pytest.approx(0.9, abs=0.03)
    assert fitted["nu"] == pytest.approx(6.0, abs=1.5)


def test_iid_t_mle_recovers_tail_parameter():
    rng = np.random.default_rng(3)
    series = [rng.standard_t(5.0, 20_000) * scale for scale in (0.01, 0.02)]
    assert fit_iid_t(series)["nu"] == pytest.approx(5.0, abs=0.5)


def test_franke_westerhoff_model_shows_fat_tails_and_clustering():
    assert np.all(FRANKE_WESTERHOFF >= HAM_PARAMETER_SPACE.lower)
    assert np.all(FRANKE_WESTERHOFF <= HAM_PARAMETER_SPACE.upper)
    returns = simulate_ham_returns(FRANKE_WESTERHOFF, observations=6000, seed=4)
    assert np.all(np.isfinite(returns))
    moments = HamSimulator(observations=6000, seeds=(4,))(FRANKE_WESTERHOFF)[0, 0]
    named = dict(zip(MOMENT_NAMES, moments, strict=True))
    assert named["excess_kurtosis"] > 1.0
    assert named["abs_return_acf_1"] > 0.1
    assert 0.003 < named["daily_volatility"] < 0.05
