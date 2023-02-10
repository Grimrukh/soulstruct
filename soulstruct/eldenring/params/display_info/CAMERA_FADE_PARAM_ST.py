from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CAMERA_FADE_PARAM_ST = {
    "param_type": "CAMERA_FADE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "NearMinDist",
            "Proximity Fade: Minimum Near Distance",
            True,
            float,
            'Near Fade minimum distance (m): Distance where �� = 0',
        ),
        ParamFieldInfo(
            "NearMaxDist",
            "Proximity Fade: Maximum Near Distance",
            True,
            float,
            'Near fade maximum distance (m): Starting distance between �� = Middel Alpha',
        ),
        ParamFieldInfo(
            "FarMinDist",
            "Proximity Fade: Minimum Far Distance",
            True,
            float,
            'Minimum distance of Far fade (m): End distance between �� = Middle Alpha',
        ),
        ParamFieldInfo(
            "FarMaxDist",
            "Proximity Fade: Maximum Far Distance",
            True,
            float,
            'Maximum Far Fade Distance (m): Distance where �� = 1',
        ),
        ParamFieldInfo(
            "MiddleAlpha",
            "Proximity Fade: Alpha",
            True,
            float,
            'Intermediate �� value',
        ),
        ParamFieldInfo(
            "dummy[12]",
            "dummy",
            False,
            pad_field(12),
            '',
        ),
    ],
}
