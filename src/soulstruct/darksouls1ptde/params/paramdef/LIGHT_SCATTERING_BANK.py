from __future__ import annotations

__all__ = ["LIGHT_SCATTERING_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LIGHT_SCATTERING_BANK(ParamRow):
    LightRotationX: int = ParamField(
        int16, "sunRotX", default=0,
        tooltip="Rotation (X-axis) of scattering light source.",
    )
    LightRotationY: int = ParamField(
        int16, "sunRotY", default=0,
        tooltip="Rotation (Y-axis) of scattering light source.",
    )
    DistanceMultiplier: int = ParamField(
        int16, "distanceMul", default=100,
        tooltip="Magnification (0-100) of scattering light source distance.",
    )
    LightRed: int = ParamField(
        int16, "sunR", default=255,
        tooltip="Red channel (0-255) of scattering light source.",
    )
    LightGreen: int = ParamField(
        int16, "sunG", default=255,
        tooltip="Green channel (0-255) of scattering light source.",
    )
    LightBlue: int = ParamField(
        int16, "sunB", default=255,
        tooltip="Blue channel (0-255) of scattering light source.",
    )
    LightAlpha: int = ParamField(
        int16, "sunA", default=600,
        tooltip="Alpha channel (0-255) of scattering light source.",
    )
    _Pad0: bytes = ParamPad(2, "pad_0[2]")
    ScatteringDirection: float = ParamField(
        float32, "lsHGg", default=0.800000011920929,
        tooltip="Coefficient of scattering direction, between -1 (backward) and 1 (forward).",
    )
    RayleighCoefficient: float = ParamField(
        float32, "lsBetaRay", default=0.20000000298023224,
        tooltip="Coefficient determining how much light is lost to scattering (e.g. simulating amount of atmosphere).",
    )
    MieCoefficient: float = ParamField(
        float32, "lsBetaMie", default=0.009999999776482582,
        tooltip="Coefficient determining how much light is scattered by larger particles (e.g. simulating "
                "dust/smoke).",
    )
    ScatteringCoefficient: int = ParamField(
        int16, "blendCoef", default=100,
        tooltip="Coefficient determining the overall amount of scattering from 0 (no scattering) to 100 (max "
                "scattering).",
    )
    SurfaceReflectanceRed: int = ParamField(
        int16, "reflectanceR", default=255,
        tooltip="Red channel (0-255) of the effect of the scattered light as it hits surfaces.",
    )
    SurfaceReflectanceGreen: int = ParamField(
        int16, "reflectanceG", default=255,
        tooltip="Green channel (0-255) of the effect of the scattered light as it hits surfaces.",
    )
    SurfaceReflectanceBlue: int = ParamField(
        int16, "reflectanceB", default=255,
        tooltip="Blue channel (0-255) of the effect of the scattered light as it hits surfaces.",
    )
    SurfaceReflectanceAlpha: int = ParamField(
        int16, "reflectanceA", default=100,
        tooltip="Alpha channel (0-255) of the effect of the scattered light as it hits surfaces.",
    )
    _Pad1: bytes = ParamPad(2, "pad_1[2]")
