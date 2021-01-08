from __future__ import annotations

import typing as tp

from soulstruct.project.base.editors.base_editor import EntryRow
from soulstruct.project.base.editors.field_editor import BaseFieldEditor

if tp.TYPE_CHECKING:
    from soulstruct.params.base.param import Param, ParamRow
    from soulstruct.params.base.draw_param import DrawParamDirectory


class LightingEntryRow(EntryRow):

    master: LightingEditor

    ENTRY_ID_WIDTH = 10

    def __init__(self, editor: BaseFieldEditor, row_index: int, main_bindings: dict = None):
        super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)
        self.linked_text = ""

    def update_entry(self, entry_id: int, entry_text: str):
        """If 'linked_text' is an empty string, then text was expected, but not found (entry highlighted)."""
        self.entry_id = entry_id
        text_links = self.master.linker.param_entry_text_link(self.entry_id)
        self.linked_text = (f"    {{{text_links[0].name}}}" if text_links[0].name else "") if text_links else None
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
        text_links = self.master.linker.param_entry_text_link(self.entry_id)
        if text_links:
            self.context_menu.add_separator()
            for text_link in text_links:
                text_link.add_to_context_menu(self.context_menu, foreground=self.STYLE_DEFAULTS["text_fg"])


class LightingEditor(BaseFieldEditor):
    DATA_NAME = "Lighting"
    TAB_NAME = "lighting"
    CATEGORY_BOX_WIDTH = 165
    ENTRY_BOX_WIDTH = 350
    ENTRY_RANGE_SIZE = 200
    FIELD_BOX_WIDTH = 500
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_COUNT = 45  # highest count (AmbientLight)

    ENTRY_ROW_CLASS = LightingEntryRow
    entries: list[LightingEntryRow]

    def __init__(self, lighting: DrawParamDirectory, linker, master=None, toplevel=False):
        self.lighting = lighting
        self.map_area_choice = None
        self.slot_choice_label = None
        self.slot_choice = None
        super().__init__(linker, master=master, toplevel=toplevel, window_title="Soulstruct Lighting Editor")
        self._on_map_area_choice()  # Sets slot option correctly.

    def build(self):
        with self.set_master(sticky="nsew", row_weights=[0, 1], column_weights=[1], auto_rows=0):

            with self.set_master(pady=10, sticky="w", row_weights=[1], column_weights=[1, 0, 0, 1], auto_columns=0):
                map_display_names = [f"{k} [{v}]" for k, v in self.lighting.DRAW_PARAM_MAPS.items()]
                self.map_area_choice = self.Combobox(
                    values=map_display_names,
                    on_select_function=self._on_map_area_choice,
                    width=40,
                    padx=10,
                    label="Map Area:",
                    label_font_size=12,
                    label_position="left",
                    font=("Segoe UI", 12),
                ).var
                self.slot_choice_label = self.Label(text="Slot:", font_size=10, padx=(30, 0))
                self.slot_choice = self.Combobox(
                    values=("0", "1"), font=("Segoe UI", 10), on_select_function=self._on_slot_choice, width=2, padx=10
                )
                self.Button(
                    text="Copy Slot 0 to Slot 1",
                    bg="#622",
                    width=20,
                    font_size=10,
                    padx=5,
                    command=self.regenerate_slot_1,
                )

            super().build()

    def _on_map_area_choice(self, _=None):
        new_map_area = self.get_map_area_name()
        self._set_valid_slot_values(new_map_area)
        self.select_entry_row_index(None)
        self.refresh_entries(reset_field_display=True)

    def _on_slot_choice(self, _=None):
        self.select_entry_row_index(None)
        self.refresh_entries(reset_field_display=True)

    def _set_valid_slot_values(self, map_area):
        if getattr(self.lighting, map_area).AmbientLight[1] is None:  # random table to check slots
            self.slot_choice.config(values=["0"])
            if self.slot_choice.var.get() == "1":
                self.flash_bg(self.slot_choice_label)
            self.slot_choice.var.set("0")
        else:
            self.slot_choice.config(values=["0", "1"])

    def go_to_area_and_slot(self, area_name, slot):
        if area_name not in self.lighting.DRAW_PARAM_MAPS:
            raise KeyError(f"Invalid area name linked: {area_name}")
        full_area_name = f"{area_name} [{self.lighting.DRAW_PARAM_MAPS[area_name]}]"
        self.map_area_choice.set(full_area_name)
        self._set_valid_slot_values(area_name)
        self.slot_choice.var.set(str(slot))
        self.refresh_entries(reset_field_display=True)

    def regenerate_slot_1(self):
        map_area = self.get_map_area_name()
        map_draw_param = getattr(self.lighting, map_area)
        if map_draw_param["AmbientLight"][1] is not None:  # picking a random category to check slots
            if (
                self.CustomDialog(
                    title="Overwrite Slot 1?",
                    message="Current map area already has data in slot 1. Overwrite it from slot 0?",
                    button_names=("Yes, overwrite it", "No, do nothing"),
                    button_kwargs=("YES", "NO"),
                    cancel_output=1,
                    default_output=1,
                )
                == 1
            ):
                return
        map_draw_param.copy_slot_0_to_slot_1()
        self.slot_choice.config(values=["0", "1"])
        self.refresh_entries(reset_field_display=True)

    def get_map_area_name(self):
        return self.map_area_choice.get().split(" [")[0]

    def _get_display_categories(self):
        return self.lighting.PARAM_NAMES

    def get_category_data(self, category=None) -> tp.Union[Param, dict]:
        if category is None:
            category = self.active_category
            if category is None:
                return {}
        map_area_choice = self.get_map_area_name()
        slot_choice = int(self.slot_choice.var.get())
        return self.lighting.get_draw_param_bnd(map_area_choice).get_param(category)[slot_choice]

    def _get_category_name_range(self, category=None, first_index=None, last_index=None) -> list:
        if category is None:
            category = self.active_category
            if category is None:
                return []
        return self.get_category_data(category).get_range(start=self.first_display_index, count=self.ENTRY_RANGE_SIZE)

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get index of entry in category. Ignores current display range."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No param category selected.")
        if entry_id not in self.get_category_data(category).rows:
            raise ValueError(f"Param ID {entry_id} does not appear in category {category}.")
        return sorted(self.get_category_data(category).rows).index(entry_id)

    def get_entry_text(self, entry_id: int, category=None) -> str:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.get_category_data(category)[entry_id].name

    def _set_entry_text(self, entry_id: int, text: str, category=None, update_row_index=None):
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        self.get_category_data(category)[entry_id].name = text
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_id, text)

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        entry_data = self.get_category_data(category).pop(entry_id)
        self.get_category_data(category)[new_id] = entry_data
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(new_id, entry_data.name)
        return True

    def get_field_dict(self, entry_id: int, category=None) -> ParamRow:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.get_category_data(category)[entry_id]

    def get_field_display_info(self, field_dict, field_name):
        display_info = field_dict.get_paramdef_field_display_info(field_name)
        return display_info.nickname, display_info.is_enabled, display_info.field_type, display_info.description

    def get_field_names(self, field_dict):
        return field_dict.field_names if field_dict else []

    def get_field_links(self, field_type, field_value, valid_null_values=None):
        if valid_null_values is None:
            valid_null_values = {0: "Default/None", -1: "Default/None"}
        return self.linker.soulstruct_link(field_type, field_value, valid_null_values=valid_null_values)
