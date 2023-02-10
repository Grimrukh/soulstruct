from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_VOLUMETRIC_EFFECT_QUALITY_DETAIL = {
    "param_type": "CS_VOLUMETRIC_EFFECT_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "fogEnabled",
            "Fog Enabled",
            True,
            int,
            'Fog enabled',
        ),
        ParamFieldInfo(
            "fogShadowEnabled",
            "Fog Shadow Enabled",
            True,
            int,
            'Fog shadow permission',
        ),
        ParamFieldInfo(
            "dmy[2]",
            "dmy",
            False,
            pad_field(2),
            'dmy',
        ),
        ParamFieldInfo(
            "fogShadowSampleCountBias",
            "Shadow Sample Count Offset",
            True,
            int,
            'Shadow sample count offset.',
        ),
        ParamFieldInfo(
            "fogLocalLightDistScale",
            "Local Light Distance Scale",
            True,
            float,
            'Local light calculation distance scale (0 does not calculate local light)',
        ),
        ParamFieldInfo(
            "fogVolueSizeScaler",
            "Fog Volume Size Scaler",
            True,
            int,
            'Fog volume size scaler',
        ),
        ParamFieldInfo(
            "fogVolueSizeDivider",
            "Fog Volume Size Division",
            True,
            int,
            'Fog volume size division',
        ),
        ParamFieldInfo(
            "fogVolumeDepthScaler",
            "Fog Volume Depth Slice Scaler",
            True,
            int,
            'Fog Volume Depth Slice Scaler',
        ),
        ParamFieldInfo(
            "fogVolumeDepthDivider",
            "Fog Volume Depth Slice Division",
            True,
            int,
            'Fog volume depth slice division',
        ),
        ParamFieldInfo(
            "fogVolumeEnabled",
            "Arranged Fog Volume Enabled",
            True,
            int,
            'Arranged fog volume enabled',
        ),
        ParamFieldInfo(
            "fogVolumeUpScaleType",
            "Upscale Type",
            True,
            int,
            'Method type at the time of upscale',
        ),
        ParamFieldInfo(
            "fogVolumeEdgeCorrectionLevel",
            "Edge Correction Level",
            True,
            int,
            'Edge correction level performed only at bilateral (0: invalid, edge redraw permission at 1: 1 / 2x1 / 2 resolution, edge redraw permission with parameter reduction at 2: 1 / 2x1 / 2 + 1x1 resolution, 3 : 1 / 2x1 / 2 + 1x1 resolution edge redraw permission)',
        ),
        ParamFieldInfo(
            "fogVolumeRayMarcingSampleCountOffset",
            "Ray Sample Count Offset",
            True,
            int,
            'Offset of sampling number during ray marching',
        ),
        ParamFieldInfo(
            "fogVolumeShadowEnabled",
            "Fog Volume Shadow Enabled",
            True,
            int,
            'Shadow permission (refers to shadow processing due to density changes in the area, where shadows are cast on the area)',
        ),
        ParamFieldInfo(
            "fogVolumeForceShadowing",
            "Fog Volume - Force Shadowing",
            True,
            int,
            'Forcibly casts a shadow on the area regardless of the setting when shadow is permitted (shadow processing is not affected)',
        ),
        ParamFieldInfo(
            "fogVolumeResolution",
            "Fog Volume Resolution",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "pad2[1]",
            "pad",
            False,
            pad_field(1),
            '',
        ),
    ],
}
