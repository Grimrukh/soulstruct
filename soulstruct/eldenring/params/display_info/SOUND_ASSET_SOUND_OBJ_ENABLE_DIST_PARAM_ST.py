from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SOUND_ASSET_SOUND_OBJ_ENABLE_DIST_PARAM_ST = {
    "param_type": "SOUND_ASSET_SOUND_OBJ_ENABLE_DIST_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "SoundObjEnableDist",
            "Sound Object - Enable Distance",
            True,
            float,
            'Asset sound sound source effective distance [m] (less than 0: invalid)',
        ),
    ],
}
