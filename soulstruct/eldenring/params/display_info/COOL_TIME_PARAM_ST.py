from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


COOL_TIME_PARAM_ST = {
    "param_type": "COOL_TIME_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "limitationTime",
            "Limitation Time - 3 Co-op Phantoms",
            True,
            float,
            'Time limit [sec] (number of cooperating spirits 3)',
        ),
        ParamFieldInfo(
            "observeTime",
            "Observation Time - 3 Co-op Phantoms",
            True,
            float,
            'Monitoring time [sec] (number of cooperating spirits 3)',
        ),
    ],
}
