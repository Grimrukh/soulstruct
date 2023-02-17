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
class ModelHeaderStruct(BinaryStruct):
    name_offset: long
    _subtype_int: int
    _subtype_index: int
    sib_path_offset: long
    _instance_count: int
    _pad1: bytes = field(init=False, **BinaryPad(12))


@dataclass(slots=True, eq=False, repr=False)
class MSBModel(BaseMSBModel):
    """MSB model entry in Bloodborne."""

    SUPERTYPE_HEADER_STRUCT: tp.ClassVar[tp.Type[BinaryStruct]] = ModelHeaderStruct
    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"
    NULL: tp.ClassVar[bytes] = b"\0\0"
    # TODO: Empty sib path different? b"\0\0" * 6 maybe?


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPieceModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.MapPiece

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\map\\{map_stem}\\sib\\{name}.sib"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)


@dataclass(slots=True, eq=False, repr=False)
class MSBObjectModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Object

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\obj\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacterModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Character

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\chr\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBItemModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Item


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayerModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Player

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\chr\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBCollisionModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Collision

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\map\\{map_stem}\\hkxwin\\{name}.hkxwin"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)


@dataclass(slots=True, eq=False, repr=False)
class MSBNavmeshModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Navmesh

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\SPRJ\\data\\Model\\map\\{map_stem}\\navimesh\\{name}.SIB"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)


@dataclass(slots=True, eq=False, repr=False)
class MSBOtherModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.Other
