from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


WORLD_MAP_PLACE_NAME_PARAM_ST = {
    "param_type": "WORLD_MAP_PLACE_NAME_PARAM_ST",
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
            "worldMapPieceId",
            "World Map Piece ID",
            True,
            int,
            'Map fragment parameter ID. Display text if you have this map fragment',
        ),
        ParamFieldInfo(
            "textId",
            "Place Name - Text ID",
            True,
            int,
            'The text ID to display. PlaceName.xlsm',
        ),
        ParamFieldInfo(
            "pad1[4]",
            "Padding",
            False,
            pad_field(4),
            '',
        ),
        ParamFieldInfo(
            "areaNo",
            "Map Area",
            True,
            int,
            'AA part of mAA_BB_CC_DD',
        ),
        ParamFieldInfo(
            "gridXNo",
            "Map Block",
            True,
            int,
            'BB part of mAA_BB_CC_DD',
        ),
        ParamFieldInfo(
            "gridZNo",
            "Map Region",
            True,
            int,
            'CC part of mAA_BB_CC_DD',
        ),
        ParamFieldInfo(
            "pad2[1]",
            "Padding",
            False,
            pad_field(1),
            'Padding',
        ),
        ParamFieldInfo(
            "posX",
            "Map Coodinate: X",
            True,
            float,
            'X coordinate',
        ),
        ParamFieldInfo(
            "posY",
            "Map Coodinate: Y",
            True,
            float,
            'Y coordinate (not used)',
        ),
        ParamFieldInfo(
            "posZ",
            "Map Coodinate: Z",
            True,
            float,
            'Z coordinate',
        ),
    ],
}
