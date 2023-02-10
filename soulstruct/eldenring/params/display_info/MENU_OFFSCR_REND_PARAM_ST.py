from soulstruct.base.params.utils import ParamFieldInfo, pad_field, bit_pad_field


MENU_OFFSCR_REND_PARAM_ST = {
    "param_type": "MENU_OFFSCR_REND_PARAM_ST",
    "file_name": "",  # TODO
    "nickname": "",  # TODO
    "fields": [
        ParamFieldInfo(
            "camAtPosX",
            "Camera Gaze Point: X",
            True,
            float,
            'Camera gaze point X',
        ),
        ParamFieldInfo(
            "camAtPosY",
            "Camera Gaze Point: Y",
            True,
            float,
            'Camera gaze point Y',
        ),
        ParamFieldInfo(
            "camAtPosZ",
            "Camera Gaze Point: Z",
            True,
            float,
            'Camera gaze point Z',
        ),
        ParamFieldInfo(
            "camDist",
            "Camera Distance",
            True,
            float,
            'Camera distance',
        ),
        ParamFieldInfo(
            "camRotX",
            "Camera Rotation: X",
            True,
            float,
            'Camera oriented X',
        ),
        ParamFieldInfo(
            "camRotY",
            "Camera Rotation: Y",
            True,
            float,
            'Suitable for camera Y',
        ),
        ParamFieldInfo(
            "camFov",
            "Camera Field of View",
            True,
            float,
            'Camera angle of view',
        ),
        ParamFieldInfo(
            "camDistMin",
            "Camera Distance - Minimum",
            True,
            float,
            'Shortest distance when operating the camera',
        ),
        ParamFieldInfo(
            "camDistMax",
            "Camera Distance - Maximum",
            True,
            float,
            'Longest distance when operating the camera',
        ),
        ParamFieldInfo(
            "camRotXMin",
            "Camera Rotation - Minimum",
            True,
            float,
            'Minimum orientation when operating the camera',
        ),
        ParamFieldInfo(
            "camRotXMax",
            "Camera Rotation - Maximum",
            True,
            float,
            'Maximum orientation when operating the camera',
        ),
        ParamFieldInfo(
            "GparamID",
            "GPARAM ID",
            True,
            int,
            'GparamID',
        ),
        ParamFieldInfo(
            "envTexId",
            "Env Texture ID",
            True,
            int,
            'Environment map texture ID. It corresponds to 4 digits of N: \\ GR \\ data \\ Other \\ SysEnvTex \\ GILM ???? _rem.dds.',
        ),
        ParamFieldInfo(
            "Grapm_ID_forPS4",
            "GPARAM ID - PS4",
            True,
            int,
            'Gparam ID (for PS4)',
        ),
        ParamFieldInfo(
            "Grapm_ID_forXB1",
            "GPARAM ID - XB1",
            True,
            int,
            'Gparam ID (for Xbox One)',
        ),
        ParamFieldInfo(
            "pad[4]",
            "reserve",
            False,
            pad_field(4),
            'reserve',
        ),
    ],
}
