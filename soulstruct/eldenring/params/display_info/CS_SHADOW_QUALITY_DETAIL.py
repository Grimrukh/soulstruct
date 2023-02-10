from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_SHADOW_QUALITY_DETAIL = {
    "param_type": "CS_SHADOW_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "enabled",
            "Shadow Enabled",
            True,
            int,
            'Shadow is enabled',
        ),
        ParamFieldInfo(
            "maxFilterLevel",
            "Maximum Filter Level",
            True,
            int,
            'Maximum filter quality allowed',
        ),
        ParamFieldInfo(
            "dmy[2]",
            "dmy",
            False,
            pad_field(2),
            '',
        ),
        ParamFieldInfo(
            "textureSizeScaler",
            "Texture Size Scalar",
            True,
            int,
            'Scaler with set shadow map resolution',
        ),
        ParamFieldInfo(
            "textureSizeDivider",
            "Texture Size Division",
            True,
            int,
            'Divide the set shadow map resolution',
        ),
        ParamFieldInfo(
            "textureMinSize",
            "Minimum Resolution",
            True,
            int,
            'Clamp resolution',
        ),
        ParamFieldInfo(
            "textureMaxSize",
            "Maximum Resolution",
            True,
            int,
            'Clamp the resolution. It will be the resolution judgment for each cascade',
        ),
        ParamFieldInfo(
            "blurCountBias",
            "Blur Count Bias",
            True,
            int,
            'Blur count bias (set count bias, unchanged at 0)',
        ),
    ],
}
