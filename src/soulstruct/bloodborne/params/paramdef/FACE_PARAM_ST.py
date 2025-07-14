from __future__ import annotations

__all__ = ["FACE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class FACE_PARAM_ST(ParamRow):
    FacePartsID: int = ParamField(
        uint8, "facePartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    SkinColorRed: int = ParamField(
        uint8, "skinColor_R ", default=128,
        tooltip="TODO",
    )
    SkinColorGreen: int = ParamField(
        uint8, "skinColor_G ", default=128,
        tooltip="TODO",
    )
    SkinColorBlue: int = ParamField(
        uint8, "skinColor_B ", default=128,
        tooltip="TODO",
    )
    HairPartsID: int = ParamField(
        uint8, "hairPartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    HairColorRed: int = ParamField(
        uint8, "hairColor_R ", default=128,
        tooltip="TODO",
    )
    HairColorGreen: int = ParamField(
        uint8, "hairColor_G ", default=128,
        tooltip="TODO",
    )
    HairColorBlue: int = ParamField(
        uint8, "hairColor_B ", default=128,
        tooltip="TODO",
    )
    LeftEyePartsID: int = ParamField(
        uint8, "eyeLPartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    LeftEyeColorRed: int = ParamField(
        uint8, "eyeLColor_R", default=128,
        tooltip="TODO",
    )
    LeftEyeColorGreen: int = ParamField(
        uint8, "eyeLColor_G", default=128,
        tooltip="TODO",
    )
    LeftEyeColorBlue: int = ParamField(
        uint8, "eyeLColor_B", default=128,
        tooltip="TODO",
    )
    RightEyePartsID: int = ParamField(
        uint8, "eyeRPartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    RightEyeColorRed: int = ParamField(
        uint8, "eyeRColor_R", default=128,
        tooltip="TODO",
    )
    RightEyeColorGreen: int = ParamField(
        uint8, "eyeRColor_G", default=128,
        tooltip="TODO",
    )
    RightEyeColorBlue: int = ParamField(
        uint8, "eyeRColor_B", default=128,
        tooltip="TODO",
    )
    EyebrowsPartsID: int = ParamField(
        uint8, "eyebrowPartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    EyebrowsColorRed: int = ParamField(
        uint8, "eyebrowColor_R ", default=128,
        tooltip="TODO",
    )
    EyebrowsColorGreen: int = ParamField(
        uint8, "eyebrowColor_G ", default=128,
        tooltip="TODO",
    )
    EyebrowsColorBlue: int = ParamField(
        uint8, "eyebrowColor_B ", default=128,
        tooltip="TODO",
    )
    EyelashesPartsID: int = ParamField(
        uint8, "eyelashPartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    EyelashesColorRed: int = ParamField(
        uint8, "eyelashColor_R ", default=128,
        tooltip="TODO",
    )
    EyelashesColorGreen: int = ParamField(
        uint8, "eyelashColor_G ", default=128,
        tooltip="TODO",
    )
    EyelashesColorBlue: int = ParamField(
        uint8, "eyelashColor_B ", default=128,
        tooltip="TODO",
    )
    BeardPartsID: int = ParamField(
        uint8, "beardPartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    BeardColorRed: int = ParamField(
        uint8, "beardColor_R ", default=128,
        tooltip="TODO",
    )
    BeardColorGreen: int = ParamField(
        uint8, "beardColor_G ", default=128,
        tooltip="TODO",
    )
    BeardColorBlue: int = ParamField(
        uint8, "beardColor_B ", default=128,
        tooltip="TODO",
    )
    AccessoriesPartsID: int = ParamField(
        uint8, "accessoriesPartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    AccessoriesColorRed: int = ParamField(
        uint8, "accessoriesColor_R ", default=128,
        tooltip="TODO",
    )
    AccessoriesColorGreen: int = ParamField(
        uint8, "accessoriesColor_G ", default=128,
        tooltip="TODO",
    )
    AccessoriesColorBlue: int = ParamField(
        uint8, "accessoriesColor_B ", default=128,
        tooltip="TODO",
    )
    DecalPartsID: int = ParamField(
        uint8, "decalPartsId", game_type=EquipmentModel, default=0,
        tooltip="TODO",
    )
    DecalColorRed: int = ParamField(
        uint8, "decalColor_R ", default=128,
        tooltip="TODO",
    )
    DecalColorGreen: int = ParamField(
        uint8, "decalColor_G ", default=128,
        tooltip="TODO",
    )
    DecalColorBlue: int = ParamField(
        uint8, "decalColor_B ", default=128,
        tooltip="TODO",
    )
    DecalPositionX: int = ParamField(
        uint8, "decalPosX", default=0,
        tooltip="TODO",
    )
    DecalPositionY: int = ParamField(
        uint8, "decalPosY", default=0,
        tooltip="TODO",
    )
    DecalAngle: int = ParamField(
        uint8, "decalAngle", default=0,
        tooltip="TODO",
    )
    DecalScale: int = ParamField(
        uint8, "decalScale", default=0,
        tooltip="TODO",
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
    ArmScale: int = ParamField(
        uint8, "chrBodyScaleArm", default=128,
        tooltip="TODO",
    )
    LegScale: int = ParamField(
        uint8, "chrBodyScaleLeg", default=128,
        tooltip="TODO",
    )
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
