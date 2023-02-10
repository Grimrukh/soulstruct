from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_WATER_QUALITY_DETAIL = {
    "param_type": "CS_WATER_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "interactionEnabled",
            "Interaction Enabled",
            True,
            int,
            'Interaction enabled',
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
