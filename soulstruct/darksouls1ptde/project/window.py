from soulstruct.darksouls1ptde.models import CHARACTER_MODELS
from soulstruct.base.project.window import ProjectWindow as _BaseProjectWindow

from .core import GameDirectoryProject
from .runtime import RuntimeManager


class ProjectWindow(_BaseProjectWindow):
    PROJECT_CLASS = GameDirectoryProject
    RUNTIME_MANAGER_CLASS = RuntimeManager
    CHARACTER_MODELS = CHARACTER_MODELS

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
        for param_table in ("Weapons", "Armor", "Rings", "Goods", "Spells"):
            params_menu.add_command(
                label=f"Rename {param_table} from Text",
                foreground="#FFF",
                command=lambda p=param_table: self._rename_param_entries_from_text(p),
            )
        return params_menu

    def _rename_param_entries_from_text(self, param_table=None):
        self.project.params.rename_entries_from_text(self.project.text, param_nickname=param_table)
        if self.page_tabs.index(self.page_tabs.select()) == self.ordered_tabs.index("params"):
            if (
                not param_table
                and self.params_tab.active_category in {"Weapons", "Armor", "Rings", "Goods", "Spells"}
                or param_table == self.params_tab.active_category
            ):
                self.params_tab.refresh_entries()
