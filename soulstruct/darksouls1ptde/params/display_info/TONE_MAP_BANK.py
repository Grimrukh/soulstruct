from __future__ import annotations

__all__ = ["TONE_MAP_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field

TONE_MAP_BANK = {
    "param_type": "TONE_MAP_BANK",
    "file_name": "ToneMapBank",
    "nickname": "ToneMapping",
    "fields": [
        ParamFieldInfo(
            "bloomBegin",
            "NearBloomThreshold",
            True,
            int,
            "Near light blooming begins when brightness exceeds this threshold.",
        ),
        ParamFieldInfo("bloomMul", "NearBloomMultiplier", True, int, "Near light blooming multiplier."),
        ParamFieldInfo(
            "bloomBeginFar",
            "FarBloomThreshold",
            True,
            int,
            "Far light blooming begins when brightness exceeds this threshold.",
        ),
        ParamFieldInfo("bloomMulFar", "FarBloomMultiplier", True, int, "Far light blooming multiplier."),
        ParamFieldInfo(
            "bloomNearDist",
            "NearBloomEndDistance",
            True,
            float,
            "Near bloom parameters apply up to this maximum distance.",
        ),
        ParamFieldInfo(
            "bloomFarDist",
            "FarBloomStartDistance",
            True,
            float,
            "Far bloom parameters apply beyond this minimum distance.",
        ),
        ParamFieldInfo(
            "grayKeyValue", "OverallBrightness", True, float, "Larger values make the screen brighter overall."
        ),
        ParamFieldInfo(
            "minAdaptedLum",
            "MinimumAdaptationBrightness",
            True,
            float,
            "Minimum brightness for tone adaptation. Smaller values mean that darker places will be adapted.",
        ),
        ParamFieldInfo(
            "maxAdapredLum",  # NOT A TYPO
            "MaximumAdaptationBrightness",
            True,
            float,
            "Maximum brightness for tone adaptation. Larger values mean that brighter places will be adapted.",
        ),
        ParamFieldInfo("adaptSpeed", "AdaptationSpeed", True, float, "Tone adaptation speed."),
        ParamFieldInfo(
            "lightShaftBegin",
            "LightShaftThreshold",
            True,
            int,
            "Light shafts will appear when brightness exceeds this threshold.",
        ),
        ParamFieldInfo("pad_0[3]", "Pad0", True, pad_field(3), "Null padding."),
        ParamFieldInfo(
            "lightShaftPower",
            "LightShaftMagnitude",
            True,
            float,
            "Light shaft magnitude (0 means no light shafts).",
        ),
        ParamFieldInfo(
            "lightShaftAttenRate",
            "LightShaftAttenuationRate",
            True,
            float,
            "Smaller values will shorten the light shafts more.",
        ),
    ],
}
