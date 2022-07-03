"""Contains additional custom instructions (by me) that wrap other real EMEVD instructions.

Though you may "call" these functions in EVS script, they are never actually called directly. The three dictionaries
defined at the top of the module (filled by decorators at module load) will be used to look up the functions. When
compiling EVS, the dictionary will be reversed and the EVS instruction name will be used to look up a custom instruction
from this module or the (category, index) for EMEDF. When decompiling to EVS,

Usually, these just combine multiple underlying EMEVD instructions into one (e.g., `IfActionButton`).
"""
__all__ = [
    "COMPILER",
    "compile_instruction",
    "compile_game_object_test",

    "RunEvent",
    "EnableObjectActivation",
    "DisableObjectActivation",
    "AwardItemLot",
    "PlayCutscene",
    "Move",
    "IfPlayerItemState",
    "IfPlayerHasItem",
    "IfPlayerHasWeapon",
    "IfPlayerHasArmor",
    "IfPlayerHasRune",
    "IfPlayerHasGood",
    "IfPlayerDoesNotHaveItem",
    "IfPlayerDoesNotHaveWeapon",
    "IfPlayerDoesNotHaveArmor",
    "IfPlayerDoesNotHaveRune",
    "IfPlayerDoesNotHaveGood",
    "IfActionButton",
    "DefineLabel",
]

import logging
import typing as tp

from soulstruct.base.events.emevd.compiler import base_compile_instruction, BooleanTestCompiler
from soulstruct.bloodborne.game_types import *
from soulstruct.darksouls1ptde.events.emevd.compiler import (
    EnableObjectActivation,
    DisableObjectActivation,
    AwardItemLot,
    PlayCutscene,
    Move,
    IfPlayerItemState,
    IfPlayerHasItem,
    IfPlayerHasWeapon,
    IfPlayerHasArmor,
    IfPlayerHasGood,
    IfPlayerDoesNotHaveItem,
    IfPlayerDoesNotHaveWeapon,
    IfPlayerDoesNotHaveArmor,
    IfPlayerDoesNotHaveGood,
    IfActionButton,
)

from .emedf import EMEDF_ALIASES
from .enums import *

_LOGGER = logging.getLogger(__name__)


# This dictionary maps EVS instruction function names to functions that produce actual numeric output. These functions
# may take different arguments to a single underlying instruction (e.g., tuples as flag ranges, `GameMap` instances) or
# merge multiple underlying instructions into one interface for simplicity, such as `IfActionButton` or `PlayCutscene`.
# If a function name does not appear in here, it will found as an 'alias' in EMEDF and compiled automatically.
# (Such functions should still appear in the PYI module for intelli-sense.)
COMPILER = {}


def compile_instruction(instr_name: str, *args, **kwargs) -> list[str]:
    """Compile instruction using `COMPILER` function if available, or fall back to `_auto_compile` below with EMEDF."""
    if instr_name in COMPILER:
        return COMPILER[instr_name](*args, **kwargs)
    return base_compile_instruction(EMEDF_ALIASES, instr_name, *args, **kwargs)


def compile_game_object_test(
    game_object_type: tp.Type[BaseGameObject],
    game_object: tp.Union[BaseGameObject, tuple],
    negate=False,
    condition: int = None,
    skip_lines=0,
    end_event=False,
    restart_event=False,
) -> list[str]:
    test = BooleanTestCompiler(compile_instruction)

    if issubclass(game_object_type, Flag):
        test.set_all("FlagEnabled", "FlagDisabled")
    elif issubclass(game_object_type, RegionVolume):
        test.if_true = "IfPlayerInsideRegion"
        test.if_false = "IfPlayerOutsideRegion"
    elif issubclass(game_object_type, Region):
        raise TypeError(f"Only `RegionVolume` subclasses can be used as direct booleans, not just `Region`.")
    elif issubclass(game_object_type, Object):
        test.set_all("ObjectNotDestroyed", "ObjectDestroyed")  # True == object NOT destroyed
    elif issubclass(game_object_type, Character):
        test.if_true = "IfCharacterAlive"
        test.if_false = "IfCharacterDead"
    elif issubclass(game_object_type, ObjActEvent):
        test.if_true = "IfObjectActivated"
    else:
        raise TypeError(f"Type `{game_object_type.__name__}` cannot be used as a boolean directly in EVS script.")

    return test.compile_object(
        game_object,
        negate=negate,
        condition=condition,
        skip_lines=skip_lines,
        end_event=end_event,
        restart_event=restart_event,
    )


def _compile(func):
    """Decorator that simply adds the decorated function to the `COMPILER` dictionary under its own name."""
    if func.__name__ in COMPILER:
        raise ValueError(f"EVS instruction {func.__name__} appeared more than once in module.")
    COMPILER[func.__name__] = func
    return func  # no actual decoration


# noinspection PyUnusedLocal
@_compile
def RunEvent(event_id, slot=0, args=(0,), arg_types="", event_layers=None):
    """Run the given `event_id`, which must be defined in the same script.

    You can omit `arg_types` if all the arguments are unsigned integers (which is usually the case).

    Note that you can also call the name of the event directly and pass in the given arguments normally.

    Note that `event_layers` is supported as an argument here for intellisense purposes, as this is the instruction
    it will most commonly be used with, but it can be used with any instruction. The EVS parser handles this keyword
    argument separately, so it will never actually be passed to an instruction function like this one.
    """
    if not arg_types:
        # Assume all signed integers, unless the only argument is zero.
        arg_types = "I" if args == (0,) else "i" * len(args)
    if len(args) != len(arg_types):
        raise ValueError("Number of event arguments does not match length of argument type string in RunEvent.")
    full_arg_types = "iI" + str(arg_types[0])
    if len(arg_types) > 1:
        full_arg_types += f"|{arg_types[1:]}"
    return base_compile_instruction(
        EMEDF_ALIASES, "RunEvent", slot=slot, event_id=event_id, args=args, arg_types=full_arg_types
    )


# Add PTDE imported functions to `COMPILER`.
_compile(EnableObjectActivation)
_compile(DisableObjectActivation)
_compile(AwardItemLot)
_compile(PlayCutscene)
_compile(Move)
_compile(IfPlayerItemState)
_compile(IfPlayerHasItem)
_compile(IfPlayerHasWeapon)
_compile(IfPlayerHasArmor)


@_compile
def IfPlayerHasRune(condition: int, rune: AccessoryTyping, including_storage: bool = False):
    return IfPlayerItemState(condition, True, rune, ItemType.Rune, including_storage)


_compile(IfPlayerHasGood)
_compile(IfPlayerDoesNotHaveItem)
_compile(IfPlayerDoesNotHaveWeapon)
_compile(IfPlayerDoesNotHaveArmor)


@_compile
def IfPlayerDoesNotHaveRune(condition: int, rune: AccessoryTyping, including_storage: bool = False):
    return IfPlayerItemState(condition, False, rune, ItemType.Rune, including_storage)


_compile(IfPlayerDoesNotHaveGood)
_compile(IfActionButton)


@_compile
def DefineLabel(label: Label | int):
    """Wrapper for generating any valid label (0-9, inclusive)."""
    if not 0 <= label <= 9:
        raise ValueError(f"Label for `DefineLabel` must be between 0 and 9, inclusive, not: {label}")
    return base_compile_instruction(EMEDF_ALIASES, f"DefineLabel_{int(label)}")
