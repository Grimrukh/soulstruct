from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MENUPROPERTY_LAYOUT = {
    "param_type": "MENUPROPERTY_LAYOUT",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "LayoutPath[16]",
            "Layout Path",
            True,
            str,
            '',
        ),
        ParamFieldInfo(
            "PropertyID",
            "Menu Property ID",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "CaptionTextID",
            "Caption Text ID",
            True,
            int,
            'If a valid text ID is set, this will be displayed in preference to the property name.',
        ),
        ParamFieldInfo(
            "HelpTextID",
            "Help Text ID",
            True,
            int,
            'Only if this is a valid text ID will it be selectable in the field help.',
        ),
        ParamFieldInfo(
            "reserved[4]",
            "reserve",
            False,
            pad_field(4),
            '',
        ),
    ],
}
