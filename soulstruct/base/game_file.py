from __future__ import annotations

__all__ = ["GameFile", "GAME_FILE_T"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from .base_binary_file import BaseBinaryFile

try:
    from typing import Self
except ImportError:  # < Python 3.11
    Self = "GameFile"

_LOGGER = logging.getLogger(__name__)


"""
TODO:
    - More of an ECS system for MSB entries.    
"""

GAME_FILE_T = tp.TypeVar("GAME_FILE_T", bound="GameFile")


@dataclass(slots=True)
class GameFile(BaseBinaryFile, abc.ABC):
    """Non-binder file in a FromSoftware game installation."""

    @classmethod
    def from_binder_path(cls, binder_path: Path | str, entry_id_or_name: int | str, from_bak=False) -> Self:
        """Open a file of this type from the given `entry_id_or_name` (`str` or `int`) of the given `Binder` source."""
        from soulstruct.containers import Binder
        binder = Binder.from_bak(binder_path) if from_bak else Binder.from_path(binder_path)

        return binder[entry_id_or_name].to_game_file(cls)

    @classmethod
    def multiple_from_binder_path(
        cls, binder_path: Path | str, entry_ids_or_names: tp.Sequence[int | str], from_bak=False
    ) -> list[Self]:
        """Open multiple files of this type from the given `entry_ids_or_names` (`str` or `int`) from
        `Binder` source."""
        from soulstruct.containers import Binder
        binder = Binder.from_bak(binder_path) if from_bak else Binder.from_path(binder_path)
        return [binder[entry_id_or_name].to_game_file(cls) for entry_id_or_name in entry_ids_or_names]
