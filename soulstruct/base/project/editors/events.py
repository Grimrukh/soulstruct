"""
TODO:
    - Search for all existing entities and color them, and hyperlink to Entities tab or Maps tab with right click?
"""
from __future__ import annotations

__all__ = ["EventsEditor"]

import logging
import re
import typing as tp
from pathlib import Path
from tkinter import TclError

from soulstruct.base.events.emevd.evs import EVSError
from soulstruct.base.project import GameDirectoryProject, ProjectDataType
from soulstruct.base.project.utilities import TagData, TkTextEditor
from soulstruct.utilities.window import SmartFrame

from .. import editor_config

if tp.TYPE_CHECKING:
    from soulstruct.base.events.event_directory import EventDirectory

_LOGGER = logging.getLogger(__name__)


class EVSTkTextEditor(TkTextEditor):

    TAGS = {
        "on_rest_behavior": TagData("#FFFFAA", r"^@[\w_]+", (0, 0)),
        "python_word": TagData(
            "#FF7F50",
            r"(^| )(class|def|if|and|or|not|elif|else|return|import|from|for|True|False|await)(\n| |:)",
            (0, 1),
        ),
        "true_false": TagData("#FF7F50", r"[ =](True|False)(,|\n| |:|\))", (1, 1)),
        "event_def": TagData("#FF6980", r"^def [\w_]+", (4, 0)),
        "import": TagData("#FFAAAA", r"^(from|import) [\w_ .*]+", (0, 0)),
        "instruction_or_high_level_test": TagData("#E6C975", r"[ \(][\w_]+(?=\()", (1, 0)),
        "low_level_test": TagData("#AAAAFF", r"^ +(If|Skip|Goto)[\w_]+", (0, 0)),
        "if_main_condition": TagData("#FF3355", r"^ +If[\w_]+(?=[(]0 *,)", (0, 0)),
        "main_condition": TagData("#FF3355", r"^ +MAIN\.Await\(", (0, 1)),
        "await_statement": TagData("#FF3355", r" await ", (0, 0)),
        "named_arg": TagData("#AAFFFF", r"[(,=\|][ \n]*(?!False)(?!True)\w[\w.]* *[,)\|]", (1, 1)),
        "func_arg_name": TagData("#FFCCAA", r"[\w_]+ *(?=\=)", (0, 0)),
        "event_arg_name": TagData("#FFAAFF", r"^def [\w_]+\(([\w_:, \n]+)\)", None),
        "number_literal": TagData("#AADDFF", r"[ ,=({\[-][\d.]+(?=($|[ ,:)}\]]))", (1, 0)),
        "and_or_condition": TagData("#AAAAFF", r"[ \(] *(AND|OR)_[\d]+(\.Add)?", (1, 0)),
        "comment": TagData("#777777", r"#.*$", (0, 0)),
        "docstring": TagData("#00ABA9", r"^ +\"\"\"[\w\n :.]+\"\"\"", (0, 0)),
        "module_docstring": TagData("#00ABA9", r'^"""(.|\n)*"""', (0, 0)),
    }

    def color_syntax(self, start="1.0", end="end"):
        super().color_syntax(start, end)
        self._apply_event_arg_name_tags()

    def _apply_event_arg_name_tags(self):
        """Get all event arg names (e.g. "arg_0_3") and color them."""
        self.tag_remove("event_arg_name", "1.0", "end")
        start_index = "1.0"
        while True:
            def_index = self.search(r"^def [\w_]+\(", start_index, regexp=True)
            if not def_index:
                break
            next_def_index = self.search(r"^def [\w_]+\(", f"{def_index} lineend", regexp=True)
            if int(next_def_index.split(".")[0]) <= int(def_index.split(".")[0]):
                break  # finished searching
            event_text = self.get(def_index, next_def_index)
            event_args_match = re.match(self.TAGS["event_arg_name"].pattern, event_text, flags=re.MULTILINE)
            if event_args_match:
                event_args = event_args_match.group(1).replace("\n", "").replace(" ", "")
                for event_arg in event_args.split(","):
                    if event_arg == "_":
                        continue  # don't recolor `slot` underscore argument
                    parts = event_arg.split(":")
                    if len(parts) == 2:
                        arg_name, arg_type = parts
                    else:
                        arg_name, arg_type = parts[0], None
                    self.highlight_pattern(
                        arg_name, tag="event_arg_name", start=def_index, end=next_def_index, clear=False
                    )
            start_index = next_def_index


class EventsEditor(SmartFrame):
    DATA_NAME = "Events"
    TAB_NAME = "events"
    TEXT_BG = "#232323"
    TEXT_BOX_WIDTH = 300

    CONFIG = editor_config

    events: EventDirectory

    def __init__(
        self,
        project: GameDirectoryProject,
        evs_directory,
        game_root,
        global_map_choice_func,
        text_font_size=14,
        master=None,
        toplevel=False,
    ):
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct EMEVD Manager")
        self._project = project
        self.evs_directory = Path(evs_directory)
        self.game_root = Path(game_root)
        self.global_map_choice_func = global_map_choice_func
        self.text_font_size = text_font_size
        self.evs_file_paths = {}
        self.evs_text = {}
        self.selected_map_id = None

        self.map_choice = None
        self.line_number = None
        self.go_to_line = None
        self.string_to_find = None
        self.evs_editor_canvas = None
        self.text_editor = None
        self.compile_button = None
        self.reload_button = None

        self.scan_evs_files()

        with self.set_master(sticky="nsew", row_weights=[0, 1, 0, 0], column_weights=[1], auto_rows=0):
            self.build()

        self.bind_to_all_children("<Control-C>", lambda _: self._compile_selected(mimic_click=True))
        self.bind_to_all_children("<Control-r>", lambda _: self.reload_selected(mimic_click=True))

        self.refresh()

    def build(self):

        with self.set_master(sticky="nsew", row_weights=[1], column_weights=[1, 1, 1, 1], auto_columns=0):
            self.map_choice = self.Combobox(
                values=(),
                initial_value="",
                width=55,
                on_select_function=self.on_map_choice,
                sticky="w",
                label="Map:",
                label_position="left",
                font=self.CONFIG.REGULAR_FONT,
                padx=10,
                pady=10,
            )
            self.line_number = self.Label(text="Line: None", padx=10, width=10, fg="#CCF", anchor="w", sticky="w").var
            self.go_to_line = self.Entry(label="Go to Line:", padx=5, width=6, sticky="w")
            self.go_to_line.bind("<Return>", self._go_to_line)
            self.string_to_find = self.Entry(label="Find Text:", padx=5, width=20, sticky="w")
            self.string_to_find.bind("<Return>", self._find_string)

        with self.set_master(sticky="nsew", row_weights=[1], column_weights=[1, 0], padx=50, pady=10):
            self.evs_editor_canvas = self.Canvas(
                horizontal_scrollbar=True,
                sticky="nsew",
                bg="#232323",
                borderwidth=0,
                highlightthickness=0,
                column=0,
                row_weights=[1],
                column_weights=[1],
            )
            editor_i_frame = self.Frame(self.evs_editor_canvas, sticky="nsew", row_weights=[1], column_weights=[1])
            self.evs_editor_canvas.create_window(0, 0, window=editor_i_frame, anchor="nw")
            editor_i_frame.bind("<Configure>", lambda e, c=self.evs_editor_canvas: self.reset_canvas_scroll_region(c))

            self.text_editor = self.CustomWidget(
                editor_i_frame,
                custom_widget_class=EVSTkTextEditor,
                set_style_defaults=("text", "cursor"),
                width=300,
                height=50,
                wrap="word",
                bg="#232323",
                font=("Consolas", self.text_font_size),
            )
            vertical_scrollbar_w = self.Scrollbar(
                orient="vertical", command=self.text_editor.yview, column=1, sticky="ns"
            )
            self.text_editor.config(bd=0, yscrollcommand=vertical_scrollbar_w.set)
            self.link_to_scrollable(self.text_editor, editor_i_frame)

            def _update_textbox_height(e):
                font_size = int(self.text_editor["font"].split()[1])
                self.text_editor["height"] = e.height // (font_size * 1.5)  # 1.5 line spacing

            self.evs_editor_canvas.bind("<Configure>", lambda e: _update_textbox_height(e))

            self.text_editor.set_callback(self._update_line_number)
            self.text_editor.bind("<Control-f>", self._control_f_search)

        with self.set_master(auto_columns=0, pady=10, column_weights=[1, 1, 1], sticky="n"):
            self.compile_button = self.Button(
                text="Save & Compile",
                width=17,
                padx=5,
                command=self._compile_selected,
                tooltip_text="Save script, then compile it to test syntax. Text will flash blue if test is successful. "
                "(Ctrl + Shift + C)",
            )
            self.reload_button = self.Button(
                text="Reload Script",
                width=17,
                padx=5,
                command=self.reload_selected,
                tooltip_text="Reload script from project. Unsaved changes to current script will be lost. (Ctrl + R)",
            )
            self.Button(
                text="Reload & Export",
                width=17,
                padx=5,
                bg="#822",
                command=self.reload_and_export,
                tooltip_text="Reload script from project, then immediately export it to game.",
            )

    @property
    def events_class(self) -> tp.Type[EventDirectory]:
        return self._project.get_data_class(ProjectDataType.Events)

    def scan_evs_files(self):
        """Detect all EVS files in project event directory."""

        # Check for `common_func.py` first, which does not use EVS extension (for importing purposes).
        common_func_path = self.evs_directory / "common_func.py"
        if common_func_path.is_file():
            self.evs_file_paths["common_func"] = common_func_path
            with common_func_path.open("r", encoding="utf-8") as f:
                self.evs_text["common_func"] = f.read()

        # Search for all `evs.py` files.
        # TODO: Extension should be modifiable, surely?
        for evs_file_path in self.evs_directory.glob("*.evs.py"):
            if evs_file_path.name.startswith("_"):
                # Ignore files starting with an underscore.
                continue
            evs_name = evs_file_path.name.split(".")[0]
            self.evs_file_paths[evs_name] = evs_file_path
            with evs_file_path.open("r", encoding="utf-8") as f:
                self.evs_text[evs_name] = f.read()

    def refresh(self):
        game_maps = [self.events_class.GET_MAP(m) for m in self.evs_file_paths]
        map_options = [f"{game_map.emevd_file_stem} [{game_map.verbose_name}]" for game_map in game_maps]
        self.map_choice["values"] = map_options
        if map_options:
            self.map_choice.var.set(map_options[0])
            self.selected_map_id = self.map_choice.get().split(" [")[0]
            self.text_editor.delete(1.0, "end")
            self.text_editor.insert(1.0, self.evs_text[self.selected_map_id])
            self.text_editor.mark_set("insert", "1.0")
            self.text_editor.color_syntax()

    def _update_line_number(self, *_):
        current_line = self.text_editor.index("insert").split(".")[0]
        self.line_number.set(f"Line: {current_line}")

    def _control_f_search(self, _):
        if self.selected_map_id:
            try:
                highlighted = self.text_editor.selection_get()
            except TclError:  # just focus on search box
                self.string_to_find.focus_force()
            else:
                self.string_to_find.var.set(highlighted)
                self.string_to_find.select_range(0, "end")
                self.string_to_find.icursor("end")
                self.string_to_find.focus_force()

    def _go_to_line(self, _):
        number = self.go_to_line.var.get()
        if not number:
            return
        number = int(number)
        if not self.selected_map_id or number < 1 or int(self.text_editor.index("end-1c").split(".")[0]) < number:
            self.flash_bg(self.go_to_line)
            return
        self.text_editor.mark_set("insert", f"{number}.0")
        self.text_editor.see(f"{number}.0")
        self.text_editor.highlight_line(number, "found")

    def _find_string(self, _):
        string = self.string_to_find.var.get()
        if not string or not self.selected_map_id:
            return
        start_line, start_char = self.text_editor.index("insert").split(".")
        index = self.text_editor.search(string, index=f"{start_line}.{int(start_char) + 1}")

        if index:
            self.clear_bg_tags()
            self.text_editor.mark_set("insert", index)
            self.text_editor.see(index)
            index_line, index_char = index.split(".")
            self.text_editor.tag_add("found", index, f"{index_line}.{int(index_char) + len(string)}")
        else:
            self.flash_bg(self.string_to_find)

    def clear_bg_tags(self):
        for tag in {"found", "error"}:
            self.text_editor.tag_remove(tag, "1.0", "end")

    def _ignored_unsaved(self):
        if self._get_current_text() != self.evs_text[self.selected_map_id]:
            if (
                self.CustomDialog(
                    title="Lose Unsaved Changes?",
                    message="Current text has changed but not been saved. Lose changes?",
                    button_names=("Yes, lose changes", "No, stay here"),
                    button_kwargs=("YES", "NO"),
                    cancel_output=1,
                    default_output=1,
                )
                == 1
            ):
                return False
        return True

    def on_map_choice(self, event=None):
        """Check if current text has changed (and warn), then switch to other text."""
        if not self._ignored_unsaved():
            game_map = self.events_class.GET_MAP(self.selected_map_id)
            self.map_choice.var.set(f"{game_map.emevd_file_stem} [{game_map.verbose_name}]")
            return
        self.selected_map_id = self.map_choice.var.get().split(" [")[0]
        if self.global_map_choice_func and event is not None:
            self.global_map_choice_func(self.selected_map_id, ignore_tabs=("events",))
        self.text_editor.delete(1.0, "end")
        self.text_editor.insert(1.0, self.evs_text[self.selected_map_id])
        self.text_editor.mark_set("insert", "1.0")
        self.text_editor.color_syntax()

    def save_selected_evs(self):
        if self.selected_map_id:
            self.text_editor.color_syntax()
            current_text = self._get_current_text()
            self.evs_text[self.selected_map_id] = current_text
            with self.evs_file_paths[self.selected_map_id].open("w", encoding="utf-8") as f:
                f.write(current_text)

    def save_all_evs(self):
        """Updates the current script, then saves all EVS scripts to 'events' project subdirectory."""
        # TODO: Use `self.events` directory class.
        if self.selected_map_id:
            current_text = self._get_current_text()
            self.evs_text[self.selected_map_id] = current_text
        for evs_name, text in self.evs_text.items():
            evs_file_path = self.evs_file_paths[evs_name]
            with evs_file_path.open("w", encoding="utf-8") as f:
                f.write(text)

    def _raise_error(self, lineno=None, message=None):
        if lineno:
            self.text_editor.mark_set("insert", f"{lineno}.0")
            self.text_editor.see(f"{lineno}.0")
            self.text_editor.highlight_line(lineno, "error")
        if message:
            self.CustomDialog(
                "EVS Error",
                f"Error encountered when trying to parse EVS script (see console for full traceback):\n\n" f"{message}",
            )

    def _compile_selected(self, mimic_click=False, flash_bg=True):
        if not self.selected_map_id:
            return
        self.save_selected_evs()
        if mimic_click:
            self.mimic_click(self.compile_button)
        try:
            # Simply attempts to parse the EVS into EMEVD; the result is not used.
            self.events_class.FILE_CLASS.from_evs_string(
                evs_string=self._get_current_text(),
                map_name=self.selected_map_id,
                script_directory=str(self.evs_file_paths[self.selected_map_id].parent)
            )
        except EVSError as ex:
            self._raise_error(ex.lineno, str(ex))
        except Exception as ex:
            lineno_match = re.search(r"line (\d+)", str(ex))
            if lineno_match:
                self._raise_error(lineno_match.group(1), str(ex))
            else:
                self._raise_error(message=str(ex))
        else:
            self.text_editor.tag_remove("error", "1.0", "end")
            if flash_bg:
                self.flash_bg(self.text_editor, "#224")

    def export_selected_evs(self, export_directory=None):
        """Convert project EVS file to game EMEVD file. Does not check any loaded text."""
        # TODO: Update `self.events`?
        if not self.selected_map_id:
            return
        if export_directory is None:
            export_directory = self.FileDialog.askdirectory(initialdir=str(self.evs_directory))
            if export_directory is None:
                return
        export_directory = Path(export_directory)
        try:
            emevd = self.events_class.FILE_CLASS.from_evs_string(
                evs_string=self.evs_file_paths[self.selected_map_id],
                map_name=self.selected_map_id,
                script_directory=str(self.evs_file_paths[self.selected_map_id].parent),
            )
        except Exception as ex:
            _LOGGER.exception("Could not interpret current EVS file in project.")
            return self.CustomDialog(
                "EVS Error",
                f"Could not interpret current EVS file in project.\n"
                f"Fix this error and try again (see console/log for full traceback):\n\n{str(ex)}",
            )
        emevd.write(export_directory / f"event/{self.selected_map_id}.emevd")

    def reload_selected(self, mimic_click=False, flash_bg=True):
        if not self.selected_map_id:
            return
        if mimic_click:
            self.mimic_click(self.reload_button)
        if self._ignored_unsaved():
            evs_path = self.evs_file_paths[self.selected_map_id]
            with evs_path.open("r", encoding="utf-8") as f:
                self.evs_text[self.selected_map_id] = f.read()
            self.text_editor.delete(1.0, "end")
            self.text_editor.insert(1.0, self.evs_text[self.selected_map_id])
            self.text_editor.mark_set("insert", "1.0")
            self.text_editor.color_syntax()
            if flash_bg:
                self.flash_bg(self.text_editor, "#242")

    def save_and_export(self):
        self.save_selected_evs()
        self.export_selected_evs(self.game_root)

    def reload_and_export(self):
        self.reload_selected()
        self.export_selected_evs(self.game_root)

    def _get_current_text(self):
        """Get all current text from TextBox, minus final newline (added by Tk)."""
        return self.text_editor.get(1.0, "end")[:-1]
