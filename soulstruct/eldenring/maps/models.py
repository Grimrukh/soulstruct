from __future__ import annotations

__all__ = [
    "MSBModel",
    "MSBMapPieceModel",
    "MSBCharacterModel",
    "MSBPlayerModel",
    "MSBCollisionModel",
    "MSBAssetModel",
]

import re
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb.models import BaseMSBModel
from soulstruct.utilities.binary import *

from .enums import MSBModelSubtype

if tp.TYPE_CHECKING:
    from soulstruct.base.maps.msb import MSBEntry


@dataclass(slots=True)
class ModelHeaderStruct(BinaryStruct):
    name_offset: long
    _subtype_int: int
    _subtype_index: int
    sib_path_offset: long
    _instance_count: int
    unk_x1c: int  # TODO: is this ever non-zero?
    _pad1: bytes = field(init=False, **BinaryPad(8))  # `type_data_offset` would go here (always zero)


@dataclass(slots=True, eq=False, repr=False)
class MSBModel(BaseMSBModel):
    """MSB model entry in Bloodborne."""

    SUPERTYPE_HEADER_STRUCT: tp.ClassVar[type[BinaryStruct]] = ModelHeaderStruct
    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"
    NULL: tp.ClassVar[bytes] = b"\0\0"
    # TODO: Empty sib path different? b"\0\0" * 6 maybe?

    unk_x1c: int = 0  # TODO: is this ever non-zero?

    def pack_header(
        self,
        writer: BinaryWriter,
        entry_offset: int,
        supertype_index: int,
        subtype_index: int,
        entry_lists: [dict[str, list[MSBEntry]]],
        instance_count: int = 0,
    ):
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            name_offset=RESERVED,
            _subtype_int=self.SUBTYPE_ENUM.value,
            _subtype_index=subtype_index,
            sib_path_offset=RESERVED,
            _instance_count=instance_count,
            unk_x1c=self.unk_x1c,
        )
        writer.fill("name_offset", writer.position - entry_offset, obj=self)
        packed_name = self.name.encode(self.NAME_ENCODING) + self.NULL
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=self)
        if self.sib_path:
            packed_sib_path = self.sib_path.encode(self.NAME_ENCODING) + self.NULL
        else:
            packed_sib_path = self.EMPTY_SIB_PATH
        while len(packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"
        writer.append(packed_sib_path)

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        # TODO: Do some models use generic sib paths?
        return {"name": self.name, "sib_path": self.sib_path, "unk_x1c": self.unk_x1c}


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPieceModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.MapPieceModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:/GR/data/Model/map/{map_stem}/sib/{name}.sib"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacterModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.CharacterModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:/GR/data/Model/chr/{name}/sib/{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayerModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.PlayerModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:/GR/data/Model/chr/{name}/sib/{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBCollisionModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.CollisionModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:/GR/data/Model/map/{map_stem}/hkxwin/{name}.hkxwin"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)


@dataclass(slots=True, eq=False, repr=False)
class MSBAssetModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.AssetModel

    # `name_prefix` is 'AEGxxx', full `name` is 'AEGxxx_xxx'.
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = (
        "N:/GR/data/Asset/Environment/geometry/{name_prefix}/{name}/sib/{name}.sib"
    )

    def set_auto_sib_path(self):
        if not re.match(self.name, r"AEG\d{3}_\d{3}"):
            raise ValueError(f"Asset model name '{self.name}' does not match expected format 'AEGxxx_xxx'.")
        self.sib_path = self.SIB_PATH_TEMPLATE.format(name_prefix=self.name[:6], name=self.name)
