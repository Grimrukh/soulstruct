from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_MOTION_BLUR_QUALITY_DETAIL = {
    "param_type": "CS_MOTION_BLUR_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "Enabled",
            "Motion Blur Enabled",
            True,
            int,
            'Motion blur Enabled',
        ),
        ParamFieldInfo(
            "ombEnabled",
            "Object Motion Blur Enabled",
            True,
            int,
            'OMB (object motion blur) Enabled',
        ),
        ParamFieldInfo(
            "forceScaleVelocityBuffer",
            "Force Scale Velocity Buffer",
            True,
            int,
            'Decrease the resolution of the velocity buffer used internally. Not effective if you are not using precision velocity buffers',
        ),
        ParamFieldInfo(
            "cheapFilterMode",
            "Cheap Filter Mode",
            True,
            int,
            'Normally processed by the Reconstruction filter, but downgraded to a lighter process',
        ),
        ParamFieldInfo(
            "sampleCountBias",
            "Sample Count Bias",
            True,
            int,
            'Give an offset to the sample count * Set to a multiple of 2',
        ),
        ParamFieldInfo(
            "recurrenceCountBias",
            "Recurrence Count Bias",
            True,
            int,
            'Give an offset to the number of recursive blurs',
        ),
        ParamFieldInfo(
            "blurMaxLengthScale",
            "Blur Max Length Scale",
            True,
            float,
            'Scale value for blur maximum length parameter',
        ),
    ],
}
