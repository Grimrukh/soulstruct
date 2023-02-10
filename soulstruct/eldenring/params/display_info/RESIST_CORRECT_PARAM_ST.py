from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


RESIST_CORRECT_PARAM_ST = {
    "param_type": "RESIST_CORRECT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "addPoint1",
            "Additional Resistance - First Activation",
            True,
            float,
            'A value that is added to the resistance value after the abnormal condition is activated once.',
        ),
        ParamFieldInfo(
            "addPoint2",
            "Additional Resistance - Second Activation",
            True,
            float,
            'A value that is added to the resistance value after the abnormal condition is activated twice.',
        ),
        ParamFieldInfo(
            "addPoint3",
            "Additional Resistance - Third Activation",
            True,
            float,
            'A value that is added to the resistance value after the abnormal condition is activated 3 times.',
        ),
        ParamFieldInfo(
            "addPoint4",
            "Additional Resistance - Fourth Activation",
            True,
            float,
            'A value that is added to the resistance value after the abnormal condition is activated 4 times.',
        ),
        ParamFieldInfo(
            "addPoint5",
            "Additional Resistance - Fifth Activation",
            True,
            float,
            'A value that is added to the resistance value after the abnormal condition is activated 5 times.',
        ),
        ParamFieldInfo(
            "addRate1",
            "Resistance Multiplier - First Activation",
            True,
            float,
            'Magnification applied to the resistance value after the abnormal condition is activated once',
        ),
        ParamFieldInfo(
            "addRate2",
            "Resistance Multiplier - Second Activation",
            True,
            float,
            'Magnification applied to the resistance value after the abnormal condition is activated twice',
        ),
        ParamFieldInfo(
            "addRate3",
            "Resistance Multiplier - Third Activation",
            True,
            float,
            'Magnification applied to the resistance value after the abnormal condition is activated 3 times',
        ),
        ParamFieldInfo(
            "addRate4",
            "Resistance Multiplier - Fourth Activation",
            True,
            float,
            'Magnification applied to the resistance value after the abnormal condition is activated 4 times',
        ),
        ParamFieldInfo(
            "addRate5",
            "Resistance Multiplier - Fifth Activation",
            True,
            float,
            'Magnification applied to the resistance value after the abnormal condition is activated 5 times',
        ),
    ],
}
