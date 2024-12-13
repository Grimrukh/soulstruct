from __future__ import annotations

__all__ = ["FACE_RANGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


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
    HeadScale: float = ParamField(
        float, "chrBodyScaleHead", default=0.0,
        tooltip="TODO",
    )
    BreastScale: float = ParamField(
        float, "chrBodyScaleBreast", default=0.0,
        tooltip="TODO",
    )
    AbdomenScale: float = ParamField(
        float, "chrBodyScaleAbdomen", default=0.0,
        tooltip="TODO",
    )
    ArmScale: float = ParamField(
        float, "chrBodyScaleArm", default=0.0,
        tooltip="TODO",
    )
    LegScale: float = ParamField(
        float, "chrBodyScaleLeg", default=0.0,
        tooltip="TODO",
    )
    Age: float = ParamField(
        float, "age", default=0.0,
        tooltip="TODO",
    )
    Gender: float = ParamField(
        float, "gender", default=0.0,
        tooltip="TODO",
    )
    CaricatureGeometry: float = ParamField(
        float, "caricatureGeometry", default=0.0,
        tooltip="TODO",
    )
    CaricatureTexture: float = ParamField(
        float, "caricatureTexture", default=0.0,
        tooltip="TODO",
    )
    GeometryData00: float = ParamField(
        float, "faceGeoData00", default=0.0,
        tooltip="Geometry data point 0.",
    )
    GeometryData01: float = ParamField(
        float, "faceGeoData01", default=0.0,
        tooltip="Geometry data point 1.",
    )
    GeometryData02: float = ParamField(
        float, "faceGeoData02", default=0.0,
        tooltip="Geometry data point 2.",
    )
    GeometryData03: float = ParamField(
        float, "faceGeoData03", default=0.0,
        tooltip="Geometry data point 3.",
    )
    GeometryData04: float = ParamField(
        float, "faceGeoData04", default=0.0,
        tooltip="Geometry data point 4.",
    )
    GeometryData05: float = ParamField(
        float, "faceGeoData05", default=0.0,
        tooltip="Geometry data point 5.",
    )
    GeometryData06: float = ParamField(
        float, "faceGeoData06", default=0.0,
        tooltip="Geometry data point 6.",
    )
    GeometryData07: float = ParamField(
        float, "faceGeoData07", default=0.0,
        tooltip="Geometry data point 7.",
    )
    GeometryData08: float = ParamField(
        float, "faceGeoData08", default=0.0,
        tooltip="Geometry data point 8.",
    )
    GeometryData09: float = ParamField(
        float, "faceGeoData09", default=0.0,
        tooltip="Geometry data point 9.",
    )
    GeometryData10: float = ParamField(
        float, "faceGeoData10", default=0.0,
        tooltip="Geometry data point 10.",
    )
    GeometryData11: float = ParamField(
        float, "faceGeoData11", default=0.0,
        tooltip="Geometry data point 11.",
    )
    GeometryData12: float = ParamField(
        float, "faceGeoData12", default=0.0,
        tooltip="Geometry data point 12.",
    )
    GeometryData13: float = ParamField(
        float, "faceGeoData13", default=0.0,
        tooltip="Geometry data point 13.",
    )
    GeometryData14: float = ParamField(
        float, "faceGeoData14", default=0.0,
        tooltip="Geometry data point 14.",
    )
    GeometryData15: float = ParamField(
        float, "faceGeoData15", default=0.0,
        tooltip="Geometry data point 15.",
    )
    GeometryData16: float = ParamField(
        float, "faceGeoData16", default=0.0,
        tooltip="Geometry data point 16.",
    )
    GeometryData17: float = ParamField(
        float, "faceGeoData17", default=0.0,
        tooltip="Geometry data point 17.",
    )
    GeometryData18: float = ParamField(
        float, "faceGeoData18", default=0.0,
        tooltip="Geometry data point 18.",
    )
    GeometryData19: float = ParamField(
        float, "faceGeoData19", default=0.0,
        tooltip="Geometry data point 19.",
    )
    GeometryData20: float = ParamField(
        float, "faceGeoData20", default=0.0,
        tooltip="Geometry data point 20.",
    )
    GeometryData21: float = ParamField(
        float, "faceGeoData21", default=0.0,
        tooltip="Geometry data point 21.",
    )
    GeometryData22: float = ParamField(
        float, "faceGeoData22", default=0.0,
        tooltip="Geometry data point 22.",
    )
    GeometryData23: float = ParamField(
        float, "faceGeoData23", default=0.0,
        tooltip="Geometry data point 23.",
    )
    GeometryData24: float = ParamField(
        float, "faceGeoData24", default=0.0,
        tooltip="Geometry data point 24.",
    )
    GeometryData25: float = ParamField(
        float, "faceGeoData25", default=0.0,
        tooltip="Geometry data point 25.",
    )
    GeometryData26: float = ParamField(
        float, "faceGeoData26", default=0.0,
        tooltip="Geometry data point 26.",
    )
    GeometryData27: float = ParamField(
        float, "faceGeoData27", default=0.0,
        tooltip="Geometry data point 27.",
    )
    GeometryData28: float = ParamField(
        float, "faceGeoData28", default=0.0,
        tooltip="Geometry data point 28.",
    )
    GeometryData29: float = ParamField(
        float, "faceGeoData29", default=0.0,
        tooltip="Geometry data point 29.",
    )
    GeometryData30: float = ParamField(
        float, "faceGeoData30", default=0.0,
        tooltip="Geometry data point 30.",
    )
    GeometryData31: float = ParamField(
        float, "faceGeoData31", default=0.0,
        tooltip="Geometry data point 31.",
    )
    GeometryData32: float = ParamField(
        float, "faceGeoData32", default=0.0,
        tooltip="Geometry data point 32.",
    )
    GeometryData33: float = ParamField(
        float, "faceGeoData33", default=0.0,
        tooltip="Geometry data point 33.",
    )
    GeometryData34: float = ParamField(
        float, "faceGeoData34", default=0.0,
        tooltip="Geometry data point 34.",
    )
    GeometryData35: float = ParamField(
        float, "faceGeoData35", default=0.0,
        tooltip="Geometry data point 35.",
    )
    GeometryData36: float = ParamField(
        float, "faceGeoData36", default=0.0,
        tooltip="Geometry data point 36.",
    )
    GeometryData37: float = ParamField(
        float, "faceGeoData37", default=0.0,
        tooltip="Geometry data point 37.",
    )
    GeometryData38: float = ParamField(
        float, "faceGeoData38", default=0.0,
        tooltip="Geometry data point 38.",
    )
    GeometryData39: float = ParamField(
        float, "faceGeoData39", default=0.0,
        tooltip="Geometry data point 39.",
    )
    GeometryData40: float = ParamField(
        float, "faceGeoData40", default=0.0,
        tooltip="Geometry data point 40.",
    )
    GeometryData41: float = ParamField(
        float, "faceGeoData41", default=0.0,
        tooltip="Geometry data point 41.",
    )
    GeometryData42: float = ParamField(
        float, "faceGeoData42", default=0.0,
        tooltip="Geometry data point 42.",
    )
    GeometryData43: float = ParamField(
        float, "faceGeoData43", default=0.0,
        tooltip="Geometry data point 43.",
    )
    GeometryData44: float = ParamField(
        float, "faceGeoData44", default=0.0,
        tooltip="Geometry data point 44.",
    )
    GeometryData45: float = ParamField(
        float, "faceGeoData45", default=0.0,
        tooltip="Geometry data point 45.",
    )
    GeometryData46: float = ParamField(
        float, "faceGeoData46", default=0.0,
        tooltip="Geometry data point 46.",
    )
    GeometryData47: float = ParamField(
        float, "faceGeoData47", default=0.0,
        tooltip="Geometry data point 47.",
    )
    GeometryData48: float = ParamField(
        float, "faceGeoData48", default=0.0,
        tooltip="Geometry data point 48.",
    )
    GeometryData49: float = ParamField(
        float, "faceGeoData49", default=0.0,
        tooltip="Geometry data point 49.",
    )
    GeometryData50: float = ParamField(
        float, "faceGeoData50", default=0.0,
        tooltip="Geometry data point 50.",
    )
    GeometryData51: float = ParamField(
        float, "faceGeoData51", default=0.0,
        tooltip="Geometry data point 51.",
    )
    GeometryData52: float = ParamField(
        float, "faceGeoData52", default=0.0,
        tooltip="Geometry data point 52.",
    )
    GeometryData53: float = ParamField(
        float, "faceGeoData53", default=0.0,
        tooltip="Geometry data point 53.",
    )
    GeometryData54: float = ParamField(
        float, "faceGeoData54", default=0.0,
        tooltip="Geometry data point 54.",
    )
    GeometryData55: float = ParamField(
        float, "faceGeoData55", default=0.0,
        tooltip="Geometry data point 55.",
    )
    GeometryData56: float = ParamField(
        float, "faceGeoData56", default=0.0,
        tooltip="Geometry data point 56.",
    )
    GeometryData57: float = ParamField(
        float, "faceGeoData57", default=0.0,
        tooltip="Geometry data point 57.",
    )
    GeometryData58: float = ParamField(
        float, "faceGeoData58", default=0.0,
        tooltip="Geometry data point 58.",
    )
    GeometryData59: float = ParamField(
        float, "faceGeoData59", default=0.0,
        tooltip="Geometry data point 59.",
    )
    GeometryData60: float = ParamField(
        float, "faceGeoData60", default=0.0,
        tooltip="Geometry data point 60.",
    )
    TextureData00: float = ParamField(
        float, "faceTexData00", default=0.0,
        tooltip="Texture data point 0.",
    )
    TextureData01: float = ParamField(
        float, "faceTexData01", default=0.0,
        tooltip="Texture data point 1.",
    )
    TextureData02: float = ParamField(
        float, "faceTexData02", default=0.0,
        tooltip="Texture data point 2.",
    )
    TextureData03: float = ParamField(
        float, "faceTexData03", default=0.0,
        tooltip="Texture data point 3.",
    )
    TextureData04: float = ParamField(
        float, "faceTexData04", default=0.0,
        tooltip="Texture data point 4.",
    )
    TextureData05: float = ParamField(
        float, "faceTexData05", default=0.0,
        tooltip="Texture data point 5.",
    )
    TextureData06: float = ParamField(
        float, "faceTexData06", default=0.0,
        tooltip="Texture data point 6.",
    )
    TextureData07: float = ParamField(
        float, "faceTexData07", default=0.0,
        tooltip="Texture data point 7.",
    )
    TextureData08: float = ParamField(
        float, "faceTexData08", default=0.0,
        tooltip="Texture data point 8.",
    )
    TextureData09: float = ParamField(
        float, "faceTexData09", default=0.0,
        tooltip="Texture data point 9.",
    )
    TextureData10: float = ParamField(
        float, "faceTexData10", default=0.0,
        tooltip="Texture data point 10.",
    )
    TextureData11: float = ParamField(
        float, "faceTexData11", default=0.0,
        tooltip="Texture data point 11.",
    )
    TextureData12: float = ParamField(
        float, "faceTexData12", default=0.0,
        tooltip="Texture data point 12.",
    )
    TextureData13: float = ParamField(
        float, "faceTexData13", default=0.0,
        tooltip="Texture data point 13.",
    )
    TextureData14: float = ParamField(
        float, "faceTexData14", default=0.0,
        tooltip="Texture data point 14.",
    )
    TextureData15: float = ParamField(
        float, "faceTexData15", default=0.0,
        tooltip="Texture data point 15.",
    )
    TextureData16: float = ParamField(
        float, "faceTexData16", default=0.0,
        tooltip="Texture data point 16.",
    )
    TextureData17: float = ParamField(
        float, "faceTexData17", default=0.0,
        tooltip="Texture data point 17.",
    )
    TextureData18: float = ParamField(
        float, "faceTexData18", default=0.0,
        tooltip="Texture data point 18.",
    )
    TextureData19: float = ParamField(
        float, "faceTexData19", default=0.0,
        tooltip="Texture data point 19.",
    )
    TextureData20: float = ParamField(
        float, "faceTexData20", default=0.0,
        tooltip="Texture data point 20.",
    )
    TextureData21: float = ParamField(
        float, "faceTexData21", default=0.0,
        tooltip="Texture data point 21.",
    )
    TextureData22: float = ParamField(
        float, "faceTexData22", default=0.0,
        tooltip="Texture data point 22.",
    )
    TextureData23: float = ParamField(
        float, "faceTexData23", default=0.0,
        tooltip="Texture data point 23.",
    )
    TextureData24: float = ParamField(
        float, "faceTexData24", default=0.0,
        tooltip="Texture data point 24.",
    )
    TextureData25: float = ParamField(
        float, "faceTexData25", default=0.0,
        tooltip="Texture data point 25.",
    )
    TextureData26: float = ParamField(
        float, "faceTexData26", default=0.0,
        tooltip="Texture data point 26.",
    )
    TextureData27: float = ParamField(
        float, "faceTexData27", default=0.0,
        tooltip="Texture data point 27.",
    )
    TextureData28: float = ParamField(
        float, "faceTexData28", default=0.0,
        tooltip="Texture data point 28.",
    )
    TextureData29: float = ParamField(
        float, "faceTexData29", default=0.0,
        tooltip="Texture data point 29.",
    )
    TextureData30: float = ParamField(
        float, "faceTexData30", default=0.0,
        tooltip="Texture data point 30.",
    )
    TextureData31: float = ParamField(
        float, "faceTexData31", default=0.0,
        tooltip="Texture data point 31.",
    )
    TextureData32: float = ParamField(
        float, "faceTexData32", default=0.0,
        tooltip="Texture data point 32.",
    )
    TextureData33: float = ParamField(
        float, "faceTexData33", default=0.0,
        tooltip="Texture data point 33.",
    )
    TextureData34: float = ParamField(
        float, "faceTexData34", default=0.0,
        tooltip="Texture data point 34.",
    )
    TextureData35: float = ParamField(
        float, "faceTexData35", default=0.0,
        tooltip="Texture data point 35.",
    )
    Burnscar: float = ParamField(
        float, "burn_scar", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
