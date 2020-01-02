"""
TODO:
    - Create Entities tab.
    - Search for all existing entities and color them, and hyperlink to Entities tab or Maps tab with right click?
    - Replace entity ID with entity name from Entities tab (which can in turn be auto-generated from Maps names).
"""

import re
from pathlib import Path
import tkinter as tk

from soulstruct.events.darksouls1 import EMEVD
from soulstruct.events.darksouls1.constants import VERBOSE_MAP_NAMES
from soulstruct.events.evs import EmevdError
from soulstruct.maps import DARK_SOULS_MAP_NAMES
from soulstruct.utilities.window import SoulstructSmartFrame


def _get_verbose_map_name(emevd_name):
    if emevd_name == "common":
        return "Common"
    area, block, _, version = re.match(r"m(\d+)_(\d+)_(\d+)_(\d+)", emevd_name).groups()
    return VERBOSE_MAP_NAMES[int(area), int(block)]


class EvsTextEditor(tk.Text):
    def __init__(self, *args, **kwargs):
        """Text widget that generates a "<CursorChange>" event when appropriate for event bindings and can highlight
        arbitrary text patterns.

        See:
            https://stackoverflow.com/a/23574537
            https://stackoverflow.com/a/3781773
        """
        super().__init__(*args, **kwargs)
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

        self.tag_configure("restart_type", foreground='#FFFFAA')
        self.tag_configure("event_def", foreground='#FFAAAA')
        self.tag_configure("docstring", foreground='#BBBBBB')
        self.tag_configure("instruction", foreground='#AAAAFF')
        self.tag_configure("low_level_test", foreground='#AAFFAA')  # starts with 'If', 'Skip', or 'Goto'
        self.tag_configure("func_arg_name", foreground='#FFCCAA')
        self.tag_configure("event_arg_name", foreground='#FFAAFF')

        self.tag_configure("found", background='#224433')
        self.tag_configure("error", background='#443322')

    def _proxy(self, *args):
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)
        if args[0] in ("insert", "delete") or args[0:3] == ("mark", "set", "insert"):
            self.event_generate("<<CursorChange>>", when="tail")

        return result

    def highlight_line(self, number, tag):
        """Apply the given tag to all text in the given line. Clears tag first."""
        self.tag_remove(tag, "1.0", "end")
        self.tag_add(tag, f"{number}.0 linestart", f"{number}.0 lineend")

    def highlight_pattern(self, pattern, tag, start="1.0", end="end", regexp=False, clear=True):
        """Apply the given tag to all text that matches the given pattern. Clears tag first by default.

        If 'regexp' is set to True, pattern will be treated as a regular expression according to Tcl's regular
        expression syntax.
        """
        if clear:
            self.tag_remove(tag, "1.0", "end")
        start = self.index(start)
        end = self.index(end)
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
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", f"{index}+{count.get()}c")
            self.tag_add(tag, "matchStart", "matchEnd")


class SoulstructEventEditor(SoulstructSmartFrame):

    TEXT_BG = '#232323'
    TEXT_BOX_WIDTH = 300

    def __init__(self, evs_directory, game_root, dcx, master=None, toplevel=False):
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct EMEVD Manager")
        self.evs_directory = Path(evs_directory)
        self.game_root = Path(game_root)
        self.dcx = dcx
        self.evs_file_paths = {}
        self.evs_text = {}
        self.selected_evs = None

        self.evs_choice = None
        self.line_number = None
        self.go_to_line = None
        self.find_string = None
        self.evs_editor_canvas = None
        self.evs_text_editor = None

        for evs_file_path in self.evs_directory.glob("*.evs.py"):
            evs_name = evs_file_path.name.split('.')[0]
            self.evs_file_paths[evs_name] = evs_file_path
            with evs_file_path.open('r', encoding='utf-8') as f:
                self.evs_text[evs_name] = f.read()

        with self.set_master(sticky='nsew', row_weights=[0, 1, 0, 0], column_weights=[1], auto_rows=0):
            self.build()

    def build(self):

        with self.set_master(sticky='nsew', row_weights=[1], column_weights=[1, 1, 1, 1], auto_columns=0):
            self.evs_choice = self.Combobox(
                values=(), initial_value="", width=30,
                on_select_function=self._on_evs_choice,
                label='Script:', label_font_size=12, label_position='left', font=('Segoe UI', 12), padx=10, pady=10)
            self.line_number = self.Label(
                text="Line: None", padx=10, width=10, fg='#CCF', anchor='w', sticky='w').var
            self.go_to_line = self.Entry(label="Go to Line:", padx=5, width=6, sticky='w')
            self.go_to_line.bind("<Return>", self._go_to_line)
            self.find_string = self.Entry(label="Find Text:", padx=5, width=20, sticky='w')
            self.find_string.bind("<Return>", self._find_string)

        with self.set_master(sticky='nsew', row_weights=[1], column_weights=[1, 0], padx=50, pady=10):
            self.evs_editor_canvas = self.Canvas(
                horizontal_scrollbar=True, sticky='nsew', bg='#232323',
                borderwidth=0, highlightthickness=0, column=0, row_weights=[1], column_weights=[1])
            editor_i_frame = self.Frame(self.evs_editor_canvas, sticky='nsew', row_weights=[1], column_weights=[1])
            self.evs_editor_canvas.create_window(0, 0, window=editor_i_frame, anchor='nw')

            self.evs_text_editor = self.CustomWidget(
                editor_i_frame, custom_widget_class=EvsTextEditor, set_style_defaults=('text', 'cursor'),
                width=300, height=50, wrap='word', bg='#232323', font=("Consolas", 10))
            vertical_scrollbar_w = self.Scrollbar(
                orient='vertical', command=self.evs_text_editor.yview, column=1, sticky='ns')
            self.evs_text_editor.config(bd=0, yscrollcommand=vertical_scrollbar_w.set)
            self.link_to_scrollable(self.evs_text_editor, editor_i_frame)

            def _update_textbox_height(e):
                font_size = int(self.evs_text_editor['font'].split()[1])
                self.evs_text_editor['height'] = e.height // (font_size * 1.5)  # 1.5 line spacing

            self.evs_editor_canvas.bind("<Configure>", lambda e: _update_textbox_height(e))

            def _update_line_number(_):
                current_line = self.evs_text_editor.index('insert').split('.')[0]
                self.line_number.set(f"Line: {current_line}")

            self.evs_text_editor.bind("<<CursorChange>>", _update_line_number)

        with self.set_master(auto_columns=0, pady=(10, 0), sticky='n'):
            self.Button(text="Save EVS", width=15, command=self._save_evs)
            self.Button(text="Validate EVS", width=15, padx=(30, 30), command=self._check_syntax)
            self.Button(text="Reload EVS", width=15, command=self._reload_selected)

        with self.set_master(auto_columns=0, pady=10, sticky='n'):
            self.Button(text="Save & Export", width=15, padx=(0, 15), bg='#822', command=self._save_and_export)
            self.Button(text="Reload & Export", width=15, padx=(15, 0), bg='#822', command=self._reload_and_export)

        self.refresh()

    def refresh(self):
        map_options = [f"{m} ({_get_verbose_map_name(m)})" for m in self.evs_file_paths]
        self.evs_choice["values"] = map_options
        if map_options:
            self.evs_choice.var.set(map_options[0])
            self.selected_evs = self.evs_choice.get().split(' (')[0]
            self.evs_text_editor.insert(1.0, self.evs_text[self.selected_evs])
            self.evs_text_editor.mark_set("insert", "1.0")
            self.color_syntax()

    def _go_to_line(self, _):
        number = self.go_to_line.var.get()
        if not number:
            return
        number = int(number)
        if number < 1 or int(self.evs_text_editor.index('end-1c').split('.')[0]) < number:
            self._flash_red_bg(self.go_to_line)
            return
        self.evs_text_editor.mark_set("insert", f"{number}.0")
        self.evs_text_editor.see(f"{number}.0")
        self.evs_text_editor.highlight_line(number, "found")

    def _find_string(self, _):
        string = self.find_string.var.get()
        if not string:
            return
        start_line, start_char = self.evs_text_editor.index("insert").split('.')
        index = self.evs_text_editor.search(string, index=f"{start_line}.{int(start_char) + 1}")

        self.clear_bg_tags()
        self.evs_text_editor.mark_set("insert", index)
        self.evs_text_editor.see(index)
        index_line, index_char = index.split('.')
        self.evs_text_editor.tag_add("found", index, f"{index_line}.{int(index_char) + len(string)}")

    def clear_bg_tags(self):
        for tag in {"found", "error"}:
            self.evs_text_editor.tag_remove(tag, "1.0", "end")

    def color_syntax(self):
        for tag in {"event_def", "instruction", "low_level_test"}:
            self.evs_text_editor.tag_remove(tag, "1.0", "end")

        self.evs_text_editor.highlight_pattern(r"^@[\w_]+", tag="restart_type", regexp=True)
        self.evs_text_editor.highlight_pattern(r"^def [\w\d_]+", tag="event_def", regexp=True)
        self.evs_text_editor.highlight_pattern(r"^[ ]+\"\"\" [\w\d :]+ \"\"\"", tag="docstring", regexp=True)
        self.evs_text_editor.highlight_pattern(r"^[ ]+[\w\d_]+", tag="instruction", regexp=True)
        self.evs_text_editor.highlight_pattern(r"^[ ]+(If|Skip|Goto)[\w\d_]+", tag="low_level_test", regexp=True)
        self.evs_text_editor.highlight_pattern(r"[\w\d_]+[ ]*(?=\=)", tag="func_arg_name", regexp=True)

        # Get all event arg names (e.g. "arg_0_3") and color them.
        self.evs_text_editor.tag_remove("event_arg_name", "1.0", "end")
        start_index = "1.0"
        while 1:
            def_index = self.evs_text_editor.search(r"^def [\w\d_]+\(", start_index, regexp=True)
            next_def_index = self.evs_text_editor.search(r"^def [\w\d_]+\(", f"{def_index} lineend", regexp=True)
            if int(next_def_index.split('.')[0]) <= int(def_index.split('.')[0]):
                break  # finished searching
            event_text = self.evs_text_editor.get(def_index, next_def_index)
            event_args_match = re.match(r"^def [\w\d_]+\(([\w\d_:, \n]+)\)", event_text, flags=re.MULTILINE)
            if event_args_match:
                event_args = event_args_match.group(1).replace('\n', '').replace(' ', '')
                for event_arg in event_args.split(','):
                    parts = event_arg.split(':')
                    if len(parts) == 2:
                        arg_name, arg_type = parts
                    else:
                        arg_name, arg_type = parts[0], None
                    self.evs_text_editor.highlight_pattern(
                        arg_name, tag="event_arg_name", start=def_index, end=next_def_index, clear=False)
            start_index = next_def_index

    def _flash_red_bg(self, widget):
        widget['bg'] = '#522'
        self.after(200, lambda: widget.config(bg=self.STYLE_DEFAULTS['bg']))

    def _ignored_unsaved(self):
        if self._get_current_text() != self.evs_text[self.selected_evs]:
            if self.dialog(title="Lose Unsaved Changes?",
                           message="Current text has changed but not been saved. Lose changes?",
                           button_names=("Yes, lose changes", "No, stay here"),
                           button_kwargs=('YES', 'NO'),
                           cancel_output=1, default_output=1) == 1:
                return False
        return True

    def _on_evs_choice(self, _):
        """Check if current text has changed (and warn), then switch to other text."""
        if self._ignored_unsaved():
            self.selected_evs = self.evs_choice.var.get().split(' (')[0]
            self.evs_text_editor.delete(1.0, 'end')
            self.evs_text_editor.insert(1.0, self.evs_text[self.selected_evs])
            self.evs_text_editor.mark_set("insert", "1.0")
            self.color_syntax()
        else:
            self.evs_choice.var.set(f"{self.selected_evs} ({DARK_SOULS_MAP_NAMES[self.selected_evs]})")  # keep previous

    def _save_evs(self):
        current_text = self._get_current_text()
        self.evs_text[self.selected_evs] = current_text
        with self.evs_file_paths[self.selected_evs].open('w', encoding='utf-8') as f:
            f.write(current_text)

    def _raise_error(self, lineno=None, message=None):
        if lineno:
            self.evs_text_editor.mark_set("insert", f"{lineno}.0")
            self.evs_text_editor.see(f"{lineno}.0")
            self.evs_text_editor.highlight_line(lineno, "error")
        if message:
            self.error_dialog(
                "EVS Error",
                f"Error encountered when trying to parse EVS script (see console for full traceback):\n\n"
                f"{message}")

    def _check_syntax(self):
        self.color_syntax()
        try:
            EMEVD(self._get_current_text())
        except EmevdError as e:
            self._raise_error(e.lineno, str(e))
        except Exception as e:
            lineno_match = re.search(r"line (\d+)", str(e))
            if lineno_match:
                self._raise_error(lineno_match.group(1), str(e))
            else:
                self._raise_error(message=str(e))
        else:
            self.evs_text_editor.tag_remove("error", "1.0", "end")
            self.info_dialog("EVS Success", "No errors encountered when parsing EVS.")

    def _export_evs(self):
        """Convert project EVS file to game EMEVD file. Does not check any loaded text."""
        try:
            emevd = EMEVD(self.evs_file_paths[self.selected_evs])
        except Exception as e:
            return self.error_dialog(
                "EVS Error", f"Could not interpret current EVS file in project.\n"
                             f"Fix this error and try again (see console for full traceback):\n\n{str(e)}")
        emevd.write_emevd(self.game_root / f"event/{self.selected_evs}.emevd{'.dcx' if self.dcx else ''}", dcx=self.dcx)

    def _reload_selected(self):
        if self._ignored_unsaved():
            evs_path = self.evs_file_paths[self.selected_evs]
            with evs_path.open('r', encoding='utf-8') as f:
                self.evs_text[self.selected_evs] = f.read()
            self.evs_text_editor.delete(1.0, 'end')
            self.evs_text_editor.insert(1.0, self.evs_text[self.selected_evs])
            self.evs_text_editor.mark_set("insert", "1.0")
            self.color_syntax()

    def _save_and_export(self):
        self._save_evs()
        self._export_evs()

    def _reload_and_export(self):
        self._reload_selected()
        self._export_evs()

    def _get_current_text(self):
        """Get all current text from TextBox, minus final newline (added by Tk)."""
        return self.evs_text_editor.get(1.0, 'end')[:-1]
