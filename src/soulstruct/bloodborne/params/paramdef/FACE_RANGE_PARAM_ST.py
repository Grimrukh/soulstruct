from __future__ import annotations

__all__ = ["FACE_RANGE_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class FACE_RANGE_PARAM_ST(ParamRow):
    FacePartsID: float = ParamField(
        float32, "facePartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    SkinColorRed: float = ParamField(
        float32, "skinColor_R ", default=0.0,
        tooltip="TODO",
    )
    SkinColorGreen: float = ParamField(
        float32, "skinColor_G ", default=0.0,
        tooltip="TODO",
    )
    SkinColorBlue: float = ParamField(
        float32, "skinColor_B ", default=0.0,
        tooltip="TODO",
    )
    HairPartsID: float = ParamField(
        float32, "hairPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    HairColorRed: float = ParamField(
        float32, "hairColor_R ", default=0.0,
        tooltip="TODO",
    )
    HairColorGreen: float = ParamField(
        float32, "hairColor_G ", default=0.0,
        tooltip="TODO",
    )
    HairColorBlue: float = ParamField(
        float32, "hairColor_B ", default=0.0,
        tooltip="TODO",
    )
    LeftEyePartsID: float = ParamField(
        float32, "eyeLPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    LeftEyeColorRed: float = ParamField(
        float32, "eyeLColor_R", default=0.0,
        tooltip="TODO",
    )
    LeftEyeColorGreen: float = ParamField(
        float32, "eyeLColor_G", default=0.0,
        tooltip="TODO",
    )
    LeftEyeColorBlue: float = ParamField(
        float32, "eyeLColor_B", default=0.0,
        tooltip="TODO",
    )
    RightEyePartsID: float = ParamField(
        float32, "eyeRPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    RightEyeColorRed: float = ParamField(
        float32, "eyeRColor_R", default=0.0,
        tooltip="TODO",
    )
    RightEyeColorGreen: float = ParamField(
        float32, "eyeRColor_G", default=0.0,
        tooltip="TODO",
    )
    RightEyeColorBlue: float = ParamField(
        float32, "eyeRColor_B", default=0.0,
        tooltip="TODO",
    )
    EyebrowsPartsID: float = ParamField(
        float32, "eyebrowPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    EyebrowsColorRed: float = ParamField(
        float32, "eyebrowColor_R ", default=0.0,
        tooltip="TODO",
    )
    EyebrowsColorGreen: float = ParamField(
        float32, "eyebrowColor_G ", default=0.0,
        tooltip="TODO",
    )
    EyebrowsColorBlue: float = ParamField(
        float32, "eyebrowColor_B ", default=0.0,
        tooltip="TODO",
    )
    EyelashesPartsID: float = ParamField(
        float32, "eyelashPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    EyelashesColorRed: float = ParamField(
        float32, "eyelashColor_R ", default=0.0,
        tooltip="TODO",
    )
    EyelashesColorGreen: float = ParamField(
        float32, "eyelashColor_G ", default=0.0,
        tooltip="TODO",
    )
    EyelashesColorBlue: float = ParamField(
        float32, "eyelashColor_B ", default=0.0,
        tooltip="TODO",
    )
    BeardPartsID: float = ParamField(
        float32, "beardPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    BeardColorRed: float = ParamField(
        float32, "beardColor_R ", default=0.0,
        tooltip="TODO",
    )
    BeardColorGreen: float = ParamField(
        float32, "beardColor_G ", default=0.0,
        tooltip="TODO",
    )
    BeardColorBlue: float = ParamField(
        float32, "beardColor_B ", default=0.0,
        tooltip="TODO",
    )
    AccessoriesPartsID: float = ParamField(
        float32, "accessoriesPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    AccessoriesColorRed: float = ParamField(
        float32, "accessoriesColor_R ", default=0.0,
        tooltip="TODO",
    )
    AccessoriesColorGreen: float = ParamField(
        float32, "accessoriesColor_G ", default=0.0,
        tooltip="TODO",
    )
    AccessoriesColorBlue: float = ParamField(
        float32, "accessoriesColor_B ", default=0.0,
        tooltip="TODO",
    )
    DecalPartsID: float = ParamField(
        float32, "decalPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    DecalColorRed: float = ParamField(
        float32, "decalColor_R ", default=0.0,
        tooltip="TODO",
    )
    DecalColorGreen: float = ParamField(
        float32, "decalColor_G ", default=0.0,
        tooltip="TODO",
    )
    DecalColorBlue: float = ParamField(
        float32, "decalColor_B ", default=0.0,
        tooltip="TODO",
    )
    DecalPositionX: float = ParamField(
        float32, "decalPosX", default=0.0,
        tooltip="TODO",
    )
    DecalPositionY: float = ParamField(
        float32, "decalPosY", default=0.0,
        tooltip="TODO",
    )
    DecalAngle: float = ParamField(
        float32, "decalAngle", default=0.0,
        tooltip="TODO",
    )
    DecalScale: float = ParamField(
        float32, "decalScale", default=0.0,
        tooltip="TODO",
    )
    HeadScale: float = ParamField(
        float32, "chrBodyScaleHead", default=0.0,
        tooltip="TODO",
    )
    BreastScale: float = ParamField(
        float32, "chrBodyScaleBreast", default=0.0,
        tooltip="TODO",
    )
    AbdomenScale: float = ParamField(
        float32, "chrBodyScaleAbdomen", default=0.0,
        tooltip="TODO",
    )
    ArmScale: float = ParamField(
        float32, "chrBodyScaleArm", default=0.0,
        tooltip="TODO",
    )
    LegScale: float = ParamField(
        float32, "chrBodyScaleLeg", default=0.0,
        tooltip="TODO",
    )
    Age: float = ParamField(
        float32, "age", default=0.0,
        tooltip="TODO",
    )
    Gender: float = ParamField(
        float32, "gender", default=0.0,
        tooltip="TODO",
    )
    CaricatureGeometry: float = ParamField(
        float32, "caricatureGeometry", default=0.0,
        tooltip="TODO",
    )
    CaricatureTexture: float = ParamField(
        float32, "caricatureTexture", default=0.0,
        tooltip="TODO",
    )
    GeometryData00: float = ParamField(
        float32, "faceGeoData00", default=0.0,
        tooltip="Geometry data point 0.",
    )
    GeometryData01: float = ParamField(
        float32, "faceGeoData01", default=0.0,
        tooltip="Geometry data point 1.",
    )
    GeometryData02: float = ParamField(
        float32, "faceGeoData02", default=0.0,
        tooltip="Geometry data point 2.",
    )
    GeometryData03: float = ParamField(
        float32, "faceGeoData03", default=0.0,
        tooltip="Geometry data point 3.",
    )
    GeometryData04: float = ParamField(
        float32, "faceGeoData04", default=0.0,
        tooltip="Geometry data point 4.",
    )
    GeometryData05: float = ParamField(
        float32, "faceGeoData05", default=0.0,
        tooltip="Geometry data point 5.",
    )
    GeometryData06: float = ParamField(
        float32, "faceGeoData06", default=0.0,
        tooltip="Geometry data point 6.",
    )
    GeometryData07: float = ParamField(
        float32, "faceGeoData07", default=0.0,
        tooltip="Geometry data point 7.",
    )
    GeometryData08: float = ParamField(
        float32, "faceGeoData08", default=0.0,
        tooltip="Geometry data point 8.",
    )
    GeometryData09: float = ParamField(
        float32, "faceGeoData09", default=0.0,
        tooltip="Geometry data point 9.",
    )
    GeometryData10: float = ParamField(
        float32, "faceGeoData10", default=0.0,
        tooltip="Geometry data point 10.",
    )
    GeometryData11: float = ParamField(
        float32, "faceGeoData11", default=0.0,
        tooltip="Geometry data point 11.",
    )
    GeometryData12: float = ParamField(
        float32, "faceGeoData12", default=0.0,
        tooltip="Geometry data point 12.",
    )
    GeometryData13: float = ParamField(
        float32, "faceGeoData13", default=0.0,
        tooltip="Geometry data point 13.",
    )
    GeometryData14: float = ParamField(
        float32, "faceGeoData14", default=0.0,
        tooltip="Geometry data point 14.",
    )
    GeometryData15: float = ParamField(
        float32, "faceGeoData15", default=0.0,
        tooltip="Geometry data point 15.",
    )
    GeometryData16: float = ParamField(
        float32, "faceGeoData16", default=0.0,
        tooltip="Geometry data point 16.",
    )
    GeometryData17: float = ParamField(
        float32, "faceGeoData17", default=0.0,
        tooltip="Geometry data point 17.",
    )
    GeometryData18: float = ParamField(
        float32, "faceGeoData18", default=0.0,
        tooltip="Geometry data point 18.",
    )
    GeometryData19: float = ParamField(
        float32, "faceGeoData19", default=0.0,
        tooltip="Geometry data point 19.",
    )
    GeometryData20: float = ParamField(
        float32, "faceGeoData20", default=0.0,
        tooltip="Geometry data point 20.",
    )
    GeometryData21: float = ParamField(
        float32, "faceGeoData21", default=0.0,
        tooltip="Geometry data point 21.",
    )
    GeometryData22: float = ParamField(
        float32, "faceGeoData22", default=0.0,
        tooltip="Geometry data point 22.",
    )
    GeometryData23: float = ParamField(
        float32, "faceGeoData23", default=0.0,
        tooltip="Geometry data point 23.",
    )
    GeometryData24: float = ParamField(
        float32, "faceGeoData24", default=0.0,
        tooltip="Geometry data point 24.",
    )
    GeometryData25: float = ParamField(
        float32, "faceGeoData25", default=0.0,
        tooltip="Geometry data point 25.",
    )
    GeometryData26: float = ParamField(
        float32, "faceGeoData26", default=0.0,
        tooltip="Geometry data point 26.",
    )
    GeometryData27: float = ParamField(
        float32, "faceGeoData27", default=0.0,
        tooltip="Geometry data point 27.",
    )
    GeometryData28: float = ParamField(
        float32, "faceGeoData28", default=0.0,
        tooltip="Geometry data point 28.",
    )
    GeometryData29: float = ParamField(
        float32, "faceGeoData29", default=0.0,
        tooltip="Geometry data point 29.",
    )
    GeometryData30: float = ParamField(
        float32, "faceGeoData30", default=0.0,
        tooltip="Geometry data point 30.",
    )
    GeometryData31: float = ParamField(
        float32, "faceGeoData31", default=0.0,
        tooltip="Geometry data point 31.",
    )
    GeometryData32: float = ParamField(
        float32, "faceGeoData32", default=0.0,
        tooltip="Geometry data point 32.",
    )
    GeometryData33: float = ParamField(
        float32, "faceGeoData33", default=0.0,
        tooltip="Geometry data point 33.",
    )
    GeometryData34: float = ParamField(
        float32, "faceGeoData34", default=0.0,
        tooltip="Geometry data point 34.",
    )
    GeometryData35: float = ParamField(
        float32, "faceGeoData35", default=0.0,
        tooltip="Geometry data point 35.",
    )
    GeometryData36: float = ParamField(
        float32, "faceGeoData36", default=0.0,
        tooltip="Geometry data point 36.",
    )
    GeometryData37: float = ParamField(
        float32, "faceGeoData37", default=0.0,
        tooltip="Geometry data point 37.",
    )
    GeometryData38: float = ParamField(
        float32, "faceGeoData38", default=0.0,
        tooltip="Geometry data point 38.",
    )
    GeometryData39: float = ParamField(
        float32, "faceGeoData39", default=0.0,
        tooltip="Geometry data point 39.",
    )
    GeometryData40: float = ParamField(
        float32, "faceGeoData40", default=0.0,
        tooltip="Geometry data point 40.",
    )
    GeometryData41: float = ParamField(
        float32, "faceGeoData41", default=0.0,
        tooltip="Geometry data point 41.",
    )
    GeometryData42: float = ParamField(
        float32, "faceGeoData42", default=0.0,
        tooltip="Geometry data point 42.",
    )
    GeometryData43: float = ParamField(
        float32, "faceGeoData43", default=0.0,
        tooltip="Geometry data point 43.",
    )
    GeometryData44: float = ParamField(
        float32, "faceGeoData44", default=0.0,
        tooltip="Geometry data point 44.",
    )
    GeometryData45: float = ParamField(
        float32, "faceGeoData45", default=0.0,
        tooltip="Geometry data point 45.",
    )
    GeometryData46: float = ParamField(
        float32, "faceGeoData46", default=0.0,
        tooltip="Geometry data point 46.",
    )
    GeometryData47: float = ParamField(
        float32, "faceGeoData47", default=0.0,
        tooltip="Geometry data point 47.",
    )
    GeometryData48: float = ParamField(
        float32, "faceGeoData48", default=0.0,
        tooltip="Geometry data point 48.",
    )
    GeometryData49: float = ParamField(
        float32, "faceGeoData49", default=0.0,
        tooltip="Geometry data point 49.",
    )
    GeometryData50: float = ParamField(
        float32, "faceGeoData50", default=0.0,
        tooltip="Geometry data point 50.",
    )
    GeometryData51: float = ParamField(
        float32, "faceGeoData51", default=0.0,
        tooltip="Geometry data point 51.",
    )
    GeometryData52: float = ParamField(
        float32, "faceGeoData52", default=0.0,
        tooltip="Geometry data point 52.",
    )
    GeometryData53: float = ParamField(
        float32, "faceGeoData53", default=0.0,
        tooltip="Geometry data point 53.",
    )
    GeometryData54: float = ParamField(
        float32, "faceGeoData54", default=0.0,
        tooltip="Geometry data point 54.",
    )
    GeometryData55: float = ParamField(
        float32, "faceGeoData55", default=0.0,
        tooltip="Geometry data point 55.",
    )
    GeometryData56: float = ParamField(
        float32, "faceGeoData56", default=0.0,
        tooltip="Geometry data point 56.",
    )
    GeometryData57: float = ParamField(
        float32, "faceGeoData57", default=0.0,
        tooltip="Geometry data point 57.",
    )
    GeometryData58: float = ParamField(
        float32, "faceGeoData58", default=0.0,
        tooltip="Geometry data point 58.",
    )
    GeometryData59: float = ParamField(
        float32, "faceGeoData59", default=0.0,
        tooltip="Geometry data point 59.",
    )
    GeometryData60: float = ParamField(
        float32, "faceGeoData60", default=0.0,
        tooltip="Geometry data point 60.",
    )
    TextureData00: float = ParamField(
        float32, "faceTexData00", default=0.0,
        tooltip="Texture data point 0.",
    )
    TextureData01: float = ParamField(
        float32, "faceTexData01", default=0.0,
        tooltip="Texture data point 1.",
    )
    TextureData02: float = ParamField(
        float32, "faceTexData02", default=0.0,
        tooltip="Texture data point 2.",
    )
    TextureData03: float = ParamField(
        float32, "faceTexData03", default=0.0,
        tooltip="Texture data point 3.",
    )
    TextureData04: float = ParamField(
        float32, "faceTexData04", default=0.0,
        tooltip="Texture data point 4.",
    )
    TextureData05: float = ParamField(
        float32, "faceTexData05", default=0.0,
        tooltip="Texture data point 5.",
    )
    TextureData06: float = ParamField(
        float32, "faceTexData06", default=0.0,
        tooltip="Texture data point 6.",
    )
    TextureData07: float = ParamField(
        float32, "faceTexData07", default=0.0,
        tooltip="Texture data point 7.",
    )
    TextureData08: float = ParamField(
        float32, "faceTexData08", default=0.0,
        tooltip="Texture data point 8.",
    )
    TextureData09: float = ParamField(
        float32, "faceTexData09", default=0.0,
        tooltip="Texture data point 9.",
    )
    TextureData10: float = ParamField(
        float32, "faceTexData10", default=0.0,
        tooltip="Texture data point 10.",
    )
    TextureData11: float = ParamField(
        float32, "faceTexData11", default=0.0,
        tooltip="Texture data point 11.",
    )
    TextureData12: float = ParamField(
        float32, "faceTexData12", default=0.0,
        tooltip="Texture data point 12.",
    )
    TextureData13: float = ParamField(
        float32, "faceTexData13", default=0.0,
        tooltip="Texture data point 13.",
    )
    TextureData14: float = ParamField(
        float32, "faceTexData14", default=0.0,
        tooltip="Texture data point 14.",
    )
    TextureData15: float = ParamField(
        float32, "faceTexData15", default=0.0,
        tooltip="Texture data point 15.",
    )
    TextureData16: float = ParamField(
        float32, "faceTexData16", default=0.0,
        tooltip="Texture data point 16.",
    )
    TextureData17: float = ParamField(
        float32, "faceTexData17", default=0.0,
        tooltip="Texture data point 17.",
    )
    TextureData18: float = ParamField(
        float32, "faceTexData18", default=0.0,
        tooltip="Texture data point 18.",
    )
    TextureData19: float = ParamField(
        float32, "faceTexData19", default=0.0,
        tooltip="Texture data point 19.",
    )
    TextureData20: float = ParamField(
        float32, "faceTexData20", default=0.0,
        tooltip="Texture data point 20.",
    )
    TextureData21: float = ParamField(
        float32, "faceTexData21", default=0.0,
        tooltip="Texture data point 21.",
    )
    TextureData22: float = ParamField(
        float32, "faceTexData22", default=0.0,
        tooltip="Texture data point 22.",
    )
    TextureData23: float = ParamField(
        float32, "faceTexData23", default=0.0,
        tooltip="Texture data point 23.",
    )
    TextureData24: float = ParamField(
        float32, "faceTexData24", default=0.0,
        tooltip="Texture data point 24.",
    )
    TextureData25: float = ParamField(
        float32, "faceTexData25", default=0.0,
        tooltip="Texture data point 25.",
    )
    TextureData26: float = ParamField(
        float32, "faceTexData26", default=0.0,
        tooltip="Texture data point 26.",
    )
    TextureData27: float = ParamField(
        float32, "faceTexData27", default=0.0,
        tooltip="Texture data point 27.",
    )
    TextureData28: float = ParamField(
        float32, "faceTexData28", default=0.0,
        tooltip="Texture data point 28.",
    )
    TextureData29: float = ParamField(
        float32, "faceTexData29", default=0.0,
        tooltip="Texture data point 29.",
    )
    TextureData30: float = ParamField(
        float32, "faceTexData30", default=0.0,
        tooltip="Texture data point 30.",
    )
    TextureData31: float = ParamField(
        float32, "faceTexData31", default=0.0,
        tooltip="Texture data point 31.",
    )
    TextureData32: float = ParamField(
        float32, "faceTexData32", default=0.0,
        tooltip="Texture data point 32.",
    )
    TextureData33: float = ParamField(
        float32, "faceTexData33", default=0.0,
        tooltip="Texture data point 33.",
    )
    TextureData34: float = ParamField(
        float32, "faceTexData34", default=0.0,
        tooltip="Texture data point 34.",
    )
    TextureData35: float = ParamField(
        float32, "faceTexData35", default=0.0,
        tooltip="Texture data point 35.",
    )
