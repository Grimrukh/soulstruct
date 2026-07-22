"""Cross-check the DS3 EVS instruction surface against `emedf.py`.

Pure-unit tests: no game data required.

Three sources define the DS3 EVS "API":
  1. `darksouls3/events/emevd/emedf.py` -> `EMEDF` (raw `(category, index)` info) and `EMEDF_ALIASES`
     (alias name -> `(category, index, info)`, including "partial" aliases with baked kwargs).
  2. `darksouls3/events/emevd/compiler.py` -> `EVSInstructionCompiler`, whose capitalised methods are
     custom instructions that wrap one or more real EMEVD instructions.
  3. `darksouls3/events/instructions.pyi` -> the AUTOMATICALLY GENERATED intellisense stub that EVS
     script authors import. This must stay in sync with (1) and (2).

`darksouls3/events/__init__.py` re-exports the map constants and enums that EVS scripts also need,
so its `__all__` is checked against `maps/constants.py` and `events/enums.py` too.
"""
from __future__ import annotations

import ast
import inspect
from pathlib import Path

import pytest

import soulstruct.darksouls3.events as ds3_events
from soulstruct.darksouls3.events.emevd.compiler import EVSInstructionCompiler
from soulstruct.darksouls3.events.emevd.emedf import (
    EMEDF,
    EMEDF_ALIASES,
    EMEDF_TESTS,
    EMEDF_COMPARISON_TESTS,
)

PYI_PATH = Path(inspect.getfile(ds3_events)).parent / "instructions.pyi"

# Names the PYI generator injects that are not EMEDF instructions.
_PYI_BASICS = {
    "ContinueOnRest", "RestartOnRest", "EndOnRest", "LastResult", "Await",
    "enable_debug", "disable_debug", "EVENTS", "Condition", "HeldCondition",
    "END", "RESTART", "MAIN", "compile_game_object_test",
}


def _parse_pyi() -> tuple[dict[str, ast.FunctionDef], list[str]]:
    tree = ast.parse(PYI_PATH.read_text(encoding="utf-8"))
    funcs = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    declared: list[str] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "__all__":
            declared = [elt.value for elt in node.value.elts]
    return funcs, declared


PYI_FUNCS, PYI_ALL = _parse_pyi()
CUSTOM_NAMES = set(EVSInstructionCompiler._CUSTOM_FUNC_NAMES)


def _pyi_arg_names(func: ast.FunctionDef) -> list[str]:
    args = func.args
    return [a.arg for a in (*args.posonlyargs, *args.args, *args.kwonlyargs)]


# ---------------------------------------------------------------------------
# EMEDF internal consistency
# ---------------------------------------------------------------------------


def test_pyi_file_exists_and_parses():
    assert PYI_PATH.is_file(), PYI_PATH
    assert len(PYI_FUNCS) > 500
    assert len(PYI_ALL) > 500


def test_emedf_aliases_all_resolve_to_emedf_entries():
    bad = [name for name, (cat, idx, _) in EMEDF_ALIASES.items() if (cat, idx) not in EMEDF]
    assert not bad, f"EMEDF_ALIASES entries with no matching EMEDF `(category, index)`: {bad}"


def test_emedf_entry_aliases_are_registered():
    """Each EMEDF entry's `alias` (and every `partials` key) must appear in `EMEDF_ALIASES`."""
    missing = []
    for (cat, idx), info in EMEDF.items():
        if info["alias"] not in EMEDF_ALIASES:
            missing.append((cat, idx, info["alias"]))
        for partial_name in info.get("partials", {}):
            if partial_name not in EMEDF_ALIASES:
                missing.append((cat, idx, partial_name))
    assert not missing, f"EMEDF aliases missing from EMEDF_ALIASES: {missing}"


def test_emedf_arg_info_is_well_formed():
    """Every EMEDF arg must declare `type` and `default` keys (used by the compiler and PYI generator)."""
    bad = []
    for (cat, idx), info in EMEDF.items():
        for arg_name, arg_info in info["args"].items():
            if "type" not in arg_info or "default" not in arg_info:
                bad.append((cat, idx, arg_name, sorted(arg_info)))
            if "internal_type" not in arg_info:
                bad.append((cat, idx, arg_name, "no internal_type"))
    assert not bad, f"Malformed EMEDF arg info: {bad[:20]}"


def test_emedf_partial_kwargs_name_real_args():
    """A partial's baked kwargs must be real argument names of the parent instruction."""
    bad = []
    for (cat, idx), info in EMEDF.items():
        arg_names = set(info["args"])
        for partial_name, baked in info.get("partials", {}).items():
            for kwarg in baked:
                if kwarg == "__docstring":
                    continue  # special key consumed by the PYI generator
                if kwarg not in arg_names:
                    bad.append((cat, idx, partial_name, kwarg))
    assert not bad, f"Partial baked kwargs that are not EMEDF args: {bad}"


def test_emedf_tests_reference_known_instructions():
    """`EMEDF_TESTS`/`EMEDF_COMPARISON_TESTS` values must be real aliases or custom compiler methods."""
    known = set(EMEDF_ALIASES) | CUSTOM_NAMES
    bad = {}
    for test_name, test_info in EMEDF_TESTS.items():
        for kind, alias in test_info.items():
            if isinstance(alias, str) and alias not in known:
                bad.setdefault(test_name, []).append((kind, alias))
    for test_name, test_info in EMEDF_COMPARISON_TESTS.items():
        alias = test_info.get("if")
        if isinstance(alias, str) and alias not in known:
            bad.setdefault(test_name, []).append(("if", alias))
    assert not bad, f"Test aliases not found in EMEDF_ALIASES or compiler: {bad}"


def test_decompiler_keys_are_real_emedf_instructions():
    from soulstruct.darksouls3.events.emevd.decompiler import DECOMPILER, OPT_ARGS_DECOMPILER

    bad = [key for key in (*DECOMPILER, *OPT_ARGS_DECOMPILER) if key not in EMEDF]
    assert not bad, f"Decompiler functions registered for unknown instructions: {bad}"


def test_decompiler_signatures_match_emedf_arg_counts():
    """A manual decompiler function must accept exactly the EMEDF args of its instruction."""
    from soulstruct.darksouls3.events.emevd.decompiler import DECOMPILER

    mismatches = []
    for (cat, idx), func in DECOMPILER.items():
        emedf_args = list(EMEDF[cat, idx]["args"])
        params = [
            p for p in inspect.signature(func).parameters.values()
            if p.kind not in (p.VAR_POSITIONAL, p.VAR_KEYWORD) and p.name != "enums_manager"
        ]
        if len(params) != len(emedf_args):
            mismatches.append((cat, idx, func.__name__, [p.name for p in params], emedf_args))
    assert not mismatches, f"Decompiler/EMEDF arg count mismatches: {mismatches}"


# ---------------------------------------------------------------------------
# EMEDF <-> generated PYI stub
# ---------------------------------------------------------------------------


def test_every_emedf_alias_has_a_pyi_stub():
    missing = sorted(name for name in EMEDF_ALIASES if name not in PYI_FUNCS)
    assert not missing, f"EMEDF aliases with no `instructions.pyi` stub: {missing}"


def test_pyi_arg_names_match_emedf_arg_names():
    """The stub signature for each alias must list exactly the EVS args EMEDF expects (in order)."""
    mismatches = []
    for name, (cat, idx, info) in EMEDF_ALIASES.items():
        func = PYI_FUNCS.get(name)
        if func is None:
            continue  # covered by the test above
        evs_args = info.get("evs_args", info["args"])
        baked = info.get("partials", {}).get(name, {})
        expected = [arg for arg in evs_args if arg not in baked]
        actual = [a for a in _pyi_arg_names(func) if a != "event_layers"]
        if actual != expected:
            mismatches.append((name, actual, expected))
    assert not mismatches, f"`instructions.pyi` signature drift ({len(mismatches)}): {mismatches[:10]}"


def test_pyi_all_entries_are_defined_in_pyi():
    """The stub's `__all__` must not reference names the stub does not define.

    `instructions.pyi` also does `from .emevd.compiler import *`, but the DS3 compiler's `__all__`
    is just `["EVSInstructionCompiler"]`, so custom-instruction names cannot come from there either.
    """
    undefined = [
        name for name in PYI_ALL
        if name not in PYI_FUNCS
        and name not in _PYI_BASICS
        and not name.startswith(("OR_", "AND_"))
    ]
    if undefined:
        pytest.xfail(
            f"`darksouls3/events/instructions.pyi` `__all__` references {len(undefined)} names it does "
            f"not define (stale generator: `_generate_instructions_pyi.generate_instr_pyi` reads "
            f"`compiler_module.__all__`, which is now just the compiler CLASS): {undefined}"
        )


@pytest.mark.xfail(
    reason="`instructions.pyi` was generated before the compiler was refactored into "
           "`EVSInstructionCompiler`, so 18 custom instructions (Move, PlayCutscene, IfActionButton, "
           "AwardItemLot, DefineLabel, IfPlayerHas*, ...) have no stub.",
    strict=False,
)
def test_every_custom_compiler_instruction_has_a_pyi_stub():
    missing = sorted(name for name in CUSTOM_NAMES if name not in PYI_FUNCS)
    assert not missing, f"Custom compiler instructions with no `instructions.pyi` stub: {missing}"


def test_pyi_stubs_are_known_instructions():
    """No orphan stubs: every PYI function must be an EMEDF alias, a test, or a custom instruction."""
    known = set(EMEDF_ALIASES) | CUSTOM_NAMES | set(EMEDF_TESTS) | set(EMEDF_COMPARISON_TESTS)
    orphans = sorted(
        name for name in PYI_FUNCS
        if name not in known and name not in _PYI_BASICS and not name.startswith(("Enable", "Disable"))
    )
    assert not orphans, f"`instructions.pyi` defines unknown instructions: {orphans}"


def test_run_common_event_pyi_signature_matches_compiler():
    """The compiler's `RunCommonEvent` accepts `slot`; the stub and EMEDF must agree."""
    compiler_params = list(inspect.signature(EVSInstructionCompiler.RunCommonEvent).parameters)[1:]
    assert "slot" in compiler_params

    emedf_args = list(EMEDF[2000, 6]["args"])
    pyi_args = _pyi_arg_names(PYI_FUNCS["RunCommonEvent"])
    if "slot" not in emedf_args or "slot" not in pyi_args:
        pytest.xfail(
            f"DS3 `RunCommonEvent` (2000, 6) EMEDF args are {emedf_args} and stub args are {pyi_args}, "
            f"but `EVSInstructionCompiler.RunCommonEvent` takes {compiler_params} and forwards "
            f"`slot=` to `_base_compile` -- which always raises `ValueError`."
        )


# ---------------------------------------------------------------------------
# `darksouls3.events` package namespace
# ---------------------------------------------------------------------------


def test_events_package_all_is_fully_defined():
    missing = [name for name in ds3_events.__all__ if not hasattr(ds3_events, name)]
    assert not missing, f"`darksouls3.events.__all__` references undefined names: {missing}"


def test_events_package_exports_every_map_constant():
    from soulstruct.darksouls3.maps import constants as map_constants

    map_names = {
        name for name in map_constants.__all__
        if name.isupper() and name not in {"ALL_MAPS", "ALL_MSB_FILE_NAMES"}
    }
    missing = sorted(name for name in map_names if not hasattr(ds3_events, name))
    assert not missing, f"`darksouls3.events` does not export map constants: {missing}"


def test_events_package_exports_every_enum():
    from soulstruct.darksouls3.events import enums as ds3_enums

    missing = sorted(name for name in ds3_enums.__all__ if not hasattr(ds3_events, name))
    assert not missing, f"`darksouls3.events` does not re-export enums: {missing}"


def test_events_all_names_are_actually_importable_via_star():
    """`from soulstruct.darksouls3.events import *` must not raise."""
    namespace = {}
    exec("from soulstruct.darksouls3.events import *", namespace)
    for name in ds3_events.__all__:
        assert name in namespace, f"`import *` did not provide {name!r}."
