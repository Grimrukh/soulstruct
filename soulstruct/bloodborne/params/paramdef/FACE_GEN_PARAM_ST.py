from __future__ import annotations

__all__ = ["FACE_GEN_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class FACE_GEN_PARAM_ST(ParamRow):
    GeometryData00: int = ParamField(
        byte, "faceGeoData00", default=0,
        tooltip="Geometry data point 0.",
    )
    GeometryData01: int = ParamField(
        byte, "faceGeoData01", default=0,
        tooltip="Geometry data point 1.",
    )
    GeometryData02: int = ParamField(
        byte, "faceGeoData02", default=0,
        tooltip="Geometry data point 2.",
    )
    GeometryData03: int = ParamField(
        byte, "faceGeoData03", default=0,
        tooltip="Geometry data point 3.",
    )
    GeometryData04: int = ParamField(
        byte, "faceGeoData04", default=0,
        tooltip="Geometry data point 4.",
    )
    GeometryData05: int = ParamField(
        byte, "faceGeoData05", default=0,
        tooltip="Geometry data point 5.",
    )
    GeometryData06: int = ParamField(
        byte, "faceGeoData06", default=0,
        tooltip="Geometry data point 6.",
    )
    GeometryData07: int = ParamField(
        byte, "faceGeoData07", default=0,
        tooltip="Geometry data point 7.",
    )
    GeometryData08: int = ParamField(
        byte, "faceGeoData08", default=0,
        tooltip="Geometry data point 8.",
    )
    GeometryData09: int = ParamField(
        byte, "faceGeoData09", default=0,
        tooltip="Geometry data point 9.",
    )
    GeometryData10: int = ParamField(
        byte, "faceGeoData10", default=0,
        tooltip="Geometry data point 10.",
    )
    GeometryData11: int = ParamField(
        byte, "faceGeoData11", default=0,
        tooltip="Geometry data point 11.",
    )
    GeometryData12: int = ParamField(
        byte, "faceGeoData12", default=0,
        tooltip="Geometry data point 12.",
    )
    GeometryData13: int = ParamField(
        byte, "faceGeoData13", default=0,
        tooltip="Geometry data point 13.",
    )
    GeometryData14: int = ParamField(
        byte, "faceGeoData14", default=0,
        tooltip="Geometry data point 14.",
    )
    GeometryData15: int = ParamField(
        byte, "faceGeoData15", default=0,
        tooltip="Geometry data point 15.",
    )
    GeometryData16: int = ParamField(
        byte, "faceGeoData16", default=0,
        tooltip="Geometry data point 16.",
    )
    GeometryData17: int = ParamField(
        byte, "faceGeoData17", default=0,
        tooltip="Geometry data point 17.",
    )
    GeometryData18: int = ParamField(
        byte, "faceGeoData18", default=0,
        tooltip="Geometry data point 18.",
    )
    GeometryData19: int = ParamField(
        byte, "faceGeoData19", default=0,
        tooltip="Geometry data point 19.",
    )
    GeometryData20: int = ParamField(
        byte, "faceGeoData20", default=0,
        tooltip="Geometry data point 20.",
    )
    GeometryData21: int = ParamField(
        byte, "faceGeoData21", default=0,
        tooltip="Geometry data point 21.",
    )
    GeometryData22: int = ParamField(
        byte, "faceGeoData22", default=0,
        tooltip="Geometry data point 22.",
    )
    GeometryData23: int = ParamField(
        byte, "faceGeoData23", default=0,
        tooltip="Geometry data point 23.",
    )
    GeometryData24: int = ParamField(
        byte, "faceGeoData24", default=0,
        tooltip="Geometry data point 24.",
    )
    GeometryData25: int = ParamField(
        byte, "faceGeoData25", default=0,
        tooltip="Geometry data point 25.",
    )
    GeometryData26: int = ParamField(
        byte, "faceGeoData26", default=0,
        tooltip="Geometry data point 26.",
    )
    GeometryData27: int = ParamField(
        byte, "faceGeoData27", default=0,
        tooltip="Geometry data point 27.",
    )
    GeometryData28: int = ParamField(
        byte, "faceGeoData28", default=0,
        tooltip="Geometry data point 28.",
    )
    GeometryData29: int = ParamField(
        byte, "faceGeoData29", default=0,
        tooltip="Geometry data point 29.",
    )
    GeometryData30: int = ParamField(
        byte, "faceGeoData30", default=0,
        tooltip="Geometry data point 30.",
    )
    GeometryData31: int = ParamField(
        byte, "faceGeoData31", default=0,
        tooltip="Geometry data point 31.",
    )
    GeometryData32: int = ParamField(
        byte, "faceGeoData32", default=0,
        tooltip="Geometry data point 32.",
    )
    GeometryData33: int = ParamField(
        byte, "faceGeoData33", default=0,
        tooltip="Geometry data point 33.",
    )
    GeometryData34: int = ParamField(
        byte, "faceGeoData34", default=0,
        tooltip="Geometry data point 34.",
    )
    GeometryData35: int = ParamField(
        byte, "faceGeoData35", default=0,
        tooltip="Geometry data point 35.",
    )
    GeometryData36: int = ParamField(
        byte, "faceGeoData36", default=0,
        tooltip="Geometry data point 36.",
    )
    GeometryData37: int = ParamField(
        byte, "faceGeoData37", default=0,
        tooltip="Geometry data point 37.",
    )
    GeometryData38: int = ParamField(
        byte, "faceGeoData38", default=0,
        tooltip="Geometry data point 38.",
    )
    GeometryData39: int = ParamField(
        byte, "faceGeoData39", default=0,
        tooltip="Geometry data point 39.",
    )
    GeometryData40: int = ParamField(
        byte, "faceGeoData40", default=0,
        tooltip="Geometry data point 40.",
    )
    GeometryData41: int = ParamField(
        byte, "faceGeoData41", default=0,
        tooltip="Geometry data point 41.",
    )
    GeometryData42: int = ParamField(
        byte, "faceGeoData42", default=0,
        tooltip="Geometry data point 42.",
    )
    GeometryData43: int = ParamField(
        byte, "faceGeoData43", default=0,
        tooltip="Geometry data point 43.",
    )
    GeometryData44: int = ParamField(
        byte, "faceGeoData44", default=0,
        tooltip="Geometry data point 44.",
    )
    GeometryData45: int = ParamField(
        byte, "faceGeoData45", default=0,
        tooltip="Geometry data point 45.",
    )
    GeometryData46: int = ParamField(
        byte, "faceGeoData46", default=0,
        tooltip="Geometry data point 46.",
    )
    GeometryData47: int = ParamField(
        byte, "faceGeoData47", default=0,
        tooltip="Geometry data point 47.",
    )
    GeometryData48: int = ParamField(
        byte, "faceGeoData48", default=0,
        tooltip="Geometry data point 48.",
    )
    GeometryData49: int = ParamField(
        byte, "faceGeoData49", default=0,
        tooltip="Geometry data point 49.",
    )
    TextureData00: int = ParamField(
        byte, "faceTexData00", default=0,
        tooltip="Texture data point 0.",
    )
    TextureData01: int = ParamField(
        byte, "faceTexData01", default=0,
        tooltip="Texture data point 1.",
    )
    TextureData02: int = ParamField(
        byte, "faceTexData02", default=0,
        tooltip="Texture data point 2.",
    )
    TextureData03: int = ParamField(
        byte, "faceTexData03", default=0,
        tooltip="Texture data point 3.",
    )
    TextureData04: int = ParamField(
        byte, "faceTexData04", default=0,
        tooltip="Texture data point 4.",
    )
    TextureData05: int = ParamField(
        byte, "faceTexData05", default=0,
        tooltip="Texture data point 5.",
    )
    TextureData06: int = ParamField(
        byte, "faceTexData06", default=0,
        tooltip="Texture data point 6.",
    )
    TextureData07: int = ParamField(
        byte, "faceTexData07", default=0,
        tooltip="Texture data point 7.",
    )
    TextureData08: int = ParamField(
        byte, "faceTexData08", default=0,
        tooltip="Texture data point 8.",
    )
    TextureData09: int = ParamField(
        byte, "faceTexData09", default=0,
        tooltip="Texture data point 9.",
    )
    TextureData10: int = ParamField(
        byte, "faceTexData10", default=0,
        tooltip="Texture data point 10.",
    )
    TextureData11: int = ParamField(
        byte, "faceTexData11", default=0,
        tooltip="Texture data point 11.",
    )
    TextureData12: int = ParamField(
        byte, "faceTexData12", default=0,
        tooltip="Texture data point 12.",
    )
    TextureData13: int = ParamField(
        byte, "faceTexData13", default=0,
        tooltip="Texture data point 13.",
    )
    TextureData14: int = ParamField(
        byte, "faceTexData14", default=0,
        tooltip="Texture data point 14.",
    )
    TextureData15: int = ParamField(
        byte, "faceTexData15", default=0,
        tooltip="Texture data point 15.",
    )
    TextureData16: int = ParamField(
        byte, "faceTexData16", default=0,
        tooltip="Texture data point 16.",
    )
    TextureData17: int = ParamField(
        byte, "faceTexData17", default=0,
        tooltip="Texture data point 17.",
    )
    TextureData18: int = ParamField(
        byte, "faceTexData18", default=0,
        tooltip="Texture data point 18.",
    )
    TextureData19: int = ParamField(
        byte, "faceTexData19", default=0,
        tooltip="Texture data point 19.",
    )
    TextureData20: int = ParamField(
        byte, "faceTexData20", default=0,
        tooltip="Texture data point 20.",
    )
    TextureData21: int = ParamField(
        byte, "faceTexData21", default=0,
        tooltip="Texture data point 21.",
    )
    TextureData22: int = ParamField(
        byte, "faceTexData22", default=0,
        tooltip="Texture data point 22.",
    )
    TextureData23: int = ParamField(
        byte, "faceTexData23", default=0,
        tooltip="Texture data point 23.",
    )
    TextureData24: int = ParamField(
        byte, "faceTexData24", default=0,
        tooltip="Texture data point 24.",
    )
    TextureData25: int = ParamField(
        byte, "faceTexData25", default=0,
        tooltip="Texture data point 25.",
    )
    TextureData26: int = ParamField(
        byte, "faceTexData26", default=0,
        tooltip="Texture data point 26.",
    )
    TextureData27: int = ParamField(
        byte, "faceTexData27", default=0,
        tooltip="Texture data point 27.",
    )
    TextureData28: int = ParamField(
        byte, "faceTexData28", default=0,
        tooltip="Texture data point 28.",
    )
    TextureData29: int = ParamField(
        byte, "faceTexData29", default=0,
        tooltip="Texture data point 29.",
    )
    TextureData30: int = ParamField(
        byte, "faceTexData30", default=0,
        tooltip="Texture data point 30.",
    )
    TextureData31: int = ParamField(
        byte, "faceTexData31", default=0,
        tooltip="Texture data point 31.",
    )
    TextureData32: int = ParamField(
        byte, "faceTexData32", default=0,
        tooltip="Texture data point 32.",
    )
    TextureData33: int = ParamField(
        byte, "faceTexData33", default=0,
        tooltip="Texture data point 33.",
    )
    TextureData34: int = ParamField(
        byte, "faceTexData34", default=0,
        tooltip="Texture data point 34.",
    )
    TextureData35: int = ParamField(
        byte, "faceTexData35", default=0,
        tooltip="Texture data point 35.",
    )
    TextureData36: int = ParamField(
        byte, "faceTexData36", default=0,
        tooltip="Texture data point 36.",
    )
    TextureData37: int = ParamField(
        byte, "faceTexData37", default=0,
        tooltip="Texture data point 37.",
    )
    TextureData38: int = ParamField(
        byte, "faceTexData38", default=0,
        tooltip="Texture data point 38.",
    )
    TextureData39: int = ParamField(
        byte, "faceTexData39", default=0,
        tooltip="Texture data point 39.",
    )
    TextureData40: int = ParamField(
        byte, "faceTexData40", default=0,
        tooltip="Texture data point 40.",
    )
    TextureData41: int = ParamField(
        byte, "faceTexData41", default=0,
        tooltip="Texture data point 41.",
    )
    TextureData42: int = ParamField(
        byte, "faceTexData42", default=0,
        tooltip="Texture data point 42.",
    )
    TextureData43: int = ParamField(
        byte, "faceTexData43", default=0,
        tooltip="Texture data point 43.",
    )
    TextureData44: int = ParamField(
        byte, "faceTexData44", default=0,
        tooltip="Texture data point 44.",
    )
    TextureData45: int = ParamField(
        byte, "faceTexData45", default=0,
        tooltip="Texture data point 45.",
    )
    TextureData46: int = ParamField(
        byte, "faceTexData46", default=0,
        tooltip="Texture data point 46.",
    )
    TextureData47: int = ParamField(
        byte, "faceTexData47", default=0,
        tooltip="Texture data point 47.",
    )
    TextureData48: int = ParamField(
        byte, "faceTexData48", default=0,
        tooltip="Texture data point 48.",
    )
    TextureData49: int = ParamField(
        byte, "faceTexData49", default=0,
        tooltip="Texture data point 49.",
    )
    FacePartsID: int = ParamField(
        byte, "facePartsId", default=0,
        tooltip="TODO",
    )
    SkinColorRed: int = ParamField(
        byte, "skinColor_R ", default=128,
        tooltip="TODO",
    )
    SkinColorGreen: int = ParamField(
        byte, "skinColor_G ", default=128,
        tooltip="TODO",
    )
    SkinColorBlue: int = ParamField(
        byte, "skinColor_B ", default=128,
        tooltip="TODO",
    )
    HairPartsID: int = ParamField(
        byte, "hairPartsId", default=0,
        tooltip="TODO",
    )
    HairColorRed: int = ParamField(
        byte, "hairColor_R ", default=128,
        tooltip="TODO",
    )
    HairColorGreen: int = ParamField(
        byte, "hairColor_G ", default=128,
        tooltip="TODO",
    )
    HairColorBlue: int = ParamField(
        byte, "hairColor_B ", default=128,
        tooltip="TODO",
    )
    LeftEyePartsID: int = ParamField(
        byte, "eyeLPartsId", default=0,
        tooltip="TODO",
    )
    LeftEyeColorRed: int = ParamField(
        byte, "eyeLColor_R", default=128,
        tooltip="TODO",
    )
    LeftEyeColorGreen: int = ParamField(
        byte, "eyeLColor_G", default=128,
        tooltip="TODO",
    )
    LeftEyeColorBlue: int = ParamField(
        byte, "eyeLColor_B", default=128,
        tooltip="TODO",
    )
    RightEyePartsID: int = ParamField(
        byte, "eyeRPartsId", default=0,
        tooltip="TODO",
    )
    RightEyeColorRed: int = ParamField(
        byte, "eyeRColor_R", default=128,
        tooltip="TODO",
    )
    RightEyeColorGreen: int = ParamField(
        byte, "eyeRColor_G", default=128,
        tooltip="TODO",
    )
    RightEyeColorBlue: int = ParamField(
        byte, "eyeRColor_B", default=128,
        tooltip="TODO",
    )
    EyebrowsPartsID: int = ParamField(
        byte, "eyebrowPartsId", default=0,
        tooltip="TODO",
    )
    EyebrowsColorRed: int = ParamField(
        byte, "eyebrowColor_R ", default=128,
        tooltip="TODO",
    )
    EyebrowsColorGreen: int = ParamField(
        byte, "eyebrowColor_G ", default=128,
        tooltip="TODO",
    )
    EyebrowsColorBlue: int = ParamField(
        byte, "eyebrowColor_B ", default=128,
        tooltip="TODO",
    )
    BeardPartsID: int = ParamField(
        byte, "beardPartsId", default=0,
        tooltip="TODO",
    )
    BeardColorRed: int = ParamField(
        byte, "beardColor_R ", default=128,
        tooltip="TODO",
    )
    BeardColorGreen: int = ParamField(
        byte, "beardColor_G ", default=128,
        tooltip="TODO",
    )
    BeardColorBlue: int = ParamField(
        byte, "beardColor_B ", default=128,
        tooltip="TODO",
    )
    AccessoriesPartsID: int = ParamField(
        byte, "accessoriesPartsId", default=0,
        tooltip="TODO",
    )
    AccessoriesColorRed: int = ParamField(
        byte, "accessoriesColor_R ", default=128,
        tooltip="TODO",
    )
    AccessoriesColorGreen: int = ParamField(
        byte, "accessoriesColor_G ", default=128,
        tooltip="TODO",
    )
    AccessoriesColorBlue: int = ParamField(
        byte, "accessoriesColor_B ", default=128,
        tooltip="TODO",
    )
    DecalPartsID: int = ParamField(
        byte, "decalPartsId", default=0,
        tooltip="TODO",
    )
    DecalColorRed: int = ParamField(
        byte, "decalColor_R ", default=128,
        tooltip="TODO",
    )
    DecalColorGreen: int = ParamField(
        byte, "decalColor_G ", default=128,
        tooltip="TODO",
    )
    DecalColorBlue: int = ParamField(
        byte, "decalColor_B ", default=128,
        tooltip="TODO",
    )
    DecalPositionX: int = ParamField(
        byte, "decalPosX", default=0,
        tooltip="TODO",
    )
    DecalPositionY: int = ParamField(
        byte, "decalPosY", default=0,
        tooltip="TODO",
    )
    DecalAngle: int = ParamField(
        byte, "decalAngle", default=0,
        tooltip="TODO",
    )
    DecalScale: int = ParamField(
        byte, "decalScale", default=0,
        tooltip="TODO",
    )
