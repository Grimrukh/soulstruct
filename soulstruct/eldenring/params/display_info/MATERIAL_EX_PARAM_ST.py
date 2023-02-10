from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MATERIAL_EX_PARAM_ST = {
    "param_type": "MATERIAL_EX_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "paramName[32]",
            "Material Param Name",
            True,
            str,
            'Set the parameter name of the material. Up to 31 characters',
        ),
        ParamFieldInfo(
            "materialId",
            "Material ID",
            True,
            int,
            'NPC Para: Resident Material Expansion Para ID setting -1 for all materials',
        ),
        ParamFieldInfo(
            "materialParamValue0",
            "Material Param Value: R",
            True,
            float,
            'NPC Para: Resident Material Extended Para ID Settings',
        ),
        ParamFieldInfo(
            "materialParamValue1",
            "Material Param Value: G",
            True,
            float,
            'NPC Para: Resident Material Expansion Para ID Settings',
        ),
        ParamFieldInfo(
            "materialParamValue2",
            "Material Param Value: B",
            True,
            float,
            'NPC Para: Resident Material Expansion Para ID Settings',
        ),
        ParamFieldInfo(
            "materialParamValue3",
            "Material Param Value: A",
            True,
            float,
            'NPC Para: Resident Material Extended Para ID Settings',
        ),
        ParamFieldInfo(
            "materialParamValue4",
            "Material Param Value: I",
            True,
            float,
            'NPC Para: Resident Material Expansion Para ID Settings',
        ),
        ParamFieldInfo(
            "pad[8]",
            "Padding",
            False,
            pad_field(8),
            'Padding',
        ),
    ],
}
