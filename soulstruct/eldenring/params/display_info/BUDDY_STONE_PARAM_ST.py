from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


BUDDY_STONE_PARAM_ST = {
    "param_type": "BUDDY_STONE_PARAM_ST",
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
            "talkChrEntityId",
            "Talk Character Entity ID",
            True,
            int,
            'Used as a foreign key when referencing from a conversation.',
        ),
        ParamFieldInfo(
            "eliminateTargetEntityId",
            "Defeat Target List Entity ID",
            True,
            int,
            'Entity ID of the character / group to be defeated by the buddy when summoned from this stele',
        ),
        ParamFieldInfo(
            "summonedEventFlagId",
            "Summoned Event Flag ID",
            True,
            int,
            'Flag ID that stands when summoned from a stone monument. When this flag is set, the stone monument cannot be summoned.',
        ),
        ParamFieldInfo(
            "isSpecial:1",
            "Is Special Monument",
            True,
            int,
            'Is the stone monument an SP stone monument or a general-purpose stone monument? A bool that distinguishes.',
        ),
        ParamFieldInfo(
            "pad1:7",
            "Padding",
            False,
            bit_pad_field(7),
            '',
        ),
        ParamFieldInfo(
            "pad2[3]",
            "Padding",
            False,
            pad_field(3),
            '',
        ),
        ParamFieldInfo(
            "buddyId",
            "Buddy ID",
            True,
            int,
            'ID of the buddy parameter. If "Special" is ��, this buddy ID will be summoned.',
        ),
        ParamFieldInfo(
            "dopingSpEffectId",
            "Applied SpEffect ID",
            True,
            int,
            'Special effect ID applied to the buddy when summoning the buddy.',
        ),
        ParamFieldInfo(
            "activateRange",
            "Activation Distance",
            True,
            int,
            'If there is at least one character to be defeated in this range, you can summon a buddy at that stone monument.',
        ),
        ParamFieldInfo(
            "overwriteReturnRange",
            "Overwrite Return Range",
            True,
            int,
            "Buddy's homecoming distance can be overridden",
        ),
        ParamFieldInfo(
            "overwriteActivateRegionEntityId",
            "Overwrite Activation Region Entity ID",
            True,
            int,
            'The range where the buddy can be summoned can be overwritten in the area of the specified entity ID.',
        ),
        ParamFieldInfo(
            "warnRegionEntityId",
            "Warn Region Entity ID",
            True,
            int,
            'Warning area entity ID',
        ),
        ParamFieldInfo(
            "pad3[24]",
            "Padding",
            False,
            pad_field(24),
            '',
        ),
    ],
}
