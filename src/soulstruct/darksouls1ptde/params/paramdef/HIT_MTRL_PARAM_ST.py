from __future__ import annotations

__all__ = ["HIT_MTRL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class HIT_MTRL_PARAM_ST(ParamRow):
    SoundRadiusMultiplier: float = ParamField(
        float32, "aiVolumeRate", default=1.0,
        tooltip="Multiplier for foot sound effect radius on this terrain.",
    )
    SpecialEffect1: int = ParamField(
        int32, "spEffectIdOnHit0", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to character walking on terrain (first of two).",
    )
    SpecialEffect2: int = ParamField(
        int32, "spEffectIdOnHit1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to character walking on terrain (second of two).",
    )
    FootEffectHeightType: int = ParamField(
        uint8, "footEffectHeightType:2", HMP_FOOT_EFFECT_HEIGHT_TYPE, bit_count=2, default=0,
        tooltip="Determines the height at which foot impact effects are generated.",
    )
    FootEffectDirectionType: int = ParamField(
        uint8, "footEffectDirType:2", HMP_FOOT_EFFECT_DIR_TYPE, bit_count=2, default=0,
        tooltip="Determines the direction of foot impact effects.",
    )
    TerrainHeightType: int = ParamField(
        uint8, "floorHeightType:2", HMP_FLOOR_HEIGHT_TYPE, bit_count=2, default=0,
        tooltip="Determines distance from floor collision at which effects are applied.",
    )
    _Pad0: bytes = ParamPad(3, "pad0[3]")
