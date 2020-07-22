import importlib.util
import logging
import sys
from pathlib import Path

_LOGGER = logging.getLogger(__name__)

_DEFAULT_STEAM_PATH = "C:\\\\Program Files (x86)\\\\Steam\\\\steamapps\\\\common\\\\"
_CONFIG_DEFAULTS = {
    "DEFAULT_PROJECT_PATH": '""',
    "STEAM_PATH": f'"{_DEFAULT_STEAM_PATH}"',
    "PTDE_PATH": 'STEAM_PATH + "Dark Souls Prepare to Die Edition\\\\DATA"',
    "DSR_PATH": 'STEAM_PATH + "DARK SOULS REMASTERED"',
    "DS2_PATH": 'STEAM_PATH + "Dark Souls II\\\\Game"',
    "DS2_SOTFS_PATH": 'STEAM_PATH + "Dark Souls II Scholar of the First Sin\\\\Game"',
    "DS3_PATH": 'STEAM_PATH + "DARK SOULS III\\\\Game"',
    "SEKIRO_PATH": 'STEAM_PATH + "Sekiro"',
    "ELDEN_RING_PATH": 'STEAM_PATH + "Elden Ring"',
}


def GET_CONFIG():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        spec = importlib.util.spec_from_file_location("config", str(Path(sys.executable).parent / "config.py"))
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
    else:
        try:
            from . import config
        except ImportError:
            raise ImportError("`config.py` module not found in Soulstruct package.")
    return {k: getattr(config, k) for k in dir(config) if k[:2] != "__"}


def SET_CONFIG(**kwargs):
    """Update `config.py` with the given keyword arguments.

    Omitted arguments default to their current values, or their given default values (above) if no current value exists.
    """
    config = {}
    use_quotes = {}
    try:
        current_config = GET_CONFIG()
    except (ImportError, FileNotFoundError, ModuleNotFoundError):
        current_config = {}
    for k, default_value in _CONFIG_DEFAULTS.items():
        if k in kwargs:
            config[k] = kwargs[k]
            use_quotes[k] = True
        elif k in current_config:
            config[k] = current_config[k]
            use_quotes[k] = True
        else:
            config[k] = default_value
            use_quotes[k] = False
    config_string = "\n".join(f'{k} = "{v}"' if use_quotes[k] else f"{k} = {v}" for k, v in config.items())
    this_path = sys.executable if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS") else __file__
    config_path = Path(this_path).parent / "config.py"
    with config_path.open("w") as f:
        f.write(config_string + "\n")
    return config


try:
    __config = GET_CONFIG()
except (ImportError, FileNotFoundError, ModuleNotFoundError):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        _LOGGER.info(
            "Creating default `config.py` file next to Soulstruct executable.\n"
            "Set your game directories in here for ease of use, including a default project path if desired."
        )
    else:
        _LOGGER.info(
            f"Creating default `config.py` file in `soulstruct` package: {str(Path(__file__).parent)}.\n"
            f"Set your game directories in here for ease of use, including a default project path if desired."
        )
    __config = SET_CONFIG()
DEFAULT_PROJECT_PATH = __config.get("DEFAULT_PROJECT_PATH")
STEAM_PATH = __config.get("STEAM_PATH")
PTDE_PATH = __config.get("PTDE_PATH")
DSR_PATH = __config.get("DSR_PATH")
DS2_PATH = __config.get("DS2_PATH")
DS2_SOTFS_PATH = __config.get("DS2_SOTFS_PATH")
DS3_PATH = __config.get("DS3_PATH")
SEKIRO_PATH = __config.get("SEKIRO_PATH")
ELDEN_RING_PATH = __config.get("ELDEN_RING_PATH")
