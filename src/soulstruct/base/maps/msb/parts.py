from __future__ import annotations

__all__ = ["BaseMSBPart"]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.utilities.maths import EulerDeg, Vector3
from soulstruct.base.maps.msb.utils import BitSet

from .enums import BaseMSBPartSubtype, MSBSupertype
from .models import BaseMSBModel
from .msb_entry import MSBEntry

if tp.TYPE_CHECKING:
    from soulstruct.utilities.misc import IDList


_LOGGER = logging.getLogger(__name__)

BIT_SET_T = tp.TypeVar("BIT_SET_T", bound=BitSet)


@dataclass(slots=True, eq=False, repr=False)
class BaseMSBPart(MSBEntry, abc.ABC, tp.Generic[BIT_SET_T]):
    """Base class for all MSB Parts entries in all games. Includes a generic parameter for `BitSet` type."""

    SUPERTYPE_ENUM: tp.ClassVar[MSBSupertype] = MSBSupertype.PARTS
    SUBTYPE_ENUM: tp.ClassVar[BaseMSBPartSubtype]
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = None
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model"]

    BIT_SET_TYPE: tp.ClassVar[type[BitSet]]  # matches `BIT_SET_T`

    model: BaseMSBModel = None
    entity_id: int = -1
    sib_path: str = ""
    translate: Vector3 = field(default_factory=Vector3.zero)
    rotate: EulerDeg = field(default_factory=EulerDeg.zero)
    scale: Vector3 = field(default_factory=lambda: Vector3.one())

    # Sized `BitSet` subclass is overridden per concrete game-specific subclass.
    draw_groups: BIT_SET_T = field(default_factory=set)
    display_groups: BIT_SET_T = field(default_factory=set)

    _model_index: int = None

    # Game structures diverge too much for useful read/write base methods here.

    def indices_to_objects(self, entry_lists: dict[str, IDList[MSBEntry]]):
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

    def has_identity_transform(self) -> bool:
        return self.translate == Vector3.zero() and self.rotate == Vector3.zero() and self.scale == Vector3.one()
