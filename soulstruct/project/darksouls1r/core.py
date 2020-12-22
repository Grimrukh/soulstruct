__all__ = ["GameDirectoryProject"]

from soulstruct.ai.darksouls1 import AIDirectory
from soulstruct.esd.darksouls1r import TalkDirectory
from soulstruct.events.darksouls1 import EMEVDDirectoryDSR
from soulstruct.games import DARK_SOULS_DSR
from soulstruct.maps.darksouls1 import MapStudioDirectory
from soulstruct.maps.darksouls1.maps import ALL_MAPS, get_map
from soulstruct.params.darksouls1r.core import GameParamBND
from soulstruct.params.darksouls1r.draw_param import DrawParamDirectory
from soulstruct.project.base.core import GameDirectoryProject as _BaseGameDirectoryProject
from soulstruct.text.darksouls1 import MSGDirectory


class GameDirectoryProject(_BaseGameDirectoryProject):

    GAME = DARK_SOULS_DSR
    DATA_TYPES = {
        "ai": AIDirectory,
        "events": EMEVDDirectoryDSR,  # modified via EVS event script files
        "lighting": DrawParamDirectory,
        "maps": MapStudioDirectory,
        "params": GameParamBND,
        "talk": TalkDirectory,  # class not used; modified via ESP state machine script files
        "text": MSGDirectory,
    }
    ALL_MAPS = ALL_MAPS
    GET_MAP = staticmethod(get_map)
