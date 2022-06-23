from __future__ import annotations

import abc
import io
import logging
import re
import typing as tp
from copy import deepcopy
from enum import IntEnum

from soulstruct.base.game_types import GameObjectSequence, Map
from soulstruct.utilities.binary import BinaryReader
from soulstruct.utilities.maths import Vector, Vector3, Matrix3, resolve_rotation

from .utils import MapFieldInfo

if tp.TYPE_CHECKING:
    from .enums import BaseMSBSubtype

_LOGGER = logging.getLogger(__name__)

_DUPLICATE_TAG_MATCH = re.compile(r"(.*)<(\d+)>$")


class MSBEntry(abc.ABC):

    ENTRY_SUBTYPE = None  # type: BaseMSBSubtype
    FIELD_INFO = {}  # type: dict[str, MapFieldInfo]
    FIELD_ORDER = ()  # If given, fields will be displayed in this order. Otherwise uses order of `FIELD_INFO` keys.
    REFERENCE_FIELDS = {}  # type: dict[str, list[str, ...]]  # maps reference entry types to field names that use them

    name: str
    description: str

    def __init__(self, source=None, **kwargs):
        """Base class for entries of any type and subtype that appear in an `MSB` (under one of the four entry lists).

        If `source` is given, it must be binary data (`bytes` or a byte buffer). You are unlikely to ever do this
        yourself; it is typically only done when a complete `MSB` is unpacked. No keyword arguments may be given in this
        case other than `description`, which will override an unpacked `description` for games that have that field.

        If `source` is not given, any keyword arguments may be given that are valid attributes for the instantiated
        subclass. In this case, `name` is compulsory; all other unspecified values will be set to their defaults.
        """
        self.name = ""
        self.description = ""  # supported by Soulstruct even when game lacks it

        if isinstance(source, (bytes, io.BufferedIOBase)):
            source = BinaryReader(source)
        if isinstance(source, BinaryReader):
            description = kwargs.pop("description", None)
            if kwargs:
                raise ValueError(
                    "Cannot instantiate MSB entry using `kwargs` (except `description`) if binary `source` is given."
                )
            self.set_defaults()
            self.unpack(source)
            if self.description and description is not None:
                _LOGGER.warning(f"`description` arg will override unpacked description for MSB entry '{self.name}'.")
                self.description = description
        elif source is None:
            try:
                self.name = kwargs.pop("name")
            except KeyError:
                raise ValueError(f"`name` must be given to `{self.__class__.__name__}` if no binary `source` is given.")
            self.description = kwargs.pop("description", "")
            default_values = self.get_default_values()
            for field_name in self.FIELD_INFO:
                try:
                    value = kwargs.pop(field_name)
                except KeyError:
                    try:
                        value = default_values[field_name].copy()  # mutable default (e.g. `list`, `set`, `Vector3`)
                    except AttributeError:
                        value = default_values[field_name]  # immutable default (e.g. `int`, `float`, `str`, `tuple`)
                if isinstance(value, IntEnum):
                    value = value.value
                setattr(self, field_name, value)
            if kwargs:
                raise ValueError(f"Invalid arguments for MSB entry class `{self.__class__.__name__}`: {tuple(kwargs)}")
        else:
            raise TypeError(f"`{self.__class__.__name__}` source must be a buffer, `bytes`, or `None` (default).")

    @abc.abstractmethod
    def pack(self):
        """Pack to bytes."""

    @abc.abstractmethod
    def unpack(self, msb_reader: BinaryReader):
        """Unpack from open `MSB` buffer."""

    def get_name_to_pack(self):
        """Remove duplicate tags '<i>' from end of name."""
        return _DUPLICATE_TAG_MATCH.sub("", self.name)

    def __getitem__(self, field_name):
        if field_name in self.FIELD_INFO:
            return getattr(self, field_name)
        raise KeyError(f"Field {field_name} does not exist in MSB entry type {self.__class__.__name__}.")

    def __setitem__(self, field_name, value):
        """Alias for setting the given attribute.

        `field_name` must be 'name', 'description', or a key in the `FIELD_INFO` dictionary for this class.
        """
        if isinstance(value, IntEnum):
            value = value.value
        if field_name.startswith("_") and hasattr(self, field_name):
            setattr(self, field_name, value)
        elif field_name in {"name", "description"} or field_name in self.FIELD_INFO:
            setattr(self, field_name, value)
        else:
            if field_name not in self.FIELD_INFO:
                raise KeyError(f"Field {repr(field_name)} does not exist in MSB entry type {self.__class__.__name__}.")
            setattr(self, field_name, value)

    def set(self, **kwargs):
        """Update any attribute fields with keyword arguments.

        Argument keys starting with double underscore are ignored so that `BinaryStruct`-produced dictionaries can
        easily be passed in. See `__setitem__()` for more.
        """
        for field_name, value in kwargs.items():
            if not field_name.startswith("__"):
                self[field_name] = value

    def set_defaults(self):
        for field_name, field_info in self.FIELD_INFO.items():
            try:
                setattr(self, field_name, field_info.default)
            except AttributeError as ex:
                raise AttributeError(
                    f"Could not set attribute '{field_name}' in class `{self.__class__.__name__}`.\n"
                    f"Error: {ex}")

    def copy(self):
        return deepcopy(self)

    @property
    def field_names(self):
        if self.FIELD_ORDER:
            return self.FIELD_ORDER
        return tuple(self.FIELD_INFO.keys())

    @property
    def all_field_names(self):
        """Includes hidden field names absent from `FIELD_ORDER`, which appear after all non-hidden fields."""
        if not self.FIELD_ORDER:
            return self.field_names  # no hidden fields or desired display order
        field_names = self.field_names
        hidden_fields = [field for field in self.FIELD_INFO.keys() if field not in field_names]
        return self.FIELD_ORDER + tuple(hidden_fields)

    def rename_names(self, old_name: str, new_name: str, entry_types=()):
        """Check any `REFERENCE_FIELDS` used by this class and rename them from `old_name` to `new_name`.

        If `entry_types` is given, only references to one of those given types will be changed. (References that can be
        multiple types only need to match one given type.)

        `GameObjectSequence` types are checked properly as well.
        """

        for reference_type, fields in self.REFERENCE_FIELDS.items():
            if not entry_types or reference_type in entry_types:
                for field_name in fields:
                    field_info = self.FIELD_INFO[field_name]
                    if issubclass(field_info.display_type, GameObjectSequence):
                        setattr(self, field_name, [
                            new_name if name == old_name else name for name in getattr(self, field_name)
                        ])
                    else:
                        if getattr(self, field_name) == old_name:
                            setattr(self, field_name, new_name)

    def to_dict(self, ignore_defaults=True) -> dict[str, tp.Any]:
        default_values = self.get_default_values()
        data = {"name": self.name}
        for name in self.all_field_names:
            value = getattr(self, name)
            if ignore_defaults and value == default_values[name]:
                continue  # don't add default values to dictionary
            if isinstance(value, Vector):
                data[name] = list(value)
            elif isinstance(value, Map):
                data[name] = str(value)
            elif isinstance(value, set):
                data[name] = sorted(value)
            else:
                data[name] = value
        return data

    def get_default_values(self):
        return {field_name: field_info.default for field_name, field_info in self.FIELD_INFO.items()}

    def __repr__(self):
        data = self.to_dict(ignore_defaults=True)
        fields = "\n    ".join(f"{k}={repr(v)}," for k, v in data.items())
        return f"{self.__class__.__name__}(\n    {fields}\n)"


class MSBEntryEntity(MSBEntry, abc.ABC):
    """Subclass of MSBEntry with 'entity_id' field (everything except Models). Useful for type checking."""

    FIELD_INFO = MSBEntry.FIELD_INFO | {
        "entity_id": MapFieldInfo(
            "Entity ID",
            int,
            -1,
            "Entity ID used to refer to this entry in other game files.",
        ),
    }

    entity_id: int

    def __init__(self, source=None, entity_enum: IntEnum = None, **kwargs):
        """Accepts `entity_enum` kwargs to pull both `name` and `entity_id` (value) from."""
        if entity_enum is not None:
            self._parse_entity_enum(entity_enum, kwargs)
        super().__init__(source, **kwargs)

    def set(self, entity_enum: IntEnum = None, **kwargs):
        """Update any attribute fields with keyword arguments.

        Argument keys starting with double underscore are ignored so that `BinaryStruct`-produced dictionaries can
        easily be passed in. See `__setitem__()` for more.
        """
        if entity_enum is not None:
            self._parse_entity_enum(entity_enum, kwargs)
        for field_name, value in kwargs.items():
            if not field_name.startswith("__"):
                self[field_name] = value

    @classmethod
    def _parse_entity_enum(cls, entity_enum: IntEnum, kwargs: dict[str, tp.Any]):
        if "name" in kwargs or "entity_id" in kwargs:
            raise ValueError(
                f"Cannot initialize or set `{cls.__name__}` with both `entity_enum` and `name`/`entity_id`.")
        if not isinstance(entity_enum, IntEnum):
            raise TypeError(f"`entity_enum` must be an `IntEnum` subclass, not `{type(entity_enum)}`.")
        kwargs["name"] = entity_enum.name
        kwargs["entity_id"] = entity_enum.value


class MSBEntryEntityCoordinates(MSBEntryEntity, abc.ABC):
    """Subclass of MSBEntryEntity with `translate` and `rotate` fields, and `rotate_in_world` method.

    Inherited by both `MSBPart` and `MSBRegion`).
    """

    FIELD_INFO = MSBEntryEntity.FIELD_INFO | {
        "translate": MapFieldInfo(
            "Translate",
            Vector3,
            Vector3.zero(),
            "3D coordinates of the part's position. Note that the anchor of the part is usually at its base.",
        ),
        "rotate": MapFieldInfo(
            "Rotate",
            Vector3,
            Vector3.zero(),
            "Euler angles for part rotation around its local X, Y, and Z axes.",
        ),
    }

    translate: Vector3
    rotate: Vector3

    def __init__(self, source=None, **kwargs):
        self._translate = Vector3.zero()
        self._rotate = Vector3.zero()
        super().__init__(source=source, **kwargs)

    def apply_rotation(
        self, rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float], pivot_point=(0, 0, 0), radians=False,
    ):
        """Modify entity `translate` and `rotate` by rotating entity around some `pivot_point` in world coordinates.

        Default `pivot_point` is the world origin (0, 0, 0). Default rotation units are degrees.
        """
        rotation = resolve_rotation(rotation, radians)
        pivot_point = Vector3(pivot_point)
        self._rotate = (rotation @ Matrix3.from_euler_angles(self.rotate)).to_euler_angles()
        self._translate = (rotation @ (self.translate - pivot_point)) + pivot_point

    @property
    def translate(self):
        return self._translate

    @translate.setter
    def translate(self, value):
        self._translate = Vector3(value)

    @property
    def rotate(self):
        return self._rotate

    @rotate.setter
    def rotate(self, value):
        if isinstance(value, (int, float)):
            self._rotate = Vector3(0, value, 0)
        else:
            self._rotate = Vector3(value)
