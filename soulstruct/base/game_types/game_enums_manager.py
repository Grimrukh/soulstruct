from __future__ import annotations

__all__ = [
    "GameEnumInfo",
    "GameEnumsManager",
]

import abc
import inspect
import logging
import typing as tp
from enum import Enum, IntEnum
from pathlib import Path
from types import ModuleType

from soulstruct.utilities.files import import_arbitrary_file
from soulstruct.base.game_types import *

_LOGGER = logging.getLogger("soulstruct")


class GameEnumInfo:
    """Holds the enum and its origin information."""

    def __init__(self, enum: Enum, module_name: str):
        self.enum = enum
        self.enum_class = enum.__class__
        self.class_name = enum.__class__.__name__
        self.module_name = module_name

    def get_variable_string(self, star_module_names: list[str]) -> str:
        """String that should appear in actual EVS calls."""
        if self.module_name in star_module_names:
            return f"{self.class_name}.{self.enum.name}"  # no module prefix alias needed
        return f"{self.get_class_alias()}.{self.enum.name}"

    def get_class_alias(self) -> str:
        # TODO: Currently using first six characters of module as alias prefix, under the assumption that it will be
        #  a properly named module (e.g. `from m10_02_enums import Characters as m10_02_Characters`).
        if self.module_name.startswith("common") and self.class_name.lower().startswith("common"):
            return self.class_name  # no need for an alias
        return f"{self.module_name[:6]}_{self.class_name}"

    def get_import_string(self) -> str:
        """Only called for non-star imports."""
        class_alias = self.get_class_alias()
        if class_alias == self.class_name:
            return f"{self.class_name}"  # no alias
        return f"{self.class_name} as {class_alias}"  # import alias (may be a generic class name)

    def __repr__(self):
        return f"GameEnumInfo({self.class_name}.{self.enum.name}<{self.enum.value}>, alias={self.get_class_alias()})"


class GameEnumsManager(abc.ABC):
    """Manages `IntEnum`s loaded from one or more modules and allows them to be used during `EVS` decompilation.

    Also used by the GUI to link to the Maps tab.
    """

    class EnumManagerError(Exception):
        """Base class."""

    class MissingEnumTypeError(EnumManagerError):
        """Indicates an enum game type is completely missing, which is generally harmless."""

    class EnumValueRepeatError(EnumManagerError):
        """Indicates an enum value occurred more than once in a star-import, which is an error."""

    class MissingEnumValueError(EnumManagerError):
        """Indicates a specific enum value is missing from a known game type, which you might want to remedy."""
        missing_enum_game_types: str
        enum_value: int

        def __init__(self, game_types: tp.Sequence[GAME_INT_TYPE], enum_value: int):
            self.missing_enum_game_types = "Any" if not game_types else " | ".join(gt.__name__ for gt in game_types)
            self.enum_value = enum_value
            super().__init__(f"Missing `{self.missing_enum_game_types}` enum value: {enum_value}")

    class AmbiguousEnumValueError(EnumManagerError):
        """Indicates a specific enum value was found in multiple NON-STAR modules, and should not be used."""

    # List of `GameObjectInt` types that are valid enum keys (e.g. can appear as EMEVD instruction/event arguments).
    VALID_GAME_TYPES: dict[GAME_INT_TYPE, dict[int, GameObjectInt]]

    # Maps module stems (e.g. 'm10_01_00_00_enums') to dictionaries mapping game types to `{value: GameEnumInfo}`
    # dictionaries. When an enum is checked out, a 'star_module' can be passed, which will be checked first. If the
    # enum is not found there, the other modules will be checked; if found THERE, only the used enum names will be
    # imported into EVS from that non-star module.
    enums: dict[str, dict[GAME_INT_TYPE, dict[int, GameEnumInfo]]]
    all_event_ids: list[int]
    all_common_event_ids: list[int]

    # Added whenever `checkout_enum()` has a hit. Can be manually cleared and monitored by caller.
    used_enums: list[GameEnumInfo]
    star_module_names: list[str]

    def __init__(self, module_paths: tp.Sequence[str | Path], all_event_ids: list[int] = None):
        """Loads modules and monitors non-star enum usage for `EMEVD.to_evs()`.

        Parses all given `module_paths` and builds nested dictionary mapping module stems to game types to enum values.
        # Example: `enums["m15_01_00_00_enums"][Character][1510100] = <Characters.BlackKnight3>`

        When the `checkout_enum()` method is used during EMEVD -> EVS decompilation, the given `star_module` (if any)
        will be checked first -- usually the enums module associated directly with that EMEVD map -- and other modules
        will only be checked if not found in the star module. The `module_name` attribute of the returned `GameEnumInfo`
        instance indicates which module was used, which can be used to construct star and non-star EVS imports.

        The same enum may safely appear in multiple `enums[module]` when parent/child types are involved -- e.g. a
        `Character` enum will appear under the `Character` itself but also the parent `MapPart` key -- but otherwise,
        conflicting values will log warnings or (if under the exact same child type key) raise a `ValueError`.
        """
        self.modules = {Path(path).name.split(".")[0]: import_arbitrary_file(path) for path in module_paths}
        self.enums = {module_stem: {} for module_stem in self.modules}
        self.all_event_ids = [] if all_event_ids is None else all_event_ids
        self.all_common_event_ids = []  # added separately

        # For generating final import statements.
        # TODO: Move to EVS decompiler process. Just track all enums checked out and their 'module_name' attributes.
        # self.used_star_modules = set()  # type: # set[str]
        # self.used_non_star_imports = {name: set() for name in self.non_star_modules}  # `modules: {EnumInfo, ...}`

        # For inspection/warning.
        self.missing_enums = set()  # type: set[tuple[str, int]]

        # Maps `int` enum values to `(entry_type, enum_class)` pairs, to track ID sources and warn about non-fatal
        # overlaps. (Fatal overlaps will raise an exception immediately.)
        self.all_enum_values = {}

        # Default. Can be set by user.
        self.used_enums = []
        self.star_module_names = []

        if self.modules:
            self.refresh_enums()

    def refresh_enums(self):
        """Completely regenerate `enums` dictionary from all registered modules."""
        self.enums = {module_stem: {} for module_stem in self.modules}

        # Iterate over all module members and find those inheriting from a type in `VALID_GAME_TYPES`.
        for module_name, module in self.modules.items():
            self._load_module(module_name, module)

    def get_sorted_missing_items(self) -> list[tuple[str, int]]:
        """Sort `missing_items` and remove all occurrences of each entity ID except the most strictly typed one."""
        strictest_items = {}  # type: dict[int, list[str]]
        disjoint_items = []
        for item in self.missing_enums:
            split_types = item[0].split(" | ")
            existing_types = strictest_items.get(item[1], None)
            if existing_types is None or existing_types == ["Any"]:
                strictest_items[item[1]] = split_types  # first occurrence, or current type is least-strict 'Any'
                continue
            if split_types == ["Any"]:
                continue  # ignore
            # Check if new types are a subset of existing types.
            split_types_set = set(split_types)
            existing_types_set = set(existing_types)
            if split_types_set.issubset(existing_types_set):
                strictest_items[item[1]] = split_types  # stricter types encountered
                continue
            elif not existing_types_set.issubset(split_types_set):
                # New types encountered that aren't a subset OR superset of existing types. Add manually.
                disjoint_items.append(item)

        return sorted([(" | ".join(types), value) for value, types in strictest_items.items()] + disjoint_items)

    @staticmethod
    def _get_module_members(module_name: str, module: ModuleType):
        return inspect.getmembers(
            module,
            lambda o: (
                inspect.isclass(o) and issubclass(o, GameObjectInt)
                and (not o.__module__ or o.__module__.endswith(module_name))
            )
        )

    def _check_existing_enum_value(self, module_name: str, game_type: GAME_INT_TYPE, enum_member: IntEnum):
        """Checks if this `enum_member.value` already exists ANYWHERE in any modules.

        Logs a warning if the same value is found in a different module, but only if the enum value is seven or more
        digits (rather than, say, a reused NPC entity ID like 6000).

        Also logs a warning if the same value already exists with a different enum type. Note that this has plenty of
        vanilla occurrences, even though I consider it bad practice! (Sorry FromSoft.)
        """
        if enum_member.value not in self.all_enum_values:
            self.all_enum_values[enum_member.value] = (module_name, game_type, enum_member.__class__)
            return

        existing_module_name, existing_game_type, existing_enum_type = self.all_enum_values[enum_member.value]
        if game_type in existing_enum_type.__mro__ or existing_enum_type in game_type.__mro__:
            # Type match (one is child of the other). Only warn if they are in different modules and the enum value is
            # seven or more digits (rather than, say, a reused NPC entity ID like 6000).
            if existing_module_name != module_name and enum_member.value >= 1_000_000:
                _LOGGER.warning(
                    f"Enum value {enum_member.value} of type `{enum_member.__class__.__name__}` (for argument type "
                    f"`{game_type.__name__}`) was defined in module '{module_name}' after already being defined in "
                    f"module '{existing_module_name}'. Harmless, but potentially redundant, as cross-map imports "
                    f"are supported by EVS decompilation."
                )
        else:
            _LOGGER.warning(
                f"Enum value {enum_member.value} of type `{enum_member.__class__.__name__}` (for argument type "
                f"`{game_type.__name__}`) in module '{module_name}' was already defined with type "
                f"`{existing_enum_type.__name__}` (for argument type `{existing_game_type.__name__}`) in module "
                f"'{existing_module_name}'. This shouldn't cause a game issue, but it may cause you headaches."
            )

    def _parse_game_type_enum(
        self,
        module_name: str,
        game_type: GAME_INT_TYPE,
        enum_member: IntEnum,
    ):
        if issubclass(game_type, MapEntity):
            if self._is_protected(enum_member):
                raise ValueError(
                    f"Enum value {enum_member.value} of `MapEntity` child type `{enum_member.__class__.__name__}` "
                    f"is a protected value and must be changed."
                )

        self._check_existing_enum_value(module_name, game_type, enum_member)

        enum_dict = self.enums[module_name].setdefault(game_type, {})
        enum_dict[enum_member.value] = GameEnumInfo(enum_member, module_name)

    def _load_module(self, module_name: str, module: ModuleType):
        """Iterate over all `GameObjectInt`-inheriting classes in `module` and register their IDs and values.

        Note that the same enum members may appear under multiple keys, as each class in each game type's hierarchy can
        appear as a dictionary key (e.g. `RegionVolume` members will also appear under the `Region` key if both are in
        `VALID_GAME_TYPES`).
        """
        self.enums[module_name] = {}  # reset
        for game_enum_name, game_enum_class in self._get_module_members(module_name, module):
            game_enum_class: GAME_INT_TYPE | tp.Iterable

            match_found = False
            for enum_member in game_enum_class:
                # We check each registered game type, as some may be hierarchical.
                for game_type in self.VALID_GAME_TYPES:
                    if game_type in game_enum_class.__mro__:
                        match_found = True
                        self._parse_game_type_enum(module_name, game_type, enum_member)

            if not match_found:
                _LOGGER.warning(
                    f"Ignoring game enum type `{game_enum_name}` in module '{module.__file__}`, as its type does not "
                    f"match any of the `VALID_GAME_TYPES` specified for this `GameEnumsManager`."
                )

    def check_out_enum(
        self,
        enum_value: int,
        *game_types: GAME_INT_TYPE | tp.Sequence[GAME_INT_TYPE],
        star_module_names: tp.Sequence[str] = None,
    ) -> GameEnumInfo:
        """Attempt to check out an enum with one of the given `game_types` and `enum_value`.

        If `star_module_names` is given, those module names will be checked first. If there are multiple hits in these
        modules, an `EnumValueRepeatError` will be raised, as the imported value in the EVS script will be unacceptably
        ambiguous. If there are NO hits in star modules and multiple hits in other, non-star modules, a warning will be
        logged and none of those enums will be checked out.

        Raises a `MissingEnumTypeError` if none of the game types are present at all, and `MissingEnumValueError` if a
        game type is present but the specific value is not.

        Args:
            enum_value (int): entity ID to check out.
            game_types: names/types of game types to check, e.g. `RegionBox`, `Flag`, etc. If empty, all types will be
                checked (e.g. for entity IDs of completely unknown type).
            star_module_names (Sequence): one or more names of modules that will be star-imported in this EVS script
                and should be checked first.
        """
        if not self.enums:
            raise self.MissingEnumTypeError("No enums loaded in `GameEnumsManager`.")

        if star_module_names is None:
            star_module_names = self.star_module_names

        if not game_types:
            # Check ALL valid game types.
            is_any = True
            game_types = []
            for module_enums in self.enums.values():
                game_types.extend(module_enums.keys())  # all enums in all modules (star modules still checked first)
        else:
            is_any = False

        # Search all managed modules for given `enum_value`, starting with `star_module_names`.
        # NOTE: To ensure maximum validity, we do NOT simply stop at the first hit (see docstring above for details).

        type_found = False
        star_hits = []
        if star_module_names:
            for star_module_name in star_module_names:
                if star_module_name not in self.enums:
                    raise KeyError(f"Module name '{star_module_name}' was not loaded by this `GameEnumsManager`.")
                module_enums = self.enums[star_module_name]
                for game_type in game_types:
                    if game_type not in module_enums:
                        continue
                    type_found = True
                    # Type has been found. Look for matching value within.
                    try:
                        enum_info = module_enums[game_type][enum_value]
                        star_hits.append(enum_info)
                    except KeyError:
                        continue  # value not found; try other `game_types`

        if len(star_hits) > 1:
            msg = "\n    ".join(repr(info) for info in star_hits)
            raise self.EnumValueRepeatError(
                f"Enum value {enum_value} was defined more than once across the given star modules:\n    {msg}"
            )
        if len(star_hits) == 1:
            if star_hits[0] not in self.used_enums:
                self.used_enums.append(star_hits[0])
            return star_hits[0]

        # Try other modules.
        non_star_hits = []
        for module_name in self.enums:
            if module_name in star_module_names:
                continue  # already checked above
            module_enums = self.enums[module_name]
            for game_type in game_types:
                if game_type not in module_enums:
                    continue
                type_found = True
                # Type has been found. Look for matching value within.
                try:
                    enum_info = module_enums[game_type][enum_value]
                    non_star_hits.append(enum_info)
                except KeyError:
                    continue  # value not found; try other `game_types`

        if len(non_star_hits) > 1:
            # TODO: Severity of this probably mostly depends on whether any restricted `game_types` were given. If not,
            #  this was already a hail mary; but if so, we do expect to find only one valid value for this game type...
            raise self.AmbiguousEnumValueError(
                f"Enum value {enum_value} appears in multiple non-star modules and cannot be resolved. Raw value "
                f"should be kept in EVS script."
            )
        if len(non_star_hits) == 1:
            if non_star_hits[0] not in self.used_enums:
                self.used_enums.append(non_star_hits[0])
            return non_star_hits[0]

        if not type_found:
            # NOTE: Only possible if some `game_types` were given, as otherwise they will be the same by definition.
            raise self.MissingEnumTypeError(
                f"No enums available for any of the given game types: `{[gt.__name__ for gt in game_types]}`."
            )

        # Types were found, but enum value not found under any of them.
        ex = self.MissingEnumValueError(game_types, enum_value)
        if is_any:
            self.missing_enums.add(("Any", ex.enum_value))
        else:
            self.missing_enums.add((ex.missing_enum_game_types, ex.enum_value))
        raise ex

    def check_out_enum_variable(
        self,
        enum_value: int,
        *game_types: GAME_INT_TYPE | tp.Sequence[GAME_INT_TYPE],
        star_module_names: tp.Sequence[str] = None,
    ) -> str:
        """Calls `check_out_enum()` but only returns `enum_info.get_variable_string()`."""

        # First, we check for protected PLAYER values.
        if enum_value == 10000:
            return "PLAYER"
        if 10001 <= enum_value <= 10009:
            return f"CLIENT_PLAYER_{enum_value - 10000}"

        if not star_module_names:
            star_module_names = self.star_module_names
        game_enum_info = self.check_out_enum(enum_value, *game_types, star_module_names=star_module_names)
        return game_enum_info.get_variable_string(star_module_names)

    def get_import_lines(self, star_module_names: tp.Collection[str], module_prefix: str) -> str:
        if not self.used_enums:
            _LOGGER.warning("No enums used by `GameEnumsManager` for import lines.")
            return ""

        imported_star = set()
        non_star_imports = {}
        imports = ""
        for used_enum in self.used_enums:
            if used_enum.module_name in star_module_names:
                if used_enum.module_name not in imported_star:
                    imports += f"\nfrom {module_prefix}{used_enum.module_name} import *"
                    imported_star.add(used_enum.module_name)
            else:
                # Non-star import.
                non_star_imports.setdefault(used_enum.module_name, set()).add(used_enum.get_import_string())
        for module_name in sorted(non_star_imports):
            sorted_aliases = sorted(non_star_imports[module_name])
            import_prefix = f"\nfrom {module_prefix}{module_name} import "
            one_line_suffix = ", ".join(sorted_aliases)
            if len(import_prefix + one_line_suffix) > 119:
                # Split across multiple lines.
                multi_line_imports = "\n    ".join(sorted_aliases)
                imports += f"{import_prefix}(\n    {multi_line_imports}\n)"
            else:
                imports += f"{import_prefix}{one_line_suffix}"

        return imports

    @staticmethod
    def _is_protected(value: int) -> bool:
        """Only checked for `MapEntity` (entity ID) enums."""
        return 10000 <= value <= 10010

    # TODO: Module-writing method.
