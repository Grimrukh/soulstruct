__all__ = ["GameDirectoryProject"]

from soulstruct.base.project.core import GameDirectoryProject as _BaseGameDirectoryProject, ProjectDataType

# from soulstruct.bloodborne.ai import AIScriptDirectory  # TODO: can't decompile
from soulstruct.bloodborne.events import EventDirectory
# from soulstruct.bloodborne.ezstate import TalkDirectory  # TODO: binary problems
from soulstruct.bloodborne.maps import MapStudioDirectory
from soulstruct.bloodborne.params import GameParamBND
# from soulstruct.bloodborne.params.draw_param import DrawParamDirectory  # TODO: GParam
from soulstruct.bloodborne.text import MSGDirectory


class GameDirectoryProject(_BaseGameDirectoryProject):
    # This also determines load order, which is important for some types (e.g. Maps -> Enums -> Events).
    DATA_TYPES = {
        ProjectDataType.Params: GameParamBND,
        # ProjectDataType.Lighting: DrawParamDirectory,
        # ProjectDataType.AI: AIScriptDirectory,
        # ProjectDataType.Talk: TalkDirectory,  # modified via ESP state machine script files
        ProjectDataType.Text: MSGDirectory,
        ProjectDataType.Maps: MapStudioDirectory,
        ProjectDataType.Enums: None,  # modified via Python modules; must be loaded after `Maps`
        ProjectDataType.Events: EventDirectory,  # modified via EVS event script files
    }

    params: GameParamBND
    maps: MapStudioDirectory
    text: MSGDirectory
