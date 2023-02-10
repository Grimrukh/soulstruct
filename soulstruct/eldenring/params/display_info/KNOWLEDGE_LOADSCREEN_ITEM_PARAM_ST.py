from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


KNOWLEDGE_LOADSCREEN_ITEM_PARAM_ST = {
    "param_type": "KNOWLEDGE_LOADSCREEN_ITEM_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "disableParam_NT:1",
            "Disable Param - Network Test",
            True,
            int,
            'Parameters marked with �� are excluded in the NT version package.',
        ),
        ParamFieldInfo(
            "disableParamReserve1:7",
            "Reserve for package output 1",
            False,
            bit_pad_field(7),
            'Reserve for package output 1',
        ),
        ParamFieldInfo(
            "disableParamReserve2[3]",
            "Reserve for package output 2",
            False,
            pad_field(3),
            'Reserve for package output 2',
        ),
        ParamFieldInfo(
            "unlockFlagId",
            "Unlock Flag ID",
            True,
            int,
            'Lifting flag (default: 0). If this event flag is set, the ban will be lifted (displayed on the loading screen). If it is 0, the ban is always lifted. The invalid flag has priority',
        ),
        ParamFieldInfo(
            "invalidFlagId",
            "Invalid Flag ID",
            True,
            int,
            'Invalid flag (default: 0). If this event flag is set, it will be disabled (it will not be displayed on the loading screen). If it is 0, this flag is not always set.',
        ),
        ParamFieldInfo(
            "msgId",
            "Message ID",
            True,
            int,
            'Text ID (Loading Text.xlsx). Used for both loading titles and loading text',
        ),
    ],
}
