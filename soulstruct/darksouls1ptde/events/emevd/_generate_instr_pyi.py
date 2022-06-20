"""Generate an `instructions` PYI module for intellisense in EVS scripts.

Uses `*.emedf.json` files shared among the modding community (HotPocketRemix, thefifthmatt) and my `EMEDF` extension
dict. Only needs to be run whenever the EMEDF JSON or my EMEDF dictionary is updated.

Does NOT manage extra (real, not PYI) instructions in `instr_wrappers.py`, which must handle their own numeric output
using arg types in EMEDF.
"""
import inspect
import textwrap
import typing as tp
from pathlib import Path

from soulstruct.utilities.files import read_json


_DEF_TEMPLATE = "def {alias}({args}):"
_MAX_LINE_WIDTH = 120


def get_arg_string(args_dict: dict[str, dict], alias_length: int) -> str:
    """Formats args, types, and defaults for appearance in Python def signature."""
    arg_strings = []
    for arg_name, arg_info in args_dict.items():
        arg_string = arg_name
        if arg_info["type"] is not None:
            if inspect.isclass(arg_info["type"]):
                arg_string += f": {arg_info['type'].__name__}"
            else:
                if tp.get_origin(arg_info["type"]) is tp.Union:
                    arg_types = tp.get_args(arg_info['type'])
                    arg_string += f": {' | '.join(a.__name__ for a in arg_types)}"
                else:
                    raise TypeError(f"Invalid type for arg '{arg_name}': {arg_info['type']}")
            long_default = True
        else:
            long_default = False
        if arg_info["default"] is not None:
            if callable(arg_info["default"]):
                # PYI file says `None`. Actual code will use the default handler lambda.
                arg_string += " = None" if long_default else "=None"
            elif arg_info["default"] == "TODO":
                # Mark as TO DO (in EMEDF dict).
                arg_string += " = None" if long_default else "=None"
            else:
                arg_string += f" = {arg_info['default']}" if long_default else f"={arg_info['default']}"
        arg_strings.append(arg_string)
    one_line = ", ".join(arg_strings)
    if 7 + alias_length + len(one_line) > _MAX_LINE_WIDTH:
        return "\n    " + "\n    ".join(s + "," for s in arg_strings) + "\n"
    else:
        return one_line


def get_docstring(docstring: str):
    """Format `docstring` with triple quotes and multiple lines if needed."""
    max_doc_line_width = _MAX_LINE_WIDTH - 4  # subtract indent
    out_docstring_lines = ["\"\"\""]
    in_lines = docstring.split("\n")
    # Remove empty lines from start and finish.
    while not in_lines[0].strip():
        in_lines = in_lines[1:]
    while not in_lines[-1].strip():
        in_lines = in_lines[:-1]
    for in_line in in_lines:
        in_line = in_line.strip()
        if in_line:
            out_docstring_lines += textwrap.wrap(in_line, width=max_doc_line_width)
        else:
            out_docstring_lines.append("")
    out_docstring_lines.append("\"\"\"")
    return "    " + "\n    ".join(out_docstring_lines)  # lines are already indented


def generate_instr_pyi(emedf_json_path: Path | str, emedf_dict: dict, pyi_path: Path | str):
    emedf = read_json(emedf_json_path)

    # TODO: __all__
    pyi_str = (
        "\"\"\"AUTOMATICALLY GENERATED. Do not edit this module.\"\"\""
        "from soulstruct.game_types import *\n"
        "from .enums import *\n\n\n"
    )

    for cat_cls in emedf["main_classes"]:
        category = cat_cls["index"]
        for instr_class in cat_cls["instrs"]:
            index = instr_class["index"]
            c_i = f"({category}, {index})"
            try:
                instr_info = emedf_dict[category, index]
            except KeyError:
                print(f"Instruction {c_i} is not in Soulstruct `EMEDF` dictionary.")
                continue  # TODO
            alias = instr_info["alias"]
            args = get_arg_string(instr_info["args"], len(alias))
            pyi_str += _DEF_TEMPLATE.format(alias=alias, args=args) + "\n"
            if "docstring" in instr_info:
                pyi_str += get_docstring(instr_info["docstring"]) + "\n"
            else:
                pyi_str += "    \"\"\"TODO\"\"\""
            pyi_str += "\n\n"

    print(pyi_str)  # TODO
    Path(pyi_path).write_text(pyi_str)


if __name__ == '__main__':
    from soulstruct.darksouls1ptde.events.emevd.emedf import EMEDF
    generate_instr_pyi("ds1-common.emedf.json", EMEDF, "instr_new.pyi")
