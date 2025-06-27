"""Convert HPR's EMEDF text format to JSON format."""

import re
from pathlib import Path

from soulstruct.utilities.files import SOULSTRUCT_PATH, write_json


category_re = re.compile(r"^(\d+) - (.*)$")
instr_re = re.compile(r"^ \[(\d+)] - (.*)$")
arg_re = re.compile(r"^ {6}(\w) {2}(.*?) \[([-\d.]+):([-\d.]+):([-\d.]+)] \(([-\d.]+)\)$")
arg_enum_re = re.compile(r"^ {6}(\w) {2}(.*?) \[ENUM: (.*)]$")


arg_types = "BHIbhifs"


def int_or_float(string):
    if "." in string:
        return float(string)
    return int(string)


def emedf_txt_to_json(txt_path: Path | str, json_path: Path | str):

    emedf_json = {
        "unknown": 0,
        "main_classes": [],
    }

    category = {}
    instruction = {}

    with Path(txt_path).open("r") as f:
        for line in f.readlines():
            line = line.strip("\n")
            if line in {"Extra Classes:", "Enums:"}:
                # Main classes are done.
                break
            if line in {"EMEDF", "Main Classes:"}:
                continue
            if not line:
                continue  # blank

            if match := category_re.match(line):
                category = {
                    "name": match.group(2),
                    "index": int(match.group(1)),
                    "instrs": [],
                }
                emedf_json["main_classes"].append(category)
            elif match := instr_re.match(line):
                if not category:
                    raise ValueError(f"Found instruction line without active category line: '{line}'")
                instruction = {
                    "name": match.group(2),
                    "index": int(match.group(1)),
                    "args": [],
                }
                category["instrs"].append(instruction)
            elif match := arg_enum_re.match(line):
                if not instruction:
                    raise ValueError(f"Found arg line without active instruction line: '{line}'")
                arg_type_str = match.group(1)
                name = match.group(2)
                enum_name = match.group(3)
                arg = {
                    "name": name,
                    "type": arg_types.index(arg_type_str),
                    "enum_name": enum_name,
                    "default": 0,
                    "min": 0,
                    "max": 0,
                    "increment": 0,
                    "format_string": "%d",
                    "unk1": 0,
                    "unk2": 0,
                    "unk3": 0,
                    "unk4": 0,
                }
                instruction["args"].append(arg)
            elif match := arg_re.match(line):
                if not instruction:
                    raise ValueError(f"Found arg line without active instruction line: '{line}'")
                arg_type_str = match.group(1)
                name = match.group(2)
                minimum_str = match.group(3)
                increment_str = match.group(4)
                maximum_str = match.group(5)
                default_str = match.group(6)
                arg = {
                    "name": name,
                    "type": arg_types.index(arg_type_str),
                    "enum_name": None,
                    "default": int_or_float(default_str),
                    "min": int_or_float(minimum_str),
                    "max": int_or_float(maximum_str),
                    "increment": int_or_float(increment_str),
                    "format_string": "%0.3f" if arg_type_str == "f" else "%d",  # TODO: handle "s"
                    "unk1": 0,
                    "unk2": 0,
                    "unk3": 0,
                    "unk4": 0,
                }
                instruction["args"].append(arg)

    write_json(json_path, emedf_json, indent=2)


if __name__ == '__main__':
    emedf_txt_to_json(
        r"C:\Users\Scott\Downloads\er-emedf-common-partial.txt",
        SOULSTRUCT_PATH("eldenring/events/emevd/er-common.emedf.json"),
    )
