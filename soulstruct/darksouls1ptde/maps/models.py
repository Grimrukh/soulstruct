__all__ = [
    "MSBModel",
    "MSBMapPieceModel",
    "MSBObjectModel",
    "MSBCharacterModel",
    "MSBPlayerModel",
    "MSBCollisionModel",
    "MSBNavmeshModel",
]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.models import BaseMSBModel
from soulstruct.utilities.binary import *

from .enums import MSBModelSubtype


@dataclass(slots=True)
class ModelHeaderStruct(BinaryStruct):
    name_offset: int
    _subtype_int: int
    _subtype_index: int
    sib_path_offset: int
    _instance_count: int
    _pad1: bytes = field(init=False, **BinaryPad(12))


@dataclass(slots=True, eq=False, repr=False)
class MSBModel(BaseMSBModel):
    """MSB model entry in Bloodborne."""

    SUPERTYPE_HEADER_STRUCT: tp.ClassVar[type[BinaryStruct]] = ModelHeaderStruct
    NAME_ENCODING = "shift-jis"
    NULL = b"\0"
    EMPTY_SIB_PATH = b"\0" * 6


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPieceModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.MapPieceModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\sib\\{name}.sib"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)

    def get_model_file_stem(self, map_stem: str):
        if not map_stem:
            raise ValueError("Map stem must be provided to get model file stem of Map Piece.")
        area = map_stem[1:3]
        return f"{self.name}A{area}"

    @classmethod
    def model_file_stem_to_model_name(cls, model_stem: str) -> str:
        return model_stem[:7]


@dataclass(slots=True, eq=False, repr=False)
class MSBObjectModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.ObjectModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\obj\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacterModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.CharacterModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\chr\\{name}\\sib\\{name}.sib"


# UNUSED IN DS1.
# class MSBItemModel(MSBModel):
#     SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.ItemModel


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayerModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.PlayerModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\chr\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBCollisionModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.CollisionModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\hkxwin\\{name}.hkxwin"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)

    def get_model_file_stem(self, map_stem: str):
        if not map_stem:
            raise ValueError("Map stem must be provided to get model file stem of Collision.")
        area = map_stem[1:3]
        return f"{self.name}A{area}"

    @classmethod
    def model_file_stem_to_model_name(cls, model_stem: str) -> str:
        return model_stem[:7]


@dataclass(slots=True, eq=False, repr=False)
class MSBNavmeshModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.NavmeshModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\FRPG\\data\\Model\\map\\{map_stem}\\navimesh\\{name}.SIB"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)

    def get_model_file_stem(self, map_stem: str):
        if not map_stem:
            raise ValueError("Map stem must be provided to get model file stem of Navmesh.")
        area = map_stem[1:3]
        return f"{self.name}A{area}"

    @classmethod
    def model_file_stem_to_model_name(cls, model_stem: str) -> str:
        return model_stem[:7]
