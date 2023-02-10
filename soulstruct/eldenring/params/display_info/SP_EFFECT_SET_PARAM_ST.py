from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SP_EFFECT_SET_PARAM_ST = {
    "param_type": "SP_EFFECT_SET_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "spEffectId1",
            "SpEffect ID [1]",
            True,
            int,
            'Special effect ID1',
        ),
        ParamFieldInfo(
            "spEffectId2",
            "SpEffect ID [2]",
            True,
            int,
            'Special effect ID2',
        ),
        ParamFieldInfo(
            "spEffectId3",
            "SpEffect ID [3]",
            True,
            int,
            'Special effect ID3',
        ),
        ParamFieldInfo(
            "spEffectId4",
            "SpEffect ID [4]",
            True,
            int,
            'Special effect ID4',
        ),
    ],
}
