from dataclasses import replace

import numpy as np
import pytest

from abm import load_stage1_config
from abm.msm import (
    FAILED_SIMULATION_PENALTY,
    MOMENT_NAMES,
    EmpiricalTarget,
    ParameterSpace,
    StageOneSimulator,
    block_bootstrap_moments,
    calibrate,
    compute_moments,
    hill_tail_index,
    objective,
    parameter_standard_errors,
)

pytest.importorskip("scipy")


def _target(moments, standard_errors):
    moments = np.asarray(moments, dtype=np.float64)
    return EmpiricalTarget(
        industries=("synthetic",),
        observations=1000,
        moments=moments,
        covariance=np.diag(np.asarray(standard_errors, dtype=np.float64) ** 2),
        per_industry=moments[None, :],
    )


def test_gaussian_moments_have_no_tails_or_memory():
    returns = np.random.default_rng(1).normal(0.0, 0.01, 50_000)
    moments = dict(zip(MOMENT_NAMES, compute_moments(returns), strict=True))
    assert moments["daily_volatility"] == pytest.approx(0.01, rel=0.02)
    assert abs(moments["excess_kurtosis"]) < 0.1
    assert abs(moments["return_acf_1"]) < 0.02
    assert abs(moments["abs_return_acf_5"]) < 0.02
    assert moments["quantile_01"] == pytest.approx(-0.0233, rel=0.05)


def test_hill_estimator_recovers_pareto_exponent():
    rng = np.random.default_rng(2)
    signs = rng.choice((-1.0, 1.0), size=200_000)
    returns = signs * (rng.pareto(3.0, size=200_000) + 1.0)
    assert hill_tail_index(returns, tail_fraction=0.01) == pytest.approx(3.0, rel=0.1)


def test_moments_keep_trading_day_spacing_with_missing_values():
    returns = np.random.default_rng(3).normal(0.0, 0.01, 2000)
    returns[100] = np.nan
    assert np.all(np.isfinite(compute_moments(returns)))


def test_block_bootstrap_is_reproducible_and_shaped():
    returns = np.random.default_rng(4).standard_t(4, 1500) * 0.01
    first = block_bootstrap_moments(
        returns, block_length=20, draws=5, rng=np.random.default_rng(7)
    )
    second = block_bootstrap_moments(
        returns, block_length=20, draws=5, rng=np.random.default_rng(7)
    )
    assert first.shape == (5, len(MOMENT_NAMES))
    np.testing.assert_array_equal(first, second)


def test_parameter_space_round_trip_and_application():
    space = ParameterSpace.from_dict({"noise_scale": (0.5, 2.5), "price_impact": (0.2, 1.2)})
    theta = np.array([1.5, 0.7])
    np.testing.assert_allclose(space.from_unit(space.to_unit(theta)), theta)
    np.testing.assert_allclose(space.from_unit(np.array([-1.0, 2.0])), [0.5, 1.2])
    config = space.apply(load_stage1_config("configs/stage1_structural_dev_v11.json"), theta)
    assert (config.noise_scale, config.price_impact) == (1.5, 0.7)
    with pytest.raises(ValueError):
        ParameterSpace.from_dict({"noise_scale": (2.0, 1.0)})


def test_objective_is_sum_of_squared_t_statistics():
    target = _target([1.0, 2.0], [0.5, 1.0])
    simulated = np.array([[2.0, 2.0], [2.0, 4.0]])
    summary = objective(simulated, target)
    scale = np.array([0.5, 1.0]) * np.sqrt(1.5)
    expected = ((np.array([2.0, 3.0]) - [1.0, 2.0]) / scale)
    np.testing.assert_allclose(summary["t_statistics"], expected)
    assert summary["j"] == pytest.approx(float(np.sum(expected**2)))


def test_objective_penalizes_mostly_failed_simulations():
    target = _target([1.0, 2.0], [0.5, 1.0])
    simulated = np.array([[np.nan, np.nan], [np.nan, np.nan], [1.0, 2.0]])
    summary = objective(simulated, target)
    assert summary["j"] == FAILED_SIMULATION_PENALTY
    assert summary["failed_paths"] == 2


class LinearSimulator:
    """Cheap stand-in for the market: moments are linear in theta plus
    seed-specific noise that is common across parameter vectors (CRN)."""

    def __init__(self, seeds=8):
        rng = np.random.default_rng(11)
        self.loading = rng.normal(size=(len(MOMENT_NAMES), 3))
        self.noise = rng.normal(scale=0.02, size=(seeds, len(MOMENT_NAMES)))

    def moments(self, theta):
        return self.loading @ theta

    def __call__(self, thetas):
        thetas = np.atleast_2d(thetas)
        return np.stack([self.moments(theta)[None, :] + self.noise for theta in thetas])


def test_calibration_recovers_known_parameters():
    simulator = LinearSimulator()
    space = ParameterSpace.from_dict({"a": (-1.0, 1.0), "b": (0.0, 2.0), "c": (1.0, 3.0)})
    truth = np.array([0.3, 1.2, 2.4])
    target = _target(simulator.moments(truth), np.full(len(MOMENT_NAMES), 0.05))
    result = calibrate(
        simulator, space, target, screen_points=64, refine_starts=2, refine_evaluations=200
    )
    np.testing.assert_allclose(result["best_theta"], truth, atol=0.05)
    errors = parameter_standard_errors(simulator, space, target, np.array(result["best_theta"]))
    assert all(0.0 < value < 0.2 for value in errors["standard_errors"])


def test_stage_one_simulator_returns_seed_by_moment_array():
    base = replace(
        load_stage1_config("configs/stage1_structural_dev_v11.json"),
        population_size=200,
        burn_in_days=50,
    )
    space = ParameterSpace.from_dict({"noise_scale": (0.5, 2.0)})
    simulator = StageOneSimulator(base, space, seeds=(1, 2), observations=500)
    first = simulator(np.array([[1.0], [1.5]]))
    assert first.shape == (2, 2, len(MOMENT_NAMES))
    assert np.all(np.isfinite(first))
    np.testing.assert_array_equal(first[0], simulator(np.array([1.0]))[0])
    assert simulator.config_for(np.array([1.5]), 2).trading_days == 550
