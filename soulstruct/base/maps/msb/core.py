from __future__ import annotations

__all__ = ["MSB"]

import abc
import json
import logging
import re
import struct
import typing as tp
from dataclasses import fields
from enum import Enum, StrEnum
from pathlib import Path

from soulstruct.base.game_file import GameFile
from soulstruct.base.game_types import GAME_INT_TYPE
from soulstruct.base.game_types.map_types import MapEntity
from soulstruct.utilities.binary import *
from soulstruct.utilities.files import write_json
from soulstruct.utilities.maths import Vector2, Vector3, Vector4
from soulstruct.utilities.misc import IDList
from .region_shapes import RegionShape

from .msb_entry import MSBEntry
from .msb_entry_list import MSBEntryList
from .events import BaseMSBEvent
from .models import BaseMSBModel
from .parts import BaseMSBPart
from .regions import BaseMSBRegion
from .utils import GroupBitSet, MSBSubtypeInfo

if tp.TYPE_CHECKING:
    from .enums import BaseMSBSubtype


_LOGGER = logging.getLogger("soulstruct")


MAP_NAME_RE = re.compile(r"m(\d\d)_(\d\d)_(\d\d)_(\d\d)")

# NOTE: Completely absent in DS1 and earlier.
MSB_HEADER_BYTES = struct.pack("4sII??BB", b"MSB ", 1, 16, False, False, 1, 255)


MSB_MODEL_T = tp.TypeVar("MSB_MODEL_T", bound=BaseMSBModel)
MSB_EVENT_T = tp.TypeVar("MSB_EVENT_T", bound=BaseMSBEvent)
MSB_REGION_T = tp.TypeVar("MSB_REGION_T", bound=BaseMSBRegion)
MSB_PART_T = tp.TypeVar("MSB_PART_T", bound=BaseMSBPart)


class MSB(GameFile, tp.Generic[MSB_MODEL_T, MSB_EVENT_T, MSB_REGION_T, MSB_PART_T], abc.ABC):
    """Handles MSB ('MapStudio') data. Subclassed by each game.

    TODO: Update docstring.

    Most game MSBs contain four relevant types of data entries:

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

    class JSONEncoder(json.JSONEncoder):
        """Handles a few extra types that appear as `MSBEntry` field types."""

        def default(self, obj):
            if isinstance(obj, RegionShape):
                return obj.to_json_dict()
            if isinstance(obj, (Vector2, Vector3, Vector4, GroupBitSet)):
                return repr(obj)

    EXT: tp.ClassVar[str] = ".msb"

    # Indicates if this class is big-endian. There is no reliable way to guess this for MSBs, other than by asserting
    # that the first entry offset shouldn't be gigantic, so the class must enable it if necessary (e.g. Demon's Souls).
    # To allow 'console override' for games typically used on PC, you can load the `BinaryReader` and set it to big-
    # endian, which will override a value of `False` here.
    IS_BIG_ENDIAN: tp.ClassVar[bool] = False
    # Header struct for each supertype list.
    SUPERTYPE_LIST_HEADER: tp.ClassVar[type[BinaryStruct]]
    # Enum of MSB supertypes.
    MSB_SUPERTYPE_ENUM: tp.ClassVar[type[StrEnum]]
    # Dictionary mapping MSB supertype name enums to their base types, in the order they appear in the MSB.
    MSB_ENTRY_SUPERTYPES: tp.ClassVar[dict[str, type[MSBEntry]]]
    # Dictionary mapping MSB supertype name enums to their subtype enum types.
    MSB_SUPERTYPE_SUBTYPE_ENUMS: tp.ClassVar[dict[str, type[BaseMSBSubtype]]]
    # Maps MSB entry supertype names (e.g. 'POINT_PARAM_ST') to dicts that map subtype enum names to subtype info.
    MSB_ENTRY_SUBTYPES: tp.ClassVar[dict[str, dict[BaseMSBSubtype, MSBSubtypeInfo]]]
    # Maps MSB entry supertype names (parts, etc.) to the relative offsets of their subtype enums, which we check in
    # advance to determine which `MSBEntry` subclass to use.
    MSB_ENTRY_SUBTYPE_OFFSETS: tp.ClassVar[dict[str, int]]
    # Maps entry subtype names ("characters", "sounds", etc.) to their corresponding `BaseGameType`, if applicable.
    ENTITY_GAME_TYPES: tp.ClassVar[dict[str, type[MapEntity]]]
    # Cached when first accessed. Maps subtype list names, e.g. 'map_pieces', to the list. Immutable.
    _SUBTYPE_LIST_NAMES: tp.ClassVar[tuple[str, ...]] = None

    # Per-type callables that map a `map_base_id` entity ID to a dictionary of `first_value` and `last_value` kwargs.
    ID_RANGES = {}  # type: dict[GAME_INT_TYPE, tp.Callable[[int], dict[str, int]]]

    # Version info.
    HAS_HEADER: tp.ClassVar[bool]
    LONG_VARINTS: tp.ClassVar[bool]
    NAME_ENCODING: tp.ClassVar[str]

    # Only new field other than subtype lists.
    byte_order: ByteOrder = ByteOrder.LittleEndian

    # Subclasses define lists of entry subtypes here (`characters`, `sound_events`, `object_models`, etc.).

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> tp.Self:
        """Unpack an MSB from the given reader."""
        
        if cls.IS_BIG_ENDIAN:
            reader.byte_order = ByteOrder.BigEndian
        elif reader.byte_order == ByteOrder.BigEndian:
            _LOGGER.warning(
                "This MSB class has `IS_BIG_ENDIAN=False`, but as the reader is set to big-endian, that will be used."
            )

        if cls.HAS_HEADER:
            header = reader.read(len(MSB_HEADER_BYTES))
            if header != MSB_HEADER_BYTES:
                raise AssertionError("Header of this MSB class did not match asserted header.")

        # This will contain both supertype lists (e.g. "PARTS_PARAM_ST") and `MSBEntryList`s (e.g. "objects").
        # The supertype lists are needed here to resolve supertype-wide indices, but will be removed before `cls()`.
        entry_lists = {}  # type: dict[str, MSBEntryList[MSBEntry] | IDList[MSBEntry]]

        next_list_offset = -1
        for supertype in cls.MSB_ENTRY_SUPERTYPES.keys():

            entry_lists[supertype] = IDList()

            def _unpack_entry(reader_: BinaryReader):
                cls._unpack_entry(reader_, supertype, entry_lists)

            next_list_offset = cls._unpack_supertype_list(reader, supertype, _unpack_entry)
            if next_list_offset != 0:
                reader.seek(next_list_offset)

        # `next_list_offset` must be zero at this stage, as all lists have been read.
        if next_list_offset != 0:
            raise ValueError(f"Final MSB list offset was not zero: {next_list_offset}")

        cls._dereference_msb_entries(entry_lists)

        # Supertype lists are transient; we only pass subtype lists to the MSB dataclass.
        for supertype_name in cls.MSB_ENTRY_SUPERTYPES:
            entry_lists.pop(supertype_name)

        return cls(byte_order=reader.byte_order, **entry_lists)

    @classmethod
    def _unpack_supertype_list(
        cls,
        reader: BinaryReader,
        supertype_name: str,
        entry_unpack_func: tp.Callable[[BinaryReader], None],
    ) -> int:
        """Unpack an MSB supertype list with an asserted name, e.g. 'PARTS_PARAM_ST'.

        Returns the offset to the next list (will be zero for final MSB list).

        The `entry_unpack_func` should handle the unpacking of individual entries and their addition to a baked-in list.
        """
        offset_fmt = "q" if cls.LONG_VARINTS else "i"
        supertype_list_header = cls.SUPERTYPE_LIST_HEADER.from_bytes(reader)
        entry_offset_count = supertype_list_header.pop("entry_offset_count")  # includes final offset to next list
        name_offset = supertype_list_header.pop("name_offset")

        entry_offsets = list(reader.unpack(f"{entry_offset_count}{offset_fmt}"))
        found_name = reader.unpack_string(offset=name_offset, encoding=cls.NAME_ENCODING)
        if found_name != supertype_name:
            raise ValueError(f"MSB internal supertype list name '{found_name}' != expected name '{supertype_name}'.")
        # NOTE: Some games have empty supertype lists (e.g. "LAYER_PARAM_ST" in Elden Ring). This will still work.
        for entry_offset in entry_offsets[:-1]:  # exclude last offset
            reader.seek(entry_offset)
            entry_unpack_func(reader)

        return entry_offsets[-1]

    @classmethod
    def _unpack_entry(cls, reader: BinaryReader, supertype: str, entry_lists: dict[str, IDList[MSBEntry]]):
        subtype_int_offset = cls.MSB_ENTRY_SUBTYPE_OFFSETS[supertype]
        if subtype_int_offset != -1:
            subtype_int = reader.peek("i", bytes_ahead=subtype_int_offset)[0]  # type: int
        else:
            # No subtype offset, so we assume 0.
            subtype_int = 0

        try:
            # noinspection PyTypeChecker
            subtype_info = cls.MSB_ENTRY_SUBTYPES[supertype][subtype_int]  # keys are `IntEnum` members
        except KeyError:
            raise TypeError(f"Unknown '{supertype}' subtype enum value: {subtype_int}")
        try:
            entry = subtype_info.entry_class.from_msb_reader(reader)
        except Exception as ex:
            _LOGGER.error(f"Error unpacking MSB entry of type '{subtype_info.entry_class.__name__}': {ex}")
            raise
        # Put entry into appropriate supertype and subtype lists (creating if necessary).
        entry_lists[supertype].append(entry)
        subtype_list_name = subtype_info.subtype_list_name
        if subtype_list_name not in entry_lists:
            entry_lists[subtype_list_name] = MSBEntryList((), supertype=supertype, entry_class=subtype_info.entry_class)
        entry_lists[subtype_list_name].append(entry)

    @classmethod
    @abc.abstractmethod
    def _dereference_msb_entries(cls, entry_lists: dict[str, IDList[MSBEntry]]):
        """Resolve entry indices to actual object references."""
        ...

    @classmethod
    def resolve_supertype_name(cls, supertype: str) -> str:
        """Resolve various aliases for supertype names to the full MSB supertype list name.
        
        Handles the four standard types only, by default.
        """
        upper = supertype.upper()
        if upper.startswith("MODEL"):
            return "MODEL_PARAM_ST"
        if upper.startswith("EVENT"):
            return "EVENT_PARAM_ST"
        if upper.startswith("REGION") or upper.startswith("POINT"):
            return "POINT_PARAM_ST"
        if upper.startswith("PARTS"):
            return "PARTS_PARAM_ST"
        raise ValueError(f"Supertype name '{supertype}' not recognized.")

    @classmethod
    def entity_id_supertypes(cls) -> tuple[str, ...]:
        """Return a tuple of supertype names whose entries define `entity_id`."""
        return "PARTS_PARAM_ST", "POINT_PARAM_ST", "EVENT_PARAM_ST"

    def get_supertype_list(self, supertype: str) -> IDList[MSBEntry]:
        """Construct a list of all MSB entries with the given supertype (e.g. "PARTS_PARAM_ST")."""
        supertype = self.resolve_supertype_name(supertype)
        supertype_list = IDList()
        for subtype_list in self:
            if subtype_list.supertype == supertype:
                supertype_list.extend(subtype_list)
        return supertype_list

    def get_models(self) -> IDList[MSB_MODEL_T]:
        # noinspection PyTypeChecker
        return self.get_supertype_list("MODEL_PARAM_ST")

    def get_events(self) -> IDList[MSB_EVENT_T]:
        # noinspection PyTypeChecker
        return self.get_supertype_list("EVENT_PARAM_ST")

    def get_regions(self) -> IDList[MSB_REGION_T]:
        # noinspection PyTypeChecker
        return self.get_supertype_list("POINT_PARAM_ST")

    def get_parts(self) -> IDList[MSB_PART_T]:
        # noinspection PyTypeChecker
        return self.get_supertype_list("PARTS_PARAM_ST")    

    def get_regions_with_shape(self, shape_name: str) -> list[MSB_REGION_T]:
        """Find all regions with given shape name. Not case-sensitive, but doesn't work with plurals."""
        name = shape_name.lower()
        return [
            region for region in self.get_regions()
            if region.shape.SHAPE_TYPE.name.lower() == name
        ]

    def get_list_of_entry(self, entry: MSBEntry) -> MSBEntryList:
        """Find subtype list that contains exact instance `entry` (e.g. for an event's attached region/part)."""
        for entry_list in self:
            if entry in entry_list:
                return entry_list
        raise ValueError(f"Entry '{entry.name}' does not appear anywhere in this MSB.")

    def to_writer(self) -> BinaryWriter:

        # Complete dictionary of all subtype AND merged supertype lists is passed to each `MSBEntry` for referencing.
        entry_lists = {
            name: getattr(self, name) for name in self.get_subtype_list_names()
        } | {
            supertype_name: self.get_supertype_list(supertype_name) for supertype_name in self.MSB_ENTRY_SUPERTYPES
        }  # type: dict[str, IDList[MSBEntry]]

        # Check for duplicate names within supertypes (except events, where duplicates are permitted and common).
        for supertype_name in ("MODEL_PARAM_ST", "PARTS_PARAM_ST", "POINT_PARAM_ST"):
            names = set()
            for entry in entry_lists[supertype_name]:
                if entry.name in names:
                    _LOGGER.warning(
                        f"Duplicate '{supertype_name}' name in MSB {self.path_minimal_stem}: '{entry.name}'"
                    )
                else:
                    names.add(entry.name)

        # Get model instance counts. We collect them all here at once to save on multiple iterations.
        model_instance_counts = {}
        for part in entry_lists["PARTS_PARAM_ST"]:
            part: MSB_PART_T
            if part.model is None:
                continue
            if part.model.name in model_instance_counts:
                model_instance_counts[part.model.name] += 1
            else:
                model_instance_counts[part.model.name] = 1

        # TODO: use writer.long_varints to communicate encoding?
        writer = BinaryWriter(byte_order=self.byte_order, long_varints=self.LONG_VARINTS)
        if self.HAS_HEADER:
            writer.append(MSB_HEADER_BYTES)
        last_supertype_name = list(self.MSB_ENTRY_SUPERTYPES)[-1]

        for supertype_name in self.MSB_ENTRY_SUPERTYPES:
            supertype_list = entry_lists[supertype_name]
            self.SUPERTYPE_LIST_HEADER.object_to_writer(
                self,
                writer,
                name_offset=RESERVED,
                entry_offset_count=len(supertype_list) + 1,  # includes final offset to next supertype list
            )
            for entry in supertype_list:
                writer.reserve("entry_offset", "v", obj=entry)
            writer.reserve("next_list_offset", "v", obj=supertype_list)

            writer.fill_with_position("name_offset", obj=self)
            self.pack_supertype_name(writer, supertype_name)

            for supertype_index, entry in enumerate(supertype_list):
                entry: MSBEntry
                writer.fill_with_position("entry_offset", obj=entry)
                subtype_name = self.MSB_ENTRY_SUBTYPES[supertype_name][entry.SUBTYPE_ENUM].subtype_list_name
                subtype_index = entry_lists[subtype_name].index(entry)
                if supertype_name == "MODEL_PARAM_ST":
                    # Models also need their instance count passed in.
                    entry: MSB_MODEL_T
                    instance_count = model_instance_counts.get(entry.name, 0)
                    if instance_count == 0 and entry.name not in {"c0000", "c1000"}:
                        _LOGGER.warning(f"Model '{entry.name}' is not used by any parts in MSB '{self.path_name}'.")
                    try:
                        entry.to_msb_writer(writer, supertype_index, subtype_index, entry_lists, instance_count)
                    except Exception as ex:
                        _LOGGER.error(
                            f"Exception occurred while trying to write entry '{entry.name}': {ex}.\n"
                            f"  Entry: {entry}"
                        )
                        raise
                else:
                    try:
                        entry.to_msb_writer(writer, supertype_index, subtype_index, entry_lists)
                    except Exception as ex:
                        _LOGGER.error(
                            f"Exception occurred while trying to write entry '{entry.name}': {ex}.\n"
                            f"  Entry: {entry}"
                        )
                        raise

            if supertype_name == last_supertype_name:
                writer.fill("next_list_offset", 0, obj=supertype_list)  # zero offset
            else:
                writer.fill_with_position("next_list_offset", obj=supertype_list)

        return writer

    @abc.abstractmethod
    def pack_supertype_name(self, writer: BinaryWriter, supertype_name: str):
        """Differs between versions slightly."""

    def find_entry_name(
        self, name: str, supertypes: tp.Iterable[str] = (), subtypes: tp.Iterable[str] = ()
    ) -> MSBEntry:
        """Get `MSBEntry` with name `name` that is one of the given `entry_subtypes` or any type by default.

        Raises a `KeyError` if the name cannot be found, and a `ValueError` if multiple entries are found.
        """
        if subtypes:  # lower case
            entry_lists = [getattr(self, f.lower()) for f in subtypes]  # type: list[MSBEntryList]
        else:
            entry_lists = self.get_all_subtype_lists()

        if supertypes:
            supertype_names = [self.resolve_supertype_name(name) for name in supertypes]
            entry_lists = [
                entry_list for entry_list in entry_lists
                if entry_list.supertype in supertype_names
            ]

        results = []
        for subtype_list in entry_lists:
            try:
                # This will raise a `ValueError` if the name appears more than once in a single entry type list.
                results.append(subtype_list.find_entry_name(name))
            except KeyError:
                pass  # name does not appear in this list
        if not results:
            if supertypes and subtypes:
                type_msg = f"supertype in {supertypes} and subtype in {subtypes}"
            elif supertypes:
                type_msg = f"supertype in {supertypes}"
            elif subtypes:
                type_msg = f"subtype in {subtypes}"
            else:
                type_msg = "any type"
            raise KeyError(f"Could not find an entry named '{name}' with {type_msg} in MSB.")
        if len(results) > 1:
            raise ValueError(f"Found entries of multiple types with name '{name}': {list(results)}")
        return results[0]

    def find_model_name(self, name: str | Enum, subtypes: tp.Iterable[str] = ()) -> MSB_MODEL_T:
        """Get `MSBModel` with name `name` that is one of the given `entry_subtypes` or any type by default.

        Raises a `KeyError` if the name cannot be found, and a `ValueError` if multiple entries are found.
        """
        if isinstance(name, Enum):
            name = name.name
        # noinspection PyTypeChecker
        return self.find_entry_name(name, supertypes=["MODEL_PARAM_ST"], subtypes=subtypes)

    def find_event_name(self, name: str | Enum, subtypes: tp.Iterable[str] = ()) -> MSB_EVENT_T:
        """Get `MSBEvent` with name `name` that is one of the given `entry_subtypes` or any type by default.

        Raises a `KeyError` if the name cannot be found, and a `ValueError` if multiple entries are found.
        """
        if isinstance(name, Enum):
            name = name.name
        # noinspection PyTypeChecker
        return self.find_entry_name(name, supertypes=["EVENT_PARAM_ST"], subtypes=subtypes)

    def find_region_name(self, name: str | Enum, subtypes: tp.Iterable[str] = ()) -> MSB_REGION_T:
        """Get `MSBRegion` with name `name` that is one of the given `entry_subtypes` or any type by default.

        Raises a `KeyError` if the name cannot be found, and a `ValueError` if multiple entries are found.
        """
        if isinstance(name, Enum):
            name = name.name
        # noinspection PyTypeChecker
        return self.find_entry_name(name, supertypes=["POINT_PARAM_ST"], subtypes=subtypes)

    def find_part_name(self, name: str | Enum, subtypes: tp.Iterable[str] = ()) -> MSB_PART_T:
        """Get `MSBPart` with name `name` that is one of the given `entry_subtypes` or any type by default.

        Raises a `KeyError` if the name cannot be found, and a `ValueError` if multiple entries are found.
        """
        if isinstance(name, Enum):
            name = name.name
        # noinspection PyTypeChecker
        return self.find_entry_name(name, supertypes=["PARTS_PARAM_ST"], subtypes=subtypes)

    def reattach_all_entry_references(self, warn_reattachments=False, backup_converter: tp.Callable[[str], str] = None):
        """Iterate over all Parts and Events, and reattach same-named references to other entries in this MSB.

        Must be called manually so you know what you're doing.
        """
        for supertype_entry_list in (self.get_parts(), self.get_events()):
            for entry in supertype_entry_list:
                self.reattach_entry_references(entry, warn_reattachments, backup_converter)

    def reattach_entry_references(
        self, entry: MSB_PART_T | MSB_EVENT_T,
        warn_reattachments=False,
        backup_converter: tp.Callable[[str], str] = None,
    ):
        """Reattach same-named references to other entries in this MSB.

        For example, if an `MSBCharacter.draw_parent` is set to a collision that is not in this MSB (e.g. because the
        character was brought in from another `MSB` instance), this method will search for a collision with the same
        name and reattach that reference. If no name match is found, an error is raised.

        If a name is not found, the `backup_converter` function (if given) will be called with the name, and the result
        will be used to search for a match. If no match is found, an error is raised.

        Must be called manually so you know what you're doing.
        """
        supertype_name = entry.SUPERTYPE_ENUM.capitalize()[:-1]  # 'Part' or 'Event'
        for field_name in entry.MSB_ENTRY_REFERENCES:
            field_value = getattr(entry, field_name)
            if field_value is None:
                if supertype_name == "Part" and field_name == "model":  # cannot be None
                    raise ValueError(f"Part {entry} has no model.")
                continue  # can be None  # TODO: but there are some fields that should almost never be None!
            if isinstance(field_value, list):
                # Sequence of referenced entries.
                for i, item in enumerate(tuple(field_value)):
                    if item is None:
                        continue
                    if not isinstance(item, MSBEntry):
                        raise ValueError(
                            f"Index {i} of sequence field `{field_name}` of {supertype_name} '{entry.name}' "
                            f"is not an `MSBEntry`: {item}"
                        )
                    try:
                        referenced_entry = self.find_entry_name(item.name)
                    except KeyError:
                        if backup_converter:
                            try:
                                referenced_entry = self.find_entry_name(backup_converter(item.name))
                            except KeyError:
                                raise KeyError(
                                    f"Could not find entry with name '{item.name}' referenced by index {i} of "
                                    f"sequence field `{field_name}` in {supertype_name} '{entry.name}'."
                                )
                        else:
                            raise KeyError(
                                f"Could not find entry with name '{item.name}' referenced by index {i} of "
                                f"sequence field `{field_name}` in {supertype_name} '{entry.name}'."
                            )
                    if item is referenced_entry:
                        continue  # already attached
                    field_value[i] = referenced_entry  # attach to same-named entity
                continue

            if not isinstance(field_value, MSBEntry):
                raise ValueError(
                    f"Field `{field_name}` of {supertype_name} '{entry.name}' is not an `MSBEntry`: {field_value}"
                )

            # Single referenced entry.
            try:
                referenced_entry = self.find_entry_name(field_value.name)
            except KeyError:
                if backup_converter:
                    try:
                        referenced_entry = self.find_entry_name(backup_converter(field_value.name))
                    except KeyError:
                        raise KeyError(
                            f"Could not find entry with name '{field_value.name}' referenced by "
                            f"field `{field_name}` in {supertype_name} '{entry.name}'."
                        )
                else:
                    raise KeyError(
                        f"Could not find entry with name '{field_value.name}' referenced by "
                        f"field `{field_name}` in {supertype_name} '{entry.name}'."
                    )
            if field_value is referenced_entry:
                continue  # already attached
            setattr(entry, field_name, referenced_entry)  # attach to same-named entity
            if warn_reattachments:
                _LOGGER.warning(
                    f"Reattached dangling reference to '{field_value.name}' in "
                    f"field `{field_name}` of {supertype_name} '{entry.name}'."
                )

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        """Return a dictionary form of the MSB.

        Fully serializes `MSBEntry` contents by converting inter-entry references to dictionaries.

        If `ignore_defaults=True` (default), entry fields that have the default values for that entry subclass will not
        be included in the entry's dictionary.

        NOTE: No MSB header information needs to be recorded. Just the version info.
        """
        entry_lists = self.get_all_subtype_lists()
        msb_dict = {"version": self.get_version_dict()}  # type: dict[str, dict[str, tp.Any]]
        for subtype_list in entry_lists:
            for supertype_name in self.MSB_ENTRY_SUPERTYPES:
                if subtype_list.supertype == supertype_name:
                    msb_dict.setdefault(supertype_name, {}).update(subtype_list.to_json_dict(self, ignore_defaults))
        return msb_dict

    def write_json(
        self,
        file_path: None | str | Path,
        encoding="utf-8",
        indent=4,
        ignore_defaults=True,
    ):
        """Create a dictionary from instance and write it to a JSON file.

        The file path will have the `.json` suffix added automatically if missing.
        """
        json_dict = self.to_dict(ignore_defaults=ignore_defaults)
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because file default `path` has not been set.")
            file_path = self.path
        file_path = Path(file_path)
        if file_path.suffix != ".json":
            file_path = file_path.with_suffix(file_path.suffix + ".json")
        write_json(file_path, json_dict, indent=indent, encoding=encoding, encoder=self.JSONEncoder)

    @classmethod
    def from_dict(cls, data: dict) -> tp.Self:
        """Load MSB from dictionary of version info and entries (sorted by supertype and nested subtype keys)."""

        if "version" not in data:
            raise ValueError("MSB dictionary is missing 'version' key.")
        if data["version"] != cls.get_version_dict():
            raise TypeError(f"Invalid MSB 'version' info in dict for this MSB class: {data['version']}")

        subtype_lists = {}
        deferred_refs = {}
        for supertype_name in cls.MSB_ENTRY_SUPERTYPES:
            if supertype_name not in data:
                # TODO: *Not* unusual for LAYERS in Elden Ring.
                # _LOGGER.warning(f"No '{supertype_name}' key found in MSB dictionary, which is unusual.")
                continue
            subtype_dict = data[supertype_name]
            for subtype_enum_name, subtype_list in subtype_dict.items():
                subtype_enum = cls.MSB_SUPERTYPE_SUBTYPE_ENUMS[supertype_name][subtype_enum_name]
                subtype_info = cls.MSB_ENTRY_SUBTYPES[supertype_name][subtype_enum]
                entries = []
                subtype_deferred = deferred_refs[subtype_info.subtype_list_name] = []
                for entry_dict in subtype_list:
                    entry, deferred = subtype_info.entry_class.from_json_dict(entry_dict)
                    if deferred:
                        subtype_deferred.append((entry, deferred))
                    entries.append(entry)
                subtype_lists[subtype_info.subtype_list_name] = MSBEntryList(
                    entries, supertype=supertype_name, entry_class=subtype_info.entry_class
                )

        cls._resolve_deferred_json_refs(subtype_lists, deferred_refs)

        return cls(**subtype_lists)

    @classmethod
    def _resolve_deferred_json_refs(cls, subtype_lists: dict[str, MSBEntryList], deferred_refs: dict):
        """Resolve deferred entry references now that all lists are complete."""

        subtype_cache = {}  # type: dict[str, tuple[dict[str, MSBEntry], set[str]]]

        for subtype_list_name, deferred_list in deferred_refs.items():
            for entry, deferred_dict in deferred_list:
                for field_name, field_ref in deferred_dict.items():
                    if isinstance(field_ref, dict):
                        ref_entry = cls._resolve_json_entry_ref(
                            entry, field_name, subtype_lists, field_ref, subtype_cache
                        )
                        setattr(entry, field_name, ref_entry)
                    elif isinstance(field_ref, list):
                        entry_list = []
                        for ref in field_ref:
                            if ref is None:
                                entry_list.append(None)
                            else:
                                ref_entry = cls._resolve_json_entry_ref(
                                    entry, field_name, subtype_lists, ref, subtype_cache, msg_field_str="array field"
                                )
                                entry_list.append(ref_entry)
                        setattr(entry, field_name, entry_list)

    @classmethod
    def _resolve_json_entry_ref(
        cls,
        entry: MSBEntry,
        field_name: str,
        subtype_lists: dict[str, MSBEntryList],
        field_ref: dict[str, str | int],
        subtype_cache: dict[str, tuple[dict[str, MSBEntry], set[str]]],
        msg_field_str="field",
    ) -> MSBEntry:
        try:
            ref_supertype, ref_subtype = field_ref["subtype"]
        except KeyError:
            ref_list_name = field_ref["subtype_list_name"]
        else:
            # Get ref list name from supertype and subtype enum values.
            subtype_enum = cls.MSB_SUPERTYPE_SUBTYPE_ENUMS[ref_supertype][ref_subtype]
            ref_list_name = cls.MSB_ENTRY_SUBTYPES[ref_supertype][subtype_enum].subtype_list_name

        try:
            subtype_list = subtype_lists[ref_list_name]
        except KeyError:
            raise ValueError(
                f"Entry '{entry.name}' {msg_field_str} `{field_name}` references missing subtype list: "
                f"`{ref_list_name}`."
            )
        if "entry_name" in field_ref:
            ref_name = field_ref["entry_name"]
            if ref_list_name not in subtype_cache:
                subtype_cache[ref_list_name] = subtype_list.get_entries_by_unique_name()
            entries_by_name, ambiguous_names = subtype_cache[ref_list_name]
            if ref_name in ambiguous_names:
                raise ValueError(
                    f"Entry '{entry.name}' {msg_field_str} `{field_name}` references ambiguous entry name: "
                    f"`{ref_list_name}[\"{ref_name}\"]`. JSON must use 'subtype_index' instead or "
                    f"referenced entry name must be made unique."
                )
            try:
                return entries_by_name[ref_name]
            except KeyError:
                raise ValueError(
                    f"Entry '{entry.name}' {msg_field_str} `{field_name}` references missing entry name: "
                    f"`{ref_list_name}[\"{ref_name}\"]`"
                )

        ref_index = field_ref["subtype_index"]
        try:
            return subtype_lists[ref_list_name][ref_index]
        except IndexError:
            raise ValueError(
                f"Entry '{entry.name}' {msg_field_str} `{field_name}` references invalid entry index: "
                f"`{ref_list_name}[{ref_index}]`"
            )

    @classmethod
    def get_version_dict(cls) -> dict[str, bool | str]:
        return {
            "has_header": cls.HAS_HEADER,
            "long_varints": cls.LONG_VARINTS,
            "name_encoding": cls.NAME_ENCODING,
        }

    @classmethod
    def get_subtype_list_names(cls) -> tuple[str, ...]:
        if cls._SUBTYPE_LIST_NAMES is not None:
            return cls._SUBTYPE_LIST_NAMES
        cls._SUBTYPE_LIST_NAMES = tuple(
            f.name for f in fields(cls)
            if f.name not in {"_path", "path", "_dcx_type", "dcx_type", "byte_order"}
        )
        return cls._SUBTYPE_LIST_NAMES

    def get_all_subtype_lists(self) -> list[MSBEntryList]:
        return [getattr(self, list_name) for list_name in self.get_subtype_list_names()]

    @classmethod
    def resolve_subtype_name(cls, subtype_name: str, assert_supertype_name: str = None) -> str:
        """Parse `subtype_name` (which could be an enum name or class name) to its subtype list name."""
        for supertype_name, subtype_info_list in cls.MSB_ENTRY_SUBTYPES.items():
            if assert_supertype_name is not None and supertype_name != assert_supertype_name:
                continue
            for info in subtype_info_list.values():
                if info.matches_name(subtype_name):
                    return info.subtype_list_name
        raise KeyError(f"Invalid MSB subtype name: {subtype_name}")

    def resolve_entries_list(
        self,
        entries: tp.Sequence[str | MSBEntry],
        supertypes: tp.Iterable[str] = (),
        subtypes: tp.Iterable[str] = (),
    ) -> IDList[MSBEntry]:
        """Lists of entries can include names of entries, if unique, or the actual `MSBEntry` instances."""
        if not entries:
            return IDList()
        resolved = IDList()
        for entry in entries:
            if isinstance(entry, str):
                resolved.append(self.find_entry_name(entry, supertypes, subtypes))
            elif isinstance(entry, MSBEntry):
                resolved.append(entry)
            else:
                raise TypeError(f"Invalid MSB entry specifier: {entry}. Must be a (unique) entry name or `MSBEntry`.")
        return resolved

    def add_entry(self, msb_entry: MSBEntry):
        """Detect subtype of entry and add to appropriate list.

        Does NOT check if entry is from the same game submodule as this MSB class; matches subtype from name only.
        """
        msb_list_name = self.resolve_subtype_name(msb_entry.SUBTYPE_ENUM.name)
        msb_list = getattr(self, msb_list_name)  # type: MSBEntryList
        msb_list.append(msb_entry)

    def get_repeated_entity_ids(self) -> dict[str, IDList[MSBEntry]]:
        """Scans all entries for repeated `entity_id` fields PER SUPERTYPE, not subtype.

        Repeated entity IDs in Parts appear to be mostly benign -- the first one will simply be used -- but repeated IDs
        in Regions (in DS1 at least) cause a fatal problem, as ALL entity IDs that occur after the first duplicated ID
        will simply not work. (Infamously, this is the case in vanilla m17_00_00_00, Duke's Archives.)

        Repeated IDs across different supertypes will be ignored.
        """
        repeats = {}
        for supertype_name in self.entity_id_supertypes():
            supertype_list = self.get_supertype_list(supertype_name)
            entity_ids = set()
            repeated_entries = IDList()  # type: IDList[MSBEntry]
            for entry in supertype_list:
                entity_id = entry.get_entity_id()
                if entity_id is None or entity_id <= 0:  # some subtypes have 'null' ID zero (e.g. environment events)
                    continue
                if entity_id in entity_ids:
                    repeated_entries.append(entry)
                else:
                    entity_ids.add(entity_id)
            repeats[supertype_name] = repeated_entries
        return repeats

    def get_supertype_entity_id_dict(self, supertype_name: str) -> dict[int, MSBEntry]:
        """Get a dictionary mapping entity IDs to `MSBEntry` instances for the given supertype.

        If multiple `MSBEntry` instances are found for a given ID, a warning is logged, and only the *first* one found
        is used (which matches game engine behavior).

        Analogous to the subtype-only method in `MSBEntryList`.
        """
        supertype_list = self.get_supertype_list(supertype_name)
        entries_by_id = {}
        for entry in supertype_list:
            entity_id = entry.get_entity_id()
            if entity_id is None or entity_id <= 0:
                continue  # ignore unavailable or null ID
            if entity_id in entries_by_id:
                _LOGGER.warning(f"Found multiple entries for entity ID {entity_id}. Only using first.")
            else:
                entries_by_id[entity_id] = entry
        return entries_by_id

    def get_supertype_entity_id_name_dict(self, supertype_name: str) -> dict[int, str]:
        """As above, but values are just entry names instead of the entries themselves."""
        entries_by_id = self.get_supertype_entity_id_dict(supertype_name)
        return {entity_id: entry.name for entity_id, entry in entries_by_id.items()}

    def find_entry_by_entity_id(self, entity_id: int, allow_multiple=True) -> MSBEntry | None:
        """Search ALL entries for the given entity ID and return that `MSBEntry` (or `None` if not found).

        If multiple entries with the same (non-default) ID are found, an error will be raised unless
        `allow_multiple=True`.
        """
        if entity_id <= 0:
            raise ValueError(f"Cannot find MSB entry using default entity ID value {entity_id}.")
        results = []
        for supertype_name in ("EVENT_PARAM_ST", "POINT_PARAM_ST", "PARTS_PARAM_ST"):  # not MODEL_PARAM_ST
            supertype_list = self.get_supertype_list(supertype_name)
            results.extend([entry for entry in supertype_list if entry.get_entity_id() == entity_id])
        if not results:
            raise KeyError(f"Could not find an entry with entity ID {entity_id} in MSB.")
        elif len(results) > 1:
            if allow_multiple:
                _LOGGER.warning(
                    f"Found multiple entries with entity ID {entity_id} in MSB. This should be fixed. "
                    f"Returning first one only."
                )
            else:
                raise ValueError(f"Found multiple entries with entity ID {entity_id} in MSB. This must be fixed.")
        return results[0]

    def remove_entry(self, entry: MSBEntry):
        """Find list containing entry and remove it."""
        subtype_list = self.get_list_of_entry(entry)
        subtype_list.remove(entry)

    def clear_all(self):
        """Clear all entry subtype lists."""
        for entry_list in self.get_all_subtype_lists():
            entry_list.clear()

    def __iter__(self):
        """Iterate over all subtype lists."""
        return iter(self.get_all_subtype_lists())

    def get_or_create_model(
        self,
        model_subtype_name: str,
        name: str,
        sib_path="",
        map_stem="",
        replace_existing=False,
    ) -> MSB_MODEL_T:
        """Get or create a model of the given subtype, with the given name and SIB path.

        Specify `replace_existing` if you want to replace an existing model with the same name, e.g. with a new SIB.

        TODO: Would be great to be able to infer the return type from the subtype name (or another arg).
        """
        for subtype_name, part_info in self.MSB_ENTRY_SUBTYPES["PARTS_PARAM_ST"].items():
            # Redirect part subtype names to their corresponding model subtype names.
            if part_info.matches_name(model_subtype_name):
                subtype_list_name = f"{subtype_name}Model"
                break
        else:
            subtype_list_name = self.resolve_subtype_name(model_subtype_name, "MODEL_PARAM_ST")
        model_list = self[subtype_list_name]
        try:
            model = model_list.find_entry_name(name)  # model with this name already exists
            if not replace_existing:
                return model
        except KeyError:
            model = self[subtype_list_name].new(name=name, sib_path=sib_path)  # type: MSB_MODEL_T
            if not model.sib_path:
                if map_stem:  # prevents empty `map_stem` from being formatted
                    model.set_auto_sib_path(map_stem=map_stem)
                else:
                    model.set_auto_sib_path()
        else:
            # Modify existing model.
            model.sib_path = sib_path
            if not model.sib_path:
                if map_stem:  # prevents empty `map_stem` from being formatted
                    model.set_auto_sib_path(map_stem=map_stem)
                else:
                    model.set_auto_sib_path()
        return model

    def has_c0000_model(self) -> bool:
        """Common check for character/player model c0000, which should be in every MSB (in every game)."""
        character_models = getattr(self, "character_models")  # type: MSBEntryList
        try:
            character_models.find_entry_name("c0000")
        except KeyError:
            player_models = getattr(self, "player_models")
            try:
                player_models.find_entry_name("c0000")
            except KeyError:
                return False
        return True

    def remove_unused_models(self) -> list[str]:
        """Remove any models not used by any parts in the MSB. Returns a list of removed model names."""
        used_models = IDList()
        for part in self.get_parts():
            if part.model is not None and part.model not in used_models:
                used_models.append(part.model)
        removed_model_names = []
        for model in self.get_models():  # transient supertype list
            if model not in used_models:
                self.remove_entry(model)
                removed_model_names.append(model.name)
        return removed_model_names

    @classmethod
    def get_display_type_dict(cls) -> dict[str, tuple[BaseMSBSubtype, ...]]:
        """Return a nested dictionary mapping MSB type names (in typical display order) to tuples of subtype enums."""
        display_dict = {}  # type: dict[str, tuple[BaseMSBSubtype, ...]]
        for supertype_name, subtype_enums in cls.MSB_ENTRY_SUBTYPES.items():
            display_dict[supertype_name] = tuple(subtype_enums)
        return {
            "Parts": display_dict["PARTS_PARAM_ST"],
            "Regions": display_dict["POINT_PARAM_ST"],
            "Events": display_dict["EVENT_PARAM_ST"],
            "Models": display_dict["MODEL_PARAM_ST"],
        }

    def __getitem__(self, subtype_name: str) -> MSBEntryList:
        """Retrieve entry subtype list by name, e.g. "characters", or enum name, e.g. "Character"."""
        subtype_list_name = self.resolve_subtype_name(subtype_name)
        return getattr(self, subtype_list_name)

    def get_models_of_part_subtype(self, part_subtype_name: str) -> MSBEntryList:
        """Retrieve all models that are used by the given part subtype."""
        model_subtype_list_name = self.resolve_subtype_name(part_subtype_name + "Model", "MODEL_PARAM_ST")
        return getattr(self, model_subtype_list_name)

    def get_map_stem(self) -> str:
        """Get the map stem (e.g. 'm10_01_00_00') from the MSB path, if possible."""
        if self.path is None:
            raise ValueError("Cannot get map stem from MSB path because it is not known.")
        if map_name_match := MAP_NAME_RE.match(self.path.name):
            return map_name_match.group(0)  # full match
        raise ValueError(f"Could not parse map stem from MSB path name: {self.path}")
