
__all__ = ["BaseMSBEvent"]

import abc
import typing as tp
from dataclasses import dataclass

from soulstruct.utilities.text import pad_chars
from soulstruct.utilities.binary import *

from .msb_entry import MSBEntry

try:
    Self = tp.Self
except AttributeError:
    Self = "BaseMSBEvent"


@dataclass(slots=True)
class BaseMSBEvent(MSBEntry, abc.ABC):
    """Parent class for MSB events, which describe various things that occur in maps (often attached to Regions)."""

    NAME_ENCODING: tp.ClassVar[str] = ""

    entity_id: int = -1
    attached_part: MSBEntry = None
    attached_region: MSBEntry = None
    
    # Temporary indices used during unpacking, before `MSBEntry` instances above can be assigned.
    # Set to `None` once consumed.
    _attached_part_index: int | None = None
    _attached_region_index: int | None = None

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "attached_part")
        self._consume_index(entry_lists, "POINT_PARAM_ST", "attached_region")
