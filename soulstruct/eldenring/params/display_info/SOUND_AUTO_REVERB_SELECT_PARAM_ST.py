from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


SOUND_AUTO_REVERB_SELECT_PARAM_ST = {
    "param_type": "SOUND_AUTO_REVERB_SELECT_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "reverbType",
            "Reverb Type",
            True,
            int,
            'Reverb type',
        ),
        ParamFieldInfo(
            "AreaNo",
            "Condition: Area Number",
            True,
            int,
            'Condition: Area No. (-1: Invalid)',
        ),
        ParamFieldInfo(
            "IndoorOutdoor",
            "Condition: Indoor/Outdoor",
            True,
            int,
            'Condition: Indoor / outdoor designation (0: outdoor, 1: indoor) (-1: invalid)',
        ),
        ParamFieldInfo(
            "useDistNoA",
            "Condition: Evaluation Distance A",
            True,
            int,
            'Condition: Evaluation distance number A to use (-1: invalid)',
        ),
        ParamFieldInfo(
            "useDistNoB",
            "Condition: Evaluation Distance B",
            True,
            int,
            'Condition: Evaluation distance number B to be used (-1: invalid)',
        ),
        ParamFieldInfo(
            "pad0[1]",
            "pad0",
            False,
            pad_field(1),
            'pad0',
        ),
        ParamFieldInfo(
            "DistMinA",
            "Condition: Evaluation Distance A - Min",
            True,
            float,
            'Condition: For evaluation distance minimum specification A (less than 0: invalid)',
        ),
        ParamFieldInfo(
            "DistMaxA",
            "Condition: Evaluation Distance A - Max",
            True,
            float,
            'Condition: For evaluation distance maximum specification A (less than 0: invalid)',
        ),
        ParamFieldInfo(
            "DistMinB",
            "Condition: Evaluation Distance B - Min",
            True,
            float,
            'Condition: For evaluation distance minimum specification A (less than 0: invalid)',
        ),
        ParamFieldInfo(
            "DistMaxB",
            "Condition: Evaluation Distance B - Max",
            True,
            float,
            'Condition: For evaluation distance maximum specification A (less than 0: invalid)',
        ),
        ParamFieldInfo(
            "NoHitNumMin",
            "Condition: No Hit Minimum",
            True,
            int,
            'Condition: No Hit number (-1: invalid)',
        ),
    ],
}
