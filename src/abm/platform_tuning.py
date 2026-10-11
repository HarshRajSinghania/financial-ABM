"""Process-level tuning for long CPU-bound simulation runs."""

from __future__ import annotations

import os
import sys

_PROCESS_POWER_THROTTLING = 4
_POWER_THROTTLING_CURRENT_VERSION = 1
_POWER_THROTTLING_EXECUTION_SPEED = 0x1


def disable_power_throttling() -> bool:
    """Opt this process out of Windows EcoQoS execution-speed throttling.

    Windows may reduce background-process performance to save power.
    The performance impact depends on the machine and workload.
    This changes only the calling process and has
    no effect on other platforms. Set ``ABM_KEEP_POWER_THROTTLING=1`` to skip.
    Returns True when throttling was switched off.
    """
    if sys.platform != "win32" or os.environ.get("ABM_KEEP_POWER_THROTTLING") == "1":
        return False
    import ctypes
    from ctypes import wintypes

    class _PowerThrottlingState(ctypes.Structure):
        _fields_ = [
            ("Version", wintypes.ULONG),
            ("ControlMask", wintypes.ULONG),
            ("StateMask", wintypes.ULONG),
        ]

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.GetCurrentProcess.restype = wintypes.HANDLE
    kernel32.SetProcessInformation.argtypes = [
        wintypes.HANDLE,
        ctypes.c_int,
        ctypes.c_void_p,
        wintypes.DWORD,
    ]
    kernel32.SetProcessInformation.restype = wintypes.BOOL
    state = _PowerThrottlingState(
        _POWER_THROTTLING_CURRENT_VERSION,
        _POWER_THROTTLING_EXECUTION_SPEED,
        0,
    )
    return bool(
        kernel32.SetProcessInformation(
            kernel32.GetCurrentProcess(),
            _PROCESS_POWER_THROTTLING,
            ctypes.byref(state),
            ctypes.sizeof(state),
        )
    )
