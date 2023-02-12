from __future__ import annotations

__all__ = ["HIT_MTRL_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class HIT_MTRL_PARAM_ST(ParamRowData):
    SoundRadiusMultiplier: float = ParamField(
        float, "aiVolumeRate", default=1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffect1: int = ParamField(
        int, "spEffectIdOnHit0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffect2: int = ParamField(
        int, "spEffectIdOnHit1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FootEffectHeightType: int = ParamField(
        byte, "footEffectHeightType:2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FootEffectDirectionType: int = ParamField(
        byte, "footEffectDirType:2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    TerrainHeightType: int = ParamField(
        byte, "floorHeightType:2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableFallDamage: int = ParamField(
        byte, "disableFallDamage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsHardnessForSoundReverb: int = ParamField(
        byte, "isHardnessForSoundReverb:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HardnessType: int = ParamField(
        byte, "hardnessType", default=0,
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
