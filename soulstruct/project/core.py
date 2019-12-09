from __future__ import annotations

import datetime
import json
import pickle
import shutil
from functools import wraps
from pathlib import Path
from textwrap import wrap
from tkinter.ttk import Notebook
from typing import Optional

from soulstruct.core import SoulstructError
from soulstruct.maps import DarkSoulsMaps
from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.project.lighting import SoulstructLightingEditor
from soulstruct.project.links import WindowLinker
from soulstruct.project.maps import SoulstructMapEditor
from soulstruct.project.params import SoulstructParamsEditor
from soulstruct.project.text import SoulstructTextEditor
from soulstruct.text import DarkSoulsText
from soulstruct.utilities import find_steam_common_paths, traverse_path_tree, word_wrap
from soulstruct.utilities.window import SoulstructSmartFrame

__all__ = ['SoulstructProject', 'SoulstructProjectError', 'SoulstructProjectWindow']


class SoulstructProjectError(SoulstructError):
    pass


def _with_config_write(func):
    @wraps(func)
    def project_method(self: SoulstructProject, *args, **kwargs):
        func(self, *args, **kwargs)
        self._write_config()

    return project_method


class SoulstructProjectWindow(SoulstructSmartFrame):

    page_tabs: Optional[Notebook]
    params_tab: Optional[SoulstructParamsEditor]
    text_tab: Optional[SoulstructTextEditor]
    maps_tab: Optional[SoulstructMapEditor]

    TAB_ORDER = ['maps', 'text', 'params', 'lighting', 'main']  # TODO

    def __init__(self, project: SoulstructProject, master=None):
        super().__init__(master=master, toplevel=True, window_title="Soulstruct")
        self.project = project
        self.linker = WindowLinker(self)  # TODO: Individual editors should have a lesser linker.

        self.page_tabs = None
        self.text_tab = None
        self.params_tab = None
        self.lighting_tab = None
        self.maps_tab = None
        self.set_geometry()

    def build(self):
        self.top_menu = self.Menu()
        self.top_menu.add_command(label="Hello", command=lambda: print("Hello there."))
        self.top_menu.add_separator()
        self.top_menu.add_command(label="Quit", command=self.destroy)
        self.toplevel.config(menu=self.top_menu)
        # TODO: Pulldown.

        self.page_tabs = self.Notebook(row=0)

        tab_frames = {tab_name: self.Frame(frame=self.page_tabs) for tab_name in self.TAB_ORDER}

        self.maps_tab = self.SmartFrame(
            frame=tab_frames['maps'], smart_frame_class=SoulstructMapEditor,
            maps=self.project.Maps, linker=self.linker, no_grid=True)
        self.maps_tab.pack()

        self.params_tab = self.SmartFrame(
            frame=tab_frames['params'], smart_frame_class=SoulstructParamsEditor,
            params=self.project.Params, linker=self.linker, no_grid=True)
        self.params_tab.pack()

        self.text_tab = self.SmartFrame(
            frame=tab_frames['text'], smart_frame_class=SoulstructTextEditor,
            text=self.project.Text, linker=self.linker, no_grid=True)
        self.text_tab.pack()

        self.lighting_tab = self.SmartFrame(
            frame=tab_frames['lighting'], smart_frame_class=SoulstructLightingEditor,
            lighting=self.project.Lighting, linker=self.linker, no_grid=True
        )
        self.lighting_tab.pack()

        self.build_main_tab(tab_frames['main'])

        # TODO: Lighting. Events (somehow). Game saves.

        for tab_name, tab_frame in tab_frames.items():
            self.page_tabs.add(tab_frame, text=f'  {tab_name.capitalize()}  ')

        # self.resizable(False, False)  # TODO
        self.set_geometry()
        self.deiconify()

    def build_main_tab(self, main_frame):
        """
        TODO:
            - SAVE ALL. Need a way to detect which files have actually changed (related to undo, redo, etc.).
            - Put subtype import options on those editor screens.
            - Button here to 'import all' from linked game directory, and from arbitrary directory (e.g. export folder).
            - Option to launch game? And an option to launch Game + Gadget?
            - Option to restart game, if it's running?
            - Buttons to 'export all to game' and 'export to dest'. Individual subtype buttons on those editor screens.
            - IMPORT EVENTS. Unpack into EVS and store in 'evs' subdirectory.
            - IMPORT ESD. Unpack and store in 'ezs' subdirectory.
            - Connect to save files (Documents/NGBI/...) and show Combobox + load button. (Also 'backup current save'.)
            - Make use of config.json project file. (Save directory, last times, etc.)

        """
        with self.set_master(main_frame, auto_columns=0):
            with self.set_master(auto_rows=0, grid_defaults={'padx': 20, 'pady': 10}):
                self.Button(text="Import All from Game Directory", bg='#235', width=30, font_size=15,
                            command=lambda: self.project.load_project(force_game_import=True))
                self.Button(text="Import Params", bg='#235', width=30, font_size=15,
                            command=self.project.import_params)
                self.Button(text="Import Text", bg='#235', width=30, font_size=15,
                            command=self.project.import_text)
                self.Button(text="Import Lighting", bg='#235', width=30, font_size=15,
                            command=self.project.import_lighting)
                self.Button(text="Import Maps", bg='#235', width=30, font_size=15,
                            command=self.project.import_maps)
                self.Button(text='Export Project', bg='#623', width=30, font_size=15,
                            command=self.project.export_project)

    def reload_data(self, name: str, data):
        name = name.lower()
        if name not in self.TAB_ORDER:
            raise ValueError(f"Invalid data type name: {name}")
        setattr(getattr(self, f'{name}_tab'), name.capitalize(), data)

    def destroy(self):
        """Destruction takes a second or so, so we withdraw first to hide the awkward lag."""
        self.withdraw()
        super().destroy()


class SoulstructProject(object):
    """Manages a directory of files that can be modded and 'pushed' into the appropriate game directory at will.

    It is recommended that you create one of these projects for each Soulstruct-based mod.

    Currently supports only Dark Souls 1.

    TODO:
        - Eventually have subclasses for different games, with shared methods here.
        - Auto-save scheduled Tk functions that operate at ten minute intervals.
        - Inspect PTD directory for lack of UDSFM when imported.
        - Store location of game save data for a future save manager.
    """
    _DEFAULT_PROJECT_ROOT = '~/Documents/Soulstruct/'

    def __init__(self, project_path: str = ''):

        self._window = SoulstructProjectWindow(project=self, master=None)

        self.game_name = ''
        self.game_root = Path()
        self.last_import_time = ''
        self.last_push_time = ''
        # TODO: Record last edit time for each file/structure.

        # Initialize with empty structures.
        self.Text = DarkSoulsText()
        self.Params = DarkSoulsGameParameters()
        self.Lighting = DarkSoulsLightingParameters()
        self.Maps = DarkSoulsMaps()

        try:
            self.project_root = self._validate_project_directory(project_path, self._DEFAULT_PROJECT_ROOT)
            self.load_config()
            self.load_project()
        except SoulstructProjectError as e:
            self.dialog(title="Project Error", message='\n'.join(wrap(str(e), 50)) + "\n\nAborting startup.",
                        button_kwargs='OK')
            raise  # TODO: should not raise an error; just flag startup failure.
        except Exception as e:
            msg = "Internal Python Error:\n\n" + '\n'.join(wrap(str(e), 50)) + "\n\nAborting startup."
            self.dialog(title="Unknown Error", message=msg, button_kwargs='OK')
            raise  # TODO: should not raise an error; just flag startup failure.

        self._window.build()
        self._window.wait_window()

    def load_project(self, force_game_import=False):
        """Load project structures (params, text, etc.) into class as attributes."""
        for attr, attr_class, pickled, import_func in zip(
                ('Text', 'Params', 'Lighting', 'Maps'),
                (DarkSoulsText, DarkSoulsGameParameters, DarkSoulsLightingParameters, DarkSoulsMaps),
                ('text.d1s', 'params.d1s', 'lighting.d1s', 'maps.d1s'),
                (self.import_text, self.import_params, self.import_lighting, self.import_maps)):
            try:
                if force_game_import:
                    raise FileNotFoundError
                with (self.project_root / pickled).open('rb') as f:
                    setattr(self, attr, pickle.load(f))
            except FileNotFoundError:
                if force_game_import or self.dialog(
                        title="Project Error",
                        message=f"Could not find saved {attr} data in project ('{pickled}').\n"
                                f"Would you like to import it from the game directory?",
                        button_names=('Yes, import the files', 'No, quit now'), button_kwargs=('YES', 'NO'),
                        cancel_output=1, default_output=1) == 0:
                    import_func()
                else:
                    raise SoulstructProjectError("Could not open project files.")
                self._window.deiconify()

    def pickle_in_project(self, obj, pickled_path):
        with (self.project_root / pickled_path).open('wb') as f:
            pickle.dump(obj, f)

    # IMPORT METHODS. These import game data sub-structures from the live game directory, and save them
    # as pickled structure instances inside the project directory.

    def import_text(self):
        self.Text = DarkSoulsText(self.game_root / 'msg/ENGLISH')
        self._window.reload_data('text', self.Text)
        self.pickle_in_project(self.Text, 'text.d1s')

    def import_params(self):
        self.Params = DarkSoulsGameParameters(self.game_root / 'param/GameParam/GameParam.parambnd')
        self._window.reload_data('params', self.Params)
        self.pickle_in_project(self.Params, 'params.d1s')

    def import_lighting(self):
        self.Lighting = DarkSoulsLightingParameters(self.game_root / 'param/DrawParam')
        self._window.reload_data('lighting', self.Lighting)
        self.pickle_in_project(self.Lighting, 'lighting.d1s')

    def import_maps(self):
        self.Maps = DarkSoulsMaps(self.game_root / 'map/MapStudio')
        self._window.reload_data('maps', self.Maps)
        self.pickle_in_project(self.Maps, 'maps.d1s')

    def export_project(self, export_directory: str = None):
        """Writes all data substructures in game formats in the chosen directory, under the same folders they
        would be in the live game directory.

        By default, the root export directory is 'export/{timestamp}' within the project directory.
        """
        if export_directory is None:
            export_directory = self.project_root / 'export' / self._get_timestamp(for_path=True)

        maps_path = export_directory / 'map/MapStudio/'
        maps_path.mkdir(parents=True, exist_ok=True)
        self.Maps.save(maps_path)

        params_path = export_directory / 'param/GameParam/GameParam.parambnd'  # DCX compression handled by BND
        params_path.parent.mkdir(parents=True, exist_ok=True)
        self.Params.save(params_path)

        text_path = export_directory / 'msg/ENGLISH/'
        text_path.mkdir(parents=True, exist_ok=True)
        self.Text.save(text_path)

        # TODO: can't save DrawParams yet.
        # lighting_path = os.path.join(export_directory, 'param/DrawParam/')
        # os.makedirs(lighting_path, exist_ok=True)
        # self.Lighting.write(lighting_path)

    def export_project_to_game(self):
        """Writes all data substructures in game formats in the live game directory, ready for play."""
        self.export_project(self.game_root)

    def load_config(self):
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
                        self.last_push_time = config['LastPushTime']
                    except KeyError:
                        raise SoulstructProjectError(
                            "Project config file does not contain necessary settings. "
                            "Delete it and load the project directory again to create "
                            "a fresh copy."
                        )
        except FileNotFoundError:
            # Create project config file.
            try:
                self.game_root, self.game_name = self._get_game_root()
            except SoulstructProjectError as e:
                raise SoulstructProjectError(str(e) + "\n\nAborting project setup.")
            self._write_config()
            if self.dialog(title="Initial project load",
                           message="Import game files now? This will override any '.d1s' files\n"
                                   "that are already in this folder.",
                           button_names=("Yes, import the files", "No, I'll do it later"),
                           button_kwargs=('YES', 'NO'),
                           cancel_output=1, default_output=1) == 0:
                self.load_project(force_game_import=True)
            self._window.deiconify()

    @_with_config_write
    def push(self):
        # TODO: Not using this at the moment. This would copy existing game-format files.
        print("# Pushing project files to game...")  # TODO: log
        for path_sequence in traverse_path_tree(MODIFIABLE_FILES[self.game_name]):
            project_file = self.project_root.joinpath(*path_sequence)
            game_file = self.game_root.joinpath(*path_sequence)
            shutil.copy2(str(project_file), str(game_file))
        self.last_push_time = self._get_timestamp()

    @staticmethod
    def _get_timestamp(for_path=False):
        return datetime.datetime.now().strftime('%Y-%m-%d %H%M%S' if for_path else '%Y-%m-%d %H:%M:%S')

    def _build_config_dict(self):
        # TODO: Separate import times for different types.
        return {
            'GameName': self.game_name,
            'GameDirectory': str(self.game_root),
            'LastImportTime': self.last_import_time,
            'LastPushTime': self.last_push_time,
        }

    def _write_config(self):
        try:
            with (self.project_root / 'config.json').open('w') as f:
                json.dump(self._build_config_dict(), f, indent=4)
        except PermissionError:
            raise SoulstructProjectError("No write access to 'config.json' in project directory.")

    def _validate_project_directory(self, project_path, default_root):
        if not project_path:
            self.dialog(
                title="Choose Soulstruct project directory",
                message="Navigate to your Soulstruct project directory.\n\n" + word_wrap(
                    "If you want to create a new project, create an empty directory and select it."
                    "The name of the directory will be the name of the project.", 50),
                button_names='OK', button_kwargs='OK')
            project_path = self._window.FileDialog.askdirectory(
                title="Choose Soulstruct project directory", initialdir=str(Path('~/Documents').expanduser()))
            if not project_path:
                raise SoulstructProjectError(word_wrap("No directory chosen. Quitting Soulstruct.", 50))

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

    def _get_game_root(self):
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

        message = ("Navigate to the game executable for this project.\n"
                   "This can normally be found in:\n\n"
                   ""
                   "Prepare to Die Edition:\n"
                   "C:/Program Files/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA/DARKSOULS.exe\n\n"
                   ""
                   "Remastered:\n"
                   "C:/Program Files/Steam/steamapps/common/DARK SOULS REMASTERED/DarkSoulsRemastered.exe\n\n"
                   ""
                   "Otherwise, you can use Steam to find your Steam directory.")
        self.dialog(title="Select game for project", message=message, font_size=12,
                    button_names='OK', button_kwargs='OK')
        game_exe = self._window.FileDialog.askopenfilename(
            title="Choose your game executable", initialdir=initial_dir, filetypes=[('Game executable', '.exe')])
        if not game_exe:
            raise SoulstructProjectError("No game executable selected.")
        game_root = Path(game_exe).parent
        if (game_root / 'DarkSoulsRemastered.exe').is_file():
            return game_root, 'Dark Souls Remastered'
        elif (game_root / 'DARKSOULS.exe').is_file():
            return game_root, 'Dark Souls Prepare to Die Edition'
        else:
            raise SoulstructProjectError("Soulstruct projects are only supported for Dark Souls 1 (either version),\n"
                                         "but your selected executable was not a version of Dark Souls.")

    def dialog(self, title, message, font_size=None, font_type=None,
               button_names=('OK',), button_kwargs=(), style_defaults=None,
               default_output=None, cancel_output=None, word_wrap_limit=None):
        if word_wrap_limit:
            message = word_wrap(message, word_wrap_limit)
        return self._window.dialog(title=title, message=message, font_size=font_size, font_type=font_type,
                                   button_names=button_names, button_kwargs=button_kwargs,
                                   style_defaults=style_defaults,
                                   default_output=default_output, cancel_output=cancel_output)


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
