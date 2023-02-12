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
    FacePartsID: float = ParamField(
        float, "facePartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    SkinColorRed: float = ParamField(
        float, "skinColor_R ", default=0.0,
        tooltip="TODO",
    )
    SkinColorGreen: float = ParamField(
        float, "skinColor_G ", default=0.0,
        tooltip="TODO",
    )
    SkinColorBlue: float = ParamField(
        float, "skinColor_B ", default=0.0,
        tooltip="TODO",
    )
    HairPartsID: float = ParamField(
        float, "hairPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    HairColorRed: float = ParamField(
        float, "hairColor_R ", default=0.0,
        tooltip="TODO",
    )
    HairColorGreen: float = ParamField(
        float, "hairColor_G ", default=0.0,
        tooltip="TODO",
    )
    HairColorBlue: float = ParamField(
        float, "hairColor_B ", default=0.0,
        tooltip="TODO",
    )
    LeftEyePartsID: float = ParamField(
        float, "eyeLPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    LeftEyeColorRed: float = ParamField(
        float, "eyeLColor_R", default=0.0,
        tooltip="TODO",
    )
    LeftEyeColorGreen: float = ParamField(
        float, "eyeLColor_G", default=0.0,
        tooltip="TODO",
    )
    LeftEyeColorBlue: float = ParamField(
        float, "eyeLColor_B", default=0.0,
        tooltip="TODO",
    )
    RightEyePartsID: float = ParamField(
        float, "eyeRPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    RightEyeColorRed: float = ParamField(
        float, "eyeRColor_R", default=0.0,
        tooltip="TODO",
    )
    RightEyeColorGreen: float = ParamField(
        float, "eyeRColor_G", default=0.0,
        tooltip="TODO",
    )
    RightEyeColorBlue: float = ParamField(
        float, "eyeRColor_B", default=0.0,
        tooltip="TODO",
    )
    EyebrowsPartsID: float = ParamField(
        float, "eyebrowPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    EyebrowsColorRed: float = ParamField(
        float, "eyebrowColor_R ", default=0.0,
        tooltip="TODO",
    )
    EyebrowsColorGreen: float = ParamField(
        float, "eyebrowColor_G ", default=0.0,
        tooltip="TODO",
    )
    EyebrowsColorBlue: float = ParamField(
        float, "eyebrowColor_B ", default=0.0,
        tooltip="TODO",
    )
    EyelashesPartsID: float = ParamField(
        float, "eyelashPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    EyelashesColorRed: float = ParamField(
        float, "eyelashColor_R ", default=0.0,
        tooltip="TODO",
    )
    EyelashesColorGreen: float = ParamField(
        float, "eyelashColor_G ", default=0.0,
        tooltip="TODO",
    )
    EyelashesColorBlue: float = ParamField(
        float, "eyelashColor_B ", default=0.0,
        tooltip="TODO",
    )
    BeardPartsID: float = ParamField(
        float, "beardPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    BeardColorRed: float = ParamField(
        float, "beardColor_R ", default=0.0,
        tooltip="TODO",
    )
    BeardColorGreen: float = ParamField(
        float, "beardColor_G ", default=0.0,
        tooltip="TODO",
    )
    BeardColorBlue: float = ParamField(
        float, "beardColor_B ", default=0.0,
        tooltip="TODO",
    )
    AccessoriesPartsID: float = ParamField(
        float, "accessoriesPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    AccessoriesColorRed: float = ParamField(
        float, "accessoriesColor_R ", default=0.0,
        tooltip="TODO",
    )
    AccessoriesColorGreen: float = ParamField(
        float, "accessoriesColor_G ", default=0.0,
        tooltip="TODO",
    )
    AccessoriesColorBlue: float = ParamField(
        float, "accessoriesColor_B ", default=0.0,
        tooltip="TODO",
    )
    DecalPartsID: float = ParamField(
        float, "decalPartsId", game_type=EquipmentModel, default=0.0,
        tooltip="TODO",
    )
    DecalColorRed: float = ParamField(
        float, "decalColor_R ", default=0.0,
        tooltip="TODO",
    )
    DecalColorGreen: float = ParamField(
        float, "decalColor_G ", default=0.0,
        tooltip="TODO",
    )
    DecalColorBlue: float = ParamField(
        float, "decalColor_B ", default=0.0,
        tooltip="TODO",
    )
    DecalPositionX: float = ParamField(
        float, "decalPosX", default=0.0,
        tooltip="TODO",
    )
    DecalPositionY: float = ParamField(
        float, "decalPosY", default=0.0,
        tooltip="TODO",
    )
    DecalAngle: float = ParamField(
        float, "decalAngle", default=0.0,
        tooltip="TODO",
    )
    DecalScale: float = ParamField(
        float, "decalScale", default=0.0,
        tooltip="TODO",
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
