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
    DATA_TYPES = {
        ProjectDataType.AI: AIScriptDirectory,
        ProjectDataType.Events: EventDirectory,  # modified via EVS event script files
        ProjectDataType.Lighting: DrawParamDirectory,
        ProjectDataType.Maps: MapStudioDirectory,
        ProjectDataType.Params: GameParamBND,
        ProjectDataType.Talk: TalkDirectory,  # modified via ESP state machine script files
        ProjectDataType.Text: MSGDirectory,
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
