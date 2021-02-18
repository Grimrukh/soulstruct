from __future__ import annotations

import abc
import logging
import typing as tp
import io
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.maths import Vector3, Matrix3, resolve_rotation

from .enums import MSBSubtype, MSBEventSubtype, MSBPartSubtype
from soulstruct.base.maps.msb.msb_entry import MSBEntry

if tp.TYPE_CHECKING:
    from soulstruct.base.maps.msb.msb_entry import MSBEntryList, MSBEntryEntity
    from soulstruct.base.maps.msb.models import MSBModelList
    from soulstruct.base.maps.msb.events import MSBEventList
    from soulstruct.base.maps.msb.regions import MSBRegionList
    from soulstruct.base.maps.msb.parts import MSBPartList

_LOGGER = logging.getLogger(__name__)


class MSB(GameFile, abc.ABC):
    """Handles MSB ('MapStudio') data. Subclassed by each game.

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
    EXT = ".msb"

    HEADER = b""

    MODEL_LIST_CLASS = None  # type: tp.Type[MSBModelList]
    EVENT_LIST_CLASS = None  # type: tp.Type[MSBEventList]
    REGION_LIST_CLASS = None  # type: tp.Type[MSBRegionList]
    PART_LIST_CLASS = None  # type: tp.Type[MSBPartList]

    def __init__(
        self,
        msb_source: tp.Union[None, str, Path, bytes, io.BufferedIOBase] = None,
        dcx_magic: tuple[int, int] = None,
    ):
        self.models = self.MODEL_LIST_CLASS()
        self.events = self.EVENT_LIST_CLASS()
        self.regions = self.REGION_LIST_CLASS()
        self.parts = self.PART_LIST_CLASS()
        self.dcx_magic = ()
        super().__init__(msb_source, dcx_magic=dcx_magic)

    def unpack(self, msb_buffer, **kwargs):
        """Unpack an MSB from the given buffer."""

        # Read (and ignore) constant header, if applicable.
        if self.HEADER:
            msb_buffer.seek(msb_buffer.tell() + len(self.HEADER))

        self.models = self.MODEL_LIST_CLASS(msb_buffer)
        self.events = self.EVENT_LIST_CLASS(msb_buffer)
        self.regions = self.REGION_LIST_CLASS(msb_buffer)
        self.parts = self.PART_LIST_CLASS(msb_buffer)

        model_names = self.models.set_and_get_unique_names()
        environment_names = self.events.get_entry_names(MSBEventSubtype.Environment)
        region_names = self.regions.set_and_get_unique_names()
        part_names = self.parts.set_and_get_unique_names()
        collision_names = self.parts.get_entry_names(MSBPartSubtype.Collision)

        self.events.set_names(region_names=region_names, part_names=part_names)
        self.parts.set_names(
            model_names=model_names,
            environment_names=environment_names,
            region_names=region_names,
            part_names=part_names,
            collision_names=collision_names,
        )

    def pack(self):
        """Constructs {name: id} dictionaries, then passes them to pack() methods as required by each."""
        model_indices = self.models.get_indices()
        local_environment_indices = {
            name: i for i, name in enumerate(self.events.get_entry_names(MSBEventSubtype.Environment))
        }
        region_indices = self.regions.get_indices()
        part_indices = self.parts.get_indices()
        local_collision_indices = {
            name: i for i, name in enumerate(self.parts.get_entry_names(MSBPartSubtype.Collision))
        }

        # Set entry indices (both self and linked) and other auto-detected fields.
        self.models.set_indices(part_instance_counts=self.parts.get_instance_counts())
        self.events.set_indices(region_indices=region_indices, part_indices=part_indices)
        self.regions.set_indices()
        self.parts.set_indices(
            model_indices=model_indices,
            local_environment_indices=local_environment_indices,
            region_indices=region_indices,
            part_indices=part_indices,
            local_collision_indices=local_collision_indices,
        )

        offset = len(self.HEADER)
        packed_models = self.models.pack(start_offset=offset)
        offset += len(packed_models)
        packed_events = self.events.pack(start_offset=offset)
        offset += len(packed_events)
        packed_regions = self.regions.pack(start_offset=offset)
        offset += len(packed_regions)
        packed_parts = self.parts.pack(start_offset=offset, is_last_table=True)

        return self.HEADER + packed_models + packed_events + packed_regions + packed_parts

    def get_entry_by_name(self, name: str, entry_types=()):
        """Get `MSBEntry` with name `name` that is one of the given `entry_types`, or any type if `entry_types=()`."""
        if not entry_types:
            entry_types = ("parts", "regions", "events", "models")
        results = {}
        for entry_type in entry_types:
            try:
                # This will raise a `ValueError` if the name appears more than once in a single entry type list.
                results[entry_type.lower()] = self[entry_type].get_entry_by_name(name)
            except KeyError:
                pass
        if not results:
            raise ValueError(f"Could not find an entry named '{name}' with type {entry_types} in MSB.")
        if len(results) > 1:
            raise ValueError(f"Found entries of multiple types with name '{name}': {list(results)}")
        return next(iter(results.values()))

    def resolve_entries_list(self, entries, entry_types=()):
        """Lists of entries can include names of entries, if unique, or the actual `MSBEntry` instances."""
        resolved = []
        for entry in entries:
            if isinstance(entry, str):
                resolved.append(self.get_entry_by_name(entry, entry_types))
            elif isinstance(entry, MSBEntry):
                resolved.append(entry)
            else:
                raise TypeError(f"Invalid entry specifier: {entry}. Must be a (unique) entry name or instance.")
        return resolved

    def get_repeated_entity_ids(self):
        repeats = {}
        for entry_type in ("Parts", "Regions", "Events"):
            entries = getattr(self, entry_type.lower())
            entity_ids = set()
            repeated_entries = []
            for entry in [e for e in entries if e.entity_id > 0]:
                if entry.entity_id in entity_ids:
                    repeated_entries.append(entry)
                else:
                    entity_ids.add(entry.entity_id)
            repeats[entry_type] = repeated_entries
        return repeats

    def get_entity_id_dict(self, entry_type, entry_subtype, names_only=False):
        """Get a dictionary mapping entity IDs to `MSBEntry` instances for the given type and subtype.

        Optionally returns dictionary mapping ID to `MSBEntry.name` only.

        If multiple `MSBEntry` instances are found for a given ID, a warning is logged, and only the *first* one found
        is used (which matches game engine behavior).
        """
        entry_type = entry_type.lower()
        if entry_type in {"parts", "events", "regions"}:
            entries = self[entry_type].get_entries(entry_subtype)
        else:
            raise ValueError("Can only get entity IDs for parts, events, and regions.")
        entries_by_id = {}
        for entry in [e for e in entries if e.entity_id > 0]:
            if entry.entity_id in entries_by_id:
                _LOGGER.warning(f"Found multiple entries for entity ID {entry.entity_id}. Only using first.")
            else:
                entries_by_id[entry.entity_id] = entry.name if names_only else entry
        return entries_by_id

    def get_entry_by_entity_id(self, entity_id: int, allow_multiple=True) -> tp.Optional[MSBEntryEntity]:
        """Search all entry types for the given ID and return that `MSBEntry` (or `None` if not found).

        If multiple entries with the same (non-default) ID are found, an error will be raised.
        """
        if entity_id <= 0:
            raise ValueError(f"MSB entity ID cannot be less than zero ({entity_id}).")
        results = [e for e in self.parts.get_entries() if e.entity_id == entity_id]
        results += [e for e in self.events.get_entries() if e.entity_id == entity_id]
        results += [e for e in self.regions.get_entries() if e.entity_id == entity_id]
        if not results:
            return None
        elif len(results) > 1:
            if allow_multiple:
                _LOGGER.warning(
                    f"Found multiple entries with entity ID {entity_id} in MSB. This should not happen. "
                    f"Returning first one only."
                )
            else:
                raise ValueError(f"Found multiple entries with entity ID {entity_id} in MSB. This should not happen.")
        return results[0]

    def move_map(
        self,
        start_translate: tp.Union[Vector3, list, tuple] = None,
        end_translate: tp.Union[Vector3, list, tuple] = None,
        start_rotate: tp.Union[Vector3, list, tuple, int, float, None] = None,
        end_rotate: tp.Union[Vector3, list, tuple, int, float, None] = None,
        selected_entries=(),
    ):
        """Move everything with a transform in this `MSB` relative to an initial and a final reference point.

        Args:
            start_translate: initial `(x, y, z)` translate of initial reference point.
            end_translate: final `(x, y, z)` translate of final reference point.
            start_rotate: initial `(x, y, z)` rotate of initial reference point, or simply `y` if a number is given.
            end_rotate: final `(x, y, z)` rotate of final reference point, or simply `y` if a number is given.
            selected_entries: if not empty, move only these given entries. Each element in this sequence can be
                an `MSBEntry` instance or the name (if unique) of a Part or Region.

        Optionally, move only a subset of entry names given in `selected_entry_names`.
        """
        selected_entries = self.resolve_entries_list(selected_entries, entry_types=("parts", "regions"))

        start_translate = Vector3(start_translate)
        end_translate = Vector3(end_translate)
        start_rotate = Vector3(0, start_rotate, 0) if isinstance(start_rotate, (int, float)) else Vector3(start_rotate)
        end_rotate = Vector3(0, end_rotate, 0) if isinstance(end_rotate, (int, float)) else Vector3(end_rotate)

        # Compute global rotation matrix required to get from `start_rotate` to `end_rotate`.
        m_start_rotate = Matrix3.from_euler_angles(start_rotate)
        m_end_rotate = Matrix3.from_euler_angles(end_rotate)
        m_world_rotation = m_end_rotate @ m_start_rotate.T
        # Apply global rotation to start point to determine required global translation.
        translation = end_translate - (m_world_rotation @ start_translate)  # type: Vector3

        self.rotate_all_in_world(m_world_rotation, selected_entries=selected_entries)
        self.translate_all(translation, selected_entries=selected_entries)

    def rotate_all_in_world(
        self,
        rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float],
        pivot_point=(0, 0, 0),
        radians=False,
        selected_entries=(),
    ):
        """Rotate every Part and Region in the map around the given `pivot_point` by the Euler angles specified by
        `rotation`, modifying both `.rotate` and (unless equal to `pivot_point`) `.translate` for each entry.

        Args:
            rotation: Euler angles, as specified by `(x, y, z)`, an Euler rotation matrix, or a single value to apply
                simple `y` rotation only.
            pivot_point: point around with `rotation` will be applied. Defaults to world origin, `(0, 0, 0)`.
            radians: if True, given `rotation` is in radians; degrees otherwise. Defaults to `False` (degrees).
            selected_entries: if not empty, move only these given entries. Each element in this sequence can be
                an `MSBEntry` instance or the name (if unique) of a Part or Region.
        """
        selected_entries = self.resolve_entries_list(selected_entries, entry_types=("parts", "regions"))

        rotation = resolve_rotation(rotation)
        pivot_point = Vector3(pivot_point)
        for part in self.parts:
            if not selected_entries or part in selected_entries:
                part.apply_rotation(rotation, pivot_point=pivot_point, radians=radians)
        for region in self.regions:
            if not selected_entries or region in selected_entries:
                region.apply_rotation(rotation, pivot_point=pivot_point, radians=radians)

    def translate_all(self, translate: tp.Union[Vector3, list, tuple], selected_entries=()):
        """Add given `translate` vector to `.translate` vector attributes of all Regions and Parts.

        Args:
            translate: `(x, y, z)` vector to shift entries by.
            selected_entries: if not empty, move only these given entries. Each element in this sequence can be
                an `MSBEntry` instance or the name (if unique) of a Part or Region.
        """
        selected_entries = self.resolve_entries_list(selected_entries, entry_types=("parts", "regions"))

        for part in self.parts:
            if not selected_entries or part in selected_entries:
                part.translate += translate
        for region in self.regions:
            if not selected_entries or region in selected_entries:
                region.translate += translate

    @classmethod
    def get_subtype_dict(cls) -> dict[str, tuple[MSBSubtype]]:
        """Return a nested dictionary mapping MSB type names (in typical display order) to tuples of subtype enums."""
        return {
            "Parts": tuple(cls.PART_LIST_CLASS.SUBTYPE_CLASSES),
            "Regions": tuple(cls.REGION_LIST_CLASS.SUBTYPE_CLASSES),
            "Events": tuple(cls.EVENT_LIST_CLASS.SUBTYPE_CLASSES),
            "Models": tuple(cls.MODEL_LIST_CLASS.SUBTYPE_CLASSES),
        }

    def __getitem__(self, entry_list_name) -> MSBEntryList:
        """Retrieve entry list by name. Can be plural, like "parts", or singular, like "part"."""
        entry_list_name = entry_list_name.lower()
        if entry_list_name in {"model", "event", "region", "part"}:
            entry_list_name += "s"
        elif entry_list_name not in {"models", "events", "regions", "parts"}:
            raise ValueError(f"{entry_list_name} is not a valid MSB entry list.")
        return getattr(self, entry_list_name.lower())

    def __iter__(self):
        return iter((self.models, self.events, self.regions, self.parts))
