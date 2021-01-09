__all__ = ["GameDirectoryProject"]

from soulstruct.ai.bloodborne import AIDirectory
# from soulstruct.esd.bloodborne import TalkDirectory  # TODO
from soulstruct.events.bloodborne import EMEVDDirectory
from soulstruct.games import BLOODBORNE
from soulstruct.maps.bloodborne import MapStudioDirectory
from soulstruct.params.bloodborne.core import GameParamBND
# from soulstruct.params.bloodborne.draw_param import DrawParamDirectory  # TODO: GParam
from soulstruct.project.base.core import GameDirectoryProject as _BaseGameDirectoryProject
from soulstruct.project.core import SoulstructProjectError
from soulstruct.text.bloodborne import MSGDirectory


class GameDirectoryProject(_BaseGameDirectoryProject):
    GAME = BLOODBORNE
    DATA_TYPES = {
        "ai": AIDirectory,
        "events": EMEVDDirectory,
        # "lighting": DrawParamDirectory,
        "maps": MapStudioDirectory,
        "params": GameParamBND,
        # "talk": TalkDirectory,
        "text": MSGDirectory,
    }
