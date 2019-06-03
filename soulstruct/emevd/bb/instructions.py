""" Full instruction set for BB. """

from __future__ import annotations
from soulstruct.emevd.shared.instructions import *
from soulstruct.emevd.game_types import *
from soulstruct.emevd.bb.enums import *


def format_instruction(event_format, *args):
    event_args = []
    arg_loads = []
    for i, arg in enumerate(args):
        if isinstance(arg, Enum):
            event_args.append(args[i].value)
        elif isinstance(arg, bool):
            event_args.append(int(arg))
        elif isinstance(arg, tuple):
            # Start offset and size of an event argument.
            write_offset = get_write_offset(event_format[2], i)
            arg_loads.append(f'    ^({write_offset} <- {arg[0]}, {arg[1]})')
            if len(event_format) == 4:
                # Use optional dummy dictionary.
                event_args.append(event_format[3][i])
            else:
                event_args.append(0)
        else:
            event_args.append(arg)
    return [f' {event_format[0]}[{event_format[1]}] ({event_format[2]}){event_args}'] + arg_loads


def IfDamageType(condition: int, attacked_character: CharacterInt, attacking_character: CharacterInt,
                 damage_type: DamageType):
    """ Similar to IsAttackedBy, but requires a certain damage type. """
    event_format = ('   3', '23', 'biiB', [0, 0, -1, 0])
    return format_instruction(event_format, condition, attacked_character, attacking_character, damage_type)


def IfActionButtonInRegion(condition: int, action_button_id: int, region: RegionInt):
    """ Probably a simplified version of IfDialogPromptActivated. """
    event_format = ('   3', '24', 'bii', [0, -1, -1])
    return format_instruction(event_format, condition, action_button_id, region)


def IfPlayerArmorType(condition: int, armor_type: ArmorType, required_armor_range_first: ArmorInt,
                      required_armor_range_last: ArmorInt):
    event_format = ('   3', '25', 'bBii', [0, ])
    return format_instruction(event_format, condition, armor_type, required_armor_range_first,
                              required_armor_range_last)


def IfPlayerInsightAmountComparison(condition: int, value: int, comparison_type: ComparisonType):
    """ Note change in argument order. """
    event_format = ('   3', '26', 'bBb', [0, 0, 0])
    return format_instruction(event_format, condition, value, comparison_type)

def IfPlayerInsightAmountEqual(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.Equal)

def IfPlayerInsightAmountNotEqual(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.NotEqual)

def IfPlayerInsightAmountGreaterThan(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.GreaterThan)

def IfPlayerInsightAmountLessThan(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.LessThan)

def IfPlayerInsightAmountGreaterThanOrEqual(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.GreaterThanOrEqual)

def IfPlayerInsightAmountLessThanOrEqual(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.LessThanOrEqual)


def IfDialogChoice(condition: int, dialog_result: DialogResult):
    event_format = ('   3', '27', 'bb', [0, 0])
    return format_instruction(event_format, condition, dialog_result)


def IfPlayGoState(condition: int, playgo_state: PlayGoState):
    """ No idea what PlayGo state is but this doesn't sound like it would be used very often. """
    event_format = ('   3', '28', 'bb', [0, 0])
    return format_instruction(event_format, condition, playgo_state)


def IfClientTypeCountComparison(condition: int, client_type: ClientType, comparison_type: ComparisonType, value):
    """ Value should only range between 0 and 4 (the maximum number of clients). """
    event_format = ('   3', '29', 'bBBB', [0, 0, 0, 0])
    return format_instruction(event_format, condition, client_type, comparison_type, value)


def IfCharacterDrawGroupState(condition: int, character: CharacterInt, state: bool):
    """ Tests if character's draw group is currently active or inactive. """
    event_format = ('   4', '15', 'biB', [0, 0, 0])
    return format_instruction(event_format, condition, character, state)

def IfCharacterDrawGroupActive(condition: int, character: CharacterInt):
    return IfCharacterDrawGroupState(condition, character, True)

def IfCharacterDrawGroupInactive(condition: int, character: CharacterInt):
    return IfCharacterDrawGroupState(condition, character, False)


def GotoIfConditionState(label: Label, required_state: bool, input_condition: int):
    event_format = ('1000', '101', 'BBb', [0, 0, 0])
    return format_instruction(event_format, label, required_state, input_condition)

def GotoIfConditionTrue(label: Label, input_condition: int):
    return GotoIfConditionState(label, True, input_condition)

def GotoIfConditionFalse(label: Label, input_condition: int):
    return GotoIfConditionState(label, False, input_condition)

def Goto(label: Label):
    """ Unconditional GOTO. """
    event_format = ('1000', '103', 'B', [0])
    return format_instruction(event_format, label)

def GotoIfValueComparison(label: Label, comparison_type: ComparisonType, left: int, right: int):
    event_format = ('1000', '105', 'Bbii')
    return format_instruction(event_format, label, comparison_type, left, right)

def GotoIfFinishedConditionState(label: Label, required_state: bool, input_condition: int):
    """ Finished version. """
    event_format = ('1000', '107', 'BBb', [0, 0, 0])
    return format_instruction(event_format, label, required_state, input_condition)

def GotoIfFinishedConditionTrue(label: Label, input_condition: int):
    return GotoIfFinishedConditionState(label, True, input_condition)

def GotoIfFinishedConditionFalse(label: Label, input_condition: int):
    return GotoIfFinishedConditionState(label, False, input_condition)

def SkipLinesIfCoopClientCountComparison(skip_lines: int, comparison_type: ComparisonType, value: int):
    """ Value should be from 0 to 4. """
    event_format = ('1003', '09', 'BBB', [0, 0, 0])
    return format_instruction(event_format, skip_lines, comparison_type, value)

def TerminateIfCoopClientCountComparison(event_end_type: EventEndType, comparison_type: ComparisonType, value: int):
    event_format = ('1003', '10', 'BBB', [0, 0, 0])
    return format_instruction(event_format, event_end_type, comparison_type, value)

def EndIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return TerminateIfCoopClientCountComparison(EventEndType.End, comparison_type, value)

def RestartIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return TerminateIfCoopClientCountComparison(EventEndType.Restart, comparison_type, value)


def SkipLinesIfPlayerGender(skip_lines: int, gender: Gender):
    event_format = ('1003', '11', 'BB')
    return format_instruction(event_format, skip_lines, gender)

def GotoIfPlayerGender(label: Label, gender: Gender):
    event_format = ('1003', '12', 'BB')
    return format_instruction(event_format, label, gender)

def TerminateIfPlayerGender(event_end_type: EventEndType, gender: Gender):
    event_format = ('1003', '13', 'BB')
    return format_instruction(event_format, event_end_type, gender)

def EndIfPlayerGender(gender: Gender):
    return TerminateIfPlayerGender(EventEndType.End, gender)

def RestartIfPlayerGender(gender: Gender):
    return TerminateIfPlayerGender(EventEndType.Restart, gender)


def SkipLinesIfClientTypeCountComparison(skip_lines: int, client_type: ClientType, comparison_type: ComparisonType,
                                         value: int):
    """ Value from 0 to 4. """
    event_format = ('1003', '14', 'BBBB', [0, 0, 0, 0])
    return format_instruction(event_format, skip_lines, client_type, comparison_type, value)

def GotoIfClientTypeCountComparison(label: Label, client_type: ClientType, comparison_type: ComparisonType,
                                    value: int):
    """ Value from 0 to 4. """
    event_format = ('1003', '15', 'BBBB', [0, 0, 0, 0])
    return format_instruction(event_format, label, client_type, comparison_type, value)

def TerminateIfClientTypeCountComparison(event_end_type: EventEndType, client_type: ClientType,
                                         comparison_type: ComparisonType, value: int):
    """ Value from 0 to 4. """
    event_format = ('1003', '16', 'BBBB', [0, 0, 0, 0])
    return format_instruction(event_format, event_end_type, client_type, comparison_type, value)

def EndIfClientTypeCountComparison(client_type: ClientType, comparison_type: ComparisonType, value: int):
    """ Value from 0 to 4. """
    return TerminateIfClientTypeCountComparison(EventEndType.End, client_type, comparison_type, value)

def RestartIfClientTypeCountComparison(client_type: ClientType, comparison_type: ComparisonType, value: int):
    """ Value from 0 to 4. """
    return TerminateIfClientTypeCountComparison(EventEndType.Restart, client_type, comparison_type, value)


def GotoIfFlagState(label: Label, state: bool, flag_type: FlagType, flag: FlagInt):
    event_format = ('1003', '101', 'BBBi')
    return format_instruction(event_format, label, state, flag_type, flag)

def GotoIfThisEventOn(label: Label):
    return GotoIfFlagState(label, True, FlagType.RelativeToThisEvent, 0)

def GotoIfThisEventOff(label: Label):
    return GotoIfFlagState(label, False, FlagType.RelativeToThisEvent, 0)

def GotoIfThisEventSlotOn(label: Label):
    return GotoIfFlagState(label, True, FlagType.RelativeToThisEventSlot, 0)

def GotoIfThisEventSlotOff(label: Label):
    return GotoIfFlagState(label, False, FlagType.RelativeToThisEventSlot, 0)

def GotoIfFlagOn(label: Label, flag: FlagInt):
    return GotoIfFlagState(label, True, FlagType.Absolute, flag)

def GotoIfFlagOff(label: Label, flag: FlagInt):
    return GotoIfFlagState(label, False, FlagType.Absolute, flag)


def GotoIfFlagRangeState(label: Label, state: RangeState, flag_type: FlagType,
                         flag_range: FlagRangeOrSequence):
    event_format = ('1003', '103', 'BBBii')
    first_flag, last_flag = resolve_flag_range(flag_range)
    return format_instruction(event_format, label, state, flag_type, first_flag, last_flag)

def GotoIfFlagRangeAllOn(label: Label, flag_range: FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AllOn, FlagType.Absolute, flag_range)

def GotoIfFlagRangeAllOff(label: Label, flag_range: FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AllOff, FlagType.Absolute, flag_range)

def GotoIfFlagRangeAnyOn(label: Label, flag_range: FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AnyOn, FlagType.Absolute, flag_range)

def GotoIfFlagRangeAnyOff(label: Label, flag_range: FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AnyOff, FlagType.Absolute, flag_range)


def GotoIfMultiplayerState(label: Label, state: MultiplayerState):
    event_format = ('1003', '105', 'Bb', [0, 0])
    return format_instruction(event_format, label, state)

def GotoIfHost(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Host)

def GotoIfClient(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Client)

def GotoIfMultiplayer(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Multiplayer)

def GotoIfConnectingMultiplayer(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.ConnnectingMultplayer)

def GotoIfSingleplayer(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Singleplayer)


def GotoIfMapPresenceState(label: Label, game_map: GameMap, state: bool):
    event_format = ('1003', '107', 'BBBB', [0, 0, 0, 0])
    area_id, block_id = tuple(game_map)
    return format_instruction(event_format, label, state, area_id, block_id)

def GotoIfInsideMap(label: Label, game_map: GameMap):
    return GotoIfMapPresenceState(label, game_map, True)

def GotoIfOutsideMap(label: Label, game_map: GameMap):
    return GotoIfMapPresenceState(label, game_map, False)


def GotoIfCoopClientCountComparison(label: Label, comparison_type: ComparisonType, value: int):
    event_format = ('1003', '109', 'BBB', [0, 0, 0])
    return format_instruction(event_format, label, comparison_type, value)


def GotoIfObjectDestructionState(label: Label, obj: ObjectInt, state: bool):
    """ Note change in argument order. """
    event_format = ('1005', '101', 'BBi', [0, 0, -1])
    return format_instruction(event_format, label, state, obj)

def GotoIfObjectDestroyed(label: Label, obj: ObjectInt):
    return GotoIfObjectDestructionState(label, obj, True)

def GotoIfObjectNotDestroyed(label: Label, obj: ObjectInt):
    return GotoIfObjectDestructionState(label, obj, False)


# MULTIPLAYER

def SkipLinesIfMultiplayerState(line_count, state: MultiplayerState):
    event_format = ('1003', '05', 'Bb')
    return format_instruction(event_format, line_count, state)

def SkipLinesIfHost(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Host)

def SkipLinesIfClient(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Client)

def SkipLinesIfMultiplayer(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Multiplayer)

def SkipLinesIfConnectingMultiplayer(skip_lines: int):
    return SkipLinesIfMultiplayerState(skip_lines, MultiplayerState.ConnectingMultiplayer)


def SkipLinesIfSingleplayer(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Singleplayer)

def TerminateIfMultiplayerState(event_end_type: EventEndType, state: MultiplayerState):
    event_format = ('1003', '06', 'Bb')
    return format_instruction(event_format, event_end_type, state)

def EndIfHost():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Host)

def EndIfClient():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Client)

def EndIfMultiplayer():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Multiplayer)

def EndIfSingleplayer():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Singleplayer)

def RestartIfHost():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Host)

def RestartIfClient():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Client)

def RestartIfMultiplayer():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Multiplayer)

def RestartIfSingleplayer():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Singleplayer)

def IfMultiplayerState(condition: int, state: MultiplayerState):
    event_format = ['   3', '06', 'bb']
    return format_instruction(event_format, condition, state)

def IfHost(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Host)

def IfClient(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Client)

def IfMultiplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Multiplayer)

def IfConnectingMultiplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.ConnectingMultiplayer)

def IfSingleplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Singleplayer)


def Label(label: Union[Label, int]):
    if isinstance(Label, int) and not 0 <= label <= 9:
        raise ValueError("Label index must be between 0 and 9, inclusive.")
    event_format = ('1014', f'{label:02d}', '')
    return format_instruction(event_format)


def PlayCutsceneAndMovePlayerAndSetTimePeriod(cutscene: int, cutscene_type: CutsceneType, region: RegionInt,
                                              game_map: GameMap, player_entity_id: int, time_period_id: int):
    """ Warp a particular player to a region and set the time period. I assume that this must be a map that is
    already loaded, like in DS1, but possibly not.

    It's probably used to warp to Bergenwerth after Rom, so either that map is already loaded when you defeat Rom, or
    this event *is* capable of warping to an entirely new map.
    """
    event_format = ('2002', '06', 'iIiBBiB')
    area_id, block_id = tuple(game_map)
    return format_instruction(event_format, cutscene, cutscene_type, region, area_id, block_id, player_entity_id,
                              time_period_id)


def PlayCutsceneAndSetTimePeriod(cutscene: int, cutscene_type: CutsceneType, player_entity_id: int,
                                 time_period_id: int):
    """ Probably used when you examine Laurence's skull, etc. """
    event_format = ('2002', '07', 'iIiB', [-1, 0, -1, 0])
    return format_instruction(event_format, cutscene, cutscene_type, player_entity_id, time_period_id)


def PlayCutsceneAndMovePlayer_Dummy(region: RegionInt, game_map: GameMap):
    """ Likely not used, doesn't even take a cutscene ID argument. """
    event_format = ('2002', '08', 'iBB', [0, 0, 0])
    area_id, block_id = tuple(game_map)
    return format_instruction(event_format, region, area_id, block_id)


def SetBossHealthBarState(character: CharacterInt, name: TextInt, slot, state: bool):
    """ Note: slot number can be 0-2 in Bloodborne. """
    event_format = ('2003', '11', 'bihi')
    if isinstance(slot, int) and slot not in (0, 1, 2):
        raise ValueError("Boss health bar slot must be 0, 1, or 2.")
    return format_instruction(event_format, state, character, slot, name)

def EnableBossHealthBar(character: CharacterInt, name: TextInt, slot=0):
    """ The character's health bar will appear at the bottom of the screen, with a name. """
    return SetBossHealthBarState(character, name, slot, True)

def DisableBossHealthBar(character: CharacterInt, name: TextInt = 0, slot=0):
    """ The character's health bar will disappear from the bottom of the screen.

    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter, so only the
    first argument actually does anything. You're welcome to specify the name for clarity anyway (and vanilla events
    will show it when decompiled). """
    return SetBossHealthBarState(character, name, slot, False)


def HandleMinibossDefeat(miniboss_id: int):
    event_format = ('2003', '15', 'i', [0])
    return format_instruction(event_format, miniboss_id)


def Unknown_2003_27(arg1: int):
    """ No information. """
    event_format = ('2003', '27', 'B')
    return format_instruction(event_format, arg1)


def EventValueOperation(source_flag: FlagInt, source_flag_bit_count: int, operand: int, target_flag: FlagInt,
                        target_flag_bit_count: int, calculation_type: CalculationType):
    """ Performs a binary operation on the source flag and operand value, and stores the result in the target flag. """
    event_format = ('2003', '41', 'iIiiIb')
    return format_instruction(event_format, source_flag, source_flag_bit_count, operand, target_flag,
                              target_flag_bit_count, calculation_type)


def StoreItemAmountSpecifiedByFlagValue(item_type: ItemType, item: ItemInt, flag: FlagInt, bit_count: int):
    """ Stores some amount of items read from a flag array. """
    event_format = ('2003', '42', 'iiiI')
    return format_instruction(event_format, item_type, item, flag, bit_count)

def GivePlayerItemAmountSpecifiedByFlagValue(item_type: ItemType, item: ItemInt, flag: FlagInt, bit_count: int):
    """ Gives player some amount of items read from a flag array. Probably used when taking items out of storage
    (i.e. the reverse of the above instruction). """
    event_format = ('2003', '43', 'iiiI')
    return format_instruction(event_format, item_type, item, flag, bit_count)


def SetDirectionDisplayState(state: bool):
    """ Not sure what this is. """
    event_format = ('2003', '44', 'B')
    return format_instruction(event_format, state)

def EnableDirectionDisplay():
    return SetDirectionDisplayState(True)

def DisableDirectionDisplay():
    return SetDirectionDisplayState(False)


def SetMapHitGridCorrespondence(hitbox: HitboxInt, level: int, grid_coord_x: int, grid_coord_y: int, state: bool):
    event_format = ('2003', '45', 'ihhhB')
    return format_instruction(event_format, hitbox, level, grid_coord_x, grid_coord_y, state)

def EnableMapHitGridCorrespondence(hitbox: HitboxInt, level: int, grid_coord_x: int, grid_coord_y: int):
    return SetMapHitGridCorrespondence(hitbox, level, grid_coord_x, grid_coord_y, True)

def DisableMapHitGridCorrespondence(hitbox: HitboxInt, level: int, grid_coord_x: int, grid_coord_y: int):
    return SetMapHitGridCorrespondence(hitbox, level, grid_coord_x, grid_coord_y, False)


def SetMapContentImageDisplayState(content_image_part_id: int, state: bool):
    event_format = ('2003', '46', 'hB')
    return format_instruction(event_format, content_image_part_id, state)


def SetMapBoundariesDisplay(hierarchy: int, grid_coord_x: int, grid_coord_y: int, state: bool):
    event_format = ('2003', '47', 'hhhB')
    return format_instruction(event_format, hierarchy, grid_coord_x, grid_coord_y, state)


def SetAreaWind(region: RegionInt, state: bool, duration: float, wind_parameter_id: int):
    event_format = ('2003', '48', 'iBfi')
    return format_instruction(event_format, region, state, duration, wind_parameter_id)


def MovePlayerToRespawnPoint(respawn_point_id: int):
    event_format = ('2003', '49', 'i', [0])
    return format_instruction(event_format, respawn_point_id)


def StartEnemySpawner(spawner_id: int):
    event_format = ('2003', '50', 'i', [-1])
    return format_instruction(event_format, spawner_id)


def SummonNPC(sign_type: Union[SingleplayerSummonSignType, int], character: CharacterInt, region: RegionInt,
              summon_flag: FlagInt, dismissal_flag: FlagInt):
    event_format = ('2003', '51', 'iiiii')
    return format_instruction(event_format, sign_type, character, region, summon_flag, dismissal_flag)


def InitializeWarpObject(warp_object_id: int):
    event_format = ('2003', '52', 'i', [0])
    return format_instruction(event_format, warp_object_id)


def BossDefeat(boss_id: int, banner_type: BannerType):
    """ Handle boss defeat and display banner. 'boss_id' is probably similar to GameAreaParam from DS1. """
    event_format = ('2003', '53', 'ib')
    return format_instruction(event_format, boss_id, banner_type)


def SendNPCSummonHome(character: CharacterInt):
    event_format = ('2003', '54', 'i', [-1])
    return format_instruction(event_format, character)


def AddSpecialEffect(character: CharacterInt, special_effect_id: int, affect_npc_part_hp: bool):
    """ 'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will do
    nothing if the character already has the special effect active (i.e. they do not stack or even reset timers).

    The Bloodborne version has an additional argument that determines whether any HP changes caused by the special
    effect should also affect NPC parts.
    """
    event_format = ('2004', '08', 'iiB')
    return format_instruction(event_format, character, special_effect_id, affect_npc_part_hp)


def RotateToFaceEntity(character: CharacterInt, target_entity: MapEntityInt, animation: int,
                       wait_for_completion: bool = False):
    """ Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at least.)

    The Bloodborne version allows you to force an animation at the same time and optionally wait until that animation
    is completed. (I assume a value of -1 avoids it.)
    """
    event_format = ('2004', '14', 'iiiB', [0, 0, -1, 0])
    return format_instruction(event_format, character, target_entity, animation, wait_for_completion)


def ChangeCharacterCloth(character: CharacterInt, bit_count: int, state_id: int):
    event_format = ('2004', '48', 'iBB', [0, 0, 0])
    return format_instruction(event_format, character, bit_count, state_id)


def ChangePatrolBehavior(character: CharacterInt, patrol_information_id: int):
    """ I don't know what a 'patrol_information_id' actually is. """
    event_format = ('2004', '49', 'ii', [0, -1])
    return format_instruction(event_format, character, patrol_information_id)


def SetDistanceLimitForConversationStateChanges(character: CharacterInt, distance: float):
    event_format = ('2004', '50', 'if')
    return format_instruction(event_format, character, distance)


def Test_RequestRagdollRestraint(recipient_character: CharacterInt, recipient_target_rigid_index: int,
                                 recipient_model_point: int, attachment_character: CharacterInt,
                                 attachment_target_rigid_index: int, attachment_model_point: int):
    event_format = ('2004', '51', 'iiiiii')
    return format_instruction(event_format, recipient_character, recipient_target_rigid_index, recipient_model_point,
                              attachment_character, attachment_target_rigid_index, attachment_model_point)


def ChangePlayerCharacterInitParam(character_init_param: int):
    """ I assume this affects the player. """
    event_format = ('2004', '52', 'i', [0])
    return format_instruction(event_format, character_init_param)


def AdaptSpecialEffectHealthChangeToNPCPart(character: CharacterInt):
    event_format = ('2004', '53', 'i', [-1])
    return format_instruction(event_format, character)


def SetGravityAndCollisionExcludingOwnWorld(character: CharacterInt, state: bool):
    """ I assume "own world" refers to the world you're hosting. """
    event_format = ('2004', '54', 'iB', [-1, 0])
    return format_instruction(event_format, character, state)


def AddSpecialEffect_WithUnknownEffect(character: CharacterInt, special_effect: int, affect_npc_parts_hp: bool):
    """ Unknown additional affect from the standard instruction, presumably. """
    event_format = ('2004', '55', 'iiB')
    return format_instruction(event_format, character, special_effect, affect_npc_parts_hp)


def ActivateObjectWithSpecificCharacter(obj: ObjectInt, objact_id: int, relative_index: int, character: CharacterInt):
    """ The standard version of this 'grabs' the nearest character and uses them in the ObjAct (e.g. Patches pulling the
    lever in the Catacombs in DS1). I presume this version lets you specify which character should be involved in the
    ObjAct. """
    event_format = ('2005', '16', 'iiii', [-1, 0, 0, -1])
    return format_instruction(event_format, obj, objact_id, relative_index, character)


def SetObjectDamageShieldState(obj: ObjectInt, state: bool):
    """ Not sure how this differs from object invulnerability. """
    event_format = ('2005', '17', 'iB', [-1, 0])
    return format_instruction(event_format, obj, state)


def RegisterHealingFountain(flag: FlagInt, obj: ObjectInt, reaction_distance: float, reaction_angle: float,
                            initial_sword_number: int, sword_level: int):
    """ No idea what this is. Apparently DS1 also has a version of this with less arguments. """
    event_format = ('2009', '05', 'iiffii')
    return format_instruction(event_format, flag, obj, reaction_distance, reaction_angle, initial_sword_number,
                              sword_level)


def SetBossMusicState(sound_id: int, state: bool):
    """ Not sure how this differs from the standard map sound instructions. """
    event_format = ('2010', '04', 'iB', [0, 0])
    return format_instruction(event_format, sound_id, state)


def NotifyDoorEventSoundDampening(entity_id: int, state: DoorState):
    """ No idea what this is or what entity the first argument is. Probably the door object. """
    event_format = ('2010', '05', 'iB', [0, 0])
    return format_instruction(event_format, entity_id, state)


def SetHitboxResState(hitbox: HitboxInt, state: bool):
    """ No idea what this is. """
    event_format = ('2011', '03', 'iB', [-1, 0])
    return format_instruction(event_format, hitbox, state)


def CreatePlayLog(name: StringOffset):
    event_format = ('2013', '01', 's', [0])
    return format_instruction(event_format, name)

def StartPlayLogMeasurement(measurement_id: int, name: StringOffset, overwrite: bool):
    event_format = ('2013', '02', 'IsB', [0, 0, 0])
    return format_instruction(event_format, measurement_id, name, overwrite)

def StopPlayLogMeasurement(measurement_id: int):
    event_format = ('2013', '03', 'I', [0])
    return format_instruction(event_format, measurement_id)

def PlayLogParameterOutput(category: PlayerPlayLogParameter, name: StringOffset,
                           output_multiplayer_state: PlayLogMultiplayerType):
    event_format = ('2013', '04', 'BsB', [0, 0, 0])
    return format_instruction(event_format, category, name, output_multiplayer_state)
