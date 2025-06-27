__all__ = [
    "DES_PATH",
    "DESR_PATH",
    "PTDE_PATH",
    "DSR_PATH",
    "DS2_PATH",
    "DS2_SOTFS_PATH",
    "BB_PATH",
    "DS3_PATH",
    "SEKIRO_PATH",
    "ELDEN_RING_PATH",

    "PARAMDEX_PATH",
    "LOG_PATH",
    "CONSOLE_LOG_LEVEL",
    "FILE_LOG_LEVEL",

    "GET_CONFIG",
    "SET_CONFIG",
]

import json
import logging
import sys
import typing as tp
from pathlib import Path

_LOGGER = logging.getLogger(__name__)

_DEFAULT_STEAM_PATH = Path(r"C:/Program Files (x86)/Steam/steamapps/common")
_SOULSTRUCT_APPDATA = Path("~/AppData/Roaming/soulstruct").expanduser()
_CONFIG_DEFAULTS = {
    "DES_PATH": Path(r"C:/Demon's Souls/PS3_GAME/USRDIR"),
    "DESR_PATH": Path(r"C:/Demon's Souls Remake/dvdroot_ps5"),
    "PTDE_PATH": _DEFAULT_STEAM_PATH / "Dark Souls Prepare to Die Edition/DATA",
    "DSR_PATH": _DEFAULT_STEAM_PATH / "DARK SOULS REMASTERED",
    "DS2_PATH": _DEFAULT_STEAM_PATH / "Dark Souls II/Game",
    "DS2_SOTFS_PATH": _DEFAULT_STEAM_PATH / "Dark Souls II Scholar of the First Sin/Game",
    "BB_PATH": Path("C:/Bloodborne/dvdroot_ps4"),
    "DS3_PATH": _DEFAULT_STEAM_PATH / "DARK SOULS III/Game",
    "SEKIRO_PATH": _DEFAULT_STEAM_PATH / "Sekiro",  # TODO: 'Game'?
    "ELDEN_RING_PATH": _DEFAULT_STEAM_PATH / "ELDEN RING/Game",
    "PARAMDEX_PATH": "",  # will default to SOULSTRUCT_PATH
    "AUTO_SETUP_LOG": True,
    "LOG_PATH": _SOULSTRUCT_APPDATA / "soulstruct.log",
    "CONSOLE_LOG_LEVEL": "INFO",
    "FILE_LOG_LEVEL": "DEBUG",
}


def GET_CONFIG() -> dict[str, tp.Any]:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        # Look for `soulstruct_config.json` next to PyInstaller executable.
        config_path = Path(sys.executable).parent / "soulstruct_config.json"
        if not config_path.exists:
            raise FileNotFoundError(f"Could not find 'soulstruct_config.json' next to Soulstruct executable.")
    else:
        # Look for `soulstruct_config.json` in user data.
        config_path = _SOULSTRUCT_APPDATA / "soulstruct_config.json"
        if not config_path.exists:
            raise FileNotFoundError(f"Could not find 'soulstruct_config.json' in user data: {config_path}.")
    with config_path.open("r") as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError as ex:
            raise json.JSONDecodeError(
                f"Error while loading 'soulstruct_config.json': {ex.msg}", "soulstruct_config.json", ex.lineno
            )
    # For keys ending in '_PATH', convert to Path objects.
    for k, v in config.items():
        if k.endswith("_PATH"):
            config[k] = Path(v)

    return config


def SET_CONFIG(**kwargs):
    """Update `soulstruct_config.json` with the given keyword arguments.

    Omitted arguments default to their current values, or their given default values (above) if no current value exists.
    """
    try:
        config = GET_CONFIG()
    except json.JSONDecodeError:
        _LOGGER.error("Error encountered while loading 'soulstruct_config.json'. Try fixing or deleting it.")
        raise
    except FileNotFoundError:
        config = {}
    for k, default_value in _CONFIG_DEFAULTS.items():
        if k in kwargs:
            config[k] = kwargs.pop(k)
        else:
            config.setdefault(k, default_value)
    if kwargs:
        raise KeyError(f"Invalid config key(s): {list(kwargs)}")

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        config_path = Path(sys.executable).parent / "soulstruct_config.json"
    else:
        config_path = _SOULSTRUCT_APPDATA / "soulstruct_config.json"

    # Convert all Path objects to strings for JSON serialization.
    config_json = {
        k: str(v) if isinstance(v, Path) else v for k, v in config.items()
    }
    with config_path.open("w") as f:
        json.dump(config_json, f, indent=4)

try:
    __config = GET_CONFIG()
except FileNotFoundError:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        _LOGGER.info(
            "Creating default `soulstruct_config.json` file next to Soulstruct executable.\n"
            f"Set your game directories and other Soulstruct settings in here."
        )
    else:
        _LOGGER.info(
            f"Creating default `soulstruct_config.json` file in `soulstruct` package: {str(Path(__file__).parent)}.\n"
            f"Set your game directories and other Soulstruct settings in here."
        )
    SET_CONFIG()
    __config = GET_CONFIG()
else:
    if len(__config) != len(_CONFIG_DEFAULTS):
        # Make sure we write and reload to get (and save) default values.
        SET_CONFIG()
        __config = GET_CONFIG()

DES_PATH = __config.get("DES_PATH")  # type: Path
DESR_PATH = __config.get("DESR_PATH")  # type: Path
PTDE_PATH = __config.get("PTDE_PATH")  # type: Path
DSR_PATH = __config.get("DSR_PATH")  # type: Path
DS2_PATH = __config.get("DS2_PATH")  # type: Path
DS2_SOTFS_PATH = __config.get("DS2_SOTFS_PATH")  # type: Path
BB_PATH = __config.get("BB_PATH")  # type: Path
DS3_PATH = __config.get("DS3_PATH")  # type: Path
SEKIRO_PATH = __config.get("SEKIRO_PATH")  # type: Path
ELDEN_RING_PATH = __config.get("ELDEN_RING_PATH")  # type: Path
PARAMDEX_PATH = __config.get("PARAMDEX_PATH")  # type: Path

LOG_PATH = __config.get("LOG_PATH")  # type: Path
CONSOLE_LOG_LEVEL = __config.get("CONSOLE_LOG_LEVEL")  # type: str
FILE_LOG_LEVEL = __config.get("FILE_LOG_LEVEL")  # type: str

def _auto_setup_log():
    # Automatically set up logging if this is enabled in the config.
    from soulstruct.logging_utils import setup

    setup(
        console_level=CONSOLE_LOG_LEVEL,
        file_level=FILE_LOG_LEVEL,
        log_path=LOG_PATH,
        rich_tracebacks=True,  # always use Rich tracebacks
        clear_old_handlers=True,
    )


if __config.get("AUTO_SETUP_LOG"):
    _auto_setup_log()
