from __future__ import annotations

__all__ = ["FACE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class FACE_PARAM_ST(ParamRow):
    GeometryData00: int = ParamField(
        uint8, "faceGeoData00", default=0,
        tooltip="Geometry data point 0.",
    )
    GeometryData01: int = ParamField(
        uint8, "faceGeoData01", default=0,
        tooltip="Geometry data point 1.",
    )
    GeometryData02: int = ParamField(
        uint8, "faceGeoData02", default=0,
        tooltip="Geometry data point 2.",
    )
    GeometryData03: int = ParamField(
        uint8, "faceGeoData03", default=0,
        tooltip="Geometry data point 3.",
    )
    GeometryData04: int = ParamField(
        uint8, "faceGeoData04", default=0,
        tooltip="Geometry data point 4.",
    )
    GeometryData05: int = ParamField(
        uint8, "faceGeoData05", default=0,
        tooltip="Geometry data point 5.",
    )
    GeometryData06: int = ParamField(
        uint8, "faceGeoData06", default=0,
        tooltip="Geometry data point 6.",
    )
    GeometryData07: int = ParamField(
        uint8, "faceGeoData07", default=0,
        tooltip="Geometry data point 7.",
    )
    GeometryData08: int = ParamField(
        uint8, "faceGeoData08", default=0,
        tooltip="Geometry data point 8.",
    )
    GeometryData09: int = ParamField(
        uint8, "faceGeoData09", default=0,
        tooltip="Geometry data point 9.",
    )
    GeometryData10: int = ParamField(
        uint8, "faceGeoData10", default=0,
        tooltip="Geometry data point 10.",
    )
    GeometryData11: int = ParamField(
        uint8, "faceGeoData11", default=0,
        tooltip="Geometry data point 11.",
    )
    GeometryData12: int = ParamField(
        uint8, "faceGeoData12", default=0,
        tooltip="Geometry data point 12.",
    )
    GeometryData13: int = ParamField(
        uint8, "faceGeoData13", default=0,
        tooltip="Geometry data point 13.",
    )
    GeometryData14: int = ParamField(
        uint8, "faceGeoData14", default=0,
        tooltip="Geometry data point 14.",
    )
    GeometryData15: int = ParamField(
        uint8, "faceGeoData15", default=0,
        tooltip="Geometry data point 15.",
    )
    GeometryData16: int = ParamField(
        uint8, "faceGeoData16", default=0,
        tooltip="Geometry data point 16.",
    )
    GeometryData17: int = ParamField(
        uint8, "faceGeoData17", default=0,
        tooltip="Geometry data point 17.",
    )
    GeometryData18: int = ParamField(
        uint8, "faceGeoData18", default=0,
        tooltip="Geometry data point 18.",
    )
    GeometryData19: int = ParamField(
        uint8, "faceGeoData19", default=0,
        tooltip="Geometry data point 19.",
    )
    GeometryData20: int = ParamField(
        uint8, "faceGeoData20", default=0,
        tooltip="Geometry data point 20.",
    )
    GeometryData21: int = ParamField(
        uint8, "faceGeoData21", default=0,
        tooltip="Geometry data point 21.",
    )
    GeometryData22: int = ParamField(
        uint8, "faceGeoData22", default=0,
        tooltip="Geometry data point 22.",
    )
    GeometryData23: int = ParamField(
        uint8, "faceGeoData23", default=0,
        tooltip="Geometry data point 23.",
    )
    GeometryData24: int = ParamField(
        uint8, "faceGeoData24", default=0,
        tooltip="Geometry data point 24.",
    )
    GeometryData25: int = ParamField(
        uint8, "faceGeoData25", default=0,
        tooltip="Geometry data point 25.",
    )
    GeometryData26: int = ParamField(
        uint8, "faceGeoData26", default=0,
        tooltip="Geometry data point 26.",
    )
    GeometryData27: int = ParamField(
        uint8, "faceGeoData27", default=0,
        tooltip="Geometry data point 27.",
    )
    GeometryData28: int = ParamField(
        uint8, "faceGeoData28", default=0,
        tooltip="Geometry data point 28.",
    )
    GeometryData29: int = ParamField(
        uint8, "faceGeoData29", default=0,
        tooltip="Geometry data point 29.",
    )
    GeometryData30: int = ParamField(
        uint8, "faceGeoData30", default=0,
        tooltip="Geometry data point 30.",
    )
    GeometryData31: int = ParamField(
        uint8, "faceGeoData31", default=0,
        tooltip="Geometry data point 31.",
    )
    GeometryData32: int = ParamField(
        uint8, "faceGeoData32", default=0,
        tooltip="Geometry data point 32.",
    )
    GeometryData33: int = ParamField(
        uint8, "faceGeoData33", default=0,
        tooltip="Geometry data point 33.",
    )
    GeometryData34: int = ParamField(
        uint8, "faceGeoData34", default=0,
        tooltip="Geometry data point 34.",
    )
    GeometryData35: int = ParamField(
        uint8, "faceGeoData35", default=0,
        tooltip="Geometry data point 35.",
    )
    GeometryData36: int = ParamField(
        uint8, "faceGeoData36", default=0,
        tooltip="Geometry data point 36.",
    )
    GeometryData37: int = ParamField(
        uint8, "faceGeoData37", default=0,
        tooltip="Geometry data point 37.",
    )
    GeometryData38: int = ParamField(
        uint8, "faceGeoData38", default=0,
        tooltip="Geometry data point 38.",
    )
    GeometryData39: int = ParamField(
        uint8, "faceGeoData39", default=0,
        tooltip="Geometry data point 39.",
    )
    GeometryData40: int = ParamField(
        uint8, "faceGeoData40", default=0,
        tooltip="Geometry data point 40.",
    )
    GeometryData41: int = ParamField(
        uint8, "faceGeoData41", default=0,
        tooltip="Geometry data point 41.",
    )
    GeometryData42: int = ParamField(
        uint8, "faceGeoData42", default=0,
        tooltip="Geometry data point 42.",
    )
    GeometryData43: int = ParamField(
        uint8, "faceGeoData43", default=0,
        tooltip="Geometry data point 43.",
    )
    GeometryData44: int = ParamField(
        uint8, "faceGeoData44", default=0,
        tooltip="Geometry data point 44.",
    )
    GeometryData45: int = ParamField(
        uint8, "faceGeoData45", default=0,
        tooltip="Geometry data point 45.",
    )
    GeometryData46: int = ParamField(
        uint8, "faceGeoData46", default=0,
        tooltip="Geometry data point 46.",
    )
    GeometryData47: int = ParamField(
        uint8, "faceGeoData47", default=0,
        tooltip="Geometry data point 47.",
    )
    GeometryData48: int = ParamField(
        uint8, "faceGeoData48", default=0,
        tooltip="Geometry data point 48.",
    )
    GeometryData49: int = ParamField(
        uint8, "faceGeoData49", default=0,
        tooltip="Geometry data point 49.",
    )
    TextureData00: int = ParamField(
        uint8, "faceTexData00", default=0,
        tooltip="Texture data point 0.",
    )
    TextureData01: int = ParamField(
        uint8, "faceTexData01", default=0,
        tooltip="Texture data point 1.",
    )
    TextureData02: int = ParamField(
        uint8, "faceTexData02", default=0,
        tooltip="Texture data point 2.",
    )
    TextureData03: int = ParamField(
        uint8, "faceTexData03", default=0,
        tooltip="Texture data point 3.",
    )
    TextureData04: int = ParamField(
        uint8, "faceTexData04", default=0,
        tooltip="Texture data point 4.",
    )
    TextureData05: int = ParamField(
        uint8, "faceTexData05", default=0,
        tooltip="Texture data point 5.",
    )
    TextureData06: int = ParamField(
        uint8, "faceTexData06", default=0,
        tooltip="Texture data point 6.",
    )
    TextureData07: int = ParamField(
        uint8, "faceTexData07", default=0,
        tooltip="Texture data point 7.",
    )
    TextureData08: int = ParamField(
        uint8, "faceTexData08", default=0,
        tooltip="Texture data point 8.",
    )
    TextureData09: int = ParamField(
        uint8, "faceTexData09", default=0,
        tooltip="Texture data point 9.",
    )
    TextureData10: int = ParamField(
        uint8, "faceTexData10", default=0,
        tooltip="Texture data point 10.",
    )
    TextureData11: int = ParamField(
        uint8, "faceTexData11", default=0,
        tooltip="Texture data point 11.",
    )
    TextureData12: int = ParamField(
        uint8, "faceTexData12", default=0,
        tooltip="Texture data point 12.",
    )
    TextureData13: int = ParamField(
        uint8, "faceTexData13", default=0,
        tooltip="Texture data point 13.",
    )
    TextureData14: int = ParamField(
        uint8, "faceTexData14", default=0,
        tooltip="Texture data point 14.",
    )
    TextureData15: int = ParamField(
        uint8, "faceTexData15", default=0,
        tooltip="Texture data point 15.",
    )
    TextureData16: int = ParamField(
        uint8, "faceTexData16", default=0,
        tooltip="Texture data point 16.",
    )
    TextureData17: int = ParamField(
        uint8, "faceTexData17", default=0,
        tooltip="Texture data point 17.",
    )
    TextureData18: int = ParamField(
        uint8, "faceTexData18", default=0,
        tooltip="Texture data point 18.",
    )
    TextureData19: int = ParamField(
        uint8, "faceTexData19", default=0,
        tooltip="Texture data point 19.",
    )
    TextureData20: int = ParamField(
        uint8, "faceTexData20", default=0,
        tooltip="Texture data point 20.",
    )
    TextureData21: int = ParamField(
        uint8, "faceTexData21", default=0,
        tooltip="Texture data point 21.",
    )
    TextureData22: int = ParamField(
        uint8, "faceTexData22", default=0,
        tooltip="Texture data point 22.",
    )
    TextureData23: int = ParamField(
        uint8, "faceTexData23", default=0,
        tooltip="Texture data point 23.",
    )
    TextureData24: int = ParamField(
        uint8, "faceTexData24", default=0,
        tooltip="Texture data point 24.",
    )
    TextureData25: int = ParamField(
        uint8, "faceTexData25", default=0,
        tooltip="Texture data point 25.",
    )
    TextureData26: int = ParamField(
        uint8, "faceTexData26", default=0,
        tooltip="Texture data point 26.",
    )
    TextureData27: int = ParamField(
        uint8, "faceTexData27", default=0,
        tooltip="Texture data point 27.",
    )
    TextureData28: int = ParamField(
        uint8, "faceTexData28", default=0,
        tooltip="Texture data point 28.",
    )
    TextureData29: int = ParamField(
        uint8, "faceTexData29", default=0,
        tooltip="Texture data point 29.",
    )
    TextureData30: int = ParamField(
        uint8, "faceTexData30", default=0,
        tooltip="Texture data point 30.",
    )
    TextureData31: int = ParamField(
        uint8, "faceTexData31", default=0,
        tooltip="Texture data point 31.",
    )
    TextureData32: int = ParamField(
        uint8, "faceTexData32", default=0,
        tooltip="Texture data point 32.",
    )
    TextureData33: int = ParamField(
        uint8, "faceTexData33", default=0,
        tooltip="Texture data point 33.",
    )
    TextureData34: int = ParamField(
        uint8, "faceTexData34", default=0,
        tooltip="Texture data point 34.",
    )
    TextureData35: int = ParamField(
        uint8, "faceTexData35", default=0,
        tooltip="Texture data point 35.",
    )
    TextureData36: int = ParamField(
        uint8, "faceTexData36", default=0,
        tooltip="Texture data point 36.",
    )
    TextureData37: int = ParamField(
        uint8, "faceTexData37", default=0,
        tooltip="Texture data point 37.",
    )
    TextureData38: int = ParamField(
        uint8, "faceTexData38", default=0,
        tooltip="Texture data point 38.",
    )
    TextureData39: int = ParamField(
        uint8, "faceTexData39", default=0,
        tooltip="Texture data point 39.",
    )
    TextureData40: int = ParamField(
        uint8, "faceTexData40", default=0,
        tooltip="Texture data point 40.",
    )
    TextureData41: int = ParamField(
        uint8, "faceTexData41", default=0,
        tooltip="Texture data point 41.",
    )
    TextureData42: int = ParamField(
        uint8, "faceTexData42", default=0,
        tooltip="Texture data point 42.",
    )
    TextureData43: int = ParamField(
        uint8, "faceTexData43", default=0,
        tooltip="Texture data point 43.",
    )
    TextureData44: int = ParamField(
        uint8, "faceTexData44", default=0,
        tooltip="Texture data point 44.",
    )
    TextureData45: int = ParamField(
        uint8, "faceTexData45", default=0,
        tooltip="Texture data point 45.",
    )
    TextureData46: int = ParamField(
        uint8, "faceTexData46", default=0,
        tooltip="Texture data point 46.",
    )
    TextureData47: int = ParamField(
        uint8, "faceTexData47", default=0,
        tooltip="Texture data point 47.",
    )
    TextureData48: int = ParamField(
        uint8, "faceTexData48", default=0,
        tooltip="Texture data point 48.",
    )
    TextureData49: int = ParamField(
        uint8, "faceTexData49", default=0,
        tooltip="Texture data point 49.",
    )
    HairStyle: int = ParamField(
        uint8, "hairStyle", FACE_PARAM_HAIRSTYLE_TYPE, default=0,
        tooltip="Hairstyle of face.",
    )
    BaseHairColor: int = ParamField(
        uint8, "hairColor_Base ", FACE_PARAM_HAIRCOLOR_TYPE, default=0,
        tooltip="Base hair color of face.",
    )
    HairColorRed: int = ParamField(
        uint8, "hairColor_R ", default=0,
        tooltip="Red channel of hair color (0 to 255).",
    )
    HairColorGreen: int = ParamField(
        uint8, "hairColor_G ", default=0,
        tooltip="Greenchannel of hair color (0 to 255).",
    )
    HairColorBlue: int = ParamField(
        uint8, "hairColor_B ", default=0,
        tooltip="Blue channel of hair color (0 to 255).",
    )
    EyeColorRed: int = ParamField(
        uint8, "eyeColor_R", default=127,
        tooltip="Red channel of eye color (0 to 255).",
    )
    EyeColorGreen: int = ParamField(
        uint8, "eyeColor_G", default=165,
        tooltip="Green channel of eye color (0 to 255).",
    )
    EyeColorBlue: int = ParamField(
        uint8, "eyeColor_B", default=178,
        tooltip="Blue channel of eye color (0 to 255).",
    )
    _Pad0: bytes = ParamPad(20, "pad[20]")
