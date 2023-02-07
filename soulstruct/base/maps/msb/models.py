from __future__ import annotations

__all__ = ["BaseMSBModel"]

import abc
import typing as tp
from dataclasses import dataclass

from soulstruct.utilities.binary import *

from .msb_entry import MSBEntry

try:
    Self = tp.Self
except AttributeError:
    Self = "BaseMSBModel"


@dataclass(slots=True)
class BaseMSBModel(MSBEntry, abc.ABC):
    """Base class used by all MSB models. (They used to not even subclass this per subtype, but now do.)"""

    NAME_ENCODING: tp.ClassVar[str] = ""
    NULL: tp.ClassVar[bytes] = b"\0"
    EMPTY_SIB_PATH: tp.ClassVar[bytes] = b"\0"
    SIB_PATH_STEM: tp.ClassVar[str] = ""

    sib_path: str = ""

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        """Models have no supertype or subtype data, just a header."""
        entry_offset = reader.position
        kwargs = cls.unpack_header(reader, entry_offset)
        return cls(**kwargs)

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)
        header_subtype_int = header.pop("subtype_int")
        if header_subtype_int != cls.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB event subtype index for `{cls.__name__}`: {header_subtype_int}")
        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        sib_path = reader.unpack_string(offset=entry_offset + header.pop("sib_path"), encoding=cls.NAME_ENCODING)
        return header.to_dict(ignore_underscore_prefix=True) | {"name": name, "sib_path": sib_path}

    @classmethod
    def unpack_supertype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        raise TypeError("MSB models contain no supertype data.")

    @classmethod
    def unpack_sunrtype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        raise TypeError("MSB models contain no subtype data.")

    def to_msb_writer(
        self,
        writer: BinaryWriter,
        supertype_index: int,
        subtype_index: int,
        entry_lists: dict[str, list[MSBEntry]],
        instance_count: int = 0,
    ):
        self.pack_header(writer, supertype_index, subtype_index, entry_lists, instance_count)

    def pack_header(
        self,
        writer: BinaryWriter,
        supertype_index: int,
        subtype_index: int,
        entry_lists: [dict[str, list[MSBEntry]]],
        instance_count: int = 0,
    ):
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            name_offset=RESERVED,
            subtype_int=self.SUBTYPE_ENUM.value,
            _subtype_index=subtype_index,
            sib_path_offset=RESERVED,
            _instance_count=instance_count,
        )
        writer.fill_with_position("name_offset", self)
        packed_name = self.name.encode(self.NAME_ENCODING) + self.NULL
        writer.append(packed_name)
        writer.fill_with_position("sib_path_offset", self)
        if self.sib_path:
            packed_sib_path = self.sib_path.encode(self.NAME_ENCODING) + self.NULL
        else:
            packed_sib_path = self.EMPTY_SIB_PATH
        while len(packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"
        writer.append(packed_sib_path)

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        # TODO: Do some models use generic sib paths?
        return {"name": self.name, "sib_path": self.sib_path}

    def __repr__(self):
        data = self.to_dict(ignore_defaults=True)
        if data:
            fields = "\n    ".join(f"{k}={repr(v)}," for k, v in data.items())
            return (
                f"{self.__class__.__name__}(\n"
                f"    name={repr(self.name)},\n"
                f"    {fields}\n"
                f")"
            )
        return f"{self.__class__.__name__}(name={repr(self.name)})"


# TODO: Put in read methods of appropriate classes. Or __post_init__.
class __BaseMSBGeometryModel(BaseMSBModel):

    def __init__(self, source=None, **kwargs):
        """Additionally Requires `map_id` if `source` is None."""
        if source is None and "sib_path" not in kwargs and ("map_id" not in kwargs or "name" not in kwargs):
            raise ValueError(
                f"`name` and `map_id` must be given to `{self.__class__.__name__}` if `sib_path` is not given."
            )
        super().__init__(source, **kwargs)
