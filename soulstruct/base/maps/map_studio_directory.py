from __future__ import annotations

__all__ = ["MapStudioDirectory", "MSB_T"]

import abc
import json
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.game_file_directory import GameFileMapDirectory
from .msb import MSB

_LOGGER = logging.getLogger(__name__)

MSB_T = tp.TypeVar("MSB_T", bound=MSB)


@dataclass(slots=True)
class MapStudioDirectory(GameFileMapDirectory[MSB_T], abc.ABC):
    """Unpack MSB map data files from a `MapStudio` directory into one single modifiable structure.

    Note that you only need to reload the map (e.g. by saving and quitting, or getting sufficiently far away from
    the map) to see changes in these files while playing the game. You do NOT need to fully restart the game, unlike
    with text and parameter/lighting changes.
    """

    FILE_NAME_PATTERN: tp.ClassVar[str] = r".*\.msb"
    FILE_CLASS: tp.ClassVar[tp.Type[MSB]]
    FILE_EXTENSION: tp.ClassVar[str] = ".msb"
    MAP_STEM_ATTRIBUTE: tp.ClassVar[str] = "msb_file_stem"

    # Override file type.
    files: dict[str, MSB] = field(default_factory=dict)  # maps 'true stems' to `FILE_CLASS` instances

    @classmethod
    def from_json_directory(cls, directory_path: Path | str):
        """Open directory of JSON files containing MSB data instead of standard `.msb` files."""
        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            raise NotADirectoryError(f"Missing directory: {directory_path}")

        all_map_stems = [getattr(game_map, cls.MAP_STEM_ATTRIBUTE) for game_map in cls.ALL_MAPS]
        files = {}
        file_name_re = re.compile(r".*\.json")
        for file_path in directory_path.glob("*"):
            if file_name_re.match(file_path.name):
                file_stem = file_path.name.split(".")[0]  # `.stem` not good enough with possible double DCX extension
                if file_stem in all_map_stems:
                    msb = files[file_stem] = cls.FILE_CLASS.from_json(file_path)
                    msb.path = directory_path / f"{file_stem}{cls.FILE_EXTENSION}"
                    all_map_stems.remove(file_stem)
                else:
                    if file_stem not in cls.QUIETLY_IGNORED_FILE_STEMS:
                        _LOGGER.warning(
                            f"Ignoring unexpected JSON file in `{cls.__name__}` directory: {file_path.name}"
                        )
                    continue

        if all_map_stems:
            _LOGGER.warning(f"Could not find some JSON files in `{cls.__name__}` directory: {', '.join(all_map_stems)}")

        return cls(directory=directory_path, files=files)

    def write_combined_json(self, json_path: str | Path, ignore_defaults=True):
        """Write all MSBs to one giant JSON file, keyed by MSB name stem.

        Generally NOT preferable to `write_json_directory()`.
        """
        data = {}
        for msb_file_stem, msb in self.files.items():
            data[msb_file_stem] = msb.to_dict(ignore_defaults=ignore_defaults)
        json_path = Path(json_path)
        json_path.parent.mkdir(exist_ok=True, parents=True)
        with Path(json_path).open("w") as f:
            json.dump(data, f)

    def write_json_directory(self, directory_path: str | Path = None, ignore_defaults=True):
        """Write each MSB to a separate JSON file, named by MSB stem, inside `dir_path`."""
        if directory_path is None:
            directory_path = self.directory
        directory_path = Path(directory_path)
        directory_path.mkdir(exist_ok=True, parents=True)
        for msb_file_stem, msb in self.files.items():
            msb.write_json(directory_path / f"{msb_file_stem}.json", ignore_defaults=ignore_defaults)
