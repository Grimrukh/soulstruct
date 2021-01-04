from soulstruct.models.darksouls1 import CHARACTER_MODELS
from soulstruct.project.base.window import ProjectWindow as _BaseProjectWindow

from .core import GameDirectoryProject


class ProjectWindow(_BaseProjectWindow):
    PROJECT_CLASS = GameDirectoryProject
    CHARACTER_MODELS = CHARACTER_MODELS
