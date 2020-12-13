from __future__ import annotations

import abc
import logging
import typing as tp
from io import BytesIO, BufferedReader
from pathlib import Path

from soulstruct.maps.enums import MSBEventSubtype, MSBPartSubtype
from soulstruct.utilities import create_bak
from soulstruct.utilities.maths import Vector3, Matrix3

from .msb_entry import MSBEntry

if tp.TYPE_CHECKING:
    from .msb_entry import MSBEntryList, MSBEntryEntity
    from .models import MSBModelList
    from .events import MSBEventList
    from .regions import MSBRegionList
    from .parts import MSBPartList

_LOGGER = logging.getLogger(__name__)


class MSB(abc.ABC):
    """Handles MSB ('MapStudio') data. Subclassed by each game.

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
    HEADER = b""

    MODEL_LIST_CLASS = NotImplemented  # type: tp.Type[MSBModelList]
    EVENT_LIST_CLASS = NotImplemented  # type: tp.Type[MSBEventList]
    REGION_LIST_CLASS = NotImplemented  # type: tp.Type[MSBRegionList]
    PART_LIST_CLASS = NotImplemented  # type: tp.Type[MSBPartList]

    def __init__(self, msb_source=None):
        self.models = self.MODEL_LIST_CLASS()
        self.events = self.EVENT_LIST_CLASS()
        self.regions = self.REGION_LIST_CLASS()
        self.parts = self.PART_LIST_CLASS()

        self.msb_path = None

        if msb_source is None:
            return
        elif isinstance(msb_source, (str, Path)):
            # File path.
            self.msb_path = Path(msb_source)
            with self.msb_path.open("rb") as msb_buffer:
                self.unpack(msb_buffer)
        elif isinstance(msb_source, bytes):
            self.unpack(BytesIO(msb_source))
        elif isinstance(msb_source, BufferedReader):
            self.unpack(msb_source)
        else:
            raise TypeError(
                f"Invalid MSB source type: {type(msb_source)}. " f"Must be string (file path), bytes, or buffer."
            )

    def unpack(self, msb_buffer):
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

        offset = 0
        packed_models = self.models.pack(start_offset=offset)
        offset += len(packed_models)
        packed_events = self.events.pack(start_offset=offset)
        offset += len(packed_events)
        packed_regions = self.regions.pack(start_offset=offset)
        offset += len(packed_regions)
        packed_parts = self.parts.pack(start_offset=offset, is_last_table=True)

        return self.HEADER + packed_models + packed_events + packed_regions + packed_parts

    def write_packed(self, msb_path=None):
        if msb_path is None:
            if self.msb_path is None:
                raise ValueError("MSB path cannot be automatically determined from instance source.")
            msb_path = self.msb_path
        if isinstance(msb_path, str):
            msb_path = Path(msb_path)
        msb_path.parent.mkdir(parents=True, exist_ok=True)
        create_bak(msb_path)
        with msb_path.open("wb") as f:
            f.write(self.pack())

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

    def rotate_all_in_world(
        self,
        rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float],
        pivot_point=(0, 0, 0),
        radians=False,
        selected_entries=None,
    ):
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

    def move_map(
        self,
        start_translate: tp.Union[Vector3, list, tuple] = None,
        end_translate: tp.Union[Vector3, list, tuple] = None,
        start_rotate: tp.Union[Vector3, list, tuple, int, float, None] = None,
        end_rotate: tp.Union[Vector3, list, tuple, int, float, None] = None,
        selected_entries=None,
    ):
        """Rotate and then translate entire map so that an entity with a translate of `start_translate` and rotate of
        `start_rotate` ends up with a translate of `end_translate` and a rotate of `end_rotate`.

        Optionally, move only a subset of entry names given in `selected_entry_names`.
        """
        if selected_entries is not None:
            selected_entries = list(selected_entries)  # so strings can be replaced with part instances
            for i, entry in enumerate(selected_entries):
                if isinstance(entry, str):
                    try:
                        selected_part = self.parts.get_entry_by_name(entry)
                    except KeyError:
                        selected_part = None
                    try:
                        selected_region = self.regions.get_entry_by_name(entry)
                    except KeyError:
                        selected_region = None
                    if selected_part and selected_region:
                        raise ValueError(
                            f"Found both a Part and Region with name '{entry}'. You must pass the desired entry "
                            f"instance directly.")
                    elif selected_part:
                        selected_entries[i] = selected_part
                    elif selected_region:
                        selected_entries[i] = selected_region
                    else:
                        raise ValueError(f"Could not find a Part or Region named '{entry}' in MSB.")
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
        if entry_type == "parts":
            entries = self.parts.get_entries(entry_subtype)
        elif entry_type == "events":
            entries = self.events.get_entries(entry_subtype)
        elif entry_type == "regions":
            entries = self.regions.get_entries(entry_subtype)
        else:
            raise ValueError("Can only get entity IDs for parts, events, and regions.")
        entries_by_id = {}
        for entry in [e for e in entries if e.entity_id > 0]:
            if entry.entity_id in entries_by_id:
                _LOGGER.warning(f"Found multiple entries for entity ID {entry.entity_id}. Only using first.")
            else:
                entries_by_id[entry.entity_id] = entry.name if names_only else entry
        return entries_by_id

    def get_entry_with_entity_id(self, entity_id: int, allow_multiple=True) -> tp.Optional[MSBEntryEntity]:
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

    def __getitem__(self, entry_list_name) -> MSBEntryList:
        if entry_list_name.lower() not in {"models", "events", "regions", "parts"}:
            raise ValueError(f"{entry_list_name} is not a valid MSB entry list.")
        return getattr(self, entry_list_name.lower())

    def __iter__(self):
        return iter((self.models, self.events, self.regions, self.parts))
