__all__ = ["GameFile", "GameFolder", "InvalidGameFileTypeError"]

import abc
import copy
import io
import json
import logging
import typing as tp
from pathlib import Path

from soulstruct.exceptions import SoulstructError
from soulstruct.containers.dcx import DCX
from soulstruct.utilities import create_bak

_LOGGER = logging.getLogger(__name__)


class InvalidGameFileTypeError(SoulstructError):
    """Exception raised from an unhandled `file_source` type passed to `GameFile` constructor."""


class GameFile(abc.ABC):
    """Python structure for a file in a FromSoftware game installation."""

    EXT = ""  # if given, this file extension will be enforced (before DCX is checked) when calling `.write()`
    Typing = tp.Union[str, Path, bytes, io.BufferedIOBase]  # all valid `GameFile` source types
    Types = (str, Path, bytes, io.BufferedIOBase)

    def __init__(
        self,
        file_source: tp.Union[None, str, Path, bytes, io.BufferedIOBase] = None,
        dcx_magic: tuple[int, int] = (),
        **kwargs,
    ):
        """Base class for a game file, with key methods and automatic DCX detection.

        Args:
            file_source (None, str, Path, bytes, BufferedIOBase): a file path, `bytes` object, or binary stream to load
                the file from. It will be checked for DCX first. Set to None (default) to create a default instance.
            dcx_magic (None, tuple): optional pair of DCX magic values to manually specify the DCX. Only permitted for
                `file_source` values that are not already DCX-compressed. (If you want to change the DCX for some
                reason, set `.dcx_magic` directly after the instance is created.)
            kwargs: keyword arguments to pass on to `unpack` or `load_dict`, depending on the source type.
        """
        self._dcx_magic = ()
        self.dcx_magic = dcx_magic

        self.path = None  # type: tp.Optional[Path]

        if file_source is None:
            return

        try:
            buffer = self._handle_other_source_types(file_source, **kwargs)
            if buffer is None:
                return
        except InvalidGameFileTypeError:
            if isinstance(file_source, dict):
                self.load_dict(file_source.copy())
                return
            if isinstance(file_source, (str, Path)):
                self.path = Path(file_source)
                if self.path.suffix == ".json":
                    with self.path.open("r") as j:
                        self.load_dict(json.load(j))
                        return
                else:
                    buffer = self.path.open("rb")
            elif isinstance(file_source, bytes):
                buffer = io.BytesIO(file_source)
            elif isinstance(file_source, io.BufferedIOBase):
                buffer = file_source
            else:
                raise InvalidGameFileTypeError(f"Invalid `GameFile` source type: {type(file_source)}")

        if self._is_dcx(buffer):
            if self.dcx_magic:
                buffer.close()
                raise ValueError("Cannot manually set `dcx_magic` before reading a DCX file source.")
            try:
                data, self.dcx_magic = DCX.get_data_and_magic(buffer)
            finally:
                buffer.close()
            buffer = io.BytesIO(data)

        try:
            self.unpack(buffer, **kwargs)
        except Exception:
            _LOGGER.error(f"Error occurred while parsing game file: {self.path}. See traceback.")
            raise
        finally:
            buffer.close()

    def _handle_other_source_types(self, file_source, **kwargs) -> tp.Optional[io.BufferedIOBase]:
        """Override this to initialize `GameFile` subclass from other types of `file_source`. This function will be
        called before the standard `GameFile.Types` are checked.

        If a `io.BufferedIOBase` object is returned, the constructor will continue with unpacking from that buffer.
        Otherwise, it will return without calling `.unpack()`.
        """
        raise InvalidGameFileTypeError(f"Invalid `GameFile` source type: {type(file_source)}")

    @abc.abstractmethod
    def unpack(self, buffer: io.BufferedIOBase, **kwargs):
        """Unpack game file from given buffer, using various `BinaryStruct`s defined in the class."""

    def load_dict(self, data: dict):
        """Load game file from given `data` dictionary (which is a copy of the source). Not supported by default."""
        raise TypeError(f"`{self.__class__.__name__}` class does not support JSON/dictionary input.")

    @abc.abstractmethod
    def pack(self, **kwargs) -> bytes:
        """Pack game file into `bytes`, using various `BinaryStruct`s defined in the class."""

    def to_dict(self, **kwargs) -> dict:
        """Create a dictionary from `GameFile` instance. Not supported by default."""
        raise TypeError(f"`{self.__class__.__name__}` class does not support JSON/dictionary output.")

    def write(self, file_path: tp.Union[None, str, Path] = None, make_dirs=True, **pack_kwargs):
        """Pack game file into `bytes`, then write to given `file_path` (or `self.path` if not given).

        Missing directories in given path will be created automatically if `make_dirs` is True. Otherwise, they must
        already exist.

        Will compress with DCX automatically and add `.dcx` file extension if `.dcx_magic` is defined. Will also
        automatically create a `.bak` version of the `file_path`, if a backup does not already exist.

        Args:
            file_path (None, str, Path): file path to write to. Defaults to `self.path`, which is automatically set at
                instance creation if a file path is used as a source.
            make_dirs (bool): if True, any directories in `file_path` that are missing will be created.
            pack_kwargs: extra keyword arguments to pass to `.pack()`.
        """
        file_path = self._get_file_path(file_path)
        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        create_bak(file_path)
        if self.dcx_magic:
            packed = DCX(self.pack(**pack_kwargs), magic=self.dcx_magic).pack()
        else:
            packed = self.pack()
        with file_path.open("wb") as f:
            f.write(packed)

    def write_json(self, file_path: tp.Union[None, str, Path], encoding="utf-8", indent=4, **kwargs):
        """Create a dictionary from `GameFile` instance. Requires `.as_dict()` to be supported.

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
        with file_path.open("w", encoding=encoding) as j:
            json.dump(json_dict, j, indent=indent)

    def copy(self):
        return copy.deepcopy(self)

    def _get_file_path(self, file_path: tp.Union[None, str, Path]) -> Path:
        """Get default path of binary file, based on `EXT` and `dcx_magic`."""
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because `GameFile` default path has not been set.")
            file_path = self.path
        file_path = Path(file_path)
        if file_path.suffix == ".dcx":
            file_path = file_path.with_name(file_path.stem)  # remove '.dcx' (may add back below)
        if self.EXT and file_path.suffix != self.EXT:
            file_path = file_path.with_suffix(file_path.suffix + self.EXT)
        if self.dcx_magic and not file_path.suffix == ".dcx":
            file_path = file_path.with_suffix(file_path.suffix + ".dcx")  # add ".dcx"
        elif not self.dcx_magic and file_path.suffix == ".dcx":
            file_path = file_path.with_name(file_path.stem)  # remove ".dcx"
        return file_path

    @staticmethod
    def _is_dcx(buffer: io.BufferedIOBase):
        offset = buffer.tell()
        is_dcx = buffer.read(4) == b"DCX\0"
        buffer.seek(offset)
        return is_dcx

    @property
    def dcx_magic(self):
        return self._dcx_magic

    @dcx_magic.setter
    def dcx_magic(self, value: tp.Optional[tuple[int, int]]):
        try:
            # Pair of DCX magic values, or empty tuple to not use DCX.
            value = tuple(value) if value is not None else ()
            if value:
                if len(value) != 2:
                    raise ValueError(f"Expected DXC `dcx_magic` to be a sequence of two integers.")
                if value[0] not in {36, 68}:
                    raise ValueError(f"Expected `dcx_magic[0]` (header offset 0x16) to be 36 or 68, not {value[0]}.")
                if value[1] not in {44, 76}:
                    raise ValueError(f"Expected `dcx_magic[1]` (header offset 0x1a) to be 44 or 76, not {value[1]}.")
        except (ValueError, TypeError):
            raise ValueError(f"`dcx_magic` should be empty (or None) or a sequence of two integers, not {value}.")
        self._dcx_magic = value


class GameFolder(abc.ABC):
    """Python structure for a folder of files in a FromSoftware installation. Implementation is much more flexible."""
