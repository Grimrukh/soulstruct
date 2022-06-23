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

from soulstruct.base.maps.msb.exceptions import MapError
from soulstruct.base.maps.msb.parts import *
from soulstruct.base.maps.msb.utils import MapFieldInfo
from soulstruct.bloodborne.game_types import *
from soulstruct.exceptions import SoulstructError, InvalidFieldValueError
from soulstruct.utilities.binary import BinaryStruct, BinaryReader
from soulstruct.utilities.conversion import int_group_to_bit_set, bit_set_to_int_group
from soulstruct.utilities.maths import Vector3
from soulstruct.utilities.misc import partialmethod

from .constants import get_map
from .enums import *
from .msb_entry import MSBEntryList

if tp.TYPE_CHECKING:
    from .msb import MSB
    from .regions import MSBRegion
    from .events import MSBEnvironmentEvent


class MSBPart(
    BaseMSBPart,
    MSB_Scale,
    MSB_ModelName,
    MSB_DrawParent,
    MSB_DrawGroups,
    MSB_DisplayGroups,
    MSB_BackreadGroups,
    abc.ABC,
):
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
    DRAW_GROUP_COUNT = 256
    DISPLAY_GROUP_COUNT = 256
    BACKREAD_GROUP_COUNT = 256

    FIELD_INFO = BaseMSBPart.FIELD_INFO | {
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
            "Scale of part. Only works for Map Pieces and Objects.",
        ),
        "draw_groups": MapFieldInfo(
            "Draw Groups",
            list,
            set(range(DRAW_GROUP_COUNT)),
            "Draw groups of part. This part will be drawn when the corresponding display group is active.",
        ),
        "display_groups": MapFieldInfo(
            "Display Groups",
            list,
            set(range(DISPLAY_GROUP_COUNT)),
            "Display groups are present in all MSB Parts, but only function for collisions.",
        ),
        "backread_groups": MapFieldInfo(
            "Backread Groups",
            list,
            set(range(BACKREAD_GROUP_COUNT)),
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

    sib_path: str
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
        super().__init__(source, **kwargs)

    def unpack(self, msb_reader: BinaryReader):
        part_offset = msb_reader.position

        header = msb_reader.unpack_struct(self.PART_HEADER_STRUCT)
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
        self.description = msb_reader.unpack_string(
            offset=part_offset + header["__description_offset"], encoding="utf-16-le",
        )
        self.name = msb_reader.unpack_string(
            offset=part_offset + header["__name_offset"], encoding="utf-16-le",
        )
        self.sib_path = msb_reader.unpack_string(
            offset=part_offset + header["__sib_path_offset"], encoding="utf-16-le",
        )

        msb_reader.seek(part_offset + header["__base_data_offset"])
        base_data = msb_reader.unpack_struct(self.PART_BASE_DATA_STRUCT)
        self.set(**base_data)

        msb_reader.seek(part_offset + header["__type_data_offset"])
        self.unpack_type_data(msb_reader)

        self._unpack_gparam_data(msb_reader, part_offset, header)
        self._unpack_scene_gparam_data(msb_reader, part_offset, header)

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
        packed_base_data = self.PART_BASE_DATA_STRUCT.pack(self)
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

    def _unpack_gparam_data(self, msb_reader: BinaryReader, part_offset, header):
        pass

    def _pack_gparam_data(self):
        return b""

    def _unpack_scene_gparam_data(self, msb_reader: BinaryReader, part_offset, header):
        pass

    def _pack_scene_gparam_data(self):
        return b""


class MSBPartGParam(MSBPart, abc.ABC):
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

    def _unpack_gparam_data(self, msb_reader: BinaryReader, part_offset, header):
        if header["__gparam_data_offset"] == 0:
            raise ValueError(f"Zero GParam offset found in GParam-supporting part {self.name}.")
        msb_reader.seek(part_offset + header["__gparam_data_offset"])
        gparam_data = msb_reader.unpack_struct(self.PART_GPARAM_STRUCT)
        self.set(**gparam_data)

    def _pack_gparam_data(self):
        return self.PART_GPARAM_STRUCT.pack(self)


class MSBPartSceneGParam(MSBPartGParam, abc.ABC):
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

    def _unpack_scene_gparam_data(self, msb_reader: BinaryReader, part_offset, header):
        if header["__scene_gparam_data_offset"] == 0:
            raise ValueError(f"Zero SceneGParam offset found in SceneGParam-supporting part {self.name}.")
        msb_reader.seek(part_offset + header["__scene_gparam_data_offset"])
        scene_gparam_data = msb_reader.unpack_struct(self.PART_SCENE_GPARAM_STRUCT)
        self.set(**scene_gparam_data)

    def _pack_scene_gparam_data(self):
        return self.PART_SCENE_GPARAM_STRUCT.pack(self)


class MSBMapPiece(MSBPart, MSBPartGParam):
    """No further modifications beyond inheritance of GParam."""

    FIELD_INFO = MSBPartGParam.FIELD_INFO | {
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
    ) + MSBPartGParam.FIELD_ORDER


class MSBObject(MSBPart, MSBPartGParam):
    """Interactable object. Note that Bloodborne has six-digit model IDs for Objects."""

    ENTRY_SUBTYPE = MSBPartSubtype.Object
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

    FIELD_INFO = MSBPartGParam.FIELD_INFO | {
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
            "a simpler alternative to draw groups (unsure what will take precedence if any draw groups are set). Set "
            "to an empty string to indicate no draw parent (`None`).",
        ),
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

    FIELD_ORDER = (
        "model_name",
        "entity_id",
        "translate",
        "rotate",
        # "scale",
        "draw_parent_name",
        "draw_groups",
        # "display_groups",
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


class MSBCharacter(MSBPart, MSBPartGParam):
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

    FIELD_INFO = MSBPartGParam.FIELD_INFO | {
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
            "a simpler alternative to draw groups (unsure what will take precedence if any draw groups are set). Set "
            "to an empty string to indicate no draw parent (`None`).",
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
        "chr_unk_x18_x1c",
        "chr_unk_x20_x22",
    ) + MSBPartGParam.FIELD_ORDER

    ai_id: int
    character_id: int
    talk_id: int
    player_id: int
    draw_parent_name: tp.Optional[str]
    default_animation: int
    damage_animation: int
    chr_unk_x18_x1c: int
    chr_unk_x20_x22: int


class MSBPlayerStart(MSBPart):
    ENTRY_SUBTYPE = MSBPartSubtype.PlayerStart
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        "16x",
    )

    FIELD_INFO = MSBPart.FIELD_INFO | {
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
    ) + MSBPart.FIELD_ORDER

    def __init__(self, source=None, **kwargs):
        if source is None:
            # Set some different defaults.
            kwargs.setdefault("model_name", "c0000")
        super().__init__(source=source, **kwargs)


class MSBCollision(MSBPart, MSBPartSceneGParam):
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

    FIELD_INFO = MSBPartSceneGParam.FIELD_INFO | {
        "display_groups": MapFieldInfo(  # overwrites `MSBPart` definition
            "Display Groups",
            list,
            set(range(MSBPart.DISPLAY_GROUP_COUNT)),
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

    REFERENCE_FIELDS = MSBPart.REFERENCE_FIELDS | {"events": ["environment_event_name"]}

    hit_filter_id: CollisionHitFilter
    sound_space_type: int
    environment_event_name: tp.Optional[str]
    reflect_plane_height: float
    area_name_id: int
    starts_disabled: bool
    attached_bonfire: int
    camera_1_id: int
    camera_2_id: int
    unk_x0b_x0c: int

    def __init__(self, source=None, **kwargs):
        self._environment_event_index = -1
        self._force_area_banner = False  # Custom field (see property).
        self._play_region_id = 0
        self._stable_footing_flag = 0
        super().__init__(source=source, **kwargs)

    def unpack_type_data(self, msb_reader: BinaryReader):
        data = msb_reader.unpack_struct(self.PART_TYPE_DATA_STRUCT, exclude_asserted=True)
        self.set(**data)
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
        if value != 0 and self._stable_footing_flag != 0:
            raise InvalidFieldValueError(
                f"Cannot set 'play_region_id' to a non-zero value ({value}) while `stable_footing_flag` is non-zero."
            )
        if not isinstance(value, int) or value <= -10:
            raise InvalidFieldValueError("'play_region_id' must be an integer greater than or equal to -9.")
        self._play_region_id = value

    @property
    def stable_footing_flag(self):
        return self._stable_footing_flag

    @stable_footing_flag.setter
    def stable_footing_flag(self, value):
        if not isinstance(value, int) or value < -1:
            raise InvalidFieldValueError(
                f"`stable_footing_flag` must be an integer no less than -1 (Collision '{self.name}')."
            )
        if value != 0 and self._play_region_id != 0:
            raise InvalidFieldValueError(
                f"Cannot set `stable_footing_flag` to a non-zero value while 'play_region_id' is not zero, even if it "
                f"is just -1: {self._play_region_id} (Collision '{self.name}')."
            )
        self._stable_footing_flag = value

    def set_indices(self, indices: PartIndicesData):
        super().set_indices(indices)
        if self.environment_event_name:
            self._environment_event_index = indices.local_environment_indices[self.environment_event_name]
        else:
            self._environment_event_index = -1

    def set_names(self, names: PartNamesData):
        super().set_names(names)
        if self._environment_event_index != -1:
            try:
                self.environment_event_name = names.environment_names[self._environment_event_index]
            except IndexError:
                for i, env in enumerate(names.environment_names):
                    print(i, env)
                print(self._environment_event_index)
                self.environment_event_name = f"BROKEN ({self._environment_event_index})"
        else:
            self.environment_event_name = None


class MSBNavmesh(MSBPart):

    ENTRY_SUBTYPE = MSBPartSubtype.Navmesh
    PART_TYPE_DATA_STRUCT = BinaryStruct(
        "8x",
    )

    FIELD_INFO = MSBPart.FIELD_INFO | {
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
        "backread_groups",  # TODO: guessing these might be used here?
    )


class MSBUnusedObject(MSBObject):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to `MSBObject`."""

    ENTRY_SUBTYPE = MSBPartSubtype.UnusedObject


class MSBUnusedCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`."""

    ENTRY_SUBTYPE = MSBPartSubtype.UnusedCharacter


class MSBMapConnection(MSBPart, MSBPart):
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
    GET_MAP = staticmethod(get_map)

    FIELD_INFO = MSBPart.FIELD_INFO | {
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

    REFERENCE_FIELDS = MSBPart.REFERENCE_FIELDS | {"parts": ["collision_name"]}

    collision_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._collision_index = -1
        self._connected_map = None
        super().__init__(source=source, **kwargs)

    def unpack_type_data(self, msb_reader):
        data = msb_reader.unpack_struct(self.PART_TYPE_DATA_STRUCT)
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

    def set_indices(self, indices: PartIndicesData):
        super().set_indices(indices)
        self._collision_index = indices.local_collision_indices[self.collision_name] if self.collision_name else -1

    def set_names(self, names: PartNamesData):
        super().set_names(names)
        self.collision_name = names.collision_names[self._collision_index] if self._collision_index != -1 else None


class MSBOtherPart(MSBPart):
    """Unknown part (enum -1). No data."""

    ENTRY_SUBTYPE = MSBPartSubtype.Other

    def unpack_type_data(self, msb_reader: BinaryReader):
        """No data to unpack."""
        pass

    def pack_type_data(self):
        """No data to pack."""
        return b""


class MSBPartList(MSBEntryList[MSBPart]):
    INTERNAL_NAME = "PARTS_PARAM_ST"
    ENTRY_LIST_NAME = "Parts"
    ENTRY_SUBTYPE_ENUM = MSBPartSubtype
    SUBTYPE_CLASSES: dict[MSBPartSubtype, tp.Type[MSBPart]] = {
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
    new_other: tp.Callable[..., MSBOtherPart] = partialmethod(new, MSBPartSubtype.Other)

    def pack_entry(self, index: int, entry: MSBPart):
        return entry.pack()

    def set_indices(
        self, model_indices, local_environment_indices, region_indices, part_indices, local_collision_indices,
    ):
        """Local type-specific index only.

        Events and other Parts may point to Parts by global entry index, but it seems the local index still matters, as
        ObjAct Events seem to break when the local object index is changed. It's possible this was just an idiosyncracy
        of Wulf's MSB Editor. Either way, this method should ensure the global and local indices are consistent.

        Remember that Navmesh indices are hard-coded into MCP and MCG files. Also note that cutscene files (remo) access
        MSB parts by index as well, which is why map mods tend to break them so often.

        `local_environment_indices` are needed for Collisions and `local_collision_indices` are needed for Map Load
        Triggers. No other MSB entry type requires local subtype indices.
        """
        type_indices = {}
        for entry in self._entries:
            try:
                indices = PartIndicesData(
                    part_type_index=type_indices.setdefault(entry.ENTRY_SUBTYPE, 0),
                    model_indices=model_indices,
                    local_environment_indices=local_environment_indices,
                    region_indices=region_indices,
                    part_indices=part_indices,
                    local_collision_indices=local_collision_indices,
                )
                entry.set_indices(indices)
            except KeyError as e:
                raise SoulstructError(f"Missing name referenced by {entry.name}: {str(e)}")
            else:
                type_indices[entry.ENTRY_SUBTYPE] += 1

    def set_names(
        self, model_names, environment_names, region_names, part_names, collision_names,
    ):
        for entry in self._entries:
            names = PartNamesData(
                model_names=model_names,
                region_names=region_names,
                environment_names=environment_names,
                part_names=part_names,
                collision_names=collision_names,
            )
            entry.set_names(names)

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
        self, collision: tp.Union[str, MSBCollision], connected_map, name=None, draw_groups=None, display_groups=None
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


for _entry_subtype in iter(MSBPartSubtype):
    setattr(
        MSBPartList,
        _entry_subtype.pluralized_name,
        property(lambda self, _e=_entry_subtype: [e for e in self._entries if e.ENTRY_SUBTYPE == _e]),
    )
