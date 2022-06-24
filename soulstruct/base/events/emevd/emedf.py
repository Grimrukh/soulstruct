from __future__ import annotations

__all__ = [
    "ArgType",
    "add_common_emedf_info",
    "HIDE",
    "BOOL",
    "INT",
    "FLOAT",
    "MODEL_POINT",
    "BIT_COUNT",
    "SPECIAL_EFFECT",
    "NO_DEFAULT",
]

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
    common_emedf_raw = read_json(common_emedf_path)

    common_emedf = {}
    for cat_dict in common_emedf_raw["main_classes"]:
        category = cat_dict["index"]
        for instr_dict in cat_dict["instrs"]:
            index = instr_dict["index"]
            common_emedf[category, index] = instr_dict

    for (category, index), info in emedf.items():
        try:
            instr = common_emedf[category, index]
        except KeyError:
            if all("internal_type" in arg_dict for arg_dict in info["args"].values()):
                continue  # permitted to be missing from real EMEDF
            raise KeyError(f"Invalid instruction ID for common EMEDF '{common_emedf_path.name}': ({category}, {index})")
        if len(info["args"]) != len(instr["args"]):
            print(category, index, info["alias"], instr["name"])
            raise ValueError(
                f"Instruction ID ({category}, {index}) has {len(instr['args'])} args in common EMEDF but has "
                f"{len(info['args'])} args in Soulstruct."
            )
        for i, arg_name in enumerate(info["args"]):
            if "internal_type" in instr["args"][i]:
                continue  # already specified manually
            instr_type = int(instr["args"][i]["type"])
            try:
                # Original dictionary is copied, as many arguments across instructions refer to common dicts.
                info["args"][arg_name] = info["args"][arg_name].copy() | {"internal_type": ArgType(instr_type)}
            except ValueError:
                raise ValueError(
                    f"Instruction ({category}, {index}) argument '{arg_name}' has unrecognized type in common EMEDF: "
                    f"{instr_type}"
                )


HIDE = {
    "hide_name": True,
}
BOOL = {
    "type": bool,
    "default": None,
}
INT = {
    "type": int,
    "default": None,
}
FLOAT = {
    "type": float,
    "default": None,
}

MODEL_POINT = {
    "type": int,
    "default": -1,
    "internal_default": -1,
}
BIT_COUNT = {
    "type": int,
    "default": None,
    "internal_default": 1,
}
SPECIAL_EFFECT = {
    "type": int,
    "default": None,
    "internal_default": -1,
}


def NO_DEFAULT(enum_cls):
    return {
        "type": enum_cls,
        "default": None
    }
