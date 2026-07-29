"""Optional progress reporting for long directory-wide operations.

Loading or writing a project's Maps/Params/Text can take tens of seconds and involves hundreds of files, so callers
that have a UI (`soulstruct-gui`) need to know which file is being handled and how far through the batch they are.
This module deliberately defines nothing but a callable signature: `soulstruct` should not know or care whether the
other end is a progress bar, a log, or nothing at all.

The callback is invoked as `progress(current, total, label)`:

- `current`: number of items **completed** so far, so the first call in a batch is `(0, total, <first item>)` and the
  last is `(total, total, "")`.
- `total`: number of items in the batch. Fixed for the duration of one call. Two-phase operations (e.g. serialize-then-
  write) count each phase separately, so the bar advances monotonically instead of resetting halfway.
- `label`: the item about to be handled (usually a file stem), or `""`.

A callback may raise to cancel the operation; library code does not catch exceptions from it, so a partially written
directory is the caller's problem to clean up.
"""
from __future__ import annotations

__all__ = ["ProgressCallback", "report_progress"]

import typing as tp

ProgressCallback = tp.Callable[[int, int, str], None]


def report_progress(progress: ProgressCallback | None, current: int, total: int, label: str = "") -> None:
    """Call `progress`, if given. Exists so call sites stay one line and never need a `None` check."""
    if progress is not None:
        progress(current, total, label)
