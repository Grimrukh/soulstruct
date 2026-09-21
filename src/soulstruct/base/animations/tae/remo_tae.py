"""Cutscene ('REMO') TAE files, as found inside DSR `remobnd` binders.

Unlike character TAEs (`TAE` in `core.py`, format version 0x1000C with 64-bit offsets), cutscene TAEs use format version
0x1000B with 32-bit offsets, have no skeleton/SIB names, and contain event types that do not exist for characters.
Since we cannot (yet) interpret those event types, this module models events generically: an integer type, start/end
times and a raw payload whose size is inferred from the file layout. The file can be written back byte-for-byte
identical to every vanilla DSR cutscene TAE (see `tests/test_remo_tae_roundtrip.py`), so it is safe to load, edit and
save real files, and `RemoTAE.new()` can build a minimal TAE for a brand new cutscene.

Layout (all little-endian, 32-bit offsets, verified against all 103 vanilla DSR cutscene TAEs):

    Header (0xA8 bytes): fixed constants plus `tae_id`, animation count and the offsets of the animation header table
        and animation group table. Every vanilla cutscene TAE has `tae_id == 10001000`, flags `[1,0,1,2,2,1,1,1]` and
        `unk_x20 == 0x10002`.
    Animation header table: `(animation_id: int32, animation_offset: int32)` per animation. One animation per cut
        (`animation_id` is the cut number, e.g. 20 for 'cut0020'), plus (usually) a 'final' animation 99999 whose events
        reset every cutscene-controlled setting (draw params etc.) with -1 values.
    Animation group table: `count, offset` then `(first_id, last_id, animation_header_offset)` per group. Consecutive
        animation IDs are merged into one group (as in character TAEs).
    Animation structs (0x1C each, contiguous): event count/offset, event group count/offset, event time count/offset,
        and the offset of the animation file struct.
    Per animation, in order: animation file struct (0x18: `is_reference=0`, self-pointer, name pointer to the
        (usually empty) UTF-16 animation file name that immediately follows, padded to 8 bytes, one junk pointer, two
        zeros), event times (unique sorted float32s), event headers
        (`start_time_offset, end_time_offset, event_data_offset`), event data blocks (`type: int32`, pointer to the
        payload that immediately follows or 0 if the type has no payload, payload), event groups
        (`count, values_offset, type_offset`) and finally, per group, its type block (`type: int32`, payload pointer or 0,
        optional 16-byte payload) followed by its `count` event header offsets.

Event group type 128 ('apply to cutscene entity') carries a 16-byte payload identifying the MSB Part the grouped events
apply to; see `RemoTAEEventGroup.ENTITY_GROUP_TYPE`. Event groups of type 0, 16 and 192 have no payload.
"""
from __future__ import annotations

__all__ = [
    "RemoTAE",
    "RemoTAEAnimation",
    "RemoTAEEvent",
    "RemoTAEEventGroup",
]

import logging
import struct
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *

_LOGGER = logging.getLogger(__name__)

# Fixed header values shared by every vanilla DSR cutscene TAE.
_MAGIC = b"TAE "
_VERSION = 0x1000B
_HEADER_SIZE = 0xA8
_ANIMATION_STRUCT_SIZE = 0x1C
_ANIMATION_FILE_STRUCT_SIZE = 0x18
_EVENT_HEADER_SIZE = 0xC
_EVENT_GROUP_SIZE = 0xC
_GROUP_PAYLOAD_SIZE = 0x10

DEFAULT_TAE_ID = 10001000
DEFAULT_FLAGS = (1, 0, 1, 2, 2, 1, 1, 1)
DEFAULT_UNK_X20 = 0x10002


def _f32(value: float) -> float:
    """Round `value` to float32 precision, so times compare exactly with values read from the file."""
    return struct.unpack("<f", struct.pack("<f", value))[0]


@dataclass(slots=True)
class RemoTAEEvent:
    """A cutscene TAE event. Payload is kept raw, as cutscene event types are not (yet) documented."""

    event_type: int
    start_time: float
    end_time: float
    data: bytes = b""  # empty for event types with no payload (their data pointer is 0)

    def __repr__(self) -> str:
        return (
            f"RemoTAEEvent(type={self.event_type}, {self.start_time:.4f}-{self.end_time:.4f}, "
            f"data={self.data.hex(' ')!r})"
        )


@dataclass(slots=True)
class RemoTAEEventGroup:
    """A group of events sharing a group type, optionally targeting a specific cutscene entity (MSB Part).

    `data` is the raw 16-byte payload of type-128 groups (`None` for other types). Decoded (unverified in-game, but
    consistent with every vanilla file): `entity_type: int16` (0 = Character, 1 = Object, 2 = Map Piece, 4 = Dummy),
    `model_id: int16` (e.g. 2510 for 'm2510B1', 5350 for 'c5350_0000'), `instance: int16` (e.g. 1 for 'c5350_0001'; -1
    for the player and Map Pieces), `block: int8`, `area: int8` (-1 for the cutscene's own map), then 8 zero bytes.
    """

    ENTITY_GROUP_TYPE: tp.ClassVar[int] = 128

    group_type: int
    event_indices: list[int] = field(default_factory=list)  # indices into `RemoTAEAnimation.events`
    data: bytes | None = None

    def __repr__(self) -> str:
        data = f", data={self.data.hex(' ')!r}" if self.data is not None else ""
        return f"RemoTAEEventGroup(type={self.group_type}, events={self.event_indices}{data})"


@dataclass(slots=True)
class RemoTAEAnimation:
    """One animation of a cutscene TAE. For cuts, `animation_id` is the cut number ('cut0020' -> 20)."""

    animation_id: int
    events: list[RemoTAEEvent] = field(default_factory=list)
    event_groups: list[RemoTAEEventGroup] = field(default_factory=list)
    # Almost always empty; two vanilla files name their cut HKX here (e.g. 'a0010.HKXwin').
    animation_file_name: str = ""
    # Vanilla files store an apparently uninitialised pointer in the animation file struct (it points somewhere
    # inside the animation's own event/group data). Preserved for byte-exact round trips; 0 for new animations.
    unk_file_x0c: int = 0

    def get_event_times(self) -> list[float]:
        """Unique, sorted float32 event start/end times (the layout vanilla files use)."""
        times = {_f32(event.start_time) for event in self.events} | {_f32(event.end_time) for event in self.events}
        return sorted(times)

    def __repr__(self) -> str:
        lines = [f"RemoTAEAnimation({self.animation_id},"]
        for event in self.events:
            lines.append(f"    {event!r},")
        for group in self.event_groups:
            lines.append(f"    {group!r},")
        lines.append(")")
        return "\n".join(lines)


class RemoTAE(GameFile):
    """Cutscene TAE (format version 0x1000B, 32-bit offsets). See module docstring."""

    tae_id: int = DEFAULT_TAE_ID
    flags: list[int] = field(default_factory=lambda: list(DEFAULT_FLAGS))
    unk_x20: int = DEFAULT_UNK_X20
    animations: list[RemoTAEAnimation] = field(default_factory=list)

    @classmethod
    def new(cls, cut_numbers: tp.Iterable[int]) -> tp.Self:
        """Create a minimal cutscene TAE with one event-less animation per cut number.

        Event-less cut animations occur in vanilla files, so this is a valid (if bare) TAE: no fades, sounds or draw
        parameter changes will happen during the cutscene. Vanilla files usually also contain a 'final' animation
        (ID 99999) that resets cutscene-controlled settings, which is omitted here as there is nothing to reset.
        """
        return cls(animations=[RemoTAEAnimation(animation_id=int(cut_number)) for cut_number in cut_numbers])

    def get_animation(self, animation_id: int) -> RemoTAEAnimation | None:
        for animation in self.animations:
            if animation.animation_id == animation_id:
                return animation
        return None

    # region Read

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        reader.byte_order = ByteOrder.LittleEndian
        data = reader.read()  # whole file; offsets below are absolute
        reader.seek(0)

        def u32(offset: int) -> int:
            return struct.unpack_from("<I", data, offset)[0]

        def i32(offset: int) -> int:
            return struct.unpack_from("<i", data, offset)[0]

        def f32(offset: int) -> float:
            return struct.unpack_from("<f", data, offset)[0]

        if data[:4] != _MAGIC:
            raise ValueError(f"Not a TAE file (magic {data[:4]!r}).")
        version = u32(0x8)
        if version != _VERSION:
            raise ValueError(
                f"`RemoTAE` only supports cutscene TAE format version 0x{_VERSION:X}, not 0x{version:X}. Character "
                f"TAEs (0x1000C) are handled by `TAE`."
            )
        file_size = u32(0xC)
        if file_size != len(data):
            raise ValueError(f"TAE header file size ({file_size}) does not match data size ({len(data)}).")
        for offset, expected in ((0x10, 0x40), (0x14, 1), (0x18, 0x50), (0x1C, 0x70), (0x24, 0)):
            if u32(offset) != expected:
                raise ValueError(f"Unexpected TAE header value at 0x{offset:X}: {u32(offset)} != {expected}")
        unk_x20 = u32(0x20)
        if data[0x28:0x40] != bytes(0x18):
            raise ValueError("Expected 24 null bytes at TAE header offset 0x28.")
        flags = list(data[0x40:0x48])
        for offset, expected in ((0x48, 1), (0x4C, 0)):
            if u32(offset) != expected:
                raise ValueError(f"Unexpected TAE header value at 0x{offset:X}: {u32(offset)} != {expected}")
        tae_id = u32(0x50)
        animation_count = u32(0x54)
        animations_offset = u32(0x58)
        animation_groups_offset = u32(0x5C)
        for offset, expected in (
            (0x60, 0x90), (0x64, animation_count), (0x6C, 0), (0x70, 1), (0x74, 0x80), (0x78, 0), (0x7C, 0),
            (0x80, tae_id), (0x84, tae_id), (0x88, 0x50), (0x8C, 0), (0x90, 0), (0x94, 0x98), (0x98, 0), (0x9C, 0),
            (0xA0, 0), (0xA4, 0),
        ):
            if u32(offset) != expected:
                raise ValueError(f"Unexpected TAE header value at 0x{offset:X}: {u32(offset)} != {expected}")
        first_animation_offset = u32(0x68)

        # Animation header table.
        animation_headers = [
            (i32(animations_offset + 8 * i), u32(animations_offset + 8 * i + 4)) for i in range(animation_count)
        ]
        if animation_count and animation_headers[0][1] != first_animation_offset:
            raise ValueError("TAE header's first animation offset does not match the first animation header.")

        # Animation groups are fully inferrable from the animation IDs; just validate them.
        group_count = u32(animation_groups_offset)
        groups_offset = u32(animation_groups_offset + 4)
        if groups_offset != animation_groups_offset + 8:
            raise ValueError("TAE animation group table offset is not immediately after its count.")
        animation_groups = [
            (i32(groups_offset + 12 * i), i32(groups_offset + 12 * i + 4), u32(groups_offset + 12 * i + 8))
            for i in range(group_count)
        ]
        expected_groups = cls._get_animation_groups([anim_id for anim_id, _ in animation_headers], animations_offset)
        if animation_groups != expected_groups:
            raise ValueError(
                f"TAE animation groups {animation_groups} do not match the groups implied by the animation IDs "
                f"{expected_groups}."
            )

        animations = []
        for anim_index, (animation_id, animation_offset) in enumerate(animation_headers):
            o = animation_offset
            event_count, events_offset = u32(o), u32(o + 4)
            event_group_count, event_groups_offset = u32(o + 8), u32(o + 12)
            event_time_count, event_times_offset = u32(o + 16), u32(o + 20)
            file_offset = u32(o + 24)

            # Animation file struct (no real content in cutscene TAEs).
            if u32(file_offset) != 0:
                raise ValueError(f"TAE animation {animation_id} has a non-zero animation file reference flag.")
            if u32(file_offset + 4) != file_offset + 8 or u32(file_offset + 8) != file_offset + 0x18:
                raise ValueError(f"TAE animation {animation_id} has unexpected animation file struct pointers.")
            unk_file_x0c = u32(file_offset + 0xC)
            if u32(file_offset + 0x10) != 0 or u32(file_offset + 0x14) != 0:
                raise ValueError(f"TAE animation {animation_id} has non-zero padding in its animation file struct.")
            # The (UTF-16, usually empty) animation file name follows the struct and ends where the next block starts.
            name_offset = file_offset + _ANIMATION_FILE_STRUCT_SIZE
            next_offsets = [o for o in (event_times_offset, events_offset, event_groups_offset) if o]
            if not next_offsets:
                if anim_index + 1 < animation_count:
                    next_offsets.append(u32(animation_headers[anim_index + 1][1] + 24))
                else:
                    next_offsets.append(file_size)
            name_end = min(next_offsets)
            animation_file_name = data[name_offset:name_end].decode("utf-16-le").rstrip(chr(0)) if name_end > name_offset else ""

            event_times = [f32(event_times_offset + 4 * i) for i in range(event_time_count)]

            # Event data payload sizes are the gaps between consecutive event data blocks; the last block ends where
            # the event groups start (or, with no groups, where the next animation's file struct starts / the file ends).
            event_headers = []
            for i in range(event_count):
                eo = events_offset + _EVENT_HEADER_SIZE * i
                event_headers.append((u32(eo), u32(eo + 4), u32(eo + 8)))
            if event_group_count:
                data_end = event_groups_offset
            elif event_count == 0:
                data_end = None  # unused
            elif anim_index + 1 < animation_count:
                next_offset = animation_headers[anim_index + 1][1]
                data_end = u32(next_offset + 24)  # next animation's file struct offset
            else:
                data_end = file_size

            events = []
            for i, (start_offset, end_offset, data_offset) in enumerate(event_headers):
                event_type = i32(data_offset)
                data_pointer = u32(data_offset + 4)
                next_data_offset = event_headers[i + 1][2] if i + 1 < event_count else data_end
                if data_pointer == 0:
                    payload = b""
                    if next_data_offset != data_offset + 8:
                        raise ValueError(
                            f"TAE animation {animation_id} event {i} (type {event_type}) has no payload pointer but "
                            f"is followed by {next_data_offset - data_offset - 8} unexpected bytes."
                        )
                elif data_pointer != data_offset + 8:
                    raise ValueError(
                        f"TAE animation {animation_id} event {i} (type {event_type}) payload pointer does not point "
                        f"immediately after the event data header."
                    )
                else:
                    payload = data[data_offset + 8:next_data_offset]
                events.append(
                    RemoTAEEvent(
                        event_type=event_type,
                        start_time=f32(start_offset),
                        end_time=f32(end_offset),
                        data=payload,
                    )
                )
                if (start_offset - event_times_offset) % 4 or (end_offset - event_times_offset) % 4:
                    raise ValueError(f"TAE animation {animation_id} event {i} time offsets are not in the time block.")

            event_header_offsets = {
                events_offset + _EVENT_HEADER_SIZE * i: i for i in range(event_count)
            }
            event_groups = []
            for i in range(event_group_count):
                go = event_groups_offset + _EVENT_GROUP_SIZE * i
                count, values_offset, type_offset = u32(go), u32(go + 4), u32(go + 8)
                group_type = i32(type_offset)
                payload_pointer = u32(type_offset + 4)
                if payload_pointer == 0:
                    payload = None
                elif payload_pointer != type_offset + 8:
                    raise ValueError(
                        f"TAE animation {animation_id} event group {i} (type {group_type}) payload pointer does not "
                        f"point immediately after the group type."
                    )
                else:
                    payload = data[type_offset + 8:type_offset + 8 + _GROUP_PAYLOAD_SIZE]
                try:
                    indices = [
                        event_header_offsets[u32(values_offset + 4 * j)] for j in range(count)
                    ]
                except KeyError as ex:
                    raise ValueError(
                        f"TAE animation {animation_id} event group {i} references unknown event header offset {ex}."
                    )
                event_groups.append(RemoTAEEventGroup(group_type=group_type, event_indices=indices, data=payload))

            animation = RemoTAEAnimation(
                animation_id=animation_id,
                events=events,
                event_groups=event_groups,
                animation_file_name=animation_file_name,
                unk_file_x0c=unk_file_x0c,
            )
            if animation.get_event_times() != event_times:
                _LOGGER.warning(
                    f"TAE animation {animation_id} event time block {event_times} is not the sorted unique set of its "
                    f"event times {animation.get_event_times()}. It will be regenerated on write."
                )
            animations.append(animation)

        return cls(tae_id=tae_id, flags=flags, unk_x20=unk_x20, animations=animations)

    # endregion

    # region Write

    @staticmethod
    def _get_animation_groups(animation_ids: list[int], animations_offset: int) -> list[tuple[int, int, int]]:
        """Group runs of consecutive animation IDs: `(first_id, last_id, first_animation_header_offset)`."""
        groups = []
        for i, animation_id in enumerate(animation_ids):
            if groups and groups[-1][1] == animation_id - 1:
                first_id, _, header_offset = groups[-1]
                groups[-1] = (first_id, animation_id, header_offset)
            else:
                groups.append((animation_id, animation_id, animations_offset + 8 * i))
        return groups

    def to_writer(self) -> BinaryWriter:
        if len(self.flags) != 8:
            raise ValueError(f"`RemoTAE.flags` must contain exactly 8 bytes, not {len(self.flags)}.")
        animation_ids = [animation.animation_id for animation in self.animations]
        if len(set(animation_ids)) != len(animation_ids):
            raise ValueError(f"`RemoTAE` animation IDs must be unique: {animation_ids}")
        animation_count = len(self.animations)

        animations_offset = _HEADER_SIZE
        animation_groups_offset = animations_offset + 8 * animation_count
        animation_groups = self._get_animation_groups(animation_ids, animations_offset)
        first_animation_offset = animation_groups_offset + 8 + 12 * len(animation_groups)

        writer = BinaryWriter(byte_order=ByteOrder.LittleEndian)
        writer.append(_MAGIC)
        writer.pack("4B", 0, 0, 0, 0)
        writer.pack("I", _VERSION)
        writer.reserve("file_size", "I", obj=self)
        writer.pack("4I", 0x40, 1, 0x50, 0x70)
        writer.pack("2I", self.unk_x20, 0)
        writer.pad(0x18)
        writer.pack("8B", *self.flags)
        writer.pack("2I", 1, 0)
        writer.pack("4I", self.tae_id, animation_count, animations_offset, animation_groups_offset)
        writer.pack("4I", 0x90, animation_count, first_animation_offset if animation_count else 0, 0)
        writer.pack("4I", 1, 0x80, 0, 0)
        writer.pack("4I", self.tae_id, self.tae_id, 0x50, 0)
        writer.pack("6I", 0, 0x98, 0, 0, 0, 0)
        if writer.position != _HEADER_SIZE:
            raise RuntimeError(f"RemoTAE header size mismatch: {writer.position} != {_HEADER_SIZE}")

        # Animation header table (offsets filled in below) and animation group table.
        for animation in self.animations:
            writer.pack("i", animation.animation_id)
            writer.reserve(f"anim{animation.animation_id}", "I", obj=self)
        writer.pack("2I", len(animation_groups), writer.position + 8)
        for first_id, last_id, header_offset in animation_groups:
            writer.pack("2iI", first_id, last_id, header_offset)

        # Animation structs (contiguous), then each animation's data blocks.
        for animation in self.animations:
            writer.fill(f"anim{animation.animation_id}", writer.position, obj=self)
            for name, count in (
                ("events", len(animation.events)),
                ("event_groups", len(animation.event_groups)),
                ("event_times", len(animation.get_event_times())),
            ):
                writer.pack("I", count)
                writer.reserve(f"anim{animation.animation_id}_{name}_offset", "I", obj=self)
            writer.reserve(f"anim{animation.animation_id}_file_offset", "I", obj=self)

        for animation in self.animations:
            self._write_animation_data(writer, animation)

        writer.fill("file_size", writer.position, obj=self)
        return writer

    def _write_animation_data(self, writer: BinaryWriter, animation: RemoTAEAnimation):
        anim = f"anim{animation.animation_id}"
        event_times = animation.get_event_times()
        time_offsets = {}  # type: dict[float, int]

        # Animation file struct: no reference, no name (name pointer targets the empty string right after the struct).
        file_offset = writer.position
        writer.fill(f"{anim}_file_offset", file_offset, obj=self)
        writer.pack("6I", 0, file_offset + 8, file_offset + _ANIMATION_FILE_STRUCT_SIZE, animation.unk_file_x0c, 0, 0)
        if animation.animation_file_name:
            writer.append(animation.animation_file_name.encode("utf-16-le") + bytes(2))
            writer.pad_align(8)

        writer.fill(f"{anim}_event_times_offset", writer.position if event_times else 0, obj=self)
        for t in event_times:
            time_offsets[t] = writer.position
            writer.pack("f", t)

        event_count = len(animation.events)
        events_offset = writer.position
        writer.fill(f"{anim}_events_offset", events_offset if event_count else 0, obj=self)
        # Event headers reference event data blocks, which follow immediately (in order).
        data_offset = events_offset + _EVENT_HEADER_SIZE * event_count
        event_header_offsets = []
        for event in animation.events:
            event_header_offsets.append(writer.position)
            writer.pack(
                "3I", time_offsets[_f32(event.start_time)], time_offsets[_f32(event.end_time)], data_offset
            )
            data_offset += 8 + len(event.data)
        for event in animation.events:
            writer.pack("i", event.event_type)
            if event.data:
                writer.pack("I", writer.position + 4)
                writer.append(event.data)
            else:
                writer.pack("I", 0)

        group_count = len(animation.event_groups)
        groups_offset = writer.position
        writer.fill(f"{anim}_event_groups_offset", groups_offset if group_count else 0, obj=self)
        # Each group's type block and value list follow the group array, in group order.
        block_offset = groups_offset + _EVENT_GROUP_SIZE * group_count
        for group in animation.event_groups:
            type_offset = block_offset
            block_offset += 8 + (_GROUP_PAYLOAD_SIZE if group.data is not None else 0)
            values_offset = block_offset
            block_offset += 4 * len(group.event_indices)
            writer.pack("3I", len(group.event_indices), values_offset, type_offset)
        for group in animation.event_groups:
            writer.pack("i", group.group_type)
            if group.data is not None:
                if len(group.data) != _GROUP_PAYLOAD_SIZE:
                    raise ValueError(
                        f"TAE animation {animation.animation_id} event group payload must be {_GROUP_PAYLOAD_SIZE} "
                        f"bytes, not {len(group.data)}."
                    )
                writer.pack("I", writer.position + 4)
                writer.append(group.data)
            else:
                writer.pack("I", 0)
            for event_index in group.event_indices:
                try:
                    writer.pack("I", event_header_offsets[event_index])
                except IndexError:
                    raise ValueError(
                        f"TAE animation {animation.animation_id} event group references event index {event_index}, "
                        f"but the animation only has {event_count} events."
                    )
        if writer.position != block_offset:
            raise RuntimeError("RemoTAE event group block size mismatch (internal error).")

    # endregion

    def __repr__(self) -> str:
        lines = [f"RemoTAE(tae_id={self.tae_id}, animations=["]
        for animation in self.animations:
            lines.extend("    " + line for line in repr(animation).split("\n"))
        lines.append("])")
        return "\n".join(lines)
