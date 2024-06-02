"""Contains additional custom instructions (by me) that wrap other real EMEVD instructions.

Though you may "call" these functions in EVS script, they are never actually called directly. The three dictionaries
defined at the top of the module (filled by decorators at module load) will be used to look up the functions. When
compiling EVS, the dictionary will be reversed and the EVS instruction name will be used to look up a custom instruction
from this module or the (category, index) for EMEDF. When decompiling to EVS,

Usually, these just combine multiple underlying EMEVD instructions into one (e.g., `IfActionButton`).
"""
from __future__ import annotations

__all__ = [
    "COMPILER",
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
    "IfPlayerHasRing",
    "IfPlayerHasGood",
    "IfPlayerDoesNotHaveItem",
    "IfPlayerDoesNotHaveWeapon",
    "IfPlayerDoesNotHaveArmor",
    "IfPlayerDoesNotHaveRing",
    "IfPlayerDoesNotHaveGood",
    "IfActionButton",
]

import logging

from soulstruct.base.events.evs.compiler import EVSInstructionCompiler
from soulstruct.darksouls1ptde.events.emevd.compiler import (
    compile_game_object_test,
    EnableObjectActivation,
    DisableObjectActivation,
    AwardItemLot,
    PlayCutscene,
    Move,
    IfPlayerItemState,
    IfPlayerHasItem,
    IfPlayerHasWeapon,
    IfPlayerHasArmor,
    IfPlayerHasRing,
    IfPlayerHasGood,
    IfPlayerDoesNotHaveItem,
    IfPlayerDoesNotHaveWeapon,
    IfPlayerDoesNotHaveArmor,
    IfPlayerDoesNotHaveRing,
    IfPlayerDoesNotHaveGood,
    IfActionButton,
)

from .emedf import EMEDF_ALIASES


_LOGGER = logging.getLogger("soulstruct")

COMPILER = EVSInstructionCompiler(EMEDF_ALIASES)


# noinspection PyUnusedLocal
@COMPILER.add_custom_instruction
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
    return COMPILER.compile(
        "_RunEvent", slot=slot, event_id=event_id, args=args, arg_types=full_arg_types
    )


# Add PTDE imported functions to `COMPILER`.
COMPILER.add_custom_instruction(EnableObjectActivation)
COMPILER.add_custom_instruction(DisableObjectActivation)
COMPILER.add_custom_instruction(AwardItemLot)
COMPILER.add_custom_instruction(PlayCutscene)
COMPILER.add_custom_instruction(Move)
COMPILER.add_custom_instruction(IfPlayerItemState)
COMPILER.add_custom_instruction(IfPlayerHasItem)
COMPILER.add_custom_instruction(IfPlayerHasWeapon)
COMPILER.add_custom_instruction(IfPlayerHasArmor)
COMPILER.add_custom_instruction(IfPlayerHasRing)
COMPILER.add_custom_instruction(IfPlayerHasGood)
COMPILER.add_custom_instruction(IfPlayerDoesNotHaveItem)
COMPILER.add_custom_instruction(IfPlayerDoesNotHaveWeapon)
COMPILER.add_custom_instruction(IfPlayerDoesNotHaveArmor)
COMPILER.add_custom_instruction(IfPlayerDoesNotHaveRing)
COMPILER.add_custom_instruction(IfPlayerDoesNotHaveGood)
COMPILER.add_custom_instruction(IfActionButton)
