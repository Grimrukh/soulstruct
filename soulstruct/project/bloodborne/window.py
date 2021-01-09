# from soulstruct.models.bloodborne import CHARACTER_MODELS
from soulstruct.project.base.window import ProjectWindow as _BaseProjectWindow

from .core import GameDirectoryProject


class ProjectWindow(_BaseProjectWindow):
    PROJECT_CLASS = GameDirectoryProject
    RUNTIME_MANAGER_CLASS = None
    CHARACTER_MODELS = {}  # TODO
