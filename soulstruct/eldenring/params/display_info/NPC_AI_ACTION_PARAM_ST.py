from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


NPC_AI_ACTION_PARAM_ST = {
    "param_type": "NPC_AI_ACTION_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "moveDir",
            "Move Direction",
            True,
            int,
            'Moving direction to enter',
        ),
        ParamFieldInfo(
            "key1",
            "Key [1]",
            True,
            int,
            'Key to enter',
        ),
        ParamFieldInfo(
            "key2",
            "Key [2]",
            True,
            int,
            'Key to enter',
        ),
        ParamFieldInfo(
            "key3",
            "Key [3]",
            True,
            int,
            'Key to enter',
        ),
        ParamFieldInfo(
            "bMoveDirHold",
            "Handle Move Direction as Long Press",
            True,
            int,
            'Whether to handle the input movement direction as long press',
        ),
        ParamFieldInfo(
            "bKeyHold1",
            "Handle Key [1] Hold as Long Press",
            True,
            int,
            'Whether to treat the key to be entered as a long press',
        ),
        ParamFieldInfo(
            "bKeyHold2",
            "Handle Key [2] Hold as Long Press",
            True,
            int,
            'Whether to treat the key to be entered as a long press',
        ),
        ParamFieldInfo(
            "bKeyHold3",
            "Handle Key [3] Hold as Long Press",
            True,
            int,
            'Whether to treat the key to be entered as a long press',
        ),
        ParamFieldInfo(
            "gestureId",
            "Gesture ID",
            True,
            int,
            'Gesture ID',
        ),
        ParamFieldInfo(
            "bLifeEndSuccess",
            "AI Goal Waits For Duration End",
            True,
            int,
            'If this is ON, the AI goal will not be successful until the end of its life',
        ),
        ParamFieldInfo(
            "pad1[3]",
            "pad",
            False,
            pad_field(3),
            'pad',
        ),
    ],
}
