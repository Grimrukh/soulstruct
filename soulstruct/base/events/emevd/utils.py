from __future__ import annotations

__all__ = [
    "COMPARISON_NODES",
    "NEG_COMPARISON_NODES",
    "no_skip_or_negate_or_return",
    "negate_only",
    "skip_and_negate_and_return",
    "ConstantCondition",
    "EventArgumentData",
    "get_value_test",
    "boolify",
    "get_write_offset",
    "get_instruction_args",
    "get_byte_offset_from_struct",
    "format_event_layers",
    "EntityEnumsManager",
]

import ast
import inspect
import logging
import struct
import types
import typing as tp
from functools import wraps
from pathlib import Path

from soulstruct.game_types.msb_types import *
from soulstruct.utilities.files import import_arbitrary_file
from .enums import PlayerEntity
from .exceptions import NoSkipOrReturnError, NoNegateError

if tp.TYPE_CHECKING:
    from soulstruct.game_types import GameObject
    from soulstruct.utilities.binary import BinaryReader

_LOGGER = logging.getLogger(__name__)

COMPARISON_NODES = {ast.Eq: 0, ast.NotEq: 1, ast.Gt: 2, ast.Lt: 3, ast.GtE: 4, ast.LtE: 5}
NEG_COMPARISON_NODES = {ast.Eq: 1, ast.NotEq: 0, ast.Gt: 5, ast.Lt: 4, ast.GtE: 3, ast.LtE: 2}


def no_skip_or_negate_or_return(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrReturnError
        if negate:
            raise NoNegateError
        if end_event or restart_event:
            raise NoSkipOrReturnError
        if condition is None:
            raise ValueError("Condition index must be specified.")
        return func(*args, condition=condition, **kwargs)

    return decorated


def negate_only(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines != 0:
            raise NoSkipOrReturnError
        if end_event or restart_event:
            raise NoSkipOrReturnError
        if condition is None:
            raise ValueError("Condition index must be specified.")
        return func(*args, condition=condition, negate=negate, **kwargs)

    return decorated


def skip_and_negate_and_return(func):
    @wraps(func)
    def decorated(*args, condition=None, negate=False, skip_lines=0, end_event=False, restart_event=False, **kwargs):
        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, skip_lines=skip_lines, negate=negate, **kwargs)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, condition=condition, negate=negate, **kwargs)

        if end_event:
            if restart_event:
                raise ValueError("You cannot use more than one of: condition, skip_lines, end_event, restart_event.")
            return func(*args, end_event=True, negate=negate, **kwargs)

        if restart_event:
            return func(*args, restart_event=True, negate=negate, **kwargs)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")

    return decorated


class ConstantCondition:
    """Condition with no arguments. These conditions have 'hard-coded' methods in the EMEVD API."""

    def __init__(
        self,
        if_true_func=None,
        if_false_func=None,
        skip_if_true_func=None,
        skip_if_false_func=None,
        end_if_true_func=None,
        end_if_false_func=None,
        restart_if_true_func=None,
        restart_if_false_func=None,
    ):
        self.if_true_func = if_true_func
        self.if_false_func = if_false_func
        self.skip_if_true_func = skip_if_true_func
        self.skip_if_false_func = skip_if_false_func
        self.end_if_true_func = end_if_true_func
        self.end_if_false_func = end_if_false_func
        self.restart_if_true_func = restart_if_true_func
        self.restart_if_false_func = restart_if_false_func

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        """ Constants are called with no user-level args. """

        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if self.skip_if_true_func is None:
                    raise NoSkipOrReturnError
                return self.skip_if_true_func(skip_lines)
            if self.skip_if_false_func is None:
                raise NoSkipOrReturnError
            return self.skip_if_false_func(skip_lines)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                return self.if_false_func(condition)
            return self.if_true_func(condition)

        if end_event:
            if restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if self.end_if_false_func is None:
                    raise NoSkipOrReturnError
                return self.end_if_false_func()
            if self.end_if_true_func is None:
                raise NoSkipOrReturnError
            return self.end_if_true_func()

        if restart_event:
            if negate:
                if self.restart_if_false_func is None:
                    raise NoSkipOrReturnError
                return self.restart_if_false_func()
            if self.restart_if_true_func is None:
                raise NoSkipOrReturnError
            return self.restart_if_true_func()

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")


class EventArgumentData:
    """Holds event argument offset tuple, e.g. `(12, 4)`, and event argument type, e.g. `Region`.

    Passed to EMEVD instructions/tests so that arguments like `anchor_type` and `destination_type` do not need to be
    specified with properly type-annotated event arguments.
    """
    offset_tuple: tuple[int, int]
    arg_class: tp.Optional[tp.Type[GameObject]]

    def __init__(self, offset_tuple: tuple[int, int], arg_class: tp.Optional[tp.Type[GameObject]] = None):
        self.offset_tuple = offset_tuple
        self.arg_class = arg_class

    def get_coord_entity_type(self):
        if self.arg_class in {Object, Region, Character}:
            self.arg_class: tp.Union[Object, Region, Character]
            return self.arg_class.get_coord_entity_type()
        raise AttributeError(f"Event argument does not have a `CoordEntityType`.")


def get_value_test(
    value,
    negate=False,
    condition=None,
    skip_lines=0,
    end_event=False,
    restart_event=False,
    skip_if_true_func=None,
    skip_if_false_func=None,
    if_true_func=None,
    if_false_func=None,
    end_if_true_func=None,
    end_if_false_func=None,
    restart_if_true_func=None,
    restart_if_false_func=None,
):
    if skip_lines > 0:
        if condition is not None or end_event or restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if skip_if_true_func is None or skip_if_false_func is None:
            raise NoSkipOrReturnError  # Both of these functions must be defined.
        if negate:
            return skip_if_true_func(skip_lines, value)
        return skip_if_false_func(skip_lines, value)
    elif skip_lines < 0:
        raise ValueError("You cannot skip a negative number of lines.")

    if condition is not None:
        if end_event or restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if negate:
            if if_false_func is None:
                raise NoNegateError  # Some game types only have a positive condition test (e.g. IfObjectActivated).
            return if_false_func(condition, value)
        return if_true_func(condition, value)

    if end_event:
        if restart_event:
            raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
        if negate:
            if end_if_false_func is None:
                raise NoSkipOrReturnError
            return end_if_false_func(value)
        if end_if_true_func is None:
            raise NoSkipOrReturnError
        return end_if_true_func(value)

    if restart_event:
        if negate:
            if restart_if_false_func is None:
                raise NoSkipOrReturnError
            return restart_if_false_func(value)
        if restart_if_true_func is None:
            raise NoSkipOrReturnError
        return restart_if_true_func(value)

    raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")


def get_byte_offset_from_struct(format_string: str) -> dict[int, tuple[int, str]]:
    """Returns a dictionary mapping `byte_offset` to `(struct_index, struct_format)` tuples.

    The byte offsets indicate where the associated element in the struct format string begins. Note that native byte
    alignment "@" is critical here, as EMEVD uses byte-aligned packed binary data.
    """
    format_string = format_string.replace("|", "")
    byte_offset_array = {}
    for i in range(len(format_string)):
        offset = struct.calcsize("@" + format_string[:i + 1]) - struct.calcsize("@" + format_string[i])
        byte_offset_array[offset] = (i, format_string[i])
    return byte_offset_array


def get_instruction_args(
    reader: BinaryReader, category, index, first_arg_offset, event_args_size, format_dict
):
    """Process instruction arguments (required and optional) from EMEVD binary."""

    previous_offset = reader.position
    if event_args_size == 0:
        return "", []
    try:
        args_format = "@" + format_dict[category][index]
    except KeyError:
        raise KeyError(f"Cannot find argument types for instruction {category}[{index:02d}].")

    # 's' arguments are actually four-byte offsets into the packed string data, though we will keep the 's' symbol.
    struct_args_format = args_format.replace("s", "I")
    required_args_size = struct.calcsize(struct_args_format)
    if required_args_size > event_args_size:
        raise ValueError(
            f"Documented size of minimum required args for instruction {category}"
            f"[{index}] is {required_args_size}, but size of args specified in EMEVD file is "
            f"only {event_args_size}."
        )

    reader.seek(first_arg_offset)
    args = reader.unpack(struct_args_format)

    # Additional arguments may appear for the instruction 2000[00], 'RunEvent'. These instructions are tightly packed
    # and are always aligned to 4. We read them here as unsigned integers and must actually parse the called event ID to
    # interpret them properly (done at `EMEVD` class level).

    extra_size = event_args_size - required_args_size

    opt_arg_count = extra_size // 4
    if opt_arg_count == 0:
        reader.seek(previous_offset)
        return args_format[1:], list(args)
    elif extra_size % 4 != 0:
        raise ValueError(
            f"Error interpreting instruction {category}[{index}]: optional argument "
            f"size is not a multiple of four bytes ({extra_size})."
        )

    opt_args = [reader.unpack_value("<I") for _ in range(opt_arg_count)]
    reader.seek(previous_offset)
    return args_format[1:] + "|" + "I" * (extra_size // 4), list(args) + opt_args


def get_write_offset(event_format, arg_index) -> int:
    """Iterate over event format string to determine write offset of given argument index."""
    offset = 0
    for i, c in enumerate(event_format):
        if c in "Hh":
            if (offset % 2) != 0:
                # Fill in remainder of 2-byte chunk.
                offset += 1
        elif c in "Iif":
            while (offset % 4) != 0:
                # Fill in remainder of 4-byte chunk.
                offset += 1
        if i == arg_index:
            return offset
        if c in "Bb":
            offset += 1
        elif c in "Hh":
            offset += 2
        elif c in "Iif":
            offset += 4


def boolify(integer):
    """Converts argument to a boolean if it's 0 or 1; otherwise passes it through (e.g. for event args)."""
    if isinstance(integer, int):
        if integer == 0:
            return False
        elif integer == 1:
            return True
    return integer


def format_event_layers(event_layers):
    if event_layers is None:
        return ""
    if isinstance(event_layers, int):
        event_layers = [event_layers]
    if not isinstance(event_layers, (list, tuple)):
        raise TypeError
    return f"<" + ", ".join(str(i) for i in event_layers) + ">"


class EntityEnumsManager:

    class EntityEnumInfo:
        """Holds the enum and its origin information."""

        def __init__(self, enum: MapEntity, module_name: str, is_star: bool):
            self.enum = enum
            self.enum_class = enum.__class__
            self.class_name = enum.__class__.__name__
            self.module_name = module_name
            self.is_star = is_star

        @property
        def class_alias(self) -> str:
            # TODO: Currently using first six characters of module as alias prefix, under the assumption that it will be
            #  a properly named module (e.g. `from m10_02_entities import Characters as m10_02_Characters`).
            if self.is_star:
                return self.class_name
            return f"{self.module_name[:6]}_{self.class_name}"

        @property
        def import_string(self):
            if self.is_star:
                return f"{self.class_name}"
            return f"{self.class_name} as {self.class_alias}"

    class MissingEntityError(Exception):
        """Indicates an enum is missing, which should be handled by the caller."""

    # Subclasses for different games may add more types.
    ENTITY_ID_SUBCLASSES = {
        "parts": (MapPiece, Object, Character, PlayerStart, Collision),
        "events": (SoundEvent, VFXEvent, SpawnerEvent, MessageEvent, SpawnPointEvent, NavigationEvent),
        "regions": (RegionPoint, RegionCircle, RegionCylinder, RegionSphere, RegionRect, RegionBox),
    }

    enums: dict[str, dict[int, EntityEnumInfo]]

    def __init__(
        self,
        star_module_paths: tp.Sequence[tp.Union[str, Path]],
        non_star_module_paths: tp.Sequence[tp.Union[str, Path]],
    ):
        """Loads modules and monitors non-star enum usage for `EMEVD.to_evs()`.

        Parses all given `entities_modules` paths and build a dictionary mapping `MapEntity` type names to
        dictionaries mapping entity IDs to enum members (e.g. `{1510100: <Characters.BlackKnight3>}`).

        A `ValueError` will be raised if the same entity ID appears multiple times, regardless of entry type.
        """
        self.star_modules = {
            Path(path).name.split(".")[0]: import_arbitrary_file(path) for path in star_module_paths
        }
        self.non_star_modules = {
            Path(path).name.split(".")[0]: import_arbitrary_file(path) for path in non_star_module_paths
        }
        self.enums = {}

        self.used_star_modules = set()  # type: set[str]
        self.used_non_star_imports = {name: set() for name in self.non_star_modules}  # `modules: {EntityEnumInfo, ...}`
        self.missing_enums = set()  # type: set[tuple[str, int]]

        self.all_entity_ids = {}  # for warnings
        for entry_type, entity_classes in self.ENTITY_ID_SUBCLASSES.items():
            star_entry_type_ids = {}
            non_star_entry_type_ids = {}
            for entity_cls in entity_classes:
                self.enums[entity_cls.__name__] = {}
                for module_name, module in self.star_modules.items():
                    self._load_module_enums(
                        module, module_name, entity_cls, entry_type, star_entry_type_ids, non_star_entry_type_ids, True
                    )
                for module_name, module in self.non_star_modules.items():
                    self._load_module_enums(
                        module, module_name, entity_cls, entry_type, star_entry_type_ids, non_star_entry_type_ids, False
                    )

    def check_out_enum(
        self, entity_id: int, *entity_cls_names: tp.Sequence[tp.Union[str, tp.Type[MapEntity]]], any_class=False
    ) -> str:
        """Attempt to check out an enum with one of the given `entity_cls_names` and `entity_id`.

        Raises a `MissingEntityError` if the entity ID is not found. Otherwise, marks the enum's module (and name for
        non-star imports) as used for the final EVS import lines. Raises `KeyError` if type name is invalid.

        If "Region" is given in `entity_cls_names`, all region subtypes will automatically be checked.

        Args:
            entity_id (int): entity ID to check out.
            entity_cls_names (str or MapEntity): names of entity classes to check, e.g. "RegionBox", "Character",
                "SoundEvent", or just the class itself.
            any_class (bool): if True, insted
        """
        if not entity_cls_names:
            if not any_class:
                raise ValueError("At least one `entity_cls_names` argument must be given (or `any_class=True`).")
            entity_cls_names = [cls.__name__ for classes in self.ENTITY_ID_SUBCLASSES.values() for cls in classes]
        elif any_class:
            raise ValueError("If `any_class=True`, do not give any `entity_cls_names` arguments.")
        else:
            entity_cls_names = [cls.__name__ if not isinstance(cls, str) else cls for cls in entity_cls_names]

        enum_info = None
        for cls_name in entity_cls_names:
            if cls_name == "Region":
                for region_subtype_name in (cls.__name__ for cls in self.ENTITY_ID_SUBCLASSES["regions"]):
                    try:
                        enum_info = self.enums[region_subtype_name][entity_id]
                        break
                    except KeyError:
                        pass
                if enum_info:
                    break
            elif cls_name == "MapPart":
                for part_subtype_name in (cls.__name__ for cls in self.ENTITY_ID_SUBCLASSES["parts"]):
                    try:
                        enum_info = self.enums[part_subtype_name][entity_id]
                        break
                    except KeyError:
                        pass
                if enum_info:
                    break
            elif cls_name not in self.enums:
                raise KeyError(f"Invalid entity class name for entity enums: '{cls_name}'")
            else:
                try:
                    enum_info = self.enums[cls_name][entity_id]
                    break
                except KeyError:
                    pass
        else:
            # Entity ID not found under any of the given classes.
            all_cls_names = "Any" if any_class else " | ".join(entity_cls_names)
            self.missing_enums.add((all_cls_names, entity_id))
            raise EntityEnumsManager.MissingEntityError(f"Missing `{all_cls_names}` entity ID: {entity_id}")

        if enum_info.is_star:
            self.used_star_modules.add(enum_info.module_name)
        else:
            self.used_non_star_imports[enum_info.module_name].add(enum_info)
        return f"{enum_info.class_alias}.{enum_info.enum.name}"

    def _load_module_enums(
        self,
        module: types.ModuleType,
        module_name: str,
        entity_cls: tp.Type[MapEntity],
        entry_type: str,
        star_entry_type_ids: dict[int, str],
        non_star_entry_type_ids: dict[int, str],
        is_star: bool,
    ):
        for enum_name, enum_class in self._get_subclasses_in_module(module, entity_cls):
            for member in enum_class:
                if member.value in star_entry_type_ids:
                    if is_star:
                        raise ValueError(
                            f"Entity ID {member.value} in enum `{enum_name}` already defined by enum "
                            f"`{star_entry_type_ids[member.value]}` of same entry type ({entry_type}) in a star import."
                        )
                    else:
                        continue  # ignore member (star import has priority)
                elif member.value in non_star_entry_type_ids:
                    if is_star:
                        pass  # will overwrite non-star member in `self.enums` below
                    else:
                        # Entity ID appears in multiple non-star imports, so we wouldn't know which to use if it was
                        # ever referenced in the present EVS script (which, of course, it generally won't be).
                        if member.value not in star_entry_type_ids and member.value in self.enums:
                            self.enums.pop(member.value)  # remove existing non-star enum (rather than use a random one)
                        continue  # skip member
                elif member.value in self.all_entity_ids:
                    existing_entry_type, existing_enum_name = self.all_entity_ids[member.value]
                    _LOGGER.info(
                        f"Entity ID {member.value} in enum `{enum_name}` (in {entry_type}) is already "
                        f"defined by enum `{existing_enum_name}` (in {existing_entry_type}). This "
                        f"shouldn't cause an issue, but it may cause you headaches."
                    )
                if member.value in [p.value for p in PlayerEntity]:
                    raise ValueError(
                        f"Entity ID {member.value} in enum `{enum_name}` is a protected entity ID: "
                        f"{PlayerEntity(member.value)}."
                    )
                self.all_entity_ids[member.value] = (entry_type, enum_name)
                enum_info = self.EntityEnumInfo(member, module_name, is_star)
                if is_star:
                    star_entry_type_ids[member.value] = enum_name
                else:
                    non_star_entry_type_ids[member.value] = enum_name
                self.enums[entity_cls.__name__][member.value] = enum_info

    @staticmethod
    def _get_subclasses_in_module(
            module: types.ModuleType, entity_class: tp.Type[MapEntity]
    ) -> list[tuple[str, tp.Type[MapEntity]]]:
        """Return a dictionary of `entity_class` subclasses from given `module`"""
        return inspect.getmembers(module, lambda o: inspect.isclass(o) and issubclass(o, entity_class))
