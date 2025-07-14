from __future__ import annotations

__all__ = ["PARTS_DRAW_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class PARTS_DRAW_PARAM_ST(ParamRow):
    Lv01BorderDist: float = ParamField(
        float32, "lv01_BorderDist", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv01PlayDist: float = ParamField(
        float32, "lv01_PlayDist", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv12BorderDist: float = ParamField(
        float32, "lv12_BorderDist", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv12PlayDist: float = ParamField(
        float32, "lv12_PlayDist", default=2.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv23BorderDist: float = ParamField(
        float32, "lv23_BorderDist", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv23PlayDist: float = ParamField(
        float32, "lv23_PlayDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv34BorderDist: float = ParamField(
        float32, "lv34_BorderDist", default=9999.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv34PlayDist: float = ParamField(
        float32, "lv34_PlayDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv45BorderDist: float = ParamField(
        float32, "lv45_BorderDist", default=9999.0,
        tooltip="TOOLTIP-TODO",
    )
    Lv45PlayDist: float = ParamField(
        float32, "lv45_PlayDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Texlv01BorderDist: float = ParamField(
        float32, "tex_lv01_BorderDist", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    Texlv01PlayDist: float = ParamField(
        float32, "tex_lv01_PlayDist", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    EnableCrossFade: bool = ParamField(
        uint32, "enableCrossFade:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DrawDist: float = ParamField(
        float32, "drawDist", default=9999.0,
        tooltip="TOOLTIP-TODO",
    )
    DrawFadeRange: float = ParamField(
        float32, "drawFadeRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ShadowDrawDist: float = ParamField(
        float32, "shadowDrawDist", default=9999.0,
        tooltip="TOOLTIP-TODO",
    )
    ShadowFadeRange: float = ParamField(
        float32, "shadowFadeRange", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    MotionBlurBorderDist: float = ParamField(
        float32, "motionBlur_BorderDist", default=20.0,
        tooltip="TOOLTIP-TODO",
    )
    IsPointLightShadowSrc: int = ParamField(
        int8, "isPointLightShadowSrc", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDirLightShadowSrc: int = ParamField(
        int8, "isDirLightShadowSrc", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsShadowDst: int = ParamField(
        int8, "isShadowDst", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsShadowOnly: int = ParamField(
        int8, "isShadowOnly", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DrawByReflectCam: int = ParamField(
        int8, "drawByReflectCam", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DrawOnlyReflectCam: int = ParamField(
        int8, "drawOnlyReflectCam", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IncludeLodMapLv: int = ParamField(
        int8, "IncludeLodMapLv", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    IsNoFarClipDraw: int = ParamField(
        uint8, "isNoFarClipDraw", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LodType: int = ParamField(
        uint8, "lodType", PARTS_DRAW_LOD_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ShadowDrawLodOffset: int = ParamField(
        int8, "shadowDrawLodOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsTraceCameraXZ: int = ParamField(
        uint8, "isTraceCameraXZ", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSkydomeDrawPhase: int = ParamField(
        uint8, "isSkydomeDrawPhase", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DistantViewModelBorderDist: float = ParamField(
        float32, "DistantViewModel_BorderDist", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    DistantViewModelPlayDist: float = ParamField(
        float32, "DistantViewModel_PlayDist", default=5.0,
        tooltip="TOOLTIP-TODO",
    )
    LimtedActivateBorderDistforGrid: float = ParamField(
        float32, "LimtedActivate_BorderDist_forGrid", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    LimtedActivatePlayDistforGrid: float = ParamField(
        float32, "LimtedActivate_PlayDist_forGrid", default=10.0,
        tooltip="TOOLTIP-TODO",
    )
    ZSortOffsetForNoFarClipDraw: float = ParamField(
        float32, "zSortOffsetForNoFarClipDraw", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ShadowDrawAlphaTestDist: float = ParamField(
        float32, "shadowDrawAlphaTestDist", default=9999.0,
        tooltip="TOOLTIP-TODO",
    )
    FowardDrawEnvmapBlendType: int = ParamField(
        uint8, "fowardDrawEnvmapBlendType", PARTS_DRAW_FOWARD_DRAW_ENVMAP_BLEND_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    LBDrawDistScaleParamID: int = ParamField(
        uint8, "LBDrawDistScaleParamID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(34, "resereve[34]")
