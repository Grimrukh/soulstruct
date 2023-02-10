from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


WHITE_SIGN_COOL_TIME_PARAM_ST = {
    "param_type": "WHITE_SIGN_COOL_TIME_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "limitationTime_Normal",
            "Limitation Time - Normal",
            True,
            float,
            'Time limit [sec] (normal, dry fingerless)',
        ),
        ParamFieldInfo(
            "limitationTime_NormalDriedFinger",
            "Limitation Time - Normal (Dried Finger)",
            True,
            float,
            'Time limit [sec] (normal / dry finger)',
        ),
        ParamFieldInfo(
            "limitationTime_Guardian",
            "Limitation Time - Guardian",
            True,
            float,
            'Time limit [sec] (Map guardian, dry fingerless)',
        ),
        ParamFieldInfo(
            "limitationTime_GuardianDriedFinger",
            "Limitation Time - Guardian (Dried Finger)",
            True,
            float,
            'Time limit [sec] (Map guardian / dry finger)',
        ),
    ],
}
