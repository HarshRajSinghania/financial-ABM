"""Run the whole stage D.2 pipeline unattended: the common baseline, then the four scenarios in parallel.

Meant to be started detached from any terminal session; progress goes to runs/v2/pipeline.log. Stops
before the scenarios if the baseline did not complete. Each step's log is runs/v2/<step>.log.
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGS = HERE / "runs" / "v2"
PYTHON = sys.executable


def log(message: str) -> None:
    with (LOGS / "pipeline.log").open("a", encoding="utf-8") as handle:
        handle.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {message}\n")


def start(*arguments: str) -> subprocess.Popen:
    name = "_".join(arguments[1:]) or arguments[0]
    handle = (LOGS / f"{name if arguments[0] == 'scenario' else arguments[0]}.log").open("w", encoding="utf-8")
    return subprocess.Popen([PYTHON, str(HERE / "run_stage_d.py"), *arguments], cwd=HERE, stdout=handle,
                            stderr=subprocess.STDOUT)


def main() -> int:
    LOGS.mkdir(parents=True, exist_ok=True)
    log("baseline started")
    code = start("baseline").wait()
    log(f"baseline finished with exit code {code}")
    if code != 0:
        return code
    processes = {name: start("scenario", name) for name in ("B", "I", "F", "IF")}
    log("scenarios started: " + ", ".join(processes))
    codes = {name: process.wait() for name, process in processes.items()}
    log(f"scenarios finished: {codes}")
    return max(codes.values())


if __name__ == "__main__":
    raise SystemExit(main())
