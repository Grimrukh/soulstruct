from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


WEATHER_LOT_TEX_PARAM_ST = {
    "param_type": "WEATHER_LOT_TEX_PARAM_ST",
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
            "srcR",
            "Pre-conversion - Map Color: R",
            True,
            int,
            'Color information (R) of the map image before conversion. Pixels with matching RGB values are associated with this parameter',
        ),
        ParamFieldInfo(
            "srcG",
            "Pre-conversion - Map Color: G",
            True,
            int,
            'Color information (G) of the map image before conversion. Pixels with matching RGB values are associated with this parameter',
        ),
        ParamFieldInfo(
            "srcB",
            "Pre-conversion - Map Color: B",
            True,
            int,
            'Color information (B) of the map image before conversion. Pixels with matching RGB values are associated with this parameter',
        ),
        ParamFieldInfo(
            "pad1[1]",
            "pad",
            False,
            pad_field(1),
            'pad. For the time being, leave it open for "image color information (A)"',
        ),
        ParamFieldInfo(
            "weatherLogId",
            "Weather Lottery ID",
            True,
            int,
            'Weather lottery ID (-1: No setting (default value))',
        ),
        ParamFieldInfo(
            "pad2[4]",
            "Pad 2",
            False,
            pad_field(4),
            '',
        ),
    ],
}
