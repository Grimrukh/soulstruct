import importlib.util
import logging
import sys
from pathlib import Path

_LOGGER = logging.getLogger(__name__)


def GET_CONFIG():
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        spec = importlib.util.spec_from_file_location("config", str(Path(sys.executable).parent / "config.py"))
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
    else:
        from . import config
    try:
        return config.PTDE_PATH, config.DSR_PATH, config.DEFAULT_PROJECT_PATH
    except AttributeError as e:
        raise ImportError(str(e))


def SET_CONFIG(ptde_path=None, dsr_path=None, default_project_path=None):
    if ptde_path is None or dsr_path is None or default_project_path is None:
        current_ptde_path, current_dsr_path, current_default_project_path = GET_CONFIG()
        if ptde_path is None:
            ptde_path = current_ptde_path
        if dsr_path is None:
            dsr_path = current_dsr_path
        if default_project_path is None:
            default_project_path = current_default_project_path
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        config_path = Path(sys.executable).parent / "config.py"
    else:
        config_path = Path(__file__).parent / "config.py"
    with config_path.open('w') as f:
        f.write(
            f"PTDE_PATH = {repr(ptde_path)}\n"
            f"DSR_PATH = {repr(dsr_path)}\n"
            f"DEFAULT_PROJECT_PATH = {repr(default_project_path)}\n"
        )

    return ptde_path, dsr_path, default_project_path


try:
    PTDE_PATH, DSR_PATH, DEFAULT_PROJECT_PATH = GET_CONFIG()
except (ImportError, FileNotFoundError, ModuleNotFoundError):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        _LOGGER.info(
            "Creating default `config.py` file next to Soulstruct executable.\n"
            "Set your game directories in here for ease of use, including a default project path if desired.")
    else:
        _LOGGER.info(
            f"Creating default `config.py` file in `soulstruct` package: {str(Path(__file__).parent)}.\n"
            f"# Set your game directories in here for ease of use, including a default project path if desired.")
    PTDE_PATH, DSR_PATH, DEFAULT_PROJECT_PATH = SET_CONFIG(
        ptde_path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA",
        dsr_path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\DARK SOULS REMASTERED",
        default_project_path="",
    )
