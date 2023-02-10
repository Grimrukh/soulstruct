from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SIGN_PUDDLE_PARAM_ST = {
    "param_type": "SIGN_PUDDLE_PARAM_ST",
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
            "matchAreaId",
            "Match Area ID",
            True,
            int,
            'ID of the simple match area to which it belongs',
        ),
        ParamFieldInfo(
            "pad1[24]",
            "pad1",
            False,
            pad_field(24),
            '',
        ),
    ],
}
