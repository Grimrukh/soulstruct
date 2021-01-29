from __future__ import annotations

__all__ = ["TalkESDBND", "TalkDirectory"]

import abc
import logging
import re
import typing as tp
from pathlib import Path

from soulstruct.bnd import BNDEntry, BaseBND
from soulstruct.game_file import InvalidGameFileTypeError

if tp.TYPE_CHECKING:
    from soulstruct.game_types import Map
    from .esd import ESD

_LOGGER = logging.getLogger(__name__)

_TALK_ESD_RE = re.compile(r"t(\d+)\.esd$")
_TALK_ESP_RE = re.compile(r"t(\d+)\.esp(\.py)$")


class TalkESDBND(BaseBND, abc.ABC):
    """Automatically loads all talk ESDs contained inside given path, or constructs BND from scratch using dictionary
    mapping talk IDs to valid ESD instance sources."""

    EXT = ".talkesdbnd"
    TALK_ESD_CLASS: tp.Type[ESD] = None
    BND_ROOT: str = None  # used for creating a new BND if instance is loaded from individual ESD/ESP file

    talk: dict[int, ESD]

    def __init__(self, talkesdbnd_source, dcx_magic=()):
        self.talk = {}
        super().__init__(talkesdbnd_source, dcx_magic=dcx_magic)

    def _handle_other_source_types(self, file_source, **kwargs):
        if isinstance(file_source, Path) and file_source.is_dir() and not (file_source / "bnd_manifest.json").exists():
            # Directory of individual ESP files/folders.
            self.set_default_bnd()
            self.path = file_source.name  # directory name
            self.reload_all_esp(file_source, allow_new=True)
            self.update_entries()
            return
        elif isinstance(file_source, dict):
            # Note that `path` cannot be detected and must be passed to `write()` manually.
            self.path = None
            self.set_default_bnd()
            self.unpack_from_dict(file_source)
            self.create_header_structs()
            return
        raise InvalidGameFileTypeError(f"`talkesdbnd_source` was not a folder of ESP files or a dictionary of `ESD`s.")

    @abc.abstractmethod
    def set_default_bnd(self):
        """Set BND attributes for loading `TalkESDBND` from an ESP file or folder thereof."""

    def unpack(self, buffer, **kwargs):
        self.talk = {}

        super().unpack(buffer, **kwargs)

        for entry in self.entries:
            entry_path = Path(entry.path)
            if esd_file_match := _TALK_ESD_RE.match(entry_path.name):
                talk_id = int(esd_file_match.group(1))
                try:
                    self.talk[talk_id] = self.TALK_ESD_CLASS(entry.data)
                except Exception as e:
                    _LOGGER.error(f"Encountered error when trying to load talk ESD {talk_id}: {e}")
                    raise
            else:
                _LOGGER.warning(f"Unexpected file in `TalkESDBND`: {entry_path.name}")

    def unpack_from_dict(self, talk_dict):
        for i, (talk_id, esd_source) in enumerate(talk_dict.items()):
            if not isinstance(talk_id, int):
                raise ValueError("Keys of `talkesdbnd_source` dict must be integer talk IDs.")
            try:
                esd = self.TALK_ESD_CLASS(esd_source)
            except Exception as e:
                _LOGGER.error(f"Could not interpret ESD source with talk ID {talk_id}. Error: {str(e)}")
                raise
            self.talk[talk_id] = esd
            self.add_entry(
                BNDEntry(
                    data=esd.pack(),
                    entry_id=i + 1,  # BND entry index starts at 1
                    path=f"{self.BND_ROOT}\\t{talk_id}.esd",
                )
            )

    def write_esp(self, talk_directory):
        talk_directory = Path(talk_directory)
        talk_directory.mkdir(parents=True, exist_ok=True)
        for talk_id, talk_esd in self.talk.items():
            talk_esd.write_esp(talk_directory / f"t{talk_id}.esp")

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
                    self.talk[talk_id] = self.TALK_ESD_CLASS(esp_source)
                except Exception as e:
                    _LOGGER.error(f"Could not load talk ESD 't{talk_id}' from ESP source {esp_source.name}. Error: {e}")
                    raise

    def update_entries(self):
        for talk_id, talk_entry in self.talk.items():
            entry_path = f"{self.BND_ROOT}\\t{talk_id}.esd"
            if entry_path in self.entries_by_path:
                self.entries_by_path[entry_path].data = talk_entry.pack()
            else:
                new_id = max([entry.id for entry in self.entries]) + 1 if self.entries else 1
                new_entry = BNDEntry(data=talk_entry.pack(), entry_id=new_id, path=entry_path)
                self.add_entry(new_entry)
                _LOGGER.debug(f"New ESD entry added to TalkESDBND: t{talk_id}.esd")

    def write(self, file_path: tp.Union[None, str, Path] = None, make_dirs=True, skip_update=False, **pack_kwargs):
        """Update BND entries from current `ESD` instances before packing/writing BND."""
        if not skip_update:
            self.update_entries()
        super().write(file_path, make_dirs)

    def __getitem__(self, talk_id):
        return self.talk[talk_id]

    def __iter__(self):
        return iter(self.talk)

    def __repr__(self):
        return f"TalkESDBND({repr(self.path)}): {list(self.talk)}"

    @classmethod
    def write_from_dict(cls, talk_dict, talkesdbnd_path, make_dirs=True):
        """Shortcut to immediately load given dictionary and write to given path."""
        talkesdbnd = cls(talk_dict)
        talkesdbnd.write(talkesdbnd_path, make_dirs=make_dirs, skip_update=True)


class TalkDirectory(abc.ABC):
    """Not actually used by `GameDirectoryProject`, but could still be useful for CLI editing."""

    ALL_MAPS: tuple[Map] = None
    GET_MAP: tp.Callable = None
    IS_DCX: bool = None
    TALKESDBND_CLASS: tp.Type[TalkESDBND] = None

    def __init__(self, talk_directory=None):
        """Unpack all talk ESD state machines into one single modifiable structure.

        Args:
            talk_directory: Directory where all the `.talkesbnd[.dcx]` files are stored. This will be inside
                'script/talk' in your game directory.
        """
        self._directory = None
        self.bnds = {}  # type: dict[str, TalkESDBND]

        if talk_directory is None:
            return
        self._directory = Path(talk_directory)
        if not self._directory.is_dir():
            raise ValueError("`TalkDirectory` should be initialized with the directory containing '.talkesdbnd' files.")
        self.load()

    def __getitem__(self, map_name):
        return self.bnds[map_name]

    def __repr__(self):
        return f"TalkDirectory({repr(str(self._directory))})"

    def write(self, talk_directory=None):
        if talk_directory is None:
            talk_directory = self._directory
        talk_directory = Path(talk_directory)
        for talkesdbnd in self.bnds.values():
            talkesdbnd.write(talk_directory / talkesdbnd.path.name)
        _LOGGER.info("All TalkESDBND files (TalkESDBND) written successfully.")

    def write_esp(self, talk_directory=None):
        if talk_directory is None:
            talk_directory = self._directory
        talk_directory = Path(talk_directory)
        for game_map in [m for m in self.ALL_MAPS if m.esd_file_stem]:
            talkesdbnd = self.bnds[game_map.name]
            talkesdbnd.write_esp(talk_directory=talk_directory / f"{game_map.esd_file_stem}")

    def load(self, talk_directory=None):
        if talk_directory is None:
            talk_directory = self._directory
        talk_directory = Path(talk_directory)
        if self._directory is None:
            self._directory = talk_directory
        for game_map in [m for m in self.ALL_MAPS if m.esd_file_stem]:
            talkesdbnd_path = talk_directory / f"{game_map.esd_file_stem}.talkesdbnd{'.dcx' if self.IS_DCX else ''}"
            try:
                self.bnds[game_map.name] = self.TALKESDBND_CLASS(talkesdbnd_path)
                setattr(self, game_map.name, self.bnds[game_map.name])
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Could not find TalkESDBND file {talkesdbnd_path} ({game_map.name}) in given directory."
                )
