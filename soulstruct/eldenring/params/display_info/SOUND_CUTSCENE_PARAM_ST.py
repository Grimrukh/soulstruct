from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SOUND_CUTSCENE_PARAM_ST = {
    "param_type": "SOUND_CUTSCENE_PARAM_ST",
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
            "ReverbType",
            "Reverb Type",
            True,
            int,
            'Specifies the reverb type to apply during the cutscene',
        ),
        ParamFieldInfo(
            "pad0[3]",
            "pad0",
            False,
            pad_field(3),
            '',
        ),
        ParamFieldInfo(
            "BgmBehaviorTypeOnStart",
            "BGM Behavior Type On Start",
            True,
            int,
            'Specifies normal BGM behavior at the start of cutscenes',
        ),
        ParamFieldInfo(
            "OneShotBgmBehaviorOnStart",
            "One-shot BGM Behavior Type On Start",
            True,
            int,
            'Specifies the one-shot BGM behavior at the start of the cutscene',
        ),
        ParamFieldInfo(
            "PostPlaySeId",
            "Post Play SE ID",
            True,
            int,
            'SEID (category: p) specification to post at the end of the cutscene (-1: do not post)',
        ),
        ParamFieldInfo(
            "PostPlaySeIdForSkip",
            "Post Play SE ID for Skip",
            True,
            int,
            'SEID_ for skipping to post at the end of the cutscene (category: p) specified (-1: not posted)',
        ),
        ParamFieldInfo(
            "EnterMapMuteStopTimeOnDrawCutscene",
            "Enter Map Mute Stop Time on Draw Cutscene",
            True,
            float,
            'Cutscene drawing time to unmute immediately after entering [seconds] (less than 0: not canceled in drawing time)',
        ),
        ParamFieldInfo(
            "reserved[8]",
            "Reserve",
            False,
            pad_field(8),
            'Reserve',
        ),
    ],
}
