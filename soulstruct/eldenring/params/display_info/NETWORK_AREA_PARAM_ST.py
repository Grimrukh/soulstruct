from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


NETWORK_AREA_PARAM_ST = {
    "param_type": "NETWORK_AREA_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "cellSizeX",
            "Cell Size: X",
            True,
            float,
            'Cell size X',
        ),
        ParamFieldInfo(
            "cellSizeY",
            "Cell Size: Y",
            True,
            float,
            'Cell size Y',
        ),
        ParamFieldInfo(
            "cellSizeZ",
            "Cell Size: Z",
            True,
            float,
            'Cell size Z',
        ),
        ParamFieldInfo(
            "cellOffsetX",
            "Cell Offset: X",
            True,
            float,
            'Cell offset X',
        ),
        ParamFieldInfo(
            "cellOffsetY",
            "Cell Offset: Y",
            True,
            float,
            'Cell offset Y',
        ),
        ParamFieldInfo(
            "cellOffsetZ",
            "Cell Offset: Z",
            True,
            float,
            'Cell offset Z',
        ),
        ParamFieldInfo(
            "enableBloodstain:1",
            "Enable Bloodstain",
            True,
            int,
            'Effective bloodstain / death illusion',
        ),
        ParamFieldInfo(
            "enableBloodMessage:1",
            "Enable Blood Message",
            True,
            int,
            'Blood character valid',
        ),
        ParamFieldInfo(
            "enableGhost:1",
            "Enable Ghost",
            True,
            int,
            'Phantom effective',
        ),
        ParamFieldInfo(
            "enableMultiPlay:1",
            "Enable Multiplayer",
            True,
            int,
            'Multiplayer enabled',
        ),
        ParamFieldInfo(
            "enableRingSearch:1",
            "Enable Ring Search",
            True,
            int,
            'Is it a search target for ring search? (Area called Kanemori Ash Spirit / Relief Blue Spirit)',
        ),
        ParamFieldInfo(
            "enableBreakInSearch:1",
            "Enable Invasion Search",
            True,
            int,
            'Is it the target of intrusion search?',
        ),
        ParamFieldInfo(
            "dummy[3]",
            "dummy",
            False,
            pad_field(3),
            '',
        ),
    ],
}
