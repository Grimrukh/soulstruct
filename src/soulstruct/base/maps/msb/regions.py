from __future__ import annotations

__all__ = ["BaseMSBRegion"]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.maths import Vector3

from .enums import BaseMSBRegionSubtype, MSBSupertype
from .msb_entry import MSBEntry
from .region_shapes import *

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList


_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True, eq=False, repr=False)
class BaseMSBRegion(MSBEntry, abc.ABC):

    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype] = MSBSupertype.REGIONS

    # Further specify subtype enum type.
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBRegionSubtype]

    # Shape enum mapping. This is correct for all games until Composite shape added.
    SHAPE_CLASSES: tp.ClassVar[dict[int, type[RegionShape]]] = {
        0: PointShape,
        1: CircleShape,
        2: SphereShape,
        3: CylinderShape,
        4: RectShape,
        5: BoxShape,
    }

    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: Vector3 = field(default_factory=Vector3.zero)
    entity_id: int = -1
    shape: RegionShape = field(default_factory=PointShape)  # default is Point

    @property
    def shape_type(self) -> RegionShapeType:
        return self.shape.SHAPE_TYPE

    @property
    def shape_type_int(self) -> int:
        """For `BinaryStruct` easy access."""
        return self.shape.SHAPE_TYPE.value

    def has_identity_transform(self) -> bool:
        return self.translate == Vector3.zero() and self.rotate == Vector3.zero()

    def change_shape_type(self, shape_type: RegionShapeType):
        """Change the shape type of this region, attempting to copy over dimensions as able."""
        if self.shape.SHAPE_TYPE == shape_type:
            return  # no change
        try:
            old_dimensions = self.shape.get_three_dimensions()
        except ValueError:
            old_dimensions = (1.0, 1.0, 1.0)  # CompositeShape

        self.shape = self.SHAPE_CLASSES[shape_type.value]()
        try:
            self.shape.set_three_dimensions(old_dimensions)
        except ValueError:
            pass  # CompositeShape

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
        """In later games, regions are more like spatial Events and have references to other MSB entries, or may have
        Composite shapes that require child Region deferencing."""
        pass
