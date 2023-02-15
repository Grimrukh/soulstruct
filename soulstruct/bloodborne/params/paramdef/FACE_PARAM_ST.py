from __future__ import annotations

__all__ = ["FACE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.bloodborne.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class FACE_PARAM_ST(ParamRow):
    FacePartsID: int = ParamField(
        byte, "facePartsId", game_type=EquipmentModel, default=0,
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
        byte, "hairPartsId", game_type=EquipmentModel, default=0,
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
        byte, "eyeLPartsId", game_type=EquipmentModel, default=0,
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
        byte, "eyeRPartsId", game_type=EquipmentModel, default=0,
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
        byte, "eyebrowPartsId", game_type=EquipmentModel, default=0,
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
    EyelashesPartsID: int = ParamField(
        byte, "eyelashPartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    EyelashesColorRed: int = ParamField(
        byte, "eyelashColor_R ", default=128,
        tooltip="TODO",
    )
    EyelashesColorGreen: int = ParamField(
        byte, "eyelashColor_G ", default=128,
        tooltip="TODO",
    )
    EyelashesColorBlue: int = ParamField(
        byte, "eyelashColor_B ", default=128,
        tooltip="TODO",
    )
    BeardPartsID: int = ParamField(
        byte, "beardPartsId", game_type=EquipmentModel, default=0,
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
        byte, "accessoriesPartsId", game_type=EquipmentModel, default=0,
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
        byte, "decalPartsId", game_type=EquipmentModel, default=0,
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
    ArmScale: int = ParamField(
        byte, "chrBodyScaleArm", default=128,
        tooltip="TODO",
    )
    LegScale: int = ParamField(
        byte, "chrBodyScaleLeg", default=128,
        tooltip="TODO",
    )
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
