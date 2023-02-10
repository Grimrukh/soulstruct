from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


ENEMY_COMMON_PARAM_ST = {
    "param_type": "ENEMY_COMMON_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "reserved0[8]",
            "reserve",
            False,
            pad_field(8),
            '(dummy8)',
        ),
        ParamFieldInfo(
            "soundTargetTryApproachTime",
            "Sound - Target Try Approach Time",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "searchTargetTryApproachTime",
            "Search - Target Try Approach Time",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "memoryTargetTryApproachTime",
            "Memory - Target Try Approach Time",
            True,
            int,
            '',
        ),
        ParamFieldInfo(
            "reserved5[40]",
            "reserve",
            False,
            pad_field(40),
            '(dummy8)',
        ),
        ParamFieldInfo(
            "activateChrByTime_PhantomId",
            "Activate Chr by Time - Phantom ID",
            True,
            int,
            'Phantom shader ID used for directing the appearance and disappearance of enemies placed in a specific time zone',
        ),
        ParamFieldInfo(
            "findUnfavorableFailedPointDist",
            "Find Unfavourable Failed Point Distance",
            True,
            float,
            'Distance to generate an interrupt, which turns out that the enemy is likely to be cut off when going to the end of the path',
        ),
        ParamFieldInfo(
            "findUnfavorableFailedPointHeight",
            "Find Unfavourable Failed Point Height",
            True,
            float,
            'The height that causes an interrupt, which turns out that the enemy is likely to be cut off when going to the end of the path',
        ),
        ParamFieldInfo(
            "reserved18[184]",
            "reserve",
            False,
            pad_field(184),
            '(dummy8)',
        ),
    ],
}
