from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CEREMONY_PARAM_ST = {
    "param_type": "CEREMONY_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "eventLayerId",
            "Event Layer ID",
            True,
            int,
            'Event maker layer ID',
        ),
        ParamFieldInfo(
            "mapStudioLayerId",
            "Map Studio Layer ID",
            True,
            int,
            'Map Studio Layer ID',
        ),
        ParamFieldInfo(
            "multiPlayAreaOffset",
            "Play Region ID Offset",
            True,
            int,
            'Multiplayer area ID offset. For example, if you enter "100", the multiplayer area ID will be offset by "100".',
        ),
        ParamFieldInfo(
            "overrideMapPlaceNameId",
            "Override Map Place Name ID",
            True,
            int,
            'Override the map name ID_place name display with the specified ID. -1: No overwrite, -2 or less, 0 or more: Overwrite the ID.',
        ),
        ParamFieldInfo(
            "overrideSaveMapNameId",
            "Override Save Map Name ID",
            True,
            int,
            'Map name ID_Overwrites the save data display with the specified ID. -1: No overwrite, -2 or less, 0 or more: Overwrite the ID.',
        ),
        ParamFieldInfo(
            "pad2[16]",
            "pad2",
            False,
            pad_field(16),
            '',
        ),
    ],
}
