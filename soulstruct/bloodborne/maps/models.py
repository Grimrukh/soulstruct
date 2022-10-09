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
    "MSBModelList",
]

import typing as tp

from soulstruct.base.maps.msb.models import BaseMSBModel, BaseMSBGeometryModel, BaseMSBModelList
from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import BinaryStruct
from soulstruct.utilities.misc import partialmethod

from .enums import MSBModelSubtype
from .msb_entry import MSBEntryList


class MSBModel(BaseMSBModel):
    """MSB model entry in Bloodborne."""

    MODEL_STRUCT = BinaryStruct(
        ("__name_offset", "q"),
        ("__model_type", "i"),
        ("_model_type_index", "i"),
        ("__sib_path_offset", "q"),
        ("_instance_count", "i"),
        "12x",
    )
    NAME_ENCODING = "utf-16-le"
    NULL = b"\0\0"
    # TODO: Empty sib path different? b"\0\0" * 6 maybe?


class MSBMapPieceModel(BaseMSBGeometryModel, MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.MapPiece


class MSBObjectModel(MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Object


class MSBCharacterModel(MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Character


class MSBItemModel(MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Item


class MSBPlayerModel(MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Player


class MSBCollisionModel(BaseMSBGeometryModel, MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Collision


class MSBNavmeshModel(BaseMSBGeometryModel, MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Navmesh


class MSBOtherModel(MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Other


class MSBModelList(BaseMSBModelList, MSBEntryList[MSBModel]):
    INTERNAL_NAME = "MODEL_PARAM_ST"
    PLURALIZED_NAME = "Models"
    ENTRY_SUBTYPE_ENUM = MSBModelSubtype

    SUBTYPE_CLASSES = {
        MSBModelSubtype.MapPiece: MSBMapPieceModel,
        MSBModelSubtype.Object: MSBObjectModel,
        MSBModelSubtype.Character: MSBCharacterModel,
        MSBModelSubtype.Item: MSBItemModel,
        MSBModelSubtype.Player: MSBPlayerModel,
        MSBModelSubtype.Collision: MSBCollisionModel,
        MSBModelSubtype.Navmesh: MSBNavmeshModel,
        MSBModelSubtype.Other: MSBOtherModel,
    }
    ENTRY_CLASS = MSBModel

    _entries: list[MSBModel]

    MapPieces: list[MSBMapPieceModel]
    Objects: list[MSBObjectModel]
    Characters: list[MSBCharacterModel]
    Items: list[MSBItemModel]
    Players: list[MSBPlayerModel]
    Collisions: list[MSBCollisionModel]
    Navmeshes: list[MSBNavmeshModel]
    Other: list[MSBOtherModel]

    new = MSBEntryList.new
    new_map_piece_model: tp.Callable[..., MSBMapPieceModel] = partialmethod(new, MSBModelSubtype.MapPiece)
    new_object_model: tp.Callable[..., MSBObjectModel] = partialmethod(new, MSBModelSubtype.Object)
    new_character_model: tp.Callable[..., MSBCharacterModel] = partialmethod(new, MSBModelSubtype.Character)
    new_item_model: tp.Callable[..., MSBItemModel] = partialmethod(new, MSBModelSubtype.Item)
    new_player_model: tp.Callable[..., MSBPlayerModel] = partialmethod(new, MSBModelSubtype.Player)
    new_collision_model: tp.Callable[..., MSBCollisionModel] = partialmethod(new, MSBModelSubtype.Collision)
    new_navmesh_model: tp.Callable[..., MSBNavmeshModel] = partialmethod(new, MSBModelSubtype.Navmesh)
    new_other_model: tp.Callable[..., MSBOtherModel] = partialmethod(new, MSBModelSubtype.Other)

    def pack_entry(self, index: int, entry: MSBModel):
        return entry.pack()

    def set_indices(self, part_instance_counts):
        """Local type-specific index only. (Note that global entry index is still used by Parts.)"""
        type_indices = {}
        for entry in self._entries:
            try:
                entry.set_indices(
                    model_type_index=type_indices.setdefault(entry.ENTRY_SUBTYPE, 0),
                    instance_count=part_instance_counts.get(entry.name, 0),
                )
            except KeyError as e:
                raise SoulstructError(
                    f"Invalid map component name for {entry.ENTRY_SUBTYPE.name} model {entry.name}: {e}"
                )
            else:
                type_indices[entry.ENTRY_SUBTYPE] += 1

    def sort(self):
        """Sort all models by type, then alphabetically."""
        sorted_entries = []  # type: list[MSBModel]
        for entry_subtype in MSBModelSubtype:
            sorted_entries += list(sorted(self.get_entries(entry_subtype), key=lambda m: m.name))
        self._entries = sorted_entries


for _entry_subtype in MSBModelSubtype:
    setattr(
        MSBModelList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
