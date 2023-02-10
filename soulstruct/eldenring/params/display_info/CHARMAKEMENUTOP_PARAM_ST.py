from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CHARMAKEMENUTOP_PARAM_ST = {
    "param_type": "CHARMAKEMENUTOP_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "commandType",
            "Command Type",
            True,
            int,
            'Command type',
        ),
        ParamFieldInfo(
            "captionId",
            "Caption ID",
            True,
            int,
            'ID of the text to be displayed',
        ),
        ParamFieldInfo(
            "faceParamId",
            "Face Param ID",
            True,
            int,
            'Face Param ID',
        ),
        ParamFieldInfo(
            "tableId",
            "Table ID - Male",
            True,
            int,
            'First ID (male) in the list of items to select. The command type is [Slider: Text ID of minimum label (n) and maximum label (n + 1), Color: ID of color table, Grid or text: First ID of character make list item, Other: Ignore]',
        ),
        ParamFieldInfo(
            "viewCondition",
            "View Condition",
            True,
            int,
            'Conditions for displaying this command',
        ),
        ParamFieldInfo(
            "previewMode",
            "Preview Mode",
            True,
            int,
            'Display mode of the character model displayed in preview',
        ),
        ParamFieldInfo(
            "reserved2[3]",
            "reserve",
            False,
            pad_field(3),
            '',
        ),
        ParamFieldInfo(
            "tableId2",
            "Table ID - Female",
            True,
            int,
            'For women with table ID. If -1, refer to for men',
        ),
        ParamFieldInfo(
            "refFaceParamId",
            "Reference Face Param ID",
            True,
            int,
            'Face param ID of the matching destination for "matching to XX"',
        ),
        ParamFieldInfo(
            "refTextId",
            "Reference Text ID",
            True,
            int,
            'Display text ID for "fit to XX"',
        ),
        ParamFieldInfo(
            "helpTextId",
            "Help Text ID",
            True,
            int,
            '1-line help text ID (-1: Get 1-line help with item text ID). Basically, item text ID = 1 line help text ID, but if you want to overwrite part of it, specify it with this parameter.',
        ),
        ParamFieldInfo(
            "unlockEventFlagId",
            "Unlock Event Flag ID",
            True,
            int,
            'Event flag to unlock this item (0: invalid value). Invalid value will always be unlocked',
        ),
        ParamFieldInfo(
            "reserved[4]",
            "reserve",
            False,
            pad_field(4),
            '',
        ),
    ],
}
