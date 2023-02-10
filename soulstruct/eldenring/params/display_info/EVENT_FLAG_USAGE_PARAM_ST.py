from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


EVENT_FLAG_USAGE_PARAM_ST = {
    "param_type": "EVENT_FLAG_USAGE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "usageType",
            "Use",
            True,
            int,
            'Use of the flag.',
        ),
        ParamFieldInfo(
            "playlogCategory",
            "Playlog category",
            True,
            int,
            'Valid only when the usage is "ON / OFF". If this is set, the play log will be collected when the flag is turned ON.',
        ),
        ParamFieldInfo(
            "padding1[2]",
            "Padding",
            False,
            pad_field(2),
            'Padding',
        ),
        ParamFieldInfo(
            "flagNum",
            "Number of secured flags",
            True,
            int,
            'Set to 1 for "ON / OFF". In the case of "frame allocation" and "integer", "parameter number-parameter number + number of secured flags-1" is secured.',
        ),
        ParamFieldInfo(
            "padding2[24]",
            "Padding",
            False,
            pad_field(24),
            'Padding',
        ),
    ],
}
