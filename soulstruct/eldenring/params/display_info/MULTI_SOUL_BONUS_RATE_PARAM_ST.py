from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MULTI_SOUL_BONUS_RATE_PARAM_ST = {
    "param_type": "MULTI_SOUL_BONUS_RATE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "host",
            "Rune Reward Multiplier - Host",
            True,
            float,
            'Host reward soul multiplier',
        ),
        ParamFieldInfo(
            "WhiteGhost_None",
            "Rune Reward Multiplier - White Phantom - None",
            True,
            float,
            'Cooperation sign white spirit reward soul multiplier',
        ),
        ParamFieldInfo(
            "WhiteGhost_Umbasa",
            "Rune Reward Multiplier - White Phantom - Gold",
            True,
            float,
            'Cooperative sign gold spirit reward soul multiplier',
        ),
        ParamFieldInfo(
            "WhiteGhost_Berserker",
            "Rune Reward Multiplier - White Phantom - Berserker",
            True,
            float,
            'Cooperation sign white Berserker reward soul multiplier',
        ),
        ParamFieldInfo(
            "BlackGhost_None_Sign",
            "Rune Reward Multiplier - Black Phantom - None",
            True,
            float,
            'Hostile sign red spirit reward soul multiplier',
        ),
        ParamFieldInfo(
            "BlackGhost_Umbasa_Sign",
            "Rune Reward Multiplier - Black Phantom - Gold",
            True,
            float,
            'Hostile sign red gold spirit reward soul multiplier',
        ),
        ParamFieldInfo(
            "BlackGhost_Berserker_Sign",
            "Rune Reward Multiplier - Black Phantom - Berserker",
            True,
            float,
            'Hostile sign red berserker reward soul multiplier',
        ),
        ParamFieldInfo(
            "BlackGhost_None_Invade",
            "Rune Reward Multiplier - Black Phantom - None - Invade",
            True,
            float,
            'Invasion reward Soul multiplier',
        ),
        ParamFieldInfo(
            "BlackGhost_Umbasa_Invade",
            "Rune Reward Multiplier - Black Phantom - Gold - Invade",
            True,
            float,
            "Invasion Orb's Red Gold Spirit Reward Soul Multiplier",
        ),
        ParamFieldInfo(
            "BlackGhost_Berserker_Invade",
            "Rune Reward Multiplier - Black Phantom - Berserker - Invade",
            True,
            float,
            'Invasion Orb Red Berserker Reward Soul Multiplier',
        ),
        ParamFieldInfo(
            "RedHunter1",
            "Rune Reward Multiplier - Red Hunter [1]",
            True,
            float,
            'Relief guest reward soul multiplier',
        ),
        ParamFieldInfo(
            "RedHunter2",
            "Rune Reward Multiplier - Red Hunter [2]",
            True,
            float,
            'Red Scare Spirit 2 Reward Soul Multiplier',
        ),
        ParamFieldInfo(
            "GuardianOfForest",
            "Rune Reward Multiplier - Forest Guardian",
            True,
            float,
            'Map Guardian Spirit (Forest) Reward Soul Magnification',
        ),
        ParamFieldInfo(
            "GuardianOfAnor",
            "Rune Reward Multiplier - Darkmoon Blade",
            True,
            float,
            'Map Guardian Spirit (Anor) Reward Soul Multiplier',
        ),
        ParamFieldInfo(
            "BattleRoyal",
            "Rune Reward Multiplier - Arena",
            True,
            float,
            'Arena reward soul multiplier',
        ),
        ParamFieldInfo(
            "YellowMonk",
            "Rune Reward Multiplier - Yellow Monk",
            True,
            float,
            "Yellow robe's old man's reward soul multiplier",
        ),
        ParamFieldInfo(
            "pad1[64]",
            "pad",
            False,
            pad_field(64),
            '',
        ),
    ],
}
