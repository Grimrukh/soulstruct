from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CHARMAKEMENU_LISTITEM_PARAM_ST = {
    "param_type": "CHARMAKEMENU_LISTITEM_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "value",
            "Value",
            True,
            int,
            'The value handled by the program. Make serial numbers within one group',
        ),
        ParamFieldInfo(
            "captionId",
            "Caption ID",
            True,
            int,
            'ID of the text to be displayed',
        ),
        ParamFieldInfo(
            "iconId",
            "Icon ID",
            True,
            int,
            'ID of the icon to be displayed',
        ),
        ParamFieldInfo(
            "reserved[7]",
            "reserve",
            False,
            pad_field(7),
            '',
        ),
    ],
}
