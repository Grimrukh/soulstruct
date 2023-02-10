from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SOUND_AUTO_ENV_SOUND_GROUP_PARAM_ST = {
    "param_type": "SOUND_AUTO_ENV_SOUND_GROUP_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "SoundNo",
            "Sound Number",
            True,
            int,
            'Sound No to play (sound type is fixed to a)',
        ),
        ParamFieldInfo(
            "ExpandRange",
            "Expand Range",
            True,
            float,
            'Extended distance of playback judgment area',
        ),
        ParamFieldInfo(
            "FollowSpeed",
            "Follow Speed",
            True,
            float,
            'Follow-up speed (fixed speed) to the target position of the actual sound source',
        ),
        ParamFieldInfo(
            "FollowRate",
            "Follow Rate",
            True,
            float,
            'Follow-up speed (difference ratio) to the target position of the actual sound source',
        ),
    ],
}
