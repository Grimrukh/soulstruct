"""Basic information structures for all FromSoftware games used across Soulstruct.

These `Game` instances are also used as singletons for game checking.

NOTE: This file is Python 3.9 compatible for Blender 3.X use.
"""
from __future__ import annotations

__all__ = [
    "Game",
    "GameSpecificType",
    "GAMES",
    "get_game",
    "DEMONS_SOULS",
    "DemonsSoulsType",
    "DEMONS_SOULS_REMAKE",
    "DemonsSoulsRemakeType",
    "DARK_SOULS_PTDE",
    "DarkSoulsPTDEType",
    "DARK_SOULS_DSR",
    "DarkSoulsDSRType",
    "DARK_SOULS_2",
    "DarkSouls2Type",
    "DARK_SOULS_2_SOTFS",
    "DarkSouls2SOTFSType",
    "BLOODBORNE",
    "BloodborneType",
    "DARK_SOULS_3",
    "DarkSouls3Type",
    "SEKIRO",
    "ELDEN_RING",
    "EldenRingType",
]

import abc
import importlib
import typing as tp
from pathlib import Path

from soulstruct.config import *
from soulstruct.containers.dcx import DCXType
from soulstruct.utilities.files import PACKAGE_PATH


class Game:

    def __init__(
        self,
        variable_name: str,
        name: str,
        submodule_name=None,
        aliases=(),
        default_dcx: DCXType = None,
        bundled_paramdef_path=Path(),
        steam_appid=None,
        default_game_path="",
        generic_game_path="",  # for display in game-finding hint dialog
        save_file_path: Path = None,  # TODO: Save name/extension probably differs outside DSR.
        executable_name="",
        gadget_name="",
        default_file_paths=None,
    ):
        self.variable_name = variable_name
        self.name = name
        self.submodule_name = submodule_name
        self.aliases = aliases
        self.default_dcx = default_dcx
        self.bundled_paramdef_path = bundled_paramdef_path
        self.steam_appid = steam_appid
        self.default_game_path = default_game_path
        self.generic_game_path = generic_game_path
        self.save_file_path = save_file_path
        self.executable_name = executable_name
        self.gadget_name = gadget_name
        self.default_file_paths = {} if default_file_paths is None else default_file_paths
        # TODO: other file version info
        # TODO: Soulstruct event import shortcut functions, etc.

    def dcxify(self, path: tp.Union[str, Path]) -> Path:
        """Append or remove ".dcx" to/from given path according to `.default_dcx`."""
        path = Path(path)
        if not self.default_dcx and path.suffix == ".dcx":
            return path.with_name(path.stem)
        elif self.default_dcx and not path.suffix == ".dcx":
            return path.with_name(path.name + ".dcx")
        return path

    def import_game_submodule(self, *args) -> tp.Any:
        if not self.submodule_name:
            raise AttributeError(f"Game {self.name} does not have any submodule in Soulstruct.")
        module_name = "soulstruct." + ".".join((self.submodule_name,) + args)
        return importlib.import_module(module_name)  # will raise an `ImportError` if it fails

    def __eq__(self, other: Game):
        return self.name == other.name

    def __repr__(self):
        return f"Game(\"{self.name}\")"


class GameSpecificType(abc.ABC):
    """Base class for classes that define `GAME`, which can be mixed in to classes for those games."""

    GAME: Game = None


DEMONS_SOULS = Game(
    "DEMONS_SOULS",
    "Demon's Souls",
    aliases=("demonssouls", "des"),
    default_dcx=DCXType.DCX_EDGE,
    default_game_path=DES_PATH,
    executable_name="EBOOT.BIN",
)


class DemonsSoulsType(GameSpecificType):
    GAME = DEMONS_SOULS


DEMONS_SOULS_REMAKE = Game(
    "DEMONS_SOULS_REMAKE",
    "Demon's Souls Remake",
    aliases=("demonssoulsremake", "desr"),
    default_dcx=None,  # TODO: Unknown.
    default_game_path=DESR_PATH,
)


class DemonsSoulsRemakeType(GameSpecificType):
    GAME = DEMONS_SOULS_REMAKE


DARK_SOULS_PTDE = Game(
    "DARK_SOULS_PTDE",
    "Dark Souls Prepare to Die Edition",
    submodule_name="darksouls1ptde",
    aliases=("darksoulspreparetodieedition", "darksoulsptde", "ptde", "darksouls1ptde"),
    default_dcx=None,
    bundled_paramdef_path=PACKAGE_PATH("darksouls1ptde/params/resources/darksouls1ptde.paramdefbnd"),
    steam_appid=211420,
    default_game_path=PTDE_PATH,
    generic_game_path="C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA",
    save_file_path=Path("~/Documents/NBGI/DarkSouls").expanduser(),
    executable_name="DARKSOULS.exe",
    gadget_name="DS Gadget.exe",
    default_file_paths={
        "AIDirectory": "script",
        "DrawParamDirectory": "param/DrawParam",
        "EMEVDDirectory": "event",
        "GameParamBND": "param/GameParam/GameParam.parambnd",
        "MapStudioDirectory": "map/MapStudio",
        "MSGDirectory": "msg/ENGLISH",
        "ParamDefBND": "paramdef/paramdef.paramdefbnd",
        "TalkDirectory": "script/talk",
    },
)


class DarkSoulsPTDEType(GameSpecificType):
    GAME = DARK_SOULS_PTDE


DARK_SOULS_DSR = Game(
    "DARK_SOULS_DSR",
    "Dark Souls Remastered",
    submodule_name="darksouls1r",
    aliases=("darksoulsremastered", "darksoulsdsr", "dsr", "ds1r", "darksouls1r"),
    default_dcx=DCXType.DCX_DFLT_10000_24_9,
    bundled_paramdef_path=PACKAGE_PATH("darksouls1r/params/resources/darksouls1r.paramdefbnd.dcx"),
    steam_appid=570940,
    default_game_path=DSR_PATH,
    generic_game_path="C:/Program Files (x86)/Steam/steamapps/common/DARK SOULS REMASTERED/",
    save_file_path=Path("~/Documents/NBGI/DARK SOULS REMASTERED").expanduser(),
    executable_name="DarkSoulsRemastered.exe",
    gadget_name="DSR-Gadget.exe",
    default_file_paths={
        "AIDirectory": "script",
        "DrawParamDirectory": "param/DrawParam",
        "EMEVDDirectory": "event",
        "GameParamBND": "param/GameParam/GameParam.parambnd.dcx",
        "MapStudioDirectory": "map/MapStudio",
        "MSGDirectory": "msg/ENGLISH",
        "ParamDefBND": "paramdef/paramdef.paramdefbnd.dcx",
        "TalkDirectory": "script/talk",
    },
)


class DarkSoulsDSRType(GameSpecificType):
    GAME = DARK_SOULS_DSR


DARK_SOULS_2 = Game(
    "DARK_SOULS_2",
    "Dark Souls II",
    submodule_name="darksouls2",
    aliases=("darksouls2", "ds2", "dks2"),
    default_dcx=DCXType.DCX_DFLT_10000_24_9,
    default_game_path=DS2_PATH,
)


class DarkSouls2Type(GameSpecificType):
    GAME = DARK_SOULS_2


DARK_SOULS_2_SOTFS = Game(
    "DARK_SOULS_2_SOTFS",
    "Dark Souls II Scholar of the First Sin",
    submodule_name="darksouls2",  # TODO: Currently identical to DS2.
    aliases=("darksouls2sotfs", "ds2sotfs", "dks2sotfs", "sotfs"),
    default_dcx=DCXType.DCX_DFLT_10000_24_9,
    default_game_path=DS2_SOTFS_PATH,
)


class DarkSouls2SOTFSType(GameSpecificType):
    GAME = DARK_SOULS_2_SOTFS


BLOODBORNE = Game(
    "BLOODBORNE",
    "Bloodborne",
    submodule_name="bloodborne",
    aliases=("bloodborne", "bb"),
    default_dcx=DCXType.DCX_DFLT_10000_44_9,
    bundled_paramdef_path=PACKAGE_PATH("bloodborne/params/resources/bloodborne.paramdefbnd.dcx"),
    steam_appid=None,
    default_game_path=BB_PATH,
    generic_game_path="{DISC}/Image0/dvdroot_ps4",
    executable_name="../eboot.bin",
    default_file_paths={
        "AIDirectory": "script",
        "EMEVDDirectory": "event",
        "GameParamBND": "param/gameparam/gameparam.parambnd.dcx",
        "MapStudioDirectory": "map/mapstudio",
        "MSGDirectory": "msg/engus",
        "ParamDefBND": "paramdef/paramdef.paramdefbnd.dcx",
        "TalkDirectory": "script/talk",
    },
)


class BloodborneType(GameSpecificType):
    GAME = BLOODBORNE


DARK_SOULS_3 = Game(
    "DARK_SOULS_3",
    "Dark Souls III",
    submodule_name="darksouls3",
    aliases=("darksouls3", "ds3", "dks3"),
    default_dcx=DCXType.DCX_DFLT_10000_44_9,
    default_game_path=DS3_PATH,
    executable_name="DarkSoulsIII.exe",
)


class DarkSouls3Type(GameSpecificType):
    GAME = DARK_SOULS_3


SEKIRO = Game(
    "SEKIRO",
    "Sekiro",
    submodule_name="sekiro",
    aliases=("sekiro", "sekiroshadowsdietwice", "sdt"),
    default_dcx=DCXType.DCX_KRAK,
    default_game_path=SEKIRO_PATH,
)


class SekiroType(GameSpecificType):
    GAME = SEKIRO


ELDEN_RING = Game(
    "ELDEN_RING",
    "Elden Ring",
    submodule_name="eldenring",
    aliases=("eldenring", "er"),
    default_dcx=DCXType.DCX_KRAK,
    default_game_path=ELDEN_RING_PATH,
    executable_name="ELDENRING.exe",
    default_file_paths={
        "EMEVDDirectory": "event",
        "MSGDirectory": "msg/engus",
    },
)


class EldenRingType(GameSpecificType):
    GAME = ELDEN_RING


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


def get_game(game_name: tp.Union[str, Game]):
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
        if game_name == game.name.lower() or game_name in game.aliases:
            hits.append(game)
    if not hits:
        raise ValueError(f"Invalid game name: {game_name}")
    if len(hits) >= 2:
        raise ValueError(f"Ambiguous game name: {game_name}.")
    return hits[0]
