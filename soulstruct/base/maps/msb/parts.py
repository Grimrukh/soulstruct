from __future__ import annotations

__all__ = [
    "MSBPart",
    "MSBMapPiece",
    "MSBObject",
    "MSBCharacter",
    "MSBPlayerStart",
    "MSBCollision",
    "MSBNavmesh",
    "MSBUnusedObject",
    "MSBUnusedCharacter",
    "MSBMapConnection",
    "MSBPartList",
]

import abc
import logging
import typing as tp
import struct

from soulstruct.exceptions import InvalidFieldValueError, SoulstructError
from soulstruct.game_types import *
from soulstruct.utilities import partialmethod
from soulstruct.utilities.binary_struct import BinaryStruct
from soulstruct.utilities.maths import Vector3

from .enums import CollisionHitFilter, MSBPartSubtype
from .msb_entry import MSBEntryList, MSBEntryEntityCoordinates
from .utils import MapFieldInfo

if tp.TYPE_CHECKING:
    from .core import MSB
    from .events import MSBEnvironmentEvent
    from .regions import MSBRegion

_LOGGER = logging.getLogger(__name__)


class MSBPart(MSBEntryEntityCoordinates, abc.ABC):

    ENTRY_SUBTYPE: MSBPartSubtype = None
    PART_HEADER_STRUCT: BinaryStruct = None
    PART_BASE_DATA_STRUCT: BinaryStruct = None
    PART_TYPE_DATA_STRUCT: BinaryStruct = None
    NAME_ENCODING = ""
    FLAG_SET_SIZE = 128

    FIELD_INFO = MSBEntryEntityCoordinates.FIELD_INFO | {
        "sib_path": MapFieldInfo(
            "SIB Path",
            str,
            "",
            "Internal path to SIB placeholder file for part.",
        ),
        "scale": MapFieldInfo(
            "Scale",
            Vector3,
            Vector3.ones(),
            "Scale of part. Only works for Map Pieces.",  # TODO: and maybe Objects?
        ),
        # Every concrete subclass defines 'model_name', 'draw_groups', and 'display_groups'.
    }

    sib_path: str
    scale: Vector3
    model_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._part_type_index = -1
        self._model_index = -1
        self._draw_groups = set()
        self._display_groups = set()
        super().__init__(source=source, **kwargs)

    def unpack_type_data(self, msb_buffer):
        """This unpacks simple attributes by default, but some Parts need to process these values more."""
        self.set(**self.PART_TYPE_DATA_STRUCT.unpack(msb_buffer, exclude_asserted=True))

    def pack_type_data(self):
        try:
            return self.PART_TYPE_DATA_STRUCT.pack_from_object(self)
        except struct.error:
            raise SoulstructError(f"Could not pack type data of MSB part '{self.name}'. See traceback.")

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        self._part_type_index = part_type_index
        try:
            self._model_index = model_indices[self.model_name] if self.model_name else -1
        except KeyError:
            raise KeyError(
                f"Invalid model name for {self.ENTRY_SUBTYPE.name} {self.name} (entity ID {self.entity_id}): "
                f"{self.model_name}"
            )

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        if self._model_index != -1:
            try:
                self.model_name = model_names[self._model_index]
            except KeyError:
                raise KeyError(
                    f"Invalid model index for {self.ENTRY_SUBTYPE.name} {self.name} (entity ID {self.entity_id}): "
                    f"{self._model_index}"
                )
        else:
            self.model_name = None

    @property
    def draw_groups(self):
        return self._draw_groups

    @draw_groups.setter
    def draw_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._draw_groups = set()
            return
        try:
            draw_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Draw groups must be a set, sequence, `None`, 'None', or ''. Or use `set` methods like `.add()`."
            )
        for i in draw_groups:
            if not isinstance(i, int) and 0 <= i < self.FLAG_SET_SIZE:
                raise InvalidFieldValueError(f"Invalid draw group: {i}. Must be 0 <= i < {self.FLAG_SET_SIZE}.")
        self._draw_groups = draw_groups

    @property
    def display_groups(self):
        return self._display_groups

    @display_groups.setter
    def display_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._display_groups = set()
            return
        try:
            display_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Display groups must be a set, sequence, `None`, 'None', or ''. Or use `set` methods like `.add()`."
            )
        for i in display_groups:
            if not isinstance(i, int) and 0 <= i < self.FLAG_SET_SIZE:
                raise ValueError(f"Invalid display group: {i}. Must be 0 <= i < {self.FLAG_SET_SIZE}.")
        self._display_groups = display_groups


class MSBMapPiece(MSBPart, abc.ABC):
    """Just a textured, visible mesh asset. Does not include any collision."""

    ENTRY_SUBTYPE = MSBPartSubtype.MapPiece
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        "8x",
    )

    FIELD_INFO = {
        "model_name": MapFieldInfo(
            "Model Name",
            MapPieceModel,
            None,
            "Name of map piece model to use for this map piece.",
        ),
    }

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
    )


class MSBObject(MSBPart, abc.ABC):
    """Instance of a physical object."""

    ENTRY_SUBTYPE = MSBPartSubtype.Object
    PART_TYPE_DATA_STRUCT: BinaryStruct = None  # Differs per game.

    FIELD_INFO = {
        "model_name": MapFieldInfo(
            "Model Name",
            ObjectModel,
            None,
            "Name of object model to use for this object.",
        ),
        "draw_parent_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Object will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn. Used as "
            "a simpler alternative to draw groups (unsure what will take precedence if any draw groups are set).",
        ),
    }

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        # "scale",
        "draw_parent_name",
        "draw_groups",
        # "display_groups",
    )

    draw_parent_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._draw_parent_index = -1
        super().__init__(source, **kwargs)

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        super().set_indices(
            part_type_index,
            model_indices,
            local_environment_indices,
            region_indices,
            part_indices,
            local_collision_indices,
        )
        self._draw_parent_index = part_indices[self.draw_parent_name] if self.draw_parent_name else -1

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        super().set_names(
            model_names, environment_names, region_names, part_names, collision_names,
        )
        self.draw_parent_name = part_names[self._draw_parent_index] if self._draw_parent_index != -1 else None


class MSBCharacter(MSBPart, abc.ABC):
    """Physical character instance."""

    ENTRY_SUBTYPE = MSBPartSubtype.Character
    PART_TYPE_DATA_STRUCT: BinaryStruct = None  # Differs for each game (slightly).

    FIELD_INFO = {
        "model_name": MapFieldInfo(
            "Model Name",
            CharacterModel,
            "c1000",  # empty character should be present in every map
            "Name of character model to use for this character.",
        ),
        "ai_id": MapFieldInfo(
            "AI ID",
            AIParam,
            -1,
            "Character's AI param ID. If set to -1, the default AI ID from the Character param (below) will be used.",
        ),
        "character_id": MapFieldInfo(
            "Character ID",
            CharacterParam,
            -1,
            "Character's main Character param ID, which contains basic character information. For 'player' characters "
            "who use model c0000, most of the fields in this param are unused (e.g. health is determined by their "
            "Vitality stat rather than the HP field in this param).",
        ),
        "talk_id": MapFieldInfo(
            "Talk ID",
            TalkScript,
            0,
            "Talk ID of character, which determines their interactions (conversations, shops, etc.). This is used "
            "to look up the corresponding 't{talk_id}.esd' file inside the 'talkesdbnd' file for this map.",
        ),
        "player_id": MapFieldInfo(
            "Player ID",
            PlayerParam,
            -1,
            "Player ID of character, which is used to initialize the stats, appearance, equipment, etc. of 'player' "
            "characters ('NPCs') who use model c0000. Unused (-1) for all other character models.",
        ),
        "draw_parent_name": MapFieldInfo(
            "Draw Parent",
            MapPart,
            None,
            "Character will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn. Used as "
            "a simpler alternative to draw groups (unsure what will take precedence if any draw groups are set).",
        ),
        "patrol_region_names": MapFieldInfo(
            "Patrol Regions",
            GameObjectSequence((Region, 8)),  # all supported games so far have eight slots
            [None] * 8,
            "List of region names that this character will patrol between (if they have standard AI logic).",
        ),
        "default_animation": MapFieldInfo(
            "Default Animation",
            int,  # TODO: Animation
            -1,
            "Default standby animation to loop for character (e.g. sitting, leaning, clutching head in hands).",
        ),
        "damage_animation": MapFieldInfo(
            "Damage Animation",
            int,  # TODO: Animation
            -1,
            "Default damage animation to use for character.",
        ),
    }

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        # "scale",
        "draw_parent_name",
        "draw_groups",
        # "display_groups",
        "player_id",
        "character_id",
        "ai_id",
        "talk_id",
        "patrol_region_names",
        "default_animation",
        "damage_animation",
    )

    ai_id: int
    character_id: int
    talk_id: int
    player_id: int
    draw_parent_name: tp.Optional[str]
    default_animation: int
    damage_animation: int

    def __init__(self, source=None, **kwargs):
        self._draw_parent_index = -1
        self._patrol_region_names = [None] * 8
        self._patrol_region_indices = [-1] * 8
        super().__init__(source=source, **kwargs)

    @property
    def patrol_region_names(self):
        return self._patrol_region_names

    @patrol_region_names.setter
    def patrol_region_names(self, value):
        """Pads out to eight names with `None`. Also replaces empty strings with `None`."""
        names = []
        for v in value:
            if v is not None and not isinstance(v, str):
                raise TypeError("Patrol point names must be strings or `None`.")
            names.append(v if v else None)
        self._patrol_region_names = value
        while len(self._patrol_region_names) < 8:
            self._patrol_region_names.append(None)

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        super().set_indices(
            part_type_index,
            model_indices,
            local_environment_indices,
            region_indices,
            part_indices,
            local_collision_indices,
        )
        self._draw_parent_index = part_indices[self.draw_parent_name] if self.draw_parent_name else -1
        self._patrol_region_indices = [region_indices[n] if n else -1 for n in self._patrol_region_names]
        while len(self._patrol_region_indices) < 8:
            self._patrol_region_indices.append(-1)

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        super().set_names(
            model_names, environment_names, region_names, part_names, collision_names,
        )
        self.draw_parent_name = part_names[self._draw_parent_index] if self._draw_parent_index != -1 else None
        self._patrol_region_names = [region_names[i] if i != -1 else None for i in self._patrol_region_indices]


class MSBPlayerStart(MSBPart, abc.ABC):
    """Starting point for the player character (e.g. a warp point). No additional data.

    Note that these are distinct from Spawn Point events, which are used much more often (e.g. bonfires).

    If the player's position within a given map is lost by the game, they will respawn at the Player Start with entity
    ID -1.
    """

    ENTRY_SUBTYPE = MSBPartSubtype.PlayerStart
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        "16x",
    )

    FIELD_INFO = {
        "model_name": MapFieldInfo(
            "Model Name",
            CharacterModel,
            "c0000",
            "Name of character model to use for this PlayerStart. This should always be c0000.",
        ),
    }

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
    )

    def __init__(self, source=None, **kwargs):
        if source is None:
            kwargs.setdefault("model_name", "c0000")
        super().__init__(source=source, **kwargs)


class MSBCollision(MSBPart, abc.ABC):
    """Physical Collision geometry. Usually these are floor pieces."""

    ENTRY_SUBTYPE = MSBPartSubtype.Collision

    FIELD_INFO = {
        "display_groups": MapFieldInfo(  # overwrites `MSBPart` definition
            "Display Groups",
            list,
            set(range(MSBPart.FLAG_SET_SIZE)),
            "Display groups of collision. These display groups will be active when the player is standing on this "
            "Collision, which will draw any parts with an overlapping draw group.",
        ),
        "model_name": MapFieldInfo(
            "Model Name",
            CollisionModel,
            None,
            "Name of collision model to use for this collision.",
        ),
        "hit_filter_id": MapFieldInfo(
            "Hit Filter ID",
            CollisionHitFilter,
            CollisionHitFilter.Normal,
            "Determines what happens when the player activates this collision (normal physics, killplane, etc.).",
        ),
        "sound_space_type": MapFieldInfo(
            "Sound Space Type",
            int,  # TODO: document enum
            0,
            "Determines how sounds are filtered when player is standing on this collision.",
        ),
        "environment_event_name": MapFieldInfo(
            "Environment Event",
            EnvironmentEvent,
            None,
            "Environment event name in map that determines ambience when standing on this collision.",
        ),
        "reflect_plane_height": MapFieldInfo(
            "Reflect Plane Height",
            float,
            0.0,
            "Vertical height of the reflect plane for this collision.",
        ),
        "area_name_id": MapFieldInfo(
            "Area Name",
            PlaceName,
            -1,
            "Name of area that this collision is in, which determines the area banner that is shown when you step on "
            "this collision (a linked texture ID lookup) and the area name that appears in the load screen (text ID). "
            "Set it to -1 to use the default area name for this map (i.e. text ID XXYY for map 'mXX_YY').",
        ),
        "force_area_banner": MapFieldInfo(
            "Show Area Banner",
            bool,
            True,  # necessary because `area_name_id` defaults to -1
            "By default, the game will only show an area name banner when you enter a map (e.g. after warping). If "
            "this option is enabled, the area name banner will be shown when you step on this collision if the area ID "
            "changes to a new value. Typical usage is to have this disabled for collisions that are very close to a "
            "different area (a 'silent area transition') and have it enabled for collisions that are further away, "
            "which produces a 'delayed area banner' effect.\n\n"
            ""
            "Do NOT enable this for two adjacent collisions with different area names, or moving back and forth "
            "between those collisions will build up a huge queue of area banners to display, which can only be cleared "
            "by restarting the game entirely.",
        ),
        "starts_disabled": MapFieldInfo(
            "Starts Disabled",
            bool,
            False,
            "If True, this collision is disabled on map load and must be manually enabled with an event script.",
        ),
        "attached_bonfire": MapFieldInfo(
            "Attached Bonfire",
            int,
            -1,
            "If this is set to a bonfire entity ID, that bonfire will be unusable if any living enemy characters are "
            "on this collision. Note that this also checks for enemies that are disabled by events.",
        ),
        "play_region_id": MapFieldInfo(
            "Play Region ID",
            int,
            0,
            "Determines the multiplayer (e.g. invasion) sub-area this collision is part of. If set to 0 (default), no "
            "multiplayer activity can occur while the player is on this collision.\n\n"
            ""
            "NOTE: This field shares space with Stable Footing Flag, so only one of them can be set to a non-zero "
            "value per collision.",
        ),
        "stable_footing_flag": MapFieldInfo(
            "Stable Footing Flag",
            int,
            0,
            "This flag must be enabled for the player's stable footing (i.e. last saved position) to be updated while "
            "standing on this collision. This is used to prevent players loading inside boss arenas before the boss is "
            "defeated. If set to 0 (default), stable footing is ALWAYS updated here. If set to -1, stable footing is "
            "NEVER updated here.\n\n"
            ""
            "NOTE: This field shares space with Play Region ID, so only one of them can be set to a non-zero value "
            "per collision.",
        ),
        "camera_1_id": MapFieldInfo(
            "Camera Param ID 1",
            CameraParam,
            -1,
            "First camera ID to use on this collision. Unsure how the two slots differ.",
        ),
        "camera_2_id": MapFieldInfo(
            "Camera Param ID 2",
            CameraParam,
            -1,
            "Second camera ID to use on this collision. Unsure how the two slots differ.",
        ),
    }

    hit_filter_id: CollisionHitFilter
    sound_space_type: int
    environment_event_name: tp.Optional[str]
    reflect_plane_height: float
    area_name_id: int
    starts_disabled: bool
    attached_bonfire: int
    camera_1_id: int
    camera_2_id: int

    def __init__(self, source=None, **kwargs):
        self._environment_event_index = -1
        self._force_area_banner = False  # Custom field (see property).
        self._play_region_id = 0
        self._stable_footing_flag = 0
        super().__init__(source=source, **kwargs)

    def unpack_type_data(self, msb_buffer):
        data = self.PART_TYPE_DATA_STRUCT.unpack(msb_buffer, exclude_asserted=True)
        self.set(**data)
        self.area_name_id = abs(data["__area_name_id"]) if data["__area_name_id"] != -1 else -1
        self._force_area_banner = data["__area_name_id"] < 0  # Custom field.
        if data["__play_region_id"] > -10:
            self._play_region_id = data["__play_region_id"]
            self._stable_footing_flag = 0
        else:
            self._play_region_id = 0
            self._stable_footing_flag = -data["__play_region_id"] - 10

    @property
    def force_area_banner(self):
        return self._force_area_banner

    @force_area_banner.setter
    def force_area_banner(self, value: bool):
        if not value and self.area_name_id == -1:
            raise InvalidFieldValueError(
                "Banner must appear when area name is set to default (-1). You must specify the area name manually to "
                "set this to False."
            )
        self._force_area_banner = bool(value)

    @property
    def play_region_id(self):
        return self._play_region_id

    @play_region_id.setter
    def play_region_id(self, value):
        if self._stable_footing_flag != 0:
            raise InvalidFieldValueError(
                "Cannot set 'play_region_id' to a non-zero value while 'stable_footing_flag' " "is non-zero."
            )
        if not isinstance(value, int) or value <= -10:
            raise InvalidFieldValueError("'play_region_id' must be an integer greater than or equal to -9.")
        self._play_region_id = value

    @property
    def stable_footing_flag(self):
        return self._stable_footing_flag

    @stable_footing_flag.setter
    def stable_footing_flag(self, value):
        if self._play_region_id != 0:
            raise InvalidFieldValueError(
                "Cannot set 'stable_footing_flag' to a non-zero value while 'play_region_id' " "is non-zero."
            )
        if not isinstance(value, int) or value < 0:
            raise InvalidFieldValueError("'stable_footing_flag' must be an integer greater than or equal to 0.")
        self._stable_footing_flag = value

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        super().set_indices(
            part_type_index,
            model_indices,
            local_environment_indices,
            region_indices,
            part_indices,
            local_collision_indices,
        )
        if self.environment_event_name:
            self._environment_event_index = local_environment_indices[self.environment_event_name]
        else:
            self._environment_event_index = -1

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        super().set_names(
            model_names, environment_names, region_names, part_names, collision_names,
        )
        if self._environment_event_index != -1:
            try:
                self.environment_event_name = environment_names[self._environment_event_index]
            except IndexError:
                for i, env in enumerate(environment_names):
                    print(i, env)
                print(self._environment_event_index)
                self.environment_event_name = f"BROKEN ({self._environment_event_index})"
        else:
            self.environment_event_name = None


class MSBNavmesh(MSBPart, abc.ABC):
    """AI navigation mesh ('navmesh'). Often called 'navimesh' in the game files.

    Note that these are distinct from 'Navigation' events, which define regions that highlight part of these physical
    navmeshes that can have their state controlled in EMEVD.
    """

    ENTRY_SUBTYPE = MSBPartSubtype.Navmesh

    FIELD_INFO = {
        "model_name": MapFieldInfo(
            "Model Name",
            NavmeshModel,
            None,
            "Name of navmesh model to use for this navmesh.",
        ),
    }

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
    )


class MSBUnusedObject(MSBObject, abc.ABC):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to `MSBObject`."""

    ENTRY_SUBTYPE = MSBPartSubtype.UnusedObject


class MSBUnusedCharacter(MSBCharacter, abc.ABC):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`."""

    ENTRY_SUBTYPE = MSBPartSubtype.UnusedCharacter


class MSBMapConnection(MSBPart, abc.ABC):
    """Links to an `MSBCollision` entry and causes another specified map to load into backread when the linked collision
    is itself in backread in the current map.

    Note that sensible draw, display, and navmesh groups are still needed to advance the backread state of the
    connected map's collisions to an interactive state (while map pieces don't care about navmesh groups).

    Uses collision models, and almost always has the same model as the linked `MSBCollision`.
    """

    ENTRY_SUBTYPE = MSBPartSubtype.MapConnection
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        ("collision_index", "i"),
        ("map_id", "4b"),
        "8x",
    )
    GET_MAP: tp.Callable[..., Map] = None

    FIELD_INFO = {
        "model_name": MapFieldInfo(
            "Collision Model Name",
            CollisionModel,
            None,
            "Name of collision model to use for this map load trigger.",
        ),
        "collision_name": MapFieldInfo(
            "Collision Part Name",
            Collision,
            None,
            "Collision part that triggers this map load.",
        ),
        # 'connected_map' field is defined in subclass so proper default map can be specified.
    }

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "draw_groups",
        "display_groups",
        "collision_name",
        "connected_map",
    )

    collision_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._collision_index = -1
        self._connected_map = None
        super().__init__(source=source, **kwargs)

    def unpack_type_data(self, msb_buffer):
        data = self.PART_TYPE_DATA_STRUCT.unpack(msb_buffer)
        self._collision_index = data["collision_index"]
        area_id, block_id, _, _ = data["map_id"]
        self._connected_map = self.GET_MAP(area_id, block_id)

    def pack_type_data(self):
        return self.PART_TYPE_DATA_STRUCT.pack(
            collision_index=self._collision_index,
            map_id=self._connected_map.map_load_tuple,  # note use of EMEVD file stem
        )

    @property
    def connected_map(self) -> Map:
        return self._connected_map

    @connected_map.setter
    def connected_map(self, value):
        self._connected_map = self.GET_MAP(value)

    def set_indices(
        self,
        part_type_index,
        model_indices,
        local_environment_indices,
        region_indices,
        part_indices,
        local_collision_indices,
    ):
        super().set_indices(
            part_type_index,
            model_indices,
            local_environment_indices,
            region_indices,
            part_indices,
            local_collision_indices,
        )
        self._collision_index = local_collision_indices[self.collision_name] if self.collision_name else -1

    def set_names(
        self, model_names, region_names, environment_names, part_names, collision_names,
    ):
        super().set_names(
            model_names, environment_names, region_names, part_names, collision_names,
        )
        self.collision_name = collision_names[self._collision_index] if self._collision_index != -1 else None


class MSBPartList(MSBEntryList[MSBPart], abc.ABC):
    ENTRY_LIST_NAME = "Parts"
    ENTRY_SUBTYPE_ENUM = MSBPartSubtype
    SUBTYPE_CLASSES: dict[MSBPartSubtype, tp.Type[MSBPart]] = {}
    SUBTYPE_OFFSET = -1  # type: int
    GET_MAP = None  # type: tp.Callable

    _entries: list[MSBPart]

    MapPieces: tp.Sequence[MSBMapPiece]
    Objects: tp.Sequence[MSBObject]
    Characters: tp.Sequence[MSBCharacter]
    PlayerStarts: tp.Sequence[MSBPlayerStart]
    Collisions: tp.Sequence[MSBCollision]
    Navmeshes: tp.Sequence[MSBNavmesh]
    UnusedObjects: tp.Sequence[MSBUnusedObject]
    UnusedCharacters: tp.Sequence[MSBUnusedCharacter]
    MapConnections: tp.Sequence[MSBMapConnection]

    new = MSBEntryList.new
    new_map_piece: tp.Callable[..., MSBMapPiece] = partialmethod(new, MSBPartSubtype.MapPiece)
    new_object: tp.Callable[..., MSBObject] = partialmethod(new, MSBPartSubtype.Object)
    new_character: tp.Callable[..., MSBCharacter] = partialmethod(new, MSBPartSubtype.Character)
    new_player_start: tp.Callable[..., MSBPlayerStart] = partialmethod(new, MSBPartSubtype.PlayerStart)
    new_collision: tp.Callable[..., MSBCollision] = partialmethod(new, MSBPartSubtype.Collision)
    new_navmesh: tp.Callable[..., MSBNavmesh] = partialmethod(new, MSBPartSubtype.Navmesh)
    new_unused_object: tp.Callable[..., MSBUnusedObject] = partialmethod(new, MSBPartSubtype.UnusedObject)
    new_unused_character: tp.Callable[..., MSBUnusedCharacter] = partialmethod(new, MSBPartSubtype.UnusedCharacter)
    new_map_connection: tp.Callable[..., MSBMapConnection] = partialmethod(new, MSBPartSubtype.MapConnection)

    def pack_entry(self, index: int, entry: MSBPart):
        return entry.pack()

    def set_indices(
        self, model_indices, local_environment_indices, region_indices, part_indices, local_collision_indices,
    ):
        """Local type-specific index only.

        Events and other Parts may point to Parts by global entry index, but it seems the local index still matters, as
        ObjAct Events seem to break when the local object index is changed. It's possible this was just an idiosyncrasy
        of Wulf's MSB Editor. Either way, this method should ensure the global and local indices are consistent.

        Remember that Navmesh indices are hard-coded into MCP and MCG files. Also note that cutscene files (remo) access
        MSB parts by index as well, which is why map mods tend to break them so often.

        `local_environment_indices` are needed for Collisions and `local_collision_indices` are needed for Map Load
        Triggers. No other MSB entry type requires local subtype indices.
        """
        type_indices = {}
        for entry in self._entries:
            try:
                entry.set_indices(
                    part_type_index=type_indices.setdefault(entry.ENTRY_SUBTYPE, 0),
                    model_indices=model_indices,
                    local_environment_indices=local_environment_indices,
                    region_indices=region_indices,
                    part_indices=part_indices,
                    local_collision_indices=local_collision_indices,
                )
            except KeyError as e:
                raise SoulstructError(f"Missing name referenced by {entry.name}: {str(e)}")
            else:
                type_indices[entry.ENTRY_SUBTYPE] += 1

    def set_names(
        self, model_names, environment_names, region_names, part_names, collision_names,
    ):
        for entry in self._entries:
            entry.set_names(
                model_names, region_names, environment_names, part_names, collision_names,
            )

    def get_instance_counts(self):
        """Returns a dictionary mapping model names to part instance counts."""
        instance_counts = {}
        for entry in self._entries:
            instance_counts.setdefault(entry.model_name, 0)
            instance_counts[entry.model_name] += 1
        return instance_counts

    # ------------------------------------- #
    # Additional special creation functions #
    # ------------------------------------- #

    def duplicate_collision_with_environment_event(
        self, collision, msb: MSB, insert_below_original=True, **kwargs,
    ) -> MSBCollision:
        """Duplicate a Collision and any attached `MSBEnvironment` instance and its region."""
        if "name" not in kwargs:
            raise ValueError(f"Must pass `name` to Collision duplication call to duplicate attached environment event.")
        new_collision = self.new_collision(
            copy_entry=collision, insert_below_original=insert_below_original, **kwargs,
        )
        if new_collision.environment_event_name is None:
            return new_collision

        try:
            environment_event: MSBEnvironmentEvent = msb.events.get_entry_by_name(
                new_collision.environment_event_name, "Environment",
            )
        except KeyError:
            raise KeyError(f"Could not find environment event '{new_collision.environment_event_name}' in MSB.")
        if not environment_event.base_region_name:
            raise AttributeError(f"Environment event '{environment_event.name}' has no anchor Region.")
        try:
            environment_region: MSBRegion = msb.regions.get_entry_by_name(environment_event.base_region_name)
        except KeyError:
            raise KeyError(f"Could not find environment region '{environment_event.base_region_name}' in MSB.")
        new_region = msb.regions.duplicate_entry(environment_region, name=f"GI Region ({kwargs['name']})")
        new_event = msb.events.duplicate_entry(environment_event, name=f"GI Event ({kwargs['name']})")
        new_event.base_region_name = new_region.name
        new_collision.environment_event_name = new_event.name
        return new_collision

    def create_map_connection_from_collision(
        self, collision, connected_map, name=None, draw_groups=None, display_groups=None
    ):
        """Creates a new `MapConnection` that references and copies the transform of the given `collision`.

        The `name` and `map_id` of the new `MapConnection` must be given. You can also specify its `draw_groups` and
        `display_groups`. Otherwise, it will leave them as the extensive default values: [0, ..., 127].
        """
        if not isinstance(collision, MSBCollision):
            collision = self.get_entry_by_name(collision, "Collision")
        if name is None:
            game_map = self.GET_MAP(connected_map)
            name = collision.name + f"_[{game_map.area_id:02d}_{game_map.block_id:02d}]"
        if name in self.get_entry_names("MapConnection"):
            raise ValueError(f"{repr(name)} is already the name of an existing MapConnection.")
        map_connection = self.SUBTYPE_CLASSES[MSBPartSubtype.MapConnection](
            name=name,
            connected_map=connected_map,
            collision_name=collision.name,
            translate=collision.translate.copy(),
            rotate=collision.rotate.copy(),
            scale=collision.scale.copy(),  # for completion's sake
            model_name=collision.model_name,
        )
        if draw_groups is not None:  # otherwise keep same draw groups
            map_connection.draw_groups = draw_groups
        if display_groups is not None:  # otherwise keep same display groups
            map_connection.display_groups = display_groups
        self.add_entry(map_connection)
        return map_connection

    def new_c1000(self, name, **kwargs) -> MSBCharacter:
        """Useful to create basic c1000 instances as debug warp points."""
        return self.new_character(name=name, model_name="c1000", **kwargs)


for _entry_subtype in MSBPartSubtype:
    setattr(
        MSBPartList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
