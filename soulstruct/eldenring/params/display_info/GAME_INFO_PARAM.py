from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


GAME_INFO_PARAM = {
    "param_type": "GAME_INFO_PARAM",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "titleMsgId",
            "Title Message ID",
            True,
            int,
            'Title name',
        ),
        ParamFieldInfo(
            "contentMsgId",
            "Content Messae ID",
            True,
            int,
            'Contents',
        ),
        ParamFieldInfo(
            "value",
            "Price",
            True,
            int,
            'price',
        ),
        ParamFieldInfo(
            "sortId",
            "Sort ID",
            True,
            int,
            'Sort ID',
        ),
        ParamFieldInfo(
            "eventId",
            "Action ID",
            True,
            int,
            'This is the action ID that determines the sales status.',
        ),
        ParamFieldInfo(
            "Pad[12]",
            "Padding",
            False,
            pad_field(12),
            'Padding',
        ),
    ],
}
