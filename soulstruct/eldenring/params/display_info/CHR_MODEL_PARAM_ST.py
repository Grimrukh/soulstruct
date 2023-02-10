from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CHR_MODEL_PARAM_ST = {
    "param_type": "CHR_MODEL_PARAM_ST",
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
            "modelMemoryType",
            "Model Memory Type",
            True,
            int,
            'Model used memory type',
        ),
        ParamFieldInfo(
            "texMemoryType",
            "Texture Memory Type",
            True,
            int,
            'Texture usage memory type',
        ),
        ParamFieldInfo(
            "cameraDitherFadeId",
            "Camera Dither Fade ID",
            True,
            int,
            'Camera fade parameter ID (-1: refer to material, 0: do not disappear, 1 ~: parameter ID)',
        ),
        ParamFieldInfo(
            "reportAnimMemSizeMb",
            "Send Report - Animation Memory Size MB",
            True,
            float,
            'If this value is exceeded, a report will be sent by the reporting system.',
        ),
    ],
}
