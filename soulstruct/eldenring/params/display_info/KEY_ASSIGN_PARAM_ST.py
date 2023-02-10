from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


KEY_ASSIGN_PARAM_ST = {
    "param_type": "KEY_ASSIGN_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "padKeyId",
            "Pad Key ID",
            True,
            int,
            'Pad (physical key)',
        ),
        ParamFieldInfo(
            "keyboardModifyKey",
            "Keyboard Modify Key",
            True,
            int,
            'Keyboard modifier keys',
        ),
        ParamFieldInfo(
            "keyboardKeyId",
            "Keyboard Key ID",
            True,
            int,
            'Keyboard (physical keys)',
        ),
        ParamFieldInfo(
            "mouseModifyKey",
            "Mouse Modify Key",
            True,
            int,
            'Mouse modifier key',
        ),
        ParamFieldInfo(
            "mouseKeyId",
            "Mouse Key ID",
            True,
            int,
            'Mouse (physical key)',
        ),
        ParamFieldInfo(
            "reserved[12]",
            "----",
            False,
            pad_field(12),
            '',
        ),
    ],
}
