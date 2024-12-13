from __future__ import annotations

__all__ = ["GameFileDirectory", "GameFileMapDirectory", "map_property"]

import abc
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.utilities.files import create_bak, get_blake2b_hash
from .base_binary_file import BaseBinaryFile, BASE_BINARY_FILE_T
from .dataclass_meta import DataclassMeta

if tp.TYPE_CHECKING:
    from .game_types.map_types import Map
    from .maps.utilities import GET_MAP_TYPING

_LOGGER = logging.getLogger("soulstruct")


GAME_FILE_DIRECTORY_T = tp.TypeVar("GAME_FILE_DIRECTORY_T", bound="GameFileDirectory")


@tp.dataclass_transform(kw_only_default=False)
class GameFileDirectoryMeta(DataclassMeta):
    """Metaclass for `GameFileDirectoryMeta` that adds dataclass wrapping."""

    def __call__(cls: type[GAME_FILE_DIRECTORY_T], *args, **kwargs) -> GAME_FILE_DIRECTORY_T:
        """Intercept instance creation to handle the single-argument path case, which calls `cls.from_path(path)`."""
        if len(args) == 1 and isinstance(args[0], (Path, str)) and not kwargs:
            # Call `from_path` if a single `path` argument is provided
            return cls.from_path(args[0])
        # Otherwise, proceed with the normal dataclass constructor.
        return super(GameFileDirectoryMeta, cls).__call__(*args, **kwargs)


@dataclass(slots=True)
class GameFileDirectory(tp.Generic[BASE_BINARY_FILE_T], abc.ABC, metaclass=GameFileDirectoryMeta):
    """Python structure for a folder of files in a FromSoftware installation. Implementation is much more flexible.

    Typical usage is to specify subclass `FILE_NAME_PATTERN`, `FILE_CLASS`, and `FILE_EXTENSION` to indicate which file
    names should be loaded into which Python class, then use `__post_init__` to compute any other fields if needed.
    """
    FILE_NAME_PATTERN: tp.ClassVar[str]
    FILE_CLASS: tp.ClassVar[type[BaseBinaryFile]]
    FILE_EXTENSION: tp.ClassVar[str] = ""  # NOTE: `.dcx` extension will be applied by `BinaryBaseFile.write()`

    # Tracks directory that instance was loaded from (if any) for argument-free write calls.
    # If this is the only argument passed to the constructor (without a keyword), then `from_path` will be called.
    directory: Path | None = field(default=None, kw_only=False)
    # Maps 'true stems' to `FILE_CLASS` instances.
    files: dict[str, BASE_BINARY_FILE_T] = field(default_factory=dict, kw_only=True)

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
        file_name_re = re.compile(cls.FILE_NAME_PATTERN + r"(\.dcx)?$")
        for file_path in directory_path.glob("*"):
            if file_name_re.match(file_path.name):
                file_path_stem = file_path.name.split(".")[0]
                files[file_path_stem] = cls.FILE_CLASS.from_path(file_path)

        return cls(directory=directory_path, files=files)

    @staticmethod
    def _write(
        paths_instances: dict[Path, BaseBinaryFile], check_file_hashes=False, no_partial_write=True
    ) -> list[Path]:
        """Internal write method. Subclasses may determine file paths differently, then call this."""
        packed_files = {}  # type: dict[Path, bytes]
        for file_path, instance in paths_instances.items():
            try:
                packed_dcx = bytes(instance)
            except Exception as ex:
                if no_partial_write:
                    _LOGGER.error(f"Failed to pack {file_path.name} (see traceback). No files written.")
                    raise
                _LOGGER.error(f"Failed to pack {file_path.name}: {ex}. Continuing with other files...")
                continue
            if check_file_hashes and file_path.is_file():
                if get_blake2b_hash(file_path) == get_blake2b_hash(packed_dcx):
                    continue  # don't write file
            packed_files[file_path] = packed_dcx

        # All files packed successfully (or partial write permitted).
        written_paths = []
        for file_path, packed_dcx in packed_files.items():
            file_path.parent.mkdir(parents=True, exist_ok=True)
            create_bak(file_path)
            with file_path.open("wb") as f:
                f.write(packed_dcx)
            written_paths.append(file_path)

        return written_paths

    def _log_directory_write(self, directory_path: Path, file_count: int):
        if file_count > 0:
            _LOGGER.info(
                f"`{self.__class__.__name__}` written to `{directory_path}` successfully "
                f"({file_count} / {len(self.files)} files)."
            )
        else:
            _LOGGER.info(f"No files (out of {len(self.files)}) written for `{self.__class__.__name__}`.")

    def write(
        self,
        directory_path: Path | str | None = None,
        check_file_hashes: bool = False,
        no_partial_write=True,
    ) -> list[Path]:
        if directory_path is None:
            if self.directory is None:
                raise ValueError("Cannot autodetect directory name (`directory` not set).")
            directory_path = self.directory
        directory_path = Path(directory_path)

        file_paths = {
            (directory_path / f"{file_stem}{self.FILE_EXTENSION}"): instance
            for file_stem, instance in self.files.items()
        }

        written_paths = self._write(file_paths, check_file_hashes, no_partial_write)
        self._log_directory_write(directory_path, len(written_paths))
        return written_paths

    def keys(self):
        return self.files.keys()

    __iter__ = keys

    def values(self):
        return self.files.values()

    def items(self):
        return self.files.items()


class GameFileMapDirectory(GameFileDirectory[BASE_BINARY_FILE_T], abc.ABC):
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
    # Any unexpected files found in here will be ignored as usual, but will not log a warning.
    QUIETLY_IGNORED_FILE_STEMS: tp.ClassVar[set[str]] = set()

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
        file_name_re = re.compile(cls.FILE_NAME_PATTERN + r"(\.dcx)?$")
        for file_path in directory_path.glob("*"):
            if file_name_re.match(file_path.name):
                file_stem = file_path.name.split(".")[0]  # `.stem` not good enough with possible double DCX extension
                if file_stem in all_map_stems:
                    files[file_stem] = cls.FILE_CLASS.from_path(file_path)
                    all_map_stems.remove(file_stem)
                else:
                    if file_stem not in cls.QUIETLY_IGNORED_FILE_STEMS:
                        _LOGGER.warning(
                            f"Ignoring file with unrecognized map stem in `{cls.__name__}` directory: {file_path.name}"
                        )
                    continue
            else:
                # _LOGGER.warning(f"Ignoring unexpected file in `{cls.__name__}` directory: {file_path.name}")
                continue

        if all_map_stems:
            _LOGGER.warning(f"Could not find some files in `{cls.__name__}` directory: {', '.join(all_map_stems)}")

        return cls(directory=directory_path, files=files)

    def write(
        self, directory_path: Path | str | None = None, check_file_hashes=False, no_partial_write=True
    ) -> list[Path]:
        """Same as `GameFileDirectory`, but reports unknown files and if any maps are missing."""
        if directory_path is None:
            if self.directory is None:
                raise ValueError("Cannot autodetect directory name (`directory` not set).")
            directory_path = self.directory
        directory_path = Path(directory_path)

        all_map_stems = [getattr(game_map, self.MAP_STEM_ATTRIBUTE) for game_map in self.ALL_MAPS]
        file_paths = {}
        for file_stem, instance in self.files.items():
            if file_stem in all_map_stems:
                all_map_stems.remove(file_stem)
            else:
                _LOGGER.warning(f"Writing unknown map file found in `{self.__class__.__name__}`: {file_stem}")
            file_paths[directory_path / f"{file_stem}{self.FILE_EXTENSION}"] = instance
        if all_map_stems:
            _LOGGER.warning(
                f"Could not find some file keys while writing `{self.__class__.__name__}` directory: "
                f"{', '.join(all_map_stems)}"
            )

        written_paths = self._write(file_paths, check_file_hashes, no_partial_write)
        if written_paths:
            _LOGGER.info(
                f"`{self.__class__.__name__}` written to `{directory_path}` successfully "
                f"({len(written_paths)} / {len(self.files)} files)."
            )
        else:
            _LOGGER.info(f"No files written for `{self.__class__.__name__}`.")
        return written_paths

    def __getitem__(self, map_source: str | tuple) -> BASE_BINARY_FILE_T:
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
