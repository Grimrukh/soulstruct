from __future__ import annotations

__all__ = ["SoulstructBaseEditor", "EntryRow"]

import abc
import logging
import typing as tp
from functools import partial

from soulstruct.constants.darksouls1.maps import get_map
from soulstruct.project.utilities import ActionHistory, ViewHistory, bind_events, EntryTextEditBox
from soulstruct.utilities import camel_case_to_spaces
from soulstruct.utilities.window import SmartFrame, ToolTip

if tp.TYPE_CHECKING:
    from soulstruct.game_types.msb_types import Map
    from soulstruct.project.links import WindowLinker

_LOGGER = logging.getLogger(__name__)


class EntryRow:
    """Container/manager for widgets of a single entry row in the Editor."""
    ENTRY_ANCHOR = "center"
    ENTRY_ROW_HEIGHT = 30
    SHOW_ENTRY_ID = True
    EDIT_ENTRY_ID = True
    ENTRY_ID_WIDTH = 15
    ENTRY_ID_FG = "#CDF"
    ENTRY_TEXT_WIDTH = 150
    ENTRY_TEXT_FG = "#FFF"

    def __init__(self, editor: SoulstructBaseEditor, row_index: int, main_bindings: dict = None):
        self.master = editor
        self.STYLE_DEFAULTS = editor.STYLE_DEFAULTS

        self.row_index = row_index
        self._entry_id = None
        self._entry_text = None
        self._active = False

        bg_color = self._get_color()

        self.row_box = editor.Frame(
            width=self.ENTRY_ID_WIDTH + self.ENTRY_TEXT_WIDTH,
            height=self.ENTRY_ROW_HEIGHT,
            bg=bg_color,
            row=row_index,
            columnspan=2 if self.SHOW_ENTRY_ID else 1,
            sticky="nsew",
        )
        bind_events(self.row_box, main_bindings)

        if self.SHOW_ENTRY_ID:
            self.id_box = editor.Frame(row=row_index, column=0, bg=bg_color, sticky="ew")
            self.id_label = editor.Label(
                self.id_box,
                text="",
                width=self.ENTRY_ID_WIDTH,
                bg=bg_color,
                fg=self.ENTRY_ID_FG,
                font_size=11,
                sticky="e",
            )
            if self.EDIT_ENTRY_ID:
                id_bindings = main_bindings.copy()
                id_bindings["<Button-1>"] = lambda _, i=row_index: self.master.select_entry_row_index(
                    i, id_clicked=True
                )
            else:
                id_bindings = main_bindings
            bind_events(self.id_box, id_bindings)
            bind_events(self.id_label, id_bindings)
        else:
            self.id_label = None

        self.text_box = editor.Frame(row=row_index, column=1 if self.SHOW_ENTRY_ID else 0, bg=bg_color, sticky="ew")
        bind_events(self.text_box, main_bindings)

        self.text_label = editor.Label(
            self.text_box,
            text="",
            bg=bg_color,
            fg=self.ENTRY_TEXT_FG,
            anchor="w",
            font_size=11,
            justify="left",
            width=self.ENTRY_TEXT_WIDTH,
        )
        bind_events(self.text_label, main_bindings)

        self.context_menu = editor.Menu(self.row_box)

        self.tool_tip = ToolTip(
            self.row_box, self.id_box, self.id_label, self.text_box, self.text_label, text=None, wraplength=350
        )

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
        self.context_menu.delete(0, "end")
        self.context_menu.add_command(
            label="Edit Entry Text in Popout (Shift + Click)",
            command=lambda: self.master.popout_entry_text_edit(self.row_index),
        )
        self.context_menu.add_command(
            label="Duplicate Entry to Next ID",
            command=lambda: self.master.add_relative_entry(self.entry_id, offset=1),
        )
        self.context_menu.add_command(
            label="Delete Entry",
            command=lambda: self.master.delete_entry(self.row_index),
        )

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

    @property
    def _colored_widgets(self):
        """Returns a tuple of all widgets that should be colored by `._update_colors()`."""
        return self.row_box, self.id_box, self.id_label, self.text_box, self.text_label

    def _update_colors(self):
        bg_color = self._get_color()
        for widget in self._colored_widgets:
            widget["bg"] = bg_color

    def _get_color(self):
        """Inspects entry text/state and assembles a tuple of 'bg' color values."""
        base_bg = int(self.STYLE_DEFAULTS["bg"].lstrip("#"))  # dark grey
        if self._entry_text is not None:
            if not self._entry_text:
                base_bg += 200  # entry text is empty (red)
            elif not self._entry_text.strip():
                base_bg += 110  # entry text contains only space (yellow)
        if self._active:
            base_bg += 123  # turquoise boost
        if self.row_index % 2:
            base_bg += 111  # every second row is slightly brighter
        return f"#{base_bg}"


class SoulstructBaseEditor(SmartFrame, abc.ABC):
    """Base class for a two-part window that edits entry IDs and names within specific categories."""
    DATA_NAME = ""
    TAB_NAME = ""
    CANVAS_BG = "#1d1d1d"
    CATEGORY_BOX_WIDTH = 250
    CATEGORY_BOX_HEIGHT = 400
    CATEGORY_ROW_HEIGHT = 30
    CATEGORY_ROW_HIGHLIGHT = 1
    CATEGORY_UNSELECTED_BG = "#242424"
    CATEGORY_SELECTED_BG = "#414141"
    ENTRY_CANVAS_BG = "#1d1d1d"
    ENTRY_BOX_WIDTH = 800
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 500

    ENTRY_ROW_CLASS = EntryRow
    entry_rows: tp.List[EntryRow]

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

        self.entry_rows = []
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
        self.bind_all("<Control-z>", self.undo)
        self.bind_all("<Control-y>", self.redo)
        self.refresh_categories()
        self.refresh_entries()

    def build_category_canvas(self):
        with self.set_master(sticky="nsew", row_weights=[1], column_weights=[1], auto_columns=0):
            self.category_canvas = self.Canvas(
                vertical_scrollbar=True,
                yscrollincrement=self.CATEGORY_ROW_HEIGHT,
                width=self.CATEGORY_BOX_WIDTH,
                height=self.CATEGORY_BOX_HEIGHT,
                borderwidth=0,
                highlightthickness=0,
                sticky="nsew",
            )
        with self.set_master(self.category_canvas):
            self.category_i_frame = self.Frame(sticky="nsew")
        self.link_to_scrollable(self.category_canvas, self.category_i_frame)
        self.category_canvas.create_window(0, 0, window=self.category_i_frame, anchor="n")
        self.category_i_frame.bind("<Configure>", lambda e, c=self.category_canvas: self.reset_canvas_scroll_region(c))

    def build_previous_range_button(self, **kwargs):
        self.previous_range_button = self.Button(
            text=f"Previous {self.ENTRY_RANGE_SIZE}",
            font_size=10,
            bg="#111",
            width=30,
            command=self._go_to_previous_entry_range,
            padx=10,
            pady=10,
            **kwargs,
        )

    def build_next_range_button(self, **kwargs):
        self.next_range_button = self.Button(
            text=f"Next {self.ENTRY_RANGE_SIZE}",
            font_size=10,
            bg="#111",
            width=30,
            command=self._go_to_next_entry_range,
            padx=10,
            pady=10,
            **kwargs,
        )

    def build_entry_frame(self):
        """Master should already be set."""
        self.entry_canvas = self.Canvas(
            width=self.ENTRY_BOX_WIDTH,
            height=self.ENTRY_BOX_HEIGHT,
            borderwidth=0,
            vertical_scrollbar=True,
            horizontal_scrollbar=True,
            sticky="nsew",
            highlightthickness=0,
            yscrollincrement=self.ENTRY_ROW_CLASS.ENTRY_ROW_HEIGHT,
            bg=self.ENTRY_CANVAS_BG,
            row_weights=[1],
            column_weights=[1],
        )
        self.entry_i_frame = self.Frame(frame=self.entry_canvas, sticky="ew", column_weights=[1, 1])
        self.entry_i_frame.bind("<Configure>", lambda e, c=self.entry_canvas: self.reset_canvas_scroll_region(c))
        self.entry_canvas.create_window(0, 0, window=self.entry_i_frame, anchor="nw")

        with self.set_master(self.entry_i_frame):
            for row in range(self.ENTRY_RANGE_SIZE):
                self.entry_rows.append(
                    self.ENTRY_ROW_CLASS(
                        self,
                        row_index=row,
                        main_bindings={
                            "<Button-1>": lambda _, i=row: self.select_entry_row_index(i),
                            "<Shift-Button-1>": lambda e, i=row: self.popout_entry_text_edit(i),
                            "<Button-3>": lambda e, i=row: self._right_click_entry(e, i),
                            "<Up>": self._entry_press_up,
                            "<Down>": self._entry_press_down,
                            "<Delete>": lambda e, i=row: self.delete_entry(i),
                            "<Prior>": lambda e: self._go_to_previous_entry_range(),
                            "<Next>": lambda e: self._go_to_next_entry_range(),
                        },
                    )
                )

    def build(self):
        with self.set_master(sticky="nsew", row_weights=[1], column_weights=[0, 1], auto_columns=0):
            self.build_category_canvas()
            with self.set_master(sticky="nsew", row_weights=[1], column_weights=[1], auto_rows=0):
                # self.build_previous_range_button()
                with self.set_master(sticky="nsew", row_weights=[1], column_weights=[1]):
                    self.build_entry_frame()
                # self.build_next_range_button()

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
        return self.map_choice.var.get().split(" [")[0]

    def get_map(self) -> Map:
        return get_map(self.map_choice_id)

    # ---------------------- #
    #   CATEGORY SELECTION   #
    # ---------------------- #

    def select_category(
        self, selected_category: tp.Optional[str], first_display_index=0, auto_scroll=False, view_change=False
    ):
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
                    box["bg"] = self.CATEGORY_SELECTED_BG
                    label["bg"] = self.CATEGORY_SELECTED_BG
                else:
                    box["bg"] = self.CATEGORY_UNSELECTED_BG
                    label["bg"] = self.CATEGORY_UNSELECTED_BG

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
                back=lambda: self.select_category(old_category), forward=lambda: self.select_category(selected_category)
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
                self.category_canvas.yview_scroll(-1, "units")

    def _category_press_down(self, _=None):
        if self.active_category is not None:
            categories = self._get_display_categories()
            active_category_index = categories.index(self.active_category)
            self._shift_selected_category(+1)
            if self.category_canvas.yview()[0] != 0.0 or active_category_index > 5:
                self.category_canvas.yview_scroll(1, "units")

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
                    row=row,
                    width=self.CATEGORY_BOX_WIDTH,
                    height=self.CATEGORY_ROW_HEIGHT,
                    highlightthickness=self.CATEGORY_ROW_HIGHLIGHT,
                    bg=self.CATEGORY_UNSELECTED_BG,
                    sticky="nsew",
                )
                label_text = camel_case_to_spaces(category).replace("_", ": ")
                label = self.Label(
                    text=label_text,
                    sticky="w",
                    row=row,
                    fg=self._get_category_text_fg(category),
                    bg=self.CATEGORY_UNSELECTED_BG,
                    padx=1,
                    font_size=10,
                )
                for widget in {label, box}:
                    bind_events(
                        widget,
                        {
                            "<Button-1>": lambda e, c=category: self.select_category(c, view_change=True),
                            "<Up>": self._category_press_up,
                            "<Down>": self._category_press_down,
                            "<Prior>": self._category_press_up,
                            "<Next>": self._category_press_down,
                        },
                    )
                if category == self.active_category:
                    label["bg"] = self.CATEGORY_SELECTED_BG
                    box["bg"] = self.CATEGORY_SELECTED_BG
                self.link_to_scrollable(self.category_canvas, box, label)
                self.category_boxes[category] = (box, label)

        self.category_canvas.yview_moveto(0)
        self.category_i_frame.columnconfigure(0, weight=1)

    @staticmethod
    def _get_category_text_fg(category: str):
        """Returns white text by default. Override to add custom colors based on category name."""
        return "#FFF" if category else "#000"

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
            as_row_index = 1 if "\n" in self.get_entry_text(entry_id) else 5

        entry_index = self.get_entry_index(entry_id)
        row_index = self._update_first_entry_display_index(entry_index, as_row_index=as_row_index)
        self.refresh_entries()
        self.entry_canvas.yview_moveto(0)
        self.select_entry_row_index(
            row_index, set_focus_to_text=set_focus_to_text, edit_if_already_selected=edit_if_already_selected
        )

    def select_entry_row_index(
        self, row_index, set_focus_to_text=True, edit_if_already_selected=True, id_clicked=False, view_change=False
    ):
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
            first_index=self.first_display_index, last_index=self.first_display_index + self.ENTRY_RANGE_SIZE,
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
                f"delete it first.",
            )
            return

        if not self._set_entry_id(old_id, new_id, category, update_row_index=row_index):
            return

        if record_action:
            self.action_history.record_action(
                undo=partial(self._set_entry_id, entry_id=new_id, new_id=old_id, category=category),
                redo=partial(self._set_entry_id, entry_id=old_id, new_id=new_id, category=category),
            )
        else:
            # Also jump to given entry and record view change.
            current_category = self.active_category
            current_entry_id = self.get_entry_id(self.active_row_index) if self.active_row_index else None
            self.linker.jump(self.TAB_NAME, category, new_id)
            self.view_history.record_view_change(
                back=partial(self.linker.jump, self.TAB_NAME, current_category, current_entry_id),
                forward=partial(self.linker.jump, self.TAB_NAME, category, new_id),
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
                undo=partial(self._set_entry_text, entry_id=entry_id, new_text=new_text, category=category),
                redo=partial(self._set_entry_text, entry_id=entry_id, new_text=current_text, category=category),
            )
        else:
            # Also jump to given entry and record view change.
            current_category = self.active_category
            current_entry_id = self.get_entry_id(self.active_row_index) if self.active_row_index else None
            self.linker.jump(self.TAB_NAME, category, entry_id)
            self.view_history.record_view_change(
                back=partial(self.linker.jump, self.TAB_NAME, current_category, current_entry_id),
                forward=partial(self.linker.jump, self.TAB_NAME, category, entry_id),
            )

    def popout_entry_text_edit(self, row_index):
        """Can actually change both ID and text."""
        entry_id = self.get_entry_id(row_index)
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            initial_text = self.get_entry_text(entry_id, self.active_category)
            popout_editor = EntryTextEditBox(
                self,
                self.active_category,
                category_data=self.get_category_data(),
                entry_id=entry_id,
                initial_text=initial_text,
            )
            try:
                new_id, new_text = popout_editor.go()
            except Exception as e:
                _LOGGER.error(e, exc_info=True)
                return self.CustomDialog("Entry ID/Text Error", f"Error occurred while setting entry ID/text:\n\n{e}")
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
                message=f"Entry ID {entry_id} already exists in category {camel_case_to_spaces(self.active_category)}.",
            )
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
        if row_index is None:
            self.bell()
            return
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
        first_index = min(
            self.first_display_index + self.ENTRY_RANGE_SIZE,
            max(len(self.get_category_data()) - self.ENTRY_RANGE_SIZE, 0),
        )
        if first_index == self.first_display_index:
            return
        return self._update_range(first_index)

    def _start_entry_id_edit(self, row_index):
        if not self._e_entry_text_edit and not self._e_entry_id_edit:
            entry_id = self.get_entry_id(row_index)
            initial_text = str(entry_id)
            self._e_entry_id_edit = self.Entry(
                self.entry_rows[row_index].id_box,
                initial_text=initial_text,
                integers_only=True,
                sticky="ew",
                width=int(self.ENTRY_ROW_CLASS.ENTRY_ID_WIDTH * 0.5),
            )
            self._e_entry_id_edit.bind("<Return>", lambda e, i=row_index: self._confirm_entry_id_edit(i))
            self._e_entry_id_edit.bind("<Up>", self._entry_press_up)  # confirms edit
            self._e_entry_id_edit.bind("<Down>", self._entry_press_down)  # confirms edit
            self._e_entry_id_edit.bind("<FocusOut>", lambda e, i=row_index: self._confirm_entry_id_edit(i))
            self._e_entry_id_edit.bind("<Escape>", lambda e: self._cancel_entry_id_edit())
            self._e_entry_id_edit.focus_set()
            self._e_entry_id_edit.select_range(0, "end")

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
            if "\n" in initial_text:
                return self.popout_entry_text_edit(row_index)
            self._e_entry_text_edit = self.Entry(
                self.entry_rows[row_index].text_box, initial_text=initial_text, sticky="ew", width=5
            )
            self._e_entry_text_edit.bind("<Return>", lambda e, i=row_index: self._confirm_entry_text_edit(i))
            self._e_entry_text_edit.bind("<Up>", self._entry_press_up)  # confirms edit
            self._e_entry_text_edit.bind("<Down>", self._entry_press_down)  # confirms edit
            self._e_entry_text_edit.bind("<FocusOut>", lambda e, i=row_index: self._confirm_entry_text_edit(i))
            self._e_entry_text_edit.bind("<Escape>", lambda e: self._cancel_entry_text_edit())
            self._e_entry_text_edit.focus_set()
            self._e_entry_text_edit.select_range(0, "end")

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
        if new_index < 0 and self.previous_range_button and self.previous_range_button["state"] == "normal":
            delta = self._go_to_previous_entry_range()
            new_row_index = -1 - delta
            self.select_entry_row_index(new_row_index, edit_if_already_selected=False)
            self.entry_canvas.yview_moveto(new_row_index / (self.ENTRY_RANGE_SIZE + 1))
        elif (
            new_index >= self.displayed_entry_count
            and self.next_range_button
            and self.next_range_button["state"] == "normal"
        ):
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
                self.entry_canvas.yview_scroll(-1, "units")

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
                self.entry_canvas.yview_scroll(1, "units")

    def _refresh_range_buttons(self):
        if self.previous_range_button:
            if not self.active_category or self.first_display_index == 0:
                self.previous_range_button["state"] = "disabled"
            else:
                self.previous_range_button["state"] = "normal"
        if self.next_range_button:
            if (
                not self.active_category
                or self.first_display_index >= len(self.get_category_data()) - self.ENTRY_RANGE_SIZE
            ):
                self.next_range_button["state"] = "disabled"
            else:
                self.next_range_button["state"] = "normal"

    # -------------------- #
    #   ABSTRACT METHODS   #  These methods MUST be overridden in child classes.
    # -------------------- #

    @abc.abstractmethod
    def _get_display_categories(self) -> list:
        """Get a list of categories to display."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_category_data(self, category=None):
        """Get a dictionary (or for some data types, a list) of entries from the active category."""
        raise NotImplementedError

    @abc.abstractmethod
    def _get_category_name_range(self, category=None, first_index=None, last_index=None) -> list:
        """Get a sub-list of entry names to display within the given category."""
        raise NotImplementedError

    @abc.abstractmethod
    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get the absolute index (NOT the displayed row index) of the given entry ID in its data dictionary/list.

        Note that for some data types (such as maps), the entry index *is* the entry ID, making this a simple method.
        """
        raise NotImplementedError

    @abc.abstractmethod
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

    @abc.abstractmethod
    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        """Set the ID of the given entry ID (exact implementation varies across the different data structures).

        If `update_row_index` is given, that row index (which should contain the given entry ID) will be refreshed.

        Never recorded as an action (the calling function should handle that).
        """
        raise NotImplementedError
