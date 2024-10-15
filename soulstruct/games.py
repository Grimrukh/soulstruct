"""Basic information structures for all FromSoftware games used across Soulstruct.

These `Game` instances are also used as singletons for game checking."""
from __future__ import annotations

__all__ = [
    "Game",
    "GAMES",
    "get_game",
    "DEMONS_SOULS",
    "DEMONS_SOULS_REMAKE",
    "DARK_SOULS_PTDE",
    "DARK_SOULS_DSR",
    "DARK_SOULS_2",
    "DARK_SOULS_2_SOTFS",
    "BLOODBORNE",
    "DARK_SOULS_3",
    "SEKIRO",
    "ELDEN_RING",
]

import importlib
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.config import *
from soulstruct.dcx import DCXType
from soulstruct.utilities.files import PACKAGE_PATH


@dataclass(slots=True, frozen=True)
class Game:

    variable_name: str
    name: str
    submodule_name: str = ""
    aliases: tuple[str, ...] = ()
    default_dcx_type: DCXType = DCXType.Null
    special_dcx_types: dict[str, DCXType] = field(default_factory=dict)
    bundled_resource_paths: dict[str, Path] = field(default_factory=dict)
    steam_appid: int | None = None
    default_game_path: str = ""
    generic_game_path: str = ""
    save_file_path: Path | None = None
    executable_name: str = ""
    interroot_prefix: str = ""
    gadget_name: str = ""
    default_file_paths: dict[str, str] = field(default_factory=dict)

    # TODO: other file version info
    # TODO: Soulstruct event import shortcut functions, etc.

    def get_dcx_type(self, file_type: str) -> DCXType:
        return self.special_dcx_types.get(file_type, self.default_dcx_type)

    def process_dcx_path(self, path: str | Path) -> str | Path:
        """Append or remove ".dcx" to/from given path according to `default_dcx_type` and/or `special_dcx_types`.

        Should NOT be called on directories; this method will not do any sort of validation, and the default DCX type
        will end up being attached to that directory name.
        """
        is_str = isinstance(path, str)  # preserve return type
        path = Path(path)
        if path.suffix == ".dcx":
            # Remove DCX to start.
            path = path.with_name(path.stem)
        dcx_type = self.special_dcx_types.get(path.suffix, self.default_dcx_type)
        if dcx_type.has_dcx_extension():
            # Add DCX extension.
            path = path.with_name(path.name + ".dcx")
        return str(path) if is_str else path

    def import_game_submodule(self, *args) -> tp.Any:
        if not self.submodule_name:
            raise AttributeError(f"Game {self.name} does not have any submodule in Soulstruct.")
        module_name = "soulstruct." + ".".join((self.submodule_name,) + args)
        return importlib.import_module(module_name)  # will raise an `ImportError` if it fails

    def from_game_submodule_import(self, module, name: str) -> tp.Any:
        if not self.submodule_name:
            raise AttributeError(f"Game {self.name} does not have any submodule in Soulstruct.")
        module_name = f"soulstruct.{self.submodule_name}.{module}"
        module = importlib.import_module(module_name)  # will raise an `ImportError` if it fails
        try:
            return getattr(module, name)
        except AttributeError:
            raise ImportError(f"Game submodule {module_name} does not have an attribute named {name}.")

    def __hash__(self):
        return hash(self.variable_name)

    def __eq__(self, other: Game):
        return self.variable_name == other.variable_name

    def __repr__(self):
        return f"Game(\"{self.variable_name}\")"


DEMONS_SOULS = Game(
    "DEMONS_SOULS",
    "Demon's Souls",
    submodule_name="demonssouls",
    aliases=("demonssouls", "des"),
    default_dcx_type=DCXType.DCX_EDGE,
    special_dcx_types={
        ".flver": DCXType.Null,  # NOTE: '.dcx' files are also present, but most dumped debug PS3 games use the non-DCX
        ".hkx": DCXType.Null,
        ".msb": DCXType.Null,
        ".nvmbnd": DCXType.Null,
    },
    bundled_resource_paths={
        "MTDBND": PACKAGE_PATH("demonssouls/models/resources/mtd.mtdbnd.dcx"),
    },
    steam_appid=None,
    default_game_path=DES_PATH,
    executable_name="EBOOT.BIN",
    interroot_prefix="N:\\DemonsSoul\\data\\DVDROOT",
    default_file_paths={
        "AIScriptDirectory": "script",
        "DrawParamDirectory": "param/drawparam",
        "EventDirectory": "event",
        "GameParamBND": "param/gameparam/gameparam.parambnd.dcx",
        "MapStudioDirectory": "map/mapstudio",
        "MSGDirectory": "msg/ENGLISH",
        "ParamDefBND": "paramdef/paramdef.paramdefbnd.dcx",
        "TalkDirectory": "script/talk",
    },
)


DEMONS_SOULS_REMAKE = Game(
    "DEMONS_SOULS_REMAKE",
    "Demon's Souls Remake",
    aliases=("demonssoulsremake", "desr"),
    default_dcx_type=DCXType.Unknown,  # TODO: Unknown.
    default_game_path=DESR_PATH,
)


DARK_SOULS_PTDE = Game(
    "DARK_SOULS_PTDE",
    "Dark Souls: Prepare to Die Edition",
    submodule_name="darksouls1ptde",
    aliases=("darksoulspreparetodieedition", "darksoulsptde", "ptde", "darksouls1ptde"),
    default_dcx_type=DCXType.Null,  # DCX not used anywhere
    bundled_resource_paths={
        "PARAMDEFBND": PACKAGE_PATH("darksouls1ptde/params/resources/paramdef.paramdefbnd"),
        "MTDBND": PACKAGE_PATH("darksouls1ptde/models/resources/Mtd.mtdbnd"),
    },
    steam_appid=211420,
    default_game_path=PTDE_PATH,
    generic_game_path="C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA",
    save_file_path=Path("~/Documents/NBGI/DarkSouls").expanduser(),
    executable_name="DARKSOULS.exe",
    interroot_prefix="N:\\FRPG\\data\\INTERROOT_win32",
    gadget_name="DS Gadget.exe",
    default_file_paths={
        "AIScriptDirectory": "script",
        "DrawParamDirectory": "param/DrawParam",
        "EventDirectory": "event",
        "GameParamBND": "param/GameParam/GameParam.parambnd",
        "MapStudioDirectory": "map/MapStudio",
        "MSGDirectory": "msg/ENGLISH",
        "ParamDefBND": "paramdef/paramdef.paramdefbnd",
        "TalkDirectory": "script/talk",
    },
)


DARK_SOULS_DSR = Game(
    "DARK_SOULS_DSR",
    "Dark Souls: Remastered",
    submodule_name="darksouls1r",
    aliases=("darksoulsremastered", "darksoulsdsr", "dsr", "ds1r", "darksouls1r"),
    default_dcx_type=DCXType.DCX_DFLT_10000_24_9,
    special_dcx_types={
        ".msb": DCXType.Null,
        ".mcg": DCXType.Null,
        ".mcp": DCXType.Null,
        ".hkxbhd": DCXType.Null,
        ".hkxbdt": DCXType.Null,
        ".tpfbhd": DCXType.Null,
        ".tpfbdt": DCXType.Null,
    },
    bundled_resource_paths={
        "PARAMDEFBND": PACKAGE_PATH("darksouls1r/params/resources/darksouls1r.paramdefbnd.dcx"),
        "MTDBND": PACKAGE_PATH("darksouls1r/models/resources/Mtd.mtdbnd.dcx"),
        "PATCH_MTDBND": PACKAGE_PATH("darksouls1r/models/resources/MtdPatch.mtdbnd.dcx"),
    },
    steam_appid=570940,
    default_game_path=DSR_PATH,
    generic_game_path="C:/Program Files (x86)/Steam/steamapps/common/DARK SOULS REMASTERED/",
    save_file_path=Path("~/Documents/NBGI/DARK SOULS REMASTERED").expanduser(),
    executable_name="DarkSoulsRemastered.exe",
    interroot_prefix="N:\\FRPG\\data\\INTERROOT_x64",
    gadget_name="DSR-Gadget.exe",
    default_file_paths={
        "AIScriptDirectory": "script",
        "DrawParamDirectory": "param/DrawParam",
        "EventDirectory": "event",
        "GameParamBND": "param/GameParam/GameParam.parambnd.dcx",
        "MapStudioDirectory": "map/MapStudio",
        "MSGDirectory": "msg/ENGLISH",
        "ParamDefBND": "paramdef/paramdef.paramdefbnd.dcx",
        "TalkDirectory": "script/talk",
    },
)


DARK_SOULS_2 = Game(
    "DARK_SOULS_2",
    "Dark Souls II",
    submodule_name="darksouls2",
    aliases=("darksouls2", "ds2", "dks2"),
    default_dcx_type=DCXType.DCX_DFLT_10000_24_9,
    default_game_path=DS2_PATH,
)


DARK_SOULS_2_SOTFS = Game(
    "DARK_SOULS_2_SOTFS",
    "Dark Souls II: Scholar of the First Sin",
    submodule_name="darksouls2",  # TODO: Currently identical to DS2.
    aliases=("darksouls2sotfs", "ds2sotfs", "dks2sotfs", "sotfs"),
    default_dcx_type=DCXType.DCX_DFLT_10000_24_9,
    default_game_path=DS2_SOTFS_PATH,
)


BLOODBORNE = Game(
    "BLOODBORNE",
    "Bloodborne",
    submodule_name="bloodborne",
    aliases=("bloodborne", "bb"),
    default_dcx_type=DCXType.DCX_DFLT_10000_44_9,
    bundled_resource_paths={
        "PARAMDEFBND": PACKAGE_PATH("bloodborne/params/resources/bloodborne.paramdefbnd.dcx"),
        "MTDBND": PACKAGE_PATH("bloodborne/models/resources/allmaterialbnd.mtdbnd.dcx"),
    },
    steam_appid=None,
    default_game_path=BB_PATH,
    generic_game_path="{DISC}/Image0/dvdroot_ps4",
    executable_name="../eboot.bin",
    interroot_prefix="N:\\SPRJ\\data\\INTERROOT_ps4",
    default_file_paths={
        "AIScriptDirectory": "script",
        "EventDirectory": "event",
        "GameParamBND": "param/gameparam/gameparam.parambnd.dcx",
        "MapStudioDirectory": "map/mapstudio",
        "MSGDirectory": "msg/engus",
        "ParamDefBND": "paramdef/paramdef.paramdefbnd.dcx",
        "TalkDirectory": "script/talk",
    },
)


DARK_SOULS_3 = Game(
    "DARK_SOULS_3",
    "Dark Souls III",
    submodule_name="darksouls3",
    aliases=("darksouls3", "ds3", "dks3"),
    default_dcx_type=DCXType.DCX_DFLT_10000_44_9,
    default_game_path=DS3_PATH,
    executable_name="DarkSoulsIII.exe",
)


SEKIRO = Game(
    "SEKIRO",
    "Sekiro: Shadows Die Twice",
    submodule_name="sekiro",
    aliases=("sekiro", "sekiroshadowsdietwice", "sdt"),
    default_dcx_type=DCXType.DCX_KRAK,
    default_game_path=SEKIRO_PATH,
)


ELDEN_RING = Game(
    "ELDEN_RING",
    "Elden Ring",
    submodule_name="eldenring",
    aliases=("eldenring", "er"),
    default_dcx_type=DCXType.DCX_KRAK,
    special_dcx_types={
        ".bin": DCXType.Null,
    },
    bundled_resource_paths={
        "MATBINBND": PACKAGE_PATH("eldenring/models/resources/allmaterial.matbinbnd.dcx"),
        "dlc01_MATBINBND": PACKAGE_PATH("eldenring/models/resources/allmaterial_dlc01.matbinbnd.dcx"),
        "dlc02_MATBINBND": PACKAGE_PATH("eldenring/models/resources/allmaterial_dlc02.matbinbnd.dcx"),
    },
    steam_appid=1245620,
    default_game_path=ELDEN_RING_PATH,
    executable_name="ELDENRING.exe",
    interroot_prefix="N:\\GR\\data\\INTERROOT_win64",
    default_file_paths={
        "EventDirectory": "event",
        "MapStudioDirectory": "map/MapStudio",
        "MSGDirectory": "msg/engus",
    },
)


GAMES = (
    DEMONS_SOULS,
    DEMONS_SOULS_REMAKE,
    DARK_SOULS_PTDE,
    DARK_SOULS_DSR,
    DARK_SOULS_2,
    DARK_SOULS_2_SOTFS,
    BLOODBORNE,
    DARK_SOULS_3,
    SEKIRO,
    ELDEN_RING,
)


def get_game(game_name: str | Game):
    """Spaces, case, apostrophes, and colons in aliases don't matter."""
    if isinstance(game_name, Game):
        return game_name
    game_name = game_name.lower()
    for old, new in ((" ", ""), ("'", ""), (":", ""), ("iii", "3"), ("ii", "2")):
        game_name.replace(old, new)
    if game_name in {"darksouls", "darksouls1", "dks"}:
        raise ValueError(f"Ambiguous game name: {game_name}. Try 'ptde' or 'dsr' instead.")
    hits = []
    for game in GAMES:
        if game_name == game.name.lower() or game_name == game.variable_name.lower() or game_name in game.aliases:
            hits.append(game)
    if not hits:
        raise ValueError(f"Invalid game name: {game_name}")
    if len(hits) >= 2:
        raise ValueError(f"Ambiguous game name: {game_name}.")
    return hits[0]
