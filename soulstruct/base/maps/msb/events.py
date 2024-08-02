from __future__ import annotations

__all__ = ["BaseMSBEvent"]

import abc
import typing as tp
from dataclasses import dataclass

from .enums import BaseMSBEventSubtype, MSBSupertype
from .msb_entry import MSBEntry

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList


@dataclass(slots=True, eq=False, repr=False)
class BaseMSBEvent(MSBEntry, abc.ABC):
    """Parent class for MSB events, which describe various things that occur in maps (often attached to Regions)."""

    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype] = MSBSupertype.EVENTS
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBEventSubtype]
    NAME_ENCODING: tp.ClassVar[str] = ""
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region"]

    entity_id: int = -1
    attached_part: MSBEntry = None
    attached_region: MSBEntry = None
    
    # Temporary indices used during unpacking, before `MSBEntry` instances above can be assigned.
    # Set to `None` once consumed.
    _attached_part_index: int = None
    _attached_region_index: int = None

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "attached_part")
        self._consume_index(entry_lists, "POINT_PARAM_ST", "attached_region")
