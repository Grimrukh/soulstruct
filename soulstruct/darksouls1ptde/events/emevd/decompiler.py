from __future__ import annotations

__all__ = ["DECOMPILER", "OPT_ARGS_DECOMPILER", "auto_decompile"]

import logging
import struct
import typing as tp

from soulstruct.base.events.emevd.utils import EntityEnumsManager
from soulstruct.game_types.msb_types import *
from soulstruct.darksouls1ptde.maps.constants import get_map_variable_name

from . import enums
from .enums import *
from .emedf import EMEDF

_LOGGER = logging.getLogger(__name__)


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


def _reprocess_args(integer_args, arg_type_string):
    """Re-interpret integer data as a given struct."""
    true_arg_type_string = arg_type_string.replace("s", "I")
    packed = struct.pack(len(integer_args) * "I", *integer_args)
    return struct.unpack("@" + true_arg_type_string, packed[: struct.calcsize(true_arg_type_string)])


def _any_strings(*args):
    return any(isinstance(arg, str) for arg in args)


def _looks_like_entity_id(value: int, event_id: int = None):
    """Guesses if `value` is an entity ID. Used with `RunEvent{Common}` calls.

    TODO: Currently blindly converting seven-digit integers in event calls, under the probably safe
     assumption that there will be no false positives. Also including four-digit integers starting with 6
     (NPC entity IDs), unless `event_id` is 11210117 (DS1R arena event - super hacky).
     Ideally, we would inspect if the event argument is used in ANY instruction as a `MapEntity`.
    """
    if not isinstance(value, int) or event_id == 11210717:
        return False
    return len(str(value)) == 7 or (len(str(value)) == 4 and str(value)[0] == "6")


class EnumValue:
    """Stores information about an `IntEnum` value, including a proper `repr` for string formatting and `eq` for
    useful value comparisons."""
    def __init__(self, enum: type, value: int):
        self.type = enum
        self.type_name = enum.__name__
        self.instance = enum(value)
        self.name = enum(value).name
        self.value = value

    def __repr__(self):
        return f"{self.type_name}.{self.name}"

    def __eq__(self, other: int):
        return self.value == other

    def __getattr__(self, name):
        return getattr(self.instance, name)


def _process_args(args: dict[str, tp.Any], emedf_args_info: dict, enums_manager: EntityEnumsManager = None):
    for arg_name, arg_value in args.items():
        if isinstance(arg_value, str):  # event argument (will be printed as a valid Python variable name)
            continue

        arg_type = emedf_args_info[arg_name]["type"]
        if arg_type is bool:
            args[arg_name] = bool(arg_value)
            continue

        try:
            origin = tp.get_origin(arg_type)
        except AttributeError:
            union_types = ()
        else:
            union_types = tp.get_args(arg_type) if origin is tp.Union else ()
            # All union types should be `MapEntity` subclasses; this will be enforced by the checkout method
            # below (invalid types will have no entity ID dictionaries).

        if Character in union_types or issubclass(arg_type, Character):
            # Check for player entity ID, but continue otherwise.
            try:
                args[arg_name] = EnumValue(PlayerEntity, arg_value).name.upper()
            except ValueError:
                pass  # check enums below
            else:
                continue

        if union_types or issubclass(arg_type, MapEntity):
            if enums_manager is None:
                continue  # leave as entity ID

            # Look up entity ID from imported module enums (generally parsed in `EMEVD.to_evs()`).

            try:
                if union_types:
                    args[arg_name] = enums_manager.check_out_enum(arg_value, *union_types)
                else:  # single class
                    args[arg_name] = enums_manager.check_out_enum(arg_value, arg_type)
            except EntityEnumsManager.MissingEntityError:
                pass
            continue  # leave as entity ID if not replaced

        try:
            enum = getattr(enums, arg_type.__name__)  # get real enum class from game-specific module
        except AttributeError:
            raise ValueError(f"Invalid enum type for decompiler (arg '{arg_name}'): {arg_type.__name__}")
        try:
            args[arg_name] = EnumValue(enum, arg_value)
        except ValueError:
            raise ValueError(f"Invalid {str(enum)} value: {arg_value}")


def _assemble_arg_string(defaults: dict, *args, **kwargs):
    """Assemble a string of `args` (without argument names) and `kwargs` (with argument names) in the given order.
    Any kwarg whose value matches the same key's value in `defaults` is left out.

    The values of `args` and `kwargs` should be ready for string formatting.
    """
    arguments = [f"{arg}" for arg in args]
    for kwarg, value in kwargs.items():
        try:
            default = defaults[kwarg]
        except KeyError:
            arguments.append(f"{kwarg}={value}")
        else:
            if value != default:
                arguments.append(f"{kwarg}={value}")
    return ", ".join(arguments)


def auto_decompile(
    category: int,
    index: int,
    arg_values: list[tp.Any],
    enums_manager: EntityEnumsManager = None,
) -> str:
    """Uses EMEDF information to decompile an EMEVD instruction to EVS format.

    Cannot be used for instructions with optional arguments, such as `RunEvent`. These are always handled with manual
    decompiling functions.
    """
    instr_info = EMEDF[category, index]
    evs_name = instr_info["alias"]
    emedf_args_info = instr_info["args"]
    if len(emedf_args_info) != len(arg_values):
        raise ValueError(
            f"Cannot decompile instruction ({category}, {index}): number of arguments in EMEDF "
            f"({len(emedf_args_info)}) does not match number of argument values given ({len(arg_values)})."
        )

    args = {arg_name: arg_values[i] for i, arg_name in enumerate(emedf_args_info)}
    _process_args(args, emedf_args_info, enums_manager)

    evs_args_info = instr_info.get("evs_args", emedf_args_info)
    arg_strings = []
    evs_args = {}
    for evs_arg_name, evs_arg_info in evs_args_info.items():
        if "to_evs" in evs_arg_info:
            # Convert to EVS args.
            evs_args[evs_arg_name] = evs_arg_info['to_evs'](args)
        elif evs_arg_name in emedf_args_info:
            # Default to EMEDF value.
            evs_args[evs_arg_name] = args[evs_arg_name]
        else:
            raise ValueError(f"EVS argument '{evs_arg_name}' does not define 'to_evs' or appear in EMEDF args.")

    # Check values against partials.
    if "partials" in instr_info:
        for partial_evs_name, partial_kwargs in instr_info["partials"].items():
            if all(evs_args[k] == v for k, v in partial_kwargs.items()):
                # Full partial kwargs match. Use this EVS name and remove partial keywords.
                evs_name = partial_evs_name
                for k in partial_kwargs:
                    evs_args.pop(k)

    # Omit default values (including for partials, which use the same default values for non-baked keywords) and hide
    # keyword names as long as `hide_name` remains True.
    hiding_names = True
    for evs_arg_name, arg_value in evs_args.items():
        hide_name = evs_args_info.get("hide_name", False)
        if hide_name and not hiding_names:
            print(f"# WARNING: 'hide_name' is False then True again for instruction '{instr_info['alias']}'.")
        hiding_names &= hide_name
        default = evs_args_info["default"]
        if default is not None:
            if callable(default):
                default = default(evs_args)
            if arg_value == default:
                # Omit from arguments.
                continue
        # Otherwise, generate string.
        arg_strings.append(f"{arg_value}" if hiding_names else f"{evs_arg_name}={arg_value}")

    # TODO: text wrap?
    return f"{evs_name}({', '.join(arg_strings)}"


@_decompile(2000, 0, uses_opt_args=True)
def _RunEvent(
    slot: int, event_id: int, first_arg: int, *opt_args, arg_types: str, enums_manager: EntityEnumsManager = None
):
    # TODO: Detect if event exists in entire EMEVD and call it by name if so.
    if not opt_args and first_arg == 0:
        # NOTE: Some Bloodborne events use non-zero slots for events without optional arguments.
        if slot != 0:
            return f"RunEvent({event_id}, {slot=})"
        return f"RunEvent({event_id})"

    args = (first_arg, *opt_args)

    if arg_types and "f" in arg_types and not arg_types.strip("i").strip("f") and all(isinstance(i, int) for i in args):
        # Process incorrectly unpacked arguments (e.g. floats represented by integers).
        try:
            args = _reprocess_args(args, arg_types)
        except struct.error:
            _LOGGER.error(
                f"Error interpreting event arguments for event ID {event_id}: args = {args}, arg_types = {arg_types}"
            )
            raise

    if enums_manager is not None:
        new_args = list(args)
        for i, arg in enumerate(args):
            if _looks_like_entity_id(arg, event_id):
                try:
                    new_args[i] = enums_manager.check_out_enum(arg, any_class=True)
                except EntityEnumsManager.MissingEntityError:
                    pass  # do nothing
        args = tuple(new_args)

    if not arg_types or not arg_types.strip("i"):
        # No arg types, or all signed integers (default). "arg_types" keyword omitted.
        return f"RunEvent({event_id}, {slot=}, args={args})"
    return f"RunEvent({event_id}, {slot=}, args={args}, arg_types=\"{arg_types}\")"


@_decompile(2002, 2)
def _PlayCutsceneAndMovePlayer(
    cutscene_id: int, cutscene_flags: CutsceneFlags, move_to_region: Region, area_id: int, block_id: int
):
    """Wrapper is always allowable."""
    move_to_map = get_map_variable_name(area_id, block_id)
    return f"PlayCutscene({cutscene_id}, {cutscene_flags=}, {move_to_region=}, {move_to_map=})"


@_decompile(2002, 3)
def _PlayCutsceneToPlayer(cutscene_id, cutscene_flags: CutsceneFlags, player_id: PlayerEntity):
    """Wrapper is always allowable."""
    return f"PlayCutscene({cutscene_id}, {cutscene_flags=}, {player_id=})"


@_decompile(2002, 4)
def _PlayCutsceneAndMoveSpecificPlayer(
    cutscene_id: int,
    cutscene_flags: int,
    move_to_region: Region,
    area_id: int,
    block_id: int,
    player_id: PlayerEntity,  # TODO: Put in EMEDF.
):
    """Wrapper is always allowable."""
    move_to_map = get_map_variable_name(area_id, block_id)
    return (
        f"PlayCutscene({cutscene_id}, {cutscene_flags=}, {player_id=}, {move_to_region=}, {move_to_map=})"
    )


@_decompile(2002, 5)
def _PlayCutsceneAndRotatePlayer(
    cutscene_id: int,
    cutscene_flags: int,
    relative_rotation_axis_x,
    relative_rotation_axis_z,
    rotation,
    vertical_translation,
    player_id: PlayerEntity,
):
    """Wrapper is always allowable."""
    return (
        f"PlayCutscene({cutscene_id=}, {cutscene_flags=}, {player_id=}, "
        f"{rotation=}, {relative_rotation_axis_x=}, {relative_rotation_axis_z=}, {vertical_translation=})"
    )


@_decompile(2003, 4)
def _AwardItemLotToAllPlayers(item_lot_id: int):
    return f"AwardItemLot({item_lot_id}, host_only=False)"


@_decompile(2003, 36)
def _AwardItemLotToHostOnly(item_lot_id: int):
    return f"AwardItemLot({item_lot_id}, host_only=True)"


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
    destination: tp.Union[Character, Object, Region],
    model_point: int,
    set_draw_parent: MapPart,
):
    if not _any_strings(destination_type) and destination_type.name == "Region" and model_point == -1:
        if isinstance(destination, MapEntity):  # `destination_type` is implicit
            return f"Move({character}, {destination=}, {set_draw_parent=})"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, {set_draw_parent=})"  # default model point
    if isinstance(destination, MapEntity):  # `destination_type` is implicit
        return f"Move({character}, {destination=}, {model_point=}, {set_draw_parent=})"
    return f"Move({character}, {destination=}, {destination_type=}, {model_point=}, {set_draw_parent=})"


@_decompile(2004, 41)
def _ShortMove(
    character: Character,
    destination_type: CoordEntityType,
    destination: tp.Union[Character, Object, Region],
    model_point: int,
):
    if not _any_strings(destination_type) and destination_type.name == "Region" and model_point == -1:
        if isinstance(destination, MapEntity):  # `destination_type` is implicit
            return f"Move({character}, {destination=}, short_move=True)"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, short_move=True)"  # default model point
    if isinstance(destination, MapEntity):  # `destination_type` is implicit
        return f"Move({character}, {destination=}, {model_point=}, short_move=True)"
    return f"Move({character}, {destination=}, {destination_type=}, {model_point=}, short_move=True)"


@_decompile(2004, 42)
def _MoveAndCopyDrawParent(
    character: Character,
    destination_type: CoordEntityType,
    destination: tp.Union[Character, Object, Region],
    model_point: int,
    copy_draw_parent: tp.Union[Character, Object],
):
    if not _any_strings(destination_type) and destination_type.name == "Region" and model_point == -1:
        if isinstance(destination, MapEntity):  # `destination_type` is implicit
            return f"Move({character}, {destination=}, {copy_draw_parent=})"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, {copy_draw_parent=})"  # default model point
    if isinstance(destination, MapEntity):  # `destination_type` is implicit
        return f"Move({character}, {destination=}, {model_point=}, {copy_draw_parent=})"
    return f"Move({character}, {destination=}, {destination_type=}, {model_point=}, {copy_draw_parent=})"


@_decompile(3, 4)
def _IfPlayerItemStateExcludingStorage(condition: int, item_type: ItemType, item, state: bool):
    if not isinstance(state, str):
        state_name = "Has" if state else "DoesNotHave"
        if isinstance(item_type, str):
            return f"IfPlayer{state_name}Item({condition}, {item}, {item_type=}, including_storage=False)"
        return f"IfPlayer{state_name}{item_type.name}({condition}, {item}, including_storage=False)"
    return f"IfPlayerItemState({condition}, {state=}, {item=}, {item_type=}, including_storage=False)"


@_decompile(3, 16)
def _IfPlayerItemStateIncludingStorage(condition: int, item_type: ItemType, item, state: bool):
    if not isinstance(state, str):
        state_name = "Has" if state else "DoesNotHave"
        if isinstance(item_type, str):
            return f"IfPlayer{state_name}Item({condition}, {item}, {item_type=}, including_storage=True)"
        return f"IfPlayer{state_name}{item_type.name}({condition}, {item}, including_storage=True)"
    return f"IfPlayerItemState({condition}, {state=}, {item=}, {item_type=}, including_storage=True)"


def _IfActionButton(
    condition: int,
    anchor_type: CoordEntityType,
    anchor_entity: tp.Union[Character, Object, Region],
    facing_angle: float,
    model_point: int,
    max_distance: float,
    prompt_text: int,
    trigger_attribute: TriggerAttribute,
    button: int,
    boss_version=False,
    line_intersects=None,
):
    defaults = {
        "trigger_attribute": TriggerAttribute.Human_or_Hollow,
        "button": 0,
    }
    if not isinstance(anchor_type, str):
        defaults["facing_angle"] = 0.0 if anchor_type.name == "Region" else 180.0
        defaults["max_distance"] = 0.0 if anchor_type.name == "Region" else 2.0
        if anchor_type.name == "Region":
            defaults["model_point"] = -1
    arg_string = _assemble_arg_string(
        defaults,
        condition,
        prompt_text=prompt_text,
        anchor_entity=anchor_entity,
        anchor_type=anchor_type,
        facing_angle=facing_angle,
        max_distance=max_distance,
        model_point=model_point,
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
    anchor_entity: tp.Union[Character, Object, Region],
    facing_angle: float,
    model_point: int,
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
        model_point,
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
    anchor_entity: tp.Union[Character, Object, Region],
    facing_angle: float,
    model_point: int,
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
        model_point,
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
    anchor_entity: tp.Union[Character, Object, Region],
    facing_angle: float,
    model_point: int,
    max_distance: float,
    prompt_text: int,
    trigger_attribute: TriggerAttribute,
    button: int,
    line_intersects: tp.Union[Character, Object, Region],
):
    return _IfActionButton(
        condition,
        anchor_type,
        anchor_entity,
        facing_angle,
        model_point,
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
    anchor_entity: tp.Union[Character, Object, Region],
    facing_angle: float,
    model_point: int,
    max_distance: float,
    prompt_text: int,
    trigger_attribute: TriggerAttribute,
    button: int,
    line_intersects: tp.Union[Character, Object, Region],
):
    return _IfActionButton(
        condition,
        anchor_type,
        anchor_entity,
        facing_angle,
        model_point,
        max_distance,
        prompt_text,
        trigger_attribute,
        button,
        boss_version=True,
        line_intersects=line_intersects,
    )
