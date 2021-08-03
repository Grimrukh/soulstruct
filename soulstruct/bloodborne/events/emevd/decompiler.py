__all__ = ["InstructionDecompiler"]

import typing as tp

from soulstruct.base.events.emevd.decompiler import InstructionDecompiler as _BaseDecompiler, parse_parameters
from soulstruct.bloodborne.maps.constants import get_map
from soulstruct.game_types.msb_types import *
from .enums import *
from . import enums


class InstructionDecompiler(_BaseDecompiler):

    ENUMS = enums
    GET_MAP = staticmethod(get_map)

    @parse_parameters
    def _3_23(self, condition, attacked_entity: Character, attacker: Character, damage_type: DamageType):
        if not self._any_vars(damage_type) and damage_type.name == "Unspecified":
            # Leave out default `damage_type` value.
            if attacker == -1:
                return f"IfAttackedWithDamageType({condition}, {attacked_entity=})"
            return f"IfAttackedWithDamageType({condition}, {attacked_entity=}, {attacker=})"
        if attacker == -1:
            return f"IfAttackedWithDamageType({condition}, {attacked_entity=}, {damage_type=})"
        return f"IfAttackedWithDamageType({condition}, {attacked_entity=}, {attacker=}, {damage_type=})"

    @parse_parameters("IfActionButtonParam", no_name_count=1)
    def _3_24(self, condition, action_button_id, entity: tp.Union[Character, Object, Region]):
        pass

    @parse_parameters("IfPlayerArmorType", no_name_count=1)
    def _3_25(self, condition, armor_type: ArmorType, required_armor_range_first, required_armor_range_last):
        pass

    @parse_parameters
    def _3_26(self, condition, value, comparison_type: ComparisonType):
        if self._any_vars(comparison_type):
            return f"IfPlayerInsightAmountComparison({condition}, {value}, {comparison_type=})"
        return f"IfPlayerInsightAmount{comparison_type.name}({condition}, {value})"

    @parse_parameters("IfDialogChoice", no_name_count=2)
    def _3_27(self, condition, dialog_result: DialogResult):
        pass

    @parse_parameters("IfPlayGoState", no_name_count=2)
    def _3_28(self, condition, playgo_state: PlayGoState):
        pass

    @parse_parameters("IfClientTypeCountComparison", no_name_count=3)
    def _3_29(self, condition, client_type: ClientType, comparison_type: ComparisonType, value):
        pass

    @parse_parameters
    def _4_15(self, condition, character: Character, state: bool):
        if state is True:
            return f"IfCharacterDrawGroupActive({condition}, {character})"
        if state is False:
            return f"IfCharacterDrawGroupInactive({condition}, {character})"
        return f"IfCharacterDrawGroupState({condition}, {character}, {state=})"

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

    @parse_parameters("SkipLinesIfCoopClientCountComparison", no_name_count=3)
    def _1003_09(self, skip_lines, comparison_type: ComparisonType, value):
        pass

    @parse_parameters
    def _1003_10(self, event_return_type: EventReturnType, comparison_type: ComparisonType, value):
        if not self._any_vars(event_return_type):
            return f"{event_return_type.name}IfCoopClientCountComparison({comparison_type}, {value})"
        return f"ReturnIfCoopClientCountComparison({event_return_type}, {comparison_type}, {value})"

    @parse_parameters("SkipLinesIfPlayerGender", no_name_count=2)
    def _1003_11(self, skip_lines, gender: Gender):
        pass

    @parse_parameters("GotoIfPlayerGender", no_name_count=2)
    def _1003_12(self, label: Label, gender: Gender):
        pass

    @parse_parameters
    def _1003_13(self, event_return_type: EventReturnType, gender: Gender):
        if not self._any_vars(event_return_type):
            return f"{event_return_type.name}IfPlayerGender({gender})"
        return f"ReturnIfPlayerGender({event_return_type}, {gender})"

    @parse_parameters("SkipLinesIfClientTypeCountComparison", no_name_count=4)
    def _1003_14(self, skip_lines, client_type: ClientType, comparison_type: ComparisonType, value):
        pass

    @parse_parameters("GotoIfClientTypeCountComparison", no_name_count=4)
    def _1003_15(self, label: Label, client_type: ClientType, comparison_type: ComparisonType, value):
        pass

    @parse_parameters
    def _1003_16(
        self, event_return_type: EventReturnType, client_type: ClientType, comparison_type: ComparisonType, value
    ):
        if not self._any_vars(event_return_type):
            return f"{event_return_type.name}IfClientTypeCountComparison({client_type}, {comparison_type}, {value})"
        return f"ReturnIfClientTypeCountComparison({event_return_type}, {client_type}, {comparison_type}, {value})"

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
    def _1005_101(self, label: Label, obj: Object, state: bool):
        if state is True:
            return f"GotoIfObjectDestroyed({label}, {obj})"
        if state is False:
            return f"GotoIfObjectNotDestroyed({label}, {obj})"
        return f"GotoIfObjectDestructionState({label}, {obj}, {state=})"

    @parse_parameters
    def _1014_00(self):
        return "DefineLabel(0)"

    @parse_parameters
    def _1014_01(self):
        return "DefineLabel(1)"

    @parse_parameters
    def _1014_02(self):
        return "DefineLabel(2)"

    @parse_parameters
    def _1014_03(self):
        return "DefineLabel(3)"

    @parse_parameters
    def _1014_04(self):
        return "DefineLabel(4)"

    @parse_parameters
    def _1014_05(self):
        return "DefineLabel(5)"

    @parse_parameters
    def _1014_06(self):
        return "DefineLabel(6)"

    @parse_parameters
    def _1014_07(self):
        return "DefineLabel(7)"

    @parse_parameters
    def _1014_08(self):
        return "DefineLabel(8)"

    @parse_parameters
    def _1014_09(self):
        return "DefineLabel(9)"

    @parse_parameters
    def _2002_06(
        self,
        cutscene,
        cutscene_type: CutsceneType,
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
    def _2002_07(self, cutscene, cutscene_type: CutsceneType, player_id: PlayerEntity, time_period_id):
        pass

    @parse_parameters
    def _2002_08(self, region: Region, area_id, block_id):
        move_to_map = self._get_game_map_variable_name(area_id, block_id)
        return f"PlayCutsceneAndMovePlayer_Dummy({region}, {move_to_map=})"

    @parse_parameters("HandleMinibossDefeat", no_name_count=1)
    def _2003_15(self, miniboss_id: Character):
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
    def _2003_45(self, collision: Collision, level, grid_x, grid_y, state: bool):
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
    def _2003_49(self, respawn_point_id: SpawnPointEvent):
        pass

    @parse_parameters("StartEnemySpawner", no_name_count=1)
    def _2003_50(self, spawner_id):
        pass

    @parse_parameters("SummonNPC", no_name_count=3)
    def _2003_51(
        self,
        sign_type: SingleplayerSummonSignType,
        character: PlayerEntity,
        region: Region,
        summon_flag,
        dismissal_flag,
    ):
        pass

    @parse_parameters("InitializeWarpObject", no_name_count=1)
    def _2003_52(self, warp_object_id):
        pass

    @parse_parameters("BossDefeat", no_name_count=2)
    def _2003_53(self, boss_id: Character, banner_type: BannerType):
        pass

    @parse_parameters("SendNPCSummonHome", no_name_count=1)
    def _2003_54(self, character: Character):
        pass

    @parse_parameters("AddSpecialEffect", no_name_count=2)
    def _2004_08(self, character: Character, special_effect_id, affect_npc_part_hp: bool):
        pass

    @parse_parameters("RotateToFaceEntity", no_name_count=2)
    def _2004_14(self, character: Character, target_entity: Character, animation, wait_for_completion: bool = False):
        pass

    @parse_parameters("ChangeCharacterCloth", no_name_count=2)
    def _2004_48(self, character: Character, bit_count, state_id):
        pass

    @parse_parameters("ChangePatrolBehavior", no_name_count=1)
    def _2004_49(self, character: Character, patrol_information_id):
        pass

    @parse_parameters("SetDistanceLimitForConversationStateChanges", no_name_count=1)
    def _2004_50(self, character: Character, distance):
        pass

    @parse_parameters("Test_RequestRagdollRestraint", no_name_count=6)
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

    @parse_parameters("SetGravityAndCollisionExcludingOwnWorld", no_name_count=2)
    def _2004_54(self, character: Character, state: bool):
        pass

    @parse_parameters("AddSpecialEffect_WithUnknownEffect", no_name_count=2)
    def _2004_55(self, character: Character, speffect, affect_npc_parts_hp: bool):
        pass

    @parse_parameters("ActivateObjectWithSpecificCharacter", no_name_count=1)
    def _2005_16(self, obj: Object, objact_id, relative_index, character: Character):
        pass

    @parse_parameters("SetObjectDamageShieldState", no_name_count=1)
    def _2005_17(self, obj: Object, state: bool):
        pass

    @parse_parameters("RegisterLantern", no_name_count=2)
    def _2009_05(self, flag, obj: Object, reaction_distance, reaction_angle, initial_sword_number, sword_level):
        pass

    @parse_parameters
    def _2010_04(self, sound_id, state: bool):
        return self._set_state("BossMusic", state, entity=sound_id)

    @parse_parameters("NotifyDoorEventSoundDampening", no_name_count=1)
    def _2010_05(self, entity_id: Object, state: DoorState):
        pass

    @parse_parameters("SetCollisionResState", no_name_count=1)
    def _2011_03(self, collision: Collision, state: bool):
        return

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
