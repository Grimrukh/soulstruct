from __future__ import annotations

__all__ = ["GameFile", "GameDirectory", "InvalidGameFileTypeError", "BinarySourceTyping", "BinarySourceTypes"]

import abc
import copy
import io
import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.exceptions import InvalidGameFileTypeError, GameFileDictSupportError
from soulstruct.containers.dcx import DCXType, compress, decompress, is_dcx
from soulstruct.games import Game, get_game
from soulstruct.utilities.binary import BinaryReader, get_blake2b_hash, BinaryWriter
from soulstruct.utilities.files import create_bak, read_json, write_json
from .binder_entry import BinderEntry

try:
    from typing import Self
except ImportError:  # Python 3.10
    Self = "GameFile"

_LOGGER = logging.getLogger(__name__)


"""
TODO:
    - Support dataclasses.
    - Combine BXF3 and BXF4 into a single class with a version switch. Same for BXF.
    - More of an ECS system for MSB entries.    
"""


# TODO: may no longer need these
BinarySourceTyping = tp.Union[str, Path, bytes, bytearray, BinderEntry, io.BufferedIOBase, BinaryReader]
BinarySourceTypes = (str, Path, bytes, bytearray, BinderEntry, io.BufferedIOBase, BinaryReader)


@dataclass(slots=True)
class GameFile(abc.ABC):
    """Python structure for a file in a FromSoftware game installation."""

    EXT: tp.ClassVar[str] = ""  # if given, extension will be enforced (before DCX is checked) when calling `.write()`

    path: None | Path = field(init=False, repr=False, default=None)  # only set by some class method constructors
    _dcx_type: DCXType = field(init=False, repr=False, default=DCXType.Null)  # accessed through `dcx_type` property

    # `__init__` is constructed automatically (and should be for all `dataclass` subclasses).

    @classmethod
    @abc.abstractmethod
    def _from_reader(cls, reader: BinaryReader) -> Self:
        pass

    @abc.abstractmethod
    def _to_writer(self) -> BinaryWriter:
        pass

    def __bytes__(self) -> bytes:
        """Applies `dcx_type` DCX automatically."""
        packed = self._to_writer().finish()
        if self._dcx_type != DCXType.Null:
            return compress(packed, self._dcx_type)
        return packed

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """Load game file from given `data` dictionary (which is a copy of the source).

        Where implemented, if `clear_old_data=True` (default), the `GameFile` instance will have all relevant data
        cleared first. Otherwise, existing data will not be cleared, and newer data with the same ID, key, etc. will
        override old data. In this case, any conflicting header data will raise a `ValueError`.

        Not supported by default.
        """
        # TODO: Make sure to copy dictionary.
        raise GameFileDictSupportError(f"`{cls.__name__}` class does not support JSON/dictionary input.")

    def to_dict(self) -> dict:
        """Create a dictionary from `GameFile` instance. Not supported by default."""
        raise GameFileDictSupportError(f"`{self.__class__.__name__}` class does not support JSON/dictionary output.")

    @classmethod
    def from_json(cls, json_path: str | Path) -> Self:
        json_dict = read_json(json_path)
        return cls.from_dict(json_dict)

    @classmethod
    def from_path(cls, path: str | Path) -> Self:
        path = Path(path)
        try:
            game_file = cls.from_bytes(path.read_bytes())
        except Exception:
            _LOGGER.error(f"Error occurred while reading `{cls.__name__}` with path '{path}. See traceback.")
            raise
        game_file.path = path
        return game_file

    @classmethod
    def from_bytes(cls, data: bytes | bytearray | io.BufferedIOBase | BinaryReader | BinderEntry) -> Self:
        """Load instance from binary data or binary stream (or `BinderEntry.data`)."""
        reader = BinaryReader(data) if not isinstance(data, BinaryReader) else data  # type: BinaryReader

        if is_dcx(reader):
            try:
                data, dcx_type = decompress(reader)
            finally:
                reader.close()
            reader = BinaryReader(data)
        else:
            dcx_type = DCXType.Null

        try:
            instance = cls._from_reader(reader)
            instance.dcx_type = dcx_type
            return instance
        except Exception:
            _LOGGER.error(f"Error occurred while reading `{cls.__name__}` from binary data. See traceback.")
            raise
        finally:
            reader.close()

    @classmethod
    def from_binder(cls, binder_source: BinarySourceTyping, entry_id_or_name: int | str, from_bak=False):
        """Open a file of this type from the given `entry_id_or_name` (`str` or `int`) of the given `Binder` source."""
        from soulstruct.containers import Binder
        binder = Binder(binder_source, from_bak=from_bak)
        return cls.from_bytes(binder[entry_id_or_name].data)

    @classmethod
    def multiple_from_binder(cls, binder_source, entry_ids_or_names: tp.Sequence[int | str], from_bak=False):
        """Open multiple files of this type from the given `entry_ids_or_names` (`str` or `int`) from
        `Binder` source."""
        from soulstruct.containers import Binder
        binder = Binder(binder_source, from_bak=from_bak)
        return [cls.from_bytes(binder[entry_id_or_name].data) for entry_id_or_name in entry_ids_or_names]

    def write(self, file_path: None | str | Path = None, make_dirs=True, check_hash=False):
        """Pack game file into `bytes`, then write to given `file_path` (or `self.path` if not given).

        Missing directories in given path will be created automatically if `make_dirs` is True. Otherwise, they must
        already exist.

        Will compress with DCX automatically and add `.dcx` file extension if `.dcx_type` is not None. Will also
        automatically create a `.bak` version of the `file_path`, if a backup does not already exist.

        Args:
            file_path (None, str, Path): file path to write to. Defaults to `self.path`, which is automatically set at
                instance creation if a file path is used as a source.
            make_dirs (bool): if True, any directories in `file_path` that are missing will be created. (Default: True)
            check_hash (bool): if True, file will not be written if file with same hash already exists. (Default: False)
        """
        file_path = self._get_file_path(file_path)
        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        packed_dcx = bytes(self)
        if check_hash and file_path.is_file():
            if get_blake2b_hash(file_path) == get_blake2b_hash(packed_dcx):
                return  # don't write file
        create_bak(file_path)
        with file_path.open("wb") as f:
            f.write(packed_dcx)

    def write_json(self, file_path: None | str | Path, encoding="utf-8", indent=4):
        """Create a dictionary from `GameFile` instance. Requires `.to_dict()` to be implemented by `GameFile` subclass.

        The file path will have the `.json` suffix added automatically.
        """
        json_dict = self.to_dict()
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because `GameFile` default path has not been set.")
            file_path = self.path
        file_path = Path(file_path)
        if file_path.suffix != ".json":
            file_path = file_path.with_suffix(file_path.suffix + ".json")
        write_json(file_path, json_dict, indent=indent, encoding=encoding)

    def create_bak(self, file_path: None | str | Path = None, make_dirs=True):
        file_path = self._get_file_path(file_path)
        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        create_bak(file_path)

    def copy(self):
        return copy.deepcopy(self)

    def _get_file_path(self, file_path: None | str | Path) -> Path:
        """Get default path of binary file, based on `EXT` and `dcx_type`."""
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because `GameFile` default path has not been set.")
            file_path = self.path
        file_path = Path(file_path)

        # 1. Remove any existing ".dcx" extension.
        while file_path.suffix == ".dcx":
            file_path = file_path.with_name(file_path.stem)  # remove '.dcx' (may add back below)

        # 2. If `EXT` is defined, add that extension to the path.
        if self.EXT and file_path.suffix != self.EXT:
            file_path = file_path.with_suffix(file_path.suffix + self.EXT)

        # 3. If `dcx_type` is not `Null`, add ".dcx" extension to the path.
        if self.dcx_type != DCXType.Null and not file_path.suffix == ".dcx":
            file_path = file_path.with_suffix(file_path.suffix + ".dcx")  # add ".dcx"

        return file_path

    @property
    def dcx_type(self):
        return self._dcx_type

    @dcx_type.setter
    def dcx_type(self, value: DCXType | None):
        """Set `dcx_type to `value`, which must be a `DCXType` or `None`."""
        if value is None or value == DCXType.Null:
            self._dcx_type = DCXType.Null
        elif isinstance(value, DCXType):
            self._dcx_type = value
        else:
            raise ValueError(f"`dcx_type` must be `DCXType` or None, not {value}.")

    @classmethod
    def from_bak(cls, game_file_path: Path | str, create_bak_if_missing=True) -> Self:
        """Looks for a `.bak` version of the given path to open preferentially, or optionally creates it if missing."""
        game_file_path = Path(game_file_path)
        bak_path = game_file_path.with_name(game_file_path.name + ".bak")
        if bak_path.is_file():
            game_file = cls.from_path(bak_path)
            game_file.path = game_file.path.with_suffix("")  # remove ".bak" extension
            return game_file
        else:
            game_file = cls.from_path(game_file_path)
            if create_bak_if_missing:
                create_bak(game_file_path)
            return game_file

    @classmethod
    def get_game(cls) -> Game:
        if match := re.match(r"^soulstruct\.(\w+)\..*$", cls.__module__):
            return get_game(match.group(1))
        raise ValueError(f"Could not detect game name from module of class `{cls.__name__}`: {cls.__module__}")


class GameDirectory(abc.ABC):
    """Python structure for a folder of files in a FromSoftware installation. Implementation is much more flexible."""
    # TODO: use this...
