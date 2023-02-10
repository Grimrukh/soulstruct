from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


GRASS_MAP_SETTINGS_PARAM_ST = {
    "param_type": "GRASS_MAP_SETTINGS_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "grassType0",
            "Grass Type [0]",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "grassType1",
            "Grass Type [1]",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "grassType2",
            "Grass Type [2]",
            True,
            int,
            '',
        ),
    ],
}
