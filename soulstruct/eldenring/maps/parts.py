from __future__ import annotations

__all__ = [
    "MSBPart",
    "MSBMapPiece",
    "MSBAsset",
    "MSBCharacter",
    "MSBPlayerStart",
    "MSBCollision",
    "MSBUnusedAsset",
    "MSBUnusedCharacter",
    "MSBMapConnection",
]

import abc
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.maps.msb import MSBEntry
from soulstruct.base.maps.msb.parts import *
from soulstruct.base.maps.msb.field_info import MapFieldInfo
from soulstruct.base.maps.msb.utils import GroupBitSet256, GroupBitSet1024
from soulstruct.eldenring.game_types import *
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3

from .enums import *
from .models import *

try:
    Self = tp.Self
except AttributeError:
    Self = "MSBPart"

if tp.TYPE_CHECKING:
    from .events import MSBPatrolRouteEvent


# Parts in Elden Ring separate their data into numerous structs, each of which can be present or absent for different
# subtypes. All of these substructs still have their data 'flattened' in each Part subtype, which leads to a lot of
# repetition in field definition, but it's the best solution until I implement some kind of 'nested' or 'pop-out' struct
# editor in the GUI (which probably wouldn't be super hard actually, but sort of annoying if you can't immediately see
# critical nested fields like draw groups).


@dataclass(slots=True)
class UnkStruct1(BinaryStruct):
    # TODO: Name 'DrawInfoData1'?
    display_groups: GroupBitSet256 = field(**BinaryArray(8, uint))
    draw_groups: GroupBitSet256 = field(**BinaryArray(8, uint))
    collision_mask: GroupBitSet1024 = field(**BinaryArray(32, uint))
    condition_1a: byte
    condition_1b: byte
    unk1_c2: byte
    unk1_c3: byte
    unk1_c4: short  # always -1 in retail, apparently
    unk1_c6: short  # always 0 or 1 in retail, apparently
    _pad1: bytes = field(init=False, **BinaryPad(0xC0))  # a lot of padding


@dataclass(slots=True)
class UnkStruct2(BinaryStruct):
    # TODO: Name 'DrawInfoData2'?
    condition_2: int
    display_groups_2: GroupBitSet256 = field(**BinaryArray(8, uint))
    unk2_24: short
    unk2_26: short
    _pad1: bytes = field(init=False, **BinaryPad(0x20))


@dataclass(slots=True)
class GparamStruct(BinaryStruct):
    light_set_id: int
    fog_id: int
    light_scattering_id: int
    environment_map_id: int
    _pad1: bytes = field(init=False, **BinaryPad(16))


@dataclass(slots=True)
class SceneGparamStruct(BinaryStruct):
    _pad1: bytes = field(init=False, **BinaryPad(16))
    transition_time: float
    _zero: int = field(init=False, **Binary(asserted=0))
    unk_sgp_18: sbyte
    unk_sgp_19: sbyte
    unk_sgp_1a: sbyte
    unk_sgp_1b: sbyte
    unk_sgp_1c: sbyte
    unk_sgp_1d: sbyte
    _pad2: bytes = field(init=False, **BinaryPad(2))
    unk_sgp_20: sbyte
    unk_sgp_21: sbyte
    _pad3: bytes = field(init=False, **BinaryPad(2))  # kept separate in case it's relevant?
    _pad4: bytes = field(init=False, **BinaryPad(0x44))


@dataclass(slots=True)
class UnkStruct7(BinaryStruct):
    unk7_00: int
    unk7_04: int
    unk7_08: int
    unk7_0C: int
    unk7_10: int
    unk7_14: int
    unk7_18: int
    _zero: int = field(init=False, **Binary(asserted=0))


@dataclass(slots=True)
class UnkStruct8(BinaryStruct):
    unk8_00: int = field(**Binary(asserted=(0, 1)))
    _pad1: bytes = field(init=False, **BinaryPad(28))


@dataclass(slots=True)
class UnkStruct9(BinaryStruct):
    unk9_00: int
    _pad1: bytes = field(init=False, **BinaryPad(28))


@dataclass(slots=True)
class UnkStruct10(BinaryStruct):
    map_id: int
    unk10_04: int
    _zero: int = field(init=False, **Binary(asserted=0))
    unk10_0c: int
    unk10_10: int = field(**Binary(asserted=(0, 1)))
    unk10_14: int
    _pad1: bytes = field(init=False, **BinaryPad(8))


@dataclass(slots=True)
class UnkStruct11(BinaryStruct):
    unk11_00: int
    unk11_04: int
    _pad1: bytes = field(init=False, **BinaryPad(24))


@dataclass(slots=True, eq=False, repr=False)
class MSBPart(BaseMSBPart, abc.ABC):

    NAME_ENCODING: tp.ClassVar[str] = "utf-16-le"
    GROUP_BIT_COUNT: tp.ClassVar[int] = 256
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:/GR/data/Model/map/{map_stem}/sib/layout.SIB"

    @dataclass(slots=True)
    class SUPERTYPE_HEADER_STRUCT(BinaryStruct):
        name_offset: long
        model_instance_id: int  # still functions as a unique instance ID for model, but starts at an offset like 9000
        _subtype_int: int
        _subtype_index: int
        model_index: int
        sib_path_offset: long
        translate: Vector3
        rotate: Vector3
        scale: Vector3
        part_unkh_44: int
        event_layer: int
        _zero: int = field(init=False, **Binary(asserted=0))
        unk1_data_offset: long
        unk2_data_offset: long
        supertype_data_offset: long
        subtype_data_offset: long
        gparam_data_offset: long
        scene_gparam_data_offset: long
        unk7_data_offset: long
        unk8_data_offset: long
        unk9_data_offset: long
        unk10_data_offset: long
        unk11_data_offset: long
        _pad1: bytes = field(init=False, **BinaryPad(24))  # three unused offsets?

    @dataclass(slots=True)
    class SUPERTYPE_DATA_STRUCT(BinaryStruct):
        entity_id: uint
        part_unkd_04: byte
        _pad1: bytes = field(**BinaryPad(3))  # includes former 'Lantern ID'
        lod_id: sbyte
        part_unkd_09: byte
        is_point_light_shadow_source: sbyte  # TODO: always 0 or -1?
        part_unkd_0b: byte
        is_shadow_source: bool
        is_static_shadow_source: byte  # TODO: bool?
        is_cascade3_shadow_source: byte  # TODO: bool?
        part_unkd_0f: byte
        part_unkd_10: byte
        is_shadow_destination: bool
        is_shadow_only: bool  # TODO: always 0?
        draw_by_reflect_cam: bool
        draw_only_reflect_cam: bool
        enable_on_above_shadow: byte
        disable_point_light_effect: bool
        part_unkd_17: byte
        part_unkd_18: int
        entity_group_ids: list[int] = field(**BinaryArray(8, uint))
        part_unkd_3c: short
        part_unkd_3e: short

    # Entity ID default override.
    entity_id: int = 0

    # Set by each concrete subclass.
    HAS_UNK1_STRUCT: tp.ClassVar[bool]
    HAS_UNK2_STRUCT: tp.ClassVar[bool]
    HAS_GPARAM_STRUCT: tp.ClassVar[bool]
    HAS_SCENE_GPARAM_STRUCT: tp.ClassVar[bool]
    HAS_UNK7_STRUCT: tp.ClassVar[bool]
    HAS_UNK8_STRUCT: tp.ClassVar[bool]
    HAS_UNK9_STRUCT: tp.ClassVar[bool]
    HAS_UNK10_STRUCT: tp.ClassVar[bool]
    HAS_UNK11_STRUCT: tp.ClassVar[bool]

    # NOTE: `model` defined by subclasses.

    # HEADER
    # TODO: Four-digit combination of two-digit 'layout ID' (from SIB path) and two-digit model instance index.
    #  SIB path is empty if first two digits here are 90 (e.g. all characters, some assets).
    #  Hopefully doesn't actually do anything (I've left it as zero in prior games).
    #  Also, -1 for collisions AFAIK, unless some models are used multiple times.
    model_instance_id: int = 0
    part_unkh_44: int = 0  # seems to be 3 for most Characters and some Assets
    event_layer: int = -1  # probably only used for Ashen Leyndell

    # PART DATA
    part_unkd_04: int = 0
    lod_id: int = 0  # TODO: probably zero for everything except Map Pieces (which do use it)
    part_unkd_09: int = 0  # TODO: seems to be 7/8/9 for Map Pieces (tied to lod_id) and zero otherwise
    is_point_light_shadow_source: int = 0
    part_unkd_0b: int = 0
    is_shadow_source: bool = False  # TODO: only seems to be enabled for some Map Pieces in Stormveil
    is_static_shadow_source: int = 0  # TODO: bool? defaults? seems to be 1 for some Map Pieces in Stormveil at least
    is_cascade3_shadow_source: int = 0  # TODO: bool? defaults? haven't found any non-zero yet
    part_unkd_0f: int = 1
    part_unkd_10: int = 0
    is_shadow_destination: bool = True
    is_shadow_only: bool = False
    draw_by_reflect_cam: bool = False  # seems be False far more often than True (may differ in maps with more water)
    draw_only_reflect_cam: bool = False
    enable_on_above_shadow: int = 0  # TODO: bool? defaults?
    disable_point_light_effect: bool = False
    part_unkd_17: int = 0
    part_unkd_18: int = 0
    entity_group_ids: list[int] = field(default_factory=lambda: [0] * 8)
    part_unkd_3c: int = -1
    part_unkd_3e: int = 0

    @classmethod
    def from_msb_reader(cls, reader: BinaryReader) -> Self:
        entry_offset = reader.position

        kwargs = cls.unpack_header(reader, entry_offset)

        reader.seek(entry_offset + kwargs.pop("supertype_data_offset"))
        kwargs |= cls.SUPERTYPE_DATA_STRUCT.from_bytes(reader).to_dict()

        # Every Part has subtype data.
        reader.seek(entry_offset + kwargs.pop("subtype_data_offset"))
        kwargs |= cls.unpack_subtype_data(reader)

        # NOTE: Unknown structs 1 and 2 come before Gparam/SceneGparam, but easier to loop
        # over them all below.

        relative_gparam_data_offset = kwargs.pop("gparam_data_offset")
        if cls.HAS_GPARAM_STRUCT:
            if relative_gparam_data_offset == 0:
                raise ValueError(f"Found invalid zero Gparam offset in `{cls.__name__}` '{kwargs['name']}.")
            reader.seek(entry_offset + relative_gparam_data_offset)
            kwargs |= GparamStruct.from_bytes(reader).to_dict()
        elif relative_gparam_data_offset != 0:
            raise ValueError(
                f"Found non-zero Gparam offset in `{cls.__name__}` '{kwargs['name']}' "
                f"but class does not have a GparamStruct."
            )

        relative_scene_gparam_data_offset = kwargs.pop("scene_gparam_data_offset")
        if cls.HAS_SCENE_GPARAM_STRUCT:
            if relative_scene_gparam_data_offset == 0:
                raise ValueError(f"Found invalid zero SceneGparam offset in `{cls.__name__}` '{kwargs['name']}.")
            reader.seek(entry_offset + relative_scene_gparam_data_offset)
            kwargs |= SceneGparamStruct.from_bytes(reader).to_dict()
        elif relative_scene_gparam_data_offset != 0:
            raise ValueError(
                f"Found non-zero SceneGparam offset in `{cls.__name__}` '{kwargs['name']}' "
                f"but class does not have a SceneGparamStruct."
            )

        for i, unk_struct_class in zip(
            (1, 2, 7, 8, 9, 10, 11),
            (UnkStruct1, UnkStruct2, UnkStruct7, UnkStruct8, UnkStruct9, UnkStruct10, UnkStruct11),
        ):
            relative_unk_data_offset = kwargs.pop(f"unk{i}_data_offset")
            if getattr(cls, f"HAS_UNK{i}_STRUCT"):
                if relative_unk_data_offset == 0:
                    raise ValueError(f"Found invalid zero UnkStruct{i} offset in `{cls.__name__}` '{kwargs['name']}.")
                reader.seek(entry_offset + relative_unk_data_offset)
                kwargs |= unk_struct_class.from_bytes(reader).to_dict()
            elif relative_unk_data_offset != 0:
                raise ValueError(
                    f"Found non-zero UnkStruct{i} offset in `{cls.__name__}` '{kwargs['name']}. It should be zero."
                )

        cls.SETATTR_CHECKS_DISABLED = True
        part = cls(**kwargs)
        cls.SETATTR_CHECKS_DISABLED = False
        return part

    @classmethod
    def unpack_header(cls, reader: BinaryReader, entry_offset: int) -> dict[str, tp.Any]:
        header = cls.SUPERTYPE_HEADER_STRUCT.from_bytes(reader)
        header_subtype_int = header.pop("_subtype_int")
        if header_subtype_int != cls.SUBTYPE_ENUM.value:
            raise ValueError(f"Unexpected MSB part subtype index for `{cls.__name__}`: {header_subtype_int}")

        name = reader.unpack_string(offset=entry_offset + header.pop("name_offset"), encoding=cls.NAME_ENCODING)
        # No description.
        sib_path = reader.unpack_string(offset=entry_offset + header.pop("sib_path_offset"), encoding=cls.NAME_ENCODING)
        kwargs = dict(
            name=name,
            sib_path=sib_path,
            _model_index=header.pop("model_index"),
        )
        return header.to_dict(ignore_underscore_prefix=True) | kwargs

    def to_msb_writer(
        self, writer: BinaryWriter, supertype_index: int, subtype_index: int, entry_lists: dict[str, list[MSBEntry]]
    ):
        """Default: pack header (with name), base data, and type data in that order."""
        entry_offset = writer.position

        self.pack_header(writer, entry_offset, supertype_index, subtype_index, entry_lists)

        # Pack structs in correct order: 1, 2, supertype_data, subtype_data, gparam, scene_gparam, 7, 8, 9, 10, 11

        unk1_data_offset = writer.position - entry_offset if self.HAS_UNK1_STRUCT else 0
        writer.fill("unk1_data_offset", unk1_data_offset, obj=self)
        if self.HAS_UNK1_STRUCT:
            UnkStruct1.object_to_writer(self, writer)

        unk2_data_offset = writer.position - entry_offset if self.HAS_UNK2_STRUCT else 0
        writer.fill("unk2_data_offset", unk2_data_offset, obj=self)
        if self.HAS_UNK2_STRUCT:
            UnkStruct2.object_to_writer(self, writer)

        supertype_data_offset = writer.position - entry_offset if self.SUPERTYPE_DATA_STRUCT is not None else 0
        writer.fill("supertype_data_offset", supertype_data_offset, obj=self)
        self.pack_supertype_data(writer, entry_offset, entry_lists)

        subtype_data_offset = writer.position - entry_offset if self.SUBTYPE_DATA_STRUCT is not None else 0
        writer.fill("subtype_data_offset", subtype_data_offset, obj=self)
        self.pack_subtype_data(writer, entry_lists)

        gparam_data_offset = writer.position - entry_offset if self.HAS_GPARAM_STRUCT is not None else 0
        writer.fill("gparam_data_offset", gparam_data_offset, obj=self)
        if self.HAS_GPARAM_STRUCT:
            GparamStruct.object_to_writer(self, writer)

        scene_gparam_data_offset = writer.position - entry_offset if self.HAS_SCENE_GPARAM_STRUCT is not None else 0
        writer.fill("scene_gparam_data_offset", scene_gparam_data_offset, obj=self)
        if self.HAS_SCENE_GPARAM_STRUCT:
            SceneGparamStruct.object_to_writer(self, writer)

        # Unknown structs 7 to 11 handled by loop:
        for i, unk_struct_class in zip(
            (7, 8, 9, 10, 11),
            (UnkStruct7, UnkStruct8, UnkStruct9, UnkStruct10, UnkStruct11),
        ):
            if getattr(self, f"HAS_UNK{i}_STRUCT"):
                writer.fill(f"unk{i}_data_offset", writer.position - entry_offset, obj=self)
                unk_struct_class.object_to_writer(self, writer)
            else:
                writer.fill(f"unk{i}_data_offset", 0, obj=self)

    def pack_header(
        self,
        writer: BinaryWriter,
        entry_offset: int,
        supertype_index: int,
        subtype_index: int,
        entry_lists: [dict[str, list[MSBEntry]]],
    ):
        self.SUPERTYPE_HEADER_STRUCT.object_to_writer(
            self,
            writer,
            description_offset=RESERVED,  # NOTE: Only Parts have descriptions.
            name_offset=RESERVED,
            _instance_index=0,  # TODO: Need to pass in...
            _subtype_int=self.SUBTYPE_ENUM.value,
            _subtype_index=subtype_index,
            model_index=self.try_index(entry_lists["MODEL_PARAM_ST"], "model"),
            sib_path_offset=RESERVED,
            supertype_data_offset=RESERVED,
            subtype_data_offset=RESERVED,
            gparam_data_offset=RESERVED,
            scene_gparam_data_offset=RESERVED,
        )
        writer.fill("description_offset", writer.position - entry_offset, obj=self)
        packed_description = self.description.encode(self.NAME_ENCODING) + b"\0\0"
        writer.append(packed_description)
        writer.fill("name_offset", writer.position - entry_offset, obj=self)
        packed_name = self.name.encode(self.NAME_ENCODING) + b"\0\0"
        writer.append(packed_name)
        writer.fill("sib_path_offset", writer.position - entry_offset, obj=self)
        packed_sib_path = (self.sib_path.encode(self.NAME_ENCODING) + b"\0\0") if self.sib_path else b"\0\0"
        strings_size = len(packed_description + packed_name + packed_sib_path)
        if strings_size <= 0x38:
            packed_sib_path += b"\0" * (0x3c - strings_size)
        else:
            packed_sib_path += b"\0" * 8
        while len(packed_description + packed_name + packed_sib_path) % 4 != 0:
            packed_sib_path += b"\0"  # Not done in SoulsFormats, but makes sense to me.
        writer.append(packed_sib_path)


@dataclass(slots=True, eq=False, repr=False)
class MSBMapPiece(MSBPart):
    """No further subtype data beyond the structs."""
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.MapPiece

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(**BinaryPad(8))

    HAS_UNK1_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK2_STRUCT: tp.ClassVar[bool] = False
    HAS_GPARAM_STRUCT: tp.ClassVar[bool] = True
    HAS_SCENE_GPARAM_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK7_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK8_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK9_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK10_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK11_STRUCT: tp.ClassVar[bool] = True

    model: MSBMapPieceModel = None

    # UNK STRUCT 1
    display_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    draw_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_on)
    collision_mask: GroupBitSet1024 = field(default_factory=GroupBitSet1024.all_off)
    condition_1a: int = 0
    condition_1b: int = 0
    unk1_c2: int = 0
    unk1_c3: int = 0
    unk1_c4: int = -1
    unk1_c6: int = 0

    # GPARAM
    light_set_id: int = field(default=-1, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=-1, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))

    # UNK STRUCT 7
    unk7_00: int = 0
    unk7_04: int = 0
    unk7_08: int = 0
    unk7_0C: int = 0
    unk7_10: int = 0
    unk7_14: int = 0
    unk7_18: int = -1

    # UNK STRUCT 8
    unk8_00: int = 0

    # UNK STRUCT 9
    unk9_00: int = 0

    # UNK STRUCT 10
    map_id: int = -1
    unk10_04: int = 0
    unk10_0c: int = -1
    unk10_10: int = 0  # always 0 or 1
    unk10_14: int = -1

    # UNK STRUCT 11
    unk11_00: int = 0
    unk11_04: int = 0


# Extra nested structs for Assets below.

@dataclass(slots=True)
class AssetUnkStruct1(BinaryStruct):
    asset_unk1_00: short
    _minus_one: short = field(init=False, **Binary(asserted=-1))
    asset_unk1_04: bool
    disable_torrent_asset_only: bool
    _minus_one2: short = field(init=False, **Binary(asserted=-1))
    _pad: list[int] = field(init=False, **BinaryArray(5, asserted=[0, 0, -1, -1, -1]))
    asset_unk1_1c: int
    _zero: int = field(init=False, **Binary(asserted=0))
    asset_unk1_24: short
    asset_unk1_26: short
    asset_unk1_28: int
    asset_unk1_2c: int
    _pad2: bytes = field(init=False, **BinaryPad(16))


@dataclass(slots=True)
class AssetUnkStruct2(BinaryStruct):
    asset_unk2_00: int
    asset_unk2_04: int
    _pad1: list[int] = field(init=False, **BinaryArray(3, asserted=[-1, 0, 0]))
    asset_unk2_14: float
    _zero: int = field(init=False, **Binary(asserted=0))
    asset_unk2_1c: byte
    asset_unk2_1d: byte
    asset_unk2_1e: byte
    asset_unk2_1f: byte
    _pad2: bytes = field(init=False, **BinaryPad(32))


@dataclass(slots=True)
class AssetUnkStruct3(BinaryStruct):
    asset_unk3_00: int
    asset_unk3_04: float
    _minus_one: sbyte = field(init=False, **Binary(asserted=-1))
    asset_unk3_09: byte
    asset_unk3_0a: byte
    asset_unk3_0b: byte
    asset_unk3_0c: short
    asset_unk3_0e: short
    asset_unk3_10: float
    disable_when_map_loaded_map_id: list[byte] = field(**BinaryArray(4))
    asset_unk3_18: int
    asset_unk3_1c: int
    asset_unk3_20: int
    asset_unk3_24: byte
    asset_unk3_25: bool
    _pad1: bytes = field(init=False, **BinaryPad(26))


@dataclass(slots=True)
class AssetUnkStruct4(BinaryStruct):
    asset_unk4_00: bool
    asset_unk4_01: byte
    asset_unk4_02: byte
    asset_unk4_03: bool
    _pad1: bytes = field(init=False, **BinaryPad(60))


@dataclass(slots=True, eq=False, repr=False)
class MSBAsset(MSBPart):
    """Interactable asset (replacing object). Used even for big static terrain features, like buildings."""
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Asset
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "unk_parts"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _zero: short = field(init=False, **Binary(asserted=0))
        asset_unk_02: short = field(**Binary(asserted=(0, 1)))
        _pad1: bytes = field(init=False, **BinaryPad(12))
        asset_unk_10: byte
        asset_unk_11: bool
        asset_unk_12: byte
        _pad2: bytes = field(init=False, **BinaryPad(9))
        asset_sfx_param_relative_id: short
        asset_unk_1e: short
        _minus_one: int = field(init=False, **Binary(asserted=-1))
        asset_unk_24: int
        asset_unk_28: int
        _zero2: int = field(init=False, **Binary(asserted=0))
        asset_unk_30: int
        asset_unk_34: int
        _unk_parts_indices: list[int] = field(**BinaryArray(6))
        asset_unk_50: bool
        asset_unk_51: byte
        _zero3: byte = field(init=False, **Binary(asserted=0))
        asset_unk_53: byte
        asset_unk_54: int
        asset_unk_58: int
        asset_unk_5c: int
        asset_unk_60: int
        asset_unk_64: int
        # These four Asset sub-struct offsets are always the same.
        _asset_unk1_offset: long = field(init=False, **Binary(asserted=0x88))
        _asset_unk2_offset: long = field(init=False, **Binary(asserted=0xC8))
        _asset_unk3_offset: long = field(init=False, **Binary(asserted=0x108))
        _asset_unk4_offset: long = field(init=False, **Binary(asserted=0x148))

    # Assets use every struct except SceneGParam.
    HAS_UNK1_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK2_STRUCT: tp.ClassVar[bool] = True
    HAS_GPARAM_STRUCT: tp.ClassVar[bool] = True
    HAS_SCENE_GPARAM_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK7_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK8_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK9_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK10_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK11_STRUCT: tp.ClassVar[bool] = True

    model: MSBAssetModel = None

    # ASSET DATA
    asset_unk_02: int = 0
    asset_unk_10: int = 0
    asset_unk_11: bool = False
    asset_unk_12: int = 255
    asset_sfx_param_relative_id: int = -1
    asset_unk_1e: int = -1
    asset_unk_24: int = -1
    asset_unk_28: int = 0
    asset_unk_30: int = -1
    asset_unk_34: int = -1
    unk_parts: list[MSBPart] = field(
        default_factory=lambda: [None] * 6, **MapFieldInfo(game_type=GameObjectIntSequence((MapPart, 6)))
    )
    asset_unk_50: bool = False
    asset_unk_51: int = 0
    asset_unk_53: int = 0
    asset_unk_54: int = -1
    asset_unk_58: int = -1
    asset_unk_5c: int = -1
    asset_unk_60: int = -1
    asset_unk_64: int = -1

    _unk_parts_indices: list[int] = field(default=None, **BinaryArray(6))

    # UNK STRUCT 1
    display_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    draw_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_on)
    collision_mask: GroupBitSet1024 = field(default_factory=GroupBitSet1024.all_off)
    condition_1a: int = 0
    condition_1b: int = 0
    unk1_c2: int = 0
    unk1_c3: int = 0
    unk1_c4: int = -1
    unk1_c6: int = 0

    # UNK STRUCT 2
    condition_2: int = -1
    display_groups_2: GroupBitSet256 = field(default_factory=GroupBitSet256.all_on)
    unk2_24: int = 0
    unk2_26: int = -1

    # GPARAM
    light_set_id: int = field(default=-1, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=-1, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))

    # UNK STRUCT 7
    unk7_00: int = 0
    unk7_04: int = 0
    unk7_08: int = 0
    unk7_0C: int = 0
    unk7_10: int = 0
    unk7_14: int = 0
    unk7_18: int = -1

    # UNK STRUCT 8
    unk8_00: int = 0

    # UNK STRUCT 9
    unk9_00: int = 0

    # UNK STRUCT 10
    map_id: int = -1
    unk10_04: int = 0
    unk10_0c: int = -1
    unk10_10: int = 0  # always 0 or 1
    unk10_14: int = -1

    # UNK STRUCT 11
    unk11_00: int = 0
    unk11_04: int = 0

    # ASSET UNK STRUCT 1
    asset_unk1_00: int = 0
    asset_unk1_04: bool = False
    # Disables ability to summon/ride Torrent, but only when asset isn't referencing a collision with `disable_torrent`.
    disable_torrent_asset_only: bool = False
    asset_unk1_1c: int = -1
    asset_unk1_24: int = -1
    asset_unk1_26: int = -1
    asset_unk1_28: int = -1
    asset_unk1_2c: int = -1

    # ASSET UNK STRUCT 2
    asset_unk2_00: int = 0
    asset_unk2_04: int = -1
    asset_unk2_14: float = -1.0
    asset_unk2_1c: int = 255
    asset_unk2_1d: int = 255
    asset_unk2_1e: int = 255
    asset_unk2_1f: int = 255

    # ASSET UNK STRUCT 3
    asset_unk3_00: int = 0
    asset_unk3_04: float = 0.0
    asset_unk3_09: int = 255
    asset_unk3_0a: int = 0
    asset_unk3_0b: int = 255
    asset_unk3_0c: int = -1
    asset_unk3_0e: int = 0
    asset_unk3_10: float = -1.0
    disable_when_map_loaded_map_id: list[int] = field(default_factory=lambda: [255, 255, 255, 255])
    asset_unk3_18: int = -1
    asset_unk3_1c: int = -1
    asset_unk3_20: int = -1
    asset_unk3_24: int = 255
    asset_unk3_25: bool = False

    # ASSET UNK STRUCT 4
    asset_unk4_00: bool = False
    asset_unk4_01: int = 255
    asset_unk4_02: int = 255
    asset_unk4_03: bool = False

    @classmethod
    def unpack_subtype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        """Reads extra four Asset sub-structs, which are just stacked after the main subtype data."""
        kwargs = cls.SUBTYPE_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)

        kwargs |= AssetUnkStruct1.from_bytes(reader).to_dict(ignore_underscore_prefix=True)
        kwargs |= AssetUnkStruct2.from_bytes(reader).to_dict(ignore_underscore_prefix=True)
        kwargs |= AssetUnkStruct3.from_bytes(reader).to_dict(ignore_underscore_prefix=True)
        kwargs |= AssetUnkStruct4.from_bytes(reader).to_dict(ignore_underscore_prefix=True)
        return kwargs

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBAsset, self).indices_to_objects(entry_lists)
        self._consume_indices(entry_lists, "PARTS_PARAM_ST", "unk_parts")

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _unk_parts_indices=self.try_index(entry_lists["PARTS_PARAM_ST"], "unk_parts"),
        )


@dataclass(slots=True, eq=False, repr=False)
class MSBCharacter(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Character
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "draw_parent", "patrol_route_event"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad1: bytes = field(init=False, **BinaryPad(8))
        ai_id: int
        character_id: int
        talk_id: int
        _zero: byte = field(init=False, **Binary(asserted=0))
        char_unk_15: bool
        platoon_id: short
        player_id: int
        _draw_parent_index: int
        _patrol_route_event_index: short  # NOTE: local event subtype index!
        _zero2: short = field(init=False, **Binary(asserted=0))
        char_unk_24: int
        char_unk_28: int
        char_activate_condition_param_id: int
        _zero3: int = field(init=False, **Binary(asserted=0))
        char_unk_34: int
        backup_event_animation_id: int
        char_unk_3c: int
        special_effect_set_param_id: list[int] = field(**BinaryArray(4))
        _pad2: bytes = field(init=False, **BinaryPad(40))
        _const_long: long = field(init=False, **Binary(asserted=0x80))
        _zero4: int = field(init=False, **Binary(asserted=0))
        char_unk_84: float
        _pad3a: list[short] = field(init=False, **BinaryArray(4, asserted=[-1, -1, -1, 0xa]))
        _pad3b: list[short] = field(init=False, **BinaryArray(4, asserted=[-1, -1, -1, 0xa]))
        _pad3c: list[short] = field(init=False, **BinaryArray(4, asserted=[-1, -1, -1, 0xa]))
        _pad3d: list[short] = field(init=False, **BinaryArray(4, asserted=[-1, -1, -1, 0xa]))
        _pad3e: list[short] = field(init=False, **BinaryArray(4, asserted=[-1, -1, -1, 0xa]))
        _pad4: bytes = field(init=False, **BinaryPad(0x10))

    HAS_UNK1_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK2_STRUCT: tp.ClassVar[bool] = False
    HAS_GPARAM_STRUCT: tp.ClassVar[bool] = True
    HAS_SCENE_GPARAM_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK7_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK8_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK9_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK10_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK11_STRUCT: tp.ClassVar[bool] = False

    model: MSBCharacterModel | MSBPlayerModel = None  # c0000 characters can use either model type

    # CHARACTER DATA
    ai_id: int = 0
    character_id: int = 0
    talk_id: int = 0
    char_unk_15: int = 0
    platoon_id: int = 0
    player_id: int = 0
    draw_parent: MSBPart = None
    patrol_route_event: MSBPatrolRouteEvent = None  # NOTE: imported under TYPE_CHECKING to avoid circular import
    char_unk_24: int = -1
    char_unk_28: int = 0
    char_activate_condition_param_id: int = 0
    char_unk_34: int = 0
    backup_event_animation_id: int = -1  # animation ID for character to 'backpedal', I believe  TODO: rename, vague
    char_unk_3c: int = 0
    special_effect_set_param_id: list[int] = field(default_factory=lambda: [0] * 4)  # TODO: SpEffectParam?
    char_unk_84: float = 1.0

    _draw_parent_index: int = None
    _patrol_route_event_index: int = None  # NOTE: local event subtype index!

    # UNK STRUCT 1
    display_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    draw_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_on)
    collision_mask: GroupBitSet1024 = field(default_factory=GroupBitSet1024.all_off)
    condition_1a: int = 0
    condition_1b: int = 0
    unk1_c2: int = 0
    unk1_c3: int = 0
    unk1_c4: int = -1
    unk1_c6: int = 0

    # GPARAM
    light_set_id: int = field(default=-1, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=-1, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))

    # UNK STRUCT 8
    unk8_00: int = 0

    # UNK STRUCT 10
    map_id: int = -1
    unk10_04: int = 0
    unk10_0c: int = -1
    unk10_10: int = 0  # always 0 or 1
    unk10_14: int = -1

    HIDE_FIELDS: tp.ClassVar = (
        "scale",
        "display_groups",
    )

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _draw_parent_index=self.try_index(entry_lists["PARTS_PARAM_ST"], "draw_parent"),
            _patrol_route_event_index=self.try_index(entry_lists["patrol_route_events"], "patrol_route_event"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBCharacter, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "PARTS_PARAM_ST", "draw_parent")
        self._consume_index(entry_lists, "patrol_route_events", "patrol_route_event")


@dataclass(slots=True, eq=False, repr=False)
class MSBPlayerStart(MSBPart):

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.PlayerStart

    HAS_UNK1_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK2_STRUCT: tp.ClassVar[bool] = False
    HAS_GPARAM_STRUCT: tp.ClassVar[bool] = False
    HAS_SCENE_GPARAM_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK7_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK8_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK9_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK10_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK11_STRUCT: tp.ClassVar[bool] = False

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        player_start_unk_00: int
        _pad1: bytes = field(init=False, **BinaryPad(0x0C))

    HIDE_FIELDS: tp.ClassVar = (
        "scale",
        "draw_groups",
        "display_groups",
    )

    model: MSBCharacterModel | MSBPlayerModel = None

    player_start_unk_00: int = 0

    # UNK STRUCT 1
    display_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    draw_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_on)
    collision_mask: GroupBitSet1024 = field(default_factory=GroupBitSet1024.all_off)
    condition_1a: int = 0
    condition_1b: int = 0
    unk1_c2: int = 0
    unk1_c3: int = 0
    unk1_c4: int = -1
    unk1_c6: int = 0

    # UNK STRUCT 8
    unk8_00: int = 0

    # UNK STRUCT 10
    map_id: int = -1
    unk10_04: int = 0
    unk10_0c: int = -1
    unk10_10: int = 0  # always 0 or 1
    unk10_14: int = -1


@dataclass(slots=True, eq=False, repr=False)
class MSBCollision(MSBPart):
    """Collision meshes of various functionality, not just for standing on.

    In Elden Ring, assets are used for many parts of the world instead of these meshes. But ground in the Lands Between
    is still mostly collisions.
    """

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.Collision
    SIB_PATH_TEMPLATE: tp.ClassVar[str] = "N:/GR/data/Model/map/{map_stem}/sib/h_layout.SIB"
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model"]

    HAS_UNK1_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK2_STRUCT: tp.ClassVar[bool] = True
    HAS_GPARAM_STRUCT: tp.ClassVar[bool] = True
    HAS_SCENE_GPARAM_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK7_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK8_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK9_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK10_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK11_STRUCT: tp.ClassVar[bool] = True

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        hit_filter_id: byte
        col_unk_01: byte
        col_unk_02: byte
        col_unk_03: byte
        col_unk_04: float
        _pad1: bytes = field(init=False, **BinaryPad(12))
        col_unk_14: float
        col_unk_18: int
        col_unk_1c: int
        play_region_id: int
        col_unk_24: short
        col_unk_26: short = field(**Binary(asserted=(0, 1)))
        _zero: int = field(init=False, **Binary(asserted=0))
        _minus_one: int = field(init=False, **Binary(asserted=-1))
        col_unk_30: int
        col_unk_34: byte
        col_unk_35: byte
        disable_torrent: bool
        _zero2: byte = field(init=False, **Binary(asserted=0))
        _minus_one2: int = field(init=False, **Binary(asserted=-1))
        col_unk_3c: short
        col_unk_3e: short
        col_unk_40: float
        _zero3: int = field(init=False, **Binary(asserted=0))
        enable_fast_travel_flag_id: uint
        col_unk_4c: short = field(**Binary(asserted=(0, 1)))
        col_unk_4e: short

    # Field type overrides.
    model: MSBCollisionModel = None

    # COLLISION DATA
    hit_filter_id: int = field(default=CollisionHitFilter.Normal.value, **MapFieldInfo(game_type=CollisionHitFilter))
    col_unk_01: int = 255
    col_unk_02: int = 255
    col_unk_03: int = 0
    col_unk_04: float = 0.0
    col_unk_14: float = -1.0
    col_unk_18: int = -10000
    col_unk_1c: int = -1
    play_region_id: int = 0
    col_unk_24: int = -1
    col_unk_26: int = 0
    col_unk_30: int = 0
    col_unk_34: int = 0  # have seen 1 or 2
    col_unk_35: int = 255
    disable_torrent: bool = False
    col_unk_3c: int = -1
    col_unk_3e: int = -1
    col_unk_40: float = 0.0
    enable_fast_travel_flag_id: int = field(default=0, **MapFieldInfo(game_type=Flag))
    col_unk_4c: int = 0
    col_unk_4e: int = -1

    # UNK STRUCT 1
    display_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    draw_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    collision_mask: GroupBitSet1024 = field(default_factory=GroupBitSet1024.all_off)
    condition_1a: int = 0
    condition_1b: int = 0
    unk1_c2: int = 0
    unk1_c3: int = 0
    unk1_c4: int = -1
    unk1_c6: int = 0

    # UNK STRUCT 2
    condition_2: int = -1
    display_groups_2: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    unk2_24: int = 0
    unk2_26: int = -1

    # GPARAM
    light_set_id: int = field(default=-1, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=-1, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))

    # SCENE GPARAM
    transition_time: float = -1.0
    unk_sgp_18: int = -1
    unk_sgp_19: int = -1
    unk_sgp_1a: int = -1
    unk_sgp_1b: int = -1
    unk_sgp_1c: int = -1
    unk_sgp_1d: int = -1
    unk_sgp_20: int = -1
    unk_sgp_21: int = -1

    # UNK STRUCT 8
    unk8_00: int = 0

    # UNK STRUCT 10
    map_id: int = -1
    unk10_04: int = 0
    unk10_0c: int = -1
    unk10_10: int = 0  # always 0 or 1
    unk10_14: int = -1

    # UNK STRUCT 11
    unk11_00: int = 0
    unk11_04: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBMapConnection(MSBPart):
    """Links to an `MSBCollision` entry and causes another specified map to load into backread when the linked collision
    is itself in backread in the current map.

    Note that sensible draw, display, and navmesh groups are still needed to advance the backread state of the
    connected map's collisions to an interactive state (while map pieces don't care about navmesh groups).

    Uses collision models, and almost always has the same model as the linked `MSBCollision`.
    """
    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.MapConnection
    MSB_ENTRY_REFERENCES: tp.ClassVar[list[str]] = ["model", "collision"]

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _collision_index: int
        connected_map_id: list[sbyte] = field(**BinaryArray(4))
        con_unk_x08: byte
        con_unk_x09: bool
        con_unk_x0a: byte
        con_unk_x0b: bool
        _zero: int = field(init=False, **Binary(asserted=0))

    HAS_UNK1_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK2_STRUCT: tp.ClassVar[bool] = True
    HAS_GPARAM_STRUCT: tp.ClassVar[bool] = False
    HAS_SCENE_GPARAM_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK7_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK8_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK9_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK10_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK11_STRUCT: tp.ClassVar[bool] = True

    model: MSBCollisionModel = None

    # MAP CONNECTION DATA
    collision: MSBCollision = None
    connected_map_id: list[int] = field(default_factory=lambda: [21, 0, 0, 0], **BinaryArray(4))
    con_unk_x08: int = 0
    con_unk_x09: bool = False
    con_unk_x0a: int = 0
    con_unk_x0b: bool = False

    _collision_index: int = None

    # UNK STRUCT 1
    display_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    draw_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_on)
    collision_mask: GroupBitSet1024 = field(default_factory=GroupBitSet1024.all_off)
    condition_1a: int = 0
    condition_1b: int = 0
    unk1_c2: int = 0
    unk1_c3: int = 0
    unk1_c4: int = -1
    unk1_c6: int = 0

    # UNK STRUCT 2
    condition_2: int = -1
    display_groups_2: GroupBitSet256 = field(default_factory=GroupBitSet256.all_on)
    unk2_24: int = 0
    unk2_26: int = -1

    # UNK STRUCT 8
    unk8_00: int = 0

    # UNK STRUCT 10
    map_id: int = -1
    unk10_04: int = 0
    unk10_0c: int = -1
    unk10_10: int = 0  # always 0 or 1
    unk10_14: int = -1

    # UNK STRUCT 11
    unk11_00: int = 0
    unk11_04: int = 0

    @classmethod
    def unpack_subtype_data(cls, reader: BinaryReader) -> dict[str, tp.Any]:
        data = cls.SUBTYPE_DATA_STRUCT.from_bytes(reader).to_dict(ignore_underscore_prefix=False)
        return data

    def pack_subtype_data(self, writer: BinaryWriter, entry_lists: dict[str, list[MSBEntry]]):
        self.SUBTYPE_DATA_STRUCT.object_to_writer(
            self,
            writer,
            _collision_index=self.try_index(entry_lists["collisions"], "collision"),
        )

    def indices_to_objects(self, entry_lists: dict[str, list[MSBEntry]]):
        super(MSBMapConnection, self).indices_to_objects(entry_lists)
        self._consume_index(entry_lists, "collisions", "collision")

    def get_connected_map(self, get_map_func: tp.Callable):
        return get_map_func(self.connected_map_id)


@dataclass(slots=True, eq=False, repr=False)
class MSBUnusedAsset(MSBPart):
    """Unused asset. May be used in cutscenes; disabled otherwise.

    Does NOT have the same layout or even use the same Part sub-structs as `MSBAsset`. Has no variable data at all.
    """

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.UnusedAsset

    @dataclass(slots=True)
    class SUBTYPE_DATA_STRUCT(BinaryStruct):
        _pad: list[int] = field(**BinaryArray(8, asserted=[0, 0, -1, 0, -1, -1, -1, -1]))

    HAS_UNK1_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK2_STRUCT: tp.ClassVar[bool] = False
    HAS_GPARAM_STRUCT: tp.ClassVar[bool] = True
    HAS_SCENE_GPARAM_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK7_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK8_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK9_STRUCT: tp.ClassVar[bool] = False
    HAS_UNK10_STRUCT: tp.ClassVar[bool] = True
    HAS_UNK11_STRUCT: tp.ClassVar[bool] = False

    model: MSBAssetModel = None

    # UNK STRUCT 1
    display_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_off)
    draw_groups: GroupBitSet256 = field(default_factory=GroupBitSet256.all_on)
    collision_mask: GroupBitSet1024 = field(default_factory=GroupBitSet1024.all_off)
    condition_1a: int = 0
    condition_1b: int = 0
    unk1_c2: int = 0
    unk1_c3: int = 0
    unk1_c4: int = -1
    unk1_c6: int = 0

    # GPARAM
    light_set_id: int = field(default=-1, **MapFieldInfo("Light Set ID", "Light set GParam ID."))
    fog_id: int = field(default=-1, **MapFieldInfo("Fog Param ID", "Fog GParam ID."))
    light_scattering_id: int = field(default=0, **MapFieldInfo("Light Scattering ID", "Light scattering GParam ID."))
    environment_map_id: int = field(default=0, **MapFieldInfo("Environment Map ID", "Environment map GParam ID."))

    # UNK STRUCT 8
    unk8_00: int = 0

    # UNK STRUCT 10
    map_id: int = -1
    unk10_04: int = 0
    unk10_0c: int = -1
    unk10_10: int = 0  # always 0 or 1
    unk10_14: int = -1

    # UNK STRUCT 11
    unk11_00: int = 0
    unk11_04: int = 0


@dataclass(slots=True, eq=False, repr=False)
class MSBUnusedCharacter(MSBCharacter):
    """Unused character. May be used in cutscenes; disabled otherwise. Identical structure to `MSBCharacter`."""

    SUBTYPE_ENUM: tp.ClassVar = MSBPartSubtype.UnusedCharacter
