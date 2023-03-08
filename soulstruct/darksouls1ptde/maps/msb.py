from __future__ import annotations

__all__ = ["MSB", "MSBSubtypeInfo", "MSBSupertype"]

import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.darksouls1ptde.game_types.map_types import *
from soulstruct.base.maps.msb import MSB as _BaseMSB, MSBSupertype, MSBEntryList
from soulstruct.base.maps.msb.utils import MSBSubtypeInfo
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.binary import *

from .constants import get_map
from .enums import *
from .models import *
from .events import *
from .regions import *
from .parts import *


@dataclass(slots=True)
class MSBEntrySuperlistHeader(BinaryStruct):
    _pad1: bytes = field(init=False, **BinaryPad(4))
    name_offset: int
    entry_offset_count: int


MSB_ENTRY_SUBTYPES = {
    MSBSupertype.MODELS: {
        "MapPieceModel": MSBSubtypeInfo(MSBModelSubtype.MapPieceModel, MSBMapPieceModel, "map_piece_models"),
        "ObjectModel": MSBSubtypeInfo(MSBModelSubtype.ObjectModel, MSBObjectModel, "object_models"),
        "CharacterModel": MSBSubtypeInfo(MSBModelSubtype.CharacterModel, MSBCharacterModel, "character_models"),
        "PlayerModel": MSBSubtypeInfo(MSBModelSubtype.PlayerModel, MSBPlayerModel, "player_models"),
        "CollisionModel": MSBSubtypeInfo(MSBModelSubtype.CollisionModel, MSBCollisionModel, "collision_models"),
        "NavmeshModel": MSBSubtypeInfo(MSBModelSubtype.NavmeshModel, MSBNavmeshModel, "navmesh_models"),
    },
    MSBSupertype.EVENTS: {
        "Light": MSBSubtypeInfo(MSBEventSubtype.Light, MSBLightEvent, "lights"),
        "Sound": MSBSubtypeInfo(MSBEventSubtype.Sound, MSBSoundEvent, "sounds"),
        "VFX": MSBSubtypeInfo(MSBEventSubtype.VFX, MSBVFXEvent, "vfx"),
        "Wind": MSBSubtypeInfo(MSBEventSubtype.Wind, MSBWindEvent, "wind"),
        "Treasure": MSBSubtypeInfo(MSBEventSubtype.Treasure, MSBTreasureEvent, "treasures"),
        "Spawner": MSBSubtypeInfo(MSBEventSubtype.Spawner, MSBSpawnerEvent, "spawners"),
        "Message": MSBSubtypeInfo(MSBEventSubtype.Message, MSBMessageEvent, "messages"),
        "ObjAct": MSBSubtypeInfo(MSBEventSubtype.ObjAct, MSBObjActEvent, "obj_acts"),
        "SpawnPoint": MSBSubtypeInfo(MSBEventSubtype.SpawnPoint, MSBSpawnPointEvent, "spawn_points"),
        "MapOffset": MSBSubtypeInfo(MSBEventSubtype.MapOffset, MSBMapOffsetEvent, "map_offsets"),
        "Navigation": MSBSubtypeInfo(MSBEventSubtype.Navigation, MSBNavigationEvent, "navigation"),
        "Environment": MSBSubtypeInfo(MSBEventSubtype.Environment, MSBEnvironmentEvent, "environments"),
        "NPCInvasion": MSBSubtypeInfo(MSBEventSubtype.NPCInvasion, MSBNPCInvasionEvent, "npc_invasions"),
    },
    MSBSupertype.REGIONS: {
        "Point": MSBSubtypeInfo(MSBRegionSubtype.Point, MSBRegionPoint, "points"),
        "Circle": MSBSubtypeInfo(MSBRegionSubtype.Circle, MSBRegionCircle, "circles"),
        "Sphere": MSBSubtypeInfo(MSBRegionSubtype.Sphere, MSBRegionSphere, "spheres"),
        "Cylinder": MSBSubtypeInfo(MSBRegionSubtype.Cylinder, MSBRegionCylinder, "cylinders"),
        "Rect": MSBSubtypeInfo(MSBRegionSubtype.Rect, MSBRegionRect, "rects"),
        "Box": MSBSubtypeInfo(MSBRegionSubtype.Box, MSBRegionBox, "boxes"),
    },
    MSBSupertype.PARTS: {
        "MapPiece": MSBSubtypeInfo(MSBPartSubtype.MapPiece, MSBMapPiece, "map_pieces"),
        "Object": MSBSubtypeInfo(MSBPartSubtype.Object, MSBObject, "objects"),
        "Character": MSBSubtypeInfo(MSBPartSubtype.Character, MSBCharacter, "characters"),
        # 3 unused.
        "PlayerStart": MSBSubtypeInfo(MSBPartSubtype.PlayerStart, MSBPlayerStart, "player_starts"),
        "Collision": MSBSubtypeInfo(MSBPartSubtype.Collision, MSBCollision, "collisions"),
        # 6 unused.
        # 7 unused.
        "Navmesh": MSBSubtypeInfo(MSBPartSubtype.Navmesh, MSBNavmesh, "navmeshes"),
        "UnusedObject": MSBSubtypeInfo(MSBPartSubtype.UnusedObject, MSBUnusedObject, "unused_objects"),
        "UnusedCharacter": MSBSubtypeInfo(MSBPartSubtype.UnusedCharacter, MSBUnusedCharacter, "unused_characters"),
        "MapConnection": MSBSubtypeInfo(MSBPartSubtype.MapConnection, MSBMapConnection, "map_connections"),
    },
}


def empty_list(supertype_prefix: str, subtype_enum_name: str) -> tp.Callable[[], MSBEntryList]:
    supertype = MSBSupertype(f"{supertype_prefix}_PARAM_ST")
    subtype_info = MSB_ENTRY_SUBTYPES[supertype][subtype_enum_name]
    return lambda: MSBEntryList(supertype=supertype, subtype_info=subtype_info)


@dataclass(slots=True)
class MSB(_BaseMSB):
    SUPERTYPE_LIST_HEADER: tp.ClassVar[tp.Type[BinaryStruct]] = MSBEntrySuperlistHeader
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[str, MSBSubtypeInfo]]] = MSB_ENTRY_SUBTYPES
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]] = {
        MSBSupertype.MODELS: 4,
        MSBSupertype.EVENTS: 8,
        MSBSupertype.REGIONS: 12,
        MSBSupertype.PARTS: 4,
    }
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
        "points": RegionPoint,
        "spheres": RegionSphere,
        "cylinders": RegionCylinder,
        "boxes": RegionBox,
    }

    # Last game (except for DSR) with this old version info.
    HAS_HEADER: tp.ClassVar[bool] = False
    LONG_VARINTS: tp.ClassVar[bool] = False
    NAME_ENCODING: tp.ClassVar[str] = "shift_jis_2004"

    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=empty_list("MODEL", "MapPieceModel"))
    object_models: MSBEntryList[MSBObjectModel] = field(default_factory=empty_list("MODEL", "ObjectModel"))
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=empty_list("MODEL", "CharacterModel"))
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=empty_list("MODEL", "PlayerModel"))
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=empty_list("MODEL", "CollisionModel"))
    navmesh_models: MSBEntryList[MSBNavmeshModel] = field(default_factory=empty_list("MODEL", "NavmeshModel"))

    lights: MSBEntryList[MSBLightEvent] = field(default_factory=empty_list("EVENT", "Light"))
    sounds: MSBEntryList[MSBSoundEvent] = field(default_factory=empty_list("EVENT", "Sound"))
    vfx: MSBEntryList[MSBVFXEvent] = field(default_factory=empty_list("EVENT", "VFX"))
    wind: MSBEntryList[MSBWindEvent] = field(default_factory=empty_list("EVENT", "Wind"))
    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=empty_list("EVENT", "Treasure"))
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=empty_list("EVENT", "Spawner"))
    messages: MSBEntryList[MSBMessageEvent] = field(default_factory=empty_list("EVENT", "Message"))
    obj_acts: MSBEntryList[MSBObjActEvent] = field(default_factory=empty_list("EVENT", "ObjAct"))
    spawn_points: MSBEntryList[MSBSpawnPointEvent] = field(default_factory=empty_list("EVENT", "SpawnPoint"))
    map_offsets: MSBEntryList[MSBMapOffsetEvent] = field(default_factory=empty_list("EVENT", "MapOffset"))
    navigation: MSBEntryList[MSBNavigationEvent] = field(default_factory=empty_list("EVENT", "Navigation"))
    environments: MSBEntryList[MSBEnvironmentEvent] = field(default_factory=empty_list("EVENT", "Environment"))
    npc_invasions: MSBEntryList[MSBNPCInvasionEvent] = field(default_factory=empty_list("EVENT", "NPCInvasion"))

    points: MSBEntryList[MSBRegionPoint] = field(default_factory=empty_list("POINT", "Point"))
    circles: MSBEntryList[MSBRegionCircle] = field(default_factory=empty_list("POINT", "Circle"))
    spheres: MSBEntryList[MSBRegionSphere] = field(default_factory=empty_list("POINT", "Sphere"))
    cylinders: MSBEntryList[MSBRegionCylinder] = field(default_factory=empty_list("POINT", "Cylinder"))
    rects: MSBEntryList[MSBRegionRect] = field(default_factory=empty_list("POINT", "Rect"))
    boxes: MSBEntryList[MSBRegionBox] = field(default_factory=empty_list("POINT", "Box"))

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=empty_list("PARTS", "MapPiece"))
    objects: MSBEntryList[MSBObject] = field(default_factory=empty_list("PARTS", "Object"))
    characters: MSBEntryList[MSBCharacter] = field(default_factory=empty_list("PARTS", "Character"))
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=empty_list("PARTS", "PlayerStart"))
    collisions: MSBEntryList[MSBCollision] = field(default_factory=empty_list("PARTS", "Collision"))
    navmeshes: MSBEntryList[MSBNavmesh] = field(default_factory=empty_list("PARTS", "Navmesh"))
    unused_objects: MSBEntryList[MSBUnusedObject] = field(default_factory=empty_list("PARTS", "UnusedObject"))
    unused_characters: MSBEntryList[MSBUnusedCharacter] = field(default_factory=empty_list("PARTS", "UnusedCharacter"))
    map_connections: MSBEntryList[MSBMapConnection] = field(default_factory=empty_list("PARTS", "MapConnection"))

    def pack_supertype_name(self, writer: BinaryWriter, supertype_name: str):
        packed_name = supertype_name.encode(self.NAME_ENCODING)
        packed_name += b"\0" * (16 - len(packed_name))  # pad to 16 characters (NOTE: 32 in older Soulstruct)
        writer.append(packed_name)

    # region Utility Methods
    def duplicate_collision_with_environment_event(
        self, collision: MSBCollision | str, at_next_index=True, **kwargs,
    ) -> MSBCollision:
        """Duplicate a Collision and any attached `MSBEnvironment` instance and its region."""
        if "name" not in kwargs:
            raise ValueError(f"Must pass `name` to Collision duplication call to duplicate attached environment event.")
        if not isinstance(collision, MSBCollision):
            collision = self.collisions.find_entry_name(collision)
        name = kwargs["name"]
        new_collision = self.collisions.duplicate(
            copy_entry=collision, at_next_index=at_next_index, **kwargs,
        )
        if not new_collision.environment_event:
            return new_collision

        environment_event = new_collision.environment_event
        if not environment_event.attached_region:
            raise AttributeError(f"Environment event '{environment_event.name}' has no anchor Region.")
        environment_region = environment_event.attached_region
        region_subtype_list = self.get_list_of_entry(environment_region)

        new_event = self.environments.duplicate(environment_event, name=f"GI Event ({name})")
        new_event.attached_region = region_subtype_list.duplicate(environment_region, name=f"GI Region ({name})")
        new_collision.environment_event = new_event
        return new_collision

    def create_map_connection_from_collision(
        self, collision: MSBCollision | str, connected_map, name=None, draw_groups=None, display_groups=None
    ):
        """Creates a new `MapConnection` that references and copies the transform of the given `collision`.

        The `name` and `map_id` of the new `MapConnection` must be given. You can also specify its `draw_groups` and
        `display_groups`. Otherwise, it will leave them as the extensive default values: [0, ..., 127].
        """
        if not isinstance(collision, MSBCollision):
            collision = self.collisions.find_entry_name(collision)
        if name is None:
            game_map = get_map(connected_map)
            name = collision.name + f"_[{game_map.area_id:02d}_{game_map.block_id:02d}]"
        if name in self.map_connections.get_entry_names():
            raise ValueError(f"{repr(name)} is already the name of an existing `MSBMapConnection`.")
        map_connection = self.map_connections.new(
            name=name,
            connected_map=connected_map,
            collision=collision,
            translate=collision.translate.copy(),
            rotate=collision.rotate.copy(),
            scale=collision.scale.copy(),  # for completion's sake
            model=collision.model,
        )
        if draw_groups is not None:  # otherwise keep same draw groups
            map_connection.draw_groups = draw_groups
        if display_groups is not None:  # otherwise keep same display groups
            map_connection.display_groups = display_groups
        return map_connection

    def new_c1000(self, name: str, **kwargs) -> MSBCharacter:
        """Useful to create basic c1000 instances as debug warp points."""
        return self.characters.new(name=name, model_name="c1000", **kwargs)

    # endregion

    def new_light_event_with_point(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        **light_event_kwargs,
    ) -> MSBLightEvent:
        if "base_region_name" in light_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        light = self.lights.new(**light_event_kwargs)
        light.attached_region = self.points.new(
            name=f"_LightEvent_{light.name}",
            translate=translate,
            rotate=rotate,
        )
        return light

    def new_sound_event_with_box(
        self,
        translate: Vector3,
        rotate: Vector3,
        width: float,
        depth: float,
        height: float,
        **sound_event_kwargs,
    ) -> MSBSoundEvent:
        if "attached_region" in sound_event_kwargs:
            raise KeyError("`attached_region` will be created and assigned automatically.")
        sound = self.sounds.new(**sound_event_kwargs)
        sound.attached_region = self.boxes.new(
            name=f"_SoundEvent_{sound.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            width=width,
            depth=depth,
            height=height,
        )
        return sound

    def new_sound_event_with_sphere(
        self,
        translate: Vector3,
        rotate: Vector3,
        radius: float,
        **sound_event_kwargs,
    ) -> MSBSoundEvent:
        if "attached_region" in sound_event_kwargs:
            raise KeyError("`attached_region` will be created and assigned automatically.")
        sound = self.sounds.new(**sound_event_kwargs)
        sphere = self.spheres.new(
            name=f"_SoundEvent_{sound.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            radius=radius,
        )
        sound.attached_region = sphere
        return sound

    def new_vfx_event_with_point(
        self,
        translate: Vector3,
        rotate: Vector3,
        point_entity_enum: RegionPoint = None,
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
        point = self.points.new(
            name=point_name,
            entity_id=point_entity_id,
            translate=translate,
            rotate=rotate,
        )
        vfx.attached_region = point
        return vfx

    def new_spawn_point_event_with_point(
        self,
        translate: Vector3,
        rotate: Vector3,
        **spawn_point_event_kwargs,
    ) -> MSBSpawnPointEvent:
        if "attached_region" in spawn_point_event_kwargs:
            raise KeyError("`attached_region` will be created and assigned automatically.")
        spawn_point = self.spawn_points.new(**spawn_point_event_kwargs)
        point = self.points.new(
            name=f"_SpawnPointEvent_{spawn_point.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
        )
        spawn_point.spawn_point_region = point
        return spawn_point

    def new_message_event_with_point(
        self,
        translate: Vector3,
        rotate: Vector3,
        **message_event_kwargs,
    ) -> MSBMessageEvent:
        if "attached_region" in message_event_kwargs:
            raise KeyError("`attached_region` will be created and assigned automatically.")
        message = self.messages.new(**message_event_kwargs)
        point = self.points.new(
            name=f"_MessageEvent_{message.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
        )
        message.attached_region = point
        return message

    def new_objact_event_for_object(
        self,
        obj_spec: MSBObject | str | int | IntEnum,
        obj_act_entity_id: int,
        obj_act_state: int = 0,
        obj_act_param_id: int = -1,
        obj_act_flag: int = None,
        name: str = None,
    ) -> MSBObjActEvent:
        """Add an `MSBObjActEvent` to the MSB attached to the given MSB `obj_name`.

        Entity ID (generally equal to the event ID that handles the ObjAct) must be given. All other variables are
        optional: ObjAct state (defaults to 0), ObjAct param ID (defaults to -1, i.e. the object's model ID), and
        associated state flag (defaults to 60000000 + the object's entity ID, if present).

        A `ValueError` will be raised if the `obj_name` has no entity ID and `obj_act_flag` is not given.
        """
        if isinstance(obj_spec, IntEnum):
            obj_spec = obj_spec.name
        if isinstance(obj_spec, str):
            obj = self.objects.find_entry_name(obj_spec)
        elif isinstance(obj_spec, int):
            obj = self.objects[obj_spec]
        else:
            raise TypeError(
                f"`obj_spec` must be an `MSBObject`, index, name, or name-synchronised `IntEnum`, not {obj_spec}."
            )
        if obj_act_flag is None:
            if obj.entity_id <= 0:
                raise ValueError(
                    f"Cannot automatically set `obj_act_flag` for ObjAct attached to object '{obj.name}', as it does "
                    f"not have a valid entity ID."
                )
            obj_act_flag = 60000000 + obj.entity_id
        if name is None:
            name = f"_ObjAct_{obj.name.lstrip('_')}"
        return self.obj_acts.new(
            name=name,
            obj_act_part_name=obj.name,
            obj_act_entity_id=obj_act_entity_id,
            obj_act_param_id=obj_act_param_id,
            obj_act_state=obj_act_state,
            obj_act_flag=obj_act_flag,
        )
