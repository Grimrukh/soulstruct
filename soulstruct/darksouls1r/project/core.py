__all__ = ["GameDirectoryProject"]

from soulstruct.base.project import GameDirectoryProject as _BaseGameDirectoryProject
from soulstruct.darksouls1r.ai import AIDirectory
from soulstruct.darksouls1r.ezstate import TalkDirectory
from soulstruct.darksouls1r.events import EMEVDDirectory
from soulstruct.darksouls1r.maps import MapStudioDirectory
from soulstruct.darksouls1r.params import GameParamBND
from soulstruct.darksouls1r.params import DrawParamDirectory
from soulstruct.darksouls1r.text import MSGDirectory
from soulstruct.games import DARK_SOULS_DSR


class GameDirectoryProject(_BaseGameDirectoryProject):

    GAME = DARK_SOULS_DSR
    DATA_TYPES = {
        "ai": AIDirectory,
        "events": EMEVDDirectory,  # modified via EVS event script files
        "lighting": DrawParamDirectory,
        "maps": MapStudioDirectory,
        "params": GameParamBND,
        "talk": TalkDirectory,  # modified via ESP state machine script files
        "text": MSGDirectory,
    }
