from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


WWISE_VALUE_TO_STR_CONVERT_PARAM_ST = {
    "param_type": "WWISE_VALUE_TO_STR_CONVERT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "disableParam_NT:1",
            "Disable Param - Network Test",
            True,
            int,
            'Parameters marked with Åõ are excluded in the NT version package.',
        ),
        ParamFieldInfo(
            "disableParamReserve1:7",
            "Reserve for package output 1",
            False,
            bit_pad_field(7),
            'Reserve for package output 1',
        ),
        ParamFieldInfo(
            "disableParamReserve2[3]",
            "Reserve for package output 2",
            False,
            pad_field(3),
            'Reserve for package output 2',
        ),
        ParamFieldInfo(
            "ParamStr[32]",
            "Param String",
            True,
            str,
            'Wwise parameter string',
        ),
    ],
}
