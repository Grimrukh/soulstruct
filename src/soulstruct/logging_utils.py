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
import os
import sys
import typing as tp
from pathlib import Path

from rich.console import Console
from rich.traceback import install as rich_tb

if tp.TYPE_CHECKING:
    from rich.console import Console

# Console and file format strings for log records.
_CONSOLE_FMT = "{level_col} ┃ {modulepath:<40} ┃ {lineno:>4d} ┃ {message}"
_FILE_FMT    = "{asctime} ┃ {levelname:>7} ┃ {pathname:<35} ┃ line {lineno:>4d} ┃ {message}"


_CONSOLE = Console(soft_wrap=True)


class BasicRichHandler(logging.Handler):

    def emit(self, record: logging.LogRecord):
        _CONSOLE.print(self.format(record))


class _SoulstructFormatter(logging.Formatter):
    """Adds `modulepath` and colorised `level_col` only for this handler."""

    _LEVEL_COLORS: dict[str, str] = {
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold red",
    }

    def __init__(
        self,
        base_module_name: str,
        fmt: str,
        *,
        style: tp.Literal['%', '$', '{'] = "{",
        color: bool = False,
    ):
        super().__init__(fmt, style=style)
        self._base_tag = f"{os.sep}{base_module_name}{os.sep}"
        self._base_name = base_module_name
        self._use_color = color

    def format(self, record: logging.LogRecord) -> str:
        if self._base_tag in record.pathname:
            relative = (
                record.pathname.split(self._base_tag, 1)[-1]
                .replace(os.sep, ".")
                .removesuffix(".py")
            )
            record.modulepath = f"{self._base_name}.{relative}"
        else:
            record.modulepath = record.pathname

        # Module path links to file and line number.
        record.modulepath = (
            f"[link={Path(record.pathname).as_uri()}:{record.lineno}]"
            f"{record.modulepath}"
            f"[/link]"
        )
        # NOTE: The string pattern 'File {path}, line {line}' in JetBrains will automatically generate an IDE link.

        if self._use_color:
            color = self._LEVEL_COLORS.get(record.levelname, "white")
            record.level_col = f"[{color}]{record.levelname:>7}[/]"
        else:
            record.level_col = f"{record.levelname:>7}"

        return super().format(record)


def setup(
    *,  # keyword-only args
    console_level: str | int = "INFO",
    file_level: str | int = "DEBUG",
    log_path: str | Path | None = None,
    rich_tracebacks: bool = True,
    clear_old_handlers=True,
    base_logger: logging.Logger | None = None,
    base_module_name="soulstruct",
) -> tuple[BasicRichHandler, logging.FileHandler | None]:
    """
    Configure Soulstruct logging.

    Args:
        console_level: Logging level for the colored console output.
        file_level: Logging level for the plain text file output (ignored if *log_path* is None).
        log_path: Path to the log file. If None, no file handler is created.
        rich_tracebacks: If True, install Rich's pretty traceback hook.
        clear_old_handlers: If False, do not clear all old handlers from library's base logger.
        base_logger: If provided, use this logger instead of the default *soulstruct* logger.
        base_module_name: The base module name to use for the logger (default is "soulstruct"). This is used to add a
            'modulepath' attribute to log records, which is the module path relative to the base module name. It is also
            used to find the base logger if *base_logger* is None.

    Returns:
        (console_handler, file_handler): The two handlers added to the *soulstruct* logger.  *file_handler* is
        None if *log_path* was None.
    """
    logger = base_logger or logging.getLogger(base_module_name)
    logger.setLevel(logging.NOTSET)  # let handlers filter

    if clear_old_handlers:
        # Clear all old handlers from the logger, so we don't get duplicate messages.
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)

    # --------------------------- console handler ----------------------------
    console_handler = BasicRichHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(_SoulstructFormatter(base_module_name, _CONSOLE_FMT, color=True))
    logger.addHandler(console_handler)

    # File handler.
    file_handler: logging.FileHandler | None = None
    if log_path is not None:
        log_path = Path(log_path)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
        file_handler.setLevel(file_level)
        file_handler.setFormatter(_SoulstructFormatter(base_module_name, _FILE_FMT, color=False))
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
