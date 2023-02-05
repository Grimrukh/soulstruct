from __future__ import annotations

__all__ = ["TalkDirectory"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass
from pathlib import Path

from soulstruct.base.game_file_directory import GameFileMapDirectory

try:
    Self = tp.Self
except AttributeError:
    Self = "TalkDirectory"

if tp.TYPE_CHECKING:
    from .talkesdbnd import TalkESDBND

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class TalkDirectory(GameFileMapDirectory, abc.ABC):
    """Directory containing `TalkESDBND` files."""

    FILE_NAME_PATTERN: tp.ClassVar[str] = r".*\.talkesdbnd"  # also manually checks for directories
    FILE_CLASS: tp.ClassVar[tp.Type[TalkESDBND]] = None  # only attribute that subclass must define
    FILE_EXTENSION = ".talkesdbnd"
    MAP_STEM_ATTRIBUTE = "esd_file_stem"

    @classmethod
    def from_path(cls, directory_path: Path | str):
        """Loads files as appropriate type (ESD/ESP folder/ESP file)."""
        if cls.FILE_NAME_PATTERN is None or cls.FILE_CLASS is None:
            raise TypeError(
                f"`GameFileDirectory` subclass `{cls.__name__}` must define `FILE_NAME_PATTERN` and `FILE_CLASS` class "
                f"variables, or override `from_path()` with its own different logic."
            )

        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            raise NotADirectoryError(f"Missing directory: {directory_path}")
        all_map_stems = [getattr(game_map, cls.MAP_STEM_ATTRIBUTE) for game_map in cls.ALL_MAPS]
        files = {}
        file_name_re = re.compile(cls.FILE_NAME_PATTERN + r"(\.dcx)?")
        for file_path in directory_path.glob("*"):

            if file_path.is_dir() and file_path.stem in all_map_stems:
                # Try to load `TalkESDBND` from directory of ESP files matching the map stem.
                files[file_path.stem] = cls.FILE_CLASS.from_esp_directory(file_path)
                all_map_stems.remove(file_path.stem)
                continue
            elif file_name_re.match(file_path.name):
                file_stem = file_path.name.split(".")[0]  # `.stem` not good enough with possible double DCX extension
                if file_stem in all_map_stems:  # `.talkesdbnd` file
                    files[file_path.name] = cls.FILE_CLASS.from_path(file_path)
                    all_map_stems.remove(file_stem)
                    continue
            _LOGGER.warning(f"Ignoring unexpected file in `{cls.__name__}` directory: {file_path.name}")

        if all_map_stems:
            _LOGGER.warning(f"Could not find some files in `{cls.__name__}` directory: {', '.join(all_map_stems)}")

        return cls(directory_path, files)

    def write_esp(self, esp_directory=None):
        """Write ESP for all maps. Defaults to loaded directory."""
        if esp_directory is None:
            esp_directory = self.directory
        esp_directory = Path(esp_directory)
        for game_map in [m for m in self.ALL_MAPS if m.esd_file_stem]:
            talkesdbnd = self.files[game_map.esd_file_stem]
            talkesdbnd.write_esp(talk_directory=esp_directory / f"{game_map.esd_file_stem}")
