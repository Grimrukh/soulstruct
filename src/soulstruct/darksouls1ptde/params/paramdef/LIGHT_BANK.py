from __future__ import annotations

__all__ = ["LIGHT_BANK"]

from soulstruct.base.params.param_row import *
from soulstruct.utilities.binary import *


class LIGHT_BANK(ParamRow):
    BakedLight0RotationX: int = ParamField(
        int16, "degRotX_0", default=0,
        tooltip="Rotation (X-axis) of ambient (parallel) light source 0.",
    )
    BakedLight0RotationY: int = ParamField(
        int16, "degRotY_0", default=0,
        tooltip="Rotation (Y-axis) of ambient (parallel) light source 0.",
    )
    BakedLight0Red: int = ParamField(
        int16, "colR_0", default=255,
        tooltip="Red channel (0-255) of ambient (parallel) light source 0.",
    )
    BakedLight0Green: int = ParamField(
        int16, "colG_0", default=255,
        tooltip="Green channel (0-255) of ambient (parallel) light source 0.",
    )
    BakedLight0Blue: int = ParamField(
        int16, "colB_0", default=255,
        tooltip="Blue channel (0-255) of ambient (parallel) light source 0.",
    )
    BakedLight0Alpha: int = ParamField(
        int16, "colA_0", default=100,
        tooltip="Alpha channel (0-255) of ambient (parallel) light source 0.",
    )
    BakedLight1RotationX: int = ParamField(
        int16, "degRotX_1", default=0,
        tooltip="Rotation (X-axis) of ambient (parallel) light source 1.",
    )
    BakedLight1RotationY: int = ParamField(
        int16, "degRotY_1", default=0,
        tooltip="Rotation (Y-axis) of ambient (parallel) light source 1.",
    )
    BakedLight1Red: int = ParamField(
        int16, "colR_1", default=255,
        tooltip="Red channel (0-255) of ambient (parallel) light source 1.",
    )
    BakedLight1Green: int = ParamField(
        int16, "colG_1", default=255,
        tooltip="Green channel (0-255) of ambient (parallel) light source 1.",
    )
    BakedLight1Blue: int = ParamField(
        int16, "colB_1", default=255,
        tooltip="Blue channel (0-255) of ambient (parallel) light source 1.",
    )
    BakedLight1Alpha: int = ParamField(
        int16, "colA_1", default=100,
        tooltip="Alpha channel (0-255) of ambient (parallel) light source 1.",
    )
    BakedLight2RotationX: int = ParamField(
        int16, "degRotX_2", default=0,
        tooltip="Rotation (X-axis) of ambient (parallel) light source 2.",
    )
    BakedLight2RotationY: int = ParamField(
        int16, "degRotY_2", default=0,
        tooltip="Rotation (Y-axis) of ambient (parallel) light source 2.",
    )
    BakedLight2Red: int = ParamField(
        int16, "colR_2", default=255,
        tooltip="Red channel (0-255) of ambient (parallel) light source 2.",
    )
    BakedLight2Green: int = ParamField(
        int16, "colG_2", default=255,
        tooltip="Green channel (0-255) of ambient (parallel) light source 2.",
    )
    BakedLight2Blue: int = ParamField(
        int16, "colB_2", default=255,
        tooltip="Blue channel (0-255) of ambient (parallel) light source 2.",
    )
    BakedLight2Alpha: int = ParamField(
        int16, "colA_2", default=100,
        tooltip="Alpha channel (0-255) of ambient (parallel) light source 2.",
    )
    TopDownLightRed: int = ParamField(
        int16, "colR_u", default=255,
        tooltip="Red channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
                "surface is oriented sideways (e.g. walls).",
    )
    TopDownLightGreen: int = ParamField(
        int16, "colG_u", default=255,
        tooltip="Green channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
                "surface is oriented sideways (e.g. walls).",
    )
    TopDownLightBlue: int = ParamField(
        int16, "colB_u", default=255,
        tooltip="Blue channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
                "surface is oriented sideways (e.g. walls).",
    )
    TopDownLightAlpha: int = ParamField(
        int16, "colA_u", default=100,
        tooltip="Alpha channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
                "surface is oriented sideways (e.g. walls).",
    )
    BottomUpLightRed: int = ParamField(
        int16, "colR_d", default=255,
        tooltip="Red channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
                "the surface is oriented sideways (e.g. walls).",
    )
    BottomUpLightGreen: int = ParamField(
        int16, "colG_d", default=255,
        tooltip="Green channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
                "the surface is oriented sideways (e.g. walls).",
    )
    BottomUpLightBlue: int = ParamField(
        int16, "colB_d", default=255,
        tooltip="Blue channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
                "the surface is oriented sideways (e.g. walls).",
    )
    BottomUpLightAlpha: int = ParamField(
        int16, "colA_d", default=100,
        tooltip="Alpha channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
                "the surface is oriented sideways (e.g. walls).",
    )
    SpecularBakedLightRotationX: int = ParamField(
        int16, "degRotX_s", default=0,
        tooltip="Rotation (X-axis) of specular ambient (parallel) light source.",
    )
    SpecularBakedLightRotationY: int = ParamField(
        int16, "degRotY_s", default=0,
        tooltip="Rotation (Y-axis) of specular ambient (parallel) light source.",
    )
    SpecularBakedLightRed: int = ParamField(
        int16, "colR_s", default=255,
        tooltip="Red channel (0-255) of specular ambient light source.",
    )
    SpecularBakedLightGreen: int = ParamField(
        int16, "colG_s", default=255,
        tooltip="Green channel (0-255) of specular ambient light source.",
    )
    SpecularBakedLightBlue: int = ParamField(
        int16, "colB_s", default=255,
        tooltip="Blue channel (0-255) of specular ambient light source.",
    )
    SpecularBakedLightAlpha: int = ParamField(
        int16, "colA_s", default=0,
        tooltip="Alpha channel (0-255) of specular ambient light source.",
    )
    DiffuseLightRed: int = ParamField(
        int16, "envDif_colR", default=255,
        tooltip="Red channel (0-255) of base diffuse ambient light of surfaces.",
    )
    DiffuseLightGreen: int = ParamField(
        int16, "envDif_colG", default=255,
        tooltip="Green channel (0-255) of base diffuse ambient light of surfaces.",
    )
    DiffuseLightBlue: int = ParamField(
        int16, "envDif_colB", default=255,
        tooltip="Blue channel (0-255) of base diffuse ambient light of surfaces.",
    )
    DiffuseLightAlpha: int = ParamField(
        int16, "envDif_colA", default=100,
        tooltip="Alpha channel (0-255) of base diffuse ambient light of surfaces.",
    )
    SpecularLightRed: int = ParamField(
        int16, "envSpc_colR", default=255,
        tooltip="Red channel (0-255) of specular ambient light of surfaces.",
    )
    SpecularLightGreen: int = ParamField(
        int16, "envSpc_colG", default=255,
        tooltip="Green channel (0-255) of specular ambient light of surfaces.",
    )
    SpecularLightBlue: int = ParamField(
        int16, "envSpc_colB", default=255,
        tooltip="Blue channel (0-255) of specular ambient light of surfaces.",
    )
    SpecularLightAlpha: int = ParamField(
        int16, "envSpc_colA", default=100,
        tooltip="Alpha channel (0-255) of specular ambient light of surfaces.",
    )
    DiffuseLightTextureID: int = ParamField(
        int16, "envDif", default=0,
        tooltip="Changing this has drastic effects on the diffuse ambient light.",
    )
    SpecularLightTextureID0: int = ParamField(
        int16, "envSpc_0", default=0,
        tooltip="Changing this has drastic effects on the specular ambient light.",
    )
    SpecularLightTextureID1: int = ParamField(
        int16, "envSpc_1", default=0,
        tooltip="Changing this has drastic effects on the specular ambient light.",
    )
    SpecularLightTextureID2: int = ParamField(
        int16, "envSpc_2", default=0,
        tooltip="Changing this has drastic effects on the specular ambient light.",
    )
    SpecularLightTextureID3: int = ParamField(
        int16, "envSpc_3", default=0,
        tooltip="Changing this has drastic effects on the specular ambient light.",
    )
    _Pad0: bytes = ParamPad(2, "pad[2]")
