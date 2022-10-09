from __future__ import annotations

__all__ = [
    "PartIndicesData",
    "PartNamesData",
    "MSB_ModelName",
    "MSB_DrawGroups",
    "MSB_DisplayGroups",
    "MSB_NavmeshGroups",
    "MSB_BackreadGroups",
    "MSB_DrawParent",
    "MSB_Scale",
    "BaseMSBPart",
    "BaseMSBPartList",
]

import abc
import logging
import typing as tp
import struct

from soulstruct.exceptions import InvalidFieldValueError, SoulstructError
from soulstruct.utilities.binary import BinaryStruct, BinaryReader
from soulstruct.utilities.maths import Vector3

from .enums import BaseMSBPartSubtype
from .msb_entry import MSBEntryEntityCoordinates
from .msb_entry_list import BaseMSBEntryList

_LOGGER = logging.getLogger(__name__)


class PartIndicesData(tp.NamedTuple):
    part_type_index: int
    model_indices: dict[str, int]
    local_environment_indices: dict[str, int]
    region_indices: dict[str, int]
    part_indices: dict[str, int]
    local_collision_indices: dict[str, int]


class PartNamesData(tp.NamedTuple):
    model_names: dict[int, str]
    region_names: dict[int, str]
    environment_names: dict[int, str]
    part_names: dict[int, str]
    collision_names: dict[int, str]


class BaseMSBPart(MSBEntryEntityCoordinates, abc.ABC):

    ENTRY_SUBTYPE: BaseMSBPartSubtype = None
    PART_HEADER_STRUCT: BinaryStruct = None
    PART_BASE_DATA_STRUCT: BinaryStruct = None
    PART_TYPE_DATA_STRUCT: BinaryStruct = None
    NAME_ENCODING = ""

    def __init__(self, source=None, **kwargs):
        self._part_type_index = -1
        super().__init__(source=source, **kwargs)

    def unpack_type_data(self, msb_reader: BinaryReader):
        """This unpacks simple attributes by default, but some Parts need to process these values more."""
        self.set(**msb_reader.unpack_struct(self.PART_TYPE_DATA_STRUCT, exclude_asserted=True))

    def pack_type_data(self):
        try:
            return self.PART_TYPE_DATA_STRUCT.pack(self)
        except struct.error:
            raise SoulstructError(f"Could not pack type data of MSB part '{self.name}'. See traceback.")

    def set_indices(self, indices: PartIndicesData):
        self._part_type_index = indices.part_type_index

    def set_names(self, names: PartNamesData):
        pass


# region Part Mix-in Classes
class MSB_BasePartMixin(BaseMSBPart, abc.ABC):
    """Type hinting for class attributes acquired from core `MSBEntry` subclasses."""
    ENTRY_SUBTYPE: BaseMSBPartSubtype
    name: str

    def __init__(self, source=None, **kwargs):
        super().__init__(source, **kwargs)


class MSB_ModelName(MSB_BasePartMixin, abc.ABC):

    model_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._model_index = -1
        super().__init__(source, **kwargs)

    def set_indices(self, indices: PartIndicesData):
        super().set_indices(indices)
        try:
            self._model_index = indices.model_indices[self.model_name] if self.model_name else -1
        except KeyError:
            raise KeyError(f"Invalid model name for {self.ENTRY_SUBTYPE.name} {self.name}: {self.model_name}")

    def set_names(self, names: PartNamesData):
        super().set_names(names)
        if self._model_index != -1:
            try:
                self.model_name = names.model_names[self._model_index]
            except KeyError:
                raise KeyError(f"Invalid model index for {self.ENTRY_SUBTYPE.name} {self.name} {self._model_index}")
        else:
            self.model_name = None


class MSB_DrawGroups(MSB_BasePartMixin, abc.ABC):

    DRAW_GROUP_COUNT: int = None  # must be implemented by concrete class
    draw_groups: set[int]

    def __init__(self, source=None, **kwargs):
        self._draw_groups = set()
        super().__init__(source, **kwargs)

    @property
    def draw_groups(self):
        return self._draw_groups

    @draw_groups.setter
    def draw_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._draw_groups = set()
            return
        try:
            draw_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Draw groups must be a set, sequence, `None`, `'None'`, or `''`. Or use `set` methods like `.add()`."
            )
        for i in draw_groups:
            if not isinstance(i, int) and 0 <= i < self.DRAW_GROUP_COUNT:
                raise InvalidFieldValueError(f"Invalid draw group: {i}. Must be 0 <= i < {self.DRAW_GROUP_COUNT}.")
        self._draw_groups = draw_groups


class MSB_DisplayGroups(MSB_BasePartMixin, abc.ABC):

    DISPLAY_GROUP_COUNT: int = None  # must be implemented by concrete class
    display_groups: set[int]

    def __init__(self, source=None, **kwargs):
        self._display_groups = set()
        super().__init__(source, **kwargs)

    @property
    def display_groups(self):
        return self._display_groups

    @display_groups.setter
    def display_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._display_groups = set()
            return
        try:
            display_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Display groups must be a set, sequence, `None`, `'None'`, or `''`. Or use `set` methods like `.add()`."
            )
        for i in display_groups:
            if not isinstance(i, int) and 0 <= i < self.DISPLAY_GROUP_COUNT:
                raise ValueError(f"Invalid display group: {i}. Must be 0 <= i < {self.DISPLAY_GROUP_COUNT}.")
        self._display_groups = display_groups


class MSB_NavmeshGroups(MSB_BasePartMixin, abc.ABC):

    NAVMESH_GROUP_COUNT: int
    navmesh_groups: set[int]

    def __init__(self, source=None, **kwargs):
        self._navmesh_groups = set()
        super().__init__(source=source, **kwargs)

    @property
    def navmesh_groups(self):
        return self._navmesh_groups

    @navmesh_groups.setter
    def navmesh_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._navmesh_groups = set()
            return
        try:
            navmesh_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Navmesh groups must be a set, sequence, `None`, 'None', or ''. Or use `set` methods like `.add()`."
            )
        for i in navmesh_groups:
            if not isinstance(i, int) and 0 <= i < self.NAVMESH_GROUP_COUNT:
                raise ValueError(f"Invalid navmesh group: {i}. Must be 0 <= i < {self.NAVMESH_GROUP_COUNT}.")
        self._navmesh_groups = navmesh_groups


class MSB_BackreadGroups(MSB_BasePartMixin, abc.ABC):

    BACKREAD_GROUP_COUNT: int
    backread_groups: set[int]

    def __init__(self, source=None, **kwargs):
        self._backread_groups = set()
        super().__init__(source, **kwargs)

    @property
    def backread_groups(self):
        return self._backread_groups

    @backread_groups.setter
    def backread_groups(self, value):
        """Converts value to a `set()` (possibly empty) and validates index range."""
        if value is None or isinstance(value, str) and value in {"None", ""}:
            self._backread_groups = set()
            return
        try:
            backread_groups = set(value)
        except (TypeError, ValueError):
            raise TypeError(
                "Backread groups must be a set, sequence, `None`, 'None', or ''. Or use `set` methods like `.add()`."
            )
        for i in backread_groups:
            if not isinstance(i, int) and 0 <= i < self.BACKREAD_GROUP_COUNT:
                raise ValueError(f"Invalid backread group: {i}. Must be 0 <= i < {self.BACKREAD_GROUP_COUNT}.")
        self._backread_groups = backread_groups


class MSB_DrawParent(MSB_BasePartMixin, abc.ABC):

    draw_parent_name: tp.Optional[str]

    def __init__(self, source=None, **kwargs):
        self._draw_parent_index = -1
        self._draw_parent_name = None
        super().__init__(source, **kwargs)

    @property
    def draw_parent_name(self):
        return self._draw_parent_name

    @draw_parent_name.setter
    def draw_parent_name(self, value: tp.Union[None, str]):
        if isinstance(value, str):
            self._draw_parent_name = value if value else None
        elif value is None:
            self._draw_parent_name = None
        else:
            raise TypeError(f"`draw_parent_name` must be a string or `None`, not {value}.")

    def set_indices(self, indices: PartIndicesData):
        super().set_indices(indices)
        self._draw_parent_index = indices.part_indices[self._draw_parent_name] if self._draw_parent_name else -1

    def set_names(self, names: PartNamesData):
        super().set_names(names)
        self._draw_parent_name = names.part_names[self._draw_parent_index] if self._draw_parent_index != -1 else None


class MSB_Scale(MSB_BasePartMixin, abc.ABC):

    scale: Vector3

    def __init__(self, source=None, **kwargs):
        self._scale = Vector3().ones()
        super().__init__(source, **kwargs)

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = Vector3(value)
# endregion


class BaseMSBPartList(BaseMSBEntryList, abc.ABC):

    @abc.abstractmethod
    def set_indices(
        self, model_indices, local_environment_indices, region_indices, part_indices, local_collision_indices,
    ):
        pass

    @abc.abstractmethod
    def set_names(self, model_names, environment_names, region_names, part_names, collision_names):
        pass

    @abc.abstractmethod
    def get_instance_counts(self):
        pass
