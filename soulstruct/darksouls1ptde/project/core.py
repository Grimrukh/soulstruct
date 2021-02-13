from __future__ import annotations

__all__ = ["GameDirectoryProject"]

import typing as tp

from soulstruct.base.project import GameDirectoryProject as _BaseGameDirectoryProject
from soulstruct.base.project.exceptions import SoulstructProjectError
from soulstruct.games import DARK_SOULS_PTDE

from soulstruct.darksouls1ptde.ai import AIDirectory
from soulstruct.darksouls1ptde.ezstate import TalkDirectory
from soulstruct.darksouls1ptde.events import EMEVDDirectory
from soulstruct.darksouls1ptde.maps import MapStudioDirectory
from soulstruct.darksouls1ptde.params import GameParamBND
from soulstruct.darksouls1ptde.params import DrawParamDirectory
from soulstruct.darksouls1ptde.text import MSGDirectory

if tp.TYPE_CHECKING:
    from soulstruct.base.project.window import ProjectWindow


class GameDirectoryProject(_BaseGameDirectoryProject):
    GAME = DARK_SOULS_PTDE
    DATA_TYPES = {
        "ai": AIDirectory,
        "events": EMEVDDirectory,
        "lighting": DrawParamDirectory,
        "maps": MapStudioDirectory,
        "params": GameParamBND,
        "talk": TalkDirectory,
        "text": MSGDirectory,
    }

    def initialize_project(self, force_import_from_game=False, with_window: ProjectWindow = None):
        self._check_ptde_unpacked()
        super().initialize_project(force_import_from_game, with_window)

    def _check_ptde_unpacked(self):
        if not (self.game_root / "map").is_dir():
            raise SoulstructProjectError(
                "Your Dark Souls: Prepare to Die Edition does not appear to be unpacked.\n"
                "Please download and run 'UnpackDarkSoulsForModding' (UDSFM) from Nexus:\n"
                "https://www.nexusmods.com/darksouls/mods/1304"
            )
