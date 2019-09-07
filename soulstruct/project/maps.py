from __future__ import annotations

from ast import literal_eval
from enum import IntEnum
from typing import List, TYPE_CHECKING

from soulstruct.core import InvalidFieldValueError
from soulstruct.maps import MAP_ENTRY_TYPES, DARK_SOULS_MAP_IDS
from soulstruct.project.actions import ActionHistory
from soulstruct.utilities import camel_case_to_spaces, Vector
from soulstruct.utilities.window import SoulstructSmartFrame, ToolTip

if TYPE_CHECKING:
    from soulstruct.maps import DarkSoulsMaps, MSB
    from soulstruct.project.core import SoulstructProject


def bind_events(widget, bindings: dict):
    for event, func in bindings.items():
        widget.bind(event, func)


# TODO: Models are handled automatically. Model entries are auto-generated from all model names.
#  - Validation is done by checking the model files for that map (only need to inspect the names inside the BND).
#  - Validation/SIB path depends on game version.
#  - Right-click pop-out selection list is available for characters (and eventually, some objects).


class _MapFieldRow(object):
    """Container for components of a row in the _MapFieldFrame.

    These are only created once, and their contents are refreshed when needed. Unlike entries, field value widgets may
    be Labels (which turn to Entries for editing), Checkbuttons, or Comboboxes. Each of these widgets is created for
    each row, so they can be displayed (with `grid()`) when needed, rather than dynamically created and destroyed
    every time a new entry/category is selected.
    """
    ROW_HEIGHT = 30
    NAME_WIDTH = 20
    VALUE_WIDTH = 60

    def __init__(self, master: _MapFieldFrame, row_index: int, change_value_func, main_bindings: dict = None):
        self.master = master
        self.linker = master.linker
        self.STYLE_DEFAULTS = master.STYLE_DEFAULTS
        self.map_entry = None

        self.index = row_index
        self._active = False
        self.field_name = ''
        self.field_type = None
        self.field_docstring = ""
        self.link_missing = False

        bg_color = self._get_color()

        self.row_box = master.Frame(
            width=master.FIELD_BOX_WIDTH, height=self.ROW_HEIGHT, bg=bg_color,
            row=row_index, columnspan=2, sticky='nsew')
        bind_events(self.row_box, main_bindings)

        self.field_name_box = master.Frame(row=row_index, column=0, bg=bg_color, sticky='w')
        bind_events(self.field_name_box, main_bindings)

        self.field_name_label = master.Label(
            self.field_name_box, text='', fg=master.FIELD_NAME_FG, width=self.NAME_WIDTH, bg=bg_color, anchor='w')
        bind_events(self.field_name_label, main_bindings)

        self.value_box = master.Frame(width=400, row=row_index, column=1, bg=bg_color, sticky='ew')
        bind_events(self.value_box, main_bindings)

        # VALUE WIDGETS

        self.value_label = master.Label(self.value_box, text='', bg=bg_color, width=self.VALUE_WIDTH, anchor='w', row=0)
        bind_events(self.value_label, main_bindings)

        self.value_vector_frame = master.Frame(
            self.value_box, bg=bg_color, width=self.VALUE_WIDTH, height=self.ROW_HEIGHT, no_grid=True)
        self.value_vector_x = master.Label(
            self.value_vector_frame, text='', bg=bg_color, width=self.VALUE_WIDTH // 8, column=0, anchor='w')
        self.value_vector_y = master.Label(
            self.value_vector_frame, text='', bg=bg_color, width=self.VALUE_WIDTH // 8, column=1, anchor='w')
        self.value_vector_z = master.Label(
            self.value_vector_frame, text='', bg=bg_color, width=self.VALUE_WIDTH // 8, column=2, anchor='w')
        for coord, label in zip('xyz', (self.value_vector_x, self.value_vector_y, self.value_vector_z)):
            vector_bindings = main_bindings.copy()
            vector_bindings.update({'<Button-1>': lambda _, c=coord: master.select_field(row_index, coord=c)})
            bind_events(label, vector_bindings)

        self.value_checkbutton = master.Checkbutton(
            self.value_box, label=None, bg=bg_color, no_grid=True,
            command=lambda: self._checkbutton_toggle(change_value_func))
        # Main focus bindings are not bound to Checkbutton.

        self.value_combobox = master.Combobox(
            self.value_box, values=None, width=self.VALUE_WIDTH, no_grid=True,
            on_select_function=lambda _: change_value_func(
                self.index, getattr(self.field_type, self.value_combobox.var.get().replace(' ', '')).value))
        # Main focus bindings are not bound to Combobox.

        self.context_menu = master.Menu(self.row_box)
        self.tool_tip = ToolTip(self.row_box, self.field_name_box, self.field_name_label, text=None)

        self.active_value_widget = self.value_label
        self.clear()  # TODO: still getting white box before I click or scroll

    def _activate_value_widget(self, widget):
        if id(self.active_value_widget) != id(widget):
            self.active_value_widget.grid_remove()
        self.active_value_widget = widget

    def _checkbutton_toggle(self, change_value_func):
        new_value = self.value_checkbutton.var.get()
        if not change_value_func(self.index, new_value):
            # Checkbutton toggle is invalid.
            self.value_checkbutton.var.set(not new_value)

    def build_field(self, entry, name, nickname, value, field_type, docstring="DOC-TODO"):
        """Update widgets with given field information."""
        self.map_entry = entry
        self.field_name = name
        self.field_type = field_type
        self.field_docstring = docstring

        field_link = None

        self.field_name_label.var.set(nickname)

        if isinstance(self.field_type, str):
            # Link could be an internal map entry name (will be converted to index on pack) or a param/text ID.
            if self.field_type == '<Text:PlaceNames>':
                special_values = {-1: 'Default Map Name (With Banner)'}
            else:
                special_values = {0: 'Default', -1: 'Default'}
            try:
                field_link = self.linker.soulstruct_link(self.field_type, value, special_values=special_values)[0]
            except IndexError:
                # print("No field link for type:", self.field_type)
                field_link = None
            if not self.field_type.startswith('<Maps'):
                field_type = int

        if isinstance(field_type, str):
            if field_type.startswith('<MapsList:'):
                self.value_label.var.set('(select to edit)')
            else:
                # Name of another MSB entry.
                self.value_label.var.set(value)
            self._activate_value_widget(self.value_label)
        elif field_type == Vector:
            # No chance of a link here.
            self.value_vector_x.var.set(f'x = {value.x:.3g}')
            self.value_vector_y.var.set(f'y = {value.y:.3g}')
            self.value_vector_z.var.set(f'z = {value.z:.3g}')
            self._activate_value_widget(self.value_vector_frame)
        elif field_type in {float, int, str}:
            value_text = f'{value:.3g}' if field_type == float else str(value)
            if field_link:
                if field_link.name is None:
                    value_text += f'   [MISSING]'
                else:
                    value_text += f'   [{field_link.name}]'
            self.value_label.var.set(value_text)
            self._activate_value_widget(self.value_label)
        elif field_type == bool:
            if value not in {0, 1}:
                raise ValueError(f"Field with 'bool' type has non-boolean value: {value}")
            self.value_checkbutton.var.set(value)
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
                enum_name = f'<Unknown: {value}>'  # TODO: ensure this is read back and saved properly
            self.value_combobox.var.set(enum_name)
            self._activate_value_widget(self.value_combobox)
        else:
            raise TypeError(f"Invalid field type: {field_type}")

        if self.field_name_label.var.get() != nickname:
            self.field_name_label.var.set(nickname)

        if field_link and not field_link.name and not self.link_missing:
            self.link_missing = True
            self._update_colors()
        elif (not field_link or field_link.name) and self.link_missing:
            self.link_missing = False
            self._update_colors()

        self.build_field_context_menu(field_link)
        self.tool_tip.text = docstring

        self.row_box.grid()
        self.field_name_box.grid()
        self.field_name_label.grid()
        self.value_box.grid()
        self.active_value_widget.grid()

    def build_field_context_menu(self, field_link):
        self.context_menu.delete(0, 'end')
        if field_link:
            if field_link.name != 'None':
                self.context_menu.add_command(
                    label=field_link.menu_text, foreground=self.STYLE_DEFAULTS['text_fg'], command=field_link)
                # TODO: Should not appear for params.
                self.context_menu.add_command(
                    label="Select linked entry name from list", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=self.open_map_name_selection_box)

    def open_map_name_selection_box(self):
        window = _MapNameSelectionBox(self.master, self.field_type)
        selected_name = window.go()
        if selected_name is not None:
            try:
                field_link = self.linker.soulstruct_link(self.field_type, selected_name)[0]
            except IndexError:
                raise IndexError("Link was broken after selecting entry from list. This should not happen; please try "
                                 "restarting Soulstruct.")
            if not field_link.name:
                selected_name += f' [MISSING]'
                if not self.link_missing:
                    self.link_missing = True
                    self._update_colors()
            else:
                if self.link_missing:
                    self.link_missing = False
                    self._update_colors()

            self.value_label.var.set(selected_name)
            self.build_field_context_menu(field_link)

    def clear(self):
        """Called when this row has no field to display."""
        self.row_box.grid_remove()
        self.field_name_box.grid_remove()
        self.field_name_label.grid_remove()
        self.value_box.grid_remove()
        self.active_value_widget.grid_remove()

    @property
    def editable(self):
        return id(self.active_value_widget) in {id(self.value_label), id(self.value_vector_frame)}

    def confirm_edit(self, new_text, coord=None):
        if not self.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")

        if isinstance(self.field_type, str):
            new_value = str(new_text) if not self.field_type.startswith('<Maps') else new_text
            try:
                field_link = self.linker.soulstruct_link(self.field_type, new_text)[0]
            except IndexError:
                pass  # No link for this field.
            else:
                if not field_link.name:
                    new_text += f' [MISSING]'
                    if not self.link_missing:
                        self.link_missing = True
                        self._update_colors()
                else:
                    if not self.field_type.startswith('<Maps:'):  # not <MapsList:
                        new_text += f' [{field_link.name}]'
                    if self.link_missing:
                        self.link_missing = False
                        self._update_colors()
                self.value_label.var.set(new_text)
                self.build_field_context_menu(field_link)
                return new_value

        if coord is not None:
            getattr(self, f'value_vector_{coord}').var.set(f'{coord} = {new_text}')
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

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value: bool):
        if not self._active and value:
            self._active = True
        elif self._active and not value:
            self._active = False
        else:
            return  # No change to active state.

        # All widget backgrounds need updating (except Combobox).
        self._update_colors()

    def _update_colors(self):
        bg_color = self._get_color()
        for widget in (self.row_box, self.field_name_box, self.field_name_label, self.value_box, self.value_label,
                       self.value_vector_frame, self.value_vector_x, self.value_vector_y, self.value_vector_z,
                       self.value_checkbutton):
            widget['bg'] = bg_color

    def _get_color(self):
        """Inspects field name/data and returns a tuple of 'bg' color values."""
        base_bg = 222
        if self.link_missing:
            base_bg += 100
        if self._active:
            base_bg += 123
        if self.index % 2:
            base_bg += 111
        return f'#{base_bg}'


class _MapEntryRow(object):
    """Container for components of a row in the _MapEntryFrame.

    These are only created once, and their contents are refreshed when needed.
    """

    def __init__(self, master: _MapEntryFrame, row_index: int, main_bindings: dict = None):
        self.master = master
        self.linker = master.linker
        self.STYLE_DEFAULTS = master.STYLE_DEFAULTS

        self.entry_name = None

        self.index = row_index
        self._active = False
        self.any_text_missing = False

        bg_color = self._get_color()

        self.row_box = master.Frame(width=master.ENTRY_BOX_WIDTH, height=25, bg=bg_color, row=row_index, sticky='nsew')
        bind_events(self.row_box, main_bindings)
        self.name_box = master.Frame(bg=bg_color, row=row_index)
        bind_events(self.name_box, main_bindings)
        self.name_label = master.Label(self.name_box, text='', bg=bg_color, anchor='w', width=60, padx=3)
        bind_events(self.name_label, main_bindings)

        self.context_menu = master.Menu(self.row_box)
        self.tool_tip = ToolTip(self.row_box, self.name_box, self.name_label, text=None, wraplength=350)

    def build_entry(self, entry_name: str, entity_id: int = -1):
        self.entry_name = entry_name
        self.name_label.var.set(entry_name + (f'   [{entity_id}]' if entity_id != -1 else ''))

        self.row_box.grid()
        self.name_box.grid()
        self.name_label.grid()

    def clear(self):
        """Called when this row has no entry to display."""
        self.row_box.grid_remove()
        self.name_box.grid_remove()
        self.name_label.grid_remove()

    def build_entry_context_menu(self):
        self.context_menu.delete(0, 'end')
        # TODO: Nothing to do here yet.

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value: bool):
        if not self._active and value:
            self._active = True
        elif self._active and not value:
            self._active = False
        else:
            return  # No change to active state.

        # All widget backgrounds need updating (except Combobox).
        self._update_colors()

    def _update_colors(self):
        bg_color = self._get_color()
        for widget in (self.row_box, self.name_box, self.name_label):
            widget['bg'] = bg_color

    def _get_color(self):
        """Inspects entry name/data and returns a tuple of 'bg' color values."""
        base_bg = 222
        if self.entry_name is not None:
            if not self.entry_name:
                base_bg += 200
            elif not self.entry_name.strip():
                base_bg += 110
        if self._active:
            base_bg += 123
        if self.index % 2:
            base_bg += 111
        return f'#{base_bg}'


class _MapFieldFrame(SoulstructSmartFrame):
    FIELD_CANVAS_BG = '#1d1d1d'
    FIELD_BOX_WIDTH = 700
    FIELD_BOX_HEIGHT = 500
    FIELD_ROW_COUNT = 173  # highest count (Special Effects)
    FIELD_NAME_FG = '#DDE'

    def __init__(self, maps, linker, master=None):
        super().__init__(master=master, toplevel=False)
        self.Maps = maps  # type: DarkSoulsMaps
        self.linker = linker

        self.map_entry = None
        self.e_field_value_edit = None
        self.e_coord = None
        self.field_index_selected = None
        self.displayed_field_count = 0
        self.field_rows = []  # type: List[_MapFieldRow]

        self.field_canvas = self.Canvas(vertical_scrollbar=True, width=self.FIELD_BOX_WIDTH,
                                        height=self.FIELD_BOX_HEIGHT, yscrollincrement=25, highlightthickness=1,
                                        padx=40, pady=40, bg=self.FIELD_CANVAS_BG)
        self.f_field_table = self.Frame(frame=self.field_canvas, width=self.FIELD_BOX_WIDTH,
                                        sticky='ew')
        self.field_canvas.create_window(
            self.FIELD_BOX_WIDTH / 2, self.FIELD_BOX_HEIGHT / 2, window=self.f_field_table, anchor='nw')
        self.f_field_table.bind(
            "<Configure>", lambda e, c=self.field_canvas: self.reset_canvas_scroll_region(c))

        with self.set_master(self.f_field_table):
            for row in range(self.FIELD_ROW_COUNT):
                self.field_rows.append(_MapFieldRow(
                    self, row_index=row, change_value_func=self._change_field_value,
                    main_bindings={
                        '<Button-1>': lambda _, i=row: self.select_field(i),
                        '<Button-3>': lambda e, i=row: self._right_click_field(e, i),
                        '<Up>': self.field_press_up,
                        '<Down>': self.field_press_down,
                    }))

    def _right_click_field(self, event, field_index):
        self.select_field(field_index, edit_if_already_selected=False)
        self.field_rows[field_index].context_menu.tk_popup(event.x_root, event.y_root)

    def refresh_fields(self, map_entry=None, reset_display=False):
        """Refresh all field name/value labels."""
        self._cancel_field_value_edit()

        self.map_entry = map_entry
        field_info = self.map_entry.FIELD_INFO if self.map_entry is not None else {}

        row = 0
        for field_name, (field_nickname, field_type, field_doc) in field_info.items():

            self.field_rows[row].build_field(
                entry=self.map_entry,
                name=field_name,
                nickname=field_nickname,
                value=getattr(self.map_entry, field_name),
                field_type=field_type,
                docstring=field_doc,
            )
            row += 1

        self.displayed_field_count = row

        for remaining_row in range(row, self.FIELD_ROW_COUNT):
            self.field_rows[remaining_row].clear()

        self.f_field_table.grid_columnconfigure(1, weight=1)

        if reset_display:
            self.select_field(0, edit_if_already_selected=False)
            self.update_idletasks()
            self.field_canvas.yview_moveto(0)

    def select_field(self, index, set_focus_to_value=True, edit_if_already_selected=True, coord=None):
        # TODO: should this start editing immediately (on left click)?
        # TODO: tab while editing moves to next field. Shift+Tab moves back. Up and down arrows also work.
        old_index = self.field_index_selected

        if old_index is not None and index == old_index:
            if edit_if_already_selected and self.field_rows[index].editable:
                return self._start_field_value_edit(index, coord=coord)
            return
        else:
            self._cancel_field_value_edit()

        self.field_index_selected = index

        if old_index is not None:
            self.field_rows[old_index].active = False
        self.field_rows[index].active = True
        if set_focus_to_value:
            self.field_rows[index].active_value_widget.focus_set()

    def field_press_up(self, _=None):
        if self.field_index_selected is not None:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.field_index_selected)
            self.shift_selected_field(-1)
            if edit_new and self.field_rows[self.field_index_selected].editable:
                self._start_field_value_edit(self.field_index_selected)
            if self.field_canvas.yview()[1] != 1.0 or self.field_index_selected < self.displayed_field_count - 5:
                self.field_canvas.yview_scroll(-1, 'units')

    def field_press_down(self, _=None):
        if self.field_index_selected is not None:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.field_index_selected)
            self.shift_selected_field(+1)
            if edit_new and self.field_rows[self.field_index_selected].editable:
                self._start_field_value_edit(self.field_index_selected)
            if self.field_canvas.yview()[0] != 0.0 or self.field_index_selected > 5:
                self.field_canvas.yview_scroll(1, 'units')

    def shift_selected_field(self, relative_index):
        if (self.field_index_selected is None
                or not 0 <= self.field_index_selected + relative_index < self.displayed_field_count):
            return
        self.select_field(self.field_index_selected + relative_index)

    def _start_field_value_edit(self, index, coord=None):
        if self.e_field_value_edit and self.e_coord and coord and coord != self.e_coord:
            # Change to editing a different coordinate.
            self._confirm_field_value_edit(index)
        if not self.e_field_value_edit:
            field_row = self.field_rows[index]
            if not field_row.editable:
                raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")
            field_name = field_row.field_name
            if field_row.field_type == float:
                self.e_field_value_edit = self.Entry(
                    field_row.value_box, initial_text=getattr(self.map_entry, field_name),
                    numbers_only=True, sticky='ew', width=5)
            elif field_row.field_type == int or isinstance(field_row.field_type, str):
                # TODO: Pop-out list editor for MapsList.
                self.e_field_value_edit = self.Entry(
                    field_row.value_box, initial_text=getattr(self.map_entry, field_name),
                    integers_only=field_row.field_type == int, sticky='ew', width=5)
            elif field_row.field_type in (str, list):
                self.e_field_value_edit = self.Entry(
                    field_row.value_box, initial_text=str(getattr(self.map_entry, field_name)),
                    sticky='ew', width=5)
            elif field_row.field_type == Vector:
                if coord is None:
                    return  # Exact coordinate not clicked.
                self.e_field_value_edit = self.Entry(
                    field_row.value_vector_frame, initial_text=getattr(getattr(self.map_entry, field_name), coord),
                    numbers_only=True, sticky='ew', width=5, column='xyz'.index(coord))
                self.e_coord = coord
            else:
                raise TypeError(f"Could not determine editing box from type {field_row.field_type}.")
            self.e_field_value_edit.bind('<Return>', lambda e, i=index: self._confirm_field_value_edit(i))
            self.e_field_value_edit.bind('<Up>', self.field_press_up)
            self.e_field_value_edit.bind('<Down>', self.field_press_down)
            self.e_field_value_edit.bind('<FocusOut>', lambda e, i=index: self._confirm_field_value_edit(i))
            self.e_field_value_edit.bind('<Escape>', lambda e: self._cancel_field_value_edit())
            self.e_field_value_edit.focus_set()
            self.e_field_value_edit.select_range(0, 'end')

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
            self._change_field_value(index, true_value)
            self._cancel_field_value_edit()

    def _change_field_value(self, index, new_value):
        """New value should have already been converted to its appropriate type."""
        field_name = self.field_rows[index].field_name
        old_value = getattr(self.map_entry, field_name)
        if self.e_coord:
            old_value = getattr(old_value, self.e_coord)
        if old_value == new_value:
            return False  # Nothing to change.
        try:
            if self.e_coord:
                setattr(getattr(self.map_entry, field_name), self.e_coord, new_value)
            else:
                setattr(self.map_entry, field_name, new_value)
        except InvalidFieldValueError as e:
            self.bell()
            self.dialog(title="Value Error", message=str(e), button_kwargs='OK')
            return False
        return True


class _MapEntryFrame(SoulstructSmartFrame):
    """Manages map entry selection/modification in editor."""
    ENTRY_CANVAS_BG = '#1d1d1d'
    ENTRY_BOX_WIDTH = 300
    ENTRY_RANGE_SIZE = 100

    field_display: _MapFieldFrame

    def __init__(self, maps, linker, master=None):
        super().__init__(master=master, toplevel=False)
        self.Maps = maps
        self.linker = linker

        self.msb_entries = None
        self.entry_rows = []  # type: List[_MapEntryRow]
        self.entry_index_selected = None
        self.first_display_index = 0
        self.displayed_entry_count = 0
        self.e_entry_name_edit = None

        with self.set_master(auto_rows=0):
            with self.set_master(auto_columns=0):
                self.previous_range_button = self.Button(
                    text=f"Previous {self.ENTRY_RANGE_SIZE}", bg='#235', width=30,
                    command=self._go_to_previous_entry_range, padx=10, pady=20, row=0, sticky='w')

                # TODO
                # self.b_create_new_map = self.Button(
                #     text="Create New Text ID", bg='#235', width=30, command=self.create_new_map_id,
                #     padx=10, pady=20)

                # TODO: restore
                # self.find_map_id_entry = self.Entry(
                #     label="Find ID:", label_position='left', width=14, padx=10)
                # self.find_map_id_entry.bind('<Return>', lambda e: self.find_map_id())
                # with self.set_master(auto_rows=0):
                #     self.find_text_string_entry = self.Entry(
                #         label="Find Text:", label_position='left', width=14, padx=10)
                #     self.find_text_string_entry.bind('<Return>', lambda e: self.find_text_string())
                #     self.replace_text_string_entry = self.Entry(
                #         label="Replace With:", label_position='left', width=14, padx=10)
                #     self.replace_text_string_entry.bind('<Return>', lambda e: self.find_text_string(replace=True))

            with self.set_master(auto_columns=0):
                with self.set_master():
                    self.entry_canvas = self.Canvas(  # TODO: what should height actually be?
                        vertical_scrollbar=True, width=self.ENTRY_BOX_WIDTH, height=500, highlightthickness=1,
                        yscrollincrement=25, padx=40, pady=40, bg=self.ENTRY_CANVAS_BG)
                    self.f_entry_table = self.Frame(frame=self.entry_canvas, width=self.ENTRY_BOX_WIDTH, sticky='ew')
                    self.entry_canvas.create_window(self.ENTRY_BOX_WIDTH / 2, 250, window=self.f_entry_table,
                                                    anchor='nw')
                    self.f_entry_table.bind(
                        "<Configure>", lambda e, c=self.entry_canvas: self.reset_canvas_scroll_region(c))

                with self.set_master():
                    self.field_display = self.SmartFrame(
                        smart_frame_class=_MapFieldFrame, maps=self.Maps, linker=self.linker)

            with self.set_master(self.f_entry_table):
                for row in range(self.ENTRY_RANGE_SIZE):
                    self.entry_rows.append(_MapEntryRow(
                        self, row_index=row, main_bindings={
                            '<Button-1>': lambda _, i=row: self.select_entry(i),
                            '<Button-3>': lambda e, i=row: self._right_click_map_entry(e, i),
                            '<Up>': self._entry_press_up,
                            '<Down>': self._entry_press_down,
                            '<Prior>': lambda e: self._go_to_previous_entry_range(),
                            '<Next>': lambda e: self._go_to_next_entry_range(),
                        }))

            with self.set_master(auto_columns=0):
                self.next_range_button = self.Button(
                    text=f"Next {self.ENTRY_RANGE_SIZE}", bg='#235', width=30, command=self._go_to_next_entry_range,
                    padx=10, pady=20)

    def refresh_field_display(self, reset_display=False):
        if self.entry_index_selected is not None:
            map_entry = self.msb_entries[self.first_display_index + self.entry_index_selected]
        else:
            map_entry = None
        self.field_display.refresh_fields(map_entry=map_entry, reset_display=reset_display)

    def select_entry(self, index, set_focus_to_name=True, edit_if_already_selected=True):
        """Select entry from index, based on currently displayed category."""
        old_index = self.entry_index_selected

        if old_index is not None:
            if index == old_index:
                if edit_if_already_selected:
                    return self._start_entry_name_edit(index)
                return
            else:
                self.entry_rows[old_index].active = False
        else:
            self._cancel_entry_name_edit()

        self.entry_index_selected = index
        if index is not None:
            self.entry_rows[index].active = True
            if set_focus_to_name:
                self.entry_rows[index].name_label.focus_set()
        self.refresh_field_display()

    def _refresh_buttons(self):
        # self.b_create_new_map['state'] = 'normal' if self.active_category else 'disabled'  # TODO
        if not self.msb_entries or self.first_display_index == 0:
            self.previous_range_button['state'] = 'disabled'
        else:
            self.previous_range_button['state'] = 'normal'
        if not self.msb_entries or self.first_display_index >= len(self.msb_entries) - self.ENTRY_RANGE_SIZE:
            self.next_range_button['state'] = 'disabled'
        else:
            self.next_range_button['state'] = 'normal'

    def refresh_entries(self, msb_entries=None, reset_fields=False):
        self._cancel_entry_name_edit()

        if msb_entries is not None:
            self.msb_entries = msb_entries

        if self.msb_entries:
            entries_to_display = self.msb_entries[
                self.first_display_index:self.first_display_index + self.ENTRY_RANGE_SIZE]
        else:
            entries_to_display = []  # All rows will be considered 'remaining' and hidden.

        row = 0
        for entry in entries_to_display:
            self.entry_rows[row].build_entry(entry_name=entry.name, entity_id=getattr(entry, 'entity_id', -1))
            row += 1

        self.displayed_entry_count = row

        for remaining_row in range(row, self.ENTRY_RANGE_SIZE):
            self.entry_rows[remaining_row].clear()

        self.f_entry_table.grid_columnconfigure(1, weight=1)
        self._refresh_buttons()

        if self.msb_entries:
            self.refresh_field_display(reset_display=reset_fields)

    def _change_entry_name(self, entry_index, new_text):
        """Change entry by index in the displayed category.

        TODO: parent class manages undo/redo with all-purpose navigation and editing. This returns True if any change
         actually happens, and False otherwise, to signal to that manager.
        """
        old_text = self.msb_entries[self.first_display_index + entry_index].name
        if old_text == new_text:
            return False  # Nothing to change.
        self.msb_entries[self.first_display_index + entry_index].name = new_text
        return True

    def _delete_entry(self, entry_index):
        """Deletes entry and returns it (or False upon failure) so that the action manager can undo the deletion."""
        self._cancel_entry_name_edit()
        return self.msb_entries.pop(self.first_display_index + entry_index)   # TODO: or False?

    def _update_first_display_index(self, new_index):
        """Updates first display index, ensuring that at least the last ten entries are visible."""
        new_index = min(new_index, len(self.msb_entries) - 10)
        self.first_display_index = new_index

    def _right_click_map_entry(self, event, entry_index):
        self.select_entry(entry_index, edit_if_already_selected=False)
        self.entry_rows[entry_index].context_menu.tk_popup(event.x_root, event.y_root)

    def _update_range(self, first_index):
        self._update_first_display_index(first_index)
        self.refresh_entries()
        self.select_entry(0, edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)

    def _go_to_previous_entry_range(self):
        first_index = max(self.first_display_index - self.ENTRY_RANGE_SIZE, 0)
        if first_index == self.first_display_index:
            return
        self._update_range(first_index)

    def _go_to_next_entry_range(self):
        first_index = min(self.first_display_index + self.ENTRY_RANGE_SIZE,
                          max(len(self.msb_entries) - self.ENTRY_RANGE_SIZE, 0))
        if first_index == self.first_display_index:
            return
        self._update_range(first_index)

    def _start_entry_name_edit(self, entry_index):
        if not self.e_entry_name_edit:
            self.e_entry_name_edit = self.Entry(
                self.entry_rows[entry_index].row_box,
                initial_text=self.msb_entries[self.first_display_index + entry_index].name,
                sticky='ew', width=60)
            self.e_entry_name_edit.bind('<Return>', lambda e, i=entry_index: self._confirm_entry_name_edit(i))
            self.e_entry_name_edit.bind('<Up>', self._entry_press_up)
            self.e_entry_name_edit.bind('<Down>', self._entry_press_down)
            self.e_entry_name_edit.bind('<FocusOut>', lambda e: self._cancel_entry_name_edit())
            self.e_entry_name_edit.bind('<Escape>', lambda e: self._cancel_entry_name_edit())
            self.e_entry_name_edit.focus_set()
            self.e_entry_name_edit.select_range(0, 'end')

    def _cancel_entry_name_edit(self):
        if self.e_entry_name_edit:
            self.e_entry_name_edit.destroy()
            self.e_entry_name_edit = None

    def _confirm_entry_name_edit(self, entry_index):
        if self.e_entry_name_edit:
            new_text = self.e_entry_name_edit.var.get()
            self._change_entry_name(entry_index, new_text)
            self._cancel_entry_name_edit()

    def _shift_selected_entry(self, relative_index):
        if self.entry_index_selected is None:
            return
        new_index = self.entry_index_selected + relative_index
        if new_index < 0 and self.previous_range_button['state'] == 'normal':
            self._go_to_previous_entry_range()
            self.select_entry(self.ENTRY_RANGE_SIZE - 1, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(1.0)
        elif new_index >= self.displayed_entry_count and self.next_range_button['state'] == 'normal':
            self._go_to_next_entry_range()
            self.select_entry(0, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(0.0)
        elif 0 <= new_index < self.displayed_entry_count:
            self.select_entry(self.entry_index_selected + relative_index)
        else:
            return  # Do nothing.

    def _entry_press_up(self, _=None):
        if self.entry_index_selected is not None:
            edit_new = self.e_entry_name_edit is not None
            self._confirm_entry_name_edit(self.entry_index_selected)
            self._shift_selected_entry(-1)
            if edit_new:
                self._start_entry_name_edit(self.entry_index_selected)
            if self.entry_canvas.yview()[1] != 1.0 or self.entry_index_selected < self.displayed_entry_count - 5:
                self.entry_canvas.yview_scroll(-1, 'units')

    def _entry_press_down(self, _=None):
        if self.entry_index_selected is not None:
            edit_new = self.e_entry_name_edit is not None
            self._confirm_entry_name_edit(self.entry_index_selected)
            self._shift_selected_entry(+1)
            if edit_new:
                self._start_entry_name_edit(self.entry_index_selected)
            if self.entry_canvas.yview()[0] != 0.0 or self.entry_index_selected > 5:
                self.entry_canvas.yview_scroll(1, 'units')


class SoulstructMapEditor(SoulstructSmartFrame):
    CANVAS_BG = '#1d1d1d'
    CATEGORY_BOX_WIDTH = 200
    CATEGORY_SELECTED_BG = '#555'

    entry_display: _MapEntryFrame

    def __init__(self, project: SoulstructProject, linker, master=None, toplevel=False):
        self.Maps = project.Maps
        self.linker = linker
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct Maps")

        self.active_entry_type_index = None
        self.entry_type_rows = {}

        self.action_history = ActionHistory()
        self.unsaved_changes = set()

        with self.set_master(auto_columns=0):
            with self.set_master(auto_rows=0, sticky='n'):
                self.map_choice = self.Combobox(
                    # TODO: refresh entries only
                    values=[camel_case_to_spaces(m) for m in DARK_SOULS_MAP_IDS], initial_value='Depths',
                    font=20, on_select_function=lambda _: self.refresh_entry_types(clear_selection=True),
                    padx=10, pady=10, sticky='n').var
                self.entry_list_choice = self.Combobox(
                    values=list(MAP_ENTRY_TYPES.keys()), initial_value='Parts', font=16,
                    on_select_function=lambda _: self.refresh_entry_types(clear_selection=True),
                    padx=10, pady=10, sticky='n').var

                self.f_maps_categories = self.Frame(width=self.CATEGORY_BOX_WIDTH, height=575, sticky='n')
                with self.set_master(self.f_maps_categories):
                    for row in range(13):
                        box = self.Frame(row=row, width=self.CATEGORY_BOX_WIDTH, height=30,
                                         highlightthickness=1, sticky='n')
                        label = self.Label(text='', sticky='ew', row=row)
                        label.bind("<Button-1>", lambda e, i=row: self.select_entry_type(i))
                        box.bind("<Button-1>", lambda e, i=row: self.select_entry_type(i))
                        self.entry_type_rows[row] = {
                            'box': box, 'label': label, 'entry_type_name': None, 'entry_type_enum': None}

            # Map entry window and field value window
            with self.set_master(auto_rows=0):
                with self.set_master(auto_columns=0):
                    self.entry_display = self.SmartFrame(
                        smart_frame_class=_MapEntryFrame, maps=self.Maps, linker=self.linker)

        self.refresh_entry_types()
        self.entry_display.refresh_entries(msb_entries=self.active_entry_type_data)
        self.bind_all('<Control-z>', self.undo)
        self.bind_all('<Control-y>', self.redo)

    def undo(self, _=None):
        if not self.action_history.undo():
            self['bg'] = '#522'
            self.after(200, lambda: self.config(bg=self.STYLE_DEFAULTS['bg']))

    def redo(self, _=None):
        if not self.action_history.redo():
            self['bg'] = '#522'
            self.after(200, lambda: self.config(bg=self.STYLE_DEFAULTS['bg']))

    def refresh_entry_types(self, _=None, clear_selection=False):
        row = 0
        for entry_type_name, entry_type_enum in MAP_ENTRY_TYPES[self.active_entry_list_name].items():
            self.build_row(row, entry_type_name, entry_type_enum)
            row += 1

        for remaining_row in range(row, 13):
            self.clear_row(remaining_row)

        if clear_selection:
            self.select_entry_type(None)
            self.entry_display.select_entry(None)
            self.entry_display.refresh_entries(self.active_entry_type_data, reset_fields=True)

    def select_entry_type(self, entry_type_index, first_display_index=0):
        old_entry_type_index = self.active_entry_type_index
        if entry_type_index is not None and entry_type_index == old_entry_type_index:
            return  # Nothing to change (no editing).
        self.active_entry_type_index = entry_type_index

        if old_entry_type_index is not None:
            self.set_row_bg(old_entry_type_index, self.STYLE_DEFAULTS['bg'])

        if self.active_entry_type_index is not None:
            self.set_row_bg(self.active_entry_type_index, self.CATEGORY_SELECTED_BG)

        self.entry_display.first_display_index = first_display_index
        self.entry_display.select_entry(None, edit_if_already_selected=False)
        self.entry_display.refresh_entries(self.active_entry_type_data, reset_fields=True)
        self.entry_display.entry_canvas.yview_moveto(0)

    def build_row(self, row, entry_type_name, entry_type_enum):
        self.entry_type_rows[row]['entry_type_name'] = entry_type_name
        self.entry_type_rows[row]['entry_type_enum'] = entry_type_enum
        self.entry_type_rows[row]['label'].var.set(camel_case_to_spaces(entry_type_name))
        self.entry_type_rows[row]['box'].grid()
        self.entry_type_rows[row]['label'].grid()

    def clear_row(self, row):
        self.entry_type_rows[row]['entry_type_name'] = ''
        self.entry_type_rows[row]['entry_type_enum'] = None
        self.entry_type_rows[row]['label'].var.set('')
        self.entry_type_rows[row]['box'].grid_remove()
        self.entry_type_rows[row]['label'].grid_remove()

    def set_row_bg(self, row, color):
        self.entry_type_rows[row]['box']['bg'] = color
        self.entry_type_rows[row]['label']['bg'] = color

    @property
    def active_map_name(self) -> str:
        return self.map_choice.get().replace(' ', '')

    @property
    def active_map_data(self) -> MSB:
        return self.Maps[self.active_map_name]

    @property
    def active_entry_list_name(self) -> str:
        return self.entry_list_choice.get()

    @property
    def active_entry_type_data(self) -> list:
        if self.active_entry_type_index is None:
            return []
        entry_type_enum = self.entry_type_rows[self.active_entry_type_index]['entry_type_enum']
        entry_list = getattr(self.active_map_data, self.active_entry_list_name.lower())
        return entry_list.get_entries(entry_type=entry_type_enum)


class _MapNameSelectionBox(SoulstructSmartFrame):
    """Small pop-out widget that allows you to select a particular type."""

    WIDTH = 50  # characters
    HEIGHT = 25  # lines

    def __init__(self, master: _MapFieldFrame, field_type):
        self.field_row = master
        super().__init__(toplevel=True, master=master, window_title="Select Entry")
        names = self.field_row.linker.get_map_entry_type_names(field_type)

        self.output = None

        with self.set_master(padx=20, pady=20):
            self._names = self.Listbox(
                values=names, width=self.WIDTH, height=self.HEIGHT, vertical_scrollbar=True, selectmode='single',
                font=16, padx=20, pady=20)

        self._names.bind('<Double-Button-1>', lambda e: self.done(True))

        self.bind_all('<Escape>', lambda e: self.done(False))
        self.protocol('WM_DELETE_WINDOW', lambda: self.done(False))
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3), transient=True)

    def go(self):
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def done(self, confirm=True):
        if confirm:
            self.output = self._names.get(self._names.curselection())
        self.quit()
