__all__ = ["MSBModel", "MSBModelList"]

import typing as tp
from functools import partial, partialmethod

from soulstruct.base.maps.msb.models import (
    MSBModel as _BaseMSBModel,
    MSBModelList as _BaseMSBModelList,
)
from soulstruct.base.maps.msb.enums import MSBModelSubtype
from soulstruct.utilities.binary_struct import BinaryStruct

from .msb_entry import MSBEntryList


class MSBModel(_BaseMSBModel):
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
    SIB_PATH_STEM = "N:\\SPRJ\\data\\Model\\"  # TODO: guessing at SPRJ


class MSBModelList(_BaseMSBModelList, MSBEntryList):

    SUBTYPE_CLASSES = {
        MSBModelSubtype.MapPiece: partial(MSBModel, model_subtype="MapPiece"),
        MSBModelSubtype.Object: partial(MSBModel, model_subtype="Object"),
        MSBModelSubtype.Character: partial(MSBModel, model_subtype="Character"),
        MSBModelSubtype.Player: partial(MSBModel, model_subtype="Player"),
        MSBModelSubtype.Collision: partial(MSBModel, model_subtype="Collision"),
        MSBModelSubtype.Navmesh: partial(MSBModel, model_subtype="Navmesh"),
        MSBModelSubtype.Other: partial(MSBModel, model_subtype="Other"),
    }
    ENTRY_CLASS = MSBModel

    MapPieces: list[MSBModel]
    Objects: list[MSBModel]
    Characters: list[MSBModel]
    Items: list[MSBModel]
    Players: list[MSBModel]
    Collisions: list[MSBModel]
    Navmeshes: list[MSBModel]
    Other: list[MSBModel]

    new_map_piece_model: tp.Callable[..., MSBModel]
    new_object_model: tp.Callable[..., MSBModel]
    new_character_model: tp.Callable[..., MSBModel]
    new_item_model: tp.Callable[..., MSBModel]
    new_player_model: tp.Callable[..., MSBModel]
    new_collision_model: tp.Callable[..., MSBModel]
    new_navmesh_model: tp.Callable[..., MSBModel]
    new_other_model: tp.Callable[..., MSBModel] = partialmethod(MSBEntryList.new, MSBModelSubtype.Other)
