from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


GPARAM_GRID_REGION_INFO_PARAM_ST = {
    "param_type": "GPARAM_GRID_REGION_INFO_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "GparamGridRegionId",
            "GPARAM Grid Region ID",
            True,
            int,
            'Open local ID for MapGparam. Used for the XX part of m60_00_00XX.gparamxml',
        ),
        ParamFieldInfo(
            "Reserve[28]",
            "Reserve",
            False,
            pad_field(28),
            'Reserve',
        ),
    ],
}
