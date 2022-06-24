"""Contains additional custom instructions (by me) that wrap other real EMEVD instructions.

Though you may "call" these functions in EVS script, they are never actually called directly. The three dictionaries
defined at the top of the module (filled by decorators at module load) will be used to look up the functions. When
compiling EVS, the dictionary will be reversed and the EVS instruction name will be used to look up a custom instruction
from this module or the (category, index) for EMEDF. When decompiling to EVS,

Usually, these just simplify or pre-bake certain arguments (e.g., `Enable/Disable` variants, tuple `FlagRange` values)
or combine multiple underlying EMEVD instructions into one (e.g., `IfActionButton`).
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
import typing as tp

from soulstruct.base.events.emevd.compiler import *
from soulstruct.darksouls1ptde.game_types import *

from .enums import *
from .emedf import EMEDF_ALIASES

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


@_compile
def EnableObjectActivation(obj: ObjectTyping, obj_act_id: int, relative_index=None):
    """
    Allows the given ObjAct to be performed with the object, optionally only at the given relative_index.

    I've combined two instructions into one here, as they're very similar.
    """
    if relative_index is None:
        return compile_instruction(
            "SetObjectActivation", obj=obj, obj_act_id=obj_act_id, state=True
        )
    return compile_instruction(
        "SetObjectActivationWithIdx", obj=obj, obj_act_id=obj_act_id, relative_index=relative_index, state=True
    )


@_compile
def DisableObjectActivation(obj: ObjectTyping, obj_act_id, relative_index=None):
    """
    Prevents the given ObjAct from being performed with the object.

    Used for doors that you can only open once, for example. Again, I've combined the relative index version here.
    """
    if relative_index is None:
        return compile_instruction("SetObjectActivation", obj=obj, obj_act_id=obj_act_id, state=False)
    return compile_instruction(
        "SetObjectActivationWithIdx", obj=obj, obj_act_id=obj_act_id, relative_index=relative_index, state=False
    )


@_compile
def AwardItemLot(item_lot_param_id: int, host_only=True):
    """Directly award an item lot to player(s). By default, only the host receives the item."""
    if host_only:
        return compile_instruction("AwardItemLotToHostOnly", item_lot_param_id=item_lot_param_id)
    return compile_instruction("AwardItemLotToAllPlayers", item_lot_param_id=item_lot_param_id)


@_compile
def PlayCutscene(
    cutscene_id: int,
    cutscene_flags: int = 0,
    player_id: int = None,
    game_map: MapTyping = None,
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
        game_map: game map that player will be moved to (`move_to_region` also required).
        move_to_region: MSB region that player will be moved to (`game_map` also required).
        rotation: degrees around Y axis by which to rotate `player_id` after the cutscene is done. Cannot be used with
            `move` args, but can be used with `vertical_translation`. Used once in known vanilla EMEVD, after you move
            the giant Anor Londo elevator for the first time in DS1.
        relative_rotation_axis_x: world X coordinate that `rotation` is relative to. Default is 0.0.
        relative_rotation_axis_z: world Z coordinate that `rotation` is relative to. Default is 0.0
        vertical_translation: vertical distance player should be moved. Can be used with `rotation`. Note that this is
            never used in any Soulstruct-supported game.
    """
    if game_map or move_to_region:
        if not (game_map and move_to_region):
            raise ValueError("You must set both 'game_map' and 'move_to_region' for cutscene moves, or neither.")
        if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
            raise ValueError("You cannot use move arguments AND rotation/translation arguments with cutscenes.")
        if player_id is None:
            return compile_instruction(
                "PlayCutsceneAndMovePlayer",
                cutscene_id=cutscene_id,
                cutscene_flags=cutscene_flags,
                move_to_region=move_to_region,
                game_map=game_map,
            )
        return compile_instruction(
            "PlayCutsceneAndMoveSpecificPlayer",
            cutscene_id=cutscene_id,
            cutscene_flags=cutscene_flags,
            move_to_region=move_to_region,
            game_map=game_map,
            player_id=player_id,
        )

    if player_id is None:
        player_id = PLAYER

    if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
        return compile_instruction(
            "PlayCutsceneAndRotatePlayer",
            cutscene_id=cutscene_id,
            cutscene_flags=cutscene_flags,
            relative_rotation_axis_x=relative_rotation_axis_x,
            relative_rotation_axis_z=relative_rotation_axis_z,
            rotation=rotation,
            vertical_translation=vertical_translation,
            player_id=player_id,
        )

    return compile_instruction(
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
        return compile_instruction(
            "ShortMove",
            character=character,
            destination=destination,
            model_point=model_point,
            destination_type=destination_type,
        )
    if copy_draw_parent is not None:
        return compile_instruction(
            "MoveAndCopyDrawParent",
            character=character,
            destination=destination,
            copy_draw_parent=copy_draw_parent,
            model_point=model_point,
            destination_type=destination_type,
        )
    if set_draw_parent is not None:
        return compile_instruction(
            "MoveAndSetDrawParent",
            character=character,
            destination=destination,
            set_draw_parent=set_draw_parent,
            model_point=model_point,
            destination_type=destination_type,
        )
    return compile_instruction(
        "MoveToEntity",
        character=character,
        destination=destination,
        model_point=model_point,
        destination_type=destination_type,
    )


@_compile
def IfPlayerItemState(
    condition: int, state: bool, item: ItemTyping, item_type: ItemType = None, including_storage: bool = False
):
    """My wrapper for the two versions that do and do not include storage (e.g., Bottomless Box) in the test."""
    if item_type is None:
        try:
            item_type = item.get_item_enum()
        except AttributeError:
            raise AttributeError("Item type not detected. Use keyword or typed item.")
    if including_storage:
        return compile_instruction(
            "IfPlayerItemStateIncludingStorage", condition=condition, item_type=item_type, item=item, state=state
        )
    return compile_instruction(
        "IfPlayerItemStateExcludingStorage", condition=condition, item_type=item_type, item=item, state=state
    )


# region `IfPlayerItemState` partials
@_compile
def IfPlayerHasItem(condition: int, item: ItemTyping, item_type: ItemType = None, including_storage: bool = False):
    return IfPlayerItemState(condition, True, item, item_type, including_storage)


@_compile
def IfPlayerHasWeapon(condition: int, weapon: WeaponTyping, including_storage: bool = False):
    return IfPlayerItemState(condition, True, weapon, ItemType.Weapon, including_storage)


@_compile
def IfPlayerHasArmor(condition: int, armor: ArmorTyping, including_storage: bool = False):
    return IfPlayerItemState(condition, True, armor, ItemType.Armor, including_storage)


@_compile
def IfPlayerHasRing(condition: int, ring: RingTyping, including_storage: bool = False):
    return IfPlayerItemState(condition, True, ring, ItemType.Ring, including_storage)


@_compile
def IfPlayerHasGood(condition: int, good: GoodTyping, including_storage: bool = False):
    return IfPlayerItemState(condition, True, good, ItemType.Good, including_storage)


@_compile
def IfPlayerDoesNotHaveItem(
    condition: int, item: ItemTyping, item_type: ItemType = None, including_storage: bool = False
):
    return IfPlayerItemState(condition, False, item, item_type, including_storage)


@_compile
def IfPlayerDoesNotHaveWeapon(condition: int, weapon: WeaponTyping, including_storage: bool = False):
    return IfPlayerItemState(condition, False, weapon, ItemType.Weapon, including_storage)


@_compile
def IfPlayerDoesNotHaveArmor(condition: int, armor: ArmorTyping, including_storage: bool = False):
    return IfPlayerItemState(condition, False, armor, ItemType.Armor, including_storage)


@_compile
def IfPlayerDoesNotHaveRing(condition: int, ring: RingTyping, including_storage: bool = False):
    return IfPlayerItemState(condition, False, ring, ItemType.Ring, including_storage)


@_compile
def IfPlayerDoesNotHaveGood(condition: int, good: GoodTyping, including_storage: bool = False):
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
            return compile_instruction("IfActionButtonBoss", **kwargs)
        else:
            return compile_instruction("IfActionButtonBossLineIntersect", **kwargs, line_intersects=line_intersects)
    else:
        if line_intersects is None:
            return compile_instruction("IfActionButtonBasic", **kwargs)
        else:
            return compile_instruction("IfActionButtonBasicLineIntersect", **kwargs, line_intersects=line_intersects)
