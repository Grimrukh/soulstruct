from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST = {
    "param_type": "LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "DrawDist_LvBegin",
            "Draw Distance - Level Start",
            True,
            int,
            'Drawing distance scale activation level (start)',
        ),
        ParamFieldInfo(
            "DrawDist_LvEnd",
            "Draw Distance - Level End",
            True,
            int,
            'Drawing distance scale activation level (completed)',
        ),
        ParamFieldInfo(
            "reserve0[2]",
            "Reserve",
            False,
            pad_field(2),
            'Reserve',
        ),
        ParamFieldInfo(
            "DrawDist_ScaleBegin",
            "Draw Distance - Scale Start",
            True,
            float,
            'Drawing distance scale (start)',
        ),
        ParamFieldInfo(
            "DrawDist_ScaleEnd",
            "Draw Distance - Scale End",
            True,
            float,
            'Drawing distance scale (completed)',
        ),
        ParamFieldInfo(
            "ShadwDrawDist_LvBegin",
            "Shadow Draw Distance - Level Start",
            True,
            int,
            'Shadow drawing distance scale activation level (start)',
        ),
        ParamFieldInfo(
            "ShadwDrawDist_LvEnd",
            "Shadow Draw Distance - Level End",
            True,
            int,
            'Shadow drawing distance scale activation level (completed)',
        ),
        ParamFieldInfo(
            "reserve1[2]",
            "Reserve",
            False,
            pad_field(2),
            'Reserve',
        ),
        ParamFieldInfo(
            "ShadwDrawDist_ScaleBegin",
            "Shadow Draw Distance - Scale Start",
            True,
            float,
            'Shadow drawing distance scale (start)',
        ),
        ParamFieldInfo(
            "ShadwDrawDist_ScaleEnd",
            "Shadow Draw Distance - Scale End",
            True,
            float,
            'Shadow drawing distance scale (completed)',
        ),
        ParamFieldInfo(
            "reserve2[24]",
            "Reserve",
            False,
            pad_field(24),
            'Reserve',
        ),
    ],
}
