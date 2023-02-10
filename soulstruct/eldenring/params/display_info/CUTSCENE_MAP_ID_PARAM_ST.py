from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CUTSCENE_MAP_ID_PARAM_ST = {
    "param_type": "CUTSCENE_MAP_ID_PARAM_ST",
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
            "disableParam_Debug:1",
            "Disable Param - Debug",
            True,
            int,
            'Parameters marked with a circle are excluded from all packages (because they are for debugging).',
        ),
        ParamFieldInfo(
            "disableParamReserve1:6",
            "Reserve for package output 1",
            False,
            bit_pad_field(6),
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
            "PlayMapId",
            "Play Map ID",
            True,
            int,
            'Please enter the map number to be played back as an 8-digit number. This is the map number used as the reference in the cutscene. If you do not specify the correct map number, the playback position will shift.',
        ),
        ParamFieldInfo(
            "RequireMapId0",
            "Require Map ID 0",
            True,
            int,
            "Please enter the map number required for display as an 8-digit number. This parameter is used by the guest as a list to determine if the cutscene can be played. If you don't need it, you can leave it as 0 or blank.",
        ),
        ParamFieldInfo(
            "RequireMapId1",
            "Require Map ID 1",
            True,
            int,
            "Please enter the map number required for display as an 8-digit number. This parameter is used by the guest as a list to determine if the cutscene can be played. If you don't need it, you can leave it as 0 or blank.",
        ),
        ParamFieldInfo(
            "RequireMapId2",
            "Require Map ID 2",
            True,
            int,
            "Please enter the map number required for display as an 8-digit number. This parameter is used by the guest as a list to determine if the cutscene can be played. If you don't need it, you can leave it as 0 or blank.",
        ),
        ParamFieldInfo(
            "RefCamPosHitPartsID",
            "Hit Part ID for Reference Camera",
            True,
            int,
            'Hit part ID for calculating camera position during loading',
        ),
        ParamFieldInfo(
            "reserved_2[12]",
            "Reserve",
            False,
            pad_field(12),
            '',
        ),
        ParamFieldInfo(
            "ClientDisableViewTimeForProgress",
            "Client Load View - Progress Bar Time",
            True,
            int,
            'The number of seconds used to display the progress of the loading screen progress bar that is displayed when the guest side cannot play in the multi. [GR] SEQ22843 [Cutscene] Players who have not read the map number required for display during cutscene playback will see the screen go dark.',
        ),
        ParamFieldInfo(
            "reserved[2]",
            "reserved",
            False,
            pad_field(2),
            'reserved',
        ),
        ParamFieldInfo(
            "HitParts_0",
            "Hit Parts [0]",
            True,
            int,
            'Hit parts waiting to be read 0',
        ),
        ParamFieldInfo(
            "HitParts_1",
            "Hit Parts [1]",
            True,
            int,
            'Hit parts waiting to be read 1',
        ),
    ],
}
