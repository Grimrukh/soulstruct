from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


CS_KEY_ASSIGN_MENUITEM_PARAM = {
    "param_type": "CS_KEY_ASSIGN_MENUITEM_PARAM",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "textID",
            "Text ID",
            True,
            int,
            'Key specified �� Item name, 1-line help ID. No key specified �� Category name ID. No text specified �� Not displayed in pad / key settings (operation list display only)',
        ),
        ParamFieldInfo(
            "key",
            "Key",
            True,
            int,
            'User input key to be assigned. If not specified, it will be treated as a category display item.',
        ),
        ParamFieldInfo(
            "enableUnassign",
            "Allow Unassignment",
            True,
            int,
            'Is it possible to unassign (default: possible)',
        ),
        ParamFieldInfo(
            "enablePadConfig",
            "Allow Pad Config",
            True,
            int,
            'Is it possible to change the pad operation assignment (default: possible)?',
        ),
        ParamFieldInfo(
            "enableMouseConfig",
            "Allow Mouse Config",
            True,
            int,
            'Is it possible to change the mouse operation assignment (default: possible)?',
        ),
        ParamFieldInfo(
            "group",
            "Group",
            True,
            int,
            'Group for determining duplicate assignments. Cannot be duplicated in the same group',
        ),
        ParamFieldInfo(
            "mappingTextID",
            "Mapping Text ID",
            True,
            int,
            'Item name to be displayed in the operation list. 0 :: Do not display in the list',
        ),
        ParamFieldInfo(
            "viewPad",
            "View Pad",
            True,
            int,
            'Whether to display with key config (pad) (default: display)',
        ),
        ParamFieldInfo(
            "viewKeyboardMouse",
            "View Keyboard/Mouse",
            True,
            int,
            'Whether to display with key config (mouse / keyboard) (default: display)',
        ),
        ParamFieldInfo(
            "padding[6]",
            "padding",
            False,
            pad_field(6),
            'Is it possible to change the pad operation assignment (default: possible)?',
        ),
    ],
}
