from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


HIT_EFFECT_SFX_CONCEPT_PARAM_ST = {
    "param_type": "HIT_EFFECT_SFX_CONCEPT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "atkIron_1",
            "Iron [1]",
            True,
            int,
            'Iron: Concept 1',
        ),
        ParamFieldInfo(
            "atkIron_2",
            "Iron [2]",
            True,
            int,
            'Iron: Concept 2',
        ),
        ParamFieldInfo(
            "atkLeather_1",
            "Leather [1]",
            True,
            int,
            'Leather: Concept 1',
        ),
        ParamFieldInfo(
            "atkLeather_2",
            "Leather [2]",
            True,
            int,
            'Leather: Concept 2',
        ),
        ParamFieldInfo(
            "atkWood_1",
            "Wood [1]",
            True,
            int,
            'Wooden: Concept 1',
        ),
        ParamFieldInfo(
            "atkWood_2",
            "Wood [2]",
            True,
            int,
            'Wooden: Concept 2',
        ),
        ParamFieldInfo(
            "atkBody_1",
            "Flesh [1]",
            True,
            int,
            'Meat: Concept 1',
        ),
        ParamFieldInfo(
            "atkBody_2",
            "Flesh [2]",
            True,
            int,
            'Meat: Concept 2',
        ),
        ParamFieldInfo(
            "atkStone_1",
            "Stone [1]",
            True,
            int,
            'Corrosion: Concept 1',
        ),
        ParamFieldInfo(
            "atkStone_2",
            "Stone [2]",
            True,
            int,
            'Corrosion: Concept 2',
        ),
        ParamFieldInfo(
            "pad[4]",
            "pad",
            False,
            pad_field(4),
            '',
        ),
        ParamFieldInfo(
            "atkNone_1",
            "None [1]",
            True,
            int,
            'None: Concept 1',
        ),
        ParamFieldInfo(
            "atkNone_2",
            "None [2]",
            True,
            int,
            'None: Concept 2',
        ),
        ParamFieldInfo(
            "reserve[52]",
            "Reserved area",
            False,
            pad_field(52),
            '',
        ),
    ],
}
