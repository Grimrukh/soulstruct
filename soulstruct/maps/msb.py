import logging
import typing as tp
from io import BytesIO, BufferedReader
from pathlib import Path

from soulstruct.maps.core import MAP_ENTRY_TYPES
from soulstruct.maps.base import MSBEntryList, MSBEntry
from soulstruct.maps.models import MSBModelList
from soulstruct.maps.events import MSBEventList
from soulstruct.maps.core import MSB_EVENT_TYPE, MSB_PART_TYPE, MSB_REGION_TYPE
from soulstruct.maps.regions import MSBRegionList
from soulstruct.maps.parts import MSBPartList
from soulstruct.utilities.core import BiDict, create_bak
from soulstruct.utilities.maths import Vector3, Matrix3

_LOGGER = logging.getLogger(__name__)

# Subset of the above, only for entry types with entity IDs.
MAP_ENTRY_ENTITY_TYPES = {
    'Parts': BiDict(
        ('MapPieces', MSB_PART_TYPE.MapPiece),
        ('Objects', MSB_PART_TYPE.Object),
        ('Characters', MSB_PART_TYPE.Character),
        ('PlayerStarts', MSB_PART_TYPE.PlayerStart),
        ('Collisions', MSB_PART_TYPE.Collision),
    ),
    'Events': BiDict(
        ('Sounds', MSB_EVENT_TYPE.Sound),
        ('FX', MSB_EVENT_TYPE.FX),
        ('Spawners', MSB_EVENT_TYPE.Spawner),
        ('Messages', MSB_EVENT_TYPE.Message),
        ('ObjActs', MSB_EVENT_TYPE.ObjAct),
        ('SpawnPoints', MSB_EVENT_TYPE.SpawnPoint),
        ('Navigation', MSB_EVENT_TYPE.Navigation),
    ),
    'Regions': BiDict(
        ('Points', MSB_REGION_TYPE.Point),
        ('Circles', MSB_REGION_TYPE.Circle),
        ('Spheres', MSB_REGION_TYPE.Sphere),
        ('Cylinders', MSB_REGION_TYPE.Cylinder),
        ('Rectangles', MSB_REGION_TYPE.Rect),
        ('Boxes', MSB_REGION_TYPE.Box),
    ),
}

# Set up shortcut attributes to sorted entry type lists (e.g. `MSBPartList.Characters`).
for cls in (MSBModelList, MSBEventList, MSBRegionList, MSBPartList):
    for entry_type_name, entry_type_enum in MAP_ENTRY_TYPES[cls.ENTRY_LIST_NAME].items():
        setattr(cls, entry_type_name, property(
            lambda self, enum=entry_type_enum: [e for e in self._entries if e.ENTRY_TYPE == enum]))


class MSB(object):
    """Handles MSB ('MapStudio') data for Dark Souls 1.

    Only DS1 (either version) is supported. PTDE and DSR have identical MSB formats (but a few changes in content).

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
        print(f"MSB saved: {str(msb_path)}")  # todo: remove

    def translate_all(self, translate: tp.Union[Vector3, list, tuple], selected_entries=None):
        """Add given `translate` to `.translate` vectors of all Regions and Parts (including Map Pieces, Collisions, and
        Navmeshes) by given XYZ. Optionally, only apply it to `selected_entry_names`.
        """
        for p in self.parts:
            if selected_entries is None or p in selected_entries:
                p.translate += translate
        for r in self.regions:
            if selected_entries is None or r in selected_entries:
                r.translate += translate

    def rotate_all_in_world(self, rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float],
                            pivot_point=(0, 0, 0), radians=False, selected_entries=None):
        """Rotate every Part and Region in the map (or a selection given in `selected_entry_names`) around the given
        pivot by the given Euler angles coordinate system, modifying both `translate` and `rotate`.

        The pivot defaults to the world origin.
        """
        if isinstance(rotation, (int, float)):
            rotation = Matrix3.from_euler_angles(0.0, rotation, 0.0)  # single rotation value interpreted as Y rotation
        elif isinstance(rotation, (Vector3, list, tuple)):
            rotation = Matrix3.from_euler_angles(rotation)
        elif not isinstance(rotation, Matrix3):
            raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")
        pivot_point = Vector3(pivot_point)
        for p in self.parts:
            if selected_entries is None or p in selected_entries:
                p.rotate_in_world(rotation, pivot_point=pivot_point, radians=radians)
        for r in self.regions:
            if selected_entries is None or r in selected_entries:
                r.rotate_in_world(rotation, pivot_point=pivot_point, radians=radians)

    def move_map(self,
                 start_translate: tp.Union[Vector3, list, tuple] = None,
                 end_translate: tp.Union[Vector3, list, tuple] = None,
                 start_rotate: tp.Union[Vector3, list, tuple, int, float, None] = None,
                 end_rotate: tp.Union[Vector3, list, tuple, int, float, None] = None,
                 selected_entries=None):
        """Rotate and then translate entire map so that an entity with a translate of `start_translate` and rotate of
        `start_rotate` ends up with a translate of `end_translate` and a rotate of `end_rotate`.

        Optionally, move only a subset of entry names given in `selected_entry_names`.
        """
        if selected_entries is not None:
            selected_entries = list(selected_entries)  # so strings can be replaced with part instances
            for i, entry in enumerate(selected_entries):
                if isinstance(entry, str):
                    selected_entries[i] = self.parts.get_part_by_name(entry)
                elif not isinstance(entry, MSBEntry):
                    raise TypeError("`selected_entries` should contain only `MSBEntry` instances or Part names.")

        if start_translate is None:
            start_translate = Vector3.zero()
        elif not isinstance(start_translate, Vector3):
            start_translate = Vector3(start_translate)
        if end_translate is None:
            end_translate = Vector3.zero()
        elif not isinstance(end_translate, Vector3):
            end_translate = Vector3(end_translate)
        if start_rotate is None:
            start_rotate = Vector3.zero()
        elif isinstance(start_rotate, (int, float)):
            start_rotate = Vector3(0, start_rotate, 0)
        else:
            start_rotate = Vector3(start_rotate)
        if end_rotate is None:
            end_rotate = Vector3.zero()
        elif isinstance(end_rotate, (int, float)):
            end_rotate = Vector3(0, end_rotate, 0)
        else:
            end_rotate = Vector3(end_rotate)

        # Compute global rotation matrix required to get from `start_rotate` to `end_rotate`.
        m_start_rotate = Matrix3.from_euler_angles(start_rotate)
        m_end_rotate = Matrix3.from_euler_angles(end_rotate)
        m_world_rotate = m_end_rotate @ m_start_rotate.T
        # Apply global rotation to start point to determine required global translation.
        translation = end_translate - (m_world_rotate @ start_translate)  # type: Vector3

        self.rotate_all_in_world(m_world_rotate, selected_entries=selected_entries)
        self.translate_all(translation, selected_entries=selected_entries)

    def get_entity_id_dict(self, entry_list_name, entry_type, names_only=False):
        """Get a dictionary mapping entity IDs to MSBEntry instances for the given list and type.

        Optionally returns dictionary mapping ID to MSBEntry `name` only.

        If multiple MSBEntry instances are found for a given ID, only the *first* one found is used.
        """
        entry_list_name = entry_list_name.lower()
        if entry_list_name == 'parts':
            entries = self.parts.get_entries(entry_type)
        elif entry_list_name == 'events':
            entries = self.events.get_entries(entry_type)
        elif entry_list_name == 'regions':
            entries = self.regions.get_entries(entry_type)
        else:
            raise ValueError("Can only get entity IDs for parts, events, and regions.")
        entries_by_id = {}
        for entry in [e for e in entries if e.entity_id > 0]:
            if entry.entity_id in entries_by_id:
                _LOGGER.debug(f"Found multiple entries for entity ID {entry.entity_id}. Only using first.")
            else:
                entries_by_id[entry.entity_id] = entry.name if names_only else entry
        return entries_by_id

    def get_entity_id(self, entity_id: int, allow_multiple=True) -> tp.Optional[MSBEntry]:
        """Search all entry types for the given ID and return that MSBEntry (or None if not found).

        If multiple entries with the same (non-default) ID are found, an error will be raised.
        """
        if entity_id <= 0:
            raise ValueError(f"MSB entity ID cannot be less than zero ({entity_id}).")
        results = []
        for entry_list_name in ("parts", "events", "regions"):
            results += [e for e in self[entry_list_name].get_entries() if e.entity_id == entity_id]
        if not results:
            return None
        elif len(results) > 1:
            if allow_multiple:
                return results
            raise ValueError(f"Found multiple entries with entity ID {entity_id} in MSB. This should not happen.")
        return results[0]

    def __getitem__(self, entry_list_name) -> MSBEntryList:
        if entry_list_name.lower() not in {'models', 'events', 'regions', 'parts'}:
            raise ValueError(f"{entry_list_name} is not a valid MSB entry list.")
        return getattr(self, entry_list_name.lower())

    def __iter__(self):
        return iter((self.models, self.events, self.regions, self.parts))


if __name__ == '__main__':
    from soulstruct import PTDE_PATH
    depths = MSB(PTDE_PATH + "/map/MapStudio/m10_00_00_00.msb")
