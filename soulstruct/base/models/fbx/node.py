from __future__ import annotations

__all__ = ["FBXNode32", "FBXNode64"]

import abc
import typing as tp
from collections import deque

from soulstruct.base.models.color import ColorRGB
from soulstruct.utilities.binary import BinaryStruct, BinaryObject, BinaryReader
from soulstruct.utilities.maths import Vector3

from .field_types import *
from .property import PropertyValueTyping, FBXProperty

try:
    import colorama
except ImportError:
    colorama = None
    RED = GREEN = BLUE = YELLOW = RESET = ""
else:
    colorama.init()
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    BLUE = colorama.Fore.BLUE
    YELLOW = colorama.Fore.YELLOW
    RESET = colorama.Fore.RESET


class FBXNodeBase(BinaryObject, abc.ABC):

    ARRAY_MAX_REPR = 5
    PROP_MAX_REPR = 10
    INDENT_PER_DEPTH = 4

    name: str
    _properties: list[FBXProperty]
    _field: tp.Optional[FBXPropertyField]
    children: list[FBXNodeBase]

    # Size is evaluated on unpack, so offsets can be tracked, and updated before pack. May be incorrect before pack.
    size: int
    depth: int  # for repr

    def unpack(self, reader: BinaryReader, start_offset: int, depth=0):
        data = reader.unpack_struct(self.STRUCT)
        name_length = data.pop("__name_length")
        self.name = reader.unpack_string(length=name_length, encoding="ascii")

        self.size = self.STRUCT.size + name_length
        self.depth = depth

        # TODO: Use `_properties` and `field` properties, which inspect the node name, etc.
        self._properties = [FBXProperty.unpack(reader) for _ in range(data.pop("__property_count"))]

        self.size += data.pop("__property_list_size")

        self.children = []
        end_offset = data.pop("__end_offset")
        while start_offset + self.size < end_offset:
            child = self.__class__(reader, start_offset=start_offset + self.size, depth=self.depth + 1)
            self.size += child.size
            if start_offset + self.size == end_offset:
                break  # empty node is not kept
            self.children.append(child)

        if self.name == "P":
            if self.children:
                raise ValueError("`FBXNode` named 'P' should not have any children.")
            name, *args = [p.value for p in self._properties]
            self._field = FBXPropertyField(name, *args)
        else:
            self._field = None

    @property
    def is_empty(self):
        """Each node finishes with an empty child node."""
        return not (self.name or self.properties or self.children)

    @property
    def properties(self) -> list[FBXProperty]:
        return self._properties

    @property
    def field(self):
        """Nodes named "P" use a list of properties to define a field and value, and have no children. Those properties
        are loaded into a `PropertyField` instance here if applicable.

        Otherwise, this will raise an `AttributeError`.
        """
        if self._field is None:
            raise AttributeError(f"FBXNode {repr(self.name)} is not a `PropertyField` node.")
        return self._field

    # TODO: Allow user to set `field`.

    def __getitem__(self, child_node_name: str):
        if not self.children:
            raise KeyError(f"FBX node {self.name} has no child nodes (was looking for {child_node_name}).")
        hits = [n for n in self.children if n.name == child_node_name]
        if not hits:
            raise KeyError(f"FBX node {self.name} has no child nodes named {child_node_name}.")
        elif len(hits) > 1:
            raise KeyError(f"FBX node {self.name} has multiple child nodes named {child_node_name}.")
        child = hits[0]
        if not child.children:
            # Return values of basic property node, unpacking single values.
            if len(child.properties) == 1:
                return child.properties[0].value
            else:
                return [p.value for p in child.properties]
        else:
            return child

    def get_extra_field(self, field_name: str):
        try:
            prop_node = self["Properties70"]
        except KeyError:
            raise KeyError(f"FBX node {self.name} has no 'Properties70' child (where extra fields are stored).")
        try:
            prop = next(n for n in prop_node.children if n.field.name == field_name)
        except StopIteration:
            raise KeyError(f"FBX node {self.name} has no extra field named {field_name}.")
        return prop.field.value

    def to_string(self) -> str:
        ind = " " * (self.INDENT_PER_DEPTH * self.depth)
        if self._field is not None:
            return self._field.to_string(indent=ind)
        prop_reprs = []
        if len(self._properties) > self.PROP_MAX_REPR:
            prop_reprs.append(f"{RED}<{len(self._properties)}> Properties{RESET}")
        else:
            for p in self._properties:
                if "Array" in p.property_type.name and len(p.value) > self.ARRAY_MAX_REPR:
                    primitive_type_name = p.property_type.name.replace("Array", "")
                    prop_reprs.append(f"{RED}<{len(p.value)} {primitive_type_name}>{RESET}")
                else:
                    prop_reprs.append(f"{BLUE}{repr(p)}{RESET}")
        lines = [f"{ind}{YELLOW}{self.name}:{RESET} {', '.join(prop_reprs)}"]
        for child in self.children:
            lines.append(child.to_string())
        return "\n".join(lines)

    def __repr__(self):
        return f"FBXNode(name={self.name}, properties={len(self._properties)}, children={len(self.children)})"


class FBXNode32(FBXNodeBase):
    STRUCT = BinaryStruct(
        ("__end_offset", "I"),
        ("__property_count", "I"),
        ("__property_list_size", "I"),
        ("__name_length", "B"),
    )

    children: list[FBXNode32]


class FBXNode64(FBXNodeBase):
    STRUCT = BinaryStruct(
        ("__end_offset", "q"),
        ("__property_count", "q"),
        ("__property_list_size", "q"),
        ("__name_length", "B"),
    )

    children: list[FBXNode64]


class FBXPropertyField:
    """Converts a list of properties in a "P" node into a single field/value object.

    Child classes convert specific known field types. This generic parent class handles any unknown fields.
    """
    class FieldParseError(Exception):
        """Error encountered while parsing field."""

    name: str
    value: tp.Any
    unknowns: list[PropertyValueTyping]

    def __init__(self, name: str, *args):
        self.name = name

        queue = deque(args)

        first_arg = queue[0].replace(" ", "_")

        if queue and hasattr(self, f"parse_{first_arg}"):
            try:
                self.value = getattr(self, f"parse_{first_arg}")(queue)
            except (self.FieldParseError, ValueError):
                raise ValueError(f"Error encountered while parsing field args: {args}")
        else:
            self.value = None

        # TODO: Start identifying specific data types, and their property list layouts, and remove them from `args`.

        self.unknowns = list(queue)

    def parse_KString(self, queue: deque) -> str:
        self._assert(queue, "KString")
        special_type = queue.popleft()  # e.g. 'Url'
        self._assert(queue, "")
        s = queue.popleft()
        if special_type:
            return f"{special_type}({repr(s)})"
        return repr(s)

    def parse_DateTime(self, queue: deque) -> str:
        self._assert(queue, "DateTime")
        self._assert(queue, "")
        self._assert(queue, "")
        dt = queue.popleft()
        return DateTime(dt)

    def parse_bool(self, queue: deque) -> bool:
        self._assert(queue, "bool")
        self._assert(queue, "")
        self._assert(queue, "")
        b = bool(queue.popleft())
        return b

    def parse_enum(self, queue: deque) -> str:
        """I don't know what enum these are part of, but presumably it's tied to the field name."""
        self._assert(queue, "enum")
        self._assert(queue, "")
        self._assert(queue, "")
        e = queue.popleft()
        return f"Enum({e})"

    def parse_int(self, queue: deque) -> int:
        self._assert(queue, "int")
        n = self.parse_Integer(queue)
        return n

    def parse_Integer(self, queue: deque) -> int:
        self._assert(queue, "Integer")
        self._assert(queue, "")
        n = queue.popleft()
        return n

    def parse_Compound(self, queue: deque) -> str:
        # TODO: No non-empty values seen yet.
        self._assert(queue, "Compound")
        self._assert(queue, "")
        self._assert(queue, "")
        return "Compound()"

    def parse_object(self, queue: deque) -> str:
        # TODO: No non-empty values seen yet.
        self._assert(queue, "object")
        self._assert(queue, "")
        self._assert(queue, "")
        return "object()"

    def parse_Visibility(self, queue: deque) -> Visibility:
        self._assert(queue, "Visibility")
        self._assert(queue, "")
        self._assert(queue, "A")
        n = queue.popleft()
        return Visibility(n)

    def parse_Visibility_Inheritance(self, queue: deque) -> VisibilityInheritance:
        self._assert(queue, "Visibility Inheritance")
        self._assert(queue, "")
        self._assert(queue, "")
        b = queue.popleft()  # TODO: Probably a bool.
        return VisibilityInheritance(b)

    def parse_FieldOfView(self, queue: deque) -> FieldOfView:
        self._assert(queue, "FieldOfView")
        self._assert(queue, "")
        self._assert(queue, "A")
        n = queue.popleft()
        return FieldOfView(n)

    def parse_FieldOfViewX(self, queue: deque) -> FieldOfViewX:
        self._assert(queue, "FieldOfViewX")
        self._assert(queue, "")
        self._assert(queue, "A")
        n = queue.popleft()
        return FieldOfViewX(n)

    def parse_FieldOfViewY(self, queue: deque) -> FieldOfViewY:
        self._assert(queue, "FieldOfViewY")
        self._assert(queue, "")
        self._assert(queue, "A")
        n = queue.popleft()
        return FieldOfViewY(n)

    def parse_OpticalCenterX(self, queue: deque) -> OpticalCenterX:
        self._assert(queue, "OpticalCenterX")
        self._assert(queue, "")
        self._assert(queue, "A")
        n = queue.popleft()
        return OpticalCenterX(n)

    def parse_OpticalCenterY(self, queue: deque) -> OpticalCenterY:
        self._assert(queue, "OpticalCenterY")
        self._assert(queue, "")
        self._assert(queue, "A")
        n = queue.popleft()
        return OpticalCenterY(n)

    def parse_Lcl_Translation(self, queue: deque) -> LclTranslation:
        self._assert(queue, "Lcl Translation")
        self._assert(queue, "")
        self._assert(queue, "A")
        x = queue.popleft()
        y = queue.popleft()
        z = queue.popleft()
        return LclTranslation(x, y, z)

    def parse_Lcl_Rotation(self, queue: deque) -> LclRotation:
        self._assert(queue, "Lcl Rotation")
        self._assert(queue, "")
        self._assert(queue, "A")
        x = queue.popleft()
        y = queue.popleft()
        z = queue.popleft()
        return LclRotation(x, y, z)

    def parse_Lcl_Scaling(self, queue: deque) -> LclScaling:
        self._assert(queue, "Lcl Scaling")
        self._assert(queue, "")
        self._assert(queue, "A")
        x = queue.popleft()
        y = queue.popleft()
        z = queue.popleft()
        return LclScaling(x, y, z)

    def parse_Vector3D(self, queue: deque) -> Vector3:
        self._assert(queue, "Vector3D")
        v = self.parse_Vector(queue)
        return v  # TODO: How does this differ from a `Vector`?

    def parse_Vector(self, queue: deque) -> Vector3:
        self._assert(queue, "Vector")
        self._assert(queue, "")
        self._assert(queue, "A", optional=True)
        x = queue.popleft()
        y = queue.popleft()
        z = queue.popleft()
        return Vector3(x, y, z)

    def parse_Color(self, queue: deque) -> ColorRGB:
        """TODO: Channel order is very likely RGB."""
        self._assert(queue, "Color")
        self._assert(queue, "", optional=True)
        self._assert(queue, "A", optional=True)
        red = queue.popleft()
        green = queue.popleft()
        blue = queue.popleft()
        return ColorRGB(red, green, blue)

    def parse_ColorRGB(self, queue: deque) -> ColorRGB:
        self._assert(queue, "ColorRGB")
        color = self.parse_Color(queue)
        return color

    def parse_Number(self, queue: deque) -> tp.Union[int, float]:
        """TODO: This could actually mean 'single', as it always seems to return a float and is used by 'double'."""
        self._assert(queue, "Number")
        self._assert(queue, "", "H", optional=True)
        self._assert(queue, "A", optional=True)
        n = queue.popleft()
        return n

    def parse_Roll(self, queue: deque) -> tp.Union[int, float]:
        self._assert(queue, "Roll")
        self._assert(queue, "")
        self._assert(queue, "A")
        n = queue.popleft()
        return n

    def parse_double(self, queue: deque) -> float:
        self._assert(queue, "double")
        n = self.parse_Number(queue)
        return float(n)

    def parse_KTime(self, queue: deque) -> KTime:
        self._assert(queue, "KTime")
        t = self.parse_Time(queue)
        return KTime(t)

    def parse_Time(self, queue: deque) -> Time:
        self._assert(queue, "Time")
        self._assert(queue, "")
        t = queue.popleft()
        return Time(t)

    def _assert(self, queue: deque, *values, optional=False):
        if not queue:
            raise self.FieldParseError(f"Ran out of args unexpectedly.")
        if optional:
            if queue[0] in values:
                return queue.popleft()
            return None
        if (v := queue.popleft()) not in values:
            raise self.FieldParseError(f"Expected one of values {repr(values)} in field queue, but found {repr(v)}.")
        return v

    def to_string(self, indent=""):
        if self.value is not None:
            return f"{indent}{GREEN}{self.name}: {BLUE}{self.value}{RESET}"
        return f"{indent}{GREEN}{self.name}: {RED}UNKNOWN{self.unknowns}{RESET}"
