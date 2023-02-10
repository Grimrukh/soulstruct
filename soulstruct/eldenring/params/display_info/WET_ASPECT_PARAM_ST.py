from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


WET_ASPECT_PARAM_ST = {
    "param_type": "WET_ASPECT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "baseColorR",
            "Base Color: R",
            True,
            int,
            'Base color color R.',
        ),
        ParamFieldInfo(
            "baseColorG",
            "Base Color: G",
            True,
            int,
            'Base color color G.',
        ),
        ParamFieldInfo(
            "baseColorB",
            "Base Color: B",
            True,
            int,
            'Base color color B.',
        ),
        ParamFieldInfo(
            "reserve_0[1]",
            "Spare 1",
            False,
            pad_field(1),
            '',
        ),
        ParamFieldInfo(
            "baseColorA",
            "Base Color: Alpha",
            True,
            float,
            'Base color override rate.',
        ),
        ParamFieldInfo(
            "metallic",
            "Metallic",
            True,
            int,
            "It's metallic.",
        ),
        ParamFieldInfo(
            "reserve_1[1]",
            "Spare 2",
            False,
            pad_field(1),
            '',
        ),
        ParamFieldInfo(
            "reserve_2[1]",
            "Spare 3",
            False,
            pad_field(1),
            '',
        ),
        ParamFieldInfo(
            "reserve_3[1]",
            "Spare 4",
            False,
            pad_field(1),
            '',
        ),
        ParamFieldInfo(
            "metallicRate",
            "Metallic Override Rate",
            True,
            float,
            'Metallic override rate.',
        ),
        ParamFieldInfo(
            "shininessRate",
            "Shininess Override Rate",
            True,
            float,
            'Shininess override rate.',
        ),
        ParamFieldInfo(
            "shininess",
            "Shininess",
            True,
            int,
            'Shininess.',
        ),
        ParamFieldInfo(
            "reserve_4[11]",
            "Spare 5",
            False,
            pad_field(11),
            '',
        ),
    ],
}
