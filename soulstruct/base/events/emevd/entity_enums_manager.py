from __future__ import annotations

__all__ = [
    "EntityEnumInfo",
    "EntityEnumsManager",
]

import abc
import inspect
import logging
import types
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


class EntityEnumsManager(abc.ABC):

    class MissingEntityError(Exception):
        """Indicates an enum is missing, which should be handled by the caller."""

    ENTITY_ID_SUBCLASSES: dict[str, tuple[tp.Type[MapEntity], ...]]
    PROTECTED_ENTITIES: tp.Type[IntEnum]

    __CACHED_MODULE_CLASSES = {}

    enums: dict[str, dict[int, EntityEnumInfo]]
    all_event_ids: list[int]
    all_common_event_ids: list[int]

    def __init__(
        self,
        star_module_paths: tp.Sequence[str | Path],
        non_star_module_paths: tp.Sequence[str | Path],
        all_event_ids: list[int],
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
        self.all_event_ids = all_event_ids
        self.all_common_event_ids = []  # added separately

        self.used_star_modules = set()  # type: set[str]
        self.used_non_star_imports = {name: set() for name in self.non_star_modules}  # `modules: {EntityEnumInfo, ...}`
        self.missing_enums = set()  # type: set[tuple[str, int]]

        self.all_entity_ids = {}  # for warnings

        if self.star_modules or self.non_star_modules:
            self.refresh_enums()

    def refresh_enums(self):
        self.enums = {}
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
        if not self.enums:
            raise self.MissingEntityError(f"No enums loaded in `EntityEnumsManager`.")

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
                raise self.MissingEntityError(f"Invalid entity class name for entity enums: {cls_name}")
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
            raise self.MissingEntityError(f"Missing `{all_cls_names}` entity ID: {entity_id}")

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
                        if member.value not in star_entry_type_ids and member.name in self.enums:
                            self.enums.pop(member.name)  # remove existing non-star enum (rather than use a random one)
                        continue  # skip member
                elif member.value in self.all_entity_ids:
                    existing_entry_type, existing_enum_name = self.all_entity_ids[member.value]
                    _LOGGER.info(
                        f"Entity ID {member.value} in enum `{enum_name}` (in {entry_type}) is already "
                        f"defined by enum `{existing_enum_name}` (in {existing_entry_type}). This "
                        f"shouldn't cause a fatal issue, but it may cause you headaches."
                    )
                if member.value in [p.value for p in self.PROTECTED_ENTITIES]:
                    raise ValueError(
                        f"Entity ID {member.value} in enum `{enum_name}` is a protected entity ID: "
                        f"{self.PROTECTED_ENTITIES(member.value)}."
                    )
                self.all_entity_ids[member.value] = (entry_type, enum_name)
                enum_info = EntityEnumInfo(member, module_name, is_star)
                if is_star:
                    star_entry_type_ids[member.value] = enum_name
                else:
                    non_star_entry_type_ids[member.value] = enum_name
                self.enums[entity_cls.__name__][member.value] = enum_info

    @classmethod
    def _get_subclasses_in_module(
        cls,
        module: types.ModuleType,
        entity_class: tp.Type[MapEntity],
    ) -> list[tuple[str, tp.Type[MapEntity]]]:
        """Return a dictionary of `entity_class` subclasses from given `module`."""
        if (module.__file__, entity_class) in cls.__CACHED_MODULE_CLASSES:
            return cls.__CACHED_MODULE_CLASSES[module.__file__, entity_class]
        enum_names_classes = cls.__CACHED_MODULE_CLASSES[module.__file__, entity_class] = inspect.getmembers(
            module, lambda o: inspect.isclass(o) and issubclass(o, entity_class)
        )
        return enum_names_classes
