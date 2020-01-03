from io import BufferedReader, BytesIO
from enum import IntEnum
import struct

from soulstruct.core import InvalidFieldValueError
from soulstruct.maps.core import MSBEntryEntity
from soulstruct.utilities import BinaryStruct, read_chars_from_buffer, Vector


class MSB_PART_TYPE(IntEnum):
    MapPiece = 0
    Object = 1
    Character = 2
    PlayerStarts = 4
    Collision = 5
    Navmesh = 8
    UnusedObject = 9
    UnusedCharacter = 10
    MapConnection = 11


def MSBPart(msb_buffer):
    """Detects the appropriate subclass of BaseMSBEvent to instantiate."""
    return BaseMSBPart.auto_part_subclass(msb_buffer)


class BaseMSBPart(MSBEntryEntity):
    PART_HEADER_STRUCT = BinaryStruct(
        ('name_offset', 'i'),
        ('part_type', 'i'),
        ('part_type_index', 'i'),
        ('model_index', 'I'),
        ('sib_path_offset', 'i'),
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

    FIELD_INFO = {
        'entity_id': (
            'Entity ID', True, int,
            "Entity ID used to refer to the part in other game files."),
        'translate': (
            'Translate', True, Vector,
            "3D coordinates of the part's position. Note that the anchor of the part is usually at its base."),
        'rotate': (
            'Rotate', True, Vector,
            "Euler angles for part rotation around its local X, Y, and Z axes."),
        'scale': (
            'Scale', True, Vector,
            "Scale of part. Only relevant for objects and collisions."),
        'draw_groups': (
            'Draw Groups', True, list,
            "Draw groups of part. These are not yet fully understood, but they determine when the part appears."),
        'display_groups': (
            'Display Groups', True, list,
            "Display groups of part. These are not yet fully understood, but they determine when the part appears."),
        'ambient_light_id': (
            'Ambient Light ID', True, int,  # TODO: Link to Lighting.
            "ID of Ambient Light parameter to use in this map's lighting parameters (DrawParam)."),
        'fog_id': (
            'Fog ID', True, int,
            "ID of Fog parameter to use in this map's lighting parameters (DrawParam)."),
        'scattered_light_id': (
            'Scattered Light ID', True, int,
            "ID of Scattered Light parameter to use in this map's lighting parameters (DrawParam)."),
        'lens_flare_id': (
            'Lens Flare ID', True, int,
            "ID of Lens Flare parameter (both types) to use in this map's lighting parameters (DrawParam)."),
        'shadow_id': (
            'Shadow ID', True, int,
            "ID of Shadow parameter to use in this map's lighting parameters (DrawParam)."),
        'dof_id': (
            'DoF ID', True, int,
            "ID of Depth of Field (DoF) ID parameter to use in this map's lighting parameters (DrawParam)."),
        'tone_map_id': (
            'Tone Map ID', True, int,
            "ID of Tone Map parameter to use in this map's lighting parameters (DrawParam)."),
        'point_light_id': (
            'Player Light ID', True, int,
            "ID of Player Light parameter (point light) to use in this map's lighting parameters (DrawParam)."),
        'tone_correct_id': (
            'Tone Correction ID', True, int,
            "ID of Tone Correction parameter to use in this map's lighting parameters (DrawParam)."),
        'lod_param_id': (
            'LoD Param ID', False, int,
            "ID of Level of Detail (LoD) parameter to use in this map's lighting parameters (DrawParam)."),
        'is_shadow_source': (
            'Can Cast Shadow', True, bool,
            "If True, this entity will cast dynamic shadows."),
        'is_shadow_destination': (
            'Can Receive Shadow', True, bool,
            "If True, this entity can have dynamic shadows cast onto it."),
        'is_shadow_only': (
            'Cast Shadow Only', True, bool,
            "If True, this entity only casts shadows."),
        'draw_by_reflect_cam': (
            'Is Reflected', True, bool,
            "If True, this entity will be reflected in water, etc."),
        'draw_only_reflect_cam': (
            'Is Only Reflected', True, bool,
            "If True, this entity will only be drawn in reflections in water, etc."),
        'use_depth_bias_float': (
            'Use Depth Bias Float', True, bool,
            "Unknown."),
        'disable_point_light_effect': (
            'Ignore Player Light', True, bool,
            "If True, this entity will not be illuminated by player light (I think)."),
    }

    ENTRY_TYPE = None

    def __init__(self, msb_part_source):
        super().__init__()
        self.sib_path = ''
        self._part_type_index = None  # TODO: investigate Wulf MSB Editor issue with global index misalignment
        self.model_name = None
        self._model_index = None
        self.translate = Vector(1, 1, 1)
        self.rotate = Vector(1, 1, 1)
        self.scale = Vector(1, 1, 1)  # only relevant for MapPiece and Object
        self.draw_groups = list(range(128))  # [0, 1, 2, ..., 128]
        self.display_groups = list(range(128))  # [0, 1, 2, ..., 128]

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

    def unpack_type_data(self, msb_buffer):
        raise NotImplementedError

    def unpack(self, msb_buffer):
        part_offset = msb_buffer.tell()

        header = self.PART_HEADER_STRUCT.unpack(msb_buffer)
        if header.part_type != self.ENTRY_TYPE:
            raise ValueError(f"Unexpected part type enum {header.part_type} for class {self.__class__.__name__}.")
        self._model_index = header.model_index
        self._part_type_index = header.part_type_index
        for transform in ('translate', 'rotate', 'scale'):
            setattr(self, transform, Vector(getattr(header, transform)))
        self.draw_groups = _flag_group_to_enabled_flags(header.draw_groups)
        self.display_groups = _flag_group_to_enabled_flags(header.display_groups)
        self.name = read_chars_from_buffer(
            msb_buffer, offset=part_offset + header.name_offset, encoding='shift-jis')
        self.sib_path = read_chars_from_buffer(
            msb_buffer, offset=part_offset + header.sib_path_offset, encoding='shift-jis')

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
        self.unpack_type_data(msb_buffer)

    def pack(self):
        draw_groups = _enabled_flags_to_flag_group(self.draw_groups)
        display_groups = _enabled_flags_to_flag_group(self.display_groups)

        name_offset = self.PART_HEADER_STRUCT.size
        packed_name = self.get_name_to_pack().encode('shift-jis') + b'\0'  # Name not padded on its own.
        sib_path_offset = name_offset + len(packed_name)
        packed_sib_path = self.sib_path.encode('shift-jis') + b'\0' if self.sib_path else b'\0' * 6
        while len(packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b'\0'
        base_data_offset = sib_path_offset + len(packed_sib_path)
        packed_base_data = self.PART_BASE_DATA_STRUCT.pack(
            entity_id=self.entity_id,
            ambient_light_id=self.ambient_light_id,
            fog_id=self.fog_id,
            scattered_light_id=self.scattered_light_id,
            lens_flare_id=self.lens_flare_id,
            shadow_id=self.shadow_id,
            dof_id=self.dof_id,
            tone_map_id=self.tone_map_id,
            tone_correct_id=self.tone_correct_id,
            point_light_id=self.point_light_id,
            lod_param_id=self.lod_param_id,
            is_shadow_source=self.is_shadow_source,
            is_shadow_destination=self.is_shadow_destination,
            is_shadow_only=self.is_shadow_only,
            draw_by_reflect_cam=self.draw_by_reflect_cam,
            draw_only_reflect_cam=self.draw_only_reflect_cam,
            use_depth_bias_float=self.use_depth_bias_float,
            disable_point_light_effect=self.disable_point_light_effect,
        )

        type_data_offset = base_data_offset + len(packed_base_data)
        packed_type_data = self.pack_type_data()

        packed_header = self.PART_HEADER_STRUCT.pack(
            name_offset=name_offset,
            part_type=self.ENTRY_TYPE,
            part_type_index=self._part_type_index,
            model_index=self._model_index,
            sib_path_offset=sib_path_offset,
            translate=list(self.translate),
            rotate=list(self.rotate),
            scale=list(self.scale),
            draw_groups=draw_groups,
            display_groups=display_groups,
            base_data_offset=base_data_offset,
            type_data_offset=type_data_offset,
        )

        return packed_header + packed_name + packed_sib_path + packed_base_data + packed_type_data

    def pack_type_data(self):
        raise NotImplementedError

    def set_indices(self, part_type_index, model_indices, region_indices, part_indices, local_collision_indices):
        self._part_type_index = part_type_index
        self._model_index = model_indices[self.model_name] if self.model_name else -1

    def set_names(self, model_names, region_names, part_names, collision_names):
        self.model_name = model_names[self._model_index]

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
    """Visible map piece. Does not include collisions."""

    MAP_PIECE_STRUCT = (
        '8x',
    )

    FIELD_INFO = {
        'model_name': (
            'Model Name', True, '<Maps:Models:MapPieces>',
            "Name of map piece model to use for this map piece."),
        **BaseMSBPart.FIELD_INFO,
    }

    ENTRY_TYPE = MSB_PART_TYPE.MapPiece

    def unpack_type_data(self, msb_buffer):
        BinaryStruct(*self.MAP_PIECE_STRUCT).unpack(msb_buffer)  # Simply checks for the nulls.

    def pack_type_data(self):
        return BinaryStruct(*self.MAP_PIECE_STRUCT).pack({})


class MSBObject(BaseMSBPart):
    """Physical object instance."""

    PART_OBJECT_STRUCT = (
        '4x',
        ('collision_index', 'i'),
        ('unk_x08_x0c', 'i'),
        ('object_pose', 'h'),
        ('unk_x0e_x10', 'h'),
        ('unk_x10_x14', 'i'),
        '4x',
    )

    FIELD_INFO = {
        'model_name': (
            'Model Name', True, '<Maps:Models:Objects>',
            "Name of object model to use for this object."),
        **BaseMSBPart.FIELD_INFO,
        'collision_name': (
            'Draw Parent', True, '<Maps:Parts>',
            "Object will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn."),
        'unk_x08_x0c': (
            'Unknown [08-0c]', False, int,
            "Unknown."),
        'object_pose': (
            'Object Pose', True, int,
            "ID of an object animation that determines its appearance, e.g. for different corpse poses."),
        'unk_x0e_x10': (
            'Unknown [0e-10]', False, int,
            "Unknown."),
        'unk_x10_x14': (
            'Unknown [10-14]', False, int,
            "Unknown."),
    }

    ENTRY_TYPE = MSB_PART_TYPE.Object

    def __init__(self, msb_part_source):
        self.collision_name = None
        self._collision_index = None
        self.unk_x08_x0c = None
        self.object_pose = None
        self.unk_x0e_x10 = None
        self.unk_x10_x14 = None
        super().__init__(msb_part_source)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_OBJECT_STRUCT).unpack(msb_buffer)
        self._collision_index = data.collision_index
        self.unk_x08_x0c = data.unk_x08_x0c
        self.object_pose = data.object_pose
        self.unk_x0e_x10 = data.unk_x0e_x10
        self.unk_x10_x14 = data.unk_x10_x14

    def pack_type_data(self):
        return BinaryStruct(*self.PART_OBJECT_STRUCT).pack(
            collision_index=self._collision_index,
            unk_x08_x0c=self.unk_x08_x0c,
            object_pose=self.object_pose,
            unk_x0e_x10=self.unk_x0e_x10,
            unk_x10_x14=self.unk_x10_x14,
        )

    def set_indices(self, part_type_index, model_indices, region_indices, part_indices, local_collision_indices):
        super().set_indices(part_type_index, model_indices, region_indices, part_indices, local_collision_indices)
        self._collision_index = part_indices[self.collision_name] if self.collision_name else -1

    def set_names(self, model_names, region_names, part_names, collision_names):
        super().set_names(model_names, region_names, part_names, collision_names)
        self.collision_name = part_names[self._collision_index] if self._collision_index != -1 else None


class MSBCharacter(BaseMSBPart):
    """Physical character instance."""

    PART_CHARACTER_STRUCT = (
        '8x',
        ('think_param_id', 'i'),
        ('npc_param_id', 'i'),
        ('talk_id', 'i'),
        ('unk_x14_x18', 'f'),
        ('chara_init_id', 'i'),
        ('collision_index', 'i'),
        '8x',
        ('patrol_point_indices', '8h'),
        ('default_animation', 'i'),
        ('unk_x3c_x40', 'i'),
    )

    FIELD_INFO = {
        'model_name': (
            'Model Name', True, '<Maps:Models:Characters|Players>',
            "Name of character model to use for this character."),
        **BaseMSBPart.FIELD_INFO,
        'think_param_id': (
            'AI ID', True, '<Params:AI>',
            "Character's AI. If set to -1, the default AI ID set in the NPC ID (below) will be used."),
        'npc_param_id': (
            'NPC ID', True, '<Params:NonPlayers>',
            "Basic character information. For 'player' (human) characters, most of the fields in this param entry are "
            "unused."),
        'talk_id': (
            'Talk ID', True, int,  # TODO: '<Talk>'
            "EzState ID of character, which determines their interactions (conversations, shops, etc.). This is used "
            "to look up the corresponding 'tXXXXXX.esd' file inside the 'talkesdbnd' archive for this map."),
        'unk_x14_x18': (
            'Unknown [14-18]', False, float,
            "Unknown floating-point number."),
        'chara_init_id': (
            'Player ID', True, '<Params:Players>',
            "Contains information for 'player' (human) characters, such as their stats and equipment."),
        'collision_name': (
            'Draw Parent', True, '<Maps:Parts>',
            "Character will be drawn as long as this parent (usually a Collision or Map Piece part) is drawn."),
        'patrol_point_names': (
            'Patrol Regions', True, '<MapsList:Regions>',
            "List of regions that this character will patrol between, in a looping sequence, if they have the standard "
            "AI logic."),
        'default_animation': (
            'Default Animation', True, int,  # TODO: '<Animation>'
            "Default looping animation for character."),
        'unk_x3c_x40': (
            'Unknown [3c-40]', False, int,
            "Unknown."),
    }
    ENTRY_TYPE = MSB_PART_TYPE.Character

    def __init__(self, msb_part_source):
        self.think_param_id = None
        self.npc_param_id = None
        self.talk_id = None
        self.unk_x14_x18 = None
        self.chara_init_id = None
        self.collision_name = None
        self._collision_index = None
        self.patrol_point_names = None
        self._patrol_point_indices = None
        self.default_animation = None
        self.unk_x3c_x40 = None
        super().__init__(msb_part_source)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_CHARACTER_STRUCT).unpack(msb_buffer)
        self.think_param_id = data.think_param_id
        self.npc_param_id = data.npc_param_id
        self.talk_id = data.talk_id
        self.unk_x14_x18 = data.unk_x14_x18
        self.chara_init_id = data.chara_init_id
        self._collision_index = data.collision_index
        self._patrol_point_indices = data.patrol_point_indices
        self.default_animation = data.default_animation
        self.unk_x3c_x40 = data.unk_x3c_x40

    def pack_type_data(self):
        return BinaryStruct(*self.PART_CHARACTER_STRUCT).pack(
            think_param_id=self.think_param_id,
            npc_param_id=self.npc_param_id,
            talk_id=self.talk_id,
            unk_x14_x18=self.unk_x14_x18,
            chara_init_id=self.chara_init_id,
            collision_index=self._collision_index,
            patrol_point_indices=self._patrol_point_indices,
            default_animation=self.default_animation,
            unk_x3c_x40=self.unk_x3c_x40,
        )

    def set_indices(self, part_type_index, model_indices, region_indices, part_indices, local_collision_indices):
        super().set_indices(part_type_index, model_indices, region_indices, part_indices, local_collision_indices)
        self._collision_index = part_indices[self.collision_name] if self.collision_name else -1
        self._patrol_point_indices = [region_indices[n] if n else -1 for n in self.patrol_point_names]

    def set_names(self, model_names, region_names, part_names, collision_names):
        super().set_names(model_names, region_names, part_names, collision_names)
        self.collision_name = part_names[self._collision_index] if self._collision_index != -1 else None
        self.patrol_point_names = [region_names[i] if i != -1 else None for i in self._patrol_point_indices]


class MSBPlayer(BaseMSBPart):
    """Starting point for a player character (e.g. a warp point). No additional data."""

    PLAYER_STRUCT = (
        '16x',
    )

    FIELD_INFO = {
        # model_name not exposed; should always be 'c0000'.
        **BaseMSBPart.FIELD_INFO,
    }

    ENTRY_TYPE = MSB_PART_TYPE.PlayerStarts

    def unpack_type_data(self, msb_buffer):
        BinaryStruct(*self.PLAYER_STRUCT).unpack(msb_buffer)  # Simply checks for the nulls.

    def pack_type_data(self):
        return BinaryStruct(*self.PLAYER_STRUCT).pack({})


class MSBCollision(BaseMSBPart):
    """Physical Collision geometry. Usually these are floor pieces."""

    PART_COLLISION_STRUCT = (
        ('hit_filter_id', 'b'),
        ('sound_space_type', 'b'),
        ('env_light_map_spot_index', 'h'),
        ('reflect_plane_height', 'f'),
        ('navmesh_groups', '4I'),
        ('vagrant_entity_ids', '3i'),
        ('area_name_id', 'h'),
        ('starts_disabled', 'h'),
        ('attached_bonfire', 'i'),
        ('minus_ones', '3i', [-1, -1, -1]),  # Possibly more bonfires?
        ('play_region_id', 'i'),
        ('lock_cam_param_id_1', 'h'),
        ('lock_cam_param_id_2', 'h'),
        '16x',
    )

    FIELD_INFO = {
        'model_name': (
            'Model Name', True, '<Maps:Models:Collisions>',
            "Name of collision model to use for this collision."),
        **BaseMSBPart.FIELD_INFO,
        'hit_filter_id': (
            'Hit Filter ID', True, int,
            "Determines what happens when the player activates this collision."),
        'sound_space_type': (
            'Sound Space Type', True, int,
            "Unknown."),
        'env_light_map_spot_index': (
            'Env. Lightmap Spot Index', True, int,
            "Unknown."),
        'reflect_plane_height': (
            'Reflect Plane Height', True, float,
            "Unknown."),
        'navmesh_groups': (
            'Navmesh Groups', True, list,
            "Unknown."),
        'vagrant_entity_ids': (
            'Vagrant Entity IDs', True, list,
            "Unknown."),
        'area_name_id': (
            'Area Name', True, '<Text:PlaceNames>',
            "Name of area that this collision is in, which determines the area banner that is shown when you step on "
            "this collision (a linked texture ID lookup) and the area name that appears in the load screen (text ID). "
            "Set it to -1 to use the default area name for this map (i.e. text ID XXYY for map 'mXX_YY')."),
        'force_area_banner': (
            'Show Area Banner', True, bool,
            "By default, the game will only show an area name banner when you enter a map (e.g. after warping). If "
            "this option is enabled, the area name banner will be shown when you step on this collision if the area ID "
            "changes to a new value. Typical usage is to have this disabled for collisions that are very close to a "
            "different area (a 'silent area transition') and have it enabled for collision that are further away, "
            "which produces a 'delayed area banner' effect.\n\n"
            ""
            "Do NOT enable this for two adjacent collision with different area names, or moving back and forth between "
            "those collisions will build up a huge queue of area banners to display, which can only be fixed by "
            "restarting the game entirely."),
        'starts_disabled': (
            'Starts Disabled', True, bool,
            "If True, this collision is disabled on map load and must be manually enabled with an event script."),
        'attached_bonfire': (
            'Attached Bonfire', True, int,
            "If this is set to a bonfire entity ID, that bonfire will be disabled if any living enemy characters are "
            "on this collision. Note that this also checks for enemies that are disabled by events."),
        'play_region_id': (
            'Play Region ID', True, int,
            "Determines the multiplayer (e.g. invasion) sub-area this collision is part of.\n\n"
            ""
            "NOTE: This field shares space with the stable footing flag, so only one of them can be set to a non-zero "
            "value per collision."),
        'stable_footing_flag': (
            'Stable Footing Flag', True, int,
            "This flag must be enabled for the player's stable footing (i.e. last saved position) to be updated while "
            "standing on this collision. This is used to prevent players loading inside boss arenas before the boss is "
            "defeated. If set to -1, the player's position will never be saved on this collision.\n\n"
            ""
            "NOTE: This field shares space with the play region ID, so only one of them can be set to a non-zero value "
            "per collision."),
        'lock_cam_param_id_1': (
            'Camera Param ID 1', True, '<Params:Cameras>',
            "First camera ID to use on this collision. Unsure how the two slots differ."),
        'lock_cam_param_id_2': (
            'Camera Param ID 2', True, '<Params:Cameras>',
            "Second camera ID to use on this collision. Unsure how the two slots differ."),
    }

    ENTRY_TYPE = MSB_PART_TYPE.Collision

    def __init__(self, msb_part_source):
        self.hit_filter_id = None
        self.sound_space_type = None
        self.env_light_map_spot_index = None
        self.reflect_plane_height = None
        self.navmesh_groups = None
        self.vagrant_entity_ids = None
        self.area_name_id = None
        self.__force_area_banner = None  # Custom field.
        self.starts_disabled = None
        self.attached_bonfire = None
        self.__play_region_id = None
        self.__stable_footing_flag = None
        self.lock_cam_param_id_1 = None
        self.lock_cam_param_id_2 = None
        super().__init__(msb_part_source)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_COLLISION_STRUCT).unpack(msb_buffer)
        self.hit_filter_id = data.hit_filter_id
        self.sound_space_type = data.sound_space_type
        self.env_light_map_spot_index = data.env_light_map_spot_index
        self.reflect_plane_height = data.reflect_plane_height
        self.navmesh_groups = _flag_group_to_enabled_flags(data.navmesh_groups)
        self.vagrant_entity_ids = data.vagrant_entity_ids
        self.area_name_id = abs(data.area_name_id) if data.area_name_id >= 0 else -1
        self.__force_area_banner = data.area_name_id < 0  # Custom field.
        self.starts_disabled = data.starts_disabled
        self.attached_bonfire = data.attached_bonfire
        if data.play_region_id > -10:
            self.__play_region_id = data.play_region_id
            self.__stable_footing_flag = 0
        else:
            self.__play_region_id = 0
            self.__stable_footing_flag = -data.play_region_id - 10
        self.lock_cam_param_id_1 = data.lock_cam_param_id_1
        self.lock_cam_param_id_2 = data.lock_cam_param_id_2

    @property
    def force_area_banner(self):
        return self.__force_area_banner

    @force_area_banner.setter
    def force_area_banner(self, value: bool):
        if not value and self.area_name_id == -1:
            raise InvalidFieldValueError(
                "Banner must appear when area name is set to default (-1). You must specify the area name manually to "
                "set this to False.")
        self.__force_area_banner = bool(value)

    @property
    def play_region_id(self):
        return self.__play_region_id

    @play_region_id.setter
    def play_region_id(self, value):
        if self.__stable_footing_flag != 0:
            raise InvalidFieldValueError("Cannot set 'play_region_id' to a non-zero value while 'stable_footing_flag' "
                                         "is non-zero.")
        if not isinstance(value, int) or value <= -10:
            raise InvalidFieldValueError("'play_region_id' must be an integer greater than or equal to -9.")
        self.__play_region_id = value

    @property
    def stable_footing_flag(self):
        return self.__stable_footing_flag

    @stable_footing_flag.setter
    def stable_footing_flag(self, value):
        if self.__play_region_id != 0:
            raise InvalidFieldValueError("Cannot set 'stable_footing_flag' to a non-zero value while 'play_region_id' "
                                         "is non-zero.")
        if not isinstance(value, int) or value < 0:
            raise InvalidFieldValueError("'stable_footing_flag' must be an integer greater than or equal to 0.")
        self.__stable_footing_flag = value

    def pack_type_data(self):
        navmesh_groups = _enabled_flags_to_flag_group(self.navmesh_groups)

        if self.area_name_id == -1 and not self.__force_area_banner:
            raise InvalidFieldValueError("'force_area_banner' must be enabled if 'area_name_id' is -1 (default).")
        signed_area_name_id = self.area_name_id * (-1 if self.area_name_id >= 0 and self.__force_area_banner else 1)
        if self.__stable_footing_flag != 0:
            play_region_id = -self.__stable_footing_flag - 10
        else:
            play_region_id = self.__play_region_id
        return BinaryStruct(*self.PART_COLLISION_STRUCT).pack(
            hit_filter_id=self.hit_filter_id,
            sound_space_type=self.sound_space_type,
            env_light_map_spot_index=self.env_light_map_spot_index,
            reflect_plane_height=self.reflect_plane_height,
            navmesh_groups=navmesh_groups,
            vagrant_entity_ids=self.vagrant_entity_ids,
            area_name_id=signed_area_name_id,
            starts_disabled=self.starts_disabled,
            attached_bonfire=self.attached_bonfire,
            play_region_id=play_region_id,
            lock_cam_param_id_1=self.lock_cam_param_id_1,
            lock_cam_param_id_2=self.lock_cam_param_id_2,
        )


class MSBNavmesh(BaseMSBPart):
    """AI navigation mesh ('navmesh'). Often called 'navimesh' in the game files."""

    PART_NAVMESH_STRUCT = (
        ('navmesh_groups', '4I'),
        '16x',
    )

    FIELD_INFO = {
        'model_name': (
            'Model Name', True, '<Maps:Models:Navmeshes>',
            "Name of navmesh model to use for this navmesh."),
        **BaseMSBPart.FIELD_INFO,
        'navmesh_groups': (
            'Navmesh Groups', True, list,
            "Unknown."),
    }

    ENTRY_TYPE = MSB_PART_TYPE.Navmesh

    def __init__(self, msb_part_source):
        self.navmesh_groups = None
        super().__init__(msb_part_source)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_NAVMESH_STRUCT).unpack(msb_buffer)
        self.navmesh_groups = _flag_group_to_enabled_flags(data.navmesh_groups)

    def pack_type_data(self):
        return BinaryStruct(*self.PART_NAVMESH_STRUCT).pack(
            navmesh_groups=_enabled_flags_to_flag_group(self.navmesh_groups),
        )


class MSBUnusedObject(MSBObject):
    """Unused object. May be used in cutscenes; disabled otherwise. Identical structure to standard MSBObject."""
    ENTRY_TYPE = MSB_PART_TYPE.UnusedObject


class MSBUnusedCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to standard MSBCharacter."""
    ENTRY_TYPE = MSB_PART_TYPE.UnusedCharacter


class MSBMapConnection(BaseMSBPart):
    """Links to an MSBMapPiece entry and causes another map to load when the player stands on that collision."""

    PART_MAP_LOAD_TRIGGER_STRUCT = (
        ('collision_index', 'i'),
        ('map_id', '4b'),
        '8x',
    )

    FIELD_INFO = {
        'model_name': (
            'Collision Model Name', True, '<Maps:Models:Collisions>',
            "Name of collision model to use for this map load trigger."),
        **BaseMSBPart.FIELD_INFO,
        'collision_name': (
            'Collision Part Name', True, '<Maps:Parts:Collisions>',
            "Collision part that triggers this map load."),
        'map_id': (
            'Map ID', True, list,
            "Parts of map name this will trigger."),  # TODO: Combobox of maps.
    }

    ENTRY_TYPE = MSB_PART_TYPE.MapConnection

    def __init__(self, msb_part_source):
        self.collision_name = None
        self._collision_index = None
        self.map_id = None
        super().__init__(msb_part_source)

    def unpack_type_data(self, msb_buffer):
        data = BinaryStruct(*self.PART_MAP_LOAD_TRIGGER_STRUCT).unpack(msb_buffer)
        self.collision_name = None
        self._collision_index = data.collision_index
        self.map_id = data.map_id  # TODO: Convert to a GameMap instance.

    def pack_type_data(self):
        return BinaryStruct(*self.PART_MAP_LOAD_TRIGGER_STRUCT).pack(
            collision_index=self._collision_index,
            map_id=self.map_id,
        )

    def set_indices(self, part_type_index, model_indices, region_indices, part_indices, local_collision_indices):
        super().set_indices(part_type_index, model_indices, region_indices, part_indices, local_collision_indices)
        self._collision_index = local_collision_indices[self.collision_name] if self.collision_name else -1

    def set_names(self, model_names, region_names, part_names, collision_names):
        super().set_names(model_names, region_names, part_names, collision_names)
        self.collision_name = collision_names[self._collision_index] if self._collision_index != -1 else None


MSB_PART_TYPE_CLASSES = {
    MSB_PART_TYPE.MapPiece: MSBMapPiece,
    MSB_PART_TYPE.Object: MSBObject,
    MSB_PART_TYPE.Character: MSBCharacter,
    MSB_PART_TYPE.PlayerStarts: MSBPlayer,
    MSB_PART_TYPE.Collision: MSBCollision,
    MSB_PART_TYPE.Navmesh: MSBNavmesh,
    MSB_PART_TYPE.UnusedObject: MSBUnusedObject,
    MSB_PART_TYPE.UnusedCharacter: MSBUnusedCharacter,
    MSB_PART_TYPE.MapConnection: MSBMapConnection,
}


def _flag_group_to_enabled_flags(flag_group):
    """Get draw or display group 128-bit field <a, b, c, ...> where a, b, c, ... are the little-endian bit
    zero-based indices of the draw groups bit field (which is unpacked/packed internally as four 32-bit integers).

    So draw groups [01001..110, 0, 000...001, 100...000] would be {1, 4, 29, 30, 95, 96}.
    """
    enabled_flags = []
    for i in range(4):
        for j in range(32):
            if (2 ** j) & flag_group[i]:
                enabled_flags.append(32 * i + j)
    return enabled_flags


def _enabled_flags_to_flag_group(enabled_flags):
    """Opposite of above method. Converts list of flag indices to four-integer bit field array for packing."""
    flag_group = [0, 0, 0, 0]
    for flag in enabled_flags:
        if not isinstance(flag, int):
            raise ValueError(f"Non-integer value {flag} appeared in MSBPart.DrawGroups or MSBPart.DisplayGroups.")
        if not 0 <= flag <= 127:
            raise ValueError(f"Invalid DrawGroups or DisplayGroups index {flag} (must be between 0 and 127).")
        flag_group[flag // 32] += 2 ** (flag % 32)
    return flag_group
