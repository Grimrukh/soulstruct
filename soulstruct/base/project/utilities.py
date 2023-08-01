from __future__ import annotations

import tkinter as tk
import typing as tp
from functools import wraps

from ...utilities.text import word_wrap, camel_case_to_spaces
from soulstruct.utilities.window import SmartFrame

from .exceptions import SoulstructProjectError

if tp.TYPE_CHECKING:
    from .editors.base_editor import BaseEditor
    from .window import ProjectWindow

__all__ = [
    "error_as_dialog",
    "TagData",
    "TkTextEditor",
    "NameSelectionBox",
    "CategorizedNameSelectionBox",
    "NumberEditBox",
    "TextEditBox",
    "EntryTextEditBox",
    "ItemTextEditBox",
    "SequenceNameEditBox",
    "GroupBitSetEditBox",
    "ActionHistory",
    "ViewHistory",
    "bind_events",
]


def bind_events(widget, bindings: dict):
    for event, func in bindings.items():
        widget.bind(event, func)


def error_as_dialog(window, func):
    @wraps(func)
    def window_method(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except SoulstructProjectError as e:
            window.CustomDialog(
                title="Soulstruct Error", message=word_wrap(str(e), 50),
            )
        except Exception as e:
            window.CustomDialog(
                title="Unknown Internal Error",
                message="Internal Error:\n\n" + word_wrap(str(e), 50) + "\n\nPlease report this error.",
            )

    return window_method


class ViewHistory:
    """Global window timeline of selected tab, category, entry, and (if applicable) field.

    Note that view changes that are caused by undo and redo functions are not treated differently here.
    """

    def __init__(self):
        self._back_stack = []
        self._forward_stack = []

    def record_view_change(self, back, forward):
        if not callable(back) or not callable(forward):
            raise TypeError("Back and forward view-changing functions must be callable and have no arguments.")
        self._back_stack.append((back, forward))
        self._forward_stack = []  # old future timeline dies

    def back(self, _=None):
        if self._back_stack:
            back, forward = self._back_stack.pop()
            back(from_history=True)
            self._forward_stack.append((back, forward))
            return True
        else:
            return False

    def forward(self, _=None):
        if self._forward_stack:
            back, forward = self._forward_stack.pop()
            forward(from_history=True)
            self._back_stack.append((back, forward))
            return True
        else:
            return False


class ActionHistory:
    """Each tab maintains a separate ActionHistory timeline of action/inverse-action data-modifying pairs for undo and
    redo."""

    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def record_action(self, undo, redo):
        """Record the undo and redo callbacks (no arguments) for an action."""
        if not callable(undo) or not callable(redo):
            raise TypeError("Action and inverse action functions must be callable and have no arguments.")
        self._undo_stack.append((undo, redo))
        self._redo_stack = []  # old future timeline dies

    def undo(self, _=None):
        if self._undo_stack:
            undo, redo = self._undo_stack.pop()
            undo(from_history=True)
            self._redo_stack.append((undo, redo))
            return True
        else:
            return False

    def redo(self, _=None):
        if self._redo_stack:
            undo, redo = self._redo_stack.pop()
            redo(from_history=True)
            self._undo_stack.append((undo, redo))
            return True
        else:
            return False


class TagData(tp.NamedTuple):
    foreground: str  # hex color
    pattern: str
    offsets: tuple[int, int] | None


_TEXT_EDITOR_TK_SETUP = """
proc widget_proxy {actual_widget callback args} {

    # This prevents recursion if the widget is called during the callback.
    set flag ::dont_recurse(actual_widget)

    # Call the real Tk widget with the real args.
    set result [uplevel [linsert $args 0 $actual_widget]]

    # Call the callback and ignore errors, but only do so on inserts, deletes, and changes in the 
    # mark. Otherwise we'll call the callback way too often.
    if {! [info exists $flag]} {
        if {([lindex $args 0] in {insert replace delete}) ||
            ([lrange $args 0 2] == {mark set insert})} {
            # the flag makes sure that whatever happens in the
            # callback doesn't cause the callbacks to be called again.
            set $flag 1
            catch {$callback $result {*}$args } callback_result
            unset -nocomplain $flag
        }
    }

    # Return the result from the real widget command.
    return $result
}
"""

_TEXT_EDITOR_TK_ALIAS = """
rename {widget} _{widget}
interp alias {{}} ::{widget} {{}} widget_proxy _{widget} {callback}
"""


class TkTextEditor(tk.Text):
    TAGS = {}  # type: dict[str, TagData]

    def __init__(self, *args, **kwargs):
        """Text widget that uses some Tcl voodoo (courtesy of Tkinter wizard Bryan Oakley) to allow arbitrary callbacks
        whenever a 'mark', 'set', or 'insert' Tcl command occurs (e.g. updating a line number tracker).

        Also includes methods for scanning and tagging arbitrary regex patterns, which should be given in `cls.TAGS`,
        and for auto-indenting new lines based on the previous line's indent.

        See: https://stackoverflow.com/a/13840728
        """
        super().__init__(*args, **kwargs)
        self.callback = None
        private_callback = self.register(self._callback)
        self.tk.eval(_TEXT_EDITOR_TK_SETUP)
        self.tk.eval(_TEXT_EDITOR_TK_ALIAS.format(
            widget=str(self), callback=private_callback,
        ))

        for tag_name, tag_data in self.TAGS.items():
            self.tag_configure(tag_name, foreground=tag_data.foreground)
        self.tag_configure("found", background="#224433")
        self.tag_configure("error", background="#443322")

        self.bind("<Return>", self._auto_indent_newline)
        self.bind("<Tab>", self._tab_four_spaces)
        self.bind("<Home>", self._home_key)
        self.bind("<Control-slash>", self._toggle_comment)
        self.bind("<Control-BackSpace>", self._delete_word)
        self.bind("<Control-less>", self._decrease_font_size)
        self.bind("<Control-greater>", self._increase_font_size)

    def _callback(self, result, *args):
        if self.callback:
            self.callback(result, *args)

    def set_callback(self, callback):
        self.callback = callback

    def highlight_line(self, number, tag):
        """Apply the given tag to all text in the given line. Clears tag first."""
        self.tag_remove(tag, "1.0", "end")
        self.tag_add(tag, f"{number}.0 linestart", f"{number}.0 lineend")

    def highlight_pattern(
        self, pattern, tag, start="1.0", end="end", regexp=False, clear=True, start_offset=0, end_offset=0
    ):
        """Apply the given tag to all text that matches the given pattern. Clears tag first by default.

        If 'regexp' is set to True, pattern will be treated as a regular expression according to Tcl's regular
        expression syntax.
        """
        start = self.index(start)
        end = self.index(end)
        if clear:
            self.tag_remove(tag, start, end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while 1:
            index = self.search(pattern, index="matchEnd", stopindex="searchLimit", count=count, regexp=regexp)
            if index == "":
                break
            if count.get() == 0:
                break  # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", f"{index}+{start_offset}c")
            self.mark_set("matchEnd", f"{index}+{count.get() - end_offset}c")
            self.tag_add(tag, "matchStart", "matchEnd")

    def color_syntax(self, start="1.0", end="end"):
        for tag, tag_data in self.TAGS.items():
            if tag_data.offsets is not None:
                self.highlight_pattern(
                    tag_data.pattern,
                    tag,
                    regexp=True,
                    clear=True,
                    start=start,
                    end=end,
                    start_offset=tag_data.offsets[0],
                    end_offset=tag_data.offsets[1],
                )

    def _tab_four_spaces(self, _):
        """Tab key inserts four spaces rather than a tab character."""
        self.insert("insert", "    ")
        return "break"

    def _home_key(self, _):
        """Home key ignores starting whitespace, unless there's ONLY whitespace before the caret."""
        pre_text = self.get("insert linestart", "insert")
        first_non_space_index = len(pre_text) - len(pre_text.lstrip(" "))
        if first_non_space_index != len(pre_text):
            # Something other than whitespace exists. Get first non-space character.
            new_index = self.index("insert linestart").split(".")[0] + f".{first_non_space_index}"
            self.mark_set("insert", new_index)
        else:
            # Only whitespace before cursor.
            self.mark_set("insert", "insert linestart")
        return "break"

    def _toggle_comment(self, _):
        """Control-/ comments or uncomments this line."""
        current_line = self.get("insert linestart", "insert lineend")
        current_line_stripped = current_line.lstrip(" ")
        spaces_before_hash = len(current_line) - len(current_line_stripped)
        if not current_line_stripped:
            # Blank line.
            pass
        elif current_line_stripped[0] == "#":
            # Line is already commented out. Remove hash (there may be others after it).
            self.delete("insert linestart", "insert lineend")
            self.insert("insert linestart", f"{' ' * spaces_before_hash}{current_line_stripped[1:]}")
            self.color_syntax("insert linestart", "insert lineend")
        else:
            # Line is not commented. Add a hash before the first non-space character.
            hash_index = self.index("insert linestart").split(".")[0] + f".{spaces_before_hash}"
            self.insert(hash_index, "#")
            self.color_syntax("insert linestart", "insert lineend")
        return "break"

    def _delete_word(self, _):
        """Deletes the word before the cursor."""
        self.delete("insert wordstart", "insert")
        return "break"

    def _auto_indent_newline(self, _):
        """Inserts a newline with the same leading spaces as the current line."""
        current_line = self.index(tk.INSERT).split('.')[0]
        line_text = self.get(f"{current_line}.0", f"{current_line}.end")
        leading_space_count = len(line_text) - len(line_text.lstrip())

        # Create a new line and add the leading spaces.
        self.insert(tk.INSERT, '\n' + ' ' * leading_space_count)

        # Return 'break' to prevent the default newline behavior.
        return "break"

    def _decrease_font_size(self, _):
        """Decreases the font size by 1."""
        font_name, font_size = self["font"].split(" ")
        self["font"] = (font_name, int(font_size) - 1)
        return "break"

    def _increase_font_size(self, _):
        """Increases the font size by 1."""
        font_name, font_size = self["font"].split(" ")
        self["font"] = (font_name, int(font_size) + 1)
        return "break"


class NameSelectionBox(SmartFrame):
    """Small pop-out widget that allows you to select a name from some list."""

    WIDTH = 50  # characters
    HEIGHT = 20  # lines

    output: str | None  # name

    def __init__(self, master, names, list_name="List", split_string=""):
        super().__init__(toplevel=True, master=master, window_title=f"Select Entry from {list_name}")

        self.output = None
        self.split_string = split_string

        with self.set_master(padx=20, pady=20, auto_rows=0):
            self.Label(text="Double-click an entry to select it.")
            self._names = self.Listbox(
                values=names,
                width=self.WIDTH,
                height=self.HEIGHT,
                vertical_scrollbar=True,
                selectmode="single",
                font=("Consolas", 14),
                padx=20,
                pady=20,
            )

        self._names.bind("<Double-Button-1>", lambda e: self.done(True))

        self.bind_all("<Escape>", lambda e: self.done(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.done(False))
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
            if self.split_string:
                self.output = self.output.split(self.split_string)[0]
        self.quit()


class CategorizedNameSelectionBox(SmartFrame):
    """Small pop-out widget that allows you to select a name from one of multiple category lists, chosen by dropdown."""

    WIDTH = 50  # characters
    HEIGHT = 20  # lines

    output: tuple[str, str] | None  # category, name

    def __init__(
        self, master, categories: dict[str, list[str]], initial_category: str = "", list_name="List", split_string=""
    ):
        super().__init__(toplevel=True, master=master, window_title=f"Select Entry from {list_name}")

        self.categories = categories
        self.output = None
        self.split_string = split_string
        if not initial_category:
            initial_category = list(categories.keys())[0]
        elif initial_category not in categories:
            raise ValueError(f"Initial category '{initial_category}' not in categories.")

        with self.set_master(padx=40, pady=40, auto_rows=0):
            self.Label(text="Double-click an entry to select it.", pady=(0, 20))
            self._category = self.Combobox(
                values=list(categories.keys()),
                initial_value=initial_category,
                width=self.WIDTH,
                font=("Consolas", 14),
                on_select_function=self._update_category,
                sticky="e",
                label="Category:",
                label_position="above",
            )
            self._name_filter = self.Entry(
                width=self.WIDTH - 10,
                font=("Consolas", 14),
                label="Filter:",
                label_position="left",
                sticky="e",
                pady=10,
            ).var
            self._name_filter.trace("w", lambda n, i, m: self._filter_names(self._name_filter.get()))
            self._names = self.Listbox(
                values=categories[initial_category],
                width=self.WIDTH,
                height=self.HEIGHT,
                vertical_scrollbar=True,
                selectmode="single",
                font=("Consolas", 14),
                sticky="e",
            )

        self._names.bind("<Double-Button-1>", lambda e: self.done(True))

        self.bind_all("<Escape>", lambda e: self.done(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.done(False))
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3), transient=True)

    def _update_category(self, _):
        """Called on dropdown change. Updates the list of names to match the selected category."""
        self._names.delete(0, "end")
        for name in self.categories[self._category.var.get()]:
            self._names.insert("end", name)

    def _filter_names(self, filter_text: str):
        """Called on text change. Filters the list of names to match the entered text."""
        self._names.delete(0, "end")
        for name in self.categories[self._category.var.get()]:
            if filter_text.lower() in name.lower():
                self._names.insert("end", name)

    def go(self):
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def done(self, confirm=True):
        if confirm:
            category = self._category.var.get()
            name = self._names.get(self._names.curselection())
            if self.split_string:
                name = name.split(self.split_string)[0]
            self.output = category, name
        self.quit()


class NumberEditBox(SmartFrame):
    """Small pop-out widget that allows you to enter a number."""

    def __init__(
        self,
        master: SmartFrame,
        initial_value=None,
        window_title="Editing Number",
        integers_only=False,
        width=16,  # characters
    ):
        super().__init__(toplevel=True, master=master, window_title=window_title)
        self.editor = master
        self.initial_text = "" if initial_value is None else str(initial_value)
        self.output = None
        self._width = width
        self._integers_only = integers_only

        self._entry = None

        self.build()

    def build(self):
        with self.set_master(auto_rows=0):
            self._entry = self.Entry(
                initial_text=self.initial_text,
                padx=20,
                pady=20,
                width=self._width,
                integers_only=self._integers_only,
                numbers_only=not self._integers_only,
            )
            with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={"padx": 10}):
                self.Button(
                    text="Confirm", command=lambda: self.done(True), **self.editor.DEFAULT_BUTTON_KWARGS["YES"]
                )
                self.Button(
                    text="Cancel", command=lambda: self.done(False), **self.editor.DEFAULT_BUTTON_KWARGS["NO"]
                )

        self.bind_all("<Escape>", lambda e: self.done(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.done(False))
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3), transient=True)

    def go(self) -> tp.Union[None, int, float]:
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def done(self, confirm=True):
        if confirm:
            new_text = self._entry.var.get()
            if new_text == self.initial_text:
                self.output = None
            else:
                try:
                    new_value = int(new_text)
                except ValueError:
                    self.CustomDialog("Invalid value", "Value must be an integer.")
                else:
                    self.output = new_value
        self.quit()


class TextEditBox(SmartFrame):
    """Small pop-out widget that allows you to modify longer strings more freely, with newlines and all."""

    def __init__(
        self,
        master: SmartFrame,
        initial_text="",
        allow_newlines=True,
        window_title="Editing Text",
        width=16,  # characters
        height=1,  # lines
    ):
        super().__init__(toplevel=True, master=master, window_title=window_title)
        self.editor = master
        self.initial_text = initial_text
        self.output = None
        self.allow_newlines = allow_newlines
        self._width = width
        self._height = height

        self._text = None

        self.build()

    def build(self):
        with self.set_master(auto_rows=0):
            self._text = self.TextBox(padx=20, pady=20, width=self._width, height=self._height)
            self._text.insert("end", self.initial_text)
            with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={"padx": 10}):
                self.Button(
                    text="Confirm", command=lambda: self.done(True), **self.editor.DEFAULT_BUTTON_KWARGS["YES"]
                )
                self.Button(
                    text="Cancel", command=lambda: self.done(False), **self.editor.DEFAULT_BUTTON_KWARGS["NO"]
                )

        self.bind_all("<Escape>", lambda e: self.done(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.done(False))
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
            new_text = self._text.get("1.0", "end" + "-1c")
            if not self.allow_newlines and "\n" in new_text:
                self.editor.CustomDialog("Text Error", "Entry cannot contain newlines.")
                return
            if new_text == self.initial_text:
                self.output = None
            else:
                self.output = new_text
        self.quit()


class EntryTextEditBox(TextEditBox):

    def __init__(
        self,
        master: BaseEditor,
        category,
        category_data,
        entry_id,
        initial_text="",
        allow_newlines=True,
        edit_entry_id=True,
        width=70,
        height=10,
    ):
        if entry_id is None and edit_entry_id:
            window_title = f"Adding entry to {camel_case_to_spaces(category)}"
        else:
            window_title = f"Editing {camel_case_to_spaces(category)}[{entry_id}]"
        self.category = category
        self.category_data = category_data
        self.entry_id = entry_id
        self._edit_entry_id = edit_entry_id
        self._id = None
        super().__init__(
            master=master,
            initial_text=initial_text,
            allow_newlines=allow_newlines,
            window_title=window_title,
            width=width,
            height=height,
        )
        self.output = [None, None]

    def build(self):
        with self.set_master(auto_rows=0):
            if self._edit_entry_id:
                self._id = self.Entry(
                    label="Entry ID:",
                    label_position="left",
                    width=10,
                    integers_only=True,
                    initial_text=self.entry_id if self.entry_id is not None else "",
                    padx=20,
                    pady=20,
                ).var
            else:
                self._id = None
            super().build()

    def done(self, confirm=True):
        if confirm:
            if self._id:
                if not self._id.get():
                    self.CustomDialog("ID Error", message="Entry ID must be set.")
                    return
                new_id = int(self._id.get())
                if new_id == self.entry_id:
                    new_id = None
            else:
                new_id = None
            new_text = self._text.get("1.0", "end" + "-1c")
            if not self.allow_newlines and "\n" in new_text:
                self.CustomDialog("Text Error", "Entry cannot contain newlines.")
                return
            if new_text == self.initial_text:
                new_text = None
            self.output = [new_id, new_text]
        self.quit()


class ItemTextEditBox(SmartFrame):
    WIDTH = 70  # characters
    DESCRIPTION_HEIGHT = 10  # lines

    def __init__(
        self, master: ProjectWindow, initial_name, initial_summary="", initial_description="", title="Editing Item Text"
    ):
        super().__init__(master=master, window_title=title)
        self.editor = master
        self.output = [initial_name, initial_summary, initial_description]
        self._name_entry = None
        self._summary_entry = None
        self._description_box = None

        self.build()

    def build(self):
        with self.set_master(auto_rows=0, padx=20, grid_defaults={"pady": 10, "sticky": "e"}):
            self._name_entry = self.Entry(initial_text=self.output[0], width=self.WIDTH, label="Name:")
            self._summary_entry = self.Entry(initial_text=self.output[1], width=self.WIDTH, label="Summary:")
            self._description_box = self.TextBox(
                width=self.WIDTH, height=self.DESCRIPTION_HEIGHT, label="Description:", label_position="above"
            )
            self._description_box.insert("end", self.output[2])
            with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={"padx": 10}):
                self.Button(
                    text="Confirm changes", command=lambda: self.done(True), **self.editor.DEFAULT_BUTTON_KWARGS["YES"]
                )
                self.Button(
                    text="Cancel changes", command=lambda: self.done(False), **self.editor.DEFAULT_BUTTON_KWARGS["NO"]
                )

        self.bind_all("<Escape>", lambda e: self.done(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.done(False))
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
            self.output[0] = self._name_entry.var.get()
            self.output[1] = self._summary_entry.var.get()
            self.output[2] = self._description_box.get("1.0", "end" + "-1c")
        self.quit()


class SequenceNameEditBox(SmartFrame):
    """Small pop-out widget that allows you to set the MSB entry names for a sequence.

    Pass it a list of valid names to get access to a selection box.
    """

    def __init__(
        self,
        master: SmartFrame,
        initial_names: tp.Sequence[str],
        valid_names: tp.Sequence[str] = None,
        window_title="Editing Sequence Names",
    ):
        super().__init__(toplevel=True, master=master, window_title=window_title)
        self.editor = master
        # Convert `None` names to empty strings.
        self._initial_names = ["" if name is None else name for name in initial_names]
        self._valid_names = valid_names
        self.output = None  # will be a list of names
        self._width = 50

        self._entries = []

        self.build()

    def build(self):
        with self.set_master(auto_rows=0, padx=10, grid_defaults={"padx": 5, "pady": 10}):
            for i, name in enumerate(self._initial_names):
                with self.set_master(auto_columns=0):
                    self._entries.append(
                        self.Entry(initial_text=name, width=self._width)
                    )
                    if self._valid_names:
                        self.Button(text="Choose Name", width=12, bg="#422", command=lambda i_=i: self.select_name(i_))
                    self.Button(text="Clear", width=6, bg="#422", command=lambda i_=i: self.clear_name(i_))
            with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={"padx": 10}):
                self.Button(
                    text="Confirm changes", command=lambda: self.done(True), **self.editor.DEFAULT_BUTTON_KWARGS["YES"]
                )
                self.Button(
                    text="Cancel changes", command=lambda: self.done(False), **self.editor.DEFAULT_BUTTON_KWARGS["NO"]
                )

        self.bind_all("<Escape>", lambda e: self.done(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.done(False))
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3), transient=True)

    def select_name(self, name_index: int):
        selected_name = NameSelectionBox(self.master, self._valid_names).go()
        if selected_name is not None:
            self._entries[name_index].var.set(selected_name)

    def clear_name(self, name_index: int):
        self._entries[name_index].var.set("")

    def go(self):
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def done(self, confirm=True):
        if confirm:
            new_names = [e.var.get() for e in self._entries]
            # Convert empty string names to `None`.
            output = [name if name else None for name in new_names]
            if output == self._initial_names:
                self.output = None  # no change
            self.output = output
        self.quit()


class GroupBitSetEditBox(SmartFrame):
    """Displays 128 or 256 checkbuttons to toggle for e.g. draw groups, display groups, navmesh groups."""

    def __init__(
        self,
        master: SmartFrame,
        initial_bit_set=None,
        bit_count=128,
        window_title="Editing Bit Groups",
    ):
        if bit_count not in {128, 256, 1024}:
            raise ValueError(f"`bit_count` must be 128, 256, or 1024, not {bit_count}.")
        super().__init__(toplevel=True, master=master, window_title=window_title)
        self.editor = master
        self.bit_count = bit_count
        self.initial_bit_set = initial_bit_set
        self.output = None
        self._checkbuttons = []

        self.build()

    def build(self):
        with self.set_master(auto_rows=0):
            with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={"padx": 10}):
                self.Button(
                    text="Enable All", command=self._enable_all,
                    **self.editor.DEFAULT_BUTTON_KWARGS["YES"]
                )
                self.Button(
                    text="Disable All", command=self._disable_all,
                    **self.editor.DEFAULT_BUTTON_KWARGS["NO"]
                )

            with self.set_master(padx=10, pady=10):

                # Calculate the number of rows and columns to use.
                if self.bit_count == 128:
                    row_count, col_count = 8, 16
                elif self.bit_count == 256:
                    row_count, col_count = 16, 16
                else:  # 1024
                    row_count, col_count = 32, 32  # TODO: maybe too many rows?

                for row in range(row_count):
                    for col in range(col_count):
                        i = row * col_count + col
                        self._checkbuttons.append(
                            self.Checkbutton(
                                initial_state=i in self.initial_bit_set,
                                label=str(i),
                                label_position="left",
                                row=row,
                                column=col,
                                selectcolor="#000",
                                command=lambda i_=i: self._checkbutton_toggle(i_),
                                sticky="e",
                            )
                        )
                        self._checkbutton_toggle(i)
            with self.set_master(auto_columns=0, padx=10, pady=10, grid_defaults={"padx": 10}):
                self.Button(
                    text="Confirm", command=lambda: self.done(True),
                    **self.editor.DEFAULT_BUTTON_KWARGS["YES"]
                )
                self.Button(
                    text="Cancel", command=lambda: self.done(False),
                    **self.editor.DEFAULT_BUTTON_KWARGS["NO"]
                )

        self.bind_all("<Escape>", lambda e: self.done(False))
        self.protocol("WM_DELETE_WINDOW", lambda: self.done(False))
        self.resizable(width=False, height=False)
        self.set_geometry(relative_position=(0.5, 0.3), transient=True)

    def go(self) -> tp.Optional[set[int]]:
        self.wait_visibility()
        self.grab_set()
        self.mainloop()
        self.destroy()
        return self.output

    def done(self, confirm=True):
        if confirm:
            output_bit_set = {i for i, checkbutton in enumerate(self._checkbuttons) if checkbutton.var.get()}
            if output_bit_set == self.initial_bit_set:
                self.output = None
            else:
                self.output = output_bit_set
        self.quit()

    def _enable_all(self):
        for checkbutton in self._checkbuttons:
            checkbutton.var.set(True)
            checkbutton.config(fg="#FFF")

    def _disable_all(self):
        for checkbutton in self._checkbuttons:
            checkbutton.var.set(False)
            checkbutton.config(fg="#555")

    def _checkbutton_toggle(self, i):
        """Modify appearance of Checkbutton when toggled."""
        checkbutton = self._checkbuttons[i]
        value = checkbutton.var.get()
        checkbutton.config(fg="#FFF" if value else "#555")
