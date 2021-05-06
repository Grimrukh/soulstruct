import logging
import sys
from pathlib import Path

try:
    import colorama
except ImportError:
    colorama = None
else:
    colorama.init()


class _ColoredFormatter(logging.Formatter):
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    COLORS = {"DEBUG": BLUE, "INFO": CYAN, "WARNING": YELLOW, "CRITICAL": YELLOW, "ERROR": RED}
    COLOR_CODES = {
        "$COLOR": "\033[0;{:d}m",
        "$BOLD_COLOR": "\033[1;{:d}m",
    }
    OTHER_CODES = {
        "$RESET": "\033[0m",
    }

    def __init__(self, fmt, style="{", use_color=True):
        super().__init__(fmt, style=style)
        self.use_color = use_color

    def format(self, record):
        """Modify record with color information before formatting it to a message."""
        s = super().format(record)
        if self.use_color:
            color = 30 + self.COLORS.get(record.levelname, self.WHITE)  # default to white
            for tag, code in self.COLOR_CODES.items():
                s = s.replace(tag, code.format(color))
            for tag, code in self.OTHER_CODES.items():
                s = s.replace(tag, code)
        else:
            s = s.replace("$RESET", "")
            for tag in self.COLOR_CODES.keys():
                s = s.replace(tag, "")
            for tag in self.OTHER_CODES.keys():
                s = s.replace(tag, "")
        return s


CONSOLE_FORMATTER = _ColoredFormatter(
    fmt="$COLOR{levelname:>7} :: $BOLD_COLOR{asctime}$COLOR :: {name:<45} :: Line {lineno:>4d} :: {message}$RESET",
    style="{",
    use_color=bool(colorama),
)
_path_source = sys.executable if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS") else __file__
CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(CONSOLE_FORMATTER)
CONSOLE_HANDLER.setLevel(logging.INFO)  # default
LOG_PATH = str(Path(_path_source).parent / "soulstruct.log")
FILE_FORMATTER = logging.Formatter(
    fmt="{levelname:>7} :: {asctime} :: {name:<35} :: Line {lineno:>4d} :: {message}", style="{"
)
FILE_HANDLER = logging.FileHandler(LOG_PATH, mode="w", encoding="shift_jis_2004")
FILE_HANDLER.setFormatter(FILE_FORMATTER)
FILE_HANDLER.setLevel(logging.DEBUG)  # default

_LOGGER = logging.getLogger("soulstruct")
_LOGGER.setLevel(1)  # All filtering is done by handlers.
_LOGGER.addHandler(CONSOLE_HANDLER)
_LOGGER.addHandler(FILE_HANDLER)

_LOGGER.info(
    f"Log file {LOG_PATH} opened with level {logging.getLevelName(FILE_HANDLER.level)} ({FILE_HANDLER.level})."
)
if not colorama:
    _LOGGER.info(
        f"Install `colorama` in your Python environment with `python -m pip install colorama` to enable colorful "
        f"console output."
    )
