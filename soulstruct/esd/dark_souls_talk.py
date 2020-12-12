import logging
import pickle
import re
from collections import OrderedDict
from pathlib import Path

from soulstruct.bnd import BND, BNDEntry, BaseBND
from soulstruct.maps.darksouls1.maps import ALL_MAPS
from soulstruct.esd.ds1ptde import ESD as ESD_PTDE
from soulstruct.esd.ds1r import ESD as ESD_DSR
from soulstruct.utilities import PACKAGE_PATH

__all__ = ["DarkSoulsTalk", "TalkESDBND"]
_LOGGER = logging.getLogger(__name__)

_TALK_ESD_RE = re.compile(r"t(\d+)\.esd$")
_TALK_ESP_RE = re.compile(r"t(\d+)\.esp(\.py)$")


class TalkESDBND:
    """Automatically loads all talk ESDs contained inside given path, or constructs BND from scratch using dictionary
    mapping talk IDs to valid ESD instance sources.

    By default, game version is automatically detected using BND paths.

    Currently only supported for DS1, hence its placement in this module.
    """

    DSR_DCX_MAGIC = (36, 44)
    DS1_BND_PATH_FMT = "N:\\FRPG\\data\\INTERROOT_{version}\\script\\talk\\t{talk_id}.esd"

    bnd: BaseBND

    def __init__(self, talkesdbnd_source, game_version=None):
        if game_version not in (None, "ptde", "dsr"):
            raise ValueError(f"`game_version` should be 'ptde', 'dsr', or None (to auto-detect), not {game_version}.")
        if game_version:
            self.esd_class = ESD_DSR if game_version == "dsr" else ESD_PTDE

        self.talk = OrderedDict()
        self.game_version = game_version

        if isinstance(talkesdbnd_source, (str, Path)):
            if talkesdbnd_source.is_file():
                # Single `.talkesdbnd` files. Game version can be detected automatically in this case.
                self.bnd = BND(talkesdbnd_source)  # path is remembered in BND
                self.bnd_name = Path(talkesdbnd_source).name
                self.unpack_from_bnd()
            elif talkesdbnd_source.is_dir():
                # Directory of individual ESP files/folders.
                self.bnd_name = "<from ESP>"
                if not self.game_version:
                    raise ValueError(
                        "`game_version` must be specified ('ptde' or 'dsr') when loading TalkESDBND from "
                        "ESP files/folders."
                    )
                self.bnd = self.get_empty_talkesdbnd()
                self.bnd_name = talkesdbnd_source.name
                self.bnd.dcx = self.DSR_DCX_MAGIC if self.game_version == "dsr" else ()
                self.reload_all_esp(talkesdbnd_source, allow_new=True)
                self.update_bnd()

        elif isinstance(talkesdbnd_source, dict):
            # Note that `bnd_name` cannot be detected and must be passed to `write()` manually.
            self.bnd_name = "<from dict>"
            if not self.game_version:
                raise ValueError(
                    "`game_version` must be specified ('ptde' or 'dsr') when loading TalkESDBND from " "dictionary."
                )
            self.bnd = self.get_empty_talkesdbnd()
            self.bnd.dcx = self.DSR_DCX_MAGIC if self.game_version == "dsr" else ()
            self.unpack_from_dict(talkesdbnd_source)

    def unpack_from_bnd(self):
        self.talk = OrderedDict()
        for entry in self.bnd:
            entry_path = Path(entry.path)
            if self.game_version is None:
                if "INTERROOT_x64" in entry.path:
                    self.game_version = "dsr"
                elif "INTERROOT_win32" in entry.path:
                    self.game_version = "ptde"
                else:
                    raise ValueError(f"Could not detect DS1 version from path: {entry.path}")
                self.esd_class = ESD_DSR if self.game_version == "dsr" else ESD_PTDE
            talk_match = _TALK_ESD_RE.match(entry_path.name)
            if talk_match:
                talk_id = int(talk_match.group(1))
                try:
                    self.talk[talk_id] = self.esd_class(entry.data, "talk")
                except Exception as e:
                    _LOGGER.error(f"Encountered error when trying to load talk ESD {talk_id}: {e}")
                    raise
            else:
                _LOGGER.warning(f"Unexpected file in TalkESDBND: {entry_path.name}")

    def unpack_from_dict(self, talk_dict):
        i = 1
        for talk_id, esd_source in talk_dict.items():
            if not isinstance(talk_id, int):
                raise ValueError("Keys of `talkesdbnd_source` dict must be integer talk IDs.")
            try:
                esd = self.esd_class(esd_source)
            except Exception as e:
                _LOGGER.error(f"Could not interpret ESD source with talk ID {talk_id}. Error: {str(e)}")
                raise
            bnd_path = self.DS1_BND_PATH_FMT.format(
                version="x64" if self.game_version == "dsr" else "win32", talk_id=talk_id
            )
            self.talk[talk_id] = esd
            self.bnd.add_entry(BNDEntry(data=esd.pack(), entry_id=i, path=bnd_path))
            i += 1

    def __getitem__(self, talk_id):
        return self.talk[talk_id]

    def __iter__(self):
        return iter(self.talk)

    def __repr__(self):
        return f"TalkESDBND({repr(self.bnd_name)}): {list(self.talk)}"

    def write_all_esp(self, directory):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        for talk_id, talk_esd in self.talk.items():
            talk_esd.write_esp(directory / f"t{talk_id}.esp")

    def reload_all_esp(self, directory, allow_new=True):
        directory = Path(directory)
        for esp_source in directory.glob("*.esp*"):
            talk_match = _TALK_ESP_RE.match(esp_source.name)
            if talk_match:
                talk_id = int(talk_match.group(1))
                if not allow_new and talk_id not in self.talk:
                    _LOGGER.warning(
                        f"# WARNING: `allow_new=False` and no talk ID found for ESP source: {esp_source.name}. "
                        f"Ignoring it."
                    )
                    continue
                try:
                    self.talk[talk_id] = self.esd_class(esp_source)
                except Exception as e:
                    _LOGGER.error(f"Could not load talk ESD 't{talk_id}' from ESP source {esp_source.name}. Error: {e}")
                    raise

    def update_bnd(self):
        for talk_id, talk_entry in self.talk.items():
            bnd_path = self.DS1_BND_PATH_FMT.format(
                version="x64" if self.game_version == "dsr" else "win32", talk_id=talk_id
            )
            if bnd_path in self.bnd.entries_by_path:
                self.bnd.entries_by_path[bnd_path].data = talk_entry.pack()
            else:
                new_id = max([entry.id for entry in self.bnd.entries]) + 1 if self.bnd.entries else 1
                new_entry = BNDEntry(data=talk_entry.pack(), entry_id=new_id, path=bnd_path)
                self.bnd.add_entry(new_entry)
                _LOGGER.debug(f"New ESD entry added to TalkESDBND: t{talk_id}.esd")

    def write(self, talkesdbnd_path=None):
        self.update_bnd()
        self.bnd.write(talkesdbnd_path)

    @classmethod
    def write_from_dict(cls, talk_dict, game_version, talkesdbnd_path):
        """Shortcut to immediately load given dictionary and write to given path without pointless BND update."""
        talkesdbnd = cls(talk_dict, game_version=game_version)
        talkesdbnd.bnd.write(talkesdbnd_path)

    @staticmethod
    def get_empty_talkesdbnd():
        """Get empty pickled `.talkesdbnd` file for Dark Souls 1 (either version)."""
        with PACKAGE_PATH("project/resources/empty_talkesdbnd.ds1").open("rb") as f:
            return pickle.load(f)


class DarkSoulsTalk:
    """Not actually used by SoulstructProject, but could still be useful for CLI editing."""

    Depths: TalkESDBND
    UndeadBurg: TalkESDBND  # and Undead Parish
    FirelinkShrine: TalkESDBND
    PaintedWorld: TalkESDBND
    DarkrootGarden: TalkESDBND  # and Darkroot Basin
    Oolacile: TalkESDBND  # and all DLC
    Catacombs: TalkESDBND
    TombOfTheGiants: TalkESDBND
    AshLake: TalkESDBND  # and Great Hollow
    Blighttown: TalkESDBND
    LostIzalith: TalkESDBND  # and Demon Ruins
    SensFortress: TalkESDBND
    AnorLondo: TalkESDBND
    NewLondoRuins: TalkESDBND  # and Valley of Drakes
    DukesArchives: TalkESDBND
    KilnOfTheFirstFlame: TalkESDBND
    UndeadAsylum: TalkESDBND

    def __init__(self, talk_directory=None):
        """Unpack Dark Souls talk ESD state machines into one single modifiable structure.

        Args:
            talk_directory: Directory where all the `.talkesbnd[.dcx]` files are stored. This will be inside
                'script/talk' in your game directory (either version).
        """
        self._directory = None
        self._data = {}

        if talk_directory is None:
            return
        self._directory = Path(talk_directory)
        if not self._directory.is_dir():
            raise ValueError("DarkSoulsTalk should be initialized with the directory containing TalkESDBND files.")

        for game_map in ALL_MAPS:
            talkesdbnd_path = self._directory / (game_map.esd_file_stem + ".talkesdbnd")
            try:
                self._data[game_map.name] = TalkESDBND(talkesdbnd_path)
                setattr(self, game_map.name, self._data[game_map.name])
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Could not find TalkESDBND file {repr(game_map.esd_file_stem)} "
                    f"({game_map.name}) in given directory."
                )

    def __getitem__(self, talkesdbnd_name):
        return self._data[talkesdbnd_name]

    def __repr__(self):
        return f"DarkSoulsTalk({repr(str(self._directory))})"

    def save(self, talk_directory=None):
        if talk_directory is None:
            talk_directory = self._directory
        talk_directory = Path(talk_directory)
        for talkesdbnd in self._data.values():
            talkesdbnd_path = talk_directory / talkesdbnd.bnd.bnd_path.name
            talkesdbnd.write(talkesdbnd_path)
        _LOGGER.info("Dark Souls talk ESD files (TalkESDBND) written successfully.")
