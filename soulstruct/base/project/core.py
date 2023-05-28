from __future__ import annotations

__all__ = ["ProjectDataType", "GameDirectoryProject", "DATA_CLASS_TYPING", "DATA_OBJECT_TYPING"]

import abc
import datetime
import json
import logging
import os
import re
import shutil
import subprocess
import sys
import threading
import typing as tp
from pathlib import Path

from soulstruct import __version__
from soulstruct.config import DEFAULT_TEXT_EDITOR_FONT_SIZE
from soulstruct.games import get_game
from soulstruct.utilities.files import PACKAGE_PATH, read_json, write_json
from soulstruct.utilities.misc import traverse_path_tree
from soulstruct.utilities.window import CustomDialog

from .enums import ProjectDataType
from .exceptions import SoulstructProjectError, RestoreBackupError
from .save_manager import SaveManager

if tp.TYPE_CHECKING:
    from soulstruct.games import Game
    # Relative imports for easier copy-pasting into game submodules.
    from ..ai import LuaBND, AIScriptDirectory
    from ..game_types import GameEnumsManager
    from ..events import EventDirectory
    from ..ezstate import TalkDirectory
    from ..maps import MapStudioDirectory
    from ..params import GameParamBND
    from soulstruct.darksouls1ptde.params.draw_param import DrawParamDirectory  # TODO: Move to PTDE/DSR subclasses.
    from ..text import MSGDirectory
    from .window import ProjectWindow

    DATA_OBJECT_TYPING = tp.Union[
        AIScriptDirectory,
        # `Events` has no data object, just plaintext EVS scripts.
        GameEnumsManager,
        DrawParamDirectory,
        GameParamBND,
        MapStudioDirectory,
        MSGDirectory,
        # `Talk` has no data object, just plaintext EVS scripts.
    ]

    DATA_CLASS_TYPING = tp.Union[
        AIScriptDirectory,
        EventDirectory,
        GameEnumsManager,
        DrawParamDirectory,
        GameParamBND,
        MapStudioDirectory,
        MSGDirectory,
        TalkDirectory,
    ]

try:
    import psutil
except ImportError:
    psutil = None

_LOGGER = logging.getLogger(__name__)

_GAME_MODULE_RE = re.compile(r"^soulstruct\.(\w+)\..*$")


class GameDirectoryProject(abc.ABC):
    """Manages an entire editable instance of a game installation (or at least, all the files Soulstruct can handle
    for that specific game).

    It is recommended that you create one of these projects for each Soulstruct-based mod.
    """

    # Default project root (for relative project paths) is in the current working directory for standard Python
    # environments or next to the frozen PyInstaller executable.
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        _DEFAULT_PROJECT_ROOT = Path(sys.executable).parent
    else:
        _DEFAULT_PROJECT_ROOT = Path(os.getcwd())

    # Maps `ProjectDataType` enums supported by this game to the classes that load them (`MapStudioDirectory`, etc.).
    DATA_TYPES: tp.ClassVar[dict[ProjectDataType, tp.Type[DATA_CLASS_TYPING]]] = {}
    DataType: tp.ClassVar[tp.Type[ProjectDataType]] = ProjectDataType

    game_root: Path
    project_root: Path
    save_manager: SaveManager
    last_import_time: str
    last_export_time: str
    python_script_directory: Path
    text_editor_font_size: int
    enums_in_events_folder: bool
    other_settings: dict[str, tp.Any]

    # Instance data dictionary. Contents should be accessed with properties (`ai`, `maps`, etc.).
    # Values here are not necessarily classes from `DATA_TYPES.values()`, e.g. Events/Talk are stored as plaintext.
    _data: dict[ProjectDataType, DATA_OBJECT_TYPING | None]
    _vanilla_game_root: Path | None

    def __init__(self, project_path="", with_window: ProjectWindow = None, game_root: Path | str = None):

        self.game_root = Path()
        self.save_manager = SaveManager(self.get_game())
        self.last_import_time = ""
        self.last_export_time = ""
        self._vanilla_game_root = None
        self.python_script_directory = Path()
        self.text_editor_font_size = DEFAULT_TEXT_EDITOR_FONT_SIZE
        self.enums_in_events_folder = False
        self.do_not_write_param_defaults = True
        self.other_settings = {}

        self._data = {}

        self.project_root = self._validate_project_directory(Path(project_path), self._DEFAULT_PROJECT_ROOT)

        config_path = self.project_root / "project_config.json"
        if config_path.is_file():
            success = self.load_existing_project(config_path, new_game_root=game_root)
            if not success:
                _LOGGER.warning("Project load interrupted. Project instance will be empty.")
        else:
            success = self.create_new_project(with_window=with_window, game_root=game_root)
            if not success:
                _LOGGER.warning("Project creation interrupted. Project instance will be empty.")

    def _get_data(self, data_type: ProjectDataType) -> DATA_OBJECT_TYPING:
        if data_type not in self.DATA_TYPES:
            raise TypeError(f"This game's `GameDirectoryProject` does not support {data_type.name} data.")
        return self._data.get(data_type, None)

    def _set_data(self, data_type: ProjectDataType, data: DATA_OBJECT_TYPING):
        if data_type not in self.DATA_TYPES:
            raise TypeError(f"This game's `GameDirectoryProject` does not support {data_type.name} data.")
        self._data[data_type] = data

    def get_data_class(self, data_type: ProjectDataType) -> tp.Type[DATA_CLASS_TYPING]:
        if data_type not in self.DATA_TYPES:
            raise TypeError(f"This game's project class does not support {data_type.name} data.")
        return self.DATA_TYPES[data_type]

    @property
    def vanilla_game_root(self):
        return self._vanilla_game_root if self._vanilla_game_root else self.game_root

    @property
    def is_empty(self) -> bool:
        return not self._data

    # region Data Properties
    @property
    def ai(self) -> AIScriptDirectory:
        return self._get_data(ProjectDataType.AI)

    @ai.setter
    def ai(self, value: AIScriptDirectory):
        self._set_data(ProjectDataType.AI, value)

    # NOTE: No `events` property. Events are stored as plaintext EVS scripts until binary file needs to be written.

    @property
    def events_directory(self):
        return self.project_root / "events"

    @property
    def lighting(self) -> DrawParamDirectory:
        return self._get_data(ProjectDataType.Lighting)

    @lighting.setter
    def lighting(self, value: DrawParamDirectory):
        self._set_data(ProjectDataType.Lighting, value)

    @property
    def maps(self) -> MapStudioDirectory:
        return self._get_data(ProjectDataType.Maps)

    @maps.setter
    def maps(self, value: MapStudioDirectory):
        self._set_data(ProjectDataType.Maps, value)

    @property
    def enums_directory(self) -> Path:
        """Enums modules can optionally be written next to EVS scripts in 'events' folder, but by default,
        go in their own folder 'enums'."""
        return self.project_root / ("events" if self.enums_in_events_folder else "enums")

    @property
    def params(self) -> GameParamBND:
        return self._get_data(ProjectDataType.Params)

    @params.setter
    def params(self, value: GameParamBND):
        self._set_data(ProjectDataType.Params, value)

    # NOTE: No `talk` property. Talk scripts are stored as plaintext ESP scripts until binary file needs to be written.

    @property
    def talk_directory(self):
        return self.project_root / "talk"

    @property
    def text(self) -> MSGDirectory:
        return self._get_data(ProjectDataType.Text)

    @text.setter
    def text(self, value: MSGDirectory):
        self._set_data(ProjectDataType.Text, value)
    # endregion

    # region Project Import Methods
    def _default_import(self, data_type: ProjectDataType, import_directory: Path | str) -> DATA_OBJECT_TYPING:
        """Simply uses `from_path()` method of data type class."""
        # TODO: warn user if project data already exists (even though we're not saving yet).
        data_class = self.get_data_class(data_type)
        import_directory = Path(import_directory)
        data_import_path = self.get_data_game_path(data_type, root=import_directory)
        return data_class.from_path(data_import_path)

    def import_all(self, import_directory: Path | str):
        for data_type in self.DATA_TYPES:
            import_func = getattr(self, f"import_{data_type}")
            import_func(import_directory)

    def import_AI(self, import_directory: Path | str):
        """Currently no options."""
        ai = self._default_import(ProjectDataType.AI, import_directory)
        self._set_data(ProjectDataType.AI, ai)

    def import_Maps(self, import_directory: Path | str):
        maps = self._default_import(ProjectDataType.Maps, import_directory)  # type: MapStudioDirectory
        self._set_data(ProjectDataType.Maps, maps)

    def import_Enums(self, import_directory: Path | str, use_loaded_maps_data=True, put_enums_in_events_folder=False):
        """Generates `{map_stem}_enums.py` modules from MSBs.

        Uses existing `maps` data if available and `use_maps_data` is True. Otherwise, imports temporary MSBs.
        """
        if use_loaded_maps_data and self.maps:
            maps = self.maps
        else:  # temporary MSB import
            maps = self._default_import(ProjectDataType.Maps, import_directory)  # type: MapStudioDirectory

        if put_enums_in_events_folder and ProjectDataType.Events not in self.DATA_TYPES:
            _LOGGER.warning("Cannot put enums modules in 'events' folder when game project does not support Events.")
            put_enums_in_events_folder = False

        self.enums_in_events_folder = put_enums_in_events_folder

        enums_folder = self.enums_directory
        for map_stem, msb in maps.files.items():
            game_map = maps.GET_MAP(map_stem)
            msb.write_enums_module(enums_folder / f"{game_map.emevd_file_stem}_enums.py")

        # No data to set (Python module files on disk ARE the project data).

    def import_Params(self, import_directory: Path | str):
        """Currently no options."""
        params = self._default_import(ProjectDataType.Params, import_directory)
        self._set_data(ProjectDataType.Params, params)

    def import_Lighting(self, import_directory: Path | str):
        """Currently no options."""
        lighting = self._default_import(ProjectDataType.Lighting, import_directory)
        self._set_data(ProjectDataType.Lighting, lighting)

    def import_Events(
        self,
        import_directory: Path | str,
        use_enums_in_event_scripts=True,
        copy_python_events_submodule=False,
    ):
        event_class = self.get_data_class(ProjectDataType.Events)  # type: tp.Type[EventDirectory]
        import_directory = Path(import_directory)
        event_directory_path = self.get_data_game_path(ProjectDataType.Events, root=import_directory)
        event_directory = event_class.from_path(event_directory_path)
        # TODO: Enums must be written first to make use of them (obviously).
        #  Can just pass our GameEnumsManager itself, in that case.
        event_directory.write_evs()
        if use_enums_in_event_scripts:
            enums_directory = self.enums_directory
        else:
            enums_directory = None
        event_directory.write_evs(
            self.events_directory,
            enums_directory=enums_directory,
            warn_missing_enums=True,  # TODO: project setting
            enums_module_prefix="." if self.enums_in_events_folder else "..enums.",
        )
        if copy_python_events_submodule:
            self.copy_events_submodule()

    def import_Text(self, import_directory: Path | str, delete_empty_text_entries=True):
        """Option to remove all empty strings from all FMGs."""
        text = self._default_import(ProjectDataType.Text, import_directory)  # type: MSGDirectory
        if delete_empty_text_entries:
            text.remove_empty_strings(category_name_regex=r".*")
        self._set_data(ProjectDataType.Text, text)

    def import_Talk(self, import_directory: Path | str):
        # TODO: Automatically writes ESP scripts to project. Should be made clear.
        talk_class = self.get_data_class(ProjectDataType.Talk)  # type: tp.Type[TalkDirectory]
        import_directory = Path(import_directory)
        talk_directory_path = self.get_data_game_path(ProjectDataType.Talk, root=import_directory)
        talk_directory = talk_class.from_path(talk_directory_path)
        talk_directory.write_esp_directory(self.talk_directory)
    # endregion

    # region Project Export Methods
    def _get_data_and_export_path(
        self, data_type: ProjectDataType, export_directory: Path | str
    ) -> tuple[DATA_OBJECT_TYPING | None, Path | None]:
        """Get default path for exporting `data_type` relative to root `export_directory`."""
        data = self._get_data(data_type)
        if not data:
            _LOGGER.warning(f"There is no {data_type.name} data to export in this project.")
            return None, None
        return data, self.get_data_game_path(data_type, root=Path(export_directory))

    def export_all(self, export_directory: Path | str):
        for data_type in self.DATA_TYPES:
            export_func = getattr(self, f"export_{data_type.name}")
            export_func(export_directory)

    def export_AI(self, export_directory: Path | str, specific_map=""):
        ai, export_path = self._get_data_and_export_path(ProjectDataType.AI, export_directory)
        if specific_map:
            luabnd = ai[specific_map]  # type: LuaBND
            luabnd.write(export_path / specific_map, check_hash=True)  # extension handled automatically
        else:
            ai.write(export_path, check_file_hashes=True)
        self._write_config()

    # TODO: Enums cannot be exported. However, may want to do a 'final sync' before exporting Maps/Events.

    def export_Events(self, export_directory: Path | str, specific_map=""):
        event_class = self.get_data_class(ProjectDataType.Events)  # type: tp.Type[EventDirectory]
        _, export_path = self._get_data_and_export_path(ProjectDataType.Events, export_directory)
        if specific_map:
            emevd = event_class.FILE_CLASS.from_evs_path(
                self.events_directory / f"{specific_map}.evs.py",
                script_directory=self.events_directory,
            )
            emevd.write(export_path / specific_map)  # extension handled automatically
        else:
            event_directory = event_class.from_path(self.project_root / "events")  # just saved
            event_directory.write(export_path)
        self._write_config()

    def export_Lighting(self, export_directory: Path | str, specific_area=""):
        lighting, export_path = self._get_data_and_export_path(ProjectDataType.Lighting, export_directory)
        if specific_area:
            drawparambnd = lighting[specific_area]
            drawparambnd.write(export_path / (specific_area + "_DrawParam"))  # extension handled automatically
        else:
            lighting.write(export_path)
        self._write_config()

    def export_Maps(self, export_directory: Path | str, specific_map=""):
        maps, export_path = self._get_data_and_export_path(ProjectDataType.Maps, export_directory)
        if specific_map:
            msb = maps[specific_map]
            msb.write(export_path / specific_map)  # extension handled automatically
        else:
            maps.write(export_path)
        self._write_config()

    def export_Params(self, export_directory: Path | str, specific_param=""):
        params, export_path = self._get_data_and_export_path(ProjectDataType.Params, export_directory)
        if specific_param and export_path.is_file():
            # Open active Binder and modify precise entry. Probably still faster than writing all Params.
            param = params[specific_param]
            params_class = self.get_data_class(ProjectDataType.Params)  # type: tp.Type[GameParamBND]
            gameparambnd = GameParamBND.from_path(export_path)
            internal_name = params_class.PARAM_NICKNAMES[specific_param]
            entry = gameparambnd.find_entry_matching_name(rf"{internal_name}\.param")
            entry.set_from_binary_file(param)
            gameparambnd.write()  # same path
        else:
            params.write(export_path)
        self._write_config()

    def export_Text(self, export_directory: Path | str, specific_fmg=""):
        text, export_path = self._get_data_and_export_path(ProjectDataType.Text, export_directory)
        if specific_fmg:
            # TODO: need to map FMG nickname to msgbnd name, entry index
            raise NotImplementedError("Cannot export specific Text categories yet.")
        else:
            text.write(export_path)
        self._write_config()

    def export_Talk(self, export_directory: Path | str, specific_map="", specific_talk_id=-1):
        """Export ESP scripts in 'talk' directory as binary game files."""
        talk_class = self.get_data_class(ProjectDataType.Talk)  # type: tp.Type[TalkDirectory]
        _, export_path = self._get_data_and_export_path(ProjectDataType.Talk, export_directory)
        if specific_map:
            if (
                specific_talk_id > -1
                and (export_path / f"t{specific_talk_id}{talk_class.FILE_CLASS.get_default_extension()}").is_file()
            ):
                talkesdbnd = talk_class.FILE_CLASS.from_path(export_path)
                esd = talkesdbnd.find_entry_matching_name(rf"t{specific_talk_id}.esd")
                talk = talkesdbnd.TALK_ESD_CLASS.from_esp_file(
                    self.project_root / f"talk/{specific_map}/t{specific_talk_id}.esp.py"
                )
                esd.set_from_binary_file(talk)
                talkesdbnd.write()  # same path
            else:
                talkesdbnd = talk_class.FILE_CLASS.from_esp_directory(self.talk_directory / specific_map)
                talkesdbnd.write(export_path / specific_map, check_hash=True)  # extension handled automatically
        else:
            talk_directory = talk_class.from_path(self.talk_directory)
            talk_directory.write(export_path)
        self._write_config()
    # endregion

    # region Project Save Methods
    def save_all(self):
        for data_type in self.DATA_TYPES:
            if data_type in {ProjectDataType.Events, ProjectDataType.Talk}:
                continue  # saved externally by editor window
            save_func = getattr(self, f"save_{data_type.name}")
            save_func()

    def save_AI(self, specific_map=""):
        ai = self._get_data(ProjectDataType.AI)  # type: AIScriptDirectory
        if not ai:
            _LOGGER.warning("There is no AI data to save in this project.")
            return
        if specific_map:
            luabnd = ai[specific_map]
            luabnd.write_unpacked_directory(self.project_root / f"ai/{specific_map}")
        else:
            ai.write_unpacked_luabnds(self.project_root / "ai_scripts")
        self._write_config()

    # TODO: Save Enums.

    # `Events` data is saved from `EventsEditor` text to EVS scripts manually.

    def save_Lighting(self, specific_area=""):
        lighting = self._get_data(ProjectDataType.Lighting)  # type: DrawParamDirectory
        if not lighting:
            _LOGGER.warning("There is no Lighting data to save in this project.")
            return
        if specific_area:
            drawparambnd = lighting[specific_area]
            drawparambnd.write_json_directory(
                self.project_root / f"lighting/{specific_area}",
                ignore_pads=True,
                ignore_defaults=self.do_not_write_param_defaults)
        else:
            lighting.write_json_directory(
                self.project_root / "lighting", ignore_pads=True, ignore_defaults=self.do_not_write_param_defaults
            )
        self._write_config()

    def save_Maps(self, specific_map=""):
        maps = self._get_data(ProjectDataType.Maps)  # type: MapStudioDirectory
        if not maps:
            _LOGGER.warning("There is no Maps data to save in this project.")
            return
        if specific_map:
            msb = maps[specific_map]
            msb.write_json(self.project_root / f"maps/{specific_map}.json")
        else:
            maps.write_json_directory(self.project_root / "maps")
        self._write_config()

    def save_Params(self, specific_param=""):
        params = self._get_data(ProjectDataType.Params)  # type: GameParamBND
        if not params:
            _LOGGER.warning("There is no Params data to save in this project.")
            return
        if specific_param:
            param = params[specific_param]
            param.write_json(
                self.project_root / f"params/{specific_param}.json",
                ignore_pads=True,
                ignore_defaults=self.do_not_write_param_defaults)
        else:
            params.write_json_directory(
                self.project_root / "params", ignore_pads=True, ignore_defaults=self.do_not_write_param_defaults
            )
        self._write_config()

    def save_Text(self, specific_fmg=""):
        text = self._get_data(ProjectDataType.Text)  # type: MSGDirectory
        if not text:
            _LOGGER.warning("There is no Text data to save in this project.")
            return
        if specific_fmg:
            text[specific_fmg].write_json(self.project_root / f"text/{specific_fmg}.json")
        else:
            text.write_json_directory(self.project_root / "text")
        self._write_config()

    # `Talk` data is saved from `TalkEditor` text to ESP manually.
    # endregion

    # region Project Load Methods

    def load_AI(self) -> bool:
        ai_class = self.get_data_class(ProjectDataType.AI)  # type: tp.Type[AIScriptDirectory]
        ai_dir = self.project_root / "ai_scripts"
        if not ai_dir.is_dir():
            self._data[ProjectDataType.AI] = None  # no AI data (yet)
            return False
        try:
            self._data[ProjectDataType.AI] = ai_class.from_unpacked_luabnds(ai_dir)
            return True
        except Exception as ex:
            _LOGGER.error(ex)
            raise SoulstructProjectError(
                f"An error occurred while trying to load AI data from 'ai_scripts' directory:\n\n{ex}"
            )

    def load_Lighting(self) -> bool:
        lighting_class = self.get_data_class(ProjectDataType.Lighting)  # type: tp.Type[DrawParamDirectory]
        lighting_dir = self.project_root / "lighting"
        if not lighting_dir.is_dir():
            self._data[ProjectDataType.Lighting] = None  # no Lighting data (yet)
            return False
        try:
            self._data[ProjectDataType.Lighting] = lighting_class.from_json_directory(lighting_dir)
            return True
        except Exception as ex:
            _LOGGER.error(ex)
            raise SoulstructProjectError(
                f"An error occurred while trying to load Lighting data from 'lighting' directory:\n\n{ex}"
            )

    def load_Enums(self) -> bool:
        enums_class = self.get_data_class(ProjectDataType.Enums)  # type: tp.Type[GameEnumsManager]
        enums_dir = self.enums_directory
        if not enums_dir.is_dir():
            self._data[ProjectDataType.Enums] = None  # no Enums data (yet)
            return False

        if enums_dir.name == "events":  # must end in 'enums.py'
            module_paths = list(enums_dir.rglob("*_enums.py"))
        else:  # any Python modules can be used
            module_paths = list(enums_dir.rglob("*.py"))
        try:
            self._data[ProjectDataType.Enums] = enums_class(module_paths)
            return True
        except Exception as ex:
            _LOGGER.error(ex)
            raise SoulstructProjectError(
                f"An error occurred while trying to load Enums data from 'enums' directory:\n\n{ex}"
            )

    # `Events` EVS scripts are loaded by `EventsEditor` for text display.

    def load_Params(self) -> bool:
        params_class = self.get_data_class(ProjectDataType.Params)  # type: tp.Type[GameParamBND]
        params_dir = self.project_root / "params"
        if not params_dir.is_dir():
            self._data[ProjectDataType.Params] = None  # no Params data (yet)
            return False
        try:
            self._data[ProjectDataType.Params] = params_class.from_json_directory(params_dir)
            return True
        except Exception as ex:
            _LOGGER.error(ex)
            raise SoulstructProjectError(
                f"An error occurred while trying to load Params data from 'params' directory:\n\n{ex}"
            )

    def load_Maps(self) -> bool:
        maps_class = self.get_data_class(ProjectDataType.Maps)  # type: tp.Type[MapStudioDirectory]
        maps_dir = self.project_root / "maps"
        if not maps_dir.is_dir():
            self._data[ProjectDataType.Maps] = None
            return False
        try:
            self._data[ProjectDataType.Maps] = maps_class.from_json_directory(maps_dir)
            return True
        except Exception as ex:
            _LOGGER.error(ex)
            raise SoulstructProjectError(
                f"An error occurred while trying to load Maps data from 'maps' directory:\n\n{ex}"
            )

    def load_Text(self) -> bool:
        text_class = self.get_data_class(ProjectDataType.Text)  # type: tp.Type[MSGDirectory]
        text_dir = self.project_root / "text"
        if not text_dir.is_dir():
            self._data[ProjectDataType.Text] = None  # no Text data (yet)
            return False
        try:
            self._data[ProjectDataType.Text] = text_class.from_json_directory(text_dir)
            return True
        except Exception as ex:
            _LOGGER.error(ex)
            raise SoulstructProjectError(
                f"An error occurred while trying to load Text data from 'text' directory:\n\n{ex}"
            )

    # `Talk` ESP scripts are loaded by `TalkEditor` for text display.
    # endregion

    def get_data_type_import_settings(self, data_type: ProjectDataType) -> dict[str, tuple[str, bool, str]]:
        """Get dictionary of settings to show in Creator Wizard (or console).

        Returned dict maps each setting name to a `(display_label, default_setting)` tuple.
        """
        if data_type == ProjectDataType.Enums:
            return dict(
                put_enums_in_events_folder=(
                    "Put Enums in Events Folder", False,
                    "Write Python `{map_stem}_enums.py` modules to 'events' folder instead of 'enums' folder."
                ),
            )

        if data_type == ProjectDataType.Events:
            return dict(

                use_enums_in_event_scripts=(
                    "Use Enums in Event Scripts", True,
                    "Use variables from enums modules to replace game IDs (flags, entity IDs, etc.) in "
                    "decompiled EVS scripts.",
                ),
                copy_python_events_submodule=(
                    "Copy Python Events Submodule", False,
                    "Copy Soulstruct `events` game submodule to 'events' project folder so your Python IDE "
                    "can resolve the EVS module imports and apply intellisense when editing the EVS scripts."
                ),  # for IDE autocomplete
            )

        if data_type == ProjectDataType.Text:
            return dict(
                delete_empty_text_entries=(
                    "Delete Empty Text Entries", True,
                    "Delete all empty text entries. The games have many of these, but they don't do "
                    "anything except make the FMG files a tiny bit smaller (due to ID range compression)."
                ),
            )

        return {}

    def get_data_game_path(self, data_type: ProjectDataType, root=None) -> Path:
        game = self.get_game()
        root = self.game_root if root is None else Path(root)
        data_class_name = self.DATA_TYPES[data_type].__name__
        try:
            return root / game.default_file_paths[data_class_name]
        except KeyError:
            raise KeyError(f"Could not get data path to {data_type} ({data_class_name}) for game {game.name}")

    # region Process/Backup Utilities
    def export_timestamped_backup(self, data_type=None):
        """TODO: Not used anywhere at the moment."""
        timestamped_dir = self.project_root / "export" / self._get_timestamp(for_path=True)
        export_func = getattr(self, f"export_{data_type}")
        export_func(timestamped_dir)

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
            raise SoulstructProjectError(
                "Python package `psutil` required for this method. Install it with `python -m pip install psutil`."
            )

        game = self.get_game()

        if try_force_quit_first:
            self.force_quit_game()
        if not self._check_steam_appid_file(self.game_root):
            raise SoulstructProjectError(f"Soulstruct cannot create the 'steam_appid.txt' file for {game.name}")
        game_exe_path = self.game_root / game.executable_name

        if not game_exe_path.is_file():
            raise SoulstructProjectError(f"Could not find game executable: {str(game_exe_path)}")

        # noinspection PyUnresolvedReferences
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
        game = self.get_game()
        if not game.executable_name:
            raise SoulstructProjectError(f"Cannot force-quit {game.name} (don't know executable name).")
        os.system(f"TASKKILL /F /IM {game.executable_name}")

    def launch_gadget(self, threaded=True):
        if not psutil:
            raise ModuleNotFoundError(
                "Python package `psutil` required for this method. Install it with `python -m pip install psutil`."
            )

        game = self.get_game()
        if not game.gadget_name:
            raise SoulstructProjectError(f"No Gadget executable known for {game.name}.")
        gadget_path = self.game_root / game.gadget_name
        if not gadget_path.is_file():
            raise SoulstructProjectError(f"Could not find Gadget executable: {str(gadget_path)}")
        # noinspection PyUnresolvedReferences
        if gadget_path.name in (p.name() for p in psutil.process_iter()):
            _LOGGER.warning(f"Cannot launch Gadget: {gadget_path.name} is already running.")
            return
        if threaded:
            gadget_thread = threading.Thread(target=subprocess.run, args=(str(gadget_path),))
            gadget_thread.start()
        else:
            # Blocks Python (including window) until DS Gadget is closed.
            subprocess.run(str(gadget_path))

    def create_game_backup(self, backup_path=None):
        """Copy existing game files (that can be edited with Soulstruct) to a backup directory, which defaults to
        'soulstruct-backup' in your game directory. Use `restore_game_backup(backup_dir)` to restore those files."""
        game = self.get_game()
        if backup_path is None:
            backup_path = self.game_root / "soulstruct-backup"
        else:
            backup_path = Path(backup_path)
        game_files = read_json(PACKAGE_PATH("project/files.json"))[game.name]
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
        game = self.get_game()
        if backup_path is None:
            backup_path = self.game_root / "soulstruct-backup"
        game_files = read_json(PACKAGE_PATH("project/files.json"))[game.name]
        for file_path_parts in traverse_path_tree(game_files):
            backup_file_path = backup_path / Path(*file_path_parts)
            if not backup_file_path.is_file():
                raise FileNotFoundError(f"Could not find backup file to restore: " f"{str(backup_file_path)}")
            game_file_path = Path(self.game_root, *file_path_parts)
            game_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(backup_file_path), str(game_file_path))

    def load_existing_project(self, config_path: Path, new_game_root: Path | str = None) -> bool:

        game = self.get_game()
        rewrite_config = False

        try:
            config = read_json(config_path)
        except json.JSONDecodeError as ex:
            _LOGGER.error(ex)
            raise SoulstructProjectError(
                "Could not interpret 'project_config.json' file. Check it for errors, or delete it to have Soulstruct "
                "create a fresh one on next load. (See log for full JSON error.)"
            )

        if "GameName" not in config:
            raise SoulstructProjectError(
                "Project config JSON file does not contain required 'GameName' key. Delete the file and load the "
                "project directory again to create a fresh config JSON. (Your project files will not be affected.)"
            )
        elif game.name != config["GameName"]:
            raise SoulstructProjectError(
                f"Project config 'GameName' is {config['GameName']}, but `GameDirectoryProject` class belongs to "
                f"{game.name}. Fix this in the JSON or delete it and load the project directory again to choose the "
                f"right game."
            )

        if "GameDirectory" not in config:
            if new_game_root is None:
                raise SoulstructProjectError(
                    "Project config JSON file does not contain 'GameRoot' key and a new `game_root` argument was not "
                    "passed to the project. Provide this argument, or delete the JSON file and load the project "
                    "directory again to create a fresh config JSON. (Your project files will not be affected.)"
                )
            self.game_root = Path(new_game_root)
            rewrite_config = True
        else:
            config_game_root = config["GameDirectory"]
            if new_game_root is not None and new_game_root != config_game_root:
                self.game_root = Path(new_game_root)
                _LOGGER.info(
                    f"Previous project 'GameDirectory' {config_game_root} has been replaced with new "
                    f"directory: {self.game_root}"
                )
                rewrite_config = True
            else:
                self.game_root = Path(config_game_root)

        if not self._validate_game_directory(self.game_root):
            _LOGGER.warning(f"Project 'GameDirectory' {self.game_root} is not valid. (See log for details.)")
            return False

        last_save_version = config.get("LastSaveVersion", "unknown")
        self.last_import_time = config.get("LastImportTime", None)
        self.last_export_time = config.get("LastExportTime", None)

        # TODO: Project creator wizard could let user choose this. Or just from File menu.
        if vanilla_game_root := config.get("VanillaGameDirectory", ""):
            self._vanilla_game_root = Path(vanilla_game_root)

        if "PythonScriptDirectory" in config:
            self.python_script_directory = Path(config["PythonScriptDirectory"])
            if not self.python_script_directory.is_absolute():
                self.python_script_directory = self.project_root / self.python_script_directory
        else:
            self.python_script_directory = self.project_root / "python_scripts"
            rewrite_config = True
            _LOGGER.info("Default project setting: PythonScriptDirectory = \"python_scripts\"")

        if "TextEditorFontSize" in config:
            self.text_editor_font_size = config["TextEditorFontSize"]
        else:
            self.text_editor_font_size = DEFAULT_TEXT_EDITOR_FONT_SIZE
            _LOGGER.info(f"Default project setting: TextEditorFontSize = {DEFAULT_TEXT_EDITOR_FONT_SIZE}")
            rewrite_config = True

        if "EnumsInEventsFolder" in config:
            self.enums_in_events_folder = config["EnumsInEventsFolder"]
        else:
            # Try to auto-detect.
            if (self.project_root / "enums").is_dir():
                self.enums_in_events_folder = config["EnumsInEventsFolder"] = False
            events_dir = self.project_root / "events"
            if events_dir.is_dir() and list(events_dir.glob("*_enums.py")):
                self.enums_in_events_folder = config["EnumsInEventsFolder"] = True
            else:  # default
                self.enums_in_events_folder = config["EnumsInEventsFolder"] = False
            _LOGGER.info(f"Default project setting: EnumsInEventsFolder = {self.enums_in_events_folder}")
            rewrite_config = True

        if "DoNotWriteParamDefaults" in config:
            self.do_not_write_param_defaults = config["DoNotWriteParamDefaults"]
        else:
            self.do_not_write_param_defaults = True
            _LOGGER.info("Default project setting: DoNotWriteParamDefaults = True")
            rewrite_config = True

        self.other_settings = config.get("OtherSettings", {})

        if last_save_version.split(".")[0] != __version__.split(".")[0]:
            # Major version difference indicates potential project file incompatibility.
            _LOGGER.warning(
                f"Project was last saved with Soulstruct version {last_save_version}, which has a different major "
                f"version number to this version of Soulstruct ({__version__}). You may need to export your "
                f"project from the other version of Soulstruct and import those game files into this project."
            )

        # Load data.
        for data_type in self.DATA_TYPES:
            if data_type in {ProjectDataType.Enums, ProjectDataType.Events, ProjectDataType.Talk}:
                continue  # loaded by their own Editor classes (from plaintext project scripts/modules).

            load_func = getattr(self, f"load_{data_type.name}")
            load_func()  # no arguments for any load functions
            _LOGGER.info(f"Loaded {data_type.name} data from project.")

        if rewrite_config:
            self._write_config()
        return True
    # endregion

    def create_new_project(self, with_window: ProjectWindow = None, game_root: Path | str = None) -> bool:
        """Load config JSON from project, or create it if missing.

        Returns two bools: `first_time` (if project JSON was created) and `force_import_from_game` (if the user
        accepted the offer to import all game data immediately).
        """
        if game_root:
            self.game_root = Path(game_root)
        else:
            try:
                self.game_root = self._get_game_root(with_window=with_window)
            except SoulstructProjectError as ex:
                raise SoulstructProjectError(str(ex) + "\n\nAborting project setup.")
            if self.game_root is None:
                return False  # abort peacefully

        if not self._validate_game_directory(self.game_root):
            return False

        if not with_window:
            # Console project import settings are very limited.
            result = input(
                "Import game files now? This will override any project files that are already in this folder. [y]/n"
            )
            result = 1 if result.lower() == "n" else 0
            if result == 0:
                for data_type in self.DATA_TYPES:
                    import_func = getattr(self, f"import_{data_type.name}")
                    import_func(import_directory=self.game_root)  # TODO: no options supported here!
                    # NOTE: Enums, Events, and Talk data are 'saved' implicitly on import (plaintext scripts written).
                    if data_type not in {ProjectDataType.Enums, ProjectDataType.Events, ProjectDataType.Talk}:
                        save_func = getattr(self, f"save_{data_type.name}")
                        save_func()
            self._write_config()
            return True

        data_type_settings = {}
        for data_type in self.DATA_TYPES:
            data_type_settings[data_type] = self.get_data_type_import_settings(data_type)

        import_settings = with_window.run_creator_wizard(
            self.get_game().name, list(self.DATA_TYPES), data_type_settings
        )
        if not import_settings:
            return False  # abort peacefully

        for data_type in self.DATA_TYPES:
            if data_type not in import_settings.import_data_types:
                # Data not imported. Tab will not appear. Can be imported later from GUI menu.
                setattr(self, data_type.value, None)
                continue
            # NOTE: It's up to each `import` function signature to match settings names properly.
            import_func = getattr(self, f"import_{data_type.name}")
            import_func(import_directory=self.game_root, **import_settings.data_type_settings[data_type])
            # NOTE: Enums, Events, and Talk data are 'saved' implicitly on import (plaintext scripts written).
            if data_type not in {ProjectDataType.Enums, ProjectDataType.Events, ProjectDataType.Talk}:
                save_func = getattr(self, f"save_{data_type.name}")
                save_func()

        self.python_script_directory = self.project_root / "python_scripts"

        self._write_config()
        return True

    def copy_events_submodule(self, with_window: ProjectWindow = None):
        name = self.get_game().submodule_name
        events_submodule = PACKAGE_PATH(f"{name}/events")
        if (self.events_directory / "soulstruct").is_dir():
            self.error(
                "'events/soulstruct' folder already exists. Cannot copy Python submodule over. "
                "Delete it and try again from the top menu.",
                with_window,
            )
            return
        (self.events_directory / f"soulstruct/{name}").mkdir(parents=True, exist_ok=True)
        shutil.copytree(events_submodule, self.events_directory / f"soulstruct/{name}/events")
        _LOGGER.info(f"Copied `soulstruct.{name}.events` submodule into project events folder.")

    def run_python_script(self, script_path: Path, stdout=None, stderr=None) -> subprocess.CompletedProcess:
        """Run given `script_path` Python script in a subprocess and wait for it to return.

        If the given path is relative, it will be resolved relative to `self.python_script_directory`, which in turn
        defaults to `{project_root}/python_scripts` and can be edited in the project JSON config.
        """
        script_path = Path(script_path)
        if not script_path.is_absolute():
            script_path = (self.python_script_directory / script_path).absolute()
        return subprocess.run(
            [sys.executable, script_path],
            text=True,
            stdout=stdout,
            stderr=stderr,
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )

    @classmethod
    def get_game(cls) -> Game:
        if match := re.match(_GAME_MODULE_RE, cls.__module__):
            return get_game(match.group(1))
        raise ValueError(f"Could not detect game name from module of class `{cls.__name__}`: {cls.__module__}")

    # region Private Methods

    @staticmethod
    def _get_timestamp(for_path=False):
        return datetime.datetime.now().strftime("%Y-%m-%d %H%M%S" if for_path else "%Y-%m-%d %H:%M:%S")

    def _build_config_dict(self):
        # TODO: Data-specific 'last' times.
        return {
            "LastSaveVersion": __version__,
            "GameName": self.get_game().name,
            "GameDirectory": str(self.game_root),
            "LastImportTime": self.last_import_time,
            "LastExportTime": self.last_export_time,
            "VanillaGameDirectory": str(self._vanilla_game_root) if self._vanilla_game_root else None,
            "PythonScriptDirectory": str(self.python_script_directory),
            "TextEditorFontSize": DEFAULT_TEXT_EDITOR_FONT_SIZE,
            "EnumsInEventsFolder": self.enums_in_events_folder,
            "DoNotWriteParamDefaults": self.do_not_write_param_defaults,
            "OtherSettings": self.other_settings,
        }

    def _write_config(self):
        try:
            write_json(self.project_root / "project_config.json", self._build_config_dict())
        except PermissionError:
            raise SoulstructProjectError("No write access to 'project_config.json' in project directory.")

    @staticmethod
    def _validate_project_directory(project_path: Path, default_root: Path) -> Path:
        if not project_path.is_absolute():
            project_path = (default_root / project_path).expanduser().absolute()
        if project_path.is_file():
            raise SoulstructProjectError("You must specify a project *directory*, not a file.")
        if not project_path.is_dir():
            try:
                project_path.mkdir(parents=True, exist_ok=True)
            except NotADirectoryError:
                raise SoulstructProjectError(f"Invalid directory path: {str(project_path)}")
            except PermissionError:
                raise SoulstructProjectError(f"No write access to create directory: {str(project_path)}")

        return project_path

    @staticmethod
    def _validate_game_directory(game_root: Path) -> bool:
        """Optional method that can be overridden to validate `game_root` when it is set/loaded."""
        return True

    def _get_game_root(self, with_window: ProjectWindow = None) -> Path | None:
        """Interactively select game directory for project. Returns `None` if no directory chosen."""
        game = self.get_game()
        initial_dir = game.default_game_path if Path(game.default_game_path).is_dir() else None

        if with_window:
            with_window.CustomDialog(
                title="Select game directory for project",
                message=None,
                custom_dialog_subclass=GameRootDialog,
                game=game,
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
            steam_appid = self.get_game().steam_appid
            if steam_appid:
                with steam_appid_path.open("w") as f:
                    f.write(str(steam_appid))
                return True
            return False
        return True

    @staticmethod
    def warning(msg, with_window: ProjectWindow = None, dialog_title="Soulstruct Warning"):
        _LOGGER.warning(msg)
        if with_window:
            with_window.CustomDialog(dialog_title, msg)

    @staticmethod
    def error(msg, with_window: ProjectWindow = None, dialog_title="Soulstruct Error"):
        _LOGGER.error(msg)
        if with_window:
            with_window.CustomDialog(dialog_title, msg)

    # endregion


class GameRootDialog(CustomDialog):

    def __init__(self, *args, game: Game = None, **kwargs):
        self.game_name = game.name
        self.generic_game_path = game.generic_game_path
        super().__init__(*args, **kwargs)

    def build(self, message, font, button_names, button_kwargs):
        with self.set_master(auto_rows=0, padx=20, pady=20):
            if self.generic_game_path:
                self.Label(
                    text=f"Navigate to your {self.game_name} installation directory for initial import.\n"
                    "In a standard Steam installation, this will be:",
                    pady=10,
                )
                self.Label(
                    text=self.generic_game_path,
                    font=("Consolas", 8),
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
