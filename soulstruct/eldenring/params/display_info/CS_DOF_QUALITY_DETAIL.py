from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_DOF_QUALITY_DETAIL = {
    "param_type": "CS_DOF_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "enabled",
            "Depth of Field Enabled",
            True,
            int,
            'DOF permission',
        ),
        ParamFieldInfo(
            "dmy[3]",
            "dmy",
            False,
            pad_field(3),
            '',
        ),
        ParamFieldInfo(
            "forceHiResoBlur",
            "Force High Resolution Blur",
            True,
            int,
            'Change the HiResolutionBlur setting (-1: forced off, 0: as-is, 1: forced on)',
        ),
        ParamFieldInfo(
            "maxBlurLevel",
            "Maximum Blur Level",
            True,
            int,
            'Maximum blur level. 2: Maximum, 1: Level to one paragraph, 0: Further reduce accuracy',
        ),
    ],
}
