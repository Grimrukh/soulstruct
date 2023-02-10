from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SE_MATERIAL_CONVERT_PARAM_ST = {
    "param_type": "SE_MATERIAL_CONVERT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "seMaterialId",
            "SE Material ID",
            True,
            int,
            'Conversion from SFX material ID (3 digits) to SE material ID (2 digits)',
        ),
        ParamFieldInfo(
            "pad[3]",
            "Padding",
            False,
            pad_field(3),
            'Padding',
        ),
    ],
}
