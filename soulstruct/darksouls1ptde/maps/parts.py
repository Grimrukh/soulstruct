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

import abc
import struct
import typing as tp

from soulstruct.exceptions import InvalidFieldValueError
from soulstruct.game_types import *
from soulstruct.base.maps.msb.utils import MapFieldInfo
from soulstruct.base.maps.msb.exceptions import MapError
from soulstruct.base.maps.msb.parts import (
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
from soulstruct.base.maps.msb.enums import MSBPartSubtype
from soulstruct.utilities.binary import BinaryStruct, BinaryReader
from soulstruct.utilities.conversion import int_group_to_bit_set, bit_set_to_int_group
from soulstruct.utilities.maths import Vector3
from .constants import get_map
from .msb_entry import MSBEntryList


class MSBPart(_BaseMSBPart, abc.ABC):
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
        ("tone_correction_id", "b"),
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
    NAME_ENCODING = "shift-jis"
    FLAG_SET_SIZE = 128

    FIELD_INFO = _BaseMSBPart.FIELD_INFO | {
        "draw_groups": MapFieldInfo(
            "Draw Groups",
            list,
            set(range(FLAG_SET_SIZE)),
            "Draw groups of part. This part will be drawn when the corresponding display group is active.",
        ),
        "display_groups": MapFieldInfo(
            "Display Groups",
            list,
            set(range(FLAG_SET_SIZE)),
            "Display groups are present in all MSB Parts, but only function for collisions.",
        ),
        "ambient_light_id": MapFieldInfo(
            "Ambient Light ID",
            AmbientLightParam,
            0,
            "ID of Ambient Light parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "fog_id": MapFieldInfo(
            "Fog ID",
            FogParam,
            0,
            "ID of Fog parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "scattered_light_id": MapFieldInfo(
            "Scattered Light ID",
            ScatteredLightParam,
            0,
            "ID of Scattered Light parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "lens_flare_id": MapFieldInfo(
            "Lens Flare ID",
            LensFlareParam,
            0,
            "ID of Lens Flare parameter (both types) to use from this map's lighting parameters (DrawParam).",
        ),
        "shadow_id": MapFieldInfo(
            "Shadow ID",
            ShadowParam,
            0,
            "ID of Shadow parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "dof_id": MapFieldInfo(
            "Depth of Field ID",
            DepthOfFieldParam,
            0,
            "ID of Depth Of Field ID parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "tone_map_id": MapFieldInfo(
            "Tone Map ID",
            ToneMappingParam,
            0,
            "ID of Tone Map parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "point_light_id": MapFieldInfo(
            "Point Light ID",
            PointLightParam,
            0,
            "ID of Point Light parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "tone_correction_id": MapFieldInfo(
            "Tone Correction ID",
            ToneCorrectionParam,
            0,
            "ID of Tone Correction parameter to use from this map's lighting parameters (DrawParam).",
        ),
        "lod_id": MapFieldInfo(
            "Level of Detail ID",
            int,
            0,  # only ever 0 or -1, seemingly at random
            "Level of Detail (LoD) parameter. Always -1 or 0, probably unused.",
        ),
        "is_shadow_source": MapFieldInfo(
            "Casts Shadow",
            bool,
            False,
            "If True, this entity will cast dynamic shadows.",
        ),
        "is_shadow_destination": MapFieldInfo(
            "Receives Shadow",
            bool,
            False,
            "If True, this entity can have dynamic shadows cast onto it.",
        ),
        "is_shadow_only": MapFieldInfo(
            "Only Casts Shadow",
            bool,
            False,
            "If True, this entity only casts shadows.",
        ),
        "draw_by_reflect_cam": MapFieldInfo(
            "Is Reflected",
            bool,
            False,
            "If True, this entity will be reflected in water, etc.",
        ),
        "draw_only_reflect_cam": MapFieldInfo(
            "Is Only Reflected",
            bool,
            False,
            "If True, this entity will only be drawn in reflections in water, etc.",
        ),
        "use_depth_bias_float": MapFieldInfo(
            "Use Depth Bias Float",
            bool,
            False,
            "Unknown.",
        ),
        "disable_point_light_effect": MapFieldInfo(
            "Ignore Point Lights",
            bool,
            False,
            "If True, this entity will not be illuminated by point lights (I think).",
        ),
    }

    LIGHTING_FIELD_ORDER = (
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        "tone_map_id",
        "point_light_id",
        "tone_correction_id",
        # "lod_id",
    )

    entity_id: int
    translate: Vector3
    rotate: Vector3
    scale: Vector3
    draw_groups: set[int]
    display_groups: set[int]
    ambient_light_id: int
    fog_id: int
    scattered_light_id: int
    lens_flare_id: int
    shadow_id: int
    dof_id: int
    tone_map_id: int
    point_light_id: int
    tone_correction_id: int
    lod_id: int
    is_shadow_source: bool
    is_shadow_destination: bool
    is_shadow_only: bool
    draw_by_reflect_cam: bool
    draw_only_reflect_cam: bool
    use_depth_bias_float: bool
    disable_point_light_effect: bool

    def unpack(self, msb_reader: BinaryReader):
        part_offset = msb_reader.position
        header = msb_reader.unpack_struct(self.PART_HEADER_STRUCT)
        if header["__part_type"] != self.ENTRY_SUBTYPE:
            raise ValueError(f"Unexpected part type enum {header['part_type']} for class {self.__class__.__name__}.")
        self._model_index = header["_model_index"]
        self._part_type_index = header["_part_type_index"]
        for transform in ("translate", "rotate", "scale"):
            setattr(self, transform, Vector3(header[transform]))
        self._draw_groups = int_group_to_bit_set(header["__draw_groups"], assert_size=4)
        self._display_groups = int_group_to_bit_set(header["__display_groups"], assert_size=4)
        self.name = msb_reader.unpack_string(
            offset=part_offset + header["__name_offset"], encoding=self.NAME_ENCODING
        )
        self.sib_path = msb_reader.unpack_string(
            offset=part_offset + header["__sib_path_offset"], encoding=self.NAME_ENCODING
        )
        msb_reader.seek(part_offset + header["__base_data_offset"])
        base_data = msb_reader.unpack_struct(self.PART_BASE_DATA_STRUCT)
        self.set(**base_data)
        msb_reader.seek(part_offset + header["__type_data_offset"])
        self.unpack_type_data(msb_reader)

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
        packed_base_data = self.PART_BASE_DATA_STRUCT.pack(self)
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
            raise MapError(f"Could not pack header data of `{self.__class__.__name__}` '{self.name}'. See traceback.")
        return packed_header + packed_name + packed_sib_path + packed_base_data + packed_type_data


class MSBMapPiece(_BaseMSBMapPiece, MSBPart):
    """Struct is common (and empty)."""

    FIELD_INFO = MSBPart.FIELD_INFO | _BaseMSBMapPiece.FIELD_INFO  # no additional game-specific fields

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        # "scale",
        "draw_groups",
        # "display_groups",
        "ambient_light_id",
        "fog_id",
        "scattered_light_id",
        "lens_flare_id",
        "shadow_id",
        "dof_id",
        # No tone map, point light, or tone correction (collisions only).
        # "is_shadow_source",
        "is_shadow_destination",
        # "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        # "use_depth_bias_float",
        # "disable_point_light_effect",
    )


class MSBObject(_BaseMSBObject, MSBPart):
    PART_TYPE_DATA_STRUCT = BinaryStruct(
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

    FIELD_INFO = MSBPart.FIELD_INFO | _BaseMSBObject.FIELD_INFO | {
        "break_term": MapFieldInfo(
            "Break Term",
            int,
            0,
            "Unknown. Related to object breakage.",
        ),
        "net_sync_type": MapFieldInfo(
            "Net Sync Type",
            int,
            0,
            "Unknown. Related to online object synchronization.",
        ),
        "default_animation": MapFieldInfo(
            "Default Animation",
            int,  # TODO: Animation
            0,
            "Object animation ID to auto-play on map load, e.g. for different corpse poses.",
        ),
        "unk_x0e_x10": MapFieldInfo(
            "Unknown [0e-10]",
            int,
            0,
            "Unknown.",
        ),
        "unk_x10_x14": MapFieldInfo(
            "Unknown [10-14]",
            int,
            0,
            "Unknown.",
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
        "break_term",
        "net_sync_type",
        "default_animation",
        # "unk_x0e_x10",
        # "unk_x10_x14",
    ) + MSBPart.LIGHTING_FIELD_ORDER + (
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        # "use_depth_bias_float",
        "disable_point_light_effect",
    )

    break_term: int
    net_sync_type: int
    default_animation: int
    unk_x0e_x10: int
    unk_x10_x14: int

    def __init__(self, source=None, **kwargs):
        if source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        super().__init__(source=source, **kwargs)


class MSBCharacter(_BaseMSBCharacter, MSBPart):
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        "8x",
        ("ai_id", "i"),
        ("character_id", "i"),
        ("talk_id", "i"),
        ("patrol_type", "B"),
        "x",
        ("platoon_id", "H"),
        ("player_id", "i"),
        ("_draw_parent_index", "i"),
        "8x",
        ("_patrol_region_indices", "8h"),
        ("default_animation", "i"),
        ("damage_animation", "i"),
    )

    FIELD_INFO = MSBPart.FIELD_INFO | _BaseMSBCharacter.FIELD_INFO | {
        "patrol_type": MapFieldInfo(
            "Patrol Type",
            int,
            0,
            "Patrol behavior type. (Effects unknown.)",
        ),
        "platoon_id": MapFieldInfo(
            "Platoon ID",
            int,
            0,
            "Unused 'platoon' ID value.",
        ),
    }

    FIELD_ORDER = _BaseMSBCharacter.FIELD_ORDER + (
        "patrol_type",
        # "platoon_id",
    ) + MSBPart.LIGHTING_FIELD_ORDER + (
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        # "use_depth_bias_float",
        "disable_point_light_effect",
    )

    patrol_type: int
    platoon_id: int

    def __init__(self, source=None, **kwargs):
        if source is None:
            # Set some different defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        super().__init__(source=source, **kwargs)


class MSBPlayerStart(_BaseMSBPlayerStart, MSBPart):

    FIELD_INFO = MSBPart.FIELD_INFO | _BaseMSBPlayerStart.FIELD_INFO

    def __init__(self, source=None, **kwargs):
        if source is None:
            # Set some different defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        super().__init__(source=source, **kwargs)


class MSBCollision(_BaseMSBCollision, MSBPart):
    """Dark Souls collision includes navmesh groups and Vagrants."""

    PART_TYPE_DATA_STRUCT = BinaryStruct(
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
        ("camera_1_id", "h"),
        ("camera_2_id", "h"),
        "16x",
    )

    FIELD_INFO = MSBPart.FIELD_INFO | _BaseMSBCollision.FIELD_INFO | {
        "navmesh_groups": MapFieldInfo(
            "Navmesh Groups",
            list,
            set(range(MSBPart.FLAG_SET_SIZE)),
            "Controls collision backread.",
        ),
        "vagrant_entity_ids": MapFieldInfo(
            "Vagrant Entity IDs",
            list,
            [-1, -1, -1],
            "Unknown.",
        ),
        "unk_x27_x28": MapFieldInfo(
            "Unknown [27-28]",
            int,
            0,
            "Unknown. Almost always zero, but see e.g. Anor Londo spinning tower collision.",
        ),
    }

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        # "scale",
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
        # "unk_x27_x28",
        "attached_bonfire",
        "play_region_id",
        "stable_footing_flag",
        "camera_1_id",
        "camera_2_id",
    ) + MSBPart.LIGHTING_FIELD_ORDER + (
        "is_shadow_source",
        "is_shadow_destination",
        "is_shadow_only",
        "draw_by_reflect_cam",
        "draw_only_reflect_cam",
        # "use_depth_bias_float",
        "disable_point_light_effect",
    )

    vagrant_entity_ids: list[int, int, int]
    unk_x27_x28: int

    def __init__(self, source=None, **kwargs):
        self._navmesh_groups = set()
        if source is None:
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        super().__init__(source=source, **kwargs)

    def unpack_type_data(self, msb_reader: BinaryReader):
        data = msb_reader.unpack_struct(self.PART_TYPE_DATA_STRUCT, exclude_asserted=True)
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
        return self.PART_TYPE_DATA_STRUCT.pack(
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
            camera_1_id=self.camera_1_id,
            camera_2_id=self.camera_2_id,
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
                "Navmesh groups must be a set, sequence, `None`, 'None', or ''. Or use `set` methods like `.add()`."
            )
        for i in navmesh_groups:
            if not isinstance(i, int) and 0 <= i < self.FLAG_SET_SIZE:
                raise ValueError(f"Invalid navmesh group: {i}. Must be 0 <= i < {self.FLAG_SET_SIZE}.")
        self._navmesh_groups = navmesh_groups


class MSBNavmesh(_BaseMSBNavmesh, MSBPart):
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        ("__navmesh_groups", "4I"),
        "16x",
    )

    FIELD_INFO = MSBPart.FIELD_INFO | _BaseMSBNavmesh.FIELD_INFO | {
        "navmesh_groups": MapFieldInfo(
            "Navmesh Groups",
            list,
            set(range(MSBPart.FLAG_SET_SIZE)),
            "Controls collision backread.",
        ),
    }

    FIELD_ORDER = _BaseMSBNavmesh.FIELD_ORDER + (
        "navmesh_groups",
    )

    def __init__(self, source=None, **kwargs):
        self._navmesh_groups = set()
        if source is None:
            kwargs.setdefault("is_shadow_source", True)
        super().__init__(source=source, **kwargs)

    def unpack_type_data(self, msb_reader: BinaryReader):
        data = msb_reader.unpack_struct(self.PART_TYPE_DATA_STRUCT, exclude_asserted=True)
        self._navmesh_groups = int_group_to_bit_set(data["__navmesh_groups"], assert_size=4)

    def pack_type_data(self):
        return self.PART_TYPE_DATA_STRUCT.pack(
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
                "Navmesh groups must be a set, sequence, `None`, 'None', or ''. Or use `set` methods like `.add()`."
            )
        for i in navmesh_groups:
            if not isinstance(i, int) and 0 <= i < self.FLAG_SET_SIZE:
                raise ValueError(f"Invalid navmesh group: {i}. Must be 0 <= i < {self.FLAG_SET_SIZE}.")
        self._navmesh_groups = navmesh_groups


class MSBUnusedObject(MSBObject):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to `MSBObject`."""

    ENTRY_SUBTYPE = MSBPartSubtype.UnusedObject


class MSBUnusedCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`."""

    ENTRY_SUBTYPE = MSBPartSubtype.UnusedCharacter


class MSBMapConnection(_BaseMSBMapConnection, MSBPart):
    GET_MAP = staticmethod(get_map)

    FIELD_INFO = MSBPart.FIELD_INFO | _BaseMSBMapConnection.FIELD_INFO | {
        "connected_map": MapFieldInfo(
            "Map ID",
            Map,
            (10, 0, 0, 0),  # Depths
            "Vanilla name or 'mAA_BB_CC_DD'-style name or (AA, BB, CC, DD) sequence of the map to be loaded.",
        ),
    }

    FIELD_ORDER = _BaseMSBMapConnection.FIELD_ORDER + MSBPart.LIGHTING_FIELD_ORDER

    def __init__(self, source=None, **kwargs):
        if source is None:
            # Set some defaults.
            kwargs.setdefault("is_shadow_source", True)
            kwargs.setdefault("is_shadow_destination", True)
            kwargs.setdefault("draw_by_reflect_cam", True)
        super().__init__(source=source, **kwargs)


class MSBPartList(_BaseMSBPartList, MSBEntryList):

    SUBTYPE_CLASSES = {
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
    SUBTYPE_OFFSET = 4
    GET_MAP = staticmethod(get_map)

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

    new_map_piece: tp.Callable[..., MSBMapPiece]
    new_object: tp.Callable[..., MSBObject]
    new_character: tp.Callable[..., MSBCharacter]
    new_player_start: tp.Callable[..., MSBPlayerStart]
    new_collision: tp.Callable[..., MSBCollision]
    new_navmesh: tp.Callable[..., MSBNavmesh]
    new_unused_object: tp.Callable[..., MSBUnusedObject]
    new_unused_character: tp.Callable[..., MSBUnusedCharacter]
    new_map_connection: tp.Callable[..., MSBMapConnection]
