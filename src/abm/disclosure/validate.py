"""Mechanical and per-asset stylized-fact checks of the multi-asset market."""

from __future__ import annotations

import numpy as np

from ..msm import MOMENT_NAMES, compute_moments
from .config import TRADING_DAYS_PER_YEAR, MarketConfig
from .harness import CONSERVATION_TOLERANCE, CrossSectionResult


def _summary(values: np.ndarray) -> dict[str, object]:
    finite = values[np.isfinite(values)]
    return {
        "finite_count": int(finite.size),
        "minimum": float(finite.min()) if finite.size else None,
        "maximum": float(finite.max()) if finite.size else None,
        "mean": float(finite.mean()) if finite.size else None,
        "median": float(np.median(finite)) if finite.size else None,
        "quantile_05": float(np.quantile(finite, 0.05)) if finite.size else None,
        "quantile_95": float(np.quantile(finite, 0.95)) if finite.size else None,
    }


def validate_market(
    result: CrossSectionResult,
    config: MarketConfig,
    *,
    return_acf_target: float | None = None,
    return_acf_tolerance: float | None = None,
    correlation_bounds: tuple[float, float] | None = None,
    conservation_tolerance: float = CONSERVATION_TOLERANCE,
) -> dict[str, object]:
    """Check every asset and day; empirical calibration remains a separate gate.

    Moments use simple price returns, matching the M1 calibration script.
    Correlations are descriptive unless the caller supplies bounds. An ACF
    target without a tolerance reports deviations without imposing a gate.
    Cash errors are relative to initial cash plus reconstructed dividends;
    share errors are the recorded daily maximum absolute error across assets.
    """
    if result.prices.shape != (config.trading_days + 1, config.n_firms) or (
        result.intrinsic_values.shape != result.prices.shape or result.burn_in_days != config.burn_in_days
    ):
        raise ValueError("result dimensions and burn-in must match config")
    if not np.isfinite(conservation_tolerance) or conservation_tolerance < 0:
        raise ValueError("conservation_tolerance must be finite and nonnegative")
    if return_acf_target is not None and not np.isfinite(return_acf_target):
        raise ValueError("return_acf_target must be finite")
    if return_acf_tolerance is not None and (
        return_acf_target is None or not np.isfinite(return_acf_tolerance) or return_acf_tolerance < 0
    ):
        raise ValueError("a finite nonnegative ACF tolerance requires a target")
    if correlation_bounds is not None and (
        len(correlation_bounds) != 2 or not np.all(np.isfinite(correlation_bounds))
        or correlation_bounds[0] > correlation_bounds[1]
    ):
        raise ValueError("correlation_bounds must be two finite ordered values")

    dividend_path = config.cash_flow_yield * result.intrinsic_values[1:].sum(axis=1) / TRADING_DAYS_PER_YEAR
    expected_cash = result.total_cash[0] + np.r_[0.0, np.cumsum(dividend_path)]
    with np.errstate(divide="ignore", invalid="ignore"):
        cash_errors = np.abs(result.total_cash - expected_cash) / np.where(expected_cash != 0, np.abs(expected_cash), 1.0)
        returns = np.expm1(result.log_returns())
    cash_error = float(np.max(cash_errors))
    share_error = float(np.max(np.abs(result.maximum_share_error)))
    mechanical_checks = {
        "finite_positive_prices": bool(np.all(np.isfinite(result.prices) & (result.prices > 0))),
        "finite_positive_intrinsic_values": bool(np.all(np.isfinite(result.intrinsic_values) & (result.intrinsic_values > 0))),
        "no_price_caps": bool(np.all(result.price_cap_hits == 0)),
        "cash_conservation": bool(np.isfinite(cash_error) and cash_error <= conservation_tolerance),
        "share_conservation": bool(np.isfinite(share_error) and share_error <= conservation_tolerance),
    }

    moments = np.full((config.n_firms, len(MOMENT_NAMES)), np.nan)
    for asset in range(config.n_firms):
        if not np.all(np.isfinite(returns[:, asset])):
            continue
        try:
            with np.errstate(divide="ignore", invalid="ignore"):
                moments[asset] = compute_moments(returns[:, asset])
        except ValueError:
            continue
    finite_moments = np.all(np.isfinite(moments), axis=1)
    heavy_tails = np.isfinite(moments[:, 1]) & (moments[:, 1] > 0)
    volatility_clustering = np.isfinite(moments[:, 3]) & (moments[:, 3] > 0)
    stylized_checks = {
        "all_assets_have_finite_moments": bool(np.all(finite_moments)),
        "all_assets_positive_excess_kurtosis": bool(np.all(heavy_tails)),
        "all_assets_positive_abs_return_acf_1": bool(np.all(volatility_clustering)),
    }

    return_acf = moments[:, 2]
    deviations = return_acf - return_acf_target if return_acf_target is not None else None
    acf_pass = np.isfinite(return_acf) & (np.abs(deviations) <= return_acf_tolerance) if (
        deviations is not None and return_acf_tolerance is not None
    ) else None
    if acf_pass is not None:
        stylized_checks["return_acf_within_supplied_tolerance"] = bool(np.all(acf_pass))

    with np.errstate(divide="ignore", invalid="ignore"):
        correlations = np.corrcoef(returns, rowvar=False) if config.n_firms > 1 else np.empty((0, 0))
    pairs = correlations[np.triu_indices(config.n_firms, k=1)] if config.n_firms > 1 else np.array([])
    correlation_pass = None
    if correlation_bounds is not None and pairs.size:
        correlation_pass = np.isfinite(pairs) & (pairs >= correlation_bounds[0]) & (pairs <= correlation_bounds[1])
        stylized_checks["correlations_within_supplied_bounds"] = bool(np.all(correlation_pass))

    return {
        "n_assets": config.n_firms,
        "observations": int(returns.shape[0]),
        "burn_in_days": config.burn_in_days,
        "mechanical": {
            "status": "PASS" if all(mechanical_checks.values()) else "FAIL",
            "checks": mechanical_checks,
            "price_cap_hits": int(np.sum(result.price_cap_hits)),
            "maximum_relative_cash_error": cash_error if np.isfinite(cash_error) else None,
            "maximum_absolute_share_error": share_error if np.isfinite(share_error) else None,
            "conservation_tolerance": conservation_tolerance,
            "cash_error_measure": "relative to expected cash; absolute if expected cash is zero",
            "share_error_measure": "daily maximum absolute error across all assets",
        },
        "stylized": {
            "status": "PASS" if all(stylized_checks.values()) else "FAIL",
            "checks": stylized_checks,
            "failed_assets": {
                "nonfinite_moments": np.flatnonzero(~finite_moments).tolist(),
                "nonpositive_excess_kurtosis": np.flatnonzero(~heavy_tails).tolist(),
                "nonpositive_abs_return_acf_1": np.flatnonzero(~volatility_clustering).tolist(),
            },
        },
        "return_acf": {
            "status": "pending" if acf_pass is None else ("PASS" if np.all(acf_pass) else "FAIL"),
            "statistics": _summary(return_acf),
            "target": return_acf_target,
            "tolerance": return_acf_tolerance,
            "threshold_source": "caller_supplied" if acf_pass is not None else None,
            "deviation_statistics": _summary(deviations) if deviations is not None else None,
            "failed_assets": np.flatnonzero(~acf_pass).tolist() if acf_pass is not None else None,
        },
        "cross_asset_correlation": {
            "status": "pending" if correlation_pass is None else ("PASS" if np.all(correlation_pass) else "FAIL"),
            "statistics": _summary(pairs),
            "pair_count": int(pairs.size),
            "bounds": list(correlation_bounds) if correlation_bounds is not None else None,
            "threshold_source": "caller_supplied" if correlation_pass is not None else None,
            "violating_pair_count": int(np.count_nonzero(~correlation_pass)) if correlation_pass is not None else None,
        },
        "moments_per_asset": [
            {"asset": asset, "moments": {
                name: float(value) if np.isfinite(value) else None
                for name, value in zip(MOMENT_NAMES, moments[asset], strict=True)
            }} for asset in range(config.n_firms)
        ],
        "empirical_calibration": {
            "status": "pending",
            "reason": "This validator does not evaluate held-out empirical targets.",
        },
    }
