from __future__ import annotations
from functools import partial
import re
from typing import TYPE_CHECKING
from soulstruct.project.actions import ActionHistory
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SoulstructSmartFrame
if TYPE_CHECKING:
    from soulstruct.project.core import SoulstructProject


class SoulstructTextEditor(SoulstructSmartFrame):
    CANVAS_BG = '#1d1d1d'
    CATEGORY_BOX_WIDTH = 250
    CATEGORY_SELECTED_BG = '#555'
    ENTRY_BOX_WIDTH = 800
    ENTRY_RANGE_SIZE = 50

    _MATCH_ITEM = re.compile(r'^(Weapon|Armor|Ring|Good|Magic)(Names|Summaries|Descriptions)$')

    def __init__(self, project: SoulstructProject, master=None, toplevel=False):
        self._Text = project.Text  # TODO: not storing project yet, but may need to for hyperlinks eventually
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct Text")

        self.active_category = 'NPCNames'
        self.category_boxes = {}
        self.show_all_categories = self.BooleanVar()
        self.text_boxes = {}
        self.text_id_selected = -1
        self.inline_edit_active = False
        self.e_inline_text_edit = None
        self.entry_range_start = 0
        self.action_history = ActionHistory()
        self.unsaved_changes = set()  # set of changed (category, text_id, action_type) pairs to highlight

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
                        label="Find ID:", label_position='left', width=10, padx=10)
                    self.find_text_id_entry.bind('<Return>', lambda e: self.find_text_id())
                    with self.set_master(auto_rows=0):
                        self.find_text_string_entry = self.Entry(
                            label="Find Text:", label_position='left', width=18, padx=10, sticky='e')
                        self.find_text_string_entry.bind('<Return>', lambda e: self.find_text_string())
                        self.replace_text_string_entry = self.Entry(
                            label="Replace With:", label_position='left', width=18, padx=10, sticky='e')
                        self.replace_text_string_entry.bind('<Return>', lambda e: self.find_text_string(replace=True))

                with self.set_master(row=1):
                    self.entry_canvas = self.Canvas(scrollbar=True, width=self.ENTRY_BOX_WIDTH, height=500,
                                                    highlightthickness=1, padx=40, pady=40, bg=self.CANVAS_BG)
                    self.f_entry_table = self.Frame(frame=self.entry_canvas, width=self.ENTRY_BOX_WIDTH, sticky='ew')
                    self.entry_canvas.create_window(self.ENTRY_BOX_WIDTH / 2, 250, window=self.f_entry_table,
                                                    anchor='nw')
                    self.f_entry_table.bind(
                        "<Configure>", lambda e, c=self.entry_canvas: self.reset_canvas_scroll_region(c))

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
            categories = getattr(self._Text, names)
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

    def select_category(self, selected_category, entry_range_start=0):
        self.cancel_inline_entry_edit()
        self.entry_range_start = entry_range_start
        if selected_category == self.active_category:
            self.refresh_text_entries()
            return

        self.text_id_selected = -1

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

        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)
        self._refresh_buttons()

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

        with self.set_master(self.f_entry_table):

            text_range = self._Text.get_range(
                self.active_category, self.entry_range_start, self.entry_range_start + self.ENTRY_RANGE_SIZE)

            for row, (text_id, text) in enumerate(text_range):
                self.text_boxes[text_id] = self.build_entry_row(row, text_id, text)

        self.f_entry_table.grid_columnconfigure(1, weight=1)
        self._refresh_buttons()

    def build_entry_row(self, row, text_id, text):
        """Build widgets for a standard text entry row."""
        row_and_id_bg, text_box_bg, text_label_bg = self.get_entry_colors(row, text_id, text)
        row_box = self.Frame(
            width=self.ENTRY_BOX_WIDTH, height=30, bg=row_and_id_bg, row=row, columnspan=2, sticky='nsew')
        self._bind_text_events(row_box, text_id)

        id_label = self.Label(text=str(text_id), width=15, row=row, column=0, bg=row_and_id_bg, sticky='e')
        self._bind_text_events(id_label, text_id)

        text_box = self.Frame(row=row, column=1, bg=text_box_bg, sticky='ew')
        self._bind_text_events(text_box, text_id)

        text_label = self.Label(text_box, text=text, bg=text_label_bg, sticky='sw', justify='left')
        self._bind_text_events(text_label, text_id)

        context_menu = self.build_entry_context_menu(text_id)

        return {'row_box': row_box, 'id_label': id_label, 'text_box': text_box,
                'text_label': text_label, 'context_menu': context_menu}

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
        if text_id not in self._Text[category]:
            raise ValueError(f"Text ID {text_id} does not appear in category {category}.")
        return sorted(self._Text[category]).index(text_id)

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

    def find_text_string(self, replace=False):
        text = self.find_text_string_entry.var.get()
        text_id_list = self.active_category_sorted_ids
        first_index = None
        for i, text_id in enumerate(text_id_list):
            if text in self.active_category_text_dict[text_id]:
                if text_id > self.text_id_selected:  # also works if text_id_selected == -1
                    next_index = i
                    break
                elif text_id != self.text_id_selected and first_index is None:
                    first_index = i
        else:
            next_index = first_index

        if self.text_id_selected >= 0 and replace and text in self.active_category_text_dict[self.text_id_selected]:
            to_replace = self.replace_text_string_entry.var.get()
            new_text = self.active_category_text_dict[self.text_id_selected].replace(text, to_replace)
            self._change_entry(self.active_category, self.text_id_selected, new_text)

        if next_index is not None:
            self.entry_range_start = next_index
            self.refresh_text_entries()
            selected_id = self.active_category_sorted_ids[next_index]
            self.select_entry(selected_id, set_focus_to_text=False, edit_if_already_selected=False)
        else:
            if replace:
                self.replace_text_string_entry['bg'] = '#522'
                self.after(200, lambda: self.replace_text_string_entry.config(bg=self.STYLE_DEFAULTS['bg']))
            else:
                self.find_text_string_entry['bg'] = '#522'
                self.after(200, lambda: self.find_text_string_entry.config(bg=self.STYLE_DEFAULTS['bg']))

    def build_entry_context_menu(self, text_id, context_menu=None):
        category = self.active_category
        if context_menu is None:
            context_menu = self.Menu()
        context_menu.add_command(
            label="Edit in Floating Box (shift + click)", foreground=self.STYLE_DEFAULTS['text_fg'],
            command=lambda i=text_id: self.do_popout_entry_edit(i))
        context_menu.add_command(
            label="Duplicate Entry to Next ID", foreground=self.STYLE_DEFAULTS['text_fg'],
            command=lambda i=text_id: self._add_relative_entry(category, i, offset=1))
        context_menu.add_command(
            label="Delete Entry", foreground=self.STYLE_DEFAULTS['text_fg'],
            command=lambda i=text_id: self._delete_entry(category, i))

        item_match = self._MATCH_ITEM.match(category)
        if item_match:
            item_type, text_type = item_match.group(1, 2)

            # Category shortcuts.
            separator_added = False
            if text_type in {'Summaries', 'Descriptions'} and text_id in self._Text[item_type + 'Names']:
                if not separator_added:
                    context_menu.add_separator()
                    separator_added = True
                context_menu.add_command(
                    label="Go to Name", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda i=text_id: self.jump_to_category_and_entry(item_type + 'Names', i))
            if text_type in {'Names', 'Descriptions'} and text_id in self._Text[item_type + 'Summaries']:
                if not separator_added:
                    context_menu.add_separator()
                    separator_added = True
                context_menu.add_command(
                    label="Go to Summary", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda i=text_id: self.jump_to_category_and_entry(item_type + 'Summaries', i))
            if text_type in {'Names', 'Summaries'} and text_id in self._Text[item_type + 'Descriptions']:
                if not separator_added:
                    context_menu.add_separator()
                context_menu.add_command(
                    label="Go to Description", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda i=text_id: self.jump_to_category_and_entry(item_type + 'Descriptions', i))

            # Automatic upgrade text generation.
            if item_type == 'Weapon' and text_type == 'Names' and text_id % 100 == 0:
                context_menu.add_separator()
                context_menu.add_command(
                    label="Create weapon upgrade names (+5)", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda c=category, i=text_id: self.create_upgrade_entries(c, i, count=5))
                context_menu.add_command(
                    label="Create weapon upgrade names (+10)", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda c=category, i=text_id: self.create_upgrade_entries(c, i, count=10))
                context_menu.add_command(
                    label="Create weapon upgrade names (+15)", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda c=category, i=text_id: self.create_upgrade_entries(c, i, count=15))

            elif item_type == 'Armor' and text_type == 'Names' and text_id % 100 == 0:
                context_menu.add_separator()
                context_menu.add_command(
                    label="Create armor upgrade names (+5)", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda c=category, i=text_id: self.create_upgrade_entries(c, i, count=5))
                context_menu.add_command(
                    label="Create armor upgrade names (+10)", foreground=self.STYLE_DEFAULTS['text_fg'],
                    command=lambda c=category, i=text_id: self.create_upgrade_entries(c, i, count=10))

        return context_menu

    def create_upgrade_entries(self, category, base_text_id, count):
        if base_text_id % 100:
            self.dialog("Invalid Base ID for Upgrades",
                        message=f"The base text ID for weapons or armor should be a multiple of 100.")
            return
        if any(base_text_id + i in self._Text[category] for i in range(1, count + 1)):
            if self.dialog("Upgrade IDs already exist",
                           message=f"Overwrite all existing entries in ID range "
                                   f"{base_text_id + 1} to {base_text_id + count}?.",
                           button_names=('Yes, overwrite them', 'No, go back'), button_kwargs=('YES', 'NO')) == 1:
                return
        base_text = self._Text[category][base_text_id]
        undo_bulk = []
        redo_bulk = []
        for i in range(1, count + 1):
            new_text = f'{base_text}+{i}'
            if base_text_id + i in self._Text[category]:
                old_text = self._Text[category][base_text_id + i]
                undo_bulk.append((category, base_text_id + i, old_text, 'change'))
                redo_bulk.append((category, base_text_id + i, new_text, 'change'))
            else:
                undo_bulk.append((category, base_text_id + i, None, 'delete'))
                redo_bulk.append((category, base_text_id + i, new_text, 'add'))
            self._Text[category][base_text_id + i] = new_text
        self.action_history.record_action(
            undo=partial(self.bulk_action, *undo_bulk, jump_to_category=category, jump_to_text_id=base_text_id),
            redo=partial(self.bulk_action, *redo_bulk, jump_to_category=category, jump_to_text_id=base_text_id),
        )
        self.refresh_text_entries()

    def jump_to_category_and_entry(self, category, text_id):
        """Simple no-questions-asked navigation. Sets start of visible range to given text ID."""
        self.select_category(category, entry_range_start=sorted(self._Text[category]).index(text_id))
        self.select_entry(text_id, edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)

    def bulk_action(self, *category_id_text_action_tuples, jump_to_category, jump_to_text_id, from_history=False):
        """Will jump to given category and ID (and refresh) once all actions have been resolved.

        Used only by ActionHistory, so 'from_history' argument has no effect.
        """
        for category, text_id, text, action in category_id_text_action_tuples:
            if action in {'add', 'change'}:
                self._Text[category][text_id] = text
            elif action == 'delete':
                self._Text[category].pop(text_id)
            else:
                raise ValueError(f"Invalid action: {action}. (This is most likely a bug.)")
        if from_history:
            self.jump_to_category_and_entry(jump_to_category, jump_to_text_id)

    @property
    def active_category_text_dict(self):
        """Sorted by text ID on retrieval."""
        return self._Text[self.active_category]

    @property
    def active_category_sorted_ids(self):
        if self.active_category is None:
            return None
        return sorted(self._Text[self.active_category])

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

    def _change_entry(self, category, text_id, text, from_history=False):
        old_text = self._Text[category][text_id]
        if old_text == text:
            return  # Nothing to change.
        self._Text[category][text_id] = text
        if from_history:
            self.jump_to_category_and_entry(category, text_id)
        elif category == self.active_category:
            self.refresh_text_entries()
        self.unsaved_changes.add((self.active_category, text_id, 'change'))
        if not from_history:
            self.action_history.record_action(
                undo=partial(self._change_entry, category, text_id, old_text),
                redo=partial(self._change_entry, category, text_id, text),
            )

    def _add_entry(self, category, text_id, text, from_history=False):
        if text_id < 0:
            self.dialog("Text ID Error", message=f"Text ID cannot be negative.")
            return
        if text_id in self._Text[category]:
            self.dialog("Text ID Error", message=f"Text ID {text_id} already exists in "
                                                 f"category {camel_case_to_spaces(category)}.")
            return

        self.cancel_inline_entry_edit()
        self._Text[category][text_id] = text
        if from_history:
            self.jump_to_category_and_entry(category, text_id)
        elif category == self.active_category:
            self.refresh_text_entries()
        if not from_history:
            self.action_history.record_action(
                undo=partial(self._delete_entry, category, text_id),
                redo=partial(self._add_entry, category, text_id, text),
            )
        self.unsaved_changes.add((self.active_category, text_id, 'add'))

    def _add_relative_entry(self, category, text_id, offset=1, text=None):
        if text is None:
            text = self._Text[category][text_id]
        self._add_entry(category=category, text_id=text_id + offset, text=text)

    def _delete_entry(self, category, text_id, from_history=False):
        self.cancel_inline_entry_edit()
        text = self._Text[category].pop(text_id)
        if category == self.active_category:
            self.refresh_text_entries()
        if not from_history:
            self.action_history.record_action(
                undo=partial(self._add_entry, category, text_id, text),
                redo=partial(self._delete_entry, category, text_id),
            )
        self.unsaved_changes.add((self.active_category, text_id, 'delete'))

    def _bind_text_events(self, widget, text_id):
        widget.bind('<Button-1>', lambda e, i=text_id: self.select_entry(i))
        widget.bind('<Shift-Button-1>', lambda e, i=text_id: self.select_entry(i, popout=True))
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
        self.entry_canvas.yview_moveto(0)

    def next_text_range(self):
        if self.active_category is None:
            return
        target_start = min(max(len(self.active_category_text_dict) - self.ENTRY_RANGE_SIZE, 0),
                           self.entry_range_start + self.ENTRY_RANGE_SIZE)
        self.entry_range_start = target_start
        self.refresh_text_entries()
        self.select_entry(list(self.text_boxes)[0], edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)

    def start_inline_entry_edit(self, edited_text_id):
        if not self.inline_edit_active:
            widgets = self.text_boxes[edited_text_id]
            text_box = widgets['text_box']
            label = widgets['text_label']
            if '\n' in label.var.get():
                return self.do_popout_entry_edit(edited_text_id)
            label.grid_remove()
            self.e_inline_text_edit = self.Entry(text_box, initial_text=label.var.get(), sticky='ew', width=60)
            self.e_inline_text_edit.bind('<Return>', lambda e, i=edited_text_id: self.confirm_inline_text_edit(i))
            self.e_inline_text_edit.bind('<FocusOut>', lambda e, i=edited_text_id: self.cancel_inline_entry_edit(i))
            self.e_inline_text_edit.bind('<Escape>', lambda e, i=edited_text_id: self.cancel_inline_entry_edit(i))
            self.e_inline_text_edit.focus_set()
            self.e_inline_text_edit.select_range(0, 'end')
            self.inline_edit_active = True

    def cancel_inline_entry_edit(self, edited_text_id=None):
        if self.inline_edit_active:
            if edited_text_id is None:
                edited_text_id = self.text_id_selected
            widgets = self.text_boxes[edited_text_id]
            label = widgets['text_label']
            self.e_inline_text_edit.destroy()
            label.grid()
            self.inline_edit_active = False

    def confirm_inline_text_edit(self, edited_text_id):
        if self.inline_edit_active:
            new_text = self.e_inline_text_edit.var.get()
            self._change_entry(self.active_category, edited_text_id, new_text)
            self.cancel_inline_entry_edit()

    def do_popout_entry_edit(self, edited_text_id):
        if not self.inline_edit_active:
            initial_text = self.active_category_text_dict[edited_text_id]
            popout_editor = _TextEditBox(self, self.active_category, edited_text_id, initial_text)
            _, new_text = popout_editor.go()
            if new_text is not None:
                self._change_entry(self.active_category, edited_text_id, new_text)

    def deselect_all_entries(self):
        return self.select_entry(-1)

    def select_entry(self, selected_text_id, set_focus_to_text=True, edit_if_already_selected=True, popout=False):
        # TODO: select multiple IDs by holding Control-Click? Why? For deletion?
        if self.text_id_selected != -1 and selected_text_id == self.text_id_selected:
            if edit_if_already_selected:
                if popout:
                    return self.do_popout_entry_edit(selected_text_id)
                return self.start_inline_entry_edit(selected_text_id)
            return
        else:
            old_text_id = self.text_id_selected

        self.text_id_selected = selected_text_id
        for row, (text_id, widgets) in enumerate(self.text_boxes.items()):
            if text_id != selected_text_id and text_id != old_text_id:
                continue
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
