from __future__ import annotations

__all__ = [
    "BaseBinaryFile",
    "BASE_BINARY_FILE_T",
    "BaseJSONEncoder",
]

import abc
import copy
import io
import json
import logging
import multiprocessing
import re
import traceback
import typing as tp
from dataclasses import asdict, field, fields
from pathlib import Path

from soulstruct.games import Game, get_game
from soulstruct.utilities.binary import *
from soulstruct.utilities.files import create_bak, read_json, write_json, get_blake2b_hash
from soulstruct.dcx import DCXType, compress, decompress, is_dcx

from .dataclass_meta import DataclassMeta

if tp.TYPE_CHECKING:
    from soulstruct.containers.entry import BinderEntry
    BASE_BINARY_BYTES_TYPING = tp.Union[bytes, bytearray, io.BufferedIOBase, BinaryReader, BinderEntry]


_LOGGER = logging.getLogger(__name__)

_GAME_MODULE_RE = re.compile(r"^soulstruct\.(\w+)\..*$")


BASE_BINARY_FILE_T = tp.TypeVar("BASE_BINARY_FILE_T", bound="BaseBinaryFile")

# Valid types for `BaseBinaryFile.from_bytes()` and similar methods:


@tp.dataclass_transform(kw_only_default=False)
class BaseBinaryFileMeta(DataclassMeta):
    """Metaclass for `BaseBinaryFileMeta` that adds dataclass wrapping."""

    def __call__(cls: type[BASE_BINARY_FILE_T], *args, **kwargs) -> BASE_BINARY_FILE_T:
        """Intercept instance creation to handle the single-argument path case, which calls `cls.from_path(path)`."""
        if len(args) == 1 and isinstance(args[0], (Path, str)) and not kwargs:
            # Call `from_path` if a single `path` argument is provided
            return cls.from_path(args[0])
        # Otherwise, proceed with the normal dataclass constructor.
        return super(BaseBinaryFileMeta, cls).__call__(*args, **kwargs)


class BaseBinaryFile(abc.ABC, metaclass=BaseBinaryFileMeta):
    """Base class for anything that is represented in binary at some point.

    Its two notable direct children are `GameFile` (which cannot be a Binder) and `Binder`.

    Includes methods for recording and automating DCX compression.
    """

    # Utility class shortcuts.
    Reader: tp.ClassVar[type[BinaryReader]] = BinaryReader
    Writer: tp.ClassVar[type[BinaryWriter]] = BinaryWriter

    # If given, extension will be enforced (before DCX is checked) when calling `.write()`.
    EXT: tp.ClassVar[str] = ""

    # If given, this `re.Pattern` will be used to check file names. Usually just `EXT` plus optional DCX extension.
    PATTERN: tp.ClassVar[re.Pattern | None] = None

    # Internal field wrapped by `path` property, which ensures any string is converted to a `Path`.
    _path: Path | None = field(init=False, repr=False)
    # Internal field wrapped by `dcx_type` property, which converts string values to `DCXType`.
    _dcx_type: DCXType | None = field(init=False, repr=False)

    # These are wrapped by properties after the class definition (below), but these serve to generate the appropriate
    # `__init__` arguments that are filtered through those property setters:

    # Records origin path of file if loaded from disk (or a `BinderEntry`). Not always available.
    # Also serves as a dummy argument for a metaclass overload trick that calls `cls.from_path(path)` instead of
    # standard dataclass keyword argument instantiation. This overload only triggers if the path (as a string or `Path`)
    # is the only argument passed to the class constructor and is NOT a keyword. If it's a keyword, a default instance
    # of the class will be constructed with `path` set to whatever the keyword value is.
    path: Path | None = field(default=None, kw_only=False)
    # Default DCX compression type for file. If `None`, then `get_game().default_dcx_type` will be used, or a
    # type-specific override of that default value if known for the `Game`.
    dcx_type: DCXType | None = field(default=None, kw_only=False)

    # All subclass fields will be keyword-only and must have default values.

    # region Read Methods

    @classmethod
    @abc.abstractmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        pass

    @abc.abstractmethod
    def to_writer(self) -> BinaryWriter:
        pass

    def __bytes__(self) -> bytes:
        """Applies `dcx_type` DCX automatically."""
        packed = bytes(self.to_writer())
        dcx_type = self._get_dcx_type()
        if dcx_type != DCXType.Null:
            return compress(packed, dcx_type)
        return packed

    def to_bytes(self) -> bytes:
        """More explicit version of `__bytes__`."""
        return bytes(self)

    @classmethod
    def to_bytes_parallel(cls, files: list[BASE_BINARY_FILE_T], calls_per_thread=10, processes: int = None) -> list[bytes | None]:
        """Use multiprocessing to pack all `BaseBinaryFile`s in parallel.

        Failed conversions will put `None` into list rather than `bytes`.
        """
        mp_args = []
        for i in range(0, (len(files) - 1) // calls_per_thread + 1, calls_per_thread):
            mp_args.append([(file,) for file in files[i:i + calls_per_thread]])
        return _process_in_parallel(_to_bytes_mp, mp_args, processes)

    @classmethod
    def from_path(cls, path: str | Path) -> tp.Self:
        _path = Path(path)
        try:
            binary_file = cls.from_bytes(BinaryReader(_path))
        except Exception:
            traceback.print_exc()
            _LOGGER.error(f"Error occurred while reading `{cls.__name__}` with path '{_path}'. See traceback.")
            raise
        if _path.suffix == ".bak":
            # Automatically removes '.bak' from `path`, for safety/convnience. User can change `path` manually.
            binary_file.path = _path.with_suffix("")
        else:
            binary_file.path = _path
        return binary_file

    @classmethod
    def from_paths_parallel(
        cls, paths: list[Path | str], calls_per_thread=10, processes: int = None
    ) -> list[BASE_BINARY_FILE_T | None]:
        """Use multiprocessing to read `BaseBinaryFile` of given subtype from each path in `paths` in parallel.

        Failed conversions will put `None` into list rather than a `BaseBinaryFile` instance.
        """
        mp_args = _chunk(paths, calls_per_thread, lambda x: [(cls, path) for path in x])
        return _process_in_parallel(_from_path_mp, mp_args, processes)

    @classmethod
    def from_bytes(cls, data: BASE_BINARY_BYTES_TYPING) -> tp.Self:
        """Load instance from binary data or binary stream (or `BinderEntry.data`)."""

        reader, dcx_type = cls._get_reader_and_dcx_type(data)

        try:
            binary_file = cls.from_reader(reader)
            binary_file.dcx_type = dcx_type
        except Exception:
            traceback.print_exc()
            _LOGGER.error(f"Error occurred while reading `{cls.__name__}` from binary data. See traceback.")
            raise
        finally:
            reader.close()
        return binary_file

    @classmethod
    def from_bytes_parallel(
        cls, data_list: list[bytes], calls_per_thread=10, processes: int = None
    ) -> list[BASE_BINARY_FILE_T | None]:
        """Use multiprocessing to read `BaseBinaryFile` of given subtype from each `bytes` in `datas` in parallel.

        Failed conversions will put `None` into list rather than a `BaseBinaryFile` instance.
        """
        mp_args = []
        for i in range(0, (len(data_list) - 1) // calls_per_thread + 1, calls_per_thread):
            mp_args.append([(cls, data) for data in data_list[i:i + calls_per_thread]])
        return _process_in_parallel(_from_bytes_mp, mp_args, processes)

    @classmethod
    def from_binder_entry(cls, binder_entry: BinderEntry) -> tp.Self:
        """Load instance from a `BinderEntry`."""
        return binder_entry.to_binary_file(cls)

    @classmethod
    def from_binder_entries_parallel(
        cls, entry_list: list[BinderEntry], calls_per_thread=10, processes: int = None
    ) -> list[BASE_BINARY_FILE_T | None]:
        """Use multiprocessing to read `BaseBinaryFile` of given subtype from each `BinderEntry` in parallel.

        Failed conversions will put `None` into list rather than a `BaseBinaryFile` instance.
        """
        mp_args = []
        for i in range(0, (len(entry_list) - 1) // calls_per_thread + 1, calls_per_thread):
            mp_args.append([(cls, entry) for entry in entry_list[i:i + calls_per_thread]])
        return _process_in_parallel(_from_binder_entry_mp, mp_args, processes)

    @classmethod
    def from_dict(cls, data: dict) -> tp.Self:
        """Load file from given `data` dictionary. Simply calls initializer by default."""
        # noinspection PyArgumentList
        return cls(**data)

    @classmethod
    def from_json(cls, json_path: str | Path) -> tp.Self:
        json_dict = read_json(json_path)
        if not isinstance(json_dict, dict):
            raise TypeError(
                f"Expected root-level dict in JSON {json_path} for class {cls.__name__}, not: {type(json_dict)}"
            )
        # TODO: Some kind of fancy recursive JSON reader that checks field types and converts dictionaries to
        #  `BaseBinaryFile` subclasses.
        file = cls.from_dict(json_dict)
        file.path = Path(json_path)
        return file

    @staticmethod
    def _get_reader_and_dcx_type(
        data: BASE_BINARY_BYTES_TYPING,
    ) -> tuple[BinaryReader, DCXType]:
        """Resolve type of `data` into a `BinaryReader` and `DCXType`."""

        # Avoid circular imports from `containers` package.
        from soulstruct.containers.entry import BinderEntry

        if isinstance(data, BinderEntry):
            reader = BinaryReader(data.get_uncompressed_data())
        elif isinstance(data, BinaryReader):
            reader = data
        else:
            reader = BinaryReader(data)

        if is_dcx(reader):
            try:
                uncompressed_data, dcx_type = decompress(reader)
            finally:
                reader.close()
            reader = BinaryReader(uncompressed_data)
        else:
            dcx_type = DCXType.Null

        return reader, dcx_type

    # endregion

    def write(self, file_path: None | str | Path = None, make_dirs=True, check_hash=False) -> list[Path]:
        """Pack game file into `bytes`, then write to given `file_path` (or `self.path` if not given).

        Missing directories in given path will be created automatically if `make_dirs` is True. Otherwise, they must
        already exist.

        Will compress with DCX automatically and add `.dcx` file extension if `.dcx_type` is not `Null`. Will also
        automatically create a `.bak` version of the `file_path`, if a backup does not already exist.

        Args:
            file_path (None, str, Path): file path to write to. Defaults to `self.path`, which is automatically set at
                instance creation if a file path is used as a source.
            make_dirs (bool): if True, any directories in `file_path` that are missing will be created. (Default: True)
            check_hash (bool): if True, file will not be written if file with same hash already exists. (Default: False)

        Returns:
            list[Path]: paths that were written to (extensions may be adjusted, e.g. for DCX). Empty if nothing new is
            written. (Child classes may write multiple files.)
        """
        _file_path = self.get_file_path(file_path)
        if make_dirs:
            _file_path.parent.mkdir(parents=True, exist_ok=True)
        packed_dcx = bytes(self)
        if check_hash and _file_path.is_file():
            if get_blake2b_hash(_file_path) == get_blake2b_hash(packed_dcx):
                return []  # don't write file
        create_bak(_file_path)
        with _file_path.open("wb") as f:
            f.write(packed_dcx)
        return [_file_path]

    def to_dict(self) -> dict[str, tp.Any]:
        """Create a dictionary from file instance. Uses `dataclasses.asdict()` by default and ignores internals."""
        # noinspection PyDataclass,PyTypeChecker
        return asdict(
            self,
            dict_factory=lambda d: {k: v for (k, v) in d if k != "_path" and k != "_dcx_type"},
        )

    def write_json(self, file_path: None | str | Path, encoding="utf-8", indent=4):
        """Create a dictionary from instance and write it to a JSON file.

        The file path will have the `.json` suffix added automatically if missing.
        """
        json_dict = self.to_dict()
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because file default `path` has not been set.")
            _file_path = self.path
        else:
            _file_path = Path(file_path)
        if _file_path.suffix != ".json":
            _file_path = _file_path.with_suffix(_file_path.suffix + ".json")
        write_json(_file_path, json_dict, indent=indent, encoding=encoding, encoder=BaseJSONEncoder)

    def create_bak(self, file_path: None | str | Path = None, make_dirs=True):
        _file_path = self.get_file_path(file_path)
        if make_dirs:
            _file_path.parent.mkdir(parents=True, exist_ok=True)
        create_bak(_file_path)

    def copy(self):
        return copy.deepcopy(self)

    def get_file_path(self, file_path: None | str | Path, add_auto_ext=False) -> Path:
        """Get default path of binary file, based on `EXT` (only if requested) and `dcx_type`."""
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because file default `path` has not been set.")
            _file_path = self.path
        else:
            _file_path = Path(file_path)

        # 0. If file path ends in '.bak', never change anything.
        if _file_path.suffix == ".bak":
            return _file_path

        # 1. Remove any existing ".dcx" extension.
        while _file_path.suffix == ".dcx":
            _file_path = _file_path.with_suffix("")  # remove '.dcx' (may add back below)

        # 2. If `EXT` is defined, add that extension to the path.
        if add_auto_ext and self.EXT and _file_path.suffix != self.EXT:
            _file_path = _file_path.with_suffix(_file_path.suffix + self.EXT)

        # 3. If `dcx_type` is not `Null`, add ".dcx" extension to the path.
        if self._get_dcx_type() != DCXType.Null and not _file_path.suffix == ".dcx":
            _file_path = _file_path.with_suffix(_file_path.suffix + ".dcx")  # add ".dcx"

        return _file_path

    @classmethod
    def get_default_extension(cls) -> str:
        if not cls.EXT:
            raise TypeError(f"Class `{cls.__name__}` has not defined `EXT`. Cannot detect default file extension.")
        ext = cls.EXT
        if cls.get_game().default_dcx_type != DCXType.Null:
            ext += ".dcx"
        return ext

    def _get_dcx_type(self) -> DCXType:
        if self.dcx_type is None:
            try:
                return self.get_game().default_dcx_type
            except ValueError:
                _LOGGER.warning(
                    f"Could not detect default DCX type for game-independent file class {self.cls_name}. "
                    f"Not using any compression."
                )
                return DCXType.Null
        return self.dcx_type

    @classmethod
    def from_bak(cls, file_path: Path | str, create_bak_if_missing=True) -> tp.Self:
        """Looks for a `.bak` version of the given path to open preferentially, or optionally creates it if missing."""
        _file_path = Path(file_path)
        bak_path = _file_path.with_name(_file_path.name + ".bak")
        if bak_path.is_file():
            binary_file = cls.from_path(bak_path)
            binary_file.path = binary_file.path.with_suffix("")  # remove ".bak" extension
            return binary_file
        else:
            binary_file = cls.from_path(_file_path)
            if create_bak_if_missing:
                create_bak(_file_path)
            return binary_file

    @classmethod
    def get_game(cls) -> Game:
        """Use `__module__` of this class to detect the `Game` it belongs to."""
        if match := re.match(_GAME_MODULE_RE, cls.__module__):
            return get_game(match.group(1))
        raise ValueError(f"Could not detect game name from module of class `{cls.__name__}`: {cls.__module__}")

    @property
    def cls_name(self) -> str:
        """Convenient property to get the name of the class without needing to use `self.__class__.__name__`."""
        return self.__class__.__name__

    @property
    def path_name(self) -> str | None:
        """Get name of `path`."""
        return self.path.name if self.path else None

    @property
    def path_stem(self) -> str | None:
        """NOTE: Like `path.stem`, this only removes the LAST suffix, e.g. 'c1000.chrbnd.dcx' -> 'c1000.chrbnd'."""
        return self.path.stem if self.path else None

    @property
    def path_minimal_stem(self) -> str | None:
        """Removes ALL suffixes from `path` name, e.g. 'c1000.chrbnd.dcx' -> 'c1000'."""
        return self.path.stem.split(".")[0] if self.path else None

    def get_dcx_type(self) -> DCXType | None:
        return self._dcx_type

    def set_dcx_type(self, dcx_type: DCXType):
        if isinstance(dcx_type, str):
            dcx_type = DCXType[dcx_type]
        elif not isinstance(dcx_type, DCXType) and dcx_type is not None:
            raise TypeError(f"DCX type must be a string or `None` or `DCXType` enum, not {dcx_type}.")
        self._dcx_type = dcx_type

    def get_field_names(self) -> list[str]:
        """Get all dataclass field names (excluding internal `_dcx_type` and `_path`)."""
        # noinspection PyDataclass,PyTypeChecker
        return [f.name for f in fields(self) if f.name != "_dcx_type" and f.name != "_path"]

    def __repr__(self) -> str:
        lines = [f"{self.cls_name}("]
        for field_name in self.get_field_names():
            lines.append(f"    {field_name}={repr(getattr(self, field_name))},")
        lines.append(")")
        return "\n".join(lines)

    # Subclass dataclasses will automatically 'restore' the default dataclass `__repr__`. This is a workaround to avoid
    # having to set `repr=False` in every dataclass decorator.
    base_repr = __repr__


# noinspection PyTypeChecker
BaseBinaryFile.dcx_type = property(
    BaseBinaryFile.get_dcx_type, BaseBinaryFile.set_dcx_type
)

# noinspection PyTypeChecker
BaseBinaryFile.path = property(
    fget=lambda self: self._path,
    fset=lambda self, path: setattr(self, "_path", Path(path) if path else None),
)


class BaseJSONEncoder(json.JSONEncoder):
    """Handles `DCXType`."""
    def default(self, o):
        if isinstance(o, DCXType):
            return o.name
        return None


def _from_path_mp(file_type: type[BASE_BINARY_FILE_T], path: Path) -> BASE_BINARY_FILE_T | None:
    """Worker for parallelized operator."""
    try:
        return file_type.from_path(path)
    except Exception as ex:
        _LOGGER.error(f"Failed to load `{file_type.__name__}` instance from path '{path}'. Error: {str(ex)}")
        return None


def _from_bytes_mp(file_type: type[BASE_BINARY_FILE_T], data: bytes) -> BASE_BINARY_FILE_T | None:
    """Worker for parallelized operator."""
    try:
        return file_type.from_bytes(data)
    except Exception as ex:
        _LOGGER.error(f"Failed to load `{file_type.__name__}` instance from data. Error: {str(ex)}")
        return None


def _from_binder_entry_mp(file_type: type[BASE_BINARY_FILE_T], entry: BinderEntry) -> BASE_BINARY_FILE_T | None:
    """Worker for parallelized operator."""
    try:
        return file_type.from_binder_entry(entry)
    except Exception as ex:
        _LOGGER.error(
            f"Failed to load `{file_type.__name__}` instance from BinderEntry '{entry.name}'. Error: {str(ex)}"
        )
        return None


def _to_bytes_mp(file: BASE_BINARY_FILE_T) -> bytes | None:
    """Worker for parallelized operator."""
    try:
        return bytes(file)
    except Exception as ex:
        _LOGGER.error(f"Failed to pack `{file.cls_name}` instance with path name '{file.path_name}'. Error: {str(ex)}")
        return None


def _chunk(lst: list, m: int, tuplefy: tp.Callable) -> list[list]:
    return [tuplefy(lst[i:i + m]) for i in range(0, len(lst), m)]


def _process_in_parallel(
    worker: tp.Callable, all_worker_args: list[tp.Any], processes: int | None
) -> list[BASE_BINARY_FILE_T]:
    returned_data = []
    with multiprocessing.Pool(processes=processes) as pool:
        for worker_args in all_worker_args:
            returned_data.extend(pool.starmap(worker, worker_args))  # blocks here until all done
    return returned_data
