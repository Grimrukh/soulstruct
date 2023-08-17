from __future__ import annotations

__all__ = ["BaseMSBPart"]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.maths import Vector3
from soulstruct.base.maps.msb.utils import GroupBitSet

from .enums import BaseMSBPartSubtype, MSBSupertype
from .models import BaseMSBModel
from .msb_entry import MSBEntry

try:
    Self = tp.Self
except AttributeError:
    Self = "BaseMSBPart"

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True, eq=False, repr=False)
class BaseMSBPart(MSBEntry, abc.ABC):

    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype] = MSBSupertype.PARTS
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBPartSubtype]
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = None
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model"]

    model: BaseMSBModel = None
    entity_id: int = -1
    sib_path: str = ""
    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: Vector3 = field(default_factory=Vector3.zero)  # XZY-order Euler angles in radians
    scale: Vector3 = field(default_factory=lambda: Vector3.one())

    # Concrete, sized `GroupBitSet` subclass is overridden per game.
    draw_groups: GroupBitSet = field(default_factory=set)
    display_groups: GroupBitSet = field(default_factory=set)

    _model_index: int = None

    # Game structures diverge too much for useful read/write base methods here.

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        """Defined by most subclasses."""
        self._consume_index(entry_lists, "MODEL_PARAM_ST", "model")

    def set_auto_sib_path(self, map_stem: str):
        """Most `MSBPart` subclasses have the same SIB path. The `layout.SIB` name might get a prefix.

        The game's base class can typically implement it, especially in later games.

        Empty `SIB_PATH_TEMPLATE` is permitted and indicates that it should be empty for that type.
        """
        if self.SIB_PATH_TEMPLATE is None:
            raise TypeError(f"Cannot set `sib_path` automatically for type `{self.cls_name}`.")
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem)
