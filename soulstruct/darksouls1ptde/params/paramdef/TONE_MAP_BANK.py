from __future__ import annotations

__all__ = ["TONE_MAP_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class TONE_MAP_BANK(ParamRow):
    NearBloomThreshold: int = ParamField(
        sbyte, "bloomBegin", default=0,
        tooltip="Near light blooming begins when brightness exceeds this threshold.",
    )
    NearBloomMultiplier: int = ParamField(
        sbyte, "bloomMul", default=0,
        tooltip="Near light blooming multiplier.",
    )
    FarBloomThreshold: int = ParamField(
        sbyte, "bloomBeginFar", default=0,
        tooltip="Far light blooming begins when brightness exceeds this threshold.",
    )
    FarBloomMultiplier: int = ParamField(
        sbyte, "bloomMulFar", default=0,
        tooltip="Far light blooming multiplier.",
    )
    NearBloomEndDistance: float = ParamField(
        float, "bloomNearDist", default=20.0,
        tooltip="Near bloom parameters apply up to this maximum distance.",
    )
    FarBloomStartDistance: float = ParamField(
        float, "bloomFarDist", default=60.0,
        tooltip="Far bloom parameters apply beyond this minimum distance.",
    )
    OverallBrightness: float = ParamField(
        float, "grayKeyValue", default=0.18000000715255737,
        tooltip="Larger values make the screen brighter overall.",
    )
    MinimumAdaptationBrightness: float = ParamField(
        float, "minAdaptedLum", default=0.10000000149011612,
        tooltip="Minimum brightness for tone adaptation. Smaller values mean that darker places will be adapted.",
    )
    MaximumAdaptationBrightness: float = ParamField(
        float, "maxAdapredLum", default=0.20000000298023224,
        tooltip="Maximum brightness for tone adaptation. Larger values mean that brighter places will be adapted.",
    )
    AdaptationSpeed: float = ParamField(
        float, "adaptSpeed", default=1.0,
        tooltip="Tone adaptation speed.",
    )
    LightShaftThreshold: int = ParamField(
        sbyte, "lightShaftBegin", default=50,
        tooltip="Light shafts will appear when brightness exceeds this threshold.",
    )
    _Pad0: bytes = ParamPad(3, "pad_0[3]")
    LightShaftMagnitude: float = ParamField(
        float, "lightShaftPower", default=0.0,
        tooltip="Light shaft magnitude (0 means no light shafts).",
    )
    LightShaftAttenuationRate: float = ParamField(
        float, "lightShaftAttenRate", default=0.949999988079071,
        tooltip="Smaller values will shorten the light shafts more.",
    )
