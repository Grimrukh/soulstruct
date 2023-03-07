from __future__ import annotations

__all__ = ["ProjectWindow"]

# from soulstruct.models.bloodborne import CHARACTER_MODELS
from soulstruct.base.project.enums import ProjectDataType
from soulstruct.base.project.window import ProjectWindow as _BaseProjectWindow

from .core import GameDirectoryProject
from .links import WindowLinker
from .maps import MapsEditor


class ProjectWindow(_BaseProjectWindow):
    PROJECT_CLASS = GameDirectoryProject
    LINKER_CLASS = WindowLinker
    MAPS_EDITOR_CLASS = MapsEditor
    RUNTIME_MANAGER_CLASS = None
    CHARACTER_MODELS = {}  # TODO

    project: GameDirectoryProject

    def _build_tools_menu(self, tools_menu):
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
        for param_nickname in ("Weapons", "Armor", "Goods", "GemsAndRunes"):  # handful of "spells" not renamed
            params_menu.add_command(
                label=f"Rename {param_nickname} from Text",
                foreground="#FFF",
                command=lambda p=param_nickname: self._rename_param_entries_from_text(p),
            )
        return params_menu

    def _rename_param_entries_from_text(self, param_nickname: str = None):
        # TODO: Doesn't work properly for Gems and Runes yet.
        self.project.params.rename_entries_from_text(self.project.text, param_nickname=param_nickname)
        if self.current_data_type == ProjectDataType.Params:
            if (
                not param_nickname
                and self.params_tab.active_category in {"Weapons", "Armor", "Goods", "GemsAndRunes"}
                or param_nickname == self.params_tab.active_category
            ):
                self.params_tab.refresh_entries()
