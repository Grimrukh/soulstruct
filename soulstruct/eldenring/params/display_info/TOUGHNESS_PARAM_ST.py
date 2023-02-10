from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


TOUGHNESS_PARAM_ST = {
    "param_type": "TOUGHNESS_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "correctionRate",
            "Toughness Correction",
            True,
            float,
            'It is a correction magnification applied to the "toughness correction magnification" of the weapon when calculating the toughness.',
        ),
        ParamFieldInfo(
            "minToughness",
            "Minimum Toughness",
            True,
            int,
            'The lower limit of current toughness applied at the beginning of the toughness period. If the toughness falls below this value at the start of toughness, it will recover to this value.',
        ),
        ParamFieldInfo(
            "isNonEffectiveCorrectionForMin",
            "Minimum Toughness not affected by Toughness Multiplier",
            True,
            int,
            'The toughness correction factor will no longer be applied to the minimum toughness.',
        ),
        ParamFieldInfo(
            "pad2[1]",
            "pad",
            False,
            pad_field(1),
            'pad',
        ),
        ParamFieldInfo(
            "spEffectId",
            "Damage Level Replacement - SpEffect ID",
            True,
            int,
            'Replacement special effect Id that takes place during the toughness period. If -1, the normal replacement rule applies. Only used by player characters',
        ),
        ParamFieldInfo(
            "proCorrectionRate",
            "Armor - Toughness Correction",
            True,
            float,
            'This is the correction factor applied to the "toughness correction factor" of the armor when determining the toughness.',
        ),
        ParamFieldInfo(
            "pad1[16]",
            "pad",
            False,
            pad_field(16),
            'pad',
        ),
    ],
}
