from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MAP_GD_REGION_ID_PARAM_ST = {
    "param_type": "MAP_GD_REGION_ID_PARAM_ST",
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
            "mapRegionId",
            "Map Region ID",
            True,
            int,
            'Map for GD use Local identification ID [00-99: Open, 1000-9999: Legacy]',
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
