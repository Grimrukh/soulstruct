from __future__ import annotations

__all__ = ["TalkESDBND"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.containers import Binder, BinderEntry

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryReader
    from .esd import ESD

_LOGGER = logging.getLogger(__name__)

_TALK_ESD_RE = re.compile(r"t(\d+)\.esd$")
_TALK_ESP_RE = re.compile(r"t(\d+)\.esp(\.py)$")


@dataclass(slots=True)
class TalkESDBND(Binder, abc.ABC):
    """Automatically loads all talk ESDs contained inside given path, or constructs BND from scratch using dictionary
    mapping talk IDs to valid ESD instance sources."""

    EXT: tp.ClassVar[str] = ".talkesdbnd"

    TALK_ESD_CLASS: tp.ClassVar[tp.Type[ESD]] = None
    BND_ROOT: tp.ClassVar[str] = None  # used for creating a new BND if instance is loaded from individual ESD/ESP file

    talk: dict[int, ESD] = field(default_factory=dict)

    def _handle_other_source_types(self, file_source, **kwargs):
        if isinstance(file_source, Path) and file_source.is_dir() and not (file_source / "bnd_manifest.json").exists():
            # Directory of individual ESP files/folders.
            self.set_default_bnd()
            self.path = file_source.with_suffix(self.EXT)
            self.reload_all_esp(file_source, allow_new=True)
            self.update_entries()
            return
        elif isinstance(file_source, dict):
            # Note that `path` cannot be detected and must be passed to `write()` manually.
            self.path = None
            self.set_default_bnd()
            self.unpack_from_dict(file_source)
            return
        raise InvalidGameFileTypeError(f"`talkesdbnd_source` was not a folder of ESP files or a dictionary of `ESD`s.")

    @abc.abstractmethod
    def set_default_bnd(self):
        """Set BND attributes for loading `TalkESDBND` from a single ESP file or folder containing them."""

    # TODO: to __post_init__
    def unpack(self, reader: BinaryReader, **kwargs):
        self.talk = {}

        super().unpack(reader, **kwargs)

        for entry in self.entries:
            entry_path = Path(entry.path)
            if esd_file_match := _TALK_ESD_RE.match(entry_path.name):
                talk_id = int(esd_file_match.group(1))
                try:
                    self.talk[talk_id] = self.TALK_ESD_CLASS(entry.get_uncompressed_data())
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
                BinderEntry(
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
                self.entries_by_path[entry_path].set_uncompressed_data(talk_entry.pack())
            else:
                new_id = max([entry.entry_id for entry in self.entries]) + 1 if self.entries else 1
                new_entry = BinderEntry(data=talk_entry.pack(), entry_id=new_id, path=entry_path)
                self.add_entry(new_entry)
                _LOGGER.debug(f"New ESD entry added to TalkESDBND (ID {new_id}): t{talk_id}.esd")

    def write(
        self,
        file_path: None | str | Path = None,
        make_dirs=True,
        check_hash=False,
        skip_update=False,
        **pack_kwargs,
    ):
        """Update BND entries from current `ESD` instances before packing/writing BND."""
        if not skip_update:
            self.update_entries()
        super().write(file_path, make_dirs=make_dirs, check_hash=check_hash)

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
