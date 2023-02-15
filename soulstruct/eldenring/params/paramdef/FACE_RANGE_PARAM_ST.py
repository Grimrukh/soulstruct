from __future__ import annotations

__all__ = ["FACE_RANGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class FACE_RANGE_PARAM_ST(ParamRow):
    FacepartsId: float = ParamField(
        float, "face_partsId", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SkincolorR: float = ParamField(
        float, "skin_color_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SkincolorG: float = ParamField(
        float, "skin_color_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SkincolorB: float = ParamField(
        float, "skin_color_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Skingloss: float = ParamField(
        float, "skin_gloss", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Skinpores: float = ParamField(
        float, "skin_pores", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Facebeard: float = ParamField(
        float, "face_beard", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEye: float = ParamField(
        float, "face_aroundEye", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEyeColorR: float = ParamField(
        float, "face_aroundEyeColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEyeColorG: float = ParamField(
        float, "face_aroundEyeColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEyeColorB: float = ParamField(
        float, "face_aroundEyeColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Facecheek: float = ParamField(
        float, "face_cheek", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacecheekColorR: float = ParamField(
        float, "face_cheekColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacecheekColorG: float = ParamField(
        float, "face_cheekColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacecheekColorB: float = ParamField(
        float, "face_cheekColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLine: float = ParamField(
        float, "face_eyeLine", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLineColorR: float = ParamField(
        float, "face_eyeLineColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLineColorG: float = ParamField(
        float, "face_eyeLineColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLineColorB: float = ParamField(
        float, "face_eyeLineColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDown: float = ParamField(
        float, "face_eyeShadowDown", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDownColorR: float = ParamField(
        float, "face_eyeShadowDownColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDownColorG: float = ParamField(
        float, "face_eyeShadowDownColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDownColorB: float = ParamField(
        float, "face_eyeShadowDownColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUp: float = ParamField(
        float, "face_eyeShadowUp", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUpColorR: float = ParamField(
        float, "face_eyeShadowUpColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUpColorG: float = ParamField(
        float, "face_eyeShadowUpColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUpColorB: float = ParamField(
        float, "face_eyeShadowUpColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Facelip: float = ParamField(
        float, "face_lip", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacelipColorR: float = ParamField(
        float, "face_lipColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacelipColorG: float = ParamField(
        float, "face_lipColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FacelipColorB: float = ParamField(
        float, "face_lipColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Bodyhair: float = ParamField(
        float, "body_hair", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BodyhairColorR: float = ParamField(
        float, "body_hairColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BodyhairColorG: float = ParamField(
        float, "body_hairColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BodyhairColorB: float = ParamField(
        float, "body_hairColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyepartsId: float = ParamField(
        float, "eye_partsId", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisColorR: float = ParamField(
        float, "eyeR_irisColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisColorG: float = ParamField(
        float, "eyeR_irisColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisColorB: float = ParamField(
        float, "eyeR_irisColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisScale: float = ParamField(
        float, "eyeR_irisScale", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataract: float = ParamField(
        float, "eyeR_cataract", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataractColorR: float = ParamField(
        float, "eyeR_cataractColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataractColorG: float = ParamField(
        float, "eyeR_cataractColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataractColorB: float = ParamField(
        float, "eyeR_cataractColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRscleraColorR: float = ParamField(
        float, "eyeR_scleraColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRscleraColorG: float = ParamField(
        float, "eyeR_scleraColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRscleraColorB: float = ParamField(
        float, "eyeR_scleraColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisDistance: float = ParamField(
        float, "eyeR_irisDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisColorR: float = ParamField(
        float, "eyeL_irisColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisColorG: float = ParamField(
        float, "eyeL_irisColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisColorB: float = ParamField(
        float, "eyeL_irisColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisScale: float = ParamField(
        float, "eyeL_irisScale", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataract: float = ParamField(
        float, "eyeL_cataract", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataractColorR: float = ParamField(
        float, "eyeL_cataractColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataractColorG: float = ParamField(
        float, "eyeL_cataractColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataractColorB: float = ParamField(
        float, "eyeL_cataractColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLscleraColorR: float = ParamField(
        float, "eyeL_scleraColor_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLscleraColorG: float = ParamField(
        float, "eyeL_scleraColor_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLscleraColorB: float = ParamField(
        float, "eyeL_scleraColor_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisDistance: float = ParamField(
        float, "eyeL_irisDistance", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HairpartsId: float = ParamField(
        float, "hair_partsId", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HaircolorR: float = ParamField(
        float, "hair_color_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HaircolorG: float = ParamField(
        float, "hair_color_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HaircolorB: float = ParamField(
        float, "hair_color_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hairshininess: float = ParamField(
        float, "hair_shininess", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HairrootBlack: float = ParamField(
        float, "hair_rootBlack", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HairwhiteDensity: float = ParamField(
        float, "hair_whiteDensity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BeardpartsId: float = ParamField(
        float, "beard_partsId", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BeardcolorR: float = ParamField(
        float, "beard_color_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BeardcolorG: float = ParamField(
        float, "beard_color_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BeardcolorB: float = ParamField(
        float, "beard_color_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Beardshininess: float = ParamField(
        float, "beard_shininess", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BeardrootBlack: float = ParamField(
        float, "beard_rootBlack", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BeardwhiteDensity: float = ParamField(
        float, "beard_whiteDensity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowpartsId: float = ParamField(
        float, "eyebrow_partsId", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowcolorR: float = ParamField(
        float, "eyebrow_color_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowcolorG: float = ParamField(
        float, "eyebrow_color_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowcolorB: float = ParamField(
        float, "eyebrow_color_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Eyebrowshininess: float = ParamField(
        float, "eyebrow_shininess", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowrootBlack: float = ParamField(
        float, "eyebrow_rootBlack", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowwhiteDensity: float = ParamField(
        float, "eyebrow_whiteDensity", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyelashpartsId: float = ParamField(
        float, "eyelash_partsId", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyelashcolorR: float = ParamField(
        float, "eyelash_color_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyelashcolorG: float = ParamField(
        float, "eyelash_color_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    EyelashcolorB: float = ParamField(
        float, "eyelash_color_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriespartsId: float = ParamField(
        float, "accessories_partsId", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriescolorR: float = ParamField(
        float, "accessories_color_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriescolorG: float = ParamField(
        float, "accessories_color_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriescolorB: float = ParamField(
        float, "accessories_color_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DecalpartsId: float = ParamField(
        float, "decal_partsId", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DecalposX: float = ParamField(
        float, "decal_posX", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DecalposY: float = ParamField(
        float, "decal_posY", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Decalangle: float = ParamField(
        float, "decal_angle", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Decalscale: float = ParamField(
        float, "decal_scale", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DecalcolorR: float = ParamField(
        float, "decal_color_R", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DecalcolorG: float = ParamField(
        float, "decal_color_G", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DecalcolorB: float = ParamField(
        float, "decal_color_B", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Decalgloss: float = ParamField(
        float, "decal_gloss", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Decalmirror: float = ParamField(
        float, "decal_mirror", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleHead: float = ParamField(
        float, "chrBodyScaleHead", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleBreast: float = ParamField(
        float, "chrBodyScaleBreast", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleAbdomen: float = ParamField(
        float, "chrBodyScaleAbdomen", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleArm: float = ParamField(
        float, "chrBodyScaleArm", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleLeg: float = ParamField(
        float, "chrBodyScaleLeg", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Age: float = ParamField(
        float, "age", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Gender: float = ParamField(
        float, "gender", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CaricatureGeometry: float = ParamField(
        float, "caricatureGeometry", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    CaricatureTexture: float = ParamField(
        float, "caricatureTexture", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData00: float = ParamField(
        float, "faceGeoData00", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData01: float = ParamField(
        float, "faceGeoData01", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData02: float = ParamField(
        float, "faceGeoData02", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData03: float = ParamField(
        float, "faceGeoData03", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData04: float = ParamField(
        float, "faceGeoData04", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData05: float = ParamField(
        float, "faceGeoData05", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData06: float = ParamField(
        float, "faceGeoData06", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData07: float = ParamField(
        float, "faceGeoData07", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData08: float = ParamField(
        float, "faceGeoData08", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData09: float = ParamField(
        float, "faceGeoData09", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData10: float = ParamField(
        float, "faceGeoData10", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData11: float = ParamField(
        float, "faceGeoData11", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData12: float = ParamField(
        float, "faceGeoData12", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData13: float = ParamField(
        float, "faceGeoData13", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData14: float = ParamField(
        float, "faceGeoData14", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData15: float = ParamField(
        float, "faceGeoData15", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData16: float = ParamField(
        float, "faceGeoData16", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData17: float = ParamField(
        float, "faceGeoData17", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData18: float = ParamField(
        float, "faceGeoData18", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData19: float = ParamField(
        float, "faceGeoData19", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData20: float = ParamField(
        float, "faceGeoData20", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData21: float = ParamField(
        float, "faceGeoData21", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData22: float = ParamField(
        float, "faceGeoData22", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData23: float = ParamField(
        float, "faceGeoData23", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData24: float = ParamField(
        float, "faceGeoData24", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData25: float = ParamField(
        float, "faceGeoData25", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData26: float = ParamField(
        float, "faceGeoData26", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData27: float = ParamField(
        float, "faceGeoData27", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData28: float = ParamField(
        float, "faceGeoData28", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData29: float = ParamField(
        float, "faceGeoData29", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData30: float = ParamField(
        float, "faceGeoData30", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData31: float = ParamField(
        float, "faceGeoData31", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData32: float = ParamField(
        float, "faceGeoData32", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData33: float = ParamField(
        float, "faceGeoData33", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData34: float = ParamField(
        float, "faceGeoData34", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData35: float = ParamField(
        float, "faceGeoData35", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData36: float = ParamField(
        float, "faceGeoData36", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData37: float = ParamField(
        float, "faceGeoData37", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData38: float = ParamField(
        float, "faceGeoData38", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData39: float = ParamField(
        float, "faceGeoData39", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData40: float = ParamField(
        float, "faceGeoData40", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData41: float = ParamField(
        float, "faceGeoData41", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData42: float = ParamField(
        float, "faceGeoData42", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData43: float = ParamField(
        float, "faceGeoData43", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData44: float = ParamField(
        float, "faceGeoData44", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData45: float = ParamField(
        float, "faceGeoData45", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData46: float = ParamField(
        float, "faceGeoData46", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData47: float = ParamField(
        float, "faceGeoData47", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData48: float = ParamField(
        float, "faceGeoData48", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData49: float = ParamField(
        float, "faceGeoData49", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData50: float = ParamField(
        float, "faceGeoData50", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData51: float = ParamField(
        float, "faceGeoData51", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData52: float = ParamField(
        float, "faceGeoData52", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData53: float = ParamField(
        float, "faceGeoData53", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData54: float = ParamField(
        float, "faceGeoData54", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData55: float = ParamField(
        float, "faceGeoData55", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData56: float = ParamField(
        float, "faceGeoData56", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData57: float = ParamField(
        float, "faceGeoData57", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData58: float = ParamField(
        float, "faceGeoData58", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData59: float = ParamField(
        float, "faceGeoData59", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData60: float = ParamField(
        float, "faceGeoData60", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData00: float = ParamField(
        float, "faceTexData00", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData01: float = ParamField(
        float, "faceTexData01", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData02: float = ParamField(
        float, "faceTexData02", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData03: float = ParamField(
        float, "faceTexData03", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData04: float = ParamField(
        float, "faceTexData04", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData05: float = ParamField(
        float, "faceTexData05", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData06: float = ParamField(
        float, "faceTexData06", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData07: float = ParamField(
        float, "faceTexData07", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData08: float = ParamField(
        float, "faceTexData08", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData09: float = ParamField(
        float, "faceTexData09", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData10: float = ParamField(
        float, "faceTexData10", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData11: float = ParamField(
        float, "faceTexData11", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData12: float = ParamField(
        float, "faceTexData12", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData13: float = ParamField(
        float, "faceTexData13", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData14: float = ParamField(
        float, "faceTexData14", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData15: float = ParamField(
        float, "faceTexData15", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData16: float = ParamField(
        float, "faceTexData16", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData17: float = ParamField(
        float, "faceTexData17", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData18: float = ParamField(
        float, "faceTexData18", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData19: float = ParamField(
        float, "faceTexData19", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData20: float = ParamField(
        float, "faceTexData20", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData21: float = ParamField(
        float, "faceTexData21", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData22: float = ParamField(
        float, "faceTexData22", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData23: float = ParamField(
        float, "faceTexData23", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData24: float = ParamField(
        float, "faceTexData24", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData25: float = ParamField(
        float, "faceTexData25", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData26: float = ParamField(
        float, "faceTexData26", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData27: float = ParamField(
        float, "faceTexData27", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData28: float = ParamField(
        float, "faceTexData28", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData29: float = ParamField(
        float, "faceTexData29", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData30: float = ParamField(
        float, "faceTexData30", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData31: float = ParamField(
        float, "faceTexData31", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData32: float = ParamField(
        float, "faceTexData32", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData33: float = ParamField(
        float, "faceTexData33", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData34: float = ParamField(
        float, "faceTexData34", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData35: float = ParamField(
        float, "faceTexData35", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Burnscar: float = ParamField(
        float, "burn_scar", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
