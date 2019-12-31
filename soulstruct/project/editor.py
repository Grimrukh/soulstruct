from __future__ import annotations

from abc import ABC
from enum import IntEnum
from typing import List, Optional, TYPE_CHECKING

from soulstruct.project.utilities import ActionHistory, bind_events
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SoulstructSmartFrame, ToolTip

if TYPE_CHECKING:
    from soulstruct.project.links import WindowLinker


class SoulstructBaseEditor(SoulstructSmartFrame, ABC):
    CANVAS_BG = '#1d1d1d'
    CATEGORY_BOX_WIDTH = 250
    CATEGORY_BOX_HEIGHT = 400
    CATEGORY_ROW_HEIGHT = 30
    CATEGORY_ROW_HIGHLIGHT = 1
    CATEGORY_UNSELECTED_BG = '#242424'
    CATEGORY_SELECTED_BG = '#414141'
    ENTRY_CANVAS_BG = '#1d1d1d'
    ENTRY_BOX_WIDTH = 800
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 50

    class EntryRow(object):
        """Container/manager for widgets of a single entry row in the Editor."""
        ENTRY_ANCHOR = 'center'
        ENTRY_ROW_WIDTH = 800
        ENTRY_ROW_HEIGHT = 30
        SHOW_ENTRY_ID = True
        EDIT_ENTRY_ID = True
        ENTRY_ID_WIDTH = 15
        ENTRY_ID_FG = '#CDF'
        ENTRY_TEXT_WIDTH = 60
        ENTRY_TEXT_FG = '#FFF'

        def __init__(self, editor: SoulstructBaseEditor, row_index: int, main_bindings: dict = None):
            self.master = editor
            self.STYLE_DEFAULTS = editor.STYLE_DEFAULTS

            self.row_index = row_index
            self._entry_id = None
            self._entry_text = None
            self._active = False

            bg_color = self._get_color()

            self.row_box = editor.Frame(
                width=self.ENTRY_ROW_WIDTH, height=self.ENTRY_ROW_HEIGHT, bg=bg_color, row=row_index,
                columnspan=2 if self.SHOW_ENTRY_ID else 1, sticky='nsew')
            bind_events(self.row_box, main_bindings)

            if self.SHOW_ENTRY_ID:
                self.id_box = editor.Frame(row=row_index, column=0, bg=bg_color, sticky='ew')
                self.id_label = editor.Label(
                    self.id_box, text='', width=self.ENTRY_ID_WIDTH, bg=bg_color, fg=self.ENTRY_ID_FG, font_size=11,
                    sticky='e')
                if self.EDIT_ENTRY_ID:
                    id_bindings = main_bindings.copy()
                    id_bindings['<Button-1>'] = lambda _, i=row_index: self.master.select_entry_row_index(
                        i, id_clicked=True)
                    id_bindings['<Shift-Button-1>'] = lambda _, i=row_index: self.master.popout_entry_id_edit(i)
                else:
                    id_bindings = main_bindings
                bind_events(self.id_box, id_bindings)
                bind_events(self.id_label, id_bindings)
            else:
                self.id_label = None

            self.text_box = editor.Frame(row=row_index, column=1 if self.SHOW_ENTRY_ID else 0, bg=bg_color, sticky='ew')
            bind_events(self.text_box, main_bindings)

            self.text_label = editor.Label(
                self.text_box, text='', bg=bg_color, fg=self.ENTRY_TEXT_FG, anchor='w', font_size=11,
                justify='left', width=self.ENTRY_TEXT_WIDTH)
            bind_events(self.text_label, main_bindings)

            self.context_menu = editor.Menu(self.row_box)

            self.tool_tip = ToolTip(
                self.row_box, self.id_box, self.id_label, self.text_box, self.text_label, text=None, wraplength=350)

        def update_entry(self, entry_id: int, entry_text: str):
            self.entry_id = entry_id
            self.entry_text = entry_text
            self._update_colors()
            self.build_entry_context_menu()

        def hide(self):
            """Called when this row has no entry to display."""
            self.row_box.grid_remove()
            if self.SHOW_ENTRY_ID:
                self.id_box.grid_remove()
                self.id_label.grid_remove()
            self.text_box.grid_remove()
            self.text_label.grid_remove()

        def unhide(self):
            self.row_box.grid()
            if self.SHOW_ENTRY_ID:
                self.id_box.grid()
                self.id_label.grid()
            self.text_box.grid()
            self.text_label.grid()

        def build_entry_context_menu(self):
            self.context_menu.delete(0, 'end')
            self.context_menu.add_command(
                label="Edit Entry Text in Floating Box (Shift + Click)", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.popout_entry_text_edit(self.row_index))
            self.context_menu.add_command(
                label="Duplicate Entry to Next ID", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.add_relative_entry(self.entry_id, offset=1))
            self.context_menu.add_command(
                label="Delete Entry", foreground=self.STYLE_DEFAULTS['text_fg'],
                command=lambda: self.master.delete_entry(self.row_index))

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

            self._update_colors()

        @property
        def entry_id(self):
            return self._entry_id

        @entry_id.setter
        def entry_id(self, value):
            self._entry_id = value
            if self.SHOW_ENTRY_ID:
                self.id_label.var.set(str(self._entry_id))

        @property
        def entry_text(self):
            return self._entry_text

        @entry_text.setter
        def entry_text(self, value):
            self._entry_text = value
            self.text_label.var.set(self._entry_text)

        def _update_colors(self):
            bg_color = self._get_color()
            for widget in (self.row_box, self.id_box, self.id_label, self.text_box, self.text_label):
                widget['bg'] = bg_color

        def _get_color(self):
            """Inspects entry text/state and assembles a tuple of 'bg' color values."""
            base_bg = int(self.STYLE_DEFAULTS['bg'].lstrip('#'))  # dark grey
            if self._entry_text is not None:
                if not self._entry_text:
                    base_bg += 200  # entry text is empty (red)
                elif not self._entry_text.strip():
                    base_bg += 110  # entry text contains only space (yellow)
            if self._active:
                base_bg += 123  # turquoise boost
            if self.row_index % 2:
                base_bg += 111  # every second row is slightly brighter
            return f'#{base_bg}'

    def __init__(self, linker: WindowLinker, master=None, toplevel=False, window_title="Soulstruct Editor"):
        super().__init__(master=master, toplevel=toplevel, window_title=window_title)
        self.linker = linker
        self.action_history = ActionHistory()
        self.unsaved_changes = set()  # set of changed (category, param_id, action_type) pairs to highlight

        self.active_category = None
        self.category_boxes = {}
        self.category_canvas = None
        self.f_categories = None

        self.entry_rows = []  # type: List[SoulstructBaseEditor.EntryRow]
        self.active_row_index = None
        self.first_display_index = 0
        self.displayed_entry_count = 0

        self.entry_canvas = None
        self.f_entry_table = None
        self.previous_range_button = None
        self.next_range_button = None
        self._e_entry_text_edit = None
        self._e_entry_id_edit = None

        self.build()
        self.bind_all('<Control-z>', self.undo)
        self.bind_all('<Control-y>', self.redo)
        self.refresh_categories()
        self.refresh_entries()

    def build_category_canvas(self):
        self.category_canvas = self.Canvas(
            vertical_scrollbar=True, width=self.CATEGORY_BOX_WIDTH, height=self.CATEGORY_BOX_HEIGHT, padx=5,
            yscrollincrement=self.CATEGORY_ROW_HEIGHT, borderwidth=0, highlightthickness=0)
        self.f_categories = self.Frame(
            self.category_canvas, width=self.CATEGORY_BOX_WIDTH, height=self.CATEGORY_BOX_HEIGHT, sticky='ew')
        self.link_to_scrollable(self.category_canvas, self.f_categories)
        self.category_canvas.create_window(0, 0, window=self.f_categories, anchor='nw')
        self.f_categories.bind(
            "<Configure>", lambda e, c=self.category_canvas: self.reset_canvas_scroll_region(c))

    def build_previous_range_button(self, **kwargs):
        self.previous_range_button = self.Button(
            text=f"Previous {self.ENTRY_RANGE_SIZE}", bg='#111', width=30,
            command=self._go_to_previous_entry_range, padx=10, pady=10, **kwargs)

    def build_next_range_button(self, **kwargs):
        self.next_range_button = self.Button(
            text=f"Next {self.ENTRY_RANGE_SIZE}", bg='#111', width=30,
            command=self._go_to_next_entry_range, padx=10, pady=10, **kwargs)

    def build_entry_frame(self):
        with self.set_master():
            self.entry_canvas = self.Canvas(
                width=self.ENTRY_BOX_WIDTH, height=self.ENTRY_BOX_HEIGHT, borderwidth=0,
                vertical_scrollbar=True, horizontal_scrollbar=True,
                highlightthickness=0, yscrollincrement=self.EntryRow.ENTRY_ROW_HEIGHT, bg=self.ENTRY_CANVAS_BG, padx=5)
            self.f_entry_table = self.Frame(self.entry_canvas, width=self.ENTRY_BOX_WIDTH, sticky='ew')
            self.entry_canvas.create_window(0, 0, window=self.f_entry_table, anchor='nw')
            self.f_entry_table.bind(
                "<Configure>", lambda e, c=self.entry_canvas: self.reset_canvas_scroll_region(c))

        with self.set_master(self.f_entry_table):
            for row in range(self.ENTRY_RANGE_SIZE):
                self.entry_rows.append(self.EntryRow(
                    self, row_index=row, main_bindings={
                        '<Button-1>': lambda _, i=row: self.select_entry_row_index(i),
                        '<Shift-Button-1>': lambda e, i=row: self.popout_entry_text_edit(i),
                        '<Button-3>': lambda e, i=row: self._right_click_entry(e, i),
                        '<Up>': self._entry_press_up,
                        '<Down>': self._entry_press_down,
                        '<Prior>': lambda e: self._go_to_previous_entry_range(),
                        '<Next>': lambda e: self._go_to_next_entry_range(),
                    }))

    def build(self):
        with self.set_master(auto_columns=0):
            self.build_category_canvas()
            with self.set_master(auto_rows=0):
                self.build_previous_range_button()
                with self.set_master():
                    self.build_entry_frame()
                self.build_next_range_button()

    def undo(self, _=None):
        if not self.action_history.undo():
            self['bg'] = '#522'
            self.after(200, lambda: self.config(bg=self.STYLE_DEFAULTS['bg']))

    def redo(self, _=None):
        if not self.action_history.redo():
            self['bg'] = '#522'
            self.after(200, lambda: self.config(bg=self.STYLE_DEFAULTS['bg']))

    def _flash_red_bg(self, widget):
        widget['bg'] = '#522'
        self.after(200, lambda: widget.config(bg=self.STYLE_DEFAULTS['bg']))

    def refresh_categories(self):
        """There are few enough categories that the widgets can be completely regenerated."""
        self.select_category(None)
        for box, label in self.category_boxes.values():
            box.destroy()
            label.destroy()
        self.category_boxes = {}
        with self.set_master(self.f_categories):

            categories = self._get_display_categories()

            for row, category in enumerate(categories):
                box = self.Frame(
                    row=row, width=self.CATEGORY_BOX_WIDTH, height=self.CATEGORY_ROW_HEIGHT,
                    highlightthickness=self.CATEGORY_ROW_HIGHLIGHT,
                    bg=self.CATEGORY_UNSELECTED_BG)
                label_text = camel_case_to_spaces(category).replace('_', ': ')
                label = self.Label(text=label_text, sticky='w', row=row, fg=self._get_category_text_fg(category),
                                   bg=self.CATEGORY_UNSELECTED_BG, padx=1, font_size=10)
                for widget in {label, box}:
                    bind_events(widget, {
                        "<Button-1>": lambda e, c=category: self.select_category(c),
                        '<Up>': self._category_press_up,
                        '<Down>': self._category_press_down,
                        '<Prior>': self._category_press_up,
                        '<Next>': self._category_press_down,
                    })
                if category == self.active_category:
                    label['bg'] = self.CATEGORY_SELECTED_BG
                    box['bg'] = self.CATEGORY_SELECTED_BG
                self.link_to_scrollable(self.category_canvas, box, label)
                self.category_boxes[category] = (box, label)

        self.category_canvas.yview_moveto(0)

    def select_category(self, selected_category: Optional[str], first_display_index=0):
        """Updates `active_category` attribute and row colors.

        By default, resets `first_display_index` to zero.
        Supports 'selected_category=None' to deselect all categories.
        """
        if selected_category != self.active_category:
            self.active_category = selected_category
            for category, (box, label) in self.category_boxes.items():
                if selected_category == category:
                    box['bg'] = self.CATEGORY_SELECTED_BG
                    label['bg'] = self.CATEGORY_SELECTED_BG
                else:
                    box['bg'] = self.CATEGORY_UNSELECTED_BG
                    label['bg'] = self.CATEGORY_UNSELECTED_BG

        self.first_display_index = first_display_index
        self.select_entry_row_index(None, edit_if_already_selected=False)
        self.refresh_entries()
        self.entry_canvas.yview_moveto(0)

    def _shift_selected_category(self, relative_index):
        if self.active_category is None:
            return
        categories = self._get_display_categories()
        active_category_index = categories.index(self.active_category)
        new_index = active_category_index + relative_index
        if 0 <= new_index < len(categories):
            new_category = categories[new_index]
            self.select_category(new_category)
        else:
            return  # Do nothing.

    def _category_press_up(self, _=None):
        if self.active_category is not None:
            categories = self._get_display_categories()
            active_category_index = categories.index(self.active_category)
            self._shift_selected_category(-1)
            if self.category_canvas.yview()[1] != 1.0 or active_category_index < len(categories) - 5:
                self.category_canvas.yview_scroll(-1, 'units')

    def _category_press_down(self, _=None):
        if self.active_category is not None:
            categories = self._get_display_categories()
            active_category_index = categories.index(self.active_category)
            self._shift_selected_category(+1)
            if self.category_canvas.yview()[0] != 0.0 or active_category_index > 5:
                self.category_canvas.yview_scroll(1, 'units')

    @staticmethod
    def _get_category_text_fg(category: str):
        """Returns white text by default; override to add more custom behavior."""
        return '#FFF' if category else '#000'

    def select_entry_id(self, entry_id, set_focus_to_text=True, edit_if_already_selected=True, as_row_index=None):
        """Select entry based on ID and set the category display range to target_row_index rows before it."""
        if as_row_index is None:
            # 5 if no newlines are in the target entry, 0 if there are.
            as_row_index = 0 if '\n' in self.get_entry_text(entry_id) else 5

        entry_index = self.get_entry_index(entry_id)
        row_index = self._update_first_entry_display_index(entry_index, as_row_index)
        self.refresh_entries()
        self.entry_canvas.yview_moveto(0)
        self.select_entry_row_index(
            row_index, set_focus_to_text=set_focus_to_text, edit_if_already_selected=edit_if_already_selected)

    def select_entry_row_index(self, row_index, set_focus_to_text=True, edit_if_already_selected=True,
                               id_clicked=False):
        """Select entry from row index, based on currently displayed category and ID range."""
        old_row_index = self.active_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected:
                    if id_clicked:
                        return self._start_entry_id_edit(row_index)
                    else:
                        return self._start_entry_text_edit(row_index)
                return
        else:
            self._cancel_entry_text_edit()

        self.active_row_index = row_index

        if old_row_index is not None:
            self.entry_rows[old_row_index].active = False
        if row_index is not None:
            self.entry_rows[row_index].active = True
            if set_focus_to_text:
                self.entry_rows[row_index].text_label.focus_set()

    def refresh_entries(self):
        self._cancel_entry_text_edit()

        entries_to_display = self._get_category_name_range(
            first_index=self.first_display_index,
            last_index=self.first_display_index + self.ENTRY_RANGE_SIZE,
        )

        row = 0
        for entry_id, entry in entries_to_display:
            self.entry_rows[row].update_entry(entry_id, self.get_entry_text(entry_id))
            self.entry_rows[row].unhide()
            row += 1

        self.displayed_entry_count = row
        for remaining_row in range(row, self.ENTRY_RANGE_SIZE):
            self.entry_rows[remaining_row].hide()

        self.f_entry_table.grid_columnconfigure(1, weight=1)
        if self.displayed_entry_count == 0:
            self.select_entry_row_index(None)
        self._refresh_buttons()

    def get_category_position_ratio(self, category):
        return list(self.category_boxes).index(category) / (len(self.category_boxes) + 1)

    def get_entry_id(self, row_index: int) -> int:
        """Retrieves true entry ID from the displayed row index (which is relative to first_display_index)."""
        return self.entry_rows[row_index].entry_id

    def _get_display_categories(self):
        raise NotImplementedError

    def get_category_dict(self, category=None):
        raise NotImplementedError

    def _get_category_name_range(self, category=None, first_index=None, last_index=None) -> list:
        raise NotImplementedError

    def get_entry_index(self, entry_id: int, category=None) -> int:
        raise NotImplementedError

    def get_entry_text(self, entry_id: int, category=None) -> str:
        raise NotImplementedError

    def _set_entry_text(self, entry_id: int, text: str, category=None, update_row_index=None):
        raise NotImplementedError

    def _change_entry_text(self, row_index, new_text, category=None):
        """Set text of given entry index in the displayed category (if different from current)."""
        if category is None:
            category = self.active_category
        entry_id = self.get_entry_id(row_index)
        current_text = self.get_entry_text(entry_id, category=category)
        if current_text == new_text:
            return False  # Nothing to change.
        self._set_entry_text(entry_id, new_text, category=category, update_row_index=row_index)

        # TODO: History action manager.
        # if from_history:
        #     self.jump_to_category_and_entry(category, text_id)
        # elif category == self.active_category:
        #     self.refresh_text_entries()
        # self.unsaved_changes.add((self.active_category, text_id, 'change'))
        # if not from_history:
        #     self.action_history.record_action(
        #         undo=partial(self._change_entry, category, text_id, old_text),
        #         redo=partial(self._change_entry, category, text_id, text),
        #     )

        return True

    def _change_entry_id(self, row_index, new_id, category=None):
        """Pop ID from given entry index in the displayed category (if different from current) and reassign."""
        raise NotImplementedError

    def popout_entry_id_edit(self, row_index):
        entry_id = self.get_entry_id(row_index)
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            initial_text = str(entry_id)
            popout_editor = TextEditBox(self, initial_text, allow_newlines=False, window_title="Editing Entry ID")
            new_text = popout_editor.go()
            if new_text is not None:
                try:
                    new_id = int(new_text)
                    if new_id < 0:
                        raise ValueError
                except ValueError:
                    self.dialog("Invalid Entry ID", "Entry ID must be a non-negative integer.")
                    return
                print(new_id)
                self._change_entry_id(row_index, new_id)

    def popout_entry_text_edit(self, entry_index):
        entry_id = self.get_entry_id(entry_index)
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            initial_text = self.get_entry_text(entry_id, self.active_category)
            popout_editor = EntryTextEditBox(self, self.active_category, entry_id, initial_text)
            _, new_text = popout_editor.go()
            if new_text is not None:
                self._change_entry_text(entry_index, new_text)

    def _add_entry(self, entry_id, text, category=None):
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("Cannot add entry without specifying category if 'active_category' is None.")
        if entry_id < 0:
            self.dialog("Entry ID Error", message=f"Entry ID cannot be negative.")
            return False
        if entry_id in self.get_category_dict():
            self.dialog("Text ID Error", message=f"Entry ID {entry_id} already exists in category "
                                                 f"{camel_case_to_spaces(self.active_category)}.")
            return False

        self._cancel_entry_text_edit()
        self._set_entry_text(entry_id, text)
        self.select_entry_id(entry_id, set_focus_to_text=True, edit_if_already_selected=False)

        # TODO
        # if from_history:
        #     self.jump_to_category_and_entry(category, text_id)
        # if not from_history:
        #     self.action_history.record_action(
        #         undo=partial(self._delete_entry, category, text_id),
        #         redo=partial(self._add_entry, category, text_id, text),
        #     )
        # self.unsaved_changes.add((self.active_category, text_id, 'add'))

        return True

    def add_relative_entry(self, entry_id, offset=1, text=None):
        if text is None:
            text = self.get_entry_text(entry_id)  # Copies name of origin entry by default.
        self._add_entry(entry_id=entry_id + offset, text=text)

    def delete_entry(self, row_index, category=None):
        """Deletes entry and returns it (or False upon failure) so that the action manager can undo the deletion."""
        self._cancel_entry_text_edit()
        entry_id = self.get_entry_id(row_index)
        deleted_entry = self.get_category_dict(category=category).pop(entry_id)
        print(deleted_entry)
        self.refresh_entries()

        # TODO
        # if not from_history:
        #     self.action_history.record_action(
        #         undo=partial(self._add_entry, category, text_id, deleted_text),
        #         redo=partial(self._delete_entry, category, text_id),
        #     )
        # self.unsaved_changes.add((self.active_category, text_id, 'delete'))

        return deleted_entry  # TODO: or return False?

    # TODO
    # def bulk_action(self, *category_id_text_action_tuples, jump_to_category, jump_to_text_id, from_history=False):
    #     """Will jump to given category and ID (and refresh) once all actions have been resolved.
    #
    #     Used only by ActionHistory, so 'from_history' argument has no effect.
    #     """
    #     for category, text_id, text, action in category_id_text_action_tuples:
    #         if action in {'add', 'change'}:
    #             self.Text[category][text_id] = text
    #         elif action == 'delete':
    #             self.Text[category].pop(text_id)
    #         else:
    #             raise ValueError(f"Invalid action: {action}. (This is most likely a bug.)")
    #     if from_history:
    #         self.jump_to_category_and_entry(jump_to_category, jump_to_text_id)

    def _update_first_entry_display_index(self, new_entry_index, as_row_index=0):
        """Updates first display index so that 'new_entry_index' becomes displayed index 'as_row_index' (or as close
        to it as possible, for very early entries).

        Returns the resulting displayed row index of new_entry_index (once '.refresh_entries' is called).
        """
        self.first_display_index = max(0, new_entry_index - as_row_index)
        return new_entry_index - self.first_display_index

    def _right_click_entry(self, event, entry_index):
        self.select_entry_row_index(entry_index, edit_if_already_selected=False)
        self.entry_rows[entry_index].context_menu.tk_popup(event.x_root, event.y_root)

    def _update_range(self, first_index):
        delta = first_index - self.first_display_index
        self.first_display_index = first_index
        self.refresh_entries()
        self.select_entry_row_index(0, edit_if_already_selected=False)
        self.update_idletasks()
        self.entry_canvas.yview_moveto(0)
        return delta

    def _go_to_previous_entry_range(self):
        first_index = max(self.first_display_index - self.ENTRY_RANGE_SIZE, 0)
        if first_index == self.first_display_index:
            return
        return self._update_range(first_index)

    def _go_to_next_entry_range(self):
        first_index = min(self.first_display_index + self.ENTRY_RANGE_SIZE,
                          max(len(self.get_category_dict()) - self.ENTRY_RANGE_SIZE, 0))
        if first_index == self.first_display_index:
            return
        return self._update_range(first_index)

    def _start_entry_id_edit(self, row_index):
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            entry_id = self.get_entry_id(row_index)
            initial_text = str(entry_id)
            self._e_entry_id_edit = self.Entry(
                self.entry_rows[row_index].id_box, initial_text=initial_text,
                integers_only=True, sticky='ew', width=self.EntryRow.ENTRY_ID_WIDTH)
            self._e_entry_id_edit.bind('<Return>', lambda e, i=row_index: self._confirm_entry_id_edit(i))
            self._e_entry_id_edit.bind('<Up>', self._entry_press_up)
            self._e_entry_id_edit.bind('<Down>', self._entry_press_down)
            self._e_entry_id_edit.bind('<FocusOut>', lambda e: self._cancel_entry_id_edit())
            self._e_entry_id_edit.bind('<Escape>', lambda e: self._cancel_entry_id_edit())
            self._e_entry_id_edit.focus_set()
            self._e_entry_id_edit.select_range(0, 'end')

    def _cancel_entry_id_edit(self):
        if self._e_entry_id_edit:
            self._e_entry_id_edit.destroy()
            self._e_entry_id_edit = None

    def _confirm_entry_id_edit(self, row_index):
        if self._e_entry_id_edit:
            try:
                new_id = int(self._e_entry_id_edit.var.get())
            except ValueError:
                pass  # shouldn't happen with 'integers_only=True' in Entry
            else:
                self._change_entry_id(row_index, new_id)
            self._cancel_entry_id_edit()

    def _start_entry_text_edit(self, row_index):
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            entry_id = self.get_entry_id(row_index)
            initial_text = self.get_entry_text(entry_id)
            if '\n' in initial_text:
                return self.popout_entry_text_edit(row_index)
            self._e_entry_text_edit = self.Entry(
                self.entry_rows[row_index].text_box, initial_text=initial_text, sticky='ew',
                width=5)
            self._e_entry_text_edit.bind('<Return>', lambda e, i=row_index: self._confirm_entry_text_edit(i))
            self._e_entry_text_edit.bind('<Up>', self._entry_press_up)
            self._e_entry_text_edit.bind('<Down>', self._entry_press_down)
            self._e_entry_text_edit.bind('<FocusOut>', lambda e: self._cancel_entry_text_edit())
            self._e_entry_text_edit.bind('<Escape>', lambda e: self._cancel_entry_text_edit())
            self._e_entry_text_edit.focus_set()
            self._e_entry_text_edit.select_range(0, 'end')

    def _cancel_entry_text_edit(self):
        if self._e_entry_text_edit:
            self._e_entry_text_edit.destroy()
            self._e_entry_text_edit = None

    def _confirm_entry_text_edit(self, row_index):
        if self._e_entry_text_edit:
            new_text = self._e_entry_text_edit.var.get()
            self._change_entry_text(row_index, new_text)
            self._cancel_entry_text_edit()

    def _shift_selected_entry(self, relative_index):
        if self.active_row_index is None:
            return
        new_index = self.active_row_index + relative_index
        if new_index < 0 and self.previous_range_button['state'] == 'normal':
            delta = self._go_to_previous_entry_range()
            new_row_index = -1 - delta
            self.select_entry_row_index(new_row_index, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(new_row_index / (self.ENTRY_RANGE_SIZE + 1))
        elif new_index >= self.displayed_entry_count and self.next_range_button['state'] == 'normal':
            delta = self._go_to_next_entry_range()
            new_row_index = 0 + self.ENTRY_RANGE_SIZE - delta
            self.select_entry_row_index(new_row_index, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(new_row_index / (self.ENTRY_RANGE_SIZE + 1))
        elif 0 <= new_index < self.displayed_entry_count:
            self.select_entry_row_index(self.active_row_index + relative_index)
        else:
            return  # Do nothing.

    def _entry_press_up(self, _=None):
        if self.active_row_index is not None:
            edit_new_text = self._e_entry_text_edit is not None
            edit_new_id = self._e_entry_id_edit is not None
            self._confirm_entry_text_edit(self.active_row_index)
            self._confirm_entry_id_edit(self.active_row_index)
            self._shift_selected_entry(-1)
            if edit_new_text:
                self._start_entry_text_edit(self.active_row_index)
            elif edit_new_id:
                self._start_entry_id_edit(self.active_row_index)
            if self.entry_canvas.yview()[1] != 1.0 or self.active_row_index < self.displayed_entry_count - 5:
                self.entry_canvas.yview_scroll(-1, 'units')

    def _entry_press_down(self, _=None):
        if self.active_row_index is not None:
            edit_new_text = self._e_entry_text_edit is not None
            edit_new_id = self._e_entry_id_edit is not None
            self._confirm_entry_text_edit(self.active_row_index)
            self._confirm_entry_id_edit(self.active_row_index)
            self._shift_selected_entry(+1)
            if edit_new_text:
                self._start_entry_text_edit(self.active_row_index)
            elif edit_new_id:
                self._start_entry_id_edit(self.active_row_index)
            if self.entry_canvas.yview()[0] != 0.0 or self.active_row_index > 5:
                self.entry_canvas.yview_scroll(1, 'units')

    def _refresh_buttons(self):
        if not self.active_category or self.first_display_index == 0:
            self.previous_range_button['state'] = 'disabled'
        else:
            self.previous_range_button['state'] = 'normal'
        if (not self.active_category
                or self.first_display_index >= len(self.get_category_dict()) - self.ENTRY_RANGE_SIZE):
            self.next_range_button['state'] = 'disabled'
        else:
            self.next_range_button['state'] = 'normal'


class TextEditBox(SoulstructSmartFrame):
    """Small pop-out widget that allows you to modify longer strings more freely, with newlines and all."""
    WIDTH = 16  # characters
    HEIGHT = 1  # lines

    def __init__(self, master: SoulstructBaseEditor, initial_text='', allow_newlines=True, window_title="Editing Text"):
        super().__init__(toplevel=True, master=master, window_title=window_title)
        self.editor = master
        self.initial_text = initial_text
        self.output = None
        self.allow_newlines = allow_newlines

        self._text = None

        self.build()

    def build(self):
        with self.set_master(auto_rows=0):
            self._text = self.TextBox(padx=20, pady=20, width=self.WIDTH, height=self.HEIGHT)
            self._text.insert('end', self.initial_text)
            with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={'padx': 10}):
                self.Button(
                    text="Confirm changes", command=lambda: self.done(True), **self.editor.DEFAULT_BUTTON_KWARGS['YES'])
                self.Button(
                    text="Cancel changes", command=lambda: self.done(False), **self.editor.DEFAULT_BUTTON_KWARGS['NO'])

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
            new_text = self._text.get('1.0', 'end' + '-1c')
            if not self.allow_newlines and '\n' in new_text:
                self.editor.dialog("Text Error", "Entry cannot contain newlines.")
                return
            if new_text == self.initial_text:
                self.output = None
            else:
                self.output = self._text.get('1.0', 'end' + '-1c')
        self.quit()


class EntryTextEditBox(TextEditBox):
    WIDTH = 70  # characters
    HEIGHT = 10  # lines

    def __init__(self, master: SoulstructBaseEditor, category, entry_id, initial_text='', allow_newlines=True):
        if entry_id is None:
            window_title = f"Adding entry to {camel_case_to_spaces(category)}"
        else:
            window_title = f"Editing {camel_case_to_spaces(category)}[{entry_id}]"
        self.category = category
        self.entry_id = entry_id
        self._id = None
        super().__init__(master=master, initial_text=initial_text, allow_newlines=allow_newlines,
                         window_title=window_title)

        self.output = [None, None]

    def build(self):
        with self.set_master(auto_rows=0):
            if self.entry_id is None:
                self._id = self.Entry(label='New Entry ID:', label_position='left', width=10, integers_only=True,
                                      padx=20, pady=20).var
            else:
                self._id = None
            super().build()

    def done(self, confirm=True):
        if confirm:
            if self._id:
                if not self._id.get():
                    self.editor.dialog("ID Error", message="New entry ID must be set.")
                    return
                new_id = int(self._id.get())
                if new_id in self.editor.get_category_dict():
                    self.editor.dialog(
                        "ID Error", message=f"Entry ID {new_id} already exists in category "
                                            f"{camel_case_to_spaces(self.category)}.")
                    return
            else:
                new_id = None
            new_text = self._text.get('1.0', 'end' + '-1c')
            if not self.allow_newlines and '\n' in new_text:
                self.editor.dialog("Text Error", "Entry cannot contain newlines.")
                return
            if new_text == self.initial_text:
                self.output = [None, None]
            else:
                self.output = [new_id, self._text.get('1.0', 'end' + '-1c')]
        self.quit()


class SoulstructBaseFieldEditor(SoulstructBaseEditor, ABC):
    FIELD_CANVAS_BG = '#1d1d1d'
    FIELD_BOX_WIDTH = 450
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_HEIGHT = 30
    FIELD_NAME_WIDTH = 30
    FIELD_VALUE_BOX_WIDTH = 200
    FIELD_VALUE_WIDTH = 50
    FIELD_ROW_COUNT = 173  # highest count (Params[SpecialEffects])
    FIELD_NAME_FG = '#DDE'

    class FieldRow(object):
        """Container/manager for widgets in a single field row in the Editor.

        These are only created once, and their contents are refreshed when needed (e.g. when a new entry is selected).
        Unlike entries, field value widgets may be Labels (which turn into Entries for editing), Checkbuttons, or
        Comboboxes. Each of these widgets is created for each row, so they can be hidden/dispalyed when needed by a
        given field type, rather than dynamically creating and destroying them every time a new entry/category is
        selected.
        """
        def __init__(self, editor: SoulstructBaseFieldEditor, row_index: int, main_bindings: dict = None):
            self.master = editor
            self.STYLE_DEFAULTS = editor.STYLE_DEFAULTS

            self.row_index = row_index
            self._active = False
            self.field_name = ''
            self.field_type = None
            self.field_docstring = ""
            self.link_missing = False

            bg_color = self._get_color()

            self.row_box = editor.Frame(
                width=editor.FIELD_BOX_WIDTH, height=editor.FIELD_ROW_HEIGHT, bg=bg_color,
                row=row_index, columnspan=2, sticky='nsew')
            bind_events(self.row_box, main_bindings)

            self.field_name_box = editor.Frame(row=row_index, column=0, bg=bg_color, sticky='w')
            bind_events(self.field_name_box, main_bindings)

            self.field_name_label = editor.Label(
                self.field_name_box, text='', fg=editor.FIELD_NAME_FG, width=editor.FIELD_NAME_WIDTH,
                bg=bg_color, anchor='w')
            bind_events(self.field_name_label, main_bindings)

            self.value_box = editor.Frame(
                width=editor.FIELD_VALUE_BOX_WIDTH, row=row_index, column=1, bg=bg_color, sticky='ew')
            bind_events(self.value_box, main_bindings)

            # VALUE WIDGETS

            self.value_label = editor.Label(
                self.value_box, text='', bg=bg_color, width=editor.FIELD_VALUE_WIDTH, anchor='w')
            bind_events(self.value_label, main_bindings)

            self.value_checkbutton = editor.Checkbutton(
                self.value_box, label=None, bg=bg_color, no_grid=True, selectcolor='#000',
                command=self._checkbutton_toggle)
            bind_events(self.value_checkbutton, main_bindings)  # TODO: why did I disable this?
            # Main focus bindings are not bound to Checkbutton.

            self.value_combobox = editor.Combobox(
                self.value_box, values=None, width=editor.FIELD_VALUE_WIDTH, no_grid=True,
                on_select_function=self._combobox_choice)
            self.value_combobox.bind('<MouseWheel>', lambda _: 'break')  # prevent scrolling on collapsed Combobox
            # Main focus bindings are not bound to Combobox.

            # TODO: BEHAVIOR_REF_TYPE combobox should also force a refresh, as it may change field names.
            #  (Class will need access to ParamEntry for this, which is fine.)

            self.context_menu = editor.Menu(self.row_box)
            self.tool_tip = ToolTip(self.row_box, self.field_name_box, self.field_name_label, text=None)

            self.active_value_widget = self.value_label
            self.hide()  # TODO: still getting white box before I click or scroll

        def _combobox_choice(self, _=None):
            """Updates field value with integer value from Combobox enum or unknown integer."""
            combobox_string = self.value_combobox.var.get()
            if combobox_string.startswith('Unknown: '):
                value = int(combobox_string[len('Unknown: '):])
            else:
                value = getattr(self.field_type, self.value_combobox.var.get().replace(' ', '')).value
            self.master.change_field_value(self.field_name, value)

        def _activate_value_widget(self, widget):
            if id(self.active_value_widget) != id(widget):
                self.active_value_widget.grid_remove()
            self.active_value_widget = widget

        def _checkbutton_toggle(self):
            new_value = self.value_checkbutton.var.get()
            if self.master.change_field_value(self.field_name, new_value):
                self.value_checkbutton.config(fg='#3F3' if new_value else '#F33', text='ON' if new_value else 'OFF')
            else:
                self.value_checkbutton.var.set(not new_value)

        def update_field(self, entry, name, nickname, value, field_type, docstring="DOC-TODO"):
            """Update widgets with given field information."""
            self.field_name = name
            self.field_type = field_type
            self.field_docstring = docstring

            nickname = camel_case_to_spaces(nickname)
            if self.field_name_label.var.get() != nickname:
                self.field_name_label.var.set(nickname)

            if isinstance(self.field_type, str):
                # Note that the *argument* `field_type` is used below, not attribute `self.field_type`.
                field_links = self.master.get_field_links(self.field_type, value)
                field_type = int
            else:
                field_links = []

            if not isinstance(field_type, str) and issubclass(field_type, IntEnum):
                self.value_combobox['values'] = [camel_case_to_spaces(e.name) for e in field_type]
                try:
                    # noinspection PyUnresolvedReferences
                    enum_name = camel_case_to_spaces(field_type(value).name)
                except ValueError:
                    enum_name = f'Unknown: {value}'
                self.value_combobox.var.set(enum_name)
                self._activate_value_widget(self.value_combobox)
            elif field_type in {float, int}:
                value_text = f'{value:.3f}' if field_type == float else str(value)
                if field_links:
                    if len(field_links) > 1:
                        value_text += '    {AMBIGUOUS}'
                    if field_links[0].name is None:
                        value_text += '    {MISSING}'
                    else:
                        value_text += f'    {{{field_links[0].name}}}'
                if self.value_label.var.get() != value_text:
                    self.value_label.var.set(value_text)  # TODO: probably redundant in terms of update efficiency
                self._activate_value_widget(self.value_label)
            elif field_type == bool:
                if value not in {0, 1}:
                    raise ValueError(f"Field with 'bool' type has non-boolean value: {value}")
                self.value_checkbutton.var.set(value)
                self.value_checkbutton.config(fg='#3F3' if value else '#F33', text='ON' if value else 'OFF')
                self._activate_value_widget(self.value_checkbutton)

            if field_links and not any(link.name for link in field_links) and not self.link_missing:
                self.link_missing = True
                self._update_colors()
            elif (not field_links or any(link.name for link in field_links)) and self.link_missing:
                self.link_missing = False
                self._update_colors()

            self.build_field_context_menu(field_links)
            self.tool_tip.text = docstring

            self.unhide()

        def hide(self):
            """Called when this row has no field to display (e.g. for smaller ParamTables or unselected entry)."""
            self.row_box.grid_remove()
            self.field_name_box.grid_remove()
            self.field_name_label.grid_remove()
            self.value_box.grid_remove()
            self.active_value_widget.grid_remove()

        def unhide(self):
            self.row_box.grid()
            self.field_name_box.grid()
            self.field_name_label.grid()
            self.value_box.grid()
            self.active_value_widget.grid()

        def build_field_context_menu(self, field_links=()):
            # TODO: other stuff? Pop out a scroll box to select an entry, for linked fields?
            self.context_menu.delete(0, 'end')
            if field_links:
                for field_link in field_links:
                    field_link.add_to_context_menu(self.context_menu, foreground=self.STYLE_DEFAULTS['text_fg'])

        @property
        def editable(self):
            return self.active_value_widget is self.value_label

        def confirm_edit(self, new_text):
            if not self.editable:
                raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")

            if isinstance(self.field_type, str):
                new_value = int(new_text)
                field_links = self.master.get_field_links(self.field_type, new_value)
                if len(field_links) > 1:
                    new_text += '    {AMBIGUOUS}'
                elif field_links and field_links[0].name is None:
                    new_text += '    {MISSING}'
                elif field_links:
                    new_text += f'    {{{field_links[0].name}}}'
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
            """Inspects field name/data and returns an RGB string."""
            base_bg = int(self.STYLE_DEFAULTS['bg'].lstrip('#'))  # dark grey
            if self.link_missing:
                base_bg += 100
            if self._active:
                base_bg += 123
            if self.row_index % 2:
                base_bg += 111
            return f'#{base_bg}'

    def __init__(self, linker: WindowLinker, master=None, toplevel=False, window_title="Soulstruct Editor"):
        self.show_hidden_fields = None
        self.field_canvas = None
        self.f_field_table = None
        self.e_field_value_edit = None
        self.selected_field_row_index = None
        self.displayed_field_count = 0
        self.field_rows = []  # type: List[SoulstructBaseFieldEditor.FieldRow]
        super().__init__(linker=linker, master=master, toplevel=toplevel, window_title=window_title)

    def build(self):
        """Builds category, entry, and field tables."""
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

    def build_hidden_fields_checkbutton(self, **kwargs):
        self.show_hidden_fields = self.Checkbutton(
            label='Show hidden fields', initial_state=False,
            command=lambda: self.refresh_fields(reset_display=True), pady=10, **kwargs).var

    def build_field_frame(self):
        with self.set_master():
            self.field_canvas = self.Canvas(
                width=self.FIELD_BOX_WIDTH, height=self.FIELD_BOX_HEIGHT, yscrollincrement=self.FIELD_ROW_HEIGHT,
                borderwidth=10, highlightthickness=0, vertical_scrollbar=True, horizontal_scrollbar=True,
                bg=self.FIELD_CANVAS_BG, padx=5)
            self.f_field_table = self.Frame(frame=self.field_canvas, width=self.FIELD_BOX_WIDTH, sticky='ew')
            self.field_canvas.create_window(0, 0, window=self.f_field_table, anchor='nw')
            self.f_field_table.bind(
                "<Configure>", lambda e, c=self.field_canvas: self.reset_canvas_scroll_region(c))

        with self.set_master(self.f_field_table):
            for row in range(self.FIELD_ROW_COUNT):
                self.field_rows.append(self.FieldRow(
                    self, row_index=row,
                    main_bindings={
                        '<Button-1>': lambda _, i=row: self.select_displayed_field_row(i),
                        '<Button-3>': lambda e, i=row: self._right_click_field(e, i),
                        '<Up>': self._field_press_up,
                        '<Down>': self._field_press_down,
                    }))

    def select_category(self, selected_category: Optional[str], first_display_index=0):
        """Updates `active_category` attribute and row colors.

        By default, resets `first_display_index` to zero.
        Supports 'selected_category=None' to deselect all categories.
        """
        if selected_category != self.active_category:
            self.active_category = selected_category
            for category, (box, label) in self.category_boxes.items():
                if selected_category == category:
                    box['bg'] = self.CATEGORY_SELECTED_BG
                    label['bg'] = self.CATEGORY_SELECTED_BG
                    label.focus_set()
                else:
                    box['bg'] = self.CATEGORY_UNSELECTED_BG
                    label['bg'] = self.CATEGORY_UNSELECTED_BG

        self.first_display_index = first_display_index
        self.select_entry_row_index(None, edit_if_already_selected=False)
        self.refresh_entries(reset_field_display=True)
        self.entry_canvas.yview_moveto(0)

    def refresh_entries(self, reset_field_display=False):
        super().refresh_entries()
        self.refresh_fields(reset_display=reset_field_display)

    def select_entry_row_index(self, row_index, set_focus_to_text=True, edit_if_already_selected=True,
                               id_clicked=False):
        super().select_entry_row_index(row_index, set_focus_to_text=set_focus_to_text,
                                       edit_if_already_selected=edit_if_already_selected, id_clicked=id_clicked)
        self.refresh_fields()
        if row_index is not None and set_focus_to_text:
            self.entry_rows[row_index].text_label.focus_set()

    def refresh_fields(self, reset_display=False):
        """Refresh all field information."""
        field_dict = self.get_selected_field_dict()

        self._cancel_field_value_edit()

        show_hidden_fields = self.show_hidden_fields.get()
        field_info_dict = self.get_field_info(field_dict)
        # field_names = self.get_field_names(field_dict)

        row = 0
        for field_name in field_info_dict:

            try:
                field_nickname, is_main, field_type, field_doc = self.get_field_info(field_dict, field_name)
            except ValueError as e:
                raise ValueError(f"Could not get field information for field {field_name}. Error: {str(e)}")

            if (isinstance(field_type, str) and '<Pad:' in field_type) or (not is_main and not show_hidden_fields):
                continue  # Skip hidden field (or always skip Pad field).

            try:
                field_value = field_dict[field_name]
            except KeyError:
                # Only some DSR-specific fields are allowed to be absent.
                if field_doc.startswith("<DSR>"):
                    continue
                raise

            self.field_rows[row].update_field(
                entry=field_dict,
                name=field_name,
                nickname=field_nickname,
                value=field_value,
                field_type=field_type,
                docstring=field_doc,
            )
            row += 1

        self.displayed_field_count = row

        for remaining_row in range(row, self.FIELD_ROW_COUNT):
            self.field_rows[remaining_row].hide()

        self.f_field_table.grid_columnconfigure(1, weight=1)

        if reset_display:
            self.select_displayed_field_row(0, edit_if_already_selected=False)
            self.update_idletasks()
            self.field_canvas.yview_moveto(0)

    def _add_entry(self, entry_id, text, category=None, new_field_dict=None):
        """Requires additional field_dict argument."""
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("Cannot add entry without specifying category if 'active_category' is None.")
        if entry_id < 0:
            self.dialog("Entry ID Error", message=f"Entry ID cannot be negative.")
            return False
        if entry_id in self.get_category_dict():
            self.dialog("Entry ID Error", message=f"Entry ID {entry_id} already exists in category "
                                                  f"{camel_case_to_spaces(self.active_category)}.")
            return False

        self._cancel_entry_text_edit()
        self.get_category_dict()[entry_id] = new_field_dict  # add entry to category dictionary
        self._set_entry_text(entry_id, text)
        self.select_entry_id(entry_id, set_focus_to_text=True, edit_if_already_selected=False)

        # TODO
        # if from_history:
        #     self.jump_to_category_and_entry(category, text_id)
        # if not from_history:
        #     self.action_history.record_action(
        #         undo=partial(self._delete_entry, category, text_id),
        #         redo=partial(self._add_entry, category, text_id, text),
        #     )
        # self.unsaved_changes.add((self.active_category, text_id, 'add'))

        return True

    def add_relative_entry(self, entry_id, offset=1, text=None):
        """Copies field dict of base entry."""
        if text is None:
            text = self.get_entry_text(entry_id)  # Copies name of origin entry by default (can be overridden).
        new_field_dict = self.get_field_dict(entry_id).copy()
        self._add_entry(entry_id=entry_id + offset, text=text, new_field_dict=new_field_dict)

    def _right_click_field(self, event, field_index):
        self.select_displayed_field_row(field_index, edit_if_already_selected=False)
        self.field_rows[field_index].context_menu.tk_popup(event.x_root, event.y_root)

    def select_field_name(self, field_name, set_focus_to_value=True, edit_if_already_selected=False):
        row_index = self.get_field_row_index_from_name(field_name)
        self.select_displayed_field_row(row_index, set_focus_to_value=set_focus_to_value,
                                        edit_if_already_selected=edit_if_already_selected)
        self.refresh_fields()
        self.field_canvas.yview_moveto(0)  # TODO: How to scroll to exact field?

    def select_displayed_field_row(self, row_index, set_focus_to_value=True, edit_if_already_selected=True):
        old_row_index = self.selected_field_row_index

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected and self.field_rows[row_index].editable:
                    return self._start_field_value_edit(row_index)
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

    def _field_press_up(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.selected_field_row_index)
            self._shift_selected_field(-1)
            if edit_new and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[1] != 1.0 or self.selected_field_row_index < self.displayed_field_count - 5:
                self.field_canvas.yview_scroll(-1, 'units')

    def _field_press_down(self, _=None):
        if self.selected_field_row_index is not None:
            edit_new = self.e_field_value_edit is not None
            self._confirm_field_value_edit(self.selected_field_row_index)
            self._shift_selected_field(+1)
            if edit_new and self.field_rows[self.selected_field_row_index].editable:
                self._start_field_value_edit(self.selected_field_row_index)
            if self.field_canvas.yview()[0] != 0.0 or self.selected_field_row_index > 5:
                self.field_canvas.yview_scroll(1, 'units')

    def _shift_selected_field(self, relative_index):
        if (self.selected_field_row_index is None
                or not 0 <= self.selected_field_row_index + relative_index < self.displayed_field_count):
            return
        self.select_displayed_field_row(self.selected_field_row_index + relative_index)

    def _get_field_edit_widget(self, row_index):
        field_row = self.field_rows[row_index]
        if not field_row.editable:
            raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")
        field_type = field_row.field_type
        field_value = self.get_field_dict(self.get_entry_id(self.active_row_index))[field_row.field_name]
        if field_type in {int, float} or isinstance(field_type, str):
            return self.Entry(
                field_row.value_box,
                integers_only=field_type == int,
                numbers_only=field_type == float,
                initial_text=str(field_value),
                sticky='ew', width=5)
        raise TypeError(f"Could not determine editing box from type {field_type}.")

    def _start_field_value_edit(self, row_index):
        if not self.e_field_value_edit:
            self.e_field_value_edit = self._get_field_edit_widget(row_index)
            if not self.e_field_value_edit:
                return  # Edit attempt was rejected.
            self.e_field_value_edit.bind('<Return>', lambda e, i=row_index: self._confirm_field_value_edit(i))
            self.e_field_value_edit.bind('<Up>', self._field_press_up)
            self.e_field_value_edit.bind('<Down>', self._field_press_down)
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
            self.change_field_value(self.field_rows[index].field_name, true_value)
            self._cancel_field_value_edit()

    def change_field_value(self, field_name: str, new_value):
        """New value should have already been converted to its appropriate type."""
        field_dict = self.get_selected_field_dict()
        old_value = field_dict[field_name]
        if old_value == new_value:
            return False  # Nothing to change.
        field_dict[field_name] = new_value
        return True

    def get_field_row_index_from_name(self, field_name):
        for row in self.field_rows:
            if row.field_name == field_name:
                return row.row_index
        raise KeyError(f"Field name {field_name} does not exist in active category/entry.")

    def get_selected_field_dict(self):
        """Returns None if no field is selected."""
        if self.active_row_index is not None:
            entry_id = self.get_entry_id(self.active_row_index)
            return self.get_field_dict(entry_id)
        else:
            return None

    def get_field_dict(self, entry_id: int, category=None):
        raise NotImplementedError

    def get_field_names(self, field_dict):
        raise NotImplementedError

    def get_field_info(self, field_dict, field_name=None):
        """This method should return the full field information dictionary if field_name is None."""
        raise NotImplementedError

    def get_field_links(self, field_type, field_value, special_values=None) -> list:
        raise NotImplementedError


class NameSelectionBox(SoulstructSmartFrame):
    """Small pop-out widget that allows you to select a name from some list."""
    WIDTH = 50  # characters
    HEIGHT = 20  # lines

    def __init__(self, master, names, list_name='List'):
        super().__init__(toplevel=True, master=master, window_title=f"Select Entry from {list_name}")

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
