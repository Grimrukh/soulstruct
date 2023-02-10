from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


GESTURE_PARAM_ST = {
    "param_type": "GESTURE_PARAM_ST",
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
            "itemId",
            "Item ID",
            True,
            int,
            'Reference item ID. Used to bring in the gesture text ID, icon ID, and sort ID for each menu. Register the tool ID of the equipment parameter',
        ),
        ParamFieldInfo(
            "msgAnimId",
            "Message Anim ID",
            True,
            int,
            'Anime ID for attaching messages. Specify the animation ID when attaching a message',
        ),
        ParamFieldInfo(
            "cannotUseRiding:1",
            "Cannot Use while Riding",
            True,
            int,
            'Is it prohibited to use while riding (default: �~)? If ��, it cannot be used while riding',
        ),
        ParamFieldInfo(
            "pad2:7",
            "Reserved area",
            False,
            bit_pad_field(7),
            '',
        ),
        ParamFieldInfo(
            "pad1[3]",
            "Reserved area",
            False,
            pad_field(3),
            '',
        ),
    ],
}
