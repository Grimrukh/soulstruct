from __future__ import annotations

__all__ = ["GameDirectoryProject"]

import abc
import datetime
import json
import logging
import os
import pickle
import shutil
import subprocess
import sys
import threading
import typing as tp
from functools import wraps
from pathlib import Path

from soulstruct import __version__
from soulstruct.config import DEFAULT_TEXT_EDITOR_FONT_SIZE
from soulstruct.games import GameSpecificType
from soulstruct.exceptions import GameFileDictSupportError
from soulstruct.utilities.files import PACKAGE_PATH, read_json, write_json
from soulstruct.utilities.misc import traverse_path_tree
from soulstruct.utilities.window import CustomDialog

from .exceptions import SoulstructProjectError, RestoreBackupError

if tp.TYPE_CHECKING:
    from soulstruct.base.game_file import GameFile
    from soulstruct.games import Game
    from ..ai.ai_directory import AIDirectory
    from ..events.emevd_directory import EMEVDDirectory
    from ..ezstate.talk_directory import TalkDirectory
    from ..maps.map_studio_directory import MapStudioDirectory
    from ..params.game_param_bnd import GameParamBND
    from ..params.draw_param import DrawParamDirectory
    from ..text.msg_directory import MSGDirectory
    from .window import ProjectWindow

try:
    import psutil
except ImportError:
    psutil = None

_LOGGER = logging.getLogger(__name__)


def _with_config_write(func):
    @wraps(func)
    def project_method(self: GameDirectoryProject, *args, **kwargs):
        func(self, *args, **kwargs)
        self._write_config()

    return project_method


def _data_type_action(func):
    """Validate `data_type` argument and recur on all project types if it is `None`."""
    @wraps(func)
    def data_type_action(self: GameDirectoryProject, data_type, *args, **kwargs):
        if data_type is None:
            for data_type in self.DATA_TYPES:
                func(self, data_type, *args, **kwargs)  # recur on every type
            return
        data_type = data_type.lower()
        if data_type not in self.DATA_TYPES:
            data_type_list = list(self.DATA_TYPES)
            raise ValueError(f"`data_type` should be None (for all types) or one of {data_type_list}, not {data_type}.")
        func(self, data_type, *args, **kwargs)

    return data_type_action


class GameDirectoryProject(GameSpecificType, abc.ABC):
    """Manages an entire editable instance of a game installation (or rather, all the file types Soulstruct can handle).

    It is recommended that you create one of these projects for each Soulstruct-based mod.
    """

    # Default project root (for relative project paths) is in the current working directory for standard Python use
    # or next to the frozen PyInstaller executable, if applicable.
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        _DEFAULT_PROJECT_ROOT = Path(sys.executable).parent
    else:
        _DEFAULT_PROJECT_ROOT = Path(os.getcwd())

    DATA_TYPES = {}  # type: dict[str, type]

    def __init__(self, project_path="", with_window: ProjectWindow = None, game_root: str | Path = None):

        self.game_root = Path()
        self.last_import_time = ""
        self.last_export_time = ""
        self._vanilla_game_root = ""
        self.text_editor_font_size = DEFAULT_TEXT_EDITOR_FONT_SIZE
        self.custom_script_directory = Path()
        self.entities_in_events_directory = False
        self.include_vanila_entities = False
        self.prefer_json = False
        # TODO: Record last edit time for each file/structure.

        # Initialize with empty structures.
        self.ai_directory = self._get_default_data("ai")  # type: AIDirectory
        self.draw_param_directory = self._get_default_data("lighting")  # type: DrawParamDirectory
        self.emevd_directory = self._get_default_data("events")  # type: EMEVDDirectory
        self.game_param_bnd = self._get_default_data("params")  # type: GameParamBND
        self.map_studio_directory = self._get_default_data("maps")  # type: MapStudioDirectory
        self.msg_directory = self._get_default_data("text")  # type: MSGDirectory
        self.talk_directory = self._get_default_data("talk")  # type: TalkDirectory

        self.project_root = self._validate_project_directory(project_path, self._DEFAULT_PROJECT_ROOT)
        first_time, force_import_from_game = self.load_config(with_window=with_window, game_root=game_root)
        self.initialize_project(force_import_from_game, with_window=with_window, first_time=first_time)

    def _get_default_data(self, data_type: str):
        if data_type not in self.DATA_TYPES:
            return None
        else:
            return self.DATA_TYPES[data_type]()

    @property
    def ai(self) -> AIDirectory:
        return self.ai_directory

    @ai.setter
    def ai(self, value: AIDirectory):
        self.ai_directory = value

    @property
    def events(self) -> EMEVDDirectory:
        return self.emevd_directory

    @events.setter
    def events(self, value: EMEVDDirectory):
        self.emevd_directory = value

    @property
    def lighting(self) -> DrawParamDirectory:
        return self.draw_param_directory

    @lighting.setter
    def lighting(self, value: DrawParamDirectory):
        self.draw_param_directory = value

    @property
    def maps(self) -> MapStudioDirectory:
        return self.map_studio_directory

    @maps.setter
    def maps(self, value: MapStudioDirectory):
        self.map_studio_directory = value

    @property
    def params(self) -> GameParamBND:
        return self.game_param_bnd

    @params.setter
    def params(self, value: GameParamBND):
        self.game_param_bnd = value

    @property
    def talk(self):
        return self.talk_directory

    @talk.setter
    def talk(self, value: TalkDirectory):
        self.talk_directory = value

    @property
    def text(self) -> MSGDirectory:
        return self.msg_directory

    @text.setter
    def text(self, value: MSGDirectory):
        self.msg_directory = value

    def initialize_project(self, force_import_from_game=False, with_window: ProjectWindow = None, first_time=False):
        """Load project structures from pickled project files if available, or prompt for initial import to create."""

        yes_to_all = force_import_from_game
        for data_type in self.DATA_TYPES:
            yes_to_all = self.import_data_type(data_type, force_import_from_game, yes_to_all, with_window=with_window)

        if "events" in self.DATA_TYPES:
            self.import_events(force_import=yes_to_all, with_window=with_window)
            self.offer_events_submodule_copy(with_window=with_window)

        if "talk" in self.DATA_TYPES:
            self.import_talk(force_import=yes_to_all, with_window=with_window)

    def import_data_type(
        self, data_type: str, force_import_from_game=False, yes_to_all=False, with_window: ProjectWindow = None
    ):
        if data_type in ("events", "talk"):
            return yes_to_all  # events and talk are not saved and loaded as pickles, just imported and exported
        try:
            if force_import_from_game:
                raise FileNotFoundError  # don't bother looking for existing file
            self.load(data_type)
        except FileNotFoundError:
            if yes_to_all:
                self.import_data_from_game(data_type)
                self.save(data_type)
            else:
                if with_window:
                    result = with_window.CustomDialog(
                        title="Data Missing",
                        message=f"Could not find saved '{data_type}' data in project.\n"
                                f"Would you like to import it from the game directory now?",
                        button_names=("Yes", "Yes to All", "No, quit now"),
                        button_kwargs=("YES", "YES", "NO"),
                        cancel_output=2,
                        default_output=2,
                    )
                else:
                    result = 2 if (
                            input(
                                f"Could not find saved '{data_type}' data in project.\n"
                                f"Would you like to import it from the game directory now? [y]/n "
                            ).lower() == "n"
                    ) else 0
                if result in {0, 1}:
                    self.import_data_from_game(data_type)
                    self.save(data_type)
                    if result == 1:
                        yes_to_all = True
                else:
                    raise SoulstructProjectError("Could not open project files.")

        return yes_to_all

    def import_events(self, force_import=False, with_window: ProjectWindow = None):
        if not (self.project_root / "events").is_dir() or not (self.project_root / "events").glob("*"):
            if force_import:
                self.import_data_from_game("events")
            else:
                if with_window:
                    result = with_window.CustomDialog(
                        title="Project Error",
                        message=f"Could not find any event scripts in project.\n"
                                f"Would you like to decompile and import them from the game directory now?",
                        button_names=("Yes", "No, I'll handle events"),
                        button_kwargs=("YES", "NO"),
                        cancel_output=1,
                        default_output=1,
                    )
                else:
                    result = 1 if (
                            input(
                                f"Could not find any event scripts in project.\n"
                                f"Would you like to import them from the game directory now? [y]/n "
                            ).lower() == "n"
                    ) else 0
                if result == 0:
                    self.import_data_from_game("events")

    def import_talk(self, force_import=False, with_window: ProjectWindow = None):
        if not (self.project_root / "talk").is_dir() or not (self.project_root / "talk").glob("*"):
            if force_import:
                self.import_data_from_game("talk")
            else:
                if with_window:
                    result = with_window.CustomDialog(
                        title="Project Error",
                        message=f"Could not find any talk scripts in project.\n"
                                f"Would you like to decompile and import them from the game directory now?",
                        button_names=("Yes", "No, I'll handle talk"),
                        button_kwargs=("YES", "NO"),
                        cancel_output=1,
                        default_output=1,
                    )
                else:
                    result = 1 if (
                            input(
                                f"Could not find any talk scripts in project.\n"
                                f"Would you like to import them from the game directory now? [y]/n "
                            ).lower() == "n"
                    ) else 0
                if result == 0:
                    self.import_data_from_game("talk")

    @_with_config_write
    @_data_type_action
    def save(self, data_type: str = None):
        """Save given data type ('maps', 'text', etc.) as pickled project file.

        Events and Talk scripts have no additional data to save beyond the project's text script files.
        """
        if data_type not in {"events", "talk"}:
            self._save_project_data(getattr(self, data_type), data_type=data_type)

    @_data_type_action
    def load(self, data_type=None):
        """Load give data type ('maps', 'text', etc.) from pickled project file.

        Events and Talk scripts have no additional data to load beyond the project's text script files.
        """
        if data_type not in {"events", "talk"}:
            setattr(self, data_type, self._load_project_data(data_type))

    def _save_project_data(self, data: GameFile, data_type: str):
        """Pickle given project data structure `obj` to path `{data_path}.ssp`.

        If `self.prefer_json=True`, and `obj.write_json()` is supported, that will be used instead. The extension of
        `data_path` will be set to `{data_path}.json` in this case.
        """
        if self.prefer_json:
            if data_type in {"maps", "params", "lighting", "text"}:
                # Save separate JSONs to `{project}/{data_type}/` directory with `write_json_dir()`.
                data: tp.Union[MapStudioDirectory, GameParamBND, DrawParamDirectory, MSGDirectory]
                data_dir_path = self.project_root / data_type
                first_time = not data_dir_path.exists()
                data.write_json_dir(data_dir_path)
                if first_time:
                    _LOGGER.info(
                        f"Created new '{data_type}' project folder with separate JSON files inside. As long as "
                        f"`PreferJSON` is enabled for this project, that directory will be loaded instead of "
                        f"'{data_type}.ssp'."
                    )
                return
            else:
                # JSON not implemented for other data types.
                data_file_path = (self.project_root / data_type).with_suffix(".json")
                try:
                    first_time = not data_file_path.exists()
                    data.write_json(data_file_path)
                except (AttributeError, GameFileDictSupportError):
                    pass  # continue to pickle backup
                else:
                    if first_time:
                        _LOGGER.info(
                            f"Created new '{data_type}.json' project file. As long as `PreferJSON` is enabled for this "
                            f"project, that file will be loaded instead of '{data_type}.ssp'."
                        )
                    return
        data_file_path = (self.project_root / data_type).with_suffix(".ssp")
        with data_file_path.open("wb") as f:
            pickle.dump(data, f)

    def _load_project_data(self, data_type: str):
        if self.prefer_json:
            try:
                if (
                    data_type in {"maps", "params", "text", "lighting"}
                    and (data_dir_path := self.project_root / data_type).is_dir()
                ):
                    # Load JSONs from directory.
                    return self.DATA_TYPES[data_type](data_dir_path, use_json=True)
                elif (data_file_path := (self.project_root / data_type).with_suffix(".json")).exists():
                    # Try to load from `{game_type}.json` file.
                    data_class = self.DATA_TYPES[data_type]
                    try:
                        return data_class(data_file_path)
                    except GameFileDictSupportError:
                        raise SoulstructProjectError(
                            f"Found a '{data_type}.json' file in this project, but the Soulstruct class used to load "
                            f"this data type does not support loading from JSON files. Was this file generated with a "
                            f"newer version?"
                        )
            except FileNotFoundError:
                pass  # continue to load SSP files below

        data_file_path = (self.project_root / data_type).with_suffix(".ssp")
        with data_file_path.open("rb") as f:
            try:
                return pickle.load(f)
            except Exception as ex:
                raise SoulstructProjectError(
                    f"Could not open project file: '{data_file_path}'.\n\n"
                    f"If you are seeing this after downloading a new version of Soulstruct, there may have been a "
                    f"non-backwards-compatible change in the internal structure of the program. Please export your "
                    f"project files from the last working version, delete the problematic file(s) after backing them "
                    f"up somewhere else, then re-import them into this new version.\n\n"
                    f"Specific error:\n{ex}"
                )

    @_with_config_write
    @_data_type_action
    def import_data(self, data_type=None, import_directory=None):
        """Import data sub-structure from binary game files.

        If `data_type` is None (default), all data types will be imported, in which case the given `import_directory`
        should contain the appropriate folder structure ('map/MapStudio', etc.) for all files.
        """
        import_directory = Path(import_directory)
        data_import_path = self.get_game_path_of_data_type(data_type, root=import_directory)
        data_instance = self.DATA_TYPES[data_type](data_import_path)
        setattr(self, data_type, data_instance)
        if data_type == "events":  # data in `EMEVDDirectory` is only read upon import and modified upon export
            self.events.write_evs(
                self.project_root / "events",
                entities_directory=self.entities_directory,
                warn_missing_enums=True,  # TODO: project setting
                entity_module_prefix="..entities.",
            )
        if data_type == "talk":  # data in `TalkDirectory` is only read upon import and modified upon export
            self.talk.write_esp(self.project_root / "talk")

    def import_data_from_game(self, data_type=None):
        """Reads data substructures in game formats from the live game directory."""
        self.import_data(data_type=data_type, import_directory=self.game_root)

    @_data_type_action
    def export_data(self, data_type=None, export_directory=None):
        export_directory = Path(export_directory)
        data_export_path = self.get_game_path_of_data_type(data_type, root=export_directory)
        data_export_path.parent.mkdir(parents=True, exist_ok=True)
        # TODO: Differentiate between exporting single EMEVD or entire directory.
        #  - Annoying to export every script individually.
        #  - Also annoying to update the 'last modified time' metadata of every game EMEVD when only one is updated.
        data = getattr(self, data_type)
        if data_type in {"events", "talk"}:
            data.load(self.project_root / data_type)  # load text files into managed `Directory` structure for export
        data.write(data_export_path)

    def export_data_to_game(self, data_type=None):
        """Writes data substructures in game formats in the live game directory, ready for play."""
        self.export_data(data_type=data_type, export_directory=self.game_root)

    def export_timestamped_backup(self, data_type=None):
        timestamped = self.project_root / "export" / self._get_timestamp(for_path=True)
        self.export_data(data_type=data_type, export_directory=timestamped)

    def restore_backup(self, target=None, delete_baks=False):
        """Restores '.bak' files, deleting whatever they would replace."""
        target = Path(target)
        if target.is_file():
            if target.suffix == ".bak":
                if (target.with_suffix("")).is_file():
                    os.remove(str(target.with_suffix("")))
                if delete_baks:
                    os.rename(str(target), str(target.with_suffix("")))
                else:
                    shutil.copy2(str(target), str(target.with_suffix("")))
            elif not (target.with_suffix(".bak")).is_file():
                raise RestoreBackupError(
                    f"Could not find a file '{str(target.with_suffix('.bak'))} " f"to restore. No action taken."
                )
            else:
                os.remove(str(target))
                if delete_baks:
                    os.rename(str(target.with_suffix(".bak")), str(target))
                else:
                    shutil.copy2(str(target.with_suffix(".bak")), str(target))
        elif target.is_dir():
            count = 0
            for bak_file in target.glob("*.bak"):
                self.restore_backup(bak_file)
                count += 1
            if count == 0:
                raise RestoreBackupError(
                    f"Could not find any '.bak' files to restore in directory '{str(target)}'. " f"No action taken."
                )
            else:
                return count

    def launch_game(self, try_force_quit_first=False, threaded=True):
        if not psutil:
            raise ModuleNotFoundError(
                "Python package `psutil` required for this method. Install it with `python -m pip install psutil`."
            )

        if try_force_quit_first:
            self.force_quit_game()
        if not self._check_steam_appid_file(self.game_root):
            raise SoulstructProjectError(f"Soulstruct cannot create the 'steam_appid.txt' file for {self.GAME.name}")
        game_exe_path = self.game_root / self.GAME.executable_name

        if not game_exe_path.is_file():
            raise SoulstructProjectError(f"Could not find game executable: {str(game_exe_path)}")

        if game_exe_path.name in (p.name() for p in psutil.process_iter()):
            _LOGGER.warning(f"Cannot launch game: {game_exe_path.name} is already running.")
            return

        if threaded:
            game_thread = threading.Thread(target=subprocess.run, args=(str(game_exe_path),))
            game_thread.start()
        else:
            # Blocks Python (including window) until game is closed.
            subprocess.run(str(game_exe_path))

    def force_quit_game(self):
        if not self.GAME.executable_name:
            raise SoulstructProjectError(f"Cannot force-quit {self.GAME.name} (don't know executable name).")
        os.system(f"TASKKILL /F /IM {self.GAME.executable_name}")

    def launch_gadget(self, threaded=True):
        if not self.GAME.gadget_name:
            raise SoulstructProjectError(f"No Gadget executable known for {self.GAME.name}.")
        gadget_path = self.game_root / self.GAME.gadget_name
        if not gadget_path.is_file():
            raise SoulstructProjectError(f"Could not find Gadget executable: {str(gadget_path)}")
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
        if not self.GAME.save_file_path:
            raise SoulstructProjectError(f"No save file directory known for {self.GAME.name}.")
        if not self.GAME.save_file_path.is_dir():
            raise SoulstructProjectError(f"Could not find save file directory root: {self.GAME.save_file_path}")
        if self.GAME.name == "Dark Souls Remastered":
            # DSR save files are saved under a Steam ID subfolder.
            steam_id_folders = list(self.GAME.save_file_path.glob("*"))
            if len(steam_id_folders) > 1:
                raise SoulstructProjectError(
                    f"Multiple Dark Souls Remastered save folders found in {str(self.GAME.save_file_path)}. Please "
                    f"remove all of them except the real one that matches your Steam ID."
                )
            elif not steam_id_folders:
                raise SoulstructProjectError(
                    f"No Dark Souls Remastered save folders found in {str(self.GAME.save_file_path)}."
                )
            return steam_id_folders[0]
        return self.GAME.save_file_path

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

    def create_game_backup(self, backup_path=None):
        """Copy existing game files (that can be edited with Soulstruct) to a backup directory, which defaults to
        'soulstruct-backup' in your game directory. Use `restore_game_backup(backup_dir)` to restore those files."""
        if backup_path is None:
            backup_path = self.game_root / "soulstruct-backup"
        else:
            backup_path = Path(backup_path)
        game_files = read_json(PACKAGE_PATH("project/files.json"))[self.GAME.name]
        for file_path_parts in traverse_path_tree(game_files):
            game_file_path = self.game_root / Path(*file_path_parts)
            if not game_file_path.is_file():
                raise FileNotFoundError(f"Could not find file in game directory to back up: " f"{str(game_file_path)}")
            backup_file_path = Path(backup_path, *file_path_parts)
            backup_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(game_file_path), str(backup_file_path))

    def restore_game_backup(self, backup_path=None):
        """Restore game files from the given folder, which defaults to 'soulstruct-backup' in your game directory.
        Create these backup files with `create_game_backup(backup_dir)`."""
        if backup_path is None:
            backup_path = self.game_root / "soulstruct-backup"
        game_files = read_json(PACKAGE_PATH("project/files.json"))[self.GAME.name]
        for file_path_parts in traverse_path_tree(game_files):
            backup_file_path = backup_path / Path(*file_path_parts)
            if not backup_file_path.is_file():
                raise FileNotFoundError(f"Could not find backup file to restore: " f"{str(backup_file_path)}")
            game_file_path = Path(self.game_root, *file_path_parts)
            game_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(backup_file_path), str(game_file_path))

    def load_config(self, with_window: ProjectWindow = None, game_root: Path = None) -> tuple[bool, bool]:
        """Load config JSON from project, or create it if missing.

        Returns two bools: `first_time` (if project JSON was created) and `force_import_from_game` (if the user
        accepted the offer to import all game data immediately).
        """
        config_path = self.project_root / "project_config.json"

        if config_path.is_file():
            try:
                config = read_json(config_path)
            except json.JSONDecodeError:
                raise SoulstructProjectError(
                    "Could not interpret 'project_config.json' file. Check it for errors, or "
                    "delete it to have Soulstruct create a fresh copy on next load."
                )
            try:
                if self.GAME.name != config["GameName"]:
                    raise SoulstructProjectError(
                        f"Project config 'GameName' is {config['GameName']}, but `GameDirectoryProject` "
                        f"instance belongs to {self.GAME.name}."
                    )
                last_save_version = config.get("LastSaveVersion", "'unknown'")
                self.game_root = Path(config["GameDirectory"])
                if game_root and str(game_root) != str(self.game_root):
                    _LOGGER.warning(
                        f"You passed `game_root` {game_root}` to the project, but it already has root "
                        f"{self.game_root}. You should change this in the config JSON directly."
                    )
                self.last_import_time = config.get("LastImportTime", None)
                self.last_export_time = config["LastExportTime"]
                self.custom_script_directory = Path(config.get("CustomScriptDirectory", "scripts"))
                if not self.custom_script_directory.is_absolute():
                    self.custom_script_directory = self.project_root / self.custom_script_directory
                if vanilla_game_root := config.get("VanillaGameDirectory", ""):
                    self._vanilla_game_root = Path(vanilla_game_root)
                self.text_editor_font_size = config.get("TextEditorFontSize", DEFAULT_TEXT_EDITOR_FONT_SIZE)
                self.entities_in_events_directory = config.get("EntitiesInEventsDirectory", False)
                self.include_vanila_entities = config.get("IncludeVanillaEntities", False)
                self.prefer_json = config.get("PreferJSON", False)
            except KeyError:
                raise SoulstructProjectError(
                    "Project config file does not contain necessary settings. "
                    "Delete it and load the project directory again to create "
                    "a fresh copy and re-link your project to the game."
                )
            if last_save_version.split(".")[0] != __version__.split(".")[0]:
                # Major version difference indicates potential project file incompatibility.
                _LOGGER.warning(
                    f"Project was last saved with Soulstruct version {last_save_version}, which has a different major "
                    f"version number to this version of Soulstruct ({__version__}). You may need to export your "
                    f"project from the other version of Soulstruct and import those game files into this project."
                )
        else:
            # Create project config file.
            if game_root:
                self.game_root = Path(game_root)
            else:
                try:
                    self.game_root = self._get_game_root(with_window=with_window)
                except SoulstructProjectError as ex:
                    raise SoulstructProjectError(str(ex) + "\n\nAborting project setup.")
            self._write_config()
            # Offer import of all data types immediately.
            if with_window:
                result = with_window.CustomDialog(
                    title="Import Project Files",
                    message="Import all game files now? This will override any project\n"
                    "files that are already in this folder.",
                    button_names=("Yes, import the files", "No, I'll do it later"),
                    button_kwargs=("YES", "NO"),
                    cancel_output=None,
                    default_output=0,
                )
            else:
                result = input(
                    "Import game files now? This will override any project files\n"
                    "that are already in this folder. [y]/n "
                )
                if result.lower == "n":
                    result = 1
                else:
                    result = 0
            if result == 0:
                return True, True
            return True, False

        return False, False

    def get_game_path_of_data_type(self, data_type, root=None) -> Path:
        root = self.game_root if root is None else Path(root)
        data_class_name = self.DATA_TYPES[data_type.lower()].__name__
        try:
            return root / self.GAME.default_file_paths[data_class_name]
        except KeyError:
            raise KeyError(f"Could not get data path to {data_type} ({data_class_name}) for game {self.GAME.name}")

    def offer_events_submodule_copy(self, with_window: ProjectWindow = None):
        """Offer to copy `soulstruct.events.{game}` into project `events` folder for IDE purposes."""
        if (self.project_root / "events").is_dir() and (self.project_root / "events").glob("*"):
            return  # don't offer if `events` already imported/exist
        if with_window:
            result = with_window.CustomDialog(
                title="Events Module Copy",
                message="Would you like to copy the game events submodule for IDE autocomplete?",
                button_names=("Yes, copy it", "No, don't bother"),
                button_kwargs=("YES", "NO"),
                cancel_output=1,
                default_output=1,
            )
        else:
            result = 1 if (
                    input(
                        "Would you like to copy the game events submodule for IDE autocomplete? [y]/n",
                    ).lower() == "n"
            ) else 0
        if result == 0:
            self.copy_events_submodule()

    def copy_events_submodule(self):
        name = self.GAME.submodule_name
        events_submodule = PACKAGE_PATH(f"{name}/events")
        (self.project_root / f"events/soulstruct/{name}").mkdir(parents=True, exist_ok=True)
        shutil.copytree(events_submodule, self.project_root / f"events/soulstruct/{name}/events")
        _LOGGER.info(f"Copied `soulstruct.{name}.events` submodule into project events folder.")

    def run_script(self, script_path: Path, stdout=None, stderr=None) -> subprocess.CompletedProcess:
        """Run given `script_path` Python script in a subprocess and wait for it to return.

        If the given path is relative, it will be resolved relative to `self.custom_script_directory`, which in turn
        defaults to `{project_root}/scripts`.
        """
        script_path = Path(script_path)
        if not script_path.is_absolute():
            script_path = (self.custom_script_directory / script_path).absolute()
        return subprocess.run(
            [sys.executable, script_path],
            text=True,
            stdout=stdout,
            stderr=stderr,
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )

    @property
    def entities_directory(self) -> Path:
        return self.project_root / ("events" if self.entities_in_events_directory else "entities")

    # ~~~ PRIVATE METHODS ~~~ #

    @staticmethod
    def _get_timestamp(for_path=False):
        return datetime.datetime.now().strftime("%Y-%m-%d %H%M%S" if for_path else "%Y-%m-%d %H:%M:%S")

    def _build_config_dict(self):
        return {
            "LastSaveVersion": __version__,
            "GameName": self.GAME.name,
            "GameDirectory": str(self.game_root),
            "LastImportTime": self.last_import_time,
            "LastExportTime": self.last_export_time,
            "VanillaGameDirectory": str(self._vanilla_game_root),
            "TextEditorFontSize": DEFAULT_TEXT_EDITOR_FONT_SIZE,
            "EntitiesInEventsDirectory": self.entities_in_events_directory,
            "IncludeVanillaEntities": self.include_vanila_entities,
            "PreferJSON": self.prefer_json,
        }

    def _write_config(self):
        try:
            write_json(self.project_root / "project_config.json", self._build_config_dict())
        except PermissionError:
            raise SoulstructProjectError("No write access to 'project_config.json' in project directory.")

    @staticmethod
    def _validate_project_directory(project_path, default_root) -> Path:
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

    def _get_game_root(self, with_window: ProjectWindow = None):
        initial_dir = self.GAME.default_game_path if Path(self.GAME.default_game_path).is_dir() else None

        if with_window:
            with_window.CustomDialog(
                title="Select game directory for project",
                message=None,
                font_size=10,
                custom_dialog_subclass=GameRootDialog,
                game=self.GAME,
            )
            game_root = with_window.FileDialog.askdirectory(title="Choose your game directory", initialdir=initial_dir)
            if not game_root:
                raise SoulstructProjectError("No game directory selected.")
            game_root = Path(game_root)
        else:
            message = (
                "Type the full path of the root game directory for this project.\n"
                "For example, for Dark Souls Remastered, it might be:\n\n"
                ""
                "    C:/Program Files (x86)/Steam/steamapps/common/DARK SOULS REMASTERED\n"
            )
            game_root = input(message + "\nPATH: ")
            try:
                game_root = Path(game_root)
                if not game_root.is_dir():
                    raise ValueError
            except ValueError:
                raise SoulstructProjectError(f"Invalid game directory: {str(game_root)}.")

        return game_root

    @property
    def vanilla_game_root(self):
        return self._vanilla_game_root if self._vanilla_game_root else self.game_root

    def _check_steam_appid_file(self, game_root):
        steam_appid_path = Path(game_root) / "steam_appid.txt"
        if not steam_appid_path.is_file():
            if self.GAME.steam_appid:
                with steam_appid_path.open("w") as f:
                    f.write(str(self.GAME.steam_appid))
                return True
            return False
        return True


class GameRootDialog(CustomDialog):

    def __init__(self, *args, game: Game = None, **kwargs):
        self.game_name = game.name
        self.generic_game_path = game.generic_game_path
        super().__init__(*args, **kwargs)

    def build(self, message, font_size, font_type, button_names, button_kwargs):
        with self.set_master(auto_rows=0, padx=20, pady=20):
            if self.generic_game_path:
                self.Label(
                    text=f"Navigate to your {self.game_name} installation directory for initial import.\n"
                    "In a standard Steam installation, this will be:",
                    pady=10,
                )
                self.Label(
                    text=self.generic_game_path,
                    font_size=8,
                    font_type="Consolas",
                    bg="#000",
                )
                self.Label(text="Otherwise, Steam can help you find your Steam installation.", pady=10)
            else:
                self.Label(
                    text=f"Navigate to your {self.game_name} installation directory for initial import.\n"
                         "Steam can help you find your Steam installation.",
                    pady=10,
                )
            self.build_buttons(button_names, button_kwargs)
