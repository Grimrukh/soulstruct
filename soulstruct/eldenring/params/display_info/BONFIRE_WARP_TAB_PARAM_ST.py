from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


BONFIRE_WARP_TAB_PARAM_ST = {
    "param_type": "BONFIRE_WARP_TAB_PARAM_ST",
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
            "textId",
            "Text ID",
            True,
            int,
            'Tab Display Name Text ID [MenuText]',
        ),
        ParamFieldInfo(
            "sortId",
            "Sort ID",
            True,
            int,
            'Tab display order sort ID. Line up from the left with aim',
        ),
        ParamFieldInfo(
            "iconId",
            "Icon ID",
            True,
            int,
            'Tab icon ID. Menu resource compliance',
        ),
        ParamFieldInfo(
            "pad[2]",
            "pad",
            False,
            pad_field(2),
            '',
        ),
    ],
}
