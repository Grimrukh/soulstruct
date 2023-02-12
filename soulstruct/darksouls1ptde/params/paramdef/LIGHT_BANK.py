from __future__ import annotations

__all__ = ["LIGHT_BANK"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class LIGHT_BANK(ParamRow):
    BakedLight0RotationX: int = ParamField(
        short, "degRotX_0", default=0,
        tooltip="Rotation (X-axis) of ambient (parallel) light source 0.",
    )
    BakedLight0RotationY: int = ParamField(
        short, "degRotY_0", default=0,
        tooltip="Rotation (Y-axis) of ambient (parallel) light source 0.",
    )
    BakedLight0Red: int = ParamField(
        short, "colR_0", default=255,
        tooltip="Red channel (0-255) of ambient (parallel) light source 0.",
    )
    BakedLight0Green: int = ParamField(
        short, "colG_0", default=255,
        tooltip="Green channel (0-255) of ambient (parallel) light source 0.",
    )
    BakedLight0Blue: int = ParamField(
        short, "colB_0", default=255,
        tooltip="Blue channel (0-255) of ambient (parallel) light source 0.",
    )
    BakedLight0Alpha: int = ParamField(
        short, "colA_0", default=100,
        tooltip="Alpha channel (0-255) of ambient (parallel) light source 0.",
    )
    BakedLight1RotationX: int = ParamField(
        short, "degRotX_1", default=0,
        tooltip="Rotation (X-axis) of ambient (parallel) light source 1.",
    )
    BakedLight1RotationY: int = ParamField(
        short, "degRotY_1", default=0,
        tooltip="Rotation (Y-axis) of ambient (parallel) light source 1.",
    )
    BakedLight1Red: int = ParamField(
        short, "colR_1", default=255,
        tooltip="Red channel (0-255) of ambient (parallel) light source 1.",
    )
    BakedLight1Green: int = ParamField(
        short, "colG_1", default=255,
        tooltip="Green channel (0-255) of ambient (parallel) light source 1.",
    )
    BakedLight1Blue: int = ParamField(
        short, "colB_1", default=255,
        tooltip="Blue channel (0-255) of ambient (parallel) light source 1.",
    )
    BakedLight1Alpha: int = ParamField(
        short, "colA_1", default=100,
        tooltip="Alpha channel (0-255) of ambient (parallel) light source 1.",
    )
    BakedLight2RotationX: int = ParamField(
        short, "degRotX_2", default=0,
        tooltip="Rotation (X-axis) of ambient (parallel) light source 2.",
    )
    BakedLight2RotationY: int = ParamField(
        short, "degRotY_2", default=0,
        tooltip="Rotation (Y-axis) of ambient (parallel) light source 2.",
    )
    BakedLight2Red: int = ParamField(
        short, "colR_2", default=255,
        tooltip="Red channel (0-255) of ambient (parallel) light source 2.",
    )
    BakedLight2Green: int = ParamField(
        short, "colG_2", default=255,
        tooltip="Green channel (0-255) of ambient (parallel) light source 2.",
    )
    BakedLight2Blue: int = ParamField(
        short, "colB_2", default=255,
        tooltip="Blue channel (0-255) of ambient (parallel) light source 2.",
    )
    BakedLight2Alpha: int = ParamField(
        short, "colA_2", default=100,
        tooltip="Alpha channel (0-255) of ambient (parallel) light source 2.",
    )
    TopDownLightRed: int = ParamField(
        short, "colR_u", default=255,
        tooltip="Red channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
                "surface is oriented sideways (e.g. walls).",
    )
    TopDownLightGreen: int = ParamField(
        short, "colG_u", default=255,
        tooltip="Green channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
                "surface is oriented sideways (e.g. walls).",
    )
    TopDownLightBlue: int = ParamField(
        short, "colB_u", default=255,
        tooltip="Blue channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
                "surface is oriented sideways (e.g. walls).",
    )
    TopDownLightAlpha: int = ParamField(
        short, "colA_u", default=100,
        tooltip="Alpha channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
                "surface is oriented sideways (e.g. walls).",
    )
    BottomUpLightRed: int = ParamField(
        short, "colR_d", default=255,
        tooltip="Red channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
                "the surface is oriented sideways (e.g. walls).",
    )
    BottomUpLightGreen: int = ParamField(
        short, "colG_d", default=255,
        tooltip="Green channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
                "the surface is oriented sideways (e.g. walls).",
    )
    BottomUpLightBlue: int = ParamField(
        short, "colB_d", default=255,
        tooltip="Blue channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
                "the surface is oriented sideways (e.g. walls).",
    )
    BottomUpLightAlpha: int = ParamField(
        short, "colA_d", default=100,
        tooltip="Alpha channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
                "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
                "the surface is oriented sideways (e.g. walls).",
    )
    SpecularBakedLightRotationX: int = ParamField(
        short, "degRotX_s", default=0,
        tooltip="Rotation (X-axis) of specular ambient (parallel) light source.",
    )
    SpecularBakedLightRotationY: int = ParamField(
        short, "degRotY_s", default=0,
        tooltip="Rotation (Y-axis) of specular ambient (parallel) light source.",
    )
    SpecularBakedLightRed: int = ParamField(
        short, "colR_s", default=255,
        tooltip="Red channel (0-255) of specular ambient light source.",
    )
    SpecularBakedLightGreen: int = ParamField(
        short, "colG_s", default=255,
        tooltip="Green channel (0-255) of specular ambient light source.",
    )
    SpecularBakedLightBlue: int = ParamField(
        short, "colB_s", default=255,
        tooltip="Blue channel (0-255) of specular ambient light source.",
    )
    SpecularBakedLightAlpha: int = ParamField(
        short, "colA_s", default=0,
        tooltip="Alpha channel (0-255) of specular ambient light source.",
    )
    DiffuseLightRed: int = ParamField(
        short, "envDif_colR", default=255,
        tooltip="Red channel (0-255) of base diffuse ambient light of surfaces.",
    )
    DiffuseLightGreen: int = ParamField(
        short, "envDif_colG", default=255,
        tooltip="Green channel (0-255) of base diffuse ambient light of surfaces.",
    )
    DiffuseLightBlue: int = ParamField(
        short, "envDif_colB", default=255,
        tooltip="Blue channel (0-255) of base diffuse ambient light of surfaces.",
    )
    DiffuseLightAlpha: int = ParamField(
        short, "envDif_colA", default=100,
        tooltip="Alpha channel (0-255) of base diffuse ambient light of surfaces.",
    )
    SpecularLightRed: int = ParamField(
        short, "envSpc_colR", default=255,
        tooltip="Red channel (0-255) of specular ambient light of surfaces.",
    )
    SpecularLightGreen: int = ParamField(
        short, "envSpc_colG", default=255,
        tooltip="Green channel (0-255) of specular ambient light of surfaces.",
    )
    SpecularLightBlue: int = ParamField(
        short, "envSpc_colB", default=255,
        tooltip="Blue channel (0-255) of specular ambient light of surfaces.",
    )
    SpecularLightAlpha: int = ParamField(
        short, "envSpc_colA", default=100,
        tooltip="Alpha channel (0-255) of specular ambient light of surfaces.",
    )
    DiffuseLightTextureID: int = ParamField(
        short, "envDif", default=0, hide=True,
        tooltip="Changing this has drastic effects on the diffuse ambient light.",
    )
    SpecularLightTextureID0: int = ParamField(
        short, "envSpc_0", default=0, hide=True,
        tooltip="Changing this has drastic effects on the specular ambient light.",
    )
    SpecularLightTextureID1: int = ParamField(
        short, "envSpc_1", default=0, hide=True,
        tooltip="Changing this has drastic effects on the specular ambient light.",
    )
    SpecularLightTextureID2: int = ParamField(
        short, "envSpc_2", default=0, hide=True,
        tooltip="Changing this has drastic effects on the specular ambient light.",
    )
    SpecularLightTextureID3: int = ParamField(
        short, "envSpc_3", default=0, hide=True,
        tooltip="Changing this has drastic effects on the specular ambient light.",
    )
    _Pad0: bytes = ParamPad(2, "pad[2]")
