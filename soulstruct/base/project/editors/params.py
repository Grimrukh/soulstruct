from __future__ import annotations

import logging
import typing as tp

from soulstruct.base.game_types import BaseParam
from soulstruct.base.params.utils import DynamicParamFieldInfo
from soulstruct.base.project.editors.base_editor import EntryRow
from soulstruct.base.project.editors.field_editor import FieldRow, BaseFieldEditor
from soulstruct.base.project.utilities import NameSelectionBox

if tp.TYPE_CHECKING:
    from soulstruct.base.params.param import ParamRow
    from soulstruct.base.params.gameparambnd import GameParamBND

_LOGGER = logging.getLogger(__name__)


class ParamFieldRow(FieldRow):

    def _is_default(self, field_type, value, field_nickname=""):
        # TODO: Each field should specify its default value(s).
        if field_nickname in {"EffectDuration", "UpdateInterval"}:
            return False
        elif field_type == int or issubclass(field_type, BaseParam):
            # TODO: Used to check `Flag` type in here as well, which is no longer a base type. Necessary?
            if value in (-1, 0, 1):
                # TODO: Will have some false positives.
                return True
        elif field_type == float:
            if field_nickname.endswith("Multiplier"):
                if value == 1.0:
                    return True
            else:
                if value in (0.0, 1.0):
                    return True
        return False


class ParamEntryRow(EntryRow):
    master: ParamsEditor

    ENTRY_ID_WIDTH = 10

    def __init__(self, editor: BaseFieldEditor, row_index: int, main_bindings: dict = None):
        super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)
        self.linked_text = ""

    def update_entry(self, entry_id: int, entry_text: str):
        """Adds linked text from text data (if present and not already identical to param entry name)."""
        self.entry_id = entry_id
        text_links = self.master.linker.get_param_entry_text_links(self.entry_id)
        self.linked_text = ""
        if text_links and text_links[0].name and text_links[0].name != entry_text:
            self.linked_text = f"    {{{text_links[0].name}}}"
        self.entry_text = entry_text
        self._update_colors()
        self.build_entry_context_menu(text_links)
        self.tool_tip.text = text_links[2].name if text_links and text_links[2].name else None

    @property
    def entry_text(self):
        return self._entry_text

    @entry_text.setter
    def entry_text(self, value):
        self._entry_text = value
        self.text_label.var.set(self._entry_text + (self.linked_text if self.linked_text is not None else ""))

    def build_entry_context_menu(self, text_links=()):
        super().build_entry_context_menu()
        self.context_menu.add_command(
            label="Duplicate Entry to Next Available ID",
            command=lambda: self.master.add_entry_to_next_available_id(self.entry_id),
        )
        text_links = self.master.linker.get_param_entry_text_links(self.entry_id)
        if text_links:
            self.context_menu.add_separator()
            for text_link in text_links:
                text_link.add_to_context_menu(self.context_menu, foreground=self.STYLE_DEFAULTS["text_fg"])
        if self.master.active_category in {"Weapons", "Armor", "Rings", "Goods", "Spells"}:
            self.context_menu.add_separator()
            self.context_menu.add_command(
                label="Edit All Text",
                command=lambda: self.master.edit_all_item_text(self.entry_id),
            )
        self.context_menu.add_separator()
        self.context_menu.add_command(
            label="Find References in Params",
            command=lambda: self.master.find_all_param_references(self.entry_id),
        )


class ParamsEditor(BaseFieldEditor):
    DATA_NAME = "Params"
    TAB_NAME = "params"
    CATEGORY_BOX_WIDTH = 165
    ENTRY_BOX_WIDTH = 350
    ENTRY_RANGE_SIZE = 300
    FIELD_BOX_WIDTH = 500
    FIELD_ROW_COUNT = 185  # highest count (Params[SpecialEffects] in Bloodborne)

    FIELD_ROW_CLASS = ParamFieldRow
    field_rows: list[ParamFieldRow]
    ENTRY_ROW_CLASS = ParamEntryRow
    entry_rows: list[ParamEntryRow]

    def __init__(self, project, linker, master=None, toplevel=False):
        self.go_to_param_id_entry = None
        self.search_result = None
        super().__init__(project, linker, master=master, toplevel=toplevel, window_title="Soulstruct Params Editor")

    @property
    def params(self) -> GameParamBND:
        return self._project.params

    def build(self):
        with self.set_master(sticky="nsew", row_weights=[0, 1], column_weights=[1], auto_rows=0):
            with self.set_master(pady=10, sticky="w", row_weights=[1], column_weights=[1, 1], auto_columns=0):
                self.go_to_param_id_entry = self.Entry(
                    label="Go to Param ID:", label_position="left", integers_only=True, width=30, padx=10
                )
                self.go_to_param_id_entry.bind("<Return>", self.go_to_param_id)
                self.search_result = self.Label(font_size=10, fg="#CCF").var

            super().build()

    def go_to_param_id(self, event):
        param_id = event.widget.var.get()
        if not param_id or self.active_category is None:
            self.flash_bg(self.go_to_param_id_entry)
            return
        param_id = int(param_id)
        params = self.get_category_data()
        if param_id not in params:
            # Find closest ID that is less than search target.
            params_above = [p_id for p_id in params if p_id < param_id]
            if not params_above:
                self.flash_bg(self.go_to_param_id_entry)
                return
            param_id = max(p_id for p_id in params if p_id < param_id)
            self.search_result.set(f"Found closest preceding entry: {param_id}")
            self.after(2000, lambda: self.search_result.set(""))
        self.select_entry_id(param_id, set_focus_to_text=False, edit_if_already_selected=False)

    def find_all_param_references(self, param_id):
        """Iterates over all ParamTables to find references to this param ID, and presents them in a floating list."""
        category = self.active_category
        param_type = self.params.PARAM_TYPES[category]
        linking_fields = []
        links = {}

        # Find all (param_name, field) pairs that could possibly reference this category.
        for param_name in self.params.PARAM_TYPES:
            param = self.params.get_param(param_name)
            for field_info in param.param_info["fields"]:
                if isinstance(field_info, DynamicParamFieldInfo):
                    # Field type will be checked below (per entry).
                    if param_type in field_info.POSSIBLE_TYPES:
                        linking_fields.append((param_name, field_info))
                elif field_info.field_type == param_type:
                    linking_fields.append((param_name, field_info))

        if not linking_fields:
            self.CustomDialog(
                "No References",
                "Could not find any fields in any Params that could possibly reference this entry type.\n"
                "There may still be references elsewhere (e.g. maps, events, animation TAE).",
            )
            return

        for param_name, field_info in linking_fields:
            for row_id, row in self.params.get_param(param_name).items():
                row_field_info = field_info(row)
                if row_field_info.field_type == param_type and row[row_field_info.name] == param_id:
                    link_text = f"{param_name}[{row_id}] {row_field_info.nickname}"
                    links[link_text] = (param_name, row_id, row_field_info.name)

        if not links:
            self.CustomDialog(
                "No References",
                "Could not find any references to this row in Params.\nThere may still be references elsewhere.",
            )
            return

        name_box = NameSelectionBox(self.master, names=links, list_name=f"Param References to {category}[{param_id}]")
        selected_link = name_box.go()
        if selected_link is not None:
            param_name, row_id, field_name = links[selected_link]
            self.select_category(param_name, auto_scroll=True)
            self.select_entry_id(row_id, edit_if_already_selected=False)
            self.select_field_name(field_name)

    def _get_display_categories(self):
        return self.params.PARAM_TYPES

    def get_category_data(self, category=None) -> dict:
        if category is None:
            category = self.active_category
            if category is None:
                return {}
        return self.params.get_param(category).rows

    def _get_category_name_range(self, category=None, first_index=None, last_index=None) -> list:
        if category is None:
            category = self.active_category
            if category is None:
                return []
        return self.params.get_param(category).get_range(start=self.first_display_index, count=self.ENTRY_RANGE_SIZE)

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get index of entry in category. Ignores current display range."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No param category selected.")
        if entry_id not in self.params.get_param(category).rows:
            raise ValueError(f"Param ID {entry_id} does not appear in category {category}.")
        return sorted(self.params.get_param(category).rows).index(entry_id)

    def get_entry_text(self, entry_id: int, category=None) -> str:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.params.get_param(category)[entry_id].name

    def _set_entry_text(self, entry_id: int, text: str, category=None, update_row_index=None):
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        self.params.get_param(category)[entry_id].name = text
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_id, text)

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        entry_data = self.params.get_param(category).pop(entry_id)
        self.params.get_param(category)[new_id] = entry_data
        if category == self.active_category and update_row_index:
            self.entry_rows[update_row_index].update_entry(new_id, entry_data.name)
        return True

    def get_field_dict(self, entry_id: int, category=None) -> ParamRow:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.params.get_param(category)[entry_id]

    def get_field_display_info(self, field_dict, field_name):
        display_info = field_dict.get_paramdef_field_display_info(field_name)
        return display_info.nickname, display_info.is_enabled, display_info.field_type, display_info.docstring

    def get_field_names(self, field_dict):
        return field_dict.field_names if field_dict else []

    def get_field_links(self, field_type, field_value, valid_null_values=None):
        if valid_null_values is None:
            valid_null_values = {0: "Default/None", -1: "Default/None"}
        else:
            print(field_type, field_value, valid_null_values)
        try:
            return self.linker.soulstruct_link(field_type, field_value, valid_null_values=valid_null_values)
        except IndexError:
            raise ValueError(f"Invalid link: type = {field_type}, value = {field_value}")

    def edit_all_item_text(self, item_id):
        """Active category should already be a valid item type."""
        try:
            self.linker.edit_all_item_text(self.active_category.rstrip("s"), item_id)
        except Exception as e:
            _LOGGER.warning(e)
            self.CustomDialog("Item Text Error", f"Could not edit item text. Error:\n\n{e}")
        else:
            self.refresh_entries()
