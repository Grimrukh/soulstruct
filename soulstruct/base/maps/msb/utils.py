from __future__ import annotations

__all__ = [
    "MSB_JSONEncoder",
    "MSBBrokenEntryReference",
    "MSBSubtypeInfo",
    "GroupBitSet",
    "GroupBitSet128",
    "GroupBitSet256",
    "GroupBitSet1024",
]

import abc
import ast
import json
import logging
import re
import typing as tp
from dataclasses import dataclass, fields

from soulstruct.utilities.maths import Matrix3, Vector2, Vector3, Vector4, resolve_rotation
from soulstruct.utilities.conversion import int_group_to_bit_set, bit_set_to_int_group

if tp.TYPE_CHECKING:
    from .core import MSB
    from .enums import BaseMSBSubtype
    from .msb_entry import MSBEntry
    from .msb_entry_list import MSBEntryList
    from .parts import BaseMSBPart
    from .regions import BaseMSBRegion

_LOGGER = logging.getLogger("soulstruct")


class MSB_JSONEncoder(json.JSONEncoder):
    """Handles a few extra types that appear as `MSBEntry` field types."""

    def default(self, obj):
        if isinstance(obj, (Vector2, Vector3, Vector4, GroupBitSet)):
            return repr(obj)


@dataclass(slots=True)
class MSBBrokenEntryReference:
    """Assigned to `MSBEntry` reference fields when the entry cannot be found."""
    name: str
    index: int


class MSBSubtypeInfo(tp.NamedTuple):
    subtype_enum: BaseMSBSubtype
    entry_class: type[MSBEntry]
    subtype_list_name: str

    def matches_name(self, name: str) -> bool:
        """Check if `name` is one of the valid specifiers for this MSB entry subtype."""
        name_options = {
            self.subtype_list_name.lower(),
            self.subtype_enum.name.lower(),
            self.subtype_enum.pluralized_name.lower(),
            self.entry_class.__name__.lower(),
        }
        return name.lower() in name_options


@dataclass(slots=True)
class GroupBitSet(abc.ABC):
    """Stores the huge, multi-`uint` bitfields used for draw/display/backread/navmesh groups in MSBs.

    Handles `list[uint]` representation, `set[int]` representation, and allows custom JSON encoding.
    """
    BIT_COUNT: tp.ClassVar[int]
    _REPR_RE: tp.ClassVar[re.Pattern]

    # Only field.
    enabled_bits: set[int]

    def __init__(self, uint_list_or_bit_set: GroupBitSet | list[int] | set[int]):
        if isinstance(uint_list_or_bit_set, self.__class__):
            # Just copy bits from other instance.
            self.enabled_bits = uint_list_or_bit_set.enabled_bits.copy()
        elif isinstance(uint_list_or_bit_set, list):
            # List of unsigned integers (e.g. from packed `MSB` file).
            self.enabled_bits = int_group_to_bit_set(uint_list_or_bit_set, assert_size=len(uint_list_or_bit_set))
        elif isinstance(uint_list_or_bit_set, set):
            if not all(isinstance(i, int) and i < self.BIT_COUNT for i in uint_list_or_bit_set):
                raise TypeError(
                    f"Set passed to `{self.__class__.__name__}` must be integers all less than {self.BIT_COUNT}, not: "
                    f"{uint_list_or_bit_set}"
                )
            self.enabled_bits = uint_list_or_bit_set.copy()
        else:
            raise TypeError(f"Cannot initialize `{self.__class__.__name__}` from {type(uint_list_or_bit_set)}.")

    @classmethod
    def from_range(cls, first_bit: int, last_bit: int) -> tp.Self:
        """Create a `GroupBitSet` with all bits in the given range enabled (inclusive at both ends)."""
        if not 0 <= first_bit <= last_bit <= cls.BIT_COUNT:
            raise ValueError(f"Invalid range for `{cls.__name__}`: {first_bit} to {last_bit} (max {cls.BIT_COUNT}).")
        return cls(set(range(first_bit, last_bit + 1)))

    @classmethod
    def all_off(cls) -> tp.Self:
        return cls(set())

    @classmethod
    def all_on(cls) -> tp.Self:
        return cls(set(range(cls.BIT_COUNT)))

    @classmethod
    def from_repr(cls, repr_string: str):
        """Also handles JSON decoding."""
        if (match := cls._REPR_RE.match(repr_string)) is None:
            raise ValueError(f"Invalid string/JSON source for `{cls.__name__}`: {repr_string}")
        bit_tuple = ast.literal_eval(match.group(1))
        if isinstance(bit_tuple, int):
            bit_tuple = (bit_tuple,)  # formatting quirk (no single comma for single-element tuple in JSON)
        return cls(uint_list_or_bit_set=set(bit_tuple))

    def to_sorted_bit_list(self) -> list[int]:
        """For GUI display, mainly."""
        return sorted(self.enabled_bits)

    def to_uints(self) -> list[int]:
        return bit_set_to_int_group(enabled_flags=self.enabled_bits, group_size=self.BIT_COUNT // 32)

    def __iter__(self):
        """Enables seamless `BinaryStruct` field packing.

        BEWARE: Do NOT use this to try to iterate over all `enabled_bits`. You must access that field directly.
        """
        return iter(self.to_uints())

    def __contains__(self, bit: int) -> bool:
        """Container check for enabled bits (otherwise it would use `__iter__` above and get the uint fields)."""
        return bit in self.enabled_bits

    def __repr__(self) -> str:
        """Also used for JSON."""
        bit_tuple = "(" + ", ".join(str(i) for i in sorted(self.enabled_bits)) + ")"
        return f"{self.__class__.__name__}{bit_tuple}"

    def copy(self) -> tp.Self:
        return self.__class__(self.enabled_bits)

    def add(self, bit: int):
        if not 0 <= bit <= self.BIT_COUNT:
            raise ValueError(f"Bit {bit} is out of range for {self.BIT_COUNT}-bit `{self.__class__.__name__}`.")
        self.enabled_bits.add(bit)

    def remove(self, bit: int):
        if not 0 <= bit <= self.BIT_COUNT:
            raise ValueError(f"Bit {bit} is out of range for {self.BIT_COUNT}-bit `{self.__class__.__name__}`.")
        self.enabled_bits.remove(bit)

    def intersection(self, other: tp.Self | set[int]) -> tp.Self:
        cls = self.__class__
        if isinstance(other, cls):
            return cls(self.enabled_bits & other.enabled_bits)
        elif isinstance(other, set):
            return cls(self.enabled_bits & other)
        raise TypeError(f"Cannot intersect `{cls.__name__}` with {type(other)}. Must be a `set` or the same type.")

    def __and__(self, other: tp.Self | set[int]) -> tp.Self:
        return self.intersection(other)

    def union(self, other: tp.Self | set[int]) -> tp.Self:
        cls = self.__class__
        if isinstance(other, cls):
            return cls(self.enabled_bits | other.enabled_bits)
        elif isinstance(other, set):
            return cls(self.enabled_bits | other)
        raise TypeError(f"Cannot union `{cls.__name__}` with {type(other)}. Must be a `set` or the same type.")

    def __or__(self, other: tp.Self | set[int]) -> tp.Self:
        return self.union(other)

    def without(self, other: tp.Self | set[int]) -> tp.Self:
        cls = self.__class__
        if isinstance(other, cls):
            return cls(self.enabled_bits - other.enabled_bits)
        elif isinstance(other, set):
            return cls(self.enabled_bits - other)
        raise TypeError(f"Cannot subtract `{cls.__name__}` from {type(other)}. Must be a `set` or the same type.")

    def __sub__(self, other: tp.Self | set[int]) -> tp.Self:
        return self.without(other)


@dataclass(slots=True, init=False, repr=False)
class GroupBitSet128(GroupBitSet):
    BIT_COUNT: tp.ClassVar[int] = 128
    _REPR_RE: tp.ClassVar[re.Pattern] = re.compile(r"^GroupBitSet128(\([\d, ]*\))$")


@dataclass(slots=True, init=False, repr=False)
class GroupBitSet256(GroupBitSet):
    BIT_COUNT: tp.ClassVar[int] = 256
    _REPR_RE: tp.ClassVar[re.Pattern] = re.compile(r"^GroupBitSet256(\([\d, ]*\))$")


@dataclass(slots=True, init=False, repr=False)
class GroupBitSet1024(GroupBitSet):
    """For Part collision masks in Elden Ring."""
    BIT_COUNT: tp.ClassVar[int] = 1024
    _REPR_RE: tp.ClassVar[re.Pattern] = re.compile(r"^GroupBitSet1024(\([\d, ]*\))$")


def merge(msb_1: MSB, msb_2: MSB, filter_func: tp.Callable = None, allow_repeated_names=False) -> MSB:
    """Created a new merged MSB containing all entries from `msb_1` and `msb_2` by simply combining their subtype lists.
    Returns a new MSB; does not modify this one. Both MSBs must have the same field names.

    If `filter_func` is given, only `MSBEntry`s for which `filter_func(entry) == True` will be merged in. Make sure
    the function can handle all entry types as appropriate for your usage.

    If any (non-filtered-out) entry in `other_msb` has the same name as an existing entry in this MSB, and
    `allow_repeated_names=False` (default), a `ValueError` will be raised.
    """
    if filter_func is not None and not callable(filter_func):
        raise ValueError("`filter_func` must be callable, take an `MSBEntry` as its argument, and return a bool.")

    msb_1_field_names = [f.name for f in fields(msb_1)]
    msb_2_field_names = [f.name for f in fields(msb_2)]
    if msb_1_field_names != msb_2_field_names:
        raise TypeError(
            f"Cannot merge MSBs with different field names:\n"
            f"    msb_1: {msb_1_field_names}\n"
            f"    msb_2: {msb_2_field_names}"
        )

    merged_entry_lists = {}
    for subtype_name in msb_1_field_names:
        msb_1_entries = getattr(msb_1, subtype_name)  # type: MSBEntryList
        msb_1_entries = msb_1_entries.get_filtered_list(filter_func)
        msb_2_entries = getattr(msb_2, subtype_name)  # type: MSBEntryList
        msb_2_entries = msb_2_entries.get_filtered_list(filter_func)
        repeated_names = set(msb_1_entries.get_entry_names()).intersection(msb_2_entries.get_entry_names())
        if repeated_names:
            if allow_repeated_names:
                _LOGGER.warning(f"Allowing repeated names in merged MSBs: {list(repeated_names)}")
            else:
                raise ValueError(f"Found repeated names in merged MSBs: {list(repeated_names)}")
        merged_entry_lists[subtype_name] = msb_1_entries  # deep-copied
        merged_entry_lists[subtype_name].extend(msb_2_entries)

    # noinspection PyArgumentList
    return msb_1.__class__(**merged_entry_lists)


def rotate_entry(
    entry: MSBEntry,
    rotation: Matrix3 | Vector3 | list | tuple | int | float,
    pivot_point: Vector3 | tuple[float, float, float] = (0.0, 0.0, 0.0),
    radians=False,
):
    """Modify entity `translate` and `rotate` by rotating entry around some `pivot_point` in world coordinates.

    Default `pivot_point` is the world origin (0, 0, 0). Default rotation units are degrees.
    """
    rotation = resolve_rotation(rotation, radians)
    pivot_point = Vector3(pivot_point)
    entry.rotate = (rotation @ Matrix3.from_euler_angles(entry.rotate)).to_euler_angles()
    entry.translate = (rotation @ (entry.translate - pivot_point)) + pivot_point


def move_map(
    msb: MSB,
    start_translate: Vector3 | None = None,
    end_translate: Vector3 | None = None,
    start_rotate: Vector3 | None = None,
    end_rotate: Vector3 | None = None,
    selected_entries=(),
):
    """Move everything with a transform in given `MSB` relative to an initial and a final reference point.

    Args:
        msb (MSB): Map whose contents will be moved.
        start_translate: initial `(x, y, z)` translate of initial reference point.
        end_translate: final `(x, y, z)` translate of final reference point.
        start_rotate: initial `(x, y, z)` rotate of initial reference point, or simply `y` if a number is given.
        end_rotate: final `(x, y, z)` rotate of final reference point, or simply `y` if a number is given.
        selected_entries: if not empty, move only these given entries. Each element in this sequence can be
            an `MSBEntry` instance or the name (if unique) of a Part or Region.

    Optionally, move only a subset of entry names given in `selected_entry_names`.
    """
    if start_translate is None:
        start_translate = Vector3.zero()
    if end_translate is None:
        end_translate = Vector3.zero()
    if start_rotate is None:
        start_rotate = Vector3.zero()
    if end_rotate is None:
        end_rotate = Vector3.zero()

    # Compute global rotation matrix required to get from `start_rotate` to `end_rotate`.
    m_start_rotate = Matrix3.from_euler_angles(start_rotate)
    m_end_rotate = Matrix3.from_euler_angles(end_rotate)
    m_world_rotation = m_end_rotate @ m_start_rotate.T

    # Apply global rotation to start point to determine required global translation.
    translation = end_translate - (m_world_rotation @ start_translate)  # type: Vector3

    rotate_all_in_world(msb, m_world_rotation, selected_entries=selected_entries)
    translate_all(msb, translation, selected_entries=selected_entries)


def rotate_part_or_region(
    entry: BaseMSBPart | BaseMSBRegion,
    rotation: Matrix3 | Vector3 | list | tuple | int | float,
    pivot_point: Vector3 | tuple[float, float, float] = (0.0, 0.0, 0.0),
    radians=False,
):
    """Modify entity `translate` and `rotate` by rotating entity around some `pivot_point` in world coordinates.
    Default `pivot_point` is the world origin (0, 0, 0). Default rotation units are degrees.
    """
    if not hasattr(entry, "translate") or not hasattr(entry, "rotate"):
        raise TypeError(
            f"Cannot rotate MSB entry type: `{entry.__class__.__name__}`. "
            f"It must have `translate` and `rotate` attributes."
        )
    rotation = resolve_rotation(rotation, radians)
    pivot_point = Vector3(pivot_point)
    entry.rotate = (rotation @ Matrix3.from_euler_angles(entry.rotate)).to_euler_angles()
    entry.translate = (rotation @ (entry.translate - pivot_point)) + pivot_point


def rotate_all_in_world(
    msb: MSB,
    rotation: Matrix3 | Vector3 | list | tuple | int | float,
    pivot_point: Vector3 | tuple[float, float, float] = (0.0, 0.0, 0.0),
    radians=False,
    selected_entries=(),
):
    """Rotate every Part and Region in the map around the given `pivot_point` by the Euler angles specified by
    `rotation`, modifying both `.rotate` and (unless equal to `pivot_point`) `.translate` for each entry.

    Args:
        msb (MSB): Map whose contents will be rotated.
        rotation: Euler angles, as specified by `(x, y, z)`, an Euler rotation matrix, or a single value to apply
            simple `y` rotation only.
        pivot_point: point around with `rotation` will be applied. Defaults to world origin, `(0, 0, 0)`.
        radians: if True, given `rotation` is in radians; degrees otherwise. Defaults to `False` (degrees).
        selected_entries: if not empty, move only these given entries. Each element in this sequence can be
            an `MSBEntry` instance or the name (if unique) of a Part or Region.
    """
    selected_entries = msb.resolve_entries_list(selected_entries, supertypes=("parts", "regions"))

    rotation_m = resolve_rotation(rotation)
    pivot_point = Vector3(pivot_point)
    for part in msb.get_parts():
        if not selected_entries or part in selected_entries:
            rotate_part_or_region(part, rotation_m, pivot_point=pivot_point, radians=radians)
    for region in msb.get_regions():
        if not selected_entries or region in selected_entries:
            rotate_part_or_region(region, rotation_m, pivot_point=pivot_point, radians=radians)


def translate_all(msb: MSB, translate: Vector3, selected_entries=()):
    """Add given `translate` vector to `.translate` vector attributes of all Regions and Parts.

    Also automatically applies vertical component (`translate.y`) to `reflect_plane_height` for Collisions.

    Args:
        msb (MSB): Map whose parts and regions will be translated.
        translate (Vector3): `(x, y, z)` vector to shift entries by.
        selected_entries: if not empty, move only these given entries. Each element in this sequence can be
            an `MSBEntry` instance or the name (if unique) of a Part or Region.
    """
    selected_entries = msb.resolve_entries_list(selected_entries, supertypes=("parts", "regions"))

    for part in msb.get_parts():
        if not selected_entries or part in selected_entries:
            part.translate += translate
            if hasattr(part, "reflect_plane_height"):
                part.reflect_plane_height += translate.y
    for region in msb.get_regions():
        if not selected_entries or region in selected_entries:
            region.translate += translate
