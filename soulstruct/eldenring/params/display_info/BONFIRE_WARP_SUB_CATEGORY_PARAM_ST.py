from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


BONFIRE_WARP_SUB_CATEGORY_PARAM_ST = {
    "param_type": "BONFIRE_WARP_SUB_CATEGORY_PARAM_ST",
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
            "textId",
            "Text ID",
            True,
            int,
            'Subcategory display name Text ID [MenuText]',
        ),
        ParamFieldInfo(
            "tabId",
            "Tab ID",
            True,
            int,
            'Kagaribi Warp Tab ID. ID of the tab to which this subcategory belongs',
        ),
        ParamFieldInfo(
            "sortId",
            "Tab Sort ID",
            True,
            int,
            'Bonfire Warp Tab Sort ID. Display order of subcategories in tabs',
        ),
        ParamFieldInfo(
            "pad[4]",
            "pad",
            False,
            pad_field(4),
            '',
        ),
    ],
}
