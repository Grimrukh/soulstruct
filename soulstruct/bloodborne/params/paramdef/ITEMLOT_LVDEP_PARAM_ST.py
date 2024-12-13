from __future__ import annotations

__all__ = ["ITEMLOT_LVDEP_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class ITEMLOT_LVDEP_PARAM_ST(ParamRow):
    ItemCategory: int = ParamField(
        int, "itemCategory", ITEMLOT_LVDEP_ITEMCATEGORY, default=0,
        tooltip="TODO",
    )
    Item: int = ParamField(
        int, "itemId", default=0,
        tooltip="TODO",
    )
