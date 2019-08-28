from io import BytesIO, BufferedReader
from soulstruct.maps.models import MSBModel
from soulstruct.maps.events import MSBEvent
from soulstruct.maps.regions import MSBRegion
from soulstruct.maps.parts import MSBPart

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer


class MSB(object):
    """Handles MSB ('MapStudio') data for Dark Souls 1.

    Only DS1 (either version) is supported.

    The MSB contains four types of data entries:

        Models: these are models that are available for map 'Part' entities such as map pieces, objects, characters,
            players, collisions, and navmeshes. Every Part included in the map will reference one of these models, and
            only models in this list will be loaded with the map.

        Events: these are 'things that happen' in the map, and are generally linked to Regions and/or Parts that have
            actual map coordinate data. There are numerous subtypes with additional data fields. Each event has an
            entity ID that may be referenced in the game events. There are no internal references to events inside the
            MSB, so they are never accessed by index and can be stored in any order.

        Regions: these are invisible points, shapes, and volumes that appear in the map. They are used to anchor events
            (e.g. spawn points, music, patrol points) and to perform location-based trigger checks in the game events
            (where they are referenced using their entity ID). Many MSB Events reference Regions by index, so their
            order needs to be carefully managed internally.

        Parts: these are actual map entities, including objects and characters. Each of them is linked to a model
            index, has a physical transform (translate, rotate, scale), and an optional entity ID. Characters and
            objects additionally have a collision index (their 'home' collision) and draw/display groups that determine
            when they are actually visible in the game. Some MSB Events reference Parts by index, so their order needs
            to be carefully managed internally.
    """

    class MSBEntryList(object):
        MAP_ENTITY_LIST_HEADER = BinaryStruct(
            '4x',
            ('name_offset', 'i'),
            ('offset_count', 'i'),
        )
        MAP_ENTITY_ENTRY_OFFSET = BinaryStruct(
            ('entry_offset', 'i'),
        )
        MAP_ENTITY_LIST_TAIL = BinaryStruct(
            ('next_entity_list_offset', 'i'),
        )

        def __init__(self, msb_entry_list_source, entry_class=None, name=''):
            self.entry_class = entry_class

            self.name = ''
            self.entries = []

            if isinstance(msb_entry_list_source, (list, tuple)):
                if not name:
                    raise ValueError("Name of MSB entry list must be given if created manually.")
                if name not in {'POINT_PARAM_ST', 'EVENT_PARAM_ST', 'PARTS_PARAM_ST', 'MODEL_PARAM_ST'}:
                    raise ValueError("Name of MSB entry list must be MODEL_PARAM_ST, EVENT_PARAM_ST, POINT_PARAM_ST, " 
                                     "or PARTS_PARAM_ST.")
                self.entries = list(msb_entry_list_source)
                return
            elif isinstance(msb_entry_list_source, bytes):
                msb_entry_list_source = BytesIO(msb_entry_list_source)
            if isinstance(msb_entry_list_source, BufferedReader):
                self.unpack(msb_entry_list_source)
            else:
                raise TypeError(f"Invalid MSB entry list source: {msb_entry_list_source}")

        def unpack(self, msb_buffer):
            header = self.MAP_ENTITY_LIST_HEADER.unpack(msb_buffer)
            entry_offsets = [self.MAP_ENTITY_ENTRY_OFFSET.unpack(msb_buffer).entry_offset
                             for _ in range(header.offset_count - 1)]
            next_entity_list_offset = self.MAP_ENTITY_LIST_TAIL.unpack(msb_buffer).next_entity_list_offset
            self.name = read_chars_from_buffer(msb_buffer, header.name_offset, encoding='utf-8')

            self.entries = []
            for entry_offset in entry_offsets:
                msb_buffer.seek(entry_offset)
                self.entries.append(self.entry_class(msb_buffer))

            msb_buffer.seek(next_entity_list_offset)

        def __getitem__(self, index):
            return self.entries[index]

    def __init__(self, msb_source):
        self.models = None
        self.events = None
        self.regions = None
        self.parts = None

        if isinstance(msb_source, str):
            # File path.
            with open(msb_source, 'rb') as msb_buffer:
                self.unpack(msb_buffer)
        elif isinstance(msb_source, bytes):
            self.unpack(BytesIO(msb_source))
        elif isinstance(msb_source, BufferedReader):
            self.unpack(msb_source)
        else:
            raise TypeError(f"Invalid MSB source type: {type(msb_source)}. "
                            f"Must be string (file path), bytes, or buffer.")

    def unpack(self, msb_buffer):
        self.models = self.MSBEntryList(msb_buffer, entry_class=MSBModel)
        self.events = self.MSBEntryList(msb_buffer, entry_class=MSBEvent)
        self.regions = self.MSBEntryList(msb_buffer, entry_class=MSBRegion)
        self.parts = self.MSBEntryList(msb_buffer, entry_class=MSBPart)


if __name__ == '__main__':
    msb_path = r"G:\Steam\steamapps\common\DARK SOULS REMASTERED\map\MapStudio\m10_00_00_00.msb"

    msb = MSB(msb_path)
