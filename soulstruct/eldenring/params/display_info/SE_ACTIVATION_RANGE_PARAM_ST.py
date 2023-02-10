from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SE_ACTIVATION_RANGE_PARAM_ST = {
    "param_type": "SE_ACTIVATION_RANGE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "activateRange",
            "Activation Range",
            True,
            float,
            'Distance to enable placement SE (m) (0 or less: always enabled)',
        ),
    ],
}
