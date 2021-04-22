__all__ = ["PropertyValueTyping", "PropertyType", "FBXProperty"]

import typing as tp
import zlib
from enum import IntEnum

if tp.TYPE_CHECKING:
    from soulstruct.utilities.binary import BinaryReader


PropertyValueTyping = tp.Union[bytes, str, bool, int, float, list[bool, ...], list[int, ...], list[float, ...]]


class PropertyType(IntEnum):

    Bytes = ord("R")  # 82
    String = ord("S")  # 83

    Bool = ord("C")  # 67
    Short = ord("Y")  # 89
    Int = ord("I")  # 73
    Long = ord("L")  # 76
    Single = ord("F")  # 70
    Double = ord("D")  # 68

    # Note that these are all lower-case chrs of the primitive scalars above, EXCEPT for "BoolArray".
    BoolArray = ord("b")  # 98
    ShortArray = ord("y")  # 121
    IntArray = ord("i")  # 105
    LongArray = ord("l")  # 108
    SingleArray = ord("f")  # 102
    DoubleArray = ord("d")  # 100

    def get_fmt(self, array_length: int = None) -> tp.Optional[str]:
        if array_length is not None and "Array" not in self.name:
            raise ValueError(f"Passed `array_length` to `PropertyType.get_fmt()` for non-array property.")
        elif array_length is None and "Array" in self.name:
            raise ValueError(f"Must pass `array_length` to `PropertyType.get_fmt()` for array property.")
        if self in {self.Bool, self.BoolArray}:
            fmt = "?"
        elif self in {self.Short, self.ShortArray}:
            fmt = "h"
        elif self in {self.Int, self.IntArray}:
            fmt = "i"
        elif self in {self.Long, self.LongArray}:
            fmt = "q"
        elif self in {self.Single, self.SingleArray}:
            fmt = "f"
        elif self in {self.Double, self.DoubleArray}:
            fmt = "d"
        else:
            raise TypeError(f"Invalid `PropertyType` for `get_fmt()`: {self.name}")
        if "Array" in self.name:
            return f"<{array_length}{fmt}"
        return f"<{fmt}"

    def get_size(self, array=False) -> int:
        primitive_name = self.name.replace("Array", "") if array else self.name
        if primitive_name == "Bool":
            return 1
        elif primitive_name == "Short":
            return 2
        elif primitive_name in {"Int", "Single"}:
            return 4
        elif primitive_name in {"Long", "Double"}:
            return 8
        raise TypeError(f"Invalid `PropertyType` for `get_size()`: {self.name}")

    def unpack_value(self, reader: BinaryReader) -> PropertyValueTyping:
        if self in {self.Bytes, self.String}:
            raw_data_size = reader.unpack_value("i")
            value = reader.read(raw_data_size)
            if self == PropertyType.String:
                # Assumed encoding (could also be "ascii").
                return value.decode("utf-8")  # str
            return value  # bytes

        if "Array" not in self.name:
            return reader.unpack_value(self.get_fmt())

        array_length, is_compressed, compressed_size = reader.unpack("III")
        if is_compressed:
            decompressed_size = self.get_size(array=True) * array_length
            decompressed = zlib.decompressobj().decompress(reader.read(compressed_size))
            if len(decompressed) != decompressed_size:
                raise ValueError(
                    f"FBX property decompressed data size ({len(decompressed)}) does not match expected size "
                    f"({decompressed_size})"
                )
            array_reader = BinaryReader(decompressed)
        else:
            array_reader = reader
        fmt = self.get_fmt(array_length)
        return list(array_reader.unpack(fmt))


class FBXProperty:
    """FBX property, which simply contains a type enum and a `value` attribute containing its data."""

    _property_type: PropertyType
    _value: tp.Union[bytes, str, bool, int, float]

    def __init__(
        self,
        value: PropertyValueTyping,
        property_type: tp.Union[PropertyType, str] = None,
    ):
        if property_type is None:
            self._property_type = self.detect_property_type(value)  # validates value as well
        else:
            self._property_type = self.parse_property_type(property_type)
            self.validate_value(value, property_type)
        self._value = value

    @property
    def property_type(self):
        return self._property_type

    @property_type.setter
    def property_type(self, property_type: tp.Union[PropertyType, str, None]):
        if property_type is None:
            self._property_type = self.detect_property_type(self._value)
        else:
            self._property_type = self.parse_property_type(property_type)
            self.validate_value(self._value, property_type)

    @property
    def value(self) -> tp.Union[bytes, str, bool, int, float]:
        return self._value

    @value.setter
    def value(self, value):
        self.validate_value(value, self._property_type)
        self._value = value

    @classmethod
    def unpack(cls, reader: BinaryReader, property_type_byte: int = None):
        """Unpack `FBXProperty` from given `reader`.

        If `property_type_byte=None` (default), it will be read from the first byte of `reader` first. Otherwise, that
        byte will be assumed as already read.
        """
        if property_type_byte is None:
            property_type_byte = reader.unpack_value("<B")
        try:
            property_type = PropertyType(property_type_byte)  # type: PropertyType
        except ValueError:
            raise ValueError(
                f"Unsupported property type read: {property_type_byte} ({chr(property_type_byte)})"
            )
        value = property_type.unpack_value(reader)
        return cls(value, property_type)

    @staticmethod
    def parse_property_type(property_type: tp.Union[PropertyType, str]):
        if isinstance(property_type, PropertyType):
            return property_type
        elif isinstance(property_type, str):
            try:
                return getattr(PropertyType, property_type.lower().capitalize())
            except AttributeError:
                raise TypeError(f"Invalid property type name: {repr(property_type)}")
        else:
            raise TypeError(
                f"`property_type` must be a `PropertyType` enum or name string, (or left as `None` to auto-detect), "
                f"not {repr(property_type)}."
            )

    def detect_property_type(self, value: PropertyValueTyping) -> PropertyType:
        if isinstance(value, bytes):
            return PropertyType.Bytes
        elif isinstance(value, str):
            return PropertyType.String
        elif isinstance(value, bool):
            return PropertyType.Bool
        elif isinstance(value, int):
            if -2 ** 15 <= value <= 2 ** 15 - 1:
                return PropertyType.Short
            elif -2 ** 31 <= value <= 2 ** 31 - 1:
                return PropertyType.Int
            return PropertyType.Long
        elif isinstance(value, float):
            return PropertyType.Double
        elif isinstance(value, (tuple, list)):
            # Iterate over every element, expecting only one property type to be found.
            array_types = [self.detect_property_type(v) for v in value]
            # Upgrade all integer types to the largest type present.
            if PropertyType.Long in array_types:
                array_types = [
                    PropertyType.Long if pt in {PropertyType.Short, PropertyType.Int} else pt
                    for pt in array_types
                ]
            elif PropertyType.Int in array_types:
                array_types = [
                    PropertyType.Int if pt == PropertyType.Short else pt
                    for pt in array_types
                ]
            array_types_set = set(array_types)
            if PropertyType.Bytes in array_types_set or PropertyType.String in array_types_set:
                raise TypeError(f"Array cannot contain `bytes` or `str` values.")
            if len(array_types_set) != 1:
                raise TypeError(f"Array with multiple property types is invalid. Types: {array_types_set}")
            return array_types[0]
        raise TypeError(
            f"Invalid property value {value} (type {type(value)}). "
            f"Value type must be bytes, str, bool, int, float, or a tuple/list of bools, ints, or floats."
        )

    def validate_value(self, value: PropertyValueTyping, property_type: PropertyType):
        type_error = TypeError(f"Value {repr(value)} is incompatible with `PropertyType` {property_type.name}.")
        if property_type == PropertyType.Bytes:
            if not isinstance(value, bytes):
                raise type_error
        elif property_type == PropertyType.String:
            if not isinstance(value, str):
                raise type_error
        elif property_type == PropertyType.Bool:
            if not isinstance(value, bool):
                raise type_error
        elif property_type == PropertyType.Short:
            if not (isinstance(value, int) and -2 ** 15 <= value <= 2 ** 15 - 1):
                raise type_error
        elif property_type == PropertyType.Int:
            if not (isinstance(value, int) and -2 ** 31 <= value <= 2 ** 31 - 1):
                raise type_error
        elif property_type == PropertyType.Long:
            if not isinstance(value, int):
                raise type_error
        elif property_type in {PropertyType.Single, PropertyType.Double}:
            if not isinstance(value, float):
                raise type_error
        elif "Array" in property_type.name:
            if not isinstance(value, (tuple, list)):
                raise TypeError(f"List/tuple of values required for `PropertyType` {property_type.name}, not {value}.")
            primitive_type = getattr(PropertyType, property_type.name.replace("Array", ""))
            for v in value:
                try:
                    self.validate_value(v, primitive_type)
                except TypeError:
                    raise TypeError(f"Array value {repr(v)} is incompatible with `PropertyType` {property_type.name}.")
        else:
            raise TypeError(f"Invalid `property_type`: {property_type}")

    def __repr__(self):
        return repr(self.value)
