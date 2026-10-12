"""Exploratory MSM fit of the M1 cross-section market to French 49 training moments."""
import glob, json, sys, time
import numpy as np
from dataclasses import replace
from datetime import date
from concurrent.futures import ProcessPoolExecutor
from abm.platform_tuning import disable_power_throttling
from abm.disclosure import MarketConfig
from abm.disclosure.harness import CrossSectionMarket, MarketDivergedError
from abm.french49 import parse_french49_zip, IndustrySplit
from abm.msm import MOMENT_NAMES, ParameterSpace, calibrate, compute_moments, empirical_target, objective

SPACE = ParameterSpace.from_dict({
    "noise_flow_scale": (0.002, 0.012),
    "noise_common_correlation": (0.1, 0.9),
    "liquidity_volatility_sensitivity": (0.0, 4.0),
    "fundamental_volatility": (0.08, 0.25),
    "transient_impact_decay": (0.8, 0.98),
    "permanent_impact_fraction": (0.4, 0.9),
    "noise_volatility_exponent": (0.0, 2.0),
})
ASSETS = np.arange(0, 200, 5)

def path_moments(args):
    theta, seed, days, burn = args
    over = dict(zip(SPACE.names, map(float, theta)))
    try:
        r = CrossSectionMarket(replace(MarketConfig(trading_days=burn + days, burn_in_days=burn, seed=seed), **over)).run()
    except MarketDivergedError:
        return np.full(len(MOMENT_NAMES), np.nan)
    ret = np.expm1(r.log_returns()[:, ASSETS])
    try:
        return np.mean([compute_moments(ret[:, i]) for i in range(ret.shape[1])], axis=0)
    except ValueError:
        return np.full(len(MOMENT_NAMES), np.nan)

class Sim:
    def __init__(self, ex, seeds, days, burn):
        self.ex, self.seeds, self.days, self.burn = ex, seeds, days, burn
    def __call__(self, thetas):
        thetas = np.atleast_2d(thetas)
        jobs = [(t, s, self.days, self.burn) for t in thetas for s in self.seeds]
        return np.array(list(self.ex.map(path_moments, jobs))).reshape(len(thetas), len(self.seeds), -1)

if __name__ == "__main__":
    disable_power_throttling()
    z = glob.glob('data/raw/kenneth_french/*/49_Industry_Portfolios_daily_CSV.zip')[0]
    ds = parse_french49_zip(z).between(date(2000, 1, 1), date(2025, 12, 31))
    target = empirical_target(ds, IndustrySplit.from_json('configs/french49_split_v1.json').train)
    with ProcessPoolExecutor(12, initializer=disable_power_throttling) as ex:
        sim = Sim(ex, seeds=(11, 12, 13, 14), days=target.observations, burn=1000)
        t = time.perf_counter()
        res = calibrate(sim, SPACE, target, screen_points=128, refine_starts=2, refine_evaluations=60,
                        progress=lambda m: print(m, flush=True))
        best = np.array(res['best_theta'])
        fresh = Sim(ex, seeds=tuple(range(101, 111)), days=target.observations, burn=1000)(best)[0]
    print('minutes', round((time.perf_counter() - t) / 60, 1))
    print('best theta', dict(zip(SPACE.names, np.round(best, 4))))
    print('calibration-seed J', round(res['best']['j'], 2), 't', np.round(res['best']['t_statistics'], 2))
    fo = objective(fresh, target)
    print('fresh-seed J', round(fo['j'], 2), 't', np.round(fo['t_statistics'], 2))
    print('sim', dict(zip(MOMENT_NAMES, np.round(fo['simulated_moments'], 4))))
    print('target', dict(zip(MOMENT_NAMES, np.round(target.moments, 4))))
    json.dump({'theta': dict(zip(SPACE.names, best.tolist())), 'calibration_j': res['best']['j'], 'fresh_j': fo['j']},
              open(sys.argv[1] if len(sys.argv) > 1 else 'calibration_result.json', 'x'), indent=2)
