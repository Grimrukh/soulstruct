from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_SHADER_QUALITY_DETAIL = {
    "param_type": "CS_SHADER_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "sssEnabled",
            "SSS Enabled",
            True,
            int,
            'SSS enabled',
        ),
        ParamFieldInfo(
            "tessellationEnabled",
            "Tessellation Enabled",
            True,
            int,
            'Tessellation enabled',
        ),
        ParamFieldInfo(
            "highPrecisionNormalEnabled",
            "High Precision Normal Enabled",
            True,
            int,
            'High precision normal valid (setting the accuracy of the normal stored in G-Buffer)',
        ),
        ParamFieldInfo(
            "dmy[1]",
            "dmy",
            True,
            str,
            '',
        ),
    ],
}
