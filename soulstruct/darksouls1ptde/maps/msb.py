from __future__ import annotations

__all__ = ["MSB", "MSBSubtypeInfo", "MSBSupertype"]

import typing as tp
from dataclasses import dataclass, field
from enum import IntEnum

from soulstruct.darksouls1ptde.game_types.map_types import *
from soulstruct.dcx import DCXType
from soulstruct.base.maps.msb import MSB as _BaseMSB, MSBEntryList
from soulstruct.base.maps.msb.utils import MSBSubtypeInfo
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.misc import IDList

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
        "All": MSBSubtypeInfo(MSBRegionSubtype.All, MSBRegion, "regions"),
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
        "DummyObject": MSBSubtypeInfo(MSBPartSubtype.DummyObject, MSBDummyObject, "unused_objects"),
        "DummyCharacter": MSBSubtypeInfo(MSBPartSubtype.DummyCharacter, MSBDummyCharacter, "unused_characters"),
        "ConnectCollision": MSBSubtypeInfo(MSBPartSubtype.ConnectCollision, MSBConnectCollision, "connect_collisions"),
    },
}


def empty(supertype_prefix: str, subtype_enum_name: str) -> tp.Callable[[], MSBEntryList]:
    supertype = MSBSupertype(f"{supertype_prefix}_PARAM_ST")
    subtype_info = MSB_ENTRY_SUBTYPES[supertype][subtype_enum_name]
    return lambda: MSBEntryList((), supertype=supertype, subtype_info=subtype_info)


@dataclass(slots=True, kw_only=True)
class MSB(_BaseMSB):
    SUPERTYPE_LIST_HEADER: tp.ClassVar[type[BinaryStruct]] = MSBEntrySuperlistHeader
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[str, MSBSubtypeInfo]]] = MSB_ENTRY_SUBTYPES
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]] = {
        MSBSupertype.MODELS: 4,
        MSBSupertype.EVENTS: 8,
        MSBSupertype.REGIONS: 4,  # always 0
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
        # Shape-based region sublist properties:
        "region_points": RegionPoint,
        "region_volumes": RegionVolume,
    }

    # Callables with `map_base_id` to get prescribed DS1 entity ID range for each MSB entity type, as class kwargs.
    #   Usage: `class Characters(Character, **MSB.ID_RANGES[Character](map_base_id)): ...`
    # Note that these are GUIDELINES for vanilla usage, but are not always followed. A few maps also have clashing IDs
    # over different supertypes in vanilla DS1 (often between `NavigationEvent`s and regions).
    ID_RANGES = {
        RegionVolume: lambda map_base_id: dict(first_value=2000 + map_base_id, last_value=2499 + map_base_id),
        RegionPoint: lambda map_base_id: dict(first_value=2500 + map_base_id, last_value=2899 + map_base_id),

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

    map_piece_models: MSBEntryList[MSBMapPieceModel] = field(default_factory=empty("MODEL", "MapPieceModel"))
    object_models: MSBEntryList[MSBObjectModel] = field(default_factory=empty("MODEL", "ObjectModel"))
    character_models: MSBEntryList[MSBCharacterModel] = field(default_factory=empty("MODEL", "CharacterModel"))
    player_models: MSBEntryList[MSBPlayerModel] = field(default_factory=empty("MODEL", "PlayerModel"))
    collision_models: MSBEntryList[MSBCollisionModel] = field(default_factory=empty("MODEL", "CollisionModel"))
    navmesh_models: MSBEntryList[MSBNavmeshModel] = field(default_factory=empty("MODEL", "NavmeshModel"))

    lights: MSBEntryList[MSBLightEvent] = field(default_factory=empty("EVENT", "Light"))
    sounds: MSBEntryList[MSBSoundEvent] = field(default_factory=empty("EVENT", "Sound"))
    vfx: MSBEntryList[MSBVFXEvent] = field(default_factory=empty("EVENT", "VFX"))
    wind: MSBEntryList[MSBWindEvent] = field(default_factory=empty("EVENT", "Wind"))
    treasures: MSBEntryList[MSBTreasureEvent] = field(default_factory=empty("EVENT", "Treasure"))
    spawners: MSBEntryList[MSBSpawnerEvent] = field(default_factory=empty("EVENT", "Spawner"))
    messages: MSBEntryList[MSBMessageEvent] = field(default_factory=empty("EVENT", "Message"))
    obj_acts: MSBEntryList[MSBObjActEvent] = field(default_factory=empty("EVENT", "ObjAct"))
    spawn_points: MSBEntryList[MSBSpawnPointEvent] = field(default_factory=empty("EVENT", "SpawnPoint"))
    map_offsets: MSBEntryList[MSBMapOffsetEvent] = field(default_factory=empty("EVENT", "MapOffset"))
    navigation: MSBEntryList[MSBNavigationEvent] = field(default_factory=empty("EVENT", "Navigation"))
    environments: MSBEntryList[MSBEnvironmentEvent] = field(default_factory=empty("EVENT", "Environment"))
    npc_invasions: MSBEntryList[MSBNPCInvasionEvent] = field(default_factory=empty("EVENT", "NPCInvasion"))

    regions: MSBEntryList[MSBRegion] = field(default_factory=empty("POINT", "All"))

    map_pieces: MSBEntryList[MSBMapPiece] = field(default_factory=empty("PARTS", "MapPiece"))
    objects: MSBEntryList[MSBObject] = field(default_factory=empty("PARTS", "Object"))
    characters: MSBEntryList[MSBCharacter] = field(default_factory=empty("PARTS", "Character"))
    player_starts: MSBEntryList[MSBPlayerStart] = field(default_factory=empty("PARTS", "PlayerStart"))
    collisions: MSBEntryList[MSBCollision] = field(default_factory=empty("PARTS", "Collision"))
    navmeshes: MSBEntryList[MSBNavmesh] = field(default_factory=empty("PARTS", "Navmesh"))
    unused_objects: MSBEntryList[MSBDummyObject] = field(default_factory=empty("PARTS", "DummyObject"))
    unused_characters: MSBEntryList[MSBDummyCharacter] = field(default_factory=empty("PARTS", "DummyCharacter"))
    connect_collisions: MSBEntryList[MSBConnectCollision] = field(default_factory=empty("PARTS", "ConnectCollision"))

    @property
    def region_points(self) -> MSBEntryList[MSBRegion]:
        return MSBEntryList(
            [region for region in self.regions if region.shape_type == RegionShapeType.Point],
            supertype=MSBSupertype.REGIONS,
            subtype_info=None,
        )

    @property
    def region_volumes(self) -> MSBEntryList[MSBRegion]:
        volume_types = RegionShapeType.get_volume_types()
        return MSBEntryList(
            [region for region in self.regions if region.shape_type in volume_types],
            supertype=MSBSupertype.REGIONS,
            subtype_info=None,
        )

    def pack_supertype_name(self, writer: BinaryWriter, supertype_name: str):
        packed_name = supertype_name.encode(self.NAME_ENCODING)
        packed_name += b"\0" * (16 - len(packed_name))  # pad to 16 characters (NOTE: 32 in older Soulstruct)
        writer.append(packed_name)

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
    def set_auto_references(self):
        """Look at all `MSBEnvironmentEvent` instances and update the `MSBCollision` they point to so it refers back
        to the same Environment event (cubemap).

        Raises a `ValueError` if multiple Environment events reference the same Collision, which should never happen.
        """
        done_collisions = IDList()
        for environment in self.environments:
            if not environment.attached_part:
                continue
            if environment.attached_part in done_collisions:
                raise ValueError(
                    f"Multiple Environment events reference the same Collision: {environment.attached_part.name}"
                )
            done_collisions.append(environment.attached_part)
            environment.attached_part.environment_event = environment

    def duplicate_collision_with_environment_event(
        self, collision: MSBCollision | str, at_next_index=True, **kwargs,
    ) -> MSBCollision:
        """Duplicate a Collision and any attached `MSBEnvironment` instance and its region."""
        if "name" not in kwargs:
            raise ValueError(f"Must pass `name` to Collision duplication call to duplicate attached environment event.")
        if not isinstance(collision, MSBCollision):
            collision = self.collisions.find_entry_name(collision)
        name = kwargs["name"]
        new_collision = self.collisions.duplicate(collision, at_next_index=at_next_index, **kwargs)
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
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
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
        translate: Vector3,
        rotate: Vector3,
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
        point = self.regions.new(
            name=point_name,
            entity_id=point_entity_id,
            translate=translate,
            rotate=rotate,
            shape=PointShape(),
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
        point = self.regions.new(
            name=f"_SpawnPointEvent_{spawn_point.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            shape=PointShape(),
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
        point = self.regions.new(
            name=f"_MessageEvent_{message.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            shape=PointShape(),
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
            obj_act_part=obj,
            obj_act_entity_id=obj_act_entity_id,
            obj_act_param_id=obj_act_param_id,
            obj_act_state=obj_act_state,
            obj_act_flag=obj_act_flag,
        )
