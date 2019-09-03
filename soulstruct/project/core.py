from __future__ import annotations
import datetime
from functools import wraps
import json
import os
import pickle
import re
import shutil
from tkinter.ttk import Notebook
from typing import Optional

from soulstruct.core import SoulstructError
from soulstruct.maps import DarkSoulsMaps, MAP_ENTRY_TYPES, MSB
from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.project.maps import SoulstructMapEditor
from soulstruct.project.params import SoulstructParamsEditor
from soulstruct.project.text import SoulstructTextEditor
from soulstruct.text import DarkSoulsText
from soulstruct.utilities import find_steam_common_paths, traverse_path_tree, word_wrap
from soulstruct.utilities.window import SoulstructSmartFrame

__all__ = ['SoulstructProject', 'SoulstructProjectError']


class SoulstructProjectError(SoulstructError):
    pass


def _with_config_write(func):
    @wraps(func)
    def project_method(self: SoulstructProject, *args, **kwargs):
        func(self, *args, **kwargs)
        self._write_config()

    return project_method


class MissingLinkError(KeyError):
    """Exception raised when a param ID linked to another table can't be found in that table."""
    pass


class WindowLinker(object):
    """Interface that generates links (go-to commands) between arbitrary parts of the Soulstruct unified window."""
    _MATCH_LINK = re.compile(r'<(.*)>')

    # TODO: Finalize these when tab order is set.
    PARAMS_TAB = 0
    TEXT_TAB = 1
    MAIN_TAB = 2
    MAPS_TAB = 3

    class Link(object):
        def __init__(self, linker: WindowLinker = None, name=None, menu_text='Go to link'):
            """Create a link within the Soulstruct GUI.

            Args:
                name: Name that will appear in [] next to ID. If None, no name will appear.
                menu_text: Text that will appear in right-click menu. Usually "Go to [type]".
            """
            self.linker = linker
            self.name = name
            self.menu_text = menu_text

        def __call__(self):
            raise NotImplementedError

    class NullLink(Link):
        """Link field has a null value, usually 0 or -1, which means the field is unused or set to a default."""
        def __init__(self, linker: WindowLinker):
            super().__init__(linker, name='None', menu_text='')

        def __call__(self):
            raise MissingLinkError("Null link cannot be called.")

    class ParamLink(Link):
        def __init__(self, linker, category, param_entry_id, create_if_missing=False, name=None):
            super().__init__(linker, name=name, menu_text=f"Jump to param entry {category}[{param_entry_id}]")
            self.category = category
            self.param_entry_id = param_entry_id

        def __call__(self):
            # TODO: Jump to specific field, for undo/redo.
            # TODO: Create if missing.
            self.linker.window.page_tabs.select(self.linker.PARAMS_TAB)
            index = sorted(self.linker.project.Params[self.category].entries).index(self.param_entry_id)
            self.linker.window.params_tab.select_category(self.category, first_display_index=index)
            self.linker.window.params_tab.entry_display.select_entry(0, edit_if_already_selected=False)
            self.linker.window.params_tab.update_idletasks()

    class TextLink(Link):
        def __init__(self, linker, category, text_id, create_if_missing=False, name=None):
            super().__init__(linker, name=name, menu_text=f"Jump to text entry {category}[{text_id}]")
            self.category = category
            self.text_id = text_id

        def __call__(self):
            # TODO: Create if missing.
            self.linker.window.page_tabs.select(self.linker.TEXT_TAB)
            self.linker.window.text_tab.select_category(
                self.category, first_display_index=sorted(self.linker.project.Text[self.category]).index(self.text_id))
            self.linker.window.text_tab.select_entry(self.text_id, edit_if_already_selected=False)
            self.linker.window.text_tab.update_idletasks()
            self.linker.window.text_tab.entry_canvas.yview_moveto(0)

    class MapLink(Link):
        def __init__(self, linker, entry_list_name, entry_type_index, entry_local_index,
                     entry_type_name=None, name=None):
            super().__init__(
                linker, name=name,
                menu_text=f"Jump to map entry {entry_list_name}"
                          f"{'.' + entry_type_name if entry_type_name is not None else ''}[{entry_local_index}]")
            self.entry_list_name = entry_list_name
            self.entry_type_index = entry_type_index
            self.entry_local_index = entry_local_index

        def __call__(self):
            self.linker.window.page_tabs.select(self.linker.MAPS_TAB)
            self.linker.window.maps_tab.entry_list_choice.set(self.entry_list_name)
            self.linker.window.maps_tab.refresh_entry_types(clear_selection=True)
            self.linker.window.maps_tab.select_entry_type(
                entry_type_index=self.entry_type_index, first_display_index=self.entry_local_index)
            self.linker.window.maps_tab.entry_display.select_entry(0, edit_if_already_selected=False)
            self.linker.window.maps_tab.update_idletasks()

    def __init__(self, window: SoulstructProjectWindow):
        self.window = window
        self.project = window.project

    def soulstruct_link(self, field_type, field_value):
        """Some field values are IDs to look up from other parameters or other types of game files (texture IDs,
        animation IDs, AI script IDs, etc.). These are coded as tags in the field information dictionary, and
        resolved here."""

        match_link = self._MATCH_LINK.match(field_type)
        if not match_link:
            raise ValueError("Invalid link.")

        name_extension = ''
        link_text = match_link.group(1)

        if ':' not in link_text:
            return []  # TODO: haven't supported these bare links yet (e.g. Flag, Animation, ...)

        link_pieces = link_text.split(':')
        table_type = link_pieces[0]

        if table_type == 'Maps':
            entry_name = field_value
            active_map = self.window.maps_tab.active_map_data  # type: MSB
            entry_list_name = link_pieces[1]
            if entry_list_name not in MAP_ENTRY_TYPES:
                raise ValueError(f"Invalid map entry list: {entry_list_name}")
            entry_list = active_map[entry_list_name]

            try:
                entry_local_index = entry_list.get_entry_type_index(entry_name)

                if len(link_pieces) == 3:
                    # Technically, map links only care about entry list type, but I'm sometimes adding some additional
                    # enforcement (like parts.characters[i].model_index linking to models.characters only).
                    entry_type_name = link_pieces[2]
                    if entry_type_name not in MAP_ENTRY_TYPES[entry_list_name]:
                        raise ValueError(f"Invalid map entry type for entry list {entry_list_name}: {entry_type_name}")
                    if entry_list[entry_name].ENTRY_TYPE != entry_list.resolve_entry_type(entry_type_name):
                        raise ValueError("Type of entry name in field does not match enforced type of field.")
                    entry_type_index = MAP_ENTRY_TYPES[entry_list_name][entry_type_name].value
                else:
                    entry_type_name = None
                    entry_type_index = entry_list[entry_name].ENTRY_TYPE.value

            except ValueError:
                # Entry name is missing (or is not of the enforced entry type).
                return [self.Link()]

            return [self.MapLink(
                self, name=field_value, entry_list_name=entry_list_name, entry_type_index=entry_type_index,
                entry_type_name=entry_type_name, entry_local_index=entry_local_index)]

        if field_value in {-1, 0}:
            # TODO: ensure that 0 means 'None' for all param/text fields.
            return [self.Link(self, name='None', menu_text='')]

        category = link_pieces[1]

        if table_type == 'Text':
            text_table = self.project.Text[category]
            if field_value not in text_table:
                return [self.Link()]
            return [self.TextLink(self, category=category, text_id=field_value, name=text_table[field_value])]

        if table_type == 'Params':
            if category in {'Attacks', 'Behaviors'}:
                # Try to determine Player vs. Non Player table.
                if category == 'Attacks':
                    if self.window.params_tab.active_category == 'PlayerBehaviors':
                        category = 'PlayerAttacks'
                    elif self.window.params_tab.active_category == 'NonPlayerBehaviors':
                        category = 'NonPlayerAttacks'
                elif category == 'Behaviors':
                    if self.window.params_tab.active_category == 'Players':
                        category = 'PlayerBehaviors'
                if category in {'Attacks', 'Behaviors'}:
                    # Could be Player or Non Player. Provide both links.
                    player_table = self.project.Params['Player' + category]
                    non_player_table = self.project.Params['NonPlayer' + category]
                    if field_value not in player_table and field_value not in non_player_table:
                        return [self.Link()]
                    links = []
                    if field_value in player_table:
                        links.append(self.ParamLink(
                            self, category='Player' + category, param_entry_id=field_value,
                            name=player_table[field_value]))
                    if field_value in player_table:
                        links.append(self.ParamLink(
                            self, category='NonPlayer' + category, param_entry_id=field_value,
                            name=player_table[field_value]))
                    if links:
                        return links
                    return [self.Link()]

            if category in {'Armor', 'Weapons'}:
                true_param_id = (self.check_armor_id(field_value) if category == 'Armor'
                                 else self.check_weapon_id(field_value))
                if true_param_id is None:
                    return [self.Link()]  # Invalid weapon/armor ID, even considering reinforcement.
                if field_value != true_param_id:
                    name_extension = '+' + str(field_value - true_param_id)
                field_value = true_param_id

            param_table = self.project.Params[category]
            try:
                name = param_table[field_value].name + name_extension
            except KeyError:
                return [self.Link()]
            else:
                return [self.ParamLink(self, category=category, param_entry_id=field_value, name=name)]

        return []  # No other table types supported yet.

    def entry_text_link(self, entry_id):
        """Return three (name, link) pairs for entries in item categories. Returns None if no link is appropriate, and
        returns an empty tuple if text should exist but cannot be found."""
        category = self.window.params_tab.active_category
        if category not in {'Weapons', 'Armor', 'Rings', 'Goods', 'Spells'}:
            return []
        text_ids = {'Names': entry_id, 'Summaries': entry_id, 'Descriptions': entry_id}
        links = []

        prefix = category.rstrip('s')

        if category == 'Weapons':
            base_weapon_id = self.check_weapon_id(entry_id)
            if base_weapon_id is not None:
                text_ids['Summaries'] = base_weapon_id
                text_ids['Descriptions'] = base_weapon_id
        elif category == 'Armor':
            base_armor_id = self.check_armor_id(entry_id)
            if base_armor_id is not None:
                text_ids['Summaries'] = base_armor_id
                text_ids['Descriptions'] = base_armor_id
        for text_category, text_id in text_ids.items():
            if text_ids[text_category] not in self.project.Text[prefix + text_category]:
                links.append(self.Link())
            else:
                links.append(self.TextLink(
                    self, category=prefix + text_category, text_id=text_id,
                    name=self.project.Text[prefix + text_category][text_id]))

        return links

    def check_armor_id(self, armor_id):
        """Checks if the given armor ID (which may include a reinforcement offset) is valid by inspecting the
        Weapons table."""
        level = armor_id % 100
        if level > 10:
            return None
        if level == 0:
            return armor_id
        base_armor = armor_id - level
        origin_field = 'originEquipPro' + ('' if level == 0 else str(level))
        try:
            origin = self.project.Params['Armor'][base_armor][origin_field]
        except KeyError:
            return None
        if origin == -1:
            return None
        return base_armor

    def check_weapon_id(self, weapon_id):
        """Checks if the given weapon ID (which may include a reinforcement offset) is valid by inspecting the
        Weapons table."""
        level = weapon_id % 100
        if level > 15:
            return None
        if level == 0:
            return weapon_id
        base_weapon = weapon_id - level
        origin_field = 'originEquipWep' + ('' if level == 0 else str(level))
        try:
            origin = self.project.Params['Weapons'][base_weapon][origin_field]
        except KeyError:
            return None
        if origin == -1:
            return None
        return base_weapon


class SoulstructProjectWindow(SoulstructSmartFrame):

    page_tabs: Optional[Notebook]
    params_tab: Optional[SoulstructParamsEditor]
    text_tab: Optional[SoulstructTextEditor]
    maps_tab: Optional[SoulstructMapEditor]

    def __init__(self, project: SoulstructProject, master=None):
        super().__init__(master=master, toplevel=True, window_title="Soulstruct")
        self.project = project
        self.linker = WindowLinker(self)

        self.page_tabs = None
        self.text_tab = None
        self.params_tab = None
        self.lighting_tab = None
        self.maps_tab = None
        self.set_geometry()
        # self.withdraw()

    def build(self):
        self.page_tabs = self.Notebook(row=0)

        f_params_tab = self.Frame(frame=self.page_tabs)
        self.page_tabs.add(f_params_tab, text='  Params  ')
        self.params_tab = self.SmartFrame(
            frame=f_params_tab, smart_frame_class=SoulstructParamsEditor, project=self.project, linker=self.linker)

        f_text_tab = self.Frame(frame=self.page_tabs)
        self.page_tabs.add(f_text_tab, text='  Text  ')
        self.text_tab = self.SmartFrame(
            frame=f_text_tab, smart_frame_class=SoulstructTextEditor, project=self.project, linker=self.linker)

        # TODO: Should obviously go first.
        f_main_tab = self.Frame(frame=self.page_tabs)
        self.page_tabs.add(f_main_tab, text='  Main  ')
        self.build_main_tab(f_main_tab)

        f_maps_tab = self.Frame(frame=self.page_tabs)
        self.page_tabs.add(f_maps_tab, text='  Maps  ')
        self.maps_tab = self.SmartFrame(
            frame=f_maps_tab, smart_frame_class=SoulstructMapEditor, project=self.project, linker=self.linker)

        # TODO: Lighting. Events (somehow). Game saves. MSB.

        self.resizable(False, False)
        self.set_geometry()
        self.deiconify()

    def build_main_tab(self, main_frame):
        with self.set_master(main_frame, auto_rows=0, grid_defaults={'padx': 100, 'pady': 20}):
            self.Button(text="Pull All from Game Directory", bg='#722', width=30, font_size=20,
                        command=lambda: self.project.load_project(force_game_pull=True))
            self.Button(text="Pull Params", bg='#722', width=30, font_size=20,
                        command=self.project.pull_params)
            self.Button(text="Pull Text", bg='#722', width=30, font_size=20,
                        command=self.project.pull_text)
            self.Button(text="Pull Lighting", bg='#722', width=30, font_size=20,
                        command=self.project.pull_lighting)
            self.Button(text="Pull Maps", bg='#722', width=30, font_size=20,
                        command=self.project.pull_maps)


class SoulstructProject(object):
    """Manages a directory of files that can be modded and 'pushed' into the appropriate game directory at will.

    It is recommended that you create one of these projects for each Soulstruct-based mod.

    Currently supports only Dark Souls 1.

    TODO:
        - Only pull exact file types that have no project pickles, and prompt for each one.
        - Eventually have subclasses for different games, with shared methods here.
        - Auto-save scheduled Tk functions that operate at ten minute intervals.
        - Inspect PTD directory for lack of UDSFM when pulled.
        - Store location of game save data for a future save manager.
    """
    _DEFAULT_PROJECT_ROOT = '~/Documents/Soulstruct/'

    def __init__(self, project_directory: str = ''):

        self._window = SoulstructProjectWindow(project=self, master=None)
        # self._window.withdraw()

        self.game_name = ''
        self.game_dir = ''
        self.last_pull_time = ''
        self.last_push_time = ''
        # TODO: Record last edit time for each file/structure.

        self.Text = DarkSoulsText(None)
        self.Params = DarkSoulsGameParameters(None)
        self.Lighting = DarkSoulsLightingParameters(None)
        self.Maps = DarkSoulsMaps(None)

        try:
            self.project_dir = self._validate_project_directory(project_directory, self._DEFAULT_PROJECT_ROOT)
            self.load_config()
            self.load_project()
        except SoulstructProjectError as e:
            self.dialog(title="Project Error", message=str(e) + "\n\nAborting startup.", button_kwargs='OK')
            raise  # TODO: should not raise an error; just flag startup failure.
        except Exception as e:
            msg = "Internal Python Error:\n\n" + str(e) + "\n\nAborting startup."
            self.dialog(title="Unknown Error", message=msg, button_kwargs='OK')
            raise  # TODO: should not raise an error; just flag startup failure.

        self._window.build()
        self._window.wait_window()

    def load_project(self, force_game_pull=False):
        """Load project structures (params, text, etc.) into class as attributes."""
        for attr, attr_class, pickled, pull_func in zip(
                ('Text', 'Params', 'Lighting', 'Maps'),
                (DarkSoulsText, DarkSoulsGameParameters, DarkSoulsLightingParameters, DarkSoulsMaps),
                ('text.d1s', 'params.d1s', 'lighting.d1s', 'maps.d1s'),
                (self.pull_text, self.pull_params, self.pull_lighting, self.pull_maps)):
            try:
                if force_game_pull:
                    raise FileNotFoundError
                with open(self.project_path(pickled), 'rb') as f:
                    setattr(self, attr, pickle.load(f))
            except FileNotFoundError:
                if force_game_pull or self.dialog(
                        title="Project Error",
                        message=f"Could not find saved {attr} data in project ('{pickled}').\n"
                                f"Would you like to pull it from the game directory?",
                        button_names=('Yes, pull the files', 'No, quit now'), button_kwargs=('YES', 'NO'),
                        cancel_output=1, default_output=1) == 0:
                    pull_func()
                else:
                    raise SoulstructProjectError("Could not open project files.")

    def save_in_project(self, obj, pickled_path):
        with open(self.project_path(pickled_path), 'wb') as f:
            pickle.dump(obj, f)

    def pull_text(self):
        self.Text = DarkSoulsText(self.game_path('msg/ENGLISH'))
        self.save_in_project(self.Text, 'text.d1s')

    def pull_params(self):
        self.Params = DarkSoulsGameParameters(self.game_path('param/GameParam/GameParam.parambnd'))
        self.save_in_project(self.Params, 'params.d1s')

    def pull_lighting(self):
        self.Lighting = DarkSoulsLightingParameters(self.game_path('param/DrawParam'))
        self.save_in_project(self.Lighting, 'lighting.d1s')

    def pull_maps(self):
        self.Maps = DarkSoulsMaps(self.game_path('map/MapStudio'))
        self.save_in_project(self.Maps, 'maps.d1s')

    def export_project(self, export_directory: str = None):
        if export_directory is None:
            export_directory = self.project_path(f'export/{self._get_timestamp(for_path=True)}')

        text_path = os.path.join(export_directory, 'msg/ENGLISH/')
        os.makedirs(text_path, exist_ok=True)
        self.Text.write(text_path)

        params_path = os.path.join(export_directory, 'param/GameParam/GameParam.parambnd')
        os.makedirs(params_path, exist_ok=True)
        self.Params.save(params_path)

        maps_path = os.path.join(export_directory, 'map/MapStudio/')
        os.makedirs(maps_path, exist_ok=True)
        self.Maps.save(maps_path)

        # TODO: can't save DrawParams yet.
        # lighting_path = os.path.join(export_directory, 'param/DrawParam/')
        # os.makedirs(lighting_path, exist_ok=True)
        # self.Lighting.write(lighting_path)

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
            if self.dialog(title="Initial project load",
                           message="Pull game files now? This will override any '.d1s' files\n"
                                   "that are already in this folder.",
                           button_names=("Yes, pull the files", "No, I'll do it later"),
                           button_kwargs=('YES', 'NO'),
                           cancel_output=1, default_output=1) == 0:
                self.load_project()

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
        # TODO: Separate pull times for different types.
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
                button_names='OK', button_kwargs='OK')
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
        self.dialog(title="Select game for project", message=message, font_size=14,
                    button_names='OK', button_kwargs='OK')
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

    def dialog(self, title, message, font_size=None, font_type=None,
               button_names=('OK',), button_kwargs=(), style_defaults=None,
               default_output=None, cancel_output=None):
        message = word_wrap(message, 50)
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
