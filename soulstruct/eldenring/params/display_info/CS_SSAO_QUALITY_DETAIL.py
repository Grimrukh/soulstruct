from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_SSAO_QUALITY_DETAIL = {
    "param_type": "CS_SSAO_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "enabled",
            "SSAO Enabled",
            True,
            int,
            'SSAO enabled',
        ),
        ParamFieldInfo(
            "cs_reprojEnabledType",
            "Reprojection Enabled",
            True,
            int,
            'When reprojection is forcibly enabled, Prevent Ghost is also enabled.',
        ),
        ParamFieldInfo(
            "cs_upScaleEnabledType",
            "Bilateral Upscale Enable Type",
            True,
            int,
            'Bilateral upscale effective',
        ),
        ParamFieldInfo(
            "cs_useNormalEnabledType",
            "Use Normal Enabled Type",
            True,
            int,
            'Valid to use normals',
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
