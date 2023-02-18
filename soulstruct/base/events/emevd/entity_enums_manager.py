from __future__ import annotations

__all__ = [
    "EntityEnumInfo",
    "GameEnumsManager",
]

import abc
import inspect
import logging
import typing as tp
from enum import Enum, IntEnum
from pathlib import Path

from soulstruct.utilities.files import import_arbitrary_file
from soulstruct.base.game_types import *

_LOGGER = logging.getLogger(__name__)


class EntityEnumInfo:
    """Holds the enum and its origin information."""

    def __init__(self, enum: Enum, module_name: str, is_star: bool):
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
        elif self.module_name.startswith("common") and self.class_name.lower().startswith("common"):
            return self.class_name
        return f"{self.module_name[:6]}_{self.class_name}"

    @property
    def import_string(self):
        if self.class_alias == self.class_name:
            return f"{self.class_name}"
        return f"{self.class_name} as {self.class_alias}"

    def __repr__(self):
        return f"EntityEnumInfo({self.class_name}, alias={self.class_alias}, is_star={self.is_star})"


class GameEnumsManager(abc.ABC):
    """Manages `IntEnum`s loaded from one or more modules and allows them to be used during `EVS` decompilation."""

    class EnumManagerError(Exception):
        """Base class."""

    class MissingEnumTypeError(EnumManagerError):
        """Indicates an enum game type is completely missing, which is generally harmless."""

    class EnumValueRepeatError(EnumManagerError):
        """Indicates an enum value occurred more than once in a star-import, which is an error."""

    class MissingEnumValueError(EnumManagerError):
        """Indicates a specific enum value is missing from a known game type, which you might want to remedy."""

    # List of `BaseGameObject` types that are valid enum keys (e.g. can appear as EMEVD instruction/event arguments).
    VALID_GAME_TYPES: dict[tp.Type[BaseGameObject], dict[int, BaseGameObject]]
    # No loaded enum members are permitted to overlap with values in this `IntEnum` (e.g. `PLAYER = 10000`).
    PROTECTED_ENUM: tp.Type[IntEnum]

    enums: dict[tp.Type[BaseGameObject], dict[int, EntityEnumInfo]]
    all_event_ids: list[int]
    all_common_event_ids: list[int]

    def __init__(
        self,
        star_module_paths: tp.Sequence[str | Path],
        non_star_module_paths: tp.Sequence[str | Path],
        all_event_ids: list[int],
    ):
        """Loads modules and monitors non-star enum usage for `EMEVD.to_evs()`.

        Parses all given `star_module_paths` and `non_star_module_paths` and builds a dictionary mapping game types
        (which may cover multiple subclasses) to dictionaries that, in turn, map enum ID values to enum members (e.g.
        `{1510100: <Characters.BlackKnight3>}`).

        Note that `star_module_paths` will appear as star imports in the decompiled EVS (generally a map-specific
        module), whereas `non_star_module_paths` will only have USED names imported from them (generally a few flags
        borrowed from other maps). If an ID appears in both types of module, the `star` module wins, and that ID's
        enum will not be imported from the `non_star` module.

        The same enum may appear in multiple `enums` keys, e.g. a `Character` enum can appear under both a specific
        `Character` key and a broader `MapPart` key.

        A `ValueError` will be raised if the same enum value appears multiple times within any single `enums` key. If
        the same value appears in different entries, a warning will be logged instead.
        """
        self.star_modules = {
            Path(path).name.split(".")[0]: import_arbitrary_file(path) for path in star_module_paths
        }
        self.non_star_modules = {
            Path(path).name.split(".")[0]: import_arbitrary_file(path) for path in non_star_module_paths
        }
        self.enums = {}
        self.all_event_ids = all_event_ids
        self.all_common_event_ids = []  # added separately
        self.protected_values = [p.value for p in self.PROTECTED_ENUM]

        # For generating final import statements.
        self.used_star_modules = set()  # type: set[str]
        self.used_non_star_imports = {name: set() for name in self.non_star_modules}  # `modules: {EntityEnumInfo, ...}`

        # For inspection/warning.
        self.missing_enums = set()  # type: set[tuple[str, int]]

        # Maps `int` enum values to `(entry_type, enum_class)` pairs, to track ID sources and warn about non-fatal
        # overlaps. (Fatal overlaps will raise an exception immediately.)
        self.all_enum_values = {}

        if self.star_modules or self.non_star_modules:
            self.refresh_enums()

    def refresh_enums(self):
        """Completely regenerate `enums` dictionary from all registered modules."""
        self.enums = {}

        # Iterate over all module members and find those inheriting from a type in `VALID_GAME_TYPES`.

        # These track sources of individual enum values from star and non-star module imports, per game type.
        # Two star sources are not allowed and will raise a `ValueError`. One star source will override all non-star
        # sources. Two non-star sources means all of them will be ignored (ambiguous).
        type_star_sources = {}
        type_non_star_sources = {}

        for module_name, module in self.star_modules.items():
            self._load_module(module_name, module, type_star_sources, type_non_star_sources, True)

        for module_name, module in self.non_star_modules.items():
            self._load_module(module_name, module, type_star_sources, type_non_star_sources, False)

    def _load_module(
        self,
        module_name: str,
        module,
        type_star_sources: dict[tp.Type[BaseGameObject], dict[int, str]],
        type_non_star_sources: dict[tp.Type[BaseGameObject], dict[int, str]],
        is_star: bool,
    ):
        for game_enum_name, game_enum_class in inspect.getmembers(
            module,
            lambda o: (
                inspect.isclass(o) and issubclass(o, BaseGameObject)
                and (not o.__module__ or o.__module__.endswith(module_name))
            )
        ):
            game_enum_class: tp.Type[BaseGameObject] | tp.Iterable

            match_found = False
            for member in game_enum_class:
                for game_type in self.VALID_GAME_TYPES:
                    # We check each registered game type, as some may be hierarchical.
                    if game_type not in game_enum_class.__mro__:
                        continue
                    match_found = True
                    enum_dict = self.enums.setdefault(game_type, {})
                    star_sources = type_star_sources.setdefault(game_type, {})
                    non_star_sources = type_non_star_sources.setdefault(game_type, {})

                    if member.value in star_sources:
                        if is_star:
                            raise self.EnumValueRepeatError(
                                f"Entity ID {member.value} in enum `{game_enum_name}` already defined by enum "
                                f"`{star_sources[member.value]}` of same entry type ({game_type.__name__}) in a "
                                f"star import."
                            )
                        else:
                            continue  # ignore member (star import has priority)
                    elif member.value in non_star_sources:
                        if is_star:
                            pass  # will overwrite non-star member in `self.enums` below
                        else:
                            # Entity ID appears in multiple non-star imports, so we wouldn't know which to use if
                            # it was ever referenced in the present EVS script (which, of course, it generally won't
                            # be).
                            if member.value not in star_sources and member.value in enum_dict:
                                # Remove existing non-star enum (rather than use a random one).
                                enum_dict.pop(member.value)
                            continue  # skip member
                    elif member.value in self.all_enum_values:
                        existing_entry_type, existing_enum_class = self.all_enum_values[member.value]
                        if game_type not in existing_enum_class.__mro__ and existing_enum_class not in game_type.__mro__:
                            _LOGGER.info(
                                f"Entity ID {member.value} in enum `{game_enum_name}` (for {game_type.__name__}) is "
                                f"already defined by enum `{existing_enum_class.__name__}` (in "
                                f"{existing_entry_type.__name__}). This shouldn't cause a game issue, but it may cause "
                                f"you headaches."
                            )
                    if member.value in self.protected_values:
                        raise ValueError(
                            f"Entity ID {member.value} in enum `{game_enum_name}` is a protected entity ID: "
                            f"{self.PROTECTED_ENUM(member.value)}."
                        )

                    self.all_enum_values[member.value] = (game_type, game_enum_class)

                    enum_info = EntityEnumInfo(member, module_name, is_star)
                    if is_star:
                        star_sources[member.value] = game_enum_name
                    else:
                        non_star_sources[member.value] = game_enum_name
                    enum_dict[member.value] = enum_info

            if not match_found:
                _LOGGER.warning(
                    f"Ignoring game enum type `{game_enum_name}` in module '{module.__file__}`, as it is not "
                    f"registered as a valid enum type for EMEVD."
                )

    def check_out_enum(
        self,
        enum_value: int,
        *game_types: tp.Type[BaseGameObject] | tp.Sequence[tp.Type[BaseGameObject]],
        any_class=False,
    ) -> str:
        """Attempt to check out an enum with one of the given `entity_cls_names` and `entity_id`.

        Raises a `MissingEnumError` if the entity ID is not found. Otherwise, marks the enum's module (and name for
        non-star imports) as used for the final EVS import lines. Raises `KeyError` if type name is invalid.

        NOTE: If "Region" is given in `entity_cls_names`, all region subtypes will automatically be checked, as region
        typed arguments are NEVER subtype-specific.

        Args:
            enum_value (int): entity ID to check out.
            game_types (str or BaseGameObject): names/types of game types to check, e.g. `RegionBox`, `Flag`, etc.
            any_class (bool): if True, check aLL available enum types in `enums`.
        """
        if not self.enums:
            raise self.MissingEnumTypeError("No enums loaded in `GameEnumsManager`.")

        if not game_types:
            if not any_class:
                raise ValueError("At least one `game_types` argument must be given (or `any_class=True`).")
            game_types = list(self.enums.keys())  # all keys
        elif any_class:
            raise ValueError("If `any_class=True`, do not give any `game_types` arguments.")

        type_valid = False
        for game_type in game_types:
            if game_type not in self.enums:
                # No enums managed for this game type.
                continue
            try:
                type_valid = True
                enum_info = self.enums[game_type][enum_value]
                break  # found
            except KeyError:
                continue  # try other passed-in (or any) game types
        else:
            if not type_valid:
                raise self.MissingEnumValueError(
                    f"No enums available for any of the given game types: `{[gt.__name__ for gt in game_types]}`."
                )
            # Entity ID not found under any of the given classes.
            all_cls_names = "Any" if any_class else " | ".join(gt.__name__ for gt in game_types)
            self.missing_enums.add((all_cls_names, enum_value))
            raise self.MissingEnumValueError(f"Missing `{all_cls_names}` enum value: {enum_value}")

        if enum_info.is_star:
            self.used_star_modules.add(enum_info.module_name)
        else:
            self.used_non_star_imports[enum_info.module_name].add(enum_info)
        return f"{enum_info.class_alias}.{enum_info.enum.name}"
