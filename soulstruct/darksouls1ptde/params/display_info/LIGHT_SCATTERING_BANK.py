from __future__ import annotations

__all__ = ["LIGHT_SCATTERING_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field


LIGHT_SCATTERING_BANK = {
    "param_type": "LIGHT_SCATTERING_BANK",
    "file_name": "LightScatteringBank",
    "nickname": "ScatteredLight",
    "fields": [
        ParamFieldInfo("sunRotX", "LightRotationX", True, int, "Rotation (X-axis) of scattering light source."),
        ParamFieldInfo("sunRotY", "LightRotationY", True, int, "Rotation (Y-axis) of scattering light source."),
        ParamFieldInfo(
            "distanceMul",
            "DistanceMultiplier",
            True,
            int,
            "Magnification (0-100) of scattering light source distance.",
        ),
        ParamFieldInfo("sunR", "LightRed", True, int, "Red channel (0-255) of scattering light source."),
        ParamFieldInfo("sunG", "LightGreen", True, int, "Green channel (0-255) of scattering light source."),
        ParamFieldInfo("sunB", "LightBlue", True, int, "Blue channel (0-255) of scattering light source."),
        ParamFieldInfo("sunA", "LightAlpha", True, int, "Alpha channel (0-255) of scattering light source."),
        ParamFieldInfo("pad_0[2]", "Pad0", False, pad_field(2), "Null padding."),
        ParamFieldInfo(
            "lsHGg",
            "ScatteringDirection",
            True,
            float,
            "Coefficient of scattering direction, between -1 (backward) and 1 (forward).",
        ),
        ParamFieldInfo(
            "lsBetaRay",
            "RayleighCoefficient",
            True,
            float,
            "Coefficient determining how much light is lost to scattering (e.g. simulating amount of atmosphere).",
        ),
        ParamFieldInfo(
            "lsBetaMie",
            "MieCoefficient",
            True,
            float,
            "Coefficient determining how much light is scattered by larger particles (e.g. simulating dust/smoke).",
        ),
        ParamFieldInfo(
            "blendCoef",
            "ScatteringCoefficient",
            True,
            int,
            "Coefficient determining the overall amount of scattering from 0 (no scattering) to 100 (max "
            "scattering).",
        ),
        ParamFieldInfo(
            "reflectanceR",
            "SurfaceReflectanceRed",
            True,
            int,
            "Red channel (0-255) of the effect of the scattered light as it hits surfaces.",
        ),
        ParamFieldInfo(
            "reflectanceG",
            "SurfaceReflectanceGreen",
            True,
            int,
            "Green channel (0-255) of the effect of the scattered light as it hits surfaces.",
        ),
        ParamFieldInfo(
            "reflectanceB",
            "SurfaceReflectanceBlue",
            True,
            int,
            "Blue channel (0-255) of the effect of the scattered light as it hits surfaces.",
        ),
        ParamFieldInfo(
            "reflectanceA",
            "SurfaceReflectanceAlpha",
            True,
            int,
            "Alpha channel (0-255) of the effect of the scattered light as it hits surfaces.",
        ),
        ParamFieldInfo("pad_1[2]", "Pad1", False, pad_field(2), "Null padding."),
    ],
}
