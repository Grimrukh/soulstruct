__all__ = ["GameDirectoryProject"]

from soulstruct.base.project.core import GameDirectoryProject as _BaseGameDirectoryProject
from soulstruct.games import BloodborneType

# from soulstruct.bloodborne.ai import AIDirectory  # TODO: can't decompile
from soulstruct.bloodborne.events import EMEVDDirectory
# from soulstruct.bloodborne.ezstate import TalkDirectory  # TODO: binary problems
from soulstruct.bloodborne.maps import MapStudioDirectory
from soulstruct.bloodborne.params import GameParamBND
# from soulstruct.bloodborne.params.draw_param import DrawParamDirectory  # TODO: GParam
from soulstruct.bloodborne.text import MSGDirectory


class GameDirectoryProject(_BaseGameDirectoryProject, BloodborneType):
    DATA_TYPES = {
        # "ai": AIDirectory,
        "events": EMEVDDirectory,
        # "lighting": DrawParamDirectory,
        "maps": MapStudioDirectory,
        "params": GameParamBND,
        # "talk": TalkDirectory,
        "text": MSGDirectory,
    }

    params: GameParamBND
    maps: MapStudioDirectory
    text: MSGDirectory
    events: EMEVDDirectory
