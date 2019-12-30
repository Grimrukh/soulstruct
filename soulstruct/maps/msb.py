import copy
from io import BytesIO, BufferedReader
from pathlib import Path
from typing import List, Iterator

from soulstruct.maps.models import MSBEntry
from soulstruct.maps.models import MSBModel, MSB_MODEL_TYPE
from soulstruct.maps.events import MSBEvent, MSB_EVENT_TYPE, BaseMSBEvent
from soulstruct.maps.regions import MSBRegion, MSB_REGION_TYPE, BaseMSBRegion
from soulstruct.maps.parts import MSBPart, MSB_PART_TYPE, BaseMSBPart

from soulstruct.utilities import BinaryStruct, read_chars_from_buffer, create_bak

MAP_ENTRY_TYPES = {
    'Parts': {
        'MapPieces': MSB_PART_TYPE.MapPiece,
        'Objects': MSB_PART_TYPE.Object,
        'Characters': MSB_PART_TYPE.Character,
        'PlayerStarts': MSB_PART_TYPE.PlayerStarts,
        'Collisions': MSB_PART_TYPE.Collision,
        'Navmeshes': MSB_PART_TYPE.Navmesh,
        'UnusedObjects': MSB_PART_TYPE.UnusedObject,
        'UnusedCharacters': MSB_PART_TYPE.UnusedCharacter,
        'MapLoadTriggers': MSB_PART_TYPE.MapLoadTrigger,
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
        'NPCInvasions': MSB_EVENT_TYPE.NPCInvasion,
    },
    'Regions': {
        'Points': MSB_REGION_TYPE.Point,
        'Circles': MSB_REGION_TYPE.Circle,
        'Spheres': MSB_REGION_TYPE.Sphere,
        'Cylinders': MSB_REGION_TYPE.Cylinder,
        'Rectangles': MSB_REGION_TYPE.Rect,
        'Boxes': MSB_REGION_TYPE.Box,
    },
    'Models': {
        'MapPieces': MSB_MODEL_TYPE.MapPiece,
        'Objects': MSB_MODEL_TYPE.Object,
        'NonHumanCharacters': MSB_MODEL_TYPE.NonHumanCharacter,
        'Unknown': MSB_MODEL_TYPE.Unknown,
        'HumanCharacters': MSB_MODEL_TYPE.HumanCharacter,
        'Collisions': MSB_MODEL_TYPE.Collision,
        'Navmeshes': MSB_MODEL_TYPE.Navmesh,
    },
}


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
        self._entries = []

        if msb_entry_list_source is None:
            return

        if isinstance(msb_entry_list_source, (list, tuple, dict)):
            if not name:
                raise ValueError("Name of MSB entry list must be given if created manually.")
            if name not in {'POINT_PARAM_ST', 'EVENT_PARAM_ST', 'PARTS_PARAM_ST', 'MODEL_PARAM_ST'}:
                raise ValueError("Name of MSB entry list must be MODEL_PARAM_ST, EVENT_PARAM_ST, POINT_PARAM_ST, "
                                 "or PARTS_PARAM_ST.")
            if isinstance(msb_entry_list_source, dict):
                msb_entry_list_source = [msb_entry_list_source[k] for k in sorted(msb_entry_list_source)]
            if isinstance(msb_entry_list_source, (list, tuple)):
                for entry in msb_entry_list_source:
                    if isinstance(entry, MSBEntry):
                        self._entries.append(entry)
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

        self._entries = []

        for entry_offset in entry_offsets:
            msb_buffer.seek(entry_offset)
            entry = self.ENTRY_CLASS(msb_buffer)
            self._entries.append(entry)

        msb_buffer.seek(next_entry_list_offset)

    def pack(self, start_offset=0, is_last_table=False):
        entries = self.get_entries()
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

    def __iter__(self):
        """Iterate over all entries."""
        return iter(self._entries)

    def __len__(self):
        """Count of all entries."""
        return len(self._entries)

    def __getitem__(self, entry_name_or_index) -> MSBEntry:
        """You can access entries using their enum, enum value, enum name, or pluralized name from MAP_ENTRY_TYPES."""
        if isinstance(entry_name_or_index, int):
            entry_index = entry_name_or_index
        elif isinstance(entry_name_or_index, str):
            entry_names = self.get_entry_names()
            entry_name_count = entry_names.count(entry_name_or_index)
            if entry_name_count > 1:
                raise ValueError(f"Entry name {entry_name_or_index} appears more than once in "
                                 f"{self.__class__.__name__}. You must access it by index.")
            elif entry_name_count == 0:
                raise ValueError(f"Entry name {entry_name_or_index} does not appear in {self.__class__.__name__}.")
            entry_index = entry_names.index(entry_name_or_index)
        else:
            raise TypeError(f"MSBEntryList key must be an entry index or entry name, not {entry_name_or_index}.")
        return self.get_entries()[entry_index]

    def get_entries(self, entry_type=None) -> list:
        if entry_type is None:
            return self._entries  # Full entry list, with types potentially intermingled.
        entry_type = self.resolve_entry_type(entry_type)
        return [e for e in self._entries if e.ENTRY_TYPE == entry_type]

    def get_entry_names(self, entry_type=None):
        """Returns an ordered list of entry names (global or type-specific).

        Note that only the global index (`entry_type=None`) is valid for index links from other MSB entries.
        """
        return [entry.name for entry in self.get_entries(entry_type=entry_type)]

    def get_entry_type(self, entry_name_or_index):
        """Returns type enum of given entry name or list-wide index."""
        return self[entry_name_or_index].ENTRY_TYPE

    def get_entry_type_index(self, entry_name_or_index):
        """Get index of entry name or global index, local to its type.

        Useful for obtaining the type-sorted display index for the GUI.
        """
        if isinstance(entry_name_or_index, int):  # Convert to name.
            entry_name_or_index = self[entry_name_or_index].name
        entry_type = self.get_entry_type(entry_name_or_index)
        return self.get_entry_names(entry_type).index(entry_name_or_index)

    def get_entry_global_index(self, entry_name_or_local_index, entry_type=None):
        """Get global index of entry with given name or index. If an index past the length of the given type sub-list
        is given, `None` is returned, which should be handled appropriately."""
        if isinstance(entry_name_or_local_index, int):
            if entry_type is None:
                raise ValueError("Cannot get global entry index from local index without specifying `entry_type`.")
            entry_type = self.resolve_entry_type(entry_type)
            entry_type_names = self.get_entry_names(entry_type)
            if entry_name_or_local_index >= len(entry_type_names):
                return None
            entry_name = entry_type_names[entry_name_or_local_index]
        else:
            entry_name = entry_name_or_local_index
        return self.get_entry_names().index(entry_name)

    def resolve_entry_type(self, entry_type):
        """Converts any valid entry type specification into the proper type enum."""
        if isinstance(entry_type, self.ENTRY_TYPE_ENUM):
            return entry_type
        try:
            if isinstance(entry_type, str):
                if entry_type in MAP_ENTRY_TYPES[self.ENTRY_LIST_NAME]:
                    return MAP_ENTRY_TYPES[self.ENTRY_LIST_NAME][entry_type]
                return getattr(self.ENTRY_TYPE_ENUM, entry_type)
            elif isinstance(entry_type, int):
                return self.ENTRY_TYPE_ENUM(entry_type)
            raise ValueError
        except ValueError:
            raise TypeError(f"Invalid entry type for entry list {self.ENTRY_LIST_NAME}: {entry_type}")

    def add_entry(self, global_index, entry):
        """Add entry at desired global index."""
        self._entries.insert(global_index, entry)

    def delete_entry(self, global_index):
        """Delete (and return) entry at desired global index."""
        return self._entries.pop(global_index)

    def duplicate_entry(self, entry_type, local_index, insert_below_original=False):
        source_entry = self.get_entries(entry_type)[local_index]
        duplicated = copy.deepcopy(source_entry)
        duplicated.name += ' <1>'  # TODO: Not nice if the source entry already has a repeated name.
        if insert_below_original:
            global_index = self.get_entry_global_index(source_entry.name)
            self._entries.insert(global_index + 1, duplicated)
        else:
            self._entries.append(duplicated)

    def get_indices(self):
        """Returns a dictionary mapping entry names to their global indices for resolving named links before repacking.

        Raises a NameError if the same name appears more than once in the entry list, which can only happen if you
        explicitly copy a name.
        """
        entry_indices = {}
        for i, entry in enumerate(self._entries):
            if entry.name in entry_indices:
                raise NameError(f"Name {repr(entry.name)} appears more than once in MSB.")
            entry_indices[entry.name] = i
        return entry_indices

    def set_and_get_unique_names(self):
        """Goes through all entries and assigns <repeat> suffixes to any repeated names, so that every entry has
        a unique name for name linking purposes. These suffixes will be removed when the MSB is packed.

        Returns a dictionary mapping entry indices to those new unique names.
        """
        unique_names = {}
        repeat_count = {}
        for i, entry in enumerate(self._entries):
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

    _entries: List[MSBModel]

    MapPieces: list
    Objects: list
    Characters: list
    Players: list
    Collisions: list
    Navmeshes: list

    def set_indices(self, part_instance_counts):
        """Local type-specific index only. (Note that global entry index is still used by Parts.)"""
        type_indices = {}
        for entry in self._entries:
            entry.set_indices(model_type_index=type_indices.setdefault(entry.ENTRY_TYPE, 0),
                              instance_count=part_instance_counts.get(entry.name, 0))
            type_indices[entry.ENTRY_TYPE] += 1

    def __iter__(self) -> Iterator[MSBModel]:
        """Iterate over all entries."""
        return iter(self._entries)


class MSBEventList(MSBEntryList):
    ENTRY_LIST_NAME = 'Events'
    ENTRY_CLASS = staticmethod(MSBEvent)
    ENTRY_TYPE_ENUM = MSB_EVENT_TYPE

    _entries: List[MSBEvent]

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
    NPCInvasions: list

    def set_names(self, region_names, part_names):
        for entry in self._entries:
            entry.set_names(region_names, part_names)

    def set_indices(self, region_indices, part_indices):
        """Global and type-specific indices both set. (Unclear if either of them do anything.)"""
        type_indices = {}
        for i, entry in enumerate(self._entries):
            entry.set_indices(event_index=i, local_event_index=type_indices.setdefault(entry.ENTRY_TYPE, 0),
                              region_indices=region_indices, part_indices=part_indices)
            type_indices[entry.ENTRY_TYPE] += 1

    def __iter__(self) -> Iterator[BaseMSBEvent]:
        """Iterate over all entries."""
        return iter(self._entries)


class MSBRegionList(MSBEntryList):
    ENTRY_LIST_NAME = 'Regions'
    ENTRY_CLASS = staticmethod(MSBRegion)
    ENTRY_TYPE_ENUM = MSB_REGION_TYPE

    _entries: List[MSBRegion]

    Points: list
    Circles: list
    Spheres: list
    Cylinders: list
    Rectangles: list
    Boxes: list

    def set_indices(self):
        """Global region index only."""
        for i, entry in enumerate(self._entries):
            entry.set_indices(region_index=i)

    def __iter__(self) -> Iterator[BaseMSBRegion]:
        """Iterate over all entries."""
        return iter(self._entries)


class MSBPartList(MSBEntryList):
    ENTRY_LIST_NAME = 'Parts'
    ENTRY_CLASS = staticmethod(MSBPart)
    ENTRY_TYPE_ENUM = MSB_PART_TYPE

    _entries: List[BaseMSBPart]

    MapPieces: list
    Objects: list
    Characters: list
    PlayerStarts: list
    Collisions: list
    Navmeshes: list
    UnusedObjects: list
    UnusedCharacters: list
    MapLoadTriggers: list

    def set_names(self, model_names, region_names, part_names, collision_names):
        for entry in self._entries:
            entry.set_names(model_names, region_names, part_names, collision_names)

    def set_indices(self, model_indices, region_indices, part_indices, local_collision_indices):
        """Local type-specific index only.

        Events and other Parts may point to Parts by global entry index, but it seems the local index still matters, as
        ObjAct Events seem to break when the local object index is changed. It's possible this was just an idiosyncrasy
        of Wulf's MSB Editor. Either way, this method should ensure the global and local indices are consistent.

        Note that cutscene files (remo) access Parts by index as well.

        `local_collision_indices` are needed for Map Load Triggers. No other MSB entry type requires local indices.
        """
        type_indices = {}
        for entry in self._entries:
            entry.set_indices(part_type_index=type_indices.setdefault(entry.ENTRY_TYPE, 0),
                              model_indices=model_indices, region_indices=region_indices, part_indices=part_indices,
                              local_collision_indices=local_collision_indices)
            type_indices[entry.ENTRY_TYPE] += 1

    def get_instance_counts(self):
        """Returns a dictionary mapping model names to part instance counts."""
        instance_counts = {}
        for entry in self._entries:
            instance_counts.setdefault(entry.model_name, 0)
            instance_counts[entry.model_name] += 1
        return instance_counts

    def __iter__(self) -> Iterator[BaseMSBPart]:
        """Iterate over all entries."""
        return iter(self._entries)


# Set up shortcut attributes to sorted entry type lists (e.g. `MSBPartList.Characters`).
for cls in (MSBModelList, MSBEventList, MSBRegionList, MSBPartList):
    for entry_type_name, entry_type_enum in MAP_ENTRY_TYPES[cls.ENTRY_LIST_NAME].items():
        setattr(cls, entry_type_name, property(
            lambda self: [e for e in self._entries if e.ENTRY_TYPE == entry_type_enum]))


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
        elif isinstance(msb_source, (str, Path)):
            # File path.
            self.msb_path = Path(msb_source)
            with self.msb_path.open('rb') as msb_buffer:
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
        collision_names = self.parts.get_entry_names(MSB_PART_TYPE.Collision)

        self.events.set_names(region_names=region_names, part_names=part_names)
        self.parts.set_names(model_names=model_names, region_names=region_names, part_names=part_names,
                             collision_names=collision_names)

    def pack(self):
        """Constructs {name: id} dictionaries, then passes them to pack() methods as required by each."""
        model_indices = self.models.get_indices()
        region_indices = self.regions.get_indices()
        part_indices = self.parts.get_indices()
        local_collision_indices = {name: i for i, name in enumerate(
            self.parts.get_entry_names(MSB_PART_TYPE.Collision))}

        # Set entry indices (both self and linked) and other auto-detected fields.
        self.models.set_indices(part_instance_counts=self.parts.get_instance_counts())
        self.events.set_indices(region_indices=region_indices, part_indices=part_indices)
        self.regions.set_indices()
        self.parts.set_indices(model_indices=model_indices, region_indices=region_indices, part_indices=part_indices,
                               local_collision_indices=local_collision_indices)

        offset = 0
        packed_models = self.models.pack(start_offset=offset)
        offset += len(packed_models)
        packed_events = self.events.pack(start_offset=offset)
        offset += len(packed_events)
        packed_regions = self.regions.pack(start_offset=offset)
        offset += len(packed_regions)
        packed_parts = self.parts.pack(start_offset=offset, is_last_table=True)

        return packed_models + packed_events + packed_regions + packed_parts

    def write_packed(self, msb_path=None):
        if msb_path is None:
            if self.msb_path is None:
                raise ValueError("MSB path cannot be automatically determined from instance source.")
            msb_path = self.msb_path
        if isinstance(msb_path, str):
            msb_path = Path(msb_path)
        create_bak(msb_path)
        with msb_path.open('wb') as f:
            f.write(self.pack())

    def translate_all(self, translate):
        """Offset translations of all regions and parts by given input.

        The input value can be anything that can be added to a Vector.
        """
        for p in self.parts:
            p.translate += translate
        for r in self.regions:
            r.translate += translate

    def __getitem__(self, entry_list_name) -> MSBEntryList:
        if entry_list_name.lower() not in {'models', 'events', 'regions', 'parts'}:
            raise ValueError(f"{entry_list_name} is not a valid MSB entry list.")
        return getattr(self, entry_list_name.lower())

    def __iter__(self):
        return iter((self.models, self.events, self.regions, self.parts))
