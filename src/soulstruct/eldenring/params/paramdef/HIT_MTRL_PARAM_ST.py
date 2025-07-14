from __future__ import annotations

__all__ = ["HIT_MTRL_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class HIT_MTRL_PARAM_ST(ParamRow):
    SoundRadiusMultiplier: float = ParamField(
        float, "aiVolumeRate", default=1.0,
        tooltip="Multiplier for foot sound effect radius on this terrain.",
    )
    SpecialEffect1: int = ParamField(
        int, "spEffectIdOnHit0", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to character walking on terrain (first of two).",
    )
    SpecialEffect2: int = ParamField(
        int, "spEffectIdOnHit1", game_type=SpecialEffectParam, default=-1,
        tooltip="Special effect applied to character walking on terrain (second of two).",
    )
    FootEffectHeightType: int = ParamField(
        byte, "footEffectHeightType:2", HMP_FOOT_EFFECT_HEIGHT_TYPE, bit_count=2, default=0,
        tooltip="Determines the height at which foot impact effects are generated.",
    )
    FootEffectDirectionType: int = ParamField(
        byte, "footEffectDirType:2", HMP_FOOT_EFFECT_DIR_TYPE, bit_count=2, default=0,
        tooltip="Determines the direction of foot impact effects.",
    )
    TerrainHeightType: int = ParamField(
        byte, "floorHeightType:2", HMP_FLOOR_HEIGHT_TYPE, bit_count=2, default=0,
        tooltip="Determines distance from floor collision at which effects are applied.",
    )
    DisableFallDamage: bool = ParamField(
        byte, "disableFallDamage:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsHardnessForSoundReverb: bool = ParamField(
        byte, "isHardnessForSoundReverb:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    HardnessType: int = ParamField(
        byte, "hardnessType", HMP_HARDNESS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(6, "pad2[6]")
    SpEffectIdOnHit0ClearCount2: int = ParamField(
        int, "spEffectIdOnHit0_ClearCount_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit0ClearCount3: int = ParamField(
        int, "spEffectIdOnHit0_ClearCount_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit0ClearCount4: int = ParamField(
        int, "spEffectIdOnHit0_ClearCount_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit0ClearCount5: int = ParamField(
        int, "spEffectIdOnHit0_ClearCount_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit0ClearCount6: int = ParamField(
        int, "spEffectIdOnHit0_ClearCount_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit0ClearCount7: int = ParamField(
        int, "spEffectIdOnHit0_ClearCount_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit0ClearCount8: int = ParamField(
        int, "spEffectIdOnHit0_ClearCount_8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit1ClearCount2: int = ParamField(
        int, "spEffectIdOnHit1_ClearCount_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit1ClearCount3: int = ParamField(
        int, "spEffectIdOnHit1_ClearCount_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit1ClearCount4: int = ParamField(
        int, "spEffectIdOnHit1_ClearCount_4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit1ClearCount5: int = ParamField(
        int, "spEffectIdOnHit1_ClearCount_5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit1ClearCount6: int = ParamField(
        int, "spEffectIdOnHit1_ClearCount_6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit1ClearCount7: int = ParamField(
        int, "spEffectIdOnHit1_ClearCount_7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdOnHit1ClearCount8: int = ParamField(
        int, "spEffectIdOnHit1_ClearCount_8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ReplaceMateiralIdRain: int = ParamField(
        short, "replaceMateiralId_Rain", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad4[2]")
    SpEffectIdforWet00: int = ParamField(
        int, "spEffectId_forWet00", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforWet01: int = ParamField(
        int, "spEffectId_forWet01", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforWet02: int = ParamField(
        int, "spEffectId_forWet02", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforWet03: int = ParamField(
        int, "spEffectId_forWet03", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIdforWet04: int = ParamField(
        int, "spEffectId_forWet04", default=-1,
        tooltip="TOOLTIP-TODO",
    )
