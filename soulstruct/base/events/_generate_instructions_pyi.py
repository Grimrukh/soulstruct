"""Generate an `instructions` PYI module for intellisense in EVS scripts.

Uses `*.emedf.json` files shared among the modding community (HotPocketRemix, thefifthmatt) and my `EMEDF` extension
dict. Only needs to be run whenever the EMEDF JSON or my EMEDF dictionary is updated.

Does NOT manage extra (real, not PYI) instructions in `instr_wrappers.py`, which must handle their own numeric output
using arg types in EMEDF.
"""
import inspect
import textwrap
import typing as tp
from enum import IntEnum
from pathlib import Path

from soulstruct.utilities.files import PACKAGE_PATH


_DEF_TEMPLATE = "\n\ndef {alias}({args}):"
_MAX_LINE_WIDTH = 120


def get_arg_string(args_dict: dict[str, dict], alias_length: int) -> str:
    """Formats args, types, and defaults for appearance in Python def signature."""
    arg_strings = []
    for arg_name, arg_info in args_dict.items():
        arg_string = arg_name
        if arg_info["type"] is not None:
            if inspect.isclass(arg_info["type"]):
                arg_string += f": {arg_info['type'].__name__}"
                if issubclass(arg_info["type"], IntEnum):
                    # `int` always permitted as well.
                    arg_string += " | int"
            else:
                if tp.get_origin(arg_info["type"]) is tp.Union:
                    arg_types = tp.get_args(arg_info['type'])
                    arg_string += f": {' | '.join(a.__name__ for a in arg_types)}"
                    if int not in arg_types and any(issubclass(arg_type, IntEnum) for arg_type in arg_types):
                        # `int` always permitted as well.
                        arg_string += " | int"
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
                default = arg_info['default']
                if isinstance(default, IntEnum):
                    default = f"{default.__class__.__name__}.{default.name}"
                arg_string += f" = {default}" if long_default else f"={default}"
        arg_strings.append(arg_string)
    one_line = ", ".join(arg_strings)
    if 7 + alias_length + len(one_line) > _MAX_LINE_WIDTH:
        return "\n    " + "\n    ".join(s + "," for s in arg_strings) + "\n"
    else:
        return one_line


def format_docstring(docstring: str):
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


def generate_instr_pyi(game_module_name: str, emedf_dict: dict, pyi_path: Path | str):
    from soulstruct.darksouls1ptde.events.emevd import compiler
    compiler_names = [
        name for name in compiler.__all__
        if name not in {"COMPILER", "compile_instruction", "get_compile_func"}
    ]

    pyi_docstring = (
        "\"\"\"AUTOMATICALLY GENERATED. Do not edit this module.\n"
        "\n"
        "Import this into any EVS script to have full access to instructions.\n"
        "Make sure you also do `from soulstruct.{game}.events import *` to get all enums, constants, and tests.\n"
        "\"\"\"\n\n")
    pyi_imports = (
        f"from soulstruct.{game_module_name}.game_types import *\n"
        "from .emevd.compiler import *\n"  # custom instructions
        "from .emevd.enums import *\n"
    )

    pyi_all_lines = []

    pyi_funcs_str = ""

    for (category, index), instr_info in emedf_dict.items():
        alias = instr_info["alias"]
        if alias in compiler_names:
            # Default function is overridden in `compiler`. Omit def AND partials from PYI.
            # Should only really occur for `RunEvent` and its kin.
            pyi_funcs_str += f"\n\n# Instruction `{alias}` is manually defined in the `compiler` module.\n"
            continue
        args_dict = {}
        for evs_arg_name, evs_arg_info in instr_info.get("evs_args", instr_info["args"]).items():
            args_dict[evs_arg_name] = instr_info["args"][evs_arg_name] if not evs_arg_info else evs_arg_info
        args = get_arg_string(args_dict, len(alias))
        pyi_funcs_str += _DEF_TEMPLATE.format(alias=alias, args=args) + "\n"
        docstring = instr_info.get("docstring", "TODO")
        for arg_name, arg_info in args_dict.items():
            if "comment" in arg_info:
                docstring += f"\n{arg_name}: {arg_info['comment']}"
        pyi_funcs_str += format_docstring(docstring) + "\n"
        pyi_all_lines.append(f"\"{alias}\",  # {category}[{index}]")

        for partial_name, partial_kwargs in instr_info.get("partials", {}).items():
            partial_args_dict = {
                arg_name: arg_info for arg_name, arg_info in args_dict.items()
                if arg_name not in partial_kwargs
            }
            partial_args = get_arg_string(partial_args_dict, len(partial_name))
            pyi_funcs_str += _DEF_TEMPLATE.format(alias=partial_name, args=partial_args) + "\n"
            partial_kwargs_str = ", ".join(f"`{k}={v}`" for k, v in partial_kwargs.items() if k != "__docstring")
            partial_docstring = f"Calls `{alias}` with {partial_kwargs_str}."
            if "__docstring" in partial_kwargs:
                partial_docstring += f"\n{partial_kwargs['__docstring']}"
            pyi_funcs_str += format_docstring(partial_docstring) + "\n"
            pyi_all_lines.append(f"\"{partial_name}\",")

    pyi_funcs_str += (
        "\n\ndef EnableThisFlag():\n"
        "    \"\"\"\n"
        "    Enables the flag ID of the current event. Does not detect slot.\n"
        "    \"\"\"\n\n\n"
        "def DisableThisFlag():\n"
        "    \"\"\"\n"
        "    Disables the flag ID of the current event. Does not detect slot.\n"
        "    \"\"\"\n"
    )
    pyi_all_lines.append(f"\"EnableThisFlag\",")
    pyi_all_lines.append(f"\"DisableThisFlag\",")

    if compiler_names:
        pyi_all = "__all__ = [\n    " + "\n    ".join(pyi_all_lines) + "\n\n    # From `compiler`:\n"
        pyi_all += "    " + "\n    ".join(f"\"{name}\"," for name in compiler_names) + "\n]\n\n"
    else:
        pyi_all = "__all__ = [\n    " + "\n    ".join(pyi_all_lines) + "\n]\n\n"
    pyi_str = pyi_docstring + pyi_all + pyi_imports + pyi_funcs_str
    # print(pyi_str)
    print(f"Writing {pyi_path}...")
    Path(pyi_path).write_text(pyi_str)


def darksouls1r():
    from soulstruct.darksouls1r.events.emevd.emedf import EMEDF
    generate_instr_pyi(
        "darksouls1r",
        EMEDF,
        PACKAGE_PATH("darksouls1r/events/instructions.pyi"),
    )


def darksouls1ptde():
    from soulstruct.darksouls1ptde.events.emevd.emedf import EMEDF
    generate_instr_pyi(
        "darksouls1ptde",
        EMEDF,
        PACKAGE_PATH("darksouls1ptde/events/instructions.pyi"),
    )


if __name__ == '__main__':
    darksouls1ptde()
    darksouls1r()
