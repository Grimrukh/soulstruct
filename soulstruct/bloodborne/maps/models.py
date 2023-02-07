__all__ = [
    "MSBModel",
    "MSBMapPieceModel",
    "MSBObjectModel",
    "MSBCharacterModel",
    "MSBItemModel",
    "MSBPlayerModel",
    "MSBCollisionModel",
    "MSBNavmeshModel",
    "MSBOtherModel",
]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.models import BaseMSBModel
from soulstruct.utilities.binary import *

from .enums import MSBModelSubtype


@dataclass(slots=True)
class ModelHeaderStruct(NewBinaryStruct):
    name_offset: long
    _model_type: int
    _model_type_index: int
    sib_path_offset: long
    _instance_count: int
    _pad1: bytes = field(init=False, **BinaryPad(12))


@dataclass(slots=True)
class MSBModel(BaseMSBModel):
    """MSB model entry in Bloodborne."""

    SUPERTYPE_HEADER_STRUCT: tp.ClassVar[tp.Type[NewBinaryStruct]] = ModelHeaderStruct
    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"
    NULL: tp.ClassVar[bytes] = b"\0\0"
    # TODO: Empty sib path different? b"\0\0" * 6 maybe?


class MSBMapPieceModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.MapPiece

    def set_sib_path_from_map_id(self, map_id: int):
        self.sib_path = self.SUBTYPE_ENUM.get_default_sib_path(self.name, map_id)


class MSBObjectModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Object


class MSBCharacterModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Character


class MSBItemModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Item


class MSBPlayerModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Player


class MSBCollisionModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Collision

    def set_sib_path_from_map_id(self, map_id: int):
        self.sib_path = self.SUBTYPE_ENUM.get_default_sib_path(self.name, map_id)


class MSBNavmeshModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Navmesh

    def set_sib_path_from_map_id(self, map_id: int):
        self.sib_path = self.SUBTYPE_ENUM.get_default_sib_path(self.name, map_id)


class MSBOtherModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Other
