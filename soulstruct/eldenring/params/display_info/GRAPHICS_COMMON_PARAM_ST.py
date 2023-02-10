from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


GRAPHICS_COMMON_PARAM_ST = {
    "param_type": "GRAPHICS_COMMON_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "hitBulletDecalOffset_HitIns",
            "Hit Bullet Decal Offset - Hit INS",
            True,
            float,
            'The position where the decal that occurs when hitting HIT INS is offset by this value in the normal direction.',
        ),
        ParamFieldInfo(
            "reserved02[8]",
            "reserve",
            False,
            pad_field(8),
            '(dummy8)',
        ),
        ParamFieldInfo(
            "charaWetDecalFadeRange",
            "Character Wet Decal Fade Range",
            True,
            float,
            'Fade range that erases decals when the character gets wet [m]',
        ),
        ParamFieldInfo(
            "reserved04[240]",
            "reserve",
            False,
            pad_field(240),
            '(dummy8)',
        ),
    ],
}
