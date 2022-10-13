from __future__ import annotations

__all__ = ["GameFile", "GameFolder", "InvalidGameFileTypeError"]

import abc
import copy
import io
import logging
import typing as tp
from pathlib import Path

from soulstruct.exceptions import InvalidGameFileTypeError, GameFileDictSupportError
from soulstruct.containers.dcx import DCXType, compress, decompress
from soulstruct.utilities.binary import BinaryReader, get_blake2b_hash
from soulstruct.utilities.files import create_bak, read_json, write_json
from .binder_entry import BinderEntry

if tp.TYPE_CHECKING:
    from soulstruct.games import Game

_LOGGER = logging.getLogger(__name__)


T = tp.TypeVar("T", bound="GameFile")


class GameFile(abc.ABC):
    """Python structure for a file in a FromSoftware game installation."""

    GAME: Game = None  # mixed in by game-specific classes
    EXT = ""  # if given, this file extension will be enforced (before DCX is checked) when calling `.write()`
    Typing = tp.Union[str, Path, bytes, BinderEntry, io.BufferedIOBase, BinaryReader]  # all globally valid source types
    Types = (str, Path, bytes, io.BufferedIOBase, BinaryReader)

    dcx_type: DCXType

    def __init__(
        self,
        file_source: Typing = None,
        dcx_type: DCXType | None = DCXType.Null,
        **kwargs,
    ):
        """Base class for a game file, with key methods and automatic DCX detection.

        Args:
            file_source (None, str, Path, bytes, BufferedIOBase): a file path, `bytes` object, or binary stream to load
                the file from. It will be checked for DCX first. Set to None (default) to create a default instance.
            dcx_type (DCXType): optional DCX compression type enum to manually specify the DCX. Only permitted for
                `file_source` values that are not already DCX-compressed. (If you want to change the DCX for some
                reason, set `.dcx_type` directly after the instance is created.)
            kwargs: keyword arguments to pass on to `unpack` for buffered sources.
        """
        self._dcx_type = DCXType.Null
        self.dcx_type = dcx_type  # run through setter

        self.path = None  # type: tp.Optional[Path]

        if file_source is None:
            return

        try:
            reader = self._handle_other_source_types(file_source, **kwargs)
            if reader is None:
                return
        except InvalidGameFileTypeError:
            if isinstance(file_source, dict):
                self.load_dict(file_source.copy())
                return
            if isinstance(file_source, (str, Path)):
                self.path = Path(file_source)
                if self.path.suffix == ".json":
                    json_dict = read_json(self.path, encoding="utf-8")
                    try:
                        self.load_dict(json_dict)
                    except Exception as ex:
                        _LOGGER.error(f"Error while loading as JSON dict: {self.path}.\n  {ex}")
                        raise
                    return
            if isinstance(file_source, (str, Path, bytes, io.BufferedIOBase, BinderEntry)):
                reader = BinaryReader(file_source)
            elif isinstance(file_source, BinaryReader):
                reader = file_source
            else:
                raise InvalidGameFileTypeError(f"Invalid `GameFile` source type: {type(file_source)}")

        if self._is_dcx(reader):
            if self.dcx_type != DCXType.Null:
                reader.close()
                raise ValueError("Cannot manually set `dcx_type` before reading a DCX file source.")
            try:
                data, self.dcx_type = decompress(reader)
            finally:
                reader.close()
            reader = BinaryReader(data)

        try:
            self.unpack(reader, **kwargs)
        except Exception:
            _LOGGER.error(f"Error occurred while parsing game file: {self.path}. See traceback.")
            raise
        finally:
            reader.close()

    def _handle_other_source_types(self, file_source, **kwargs) -> tp.Optional[BinaryReader]:
        """Override this to initialize `GameFile` subclass from other types of `file_source`. This function will be
        called before the standard `GameFile.Types` are checked.

        If a `BinaryReader` object is returned, the constructor will continue with unpacking from that reader.
        Otherwise, it will return without calling `.unpack()`.

        If no valid source types are found, raise `InvalidGameFileTypeError` (like below) to have the constructor
        continue checking the standard source types.
        """
        raise InvalidGameFileTypeError(f"No special handler for `GameFile` source type: {type(file_source)}")

    @classmethod
    def from_binder(cls, binder_source: Typing, entry_id_or_name: int | str, from_bak=False):
        """Open a file of this type from the given `entry_id_or_name` (`str` or `int`) of the given `Binder` source."""
        from soulstruct.containers import Binder
        binder = Binder(binder_source, from_bak=from_bak)
        return cls(binder[entry_id_or_name])

    @classmethod
    def multiple_from_binder(cls, binder_source, entry_ids_or_names: tp.Sequence[int | str], from_bak=False):
        """Open multiple files of this type from the given `entry_ids_or_names` (`str` or `int`) from
        `Binder` source."""
        from soulstruct.containers import Binder
        binder = Binder(binder_source, from_bak=from_bak)
        return [cls(binder[entry_id_or_name]) for entry_id_or_name in entry_ids_or_names]

    @abc.abstractmethod
    def unpack(self, reader: BinaryReader, **kwargs):
        """Unpack game file from given buffer, using various `BinaryStruct`s defined in the class."""

    def load_dict(self, data: dict, clear_old_data=True):
        """Load game file from given `data` dictionary (which is a copy of the source).

        Where implemented, if `clear_old_data=True` (default), the `GameFile` instance will have all relevant data
        cleared  first. Otherwise, existing data will not be cleared, and newer data with the same ID, key, etc. will
        override old data. In this case, any conflicting header data will raise a `ValueError`.

        Not supported by default.
        """
        raise GameFileDictSupportError(f"`{self.__class__.__name__}` class does not support JSON/dictionary input.")

    @abc.abstractmethod
    def pack(self, **kwargs) -> bytes:
        """Pack game file into `bytes`, using various `BinaryStruct`s defined in the class."""

    def pack_dcx(self, **kwargs) -> bytes:
        """Call `pack()` and apply DCX compression to binary data, if appropriate, based on `self.dcx_type`."""
        if self._dcx_type != DCXType.Null:
            return compress(self.pack(**kwargs), self._dcx_type)
        return self.pack(**kwargs)

    def to_dict(self, **kwargs) -> dict:
        """Create a dictionary from `GameFile` instance. Not supported by default."""
        raise GameFileDictSupportError(f"`{self.__class__.__name__}` class does not support JSON/dictionary output.")

    def write(self, file_path: None | str | Path = None, make_dirs=True, check_hash=False, **pack_kwargs):
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
            pack_kwargs: extra keyword arguments to pass to `.pack()`.
        """
        file_path = self._get_file_path(file_path)
        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        packed = self.pack_dcx(**pack_kwargs)
        if check_hash and file_path.is_file():
            # TODO: This may always report that DCX files have changed, but decompressing the existing file to check its
            #  real hash seems excessive?
            if get_blake2b_hash(file_path) == get_blake2b_hash(packed):
                return  # don't write file
        create_bak(file_path)
        with file_path.open("wb") as f:
            f.write(packed)

    def write_json(self, file_path: None | str | Path, encoding="utf-8", indent=4, **kwargs):
        """Create a dictionary from `GameFile` instance. Requires `.to_dict()` to be implemented by `GameFile` subclass.

        The file path will have the `.json` suffix added automatically.
        """
        json_dict = self.to_dict(**kwargs)
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

    @staticmethod
    def _is_dcx(reader: BinaryReader) -> bool:
        """Checks if file data starts with DCX (or DCP) magic."""
        return reader.unpack_value("4s", offset=0) in {b"DCP\0", b"DCX\0"}

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
    def from_bak(cls: tp.Type[T], game_file_path: tp.Union[Path, str], dcx_type=None, create_bak_if_missing=True) -> T:
        """Looks for a `.bak` version of the given path to open preferentially, or optionally creates it if missing."""
        game_file_path = Path(game_file_path)
        bak_path = game_file_path.with_name(game_file_path.name + ".bak")
        if bak_path.is_file():
            game_file = cls(bak_path, dcx_type=dcx_type)
            game_file.path = game_file.path.with_suffix("")  # remove ".bak" extension
            return game_file
        else:
            game_file = cls(game_file_path, dcx_type=dcx_type)
            if create_bak_if_missing:
                create_bak(game_file_path)
            return game_file


class GameFolder(abc.ABC):
    """Python structure for a folder of files in a FromSoftware installation. Implementation is much more flexible."""
