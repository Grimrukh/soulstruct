from __future__ import annotations

__all__ = ["FACE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class FACE_PARAM_ST(ParamRow):
    FacepartsId: int = ParamField(
        uint8, "face_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SkincolorR: int = ParamField(
        uint8, "skin_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    SkincolorG: int = ParamField(
        uint8, "skin_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    SkincolorB: int = ParamField(
        uint8, "skin_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Skingloss: int = ParamField(
        uint8, "skin_gloss", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Skinpores: int = ParamField(
        uint8, "skin_pores", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Facebeard: int = ParamField(
        uint8, "face_beard", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEye: int = ParamField(
        uint8, "face_aroundEye", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEyeColorR: int = ParamField(
        uint8, "face_aroundEyeColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEyeColorG: int = ParamField(
        uint8, "face_aroundEyeColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacearoundEyeColorB: int = ParamField(
        uint8, "face_aroundEyeColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Facecheek: int = ParamField(
        uint8, "face_cheek", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacecheekColorR: int = ParamField(
        uint8, "face_cheekColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacecheekColorG: int = ParamField(
        uint8, "face_cheekColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacecheekColorB: int = ParamField(
        uint8, "face_cheekColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLine: int = ParamField(
        uint8, "face_eyeLine", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLineColorR: int = ParamField(
        uint8, "face_eyeLineColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLineColorG: int = ParamField(
        uint8, "face_eyeLineColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeLineColorB: int = ParamField(
        uint8, "face_eyeLineColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDown: int = ParamField(
        uint8, "face_eyeShadowDown", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDownColorR: int = ParamField(
        uint8, "face_eyeShadowDownColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDownColorG: int = ParamField(
        uint8, "face_eyeShadowDownColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowDownColorB: int = ParamField(
        uint8, "face_eyeShadowDownColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUp: int = ParamField(
        uint8, "face_eyeShadowUp", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUpColorR: int = ParamField(
        uint8, "face_eyeShadowUpColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUpColorG: int = ParamField(
        uint8, "face_eyeShadowUpColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FaceeyeShadowUpColorB: int = ParamField(
        uint8, "face_eyeShadowUpColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Facelip: int = ParamField(
        uint8, "face_lip", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacelipColorR: int = ParamField(
        uint8, "face_lipColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacelipColorG: int = ParamField(
        uint8, "face_lipColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    FacelipColorB: int = ParamField(
        uint8, "face_lipColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Bodyhair: int = ParamField(
        uint8, "body_hair", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BodyhairColorR: int = ParamField(
        uint8, "body_hairColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BodyhairColorG: int = ParamField(
        uint8, "body_hairColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BodyhairColorB: int = ParamField(
        uint8, "body_hairColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyepartsId: int = ParamField(
        uint8, "eye_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisColorR: int = ParamField(
        uint8, "eyeR_irisColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisColorG: int = ParamField(
        uint8, "eyeR_irisColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisColorB: int = ParamField(
        uint8, "eyeR_irisColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisScale: int = ParamField(
        uint8, "eyeR_irisScale", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataract: int = ParamField(
        uint8, "eyeR_cataract", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataractColorR: int = ParamField(
        uint8, "eyeR_cataractColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataractColorG: int = ParamField(
        uint8, "eyeR_cataractColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRcataractColorB: int = ParamField(
        uint8, "eyeR_cataractColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRscleraColorR: int = ParamField(
        uint8, "eyeR_scleraColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRscleraColorG: int = ParamField(
        uint8, "eyeR_scleraColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRscleraColorB: int = ParamField(
        uint8, "eyeR_scleraColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeRirisDistance: int = ParamField(
        uint8, "eyeR_irisDistance", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisColorR: int = ParamField(
        uint8, "eyeL_irisColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisColorG: int = ParamField(
        uint8, "eyeL_irisColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisColorB: int = ParamField(
        uint8, "eyeL_irisColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisScale: int = ParamField(
        uint8, "eyeL_irisScale", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataract: int = ParamField(
        uint8, "eyeL_cataract", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataractColorR: int = ParamField(
        uint8, "eyeL_cataractColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataractColorG: int = ParamField(
        uint8, "eyeL_cataractColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLcataractColorB: int = ParamField(
        uint8, "eyeL_cataractColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLscleraColorR: int = ParamField(
        uint8, "eyeL_scleraColor_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLscleraColorG: int = ParamField(
        uint8, "eyeL_scleraColor_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLscleraColorB: int = ParamField(
        uint8, "eyeL_scleraColor_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyeLirisDistance: int = ParamField(
        uint8, "eyeL_irisDistance", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HairpartsId: int = ParamField(
        uint8, "hair_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HaircolorR: int = ParamField(
        uint8, "hair_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HaircolorG: int = ParamField(
        uint8, "hair_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HaircolorB: int = ParamField(
        uint8, "hair_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Hairshininess: int = ParamField(
        uint8, "hair_shininess", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HairrootBlack: int = ParamField(
        uint8, "hair_rootBlack", default=128,
        tooltip="TOOLTIP-TODO",
    )
    HairwhiteDensity: int = ParamField(
        uint8, "hair_whiteDensity", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardpartsId: int = ParamField(
        uint8, "beard_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BeardcolorR: int = ParamField(
        uint8, "beard_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardcolorG: int = ParamField(
        uint8, "beard_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardcolorB: int = ParamField(
        uint8, "beard_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Beardshininess: int = ParamField(
        uint8, "beard_shininess", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardrootBlack: int = ParamField(
        uint8, "beard_rootBlack", default=128,
        tooltip="TOOLTIP-TODO",
    )
    BeardwhiteDensity: int = ParamField(
        uint8, "beard_whiteDensity", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowpartsId: int = ParamField(
        uint8, "eyebrow_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowcolorR: int = ParamField(
        uint8, "eyebrow_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowcolorG: int = ParamField(
        uint8, "eyebrow_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowcolorB: int = ParamField(
        uint8, "eyebrow_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Eyebrowshininess: int = ParamField(
        uint8, "eyebrow_shininess", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowrootBlack: int = ParamField(
        uint8, "eyebrow_rootBlack", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyebrowwhiteDensity: int = ParamField(
        uint8, "eyebrow_whiteDensity", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyelashpartsId: int = ParamField(
        uint8, "eyelash_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EyelashcolorR: int = ParamField(
        uint8, "eyelash_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyelashcolorG: int = ParamField(
        uint8, "eyelash_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    EyelashcolorB: int = ParamField(
        uint8, "eyelash_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriespartsId: int = ParamField(
        uint8, "accessories_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriescolorR: int = ParamField(
        uint8, "accessories_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriescolorG: int = ParamField(
        uint8, "accessories_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    AccessoriescolorB: int = ParamField(
        uint8, "accessories_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    DecalpartsId: int = ParamField(
        uint8, "decal_partsId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DecalposX: int = ParamField(
        uint8, "decal_posX", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DecalposY: int = ParamField(
        uint8, "decal_posY", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Decalangle: int = ParamField(
        uint8, "decal_angle", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Decalscale: int = ParamField(
        uint8, "decal_scale", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DecalcolorR: int = ParamField(
        uint8, "decal_color_R", default=128,
        tooltip="TOOLTIP-TODO",
    )
    DecalcolorG: int = ParamField(
        uint8, "decal_color_G", default=128,
        tooltip="TOOLTIP-TODO",
    )
    DecalcolorB: int = ParamField(
        uint8, "decal_color_B", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Decalgloss: int = ParamField(
        uint8, "decal_gloss", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Decalmirror: int = ParamField(
        uint8, "decal_mirror", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HeadScale: int = ParamField(
        uint8, "chrBodyScaleHead", default=128,
        tooltip="TODO",
    )
    BreastScale: int = ParamField(
        uint8, "chrBodyScaleBreast", default=128,
        tooltip="TODO",
    )
    AbdomenScale: int = ParamField(
        uint8, "chrBodyScaleAbdomen", default=128,
        tooltip="TODO",
    )
    ChrBodyScaleRArm: int = ParamField(
        uint8, "chrBodyScaleRArm", default=128,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleRLeg: int = ParamField(
        uint8, "chrBodyScaleRLeg", default=128,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleLArm: int = ParamField(
        uint8, "chrBodyScaleLArm", default=128,
        tooltip="TOOLTIP-TODO",
    )
    ChrBodyScaleLLeg: int = ParamField(
        uint8, "chrBodyScaleLLeg", default=128,
        tooltip="TOOLTIP-TODO",
    )
    Burnscar: int = ParamField(
        uint8, "burn_scar", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyepartsId: bool = ParamField(
        uint8, "override_eye_partsId:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyeirisColor: bool = ParamField(
        uint8, "override_eye_irisColor:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Overrideeyecataract: bool = ParamField(
        uint8, "override_eye_cataract:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyecataractColor: bool = ParamField(
        uint8, "override_eye_cataractColor:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    OverrideeyescleraColor: bool = ParamField(
        uint8, "override_eye_scleraColor:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    Overrideburnscar: bool = ParamField(
        uint8, "override_burn_scar:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "pad2:2", bit_count=2)
    _Pad0: bytes = ParamPad(5, "pad[5]")
    Age: int = ParamField(
        uint8, "age", default=128,
        tooltip="TODO",
    )
    Gender: int = ParamField(
        uint8, "gender", default=128,
        tooltip="TODO",
    )
    CaricatureGeometry: int = ParamField(
        uint8, "caricatureGeometry", default=128,
        tooltip="TODO",
    )
    CaricatureTexture: int = ParamField(
        uint8, "caricatureTexture", default=128,
        tooltip="TODO",
    )
    GeometryData00: int = ParamField(
        uint8, "faceGeoData00", default=128,
        tooltip="Geometry data point 0.",
    )
    GeometryData01: int = ParamField(
        uint8, "faceGeoData01", default=128,
        tooltip="Geometry data point 1.",
    )
    GeometryData02: int = ParamField(
        uint8, "faceGeoData02", default=128,
        tooltip="Geometry data point 2.",
    )
    GeometryData03: int = ParamField(
        uint8, "faceGeoData03", default=128,
        tooltip="Geometry data point 3.",
    )
    GeometryData04: int = ParamField(
        uint8, "faceGeoData04", default=128,
        tooltip="Geometry data point 4.",
    )
    GeometryData05: int = ParamField(
        uint8, "faceGeoData05", default=128,
        tooltip="Geometry data point 5.",
    )
    GeometryData06: int = ParamField(
        uint8, "faceGeoData06", default=128,
        tooltip="Geometry data point 6.",
    )
    GeometryData07: int = ParamField(
        uint8, "faceGeoData07", default=128,
        tooltip="Geometry data point 7.",
    )
    GeometryData08: int = ParamField(
        uint8, "faceGeoData08", default=128,
        tooltip="Geometry data point 8.",
    )
    GeometryData09: int = ParamField(
        uint8, "faceGeoData09", default=128,
        tooltip="Geometry data point 9.",
    )
    GeometryData10: int = ParamField(
        uint8, "faceGeoData10", default=128,
        tooltip="Geometry data point 10.",
    )
    GeometryData11: int = ParamField(
        uint8, "faceGeoData11", default=128,
        tooltip="Geometry data point 11.",
    )
    GeometryData12: int = ParamField(
        uint8, "faceGeoData12", default=128,
        tooltip="Geometry data point 12.",
    )
    GeometryData13: int = ParamField(
        uint8, "faceGeoData13", default=128,
        tooltip="Geometry data point 13.",
    )
    GeometryData14: int = ParamField(
        uint8, "faceGeoData14", default=128,
        tooltip="Geometry data point 14.",
    )
    GeometryData15: int = ParamField(
        uint8, "faceGeoData15", default=128,
        tooltip="Geometry data point 15.",
    )
    GeometryData16: int = ParamField(
        uint8, "faceGeoData16", default=128,
        tooltip="Geometry data point 16.",
    )
    GeometryData17: int = ParamField(
        uint8, "faceGeoData17", default=128,
        tooltip="Geometry data point 17.",
    )
    GeometryData18: int = ParamField(
        uint8, "faceGeoData18", default=128,
        tooltip="Geometry data point 18.",
    )
    GeometryData19: int = ParamField(
        uint8, "faceGeoData19", default=128,
        tooltip="Geometry data point 19.",
    )
    GeometryData20: int = ParamField(
        uint8, "faceGeoData20", default=128,
        tooltip="Geometry data point 20.",
    )
    GeometryData21: int = ParamField(
        uint8, "faceGeoData21", default=128,
        tooltip="Geometry data point 21.",
    )
    GeometryData22: int = ParamField(
        uint8, "faceGeoData22", default=128,
        tooltip="Geometry data point 22.",
    )
    GeometryData23: int = ParamField(
        uint8, "faceGeoData23", default=128,
        tooltip="Geometry data point 23.",
    )
    GeometryData24: int = ParamField(
        uint8, "faceGeoData24", default=128,
        tooltip="Geometry data point 24.",
    )
    GeometryData25: int = ParamField(
        uint8, "faceGeoData25", default=128,
        tooltip="Geometry data point 25.",
    )
    GeometryData26: int = ParamField(
        uint8, "faceGeoData26", default=128,
        tooltip="Geometry data point 26.",
    )
    GeometryData27: int = ParamField(
        uint8, "faceGeoData27", default=128,
        tooltip="Geometry data point 27.",
    )
    GeometryData28: int = ParamField(
        uint8, "faceGeoData28", default=128,
        tooltip="Geometry data point 28.",
    )
    GeometryData29: int = ParamField(
        uint8, "faceGeoData29", default=128,
        tooltip="Geometry data point 29.",
    )
    GeometryData30: int = ParamField(
        uint8, "faceGeoData30", default=128,
        tooltip="Geometry data point 30.",
    )
    GeometryData31: int = ParamField(
        uint8, "faceGeoData31", default=128,
        tooltip="Geometry data point 31.",
    )
    GeometryData32: int = ParamField(
        uint8, "faceGeoData32", default=128,
        tooltip="Geometry data point 32.",
    )
    GeometryData33: int = ParamField(
        uint8, "faceGeoData33", default=128,
        tooltip="Geometry data point 33.",
    )
    GeometryData34: int = ParamField(
        uint8, "faceGeoData34", default=128,
        tooltip="Geometry data point 34.",
    )
    GeometryData35: int = ParamField(
        uint8, "faceGeoData35", default=128,
        tooltip="Geometry data point 35.",
    )
    GeometryData36: int = ParamField(
        uint8, "faceGeoData36", default=128,
        tooltip="Geometry data point 36.",
    )
    GeometryData37: int = ParamField(
        uint8, "faceGeoData37", default=128,
        tooltip="Geometry data point 37.",
    )
    GeometryData38: int = ParamField(
        uint8, "faceGeoData38", default=128,
        tooltip="Geometry data point 38.",
    )
    GeometryData39: int = ParamField(
        uint8, "faceGeoData39", default=128,
        tooltip="Geometry data point 39.",
    )
    GeometryData40: int = ParamField(
        uint8, "faceGeoData40", default=128,
        tooltip="Geometry data point 40.",
    )
    GeometryData41: int = ParamField(
        uint8, "faceGeoData41", default=128,
        tooltip="Geometry data point 41.",
    )
    GeometryData42: int = ParamField(
        uint8, "faceGeoData42", default=128,
        tooltip="Geometry data point 42.",
    )
    GeometryData43: int = ParamField(
        uint8, "faceGeoData43", default=128,
        tooltip="Geometry data point 43.",
    )
    GeometryData44: int = ParamField(
        uint8, "faceGeoData44", default=128,
        tooltip="Geometry data point 44.",
    )
    GeometryData45: int = ParamField(
        uint8, "faceGeoData45", default=128,
        tooltip="Geometry data point 45.",
    )
    GeometryData46: int = ParamField(
        uint8, "faceGeoData46", default=128,
        tooltip="Geometry data point 46.",
    )
    GeometryData47: int = ParamField(
        uint8, "faceGeoData47", default=128,
        tooltip="Geometry data point 47.",
    )
    GeometryData48: int = ParamField(
        uint8, "faceGeoData48", default=128,
        tooltip="Geometry data point 48.",
    )
    GeometryData49: int = ParamField(
        uint8, "faceGeoData49", default=128,
        tooltip="Geometry data point 49.",
    )
    GeometryData50: int = ParamField(
        uint8, "faceGeoData50", default=128,
        tooltip="Geometry data point 50.",
    )
    GeometryData51: int = ParamField(
        uint8, "faceGeoData51", default=128,
        tooltip="Geometry data point 51.",
    )
    GeometryData52: int = ParamField(
        uint8, "faceGeoData52", default=128,
        tooltip="Geometry data point 52.",
    )
    GeometryData53: int = ParamField(
        uint8, "faceGeoData53", default=128,
        tooltip="Geometry data point 53.",
    )
    GeometryData54: int = ParamField(
        uint8, "faceGeoData54", default=128,
        tooltip="Geometry data point 54.",
    )
    GeometryData55: int = ParamField(
        uint8, "faceGeoData55", default=128,
        tooltip="Geometry data point 55.",
    )
    GeometryData56: int = ParamField(
        uint8, "faceGeoData56", default=128,
        tooltip="Geometry data point 56.",
    )
    GeometryData57: int = ParamField(
        uint8, "faceGeoData57", default=128,
        tooltip="Geometry data point 57.",
    )
    GeometryData58: int = ParamField(
        uint8, "faceGeoData58", default=128,
        tooltip="Geometry data point 58.",
    )
    GeometryData59: int = ParamField(
        uint8, "faceGeoData59", default=128,
        tooltip="Geometry data point 59.",
    )
    GeometryData60: int = ParamField(
        uint8, "faceGeoData60", default=128,
        tooltip="Geometry data point 60.",
    )
    TextureData00: int = ParamField(
        uint8, "faceTexData00", default=128,
        tooltip="Texture data point 0.",
    )
    TextureData01: int = ParamField(
        uint8, "faceTexData01", default=128,
        tooltip="Texture data point 1.",
    )
    TextureData02: int = ParamField(
        uint8, "faceTexData02", default=128,
        tooltip="Texture data point 2.",
    )
    TextureData03: int = ParamField(
        uint8, "faceTexData03", default=128,
        tooltip="Texture data point 3.",
    )
    TextureData04: int = ParamField(
        uint8, "faceTexData04", default=128,
        tooltip="Texture data point 4.",
    )
    TextureData05: int = ParamField(
        uint8, "faceTexData05", default=128,
        tooltip="Texture data point 5.",
    )
    TextureData06: int = ParamField(
        uint8, "faceTexData06", default=128,
        tooltip="Texture data point 6.",
    )
    TextureData07: int = ParamField(
        uint8, "faceTexData07", default=128,
        tooltip="Texture data point 7.",
    )
    TextureData08: int = ParamField(
        uint8, "faceTexData08", default=128,
        tooltip="Texture data point 8.",
    )
    TextureData09: int = ParamField(
        uint8, "faceTexData09", default=128,
        tooltip="Texture data point 9.",
    )
    TextureData10: int = ParamField(
        uint8, "faceTexData10", default=128,
        tooltip="Texture data point 10.",
    )
    TextureData11: int = ParamField(
        uint8, "faceTexData11", default=128,
        tooltip="Texture data point 11.",
    )
    TextureData12: int = ParamField(
        uint8, "faceTexData12", default=128,
        tooltip="Texture data point 12.",
    )
    TextureData13: int = ParamField(
        uint8, "faceTexData13", default=128,
        tooltip="Texture data point 13.",
    )
    TextureData14: int = ParamField(
        uint8, "faceTexData14", default=128,
        tooltip="Texture data point 14.",
    )
    TextureData15: int = ParamField(
        uint8, "faceTexData15", default=128,
        tooltip="Texture data point 15.",
    )
    TextureData16: int = ParamField(
        uint8, "faceTexData16", default=128,
        tooltip="Texture data point 16.",
    )
    TextureData17: int = ParamField(
        uint8, "faceTexData17", default=128,
        tooltip="Texture data point 17.",
    )
    TextureData18: int = ParamField(
        uint8, "faceTexData18", default=128,
        tooltip="Texture data point 18.",
    )
    TextureData19: int = ParamField(
        uint8, "faceTexData19", default=128,
        tooltip="Texture data point 19.",
    )
    TextureData20: int = ParamField(
        uint8, "faceTexData20", default=128,
        tooltip="Texture data point 20.",
    )
    TextureData21: int = ParamField(
        uint8, "faceTexData21", default=128,
        tooltip="Texture data point 21.",
    )
    TextureData22: int = ParamField(
        uint8, "faceTexData22", default=128,
        tooltip="Texture data point 22.",
    )
    TextureData23: int = ParamField(
        uint8, "faceTexData23", default=128,
        tooltip="Texture data point 23.",
    )
    TextureData24: int = ParamField(
        uint8, "faceTexData24", default=128,
        tooltip="Texture data point 24.",
    )
    TextureData25: int = ParamField(
        uint8, "faceTexData25", default=128,
        tooltip="Texture data point 25.",
    )
    TextureData26: int = ParamField(
        uint8, "faceTexData26", default=128,
        tooltip="Texture data point 26.",
    )
    TextureData27: int = ParamField(
        uint8, "faceTexData27", default=128,
        tooltip="Texture data point 27.",
    )
    TextureData28: int = ParamField(
        uint8, "faceTexData28", default=128,
        tooltip="Texture data point 28.",
    )
    TextureData29: int = ParamField(
        uint8, "faceTexData29", default=128,
        tooltip="Texture data point 29.",
    )
    TextureData30: int = ParamField(
        uint8, "faceTexData30", default=128,
        tooltip="Texture data point 30.",
    )
    TextureData31: int = ParamField(
        uint8, "faceTexData31", default=128,
        tooltip="Texture data point 31.",
    )
    TextureData32: int = ParamField(
        uint8, "faceTexData32", default=128,
        tooltip="Texture data point 32.",
    )
    TextureData33: int = ParamField(
        uint8, "faceTexData33", default=128,
        tooltip="Texture data point 33.",
    )
    TextureData34: int = ParamField(
        uint8, "faceTexData34", default=128,
        tooltip="Texture data point 34.",
    )
    TextureData35: int = ParamField(
        uint8, "faceTexData35", default=128,
        tooltip="Texture data point 35.",
    )
    GeoAsymData00: int = ParamField(
        uint8, "faceGeoAsymData00", default=128,
        tooltip="Geometry asym data point 0.",
    )
    GeoAsymData01: int = ParamField(
        uint8, "faceGeoAsymData01", default=128,
        tooltip="Geometry asym data point 1.",
    )
    GeoAsymData02: int = ParamField(
        uint8, "faceGeoAsymData02", default=128,
        tooltip="Geometry asym data point 2.",
    )
    GeoAsymData03: int = ParamField(
        uint8, "faceGeoAsymData03", default=128,
        tooltip="Geometry asym data point 3.",
    )
    GeoAsymData04: int = ParamField(
        uint8, "faceGeoAsymData04", default=128,
        tooltip="Geometry asym data point 4.",
    )
    GeoAsymData05: int = ParamField(
        uint8, "faceGeoAsymData05", default=128,
        tooltip="Geometry asym data point 5.",
    )
    GeoAsymData06: int = ParamField(
        uint8, "faceGeoAsymData06", default=128,
        tooltip="Geometry asym data point 6.",
    )
    GeoAsymData07: int = ParamField(
        uint8, "faceGeoAsymData07", default=128,
        tooltip="Geometry asym data point 7.",
    )
    GeoAsymData08: int = ParamField(
        uint8, "faceGeoAsymData08", default=128,
        tooltip="Geometry asym data point 8.",
    )
    GeoAsymData09: int = ParamField(
        uint8, "faceGeoAsymData09", default=128,
        tooltip="Geometry asym data point 9.",
    )
    GeoAsymData10: int = ParamField(
        uint8, "faceGeoAsymData10", default=128,
        tooltip="Geometry asym data point 10.",
    )
    GeoAsymData11: int = ParamField(
        uint8, "faceGeoAsymData11", default=128,
        tooltip="Geometry asym data point 11.",
    )
    GeoAsymData12: int = ParamField(
        uint8, "faceGeoAsymData12", default=128,
        tooltip="Geometry asym data point 12.",
    )
    GeoAsymData13: int = ParamField(
        uint8, "faceGeoAsymData13", default=128,
        tooltip="Geometry asym data point 13.",
    )
    GeoAsymData14: int = ParamField(
        uint8, "faceGeoAsymData14", default=128,
        tooltip="Geometry asym data point 14.",
    )
    GeoAsymData15: int = ParamField(
        uint8, "faceGeoAsymData15", default=128,
        tooltip="Geometry asym data point 15.",
    )
    GeoAsymData16: int = ParamField(
        uint8, "faceGeoAsymData16", default=128,
        tooltip="Geometry asym data point 16.",
    )
    GeoAsymData17: int = ParamField(
        uint8, "faceGeoAsymData17", default=128,
        tooltip="Geometry asym data point 17.",
    )
    GeoAsymData18: int = ParamField(
        uint8, "faceGeoAsymData18", default=128,
        tooltip="Geometry asym data point 18.",
    )
    GeoAsymData19: int = ParamField(
        uint8, "faceGeoAsymData19", default=128,
        tooltip="Geometry asym data point 19.",
    )
    GeoAsymData20: int = ParamField(
        uint8, "faceGeoAsymData20", default=128,
        tooltip="Geometry asym data point 20.",
    )
    GeoAsymData21: int = ParamField(
        uint8, "faceGeoAsymData21", default=128,
        tooltip="Geometry asym data point 21.",
    )
    GeoAsymData22: int = ParamField(
        uint8, "faceGeoAsymData22", default=128,
        tooltip="Geometry asym data point 22.",
    )
    GeoAsymData23: int = ParamField(
        uint8, "faceGeoAsymData23", default=128,
        tooltip="Geometry asym data point 23.",
    )
    GeoAsymData24: int = ParamField(
        uint8, "faceGeoAsymData24", default=128,
        tooltip="Geometry asym data point 24.",
    )
    GeoAsymData25: int = ParamField(
        uint8, "faceGeoAsymData25", default=128,
        tooltip="Geometry asym data point 25.",
    )
