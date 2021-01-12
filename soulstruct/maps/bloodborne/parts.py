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
import typing as tp

from soulstruct.game_types import *
from soulstruct.maps.core import MapError, MapFieldInfo
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
from soulstruct.maps.enums import MSBPartSubtype
from soulstruct.utilities import read_chars_from_buffer, partialmethod
from soulstruct.utilities.binary_struct import BinaryStruct
from soulstruct.utilities.conversion import int_group_to_bit_set, bit_set_to_int_group
from soulstruct.utilities.maths import Vector3

from .maps import get_map
from .msb_entry import MSBEntryList
from ...core import InvalidFieldValueError


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
    NAME_ENCODING = "utf-16-le"
    FLAG_SET_SIZE = 256

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
        "backread_groups": MapFieldInfo(
            "Backread Groups",
            list,
            set(range(FLAG_SET_SIZE)),
            "Backread groups are present in all MSB Parts, but only function for collisions (probably).",
        ),
        "base_unk_x04_x05": MapFieldInfo(
            "Unknown Base [04-05]",
            int,
            -1,
            "Unknown base data integer.",
        ),
        "base_unk_x05_x06": MapFieldInfo(
            "Unknown Base [05-06]",
            int,
            -1,
            "Unknown base data integer.",
        ),
        "base_unk_x06_x07": MapFieldInfo(
            "Unknown Base [06-07]",
            int,
            -1,
            "Unknown base data integer.",
        ),
        "base_unk_x07_x08": MapFieldInfo(
            "Unknown Base [07-08]",
            int,
            -1,
            "Unknown base data integer.",
        ),
        "lantern_id": MapFieldInfo(
            "Lantern ID",
            int,
            0,
            "Lantern param ID.",
        ),
        "lod_id": MapFieldInfo(
            "LoD ID",
            int,
            -1,
            "LoD (level of detail) param ID.",
        ),
        "base_unk_x0e_x0f": MapFieldInfo(
            "Unknown Base [0e-0f]",
            int,
            20,
            "Unknown base data integer.",
        ),
        "base_unk_x0f_x10": MapFieldInfo(
            "Unknown Base [0f-10]",
            int,
            0,
            "Unknown base data integer.",
        ),
    }

    FIELD_ORDER = (
        "base_unk_x04_x05",
        "base_unk_x05_x06",
        "base_unk_x06_x07",
        "base_unk_x07_x08",
        "lantern_id",
        "lod_id",
        "base_unk_x0e_x0f",
        "base_unk_x0f_x10",
    )

    base_unk_x04_x05: int
    base_unk_x05_x06: int
    base_unk_x06_x07: int
    base_unk_x07_x08: int
    lantern_id: int
    lod_id: int
    base_unk_x0e_x0f: int
    base_unk_x0f_x10: int

    def __init__(self, source=None, **kwargs):
        self._instance_index = 0
        self._draw_groups = set()
        self._display_groups = set()
        self._backread_groups = set()
        super().__init__(source, **kwargs)

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

        self._unpack_gparam_data(msb_buffer, part_offset, header)
        self._unpack_scene_gparam_data(msb_buffer, part_offset, header)

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
        packed_gparam_data = self._pack_gparam_data()
        scene_gparam_data_offset = gparam_data_offset + len(packed_gparam_data)
        packed_scene_gparam_data = self._pack_scene_gparam_data()
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

    @property
    def backread_groups(self):
        return self._backread_groups

    @backread_groups.setter
    def backread_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._display_groups = set()
            return
        try:
            display_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Backread groups must be a set, sequence, `None`, 'None', or ''. Or use `set` methods like `.add()`."
            )
        for i in display_groups:
            if not isinstance(i, int) and 0 <= i < self.FLAG_SET_SIZE:
                raise ValueError(f"Invalid backread group: {i}. Must be 0 <= i < {self.FLAG_SET_SIZE}.")
        self._display_groups = display_groups

    def _unpack_gparam_data(self, msb_buffer, part_offset, header):
        pass

    def _pack_gparam_data(self):
        return b""

    def _unpack_scene_gparam_data(self, msb_buffer, part_offset, header):
        pass

    def _pack_scene_gparam_data(self):
        return b""


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
        "light_set_id": MapFieldInfo(
            "Light Set ID",
            int,  # TODO: GParam support.
            0,
            "Light set GParam ID.",
        ),
        "fog_id": MapFieldInfo(
            "Fog Param ID",
            int,  # TODO: GParam support.
            0,
            "Fog GParam ID.",
        ),
        "light_scattering_id": MapFieldInfo(
            "Light Scattering ID",
            int,  # TODO: GParam support.
            0,
            "Light scattering GParam ID.",
        ),
        "environment_map_id": MapFieldInfo(
            "Environment Map ID",
            int,  # TODO: GParam support.
            0,
            "Environment map GParam ID.",
        ),
    }

    FIELD_ORDER = MSBPart.FIELD_ORDER + (
        "light_set_id",
        "fog_id",
        "light_scattering_id",
        "environment_map_id",
    )

    light_set_id: int
    fog_id: int
    light_scattering_id: int
    environment_map_id: int

    def _unpack_gparam_data(self, msb_buffer, part_offset, header):
        if header["__gparam_data_offset"] == 0:
            raise ValueError(f"Zero GParam offset found in GParam-supporting part {self.name}.")
        msb_buffer.seek(part_offset + header["__gparam_data_offset"])
        gparam_data = self.PART_GPARAM_STRUCT.unpack(msb_buffer)
        self.set(**gparam_data)

    def _pack_gparam_data(self):
        return self.PART_GPARAM_STRUCT.pack_from_object(self)


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
        "sg_unk_x00_x04": MapFieldInfo(
            "Unk SceneG [00-04]",
            int,
            0,
            "Unknown integer.",
        ),
        "sg_unk_x04_x08": MapFieldInfo(
            "Unk SceneG [04-08]",
            int,
            0,
            "Unknown integer.",
        ),
        "sg_unk_x08_x0c": MapFieldInfo(
            "Unk SceneG [08-0c]",
            int,
            0,
            "Unknown integer.",
        ),
        "sg_unk_x0c_x10": MapFieldInfo(
            "Unk SceneG [0c-10]",
            int,
            0,
            "Unknown integer.",
        ),
        "sg_unk_x10_x14": MapFieldInfo(
            "Unk SceneG [10-14]",
            int,
            0,
            "Unknown integer.",
        ),
        "sg_unk_x14_x18": MapFieldInfo(
            "Unk SceneG [14-18]",
            int,
            0,
            "Unknown integer.",
        ),
        "event_ids": MapFieldInfo(
            "Event IDs",
            list,
            [-1, -1, -1, -1],
            "List of four byte-sized event IDs.",
        ),
        "sg_unk_x40_x44": MapFieldInfo(
            "Unk SceneG [40-44]",
            float,
            0.0,
            "Unknown floating-point number.",
        ),
    }

    FIELD_ORDER = MSBPartGParam.FIELD_ORDER + (
        "sg_unk_x00_x04",
        "sg_unk_x04_x08",
        "sg_unk_x08_x0c",
        "sg_unk_x0c_x10",
        "sg_unk_x10_x14",
        "sg_unk_x14_x18",
        "event_ids",
        "sg_unk_x40_x44",
    )

    sg_unk_x00_x04: int
    sg_unk_x04_x08: int
    sg_unk_x08_x0c: int
    sg_unk_x0c_x10: int
    sg_unk_x10_x14: int
    sg_unk_x14_x18: int
    event_ids: list[int, int, int, int]
    sg_unk_x40_x44: float

    def _unpack_scene_gparam_data(self, msb_buffer, part_offset, header):
        if header["__scene_gparam_data_offset"] == 0:
            raise ValueError(f"Zero SceneGParam offset found in SceneGParam-supporting part {self.name}.")
        msb_buffer.seek(part_offset + header["__scene_gparam_data_offset"])
        scene_gparam_data = self.PART_SCENE_GPARAM_STRUCT.unpack(msb_buffer)
        self.set(**scene_gparam_data)

    def _pack_scene_gparam_data(self):
        return self.PART_SCENE_GPARAM_STRUCT.pack_from_object(self)


class MSBMapPiece(_BaseMSBMapPiece, MSBPartGParam):
    """No further modifications beyond inheritance of GParam."""

    FIELD_INFO = MSBPartGParam.FIELD_INFO | _BaseMSBMapPiece.FIELD_INFO
    FIELD_ORDER = _BaseMSBMapPiece.FIELD_ORDER + MSBPartGParam.FIELD_ORDER


class MSBObject(_BaseMSBObject, MSBPartGParam):
    """Interactable object. Note that Bloodborne has six-digit model IDs for Objects."""

    PART_TYPE_DATA_STRUCT = BinaryStruct(
        "4x",
        ("_draw_parent_index", "i"),
        ("break_term", "b"),
        ("net_sync_type", "b"),
        ("collision_hit_filter", "?"),
        ("set_main_object_structure_bools", "?"),
        ("animation_ids", "4h"),
        ("model_vfx_param_id_offsets", "4h"),
    )

    FIELD_INFO = MSBPartGParam.FIELD_INFO | _BaseMSBObject.FIELD_INFO | {
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
        "collision_hit_filter": MapFieldInfo(
            "Collision Hit Filter",
            bool,
            False,
            "Unclear what this does when enabled.",
        ),
        "set_main_object_structure_bools": MapFieldInfo(
            "Set Main Object Structure Bools",
            bool,
            False,
            "Unknown.",
        ),
        "animation_ids": MapFieldInfo(
            "Animation IDs",
            list,
            [-1, -1, -1, -1],
            "Default animation IDs for object (e.g. corpse poses). Only the first is used, according to Pav.",
        ),
        "model_vfx_param_id_offsets": MapFieldInfo(
            "Model VFX Param ID Offsets",
            list,
            [0, 0, 0, 0],
            "Offsets for model VFX param IDs. Only the first is used, according to Pav.",
        ),
    }

    FIELD_ORDER = _BaseMSBObject.FIELD_ORDER + (
        # "backread_groups",
        "break_term",
        "net_sync_type",
        "collision_hit_filter",
        "set_main_object_structure_bools",
        "animation_ids",
        "model_vfx_param_id_offsets",
    ) + MSBPartGParam.FIELD_ORDER

    break_term: int
    net_sync_type: int
    collision_hit_filter: bool
    set_main_object_structure_bools: bool
    animation_ids: list[int, int, int, int]
    model_vfx_param_id_offsets: list[int, int, int, int]


class MSBCharacter(_BaseMSBCharacter, MSBPartGParam):
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        "8x",
        ("ai_id", "i"),
        ("character_id", "i"),
        ("talk_id", "i"),
        ("player_id", "i"),
        ("chr_unk_x18_x1c", "i"),
        ("_draw_parent_index", "i"),
        ("chr_unk_x20_x22", "h"),
        "6x",
        ("_patrol_region_indices", "8h"),
        ("default_animation", "i"),
        ("damage_animation", "i"),
    )

    FIELD_INFO = MSBPartGParam.FIELD_INFO | _BaseMSBCharacter.FIELD_INFO | {
        "chr_unk_x18_x1c": MapFieldInfo(
            "Unknown Chr [18-1c]",
            int,
            0,
            "Unknown integer.",
        ),
        "chr_unk_x20_x22": MapFieldInfo(
            "Unknown Chr [20-22]",
            int,
            0,
            "Unknown 16-bit integer.",
        ),
    }

    FIELD_ORDER = _BaseMSBCharacter.FIELD_ORDER + (
        "chr_unk_x18_x1c",
        "chr_unk_x20_x22",
    ) + MSBPartGParam.FIELD_ORDER

    chr_unk_x18_x1c: int
    chr_unk_x20_x22: int


class MSBPlayerStart(_BaseMSBPlayerStart, MSBPart):

    FIELD_INFO = MSBPart.FIELD_INFO | _BaseMSBPlayerStart.FIELD_INFO
    FIELD_ORDER = _BaseMSBPlayerStart.FIELD_ORDER + MSBPart.FIELD_ORDER


class MSBCollision(_BaseMSBCollision, MSBPartSceneGParam):
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        ("hit_filter_id", "B"),
        ("sound_space_type", "B"),
        ("_environment_event_index", "h"),
        ("reflect_plane_height", "f"),
        ("__area_name_id", "h"),
        ("starts_disabled", "?"),
        ("unk_x0b_x0c", "B"),
        ("attached_bonfire", "i"),
        ("__play_region_id", "i"),
        ("camera_1_id", "h"),
        ("camera_2_id", "h"),
    )

    FIELD_INFO = MSBPartSceneGParam.FIELD_INFO | _BaseMSBCollision.FIELD_INFO | {
        "unk_x0b_x0c": MapFieldInfo(
            "Unknown [0b-0c]",
            int,
            0,
            "Unknown. Almost always zero (in DS1 at least).",
        ),
        "attached_bonfire": MapFieldInfo(
            "Attached Lantern",
            int,
            -1,
            "If this is set to a lantern entity ID, that lantern will be unusable if any living enemy characters are "
            "on this collision. Note that this also checks for enemies that are disabled by events.",
        ),
        # TODO: Confirm Bloodborne uses the same signed system for Stable Footing Flag.
    }

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "draw_groups",
        "display_groups",
        "backread_groups",
        "hit_filter_id",
        "sound_space_type",
        "environment_event_name",
        "reflect_plane_height",
        "area_name_id",
        "force_area_banner",
        "starts_disabled",
        "unk_x0b_x0c",
        "attached_bonfire",
        "play_region_id",
        "stable_footing_flag",
        "camera_1_id",
        "camera_2_id",
    ) + MSBPartSceneGParam.FIELD_ORDER

    unk_x0b_x0c: int

    def pack_type_data(self):
        """Pack to bytes, presumably as part of a full `MSB` pack."""

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
            __area_name_id=signed_area_name_id,
            starts_disabled=self.starts_disabled,
            unk_x0b_x0c=self.unk_x0b_x0c,
            attached_bonfire=self.attached_bonfire,
            __play_region_id=play_region_id,
            camera_1_id=self.camera_1_id,
            camera_2_id=self.camera_2_id,
        )


class MSBNavmesh(_BaseMSBNavmesh, MSBPart):
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        "8x",
    )

    FIELD_INFO = MSBPart.FIELD_INFO | _BaseMSBNavmesh.FIELD_INFO

    FIELD_ORDER = _BaseMSBNavmesh.FIELD_ORDER + (
        "backread_groups",  # TODO: guessing these might be used here?
    )


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
            (21, 0, 0, 0),
            "Vanilla name or 'mAA_BB_CC_DD'-style name or (AA, BB, CC, DD) sequence of the map to be loaded.",
        ),
    }

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        "draw_groups",
        "display_groups",
        "backread_groups",  # TODO: guessing these might be used here?
        "collision_name",
        "connected_map",
    )


class MSBOtherPart(MSBPart):
    """Unknown part (enum -1). No data."""

    ENTRY_SUBTYPE = MSBPartSubtype.Other

    def unpack_type_data(self, msb_buffer):
        """No data to unpack."""
        pass

    def pack_type_data(self):
        """No data to pack."""
        return b""


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
        MSBPartSubtype.Other: MSBOtherPart,
    }
    SUBTYPE_OFFSET = 20
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
    Other: tp.Sequence[MSBOtherPart]

    new_map_piece: tp.Callable[..., MSBMapPiece]
    new_object: tp.Callable[..., MSBObject]
    new_character: tp.Callable[..., MSBCharacter]
    new_player_start: tp.Callable[..., MSBPlayerStart]
    new_collision: tp.Callable[..., MSBCollision]
    new_navmesh: tp.Callable[..., MSBNavmesh]
    new_unused_object: tp.Callable[..., MSBUnusedObject]
    new_unused_character: tp.Callable[..., MSBUnusedCharacter]
    new_map_connection: tp.Callable[..., MSBMapConnection]
    new_other: tp.Callable[..., MSBOtherPart] = partialmethod(_BaseMSBPartList.new, MSBPartSubtype.Other)


for _entry_subtype in MSBPartSubtype:
    setattr(
        MSBPartList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
