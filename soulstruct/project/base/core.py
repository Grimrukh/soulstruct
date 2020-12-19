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

from soulstruct.config import DEFAULT_TEXT_EDITOR_FONT_SIZE
from soulstruct.games import Game
from soulstruct.project.core import SoulstructProjectError, RestoreBackupError
from soulstruct.utilities import PACKAGE_PATH, traverse_path_tree
from soulstruct.utilities.window import CustomDialog

if tp.TYPE_CHECKING:
    from soulstruct.ai.base.ai_directory import AIDirectory
    from soulstruct.esd.base.talk_esd_bnd import TalkESDBND
    from soulstruct.game_types import Map
    from soulstruct.maps.base.map_studio_directory import MapStudioDirectory
    from soulstruct.params.base.game_param_bnd import GameParamBND
    from soulstruct.params.darksouls1r.draw_param import DrawParamDirectory
    from soulstruct.project.window import ProjectWindow
    from soulstruct.text.base.msg_directory import MSGDirectory

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
    """Validate `data_type` argument and recur on all project types if it is none."""
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


class GameDirectoryProject(abc.ABC):
    """Manages an entire editable instance of a game installation (or rather, all the file types Soulstruct can handle).

    It is recommended that you create one of these projects for each Soulstruct-based mod.
    """

    # Default project root (for relative project paths) is in the current working directory for standard Python use
    # or next to the frozen PyInstaller executable, if applicable.
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        _DEFAULT_PROJECT_ROOT = Path(sys.executable).parent
    else:
        _DEFAULT_PROJECT_ROOT = Path(os.getcwd())

    GAME: Game = None
    DATA_TYPES = {}  # type: dict[str, type]
    CONVERT_EVENTS: tp.Callable = None
    TALKESD_BND: tp.Type[TalkESDBND] = None
    IGNORE_TALK_FILES: tuple[str] = ()
    ALL_MAPS: list[Map] = None
    GET_MAP: tp.Callable = None

    def __init__(self, project_path="", with_window: ProjectWindow = None):

        self.game_root = Path()
        self.last_import_time = ""
        self.last_export_time = ""
        self.text_editor_font_size = DEFAULT_TEXT_EDITOR_FONT_SIZE
        # TODO: Record last edit time for each file/structure.

        # Initialize with empty structures.
        self.ai_directory = self.DATA_TYPES["ai"]()  # type: AIDirectory
        self.draw_param_directory = self.DATA_TYPES["lighting"]()  # type: DrawParamDirectory
        self.map_studio_directory = self.DATA_TYPES["maps"]()  # type: MapStudioDirectory
        self.game_param_bnd = self.DATA_TYPES["params"]()  # type: GameParamBND
        self.msg_directory = self.DATA_TYPES["text"]()  # type: MSGDirectory
        # No structures for Events or Talk (scripts stored as plain-text EVS and ESP files).

        self.project_root = self._validate_project_directory(project_path, self._DEFAULT_PROJECT_ROOT)
        self.load_config(with_window=with_window)
        self.initialize_project(with_window=with_window)

    @property
    def ai(self) -> AIDirectory:
        return self.ai_directory

    @ai.setter
    def ai(self, value: AIDirectory):
        self.ai_directory = value

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
    def text(self) -> MSGDirectory:
        return self.msg_directory

    @text.setter
    def text(self, value: MSGDirectory):
        self.msg_directory = value

    def initialize_project(self, force_import_from_game=False, with_window: ProjectWindow = None):
        """Load project structures from pickled project files if available, or prompt for initial import to create."""

        yes_to_all = force_import_from_game
        for data_type in self.DATA_TYPES:
            if data_type in ("events", "talk"):
                continue  # Events and Talk are not saved and loaded, just imported and exported.
            try:
                if force_import_from_game:
                    raise FileNotFoundError  # don't bother looking for existing file
                self.load(data_type)
            except FileNotFoundError:
                if yes_to_all:
                    self.import_data_from_game(data_type)
                    self.write(data_type)
                else:
                    if with_window:
                        result = with_window.CustomDialog(
                            title="Project Error",
                            message=f"Could not find saved '{data_type}' data in project.\n"
                            f"Would you like to import it from the game directory now?",
                            button_names=("Yes", "Yes to All", "No, quit now"),
                            button_kwargs=("YES", "YES", "NO"),
                            cancel_output=2,
                            default_output=2,
                        )
                    else:
                        result = (
                            2
                            if input(
                                f"Could not find saved '{data_type}' data in project.\n"
                                f"Would you like to import it from the game directory now? [y]/n"
                            ).lower()
                            == "n"
                            else 0
                        )
                    if result in {0, 1}:
                        self.import_data_from_game(data_type)
                        self.write(data_type)
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
                        button_kwargs=("YES", "NO"),
                        cancel_output=1,
                        default_output=1,
                    )
                else:
                    result = (
                        1
                        if input(
                            f"Could not find any event scripts in project.\n"
                            f"Would you like to import them from the game directory now? [y]/n"
                        ).lower()
                        == "n"
                        else 0
                    )
                if result == 0:
                    self.import_data_from_game("events")

        if not (self.project_root / "talk").is_dir() or not (self.project_root / "talk").glob("*"):
            if yes_to_all:
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
                    result = (
                        1
                        if input(
                            f"Could not find any talk scripts in project.\n"
                            f"Would you like to import them from the game directory now? [y]/n"
                        ).lower()
                        == "n"
                        else 0
                    )
                if result == 0:
                    self.import_data_from_game("talk")

    @_data_type_action
    def write(self, data_type=None):
        """Save given data type ('maps', 'text', etc.) as pickled project file."""
        if data_type in {"events", "talk"}:
            # TODO: Save all scripts to text files.
            pass
        else:
            self._write_project_data(getattr(self, data_type), data_type + ".d1s")

    @_data_type_action
    def load(self, data_type=None):
        """Load give data type ('maps', 'text', etc.) from pickled project file."""
        if data_type in {"events", "talk"}:
            # TODO: Load all scripts from text files.
            pass
        else:
            setattr(self, data_type, self._load_project_data(data_type + ".d1s"))

    def _write_project_data(self, obj, pickled_path):
        with (self.project_root / pickled_path).open("wb") as f:
            pickle.dump(obj, f)

    def _load_project_data(self, pickled_path):
        with (self.project_root / pickled_path).open("rb") as f:
            try:
                return pickle.load(f)
            except Exception as ex:
                raise SoulstructProjectError(
                    f"Could not open project file: {self.project_root / pickled_path}.\n\n"
                    f"If you are seeing this after downloading a new version of Soulstruct, there may have been a "
                    f"non-backwards-compatible change in the internal structure of the program. Please export your "
                    f"project files from the last working version, delete the problematic file(s) after backing them "
                    f"up somewhere else, then re-import them into this new version.\n\n"
                    f"Specific error:\n{ex}"
                )

    @_data_type_action
    def import_data(self, data_type=None, import_directory=None):
        """Import data sub-structure from binary game files.

        If `data_type` is None (default), all data types will be imported, in which case the given `import_directory`
        should contain the appropriate folder structure ('map/MapStudio', 'msg/ENGLISH', etc.) for all files.
        """
        import_directory = Path(import_directory)
        data_import_path = self._game_path(data_type, root=import_directory)
        if data_type == "events":
            self._import_events(data_import_path)
        elif data_type == "talk":
            self._import_talk(data_import_path)
        else:
            data_instance = self.DATA_TYPES[data_type](data_import_path)
            print(self, data_type, data_instance)
            setattr(self, data_type, data_instance)

    def import_data_from_game(self, data_type=None):
        """Reads data substructures in game formats from the live game directory."""
        self.import_data(data_type=data_type, import_directory=self.game_root)

    def _import_events(self, import_directory):
        """Converts binary EMEVD to EVS.PY in '[project]/events'."""
        self.CONVERT_EVENTS(
            output_type="evs.py",
            output_directory=self.project_root / "events",
            input_type=self.GAME.dcxify("emevd"),
            input_directory=import_directory,
        )

    def _import_talk(self, import_directory):
        """Write all Talk ESD files in given directory into project as ESP files sorted by map folders."""
        for talkesdbnd in import_directory.glob(f"*.talkesdbnd" + (".dcx" if self.GAME.uses_dcx else "")):
            map_id = talkesdbnd.name.split(".talkesdbnd")[0]
            if map_id not in self.IGNORE_TALK_FILES:
                self.TALKESD_BND(talkesdbnd).write_all_esp(self.project_root / f"talk/{map_id}")

    @_data_type_action
    def export_data(self, data_type=None, export_directory=None):
        export_directory = Path(export_directory)
        data_export_path = self._game_path(data_type, root=export_directory)
        data_export_path.mkdir(parents=True, exist_ok=True)
        if data_type == "events":
            # Never called from window ("Export Events" exports selected script only).
            self._export_events(data_export_path)
        elif data_type == "talk":
            # Never called from window ("Export Talk" exports all talk in selected map only).
            self._export_talk(data_export_path)
        else:
            getattr(self, data_type).save(data_export_path)

    def export_data_to_game(self, data_type=None):
        """Writes data substructures in game formats in the live game directory, ready for play."""
        self.export_data(data_type=data_type, export_directory=self.game_root)

    def export_timestamped_backup(self, data_type=None):
        timestamped = self.project_root / "export" / self._get_timestamp(for_path=True)
        self.export_data(data_type=data_type, export_directory=timestamped)

    def _export_events(self, export_directory):
        """Converts EVS.PY in '[project]/events' to binary EMEVD."""
        # TODO: File menu export option may only export current EMEVD? Should export all by calling this.
        self.CONVERT_EVENTS(
            output_type=self.GAME.dcxify("emevd"),
            output_directory=export_directory,
            input_type="evs.py",
            input_directory=self.project_root / "events",
        )
        _LOGGER.info("Event files (EMEVD) written successfully.")

    def _export_talk(self, export_directory):
        """Exports all TalkESDBND files to game from individual map folders in '[project]/talk'."""
        for map_directory in (self.project_root / "talk").glob("*"):
            if map_directory.name not in [g.name for g in self.ALL_MAPS]:
                continue  # unexpected folder
            bnd_file_name = self.GAME.dcxify(self.GET_MAP(map_directory.name).esd_file_stem + ".talkesdbnd")
            talk = self.TALKESD_BND(map_directory)
            talk.write(export_directory / bnd_file_name)

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
        with PACKAGE_PATH("project/files.json").open("r") as f:
            game_files = json.load(f)[self.GAME.name]
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
        with PACKAGE_PATH("project/files.json").open("rb") as f:
            game_files = json.load(f)[self.GAME.name]
        for file_path_parts in traverse_path_tree(game_files):
            backup_file_path = backup_path / Path(*file_path_parts)
            if not backup_file_path.is_file():
                raise FileNotFoundError(f"Could not find backup file to restore: " f"{str(backup_file_path)}")
            game_file_path = Path(self.game_root, *file_path_parts)
            game_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(backup_file_path), str(game_file_path))

    def load_config(self, with_window: ProjectWindow = None):
        try:
            with (self.project_root / "project_config.json").open("r") as f:
                try:
                    config = json.load(f)
                except json.JSONDecodeError:
                    raise SoulstructProjectError(
                        "Could not interpret 'project_config.json' file. Check it for errors, or "
                        "delete it to have Soulstruct create a fresh copy on next load."
                    )
                else:
                    try:
                        if self.GAME.name != config["GameName"]:
                            raise SoulstructProjectError(
                                f"Project config 'GameName' is {config['GameName']}, but `GameDirectoryProject` "
                                f"instance belongs to {self.GAME.name}."
                            )
                        self.game_root = Path(config["GameDirectory"])
                        self.last_import_time = config.get("LastImportTime", None)
                        self.last_export_time = config["LastExportTime"]
                        self.text_editor_font_size = config.get("TextEditorFontSize", DEFAULT_TEXT_EDITOR_FONT_SIZE)
                    except KeyError:
                        raise SoulstructProjectError(
                            "Project config file does not contain necessary settings. "
                            "Delete it and load the project directory again to create "
                            "a fresh copy and re-link your project to the game."
                        )
        except FileNotFoundError:
            # Create project config file.
            try:
                self.game_root = self._get_game_root(with_window=with_window)
            except SoulstructProjectError as e:
                raise SoulstructProjectError(str(e) + "\n\nAborting project setup.")
            self._write_config()
            if with_window:
                result = with_window.CustomDialog(
                    title="Import Project Files",
                    message="Import game files now? This will override any project\n"
                    "files that are already in this folder.",
                    button_names=("Yes, import the files", "No, I'll do it later"),
                    button_kwargs=("YES", "NO"),
                    cancel_output=None,
                    default_output=0,
                )
            else:
                result = input(
                    "Import game files now? This will override any project files\n"
                    "that are already in this folder. [y]/n"
                )
                if result.lower == "n":
                    result = 1
                else:
                    result = 0
            if result == 0:
                self.initialize_project(force_import_from_game=True)

    def _game_path(self, data_type, root=None):
        root = self.game_root if root is None else Path(root)
        data_class_name = self.DATA_TYPES[data_type.lower()].__name__
        try:
            return root / self.GAME.default_file_paths[data_class_name]
        except KeyError:
            raise KeyError(f"Could not get data path to {data_type} ({data_class_name}) for game {self.GAME.name}")

    @staticmethod
    def _get_timestamp(for_path=False):
        return datetime.datetime.now().strftime("%Y-%m-%d %H%M%S" if for_path else "%Y-%m-%d %H:%M:%S")

    def _build_config_dict(self):
        return {
            "GameName": self.GAME.name,
            "GameDirectory": str(self.game_root),
            "LastImportTime": self.last_import_time,
            "LastExportTime": self.last_export_time,
            "TextEditorFontSize": DEFAULT_TEXT_EDITOR_FONT_SIZE,
        }

    def _write_config(self):
        try:
            with (self.project_root / "project_config.json").open("w") as f:
                json.dump(self._build_config_dict(), f, indent=4)
        except PermissionError:
            raise SoulstructProjectError("No write access to 'project_config.json' in project directory.")

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

    def _get_game_root(self, with_window: ProjectWindow = None):
        initial_dir = self.GAME.default_game_path if Path(self.GAME.default_game_path).is_dir() else None

        if with_window:
            with_window.CustomDialog(
                title="Select game directory for project",
                message=None,
                font_size=10,
                custom_dialog_subclass=GameRootDialog,
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
    def build(self, message, font_size, font_type, button_names, button_kwargs):
        with self.set_master(auto_rows=0, padx=20, pady=20):
            self.Label(
                text="Navigate to the game installation directory for this project.\n"
                "In a standard Steam installation, this will be:",
                pady=10,
            )
            self.Label(text="Dark Souls: Prepare to Die Edition", font_type="Consolas")
            self.Label(
                text="C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/DATA",
                font_size=8,
                font_type="Consolas",
                bg="#000",
            )
            self.Label(text="Dark Souls Remastered", font_type="Consolas")
            self.Label(
                text="C:/Program Files (x86)/Steam/steamapps/common/DARK SOULS REMASTERED/",
                font_size=8,
                font_type="Consolas",
                bg="#000",
            )
            self.Label(text="Steam can help you find your Steam installation.", pady=10)
            self.build_buttons(button_names, button_kwargs)
