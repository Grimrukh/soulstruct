from __future__ import annotations

__all__ = ["DUNGEON_SUB_FEAT_LOT_PARAM"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class DUNGEON_SUB_FEAT_LOT_PARAM(ParamRowData):
    SubFeatureNameID: int = ParamField(
        uint, "subFeatureNameId", default=0,
        tooltip="TODO",
    )
    RequiredMaterialID: int = ParamField(
        uint, "requiredMaterialId", default=0,
        tooltip="TODO",
    )
    SubFeatureID1: int = ParamField(
        sbyte, "subFeatureId_1", default=-1,
        tooltip="TODO",
    )
    SubFeatureID2: int = ParamField(
        sbyte, "subFeatureId_2", default=-1,
        tooltip="TODO",
    )
    SubFeatureID3: int = ParamField(
        sbyte, "subFeatureId_3", default=-1,
        tooltip="TODO",
    )
    SubFeatureID4: int = ParamField(
        sbyte, "subFeatureId_4", default=-1,
        tooltip="TODO",
    )
    SubFeatureID5: int = ParamField(
        sbyte, "subFeatureId_5", default=-1,
        tooltip="TODO",
    )
    SubFeatureID6: int = ParamField(
        sbyte, "subFeatureId_6", default=-1,
        tooltip="TODO",
    )
    SubFeatureID7: int = ParamField(
        sbyte, "subFeatureId_7", default=-1,
        tooltip="TODO",
    )
    SubFeatureID8: int = ParamField(
        sbyte, "subFeatureId_8", default=-1,
        tooltip="TODO",
    )
    SubFeatureID9: int = ParamField(
        sbyte, "subFeatureId_9", default=-1,
        tooltip="TODO",
    )
    SubFeatureID10: int = ParamField(
        sbyte, "subFeatureId_10", default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad_0[2]")
    Rate1: float = ParamField(
        float, "rate_1", default=0.0,
        tooltip="TODO",
    )
    Rate2: float = ParamField(
        float, "rate_2", default=0.0,
        tooltip="TODO",
    )
    Rate3: float = ParamField(
        float, "rate_3", default=0.0,
        tooltip="TODO",
    )
    Rate4: float = ParamField(
        float, "rate_4", default=0.0,
        tooltip="TODO",
    )
    Rate5: float = ParamField(
        float, "rate_5", default=0.0,
        tooltip="TODO",
    )
    Rate6: float = ParamField(
        float, "rate_6", default=0.0,
        tooltip="TODO",
    )
    Rate7: float = ParamField(
        float, "rate_7", default=0.0,
        tooltip="TODO",
    )
    Rate8: float = ParamField(
        float, "rate_8", default=0.0,
        tooltip="TODO",
    )
    Rate9: float = ParamField(
        float, "rate_9", default=0.0,
        tooltip="TODO",
    )
    Rate10: float = ParamField(
        float, "rate_10", default=0.0,
        tooltip="TODO",
    )
