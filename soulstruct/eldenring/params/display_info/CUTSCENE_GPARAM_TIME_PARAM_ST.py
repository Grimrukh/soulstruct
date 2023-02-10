from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CUTSCENE_GPARAM_TIME_PARAM_ST = {
    "param_type": "CUTSCENE_GPARAM_TIME_PARAM_ST",
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
            "DstTimezone_Morning",
            "Destination Timezone: Morning",
            True,
            int,
            'Morning (Refer to the cutscene time conversion setting sheet for the conversion time)',
        ),
        ParamFieldInfo(
            "DstTimezone_Noon",
            "Destination Timezone: Noon",
            True,
            int,
            'Day A (Refer to the cutscene time conversion setting sheet for the conversion time)',
        ),
        ParamFieldInfo(
            "DstTimezone_AfterNoon",
            "Destination Timezone: Afternoon",
            True,
            int,
            'Noon-B (Refer to the cutscene time conversion setting sheet for the conversion time)',
        ),
        ParamFieldInfo(
            "DstTimezone_Evening",
            "Destination Timezone: Evening",
            True,
            int,
            'Evening (Refer to the cutscene time conversion setting sheet for the conversion time)',
        ),
        ParamFieldInfo(
            "DstTimezone_Night",
            "Destination Timezone: Night",
            True,
            int,
            'Night (Refer to the cutscene time conversion setting sheet for the conversion time)',
        ),
        ParamFieldInfo(
            "DstTimezone_DeepNightA",
            "Destination Timezone: Deep Night A",
            True,
            int,
            'Midnight A (Refer to the cutscene time conversion setting sheet for the conversion time)',
        ),
        ParamFieldInfo(
            "DstTimezone_DeepNightB",
            "Destination Timezone: Deep Night B",
            True,
            int,
            'Midnight B (Refer to the cutscene time conversion setting sheet for the conversion time)',
        ),
        ParamFieldInfo(
            "reserved[1]",
            "reserved",
            False,
            pad_field(1),
            'reserved',
        ),
        ParamFieldInfo(
            "PostPlayIngameTime",
            "Post Cutscene In-game Time",
            True,
            float,
            'Specify in-game time at the end of playback [hour] [-1.0 to 24.0] (-1 (less than 0): do nothing)',
        ),
    ],
}
