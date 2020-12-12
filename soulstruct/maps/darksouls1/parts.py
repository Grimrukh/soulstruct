import struct

from soulstruct.game_types import *
from soulstruct.maps import MapError
from soulstruct.maps.base.parts import (
    MSBPart as BaseMSBPart,
    MSBPartList as BaseMSBPartList,
    MSBPartSubtype,
    MSBMapPiece as BaseMSBMapPiece,
    MSBObject as BaseMSBObject,
    MSBCharacter as BaseMSBCharacter,
    MSBPlayerStart,
    MSBCollision,
    MSBNavmesh,
    MSBUnusedObject,
    MSBUnusedCharacter,
    MSBMapConnection,
)
from soulstruct.utilities import BinaryStruct, read_chars_from_buffer
from soulstruct.utilities.conversion import int_group_to_bit_set, bit_set_to_int_group
from soulstruct.utilities.maths import Vector3


class MSBPart(BaseMSBPart):
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
        self._draw_groups = int_group_to_bit_set(header["__draw_groups"])
        self._display_groups = int_group_to_bit_set(header["__display_groups"])
        self.name = read_chars_from_buffer(
            msb_buffer, offset=part_offset + header["__name_offset"], encoding="shift-jis"
        )
        self.sib_path = read_chars_from_buffer(
            msb_buffer, offset=part_offset + header["__sib_path_offset"], encoding="shift-jis"
        )
        msb_buffer.seek(part_offset + header["__base_data_offset"])
        base_data = self.PART_BASE_DATA_STRUCT.unpack(msb_buffer)
        self.set(**base_data)
        msb_buffer.seek(part_offset + header["__type_data_offset"])
        self.unpack_type_data(msb_buffer)

    def pack(self):
        """Pack to bytes, presumably as part of a full `MSB` pack."""

        # Validate draw/display groups before doing any real work.
        draw_groups = bit_set_to_int_group(self._draw_groups)
        display_groups = bit_set_to_int_group(self._display_groups)

        name_offset = self.PART_HEADER_STRUCT.size
        packed_name = self.get_name_to_pack().encode("shift-jis") + b"\0"  # Name not padded on its own.
        sib_path_offset = name_offset + len(packed_name)
        packed_sib_path = self.sib_path.encode("shift-jis") + b"\0" if self.sib_path else b"\0" * 6
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


class MSBMapPiece(BaseMSBMapPiece, MSBPart):
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


class MSBObject(BaseMSBObject, MSBPart):
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


class MSBCharacter(BaseMSBCharacter, MSBPart):

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
        ("_patrol_point_indices", "8h"),
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
        "patrol_point_names": (
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
        "patrol_point_names",
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


class MSBPartList(BaseMSBPartList):
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
