from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


DIRECTION_CAMERA_PARAM_ST = {
    "param_type": "DIRECTION_CAMERA_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "isUseOption:1",
            "Is Use Option",
            True,
            int,
            'Is it affected by the production camera ON / OFF option?',
        ),
        ParamFieldInfo(
            "pad2:3",
            "pad",
            False,
            bit_pad_field(3),
            'pad',
        ),
        ParamFieldInfo(
            "pad1[15]",
            "pad",
            False,
            pad_field(15),
            'pad',
        ),
    ],
}
