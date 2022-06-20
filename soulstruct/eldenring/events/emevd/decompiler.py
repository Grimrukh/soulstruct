__all__ = ["InstructionDecompiler"]

import struct
import logging
from typing import Union

from soulstruct.base.events.emevd.decompiler import (
    InstructionDecompiler as _BaseDecompiler,
    parse_parameters,
)
from soulstruct.base.events.emevd.utils import EntityEnumsManager
from soulstruct.eldenring.maps.constants import get_map
from soulstruct.game_types.msb_types import *
from .enums import *
from . import enums

_LOGGER = logging.getLogger(__name__)


class InstructionDecompiler(_BaseDecompiler):
    RUN_EVENT_INSTRUCTIONS = _BaseDecompiler.RUN_EVENT_INSTRUCTIONS + [(2000, 6)]

    ENUMS = enums
    GET_MAP = staticmethod(get_map)

    def _get_game_map_variable_name(self, area_id, block_id, cc_id=0, dd_id=0):
        """Attempts to get the EVS variable name of the game map, like "UNDEAD_BURG".

        Falls back to "(area_id, block_id)" tuple (e.g. for event arguments or custom map IDs).
        """
        try:
            return self.GET_MAP((area_id, block_id, cc_id, dd_id)).variable_name
        except (KeyError, ValueError):
            return f"({area_id}, {block_id}, {cc_id}, {dd_id})"

    def _add_min_target_count(self, string, min_target_count):
        if min_target_count == 1:
            return string
        return string[:-1] + f", {min_target_count=})"

    def _add_target_args(self, string, target_comparison_type, target_count):
        if target_comparison_type == 0 and target_count == 1:
            return string
        target_comparison_type = f"ComparisonType.{ComparisonType(target_comparison_type).name}"
        return string[:-1] + f", {target_comparison_type=}, {target_count=})"

    def _2000_06(self, req_args, opt_args, arg_types, enums_manager):
        event_id, first_arg = req_args
        if not opt_args and first_arg == 0:
            return f"RunCommonEvent({event_id})"

        args = (first_arg, *opt_args)

        if arg_types and "f" in arg_types and not arg_types.strip("i").strip("f") and all(isinstance(i, int) for i in args):
            # Process incorrectly unpacked arguments (e.g. floats represented by integers).
            try:
                args = self._reprocess_args(args, arg_types)
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
            return f"RunCommonEvent({event_id}, args={args})"
        return f"RunCommonEvent({event_id}, args={args}, arg_types=\"{arg_types}\")"

    @parse_parameters("UnknownSystem_07")
    def _2000_07(self, slot):
        """TODO: Not known to HPR. Argument seems to match event slot number."""
        pass

    @parse_parameters("UnknownSystem_08")
    def _2000_08(self, slot):
        """TODO: Not known to HPR. Argument seems to match event slot number."""
        pass

    @parse_parameters("IfUnsignedValueComparison", no_name_count=2)
    def _0_02(self, condition, comparison_type: ComparisonType, left, right):
        pass

    @parse_parameters
    def _1_05(self, condition, start_hours, start_minutes, start_seconds, end_hours, end_minutes, end_seconds):
        return (
            f"IfTimeOfDay({condition}, earliest=({start_hours}, {start_minutes}, {start_seconds}), "
            f"latest=({end_hours}, {end_minutes}, {end_seconds}))"
        )

    def _3_02(self, condition, state, character: Character, region: Region, min_target_count=-1):
        return self._add_min_target_count(
            super()._3_02(condition, state, character, region),
            min_target_count,
        )

    def _3_03(
        self,
        condition,
        state,
        entity: Union[Character, Object, Region],
        other_entity: Union[Character, Object, Region],
        radius,
        min_target_count=1,
    ):
        """`IfEntityDistanceState`"""
        return self._add_min_target_count(
            super()._3_03(condition, state, entity, other_entity, radius),
            min_target_count,
        )

    @parse_parameters
    def _3_08(self, condition, state: bool, area_id, block_id, cc_id, dd_id):
        game_map = self._get_game_map_variable_name(area_id, block_id, cc_id, dd_id)
        if state is True:
            return f"IfInsideMap({condition}, {game_map=})"
        elif state is False:
            return f"IfOutsideMap({condition}, {game_map=})"
        return f"IfMapPresenceState({condition}, {game_map=}, {state=})"

    @parse_parameters
    def _3_23(self, condition, attacked_entity: Character, attacker: Character, damage_type: DamageType):
        if not self._any_vars(damage_type) and damage_type.name == "Unspecified":
            # Leave out default `damage_type` value.
            return f"IfAttackedWithDamageType({condition}, {attacked_entity=}, {attacker=})"
        return f"IfAttackedWithDamageType({condition}, {attacked_entity=}, {attacker=}, {damage_type=})"

    @parse_parameters("IfActionButtonParam", no_name_count=1)
    def _3_24(self, condition, action_button_id, entity: PlayerEntity):
        pass

    @parse_parameters
    def _3_26(self, condition, not_in_own_world: bool):
        if not_in_own_world is True:
            return f"IfPlayerNotInOwnWorld({condition})"
        if not_in_own_world is False:
            return f"IfPlayerInOwnWorld({condition})"
        return f"IfPlayerOwnWorldState({condition}, {not_in_own_world=}"

    @parse_parameters
    def _3_28(self, condition, state: bool, area_id, block_id, ceremony_id):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        if state is True:
            return f"IfMapInCeremony({condition}, {game_map=}, {ceremony_id=})"
        if state is False:
            return f"IfMapNotInCeremony({condition}, {game_map=}, {ceremony_id=})"
        return f"IfMapCeremonyState({condition}, {state=}, {game_map=}, {ceremony_id=})"

    @parse_parameters("IfMultiplayerNetworkPenalized", no_name_count=1)
    def _3_29(self, condition):
        pass

    @parse_parameters
    def _3_30(self, condition, area_id, block_id, cc_id, dd_id):
        game_map = self._get_game_map_variable_name(area_id, block_id, cc_id, dd_id)
        return f"IfInsideMapTile({condition}, {game_map=})"

    @parse_parameters("IfUnknownCondition_31", no_name_count=1)
    def _3_31(self, condition, hours, unk_2, unk_3):
        pass

    @parse_parameters("IfHollowArenaMatchReadyState", no_name_count=1)
    def _3_32(self, condition, is_ready: bool):
        return

    @parse_parameters("IfUnknownCondition_33", no_name_count=1)
    def _3_33(self, condition, unk_1, unk_2: bool):
        """TODO: Not known to HPR."""
        pass

    @parse_parameters("IfPlayerHasArmorEquipped", no_name_count=1)
    def _3_34(self, condition, armor_slot, armor_id, unk_1):
        pass

    @parse_parameters("IfHollowArenaTeamResults", no_name_count=1)
    def _3_35(self, condition, result: HollowArenaResult):
        pass

    @parse_parameters("IfUnknownFlagCheck", no_name_count=1)
    def _3_37(self, condition, flag, state: bool):
        """TODO: Not known to HPR."""
        pass

    @parse_parameters("IfSteamDisconnected", no_name_count=1)
    def _3_38(self, condition, is_disconnected: bool):
        pass

    @parse_parameters("IfAllyPhantomCountComparison", no_name_count=1)
    def _3_39(self, condition, comparison_state: bool, comparison_type: ComparisonType, value):
        pass

    # Many DS3 EMEVD instructions have two "target" arguments added to the old ones. These are omitted from the
    # decompiled script if left as their default values.

    def _4_00(self, condition, character: Character, state, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            super()._4_00(condition, character, state),
            target_comparison_type,
            target_count,
        )

    def _4_02(self, condition, character: Character, comparison_type, value, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            super()._4_02(condition, character, comparison_type, value),
            target_comparison_type,
            target_count,
        )

    def _4_03(self, condition, character: Character, character_type, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            super()._4_03(condition, character, character_type),
            target_comparison_type,
            target_count,
        )

    def _4_05(self, condition, character: Character, special_effect, state, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            super()._4_05(condition, character, special_effect, state),
            target_comparison_type,
            target_count,
        )

    def _4_07(self, condition, character: Character, state, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            super()._4_07(condition, character, state),
            target_comparison_type,
            target_count,
        )

    def _4_08(self, condition, character: Character, tae_event_id, state, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            super()._4_08(condition, character, tae_event_id, state),
            target_comparison_type,
            target_count,
        )

    def _4_09(self, condition, character: Character, ai_status, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            super()._4_09(condition, character, ai_status),
            target_comparison_type,
            target_count,
        )

    def _4_14(self, condition, character: Character, comparison_type, value, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            super()._4_14(condition, character, comparison_type, value),
            target_comparison_type,
            target_count,
        )

    @parse_parameters
    def _4_15(
        self,
        condition,
        character: Character,
        state: bool,
        target_comparison_type: ComparisonType = 0,
        target_count=1,
    ):
        """New instruction in DS3 that displaces `HealthValueComparison` to _4_14 (above)."""
        if state is True:
            string = f"IfCharacterDrawGroupActive({condition}, {character})"
        elif state is False:
            string = f"IfCharacterDrawGroupInactive({condition}, {character})"
        else:
            string = f"IfCharacterDrawGroupState({condition}, {character=}, {state=})"
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters("IfPlayerRemainingYoelLevelComparison", no_name_count=1)
    def _4_26(self, condition, comparison_type: ComparisonType, value):
        pass

    @parse_parameters
    def _4_27(
        self,
        condition,
        character: Character,
        invade_type,
        target_comparison_type: ComparisonType = 0,
        target_count=1,
    ):
        return self._add_target_args(
            f"IfCharacterInvadeType({condition}, {character=}, {invade_type=})",
            target_comparison_type,
            target_count,
        )

    @parse_parameters("IfCharacterChameleonState", no_name_count=1)
    def _4_28(self, condition, character: Character, chameleon_vfx_id, unk_1):
        """TODO: Maybe changed completely."""
        pass

    @parse_parameters("IfUnknownCharacterCondition_31", no_name_count=1)
    def _4_31(self, condition, character: Character, unk_1, unk_2):
        pass

    @parse_parameters
    def _4_34(self, condition, character: Character, unk_1, unk_2, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            f"IfUnknownCharacterCondition_34({condition}, {character}, {unk_1=}, {unk_2=})",
            target_comparison_type=target_comparison_type,
            target_count=target_count,
        )

    def _5_00(self, condition, state, obj: Object, target_comparison_type=0, target_count=1):
        return self._add_target_args(
            super()._5_00(condition, state, obj),
            target_comparison_type,
            target_count,
        )

    @parse_parameters
    def _5_09(
        self,
        condition,
        obj: Object,
        comparison_type: ComparisonType,
        state: bool,
        target_comparison_type: ComparisonType = 0,
        target_count=1,
    ):
        return self._add_target_args(
            f"IfObjectBurnState({condition}, {obj=}, {comparison_type=}, {state=})",
            target_comparison_type,
            target_count,
        )

    @parse_parameters
    def _5_10(self, condition, obj: Object, state: bool, target_comparison_type: ComparisonType = 0, target_count=1):
        if state is True:
            string = f"IfObjectBackreadEnabled({condition}, {obj=})"
        elif state is False:
            string = f"IfObjectBackreadDisabled({condition}, {obj=})"
        else:
            string = f"IfObjectBackreadState({condition}, {obj=}, {state=})"
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters
    def _5_11(self, condition, obj: Object, state: bool, target_comparison_type: ComparisonType = 0, target_count=1):
        if state is True:
            string = f"IfObjectBackreadEnabled_Alternate({condition}, {obj=})"
        elif state is False:
            string = f"IfObjectBackreadDisabled_Alternate({condition}, {obj=})"
        else:
            string = f"IfObjectBackreadState_Alternate({condition}, {obj=}, {state=})"
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters
    def _1000_10(self, line_count, comparison_type: ComparisonType, left, right):
        if comparison_type == ComparisonType.Equal:
            return f"SkipIfUnsignedEqual({line_count}, {left}, {right})"
        elif comparison_type == ComparisonType.NotEqual:
            return f"SkipIfUnsignedNotEqual({line_count}, {left}, {right})"
        return f"SkipIfUnsignedComparison({line_count}, {comparison_type}, {left=}, {right=})"

    @parse_parameters
    def _1000_11(self, event_return_type: EventReturnType, comparison_type: ComparisonType, left, right):
        if (
            self._any_vars(event_return_type, comparison_type)
            or comparison_type not in (ComparisonType.Equal, ComparisonType.NotEqual)
        ):
            return f"ReturnIfUnsignedComparison({event_return_type}, {comparison_type}, {left=}, {right=})"
        return f"{event_return_type.name}IfUnsigned{comparison_type.name}({left=}, {right=})"

    @parse_parameters
    def _1000_101(self, label: Label, state: bool, input_condition):
        if not self._any_vars(state):
            return f"GotoIfCondition{state}({label}, {input_condition=})"
        return f"GotoIfConditionState({label}, {state=}, {input_condition=})"

    @parse_parameters("Goto", no_name_count=1)
    def _1000_103(self, label: Label):
        pass

    @parse_parameters("GotoIfValueComparison", no_name_count=2)
    def _1000_105(self, label: Label, comparison_type: ComparisonType, left, right):
        pass

    @parse_parameters
    def _1000_107(self, label: Label, state: bool, input_condition):
        if not self._any_vars(state):
            return f"GotoIfFinishedCondition{state}({label}, {input_condition=})"
        return f"GotoIfFinishedConditionState({label}, {state=}, {input_condition=})"

    @parse_parameters("WaitHollowArenaHalftime")
    def _1001_04(self, match_type, is_second_half: bool):
        pass

    @parse_parameters("WaitFramesAfterCutscene", no_name_count=1)
    def _1001_06(self, frames):
        pass

    @parse_parameters("SkipLinesIfCoopClientCountComparison", no_name_count=3)
    def _1003_09(self, skip_lines, comparison_type: ComparisonType, value):
        pass

    @parse_parameters
    def _1003_10(self, event_return_type: EventReturnType, comparison_type: ComparisonType, value):
        if not self._any_vars(event_return_type):
            return f"{event_return_type.name}IfCoopClientCountComparison({comparison_type}, {value})"
        return f"ReturnIfCoopClientCountComparison({event_return_type}, {comparison_type}, {value})"

    @parse_parameters
    def _1003_11(
        self,
        label: Label,
        character: Character,
        special_effect,
        state: bool,
        target_comparison_type: ComparisonType = 0,
        target_count=-1,
    ):
        if state is True:
            string = f"GotoIfCharacterHasSpecialEffect({label}, {character=}, {special_effect=})"
        elif state is False:
            string = f"GotoIfCharacterDoesNotHaveSpecialEffect({label}, {character=}, {special_effect=})"
        else:
            string = f"GotoIfCharacterSpecialEffectState({label}, {character=}, {special_effect=}, {state=})"
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters
    def _1003_12(self, lines, not_in_own_world: bool):
        if not_in_own_world is True:
            return f"SkipIfPlayerNotInOwnWorld({lines})"
        elif not_in_own_world is False:
            return f"SkipIfPlayerInOwnWorld({lines})"
        return f"SkipIfPlayerOwnWorldState({lines}, {not_in_own_world=})"

    @parse_parameters
    def _1003_13(self, label: Label, not_in_own_world: bool):
        if not_in_own_world is True:
            return f"GotoIfPlayerNotInOwnWorld({label})"
        elif not_in_own_world is False:
            return f"GotoIfPlayerInOwnWorld({label})"
        return f"GotoIfPlayerOwnWorldState({label}, {not_in_own_world=})"

    @parse_parameters
    def _1003_14(self, event_return_type: EventReturnType, not_in_own_world: bool):
        if self._any_vars(event_return_type):
            return f"ReturnIfPlayerOwnWorldState({event_return_type=}, {not_in_own_world=})"
        if self._any_vars(not_in_own_world):
            return f"{event_return_type.name}IfPlayerOwnWorldState({not_in_own_world=})"
        state = "Not" if not_in_own_world else ""
        return f"{event_return_type.name}IfPlayer{state}InOwnWorld()"

    @parse_parameters
    def _1003_101(self, label: Label, state: FlagState, flag_type: FlagType, flag):
        if self._any_vars(state, flag_type):
            return f"GotoIfFlagState({label}, {state=}, {flag_type=}, {flag=})"
        if state != FlagState.Change:
            if flag_type == FlagType.Absolute:
                return f"GotoIfFlag{state.name}({label}, {flag})"
            elif flag == 0:
                if flag_type == FlagType.RelativeToThisEvent:
                    return f"GotoIfThisEvent{state.name}({label})"
                elif flag_type == FlagType.RelativeToThisEventSlot:
                    return f"GotoIfThisEventSlot{state.name}({label})"
        return f"GotoIfFlagState({label}, {state=}, {flag_type=}, {flag=})" + self.SUSPICIOUS

    @parse_parameters
    def _1003_103(self, label: Label, state: RangeState, flag_type: FlagType, first_flag, last_flag):
        flag_range = f"({first_flag}, {last_flag})"
        if self._any_vars(state, flag_type):
            return f"GotoIfFlagRangeState({label}, {state=}, {flag_type=}, {flag_range=})"
        if flag_type == FlagType.Absolute:
            return f"GotoIfFlagRange{state.name}({label}, {flag_range})"
        return f"GotoIfFlagRangeState({label}, {state=}, {flag_type=}, {flag_range=})" + self.SUSPICIOUS

    @parse_parameters
    def _1003_105(self, label: Label, state: MultiplayerState):
        if self._any_vars(state):
            return f"GotoIfMultiplayerState({label}, {state=})"
        return f"GotoIf{state.name}({label})"

    @parse_parameters
    def _1003_107(self, label: Label, state: bool, area_id, block_id):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        if state is True:
            return f"GotoIfInsideMap({label}, {game_map})"
        if state is False:
            return f"GotoIfOutsideMap({label}, {game_map})"
        return f"GotoIfMapPresenceState({label}, {game_map}, {state=})"

    @parse_parameters("GotoIfCoopClientCountComparison", no_name_count=3)
    def _1003_109(self, label: Label, comparison_type: ComparisonType, value):
        pass

    @parse_parameters
    def _1003_111(
        self,
        event_return_type: EventReturnType,
        character: Character,
        special_effect,
        state: bool,
        target_comparison_type: ComparisonType = 0,
        target_count=1,
    ):
        if self._any_vars(event_return_type):
            string = (
                f"ReturnIfCharacterSpecialEffectState({event_return_type=}, {character=}, {special_effect=}, {state=})"
            )
        elif self._any_vars(state):
            string = f"{event_return_type.name}IfCharacterSpecialEffectState({character}, {special_effect=}, {state=})"
        else:
            state_name = "Has" if state else "DoesNotHave"
            string = f"{event_return_type.name}IfCharacter{state_name}SpecialEffect({character}, {special_effect})"
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters
    def _1003_112(
        self,
        line_count,
        character: Character,
        special_effect,
        state: bool,
        target_comparison_type: ComparisonType = 0,
        target_count=1,
    ):
        if self._any_vars(state):
            string = f"SkipLinesIfCharacterSpecialEffectState({line_count}, {character=}, {special_effect=}, {state=})"
        else:
            state_name = "Has" if state else "DoesNotHave"
            string = f"SkipLinesIfCharacter{state_name}SpecialEffect({line_count}, {character}, {special_effect=})"
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters
    def _1003_200(self, label: Label, state: bool, character: Character, region: Region, min_target_count=-1):
        if state is True:
            string = f"GotoIfCharacterInsideRegion({label}, {character=}, {region=})"
        elif state == 0:
            string = f"GotoIfCharacterOutsideRegion({label}, {character=}, {region=})"
        else:
            string = f"GotoIfCharacterRegionState({label}, {state=}, {character=}, {region=})"
        return self._add_min_target_count(string, min_target_count)

    @parse_parameters
    def _1003_201(
        self,
        event_return_type: EventReturnType,
        state: bool,
        character: Character,
        region: Region,
        min_target_count=-1,
    ):
        if self._any_vars(event_return_type):
            string = f"ReturnIfCharacterRegionState({event_return_type=}, {state=}, {character=}, {region=})"
        elif self._any_vars(state):
            string = f"{event_return_type.name}IfCharacterRegionState({state=}, {character}, {region=})"
        else:
            state_name = "Inside" if state else "Outside"
            string = f"{event_return_type.name}IfCharacter{state_name}Region({character}, {region})"
        return self._add_min_target_count(string, min_target_count)

    @parse_parameters
    def _1003_202(self, line_count, state: bool, character: Character, region: Region, min_target_count=-1):
        if state is True:
            string = f"SkipLinesIfCharacterInsideRegion({line_count}, {character=}, {region=})"
        elif state is False:
            string = f"SkipLinesIfCharacterOutsideRegion({line_count}, {character=}, {region=})"
        else:
            string = f"SkipLinesIfCharacterRegionState({line_count}, {state=}, {character=}, {region=})"
        return self._add_min_target_count(string, min_target_count)

    @parse_parameters("GotoIfHollowArenaMatchType", no_name_count=1)
    def _1003_211(self, label: Label, match_type: HollowArenaMatchType):
        pass

    @parse_parameters
    def _1004_00(
        self,
        line_count,
        character: Character,
        special_effect,
        state: bool,
        target_comparison_type: ComparisonType = 0,
        target_count=1,
    ):
        if state is True:
            string = f"SkipLinesIfCharacterHasSpecialEffect({line_count}, {character=}, {special_effect=})"
        elif state is False:
            string = f"SkipLinesIfCharacterDoesNotHaveSpecialEffect({line_count}, {character=}, {special_effect=})"
        else:
            string = (
                f"SkipLinesIfCharacterSpecialEffectState({line_count}, {character=}, "
                f"{special_effect=}, state={state=})"
            )
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters
    def _1004_01(
        self,
        label: Label,
        character: Character,
        special_effect,
        state: bool,
        target_comparison_type: ComparisonType = 0,
        target_count=1,
    ):
        if state is True:
            string = f"GotoIfCharacterHasSpecialEffect({label}, {character=}, {special_effect=})"
        elif state is False:
            string = f"GotoIfCharacterDoesNotHaveSpecialEffect({label}, {character=}, {special_effect=})"
        else:
            string = (
                f"GotoIfCharacterSpecialEffectState({label}, {character=}, "
                f"{special_effect=}, has_effect={state=})"
            )
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters
    def _1004_02(
        self,
        event_return_type: EventReturnType,
        character: Character,
        special_effect,
        state: bool,
        target_comparison_type: ComparisonType = 0,
        target_count=1,
    ):
        if self._any_vars(event_return_type, state):
            string = (
                f"ReturnIfCharacterSpecialEffectState({event_return_type}, {character}, {special_effect=}, {state=})"
            )
        else:
            state_name = "Has" if state else "DoesNotHave"
            string = (
                f"{event_return_type.name}IfCharacter{state_name}SpecialEffect({character}, {special_effect=})"
            )
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters("UnknownCharacterControl_05")
    def _1004_05(self, unk_1, unk_2, unk_3):
        pass

    @parse_parameters
    def _1005_01(
        self, line_count, state: bool, obj: Object, target_comparison_type: ComparisonType = 0, target_count=-1
    ):
        if state is True:
            string = f"SkipLinesIfObjectDestroyed({line_count}, {obj=})"
        elif state is False:
            string = f"SkipLinesIfObjectNotDestroyed({line_count}, {obj=})"
        else:
            string = f"SkipLinesIfObjectDestructionState({line_count}, {obj=}, {state=})"
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters
    def _1005_02(
        self,
        event_return_type: EventReturnType,
        state: bool,
        obj: Object,
        target_comparison_type: ComparisonType = 0,
        target_count=-1,
    ):
        if self._any_vars(event_return_type, state):
            string = f"ReturnIfObjectDestructionState({event_return_type=}, {obj=}, {state=})"
        else:
            state_name = "" if state else "Not"
            string = f"{event_return_type.name}IfObject{state_name}Destroyed({obj})"
        return self._add_target_args(string, target_comparison_type, target_count)

    @parse_parameters
    def _1005_101(
        self,
        label: Label,
        state: bool,
        obj: Object,
        target_comparison_type: ComparisonType = 0,
        target_count=-1,
    ):
        if self._any_vars(state):
            string = f"GotoIfObjectDestructionState({label}, {obj=}, {state=})"
        else:
            state_name = "" if state else "Not"
            string = f"GotoIfObject{state_name}Destroyed({label}, {obj=})"
        return self._add_target_args(string, target_comparison_type, target_count)

    def _1014_00(self):
        return "DefineLabel(0)"

    def _1014_01(self):
        return "DefineLabel(1)"

    def _1014_02(self):
        return "DefineLabel(2)"

    def _1014_03(self):
        return "DefineLabel(3)"

    def _1014_04(self):
        return "DefineLabel(4)"

    def _1014_05(self):
        return "DefineLabel(5)"

    def _1014_06(self):
        return "DefineLabel(6)"

    def _1014_07(self):
        return "DefineLabel(7)"

    def _1014_08(self):
        return "DefineLabel(8)"

    def _1014_09(self):
        return "DefineLabel(9)"

    def _1014_10(self):
        return "DefineLabel(10)"

    def _1014_11(self):
        return "DefineLabel(11)"

    def _1014_12(self):
        return "DefineLabel(12)"

    def _1014_13(self):
        return "DefineLabel(13)"

    def _1014_14(self):
        return "DefineLabel(14)"

    def _1014_15(self):
        return "DefineLabel(15)"

    def _1014_16(self):
        return "DefineLabel(16)"

    def _1014_17(self):
        return "DefineLabel(17)"

    def _1014_18(self):
        return "DefineLabel(18)"

    def _1014_19(self):
        return "DefineLabel(19)"

    def _1014_20(self):
        return "DefineLabel(20)"

    @parse_parameters("UnknownTimer_04")
    def _2001_04(self, hours, minutes, seconds, unk_1, unk_2, unk_3, unk_4, unk_5, unk_6):
        pass

    @parse_parameters("UnknownTimer_05")
    def _2001_05(self, unk_1):
        pass

    @parse_parameters
    def _2002_06(
        self,
        cutscene,
        cutscene_type: CutsceneFlags,
        move_to_region: Region,
        area_id,
        block_id,
        player_id: PlayerEntity,
        time_period_id,
    ):
        move_to_map = self._get_game_map_variable_name(area_id, block_id)
        return (
            f"PlayCutsceneAndMovePlayerAndSetTimePeriod({cutscene}, {cutscene_type}, {move_to_region=}, "
            f"{move_to_map=}, {player_id=}, {time_period_id=})"
        )

    @parse_parameters("PlayCutsceneAndSetTimePeriod", no_name_count=2)
    def _2002_07(self, cutscene, cutscene_type: CutsceneFlags, player_id: PlayerEntity, time_period_id):
        pass

    @parse_parameters
    def _2002_08(self, move_to_region: Region, area_id, block_id):
        move_to_map = self._get_game_map_variable_name(area_id, block_id)
        return f"PlayCutsceneAndMovePlayer_Dummy({move_to_region}, {move_to_map})"

    @parse_parameters
    def _2002_09(
        self,
        cutscene,
        cutscene_type: CutsceneFlags,
        ceremony_id,
        unknown,
        move_to_region: Region,
        area_id,
        block_id,
        player_id: PlayerEntity,
    ):
        move_to_map = self._get_game_map_variable_name(area_id, block_id)
        return (
            f"PlayCutsceneAndMovePlayerAndSetMapCeremony({cutscene}, {cutscene_type}, {ceremony_id=}, {unknown=}, "
            f"{move_to_region=}, {move_to_map=}, {player_id=})"
        )

    @parse_parameters("UnknownCutscene_10")
    def _2002_10(
        self,
        cutscene,
        cutscene_type: CutsceneFlags,
        player_id: PlayerEntity,
        hours,
        unk_2,
        unk_3,
        unk_4,
        unk_5,
        unk_6,
    ):
        pass

    @parse_parameters("UnknownCutscene_11")
    def _2002_11(
        self,
        cutscene,
        cutscene_type: CutsceneFlags,
        unk_1,
        move_to_region: Region,
        player_id: PlayerEntity,
        unk_2,
        unk_3,
        unk_4,
        unk_5,
        unk_6,
    ):
        pass

    @parse_parameters("UnknownCutscene_12")
    def _2002_12(
        self,
        cutscene,
        cutscene_type: CutsceneFlags,
        respawn_point,
        move_to_region: Region,
        player_id: PlayerEntity,
        unk_2,
        unk_3,
        unk_4,
        unk_5,
        unk_6,
        unk_7,
        unk_8,
        unk_9,
    ):
        pass

    @parse_parameters("UnknownCutscene_13")
    def _2002_13(
        self,
        cutscene,
        cutscene_type: CutsceneFlags,
        respawn_point,
        move_to_region: Region,
        player_id: PlayerEntity,
        unk_2,
        unk_3,
    ):
        pass

    @parse_parameters("KillBossWithUnknown")
    def _2003_12(self, game_area_param_id, unk1):
        pass

    @parse_parameters
    def _2003_11(self, state: bool, character: Character, slot, name):
        """Argument order has changed from DS1."""
        if self._any_vars(state, slot):
            return f"SetBossHealthBarState({character}, {name=}, {slot=}, {state=})"
        state_name = "Enable" if state else "Disable"
        if slot == 0:
            return f"{state_name}BossHealthBar({character}, {name=})"
        return f"{state_name}BossHealthBar({character}, {name=}, {slot=})"

    @parse_parameters
    def _2003_14(self, area_id, block_id, cc_id, dd_id, player_start: PlayerStart, unk_1):
        game_map = self._get_game_map_variable_name(area_id, block_id, cc_id, dd_id)
        return f"WarpToMap({game_map=}, {player_start=}, {unk_1=})"

    @parse_parameters("HandleMinibossDefeat", no_name_count=1)
    def _2003_15(self, miniboss_id):
        pass

    @parse_parameters("ForceAnimation", no_name_count=2)
    def _2003_18(
        self,
        entity: PlayerEntity,
        animation_id,
        loop: bool = False,
        wait_for_completion: bool = False,
        skip_transition: bool = False,
        unknown1=0,  # NOT just `target_comparison_type`, apparently
        unknown2=0.0,  # NOT the usual 1.0 from `target_count`
    ):
        pass

    @parse_parameters("Unknown_2003_27", no_name_count=1)
    def _2003_27(self, arg1):
        pass

    @parse_parameters("EventValueOperation")
    def _2003_41(
        self,
        source_flag,
        source_flag_bit_count,
        operand,
        target_flag,
        target_flag_bit_count,
        calculation_type: CalculationType,
    ):
        pass

    @parse_parameters("StoreItemAmountSpecifiedByFlagValue", no_name_count=2)
    def _2003_42(self, item_type: ItemType, item, flag, bit_count):
        pass

    @parse_parameters("GivePlayerItemAmountSpecifiedByFlagValue", no_name_count=2)
    def _2003_43(self, item_type: ItemType, item, flag, bit_count):
        pass

    @parse_parameters
    def _2003_44(self, state: bool):
        return self._set_state("DirectionDisplay", state)

    @parse_parameters
    def _2003_45(self, collision, level, grid_x, grid_y, state: bool):
        if state is True:
            return f"EnableMapHitGridCorrespondence({collision}, {level}, {grid_x}, {grid_y})"
        if state is False:
            return f"DisableMapHitGridCorrespondence({collision}, {level}, {grid_x}, {grid_y})"
        return f"SetMapHitGridCorrespondence({collision}, {level}, {grid_x}, {grid_y}, {state=})"

    @parse_parameters
    def _2003_46(self, content_image_part_id, state: bool):
        """No Enable/Disable wrappers."""
        return f"SetMapContentImageDisplayState({content_image_part_id}, {state=})"

    @parse_parameters
    def _2003_47(self, hierarchy, grid_x, grid_y, state: bool):
        """No Enable/Disable wrappers."""
        return f"SetMapBoundariesDisplay({hierarchy}, {grid_x}, {grid_y}, {state=})"

    @parse_parameters
    def _2003_48(self, region: Region, state: bool, duration, wind_parameter_id):
        return f"SetAreaWind({region}, {state=}, {duration=}, {wind_parameter_id=})"

    @parse_parameters("WarpPlayerToRespawnPoint", no_name_count=1)
    def _2003_49(self, respawn_point_id):
        pass

    @parse_parameters("StartEnemySpawner", no_name_count=1)
    def _2003_50(self, spawner_id):
        pass

    @parse_parameters("SummonNPC", no_name_count=3)
    def _2003_51(
        self, sign_type: SingleplayerSummonSignType, character: Character, region: Region, summon_flag, dismissal_flag
    ):
        pass

    @parse_parameters("InitializeWarpObject", no_name_count=1)
    def _2003_52(self, warp_object_id: Object):
        pass

    @parse_parameters("MakeEnemyAppear", no_name_count=1)
    def _2003_54(self, character: Character):
        pass

    @parse_parameters("SetCurrentMapCeremony")
    def _2003_57(self, ceremony_id):
        pass

    @parse_parameters
    def _2003_59(self, area_id, block_id, ceremony_id):
        game_map = self._get_game_map_variable_name(area_id, block_id)
        return f"SetMapCeremony({game_map=}, {ceremony_id=})"

    @parse_parameters("DisplayEpitaphMessage", no_name_count=1)
    def _2003_61(self, message):
        pass

    @parse_parameters("SetNetworkConnectedFlagState")
    def _2003_62(self, flag, state: FlagState):
        pass

    @parse_parameters
    def _2003_63(self, first_flag, last_flag, state: RangeState):
        flag_range = f"({first_flag}, {last_flag})"
        return f"SetNetworkConnectedFlagRangeState({flag_range}, {state=})"

    @parse_parameters("SetOmissionModeCounts")
    def _2003_64(self, level_1_count, level_2_count):
        pass
        
    @parse_parameters("ResetOmissionModeCountsToDefault")
    def _2003_65(self):
        pass

    @parse_parameters
    def _2003_66(self, flag_type: FlagType, flag, state: bool):
        """New default instruction for modifying flags (replacing 2003[02])."""
        if flag_type == FlagType.Absolute:
            return self._set_state("Flag", state, flag)
        elif flag_type == FlagType.RelativeToThisEvent:
            return self._set_state("RelativeFlag", state, flag)
        elif flag_type == FlagType.RelativeToThisEventSlot:
            return self._set_state("SlotRelativeFlag", state, flag)
        # Variable `flag_type`.
        return f"SetFlagState({flag_type}, {flag}, {state})"

    @parse_parameters("InitializeCrowTradeRegion", no_name_count=1)
    def _2003_67(self, region: Region):
        pass

    @parse_parameters("UnknownEventCommand")
    def _2003_68(self, unk_1, unk_2, unk_3):
        pass

    @parse_parameters
    def _2003_69(self, flag_type: FlagType, flag, state: bool):
        if flag_type == FlagType.Absolute and state is True:
            return f"EnableFlag_Alternate({flag})"
        elif state is False:
            return f"DisableFlag_Alternate({flag})"
        # Variable `state`.
        return f"SetFlagState_Alternate({flag_type}, {flag}, {state})"

    @parse_parameters("SetNetworkInteractionState", no_name_count=1)
    def _2003_70(self, state: bool):
        pass

    @parse_parameters
    def _2003_71(self, is_invisible):
        if is_invisible == 1:
            return f"DisableHUDVisibility()"
        elif is_invisible == 0:
            return f"EnableHUDVisibility()"
        return f"SetHUDVisibilityState({is_invisible=})"

    @parse_parameters
    def _2003_72(self, bonfire_obj: Object, animation, state: bool):
        if state is True:
            return f"EnableBonfireWarping({bonfire_obj=}, {animation=})"
        if state is False:
            return f"DisableBonfireWarping({bonfire_obj=}, {animation=})"
        return f"SetBonfireWarpingState({bonfire_obj=}, {animation=}, {state=})"

    @parse_parameters("SetAutogeneratedEventSpecificFlag_1")
    def _2003_73(self, unknown1, unknown2):
        pass

    @parse_parameters("HandleBossDefeatAndDisplayBanner")
    def _2003_74(self, boss: Character, banner: BannerType):
        pass

    @parse_parameters("SetAutogeneratedEventSpecificFlag_2")
    def _2003_75(self, unknown1, unknown2):
        pass

    @parse_parameters("SetLoadingScreenTipsState")
    def _2003_76(self, tips_disabled: bool, unk1, unk2, unk3, unk4):
        pass

    @parse_parameters("AwardGestureItem")
    def _2003_77(self, gesture_id, item_type: ItemType, item_id):
        pass

    @parse_parameters
    def _2003_78(self, character: Character):
        return f"SendNPCSummonHome({character})"

    @parse_parameters("Unknown_2003_79")
    def _2003_79(self, unknown1):
        pass

    @parse_parameters("UnknownEvent_80")
    def _2003_80(self, unk_1):
        pass

    @parse_parameters("UnknownEvent_81")
    def _2003_81(self, unk_1):
        pass

    @parse_parameters("AddSpecialEffect", no_name_count=2)
    def _2004_08(self, character: Character, special_effect_id):
        pass

    @parse_parameters("RotateToFaceEntity", no_name_count=2)
    def _2004_14(
        self,
        character: Character,
        target_entity: Union[Character, Object, Region],
        animation,
        wait_for_completion: bool,
    ):
        pass

    @parse_parameters("ChangeCharacterCloth", no_name_count=1)
    def _2004_48(self, character: Character, bit_count, state_id):
        pass

    @parse_parameters("ChangePatrolBehavior", no_name_count=1)
    def _2004_49(self, character: Character, patrol_information_id):
        pass

    @parse_parameters("SetLockOnPoint", no_name_count=1)
    def _2004_50(self, character: Character, lock_on_model_point, state: bool):
        pass

    @parse_parameters("Test_RequestRagdollRestraint")
    def _2004_51(
        self,
        recipient_character: Character,
        recipient_target_rigid_index,
        recipient_model_point,
        attachment_character: Character,
        attachment_target_rigid_index,
        attachment_model_point,
    ):
        pass

    @parse_parameters("ChangePlayerCharacterInitParam", no_name_count=1)
    def _2004_52(self, character_init_param):
        pass

    @parse_parameters("AdaptSpecialEffectHealthChangeToNPCPart", no_name_count=1)
    def _2004_53(self, character: Character):
        pass

    @parse_parameters("ImmediateActivate")
    def _2004_54(self, character: Character, state: bool):
        pass

    @parse_parameters("SetCharacterTalkRange", no_name_count=1)
    def _2004_55(self, character: Character, distance):
        pass

    @parse_parameters("IncrementCharacterNewGameCycle", no_name_count=1)
    def _2004_57(self, character: Character):
        pass

    @parse_parameters("SetMultiplayerBuffs_NonBoss", no_name_count=1)
    def _2004_58(self, character: Character, state: bool):
        pass

    @parse_parameters("Unknown_2004_59", no_name_count=1)
    def _2004_59(self, character: Character, state: bool):
        pass

    @parse_parameters("SetPlayerRemainingYoelLevels")
    def _2004_60(self, level_count):
        pass

    @parse_parameters("UnknownCharacter_68")
    def _2004_68(self, character: Character, unk_1, unk_2):
        pass

    @parse_parameters("UnknownCharacter_73")
    def _2004_73(self, character: Character, unk_1):
        pass

    @parse_parameters("UnknownCharacter_74")
    def _2004_74(self, character: Character, unk_1, region: Region, unk_2, character_2: Character, unk_3, unk_4):
        pass

    @parse_parameters("UnknownCharacter_75")
    def _2004_75(self, character: Character, unk_1, unk_2):
        pass

    @parse_parameters("UnknownCharacter_76")
    def _2004_76(self, flag, item_lot):
        pass

    @parse_parameters("UnknownCharacter_77")
    def _2004_77(self, unk_1, unk_2, unk_3, unk_4):
        pass

    @parse_parameters("ExtinguishBurningObjects")
    def _2005_16(self):
        pass

    @parse_parameters("ShowObjectByMapCeremony")
    def _2005_17(self, obj: Object, ceremony_id, unknown):
        pass

    @parse_parameters("DestroyObject_NoSlot")
    def _2005_19(self, obj: Object):
        pass

    @parse_parameters("SetUnknownVFX_06")
    def _2006_06(self, vfx_id):
        pass

    @parse_parameters("DisplayDialogAndSetFlags")
    def _2007_10(
        self,
        message,
        button_type: ButtonType,
        number_buttons: NumberButtons,
        anchor_entity: Union[Character, Object, Region],
        display_distance,
        left_flag,
        right_flag,
        cancel_flag,
    ):
        pass

    @parse_parameters("DisplayAreaWelcomeMessage", no_name_count=1)
    def _2007_11(self, message):
        pass

    @parse_parameters("DisplayHollowArenaMessage", no_name_count=1)
    def _2007_12(self, message, unknown, pad_enabled: bool):
        pass

    @parse_parameters("DisplayTutorialMessage")
    def _2007_15(self, tutorial_param_id, unk_1: bool, unk_2: bool):
        pass

    @parse_parameters("DisplayUnknownMessage_16")
    def _2007_16(self, unk_1, unk_2):
        pass

    @parse_parameters("UnknownCameraCommand")
    def _2008_04(self, unk_1, unk_2):
        pass

    @parse_parameters("RegisterLantern", no_name_count=2)
    def _2009_05(self, flag, obj: Object, reaction_distance, reaction_angle, initial_sword_number, sword_level):
        pass

    @parse_parameters("BanishInvaders")
    def _2009_08(self, unknown):
        pass

    @parse_parameters("BanishPhantomsAndUpdateServerPvPStats")
    def _2009_10(self, unknown):
        pass

    @parse_parameters("BanishPhantoms")
    def _2009_11(self, unknown):
        pass

    @parse_parameters
    def _2010_04(self, sound_id: SoundEvent, state: bool):
        return self._set_state("BossMusic", state, entity=sound_id)

    @parse_parameters("NotifyDoorEventSoundDampening", no_name_count=1)
    def _2010_05(self, entity_id: Object, state: DoorState):
        pass

    @parse_parameters
    def _2010_06(self, sound_id: SoundEvent, state: bool, fade_duration):
        if state is True:
            return f"EnableSoundEventWithFade({sound_id=}, {fade_duration=})"
        elif state is False:
            return f"DisableSoundEventWithFade({sound_id=}, {fade_duration=})"
        return f"SetSoundEventWithFade({sound_id=}, {state=}, {fade_duration=})"

    @parse_parameters("SuppressSoundEvent")
    def _2010_07(self, sound_id: SoundEvent, unk_1, is_suppressed: bool):
        pass

    @parse_parameters("SetCollisionResState")
    def _2011_03(self, collision: Collision, state: bool):
        pass

    @parse_parameters("ActivateCollisionAndCreateNavmesh")
    def _2011_04(self, collision: Collision, state: bool):
        pass

    @parse_parameters
    def _2012_08(self, state: bool):
        if state is True:
            return "EnableAreaWelcomeMessage()"
        elif state is False:
            return "DisableAreaWelcomeMessage()"
        return f"SetAreaWelcomeMessageState({state=})"

    @parse_parameters("UnknownMap_12")
    def _2012_12(self, unk_1):
        pass

    @parse_parameters("CreatePlayLog", no_name_count=1)
    def _2013_01(self, name_string):
        pass

    @parse_parameters("StartPlayLogMeasurement", no_name_count=2)
    def _2013_02(self, measurement_id, name_string, overwrite: bool):
        pass

    @parse_parameters("StopPlayLogMeasurement", no_name_count=1)
    def _2013_03(self, measurement_id):
        pass

    @parse_parameters("PlayLogParameterOutput", no_name_count=3)
    def _2013_04(self, category: PlayerPlayLogParameter, name_string, output_multiplayer_state: PlayLogMultiplayerType):
        pass
