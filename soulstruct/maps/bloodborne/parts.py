__all__ = [
    "MSBPart",
    "MSBMapPiece",
    "MSBObject",
    "MSBCharacter",
    "MSBPlayerStart",
    "MSBCollision",
    "MSBUnusedObject",
    "MSBUnusedCharacter",
    "MSBNavmesh",
    "MSBMapConnection",
    "MSBPartList",
]

import struct

from soulstruct.game_types import *
from soulstruct.maps import MapError
from soulstruct.maps.base.parts import (
    MSBPart as _BaseMSBPart,
    MSBPartList as _BaseMSBPartList,
    MSBMapPiece as _BaseMSBMapPiece,
    MSBObject as _BaseMSBObject,
    MSBCharacter as _BaseMSBCharacter,
    MSBPlayerStart as _BaseMSBPlayerStart,
    MSBCollision as _BaseMSBCollision,
    MSBNavmesh as _BaseMSBNavmesh,
    MSBMapConnection as _BaseMSBMapConnection,
)
from soulstruct.maps.enums import CollisionHitFilter, MSBPartSubtype
from soulstruct.utilities import BinaryStruct, read_chars_from_buffer
from soulstruct.utilities.conversion import int_group_to_bit_set, bit_set_to_int_group
from soulstruct.utilities.maths import Vector3

from .maps import get_map
from .msb_entry import MSBEntryList


class MSBPart(_BaseMSBPart):
    PART_HEADER_STRUCT = BinaryStruct(
        ("__description_offset", "q"),
        ("__name_offset", "q"),
        ("_instance_index", "i"),  # TK says "Unknown; appears to count up with each instance of a model added."
        ("__part_type", "i"),
        ("_part_type_index", "i"),
        ("_model_index", "i"),
        ("__sib_path_offset", "q"),
        ("translate", "3f"),
        ("rotate", "3f"),
        ("scale", "3f"),
        ("__draw_groups", "8I"),
        ("__display_groups", "8I"),
        ("__backread_groups", "8I"),
        "4x",
        ("__base_data_offset", "q"),
        ("__type_data_offset", "q"),
        ("__gparam_data_offset", "q"),
        ("__scene_gparam_data_offset", "q"),
    )

    PART_BASE_DATA_STRUCT = BinaryStruct(
        ("entity_id", "i"),
        ("base_unk_x04_x05", "b"),
        ("base_unk_x05_x06", "b"),
        ("base_unk_x06_x07", "b"),
        ("base_unk_x07_x08", "b"),
        "4x",
        ("lantern_id", "b"),
        ("lod_id", "b"),
        ("base_unk_x0e_x0f", "b"),
        ("base_unk_x0f_x10", "b"),
    )

    PART_GPARAM_STRUCT = None  # type: BinaryStruct
    PART_SCENE_GPARAM_STRUCT = None  # type: BinaryStruct

    NAME_ENCODING = "utf-16-le"

    FIELD_INFO = {
        "entity_id": (
            "Entity ID",
            int,
            "Entity ID used to refer to the part in other game files.",
        ),
        "translate": (
            "Translate",
            Vector3,
            "3D coordinates of the part's position. Note that the anchor of the part is usually at its base.",
        ),
        "rotate": (
            "Rotate",
            Vector3,
            "Euler angles for part rotation around its local X, Y, and Z axes.",
        ),
        "scale": (
            "Scale",
            Vector3,
            "Scale of part. Only works for map pieces.",
        ),
        "draw_groups": (
            "Draw Groups",
            list,
            "Draw groups of part. This part will be drawn when the corresponding display group is active.",
        ),
        "display_groups": (
            "Display Groups",
            list,
            "Display groups are present in all MSB Parts, but only function for collisions.",
        ),
        "backread_groups": (
            "Backread Groups",
            list,
            "Backread groups are present in all MSB Parts, but only function for collisions (maybe).",
        ),
    }

    # This base list will always be overridden by concrete subclasses, but it's here for reference.
    FIELD_NAMES = (
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "backread_groups",
    )

    def __init__(self, msb_part_source=None):
        self._draw_groups = set(range(256))  # {0, 1, 2, ..., 255}
        self._display_groups = set(range(256))  # {0, 1, 2, ..., 255}
        self._backread_groups = set(range(256))  # {0, 1, 2, ..., 255}
        self._instance_index = 0

        # Base data
        self.base_unk_x04_x05 = 0
        self.base_unk_x05_x06 = 0
        self.base_unk_x06_x07 = 0
        self.base_unk_x07_x08 = 0
        self.lantern_id = 0
        self.lod_id = 0
        self.base_unk_x0e_x0f = 0
        self.base_unk_x0f_x10 = 0

        super().__init__(msb_part_source)

    def unpack(self, msb_buffer):
        part_offset = msb_buffer.tell()

        header = self.PART_HEADER_STRUCT.unpack(msb_buffer)
        if header["__part_type"] != self.ENTRY_SUBTYPE:
            raise ValueError(f"Unexpected part type enum {header['part_type']} for class {self.__class__.__name__}.")
        self._instance_index = header["_instance_index"]
        self._model_index = header["_model_index"]
        self._part_type_index = header["_part_type_index"]
        for transform in ("translate", "rotate", "scale"):
            setattr(self, transform, Vector3(header[transform]))
        self._draw_groups = int_group_to_bit_set(header["__draw_groups"], assert_size=8)
        self._display_groups = int_group_to_bit_set(header["__display_groups"], assert_size=8)
        self._backread_groups = int_group_to_bit_set(header["__backread_groups"], assert_size=8)
        self.description = read_chars_from_buffer(
            msb_buffer, offset=part_offset + header["__description_offset"], encoding="utf-16-le",
        )
        self.name = read_chars_from_buffer(
            msb_buffer, offset=part_offset + header["__name_offset"], encoding="utf-16-le",
        )
        self.sib_path = read_chars_from_buffer(
            msb_buffer, offset=part_offset + header["__sib_path_offset"], encoding="utf-16-le",
        )

        msb_buffer.seek(part_offset + header["__base_data_offset"])
        base_data = self.PART_BASE_DATA_STRUCT.unpack(msb_buffer)
        self.set(**base_data)

        msb_buffer.seek(part_offset + header["__type_data_offset"])
        self.unpack_type_data(msb_buffer)

        if header["__gparam_data_offset"]:
            if not self.PART_GPARAM_STRUCT:
                raise ValueError(f"Found a GParam offset in non-GParam-supporting part {self.name}.")
            msb_buffer.seek(part_offset + header["__gparam_data_offset"])
            gparam_data = self.PART_GPARAM_STRUCT.unpack(msb_buffer)
            self.set(**gparam_data)
        elif self.PART_GPARAM_STRUCT:
            raise ValueError(f"No GParam offset found in GParam-supporting part {self.name}.")

        if header["__scene_gparam_data_offset"]:
            if not self.PART_SCENE_GPARAM_STRUCT:
                raise ValueError(f"Found a SceneGParam offset in non-SceneGParam-supporting part {self.name}.")
            msb_buffer.seek(part_offset + header["__scene_gparam_data_offset"])
            scene_gparam_data = self.PART_SCENE_GPARAM_STRUCT.unpack(msb_buffer)
            self.set(**scene_gparam_data)
        elif self.PART_SCENE_GPARAM_STRUCT:
            raise ValueError(f"No SceneGParam offset found in Scene-GParam-supporting part {self.name}.")

    def pack(self) -> bytes:
        """Pack to bytes, presumably as part of a full `MSB` pack."""

        # Validate draw/display/backread groups before doing any real work.
        draw_groups = bit_set_to_int_group(self._draw_groups, group_size=8)
        display_groups = bit_set_to_int_group(self._display_groups, group_size=8)
        backread_groups = bit_set_to_int_group(self._backread_groups, group_size=8)

        description_offset = self.PART_HEADER_STRUCT.size
        packed_description = self.description.encode("utf-16-le") + b"\0\0"
        name_offset = description_offset + len(packed_description)
        packed_name = self.get_name_to_pack().encode("utf-16-le") + b"\0\0"
        sib_path_offset = name_offset + len(packed_name)
        packed_sib_path = self.sib_path.encode("utf-16-le") + b"\0\0" if self.sib_path else b"\0\0"
        strings_size = len(packed_description + packed_name + packed_sib_path)
        if strings_size <= 0x38:
            packed_sib_path += b"\0" * (0x3c - strings_size)
        else:
            packed_sib_path += b"\0" * 8
        while len(packed_description + packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"  # Not done in SoulsFormats, but makes sense to me.

        base_data_offset = sib_path_offset + len(packed_sib_path)
        packed_base_data = self.PART_BASE_DATA_STRUCT.pack_from_object(self)
        type_data_offset = base_data_offset + len(packed_base_data)
        packed_type_data = self.pack_type_data()
        gparam_data_offset = type_data_offset + len(packed_type_data)
        packed_gparam_data = self.PART_GPARAM_STRUCT.pack_from_object(self)
        scene_gparam_data_offset = gparam_data_offset + len(packed_gparam_data)
        packed_scene_gparam_data = self.PART_SCENE_GPARAM_STRUCT.pack_from_object(self)
        try:
            packed_header = self.PART_HEADER_STRUCT.pack(
                __description_offset=description_offset,
                __name_offset=name_offset,
                _instance_index=self._instance_index,
                __part_type=self.ENTRY_SUBTYPE,
                _part_type_index=self._part_type_index,
                _model_index=self._model_index,
                __sib_path_offset=sib_path_offset,
                translate=list(self.translate),
                rotate=list(self.rotate),
                scale=list(self.scale),
                __draw_groups=draw_groups,
                __display_groups=display_groups,
                __backread_groups=backread_groups,
                __base_data_offset=base_data_offset,
                __type_data_offset=type_data_offset,
                __gparam_data_offset=gparam_data_offset,
                __scene_gparam_data_offset=scene_gparam_data_offset,
            )
        except struct.error:
            raise MapError(f"Could not pack header data of MSB part '{self.name}'. See traceback.")
        return (
            packed_header + packed_description + packed_name + packed_sib_path
            + packed_base_data + packed_type_data + packed_gparam_data + packed_scene_gparam_data
        )


class MSBPartGParam(MSBPart):
    """Subclass of `MSBPart` that includes GParam fields."""
    PART_GPARAM_STRUCT = BinaryStruct(
        ("light_set_id", "i"),
        ("fog_id", "i"),
        ("light_scattering_id", "i"),
        ("environment_map_id", "i"),
        "16x",
    )

    FIELD_INFO = MSBPart.FIELD_INFO | {
        "light_set_id": (
            "Light Set ID",
            int,  # TODO: GParam support.
            "Light set GParam ID.",
        ),
        "fog_id": (
            "Fog Param ID",
            int,  # TODO: GParam support.
            "Fog GParam ID.",
        ),
        "light_scattering_id": (
            "Light Scattering ID",
            int,  # TODO: GParam support.
            "Light scattering GParam ID.",
        ),
        "environment_map_id": (
            "Environment Map ID",
            int,  # TODO: GParam support.
            "Environment map GParam ID.",
        ),
    }

    FIELD_NAMES = MSBPart.FIELD_NAMES + (
        "light_set_id",
        "fog_id",
        "light_scattering_id",
        "environment_map_id",
    )

    def __init__(self, msb_part_source=None):
        self.light_set_id = 0
        self.fog_id = 0
        self.light_scattering_id = 0
        self.environment_map_id = 0
        super().__init__(msb_part_source)


class MSBPartSceneGParam(MSBPartGParam):
    """Subclass of `MSBPart` that includes SceneGParam (and GParam) fields."""
    PART_SCENE_GPARAM_STRUCT = BinaryStruct(
        ("sg_unk_x00_x04", "i"),
        ("sg_unk_x04_x08", "i"),
        ("sg_unk_x08_x0c", "i"),
        ("sg_unk_x0c_x10", "i"),
        ("sg_unk_x10_x14", "i"),
        ("sg_unk_x14_x18", "i"),
        "36x",
        ("event_ids", "4b"),
        ("sg_unk_x40_x44", "f"),
        "12x",
    )

    FIELD_INFO = MSBPartGParam.FIELD_INFO | {
        "sg_unk_x00_x04": (
            "Unknown SceneGParam [00-04]",
            int,
            "Unknown integer.",
        ),
        "sg_unk_x04_x08": (
            "Unknown SceneGParam [04-08]",
            int,
            "Unknown integer.",
        ),
        "sg_unk_x08_x0c": (
            "Unknown SceneGParam [08-0c]",
            int,
            "Unknown integer.",
        ),
        "sg_unk_x0c_x10": (
            "Unknown SceneGParam [0c-10]",
            int,
            "Unknown integer.",
        ),
        "sg_unk_x10_x14": (
            "Unknown SceneGParam [10-14]",
            int,
            "Unknown integer.",
        ),
        "sg_unk_x14_x18": (
            "Unknown SceneGParam [14-18]",
            int,
            "Unknown integer.",
        ),
        "event_ids": (
            "Event IDs",
            list,
            "List of four byte-sized event IDs.",
        ),
        "sg_unk_x40_x44": (
            "Unknown SceneGParam [40-44]",
            float,
            "Unknown floating-point number.",
        ),
    }

    FIELD_NAMES = MSBPartGParam.FIELD_NAMES + (
        "sg_unk_x00_x04",
        "sg_unk_x04_x08",
        "sg_unk_x08_x0c",
        "sg_unk_x0c_x10",
        "sg_unk_x10_x14",
        "sg_unk_x14_x18",
        "event_ids",
        "sg_unk_x40_x44",
    )

    def __init__(self, msb_part_source=None):
        self.sg_unk_x00_x04 = 0
        self.sg_unk_x04_x08 = 0
        self.sg_unk_x08_x0c = 0
        self.sg_unk_x0c_x10 = 0
        self.sg_unk_x10_x14 = 0
        self.sg_unk_x14_x18 = 0
        self.event_ids = [0, 0, 0, 0]
        self.sg_unk_x40_x44 = 0.0
        super().__init__(msb_part_source)


class MSBMapPiece(_BaseMSBMapPiece, MSBPartGParam):
    """No further modifications."""

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            MapPieceModel,
            "Name of map piece model to use for this map piece.",
        ),
        **MSBPart.FIELD_INFO,
    }


class MSBObject(_BaseMSBObject, MSBPartGParam):
    """Interactable object. Note that Bloodborne has six-digit model IDs for Objects."""

    PART_TYPE_DATA_STRUCT = (
        "4x",
        ("_draw_parent_index", "i"),
        ("break_term", "b"),
        ("net_sync_type", "b"),
        ("collision_hit_filter", "?"),
        ("set_main_object_structure_bools", "?"),
        ("animation_ids", "4h"),
        ("model_fx_param_id_offsets", "4h"),
    )

    # TODO: FIELD_INFO and FIELD_NAMES

    def __init__(self, msb_part_source=None, **kwargs):
        self.break_term = 0
        self.net_sync_type = 0
        self.collision_hit_filter = False
        self.set_main_object_structure_bools = False
        # TODO: If only the first is used, just use a `default_animation` property and set the rest to -1.
        self.animation_ids = [-1, -1, -1, -1]  # Pav says only the first one is actually used
        # TODO: If only the first is used, just use a `model_fx_param_id_offset` property and set the rest to -1.
        self.model_fx_param_id_offsets = [0, 0, 0, 0]  # Pav says only the first one is actually used
        super().__init__(msb_part_source)
        self.set(**kwargs)


class MSBCharacter(_BaseMSBCharacter, MSBPartGParam):
    PART_TYPE_DATA_STRUCT = (
        "8x",
        ("think_id", "i"),
        ("npc_id", "i"),
        ("talk_id", "i"),
        ("chara_init_id", "i"),
        ("chr_unk_x18_x1c", "i"),
        ("_draw_parent_index", "i"),
        ("chr_unk_x20_x22", "h"),
        "6x",
        ("_patrol_region_indices", "8h"),
        ("default_animation", "i"),
        ("damage_animation", "i"),
    )

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            CharacterModel,
            "Name of character model to use for this character.",
        ),
        **MSBPart.FIELD_INFO,
        "think_id": (
            "AI ID",
            AIParam,
            "Character's AI. If set to -1, the default AI ID set in the NPC ID (below) will be used.",
        ),
        "npc_id": (
            "Character ID",
            CharacterParam,
            "Basic character information. For 'player' (human) characters, most of the fields in this param entry are "
            "unused.",
        ),
        "talk_id": (
            "Talk ID",
            TalkScript,
            "EzState ID of character, which determines their interactions (conversations, shops, etc.). This is used "
            "to look up the corresponding 'tXXXXXX.esd' file inside the 'talkesdbnd' archive for this map.",
        ),
        "chara_init_id": (
            "Player ID",
            PlayerParam,
            "Contains information for 'player' (human) characters, such as their stats and equipment.",
        ),
        "chr_unk_x18_x1c": (
            "Chr Unknown [18-1c]",
            int,
            "Unknown integer.",
        ),
        "draw_parent_name": (
            "Draw Parent",
            MapPart,
            "Character will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
        ),
        "chr_unk_x20_x22": (
            "Chr Unknown [20-22]",
            int,
            "Unknown 16-bit integer.",
        ),
        "patrol_region_names": (
            "Patrol Regions",
            GameObjectSequence((Region, 8)),
            "List of regions that this character will patrol between, in a looping sequence, if they have the standard "
            "AI logic.",
        ),
        "default_animation": (
            "Default Animation",
            int,  # TODO: Animation
            "Default looping animation for character.",
        ),
        "damage_animation": (
            "Damage Animation",
            int,
            "Default damage animation to use for character.",
        ),
    }

    # TODO: FIELD_NAMES?

    def __init__(self, msb_part_source=None, **kwargs):
        self.chr_unk_x18_x1c = 0
        self.chr_unk_x20_x22 = 0
        super().__init__(msb_part_source)
        self.set(**kwargs)


class MSBPlayerStart(_BaseMSBPlayerStart, MSBPart):
    """TODO: FIELD stuff."""


class MSBCollision(_BaseMSBCollision, MSBPartSceneGParam):
    PART_TYPE_DATA_STRUCT = (
        ("hit_filter_id", "B"),
        ("sound_space_type", "B"),
        ("_environment_event_index", "h"),
        ("reflect_plane_height", "f"),
        ("__area_name_id", "h"),
        ("starts_disabled", "?"),
        ("unk_x0b_x0c", "B"),
        ("attached_bonfire", "i"),
        ("__play_region_id", "i"),
        ("lock_cam_param_id_1", "h"),
        ("lock_cam_param_id_2", "h"),
    )

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            CollisionModel,
            "Name of collision model to use for this collision.",
        ),
        **MSBPart.FIELD_INFO,
        "display_groups": (
            "Display Groups",
            list,
            "Display groups of collision. These display groups will be active when the player is standing on this "
            "Collision, which will draw any parts with an overlapping draw group.",
        ),
        "hit_filter_id": (
            "Hit Filter ID",
            CollisionHitFilter,
            "Determines what happens when the player activates this collision.",
        ),
        "sound_space_type": (
            "Sound Space Type",
            int,
            "Unknown.",
        ),
        "environment_event_name": (
            "Environment Event",
            EnvironmentEvent,
            "Environment event in map that determines ambience when standing on this collision.",
        ),
        "reflect_plane_height": (
            "Reflect Plane Height",
            float,
            "Vertical height of the reflect plane for this collision.",
        ),
        # TODO: Confirm Bloodborne uses the same signed system for Area Name.
        "area_name_id": (
            "Area Name",
            PlaceName,
            "Name of area that this collision is in, which determines the area banner that is shown when you step on "
            "this collision (a linked texture ID lookup) and the area name that appears in the load screen (text ID). "
            "Set it to -1 to use the default area name for this map (i.e. text ID XXYY for map 'mXX_YY').",
        ),
        "force_area_banner": (
            "Show Area Banner",
            bool,
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
        "starts_disabled": (
            "Starts Disabled",
            bool,
            "If True, this collision is disabled on map load and must be manually enabled with an event script.",
        ),
        "unk_x0b_x0c": (
            "Unknown [0b-0c]",
            int,
            "Unknown. Almost always zero (in DS1 at least).",
        ),
        "attached_bonfire": (
            "Attached Bonfire",
            int,
            "If this is set to a bonfire entity ID, that bonfire will be disabled if any living enemy characters are "
            "on this collision. Note that this also checks for enemies that are disabled by events.",
        ),
        # TODO: Confirm Bloodborne uses the same signed system for Stable Footing Flag.
        "play_region_id": (
            "Play Region ID",
            int,
            "Determines the multiplayer (e.g. invasion) sub-area this collision is part of.\n\n"
            ""
            "NOTE: This field shares space with the stable footing flag, so only one of them can be set to a non-zero "
            "value per collision.",
        ),
        "stable_footing_flag": (
            "Stable Footing Flag",
            int,
            "This flag must be enabled for the player's stable footing (i.e. last saved position) to be updated while "
            "standing on this collision. This is used to prevent players loading inside boss arenas before the boss is "
            "defeated. If set to -1, the player's position will never be saved on this collision.\n\n"
            ""
            "NOTE: This field shares space with the play region ID, so only one of them can be set to a non-zero value "
            "per collision.",
        ),
        "lock_cam_param_id_1": (
            "Camera Param ID 1",
            CameraParam,
            "First camera ID to use on this collision. Unsure how the two slots differ.",
        ),
        "lock_cam_param_id_2": (
            "Camera Param ID 2",
            CameraParam,
            "Second camera ID to use on this collision. Unsure how the two slots differ.",
        ),
    }

    # TODO: FIELD_NAMES and HIDDEN_FIELDS.


class MSBNavmesh(_BaseMSBNavmesh, MSBPart):
    PART_TYPE_DATA_STRUCT = (
        "8x",
    )

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            NavmeshModel,
            "Name of navmesh model to use for this navmesh.",
        ),
        **MSBPart.FIELD_INFO,
    }


class MSBUnusedObject(MSBObject):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to `MSBObject`."""
    ENTRY_SUBTYPE = MSBPartSubtype.UnusedObject


class MSBUnusedCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`."""
    ENTRY_SUBTYPE = MSBPartSubtype.UnusedCharacter


class MSBMapConnection(_BaseMSBMapConnection, MSBPart):

    FIELD_INFO = {
        "model_name": (
            "Collision Model Name",
            CollisionModel,
            "Name of collision model to use for this map load trigger.",
        ),
        **MSBPart.FIELD_INFO,
        "collision_name": (
            "Collision Part Name",
            Collision,
            "Collision part that triggers this map load.",
        ),
        "connected_map": (
            "Map ID",
            Map,
            "Vanilla name or 'mAA_BB_CC_DD'-style name or (AA, BB, CC, DD) sequence of the map to be loaded.",
        ),
    }

    GET_MAP = staticmethod(get_map)
    DEFAULT_MAP = (21, 0, 0, 0)  # Hunter's Dream

    def __init__(self, msb_part_source=None, **kwargs):
        self.collision_name = None
        self._collision_index = None
        self._connected_map = self.GET_MAP(self.DEFAULT_MAP)  # type: Map
        super().__init__(msb_part_source)
        self.set(**kwargs)
        if self._connected_map.area_id == 30:
            print(self.name)


class MSBOtherPart(MSBPart):
    """Unknown part (enum -1). No data."""
    ENTRY_SUBTYPE = MSBPartSubtype.Other


class MSBPartList(_BaseMSBPartList, MSBEntryList):
    PART_SUBTYPE_CLASSES = {
        MSBPartSubtype.MapPiece: MSBMapPiece,
        MSBPartSubtype.Object: MSBObject,
        MSBPartSubtype.Character: MSBCharacter,
        MSBPartSubtype.PlayerStart: MSBPlayerStart,
        MSBPartSubtype.Collision: MSBCollision,
        MSBPartSubtype.Navmesh: MSBNavmesh,
        MSBPartSubtype.UnusedObject: MSBUnusedObject,
        MSBPartSubtype.UnusedCharacter: MSBUnusedCharacter,
        MSBPartSubtype.MapConnection: MSBMapConnection,
        MSBPartSubtype.Other: MSBOtherPart,
    }
    PART_SUBTYPE_OFFSET = 20
    GET_MAP = staticmethod(get_map)


for _entry_subtype in MSBPartSubtype:
    setattr(
        MSBPartList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
