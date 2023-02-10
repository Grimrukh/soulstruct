from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


AI_SOUND_PARAM_ST = {
    "param_type": "AI_SOUND_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "radius",
            "Radius",
            True,
            float,
            'AI sound radius',
        ),
        ParamFieldInfo(
            "lifeFrame",
            "Duration",
            True,
            float,
            'Time for AI sound to remain',
        ),
        ParamFieldInfo(
            "bSpEffectEnable",
            "Is Affected by Sound Radius Magnification",
            True,
            int,
            'Whether it is affected by the special effect "Sound Radius Magnification"',
        ),
        ParamFieldInfo(
            "type",
            "Rate Type",
            True,
            int,
            'AI sound type',
        ),
        ParamFieldInfo(
            "opposeTarget:1",
            "Target: Hostile",
            True,
            int,
            'Target: �� Hostile',
        ),
        ParamFieldInfo(
            "friendlyTarget:1",
            "Target: Friendly",
            True,
            int,
            'Target: �� Allies',
        ),
        ParamFieldInfo(
            "selfTarget:1",
            "Target: Self",
            True,
            int,
            'Target: myself',
        ),
        ParamFieldInfo(
            "disableOnTargetPCompany:1",
            "Disable on Targeting Player",
            True,
            int,
            "You can't listen while targeting your PC",
        ),
        ParamFieldInfo(
            "rank",
            "Rank",
            True,
            int,
            'Character behavior (former: sound type)',
        ),
        ParamFieldInfo(
            "forgetTime",
            "Forget Time",
            True,
            float,
            'Time to forget the sound target (overwrite) [sec]',
        ),
        ParamFieldInfo(
            "priority",
            "Priority",
            True,
            int,
            'AI sound priority',
        ),
        ParamFieldInfo(
            "soundBehaviorId",
            "Sound Behavior ID",
            True,
            int,
            'Behavior ID',
        ),
        ParamFieldInfo(
            "aiSoundLevel",
            "AI Sound Level",
            True,
            int,
            'How hard it is to hear',
        ),
        ParamFieldInfo(
            "replaningState",
            "Replanning State",
            True,
            int,
            'AI state setting to run replanning when listening to AI sound',
        ),
        ParamFieldInfo(
            "pad1[6]",
            "pad",
            False,
            pad_field(6),
            'pad',
        ),
    ],
}
