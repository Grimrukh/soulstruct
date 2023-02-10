from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MAP_GRID_CREATE_HEIGHT_LIMIT_INFO_PARAM_ST = {
    "param_type": "MAP_GRID_CREATE_HEIGHT_LIMIT_INFO_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "GridEnableCreateHeightMin",
            "Min Height - Grid Creation (LOD2)",
            True,
            float,
            'Minimum height that can be built in the grid [m]. (LOD 2 units)',
        ),
        ParamFieldInfo(
            "GridEnableCreateHeightMax",
            "Max Height - Grid Creation (LOD2)",
            True,
            float,
            'Maximum height that can be constructed in the grid [m]. (LOD 2 units)',
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
