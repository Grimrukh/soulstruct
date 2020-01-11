import importlib.util
import sys
from pathlib import Path

from .project import SoulstructProject
from .bnd import BND
from .dcx import DCX


try:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        spec = importlib.util.spec_from_file_location("config", str(Path(sys.executable).parent / "config.py"))
        config = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config)
        try:
            DSR_PATH = config.DSR_PATH
            PTDE_PATH = config.PTDE_PATH
            DEFAULT_PROJECT_PATH = config.DEFAULT_PROJECT_PATH
        except AttributeError as e:
            raise ImportError(str(e))
    else:
        from .config import DSR_PATH, PTDE_PATH, DEFAULT_PROJECT_PATH
except (ImportError, FileNotFoundError, ModuleNotFoundError) as e:
    PTDE_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA"
    DSR_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\DARK SOULS REMASTERED"
    DEFAULT_PROJECT_PATH = None
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        print("# Creating default `config.py` file next to Soulstruct executable.\n"
              "# Set your game directories in here for ease of use, including a default project path if desired.")
        config_path = Path(sys.executable).parent / "config.py"
    else:
        print("# Creating default `config.py` file in `soulstruct` package.\n"
              "# Set your game directories in here for ease of use, including a default project path if desired.")
        config_path = Path(__file__).parent / "config.py"
    with config_path.open('w') as f:
        f.write(
            f"PTDE_PATH = {repr(PTDE_PATH)}\n"
            f"DSR_PATH = {repr(DSR_PATH)}\n"
            f"DEFAULT_PROJECT_PATH = {repr(DEFAULT_PROJECT_PATH)}\n"
        )
