from __future__ import annotations

__all__ = ["DUNGEON_SUB_FEAT_LOT_PARAM"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class DUNGEON_SUB_FEAT_LOT_PARAM(ParamRow):
    SubFeatureNameID: int = ParamField(
        uint32, "subFeatureNameId", default=0,
        tooltip="TODO",
    )
    RequiredMaterialID: int = ParamField(
        uint32, "requiredMaterialId", default=0,
        tooltip="TODO",
    )
    SubFeatureID1: int = ParamField(
        int8, "subFeatureId_1", default=-1,
        tooltip="TODO",
    )
    SubFeatureID2: int = ParamField(
        int8, "subFeatureId_2", default=-1,
        tooltip="TODO",
    )
    SubFeatureID3: int = ParamField(
        int8, "subFeatureId_3", default=-1,
        tooltip="TODO",
    )
    SubFeatureID4: int = ParamField(
        int8, "subFeatureId_4", default=-1,
        tooltip="TODO",
    )
    SubFeatureID5: int = ParamField(
        int8, "subFeatureId_5", default=-1,
        tooltip="TODO",
    )
    SubFeatureID6: int = ParamField(
        int8, "subFeatureId_6", default=-1,
        tooltip="TODO",
    )
    SubFeatureID7: int = ParamField(
        int8, "subFeatureId_7", default=-1,
        tooltip="TODO",
    )
    SubFeatureID8: int = ParamField(
        int8, "subFeatureId_8", default=-1,
        tooltip="TODO",
    )
    SubFeatureID9: int = ParamField(
        int8, "subFeatureId_9", default=-1,
        tooltip="TODO",
    )
    SubFeatureID10: int = ParamField(
        int8, "subFeatureId_10", default=-1,
        tooltip="TODO",
    )
    _Pad0: bytes = ParamPad(2, "pad_0[2]")
    Rate1: float = ParamField(
        float32, "rate_1", default=0.0,
        tooltip="TODO",
    )
    Rate2: float = ParamField(
        float32, "rate_2", default=0.0,
        tooltip="TODO",
    )
    Rate3: float = ParamField(
        float32, "rate_3", default=0.0,
        tooltip="TODO",
    )
    Rate4: float = ParamField(
        float32, "rate_4", default=0.0,
        tooltip="TODO",
    )
    Rate5: float = ParamField(
        float32, "rate_5", default=0.0,
        tooltip="TODO",
    )
    Rate6: float = ParamField(
        float32, "rate_6", default=0.0,
        tooltip="TODO",
    )
    Rate7: float = ParamField(
        float32, "rate_7", default=0.0,
        tooltip="TODO",
    )
    Rate8: float = ParamField(
        float32, "rate_8", default=0.0,
        tooltip="TODO",
    )
    Rate9: float = ParamField(
        float32, "rate_9", default=0.0,
        tooltip="TODO",
    )
    Rate10: float = ParamField(
        float32, "rate_10", default=0.0,
        tooltip="TODO",
    )
