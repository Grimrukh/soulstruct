import logging

from soulstruct.base.project.exceptions import SoulstructProjectError
from soulstruct.base.project.window import ProjectWindow as _BaseProjectWindow
from soulstruct.darksouls1r.maps.utilities import build_ffxbnd
from soulstruct.darksouls1r.constants import CHARACTER_MODELS
from .core import GameDirectoryProject
from .lighting import LightingEditor
from .links import WindowLinker
from .runtime import RuntimeManager

_LOGGER = logging.getLogger(__name__)


class ProjectWindow(_BaseProjectWindow):
    PROJECT_CLASS = GameDirectoryProject
    LINKER_CLASS = WindowLinker
    LIGHTING_EDITOR_CLASS = LightingEditor
    RUNTIME_MANAGER_CLASS = RuntimeManager
    CHARACTER_MODELS = CHARACTER_MODELS

    project: GameDirectoryProject
    runtime_tab: RuntimeManager

    def _build_tools_menu(self, tools_menu):
        maps_submenu = self.Menu(tearoff=0)
        self._build_maps_submenu(maps_submenu)
        tools_menu.add_cascade(label="Maps", foreground="#FFF", menu=maps_submenu)

        params_submenu = self.Menu(tearoff=0)
        self._build_params_submenu(params_submenu)
        tools_menu.add_cascade(label="Params", foreground="#FFF", menu=params_submenu)

        tools_menu.add_separator()

        super()._build_tools_menu(tools_menu)

    def _build_params_submenu(self, params_menu):
        params_menu.add_command(
            label="Rename All Items/Equipment from Text",
            foreground="#FFF",
            command=self._rename_param_entries_from_text,
        )
        for param_table in ("Weapons", "Armor", "Rings", "Goods", "Spells"):
            params_menu.add_command(
                label=f"Rename {param_table} from Text",
                foreground="#FFF",
                command=lambda p=param_table: self._rename_param_entries_from_text(p),
            )
        return params_menu

    def _build_maps_submenu(self, maps_menu):
        maps_menu.add_command(
            label="Rebuild FFXBNDs from Maps",
            foreground="#FFF",
            command=self._rebuild_ffxbnds_from_maps,
        )
        maps_menu.add_command(
            label="Translate Vanilla Event/Region Entries with Entity IDs",
            foreground="#FFF",
            command=self._translate_all_event_region_entity_id_names,
        )

    def _rename_param_entries_from_text(self, param_table=None):
        # TODO: Add `rename_entries_from_text` method to supported games (or base class, even).
        self.project.params.rename_entries_from_text(self.project.text, param_nickname=param_table)
        if self.page_tabs.index(self.page_tabs.select()) == self.ordered_tabs.index("params"):
            if (
                not param_table
                and self.params_tab.active_category in {"Weapons", "Armor", "Rings", "Goods", "Spells"}
                or param_table == self.params_tab.active_category
            ):
                self.params_tab.refresh_entries()

    def _rebuild_ffxbnds_from_maps(self):
        """Rebuild game FFXBND file for each map based on current characters in project."""
        if self.project.GAME.name != "Dark Souls Remastered":
            raise SoulstructProjectError("FFXBND Rebuilder is currently only available for Dark Souls Remastered.")
        vanilla_game_root = self.project.vanilla_game_root
        if vanilla_game_root == self.project.game_root:
            _LOGGER.warning(
                "No 'VanillaGameDirectory' given in project config. Using FFXBND files ('.bak' if possible) in "
                "standard game directory as sources, which may cause issues if you are modifying them more than once "
                "and removing the initial backups."
            )

        def _threaded_rebuild_ffxbnd():
            for map_name, msb in self.project.maps.msbs.items():
                game_map = self.project.maps.GET_MAP(map_name)
                if not game_map.ffxbnd_file_name:
                    _LOGGER.warning(f"No FFXBND file name known for map: {map_name}. Nothing written.")
                build_ffxbnd(
                    msb,
                    ffxbnd_path=self.project.game_root / f"sfx/{game_map.ffxbnd_file_name}.ffxbnd.dcx",
                    ffxbnd_search_directory=vanilla_game_root / "sfx",
                    prefer_bak=True,
                )

        try:
            self._thread_with_loading_dialog(
                "Rebuilding FFXBNDs",
                "Rebuilding FFXBND files from current Maps data...",
                _threaded_rebuild_ffxbnd,
            )
        except Exception as ex:
            message = (f"Error occurred while rebuilding FFXBND files:\n\n"
                       f"{ex}\n\n"
                       f"Only some FFXBND files may have been written.")
            return self.CustomDialog(title="FFXBND Error", message=message)

    def _translate_all_event_region_entity_id_names(self):
        """Translate all MSB entry names that have entity IDs.

        Allows events and regions with Japanese names to be written to entities module. Parts should already be valid
        identifiers, but are checked as well anyway.
        """
        for msb in self.project.maps.msbs.values():
            msb.translate_entity_id_names()
