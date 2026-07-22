"""Programmatic cross-checks of the Elden Ring EVS instruction API against the EMEDF instruction table.

These are all PURE UNIT TESTS: no game installation and no test binaries are required. They exist because a
mismatch between the three parallel descriptions of the ER instruction set silently produces broken (or
unbuildable) event scripts:

    1. `eldenring/events/emevd/emedf.py`      -- `EMEDF` dict, the single source of truth `(category, index)`
                                                 -> alias, arg names/types/defaults, partials.
    2. `eldenring/events/emevd/compiler.py`   -- `EVSInstructionCompiler` custom wrapper methods, which call
                                                 `self._base_compile("<alias>", **kwargs)`. The alias AND the
                                                 kwarg names must exist in EMEDF or compilation raises.
    3. `eldenring/events/instructions.pyi`    -- generated intellisense stub; its `def`s and `__all__` are what
                                                 users actually see when writing EVS.

Failures marked `xfail` are confirmed library bugs (see the audit report), not test weaknesses.
"""
from __future__ import annotations

import ast
import collections
import inspect
from pathlib import Path

import pytest

from soulstruct.eldenring.events.emevd import compiler as er_compiler
from soulstruct.eldenring.events.emevd.compiler import EVSInstructionCompiler
from soulstruct.eldenring.events.emevd.decompiler import DECOMPILER, OPT_ARGS_DECOMPILER
from soulstruct.eldenring.events.emevd.emedf import (
    EMEDF,
    EMEDF_ALIASES,
    EMEDF_COMPARISON_TESTS,
    EMEDF_TESTS,
)
from soulstruct.eldenring.events.emevd.evs import EVSParser
from soulstruct.eldenring.events.enums import ConditionGroup, TeamType
from soulstruct.utilities.files import SOULSTRUCT_PATH


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _emedf_source_tree() -> ast.Module:
    path = Path(inspect.getfile(er_compiler)).parent / "emedf.py"
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def _compiler_source_tree() -> ast.Module:
    path = Path(inspect.getfile(er_compiler))
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def _pyi_path() -> Path:
    return Path(SOULSTRUCT_PATH("eldenring/events/instructions.pyi"))


def _pyi_tree() -> ast.Module:
    path = _pyi_path()
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def _pyi_functions() -> dict[str, list[str]]:
    """Map top-level PYI function name -> ordered positional arg names."""
    return {
        node.name: [a.arg for a in node.args.args]
        for node in _pyi_tree().body
        if isinstance(node, ast.FunctionDef)
    }


def _pyi_all() -> list[str]:
    for node in _pyi_tree().body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "__all__":
            return [ast.literal_eval(elt) for elt in node.value.elts]
    raise AssertionError("`instructions.pyi` has no `__all__`.")


def _evs_arg_names(instr_info: dict) -> list[str]:
    """EVS-facing argument names for a full (non-partial) instruction."""
    return list(instr_info.get("evs_args", instr_info["args"]))


def _emedf_evs_signatures() -> dict[str, list[str]]:
    """Expected EVS signature (ordered arg names) for every alias AND partial name in EMEDF."""
    signatures = {}
    for (category, index), info in EMEDF.items():
        arg_names = _evs_arg_names(info)
        signatures[info["alias"]] = arg_names
        for partial_name, partial_kwargs in info.get("partials", {}).items():
            signatures[partial_name] = [a for a in arg_names if a not in partial_kwargs]
    return signatures


def _base_compile_calls() -> list[tuple[int, str | None, list[str]]]:
    """Statically extract every `self._base_compile(...)` call in the ER compiler module.

    Returns `(lineno, instruction_name_or_None, kwarg_names)` tuples. `None` name means a non-literal
    (e.g. f-string) instruction name, which cannot be checked statically.
    """
    calls = []
    for node in ast.walk(_compiler_source_tree()):
        if not isinstance(node, ast.Call):
            continue
        if not (isinstance(node.func, ast.Attribute) and node.func.attr == "_base_compile"):
            continue
        if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
            name = node.args[0].value
        else:
            name = None
        kwargs = [kw.arg for kw in node.keywords if kw.arg is not None]
        calls.append((node.lineno, name, kwargs))
    return calls


# ---------------------------------------------------------------------------
# EMEDF internal consistency
# ---------------------------------------------------------------------------


def test_emedf_is_populated():
    assert len(EMEDF) > 300
    assert len(EMEDF_ALIASES) > len(EMEDF)  # partials add extra names
    assert EMEDF_TESTS and EMEDF_COMPARISON_TESTS


def test_every_emedf_entry_has_alias_args_and_internal_types():
    """Every instruction must be fully described, or `_base_compile` cannot build its `arg_types` string."""
    problems = []
    for (category, index), info in EMEDF.items():
        if not info.get("alias"):
            problems.append(f"({category}, {index}) has no alias")
            continue
        if not info["alias"].isidentifier():
            problems.append(f"({category}, {index}) alias {info['alias']!r} is not an identifier")
        for arg_name, arg_info in info["args"].items():
            if "internal_type" not in arg_info:
                problems.append(f"({category}, {index}) '{info['alias']}' arg '{arg_name}' has no internal_type")
            if "default" not in arg_info:
                problems.append(f"({category}, {index}) '{info['alias']}' arg '{arg_name}' has no 'default' key")
    assert not problems, "\n".join(problems)


def test_emedf_alias_and_partial_names_are_unique():
    """`EMEDF_ALIASES` is a flat name -> instruction dict; a duplicate name would silently shadow."""
    counter = collections.Counter()
    for info in EMEDF.values():
        counter[info["alias"]] += 1
        for partial_name in info.get("partials", {}):
            counter[partial_name] += 1
    duplicates = {name: count for name, count in counter.items() if count > 1}
    assert not duplicates, f"Duplicate EVS instruction names: {duplicates}"


def test_partial_kwargs_and_evs_args_reference_real_args():
    problems = []
    for (category, index), info in EMEDF.items():
        args = info["args"]
        for partial_name, partial_kwargs in info.get("partials", {}).items():
            for kwarg in partial_kwargs:
                if kwarg == "__docstring":
                    continue
                if kwarg not in args:
                    problems.append(f"({category}, {index}) partial '{partial_name}' bakes unknown arg '{kwarg}'")
    assert not problems, "\n".join(problems)


def test_evs_args_are_resolvable():
    """Each `evs_args` entry must either carry its own info dict or name a real EMEDF arg."""
    problems = []
    for (category, index), info in EMEDF.items():
        for evs_arg_name, evs_arg_info in info.get("evs_args", {}).items():
            if not evs_arg_info and evs_arg_name not in info["args"]:
                problems.append(
                    f"({category}, {index}) '{info['alias']}' evs_arg '{evs_arg_name}' is empty and not a real arg"
                )
    assert not problems, "\n".join(problems)


def test_emedf_tests_reference_existing_instructions():
    """Every boolean test in `EMEDF_TESTS` must map to a real EMEDF alias/partial or a compiler method."""
    custom = EVSInstructionCompiler._CUSTOM_FUNC_NAMES
    problems = []
    for test_name, test_info in EMEDF_TESTS.items():
        for key, instr_name in test_info.items():
            if instr_name not in EMEDF_ALIASES and instr_name not in custom:
                problems.append(f"test '{test_name}'[{key}] -> unknown instruction '{instr_name}'")
    for cmp_name, cmp_info in EMEDF_COMPARISON_TESTS.items():
        if cmp_info["test_name"] not in EMEDF_TESTS:
            problems.append(f"comparison test '{cmp_name}' -> unknown test '{cmp_info['test_name']}'")
    assert not problems, "\n".join(problems)


@pytest.mark.xfail(
    reason="EMEDF dict literal contains duplicate (category, index) keys: (1005, 1), (1005, 2) and (2003, 41). "
           "The later definition silently wins; (2003, 41) 'ActivateKillplaneForModel' is lost entirely.",
    strict=False,
)
def test_emedf_literal_has_no_duplicate_instruction_ids():
    """A duplicate key in the 5000-line `EMEDF` dict literal is invisible at runtime."""
    keys = []
    for node in _emedf_source_tree().body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "EMEDF":
            keys = [(ast.literal_eval(k), k.lineno) for k in node.value.keys]
            break
    assert keys, "Could not locate `EMEDF = {...}` literal in emedf.py."
    counter = collections.Counter(key for key, _ in keys)
    duplicates = {
        key: [lineno for k, lineno in keys if k == key]
        for key, count in counter.items() if count > 1
    }
    assert not duplicates, f"Duplicate instruction IDs in EMEDF literal: {duplicates}"


# ---------------------------------------------------------------------------
# Compiler wrappers vs EMEDF  (the highest-value cross-check)
# ---------------------------------------------------------------------------


def test_compiler_custom_names_are_capitalised_methods():
    """`process_custom_instructions` collects every capitalised callable on the class."""
    custom = EVSInstructionCompiler._CUSTOM_FUNC_NAMES
    assert "RunCommonEvent" in custom, "ER must override `RunCommonEvent`."
    assert "RunEvent" in custom, "`RunEvent` is inherited from the base compiler."
    for name in custom:
        assert name[0].isupper(), name
        assert callable(getattr(EVSInstructionCompiler, name))
    # Condition-arg indices are recorded for every custom function.
    assert set(EVSInstructionCompiler._CUSTOM_FUNC_CONDITION_ARGS) == custom


@pytest.mark.xfail(
    reason="ER compiler wrappers still call DS3-era instructions that FromSoft removed in Elden Ring: "
           "MoveToEntity, IfActionButtonBasic/Boss(+LineIntersect), PlayCutsceneAndMovePlayer/"
           "MoveSpecificPlayer/RotatePlayer. `Move()`, `IfActionButton()`/`ActionButton()` and most "
           "`PlayCutscene()` forms therefore raise ValueError in EVS.",
    strict=False,
)
def test_compiler_base_compile_targets_exist_in_emedf():
    missing = [
        (lineno, name) for lineno, name, _ in _base_compile_calls()
        if name is not None and name not in EMEDF_ALIASES
    ]
    assert not missing, f"`_base_compile` calls unknown instructions (compiler.py line, name): {missing}"


@pytest.mark.xfail(
    reason="ER EMEDF renamed the `obj` argument of (2005, 6)/(2005, 14) to `asset`, but "
           "`Enable/DisableAssetActivation` in compiler.py still pass `obj=`. Any EVS script using them "
           "fails to compile -- including Soulstruct's own decompiled vanilla output.",
    strict=False,
)
def test_compiler_base_compile_kwargs_exist_in_emedf():
    problems = []
    for lineno, name, kwargs in _base_compile_calls():
        if name is None or name not in EMEDF_ALIASES:
            continue  # covered by the previous test
        category, index, info = EMEDF_ALIASES[name]
        valid = set(_evs_arg_names(info)) - set(info.get("partials", {}).get(name, {}))
        bad = [k for k in kwargs if k not in valid and k != "arg_types"]
        if bad:
            problems.append(f"compiler.py:{lineno} `{name}` got {bad}; valid EVS args are {sorted(valid)}")
    assert not problems, "\n".join(problems)


def test_define_label_wrapper_covers_full_label_range():
    """`DefineLabel(n)` builds the instruction name dynamically, so it can't be checked statically."""
    for label in range(21):
        assert f"DefineLabel_{label}" in EMEDF_ALIASES, label
    assert "DefineLabel_21" not in EMEDF_ALIASES


@pytest.mark.xfail(
    reason="`EVSInstructionCompiler.compile` uses `kwargs.get('condition', args[index])`; the default is "
           "evaluated eagerly, so passing `condition` as a KEYWORD to any custom instruction raises "
           "IndexError instead of compiling.",
    strict=False,
)
def test_custom_instruction_accepts_condition_as_keyword():
    from soulstruct.eldenring.events.emevd import EMEVD

    evs = (
        "from soulstruct.eldenring.events import *\n"
        "from soulstruct.eldenring.events.instructions import *\n"
        "\n\n"
        "@ContinueOnRest(0)\n"
        "def Constructor():\n"
        '    """Event 0"""\n'
        "    IfPlayerHasGood(condition=AND_1, good=100)\n"
        "    End()\n"
    )
    EMEVD.from_evs_string(evs, map_name="m10_00_00_00")


# ---------------------------------------------------------------------------
# Decompiler vs EMEDF
# ---------------------------------------------------------------------------


@pytest.mark.xfail(
    reason="`decompiler.py` still registers handlers for instructions removed in ER: (3, 5), (3, 13), "
           "(3, 18), (3, 19) (old IfActionButton family) and (2002, 5) (PlayCutsceneAndRotatePlayer). "
           "They are unreachable dead code copied from the DS3 port.",
    strict=False,
)
def test_decompiler_only_registers_real_er_instructions():
    unknown = sorted(set(DECOMPILER) - set(EMEDF)) + sorted(set(OPT_ARGS_DECOMPILER) - set(EMEDF))
    assert not unknown, f"Decompiler handlers for instructions absent from ER EMEDF: {unknown}"


def test_opt_args_decompiler_covers_run_event_instructions():
    """`RunEvent`/`RunCommonEvent` take a variable number of trailing args and need the opt-args path."""
    assert set(OPT_ARGS_DECOMPILER) == {(2000, 0), (2000, 6)}
    assert EMEDF[(2000, 0)]["alias"] == "RunEvent"
    assert EMEDF[(2000, 6)]["alias"] == "RunCommonEvent"


def test_decompiler_and_normal_decompiler_are_disjoint():
    assert not set(DECOMPILER) & set(OPT_ARGS_DECOMPILER)


# ---------------------------------------------------------------------------
# `instructions.pyi` (public API surface) vs EMEDF
# ---------------------------------------------------------------------------


def test_pyi_stub_exists_and_parses():
    assert _pyi_path().is_file()
    assert len(_pyi_functions()) > 900


def test_pyi_signatures_match_emedf_argument_order():
    """THE critical check: a reordered/renamed PYI arg silently produces a wrong event script."""
    pyi_funcs = _pyi_functions()
    problems = []
    for name, expected in _emedf_evs_signatures().items():
        if name not in pyi_funcs:
            continue  # coverage is checked separately below
        actual = [a for a in pyi_funcs[name] if a != "event_layers"]
        if actual != expected:
            problems.append(f"{name}: PYI {actual} != EMEDF {expected}")
    assert not problems, "\n".join(problems)


def test_pyi_declares_event_layers_on_every_instruction():
    """ER supports event layers, so the generator appends `event_layers=()` to every instruction def."""
    pyi_funcs = _pyi_functions()
    emedf_names = set(_emedf_evs_signatures())
    missing = [
        name for name, args in pyi_funcs.items()
        if name in emedf_names and "event_layers" not in args
    ]
    assert not missing, f"Instructions missing `event_layers` in PYI: {missing}"


@pytest.mark.xfail(
    reason="`instructions.pyi` is stale relative to `emedf.py`: 6 instructions added to EMEDF have no stub "
           "(no intellisense, absent from `__all__`). Regenerating it is currently impossible because "
           "`_generate_instructions_pyi.py` still expects module-level compiler functions.",
    strict=False,
)
def test_pyi_covers_every_emedf_instruction():
    pyi_funcs = _pyi_functions()
    pyi_all = set(_pyi_all())
    custom = EVSInstructionCompiler._CUSTOM_FUNC_NAMES
    missing = sorted(
        name for name in _emedf_evs_signatures()
        if name not in pyi_funcs and name not in pyi_all and name not in custom
    )
    assert not missing, f"EMEDF instructions absent from `instructions.pyi`: {missing}"


def test_pyi_all_names_are_all_defined_somewhere():
    """Every exported PYI name must be a stub `def`, a condition group, a basic, or a compiler method."""
    pyi_funcs = _pyi_functions()
    pyi_tree = _pyi_tree()
    assigned = {
        target.id
        for node in pyi_tree.body if isinstance(node, ast.Assign)
        for target in node.targets if isinstance(target, ast.Name)
    }
    classes = {node.name for node in pyi_tree.body if isinstance(node, ast.ClassDef)}
    basics = {"EVENTS", "Condition", "HeldCondition", "END", "RESTART"}
    unresolved = [
        name for name in _pyi_all()
        if name not in pyi_funcs
        and name not in assigned
        and name not in classes
        and name not in basics
        and not hasattr(EVSInstructionCompiler, name)
    ]
    assert not unresolved, f"`instructions.pyi.__all__` exports undefined names: {unresolved}"


def test_pyi_has_no_duplicate_definitions():
    counter = collections.Counter(
        node.name for node in _pyi_tree().body if isinstance(node, ast.FunctionDef)
    )
    duplicates = {name: count for name, count in counter.items() if count > 1}
    assert not duplicates, duplicates


def test_pyi_exports_every_custom_compiler_instruction():
    """Custom wrappers have no stub `def`, so they must at least appear in `__all__` for intellisense."""
    pyi_all = set(_pyi_all())
    missing = sorted(EVSInstructionCompiler._CUSTOM_FUNC_NAMES - pyi_all)
    assert not missing, f"Custom compiler instructions absent from PYI `__all__`: {missing}"


# ---------------------------------------------------------------------------
# ER-specific enum / parser conventions
# ---------------------------------------------------------------------------


def test_condition_group_slots_match_enum():
    """ER has 15 AND and 15 OR condition groups (DS1 had 7)."""
    assert EVSParser.AND_SLOTS == list(range(1, 16))
    assert EVSParser.OR_SLOTS == [-i for i in range(1, 16)]
    assert {group.value for group in ConditionGroup} == set(range(-15, 16))
    assert ConditionGroup.MAIN == 0


def test_er_parser_flags():
    assert EVSParser.SUPPORTS_COMMON_FUNC is True
    assert EVSParser.USES_COMMON_FUNC_SLOT is True
    assert EVSParser.SPECIAL_EVENT_NAMES == {
        0: "Constructor",
        50: "Preconstructor",
        100: "Postconstructor1",
        200: "Postconstructor2",
    }


def test_run_common_event_is_a_real_instruction_in_er():
    """Unlike DS3/Bloodborne, ER has a dedicated (2000, 6) with a `slot` argument."""
    category, index, info = EMEDF_ALIASES["RunCommonEvent"]
    assert (category, index) == (2000, 6)
    assert list(info["args"]) == ["slot", "event_id", "args"]
    assert list(info["evs_args"]) == ["event_id", "slot", "args", "arg_types"]


@pytest.mark.xfail(
    reason="`TeamType.Unknown67 = 70` and `TeamType.Unknown70 = 70` share a value, so `Unknown70` is a "
           "silent alias and the `Unknown67` name contradicts its value.",
    strict=False,
)
def test_team_type_values_are_unique():
    names_by_value = collections.defaultdict(list)
    for name, value in TeamType.__members__.items():
        names_by_value[value.value].append(name)
    duplicates = {v: n for v, n in names_by_value.items() if len(n) > 1}
    assert not duplicates, duplicates


@pytest.mark.xfail(
    reason="`OnRestBehavior` is listed twice in both `events.__all__` and `events.enums.__all__`.",
    strict=False,
)
def test_public_all_lists_have_no_duplicates():
    import soulstruct.eldenring.events as events_module
    import soulstruct.eldenring.events.enums as enums_module

    problems = {}
    for module in (events_module, enums_module):
        duplicates = [n for n, c in collections.Counter(module.__all__).items() if c > 1]
        if duplicates:
            problems[module.__name__] = duplicates
    assert not problems, problems


def test_public_all_names_all_resolve():
    import soulstruct.eldenring.events as events_module
    import soulstruct.eldenring.events.enums as enums_module

    for module in (events_module, enums_module):
        missing = [name for name in module.__all__ if not hasattr(module, name)]
        assert not missing, f"{module.__name__}.__all__ exports missing names: {missing}"
