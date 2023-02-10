from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SOUND_COMMON_INGAME_PARAM_ST = {
    "param_type": "SOUND_COMMON_INGAME_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "ParamKeyStr[32]",
            "Param Key",
            True,
            str,
            'Key string of the parameter',
        ),
        ParamFieldInfo(
            "ParamValueStr[32]",
            "Param Value",
            True,
            str,
            'Value string of the parameter',
        ),
    ],
}
