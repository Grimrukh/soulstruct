from __future__ import annotations

__all__ = ["HIT_MTRL_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class HIT_MTRL_PARAM_ST(ParamRowData):
    SoundRadiusMultiplier: float = ParamField(
        float, "aiVolumeRate", default=1.0,
        tooltip="Multiplier for foot sound effect radius on this terrain.",
    )
    SpecialEffect1: SpecialEffectParam = ParamField(
        int, "spEffectIdOnHit0", default=-1,
        tooltip="Special effect applied to character walking on terrain (first of two).",
    )
    SpecialEffect2: SpecialEffectParam = ParamField(
        int, "spEffectIdOnHit1", default=-1,
        tooltip="Special effect applied to character walking on terrain (second of two).",
    )
    FootEffectHeightType: HMP_FOOT_EFFECT_HEIGHT_TYPE = ParamField(
        byte, "footEffectHeightType:2", bit_count=2, default=0,
        tooltip="Determines the height at which foot impact effects are generated.",
    )
    FootEffectDirectionType: HMP_FOOT_EFFECT_DIR_TYPE = ParamField(
        byte, "footEffectDirType:2", bit_count=2, default=0,
        tooltip="Determines the direction of foot impact effects.",
    )
    TerrainHeightType: HMP_FLOOR_HEIGHT_TYPE = ParamField(
        byte, "floorHeightType:2", bit_count=2, default=0,
        tooltip="Determines distance from floor collision at which effects are applied.",
    )
    _Pad0: bytes = ParamPad(3, "pad0[3]")
