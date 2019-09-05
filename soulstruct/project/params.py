from __future__ import annotations

from enum import IntEnum
from typing import List, Optional, TYPE_CHECKING

from soulstruct.project.actions import ActionHistory
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SoulstructSmartFrame, ToolTip

if TYPE_CHECKING:
    from soulstruct.params import DarkSoulsGameParameters
    from soulstruct.params.core import ParamEntry, ParamTable
    from soulstruct.project.core import SoulstructProject


# TODO: Can't jump to Conversations, because they're internal by default.
# TODO: right click on entry to gain options to edit name, summary, description for appropriate types


def bind_events(widget, bindings: dict):
    for event, func in bindings.items():
        widget.bind(event, func)


class _ParamEntryRow(object):
    """Container for components of a row in the _ParamEntryFrame.

    These are only created once, and their contents are refreshed when needed.
    """

    def __init__(self, master: _ParamEntryFrame, row_index: int, main_bindings: dict = None):
        self.master = master
        self.linker = master.linker
        self.STYLE_DEFAULTS = master.STYLE_DEFAULTS

        self.entry_id = None
        self.entry_name = None

        self.index = row_index
        self._active = False
        self.any_text_missing = False

        bg_color = self._get_color()

        self.row_box = master.Frame(
            width=master.ENTRY_BOX_WIDTH, height=30, bg=bg_color, row=row_index, columnspan=2,
            sticky='nsew')
        bind_events(self.row_box, main_bindings)

        self.id_label = master.Label(text='', width=15, row=row_index, column=0, bg=bg_color, sticky='e')
        bind_events(self.id_label, main_bindings)

        self.name_box = master.Frame(row=row_index, column=1, bg=bg_color, sticky='ew')
        bind_events(self.name_box, main_bindings)

        self.name_label = master.Label(self.name_box, text='', bg=bg_color, anchor='w', width=60)
        bind_events(self.name_label, main_bindings)

        self.context_menu = master.Menu(self.row_box)
        self.tool_tip = ToolTip(self.row_box, self.id_label, self.name_box, self.name_label, text=None,
                                wraplength=350)

    def build_entry(self, entry_id: int, entry_name: str):
        self.entry_id = entry_id
        self.entry_name = entry_name

        text_links = self.linker.entry_text_link(self.entry_id)
        name_extension = f" [{text_links[0].name}]" if text_links and text_links[0].name else ""
        self.id_label.var.set(str(self.entry_id))
        self.name_label.var.set(self.entry_name + name_extension)

        if text_links and not any(link.name for link in text_links) and not self.any_text_missing:
            self.any_text_missing = True
            self._update_colors()
        elif (not text_links or all(link.name for link in text_links)) and self.any_text_missing:
            self.any_text_missing = False
            self._update_colors()

        self.build_entry_context_menu(text_links)
        if text_links and text_links[2].name:
            self.tool_tip.text = text_links[2].name
        else:
            self.tool_tip.text = None

        self.row_box.grid()
        self.id_label.grid()
        self.name_box.grid()
        self.name_label.grid()

    def clear(self):
        """Called when this row has no entry to display."""
        self.row_box.grid_remove()
        self.id_label.grid_remove()
        self.name_box.grid_remove()
        self.name_label.grid_remove()

    def build_entry_context_menu(self, text_links):
        # TODO: other stuff? Pop out a text edit box?
        # TODO: Other function I can think of here is 'view uses', which will search for things that link to this
        #  type of param (e.g. other params). Such places should be indexed already so they can be searched.
        self.context_menu.delete(0, 'end')
        if text_links:
            for text_link in text_links:
                if text_link.name != 'None':
                    self.context_menu.add_command(
                        label=text_link.menu_text, foreground=self.STYLE_DEFAULTS['text_fg'], command=text_link.link)

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
        for widget in (self.row_box, self.id_label, self.name_box, self.name_label):
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


class _ParamFieldRow(object):
    """Container for components of a row in the _ParamFieldFrame.

    These are only created once, and their contents are refreshed when needed. Unlike entries, field value widgets may
    be Labels (which turn to Entries for editing), Checkbuttons, or Comboboxes. Each of these widgets is created for
    each row, so they can be displayed (with `grid()`) when needed, rather than dynamically created and destroyed
    every time a new entry/category is selected.
    """
    ROW_HEIGHT = 30

    def __init__(self, master: _ParamFieldFrame, row_index: int, change_value_func, main_bindings: dict = None):
        self.master = master
        self.linker = master.linker
        self.STYLE_DEFAULTS = master.STYLE_DEFAULTS
        self.param_entry = None

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
            self.field_name_box, text='', fg=master.FIELD_NAME_FG, width=30, bg=bg_color, anchor='w')
        bind_events(self.field_name_label, main_bindings)

        self.value_box = master.Frame(width=200, row=row_index, column=1, bg=bg_color, sticky='ew')
        bind_events(self.value_box, main_bindings)

        # VALUE WIDGETS

        self.value_label = master.Label(self.value_box, text='', bg=bg_color, width=50, anchor='w')
        bind_events(self.value_label, main_bindings)

        self.value_checkbutton = master.Checkbutton(
            self.value_box, label=None, bg=bg_color, no_grid=True,
            command=lambda: change_value_func(self.index, self.value_checkbutton.var.get()))
        # Main focus bindings are not bound to Checkbutton.

        self.value_combobox = master.Combobox(
            self.value_box, values=None, width=20, no_grid=True,
            on_select_function=lambda _: change_value_func(
                self.index, getattr(self.field_type, self.value_combobox.var.get().replace(' ', '')).value))
        # Main focus bindings are not bound to Combobox.
        # TODO: BEHAVIOR_REF_TYPE combobox should also force a refresh, as it may change field names.
        #  (Class will need access to ParamEntry for this, which is fine.)

        self.context_menu = master.Menu(self.row_box)
        self.tool_tip = ToolTip(self.row_box, self.field_name_box, self.field_name_label, text=None)

        self.active_value_widget = self.value_label
        self.clear()  # TODO: still getting white box before I click or scroll

    def _activate_value_widget(self, widget):
        if widget is self.value_label:
            if id(self.active_value_widget) in {id(self.value_checkbutton), id(self.value_combobox)}:
                self.active_value_widget.grid_remove()
            self.active_value_widget = self.value_label
        if widget is self.value_checkbutton:
            if id(self.active_value_widget) in {id(self.value_label), id(self.value_combobox)}:
                self.active_value_widget.grid_remove()
            self.active_value_widget = self.value_checkbutton
        if widget is self.value_combobox:
            if id(self.active_value_widget) in {id(self.value_label), id(self.value_checkbutton)}:
                self.active_value_widget.grid_remove()
            self.active_value_widget = self.value_combobox

    def build_field(self, entry, name, value, nickname, field_type, docstring="DOC-TODO"):
        """Update widgets with given field information."""
        self.param_entry = entry
        nickname = camel_case_to_spaces(nickname)
        self.field_name = name
        self.field_type = field_type
        self.field_docstring = docstring

        if isinstance(self.field_type, str):
            param_links = self.linker.soulstruct_link(self.field_type, self.param_entry[self.field_name],
                                                      special_values={0: 'Default', -1: 'Default'})
            field_type = int
        else:
            param_links = []

        if issubclass(field_type, IntEnum):
            self.value_combobox['values'] = [camel_case_to_spaces(e.name) for e in field_type]
            try:
                # noinspection PyUnresolvedReferences
                enum_name = camel_case_to_spaces(field_type(value).name)
            except ValueError:
                enum_name = f'<Unknown: {value}>'  # TODO: ensure this is read back and saved properly
            self.value_combobox.var.set(enum_name)
            self._activate_value_widget(self.value_combobox)
        elif field_type in {float, int}:
            value_text = f'{value:.3f}' if field_type == float else str(value)
            if param_links:
                if len(param_links) > 1:
                    value_text += f' [Ambiguous]'
                if param_links[0].name is None:
                    value_text += f' [MISSING]'
                else:
                    value_text += f' [{param_links[0].name}]'
            if self.value_label.var.get() != value_text:
                self.value_label.var.set(value_text)  # TODO: probably a redundant check in terms of update efficiency
            self._activate_value_widget(self.value_label)
        elif field_type == bool:
            if value not in {0, 1}:
                raise ValueError(f"Field with 'bool' type has non-boolean value: {value}")
            self.value_checkbutton.var.set(value)
            self._activate_value_widget(self.value_checkbutton)

        if self.field_name_label.var.get() != nickname:
            self.field_name_label.var.set(nickname)

        if param_links and not any(link.name for link in param_links) and not self.link_missing:
            self.link_missing = True
            self._update_colors()
        elif (not param_links or any(link.name for link in param_links)) and self.link_missing:
            self.link_missing = False
            self._update_colors()

        self.build_field_context_menu(param_links)
        self.tool_tip.text = docstring

        self.row_box.grid()
        self.field_name_box.grid()
        self.field_name_label.grid()
        self.value_box.grid()
        self.active_value_widget.grid()

    def build_field_context_menu(self, param_links):
        # TODO: other stuff? Pop out a scroll box to select an entry, for linked fields?
        self.context_menu.delete(0, 'end')
        if param_links:
            for param_link in param_links:
                if param_link.name != 'None':
                    self.context_menu.add_command(
                        label=param_link.menu_text, foreground=self.STYLE_DEFAULTS['text_fg'], command=param_link)

    def clear(self):
        """Called when this row has no field to display (e.g. for smaller ParamTables or unselected entry)."""
        self.row_box.grid_remove()
        self.field_name_box.grid_remove()
        self.field_name_label.grid_remove()
        self.value_box.grid_remove()
        self.active_value_widget.grid_remove()

    @property
    def editable(self):
        return self.active_value_widget is self.value_label

    def confirm_edit(self, new_text):
        if not self.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")

        if isinstance(self.field_type, str):
            new_value = int(new_text)
            param_links = self.linker.soulstruct_link(self.field_type, new_value,
                                                      special_values={0: 'Default', -1: 'Default'})
            if len(param_links) > 1:
                new_text += f' [Ambiguous]'
            elif param_links and param_links[0].name is None:
                new_text += f' [MISSING]'
            elif param_links:
                new_text += f' [{param_links[0].name}]'
            self.value_label.var.set(new_text)
            return new_value

        self.value_label.var.set(new_text)

        if self.field_type == float:
            return float(new_text)
        elif self.field_type == int:
            return int(new_text)

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
        for widget in (self.row_box, self.field_name_box, self.field_name_label, self.value_box,
                       self.value_label, self.value_checkbutton):
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


class _ParamFieldFrame(SoulstructSmartFrame):
    FIELD_CANVAS_BG = '#1d1d1d'
    FIELD_BOX_WIDTH = 550
    FIELD_ROW_COUNT = 173  # highest count (Special Effects)
    FIELD_NAME_FG = '#DDE'

    def __init__(self, params, linker, master=None):
        super().__init__(master=master, toplevel=False)
        self.Params = params  # type: DarkSoulsGameParameters
        self.linker = linker

        self.param_entry = None
        self.e_field_value_edit = None
        self.field_index_selected = None
        self.displayed_field_count = 0
        self.field_rows = []  # type: List[_ParamFieldRow]

        self.field_canvas = self.Canvas(vertical_scrollbar=True, width=self.FIELD_BOX_WIDTH, height=500,
                                        yscrollincrement=25, highlightthickness=1,
                                        padx=40, pady=40, bg=self.FIELD_CANVAS_BG)
        self.f_field_table = self.Frame(frame=self.field_canvas, width=self.FIELD_BOX_WIDTH,
                                        sticky='ew')
        self.field_canvas.create_window(
            self.FIELD_BOX_WIDTH / 2, 250, window=self.f_field_table, anchor='nw')
        self.f_field_table.bind(
            "<Configure>", lambda e, c=self.field_canvas: self.reset_canvas_scroll_region(c))

        with self.set_master(self.f_field_table):
            for row in range(self.FIELD_ROW_COUNT):
                self.field_rows.append(_ParamFieldRow(
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

    def refresh(self, param_entry: ParamEntry = None, field_info_func=None,
                show_hidden_fields=False, reset_display=False):
        """Refresh all field name/value labels."""
        self._cancel_field_value_edit()

        if param_entry is not None:
            self.param_entry = param_entry

        field_names = field_info_func(self.param_entry).keys() if self.param_entry is not None else []

        row = 0
        for field_name in field_names:

            field_nickname, is_main, field_type, field_doc = field_info_func(self.param_entry, field_name)
            if (isinstance(field_type, str) and '<Pad:' in field_type) or (not is_main and not show_hidden_fields):
                continue  # Skip hidden field (or always skip Pad field).

            field_nickname = camel_case_to_spaces(field_nickname)

            self.field_rows[row].build_field(
                entry=self.param_entry,
                name=field_name,
                value=self.param_entry[field_name],
                nickname=field_nickname,
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

    def select_field(self, index, set_focus_to_value=True, edit_if_already_selected=True):
        # TODO: should this start editing immediately (on left click)?
        # TODO: tab while editing moves to next field. Shift+Tab moves back. Up and down arrows also work.

        old_index = self.field_index_selected

        if old_index is not None and index == old_index:
            if edit_if_already_selected and self.field_rows[index].editable:
                return self._start_field_value_edit(index)
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

    def _start_field_value_edit(self, index):
        if not self.e_field_value_edit:
            field_row = self.field_rows[index]
            if not field_row.editable:
                raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")
            field_name = field_row.field_name
            if field_row.field_type == float:
                self.e_field_value_edit = self.Entry(
                    field_row.value_box, numbers_only=True, initial_text=self.param_entry[field_name],
                    sticky='ew', width=5)
            elif field_row.field_type == int or isinstance(field_row.field_type, str):
                self.e_field_value_edit = self.Entry(
                    field_row.value_box, integers_only=True, initial_text=self.param_entry[field_name],
                    sticky='ew', width=5)
            self.e_field_value_edit.bind('<Return>', lambda e, i=index: self._confirm_field_value_edit(i))
            self.e_field_value_edit.bind('<Up>', self.field_press_up)
            self.e_field_value_edit.bind('<Down>', self.field_press_down)
            self.e_field_value_edit.bind('<FocusOut>', lambda e: self._cancel_field_value_edit())
            self.e_field_value_edit.bind('<Escape>', lambda e: self._cancel_field_value_edit())
            self.e_field_value_edit.focus_set()
            self.e_field_value_edit.select_range(0, 'end')

    def _cancel_field_value_edit(self):
        if self.e_field_value_edit:
            self.e_field_value_edit.destroy()
            self.e_field_value_edit = None

    def _confirm_field_value_edit(self, index):
        if self.e_field_value_edit:
            try:
                true_value = self.field_rows[index].confirm_edit(new_text=self.e_field_value_edit.var.get())
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
        old_value = self.param_entry[field_name]
        if old_value == new_value:
            return False  # Nothing to change.
        self.param_entry[field_name] = new_value
        return True


class _ParamEntryFrame(SoulstructSmartFrame):
    """Manages param entry selection/modification in editor."""
    ENTRY_CANVAS_BG = '#1d1d1d'
    ENTRY_BOX_WIDTH = 450
    ENTRY_RANGE_SIZE = 50

    field_display: _ParamFieldFrame

    def __init__(self, params, linker, master=None):
        super().__init__(master=master, toplevel=False)
        self.Params = params
        self.linker = linker

        self.param_table = None  # type: Optional[ParamTable]
        self.entry_rows = []  # type: List[_ParamEntryRow]
        self.entry_index_selected = None
        self.first_display_index = 0
        self.displayed_entry_count = 0
        self.e_entry_name_edit = None

        with self.set_master(auto_rows=0):
            with self.set_master(auto_columns=0):
                self.previous_range_button = self.Button(
                    text=f"Previous {self.ENTRY_RANGE_SIZE}", bg='#722', width=30,
                    command=self._go_to_previous_entry_range, padx=10, pady=20, row=0, sticky='w')

                # TODO
                # self.b_create_new_param = self.Button(
                #     text="Create New Text ID", bg='#722', width=30, command=self.create_new_param_id,
                #     padx=10, pady=20)

                # TODO: restore
                # self.find_param_id_entry = self.Entry(
                #     label="Find ID:", label_position='left', width=14, padx=10)
                # self.find_param_id_entry.bind('<Return>', lambda e: self.find_param_id())
                # with self.set_master(auto_rows=0):
                #     self.find_text_string_entry = self.Entry(
                #         label="Find Text:", label_position='left', width=14, padx=10)
                #     self.find_text_string_entry.bind('<Return>', lambda e: self.find_text_string())
                #     self.replace_text_string_entry = self.Entry(
                #         label="Replace With:", label_position='left', width=14, padx=10)
                #     self.replace_text_string_entry.bind('<Return>', lambda e: self.find_text_string(replace=True))

                self.show_hidden_fields = self.Checkbutton(
                    label='Show hidden fields', initial_state=False,
                    command=lambda: self.refresh_field_display(reset_display=True), pady=20).var

            with self.set_master(auto_columns=0):
                with self.set_master():
                    self.entry_canvas = self.Canvas(  # TODO: what should height actually be?
                        vertical_scrollbar=True, width=self.ENTRY_BOX_WIDTH, height=500, highlightthickness=1,
                        yscrollincrement=30, padx=40, pady=40, bg=self.ENTRY_CANVAS_BG)
                    self.f_entry_table = self.Frame(frame=self.entry_canvas, width=self.ENTRY_BOX_WIDTH, sticky='ew')
                    self.entry_canvas.create_window(self.ENTRY_BOX_WIDTH / 2, 250, window=self.f_entry_table,
                                                    anchor='nw')
                    self.f_entry_table.bind(
                        "<Configure>", lambda e, c=self.entry_canvas: self.reset_canvas_scroll_region(c))

                with self.set_master():
                    self.field_display = self.SmartFrame(
                        smart_frame_class=_ParamFieldFrame, params=self.Params, linker=self.linker)

            with self.set_master(self.f_entry_table):
                for row in range(self.ENTRY_RANGE_SIZE):
                    self.entry_rows.append(_ParamEntryRow(
                        self, row_index=row, main_bindings={
                            '<Button-1>': lambda _, i=row: self.select_entry(i),
                            '<Button-3>': lambda e, i=row: self._right_click_param_entry(e, i),
                            '<Up>': self._entry_press_up,
                            '<Down>': self._entry_press_down,
                            '<Prior>': lambda e: self._go_to_previous_entry_range(),
                            '<Next>': lambda e: self._go_to_next_entry_range(),
                        }))

            with self.set_master(auto_columns=0):
                self.next_range_button = self.Button(
                    text=f"Next {self.ENTRY_RANGE_SIZE}", bg='#722', width=30, command=self._go_to_next_entry_range,
                    padx=10, pady=20)

    def refresh_field_display(self, reset_display=False):
        if self.entry_index_selected is not None:
            param_id = self.entry_rows[self.entry_index_selected].entry_id
            param_entry = self.param_table[param_id]
        else:
            param_entry = None
        self.field_display.refresh(param_entry=param_entry, field_info_func=self.param_table.get_field_info,
                                   show_hidden_fields=self.show_hidden_fields.get(), reset_display=reset_display)

    def select_entry(self, index, set_focus_to_name=True, edit_if_already_selected=True):
        """Select entry from index, based on currently displayed category."""
        old_index = self.entry_index_selected

        if old_index is not None:
            if index == old_index:
                if edit_if_already_selected:
                    return self._start_entry_name_edit(index)
                return
        else:
            self._cancel_entry_name_edit()

        self.entry_index_selected = index

        if old_index is not None:
            self.entry_rows[old_index].active = False
        self.entry_rows[index].active = True
        if set_focus_to_name:
            self.entry_rows[index].name_label.focus_set()
        self.refresh_field_display()

    def _refresh_buttons(self):
        # self.b_create_new_param['state'] = 'normal' if self.active_category else 'disabled'  # TODO
        if not self.param_table or self.first_display_index == 0:
            self.previous_range_button['state'] = 'disabled'
        else:
            self.previous_range_button['state'] = 'normal'
        if not self.param_table or self.first_display_index >= len(self.param_table) - self.ENTRY_RANGE_SIZE:
            self.next_range_button['state'] = 'disabled'
        else:
            self.next_range_button['state'] = 'normal'

    def refresh_entries(self, param_table: ParamTable = None, reset_fields=False):
        self._cancel_entry_name_edit()

        if param_table is not None:
            self.param_table = param_table

        if self.param_table:
            entries_to_display = self.param_table.get_range(start=self.first_display_index, count=self.ENTRY_RANGE_SIZE)
        else:
            entries_to_display = []  # All rows will be considered 'remaining' and hidden.

        row = 0
        for entry_id, entry in entries_to_display:
            self.entry_rows[row].build_entry(
                entry_id=entry_id,
                entry_name=entry.name,
                # TODO: text link may need refreshing when edited.
            )
            row += 1

        self.displayed_entry_count = row

        for remaining_row in range(row, self.ENTRY_RANGE_SIZE):
            self.entry_rows[remaining_row].clear()

        self.f_entry_table.grid_columnconfigure(1, weight=1)
        self._refresh_buttons()

        if self.param_table:
            self.refresh_field_display(reset_display=reset_fields)

    def _get_param_index(self, param_id):
        """Get index of given param ID in currently displayed category."""
        if param_id not in self.param_table:
            raise ValueError(f"There is no ParamEntry with ID {param_id} in category {self.param_table.name}.")
        return sorted(self.param_table).index(param_id)

    def _change_entry_name(self, entry_index, new_text):
        """Change entry by index in the displayed category.

        TODO: parent class manages undo/redo with all-purpose navigation and editing. This returns True if any change
         actually happens, and False otherwise, to signal to that manager.
        """
        entry_id = self.entry_rows[entry_index].entry_id
        old_text = self.param_table[entry_id].name
        if old_text == new_text:
            return False  # Nothing to change.
        self.param_table[entry_id].name = new_text
        return True

    def _add_entry(self, param_id, name):
        # TODO: Need some kind of default template for each param if this will be allowed - better to duplicate.
        #  Maybe you can indicate what param ID you want to copy, at least.
        if param_id < 0:
            self.dialog("Text ID Error", message=f"Text ID cannot be negative.")
            return False
        if param_id in self.param_table:
            self.dialog("Text ID Error", message=f"Text ID {param_id} already exists in category "
                                                 f"{camel_case_to_spaces(self.param_table.nickname)}.")
            return False

        self._cancel_entry_name_edit()
        self.param_table[param_id].name = name
        new_index = self._get_param_index(param_id)
        self._update_first_display_index(new_index)
        self.refresh_entries()
        self.select_entry(new_index)
        return True

    def _add_relative_entry(self, param_id, offset=1, name=None):
        if name is None:
            name = self.param_table[param_id].name
        self._add_entry(param_id=param_id + offset, name=name)

    def _delete_entry(self, entry_index):
        """Deletes entry and returns it (or False upon failure) so that the action manager can undo the deletion."""
        self._cancel_entry_name_edit()
        entry_id = self.entry_rows[entry_index].entry_id
        return self.param_table.pop(entry_id)   # TODO: or False?

    def _update_first_display_index(self, new_index):
        """Updates first display index, ensuring that at least the last ten entries are visible."""
        new_index = min(new_index, len(self.param_table) - 10)
        self.first_display_index = new_index

    def _right_click_param_entry(self, event, entry_index):
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
                          max(len(self.param_table) - self.ENTRY_RANGE_SIZE, 0))
        if first_index == self.first_display_index:
            return
        self._update_range(first_index)

    def _start_entry_name_edit(self, entry_index):
        if not self.e_entry_name_edit:
            param_id = self.entry_rows[entry_index].entry_id
            self.e_entry_name_edit = self.Entry(
                self.entry_rows[entry_index].name_box, initial_text=self.param_table[param_id].name,
                sticky='ew', width=60)
            self.e_entry_name_edit.bind('<Return>', lambda e, i=param_id: self._confirm_entry_name_edit(i))
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


class SoulstructParamsEditor(SoulstructSmartFrame):
    CANVAS_BG = '#1d1d1d'
    CATEGORY_BOX_WIDTH = 200
    CATEGORY_SELECTED_BG = '#555'

    entry_display: _ParamEntryFrame

    def __init__(self, project: SoulstructProject, linker, master=None, toplevel=False):
        self.Params = project.Params
        self.linker = linker
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct Params")

        self.active_category = None
        self.category_boxes = {}

        self.action_history = ActionHistory()
        self.unsaved_changes = set()  # set of changed (category, param_id, action_type) pairs to highlight

        with self.set_master(auto_columns=0):
            # Category selection window
            with self.set_master(auto_rows=0):
                self.param_category_canvas = self.Canvas(
                    vertical_scrollbar=True, width=self.CATEGORY_BOX_WIDTH, height=575, padx=40, pady=40,
                    highlightthickness=0)
                self.f_params_categories = self.Frame(width=self.CATEGORY_BOX_WIDTH, height=575, sticky='ew')
                self.link_to_scrollable(self.param_category_canvas, self.f_params_categories)
                self.param_category_canvas.create_window(
                    self.CATEGORY_BOX_WIDTH / 2, 300, window=self.f_params_categories, anchor='nw')
                self.f_params_categories.bind(
                    "<Configure>", lambda e, c=self.param_category_canvas: self.reset_canvas_scroll_region(c))

                self.refresh_categories()

            # Param entry window and field value window
            with self.set_master(auto_rows=0):
                with self.set_master(auto_columns=0):
                    self.entry_display = self.SmartFrame(
                        smart_frame_class=_ParamEntryFrame, params=self.Params, linker=self.linker)

        self.entry_display.refresh_entries(param_table=self.active_category_param_table)
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

    def refresh_categories(self):
        for box, label in self.category_boxes.values():
            box.destroy()
            label.destroy()
        self.category_boxes = {}
        with self.set_master(self.f_params_categories):
            categories = self.Params.param_names
            for row, category in enumerate(categories):
                box = self.Frame(row=row, width=self.CATEGORY_BOX_WIDTH, height=30, highlightthickness=1)
                label_text = camel_case_to_spaces(category).replace(' _', ':')
                label = self.Label(text=label_text, sticky='ew', row=row)
                label.bind("<Button-1>", lambda e, c=category: self.select_category(c))
                box.bind("<Button-1>", lambda e, c=category: self.select_category(c))
                if category == self.active_category:
                    label['bg'] = self.CATEGORY_SELECTED_BG
                    box['bg'] = self.CATEGORY_SELECTED_BG
                self.link_to_scrollable(self.param_category_canvas, box, label)
                self.category_boxes[category] = (box, label)

    def select_category(self, selected_category, first_display_index=0):
        if selected_category != self.active_category:
            self.active_category = selected_category
            for category, (box, label) in self.category_boxes.items():
                if selected_category == category:
                    box['bg'] = self.CATEGORY_SELECTED_BG
                    label['bg'] = self.CATEGORY_SELECTED_BG
                else:
                    box['bg'] = self.STYLE_DEFAULTS['bg']
                    label['bg'] = self.STYLE_DEFAULTS['bg']

        self.entry_display.first_display_index = first_display_index
        self.entry_display.refresh_entries(param_table=self.active_category_param_table, reset_fields=True)
        self.entry_display.select_entry(0, edit_if_already_selected=False)
        self.entry_display.entry_canvas.yview_moveto(0)

    @property
    def active_category_param_table(self) -> ParamTable:
        return self.Params[self.active_category] if self.active_category is not None else None

    @property
    def active_category_sorted_ids(self):
        if self.active_category is None:
            return None
        return sorted(self.Params[self.active_category])
