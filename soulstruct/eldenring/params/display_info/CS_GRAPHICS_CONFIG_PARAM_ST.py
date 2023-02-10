from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_GRAPHICS_CONFIG_PARAM_ST = {
    "param_type": "CS_GRAPHICS_CONFIG_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "m_textureFilterQuality",
            "Texture Filter Quality",
            True,
            int,
            'Texture filter quality (default Midele)',
        ),
        ParamFieldInfo(
            "m_aaQuality",
            "AA Quality",
            True,
            int,
            'AA quality (default High)',
        ),
        ParamFieldInfo(
            "m_ssaoQuality",
            "SSAO Quality",
            True,
            int,
            'SSAO quality (default High)',
        ),
        ParamFieldInfo(
            "m_dofQuality",
            "Depth of Field Quality",
            True,
            int,
            'Depth of field quality (default High)',
        ),
        ParamFieldInfo(
            "m_motionBlurQuality",
            "Motion Blur Quality",
            True,
            int,
            'Motion blur quality (default High)',
        ),
        ParamFieldInfo(
            "m_shadowQuality",
            "Shadow Quality",
            True,
            int,
            'Shadow quality (default High)',
        ),
        ParamFieldInfo(
            "m_lightingQuality",
            "Lighting Quality",
            True,
            int,
            'Lighting quality (default High)',
        ),
        ParamFieldInfo(
            "m_effectQuality",
            "Effect Quality",
            True,
            int,
            'Effect quality (default High)',
        ),
        ParamFieldInfo(
            "m_decalQuality",
            "Decal Quality",
            True,
            int,
            'Decal quality (default High)',
        ),
        ParamFieldInfo(
            "m_reflectionQuality",
            "Reflection Quality",
            True,
            int,
            'Reflection quality (default High)',
        ),
        ParamFieldInfo(
            "m_waterQuality",
            "Water Quality",
            True,
            int,
            'Water quality (default High)',
        ),
        ParamFieldInfo(
            "m_shaderQuality",
            "Shader Quality",
            True,
            int,
            'Shader quality (default High)',
        ),
        ParamFieldInfo(
            "m_volumetricEffectQuality",
            "Volumetric Effect Quality",
            True,
            int,
            'Volumetric effect quality (default High)',
        ),
        ParamFieldInfo(
            "m_dummy[3]",
            "dmy",
            False,
            pad_field(3),
            '',
        ),
    ],
}
