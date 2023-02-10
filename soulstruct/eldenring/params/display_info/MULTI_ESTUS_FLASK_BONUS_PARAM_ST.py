from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MULTI_ESTUS_FLASK_BONUS_PARAM_ST = {
    "param_type": "MULTI_ESTUS_FLASK_BONUS_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "host",
            "Flask Recovery - Host",
            True,
            int,
            'Number of host est recovery',
        ),
        ParamFieldInfo(
            "WhiteGhost_None",
            "Flask Recovery - White Phantom - None",
            True,
            int,
            'Number of white spirits recovering from the cooperation sign',
        ),
        ParamFieldInfo(
            "WhiteGhost_Umbasa",
            "Flask Recovery - White Phantom - Gold",
            True,
            int,
            'Number of est recovery of gold spirits of cooperation sign',
        ),
        ParamFieldInfo(
            "WhiteGhost_Berserker",
            "Flask Recovery - White Phantom - Berserker",
            True,
            int,
            "Number of recovery of white Berserker's est of cooperation sign",
        ),
        ParamFieldInfo(
            "BlackGhost_None_Sign",
            "Flask Recovery - Black Phantom - None",
            True,
            int,
            'Number of est recovery of red spirits of hostile sign',
        ),
        ParamFieldInfo(
            "BlackGhost_Umbasa_Sign",
            "Flask Recovery - Black Phantom - Gold",
            True,
            int,
            'Number of est recovery of red gold spirit of hostile sign',
        ),
        ParamFieldInfo(
            "BlackGhost_Berserker_Sign",
            "Flask Recovery - Black Phantom - Berserker",
            True,
            int,
            'Number of est recovery of red Berserker of hostile sign',
        ),
        ParamFieldInfo(
            "BlackGhost_None_Invade",
            "Flask Recovery - Black Phantom - None - Invasion",
            True,
            int,
            'Number of intrusion est recovery',
        ),
        ParamFieldInfo(
            "BlackGhost_Umbasa_Invade",
            "Flask Recovery - Black Phantom - Gold - Invasion",
            True,
            int,
            'Number of est recovery of red gold spirits of invading orbs',
        ),
        ParamFieldInfo(
            "BlackGhost_Berserker_Invade",
            "Flask Recovery - Black Phantom - Berserker - Invasion",
            True,
            int,
            'Invasion Orb Red Berserker Est Recovery Number',
        ),
        ParamFieldInfo(
            "RedHunter1",
            "Flask Recovery - Red Hunter [1]",
            True,
            int,
            "Number of rescue guests' est recovery",
        ),
        ParamFieldInfo(
            "RedHunter2",
            "Flask Recovery - Red Hunter [2]",
            True,
            int,
            'Number of est recovery of Red Scare Spirit 2',
        ),
        ParamFieldInfo(
            "GuardianOfForest",
            "Flask Recovery - Forest Guardian",
            True,
            int,
            'Map guardian spirit (forest) est recovery number',
        ),
        ParamFieldInfo(
            "GuardianOfAnor",
            "Flask Recovery - Darkmoon Blade",
            True,
            int,
            'Map Guardian Spirit (Anor) Est Recovery Number',
        ),
        ParamFieldInfo(
            "BattleRoyal",
            "Flask Recovery - Arena",
            True,
            int,
            'Number of est recovery in the arena',
        ),
        ParamFieldInfo(
            "YellowMonk",
            "Flask Recovery - Yellow Monk",
            True,
            int,
            'The number of est recovery of the old man in yellow',
        ),
        ParamFieldInfo(
            "pad1[48]",
            "pad",
            False,
            pad_field(48),
            '',
        ),
    ],
}
