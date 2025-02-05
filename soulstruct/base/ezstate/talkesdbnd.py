from __future__ import annotations

__all__ = ["TalkESDBND"]

import abc
import logging
import re
import typing as tp
from dataclasses import field
from pathlib import Path

from soulstruct.containers import Binder
from .esd import ESD

_LOGGER = logging.getLogger("soulstruct")

_TALK_RE = re.compile(r"t(\d+)")
_TALK_ESD_RE = re.compile(r"t(\d+)\.esd$")
_TALK_ESP_RE = re.compile(r"t(\d+)\.esp(\.py)$")


TALK_ESD_T = tp.TypeVar("TALK_ESD_T", bound=ESD)


class TalkESDBND(Binder, tp.Generic[TALK_ESD_T], abc.ABC):
    """Automatically loads all talk ESDs contained inside given path, or constructs BND from scratch using dictionary
    mapping talk IDs to valid ESD instance sources.

    TODO: Lazy loading.
    """

    EXT: tp.ClassVar[str] = ".talkesdbnd"
    IS_SPLIT_BXF: tp.ClassVar[bool] = False

    TALK_ESD_CLASS: tp.ClassVar[type[ESD]] = None

    talk: dict[int, TALK_ESD_T] = field(default_factory=dict)

    def __post_init__(self):
        if self.talk:
            return

        # Load from binary Binder source.
        for entry in self.entries:
            if not (match := _TALK_ESD_RE.match(entry.name)):
                _LOGGER.warning(f"Ignoring unknown entry '{entry.name}' in TalkESDBND Binder.")
                continue
            talk_id = int(match.group(1))
            try:
                self.talk[talk_id] = entry.to_binary_file(self.TALK_ESD_CLASS)
            except Exception as ex:
                _LOGGER.error(f"Could not load talk ESD 't{talk_id}' from TalkESDBND entry '{entry.name}'. Error: {ex}")
                raise

    def get_default_new_entry_id(self, entry_name: str) -> int:
        return self.get_first_new_entry_id_in_range(0, 1000000)

    @classmethod
    def from_esp_directory(cls, esp_directory: Path | str) -> tp.Self:
        """Load from directory of individual ESP files/folders."""
        esp_directory = Path(esp_directory)

        talk = {}
        for esp_path in Path(esp_directory).glob("t*"):
            if not (match := _TALK_RE.match(esp_path.name)):
                continue  # ignore file

            talk_id = int(match.group(1))

            try:
                if esp_path.is_dir():
                    talk[talk_id] = cls.TALK_ESD_CLASS.from_esp_directory(esp_path)
                elif _TALK_ESP_RE.match(esp_path.name):
                    talk[talk_id] = cls.TALK_ESD_CLASS.from_esp_file(esp_path)
                else:
                    continue  # ignore file
            except Exception as ex:
                _LOGGER.error(f"Could not load talk 't{talk_id}' from ESP directory/file {esp_path.name}. Error: {ex}")

        # No need to generate Binder entries until write requested.
        return cls(path=esp_directory.with_suffix(cls.EXT), talk=talk)

    @classmethod
    def from_talk_dict(cls, talk_dict: dict[int, ESD]) -> tp.Self:
        return cls(talk=talk_dict.copy())

    def write_esp_directory(self, esp_directory: Path | str):
        """Write `TalkESDBND` as a directory of ESP files (1 state machine) and/or folders (2+ state machines)."""
        esp_directory = Path(esp_directory)
        esp_directory.mkdir(parents=True, exist_ok=True)
        for talk_id, talk_esd in self.talk.items():
            if len(talk_esd.state_machines) == 1:
                talk_esd.write_esp_file(esp_directory / f"t{talk_id}.esp.py")
            else:
                talk_esd.write_esp_directory(esp_directory / f"t{talk_id}")

    def entry_autogen(self):
        """Regenerate Binder entries from `talk` dictionary."""

        # Remove BND talk entries that aren't still present in this `TalkESDBND` instance.
        current_entry_names = [f"t{talk_id}.esd" for talk_id in self.talk]
        for entry_name in [entry.name for entry in self.entries]:
            if entry_name not in current_entry_names:
                self.remove_entry_name(entry_name)

        for talk_entry_name, talk_esd in zip(current_entry_names, self.talk.values(), strict=True):
            entry_path = self.get_default_entry_path(talk_entry_name)
            entry = self.set_default_entry(entry_path)
            if not entry.data:
                _LOGGER.debug(f"New ESD entry added to `TalkESDBND`: {talk_entry_name}")
            entry.set_from_binary_file(talk_esd)

        # Sort entries by name.
        self.entries.sort(key=lambda entry: entry.name)

    def __getitem__(self, talk_id) -> TALK_ESD_T:
        return self.talk[talk_id]

    def __iter__(self):
        return iter(self.talk)

    def __repr__(self):
        return f"TalkESDBND({repr(self.path)}): {list(self.talk)}"

    @classmethod
    def write_from_dict(cls, talk_dict, talkesdbnd_path, make_dirs=True):
        """Shortcut to immediately load given dictionary and write to given `.talkesdbnd` path."""
        talkesdbnd = cls.from_talk_dict(talk_dict)  # type: tp.Self
        # Skip `entry_autogen()` call in this class.
        Binder.write(talkesdbnd, talkesdbnd_path, make_dirs=make_dirs)
