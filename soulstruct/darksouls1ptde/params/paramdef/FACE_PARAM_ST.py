from __future__ import annotations

__all__ = ["FACE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


class FACE_PARAM_ST(ParamRow):
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
    HairStyle: int = ParamField(
        byte, "hairStyle", FACE_PARAM_HAIRSTYLE_TYPE, default=0,
        tooltip="Hairstyle of face.",
    )
    BaseHairColor: int = ParamField(
        byte, "hairColor_Base ", FACE_PARAM_HAIRCOLOR_TYPE, default=0,
        tooltip="Base hair color of face.",
    )
    HairColorRed: int = ParamField(
        byte, "hairColor_R ", default=0,
        tooltip="Red channel of hair color (0 to 255).",
    )
    HairColorGreen: int = ParamField(
        byte, "hairColor_G ", default=0,
        tooltip="Greenchannel of hair color (0 to 255).",
    )
    HairColorBlue: int = ParamField(
        byte, "hairColor_B ", default=0,
        tooltip="Blue channel of hair color (0 to 255).",
    )
    EyeColorRed: int = ParamField(
        byte, "eyeColor_R", default=127,
        tooltip="Red channel of eye color (0 to 255).",
    )
    EyeColorGreen: int = ParamField(
        byte, "eyeColor_G", default=165,
        tooltip="Green channel of eye color (0 to 255).",
    )
    EyeColorBlue: int = ParamField(
        byte, "eyeColor_B", default=178,
        tooltip="Blue channel of eye color (0 to 255).",
    )
    _Pad0: bytes = ParamPad(20, "pad[20]")
