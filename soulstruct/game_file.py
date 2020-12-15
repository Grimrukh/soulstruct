__all__ = ["GameFile"]

import abc
import io
import json
import typing as tp
from pathlib import Path

from soulstruct.dcx import DCX
from soulstruct.utilities import create_bak


class GameFile(abc.ABC):

    EXT = ""  # if given, this file extension will be enforced (before DCX is checked) when calling `.write()`
    Typing = tp.Union[str, Path, bytes, io.BufferedIOBase]  # all valid `GameFile` source types
    Types = (str, Path, bytes, io.BufferedIOBase)

    def __init__(
        self,
        file_source: tp.Union[None, str, Path, bytes, io.BufferedIOBase] = None,
        dcx_magic: tuple[int, int] = None,
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
        try:
            # Pair of DCX magic values, or empty tuple to not use DCX.
            self.dcx_magic = tuple(dcx_magic) if dcx_magic is not None else ()
            if len(self.dcx_magic) != 2 or not all(isinstance(m, int) for m in self.dcx_magic):
                raise ValueError
        except (ValueError, TypeError):
            raise ValueError(f"`dcx_magic` should be empty (or None) or a sequence of two values.")

        self.path = None  # type: tp.Optional[Path]

        if file_source is None:
            return

        if isinstance(file_source, dict):
            self.load_dict(file_source)
            return
        if isinstance(file_source, (str, Path)):
            self.path = Path(file_source)
            if self.path.suffix == ".json":
                with self.path.open(self.path, "r") as j:
                    self.load_dict(json.load(j))
                    return
            else:
                buffer = self.path.open("rb")
        elif isinstance(file_source, bytes):
            buffer = io.BytesIO(file_source)
        elif isinstance(file_source, io.BufferedIOBase):
            buffer = file_source
        else:
            raise TypeError(f"Invalid `GameFile` source type: {type(file_source)}")

        if self._is_dcx(buffer):
            if self.dcx_magic:
                raise ValueError("Cannot manually set `dcx_magic` before reading a DCX file source.")
            data, self.dcx_magic = DCX.get_data_and_magic(buffer)
            buffer = io.BytesIO(data)

        self.unpack(buffer, **kwargs)

    @abc.abstractmethod
    def unpack(self, buffer: io.BufferedIOBase, **kwargs):
        """Unpack game file from given buffer, using various `BinaryStruct`s defined in the class."""

    def load_dict(self, data: dict):
        """Load game file from given `data` dictionary. Not supported by default."""
        raise TypeError(f"`{self.__class__.__name__}` class does not support JSON/dictionary data.")

    @abc.abstractmethod
    def pack(self, **kwargs) -> bytes:
        """Pack game file into `bytes`, using various `BinaryStruct`s defined in the class."""

    def as_dict(self) -> dict:
        """Create a dictionary from `GameFile` instance. Not supported by default."""
        raise TypeError(f"`{self.__class__.__name__}` class does not support JSON/dictionary data.")

    def write(self, file_path: tp.Union[None, str, Path], make_dirs=True, **pack_kwargs):
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

    def write_json(self, file_path: tp.Union[None, str, Path]):
        """Create a dictionary from `GameFile` instance. Requires `.as_dict()` to be supported.

        The file path will have the `.json` suffix added automatically.
        """
        json_dict = self.as_dict()
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because `GameFile` default path has not been set.")
            file_path = self.path
        file_path = Path(file_path)
        if file_path.suffix != ".json":
            file_path = file_path.with_suffix(file_path.suffix + ".json")
        with file_path.open("w") as j:
            json.dump(json_dict, j, indent=4)

    def _get_file_path(self, file_path: tp.Union[None, str, Path]) -> Path:
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because `GameFile` default path has not been set.")
            file_path = self.path
        file_path = Path(file_path)
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
