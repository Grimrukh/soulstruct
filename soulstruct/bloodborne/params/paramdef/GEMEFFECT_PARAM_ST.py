from __future__ import annotations

__all__ = ["GEMEFFECT_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


class GEMEFFECT_PARAM_ST(ParamRow):
    SpecialEffectID: int = ParamField(
        int, "speffectId", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
    CategoryID: int = ParamField(
        int, "categoryId", default=0,
        tooltip="TODO",
    )
    EffectRank: int = ParamField(
        int, "effectRank", default=0,
        tooltip="TODO",
    )
    MinimumRank: int = ParamField(
        int, "rankMin", default=0,
        tooltip="TODO",
    )
    MaximumRank: int = ParamField(
        int, "rankMax", default=0,
        tooltip="TODO",
    )
    DisposalPrice: int = ParamField(
        int, "disposalPrice", default=0,
        tooltip="TODO",
    )
    GemIconIDOffset: int = ParamField(
        ushort, "gemIconIdOffset", default=0,
        tooltip="TODO",
    )
    SortID: int = ParamField(
        ushort, "sortId:14", bit_count=14, default=0,
        tooltip="TODO",
    )
    SortCategory: int = ParamField(
        ushort, "sortCategory:2", bit_count=2, default=0,
        tooltip="TODO",
    )
    GemNameIDOffset: int = ParamField(
        uint, "gemNameIdOffset", default=0,
        tooltip="TODO",
    )
    AttackSpecialEffectID: int = ParamField(
        int, "speffectId_forAtk", game_type=SpecialEffectParam, default=-1,
        tooltip="TODO",
    )
