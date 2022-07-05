from __future__ import annotations

__all__ = [
    "ArgType",
    "add_common_emedf_info",
    "build_emedf_aliases_tests",
    "HIDE_NAME",
    "BOOL",
    "INT",
    "FLOAT",
    "MODEL_POINT",
    "BIT_COUNT",
    "SPECIAL_EFFECT",
    "NO_DEFAULT",
]

import typing as tp
from enum import IntEnum
from pathlib import Path

from soulstruct.utilities.files import read_json
from .enums import BaseNegatableEMEVDEnum


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


def build_emedf_aliases_tests(emedf: dict) -> tuple[dict, dict]:
    # Retrieve instruction information by EVS instruction alias name (or partial name) and build test dictionary.
    emedf_aliases = {v["alias"]: (category, index, v) for (category, index), v in emedf.items()}
    emedf_tests = {}
    for (category, index), v in emedf.items():

        if "partials" in v:
            for partial_name in v["partials"]:
                emedf_aliases[partial_name] = (category, index, v)

            if v["alias"].endswith("IfConditionState") or v["alias"].endswith("IfFinishedConditionState"):
                continue  # condition tests are handled with `Condition` EVS object

            if v["alias"].startswith("If"):
                for partial_name in v["partials"]:
                    emedf_tests.setdefault(partial_name[2:], {})["if"] = partial_name
            elif v["alias"].startswith("SkipLinesIf"):
                for partial_name, partial_kwargs in v["partials"].items():
                    boolean_kwargs = [
                        (kw, kw_v) for kw, kw_v in partial_kwargs.items()
                        if isinstance(kw_v, (bool, BaseNegatableEMEVDEnum))
                    ]
                    if len(boolean_kwargs) == 1:
                        bool_name, bool_value = boolean_kwargs[0]
                        if isinstance(bool_value, BaseNegatableEMEVDEnum):
                            try:
                                negated_value = bool_value.negate()
                            except ValueError:
                                continue
                        else:
                            negated_value = not bool_value
                        negated_kwargs = partial_kwargs.copy() | {bool_name: negated_value}

                        for check_partial_name, check_partial_kwargs in v["partials"].items():
                            if check_partial_kwargs == negated_kwargs:
                                emedf_tests.setdefault(partial_name[11:], {})["skip"] = check_partial_name
            elif v["alias"].startswith("ReturnIf"):
                for partial_name in v["partials"]:
                    if partial_name.startswith("EndIf"):
                        emedf_tests.setdefault(partial_name[5:], {})["end"] = partial_name
                    elif partial_name.startswith("RestartIf"):
                        emedf_tests.setdefault(partial_name[9:], {})["restart"] = partial_name
            elif v["alias"].startswith("GotoIf"):
                for partial_name in v["partials"]:
                    emedf_tests.setdefault(partial_name[6:], {})["goto"] = partial_name

    return emedf_aliases, emedf_tests


HIDE_NAME = {
    "hide_name": True,
}
BOOL = {  # boolean event arguments will be typed as integers
    "type": tp.Union[bool, int],
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
