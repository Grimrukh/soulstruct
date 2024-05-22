from __future__ import annotations

__all__ = [
    "AdvancedDecompiler",
]

import re

# TODO: A lot more can be done here.
#   - Implement `if LastResult(condition_group):` checks.
#   - Decompile 'Goto' instructions for games that support it. Complicated, however, because:
#       - When compiling `if` blocks, it will be ambiguous as to whether to use 'SkipLines' or 'Goto'. Obviously 'Goto'
#       is almost always preferred, and should affect nothing, but it would be annoying to lose vanilla faithfulness.
#       If we accept that, the rule could be something like 'use SkipLines when `if` block is <= 2 instructions'.
#       - When compiling `if` blocks to 'Goto', we have to be sure that the game has a supporting 'Goto', because they
#       did add and maybe remove some in later games. The compiler might already handle this automatically, though, by
#       constructing the EMEDF search alias automatically.


# Advanced decompilation of 1:1 EMEVD:EVS instruction lines into more complex, indented Python `if/else` blocks and
# some other useful substitutions for aliases like `MAIN.Await()`.

# NOTE: There is no 'LastConditionResult' version of this, since it acts upon condition groups directly.
_IF_CONDITION_RE = re.compile(
    r"^(?P<indent> *)IfCondition(?P<state>True|False)\("
    r"(?P<condition>(MAIN|((AND|OR)_\d+))), input_condition=(?P<input_condition>(MAIN|((AND|OR)_\d+)))\)$"
)
_IF_COMPARISON_RE = re.compile(
    r"^(?P<indent> *)If(?P<test>.*?)(?P<comp>Equal|NotEqual|GreaterThan|LessThan|GreaterThanOrEqual|LessThanOrEqual)"
    r"\((?P<condition>(MAIN|((AND|OR)_\d+)))(?P<pre_args>.*?), value=(?P<value>[\w_.]+)(?P<post_args>, .*?)?\)$"
)
_IF_OTHER_TEST_RE = re.compile(
    r"^(?P<indent> *)If(?P<test>.*?)\((?P<condition>(MAIN|((AND|OR)_\d+)))(?P<args>.*?)\)$"
)
_SKIP_TEST_RE = re.compile(
    r"^(?P<indent> *)SkipLinesIf(?P<test>.*?)\((?P<line_count>\d+)(?P<args>.*?)\)$"
)
# Checked WITHIN identified skip tests to find effective `else` blocks.
_UNCONDITIONAL_SKIP_RE = re.compile(
    r"^(?P<indent> *)SkipLines\((?P<line_count>\d+)\)$"
)
_RETURN_CONDITION_RE = re.compile(
    r"^(?P<indent> *)(?P<return_type>End|Restart)If(?P<eval_type>Condition|LastConditionResult)(?P<state>True|False)\("
    r"input_condition=(?P<condition>((AND|OR)_\d+))\)$"
)
_RETURN_RE = re.compile(
    r"^(?P<indent> *)(?P<return_type>End|Restart)If(?P<test>.*)\((?P<args>.*?)\)$"
)


# Convert instruction text to Python operator strings.
_COMPARISON_OPERATORS = {
    "Equal": "==",
    "NotEqual": "!=",
    "GreaterThan": ">",
    "LessThan": "<",
    "GreaterThanOrEqual": ">=",
    "LessThanOrEqual": "<=",
}


class AdvancedDecompiler:

    class _DecompileFrame:
        i: int  # line count
        in_lines: list[str]  # original 1:1 EVS instruction lines
        out_lines: list[str]  # more Pythonic output lines that may include indented blocks and new aliases

        def __init__(self, in_lines: list[str]):
            self.i = 0
            self.in_lines = in_lines
            self.out_lines = []

    emedf_tests: dict[str, dict[str, str]]
    emedf_comparison_tests: dict[str, dict[str, str]]

    _frame_stack: list[_DecompileFrame]
    
    def __init__(self, emedf_tests: dict[str, dict[str, str]], emedf_comparison_tests: dict[str, dict[str, str]]):
        self.emedf_tests = emedf_tests
        self.emedf_comparison_tests = emedf_comparison_tests
        self._frame_stack = []

    @property
    def i(self):
        return self._frame_stack[-1].i

    @i.setter
    def i(self, value: int):
        self._frame_stack[-1].i = value

    @property
    def in_lines(self):
        return self._frame_stack[-1].in_lines

    @property
    def out_lines(self):
        return self._frame_stack[-1].out_lines

    @property
    def current_line(self) -> str:
        return self.in_lines[self.i]
    
    def get_line_ahead(self, count: int = 1) -> str:
        return self.in_lines[self.i + count]

    def adv_decompile(self, instruction_lines: list[str], conditions_only=False) -> list[str]:
        """Parses basic EVS output (already a list of strings) and replaces it with relatively simply Python `if/else`
        tests and aliases like `MAIN.Await()` where possible.
    
        Also called recursively on sub-lists of instruction blocks.
    
        Note that none of the input `instruction_lines` have been indented yet, so we can add our own indentation here
        as necessary and ALL of it will be indented later by the caller `to_evs()`.
    
        TODO:
            - Currently, only "End/RestartIf" and "SkipIf" instructions (that do NOT skip other skip instructions) are
            being converted to `if` blocks.
            - Work to do for "If" condition decompilation:
                - Uses a modified condition-building EVS syntax that hasn't actually been implemented.
                - Main struggle is with line skips that skip OTHER skips (skip chains) or condition instructions (so
                it's ambiguous as to where the group instance should first be defined in EVS).
        """
    
        # Initialize state.
        self._frame_stack.append(self._DecompileFrame(instruction_lines))

        while self.i < len(self.in_lines):
    
            line = self.current_line
    
            if match := _IF_CONDITION_RE.match(line):
                self.if_condition(match.groupdict())
                continue

            if match := _IF_COMPARISON_RE.match(line):
                self.if_comparison(line, match.groupdict())
                continue

            if match := _IF_OTHER_TEST_RE.match(line):
                self.if_test(line, match.groupdict())
                continue
                
            if not conditions_only:                
                
                if match := _SKIP_TEST_RE.match(line):
                    self.skip_test(line, match.groupdict())
                    continue
    
                elif match := _RETURN_CONDITION_RE.match(line):
                    self.return_condition(match.groupdict())
                    continue
    
                elif match := _RETURN_RE.match(line):
                    self.return_test(line, match.groupdict())
                    continue

            # Failed to do any advanced decompiling. Copy line as-is.
            self.out_lines.append(line)
            self.i += 1
    
        # Remove any trailing blank lines that were added due to the last instruction.
        while self.out_lines[-1] == "":
            self.out_lines.pop()

        # Pop frame stack.
        stack = self._frame_stack.pop()
        
        return stack.out_lines
    
    def if_condition(self, match_dict: dict[str, str]):
        """One condition group is added to another."""
        indent = match_dict["indent"]
        state = match_dict["state"] == "True"
        condition = match_dict["condition"]
        input_condition = match_dict["input_condition"]
        if not state:
            input_condition = f"not {input_condition}"
    
        # TODO: If condition was just defined on previous line, we could move the whole thing here.
        #  However, this veers into "lost info" territory, as we won't know what condition number the game
        #  originally used (and would have to look ahead for "finished" usage).
    
        if condition == "MAIN":
            if self.out_lines and self.out_lines[-1] != "":
                self.out_lines.append("")
            self.out_lines.extend([f"{indent}MAIN.Await({input_condition})", ""])
            self.i += 1
        else:
            self.out_lines.append(f"{indent}{condition}.Add({input_condition})")
            self.i += 1

    def if_comparison(self, line: str, match_dict: dict[str, str]):
        indent = match_dict["indent"]
        test = match_dict["test"]
        operator = _COMPARISON_OPERATORS[match_dict["comp"]]
        if test not in self.emedf_comparison_tests:
            self.out_lines.append(line)
            self.i += 1
            return
        condition = match_dict["condition"]
        pre_args = match_dict["pre_args"].removeprefix(", ")
        value = match_dict["value"]
        post_args = match_dict["post_args"] if match_dict["post_args"] else ""
        if condition == "MAIN":
            if self.out_lines and self.out_lines[-1] != "":
                self.out_lines.append("")
            self.out_lines.extend([f"{indent}MAIN.Await({test}({pre_args}{post_args}) {operator} {value})", ""])
            self.i += 1
        else:
            self.out_lines.append(f"{indent}{condition}.Add({test}({pre_args}{post_args}) {operator} {value})")
            self.i += 1

    def if_test(self, line: str, match_dict: dict[str, str]):
        indent = match_dict["indent"]
        test = match_dict["test"]
        if test not in self.emedf_tests or "if" not in self.emedf_tests[test]:
            # 'if' should always be in tests dict, but just for clarity.
            self.out_lines.append(line)
            self.i += 1
            return
        condition = match_dict["condition"]
        args = match_dict["args"].removeprefix(", ")  # no need to split or parse (and could be empty)
        if condition == "MAIN":
            if self.out_lines and self.out_lines[-1] != "":
                self.out_lines.append("")
            self.out_lines.extend([f"{indent}MAIN.Await({test}({args}))", ""])
            self.i += 1
        else:
            self.out_lines.append(f"{indent}{condition}.Add({test}({args}))")
            self.i += 1

    def skip_test(self, line: str, match_dict: dict[str, str]):
        indent = match_dict["indent"]
        test = match_dict["test"]
        line_count = int(match_dict["line_count"])
        if line_count == 0:
            # Occurs rarely.
            self.out_lines.append(f"{line}  # NOTE: useless skip")
            self.i += 1
            return
        args = match_dict["args"].removeprefix(", ")
        # Find negated skip.
        for test_name, tests in self.emedf_tests.items():
            if tests.get("skip", "") == f"SkipLinesIf{test}":
                break
        else:
            # Could not find test name (possibly no negation).
            self.out_lines.append(line)
            self.i += 1
            return  
        if_block_lines = [f"{indent}{self.get_line_ahead(1 + j)}" for j in range(line_count)]
        if any("SkipLinesIf" in instr for instr in if_block_lines):
            # Cannot yet skip other skips. Ignore this line, and recur on block lines for conditions only.
            self.out_lines.append(line)
            self.i += 1
            self.out_lines.extend(self.adv_decompile(if_block_lines, conditions_only=True))
            self.i += len(if_block_lines)
            return
        if any(
            "SkipLines(" in instr for instr in (if_block_lines[:-1] if len(if_block_lines) > 1 else if_block_lines)
        ):
            # Cannot yet skip other unconditional skips EXCEPT as the last block instruction (`else`).
            self.out_lines.append(line)
            self.i += 1
            self.out_lines.extend(self.adv_decompile(if_block_lines, conditions_only=True))
            self.i += len(if_block_lines)
            return
        if unconditional_match := _UNCONDITIONAL_SKIP_RE.match(self.get_line_ahead(line_count)):
            else_line_count = int(unconditional_match.groupdict()["line_count"])
            else_block_lines = [
                f"{indent}    {self.get_line_ahead(line_count + 1 + j)}" for j in range(else_line_count)
            ]
            if any("SkipLines" in instr for instr in else_block_lines):
                # Cannot yet skip other skips (conditional or unconditional) in `else` block.
                self.out_lines.append(line)
                self.i += 1
                self.out_lines.extend(self.adv_decompile(if_block_lines, conditions_only=True))
                self.i += len(if_block_lines)
                return
            if_block_lines = if_block_lines[:-1]  # ignore unconditional skip
        else:
            else_line_count = 0
            else_block_lines = []
        self.out_lines.append(f"{indent}if {test_name}({args}):")
        self.i += 1
        # Recur on indented `if` block (which contains no skips, as per above).
        self.out_lines.extend(self.adv_decompile(
            [f"    {if_line}" for if_line in if_block_lines],
            conditions_only=False,
        ))
        self.i += line_count
        if else_block_lines:
            # Recur on indented `else` block (which contains no skips, as per above).
            self.out_lines.append(f"{indent}else:")
            # No need for `i += 1`, as `line_count` includes the unconditional skip that `else` is replacing.
            self.out_lines.extend(self.adv_decompile(else_block_lines, conditions_only=False))
            self.i += else_line_count

    def return_condition(self, match_dict: dict[str, str]):
        indent = match_dict["indent"]
        return_type = match_dict["return_type"].lower()
        state = match_dict["state"] == "True"
        condition = match_dict["condition"]
        if match_dict["eval_type"] == "LastConditionResult":
            condition = f"LastResult({condition})"
        if not state:
            condition = f"not {condition}"
        self.out_lines.append(f"{indent}if {condition}:")
        self.out_lines.append(f"{indent}    return{' RESTART' if return_type == 'restart' else ''}")
        self.i += 1

    def return_test(self, line: str, match_dict: dict[str, str]):
        indent = match_dict["indent"]
        return_type = match_dict["return_type"].lower()
        test = match_dict["test"]
        if test not in self.emedf_tests or return_type not in self.emedf_tests[test]:
            # Ignore (no end/restart test).
            self.out_lines.append(line)
            self.i += 1
            return
        args = match_dict["args"].removeprefix(", ")
        self.out_lines.append(f"{indent}if {test}({args}):")
        self.out_lines.append(f"{indent}    return{' RESTART' if return_type == 'restart' else ''}")
        self.i += 1
