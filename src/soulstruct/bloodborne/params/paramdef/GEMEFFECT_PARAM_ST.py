from __future__ import annotations

__all__ = ["GEMEFFECT_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class GEMEFFECT_PARAM_ST(ParamRow):
    SpecialEffectID: int = ParamField(
        int32, "speffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    CategoryID: int = ParamField(
        int32, "categoryId", default=0,
        tooltip="TODO",
    )
    EffectRank: int = ParamField(
        int32, "effectRank", default=0,
        tooltip="TODO",
    )
    MinimumRank: int = ParamField(
        int32, "rankMin", default=0,
        tooltip="TODO",
    )
    MaximumRank: int = ParamField(
        int32, "rankMax", default=0,
        tooltip="TODO",
    )
    DisposalPrice: int = ParamField(
        int32, "disposalPrice", default=0,
        tooltip="TODO",
    )
    GemIconIDOffset: int = ParamField(
        uint16, "gemIconIdOffset", default=0,
        tooltip="TODO",
    )
    SortID: int = ParamField(
        uint16, "sortId:14", bit_count=14, default=0,
        tooltip="TODO",
    )
    SortCategory: int = ParamField(
        uint16, "sortCategory:2", bit_count=2, default=0,
        tooltip="TODO",
    )
    GemNameIDOffset: int = ParamField(
        uint32, "gemNameIdOffset", default=0,
        tooltip="TODO",
    )
    AttackSpecialEffectID: int = ParamField(
        int32, "speffectId_forAtk", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
