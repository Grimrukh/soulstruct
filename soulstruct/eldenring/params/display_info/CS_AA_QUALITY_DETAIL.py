from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_AA_QUALITY_DETAIL = {
    "param_type": "CS_AA_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "enabled",
            "AA Enabled",
            True,
            int,
            'AA valid',
        ),
        ParamFieldInfo(
            "forceFXAA2",
            "Force FXAA2",
            True,
            int,
            'Force FXAA2',
        ),
        ParamFieldInfo(
            "dmy[2]",
            "dmy",
            False,
            pad_field(2),
            '',
        ),
    ],
}
