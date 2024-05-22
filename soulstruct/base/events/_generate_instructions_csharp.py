"""Module to generate the basic set of C# instructions and partials that return `SoulsFormats.EMEVD.Instruction`."""
import inspect
import re
import textwrap
from enum import IntEnum

from soulstruct.base.events.emevd.emedf import ArgType
from soulstruct.eldenring.events import enums

_MAX_LINE_WIDTH = 120

# Regex to replace all instances of "Id{capital_letter}" with "ID{capital_letter}".
_ID_CAPS_RE = re.compile(r"Id([A-Z_]|$)")


def get_mixed_case(name: str) -> str:
    """Converts `snake_case` to `mixedCase`."""
    mixed_case = "".join(word.capitalize() if i > 0 else word for i, word in enumerate(name.split("_")))
    # Do "ID" replacement.
    mixed_case = _ID_CAPS_RE.sub(r"ID\1", mixed_case)
    return mixed_case


def get_csharp_const(value) -> str:
    if isinstance(value, bool):
        return value and "1" or "0"
    if isinstance(value, float):
        return f"{value}f"
    return str(value)


def get_csharp_arg_string(
    args_dict: dict[str, dict],
    alias_length: int,
    evs_arg_order: list[str] = None,
    partial_kwargs: dict = None,
    no_defaults=False,
    add_event_layers: bool = False,
) -> tuple[str, list[str]]:
    """Formats args, types, and defaults for appearance in C# function signature.

    Also returns a list of just the arg names for actual use in the function.
    """
    arg_strings = []  # these are in EVS arg order (if different) for better defaults
    if partial_kwargs:
        arg_names = []  # these are ALSO in EVS order
    else:
        arg_names = [""] * len(args_dict)  # these are in true EMEDF order for use in `new Instruction()`
    last_default_arg = ""

    if evs_arg_order is None:
        evs_arg_order = list(args_dict.keys())
    emedf_arg_order = list(args_dict)

    partial_kwargs = partial_kwargs or {}

    for arg_name in evs_arg_order:
        arg_info = args_dict[arg_name]
        cased_arg_name = get_mixed_case(arg_name)
        try:
            internal_type = arg_info["internal_type"]
        except KeyError:
            print(arg_info)
            raise ValueError(f"Argument '{arg_name}' has no 'internal_type' specified.")
        match internal_type:
            case ArgType.f32:
                c_type = "float"
            case ArgType.fixstr:
                c_type = "string"
            case ArgType.u8:
                c_type = "byte"
            case ArgType.u16:
                c_type = "ushort"
            case ArgType.u32:
                c_type = "uint"
            case ArgType.s8:
                c_type = "sbyte"
            case ArgType.s16:
                c_type = "short"
            case ArgType.s32:
                c_type = "int"
            case _:
                raise ValueError(f"Invalid `ArgType`: {arg_info['internal_type']}")

        cast_type = ""
        if inspect.isclass(arg_info["type"]) and issubclass(arg_info["type"], IntEnum):
            # Enum will be defined in file.
            if not partial_kwargs:
                cast_type = f"({c_type})"
            c_type = f"{arg_info['type'].__name__}"
            arg_string = f"{c_type} {cased_arg_name}"
        else:
            arg_string = f"{c_type} {cased_arg_name}"

        if (
            not no_defaults
            and arg_info["default"] is not None
            and not callable(arg_info["default"])
            and not isinstance(arg_info["default"], str)
        ):
            default = arg_info["default"]
            if isinstance(default, IntEnum):
                default_str = f"{default.__class__.__name__}.{default.name}"
            else:
                default_str = get_csharp_const(default)
            arg_string += f" = {default_str}"
            last_default_arg = arg_name
        elif last_default_arg:
            raise ValueError(f"Non-default argument '{arg_name}' follows default argument '{last_default_arg}'.")

        if arg_name not in partial_kwargs:
            arg_strings.append(arg_string)

        if partial_kwargs:
            if arg_name in partial_kwargs:
                # Call uses baked partial kwarg, and same order as EVS.
                baked_value = partial_kwargs[arg_name]
                if isinstance(baked_value, IntEnum):
                    baked_str = f"{baked_value.__class__.__name__}.{baked_value.name}"
                else:
                    baked_str = get_csharp_const(baked_value)
                arg_names.append(baked_str)
            else:
                arg_names.append(f"{cased_arg_name}")
        else:
            emedf_index = emedf_arg_order.index(arg_name)
            arg_names[emedf_index] = f"{cast_type}{cased_arg_name}"

    if add_event_layers:
        arg_strings.append("int[]? eventLayers = null")

    one_line = ", ".join(arg_strings)
    if 7 + alias_length + len(one_line) > _MAX_LINE_WIDTH:
        return "\n        " + ",\n        ".join(arg_strings), arg_names
    else:
        return one_line, arg_names


def format_csharp_docstring(docstring: str) -> list[str]:
    """Format `docstring` with triple quotes and multiple lines if needed."""
    max_doc_line_width = _MAX_LINE_WIDTH - 8  # subtract indent and '/// '
    out_docstring_lines = ["<summary>"]
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
    out_docstring_lines.append("</summary>")
    return ["/// " + line for line in out_docstring_lines]


def _generate_eldenring_csharp_enums():
    files_lines = ["namespace WarBetween.Events;", ""]

    # First, all `enums` classes. Get all `BaseEMEVDEnum` subclasses from `enums` module:
    enums_classes = []
    for name, obj in vars(enums).items():
        if (
            isinstance(obj, type) and issubclass(obj, IntEnum) and obj is not IntEnum
            and not name.startswith("Base")
        ):
            enums_classes.append(obj)

    for enum_class in enums_classes:
        files_lines.append("\npublic enum " + enum_class.__name__ + "\n{")
        for name, value in enum_class.__members__.items():
            files_lines.append("    " + name + " = " + str(value.value) + ",")
        files_lines.append("}")

    return "\n".join(files_lines)


def _generate_eldenring_csharp_instructions(emedf_dict):

    files_lines = [
        "using static SoulsFormats.EMEVD;",
        "",
        "namespace WarBetween.Events;",
        "",
        "",
        "/// <summary>",
        "/// Soulstruct-generated class for Elden Ring EMEVD instructions.",
        "/// </summary>",
        "public static class EMEDF",
        "{",
    ]

    instr_lines = []

    # Add RunEvent and RunCommonEvent.
    for (category, index, name) in ((2000, 0, "RunEvent"), (2000, 6, "RunCommonEvent")):
        instr_lines.append("")
        instr_lines.append(f"/// <summary>")
        instr_lines.append(f"/// Run a {'CommonFunc' if index == 6 else 'local'} event ID with given slot and arguments.")
        instr_lines.append(f"/// </summary>")
        instr_lines.append(f"public static Instruction {name}(int slot, uint eventID, params object[] args)")
        instr_lines.append("{")
        instr_lines.append("    if (args.Length == 0)")
        instr_lines.append(f"        return new Instruction({category}, {index}, slot, eventID, 0);")
        instr_lines.append("    object[] allArgs = new object[2 + args.Length];")
        instr_lines.append("    allArgs[0] = slot;")
        instr_lines.append("    allArgs[1] = eventID;")
        instr_lines.append("    for (int i = 0; i < args.Length; i++)")
        instr_lines.append("        allArgs[i + 2] = args[i];")
        instr_lines.append(f"    return new Instruction({category}, {index}, allArgs);")
        instr_lines.append("}")

    for (category, index), instr_info in emedf_dict.items():

        if (category, index) == (2000, 0):
            continue  # RunEvent
        if (category, index) == (2000, 6):
            continue  # RunCommonEvent

        # print(category, index, instr_info["alias"])

        alias = instr_info["alias"]
        args_dict = instr_info["args"]  # NOT "evs_args"
        evs_args = instr_info.get("evs_args", None)
        if evs_args is not None and set(evs_args) != set(args_dict):
            evs_args = None  # args are NOT just reordered

        try:
            args, arg_names = get_csharp_arg_string(args_dict, len(alias), evs_args)
            defaults_failed = False
        except ValueError:
            # Problem with defaults. Just use EMEDF order and NO defaults.
            args, arg_names = get_csharp_arg_string(args_dict, len(alias), no_defaults=True)
            defaults_failed = True

        docstring = instr_info.get("docstring", "TODO")
        for arg_name, arg_info in args_dict.items():
            if "comment" in arg_info:
                docstring += f"\n{arg_name}: {arg_info['comment']}"
        instr_lines.append("")
        instr_lines += format_csharp_docstring(docstring)
        instr_lines.append(f"public static Instruction {alias}({args})")
        if arg_names:
            instr_lines.append(f"    => new({category}, {index}, {', '.join(arg_names)});")
        else:
            instr_lines.append(f"    => new({category}, {index});")

        for partial_name, partial_kwargs in instr_info.get("partials", {}).items():

            try:
                if defaults_failed:
                    raise ValueError("Partial auto fail")
                partial_args, partial_arg_names = get_csharp_arg_string(
                    args_dict, len(partial_name), evs_args, partial_kwargs=partial_kwargs
                )
            except ValueError:
                # Problem with defaults. Just use EMEDF order and NO defaults.
                partial_args, partial_arg_names = get_csharp_arg_string(
                    args_dict, len(partial_name), partial_kwargs=partial_kwargs, no_defaults=True
                )

            partial_kwargs_str = ", ".join(f"`{k}={v}`" for k, v in partial_kwargs.items() if k != "__docstring")
            partial_docstring = f"Calls `{alias}` with {partial_kwargs_str}."
            if "__docstring" in partial_kwargs:
                partial_docstring += f"\n{partial_kwargs['__docstring']}"
            instr_lines.append("")
            instr_lines += format_csharp_docstring(partial_docstring)
            instr_lines.append(f"public static Instruction {partial_name}({partial_args})")
            instr_lines.append(f"    => {alias}({', '.join(partial_arg_names)});")

        if (category, index) == (0, 0):
            # Add AWAIT alias for condition groups.
            instr_lines.append("")
            instr_lines.append("/// <summary>")
            instr_lines.append("/// Load given condition group into MAIN (0) and wait for it to be true.")
            instr_lines.append("/// </summary>")
            instr_lines.append("public static Instruction AWAIT(ConditionGroup inputCondition)")
            instr_lines.append("    => IfConditionState(ConditionGroup.MAIN, 1, inputCondition);")

    instr_lines = ["    " + line for line in instr_lines]
    files_lines += instr_lines
    files_lines.append("}")

    return "\n".join(files_lines)


if __name__ == '__main__':
    from soulstruct.eldenring.events.emevd.emedf import EMEDF
    # file = _generate_eldenring_csharp_enums()
    # file = _generate_eldenring_csharp_instructions(EMEDF)
    # print(file)
    for (category, index), instr_info in EMEDF.items():
        print(f"    [({category}, {index})] = \"{instr_info['alias']}\",")
