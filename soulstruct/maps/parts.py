from io import BufferedReader, BytesIO
from enum import IntEnum
import struct

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer, Vector


class MSB_PART_TYPE(IntEnum):
    MapPiece = 0
    Object = 1
    Character = 2
    Player = 4
    Collision = 5
    Navmesh = 8
    DummyObject = 9
    DummyCharacter = 10
    MapLoadTrigger = 11


def MSBPart(msb_buffer):
    """Detects the appropriate subclass of BaseMSBEvent to instantiate."""
    # TODO: support more types?
    return BaseMSBPart.auto_part_subclass(msb_buffer)


class BaseMSBPart(object):
    PART_HEADER_STRUCT = BinaryStruct(
        ('name_offset', 'i'),
        ('part_type', 'i'),
        ('part_type_index', 'i'),
        ('model_index', 'I'),
        ('sib_offset', 'i'),
        ('translate', '3f'),
        ('rotate', '3f'),
        ('scale', '3f'),
        ('draw_groups', '4I'),
        ('display_groups', '4I'),
        ('base_data_offset', 'i'),
        ('type_data_offset', 'i'),
        '4x',
    )

    PART_BASE_DATA_STRUCT = BinaryStruct(
        ('entity_id', 'i'),
        ('ambient_light_id', 'b'),
        ('fog_id', 'b'),
        ('scattered_light_id', 'b'),
        ('lens_flare_id', 'b'),
        ('shadow_id', 'b'),
        ('dof_id', 'b'),
        ('tone_map_id', 'b'),
        ('tone_correct_id', 'b'),
        ('point_light_id', 'b'),
        ('lod_param_id', 'b'),
        'x',
        ('is_shadow_source', '?'),
        ('is_shadow_destination', '?'),
        ('is_shadow_only', '?'),
        ('draw_by_reflect_cam', '?'),
        ('draw_only_reflect_cam', '?'),
        ('use_depth_bias_float', '?'),
        ('disable_point_light_effect', '?'),
        '2x',
    )

    PART_TYPE = -1

    def __init__(self, msb_part_source):
        self.name = ''
        self.sib_path = ''
        self.part_type_index = None  # TODO: dodgy part index seems to break ObjAct events and some cutscene characters
        self.model_index = None
        self.translate = Vector(1, 1, 1)
        self.rotate = Vector(1, 1, 1)
        self.scale = Vector(1, 1, 1)  # only relevant for MapPiece and Object
        self.draw_groups = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
        self.display_groups = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
        self.entity_id = None

        # Lighting parameters
        self.ambient_light_id = None
        self.fog_id = None
        self.scattered_light_id = None
        self.lens_flare_id = None
        self.shadow_id = None
        self.dof_id = None
        self.tone_map_id = None
        self.tone_correct_id = None
        self.point_light_id = None

        # Additional parameters (mostly unknown)
        self.lod_param_id = None
        self.is_shadow_source = None
        self.is_shadow_destination = None
        self.is_shadow_only = None
        self.draw_by_reflect_cam = None
        self.draw_only_reflect_cam = None
        self.use_depth_bias_float = None
        self.disable_point_light_effect = None

        if isinstance(msb_part_source, bytes):
            msb_part_source = BytesIO(msb_part_source)
        if isinstance(msb_part_source, BufferedReader):
            self.unpack(msb_part_source)
        else:
            raise TypeError("'msb_part_source' must be a buffer or bytes.")

    def unpack(self, msb_buffer):
        raise NotImplementedError

    def unpack_base(self, msb_buffer):
        part_offset = msb_buffer.tell()

        header = self.PART_HEADER_STRUCT.unpack(msb_buffer)
        if header.part_type != self.PART_TYPE:
            raise ValueError(f"Unexpected part type enum {header.part_type} for class {self.__class__.__name__}.")
        self.model_index = header.model_index
        self.part_type_index = header.part_type_index
        for transform in ('translate', 'rotate', 'scale'):
            setattr(self, transform, Vector(getattr(header, transform)))
        self.draw_groups = header.draw_groups
        self.display_groups = header.display_groups
        self.name = read_chars_from_buffer(msb_buffer, offset=part_offset + header.name_offset, encoding='shift-jis')
        self.sib_path = read_chars_from_buffer(msb_buffer, offset=part_offset + header.sib_offset, encoding='shift-jis')

        msb_buffer.seek(part_offset + header.base_data_offset)
        base_data = self.PART_BASE_DATA_STRUCT.unpack(msb_buffer)

        self.entity_id = base_data.entity_id
        self.ambient_light_id = base_data.ambient_light_id
        self.fog_id = base_data.fog_id
        self.scattered_light_id = base_data.scattered_light_id
        self.lens_flare_id = base_data.lens_flare_id
        self.shadow_id = base_data.shadow_id
        self.dof_id = base_data.dof_id
        self.tone_map_id = base_data.tone_map_id
        self.tone_correct_id = base_data.tone_correct_id
        self.point_light_id = base_data.point_light_id
        self.lod_param_id = base_data.lod_param_id
        self.is_shadow_source = base_data.is_shadow_source
        self.is_shadow_destination = base_data.is_shadow_destination
        self.is_shadow_only = base_data.is_shadow_only
        self.draw_by_reflect_cam = base_data.draw_by_reflect_cam
        self.draw_only_reflect_cam = base_data.draw_only_reflect_cam
        self.use_depth_bias_float = base_data.use_depth_bias_float
        self.disable_point_light_effect = base_data.disable_point_light_effect

        msb_buffer.seek(part_offset + header.type_data_offset)
        # Ready for subclass type data unpack.

    @staticmethod
    def auto_part_subclass(msb_buffer):
        old_offset = msb_buffer.tell()
        msb_buffer.seek(old_offset + 4)
        try:
            part_type_int = struct.unpack('i', msb_buffer.read(4))[0]
            part_type = MSB_PART_TYPE(part_type_int)
        except (ValueError, TypeError):
            part_type = None
        msb_buffer.seek(old_offset)
        return MSB_PART_TYPE_CLASSES[part_type](msb_buffer)


class MSBMapPiece(BaseMSBPart):
    """Visible map piece. Does not include hitboxes (collision)."""

    MAP_PIECE_STRUCT = (
        '8x',
    )

    PART_TYPE = MSB_PART_TYPE.MapPiece

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        BinaryStruct(*self.MAP_PIECE_STRUCT).unpack(msb_buffer)  # Simply checks for the nulls.


class MSBObject(BaseMSBPart):
    """Physical object instance."""

    OBJECT_STRUCT = (
        '4x',
        ('collision_index', 'i'),
        ('unk_x08_x0c', 'i'),
        ('unk_x0c_x0e', 'h'),
        ('unk_x0e_x10', 'h'),
        ('unk_x10_x14', 'i'),
    )

    PART_TYPE = MSB_PART_TYPE.Object

    def __init__(self, msb_part_source):
        self.collision_index = None
        self.unk_x08_x0c = None
        self.unk_x0c_x0e = None
        self.unk_x0e_x10 = None
        self.unk_x10_x14 = None
        super().__init__(msb_part_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.OBJECT_STRUCT).unpack(msb_buffer)
        self.collision_index = data.collision_index
        self.unk_x08_x0c = data.unk_x08_x0c
        self.unk_x0c_x0e = data.unk_x0c_x0e
        self.unk_x0e_x10 = data.unk_x0e_x10
        self.unk_x10_x14 = data.unk_x10_x14


class MSBCharacter(BaseMSBPart):
    """Physical character instance."""

    CHARACTER_STRUCT = (
        '8x',
        ('think_param_id', 'i'),
        ('npc_param_id', 'i'),
        ('talk_id', 'i'),
        ('unk_x14_x18', 'f'),
        ('chara_init_id', 'i'),
        ('collision_index', 'i'),
        '8x',
        ('patrol_point_indices', '8h'),
        ('unk_x38_x3c', 'i'),
        ('unk_x3c_x40', 'i'),
    )

    PART_TYPE = MSB_PART_TYPE.Character

    def __init__(self, msb_part_source):
        self.think_param_id = None
        self.npc_param_id = None
        self.talk_id = None
        self.unk_x14_x18 = None
        self.chara_init_id = None
        self.collision_index = None
        self.patrol_point_indices = None
        self.unk_x38_x3c = None
        self.unk_x3c_x40 = None
        super().__init__(msb_part_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.CHARACTER_STRUCT).unpack(msb_buffer)
        self.think_param_id = data.think_param_id
        self.npc_param_id = data.npc_param_id
        self.talk_id = data.talk_id
        self.unk_x14_x18 = data.unk_x14_x18
        self.chara_init_id = data.chara_init_id
        self.collision_index = data.collision_index
        self.patrol_point_indices = data.patrol_point_indices
        self.unk_x38_x3c = data.unk_x38_x3c
        self.unk_x3c_x40 = data.unk_x3c_x40


class MSBPlayer(BaseMSBPart):
    """Starting point for a player character (e.g. a warp point)."""

    PLAYER_STRUCT = (
        '16x',
    )

    PART_TYPE = MSB_PART_TYPE.Player

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        BinaryStruct(*self.PLAYER_STRUCT).unpack(msb_buffer)  # Simply checks for the nulls.


class MSBCollision(BaseMSBPart):
    """Physical hitbox geometry. Usually these are floor pieces."""

    COLLISION_STRUCT = (
        ('hit_filter_id', 'b'),
        ('sound_space_type', 'b'),
        ('env_light_map_spot_index', 'h'),
        ('reflect_plane_height', 'f'),
        ('navmesh_groups', '4I'),
        ('vagrant_entity_ids', '3i'),
        ('map_name_id', 'h'),
        ('disable_start', 'h'),
        ('disable_bonfire_entity_id', 'i'),
        ('minus_ones', '3i', [-1, -1, -1]),
        ('play_region_id', 'i'),
        ('lock_cam_param_id_1', 'h'),
        ('lock_cam_param_id_2', 'h'),
        '16x',
    )

    PART_TYPE = MSB_PART_TYPE.Collision

    def __init__(self, msb_part_source):
        self.hit_filter_id = None
        self.sound_space_type = None
        self.env_light_map_spot_index = None
        self.reflect_plane_height = None
        self.navmesh_groups = None
        self.vagrant_entity_ids = None
        self.map_name_id = None
        self.disable_start = None
        self.disable_bonfire_entity_id = None
        self.play_region_id = None
        self.lock_cam_param_id_1 = None
        self.lock_cam_param_id_2 = None
        super().__init__(msb_part_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.COLLISION_STRUCT).unpack(msb_buffer)
        self.hit_filter_id = data.hit_filter_id
        self.sound_space_type = data.sound_space_type
        self.env_light_map_spot_index = data.env_light_map_spot_index
        self.reflect_plane_height = data.reflect_plane_height
        self.navmesh_groups = data.navmesh_groups
        self.vagrant_entity_ids = data.vagrant_entity_ids
        self.map_name_id = data.map_name_id
        self.disable_start = data.disable_start
        self.disable_bonfire_entity_id = data.disable_bonfire_entity_id
        self.play_region_id = data.play_region_id
        self.lock_cam_param_id_1 = data.lock_cam_param_id_1
        self.lock_cam_param_id_2 = data.lock_cam_param_id_2


class MSBNavmesh(BaseMSBPart):
    """AI navigation mesh ('navmesh'). Often called 'navimesh' in the game files."""

    NAVMESH_STRUCT = (
        ('navmesh_groups', '4I'),
        '16x',
    )

    PART_TYPE = MSB_PART_TYPE.Navmesh

    def __init__(self, msb_part_source):
        self.navmesh_groups = None
        super().__init__(msb_part_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.NAVMESH_STRUCT).unpack(msb_buffer)
        self.navmesh_groups = data.navmesh_groups


class MSBDummyObject(MSBObject):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to standard MSBObject."""
    PART_TYPE = MSB_PART_TYPE.DummyObject


class MSBDummyCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to standard MSBCharacter."""
    PART_TYPE = MSB_PART_TYPE.DummyCharacter


class MSBMapLoadTrigger(BaseMSBPart):
    """Links to an MSBCollision entry and causes another map to load when the player stands on that collision."""

    MAP_LOAD_TRIGGER_STRUCT = (
        ('collision_index', 'i'),
        ('map_id', '4b'),
        '8x',
    )

    PART_TYPE = MSB_PART_TYPE.MapLoadTrigger

    def __init__(self, msb_part_source):
        self.collision_index = None
        self.map_id = None
        super().__init__(msb_part_source)

    def unpack(self, msb_buffer):
        self.unpack_base(msb_buffer)
        data = BinaryStruct(*self.MAP_LOAD_TRIGGER_STRUCT).unpack(msb_buffer)
        self.collision_index = data.collision_index
        self.map_id = data.map_id  # TODO: Convert to a GameMap instance.


MSB_PART_TYPE_CLASSES = {
    MSB_PART_TYPE.MapPiece: MSBMapPiece,
    MSB_PART_TYPE.Object: MSBObject,
    MSB_PART_TYPE.Character: MSBCharacter,
    MSB_PART_TYPE.Player: MSBPlayer,
    MSB_PART_TYPE.Collision: MSBCollision,
    MSB_PART_TYPE.Navmesh: MSBNavmesh,
    MSB_PART_TYPE.DummyObject: MSBDummyObject,
    MSB_PART_TYPE.DummyCharacter: MSBDummyCharacter,
    MSB_PART_TYPE.MapLoadTrigger: MSBMapLoadTrigger,
}
