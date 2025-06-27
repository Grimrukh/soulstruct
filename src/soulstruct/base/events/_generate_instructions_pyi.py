"""Generate an `instructions` PYI module for intellisense in EVS scripts.

Uses `*.emedf.json` files shared among the modding community (HotPocketRemix, thefifthmatt) and my `EMEDF` extension
dict. Only needs to be run whenever the EMEDF JSON or my EMEDF dictionary is updated.

Does NOT manage extra (real, not PYI) instructions in `instr_wrappers.py`, which must handle their own numeric output
using arg types in EMEDF.
"""
from __future__ import annotations

import inspect
import textwrap
import typing as tp
from enum import IntEnum
from pathlib import Path

from soulstruct.utilities.files import SOULSTRUCT_PATH


_DEF_TEMPLATE = "\n\n# ({category}, {index})\ndef {alias}({args}):"
_DEF_TEMPLATE_RET = "\n\ndef {alias}({args}) -> {ret_type}:"
_MAX_LINE_WIDTH = 120


# Shared EMEVD names defined in all games' `instructions.pyi` module.
# Note that `MAIN` is not defined here, as it will appear in each game's condition enum.
BASICS = """
# Restart decorators. They can be used as names (not function calls) or have an event ID argument.
def ContinueOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...
def RestartOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...
def EndOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...

# Dummy enum for accessing event flags defined by events.
class EVENTS(Flag): ...


class Condition:
    \"\"\"
    Create a condition group for use in `Await` or `If` instructions.
    
    If `hold = True`, the EVS parser will NOT permit the internal condition group slot assigned to this `Condition` to
    be automatically re-used once it is evaluated by the game engine and marked as OLD (e.g. by a `Main.AWAIT()` call).    
    \"\"\"
    def __init__(self, condition, hold: bool = False): ...


class HeldCondition(Condition):
    \"\"\"
    Alternative syntax for `Condition(condition, hold=True)`. (See above.)
    \"\"\"
    def __init__(self, condition): ...


def LastResult(condition_group: ConditionGroup | Condition):
    \"\"\"
    Wrap a defined `Condition` or naked condition group like `AND_1` with this to tell EVS/EMEVD that you want to check
    the LAST RESULT of this condition group rather than actively re-evaluating it.
    \"\"\"    


def Await(condition):
    \"\"\"
    The Await function. Equivalent to `MAIN.Await()`, which the EVS decompiler will prefer.
    
    You can also use the built-in 'await' Python keyword, but Python linters might complain about this (e.g. because
    you haven't declared your function with `async def` or because of the type being passed to `await`).
    \"\"\"
    ...


def enable_debug():
    \"\"\"
    Enables EVS debugging for the rest of the EVS file. Disable with `disable_debug()`.
    \"\"\"
    ...


def disable_debug():
    \"\"\"
    Disables EVS debugging for the rest of the EVS file. Enable with `enable_debug()`.
    \"\"\"
    ...


# Terminators that can be returned by events as cleaner syntax.
END = ...  # use with `return END`, identical to `return` or `End()`
RESTART = ...  # use with `return RESTART`, identical to `Restart()`

"""


def get_arg_string(args_dict: dict[str, dict], alias_length: int, add_event_layers: bool = False) -> str:
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
            default = arg_info["default"]
            if callable(default):
                # PYI file says `None`. Actual code will use the default handler lambda.
                arg_string += " = None" if long_default else "=None"
            elif default == "TODO":
                # Mark as TO DO (in EMEDF dict).
                arg_string += " = None" if long_default else "=None"
            elif isinstance(default, str):
                arg_string += f" = \"{default}\"" if long_default else f"=\"{default}\""
            else:
                if isinstance(default, IntEnum):
                    default = f"{default.__class__.__name__}.{default.name}"
                arg_string += f" = {default}" if long_default else f"={default}"
        arg_strings.append(arg_string)
    if add_event_layers:
        arg_strings.append("event_layers=()")
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


_RUN_EVENT_TEMPLATE = "def Run{0}Event(event_id: int | tp.Callable, {1}args = (0,), arg_types = \"\"{2}):"


def get_run_event_string(common=False, has_slot=True, has_event_layers=False):
    return _RUN_EVENT_TEMPLATE.format(
        "Common" if common else "",
        "slot: int = 0, " if has_slot else "",
        ", event_layers=()" if has_event_layers else "",
    )


def generate_instr_pyi(
    game_module_name: str,
    emedf_dict: dict,
    emedf_aliases: dict,
    emedf_tests: dict,
    emedf_comparison_tests: dict,
    condition_group_enum: type[IntEnum],
    pyi_path: Path | str,
    compiler_module,
    has_event_layers: bool = False,
    has_run_common_event=False,
    run_common_event_takes_slot=False,
):
    """Write Soulstruct `instructions.pyi` module for given game."""
    compiler_names = [
        name for name in compiler_module.__all__
        if name not in {"COMPILER", "compile_instruction", "get_compile_func", "BooleanTestCompiler"}
    ]

    pyi_docstring = (
        "\"\"\"AUTOMATICALLY GENERATED. Do not edit this module manually.\n"
        "\n"
        "Import this into any EVS script to have full access to instructions.\n"
        "Make sure you also do `from soulstruct.{game}.events import *` to get all enums, constants, and tests.\n"
        "You will likely also want `from soulstruct.{game}.game_types import *`.\n"
        "\"\"\"\n\n")
    pyi_imports = (
        "import typing as tp\n\n"
        f"from soulstruct.{game_module_name}.game_types import *\n"
        "from .emevd.compiler import *\n"  # custom instructions
        "from .enums import *\n"
    )

    pyi_all_lines = [
        "# Basics:",
        "\"ContinueOnRest\",",
        "\"RestartOnRest\",",
        "\"EndOnRest\",",
        "\"EVENTS\",",
        "\"Condition\",",
        "\"HeldCondition\",",
        "\"LastResult\",",
        "\"Await\",",
        "\"END\",",
        "\"RESTART\",",
        "\"RunEvent\",",
        "\"enable_debug\",",
        "\"disable_debug\",",
    ]

    pyi_funcs_str = BASICS

    pyi_all_lines.append("# Condition groups:")
    pyi_funcs_str += "\n# Condition groups:\n"
    for condition_group in condition_group_enum:
        # Defined in enum order, which usually matches value (from highest OR through MAIN to highest AND).
        pyi_funcs_str += f"{condition_group.name} = {condition_group_enum.__name__}.{condition_group.name}\n"
        pyi_all_lines.append(f"\"{condition_group.name}\",")

    pyi_all_lines.append("# Built-in instructions:")

    if game_module_name == "bloodborne":
        # Bloodborne supports `common_func` event import, but still uses `RunEvent` for them and has no
        # `RunCommonEvent` instruction. We also know it does NOT support event layers.
        pyi_funcs_str += (
            f"\n\n{get_run_event_string()}\n"
            "    \"\"\"Run an event by its ID or function. "
            "In Bloodborne, this could be a event defined in `common`.\"\"\"\n"
            "    ...\n"
        )
    elif has_event_layers:
        # We know that supporting event layers == supporting `common_func` and `RunCommonEvent`.
        pyi_funcs_str += (
            f"\n\n{get_run_event_string(has_event_layers=True)}\n"
            "    \"\"\"Run an event by its ID or function. "
            "This should NOT be an event defined in `common_func`.\"\"\"\n"
            "    ...\n"
        )
    else:
        pyi_funcs_str += (
            f"\n\n{get_run_event_string()}\n"
            "    \"\"\"Run an event by its ID or function. Use this for imported 'template' events as well.\"\"\"\n"
            "    ...\n"
        )

    if has_run_common_event:
        pyi_all_lines.append(f"\"RunCommonEvent\",")
        pyi_funcs_str += "\n\n"
        pyi_funcs_str += get_run_event_string(common=True, has_slot=run_common_event_takes_slot, has_event_layers=True)
        pyi_funcs_str += (
            f"\n    \"\"\"\n     Run a common event by its ID or function. "
            f"{'Also accepts slot, though the purpose of it is unclear. ' if run_common_event_takes_slot else ''}\n\n"
            f"    This event is typically defined in `common_func` but may also be local.\n    \"\"\"\n"
            f"    ...\n"
        )

    for (category, index), instr_info in emedf_dict.items():
        alias = instr_info["alias"]
        if alias in compiler_names:
            # Default function is overridden in `compiler`. Omit def AND partials from PYI.
            # Should only really occur for `RunEvent` and its kin.
            pyi_funcs_str += f"\n\n# Instruction `{alias}` ({category}, {index}) is defined in the `compiler` module.\n"
            continue
        args_dict = {}
        for evs_arg_name, evs_arg_info in instr_info.get("evs_args", instr_info["args"]).items():
            args_dict[evs_arg_name] = instr_info["args"][evs_arg_name] if not evs_arg_info else evs_arg_info
        args = get_arg_string(args_dict, len(alias), add_event_layers=has_event_layers)
        pyi_funcs_str += _DEF_TEMPLATE.format(category=category, index=index, alias=alias, args=args) + "\n"
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
            partial_args = get_arg_string(partial_args_dict, len(partial_name), add_event_layers=has_event_layers)
            pyi_funcs_str += _DEF_TEMPLATE.format(
                category=category, index=index, alias=partial_name, args=partial_args) + "\n"
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
    pyi_all_lines.append("\"EnableThisFlag\",")
    pyi_all_lines.append("\"DisableThisFlag\",")

    if compiler_names:
        pyi_all_lines.append("# Custom instructions from `compiler`:")
        for name in compiler_names:
            pyi_all_lines.append(f"\"{name}\",")

    pyi_all_lines.append("# Boolean test functions:")

    for test_name, test_info in emedf_tests.items():

        # We use the 'If' instruction to generate the signatures.
        # TODO: EMEDF_TESTS generator should make sure the partial signatures are identical.
        if_instr_name = test_info["if"]
        partial_docstring = ""
        try:
            category, index, instr_info = emedf_aliases[if_instr_name]
        except KeyError:
            if if_instr_name in compiler_names:
                test_func = getattr(compiler_module, if_instr_name)
                parameters = inspect.signature(test_func).parameters
                type_hints = tp.get_type_hints(test_func)  # `parameters` may contain strings instead of classes
                test_args_dict = {
                    p.name: {
                        "type": type_hints[name],
                        "default": (lambda: None) if p.default is None
                        else (p.default if p.default != p.empty else None)
                    }
                    for name, p in parameters.items()
                    if name != "condition"
                }
                partial_docstring = f"Calls `compiler.{if_instr_name}`."
            else:
                print(compiler_names)
                raise KeyError(f"No instruction named `{if_instr_name}` in EMEDF or compiler module.")
        else:
            args_dict = {}
            for evs_arg_name, evs_arg_info in instr_info.get("evs_args", instr_info["args"]).items():
                args_dict[evs_arg_name] = instr_info["args"][evs_arg_name] if not evs_arg_info else evs_arg_info

            if instr_info["alias"] == if_instr_name:
                test_args_dict = {
                    arg_name: arg_info for arg_name, arg_info in args_dict.items()
                    if arg_name not in {"condition", "line_count", "label"}
                }
            else:
                # Also remove baked kwargs, in addition to testing kwargs (condition, line_count, label).
                partial_kwargs = instr_info["partials"][if_instr_name]  # guaranteed to exist
                test_args_dict = {
                    arg_name: arg_info for arg_name, arg_info in args_dict.items()
                    if arg_name not in partial_kwargs and arg_name not in {"condition", "line_count", "label"}
                }
                if "__docstring" in partial_kwargs:
                    partial_docstring = f"\n{partial_kwargs['__docstring']}"

        test_args = get_arg_string(test_args_dict, len(if_instr_name), add_event_layers=has_event_layers)
        pyi_funcs_str += _DEF_TEMPLATE_RET.format(alias=test_name, args=test_args, ret_type="bool") + "\n"

        if partial_docstring:
            pyi_funcs_str += format_docstring(partial_docstring) + "\n"
        pyi_funcs_str += "    ...\n"
        pyi_all_lines.append(f"\"{test_name}\",")

    for comparison_test_name, comparison_test_info in emedf_comparison_tests.items():
        test_name = comparison_test_info["test_name"]
        if_instr_name = emedf_tests[test_name]["if"]  # must be present
        category, index, instr_info = emedf_aliases[if_instr_name]  # must be present
        partial_docstring = f"Compare output to a value as a shortcut for calling `{test_name}(...)`."
        args_dict = {}
        for evs_arg_name, evs_arg_info in instr_info.get("evs_args", instr_info["args"]).items():
            args_dict[evs_arg_name] = instr_info["args"][evs_arg_name] if not evs_arg_info else evs_arg_info
        test_args_dict = {
            arg_name: arg_info for arg_name, arg_info in args_dict.items()
            if arg_name not in {"condition", "line_count", "label", "comparison_type", "value"}
        }

        test_args = get_arg_string(test_args_dict, len(if_instr_name), add_event_layers=has_event_layers)
        ret_type = comparison_test_info["return_type"].__name__
        pyi_funcs_str += _DEF_TEMPLATE_RET.format(alias=comparison_test_name, args=test_args, ret_type=ret_type) + "\n"

        if partial_docstring:
            pyi_funcs_str += format_docstring(partial_docstring) + "\n"
        pyi_funcs_str += "    ...\n"
        pyi_all_lines.append(f"\"{comparison_test_name}\",")

    pyi_all = "__all__ = [\n    " + "\n    ".join(pyi_all_lines) + "\n]\n\n"
    pyi_str = pyi_docstring + pyi_all + pyi_imports + pyi_funcs_str
    # print(pyi_str)
    print(f"Writing {pyi_path}...")
    Path(pyi_path).write_text(pyi_str)


def darksouls1ptde():
    from soulstruct.darksouls1ptde.events.emevd import compiler
    from soulstruct.darksouls1ptde.events.enums import ConditionGroup
    from soulstruct.darksouls1ptde.events.emevd.emedf import EMEDF, EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS
    generate_instr_pyi(
        "darksouls1ptde",
        EMEDF,
        EMEDF_ALIASES,
        EMEDF_TESTS,
        EMEDF_COMPARISON_TESTS,
        ConditionGroup,
        SOULSTRUCT_PATH("darksouls1ptde/events/instructions.pyi"),
        compiler,
    )


def darksouls1r():
    from soulstruct.darksouls1r.events.emevd import compiler
    from soulstruct.darksouls1r.events.enums import ConditionGroup
    from soulstruct.darksouls1r.events.emevd.emedf import EMEDF, EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS
    generate_instr_pyi(
        "darksouls1r",
        EMEDF,
        EMEDF_ALIASES,
        EMEDF_TESTS,
        EMEDF_COMPARISON_TESTS,
        ConditionGroup,
        SOULSTRUCT_PATH("darksouls1r/events/instructions.pyi"),
        compiler,
    )


def bloodborne():
    from soulstruct.bloodborne.events.emevd import compiler
    from soulstruct.bloodborne.events.enums import ConditionGroup
    from soulstruct.bloodborne.events.emevd.emedf import EMEDF, EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS
    generate_instr_pyi(
        "bloodborne",
        EMEDF,
        EMEDF_ALIASES,
        EMEDF_TESTS,
        EMEDF_COMPARISON_TESTS,
        ConditionGroup,
        SOULSTRUCT_PATH("bloodborne/events/instructions.pyi"),
        compiler,
    )


def darksouls3():
    from soulstruct.darksouls3.events.emevd import compiler
    from soulstruct.darksouls3.events.enums import ConditionGroup
    from soulstruct.darksouls3.events.emevd.emedf import EMEDF, EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS
    generate_instr_pyi(
        "darksouls3",
        EMEDF,
        EMEDF_ALIASES,
        EMEDF_TESTS,
        EMEDF_COMPARISON_TESTS,
        ConditionGroup,
        SOULSTRUCT_PATH("darksouls3/events/instructions.pyi"),
        compiler,
        has_event_layers=True,
    )


def eldenring():
    from soulstruct.eldenring.events.emevd import compiler
    from soulstruct.eldenring.events.enums import ConditionGroup
    from soulstruct.eldenring.events.emevd.emedf import EMEDF, EMEDF_ALIASES, EMEDF_TESTS, EMEDF_COMPARISON_TESTS

    generate_instr_pyi(
        "eldenring",
        EMEDF,
        EMEDF_ALIASES,
        EMEDF_TESTS,
        EMEDF_COMPARISON_TESTS,
        ConditionGroup,
        SOULSTRUCT_PATH("eldenring/events/instructions.pyi"),
        compiler,
        has_event_layers=True,
        has_run_common_event=True,
        run_common_event_takes_slot=True,
    )


if __name__ == '__main__':
    darksouls1ptde()
    darksouls1r()
    bloodborne()
    darksouls3()
    eldenring()
