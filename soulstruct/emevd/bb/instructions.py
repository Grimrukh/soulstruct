""" Full instruction set for BB. """

from __future__ import annotations
from soulstruct.emevd.core import set_instruction_arg_types
from soulstruct.emevd.shared.instructions import *
from soulstruct.emevd.game_types import *
from soulstruct.emevd.bb.enums import *


INSTRUCTION_ARG_TYPES = {
    2000: {
        0: 'iII', 1: 'iI', 2: 'B', 3: 'B', 4: 'I',
        5: 'B'},
    2001: {},
    2002: {1: 'iI', 2: 'iIiBB', 3: 'iIi', 4: 'iIiBBi',
           5: 'iIffifi', 6: 'iIiBBiB', 7: 'iIiB', 8: 'iBB'},
    2003: {
        1: 'iiBB', 2: 'iB', 3: 'iB', 4: 'i',
        5: 'iiiiiii', 6: 'iB', 7: 'iB', 8: 'iiB', 9: 'i',
        10: 'h', 11: 'bihi', 12: 'i', 13: 'iIB', 14: 'BBi',
        15: 'i', 16: 'I', 17: 'IIB', 18: 'iiBBB', 19: 'hh',
        20: 'i', 21: 'B', 22: 'iiB', 23: 'i', 24: 'iii',
        25: 'iiiii', 26: 'iB', 27: 'B', 28: 'i', 29: 'Bb',
        30: 'B', 31: 'iII', 32: 'iI', 33: 'i', 34: 'iiii',
        35: 'ii', 36: 'i', 37: '', 38: '', 39: '',
        40: '', 41: 'iIiiIb', 42: 'iiiI', 43: 'iiiI', 44: 'B',
        45: 'ihhhB', 46: 'hB', 47: 'hhhB', 48: 'iBfi', 49: 'i',
        50: 'i', 51: 'iiiii', 52: 'i', 53: 'ib', 54: 'i'},
    2004: {
        1: 'iB', 2: 'iB', 3: 'iBii', 4: 'iB', 
        5: 'iB', 6: 'iiB', 7: 'i', 8: 'iiB', 9: 'iiiiii', 
        10: 'iB', 11: 'ii', 12: 'iB', 13: 'ii', 14: 'iiiB', 
        15: 'iB', 16: 'i', 17: 'iiB', 18: 'iif', 19: 'ii', 
        20: 'i', 21: 'ii', 22: 'ihhiffBB', 23: 'iiiB', 24: 'iiii', 
        25: 'iif', 26: 'iBB', 27: 'iBB', 28: 'ii', 29: 'iB', 
        30: 'iB', 31: 'iB', 32: 'iiBii', 33: 'ii', 34: 'iBb', 
        35: 'iB', 36: 'iii', 37: 'i', 38: 'B', 39: 'iB', 
        40: 'iBiii', 41: 'iBii', 42: 'iBiii', 43: 'iB', 44: 'iB', 
        45: 'ii', 46: 'B', 47: '', 48: 'iBB', 49: 'ii', 
        50: 'if', 51: 'iiiiii', 52: 'i', 53: 'i', 54: 'iB', 
        55: 'iiB'},
    2005: {
        1: 'ib', 2: 'i', 3: 'iB', 4: 'iB', 
        5: 'iii', 6: 'iiB', 7: 'ii', 8: 'ib', 9: 'iiiiifff', 
        10: 'iBBB', 11: 'iih', 12: 'i', 13: 'iB', 14: 'iiiB', 
        15: 'i', 16: 'iiii', 17: 'iB'},
    2006: {
        1: 'iB', 2: 'i', 3: 'iiii', 4: 'iii', 
        5: 'ii'},
    2007: {
        1: 'ihhif', 2: 'B', 3: 'iB', 4: 'iB', 
        5: 'i', 6: 'i', 7: 'i', 8: 'i', 9: 'i'},
    2008: {
        1: 'ii', 2: 'iiiiff', 3: 'BBH'},
    2009: {
        0: 'iii', 1: 'iii', 2: 'iii', 3: 'iiffi', 4: 'i', 
        5: 'iiffii', 6: 'B'},
    2010: {
        1: 'BHiii', 2: 'iii', 3: 'iB', 4: 'iB', 
        5: 'iB'},
    2011: {
        1: 'iB', 2: 'iB', 3: 'iB'},
    2012: {
        1: 'iB'},
    2013: {
        1: 's', 2: 'IsB', 3: 'I', 4: 'BsB'},
    1000: {
        0: 'Bb', 1: 'BBb', 2: 'BBb', 3: 'B', 4: 'B', 5: 'Bbii',
        6: 'Bbii', 7: 'BBb', 8: 'BBb', 9: 'f', 
        101: 'BBb', 103: 'B', 105: 'Bbii', 107: 'BBb'},
    1001: {
        0: 'f', 1: 'i', 2: 'ff', 3: 'ii'},
    1003: {
        0: 'BBi', 1: 'BBBi', 2: 'BBBi', 3: 'BBBii', 4: 'BBBii', 
        5: 'Bb', 6: 'Bb', 7: 'BBBB', 8: 'BBBB', 9: 'BBB', 
        10: 'BBB', 11: 'BB', 12: 'BB', 13: 'BB', 14: 'BBBB', 
        15: 'BBBB', 16: 'BBBB', 101: 'BBBi', 103: 'BBBii', 
        105: 'Bb', 107: 'BBBB', 109: 'BBB'},
    1005: {
        0: 'Bi', 1: 'BBi', 2: 'BBi', 101: 'BBi'},
    1014: {
        0: '', 1: '', 2: '', 3: '', 4: '', 
        5: '', 6: '', 7: '', 8: '', 9: ''},
    0: {
        0: 'bBb', 1: 'bbii'},
    1: {
        0: 'bf', 1: 'bi', 2: 'bff', 3: 'bii'},
    3: {
        0: 'bBBi', 1: 'bBBii', 2: 'bBii', 3: 'bBiif', 4: 'bBiB', 
        5: 'biifhfiBi', 6: 'bb', 7: 'bBi', 8: 'bBBB', 9: 'bI', 
        10: 'bBiibi', 11: 'bBBB', 12: 'biBBI', 13: 'biifhfiBi', 14: 'bi', 
        15: 'bii', 16: 'bBiB', 17: 'bBB', 18: 'biifhfiBii', 19: 'biifhfiBii', 
        20: 'biBBiB', 21: 'bB', 22: 'bB', 23: 'biiB', 24: 'bii', 
        25: 'bBii', 26: 'bBb', 27: 'bb', 28: 'bb', 29: 'bBBB'},
    4: {
        0: 'biB', 1: 'bii', 2: 'bibf', 3: 'bib', 4: 'biiB', 
        5: 'biiB', 6: 'biiib', 7: 'biB', 8: 'biiB', 9: 'biB', 
        10: 'bB', 11: 'bB', 12: 'bB', 13: 'bBI', 14: 'biBi', 
        15: 'biB'},
    5: {
        0: 'bBi', 1: 'bii', 2: 'bi', 3: 'bibi'},
    11: {
        0: 'bi', 1: 'bi', 2: 'bi'}
}


set_instruction_arg_types(INSTRUCTION_ARG_TYPES)


def IfDamageType(condition: int, attacked_character: CharacterInt, attacking_character: CharacterInt,
                 damage_type: DamageType):
    """ Similar to IsAttackedBy, but requires a certain damage type. """
    instruction_info = (3, 23, [0, 0, -1, 0])
    return numeric_instruction(instruction_info, condition, attacked_character, attacking_character, damage_type)


def IfActionButtonInRegion(condition: int, action_button_id: int, region: RegionInt):
    """ Probably a simplified version of IfDialogPromptActivated. """
    instruction_info = (3, 24, [0, -1, -1])
    return numeric_instruction(instruction_info, condition, action_button_id, region)


def IfPlayerArmorType(condition: int, armor_type: ArmorType, required_armor_range_first: ArmorInt,
                      required_armor_range_last: ArmorInt):
    instruction_info = (3, 25, [0, ])
    return numeric_instruction(instruction_info, condition, armor_type, required_armor_range_first,
                               required_armor_range_last)


def IfPlayerInsightAmountComparison(condition: int, value: int, comparison_type: ComparisonType):
    """ Note change in argument order. """
    instruction_info = (3, 26, [0, 0, 0])
    return numeric_instruction(instruction_info, condition, value, comparison_type)

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
    instruction_info = (3, 27, [0, 0])
    return numeric_instruction(instruction_info, condition, dialog_result)


def IfPlayGoState(condition: int, playgo_state: PlayGoState):
    """ No idea what PlayGo state is but this doesn't sound like it would be used very often. """
    instruction_info = (3, 28, [0, 0])
    return numeric_instruction(instruction_info, condition, playgo_state)


def IfClientTypeCountComparison(condition: int, client_type: ClientType, comparison_type: ComparisonType, value):
    """ Value should only range between 0 and 4 (the maximum number of clients). """
    instruction_info = (3, 29, [0, 0, 0, 0])
    return numeric_instruction(instruction_info, condition, client_type, comparison_type, value)


def IfCharacterDrawGroupState(condition: int, character: CharacterInt, state: bool):
    """ Tests if character's draw group is currently active or inactive. """
    instruction_info = (4, 15, [0, 0, 0])
    return numeric_instruction(instruction_info, condition, character, state)

def IfCharacterDrawGroupActive(condition: int, character: CharacterInt):
    return IfCharacterDrawGroupState(condition, character, True)

def IfCharacterDrawGroupInactive(condition: int, character: CharacterInt):
    return IfCharacterDrawGroupState(condition, character, False)


def GotoIfConditionState(label: Label, required_state: bool, input_condition: int):
    instruction_info = (1000, 101, [0, 0, 0])
    return numeric_instruction(instruction_info, label, required_state, input_condition)

def GotoIfConditionTrue(label: Label, input_condition: int):
    return GotoIfConditionState(label, True, input_condition)

def GotoIfConditionFalse(label: Label, input_condition: int):
    return GotoIfConditionState(label, False, input_condition)

def Goto(label: Label):
    """ Unconditional GOTO. """
    instruction_info = (1000, 103, [0])
    return numeric_instruction(instruction_info, label)

def GotoIfValueComparison(label: Label, comparison_type: ComparisonType, left: int, right: int):
    instruction_info = (1000, 105)
    return numeric_instruction(instruction_info, label, comparison_type, left, right)

def GotoIfFinishedConditionState(label: Label, required_state: bool, input_condition: int):
    """ Finished version. """
    instruction_info = (1000, 107, [0, 0, 0])
    return numeric_instruction(instruction_info, label, required_state, input_condition)

def GotoIfFinishedConditionTrue(label: Label, input_condition: int):
    return GotoIfFinishedConditionState(label, True, input_condition)

def GotoIfFinishedConditionFalse(label: Label, input_condition: int):
    return GotoIfFinishedConditionState(label, False, input_condition)

def SkipLinesIfCoopClientCountComparison(skip_lines: int, comparison_type: ComparisonType, value: int):
    """ Value should be from 0 to 4. """
    instruction_info = (1003, 9, [0, 0, 0])
    return numeric_instruction(instruction_info, skip_lines, comparison_type, value)

def TerminateIfCoopClientCountComparison(event_end_type: EventEndType, comparison_type: ComparisonType, value: int):
    instruction_info = (1003, 10, [0, 0, 0])
    return numeric_instruction(instruction_info, event_end_type, comparison_type, value)

def EndIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return TerminateIfCoopClientCountComparison(EventEndType.End, comparison_type, value)

def RestartIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return TerminateIfCoopClientCountComparison(EventEndType.Restart, comparison_type, value)


def SkipLinesIfPlayerGender(skip_lines: int, gender: Gender):
    instruction_info = (1003, 11)
    return numeric_instruction(instruction_info, skip_lines, gender)

def GotoIfPlayerGender(label: Label, gender: Gender):
    instruction_info = (1003, 12)
    return numeric_instruction(instruction_info, label, gender)

def TerminateIfPlayerGender(event_end_type: EventEndType, gender: Gender):
    instruction_info = (1003, 13)
    return numeric_instruction(instruction_info, event_end_type, gender)

def EndIfPlayerGender(gender: Gender):
    return TerminateIfPlayerGender(EventEndType.End, gender)

def RestartIfPlayerGender(gender: Gender):
    return TerminateIfPlayerGender(EventEndType.Restart, gender)


def SkipLinesIfClientTypeCountComparison(skip_lines: int, client_type: ClientType, comparison_type: ComparisonType,
                                         value: int):
    """ Value from 0 to 4. """
    instruction_info = (1003, 14, [0, 0, 0, 0])
    return numeric_instruction(instruction_info, skip_lines, client_type, comparison_type, value)

def GotoIfClientTypeCountComparison(label: Label, client_type: ClientType, comparison_type: ComparisonType,
                                    value: int):
    """ Value from 0 to 4. """
    instruction_info = (1003, 15, [0, 0, 0, 0])
    return numeric_instruction(instruction_info, label, client_type, comparison_type, value)

def TerminateIfClientTypeCountComparison(event_end_type: EventEndType, client_type: ClientType,
                                         comparison_type: ComparisonType, value: int):
    """ Value from 0 to 4. """
    instruction_info = (1003, 16, [0, 0, 0, 0])
    return numeric_instruction(instruction_info, event_end_type, client_type, comparison_type, value)

def EndIfClientTypeCountComparison(client_type: ClientType, comparison_type: ComparisonType, value: int):
    """ Value from 0 to 4. """
    return TerminateIfClientTypeCountComparison(EventEndType.End, client_type, comparison_type, value)

def RestartIfClientTypeCountComparison(client_type: ClientType, comparison_type: ComparisonType, value: int):
    """ Value from 0 to 4. """
    return TerminateIfClientTypeCountComparison(EventEndType.Restart, client_type, comparison_type, value)


def GotoIfFlagState(label: Label, state: bool, flag_type: FlagType, flag: FlagInt):
    instruction_info = (1003, 101)
    return numeric_instruction(instruction_info, label, state, flag_type, flag)

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
    instruction_info = (1003, 103)
    first_flag, last_flag = tuple(flag_range)
    return numeric_instruction(instruction_info, label, state, flag_type, first_flag, last_flag)

def GotoIfFlagRangeAllOn(label: Label, flag_range: FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AllOn, FlagType.Absolute, flag_range)

def GotoIfFlagRangeAllOff(label: Label, flag_range: FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AllOff, FlagType.Absolute, flag_range)

def GotoIfFlagRangeAnyOn(label: Label, flag_range: FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AnyOn, FlagType.Absolute, flag_range)

def GotoIfFlagRangeAnyOff(label: Label, flag_range: FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AnyOff, FlagType.Absolute, flag_range)


def GotoIfMultiplayerState(label: Label, state: MultiplayerState):
    instruction_info = (1003, 105, [0, 0])
    return numeric_instruction(instruction_info, label, state)

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
    instruction_info = (1003, 107, [0, 0, 0, 0])
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, label, state, area_id, block_id)

def GotoIfInsideMap(label: Label, game_map: GameMap):
    return GotoIfMapPresenceState(label, game_map, True)

def GotoIfOutsideMap(label: Label, game_map: GameMap):
    return GotoIfMapPresenceState(label, game_map, False)


def GotoIfCoopClientCountComparison(label: Label, comparison_type: ComparisonType, value: int):
    instruction_info = (1003, 109, [0, 0, 0])
    return numeric_instruction(instruction_info, label, comparison_type, value)


def GotoIfObjectDestructionState(label: Label, obj: ObjectInt, state: bool):
    """ Note change in argument order. """
    instruction_info = (1005, 101, [0, 0, -1])
    return numeric_instruction(instruction_info, label, state, obj)

def GotoIfObjectDestroyed(label: Label, obj: ObjectInt):
    return GotoIfObjectDestructionState(label, obj, True)

def GotoIfObjectNotDestroyed(label: Label, obj: ObjectInt):
    return GotoIfObjectDestructionState(label, obj, False)


# MULTIPLAYER

def SkipLinesIfMultiplayerState(line_count, state: MultiplayerState):
    instruction_info = (1003, 5)
    return numeric_instruction(instruction_info, line_count, state)

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
    instruction_info = (1003, 6)
    return numeric_instruction(instruction_info, event_end_type, state)

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
    instruction_info = (3, 6)
    return numeric_instruction(instruction_info, condition, state)

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
    instruction_info = (1014, label)
    return numeric_instruction(instruction_info)


def PlayCutsceneAndMovePlayerAndSetTimePeriod(cutscene: int, cutscene_type: CutsceneType, region: RegionInt,
                                              game_map: GameMap, player_id: int, time_period_id: int):
    """ Warp a particular player to a region and set the time period. I assume that this must be a map that is
    already loaded, like in DS1, but possibly not.

    It's probably used to warp to Bergenwerth after Rom, so either that map is already loaded when you defeat Rom, or
    this event *is* capable of warping to an entirely new map.
    """
    instruction_info = (2002, 6)
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, cutscene, cutscene_type, region, area_id, block_id, player_id,
                               time_period_id)


def PlayCutsceneAndSetTimePeriod(cutscene: int, cutscene_type: CutsceneType, player_id: int,
                                 time_period_id: int):
    """ Probably used when you examine Laurence's skull, etc. """
    instruction_info = (2002, 7, [-1, 0, -1, 0])
    return numeric_instruction(instruction_info, cutscene, cutscene_type, player_id, time_period_id)


def PlayCutsceneAndMovePlayer_Dummy(region: RegionInt, game_map: GameMap):
    """ Likely not used, doesn't even take a cutscene ID argument. """
    instruction_info = (2002, 8, [0, 0, 0])
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, region, area_id, block_id)


def SetBossHealthBarState(character: CharacterInt, name: TextInt, slot, state: bool):
    """ Note: slot number can be 0-2 in Bloodborne. """
    instruction_info = (2003, 11)
    if isinstance(slot, int) and slot not in (0, 1, 2):
        raise ValueError("Boss health bar slot must be 0, 1, or 2.")
    return numeric_instruction(instruction_info, state, character, slot, name)

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
    instruction_info = (2003, 15, [0])
    return numeric_instruction(instruction_info, miniboss_id)


def Unknown_2003_27(arg1: int):
    """ No information. """
    instruction_info = (2003, 27)
    return numeric_instruction(instruction_info, arg1)


def EventValueOperation(source_flag: FlagInt, source_flag_bit_count: int, operand: int, target_flag: FlagInt,
                        target_flag_bit_count: int, calculation_type: CalculationType):
    """ Performs a binary operation on the source flag and operand value, and stores the result in the target flag. """
    instruction_info = (2003, 41)
    return numeric_instruction(instruction_info, source_flag, source_flag_bit_count, operand, target_flag,
                               target_flag_bit_count, calculation_type)


def StoreItemAmountSpecifiedByFlagValue(item_type: ItemType, item: ItemInt, flag: FlagInt, bit_count: int):
    """ Stores some amount of items read from a flag array. """
    instruction_info = (2003, 42)
    return numeric_instruction(instruction_info, item_type, item, flag, bit_count)

def GivePlayerItemAmountSpecifiedByFlagValue(item_type: ItemType, item: ItemInt, flag: FlagInt, bit_count: int):
    """ Gives player some amount of items read from a flag array. Probably used when taking items out of storage
    (i.e. the reverse of the above instruction). """
    instruction_info = (2003, 43)
    return numeric_instruction(instruction_info, item_type, item, flag, bit_count)


def SetDirectionDisplayState(state: bool):
    """ Not sure what this is. """
    instruction_info = (2003, 44)
    return numeric_instruction(instruction_info, state)

def EnableDirectionDisplay():
    return SetDirectionDisplayState(True)

def DisableDirectionDisplay():
    return SetDirectionDisplayState(False)


def SetMapHitGridCorrespondence(hitbox: HitboxInt, level: int, grid_coord_x: int, grid_coord_y: int, state: bool):
    instruction_info = (2003, 45)
    return numeric_instruction(instruction_info, hitbox, level, grid_coord_x, grid_coord_y, state)

def EnableMapHitGridCorrespondence(hitbox: HitboxInt, level: int, grid_coord_x: int, grid_coord_y: int):
    return SetMapHitGridCorrespondence(hitbox, level, grid_coord_x, grid_coord_y, True)

def DisableMapHitGridCorrespondence(hitbox: HitboxInt, level: int, grid_coord_x: int, grid_coord_y: int):
    return SetMapHitGridCorrespondence(hitbox, level, grid_coord_x, grid_coord_y, False)


def SetMapContentImageDisplayState(content_image_part_id: int, state: bool):
    instruction_info = (2003, 46)
    return numeric_instruction(instruction_info, content_image_part_id, state)


def SetMapBoundariesDisplay(hierarchy: int, grid_coord_x: int, grid_coord_y: int, state: bool):
    instruction_info = (2003, 47)
    return numeric_instruction(instruction_info, hierarchy, grid_coord_x, grid_coord_y, state)


def SetAreaWind(region: RegionInt, state: bool, duration: float, wind_parameter_id: int):
    instruction_info = (2003, 48)
    return numeric_instruction(instruction_info, region, state, duration, wind_parameter_id)


def MovePlayerToRespawnPoint(respawn_point_id: int):
    instruction_info = (2003, 49, [0])
    return numeric_instruction(instruction_info, respawn_point_id)


def StartEnemySpawner(spawner_id: int):
    instruction_info = (2003, 50, [-1])
    return numeric_instruction(instruction_info, spawner_id)


def SummonNPC(sign_type: Union[SingleplayerSummonSignType, int], character: CharacterInt, region: RegionInt,
              summon_flag: FlagInt, dismissal_flag: FlagInt):
    instruction_info = (2003, 51)
    return numeric_instruction(instruction_info, sign_type, character, region, summon_flag, dismissal_flag)


def InitializeWarpObject(warp_object_id: int):
    instruction_info = (2003, 52, [0])
    return numeric_instruction(instruction_info, warp_object_id)


def BossDefeat(boss_id: int, banner_type: BannerType):
    """ Handle boss defeat and display banner. 'boss_id' is probably similar to GameAreaParam from DS1. """
    instruction_info = (2003, 53)
    return numeric_instruction(instruction_info, boss_id, banner_type)


def SendNPCSummonHome(character: CharacterInt):
    instruction_info = (2003, 54, [-1])
    return numeric_instruction(instruction_info, character)


def AddSpecialEffect(character: CharacterInt, special_effect_id: int, affect_npc_part_hp: bool):
    """ 'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will do
    nothing if the character already has the special effect active (i.e. they do not stack or even reset timers).

    The Bloodborne version has an additional argument that determines whether any HP changes caused by the special
    effect should also affect NPC parts.
    """
    instruction_info = (2004, 8)
    return numeric_instruction(instruction_info, character, special_effect_id, affect_npc_part_hp)


def RotateToFaceEntity(character: CharacterInt, target_entity: MapEntityInt, animation: int,
                       wait_for_completion: bool = False):
    """ Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at least.)

    The Bloodborne version allows you to force an animation at the same time and optionally wait until that animation
    is completed. (I assume a value of -1 avoids it.)
    """
    instruction_info = (2004, 14, [0, 0, -1, 0])
    return numeric_instruction(instruction_info, character, target_entity, animation, wait_for_completion)


def ChangeCharacterCloth(character: CharacterInt, bit_count: int, state_id: int):
    instruction_info = (2004, 48, [0, 0, 0])
    return numeric_instruction(instruction_info, character, bit_count, state_id)


def ChangePatrolBehavior(character: CharacterInt, patrol_information_id: int):
    """ I don't know what a 'patrol_information_id' actually is. """
    instruction_info = (2004, 49, [0, -1])
    return numeric_instruction(instruction_info, character, patrol_information_id)


def SetDistanceLimitForConversationStateChanges(character: CharacterInt, distance: float):
    instruction_info = (2004, 50)
    return numeric_instruction(instruction_info, character, distance)


def Test_RequestRagdollRestraint(recipient_character: CharacterInt, recipient_target_rigid_index: int,
                                 recipient_model_point: int, attachment_character: CharacterInt,
                                 attachment_target_rigid_index: int, attachment_model_point: int):
    instruction_info = (2004, 51)
    return numeric_instruction(instruction_info, recipient_character, recipient_target_rigid_index, recipient_model_point,
                               attachment_character, attachment_target_rigid_index, attachment_model_point)


def ChangePlayerCharacterInitParam(character_init_param: int):
    """ I assume this affects the player. """
    instruction_info = (2004, 52, [0])
    return numeric_instruction(instruction_info, character_init_param)


def AdaptSpecialEffectHealthChangeToNPCPart(character: CharacterInt):
    instruction_info = (2004, 53, [-1])
    return numeric_instruction(instruction_info, character)


def SetGravityAndCollisionExcludingOwnWorld(character: CharacterInt, state: bool):
    """ I assume "own world" refers to the world you're hosting. """
    instruction_info = (2004, 54, [-1, 0])
    return numeric_instruction(instruction_info, character, state)


def AddSpecialEffect_WithUnknownEffect(character: CharacterInt, special_effect: int, affect_npc_parts_hp: bool):
    """ Unknown additional affect from the standard instruction, presumably. """
    instruction_info = (2004, 55)
    return numeric_instruction(instruction_info, character, special_effect, affect_npc_parts_hp)


def ActivateObjectWithSpecificCharacter(obj: ObjectInt, objact_id: int, relative_index: int, character: CharacterInt):
    """ The standard version of this 'grabs' the nearest character and uses them in the ObjAct (e.g. Patches pulling the
    lever in the Catacombs in DS1). I presume this version lets you specify which character should be involved in the
    ObjAct. """
    instruction_info = (2005, 16, [-1, 0, 0, -1])
    return numeric_instruction(instruction_info, obj, objact_id, relative_index, character)


def SetObjectDamageShieldState(obj: ObjectInt, state: bool):
    """ Not sure how this differs from object invulnerability. """
    instruction_info = (2005, 17, [-1, 0])
    return numeric_instruction(instruction_info, obj, state)


def RegisterHealingFountain(flag: FlagInt, obj: ObjectInt, reaction_distance: float, reaction_angle: float,
                            initial_sword_number: int, sword_level: int):
    """ No idea what this is. Apparently DS1 also has a version of this with less arguments. """
    instruction_info = (2009, 5)
    return numeric_instruction(instruction_info, flag, obj, reaction_distance, reaction_angle, initial_sword_number,
                               sword_level)


def SetBossMusicState(sound_id: int, state: bool):
    """ Not sure how this differs from the standard map sound instructions. """
    instruction_info = (2010, 4, [0, 0])
    return numeric_instruction(instruction_info, sound_id, state)


def NotifyDoorEventSoundDampening(entity_id: int, state: DoorState):
    """ No idea what this is or what entity the first argument is. Probably the door object. """
    instruction_info = (2010, 5, [0, 0])
    return numeric_instruction(instruction_info, entity_id, state)


def SetHitboxResState(hitbox: HitboxInt, state: bool):
    """ No idea what this is. """
    instruction_info = (2011, 3, [-1, 0])
    return numeric_instruction(instruction_info, hitbox, state)


def CreatePlayLog(name: StringOffset):
    instruction_info = (2013, 1, [0])
    return numeric_instruction(instruction_info, name)

def StartPlayLogMeasurement(measurement_id: int, name: StringOffset, overwrite: bool):
    instruction_info = (2013, 2, [0, 0, 0])
    return numeric_instruction(instruction_info, measurement_id, name, overwrite)

def StopPlayLogMeasurement(measurement_id: int):
    instruction_info = (2013, 3, [0])
    return numeric_instruction(instruction_info, measurement_id)

def PlayLogParameterOutput(category: PlayerPlayLogParameter, name: StringOffset,
                           output_multiplayer_state: PlayLogMultiplayerType):
    instruction_info = (2013, 4, [0, 0, 0])
    return numeric_instruction(instruction_info, category, name, output_multiplayer_state)
