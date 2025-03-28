import logging
import sys
from pathlib import Path

try:
    import colorama
except ImportError:
    colorama = None
else:
    colorama.just_fix_windows_console()


_LOGGER = logging.getLogger("soulstruct")


class _ModuleFormatter(logging.Formatter):

    def __init__(self, base_module_name: str, fmt, style="{"):
        super().__init__(fmt, style=style)
        self.base_module_name = base_module_name
        self.module_dir = f"\\{self.base_module_name}\\"  # for relative module path

    def format(self, record):
        """Modify record with color information before formatting it to a message."""
        if self.module_dir in record.pathname:
            relative_module = record.pathname.split(self.module_dir, 1)[-1].replace("\\", ".").removesuffix(".py")
            record.modulepath = f"{self.base_module_name}.{relative_module}"
        else:
            record.modulepath = record.pathname
        return super().format(record)


class _ColoredModuleFormatter(_ModuleFormatter):
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    COLORS = {"DEBUG": BLUE, "INFO": CYAN, "WARNING": YELLOW, "CRITICAL": YELLOW, "ERROR": RED}
    COLOR_CODES = {
        "$COLOR": "\033[0;{:d}m",
        "$BOLD_COLOR": "\033[1;{:d}m",
    }
    OTHER_CODES = {
        "$RESET": "\033[0m",
    }

    def __init__(self, base_module_name: str, fmt, style="{", use_color=True):
        super().__init__(base_module_name, fmt, style=style)
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


CONSOLE_FORMATTER: _ColoredModuleFormatter | None = None
CONSOLE_HANDLER: logging.StreamHandler | None = None
FILE_FORMATTER: _ModuleFormatter | None = None
FILE_HANDLER: logging.FileHandler | None = None


def set_up_logging():
    global CONSOLE_FORMATTER, CONSOLE_HANDLER, FILE_FORMATTER, FILE_HANDLER

    _LOGGER.setLevel(1)  # All filtering is done by handlers.

    CONSOLE_FORMATTER = _ColoredModuleFormatter(
        base_module_name="soulstruct",
        fmt="$COLOR{levelname:>7} :: {modulepath:<40} :: {lineno:>4d} :: {message}$RESET",
        style="{",
        use_color=bool(colorama),
    )
    _path_source = sys.executable if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS") else __file__
    CONSOLE_HANDLER = logging.StreamHandler()
    CONSOLE_HANDLER.setFormatter(CONSOLE_FORMATTER)
    CONSOLE_HANDLER.setLevel(logging.INFO)  # default
    _LOGGER.addHandler(CONSOLE_HANDLER)

    FILE_FORMATTER = _ModuleFormatter(
        base_module_name="soulstruct",
        fmt="{levelname:>7} :: {asctime} :: {pathname:<35} :: Line {lineno:>4d} :: {message}",
        style="{",
    )
    log_path = str(Path(_path_source).parent / "soulstruct.log")
    FILE_HANDLER = logging.FileHandler(log_path, mode="w", encoding="shift_jis_2004")
    FILE_HANDLER.setFormatter(FILE_FORMATTER)
    FILE_HANDLER.setLevel(logging.DEBUG)  # default
    _LOGGER.addHandler(FILE_HANDLER)

    def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            # Use default `excepthook` for KeyboardInterrupts.
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
        else:
            _LOGGER.critical("Unhandled exception: ", exc_info=(exc_type, exc_value, exc_traceback))

    sys.excepthook = handle_unhandled_exception

    # NOTE: Disabled, as it's annoying with `multiprocessing`.
    # _LOGGER.info(
    #     f"Log file {LOG_PATH} opened with level {logging.getLevelName(FILE_HANDLER.level)} ({FILE_HANDLER.level})."
    # )

    if not colorama:
        _LOGGER.info(
            "Install `colorama` in your Python environment with `python -m pip install colorama` to enable colorful "
            "console output."
        )


# Only set up once (e.g. not every time we reload Blender scripts).
if not _LOGGER.hasHandlers():
    set_up_logging()
