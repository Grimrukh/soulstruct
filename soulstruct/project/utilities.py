from __future__ import annotations
import tkinter as tk
import typing as tp
from collections import namedtuple
from functools import wraps

from soulstruct.ai import DarkSoulsAIScripts
from soulstruct.core import SoulstructError
from soulstruct.maps import DarkSoulsMaps
from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.text import DarkSoulsText
from soulstruct.utilities import word_wrap, camel_case_to_spaces
from soulstruct.utilities.window import SmartFrame

if tp.TYPE_CHECKING:
    from soulstruct.project.editor import SoulstructBaseEditor

__all__ = [
    "SoulstructProjectError",
    "RestoreBackupError",
    "error_as_dialog",
    "TagData",
    "TextEditor",
    "NameSelectionBox",
    "TextEditBox",
    "EntryTextEditBox",
    "ItemTextEditBox",
    "ActionHistory",
    "ViewHistory",
    "bind_events",
    "data_type_caps",
    "DATA_TYPES",
]


class SoulstructProjectError(SoulstructError):
    pass


class RestoreBackupError(SoulstructError):
    pass


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


TagData = namedtuple("TagData", ("foreground", "pattern", "offsets"))


class TextEditor(tk.Text):
    TAGS = {}  # type: tp.Dict[str, TagData]

    def __init__(self, *args, **kwargs):
        """Text widget that uses some Tcl voodoo (courtesy of Tkinter wizard Bryan Oakley) to allow arbitrary callbacks
        whenever a 'mark', 'set', or 'insert' Tcl command occurs (e.g. updating a line number tracker).

        Also includes methods for scanning and tagging arbitrary regex patterns, which should be given in `cls.TAGS`.

        See: https://stackoverflow.com/a/13840728
        """
        super().__init__(*args, **kwargs)
        self.callback = None
        private_callback = self.register(self._callback)
        self.tk.eval(
            """
            proc widget_proxy {actual_widget callback args} {

                # this prevents recursion if the widget is called
                # during the callback
                set flag ::dont_recurse(actual_widget)

                # call the real tk widget with the real args
                set result [uplevel [linsert $args 0 $actual_widget]]

                # call the callback and ignore errors, but only
                # do so on inserts, deletes, and changes in the 
                # mark. Otherwise we'll call the callback way too 
                # often.
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

                # return the result from the real widget command
                return $result
            }
            """
        )
        self.tk.eval(
            """
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy _{widget} {callback}
        """.format(
                widget=str(self), callback=private_callback
            )
        )

        for tag_name, tag_data in self.TAGS.items():
            self.tag_configure(tag_name, foreground=tag_data.foreground)
        self.tag_configure("found", background="#224433")
        self.tag_configure("error", background="#443322")

        self.bind("<Tab>", self._tab_four_spaces)
        self.bind("<Home>", self._home_key)
        self.bind("<Control-slash>", self._toggle_comment)

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
        """Home key ignores starting whitespace, unless there's only whitespace."""
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


def data_type_caps(data_type):
    if data_type.lower() == "ai":
        return "AI"
    return data_type.capitalize()


DATA_TYPES = {
    "maps": DarkSoulsMaps,
    "params": DarkSoulsGameParameters,
    "lighting": DarkSoulsLightingParameters,
    "text": DarkSoulsText,
    "events": None,  # modified via EVS event script files
    "ai": DarkSoulsAIScripts,
    "talk": None,  # modified via ESP state machine script files
}


class NameSelectionBox(SmartFrame):
    """Small pop-out widget that allows you to select a name from some list."""

    WIDTH = 50  # characters
    HEIGHT = 20  # lines

    def __init__(self, master, names, list_name="List"):
        super().__init__(toplevel=True, master=master, window_title=f"Select Entry from {list_name}")

        self.output = None

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
        self.quit()


class TextEditBox(SmartFrame):
    """Small pop-out widget that allows you to modify longer strings more freely, with newlines and all."""

    WIDTH = 16  # characters
    HEIGHT = 1  # lines

    def __init__(self, master: SmartFrame, initial_text="", allow_newlines=True, window_title="Editing Text"):
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
            self._text.insert("end", self.initial_text)
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
    WIDTH = 70  # characters
    HEIGHT = 10  # lines

    def __init__(
        self,
        master: SoulstructBaseEditor,
        category,
        category_data,
        entry_id,
        initial_text="",
        allow_newlines=True,
        edit_entry_id=True,
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
            master=master, initial_text=initial_text, allow_newlines=allow_newlines, window_title=window_title
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

    def __init__(self, master, initial_name, initial_summary="", initial_description="", title="Editing Item Text"):
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
