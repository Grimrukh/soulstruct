from __future__ import annotations

__all__ = ["BaseMSBModel"]

import abc
import typing as tp
from dataclasses import dataclass
from string import Formatter

from soulstruct.utilities.binary import *

from .enums import BaseMSBModelSubtype, MSBSupertype
from .msb_entry import MSBEntry

try:
    Self = tp.Self
except AttributeError:
    Self = "BaseMSBModel"


@dataclass(slots=True, eq=False, repr=False)
class BaseMSBModel(MSBEntry, abc.ABC):
    """Base class used by all MSB models. (They used to not even subclass this per subtype, but now do.)"""

    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype] = MSBSupertype.MODELS
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBModelSubtype]
    NAME_ENCODING: tp.ClassVar[str] = ""

    NULL: tp.ClassVar[bytes] = b"\0"
    EMPTY_SIB_PATH: tp.ClassVar[bytes] = b"\0"
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = ""

    sib_path: str = ""

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        """Models have no supertype or subtype data, just a header."""
        entry_offset = reader.position
        kwargs = cls.unpack_header(reader, entry_offset)
        cls.SETATTR_CHECKS_DISABLED = True
        msb_model = cls(**kwargs)
        cls.SETATTR_CHECKS_DISABLED = False
        return msb_model

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)
        header_subtype_int = header.pop("_subtype_int")
        if header_subtype_int != cls.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB event subtype index for `{cls.__name__}`: {header_subtype_int}")
        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        sib_path = reader.unpack_string(offset=entry_offset + header.pop("sib_path_offset"), encoding=cls.NAME_ENCODING)
        return header.to_dict(ignore_underscore_prefix=True) | {"name": name, "sib_path": sib_path}

    @classmethod
    def unpack_supertype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        raise TypeError("MSB models contain no supertype data.")

    @classmethod
    def unpack_subtype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        raise TypeError("MSB models contain no subtype data.")

    def to_msb_writer(
        self,
        writer: BinaryWriter,
        supertype_index: int,
        subtype_index: int,
        entry_lists: dict[str, list[MSBEntry]],
        instance_count: int = 0,
    ):
        self.pack_header(writer, writer.position, supertype_index, subtype_index, entry_lists, instance_count)

    def pack_header(
        self,
        writer: BinaryWriter,
        entry_offset: int,
        supertype_index: int,
        subtype_index: int,
        entry_lists: [dict[str, list[MSBEntry]]],
        instance_count: int = 0,
    ):
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            name_offset=RESERVED,
            _subtype_int=self.SUBTYPE_ENUM.value,
            _subtype_index=subtype_index,
            sib_path_offset=RESERVED,
            _instance_count=instance_count,
        )
        writer.fill("name_offset", writer.position - entry_offset, obj=self)
        packed_name = self.name.encode(self.NAME_ENCODING) + self.NULL
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=self)
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

    def set_auto_sib_path(self, **format_kwargs):
        """Some `MSBModel` subclasses can auto-generate SIB path from `SIB_PATH_TEMPLATE` and `format_kwargs`.

        Tries to format `SIB_PATH_TEMPLATE` with just `self.name` by default. Typically, if more kwargs are required,
        this method is overridden, but it should still work if I forget (and extra `kwargs` are harmless).
        """
        if not self.SIB_PATH_TEMPLATE:
            raise TypeError(f"Cannot set `sib_path` automatically for type `{self.cls_name}`.")
        # Otherwise, try to format with just model `name`.
        try:
            self.sib_path = self.SIB_PATH_TEMPLATE.format(name=self.name, **format_kwargs)
        except KeyError:
            keys = [i[1] for i in Formatter().parse(self.SIB_PATH_TEMPLATE) if i[1] is not None and i[1] != "name"]
            raise TypeError(f"Setting `sib_path` automatically for type `{self.cls_name}` requires more kwargs: {keys}")

    def get_model_file_stem(self, map_stem: str):
        """Allows subclasses to depend on `map_stem` when generating model file stem. Default is just name."""
        return self.name
