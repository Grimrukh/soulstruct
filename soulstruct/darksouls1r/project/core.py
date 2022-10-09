from __future__ import annotations

__all__ = ["GameDirectoryProject"]

import logging
import shutil
import typing as tp

from soulstruct.base.project import GameDirectoryProject as _BaseGameDirectoryProject
from soulstruct.darksouls1r.ai import AIDirectory
from soulstruct.darksouls1r.ezstate import TalkDirectory
from soulstruct.darksouls1r.events import EMEVDDirectory
from soulstruct.darksouls1r.maps import MapStudioDirectory
from soulstruct.darksouls1r.params import GameParamBND
from soulstruct.darksouls1r.params import DrawParamDirectory
from soulstruct.darksouls1r.text import MSGDirectory
from soulstruct.games import DarkSoulsDSRType
from soulstruct.utilities.files import PACKAGE_PATH

if tp.TYPE_CHECKING:
    from .window import ProjectWindow

_LOGGER = logging.getLogger(__name__)


class GameDirectoryProject(_BaseGameDirectoryProject, DarkSoulsDSRType):

    DATA_TYPES = {
        "ai": AIDirectory,
        "events": EMEVDDirectory,  # modified via EVS event script files
        "lighting": DrawParamDirectory,
        "maps": MapStudioDirectory,
        "params": GameParamBND,
        "talk": TalkDirectory,  # modified via ESP state machine script files
        "text": MSGDirectory,
    }

    ai: AIDirectory
    events: EMEVDDirectory
    lighting: DrawParamDirectory
    maps: MapStudioDirectory
    params: GameParamBND
    talk: TalkDirectory
    text: MSGDirectory

    def initialize_project(self, force_import_from_game=False, with_window: ProjectWindow = None, first_time=False):
        """Also offer to translate events/regions with entity IDs and export entities modules."""

        yes_to_all = force_import_from_game

        for data_type in self.DATA_TYPES:
            yes_to_all = self.import_data_type(data_type, force_import_from_game, yes_to_all, with_window=with_window)

            if data_type == "maps" and first_time and self.maps is not None:
                archives_msb = self.maps.DukesArchives
                repeats = archives_msb.get_repeated_entity_ids()
                if {e.entity_id for e in repeats["Regions"]} == {1702745, 1702746, 1702747, 1702748}:
                    if self.offer_fix_broken_regions(with_window):
                        self.save("maps")
                if self.offer_translate_entities(with_window=with_window):
                    self.save("maps")
                    self.offer_entities_export(with_window=with_window)

        if "events" in self.DATA_TYPES:
            self.import_events(force_import=yes_to_all, with_window=with_window)
            self.offer_events_submodule_copy(with_window=with_window)

        if "talk" in self.DATA_TYPES:
            self.import_talk(force_import=yes_to_all, with_window=with_window)

    def copy_events_submodule(self):
        """Also need PTDE submodule for DSR."""
        super().copy_events_submodule()
        name = "darksouls1ptde"
        events_submodule = PACKAGE_PATH(f"{name}/events")
        (self.project_root / f"events/soulstruct/{name}").mkdir(parents=True, exist_ok=True)
        shutil.copytree(events_submodule, self.project_root / f"events/soulstruct/{name}/events")
        _LOGGER.info(f"Copied `soulstruct.{name}.events` submodule into project events folder (needed for DSR).")

    def offer_fix_broken_regions(self, with_window: ProjectWindow = None):
        """Offer to fix broken regions in Duke's Archives."""
        if with_window:
            result = with_window.CustomDialog(
                title="Region Cleanup",
                message="In vanilla Dark Souls, the Duke's Archives has four unused regions that can break event\n"
                        "scripts. Would you like Soulstruct to delete those four regions now?",
                button_names=("Yes, delete them", "No, leave them be"),
                button_kwargs=("YES", "NO"),
                cancel_output=1,
                default_output=1,
            )
        else:
            result = 1 if (
                input(
                    "In vanilla Dark Souls, the Duke's Archives has four unused regions that can break event\n"
                    "scripts. Would you like Soulstruct to delete those four regions now? [y]/n",
                ).lower() == "n"
            ) else 0
        if result == 0:
            archives_msb = self.maps.DukesArchives
            repeats = archives_msb.get_repeated_entity_ids()  # re-checking just in case
            if {e.entity_id for e in repeats["Regions"]} == {1702745, 1702746, 1702747, 1702748}:
                for entry in repeats["Regions"]:
                    archives_msb.regions.delete_entry(entry)
            return True
        else:
            return False

    def offer_translate_entities(self, with_window: ProjectWindow = None):
        """Offer to translate event/region entry names with entity IDs."""
        if with_window:
            result = with_window.CustomDialog(
                title="Entry Translation",
                message="Would you like to translate vanilla event/region MSB entries with entity IDs?\n"
                        "This is necessary to properly export their names as event entities for EVS scripting,\n"
                        "but will overwrite any name changes you've made for vanilla entity IDs.",
                button_names=("Yes, translate them", "No, leave them be"),
                button_kwargs=("YES", "NO"),
                cancel_output=1,
                default_output=1,
            )
        else:
            result = 1 if (
                input(
                    "Would you like to translate vanilla event/region MSB entries with entity IDs?\n"
                    "This is necessary to properly export their names as event entities for EVS scripting,\n"
                    "but will overwrite any name changes you've made for vanilla entity IDs. [y]/n",
                ).lower() == "n"
            ) else 0
        if result == 0:
            for msb in self.maps.msbs.values():
                msb.translate_entity_id_names()
            return True
        else:
            return False

    def offer_entities_export(self, with_window: ProjectWindow = None):
        """Offer to export all entities modules."""
        # TODO: Offer to automatically set MSB entity ID sync with modules.
        if with_window:
            result = with_window.CustomDialog(
                title="Entities Export",
                message="Would you also like to export all 'entities' Python modules for EVS use?\n",
                # TODO: Third option for automatic sync.
                button_names=("Yes, export them", "No, don't write them"),
                button_kwargs=("YES", "NO"),
                cancel_output=1,
                default_output=1,
            )
        else:
            result = 1 if (
                input(
                    "Would you also like to export all 'entities' Python modules for EVS use? [y]/n"
                ).lower() == "n"
            ) else 0
        if result == 0:

            if with_window:
                write_vanilla_entities_result = with_window.CustomDialog(
                    title="Entities Export",
                    message="Would you also like to include pre-identified game IDs in the 'entities' module?\n",
                    button_names=("Yes, include them", "No, just write entities in entities"),
                    button_kwargs=("YES", "NO"),
                    cancel_output=1,
                    default_output=1,
                )
            else:
                write_vanilla_entities_result = 1 if (
                    input(
                        "Would you also like to include pre-identified game IDs in the 'entities' module?\n",
                    ).lower() == "n"
                ) else 0

            # NOTE: Vanilla entities are read from PTDE directory.

            if write_vanilla_entities_result == 0:
                # Write vanilla `common` entities, if it exists.
                try:
                    vanilla_common_entities = PACKAGE_PATH(
                        f"darksouls1ptde/events/vanilla_entities/common_entities.py"
                    ).read_text()
                except FileNotFoundError:
                    _LOGGER.warning("Could not find `common_entities.py` in Soulstruct for this game. Ignoring.")
                    pass
                else:
                    _LOGGER.info("Writing `common_entities.py` to project from Soulstruct.")
                    common_entities_path = self.project_root / f"entities/common_entities.py"
                    common_entities_path.parent.mkdir(parents=True, exist_ok=True)
                    common_entities_path.write_text(vanilla_common_entities)
                    # `EMEVDDirectory.to_evs()` will automatically add non-star imports from `common` if it exists.

            for map_name, msb in self.maps.msbs.items():
                game_map = self.maps.GET_MAP(map_name)

                if write_vanilla_entities_result == 0:
                    self.include_vanila_entities = True

                msb.write_entities_module(
                    self.project_root / f"entities/{game_map.emevd_file_stem}_entities.py",
                    include_vanilla_entities=self.include_vanila_entities
                )
            return True
        else:
            return False
