from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_REFLECTION_QUALITY_DETAIL = {
    "param_type": "CS_REFLECTION_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "enabled",
            "Reflection Enabled",
            True,
            int,
            'Reflective effective',
        ),
        ParamFieldInfo(
            "localLightEnabled",
            "Local Light Enabled",
            True,
            int,
            'Local light enabled',
        ),
        ParamFieldInfo(
            "localLightForceEnabled",
            "Local Light Forced Enabled",
            True,
            int,
            'Local light forced enable',
        ),
        ParamFieldInfo(
            "dmy[1]",
            "dmy",
            False,
            pad_field(1),
            '',
        ),
        ParamFieldInfo(
            "resolutionDivider",
            "Resolution Scale",
            True,
            int,
            'Resolution scale',
        ),
        ParamFieldInfo(
            "ssrEnabled",
            "SSR Enabled",
            True,
            int,
            'SSR enabled',
        ),
        ParamFieldInfo(
            "ssrGaussianBlurEnabled",
            "Gaussian Blur Enabled",
            True,
            int,
            'Gaussian blur permission',
        ),
        ParamFieldInfo(
            "dmy2[2]",
            "dmy",
            False,
            pad_field(2),
            '',
        ),
        ParamFieldInfo(
            "ssrDepthRejectThresholdScale",
            "Calculated Distance Scale",
            True,
            float,
            'Calculated distance scale',
        ),
        ParamFieldInfo(
            "ssrRayTraceStepScale",
            "Raytrace Step Scale",
            True,
            float,
            'Raytrace step factor (multiply by SSR parameter)',
        ),
        ParamFieldInfo(
            "ssrFadeToViewerBias",
            "Fade Angle Bias",
            True,
            float,
            'Fade angle bias. High quality when made smaller',
        ),
        ParamFieldInfo(
            "ssrFresnelRejectBias",
            "Fresnel Reject Bias",
            True,
            float,
            'Fresnel reject bias. High quality when made smaller',
        ),
    ],
}
