"""Script used while refactoring EMEVD instructions and decompiler into new `EMEDF` dictionary.

Not likely to be used again, but kept here for posterity.
"""
import re
import typing as tp
from ast import literal_eval
from pathlib import Path
from soulstruct.utilities.files import read_json, PACKAGE_PATH


def _generate():

    def_re = re.compile(r"^def (.*)\((.*)\):", re.DOTALL)
    arg_re = re.compile(r"(\w[\w\d_]*)(: \w[\w\d_]*)?( *= *.*)?")
    doc_re = re.compile(r"^[ \"\n]*(.*?)[ \"\n]*$", re.DOTALL)  # strips all quotes and spaces

    base_module = PACKAGE_PATH("base/events/emevd/instructions.py").read_text().split("\n")
    game_module = Path("instructions.py").read_text().split("\n")
    instr_module = base_module + game_module

    emedf = read_json("../../darksouls1ptde/events/emevd/ds1-common.emedf.json")

    new_module = "EMEDF = {\n"

    for category_class in emedf["main_classes"]:
        category = category_class["index"]
        for instruction_class in category_class["instrs"]:
            index = instruction_class["index"]

            category_index = f"[{category}, {index}]"

            # Search module for (category, index)
            i_re = re.compile(rf"^ *instruction_info = \({category}, {index}\)")
            for i, line in enumerate(instr_module):
                if i_re.match(line):
                    # Go backwards to find function def start line
                    while not instr_module[i].startswith("def "):
                        i -= 1
                    def_string = instr_module[i]
                    # Append extra lines until a line ending with "):" is found
                    while not instr_module[i].endswith("):"):
                        i += 1
                        def_string += instr_module[i]  # will omit newline characters but that's fine (good, even)
                    if not (match := def_re.match(def_string)):
                        print(f"   {category_index} -- COULD NOT PARSE PYTHON DEF: {def_string}")
                        new_module += f"    # TODO: {category_index} (could not parse Python def)\n"
                        break
                    instr_name = match.group(1)
                    args = [s.strip() for s in match.group(2).split(",") if s.strip()]  # includes types and defaults
                    print(f"{category_index} | {instruction_class['name']} | {instr_name}({', '.join(args)})")
                    if len(args) != len(instruction_class["args"]):
                        print(f"    {category_index} -- ARG COUNT DOES NOT MATCH: {len(args)} vs. {len(instruction_class['args'])}")
                        new_module += f"    # TODO: {category_index} (arg count does not match)\n"
                        break

                    # Read docstring
                    i += 1  # after def
                    indent = " " * 12
                    if instr_module[i].lstrip().startswith("\"\"\""):
                        doc_string_lines = []
                        line_tex = doc_re.match(instr_module[i]).group(1)
                        if line_tex:
                            doc_string_lines.append(line_tex)
                        # Append extra lines until closing quotes are found
                        while not instr_module[i].rstrip().endswith("\"\"\""):
                            i += 1
                            line_text = doc_re.match(instr_module[i]).group(1)
                            doc_string_lines.append(line_text)
                        if not doc_string_lines[-1]:
                            doc_string_lines = doc_string_lines[:-1]
                        doc_string = f"\"\"\"\n{indent}" + f"\n{indent}".join(doc_string_lines) + f"\n        \"\"\""
                    else:
                        doc_string = "\"TODO\""

                    arg_dicts = []

                    for arg in args:
                        if not (arg_match := arg_re.match(arg)):
                            raise ValueError(f"    {category_index} -- COULD NOT PARSE ARG: {arg}")
                        arg_dict = {"name": arg_match.group(1)}  # type: dict[str, tp.Any]
                        if arg_match.group(2):
                            arg_dict["type"] = arg_match.group(2)[2:]  # skip ": "
                        else:
                            arg_dict["type"] = None
                        if arg_match.group(3):
                            arg_default = re.match(r"[ =]*(.*)", arg_match.group(3)).group(1)  # MUST match
                            if arg_default == "None":
                                arg_dict["default"] = "TODO"
                            else:
                                arg_dict["default"] = literal_eval(arg_default)
                                if arg_dict["type"] is None:
                                    arg_dict["type"] = type(arg_dict["default"]).__name__
                        else:
                            arg_dict["default"] = None  # indicates absence of default, NOT `None` as default
                        arg_dicts.append(arg_dict)

                    new_module += f"    ({category}, {index}): {{\n"
                    new_module += f"        \"alias\": \"{instr_name}\",\n"
                    new_module += f"        \"docstring\": {doc_string},\n"  # triple-quoted
                    if not arg_dicts:
                        new_module += f"        \"args\": {{}},\n"
                    else:
                        new_module += f"        \"args\": {{\n"
                        for arg_dict in arg_dicts:
                            new_module += f"            \"{arg_dict['name']}\": {{\n"
                            if arg_dict['type'] is None:
                                new_module += f"                \"type\": {arg_dict['type']},  # TODO\n"
                            else:
                                new_module += f"                \"type\": {arg_dict['type']},\n"
                            new_module += f"                \"default\": {repr(arg_dict['default'])},\n"
                            new_module += f"            }},\n"
                        new_module += f"        }},\n"
                    new_module += "    },\n"
                    break
            else:
                new_module += f"    # TODO: Could not find {category_index}: {instruction_class['name']}\n"

    new_module += "}\n"
    print(new_module)


if __name__ == '__main__':
    _generate()
