from __future__ import annotations

import logging
import os
import re
import typing as tp
from pathlib import Path

from soulstruct.base.ezstate.esd.exceptions import ESDScriptError
from soulstruct.base.project.editors.base_editor import BaseEditor, EntryRow
from soulstruct.base.project.utilities import bind_events, TagData, TextEditor

if tp.TYPE_CHECKING:
    from soulstruct.base.ezstate.talk_directory import TalkDirectory

__all__ = ["TalkEditor"]
_LOGGER = logging.getLogger(__name__)
_TALK_ESP_MATCH = re.compile(r"^t(\d+)\.esp\.py$")


class ESPTextEditor(TextEditor):
    TAGS = {
        "import": TagData("#FFAAAA", r"^(from|import) [\w\d_ .*]+", (0, 0)),
        "python_word": TagData(
            "#FF7F50", r"(^| )(class|def|if|and|or|elif|else|return|import|from|for|True|False)(\n| |:)", (0, 1)
        ),
        "test_func": TagData("#B2D8B2", r"[ (][\w\d_]+(?=\()", (1, 0)),
        "basic_arg": TagData("#888888", r"\((State|self)(?=\))", (1, 0)),
        "state_def": TagData("#FF6980", r"^class [\w\d_]+", (6, 0)),
        "state_name": TagData("#CCCCDD", r"[ ,\[]State_\d+[ ,\]]", (1, 1)),
        "state_name_endline": TagData("#CCCCDD", r"[ ,\[]State_\d+$", (1, 0)),
        "method_def": TagData("#F6D985", r" def (previous_states|enter|test|exit)(?=\()", (5, 0)),
        "command": TagData("#82B882", r"^ +[\w\d_]+(?=\()", (0, 0)),
        "keyword": TagData("#FF7878", r"(, |\w\()[\w\d_]+(?=\=)", (2, 0)),
        "number_literal": TagData("#AADDFF", r"[ ,=({\[-][\d.]+(?=($|[ ,:)}\]]))", (1, 0)),
        "string_arg": TagData("#B2D8B2", r"='[\w\d_ ]+'", (1, 0)),
        "comment": TagData("#00ABA9", r"#.*$", (0, 0)),
        "docstring": TagData("#00ABA9", r'^[ ]+"""[\w\d\n :.]+"""', (0, 0)),
        "module_docstring": TagData("#00ABA9", r'^"""(.|\n)*"""', (0, 0)),
    }


class TalkEntryRow(EntryRow):
    """Container/manager for widgets of a single entry row in the Editor."""

    ENTRY_ANCHOR = "center"
    ENTRY_ROW_HEIGHT = 30
    EDIT_ENTRY_ID = True
    ENTRY_ID_WIDTH = 15
    ENTRY_ID_FG = "#CDF"

    # noinspection PyMissingConstructor
    def __init__(self, editor: TalkEditor, row_index: int, main_bindings: dict = None):
        self.master = editor
        self.STYLE_DEFAULTS = editor.STYLE_DEFAULTS

        self.row_index = row_index
        self._entry_id = None
        self._entry_text = None  # never changes
        self._active = False

        bg_color = self._get_color()

        self.row_box = editor.Frame(
            width=self.ENTRY_ID_WIDTH,
            height=self.ENTRY_ROW_HEIGHT,
            bg=bg_color,
            row=row_index,
            columnspan=3,
            sticky="nsew",
        )
        bind_events(self.row_box, main_bindings)

        self.id_box = editor.Frame(row=row_index, column=1, bg=bg_color, sticky="ew")
        self.id_label = editor.Label(
            self.id_box,
            text="",
            width=self.ENTRY_ID_WIDTH,
            bg=bg_color,
            fg=self.ENTRY_ID_FG,
            font_size=11,
            sticky="e",
        )
        id_bindings = main_bindings.copy()
        id_bindings["<Button-1>"] = lambda _, i=row_index: self.master.select_entry_row_index(i, id_clicked=True)
        # id_bindings["<Shift-Button-1>"] = lambda _, i=row_index: self.master.popout_entry_id_edit(i)
        bind_events(self.id_box, id_bindings)
        bind_events(self.id_label, id_bindings)

        self.context_menu = editor.Menu(self.row_box)

        self.tool_tip = None

    def update_entry(self, entry_id: int, entry_text=None):
        self.entry_id = entry_id
        self._update_colors()
        self.build_entry_context_menu()

    def hide(self):
        """Called when this row has no entry to display."""
        self.row_box.grid_remove()
        self.id_box.grid_remove()
        self.id_label.grid_remove()

    def unhide(self):
        self.row_box.grid()
        self.id_box.grid()
        self.id_label.grid()

    def build_entry_context_menu(self):
        self.context_menu.delete(0, "end")
        self.context_menu.add_command(
            label="Duplicate Entry to Next ID",
            command=lambda: self.master.add_relative_entry(self.entry_id, offset=1),
        )
        self.context_menu.add_command(
            label="Delete Entry",
            command=lambda: self.master.delete_entry(self.row_index),
        )

    @property
    def _colored_widgets(self):
        return self.row_box, self.id_box, self.id_label


class TalkEditor(BaseEditor):
    DATA_NAME = "Talk"
    TAB_NAME = "talk"
    CATEGORY_BOX_WIDTH = 0
    ENTRY_BOX_WIDTH = 126
    ENTRY_BOX_HEIGHT = 400
    ENTRY_RANGE_SIZE = 200

    ENTRY_ROW_CLASS = TalkEntryRow
    entry_rows: list[TalkEntryRow]

    def __init__(
        self,
        project,
        esp_directory: tp.Union[str, Path],
        global_map_choice_func: tp.Callable,
        text_font_size=10,
        linker=None,
        master=None,
        toplevel=False,
    ):
        self.esp_directory = Path(esp_directory)
        self.global_map_choice_func = global_map_choice_func
        self.text_font_size = text_font_size
        self.selected_map_id = ""
        self.esp_file_paths = {}
        self.esp_text = {}  # updated at the same time as files; used to check for unsaved changes

        self.map_choice = None
        self.reload_all_button = None
        self.line_number = None
        self.go_to_line = None
        self.string_to_find = None
        self.state_to_find = None
        self.esp_editor_canvas = None
        self.esp_editor = None  # type: tp.Optional[ESPTextEditor]
        self.compile_button = None
        self.reload_button = None

        self._project = project  # needed before refresh
        self.refresh()

        super().__init__(project, linker, master=master, toplevel=toplevel, window_title="Soulstruct Talk Editor")

    @property
    def talk(self) -> TalkDirectory:
        return self._project.talk

    def refresh(self):
        """Reloads all ESP files from all maps."""
        self.esp_file_paths = {}
        self.esp_text = {}
        for map_directory in self.esp_directory.glob("*"):
            try:
                game_map = self.talk.GET_MAP(map_directory.name)
            except ValueError:
                _LOGGER.warning(
                    f"Unexpected folder found in project '/talk' directory and ignored: " f"{map_directory.name}"
                )
                continue
            for esp_path in map_directory.glob("*.esp.py"):
                talk_match = _TALK_ESP_MATCH.match(esp_path.name)
                if not talk_match:
                    _LOGGER.warning(f"Invalid ESP file found and ignored: {str(esp_path)}")
                    continue
                talk_id = int(talk_match.group(1))
                self.esp_file_paths.setdefault(game_map.esd_file_stem, {})[talk_id] = esp_path
                with esp_path.open(mode="r", encoding="utf-8") as f:
                    self.esp_text.setdefault(game_map.esd_file_stem, {})[talk_id] = f.read()

    def refresh_categories(self):
        pass  # Unused.

    def build(self):
        with self.set_master(sticky="nsew", row_weights=[0, 1], column_weights=[1], auto_rows=0):
            with self.set_master(pady=10, sticky="w", row_weights=[1], column_weights=[1, 1], auto_columns=0):
                map_display_strings = [
                    f"{game_map.esd_file_stem} [{game_map.verbose_name}]"
                    for game_map in self.talk.ALL_MAPS
                    if game_map.esd_file_stem
                ]
                self.map_choice = self.Combobox(
                    values=map_display_strings,
                    label="Map:",
                    label_font_size=12,
                    label_position="left",
                    width=35,
                    font=("Segoe UI", 12),
                    on_select_function=self.on_map_choice,
                    sticky="w",
                    padx=(10, 30),
                )
                self.selected_map_id = self.map_choice_id
                self.reload_all_button = self.Button(
                    text="Reload All in Map",
                    font_size=10,
                    bg="#222",
                    width=25,
                    padx=5,
                    command=self.reload_all_in_map,
                    tooltip_text="Reload all talk scripts in selected map from project directory. (Ctrl + Shift + R)",
                )

            with self.set_master(sticky="nsew", row_weights=[1], column_weights=[0, 1], auto_columns=0):
                with self.set_master(sticky="nsew", row_weights=[1], column_weights=[1]):
                    self.build_entry_frame()
                with self.set_master(
                    sticky="nsew", row_weights=[0, 1, 0, 0], column_weights=[1], padx=50, pady=10, auto_rows=0
                ):
                    with self.set_master(sticky="nsew", column_weights=[1, 1, 1, 1], auto_columns=0, pady=5):
                        self.line_number = self.Label(
                            text="Line: None", padx=10, width=10, fg="#CCF", anchor="w", sticky="w"
                        ).var
                        self.go_to_line = self.Entry(label="Go to Line:", padx=5, width=6, sticky="w")
                        self.go_to_line.bind("<Return>", self._go_to_line)
                        self.state_to_find = self.Entry(label="Go to State:", padx=5, width=6, sticky="w")
                        self.state_to_find.bind("<Return>", self._find_state)
                        self.string_to_find = self.Entry(label="Find Text:", padx=5, width=20, sticky="w")
                        self.string_to_find.bind("<Return>", self._find_string)
                    with self.set_master(sticky="nsew", row_weights=[1], column_weights=[1, 0]):
                        self.build_script_editor()
                    with self.set_master(
                        sticky="nsew", row_weights=[1], column_weights=[1, 1], pady=10, auto_columns=0
                    ):
                        self.compile_button = self.Button(
                            text="Save & Compile",
                            font_size=10,
                            bg="#222",
                            width=20,
                            padx=5,
                            command=self.compile_selected,
                            state="disabled",
                            sticky="e",
                            tooltip_text="Save selected script, then test if it compiles to game ESD format without "
                            "errors. Automatically checked on export as well. (Ctrl + Shift + C)",
                        )
                        self.reload_button = self.Button(
                            text="Reload Script",
                            font_size=10,
                            bg="#222",
                            width=20,
                            padx=5,
                            command=self.reload_selected,
                            sticky="w",
                            tooltip_text="Reload selected script from project files. If there are unsaved changes in "
                            "the current script, you will be asked to confirm their loss first. "
                            "(Ctrl + R)",
                        )

        self.bind_to_all_children("<Control-C>", lambda _: self.compile_selected(mimic_click=True))
        self.bind_to_all_children("<Control-r>", lambda _: self.reload_selected(mimic_click=True))
        self.bind_to_all_children("<Control-R>", lambda _: self.reload_all_in_map(mimic_click=True))

    def build_script_editor(self):
        self.esp_editor_canvas = self.Canvas(
            horizontal_scrollbar=True,
            sticky="nsew",
            bg="#232323",
            borderwidth=0,
            highlightthickness=0,
            row=0,
            column=0,
            row_weights=[1],
            column_weights=[1],
        )
        editor_i_frame = self.Frame(self.esp_editor_canvas, row_weights=[1], column_weights=[1])
        self.esp_editor_canvas.create_window(0, 0, window=editor_i_frame, anchor="nw")
        editor_i_frame.bind("<Configure>", lambda e, c=self.esp_editor_canvas: self.reset_canvas_scroll_region(c))

        self.esp_editor = self.CustomWidget(
            editor_i_frame,
            custom_widget_class=ESPTextEditor,
            set_style_defaults=("text", "cursor"),
            row=0,
            width=400,
            height=50,
            wrap="word",
            bg="#232323",
            font=("Consolas", self.text_font_size),
            state="disabled",
        )
        vertical_scrollbar_w = self.Scrollbar(
            orient="vertical", command=self.esp_editor.yview, row=0, column=1, sticky="ns"
        )
        self.esp_editor.config(bd=0, yscrollcommand=vertical_scrollbar_w.set)
        self.link_to_scrollable(self.esp_editor, editor_i_frame)

        def _update_textbox_height(e):
            font_size = int(self.esp_editor["font"].split()[1])
            self.esp_editor["height"] = e.height // (font_size * 1.5)  # 1.5 line spacing

        self.esp_editor_canvas.bind("<Configure>", lambda e: _update_textbox_height(e))

        self.esp_editor.set_callback(self._update_line_number)
        self.esp_editor.bind("<Control-f>", self._control_f_search)

    def _go_to_line(self, _):
        number = self.go_to_line.var.get()
        if not number:
            return
        number = int(number)
        if not self.selected_map_id or number < 1 or int(self.esp_editor.index("end-1c").split(".")[0]) < number:
            self.flash_bg(self.go_to_line)
            return
        self.esp_editor.mark_set("insert", f"{number}.0")
        self.esp_editor.see(f"{number}.0")
        self.esp_editor.highlight_line(number, "found")

    def _find_string(self, _, string=None, flash_bg=True):
        if string is None:
            string = self.string_to_find.var.get()
        if not string or not self.selected_map_id:
            return
        start_line, start_char = self.esp_editor.index("insert").split(".")
        index = self.esp_editor.search(string, index=f"{start_line}.{int(start_char) + 1}")

        if index:
            self.clear_bg_tags()
            self.esp_editor.mark_set("insert", index)
            self.esp_editor.see(index)
            index_line, index_char = index.split(".")
            self.esp_editor.tag_add("found", index, f"{index_line}.{int(index_char) + len(string)}")
            return True
        elif flash_bg:
            self.flash_bg(self.string_to_find)
            return False

    def _find_state(self, _, state=None, flash_bg=True):
        if state is None:
            state = self.state_to_find.var.get()
            if not state or not self.selected_map_id:
                return
            try:
                state = int(state)
            except ValueError:
                if flash_bg:
                    self.flash_bg(self.state_to_find)
                self.state_to_find.var.set("")
                return

        if not self._find_string(_, string=f"class State_{state}(State):", flash_bg=False) and flash_bg:
            self.flash_bg(self.state_to_find)
            return False

    def clear_bg_tags(self):
        for tag in {"found", "error"}:
            self.esp_editor.tag_remove(tag, "1.0", "end")

    def _update_line_number(self, *_):
        current_line = self.esp_editor.index("insert").split(".")[0]
        self.line_number.set(f"Line: {current_line}")

    def _control_f_search(self, _):
        if self.selected_map_id:
            highlighted = self.esp_editor.selection_get()
            self.string_to_find.var.set(highlighted)
            self.string_to_find.select_range(0, "end")
            self.string_to_find.icursor("end")
            self.string_to_find.focus_force()

    def _highlight_error(self, lineno):
        self.esp_editor.mark_set("insert", f"{lineno}.0")
        self.esp_editor.see(f"{lineno}.0")
        self.esp_editor.highlight_line(lineno, "error")

    def _get_current_text(self):
        """Get all current text from TextBox, minus final newline (added by Tk)."""
        return self.esp_editor.get(1.0, "end")[:-1]

    def _ignored_unsaved(self):
        if self._get_current_text() != self.get_esd_text():
            if (
                self.CustomDialog(
                    title="Lose Unsaved Changes?",
                    message="Current script changes have not been saved. Lose changes?",
                    button_names=("Yes, lose changes", "No, stay here"),
                    button_kwargs=("YES", "NO"),
                    cancel_output=1,
                    default_output=1,
                )
                == 1
            ):
                return False
        return True

    def save_selected_esp(self, flash_bg=True):
        """Write selected ESP script to project folder. Also re-colors syntax."""
        if self.active_row_index is None:
            return self.CustomDialog(title="No Talk Selected", message="No talk ID selected to save.")
        self.esp_editor.color_syntax()
        current_text = self._get_current_text()
        talk_id = self.get_entry_id()
        self.esp_text[self.selected_map_id][talk_id] = current_text
        with self.esp_file_paths[self.selected_map_id][talk_id].open("w", encoding="utf-8") as f:
            f.write(current_text)
        if flash_bg:
            self.flash_bg(self.esp_editor, "#232")

    def export_all_in_map(self, export_directory=None):
        if not self.selected_map_id:
            return
        if export_directory is None:
            export_directory = self.FileDialog.askdirectory(initialdir=str(self.esp_directory))
            if export_directory is None:
                return
        export_directory = Path(export_directory)
        bnd_name = f"script/talk/{self.selected_map_id}.talkesdbnd{'.dcx' if self.talk.IS_DCX else ''}"
        try:
            self.talk.TALKESDBND_CLASS.write_from_dict(
                talk_dict=self.esp_file_paths[self.selected_map_id],
                talkesdbnd_path=export_directory / bnd_name,
            )
        except Exception as e:
            _LOGGER.exception("Error encountered while trying to export ESP scripts.")
            self.CustomDialog(
                title="Talk Export Error",
                message=f"Error encountered while trying to export ESP scripts (see console for full traceback):\n\n"
                f"{str(e)}",
            )
        return self.CustomDialog(
            title="Talk Export Successful",
            message=f"All talk scripts in {self.selected_map_id} were exported successfully.",
        )

    def compile_selected(self, mimic_click=False, flash_bg=True):
        if self.compile_button["state"] == "normal" and self.active_row_index is not None:
            # TODO: need a reference to banner save button to mimic click
            self.save_selected_esp(flash_bg=False)  # has to save to load from file
            if mimic_click:
                self.mimic_click(self.compile_button)
            talk_id = self.get_entry_id()
            try:
                self.talk.TALKESDBND_CLASS.TALK_ESD_CLASS(self.esp_file_paths[self.selected_map_id][talk_id])
            except ESDScriptError as e:
                _LOGGER.error(
                    f"Error encountered when parsing ESP script {talk_id} in {self.selected_map_id}. "
                    f"Error: {str(e)}."
                )
                self._raise_error(e.lineno, message=str(e), internal=False)
            except Exception as e:
                _LOGGER.exception(
                    f"Error encountered when parsing ESP script {talk_id} in {self.selected_map_id}. "
                    f"See full traceback below."
                )
                self._raise_error(message=str(e), internal=True)
            else:
                self.esp_editor.tag_remove("error", "1.0", "end")
                if flash_bg:
                    self.flash_bg(self.esp_editor, "#224")

    def reload_selected(self, mimic_click=False):
        """Reload selected script from project directory. Confirms loss of unsaved changes first."""
        if self.reload_button["state"] == "normal" and self.active_row_index is not None:
            if mimic_click:
                self.mimic_click(self.reload_button)
            if not self._ignored_unsaved():
                return
            talk_id = self.get_entry_id()
            esp_path = self.esp_file_paths[self.selected_map_id][talk_id]
            try:
                with esp_path.open("r", encoding="utf-8") as f:
                    self.esp_text[self.selected_map_id][talk_id] = f.read()
            except FileNotFoundError:
                self.CustomDialog(
                    title="ESP File Missing", message=f"ESP talk file 't{talk_id}.esp' not found in\n'{str(esp_path)}'."
                )
            else:
                self.update_talk_text()

    def reload_all_in_map(self, mimic_click=False):
        if (
            self.CustomDialog(
                title="Confirm Reload",
                message=f"Any unsaved scripts in the current map will be replaced with reloaded files\n"
                f"or lost entirely if no file with that talk ID exists.\n\n"
                f"Continue with full map reload?",
                button_names=("Yes, continue", "No, go back"),
                button_kwargs=("YES", "NO"),
                return_output=0,
                cancel_output=1,
                default_output=0,
            )
            == 1
        ):
            return

        if mimic_click:
            self.mimic_click(self.reload_all_button)

        map_directory = self.esp_directory / f"{self.selected_map_id}"

        # Check for missing files.
        current_ids = self._get_category_name_range()
        missing_files = []
        for current_id in current_ids:
            id_path = map_directory / f"t{current_id}.esp.py"
            if not id_path.is_file():
                missing_files.append(str(id_path))
        if missing_files:
            missing_string = "\n".join(missing_files)
            if (
                self.CustomDialog(
                    title="Confirm Missing Files",
                    message=f"The following talk ESP files could not be found:\n"
                    f"{missing_string}\n\n"
                    f"These talk IDs will be lost. Continue anyway?",
                    button_names=("Yes, lose those IDs", "No, cancel reload"),
                    button_kwargs=("YES", "NO"),
                    return_output=0,
                    cancel_output=1,
                    default_output=0,
                )
                == 1
            ):
                return

        self.esp_file_paths[self.selected_map_id] = {}
        self.esp_text[self.selected_map_id] = {}
        for esp_path in map_directory.glob("*.esp.py"):
            talk_match = _TALK_ESP_MATCH.match(esp_path.name)
            if not talk_match:
                _LOGGER.warning(f"Invalid ESP file found and ignored: {str(esp_path)}")
                continue
            talk_id = int(talk_match.group(1))
            self.esp_file_paths.setdefault(self.selected_map_id, {})[talk_id] = esp_path
            with esp_path.open(mode="r", encoding="utf-8") as f:
                self.esp_text.setdefault(self.selected_map_id, {})[talk_id] = f.read()
        self.refresh_entries()
        if self.active_row_index is not None:
            self.update_talk_text()

    def refresh_entries(self):
        self._cancel_entry_id_edit()

        talk_ids_to_display = self._get_category_name_range(
            first_index=self.first_display_index, last_index=self.first_display_index + self.ENTRY_RANGE_SIZE,
        )

        row = 0
        for talk_id in talk_ids_to_display:
            self.entry_rows[row].update_entry(entry_id=talk_id)
            self.entry_rows[row].unhide()
            row += 1

        self.displayed_entry_count = row
        for remaining_row in range(row, len(self.entry_rows)):
            self.entry_rows[remaining_row].hide()

        if self.displayed_entry_count == 0:
            self.select_entry_row_index(None)  # TODO: select first index if present?
        self._refresh_range_buttons()

    def select_entry_id(self, entry_id, set_focus_to_text=False, edit_if_already_selected=True, as_row_index=None):
        """Select entry based on ID and set the category display range to target_row_index rows before it."""
        entry_index = self.get_entry_index(entry_id)
        self.refresh_entries()
        self.select_entry_row_index(
            entry_index, set_focus_to_text=False, edit_if_already_selected=edit_if_already_selected
        )

    def select_entry_row_index(
        self, row_index, set_focus_to_text=False, edit_if_already_selected=True, id_clicked=False, check_unsaved=True
    ):
        """Select entry from row index, based on currently displayed category and ID range."""
        old_row_index = self.active_row_index

        if check_unsaved and old_row_index != row_index and old_row_index is not None:
            if not self._ignored_unsaved():
                return

        if old_row_index is not None and row_index is not None:
            if row_index == old_row_index:
                if edit_if_already_selected and id_clicked:
                    return self._start_entry_id_edit(row_index)
        else:
            self._cancel_entry_id_edit()

        self.active_row_index = row_index

        if old_row_index is not None:
            self.entry_rows[old_row_index].active = False
        if row_index is not None:
            self.entry_rows[row_index].active = True
            self.esp_editor["state"] = "normal"
            self.compile_button["state"] = "normal"
            self.reload_button["state"] = "normal"
            self.update_talk_text()
        else:
            # No entry is selected.
            self.esp_editor.delete(1.0, "end")
            self.esp_editor["state"] = "disabled"
            self.compile_button["state"] = "disabled"
            self.reload_button["state"] = "disabled"

    def update_talk_text(self):
        self.esp_editor.delete(1.0, "end")
        self.esp_editor.insert(1.0, self.get_selected_text())
        self.esp_editor.mark_set("insert", "1.0")
        self.esp_editor.color_syntax()

    def get_esd_text(self, row_index=None):
        talk_id = self.get_entry_id(row_index)
        return self.esp_text[self.selected_map_id][talk_id]

    def on_map_choice(self, event=None):
        if self.active_row_index is not None and not self._ignored_unsaved():
            # Keep currently selected map.
            self.map_choice.var.set(f"{self.selected_map_id} [{self.talk.GET_MAP(self.selected_map_id).name}]")
            return
        self.selected_map_id = self.map_choice_id
        if self.global_map_choice_func and event is not None:
            self.global_map_choice_func(self.map_choice_id, ignore_tabs=("talk",))
        self.select_entry_row_index(None, check_unsaved=False)
        self.refresh_entries()
        self.entry_canvas.yview_moveto(0)

    def _add_entry(self, entry_id, text=None, category=None, new_esp_string=None):
        if entry_id <= 0:
            self.CustomDialog(title="Talk ID Error", message=f"Talk ID must be greater than zero.")
            return False
        if entry_id in self.get_category_data():
            self.CustomDialog(title="Talk ID Error", message=f"Talk ID {entry_id} already exists.")
            return False

        self._cancel_entry_id_edit()
        with (self.esp_directory / f"{self.selected_map_id}/t{entry_id}.esp.py").open(mode="w", encoding="utf-8") as f:
            f.write(new_esp_string)
        self.refresh()  # scan for new talk ID
        self.select_entry_id(entry_id, set_focus_to_text=True, edit_if_already_selected=False)

    def add_relative_entry(self, entry_id, goal_type=None, offset=1, text=None):
        esp_text = self.esp_text[self.selected_map_id][entry_id]
        self._add_entry(entry_id=entry_id + offset, text=text, new_esp_string=esp_text)

    def delete_entry(self, row_index, category=None):
        """Deletes talk script file in project. Cannot be undone."""
        if row_index is None:
            self.bell()
            return
        self._cancel_entry_id_edit()
        talk_id = self.get_entry_id(row_index)
        if (
            self.CustomDialog(
                title="Confirm Deletion",
                message=f"Delete talk ID {talk_id} in map {self.selected_map_id}? This will\n"
                f"delete the ESP file in your project directory and cannot be undone.",
                button_names=("Yes, delete it", "No, go back"),
                button_kwargs=("YES", "NO"),
                cancel_output=1,
                default_output=1,
            )
            == 1
        ):
            return
        esp_path = self.get_esp_path(row_index)
        os.remove(str(esp_path))
        self.esp_text[self.selected_map_id].pop(talk_id)
        self.esp_file_paths[self.selected_map_id].pop(talk_id)
        self.select_entry_row_index(None, check_unsaved=False)
        self.refresh_entries()

    def get_category_data(self, category=None) -> dict[int, str]:
        """Gets list of talk IDs and their paths. Category argument does nothing."""
        return self.esp_file_paths[self.selected_map_id]

    def get_selected_text(self) -> str:
        return self.esp_text[self.selected_map_id][self.get_entry_id()]

    def get_esp_path(self, row_index=None) -> Path:
        if row_index is None:
            row_index = self.active_row_index
        return self.esp_directory / f"{self.selected_map_id}/t{self.get_entry_id(row_index)}.esp.py"

    def _get_category_name_range(self, category=None, first_index=None, last_index=None):
        """Returns list of talk IDs in map."""
        return list(self.get_category_data())

    def get_entry_index(self, entry_id: int, category=None) -> int:
        """Get index of entry. Ignores current display range."""
        entry_ids = self._get_category_name_range()
        if entry_id not in entry_ids:
            raise ValueError(f"Talk ID {entry_id} does not exist.")
        return entry_ids.index(entry_id)

    def get_entry_text(self, entry_id: int, category=None) -> str:
        # Not used.
        pass

    def _set_entry_text(self, entry_id: int, text: str, category=None, update_row_index=None):
        # Not used.
        pass

    def _set_entry_id(self, entry_id: int, new_id: int, category=None, update_row_index=None):
        talk_dict = self.get_category_data()
        talk_dict[new_id] = talk_dict.pop(entry_id)
        if update_row_index is not None:
            self.entry_rows[update_row_index].update_entry(entry_id=new_id)
        return True

    def _get_display_categories(self):
        """Unused."""
        return []

    def _raise_error(self, lineno=None, message=None, internal=False):
        if lineno:
            self.esp_editor.mark_set("insert", f"{lineno}.0")
            self.esp_editor.see(f"{lineno}.0")
            self.esp_editor.highlight_line(lineno, "error")
        if message:
            self.CustomDialog(
                title="ESP Error",
                message=f"Error encountered when parsing ESP script "
                f"{'(see log for full traceback)' if internal else ''}:\n\n{message}",
            )
