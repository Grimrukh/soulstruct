from __future__ import annotations

from typing import TYPE_CHECKING

from soulstruct.project.editor import SoulstructBaseFieldEditor, NameSelectionBox

if TYPE_CHECKING:
    from soulstruct.params import DarkSoulsGameParameters, ParamEntry


class SoulstructParamsEditor(SoulstructBaseFieldEditor):
    DATA_NAME = "Params"
    TAB_NAME = "params"
    CATEGORY_BOX_WIDTH = 165
    ENTRY_BOX_WIDTH = 350
    ENTRY_RANGE_SIZE = 200
    FIELD_BOX_WIDTH = 500
    FIELD_ROW_COUNT = 173  # highest count (Params[SpecialEffects])

    class EntryRow(SoulstructBaseFieldEditor.EntryRow):
        ENTRY_ID_WIDTH = 10
        master: SoulstructParamsEditor

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
            self.context_menu.add_separator()
            self.context_menu.add_command(
                label="Find References in Params", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.find_all_param_references(self.master.active_category, self.entry_id))

    def __init__(self, params: DarkSoulsGameParameters, linker, master=None, toplevel=False):
        self.Params = params
        self.go_to_param_id_entry = None
        self.search_result = None
        super().__init__(linker, master=master, toplevel=toplevel, window_title="Soulstruct Params Editor")

    def build(self):
        with self.set_master(sticky='nsew', row_weights=[0, 1], column_weights=[1], auto_rows=0):

            with self.set_master(pady=10, sticky='w', row_weights=[1], column_weights=[1, 1], auto_columns=0):
                self.go_to_param_id_entry = self.Entry(
                    label="Go to Param ID:", label_position='left', integers_only=True, width=30, padx=10)
                self.go_to_param_id_entry.bind('<Return>', self.go_to_param_id)
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
            # Find closest.
            param_id = max(p_id for p_id in params if p_id < param_id)
            self.search_result.set(f"Found closest preceding entry: {param_id}")
            self.after(2000, lambda: self.search_result.set(""))
        self.select_entry_id(param_id, set_focus_to_text=False, edit_if_already_selected=False)

    def find_all_param_references(self, category, param_id):
        """Iterates over all ParamTables to find references to this param ID, and presents them in a floating list."""
        param_link = f"<Params:{category}>"
        linking_fields = []
        links = []

        # Find all (category, field) pairs that could possibly reference this category.
        for param_name in self.Params.param_names:
            param_table = self.Params[param_name]
            info = param_table.get_field_info()
            for field_name, field_info in info.items():
                if callable(field_info):
                    continue  # can't possibly call with every single entry
                _, _, field_type, _ = field_info
                if isinstance(field_type, str) and field_type == param_link:
                    linking_fields.append((param_name, field_name))

        for param_name, field_name in linking_fields:
            for entry_id, field_dict in self.Params[param_name].items():
                if field_dict[field_name] == param_id:
                    links.append(f"{param_name} : {entry_id} : {field_name}")

        name_box = NameSelectionBox(self.master, names=links, list_name=f"Param References to {category}[{param_id}]")
        selected_name = name_box.go()
        if selected_name is not None:
            param_name, entry_id, field_name = selected_name.split(" : ")
            self.select_category(param_name, auto_scroll=True)
            self.select_entry_id(int(entry_id), edit_if_already_selected=False)
            self.select_field_name(field_name)

    def _get_display_categories(self):
        return self.Params.param_names

    def get_category_data(self, category=None):
        if category is None:
            category = self.active_category
            if category is None:
                return {}
        return self.Params[category].entries

    def _get_category_name_range(self, category=None, first_index=None, last_index=None) -> list:
        if category is None:
            category = self.active_category
            if category is None:
                return []
        return self.Params[category].get_range(start=self.first_display_index, count=self.ENTRY_RANGE_SIZE)

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get index of entry in category. Ignores current display range."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No param category selected.")
        if entry_id not in self.Params[category].entries:
            raise ValueError(f"Param ID {entry_id} does not appear in category {category}.")
        return sorted(self.Params[category].entries).index(entry_id)

    def get_entry_text(self, entry_id: int, category=None) -> str:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.Params[category][entry_id].name

    def _set_entry_text(self, entry_id: int, text: str, category=None, update_row_index=None):
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        self.Params[category][entry_id].name = text
        if category == self.active_category and update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_id, text)

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        entry_data = self.Params[category].pop(entry_id)
        self.Params[category][new_id] = entry_data
        if category == self.active_category and update_row_index:
            self.entry_rows[update_row_index].update_entry(new_id, entry_data.name)
        return True

    def get_field_dict(self, entry_id: int, category=None) -> ParamEntry:
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("No params category selected.")
        return self.Params[category][entry_id]

    def get_field_info(self, field_dict, field_name=None, category=None):
        """This method should return the full field information dictionary if field_name is None."""
        if field_dict is None:
            return {}
        if category is None:
            category = self.active_category
        return self.Params[category].get_field_info(field_dict, field_name=field_name)

    def get_field_names(self, field_dict):
        return field_dict.field_names if field_dict else []

    def get_field_links(self, field_type, field_value, valid_null_values=None):
        if valid_null_values is None:
            valid_null_values = {0: 'Default/None', -1: 'Default/None'}
        return self.linker.soulstruct_link(field_type, field_value, valid_null_values=valid_null_values)
