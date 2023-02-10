from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


AUTO_CREATE_ENV_SOUND_PARAM_ST = {
    "param_type": "AUTO_CREATE_ENV_SOUND_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "RangeMin",
            "Appearance Distance - Min",
            True,
            float,
            'Appearance distance Min [m]',
        ),
        ParamFieldInfo(
            "RangeMax",
            "Appearance Distance - Max",
            True,
            float,
            'Appearance distance Max [',
        ),
        ParamFieldInfo(
            "LifeTimeMin",
            "Duration - Min",
            True,
            float,
            'Lifespan Min [seconds]',
        ),
        ParamFieldInfo(
            "LifeTimeMax",
            "Duration - Max",
            True,
            float,
            'Lifespan Max [seconds]',
        ),
        ParamFieldInfo(
            "DeleteDist",
            "Delete Distance",
            True,
            float,
            'Delete distance [m]',
        ),
        ParamFieldInfo(
            "NearDist",
            "Near Distance",
            True,
            float,
            'Neighborhood judgment distance [m]',
        ),
        ParamFieldInfo(
            "LimiteRotateMin",
            "Generation Angle Limit - Min",
            True,
            float,
            'Angle limit Min [degree] (Specify the Y-axis angle +-in front of the camera. 180 is omnidirectional)',
        ),
        ParamFieldInfo(
            "LimiteRotateMax",
            "Generation Angle Limit - Max",
            True,
            float,
            'Angle limit Max [degree] (Specify the Y-axis angle +-in front of the camera. 180 is omnidirectional)',
        ),
    ],
}
