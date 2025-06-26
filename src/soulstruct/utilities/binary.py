"""Wrapper for my library `constrata` that adds some metadata factories for Soulstruct types."""

__all__ = [
    "BinaryStruct",
    "ByteOrder",
    "BinaryFieldTypeError",
    "BinaryFieldValueError",
    "BinaryReader",
    "BinaryWriter",

    "Binary",
    "binary",
    "BinaryString",
    "binary_string",
    "BinaryArray",
    "binary_array",
    "BinaryPad",
    "binary_pad",

    "byte",
    "uint8",
    "sbyte",
    "int8",
    "ushort",
    "uint16",
    "short",
    "int16",
    "uint",
    "uint32",
    "int32",
    "ulong",
    "uint64",
    "long",
    "int64",
    "single",
    "float32",
    "double",
    "float64",
    "varint",
    "varuint",
    "RESERVED",
]

from constrata import *
from constrata.metadata import BinaryArrayMetadata

if not BinaryStruct.METADATA_FACTORIES:
    from soulstruct.utilities.maths import Vector2, Vector3, Vector4

    # `Vector.__iter__` allows automatic pack support.
    BinaryStruct.METADATA_FACTORIES = {
        "Vector2": lambda: BinaryArrayMetadata(2, "2f", unpack_func=Vector2),
        "Vector3": lambda: BinaryArrayMetadata(3, "3f", unpack_func=Vector3),
        "Vector4": lambda: BinaryArrayMetadata(4, "4f", unpack_func=Vector4),
    }
