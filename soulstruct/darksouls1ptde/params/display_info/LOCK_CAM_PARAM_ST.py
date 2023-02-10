from __future__ import annotations

__all__ = ["LOCK_CAM_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo, pad_field

LOCK_CAM_PARAM_ST = {
    "param_type": "LOCK_CAM_PARAM_ST",
    "file_name": "LockCamParam",
    "nickname": "Cameras",
    "fields": [
        ParamFieldInfo(
            "camDistTarget",
            "CameraDistanceFromTarget",
            True,
            float,
            "Distance maintained from target by camera in meters. (Default value is 4.)",
        ),
        ParamFieldInfo(
            "rotRangeMinX",
            "MinRotationElevation",
            True,
            float,
            "Minimum angle of elevation (X-axis rotation) permitted for camera.",
        ),
        ParamFieldInfo(
            "lockRotXShiftRatio",
            "LockElevationShiftRatio",
            True,
            float,
            "'Lock X-rotation shift ratio (0.0 to 1.0).' Unclear effect. Default value is 0.6.",
        ),
        ParamFieldInfo(
            "chrOrgOffset_Y",
            "CharacterVerticalOffset",
            True,
            float,
            "Vertical offset of camera target from character's base. Default value is 1.42.",
        ),
        ParamFieldInfo(
            "chrLockRangeMaxRadius",
            "MaxDistanceFromCharacter",
            True,
            float,
            "Maximum distance ('radius') of camera from character in meters. Default value is 15; only other "
            "value used is 7.",
        ),
        ParamFieldInfo(
            "camFovY",
            "VerticalFieldOfView",
            True,
            float,
            "Vertical field of view of camera in degrees. Default value is 43. Never goes above 48 (Lost Izalith).",
        ),
        ParamFieldInfo("pad[8]", "Pad1", False, pad_field(8), "Null padding."),
    ],
}
