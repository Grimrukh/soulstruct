from __future__ import annotations
from functools import partial
from typing import Optional, TYPE_CHECKING

from soulstruct.project.actions import ActionHistory
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SoulstructSmartFrame

if TYPE_CHECKING:
    from soulstruct.params.core import ParamEntry, ParamTable
    from soulstruct.project.core import SoulstructProject


# TODO:
#  Stop creating all of the widgets every time you select something!
#  Create all N sets of widgets once, and when a category is selected, update the ID/text/value labels and point
#    the widget set to a specific param entry ID or field name.


class SoulstructParamsEditor(SoulstructSmartFrame):
    CANVAS_BG = '#1d1d1d'
    CATEGORY_BOX_WIDTH = 200
    CATEGORY_SELECTED_BG = '#555'
    ENTRY_BOX_WIDTH = 600
    ENTRY_RANGE_SIZE = 50
    FIELD_BOX_WIDTH = 500
    FIELD_ROW_COUNT = 150  # TODO: set to max field count
    FIELD_NAME_FG = '#DDE'

    def __init__(self, project: SoulstructProject, master=None, toplevel=False):
        self.Params = project.Params
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct Params")

        self.active_category = 'Humans'
        self.category_boxes = {}
        self.param_id_selected = -1
        self.e_param_name_edit = None
        self.entry_range_start = 0

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
                    scrollbar=True, width=self.CATEGORY_BOX_WIDTH, height=575, padx=40, pady=40,
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
                    self.previous_range_button = self.Button(
                        text=f"Previous {self.ENTRY_RANGE_SIZE}", bg='#722', width=30,
                        command=self.previous_param_entry_range, padx=10, pady=20, row=0, sticky='w')

                    # TODO
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
                        command=lambda: self.refresh_field_values(True), pady=20).var

                with self.set_master(auto_columns=0):

                    with self.set_master():
                        self.entry_canvas = self.Canvas(scrollbar=True, width=self.ENTRY_BOX_WIDTH, height=500,
                                                        highlightthickness=1, padx=40, pady=40, bg=self.CANVAS_BG)
                        self.f_entry_table = self.Frame(
                            frame=self.entry_canvas, width=self.ENTRY_BOX_WIDTH, sticky='ew')
                        self.entry_canvas.create_window(
                            self.ENTRY_BOX_WIDTH / 2, 250, window=self.f_entry_table, anchor='nw')
                        self.f_entry_table.bind(
                            "<Configure>", lambda e, c=self.entry_canvas: self.reset_canvas_scroll_region(c))

                        with self.set_master(self.f_entry_table):
                            self.entry_row_boxes = []
                            for row in range(self.ENTRY_RANGE_SIZE):
                                self.entry_row_boxes.append(self.create_entry_row(row))

                    with self.set_master():
                        self.field_canvas = self.Canvas(scrollbar=True, width=self.FIELD_BOX_WIDTH, height=500,
                                                        yscrollincrement=25, highlightthickness=1,
                                                        padx=40, pady=40, bg=self.CANVAS_BG)
                        self.f_field_table = self.Frame(frame=self.field_canvas, width=self.ENTRY_BOX_WIDTH,
                                                        sticky='ew')
                        self.field_canvas.create_window(
                            self.FIELD_BOX_WIDTH / 2, 250, window=self.f_field_table, anchor='nw')
                        self.f_field_table.bind(
                            "<Configure>", lambda e, c=self.field_canvas: self.reset_canvas_scroll_region(c))

                        with self.set_master(self.f_field_table):
                            self.field_row_boxes = []
                            for row in range(self.FIELD_ROW_COUNT):
                                self.field_row_boxes.append(self.create_field_row(row))

                with self.set_master(auto_columns=0):
                    self.next_range_button = self.Button(
                        text=f"Next {self.ENTRY_RANGE_SIZE}", bg='#722', width=30, command=self.next_param_entry_range,
                        padx=10, pady=20)

                    # TODO
                    # self.b_create_new_param = self.Button(
                    #     text="Create New Text ID", bg='#722', width=30, command=self.create_new_param_id,
                    #     padx=10, pady=20)

        self.refresh_entry_rows()
        self.refresh_field_values()
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

    def select_category(self, selected_category, entry_range_start=0):
        self.cancel_param_name_edit()
        self.entry_range_start = entry_range_start
        if selected_category == self.active_category:
            self.refresh_entry_rows()
            return

        self.param_id_selected = -1

        # TODO: Handle absent category. Hide all entry rows?

        self.active_category = selected_category
        for category, (box, label) in self.category_boxes.items():
            if selected_category == category:
                box['bg'] = self.CATEGORY_SELECTED_BG
                label['bg'] = self.CATEGORY_SELECTED_BG
            else:
                box['bg'] = self.STYLE_DEFAULTS['bg']
                label['bg'] = self.STYLE_DEFAULTS['bg']

        self.refresh_entry_rows()
        self.refresh_field_values()
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)
        self._refresh_buttons()

    def create_entry_row(self, row):
        row_and_id_bg, name_box_bg, name_label_bg = self.get_entry_colors(row)
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

        # context_menu = self.build_entry_context_menu(param_id)  # TODO: do in refresh, not here

        return {'row_box': row_box, 'id_label': id_label, 'name_box': name_box,
                'name_label': name_label, 'param_id': -1, 'context_menu': None}

    def create_field_row(self, row):
        row_and_name_bg, value_box_bg, value_label_bg = self.get_field_colors(row)
        row_box = self.Frame(
            width=self.FIELD_BOX_WIDTH, height=25, bg=row_and_name_bg, row=row, columnspan=2, sticky='nsew')
        self._bind_field_row_events(row_box, row)

        field_name_box = self.Frame(row=row, column=0, bg=row_and_name_bg, sticky='w')
        self._bind_field_row_events(field_name_box, row)

        field_name_label = self.Label(field_name_box, text='', fg=self.FIELD_NAME_FG, bg=row_and_name_bg, anchor='w')
        self._bind_field_row_events(field_name_label, row)

        value_box = self.Frame(width=200, row=row, column=1, bg=value_box_bg, sticky='ew')
        self._bind_field_row_events(value_box, row)

        value_label = self.Label(value_box, text='', bg=value_label_bg, width=10, anchor='w')
        self._bind_field_row_events(value_label, row)

        # context_menu = self.build_field_context_menu(field_name, field_doc)  # TODO

        return {'row_box': row_box, 'field_name_box': field_name_box, 'field_name_label': field_name_label,
                'value_box': value_box, 'value_label': value_label, 'field_name': '', 'context_menu': None}

    def refresh_entry_rows(self):
        self.cancel_param_name_edit()
        self.cancel_field_value_edit()

        if self.active_category is not None:
            text_range = self.Params.get_range(
                self.active_category, self.entry_range_start, self.entry_range_start + self.ENTRY_RANGE_SIZE)
        else:
            text_range = []  # All rows will be considered 'remaining' and hidden.

        row = 0
        for param_id, param_entry in text_range:
            row_dict = self.entry_row_boxes[row]
            row_and_id_bg, name_box_bg, name_label_bg = self.get_entry_colors(row, param_id, param_entry.name)
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

        for remaining_row in range(row, self.ENTRY_RANGE_SIZE):
            row_dict = self.entry_row_boxes[remaining_row]
            row_dict['param_id'] = -1
            row_dict['row_box'].grid_remove()
            row_dict['id_label'].grid_remove()
            row_dict['name_box'].grid_remove()
            row_dict['name_label'].grid_remove()

        self.f_entry_table.grid_columnconfigure(1, weight=1)
        self._refresh_buttons()

    def get_entry_colors(self, row, param_id=None, entry_name=None):
        """Inspects entry data and returns a tuple of 'bg' color values (row_and_id_bg, name_box_bg, name_label_bg)."""
        base_bg = 222
        row_and_id_bg = name_box_bg = name_label_bg = 0
        if entry_name is not None:
            if not entry_name:
                base_bg += 200
            elif not entry_name.strip():
                name_label_bg += 110
        if param_id is not None and param_id == self.param_id_selected:
            base_bg += 123
        if row % 2:
            base_bg += 111
        return f'#{base_bg + row_and_id_bg}', f'#{base_bg + name_box_bg}', f'#{base_bg + name_label_bg}'

    def select_entry(self, entry_index, set_focus_to_name=True, edit_if_already_selected=True):

        selected_param_id = self.entry_row_boxes[entry_index]['param_id']

        if self.param_id_selected != -1 and selected_param_id == self.param_id_selected:
            if edit_if_already_selected:
                return self.start_entry_edit(entry_index)
            return
        else:
            reset_scrollbar = self.param_id_selected == -1

        old_selected_id = self.param_id_selected
        self.param_id_selected = selected_param_id
        for row, row_dict in enumerate(self.entry_row_boxes):
            if row_dict['param_id'] == -1 or row_dict['param_id'] not in {selected_param_id, old_selected_id}:
                continue
            text = row_dict['name_label'].var.get()
            row_and_id_bg, name_box_bg, name_label_bg = self.get_entry_colors(row, row_dict['param_id'], text)
            row_dict['row_box']['bg'] = row_dict['id_label']['bg'] = row_and_id_bg
            row_dict['name_box']['bg'] = name_box_bg
            row_dict['name_label']['bg'] = name_label_bg
            if row_dict['param_id'] == selected_param_id and set_focus_to_name:
                row_dict['name_label'].focus_set()

        self.refresh_field_values()

        if reset_scrollbar:
            self.update_idletasks()
            self.field_canvas.yview_moveto(0)

    def get_field_colors(self, row, field_name=None, field_value=None):
        """Inspects field name/data and returns a tuple of 'bg' color values."""
        base_bg = 222
        row_and_name_bg = value_box_bg = value_label_bg = 0
        if field_value is not None and field_value == '':
            base_bg += 200
        if field_name is not None and field_name == self.active_field_name:
            base_bg += 123
        if row % 2:
            base_bg += 111
        return f'#{base_bg + row_and_name_bg}', f'#{base_bg + value_box_bg}', f'#{base_bg + value_label_bg}'

    def build_entry_context_menu(self, param_id, context_menu=None):
        # TODO: Only function I can think of here is 'view uses', which will search for things that link to this
        #  type of param (e.g. other params). Such places should be indexed already so they can be searched.
        category = self.active_category
        if context_menu is None:
            context_menu = self.Menu()

        # TODO

        return context_menu

    def refresh_field_values(self, scroll_to_top=False):
        self.cancel_param_name_edit()
        self.cancel_field_value_edit()

        try:
            field_names = self.active_param_entry.field_names
        except AttributeError:
            field_names = []  # All rows will be considered 'remaining' and hidden.

        row = 0
        for field_name in field_names:

            # TODO: print utility
            # print(f"        {repr(field_name)}: (\n"
            #       f"            '', True, None,\n"
            #       f"            \"\"),")

            row_dict = self.field_row_boxes[row]
            field_nickname, is_main, field_type, field_doc = self.get_field_info(field_name)  # TODO: use type and doc
            if self.should_hide_field(is_main, field_type):
                continue  # Skip hidden field.

            field_value = str(self.active_param_entry[field_name])

            row_and_name_bg, value_box_bg, value_label_bg = self.get_field_colors(row, field_name, field_value)
            row_dict['field_name'] = field_name
            row_dict['row_box'].config(bg=row_and_name_bg)
            row_dict['row_box'].grid()
            row_dict['field_name_box'].config(bg=row_and_name_bg)
            row_dict['field_name_box'].grid()
            row_dict['field_name_label'].config(bg=row_and_name_bg)
            row_dict['field_name_label'].var.set(camel_case_to_spaces(field_nickname))
            row_dict['field_name_label'].grid()
            row_dict['value_box'].config(bg=value_box_bg)
            row_dict['value_box'].grid()
            row_dict['value_label'].config(bg=value_label_bg)
            row_dict['value_label'].var.set(field_value)
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
        self._refresh_buttons()

        if scroll_to_top:
            self.field_canvas.yview_moveto(0)

    def should_hide_field(self, is_main, field_type):
        return ((isinstance(field_type, str) and 'Pad:' in field_type)
                or (not is_main and not self.show_hidden_fields.get()))

    def build_field_context_menu(self, field_name, field_doc, context_menu=None):
        category = self.active_category
        if context_menu is None:
            context_menu = self.Menu()
        # TODO
        return context_menu

    def _bind_field_row_events(self, widget, field_index):
        widget.bind('<Button-1>', lambda e, f=field_index: self.select_field(f))
        widget.bind('<Up>', self.field_press_up)
        widget.bind('<Down>', self.field_press_down)

    def field_press_up(self, _=None):
        if self.field_index_selected != -1:
            edit_new = self.field_value_edit_active
            self.confirm_field_value_edit(self.field_index_selected)
            self.shift_selected_field(-1)
            if edit_new:
                self.start_field_value_edit(self.field_index_selected)
            if self.field_canvas.yview()[1] != 1.0 or self.field_index_selected < self.displayed_field_count - 5:
                self.field_canvas.yview_scroll(-1, 'units')

    def field_press_down(self, _=None):
        if self.field_index_selected != -1:
            edit_new = self.field_value_edit_active
            self.confirm_field_value_edit(self.field_index_selected)
            self.shift_selected_field(+1)
            if edit_new:
                self.start_field_value_edit(self.field_index_selected)
            if self.field_canvas.yview()[0] != 0.0 or self.field_index_selected > 5:
                self.field_canvas.yview_scroll(1, 'units')

    def shift_selected_field(self, relative_index):
        if (self.field_index_selected == -1
                or not 0 <= self.field_index_selected + relative_index < self.displayed_field_count):
            return
        self.select_field(self.field_index_selected + relative_index)

    def jump_to_category_and_entry(self, category, param_id):
        """Simple no-questions-asked navigation. Sets start of visible range to given text ID."""
        self.select_category(category, entry_range_start=sorted(self.Params[category]).index(param_id))
        self.select_entry(param_id, edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)

    def _refresh_buttons(self):
        # self.b_create_new_param['state'] = 'normal' if self.active_category else 'disabled'  # TODO
        if not self.active_category or self.entry_range_start == 0:
            self.previous_range_button['state'] = 'disabled'
        else:
            self.previous_range_button['state'] = 'normal'
        if (not self.active_category
                or self.entry_range_start > len(self.active_category_param_table) - self.ENTRY_RANGE_SIZE):
            self.next_range_button['state'] = 'disabled'
        else:
            self.next_range_button['state'] = 'normal'

    def deselect_all_entries(self):
        return self.select_entry(-1)

    def select_field(self, field_index, set_focus_to_value=True, edit_if_already_selected=True):
        # TODO: should this start editing immediately (on left click)?
        # TODO: tab while editing moves to next field. Shift+Tab moves back. Up and down arrows also work.
        # TODO: select entire value when editing starts.

        field_name_selected = self.field_row_boxes[field_index]['field_name']

        if self.active_field_name != '' and field_name_selected == self.active_field_name:
            if edit_if_already_selected:
                return self.start_field_value_edit(field_index)
            return
        else:
            old_selected_field = self.active_field_name
            self.cancel_field_value_edit()

        self.active_field_name = field_name_selected
        self.field_index_selected = field_index
        for row, row_dict in enumerate(self.field_row_boxes):
            field_name = row_dict['field_name']
            if field_name == '' or field_name not in {field_name_selected, old_selected_field}:
                continue
            value_string = str(self.active_param_entry[field_name])  # never reads from label directly
            row_and_name_bg, value_box_bg, value_label_bg = self.get_field_colors(row, field_name, value_string)
            row_dict['row_box']['bg'] = row_and_name_bg
            row_dict['field_name_box']['bg'] = row_dict['field_name_label']['bg'] = row_and_name_bg
            row_dict['value_label']['bg'] = value_label_bg
            row_dict['value_box']['bg'] = value_box_bg
            if field_name == field_name_selected and set_focus_to_value:
                row_dict['value_label'].focus_set()

    def _change_entry_name(self, category, param_id, text, from_history=False):
        old_text = self.Params[category][param_id].name
        if old_text == text:
            return  # Nothing to change.
        self.Params[category][param_id].name = text
        if from_history:
            self.jump_to_category_and_entry(category, param_id)
        elif category == self.active_category:
            self.refresh_entry_rows()
        self.unsaved_changes.add((self.active_category, param_id, 'change'))
        if not from_history:
            self.action_history.record_action(
                undo=partial(self._change_entry_name, category, param_id, old_text),
                redo=partial(self._change_entry_name, category, param_id, text),
            )

    def _add_entry(self, category, param_id, text, from_history=False):
        # TODO: Need some kind of default template for each param if this will be allowed - better to duplicate.
        #  Maybe you can indicate what param ID you want to copy, at least.
        if param_id < 0:
            self.dialog("Text ID Error", message=f"Text ID cannot be negative.")
            return
        if param_id in self.Params[category]:
            self.dialog("Text ID Error", message=f"Text ID {param_id} already exists in "
                                                 f"category {camel_case_to_spaces(category)}.")
            return

        self.cancel_param_name_edit()
        self.Params[category][param_id].name = text
        if from_history:
            self.jump_to_category_and_entry(category, param_id)
        elif category == self.active_category:
            self.refresh_entry_rows()
        if not from_history:
            self.action_history.record_action(
                undo=partial(self._delete_entry, category, param_id),
                redo=partial(self._add_entry, category, param_id, text),
            )
        self.unsaved_changes.add((self.active_category, param_id, 'add'))

    def _add_relative_entry(self, category, param_id, offset=1, text=None):
        if text is None:
            text = self.Params[category][param_id]
        self._add_entry(category=category, param_id=param_id + offset, text=text)

    def _delete_entry(self, category, param_id, from_history=False):
        self.cancel_param_name_edit()
        param_entry = self.Params[category].pop(param_id)
        if category == self.active_category:
            self.refresh_entry_rows()
        if not from_history:
            self.action_history.record_action(
                undo=partial(self._add_entry, category, param_id, param_entry),
                redo=partial(self._delete_entry, category, param_id),
            )
        self.unsaved_changes.add((self.active_category, param_id, 'delete'))

    def _bind_entry_row_events(self, widget, entry_index):
        widget.bind('<Button-1>', lambda e, i=entry_index: self.select_entry(i))
        widget.bind('<Prior>', lambda e: self.previous_param_entry_range())
        widget.bind('<Next>', lambda e: self.next_param_entry_range())
        widget.bind('<Button-3>', lambda e, i=entry_index: self._right_click_param_entry(e, i))

    def _right_click_param_entry(self, event, entry_index):
        self.select_entry(entry_index, edit_if_already_selected=False)
        self.context_menus[entry_index].tk_popup(event.x_root, event.y_root)

    def previous_param_entry_range(self):
        if self.active_category is None:
            return
        target_start = max(self.entry_range_start - self.ENTRY_RANGE_SIZE, 0)
        if target_start == self.entry_range_start:
            return
        self.entry_range_start = target_start
        self.refresh_entry_rows()
        self.select_entry(0, edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)

    def next_param_entry_range(self):
        if self.active_category is None:
            return
        target_start = min(max(len(self.active_category_param_table) - self.ENTRY_RANGE_SIZE, 0),
                           self.entry_range_start + self.ENTRY_RANGE_SIZE)
        self.entry_range_start = target_start
        self.refresh_entry_rows()
        self.select_entry(0, edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)

    def start_entry_edit(self, entry_index):
        if not self.param_name_edit_active:
            edited_param_id = self.entry_row_boxes[entry_index]['param_id']
            if edited_param_id == -1:
                print("# WARNING: Invalid entry box was selected somehow.")
                return
            self.e_param_name_edit = self.Entry(
                self.entry_row_boxes[entry_index]['name_box'], initial_text=self.active_param_entry.name,
                sticky='ew', width=60)
            self.e_param_name_edit.bind('<Return>', lambda e, i=edited_param_id: self.confirm_param_name_edit(i))
            self.e_param_name_edit.bind('<FocusOut>', lambda e: self.cancel_param_name_edit())
            self.e_param_name_edit.bind('<Escape>', lambda e: self.cancel_param_name_edit())
            self.e_param_name_edit.focus_set()
            self.e_param_name_edit.select_range(0, 'end')
            self.param_name_edit_active = True

    def cancel_param_name_edit(self):
        if self.param_name_edit_active:
            self.e_param_name_edit.destroy()
            self.param_name_edit_active = False

    def confirm_param_name_edit(self, edited_param_id):
        if self.param_name_edit_active:
            new_text = self.e_param_name_edit.var.get()
            self._change_entry_name(self.active_category, edited_param_id, new_text)
            self.cancel_param_name_edit()

    def start_field_value_edit(self, field_index):
        if not self.field_value_edit_active:
            edited_field_name = self.field_row_boxes[field_index]['field_name']
            self.e_param_field_edit = self.Entry(
                self.field_row_boxes[field_index]['value_box'],
                initial_text=self.active_param_entry[edited_field_name], sticky='ew', width=5)
            self.e_param_field_edit.bind('<Return>', lambda e, i=field_index: self.confirm_field_value_edit(i))
            self.e_param_field_edit.bind('<Up>', self.field_press_up)
            self.e_param_field_edit.bind('<Down>', self.field_press_down)
            self.e_param_field_edit.bind('<FocusOut>', lambda e: self.cancel_field_value_edit())
            self.e_param_field_edit.bind('<Escape>', lambda e: self.cancel_field_value_edit())
            self.e_param_field_edit.focus_set()
            self.e_param_field_edit.select_range(0, 'end')
            self.field_value_edit_active = True

    def cancel_field_value_edit(self):
        if self.field_value_edit_active:
            self.e_param_field_edit.destroy()
            self.field_value_edit_active = False

    def confirm_field_value_edit(self, field_index):
        if self.field_value_edit_active:
            new_value_text = self.e_param_field_edit.var.get()
            # TODO: cast string to appropriate type.
            field_name = self.active_field_name
            self._change_field_value(self.active_category, self.param_id_selected, field_name, new_value_text)
            self.field_row_boxes[field_index]['value_label'].var.set(new_value_text)
            self.cancel_field_value_edit()

    def _change_field_value(self, category, param_id, field_name, value, from_history=False):
        old_value = self.Params[category][param_id][field_name]
        if old_value == value:
            return  # Nothing to change.
        self.Params[category][param_id][field_name] = value
        if from_history:
            # TODO
            self.jump_to_category_and_entry(category, param_id)

        # self.unsaved_changes.add((self.active_category, param_id, 'change'))  # TODO
        # if not from_history:  # TODO
        #     self.action_history.record_action(
        #         undo=partial(self._change_entry_name, category, param_id, old_text),
        #         redo=partial(self._change_entry_name, category, param_id, text),
        #     )

    @property
    def active_category_param_table(self) -> ParamTable:
        return self.Params[self.active_category]

    @property
    def active_category_sorted_ids(self):
        if self.active_category is None:
            return None
        return sorted(self.Params[self.active_category])

    @property
    def active_param_entry(self) -> Optional[ParamEntry]:
        if self.param_id_selected == -1:
            return None
        return self.active_category_param_table[self.param_id_selected]

    def get_field_info(self, field_name) -> tuple:
        return self.active_category_param_table.get_field_info(self.active_param_entry, field_name)
