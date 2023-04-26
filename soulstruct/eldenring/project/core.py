from __future__ import annotations

__all__ = ["GameDirectoryProject"]

import logging
import typing as tp
from pathlib import Path

from soulstruct.base.project.core import GameDirectoryProject as _BaseGameDirectoryProject, ProjectDataType

from soulstruct.eldenring.events import EventDirectory
from soulstruct.eldenring.events.create_vanilla_entities import copy_vanilla_entities
from soulstruct.eldenring.maps import MapStudioDirectory
from soulstruct.eldenring.text import MSGDirectory

if tp.TYPE_CHECKING:
    from .window import ProjectWindow

_LOGGER = logging.getLogger(__name__)


class GameDirectoryProject(_BaseGameDirectoryProject):
    DATA_TYPES = {
        # ProjectDataType.Params: GameParamBND,
        # ProjectDataType.Lighting: DrawParamDirectory,
        # ProjectDataType.AI: AIScriptDirectory,
        # ProjectDataType.Talk: TalkDirectory,  # modified via ESP state machine script files
        ProjectDataType.Text: MSGDirectory,
        ProjectDataType.Maps: MapStudioDirectory,
        ProjectDataType.Enums: None,  # modified via Python modules; must be loaded after `Maps`
        ProjectDataType.Events: EventDirectory,  # modified via EVS event script files
    }

    events: EventDirectory
    maps: MapStudioDirectory
    text: MSGDirectory

    @staticmethod
    def warn_long_event_import(with_window: ProjectWindow = None):
        if with_window:
            with_window.CustomDialog(
                title="Long Operation Warning",
                message="Decompiling events using entities. This may take a while!\n"
                        "The project window will appear when ready.",
            )
        else:
            _LOGGER.warning(
                "Decompiling events using entities. This may take a while! The project window will appear when done."
            )

    # TODO: copy in vanilla enums

    def import_Events(
        self,
        import_directory: Path | str,
        use_enums_in_event_scripts=True,
        copy_python_events_submodule=False,
    ):
        """Offers entities directory creation."""
        if use_enums_in_event_scripts:
            self.warn_long_event_import()
        super().import_Events(import_directory, use_enums_in_event_scripts, copy_python_events_submodule)
