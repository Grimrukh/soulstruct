from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_EFFECT_QUALITY_DETAIL = {
    "param_type": "CS_EFFECT_QUALITY_DETAIL",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "softParticleEnabled",
            "Soft Particles Enabled",
            True,
            int,
            'Soft particles Enabled',
        ),
        ParamFieldInfo(
            "glowEnabled",
            "Glow Enabled",
            True,
            int,
            'Glow effective',
        ),
        ParamFieldInfo(
            "distortionEnable",
            "Distortion Enabled",
            True,
            int,
            'Distortion effective',
        ),
        ParamFieldInfo(
            "cs_upScaleEnabledType",
            "Enable Bilateral Upscale",
            True,
            int,
            'Bilateral upscale effective',
        ),
        ParamFieldInfo(
            "fNumOnceEmitsScale",
            "Number of Emits in Instance",
            True,
            float,
            'Number of Emits at one time',
        ),
        ParamFieldInfo(
            "fEmitSpanScale",
            "Emit Interval",
            True,
            float,
            'Emit interval',
        ),
        ParamFieldInfo(
            "fLodDistance1Scale",
            "1st LOD Distance Scale",
            True,
            float,
            '1st stage LOD distance scale',
        ),
        ParamFieldInfo(
            "fLodDistance2Scale",
            "2nd LOD Distance Scale",
            True,
            float,
            'Second stage LOD distance scale',
        ),
        ParamFieldInfo(
            "fLodDistance3Scale",
            "3rd LOD Distance Scale",
            True,
            float,
            '3rd stage LOD distance scale',
        ),
        ParamFieldInfo(
            "fLodDistance4Scale",
            "4th LOD Distance Scale",
            True,
            float,
            '4th stage LOD distance scale',
        ),
        ParamFieldInfo(
            "fScaleRenderDistanceScale",
            "Scale Render Distance Scale",
            True,
            float,
            'Magnification to the distance registered in the reduction buffer',
        ),
        ParamFieldInfo(
            "dmy[4]",
            "dummy",
            False,
            pad_field(4),
            '',
        ),
    ],
}
