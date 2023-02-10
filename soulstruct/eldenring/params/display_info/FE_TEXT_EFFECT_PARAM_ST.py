from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


FE_TEXT_EFFECT_PARAM_ST = {
    "param_type": "FE_TEXT_EFFECT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "resId",
            "Resource ID",
            True,
            int,
            'Instance name of the menu resource. ID of TextEffect_X',
        ),
        ParamFieldInfo(
            "pad1[2]",
            "Padding",
            False,
            pad_field(2),
            '',
        ),
        ParamFieldInfo(
            "textId",
            "Text ID",
            True,
            int,
            'Text ID to display (-1: No text). MenuText',
        ),
        ParamFieldInfo(
            "seId",
            "SE ID",
            True,
            int,
            'Voice ID to play (-1: No SE)',
        ),
        ParamFieldInfo(
            "canMixMapName:1",
            "Display Simultaneously with Map Name",
            True,
            int,
            'Whether to display at the same time as the map name',
        ),
        ParamFieldInfo(
            "pad3:7",
            "Padding",
            False,
            bit_pad_field(7),
            '',
        ),
        ParamFieldInfo(
            "pad2[19]",
            "Padding",
            False,
            pad_field(19),
            '',
        ),
    ],
}
