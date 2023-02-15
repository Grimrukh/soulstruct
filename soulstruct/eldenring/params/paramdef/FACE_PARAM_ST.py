from __future__ import annotations

__all__ = ["FACE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class FACE_PARAM_ST(ParamRow):
    FacepartsId: int = ParamField(
        byte, "face_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SkincolorR: int = ParamField(
        byte, "skin_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    SkincolorG: int = ParamField(
        byte, "skin_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    SkincolorB: int = ParamField(
        byte, "skin_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Skingloss: int = ParamField(
        byte, "skin_gloss", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Skinpores: int = ParamField(
        byte, "skin_pores", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Facebeard: int = ParamField(
        byte, "face_beard", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEye: int = ParamField(
        byte, "face_aroundEye", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEyeColorR: int = ParamField(
        byte, "face_aroundEyeColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEyeColorG: int = ParamField(
        byte, "face_aroundEyeColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEyeColorB: int = ParamField(
        byte, "face_aroundEyeColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Facecheek: int = ParamField(
        byte, "face_cheek", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacecheekColorR: int = ParamField(
        byte, "face_cheekColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacecheekColorG: int = ParamField(
        byte, "face_cheekColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacecheekColorB: int = ParamField(
        byte, "face_cheekColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLine: int = ParamField(
        byte, "face_eyeLine", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLineColorR: int = ParamField(
        byte, "face_eyeLineColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLineColorG: int = ParamField(
        byte, "face_eyeLineColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLineColorB: int = ParamField(
        byte, "face_eyeLineColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDown: int = ParamField(
        byte, "face_eyeShadowDown", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDownColorR: int = ParamField(
        byte, "face_eyeShadowDownColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDownColorG: int = ParamField(
        byte, "face_eyeShadowDownColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDownColorB: int = ParamField(
        byte, "face_eyeShadowDownColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUp: int = ParamField(
        byte, "face_eyeShadowUp", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUpColorR: int = ParamField(
        byte, "face_eyeShadowUpColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUpColorG: int = ParamField(
        byte, "face_eyeShadowUpColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUpColorB: int = ParamField(
        byte, "face_eyeShadowUpColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Facelip: int = ParamField(
        byte, "face_lip", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacelipColorR: int = ParamField(
        byte, "face_lipColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacelipColorG: int = ParamField(
        byte, "face_lipColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacelipColorB: int = ParamField(
        byte, "face_lipColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Bodyhair: int = ParamField(
        byte, "body_hair", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BodyhairColorR: int = ParamField(
        byte, "body_hairColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BodyhairColorG: int = ParamField(
        byte, "body_hairColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BodyhairColorB: int = ParamField(
        byte, "body_hairColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyepartsId: int = ParamField(
        byte, "eye_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisColorR: int = ParamField(
        byte, "eyeR_irisColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisColorG: int = ParamField(
        byte, "eyeR_irisColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisColorB: int = ParamField(
        byte, "eyeR_irisColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisScale: int = ParamField(
        byte, "eyeR_irisScale", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataract: int = ParamField(
        byte, "eyeR_cataract", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataractColorR: int = ParamField(
        byte, "eyeR_cataractColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataractColorG: int = ParamField(
        byte, "eyeR_cataractColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataractColorB: int = ParamField(
        byte, "eyeR_cataractColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRscleraColorR: int = ParamField(
        byte, "eyeR_scleraColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRscleraColorG: int = ParamField(
        byte, "eyeR_scleraColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRscleraColorB: int = ParamField(
        byte, "eyeR_scleraColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisDistance: int = ParamField(
        byte, "eyeR_irisDistance", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisColorR: int = ParamField(
        byte, "eyeL_irisColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisColorG: int = ParamField(
        byte, "eyeL_irisColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisColorB: int = ParamField(
        byte, "eyeL_irisColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisScale: int = ParamField(
        byte, "eyeL_irisScale", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataract: int = ParamField(
        byte, "eyeL_cataract", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataractColorR: int = ParamField(
        byte, "eyeL_cataractColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataractColorG: int = ParamField(
        byte, "eyeL_cataractColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataractColorB: int = ParamField(
        byte, "eyeL_cataractColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLscleraColorR: int = ParamField(
        byte, "eyeL_scleraColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLscleraColorG: int = ParamField(
        byte, "eyeL_scleraColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLscleraColorB: int = ParamField(
        byte, "eyeL_scleraColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisDistance: int = ParamField(
        byte, "eyeL_irisDistance", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HairpartsId: int = ParamField(
        byte, "hair_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HaircolorR: int = ParamField(
        byte, "hair_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HaircolorG: int = ParamField(
        byte, "hair_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HaircolorB: int = ParamField(
        byte, "hair_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Hairshininess: int = ParamField(
        byte, "hair_shininess", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HairrootBlack: int = ParamField(
        byte, "hair_rootBlack", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HairwhiteDensity: int = ParamField(
        byte, "hair_whiteDensity", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardpartsId: int = ParamField(
        byte, "beard_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BeardcolorR: int = ParamField(
        byte, "beard_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardcolorG: int = ParamField(
        byte, "beard_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardcolorB: int = ParamField(
        byte, "beard_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Beardshininess: int = ParamField(
        byte, "beard_shininess", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardrootBlack: int = ParamField(
        byte, "beard_rootBlack", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardwhiteDensity: int = ParamField(
        byte, "beard_whiteDensity", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowpartsId: int = ParamField(
        byte, "eyebrow_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowcolorR: int = ParamField(
        byte, "eyebrow_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowcolorG: int = ParamField(
        byte, "eyebrow_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowcolorB: int = ParamField(
        byte, "eyebrow_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Eyebrowshininess: int = ParamField(
        byte, "eyebrow_shininess", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowrootBlack: int = ParamField(
        byte, "eyebrow_rootBlack", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowwhiteDensity: int = ParamField(
        byte, "eyebrow_whiteDensity", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyelashpartsId: int = ParamField(
        byte, "eyelash_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyelashcolorR: int = ParamField(
        byte, "eyelash_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyelashcolorG: int = ParamField(
        byte, "eyelash_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyelashcolorB: int = ParamField(
        byte, "eyelash_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriespartsId: int = ParamField(
        byte, "accessories_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriescolorR: int = ParamField(
        byte, "accessories_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriescolorG: int = ParamField(
        byte, "accessories_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriescolorB: int = ParamField(
        byte, "accessories_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    DecalpartsId: int = ParamField(
        byte, "decal_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DecalposX: int = ParamField(
        byte, "decal_posX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DecalposY: int = ParamField(
        byte, "decal_posY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Decalangle: int = ParamField(
        byte, "decal_angle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Decalscale: int = ParamField(
        byte, "decal_scale", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DecalcolorR: int = ParamField(
        byte, "decal_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    DecalcolorG: int = ParamField(
        byte, "decal_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    DecalcolorB: int = ParamField(
        byte, "decal_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Decalgloss: int = ParamField(
        byte, "decal_gloss", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Decalmirror: int = ParamField(
        byte, "decal_mirror", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleHead: int = ParamField(
        byte, "chrBodyScaleHead", default=128,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleBreast: int = ParamField(
        byte, "chrBodyScaleBreast", default=128,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleAbdomen: int = ParamField(
        byte, "chrBodyScaleAbdomen", default=128,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleRArm: int = ParamField(
        byte, "chrBodyScaleRArm", default=128,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleRLeg: int = ParamField(
        byte, "chrBodyScaleRLeg", default=128,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleLArm: int = ParamField(
        byte, "chrBodyScaleLArm", default=128,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleLLeg: int = ParamField(
        byte, "chrBodyScaleLLeg", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Burnscar: int = ParamField(
        byte, "burn_scar", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyepartsId: bool = ParamField(
        byte, "override_eye_partsId:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyeirisColor: bool = ParamField(
        byte, "override_eye_irisColor:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Overrideeyecataract: bool = ParamField(
        byte, "override_eye_cataract:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyecataractColor: bool = ParamField(
        byte, "override_eye_cataractColor:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyescleraColor: bool = ParamField(
        byte, "override_eye_scleraColor:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Overrideburnscar: bool = ParamField(
        byte, "override_burn_scar:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad2:2", bit_count=2)
    _Pad0: bytes = ParamPad(5, "pad[5]")
    Age: int = ParamField(
        byte, "age", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Gender: int = ParamField(
        byte, "gender", default=128,
        tooltip="TOOLTIP-TODO",
    )
    CaricatureGeometry: int = ParamField(
        byte, "caricatureGeometry", default=128,
        tooltip="TOOLTIP-TODO",
    )
    CaricatureTexture: int = ParamField(
        byte, "caricatureTexture", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData00: int = ParamField(
        byte, "faceGeoData00", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData01: int = ParamField(
        byte, "faceGeoData01", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData02: int = ParamField(
        byte, "faceGeoData02", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData03: int = ParamField(
        byte, "faceGeoData03", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData04: int = ParamField(
        byte, "faceGeoData04", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData05: int = ParamField(
        byte, "faceGeoData05", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData06: int = ParamField(
        byte, "faceGeoData06", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData07: int = ParamField(
        byte, "faceGeoData07", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData08: int = ParamField(
        byte, "faceGeoData08", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData09: int = ParamField(
        byte, "faceGeoData09", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData10: int = ParamField(
        byte, "faceGeoData10", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData11: int = ParamField(
        byte, "faceGeoData11", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData12: int = ParamField(
        byte, "faceGeoData12", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData13: int = ParamField(
        byte, "faceGeoData13", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData14: int = ParamField(
        byte, "faceGeoData14", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData15: int = ParamField(
        byte, "faceGeoData15", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData16: int = ParamField(
        byte, "faceGeoData16", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData17: int = ParamField(
        byte, "faceGeoData17", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData18: int = ParamField(
        byte, "faceGeoData18", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData19: int = ParamField(
        byte, "faceGeoData19", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData20: int = ParamField(
        byte, "faceGeoData20", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData21: int = ParamField(
        byte, "faceGeoData21", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData22: int = ParamField(
        byte, "faceGeoData22", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData23: int = ParamField(
        byte, "faceGeoData23", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData24: int = ParamField(
        byte, "faceGeoData24", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData25: int = ParamField(
        byte, "faceGeoData25", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData26: int = ParamField(
        byte, "faceGeoData26", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData27: int = ParamField(
        byte, "faceGeoData27", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData28: int = ParamField(
        byte, "faceGeoData28", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData29: int = ParamField(
        byte, "faceGeoData29", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData30: int = ParamField(
        byte, "faceGeoData30", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData31: int = ParamField(
        byte, "faceGeoData31", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData32: int = ParamField(
        byte, "faceGeoData32", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData33: int = ParamField(
        byte, "faceGeoData33", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData34: int = ParamField(
        byte, "faceGeoData34", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData35: int = ParamField(
        byte, "faceGeoData35", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData36: int = ParamField(
        byte, "faceGeoData36", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData37: int = ParamField(
        byte, "faceGeoData37", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData38: int = ParamField(
        byte, "faceGeoData38", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData39: int = ParamField(
        byte, "faceGeoData39", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData40: int = ParamField(
        byte, "faceGeoData40", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData41: int = ParamField(
        byte, "faceGeoData41", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData42: int = ParamField(
        byte, "faceGeoData42", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData43: int = ParamField(
        byte, "faceGeoData43", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData44: int = ParamField(
        byte, "faceGeoData44", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData45: int = ParamField(
        byte, "faceGeoData45", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData46: int = ParamField(
        byte, "faceGeoData46", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData47: int = ParamField(
        byte, "faceGeoData47", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData48: int = ParamField(
        byte, "faceGeoData48", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData49: int = ParamField(
        byte, "faceGeoData49", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData50: int = ParamField(
        byte, "faceGeoData50", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData51: int = ParamField(
        byte, "faceGeoData51", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData52: int = ParamField(
        byte, "faceGeoData52", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData53: int = ParamField(
        byte, "faceGeoData53", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData54: int = ParamField(
        byte, "faceGeoData54", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData55: int = ParamField(
        byte, "faceGeoData55", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData56: int = ParamField(
        byte, "faceGeoData56", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData57: int = ParamField(
        byte, "faceGeoData57", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData58: int = ParamField(
        byte, "faceGeoData58", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData59: int = ParamField(
        byte, "faceGeoData59", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoData60: int = ParamField(
        byte, "faceGeoData60", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData00: int = ParamField(
        byte, "faceTexData00", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData01: int = ParamField(
        byte, "faceTexData01", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData02: int = ParamField(
        byte, "faceTexData02", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData03: int = ParamField(
        byte, "faceTexData03", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData04: int = ParamField(
        byte, "faceTexData04", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData05: int = ParamField(
        byte, "faceTexData05", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData06: int = ParamField(
        byte, "faceTexData06", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData07: int = ParamField(
        byte, "faceTexData07", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData08: int = ParamField(
        byte, "faceTexData08", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData09: int = ParamField(
        byte, "faceTexData09", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData10: int = ParamField(
        byte, "faceTexData10", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData11: int = ParamField(
        byte, "faceTexData11", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData12: int = ParamField(
        byte, "faceTexData12", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData13: int = ParamField(
        byte, "faceTexData13", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData14: int = ParamField(
        byte, "faceTexData14", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData15: int = ParamField(
        byte, "faceTexData15", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData16: int = ParamField(
        byte, "faceTexData16", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData17: int = ParamField(
        byte, "faceTexData17", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData18: int = ParamField(
        byte, "faceTexData18", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData19: int = ParamField(
        byte, "faceTexData19", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData20: int = ParamField(
        byte, "faceTexData20", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData21: int = ParamField(
        byte, "faceTexData21", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData22: int = ParamField(
        byte, "faceTexData22", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData23: int = ParamField(
        byte, "faceTexData23", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData24: int = ParamField(
        byte, "faceTexData24", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData25: int = ParamField(
        byte, "faceTexData25", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData26: int = ParamField(
        byte, "faceTexData26", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData27: int = ParamField(
        byte, "faceTexData27", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData28: int = ParamField(
        byte, "faceTexData28", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData29: int = ParamField(
        byte, "faceTexData29", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData30: int = ParamField(
        byte, "faceTexData30", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData31: int = ParamField(
        byte, "faceTexData31", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData32: int = ParamField(
        byte, "faceTexData32", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData33: int = ParamField(
        byte, "faceTexData33", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData34: int = ParamField(
        byte, "faceTexData34", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceTexData35: int = ParamField(
        byte, "faceTexData35", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData00: int = ParamField(
        byte, "faceGeoAsymData00", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData01: int = ParamField(
        byte, "faceGeoAsymData01", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData02: int = ParamField(
        byte, "faceGeoAsymData02", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData03: int = ParamField(
        byte, "faceGeoAsymData03", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData04: int = ParamField(
        byte, "faceGeoAsymData04", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData05: int = ParamField(
        byte, "faceGeoAsymData05", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData06: int = ParamField(
        byte, "faceGeoAsymData06", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData07: int = ParamField(
        byte, "faceGeoAsymData07", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData08: int = ParamField(
        byte, "faceGeoAsymData08", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData09: int = ParamField(
        byte, "faceGeoAsymData09", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData10: int = ParamField(
        byte, "faceGeoAsymData10", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData11: int = ParamField(
        byte, "faceGeoAsymData11", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData12: int = ParamField(
        byte, "faceGeoAsymData12", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData13: int = ParamField(
        byte, "faceGeoAsymData13", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData14: int = ParamField(
        byte, "faceGeoAsymData14", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData15: int = ParamField(
        byte, "faceGeoAsymData15", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData16: int = ParamField(
        byte, "faceGeoAsymData16", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData17: int = ParamField(
        byte, "faceGeoAsymData17", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData18: int = ParamField(
        byte, "faceGeoAsymData18", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData19: int = ParamField(
        byte, "faceGeoAsymData19", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData20: int = ParamField(
        byte, "faceGeoAsymData20", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData21: int = ParamField(
        byte, "faceGeoAsymData21", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData22: int = ParamField(
        byte, "faceGeoAsymData22", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData23: int = ParamField(
        byte, "faceGeoAsymData23", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData24: int = ParamField(
        byte, "faceGeoAsymData24", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceGeoAsymData25: int = ParamField(
        byte, "faceGeoAsymData25", default=128,
        tooltip="TOOLTIP-TODO",
    )
