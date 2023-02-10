from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


BASECHR_SELECT_MENU_PARAM_ST = {
    "param_type": "BASECHR_SELECT_MENU_PARAM_ST",
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
            "chrInitParam",
            "Chr Init Param ID - Class",
            True,
            int,
            'Specify the initial parameter ID for each architype for which face para is set.',
        ),
        ParamFieldInfo(
            "originChrInitParam",
            "Chr Init Param ID - Origin",
            True,
            int,
            'Specify the initial parameter ID for each feature archetype',
        ),
        ParamFieldInfo(
            "imageId",
            "Image ID",
            True,
            int,
            'Images lined up on the base character selection screen. Specify the number of frames of resources embedded in Fla',
        ),
        ParamFieldInfo(
            "textId",
            "Text ID",
            True,
            int,
            'Occupation name menu text ID',
        ),
        ParamFieldInfo(
            "reserve[12]",
            "Reserve",
            False,
            pad_field(12),
            '',
        ),
    ],
}
