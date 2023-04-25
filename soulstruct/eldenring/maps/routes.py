"""New supertype of MSB entry that seems connected to sound-muffling regions."""
from __future__ import annotations

__all__ = ["MSBRoute", "MSBMufflingPortalLink", "MSBMufflingBoxLink", "MSBOtherRoute"]

from dataclasses import dataclass, field
import typing as tp

from soulstruct.base.maps.msb.msb_entry import MSBEntry
from soulstruct.utilities.binary import *
from soulstruct.utilities.text import pad_chars

from .enums import MSBRouteSubtype

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBRoute"


@dataclass(slots=True, eq=False, repr=False)
class MSBRoute(MSBEntry):

    NAME_ENCODING = "utf-16-le"

    @dataclass(slots=True)
    class SUPERTYPE_HEADER_STRUCT(BinaryStruct):
        name_offset: long
        route_unkh_08: int
        route_unkh_0c: int
        _subtype_int: int
        _subtype_index: int  # NOTE: unknown behavior for (likely unused) `OtherRoute` so is stored manually
        _pad1: bytes = field(init=False, **BinaryPad(0x68))

    route_unkh_08: int = 0
    route_unkh_0c: int = 0

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        """Regions do not have 'supertype data'. Just a header (with some supertype data) and optional subtype data."""
        entry_offset = reader.position
        kwargs = cls.unpack_header(reader, entry_offset)

        # No supertype or subtype data.

        cls.SETATTR_CHECKS_DISABLED = True
        msb_route = cls(**kwargs)
        cls.SETATTR_CHECKS_DISABLED = False
        return msb_route


@dataclass(slots=True, eq=False, repr=False)
class MSBMufflingPortalLink(MSBRoute):
    """Something to do with sound-muffling portals (a region subtype).

    No subtype data, or indeed any additional logic.
    """
    SUBTYPE_ENUM: tp.ClassVar[MSBRouteSubtype] = MSBRouteSubtype.MufflingPortalLink


@dataclass(slots=True, eq=False, repr=False)
class MSBMufflingBoxLink(MSBRoute):
    """Something to do with sound-muffling boxes (a region subtype).

    No subtype data, or indeed any additional logic.
    """
    SUBTYPE_ENUM: tp.ClassVar[MSBRouteSubtype] = MSBRouteSubtype.MufflingBoxLink


@dataclass(slots=True, eq=False, repr=False)
class MSBOtherRoute(MSBRoute):
    """Unknown. Uses stored subtype index rather than auto-incremented one.

    Likely unused.
    """
    SUBTYPE_ENUM: tp.ClassVar[MSBRouteSubtype] = MSBRouteSubtype.OtherRoute

    stored_subtype_index: int = 0  # stored manually for `OtherRoute`; otherwise, auto-set as usual

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)
        header_subtype_int = header.pop("_subtype_int")
        if header_subtype_int != cls.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB event subtype index for `{cls.__name__}`: {header_subtype_int}")
        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        subtype_index = header.pop("_subtype_index")
        return header.to_dict(ignore_underscore_prefix=True) | {"name": name, "stored_subtype_index": subtype_index}

    def pack_header(
        self,
        writer: BinaryWriter,
        entry_offset: int,
        supertype_index: int,
        subtype_index: int,
        entry_lists: [dict[str, list[MSBEntry]]],
    ):
        header_offset = writer.position
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            name_offset=RESERVED,
            _supertype_index=supertype_index,
            _subtype_int=self.SUBTYPE_ENUM.value,
            _subtype_index=self.stored_subtype_index,
            supertype_data_offset=RESERVED,
            subtype_data_offset=RESERVED,
        )
        writer.fill("name_offset", writer.position - header_offset, obj=self)
        writer.append(pad_chars(self.name, encoding=self.NAME_ENCODING, alignment=4))
