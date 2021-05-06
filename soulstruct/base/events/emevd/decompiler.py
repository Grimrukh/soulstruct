"""Verbose output that matches EVS language for 'decompiling'. (Does not use IF blocks.)"""
from __future__ import annotations

__all__ = ["parse_parameters", "EnumValue", "InstructionDecompiler"]

import abc
import inspect
import logging
import struct
import typing as tp
from functools import wraps
from typing import Union

from soulstruct.game_types.msb_types import *

from .exceptions import InstructionNotFoundError
from .enums import *
from .utils import EntityEnumsManager

_LOGGER = logging.getLogger(__name__)


def parse_parameters(func_name: str = None, no_name_count=0, ignore_args=()):
    """Generates a decorator that produces a formatted string based on `func_name` and the signature of the decorated
    `InstructionDecompiler` method.

    If neither `func_name` nor `no_name_count` are given, the formatted string is left to the body of the decorated
    method. Otherwise, the method can simply `pass`, as it will never actually be called by the decorator.

    If this function is used as a decorator, it will auto-call the generated decorator on the decorated method (i.e.
    `@parse_parameters` and `@parse_parameters()` have the same effect as decorators).
    """

    if callable(func_name):
        decorate_func, func_name = func_name, None  # auto-call decorator at end
    else:
        decorate_func = None

    def _decorator(func):
        sig = inspect.signature(func)
        defaults = {k: v.default for k, v in sig.parameters.items() if v.default is not inspect.Parameter.empty}

        @wraps(func)
        def _wrapper(self: InstructionDecompiler, *args, enums_manager: EntityEnumsManager):
            if func_name is not None and ignore_args and args == ignore_args:
                return f"{func_name}()"  # arguments are ignored
            try:
                parameters = sig.bind(self, *args).arguments
            except Exception:
                _LOGGER.error(f"Decompiler error: signature = {sig}, received = {('self',) + args}")
                raise
            self._set_enums(parameters, tp.get_type_hints(func), enums_manager=enums_manager)
            if func_name is not None:
                # Function can simply `pass` in this case, as it is never called.
                arg_strings = []
                for i, (key, value) in enumerate(parameters.items()):
                    if i == 0:
                        continue  # self
                    if i < no_name_count + 1:
                        arg_strings.append(f"{value}")
                    elif key in defaults and defaults[key] == value:
                        continue  # leave keyword argument out
                    else:
                        arg_strings.append(f"{key}={value}")
                arg_string = ", ".join(arg_strings)
                return f"{func_name}({arg_string})"
            return func(**parameters)  # enums replaced

        return _wrapper

    if decorate_func:
        return _decorator(decorate_func)  # return default decorator

    return _decorator


class Variable(str):
    """Type of string representing variable event arguments."""
    pass


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


class InstructionDecompiler(abc.ABC):
    """Converts `Instruction` information to low-level EVS language instructions and tests.

    Not yet intelligent enough to produce higher-level features like `if` blocks or `and`/`or` operations.

    Subclassed by each game to specify further instructions. Instructions that are shared across the `EMEVD`
    specification for all supported FromSoft games are defined here.
    """
    SUSPICIOUS = "  # WARNING: Suspicious usage!"
    RUN_EVENT_INSTRUCTIONS = [(2000, 0)]

    ENUMS = None  # type: tp.Any  # game-specific `enums` module (e.g. `soulstruct.darksouls1r.events.emevd.enums`)
    GET_MAP = None  # type: tp.Callable  # converts `(area_id, block_id)` to `GameMap` instance

    def decompile(
        self,
        category: int,
        index: int,
        req_args: list[str],
        opt_args: list[str],
        arg_types: tp.Optional[str] = None,
        enums_manager: EntityEnumsManager = None,
    ) -> str:
        """Check instruction arguments and call the appropriate instruction method."""
        if (category, index) in self.RUN_EVENT_INSTRUCTIONS:
            return self._call(category, index, req_args, opt_args, arg_types, enums_manager=enums_manager)
        elif opt_args or arg_types:
            _LOGGER.error(
                f"Instruction {category}[{index:02d}] cannot use optional arguments or types: "
                f"args = {req_args}, opt_args = {opt_args}, arg_types = {arg_types}"
            )
            raise ValueError(f"Instruction {category}[{index:02d}] cannot use optional arguments.")
        return self._call(category, index, *req_args, enums_manager=enums_manager)

    def _call(self, category, index, *args, enums_manager: EntityEnumsManager):
        try:
            instr_method = getattr(self, f"_{category}_{index:02d}")
        except AttributeError:
            raise InstructionNotFoundError(
                f"Unknown instruction in decompiler: {category}[{index:02d}].")
        try:
            instr_string = instr_method(*args, enums_manager=enums_manager)
        except Exception:
            _LOGGER.error(
                f"Could not decompile instruction {category}[{index:02d}].\nArgs: {args}"
            )
            raise
        return instr_string.replace("'", "")  # f-string '=' printing puts strings (event arguments) in single quotes

    def _get_game_map_variable_name(self, area_id, block_id):
        """Attempts to get the EVS variable name of the game map, like "UNDEAD_BURG".

        Falls back to "(area_id, block_id)" tuple (e.g. for event arguments or custom map IDs).
        """
        try:
            return self.GET_MAP(area_id, block_id).variable_name
        except (KeyError, ValueError):
            return f"({area_id}, {block_id})"

    def _set_enums(
        self,
        parameters: dict[str, tp.Any],
        type_hints: dict[str, Union[type, Union]],
        enums_manager: EntityEnumsManager,
    ):
        """Modifies dictionary in-place by replacing detected enum values with their string names."""
        for key, value in parameters.items():
            if enum_class := type_hints.get(key, None):
                if isinstance(value, str):  # event argument
                    parameters[key] = Variable(value)
                    continue

                if enum_class is bool:
                    parameters[key] = bool(value)
                    continue

                if enum_class is PlayerEntity:
                    # MUST be a player entity ID (e.g. 10000).
                    try:
                        parameters[key] = EnumValue(enum_class, value).name.upper()  # all-caps name (e.g. `PLAYER`)
                    except ValueError:
                        pass
                    continue  # leave as entity ID

                try:
                    origin = tp.get_origin(enum_class)
                except AttributeError:
                    union_types = ()
                else:
                    union_types = tp.get_args(enum_class) if origin is Union else ()
                    # All union types should be `MapEntity` subclasses; this will be enforced by the checkout method
                    # below (invalid types will have no entity ID dictionaries).

                if Character in union_types or issubclass(enum_class, Character):
                    # Check for player entity ID, but continue otherwise.
                    try:
                        parameters[key] = EnumValue(PlayerEntity, value).name.upper()
                    except ValueError:
                        pass  # check enums below
                    else:
                        continue

                if union_types or issubclass(enum_class, MapEntity):
                    if enums_manager is None:
                        continue  # leave as entity ID

                    # Look up entity ID from imported module enums (generally parsed in `EMEVD.to_evs()`).
                    
                    try:
                        if union_types:
                            parameters[key] = enums_manager.check_out_enum(value, *union_types)
                        else:  # single class
                            parameters[key] = enums_manager.check_out_enum(value, enum_class)
                    except EntityEnumsManager.MissingEntityError:
                        pass
                    continue  # leave as entity ID if not replaced

                try:
                    enum = getattr(self.ENUMS, enum_class.__name__)  # get real enum class from game-specific module
                except AttributeError:
                    raise ValueError(f"Invalid enum type for decompiler (arg '{key}'): {enum_class.__name__}")
                try:
                    parameters[key] = EnumValue(enum, value)
                except ValueError:
                    raise ValueError(f"Invalid {str(enum)} value: {value}")

    @staticmethod
    def _any_vars(*args):
        return any(isinstance(v, Variable) for v in args)

    @staticmethod
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

    @staticmethod
    def _process_args(integer_args, arg_type_string):
        """Re-interpret integer data as a given struct."""
        true_arg_type_string = arg_type_string.replace("s", "I")
        packed = struct.pack(len(integer_args) * "I", *integer_args)
        return struct.unpack("@" + true_arg_type_string, packed[: struct.calcsize(true_arg_type_string)])

    @staticmethod
    def _set_state(state_type, state: bool, entity: tp.Any = ""):
        """Generates a simple 'Enable{state_type}', 'Disable{state_type}', or 'Set{state_type}State' instruction."""
        if state is True:
            return f"Enable{state_type}({entity})"
        elif state is False:
            return f"Disable{state_type}({entity})"
        # Variable `state`.
        return f"Set{state_type}State(" + (f"{entity}, " if entity else "") + f"{state=})"

    @staticmethod
    def _looks_like_entity_id(value: int):
        """Guesses if `value` is an entity ID. Used with `RunEvent{Common}` calls.

        TODO: Currently blindly converting seven-digit integers in event calls, under the probably safe
         assumption that there will be no false positives. Also including four-digit integers starting with 6
         (NPC entity IDs).
        """
        return isinstance(value, int) and (len(str(value)) == 7 or len(str(value)) == 4 and str(value)[0] == "6")

    def _2000_00(self, req_args, opt_args, arg_types, enums_manager: EntityEnumsManager = None):
        slot, event_id, first_arg = req_args
        if not opt_args and first_arg == 0:
            # NOTE: Some Bloodborne events use non-zero slots for events without optional arguments.
            if slot != 0:
                return f"RunEvent({event_id}, {slot=})"
            return f"RunEvent({event_id})"

        args = (first_arg, *opt_args)

        if arg_types and arg_types.strip("i") and all(isinstance(i, int) for i in args):
            # Process incorrectly unpacked arguments (e.g. floats represented by integers).
            try:
                args = self._process_args(args, arg_types)
            except struct.error:
                _LOGGER.error(
                    f"Error interpreting event arguments for event ID {event_id}: "
                    f"args = {args}, arg_types = {arg_types}"
                )
                raise

        if enums_manager is not None:
            new_args = list(args)
            for i, arg in enumerate(args):
                if self._looks_like_entity_id(arg):
                    try:
                        new_args[i] = enums_manager.check_out_enum(arg, any_class=True)
                    except EntityEnumsManager.MissingEntityError:
                        pass  # do nothing
            args = tuple(new_args)

        if not arg_types or not arg_types.strip("i"):
            # No arg types, or all signed integers (default). "arg_types" keyword omitted.
            return f"RunEvent({event_id}, {slot=}, args={args})"
        return f"RunEvent({event_id}, {slot=}, args={args}, arg_types=\"{arg_types}\")"

    # ~~~~~~~~~~~~~~ #
    # ~~~ SYSTEM ~~~ #
    # ~~~~~~~~~~~~~~ #

    @parse_parameters
    def _2000_02(self, state: bool):
        return self._set_state("NetworkSync", state)

    @parse_parameters("ClearMainCondition", no_name_count=1)
    def _2000_03(self, dummy_arg):
        pass

    @parse_parameters("IssuePrefetchRequest", no_name_count=1)
    def _2000_04(self, request_id):
        pass

    @parse_parameters("SaveRequest", ignore_args=(0,))
    def _2000_05(self):
        pass

    # ~~~~~~~~~~~~~~~~ #
    # ~~~ CUTSCENE ~~~ #
    # ~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _2002_02(self, cutscene_id, cutscene_type: CutsceneType, move_to_region: Region, area_id, block_id):
        move_to_map = self._get_game_map_variable_name(area_id, block_id)
        if self._any_vars(cutscene_type):
            return f"PlayCutsceneAndMovePlayer({cutscene_id}, {cutscene_type=}, {move_to_region=}, {move_to_map=})"
        skippable = cutscene_type.is_skippable()
        fade_out = cutscene_type.is_fade_out()
        return f"PlayCutscene({cutscene_id}, {skippable=}, {fade_out=}, {move_to_region=}, {move_to_map=})"

    @parse_parameters
    def _2002_03(self, cutscene_id, cutscene_type: CutsceneType, player_id: PlayerEntity):
        if self._any_vars(cutscene_type):
            return f"PlayCutsceneToPlayer({cutscene_id}, {cutscene_type=}, {player_id=})"
        skippable = cutscene_type.is_skippable()
        fade_out = cutscene_type.is_fade_out()
        return f"PlayCutscene({cutscene_id}, {skippable=}, {fade_out=}, {player_id=})"

    @parse_parameters
    def _2002_04(
        self,
        cutscene_id,
        cutscene_type: CutsceneType,
        move_to_region: Region,
        area_id,
        block_id,
        player_id: PlayerEntity,
    ):
        move_to_map = self._get_game_map_variable_name(area_id, block_id)
        if self._any_vars(cutscene_type):
            return (
                f"PlayCutsceneAndMoveSpecificPlayer({cutscene_id}, {cutscene_type=}, {move_to_region=}, "
                f"{move_to_map=}, {player_id=})"
            )
        skippable = cutscene_type.is_skippable()
        fade_out = cutscene_type.is_fade_out()
        return (
            f"PlayCutscene({cutscene_id}, {skippable=}, {fade_out=}, {player_id=}, {move_to_region=}, {move_to_map=})"
        )

    @parse_parameters
    def _2002_05(
        self,
        cutscene_id,
        cutscene_type: CutsceneType,
        relative_rotation_axis_x,
        relative_rotation_axis_z,
        rotation,
        vertical_translation,
        player_id: PlayerEntity,
    ):
        if self._any_vars(cutscene_type):
            return (
                f"PlayCutsceneAndRotatePlayer({cutscene_id}, {cutscene_type=}, {relative_rotation_axis_x=}, "
                f"{relative_rotation_axis_z=}, {rotation=}, {vertical_translation=}, {player_id=})"
            )
        skippable = cutscene_type.is_skippable()
        fade_out = cutscene_type.is_fade_out()
        return (
            f"PlayCutscene({cutscene_id=}, {skippable=}, {fade_out=}, {player_id=}, {rotation=}, "
            f"{relative_rotation_axis_x=}, {relative_rotation_axis_z=}, {vertical_translation=})"
        )

    # ~~~~~~~~~~~~~ #
    # ~~~ EVENT ~~~ #
    # ~~~~~~~~~~~~~ #

    @parse_parameters("RequestAnimation", no_name_count=2)
    def _2003_01(self, entity_id: Character, animation_id, loop: bool, wait_for_completion: bool):
        pass

    @parse_parameters
    def _2003_02(self, flag, state: bool):
        return self._set_state("Flag", state, flag)

    @parse_parameters
    def _2003_03(self, spawner_id: SpawnerEvent, state: bool):
        return self._set_state("Spawner", state, spawner_id)

    @parse_parameters
    def _2003_04(self, item_lot):
        return f"AwardItemLot({item_lot}, host_only=False)"

    @parse_parameters("ShootProjectile")
    def _2003_05(
        self,
        owner_entity: Character,
        projectile_id,
        model_point,
        behavior_id,
        launch_angle_x,
        launch_angle_y,
        launch_angle_z,
    ):
        pass

    @parse_parameters
    def _2003_08(self, event_id, slot, event_return_type: EventReturnType):
        if event_return_type == 1:
            if slot == 0:
                return f"RestartEvent({event_id})"
            return f"RestartEvent({event_id}, {slot=})"
        elif event_return_type == 0:
            if slot == 0:
                return f"StopEvent({event_id})"
            return f"StopEvent({event_id}, {slot=})"
        return f"SetEventState({event_id}, {slot=}, {event_return_type=})"

    @parse_parameters
    def _2003_11(self, state: bool, character: Character, slot, name):
        if state == 1:
            return f"EnableBossHealthBar({character}, {name=}, {slot=})"
        elif state == 0:
            return f"DisableBossHealthBar({character}, {name=}, {slot=})"
        return f"SetBossHealthBarState({character}, {name=}, {slot=}, {state=})"

    @parse_parameters("KillBoss", no_name_count=1)
    def _2003_12(self, game_area_param_id):
        pass

    @parse_parameters
    def _2003_13(
        self,
        navmesh_id: NavigationEvent,
        navmesh_type: NavmeshType,
        operation: OnOffChange,
    ):
        if operation == 2:
            return f"ToggleNavmeshType({navmesh_id}, {navmesh_type})"
        elif operation == 1:
            return f"DisableNavmeshType({navmesh_id}, {navmesh_type})"
        elif operation == 0:
            return f"EnableNavmeshType({navmesh_id}, {navmesh_type})"
        return f"SetNavmeshType({navmesh_id}, {navmesh_type}, {operation=})"

    @parse_parameters
    def _2003_14(self, area_id, block_id, player_start: PlayerStart):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        return f"WarpToMap({game_map=}, {player_start=})"

    @parse_parameters("TriggerMultiplayerEvent", no_name_count=1)
    def _2003_16(self, multiplayer_event_id):
        pass

    @parse_parameters
    def _2003_17(self, first_flag, last_flag, state: bool):
        if state == 1:
            return f"EnableRandomFlagInRange(({first_flag}, {last_flag}))"
        elif state == 0:
            return f"DisableRandomFlagInRange(({first_flag}, {last_flag}))"
        return f"SetRandomFlagInRange(({first_flag}, {last_flag}), {state=})"

    @parse_parameters("ForceAnimation", no_name_count=2)
    def _2003_18(
        self,
        entity_id: Union[Character, Object],
        animation_id,
        loop: bool = False,
        wait_for_completion: bool = False,
        skip_transition: bool = False,
    ):
        pass

    @parse_parameters("SetMapDrawParamSlot", no_name_count=1)
    def _2003_19(self, area_id, slot):
        pass

    @parse_parameters("IncrementNewGameCycle", no_name_count=1)
    def _2003_21(self, dummy_arg):
        pass

    @parse_parameters
    def _2003_22(self, first_flag, last_flag, state: bool):
        return self._set_state("FlagRange", state, entity=f"({first_flag}, {last_flag})")

    @parse_parameters("SetRespawnPoint", no_name_count=1)
    def _2003_23(self, respawn_point_id: SpawnPointEvent):
        pass

    @parse_parameters
    def _2003_24(self, item_type: ItemType, item_id, quantity):
        if isinstance(item_type, Variable):
            if quantity > 0:
                return f"RemoveItemFromPlayer({item_id}, {item_type=}, {quantity=})"
            return f"RemoveItemFromPlayer({item_id}, {item_type=})"
        else:
            if quantity > 0:
                return f"Remove{item_type.name}FromPlayer({item_id}, {quantity=})"
            return f"Remove{item_type.name}FromPlayer({item_id})"

    @parse_parameters("PlaceSummonSign", no_name_count=2)
    def _2003_25(
        self,
        sign_type: SummonSignType,
        character: Character,
        region: Region,
        summon_flag,
        dismissal_flag,
    ):
        pass

    @parse_parameters
    def _2003_26(self, soapstone_message: MessageEvent, state: bool):
        return self._set_state("SoapstoneMessage", state, entity=soapstone_message)

    @parse_parameters("AwardAchievement", no_name_count=1)
    def _2003_28(self, achievement_id):
        pass

    @parse_parameters
    def _2003_30(self, spawning_disabled: bool):
        """Bool is inverted here."""
        if spawning_disabled == 1:
            return "DisableVagrantSpawning()"
        elif spawning_disabled == 0:
            return "EnableVagrantSpawning()"
        return f"SetVagrantSpawningState({spawning_disabled=})"

    @parse_parameters("IncrementEventValue", no_name_count=1)
    def _2003_31(self, flag, bit_count, max_value):
        pass

    @parse_parameters("ClearEventValue", no_name_count=1)
    def _2003_32(self, flag, bit_count):
        pass

    @parse_parameters("SetNextSnugglyTrade", no_name_count=1)
    def _2003_33(self, next_snuggly_flag):
        pass

    @parse_parameters("SnugglyItemDrop", no_name_count=1)
    def _2003_34(self, item_lot_id, region: Region, flag, collision):
        pass

    @parse_parameters("MoveRemains")
    def _2003_35(self, source_region: Region, destination_region: Region):
        pass

    @parse_parameters
    def _2003_36(self, item_lot_id):
        return f"AwardItemLot({item_lot_id}, host_only=True)"

    @parse_parameters("ArenaRankingRequest1v1")
    def _2003_37(self):
        pass

    @parse_parameters("ArenaRankingRequest2v2")
    def _2003_38(self):
        pass

    @parse_parameters("ArenaRankingRequestFFA")
    def _2003_39(self):
        pass

    @parse_parameters("ArenaExitRequest")
    def _2003_40(self):
        pass

    # ~~~~~~~~~~~~~~~~~ #
    # ~~~ CHARACTER ~~~ #
    # ~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _2004_01(self, character: Character, state: bool):
        return self._set_state("AI", state, entity=character)

    @parse_parameters("SetTeamType", no_name_count=2)
    def _2004_02(self, character: Character, team_type: TeamType):
        pass

    @parse_parameters
    def _2004_03(
        self,
        character: Character,
        destination_type: CoordEntityType,
        destination: Union[Character, Object, Region],
        model_point,
    ):
        if not self._any_vars(destination_type) and destination_type.name == "Region" and model_point == -1:
            return f"Move({character}, {destination=}, {destination_type=})"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, {model_point=})"

    @parse_parameters("Kill", no_name_count=1)
    def _2004_04(self, character: Character, award_souls: bool):
        pass

    @parse_parameters
    def _2004_05(self, character: Character, state: bool):
        return self._set_state("Character", state, entity=character)

    @parse_parameters("EzstateAIRequest", no_name_count=1)
    def _2004_06(self, character: Character, command_id, slot):
        pass

    @parse_parameters("CreateProjectileOwner", no_name_count=1)
    def _2004_07(self, entity_id: Character):
        pass

    # 2004_08 is "AddSpecialEffect", which differs from game to game.

    @parse_parameters
    def _2004_09(
        self,
        character: Character,
        standby_animation,
        damage_animation,
        cancel_animation,
        death_animation,
        standby_return_animation,
    ):
        animations = (
            "standby_animation", "damage_animation", "cancel_animation", "death_animation", "standby_return_animation"
        )
        if all(
            anim == -1 for anim in (
                standby_animation, damage_animation, cancel_animation, death_animation, standby_return_animation
            )
        ):
            return f"ResetStandbyAnimationSettings({character})"
        arg_string = self._assemble_arg_string(
            {anim: -1 for anim in animations},
            character,
            standby_animation=standby_animation,
            damage_animation=damage_animation,
            cancel_animation=cancel_animation,
            death_animation=death_animation,
            standby_return_animation=standby_return_animation,
        )
        return f"SetStandbyAnimationSettings({arg_string})"

    @parse_parameters
    def _2004_10(self, character: Character, state: bool):
        return self._set_state("Gravity", state, entity=character)

    @parse_parameters("SetCharacterEventTarget", no_name_count=2)
    def _2004_11(self, character: Character, region: Region):
        pass

    @parse_parameters
    def _2004_12(self, character: Character, state: bool):
        return self._set_state("Immortality", state, entity=character)

    @parse_parameters("SetNest", no_name_count=2)
    def _2004_13(self, character: Character, nest_region: Region):
        pass

    # 2004_14 is "RotateToFaceEntity", which differs from game to game.

    @parse_parameters
    def _2004_15(self, character: Character, state: bool):
        return self._set_state("Invincibility", state, entity=character)

    @parse_parameters("ClearTargetList", no_name_count=1)
    def _2004_16(self, character: Character):
        pass

    @parse_parameters("AICommand", no_name_count=1)
    def _2004_17(self, character: Character, command_id, slot):
        pass

    @parse_parameters("SetEventPoint", no_name_count=1)
    def _2004_18(self, character: Character, region: Region, reaction_range):
        pass

    @parse_parameters("SetAIParamID", no_name_count=2)
    def _2004_19(self, character: Character, ai_id):
        pass

    @parse_parameters("ReplanAI", no_name_count=1)
    def _2004_20(self, character: Character):
        pass

    @parse_parameters("CancelSpecialEffect", no_name_count=2)
    def _2004_21(self, character: Character, special_effect_id):
        pass

    @parse_parameters("CreateNPCPart", no_name_count=1)
    def _2004_22(
        self,
        character: Character,
        npc_part_id,
        part_index: NPCPartType,
        part_health,
        damage_correction,
        body_damage_correction,
        is_invincible: bool,
        start_in_stop_state: bool,
    ):
        pass

    @parse_parameters("SetNPCPartHealth", no_name_count=1)
    def _2004_23(self, character: Character, npc_part_id, desired_health, overwrite_max: bool):
        pass

    @parse_parameters("SetNPCPartEffects", no_name_count=1)
    def _2004_24(self, character: Character, npc_part_id, material_sfx_id, material_vfx_id):
        pass

    @parse_parameters("SetNPCPartBulletDamageScaling", no_name_count=1)
    def _2004_25(self, character: Character, npc_part_id, desired_scaling):
        pass

    @parse_parameters("SetDisplayMask", no_name_count=1)
    def _2004_26(self, character: Character, bit_index, switch_type: OnOffChange):
        pass

    @parse_parameters("SetCollisionMask", no_name_count=1)
    def _2004_27(self, character: Character, bit_index, switch_type: OnOffChange):
        pass

    @parse_parameters("SetNetworkUpdateAuthority", no_name_count=2)
    def _2004_28(self, character: Character, authority_level: UpdateAuthority):
        pass

    @parse_parameters
    def _2004_29(self, character: Character, remove: bool):
        """Bool is inverted here."""
        if remove is True:
            return f"DisableBackread({character})"
        elif remove is False:
            return f"EnableBackread({character})"
        return f"SetBackreadState({character}, {remove=})"

    @parse_parameters
    def _2004_30(self, character: Character, state: bool):
        return self._set_state("HealthBar", state, entity=character)

    @parse_parameters
    def _2004_31(self, character: Character, is_disabled: bool):
        """Bool is inverted here."""
        if is_disabled is True:
            return f"DisableCharacterCollision({character})"
        elif is_disabled == 0:
            return f"EnableCharacterCollision({character})"
        return f"SetCharacterCollisionState({character}, {is_disabled=})"

    @parse_parameters("AIEvent", no_name_count=1)
    def _2004_32(self, character: Character, command_id, slot, first_event_flag, last_event_flag):
        pass

    @parse_parameters("ReferDamageToEntity", no_name_count=2)
    def _2004_33(self, character: Character, target_entity_id: Character):
        pass

    @parse_parameters("SetNetworkUpdateRate", no_name_count=1)
    def _2004_34(self, character: Character, is_fixed: bool, update_rate: CharacterUpdateRate):
        pass

    @parse_parameters("SetBackreadStateAlternate", no_name_count=1)
    def _2004_35(self, character: Character, state: bool):
        pass

    @parse_parameters("HellkiteBreathControl", no_name_count=1)
    def _2004_36(self, character: Character, obj: Object, animation_id):
        pass

    @parse_parameters("DropMandatoryTreasure", no_name_count=1)
    def _2004_37(self, character: Character):
        pass

    @parse_parameters("BetrayCurrentCovenant", ignore_args=(0,))
    def _2004_38(self):
        pass

    @parse_parameters
    def _2004_39(self, character: Character, state: bool):
        return self._set_state("Animations", state, entity=character)

    @parse_parameters
    def _2004_40(
        self,
        character: Character,
        destination_type: CoordEntityType,
        destination: Union[Character, Object, Region],
        model_point,
        set_draw_parent: MapPart,
    ):
        if not self._any_vars(destination_type) and destination_type.name == "Region" and model_point == -1:
            return f"Move({character}, {destination=}, {destination_type=}, {set_draw_parent=})"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, {model_point=}, {set_draw_parent=})"

    @parse_parameters
    def _2004_41(
        self,
        character: Character,
        destination_type: CoordEntityType,
        destination: Union[Character, Object, Region],
        model_point,
    ):
        if not self._any_vars(destination_type) and destination_type.name == "Region" and model_point == -1:
            return f"Move({character}, {destination=}, {destination_type=}, short_move=True)"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, {model_point=}, short_move=True)"

    @parse_parameters
    def _2004_42(
        self,
        character: Character,
        destination_type: CoordEntityType,
        destination: Union[Character, Object, Region],
        model_point,
        copy_draw_parent: Union[Character, Object],
    ):
        if not self._any_vars(destination_type) and destination_type.name == "Region" and model_point == -1:
            return f"Move({character}, {destination=}, {destination_type=}, {copy_draw_parent=})"  # default model point
        return f"Move({character}, {destination=}, {destination_type=}, {model_point=}, {copy_draw_parent=})"

    @parse_parameters("ResetAnimation", no_name_count=1)
    def _2004_43(self, character: Character, disable_interpolation: bool):
        pass

    @parse_parameters("SetTeamTypeAndExitStandbyAnimation", no_name_count=2)
    def _2004_44(self, character: Character, team_type: TeamType):
        pass

    @parse_parameters("HumanityRegistration", no_name_count=2)
    def _2004_45(self, character: Character, initial_humanity_flag):
        pass

    @parse_parameters("IncrementPvPSin", ignore_args=(0,))
    def _2004_46(self):
        pass

    @parse_parameters("EqualRecovery")
    def _2004_47(self):
        pass

    # ~~~~~~~~~~~~~~ #
    # ~~~ OBJECT ~~~ #
    # ~~~~~~~~~~~~~~ #

    @parse_parameters("DestroyObject", no_name_count=1)
    def _2005_01(self, obj: Object, slot=1):
        pass

    @parse_parameters("RestoreObject", no_name_count=1)
    def _2005_02(self, obj: Object):
        pass

    @parse_parameters
    def _2005_03(self, obj: Object, state: bool):
        return self._set_state("Object", state, entity=obj)

    @parse_parameters
    def _2005_04(self, obj: Object, state: bool):
        return self._set_state("Treasure", state, entity=obj)

    @parse_parameters("ActivateObject", no_name_count=1)
    def _2005_05(self, obj: Object, obj_act_id, relative_index):
        pass

    @parse_parameters
    def _2005_06(self, obj: Object, obj_act_id, state: bool):
        return self._set_state("ObjectActivation", state, entity=f"{obj}, {obj_act_id=}")

    @parse_parameters("EndOfAnimation", no_name_count=2)
    def _2005_07(self, obj: Object, animation_id):
        """I have not wrapped this instruction. Just using standard EndOfAnimation (as the game does)."""
        pass

    @parse_parameters("PostDestruction", no_name_count=1)
    def _2005_08(self, obj: Object, slot=1):
        pass

    @parse_parameters("CreateHazard", no_name_count=2)
    def _2005_09(
        self,
        obj_flag,
        obj: Object,
        model_point,
        behavior_param_id,
        target_type: DamageTargetType,
        radius,
        life,
        repetition_time,
    ):
        pass

    @parse_parameters
    def _2005_10(self, obj: Object, area_id, block_id, statue_type: StatueType):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        return f"RegisterStatue({obj}, {game_map=}, {statue_type=})"

    @parse_parameters("MoveObjectToCharacter", no_name_count=1)
    def _2005_11(self, obj: Object, character: Character, model_point):
        pass

    @parse_parameters("RemoveObjectFlag", no_name_count=1)
    def _2005_12(self, obj_flag):
        pass

    @parse_parameters
    def _2005_13(self, obj: Object, state: bool):
        return self._set_state("ObjectInvulnerability", state, entity=obj)

    @parse_parameters
    def _2005_14(self, obj: Object, obj_act_id, relative_index, state: bool):
        """Defers to a wrapper instruction shared with 2005_06 if `state` is not an event argument."""
        if state is True:
            return f"EnableObjectActivation({obj}, {obj_act_id=}, {relative_index=})"
        elif state == 0:
            return f"DisableObjectActivation({obj}, {obj_act_id=}, {relative_index=})"
        return f"SetObjectActivationWithIdx({obj}, {obj_act_id=}, {relative_index=}, {state=})"

    @parse_parameters("EnableTreasureCollection", no_name_count=1)
    def _2005_15(self, obj: Object):
        pass

    # ~~~~~~~~~~~ #
    # ~~~ VFX ~~~ #
    # ~~~~~~~~~~~ #

    @parse_parameters("DeleteVFX", no_name_count=1)
    def _2006_01(self, vfx_id: VFXEvent, erase_root_only: bool):
        pass

    @parse_parameters("CreateVFX", no_name_count=1)
    def _2006_02(self, vfx_id: VFXEvent):
        pass

    @parse_parameters
    def _2006_03(
        self,
        anchor_type: CoordEntityType,
        anchor_entity: Union[Character, Object, Region],
        model_point,
        vfx_id,  # true VFX file ID, NOT a `VFXEvent`!
    ):
        """Argument order changed."""
        if not self._any_vars(anchor_type) and anchor_type.name == "Region" and model_point == -1:
            return f"CreateTemporaryVFX({vfx_id}, {anchor_entity=}, {anchor_type=})"
        return f"CreateTemporaryVFX({vfx_id}, {anchor_entity=}, {anchor_type=}, {model_point=})"

    @parse_parameters
    def _2006_04(self, obj: Object, model_point, vfx_id):
        """Argument order changed. Note that `vfx_id` is a real VFX file ID, NOT a `VFXEvent`."""
        return f"CreateObjectVFX({vfx_id}, {obj=}, {model_point=})"

    @parse_parameters("DeleteObjectVFX", no_name_count=1)
    def _2006_05(self, obj: Object, erase_root: bool):
        pass

    # ~~~~~~~~~~~~~~~ #
    # ~~~ MESSAGE ~~~ #
    # ~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _2007_01(
        self,
        text_id,
        button_type: ButtonType,
        number_buttons: NumberButtons,
        anchor_entity: Union[Character, Object, Region],
        display_distance,
    ):
        return f"DisplayDialog({text_id}, {anchor_entity=}, {display_distance=}, {button_type=}, {number_buttons=})"

    @parse_parameters("DisplayBanner", no_name_count=1)
    def _2007_02(self, banner_type: BannerType):
        pass

    @parse_parameters("DisplayStatus", no_name_count=1)
    def _2007_03(self, text_id, pad_enabled: bool):
        pass

    @parse_parameters("DisplayBattlefieldMessage", no_name_count=1)
    def _2007_04(self, text_id, display_location_index):
        pass

    @parse_parameters("ArenaSetNametag1", no_name_count=1)
    def _2007_05(self, player_id: PlayerEntity):
        pass

    @parse_parameters("ArenaSetNametag2", no_name_count=1)
    def _2007_06(self, player_id: PlayerEntity):
        pass

    @parse_parameters("ArenaSetNametag3", no_name_count=1)
    def _2007_07(self, player_id: PlayerEntity):
        pass

    @parse_parameters("ArenaSetNametag4", no_name_count=1)
    def _2007_08(self, player_id: PlayerEntity):
        pass

    @parse_parameters("DisplayArenaDissolutionMessage", no_name_count=1)
    def _2007_09(self, player_id: PlayerEntity):
        pass

    # ~~~~~~~~~~~~~~ #
    # ~~~ CAMERA ~~~ #
    # ~~~~~~~~~~~~~~ #

    @parse_parameters("ChangeCamera")
    def _2008_01(self, normal_camera_id, locked_camera_id):
        pass

    @parse_parameters
    def _2008_02(
        self,
        vibration_id,
        anchor_type: CoordEntityType,
        anchor_entity: Union[Character, Object, Region],
        model_point,
        decay_start_distance,
        decay_end_distance,
    ):
        if not self._any_vars(anchor_type) and anchor_type.name == "Region" and model_point == -1:
            return (
                f"SetCameraVibration({vibration_id=}, {anchor_entity=}, {decay_start_distance=}, "
                f"{decay_end_distance=}, {anchor_type=})"
            )
        return (
            f"SetCameraVibration({vibration_id=}, {anchor_entity=}, {model_point=}, {decay_start_distance=}, "
            f"{decay_end_distance=}, {anchor_type=})"
        )

    @parse_parameters
    def _2008_03(self, area_id, block_id, camera_slot):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        return f"SetLockedCameraSlot({game_map=}, {camera_slot=})"

    # ~~~~~~~~~~~~~~ #
    # ~~~ SCRIPT ~~~ #
    # ~~~~~~~~~~~~~~ #

    @parse_parameters("RegisterLadder")
    def _2009_00(self, start_climbing_flag, stop_climbing_flag, obj: Object):
        pass

    @parse_parameters("RegisterBonfire", no_name_count=1)
    def _2009_03(self, bonfire_flag, obj: Object, reaction_distance, reaction_angle, initial_kindle_level):
        pass

    @parse_parameters("ActivateMultiplayerBuffs", no_name_count=1)
    def _2009_04(self, character_id: Character):
        pass

    @parse_parameters("NotifyBossBattleStart", ignore_args=(0,))
    def _2009_06(self):
        pass

    @parse_parameters("SendToScript")
    def _2009_07(self, int1, int2, float1, float2):
        """Special function added by Horkrux for DarkSoulsScripting communication."""
        pass

    # ~~~~~~~~~~~~~ #
    # ~~~ SOUND ~~~ #
    # ~~~~~~~~~~~~~ #

    @parse_parameters("SetBackgroundMusic")
    def _2010_01(self, state: bool, slot, entity: Union[Character, Object, Region], sound_type: SoundType, sound_id):
        pass

    @parse_parameters("PlaySoundEffect")
    def _2010_02(self, anchor_entity: Union[Character, Object, Region], sound_type: SoundType, sound_id):
        pass

    @parse_parameters
    def _2010_03(self, sound_id, state: bool):
        return self._set_state("SoundEvent", state, entity=sound_id)

    # ~~~~~~~~~~~~~~~~~ #
    # ~~~ COLLISION ~~~ #
    # ~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _2011_01(self, collision_id: Collision, state: bool):
        return self._set_state("Collision", state, entity=collision_id)

    @parse_parameters
    def _2011_02(self, collision_id: Collision, state: bool):
        return self._set_state("CollisionBackreadMask", state, entity=collision_id)

    # ~~~~~~~~~~~~~~~~~~ #
    # ~~~ MAP PIECES ~~~ #
    # ~~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _2012_01(self, map_piece_id, state: bool):
        return self._set_state("MapPiece", state, entity=map_piece_id)

    # ~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~ LOGIC: SYSTEM ~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _1000_00(self, state: bool, condition):
        if state is True:
            return f"AwaitConditionTrue({condition})"
        if state is False:
            return f"AwaitConditionFalse({condition})"
        return f"AwaitConditionState({state=}, {condition=})"

    @parse_parameters
    def _1000_01(self, line_count, state: bool, condition):
        if state is True:
            return f"SkipLinesIfConditionTrue({line_count}, {condition})"
        elif state is False:
            return f"SkipLinesIfConditionFalse({line_count}, {condition})"
        return f"SkipLinesIfConditionState({line_count}, {state=}, {condition=})"

    @parse_parameters
    def _1000_02(self, event_return_type: EventReturnType, state: bool, input_condition):
        if self._any_vars(event_return_type, state):
            return f"ReturnIfConditionState({event_return_type=}, {state=}, {input_condition=})"
        return f"{event_return_type.name}IfCondition{state}({input_condition})"

    @parse_parameters("SkipLines", no_name_count=1)
    def _1000_03(self, line_count):
        pass

    @parse_parameters
    def _1000_04(self, event_return_type: EventReturnType):
        if not self._any_vars(event_return_type):
            return f"{event_return_type.name}()"
        return f"Return({event_return_type=})"

    @parse_parameters
    def _1000_05(self, line_count, comparison_type: ComparisonType, left, right):
        if isinstance(comparison_type, Variable):
            return f"SkipLinesIfComparison({line_count}, {comparison_type=}, {left=}, {right=})"
        return f"SkipLinesIf{comparison_type.name}({line_count}, {left=}, {right=})"

    @parse_parameters()
    def _1000_06(
        self,
        event_return_type: EventReturnType,
        comparison_type: ComparisonType,
        left,
        right,
    ):
        if self._any_vars(event_return_type, comparison_type):
            return f"ReturnIfComparison({event_return_type=}, {comparison_type=}, {left=}, {right=})"
        return f"{event_return_type.name}If{comparison_type.name}({left=}, {right=})"

    @parse_parameters
    def _1000_07(self, line_count, state: bool, input_condition):
        if state is True:
            return f"SkipLinesIfFinishedConditionTrue({line_count}, {input_condition})"
        elif state is False:
            return f"SkipLinesIfFinishedConditionFalse({line_count}, {input_condition})"
        return f"SkipLinesIfFinishedConditionState({line_count}, {state=}, {input_condition=})"

    @parse_parameters
    def _1000_08(self, event_return_type: EventReturnType, state: bool, input_condition):
        if self._any_vars(event_return_type, state):
            return f"ReturnIfFinishedConfditionState({event_return_type=}, {state=}, {input_condition=})"
        return f"{event_return_type.name}IfFinishedCondition{bool(state)}({input_condition})"

    @parse_parameters("WaitForNetworkApproval")
    def _1000_09(self, max_seconds):
        pass

    # ~~~~~~~~~~~~~~~~~~~ #
    # ~~~ LOGIC: TIME ~~~ #
    # ~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters("Wait", no_name_count=1)
    def _1001_00(self, seconds):
        pass

    @parse_parameters("WaitFrames", no_name_count=1)
    def _1001_01(self, frames):
        pass

    @parse_parameters("WaitRandomSeconds")
    def _1001_02(self, min_seconds, max_seconds):
        pass

    @parse_parameters("WaitRandomFrames")
    def _1001_03(self, min_frames, max_frames):
        pass

    # ~~~~~~~~~~~~~~~~~~~~ #
    # ~~~ LOGIC: EVENT ~~~ #
    # ~~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _1003_00(self, state: FlagState, flag_type: FlagType, flag):
        if self._any_vars(state, flag_type):
            return f"AwaitFlagState({state=}, {flag_type=}, {flag=})"
        if state != 2:
            if flag_type == 0:
                return f"AwaitFlag{state.name}({flag})"
            elif flag_type == 1:
                if flag == 0:
                    return f"AwaitThisEvent{state.name}()"
            elif flag_type == 2:
                if flag == 0:
                    return f"AwaitThisEventSlot{state.name}()"
        # No simple instruction found -- this implies a highly unusual combination of arguments!
        return f"AwaitFlagState({state=}, {flag_type=}, {flag=})" + self.SUSPICIOUS

    @parse_parameters
    def _1003_01(self, line_count, state: FlagState, flag_type: FlagType, flag):
        if self._any_vars(state, flag_type):
            return f"SkipLinesIfFlagState({state=}, {flag_type=}, {flag=})"
        if state != 2:
            if flag_type == 0:
                return f"SkipLinesIfFlag{state.name}({line_count}, {flag})"
            elif flag == 0:
                if flag_type == 1:
                    return f"SkipLinesIfThisEvent{state.name}({line_count})"
                elif flag_type == 2:
                    return f"SkipLinesIfThisEventSlot{state.name}({line_count})"
        # No simple instruction found -- this implies a highly unusual combination of arguments!
        return f"SkipLinesIfFlagState({state=}, {flag_type=}, {flag=})" + self.SUSPICIOUS

    @parse_parameters
    def _1003_02(
        self,
        event_return_type: EventReturnType,
        state: FlagState,
        flag_type: FlagType,
        flag,
    ):
        if self._any_vars(event_return_type, state, flag_type):
            return f"ReturnIfFlagState({event_return_type=}, {state=}, {flag_type=}, {flag=})"
        if state != 2:
            if flag_type == 0:
                return f"{event_return_type.name}IfFlag{state.name}({flag})"
            elif flag == 0:
                if flag_type == 1:
                    return f"{event_return_type.name}IfThisEvent{state.name}()"
                elif flag_type == 2:
                    return f"{event_return_type.name}IfThisEventSlot{state.name}()"
        # No simple instruction found -- this implies a highly unusual combination of arguments!
        return f"ReturnIfFlagState({event_return_type=}, {state=}, {flag_type=}, {flag=})" + self.SUSPICIOUS

    @parse_parameters
    def _1003_03(
        self, line_count, state: RangeState, flag_type: FlagType, first_flag, last_flag
    ):
        flag_range = f"({first_flag}, {last_flag})"
        if self._any_vars(state, flag_type):
            return f"SkipLinesIfFlagRangeState({line_count}, {state=}, {flag_type=}, {flag_range=})"
        if flag_type == 0:
            return f"SkipLinesIfFlagRange{state.name}({line_count}, {flag_range})"
        return f"SkipLinesIfFlagRangeState({line_count}, {state=}, {flag_type=}, {flag_range=})" + self.SUSPICIOUS

    @parse_parameters
    def _1003_04(
        self,
        event_return_type: EventReturnType,
        state: RangeState,
        flag_type: FlagType,
        first_flag,
        last_flag,
    ):
        flag_range = f"({first_flag}, {last_flag})"
        if self._any_vars(event_return_type, state, flag_type):
            return f"ReturnIfFlagRangeState({event_return_type=}, {state=}, {flag_type=}, {flag_range=})"
        if flag_type == 0:
            return f"{event_return_type.name}IfFlagRange{state.name}({flag_range})"
        return f"ReturnIfFlagRangeState({event_return_type=}, {state=}, {flag_type=}, {flag_range=})" + self.SUSPICIOUS

    @parse_parameters
    def _1003_05(self, line_count, state: MultiplayerState):
        if self._any_vars(state):
            return f"SkipLinesIfMultiplayerState({line_count}, {state=})"
        return f"SkipLinesIf{state.name}({line_count})"

    @parse_parameters
    def _1003_06(self, event_return_type: EventReturnType, state: MultiplayerState):
        if self._any_vars(event_return_type, state):
            return f"ReturnIfMultiplayerState({event_return_type=}, {state=})"
        return f"{event_return_type.name}If{state.name}()"

    @parse_parameters
    def _1003_07(self, line_count, state: bool, area_id, block_id):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        if state is True:
            return f"SkipLinesIfInsideMap({line_count}, {game_map=})"
        elif state is False:
            return f"SkipLinesIfOutsideMap({line_count}, {game_map=})"
        return f"SkipLinesIfMapPresenceState({line_count}, {state=}, {game_map=})"

    @parse_parameters
    def _1003_08(self, event_return_type: EventReturnType, state: bool, area_id, block_id):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        if self._any_vars(event_return_type, state):
            return f"ReturnIfMapPresenceState({event_return_type=}, {game_map=}, {state=})"
        if state is True:
            return f"{event_return_type.name}IfInsideMap({game_map=})"
        elif state is False:
            return f"{event_return_type.name}IfOutsideMap({game_map=})"
        return f"ReturnIfMapPresenceState({event_return_type=}, {game_map=}, {state=})" + self.SUSPICIOUS

    # ~~~~~~~~~~~~~~~~~~~~ #
    # ~~~ LOGIC: OBJECT~~~ #
    # ~~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _1005_00(self, state: bool, obj: Object):
        if state is True:
            return f"AwaitObjectDestroyed({obj})"
        if state is False:
            return f"AwaitObjectNotDestroyed({obj})"
        return f"AwaitObjectDestructionState({state=}, {obj=})"

    @parse_parameters
    def _1005_01(self, line_count, state: bool, obj: Object):
        if state is True:
            return f"SkipLinesIfObjectDestroyed({line_count}, {obj})"
        if state is False:
            return f"SkipLinesIfObjectNotDestroyed({line_count}, {obj})"
        return f"SkipLinesIfObjectDestructionState({line_count}, {obj}, {state=})"

    @parse_parameters
    def _1005_02(self, event_return_type: EventReturnType, state: bool, obj: Object):
        if self._any_vars(event_return_type, state):
            return f"ReturnIfObjectDestructionState({event_return_type=}, {obj=}, {state=})"
        if state is True:
            return f"{event_return_type.name}IfObjectDestroyed({obj})"
        elif state is False:
            return f"{event_return_type.name}IfObjectNotDestroyed({obj})"
        return f"ReturnIfObjectDestructionState({event_return_type=}, {obj=}, {state=})" + self.SUSPICIOUS

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~ CONDITIONS: SYSTEM ~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _0_00(self, condition, state: bool, input_condition):
        if self._any_vars(state):
            return f"IfConditionState({condition}, {state=}, {input_condition=})"
        return f"IfCondition{state}({condition}, {input_condition=})"

    @parse_parameters("IfValueComparison", no_name_count=2)
    def _0_01(self, condition, comparison_type: ComparisonType, left, right):
        pass

    # ~~~~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~ CONDITIONS: TIME ~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters("IfTimeElapsed", no_name_count=2)
    def _1_00(self, condition, seconds):
        pass

    @parse_parameters("IfFramesElapsed", no_name_count=2)
    def _1_01(self, condition, frames):
        pass

    @parse_parameters("IfRandomTimeElapsed", no_name_count=1)
    def _1_02(self, condition, min_seconds, max_seconds):
        pass

    @parse_parameters("IfRandomFramesElapsed", no_name_count=1)
    def _1_03(self, condition, min_frames, max_frames):
        pass

    # ~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~ CONDITIONS: EVENT ~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _3_00(self, condition, state: FlagState, flag_type: FlagType, flag):
        if self._any_vars(state, flag_type):
            return f"IfFlagState({condition}, {state=}, {flag_type=}, {flag=})"
        if flag_type == 0:
            return f"IfFlag{state.name}({condition}, {flag})"
        elif flag == 0:
            if flag_type == 1:
                return f"IfThisEvent{state.name}({condition})"
            elif flag_type == 2:
                return f"IfThisEventSlot{state.name}({condition})"
        return f"IfFlagState({condition}, {state=}, {flag_type=}, {flag=})" + self.SUSPICIOUS

    @parse_parameters
    def _3_01(self, condition, state: RangeState, flag_type: FlagType, first_flag, last_flag):
        flag_range = f"({first_flag}, {last_flag})"
        if self._any_vars(state, flag_type):
            return f"IfFlagRangeState({condition}, {state=}, {flag_type=}, {flag_range=})"
        if flag_type == 0:
            return f"IfFlagRange{state.name}({condition}, {flag_range})"
        return f"IfFlagRangeState({condition}, {state=}, {flag_type=}, {flag_range=})" + self.SUSPICIOUS

    @parse_parameters
    def _3_02(self, condition, state: bool, character: Character, region: Region):
        if state is True:
            return f"IfCharacterInsideRegion({condition}, {character}, {region=})"
        elif state is False:
            return f"IfCharacterOutsideRegion({condition}, {character}, {region=})"
        return f"IfCharacterRegionState({condition}, {character}, {region=}, {state=})"

    @parse_parameters
    def _3_03(
        self,
        condition,
        state: bool,
        entity: Union[Character, Object, Region],
        other_entity: Union[Character, Object, Region],
        radius,
    ):
        if state is True:
            return f"IfEntityWithinDistance({condition}, {entity}, {other_entity}, {radius=})"
        elif state is False:
            return f"IfEntityBeyondDistance({condition}, {entity}, {other_entity}, {radius=})"
        return f"IfEntityDistanceState({condition}, {entity}, {other_entity}, {radius}, {state=})"

    @parse_parameters
    def _3_04(self, condition, item_type: ItemType, item, state: bool):
        if not isinstance(state, Variable):
            state_name = "Has" if state else "DoesNotHave"
            if isinstance(item_type, Variable):
                return f"IfPlayer{state_name}Item({condition}, {item}, {item_type=}, including_box=False)"
            return f"IfPlayer{state_name}{item_type.name}({condition}, {item}, including_box=False)"
        return f"IfPlayerItemState({condition}, {state=}, {item=}, {item_type=}, including_box=False)"

    @parse_parameters
    def _3_05(
        self,
        condition,
        anchor_type: CoordEntityType,
        anchor_entity: Union[Character, Object, Region],
        facing_angle,
        model_point,
        max_distance,
        prompt_text,
        trigger_attribute: TriggerAttribute,
        button,
    ):
        defaults = {
            "trigger_attribute": self.ENUMS.TriggerAttribute.Human_or_Hollow,
            "button": 0,
        }
        if not self._any_vars(anchor_type):
            defaults["facing_angle"] = 0.0 if anchor_type.name == "Region" else 180.0
            defaults["max_distance"] = 0.0 if anchor_type.name == "Region" else 2.0
            if anchor_type.name == "Region":
                defaults["model_point"] = -1
        arg_string = self._assemble_arg_string(
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
        return f"IfActionButton({arg_string})"

    @parse_parameters
    def _3_06(self, condition, state: MultiplayerState):
        if self._any_vars(state):
            return f"IfMultiplayerState({condition}, {state=})"
        return f"If{state.name}({condition})"

    @parse_parameters
    def _3_07(self, condition, state: bool, region: Region):
        if state is True:
            return f"IfAllPlayersInsideRegion({condition}, {region=})"
        elif state is False:
            return f"IfAllPlayersOutsideRegion({condition}, {region=})"
        return f"IfAllPlayersRegionState({condition}, {region=}, {state=})"

    @parse_parameters
    def _3_08(self, condition, state: bool, area_id, block_id):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        if state is True:
            return f"IfInsideMap({condition}, {game_map=})"
        elif state is False:
            return f"IfOutsideMap({condition}, {game_map=})"
        return f"IfMapPresenceState({condition}, {game_map=}, {state=})"

    @parse_parameters("IfMultiplayerEvent", no_name_count=2)
    def _3_09(self, condition, multiplayer_event_id):
        pass

    @parse_parameters
    def _3_10(
        self,
        condition,
        flag_type: FlagType,
        first_flag,
        last_flag,
        comparison_type: ComparisonType,
        comparison_value,
    ):
        flag_range = f"({first_flag}, {last_flag})"
        if self._any_vars(flag_type, comparison_type):
            return (
                f"IfTrueFlagCountComparison({condition}, {comparison_value}, {flag_type}, "
                f"{comparison_type}, {flag_range})"
            )
        if flag_type == 0:
            return f"IfTrueFlagCount{comparison_type.name}({condition}, {comparison_value}, {flag_range})"
        return (
            f"IfTrueFlagCountComparison({condition}, {comparison_value}, {flag_type}, "
            f"{comparison_type}, {flag_range})"
        )

    @parse_parameters
    def _3_11(
        self,
        condition,
        world_tendency_type: WorldTendencyType,
        comparison_type: ComparisonType,
        value,
    ):
        if world_tendency_type == 0:
            if comparison_type == 4:
                return f"IfWhiteWorldTendencyGreaterThanOrEqual({condition}, {value})"
            return f"IfWhiteWorldTendencyComparison({condition}, {comparison_type=}, {value=})"
        if world_tendency_type == 1:
            if comparison_type == 4:
                return f"IfBlackWorldTendencyGreaterThanOrEqual({condition}, {value})"
            return f"IfBlackWorldTendencyComparison({condition}, {comparison_type=}, {value=})"
        return f"IfWorldTendencyComparison({condition}, {world_tendency_type=}, {comparison_type=}, {value=})"

    @parse_parameters
    def _3_12(self, condition, flag, bit_count, comparison_type: ComparisonType, value):
        if comparison_type == 0:
            return f"IfEventValueEqual({condition}, {flag}, {bit_count=}, {value=})"
        if comparison_type == 2:
            return f"IfEventValueGreaterThan({condition}, {flag}, {bit_count=}, {value=})"
        return f"IfEventValueComparison({condition}, {flag}, {bit_count=}, {comparison_type=}, {value=})"

    @parse_parameters
    def _3_13(
        self,
        condition,
        anchor_type: CoordEntityType,
        anchor_entity: Union[Character, Object, Region],
        facing_angle,
        model_point,
        max_distance,
        prompt_text,
        trigger_attribute: TriggerAttribute,
        button,
    ):
        defaults = {
            "trigger_attribute": self.ENUMS.TriggerAttribute.Human_or_Hollow,
            "button": 0,
        }
        if not self._any_vars(anchor_type):
            defaults["facing_angle"] = 0.0 if anchor_type.name == "Region" else 180.0
            defaults["max_distance"] = 0.0 if anchor_type.name == "Region" else 2.0
            if anchor_type.name == "Region":
                defaults["model_point"] = -1
        arg_string = self._assemble_arg_string(
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
            boss_version=True,
        )
        return f"IfActionButton({arg_string})"

    @parse_parameters("IfAnyItemDroppedInRegion", no_name_count=2)
    def _3_14(self, condition, region: Region):
        pass

    @parse_parameters
    def _3_15(self, condition, item_type: ItemType, item_id):
        return f"IfItemDropped({condition}, {item_id}, {item_type=})"

    @parse_parameters
    def _3_16(self, condition, item_type: ItemType, item, state: bool):
        if not isinstance(state, Variable):
            state_name = "Has" if state else "DoesNotHave"
            if isinstance(item_type, Variable):
                return f"IfPlayer{state_name}Item({condition}, {item}, {item_type=}, including_box=True)"
            return f"IfPlayer{state_name}{item_type.name}({condition}, {item}, including_box=True)"
        return f"IfPlayerItemState({condition}, {state=}, {item=}, {item_type=}, including_box=True)"

    @parse_parameters
    def _3_17(self, condition, comparison_type: ComparisonType, completion_count):
        if comparison_type == 0:
            return f"IfNewGameCycleEqual({condition}, {completion_count=})"
        if comparison_type == 4:
            return f"IfNewGameCycleGreaterThanOrEqual({condition}, {completion_count=})"
        return f"IfNewGameCycleComparison({condition}, {comparison_type=}, {completion_count=})"

    @parse_parameters
    def _3_18(
        self,
        condition,
        anchor_type: CoordEntityType,
        anchor_entity: Union[Character, Object, Region],
        facing_angle,
        model_point,
        max_distance,
        prompt_text,
        trigger_attribute: TriggerAttribute,
        button,
        line_intersects: Union[Character, Object, Region],
    ):
        defaults = {
            "trigger_attribute": self.ENUMS.TriggerAttribute.Human_or_Hollow,
            "button": 0,
        }
        if not self._any_vars(anchor_type):
            defaults["facing_angle"] = 0.0 if anchor_type.name == "Region" else 180.0
            defaults["max_distance"] = 0.0 if anchor_type.name == "Region" else 2.0
            if anchor_type.name == "Region":
                defaults["model_point"] = -1
        arg_string = self._assemble_arg_string(
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
            line_intersects=line_intersects,
        )
        return f"IfActionButton({arg_string})"

    @parse_parameters
    def _3_19(
        self,
        condition,
        anchor_type: CoordEntityType,
        anchor_entity: Union[Character, Object, Region],
        facing_angle,
        model_point,
        max_distance,
        prompt_text,
        trigger_attribute: TriggerAttribute,
        button,
        line_intersects: Union[Character, Object, Region],
    ):
        defaults = {
            "trigger_attribute": self.ENUMS.TriggerAttribute.Human_or_Hollow,
            "button": 0,
        }
        if not self._any_vars(anchor_type):
            defaults["facing_angle"] = 0.0 if anchor_type.name == "Region" else 180.0
            defaults["max_distance"] = 0.0 if anchor_type.name == "Region" else 2.0
            if anchor_type.name == "Region":
                defaults["model_point"] = -1
        arg_string = self._assemble_arg_string(
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
            line_intersects=line_intersects,
            boss_version=True,
        )
        return f"IfActionButton({arg_string})"

    @parse_parameters("IfEventsComparison", no_name_count=6)
    def _3_20(
        self,
        condition,
        left_flag,
        left_bit_count,
        comparison_type: ComparisonType,
        right_flag,
        right_bit_count,
    ):
        pass

    @parse_parameters
    def _3_21(self, condition, is_owned: bool):
        if is_owned is True:
            return f"IfDLCOwned({condition})"
        elif is_owned is False:
            return f"IfDLCNotOwned({condition})"
        return f"IfDLCState({condition}, {is_owned=})"

    @parse_parameters
    def _3_22(self, condition, state: bool):
        if state is True:
            return f"IfOnline({condition})"
        elif state is False:
            return f"IfOffline({condition})"
        return f"IfOnlineState({condition}, {state=})"

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~ CONDITIONS: CHARACTER ~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _4_00(self, condition, character: Character, state: bool):
        if state is True:
            return f"IfCharacterDead({condition}, {character})"
        elif state is False:
            return f"IfCharacterAlive({condition}, {character})"
        return f"IfCharacterDeathState({condition}, {character}, {state=})"

    @parse_parameters("IfAttacked", no_name_count=2)
    def _4_01(self, condition, attacked: Character, attacker: Character):
        pass

    @parse_parameters
    def _4_02(
        self,
        condition,
        character: Character,
        comparison_type: ComparisonType,
        value,
    ):
        if not isinstance(comparison_type, Variable):
            return f"IfHealth{comparison_type.name}({condition}, {character}, {value})"
        return f"IfHealthComparison({condition}, {character=}, {comparison_type=}, {value=})"

    @parse_parameters
    def _4_03(self, condition, character: Character, character_type: CharacterType):
        if character_type == 8:
            return f"IfCharacterHollow({condition}, {character})"
        elif character_type == 0:
            return f"IfCharacterHuman({condition}, {character})"
        return f"IfCharacterType({condition}, {character}, {character_type})"

    @parse_parameters
    def _4_04(
        self,
        condition,
        targeting_character: Character,
        targeted_character: Character,
        state: bool,
    ):
        if state is True:
            return f"IfCharacterTargeting({condition}, {targeting_character}, {targeted_character})"
        elif state is False:
            return f"IfCharacterNotTargeting({condition}, {targeting_character}, {targeted_character})"
        return f"IfCharacterTargetingState({condition}, {targeting_character}, {targeted_character}, {state=})"

    @parse_parameters
    def _4_05(self, condition, character: Character, special_effect, state: bool):
        if state is True:
            return f"IfCharacterHasSpecialEffect({condition}, {character}, {special_effect})"
        elif state is False:
            return f"IfCharacterDoesNotHaveSpecialEffect({condition}, {character}, {special_effect})"
        return f"IfCharacterSpecialEffectState({condition}, {character}, {special_effect}, {state=})"

    @parse_parameters
    def _4_06(
        self,
        condition,
        character: Character,
        npc_part_id,
        value,
        comparison_type: ComparisonType,
    ):
        if comparison_type == 5:
            return f"IfCharacterPartHealthLessThanOrEqual({condition}, {character}, {npc_part_id=}, {value=})"
        return (
            f"IfCharacterPartHealthComparison({condition}, {character}, {npc_part_id=}, "
            f"{comparison_type=}, {value=})"
        )

    @parse_parameters
    def _4_07(self, condition, character: Character, state: bool):
        if state is True:
            return f"IfCharacterBackreadEnabled({condition}, {character})"
        elif state is False:
            return f"IfCharacterBackreadDisabled({condition}, {character})"
        return f"IfCharacterBackreadState({condition}, {character}, {state=})"

    @parse_parameters
    def _4_08(self, condition, character: Character, tae_event_id, state: bool):
        if state is True:
            return f"IfHasTAEEvent({condition}, {character}, {tae_event_id=})"
        elif state is False:
            return f"IfDoesNotHaveTAEEvent({condition}, {character}, {tae_event_id=})"
        return f"IfTAEEventState({condition}, {character}, {tae_event_id=}, {state=})"

    @parse_parameters("IfHasAIStatus", no_name_count=2)
    def _4_09(self, condition, character: Character, ai_status: AIStatusType):
        pass

    @parse_parameters
    def _4_10(self, condition, state: bool):
        if state is True:
            return f"IfSkullLanternActive({condition})"
        elif state is False:
            return f"IfSkullLanternInactive({condition})"
        return f"IfSkullLanternState({condition}, {state=})"

    @parse_parameters("IfPlayerClass", no_name_count=2)
    def _4_11(self, condition, class_type: ClassType):
        pass

    @parse_parameters("IfPlayerCovenant", no_name_count=2)
    def _4_12(self, condition, covenant: Covenant):
        pass

    @parse_parameters
    def _4_13(self, condition, comparison_type: ComparisonType, comparison_value):
        if comparison_type == 4:
            return f"IfPlayerSoulLevelGreaterThanOrEqual({condition}, {comparison_value})"
        if comparison_type == 5:
            return f"IfPlayerSoulLevelLessThanOrEqual({condition}, {comparison_value})"
        return f"IfPlayerSoulLevelComparison({condition}, {comparison_type}, {comparison_value})"

    @parse_parameters
    def _4_14(
        self,
        condition,
        character: Character,
        comparison_type: ComparisonType,
        value,
    ):
        if isinstance(comparison_type, Variable):
            return f"IfHealthValueComparison({condition}, {character}, {comparison_type}, {value})"
        return f"IfHealthValue{comparison_type.name}({condition}, {character}, {value})"

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~ CONDITIONS: OBJECT ~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters
    def _5_00(self, condition, state: bool, obj: Object):
        if state is True:
            return f"IfObjectDestroyed({condition}, {obj})"
        elif state is False:
            return f"IfObjectNotDestroyed({condition}, {obj})"
        return f"IfObjectDestructionState({condition}, {obj}, {state=})"

    @parse_parameters("IfObjectDamagedBy", no_name_count=2)
    def _5_01(self, condition, obj: Object, attacker: Character):
        pass

    @parse_parameters("IfObjectActivated", no_name_count=1)
    def _5_02(self, condition, obj_act_id):
        pass

    @parse_parameters("IfObjectHealthValueComparison", no_name_count=4)
    def _5_03(self, condition, obj: Object, comparison_type: ComparisonType, value):
        pass

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~ CONDITIONS: COLLISION ~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    @parse_parameters("IfMovingOnCollision", no_name_count=2)
    def _11_00(self, condition, collision):
        pass

    @parse_parameters("IfRunningOnCollision", no_name_count=2)
    def _11_01(self, condition, collision):
        pass

    @parse_parameters("IfStandingOnCollision", no_name_count=2)
    def _11_02(self, condition, collision):
        pass
