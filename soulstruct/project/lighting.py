from __future__ import annotations

from typing import Union, TYPE_CHECKING

from soulstruct.params.dark_souls_params import DRAW_PARAM_MAPS
from soulstruct.project.editor import SoulstructBaseFieldEditor
if TYPE_CHECKING:
    from soulstruct.params import DarkSoulsLightingParameters, ParamTable, ParamEntry


class SoulstructLightingEditor(SoulstructBaseFieldEditor):
    CATEGORY_BOX_WIDTH = 165
    ENTRY_BOX_WIDTH = 350
    ENTRY_RANGE_SIZE = 200
    FIELD_BOX_WIDTH = 500
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_COUNT = 45  # highest count (AmbientLight)

    class EntryRow(SoulstructBaseFieldEditor.EntryRow):
        ENTRY_ID_WIDTH = 10

        def __init__(self, editor: SoulstructBaseFieldEditor, row_index: int, main_bindings: dict = None):
            super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)
            self.linked_text = ''

        def update_entry(self, entry_id: int, entry_text: str):
            """If 'linked_text' is an empty string, then text was expected, but not found (entry highlighted)."""
            self.entry_id = entry_id
            text_links = self.master.linker.param_entry_text_link(self.entry_id)
            self.linked_text = (f'    {{{text_links[0].name}}}' if text_links[0].name else '') if text_links else None
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
            self.text_label.var.set(self._entry_text + (self.linked_text if self.linked_text is not None else ''))

        def build_entry_context_menu(self, text_links=()):
            # TODO: 'View uses': search things that link to this type of param for this ID.
            super().build_entry_context_menu()
            text_links = self.master.linker.param_entry_text_link(self.entry_id)
            if text_links:
                self.context_menu.add_separator()
                for text_link in text_links:
                    text_link.add_to_context_menu(self.context_menu, foreground=self.STYLE_DEFAULTS['text_fg'])

    def __init__(self, lighting: DarkSoulsLightingParameters, linker, master=None, toplevel=False):
        self.Lighting = lighting
        self.map_area_choice = None
        self.slot_choice_label = None
        self.slot_choice = None
        super().__init__(linker, master=master, toplevel=toplevel, window_title="Soulstruct Lighting Editor")
        self._on_map_area_choice()  # Sets slot option correctly.

    def build(self):
        with self.set_master(sticky='nsew', row_weights=[0, 1], column_weights=[1], auto_rows=0):

            with self.set_master(pady=10, sticky='w', row_weights=[1], column_weights=[1], auto_columns=0):
                map_display_names = [f'{k} ({v})' for k, v in DRAW_PARAM_MAPS.items()]
                self.map_area_choice = self.Combobox(
                    values=map_display_names, on_select_function=self._on_map_area_choice, width=40, padx=10,
                    label='Map Area:', label_font_size=12, label_position='left', font=('Segoe UI', 12)).var
                self.slot_choice_label = self.Label(text='Slot:', font_size=12, padx=(30, 0))
                self.slot_choice = self.Combobox(
                    values=('0', '1'), font=('Segoe UI', 12), on_select_function=self._on_slot_choice, width=5, padx=10)

            super().build()

    def _on_map_area_choice(self, _=None):
        new_map_area = self.map_area_choice.get().split(' (')[0]
        param_tables = getattr(self.Lighting, new_map_area)['AmbientLight']  # picking a random category to check slots
        if param_tables[1] is None:
            self.slot_choice.config(values=['0'])
            if self.slot_choice.var.get() == '1':
                self._flash_red_bg(self.slot_choice_label)
            self.slot_choice.var.set('0')
        else:
            self.slot_choice.config(values=['0', '1'])
        self.select_entry_row_index(None)
        self.refresh_entries(reset_field_display=True)

    def _on_slot_choice(self, _=None):
        self.select_entry_row_index(None)
        self.refresh_entries(reset_field_display=True)

    def _get_display_categories(self):
        return self.Lighting.param_names

    def get_category_dict(self, category=None) -> Union[ParamTable, dict]:
        if category is None:
            category = self.active_category
            if category is None:
                return {}
        map_area_choice = self.map_area_choice.get().split(' (')[0]
        slot_choice = int(self.slot_choice.var.get())
        return self.Lighting[map_area_choice][category][slot_choice]

    def _get_category_name_range(self, category=None, first_index=None, last_index=None) -> list:
        if category is None:
            category = self.active_category
            if category is None:
                return []
        return self.get_category_dict(category).get_range(
            start=self.first_display_index, count=self.ENTRY_RANGE_SIZE)

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get index of entry in category. Ignores current display range."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No param category selected.")
        if entry_id not in self.get_category_dict(category).entries:
            raise ValueError(f"Param ID {entry_id} does not appear in category {category}.")
        return sorted(self.get_category_dict(category).entries).index(entry_id)

    def get_entry_text(self, entry_id: int, category=None) -> str:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.get_category_dict(category)[entry_id].name

    def _set_entry_text(self, entry_id: int, text: str, category=None, update_row_index=None):
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        self.get_category_dict(category)[entry_id].name = text
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_id, text)

    def _change_entry_id(self, row_index, new_id, category=None):
        if category is None:
            category = self.active_category
        old_id = self.get_entry_id(row_index)
        if old_id == new_id:
            return False
        if new_id in self.get_category_dict(category).entries:
            self.dialog("Entry ID Clash", f"Entry ID {new_id} already exists in Params.{category}. You must change or "
                                          f"delete it first.")
            return False
        entry_data = self.get_category_dict(category).pop(old_id)
        self.get_category_dict(category)[new_id] = entry_data
        if category == self.active_category and self.EntryRow.SHOW_ENTRY_ID:
            self.entry_rows[row_index].update_entry(new_id, entry_data.name)
        return True

    def get_field_dict(self, entry_id: int, category=None) -> ParamEntry:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.get_category_dict(category)[entry_id]

    def get_field_info(self, field_dict, field_name=None, category=None):
        """This method should return the full field information dictionary if field_name is None."""
        if field_dict is None:
            return {}
        if category is None:
            category = self.active_category
        return self.get_category_dict(category).get_field_info(field_dict, field_name=field_name)

    def get_field_names(self, field_dict):
        return field_dict.field_names if field_dict else []

    def get_field_links(self, field_type, field_value, valid_null_values=None):
        if valid_null_values is None:
            valid_null_values = {0: 'Default/None', -1: 'Default/None'}
        return self.linker.soulstruct_link(field_type, field_value, valid_null_values=valid_null_values)
