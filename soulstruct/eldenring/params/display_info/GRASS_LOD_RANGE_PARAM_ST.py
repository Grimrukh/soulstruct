from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


GRASS_LOD_RANGE_PARAM_ST = {
    "param_type": "GRASS_LOD_RANGE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "LOD0_range",
            "LOD 0 - Distance",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "LOD0_play",
            "LOD 0 - Play",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "LOD1_range",
            "LOD 1 - Distance",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "LOD1_play",
            "LOD 1 - Play",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "LOD2_range",
            "LOD 2 - Distance",
            True,
            float,
            '',
        ),
        ParamFieldInfo(
            "LOD2_play",
            "LOD 2 - Play",
            True,
            float,
            '',
        ),
    ],
}
