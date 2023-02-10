from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_TEXTURE_FILTER_QUALITY_DETAIL = {
    "param_type": "CS_TEXTURE_FILTER_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "filter",
            "Texture Filter",
            True,
            int,
            'filter',
        ),
        ParamFieldInfo(
            "dmy[3]",
            "dmy",
            False,
            pad_field(3),
            '',
        ),
        ParamFieldInfo(
            "maxAnisoLevel",
            "Anisotropic Level",
            True,
            int,
            'Aniso level',
        ),
    ],
}
