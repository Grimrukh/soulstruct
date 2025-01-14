from __future__ import annotations

__all__ = [
    "EMEDF_TYPING",
    "ArgType",
    "add_common_emedf_info",
    "build_emedf_aliases_tests",
    "get_coord_entity_type",
    "HIDE_NAME",
    "BOOL",
    "INT",
    "FLOAT",
    "DUMMY_ID",
    "BIT_COUNT",
    "SPECIAL_EFFECT",
    "NO_DEFAULT",
]

import typing as tp
from collections import defaultdict
from enum import IntEnum
from pathlib import Path

from soulstruct.utilities.files import read_json
from ..enums import BaseNegatableEMEVDEnum
from .utils import get_coord_entity_type


# EMEDF is a dictionary mapping instruction `(category, index)` to a dictionary of information (strings and types).
EMEDF_TYPING = tp.Dict[tuple[int, int], dict[str, tp.Any]]


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


def add_common_emedf_info(emedf: EMEDF_TYPING, common_emedf_path: Path | str):
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


def build_emedf_aliases_tests(emedf: EMEDF_TYPING) -> tuple[dict, dict, dict]:
    """Retrieve instruction information by EVS instruction alias name (or partial name) and build test dictionary.

    Returns three dictionaries:
        - `emedf_aliases`: maps alias names to instruction information dictionaries.
        - `emedf_tests`: maps test names to instructions for these keys, when they exist:
            - "if": If{Test} instruction.
            - "skip_if": SkipLinesIf{Test} instruction.
            - "skip_if_not": SkipLinesIf{NotTest} instruction with negated test (e.g. 'EnabledFlag' -> 'DisabledFlag').
            - "end_if": EndIf{Test} instruction.
            - "restart_if": RestartIf{Test} instruction.
        - `emedf_comparison_tests`: maps comparison test names to dictionaries with "test_name" and "return_type" keys.

    NOTE: In practice, the values of the test instructions are predictable from their keys (e.g. test `FlagEnabled` key
    "skip_if" will be `SkipLinesIfFlagEnabled`). But we may as well assign the names rather than just existence bools.
    """
    emedf_aliases = {v["alias"]: (category, index, v) for (category, index), v in emedf.items()}
    emedf_tests = defaultdict(dict)
    emedf_comparison_tests = {}
    for (category, index), v in emedf.items():

        alias = v["alias"]
        partials = v.get("partials", {})
        for partial_name in partials:
            emedf_aliases[partial_name] = (category, index, v)

        if alias.endswith("IfConditionState") or alias.endswith("IfLastConditionResultState"):
            continue  # condition tests are handled with `Condition` EVS object and `ConditionGroup` enum

        if alias.startswith("If") and not alias.startswith("If_Unknown"):

            # TODO: Need to detect negated versions and add to 'if_not', 'skip_not', 'end_not', 'restart_not'...

            test_name = alias.removeprefix("If")
            emedf_tests[test_name]["if"] = alias

            for partial_name in partials:
                test_name = partial_name.removeprefix("If")
                emedf_tests[test_name]["if"] = partial_name

            # Comparison tests are also added to a third specific dictionary.
            if alias.endswith("Comparison") and "comparison_type" in v["args"] and "value" in v["args"]:
                comparator_test_name = alias.removeprefix("If").removesuffix("Comparison")  # e.g., `HealthRatio`
                emedf_comparison_tests[comparator_test_name] = {
                    "test_name": alias.removeprefix("If"),  # test defined above, e.g., `HealthComparison()`.
                    "return_type": v["args"]["value"]["type"],
                }

        elif alias.startswith("SkipLinesIf"):

            for partial_name, partial_kwargs in partials.items():

                test_name = partial_name.removeprefix("SkipLinesIf")

                # Add "skip_if" test:
                emedf_tests[test_name]["skip_if"] = partial_name

                # Search for and add "skip_if_not" test, which in practice is more useful than "skip_if" as it
                # corresponds to `if {test}:` in higher-level code.

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
                            continue  # not all enum values necessarily have negations
                    else:
                        negated_value = not bool_value
                    negated_kwargs = partial_kwargs.copy() | {bool_name: negated_value}

                    for check_partial_name, check_partial_kwargs in partials.items():
                        if check_partial_kwargs == negated_kwargs:
                            emedf_tests[test_name]["skip_if_not"] = check_partial_name
                            break

        elif alias.startswith("ReturnIf"):
            # Base "ReturnIf" instructions do not need to be tests here. They always have partials.
            for partial_name in partials:
                if partial_name.startswith("EndIf"):
                    test_name = partial_name.removeprefix("EndIf")
                    emedf_tests[test_name]["end_if"] = partial_name
                elif partial_name.startswith("RestartIf"):
                    test_name = partial_name.removeprefix("RestartIf")
                    emedf_tests[test_name]["restart_if"] = partial_name

        elif alias.startswith("GotoIf"):
            # TODO: Should probably implement tests for base instructions here.
            for partial_name in partials:
                test_name = partial_name.removeprefix("GotoIf")
                emedf_tests[test_name]["goto"] = partial_name

    tests_to_remove = [name for name, info in emedf_tests.items() if "if" not in info]
    for test_name in tests_to_remove:
        emedf_tests.pop(test_name)

    return emedf_aliases, emedf_tests, emedf_comparison_tests


HIDE_NAME = {
    "hide_name": True,
}

# Shortcuts for Python types with no default.
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

DUMMY_ID = {
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
