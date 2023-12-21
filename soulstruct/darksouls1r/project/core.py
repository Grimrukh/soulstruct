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
from soulstruct.darksouls1r.maps import MapStudioDirectory
from soulstruct.darksouls1r.params import GameParamBND
from soulstruct.darksouls1r.params import DrawParamDirectory
from soulstruct.darksouls1r.text import MSGDirectory
from soulstruct.utilities.files import PACKAGE_PATH

if tp.TYPE_CHECKING:
    from .window import ProjectWindow

_LOGGER = logging.getLogger(__name__)


class GameDirectoryProject(_BaseGameDirectoryProject):

    # This also determines load order, which is important for some types (e.g. Maps -> Enums -> Events).
    DATA_TYPES = {
        ProjectDataType.Params: GameParamBND,
        ProjectDataType.Lighting: DrawParamDirectory,
        ProjectDataType.AI: AIScriptDirectory,
        ProjectDataType.Talk: TalkDirectory,  # modified via ESP state machine script files
        ProjectDataType.Text: MSGDirectory,
        ProjectDataType.Maps: MapStudioDirectory,
        ProjectDataType.Enums: None,  # modified via Python modules; must be loaded after `Maps`
        ProjectDataType.Events: EventDirectory,  # modified via EVS event script files
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
                translate_japanese_map_entity_names=(
                    "Translate Japanese Map Entity Names", True,
                    "Apply bundled translations for vanilla event/region MSB entries with entity IDs. "
                    "This is necessary to use their names as variables event entities in EVS scripts, "
                    "but will overwrite any name changes you've already made to the names of those MSB entries.",
                ),
                remove_broken_regions=(
                    "Remove Broken Duke's Archives Regions", True,
                    "In vanilla Dark Souls, the Duke's Archives has four unused regions that can break event\n"
                    "scripts. It is highly recommended that you use this option to immediately delete them.",
                ),
            )
        elif data_type == ProjectDataType.Enums:
            base_dict |= dict(
                use_bundled_vanilla_enums=(
                    "Use Vanilla Entities from Soulstruct", False,  # TODO: disabling by default for now
                    "Use the renamed (vanilla) game IDs included with Soulstruct for this game.",
                ),
            )

        return base_dict

    def write_enums_modules_with_bundled_vanilla(self, map_studio_directory: MapStudioDirectory):
        """Write vanilla enums packaged with Soulstruct for DSR (adding any new entries in MSB).

        TODO: These need to be MERGED with newly written enums from an MSB, but it's not clear how to handle precedence,
         since we want to overwrite crappy vanilla names BUT keep any custom names the user has added.

        TODO: Uses vanilla enums from PTDE, which are currently only those shared in both versions.
        """
        try:
            vanilla_common_enums = PACKAGE_PATH(
                f"darksouls1ptde/events/vanilla/enums/common_enums.py"
            ).read_text()
        except FileNotFoundError:
            _LOGGER.warning("Could not find `common_enums.py` in Soulstruct for this game. Ignoring.")
            pass
        else:
            _LOGGER.info("Writing `common_enums.py` to project from Soulstruct.")
            common_enums_path = self.enums_directory / "common_enums.py"
            common_enums_path.parent.mkdir(parents=True, exist_ok=True)
            common_enums_path.write_text(vanilla_common_enums)
            # `EventDirectory.to_evs()` will automatically add non-star imports from `common` if it exists.

        for map_stem, msb in map_studio_directory.files.items():
            game_map = map_studio_directory.GET_MAP(map_stem)
            try:
                vanilla_module = PACKAGE_PATH(
                    f"darksouls1ptde/events/vanilla/enums/{game_map.emevd_file_stem}_enums.py"
                ).read_text()
            except FileNotFoundError:
                vanilla_module = ""
            msb.write_enums_module(
                self.enums_directory / f"{game_map.emevd_file_stem}_enums.py",
                append_to_module=vanilla_module,
            )

    def import_Maps(
        self,
        import_directory: Path | str,
        put_enums_in_events_folder=False,
        translate_japanese_map_entity_names=True,
        remove_broken_regions=True,
    ):
        maps = self._default_import(ProjectDataType.Maps, import_directory)  # type: MapStudioDirectory

        # Delete broken regions (if requested) before translating names, to avoid extra warnings.
        if remove_broken_regions:
            archives_msb = maps.DukesArchives
            repeats = archives_msb.get_repeated_entity_ids()
            if {e.get_entity_id() for e in repeats["POINT_PARAM_ST"]} == {1702745, 1702746, 1702747, 1702748}:
                for entry in repeats["POINT_PARAM_ST"]:
                    archives_msb.remove_entry(entry)

        if translate_japanese_map_entity_names:
            # NOTE: Must be done BEFORE writing `enums` modules below.
            for msb_name, msb in maps.files.items():
                _LOGGER.info(f"Translating Japanese entity names in {msb_name}.msb...")
                msb.translate_entity_id_names()

        self._set_data(ProjectDataType.Maps, maps)

    def import_Enums(
        self,
        import_directory: Path | str,
        use_loaded_maps_data=True,
        put_enums_in_events_folder=False,
        use_bundled_vanilla_enums=True,
    ):
        """Generates `{map_stem}_enums.py` modules from MSBs.

        Uses existing `maps` data if available and `use_maps_data` is True. Otherwise, imports temporary MSBs.
        """
        if use_loaded_maps_data and self.maps:
            maps = self.maps
        else:  # temporary MSB import
            maps = self._default_import(ProjectDataType.Maps, import_directory)  # type: MapStudioDirectory

        if put_enums_in_events_folder and ProjectDataType.Events not in self.DATA_TYPES:
            _LOGGER.warning("Cannot put enums modules in 'events' folder when game project does not support Events.")
            put_enums_in_events_folder = False

        self.enums_in_events_folder = put_enums_in_events_folder

        if use_bundled_vanilla_enums:
            # Enums modules will contain predefined vanilla MSB entity IDs *and* any new IDs from the MSB.
            self.write_enums_modules_with_bundled_vanilla(maps)
        else:
            # Enums modules will only contain IDs from the MSB, with their MSB names.
            enums_folder = self.enums_directory
            for map_stem, msb in maps.files.items():
                game_map = maps.GET_MAP(map_stem)
                msb.write_enums_module(enums_folder / f"{game_map.emevd_file_stem}_enums.py")

    def copy_events_submodule(self, with_window: ProjectWindow = None):
        """Also need PTDE submodule for DSR."""
        super().copy_events_submodule()
        name = "darksouls1ptde"
        events_submodule = PACKAGE_PATH(f"{name}/events")
        (self.project_root / f"events/soulstruct/{name}").mkdir(parents=True, exist_ok=True)
        shutil.copytree(events_submodule, self.project_root / f"events/soulstruct/{name}/events")
        _LOGGER.info(f"Copied `soulstruct.{name}.events` submodule into project events folder (needed for DSR).")
