from __future__ import annotations

import datetime
import json
import logging
import os
import pickle
import shutil
import subprocess
import sys
import threading
from typing import TYPE_CHECKING
from functools import wraps
from pathlib import Path

from soulstruct._config import PTDE_PATH, DSR_PATH
from soulstruct.ai import DarkSoulsAIScripts
from soulstruct.constants.darksouls1.maps import ALL_MAPS, get_map
from soulstruct.esd.dark_souls_talk import TalkESDBND
from soulstruct.events.darksouls1.core import convert_events
from soulstruct.maps import DarkSoulsMaps
from soulstruct.params import DarkSoulsGameParameters, DarkSoulsLightingParameters
from soulstruct.text import DarkSoulsText
from soulstruct.utilities import PACKAGE_PATH, traverse_path_tree
from soulstruct.utilities.window import CustomDialog

from .utilities import SoulstructProjectError, data_type_caps, RestoreBackupError, DATA_TYPES

if TYPE_CHECKING:
    from .window import SoulstructProjectWindow


try:
    import psutil
except ImportError:
    psutil = None

__all__ = ["SoulstructProject"]
_LOGGER = logging.getLogger(__name__)

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


class SoulstructProject:
    """Manages a directory of easily-modded Soulstruct files that can imported and exported.

    It is recommended that you create one of these projects for each Soulstruct-based mod.

    Currently supports only Dark Souls 1.

    TODO:
        - Eventually have subclasses for different games, with shared methods here.
    """

    # Default project root (for relative project paths) is in the current working directory for standard Python use
    # or next to the frozen PyInstaller executable, if applicable.
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        _DEFAULT_PROJECT_ROOT = Path(sys.executable).parent
    else:
        _DEFAULT_PROJECT_ROOT = Path(os.getcwd())

    def __init__(self, project_path="", with_window: SoulstructProjectWindow = None):

        self.game_name = ""
        self.game_root = Path()
        self.game_exe_path = Path()
        self.game_save_root = Path()
        self.last_import_time = ""
        self.last_export_time = ""
        self.text_font_size = 10
        # TODO: Record last edit time for each file/structure.

        # Initialize with empty structures.
        self.Text = DarkSoulsText()
        self.Params = DarkSoulsGameParameters()
        self.Lighting = DarkSoulsLightingParameters()
        self.Maps = DarkSoulsMaps()
        self.AI = DarkSoulsAIScripts()
        # No structures for Events or Talk (scripts stored as plain-text EVS and ESP files).

        self.project_root = self._validate_project_directory(project_path, self._DEFAULT_PROJECT_ROOT)
        self.load_config(with_window=with_window)
        self.initialize_project(with_window=with_window)

    def initialize_project(self, force_import_from_game=False, with_window: SoulstructProjectWindow = None):
        """Load project structures from pickled project files if available, or prompt for initial import to create."""
        if self.game_name == "Dark Souls Prepare to Die Edition":
            self._check_ptde_unpacked()

        yes_to_all = force_import_from_game
        for data_type in DATA_TYPES:
            if data_type in ("events", "talk"):
                continue  # Events and Talk are not saved and loaded, just imported and exported.
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
                            message=f"Could not find saved {data_type_caps(data_type)} data in project.\n"
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
                                f"Could not find saved {data_type_caps(data_type)} data in project.\n"
                                f"Would you like to import it from the game directory now? [y]/n"
                            ).lower()
                            == "n"
                            else 0
                        )
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
        self._save_project_data(getattr(self, data_type_caps(data_type)), data_type + ".d1s")

    def load(self, data_type=None):
        """Load give data type ('maps', 'text', etc.) from pickled project file. Defaults to loading all types (except
        'events', which are handled manually)."""
        if data_type is None:
            for data_type in [k for k, v in DATA_TYPES.items() if v]:
                self.load(data_type)
        data_type = data_type.lower()
        if data_type not in DATA_TYPES:
            raise ValueError(f"Data type to save should be one of {DATA_TYPES} (or None), not {data_type}.")
        setattr(self, data_type_caps(data_type), self._load_project_data(data_type + ".d1s"))

    def _save_project_data(self, obj, pickled_path):
        with (self.project_root / pickled_path).open("wb") as f:
            pickle.dump(obj, f)

    def _load_project_data(self, pickled_path):
        with (self.project_root / pickled_path).open("rb") as f:
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
        elif data_type == "talk":
            self._import_talk(data_import_path)
        else:
            setattr(self, data_type_caps(data_type), DATA_TYPES[data_type](data_import_path))

    def import_data_from_game(self, data_type=None):
        """Reads data substructures in game formats from the live game directory."""
        self.import_data(data_type=data_type, import_directory=self.game_root)

    def _import_events(self, import_directory):
        """Converts binary EMEVD to EVS.PY in '[project]/events'."""
        convert_events(
            output_type="evs.py",
            output_directory=self.project_root / "events",
            input_type="emevd.dcx" if self.game_name == "Dark Souls Remastered" else "emevd",
            input_directory=import_directory,
        )

    def _import_talk(self, import_directory):
        if self.game_name == "Dark Souls Prepare to Die Edition":
            game_version = "ptde"
        elif self.game_name == "Dark Souls Remastered":
            game_version = "dsr"
        else:
            raise ValueError("Cannot export talk for non-DS1 game.")
        for talkesdbnd in import_directory.glob(f"*.talkesdbnd{'.dcx' if game_version == 'dsr' else ''}"):
            map_id = talkesdbnd.name.split(".talkesdbnd")[0]
            if map_id in ("m12_00_00_01", "m14_02_00_00"):
                continue  # skipped
            TalkESDBND(talkesdbnd, game_version=game_version).write_all_esp(self.project_root / f"talk/{map_id}")

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
            # Never called from window ("Export Events" exports selected script only).
            self._export_events(data_export_path)
        elif data_type == "talk":
            # Never called from window ("Export Talk" exports all talk in selected map only).
            self._export_talk(data_export_path)
        else:
            getattr(self, data_type_caps(data_type)).save(data_export_path)

    def export_data_to_game(self, data_type=None):
        """Writes data substructures in game formats in the live game directory, ready for play."""
        self.export_data(data_type=data_type, export_directory=self.game_root)

    def export_timestamped_backup(self, data_type=None):
        timestamped = self.project_root / "export" / self._get_timestamp(for_path=True)
        self.export_data(data_type=data_type, export_directory=timestamped)

    def _export_events(self, export_directory):
        """Converts EVS.PY in '[project]/events' to binary EMEVD."""
        convert_events(
            output_type="emevd.dcx" if self.game_name == "Dark Souls Remastered" else "emevd",
            output_directory=export_directory,
            input_type="evs.py",
            input_directory=self.project_root / "events",
        )
        _LOGGER.info("Dark Souls event files (EMEVD) written successfully.")

    def _export_talk(self, export_directory):
        """Exports all TalkESDBND files to game from individual map folders in '[project]/talk'."""
        if self.game_name == "Dark Souls Prepare to Die Edition":
            game_version = "ptde"
        elif self.game_name == "Dark Souls Remastered":
            game_version = "dsr"
        else:
            raise ValueError("Cannot export talk for non-DS1 game.")
        for map_directory in (self.project_root / "talk").glob("*"):
            if map_directory.name not in [g.name for g in ALL_MAPS]:
                continue  # unexpected folder
            bnd_file_name = get_map(map_directory.name).esd_file_stem + ".talkesdbnd"
            talk = TalkESDBND(map_directory, game_version=game_version)
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

    def launch_game(self, try_force_quit_first=False, threaded=True, debug=False):
        if not psutil:
            raise ModuleNotFoundError(
                "Python package `psutil` required for this method. Install it with `python -m pip install psutil`."
            )

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
        if not self.game_save_root.is_dir():
            raise SoulstructProjectError(f"Could not find Dark Souls save directory root: {str(self.game_save_root)}")
        if self.game_name == "Dark Souls Remastered":
            steam_id_folders = list(self.game_save_root.glob("*"))
            if len(steam_id_folders) > 1:
                raise SoulstructProjectError(
                    f"Multiple Dark Souls Remastered save folders found in {str(self.game_save_root)}. Please move all "
                    f"of them except your real one."
                )
            elif not steam_id_folders:
                raise SoulstructProjectError(
                    f"No Dark Souls Remastered save folders found in {str(self.game_save_root)}."
                )
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

    def create_game_backup(self, backup_path=None):
        """Copy existing game files (that can be edited with Soulstruct) to a backup directory, which defaults to
        'soulstruct-backup' in your game directory. Use `restore_game_backup(backup_dir)` to restore those files."""
        if backup_path is None:
            backup_path = self.game_root / "soulstruct-backup"
        else:
            backup_path = Path(backup_path)
        with PACKAGE_PATH("project/files.json").open("rb") as f:
            game_files = json.load(f)[self.game_name]
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
            game_files = json.load(f)[self.game_name]
        for file_path_parts in traverse_path_tree(game_files):
            backup_file_path = backup_path / Path(*file_path_parts)
            if not backup_file_path.is_file():
                raise FileNotFoundError(f"Could not find backup file to restore: " f"{str(backup_file_path)}")
            game_file_path = Path(self.game_root, *file_path_parts)
            game_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(backup_file_path), str(game_file_path))

    def load_config(self, with_window: SoulstructProjectWindow = None):
        try:
            with (self.project_root / "config.json").open("r") as f:
                try:
                    config = json.load(f)
                except json.JSONDecodeError:
                    raise SoulstructProjectError(
                        "Could not interpret 'config.json' file. Check it for errors, or "
                        "delete it to have Soulstruct create a fresh copy on next load."
                    )
                else:
                    try:
                        self.game_name = config["GameName"]
                        self.game_exe_path = Path(config["GameExecutable"])
                        self.game_root = Path(config["GameDirectory"])
                        self.game_save_root = Path(config["SaveDirectory"])
                        self.last_import_time = config.get("LastImportTime", None)
                        self.last_export_time = config["LastExportTime"]
                        self.text_font_size = config.get("TextFontSize", 10)
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

    def _check_ptde_unpacked(self):
        if not (self.game_root / "map").is_dir():
            raise SoulstructProjectError(
                "Your Dark Souls: Prepare to Die Edition does not appear to be unpacked.\n"
                "Please download and run 'UnpackDarkSoulsForModding' (UDSFM) from Nexus:\n"
                "https://www.nexusmods.com/darksouls/mods/1304"
            )

    def _game_path(self, data_type, root=None):
        root = self.game_root if root is None else Path(root)
        data_type = data_type.lower()
        if data_type == "maps":
            return root / "map/MapStudio"
        elif data_type == "params":
            return root / "param/GameParam"
        elif data_type == "text":
            return root / "msg/ENGLISH"
        elif data_type == "lighting":
            return root / "param/DrawParam"
        elif data_type == "events":
            return root / "event"
        elif data_type == "ai":
            return root / "script"
        elif data_type == "talk":
            return root / "script/talk"
        else:
            raise ValueError(f"Invalid game data type: {data_type}")

    @staticmethod
    def _get_timestamp(for_path=False):
        return datetime.datetime.now().strftime("%Y-%m-%d %H%M%S" if for_path else "%Y-%m-%d %H:%M:%S")

    def _build_config_dict(self):
        return {
            "GameName": self.game_name,
            "GameExecutable": str(self.game_exe_path),
            "GameDirectory": str(self.game_root),
            "SaveDirectory": str(self.game_save_root),
            "LastImportTime": self.last_import_time,
            "LastExportTime": self.last_export_time,
            "TextFontSize": self.text_font_size,
        }

    def _write_config(self):
        try:
            with (self.project_root / "config.json").open("w") as f:
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
            with_window.CustomDialog(
                title="Select game for project", message=None, font_size=10, custom_dialog_subclass=GameRootDialog
            )
            game_exe = with_window.FileDialog.askopenfilename(
                title="Choose your game executable", initialdir=initial_dir, filetypes=[("Game executable", ".exe")]
            )
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
        if (game_root / "DarkSoulsRemastered.exe").is_file():
            return game_root, game_exe, "Dark Souls Remastered"
        elif (game_root / "DARKSOULS.exe").is_file():
            return game_root, game_exe, "Dark Souls Prepare to Die Edition"
        else:
            raise SoulstructProjectError(
                "Soulstruct projects are only supported for Dark Souls 1 (either version),\n"
                "but your selected executable was not a version of Dark Souls."
            )

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


class GameRootDialog(CustomDialog):
    def build(self, message, font_size, font_type, button_names, button_kwargs):
        with self.set_master(auto_rows=0, padx=20, pady=20):
            self.Label(
                text="Navigate to the game executable for this project.\n"
                "In a standard Steam installation, this will be:",
                pady=10,
            )
            self.Label(text="Dark Souls: Prepare to Die Edition", font_type="Consolas")
            self.Label(
                text="C:/Program Files (x86)/Steam/steamapps/common/Dark Souls Prepare to Die Edition/"
                "DATA/DARKSOULS.exe",
                font_size=8,
                font_type="Consolas",
                bg="#000",
            )
            self.Label(text="Dark Souls Remastered", font_type="Consolas")
            self.Label(
                text="C:/Program Files (x86)/Steam/steamapps/common/DARK SOULS REMASTERED/" "DarkSoulsRemastered.exe",
                font_size=8,
                font_type="Consolas",
                bg="#000",
            )
            self.Label(text="Steam can help you find your Steam installation.", pady=10)
            self.build_buttons(button_names, button_kwargs)
