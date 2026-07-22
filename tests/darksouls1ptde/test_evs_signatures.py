"""Pure-unit cross-checks between the DS1 PTDE EVS instruction wrappers and `emevd/emedf.py`.

The `EVSInstructionCompiler` custom methods (`events/emevd/compiler.py`) are hand-written wrappers
that delegate to real EMEVD instructions via `self._base_compile("<EMEDF alias>", **kwargs)`. If an
alias is renamed or an argument name changes in `emedf.py`, nothing catches it until a user's EVS
script blows up (or, worse, silently compiles wrong). These tests catch that statically (via AST)
*and* dynamically (by actually invoking every wrapper).

Everything here runs without any game data.
"""
from __future__ import annotations

import ast
import inspect
import textwrap
from collections import Counter

import pytest

from soulstruct.base.events.evs.conditions import EVSConditionManager
from soulstruct.darksouls1ptde.events.emevd.compiler import EVSInstructionCompiler
from soulstruct.darksouls1ptde.events.emevd.emedf import (
    EMEDF,
    EMEDF_ALIASES,
    EMEDF_TESTS,
    EMEDF_COMPARISON_TESTS,
)
from soulstruct.darksouls1ptde.events.emevd.evs import EVSParser
from soulstruct.darksouls1ptde.events.enums import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.maps.constants import DEPTHS


# Custom compiler methods that deliberately shadow a real EMEDF alias (these take priority in
# `EVSInstructionCompiler.compile()`, so any *unintentional* shadow is a silent behaviour change).
KNOWN_ALIAS_SHADOWS = {"RunEvent"}


@pytest.fixture(scope="module")
def compiler() -> EVSInstructionCompiler:
    cond_manager = EVSConditionManager(EVSParser.OR_SLOTS, EVSParser.AND_SLOTS)
    cond_manager.reset(11000000)
    return EVSInstructionCompiler(cond_manager)


def _base_compile_calls():
    """Yield `(method_name, instr_name, explicit_kwarg_names, has_star_kwargs)` for every literal
    `self._base_compile("Name", ...)` call in the PTDE compiler module."""
    source = textwrap.dedent(inspect.getsource(EVSInstructionCompiler))
    class_node = ast.parse(source).body[0]
    for method in class_node.body:
        if not isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for node in ast.walk(method):
            if not isinstance(node, ast.Call):
                continue
            func = node.func
            if not (isinstance(func, ast.Attribute) and func.attr == "_base_compile"):
                continue
            if not node.args or not isinstance(node.args[0], ast.Constant):
                continue  # dynamic instruction name; can't check statically
            kwarg_names = [kw.arg for kw in node.keywords if kw.arg is not None]
            has_star = any(kw.arg is None for kw in node.keywords)
            yield method.name, node.args[0].value, kwarg_names, has_star


# ---------------------------------------------------------------------------
# EMEDF table integrity
# ---------------------------------------------------------------------------


def test_emedf_alias_and_partial_names_are_unique():
    """`build_emedf_aliases_tests` writes aliases and partials into one flat dict; a collision would
    silently make one instruction unreachable."""
    names = []
    for info in EMEDF.values():
        names.append(info["alias"])
        names.extend(info.get("partials", {}))
    duplicates = {name: count for name, count in Counter(names).items() if count > 1}
    assert not duplicates, f"Duplicate EMEDF alias/partial names: {duplicates}"


def test_emedf_aliases_contains_every_alias_and_partial():
    for (category, index), info in EMEDF.items():
        assert info["alias"] in EMEDF_ALIASES, f"Alias missing from EMEDF_ALIASES: {info['alias']}"
        assert EMEDF_ALIASES[info["alias"]][:2] == (category, index)
        for partial_name in info.get("partials", {}):
            assert partial_name in EMEDF_ALIASES
            assert EMEDF_ALIASES[partial_name][:2] == (category, index)


def test_emedf_alias_names_are_valid_identifiers():
    for name in EMEDF_ALIASES:
        assert name.isidentifier(), f"EMEDF alias is not a valid Python identifier: {name!r}"


def test_emedf_entries_have_required_keys():
    for (category, index), info in EMEDF.items():
        assert "alias" in info, f"({category}, {index}) has no 'alias'."
        assert "args" in info, f"({category}, {index}) has no 'args'."
        for arg_name, arg_info in info["args"].items():
            assert arg_name.isidentifier(), f"({category}, {index}) arg name invalid: {arg_name!r}"
            assert "type" in arg_info, f"({category}, {index}) arg '{arg_name}' has no 'type'."
            assert "default" in arg_info, f"({category}, {index}) arg '{arg_name}' has no 'default'."
            assert "internal_type" in arg_info, (
                f"({category}, {index}) arg '{arg_name}' has no 'internal_type' "
                f"(should come from `ds1-common.emedf.json`)."
            )


def test_emedf_partial_kwargs_are_real_args():
    for (category, index), info in EMEDF.items():
        arg_names = set(info.get("evs_args", info["args"]))
        for partial_name, partial_kwargs in info.get("partials", {}).items():
            # `__`-prefixed keys (e.g. `__docstring`) are documentation pseudo-kwargs, not real args.
            unknown = {k for k in partial_kwargs if not k.startswith("__")} - arg_names
            assert not unknown, (
                f"Partial '{partial_name}' of ({category}, {index}) bakes unknown arg(s) {unknown}; "
                f"valid args: {sorted(arg_names)}"
            )


def test_emedf_evs_args_are_subset_or_superset_of_args():
    """`evs_args`, when present, must reuse the same arg names or supply its own info dicts."""
    for (category, index), info in EMEDF.items():
        evs_args = info.get("evs_args")
        if evs_args is None:
            continue
        for arg_name, arg_info in evs_args.items():
            if not arg_info:  # empty dict -> falls back to `args[arg_name]`
                assert arg_name in info["args"], (
                    f"({category}, {index}) `evs_args` entry '{arg_name}' is empty but has no "
                    f"matching entry in `args`."
                )


def test_emedf_arg_types_format_string_is_well_formed():
    from soulstruct.base.events.emevd.emedf import ArgType

    for (category, index), info in EMEDF.items():
        fmt = "".join(arg["internal_type"].get_fmt() for arg in info["args"].values())
        assert all(c in "BbHhIifs" for c in fmt), f"({category}, {index}) bad fmt: {fmt}"
        for arg in info["args"].values():
            assert isinstance(arg["internal_type"], ArgType)


def test_emedf_tests_reference_known_instructions():
    known = set(EMEDF_ALIASES) | set(EVSInstructionCompiler._CUSTOM_FUNC_NAMES)
    for test_name, test_info in EMEDF_TESTS.items():
        assert test_info.get("if"), f"EMEDF test '{test_name}' has no 'if' instruction."
        for key, instr_name in test_info.items():
            assert instr_name in known, (
                f"EMEDF test '{test_name}' key '{key}' refers to unknown instruction '{instr_name}'."
            )


def test_emedf_comparison_tests_reference_known_instructions():
    for test_name, info in EMEDF_COMPARISON_TESTS.items():
        assert "test_name" in info and "return_type" in info
        assert f"If{info['test_name']}" in EMEDF_ALIASES, (
            f"Comparison test '{test_name}' -> unknown instruction 'If{info['test_name']}'."
        )


# ---------------------------------------------------------------------------
# Static cross-check: compiler wrappers vs EMEDF
# ---------------------------------------------------------------------------


def test_base_compile_calls_found():
    """Sanity check that the AST scan actually found the wrapper calls (guards against silent skips)."""
    calls = list(_base_compile_calls())
    assert len(calls) >= 15, f"Expected many `_base_compile` calls in PTDE compiler; found {len(calls)}."


@pytest.mark.parametrize(
    "method_name,instr_name,kwarg_names,has_star",
    list(_base_compile_calls()),
    ids=lambda v: v if isinstance(v, str) else "",
)
def test_base_compile_target_exists_and_kwargs_match(method_name, instr_name, kwarg_names, has_star):
    assert instr_name in EMEDF_ALIASES, (
        f"`{method_name}` calls `_base_compile('{instr_name}')` but that alias is not in EMEDF."
    )
    category, index, info = EMEDF_ALIASES[instr_name]
    evs_args = info.get("evs_args", info["args"])
    baked = set(info.get("partials", {}).get(instr_name, {}))
    valid = set(evs_args) - baked

    unknown = set(kwarg_names) - valid
    assert not unknown, (
        f"`{method_name}` passes unknown keyword(s) {sorted(unknown)} to '{instr_name}' "
        f"({category}, {index}). Valid EVS args: {sorted(valid)}"
    )
    assert len(kwarg_names) == len(set(kwarg_names)), f"Duplicate kwargs in `{method_name}`."

    if not has_star:
        # All non-defaultable arguments must be supplied explicitly.
        required = {
            name for name in valid
            if evs_args[name].get("default", evs_args.get(name) and None) is None
            and (evs_args[name] or info["args"][name])["default"] is None
        }
        missing = required - set(kwarg_names)
        assert not missing, (
            f"`{method_name}` -> '{instr_name}' is missing required arg(s) {sorted(missing)}."
        )


def test_custom_compiler_methods_do_not_shadow_emedf_aliases():
    shadows = {
        name for name in EVSInstructionCompiler._CUSTOM_FUNC_NAMES if name in EMEDF_ALIASES
    } - KNOWN_ALIAS_SHADOWS
    assert not shadows, (
        f"Custom compiler method(s) {sorted(shadows)} shadow real EMEDF aliases and will take "
        f"priority in `EVSInstructionCompiler.compile()`. Rename them or add to KNOWN_ALIAS_SHADOWS."
    )


def test_custom_func_condition_arg_indices_are_correct():
    """`_CUSTOM_FUNC_CONDITION_ARGS` drives condition-group tracking; verify it against signatures."""
    for method_name, (out_index, in_index) in EVSInstructionCompiler._CUSTOM_FUNC_CONDITION_ARGS.items():
        method = getattr(EVSInstructionCompiler, method_name)
        params = list(inspect.signature(method).parameters)[1:]  # drop `self`
        expected_out = params.index("condition") if "condition" in params else None
        expected_in = params.index("input_condition") if "input_condition" in params else None
        assert out_index == expected_out, f"{method_name}: bad output condition index."
        assert in_index == expected_in, f"{method_name}: bad input condition index."


def test_every_if_prefixed_custom_method_takes_condition_first():
    """EVS convention: `If*` instructions take the output condition group as their first argument."""
    for method_name in sorted(EVSInstructionCompiler._CUSTOM_FUNC_NAMES):
        if not method_name.startswith("If"):
            continue
        params = list(inspect.signature(getattr(EVSInstructionCompiler, method_name)).parameters)[1:]
        assert params and params[0] == "condition", (
            f"`{method_name}` should take `condition` as its first argument, got {params[:1]}."
        )


# ---------------------------------------------------------------------------
# Dynamic cross-check: actually invoke every wrapper
# ---------------------------------------------------------------------------


def _assert_instruction(lines, expected_alias: str):
    """Assert the compiled numeric output targets the EMEDF instruction named `expected_alias`.

    The expected `(category, index)` is looked up from EMEDF itself, so these tests pin the
    *wrapper -> alias* mapping (the thing that silently breaks) rather than hard-coded IDs.
    """
    assert expected_alias in EMEDF_ALIASES, f"Unknown EMEDF alias used in test: {expected_alias}"
    category, index, _ = EMEDF_ALIASES[expected_alias]
    assert isinstance(lines, list) and lines, "Compiler must return a non-empty list of strings."
    head = lines[0]
    assert head.strip().startswith(f"{category}["), (
        f"Expected `{expected_alias}` category {category}, got: {head!r}"
    )
    assert f"[{index:02d}]" in head, f"Expected `{expected_alias}` index {index}, got: {head!r}"


def test_enable_disable_object_activation(compiler):
    _assert_instruction(compiler.EnableObjectActivation(1001000, 1), "SetObjectActivation")
    _assert_instruction(
        compiler.EnableObjectActivation(1001000, 1, relative_index=2), "SetObjectActivationWithIdx"
    )
    _assert_instruction(compiler.DisableObjectActivation(1001000, 1), "SetObjectActivation")
    _assert_instruction(
        compiler.DisableObjectActivation(1001000, 1, relative_index=2), "SetObjectActivationWithIdx"
    )
    # State bit must differ between the enable/disable variants.
    assert compiler.EnableObjectActivation(1001000, 1) != compiler.DisableObjectActivation(1001000, 1)


def test_award_item_lot(compiler):
    _assert_instruction(compiler.AwardItemLot(50), "AwardItemLotToHostOnly")
    _assert_instruction(compiler.AwardItemLot(50, host_only=False), "AwardItemLotToAllPlayers")


def test_play_cutscene_variants(compiler):
    _assert_instruction(compiler.PlayCutscene(120000), "PlayCutsceneToPlayer")
    _assert_instruction(compiler.PlayCutscene(120000, player_id=10001), "PlayCutsceneToPlayer")
    _assert_instruction(
        compiler.PlayCutscene(120000, game_map=DEPTHS, move_to_region=1002000),
        "PlayCutsceneAndMovePlayer",
    )
    _assert_instruction(
        compiler.PlayCutscene(120000, game_map=DEPTHS, move_to_region=1002000, player_id=10001),
        "PlayCutsceneAndMoveSpecificPlayer",
    )
    _assert_instruction(compiler.PlayCutscene(120000, rotation=90), "PlayCutsceneAndRotatePlayer")


def test_play_cutscene_argument_validation(compiler):
    with pytest.raises(ValueError):
        compiler.PlayCutscene(120000, game_map=DEPTHS)  # no `move_to_region`
    with pytest.raises(ValueError):
        compiler.PlayCutscene(120000, move_to_region=1002000)  # no `game_map`
    with pytest.raises(ValueError):
        compiler.PlayCutscene(120000, game_map=DEPTHS, move_to_region=1002000, rotation=90)


def test_move_variants(compiler):
    _assert_instruction(
        compiler.Move(1000000, 1002000, destination_type=CoordEntityType.Region), "MoveToEntity"
    )
    _assert_instruction(
        compiler.Move(1000000, 1002000, destination_type=CoordEntityType.Region, short_move=True),
        "ShortMove",
    )
    _assert_instruction(
        compiler.Move(
            1000000, 1002000, destination_type=CoordEntityType.Region, copy_draw_parent=1003200
        ),
        "MoveAndCopyDrawParent",
    )
    _assert_instruction(
        compiler.Move(
            1000000, 1002000, destination_type=CoordEntityType.Region, set_draw_parent=1003200
        ),
        "MoveAndSetDrawParent",
    )


def test_move_argument_validation(compiler):
    with pytest.raises(ValueError):
        compiler.Move(
            1000000, 1002000, destination_type=CoordEntityType.Region,
            copy_draw_parent=1, set_draw_parent=2,
        )
    with pytest.raises(ValueError):
        compiler.Move(
            1000000, 1002000, destination_type=CoordEntityType.Region,
            short_move=True, set_draw_parent=2,
        )
    with pytest.raises(AttributeError):
        compiler.Move(1000000, 1002000)  # untyped destination, no `destination_type`


def test_move_detects_player_destination(compiler):
    lines = compiler.Move(1000000, PLAYER)
    _assert_instruction(lines, "MoveToEntity")
    assert str(int(CoordEntityType.Character)) in lines[0]


def test_if_player_item_state_partials(compiler):
    including = compiler.IfPlayerItemState(1, True, 100000, ItemType.Weapon, including_storage=True)
    excluding = compiler.IfPlayerItemState(1, True, 100000, ItemType.Weapon, including_storage=False)
    _assert_instruction(including, "IfPlayerItemStateIncludingStorage")
    _assert_instruction(excluding, "IfPlayerItemStateExcludingStorage")
    assert compiler.IfPlayerHasWeapon(1, 100000) == excluding
    assert compiler.IfPlayerDoesNotHaveWeapon(1, 100000) != excluding
    for method in (compiler.IfPlayerHasArmor, compiler.IfPlayerHasRing, compiler.IfPlayerHasGood):
        _assert_instruction(method(1, 1000), "IfPlayerItemStateExcludingStorage")


def test_if_player_item_state_requires_detectable_item_type(compiler):
    with pytest.raises(AttributeError):
        compiler.IfPlayerItemState(1, True, 100000)  # plain int -> no `get_item_enum`


def test_if_action_button_variants(compiler):
    kwargs = dict(condition=1, prompt_text=10, anchor_entity=1001000, anchor_type=CoordEntityType.Object)
    _assert_instruction(compiler.IfActionButton(**kwargs), "IfActionButtonBasic")
    _assert_instruction(compiler.IfActionButton(**kwargs, boss_version=True), "IfActionButtonBoss")
    _assert_instruction(
        compiler.IfActionButton(**kwargs, line_intersects=1003200),
        "IfActionButtonBasicLineIntersect",
    )
    _assert_instruction(
        compiler.IfActionButton(**kwargs, boss_version=True, line_intersects=1003200),
        "IfActionButtonBossLineIntersect",
    )


def test_if_action_button_requires_anchor_type(compiler):
    with pytest.raises(ValueError):
        compiler.IfActionButton(condition=1, prompt_text=10, anchor_entity=1001000)


def test_run_event_arg_types(compiler):
    """`RunEvent` builds its own `arg_types` string; check the 'iI<first>|<rest>' convention."""
    no_args = compiler.RunEvent(11000000)
    assert "(iII)" in no_args[0]
    two_args = compiler.RunEvent(11000000, slot=1, args=(1000, 2000))
    assert "(iIi|i)" in two_args[0], two_args[0]
    with pytest.raises(ValueError):
        compiler.RunEvent(11000000, args=(1, 2), arg_types="i")


@pytest.mark.parametrize(
    "instr_name",
    sorted(name for name in EMEDF_ALIASES if name.startswith(("Enable", "Disable"))),
)
def test_enable_disable_partials_differ(instr_name):
    """Every `Enable*` partial should have a `Disable*` sibling on the same instruction (and vice versa)."""
    category, index, info = EMEDF_ALIASES[instr_name]
    partials = info.get("partials", {})
    if instr_name not in partials:
        pytest.skip(f"'{instr_name}' is a base alias, not a partial.")
    sibling = (
        instr_name.replace("Enable", "Disable", 1) if instr_name.startswith("Enable")
        else instr_name.replace("Disable", "Enable", 1)
    )
    assert sibling in partials, f"'{instr_name}' has no '{sibling}' sibling on ({category}, {index})."
