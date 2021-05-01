"""Basic information structures for all FromSoftware games used across Soulstruct.

These `Game` instances are also used as singletons for game checking.
"""
from __future__ import annotations

__all__ = [
    "Game",
    "GAMES",
    "get_game",
    "GameSelector",

    "DEMONS_SOULS",
    "DEMONS_SOULS_REMAKE",
    "DARK_SOULS_PTDE",
    "DARK_SOULS_DSR",
    "DARK_SOULS_2",
    "DARK_SOULS_2_SOTFS",
    "BLOODBORNE",
    "DARK_SOULS_3",
    "SEKIRO",
]

import importlib
import typing as tp
from pathlib import Path

from soulstruct.config import *
from soulstruct.utilities.files import PACKAGE_PATH
from soulstruct.utilities.window import SmartFrame, bind_to_all_children


class Game:

    def __init__(
        self,
        name,
        subpackage_name=None,
        aliases=(),
        uses_dcx=True,
        bundled_paramdef_path=Path(),
        steam_appid=None,
        default_game_path="",
        generic_game_path="",  # for display in game-finding hint dialog
        save_file_path: Path = None,  # TODO: Save name/extension probably differs outside DSR.
        executable_name="",
        gadget_name="",
        default_file_paths=None,
    ):
        self.name = name
        self.submodule_name = subpackage_name
        self.aliases = aliases
        self.uses_dcx = uses_dcx
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
        """Append or remove ".dcx" to/from given path according to `.uses_dcx`."""
        path = Path(path)
        if not self.uses_dcx and path.suffix == ".dcx":
            return path.with_name(path.stem)
        elif self.uses_dcx and not path.suffix == ".dcx":
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
    subpackage_name="darksouls1ptde",
    aliases=("darksoulspreparetodieedition", "darksoulsptde", "ptde", "darksouls1ptde"),
    uses_dcx=False,
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
DARK_SOULS_DSR = Game(
    "Dark Souls Remastered",
    subpackage_name="darksouls1r",
    aliases=("darksoulsremastered", "darksoulsdsr", "dsr", "ds1r", "darksouls1r"),
    uses_dcx=True,
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
DARK_SOULS_2 = Game(
    "Dark Souls II",
    subpackage_name="darksouls2",
    aliases=("darksouls2", "ds2", "dks2"),
    uses_dcx=True,
    default_game_path=DS2_PATH,
)
DARK_SOULS_2_SOTFS = Game(
    "Dark Souls II Scholar of the First Sin",
    subpackage_name="darksouls2",  # TODO: Currently identical to DS2.
    aliases=("darksouls2sotfs", "ds2sotfs", "dks2sotfs", "sotfs"),
    uses_dcx=True,
    default_game_path=DS2_SOTFS_PATH,
)
BLOODBORNE = Game(
    "Bloodborne",
    subpackage_name="bloodborne",
    aliases=("bloodborne", "bb"),
    uses_dcx=True,
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
DARK_SOULS_3 = Game(
    "Dark Souls III",
    subpackage_name="darksouls3",
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
    hits = []
    for game in GAMES:
        if game_name == game.name.lower() or game_name in game.aliases:
            hits.append(game)
    if not hits:
        raise ValueError(f"Invalid game name: {game_name}")
    if len(hits) >= 2:
        raise ValueError(f"Ambiguous game name: {game_name}.")
    return hits[0]


class GameSelector(SmartFrame):

    def __init__(self, *name_options):
        super().__init__(window_title="Game Selector")

        self.protocol("WM_DELETE_WINDOW", lambda: self.done(None))
        self.resizable(width=False, height=False)
        bind_to_all_children(self.toplevel, "<Escape>", lambda _: self.done(None))

        self.output = None  # type: tp.Optional[Game]
        self.build(name_options)

    def build(self, name_options):
        with self.set_master(padx=20, pady=10, auto_rows=0):
            self.Label(text="Choose the game you are modding:", padx=10, pady=20)
            for name_option in name_options:
                try:
                    game = get_game(name_option)
                except ValueError:
                    raise ValueError(f"Invalid game name: {name_option}")
                self.Button(
                    text=game.name,
                    command=lambda g=game: self.done(g),
                    bg="#422",
                    fg="#FFF",
                    width=30,
                    pady=10,
                    padx=10,
                )

    def go(self) -> Game:
        self.toplevel.wait_visibility()
        self.toplevel.grab_set()
        self.toplevel.mainloop()
        self.toplevel.destroy()
        return self.output

    def done(self, game: tp.Optional[Game]):
        self.output = game
        self.toplevel.quit()
