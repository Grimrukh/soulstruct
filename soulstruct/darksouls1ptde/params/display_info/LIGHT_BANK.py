from __future__ import annotations

__all__ = ["LIGHT_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field


LIGHT_BANK = {
    "param_type": "LIGHT_BANK",
    "file_name": "LightBank",
    "nickname": "BakedLight",
    "fields": [
        ParamFieldInfo(
            "degRotX_0",
            "BakedLight0RotationX",
            True,
            int,
            "Rotation (X-axis) of ambient (parallel) light source 0.",
        ),
        ParamFieldInfo(
            "degRotY_0",
            "BakedLight0RotationY",
            True,
            int,
            "Rotation (Y-axis) of ambient (parallel) light source 0.",
        ),
        ParamFieldInfo(
            "colR_0", "BakedLight0Red", True, int, "Red channel (0-255) of ambient (parallel) light source 0."
        ),
        ParamFieldInfo(
            "colG_0",
            "BakedLight0Green",
            True,
            int,
            "Green channel (0-255) of ambient (parallel) light source 0.",
        ),
        ParamFieldInfo(
            "colB_0", "BakedLight0Blue", True, int, "Blue channel (0-255) of ambient (parallel) light source 0."
        ),
        ParamFieldInfo(
            "colA_0",
            "BakedLight0Alpha",
            True,
            int,
            "Alpha channel (0-255) of ambient (parallel) light source 0.",
        ),
        ParamFieldInfo(
            "degRotX_1",
            "BakedLight1RotationX",
            True,
            int,
            "Rotation (X-axis) of ambient (parallel) light source 1.",
        ),
        ParamFieldInfo(
            "degRotY_1",
            "BakedLight1RotationY",
            True,
            int,
            "Rotation (Y-axis) of ambient (parallel) light source 1.",
        ),
        ParamFieldInfo(
            "colR_1", "BakedLight1Red", True, int, "Red channel (0-255) of ambient (parallel) light source 1."
        ),
        ParamFieldInfo(
            "colG_1",
            "BakedLight1Green",
            True,
            int,
            "Green channel (0-255) of ambient (parallel) light source 1.",
        ),
        ParamFieldInfo(
            "colB_1", "BakedLight1Blue", True, int, "Blue channel (0-255) of ambient (parallel) light source 1."
        ),
        ParamFieldInfo(
            "colA_1",
            "BakedLight1Alpha",
            True,
            int,
            "Alpha channel (0-255) of ambient (parallel) light source 1.",
        ),
        ParamFieldInfo(
            "degRotX_2",
            "BakedLight2RotationX",
            True,
            int,
            "Rotation (X-axis) of ambient (parallel) light source 2.",
        ),
        ParamFieldInfo(
            "degRotY_2",
            "BakedLight2RotationY",
            True,
            int,
            "Rotation (Y-axis) of ambient (parallel) light source 2.",
        ),
        ParamFieldInfo(
            "colR_2", "BakedLight2Red", True, int, "Red channel (0-255) of ambient (parallel) light source 2."
        ),
        ParamFieldInfo(
            "colG_2",
            "BakedLight2Green",
            True,
            int,
            "Green channel (0-255) of ambient (parallel) light source 2.",
        ),
        ParamFieldInfo(
            "colB_2", "BakedLight2Blue", True, int, "Blue channel (0-255) of ambient (parallel) light source 2."
        ),
        ParamFieldInfo(
            "colA_2",
            "BakedLight2Alpha",
            True,
            int,
            "Alpha channel (0-255) of ambient (parallel) light source 2.",
        ),
        ParamFieldInfo(
            "colR_u",
            "TopDownLightRed",
            True,
            int,
            "Red channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
            "surface is oriented sideways (e.g. walls).",
        ),
        ParamFieldInfo(
            "colG_u",
            "TopDownLightGreen",
            True,
            int,
            "Green channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
            "surface is oriented sideways (e.g. walls).",
        ),
        ParamFieldInfo(
            "colB_u",
            "TopDownLightBlue",
            True,
            int,
            "Blue channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
            "surface is oriented sideways (e.g. walls).",
        ),
        ParamFieldInfo(
            "colA_u",
            "TopDownLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
            "surface is oriented sideways (e.g. walls).",
        ),
        ParamFieldInfo(
            "colR_d",
            "BottomUpLightRed",
            True,
            int,
            "Red channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
            "the surface is oriented sideways (e.g. walls).",
        ),
        ParamFieldInfo(
            "colG_d",
            "BottomUpLightGreen",
            True,
            int,
            "Green channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
            "the surface is oriented sideways (e.g. walls).",
        ),
        ParamFieldInfo(
            "colB_d",
            "BottomUpLightBlue",
            True,
            int,
            "Blue channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
            "the surface is oriented sideways (e.g. walls).",
        ),
        ParamFieldInfo(
            "colA_d",
            "BottomUpLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
            "the surface is oriented sideways (e.g. walls).",
        ),
        ParamFieldInfo(
            "degRotX_s",
            "SpecularBakedLightRotationX",
            True,
            int,
            "Rotation (X-axis) of specular ambient (parallel) light source.",
        ),
        ParamFieldInfo(
            "degRotY_s",
            "SpecularBakedLightRotationY",
            True,
            int,
            "Rotation (Y-axis) of specular ambient (parallel) light source.",
        ),
        ParamFieldInfo(
            "colR_s", "SpecularBakedLightRed", True, int, "Red channel (0-255) of specular ambient light source."
        ),
        ParamFieldInfo(
            "colG_s",
            "SpecularBakedLightGreen",
            True,
            int,
            "Green channel (0-255) of specular ambient light source.",
        ),
        ParamFieldInfo(
            "colB_s",
            "SpecularBakedLightBlue",
            True,
            int,
            "Blue channel (0-255) of specular ambient light source.",
        ),
        ParamFieldInfo(
            "colA_s",
            "SpecularBakedLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of specular ambient light source.",
        ),
        ParamFieldInfo(
            "envDif_colR",
            "DiffuseLightRed",
            True,
            int,
            "Red channel (0-255) of base diffuse ambient light of surfaces.",
        ),
        ParamFieldInfo(
            "envDif_colG",
            "DiffuseLightGreen",
            True,
            int,
            "Green channel (0-255) of base diffuse ambient light of surfaces.",
        ),
        ParamFieldInfo(
            "envDif_colB",
            "DiffuseLightBlue",
            True,
            int,
            "Blue channel (0-255) of base diffuse ambient light of surfaces.",
        ),
        ParamFieldInfo(
            "envDif_colA",
            "DiffuseLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of base diffuse ambient light of surfaces.",
        ),
        ParamFieldInfo(
            "envSpc_colR",
            "SpecularLightRed",
            True,
            int,
            "Red channel (0-255) of specular ambient light of surfaces.",
        ),
        ParamFieldInfo(
            "envSpc_colG",
            "SpecularLightGreen",
            True,
            int,
            "Green channel (0-255) of specular ambient light of surfaces.",
        ),
        ParamFieldInfo(
            "envSpc_colB",
            "SpecularLightBlue",
            True,
            int,
            "Blue channel (0-255) of specular ambient light of surfaces.",
        ),
        ParamFieldInfo(
            "envSpc_colA",
            "SpecularLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of specular ambient light of surfaces.",
        ),
        ParamFieldInfo(
            "envDif",
            "DiffuseLightTextureID",
            False,
            int,
            "Changing this has drastic effects on the diffuse ambient light.",
        ),
        ParamFieldInfo(
            "envSpc_0",
            "SpecularLightTextureID0",
            False,
            int,
            "Changing this has drastic effects on the specular ambient light.",
        ),
        ParamFieldInfo(
            "envSpc_1",
            "SpecularLightTextureID1",
            False,
            int,
            "Changing this has drastic effects on the specular ambient light.",
        ),
        ParamFieldInfo(
            "envSpc_2",
            "SpecularLightTextureID2",
            False,
            int,
            "Changing this has drastic effects on the specular ambient light.",
        ),
        ParamFieldInfo(
            "envSpc_3",
            "SpecularLightTextureID3",
            False,
            int,
            "Changing this has drastic effects on the specular ambient light.",
        ),
        ParamFieldInfo("pad[2]", "Pad1", False, pad_field(2), "Null padding."),
    ],
}
