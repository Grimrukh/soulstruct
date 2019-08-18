from __future__ import annotations
import datetime
from functools import wraps
import json
import os
import pickle
import shutil
from tkinter import Frame
from tkinter.constants import *

from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.text import DarkSoulsText
from soulstruct.utilities import find_steam_common_paths, traverse_path_tree, word_wrap, camel_case_to_spaces
from soulstruct.utilities.window import BaseWindow

__all__ = ['SoulstructProject', 'SoulstructError', 'SoulstructProjectError']


# TODO: SoulstructProject needs to wrap BaseWindow, not subclass it, to keep the namespace clear for interactive mode.
# TODO: Inspect PTD directory for lack of unpacking.


class SoulstructError(Exception):
    def __init__(self, msg=None):
        super().__init__(word_wrap(msg, 60) if msg else msg)


class SoulstructProjectError(SoulstructError):
    pass


def _with_config_write(func):
    @wraps(func)
    def project_method(self: SoulstructProject, *args, **kwargs):
        func(self, *args, **kwargs)
        self._write_config()

    return project_method


# TODO: Separate Frame subclasses for each tab, so they can be launched independently.
class _TextEditor(Frame):

    def __init__(self, *args, soulstruct_project, **kwargs):
        super().__init__(*args, **kwargs)
        self._project = soulstruct_project  # Will need whole project for resolving references.


class _SoulstructProjectWindow(BaseWindow):

    def __init__(self, soulstruct_project: SoulstructProject, master=None):
        """TODO: Build window.

        I'm thinking: main tabs up top (Text, Params, Lighting) in large text.

        In Text:
            Select category (FMG) in left pane.
            Right pane is a two-column scrollable window of IDs and text. Loads when a category is selected.

            You can freely edit both IDs and names, but when confirming the edit, it will complain if the ID matches an
            existing ID and refuse to make the change.

            Empty entries are highlighted in red. These will be removed when you next save (a warning will pop up when
                you save, which you can set to never appear again).
            Buttons to delete entries and insert a new empty one below the current selection (auto-numbered).

            LATER: Undo/redo button. It takes about 30 ms to make an entire copy of the Text dictionary, so it's easy
                to save stacks of states.

            LATER: You can find all usages of a given text entry. They pop up in a separate window with hyperlinks to
                each occurrence.

        In Params:


        """
        self.project = soulstruct_project
        super().__init__("Soulstruct", master=master)

        self.file_types = None

        self.f_text_categories = None
        self.category_boxes = {}

    def build(self):

        self.file_types = self.Notebook()

        text_tab = self.Frame(frame=self.file_types)
        self.file_types.add(text_tab, text='Text')
        self.build_text_tab(text_tab)

        # TODO
        self.set_geometry()

    def build_text_tab(self, text_tab):
        with self.set_master(text_tab, auto_columns=0):
            category_canvas = self.Canvas(scrollbar=True, width=250, height=500, padx=40, pady=40, highlightthickness=0)
            with self.set_master(category_canvas):
                self.f_text_categories = self.Frame(width=250, height=500, sticky=EW)
                category_canvas.create_window(125, 250, window=self.f_text_categories, anchor=CENTER)
                self.f_text_categories.bind(
                    "<Configure>", lambda event, c=category_canvas: self.reset_canvas_scroll_region(event, c))

                with self.set_master(self.f_text_categories):
                    row = 0
                    for category in self.project.Text.fmg_names:
                        box = self.Frame(row=row, width=250, height=30)
                        label_text = camel_case_to_spaces(category).replace(' _', ':')
                        label = self.Label(text=label_text, sticky=EW, row=row)
                        label.bind("<Button-1>", lambda e, c=category: self.select_text_category(c))
                        box.bind("<Button-1>", lambda e, c=category: self.select_text_category(c))
                        self.category_boxes[category] = (box, label)
                        row += 1

        self.selected_text_category = 'PlaceNames'

    def populate_text(self):


            category_canvas = self.Canvas(scrollbar=True, width=250, height=500, padx=40, pady=40, highlightthickness=0)
            with self.set_master(category_canvas):
                self.f_text_categories = self.Frame(width=250, height=500, sticky=EW)
                category_canvas.create_window(125, 250, window=self.f_text_categories, anchor=CENTER)
                self.f_text_categories.bind(
                    "<Configure>", lambda event, c=category_canvas: self.reset_canvas_scroll_region(event, c))

                with self.set_master(self.f_text_categories):
                    row = 0
                    for category in self.project.Text.fmg_names:
                        box = self.Frame(row=row, width=250, height=30)
                        label_text = camel_case_to_spaces(category).replace(' _', ':')
                        label = self.Label(text=label_text, sticky=EW, row=row)
                        label.bind("<Button-1>", lambda e, c=category: self.select_text_category(c))
                        box.bind("<Button-1>", lambda e, c=category: self.select_text_category(c))
                        self.category_boxes[category] = (box, label)
                        row += 1

    def select_text_category(self, selected: str):
        for category, (box, label) in self.category_boxes.items():
            if selected == category:
                box['bg'] = '#555555'
                label['bg'] = '#555555'
                # TODO: Load window if this category isn't already selected.
            else:
                box['bg'] = self.STYLE_DEFAULTS['bg']
                label['bg'] = self.STYLE_DEFAULTS['bg']


class SoulstructProject(object):
    """Manages a directory of files that can be modded and 'pushed' into the appropriate game directory at will.

    It is recommended that you create one of these projects for each Soulstruct-based mod.

    Currently supports only Dark Souls 1.
    TODO:
        - Eventually have subclasses for different games, with shared methods here.
        - Auto-save decorators that operate at ten minute intervals on write methods.
    """
    _DEFAULT_PROJECT_ROOT = '~/Documents/Soulstruct/'
    _OK_BUTTON_KWARGS = {'fg': '#FFFFFF', 'bg': '#442222', 'width': 20}
    _YES_BUTTON_KWARGS = {'fg': '#FFFFFF', 'bg': '#772222'}
    _NO_BUTTON_KWARGS = {'fg': '#FFFFFF', 'bg': '#444444'}

    def __init__(self, project_directory: str = ''):

        self._window = _SoulstructProjectWindow(soulstruct_project=self, master=None)
        # self._window.withdraw()

        self.game_name = ''
        self.game_dir = ''
        self.last_pull_time = ''
        self.last_push_time = ''
        # TODO: Record last edit time for each file/structure.

        self.Text = None    # type: DarkSoulsText
        self.Params = None  # type: DarkSoulsGameParameters
        self.Lighting = None  # type: DarkSoulsLightingParameters

        try:
            self.project_dir = self._validate_project_directory(project_directory, self._DEFAULT_PROJECT_ROOT)
            self.load_config()
            try:
                self.unpickle_all()
            except FileNotFoundError:
                # TODO: Should try to unpickle all, then prompt you to pull missing files.
                self.load_project()
        except SoulstructProjectError as e:
            self.dialog(title="Project Error", message=str(e), button_kwargs=self._OK_BUTTON_KWARGS)
            raise
        except Exception as e:
            msg = "Internal Python Error:\n\n" + str(e)
            self.dialog(title="Unknown Error", message=msg, button_kwargs=self._OK_BUTTON_KWARGS)
            raise

        self._window.build()
        self._window.wait_window()

    def load_project(self):
        """Load project structures (params, text, etc.) into dictionary as attributes.

        TODO: Will eventually look for entire pickled project file first.
        """
        self.Text = DarkSoulsText(self.project_path('msg/ENGLISH'))
        self.Params = DarkSoulsGameParameters(self.project_path('param/GameParam/GameParam.parambnd'))
        self.Lighting = DarkSoulsLightingParameters(self.project_path('param/DrawParam'))

    def export_project(self, export_directory: str = None):
        if export_directory is None:
            export_directory = self.project_path(f'export/{self._get_timestamp(for_path=True)}')

        text_path = os.path.join(export_directory, 'msg/ENGLISH/')
        os.makedirs(text_path, exist_ok=True)
        self.Text.write(text_path)

        params_path = os.path.join(export_directory, 'param/GameParam/GameParam.parambnd')
        os.makedirs(params_path, exist_ok=True)
        self.Params.save(params_path)

        # TODO
        # lighting_path = os.path.join(export_directory, 'param/DrawParam/')
        # os.makedirs(lighting_path, exist_ok=True)
        # self.Lighting.write(lighting_path)

    def pickle_all(self):
        with open(self.project_path('Text.dstext'), 'wb') as f:
            pickle.dump(self.Text, f)
        with open(self.project_path('Params.dstext'), 'wb') as f:
            pickle.dump(self.Params, f)
        with open(self.project_path('Lighting.dstext'), 'wb') as f:
            pickle.dump(self.Lighting, f)

    def unpickle_all(self):
        try:
            with open(self.project_path('Text.dstext'), 'rb') as f:
                self.Text = pickle.load(f)
            with open(self.project_path('Params.dstext'), 'rb') as f:
                self.Params = pickle.load(f)
            with open(self.project_path('Lighting.dstext'), 'rb') as f:
                self.Lighting = pickle.load(f)
        except FileNotFoundError:
            self.dialog(title="Project Error", message="(TODO) Could not unpickle files. Will try to pull.",
                        button_kwargs=self._OK_BUTTON_KWARGS)
            raise

    def load_config(self):
        try:
            with open(os.path.join(self.project_dir, 'config.json'), 'r') as f:
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
                        self.game_dir = config['GameDirectory']
                        self.last_pull_time = config.get('LastPullTime', None)
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
                self.game_dir, self.game_name = self._get_live_game_directory()
            except SoulstructProjectError as e:
                raise SoulstructProjectError(str(e) + "\n\nAborting project setup.")
            if self.dialog(title="Initial project pull",
                           message="Pull game files from game directory into project directory now?",
                           button_names=("Yes, pull the files", "No, I'll do it later"),
                           button_kwargs=(self._YES_BUTTON_KWARGS, self._NO_BUTTON_KWARGS),
                           cancel_output=1, default_output=1) == 0:
                self.pull()

    @_with_config_write
    def pull(self):
        print("# Pulling game files into project...")  # TODO: log
        for path_sequence in traverse_path_tree(MODIFIABLE_FILES[self.game_name]):
            game_file = os.path.join(self.game_dir, *path_sequence)
            project_file = os.path.join(self.project_dir, *path_sequence)
            try:
                os.makedirs(os.path.dirname(project_file), exist_ok=True)
                shutil.copy2(game_file, project_file)
            except FileNotFoundError:
                raise SoulstructProjectError(f"Could not find expected game file: {repr(game_file)}")
        self.last_pull_time = self._get_timestamp()

    @_with_config_write
    def push(self):
        print("# Pushing project files to game...")  # TODO: log
        for path_sequence in traverse_path_tree(MODIFIABLE_FILES[self.game_name]):
            project_file = os.path.join(self.project_dir, *path_sequence)
            game_file = os.path.join(self.game_dir, *path_sequence)
            shutil.copy2(project_file, game_file)
        self.last_push_time = self._get_timestamp()

    def game_path(self, *relative_parts):
        return os.path.abspath(os.path.join(self.game_dir, *relative_parts))

    def project_path(self, *relative_parts):
        return os.path.abspath(os.path.join(self.project_dir, *relative_parts))

    @staticmethod
    def _get_timestamp(for_path=False):
        if for_path:
            return datetime.datetime.now().strftime('%Y %B %d %H.%M.%S')
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _build_config_dict(self):
        return {
            'GameName': self.game_name,
            'GameDirectory': self.game_dir,
            'LastPullTime': self.last_pull_time,
            'LastPushTime': self.last_push_time,
        }

    def _write_config(self):
        try:
            with open(os.path.join(self.project_dir, 'config.json'), 'w') as f:
                json.dump(self._build_config_dict(), f, indent=4)
        except PermissionError:
            raise SoulstructProjectError("No write access to 'config.json' in project directory.")

    def _validate_project_directory(self, project_dir, default_root):
        if not project_dir:
            self.dialog(
                title="Choose Soulstruct project directory",
                message="Navigate to your Soulstruct project directory.\n\n" + word_wrap(
                    "If you want to create a new project, create an empty directory and select it."
                    "The name of the directory will be the name of the project.", 50),
                button_names='OK', button_kwargs={**self._YES_BUTTON_KWARGS, 'width': 15})
            project_dir = self._window.FileDialog.askdirectory(
                title="Choose Soulstruct project directory", initialdir=os.path.expanduser('~/Documents'))
            if not project_dir:
                raise SoulstructProjectError(word_wrap("No directory chosen. Quitting Soulstruct.", 50))
        if not os.path.isabs(project_dir):
            project_dir = os.path.abspath(os.path.join(default_root, project_dir))
        if os.path.isfile(project_dir):
            raise SoulstructProjectError("You must specify a project *directory*, not a file.")

        if not os.path.isdir(project_dir):
            try:
                os.makedirs(project_dir, exist_ok=True)
            except NotADirectoryError:
                raise SoulstructProjectError(f"Invalid directory path: {repr(project_dir)}.")
            except PermissionError:
                raise SoulstructProjectError(f"No write access to create directory: {repr(project_dir)}.")

        return project_dir

    def _get_live_game_directory(self):
        for common_path in find_steam_common_paths():
            dsr_path = os.path.join(common_path, 'DARK SOULS REMASTERED')
            if os.path.isdir(dsr_path):
                initial_dir = dsr_path
                break
            ptd_path = os.path.join(common_path, 'Dark Souls Prepare to Die Edition/DATA')
            if os.path.isdir(ptd_path):
                initial_dir = ptd_path
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
        self.dialog(title="Select game for project", message=message,
                    button_names='OK', button_kwargs={**self._YES_BUTTON_KWARGS, 'width': 15}, font_size=14)
        live_dir = self._window.FileDialog.askopenfilename(
            title="Choose your game executable", initialdir=initial_dir, filetypes=[('Game executable', '.exe')])
        if not live_dir:
            raise SoulstructProjectError("No game directory selected.")
        if os.path.isfile(os.path.join(live_dir, 'DarkSoulsRemastered.exe')):
            return live_dir, 'Dark Souls Remastered'
        elif os.path.isfile(os.path.join(live_dir, 'DARKSOULS.exe')):
            return live_dir, 'Dark Souls Prepare to Die Edition'
        else:
            raise SoulstructProjectError("Soulstruct projects are only supported for Dark Souls 1 (either version),\n"
                                         "but your selected executable was not a version of Dark Souls.")

    def dialog(self, title, message, *args, **kwargs):
        message = word_wrap(message, 50)
        return self._window.custom_dialog(title, message, *args, **kwargs)


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
