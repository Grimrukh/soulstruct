from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


GPARAM_REF_SETTINGS_PARAM_ST = {
    "param_type": "GPARAM_REF_SETTINGS_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "disableParam_NT:1",
            "Disable Param - Network Test",
            True,
            int,
            'Parameters marked with �� are excluded in the NT version package.',
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
            "RefTargetMapId",
            "Reference Target Map ID",
            True,
            int,
            'Specify the referenced map number. Legacy: m10_10_00_00-> 10010000, Open: m60_ ?? _ ?? _ ??-> m60000000',
        ),
        ParamFieldInfo(
            "Reserve[24]",
            "Reserve",
            False,
            pad_field(24),
            'Reserve',
        ),
    ],
}
