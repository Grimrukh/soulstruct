from __future__ import annotations

__all__ = ["GameFile"]

import abc
import logging
import re
import typing as tp
from pathlib import Path

from .base_binary_file import BaseBinaryFile

if tp.TYPE_CHECKING:
    from soulstruct.containers import Binder

_LOGGER = logging.getLogger(__name__)


class GameFile(BaseBinaryFile, abc.ABC):
    """Any non-Binder file in a FromSoftware game installation."""

    @classmethod
    def from_binder(cls, binder: Binder, entry_spec: int | Path | str | re.Pattern | None = None) -> tp.Self:
        """Load a single instance of this type from the specified `entry_spec`.

        The type of `entry_spec` determines how the entry is found. An integer will be interpreted as an entry ID, a
        `Path` will be interpreted as a full entry path, a string will be interpreted as an entry name only, and a
        `re.Pattern` will be used to search all entry names. It will default to the latter using `PATTERN` class
        attribute.

        Will raise an exception if no matching entries or multiple matching entries exist in the BND.
        """
        if entry_spec is None:
            entry_spec = cls.PATTERN
            if entry_spec is None:
                raise ValueError(f"`entry_spec` not given and class {cls.__name__} has no default PATTERN.")
        flver_entry = binder[entry_spec]
        return cls.from_bytes(flver_entry)

    @classmethod
    def from_binder_path(
        cls, binder_path: Path | str, entry_spec: int | Path | str | re.Pattern | None = None, from_bak=False
    ) -> tp.Self:
        """Open a file of this type from the given `entry_id_or_name` (`str` or `int`) of the given `Binder` source."""
        from soulstruct.containers import Binder

        # Validate `entry_spec` now before opening Binder.
        if entry_spec is None:
            entry_spec = cls.PATTERN
            if entry_spec is None:
                raise ValueError(f"`entry_spec` not given and class {cls.__name__} has no default PATTERN.")

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
