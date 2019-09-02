from collections import OrderedDict
import copy
from io import BytesIO, BufferedReader
from itertools import chain
import os
import shutil

from soulstruct.maps.models import MSBEntry
from soulstruct.maps.models import MSBModel, MSB_MODEL_TYPE
from soulstruct.maps.events import MSBEvent, MSB_EVENT_TYPE
from soulstruct.maps.regions import MSBRegion, MSB_REGION_TYPE
from soulstruct.maps.parts import MSBPart, MSB_PART_TYPE

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer


class MSBEntryList(object):

    MAP_ENTITY_LIST_HEADER = BinaryStruct(
        '4x',
        ('name_offset', 'i'),
        ('entry_offset_count', 'i'),
    )
    MAP_ENTITY_ENTRY_OFFSET = BinaryStruct(
        ('entry_offset', 'i'),
    )
    MAP_ENTITY_LIST_TAIL = BinaryStruct(
        ('next_entry_list_offset', 'i'),
    )

    ENTRY_LIST_NAME = None
    ENTRY_CLASS = None
    ENTRY_TYPE_ENUM = None

    def __init__(self, msb_entry_list_source=None, name=''):

        self.name = ''
        self._entries = OrderedDict()
        for entry_type in MAP_ENTRY_TYPES[self.ENTRY_LIST_NAME].values():
            self._entries[entry_type] = []

        if msb_entry_list_source is None:
            return

        if isinstance(msb_entry_list_source, (list, tuple, dict)):
            if not name:
                raise ValueError("Name of MSB entry list must be given if created manually.")
            if name not in {'POINT_PARAM_ST', 'EVENT_PARAM_ST', 'PARTS_PARAM_ST', 'MODEL_PARAM_ST'}:
                raise ValueError("Name of MSB entry list must be MODEL_PARAM_ST, EVENT_PARAM_ST, POINT_PARAM_ST, "
                                 "or PARTS_PARAM_ST.")
            if isinstance(msb_entry_list_source, dict):
                self._entries = msb_entry_list_source
            else:
                for entry in msb_entry_list_source:
                    if isinstance(entry, MSBEntry):
                        self._entries.setdefault(entry.ENTRY_TYPE, []).append(entry)
                    else:
                        raise TypeError("Non-MSBEntry found in source sequence for MSB.")
            return
        if isinstance(msb_entry_list_source, bytes):
            msb_entry_list_source = BytesIO(msb_entry_list_source)
        if isinstance(msb_entry_list_source, BufferedReader):
            self.unpack(msb_entry_list_source)
        else:
            raise TypeError(f"Invalid MSB entry list source: {msb_entry_list_source}")

    def unpack(self, msb_buffer):

        header = self.MAP_ENTITY_LIST_HEADER.unpack(msb_buffer)
        entry_offsets = [self.MAP_ENTITY_ENTRY_OFFSET.unpack(msb_buffer).entry_offset
                         for _ in range(header.entry_offset_count - 1)]
        next_entry_list_offset = self.MAP_ENTITY_LIST_TAIL.unpack(msb_buffer).next_entry_list_offset
        self.name = read_chars_from_buffer(msb_buffer, header.name_offset, encoding='utf-8')

        self._entries = OrderedDict()
        for entry_type in MAP_ENTRY_TYPES[self.ENTRY_LIST_NAME].values():
            self._entries[entry_type] = []

        for entry_offset in entry_offsets:
            msb_buffer.seek(entry_offset)
            entry = self.ENTRY_CLASS(msb_buffer)
            self._entries[entry.ENTRY_TYPE].append(entry)

        for entry_type_name, entry_type_enum in MAP_ENTRY_TYPES[self.ENTRY_LIST_NAME]:
            setattr(self, entry_type_name, self._entries[entry_type_enum])

        msb_buffer.seek(next_entry_list_offset)

    def pack(self, start_offset=0, is_last_table=False):
        entries = self.get_all_entries()
        entry_offsets = []
        packed_entries = b''
        offset = start_offset + (self.MAP_ENTITY_LIST_HEADER.size
                                 + self.MAP_ENTITY_ENTRY_OFFSET.size * len(entries)
                                 + self.MAP_ENTITY_LIST_TAIL.size)
        packed_name = self.name.encode('utf-8')
        name_offset = offset
        while len(packed_name) % 4 != 0:
            packed_name += b'\0'
        offset += len(packed_name)
        for entry in entries:
            entry_offsets.append(offset)
            packed_entry = entry.pack()
            packed_entries += packed_entry
            offset += len(packed_entry)

        next_entry_list_offset = offset if not is_last_table else 0

        packed_header = self.MAP_ENTITY_LIST_HEADER.pack(
            name_offset=name_offset,
            entry_offset_count=len(entries) + 1,
        )
        packed_header += self.MAP_ENTITY_ENTRY_OFFSET.pack([{'entry_offset': o} for o in entry_offsets])
        packed_header += self.MAP_ENTITY_LIST_TAIL.pack(next_entry_list_offset=next_entry_list_offset)

        return packed_header + packed_name + packed_entries

    def __getitem__(self, entry_type):
        if isinstance(entry_type, str) and entry_type in MAP_ENTRY_TYPES[self.ENTRY_LIST_NAME]:
            return self._entries[MAP_ENTRY_TYPES[self.ENTRY_LIST_NAME][entry_type]]
        else:
            try:
                return self._entries[entry_type]
            except KeyError:
                pass
        raise AttributeError(f"MSB entry list {self.ENTRY_LIST_NAME} has no entry type sub-list {repr(entry_type)}")

    def __iter__(self):
        return iter(self.get_all_entries())

    def get_all_entries(self):
        return list(chain(*self._entries.values()))

    def duplicate_entry(self, entry_type, index, insert_below_original=False):
        duplicated = copy.deepcopy(self._entries[entry_type][index])
        if insert_below_original:
            self._entries[entry_type].insert(index + 1, duplicated)
        else:
            self._entries[entry_type].append(duplicated)

    def get_indices(self):
        entry_indices = {}
        for i, entry in enumerate(self.get_all_entries()):
            if entry.name in entry_indices:
                raise NameError(f"Name {repr(entry.name)} appears more than once in MSB.")
            entry_indices[entry.name] = i
        return entry_indices

    def set_and_get_unique_names(self):
        unique_names = {}
        repeat_count = {}
        for i, entry in enumerate(self.get_all_entries()):
            if entry.name in unique_names.values():
                repeat_count.setdefault(entry.name, 0)
                repeat_count[entry.name] += 1
                entry.name += f' <{repeat_count[entry.name]}>'
            unique_names[i] = entry.name
        return unique_names


class MSBModelList(MSBEntryList):

    ENTRY_LIST_NAME = 'Models'
    ENTRY_CLASS = staticmethod(MSBModel)
    ENTRY_TYPE_ENUM = MSB_MODEL_TYPE

    MapPieces: list
    Objects: list
    Characters: list
    Players: list
    Collisions: list
    Navmeshes: list

    def set_indices(self, part_instance_counts):
        """Local type-specific index only. (Note that global entry index is still used by Parts.)"""
        type_indices = {}
        for entry in self.get_all_entries():
            entry.set_indices(model_type_index=type_indices.setdefault(entry.model_type, 0),
                              instance_count=part_instance_counts.get(entry.name, 0))
            type_indices[entry.model_type] += 1


class MSBEventList(MSBEntryList):
    ENTRY_LIST_NAME = 'Events'
    ENTRY_CLASS = staticmethod(MSBEvent)
    ENTRY_TYPE_ENUM = MSB_EVENT_TYPE

    Lights: list
    Sounds: list
    FX: list
    Wind: list
    Treasure: list
    Spawners: list
    Messages: list
    ObjActs: list
    SpawnPoints: list
    MapOffsets: list
    Navigation: list
    Environment: list
    NPCInvasion: list

    def set_names(self, region_names, part_names):
        for entry in self.get_all_entries():
            entry.set_names(region_names, part_names)

    def set_indices(self, region_indices, part_indices):
        """Global and type-specific indices both set. (Unclear if either of them do anything.)"""
        type_indices = {}
        for i, entry in enumerate(self.get_all_entries()):
            entry.set_indices(event_index=i, event_type_index=type_indices.setdefault(entry.EVENT_TYPE, 0),
                              region_indices=region_indices, part_indices=part_indices)
            type_indices[entry.EVENT_TYPE] += 1


class MSBRegionList(MSBEntryList):
    ENTRY_LIST_NAME = 'Regions'
    ENTRY_CLASS = staticmethod(MSBRegion)
    ENTRY_TYPE_ENUM = MSB_REGION_TYPE

    Points: list
    Circles: list
    Spheres: list
    Cylinders: list
    Rectangles: list
    Boxes: list

    def set_indices(self):
        """Global region index only."""
        for i, entry in enumerate(self.get_all_entries()):
            entry.set_indices(region_index=i)


class MSBPartList(MSBEntryList):
    ENTRY_LIST_NAME = 'Parts'
    ENTRY_CLASS = staticmethod(MSBPart)
    ENTRY_TYPE_ENUM = MSB_PART_TYPE

    MapPieces: list
    Objects: list
    Characters: list
    PlayerStarts: list
    Collisions: list
    Navmeshes: list
    DummyObjects: list
    DummyCharacters: list
    MapLoadTriggers: list

    def set_names(self, model_names, region_names, part_names):
        for entry in self.get_all_entries():
            entry.set_names(model_names, region_names, part_names)

    def set_indices(self, model_indices, region_indices, part_indices):
        """Local type-specific index only.

        Events and other Parts may point to Parts by global entry index, but it seems the local index still matters, as
        ObjAct Events seem to break when the local object index is changed. It's possible this was just an idiosyncrasy
        of Wulf's MSB Editor. Either way, this method should ensure the global and local indices are consistent.

        Note that cutscene files (remo) access Parts by index as well.
        """
        type_indices = {}
        for entry in self.get_all_entries():
            entry.set_indices(part_type_index=type_indices.setdefault(entry.PART_TYPE, 0),
                              model_indices=model_indices, region_indices=region_indices, part_indices=part_indices)
            type_indices[entry.PART_TYPE] += 1

    def get_instance_counts(self):
        """Returns a dictionary mapping model names to part instance counts."""
        instance_counts = {}
        for entry in self.get_all_entries():
            instance_counts.setdefault(entry.model_name, 0)
            instance_counts[entry.model_name] += 1
        return instance_counts


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

    def __init__(self, msb_source=None):
        self.models = MSBModelList()
        self.events = MSBEventList()
        self.regions = MSBRegionList()
        self.parts = MSBPartList()

        self.msb_path = None

        if msb_source is None:
            return
        elif isinstance(msb_source, str):
            # File path.
            self.msb_path = msb_source
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
        self.models = MSBModelList(msb_buffer)
        self.events = MSBEventList(msb_buffer)
        self.regions = MSBRegionList(msb_buffer)
        self.parts = MSBPartList(msb_buffer)

        model_names = self.models.set_and_get_unique_names()
        region_names = self.regions.set_and_get_unique_names()
        part_names = self.parts.set_and_get_unique_names()

        self.events.set_names(region_names=region_names, part_names=part_names)
        self.parts.set_names(model_names=model_names, region_names=region_names, part_names=part_names)

    def pack(self):
        """Constructs {name: id} dictionaries, then passes them to pack() methods as required by each."""
        model_indices = self.models.get_indices()
        region_indices = self.regions.get_indices()
        part_indices = self.parts.get_indices()

        # Set entry indices (both self and linked) and other auto-detected fields.
        self.models.set_indices(part_instance_counts=self.parts.get_instance_counts())
        self.events.set_indices(region_indices=region_indices, part_indices=part_indices)
        self.regions.set_indices()
        self.parts.set_indices(model_indices=model_indices, region_indices=region_indices, part_indices=part_indices)

        offset = 0
        packed_models = self.models.pack(start_offset=offset)
        offset += len(packed_models)
        packed_events = self.events.pack(start_offset=offset)
        offset += len(packed_events)
        packed_regions = self.regions.pack(start_offset=offset)
        offset += len(packed_regions)
        packed_parts = self.parts.pack(start_offset=offset, is_last_table=True)

        return packed_models + packed_events + packed_regions + packed_parts

    def write_packed(self, msb_path=None, create_bak=True):
        if msb_path is None:
            if self.msb_path is None:
                raise ValueError("MSB path cannot be automatically determined from input.")
            msb_path = self.msb_path

        if create_bak and os.path.isfile(msb_path) and not os.path.isfile(msb_path + '.bak'):
            print(f"# Backup of file {repr(msb_path)} does not exist. Creating now...")
            shutil.copy(msb_path, msb_path + '.bak')

        with open(msb_path, 'wb') as f:
            f.write(self.pack())

    # TODO: pickle/load

    def __iter__(self):
        yield self.models
        yield self.events
        yield self.regions
        yield self.parts


MAP_ENTRY_TYPES = {
    'Models': {
        'MapPieces': MSB_MODEL_TYPE.MapPiece,
        'Objects': MSB_MODEL_TYPE.Object,
        'Characters': MSB_MODEL_TYPE.Enemy,
        'Players': MSB_MODEL_TYPE.Player,
        'Collisions': MSB_MODEL_TYPE.Collision,
        'Navmeshes': MSB_MODEL_TYPE.Navmesh,
    },
    'Events': {
        'Lights': MSB_EVENT_TYPE.Light,
        'Sounds': MSB_EVENT_TYPE.Sound,
        'FX': MSB_EVENT_TYPE.FX,
        'Wind': MSB_EVENT_TYPE.Wind,
        'Treasure': MSB_EVENT_TYPE.Treasure,
        'Spawners': MSB_EVENT_TYPE.Spawner,
        'Messages': MSB_EVENT_TYPE.Message,
        'ObjActs': MSB_EVENT_TYPE.ObjAct,
        'SpawnPoints': MSB_EVENT_TYPE.SpawnPoint,
        'MapOffsets': MSB_EVENT_TYPE.MapOffset,
        'Navigation': MSB_EVENT_TYPE.Navigation,
        'Environment': MSB_EVENT_TYPE.Environment,
        'NPCInvasion': MSB_EVENT_TYPE.NPCInvasion,
    },
    'Regions': {
        'Points': MSB_REGION_TYPE.Point,
        'Circles': MSB_REGION_TYPE.Circle,
        'Spheres': MSB_REGION_TYPE.Sphere,
        'Cylinders': MSB_REGION_TYPE.Cylinder,
        'Rectangles': MSB_REGION_TYPE.Rect,
        'Boxes': MSB_REGION_TYPE.Box,
    },
    'Parts': {
        'MapPieces': MSB_PART_TYPE.MapPiece,
        'Objects': MSB_PART_TYPE.Object,
        'Characters': MSB_PART_TYPE.Character,
        'PlayerStarts': MSB_PART_TYPE.PlayerStarts,
        'Collisions': MSB_PART_TYPE.Collision,
        'Navmeshes': MSB_PART_TYPE.Navmesh,
        'DummyObjects': MSB_PART_TYPE.DummyObject,
        'DummyCharacters': MSB_PART_TYPE.DummyCharacter,
        'MapLoadTriggers': MSB_PART_TYPE.MapLoadTrigger,
    }
}
