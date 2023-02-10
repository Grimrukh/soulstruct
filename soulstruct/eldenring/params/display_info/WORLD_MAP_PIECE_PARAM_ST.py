from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


WORLD_MAP_PIECE_PARAM_ST = {
    "param_type": "WORLD_MAP_PIECE_PARAM_ST",
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
            "openEventFlagId",
            "Open - Event Flag ID",
            True,
            int,
            'Event flag ID of open condition',
        ),
        ParamFieldInfo(
            "openTravelAreaLeft",
            "Open - Traversal Area - X Min",
            True,
            float,
            'Coordinates of the traversal area that expands when opened (Xmin)',
        ),
        ParamFieldInfo(
            "openTravelAreaRight",
            "Open - Traversal Area - X Max",
            True,
            float,
            'Coordinates of the traversal area that expands when opened (Xmax)',
        ),
        ParamFieldInfo(
            "openTravelAreaTop",
            "Open - Traversal Area - Y Min",
            True,
            float,
            'Coordinates of the traversal area that expands when opened (Ymin)',
        ),
        ParamFieldInfo(
            "openTravelAreaBottom",
            "Open - Traversal Area - Y Max",
            True,
            float,
            'Coordinates of the traversal area that expands when opened (Ymax)',
        ),
        ParamFieldInfo(
            "acquisitionEventFlagId",
            "Acquisition - Event Flag ID",
            True,
            int,
            'Event flag ID of the acquisition production start condition. Assuming that only one of the map fragments is On',
        ),
        ParamFieldInfo(
            "acquisitionEventScale",
            "Acquisition - Display Scale",
            True,
            float,
            'Display magnification at the time of acquisition production',
        ),
        ParamFieldInfo(
            "acquisitionEventCenterX",
            "Acquisition - Center X Coordinate",
            True,
            float,
            'Center coordinates (X) at the time of acquisition production',
        ),
        ParamFieldInfo(
            "acquisitionEventCenterY",
            "Acquisition - Center Y Coordinate",
            True,
            float,
            'For the central seat at the time of acquisition production (Y)',
        ),
        ParamFieldInfo(
            "acquisitionEventResScale",
            "Acquisition - Display Resource Scale",
            True,
            float,
            'Display magnification of blindfold resources for acquisition production',
        ),
        ParamFieldInfo(
            "acquisitionEventResOffsetX",
            "Acquisition - Resource Offset X",
            True,
            float,
            'Display position offset (X) of blindfold resource for acquisition production',
        ),
        ParamFieldInfo(
            "acquisitionEventResOffsetY",
            "Acquisition - Resource Offset Y",
            True,
            float,
            'Offset of display position of blindfold resource for acquisition production (Y)',
        ),
        ParamFieldInfo(
            "pad[12]",
            "pad",
            False,
            pad_field(12),
            '',
        ),
    ],
}
