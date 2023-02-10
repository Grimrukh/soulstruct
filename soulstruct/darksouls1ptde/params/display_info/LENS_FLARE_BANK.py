from __future__ import annotations

__all__ = ["LENS_FLARE_BANK"]

from soulstruct.base.params.utils import ParamFieldInfo

LENS_FLARE_BANK = {
    "param_type": "LENS_FLARE_BANK",
    "file_name": "LensFlareBank",
    "nickname": "LensFlares",
    "fields": [
        ParamFieldInfo(
            "texId",
            "LensFlareTextureID",
            True,
            int,
            "Texture ID of lens flare (texture name format is 'lensflare_XX'). -1 means disabled.",
        ),
        ParamFieldInfo("isFlare", "IsLensFlare", True, bool, "Flare if enabled, or 'ghost' if disabled."),
        ParamFieldInfo("enableRoll", "EnableRotation", True, bool, "Allows lens flare texture to rotate with camera."),
        ParamFieldInfo(
            "enableScale", "EnableScaling", True, bool, "Allows lens flare texture to change scale with camera."
        ),
        ParamFieldInfo(
            "locateDistRate",
            "PositionRatio",
            True,
            float,
            "Relative position of lens flare between light source (0.0) and center of screen (1.0).",
        ),
        ParamFieldInfo("texScale", "TextureScale", True, float, "Base scaling of lens flare texture."),
        ParamFieldInfo("colR", "TextureRed", True, int, "Red channel (0-255) of lens flare texture."),
        ParamFieldInfo("colG", "TextureGreen", True, int, "Green channel (0-255) of lens flare texture."),
        ParamFieldInfo("colB", "TextureBlue", True, int, "Blue channel (0-255) of lens flare texture."),
        ParamFieldInfo("colA", "TextureAlpha", True, int, "Alpha channel (0-255) of lens flare texture."),
    ],
}
