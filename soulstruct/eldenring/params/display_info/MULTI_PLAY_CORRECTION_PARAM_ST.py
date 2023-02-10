from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MULTI_PLAY_CORRECTION_PARAM_ST = {
    "param_type": "MULTI_PLAY_CORRECTION_PARAM_ST",
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
            "client1SpEffectId",
            "Friendly Client [1] - SpEffect ID",
            True,
            int,
            '1 cooperating client Special effect ID',
        ),
        ParamFieldInfo(
            "client2SpEffectId",
            "Friendly Client [2] - SpEffect ID",
            True,
            int,
            '2 cooperating clients Special effect ID',
        ),
        ParamFieldInfo(
            "client3SpEffectId",
            "Friendly Client [3] - SpEffect ID",
            True,
            int,
            '3 cooperating clients Special effect ID',
        ),
        ParamFieldInfo(
            "bOverrideSpEffect",
            "Override SpEffect when Client Count Changes",
            True,
            int,
            'Whether to overwrite when the number of cooperating people fluctuates',
        ),
        ParamFieldInfo(
            "pad3[15]",
            "pad",
            False,
            pad_field(15),
            'pad',
        ),
    ],
}
