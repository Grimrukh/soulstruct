__all__ = [
    "FOG_BANK",
    "LIGHT_BANK",
    "LIGHT_SCATTERING_BANK",
    "POINT_LIGHT_BANK",
    "LENS_FLARE_BANK",
    "LENS_FLARE_EX_BANK",
    "DOF_BANK",
    "TONE_MAP_BANK",
    "TONE_CORRECT_BANK",
    "SHADOW_BANK",
]

from soulstruct.base.params.utils import FieldDisplayInfo, pad_field

FOG_BANK = {
    "paramdef_name": "FOG_BANK",
    "file_name": "FogBank",
    "nickname": "Fog",
    "fields": [
        FieldDisplayInfo("fogBeginZ", "FogStartDistance", True, int, "Distance (m) at which fog begins."),
        FieldDisplayInfo("fogEndZ", "FogEndDistance", True, int, "Distance (m) at which fog ends."),
        FieldDisplayInfo("degRotZ", "RotationZ", True, int, "Rotation of fog around the Z axis."),
        FieldDisplayInfo("degRotW", "RotationW", True, int, "Rotation of fog around the W axis."),
        FieldDisplayInfo("colR", "Red", True, int, "Red color channel (0-255)."),
        FieldDisplayInfo("colG", "Green", True, int, "Green color channel (0-255)."),
        FieldDisplayInfo("colB", "Blue", True, int, "Blue color channel (0-255)."),
        FieldDisplayInfo("colA", "Alpha", True, int, "Alpha channel (0-255)."),
    ],
}

LIGHT_BANK = {
    "paramdef_name": "LIGHT_BANK",
    "file_name": "LightBank",
    "nickname": "AmbientLight",
    "fields": [
        FieldDisplayInfo(
            "degRotX_0",
            "AmbientLight0RotationX",
            True,
            int,
            "Rotation (X-axis) of ambient (parallel) light source 0.",
        ),
        FieldDisplayInfo(
            "degRotY_0",
            "AmbientLight0RotationY",
            True,
            int,
            "Rotation (Y-axis) of ambient (parallel) light source 0.",
        ),
        FieldDisplayInfo(
            "colR_0", "AmbientLight0Red", True, int, "Red channel (0-255) of ambient (parallel) light source 0."
        ),
        FieldDisplayInfo(
            "colG_0",
            "AmbientLight0Green",
            True,
            int,
            "Green channel (0-255) of ambient (parallel) light source 0.",
        ),
        FieldDisplayInfo(
            "colB_0", "AmbientLight0Blue", True, int, "Blue channel (0-255) of ambient (parallel) light source 0."
        ),
        FieldDisplayInfo(
            "colA_0",
            "AmbientLight0Alpha",
            True,
            int,
            "Alpha channel (0-255) of ambient (parallel) light source 0.",
        ),
        FieldDisplayInfo(
            "degRotX_1",
            "AmbientLight1RotationX",
            True,
            int,
            "Rotation (X-axis) of ambient (parallel) light source 1.",
        ),
        FieldDisplayInfo(
            "degRotY_1",
            "AmbientLight1RotationY",
            True,
            int,
            "Rotation (Y-axis) of ambient (parallel) light source 1.",
        ),
        FieldDisplayInfo(
            "colR_1", "AmbientLight1Red", True, int, "Red channel (0-255) of ambient (parallel) light source 1."
        ),
        FieldDisplayInfo(
            "colG_1",
            "AmbientLight1Green",
            True,
            int,
            "Green channel (0-255) of ambient (parallel) light source 1.",
        ),
        FieldDisplayInfo(
            "colB_1", "AmbientLight1Blue", True, int, "Blue channel (0-255) of ambient (parallel) light source 1."
        ),
        FieldDisplayInfo(
            "colA_1",
            "AmbientLight1Alpha",
            True,
            int,
            "Alpha channel (0-255) of ambient (parallel) light source 1.",
        ),
        FieldDisplayInfo(
            "degRotX_2",
            "AmbientLight2RotationX",
            True,
            int,
            "Rotation (X-axis) of ambient (parallel) light source 2.",
        ),
        FieldDisplayInfo(
            "degRotY_2",
            "AmbientLight2RotationY",
            True,
            int,
            "Rotation (Y-axis) of ambient (parallel) light source 2.",
        ),
        FieldDisplayInfo(
            "colR_2", "AmbientLight2Red", True, int, "Red channel (0-255) of ambient (parallel) light source 2."
        ),
        FieldDisplayInfo(
            "colG_2",
            "AmbientLight2Green",
            True,
            int,
            "Green channel (0-255) of ambient (parallel) light source 2.",
        ),
        FieldDisplayInfo(
            "colB_2", "AmbientLight2Blue", True, int, "Blue channel (0-255) of ambient (parallel) light source 2."
        ),
        FieldDisplayInfo(
            "colA_2",
            "AmbientLight2Alpha",
            True,
            int,
            "Alpha channel (0-255) of ambient (parallel) light source 2.",
        ),
        FieldDisplayInfo(
            "colR_u",
            "TopDownLightRed",
            True,
            int,
            "Red channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
            "surface is oriented sideways (e.g. walls).",
        ),
        FieldDisplayInfo(
            "colG_u",
            "TopDownLightGreen",
            True,
            int,
            "Green channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
            "surface is oriented sideways (e.g. walls).",
        ),
        FieldDisplayInfo(
            "colB_u",
            "TopDownLightBlue",
            True,
            int,
            "Blue channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
            "surface is oriented sideways (e.g. walls).",
        ),
        FieldDisplayInfo(
            "colA_u",
            "TopDownLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of ambient light of upward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly upward (e.g. floors) and decreases as a function of orientation until the "
            "surface is oriented sideways (e.g. walls).",
        ),
        FieldDisplayInfo(
            "colR_d",
            "BottomUpLightRed",
            True,
            int,
            "Red channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
            "the surface is oriented sideways (e.g. walls).",
        ),
        FieldDisplayInfo(
            "colG_d",
            "BottomUpLightGreen",
            True,
            int,
            "Green channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
            "the surface is oriented sideways (e.g. walls).",
        ),
        FieldDisplayInfo(
            "colB_d",
            "BottomUpLightBlue",
            True,
            int,
            "Blue channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
            "the surface is oriented sideways (e.g. walls).",
        ),
        FieldDisplayInfo(
            "colA_d",
            "BottomUpLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of ambient light of downward-facing surfaces. This has the largest effect for "
            "surfaces oriented exactly downward (e.g. ceilings) and decreases as a function of orientation until "
            "the surface is oriented sideways (e.g. walls).",
        ),
        FieldDisplayInfo(
            "degRotX_s",
            "SpecularAmbientLightRotationX",
            True,
            int,
            "Rotation (X-axis) of specular ambient (parallel) light source.",
        ),
        FieldDisplayInfo(
            "degRotY_s",
            "SpecularAmbientLightRotationY",
            True,
            int,
            "Rotation (Y-axis) of specular ambient (parallel) light source.",
        ),
        FieldDisplayInfo(
            "colR_s", "SpecularAmbientLightRed", True, int, "Red channel (0-255) of specular ambient light source."
        ),
        FieldDisplayInfo(
            "colG_s",
            "SpecularAmbientLightGreen",
            True,
            int,
            "Green channel (0-255) of specular ambient light source.",
        ),
        FieldDisplayInfo(
            "colB_s",
            "SpecularAmbientLightBlue",
            True,
            int,
            "Blue channel (0-255) of specular ambient light source.",
        ),
        FieldDisplayInfo(
            "colA_s",
            "SpecularAmbientLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of specular ambient light source.",
        ),
        FieldDisplayInfo(
            "envDif_colR",
            "DiffuseLightRed",
            True,
            int,
            "Red channel (0-255) of base diffuse ambient light of surfaces.",
        ),
        FieldDisplayInfo(
            "envDif_colG",
            "DiffuseLightGreen",
            True,
            int,
            "Green channel (0-255) of base diffuse ambient light of surfaces.",
        ),
        FieldDisplayInfo(
            "envDif_colB",
            "DiffuseLightBlue",
            True,
            int,
            "Blue channel (0-255) of base diffuse ambient light of surfaces.",
        ),
        FieldDisplayInfo(
            "envDif_colA",
            "DiffuseLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of base diffuse ambient light of surfaces.",
        ),
        FieldDisplayInfo(
            "envSpc_colR",
            "SpecularLightRed",
            True,
            int,
            "Red channel (0-255) of specular ambient light of surfaces.",
        ),
        FieldDisplayInfo(
            "envSpc_colG",
            "SpecularLightGreen",
            True,
            int,
            "Green channel (0-255) of specular ambient light of surfaces.",
        ),
        FieldDisplayInfo(
            "envSpc_colB",
            "SpecularLightBlue",
            True,
            int,
            "Blue channel (0-255) of specular ambient light of surfaces.",
        ),
        FieldDisplayInfo(
            "envSpc_colA",
            "SpecularLightAlpha",
            True,
            int,
            "Alpha channel (0-255) of specular ambient light of surfaces.",
        ),
        FieldDisplayInfo(
            "envDif",
            "DiffuseLightTextureID",
            False,
            int,
            "Changing this has drastic effects on the diffuse ambient light.",
        ),
        FieldDisplayInfo(
            "envSpc_0",
            "SpecularLightTextureID0",
            False,
            int,
            "Changing this has drastic effects on the specular ambient light.",
        ),
        FieldDisplayInfo(
            "envSpc_1",
            "SpecularLightTextureID1",
            False,
            int,
            "Changing this has drastic effects on the specular ambient light.",
        ),
        FieldDisplayInfo(
            "envSpc_2",
            "SpecularLightTextureID2",
            False,
            int,
            "Changing this has drastic effects on the specular ambient light.",
        ),
        FieldDisplayInfo(
            "envSpc_3",
            "SpecularLightTextureID3",
            False,
            int,
            "Changing this has drastic effects on the specular ambient light.",
        ),
        FieldDisplayInfo("pad[2]", "Pad1", False, pad_field(2), "Null padding."),
    ],
}

LIGHT_SCATTERING_BANK = {
    "paramdef_name": "LIGHT_SCATTERING_BANK",
    "file_name": "LightScatteringBank",
    "nickname": "ScatteredLight",
    "fields": [
        FieldDisplayInfo("sunRotX", "LightRotationX", True, int, "Rotation (X-axis) of scattering light source."),
        FieldDisplayInfo("sunRotY", "LightRotationY", True, int, "Rotation (Y-axis) of scattering light source."),
        FieldDisplayInfo(
            "distanceMul",
            "DistanceMultiplier",
            True,
            int,
            "Magnification (0-100) of scattering light source distance.",
        ),
        FieldDisplayInfo("sunR", "LightRed", True, int, "Red channel (0-255) of scattering light source."),
        FieldDisplayInfo("sunG", "LightGreen", True, int, "Green channel (0-255) of scattering light source."),
        FieldDisplayInfo("sunB", "LightBlue", True, int, "Blue channel (0-255) of scattering light source."),
        FieldDisplayInfo("sunA", "LightAlpha", True, int, "Alpha channel (0-255) of scattering light source."),
        FieldDisplayInfo("pad_0[2]", "Pad0", False, pad_field(2), "Null padding."),
        FieldDisplayInfo(
            "lsHGg",
            "ScatteringDirection",
            True,
            float,
            "Coefficient of scattering direction, between -1 (backward) and 1 (forward).",
        ),
        FieldDisplayInfo(
            "lsBetaRay",
            "RayleighCoefficient",
            True,
            float,
            "Coefficient determining how much light is lost to scattering (e.g. simulating amount of atmosphere).",
        ),
        FieldDisplayInfo(
            "lsBetaMie",
            "MieCoefficient",
            True,
            float,
            "Coefficient determining how much light is scattered by larger particles (e.g. simulating dust/smoke).",
        ),
        FieldDisplayInfo(
            "blendCoef",
            "ScatteringCoefficient",
            True,
            int,
            "Coefficient determining the overall amount of scattering from 0 (no scattering) to 100 (max "
            "scattering).",
        ),
        FieldDisplayInfo(
            "reflectanceR",
            "SurfaceReflectanceRed",
            True,
            int,
            "Red channel (0-255) of the effect of the scattered light as it hits surfaces.",
        ),
        FieldDisplayInfo(
            "reflectanceG",
            "SurfaceReflectanceGreen",
            True,
            int,
            "Green channel (0-255) of the effect of the scattered light as it hits surfaces.",
        ),
        FieldDisplayInfo(
            "reflectanceB",
            "SurfaceReflectanceBlue",
            True,
            int,
            "Blue channel (0-255) of the effect of the scattered light as it hits surfaces.",
        ),
        FieldDisplayInfo(
            "reflectanceA",
            "SurfaceReflectanceAlpha",
            True,
            int,
            "Alpha channel (0-255) of the effect of the scattered light as it hits surfaces.",
        ),
        FieldDisplayInfo("pad_1[2]", "Pad1", False, pad_field(2), "Null padding."),
    ],
}

POINT_LIGHT_BANK = {
    "paramdef_name": "POINT_LIGHT_BANK",
    "file_name": "PointLightBank",
    "nickname": "PointLights",
    "fields": [
        FieldDisplayInfo(
            "dwindleBegin",
            "FadeStartDistance",
            True,
            float,
            "Distance at which player's point light begins to fade.",
        ),
        FieldDisplayInfo(
            "dwindleEnd",
            "FadeEndDistance",
            True,
            float,
            "Distance at which player's point light finishes fading and disappears entirely.",
        ),
        FieldDisplayInfo("colR", "PointLightRed", True, int, "Red channel (0-255) of point light."),
        FieldDisplayInfo("colG", "PointLightGreen", True, int, "Green channel (0-255) of point light."),
        FieldDisplayInfo("colB", "PointLightBlue", True, int, "Blue channel (0-255) of point light."),
        FieldDisplayInfo("colA", "PointLightAlpha", True, int, "Alpha channel (0-255) of point light."),
    ],
}

LENS_FLARE_BANK = {
    "paramdef_name": "LENS_FLARE_BANK",
    "file_name": "LensFlareBank",
    "nickname": "LensFlares",
    "fields": [
        FieldDisplayInfo(
            "texId",
            "LensFlareTextureID",
            True,
            int,
            "Texture ID of lens flare (texture name format is 'lensflare_XX'). -1 means disabled.",
        ),
        FieldDisplayInfo("isFlare", "IsLensFlare", True, bool, "Flare if enabled, or 'ghost' if disabled."),
        FieldDisplayInfo("enableRoll", "EnableRotation", True, bool, "Allows lens flare texture to rotate with camera."),
        FieldDisplayInfo(
            "enableScale", "EnableScaling", True, bool, "Allows lens flare texture to change scale with camera."
        ),
        FieldDisplayInfo(
            "locateDistRate",
            "PositionRatio",
            True,
            float,
            "Relative position of lens flare between light source (0.0) and center of screen (1.0).",
        ),
        FieldDisplayInfo("texScale", "TextureScale", True, float, "Base scaling of lens flare texture."),
        FieldDisplayInfo("colR", "TextureRed", True, int, "Red channel (0-255) of lens flare texture."),
        FieldDisplayInfo("colG", "TextureGreen", True, int, "Green channel (0-255) of lens flare texture."),
        FieldDisplayInfo("colB", "TextureBlue", True, int, "Blue channel (0-255) of lens flare texture."),
        FieldDisplayInfo("colA", "TextureAlpha", True, int, "Alpha channel (0-255) of lens flare texture."),
    ],
}

LENS_FLARE_EX_BANK = {
    "paramdef_name": "LENS_FLARE_EX_BANK",
    "file_name": "LensFlareExBank",
    "nickname": "LensFlareSources",
    "fields": [
        FieldDisplayInfo(
            "lightDegRotX",
            "LensFlareSourceRotationX",
            True,
            int,
            "Rotation (X-axis) of visible light source (e.g. sun) that causes lens flares.",
        ),
        FieldDisplayInfo(
            "lightDegRotY",
            "LensFlareSourceRotationY",
            True,
            int,
            "Rotation (Y-axis) of visible light source (e.g. sun) that causes lens flares.",
        ),
        FieldDisplayInfo(
            "colR", "LensFlareSourceRed", True, int, "Red channel (0-255) of visible light source (e.g. sun)."
        ),
        FieldDisplayInfo(
            "colG", "LensFlareSourceGreen", True, int, "Green channel (0-255) of visible light source (e.g. sun)."
        ),
        FieldDisplayInfo(
            "colB", "LensFlareSourceBlue", True, int, "Blue channel (0-255) of visible light source (e.g. sun)."
        ),
        FieldDisplayInfo(
            "colA", "LensFlareSourceAlpha", True, int, "Alpha channel (0-255) of visible light source (e.g. sun)."
        ),
        FieldDisplayInfo(
            "lightDist",
            "LensFlareSourceDistance",
            True,
            float,
            "Distance of visible light source (e.g. sun). Not sure about the units.",
        ),
    ],
}

DOF_BANK = {
    "paramdef_name": "DOF_BANK",
    "file_name": "DofBank",
    "nickname": "DepthOfField",
    "fields": [
        FieldDisplayInfo(
            "farDofBegin",
            "FarBlurStartDistance",
            True,
            float,
            "Distance (m) at which far depth of field blur begins.",
        ),
        FieldDisplayInfo(
            "farDofEnd",
            "FarBlurEndDistance",
            True,
            float,
            "Distance (m) at which far depth of field blur ends (reaches maximum).",
        ),
        FieldDisplayInfo(
            "farDofMul",
            "FarBlurMagnitude",
            True,
            int,
            "Amount of far depth of field blur applied between the start and end distances.",
        ),
        FieldDisplayInfo("pad_0[3]", "Pad0", False, pad_field(3), "Null padding."),
        FieldDisplayInfo(
            "nearDofBegin",
            "NearBlurStartDistance",
            True,
            float,
            "Distance (m) at which near depth of field blur begins (further away than end distance).",
        ),
        FieldDisplayInfo(
            "nearDofEnd",
            "NearBlurEndDistance",
            True,
            float,
            "Distance (m) at which near depth of field blur ends (reaches maximum) (closer than start distance).",
        ),
        FieldDisplayInfo(
            "nearDofMul",
            "NearBlurMagnitude",
            True,
            int,
            "Amount of near depth of field blur applied between start and end distances.",
        ),
        FieldDisplayInfo("pad_1[3]", "Pad1", False, pad_field(3), "Null padding."),
        FieldDisplayInfo(
            "dispersionSq",
            "BlurSquaredDispersion",
            True,
            float,
            "Squared dispersion of depth of field blur (greater value means more blur).",
        ),
    ],
}

TONE_MAP_BANK = {
    "paramdef_name": "TONE_MAP_BANK",
    "file_name": "ToneMapBank",
    "nickname": "ToneMapping",
    "fields": [
        FieldDisplayInfo(
            "bloomBegin",
            "NearBloomThreshold",
            True,
            int,
            "Near light blooming begins when brightness exceeds this threshold.",
        ),
        FieldDisplayInfo("bloomMul", "NearBloomMultiplier", True, int, "Near light blooming multiplier."),
        FieldDisplayInfo(
            "bloomBeginFar",
            "FarBloomThreshold",
            True,
            int,
            "Far light blooming begins when brightness exceeds this threshold.",
        ),
        FieldDisplayInfo("bloomMulFar", "FarBloomMultiplier", True, int, "Far light blooming multiplier."),
        FieldDisplayInfo(
            "bloomNearDist",
            "NearBloomEndDistance",
            True,
            float,
            "Near bloom parameters apply up to this maximum distance.",
        ),
        FieldDisplayInfo(
            "bloomFarDist",
            "FarBloomStartDistance",
            True,
            float,
            "Far bloom parameters apply beyond this minimum distance.",
        ),
        FieldDisplayInfo(
            "grayKeyValue", "OverallBrightness", True, float, "Larger values make the screen brighter overall."
        ),
        FieldDisplayInfo(
            "minAdaptedLum",
            "MinimumAdaptationBrightness",
            True,
            float,
            "Minimum brightness for tone adaptation. Smaller values mean that darker places will be adapted.",
        ),
        FieldDisplayInfo(
            "maxAdapredLum",  # NOT A TYPO
            "MaximumAdaptationBrightness",
            True,
            float,
            "Maximum brightness for tone adaptation. Larger values mean that brighter places will be adapted.",
        ),
        FieldDisplayInfo("adaptSpeed", "AdaptationSpeed", True, float, "Tone adaptation speed."),
        FieldDisplayInfo(
            "lightShaftBegin",
            "LightShaftThreshold",
            True,
            int,
            "Light shafts will appear when brightness exceeds this threshold.",
        ),
        FieldDisplayInfo("pad_0[3]", "Pad0", True, pad_field(3), "Null padding."),
        FieldDisplayInfo(
            "lightShaftPower",
            "LightShaftMagnitude",
            True,
            float,
            "Light shaft magnitude (0 means no light shafts).",
        ),
        FieldDisplayInfo(
            "lightShaftAttenRate",
            "LightShaftAttenuationRate",
            True,
            float,
            "Smaller values will shorten the light shafts more.",
        ),
    ],
}

TONE_CORRECT_BANK = {
    "paramdef_name": "TONE_CORRECT_BANK",
    "file_name": "ToneCorrectBank",
    "nickname": "ToneCorrection",
    "fields": [
        FieldDisplayInfo(
            "brightnessR", "BrightnessRed", True, float, "Red channel (relative to 1) of tone correct brightness."
        ),
        FieldDisplayInfo(
            "brightnessG", "BrightnessGreen", True, float, "Green channel (relative to 1) of tone correct brightness."
        ),
        FieldDisplayInfo(
            "brightnessB", "BrightnessBlue", True, float, "Blue channel (relative to 1) of tone correct brightness."
        ),
        FieldDisplayInfo(
            "contrastR", "ContrastRed", True, float, "Red channel (relative to 1) of tone correct contrast."
        ),
        FieldDisplayInfo(
            "contrastG", "ContrastGreen", True, float, "Green channel (relative to 1) of tone correct contrast."
        ),
        FieldDisplayInfo(
            "contrastB", "ContrastBlue", True, float, "Blue channel (relative to 1) of tone correct contrast."
        ),
        FieldDisplayInfo("saturation", "SaturationCorrection", True, float, "Color saturation correction value."),
        FieldDisplayInfo("hue", "HueCorrection", True, float, "Color hue correction value."),
    ],
}

SHADOW_BANK = {
    "paramdef_name": "SHADOW_BANK",
    "file_name": "ShadowBank",
    "nickname": "Shadows",
    "fields": [
        FieldDisplayInfo(
            "lightDegRotX", "ShadowSourceRotationX", True, int, "Rotation (X-axis) of shadow-casting light source."
        ),
        FieldDisplayInfo(
            "lightDegRotY", "ShadowSourceRotationY", True, int, "Rotation (Y-axis) of shadow-casting light source."
        ),
        FieldDisplayInfo(
            "densityRatio",
            "ShadowDensityPercentage",
            True,
            int,
            "Density of cast shadow (0-100), where 100 is the darkest.",
        ),
        FieldDisplayInfo("colR", "ShadowRed", True, int, "Red channel (0-255) of cast shadow."),
        FieldDisplayInfo("colG", "ShadowGreen", True, int, "Green channel (0-255) of cast shadow."),
        FieldDisplayInfo("colB", "ShadowBlue", True, int, "Blue channel (0-255) of cast shadow."),
        FieldDisplayInfo(
            "beginDist",
            "ShadowStartDistance",
            True,
            float,
            "Minimum distance (m) at which shadows are cast. A value of 0 means the camera's near-clip plane is "
            "used.",
        ),
        FieldDisplayInfo("endDist", "ShadowEndDistance", True, float, "Maximum distance (m) at which shadows are cast."),
        FieldDisplayInfo(
            "calibulateFar",
            "HeadOnDistanceReduction",
            True,
            float,
            "Shorten the shadow end distance by this distance when facing the light source direction.",
        ),
        FieldDisplayInfo("fadeBeginDist", "FadeStartDistance", True, float, "Shadow starts fading at this distance."),
        FieldDisplayInfo(
            "fadeDist", "FadeDistance", True, float, "Distance (after start distance) until shadow is fully faded."
        ),
        FieldDisplayInfo(
            "persedDepthOffset",
            "DepthOffset",
            True,
            float,
            "Depth offset for shadows. With negative values, self-shadows are less likely to occur.",
        ),
        FieldDisplayInfo(
            "ｇradFactor",
            "ShadowMapStrength",
            True,
            float,
            "Negative values weaken the shadow map, positive values strengthen it.",
        ),
        FieldDisplayInfo(
            "shadowVolumeDepth",
            "ShadowVolumeDepth",
            True,
            float,
            "Increase this value to cast shadows on tall objects such as buildings.",
        ),
    ],
}

# 'LENS_FLAG_EX_BANK': 'LensFlareExBank',  # unused
# 'ENV_LIGHT_TEX_BANK': 'EnvLightTexBank',  # unused
# 'LOD_BANK': 'LodBank',  # unused
