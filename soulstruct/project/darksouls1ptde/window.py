from soulstruct.models.darksouls1 import CHARACTER_MODELS
from soulstruct.project.base.window import ProjectWindow as _BaseProjectWindow

from .core import GameDirectoryProject
from .runtime import RuntimeManager


class ProjectWindow(_BaseProjectWindow):
    PROJECT_CLASS = GameDirectoryProject
    RUNTIME_MANAGER_CLASS = RuntimeManager
    CHARACTER_MODELS = CHARACTER_MODELS
