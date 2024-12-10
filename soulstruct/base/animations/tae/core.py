"""'Time Act Editor' (TAE) file format.

TAE files contain various events (function callbacks with parameters) that occur on specific frames of corresponding
model animations (HKX files), such as sounds, FFX spawning, hitboxes, parry windows, and so on. Essentially, they are
responsible for everything that happens during an animation other than the actual FLVER bone/mesh deformation controlled
by the HKX file.

I currently have no plans to support any GUI editing of TAE events, as Meowmaritus's DS Anim Studio already does this
in an unbeatably good way. However, as such a critical game format, I do want it here for completion (and to permit
scripted changes).

Currently only made for Dark Souls Remastered. (PTDE is identical, but with 32-bit offsets, I believe.)
"""
from __future__ import annotations

__all__ = [
    "TAE",
    "TAEAnimation",
    "TAEEvent",
    "TAEEventGroup",
]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.exceptions import SoulstructError
from soulstruct.utilities.binary import *

from .enums import TAEEventType
from .events import TAEEventData
from . import events


@dataclass(slots=True)
class TAEEvent:

    event_type: TAEEventType
    start_time: float
    end_time: float
    event_data: TAEEventData

    @classmethod
    def from_tae_reader(cls, reader: BinaryReader) -> tp.Self:
        start_time_offset, end_time_offset, event_data_offset = reader.unpack("qqq")
        start_time = reader.unpack_value("f", offset=start_time_offset)
        end_time = reader.unpack_value("f", offset=end_time_offset)

        with reader.temp_offset(event_data_offset):
            event_type_value = reader.unpack_value("q")  # 64-bit enum value
            try:
                event_type = TAEEventType(event_type_value)
            except ValueError:
                raise ValueError(f"Invalid/unknown TAE event type value: {event_type_value}")

            reader.unpack_value("q", asserted=reader.position + 8)  # event data offset (immediately after this)
            # Names of `TAEEventData` subclasses match `TAEventTypes` enum names.
            try:
                event_data_class = getattr(events, event_type.name)  # type: type[TAEEventData]
            except AttributeError:
                raise AttributeError(f"No TAE event data class corresponding to known event type: {event_type.name}")
            if event_data_class.event_type != event_type:
                raise SoulstructError(
                    f"Event data class {event_data_class.__name__} does not match event type {event_type}. This is an "
                    f"internal Soulstruct error; please report it to Grimrukh."
                )
            event_data = event_data_class.from_bytes(reader)

        return cls(event_type=event_type, start_time=start_time, end_time=end_time, event_data=event_data)


@dataclass(slots=True)
class TAEEventGroup:
    """A group of animation events with a shared `TAEEventType` that does not necessarily match their own type."""

    event_type: TAEEventType
    event_indices: list[int]

    @classmethod
    def from_tae_reader(cls, reader: BinaryReader, event_offsets_to_indices: dict[int, int]) -> tp.Self:
        """Event groups reference event offsets, but we use the `event_offsets_to_indices` dict (from main `TAE`) to
        remap these offsets to event indices."""
        entry_count, values_offset, type_offset = reader.unpack("qqq")
        reader.unpack_value("q", asserted=0)

        with reader.temp_offset(type_offset):
            event_type_value = reader.unpack_value("q")
            try:
                event_type = TAEEventType(event_type_value)
            except ValueError:
                raise ValueError(f"Invalid/unknown TAE event type value (in event group): {event_type_value}")
            reader.unpack_value("q", asserted=0)

        with reader.temp_offset(values_offset):
            header_offsets = reader.unpack(f"{entry_count}i")
            event_indices = [event_offsets_to_indices[offset] for offset in header_offsets]

        return cls(event_type=event_type, event_indices=event_indices)


@dataclass(slots=True)
class TAEAnimation:

    @dataclass(slots=True)
    class STRUCT(BinaryStruct):
        event_headers_offset: int64
        event_groups_offset: int64
        event_times_offset: int64
        animation_file_offset: int64
        event_count: int32
        event_group_count: int32
        event_times_count: int32
        _zero: int32 = field(init=False, **Binary(asserted=0))

    animation_id: int
    events: list[TAEEvent]
    event_groups: list[TAEEventGroup]
    is_animation_file_reference: bool
    animation_file_unk_x18: int
    animation_file_unk_x1c: int
    animation_file_name: str

    @classmethod
    def from_tae_reader(cls, reader: BinaryReader, encoding: str) -> tp.Self:
        animation_id, offset = reader.unpack("qq")
        with reader.temp_offset(offset):
            animation_struct = cls.STRUCT.from_bytes(reader)
            event_offsets_to_indices = {}
            tae_events = []
            with reader.temp_offset(animation_struct.event_headers_offset):
                for event_index in range(animation_struct.event_count):
                    event_offsets_to_indices[reader.position] = event_index
                    tae_events.append(TAEEvent.from_tae_reader(reader))

            event_groups = []
            with reader.temp_offset(animation_struct.event_groups_offset):
                for _ in range(animation_struct.event_group_count):
                    event_groups.append(TAEEventGroup.from_tae_reader(reader, event_offsets_to_indices))

            with reader.temp_offset(animation_struct.animation_file_offset):
                animation_file_reference = reader.unpack_value("?")
                reader.unpack_value("q", asserted=reader.position + 8)  # file name offset (immediately after this)
                animation_file_name_offset = reader.unpack_value("q")
                animation_file_unk_x18, animation_file_unk_x1c = reader.unpack("ii")
                reader.unpack("qq", asserted=(0, 0))

                # SF checks that file name offset is within buffer. We can just catch a `ValueError` instead.
                try:
                    animation_file_name = reader.unpack_string(offset=animation_file_name_offset, encoding=encoding)
                except ValueError:
                    animation_file_name = ""
                else:
                    # SF NOTE: When `is_animation_file_reference == False`, there is always an animation file name.
                    # When `is_animation_file_reference == True`, there is *usually* not a file name, but sometimes is.
                    # We ignore file names without a valid suffix.

                    if not animation_file_name.endswith((".hkt", ".hkx")):
                        animation_file_name = ""

        return cls(
            animation_id=animation_id,
            events=tae_events,
            event_groups=event_groups,
            is_animation_file_reference=animation_file_reference,
            animation_file_unk_x18=animation_file_unk_x18,
            animation_file_unk_x1c=animation_file_unk_x1c,
            animation_file_name=animation_file_name,
        )


@dataclass(slots=True)
class TAEHeaderStruct(BinaryStruct):
    magic: str = field(init=False, **BinaryString(4, asserted="TAE "))
    _fixed_0: list[sbyte] = field(init=False, **BinaryArray(4, asserted=[0x0, 0x0, 0x0, 0xff]))
    version: int = field(init=False, **Binary(asserted=0x1000C))
    file_size: int
    _fixed_1: list[int64] = field(init=False, **BinaryArray(4, asserted=[0x40, 0x1, 0x50, 0x80]))
    unk_x30: int
    _zero: int64 = field(init=False, **Binary(asserted=0))
    flags: list[byte] = field(**BinaryArray(8))
    _one: int64 = field(init=False, **Binary(asserted=1))
    tae_id_0: int32
    animation_count_0: int32
    animations_offset: int64
    animation_groups_offset: int64
    _xa0: int64 = field(init=False, **Binary(asserted=0xa0))
    animation_count_1: int32
    first_animation_offset: int64
    _one_2: int64 = field(init=False, **Binary(asserted=1))
    _x90: int64 = field(init=False, **Binary(asserted=0x90))
    tae_id_1: int32
    tae_id_2: int32
    _x50: int64 = field(init=False, **Binary(asserted=0x50))
    _zero_2: int64 = field(init=False, **Binary(asserted=0))
    _xb0: int64 = field(init=False, **Binary(asserted=0xb0))
    skeleton_name_offset: int64
    sib_name_offset: int64
    _pad: bytes = field(init=False, **BinaryPad(0x2))


@dataclass(slots=True)
class TAE(GameFile):
    """TODO: Write methods."""

    tae_id: int
    flags: list[int]  # unknown flags
    skeleton_name: str
    sib_name: str
    animations: list[TAEAnimation]
    unk_x30: int

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        """Read TAE from reader.

        TODO: TAE is always little-endian? Not touching existing endianness for now.
        """
        header = TAEHeaderStruct.from_bytes(reader)
        encoding = reader.get_utf_16_encoding()

        # These strings sit right after the header, with a 0x10 pad afterward.
        skeleton_name = reader.unpack_string(offset=header.skeleton_name_offset, encoding=encoding)
        sib_name = reader.unpack_string(offset=header.sib_name_offset, encoding=encoding)

        reader.seek(header.animations_offset)  # no step-in needed
        animations = [TAEAnimation.from_tae_reader(reader, encoding) for _ in range(header.animation_count_0)]
        # We don't read animation groups, as they don't actually contain information (inferrable from animation IDs).

        return cls(
            tae_id=header.tae_id_0,
            flags=header.flags,
            skeleton_name=skeleton_name,
            sib_name=sib_name,
            animations=animations,
            unk_x30=header.unk_x30,
        )

    def to_writer(self) -> BinaryWriter:
        pass
