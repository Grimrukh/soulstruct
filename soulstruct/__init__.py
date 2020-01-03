from .project import SoulstructProject
from .bnd import BND
from .dcx import DCX

try:
    from .config import DSR_PATH, PTDE_PATH, DEFAULT_PROJECT_PATH
except ImportError:
    print("# Creating default `config.py` template in soulstruct. Set your game directories in here for ease of use.")
    from pathlib import Path
    PTDE_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA"
    DSR_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\DARK SOULS REMASTERED"
    DEFAULT_PROJECT_PATH = str(Path("~\\Documents\\Dark Souls\\soulstruct-projects\\my_project").expanduser())
    with (Path(__file__).parent / 'config.py').open('w') as f:
        f.write(
            f"PTDE_PATH = {repr(PTDE_PATH)}\n"
            f"DSR_PATH = {repr(DSR_PATH)}\n"
            f"DEFAULT_PROJECT_PATH = {repr(DEFAULT_PROJECT_PATH)}\n"
        )
