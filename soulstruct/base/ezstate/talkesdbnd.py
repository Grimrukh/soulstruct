from __future__ import annotations

__all__ = ["TalkESDBND"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.containers import Binder, BinderEntry

try:
    Self = tp.Self
except AttributeError:
    Self = "TalkESDBND"

if tp.TYPE_CHECKING:
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

    talk: dict[int, ESD] = field(default_factory=dict)

    def __post_init__(self):
        if not self.talk and self.entries:
            return

        # Load from binary Binder source.
        for entry in self.entries:
            if not (match := _TALK_ESD_RE.match(entry.name)):
                _LOGGER.warning(f"Ignoring unknown entry '{entry.name}' in TalkESDBND Binder.")
                continue
            talk_id = match.group(1)
            try:
                self.talk[talk_id] = entry.to_game_file(self.TALK_ESD_CLASS)
            except Exception as ex:
                _LOGGER.error(f"Could not load talk ESD 't{talk_id}' from TalkESDBND entry '{entry.name}'. Error: {ex}")
                raise

    def get_default_entry_id(self, entry_name: str) -> int:
        return self.get_first_new_entry_id_in_range(0, 1000000)

    @classmethod
    def from_esp_directory(cls, esp_directory: str | Path) -> Self:
        """Load from directory of individual ESP files/folders."""
        talkesdbnd = cls()  # type: Self
        talkesdbnd.path = esp_directory.with_suffix(cls.EXT)
        talkesdbnd.reload_all_esp(esp_directory, allow_new=True)
        talkesdbnd.regenerate_entries()
        return talkesdbnd

    @classmethod
    def from_talk_dict(cls, talk_dict: dict[int, ESD]) -> Self:
        talkesdbnd = cls()  # type: Self
        talkesdbnd.talk = talk_dict.copy()
        talkesdbnd.regenerate_entries()
        return talkesdbnd

    def write_esp(self, esp_directory: Path | str):
        esp_directory = Path(esp_directory)
        esp_directory.mkdir(parents=True, exist_ok=True)
        for talk_id, talk_esd in self.talk.items():
            talk_esd.write_esp(esp_directory / f"t{talk_id}.esp")

    def reload_all_esp(self, esp_directory: Path | str, allow_new=True):
        """Read ESP files in `esp_directory` into `talk`.

        If `allow_new=False`, only existing keys in `talk` will be reloaded from found files.
        """
        for esp_path in Path(esp_directory).glob("*.esp*"):
            talk_match = _TALK_ESP_RE.match(esp_path.name)
            if talk_match:
                talk_id = int(talk_match.group(1))
                if not allow_new and talk_id not in self.talk:
                    _LOGGER.warning(
                        f"# WARNING: `allow_new=False` and no talk ID found for ESP file: {esp_path.name}. "
                        f"Ignoring it."
                    )
                    continue
                try:
                    self.talk[talk_id] = esd = self.TALK_ESD_CLASS.from_path(esp_path)
                except Exception as e:
                    _LOGGER.error(f"Could not load talk ESD 't{talk_id}' from ESP file {esp_path.name}. Error: {e}")
                    raise
                else:
                    # Update/create this Binder entry rather than blindly regenerating all of them.
                    entry_path = self.get_default_entry_path(f"t{talk_id}.esd")
                    if entry_path in self.entries_by_path:
                        # Just update data.
                        self.entries_by_path[entry_path].set_from_game_file(esd)
                    else:
                        # Add new entry.
                        new_id = self.get_default_entry_id(entry_path)
                        new_entry = BinderEntry(data=bytes(esd), entry_id=new_id, path=entry_path)
                        self.add_entry(new_entry)
                        _LOGGER.debug(f"New ESD entry from ESP file {esp_path.name} added to TalkESDBND (ID {new_id}).")

    def regenerate_entries(self):
        """Regenerate Binder entries from `talk` dictionary."""

        # Remove BND talk entries that aren't still present in this `TalkESDBND` instance.
        current_entry_names = [f"{talk_id}.esd" for talk_id in self.talk]
        for entry_name in [entry.name for entry in self.entries]:
            if entry_name not in current_entry_names:
                self.remove_entry_name(entry_name)

        for talk_entry_name, talk_esd in zip(current_entry_names, self.talk.values(), strict=True):
            entry_path = self.get_default_entry_path(talk_entry_name)
            if entry_path in self.entries_by_path:
                # Just update data.
                self.entries_by_path[entry_path].set_from_game_file(talk_esd)
            else:
                # Add new entry.
                new_id = self.get_default_entry_id(talk_entry_name)
                new_entry = BinderEntry(data=bytes(talk_esd), entry_id=new_id, path=entry_path)
                self.add_entry(new_entry)
                _LOGGER.debug(f"New ESD entry added to TalkESDBND (ID {new_id}): {talk_entry_name}")

    def __getitem__(self, talk_id):
        return self.talk[talk_id]

    def __iter__(self):
        return iter(self.talk)

    def __repr__(self):
        return f"TalkESDBND({repr(self.path)}): {list(self.talk)}"

    def write(
        self,
        file_path: None | str | Path = None,
        bdt_file_path: None | str | Path = None,
        make_dirs=True,
        check_hash=False,
    ):
        if bdt_file_path is not None:
            raise TypeError(
                f"Cannot write `TalkESDBND` to a split `BXF` file. (Invalid `bdt_file_path`: {bdt_file_path})"
            )
        self.regenerate_entries()
        super(TalkESDBND, self).write(file_path, make_dirs=make_dirs, check_hash=check_hash)

    @classmethod
    def write_from_dict(cls, talk_dict, talkesdbnd_path, make_dirs=True):
        """Shortcut to immediately load given dictionary and write to given `.talkesdbnd` path."""
        talkesdbnd = cls.from_talk_dict(talk_dict)  # type: Self
        # Skip regeneneration in this class's `write`.
        Binder.write(talkesdbnd, talkesdbnd_path, make_dirs=make_dirs)
