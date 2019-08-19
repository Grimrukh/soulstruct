from __future__ import annotations
from functools import partial
from typing import TYPE_CHECKING
from soulstruct.project.actions import ActionHistory
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SoulstructSmartFrame
if TYPE_CHECKING:
    from soulstruct.project.core import SoulstructProject


class SoulstructTextEditor(SoulstructSmartFrame):
    CANVAS_BG = '#111'
    CATEGORY_BOX_WIDTH = 250
    CATEGORY_SELECTED_BG = '#555'
    ENTRY_BOX_WIDTH = 800
    ENTRY_RANGE_SIZE = 50

    def __init__(self, project: SoulstructProject, master=None, toplevel=False):
        self.Text = project.Text  # TODO: not storing project yet, but may need to for hyperlinks eventually
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct Text")

        self.active_category = 'NPCNames'
        self.category_boxes = {}
        self.show_all_categories = self.BooleanVar()
        self.text_boxes = {}
        self.text_id_selected = None
        self.inline_edit_active = False
        self.inline_text_edit_entry = None
        self.entry_range_start = 0
        self.action_history = ActionHistory()
        self.unsaved_changes = set()  # set of changed (category, text_id, action_type) pairs to highlight

        # TODO: Detect if sequential entries are +1 to ID and add '+N' to text string, and collapse them. They can
        #  be edited by editing the first one, or you can manually un-collapse them with right click. This shouldn't
        #  be too difficult to implement. Also consider doing this for the upgrade paths (hard-coded knowledge of
        #  their order and ID offsets), though this will be difficult for the abbreviated long names. Leave for now.

        # TODO: Right-click options for 'jump to name/description/summary' for appropriate categories.

        with self.set_master(auto_columns=0):
            with self.set_master(auto_rows=0):
                with self.set_master():
                    self.text_category_canvas = self.Canvas(
                        scrollbar=True, width=self.CATEGORY_BOX_WIDTH, height=575, padx=40, pady=40,
                        highlightthickness=0)
                    self.f_text_categories = self.Frame(width=self.CATEGORY_BOX_WIDTH, height=575, sticky='ew')
                    self.link_to_scrollable(self.text_category_canvas, self.f_text_categories)
                    self.text_category_canvas.create_window(
                        self.CATEGORY_BOX_WIDTH / 2, 300, window=self.f_text_categories, anchor='nw')
                    self.f_text_categories.bind(
                        "<Configure>", lambda e, c=self.text_category_canvas: self.reset_canvas_scroll_region(c))

                    self.refresh_categories()

                self.show_all_categories = self.Checkbutton(label='Show internal categories ', initial_state=False,
                                                            command=self.refresh_categories, pady=20).var

            with self.set_master():
                with self.set_master(row=0, auto_columns=0):
                    self.previous_range_button = self.Button(
                        text=f"Previous {self.ENTRY_RANGE_SIZE}", bg='#722', width=30,
                        command=self.previous_text_range, padx=10, pady=20, row=0, sticky='w')
                    self.find_text_id_entry = self.Entry(
                        label="Find ID:", label_position='left', width=14, padx=10)
                    self.find_text_id_entry.bind('<Return>', lambda e: self.find_text_id())
                    self.find_text_string_entry = self.Entry(
                        label="Find Text:", label_position='left', width=14, padx=10)
                    self.find_text_string_entry.bind('<Return>', lambda e: self.find_text_string())

                with self.set_master(row=1):
                    self.fmg_canvas = self.Canvas(scrollbar=True, width=self.ENTRY_BOX_WIDTH, height=500,
                                                  highlightthickness=1, padx=40, pady=40, bg=self.CANVAS_BG)
                    self.f_fmg_entries = self.Frame(frame=self.fmg_canvas, width=self.ENTRY_BOX_WIDTH, sticky='ew')
                    self.fmg_canvas.create_window(self.ENTRY_BOX_WIDTH / 2, 250, window=self.f_fmg_entries,
                                                  anchor='nw')
                    self.f_fmg_entries.bind(
                        "<Configure>", lambda e, c=self.fmg_canvas: self.reset_canvas_scroll_region(c))

                with self.set_master(row=2, auto_columns=0):
                    self.next_range_button = self.Button(
                        text=f"Next {self.ENTRY_RANGE_SIZE}", bg='#722', width=30, command=self.next_text_range,
                        padx=10, pady=20)
                    self.create_new_text_button = self.Button(
                        text="Create New Text ID", bg='#722', width=30, command=self.create_new_text_id,
                        padx=10, pady=20)

                self.refresh_text_entries()

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
        with self.set_master(self.f_text_categories):
            names = 'all_categories' if self.show_all_categories.get() else 'main_categories'
            categories = getattr(self.Text, names)
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
                self.link_to_scrollable(self.text_category_canvas, box, label)
                self.category_boxes[category] = (box, label)

    def create_new_text_id(self):
        if self.active_category is None:
            return
        floating_edit = _TextEditBox(self, self.active_category, text_id=None)
        new_id, new_text = floating_edit.go()
        if new_id is not None:  # Confirmed text change.
            self.active_category_text_dict[new_id] = new_text
            self.refresh_text_entries()

    def get_text_index(self, category, text_id):
        """Get the index of a given ID in category."""
        if text_id not in self.Text[category]:
            raise ValueError(f"Text ID {text_id} does not appear in category {category}.")
        return list(self.Text[category]).index(text_id)

    def find_text_id(self):
        try:
            id_to_find = int(self.find_text_id_entry.var.get())
            if id_to_find < 0:
                raise ValueError
        except ValueError:
            self.dialog("Value Error", message=f"Invalid text ID: {self.find_text_id_entry.var.get()}.\n\n"
                                               f"The ID must be an integer (zero or greater).",
                        button_kwargs='OK')
            return
        if id_to_find in self.active_category_text_dict:
            self.entry_range_start = self.get_text_index(self.active_category, id_to_find)
            self.refresh_text_entries()
            self.select_entry(id_to_find, edit_if_already_selected=False)
        else:
            self.find_text_id_entry['bg'] = '#522'
            self.after(200, lambda: self.find_text_id_entry.config(bg=self.STYLE_DEFAULTS['bg']))

    def find_text_string(self):
        text = self.find_text_string_entry.var.get()
        text_id_list = list(self.active_category_text_dict)
        first_index = None
        for i, text_id in enumerate(text_id_list):
            if text in self.active_category_text_dict[text_id]:
                if self.text_id_selected is None or i > self.text_id_selected:
                    next_index = i
                    break
                elif first_index is None:
                    first_index = i
        else:
            next_index = first_index

        if next_index is not None:
            self.entry_range_start = next_index
            self.refresh_text_entries()
            self.select_entry(next_index, set_focus_to_text=False, edit_if_already_selected=False)
        else:
            self.find_text_string_entry['bg'] = '#522'
            self.after(200, lambda: self.find_text_string_entry.config(bg=self.STYLE_DEFAULTS['bg']))

    def select_category(self, selected_category):
        if selected_category == self.active_category:
            return  # No change.

        self.cancel_inline_entry_edit()
        self.entry_range_start = 0

        if selected_category is None:
            self.active_category = None
            for widgets in self.text_boxes.values():
                for w in widgets.values():
                    w.destroy()
            return

        self.active_category = selected_category
        for category, (box, label) in self.category_boxes.items():
            if selected_category == category:
                box['bg'] = self.CATEGORY_SELECTED_BG
                label['bg'] = self.CATEGORY_SELECTED_BG
                self.refresh_text_entries()
            else:
                box['bg'] = self.STYLE_DEFAULTS['bg']
                label['bg'] = self.STYLE_DEFAULTS['bg']

        self.update()
        self.fmg_canvas.yview_moveto(0)
        self.previous_range_button['state'] = 'disabled'

        if self.entry_range_start == min(max(
                len(self.active_category_text_dict) - self.ENTRY_RANGE_SIZE, 0),
                self.entry_range_start + self.ENTRY_RANGE_SIZE):
            self.next_range_button['state'] = 'disabled'
        else:
            self.next_range_button['state'] = 'normal'

    def get_entry_colors(self, row, text_id, text):
        """Inspects entry data and returns a tuple of 'bg' color values (row_and_id_bg, text_box_bg, text_label_bg)."""
        base_bg = 222
        row_and_id_bg = text_box_bg = text_label_bg = 0
        if not text:
            base_bg += 200
        elif not text.strip():
            text_label_bg += 110
        if text_id == self.text_id_selected:
            base_bg += 123
        if row % 2:
            base_bg += 111
        return f'#{base_bg + row_and_id_bg}', f'#{base_bg + text_box_bg}', f'#{base_bg + text_label_bg}'

    def refresh_text_entries(self):
        self.cancel_inline_entry_edit()

        for widgets in self.text_boxes.values():
            for w in widgets.values():
                w.destroy()
        self.text_boxes = {}

        if self.active_category is None:
            return

        with self.set_master(self.f_fmg_entries):
            for row, (text_id, text) in enumerate(
                    self.Text.get_range(self.active_category, self.entry_range_start,
                                        self.entry_range_start + self.ENTRY_RANGE_SIZE)):
                row_and_id_bg, text_box_bg, text_label_bg = self.get_entry_colors(row, text_id, text)
                row_box = self.Frame(width=self.ENTRY_BOX_WIDTH, height=30, bg=row_and_id_bg,
                                     row=row, columnspan=2, sticky='nsew')
                self._bind_text_events(row_box, text_id)

                id_label = self.Label(text=str(text_id), width=15, row=row, column=0, bg=row_and_id_bg, sticky='e')
                self._bind_text_events(id_label, text_id)

                text_box = self.Frame(row=row, column=1, bg=text_box_bg, sticky='ew')
                self._bind_text_events(text_box, text_id)

                text_label = self.Label(text_box, text=text, bg=text_label_bg, sticky='sw', justify='left')
                self._bind_text_events(text_label, text_id)

                context_menu = self.Menu()
                context_menu.add_command(
                    label="Edit in Floating Box (shift + click)", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda i=text_id: self.do_popout_entry_edit(i))
                context_menu.add_command(
                    label="Duplicate Entry to Next ID", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda i=text_id: self._add_relative_entry(self.active_category, i, offset=1))
                context_menu.add_command(
                    label="Delete Entry", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda i=text_id: self._delete_entry(self.active_category, i))

                self.text_boxes[text_id] = {'row_box': row_box, 'id_label': id_label, 'text_box': text_box,
                                            'text_label': text_label, 'context_menu': context_menu}
                row += 1

        self.f_fmg_entries.grid_columnconfigure(1, weight=1)
        self._refresh_buttons()

    @property
    def active_category_text_dict(self):
        """Sorted by text ID on retrieval."""
        if self.active_category is None:
            return None
        return {key: self.Text[self.active_category][key] for key in sorted(self.Text[self.active_category])}

    def _refresh_buttons(self):
        self.create_new_text_button['state'] = 'normal' if self.active_category else 'disabled'
        if not self.active_category or self.entry_range_start == 0:
            self.previous_range_button['state'] = 'disabled'
        else:
            self.previous_range_button['state'] = 'normal'
        if (not self.active_category
                or self.entry_range_start > len(self.active_category_text_dict) - self.ENTRY_RANGE_SIZE):
            self.next_range_button['state'] = 'disabled'
        else:
            self.next_range_button['state'] = 'normal'

    def _right_click_text_entry(self, event, text_id):
        self.select_entry(text_id, edit_if_already_selected=False)
        self.text_boxes[text_id]['context_menu'].tk_popup(event.x_root, event.y_root)

    def _change_entry(self, category, text_id, text, record_action=True):
        old_text = self.Text[category][text_id]
        self.Text[category][text_id] = text
        if category == self.active_category:
            self.refresh_text_entries()
        if record_action:
            self.action_history.record_action(
                undo=partial(self._change_entry, category, text_id, old_text),
                redo=partial(self._change_entry, category, text_id, text),
            )

    def _add_entry(self, category, text_id, text, record_action=True):
        if text_id < 0:
            self.dialog("Text ID Error", message=f"Text ID cannot be negative.")
            return
        if text_id in self.Text[category]:
            self.dialog("Text ID Error", message=f"Text ID {text_id} already exists in "
                                                 f"category {camel_case_to_spaces(category)}.")
            return

        self.cancel_inline_entry_edit()
        self.Text[category][text_id] = text
        if category == self.active_category:
            self.refresh_text_entries()
        if record_action:
            self.action_history.record_action(
                undo=partial(self._delete_entry, category, text_id),
                redo=partial(self._add_entry, category, text_id, text),
            )
        self.unsaved_changes.add((self.active_category, text_id, 'add'))

    def _add_relative_entry(self, category, text_id, offset=1, text=None):
        if text is None:
            text = self.Text[category][text_id]
        self._add_entry(category=category, text_id=text_id + offset, text=text)

    def _delete_entry(self, category, text_id, record_action=True):
        self.cancel_inline_entry_edit()
        text = self.Text[category].pop(text_id)
        if category == self.active_category:
            self.refresh_text_entries()
        if record_action:
            self.action_history.record_action(
                undo=partial(self._add_entry, category, text_id, text),
                redo=partial(self._delete_entry, category, text_id),
            )
        self.unsaved_changes.add((self.active_category, text_id, 'delete'))

    def _bind_text_events(self, widget, text_id):
        widget.bind('<Button-1>', lambda e, i=text_id: self.select_entry(i))
        widget.bind('<Shift-Button-1>', lambda e, i=text_id: self.do_popout_entry_edit(i))
        widget.bind('<Prior>', lambda e: self.previous_text_range())
        widget.bind('<Next>', lambda e: self.next_text_range())
        widget.bind('<Button-3>', lambda e, i=text_id: self._right_click_text_entry(e, i))

    def previous_text_range(self):
        if self.active_category is None:
            return
        target_start = max(self.entry_range_start - self.ENTRY_RANGE_SIZE, 0)
        if target_start == self.entry_range_start:
            return
        self.entry_range_start = target_start
        self.refresh_text_entries()
        self.select_entry(list(self.text_boxes)[0], edit_if_already_selected=False)
        self.update_idletasks()
        self.fmg_canvas.yview_moveto(0)

    def next_text_range(self):
        if self.active_category is None:
            return
        target_start = min(max(len(self.active_category_text_dict) - self.ENTRY_RANGE_SIZE, 0),
                           self.entry_range_start + self.ENTRY_RANGE_SIZE)
        self.entry_range_start = target_start
        self.refresh_text_entries()
        self.select_entry(list(self.text_boxes)[0], edit_if_already_selected=False)
        self.update_idletasks()
        self.fmg_canvas.yview_moveto(0)

    def start_inline_entry_edit(self, edited_text_id):
        if not self.inline_edit_active:
            widgets = self.text_boxes[edited_text_id]
            text_box = widgets['text_box']
            label = widgets['text_label']
            if '\n' in label.var.get():
                return self.do_popout_entry_edit(edited_text_id)
            label.grid_remove()
            self.inline_text_edit_entry = self.Entry(text_box, initial_text=label.var.get(), sticky='ew', width=60)
            self.inline_text_edit_entry.bind('<Return>', lambda e, i=edited_text_id: self.confirm_inline_text_edit(i))
            self.inline_text_edit_entry.bind('<FocusOut>', lambda e, i=edited_text_id: self.cancel_inline_entry_edit(i))
            self.inline_text_edit_entry.bind('<Escape>', lambda e, i=edited_text_id: self.cancel_inline_entry_edit(i))
            self.inline_text_edit_entry.focus_set()
            self.inline_edit_active = True

    def cancel_inline_entry_edit(self, edited_text_id=None):
        if self.inline_edit_active:
            if edited_text_id is None:
                edited_text_id = self.text_id_selected
            widgets = self.text_boxes[edited_text_id]
            label = widgets['text_label']
            self.inline_text_edit_entry.destroy()
            label.grid()
            self.inline_edit_active = False

    def confirm_inline_text_edit(self, edited_text_id):
        if self.inline_edit_active:
            new_text = self.inline_text_edit_entry.var.get()
            if self.active_category_text_dict[edited_text_id] != new_text:
                self.unsaved_changes.add((self.active_category, edited_text_id, 'change'))
            self.active_category_text_dict[edited_text_id] = new_text
            widgets = self.text_boxes[edited_text_id]
            label = widgets['text_label']
            self.inline_text_edit_entry.destroy()
            label.var.set(new_text)
            label.grid()
            self.inline_edit_active = False

    def do_popout_entry_edit(self, edited_text_id):
        if not self.inline_edit_active:
            initial_text = self.active_category_text_dict[edited_text_id]
            label = self.text_boxes[edited_text_id]['text_label']
            floating_edit = _TextEditBox(self, self.active_category, edited_text_id, label.var.get())
            _, new_text = floating_edit.go()
            if new_text is not None and new_text != initial_text:  # Confirmed text change.
                self.active_category_text_dict[edited_text_id] = new_text
                self.unsaved_changes.add((self.active_category, edited_text_id, 'change'))
                label.var.set(new_text)

    def deselect_all_entries(self):
        return self.select_entry(-1)

    def select_entry(self, selected_text_id, set_focus_to_text=True, edit_if_already_selected=True):
        # TODO: select multiple IDs by holding Control-Click? Why? For deletion?
        if self.text_id_selected != -1 and selected_text_id == self.text_id_selected:
            if edit_if_already_selected:
                return self.start_inline_entry_edit(selected_text_id)
            return

        self.text_id_selected = selected_text_id
        for row, (text_id, widgets) in enumerate(self.text_boxes.items()):
            text = widgets['text_label'].var.get()
            row_and_id_bg, text_box_bg, text_label_bg = self.get_entry_colors(row, text_id, text)
            widgets['row_box']['bg'] = widgets['id_label']['bg'] = row_and_id_bg
            widgets['text_box']['bg'] = text_box_bg
            widgets['text_label']['bg'] = text_label_bg
            if text_id == selected_text_id and set_focus_to_text:
                widgets['text_label'].focus_set()


class _TextEditBox(SoulstructSmartFrame):
    """Small pop-out widget that allows you to modify longer text more freely, with newlines and all."""

    WIDTH = 50  # characters
    HEIGHT = 10  # lines

    def __init__(self, master: SoulstructTextEditor,
                 text_category, text_id, initial_text=''):
        if text_id is None:
            window_title = f"Adding text entry to {camel_case_to_spaces(text_category)}"
        else:
            window_title = f"Editing {camel_case_to_spaces(text_category)} [{text_id}]"
        self.text_editor = master
        super().__init__(toplevel=True, master=master, window_title=window_title)

        self.initial_text = initial_text
        self.text_category = text_category
        self.output = [None, None]

        self.start_auto_rows()
        if text_id is None:
            self._id = self.Entry(label='New Text ID:', label_position='left', width=10, integers_only=True,
                                  padx=20, pady=20).var
        else:
            self._id = None

        self._text = self.Text(padx=20, pady=20, width=self.WIDTH, height=self.HEIGHT)
        self._text.insert('end', initial_text)
        with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={'padx': 10}):
            self.Button(text="Confirm changes", command=lambda: self.done(True), **master.DEFAULT_BUTTON_KWARGS['YES'])
            self.Button(text="Cancel changes", command=lambda: self.done(False), **master.DEFAULT_BUTTON_KWARGS['NO'])

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
            if self._id:
                if not self._id.get():
                    self.text_editor.dialog("ID Error", message="New text ID must be set.")
                    return
                new_id = int(self._id.get())
                if new_id in self.text_editor.Text[self.text_category]:
                    self.text_editor.dialog("ID Error", message=f"Text ID {new_id} already exists in "
                                                                f"category {camel_case_to_spaces(self.text_category)}.")
                    return
            else:
                new_id = None
            new_text = self._text.get('1.0', 'end' + '-1c')
            if new_text == self.initial_text:
                self.output = [None, None]
            else:
                self.output = [new_id, self._text.get('1.0', 'end' + '-1c')]
        self.quit()
