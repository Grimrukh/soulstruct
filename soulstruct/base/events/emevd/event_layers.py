from __future__ import annotations

__all__ = ["EventLayersStruct", "EventLayers"]

from dataclasses import dataclass, field

from soulstruct.utilities.binary import *


@dataclass(slots=True)
class EventLayersStruct(NewBinaryStruct):
    _two: uint = field(init=False, **Binary(asserted=2))
    event_layers_uint: uint  # bit flag field (only real variable field)
    _zero: varuint = field(init=False, **Binary(asserted=0))
    _minus_one: varint = field(init=False, **Binary(asserted=-1))
    _one: varint = field(init=False, **Binary(asserted=1))


@dataclass(slots=True)
class EventLayers:
    """Only later games use this (and rarely at that). Elden Ring may not even support it any more.

    Each instruction will only run if the map's current event layer (e.g. set by a ceremony) is enabled in the bit field
    (or by default, all are enabled).

    The event layer is simply a 32-bit bit field (represented here as a list of enabled bit flags in little-endian
    order). The bit field is packed as a 32-bit uint surrounded by a few constants.

    When packed, the instruction will contain an offset into a packed table of event layer values, which can be shared
    across multiple instructions.
    """

    event_layers_uint: int

    @classmethod
    def from_emevd_reader(cls, reader: BinaryReader, event_layers_offset: int):
        """Unpack event layer bit field as <a, b, c, ...> where a, b, c, ... are the little-endian bit
        zero-based indices of the event layer bit field. 

        e.g. field 01001...110 would be {1, 4, 29, 30}.

        NOTE: The same `event_layers_offset` may be used by multiple instructions, rather than packing the same event
        layer over and over. This is handled when writing as well.
        """
        reader.seek(event_layers_offset)
        event_layers_struct = EventLayersStruct.from_bytes(reader)
        return cls(event_layers_struct.event_layers_uint)

    def get_enabled_event_layers(self) -> list[int]:
        """Parses bits of `uint` to return the list of enabled bits (0 to 31)."""
        enabled_event_layers_list = []
        for i in range(32):
            if (2 ** i) & self.event_layers_uint:
                enabled_event_layers_list.append(i)
        return enabled_event_layers_list

    def to_emevd_writer(self, writer: BinaryWriter):
        EventLayersStruct.object_to_writer(self, writer)

    def to_numeric(self):
        return f" <{', '.join(str(e) for e in self.get_enabled_event_layers())}>"

    def to_evs(self):
        return f"event_layers={self.get_enabled_event_layers()}"

    def __hash__(self) -> int:
        """Only the `event_layers_uint` determines object uniqueness.

        Probably automated by `dataclass` but being explicit, since it's actually used.
        """
        return hash(self.event_layers_uint)

    @staticmethod
    def flags_to_uint(flags_list: list[int]):
        """NOTE: Just for my memory. Not needed."""
        return sum(2 ** i for i in flags_list)
