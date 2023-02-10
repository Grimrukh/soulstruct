from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_DECAL_QUALITY_DETAIL = {
    "param_type": "CS_DECAL_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "enabled",
            "Decal Enabled",
            True,
            int,
            'Decal valid',
        ),
        ParamFieldInfo(
            "dmy[3]",
            "dmy",
            False,
            pad_field(3),
            '',
        ),
    ],
}
