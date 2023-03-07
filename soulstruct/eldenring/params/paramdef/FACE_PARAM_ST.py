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
    HeadScale: int = ParamField(
        byte, "chrBodyScaleHead", default=128,
        tooltip="TODO",
    )
    BreastScale: int = ParamField(
        byte, "chrBodyScaleBreast", default=128,
        tooltip="TODO",
    )
    AbdomenScale: int = ParamField(
        byte, "chrBodyScaleAbdomen", default=128,
        tooltip="TODO",
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
        tooltip="TODO",
    )
    Gender: int = ParamField(
        byte, "gender", default=128,
        tooltip="TODO",
    )
    CaricatureGeometry: int = ParamField(
        byte, "caricatureGeometry", default=128,
        tooltip="TODO",
    )
    CaricatureTexture: int = ParamField(
        byte, "caricatureTexture", default=128,
        tooltip="TODO",
    )
    GeometryData00: int = ParamField(
        byte, "faceGeoData00", default=128,
        tooltip="Geometry data point 0.",
    )
    GeometryData01: int = ParamField(
        byte, "faceGeoData01", default=128,
        tooltip="Geometry data point 1.",
    )
    GeometryData02: int = ParamField(
        byte, "faceGeoData02", default=128,
        tooltip="Geometry data point 2.",
    )
    GeometryData03: int = ParamField(
        byte, "faceGeoData03", default=128,
        tooltip="Geometry data point 3.",
    )
    GeometryData04: int = ParamField(
        byte, "faceGeoData04", default=128,
        tooltip="Geometry data point 4.",
    )
    GeometryData05: int = ParamField(
        byte, "faceGeoData05", default=128,
        tooltip="Geometry data point 5.",
    )
    GeometryData06: int = ParamField(
        byte, "faceGeoData06", default=128,
        tooltip="Geometry data point 6.",
    )
    GeometryData07: int = ParamField(
        byte, "faceGeoData07", default=128,
        tooltip="Geometry data point 7.",
    )
    GeometryData08: int = ParamField(
        byte, "faceGeoData08", default=128,
        tooltip="Geometry data point 8.",
    )
    GeometryData09: int = ParamField(
        byte, "faceGeoData09", default=128,
        tooltip="Geometry data point 9.",
    )
    GeometryData10: int = ParamField(
        byte, "faceGeoData10", default=128,
        tooltip="Geometry data point 10.",
    )
    GeometryData11: int = ParamField(
        byte, "faceGeoData11", default=128,
        tooltip="Geometry data point 11.",
    )
    GeometryData12: int = ParamField(
        byte, "faceGeoData12", default=128,
        tooltip="Geometry data point 12.",
    )
    GeometryData13: int = ParamField(
        byte, "faceGeoData13", default=128,
        tooltip="Geometry data point 13.",
    )
    GeometryData14: int = ParamField(
        byte, "faceGeoData14", default=128,
        tooltip="Geometry data point 14.",
    )
    GeometryData15: int = ParamField(
        byte, "faceGeoData15", default=128,
        tooltip="Geometry data point 15.",
    )
    GeometryData16: int = ParamField(
        byte, "faceGeoData16", default=128,
        tooltip="Geometry data point 16.",
    )
    GeometryData17: int = ParamField(
        byte, "faceGeoData17", default=128,
        tooltip="Geometry data point 17.",
    )
    GeometryData18: int = ParamField(
        byte, "faceGeoData18", default=128,
        tooltip="Geometry data point 18.",
    )
    GeometryData19: int = ParamField(
        byte, "faceGeoData19", default=128,
        tooltip="Geometry data point 19.",
    )
    GeometryData20: int = ParamField(
        byte, "faceGeoData20", default=128,
        tooltip="Geometry data point 20.",
    )
    GeometryData21: int = ParamField(
        byte, "faceGeoData21", default=128,
        tooltip="Geometry data point 21.",
    )
    GeometryData22: int = ParamField(
        byte, "faceGeoData22", default=128,
        tooltip="Geometry data point 22.",
    )
    GeometryData23: int = ParamField(
        byte, "faceGeoData23", default=128,
        tooltip="Geometry data point 23.",
    )
    GeometryData24: int = ParamField(
        byte, "faceGeoData24", default=128,
        tooltip="Geometry data point 24.",
    )
    GeometryData25: int = ParamField(
        byte, "faceGeoData25", default=128,
        tooltip="Geometry data point 25.",
    )
    GeometryData26: int = ParamField(
        byte, "faceGeoData26", default=128,
        tooltip="Geometry data point 26.",
    )
    GeometryData27: int = ParamField(
        byte, "faceGeoData27", default=128,
        tooltip="Geometry data point 27.",
    )
    GeometryData28: int = ParamField(
        byte, "faceGeoData28", default=128,
        tooltip="Geometry data point 28.",
    )
    GeometryData29: int = ParamField(
        byte, "faceGeoData29", default=128,
        tooltip="Geometry data point 29.",
    )
    GeometryData30: int = ParamField(
        byte, "faceGeoData30", default=128,
        tooltip="Geometry data point 30.",
    )
    GeometryData31: int = ParamField(
        byte, "faceGeoData31", default=128,
        tooltip="Geometry data point 31.",
    )
    GeometryData32: int = ParamField(
        byte, "faceGeoData32", default=128,
        tooltip="Geometry data point 32.",
    )
    GeometryData33: int = ParamField(
        byte, "faceGeoData33", default=128,
        tooltip="Geometry data point 33.",
    )
    GeometryData34: int = ParamField(
        byte, "faceGeoData34", default=128,
        tooltip="Geometry data point 34.",
    )
    GeometryData35: int = ParamField(
        byte, "faceGeoData35", default=128,
        tooltip="Geometry data point 35.",
    )
    GeometryData36: int = ParamField(
        byte, "faceGeoData36", default=128,
        tooltip="Geometry data point 36.",
    )
    GeometryData37: int = ParamField(
        byte, "faceGeoData37", default=128,
        tooltip="Geometry data point 37.",
    )
    GeometryData38: int = ParamField(
        byte, "faceGeoData38", default=128,
        tooltip="Geometry data point 38.",
    )
    GeometryData39: int = ParamField(
        byte, "faceGeoData39", default=128,
        tooltip="Geometry data point 39.",
    )
    GeometryData40: int = ParamField(
        byte, "faceGeoData40", default=128,
        tooltip="Geometry data point 40.",
    )
    GeometryData41: int = ParamField(
        byte, "faceGeoData41", default=128,
        tooltip="Geometry data point 41.",
    )
    GeometryData42: int = ParamField(
        byte, "faceGeoData42", default=128,
        tooltip="Geometry data point 42.",
    )
    GeometryData43: int = ParamField(
        byte, "faceGeoData43", default=128,
        tooltip="Geometry data point 43.",
    )
    GeometryData44: int = ParamField(
        byte, "faceGeoData44", default=128,
        tooltip="Geometry data point 44.",
    )
    GeometryData45: int = ParamField(
        byte, "faceGeoData45", default=128,
        tooltip="Geometry data point 45.",
    )
    GeometryData46: int = ParamField(
        byte, "faceGeoData46", default=128,
        tooltip="Geometry data point 46.",
    )
    GeometryData47: int = ParamField(
        byte, "faceGeoData47", default=128,
        tooltip="Geometry data point 47.",
    )
    GeometryData48: int = ParamField(
        byte, "faceGeoData48", default=128,
        tooltip="Geometry data point 48.",
    )
    GeometryData49: int = ParamField(
        byte, "faceGeoData49", default=128,
        tooltip="Geometry data point 49.",
    )
    GeometryData50: int = ParamField(
        byte, "faceGeoData50", default=128,
        tooltip="Geometry data point 50.",
    )
    GeometryData51: int = ParamField(
        byte, "faceGeoData51", default=128,
        tooltip="Geometry data point 51.",
    )
    GeometryData52: int = ParamField(
        byte, "faceGeoData52", default=128,
        tooltip="Geometry data point 52.",
    )
    GeometryData53: int = ParamField(
        byte, "faceGeoData53", default=128,
        tooltip="Geometry data point 53.",
    )
    GeometryData54: int = ParamField(
        byte, "faceGeoData54", default=128,
        tooltip="Geometry data point 54.",
    )
    GeometryData55: int = ParamField(
        byte, "faceGeoData55", default=128,
        tooltip="Geometry data point 55.",
    )
    GeometryData56: int = ParamField(
        byte, "faceGeoData56", default=128,
        tooltip="Geometry data point 56.",
    )
    GeometryData57: int = ParamField(
        byte, "faceGeoData57", default=128,
        tooltip="Geometry data point 57.",
    )
    GeometryData58: int = ParamField(
        byte, "faceGeoData58", default=128,
        tooltip="Geometry data point 58.",
    )
    GeometryData59: int = ParamField(
        byte, "faceGeoData59", default=128,
        tooltip="Geometry data point 59.",
    )
    GeometryData60: int = ParamField(
        byte, "faceGeoData60", default=128,
        tooltip="Geometry data point 60.",
    )
    TextureData00: int = ParamField(
        byte, "faceTexData00", default=128,
        tooltip="Texture data point 0.",
    )
    TextureData01: int = ParamField(
        byte, "faceTexData01", default=128,
        tooltip="Texture data point 1.",
    )
    TextureData02: int = ParamField(
        byte, "faceTexData02", default=128,
        tooltip="Texture data point 2.",
    )
    TextureData03: int = ParamField(
        byte, "faceTexData03", default=128,
        tooltip="Texture data point 3.",
    )
    TextureData04: int = ParamField(
        byte, "faceTexData04", default=128,
        tooltip="Texture data point 4.",
    )
    TextureData05: int = ParamField(
        byte, "faceTexData05", default=128,
        tooltip="Texture data point 5.",
    )
    TextureData06: int = ParamField(
        byte, "faceTexData06", default=128,
        tooltip="Texture data point 6.",
    )
    TextureData07: int = ParamField(
        byte, "faceTexData07", default=128,
        tooltip="Texture data point 7.",
    )
    TextureData08: int = ParamField(
        byte, "faceTexData08", default=128,
        tooltip="Texture data point 8.",
    )
    TextureData09: int = ParamField(
        byte, "faceTexData09", default=128,
        tooltip="Texture data point 9.",
    )
    TextureData10: int = ParamField(
        byte, "faceTexData10", default=128,
        tooltip="Texture data point 10.",
    )
    TextureData11: int = ParamField(
        byte, "faceTexData11", default=128,
        tooltip="Texture data point 11.",
    )
    TextureData12: int = ParamField(
        byte, "faceTexData12", default=128,
        tooltip="Texture data point 12.",
    )
    TextureData13: int = ParamField(
        byte, "faceTexData13", default=128,
        tooltip="Texture data point 13.",
    )
    TextureData14: int = ParamField(
        byte, "faceTexData14", default=128,
        tooltip="Texture data point 14.",
    )
    TextureData15: int = ParamField(
        byte, "faceTexData15", default=128,
        tooltip="Texture data point 15.",
    )
    TextureData16: int = ParamField(
        byte, "faceTexData16", default=128,
        tooltip="Texture data point 16.",
    )
    TextureData17: int = ParamField(
        byte, "faceTexData17", default=128,
        tooltip="Texture data point 17.",
    )
    TextureData18: int = ParamField(
        byte, "faceTexData18", default=128,
        tooltip="Texture data point 18.",
    )
    TextureData19: int = ParamField(
        byte, "faceTexData19", default=128,
        tooltip="Texture data point 19.",
    )
    TextureData20: int = ParamField(
        byte, "faceTexData20", default=128,
        tooltip="Texture data point 20.",
    )
    TextureData21: int = ParamField(
        byte, "faceTexData21", default=128,
        tooltip="Texture data point 21.",
    )
    TextureData22: int = ParamField(
        byte, "faceTexData22", default=128,
        tooltip="Texture data point 22.",
    )
    TextureData23: int = ParamField(
        byte, "faceTexData23", default=128,
        tooltip="Texture data point 23.",
    )
    TextureData24: int = ParamField(
        byte, "faceTexData24", default=128,
        tooltip="Texture data point 24.",
    )
    TextureData25: int = ParamField(
        byte, "faceTexData25", default=128,
        tooltip="Texture data point 25.",
    )
    TextureData26: int = ParamField(
        byte, "faceTexData26", default=128,
        tooltip="Texture data point 26.",
    )
    TextureData27: int = ParamField(
        byte, "faceTexData27", default=128,
        tooltip="Texture data point 27.",
    )
    TextureData28: int = ParamField(
        byte, "faceTexData28", default=128,
        tooltip="Texture data point 28.",
    )
    TextureData29: int = ParamField(
        byte, "faceTexData29", default=128,
        tooltip="Texture data point 29.",
    )
    TextureData30: int = ParamField(
        byte, "faceTexData30", default=128,
        tooltip="Texture data point 30.",
    )
    TextureData31: int = ParamField(
        byte, "faceTexData31", default=128,
        tooltip="Texture data point 31.",
    )
    TextureData32: int = ParamField(
        byte, "faceTexData32", default=128,
        tooltip="Texture data point 32.",
    )
    TextureData33: int = ParamField(
        byte, "faceTexData33", default=128,
        tooltip="Texture data point 33.",
    )
    TextureData34: int = ParamField(
        byte, "faceTexData34", default=128,
        tooltip="Texture data point 34.",
    )
    TextureData35: int = ParamField(
        byte, "faceTexData35", default=128,
        tooltip="Texture data point 35.",
    )
    GeoAsymData00: int = ParamField(
        byte, "faceGeoAsymData00", default=128,
        tooltip="Geometry asym data point 0.",
    )
    GeoAsymData01: int = ParamField(
        byte, "faceGeoAsymData01", default=128,
        tooltip="Geometry asym data point 1.",
    )
    GeoAsymData02: int = ParamField(
        byte, "faceGeoAsymData02", default=128,
        tooltip="Geometry asym data point 2.",
    )
    GeoAsymData03: int = ParamField(
        byte, "faceGeoAsymData03", default=128,
        tooltip="Geometry asym data point 3.",
    )
    GeoAsymData04: int = ParamField(
        byte, "faceGeoAsymData04", default=128,
        tooltip="Geometry asym data point 4.",
    )
    GeoAsymData05: int = ParamField(
        byte, "faceGeoAsymData05", default=128,
        tooltip="Geometry asym data point 5.",
    )
    GeoAsymData06: int = ParamField(
        byte, "faceGeoAsymData06", default=128,
        tooltip="Geometry asym data point 6.",
    )
    GeoAsymData07: int = ParamField(
        byte, "faceGeoAsymData07", default=128,
        tooltip="Geometry asym data point 7.",
    )
    GeoAsymData08: int = ParamField(
        byte, "faceGeoAsymData08", default=128,
        tooltip="Geometry asym data point 8.",
    )
    GeoAsymData09: int = ParamField(
        byte, "faceGeoAsymData09", default=128,
        tooltip="Geometry asym data point 9.",
    )
    GeoAsymData10: int = ParamField(
        byte, "faceGeoAsymData10", default=128,
        tooltip="Geometry asym data point 10.",
    )
    GeoAsymData11: int = ParamField(
        byte, "faceGeoAsymData11", default=128,
        tooltip="Geometry asym data point 11.",
    )
    GeoAsymData12: int = ParamField(
        byte, "faceGeoAsymData12", default=128,
        tooltip="Geometry asym data point 12.",
    )
    GeoAsymData13: int = ParamField(
        byte, "faceGeoAsymData13", default=128,
        tooltip="Geometry asym data point 13.",
    )
    GeoAsymData14: int = ParamField(
        byte, "faceGeoAsymData14", default=128,
        tooltip="Geometry asym data point 14.",
    )
    GeoAsymData15: int = ParamField(
        byte, "faceGeoAsymData15", default=128,
        tooltip="Geometry asym data point 15.",
    )
    GeoAsymData16: int = ParamField(
        byte, "faceGeoAsymData16", default=128,
        tooltip="Geometry asym data point 16.",
    )
    GeoAsymData17: int = ParamField(
        byte, "faceGeoAsymData17", default=128,
        tooltip="Geometry asym data point 17.",
    )
    GeoAsymData18: int = ParamField(
        byte, "faceGeoAsymData18", default=128,
        tooltip="Geometry asym data point 18.",
    )
    GeoAsymData19: int = ParamField(
        byte, "faceGeoAsymData19", default=128,
        tooltip="Geometry asym data point 19.",
    )
    GeoAsymData20: int = ParamField(
        byte, "faceGeoAsymData20", default=128,
        tooltip="Geometry asym data point 20.",
    )
    GeoAsymData21: int = ParamField(
        byte, "faceGeoAsymData21", default=128,
        tooltip="Geometry asym data point 21.",
    )
    GeoAsymData22: int = ParamField(
        byte, "faceGeoAsymData22", default=128,
        tooltip="Geometry asym data point 22.",
    )
    GeoAsymData23: int = ParamField(
        byte, "faceGeoAsymData23", default=128,
        tooltip="Geometry asym data point 23.",
    )
    GeoAsymData24: int = ParamField(
        byte, "faceGeoAsymData24", default=128,
        tooltip="Geometry asym data point 24.",
    )
    GeoAsymData25: int = ParamField(
        byte, "faceGeoAsymData25", default=128,
        tooltip="Geometry asym data point 25.",
    )
