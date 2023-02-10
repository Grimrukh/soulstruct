from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


BULLET_CREATE_LIMIT_PARAM_ST = {
    "param_type": "BULLET_CREATE_LIMIT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "limitNum_byGroup",
            "Max Amount - By Group",
            True,
            int,
            'Maximum number of creations in the same group',
        ),
        ParamFieldInfo(
            "isLimitEachOwner:1",
            "Is Limited for each Owner",
            True,
            int,
            'Is it restricted for each owner?',
        ),
        ParamFieldInfo(
            "pad2:7",
            "Padding",
            False,
            bit_pad_field(7),
            'pad2',
        ),
        ParamFieldInfo(
            "pad[30]",
            "Padding",
            False,
            pad_field(30),
            'pad3',
        ),
    ],
}
