"""Run the unchanged stage B diagnosis scripts on the saturated grid, writing outputs here.

The scripts in ../disclosure_fixed_fine_diagnosis_20261013 keep their recorded hashes; this wrapper only
redirects their grid and output paths. The redirection sits at module level, so the worker processes that
diagnose.py spawns pick it up as well.

Usage: python rerun_stage_b_scripts.py [--workers N]
"""

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent / "disclosure_fixed_fine_diagnosis_20261013"))

import diagnose  # noqa: E402
import grid_tables  # noqa: E402
import saturation  # noqa: E402

GRID = ROOT / "reports/disclosure_csi300_fixed_fine_saturated_development_20261013_v1"
for module in (diagnose, grid_tables, saturation):
    module.GRID = GRID
    module.HERE = HERE
saturation.DOMAIN = ROOT / "configs/domains/csi300_huazheng_esg_quantile_copula_fixed_fine_saturated.json"


if __name__ == "__main__":
    grid_tables.main()
    workers = sys.argv[sys.argv.index("--workers") + 1] if "--workers" in sys.argv else "12"
    sys.argv = [sys.argv[0], "--workers", workers]
    diagnose.main()
    saturation.main()
