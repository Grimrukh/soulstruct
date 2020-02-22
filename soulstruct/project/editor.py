from __future__ import annotations

import logging
from abc import ABC
from enum import IntEnum
from functools import partial
from typing import List, Optional, TYPE_CHECKING

from soulstruct.project.utilities import ActionHistory, ViewHistory, bind_events, EntryTextEditBox
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SmartFrame, ToolTip

if TYPE_CHECKING:
    from soulstruct.project.links import WindowLinker

_LOGGER = logging.getLogger(__name__)


class SoulstructBaseEditor(SmartFrame, ABC):
    DATA_NAME = ""
    TAB_NAME = ""
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
        ENTRY_ROW_HEIGHT = 30
        SHOW_ENTRY_ID = True
        EDIT_ENTRY_ID = True
        ENTRY_ID_WIDTH = 15
        ENTRY_ID_FG = '#CDF'
        ENTRY_TEXT_WIDTH = 150
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
                width=self.ENTRY_ID_WIDTH + self.ENTRY_TEXT_WIDTH, height=self.ENTRY_ROW_HEIGHT, bg=bg_color,
                row=row_index, columnspan=2 if self.SHOW_ENTRY_ID else 1, sticky='nsew')
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
        self.view_history = ViewHistory()
        self.category_selected_entry_id = {}  # maps categories to their currently selected entry IDs
        self.unsaved_changes = set()  # set of changed (category, param_id, action_type) pairs to highlight

        self.map_choice = None  # Combobox used by most tabs.

        self.active_category = None
        self.category_boxes = {}
        self.category_canvas = None
        self.category_i_frame = None

        self.entry_rows = []  # type: List[SoulstructBaseEditor.EntryRow]
        self.active_row_index = None
        self.first_display_index = 0
        self.displayed_entry_count = 0

        self.entry_canvas = None
        self.entry_i_frame = None
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
        with self.set_master(sticky='nsew', row_weights=[1], column_weights=[1], auto_columns=0):
            self.category_canvas = self.Canvas(
                vertical_scrollbar=True, yscrollincrement=self.CATEGORY_ROW_HEIGHT,
                width=self.CATEGORY_BOX_WIDTH, height=self.CATEGORY_BOX_HEIGHT,
                borderwidth=0, highlightthickness=0, sticky='nsew')
        with self.set_master(self.category_canvas):
            self.category_i_frame = self.Frame(sticky='nsew')
        self.link_to_scrollable(self.category_canvas, self.category_i_frame)
        self.category_canvas.create_window(0, 0, window=self.category_i_frame, anchor='n')
        self.category_i_frame.bind("<Configure>", lambda e, c=self.category_canvas: self.reset_canvas_scroll_region(c))

    def build_previous_range_button(self, **kwargs):
        self.previous_range_button = self.Button(
            text=f"Previous {self.ENTRY_RANGE_SIZE}", font_size=10, bg='#111', width=30,
            command=self._go_to_previous_entry_range, padx=10, pady=10, **kwargs)

    def build_next_range_button(self, **kwargs):
        self.next_range_button = self.Button(
            text=f"Next {self.ENTRY_RANGE_SIZE}", font_size=10, bg='#111', width=30,
            command=self._go_to_next_entry_range, padx=10, pady=10, **kwargs)

    def build_entry_frame(self):
        """Master should already be set."""
        self.entry_canvas = self.Canvas(
            width=self.ENTRY_BOX_WIDTH, height=self.ENTRY_BOX_HEIGHT, borderwidth=0,
            vertical_scrollbar=True, horizontal_scrollbar=True, sticky='nsew',
            highlightthickness=0, yscrollincrement=self.EntryRow.ENTRY_ROW_HEIGHT, bg=self.ENTRY_CANVAS_BG,
            row_weights=[1], column_weights=[1])
        self.entry_i_frame = self.Frame(frame=self.entry_canvas, sticky='ew', column_weights=[1, 1])
        self.entry_i_frame.bind("<Configure>", lambda e, c=self.entry_canvas: self.reset_canvas_scroll_region(c))
        self.entry_canvas.create_window(0, 0, window=self.entry_i_frame, anchor='nw')

        with self.set_master(self.entry_i_frame):
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
        with self.set_master(sticky='nsew', row_weights=[1], column_weights=[0, 1], auto_columns=0):
            self.build_category_canvas()
            with self.set_master(sticky='nsew', row_weights=[0, 1, 0], column_weights=[1], auto_rows=0):
                self.build_previous_range_button()
                with self.set_master(sticky='nsew', row_weights=[1], column_weights=[1]):
                    self.build_entry_frame()
                self.build_next_range_button()

    def undo(self, _=None):
        if not self.action_history.undo():
            # TODO: flash undo button red to indicate there's nothing to undo.
            pass

    def redo(self, _=None):
        if not self.action_history.redo():
            # TODO: flash redo button red to indicate there's nothing to undo.
            pass

    @property
    def map_choice_id(self):
        if self.map_choice is None:
            raise AttributeError("Tried to get map choice ID in a tab that does not have map choice.")
        return self.map_choice.var.get().split(' [')[0]

    # ---------------------- #
    #   CATEGORY SELECTION   #
    # ---------------------- #

    def select_category(self, selected_category: Optional[str], first_display_index=0, auto_scroll=False,
                        view_change=False):
        """Updates `active_category` attribute and row colors.

        By default, resets `first_display_index` to zero.
        Supports 'selected_category=None' to deselect all categories.
        Optionally recorded as a view change (e.g. from manually clicking the category).
        """
        old_category = self.active_category

        if old_category is not None:
            selected_entry_id = self.get_entry_id(self.active_row_index) if self.active_row_index else None
            self.category_selected_entry_id[old_category] = selected_entry_id

        if selected_category != self.active_category:
            self.active_category = selected_category
            for category, (box, label) in self.category_boxes.items():
                if selected_category == category:
                    box['bg'] = self.CATEGORY_SELECTED_BG
                    label['bg'] = self.CATEGORY_SELECTED_BG
                else:
                    box['bg'] = self.CATEGORY_UNSELECTED_BG
                    label['bg'] = self.CATEGORY_UNSELECTED_BG

        if auto_scroll:
            view_ratio = list(self.category_boxes).index(self.active_category) / (len(self.category_boxes) + 1)
            self.category_canvas.yview_moveto(view_ratio)

        self.first_display_index = first_display_index
        self.select_entry_row_index(None, edit_if_already_selected=False)
        self.refresh_entries()
        last_selected_entry_id = self.category_selected_entry_id.get(self.active_category, None)
        if last_selected_entry_id is not None:
            self.select_entry_id(last_selected_entry_id, edit_if_already_selected=False)
        else:
            # Leave no entry selected.
            self.entry_canvas.yview_moveto(0)

        if view_change and old_category is not None:
            self.view_history.record_view_change(
                back=lambda: self.select_category(old_category),
                forward=lambda: self.select_category(selected_category)
            )

    def _shift_selected_category(self, relative_index):
        """Change category by given relative index (usually +1 or -1). Doesn't count as a view change."""
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

    def refresh_categories(self):
        """There are few enough categories changing rarely enough that the widgets can just be regenerated."""
        self.select_category(None)
        for box, label in self.category_boxes.values():
            box.destroy()
            label.destroy()
        self.category_boxes = {}
        with self.set_master(self.category_i_frame):

            categories = self._get_display_categories()

            for row, category in enumerate(categories):
                box = self.Frame(
                    row=row, width=self.CATEGORY_BOX_WIDTH, height=self.CATEGORY_ROW_HEIGHT,
                    highlightthickness=self.CATEGORY_ROW_HIGHLIGHT,
                    bg=self.CATEGORY_UNSELECTED_BG, sticky='nsew')
                label_text = camel_case_to_spaces(category).replace('_', ': ')
                label = self.Label(text=label_text, sticky='w', row=row, fg=self._get_category_text_fg(category),
                                   bg=self.CATEGORY_UNSELECTED_BG, padx=1, font_size=10)
                for widget in {label, box}:
                    bind_events(widget, {
                        "<Button-1>": lambda e, c=category: self.select_category(c, view_change=True),
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
        self.category_i_frame.columnconfigure(0, weight=1)

    @staticmethod
    def _get_category_text_fg(category: str):
        """Returns white text by default. Override to add custom colors based on category name."""
        return '#FFF' if category else '#000'

    # ------------------- #
    #   ENTRY SELECTION   #
    # ------------------- #

    def get_entry_id(self, row_index: int = None) -> int:
        """Retrieves true entry ID from the displayed row index (which is relative to `.first_display_index`).
        Row index defaults to active row index.
        """
        if row_index is None:
            row_index = self.active_row_index
        return self.entry_rows[row_index].entry_id

    def select_entry_id(self, entry_id, set_focus_to_text=True, edit_if_already_selected=True, as_row_index=None):
        """Select entry based on ID and set the category display range to a value such that the selected entry has
        row index `as_row_index` (or as close as possible).

        Optionally sets window focus to text (default True) and edits text if it's already selected (default True).

        Never counts as a view change (more primitive method `select_entry_row_index` can, though).
        """
        if as_row_index is None:
            # Default value is 5 if no newlines are in the target entry and 1 if there are.
            as_row_index = 1 if '\n' in self.get_entry_text(entry_id) else 5

        entry_index = self.get_entry_index(entry_id)
        row_index = self._update_first_entry_display_index(entry_index, as_row_index=as_row_index)
        self.refresh_entries()
        self.entry_canvas.yview_moveto(0)
        self.select_entry_row_index(
            row_index, set_focus_to_text=set_focus_to_text, edit_if_already_selected=edit_if_already_selected)

    def select_entry_row_index(self, row_index, set_focus_to_text=True, edit_if_already_selected=True,
                               id_clicked=False, view_change=False):
        """Select entry from row index, based on currently displayed category and ID range.

        Optionally counts as a view change (default False).
        """
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
            self._cancel_entry_id_edit()
            self._cancel_entry_text_edit()

        self.active_row_index = row_index

        if old_row_index is not None:
            self.entry_rows[old_row_index].active = False
        if row_index is not None:
            self.entry_rows[row_index].active = True
            if set_focus_to_text:
                self.entry_rows[row_index].text_label.focus_set()

        if view_change and old_row_index is not None:
            # View history operates on entry ID rather than row index.
            self.view_history.record_view_change(
                back=lambda: self.select_entry_id(self.get_entry_id(old_row_index), edit_if_already_selected=False),
                forward=lambda: self.select_entry_id(self.get_entry_id(row_index), edit_if_already_selected=False),
            )

    def refresh_entries(self):
        """Refresh entry display. Doesn't affect selected entry row (unless no entries are displayed, in which case
        all rows are deselected)."""
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()

        entries_to_display = self._get_category_name_range(
            first_index=self.first_display_index,
            last_index=self.first_display_index + self.ENTRY_RANGE_SIZE,
        )

        row = 0
        for entry_id, _ in entries_to_display:
            self.entry_rows[row].update_entry(entry_id, self.get_entry_text(entry_id))
            self.entry_rows[row].unhide()
            row += 1

        self.displayed_entry_count = row
        for remaining_row in range(row, self.ENTRY_RANGE_SIZE):
            self.entry_rows[remaining_row].hide()

        if self.displayed_entry_count == 0:
            self.select_entry_row_index(None)
        self._refresh_range_buttons()

    def change_entry_id(self, row_index, new_id, category=None, record_action=True):
        """Set ID of given entry row index in the displayed category (if different from current).

        Optionally recorded as an action (default True).
        """
        if category is None:
            category = self.active_category
        old_id = self.get_entry_id(row_index)
        if old_id == new_id:
            return  # No change.
        if new_id in self.get_category_data():
            self.CustomDialog(
                title="Entry ID Clash",
                message=f"Entry ID {new_id} already exists in {self.DATA_NAME}.{category}. You must change or "
                        f"delete it first.")
            return

        if not self._set_entry_id(old_id, new_id, category, update_row_index=row_index):
            return

        if record_action:
            self.action_history.record_action(
                    undo=partial(self._set_entry_id,
                                 entry_id=new_id, new_id=old_id, category=category),
                    redo=partial(self._set_entry_id,
                                 entry_id=old_id, new_id=new_id, category=category),
                )
        else:
            # Also jump to given entry and record view change.
            current_category = self.active_category
            current_entry_id = self.get_entry_id(self.active_row_index) if self.active_row_index else None
            self.linker.jump(self.TAB_NAME, category, new_id)
            self.view_history.record_view_change(
                back=partial(self.linker.jump, self.TAB_NAME, current_category, current_entry_id),
                forward=partial(self.linker.jump, self.TAB_NAME, category, new_id)
            )

    def change_entry_text(self, row_index, new_text, category=None, record_action=True):
        """Set text of given entry index in the displayed category (if different from current).

        Optionally recorded as an action (default True).
        """
        if category is None:
            category = self.active_category
        entry_id = self.get_entry_id(row_index)
        current_text = self.get_entry_text(entry_id, category=category)
        if current_text == new_text:
            return  # Nothing to change.

        if not self._set_entry_text(entry_id, new_text, category=category, update_row_index=row_index):
            return

        if record_action:
            self.action_history.record_action(
                    undo=partial(self._set_entry_text,
                                 entry_id=entry_id, new_text=new_text, category=category),
                    redo=partial(self._set_entry_text,
                                 entry_id=entry_id, new_text=current_text, category=category),
                )
        else:
            # Also jump to given entry and record view change.
            current_category = self.active_category
            current_entry_id = self.get_entry_id(self.active_row_index) if self.active_row_index else None
            self.linker.jump(self.TAB_NAME, category, entry_id)
            self.view_history.record_view_change(
                back=partial(self.linker.jump, self.TAB_NAME, current_category, current_entry_id),
                forward=partial(self.linker.jump, self.TAB_NAME, category, entry_id)
            )

    def popout_entry_text_edit(self, row_index):
        """Can actually change both ID and text."""
        entry_id = self.get_entry_id(row_index)
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            initial_text = self.get_entry_text(entry_id, self.active_category)
            popout_editor = EntryTextEditBox(self, self.active_category, category_data=self.get_category_data(),
                                             entry_id=entry_id, initial_text=initial_text)
            try:
                new_id, new_text = popout_editor.go()
            except Exception as e:
                _LOGGER.error(e, exc_info=True)
                return self.CustomDialog(
                    "Entry ID/Text Error", f"Error occurred while setting entry ID/text:\n\n{e}")
            if new_id is not None:
                self.change_entry_id(row_index, new_id)
            if new_text is not None:
                self.change_entry_text(row_index, new_text)

    def _add_entry(self, entry_id, text, category=None):
        if category is None:
            category = self.active_category
            if category is None:
                raise ValueError("Cannot add entry without specifying category if 'active_category' is None.")
        if entry_id < 0:
            self.CustomDialog("Entry ID Error", message=f"Entry ID cannot be negative.")
            return False
        if entry_id in self.get_category_data():
            self.CustomDialog(
                title="Text ID Error",
                message=f"Entry ID {entry_id} already exists in category {camel_case_to_spaces(self.active_category)}.")
            return False

        self._cancel_entry_id_edit()
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
        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()
        entry_id = self.get_entry_id(row_index)
        deleted_entry = self.get_category_data(category=category).pop(entry_id)
        self.select_entry_row_index(None)
        self.refresh_entries()
        return deleted_entry

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
                          max(len(self.get_category_data()) - self.ENTRY_RANGE_SIZE, 0))
        if first_index == self.first_display_index:
            return
        return self._update_range(first_index)

    def _start_entry_id_edit(self, row_index):
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            entry_id = self.get_entry_id(row_index)
            initial_text = str(entry_id)
            self._e_entry_id_edit = self.Entry(
                self.entry_rows[row_index].id_box, initial_text=initial_text,
                integers_only=True, sticky='ew', width=int(self.EntryRow.ENTRY_ID_WIDTH * 0.5))
            self._e_entry_id_edit.bind('<Return>', lambda e, i=row_index: self._confirm_entry_id_edit(i))
            self._e_entry_id_edit.bind('<Up>', self._entry_press_up)  # confirms edit
            self._e_entry_id_edit.bind('<Down>', self._entry_press_down)  # confirms edit
            self._e_entry_id_edit.bind('<FocusOut>', lambda e, i=row_index: self._confirm_entry_id_edit(i))
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
                if self._e_entry_id_edit.var.get() != "-":
                    raise
            else:
                self.change_entry_id(row_index, new_id)
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
            self._e_entry_text_edit.bind('<Up>', self._entry_press_up)  # confirms edit
            self._e_entry_text_edit.bind('<Down>', self._entry_press_down)  # confirms edit
            self._e_entry_text_edit.bind('<FocusOut>', lambda e, i=row_index: self._confirm_entry_text_edit(i))
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
            self.change_entry_text(row_index, new_text)
            self._cancel_entry_text_edit()

    def _shift_selected_entry(self, relative_index):
        if self.active_row_index is None:
            return
        new_index = self.active_row_index + relative_index
        if (new_index < 0
                and self.previous_range_button and self.previous_range_button['state'] == 'normal'):
            delta = self._go_to_previous_entry_range()
            new_row_index = -1 - delta
            self.select_entry_row_index(new_row_index, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(new_row_index / (self.ENTRY_RANGE_SIZE + 1))
        elif (new_index >= self.displayed_entry_count
              and self.next_range_button and self.next_range_button['state'] == 'normal'):
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

    def _refresh_range_buttons(self):
        if self.previous_range_button:
            if not self.active_category or self.first_display_index == 0:
                self.previous_range_button['state'] = 'disabled'
            else:
                self.previous_range_button['state'] = 'normal'
        if self.next_range_button:
            if (not self.active_category
                    or self.first_display_index >= len(self.get_category_data()) - self.ENTRY_RANGE_SIZE):
                self.next_range_button['state'] = 'disabled'
            else:
                self.next_range_button['state'] = 'normal'

    # -------------------- #
    #   ABSTRACT METHODS   #  These methods MUST be overridden in child classes.
    # -------------------- #

    def _get_display_categories(self) -> list:
        """Get a list of categories to display."""
        raise NotImplementedError

    def get_category_data(self, category=None):
        """Get a dictionary (or for some data types, a list) of entries from the active category."""
        raise NotImplementedError

    def _get_category_name_range(self, category=None, first_index=None, last_index=None) -> list:
        """Get a sub-list of entry names to display within the given category."""
        raise NotImplementedError

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get the absolute index (NOT the displayed row index) of the given entry ID in its data dictionary/list.

        Note that for some data types (such as maps), the entry index *is* the entry ID, making this a simple method.
        """
        raise NotImplementedError

    def get_entry_text(self, entry_id: int, category=None) -> str:
        """Get the name of the given entry ID."""
        raise NotImplementedError

    def _set_entry_text(self, entry_id: int, text: str, category=None, update_row_index=None) -> bool:
        """Set the name of the given entry ID (exact implementation varies across the different data structures).
        Returns True if the change was actually made, and False otherwise.

        If `update_row_index` is given, that row index (which should contain the given entry ID) will be refreshed.

        Never recorded as an action (the calling function should handle that).
        """
        raise NotImplementedError

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        """Set the ID of the given entry ID (exact implementation varies across the different data structures).

        If `update_row_index` is given, that row index (which should contain the given entry ID) will be refreshed.

        Never recorded as an action (the calling function should handle that).
        """
        raise NotImplementedError


class SoulstructBaseFieldEditor(SoulstructBaseEditor, ABC):
    FIELD_CANVAS_BG = '#1d1d1d'
    FIELD_BOX_WIDTH = 450
    FIELD_BOX_HEIGHT = 400
    FIELD_ROW_HEIGHT = 30
    FIELD_NAME_WIDTH = 30
    FIELD_VALUE_BOX_WIDTH = 200
    FIELD_VALUE_WIDTH = 50
    FIELD_ROW_COUNT = 0  # must be set in child
    FIELD_NAME_FG = '#DDE'
    FIELD_NAME_FG_DEFAULT = '#777'
    FIELD_VALUE_FG = '#FFF'
    FIELD_VALUE_FG_DEFAULT = '#777'

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
            self._default_value = False
            self.field_name = ""
            self.field_type = None
            self.field_nickname = ""
            self.field_docstring = ""
            self.field_links = []
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
                bg=bg_color, anchor='w', font_size=10)
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
            # Main focus bindings are not bound to Checkbutton.

            self.value_combobox = editor.Combobox(
                self.value_box, values=None, width=editor.FIELD_VALUE_WIDTH, no_grid=True, font=("Segoe UI", 10),
                on_select_function=self._combobox_choice)
            self.value_combobox.bind('<MouseWheel>', lambda _: 'break')  # prevent scrolling on collapsed Combobox
            # Main focus bindings are not bound to Combobox.

            # TODO: BEHAVIOR_REF_TYPE combobox should also force a refresh, as it may change field names.
            #  (Class will need access to ParamEntry for this, which is fine.)

            self.context_menu = editor.Menu(self.row_box)
            self.tool_tip = ToolTip(self.row_box, self.field_name_box, self.field_name_label, text=None)

            self.active_value_widget = self.value_label
            self.hide()

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
            self.field_nickname = camel_case_to_spaces(nickname)
            self.field_docstring = docstring

            if self.field_name_label.var.get() != self.field_nickname:
                self.field_name_label.var.set(self.field_nickname)

            if isinstance(self.field_type, str):
                # Note that the *argument* `field_type` is used below, not attribute `self.field_type`.
                self.field_links = self.master.get_field_links(self.field_type, value)
                field_type = int
            else:
                self.field_links = []

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
                if self.field_links:
                    if len(self.field_links) > 1:
                        value_text += '    {AMBIGUOUS}'
                    if self.field_links[0].name is None:
                        value_text += '    {BROKEN LINK}'
                    else:
                        value_text += f'    {{{self.field_links[0].name}}}'
                if self.value_label.var.get() != value_text:
                    self.value_label.var.set(value_text)  # TODO: probably redundant in terms of update efficiency
                self._activate_value_widget(self.value_label)
            elif field_type == bool:
                if value not in {0, 1}:
                    raise ValueError(f"Field with 'bool' type has non-boolean value: {value}")
                self.value_checkbutton.var.set(value)
                self.value_checkbutton.config(fg='#3F3' if value else '#F33', text='ON' if value else 'OFF')
                self._activate_value_widget(self.value_checkbutton)

            if self.field_links and not any(link.name for link in self.field_links) and not self.link_missing:
                self.link_missing = True
                self._update_colors()
            elif (not self.field_links or any(link.name for link in self.field_links)) and self.link_missing:
                self.link_missing = False
                self._update_colors()

            if self._is_default(field_type, value, self.field_nickname):
                self.field_name_label["fg"] = self.master.FIELD_NAME_FG_DEFAULT
                self.value_label["fg"] = self.master.FIELD_VALUE_FG_DEFAULT
            else:
                self.field_name_label["fg"] = self.master.FIELD_NAME_FG
                self.value_label["fg"] = self.master.FIELD_VALUE_FG

            self.build_field_context_menu()
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

        def build_field_context_menu(self):
            # TODO: other stuff? Pop out a scroll box to select an entry, for linked fields?
            self.context_menu.delete(0, 'end')
            if self.field_links:
                for field_link in self.field_links:
                    field_link.add_to_context_menu(self.context_menu, foreground=self.STYLE_DEFAULTS['text_fg'])

        @property
        def editable(self):
            return self.active_value_widget is self.value_label

        def confirm_edit(self, new_text):
            """Inspects new text and returns new field value, or None if the field shouldn't be changed."""
            if not self.editable:
                raise TypeError("Cannot edit a boolean or dropdown field. (Internal error, tell the developer!)")

            if isinstance(self.field_type, str):
                new_value = int(new_text)
                self.field_links = self.master.get_field_links(self.field_type, new_value)
                if len(self.field_links) > 1:
                    new_text += '    {AMBIGUOUS}'
                elif self.field_links and self.field_links[0].name is None:
                    new_text += '    {BROKEN LINK}'
                elif self.field_links:
                    new_text += f'    {{{self.field_links[0].name}}}'
                self.value_label.var.set(new_text)
                if self.field_links and not any(link.name for link in self.field_links) and not self.link_missing:
                    self.link_missing = True
                    self._update_colors()
                elif (not self.field_links or any(link.name for link in self.field_links)) and self.link_missing:
                    self.link_missing = False
                    self._update_colors()
                return new_value

            if self.field_type in {float, int}:
                if new_text == "-":
                    return None  # no change
                if self.field_type == float:
                    new_value = float(new_text)
                    self.value_label.var.set(f"{new_value:.3f}")
                    if self._is_default(self.field_type, new_value, self.field_nickname):
                        self.field_name_label["fg"] = self.master.FIELD_NAME_FG_DEFAULT
                        self.value_label["fg"] = self.master.FIELD_VALUE_FG_DEFAULT
                    else:
                        self.field_name_label["fg"] = self.master.FIELD_NAME_FG
                        self.value_label["fg"] = self.master.FIELD_VALUE_FG
                    return new_value
                elif self.field_type == int:
                    new_value = int(new_text)
                    self.value_label.var.set(str(new_value))
                    if self._is_default(self.field_type, new_value, self.field_nickname):
                        self.field_name_label["fg"] = self.master.FIELD_NAME_FG_DEFAULT
                        self.value_label["fg"] = self.master.FIELD_VALUE_FG_DEFAULT
                    else:
                        self.field_name_label["fg"] = self.master.FIELD_NAME_FG
                        self.value_label["fg"] = self.master.FIELD_VALUE_FG
                    return new_value

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

        def _is_default(self, field_type, value, field_nickname=""):
            if self.master.TAB_NAME == "params":
                if field_type == int:
                    if value in (-1, 0, 1):
                        # TODO: Will have some false positives.
                        return True
                elif field_type == float:
                    if field_nickname.endswith("Multiplier"):
                        if value == 1.0:
                            return True
                    else:
                        if value in (0.0, 1.0):
                            return True
            return False

    def __init__(self, linker: WindowLinker, master=None, toplevel=False, window_title="Soulstruct Editor"):
        if self.FIELD_ROW_COUNT == 0:
            raise AttributeError("Class attribute `FIELD_ROW_COUNT` must be set by child of SoulstructBaseFieldEditor.")
        self.show_hidden_fields = None
        self.field_canvas = None
        self.field_i_frame = None
        self.e_field_value_edit = None
        self.selected_field_row_index = None
        self.displayed_field_count = 0
        self.field_rows = []  # type: List[SoulstructBaseFieldEditor.FieldRow]
        super().__init__(linker=linker, master=master, toplevel=toplevel, window_title=window_title)

    def build(self):
        """Builds category, entry, and field tables."""
        with self.set_master(sticky='nsew', row_weights=[1], column_weights=[0, 1], auto_columns=0):
            self.build_category_canvas()
            with self.set_master(sticky='nsew', row_weights=[0, 1, 0], column_weights=[1, 1]):
                self.build_previous_range_button(row=0, column=0)
                self.build_hidden_fields_checkbutton(row=0, column=1)
                with self.set_master(sticky='nsew', row=1, column=0, row_weights=[1], column_weights=[1]):
                    self.build_entry_frame()
                with self.set_master(sticky='nsew', row=1, column=1, row_weights=[1], column_weights=[1]):
                    self.build_field_frame()
                self.build_next_range_button(row=2, column=0)

    def build_hidden_fields_checkbutton(self, **kwargs):
        self.show_hidden_fields = self.Checkbutton(
            label='Show hidden fields', initial_state=False,
            command=lambda: self.refresh_fields(reset_display=True), pady=10, **kwargs).var

    def build_field_frame(self):
        self.field_canvas = self.Canvas(
            yscrollincrement=self.FIELD_ROW_HEIGHT, vertical_scrollbar=True, horizontal_scrollbar=True,
            borderwidth=10, highlightthickness=0, bg=self.FIELD_CANVAS_BG, sticky='nsew',
            row_weights=[1], column_weights=[1])
        self.field_i_frame = self.Frame(frame=self.field_canvas, width=self.FIELD_BOX_WIDTH, sticky='nsew')
        self.field_i_frame.bind("<Configure>", lambda e, c=self.field_canvas: self.reset_canvas_scroll_region(c))
        self.field_canvas.create_window(0, 0, window=self.field_i_frame, anchor='nw')

        with self.set_master(self.field_i_frame):
            for row in range(self.FIELD_ROW_COUNT):
                self.field_rows.append(self.FieldRow(
                    self, row_index=row,
                    main_bindings={
                        '<Button-1>': lambda _, i=row: self.select_displayed_field_row(i),
                        '<Button-3>': lambda e, i=row: self._right_click_field(e, i),
                        '<Up>': self._field_press_up,
                        '<Down>': self._field_press_down,
                    }))

    def select_category(self, selected_category: Optional[str], first_display_index=0, auto_scroll=False,
                        view_change=False):
        """Updates `active_category` attribute and row colors.

        By default, resets `first_display_index` to zero.
        Supports 'selected_category=None' to deselect all categories.
        """
        old_category = self.active_category

        if old_category is not None:
            selected_entry_id = self.get_entry_id(self.active_row_index) if self.active_row_index else None
            self.category_selected_entry_id[old_category] = selected_entry_id

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

        if auto_scroll:
            view_ratio = list(self.category_boxes).index(self.active_category) / (len(self.category_boxes) + 1)
            self.category_canvas.yview_moveto(view_ratio)

        self.first_display_index = first_display_index
        self.select_entry_row_index(None, edit_if_already_selected=False)
        self.refresh_entries(reset_field_display=True)  # TODO: this argument is the only difference. Better way?
        last_selected_entry_id = self.category_selected_entry_id.get(self.active_category, None)
        if last_selected_entry_id is not None:
            self.select_entry_id(last_selected_entry_id, edit_if_already_selected=False)
        else:
            # Leave no entry selected.
            self.entry_canvas.yview_moveto(0)

        if view_change and old_category is not None:
            self.view_history.record_view_change(
                back=lambda: self.select_category(old_category),
                forward=lambda: self.select_category(selected_category)
            )

    def refresh_entries(self, reset_field_display=False):
        super().refresh_entries()
        self.refresh_fields(reset_display=reset_field_display)

    def select_entry_row_index(self, row_index, set_focus_to_text=True, edit_if_already_selected=True,
                               id_clicked=False, view_change=False):
        super().select_entry_row_index(row_index, set_focus_to_text=set_focus_to_text,
                                       edit_if_already_selected=edit_if_already_selected, id_clicked=id_clicked,
                                       view_change=view_change)
        self.refresh_fields()

        # `refresh_fields()` seems to steal focus aggressively, so end by setting it back to entry name.
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

        self.field_i_frame.grid_columnconfigure(1, weight=1)

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
            self.CustomDialog("Entry ID Error", message=f"Entry ID cannot be negative.")
            return False
        if entry_id in self.get_category_data():
            self.CustomDialog(
                title="Entry ID Error",
                message=f"Entry ID {entry_id} already exists in category {camel_case_to_spaces(self.active_category)}.")
            return False

        self._cancel_entry_id_edit()
        self._cancel_entry_text_edit()
        self.get_category_data()[entry_id] = new_field_dict  # add entry to category dictionary
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

    def select_field_name(self, field_name, set_focus_to_value=True, edit_if_already_selected=False, auto_scroll=True):
        row_index = self.get_field_row_index_from_name(field_name)
        self.select_displayed_field_row(row_index, set_focus_to_value=set_focus_to_value,
                                        edit_if_already_selected=edit_if_already_selected)
        self.refresh_fields()

        self.field_canvas.yview_moveto(0)
        if auto_scroll:
            self.field_canvas.yview_scroll(row_index, "units")

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
            self.e_field_value_edit.bind('<Up>', self._field_press_up)  # confirms edit
            self.e_field_value_edit.bind('<Down>', self._field_press_down)  # confirms edit
            self.e_field_value_edit.bind('<FocusOut>', lambda e, i=row_index: self._confirm_field_value_edit(i))
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
                _LOGGER.error(f"Could not interpret field value. Error: {str(e)}")
                self.bell()
                return
            if true_value is not None:
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

    def get_field_links(self, field_type, field_value, valid_null_values=None) -> list:
        raise NotImplementedError
