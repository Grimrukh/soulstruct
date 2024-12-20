from __future__ import annotations

__all__ = [
    "MSBModel",
    "MSBMapPieceModel",
    "MSBCharacterModel",
    "MSBPlayerModel",
    "MSBCollisionModel",
    "MSBAssetModel",
]

import abc
import re
import typing as tp
from dataclasses import dataclass

from soulstruct.base.maps.msb.msb_entry import *
from soulstruct.base.maps.msb.models import BaseMSBModel
from soulstruct.utilities.binary import *

from .enums import MSBModelSubtype

if tp.TYPE_CHECKING:
    from soulstruct.base.maps.msb import MSBEntry
    from soulstruct.utilities.misc import IDList


class ModelHeaderStruct(MSBHeaderStruct):
    name_offset: long
    _subtype_int: int
    subtype_index: int
    sib_path_offset: long
    instance_count: int
    unk_x1c: int  # TODO: is this ever non-zero?
    _pad1: bytes = binary_pad(8, init=False)  # `type_data_offset` would go here (always zero)

    @classmethod
    def reader_to_entry_kwargs(
        cls,
        reader: BinaryReader,
        entry_type: type[MSBEntry],
        entry_offset: int,
    ) -> dict[str, tp.Any]:
        kwargs = super(ModelHeaderStruct, cls).reader_to_entry_kwargs(reader, entry_type, entry_offset)
        sib_path = reader.unpack_string(
            offset=entry_offset + kwargs.pop("sib_path_offset"), encoding=entry_type.NAME_ENCODING
        )
        kwargs["sib_path"] = sib_path
        kwargs.pop("instance_count")
        return kwargs

    @classmethod
    def preprocess_write_kwargs(
        cls,
        entry: MSBEntry,
        entry_lists: dict[str, IDList[MSBEntry]],
        kwargs: dict[str, tp.Any],
    ) -> None:
        super(ModelHeaderStruct, cls).preprocess_write_kwargs(entry, entry_lists, kwargs)
        kwargs["sib_path_offset"] = RESERVED
        kwargs.pop("supertype_index")
        if "instance_count" not in kwargs:
            raise ValueError("MSBModel must have `instance_count` set in `kwargs_to_msb_writer`.")

    @classmethod
    def post_write(
        cls,
        entry: MSBModel,
        writer: BinaryWriter,
        entry_offset: int,
        entry_lists: [dict[str, IDList[MSBEntry]]],  # may be required by subclasses
    ):
        # No super.
        writer.fill("name_offset", writer.position - entry_offset, obj=entry)
        packed_name = entry.name.encode(entry.NAME_ENCODING) + b"\0\0"
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=entry)
        if entry.sib_path:
            packed_sib_path = entry.sib_path.encode(entry.NAME_ENCODING) + b"\0\0"
        else:
            packed_sib_path = b"\0\0\0\0\0\0"  # TODO: confirm length
        while len(packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"
        writer.append(packed_sib_path)


@dataclass(slots=True, eq=False, repr=False)
class MSBModel(BaseMSBModel, abc.ABC):
    """MSB model entry in Bloodborne."""

    HEADER_STRUCT = ModelHeaderStruct
    NAME_ENCODING = "utf-16-le"

    unk_x1c: int = 0  # TODO: is this ever non-zero?

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        # TODO: Do some models use generic sib paths?
        return {"name": self.name, "sib_path": self.sib_path, "unk_x1c": self.unk_x1c}


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPieceModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.MapPieceModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\GR\\data\\Model\\map\\{map_stem}\\sib\\{name}.sib"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacterModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.CharacterModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\GR\\data\\Model\\chr\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayerModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.PlayerModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\GR\\data\\Model\\chr\\{name}\\sib\\{name}.sib"


@dataclass(slots=True, eq=False, repr=False)
class MSBCollisionModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.CollisionModel

    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:\\GR\\data\\Model\\map\\{map_stem}\\hkxwin\\{name}.hkxwin"

    def set_auto_sib_path(self, map_stem: str):
        self.sib_path = self.SIB_PATH_TEMPLATE.format(map_stem=map_stem, name=self.name)


@dataclass(slots=True, eq=False, repr=False)
class MSBAssetModel(MSBModel):
    SUBTYPE_ENUM: tp.ClassVar = MSBModelSubtype.AssetModel

    # `name_prefix` is 'AEGxxx', full `name` is 'AEGxxx_xxx'.
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = (
        "N:\\GR\\data\\Asset\\Environment\\geometry\\{name_prefix}\\{name}\\sib\\{name}.sib"
    )

    def set_auto_sib_path(self):
        if not re.match(self.name, r"AEG\d{3}_\d{3}"):
            raise ValueError(f"Asset model name '{self.name}' does not match expected format: 'AEGxxx_xxx'")
        self.sib_path = self.SIB_PATH_TEMPLATE.format(name_prefix=self.name[:6], name=self.name)
