from __future__ import annotations

__all__ = ["GameDirectoryProject"]

from pathlib import Path

from soulstruct.base.project import GameDirectoryProject as _BaseGameDirectoryProject, ProjectDataType

from soulstruct.darksouls1ptde.ai import AIScriptDirectory
from soulstruct.darksouls1ptde.ezstate import TalkDirectory
from soulstruct.darksouls1ptde.events import EventDirectory
from soulstruct.darksouls1ptde.maps import MapStudioDirectory
from soulstruct.darksouls1ptde.params import GameParamBND
from soulstruct.darksouls1ptde.params import DrawParamDirectory
from soulstruct.darksouls1ptde.text import MSGDirectory


class GameDirectoryProject(_BaseGameDirectoryProject):
    # This also determines load order, which is important for some types (e.g. Maps -> Enums -> Events).
    DATA_TYPES = {
        ProjectDataType.Params: GameParamBND,
        ProjectDataType.Lighting: DrawParamDirectory,
        ProjectDataType.AI: AIScriptDirectory,
        ProjectDataType.Talk: TalkDirectory,  # modified via ESP state machine script files
        ProjectDataType.Text: MSGDirectory,
        ProjectDataType.Maps: MapStudioDirectory,
        ProjectDataType.Enums: None,  # modified via Python modules; must be loaded after `Maps`
        ProjectDataType.Events: EventDirectory,  # modified via EVS event script files
    }

    def _validate_game_directory(self, game_root: Path) -> bool:
        if not (game_root / "map").is_dir():
            self.error(
                "Your Dark Souls: Prepare to Die Edition does not appear to be unpacked.\n"
                "Please download and run 'UnpackDarkSoulsForModding' (UDSFM) from Nexus:\n"
                "https://www.nexusmods.com/darksouls/mods/1304"
            )
            return False
        return True
