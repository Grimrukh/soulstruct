__all__ = [
    "MSBModel",
    "MSBMapPieceModel",
    "MSBObjectModel",
    "MSBCharacterModel",
    "MSBPlayerModel",
    "MSBCollisionModel",
    "MSBNavmeshModel",
    "MSBModelList",
]

import typing as tp

from soulstruct.base.maps.msb.msb_entry_list import GenericMSBEntryList
from soulstruct.base.maps.msb.models import BaseMSBModel, BaseMSBGeometryModel
from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import BinaryStruct
from soulstruct.utilities.misc import partialmethod

from .enums import MSBModelSubtype
from .msb_entry import MSBEntryList


class MSBModel(BaseMSBModel):
    """MSB model entry in Dark Souls."""

    MODEL_STRUCT = BinaryStruct(
        ("__name_offset", "i"),
        ("__model_type", "i"),
        ("_model_type_index", "i"),
        ("__sib_path_offset", "i"),
        ("_instance_count", "i"),
        "12x",
    )
    NAME_ENCODING = "shift-jis"
    NULL = b"\0"
    EMPTY_SIB_PATH = b"\0" * 6


class MSBMapPieceModel(BaseMSBGeometryModel, MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.MapPiece


class MSBObjectModel(MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Object


class MSBCharacterModel(MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Character


class MSBPlayerModel(MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Player


class MSBCollisionModel(BaseMSBGeometryModel, MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Collision


class MSBNavmeshModel(BaseMSBGeometryModel, MSBModel):
    ENTRY_SUBTYPE = MSBModelSubtype.Navmesh


class MSBModelList(MSBEntryList[MSBModel]):
    INTERNAL_NAME = "MODEL_PARAM_ST"
    PLURALIZED_NAME = "Models"
    ENTRY_SUBTYPE_ENUM = MSBModelSubtype

    SUBTYPE_CLASSES = {
        MSBModelSubtype.MapPiece: MSBMapPieceModel,
        MSBModelSubtype.Object: MSBObjectModel,
        MSBModelSubtype.Character: MSBCharacterModel,
        MSBModelSubtype.Player: MSBPlayerModel,
        MSBModelSubtype.Collision: MSBCollisionModel,
        MSBModelSubtype.Navmesh: MSBNavmeshModel,
    }
    SUBTYPE_OFFSET = 4

    _entries: list[MSBModel]

    new = MSBEntryList.new
    new_map_piece_model: tp.Callable[..., MSBMapPieceModel] = partialmethod(new, MSBModelSubtype.MapPiece)
    new_object_model: tp.Callable[..., MSBObjectModel] = partialmethod(new, MSBModelSubtype.Object)
    new_character_model: tp.Callable[..., MSBCharacterModel] = partialmethod(new, MSBModelSubtype.Character)
    new_player_model: tp.Callable[..., MSBPlayerModel] = partialmethod(new, MSBModelSubtype.Player)
    new_collision_model: tp.Callable[..., MSBCollisionModel] = partialmethod(new, MSBModelSubtype.Collision)
    new_navmesh_model: tp.Callable[..., MSBNavmeshModel] = partialmethod(new, MSBModelSubtype.Navmesh)

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

    @property
    def MapPieces(self) -> GenericMSBEntryList[MSBMapPieceModel]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBMapPieceModel)])

    @property
    def Objects(self) -> GenericMSBEntryList[MSBObjectModel]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBObjectModel)])

    @property
    def Characters(self) -> GenericMSBEntryList[MSBCharacterModel]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBCharacterModel)])

    @property
    def Players(self) -> GenericMSBEntryList[MSBPlayerModel]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBPlayerModel)])

    @property
    def Collisions(self) -> GenericMSBEntryList[MSBCollisionModel]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBCollisionModel)])

    @property
    def Navmeshes(self) -> GenericMSBEntryList[MSBNavmeshModel]:
        return GenericMSBEntryList([e for e in self._entries if isinstance(e, MSBNavmeshModel)])
