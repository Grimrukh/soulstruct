from __future__ import annotations

__all__ = ["MSB"]

import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.darksouls1ptde.game_types.map_types import *
from soulstruct.base.maps.msb import MSB as _BaseMSB, MSBSubtypeInfo, MSBEntryList
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.binary import *

from .constants import get_map
from .enums import MSBModelSubtype, MSBEventSubtype, MSBRegionSubtype, MSBPartSubtype
from .models import *
from .events import *
from .regions import *
from .parts import *


@dataclass(slots=True)
class MSBEntrySuperlistHeader(NewBinaryStruct):
    _pad1: bytes = field(init=False, **BinaryPad(4))
    name_offset: int
    entry_offset_count: int


class MSB(_BaseMSB):
    SUPERTYPE_LIST_HEADER: tp.ClassVar[tp.Type[NewBinaryStruct]] = MSBEntrySuperlistHeader
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[int, MSBSubtypeInfo]]] = {
        "MODEL_PARAM_ST": {
            0: MSBSubtypeInfo(MSBModelSubtype.MapPiece, MSBMapPieceModel, "map_piece_models"),
            1: MSBSubtypeInfo(MSBModelSubtype.Object, MSBObjectModel, "object_models"),
            2: MSBSubtypeInfo(MSBModelSubtype.Character, MSBCharacterModel, "character_models"),
            # 3: MSBSubtypeInfo(MSBModelSubtype.Item, MSBItemModel, "item_models"),  # NOT IN DS1
            4: MSBSubtypeInfo(MSBModelSubtype.Player, MSBPlayerModel, "player_models"),
            5: MSBSubtypeInfo(MSBModelSubtype.Collision, MSBCollisionModel, "collision_models"),
            6: MSBSubtypeInfo(MSBModelSubtype.Navmesh, MSBNavmeshModel, "navmesh_models"),
        },
        "EVENT_PARAM_ST": {
            1: MSBSubtypeInfo(MSBEventSubtype.Sound, MSBSoundEvent, "sounds"),
            2: MSBSubtypeInfo(MSBEventSubtype.VFX, MSBVFXEvent, "vfx"),
            3: MSBSubtypeInfo(MSBEventSubtype.Wind, MSBWindEvent, "wind"),
            4: MSBSubtypeInfo(MSBEventSubtype.Treasure, MSBTreasureEvent, "treasures"),
            5: MSBSubtypeInfo(MSBEventSubtype.Spawner, MSBSpawnerEvent, "spawners"),
            6: MSBSubtypeInfo(MSBEventSubtype.Message, MSBMessageEvent, "messages"),
            7: MSBSubtypeInfo(MSBEventSubtype.ObjAct, MSBObjActEvent, "obj_acts"),
            8: MSBSubtypeInfo(MSBEventSubtype.SpawnPoint, MSBSpawnPointEvent, "spawn_points"),
            9: MSBSubtypeInfo(MSBEventSubtype.MapOffset, MSBMapOffsetEvent, "map_offsets"),
            10: MSBSubtypeInfo(MSBEventSubtype.Navigation, MSBNavigationEvent, "navigation"),
            11: MSBSubtypeInfo(MSBEventSubtype.Environment, MSBEnvironmentEvent, "environments"),
            12: MSBSubtypeInfo(MSBEventSubtype.NPCInvasion, MSBNPCInvasionEvent, "npc_invasions"),
        },
        "POINT_PARAM_ST": {
            0: MSBSubtypeInfo(MSBRegionSubtype.Point, MSBRegionPoint, "points"),
            1: MSBSubtypeInfo(MSBRegionSubtype.Circle, MSBRegionCircle, "circles"),
            2: MSBSubtypeInfo(MSBRegionSubtype.Sphere, MSBRegionSphere, "spheres"),
            3: MSBSubtypeInfo(MSBRegionSubtype.Cylinder, MSBRegionCylinder, "cylinders"),
            4: MSBSubtypeInfo(MSBRegionSubtype.Rect, MSBRegionRect, "rects"),
            5: MSBSubtypeInfo(MSBRegionSubtype.Box, MSBRegionBox, "boxes"),
        },
        "PARTS_PARAM_ST": {
            0: MSBSubtypeInfo(MSBPartSubtype.MapPiece, MSBMapPiece, "map_pieces"),
            1: MSBSubtypeInfo(MSBPartSubtype.Object, MSBObject, "objects"),
            2: MSBSubtypeInfo(MSBPartSubtype.Character, MSBCharacter, "characters"),
            # 3 unused.
            4: MSBSubtypeInfo(MSBPartSubtype.PlayerStart, MSBPlayerStart, "player_starts"),
            5: MSBSubtypeInfo(MSBPartSubtype.Collision, MSBCollision, "collisions"),
            # 6 unused.
            # 7 unused.
            8: MSBSubtypeInfo(MSBPartSubtype.Navmesh, MSBNavmesh, "navmeshes"),
            9: MSBSubtypeInfo(MSBPartSubtype.UnusedObject, MSBUnusedObject, "unused_objects"),
            10: MSBSubtypeInfo(MSBPartSubtype.UnusedCharacter, MSBUnusedCharacter, "unused_characters"),
            11: MSBSubtypeInfo(MSBPartSubtype.MapConnection, MSBMapConnection, "map_connections"),
        },
    }
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]] = {
        "MODEL_PARAM_ST": 4,
        "EVENT_PARAM_ST": 8,
        "POINT_PARAM_ST": 12,
        "PARTS_PARAM_ST": 4,
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

    # TODO: default factory methods need supertype name, subtype enum, subtype class
    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=MSBEntryList)
    object_models: MSBEntryList[MSBObjectModel] = field(default_factory=MSBEntryList)
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=MSBEntryList)
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=MSBEntryList)
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=MSBEntryList)
    navmesh_models: MSBEntryList[MSBNavmeshModel] = field(default_factory=MSBEntryList)

    lights: MSBEntryList[MSBLightEvent] = field(default_factory=MSBEntryList)
    sounds: MSBEntryList[MSBSoundEvent] = field(default_factory=MSBEntryList)
    vfx: MSBEntryList[MSBVFXEvent] = field(default_factory=MSBEntryList)
    wind: MSBEntryList[MSBWindEvent] = field(default_factory=MSBWindEvent)
    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=MSBEntryList)
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=MSBEntryList)
    messages: MSBEntryList[MSBMessageEvent] = field(default_factory=MSBEntryList)
    obj_acts: MSBEntryList[MSBObjActEvent] = field(default_factory=MSBEntryList)
    spawn_points: MSBEntryList[MSBSpawnPointEvent] = field(default_factory=MSBEntryList)
    map_offsets: MSBEntryList[MSBMapOffsetEvent] = field(default_factory=MSBEntryList)
    navigation: MSBEntryList[MSBNavigationEvent] = field(default_factory=MSBEntryList)
    environments: MSBEntryList[MSBEnvironmentEvent] = field(default_factory=MSBEntryList)
    npc_invasions: MSBEntryList[MSBNPCInvasionEvent] = field(default_factory=MSBEntryList)

    points: MSBEntryList[MSBRegionPoint] = field(default_factory=MSBEntryList)
    circles: MSBEntryList[MSBRegionCircle] = field(default_factory=MSBEntryList)
    spheres: MSBEntryList[MSBRegionSphere] = field(default_factory=MSBEntryList)
    cylinders: MSBEntryList[MSBRegionCylinder] = field(default_factory=MSBEntryList)
    rects: MSBEntryList[MSBRegionRect] = field(default_factory=MSBEntryList)
    boxes: MSBEntryList[MSBRegionBox] = field(default_factory=MSBEntryList)

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=MSBEntryList)
    objects: MSBEntryList[MSBObject] = field(default_factory=MSBEntryList)
    characters: MSBEntryList[MSBCharacter] = field(default_factory=MSBEntryList)
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=MSBEntryList)
    collisions: MSBEntryList[MSBCollision] = field(default_factory=MSBEntryList)
    navmeshes: MSBEntryList[MSBNavmesh] = field(default_factory=MSBEntryList)
    unused_objects: MSBEntryList[MSBUnusedObject] = field(default_factory=MSBEntryList)
    unused_characters: MSBEntryList[MSBUnusedCharacter] = field(default_factory=MSBEntryList)
    map_connections: MSBEntryList[MSBMapConnection] = field(default_factory=MSBEntryList)

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

    def new_sound_event_with_box(
        self,
        translate: Vector3,
        rotate: Vector3,
        width: float,
        depth: float,
        height: float,
        **sound_event_kwargs,
    ):
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
    ):
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
        point_entity_enum: tp.Optional[RegionPoint] = None,
        **vfx_event_kwargs,
    ):
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
    ):
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
    ):
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
    ):
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
