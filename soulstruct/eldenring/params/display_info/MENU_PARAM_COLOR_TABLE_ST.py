from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MENU_PARAM_COLOR_TABLE_ST = {
    "param_type": "MENU_PARAM_COLOR_TABLE_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "lerpMode",
            "Lerp Mode",
            True,
            int,
            'Interpolation method',
        ),
        ParamFieldInfo(
            "pad1[3]",
            "pad",
            False,
            pad_field(3),
            '',
        ),
        ParamFieldInfo(
            "h",
            "Hue",
            True,
            int,
            'Hue. Treat as a fixed value in interpolation',
        ),
        ParamFieldInfo(
            "pad2[2]",
            "pad",
            False,
            pad_field(2),
            '',
        ),
        ParamFieldInfo(
            "s1",
            "Saturation [1]",
            True,
            float,
            'Saturation 1. Treated as the first point of interpolation',
        ),
        ParamFieldInfo(
            "v1",
            "Brightness [1]",
            True,
            float,
            'Brightness 1. Treated as the first point of interpolation',
        ),
        ParamFieldInfo(
            "s2",
            "Saturation [2]",
            True,
            float,
            'Saturation 2. Treated as the second point of interpolation',
        ),
        ParamFieldInfo(
            "v2",
            "Brightness [2]",
            True,
            float,
            'Brightness 2. Treated as the second point of interpolation',
        ),
        ParamFieldInfo(
            "s3",
            "Saturation [3]",
            True,
            float,
            'Saturation 3. Treated as the third point of interpolation',
        ),
        ParamFieldInfo(
            "v3",
            "Brightness [3]",
            True,
            float,
            'Brightness 3. Treated as the third point of interpolation',
        ),
    ],
}
