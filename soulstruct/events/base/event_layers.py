from soulstruct.utilities import BaseStruct


class BaseEventLayers(BaseStruct):
    """Only DS3 uses this (and rarely at that), though the infrastructure *may* be there for other games.

    Each instruction will only run if the map's current event layer (e.g. set by a ceremony) is enabled in
    the bit field (or by default, all are enabled).
    """

    def __init__(self, event_layers: list):
        """The event layer is simply a 32-bit bit field (represented here as a list of enabled bit flags
        in little-endian order). The bit field is packed as a 32-bit uint surrounded by a few constants.

        When packed, the instruction will contain an offset into a packed table of event layer values, which
        can be shared across multiple instructions.
        """
        self.event_layers = event_layers

    @classmethod
    def unpack(cls, file, event_layers_offset):
        """Unpack event layer bit field as <a, b, c, ...> where a, b, c, ... are the little-endian bit
        zero-based indices of the event layer bit field. 

        e.g. field 01001...110 would be {1, 4, 29, 30}.
        """
        file.seek(event_layers_offset)
        d = cls.STRUCT.unpack(file)
        enabled_event_layers_list = []
        for i in range(32):
            if (2 ** i) & d["event_layers"]:
                enabled_event_layers_list.append(i)  # TODO: Not sure why I was converting these to strings before.
        return cls(enabled_event_layers_list)

    def pack(self):
        """Opposite of `unpack`. Converts list of enabled flags into a single 32-bit uint."""
        packed_field = sum(2 ** i for i in self.event_layers)
        return self.STRUCT.pack(event_layers=packed_field)

    def to_numeric(self):
        return f" <{', '.join(str(e) for e in self.event_layers)}>"

    def to_evs(self):
        return f", event_layers={self.event_layers})"
