__all__ = ["GameDirectoryProject"]

from soulstruct.ai.darksouls1 import AIDirectory
from soulstruct.events.darksouls1 import convert_events, EMEVDDirectoryDSR
from soulstruct.games import DARK_SOULS_DSR
from soulstruct.maps.darksouls1 import MapStudioDirectory
from soulstruct.maps.darksouls1.maps import ALL_MAPS, get_map
from soulstruct.params.darksouls1r.core import GameParamBND
from soulstruct.params.darksouls1r.draw_param import DrawParamDirectory
from soulstruct.project.base.core import GameDirectoryProject as _BaseGameDirectoryProject
from soulstruct.esd.darksouls1r.talk_esd_bnd import TalkESDBND, TalkDirectory
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
    CONVERT_EVENTS = convert_events
    TALKESD_BND = TalkESDBND
    IGNORE_TALK_FILES = ("m12_00_00_01", "m14_02_00_00")
    ALL_MAPS = ALL_MAPS
    GET_MAP = get_map
