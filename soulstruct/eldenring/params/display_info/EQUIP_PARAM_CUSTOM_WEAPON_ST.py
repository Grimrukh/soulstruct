from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


EQUIP_PARAM_CUSTOM_WEAPON_ST = {
    "param_type": "EQUIP_PARAM_CUSTOM_WEAPON_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "baseWepId",
            "Base Weapon ID",
            True,
            int,
            'Weapon base ID',
        ),
        ParamFieldInfo(
            "gemId",
            "Gem ID",
            True,
            int,
            'Magic stone ID',
        ),
        ParamFieldInfo(
            "reinforceLv",
            "Reinforcement Level",
            True,
            int,
            'Enhancement value',
        ),
        ParamFieldInfo(
            "pad[7]",
            "pad",
            False,
            pad_field(7),
            'pad',
        ),
    ],
}
