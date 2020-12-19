"""Basic information structures for all FromSoftware games used across Soulstruct."""
from __future__ import annotations

from soulstruct.config import *
from soulstruct.utilities import PACKAGE_PATH

__all__ = [
    "Game",
    "DEMONS_SOULS",
    "DEMONS_SOULS_REMAKE",
    "DARK_SOULS_PTDE",
    "DARK_SOULS_DSR",
    "DARK_SOULS_2",
    "DARK_SOULS_2_SOTFS",
    "BLOODBORNE",
    "DARK_SOULS_3",
    "SEKIRO",
    "GAMES",
    "get_game",
]


class Game:

    def __init__(
        self,
        name,
        aliases=(),
        uses_dcx=True,
        bundled_paramdef_path="",
        steam_appid=None,
        default_game_path="",
        save_file_path: Path = None,  # TODO: Save name/extension probably differs outside DSR.
        executable_name="",
        gadget_name="",
        default_file_paths=None,
    ):
        self.name = name
        self.aliases = aliases
        self.uses_dcx = uses_dcx
        self.bundled_paramdef_path = bundled_paramdef_path
        self.steam_appid = steam_appid
        self.default_game_path = default_game_path
        self.save_file_path = save_file_path
        self.executable_name = executable_name
        self.gadget_name = gadget_name
        self.default_file_paths = {} if default_file_paths is None else default_file_paths
        # TODO: other file version info
        # TODO: Soulstruct event import shortcut functions, etc.

    def dcxify(self, path: tp.Union[str, Path]) -> Path:
        """Append or remove ".dcx" to/from given path according to `.uses_dcx`."""
        path = Path(path)
        if not self.uses_dcx and path.suffix == ".dcx":
            return path.with_name(path.stem)
        elif self.uses_dcx and not path.suffix == ".dcx":
            return path.with_name(path.name + ".dcx")
        return path

    def __eq__(self, other: Game):
        return self.name == other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Game({self.name})"


DEMONS_SOULS = Game(
    "Demon's Souls",
    aliases=("demonssouls", "des"),
    uses_dcx=False,
    default_game_path=DES_PATH,
    executable_name="EBOOT.BIN",
)
DEMONS_SOULS_REMAKE = Game(
    "Demon's Souls Remake",
    aliases=("demonssoulsremake", "desr"),
    uses_dcx=False,  # TODO: Unknown.
    default_game_path=DESR_PATH,
)
DARK_SOULS_PTDE = Game(
    "Dark Souls Prepare to Die Edition",
    aliases=("darksoulspreparetodieedition", "darksoulsptde", "ptde"),
    uses_dcx=False,
    bundled_paramdef_path=PACKAGE_PATH("params/darksouls1ptde/resources/paramdef.paramdefbnd"),
    steam_appid=211420,
    default_game_path=PTDE_PATH,
    save_file_path=Path("~/Documents/NBGI/DarkSouls").expanduser(),
    executable_name="DARKSOULS.exe",
    gadget_name="DS Gadget.exe",
    default_file_paths={
        "AIDirectory": "script",
        "DrawParamDirectory": "param/DrawParam",
        "EMEVDDirectoryPTDE": "event",
        "GameParamBND": "param/GameParam/GameParam.parambnd",
        "MapStudioDirectory": "map/MapStudio",
        "MSGDirectory": "msg/ENGLISH",
        "ParamDefBND": "paramdef/paramdef.paramdefbnd",
        "TalkDirectory": "script/talk",
    },
)
DARK_SOULS_DSR = Game(
    "Dark Souls Remastered",
    aliases=("darksoulsremastered", "darksoulsdsr", "dsr"),
    uses_dcx=True,
    bundled_paramdef_path=PACKAGE_PATH("params/darksouls1r/resources/paramdef.paramdefbnd.dcx"),
    steam_appid=570940,
    default_game_path=DSR_PATH,
    save_file_path=Path("~/Documents/NBGI/DARK SOULS REMASTERED").expanduser(),
    executable_name="DarkSoulsRemastered.exe",
    default_file_paths={
        "AIDirectory": "script",
        "DrawParamDirectory": "param/DrawParam",
        "EMEVDDirectoryDSR": "event",
        "GameParamBND": "param/GameParam/GameParam.parambnd.dcx",
        "MapStudioDirectory": "map/MapStudio",
        "MSGDirectory": "msg/ENGLISH",
        "ParamDefBND": "paramdef/paramdef.paramdefbnd.dcx",
        "TalkDirectory": "script/talk",
    },
)
DARK_SOULS_2 = Game(
    "Dark Souls II",
    aliases=("darksouls2", "ds2", "dks2"),
    uses_dcx=True,
    default_game_path=DS2_PATH,
)
DARK_SOULS_2_SOTFS = Game(
    "Dark Souls II Scholar of the First Sin",
    aliases=("darksouls2sotfs", "ds2sotfs", "dks2sotfs", "sotfs"),
    uses_dcx=True,
    default_game_path=DS2_SOTFS_PATH,
)
BLOODBORNE = Game(
    "Bloodborne",
    aliases=("bloodborne", "bb"),
    uses_dcx=True,
    bundled_paramdef_path=PACKAGE_PATH("params/bloodborne/resources/bloodborne.paramdefbnd.dcx"),
    steam_appid=None,
    default_game_path=BB_PATH,
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
DARK_SOULS_3 = Game(
    "Dark Souls III",
    aliases=("darksouls3", "ds3", "dks3"),
    uses_dcx=True,
    default_game_path=DS3_PATH,
    executable_name="DarkSoulsIII.exe",
)
SEKIRO = Game(
    "Sekiro",
    aliases=("sekiro", "sekiroshadowsdietwice", "sdt"),
    uses_dcx=True,
    default_game_path=SEKIRO_PATH,
)
ELDEN_RING = Game(
    "Elden Ring",
    aliases=("eldenring", "er"),
    uses_dcx=True,
    default_game_path=ELDEN_RING_PATH,
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


def get_game(game_name: tp.Union[str, Game]):
    """Spaces, case, apostrophes, and colons in aliases don't matter."""
    if isinstance(game_name, Game):
        return game_name
    game_name = game_name.lower()
    for old, new in ((" ", ""), ("'", ""), (":", ""), ("iii", "3"), ("ii", "2")):
        game_name.replace(old, new)
    if game_name in {"darksouls", "darksouls1", "dks"}:
        raise ValueError(f"Ambiguous game name: {game_name}. Try 'ptde' or 'dsr' instead.")
    for game in GAMES:
        if game_name in game.aliases:
            return game
    raise ValueError(f"Invalid game name: {game_name}")
