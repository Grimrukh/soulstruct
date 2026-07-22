"""Pure-unit cross-checks between Bloodborne's EMEDF instruction dictionary, the custom EVS instruction
wrappers in `events/emevd/compiler.py`, and the generated `events/instructions.pyi` stub module.

These tests need no game data at all, so they always run. A mismatch here silently produces broken event
scripts (wrong argument order, missing arguments, instructions that cannot be compiled at all), so this is
the highest-value check for the `events` subpackage.
"""
from __future__ import annotations

import ast
import inspect
from pathlib import Path

import pytest

from soulstruct.bloodborne.events.emevd.emedf import (
    EMEDF,
    EMEDF_ALIASES,
    EMEDF_TESTS,
    EMEDF_COMPARISON_TESTS,
)
from soulstruct.bloodborne.events.emevd.compiler import EVSInstructionCompiler
from soulstruct.bloodborne.events.emevd.evs import EVSParser

# Names defined in the PYI's "BASICS" block, which are EVS syntax rather than EMEVD instructions.
_PYI_BASICS = {
    "ContinueOnRest",
    "RestartOnRest",
    "EndOnRest",
    "LastResult",
    "Await",
    "enable_debug",
    "disable_debug",
    "EnableThisFlag",
    "DisableThisFlag",
}

# Ignore keyword-only sugar that the generator appends to every signature.
_IGNORED_ARGS = {"event_layers"}


@pytest.fixture(scope="module")
def pyi_defs() -> dict[str, ast.FunctionDef]:
    """Parse `bloodborne/events/instructions.pyi` into a dict of top-level function defs."""
    import soulstruct.bloodborne.events as bb_events

    pyi_path = Path(bb_events.__file__).parent / "instructions.pyi"
    if not pyi_path.is_file():
        pytest.skip(f"Missing generated stub module: {pyi_path}")
    tree = ast.parse(pyi_path.read_text(encoding="utf-8"))
    return {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}


@pytest.fixture(scope="module")
def pyi_all() -> list[str]:
    import soulstruct.bloodborne.events as bb_events

    pyi_path = Path(bb_events.__file__).parent / "instructions.pyi"
    if not pyi_path.is_file():
        pytest.skip(f"Missing generated stub module: {pyi_path}")
    tree = ast.parse(pyi_path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "__all__":
            return [element.value for element in node.value.elts]
    pytest.fail("`__all__` not found in `instructions.pyi`.")


def _def_arg_names(node: ast.FunctionDef) -> list[str]:
    args = node.args
    names = [a.arg for a in args.posonlyargs + args.args + args.kwonlyargs]
    return [name for name in names if name not in _IGNORED_ARGS]


def _emedf_evs_signature(alias: str) -> list[str]:
    """EVS-visible argument names for an EMEDF alias or partial (baked kwargs removed)."""
    category, index, info = EMEDF_ALIASES[alias]
    evs_args = info.get("evs_args", info["args"])
    baked = info.get("partials", {}).get(alias, {}) if alias in info.get("partials", {}) else {}
    return [name for name in evs_args if name not in baked]


# ---------------------------------------------------------------------------
# EMEDF internal consistency
# ---------------------------------------------------------------------------


def test_emedf_keys_are_sorted_id_pairs():
    """EMEDF is keyed by `(category, index)` and re-sorted at module load."""
    keys = list(EMEDF)
    assert keys == sorted(keys)
    for key in keys:
        assert isinstance(key, tuple) and len(key) == 2
        assert all(isinstance(k, int) for k in key)


def test_emedf_entries_have_alias_and_args():
    for (category, index), info in EMEDF.items():
        assert "alias" in info, f"({category}, {index}) has no 'alias'."
        assert "args" in info, f"({category}, {index}) '{info.get('alias')}' has no 'args'."
        assert isinstance(info["args"], dict)


def test_emedf_aliases_are_unique():
    """Two instructions must never share an alias, or one silently shadows the other in `EMEDF_ALIASES`."""
    seen = {}
    for (category, index), info in EMEDF.items():
        alias = info["alias"]
        assert alias not in seen, f"Alias '{alias}' used by both {seen.get(alias)} and ({category}, {index})."
        seen[alias] = (category, index)
        for partial_name in info.get("partials", {}):
            assert partial_name not in seen, (
                f"Partial '{partial_name}' of ({category}, {index}) collides with {seen[partial_name]}."
            )
            seen[partial_name] = (category, index)


def test_emedf_args_all_have_internal_types():
    """Every EMEDF argument needs an `internal_type` (from `bb-common.emedf.json` or manual) to be packable."""
    missing = [
        f"({category}, {index}) {info['alias']}.{arg_name}"
        for (category, index), info in EMEDF.items()
        for arg_name, arg_info in info["args"].items()
        if "internal_type" not in arg_info
    ]
    assert not missing, f"EMEDF args without `internal_type`: {missing}"


def test_emedf_partial_baked_kwargs_are_real_args():
    bad = []
    for (category, index), info in EMEDF.items():
        arg_names = set(info.get("evs_args", info["args"])) | set(info["args"])
        for partial_name, baked in info.get("partials", {}).items():
            for key in baked:
                if key == "__docstring":
                    continue
                if key not in arg_names:
                    bad.append(f"({category}, {index}) partial '{partial_name}' bakes unknown arg '{key}'")
    assert not bad, bad


def test_emedf_evs_args_are_subset_of_args():
    """`evs_args` may rename/reorder, but every EMEDF `args` entry must be derivable."""
    bad = []
    for (category, index), info in EMEDF.items():
        if "evs_args" not in info:
            continue
        for arg_name, arg_info in info["args"].items():
            if arg_name in info["evs_args"]:
                continue
            if "from_evs" in arg_info or arg_info.get("type") is tuple:
                continue
            bad.append(f"({category}, {index}) {info['alias']}: EMEDF arg '{arg_name}' has no `from_evs`.")
    assert not bad, bad


# ---------------------------------------------------------------------------
# EMEDF tests dictionaries
# ---------------------------------------------------------------------------


def test_emedf_tests_reference_real_instructions():
    """Every boolean test entry must map to a real EMEDF alias/partial or a custom compiler method."""
    known = set(EMEDF_ALIASES) | set(EVSInstructionCompiler._CUSTOM_FUNC_NAMES)
    bad = [
        (test_name, key, instr_name)
        for test_name, info in EMEDF_TESTS.items()
        for key, instr_name in info.items()
        if instr_name not in known
    ]
    assert not bad, f"Unresolvable test instructions: {bad}"


def test_emedf_tests_always_have_if_variant():
    for test_name, info in EMEDF_TESTS.items():
        assert "if" in info, f"Test '{test_name}' has no 'if' instruction: {info}"


def test_emedf_test_variants_share_a_signature():
    """`IfX`, `SkipLinesIfX`, `EndIfX`, `RestartIfX` must take the same non-control arguments."""
    control_args = {"condition", "line_count", "label"}
    mismatches = []
    for test_name, info in EMEDF_TESTS.items():
        signatures = {}
        for key, instr_name in info.items():
            if instr_name in EVSInstructionCompiler._CUSTOM_FUNC_NAMES:
                continue  # custom Python wrapper; checked separately
            signatures[key] = [a for a in _emedf_evs_signature(instr_name) if a not in control_args]
        distinct = {tuple(sig) for sig in signatures.values()}
        if len(distinct) > 1:
            mismatches.append((test_name, signatures))
    assert not mismatches, f"Test variants with differing signatures: {mismatches}"


def test_emedf_comparison_tests_are_well_formed():
    for name, info in EMEDF_COMPARISON_TESTS.items():
        assert info["test_name"] in EMEDF_TESTS, f"Comparison test '{name}' has unknown test '{info['test_name']}'."
        assert isinstance(info["return_type"], type), f"Comparison test '{name}' return type is not a class."


# ---------------------------------------------------------------------------
# Custom compiler wrappers
# ---------------------------------------------------------------------------


def test_custom_compiler_methods_are_registered():
    """`process_custom_instructions()` must have collected every capitalised public method."""
    expected = {
        name for name in dir(EVSInstructionCompiler)
        if name and name[0].isupper() and callable(getattr(EVSInstructionCompiler, name))
    }
    assert expected == EVSInstructionCompiler._CUSTOM_FUNC_NAMES
    assert set(EVSInstructionCompiler._CUSTOM_FUNC_CONDITION_ARGS) == EVSInstructionCompiler._CUSTOM_FUNC_NAMES


def test_custom_compiler_condition_arg_indices_are_correct():
    """The cached `(condition, input_condition)` positional indices must match the real signatures."""
    for name, (cond_index, input_index) in EVSInstructionCompiler._CUSTOM_FUNC_CONDITION_ARGS.items():
        params = list(inspect.signature(getattr(EVSInstructionCompiler, name)).parameters)[1:]  # drop `self`
        expected_cond = params.index("condition") if "condition" in params else None
        expected_input = params.index("input_condition") if "input_condition" in params else None
        assert cond_index == expected_cond, f"{name}: condition index {cond_index} != {expected_cond}"
        assert input_index == expected_input, f"{name}: input_condition index {input_index} != {expected_input}"


def test_custom_compiler_base_compile_targets_exist():
    """Every `self._base_compile("Name", ...)` literal in the compiler module must be a real EMEDF alias."""
    import soulstruct.bloodborne.events.emevd.compiler as compiler_module

    source = Path(compiler_module.__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    missing = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not (isinstance(func, ast.Attribute) and func.attr == "_base_compile"):
            continue
        if not node.args:
            continue
        first = node.args[0]
        if isinstance(first, ast.Constant) and isinstance(first.value, str):
            if first.value not in EMEDF_ALIASES:
                missing.append(first.value)
        elif isinstance(first, ast.JoinedStr):
            continue  # e.g. `DefineLabel_{n}`, checked below
    assert not missing, f"`_base_compile` targets missing from EMEDF: {sorted(set(missing))}"


def test_define_label_partials_exist():
    """`DefineLabel` compiles to `DefineLabel_{0-9}`; all ten must exist."""
    for i in range(10):
        assert f"DefineLabel_{i}" in EMEDF_ALIASES, f"Missing `DefineLabel_{i}` in EMEDF."


def test_custom_compiler_base_compile_kwargs_are_valid():
    """Keyword arguments passed by custom wrappers must exist in the target instruction's EVS signature."""
    import soulstruct.bloodborne.events.emevd.compiler as compiler_module

    tree = ast.parse(Path(compiler_module.__file__).read_text(encoding="utf-8"))
    bad = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        if not (isinstance(func, ast.Attribute) and func.attr == "_base_compile"):
            continue
        if not node.args or not isinstance(node.args[0], ast.Constant):
            continue
        target = node.args[0].value
        if target not in EMEDF_ALIASES:
            continue  # reported by another test
        signature = set(_emedf_evs_signature(target))
        for keyword in node.keywords:
            if keyword.arg is None:
                continue  # `**kwargs` expansion; cannot check statically
            if keyword.arg not in signature:
                bad.append(f"{target}: unexpected kwarg '{keyword.arg}' (valid: {sorted(signature)})")
    assert not bad, bad


# ---------------------------------------------------------------------------
# `instructions.pyi` <-> EMEDF
# ---------------------------------------------------------------------------


def test_every_emedf_alias_has_a_pyi_def(pyi_defs):
    """Every alias/partial must be exposed in the stub, or IDE users cannot see it."""
    custom = EVSInstructionCompiler._CUSTOM_FUNC_NAMES
    missing = [alias for alias in EMEDF_ALIASES if alias not in pyi_defs and alias not in custom]
    assert not missing, f"EMEDF aliases missing a `def` in `instructions.pyi`: {missing}"


def test_pyi_defs_all_resolve(pyi_defs):
    """Every `def` in the stub must be an EMEDF alias, a boolean test, or a known EVS basic."""
    resolvable = (
        set(EMEDF_ALIASES)
        | set(EVSInstructionCompiler._CUSTOM_FUNC_NAMES)
        | set(EMEDF_TESTS)
        | set(EMEDF_COMPARISON_TESTS)
        | _PYI_BASICS
    )
    unknown = sorted(set(pyi_defs) - resolvable)
    assert not unknown, f"`instructions.pyi` defines unresolvable names: {unknown}"


def test_pyi_signatures_match_emedf(pyi_defs):
    """THE key check: stub argument names and order must equal the compiler's EVS signature."""
    mismatches = []
    for alias in EMEDF_ALIASES:
        if alias in EVSInstructionCompiler._CUSTOM_FUNC_NAMES:
            continue  # real Python function; its own signature is authoritative
        if alias not in pyi_defs:
            continue  # reported by `test_every_emedf_alias_has_a_pyi_def`
        expected = _emedf_evs_signature(alias)
        actual = _def_arg_names(pyi_defs[alias])
        if expected != actual:
            mismatches.append((alias, expected, actual))
    assert not mismatches, f"PYI/EMEDF signature mismatches: {mismatches}"


def test_pyi_test_signatures_match_emedf(pyi_defs):
    """Boolean test stubs (e.g. `FlagEnabled`) must drop only the control args from their `If` instruction."""
    control_args = {"condition", "line_count", "label"}
    mismatches = []
    for test_name, info in EMEDF_TESTS.items():
        if test_name not in pyi_defs:
            continue
        if_instr = info["if"]
        if if_instr in EVSInstructionCompiler._CUSTOM_FUNC_NAMES:
            expected = [
                p for p in list(inspect.signature(getattr(EVSInstructionCompiler, if_instr)).parameters)[1:]
                if p not in control_args
            ]
        else:
            expected = [a for a in _emedf_evs_signature(if_instr) if a not in control_args]
        actual = _def_arg_names(pyi_defs[test_name])
        if expected != actual:
            mismatches.append((test_name, if_instr, expected, actual))
    assert not mismatches, f"PYI test signature mismatches: {mismatches}"


@pytest.mark.xfail(
    reason="`instructions.pyi.__all__` still lists the pre-refactor custom instruction function names "
           "(and `compile_game_object_test`), but `compiler.__all__` now only exports `EVSInstructionCompiler`, "
           "so these names resolve to nothing for IDEs. The PYI generator reads `compiler_module.__all__`.",
    strict=False,
)
def test_pyi_all_entries_are_defined(pyi_all, pyi_defs):
    """`__all__` names must actually exist in the stub or be importable from its star-imports.

    The stub does `from .emevd.compiler import *`, but that module's `__all__` only exports the
    `EVSInstructionCompiler` class -- so custom instruction names listed in `__all__` resolve to nothing.
    """
    import soulstruct.bloodborne.events.emevd.compiler as compiler_module
    import soulstruct.bloodborne.events.enums as enums_module
    import soulstruct.bloodborne.game_types as game_types_module

    pyi_path = Path(compiler_module.__file__).parent.parent / "instructions.pyi"
    tree = ast.parse(pyi_path.read_text(encoding="utf-8"))
    defined = set(pyi_defs)
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            defined.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    defined.add(target.id)

    star_exported = set()
    for module in (compiler_module, enums_module, game_types_module):
        star_exported |= set(getattr(module, "__all__", ()) or dir(module))

    unresolved = sorted(n for n in pyi_all if n not in defined and n not in star_exported)
    assert not unresolved, (
        f"`instructions.pyi.__all__` exports names that are neither defined nor star-imported: {unresolved}"
    )


@pytest.mark.xfail(
    reason="'RunEvent' appears twice in `instructions.pyi.__all__`: once in the hard-coded BASICS list and "
           "again in the 'Custom instructions from `compiler`' block.",
    strict=False,
)
def test_pyi_all_has_no_duplicates(pyi_all):
    duplicates = sorted({name for name in pyi_all if pyi_all.count(name) > 1})
    assert not duplicates, f"Duplicate names in `instructions.pyi.__all__`: {duplicates}"


# ---------------------------------------------------------------------------
# Parser wiring
# ---------------------------------------------------------------------------


def test_evs_parser_condition_slots():
    """Bloodborne has 15 AND and 15 OR condition group slots, mirrored around MAIN (0)."""
    assert EVSParser.AND_SLOTS == list(range(1, 16))
    assert EVSParser.OR_SLOTS == [-i for i in range(1, 16)]
    assert EVSParser.COMPILER_CLASS is EVSInstructionCompiler
    assert EVSParser.EMEDF_ALIASES is EMEDF_ALIASES


def test_condition_group_enum_matches_parser_slots():
    from soulstruct.bloodborne.events.enums import ConditionGroup

    values = {group.value for group in ConditionGroup}
    assert values == set(EVSParser.AND_SLOTS) | set(EVSParser.OR_SLOTS) | {0}
