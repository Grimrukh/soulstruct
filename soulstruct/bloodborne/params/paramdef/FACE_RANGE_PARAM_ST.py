from __future__ import annotations

__all__ = ["FACE_RANGE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class FACE_RANGE_PARAM_ST(ParamRow):
    FacePartsID: int = ParamField(
        float, "facePartsId", default=0.0,
        tooltip="TODO",
    )
    SkinColorRed: int = ParamField(
        float, "skinColor_R ", default=0.0,
        tooltip="TODO",
    )
    SkinColorGreen: int = ParamField(
        float, "skinColor_G ", default=0.0,
        tooltip="TODO",
    )
    SkinColorBlue: int = ParamField(
        float, "skinColor_B ", default=0.0,
        tooltip="TODO",
    )
    HairPartsID: int = ParamField(
        float, "hairPartsId", default=0.0,
        tooltip="TODO",
    )
    HairColorRed: int = ParamField(
        float, "hairColor_R ", default=0.0,
        tooltip="TODO",
    )
    HairColorGreen: int = ParamField(
        float, "hairColor_G ", default=0.0,
        tooltip="TODO",
    )
    HairColorBlue: int = ParamField(
        float, "hairColor_B ", default=0.0,
        tooltip="TODO",
    )
    LeftEyePartsID: int = ParamField(
        float, "eyeLPartsId", default=0.0,
        tooltip="TODO",
    )
    LeftEyeColorRed: int = ParamField(
        float, "eyeLColor_R", default=0.0,
        tooltip="TODO",
    )
    LeftEyeColorGreen: int = ParamField(
        float, "eyeLColor_G", default=0.0,
        tooltip="TODO",
    )
    LeftEyeColorBlue: int = ParamField(
        float, "eyeLColor_B", default=0.0,
        tooltip="TODO",
    )
    RightEyePartsID: int = ParamField(
        float, "eyeRPartsId", default=0.0,
        tooltip="TODO",
    )
    RightEyeColorRed: int = ParamField(
        float, "eyeRColor_R", default=0.0,
        tooltip="TODO",
    )
    RightEyeColorGreen: int = ParamField(
        float, "eyeRColor_G", default=0.0,
        tooltip="TODO",
    )
    RightEyeColorBlue: int = ParamField(
        float, "eyeRColor_B", default=0.0,
        tooltip="TODO",
    )
    EyebrowsPartsID: int = ParamField(
        float, "eyebrowPartsId", default=0.0,
        tooltip="TODO",
    )
    EyebrowsColorRed: int = ParamField(
        float, "eyebrowColor_R ", default=0.0,
        tooltip="TODO",
    )
    EyebrowsColorGreen: int = ParamField(
        float, "eyebrowColor_G ", default=0.0,
        tooltip="TODO",
    )
    EyebrowsColorBlue: int = ParamField(
        float, "eyebrowColor_B ", default=0.0,
        tooltip="TODO",
    )
    EyelashesPartsID: int = ParamField(
        float, "eyelashPartsId", default=0.0,
        tooltip="TODO",
    )
    EyelashesColorRed: int = ParamField(
        float, "eyelashColor_R ", default=0.0,
        tooltip="TODO",
    )
    EyelashesColorGreen: int = ParamField(
        float, "eyelashColor_G ", default=0.0,
        tooltip="TODO",
    )
    EyelashesColorBlue: int = ParamField(
        float, "eyelashColor_B ", default=0.0,
        tooltip="TODO",
    )
    BeardPartsID: int = ParamField(
        float, "beardPartsId", default=0.0,
        tooltip="TODO",
    )
    BeardColorRed: int = ParamField(
        float, "beardColor_R ", default=0.0,
        tooltip="TODO",
    )
    BeardColorGreen: int = ParamField(
        float, "beardColor_G ", default=0.0,
        tooltip="TODO",
    )
    BeardColorBlue: int = ParamField(
        float, "beardColor_B ", default=0.0,
        tooltip="TODO",
    )
    AccessoriesPartsID: int = ParamField(
        float, "accessoriesPartsId", default=0.0,
        tooltip="TODO",
    )
    AccessoriesColorRed: int = ParamField(
        float, "accessoriesColor_R ", default=0.0,
        tooltip="TODO",
    )
    AccessoriesColorGreen: int = ParamField(
        float, "accessoriesColor_G ", default=0.0,
        tooltip="TODO",
    )
    AccessoriesColorBlue: int = ParamField(
        float, "accessoriesColor_B ", default=0.0,
        tooltip="TODO",
    )
    DecalPartsID: int = ParamField(
        float, "decalPartsId", default=0.0,
        tooltip="TODO",
    )
    DecalColorRed: int = ParamField(
        float, "decalColor_R ", default=0.0,
        tooltip="TODO",
    )
    DecalColorGreen: int = ParamField(
        float, "decalColor_G ", default=0.0,
        tooltip="TODO",
    )
    DecalColorBlue: int = ParamField(
        float, "decalColor_B ", default=0.0,
        tooltip="TODO",
    )
    DecalPositionX: int = ParamField(
        float, "decalPosX", default=0.0,
        tooltip="TODO",
    )
    DecalPositionY: int = ParamField(
        float, "decalPosY", default=0.0,
        tooltip="TODO",
    )
    DecalAngle: int = ParamField(
        float, "decalAngle", default=0.0,
        tooltip="TODO",
    )
    DecalScale: int = ParamField(
        float, "decalScale", default=0.0,
        tooltip="TODO",
    )
    HeadScale: int = ParamField(
        float, "chrBodyScaleHead", default=0.0,
        tooltip="TODO",
    )
    BreastScale: int = ParamField(
        float, "chrBodyScaleBreast", default=0.0,
        tooltip="TODO",
    )
    AbdomenScale: int = ParamField(
        float, "chrBodyScaleAbdomen", default=0.0,
        tooltip="TODO",
    )
    ArmScale: int = ParamField(
        float, "chrBodyScaleArm", default=0.0,
        tooltip="TODO",
    )
    LegScale: int = ParamField(
        float, "chrBodyScaleLeg", default=0.0,
        tooltip="TODO",
    )
    Age: int = ParamField(
        float, "age", default=0.0,
        tooltip="TODO",
    )
    Gender: int = ParamField(
        float, "gender", default=0.0,
        tooltip="TODO",
    )
    CaricatureGeometry: int = ParamField(
        float, "caricatureGeometry", default=0.0,
        tooltip="TODO",
    )
    CaricatureTexture: int = ParamField(
        float, "caricatureTexture", default=0.0,
        tooltip="TODO",
    )
    GeometryData00: int = ParamField(
        float, "faceGeoData00", default=0.0,
        tooltip="Geometry data point 0.",
    )
    GeometryData01: int = ParamField(
        float, "faceGeoData01", default=0.0,
        tooltip="Geometry data point 1.",
    )
    GeometryData02: int = ParamField(
        float, "faceGeoData02", default=0.0,
        tooltip="Geometry data point 2.",
    )
    GeometryData03: int = ParamField(
        float, "faceGeoData03", default=0.0,
        tooltip="Geometry data point 3.",
    )
    GeometryData04: int = ParamField(
        float, "faceGeoData04", default=0.0,
        tooltip="Geometry data point 4.",
    )
    GeometryData05: int = ParamField(
        float, "faceGeoData05", default=0.0,
        tooltip="Geometry data point 5.",
    )
    GeometryData06: int = ParamField(
        float, "faceGeoData06", default=0.0,
        tooltip="Geometry data point 6.",
    )
    GeometryData07: int = ParamField(
        float, "faceGeoData07", default=0.0,
        tooltip="Geometry data point 7.",
    )
    GeometryData08: int = ParamField(
        float, "faceGeoData08", default=0.0,
        tooltip="Geometry data point 8.",
    )
    GeometryData09: int = ParamField(
        float, "faceGeoData09", default=0.0,
        tooltip="Geometry data point 9.",
    )
    GeometryData10: int = ParamField(
        float, "faceGeoData10", default=0.0,
        tooltip="Geometry data point 10.",
    )
    GeometryData11: int = ParamField(
        float, "faceGeoData11", default=0.0,
        tooltip="Geometry data point 11.",
    )
    GeometryData12: int = ParamField(
        float, "faceGeoData12", default=0.0,
        tooltip="Geometry data point 12.",
    )
    GeometryData13: int = ParamField(
        float, "faceGeoData13", default=0.0,
        tooltip="Geometry data point 13.",
    )
    GeometryData14: int = ParamField(
        float, "faceGeoData14", default=0.0,
        tooltip="Geometry data point 14.",
    )
    GeometryData15: int = ParamField(
        float, "faceGeoData15", default=0.0,
        tooltip="Geometry data point 15.",
    )
    GeometryData16: int = ParamField(
        float, "faceGeoData16", default=0.0,
        tooltip="Geometry data point 16.",
    )
    GeometryData17: int = ParamField(
        float, "faceGeoData17", default=0.0,
        tooltip="Geometry data point 17.",
    )
    GeometryData18: int = ParamField(
        float, "faceGeoData18", default=0.0,
        tooltip="Geometry data point 18.",
    )
    GeometryData19: int = ParamField(
        float, "faceGeoData19", default=0.0,
        tooltip="Geometry data point 19.",
    )
    GeometryData20: int = ParamField(
        float, "faceGeoData20", default=0.0,
        tooltip="Geometry data point 20.",
    )
    GeometryData21: int = ParamField(
        float, "faceGeoData21", default=0.0,
        tooltip="Geometry data point 21.",
    )
    GeometryData22: int = ParamField(
        float, "faceGeoData22", default=0.0,
        tooltip="Geometry data point 22.",
    )
    GeometryData23: int = ParamField(
        float, "faceGeoData23", default=0.0,
        tooltip="Geometry data point 23.",
    )
    GeometryData24: int = ParamField(
        float, "faceGeoData24", default=0.0,
        tooltip="Geometry data point 24.",
    )
    GeometryData25: int = ParamField(
        float, "faceGeoData25", default=0.0,
        tooltip="Geometry data point 25.",
    )
    GeometryData26: int = ParamField(
        float, "faceGeoData26", default=0.0,
        tooltip="Geometry data point 26.",
    )
    GeometryData27: int = ParamField(
        float, "faceGeoData27", default=0.0,
        tooltip="Geometry data point 27.",
    )
    GeometryData28: int = ParamField(
        float, "faceGeoData28", default=0.0,
        tooltip="Geometry data point 28.",
    )
    GeometryData29: int = ParamField(
        float, "faceGeoData29", default=0.0,
        tooltip="Geometry data point 29.",
    )
    GeometryData30: int = ParamField(
        float, "faceGeoData30", default=0.0,
        tooltip="Geometry data point 30.",
    )
    GeometryData31: int = ParamField(
        float, "faceGeoData31", default=0.0,
        tooltip="Geometry data point 31.",
    )
    GeometryData32: int = ParamField(
        float, "faceGeoData32", default=0.0,
        tooltip="Geometry data point 32.",
    )
    GeometryData33: int = ParamField(
        float, "faceGeoData33", default=0.0,
        tooltip="Geometry data point 33.",
    )
    GeometryData34: int = ParamField(
        float, "faceGeoData34", default=0.0,
        tooltip="Geometry data point 34.",
    )
    GeometryData35: int = ParamField(
        float, "faceGeoData35", default=0.0,
        tooltip="Geometry data point 35.",
    )
    GeometryData36: int = ParamField(
        float, "faceGeoData36", default=0.0,
        tooltip="Geometry data point 36.",
    )
    GeometryData37: int = ParamField(
        float, "faceGeoData37", default=0.0,
        tooltip="Geometry data point 37.",
    )
    GeometryData38: int = ParamField(
        float, "faceGeoData38", default=0.0,
        tooltip="Geometry data point 38.",
    )
    GeometryData39: int = ParamField(
        float, "faceGeoData39", default=0.0,
        tooltip="Geometry data point 39.",
    )
    GeometryData40: int = ParamField(
        float, "faceGeoData40", default=0.0,
        tooltip="Geometry data point 40.",
    )
    GeometryData41: int = ParamField(
        float, "faceGeoData41", default=0.0,
        tooltip="Geometry data point 41.",
    )
    GeometryData42: int = ParamField(
        float, "faceGeoData42", default=0.0,
        tooltip="Geometry data point 42.",
    )
    GeometryData43: int = ParamField(
        float, "faceGeoData43", default=0.0,
        tooltip="Geometry data point 43.",
    )
    GeometryData44: int = ParamField(
        float, "faceGeoData44", default=0.0,
        tooltip="Geometry data point 44.",
    )
    GeometryData45: int = ParamField(
        float, "faceGeoData45", default=0.0,
        tooltip="Geometry data point 45.",
    )
    GeometryData46: int = ParamField(
        float, "faceGeoData46", default=0.0,
        tooltip="Geometry data point 46.",
    )
    GeometryData47: int = ParamField(
        float, "faceGeoData47", default=0.0,
        tooltip="Geometry data point 47.",
    )
    GeometryData48: int = ParamField(
        float, "faceGeoData48", default=0.0,
        tooltip="Geometry data point 48.",
    )
    GeometryData49: int = ParamField(
        float, "faceGeoData49", default=0.0,
        tooltip="Geometry data point 49.",
    )
    GeometryData50: int = ParamField(
        float, "faceGeoData50", default=0.0,
        tooltip="Geometry data point 50.",
    )
    GeometryData51: int = ParamField(
        float, "faceGeoData51", default=0.0,
        tooltip="Geometry data point 51.",
    )
    GeometryData52: int = ParamField(
        float, "faceGeoData52", default=0.0,
        tooltip="Geometry data point 52.",
    )
    GeometryData53: int = ParamField(
        float, "faceGeoData53", default=0.0,
        tooltip="Geometry data point 53.",
    )
    GeometryData54: int = ParamField(
        float, "faceGeoData54", default=0.0,
        tooltip="Geometry data point 54.",
    )
    GeometryData55: int = ParamField(
        float, "faceGeoData55", default=0.0,
        tooltip="Geometry data point 55.",
    )
    GeometryData56: int = ParamField(
        float, "faceGeoData56", default=0.0,
        tooltip="Geometry data point 56.",
    )
    GeometryData57: int = ParamField(
        float, "faceGeoData57", default=0.0,
        tooltip="Geometry data point 57.",
    )
    GeometryData58: int = ParamField(
        float, "faceGeoData58", default=0.0,
        tooltip="Geometry data point 58.",
    )
    GeometryData59: int = ParamField(
        float, "faceGeoData59", default=0.0,
        tooltip="Geometry data point 59.",
    )
    GeometryData60: int = ParamField(
        float, "faceGeoData60", default=0.0,
        tooltip="Geometry data point 60.",
    )
    TextureData00: int = ParamField(
        float, "faceTexData00", default=0.0,
        tooltip="Texture data point 0.",
    )
    TextureData01: int = ParamField(
        float, "faceTexData01", default=0.0,
        tooltip="Texture data point 1.",
    )
    TextureData02: int = ParamField(
        float, "faceTexData02", default=0.0,
        tooltip="Texture data point 2.",
    )
    TextureData03: int = ParamField(
        float, "faceTexData03", default=0.0,
        tooltip="Texture data point 3.",
    )
    TextureData04: int = ParamField(
        float, "faceTexData04", default=0.0,
        tooltip="Texture data point 4.",
    )
    TextureData05: int = ParamField(
        float, "faceTexData05", default=0.0,
        tooltip="Texture data point 5.",
    )
    TextureData06: int = ParamField(
        float, "faceTexData06", default=0.0,
        tooltip="Texture data point 6.",
    )
    TextureData07: int = ParamField(
        float, "faceTexData07", default=0.0,
        tooltip="Texture data point 7.",
    )
    TextureData08: int = ParamField(
        float, "faceTexData08", default=0.0,
        tooltip="Texture data point 8.",
    )
    TextureData09: int = ParamField(
        float, "faceTexData09", default=0.0,
        tooltip="Texture data point 9.",
    )
    TextureData10: int = ParamField(
        float, "faceTexData10", default=0.0,
        tooltip="Texture data point 10.",
    )
    TextureData11: int = ParamField(
        float, "faceTexData11", default=0.0,
        tooltip="Texture data point 11.",
    )
    TextureData12: int = ParamField(
        float, "faceTexData12", default=0.0,
        tooltip="Texture data point 12.",
    )
    TextureData13: int = ParamField(
        float, "faceTexData13", default=0.0,
        tooltip="Texture data point 13.",
    )
    TextureData14: int = ParamField(
        float, "faceTexData14", default=0.0,
        tooltip="Texture data point 14.",
    )
    TextureData15: int = ParamField(
        float, "faceTexData15", default=0.0,
        tooltip="Texture data point 15.",
    )
    TextureData16: int = ParamField(
        float, "faceTexData16", default=0.0,
        tooltip="Texture data point 16.",
    )
    TextureData17: int = ParamField(
        float, "faceTexData17", default=0.0,
        tooltip="Texture data point 17.",
    )
    TextureData18: int = ParamField(
        float, "faceTexData18", default=0.0,
        tooltip="Texture data point 18.",
    )
    TextureData19: int = ParamField(
        float, "faceTexData19", default=0.0,
        tooltip="Texture data point 19.",
    )
    TextureData20: int = ParamField(
        float, "faceTexData20", default=0.0,
        tooltip="Texture data point 20.",
    )
    TextureData21: int = ParamField(
        float, "faceTexData21", default=0.0,
        tooltip="Texture data point 21.",
    )
    TextureData22: int = ParamField(
        float, "faceTexData22", default=0.0,
        tooltip="Texture data point 22.",
    )
    TextureData23: int = ParamField(
        float, "faceTexData23", default=0.0,
        tooltip="Texture data point 23.",
    )
    TextureData24: int = ParamField(
        float, "faceTexData24", default=0.0,
        tooltip="Texture data point 24.",
    )
    TextureData25: int = ParamField(
        float, "faceTexData25", default=0.0,
        tooltip="Texture data point 25.",
    )
    TextureData26: int = ParamField(
        float, "faceTexData26", default=0.0,
        tooltip="Texture data point 26.",
    )
    TextureData27: int = ParamField(
        float, "faceTexData27", default=0.0,
        tooltip="Texture data point 27.",
    )
    TextureData28: int = ParamField(
        float, "faceTexData28", default=0.0,
        tooltip="Texture data point 28.",
    )
    TextureData29: int = ParamField(
        float, "faceTexData29", default=0.0,
        tooltip="Texture data point 29.",
    )
    TextureData30: int = ParamField(
        float, "faceTexData30", default=0.0,
        tooltip="Texture data point 30.",
    )
    TextureData31: int = ParamField(
        float, "faceTexData31", default=0.0,
        tooltip="Texture data point 31.",
    )
    TextureData32: int = ParamField(
        float, "faceTexData32", default=0.0,
        tooltip="Texture data point 32.",
    )
    TextureData33: int = ParamField(
        float, "faceTexData33", default=0.0,
        tooltip="Texture data point 33.",
    )
    TextureData34: int = ParamField(
        float, "faceTexData34", default=0.0,
        tooltip="Texture data point 34.",
    )
    TextureData35: int = ParamField(
        float, "faceTexData35", default=0.0,
        tooltip="Texture data point 35.",
    )
