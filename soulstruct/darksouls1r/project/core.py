from __future__ import annotations

__all__ = ["GameDirectoryProject"]

import logging
import shutil
import typing as tp
from pathlib import Path

from soulstruct.base.project import GameDirectoryProject as _BaseGameDirectoryProject, ProjectDataType
from soulstruct.darksouls1r.ai import AIScriptDirectory
from soulstruct.darksouls1r.ezstate import TalkDirectory
from soulstruct.darksouls1r.events import EventDirectory
from soulstruct.darksouls1r.maps import MapStudioDirectory, MSB
from soulstruct.darksouls1r.params import GameParamBND
from soulstruct.darksouls1r.params import DrawParamDirectory
from soulstruct.darksouls1r.text import MSGDirectory
from soulstruct.utilities.files import PACKAGE_PATH

if tp.TYPE_CHECKING:
    from .window import ProjectWindow

_LOGGER = logging.getLogger(__name__)


class GameDirectoryProject(_BaseGameDirectoryProject):

    DATA_TYPES = {
        ProjectDataType.AI: AIScriptDirectory,
        ProjectDataType.Events: EventDirectory,  # modified via EVS event script files
        ProjectDataType.Lighting: DrawParamDirectory,
        ProjectDataType.Maps: MapStudioDirectory,
        ProjectDataType.Params: GameParamBND,
        ProjectDataType.Talk: TalkDirectory,  # modified via ESP state machine script files
        ProjectDataType.Text: MSGDirectory,
    }

    ai: AIScriptDirectory
    lighting: DrawParamDirectory
    maps: MapStudioDirectory
    params: GameParamBND
    text: MSGDirectory

    def get_data_type_import_settings(self, data_type: ProjectDataType) -> dict[str, tuple[str, bool, str]]:
        base_dict = super().get_data_type_import_settings(data_type)
        if data_type == ProjectDataType.Maps:
            base_dict |= dict(
                use_bundled_vanilla_enums=(
                    "Use Vanilla Entities from Soulstruct", True,
                    "Use the renamed (vanilla) game IDs included with Soulstruct for this game."
                ),
                translate_japanese_map_entity_names=(
                    "Translate Japanese Map Entity Names", True,
                    "Apply bundled translations for vanilla event/region MSB entries with entity IDs. "
                    "This is necessary to use their names as variables event entities in EVS scripts, "
                    "but will overwrite any name changes you've already made to the names of those MSB entries.",
                ),
                remove_broken_regions=(
                    "Remove Broken Duke's Archives Regions", True,
                    "In vanilla Dark Souls, the Duke's Archives has four unused regions that can break event\n"
                    "scripts. Would you like Soulstruct to delete those four regions now?",
                ),
            )
        return base_dict

    def write_vanilla_entities(self, map_studio_directory: MapStudioDirectory, in_events_folder=False):
        # Write vanilla `common` entities, if it exists.
        enums_dir = self.project_root / ("events" if in_events_folder else "enums")
        try:
            vanilla_common_entities = PACKAGE_PATH(
                f"darksouls1ptde/events/vanilla_entities/common_entities.py"
            ).read_text()
        except FileNotFoundError:
            _LOGGER.warning("Could not find `common_entities.py` in Soulstruct for this game. Ignoring.")
            pass
        else:
            _LOGGER.info("Writing `common_entities.py` to project from Soulstruct.")
            common_entities_path = enums_dir / "common_enums.py"
            common_entities_path.parent.mkdir(parents=True, exist_ok=True)
            common_entities_path.write_text(vanilla_common_entities)
            # `EventDirectory.to_evs()` will automatically add non-star imports from `common` if it exists.

        for map_stem, msb in map_studio_directory.files.items():
            game_map = map_studio_directory.GET_MAP(map_stem)
            try:
                vanilla_module = PACKAGE_PATH(
                    f"darksouls1ptde/events/vanilla_entities/{game_map.emevd_file_stem}_entities.py"
                ).read_text()
            except FileNotFoundError:
                vanilla_module = ""
            msb.write_entities_module(
                enums_dir / f"{game_map.emevd_file_stem}_enums.py",
                append_to_module=vanilla_module,
            )

    def import_Maps(
        self,
        import_directory: Path | str,
        put_enums_in_events_folder=False,
        use_bundled_vanilla_enums=True,
        translate_japanese_map_entity_names=True,
        remove_broken_regions=True,
    ):
        maps = self._default_import(ProjectDataType.Maps, import_directory)  # type: MapStudioDirectory

        if translate_japanese_map_entity_names:
            # NOTE: Must be done BEFORE writing `enums` modules below.
            for msb in maps.files.values():
                msb: MSB
                msb.translate_entity_id_names()

        if use_bundled_vanilla_enums:
            self.write_vanilla_entities(maps)

        if remove_broken_regions:
            archives_msb = maps.DukesArchives
            repeats = archives_msb.get_repeated_entity_ids()
            if {e.get_entity_id() for e in repeats["POINT_PARAM_ST"]} == {1702745, 1702746, 1702747, 1702748}:
                for entry in repeats["POINT_PARAM_ST"]:
                    archives_msb.remove_entry(entry)

        self._set_data(ProjectDataType.Maps, maps)

    def copy_events_submodule(self, with_window: ProjectWindow = None):
        """Also need PTDE submodule for DSR."""
        super().copy_events_submodule()
        name = "darksouls1ptde"
        events_submodule = PACKAGE_PATH(f"{name}/events")
        (self.project_root / f"events/soulstruct/{name}").mkdir(parents=True, exist_ok=True)
        shutil.copytree(events_submodule, self.project_root / f"events/soulstruct/{name}/events")
        _LOGGER.info(f"Copied `soulstruct.{name}.events` submodule into project events folder (needed for DSR).")
