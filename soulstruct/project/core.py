"""
TODO:
    - "Save Events" should say "Save Event Script"
"""
from __future__ import annotations

import datetime
import json
import logging
import os
import pickle
import re
import shutil
import subprocess
import threading
from functools import wraps
from pathlib import Path
from typing import Optional

from soulstruct._config import PTDE_PATH, DSR_PATH
from soulstruct.ai import DarkSoulsAIScripts
from soulstruct.bnd import BND
from soulstruct.events.darksouls1.core import convert_events
from soulstruct.maps import DarkSoulsMaps
from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.text import DarkSoulsText
from soulstruct.utilities.core import word_wrap
from soulstruct.utilities.window import SmartFrame, CustomDialog

from .ai import SoulstructAIEditor
from .entities import SoulstructEntityEditor
from .events import SoulstructEventEditor
from .lighting import SoulstructLightingEditor
from .links import WindowLinker
from .maps import SoulstructMapEditor
from .params import SoulstructParamsEditor
from .runtime import SoulstructRuntimeManager
from .text import SoulstructTextEditor
from .utilities import SoulstructProjectError

try:
    import psutil
except ImportError:
    psutil = None

__all__ = ['SoulstructProject', 'SoulstructProjectWindow']
_LOGGER = logging.getLogger(__name__)


DATA_TYPES = {
    'maps': DarkSoulsMaps,
    'params': DarkSoulsGameParameters,
    'lighting': DarkSoulsLightingParameters,
    'text': DarkSoulsText,
    'events': None,  # modified via EVS script files
    'ai': DarkSoulsAIScripts,
}

STEAM_APPIDS = {
    "Dark Souls Prepare to Die Edition": 211420,
    "Dark Souls Remastered": 570940,
}


def _with_config_write(func):
    @wraps(func)
    def project_method(self: SoulstructProject, *args, **kwargs):
        func(self, *args, **kwargs)
        self._write_config()

    return project_method


class SoulstructProjectWindow(SmartFrame):
    maps_tab: Optional[SoulstructMapEditor]
    entities_tab: Optional[SoulstructEntityEditor]
    params_tab: Optional[SoulstructParamsEditor]
    lighting_tab: Optional[SoulstructLightingEditor]
    text_tab: Optional[SoulstructTextEditor]
    events_tab: Optional[SoulstructEventEditor]
    ai_tab: Optional[SoulstructAIEditor]

    TAB_ORDER = ['maps', 'entities', 'params', 'lighting', 'text', 'events', 'ai', 'runtime']

    def __init__(self, project_path=None, master=None):
        super().__init__(master=master, toplevel=True, icon_data=SOULSTRUCT_ICON,
                         window_title="Soulstruct Project Editor")
        self.withdraw()

        if not project_path:
            self.CustomDialog(
                title="Choose Soulstruct project directory",
                message="Navigate to your Soulstruct project directory.\n\n" + word_wrap(
                    "If you want to create a new project, create an empty directory and select it. "
                    "The name of the directory will be the name of the project.", 50))
            project_path = self.FileDialog.askdirectory(
                title="Choose Soulstruct project directory", initialdir=str(Path('~/Documents').expanduser()))
            if not project_path:
                self.CustomDialog(title="Project Error", message="No directory chosen. Quitting Soulstruct.")
                raise SoulstructProjectError("No directory chosen. Quitting Soulstruct.")

        self.toplevel.title("Soulstruct Project Editor: " + Path(project_path).name)

        try:
            self.project = SoulstructProject(project_path, with_window=self)
            _LOGGER.info(f"Opened project: {project_path}")
        except SoulstructProjectError as e:
            self.deiconify()
            self.CustomDialog(title="Project Error", message=word_wrap(str(e), 50) + "\n\nAborting startup.")
            raise
        except Exception as e:
            self.deiconify()
            msg = "Internal Python Error:\n\n" + word_wrap(str(e), 50) + "\n\nAborting startup."
            self.CustomDialog(title="Unknown Error", message=msg)
            raise

        self.linker = WindowLinker(self)  # TODO: Individual editors should have a lesser linker.

        with self.set_master(column_weights=[1], row_weights=[0, 1], auto_rows=0, sticky='nsew'):
            self.global_ribbon = self.Frame(row_weights=[1], column_weights=[1, 1, 1, 1], pady=(10, 5))
            self.page_tabs = self.Notebook(name="project_notebook", sticky='nsew')

        self.maps_tab = None
        self.entities_tab = None
        self.params_tab = None
        self.text_tab = None
        self.lighting_tab = None
        self.events_tab = None
        self.ai_tab = None
        self.runtime_tab = None

        self.save_all_button = None
        self.save_tab_button = None
        self.export_all_button = None
        self.export_tab_button = None

        self.toplevel.minsize(700, 500)
        self.alphanumeric_word_boundaries()
        self.toplevel.protocol("WM_DELETE_WINDOW", self.confirm_quit)  # TODO: enable on release
        self.build()
        self.deiconify()

    def build(self):
        self.build_top_menu()

        with self.set_master(self.global_ribbon, auto_columns=0, grid_defaults={'padx': 5}):
            self.save_all_button = self.Button(
                text="Save Entire Project", width=20, bg="#622",
                tooltip_text="Saves all project data types to local project files. (Ctrl + Shift + S)",
                command=self._save_data)
            self.save_tab_button = self.Button(
                text="Save Tab Data", width=20,
                tooltip_text="Saves just the indicated data type to local project files. (Ctrl + S)",
                command=lambda: self._save_data(self.current_data_type))
            self.export_tab_button = self.Button(
                text="Export Tab Data", width=20,
                tooltip_text="Saves and exports just the indicated data type to the game directory. (Ctrl + E)",
                command=lambda: self._export_data(self.current_data_type, self.project.game_root))
            self.export_all_button = self.Button(
                text="Export Entire Project", width=20, bg="#622",
                tooltip_text="Saves and exports all project data types to the game directory. (Ctrl + Shift + E)",
                command=lambda: self._export_data(export_directory=self.project.game_root))

        tab_frames = {tab_name: self.Frame(frame=self.page_tabs, sticky='nsew', row_weights=[1], column_weights=[1])
                      for tab_name in self.TAB_ORDER}

        self.maps_tab = self.SmartFrame(
            frame=tab_frames['maps'], smart_frame_class=SoulstructMapEditor,
            maps=self.project.Maps, linker=self.linker, sticky='nsew')
        self.maps_tab.bind("<Visibility>", self._update_banner)

        self.entities_tab = self.SmartFrame(
            frame=tab_frames['entities'], smart_frame_class=SoulstructEntityEditor,
            maps=self.project.Maps, evs_directory=self.project.project_root / "events", linker=self.linker,
            sticky='nsew')
        self.entities_tab.bind("<Visibility>", self._update_banner)

        self.params_tab = self.SmartFrame(
            frame=tab_frames['params'], smart_frame_class=SoulstructParamsEditor,
            params=self.project.Params, linker=self.linker, sticky='nsew')
        self.params_tab.bind("<Visibility>", self._update_banner)

        self.lighting_tab = self.SmartFrame(
            frame=tab_frames['lighting'], smart_frame_class=SoulstructLightingEditor,
            lighting=self.project.Lighting, linker=self.linker, sticky='nsew')
        self.lighting_tab.bind("<Visibility>", self._update_banner)

        self.text_tab = self.SmartFrame(
            frame=tab_frames['text'], smart_frame_class=SoulstructTextEditor,
            text=self.project.Text, linker=self.linker, sticky='nsew')
        self.text_tab.bind("<Visibility>", self._update_banner)

        self.events_tab = self.SmartFrame(
            frame=tab_frames['events'], smart_frame_class=SoulstructEventEditor,
            evs_directory=self.project.project_root / "events", game_root=self.project.game_root,
            dcx=self.project.game_name == "Dark Souls Remastered", sticky='nsew')
        self.events_tab.bind("<Visibility>", self._update_banner)

        self.ai_tab = self.SmartFrame(
            frame=tab_frames['ai'], smart_frame_class=SoulstructAIEditor,
            ai=self.project.AI, script_directory=self.project.project_root / "ai_scripts",
            game_root=self.project.game_root, allow_decompile=self.project.game_name == "Dark Souls Remastered",
            linker=self.linker, sticky='nsew')
        self.ai_tab.bind("<Visibility>", self._update_banner)

        self.runtime_tab = self.SmartFrame(
            frame=tab_frames['runtime'], smart_frame_class=SoulstructRuntimeManager,
            project=self.project, sticky='nsew')
        self.runtime_tab.bind("<Visibility>", self._update_banner)

        for tab_name, tab_frame in tab_frames.items():
            self.page_tabs.add(tab_frame, text=f'  {_fixed_caps(tab_name)}  ')

        self.create_key_bindings()

        self.set_geometry()

    def build_top_menu(self):
        top_menu = self.Menu()

        file_menu = self.Menu(tearoff=0)
        save_menu = self.Menu(tearoff=0)
        save_menu.add_command(
            label=f"Save Entire Project", foreground='#FFF',
            command=self._save_data)
        save_menu.add_separator()
        for data_type in DATA_TYPES:
            save_menu.add_command(
                label=f"Save {_fixed_caps(data_type)}", foreground='#FFF',
                command=lambda d=data_type: self._save_data(d))
        file_menu.add_cascade(label=f"Save", foreground='#FFF', menu=save_menu)
        file_menu.add_separator()
        for import_dir in (self.project.game_root, None):
            import_menu = self.Menu(tearoff=0)
            import_menu.add_command(
                label=f"Import Everything", foreground='#FFF',
                command=lambda i=import_dir: self._import_data(import_directory=i))
            import_menu.add_separator()
            for data_type in DATA_TYPES:
                import_menu.add_command(
                    label=f"Import {_fixed_caps(data_type)}", foreground='#FFF',
                    command=lambda d=data_type, i=import_dir: self._import_data(d, import_directory=i))
            file_menu.add_cascade(label=f"Import from{' Game' if import_dir else '...'}",
                                  foreground='#FFF', menu=import_menu)
        file_menu.add_separator()
        for export_dir in (self.project.game_root, None):
            export_menu = self.Menu(tearoff=0)
            export_menu.add_command(
                label=f"Export Everything", foreground='#FFF',
                command=lambda e=export_dir: self._export_data(export_directory=e))
            export_menu.add_separator()
            for data_type in DATA_TYPES:
                export_menu.add_command(
                    label=f"Export {_fixed_caps(data_type)}", foreground='#FFF',
                    command=lambda d=data_type, e=export_dir: self._export_data(d, export_directory=e))
            file_menu.add_cascade(label=f"Export to{' Game' if export_dir else '...'}",
                                  foreground='#FFF', menu=export_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Set as Default Project", foreground='#FFF',
                              command=self._set_as_default_project)
        file_menu.add_command(label="Clear Default Project", foreground='#FFF',
                              command=self._clear_default_project)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", foreground='#FFF', command=self.confirm_quit)
        top_menu.add_cascade(label="File", menu=file_menu)

        tools_menu = self.Menu(tearoff=0)
        tools_menu.add_command(label="Restore .bak File", foreground='#FFF',
                               command=lambda: self._restore_backup(full_folder=False))
        tools_menu.add_command(label="Restore .bak Files", foreground='#FFF',
                               command=lambda: self._restore_backup(full_folder=True))
        tools_menu.add_separator()
        tools_menu.add_command(label="Unpack BND", foreground='#FFF',
                               command=self._unpack_bnd)
        tools_menu.add_command(label="Repack BND", foreground='#FFF',
                               command=self._repack_bnd)
        top_menu.add_cascade(label="Tools", menu=tools_menu)

        # TODO: edit commands
        # edit_menu = self.Menu(tearoff=0)
        # edit_menu.add_command(label="Undo", foreground='#FFF', command=lambda: print("Undo"))
        # edit_menu.add_command(label="Redo", foreground='#FFF', command=lambda: print("Redo"))
        # edit_menu.add_command(label="Copy", foreground='#FFF', command=lambda: print("Copy"))
        # edit_menu.add_command(label="Cut", foreground='#FFF', command=lambda: print("Cut"))
        # edit_menu.add_command(label="Paste", foreground='#FFF', command=lambda: print("Paste"))
        # top_menu.add_cascade(label="Edit", menu=edit_menu)

        self.toplevel.config(menu=top_menu)

    def alphanumeric_word_boundaries(self):
        """See: http://www.tcl.tk/man/tcl8.5/TclCmd/library.htm#M19"""
        self.tk.call('tcl_wordBreakAfter', '', 0)
        self.tk.call('set', 'tcl_wordchars', '[a-zA-Z0-9_.]')
        self.tk.call('set', 'tcl_nonwordchars', '[^a-zA-Z0-9_.]')

    def create_key_bindings(self):
        self.bind_all("<Control-s>", lambda _: self._save_data(self.current_data_type, mimic_click=True))
        self.bind_all("<Control-S>", lambda _: self._save_data(mimic_click=True))
        self.bind_all("<Control-e>", lambda _: self._export_data(
            self.current_data_type, export_directory=self.project.game_root, mimic_click=True))
        self.bind_all("<Control-E>", lambda _: self._export_data(
            export_directory=self.project.game_root, mimic_click=True))

    def refresh_tab_data(self, data_type=None):
        if data_type is None:
            for data_type in self.TAB_ORDER:
                self.refresh_tab_data(data_type)
        data_type = data_type.lower()
        if data_type not in self.TAB_ORDER:
            raise ValueError(f"Invalid data type name: {data_type}")
        if data_type == "events":
            self.events_tab.refresh()
        elif data_type == "entities":
            self.entities_tab.Maps = self.project.Maps
        else:
            project_data = getattr(self.project, _fixed_caps(data_type))
            setattr(getattr(self, f'{data_type}_tab'), _fixed_caps(data_type), project_data)

    def confirm_quit(self):
        if self.CustomDialog(title="Quit Soulstruct?",
                             message="Quit Soulstruct? Any unsaved changes will be lost.",
                             button_names=("Yes, quit", "No, go back"),
                             button_kwargs=('YES', 'NO'),
                             cancel_output=1, default_output=1) == 0:
            self.destroy()

    def destroy(self):
        """Destruction takes a second or so, so we withdraw first to hide the awkward lag."""
        self.withdraw()
        super().destroy()

    @property
    def current_data_type(self):
        data_type = self.TAB_ORDER[self.page_tabs.index(self.page_tabs.select())]
        if data_type == "entities":
            return "maps"
        return data_type

    def _import_data(self, data_type=None, import_directory=None):
        if import_directory is None:
            import_directory = self._choose_directory()
            if import_directory is None:
                return  # Abort import.
        # TODO: progress bar
        self.project.import_data(data_type, import_directory)
        self.refresh_tab_data(data_type)

    def _save_data(self, data_type=None, mimic_click=False):
        if data_type == "runtime":
            return  # nothing to save
        elif data_type == "events":
            self.events_tab.save_selected_evs()
            if mimic_click:
                self.mimic_click(self.save_tab_button)
            return
        elif data_type == "ai" and self.ai_tab.confirm_button["state"] == "normal":
            self.ai_tab.confirm_selected(mimic_click=mimic_click)
            # doesn't return here
        # TODO: progress bar
        if mimic_click:
            if data_type is None:
                self.mimic_click(self.save_all_button)
            else:
                self.mimic_click(self.save_tab_button)
        self.project.save(data_type)  # doesn't save events
        if data_type is None:
            self.events_tab.save_all_evs()  # saves EVS files to project subdirectory
        self.flash_bg(self)

    def _export_data(self, data_type=None, export_directory=None, mimic_click=False):
        if export_directory is None:
            export_directory = self._choose_directory()
            if export_directory is None:
                return  # Abort export.
        if data_type == "events":
            # Specifying 'events' here means the selected script only.
            self.events_tab.save_selected_evs()
            self.mimic_click(self.save_tab_button)
            self.events_tab.export_selected_evs(export_directory)
            if mimic_click:
                self.mimic_click(self.export_tab_button)
            return
        # TODO: progress bar
        if mimic_click:
            if data_type is None:
                self.mimic_click(self.export_all_button)
            else:
                self.mimic_click(self.export_tab_button)
        self.project.export_data(data_type, export_directory)

    def _restore_backup(self, target=None, full_folder=False):
        if target is None:
            if full_folder:
                target = self.FileDialog.askdirectory(
                    title="Choose Folder to Restore Backups", initialdir=str(self.project.game_root))
            else:
                target = self.FileDialog.askopenfilename(
                    title="Choose File to Restore Backup", initialdir=str(self.project.game_root),
                    filetypes=[("Bak file", ".bak")])
            if not target:
                return
        try:
            count = self.project.restore_backup(target=target)
        except RestoreBackupError as e:
            return self.CustomDialog(title="Restore Backup Error", message=str(e))
        if count:
            return self.CustomDialog(
                title="Restore Successful",
                message=f"{count} '.bak' files restored in folder\n'{str(target)}'.")
        return self.CustomDialog("Restore Successful", f"Backup file '{str(target)}' restored.")

    def _unpack_bnd(self):
        target = self.FileDialog.askopenfilename(
            title="Choose BND File to Unpack", initialdir=str(self.project.game_root))
        if target is None:
            return
        if not re.match(r".*\.[a-z]*bnd(\.dcx)?$", target):
            return self.CustomDialog(
                title="Invalid BND File",
                message=f"A valid BND file (with or without DCX) must be selected.")
        BND(target).write_unpacked_dir()

    def _repack_bnd(self):
        target = self.FileDialog.askdirectory(
            title="Choose Unpacked BND Directory to Repack", initialdir=str(self.project.game_root))
        if target is None:
            return
        if not re.match(r".*\.[a-z]*bnd", target):
            return self.CustomDialog(
                title="Invalid Directory",
                message=f"A valid unpacked BND directory (with a 'bnd_manifest.txt' file) must be selected.")
        BND(target).write()

    def _set_as_default_project(self):
        """Set this project directory as the Soulstruct default in `config.py`."""
        from soulstruct._config import SET_CONFIG
        SET_CONFIG(default_project_path=str(self.project.project_root))

    @staticmethod
    def _clear_default_project():
        from soulstruct._config import SET_CONFIG
        SET_CONFIG(default_project_path='')

    def _choose_directory(self, initial_dir=None, **kwargs):
        if initial_dir is None:
            initial_dir = str(self.project.project_root)
        directory = self.FileDialog.askdirectory(initialdir=initial_dir, **kwargs)
        if directory is None:
            return None
        return Path(directory)

    def _update_banner(self, event):
        try:
            data_name = event.widget.DATA_NAME
        except AttributeError:
            raise AttributeError(f"No `DATA_NAME` for widget: {type(event.widget)}")
        if data_name is None:
            self.save_tab_button.var.set(f"Save")
            self.export_tab_button.var.set(f"Export")
            self.save_tab_button["state"] = "disabled"
            self.export_tab_button["state"] = "disabled"
        else:
            self.save_all_button["state"] = "normal"
            self.save_tab_button["state"] = "normal"
            self.export_all_button["state"] = "normal"
            self.export_tab_button["state"] = "normal"
            if data_name == "Events":
                self.save_tab_button.var.set(f"Save Event Script")
                self.export_tab_button.var.set(f"Export Event Script")
            else:
                self.save_tab_button.var.set(f"Save {data_name}")
                self.export_tab_button.var.set(f"Export {data_name}")


class SoulstructProject(object):
    """Manages a directory of easily-modded Soulstruct files that can imported and exported.

    It is recommended that you create one of these projects for each Soulstruct-based mod.

    Currently supports only Dark Souls 1.

    TODO:
        - Eventually have subclasses for different games, with shared methods here.
        - Auto-save scheduled Tk functions that operate at ten minute intervals.
        - Inspect PTDE directory for lack of UDSFM when imported.
    """
    _DEFAULT_PROJECT_ROOT = '~/Documents/Soulstruct/'

    def __init__(self, project_path="", with_window: SoulstructProjectWindow = None):

        self.game_name = ''
        self.game_root = Path()
        self.game_exe_path = Path()
        self.game_save_root = Path()
        self.last_import_time = ''
        self.last_export_time = ''
        # TODO: Record last edit time for each file/structure.

        # Initialize with empty structures.
        self.Text = DarkSoulsText()
        self.Params = DarkSoulsGameParameters()
        self.Lighting = DarkSoulsLightingParameters()
        self.Maps = DarkSoulsMaps()
        self.AI = DarkSoulsAIScripts()

        self.project_root = self._validate_project_directory(project_path, self._DEFAULT_PROJECT_ROOT)
        self.load_config(with_window=with_window)
        self.initialize_project(with_window=with_window)

    def initialize_project(self, force_import_from_game=False, with_window: SoulstructProjectWindow = None):
        """Load project structures from pickled project files if available, or prompt for initial import to create."""
        yes_to_all = force_import_from_game
        for data_type in DATA_TYPES:
            if data_type == "events":
                continue  # Events are not saved and loaded, just imported and exported.
            try:
                if force_import_from_game:
                    raise FileNotFoundError
                self.load(data_type)
            except FileNotFoundError:
                if yes_to_all:
                    self.import_data_from_game(data_type)
                    self.save(data_type)
                else:
                    if with_window:
                        result = with_window.CustomDialog(
                            title="Project Error",
                            message=f"Could not find saved {_fixed_caps(data_type)} data in project.\n"
                                    f"Would you like to import it from the game directory now?",
                            button_names=("Yes", "Yes to All", "No, quit now"),
                            button_kwargs=('YES', 'YES', 'NO'),
                            cancel_output=2, default_output=2,
                        )
                    else:
                        result = 2 if input(
                            f"Could not find saved {_fixed_caps(data_type)} data in project.\n"
                            f"Would you like to import it from the game directory now? [y]/n").lower() == 'n' else 0
                    if result in {0, 1}:
                        self.import_data_from_game(data_type)
                        self.save(data_type)
                        if result == 1:
                            yes_to_all = True
                    else:
                        raise SoulstructProjectError("Could not open project files.")

        if not (self.project_root / "events").is_dir() or not (self.project_root / "events").glob("*"):
            if yes_to_all:
                self.import_data_from_game("events")
            else:
                if with_window:
                    result = with_window.CustomDialog(
                        title="Project Error",
                        message=f"Could not find any event scripts in project.\n"
                                f"Would you like to decompile and import them from the game directory now?",
                        button_names=("Yes", "No, I'll handle events"),
                        button_kwargs=('YES', 'NO'),
                        cancel_output=1, default_output=1)
                else:
                    result = 1 if input(
                        f"Could not find any event scripts in project.\n"
                        f"Would you like to import them from the game directory now? [y]/n").lower() == 'n' else 0
                if result == 0:
                    self.import_data_from_game("events")

    def save(self, data_type=None):
        """Save given data type ('maps', 'text', etc.) as pickled project file.

        Defaults to saving all types except events, which are handled separately.
        """
        if data_type is None:
            for data_type in [k for k, v in DATA_TYPES.items() if v]:
                self.save(data_type)
        data_type = data_type.lower()
        if data_type not in DATA_TYPES:
            raise ValueError(f"Data type to load should be one of {DATA_TYPES} (or None), not {data_type}.")
        self._save_project_data(getattr(self, _fixed_caps(data_type)), data_type + ".d1s")

    def load(self, data_type=None):
        """Load give data type ('maps', 'text', etc.) from pickled project file. Defaults to loading all types (except
        'events', which are handled manually)."""
        if data_type is None:
            for data_type in [k for k, v in DATA_TYPES.items() if v]:
                self.load(data_type)
        data_type = data_type.lower()
        if data_type not in DATA_TYPES:
            raise ValueError(f"Data type to save should be one of {DATA_TYPES} (or None), not {data_type}.")
        setattr(self, _fixed_caps(data_type), self._load_project_data(data_type + ".d1s"))

    def _save_project_data(self, obj, pickled_path):
        with (self.project_root / pickled_path).open('wb') as f:
            pickle.dump(obj, f)

    def _load_project_data(self, pickled_path):
        with (self.project_root / pickled_path).open('rb') as f:
            return pickle.load(f)

    def import_data(self, data_type=None, import_directory=None):
        """Import data sub-structure from binary game files.

        If `data_type` is None (default), all data types will be imported, in which case the given `import_directory`
        should contain the appropriate folder structure ('map/MapStudio', 'msg/ENGLISH', etc.) for all files.
        """
        if data_type is None:
            for data_type in DATA_TYPES:
                self.import_data(data_type, import_directory)
        data_type = data_type.lower()
        if data_type not in DATA_TYPES:
            raise ValueError(f"Data type to import should be one of {DATA_TYPES} (or None), not {data_type}.")
        import_directory = Path(import_directory)
        data_import_path = self._game_path(data_type, root=import_directory)
        if data_type == "events":
            self._import_events(data_import_path)
        else:
            setattr(self, _fixed_caps(data_type), DATA_TYPES[data_type](data_import_path))

    def import_data_from_game(self, data_type=None):
        """Reads data substructures in game formats from the live game directory."""
        self.import_data(data_type=data_type, import_directory=self.game_root)

    def _import_events(self, import_directory):
        """Converts binary EMEVD to EVS.PY in '[project]/events'."""
        convert_events(output_type="evs.py", output_directory=self.project_root / 'events',
                       input_type="emevd.dcx" if self.game_name == "Dark Souls Remastered" else "emevd",
                       input_directory=import_directory)

    def export_data(self, data_type=None, export_directory=None):
        if data_type is None:
            for data_type in DATA_TYPES:
                self.export_data(data_type, export_directory)
            return
        data_type = data_type.lower()
        if data_type not in DATA_TYPES:
            raise ValueError(f"Data type to export should be one of {DATA_TYPES} (or None), not {data_type}.")
        export_directory = Path(export_directory)
        data_export_path = self._game_path(data_type, root=export_directory)
        data_export_path.mkdir(parents=True, exist_ok=True)
        if data_type == "events":
            self._export_events(data_export_path)
        else:
            getattr(self, _fixed_caps(data_type)).save(data_export_path)

    def export_data_to_game(self, data_type=None):
        """Writes data substructures in game formats in the live game directory, ready for play."""
        self.export_data(data_type=data_type, export_directory=self.game_root)

    def export_timestamped_backup(self, data_type=None):
        timestamped = self.project_root / 'export' / self._get_timestamp(for_path=True)
        self.export_data(data_type=data_type, export_directory=timestamped)

    def _export_events(self, export_directory):
        """Converts EVS.PY in '[project]/events' to binary EMEVD."""
        convert_events(output_type="emevd.dcx" if self.game_name == "Dark Souls Remastered" else "emevd",
                       output_directory=export_directory,
                       input_type="evs.py",
                       input_directory=self.project_root / "events")
        _LOGGER.info("Dark Souls event files (EMEVD) written successfully.")

    def restore_backup(self, target=None):
        """Restores '.bak' files, deleting whatever they would replace."""
        target = Path(target)
        if target.is_file():
            if target.suffix == ".bak":
                if (target.with_suffix("")).is_file():
                    os.remove(str(target.with_suffix("")))
                os.rename(str(target), str(target.with_suffix("")))
            elif not (target.with_suffix(".bak")).is_file():
                raise RestoreBackupError(f"Could not find a file '{str(target.with_suffix('.bak'))} "
                                         f"to restore. No action taken.")
            else:
                os.remove(str(target))
                os.rename(str(target.with_suffix(".bak")), str(target))
        elif target.is_dir():
            count = 0
            for bak_file in target.glob("*.bak"):
                self.restore_backup(bak_file)
                count += 1
            if count == 0:
                raise RestoreBackupError(f"Could not find any '.bak' files to restore in directory '{str(target)}'. "
                                         f"No action taken.")
            else:
                return count

    def launch_game(self, try_force_quit_first=False, threaded=True, debug=False):
        if not psutil:
            raise ModuleNotFoundError(
                "Python package `psutil` required for this method. Install it with `python -m pip install psutil`.")

        if debug and not self.game_name == "Dark Souls Prepare to Die Edition":
            raise SoulstructProjectError(f"Can only launch debug version of Dark Souls PTDE, not {self.game_name}.")
        if try_force_quit_first:
            self.force_quit_game(including_debug=debug)
        self._check_steam_appid_file(self.game_root, self.game_name)
        if debug:
            game_exe_path = self.game_exe_path.parent / (self.game_exe_path.stem + "_DEBUG.exe")
            if game_exe_path.name in (p.name() for p in psutil.process_iter()):
                _LOGGER.warning(f"Cannot launch debug game: {game_exe_path.name} is already running.")
                return
        else:
            game_exe_path = self.game_exe_path

        if not game_exe_path.is_file():
            raise SoulstructProjectError(f"Could not find game executable: {str(game_exe_path)}")

        if self.game_exe_path.name in (p.name() for p in psutil.process_iter()):
            _LOGGER.warning(f"Cannot launch game: {self.game_exe_path.name} is already running.")
            return

        game_exe_str = str(game_exe_path)
        if threaded:
            game_thread = threading.Thread(target=subprocess.run, args=(game_exe_str,))
            game_thread.start()
        else:
            # Blocks Python (including window) until game is closed.
            subprocess.run(game_exe_str)

    def force_quit_game(self, including_debug=False):
        os.system(f"TASKKILL /F /IM {self.game_exe_path.name}")
        if including_debug:
            os.system(f"TASKKILL /F /IM {self.game_exe_path.stem + '_DEBUG.exe'}")

    def launch_gadget(self, threaded=True):
        if self.game_name == "Dark Souls Prepare to Die Edition":
            gadget_path = self.game_root / "DS Gadget.exe"
        elif self.game_name == "Dark Souls Remastered":
            gadget_path = self.game_root / "DSR-Gadget.exe"
        else:
            raise SoulstructProjectError(f"Invalid game name: {self.game_name}")
        if not gadget_path.is_file():
            raise SoulstructProjectError(f"Could not find DS Gadget file: {str(gadget_path)}")
        if gadget_path.name in (p.name() for p in psutil.process_iter()):
            _LOGGER.warning(f"Cannot launch Gadget: {gadget_path.name} is already running.")
            return
        if threaded:
            gadget_thread = threading.Thread(target=subprocess.run, args=(str(gadget_path),))
            gadget_thread.start()
        else:
            # Blocks Python (including window) until DS Gadget is closed.
            subprocess.run(str(gadget_path))

    def get_game_saves(self):
        save_folder = self._get_save_folder()
        return [save_file.stem for save_file in save_folder.glob("*.sl2") if save_file.stem != "DRAKS0005"]

    def _get_save_folder(self):
        if self.game_name == "Dark Souls Remastered":
            steam_id_folders = list(self.game_save_root.glob("*"))
            if len(steam_id_folders) > 1:
                raise SoulstructProjectError(
                    f"Multiple Dark Souls Remastered save folders found in {str(self.game_save_root)}. Please move all "
                    f"of them except your real one.")
            elif not steam_id_folders:
                raise SoulstructProjectError(
                    f"No Dark Souls Remastered save folders found in {str(self.game_save_root)}.")
            return steam_id_folders[0]
        elif self.game_name == "Dark Souls Prepare to Die Edition":
            return self.game_save_root
        else:
            raise SoulstructProjectError(f"Invalid game name: {self.game_name}")

    def load_game_save(self, save_name):
        if not save_name:
            raise SoulstructProjectError("No save name given.")
        save_folder = self._get_save_folder()
        save_file_path = (save_folder / save_name).with_suffix(".sl2")
        if not save_file_path.is_file():
            raise SoulstructProjectError(f"Could not find save file: {str(save_file_path)}")
        active_path_str = str(save_folder / "DRAKS0005.sl2")
        try:
            os.remove(active_path_str)
        except FileNotFoundError:
            pass
        shutil.copy2(str(save_file_path), active_path_str)

    def delete_game_save(self, save_name):
        if not save_name:
            raise SoulstructProjectError("No save name given.")
        save_folder = self._get_save_folder()
        save_file_path = (save_folder / save_name).with_suffix(".sl2")
        if not save_file_path.is_file():
            raise SoulstructProjectError(f"Could not find save file: {str(save_file_path)}")
        os.remove(save_file_path)

    def create_game_save(self, save_name, overwrite=False):
        if not save_name:
            raise SoulstructProjectError("No save name given.")
        save_folder = self._get_save_folder()
        save_file_path = (save_folder / save_name).with_suffix(".sl2")
        active_path = save_folder / "DRAKS0005.sl2"
        if save_file_path.is_file() and not overwrite:
            raise SoulstructProjectError(f"Save file already exists: {str(save_file_path)}")
        if not active_path.is_file():
            raise SoulstructProjectError(f"Active game save file {str(active_path)} could not be found.")
        shutil.copy2(str(active_path), str(save_file_path))

    def load_config(self, with_window: SoulstructProjectWindow = None):
        try:
            with (self.project_root / 'config.json').open('r') as f:
                try:
                    config = json.load(f)
                except json.JSONDecodeError:
                    raise SoulstructProjectError(
                        "Could not interpret 'config.json' file. Check it for errors, or "
                        "delete it to have Soulstruct create a fresh copy on next load."
                    )
                else:
                    try:
                        self.game_name = config['GameName']
                        self.game_exe_path = Path(config['GameExecutable'])
                        self.game_root = Path(config['GameDirectory'])
                        self.game_save_root = Path(config['SaveDirectory'])
                        self.last_import_time = config.get('LastImportTime', None)
                        self.last_export_time = config['LastExportTime']
                    except KeyError:
                        raise SoulstructProjectError(
                            "Project config file does not contain necessary settings. "
                            "Delete it and load the project directory again to create "
                            "a fresh copy and re-link your project to the game."
                        )
        except FileNotFoundError:
            # Create project config file.
            try:
                self.game_root, self.game_exe_path, self.game_name = self._get_game_root(with_window=with_window)
            except SoulstructProjectError as e:
                raise SoulstructProjectError(str(e) + "\n\nAborting project setup.")
            if self.game_name == "Dark Souls Prepare to Die Edition":
                self.game_save_root = Path("~/Documents/NBGI/DarkSouls").expanduser()
            elif self.game_name == "Dark Souls Remastered":
                self.game_save_root = Path("~/Documents/NBGI/DARK SOULS REMASTERED").expanduser()
            self._write_config()
            if with_window:
                result = with_window.CustomDialog(
                    title="Import Project Files",
                    message="Import game files now? This will override any project\n"
                            "files that are already in this folder.",
                    button_names=("Yes, import the files", "No, I'll do it later"),
                    button_kwargs=('YES', 'NO'),
                    cancel_output=None, default_output=0)
            else:
                result = input("Import game files now? This will override any project files\n"
                               "that are already in this folder. [y]/n")
                if result.lower == "n":
                    result = 1
                else:
                    result = 0
            if result == 0:
                self.initialize_project(force_import_from_game=True)

    def _game_path(self, data_type, root=None):
        root = self.game_root if root is None else Path(root)
        data_type = data_type.lower()
        if data_type == 'maps':
            return root / 'map/MapStudio'
        elif data_type == 'params':
            return root / 'param/GameParam'
        elif data_type == 'text':
            return root / 'msg/ENGLISH'
        elif data_type == 'lighting':
            return root / 'param/DrawParam'
        elif data_type == 'events':
            return root / 'event'
        elif data_type == 'ai':
            return root / 'script'
        else:
            raise ValueError(f"Invalid game data type: {data_type}")

    @staticmethod
    def _get_timestamp(for_path=False):
        return datetime.datetime.now().strftime('%Y-%m-%d %H%M%S' if for_path else '%Y-%m-%d %H:%M:%S')

    def _build_config_dict(self):
        return {
            'GameName': self.game_name,
            'GameExecutable': str(self.game_exe_path),
            'GameDirectory': str(self.game_root),
            'SaveDirectory': str(self.game_save_root),
            'LastImportTime': self.last_import_time,
            'LastExportTime': self.last_export_time,
        }

    def _write_config(self):
        try:
            with (self.project_root / 'config.json').open('w') as f:
                json.dump(self._build_config_dict(), f, indent=4)
        except PermissionError:
            raise SoulstructProjectError("No write access to 'config.json' in project directory.")

    @staticmethod
    def _validate_project_directory(project_path, default_root):
        project_path = Path(project_path)
        if not project_path.is_absolute():
            project_path = (default_root / project_path).expanduser().absolute()
        if project_path.is_file():
            raise SoulstructProjectError("You must specify a project *directory*, not a file.")
        if not project_path.is_dir():
            try:
                project_path.mkdir(parents=True, exist_ok=True)
            except NotADirectoryError:
                raise SoulstructProjectError(f"Invalid directory path: {str(project_path)}.")
            except PermissionError:
                raise SoulstructProjectError(f"No write access to create directory: {str(project_path)}.")

        return project_path

    @staticmethod
    def _get_game_root(with_window: SoulstructProjectWindow = None):
        if Path(DSR_PATH).is_dir():
            initial_dir = DSR_PATH
        elif Path(PTDE_PATH).is_dir():
            initial_dir = PTDE_PATH
        else:
            initial_dir = None

        if with_window:
            with_window.CustomDialog(title="Select game for project", message=None, font_size=10,
                                     custom_dialog_subclass=GameRootDialog)
            game_exe = with_window.FileDialog.askopenfilename(
                title="Choose your game executable", initialdir=initial_dir, filetypes=[('Game executable', '.exe')])
            if not game_exe:
                raise SoulstructProjectError("No game executable selected.")
            game_exe = Path(game_exe)
        else:
            message = (
                "Type the full path of the game executable for this project.\n"
                "This can normally be found in:\n\n"
                ""
                "Dark Souls: Prepare to Die Edition:\n"
                "    C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/"
                "DATA/DARKSOULS.exe\n\n"
                ""
                "Dark Souls Remastered:\n"
                "    C:/Program Files (x86)/Steam/steamapps/common/DARK SOULS REMASTERED/DarkSoulsRemastered.exe\n"
            )
            game_exe = input(message + "\nPATH: ")
            try:
                game_exe = Path(game_exe)
                if not Path(game_exe).is_file() and Path(game_exe).suffix == ".exe":
                    raise ValueError
            except ValueError:
                raise SoulstructProjectError(f"Invalid executable file path: {str(game_exe)}.")

        game_root = game_exe.parent
        if (game_root / 'DarkSoulsRemastered.exe').is_file():
            return game_root, game_exe, 'Dark Souls Remastered'
        elif (game_root / 'DARKSOULS.exe').is_file():
            return game_root, game_exe, 'Dark Souls Prepare to Die Edition'
        else:
            raise SoulstructProjectError("Soulstruct projects are only supported for Dark Souls 1 (either version),\n"
                                         "but your selected executable was not a version of Dark Souls.")

    @staticmethod
    def _check_steam_appid_file(game_root, game_name):
        steam_appid_path = Path(game_root) / "steam_appid.txt"
        if not steam_appid_path.is_file():
            if game_name in STEAM_APPIDS:
                with steam_appid_path.open("w") as f:
                    f.write(str(STEAM_APPIDS[game_name]))
                return True
            else:
                raise SoulstructProjectError(f"Invalid game name for creating 'steam_appid.txt': {game_name}")
        return True


def _fixed_caps(data_type):
    if data_type.lower() == "ai":
        return "AI"
    return data_type.capitalize()


MODIFIABLE_FILES = {
    'Dark Souls Prepare to Die Edition': {
        'event': [
            "common.emevd",
            "m10_00_00_00.emevd",
            "m10_01_00_00.emevd",
            "m10_02_00_00.emevd",
            "m11_00_00_00.emevd",
            "m12_00_00_00.emevd",
            "m12_01_00_00.emevd",
            "m13_00_00_00.emevd",
            "m13_01_00_00.emevd",
            "m13_02_00_00.emevd",
            "m14_00_00_00.emevd",
            "m14_01_00_00.emevd",
            "m15_00_00_00.emevd",
            "m15_01_00_00.emevd",
            "m16_00_00_00.emevd",
            "m17_00_00_00.emevd",
            "m18_00_00_00.emevd",
            "m18_01_00_00.emevd",
        ],
        'msg': {
            'ENGLISH': [
                'item.msgbnd',
                'menu.msgbnd',
            ],
        },
        'param': {
            'GameParam': [
                'GameParam.parambnd',
            ],
            'DrawParam': [
                "a10_DrawParam.parambnd",
                "a11_DrawParam.parambnd",
                "a12_DrawParam.parambnd",
                "a13_DrawParam.parambnd",
                "a14_DrawParam.parambnd",
                "a15_DrawParam.parambnd",
                "a16_DrawParam.parambnd",
                "a17_DrawParam.parambnd",
                "a18_DrawParam.parambnd",
                "a99_DrawParam.parambnd",
                "default_DrawParam.parambnd",
            ],
        },
    },
    'Dark Souls Remastered': {
        'event': [
            "common.emevd.dcx",
            "m10_00_00_00.emevd.dcx",
            "m10_01_00_00.emevd.dcx",
            "m10_02_00_00.emevd.dcx",
            "m11_00_00_00.emevd.dcx",
            "m12_00_00_00.emevd.dcx",
            "m12_01_00_00.emevd.dcx",
            "m13_00_00_00.emevd.dcx",
            "m13_01_00_00.emevd.dcx",
            "m13_02_00_00.emevd.dcx",
            "m14_00_00_00.emevd.dcx",
            "m14_01_00_00.emevd.dcx",
            "m15_00_00_00.emevd.dcx",
            "m15_01_00_00.emevd.dcx",
            "m16_00_00_00.emevd.dcx",
            "m17_00_00_00.emevd.dcx",
            "m18_00_00_00.emevd.dcx",
            "m18_01_00_00.emevd.dcx",
        ],
        'msg': {
            'ENGLISH': [
                'item.msgbnd.dcx',
                'menu.msgbnd.dcx',
            ],
        },
        'param': {
            'GameParam': [
                'GameParam.parambnd.dcx'
            ],
            'DrawParam': [
                "a10_DrawParam.parambnd.dcx",
                "a11_DrawParam.parambnd.dcx",
                "a12_DrawParam.parambnd.dcx",
                "a13_DrawParam.parambnd.dcx",
                "a14_DrawParam.parambnd.dcx",
                "a15_DrawParam.parambnd.dcx",
                "a16_DrawParam.parambnd.dcx",
                "a17_DrawParam.parambnd.dcx",
                "a18_DrawParam.parambnd.dcx",
                "a99_DrawParam.parambnd.dcx",
                "default_DrawParam.parambnd.dcx",
            ],
        },
    },
}

SOULSTRUCT_ICON = """
R0lGODlhUABaAOfXAAABAAQABgACAAcAAAgBAAEEAAIFAQsEAwgFCgQHAgUIBAwGBAoGDA4HBQYKBQwJDggLBw8JBwkMCBAKCBELCg
sNCg8MEBANEQwPCxEOEg0QDBIPEw4RDRMQFBASDxQRFRETEBUSFhIUERMUEhUTFxMVExYUFxsTGBQWFBcVGBUXFBgWGRYYFRkXGhkX
GhcYFhMaFxoYGxgZFxgaGBsZHBkbGBwaHRwaHhUdGRocGR0bHhscGhYeGhceGxsdGx4cHyMbIBweHB8dICQcIR0fHCAeISAeIh4gHS
EfIh8gHhsiHx8hHyIgIyAiICMhJCEjICQiJSQiJiIkISUjJiMkIiMlIyYkJysjKCQmJCclKCUnJCgmKSkmKiYoJScoJiknKycpJyoo
KygqKCspLCkrKCwqLSosKSstKiwtKy4sMCwuLC8tMTQsMS0vLTAuMS4wLTEvMi8xLjIwMzMwNDAyLzQxNTEzMDIzMTI0MjUzNzM1Mz
Y0NzQ2Mzc1ODU3NDg2OTk2OjY4NTo3Ozc5Njg5Nzo4PDg6ODs5PTk7OTw6PTo8OT07Pjs9Oj48Pzw+Oz89QEA9QTpANz0/PEE+Qj5A
PUI/Qz9BPj9BP0JAREBCQENBRUFDQERCRkJEQUNFQkRGQ0dFSEhFSUlGSktITEtJTUlLSUxKTkpMSUtNSk9NUFVMUVBOUVJPU1NQVF
RRVVFTUFVSVlJUUVNVUlNVU1VXVVhWWlZYVVlXW1tZXVxaXltdWlxeW11fXF5gXWFjYGJlYmNmY21kamNqYGtpbWxqbnVscnR2c3l3
e3t5fXt9enx+e4OBhYOFgoSGg4uNioyOi4qTjpWXlJyZnZ2anpuemrWyttXX1P////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAP8ALAAAAABQAFoAAAj+AP8JHEiwoMGDCBMqXMiwocOHEC
NKnEixosWLAlFh3MiRoMaOIC+iyhTyYJI6JRPeOaVJU8qCTix6ENAQBIc9oWC5elnQi5SJBzw47MBhyh5XO3kOrMBEIg2aEEFAGRRo
kFKBAp5IlAE1IhEigQJd/YcSYg0HEx7eeBPnTY8dbwgZ9MOnY4K6EAUIAJJwSxYvSf6NiYMAwSctVN68IejlDhmQAkBI1GvCYIIRgL
IMTPKmcJxEPBLJFXiGjxc/kCkKeDCkIKARIwaqGNHZxptEVLQMPGOGjJeLFciMufPvTteBsBrqlUzQTxIJgbVw6ZICAZU7F/r8EViD
EZmyCAP+L6QihYoEyVs8UCn4KgFDJ3r/uReYJAmfO4sWNcpSmAqVCxb0IRAZ3oWhEBMrhJdEGOS98EIWWWxhBV4DURVbQQYONEd8/9
A0RgX2jdKIFlssQgUCKZjQzB7Z/VODGYqAZ9ALTmj1zwVU7OBfEkf0KIEMA2mGEBGOJMTBPxtCxUECO0DHxyhbcMABKycW1gwzFljg
SA05fJfhPw844YAACWCgQgsXPGEGeSZIccQIbxaUCEOljOLJYm90UNgZZCTg3hMJCMCZYm/Ud18HAkwhgATFoCEBIYowgYATlFgiEB
N16KXXCD90GQYZZKzQwgqkTuSAEG+ggcYnZ+xJxpH+HCThpyOKEbFDEneMkoRef0whgQSpSIAEIYQURsku8Hmw6wia7pDDDzsg8EKR
CITxZUJNEeTAtgKwwAIaZ5yRRG87lKtpLprsQMQbv/IhAa9//OooAkjIUiwCvFAigAczeaGIphgEjMA/MYSaoQ4KJbFBQdxqesYRHR
yhgQBk3BooI+wSUcmv9enVQR/ytkovIZZMSkkHTHAgwAiKeKGpXmQUtoIgAq3wWEJ8zDcQA0WwoCkIQFPxg1451PCUygJ4kYNebBQR
qAB3CCKACvciIIcgYSBAiAoCdKEXEeByoUUHItzgQANoPJY0QwKUQVBhKqygwruRUaG0Xi2oPGb+BS4LsMHLItzRBbOC0FHY1Vmn4P
XKX59BiCCDb3tDunrtwLYAk+yMwNQSMAHCTEmPoVcDemNQwcsvk8ds106YYIIc1hYGOeoaMNvBCA7swIkbemHgkF6QtCIIEpt3K0Dg
oOcwsV4NC5BDEaiLIIDUehVmghMoZj2CIIKsDngWN6DhxpjHXS4ELrksQvsZmjYQqAOgC3BDGOSTCYJeoYBCxcsN7CXEAw4QRCsIsS
0VpIBUpDKPXhhguYMgrCBQ0UsjcgEIvUxhYhpYXgLIxxUB8O10L9uVXoIRiv0JoH8C6ED/tsW9bUFBDmRQRAyKp5cL8EAgDxTIDm5G
kC50ASv+vEJUB9BghuURYIP9i98YLiAAAmhKDpqiQgkZIAAqrqYBD2jAthygAilAIQUEagENBXABglwBhw00SBe2MBBNIYoDZjjDDh
wQqA2izoP1E4Ac6KAX/4DiBAs0wQMe0IEtOmAOUtgWAmxGQwkUZGIJ0MAYEFKEyuzmZbFiQgJEwKyZPO2TftJUDfTyBD4ASlMVkAAV
WJDKbslgTEir3iINQibf0eAgAkCCQZChlw0oTC8VkN4BUDemAzzNOJrywBPuqEoW/OpXf9PL/DAggIHRJwlKGIgGnHBLh5AhFpriwB
yQxqwE0K2JvawjKn7mgfuR6Wms1EszUciBG4DQEY/+WQFvCsICNjakEq8gw8uYAEVgbgCFL9tAoDiAzDvwgZR/k8DT6PZM5jngBksT
QKkAcyGBvEAF3VzILWrRQVjKoAXyZEL8NJWAF7xLAjbQlCzMoBcZFAYBDojlon6lFyYIQgt9NIF/AEUQIkxSIQJwQBsF8Erm3ZFMqF
Pgu2iwB70kQy+8KUzeQpgCvaiACSLIgvQQYAI+7E9n/zDqQrYlkDFxZUzw4yIT9FLHcwrApZqigSqsKgummqEw0ezpS5nANQFoQWpk
5YMJIqPNMRw1IYbcogA4EFgD0lUAw3xXoN7FAinoZRVPiYUyBNCCSIjRqRLo6tTmqhfuZUGorgP+gRwEwoFyLWRRBEuqCNw5gqeNqQ
EohWoexSmHQC0zUMbwAgLSUJheevVdz9FLFqxAJgbc9FcCmclCdpXdyYLgCdLb5NOSOqbxYjIJHNCFJF7mGzcwt3goTMHcCiuBP5Tz
ptZ8QbZuCxW4fneZx1udA5oK1Tt6IL26QJ0XZJEGNxTPikzYFd1W8BoB/EEQgBAEAiSwAp9dTiBPiUGHoKYp6SW1BfVDGghwEE4lPF
UWyXCwAFIQXyY4ILVJ3YJe+iBADXM4nEidD4cKM4fF0pV89ZvCxRSBX9QRobXTEMSYWJtUGXAAAzmgpqY0gMU7MmSYAkGUQLB3vXA2
D3UxLIz+EO5whC3vgH2CkIaU5Um3DbxAmlp+avkS4qd/0E0gUCDr5jb7yjMXVgWFQQUqEnxHYkQ5j5pyADXn9+SX/QMIjmCEQwIFRE
CTFVF0RfFdPdYHTY2gMPfp0R0dMIxh/DbSvQOmHDWAASAAgZAdZcjEOv2P5WXUonpJwtxGx4AGMFEAMbifA9yplzc84xl4A10AnCgA
JrwLfl5VARSksAFrjkcDQOyK/Ij5gr9FWFOqFcAEiJZU1L3BGbzQy50FEIAByFO1LbizB1SwrRV02yEuC/c/zBCGG+gFFcjkwJjmlt
rACuAKT9HzG3YRTr0QIAB0rukLPjcHOfB7YUtNCBn+fBfuWAtA0aij2y81dYUr6FkAitHUC8hn70WlG9tQoIIV5tCCDThBhAsBGlRA
QD6MHu+nejavBir9VO41twUoRHILVtoAL4zAC4RwggrYIAFwL6QGIJBBIQeMUQyEQXpbEMTy7sgBumGACGtHHQIA0VzyET2cr0ThBQ
a3Pa1jtyYL7V2Wj23YM6x9vEtyWNxfhgBiaDjSPKjftjjAgAtsgIlX74JLKxCRMdEAaVjWMVZ3QNc6vwwDi3+ZIKjxeL1wYGlEh+uY
LnAC1Q7uHy9ggUPK2EYVrN0TaPBYYTpAtwQcOFBNfmojqnEM1HVvZTxAHZa3lQQudkEFDiE5ryf+pgKuIfqmG0CaBJBWmC3gVM/VqM
Zlp0e9HNSPb+6vvgO6IIjuN6QCj2UEMMlA+BT2CAEJgDQBWD1aIAxAhX7Nh04rszp3RzRjkAMt5FPY9xDa9w99QxPzVk1mcASb0wCZ
lQDDVBhaMEYvwwjVoD4v126mg2XVxwSsQDMR0RpLRRNnAHfLkyV64TL1Y15PRQd8JHc35UEv8yvb4gmesGcOoVT/sEW9FkcaYAETYA
HA9FTI9HI+KG96UQRCUBgJUAEVsFnM8waeoIQUwXla1IB6QQNX0H93dAcmREx64Qy98DIt0AqFAT1kIgI8JQF3wlYXMXYZKABqeHpP
FV486AD+z+AMqDMKGlYEFfROPCUFbUGGFjEmIuAAFZAGTcIDv7ZTT9UCvrAHzfU11mALJ3VgHiAHGHU3J0RHenEEgxALRLARcPUPO/
AITbJi2zJMA3hHLwANQVg50UALMqBflFVPBSdv9XMEiRALssARPaAXPeBeTSIAOLAtmiVPowNLoSiKAkBTAmALt3BSIiQ/WYaFL1ML
sjCLtCg9tthgc0ReCrVqHIBiCLAHvoAAGkB6pPUC+RZOBmc6Z3YEtZBGG3EBvpMAnxIGQiACWqQpRqZld7ctc3BI3ZcCYxAGrHg8Gb
R4DqAFfDCCCMAJBPEENjIRBjcfO+AFYUAEJhZrWkb+PnQgB9sykxXpPF4AQk/Dj+02NbmBaGmgCWkQYU/ABHYgFBRBBkj5DyMgBEJw
BCmiWhVwA0wkdA2wDBXJbw2TZ4GyjwKgAR3EAVqkAlrgBprgBjEwTpKRBHNwEUuiMw5gAo8ACZrSNyCwNA6AC7jgcdtSUKh0OkRATW
YQTRzAbyxABZpQCSGVXftVEVRwOkDUBfq3L+6EkBcQKKMwCtHHA8p2dy1wUjUVXAKwCZygewqBBiWRg13wXcxmOqM0SrrIPJyZVOGn
F3Mwb53wC5yQAqf5Ei4zAnwQPxWgZXagZ7MZV3c1CsEFDMBgmmOREOTRO3wTBgJgB6MEabEnJXr+IQejEGybwCHPqRBx5wlc0XES5U
miNErVBCoIkAR8FJ63NYMqMAp3Nm88WAPqmWYIQAdHAp8Jw3n/4AmFNQfdWWAJ0GYCcATFWZ2OsALD558MwTUC0Ql4s0cuBYJPQ5B6
UQOjIDOK0EYQKhBUwBxA5B6uUARjtC1aFCiiwBUtYAo0UBi6EKIGUQF3QKLFiJr/4AopKlkysDQtMAqjNAW7wAA0ahDXsRto4BL/IA
jQ030jQAWWsC34OUqm0JYyQBJHiksEAQOWIhBCwAi/oQi6QAkUKQdwAAdAsqUUsQJ8wByDoClb0AqN0J9sShEmNmJ6oQX6oRsCQSFL
eacD4R8wByEZtjIIO1AijYAQlCioDEEIsVAuXBCojloRAuBZP1GpG/Erq6SpGCEBNQCq4RkQADs=
"""


class RestoreBackupError(Exception):
    pass


class GameRootDialog(CustomDialog):

    def build(self, message, font_size, font_type, button_names, button_kwargs):
        with self.set_master(auto_rows=0, padx=20, pady=20):
            self.Label(text="Navigate to the game executable for this project.\n"
                            "In a standard Steam installation, this will be:", pady=10)
            self.Label(text="Dark Souls: Prepare to Die Edition", font_type="Consolas")
            self.Label(text="C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/"
                            "DATA/DARKSOULS.exe", font_size=8, font_type="Consolas", bg='#000')
            self.Label(text="Dark Souls Remastered", font_type="Consolas")
            self.Label(text="C:/Program Files (x86)/Steam/steamapps/common/DARK SOULS REMASTERED/"
                            "DarkSoulsRemastered.exe", font_size=8, font_type="Consolas", bg='#000')
            self.Label(text="Steam can help you find your Steam installation.", pady=10)
            self.build_buttons(button_names, button_kwargs)
