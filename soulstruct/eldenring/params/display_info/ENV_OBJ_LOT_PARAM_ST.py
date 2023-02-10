from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


ENV_OBJ_LOT_PARAM_ST = {
    "param_type": "ENV_OBJ_LOT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "AssetId_0",
            "Asset ID [0]",
            True,
            int,
            'AssetId_0 (-1: Ignore)',
        ),
        ParamFieldInfo(
            "AssetId_1",
            "Asset ID [1]",
            True,
            int,
            'AssetId_1 (-1: Ignore)',
        ),
        ParamFieldInfo(
            "AssetId_2",
            "Asset ID [2]",
            True,
            int,
            'AssetId_2 (-1: Ignore)',
        ),
        ParamFieldInfo(
            "AssetId_3",
            "Asset ID [3]",
            True,
            int,
            'AssetId_3 (-1: Ignore)',
        ),
        ParamFieldInfo(
            "AssetId_4",
            "Asset ID [4]",
            True,
            int,
            'AssetId_4 (-1: Ignore)',
        ),
        ParamFieldInfo(
            "AssetId_5",
            "Asset ID [5]",
            True,
            int,
            'AssetId_5 (-1: Ignore)',
        ),
        ParamFieldInfo(
            "AssetId_6",
            "Asset ID [6]",
            True,
            int,
            'AssetId_6 (-1: Ignore)',
        ),
        ParamFieldInfo(
            "AssetId_7",
            "Asset ID [7]",
            True,
            int,
            'AssetId_7 (-1: Ignore)',
        ),
        ParamFieldInfo(
            "CreateWeight_0",
            "Create Weight [0]",
            True,
            int,
            'Appearance ratio point (weight) _0: 0 is ignored',
        ),
        ParamFieldInfo(
            "CreateWeight_1",
            "Create Weight [1]",
            True,
            int,
            'Appearance ratio point (weight) _1',
        ),
        ParamFieldInfo(
            "CreateWeight_2",
            "Create Weight [2]",
            True,
            int,
            'Appearance ratio point (weight) _2',
        ),
        ParamFieldInfo(
            "CreateWeight_3",
            "Create Weight [3]",
            True,
            int,
            'Appearance ratio point (weight) _3',
        ),
        ParamFieldInfo(
            "CreateWeight_4",
            "Create Weight [4]",
            True,
            int,
            'Appearance ratio point (weight) _4',
        ),
        ParamFieldInfo(
            "CreateWeight_5",
            "Create Weight [5]",
            True,
            int,
            'Appearance ratio point (weight) _5',
        ),
        ParamFieldInfo(
            "CreateWeight_6",
            "Create Weight [6]",
            True,
            int,
            'Appearance ratio point (weight) _6',
        ),
        ParamFieldInfo(
            "CreateWeight_7",
            "Create Weight [7]",
            True,
            int,
            'Appearance ratio point (weight) _7',
        ),
        ParamFieldInfo(
            "Reserve_0[24]",
            "Reserve",
            False,
            pad_field(24),
            'Reserve',
        ),
    ],
}
