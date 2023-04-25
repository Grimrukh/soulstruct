from __future__ import annotations

__all__ = [
    "MSBEvent",
    "MSBTreasureEvent",
    "MSBSpawnerEvent",
    "MSBObjActEvent",
    "MSBNavigationEvent",
    "MSBNPCInvasionEvent",
    "MSBPlatoonEvent",
    "MSBPatrolRouteEvent",
    "MSBMountEvent",
    "MSBSignPoolEvent",
    "MSBRetryPointEvent",
    "MSBOtherEvent",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.bloodborne.game_types import *
from soulstruct.base.maps.msb.events import BaseMSBEvent
from soulstruct.base.maps.msb import MSBEntry
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.utilities.binary import *

from .enums import MSBEventSubtype
from .regions import MSBRegion
from .parts import MSBPart

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBEvent"


@dataclass(slots=True, eq=False, repr=False)
class MSBEvent(BaseMSBEvent, abc.ABC):
    """MSB event entry in Bloodborne."""

    @dataclass(slots=True)
    class SUPERTYPE_HEADER_STRUCT(BinaryStruct):
        name_offset: long
        _supertype_index: int
        _subtype_int: int
        _subtype_index: int
        event_unkh_14: int = field(**Binary(asserted=(0, 1)))
        supertype_data_offset: long
        subtype_data_offset: long
        unk_data_offset: long

    @dataclass(slots=True)
    class SUPERTYPE_DATA_STRUCT(BinaryStruct):
        _attached_part_index: int
        _attached_region_index: int
        entity_id: int
        event_unkd_0c: byte
        _pad1: bytes = field(init=False, **BinaryPad(3))

    @dataclass(slots=True)
    class UNK_DATA_STRUCT(BinaryStruct):
        map_id: int
        unk_04: int
        unk_08: int
        unk_0c: int
        _pad1: bytes = field(init=False, **BinaryPad(16))

    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"

    # Field type overrides.
    attached_part: MSBPart = None
    attached_region: MSBRegion = None

    event_unkh_14: int = 0
    event_unkd_0c: int = 0

    map_id: int = 0
    unk_04: int = 0
    unk_08: int = 0
    unk_0c: int = 0

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        """Default minimal method. Most subclasses can just override one of the header/data unpack methods."""
        entry_offset = reader.position
        kwargs = cls.unpack_header(reader, entry_offset)

        reader.seek(entry_offset + kwargs.pop("supertype_data_offset"))
        kwargs |= cls.unpack_supertype_data(reader)

        relative_subtype_data_offset = kwargs.pop("subtype_data_offset")
        if relative_subtype_data_offset > 0:
            reader.seek(entry_offset + relative_subtype_data_offset)
            kwargs |= cls.unpack_subtype_data(reader)

        relative_unk_data_offset = kwargs.pop("unk_data_offset")
        reader.seek(entry_offset + relative_unk_data_offset)
        kwargs |= cls.UNK_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

        cls.SETATTR_CHECKS_DISABLED = True  # will be re-enabled in `__post_init__`
        msb_entry = cls(**kwargs)
        cls.SETATTR_CHECKS_DISABLED = False
        return msb_entry

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, list[MSBEntry]]
    ):
        """Default: pack header (with name), base data, and type data in that order."""
        entry_offset = writer.position
        try:
            self.pack_header(writer, entry_offset, supertype_index, subtype_index, entry_lists)
        except Exception:
            print(self.to_dict(ignore_defaults=False))
            raise
        writer.fill("supertype_data_offset", writer.position - entry_offset, obj=self)
        self.pack_supertype_data(writer, entry_offset, entry_lists)

        subtype_data_offset = writer.position - entry_offset if self.SUBTYPE_DATA_STRUCT is not None else 0
        writer.fill("subtype_data_offset", subtype_data_offset, obj=self)
        self.pack_subtype_data(writer, entry_lists)

        writer.fill("unk_data_offset", writer.position - entry_offset, obj=self)
        self.UNK_DATA_STRUCT.object_to_writer(self, writer)


@dataclass(slots=True, eq=False, repr=False)
class MSBTreasureEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Treasure
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "treasure_part"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(**BinaryPad(8))
        _treasure_part_index: int
        _pad2: bytes = field(**BinaryPad(4))
        item_lot: int
        _pad3: bytes = field(**BinaryPad(0x24, b"\xFF"))
        action_button_id: int
        pickup_animation_id: int
        is_in_chest: bool
        starts_disabled: bool
        _pad4: bytes = field(**BinaryPad(14))

    treasure_part: MSBPart = None
    item_lot: int = field(default=-1, **MapFieldInfo(game_type=ItemLotParam))
    action_button_id: int = 0
    pickup_animation_id: int = 0
    is_in_chest: bool = False
    starts_disabled: bool = False
    
    _treasure_part_index: int = None

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _treasure_part_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "treasure_part"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBTreasureEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "treasure_part")


@dataclass(slots=True, eq=False, repr=False)
class MSBSpawnerEvent(MSBEvent):
    """Attributes are identical to base event, except there are eight spawn region slots."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Spawner
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "spawn_parts", "spawn_regions"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        max_count: byte
        spawner_type: sbyte
        limit_count: short
        min_spawner_count: short
        max_spawner_count: short
        min_interval: float
        max_interval: float
        initial_spawn_count: byte
        _pad1: bytes = field(**BinaryPad(3))
        spawner_unk_14: float
        spawner_unk_18: float
        _pad2: bytes = field(**BinaryPad(0x14))
        _spawn_regions_indices: list[int] = field(**BinaryArray(8))
        _pad3: bytes = field(**BinaryPad(0x10))
        _spawn_parts_indices: list[int] = field(**BinaryArray(32))
        _pad4: bytes = field(**BinaryPad(0x20))

    max_count: int = 255
    spawner_type: int = 0
    limit_count: int = -1
    min_spawner_count: int = 1
    max_spawner_count: int = 1
    min_interval: float = 1.0
    max_interval: float = 1.0
    initial_spawn_count: int = 1
    spawner_unk_14: float = 0.0
    spawner_unk_18: float = 0.0
    spawn_parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 32, **MapFieldInfo(game_type=GameObjectIntSequence((Character, 32)))
    )
    spawn_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 8, **MapFieldInfo(GameObjectIntSequence((Region, 8)))
    )

    _spawn_parts_indices: list[int] = field(default=None, **BinaryArray(32))
    _spawn_regions_indices: list[int] = field(default=None, **BinaryArray(8))

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _spawn_parts_indices=self.try_index(entry_lists["PARTS_PARAM_ST"], "spawn_parts"),
            _spawn_regions_indices=self.try_index(entry_lists["POINT_PARAM_ST"], "spawn_regions"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBSpawnerEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "spawn_parts")
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "spawn_regions")


@dataclass(slots=True, eq=False, repr=False)
class MSBObjActEvent(MSBEvent):
    """Attributes are identical to base event, except the param ID is 32-bit rather than 16-bit."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.ObjAct
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "obj_act_part"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        obj_act_entity_id: int
        _obj_act_part_index: int
        obj_act_param_id: int
        obj_act_state: byte
        _pad1: bytes = field(**BinaryPad(3))
        obj_act_flag: int
        _pad2: bytes = field(**BinaryPad(12))

    obj_act_entity_id: int = -1
    obj_act_part: MSBPart = None
    obj_act_param_id: int = field(default=-1, **MapFieldInfo(game_type=ObjActParam))
    obj_act_state: int = 0
    obj_act_flag: int = field(default=0, **MapFieldInfo(game_type=Flag))

    _obj_act_part_index: int = None

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _obj_act_part_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "obj_act_part"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBObjActEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "obj_act_part")


@dataclass(slots=True, eq=False, repr=False)
class MSBNavigationEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Navigation
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "navigation_region"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _navigation_region_index: int
        _pad1: bytes = field(**BinaryPad(12))

    navigation_region: MSBRegion = None

    _navigation_region_index: int = None

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _navigation_region_index=self.try_index(entry_lists["POINT_PARAM_ST"], "navigation_region"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBNavigationEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "POINT_PARAM_ST", "navigation_region")


@dataclass(slots=True, eq=False, repr=False)
class MSBNPCInvasionEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.NPCInvasion

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        host_entity_id: int
        invasion_flag_id: int
        activate_goods_id: int
        npc_invasion_unk_0c: int
        npc_invasion_unk_10: int
        npc_invasion_unk_14: int
        npc_invasion_unk_18: int
        npc_invasion_unk_1c: int
        _minus_one: int = field(**Binary(asserted=-1))

    host_entity_id: int = -1
    invasion_flag_id: int = field(default=-1, **MapFieldInfo(game_type=Flag))
    activate_goods_id: int = -1  # TODO: Goods Param?
    npc_invasion_unk_0c: int = 0
    npc_invasion_unk_10: int = 0
    npc_invasion_unk_14: int = 0
    npc_invasion_unk_18: int = 0
    npc_invasion_unk_1c: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBPlatoonEvent(MSBEvent):
    """Defines a group (platoon) of enemies."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Platoon
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = [
        "attached_part", "attached_region", "platoon_parts"
    ]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        platoon_id_script_activate: int
        state: int
        _pad1: bytes = field(**BinaryPad(8))
        _platoon_parts_indices: list[int] = field(**BinaryArray(32))

    platoon_id_script_activate: int = -1
    state: int = -1
    platoon_parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 32, **MapFieldInfo(game_type=GameObjectIntSequence((MapPart, 32)))
    )

    _platoon_parts_indices: list[int] = field(default=None, **BinaryArray(32))

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _platoon_parts_indices=self.try_index(entry_lists["PARTS_PARAM_ST"], "platoon_parts"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBPlatoonEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "platoon_parts")


@dataclass(slots=True, eq=False, repr=False)
class MSBPatrolRouteEvent(MSBEvent):
    """Defines a patrol route through a sequence of up to 32 regions."""

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.PatrolRouteEvent
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "patrol_regions"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        patrol_type: byte
        _pad1: bytes = field(**BinaryPad(2))
        _one: byte = field(**Binary(asserted=1))
        _minus_one: int = field(**Binary(asserted=-1))
        _pad2: bytes = field(**BinaryPad(8))
        _patrol_regions_indices: list[short] = field(**BinaryArray(64))

    patrol_type: int = 0
    patrol_regions: list[MSBRegion] = field(
        default_factory=lambda: [None] * 64, **MapFieldInfo(game_type=GameObjectIntSequence((Region, 64)))
    )

    _patrol_regions_indices: list[int] = field(default=None, **BinaryArray(64))

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _patrol_regions_indices=self.try_index(entry_lists["POINT_PARAM_ST"], "patrol_regions"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBPatrolRouteEvent, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "POINT_PARAM_ST", "patrol_regions")


@dataclass(slots=True, eq=False, repr=False)
class MSBMountEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.Mount
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "rider_part", "mount_part"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _rider_part_index: int
        _mount_part_index: int

    rider_part: MSBPart = None
    mount_part: MSBPart = None

    _rider_part_index: int = None
    _mount_part_index: int = None

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _rider_part_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "rider_part"),
            _mount_part_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "mount_part"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBMountEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "rider_part")
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "mount_part")


@dataclass(slots=True, eq=False, repr=False)
class MSBSignPoolEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.SignPool
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "sign_part"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _sign_part_index: int
        sign_pool_unk_04: int
        _pad1: bytes = field(**BinaryPad(8))

    sign_part: MSBPart = None
    sign_pool_unk_04: int = 0

    _sign_part_index: int = None

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _sign_part_index=self.try_index(entry_lists["POINT_PARAM_ST"], "sign_part"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBSignPoolEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "sign_part")


@dataclass(slots=True, eq=False, repr=False)
class MSBRetryPointEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.RetryPoint
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["attached_part", "attached_region", "retry_part", "retry_region"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _retry_part_index: int
        event_flag_id: uint
        retry_point_unk_08: float
        _retry_region_index: short
        _zero: short = field(**Binary(asserted=0))

    retry_part: MSBPart = None
    event_flag_id: int = field(default=0, **MapFieldInfo(game_type=Flag))
    retry_point_unk_08: float = 0.0
    retry_region: MSBRegion = None

    _retry_part_index: int = None
    _retry_region_index: int = None

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _retry_part_index=self.try_index(entry_lists["POINT_PARAM_ST"], "retry_part"),
            _retry_region_index=self.try_index(entry_lists["POINT_PARAM_ST"], "retry_region"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBRetryPointEvent, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "retry_part")
        self._consume_index(entry_lists, "POINT_PARAM_ST", "retry_region")


@dataclass(slots=True, eq=False, repr=False)
class MSBOtherEvent(MSBEvent):

    SUBTYPE_ENUM: tp.ClassVar = MSBEventSubtype.OtherEvent

    SUBTYPE_DATA_STRUCT: tp.ClassVar = None
