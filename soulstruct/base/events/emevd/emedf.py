from __future__ import annotations

__all__ = ["ArgType", "add_common_emedf_info"]

from enum import IntEnum
from pathlib import Path

from soulstruct.utilities.files import read_json


class ArgType(IntEnum):
    u8 = 0
    u16 = 1
    u32 = 2
    s8 = 3
    s16 = 4
    s32 = 5
    f32 = 6
    fixstr = 8  # 32-bit index of an EMEVD string

    def get_size(self):
        if self in {ArgType.u8, ArgType.s8}:
            return 1
        elif self in {ArgType.u16, ArgType.s16}:
            return 2
        elif self in {ArgType.u32, ArgType.s32, ArgType.f32, ArgType.fixstr}:
            return 4
        else:
            raise ValueError(f"Invalid `ArgType`: {self}")

    def get_fmt(self):
        if self == ArgType.u8:
            return "B"
        elif self == ArgType.u16:
            return "H"
        elif self == ArgType.u32:
            return "I"
        elif self == ArgType.s8:
            return "b"
        elif self == ArgType.s16:
            return "h"
        elif self == ArgType.s32:
            return "i"
        elif self == ArgType.f32:
            return "f"
        elif self == ArgType.fixstr:
            return "s"  # 32-bit index of an EMEVD string
        else:
            raise ValueError(f"Invalid `ArgType`: {self}")

    def get_type_min_max(self):
        """Get bit-limited minimum and maximum of each type."""
        if self == ArgType.u8:
            return 0, 255
        elif self == ArgType.u16:
            return 0, 65535
        elif self == ArgType.u32 or self == ArgType.fixstr:
            return 0, 4294967295
        elif self == ArgType.s8:
            return -128, 127
        elif self == ArgType.s16:
            return -32768, 32767
        elif self == ArgType.s32:
            return -2147483648, 2147483647
        elif self == ArgType.f32:
            return -float("inf"), float("inf")
        else:
            raise ValueError(f"Invalid `ArgType`: {self}")

    @classmethod
    def from_fmt(cls, fmt: str):
        if fmt == "B":
            return ArgType.u8
        elif fmt == "H":
            return ArgType.u16
        elif fmt == "I":
            return ArgType.u32
        elif fmt == "b":
            return ArgType.s8
        elif fmt == "h":
            return ArgType.s16
        elif fmt == "i":
            return ArgType.s32
        elif fmt == "f":
            return ArgType.f32
        elif fmt == "s":
            return ArgType.fixstr
        else:
            raise ValueError(f"Invalid `ArgType` fmt: {fmt}")


def add_common_emedf_info(emedf: dict, common_emedf_path: Path | str):
    """Insert information from EMEDF JSON into dictionary.

    Currently, just adds internal argument types.
    """
    common_emedf_path = Path(common_emedf_path)
    common_emedf = read_json(common_emedf_path)
    for (category, index), info in emedf.items():
        try:
            instr = common_emedf["main_classes"][category]["instrs"][index]
        except KeyError:
            raise KeyError(f"Invalid instruction ID for common EMEDF '{common_emedf_path.name}': ({category}, {index})")
        if len(info["args"]) != len(instr["args"]):
            raise ValueError(
                f"Instruction ID ({category}, {index}) has {len(instr['args'])} in common EMEDF but has "
                f"{len(info['args'])} in Soulstruct."
            )
        for i, (arg_name, arg_info) in enumerate(info["args"].items()):
            instr_type = int(instr["args"][i]["type"])
            try:
                arg_info["internal_type"] = ArgType(instr_type)
            except ValueError:
                raise ValueError(
                    f"Instruction ({category}, {index}) argument '{arg_name}' has unrecognized type in common EMEDF: "
                    f"{instr_type}"
                )
