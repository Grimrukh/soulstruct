from __future__ import annotations

__all__ = ["MSB"]

import abc
import logging
import re
import struct
import typing as tp
from dataclasses import dataclass, fields
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.base.game_types.map_types import MapEntity
from soulstruct.utilities.binary import *
from soulstruct.utilities.maths import Vector3, Matrix3, resolve_rotation

from .msb_entry import MSBEntry
from .events import BaseMSBEvent
from .models import BaseMSBModel
from .parts import BaseMSBPart
from .regions import BaseMSBRegion

try:
    Self = tp.Self
except AttributeError:
    Self = "MSB"

if tp.TYPE_CHECKING:
    from .enums import BaseMSBSubtype
    from .msb_entry_list import *

_LOGGER = logging.getLogger(__name__)


MAP_NAME_RE = re.compile(r"m(\d\d)_(\d\d)_.*")
PY_NAME_RE = re.compile(r"^[A-z_][\w_]*$")  # valid Python variable name


# NOTE: Completely absent in DS1 and earlier.
MSB_HEADER_BYTES = struct.pack("4sII??BB", b"MSB ", 1, 16, False, False, 1, 255)
MSB_ENTRY_SUPERTYPES = {
    "MODEL_PARAM_ST": BaseMSBModel,
    "EVENT_PARAM_ST": BaseMSBEvent,
    "POINT_PARAM_ST": BaseMSBRegion,
    "PARTS_PARAM_ST": BaseMSBPart,
}


class MSBSubtypeInfo(tp.NamedTuple):
    index: int
    entry_class: tp.Type[MSBEntry]
    msb_list_attr_name: str
    plural_name: str


# Utility tuples that hold combined information mapping inter-entry indices to `MSBEntry` instances, and vice versa.
# Only used transiently when unpacking/packing to prevent hideous function signatures.
class PartObjectsToIndices(tp.NamedTuple):
    part_type_index: int  # TODO: I used this as an 'easy' way to set part subtype indices ('_part_type_index'). Dump.
    models: dict[MSBEntry, int]
    environments: dict[MSBEntry, int]  # subtype indices
    regions: dict[MSBEntry, int]
    parts: dict[MSBEntry, int]
    collisions: dict[MSBEntry, int]  # subtype indices


class IndexedEntryLists(tp.NamedTuple):
    models: list[MSBEntry]
    events: list[MSBEntry]
    regions: list[MSBEntry]
    parts: list[MSBEntry]
    environments: list[MSBEntry]  # event subtype
    collisions: list[MSBEntry]  # part subtype


@dataclass(slots=True)
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
    EXT: tp.ClassVar[str] = ".msb"

    # TODO: Lots of info needed here.
    #  - Each superlist needs to know the offset to check for subtype int.
    #  - Need to map subtype int to subtype class.
    #   - Don't need a subtype enum anymore, really? Just dictionaries that map int <> class for reading/writing?

    # TODO: Other stuff:
    #  - Dictionary that contains common field info ('entity_id', etc.) that can be indexed.

    SUPERTYPE_LIST_HEADER: tp.ClassVar[tp.Type[NewBinaryStruct]]
    # Maps MSB entry superlist names (parts, etc.) to dicts that map subtype enum ints to game-specific subtype info.
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[int, MSBSubtypeInfo]]]
    # Maps MSB entry superlist names (parts, etc.) to the relative offsets of their subtype enums.
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]]
    # Maps entry supertypes ('parts', 'events', etc.) to lists of `BaseGameType` types that appear in them.
    ENTITY_GAME_TYPES: tp.ClassVar[dict[str, tuple[MapEntity, ...]]]

    # Version info.
    HAS_HEADER: tp.ClassVar[bool]
    LONG_VARINTS: tp.ClassVar[bool]
    NAME_ENCODING: tp.ClassVar[str]

    # Subclasses define lists of entry subtypes here (`characters`, `sound_events`, `object_models`, etc.).

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> Self:
        """Unpack an MSB from the given reader."""

        if cls.HAS_HEADER:
            header = reader.read(len(MSB_HEADER_BYTES))
            if header != MSB_HEADER_BYTES:
                raise AssertionError("Header of this MSB class did not match asserted header.")

        offset_fmt = "q" if cls.LONG_VARINTS else "i"
        entry_lists = {}  # type: dict[str, list[MSBEntry]]  # both super (e.g. "parts") and sub-lists (e.g. "objects")
        for supertype_name in MSB_ENTRY_SUPERTYPES:
            superlist_header = cls.SUPERTYPE_LIST_HEADER.from_bytes(reader)
            entry_offset_count = superlist_header.pop("entry_offset_count")  # includes final offset to next list
            name_offset = superlist_header.pop("name_offset")
            entry_offsets = list(reader.unpack(f"{entry_offset_count}{offset_fmt}"))
            superlist_name = reader.unpack_string(offset=name_offset, encoding=cls.NAME_ENCODING)
            if superlist_name != (expected_name := supertype_name):
                raise ValueError(f"MSB entry list name '{superlist_name}' does not match name '{expected_name}'.")
            for entry_offset in entry_offsets[:-1]:  # exclude last offset
                reader.seek(entry_offset)
                cls._unpack_entry(reader, superlist_name, entry_lists)
            reader.seek(entry_offsets[-1])

        # Resolve entry indices to actual object references.
        for event in entry_lists["EVENT_PARAM_ST"]:
            event: BaseMSBEvent
            event.indices_to_objects(entry_lists)

        for part in entry_lists["PARTS_PARAM_ST"]:
            part: BaseMSBPart
            part.indices_to_objects(entry_lists)

        for superlist_name in MSB_ENTRY_SUPERTYPES:
            entry_lists.pop(superlist_name)  # only pass subtype lists to constructor

        # noinspection PyArgumentList
        return cls(**entry_lists)

    @classmethod
    def _unpack_entry(cls, reader: BinaryReader, superlist_name: str, entry_lists: dict[str, list[MSBEntry]]):
        subtype_int = reader.unpack_value("i", offset=cls.MSB_ENTRY_SUBTYPE_OFFSETS[superlist_name])
        subtype_info = cls.MSB_ENTRY_SUBTYPES[superlist_name][subtype_int]
        subtype_class = subtype_info.entry_class
        entry = subtype_class.from_msb_reader(reader)
        # Put entry into appropriate supertype and subtype lists (creating if necessary).
        entry_lists.setdefault(superlist_name, []).append(entry)
        entry_lists.setdefault(subtype_info.msb_list_attr_name, []).append(entry)

    def _add_supertype_lists(self, entry_lists: dict[str, list[MSBEntry]]):
        """Checks base class of first instance of each subtype list (if not empty) to determine supertype.

        NOTE: Supertype lists contain `(subtype_name, entry)` tuples instead of just the entries. Supertype lists will
        also be correctly ordered by subtype enum.
        """
        supertype_lists = {supertype_name: [] for supertype_name in MSB_ENTRY_SUPERTYPES}
        for subtype_name, subtype_list in entry_lists:
            for supertype_name, supertype_base_class in MSB_ENTRY_SUPERTYPES.items():
                if subtype_list and isinstance(subtype_list[0], supertype_base_class):
                    named_subtypes = [(subtype_name, entry) for entry in subtype_list]
                    supertype_lists[supertype_name].extend(named_subtypes)

    def to_writer(self) -> BinaryWriter:
        entry_lists = {field.name: getattr(self, field.name) for field in fields(self)}
        self._add_supertype_lists(entry_lists)

        # Get model instance counts.
        model_instance_counts = {}
        for part in entry_lists["parts"]:
            part: BaseMSBPart
            if part.model.name in model_instance_counts:
                model_instance_counts[part.model.name] += 1
            else:
                model_instance_counts[part.model.name] = 1

        # TODO: use writer.varint_size to communicate encoding?
        writer = BinaryWriter(byte_order=ByteOrder.LittleEndian, varint_size=8 if self.LONG_VARINTS else 4)
        if self.HAS_HEADER:
            writer.append(MSB_HEADER_BYTES)

        for supertype_name in MSB_ENTRY_SUPERTYPES:
            supertype_list = entry_lists[supertype_name]
            self.SUPERTYPE_LIST_HEADER.object_to_writer(
                self,
                writer,
                name_offset=RESERVED,
                entry_offset_count=len(supertype_list) + 1,  # includes final offset to next supertype list
            )
            for _, entry in supertype_list:
                writer.reserve("v", "entry_offset", obj=entry)
            writer.reserve("v", "next_list_offset", obj=supertype_list)

            writer.fill_with_position("name_offset", obj=self)
            packed_name = supertype_name.encode("utf-8")
            packed_name += b"\0" * (16 - len(packed_name))  # pad to 16 characters (NOTE: 32 in older Soulstruct)
            writer.append(packed_name)

            for supertype_index, (subtype_name, entry) in enumerate(supertype_list):
                entry: MSBEntry
                writer.fill_with_position("entry_offset", obj=entry)
                subtype_index = entry_lists[subtype_name].index(entry)
                if supertype_name == "MODEL_PARAM_ST":
                    entry: BaseMSBModel
                    instance_count = model_instance_counts[entry.name]
                    entry.to_msb_writer(writer, supertype_index, subtype_index, entry_lists, instance_count)
                else:
                    entry.to_msb_writer(writer, supertype_index, subtype_index, entry_lists)

            if supertype_name == MSB_ENTRY_SUPERTYPES[-1]:
                writer.fill("next_list_offset", 0, obj=supertype_list)  # zero offset
            else:
                writer.fill_with_position("next_list_offset", obj=supertype_list)

        return writer

    def get_entry_by_name(self, name: str, entry_types=()) -> tp.Optional[MSBEntry]:
        """Get `MSBEntry` with name `name` that is one of the given `entry_types`, or any type if `entry_types=()`.

        Raises a `KeyError` if the name cannot be found, and a `ValueError` if multiple entries are found.
        """
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
            raise KeyError(f"Could not find an entry named '{name}' with type {entry_types} in MSB.")
        if len(results) > 1:
            raise ValueError(f"Found entries of multiple types with name '{name}': {list(results)}")
        return next(iter(results.values()))

    def to_dict(self, ignore_defaults=True) -> dict:
        """Return a dictionary form of the MSB.

        If `ignore_defaults=True` (default), entry fields that have the default values for that entry subclass will not
        be included in the entry's dictionary.

        TODO: Later MSB versions may have header data.
        """
        return {
            "parts": self.parts.to_dict(ignore_defaults=ignore_defaults),
            "events": self.events.to_dict(ignore_defaults=ignore_defaults),
            "regions": self.regions.to_dict(ignore_defaults=ignore_defaults),
            "models": self.models.to_dict(ignore_defaults=ignore_defaults),
        }

    def load_dict(self, data: dict, clear_old_data=True):
        if clear_old_data:
            self.parts.clear()
            self.events.clear()
            self.regions.clear()
            self.models.clear()
        for entry_type in ("parts", "events", "regions", "models"):
            entry_list = getattr(self, entry_type)  # type: BaseMSBEntryList
            for entry_subtype_name, entries in data.get(entry_type, []).items():
                entry_subtype_enum = getattr(entry_list.ENTRY_SUBTYPE_ENUM, entry_subtype_name)
                subtype_class = entry_list.SUBTYPE_CLASSES[entry_subtype_enum]
                for entry_dict in entries:
                    entry = subtype_class(**entry_dict)
                    entry_list.add_entry(entry)

    def rename_references(self, old_name: str, new_name: str, entry_types: tp.Sequence[str] = ()):
        """Looks for all linked references to `old_name` in parts and events, and renames any to `new_name`.

        If `entry_types` is given, only references to those entry types will be checked.
        """
        if entry_types:
            parsed_entry_types = []
            for entry_type_name in entry_types:
                entry_type_name = entry_type_name.lower()
                if entry_type_name in {"model", "event", "region", "part"}:
                    entry_type_name += "s"
                elif entry_type_name not in {"models", "events", "regions", "parts"}:
                    raise ValueError(f"{entry_type_name} is not a valid MSB entry type.")
                parsed_entry_types.append(entry_type_name)
            entry_types = tuple(parsed_entry_types)

        for entry in self.parts:
            entry.rename_names(old_name, new_name, entry_types=entry_types)
        for entry in self.events:
            entry.rename_names(old_name, new_name, entry_types=entry_types)

    def resolve_entries_list(self, entries, entry_types=()):
        """Lists of entries can include names of entries, if unique, or the actual `MSBEntry` instances."""
        if not entries:
            return []
        resolved = []
        for entry in entries:
            if isinstance(entry, str):
                resolved.append(self.get_entry_by_name(entry, entry_types))
            elif isinstance(entry, MSBEntry):
                resolved.append(entry)
            else:
                raise TypeError(f"Invalid entry specifier: {entry}. Must be a (unique) entry name or instance.")
        return resolved

    def get_repeated_entity_ids(self) -> dict[str, list[MSBEntryEntity]]:
        repeats = {}
        for entry_type in ("Parts", "Regions", "Events"):
            entries = getattr(self, entry_type.lower())
            entity_ids = set()
            repeated_entries = []  # type: list[MSBEntryEntity]
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
            raise KeyError(f"Could not find an entry with entity ID {entity_id} in MSB.")
        elif len(results) > 1:
            if allow_multiple:
                _LOGGER.warning(
                    f"Found multiple entries with entity ID {entity_id} in MSB. This should not happen. "
                    f"Returning first one only."
                )
            else:
                raise ValueError(f"Found multiple entries with entity ID {entity_id} in MSB. This should not happen.")
        return results[0]

    def clear_all(self):
        """Clear all four entry lists."""
        self.models.clear()
        self.events.clear()
        self.regions.clear()
        self.parts.clear()

    def merge(self, other_msb_source: tp.Union[GameFile.Typing, MSB], filter_func: tp.Callable = None):
        """Merge `other_msb_source` into this one by simply appending each of the other MSB's four entry lists to this.

        If `filter_func` is given, only entries (of all four types) for which `filter_func(entry) == True` will be
        merged in. Make sure the function can handle all four entry types, if appropriate.

        If any (non-filtered-out) entry in `other_msb_source` has the same name as an existing entry in this MSB, a
        `ValueError` will be raised.

        Returns a copy of the MSB.
        """
        if filter_func is not None and not callable(filter_func):
            raise ValueError("`filter_func` must be callable, take an MSB entry as an argument, and return a bool.")
        other_msb_path = other_msb_source if isinstance(other_msb_source, (str, Path)) else "<MSB>"
        if not isinstance(other_msb_source, self.__class__):
            other_msb_source = self.__class__(other_msb_source)
        merged_msb = self.copy()
        for entry_type in ("Model", "Event", "Region", "Part"):  # capitalized for nice error message below
            existing_entries = merged_msb[entry_type]
            existing_entry_list = set(existing_entries.get_entry_names())
            other_entry_list = other_msb_source[entry_type]
            skipped_repeated_entries = []
            for other_entry in other_entry_list:
                if filter_func is not None and not filter_func(other_entry):
                    continue  # skip entry
                if other_entry.name in existing_entry_list:
                    skipped_repeated_entries.append(other_entry)
                    continue
                existing_entries.add_entry(other_entry)
                existing_entry_list.add(other_entry.name)
            if skipped_repeated_entries:
                _LOGGER.warning(
                    f"{len(skipped_repeated_entries)} MSB {entry_type} entries already exist in MSB and "
                    f"were not merged in from '{other_msb_path.name}'."
                )
        return merged_msb

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

        Also automatically applies vertical component (`translate.y`) to `reflect_plane_height` for Collisions.

        Args:
            translate: `(x, y, z)` vector to shift entries by.
            selected_entries: if not empty, move only these given entries. Each element in this sequence can be
                an `MSBEntry` instance or the name (if unique) of a Part or Region.
        """
        selected_entries = self.resolve_entries_list(selected_entries, entry_types=("parts", "regions"))

        for part in self.parts:
            if not selected_entries or part in selected_entries:
                part.translate += translate
                if hasattr(part, "reflect_plane_height"):
                    part.reflect_plane_height += translate.y
        for region in self.regions:
            if not selected_entries or region in selected_entries:
                region.translate += translate

    def write_entities_module(
        self,
        module_path: str | Path = None,
        area_id: int = None,
        block_id: int = None,
        # TODO: cc_id and dd_id for Elden Ring
        append_to_module: str = ""
    ):
        """Generates a '{mXX_YY}_entities.py' file with entity IDs for import into EVS script.

        If `append_to_module` text is given, all map entities will be appended to it.
        """
        if module_path is None:
            if self.path is None:
                raise ValueError("Cannot auto-detect MSB entities `module_path` (MSB path not known).")
            module_path = self.path.parent / f"{self.path.name.split('.')[0]}_entities.py"

        module_path.parent.mkdir(parents=True, exist_ok=True)

        auto_map_range_start = None
        if area_id is None and block_id is None:
            if self.path:
                map_name_match = MAP_NAME_RE.match(self.path.name)
                if map_name_match:
                    area_id, block_id = map(int, map_name_match.group(1, 2))
                    auto_map_range_start = area_id * 100000 + block_id * 10000
                else:
                    _LOGGER.warning(
                        f"Could not auto-detect map area and block (cannot parse from MSB path: {self.path}). "
                        "Auto-enumerator functions will be commented out; replace the {MAP_RANGE_START} string in each "
                        "one and uncomment to use."
                    )
            else:
                _LOGGER.warning(
                    "Could not auto-detect map area and block (MSB path not known). Auto-enumerator functions will be"
                    "commented out; replace the {MAP_RANGE_START} string in each one and uncomment to use."
                )
        elif area_id is not None and block_id is not None:
            auto_map_range_start = area_id * 100000 + block_id * 10000
        else:
            raise ValueError("Both `area_id` and `block_id` must be given, or neither for automatic detection.")

        trailing_digit_re = re.compile(r"(.*?)(\d+)")

        def sort_key(key_value) -> tuple[str, int]:
            """Sort trailing digits properly."""
            _, value_ = key_value
            if match := trailing_digit_re.match(value_.name):
                return match.group(1), int(match.group(2))
            return value_.name, 0

        module_path = Path(module_path)

        game_types_import = f"from soulstruct.{self.GAME.submodule_name}.game_types import *\n"
        if append_to_module:
            if game_types_import not in append_to_module:
                # Add game type start import to module. (Very rare that it wouldn't already be there.)
                first_class_def_index = append_to_module.find("\nclass")
                if first_class_def_index != -1:
                    append_to_module = append_to_module.replace("\nclass", game_types_import + "\n\nclass", 1)
                else:
                    append_to_module += game_types_import
            module_text = append_to_module.rstrip("\n") + "\n"
        else:
            module_text = game_types_import

        for entry_type_name, entry_subtypes in self.ENTITY_GAME_TYPES.items():
            for entry_subtype in entry_subtypes:
                class_name = entry_subtype.get_msb_entry_type_subtype(pluralized_subtype=True)[1]
                class_text = ""
                entity_id_dict = self.get_entity_id_dict(entry_type_name, entry_subtype)
                sorted_entity_id_dict = {
                    k: v for k, v in sorted(entity_id_dict.items(), key=sort_key)
                }
                for entity_id, entry in sorted_entity_id_dict.items():
                    # name = entry.name.replace(" ", "_")
                    try:
                        name = entry.name.encode("utf-8").decode("ascii")
                    except UnicodeDecodeError:
                        class_text += f"    # TODO: Non-ASCII name characters.\n    # {entry.name} = {entity_id}"
                    else:
                        if not PY_NAME_RE.match(name):
                            class_text += f"    # TODO: Invalid variable name.\n    # {entry.name} = {entity_id}"
                        else:
                            class_text += f"    {name} = {entity_id}"
                    if entry.description:
                        class_text += f"  # {entry.description}"
                    class_text += "\n"
                if class_text:
                    class_def = f"\n\nclass {class_name}({entry_subtype.__name__}):\n"
                    class_def += f"    \"\"\"`{entry_subtype.__name__}` entity IDs for MSB and EVS use.\"\"\"\n\n"
                    auto_lines = [
                        "    # noinspection PyMethodParameters",
                        "    def _generate_next_value_(name, _, count, __):",
                        f"        return {entry_subtype.__name__}.auto_generate(count, {{MAP_RANGE_START}})",
                    ]
                    if auto_map_range_start is None:
                        auto_lines = ["    # " + line[4:] for line in auto_lines]
                    else:
                        auto_lines[-1] = auto_lines[-1].format(MAP_RANGE_START=auto_map_range_start)
                    class_def += "\n".join(auto_lines) + "\n\n"
                    class_text = class_def + class_text
                    module_text += class_text

        with module_path.open("w", encoding="utf-8") as f:
            f.write(module_text)

    # TODO: Methods to import entity IDs from module by matching names, and import names from module by matching entity
    #  IDs (e.g. once you fix exported Japanese names).

    @classmethod
    def get_subtype_dict(cls) -> dict[str, tuple[BaseMSBSubtype]]:
        """Return a nested dictionary mapping MSB type names (in typical display order) to tuples of subtype enums."""
        return {
            "Parts": tuple(cls.PART_LIST_CLASS.SUBTYPE_CLASSES.keys()),
            "Regions": tuple(cls.REGION_LIST_CLASS.SUBTYPE_CLASSES.keys()),
            "Events": tuple(cls.EVENT_LIST_CLASS.SUBTYPE_CLASSES.keys()),
            "Models": tuple(cls.MODEL_LIST_CLASS.SUBTYPE_CLASSES.keys()),
        }

    def __getitem__(self, entry_list_name) -> BaseMSBEntryList:
        """Retrieve entry list by name. Can be plural, like "parts", or singular, like "part"."""
        entry_list_name = entry_list_name.lower()
        if entry_list_name in {"model", "event", "region", "part"}:
            entry_list_name += "s"
        elif entry_list_name not in {"models", "events", "regions", "parts"}:
            raise ValueError(f"{entry_list_name} is not a valid MSB entry list.")
        return getattr(self, entry_list_name)

    @staticmethod
    def set_and_get_unique_names(entry_superlist: list[MSBEntry]) -> dict[int, str]:
        """Goes through all entries and assigns <repeat> suffixes to any repeated names, so that every entry has
        a unique name for name linking purposes. These suffixes will be removed when the MSB is packed.

        Returns a dictionary mapping entry indices to those new unique names.
        """
        unique_names = {}
        repeat_count = {}
        for i, entry in enumerate(entry_superlist):
            if entry.name in unique_names.values():
                repeat_count.setdefault(entry.name, 0)
                repeat_count[entry.name] += 1
                entry.name += f" <{repeat_count[entry.name]}>"
            unique_names[i] = entry.name
        return unique_names