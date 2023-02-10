from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


WAYPOINT_PARAM_ST = {
    "param_type": "WAYPOINT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "attribute1",
            "Attribute [1]",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "attribute2",
            "Attribute [2]",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "attribute3",
            "Attribute [3]",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "attribute4",
            "Attribute [4]",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "padding4[8]",
            "Padding 4",
            False,
            pad_field(8),
            '',
        ),
    ],
}
