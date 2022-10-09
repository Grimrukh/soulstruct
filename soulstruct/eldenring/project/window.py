from soulstruct.base.project.window import ProjectWindow as _BaseProjectWindow

from .core import GameDirectoryProject
from .links import WindowLinker


class ProjectWindow(_BaseProjectWindow):
    PROJECT_CLASS = GameDirectoryProject
    LINKER_CLASS = WindowLinker
    RUNTIME_MANAGER_CLASS = None
    CHARACTER_MODELS = {}  # TODO

    project: GameDirectoryProject
