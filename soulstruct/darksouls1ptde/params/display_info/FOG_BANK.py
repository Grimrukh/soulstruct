from __future__ import annotations

__all__ = ["FOG_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo


FOG_BANK = {
    "param_type": "FOG_BANK",
    "file_name": "FogBank",
    "nickname": "Fog",
    "fields": [
        ParamFieldInfo("fogBeginZ", "FogStartDistance", True, int, "Distance (m) at which fog begins."),
        ParamFieldInfo("fogEndZ", "FogEndDistance", True, int, "Distance (m) at which fog ends."),
        ParamFieldInfo("degRotZ", "RotationZ", True, int, "Rotation of fog around the Z axis."),
        ParamFieldInfo("degRotW", "RotationW", True, int, "Rotation of fog around the W axis."),
        ParamFieldInfo("colR", "Red", True, int, "Red color channel (0-255)."),
        ParamFieldInfo("colG", "Green", True, int, "Green color channel (0-255)."),
        ParamFieldInfo("colB", "Blue", True, int, "Blue color channel (0-255)."),
        ParamFieldInfo("colA", "Alpha", True, int, "Alpha channel (0-255)."),
    ],
}
