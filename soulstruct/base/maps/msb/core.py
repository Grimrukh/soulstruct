from __future__ import annotations

import abc
import io
import logging
import re
import typing as tp
from pathlib import Path

from soulstruct.base.game_file import GameFile
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
        dcx_magic: tuple[int, int] = None,
    ):
        self.models = self.MODEL_LIST_CLASS()
        self.events = self.EVENT_LIST_CLASS()
        self.regions = self.REGION_LIST_CLASS()
        self.parts = self.PART_LIST_CLASS()
        self.dcx_magic = ()
        super().__init__(msb_source, dcx_magic=dcx_magic)

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
