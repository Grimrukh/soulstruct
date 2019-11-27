from __future__ import annotations

from ast import literal_eval
from enum import IntEnum
from typing import List, TYPE_CHECKING

from soulstruct.core import InvalidFieldValueError
from soulstruct.maps import MAP_ENTRY_TYPES, DARK_SOULS_MAP_IDS
from soulstruct.project.utilities import bind_events
from soulstruct.project.editor import SoulstructBaseFieldEditor, NameSelectionBox
from soulstruct.utilities import camel_case_to_spaces, Vector
from soulstruct.utilities.window import SoulstructSmartFrame

if TYPE_CHECKING:
    from soulstruct.maps import DarkSoulsMaps


# TODO: Models are handled automatically. Model entries are auto-generated from all used model names.
#  - Validation is done by checking the model files for that map (only need to inspect the names inside the BND).
#  - Validation/SIB path depends on game version.
#  - Right-click pop-out selection list is available for characters (and eventually, some objects).


class _MapEntryFrame(SoulstructSmartFrame):
    """Manages map entry selection/modification in editor."""


class SoulstructMapEditor(SoulstructBaseFieldEditor):
    CATEGORY_BOX_WIDTH = 300
    ENTRY_BOX_WIDTH = 300
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 100
    FIELD_BOX_WIDTH = 450
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_COUNT = 50  # TODO: highest count in Maps? Probably closer to 20-30
    FIELD_NAME_WIDTH = 20
    FIELD_VALUE_BOX_WIDTH = 200
    FIELD_VALUE_WIDTH = 60

    class FieldRow(SoulstructBaseFieldEditor.FieldRow):

        def __init__(self, editor: SoulstructMapEditor, row_index: int, main_bindings: dict = None):
            super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)

            bg_color = self._get_color()

            self.value_vector_frame = editor.Frame(
                self.value_box, bg=bg_color, width=editor.FIELD_VALUE_WIDTH, height=editor.FIELD_ROW_HEIGHT,
                no_grid=True)
            bind_events(self.value_vector_frame, main_bindings)
            self.value_vector_x = editor.Label(
                self.value_vector_frame, text='', bg=bg_color, width=editor.FIELD_VALUE_WIDTH // 6,
                column=0, anchor='w')
            self.value_vector_y = editor.Label(
                self.value_vector_frame, text='', bg=bg_color, width=editor.FIELD_VALUE_WIDTH // 6,
                column=1, anchor='w')
            self.value_vector_z = editor.Label(
                self.value_vector_frame, text='', bg=bg_color, width=editor.FIELD_VALUE_WIDTH // 6,
                column=2, anchor='w')

            for coord, label in zip('xyz', (self.value_vector_x, self.value_vector_y, self.value_vector_z)):
                vector_bindings = main_bindings.copy()
                vector_bindings.update({
                    '<Button-1>': lambda _, c=coord: editor.select_displayed_field_row(row_index, coord=c)})
                bind_events(label, vector_bindings)

            self.unhide()

        def update_field(self, entry, name, nickname, value, field_type, docstring="DOC-TODO"):
            """Update widgets with given field information."""
            self.field_name = name
            self.field_type = field_type
            self.field_docstring = docstring

            nickname = camel_case_to_spaces(nickname)
            if self.field_name_label.var.get() != nickname:
                self.field_name_label.var.set(nickname)

            if isinstance(self.field_type, str):
                # Link could be an internal map entry name (will be converted to index on pack) or a param/text ID.
                # Note that the *argument* 'field_type' is used below, not attribute self.field_type.
                field_links = self.master.get_field_links(self.field_type, value)
                if not self.field_type.startswith('<Maps'):
                    field_type = int  # otherwise, leave as link string for first condition below
            else:
                field_links = []

            # Type checking order: [link_string, Vector, float/int/str, bool, list, IntEnum]
            if isinstance(field_type, str):
                if field_type.startswith('<MapsList:'):
                    # TODO: better display?
                    self.value_label.var.set('(select to edit)')
                else:
                    # Name of another MSB entry.
                    self.value_label.var.set(value)
                self._activate_value_widget(self.value_label)

            elif field_type == Vector:
                # No chance of a link here. TODO: replace equals?
                self.value_vector_x.var.set(f'x: {value.x:.3g}')
                self.value_vector_y.var.set(f'y: {value.y:.3g}')
                self.value_vector_z.var.set(f'z: {value.z:.3g}')
                self._activate_value_widget(self.value_vector_frame)

            elif field_type in {float, int, str}:
                value_text = f'{value:.3f}' if field_type == float else str(value)
                if field_links:
                    if len(field_links) > 1:
                        value_text += '    {AMBIGUOUS}'
                    if field_links[0].name is None:
                        value_text += '    {MISSING}'
                    else:
                        value_text += f'    {{{field_links[0].name}}}'
                if self.value_label.var.get() != value_text:
                    self.value_label.var.set(value_text)
                self._activate_value_widget(self.value_label)

            elif field_type == bool:
                if value not in {0, 1}:
                    raise ValueError(f"Field with 'bool' type has non-boolean value: {value}")
                self.value_checkbutton.var.set(value)
                self.value_checkbutton.config(fg='#3F3' if value else '#F33', text='ON' if value else 'OFF')
                self._activate_value_widget(self.value_checkbutton)

            elif field_type == list:
                value_text = repr(value)
                self.value_label.var.set(value_text)
                self._activate_value_widget(self.value_label)

            elif issubclass(field_type, IntEnum):
                self.value_combobox['values'] = [camel_case_to_spaces(e.name) for e in field_type]
                try:
                    # noinspection PyUnresolvedReferences
                    enum_name = camel_case_to_spaces(field_type(value).name)
                except ValueError:
                    enum_name = f'Unknown: {value}'
                self.value_combobox.var.set(enum_name)
                self._activate_value_widget(self.value_combobox)

            if field_links and not any(link.name for link in field_links) and not self.link_missing:
                self.link_missing = True
                self._update_colors()
            elif (not field_links or any(link.name for link in field_links)) and self.link_missing:
                self.link_missing = False
                self._update_colors()

            self.build_field_context_menu(field_links)
            self.tool_tip.text = docstring

            self.unhide()

        def build_field_context_menu(self, field_links=()):
            """For linked fields, adds an option to select an entry name from the linked table."""
            self.context_menu.delete(0, 'end')
            if field_links:
                for field_link in field_links:
                    field_link.add_to_context_menu(self.context_menu, foreground=self.STYLE_DEFAULTS['text_fg'])
                self.context_menu.add_command(
                    label="Select linked entry name from list", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=self.open_map_name_selection_box)

        def open_map_name_selection_box(self):
            names = self.master.linker.get_map_entry_type_names(self.field_type)
            window = NameSelectionBox(self.master, names)
            selected_name = window.go()
            if selected_name is not None:
                try:
                    field_links = self.master.linker.soulstruct_link(self.field_type, selected_name)
                except IndexError:
                    raise IndexError(
                        "Link was broken after selecting entry from list. This should not happen; please try "
                        "restarting Soulstruct.")
                if not field_links[0].name:
                    selected_name += '   {MISSING}'
                    if not self.link_missing:
                        self.link_missing = True
                        self._update_colors()
                else:
                    if self.link_missing:
                        self.link_missing = False
                        self._update_colors()

                self.master.change_field_value(self.field_name, selected_name)
                self.value_label.var.set(selected_name)
                self.build_field_context_menu(field_links)

        @property
        def editable(self):
            return id(self.active_value_widget) in {id(self.value_label), id(self.value_vector_frame)}

        def confirm_edit(self, new_text, coord=None):
            if not self.editable:
                raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")

            if isinstance(self.field_type, str):
                new_value = str(new_text) if not self.field_type.startswith('<Maps') else new_text
                try:
                    field_link = self.master.linker.soulstruct_link(self.field_type, new_text)[0]
                except IndexError:
                    pass  # No link for this field.
                else:
                    if not field_link.name:
                        new_text += '  {MISSING}'
                        if not self.link_missing:
                            self.link_missing = True
                            self._update_colors()
                    else:
                        if not self.field_type.startswith('<Maps:'):  # not <MapsList:
                            new_text += f'  {{{field_link.name}}}'
                        if self.link_missing:
                            self.link_missing = False
                            self._update_colors()
                    self.value_label.var.set(new_text)
                    self.build_field_context_menu(field_link)
                    return new_value

            if coord is not None:
                # TODO: Not a fan of the equal sign.
                getattr(self, f'value_vector_{coord}').var.set(f'{coord}: {new_text}')
            else:
                self.value_label.var.set(new_text)

            if self.field_type in (float, Vector):
                return float(new_text)
            elif self.field_type == int:
                return int(new_text)
            elif self.field_type == str:
                return new_text
            elif self.field_type == list:
                try:
                    true_value = literal_eval(new_text)
                    if not isinstance(true_value, list):
                        raise ValueError()
                except (SyntaxError, ValueError):
                    raise ValueError("Field value must be a list of integers.")
                return true_value
            else:
                raise TypeError(f"Could not confirm new field value of type {self.field_type}.")

        def _update_colors(self):
            bg_color = self._get_color()
            for widget in (self.row_box, self.field_name_box, self.field_name_label, self.value_box, self.value_label,
                           self.value_vector_frame, self.value_vector_x, self.value_vector_y, self.value_vector_z,
                           self.value_checkbutton):
                widget['bg'] = bg_color

    class EntryRow(SoulstructBaseFieldEditor.EntryRow):
        """Entry rows for Maps have no ID, and also display their Entity ID field if they have a non-default value."""
        ENTRY_ID_WIDTH = 5

        def __init__(self, editor: SoulstructMapEditor, row_index: int, main_bindings: dict = None):
            super().__init__(editor=editor, row_index=row_index, main_bindings=main_bindings)

        def update_entry(self, entry_index: int, entry_text: str, entity_id: int = -1):
            self.entry_id = entry_index
            self._entry_text = entry_text
            self.text_label.var.set(entry_text + (f'   {{Entity ID: {entity_id}}}' if entity_id != -1 else ''))
            self.unhide()

        def build_entry_context_menu(self):
            self.context_menu.delete(0, 'end')
            self.context_menu.add_command(
                label="Edit in Floating Box (Shift + Click)", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.popout_entry_edit(self.row_index))
            self.context_menu.add_command(
                label="Duplicate Entry to Next Index", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.add_relative_entry(self.row_index, offset=1))
            self.context_menu.add_command(
                label="Delete Entry", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.delete_entry(self.row_index))

    entry_rows: List[SoulstructMapEditor.EntryRow]
    field_rows: List[SoulstructMapEditor.FieldRow]

    def __init__(self, maps: DarkSoulsMaps, linker, master=None, toplevel=False):
        self.Maps = maps
        self.e_coord = None
        self.map_choice = None
        self.entry_type_rows = {}
        self.active_entry_type_index = None
        super().__init__(linker, master=master, toplevel=toplevel, window_title="Soulstruct Map Data Editor")

    def build(self):
        with self.set_master(auto_rows=0):
            map_display_names = [camel_case_to_spaces(m) for m in DARK_SOULS_MAP_IDS]
            self.map_choice = self.Combobox(
                values=map_display_names, font=20,
                on_select_function=lambda _: self.refresh_entries(reset_field_display=True),
                padx=10, pady=10).var

            with self.set_master(auto_columns=0):
                self.build_category_canvas()
                with self.set_master():
                    self.build_previous_range_button(row=0, column=0)
                    self.build_hidden_fields_checkbutton(row=0, column=1)
                    with self.set_master(row=1, column=0):
                        self.build_entry_frame()
                    with self.set_master(row=1, column=1):
                        self.build_field_frame()
                    self.build_next_range_button(row=2, column=0)

    def _add_entry(self, entry_index: int, text: str, field_dict=None):
        """Requires additional field_dict argument."""
        entry_list = self.get_category_dict()
        if not 0 <= entry_index <= len(entry_list):
            self.dialog("Entry Index Error", message=f"Entry index must be between zero and the current list length.")
            return False

        self._cancel_entry_text_edit()
        entry_list.insert(entry_index, field_dict)  # insert entry into desired position in list
        self._set_entry_text(entry_index, text)
        self.select_entry_id(entry_index, set_focus_to_text=True, edit_if_already_selected=False)
        # TODO: ActionHistory stuff?
        return True

    def add_relative_entry(self, entry_index, offset=1, text=None):
        """Uses entry index instead of dictionary ID."""
        if text is None:
            text = self.get_entry_text(entry_index)  # Copies name of origin entry by default.
        self._add_entry(entry_index + offset, text)

    def select_displayed_field_row(self, row_index, set_focus_to_value=True, edit_if_already_selected=True, coord=None):
        old_row_index = self.selected_field_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected and self.field_rows[row_index].editable:
                    return self._start_field_value_edit(row_index, coord=coord)
                return
        else:
            self._cancel_field_value_edit()

        self.selected_field_row_index = row_index

        if old_row_index is not None:
            self.field_rows[old_row_index].active = False
        if row_index is not None:
            self.field_rows[row_index].active = True
            if set_focus_to_value:
                self.field_rows[row_index].active_value_widget.focus_set()

    # TODO: how does field_press react if a coord is being edited? Should go to next coord, probably.

    def _get_field_edit_widget(self, row_index):
        field_row = self.field_rows[row_index]
        if not field_row.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")
        field_type = field_row.field_type
        field_value = self.get_field_dict(self.get_entry_id(self.selected_entry_row_index))[field_row.field_name]
        if field_type in {int, float, str, list} or isinstance(field_type, str):
            return self.Entry(
                field_row.value_box,
                initial_text=str(field_value),
                numbers_only=field_type == float,
                integers_only=field_type == int,
                sticky='ew', width=5)
        elif field_type == Vector:
            if self.e_coord is None:
                return None  # Exact coordinate not clicked.
            return self.Entry(
                field_row.value_vector_frame, initial_text=getattr(field_value, self.e_coord),
                numbers_only=True, sticky='ew', width=5, column='xyz'.index(self.e_coord))
        raise TypeError(f"Could not determine editing box from type {field_type}.")

    def _start_field_value_edit(self, row_index, coord=None):
        if self.e_field_value_edit and self.e_coord and coord and coord != self.e_coord:
            # Finish up previous coord edit.
            self._confirm_field_value_edit(row_index)
        self.e_coord = coord
        super()._start_field_value_edit(row_index)

    def _cancel_field_value_edit(self):
        if self.e_field_value_edit:
            self.e_field_value_edit.destroy()
            self.e_field_value_edit = None
            self.e_coord = None

    def _confirm_field_value_edit(self, index):
        if self.e_field_value_edit:
            try:
                true_value = self.field_rows[index].confirm_edit(
                    new_text=self.e_field_value_edit.var.get(), coord=self.e_coord)
            except ValueError as e:
                # Entry input restrictions are supposed to prevent this.
                print(str(e))
                self.bell()
                return
            self.change_field_value(self.field_rows[index].field_name, true_value)
            self._cancel_field_value_edit()

    def change_field_value(self, field_name: str, new_value):
        field_dict = self.get_selected_field_dict()
        old_value = field_dict[field_name]
        if self.e_coord:
            old_value = getattr(old_value, self.e_coord)
        if old_value == new_value:
            return False  # Nothing to change.
        try:
            if self.e_coord:
                setattr(field_dict[field_name], self.e_coord, new_value)
            else:
                field_dict[field_name] = new_value
        except InvalidFieldValueError as e:
            self.bell()
            self.dialog(title="Value Error", message=str(e), button_kwargs='OK')
            return False
        return True

    def _get_display_categories(self):
        """ALl combinations of MSB entry list names and their subtypes."""
        categories = []
        for entry_list_name, entry_type_names in MAP_ENTRY_TYPES.items():
            for name in entry_type_names:
                categories.append(f'{entry_list_name}:{name}')
        return categories

    def get_selected_msb(self):
        return self.Maps[self.map_choice.get().replace(' ', '')]

    def get_category_dict(self, category=None):
        """Gets entry data from map choice, entry list choice, and entry type choice (active category).

        For Maps, this actually returns a *list*, not a dict. Entry IDs are equivalent to entry indexes in this list, so
        all parent methods still function as expected.
        """
        if category is None:
            category = self.active_category
            if category is None:
                return []
        map_choice = self.map_choice.get().replace(' ', '')
        entry_list, entry_type = category.split(':')
        return self.Maps[map_choice][entry_list].get_entries(entry_type)

    def _get_category_name_range(self, category=None, first_index=None, last_index=None):
        """Returns an zip() generator for parent method."""
        entry_list = self.get_category_dict(category)
        return zip(range(first_index, last_index), entry_list[first_index:last_index])

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Entry index and entry ID are equivalent in Maps.

        Note that .get_entry_id() is still necessary to get the true entry index from the displayed row index.
        """
        return entry_id

    def get_entry_text(self, entry_index: int, category=None) -> str:
        entry_list = self.get_category_dict(category)
        return entry_list[entry_index].name

    def _set_entry_text(self, entry_index: int, text: str, category=None):
        entry_list = self.get_category_dict(category)
        entry_list[entry_index].name = text

    def get_field_dict(self, entry_index: int, category=None):
        """Uses entry index instad of entry ID."""
        return self.get_category_dict(category)[entry_index]

    def get_field_info(self, field_dict, field_name=None):
        if field_name is not None:
            return field_dict.FIELD_INFO[field_name]
        return field_dict.FIELD_INFO

    def get_field_links(self, field_type, field_value, valid_null_values=None) -> list:
        if valid_null_values is None:
            if field_type == '<Text:PlaceNames>':
                valid_null_values = {-1: 'Default Map Name + Force Banner'}
            else:
                valid_null_values = {0: 'Default/None', -1: 'Default/None'}
        return self.linker.soulstruct_link(field_type, field_value, valid_null_values=valid_null_values)
