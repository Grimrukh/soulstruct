from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


POSTURE_CONTROL_PARAM_WEP_LEFT_ST = {
    "param_type": "POSTURE_CONTROL_PARAM_WEP_LEFT_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "a000_leftArmFB",
            "[a000] Left Arm - Front/Back",
            True,
            int,
            'Left arm_front and back',
        ),
        ParamFieldInfo(
            "a000_leftWristFB",
            "[a000] Left Wrist - Front/Back",
            True,
            int,
            'Left wrist_front and back',
        ),
        ParamFieldInfo(
            "a000_leftWristIO",
            "[a000] Left Wrist - Inside/Outside",
            True,
            int,
            'Left wrist_inside and outside',
        ),
        ParamFieldInfo(
            "a002_leftArmFB",
            "[a002] Left Arm - Front/Back",
            True,
            int,
            'Left arm_front and back',
        ),
        ParamFieldInfo(
            "a002_leftWristFB",
            "[a002] Left Wrist - Front/Back",
            True,
            int,
            'Left wrist_front and back',
        ),
        ParamFieldInfo(
            "a002_leftWristIO",
            "[a002] Left Wrist - Inside/Outside",
            True,
            int,
            'Left wrist_inside and outside',
        ),
        ParamFieldInfo(
            "a003_leftArmFB",
            "[a003] Left Arm - Front/Back",
            True,
            int,
            'Left arm_front and back',
        ),
        ParamFieldInfo(
            "a003_leftWristFB",
            "[a003] Left Wrist - Front/Back",
            True,
            int,
            'Left wrist_front and back',
        ),
        ParamFieldInfo(
            "a003_leftWristIO",
            "[a003] Left Wrist - Inside/Outside",
            True,
            int,
            'Left wrist_inside and outside',
        ),
        ParamFieldInfo(
            "pad[14]",
            "pad",
            False,
            pad_field(14),
            '',
        ),
    ],
}
