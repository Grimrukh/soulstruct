from __future__ import annotations

__all__ = ["RITUAL_REQUIRED_MAT_PARAM"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class RITUAL_REQUIRED_MAT_PARAM(ParamRow):
    UseSoul: int = ParamField(
        uint32, "useSoul", default=0,
        tooltip="TODO",
    )
    MaterialItemID1: int = ParamField(
        uint32, "materialItemId_1", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialItemID2: int = ParamField(
        uint32, "materialItemId_2", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialItemID3: int = ParamField(
        uint32, "materialItemId_3", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialItemID4: int = ParamField(
        uint32, "materialItemId_4", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialItemID5: int = ParamField(
        uint32, "materialItemId_5", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialCount1: int = ParamField(
        uint32, "num_1", default=0,
        tooltip="TODO",
    )
    MaterialCount2: int = ParamField(
        uint32, "num_2", default=0,
        tooltip="TODO",
    )
    MaterialCount3: int = ParamField(
        uint32, "num_3", default=0,
        tooltip="TODO",
    )
    MaterialCount4: int = ParamField(
        uint32, "num_4", default=0,
        tooltip="TODO",
    )
    MaterialCount5: int = ParamField(
        uint32, "num_5", default=0,
        tooltip="TODO",
    )
