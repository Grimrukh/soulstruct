from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MENU_VALUE_TABLE_SPEC = {
    "param_type": "MENU_VALUE_TABLE_SPEC",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "value",
            "Value",
            True,
            int,
            'Value to compare',
        ),
        ParamFieldInfo(
            "textId",
            "Text ID",
            True,
            int,
            'Converted text ID',
        ),
        ParamFieldInfo(
            "compareType",
            "Compare Type",
            True,
            int,
            'Comparison type',
        ),
        ParamFieldInfo(
            "padding[3]",
            "Padding",
            False,
            pad_field(3),
            'Padding',
        ),
    ],
}
