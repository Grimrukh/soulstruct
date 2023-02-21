from __future__ import annotations

__all__ = ["GameDirectoryProject"]

import typing as tp

from soulstruct.base.project.core import GameDirectoryProject as _BaseGameDirectoryProject

from soulstruct.eldenring.events import EventDirectory
from soulstruct.eldenring.events.create_vanilla_entities import copy_vanilla_entities
from soulstruct.eldenring.text import MSGDirectory

if tp.TYPE_CHECKING:
    from .window import ProjectWindow


class GameDirectoryProject(_BaseGameDirectoryProject):
    DATA_TYPES = {
        # "ai": AIScriptDirectory,
        "events": EventDirectory,
        # "lighting": DrawParamDirectory,
        # "maps": MapStudioDirectory,
        # "params": GameParamBND,
        # "talk": TalkDirectory,
        "text": MSGDirectory,
    }

    events: EventDirectory
    text: MSGDirectory

    def warn_long_event_import(self, with_window: ProjectWindow = None):
        if with_window:
            with_window.CustomDialog(
                title="Long Operation Warning",
                message="Decompiling events using entities. This may take a while!\n"
                        "The project window will appear when ready.",
            )
        else:
            print(
                "Decompiling events using entities. This may take a while!\n"
                "The project window will appear when done."
            )

    def import_Events(self, force_import=False, with_window: ProjectWindow = None):
        """Offers entities directory creation."""
        events_dir = self.project_root / "events"
        entities_dir = self.entities_directory
        events_exist = events_dir.is_dir() and events_dir.glob("*")

        if not entities_dir.is_dir():
            if with_window:
                result = with_window.CustomDialog(
                    title="Entities Import",
                    message=f"Could not find any event entities in project.\n"
                            f"Would you like to copy vanilla entities from Soulstruct or \n"
                            f"ignore them and use only numerical entity IDs in event scripts?",
                    button_names=("Yes, copy from Soulstruct", "No, I don't want entities"),
                    button_kwargs=("YES", "NO"),
                    cancel_output=1,
                    default_output=0,
                )
            else:
                result = 1 if (
                    input(
                        f"Could not find any event scripts in project.\n"
                        f"Would you like to create them from scratch now? [y]/n "
                    ).lower() == "n"
                ) else 0

            if result == 0:
                # Copy from Soulstruct.
                copy_vanilla_entities(entities_dir)
                if events_exist:
                    # Offer recreation of event scripts.
                    if with_window:
                        overwrite_result = with_window.CustomDialog(
                            title="Re-import Events",
                            message=f"Entities have been created, but there are already events in this project.\n"
                                    f"Would you like to re-import them from the game now to use entity names?\n"
                                    f"This will overwrite any existing script changes!",
                            button_names=("Yes, OVERWRITE them", "No, KEEP my scripts"),
                            button_kwargs=("YES", "NO"),
                            cancel_output=1,
                            default_output=1,
                        )
                    else:
                        overwrite_result = 1 if (
                            input(
                                f"Entities created, but project already has event scripts.\n"
                                f"Would you like to re-import and OVERWRITE them from the game now? [y]/n "
                            ).lower() == "n"
                        ) else 0
                    if overwrite_result == 0:
                        force_import = True
                        events_exist = False

        if not events_exist:
            if force_import:
                if self.entities_directory.is_dir():
                    self.warn_long_event_import(with_window=with_window)
                self.import_data_from_game("events")
            else:
                if with_window:
                    result = with_window.CustomDialog(
                        title="Project Error",
                        message=f"Could not find any event scripts in project.\n"
                                f"Would you like to decompile and import them from the game directory now?",
                        button_names=("Yes", "No, I'll handle events"),
                        button_kwargs=("YES", "NO"),
                        cancel_output=1,
                        default_output=1,
                    )
                else:
                    result = 1 if (
                        input(
                            f"Could not find any event scripts in project.\n"
                            f"Would you like to import them from the game directory now? [y]/n "
                        ).lower() == "n"
                    ) else 0
                if result == 0:
                    if self.entities_directory.is_dir():
                        self.warn_long_event_import(with_window=with_window)
                    self.import_data_from_game("events")
