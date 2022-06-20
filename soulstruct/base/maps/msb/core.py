from __future__ import annotations

import abc
import io
import logging
import re
import typing as tp
from enum import IntEnum
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.containers.dcx import DCXType
from soulstruct.games import GameSpecificType
from soulstruct.game_types.msb_types import *
from soulstruct.utilities.binary import BinaryReader
from soulstruct.utilities.maths import Vector3, Matrix3, resolve_rotation

from .enums import MSBSubtype, MSBEventSubtype, MSBPartSubtype
from .msb_entry import MSBEntry

if tp.TYPE_CHECKING:
    from .msb_entry import MSBEntryList, MSBEntryEntity
    from .models import MSBModelList
    from .events import MSBEventList
    from .regions import MSBRegionList
    from .parts import MSBPartList

_LOGGER = logging.getLogger(__name__)


# These are ordered by convenience (same as GUI).
ENTITY_GAME_TYPES = {
    "parts": (
        MapPiece,
        Object,
        Character,
        PlayerStart,
        Collision,
    ),
    "events": (
        SoundEvent,
        VFXEvent,
        SpawnerEvent,
        MessageEvent,
        SpawnPointEvent,
        NavigationEvent,
    ),
    "regions": (
        RegionPoint,
        RegionSphere,
        RegionCylinder,
        RegionBox,
    ),
}


MAP_NAME_RE = re.compile(r"m(\d\d)_(\d\d)_.*")


class MSB(GameFile, GameSpecificType, abc.ABC):
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
        msb_source: tp.Union[None, str, Path, bytes, io.BufferedIOBase, BinaryReader] = None,
        dcx_type: DCXType = None,
    ):
        self.models = self.MODEL_LIST_CLASS()
        self.events = self.EVENT_LIST_CLASS()
        self.regions = self.REGION_LIST_CLASS()
        self.parts = self.PART_LIST_CLASS()
        self.dcx_type = None  # MSB files never use DCX
        super().__init__(msb_source, dcx_type=dcx_type)

    def unpack(self, msb_reader: BinaryReader, **kwargs):
        """Unpack an MSB from the given reader."""

        # Read (and ignore) constant header, if applicable.
        if self.HEADER:
            msb_reader.seek(msb_reader.position + len(self.HEADER))

        self.models = self.MODEL_LIST_CLASS(msb_reader)
        self.events = self.EVENT_LIST_CLASS(msb_reader)
        self.regions = self.REGION_LIST_CLASS(msb_reader)
        self.parts = self.PART_LIST_CLASS(msb_reader)

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
            entry_list = getattr(self, entry_type)  # type: MSBEntryList
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
                print(
                    f"# WARNING: {len(skipped_repeated_entries)} MSB {entry_type} entries already exist in MSB and "
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

    def write_entities_module(self, module_path: tp.Union[str, Path] = None, area_id: int = None, block_id: int = None):
        """Generates a '{mXX_YY}_entities.py' file with entity IDs for import into EVS script."""
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
        module_text = "from soulstruct.games import DARK_SOULS_DSR\nfrom soulstruct.game_types import *\n"
        for entry_type_name, entry_subtypes in ENTITY_GAME_TYPES.items():
            for entry_subtype in entry_subtypes:
                class_name = entry_subtype.get_msb_entry_type_subtype(pluralized_subtype=True)[1]
                class_text = ""
                entity_id_dict = self.get_entity_id_dict(entry_type_name, entry_subtype)
                sorted_entity_id_dict = {
                    k: v for k, v in sorted(entity_id_dict.items(), key=sort_key)
                }
                for entity_id, entry in sorted_entity_id_dict.items():
                    name = entry.name.replace(" ", "_")
                    try:
                        name = name.encode("utf-8").decode("ascii")
                    except UnicodeDecodeError:
                        class_text += f"    # {name} = {entity_id}  # TODO: Invalid name characters."
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
                        f"        return {entry_subtype.__name__}.auto_generate(count, {self.GAME.variable_name}, "
                        f"{{MAP_RANGE_START}})",
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
        return getattr(self, entry_list_name)

    def __iter__(self):
        return iter((self.models, self.events, self.regions, self.parts))

    def new_sound_event_with_box(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        width: float,
        depth: float,
        height: float,
        **sound_event_kwargs,
    ):
        if "base_region_name" in sound_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        sound = self.events.new_sound(**sound_event_kwargs)
        box = self.regions.new_box(
            name=f"_SoundEvent_{sound.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            width=width,
            depth=depth,
            height=height,
        )
        sound.base_region_name = box.name
        return sound

    def new_sound_event_with_sphere(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        radius: float,
        **sound_event_kwargs,
    ):
        if "base_region_name" in sound_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        sound = self.events.new_sound(**sound_event_kwargs)
        sphere = self.regions.new_sphere(
            name=f"_SoundEvent_{sound.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
            radius=radius,
        )
        sound.base_region_name = sphere.name
        return sound

    def new_vfx_event_with_point(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        point_entity_enum: tp.Optional[RegionPoint] = None,
        **vfx_event_kwargs,
    ):
        if "base_region_name" in vfx_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        vfx = self.events.new_vfx(**vfx_event_kwargs)
        point_name = f"_VFXEvent_{vfx.name.lstrip('_')}"
        if point_entity_enum is not None:
            if point_entity_enum.name != point_name:
                raise ValueError(f"Name of `point_entity_enum` must be '{point_name}', not '{point_entity_enum.name}'.")
            point_entity_id = point_entity_enum.value
        else:
            point_entity_id = -1
        point = self.regions.new_point(
            name=point_name,
            entity_id=point_entity_id,
            translate=translate,
            rotate=rotate,
        )
        vfx.base_region_name = point.name
        return vfx

    def new_spawn_point_event_with_point(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        **spawn_point_event_kwargs,
    ):
        if "base_region_name" in spawn_point_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        spawn_point = self.events.new_spawn_point(**spawn_point_event_kwargs)
        point = self.regions.new_point(
            name=f"_SpawnPointEvent_{spawn_point.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
        )
        spawn_point.spawn_point_region_name = point.name
        return spawn_point

    def new_message_event_with_point(
        self,
        translate: tp.Union[Vector3, tuple, list],
        rotate: tp.Union[Vector3, tuple, list],
        **message_event_kwargs,
    ):
        if "base_region_name" in message_event_kwargs:
            raise KeyError("`base_region_name` will be created and assigned automatically.")
        message = self.events.new_message(**message_event_kwargs)
        point = self.regions.new_point(
            name=f"_MessageEvent_{message.name.lstrip('_')}",
            translate=translate,
            rotate=rotate,
        )
        message.base_region_name = point.name
        return message

    def new_objact_event_for_object(
        self,
        obj_spec: tp.Union[str, int, IntEnum],
        obj_act_entity_id: int,
        obj_act_state: int = 0,
        obj_act_param_id: int = -1,
        obj_act_flag: int = None,
        name: str = None,
    ):
        """Add an `MSBObjActEvent` to the MSB attached to the given MSB `obj_name`.

        Entity ID (generally equal to the event ID that handles the ObjAct) must be given. All other variables are
        optional: ObjAct state (defaults to 0), ObjAct param ID (defaults to -1, i.e. the object's model ID), and
        associated state flag (defaults to 60000000 + the object's entity ID, if present).

        A `ValueError` will be raised if the `obj_name` has no entity ID and `obj_act_flag` is not given.
        """
        if isinstance(obj_spec, IntEnum):
            obj_spec = obj_spec.name
        if isinstance(obj_spec, str):
            obj = self.parts.get_entry_by_name(obj_spec, "Object")
        elif isinstance(obj_spec, int):
            obj = self.parts.get_entries("Object")[obj_spec]
        else:
            raise TypeError(f"`obj_spec` must be an index, name, or name-synchronised `IntEnum`, not {obj_spec}.")
        if obj_act_flag is None:
            if obj.entity_id <= 0:
                raise ValueError(
                    f"Cannot automatically set `obj_act_flag` for ObjAct attached to object '{obj.name}', as it does "
                    f"not have a valid entity ID."
                )
            obj_act_flag = 60000000 + obj.entity_id
        if name is None:
            name = f"_ObjAct_{obj.name.lstrip('_')}"
        return self.events.new_obj_act(
            name=name,
            obj_act_part_name=obj.name,
            obj_act_entity_id=obj_act_entity_id,
            obj_act_param_id=obj_act_param_id,
            obj_act_state=obj_act_state,
            obj_act_flag=obj_act_flag,
        )
