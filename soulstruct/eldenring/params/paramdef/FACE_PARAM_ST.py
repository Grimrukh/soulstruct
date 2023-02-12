from __future__ import annotations

__all__ = ["FACE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class FACE_PARAM_ST(ParamRowData):
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
    HeadScale: int = ParamField(
        byte, "chrBodyScaleHead", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BreastScale: int = ParamField(
        byte, "chrBodyScaleBreast", default=128,
        tooltip="TOOLTIP-TODO",
    )
    AbdomenScale: int = ParamField(
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
    OverrideeyepartsId: int = ParamField(
        byte, "override_eye_partsId:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyeirisColor: int = ParamField(
        byte, "override_eye_irisColor:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Overrideeyecataract: int = ParamField(
        byte, "override_eye_cataract:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyecataractColor: int = ParamField(
        byte, "override_eye_cataractColor:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyescleraColor: int = ParamField(
        byte, "override_eye_scleraColor:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Overrideburnscar: int = ParamField(
        byte, "override_burn_scar:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad2:2")
    _Pad1: bytes = ParamPad(5, "pad[5]")
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
    GeometryData00: int = ParamField(
        byte, "faceGeoData00", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData01: int = ParamField(
        byte, "faceGeoData01", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData02: int = ParamField(
        byte, "faceGeoData02", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData03: int = ParamField(
        byte, "faceGeoData03", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData04: int = ParamField(
        byte, "faceGeoData04", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData05: int = ParamField(
        byte, "faceGeoData05", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData06: int = ParamField(
        byte, "faceGeoData06", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData07: int = ParamField(
        byte, "faceGeoData07", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData08: int = ParamField(
        byte, "faceGeoData08", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData09: int = ParamField(
        byte, "faceGeoData09", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData10: int = ParamField(
        byte, "faceGeoData10", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData11: int = ParamField(
        byte, "faceGeoData11", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData12: int = ParamField(
        byte, "faceGeoData12", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData13: int = ParamField(
        byte, "faceGeoData13", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData14: int = ParamField(
        byte, "faceGeoData14", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData15: int = ParamField(
        byte, "faceGeoData15", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData16: int = ParamField(
        byte, "faceGeoData16", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData17: int = ParamField(
        byte, "faceGeoData17", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData18: int = ParamField(
        byte, "faceGeoData18", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData19: int = ParamField(
        byte, "faceGeoData19", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData20: int = ParamField(
        byte, "faceGeoData20", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData21: int = ParamField(
        byte, "faceGeoData21", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData22: int = ParamField(
        byte, "faceGeoData22", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData23: int = ParamField(
        byte, "faceGeoData23", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData24: int = ParamField(
        byte, "faceGeoData24", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData25: int = ParamField(
        byte, "faceGeoData25", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData26: int = ParamField(
        byte, "faceGeoData26", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData27: int = ParamField(
        byte, "faceGeoData27", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData28: int = ParamField(
        byte, "faceGeoData28", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData29: int = ParamField(
        byte, "faceGeoData29", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData30: int = ParamField(
        byte, "faceGeoData30", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData31: int = ParamField(
        byte, "faceGeoData31", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData32: int = ParamField(
        byte, "faceGeoData32", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData33: int = ParamField(
        byte, "faceGeoData33", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData34: int = ParamField(
        byte, "faceGeoData34", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData35: int = ParamField(
        byte, "faceGeoData35", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData36: int = ParamField(
        byte, "faceGeoData36", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData37: int = ParamField(
        byte, "faceGeoData37", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData38: int = ParamField(
        byte, "faceGeoData38", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData39: int = ParamField(
        byte, "faceGeoData39", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData40: int = ParamField(
        byte, "faceGeoData40", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData41: int = ParamField(
        byte, "faceGeoData41", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData42: int = ParamField(
        byte, "faceGeoData42", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData43: int = ParamField(
        byte, "faceGeoData43", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData44: int = ParamField(
        byte, "faceGeoData44", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData45: int = ParamField(
        byte, "faceGeoData45", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData46: int = ParamField(
        byte, "faceGeoData46", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData47: int = ParamField(
        byte, "faceGeoData47", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData48: int = ParamField(
        byte, "faceGeoData48", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData49: int = ParamField(
        byte, "faceGeoData49", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData50: int = ParamField(
        byte, "faceGeoData50", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData51: int = ParamField(
        byte, "faceGeoData51", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData52: int = ParamField(
        byte, "faceGeoData52", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData53: int = ParamField(
        byte, "faceGeoData53", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData54: int = ParamField(
        byte, "faceGeoData54", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData55: int = ParamField(
        byte, "faceGeoData55", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData56: int = ParamField(
        byte, "faceGeoData56", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData57: int = ParamField(
        byte, "faceGeoData57", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData58: int = ParamField(
        byte, "faceGeoData58", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData59: int = ParamField(
        byte, "faceGeoData59", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeometryData60: int = ParamField(
        byte, "faceGeoData60", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData00: int = ParamField(
        byte, "faceTexData00", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData01: int = ParamField(
        byte, "faceTexData01", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData02: int = ParamField(
        byte, "faceTexData02", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData03: int = ParamField(
        byte, "faceTexData03", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData04: int = ParamField(
        byte, "faceTexData04", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData05: int = ParamField(
        byte, "faceTexData05", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData06: int = ParamField(
        byte, "faceTexData06", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData07: int = ParamField(
        byte, "faceTexData07", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData08: int = ParamField(
        byte, "faceTexData08", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData09: int = ParamField(
        byte, "faceTexData09", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData10: int = ParamField(
        byte, "faceTexData10", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData11: int = ParamField(
        byte, "faceTexData11", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData12: int = ParamField(
        byte, "faceTexData12", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData13: int = ParamField(
        byte, "faceTexData13", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData14: int = ParamField(
        byte, "faceTexData14", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData15: int = ParamField(
        byte, "faceTexData15", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData16: int = ParamField(
        byte, "faceTexData16", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData17: int = ParamField(
        byte, "faceTexData17", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData18: int = ParamField(
        byte, "faceTexData18", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData19: int = ParamField(
        byte, "faceTexData19", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData20: int = ParamField(
        byte, "faceTexData20", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData21: int = ParamField(
        byte, "faceTexData21", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData22: int = ParamField(
        byte, "faceTexData22", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData23: int = ParamField(
        byte, "faceTexData23", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData24: int = ParamField(
        byte, "faceTexData24", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData25: int = ParamField(
        byte, "faceTexData25", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData26: int = ParamField(
        byte, "faceTexData26", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData27: int = ParamField(
        byte, "faceTexData27", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData28: int = ParamField(
        byte, "faceTexData28", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData29: int = ParamField(
        byte, "faceTexData29", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData30: int = ParamField(
        byte, "faceTexData30", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData31: int = ParamField(
        byte, "faceTexData31", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData32: int = ParamField(
        byte, "faceTexData32", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData33: int = ParamField(
        byte, "faceTexData33", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData34: int = ParamField(
        byte, "faceTexData34", default=128,
        tooltip="TOOLTIP-TODO",
    )
    TextureData35: int = ParamField(
        byte, "faceTexData35", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData00: int = ParamField(
        byte, "faceGeoAsymData00", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData01: int = ParamField(
        byte, "faceGeoAsymData01", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData02: int = ParamField(
        byte, "faceGeoAsymData02", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData03: int = ParamField(
        byte, "faceGeoAsymData03", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData04: int = ParamField(
        byte, "faceGeoAsymData04", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData05: int = ParamField(
        byte, "faceGeoAsymData05", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData06: int = ParamField(
        byte, "faceGeoAsymData06", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData07: int = ParamField(
        byte, "faceGeoAsymData07", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData08: int = ParamField(
        byte, "faceGeoAsymData08", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData09: int = ParamField(
        byte, "faceGeoAsymData09", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData10: int = ParamField(
        byte, "faceGeoAsymData10", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData11: int = ParamField(
        byte, "faceGeoAsymData11", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData12: int = ParamField(
        byte, "faceGeoAsymData12", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData13: int = ParamField(
        byte, "faceGeoAsymData13", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData14: int = ParamField(
        byte, "faceGeoAsymData14", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData15: int = ParamField(
        byte, "faceGeoAsymData15", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData16: int = ParamField(
        byte, "faceGeoAsymData16", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData17: int = ParamField(
        byte, "faceGeoAsymData17", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData18: int = ParamField(
        byte, "faceGeoAsymData18", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData19: int = ParamField(
        byte, "faceGeoAsymData19", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData20: int = ParamField(
        byte, "faceGeoAsymData20", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData21: int = ParamField(
        byte, "faceGeoAsymData21", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData22: int = ParamField(
        byte, "faceGeoAsymData22", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData23: int = ParamField(
        byte, "faceGeoAsymData23", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData24: int = ParamField(
        byte, "faceGeoAsymData24", default=128,
        tooltip="TOOLTIP-TODO",
    )
    GeoAsymData25: int = ParamField(
        byte, "faceGeoAsymData25", default=128,
        tooltip="TOOLTIP-TODO",
    )
