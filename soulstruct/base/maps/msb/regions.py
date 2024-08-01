from __future__ import annotations

__all__ = ["BaseMSBRegion"]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import BaseMSBRegionSubtype, MSBSupertype
from .msb_entry import MSBEntry
from .region_shapes import *

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList


_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True, eq=False, repr=False)
class BaseMSBRegion(MSBEntry, abc.ABC):

    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype] = MSBSupertype.REGIONS

    # Further specify subtype enum type.
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBRegionSubtype]

    # Shape enum mapping. This is correct for all games until Composite shape added.
    SHAPE_TYPES: tp.ClassVar[dict[int, type[MSBRegionShape]]] = {
        0: MSBRegionPoint,
        1: MSBRegionCircle,
        2: MSBRegionSphere,
        3: MSBRegionCylinder,
        4: MSBRegionRect,
        5: MSBRegionBox,
    }

    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: Vector3 = field(default_factory=Vector3.zero)
    entity_id: int = -1
    shape: MSBRegionShape = field(default_factory=MSBRegionPoint)  # default is Point

    @property
    def shape_type_int(self) -> int:
        return self.shape.SHAPE_TYPE.value

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        """In later games, regions are more like spatial Events and have references to other MSB entries, or may have
        Composite shapes that require child Region deferencing."""
        pass
