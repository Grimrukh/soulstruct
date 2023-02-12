from __future__ import annotations

__all__ = ["ITEMLOT_LVDEP_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.params.enums import *

from .dynamics import ItemLotReference


# noinspection PyDataclass
@dataclass(slots=True)
class ITEMLOT_LVDEP_PARAM_ST(ParamRow):
    ItemCategory: ITEMLOT_LVDEP_ITEMCATEGORY = ParamField(
        int, "itemCategory", default=0,
        tooltip="TODO",
    )
    Item: int = ParamField(
        int, "itemId", default=0, dynamic_callback=ItemLotReference(0),
        tooltip="TODO",
    )
