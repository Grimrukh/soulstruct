from __future__ import annotations

__all__ = ["DECOMPILER", "OPT_ARGS_DECOMPILER", "decompile_instruction"]

import logging
import typing as tp

from soulstruct.base.events.evs.decompiler import (
    base_decompiler_instruction,
    assemble_arg_string,
    base_decompile_run_event,
    base_decompile_run_common_event,
)
from soulstruct.darksouls3.game_types.game_enums_manager import GameEnumsManager
from soulstruct.darksouls3.game_types.map_types import *
from soulstruct.darksouls3.maps.constants import get_map_variable_name

from .. import enums
from ..enums import *
from .emedf import EMEDF

_LOGGER = logging.getLogger("soulstruct")


# This dictionary maps IDs, i.e. `(category, index)` pairs, to functions that generate EVS text.
# Multiple instruction IDs may map to the same function, e.g., `IfActionButton`.
# These function values MUST support the EMEDF arguments of all instruction IDs that map to them.
# If an instruction ID does not appear in here, it will be decompiled automatically from its EMEDF information.
DECOMPILER = {}
# Alternate dictionary for instructions whose decompiling functions expect `*opt_args, arg_types, enums_manager` args,
# such as `RunEvent` (2000, 0).
OPT_ARGS_DECOMPILER = {}


def _decompile(category: int, index: int, uses_opt_args=False):
    """Generated decorator that adds the decorated function to the `DECOMPILER` dictionary under `(category, index)`.

    The decorated function will be called from `Instruction.to_evs()` with its EMEVD arguments passed in.
    """
    decompiler_dict = OPT_ARGS_DECOMPILER if uses_opt_args else DECOMPILER
    if (category, index) in decompiler_dict:
        raise ValueError(f"Decompiler for ({category}, {index}) appeared more than once in module.")

    def decorator(func):
        decompiler_dict[category, index] = func
        return func  # no actual decoration

    return decorator


def decompile_instruction(
    category: int,
    index: int,
    req_args: list[tp.Any],
    opt_args: list[tp.Any] = None,
    opt_arg_types="",
    enums_manager: GameEnumsManager = None,
) -> str:
    """Uses a manual function (decorated below) or EMEDF information to decompile an EMEVD instruction to EVS format.

    `opt_args` and `opt_arg_types` are only permitted for instructions that take optional arguments, such as `RunEvent`.
    """
    return base_decompiler_instruction(
        EMEDF,
        DECOMPILER,
        OPT_ARGS_DECOMPILER,
        enums,
        category,
        index,
        req_args,
        opt_args,
        opt_arg_types,
        enums_manager,
    )


@_decompile(2000, 0, uses_opt_args=True)
def _RunEvent(
    slot: int, event_id: int, first_arg: int, *opt_args, arg_types: str, enums_manager: GameEnumsManager = None
):
    return base_decompile_run_event(
        slot, event_id, first_arg, *opt_args, arg_types=arg_types, enums_manager=enums_manager
    )


@_decompile(2000, 6, uses_opt_args=True)
def _RunCommonEvent(
    event_id: int, first_arg: int, *opt_args, arg_types: str, enums_manager: GameEnumsManager = None
):
    return base_decompile_run_common_event(
        event_id, first_arg, *opt_args, arg_types=arg_types, enums_manager=enums_manager
    )


@_decompile(2002, 2)
def _PlayCutsceneAndMovePlayer(
    cutscene_id: int, cutscene_flags: CutsceneFlags, move_to_region: Region, area_id: int, block_id: int
):
    """Wrapper is always allowable."""
    game_map = get_map_variable_name((area_id, block_id))
    return f"PlayCutscene({cutscene_id}, {cutscene_flags=}, {move_to_region=}, game_map={game_map})"


@_decompile(2002, 3)
def _PlayCutsceneToPlayer(cutscene_id, cutscene_flags: CutsceneFlags, player_id: Character):
    """Wrapper is always allowable."""
    return f"PlayCutscene({cutscene_id}, {cutscene_flags=}, {player_id=})"


@_decompile(2002, 4)
def _PlayCutsceneAndMoveSpecificPlayer(
    cutscene_id: int,
    cutscene_flags: int,
    move_to_region: Region,
    area_id: int,
    block_id: int,
    player_id: Character,
):
    """Wrapper is always allowable."""
    game_map = get_map_variable_name((area_id, block_id))
    return (
        f"PlayCutscene({cutscene_id}, {cutscene_flags=}, {player_id=}, {move_to_region=}, game_map={game_map})"
    )


@_decompile(2002, 5)
def _PlayCutsceneAndRotatePlayer(
    cutscene_id: int,
    cutscene_flags: int,
    relative_rotation_axis_x,
    relative_rotation_axis_z,
    rotation,
    vertical_translation,
    player_id: Character,
):
    """Wrapper is always allowable."""
    return (
        f"PlayCutscene({cutscene_id=}, {cutscene_flags=}, {player_id=}, "
        f"{rotation=}, {relative_rotation_axis_x=}, {relative_rotation_axis_z=}, {vertical_translation=})"
    )


@_decompile(2003, 4)
def _AwardItemLotToAllPlayers(item_lot: int):
    return f"AwardItemLot({item_lot}, host_only=False)"


@_decompile(2003, 36)
def _AwardItemLotToHostOnly(item_lot: int):
    return f"AwardItemLot({item_lot}, host_only=True)"


@_decompile(2005, 6)
def _SetObjectActivation(obj: Object, obj_act_id: int, state: bool):
    if state is True:
        return f"EnableObjectActivation({obj}, {obj_act_id=})"
    elif state is False:
        return f"DisableObjectActivation({obj}, {obj_act_id=})"
    return f"SetObjectActivation({obj}, {obj_act_id=}, {state=})"


@_decompile(2005, 14)
def _SetObjectActivationWithIdx(obj: Object, obj_act_id, relative_index, state: bool):
    """Defers to a wrapper instruction shared with (2005, 6) if `state` is not an event argument."""
    if state is True:
        return f"EnableObjectActivation({obj}, {obj_act_id=}, {relative_index=})"
    elif state is False:
        return f"DisableObjectActivation({obj}, {obj_act_id=}, {relative_index=})"
    return f"SetObjectActivationWithIdx({obj}, {obj_act_id=}, {relative_index=}, {state=})"


@_decompile(2004, 40)
def _MoveAndSetDrawParent(
    character: Character,
    destination_type: CoordEntityType,
    destination: Object | Character | Region,
    dummy_id: int,
    set_draw_parent: MapPart,
):
    if not isinstance(destination_type, str) and destination_type.name == "Region" and dummy_id == -1:
        if isinstance(destination, MapEntity):  # `destination_type` is implicit
            return f"Move({character}, {destination=}, {set_draw_parent=})"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, {set_draw_parent=})"  # default model point
    if isinstance(destination, MapEntity):  # `destination_type` is implicit
        return f"Move({character}, {destination=}, {dummy_id=}, {set_draw_parent=})"
    return f"Move({character}, {destination=}, {destination_type=}, {dummy_id=}, {set_draw_parent=})"


@_decompile(2004, 41)
def _ShortMove(
    character: Character,
    destination_type: CoordEntityType,
    destination: Object | Character | Region,
    dummy_id: int,
):
    if not isinstance(destination_type, str) and destination_type.name == "Region" and dummy_id == -1:
        if isinstance(destination, MapEntity):  # `destination_type` is implicit
            return f"Move({character}, {destination=}, short_move=True)"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, short_move=True)"  # default model point
    if isinstance(destination, MapEntity):  # `destination_type` is implicit
        return f"Move({character}, {destination=}, {dummy_id=}, short_move=True)"
    return f"Move({character}, {destination=}, {destination_type=}, {dummy_id=}, short_move=True)"


@_decompile(2004, 42)
def _MoveAndCopyDrawParent(
    character: Character,
    destination_type: CoordEntityType,
    destination: Object | Character | Region,
    dummy_id: int,
    copy_draw_parent: Object | Character,
):
    if not isinstance(destination_type, str) and destination_type.name == "Region" and dummy_id == -1:
        if isinstance(destination, MapEntity):  # `destination_type` is implicit
            return f"Move({character}, {destination=}, {copy_draw_parent=})"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, {copy_draw_parent=})"  # default model point
    if isinstance(destination, MapEntity):  # `destination_type` is implicit
        return f"Move({character}, {destination=}, {dummy_id=}, {copy_draw_parent=})"
    return f"Move({character}, {destination=}, {destination_type=}, {dummy_id=}, {copy_draw_parent=})"


@_decompile(3, 4)
def _IfPlayerItemStateExcludingStorage(condition: int, item_type: ItemType, item, state: bool):
    if not isinstance(state, str) and not isinstance(item_type, str):
        state_name = "Has" if state else "DoesNotHave"
        if isinstance(item_type, str):
            return f"IfPlayer{state_name}Item({condition}, {item}, {item_type=})"
        return f"IfPlayer{state_name}{item_type.name}({condition}, {item})"
    return f"IfPlayerItemState({condition}, {state=}, {item=}, {item_type=})"


@_decompile(3, 16)
def _IfPlayerItemStateIncludingStorage(condition: int, item_type: ItemType, item, state: bool):
    if not isinstance(state, str):
        state_name = "Has" if state else "DoesNotHave"
        if isinstance(item_type, str):
            return f"IfPlayer{state_name}Item({condition}, {item}, {item_type=}, including_storage=True)"
        return f"IfPlayer{state_name}{item_type.name}({condition}, {item}, including_storage=True)"
    return f"IfPlayerItemState({condition}, {state=}, {item=}, {item_type=}, including_storage=True)"


# TODO: I'm not 100% certain that the old `IfActionButton` works in DS3.


def _IfActionButton(
    condition: int,
    anchor_type: CoordEntityType,
    anchor_entity: Object | Character | Region,
    facing_angle: float,
    dummy_id: int,
    max_distance: float,
    prompt_text: int,
    trigger_attribute: TriggerAttribute,
    button: int,
    boss_version=False,
    line_intersects=None,
):
    defaults = {
        "trigger_attribute": TriggerAttribute.Human | TriggerAttribute.Hollow,
        "button": 0,
    }
    if not isinstance(anchor_type, str):
        defaults["facing_angle"] = 0.0 if anchor_type.name == "Region" else 180.0
        defaults["max_distance"] = 0.0 if anchor_type.name == "Region" else 2.0
        if anchor_type.name == "Region":
            defaults["dummy_id"] = -1
    arg_string = assemble_arg_string(
        defaults,
        condition,
        prompt_text=prompt_text,
        anchor_entity=anchor_entity,
        anchor_type=anchor_type,
        facing_angle=facing_angle,
        max_distance=max_distance,
        dummy_id=dummy_id,
        button=button,
        trigger_attribute=trigger_attribute,
    )
    if boss_version:
        if line_intersects is not None:
            return f"IfActionButton({arg_string}, {boss_version=}, {line_intersects=})"
        else:
            return f"IfActionButton({arg_string}, {boss_version=})"
    else:
        if line_intersects is not None:
            return f"IfActionButton({arg_string}, {line_intersects=})"
        else:
            return f"IfActionButton({arg_string})"


@_decompile(3, 5)
def _IfActionButtonBasic(
    condition: int,
    anchor_type: CoordEntityType,
    anchor_entity: Object | Character | Region,
    facing_angle: float,
    dummy_id: int,
    max_distance: float,
    prompt_text: int,
    trigger_attribute: TriggerAttribute,
    button: int,
):
    return _IfActionButton(
        condition,
        anchor_type,
        anchor_entity,
        facing_angle,
        dummy_id,
        max_distance,
        prompt_text,
        trigger_attribute,
        button,
        boss_version=False,
        line_intersects=None,
    )


@_decompile(3, 13)
def _IfActionButtonBasic(
    condition: int,
    anchor_type: CoordEntityType,
    anchor_entity: Object | Character | Region,
    facing_angle: float,
    dummy_id: int,
    max_distance: float,
    prompt_text: int,
    trigger_attribute: TriggerAttribute,
    button: int,
):
    return _IfActionButton(
        condition,
        anchor_type,
        anchor_entity,
        facing_angle,
        dummy_id,
        max_distance,
        prompt_text,
        trigger_attribute,
        button,
        boss_version=True,
        line_intersects=None,
    )


@_decompile(3, 18)
def _IfActionButtonBasic(
    condition: int,
    anchor_type: CoordEntityType,
    anchor_entity: Object | Character | Region,
    facing_angle: float,
    dummy_id: int,
    max_distance: float,
    prompt_text: int,
    trigger_attribute: TriggerAttribute,
    button: int,
    line_intersects: Object | Character | Region,
):
    return _IfActionButton(
        condition,
        anchor_type,
        anchor_entity,
        facing_angle,
        dummy_id,
        max_distance,
        prompt_text,
        trigger_attribute,
        button,
        boss_version=False,
        line_intersects=line_intersects,
    )


@_decompile(3, 19)
def _IfActionButtonBasic(
    condition: int,
    anchor_type: CoordEntityType,
    anchor_entity: Object | Character | Region,
    facing_angle: float,
    dummy_id: int,
    max_distance: float,
    prompt_text: int,
    trigger_attribute: TriggerAttribute,
    button: int,
    line_intersects: Object | Character | Region,
):
    return _IfActionButton(
        condition,
        anchor_type,
        anchor_entity,
        facing_angle,
        dummy_id,
        max_distance,
        prompt_text,
        trigger_attribute,
        button,
        boss_version=True,
        line_intersects=line_intersects,
    )


@_decompile(1014, 0)
def _DefineLabel_0():
    return "DefineLabel(0)"


@_decompile(1014, 1)
def _DefineLabel_1():
    return "DefineLabel(1)"


@_decompile(1014, 2)
def _DefineLabel_2():
    return "DefineLabel(2)"


@_decompile(1014, 3)
def _DefineLabel_3():
    return "DefineLabel(3)"


@_decompile(1014, 4)
def _DefineLabel_4():
    return "DefineLabel(4)"


@_decompile(1014, 5)
def _DefineLabel_5():
    return "DefineLabel(5)"


@_decompile(1014, 6)
def _DefineLabel_6():
    return "DefineLabel(6)"


@_decompile(1014, 7)
def _DefineLabel_7():
    return "DefineLabel(7)"


@_decompile(1014, 8)
def _DefineLabel_8():
    return "DefineLabel(8)"


@_decompile(1014, 9)
def _DefineLabel_9():
    return "DefineLabel(9)"


@_decompile(1014, 10)
def _DefineLabel_10():
    return "DefineLabel(10)"


@_decompile(1014, 11)
def _DefineLabel_11():
    return "DefineLabel(11)"


@_decompile(1014, 12)
def _DefineLabel_12():
    return "DefineLabel(12)"


@_decompile(1014, 13)
def _DefineLabel_13():
    return "DefineLabel(13)"


@_decompile(1014, 14)
def _DefineLabel_14():
    return "DefineLabel(14)"


@_decompile(1014, 15)
def _DefineLabel_15():
    return "DefineLabel(15)"


@_decompile(1014, 16)
def _DefineLabel_16():
    return "DefineLabel(16)"


@_decompile(1014, 17)
def _DefineLabel_17():
    return "DefineLabel(17)"


@_decompile(1014, 18)
def _DefineLabel_18():
    return "DefineLabel(18)"


@_decompile(1014, 19)
def _DefineLabel_19():
    return "DefineLabel(19)"


@_decompile(1014, 20)
def _DefineLabel_20():
    return "DefineLabel(20)"
