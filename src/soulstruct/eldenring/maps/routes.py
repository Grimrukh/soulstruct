"""New supertype of MSB entry that seems connected to sound-muffling regions."""
from __future__ import annotations

__all__ = [
    "MSBRoute",
    "MSBMufflingPortalLink",
    "MSBMufflingBoxLink",
    "MSBOtherRoute",
]

from dataclasses import dataclass, field
import typing as tp

from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.utilities.binary import *

from .enums import MSBSupertype, MSBRouteSubtype


class RouteHeaderStruct(MSBHeaderStruct):
    name_offset: long
    route_unkh_08: int
    route_unkh_0c: int
    _subtype_int: int
    subtype_index: int  # NOTE: unknown behavior for (likely unused) `OtherRoute` so is stored manually
    _pad1: bytes = binary_pad(0x68, init=False)

    @classmethod
    def preprocess_write_kwargs(
        cls,
        entry: MSBEntry,
        entry_lists: dict[str, IDList[MSBEntry]],
        kwargs: dict[str, tp.Any],
    ) -> None:
        super(RouteHeaderStruct, cls).preprocess_write_kwargs(entry, entry_lists, kwargs)
        kwargs.pop("supertype_index")


@dataclass(slots=True, eq=False, repr=False)
class MSBRoute(MSBEntry):

    SUPERTYPE_ENUM: tp.ClassVar = MSBSupertype.ROUTES
    HEADER_STRUCT = RouteHeaderStruct
    STRUCTS = {}  # no other route structs

    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"

    route_unkh_08: int = 0
    route_unkh_0c: int = 0


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

    TODO: Apparently, the `subtype_index` of these entries does not behave as normal. I used to store it, but haven't
     been bothered retaining that since the last overhaul. I don't think the game ever instantiates this anyway.
    """
    SUBTYPE_ENUM: tp.ClassVar[MSBRouteSubtype] = MSBRouteSubtype.OtherRoute
