from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MAP_MIMICRY_ESTABLISHMENT_PARAM_ST = {
    "param_type": "MAP_MIMICRY_ESTABLISHMENT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "mimicryEstablishment0",
            "Mimicry Weight [0]",
            True,
            float,
            'Mimicry weight 0',
        ),
        ParamFieldInfo(
            "mimicryEstablishment1",
            "Mimicry Weight [1]",
            True,
            float,
            'Mimicry weight 1',
        ),
        ParamFieldInfo(
            "mimicryEstablishment2",
            "Mimicry Weight [2]",
            True,
            float,
            'Mimicry weight 2',
        ),
        ParamFieldInfo(
            "mimicryBeginSfxId0",
            "Mimicry - Init SFX ID [0]",
            True,
            int,
            'Mimicry 0 SFXID Forward swing',
        ),
        ParamFieldInfo(
            "mimicrySfxId0",
            "Mimicry - Midst SFX ID [0]",
            True,
            int,
            'Mimicry 0 SFXID body',
        ),
        ParamFieldInfo(
            "mimicryEndSfxId0",
            "Mimicry - End SFX ID [0]",
            True,
            int,
            'Mimicry 0 SFXID release',
        ),
        ParamFieldInfo(
            "mimicryBeginSfxId1",
            "Mimicry - Init SFX ID [1]",
            True,
            int,
            'Mimicry 1 SFXID Forward swing',
        ),
        ParamFieldInfo(
            "mimicrySfxId1",
            "Mimicry - Midst SFX ID [1]",
            True,
            int,
            'Mimicry 1 SFXID body',
        ),
        ParamFieldInfo(
            "mimicryEndSfxId1",
            "Mimicry - End SFX ID [1]",
            True,
            int,
            'Mimicry 1 SFXID release',
        ),
        ParamFieldInfo(
            "mimicryBeginSfxId2",
            "Mimicry - Init SFX ID [2]",
            True,
            int,
            'Mimicry 2 SFXID Forward swing',
        ),
        ParamFieldInfo(
            "mimicrySfxId2",
            "Mimicry - Midst SFX ID [2]",
            True,
            int,
            'Mimicry 2 SFXID body',
        ),
        ParamFieldInfo(
            "mimicryEndSfxId2",
            "Mimicry - End SFX ID [2]",
            True,
            int,
            'Mimicry 2 SFXID cancellation',
        ),
        ParamFieldInfo(
            "pad1[16]",
            "pad",
            False,
            pad_field(16),
            'pad',
        ),
    ],
}
