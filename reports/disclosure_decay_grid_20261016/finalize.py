"""Write the grid summary with the stock runner, avoiding the hung WMI query (see _no_wmi.py).

  python reports/disclosure_decay_grid_20261016/finalize.py --spec configs/disclosure_decay_grid_v1.json \
      --output reports/disclosure_decay_grid_20261016/grid_v1 --workers 1 --resume

Arguments go straight to abm.disclosure.experiments. With every trial complete, --resume starts no trial: it checks
the frozen identity, collects the records, writes summary.json and renders the report.
"""

from __future__ import annotations

import sys

from _no_wmi import prefill_uname

prefill_uname()

from abm.disclosure.experiments import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
