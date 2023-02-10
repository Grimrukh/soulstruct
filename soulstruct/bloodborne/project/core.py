__all__ = ["GameDirectoryProject"]

from soulstruct.base.project.core import GameDirectoryProject as _BaseGameDirectoryProject

# from soulstruct.bloodborne.ai import ScriptDirectory  # TODO: can't decompile
from soulstruct.bloodborne.events import EventDirectory
# from soulstruct.bloodborne.ezstate import TalkDirectory  # TODO: binary problems
from soulstruct.bloodborne.maps import MapStudioDirectory
from soulstruct.bloodborne.params import GameParamBND
# from soulstruct.bloodborne.params.draw_param import DrawParamDirectory  # TODO: GParam
from soulstruct.bloodborne.text import MSGDirectory


class GameDirectoryProject(_BaseGameDirectoryProject):
    DATA_TYPES = {
        # "ai": ScriptDirectory,
        "events": EventDirectory,
        # "lighting": DrawParamDirectory,
        "maps": MapStudioDirectory,
        "params": GameParamBND,
        # "talk": TalkDirectory,
        "text": MSGDirectory,
    }

    params: GameParamBND
    maps: MapStudioDirectory
    text: MSGDirectory
    events: EventDirectory
