from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_LIGHTING_QUALITY_DETAIL = {
    "param_type": "CS_LIGHTING_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "localLightDistFactor",
            "Local Light Distance Factor",
            True,
            float,
            'Local light effective distance coefficient (smaller, it disappears at a short distance)',
        ),
        ParamFieldInfo(
            "localLightShadowEnabled",
            "Local Light Shadow Enabled",
            True,
            int,
            'Local light shadow enabled',
        ),
        ParamFieldInfo(
            "forwardPassLightingEnabled",
            "Forward Pass Write Enabled",
            True,
            int,
            'Forward pass writing enabled',
        ),
        ParamFieldInfo(
            "localLightShadowSpecLevelMax",
            "Local Light Shadow Specular Level",
            True,
            int,
            'Local light shadow spec level. The larger the value, the more light sources will be shadowed.',
        ),
        ParamFieldInfo(
            "dmy[1]",
            "dmy",
            False,
            pad_field(1),
            '',
        ),
    ],
}
