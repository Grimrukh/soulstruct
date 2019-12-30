"""
TODO:
    - Button to open selected script in preferred IDE/editor.
    - Functions to help search all events for Entity ID references, etc.
"""
import re
from pathlib import Path

from soulstruct.events.darksouls1 import EMEVD, VERBOSE_MAP_NAMES
from soulstruct.maps import DARK_SOULS_MAP_NAMES
from soulstruct.utilities.window import SoulstructSmartFrame


def _get_verbose_map_name(emevd_name):
    if emevd_name == "common":
        return "Common"
    area, block, _, version = re.match(r"m(\d+)_(\d+)_(\d+)_(\d+)", emevd_name).groups()
    return VERBOSE_MAP_NAMES[int(area), int(block)]


class SoulstructEventEditor(SoulstructSmartFrame):

    def __init__(self, evs_directory, game_root, dcx, master=None, toplevel=False):
        super().__init__(master=master, toplevel=toplevel, window_title="Soulstruct EMEVD Manager")
        self.evs_directory = Path(evs_directory)
        self.game_root = Path(game_root)
        self.dcx = dcx
        self.evs_file_paths = {}
        self.evs_text = {}
        self.selected_evs = None

        for evs_file_path in self.evs_directory.glob("*.evs.py"):
            evs_name = evs_file_path.name.split('.')[0]
            self.evs_file_paths[evs_name] = evs_file_path
            with evs_file_path.open('r', encoding='utf-8') as f:
                self.evs_text[evs_name] = f.read()

        self.start_auto_rows()

        map_options = [f"{m} ({_get_verbose_map_name(m)})" for m in self.evs_file_paths]

        self.evs_choice = self.Combobox(
            values=map_options, initial_value=map_options[0] if map_options else "", width=30,
            on_select_function=self._on_evs_choice,
            label='Script:', label_font_size=12, label_position='left', font=('Segoe UI', 12), padx=10, pady=10).var

        with self.set_master():
            self.evs_editor_canvas = self.Canvas(
                horizontal_scrollbar=True, width=800, height=400, padx=5,
                yscrollincrement=12, borderwidth=0, highlightthickness=0, column=0)
            editor_frame = self.Frame(self.evs_editor_canvas, width=120, height=60, sticky='ew')
            self.link_to_scrollable(self.evs_editor_canvas, editor_frame)
            self.evs_editor_canvas.create_window(0, 0, window=editor_frame, anchor='nw')
            editor_frame.bind("<Configure>", lambda e, c=self.evs_editor_canvas: self.reset_canvas_scroll_region(c))

            self.evs_text_editor = self.TextBox(editor_frame, width=200, height=25, wrap='word', bg='#252525')
            vertical_scrollbar_w = self.Scrollbar(
                orient='vertical', command=self.evs_text_editor.yview, column=1, sticky='ns')
            self.evs_text_editor.config(bd=0, yscrollcommand=vertical_scrollbar_w.set)

        with self.set_master(auto_columns=0, pady=(10, 5)):
            self.Button(text="Save EVS", width=15, command=self._save_evs)
            self.Button(text="Check Syntax", width=15, padx=(30, 30), command=self._check_syntax)
            self.Button(text="Reload EVS", width=15, command=self._reload_selected)

        with self.set_master(auto_columns=0):
            self.Button(text="Save & Export", width=15, padx=(0, 15), bg='#822', command=self._save_and_export)
            self.Button(text="Reload & Export", width=15, padx=(15, 0), bg='#822', command=self._reload_and_export)

        if map_options:
            self.selected_evs = self.evs_choice.get().split(' (')[0]
            self.evs_text_editor.insert(1.0, self.evs_text[self.selected_evs])

    def refresh(self):
        map_options = [f"{m} ({_get_verbose_map_name(m)})" for m in self.evs_file_paths]
        self.evs_choice["values"] = map_options
        if map_options:
            self.evs_choice.set(map_options[0])
            self.selected_evs = self.evs_choice.get().split(' (')[0]
            self.evs_text_editor.insert(1.0, self.evs_text[self.selected_evs])

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
            self.selected_evs = self.evs_choice.get().split(' (')[0]
            self.evs_text_editor.delete(1.0, 'end')
            self.evs_text_editor.insert(1.0, self.evs_text[self.selected_evs])
        else:
            self.evs_choice.set(f"{self.selected_evs} ({DARK_SOULS_MAP_NAMES[self.selected_evs]})")  # keep previous

    def _save_evs(self):
        current_text = self._get_current_text()
        self.evs_text[self.selected_evs] = current_text
        with self.evs_file_paths[self.selected_evs].open('w', encoding='utf-8') as f:
            f.write(current_text)

    def _check_syntax(self):
        try:
            EMEVD(self._get_current_text())
        except Exception as e:
            self.error_dialog("EVS Error",
                              f"Error encountered when trying to parse EVS script (see console for full traceback):\n\n"
                              f"{str(e)}")
        else:
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

    def _save_and_export(self):
        self._save_evs()
        self._export_evs()

    def _reload_and_export(self):
        self._reload_selected()
        self._export_evs()

    def _get_current_text(self):
        """Get all current text from TextBox, minus final newline (added by Tk)."""
        return self.evs_text_editor.get(1.0, 'end')[:-1]
