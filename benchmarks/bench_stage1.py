"""Time Stage 1 runs and fingerprint their outputs.

Compare timings under the same configuration. Matching Stage 1 fingerprints
verify unchanged simulation outputs; speedups depend on the machine and workload.

    python benchmarks/bench_stage1.py --days 1000 3500 --seeds 1 2 3
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import replace
from pathlib import Path
from typing import Sequence

from abm import load_stage1_config, run_stage1
from abm.platform_tuning import disable_power_throttling
from abm.stage2 import create_market_harness, load_simulation_config

ROOT = Path(__file__).resolve().parents[1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "configs" / "stage1.json")
    parser.add_argument("--stage2-config", type=Path, default=ROOT / "configs" / "stage2_five_nodes.json")
    parser.add_argument("--days", type=int, nargs="+", default=[1000, 3500])
    parser.add_argument("--seeds", type=int, nargs="+", default=[1, 2, 3])
    parser.add_argument("--output", type=Path, help="write results as JSON")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.output and args.output.exists():
        raise FileExistsError(args.output)
    power_throttling_disabled = disable_power_throttling()
    print(f"power throttling disabled: {power_throttling_disabled}")
    base = load_stage1_config(args.config)
    rows: list[dict[str, object]] = []
    for days in args.days:
        for seed in args.seeds:
            config = replace(base, seed=seed, trading_days=days, burn_in_days=min(base.burn_in_days, days // 2))
            start = time.perf_counter()
            result = run_stage1(config)
            elapsed = time.perf_counter() - start
            rows.append({"kind": "stage1", "days": days, "seed": seed,
                         "power_throttling_disabled": power_throttling_disabled,
                         "seconds": round(elapsed, 3), "fingerprint": result.fingerprint()})
            print(f"stage1 days={days:>6} seed={seed:>3} {elapsed:8.2f}s {result.fingerprint()[:16]}")
    if args.stage2_config.exists():
        config = load_simulation_config(args.stage2_config)
        start = time.perf_counter()
        result = create_market_harness(config).run()
        elapsed = time.perf_counter() - start
        rows.append({"kind": "stage2", "config": args.stage2_config.name,
                     "power_throttling_disabled": power_throttling_disabled,
                     "seconds": round(elapsed, 3), "fingerprint": result.fingerprint()})
        print(f"stage2 {args.stage2_config.name} {elapsed:8.2f}s {result.fingerprint()[:16]}")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("x", encoding="utf-8") as destination:
            destination.write(json.dumps(rows, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
