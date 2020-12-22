from soulstruct.project.base.window import ProjectWindow as _BaseProjectWindow

from .core import GameDirectoryProject


class ProjectWindow(_BaseProjectWindow):
    PROJECT_CLASS = GameDirectoryProject
