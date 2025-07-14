from __future__ import annotations

__all__ = ["TONE_MAP_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class TONE_MAP_BANK(ParamRow):
    NearBloomThreshold: int = ParamField(
        int16, "bloomBegin", default=0,
        tooltip="Near light blooming begins when brightness exceeds this threshold.",
    )
    NearBloomMultiplier: int = ParamField(
        int16, "bloomMul", default=0,
        tooltip="Near light blooming multiplier.",
    )
    FarBloomThreshold: int = ParamField(
        int16, "bloomBeginFar", default=0,
        tooltip="Far light blooming begins when brightness exceeds this threshold.",
    )
    FarBloomMultiplier: int = ParamField(
        int16, "bloomMulFar", default=0,
        tooltip="Far light blooming multiplier.",
    )
    NearBloomEndDistance: float = ParamField(
        float32, "bloomNearDist", default=20.0,
        tooltip="Near bloom parameters apply up to this maximum distance.",
    )
    FarBloomStartDistance: float = ParamField(
        float32, "bloomFarDist", default=60.0,
        tooltip="Far bloom parameters apply beyond this minimum distance.",
    )
    OverallBrightness: float = ParamField(
        float32, "grayKeyValue", default=0.18000000715255737,
        tooltip="Larger values make the screen brighter overall.",
    )
    MinimumAdaptationBrightness: float = ParamField(
        float32, "minAdaptedLum", default=0.10000000149011612,
        tooltip="Minimum brightness for tone adaptation. Smaller values mean that darker places will be adapted.",
    )
    MaximumAdaptationBrightness: float = ParamField(
        float32, "maxAdapredLum", default=0.20000000298023224,
        tooltip="Maximum brightness for tone adaptation. Larger values mean that brighter places will be adapted.",
    )
    AdaptationSpeed: float = ParamField(
        float32, "adaptSpeed", default=1.0,
        tooltip="Tone adaptation speed.",
    )
    LightShaftThreshold: int = ParamField(
        int8, "lightShaftBegin", default=50,
        tooltip="Light shafts will appear when brightness exceeds this threshold.",
    )
    _Pad0: bytes = ParamPad(3, "pad_0[3]")
    LightShaftMagnitude: float = ParamField(
        float32, "lightShaftPower", default=0.0,
        tooltip="Light shaft magnitude (0 means no light shafts).",
    )
    LightShaftAttenuationRate: float = ParamField(
        float32, "lightShaftAttenRate", default=0.949999988079071,
        tooltip="Smaller values will shorten the light shafts more.",
    )
    InverseToneMapMultiplier: float = ParamField(
        float32, "inverseToneMapMul", default=3.0,
        tooltip="New tone mapping field. (Added in DSR)",
    )
