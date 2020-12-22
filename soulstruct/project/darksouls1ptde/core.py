__all__ = ["GameDirectoryProject"]

import typing as tp

from soulstruct.ai.darksouls1 import AIDirectory
from soulstruct.esd.darksouls1ptde import TalkDirectory
from soulstruct.events.darksouls1 import EMEVDDirectoryPTDE
from soulstruct.games import DARK_SOULS_PTDE
from soulstruct.maps.darksouls1 import MapStudioDirectory
from soulstruct.maps.darksouls1.maps import ALL_MAPS, get_map
from soulstruct.params.darksouls1r.core import GameParamBND
from soulstruct.params.darksouls1r.draw_param import DrawParamDirectory
from soulstruct.project.base.core import GameDirectoryProject as _BaseGameDirectoryProject
from soulstruct.project.core import SoulstructProjectError
from soulstruct.text.darksouls1 import MSGDirectory

if tp.TYPE_CHECKING:
    from soulstruct.project import ProjectWindow


class GameDirectoryProject(_BaseGameDirectoryProject):
    GAME = DARK_SOULS_PTDE
    DATA_TYPES = {
        "ai": AIDirectory,
        "events": EMEVDDirectoryPTDE,
        "lighting": DrawParamDirectory,
        "maps": MapStudioDirectory,
        "params": GameParamBND,
        "talk": TalkDirectory,
        "text": MSGDirectory,
    }
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)

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
