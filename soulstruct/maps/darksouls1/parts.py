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

from soulstruct.core import InvalidFieldValueError
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
        ("__name_offset", "i"),
        ("__part_type", "i"),
        ("_part_type_index", "i"),
        ("_model_index", "I"),
        ("__sib_path_offset", "i"),
        ("translate", "3f"),
        ("rotate", "3f"),
        ("scale", "3f"),
        ("__draw_groups", "4I"),
        ("__display_groups", "4I"),
        ("__base_data_offset", "i"),
        ("__type_data_offset", "i"),
        "4x",
    )

    PART_BASE_DATA_STRUCT = BinaryStruct(
        ("entity_id", "i"),
        ("ambient_light_id", "b"),
        ("fog_id", "b"),
        ("scattered_light_id", "b"),
        ("lens_flare_id", "b"),
        ("shadow_id", "b"),
        ("dof_id", "b"),
        ("tone_map_id", "b"),
        ("tone_correct_id", "b"),
        ("point_light_id", "b"),
        ("lod_id", "b"),
        "x",
        ("is_shadow_source", "?"),
        ("is_shadow_destination", "?"),
        ("is_shadow_only", "?"),
        ("draw_by_reflect_cam", "?"),
        ("draw_only_reflect_cam", "?"),
        ("use_depth_bias_float", "?"),
        ("disable_point_light_effect", "?"),
        "2x",
    )

    NAME_ENCODING = "shift_jis_2004"

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
        "ambient_light_id": (
            "Ambient Light ID",
            AmbientLightParam,
            "ID of Ambient Light parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "fog_id": (
            "Fog ID",
            FogParam,
            "ID of Fog parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "scattered_light_id": (
            "Scattered Light ID",
            ScatteredLightParam,
            "ID of Scattered Light parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "lens_flare_id": (
            "Lens Flare ID",
            LensFlareParam,
            "ID of Lens Flare parameter (both types) to use from this map's lighting parameters (DrawParam).",
        ),
        "shadow_id": (
            "Shadow ID",
            ShadowParam,
            "ID of Shadow parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "dof_id": (
            "Depth of Field ID",
            DepthOfFieldParam,
            "ID of Depth Of Field ID parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "tone_map_id": (
            "Tone Map ID",
            ToneMappingParam,
            "ID of Tone Map parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "point_light_id": (
            "Point Light ID",
            PointLightParam,
            "ID of Point Light parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "tone_correct_id": (
            "Tone Correction ID",
            ToneCorrectionParam,
            "ID of Tone Correction parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "lod_id": (
            "Level of Detail ID",
            int,
            "Level of Detail (LoD) parameter. Always -1 or 0, probably unused.",
        ),
        "is_shadow_source": (
            "Casts Shadow",
            bool,
            "If True, this entity will cast dynamic shadows.",
        ),
        "is_shadow_destination": (
            "Receives Shadow",
            bool,
            "If True, this entity can have dynamic shadows cast onto it.",
        ),
        "is_shadow_only": (
            "Only Casts Shadow",
            bool,
            "If True, this entity only casts shadows.",
        ),
        "draw_by_reflect_cam": (
            "Is Reflected",
            bool,
            "If True, this entity will be reflected in water, etc.",
        ),
        "draw_only_reflect_cam": (
            "Is Only Reflected",
            bool,
            "If True, this entity will only be drawn in reflections in water, etc.",
        ),
        "use_depth_bias_float": (
            "Use Depth Bias Float",
            bool,
            "Unknown.",
        ),
        "disable_point_light_effect": (
            "Ignore Point Lights",
            bool,
            "If True, this entity will not be illuminated by point lights (I think).",
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
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    # Default hidden fields for MSB Parts. Subtypes may override this.
    HIDDEN_FIELDS = (
        "lod_id",
        "use_depth_bias_float",
    )

    def __init__(self, msb_part_source=None):
        self._draw_groups = set(range(128))  # {0, 1, 2, ..., 127}
        self._display_groups = set(range(128))  # {0, 1, 2, ..., 127}

        # Lighting parameters
        self.ambient_light_id = 0
        self.fog_id = 0
        self.scattered_light_id = 0
        self.lens_flare_id = 0
        self.shadow_id = 0
        self.dof_id = 0
        self.tone_map_id = 0
        self.tone_correct_id = 0
        self.point_light_id = 0
        self.lod_id = -1  # only ever 0 or -1, seemingly at random

        # Additional boolean parameters (exact effects may be unknown)
        self.is_shadow_source = False
        self.is_shadow_destination = False
        self.is_shadow_only = False
        self.draw_by_reflect_cam = False
        self.draw_only_reflect_cam = False
        self.use_depth_bias_float = False
        self.disable_point_light_effect = False

        super().__init__(msb_part_source)

    def unpack(self, msb_buffer):
        part_offset = msb_buffer.tell()

        header = self.PART_HEADER_STRUCT.unpack(msb_buffer)
        if header["__part_type"] != self.ENTRY_SUBTYPE:
            raise ValueError(f"Unexpected part type enum {header['part_type']} for class {self.__class__.__name__}.")
        self._model_index = header["_model_index"]
        self._part_type_index = header["_part_type_index"]
        for transform in ("translate", "rotate", "scale"):
            setattr(self, transform, Vector3(getattr(header, transform)))
        self._draw_groups = int_group_to_bit_set(header["__draw_groups"], assert_size=4)
        self._display_groups = int_group_to_bit_set(header["__display_groups"], assert_size=4)
        self.name = read_chars_from_buffer(
            msb_buffer, offset=part_offset + header["__name_offset"], encoding=self.NAME_ENCODING
        )
        self.sib_path = read_chars_from_buffer(
            msb_buffer, offset=part_offset + header["__sib_path_offset"], encoding=self.NAME_ENCODING
        )
        msb_buffer.seek(part_offset + header["__base_data_offset"])
        base_data = self.PART_BASE_DATA_STRUCT.unpack(msb_buffer)
        self.set(**base_data)
        msb_buffer.seek(part_offset + header["__type_data_offset"])
        self.unpack_type_data(msb_buffer)

    def pack(self):
        """Pack to bytes, presumably as part of a full `MSB` pack."""

        # Validate draw/display groups before doing any real work.
        draw_groups = bit_set_to_int_group(self._draw_groups, group_size=4)
        display_groups = bit_set_to_int_group(self._display_groups, group_size=4)

        name_offset = self.PART_HEADER_STRUCT.size
        packed_name = self.get_name_to_pack().encode(self.NAME_ENCODING) + b"\0"  # Name not padded on its own.
        sib_path_offset = name_offset + len(packed_name)
        packed_sib_path = self.sib_path.encode(self.NAME_ENCODING) + b"\0" if self.sib_path else b"\0" * 6
        while len(packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"
        base_data_offset = sib_path_offset + len(packed_sib_path)
        packed_base_data = self.PART_BASE_DATA_STRUCT.pack_from_object(self)
        type_data_offset = base_data_offset + len(packed_base_data)
        packed_type_data = self.pack_type_data()
        try:
            packed_header = self.PART_HEADER_STRUCT.pack(
                __name_offset=name_offset,
                __part_type=self.ENTRY_SUBTYPE,
                _part_type_index=self._part_type_index,
                _model_index=self._model_index,
                __sib_path_offset=sib_path_offset,
                translate=list(self.translate),
                rotate=list(self.rotate),
                scale=list(self.scale),
                __draw_groups=draw_groups,
                __display_groups=display_groups,
                __base_data_offset=base_data_offset,
                __type_data_offset=type_data_offset,
            )
        except struct.error:
            raise MapError(f"Could not pack header data of MSB part '{self.name}'. See traceback.")
        return packed_header + packed_name + packed_sib_path + packed_base_data + packed_type_data


class MSBMapPiece(_BaseMSBMapPiece, MSBPart):
    """Struct is common (and empty)."""

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            MapPieceModel,
            "Name of map piece model to use for this map piece.",
        ),
        **MSBPart.FIELD_INFO,
    }

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "display_groups",
        "lod_id",
        "is_shadow_source",
        "is_shadow_only",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )


class MSBObject(_BaseMSBObject, MSBPart):
    PART_TYPE_DATA_STRUCT = (
        "4x",
        ("_draw_parent_index", "i"),
        ("break_term", "b"),
        ("net_sync_type", "b"),
        "2x",
        ("default_animation", "h"),
        ("unk_x0e_x10", "h"),
        ("unk_x10_x14", "i"),
        "4x",
    )

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            ObjectModel,
            "Name of object model to use for this object.",
        ),
        **MSBPart.FIELD_INFO,
        "draw_parent_name": (
            "Draw Parent",
            MapPart,
            "Object will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
        ),
        "break_term": (
            "Break Term",
            int,
            "Unknown. Related to object breakage.",
        ),
        "net_sync_type": (
            "Net Sync Type",
            int,
            "Unknown. Related to online object synchronization.",
        ),
        "default_animation": (
            "Default Animation",
            int,  # TODO: Animation
            "Object animation ID to auto-play on map load, e.g. for different corpse poses.",
        ),
        "unk_x0e_x10": (
            "Unknown [0e-10]",
            int,
            "Unknown.",
        ),
        "unk_x10_x14": (
            "Unknown [10-14]",
            int,
            "Unknown.",
        ),
    }

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_parent_name",
        "draw_groups",
        "display_groups",
        "break_term",
        "net_sync_type",
        "default_animation",
        "unk_x0e_x10",
        "unk_x10_x14",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "display_groups",
        "lod_id",
        "unk_x0e_x10",
        "unk_x10_x14",
        "use_depth_bias_float",
    )

    def __init__(self, msb_part_source=None, **kwargs):
        self.break_term = 0
        self.net_sync_type = 0
        self.default_animation = 0
        self.unk_x0e_x10 = 0
        self.unk_x10_x14 = 0
        super().__init__(msb_part_source)
        if msb_part_source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        self.set(**kwargs)


class MSBCharacter(_BaseMSBCharacter, MSBPart):

    PART_TYPE_DATA_STRUCT = (
        "8x",
        ("think_id", "i"),
        ("npc_id", "i"),
        ("talk_id", "i"),
        ("patrol_type", "B"),
        "x",
        ("platoon_id", "H"),
        ("chara_init_id", "i"),
        ("_draw_parent_index", "i"),
        "8x",
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
        "patrol_type": (
            "Patrol Type",
            int,
            "Patrol behavior type. (Effects unknown.)",
        ),
        "platoon_id": (
            "Platoon ID",
            int,
            "Unused 'platoon' ID value.",
        ),
        "chara_init_id": (
            "Player ID",
            PlayerParam,
            "Contains information for 'player' (human) characters, such as their stats and equipment.",
        ),
        "draw_parent_name": (
            "Draw Parent",
            MapPart,
            "Character will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn.",
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

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_parent_name",
        "draw_groups",
        "display_groups",
        "chara_init_id",
        "npc_id",
        "think_id",
        "talk_id",
        "patrol_type",
        "patrol_region_names",
        "platoon_id",
        "default_animation",
        "damage_animation",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "display_groups",
        "platoon_id",
        "lod_id",
        "use_depth_bias_float",
    )

    def __init__(self, msb_part_source=None, **kwargs):
        self.patrol_type = 0
        self.platoon_id = 0
        super().__init__(msb_part_source)
        if msb_part_source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        self.set(**kwargs)


class MSBPlayerStart(_BaseMSBPlayerStart, MSBPart):

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            CharacterModel,
            "Name of character model to use for this PlayerStart. This should always be c0000.",
        ),
        **MSBPart.FIELD_INFO,
    }

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "draw_groups",
        "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    def __init__(self, msb_part_source=None, **kwargs):
        super().__init__(msb_part_source, **kwargs)
        if msb_part_source is None:
            if "is_shadow_source" not in kwargs:
                self.is_shadow_source = True
            if "is_shadow_destination" not in kwargs:
                self.is_shadow_destination = True
            if "draw_by_reflect_cam" not in kwargs:
                self.draw_by_reflect_cam = True


class MSBCollision(_BaseMSBCollision, MSBPart):
    """Dark Souls collision includes navmesh groups and Vagrants."""

    PART_TYPE_DATA_STRUCT = (
        ("hit_filter_id", "B"),
        ("sound_space_type", "B"),
        ("_environment_event_index", "h"),
        ("reflect_plane_height", "f"),
        ("__navmesh_groups", "4I"),
        ("vagrant_entity_ids", "3i"),
        ("__area_name_id", "h"),
        ("starts_disabled", "?"),
        ("unk_x27_x28", "B"),
        ("attached_bonfire", "i"),
        ("minus_ones", "3i", [-1, -1, -1]),  # Never used. Possibly more bonfires?
        ("__play_region_id", "i"),
        ("lock_cam_param_id_1", "h"),
        ("lock_cam_param_id_2", "h"),
        "16x",
    )

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            CollisionModel,
            "Name of collision model to use for this collision.",
        ),
        **MSBPart.FIELD_INFO,
        "display_groups": (  # TODO: it's fine that "display_groups" is already a key in MSBPart.FIELD_INFO?
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
        "navmesh_groups": (
            "Navmesh Groups",
            list,
            "Controls collision backread.",
        ),
        "vagrant_entity_ids": (
            "Vagrant Entity IDs",
            list,
            "Unknown.",
        ),
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
        "unk_x27_x28": (
            "Unknown [27-28]",
            int,
            "Unknown. Almost always zero, but see e.g. Anor Londo gondola collision.",
        ),
        "attached_bonfire": (
            "Attached Bonfire",
            int,
            "If this is set to a bonfire entity ID, that bonfire will be disabled if any living enemy characters are "
            "on this collision. Note that this also checks for enemies that are disabled by events.",
        ),
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

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "navmesh_groups",
        "hit_filter_id",
        "sound_space_type",
        "environment_event_name",
        "reflect_plane_height",
        "vagrant_entity_ids",
        "area_name_id",
        "force_area_banner",
        "starts_disabled",
        "unk_x27_x28",
        "attached_bonfire",
        "play_region_id",
        "stable_footing_flag",
        "lock_cam_param_id_1",
        "lock_cam_param_id_2",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "lod_id",
        "unk_x27_x28",
        "use_depth_bias_float",
    )

    def __init__(self, msb_part_source=None, **kwargs):
        self._navmesh_groups = set(range(128))
        self.vagrant_entity_ids = [-1, -1, -1]
        self.unk_x27_x28 = 0
        super().__init__(msb_part_source)
        if msb_part_source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_TYPE_DATA_STRUCT).unpack(msb_buffer, include_asserted=False)
        self.set(**data)
        self._navmesh_groups = int_group_to_bit_set(data["__navmesh_groups"], assert_size=4)
        self.area_name_id = abs(data["__area_name_id"]) if data["__area_name_id"] != -1 else -1
        self._force_area_banner = data["__area_name_id"] < 0  # Custom field.
        if data["__play_region_id"] > -10:
            self._play_region_id = data["__play_region_id"]
            self._stable_footing_flag = 0
        else:
            self._play_region_id = 0
            self._stable_footing_flag = -data["__play_region_id"] - 10

    def pack_type_data(self):
        """Pack to bytes, presumably as part of a full `MSB` pack."""

        # Validate navmesh groups before doing any real work.
        navmesh_groups = bit_set_to_int_group(self._navmesh_groups, group_size=4)

        if self.area_name_id == -1 and not self._force_area_banner:
            raise InvalidFieldValueError("`force_area_banner` must be enabled if `area_name_id == -1` (default).")
        signed_area_name_id = self.area_name_id * (-1 if self.area_name_id >= 0 and self._force_area_banner else 1)
        if self._stable_footing_flag != 0:
            play_region_id = -self._stable_footing_flag - 10
        else:
            play_region_id = self._play_region_id
        return BinaryStruct(*self.PART_TYPE_DATA_STRUCT).pack(
            hit_filter_id=self.hit_filter_id,
            sound_space_type=self.sound_space_type,
            _environment_event_index=self._environment_event_index,
            reflect_plane_height=self.reflect_plane_height,
            __navmesh_groups=navmesh_groups,
            vagrant_entity_ids=self.vagrant_entity_ids,
            __area_name_id=signed_area_name_id,
            starts_disabled=self.starts_disabled,
            unk_x27_x28=self.unk_x27_x28,
            attached_bonfire=self.attached_bonfire,
            __play_region_id=play_region_id,
            lock_cam_param_id_1=self.lock_cam_param_id_1,
            lock_cam_param_id_2=self.lock_cam_param_id_2,
        )

    @property
    def navmesh_groups(self):
        return self._navmesh_groups

    @navmesh_groups.setter
    def navmesh_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._navmesh_groups = set()
            return
        try:
            navmesh_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Navmesh groups must be a set, sequence, `None`, 'None', or ''. "
                "Or use `.navmesh_groups.add()`, etc.)."
            )
        for i in navmesh_groups:
            if not 0 <= i <= 127:
                raise ValueError(f"Invalid navmesh group: {i}. Must range from 0 to 127, inclusive.")
        self._navmesh_groups = navmesh_groups


class MSBNavmesh(_BaseMSBNavmesh, MSBPart):
    PART_TYPE_DATA_STRUCT = (
        ("__navmesh_groups", "4I"),
        "16x",
    )

    FIELD_INFO = {
        "model_name": (
            "Model Name",
            NavmeshModel,
            "Name of navmesh model to use for this navmesh.",
        ),
        **MSBPart.FIELD_INFO,
        "navmesh_groups": (
            "Navmesh Groups",
            list,
            "Enables backread of collisions with overlapping navmesh groups, if the nodes are also close enough in "
            "the MCG/MCP network.",
        ),
    }

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "navmesh_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "lod_id",
        "use_depth_bias_float",
        "draw_groups",
        "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    def __init__(self, msb_part_source=None, **kwargs):
        self._navmesh_groups = set(range(128))
        super().__init__(msb_part_source)
        if msb_part_source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
        self.set(**kwargs)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_TYPE_DATA_STRUCT).unpack(msb_buffer, include_asserted=False)
        self._navmesh_groups = int_group_to_bit_set(data["__navmesh_groups"], assert_size=4)

    def pack_type_data(self):
        return BinaryStruct(*self.PART_TYPE_DATA_STRUCT).pack(
            __navmesh_groups=bit_set_to_int_group(self._navmesh_groups, group_size=4),
        )

    @property
    def navmesh_groups(self):
        return self._navmesh_groups

    @navmesh_groups.setter
    def navmesh_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._navmesh_groups = set()
            return
        try:
            navmesh_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Navmesh groups must be a set, sequence, `None`, 'None', or ''. "
                "Or use `.navmesh_groups.add()`, etc.)."
            )
        for i in navmesh_groups:
            if not 0 <= i <= 127:
                raise ValueError(f"Invalid navmesh group: {i}. Must range from 0 to 127, inclusive.")
        self._navmesh_groups = navmesh_groups


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

    FIELD_NAMES = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "scale",
        "draw_groups",
        "display_groups",
        "collision_name",
        "connected_map",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correct_id",
        "lod_id",
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    HIDDEN_FIELDS = (
        "scale",
        "lod_id",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        "use_depth_bias_float",
        "disable_point_light_effect",
    )

    GET_MAP = staticmethod(get_map)
    DEFAULT_MAP = (10, 0, 0, 0)  # Depths

    def __init__(self, msb_part_source=None, **kwargs):
        self.collision_name = None
        self._collision_index = None
        self._connected_map = self.GET_MAP(self.DEFAULT_MAP)
        super().__init__(msb_part_source)
        if msb_part_source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        self.set(**kwargs)


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
    }
    PART_SUBTYPE_OFFSET = 4
    GET_MAP = staticmethod(get_map)


for _entry_subtype in MSBPartSubtype:
    setattr(
        MSBPartList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
