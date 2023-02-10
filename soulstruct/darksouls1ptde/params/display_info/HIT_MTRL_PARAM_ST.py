from __future__ import annotations

__all__ = ["HIT_MTRL_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field
from soulstruct.darksouls1ptde.game_types import *
from ..enums import *

HIT_MTRL_PARAM_ST = {
    "param_type": "HIT_MTRL_PARAM_ST",
    "file_name": "HitMtrlParam",
    "nickname": "Terrains",
    "fields": [
        ParamFieldInfo(
            "aiVolumeRate",
            "SoundRadiusMultiplier",
            True,
            float,
            "Multiplier for foot sound effect radius on this terrain.",
        ),
        ParamFieldInfo(
            "spEffectIdOnHit0",
            "SpecialEffect1",
            True,
            SpecialEffectParam,
            "Special effect applied to character walking on terrain (first of two).",
        ),
        ParamFieldInfo(
            "spEffectIdOnHit1",
            "SpecialEffect2",
            True,
            SpecialEffectParam,
            "Special effect applied to character walking on terrain (second of two).",
        ),
        ParamFieldInfo(
            "footEffectHeightType:2",
            "FootEffectHeightType",
            True,
            HMP_FOOT_EFFECT_HEIGHT_TYPE,
            "Determines the height at which foot impact effects are generated.",
        ),
        ParamFieldInfo(
            "footEffectDirType:2",
            "FootEffectDirectionType",
            True,
            HMP_FOOT_EFFECT_DIR_TYPE,
            "Determines the direction of foot impact effects.",
        ),
        ParamFieldInfo(
            "floorHeightType:2",
            "TerrainHeightType",
            True,
            HMP_FLOOR_HEIGHT_TYPE,
            "Determines distance from floor collision at which effects are applied.",
        ),
        ParamFieldInfo("pad0[3]", "Pad1", False, pad_field(3), "Null padding."),
    ],
}
