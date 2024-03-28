__all__ = [
    "DEFAULT_PROJECT_PATH",
    "DEFAULT_TEXT_EDITOR_FONT_SIZE",
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

    "GET_CONFIG",
    "SET_CONFIG",
]

import json
import logging
import sys
import typing as tp
from pathlib import Path

_LOGGER = logging.getLogger("soulstruct")

_DEFAULT_STEAM_PATH = r"Z:\home\astrale\.steam\steam\steamapps\common"
_CONFIG_DEFAULTS = {
    "DEFAULT_PROJECT_PATH": r"Z:\home\astrale\Bureau\moddingDS",
    "DEFAULT_TEXT_EDITOR_FONT_SIZE": 14,
    "DES_PATH": r"C:\Demon's Souls\PS3_GAME\USRDIR",
    "DESR_PATH": r"C:\Demon's Souls Remake\dvdroot_ps5",
    "PTDE_PATH": _DEFAULT_STEAM_PATH + r"\Dark Souls Prepare to Die Edition\DATA",
    "DSR_PATH": _DEFAULT_STEAM_PATH + r"\DARK SOULS REMASTERED",
    "DS2_PATH": _DEFAULT_STEAM_PATH + r"\Dark Souls II\Game",
    "DS2_SOTFS_PATH": _DEFAULT_STEAM_PATH + r"\Dark Souls II Scholar of the First Sin\Game",
    "BB_PATH": r"C:\Bloodborne\dvdroot_ps4",
    "DS3_PATH": _DEFAULT_STEAM_PATH + r"\DARK SOULS III\Game",
    "SEKIRO_PATH": _DEFAULT_STEAM_PATH + r"\Sekiro",  # TODO: 'Game'?
    "ELDEN_RING_PATH": _DEFAULT_STEAM_PATH + r"\ELDEN RING\Game",
    "PARAMDEX_PATH": "",  # will default to PACKAGE_PATH
}


def GET_CONFIG() -> dict[str, tp.Any]:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        # Look for `soulstruct_config.json` next to PyInstaller executable.
        config_path = Path(sys.executable).parent / "soulstruct_config.json"
        if not config_path.exists:
            raise FileNotFoundError(f"Could not find 'soulstruct_config.json' next to Soulstruct executable.")
    else:
        # Look for `soulstruct_config.json` in `soulstruct` package.
        config_path = Path(__file__).parent / "soulstruct_config.json"
        if not config_path.exists:
            raise FileNotFoundError(f"Could not find 'soulstruct_config.json' in Soulstruct package.")
    with config_path.open("r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as ex:
            raise json.JSONDecodeError(
                f"Error while loading 'soulstruct_config.json': {ex.msg}", "soulstruct_config.json", ex.lineno
            )


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
    config_dir = Path(sys.executable if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS") else __file__).parent
    with (config_dir / "soulstruct_config.json").open("w") as f:
        json.dump(config, f, indent=4)


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

DEFAULT_PROJECT_PATH = __config.get("DEFAULT_PROJECT_PATH")
DEFAULT_TEXT_EDITOR_FONT_SIZE = __config.get("DEFAULT_TEXT_EDITOR_FONT_SIZE")
DES_PATH = __config.get("DES_PATH")
DESR_PATH = __config.get("DESR_PATH")
PTDE_PATH = __config.get("PTDE_PATH")
DSR_PATH = __config.get("DSR_PATH")
DS2_PATH = __config.get("DS2_PATH")
DS2_SOTFS_PATH = __config.get("DS2_SOTFS_PATH")
BB_PATH = __config.get("BB_PATH")
DS3_PATH = __config.get("DS3_PATH")
SEKIRO_PATH = __config.get("SEKIRO_PATH")
ELDEN_RING_PATH = __config.get("ELDEN_RING_PATH")
PARAMDEX_PATH = __config.get("PARAMDEX_PATH")
