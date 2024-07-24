from __future__ import annotations

__all__ = ["GameFile", "GAME_FILE_T"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass
from pathlib import Path

from .base_binary_file import BaseBinaryFile

if tp.TYPE_CHECKING:
    from soulstruct.containers import Binder

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class GameFile(BaseBinaryFile, abc.ABC):
    """Non-binder file in a FromSoftware game installation."""

    @classmethod
    def from_binder(cls, binder: Binder, entry_spec: int | Path | str | re.Pattern = None) -> tp.Self:
        """Load a single instance of this type from the specified `entry_spec`.

        The type of `entry_spec` determines how the entry is found. An integer will be interpreted as an entry ID, a
        `Path` will be interpreted as a full entry path, a string will be interpreted as an entry name only, and a
        `re.Pattern` will be be used to search all entry names. It will default to the latter using `PATTERN` class
        attribute.

        Will raise an exception if no matching entries or multiple matching entries exist in the BND.
        """
        entry_spec = entry_spec or cls.PATTERN
        flver_entry = binder[entry_spec]
        return cls.from_bytes(flver_entry)

    @classmethod
    def from_binder_path(
        cls, binder_path: Path | str, entry_spec: int | Path | str | re.Pattern = None, from_bak=False
    ) -> tp.Self:
        """Open a file of this type from the given `entry_id_or_name` (`str` or `int`) of the given `Binder` source."""
        from soulstruct.containers import Binder
        binder = Binder.from_bak(binder_path) if from_bak else Binder.from_path(binder_path)
        return cls.from_binder(binder, entry_spec)

    @classmethod
    def multiple_from_binder_path(
        cls, binder_path: Path | str, entry_specs: tp.Sequence[int | Path | str | re.Pattern], from_bak=False
    ) -> list[tp.Self]:
        """Open multiple files of this type from the given `entry_ids_or_names` (each can be a `str` or `int`) from
        Binder read from `binder_path`."""
        from soulstruct.containers import Binder
        binder = Binder.from_bak(binder_path) if from_bak else Binder.from_path(binder_path)
        return [binder[entry_spec].to_binary_file(cls) for entry_spec in entry_specs]


GAME_FILE_T = tp.TypeVar("GAME_FILE_T", bound=GameFile)
