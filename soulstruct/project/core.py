"""
TODO:
    - Manage ESD. Unpack and store in 'esdpy' subdirectory.
"""
from __future__ import annotations

import datetime
import json
import os
import pickle
from functools import wraps
from pathlib import Path
from typing import Optional

from soulstruct.core import SoulstructError
from soulstruct.events.darksouls1.core import convert_events
from soulstruct.maps import DarkSoulsMaps
from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.text import DarkSoulsText
from soulstruct.utilities import find_steam_common_paths, word_wrap
from soulstruct.utilities.window import SoulstructSmartFrame

from .entities import SoulstructEntityEditor
from .events import SoulstructEventEditor
from .lighting import SoulstructLightingEditor
from .links import WindowLinker
from .maps import SoulstructMapEditor
from .params import SoulstructParamsEditor
from .text import SoulstructTextEditor

__all__ = ['SoulstructProject', 'SoulstructProjectError', 'SoulstructProjectWindow']

DATA_TYPES = {
    'maps': DarkSoulsMaps,
    'params': DarkSoulsGameParameters,
    'lighting': DarkSoulsLightingParameters,
    'text': DarkSoulsText,
    'events': None,  # modified via EVS script files
}


class SoulstructProjectError(SoulstructError):
    pass


def _with_config_write(func):
    @wraps(func)
    def project_method(self: SoulstructProject, *args, **kwargs):
        func(self, *args, **kwargs)
        self._write_config()

    return project_method


class SoulstructProjectWindow(SoulstructSmartFrame):
    maps_tab: Optional[SoulstructMapEditor]
    entities_tab: Optional[SoulstructEntityEditor]
    params_tab: Optional[SoulstructParamsEditor]
    lighting_tab: Optional[SoulstructLightingEditor]
    text_tab: Optional[SoulstructTextEditor]
    events_tab: Optional[SoulstructEventEditor]

    TAB_ORDER = ['maps', 'entities', 'params', 'lighting', 'text', 'events']

    def __init__(self, project_path, master=None):
        super().__init__(master=master, toplevel=True, icon_data=SOULSTRUCT_ICON, window_title="Soulstruct")
        self.withdraw()

        if not project_path:
            self.dialog(
                title="Choose Soulstruct project directory",
                message="Navigate to your Soulstruct project directory.\n\n" + word_wrap(
                    "If you want to create a new project, create an empty directory and select it."
                    "The name of the directory will be the name of the project.", 50),
                button_names='OK', button_kwargs='OK')
            project_path = self.FileDialog.askdirectory(
                title="Choose Soulstruct project directory", initialdir=str(Path('~/Documents').expanduser()))
            if not project_path:
                raise SoulstructProjectError(word_wrap("No directory chosen. Quitting Soulstruct.", 50))

        try:
            self.project = SoulstructProject(project_path, with_window=self)
        except SoulstructProjectError as e:
            self.deiconify()
            self.dialog(title="Project Error", message=word_wrap(str(e), 50) + "\n\nAborting startup.",
                        button_kwargs='OK')
            raise  # TODO: should not raise an error; just flag startup failure.
        except Exception as e:
            self.deiconify()
            msg = "Internal Python Error:\n\n" + word_wrap(str(e), 50) + "\n\nAborting startup."
            self.dialog(title="Unknown Error", message=msg, button_kwargs='OK')
            raise  # TODO: should not raise an error; just flag startup failure.

        self.linker = WindowLinker(self)  # TODO: Individual editors should have a lesser linker.

        self.page_tabs = self.Notebook(name="project_notebook", sticky='nsew')
        self.maps_tab = None
        self.entities_tab = None
        self.params_tab = None
        self.text_tab = None
        self.lighting_tab = None
        self.events_tab = None

        self.toplevel.minsize(700, 500)
        # self.toplevel.protocol("WM_DELETE_WINDOW", self.confirm_quit)  # TODO: enable on release
        self.build()
        self.deiconify()

    def build(self):
        self.build_top_menu()

        tab_frames = {tab_name: self.Frame(frame=self.page_tabs, sticky='nsew', row_weights=[1], column_weights=[1])
                      for tab_name in self.TAB_ORDER}

        self.maps_tab = self.SmartFrame(
            frame=tab_frames['maps'], smart_frame_class=SoulstructMapEditor,
            maps=self.project.Maps, linker=self.linker)
        self.maps_tab.grid(sticky='nsew')

        self.entities_tab = self.SmartFrame(
            frame=tab_frames['entities'], smart_frame_class=SoulstructEntityEditor,
            maps=self.project.Maps, evs_directory=self.project.project_root / "events", linker=self.linker)
        self.entities_tab.grid(sticky='nsew')

        self.params_tab = self.SmartFrame(
            frame=tab_frames['params'], smart_frame_class=SoulstructParamsEditor,
            params=self.project.Params, linker=self.linker)
        self.params_tab.grid(sticky='nsew')

        self.lighting_tab = self.SmartFrame(
            frame=tab_frames['lighting'], smart_frame_class=SoulstructLightingEditor,
            lighting=self.project.Lighting, linker=self.linker)
        self.lighting_tab.grid(sticky='nsew')

        self.text_tab = self.SmartFrame(
            frame=tab_frames['text'], smart_frame_class=SoulstructTextEditor,
            text=self.project.Text, linker=self.linker)
        self.text_tab.grid(sticky='nsew')

        self.events_tab = self.SmartFrame(
            frame=tab_frames['events'], smart_frame_class=SoulstructEventEditor,
            evs_directory=self.project.project_root / "events", game_root=self.project.game_root,
            dcx=self.project.game_name == "Dark Souls Remastered")
        self.events_tab.grid(sticky='nsew')

        # self.build_runtime_tab(tab_frames['runtime'])  # TODO: game launcher, etc.

        for tab_name, tab_frame in tab_frames.items():
            self.page_tabs.add(tab_frame, text=f'  {tab_name.capitalize()}  ')

        self.set_key_bindings()

        self.set_geometry()

    def build_top_menu(self):
        top_menu = self.Menu()

        file_menu = self.Menu(tearoff=0)
        file_menu.add_command(label="Save Entire Project", foreground='#FFF', command=self._save_data)
        file_menu.add_separator()
        for import_dir in (self.project.game_root, None):
            import_menu = self.Menu(tearoff=0)
            import_menu.add_command(
                label=f"Import Everything", foreground='#FFF',
                command=lambda i=import_dir: self._import_data(import_directory=i))
            import_menu.add_separator()
            for data_type in DATA_TYPES:
                import_menu.add_command(
                    label=f"Import {data_type.capitalize()}", foreground='#FFF',
                    command=lambda d=data_type, i=import_dir: self._import_data(d, import_directory=i))
            file_menu.add_cascade(label=f"Import from{' Game' if import_dir else '...'}",
                                  foreground='#FFF', menu=import_menu)
        for export_dir in (self.project.game_root, None):
            export_menu = self.Menu(tearoff=0)
            export_menu.add_command(
                label=f"Export Everything", foreground='#FFF',
                command=lambda e=export_dir: self._export_data(export_directory=e))
            export_menu.add_separator()
            for data_type in DATA_TYPES:
                export_menu.add_command(
                    label=f"Export {data_type.capitalize()}", foreground='#FFF',
                    command=lambda d=data_type, e=export_dir: self._export_data(d, export_directory=e))
            file_menu.add_cascade(label=f"Export to{' Game' if export_dir else '...'}",
                                  foreground='#FFF', menu=export_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Restore .bak File", foreground='#FFF',
                              command=lambda: self._restore_backup(full_folder=False))
        file_menu.add_command(label="Restore .bak Files", foreground='#FFF',
                              command=lambda: self._restore_backup(full_folder=True))
        file_menu.add_separator()
        file_menu.add_command(label="Quit", foreground='#FFF', command=self.confirm_quit)
        top_menu.add_cascade(label="File", menu=file_menu)

        # TODO: edit commands
        # edit_menu = self.Menu(tearoff=0)
        # edit_menu.add_command(label="Undo", foreground='#FFF', command=lambda: print("Undo"))
        # edit_menu.add_command(label="Redo", foreground='#FFF', command=lambda: print("Redo"))
        # edit_menu.add_command(label="Copy", foreground='#FFF', command=lambda: print("Copy"))
        # edit_menu.add_command(label="Cut", foreground='#FFF', command=lambda: print("Cut"))
        # edit_menu.add_command(label="Paste", foreground='#FFF', command=lambda: print("Paste"))
        # top_menu.add_cascade(label="Edit", menu=edit_menu)

        self.toplevel.config(menu=top_menu)

    def build_runtime_tab(self, main_frame):
        """
        TODO:
            - Option to launch game? And an option to launch Game + Gadget?
            - Option to restart game, if it's running?
            - Option to connect to running game and extract current player XYZ coordinates into an MSB entry?
            - Connect to save files (Documents/NGBI/...) and show Combobox + load button. (Also 'backup current save'.)
        """
        pass

    def set_key_bindings(self):
        self.bind_all("<Control-s>", lambda _: self._save_data(self.current_data_type))
        self.bind_all("<Control-e>", lambda _: self._export_data(self.current_data_type, self.project.game_root))
        self.bind_all("<Shift-Control-e>", lambda _: self._export_data(self.current_data_type, None))

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
            project_data = getattr(self.project, data_type.capitalize())
            setattr(getattr(self, f'{data_type}_tab'), data_type.capitalize(), project_data)

    def confirm_quit(self):
        if self.dialog(title="Quit Soulstruct?",
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

    def _save_data(self, data_type=None):
        if data_type == "events":
            self.events_tab.save_selected_evs()
            self.mimic_click(self.events_tab.save_button)
            return
        # TODO: progress bar
        self.project.save(data_type)
        if data_type is None:
            self.events_tab.save_all_evs()
        self._flash_red_bg(self)

    def _export_data(self, data_type=None, export_directory=None):
        if export_directory is None:
            export_directory = self._choose_directory()
            if export_directory is None:
                return  # Abort export.
        if data_type == "events":
            self.events_tab.export_selected_evs(export_directory)
            self.mimic_click(self.events_tab.export_button)
            return
        # TODO: progress bar
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
            return self.dialog("Restore Backup Error", message=str(e))
        if count:
            return self.dialog("Restore Successful", f"{count} '.bak' files restored in folder\n'{str(target)}'.")
        return self.dialog("Restore Successful", f"Backup file '{str(target)}' restored.")

    def _choose_directory(self, initial_dir=None, **kwargs):
        if initial_dir is None:
            initial_dir = str(self.project.project_root)
        directory = self.FileDialog.askdirectory(initialdir=initial_dir, **kwargs)
        return Path(directory) if directory is not None else None


class SoulstructProject(object):
    """Manages a directory of easily-modded Soulstruct files that can imported and exported.

    It is recommended that you create one of these projects for each Soulstruct-based mod.

    Currently supports only Dark Souls 1.

    TODO:
        - Eventually have subclasses for different games, with shared methods here.
        - Auto-save scheduled Tk functions that operate at ten minute intervals.
        - Inspect PTD directory for lack of UDSFM when imported.
        - Store location of game save data for a future save manager.
    """
    _DEFAULT_PROJECT_ROOT = '~/Documents/Soulstruct/'

    def __init__(self, project_path="", with_window: SoulstructProjectWindow = None):

        self.game_name = ''
        self.game_root = Path()
        self.last_import_time = ''
        self.last_export_time = ''
        # TODO: Record last edit time for each file/structure.

        # Initialize with empty structures.
        self.Text = DarkSoulsText()
        self.Params = DarkSoulsGameParameters()
        self.Lighting = DarkSoulsLightingParameters()
        self.Maps = DarkSoulsMaps()

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
                        result = with_window.dialog(
                            title="Project Error",
                            message=f"Could not find saved {data_type.capitalize()} data in project.\n"
                                    f"Would you like to import it from the game directory now?",
                            button_names=("Yes", "Yes to All", "No, quit now"),
                            button_kwargs=('YES', 'YES', 'NO'),
                            cancel_output=2, default_output=2
                        )
                    else:
                        result = input(
                            f"Could not find saved {data_type.capitalize()} data in project.\n"
                            f"Would you like to import it from the game directory now? [y]/n")
                        if result.lower == "n":
                            result = 2
                        else:
                            result = 0
                    if result in {0, 1}:
                        self.import_data_from_game(data_type)
                        self.save(data_type)
                        if result == 1:
                            yes_to_all = True
                    else:
                        raise SoulstructProjectError("Could not open project files.")

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
        self._save_project_data(getattr(self, data_type.capitalize()), data_type + ".d1s")

    def load(self, data_type=None):
        """Load give data type ('maps', 'text', etc.) from pickled project file. Defaults to loading all types (except
        'events', which are handled manually)."""
        if data_type is None:
            for data_type in [k for k, v in DATA_TYPES.items() if v]:
                self.load(data_type)
        data_type = data_type.lower()
        if data_type not in DATA_TYPES:
            raise ValueError(f"Data type to save should be one of {DATA_TYPES} (or None), not {data_type}.")
        setattr(self, data_type.capitalize(), self._load_project_data(data_type + ".d1s"))

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
            setattr(self, data_type.capitalize(), DATA_TYPES[data_type](data_import_path))

    def import_data_from_game(self, data_type=None):
        """Reads data substructures in game formats from the live game directory."""
        self.import_data(data_type=data_type, import_directory=self.game_root)

    def _import_events(self, import_directory):
        """Converts binary EMEVD to EVS.PY in '[project]/events'."""
        convert_events(output_type="evs.py", output_directory=self.project_root / 'events',
                       input_directory=import_directory)

    def export_data(self, data_type=None, export_directory=None):
        if data_type is None:
            for data_type in DATA_TYPES:
                self.export_data(data_type, export_directory)
        data_type = data_type.lower()
        if data_type not in DATA_TYPES:
            raise ValueError(f"Data type to export should be one of {DATA_TYPES} (or None), not {data_type}.")
        export_directory = Path(export_directory)
        data_export_path = self._game_path(data_type, root=export_directory)
        data_export_path.mkdir(parents=True, exist_ok=True)
        if data_type == "events":
            self._export_events(data_export_path)
        else:
            getattr(self, data_type.capitalize()).save(data_export_path)

    def export_data_to_game(self, data_type=None):
        """Writes data substructures in game formats in the live game directory, ready for play."""
        self.export_data(data_type=data_type, export_directory=self.game_root)

    def export_timestamped_backup(self, data_type=None):
        timestamped = self.project_root / 'export' / self._get_timestamp(for_path=True)
        self.export_data(data_type=data_type, export_directory=timestamped)

    def _export_events(self, export_directory):
        """Converts EVS.PY in '[project]/events' to binary EMEVD."""
        convert_events(output_type="emevd", output_directory=export_directory,
                       input_directory=self.project_root / "events")

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
                        self.game_root = Path(config['GameDirectory'])
                        self.last_import_time = config.get('LastImportTime', None)
                        self.last_export_time = config['LastExportTime']
                    except KeyError:
                        raise SoulstructProjectError(
                            "Project config file does not contain necessary settings. "
                            "Delete it and load the project directory again to create "
                            "a fresh copy."
                        )
        except FileNotFoundError:
            # Create project config file.
            try:
                self.game_root, self.game_name = self._get_game_root(with_window=with_window)
            except SoulstructProjectError as e:
                raise SoulstructProjectError(str(e) + "\n\nAborting project setup.")
            self._write_config()
            if with_window:
                result = with_window.dialog(title="Initial project load",
                                            message="Import game files now? This will override any project files\n"
                                                    "that are already in this folder.",
                                            button_names=("Yes, import the files", "No, I'll do it later"),
                                            button_kwargs=('YES', 'NO'),
                                            cancel_output=1, default_output=1)
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

    @staticmethod
    def _get_timestamp(for_path=False):
        return datetime.datetime.now().strftime('%Y-%m-%d %H%M%S' if for_path else '%Y-%m-%d %H:%M:%S')

    def _build_config_dict(self):
        # TODO: Separate import times for different types.
        return {
            'GameName': self.game_name,
            'GameDirectory': str(self.game_root),
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
        for common_path in find_steam_common_paths():
            dsr_path = Path(common_path, 'DARK SOULS REMASTERED')
            if dsr_path.is_dir():
                initial_dir = str(dsr_path)
                break
            ptd_path = Path(common_path, 'Dark Souls Prepare to Die Edition/DATA')
            if ptd_path.is_dir():
                initial_dir = str(ptd_path)
                break
        else:
            initial_dir = None

        message = (
            ("Navigate to " if with_window else "Type the full path of ") +
            "the game executable for this project.\n"
            "This can normally be found in:\n\n"
            ""
            "Prepare to Die Edition:\n"
            "C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA/DARKSOULS.exe\n\n"
            ""
            "Remastered:\n"
            "C:/Program Files (x86)/Steam/steamapps/common/DARK SOULS REMASTERED/DarkSoulsRemastered.exe\n\n"
            ""
            "Otherwise, you can use Steam to find your Steam directory."
        )
        if with_window:
            with_window.dialog(title="Select game for project", message=message, font_size=12,
                               button_names='OK', button_kwargs='OK')
            game_exe = with_window.FileDialog.askopenfilename(
                title="Choose your game executable", initialdir=initial_dir, filetypes=[('Game executable', '.exe')])
            if not game_exe:
                raise SoulstructProjectError("No game executable selected.")
            game_exe = Path(game_exe)
        else:
            game_exe = input(message + "\nPATH: ")
            try:
                game_exe = Path(game_exe)
                if not Path(game_exe).is_file() and Path(game_exe).suffix == ".exe":
                    raise ValueError
            except ValueError:
                raise SoulstructProjectError(f"Invalid executable file path: {str(game_exe)}.")

        game_root = game_exe.parent
        if (game_root / 'DarkSoulsRemastered.exe').is_file():
            return game_root, 'Dark Souls Remastered'
        elif (game_root / 'DARKSOULS.exe').is_file():
            return game_root, 'Dark Souls Prepare to Die Edition'
        else:
            raise SoulstructProjectError("Soulstruct projects are only supported for Dark Souls 1 (either version),\n"
                                         "but your selected executable was not a version of Dark Souls.")


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
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
"""


class RestoreBackupError(Exception):
    pass
