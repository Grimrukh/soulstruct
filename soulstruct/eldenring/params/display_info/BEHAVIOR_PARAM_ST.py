from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


BEHAVIOR_PARAM_ST = {
    "param_type": "BEHAVIOR_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "variationId",
            "Behavior Variation ID",
            True,
            int,
            'Used when calculating the ID for attack parameters. It is not used directly on the actual machine.',
        ),
        ParamFieldInfo(
            "behaviorJudgeId",
            "Behavior Judge ID",
            True,
            int,
            'Used when calculating the ID for attack parameters. This ID matches the action judgment ID entered in TimeActEditor. It is not used directly on the actual machine.',
        ),
        ParamFieldInfo(
            "ezStateBehaviorType_old",
            "State Behavior Type",
            True,
            int,
            'For ID calculation rules',
        ),
        ParamFieldInfo(
            "refType",
            "Reference Type",
            True,
            int,
            'Specify the reference ID so that it is correct.',
        ),
        ParamFieldInfo(
            "pad2[2]",
            "pad",
            False,
            pad_field(2),
            '',
        ),
        ParamFieldInfo(
            "refId",
            "Reference ID",
            True,
            int,
            'It can be used properly according to the attack power, missile, ID of special effect parameter, and refType.',
        ),
        ParamFieldInfo(
            "consumeSA",
            "Poise Cost",
            True,
            float,
            'Set the amount of SA consumed during action.',
        ),
        ParamFieldInfo(
            "stamina",
            "Stamina Cost",
            True,
            int,
            'Set the amount of stamina consumed during action.',
        ),
        ParamFieldInfo(
            "consumeDurability",
            "Durability Cost",
            True,
            int,
            'Set the durability of weapons consumed during action.',
        ),
        ParamFieldInfo(
            "category",
            "Category",
            True,
            int,
            'Since there are effects (enchantment weapons, etc.) whose parameters fluctuate depending on skills, magic, items, etc., set each action so that the determined effect can correspond to the effect such as "power up only weapon attack". Set "None" for items that do not need to be set, such as varistor.',
        ),
        ParamFieldInfo(
            "heroPoint",
            "Humanity Cost",
            True,
            int,
            'Set the amount of humanity consumed during action',
        ),
        ParamFieldInfo(
            "pad1[2]",
            "pad",
            False,
            pad_field(2),
            '',
        ),
    ],
}
