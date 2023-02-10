from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MENUPROPERTY_SPEC = {
    "param_type": "MENUPROPERTY_SPEC",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "CaptionTextID",
            "Caption Text ID",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "IconID",
            "Icon ID",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "RequiredPropertyID",
            "Required Property ID",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "CompareType",
            "Compare Type",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "pad2[1]",
            "Padding",
            False,
            pad_field(1),
            '',
        ),
        ParamFieldInfo(
            "FormatType",
            "Format Type",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "pad[16]",
            "Padding",
            False,
            pad_field(16),
            '',
        ),
    ],
}
