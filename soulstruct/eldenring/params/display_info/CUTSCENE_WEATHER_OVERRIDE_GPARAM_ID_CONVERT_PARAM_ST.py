from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CUTSCENE_WEATHER_OVERRIDE_GPARAM_ID_CONVERT_PARAM_ST = {
    "param_type": "CUTSCENE_WEATHER_OVERRIDE_GPARAM_ID_CONVERT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "weatherOverrideGparamId",
            "Weather Override GPARAM ID",
            True,
            int,
            'The ID of the ?? part of s00_00_0000_WeatherOverride_ ??. Gparam',
        ),
    ],
}
