from __future__ import annotations
from functools import partial
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from soulstruct.project.actions import ActionHistory
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SoulstructSmartFrame

if TYPE_CHECKING:
    from soulstruct.params.core import ParamEntry, ParamTable
    from soulstruct.project.core import SoulstructProject


class _ParamFieldFrame(SoulstructSmartFrame):
    FIELD_CANVAS_BG = '#1d1d1d'
    FIELD_BOX_WIDTH = 500
    FIELD_ROW_COUNT = 150  # TODO: set to max field count
    FIELD_NAME_FG = '#DDE'

    def __init__(self, master=None):
        super().__init__(master=master, toplevel=False)

        self.param_entry = None
        self.e_field_value_edit = None
        self.field_index_selected = None
        self.displayed_field_count = 0
        self.field_row_boxes = []  # type: List[Dict[str, Dict]]

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
            self.field_row_boxes = [self._create_field_row(row) for row in range(self.FIELD_ROW_COUNT)]

    def refresh(self, param_entry: ParamEntry = None, field_info_func=None,
                show_hidden_fields=False, reset_display=False):
        self._cancel_field_value_edit()

        if param_entry is None:
            param_entry = self.param_entry
        else:
            self.param_entry = param_entry

        try:
            field_names = self.param_entry.field_names
        except AttributeError:
            field_names = []  # All rows will be considered 'remaining' and hidden.

        row = 0
        for field_name in field_names:

            # TODO: print utility
            print(f"        {repr(field_name)}: (\n"
                  f"            '', True, None,\n"
                  f"            \"\"),")

            # TODO: use type and doc
            field_nickname, is_main, field_type, field_doc = field_info_func(param_entry, field_name)
            if (isinstance(field_type, str) and '<Pad:' in field_type) or (not is_main and not show_hidden_fields):
                continue  # Skip hidden field.

            field_value_raw = self.param_entry[field_name]
            if isinstance(field_value_raw, float):
                field_value_str = f'{field_value_raw:.3f}'
            else:
                field_value_str = str(field_value_raw)

            row_dict = self.field_row_boxes[row]
            field_nickname = camel_case_to_spaces(field_nickname)

            row_and_name_bg, value_box_bg, value_label_bg = self._get_field_colors(row, field_value_str)
            row_dict['field_name'] = field_name
            if row_dict['row_box']['bg'] != row_and_name_bg:
                row_dict['row_box'].config(bg=row_and_name_bg)
            row_dict['row_box'].grid()
            if row_dict['field_name_box']['bg'] != row_and_name_bg:
                row_dict['field_name_box'].config(bg=row_and_name_bg)
            row_dict['field_name_box'].grid()
            if row_dict['field_name_label']['bg'] != row_and_name_bg:
                row_dict['field_name_label'].config(bg=row_and_name_bg)
            if row_dict['field_name_label'].var.get() != field_nickname:
                row_dict['field_name_label'].var.set(field_nickname)
            row_dict['field_name_label'].grid()
            if row_dict['value_box']['bg'] != value_box_bg:
                row_dict['value_box'].config(bg=value_box_bg)
            row_dict['value_box'].grid()
            if row_dict['value_label']['bg'] != value_label_bg:
                row_dict['value_label'].config(bg=value_label_bg)
            if row_dict['value_label'].var.get() != field_value_str:
                row_dict['value_label'].var.set(field_value_str)
            row_dict['value_label'].grid()
            row += 1

        self.displayed_field_count = row

        for remaining_row in range(row, self.FIELD_ROW_COUNT):
            row_dict = self.field_row_boxes[remaining_row]
            row_dict['field_name'] = ''
            row_dict['row_box'].grid_remove()
            row_dict['field_name_box'].grid_remove()
            row_dict['field_name_label'].grid_remove()
            row_dict['value_box'].grid_remove()
            row_dict['value_label'].grid_remove()

        self.f_field_table.grid_columnconfigure(1, weight=1)

        if reset_display:
            self.select_field(0, edit_if_already_selected=False)
            self.field_canvas.yview_moveto(0)

    def select_field(self, field_index, set_focus_to_value=True, edit_if_already_selected=True):
        # TODO: should this start editing immediately (on left click)?
        # TODO: tab while editing moves to next field. Shift+Tab moves back. Up and down arrows also work.
        # TODO: select entire value when editing starts.

        old_field_index = self.field_index_selected

        if old_field_index is not None and field_index == old_field_index:
            if edit_if_already_selected:
                return self._start_field_value_edit(field_index)
            return
        else:
            self._cancel_field_value_edit()

        self.field_index_selected = field_index

        self._update_row_colors(field_index)
        if old_field_index is not None:
            self._update_row_colors(old_field_index)
        if set_focus_to_value:
            self.field_row_boxes[field_index]['value_label'].focus_set()

    def _update_row_colors(self, row):
        row_dict = self.field_row_boxes[row]
        field_name = row_dict['field_name']
        value_string = str(self.param_entry[field_name])  # never reads from label directly
        row_and_name_bg, value_box_bg, value_label_bg = self._get_field_colors(row, value_string)
        row_dict['row_box'].config(bg=row_and_name_bg)
        row_dict['field_name_box'].config(bg=row_and_name_bg)
        row_dict['field_name_label'].config(bg=row_and_name_bg)
        row_dict['value_label'].config(bg=value_label_bg)
        row_dict['value_box'].config(bg=value_box_bg)

    def _create_field_row(self, row):
        row_and_name_bg, value_box_bg, value_label_bg = self._get_field_colors(row)
        row_box = self.Frame(
            width=self.FIELD_BOX_WIDTH, height=25, bg=row_and_name_bg, row=row, columnspan=2, sticky='nsew')
        self._bind_field_row_events(row_box, row)

        field_name_box = self.Frame(row=row, column=0, bg=row_and_name_bg, sticky='w')
        self._bind_field_row_events(field_name_box, row)

        field_name_label = self.Label(field_name_box, text='', fg=self.FIELD_NAME_FG, width=30,
                                      bg=row_and_name_bg, anchor='w')
        self._bind_field_row_events(field_name_label, row)

        value_box = self.Frame(width=200, row=row, column=1, bg=value_box_bg, sticky='ew')
        self._bind_field_row_events(value_box, row)

        value_label = self.Label(value_box, text='', bg=value_label_bg, width=10, anchor='w')
        self._bind_field_row_events(value_label, row)

        # context_menu = self.build_field_context_menu(field_name, field_doc)  # TODO

        return {'row_box': row_box, 'field_name_box': field_name_box, 'field_name_label': field_name_label,
                'value_box': value_box, 'value_label': value_label, 'field_name': '', 'context_menu': None}

    def _get_field_colors(self, row, field_value=None):
        """Inspects field name/data and returns a tuple of 'bg' color values."""
        base_bg = 222
        row_and_name_bg = value_box_bg = value_label_bg = 0
        if field_value is not None and field_value == '':
            base_bg += 200
        if row == self.field_index_selected:
            base_bg += 123
        if row % 2:
            base_bg += 111
        return f'#{base_bg + row_and_name_bg}', f'#{base_bg + value_box_bg}', f'#{base_bg + value_label_bg}'

    def should_hide_field(self, is_main, field_type):
        return

    def build_field_context_menu(self, field_name, field_doc, context_menu=None):
        if context_menu is None:
            context_menu = self.Menu()
        # TODO
        return context_menu

    def _bind_field_row_events(self, widget, field_index):
        widget.bind('<Button-1>', lambda e, i=field_index: self.select_field(i))
        widget.bind('<Up>', self.field_press_up)
        widget.bind('<Down>', self.field_press_down)

    def field_press_up(self, _=None):
        if self.field_index_selected != -1:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.field_index_selected)
            self.shift_selected_field(-1)
            if edit_new:
                self._start_field_value_edit(self.field_index_selected)
            if self.field_canvas.yview()[1] != 1.0 or self.field_index_selected < self.displayed_field_count - 5:
                self.field_canvas.yview_scroll(-1, 'units')

    def field_press_down(self, _=None):
        if self.field_index_selected != -1:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.field_index_selected)
            self.shift_selected_field(+1)
            if edit_new:
                self._start_field_value_edit(self.field_index_selected)
            if self.field_canvas.yview()[0] != 0.0 or self.field_index_selected > 5:
                self.field_canvas.yview_scroll(1, 'units')

    def shift_selected_field(self, relative_index):
        if (self.field_index_selected == -1
                or not 0 <= self.field_index_selected + relative_index < self.displayed_field_count):
            return
        self.select_field(self.field_index_selected + relative_index)

    def _start_field_value_edit(self, field_index):
        if not self.e_field_value_edit:
            field_name = self.field_row_boxes[field_index]['field_name']
            self.e_field_value_edit = self.Entry(
                self.field_row_boxes[field_index]['value_box'],
                initial_text=self.param_entry[field_name], sticky='ew', width=5)
            self.e_field_value_edit.bind('<Return>', lambda e, i=field_index: self._confirm_field_value_edit(i))
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

    def _confirm_field_value_edit(self, field_index):
        if self.e_field_value_edit:
            new_value_text = self.e_field_value_edit.var.get()
            self._change_field_value(field_index, new_value_text)
            self.field_row_boxes[field_index]['value_label'].var.set(new_value_text)
            self._cancel_field_value_edit()

    def _change_field_value(self, field_index, new_value):
        # TODO: Cast to proper field type.
        field_name = self.field_row_boxes[field_index]['field_name']
        old_value = self.param_entry[field_name]
        if old_value == new_value:
            return False  # Nothing to change.
        self.param_entry[field_name] = new_value
        return True


class _ParamEntryFrame(SoulstructSmartFrame):
    """Manages param entry selection/modification in editor."""

    ENTRY_CANVAS_BG = '#1d1d1d'
    ENTRY_BOX_WIDTH = 600
    ENTRY_RANGE_SIZE = 50

    def __init__(self, master=None):
        super().__init__(master=master, toplevel=False)

        self.param_table = None  # type: Optional[ParamTable]
        self.entry_row_boxes = []  # type: List[Dict[str, Any]]
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
                    self.field_display = self.SmartFrame(smart_frame_class=_ParamFieldFrame)  # type: _ParamFieldFrame

            with self.set_master(self.f_entry_table):
                self.entry_row_boxes = [self._create_entry_row(row) for row in range(self.ENTRY_RANGE_SIZE)]

            with self.set_master(auto_columns=0):
                self.next_range_button = self.Button(
                    text=f"Next {self.ENTRY_RANGE_SIZE}", bg='#722', width=30, command=self._go_to_next_entry_range,
                    padx=10, pady=20)

    def refresh_field_display(self, reset_display=False):

        if self.entry_index_selected is not None:
            param_id = self.entry_row_boxes[self.entry_index_selected]['param_id']
            param_entry = self.param_table[param_id]
        else:
            param_entry = None
        self.field_display.refresh(param_entry=param_entry, field_info_func=self.param_table.get_field_info,
                                   show_hidden_fields=self.show_hidden_fields.get(), reset_display=reset_display)

    def _create_entry_row(self, row: int) -> dict:
        row_and_id_bg, name_box_bg, name_label_bg = self._get_entry_colors(row)
        row_box = self.Frame(
            width=self.ENTRY_BOX_WIDTH, height=30, bg=row_and_id_bg, row=row, columnspan=2,
            sticky='nsew')
        self._bind_entry_row_events(row_box, row)

        id_label = self.Label(text='', width=15, row=row, column=0, bg=row_and_id_bg, sticky='e')
        self._bind_entry_row_events(id_label, row)

        name_box = self.Frame(row=row, column=1, bg=name_box_bg, sticky='ew')
        self._bind_entry_row_events(name_box, row)

        name_label = self.Label(name_box, text='', bg=name_label_bg, anchor='w', width=60)
        self._bind_entry_row_events(name_label, row)

        # context_menu = self.build_entry_context_menu(param_id)  # TODO: do in refresh, not here?

        return {'row_box': row_box, 'id_label': id_label, 'name_box': name_box,
                'name_label': name_label, 'param_id': -1, 'context_menu': None}

    def refresh(self, param_table: ParamTable = None, reset_fields=False):
        """Display entry information from given ParamTable and current entry display range.

        If no category is given, the last displayed category will be used.
        """
        self._cancel_entry_name_edit()

        if param_table is not None:
            self.param_table = param_table

        if self.param_table != '':
            entries_to_display = self.param_table.get_range(start=self.first_display_index, count=self.ENTRY_RANGE_SIZE)
        else:
            entries_to_display = []  # All rows will be considered 'remaining' and hidden.

        row = 0
        for param_id, param_entry in entries_to_display:
            row_dict = self.entry_row_boxes[row]
            row_and_id_bg, name_box_bg, name_label_bg = self._get_entry_colors(row, param_entry.name)
            row_dict['param_id'] = param_id
            row_dict['row_box'].config(bg=row_and_id_bg)
            row_dict['row_box'].grid()
            row_dict['id_label'].config(bg=row_and_id_bg)
            row_dict['id_label'].var.set(str(param_id))
            row_dict['id_label'].grid()
            row_dict['name_box'].config(bg=name_box_bg)
            row_dict['name_box'].grid()
            row_dict['name_label'].config(bg=name_label_bg)
            row_dict['name_label'].var.set(param_entry.name)
            row_dict['name_label'].grid()
            row += 1

        self.displayed_entry_count = row

        for remaining_row in range(row, self.ENTRY_RANGE_SIZE):
            row_dict = self.entry_row_boxes[remaining_row]
            row_dict['param_id'] = -1
            row_dict['row_box'].grid_remove()
            row_dict['id_label'].grid_remove()
            row_dict['name_box'].grid_remove()
            row_dict['name_label'].grid_remove()

        self.f_entry_table.grid_columnconfigure(1, weight=1)
        self._refresh_buttons()

        self.refresh_field_display(reset_display=reset_fields)

    def select_entry(self, entry_index, set_focus_to_name=True, edit_if_already_selected=True):
        """Select entry from index, based on currently displayed category."""

        old_entry_index = self.entry_index_selected
        self.entry_index_selected = entry_index

        if old_entry_index is not None:
            if entry_index == old_entry_index:
                if edit_if_already_selected:
                    return self._start_entry_name_edit(entry_index)
                return
            self._update_row_colors(old_entry_index)
            reset_field_scrollbar = False
        else:
            reset_field_scrollbar = True

        self._update_row_colors(entry_index)
        if set_focus_to_name:
            self.entry_row_boxes[entry_index]['name_label'].focus_set()
        self.refresh_field_display()
        if reset_field_scrollbar:
            self.update_idletasks()
            self.field_display.field_canvas.yview_moveto(0)

    def _update_row_colors(self, row):
        row_dict = self.entry_row_boxes[row]
        entry_name = self.param_table[self.entry_row_boxes[row]['param_id']].name
        row_and_id_bg, name_box_bg, name_label_bg = self._get_entry_colors(row, entry_name)
        row_dict['row_box'].config(bg=row_and_id_bg)
        row_dict['id_label'].config(bg=row_and_id_bg)
        row_dict['name_box'].config(bg=name_box_bg)
        row_dict['name_label'].config(bg=name_label_bg)

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

    def jump_to_param_id(self, param_id):
        self.first_display_index = self._get_param_index(param_id)
        self.refresh()
        self.select_entry(self.first_display_index, edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)

    def _get_entry_colors(self, row, entry_name=None):
        """Inspects entry data and returns a tuple of 'bg' color values (row_and_id_bg, name_box_bg, name_label_bg)."""
        base_bg = 222
        row_and_id_bg = name_box_bg = name_label_bg = 0
        if entry_name is not None:
            if not entry_name:
                base_bg += 200
            elif not entry_name.strip():
                name_label_bg += 110
        if row == self.entry_index_selected:
            base_bg += 123
        if row % 2:
            base_bg += 111
        return f'#{base_bg + row_and_id_bg}', f'#{base_bg + name_box_bg}', f'#{base_bg + name_label_bg}'

    def build_entry_context_menu(self, param_id, context_menu=None):
        # TODO: Only function I can think of here is 'view uses', which will search for things that link to this
        #  type of param (e.g. other params). Such places should be indexed already so they can be searched.
        category = self.active_category
        if context_menu is None:
            context_menu = self.Menu()

        # TODO

        return context_menu

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
        param_id = self.entry_row_boxes[entry_index]['param_id']
        old_text = self.param_table[param_id].name
        if old_text == new_text:
            return False  # Nothing to change.
        self.param_table[param_id].name = new_text
        self.entry_row_boxes[entry_index]['name_label'].var.set(new_text)
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
        self.refresh()
        self.select_entry(new_index)
        return True

    def _add_relative_entry(self, param_id, offset=1, name=None):
        if name is None:
            name = self.param_table[param_id].name
        self._add_entry(param_id=param_id + offset, name=name)

    def _delete_entry(self, entry_index):
        """Deletes entry and returns it (or False upon failure) so that the action manager can undo the deletion."""
        self._cancel_entry_name_edit()
        param_id = self.entry_row_boxes[entry_index]['param_id']
        return self.param_table.pop(param_id)

    def _bind_entry_row_events(self, widget, entry_index):
        widget.bind('<Button-1>', lambda e, i=entry_index: self.select_entry(i))
        widget.bind('<Up>', self._entry_press_up)
        widget.bind('<Down>', self._entry_press_down)
        widget.bind('<Prior>', lambda e: self._go_to_previous_entry_range())
        widget.bind('<Next>', lambda e: self._go_to_next_entry_range())
        widget.bind('<Button-3>', lambda e, i=entry_index: self._right_click_param_entry(e, i))

    def _update_first_display_index(self, new_index):
        """Updates first display index, ensuring that at least the last ten entries are visible."""
        new_index = min(new_index, len(self.param_table) - 10)
        self.first_display_index = new_index

    def _right_click_param_entry(self, event, entry_index):
        self.select_entry(entry_index, edit_if_already_selected=False)
        self.context_menus[entry_index].tk_popup(event.x_root, event.y_root)

    def _update_range(self, first_index):
        self._update_first_display_index(first_index)
        self.refresh()
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
            param_id = self.entry_row_boxes[entry_index]['param_id']
            self.e_entry_name_edit = self.Entry(
                self.entry_row_boxes[entry_index]['name_box'], initial_text=self.param_table[param_id].name,
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
        if self.entry_index_selected != -1:
            edit_new = self.e_entry_name_edit is not None
            self._confirm_entry_name_edit(self.entry_index_selected)
            self._shift_selected_entry(-1)
            if edit_new:
                self._start_entry_name_edit(self.entry_index_selected)
            if self.entry_canvas.yview()[1] != 1.0 or self.entry_index_selected < self.displayed_entry_count - 5:
                self.entry_canvas.yview_scroll(-1, 'units')

    def _entry_press_down(self, _=None):
        if self.entry_index_selected != -1:
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

    def __init__(self, project: SoulstructProject, master=None, toplevel=False):
        self.Params = project.Params
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct Params")

        self.active_category = 'Players'
        self.category_boxes = {}

        self.param_field_boxes = {}
        self.active_field_name = ''
        self.field_index_selected = -1
        self.e_param_field_edit = None
        self.show_hidden_fields = self.BooleanVar()
        self.displayed_field_count = 0

        self.param_name_edit_active = False
        self.field_value_edit_active = False

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

                    self.entry_display = self.SmartFrame(smart_frame_class=_ParamEntryFrame)  # type: _ParamEntryFrame

        self.entry_display.refresh(self.active_category_param_table)
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

    def select_category(self, selected_category):
        if selected_category == self.active_category:
            return

        self.active_category = selected_category
        for category, (box, label) in self.category_boxes.items():
            if selected_category == category:
                box['bg'] = self.CATEGORY_SELECTED_BG
                label['bg'] = self.CATEGORY_SELECTED_BG
            else:
                box['bg'] = self.STYLE_DEFAULTS['bg']
                label['bg'] = self.STYLE_DEFAULTS['bg']

        self.entry_display.refresh(self.active_category_param_table, reset_fields=True)
        self.entry_display.select_entry(0, edit_if_already_selected=False)
        self.entry_display.entry_canvas.yview_moveto(0)

    @property
    def active_category_param_table(self) -> ParamTable:
        return self.Params[self.active_category]

    @property
    def active_category_sorted_ids(self):
        if self.active_category is None:
            return None
        return sorted(self.Params[self.active_category])

    # def jump_to_category_and_entry(self, category, param_id):
    #     """Simple no-questions-asked navigation. Sets start of visible range to given text ID."""
    #     self.select_category(category, entry_range_start=sorted(self.Params[category]).index(param_id))
    #     self.select_entry(param_id, edit_if_already_selected=False)
    #     self.update_idletasks()
    #     self.entry_canvas.yview_moveto(0)
