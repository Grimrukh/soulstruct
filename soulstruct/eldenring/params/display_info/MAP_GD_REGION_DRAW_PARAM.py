from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MAP_GD_REGION_DRAW_PARAM = {
    "param_type": "MAP_GD_REGION_DRAW_PARAM",
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
            "overrideIVLocalLightScale",
            "Override Irradiance Volume Local Light Scale",
            True,
            float,
            'Local light scale value at the time of IV shooting (0 or less: no overwrite) [GR] SEQ13338 [Irradiance volume] I want to change the indirect scale of the SFX light source uniformly.',
        ),
    ],
}
