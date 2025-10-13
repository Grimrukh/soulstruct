from __future__ import annotations

__all__ = ["MSB", "MSBSubtypeInfo", "MSBSupertype", "BitSet128"]

import typing as tp
from dataclasses import field
from enum import StrEnum

from soulstruct.darksouls1ptde.game_types.map_types import *
from soulstruct.dcx import DCXType
from soulstruct.base.maps.msb import MSB as _BaseMSB, MSBEntryList, MSBEntry, BaseMSBSubtype
from soulstruct.base.maps.msb.utils import MSBSubtypeInfo, BitSet128
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import EulerDeg, Vector3
from soulstruct.utilities.misc import IDList

from .constants import get_map
from .enums import *
from .models import *
from .events import *
from .regions import *
from .parts import *
from .trees import *


class MSBEntrySuperlistHeader(BinaryStruct):
    _pad1: bytes = binary_pad(4, init=False)
    name_offset: int
    entry_offset_count: int


MSB_ENTRY_SUBTYPES = {
    MSBSupertype.MODELS: {
        MSBModelSubtype.MapPieceModel: MSBSubtypeInfo(MSBMapPieceModel, "map_piece_models"),
        MSBModelSubtype.ObjectModel: MSBSubtypeInfo(MSBObjectModel, "object_models"),
        MSBModelSubtype.CharacterModel: MSBSubtypeInfo(MSBCharacterModel, "character_models"),
        MSBModelSubtype.PlayerModel: MSBSubtypeInfo(MSBPlayerModel, "player_models"),
        MSBModelSubtype.CollisionModel: MSBSubtypeInfo(MSBCollisionModel, "collision_models"),
        MSBModelSubtype.NavmeshModel: MSBSubtypeInfo(MSBNavmeshModel, "navmesh_models"),
        MSBModelSubtype.DummyObjectModel: MSBSubtypeInfo(MSBDummyObjectModel, "dummy_object_models"),
        MSBModelSubtype.DummyCharacterModel: MSBSubtypeInfo(MSBDummyCharacterModel, "dummy_character_models"),
    },
    MSBSupertype.EVENTS: {
        MSBEventSubtype.Light: MSBSubtypeInfo(MSBLightEvent, "lights"),
        MSBEventSubtype.Sound: MSBSubtypeInfo(MSBSoundEvent, "sounds"),
        MSBEventSubtype.VFX: MSBSubtypeInfo(MSBVFXEvent, "vfx"),
        MSBEventSubtype.Wind: MSBSubtypeInfo(MSBWindEvent, "wind"),
        MSBEventSubtype.Treasure: MSBSubtypeInfo(MSBTreasureEvent, "treasures"),
        MSBEventSubtype.Spawner: MSBSubtypeInfo(MSBSpawnerEvent, "spawners"),
        MSBEventSubtype.Message: MSBSubtypeInfo(MSBMessageEvent, "messages"),
    },
    MSBSupertype.REGIONS: {
        MSBRegionSubtype.All: MSBSubtypeInfo(MSBRegion, "regions"),
    },
    MSBSupertype.PARTS: {
        MSBPartSubtype.MapPiece: MSBSubtypeInfo(MSBMapPiece, "map_pieces"),
        MSBPartSubtype.Object: MSBSubtypeInfo(MSBObject, "objects"),
        MSBPartSubtype.Character: MSBSubtypeInfo(MSBCharacter, "characters"),
        # 3 unused.
        MSBPartSubtype.PlayerStart: MSBSubtypeInfo(MSBPlayerStart, "player_starts"),
        MSBPartSubtype.Collision: MSBSubtypeInfo(MSBCollision, "collisions"),
        # 6 unused.
        MSBPartSubtype.Protoboss: MSBSubtypeInfo(MSBProtoboss, "protobosses"),
        MSBPartSubtype.Navmesh: MSBSubtypeInfo(MSBNavmesh, "navmeshes"),
        MSBPartSubtype.DummyObject: MSBSubtypeInfo(MSBDummyObject, "dummy_objects"),
        MSBPartSubtype.DummyCharacter: MSBSubtypeInfo(MSBDummyCharacter, "dummy_characters"),
        MSBPartSubtype.ConnectCollision: MSBSubtypeInfo(MSBConnectCollision, "connect_collisions"),
    },
    MSBSupertype.TREES: {
        MSBTreeSubtype.Tree: MSBSubtypeInfo(MSBTree, "trees"),
    }
}  # type: dict[str, dict[BaseMSBSubtype, MSBSubtypeInfo]]


def empty(subtype_enum: BaseMSBSubtype) -> tp.Callable[[], MSBEntryList]:
    supertype = MSBSupertype(subtype_enum.get_supertype_name())  # for validation
    subtype_info = MSB_ENTRY_SUBTYPES[supertype][subtype_enum]
    return lambda: MSBEntryList((), supertype=supertype, entry_class=subtype_info.entry_class)


class MSB(_BaseMSB[MSBModel, MSBEvent, MSBRegion, MSBPart]):
    IS_BIG_ENDIAN: tp.ClassVar[bool] = True  # for PS3
    SUPERTYPE_LIST_HEADER: tp.ClassVar[type[BinaryStruct]] = MSBEntrySuperlistHeader
    MSB_SUPERTYPE_ENUM: tp.ClassVar[type[StrEnum]] = MSBSupertype
    MSB_ENTRY_SUPERTYPES: tp.ClassVar[dict[str, type[MSBEntry]]] = {
        MSBSupertype.MODELS: MSBModel,
        MSBSupertype.EVENTS: MSBEvent,
        MSBSupertype.REGIONS: MSBRegion,
        MSBSupertype.PARTS: MSBPart,
        MSBSupertype.TREES: MSBTree,
    }
    MSB_SUPERTYPE_SUBTYPE_ENUMS: tp.ClassVar[dict[str, type[BaseMSBSubtype]]] = {
        MSBSupertype.MODELS: MSBModelSubtype,
        MSBSupertype.EVENTS: MSBEventSubtype,
        MSBSupertype.REGIONS: MSBRegionSubtype,
        MSBSupertype.PARTS: MSBPartSubtype,
        MSBSupertype.TREES: MSBTreeSubtype,
    }
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[BaseMSBSubtype, MSBSubtypeInfo]]] = MSB_ENTRY_SUBTYPES
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]] = {
        MSBSupertype.MODELS: 4,
        MSBSupertype.EVENTS: 8,
        MSBSupertype.REGIONS: 4,  # always 0
        MSBSupertype.PARTS: 4,
        MSBSupertype.TREES: -1,  # no subtype index
    }
    MODEL_CLASS: tp.ClassVar[type[MSBModel]] = MSBModel
    EVENT_CLASS: tp.ClassVar[type[MSBEvent]] = MSBEvent
    REGION_CLASS: tp.ClassVar[type[MSBRegion]] = MSBRegion
    PART_CLASS: tp.ClassVar[type[MSBPart]] = MSBPart
    ENTITY_GAME_TYPES: tp.ClassVar[dict[str, MapEntity]] = {
        "map_pieces": MapPiece,
        "objects": Object,
        "characters": Character,
        "player_starts": PlayerStart,
        "collisions": Collision,
        "sounds": SoundEvent,
        "vfx": VFXEvent,
        "spawners": SpawnerEvent,
        "messages": MessageEvent,
        "spawn_points": SpawnPointEvent,
        "navigation": NavigationEvent,
        "regions": Region,
    }

    # Callables with `map_base_id` to get prescribed DS1 entity ID range for each MSB entity type, as class kwargs.
    #   Usage: `class Characters(Character, **MSB.ID_RANGES[Character](map_base_id)): ...`
    # Note that these are GUIDELINES for vanilla usage, but are not always followed. A few maps also have clashing IDs
    # over different supertypes in vanilla DS1 (often between `NavigationEvent`s and regions).
    ID_RANGES = {
        Region: lambda map_base_id: dict(first_value=2000 + map_base_id, last_value=2899 + map_base_id),

        MapPiece: lambda map_base_id: dict(first_value=3000 + map_base_id, last_value=3199 + map_base_id),
        Collision: lambda map_base_id: dict(first_value=3200 + map_base_id, last_value=3399 + map_base_id),
        Object: lambda map_base_id: dict(first_value=1000 + map_base_id, last_value=1899 + map_base_id),
        # IDs 1900-1989 are reserved for bonfire object entities.
        Character: lambda map_base_id: dict(first_value=0 + map_base_id, last_value=899 + map_base_id),
        # IDs 900-989 are reserved for bonfire character entities.
        PlayerStart: lambda map_base_id: dict(first_value=990 + map_base_id, last_value=999 + map_base_id),

        SoundEvent: lambda map_base_id: dict(first_value=3800 + map_base_id, last_value=3899 + map_base_id),
        VFXEvent: lambda map_base_id: dict(first_value=3400 + map_base_id, last_value=3599 + map_base_id),
        SpawnerEvent: lambda map_base_id: dict(first_value=3600 + map_base_id, last_value=3699 + map_base_id),
        MessageEvent: lambda map_base_id: dict(first_value=3700 + map_base_id, last_value=3799 + map_base_id),
        SpawnPointEvent: lambda map_base_id: dict(first_value=3900 + map_base_id, last_value=3949 + map_base_id),
    }

    # Last game (except for DSR) with this old version info.
    HAS_HEADER: tp.ClassVar[bool] = False
    LONG_VARINTS: tp.ClassVar[bool] = False
    NAME_ENCODING: tp.ClassVar[str] = "shift_jis_2004"

    dcx_type: DCXType | None = field(default=DCXType.Null, kw_only=True)

    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=empty(MSBModelSubtype.MapPieceModel))
    object_models: MSBEntryList[MSBObjectModel] = field(default_factory=empty(MSBModelSubtype.ObjectModel))
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=empty(MSBModelSubtype.CharacterModel))
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=empty(MSBModelSubtype.PlayerModel))
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=empty(MSBModelSubtype.CollisionModel))
    navmesh_models: MSBEntryList[MSBNavmeshModel] = field(default_factory=empty(MSBModelSubtype.NavmeshModel))
    dummy_object_models: MSBEntryList[MSBDummyObjectModel] = field(
        default_factory=empty(MSBModelSubtype.DummyObjectModel))
    dummy_character_models: MSBEntryList[MSBDummyCharacterModel] = field(
        default_factory=empty(MSBModelSubtype.DummyCharacterModel))

    lights: MSBEntryList[MSBLightEvent] = field(default_factory=empty(MSBEventSubtype.Light))
    sounds: MSBEntryList[MSBSoundEvent] = field(default_factory=empty(MSBEventSubtype.Sound))
    vfx: MSBEntryList[MSBVFXEvent] = field(default_factory=empty(MSBEventSubtype.VFX))
    wind: MSBEntryList[MSBWindEvent] = field(default_factory=empty(MSBEventSubtype.Wind))
    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=empty(MSBEventSubtype.Treasure))
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=empty(MSBEventSubtype.Spawner))
    messages: MSBEntryList[MSBMessageEvent] = field(default_factory=empty(MSBEventSubtype.Message))

    regions: MSBEntryList[MSBRegion] = field(default_factory=empty(MSBRegionSubtype.All))

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=empty(MSBPartSubtype.MapPiece))
    objects: MSBEntryList[MSBObject] = field(default_factory=empty(MSBPartSubtype.Object))
    characters: MSBEntryList[MSBCharacter] = field(default_factory=empty(MSBPartSubtype.Character))
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=empty(MSBPartSubtype.PlayerStart))
    collisions: MSBEntryList[MSBCollision] = field(default_factory=empty(MSBPartSubtype.Collision))
    protobosses: MSBEntryList[MSBProtoboss] = field(default_factory=empty(MSBPartSubtype.Protoboss))
    navmeshes: MSBEntryList[MSBNavmesh] = field(default_factory=empty(MSBPartSubtype.Navmesh))
    dummy_objects: MSBEntryList[MSBDummyObject] = field(default_factory=empty(MSBPartSubtype.DummyObject))
    dummy_characters: MSBEntryList[MSBDummyCharacter] = field(default_factory=empty(MSBPartSubtype.DummyCharacter))
    connect_collisions: MSBEntryList[MSBConnectCollision] = field(
        default_factory=empty(MSBPartSubtype.ConnectCollision))

    trees: MSBEntryList[MSBTree] = field(default_factory=empty(MSBTreeSubtype.Tree))

    @classmethod
    def _dereference_msb_entries(cls, entry_lists: dict[str, IDList[MSBEntry]]):
        # Resolve entry indices to actual object references.
        for event in entry_lists[MSBSupertype.EVENTS]:
            event: MSBEvent
            event.indices_to_objects(entry_lists)

        for region in entry_lists[MSBSupertype.REGIONS]:
            region: MSBRegion
            region.indices_to_objects(entry_lists)

        for part in entry_lists[MSBSupertype.PARTS]:
            part: MSBPart
            part.indices_to_objects(entry_lists)

    @classmethod
    def resolve_supertype_name(cls, supertype: str) -> str:
        """Resolve various forms of the supertype name into this enum."""
        upper = supertype.upper()
        if upper.startswith("MODEL"):
            return MSBSupertype.MODELS
        if upper.startswith("EVENT"):
            return MSBSupertype.EVENTS
        if upper.startswith("REGION") or upper.startswith("POINT"):
            return MSBSupertype.REGIONS
        if upper.startswith("PARTS"):
            return MSBSupertype.PARTS
        if upper.startswith("TREE") or upper.startswith("MAPSTUDIO_TREE"):
            return MSBSupertype.TREES
        raise ValueError(f"Cannot resolve unknown MSB supertype name: {supertype}")

    @classmethod
    def entity_id_supertypes(cls) -> tuple[str, ...]:
        """Returns all supertypes whose entries use entity IDs."""
        return MSBSupertype.EVENTS, MSBSupertype.REGIONS, MSBSupertype.PARTS

    @property
    def region_points(self) -> MSBEntryList[MSBRegion]:
        return MSBEntryList(
            [region for region in self.regions if region.shape_type == RegionShapeType.Point],
            supertype=MSBSupertype.REGIONS,
            entry_class=MSBRegion,
        )

    @property
    def region_volumes(self) -> MSBEntryList[MSBRegion]:
        volume_types = RegionShapeType.get_volume_types()
        return MSBEntryList(
            [region for region in self.regions if region.shape_type in volume_types],
            supertype=MSBSupertype.REGIONS,
            entry_class=MSBRegion,
        )

    def pack_supertype_name(self, writer: BinaryWriter, supertype_name: str):
        packed_name = supertype_name.encode(self.NAME_ENCODING)
        packed_name += b"\0" * (16 - len(packed_name))  # pad to 16 characters (NOTE: 32 in older Soulstruct)
        writer.append(packed_name)
        writer.pad_align(4)

    # region Auto Model Creation

    def auto_map_piece_model(self, model_name: str, map_stem: str) -> MSBMapPieceModel:
        """Find `model_name` Map Piece Model in MSB, or create it if missing."""
        try:
            return self.map_piece_models[model_name]
        except KeyError:
            map_piece_model = self.map_piece_models.new(name=model_name)
            map_piece_model.set_auto_sib_path(map_stem)
            return map_piece_model

    def auto_object_model(self, model_name: str) -> MSBObjectModel:
        """Find `model_name` Object Model in MSB, or create it if missing."""
        try:
            return self.object_models[model_name]
        except KeyError:
            object_model = self.object_models.new(name=model_name)
            object_model.set_auto_sib_path()
            return object_model

    def auto_character_model(self, model_name: str) -> MSBCharacterModel:
        """Find `model_name` Character Model in MSB, or create it if missing."""
        try:
            return self.character_models[model_name]
        except KeyError:
            character_model = self.character_models.new(name=model_name)
            character_model.set_auto_sib_path()
            return character_model

    def auto_player_model(self, model_name: str) -> MSBPlayerModel:
        """Find `model_name` Player Model in MSB, or create it if missing."""
        try:
            return self.player_models[model_name]
        except KeyError:
            player_model = self.player_models.new(name=model_name)
            player_model.set_auto_sib_path()
            return player_model

    def auto_collision_model(self, model_name: str, map_stem: str) -> MSBCollisionModel:
        """Find `model_name` Collision Model in MSB, or create it if missing."""
        try:
            return self.collision_models[model_name]
        except KeyError:
            collision_model = self.collision_models.new(name=model_name)
            collision_model.set_auto_sib_path(map_stem)
            return collision_model

    def auto_navmesh_model(self, model_name: str, map_stem: str) -> MSBNavmeshModel:
        """Find `model_name` Navmesh Model in MSB, or create it if missing."""
        try:
            return self.navmesh_models[model_name]
        except KeyError:
            navmesh_model = self.navmesh_models.new(name=model_name)
            navmesh_model.set_auto_sib_path(map_stem)
            return navmesh_model

    def auto_model(self, msb_part: MSBPart, model_name: str, map_stem="") -> MSBModel | None:
        """Detect model type from `msb_part` and call appropriate `auto_{subtype}_model()` method to either find an
        existing model of the expected type and name or create a new one and add it to the MSB automatically.

        The found or created model is assigned to `msb_part.model` and returned in case the caller wishes to inspect or
        modify it further (noting that it may be in use by other parts already).

        Creates `MSBCharacterModel` for `MSBPlayerStart` Parts (c0000), which is more common, but only after checking if
        an `MSBPlayerModel` already exists.
        """
        if isinstance(msb_part, MSBMapPiece):
            model = self.auto_map_piece_model(model_name, map_stem)
        elif isinstance(msb_part, MSBObject):  # includes `MSBDummyObject`
            model = self.auto_object_model(model_name)
        elif isinstance(msb_part, (MSBCharacter, MSBPlayerStart)):  # includes `MSBDummyCharacter`
            try:
                model = self.player_models[model_name]
            except KeyError:
                model = self.auto_character_model(model_name)
        elif isinstance(msb_part, (MSBCollision, MSBConnectCollision)):
            model = self.auto_collision_model(model_name, map_stem)
        elif isinstance(msb_part, MSBNavmesh):
            model = self.auto_navmesh_model(model_name, map_stem)
        else:
            raise TypeError(f"Cannot auto-create model for MSB part of type {msb_part.cls_name}.")

        msb_part.model = model
        return model

    # endregion

    # region Utility Methods
    def create_connect_collision_from_collision(
        self, collision: MSBCollision | str,
        connected_map_id: tuple[int, int, int, int],
        name=None,
        draw_groups=None,
        display_groups=None,
    ) -> MSBConnectCollision:
        """Creates a new `ConnectCollision` that references and copies the transform of the given `collision`.

        The `name` and `map_id` of the new `ConnectCollision` must be given. You can also specify its `draw_groups` and
        `display_groups`. Otherwise, it will leave them as the extensive default values: [0, ..., 127].
        """
        if not isinstance(collision, MSBCollision):
            collision = self.collisions.find_entry_name(collision)
        if name is None:
            game_map = get_map(connected_map_id)
            name = collision.name + f"_[{game_map.area_id:02d}_{game_map.block_id:02d}]"
        if name in self.connect_collisions.get_entry_names():
            raise ValueError(f"{repr(name)} is already the name of an existing `MSBConnectCollision`.")
        connect_collision = self.connect_collisions.new(
            name=name,
            model=collision.model,
            connected_map_id=connected_map_id,
            collision=collision,
            translate=collision.translate.copy(),
            rotate=collision.rotate.copy(),
            scale=collision.scale.copy(),  # for completion's sake
        )
        if draw_groups is not None:  # otherwise keep same draw groups
            connect_collision.draw_groups = draw_groups
        if display_groups is not None:  # otherwise keep same display groups
            connect_collision.display_groups = display_groups
        return connect_collision

    def new_c1000(self, name: str, **kwargs) -> MSBCharacter:
        """Useful to create basic c1000 instances as debug warp points."""
        return self.characters.new(name=name, model=self.auto_character_model("c1000"), **kwargs)

    # endregion

    def new_light_event_with_point(
        self,
        translate: Vector3 | tuple[float, float, float] | list[float],
        rotate: EulerDeg | tuple[float, float, float] | list[float],
        **light_event_kwargs,
    ) -> MSBLightEvent:
        if "base_region_name" in light_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        light = self.lights.new(**light_event_kwargs)
        light.attached_region = self.regions.new(
            name=f"_LightEvent_{light.name}",
            translate=translate,
            rotate=rotate,
            shape=PointShape(),
        )
        return light

    def new_sound_event_with_box(
        self,
        translate: Vector3 | tuple[float, float, float] | list[float],
        rotate: EulerDeg | tuple[float, float, float] | list[float],
        width: float,
        depth: float,
        height: float,
        **sound_event_kwargs,
    ) -> MSBSoundEvent:
        if "attached_region" in sound_event_kwargs:
            raise KeyError("`attached_region` will be created and assigned automatically.")
        sound = self.sounds.new(**sound_event_kwargs)
        sound.attached_region = self.regions.new(
            name=f"_SoundEvent_{sound.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            shape=BoxShape(
                width=width,
                depth=depth,
                height=height,
            )
        )
        return sound

    def new_sound_event_with_sphere(
        self,
        translate: Vector3 | tuple[float, float, float] | list[float],
        rotate: EulerDeg | tuple[float, float, float] | list[float],
        radius: float,
        **sound_event_kwargs,
    ) -> MSBSoundEvent:
        if "attached_region" in sound_event_kwargs:
            raise KeyError("`attached_region` will be created and assigned automatically.")
        sound = self.sounds.new(**sound_event_kwargs)
        sphere = self.regions.new(
            name=f"_SoundEvent_{sound.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            shape=SphereShape(
                radius=radius,
            ),
        )
        sound.attached_region = sphere
        return sound

    def new_vfx_event_with_point(
        self,
        translate: Vector3 | tuple[float, float, float] | list[float],
        rotate: EulerDeg | tuple[float, float, float] | list[float],
        point_entity_enum: Region = None,
        **vfx_event_kwargs,
    ) -> MSBVFXEvent:
        if "attached_region" in vfx_event_kwargs:
            raise KeyError("`attached_region` will be created and assigned automatically.")
        vfx = self.vfx.new(**vfx_event_kwargs)
        point_name = f"_VFXEvent_{vfx.name.lstrip('_')}"
        if point_entity_enum is not None:
            if point_entity_enum.name != point_name:
                raise ValueError(f"Name of `point_entity_enum` must be '{point_name}', not '{point_entity_enum.name}'.")
            point_entity_id = point_entity_enum.value
        else:
            point_entity_id = -1
        point = self.regions.new(
            name=point_name,
            entity_id=point_entity_id,
            translate=translate,
            rotate=rotate,
            shape=PointShape(),
        )
        vfx.attached_region = point
        return vfx

    def new_message_event_with_point(
        self,
        translate: Vector3 | tuple[float, float, float] | list[float],
        rotate: EulerDeg | tuple[float, float, float] | list[float],
        **message_event_kwargs,
    ) -> MSBMessageEvent:
        if "attached_region" in message_event_kwargs:
            raise KeyError("`attached_region` will be created and assigned automatically.")
        message = self.messages.new(**message_event_kwargs)
        point = self.regions.new(
            name=f"_MessageEvent_{message.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            shape=PointShape(),
        )
        message.attached_region = point
        return message
