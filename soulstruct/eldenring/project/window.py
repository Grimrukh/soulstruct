from __future__ import annotations

import typing as tp

from soulstruct.base.project.enums import ProjectDataType
from soulstruct.base.project.window import ProjectWindow as _BaseProjectWindow, ImportSettings, ProjectCreatorWizard

from .core import GameDirectoryProject
from .links import WindowLinker


class ProjectWindow(_BaseProjectWindow):
    PROJECT_CLASS = GameDirectoryProject
    LINKER_CLASS = WindowLinker
    RUNTIME_MANAGER_CLASS = None
    CHARACTER_MODELS = {}  # TODO

    project: GameDirectoryProject

    def run_creator_wizard(
        self,
        game_name: str,
        supported_data_types: tp.Sequence[ProjectDataType],
        data_type_settings: dict[ProjectDataType, dict[str, tuple[str, bool, str]]],
    ) -> ImportSettings | None:
        """Launch Project Creator Wizard window and block until it returns its boolean dictionary.

        Elden Ring creator wizard warns the user if they are using enums in EVS scripts, which can take a long time for
        Elden Ring's many MSBs and EMEVDs.
        """
        wizard = ProjectCreatorWizard(
            master=self,
            game_name=game_name,
            supported_data_types=supported_data_types,
            data_type_settings=data_type_settings,
        )
        import_settings = wizard.go()
        if import_settings:
            if import_settings.data_type_settings.get(ProjectDataType.Events, {}).get("use_enums_in_event_scripts"):
                GameDirectoryProject.warn_long_event_import(with_window=self)
        return import_settings
