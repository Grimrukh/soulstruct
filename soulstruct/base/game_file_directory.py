from __future__ import annotations

__all__ = ["GameFileDirectory", "GameFileMapDirectory", "map_property"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

if tp.TYPE_CHECKING:
    from .base_binary_file import BaseBinaryFile, BASE_BINARY_FILE_T
    from .game_types.map_types import Map
    from .maps.utilities import GET_MAP_TYPING

try:
    from typing import Self
except ImportError:  # < Python 3.11
    Self = "GameFileDirectory"

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class GameFileDirectory(tp.Generic[BASE_BINARY_FILE_T], abc.ABC):
    """Python structure for a folder of files in a FromSoftware installation. Implementation is much more flexible.

    Typical usage is to specify subclass `FILE_RE` and `FILE_CLASS` to indicate which file names should be loaded into
    which Python class, then use `__post_init__` to compute other fields.
    """
    FILE_NAME_PATTERN: tp.ClassVar[str] = None
    FILE_CLASS: tp.ClassVar[tp.Type[BaseBinaryFile]] = None
    FILE_EXTENSION: tp.ClassVar[str] = ""  # NOTE: `.dcx` extension will be applied by `BinaryBaseFile.write()`

    directory: Path = Path()
    files: dict[str, BASE_BINARY_FILE_T] = field(default_factory=dict)  # maps 'true stems' to `FILE_CLASS` instances

    @classmethod
    def from_path(cls, directory_path: Path | str):
        if cls.FILE_NAME_PATTERN is None or cls.FILE_CLASS is None:
            raise TypeError(
                f"`GameFileDirectory` subclass `{cls.__name__}` must define `FILE_NAME_PATTERN` and `FILE_CLASS` class "
                f"variables, or override `from_path()` with its own different logic."
            )

        directory_path = Path(directory_path)
        if not directory_path.is_dir():
            raise NotADirectoryError(f"Missing directory: {directory_path}")
        files = {}
        file_name_re = re.compile(cls.FILE_NAME_PATTERN + r"(\.dcx)?")
        for file_path in directory_path.glob("*"):
            if file_name_re.match(file_path.name):
                file_path_stem = file_path.name.split(".")[0]
                files[file_path_stem] = cls.FILE_CLASS.from_path(file_path)

        return cls(directory_path, files)

    def write(self, directory_path: Path | str | None = None, check_file_hashes: bool = False):
        if directory_path is None:
            if self.directory is None:
                raise ValueError("Cannot autodetect directory name (`directory` not set).")
            directory_path = self.directory
        directory_path = Path(directory_path)
        directory_path.mkdir(parents=True, exist_ok=True)
        for file_stem, instance in self.files.items():
            instance.write(directory_path / f"{file_stem}{self.FILE_EXTENSION}", check_hash=check_file_hashes)
        _LOGGER.info(
            f"`{self.__class__.__name__}` written to `{directory_path}` successfully ({len(self.files)} files)."
        )

    def keys(self):
        return self.files.keys()

    __iter__ = keys

    def values(self):
        return self.files.values()

    def items(self):
        return self.files.items()


@dataclass(slots=True)
class GameFileMapDirectory(GameFileDirectory, abc.ABC):
    """Game file directory that expects to find a file for each game map in `ALL_MAPS`, which should be defined by the
    game-specific subclass.

    A warning will be logged if a given map's file is not found in an opened directory, or if it is missing from the
    `files` dictionary when writing the directory.
    """

    # Game-specific list of `map` instances. May or may not include a 'common' file.
    ALL_MAPS: tp.ClassVar[tuple[Map]] = ()
    # Function that takes various flexible ways of specifying a map and returns a game-specific `Map` instance.
    GET_MAP: tp.ClassVar[GET_MAP_TYPING] = None
    # Name of `Map` attribute to use when determining which stems to look for. (Should also work for 'common' files.)
    # `emevd_file_stem` is the default because it contains the least irregularities so far, in my experience.
    MAP_STEM_ATTRIBUTE: tp.ClassVar[str] = "emevd_file_stem"

    # NOTE: Game-specific subclasses will generally want to define map name getter properties, a la:
    #  `UndeadBurg = property(lambda self: self.files[UNDEAD_BURG.msb_file_stem])`

    @classmethod
    def from_path(cls, directory_path: Path | str):
        # NOTE: Pattern is still used in combination with `Map` stems.
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
            if file_name_re.match(file_path.name):
                file_stem = file_path.name.split(".")[0]  # `.stem` not good enough with possible double DCX extension
                if file_stem in all_map_stems:
                    files[file_path.name] = cls.FILE_CLASS.from_path(file_path)
                    all_map_stems.remove(file_stem)
                else:
                    _LOGGER.warning(f"Ignoring unexpected file in `{cls.__name__}` directory: {file_path.name}")
                    continue

        if all_map_stems:
            _LOGGER.warning(f"Could not find some files in `{cls.__name__}` directory: {', '.join(all_map_stems)}")

        return cls(directory_path, files)

    def write(self, directory_path: Path | str | None = None, check_file_hashes: bool = False):
        """Same as `GameFileDirectory`, but reports unknown files and if any maps are missing."""
        if directory_path is None:
            if self.directory is None:
                raise ValueError("Cannot autodetect directory name (`directory` not set).")
            directory_path = self.directory
        directory_path = Path(directory_path)
        all_map_stems = [getattr(game_map, self.MAP_STEM_ATTRIBUTE) for game_map in self.ALL_MAPS]
        directory_path.mkdir(parents=True, exist_ok=True)
        for file_name, instance in self.files.items():
            file_stem = file_name.split(".")[0]
            if file_stem in all_map_stems:
                all_map_stems.remove(file_stem)
            else:
                _LOGGER.warning(f"Writing unknown map file found in `{self.__class__.__name__}`: {file_name}")
            instance.write(directory_path / file_name, check_hash=check_file_hashes)
        if all_map_stems:
            _LOGGER.warning(
                f"Could not find some files while writing `{self.__class__.__name__}` directory: "
                f"{', '.join(all_map_stems)}"
            )
        _LOGGER.info(
            f"`{self.__class__.__name__}` written to `{directory_path}` successfully ({len(self.files)} files)."
        )

    def __getitem__(self, map_source: str | tuple):
        game_map = self.GET_MAP(map_source)
        map_stem = getattr(game_map, self.MAP_STEM_ATTRIBUTE)
        for file_name, file_instance in self.files.items():
            if file_name.split(".")[0] == map_stem:
                return file_instance
        raise KeyError(
            f"Could not find map `{game_map.name}` with stem `{map_stem}` (from spec `{map_source}`) in this "
            f"`{self.__class__.__name__}`."
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.directory}, <{len(self.files)} files>)"


def map_property(game_map: Map):
    """Assists in assigning properties to map names, e.g. `UndeadBurg = map_property(UNDEAD_BURG)"""
    return property(lambda self: self.files[getattr(game_map, self.MAP_STEM_ATTRIBUTE)])
