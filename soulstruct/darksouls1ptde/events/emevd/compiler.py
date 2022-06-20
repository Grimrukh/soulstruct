"""Contains additional custom instructions (by me) that wrap other real EMEVD instructions.

Though you may "call" these functions in EVS script, they are never actually called directly. The three dictionaries
defined at the top of the module (filled by decorators at module load) will be used to look up the functions. When
compiling EVS, the dictionary will be reversed and the EVS instruction name will be used to look up a custom instruction
from this module or the (category, index) for EMEDF. When decompiling to EVS,

Usually, these just simplify or pre-bake certain arguments (e.g., `Enable/Disable` variants, tuple `FlagRange` values)
or combine multiple underlying EMEVD instructions into one (e.g., `IfActionButton`).
"""
import logging
from enum import Enum

from soulstruct.base.events.emevd.numeric import to_numeric
from soulstruct.base.events.emevd.utils import get_write_offset, EventArgumentData
from soulstruct.game_types import *

from .enums import *
from .emedf import EMEDF, EMEDF_ALIASES

_LOGGER = logging.getLogger(__name__)


# This dictionary maps EVS instruction function names to functions that produce actual numeric output. These functions
# may take different arguments to a single underlying instruction (e.g., tuples as flag ranges, `GameMap` instances) or
# merge multiple underlying instructions into one interface for simplicity, such as `IfActionButton` or `PlayCutscene`.
# If a function name does not appear in here, it will found as an 'alias' in EMEDF and compiled automatically.
# (Such functions should still appear in the PYI module for intelli-sense.)
COMPILER = {}


def auto_compile(instr_name: str, *args, **kwargs) -> list[str]:
    """Compile instruction from EMEDF information.

    If positional `args` are used, they must be ordered correctly for EMEDF and not repeated in `kwargs`, just like
    regular Python.
    """
    category, index, instr_info = EMEDF_ALIASES[instr_name]
    emedf_args_info = instr_info["args"]
    evs_args_info = instr_info.get("evs_args", emedf_args_info)

    # Build real `kwargs` from `args and `kwargs`.
    args = list(args)
    evs_kwargs = {}
    for evs_arg_name in evs_args_info:
        if args:
            evs_kwargs[evs_arg_name] = args.pop(0)
        else:
            if evs_arg_name in kwargs and evs_arg_name in evs_kwargs:
                # Positional argument was also given as keyword. Invalid usage.
                raise ValueError(
                    f"Keyword argument '{evs_arg_name}' for instruction '{instr_name}' was already given as a "
                    f"position argument."
                )
            evs_kwargs[evs_arg_name] = kwargs[evs_arg_name]

    if "partials" in instr_info and instr_name in instr_info["partials"]:
        # Fill in baked keyword arguments and redirect name.
        for k, v in instr_info["partials"][instr_name]:
            if k in evs_kwargs:
                raise ValueError(f"Keyword '{k}' should not be given to partially baked instruction '{instr_name}'.")
            evs_kwargs[k] = v
        instr_name = instr_info["alias"]

    # Fill in default EVS arguments.
    for evs_arg_name, evs_arg_info in evs_args_info.items():
        if not evs_arg_info:
            evs_arg_info = emedf_args_info[evs_arg_name]
        if evs_arg_name not in evs_kwargs:
            default = evs_arg_info["default"]
            if default is None:
                raise ValueError(
                    f"Missing required argument for instruction '{instr_name}' ({category}, {index}): {evs_arg_name}"
                )
            if callable(default):
                try:
                    default = default(evs_kwargs)
                except ValueError as ex:
                    raise ValueError(
                        f"Could not automatically determine default value for argument '{evs_arg_name}' in instruction "
                        f"'{instr_name}' ({category}, {index}). Error: {ex}"
                    )
            evs_kwargs[evs_arg_name] = default

    arg_types = "".join(arg["type"].get_fmt() for arg in emedf_args_info)
    arg_list = []
    arg_loads = []

    # Convert EVS arguments to EMEVD.
    for i, (arg_name, arg_info) in enumerate(emedf_args_info.items()):
        if "from_evs" in arg_info:
            arg_value = arg_info["from_evs"](evs_kwargs)
        elif arg_name not in evs_kwargs:
            raise ValueError(
                f"Argument '{arg_name}' in instruction '{instr_name}' ({category}, {index}) has no 'from_evs' function "
                f"defined in EMEDF."
            )
        else:
            arg_value = evs_kwargs[arg_name]

        if isinstance(arg_value, EventArgumentData):
            arg_value = arg_value.offset_tuple

        if isinstance(arg_value, Enum):
            arg_list.append(arg_value.value)
        elif isinstance(arg_value, bool):
            arg_list.append(int(arg_value))
        elif isinstance(arg_value, tuple):
            # Start offset and size of an event argument.
            write_offset = get_write_offset(arg_types, i)
            arg_loads.append(f"    ^({write_offset} <- {arg_value[0]}, {arg_value[1]})")
            internal_default = arg_info.get("internal_default", 0)
            arg_list.append(internal_default)  # value that will be overridden by event argument
        else:
            arg_list.append(arg_value)
    instruction_string = f"{category: 5d}[{index:02d}] ({arg_types}){arg_list}"
    return [instruction_string] + arg_loads


def _compile(func):
    """Decorator that simply adds the decorated function to the `COMPILER` dictionary under its own name."""
    if func.__name__ in COMPILER:
        raise ValueError(f"EVS instruction {func.__name__} appeared more than once in module.")
    COMPILER[func.__name__] = func
    return func  # no actual decoration


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
    format_string = "iI" + str(arg_types[0])
    if len(arg_types) > 1:
        format_string += f"|{arg_types[1:]}"
    return to_numeric(
        2000, 0, EMEDF[2000, 0], slot, event_id, *args, arg_types=format_string, event_layers=event_layers
    )


@_compile
def EnableObjectActivation(obj: ObjectTyping, obj_act_id: int, relative_index=None):
    """
    Allows the given ObjAct to be performed with the object, optionally only at the given relative_index.

    I've combined two instructions into one here, as they're very similar.
    """
    if relative_index is None:
        return auto_compile("SetObjectActivation", obj=obj, obj_act_id=obj_act_id, state=True)
    return auto_compile(
        "SetObjectActivationWithIdx", obj=obj, obj_act_id=obj_act_id, relative_index=relative_index, state=True
    )


@_compile
def DisableObjectActivation(obj: ObjectTyping, obj_act_id, relative_index=None):
    """
    Prevents the given ObjAct from being performed with the object.

    Used for doors that you can only open once, for example. Again, I've combined the relative index version here.
    """
    if relative_index is None:
        return auto_compile("SetObjectActivation", obj=obj, obj_act_id=obj_act_id, state=False)
    return auto_compile(
        "SetObjectActivationWithIdx", obj=obj, obj_act_id=obj_act_id, relative_index=relative_index, state=False
    )


# TODO: Move to PYI (add to auto-generator).
def EnableThisFlag():
    """Handled directly by the compiler, which calls `EnableFlag()` with the current event ID as its argument."""
    pass


# TODO: Move to PYI (add to auto-generator).
def DisableThisFlag():
    """Handled directly by the compiler, which calls `DisableFlag()` with the current event ID as its argument."""
    pass


@_compile
def AwardItemLot(item_lot_param_id: int, host_only=True):
    """Directly award an item lot to player(s). By default, only the host receives the item."""
    if host_only:
        return auto_compile("AwardItemLotToHostOnly", item_lot_param_id=item_lot_param_id)
    return auto_compile("AwardItemLotToAllPlayers", item_lot_param_id=item_lot_param_id)


@_compile
def PlayCutscene(
    cutscene_id: int,
    cutscene_flags: int = 0,
    player_id: int = None,
    move_to_map: MapTyping = None,
    move_to_region: RegionTyping = None,
    rotation: int = 0,
    relative_rotation_axis_x: float = 0.0,
    relative_rotation_axis_z: float = 0.0,
    vertical_translation: float = 0.0,
):
    """Unified instruction for playing cutscenes. EMEVD has several instructions for playing cutscenes that allow
    different side-effects like playing the cutscene to a specific player, moving a player to a new region/map, or
    rotating a player. This method detects the appropriate low-level instruction to call.

    Args:
        cutscene_id: six-digit cutscene ID which looks up "remo/scn{cutscene_id}.remobnd" in your game files.
        cutscene_flags: bit flags from `CutsceneFlags`, e.g. for unskippable or fade-out cutscenes. Cutscenes are
            generally not skippable in multiplayer.
        player_id: player who will see cutscene or be moved/rotated. Defaults to host player (`10000`). Note that other
            players, e.g. summons, will generally have their own cutscene be played to them in their own EMEVD.
        move_to_map: game map that player will be moved to (`move_to_region` also required).
        move_to_region: MSB region that player will be moved to (`move_to_map` also required).
        rotation: degrees around Y axis by which to rotate `player_id` after the cutscene is done. Cannot be used with
            `move` args, but can be used with `vertical_translation`. Used once in known vanilla EMEVD, after you move
            the giant Anor Londo elevator for the first time in DS1.
        relative_rotation_axis_x: world X coordinate that `rotation` is relative to. Default is 0.0.
        relative_rotation_axis_z: world Z coordinate that `rotation` is relative to. Default is 0.0
        vertical_translation: vertical distance player should be moved. Can be used with `rotation`. Note that this is
            never used in any Soulstruct-supported game.
    """
    if move_to_map or move_to_region:
        if not (move_to_map and move_to_region):
            raise ValueError("You must set both 'move_to_map' and 'move_to_region' for cutscene moves, or neither.")
        if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
            raise ValueError("You cannot use move arguments AND rotation/translation arguments with cutscenes.")
        if player_id is None:
            return auto_compile(
                "PlayCutsceneAndMovePlayer",
                cutscene_id=cutscene_id,
                cutscene_flags=cutscene_flags,
                move_to_region=move_to_region,
                move_to_map=move_to_map,
            )
        return auto_compile(
            "PlayCutsceneAndMoveSpecificPlayer",
            cutscene_id=cutscene_id,
            cutscene_flags=cutscene_flags,
            move_to_region=move_to_region,
            move_to_map=move_to_map,
            player_id=player_id,
        )

    if player_id is None:
        player_id = PLAYER

    if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
        return auto_compile(
            "PlayCutsceneAndRotatePlayer",
            cutscene_id=cutscene_id,
            cutscene_flags=cutscene_flags,
            relative_rotation_axis_x=relative_rotation_axis_x,
            relative_rotation_axis_z=relative_rotation_axis_z,
            rotation=rotation,
            vertical_translation=vertical_translation,
            player_id=player_id,
        )

    return auto_compile(
        "PlayCutsceneToPlayer",
        cutscene_id=cutscene_id,
        cutscene_flags=cutscene_flags,
        player_id=player_id,
    )


@_compile
def Move(
    character: CharacterTyping,
    destination: CoordEntityTyping,
    model_point=-1,
    copy_draw_parent: MapPartTyping = None,
    set_draw_parent: MapPartTyping = None,
    short_move=False,
    destination_type=None,
):
    """Unified instruction for moving a character to some destination entity in the same map.

    Not sure what sort of optimizations 'short' makes, but it's used at various times by the game. I would guess you can
    safely use it when you are moving the character within the same draw group collision. You can also change the draw
    parent of the moved character, which changes when it will be drawn, by setting it manually to a collision in the
    MSB or copying it from an existing map entity (often the same entity as the warp destination).

    I'm calling this 'Move' to distinguish it from warping between maps, which is what people will typically think
    of when they see the term 'warp'.
    """
    if destination_type is None:
        if destination == PLAYER:
            destination_type = CoordEntityType.Character
        else:
            try:
                destination_type = destination.get_coord_entity_type()
            except AttributeError:
                raise AttributeError(
                    "Warp destination has no category. Use 'destination_type' keyword or a " "typed destination."
                )
    if copy_draw_parent is not None and set_draw_parent is not None:
        raise ValueError("You cannot copy and set the draw parent at the same time.")
    if short_move:
        if copy_draw_parent or set_draw_parent:
            raise ValueError("You cannot copy or set the draw parent during a short move.")
        return auto_compile(
            "ShortMove",
            character=character,
            destination=destination,
            model_point=model_point,
            destination_type=destination_type,
        )
    if copy_draw_parent is not None:
        return auto_compile(
            "MoveAndCopyDrawParent",
            character=character,
            destination=destination,
            copy_draw_parent=copy_draw_parent,
            model_point=model_point,
            destination_type=destination_type,
        )
    if set_draw_parent is not None:
        return auto_compile(
            "MoveAndSetDrawParent",
            character=character,
            destination=destination,
            set_draw_parent=set_draw_parent,
            model_point=model_point,
            destination_type=destination_type,
        )
    return auto_compile(
        "MoveToEntity",
        character=character,
        destination=destination,
        model_point=model_point,
        destination_type=destination_type,
    )


@_compile
def IfPlayerItemState(
    condition: int, state: bool, item: ItemTyping, item_type: ItemType = None, including_storage: bool = True
):
    """My wrapper for the two versions that do and do not include storage (e.g., Bottomless Box) in the test."""
    if item_type is None:
        try:
            item_type = item.item_enum
        except AttributeError:
            raise AttributeError("Item type not detected. Use keyword or typed item.")
    if including_storage:
        return auto_compile(
            "IfPlayerItemStateIncludingStorage", condition=condition, item_type=item_type, item=item, state=state
        )
    return auto_compile(
        "IfPlayerItemStateExcludingStorage", condition=condition, item_type=item_type, item=item, state=state
    )


# region `IfPlayerItemState` partials
@_compile
def IfPlayerHasItem(condition: int, item: ItemTyping, item_type: ItemType = None, including_storage: bool = True):
    return IfPlayerItemState(condition, True, item, item_type, including_storage)


@_compile
def IfPlayerHasWeapon(condition: int, weapon: WeaponTyping, including_storage: bool = True):
    return IfPlayerItemState(condition, True, weapon, ItemType.Weapon, including_storage)


@_compile
def IfPlayerHasArmor(condition: int, armor: ArmorTyping, including_storage: bool = True):
    return IfPlayerItemState(condition, True, armor, ItemType.Armor, including_storage)


@_compile
def IfPlayerHasRing(condition: int, ring: RingTyping, including_storage: bool = True):
    return IfPlayerItemState(condition, True, ring, ItemType.Ring, including_storage)


@_compile
def IfPlayerHasGood(condition: int, good: GoodTyping, including_storage: bool = True):
    return IfPlayerItemState(condition, True, good, ItemType.Good, including_storage)


@_compile
def IfPlayerDoesNotHaveItem(
    condition: int, item: ItemTyping, item_type: ItemType = None, including_storage: bool = True
):
    return IfPlayerItemState(condition, False, item, item_type, including_storage)


@_compile
def IfPlayerDoesNotHaveWeapon(condition: int, weapon: WeaponTyping, including_storage: bool = True):
    return IfPlayerItemState(condition, False, weapon, ItemType.Weapon, including_storage)


@_compile
def IfPlayerDoesNotHaveArmor(condition: int, armor: ArmorTyping, including_storage: bool = True):
    return IfPlayerItemState(condition, False, armor, ItemType.Armor, including_storage)


@_compile
def IfPlayerDoesNotHaveRing(condition: int, ring: RingTyping, including_storage: bool = True):
    return IfPlayerItemState(condition, False, ring, ItemType.Ring, including_storage)


@_compile
def IfPlayerDoesNotHaveGood(condition: int, good: GoodTyping, including_storage: bool = True):
    return IfPlayerItemState(condition, False, good, ItemType.Good, including_storage)
# endregion


@_compile
def IfActionButton(
    condition: int,
    prompt_text: EventTextTyping,
    anchor_entity: CoordEntityTyping,
    anchor_type: CoordEntityType = None,
    facing_angle: float = None,
    max_distance: float = None,
    model_point=-1,
    trigger_attribute=TriggerAttribute.Human_or_Hollow,
    button=0,
    boss_version=False,
    line_intersects=None,
):
    if anchor_type is None:
        # Anchor type will never be PLAYER here.
        try:
            anchor_type = anchor_entity.get_coord_entity_type()
        except AttributeError:
            raise ValueError(
                "The `anchor_type` keyword is needed if `anchor_entity` is not an `Object`, `Region`, or `Character`."
            )

    kwargs = dict(
        condition=condition,
        anchor_type=anchor_type,
        anchor_entity=anchor_entity,
        facing_angle=facing_angle,
        model_point=model_point,
        max_distance=max_distance,
        prompt_text=prompt_text,
        trigger_attribute=trigger_attribute,
        button=button,
    )

    if boss_version:
        if line_intersects is None:
            return auto_compile("IfActionButtonBoss", **kwargs)
        else:
            return auto_compile("IfActionButtonBossLineIntersect", **kwargs, line_intersects=line_intersects)
    else:
        if line_intersects is None:
            return auto_compile("IfActionButtonBasic", **kwargs)
        else:
            return auto_compile("IfActionButtonBasicLineIntersect", **kwargs, line_intersects=line_intersects)
