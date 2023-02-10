from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CUTSCENE_TIMEZONE_CONVERT_PARAM_ST = {
    "param_type": "CUTSCENE_TIMEZONE_CONVERT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "SrcTimezoneStart",
            "Source - Timezone Start",
            True,
            float,
            'Start time of the time zone to be converted to cutscene time [hour]',
        ),
        ParamFieldInfo(
            "DstCutscenTime",
            "Destination - Cutscene Time",
            True,
            float,
            'Enter the time used during cutscene playback in hours [hour]',
        ),
    ],
}
