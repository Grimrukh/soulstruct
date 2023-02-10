from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


COMMON_SYSTEM_PARAM_ST = {
    "param_type": "COMMON_SYSTEM_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "mapSaveMapNameIdOnGameStart",
            "Save Data - Game Start: Map Name",
            True,
            int,
            'At the start of the game Map name ID_for save data (SEQ15052)',
        ),
        ParamFieldInfo(
            "reserve0[60]",
            "Reserve",
            False,
            pad_field(60),
            'Reserve',
        ),
    ],
}
