from __future__ import annotations

__all__ = ["RITUAL_REQUIRED_MAT_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class RITUAL_REQUIRED_MAT_PARAM(ParamRow):
    UseSoul: int = ParamField(
        uint, "useSoul", default=0,
        tooltip="TODO",
    )
    MaterialItemID1: int = ParamField(
        uint, "materialItemId_1", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialItemID2: int = ParamField(
        uint, "materialItemId_2", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialItemID3: int = ParamField(
        uint, "materialItemId_3", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialItemID4: int = ParamField(
        uint, "materialItemId_4", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialItemID5: int = ParamField(
        uint, "materialItemId_5", game_type=GoodParam, default=0,
        tooltip="TODO",
    )
    MaterialCount1: int = ParamField(
        uint, "num_1", default=0,
        tooltip="TODO",
    )
    MaterialCount2: int = ParamField(
        uint, "num_2", default=0,
        tooltip="TODO",
    )
    MaterialCount3: int = ParamField(
        uint, "num_3", default=0,
        tooltip="TODO",
    )
    MaterialCount4: int = ParamField(
        uint, "num_4", default=0,
        tooltip="TODO",
    )
    MaterialCount5: int = ParamField(
        uint, "num_5", default=0,
        tooltip="TODO",
    )
