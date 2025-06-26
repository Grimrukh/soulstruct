"""
Rich-based logging setup for the `soulstruct` package:

```
import soulstruct.logging_utils as slog

# in your script or CLI entry point (e.g. `soulstruct.__main__`)
console_h, file_h = slog.setup(
    console_level="INFO",    # or int
    file_level="DEBUG",
    log_path="soulstruct.log",   # None -> no file handler
)
```

Or inside library code:

```
import logging
log = logging.getLogger(__name__)
log.info("Hello")
```

No side effects occur until `setup()` is invoked.
"""
from __future__ import annotations

__all__ = [
    "setup",
]

import logging
import sys
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install as rich_tb

_BASE_MODULE_NAME = "soulstruct"

# Console and file format strings for log records.
_CONSOLE_FMT = "{levelname:>7} ┃ {modulepath:<40} ┃ {lineno:>4d} ┃ {message}"
_FILE_FMT    = "{asctime} ┃ {levelname:>7} ┃ {pathname:<35} ┃ line {lineno:>4d} ┃ {message}"

# LogRecord factory to inject `modulepath` once per record                     #
_default_factory = logging.getLogRecordFactory()


def _record_factory(*args, **kwargs):  # type: ignore[override]
    record: logging.LogRecord = _default_factory(*args, **kwargs)
    path_tag = f"\\{_BASE_MODULE_NAME}\\"
    if path_tag in record.pathname:
        relative = (
            record.pathname.split(path_tag, 1)[-1]
            .replace("\\", ".")
            .removesuffix(".py")
        )
        record.modulepath = f"{_BASE_MODULE_NAME}.{relative}"
    else:
        record.modulepath = record.pathname
    return record


logging.setLogRecordFactory(_record_factory)

# Ensure library emits safely even if host never calls `setup()`.
logging.getLogger(_BASE_MODULE_NAME).addHandler(logging.NullHandler())


def setup(
    *,  # keyword-only args
    console_level: str | int = "INFO",
    file_level: str | int = "DEBUG",
    log_path: str | Path | None = None,
    rich_tracebacks: bool = True,
    clear_old_handlers=True,
) -> tuple[RichHandler, logging.FileHandler | None]:
    """
    Configure Soulstruct logging.

    Args:
        console_level: Logging level for the coloured console output.
        file_level: Logging level for the plain text file output (ignored if *log_path* is None).
        log_path: Path to the log file.  If None, no file handler is created.
        rich_tracebacks: If True, install Rich's pretty traceback hook.
        clear_old_handlers: If False, do not clear all old handlers from library's base logger.

    Returns:
        (console_handler, file_handler): The two handlers added to the *soulstruct* logger.  *file_handler* is
        None if *log_path* was None.
    """
    logger = logging.getLogger(_BASE_MODULE_NAME)
    logger.setLevel(logging.NOTSET)  # let handlers filter

    if clear_old_handlers:
        # Clear all old handlers from the logger, so we don't get duplicate messages.
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

    # --------------------------- console handler ----------------------------
    console = Console()
    console_handler = RichHandler(
        console=console,
        markup=False,  # we're formatting plaintext, no [tags]
        show_time=False,
        show_level=False,
        show_path=False,
        rich_tracebacks=False,  # we install tracebacks globally below
    )
    console_handler.setLevel(console_level)
    console_handler.setFormatter(logging.Formatter(_CONSOLE_FMT, style="{"))
    logger.addHandler(console_handler)

    # File handler.
    file_handler: logging.FileHandler | None = None
    if log_path is not None:
        log_path = Path(log_path)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
        file_handler.setLevel(file_level)
        file_handler.setFormatter(logging.Formatter(_FILE_FMT, style="{"))
        logger.addHandler(file_handler)

    # Pretty tracebacks.
    if rich_tracebacks:
        rich_tb(show_locals=False)

    # Unhandled exception hook.
    def _excepthook(exc_type, exc_val, exc_tb):
        if issubclass(exc_type, KeyboardInterrupt):
            # Keep default behaviour for Ctrl-C
            sys.__excepthook__(exc_type, exc_val, exc_tb)
        else:
            logger.critical("Unhandled exception:", exc_info=(exc_type, exc_val, exc_tb))

    sys.excepthook = _excepthook

    return console_handler, file_handler
