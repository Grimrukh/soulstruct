from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


TUTORIAL_PARAM_ST = {
    "param_type": "TUTORIAL_PARAM_ST",
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
            "menuType",
            "Menu Type",
            True,
            int,
            'Specifies the type of tutorial menu to display',
        ),
        ParamFieldInfo(
            "triggerType",
            "Trigger Type",
            True,
            int,
            'Display timing (default: 0: "-"). You will see this tutorial when you open this menu. Specify 0: "-" if you do not want to display it when you open the menu.',
        ),
        ParamFieldInfo(
            "repeatType",
            "Repeat Type",
            True,
            int,
            'Number of times to display (default: 0: once in the game)',
        ),
        ParamFieldInfo(
            "pad1[1]",
            "Padding",
            False,
            pad_field(1),
            '',
        ),
        ParamFieldInfo(
            "imageId",
            "Image ID",
            True,
            int,
            'Specifies the tutorial image ID to display (default: 0). Specify 0 if you do not want to display the image',
        ),
        ParamFieldInfo(
            "pad2[2]",
            "Padding",
            False,
            pad_field(2),
            '',
        ),
        ParamFieldInfo(
            "unlockEventFlagId",
            "Unlock Event Flag ID",
            True,
            int,
            'Event flag ID for display permission (default: 0). It will not be displayed until this flag is set. Specify 0 if you always want to allow',
        ),
        ParamFieldInfo(
            "textId",
            "Text ID",
            True,
            int,
            'ID of the text to be displayed in the tutorial [TutorialText.xlsm]. This text ID is used for both "Title" and "Body"',
        ),
        ParamFieldInfo(
            "displayMinTime",
            "Display Minimum Time",
            True,
            float,
            "Shortest display guaranteed time [seconds]. Even if it is closed due to an event etc., it will be closed after displaying at least this time. It's only for toast, so it's ignored in modals",
        ),
        ParamFieldInfo(
            "displayTime",
            "Display Time",
            True,
            float,
            "Display time [seconds]. It will close automatically after this time has passed since the toast was displayed. It's only for toast, so it's ignored in modals",
        ),
        ParamFieldInfo(
            "pad3[4]",
            "Padding",
            False,
            pad_field(4),
            '',
        ),
    ],
}
