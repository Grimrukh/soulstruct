from __future__ import annotations
from functools import partial
from typing import Optional, TYPE_CHECKING

from soulstruct.project.actions import ActionHistory
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SoulstructSmartFrame
if TYPE_CHECKING:
    from soulstruct.params.core import ParamEntry, ParamTable
    from soulstruct.project.core import SoulstructProject


class SoulstructParamsEditor(SoulstructSmartFrame):
    CANVAS_BG = '#1d1d1d'
    CATEGORY_BOX_WIDTH = 250
    CATEGORY_SELECTED_BG = '#555'
    ENTRY_BOX_WIDTH = 600
    ENTRY_RANGE_SIZE = 50
    FIELD_BOX_WIDTH = 400

    def __init__(self, project: SoulstructProject, master=None, toplevel=False):
        """
        TODO:
            - Scroll window for field editing.
        """
        self.Params = project.Params
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct Params")

        self.active_category = 'AI'
        self.category_boxes = {}
        self.param_entry_boxes = {}
        self.param_id_selected = -1
        self.e_param_name_edit = None
        self.entry_range_start = 0

        self.param_field_boxes = {}
        self.field_name_selected = ''
        self.e_param_field_edit = None
        self.show_hidden_fields = self.BooleanVar()

        self.edit_active = False  # refers to any edit (entry name or field value)

        self.action_history = ActionHistory()
        self.unsaved_changes = set()  # set of changed (category, param_id, action_type) pairs to highlight

        with self.set_master(auto_columns=0):
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

            with self.set_master(auto_rows=0):
                with self.set_master(auto_columns=0):
                    self.previous_range_button = self.Button(
                        text=f"Previous {self.ENTRY_RANGE_SIZE}", bg='#722', width=30,
                        command=self.previous_param_entry_range, padx=10, pady=20, row=0, sticky='w')
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

                with self.set_master():
                    self.entry_canvas = self.Canvas(scrollbar=True, width=self.ENTRY_BOX_WIDTH, height=500,
                                                    highlightthickness=1, padx=40, pady=40, bg=self.CANVAS_BG)
                    self.f_entry_table = self.Frame(frame=self.entry_canvas, width=self.ENTRY_BOX_WIDTH, sticky='ew')
                    self.entry_canvas.create_window(self.ENTRY_BOX_WIDTH / 2, 250, window=self.f_entry_table,
                                                    anchor='nw')
                    self.f_entry_table.bind(
                        "<Configure>", lambda e, c=self.entry_canvas: self.reset_canvas_scroll_region(c))

                with self.set_master(auto_columns=0):
                    self.next_range_button = self.Button(
                        text=f"Next {self.ENTRY_RANGE_SIZE}", bg='#722', width=30, command=self.next_param_entry_range,
                        padx=10, pady=20)
                    # TODO: restore
                    # self.b_create_new_param = self.Button(
                    #     text="Create New Text ID", bg='#722', width=30, command=self.create_new_param_id,
                    #     padx=10, pady=20)

                self.refresh_param_entries()

            with self.set_master(auto_rows=0):

                with self.set_master():
                    self.field_canvas = self.Canvas(scrollbar=True, width=self.FIELD_BOX_WIDTH, height=500,
                                                    highlightthickness=1, padx=40, pady=40, bg=self.CANVAS_BG)
                    self.f_field_table = self.Frame(frame=self.field_canvas, width=self.ENTRY_BOX_WIDTH, sticky='ew')
                    self.field_canvas.create_window(
                        self.FIELD_BOX_WIDTH / 2, 250, window=self.f_field_table, anchor='nw')
                    self.f_field_table.bind(
                        "<Configure>", lambda e, c=self.field_canvas: self.reset_canvas_scroll_region(c))

                with self.set_master(auto_columns=0):
                    self.show_hidden_fields = self.Checkbutton(
                        label='Show hidden fields', initial_state=False,
                        command=lambda: self.refresh_entry_fields(True), pady=20).var

                self.refresh_entry_fields()

        self._refresh_buttons()
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
            if self.active_category not in categories:
                self.select_category(None)
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
            self.refresh_param_entries()
            return

        self.param_id_selected = -1

        if selected_category is None:
            self.active_category = None
            for widgets in self.param_entry_boxes.values():
                for w in widgets.values():
                    w.destroy()
            return

        self.active_category = selected_category
        for category, (box, label) in self.category_boxes.items():
            if selected_category == category:
                box['bg'] = self.CATEGORY_SELECTED_BG
                label['bg'] = self.CATEGORY_SELECTED_BG
            else:
                box['bg'] = self.STYLE_DEFAULTS['bg']
                label['bg'] = self.STYLE_DEFAULTS['bg']

        self.refresh_param_entries()
        self.refresh_entry_fields()
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)
        self._refresh_buttons()

        print(self.active_category_param_table.param_name)  # TODO

    def get_entry_colors(self, row, param_id, text):
        """Inspects entry data and returns a tuple of 'bg' color values (row_and_id_bg, text_box_bg, text_label_bg)."""
        base_bg = 222
        row_and_id_bg = text_box_bg = text_label_bg = 0
        if not text:
            base_bg += 200
        elif not text.strip():
            text_label_bg += 110
        if param_id == self.param_id_selected:
            base_bg += 123
        if row % 2:
            base_bg += 111
        return f'#{base_bg + row_and_id_bg}', f'#{base_bg + text_box_bg}', f'#{base_bg + text_label_bg}'

    def get_field_colors(self, row, field_name, field_value):
        """Inspects field name/data and returns a tuple of 'bg' color values."""
        base_bg = 222
        row_and_name_bg = value_box_bg = value_label_bg = 0
        if field_value == '':
            base_bg += 200
        if field_name == self.field_name_selected:
            base_bg += 123
        if row % 2:
            base_bg += 111
        return f'#{base_bg + row_and_name_bg}', f'#{base_bg + value_box_bg}', f'#{base_bg + value_label_bg}'

    def refresh_param_entries(self):
        self.cancel_param_name_edit()

        for widgets in self.param_entry_boxes.values():
            for w in widgets.values():
                w.destroy()
        self.param_entry_boxes = {}

        if self.active_category is None:
            return

        with self.set_master(self.f_entry_table):

            text_range = self.Params.get_range(
                self.active_category, self.entry_range_start, self.entry_range_start + self.ENTRY_RANGE_SIZE)

            for row, (param_id, text) in enumerate(text_range):
                self.param_entry_boxes[param_id] = self.build_param_entry_row(row, param_id, text)

        self.f_entry_table.grid_columnconfigure(1, weight=1)
        self._refresh_buttons()

    def build_param_entry_row(self, row, param_id, param_entry):
        """Build widgets for a standard text entry row."""
        row_and_id_bg, text_box_bg, text_label_bg = self.get_entry_colors(row, param_id, param_entry.name)
        row_box = self.Frame(
            width=self.ENTRY_BOX_WIDTH, height=30, bg=row_and_id_bg, row=row, columnspan=2, sticky='nsew')
        self._bind_entry_row_events(row_box, param_id)

        id_label = self.Label(text=str(param_id), width=15, row=row, column=0, bg=row_and_id_bg, sticky='e')
        self._bind_entry_row_events(id_label, param_id)

        text_box = self.Frame(row=row, column=1, bg=text_box_bg, sticky='ew')
        self._bind_entry_row_events(text_box, param_id)

        text_label = self.Label(text_box, text=param_entry.name, bg=text_label_bg, sticky='sw', justify='left')
        self._bind_entry_row_events(text_label, param_id)

        context_menu = self.build_entry_context_menu(param_id)

        return {'row_box': row_box, 'id_label': id_label, 'text_box': text_box,
                'text_label': text_label, 'context_menu': context_menu}
    
    def build_entry_context_menu(self, param_id, context_menu=None):
        # TODO: Only function I can think of here is 'view uses', which will search for things that link to this
        #  type of param (e.g. other params). Such places should be indexed already so they can be searched.
        category = self.active_category
        if context_menu is None:
            context_menu = self.Menu()
            
        # TODO
            
        return context_menu

    def refresh_entry_fields(self, scroll_to_top=False):
        self.cancel_param_name_edit()
        # TODO: cancel field value edit as well.

        for widgets in self.param_field_boxes.values():
            for w in widgets.values():
                w.destroy()
        self.param_field_boxes = {}

        if self.active_param_entry is None:
            return

        with self.set_master(self.f_field_table):
            row = 0
            for field_name in self.active_param_entry.field_names:
                field_nickname, is_main, field_type, field_doc = self.active_category_param_table.field_info.get(
                    field_name, (field_name, True, None, "DOC-TODO"))
                if not is_main and not self.show_hidden_fields.get():
                    continue  # Skip hidden field.
                self.param_field_boxes[field_name] = self.build_param_field_row(
                    row, field_name, field_nickname, field_type, field_doc)
                row += 1

        self.f_field_table.grid_columnconfigure(1, weight=1)
        if scroll_to_top:
            self.field_canvas.yview_moveto(0)

    def build_param_field_row(self, row, field_name, field_nickname, field_type, field_doc):
        """Build widgets for a standard text entry row."""
        value_string = str(self.active_param_entry[field_name])

        row_and_name_bg, value_box_bg, value_label_bg = self.get_field_colors(row, field_name, value_string)
        row_box = self.Frame(
            width=self.FIELD_BOX_WIDTH, height=25, bg=row_and_name_bg, row=row, columnspan=2, sticky='nsew')
        self._bind_field_row_events(row_box, field_name)

        name_box = self.Frame(row=row, column=0, bg=row_and_name_bg, sticky='e')
        self._bind_field_row_events(name_box, field_name)

        name_label = self.Label(name_box, text=camel_case_to_spaces(field_nickname) + ': ',
                                bg=row_and_name_bg, sticky='e', justify='right')
        self._bind_field_row_events(name_label, field_name)

        value_box = self.Frame(
            width=200, row=row, column=1, bg=value_box_bg, sticky='ew')
        self._bind_field_row_events(value_box, field_name)

        value_label = self.Label(value_box, text=value_string, bg=value_label_bg, sticky='sw', justify='left')
        self._bind_field_row_events(value_label, field_name)

        context_menu = self.build_field_context_menu(field_name, field_doc)

        # TODO: store field_type somewhere for casting upon confirmation.

        return {'row_box': row_box, 'name_box': name_box, 'name_label': name_label, 'value_box': value_box,
                'value_label': value_label, 'context_menu': context_menu}

    def build_field_context_menu(self, field_name, field_doc, context_menu=None):
        category = self.active_category
        if context_menu is None:
            context_menu = self.Menu()

        # TODO

        return context_menu

    def _bind_field_row_events(self, widget, field_name):
        widget.bind('<Button-1>', lambda e, f=field_name: self.select_field(f))

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

    def select_entry(self, selected_param_id, set_focus_to_name=True, edit_if_already_selected=True):
        if self.param_id_selected != -1 and selected_param_id == self.param_id_selected:
            if edit_if_already_selected:
                return self.start_entry_edit(selected_param_id)
            return
        else:
            reset_scrollbar = self.param_id_selected == -1

        self.param_id_selected = selected_param_id
        for row, (param_id, widgets) in enumerate(self.param_entry_boxes.items()):
            text = widgets['text_label'].var.get()
            row_and_id_bg, name_box_bg, name_label_bg = self.get_entry_colors(row, param_id, text)
            widgets['row_box']['bg'] = widgets['id_label']['bg'] = row_and_id_bg
            widgets['text_box']['bg'] = name_box_bg
            widgets['text_label']['bg'] = name_label_bg
            if param_id == selected_param_id and set_focus_to_name:
                widgets['text_label'].focus_set()

        self.refresh_entry_fields()

        if reset_scrollbar:
            self.update_idletasks()
            self.field_canvas.yview_moveto(0)

    def select_field(self, field_name_selected, set_focus_to_value=True, edit_if_already_selected=True):
        # TODO: should this start editing immediately (on left click)?
        # TODO: tab while editing moves to next field.
        if self.field_name_selected != '' and field_name_selected == self.field_name_selected:
            if edit_if_already_selected:
                return self.start_field_value_edit(field_name_selected)
            return
        else:
            old_selected_field = self.field_name_selected

        self.field_name_selected = field_name_selected
        for row, (field_name, widgets) in enumerate(self.param_field_boxes.items()):
            if field_name != field_name_selected and field_name != old_selected_field:
                continue
            value_string = str(self.active_param_entry[field_name])  # never read from label directly!
            row_and_name_bg, value_box_bg, value_label_bg = self.get_field_colors(row, field_name, value_string)
            widgets['row_box']['bg'] = widgets['name_box']['bg'] = widgets['name_label']['bg'] = row_and_name_bg
            widgets['value_label']['bg'] = value_label_bg
            widgets['value_box']['bg'] = value_box_bg
            if field_name == field_name_selected and set_focus_to_value:
                widgets['value_label'].focus_set()

    def _change_entry_name(self, category, param_id, text, from_history=False):
        old_text = self.Params[category][param_id].name
        if old_text == text:
            return  # Nothing to change.
        self.Params[category][param_id].name = text
        if from_history:
            self.jump_to_category_and_entry(category, param_id)
        elif category == self.active_category:
            self.refresh_param_entries()
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
            self.refresh_param_entries()
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
            self.refresh_param_entries()
        if not from_history:
            self.action_history.record_action(
                undo=partial(self._add_entry, category, param_id, param_entry),
                redo=partial(self._delete_entry, category, param_id),
            )
        self.unsaved_changes.add((self.active_category, param_id, 'delete'))

    def _bind_entry_row_events(self, widget, param_id):
        widget.bind('<Button-1>', lambda e, i=param_id: self.select_entry(i))
        widget.bind('<Prior>', lambda e: self.previous_param_entry_range())
        widget.bind('<Next>', lambda e: self.next_param_entry_range())
        widget.bind('<Button-3>', lambda e, i=param_id: self._right_click_param_entry(e, i))

    def _right_click_param_entry(self, event, param_id):
        self.select_entry(param_id, edit_if_already_selected=False)
        self.param_entry_boxes[param_id]['context_menu'].tk_popup(event.x_root, event.y_root)

    def previous_param_entry_range(self):
        if self.active_category is None:
            return
        target_start = max(self.entry_range_start - self.ENTRY_RANGE_SIZE, 0)
        if target_start == self.entry_range_start:
            return
        self.entry_range_start = target_start
        self.refresh_param_entries()
        self.select_entry(list(self.param_entry_boxes)[0], edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)

    def next_param_entry_range(self):
        if self.active_category is None:
            return
        target_start = min(max(len(self.active_category_param_table) - self.ENTRY_RANGE_SIZE, 0),
                           self.entry_range_start + self.ENTRY_RANGE_SIZE)
        self.entry_range_start = target_start
        self.refresh_param_entries()
        self.select_entry(list(self.param_entry_boxes)[0], edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)

    def start_entry_edit(self, edited_param_id):
        if not self.edit_active:
            widgets = self.param_entry_boxes[edited_param_id]
            text_box = widgets['text_box']
            label = widgets['text_label']
            label.grid_remove()
            self.e_param_name_edit = self.Entry(text_box, initial_text=label.var.get(), sticky='ew', width=60)
            self.e_param_name_edit.bind('<Return>', lambda e, i=edited_param_id: self.confirm_entry_name_edit(i))
            self.e_param_name_edit.bind('<FocusOut>', lambda e, i=edited_param_id: self.cancel_param_name_edit(i))
            self.e_param_name_edit.bind('<Escape>', lambda e, i=edited_param_id: self.cancel_param_name_edit(i))
            self.e_param_name_edit.focus_set()
            self.e_param_name_edit.select_range(0, 'end')
            self.edit_active = True

    def cancel_param_name_edit(self, edited_param_id=None):
        if self.edit_active:
            if edited_param_id is None:
                edited_param_id = self.param_id_selected
            widgets = self.param_entry_boxes[edited_param_id]
            label = widgets['text_label']
            self.e_param_name_edit.destroy()
            label.grid()
            self.edit_active = False

    def confirm_entry_name_edit(self, edited_param_id):
        if self.edit_active:
            new_text = self.e_param_name_edit.var.get()
            self._change_entry_name(self.active_category, edited_param_id, new_text)
            self.cancel_param_name_edit()

    def start_field_value_edit(self, field_name):
        if not self.edit_active:
            widgets = self.param_field_boxes[field_name]
            value_box = widgets['value_box']
            label = widgets['value_label']
            label.grid_remove()
            self.e_param_field_edit = self.Entry(value_box, initial_text=label.var.get(), sticky='ew', width=60)
            self.e_param_field_edit.bind('<Return>', lambda e, f=field_name: self.confirm_field_value_edit(f))
            self.e_param_field_edit.bind('<FocusOut>', lambda e, f=field_name: self.cancel_field_value_edit(f))
            self.e_param_field_edit.bind('<Escape>', lambda e, f=field_name: self.cancel_field_value_edit(f))
            self.e_param_field_edit.focus_set()
            self.e_param_field_edit.select_range(0, 'end')
            self.edit_active = True

    def cancel_field_value_edit(self, field_name_selected=None):
        if self.edit_active:
            if field_name_selected is None:
                field_name_selected = self.field_name_selected
            widgets = self.param_field_boxes[field_name_selected]
            label = widgets['value_label']
            self.e_param_field_edit.destroy()
            label.grid()
            self.edit_active = False

    def confirm_field_value_edit(self, field_name):
        if self.edit_active:
            new_value_text = self.e_param_field_edit.var.get()
            # TODO: cast string to appropriate type.
            self._change_field_value(self.active_category, self.param_id_selected, field_name, new_value_text)
            self.cancel_field_value_edit(field_name_selected=field_name)

    def _change_field_value(self, category, param_id, field_name, value, from_history=False):
        old_value = self.Params[category][param_id][field_name]
        if old_value == value:
            return  # Nothing to change.
        self.Params[category][param_id][field_name] = value
        if from_history:
            # TODO
            self.jump_to_category_and_entry(category, param_id)
        elif category == self.active_category:
            self.refresh_entry_fields()
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
