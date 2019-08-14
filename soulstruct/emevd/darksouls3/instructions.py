"""Full instruction set for DS3.

Many instructions in DS3 have some added debug parameters called 'target_comparison_type' and 'target_count', each of
which are almost always set to '==' and '1' in the vanilla events. You probably don't want to change those, but if so,
I've only left access to them in the base instruction of each type (the ones that actually call `numeric_instruction`).
"""

from __future__ import annotations
from soulstruct.emevd.core import set_instruction_arg_types
from soulstruct.emevd.shared.instructions import *
from soulstruct.enums.darksouls3 import *
import soulstruct.game_types as gt


INSTRUCTION_ARG_TYPES = {
    2000: {
        0: 'iII', 1: 'iI', 2: 'B', 3: 'B', 4: 'I',
        5: 'B', 6: 'II'},
    2001: {},
    2002: {
        1: 'iI', 2: 'iIiBB', 3: 'iIi', 4: 'iIiBBi',
        5: 'iIffifi', 6: 'iIiBBiB', 7: 'iIiB', 8: 'iBB', 9: 'iIIiiBBi',
        10: 'iIIii', 11: 'iIiBBiBB', 12: 'iIiBBii'},
    2003: {
        1: 'iiBB', 2: 'iB', 3: 'iB', 4: 'i',
        5: 'iiiiiii', 6: 'iB', 7: 'iB', 8: 'iiB', 9: 'i',
        10: 'h', 11: 'bihi', 12: 'i', 13: 'iIB', 14: 'BBi',
        15: 'i', 16: 'I', 17: 'IIB', 18: 'iiBBBBf', 19: 'hh',
        20: 'i', 21: 'B', 22: 'iiB', 23: 'i', 24: 'iii',
        25: 'iiiii', 26: 'iB', 27: 'B', 28: 'i', 29: 'Bb',
        30: 'B', 31: 'iII', 32: 'iI', 33: 'i', 34: 'iiii',
        35: 'ii', 36: 'i', 37: '', 38: '', 39: '',
        40: '', 41: 'iIiiIb', 42: 'iiiI', 43: 'iiiI', 44: 'B',
        45: 'ihhhB', 46: 'hB', 47: 'hhhB', 48: 'iBfi', 49: 'i',
        50: 'i', 51: 'iiiii', 52: 'i', 54: 'i',
        57: 'I', 59: 'IBI', 61: 'i', 62: 'iB', 63: 'iiB', 64: 'ii',
        65: '', 66: 'Iiiii', 67: 'i',
        70: 'B', 71: 'B', 72: 'iiB', 73: 'BB', 74: 'iB',
        75: 'BB', 76: 'B', 77: 'HHi', 78: 'i', 79: 'B',
        80: 'bihiB', 81: 'iiiii'},
    2004: {
        1: 'iB', 2: 'iB', 3: 'iBii', 4: 'iB',
        5: 'iB', 6: 'iiB', 7: 'i', 8: 'ii', 9: 'iiiiii',
        10: 'iB', 11: 'ii', 12: 'iB', 13: 'ii', 14: 'iiiB',
        15: 'iB', 16: 'i', 17: 'iiB', 18: 'iif', 19: 'ii',
        20: 'i', 21: 'ii', 22: 'ihhiffBB', 23: 'iiiB', 24: 'iiii',
        25: 'iif', 26: 'iBB', 27: 'iBB', 28: 'ii', 29: 'iB',
        30: 'iB', 31: 'iB', 32: 'iiBii', 33: 'ii', 34: 'iBb',
        35: 'iB', 36: 'iii', 37: 'i', 38: 'B', 39: 'iB',
        40: 'iBiii', 41: 'iBii', 42: 'iBiii', 43: 'iB', 44: 'iB',
        45: 'ii', 46: 'B', 47: '', 48: 'iBB', 49: 'ii',
        50: 'iiB', 51: 'iiiiii', 52: 'i', 53: 'i', 54: 'iB',
        55: 'if', 57: 'i', 58: 'iB', 59: 'iB',
        60: 'B'},
    2005: {
        1: 'ib', 2: 'i', 3: 'iB', 4: 'iB',
        5: 'iii', 6: 'iiB', 7: 'ii', 8: 'ib', 9: 'iiiiifff',
        10: 'iBBB', 11: 'iih', 12: 'i', 13: 'iB', 14: 'iiiB',
        15: 'i', 16: '', 17: 'iIi', 19: 'i'},
    2006: {
        1: 'iB', 2: 'i', 3: 'iiii', 4: 'iii',
        5: 'ii'},
    2007: {
        1: 'ihhif', 2: 'B', 3: 'iB', 4: 'iB',
        5: 'i', 6: 'i', 7: 'i', 8: 'i', 9: 'i',
        10: 'ihhifiii', 11: 'i', 12: 'ihB'},
    2008: {
        1: 'ii', 2: 'iiiiff', 3: 'BBH'},
    2009: {
        0: 'iii', 1: 'iii', 2: 'iii', 3: 'iiffi', 4: 'i',
        5: 'iiffii', 6: 'B', 8: 'i',
        10: 'i', 11: 'i'},
    2010: {
        1: 'BHiii', 2: 'iii', 3: 'iB', 4: 'iB',
        5: 'iB', 6: 'iBf', 7: 'i'},
    2011: {
        1: 'iB', 2: 'iB', 3: 'iB', 4: 'iB'},
    2012: {
        1: 'iB', 8: 'B'},
    2013: {
        1: 's', 2: 'IsB', 3: 'I', 4: 'BsB'},
    1000: {
        0: 'Bb', 1: 'BBb', 2: 'BBb', 3: 'B', 4: 'B',
        5: 'Bbii', 6: 'Bbii', 7: 'BBb', 8: 'BBb', 9: 'f', 
        101: 'BBb', 103: 'B', 105: 'Bbii', 107: 'BBb'},
    1001: {
        0: 'f', 1: 'i', 2: 'ff', 3: 'ii', 4: 'BB'},
    1003: {
        0: 'BBi', 1: 'BBBi', 2: 'BBBi', 3: 'BBBii', 4: 'BBBii', 
        5: 'Bb', 6: 'Bb', 7: 'BBBB', 8: 'BBBB', 9: 'BBB', 
        10: 'BBB', 11: 'BiiBbi', 12: 'BB', 13: 'BB', 14: 'BBBB', 
        15: 'BBBB', 16: 'BBBB', 101: 'BBBi', 103: 'BBBii', 
        105: 'Bb', 107: 'BBBB', 109: 'BBB', 111: 'BiiBbi', 112: 'BiiBbi', 
        200: 'BBiii', 201: 'BBiii', 202: 'BBiii', 211: 'BB'},
    1005: {
        0: 'Bi', 1: 'BBibf', 2: 'BBibf', 101: 'BBibf'},
    1014: {
        0: '', 1: '', 2: '', 3: '', 4: '', 
        5: '', 6: '', 7: '', 8: '', 9: '', 
        10: '', 11: '', 12: '', 13: '', 14: '', 
        15: '', 16: '', 17: '', 18: '', 19: '', 
        20: ''},
    0: {
        0: 'bBb', 1: 'bbii'},
    1: {
        0: 'bf', 1: 'bi', 2: 'bff', 3: 'bii'},
    3: {
        0: 'bBBi', 1: 'bBBii', 2: 'bBiii', 3: 'bBiifi', 4: 'bBiB', 
        5: 'biifhfiBi', 6: 'bb', 7: 'bBi', 8: 'bBBB', 9: 'bI',
        10: 'bBiibi', 11: 'bBBB', 12: 'biBBI', 13: 'biifhfiBi', 14: 'bi', 
        15: 'bii', 16: 'bBiB', 17: 'bBB', 18: 'biifhfiBii', 19: 'biifhfiBii', 
        20: 'biBBiB', 21: 'bB', 22: 'bB', 23: 'biiB', 24: 'bii', 
        25: 'bBii', 26: 'bB', 28: 'bBBBH', 29: 'b', 
        30: 'bB', 31: 'bi', 32: 'bB', 33: 'bB', 34: 'bbi', 
        35: 'bB', 38: 'bB', 39: 'bBbi'},
    4: {0: 'biBbf', 1: 'bii', 2: 'bibfbf', 3: 'bibbf', 4: 'biiB', 
        5: 'biiBbf', 6: 'biiib', 7: 'biBbf', 8: 'biiBbf', 9: 'biBbf', 
        10: 'bB', 11: 'bB', 12: 'bB', 13: 'bBI', 14: 'biBibf', 
        15: 'biBbf', 26: 'bBi', 27: 'biBbf', 28: 'biiB'},
    5: {
        0: 'bBibf', 1: 'bii', 2: 'bi', 3: 'bibi', 9: 'biBBbf', 
        10: 'biBbf', 11: 'biBbf'},
    11: {
        0: 'bi', 1: 'bi', 2: 'bi'}
}


set_instruction_arg_types(INSTRUCTION_ARG_TYPES)


# 2000: SYSTEM

def RunCommonEvent(event_id: int, args=(0,), arg_types=None):
    """ Same as RunEvent, but takes no slots. """
    instruction_info = (2000, 6)  # List for this instruction only, as it may required modification.
    if arg_types is None:
        arg_types = 'I' * len(args)
    if len(args) != len(arg_types):
        raise ValueError("Number of event arguments does not match length of argument type string.")
    format_string = 'I' + str(arg_types[0])
    if len(arg_types) > 1:
        format_string += f'|{arg_types[1:]}'
    return numeric_instruction(instruction_info, event_id, *args, arg_types=format_string)


# 3: CONDITIONS (EVENT)

def IfCharacterRegionState(condition, entity: gt.AnimatedInt, region: gt.RegionInt, state: bool,
                           min_target_count: int = 1):
    """ New argument with unknown purpose. Always 1 in vanilla resources. Probably for debug. """
    instruction_info = (3, 2)
    return numeric_instruction(instruction_info, condition, state, entity, region, min_target_count)

def IfCharacterInsideRegion(condition: int, entity: gt.AnimatedInt, region: gt.RegionInt):
    return IfCharacterRegionState(condition, entity, region, True)

def IfCharacterOutsideRegion(condition: int, entity: gt.AnimatedInt, region: gt.RegionInt):
    return IfCharacterRegionState(condition, entity, region, False)

def IfPlayerInsideRegion(condition: int, region: gt.RegionInt):
    return IfCharacterRegionState(condition, PLAYER, region, True)

def IfPlayerOutsideRegion(condition: int, region: gt.RegionInt):
    return IfCharacterRegionState(condition, PLAYER, region, False)


def IfEntityDistanceState(condition: int, entity: gt.CoordEntityInt, other_entity: gt.CoordEntityInt, radius: float,
                          state: bool, min_target_count: int = 1):
    """ Same new argument as region test, with unknown purpose, and again always 1 in EMEVD resources. """
    instruction_info = (3, 3)
    return numeric_instruction(instruction_info, condition, state, entity, other_entity, radius, min_target_count)

def IfEntityWithinDistance(condition: int, entity: gt.CoordEntityInt, other_entity: gt.CoordEntityInt, radius: float):
    return IfEntityDistanceState(condition, entity, other_entity, radius, True)

def IfEntityBeyondDistance(condition: int, entity: gt.CoordEntityInt, other_entity: gt.CoordEntityInt, radius: float):
    return IfEntityDistanceState(condition, entity, other_entity, radius, False)

def IfPlayerWithinDistance(condition: int, other_entity: gt.CoordEntityInt, radius: float):
    return IfEntityDistanceState(condition, PLAYER, other_entity, radius, True)

def IfPlayerBeyondDistance(condition: int, other_entity: gt.CoordEntityInt, radius: float):
    return IfEntityDistanceState(condition, PLAYER, other_entity, radius, False)


def IfMultiplayerState(condition: int, state: MultiplayerState):
    instruction_info = (3, 6)
    return numeric_instruction(instruction_info, condition, state)

def IfHost(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Host)

def IfClient(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Client)

def IfTryingToCreateSession(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.TryingToCreateSession)

def IfTryingToJoinSession(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.TryingToJoinSession)

def IfLeavingSession(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.LeavingSession)

def IfFailedToCreateSession(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.FailedToCreateSession)


def IfDamageType(condition: int, attacked_entity: gt.AnimatedInt, attacking_character: gt.CharacterInt,
                 damage_type: DamageType):
    """ Similar to IsAttackedBy, but requires a certain damage type. """
    instruction_info = (3, 23, [0, 0, -1, 0])
    return numeric_instruction(instruction_info, condition, attacked_entity, attacking_character, damage_type)


def IfActionButtonInRegion(condition: int, action_button_id: int, region: gt.RegionInt):
    """ Probably a simplified version of IfDialogPromptActivated. """
    instruction_info = (3, 24, [0, -1, -1])
    return numeric_instruction(instruction_info, condition, action_button_id, region)


def IfPlayerOwnWorldState(condition: int, not_in_own_world: bool):
    """ Excluding Arena. """
    instruction_info = (3, 26)
    return numeric_instruction(instruction_info, condition, not_in_own_world)

def IfPlayerInOwnWorld(condition: int):
    return IfPlayerOwnWorldState(condition, False)

def IfPlayerNotInOwnWorld(condition: int):
    return IfPlayerOwnWorldState(condition, True)


def IfMapCeremonyState(condition: int, state: bool, game_map: gt.MapOrSequence, ceremony_id: int):
    """ Ceremony states are unused (except for Untended Graves, I believe). """
    instruction_info = (3, 28)
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, condition, state, area_id, block_id, ceremony_id)

def IfMapInCeremony(condition: int, game_map: gt.MapOrSequence, ceremony_id: int):
    return IfMapCeremonyState(condition, True, game_map, ceremony_id)

def IfMapNotInCeremony(condition: int, game_map: gt.MapOrSequence, ceremony_id: int):
    return IfMapCeremonyState(condition, False, game_map, ceremony_id)


def IfMultiplayerNetworkPenalized(condition: int):
    instruction_info = (3, 29)
    return numeric_instruction(instruction_info, condition)


def IfPlayerGender(condition: int, gender: Gender):
    """ Note that this condition version of the gender test was absent in Bloodborne. """
    instruction_info = (3, 30)
    return numeric_instruction(instruction_info, condition, gender)


def IfOngoingCutsceneFinished(condition: int, cutscene_id: int):
    instruction_info = (3, 31)
    return numeric_instruction(instruction_info, condition, cutscene_id)


def IfHollowArenaMatchReadyState(condition: int, is_ready: bool):
    instruction_info = (3, 32)
    return numeric_instruction(instruction_info, condition, is_ready)


def IfHollowArenaSoloResults(condition: int, result: HollowArenaResult):
    instruction_info = (3, 33)
    return numeric_instruction(instruction_info, condition, result)


def IfHollowArenaSoloScoreComparison(condition: int, comparison_type: ComparisonType, value: int):
    """ EMEDF incorrectly says that the value size is 'B'. """
    instruction_info = (3, 34)
    return numeric_instruction(instruction_info, condition, comparison_type, value)


def IfHollowArenaTeamResults(condition: int, result: HollowArenaResult):
    instruction_info = (3, 35)
    return numeric_instruction(instruction_info, condition, result)


def IfSteamDisconnected(condition: int, is_disconnected: bool):
    instruction_info = (3, 38)
    return numeric_instruction(instruction_info, condition, is_disconnected)


def IfAllyPhantomCountComparison(condition: int, comparison_state: bool, comparison_type: ComparisonType, value: int):
    """ Note that there's a 'comparison_state' bool that can be used to invert the operation (kind of pointless). """
    instruction_info = (3, 39)
    return numeric_instruction(instruction_info, condition, comparison_state, comparison_type, value)


# 4: CONDITIONS (CHARACTER)
# New 'comparison_type' and 'target_count' arguments added to many of them; unknown purpose.
# To make things even weirder, the 'target_count' usually seems to be a float.

def IfCharacterDeathState(condition: int, character: gt.CharacterInt, state: bool,
                          target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    instruction_info = (4, 0)
    return numeric_instruction(instruction_info, condition, character, state,
                               target_comparison_type, target_count)

def IfCharacterDead(condition: int, character: gt.CharacterInt):
    return IfCharacterDeathState(condition, character, True)

def IfCharacterAlive(condition: int, character: gt.CharacterInt):
    return IfCharacterDeathState(condition, character, False)


def IfHealthComparison(condition: int, character: gt.CharacterInt, comparison_type: ComparisonType, value,
                       target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    instruction_info = (4, 2)
    return numeric_instruction(instruction_info, condition, character, comparison_type, value,
                               target_comparison_type, target_count)

def IfHealthEqual(condition: int, character: gt.CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.Equal, value)

def IfHealthNotEqual(condition: int, character: gt.CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.NotEqual, value)

def IfHealthGreaterThan(condition: int, character: gt.CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.GreaterThan, value)

def IfHealthLessThan(condition: int, character: gt.CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.LessThan, value)

def IfHealthGreaterThanOrEqual(condition: int, character: gt.CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.GreaterThanOrEqual, value)

def IfHealthLessThanOrEqual(condition: int, character: gt.CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.LessThanOrEqual, value)


def IfCharacterType(condition: int, character: gt.CharacterInt, character_type: CharacterType,
                    target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    instruction_info = (4, 3)
    return numeric_instruction(instruction_info, condition, character, character_type,
                               target_comparison_type, target_count)

def IfCharacterHollow(condition: int, character: gt.CharacterInt):
    return IfCharacterType(condition, character, CharacterType.Hollow)

def IfCharacterHuman(condition: int, character: gt.CharacterInt):
    return IfCharacterType(condition, character, CharacterType.Human)


def IfCharacterSpecialEffectState(condition: int, character: gt.CharacterInt, special_effect: int, state,
                                  target_comparison_type: ComparisonType = ComparisonType.Equal,
                                  target_count: float = 1.0):
    instruction_info = (4, 5, [0, 0, -1, 0, 0, 0])
    return numeric_instruction(instruction_info, condition, character, special_effect, state,
                               target_comparison_type, target_count)

def IfCharacterHasSpecialEffect(condition: int, character: gt.CharacterInt, special_effect):
    return IfCharacterSpecialEffectState(condition, character, special_effect, True)

def IfCharacterDoesNotHaveSpecialEffect(condition: int, character: gt.CharacterInt, special_effect):
    return IfCharacterSpecialEffectState(condition, character, special_effect, False)

def IfPlayerHasSpecialEffect(condition: int, special_effect):
    return IfCharacterSpecialEffectState(condition, PLAYER, special_effect, True)

def IfPlayerDoesNotHaveSpecialEffect(condition: int, special_effect):
    return IfCharacterSpecialEffectState(condition, PLAYER, special_effect, False)


def IfCharacterBackreadState(condition: int, character: gt.CharacterInt, state: bool,
                             target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    instruction_info = (4, 7)
    return numeric_instruction(instruction_info, condition, character, state,
                               target_comparison_type, target_count)

def IfCharacterBackreadEnabled(condition: int, character: gt.CharacterInt):
    return IfCharacterBackreadState(condition, character, True)

def IfCharacterBackreadDisabled(condition: int, character: gt.CharacterInt):
    return IfCharacterBackreadState(condition, character, False)


def IfTAEEventState(condition: int, character: gt.CharacterInt, tae_event_id: int, state: bool,
                    target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    instruction_info = (4, 8, [0, 0, -1, 0, 0, 0])
    return numeric_instruction(instruction_info, condition, character, tae_event_id, state,
                               target_comparison_type, target_count)

def IfHasTAEEvent(condition: int, character: gt.CharacterInt, tae_event_id: int):
    return IfTAEEventState(condition, character, tae_event_id, True)

def IfDoesNotHaveTAEEvent(condition: int, character: gt.CharacterInt, tae_event_id: int):
    return IfTAEEventState(condition, character, tae_event_id, False)


def IfHasAIStatus(condition: int, character: gt.CharacterInt, ai_status: AIStatusType,
                  target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    instruction_info = (4, 9)
    return numeric_instruction(instruction_info, condition, character, ai_status,
                               target_comparison_type, target_count)


def IfHealthValueComparison(condition: int, character: gt.CharacterInt, comparison_type: ComparisonType, value,
                            target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    instruction_info = (4, 14)
    return numeric_instruction(instruction_info, condition, character, comparison_type, value,
                               target_comparison_type, target_count)

def IfHealthValueEqual(condition: int, character: gt.CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.Equal, value)

def IfHealthValueNotEqual(condition: int, character: gt.CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.NotEqual, value)

def IfHealthValueGreaterThan(condition: int, character: gt.CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.GreaterThan, value)

def IfHealthValueLessThan(condition: int, character: gt.CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.LessThan, value)

def IfHealthValueGreaterThanOrEqual(condition: int, character: gt.CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.GreaterThanOrEqual, value)

def IfHealthValueLessThanOrEqual(condition: int, character: gt.CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.LessThanOrEqual, value)


def IfCharacterDrawGroupState(condition: int, character: gt.CharacterInt, state: bool,
                              target_comparison_type: ComparisonType = ComparisonType.Equal,
                              target_count: float = 1.0):
    """ Tests if character's draw group is currently active or inactive. """
    instruction_info = (4, 15, [0, 0, 0, 0, 0])
    return numeric_instruction(instruction_info, condition, character, state,
                               target_comparison_type, target_count)

def IfCharacterDrawGroupActive(condition: int, character: gt.CharacterInt):
    return IfCharacterDrawGroupState(condition, character, True)

def IfCharacterDrawGroupInactive(condition: int, character: gt.CharacterInt):
    return IfCharacterDrawGroupState(condition, character, False)


def IfPlayerRemainingYoelLevelComparison(condition: int, comparison_type: ComparisonType, value: int):
    """ Tests the number of remaining levels available from Yoel, I presume. """
    instruction_info = (4, 26)
    return numeric_instruction(instruction_info, condition, comparison_type, value)


def IfCharacterInvadeType(condition: int, character: gt.CharacterInt, invade_type: int,
                          target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    """ 'invade_type' has an unknown type in the EMEDF. Probably refers to the invader's covenant. """
    instruction_info = (4, 27)
    return numeric_instruction(instruction_info, condition, character, invade_type,
                               target_comparison_type, target_count)


def IfCharacterChameleonState(condition: int, character: gt.CharacterInt, chameleon_fx_id: int, is_transformed: bool):
    instruction_info = (4, 28)
    return numeric_instruction(instruction_info, condition, character, chameleon_fx_id, is_transformed)


# 5: CONDITIONS (OBJECT)
# Same new arguments as characters for the destruction test and all new tests.

def IfObjectDestructionState(condition: int, obj: gt.ObjectInt, state: bool,
                             target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    instruction_info = (5, 0)
    return numeric_instruction(instruction_info, condition, state, obj,
                               target_comparison_type, target_count)

def IfObjectDestroyed(condition: int, obj: gt.ObjectInt):
    return IfObjectDestructionState(condition, obj, True)

def IfObjectNotDestroyed(condition: int, obj: gt.ObjectInt):
    return IfObjectDestructionState(condition, obj, False)


def IfObjectBurnState(condition: int, obj: gt.ObjectInt, comparison_type: ComparisonType, state: bool,
                      target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    """ This test is used exactly once, in the High Wall of Lothric, where the 'comparison_type' is GreaterThan. I have
    no idea what that argument does. However, it's possible that 'state' isn't actually a bool, but some measure of the
    intensity of the burn state, because the event it's used in strongly suggests that a fire effect is created as long
    as the burn state is 'greater than zero'. """
    instruction_info = (5, 9)
    return numeric_instruction(instruction_info, condition, obj, comparison_type, state,
                               target_comparison_type, target_count)


def IfObjectBackreadState(condition: int, obj: gt.ObjectInt, state: bool,
                          target_comparison_type: ComparisonType = ComparisonType.Equal, target_count: float = 1.0):
    instruction_info = (5, 10)
    return numeric_instruction(instruction_info, condition, obj, state,
                               target_comparison_type, target_count)

def IfObjectBackreadEnabled(condition: int, obj: gt.ObjectInt):
    return IfObjectBackreadState(condition, obj, True)

def IfObjectBackreadDisabled(condition: int, obj: gt.ObjectInt):
    return IfObjectBackreadState(condition, obj, False)


def IfObjectBackreadState_Alternate(condition: int, obj: gt.ObjectInt, state: bool,
                                    target_comparison_type: ComparisonType = ComparisonType.Equal,
                                    target_count: float = 1.0):
    """ The fact they added this suggests that the 'alternate' version that already existed for characters is actually
    useful in some way (and they did use it in DS1). """
    instruction_info = (5, 11)
    return numeric_instruction(instruction_info, condition, obj, state,
                               target_comparison_type, target_count)

def IfObjectBackreadEnabled_Alternate(condition: int, obj: gt.ObjectInt):
    return IfObjectBackreadState_Alternate(condition, obj, True)

def IfObjectBackreadDisabled_Alternate(condition: int, obj: gt.ObjectInt):
    return IfObjectBackreadState_Alternate(condition, obj, False)


# 1000: CONTROL FLOW (BASIC)

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


# 1001: CONTROL FLOW (TIMER)

def WaitHollowArenaHalftime(match_type: HollowArenaMatchType, is_second_half: bool):
    """ 'StayParam lookup'. """
    instruction_info = (1001, 4)
    return numeric_instruction(instruction_info, match_type, is_second_half)


# 1003: CONTROL FLOW (EVENT)

def SkipLinesIfMultiplayerState(line_count, state: MultiplayerState):
    instruction_info = (1003, 5)
    return numeric_instruction(instruction_info, line_count, state)

def SkipLinesIfHost(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Host)

def SkipLinesIfClient(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Client)

def SkipLinesIfTryingToCreateSession(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.TryingToCreateSession)

def SkipLinesIfTryingToJoinSession(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.TryingToJoinSession)

def SkipLinesIfLeavingSession(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.LeavingSession)

def SkipLinesIfFailedToCreateSession(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.FailedToCreateSession)


def TerminateIfMultiplayerState(event_end_type: EventEndType, state: MultiplayerState):
    instruction_info = (1003, 6)
    return numeric_instruction(instruction_info, event_end_type, state)

def EndIfHost():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Host)

def EndIfClient():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Client)

def EndIfTryingToCreateSession():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.TryingToCreateSession)

def EndIfTryingToJoinSession():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.TryingToJoinSession)

def EndIfLeavingSession():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.LeavingSession)

def EndIfFailedToCreateSession():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.FailedToCreateSession)

def RestartIfHost():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Host)

def RestartIfClient():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Client)

def RestartIfTryingToCreateSession():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.TryingToCreateSession)

def RestartIfTryingToJoinSession():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.TryingToJoinSession)

def RestartIfLeavingSession():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.LeavingSession)

def RestartIfFailedToCreateSession():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.FailedToCreateSession)


def SkipLinesIfCoopClientCountComparison(line_count: int, comparison_type: ComparisonType, value: int):
    """ Value should be from 0 to 4. """
    instruction_info = (1003, 9, [0, 0, 0])
    return numeric_instruction(instruction_info, line_count, comparison_type, value)


def TerminateIfCoopClientCountComparison(event_end_type: EventEndType, comparison_type: ComparisonType, value: int):
    instruction_info = (1003, 10, [0, 0, 0])
    return numeric_instruction(instruction_info, event_end_type, comparison_type, value)

def EndIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return TerminateIfCoopClientCountComparison(EventEndType.End, comparison_type, value)

def RestartIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return TerminateIfCoopClientCountComparison(EventEndType.Restart, comparison_type, value)


def GotoIfCharacterSpecialEffectState(label: Label, character: gt.CharacterInt, special_effect: int, state: bool,
                                      target_comparison_type: ComparisonType = ComparisonType.Equal,
                                      target_count: int = 1):
    """ Note that 'target_count' is now an integer again... """
    instruction_info = (1003, 11)
    return numeric_instruction(instruction_info, label, character, special_effect, state,
                               target_comparison_type, target_count)

def GotoIfCharacterHasSpecialEffect(label: Label, character: gt.CharacterInt, special_effect: int,
                                    target_comparison_type: ComparisonType = ComparisonType.Equal,
                                    target_count: int = 1):
    return GotoIfCharacterSpecialEffectState(label, character, special_effect, True,
                                             target_comparison_type, target_count)

def GotoIfCharacterDoesNotHaveSpecialEffect(label: Label, character: gt.CharacterInt, special_effect: int,
                                            target_comparison_type: ComparisonType = ComparisonType.Equal,
                                            target_count: int = 1):
    return GotoIfCharacterSpecialEffectState(label, character, special_effect, False,
                                             target_comparison_type, target_count)


def GotoIfPlayerOwnWorldState(label: Label, not_in_own_world: bool):
    instruction_info = (1003, 12)
    return numeric_instruction(instruction_info, label, not_in_own_world)

def GotoIfPlayerInOwnWorld(label: Label):
    return GotoIfPlayerOwnWorldState(label, False)

def GotoIfPlayerNotInOwnWorld(label: Label):
    return GotoIfPlayerOwnWorldState(label, True)

def TerminateIfPlayerOwnWorldState(event_end_type: EventEndType, not_in_own_world: bool):
    instruction_info = (1003, 13)
    return numeric_instruction(instruction_info, event_end_type, not_in_own_world)

def EndIfPlayerOwnWorldState(not_in_own_world: bool):
    return TerminateIfPlayerOwnWorldState(EventEndType.End, not_in_own_world)

def EndIfPlayerInOwnWorld():
    return TerminateIfPlayerOwnWorldState(EventEndType.End, False)

def EndIfPlayerNotInOwnWorld():
    return TerminateIfPlayerOwnWorldState(EventEndType.End, True)

def RestartIfPlayerOwnWorldState(not_in_own_world: bool):
    return TerminateIfPlayerOwnWorldState(EventEndType.Restart, not_in_own_world)

def RestartIfPlayerInOwnWorld():
    return TerminateIfPlayerOwnWorldState(EventEndType.Restart, False)

def RestartIfPlayerNotInOwnWorld():
    return TerminateIfPlayerOwnWorldState(EventEndType.Restart, True)


def SkipLinesIfClientTypeCountComparison(line_count: int, client_type: ClientType, comparison_type: ComparisonType,
                                         value: int):
    """ Value from 0 to 4. """
    instruction_info = (1003, 14, [0, 0, 0, 0])
    return numeric_instruction(instruction_info, line_count, client_type, comparison_type, value)

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


def GotoIfFlagState(label: Label, state: bool, flag_type: FlagType, flag: gt.FlagInt):
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

def GotoIfFlagOn(label: Label, flag: gt.FlagInt):
    return GotoIfFlagState(label, True, FlagType.Absolute, flag)

def GotoIfFlagOff(label: Label, flag: gt.FlagInt):
    return GotoIfFlagState(label, False, FlagType.Absolute, flag)


def GotoIfFlagRangeState(label: Label, state: RangeState, flag_type: FlagType,
                         flag_range: gt.FlagRangeOrSequence):
    instruction_info = (1003, 103)
    first_flag, last_flag = tuple(flag_range)
    return numeric_instruction(instruction_info, label, state, flag_type, first_flag, last_flag)

def GotoIfFlagRangeAllOn(label: Label, flag_range: gt.FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AllOn, FlagType.Absolute, flag_range)

def GotoIfFlagRangeAllOff(label: Label, flag_range: gt.FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AllOff, FlagType.Absolute, flag_range)

def GotoIfFlagRangeAnyOn(label: Label, flag_range: gt.FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AnyOn, FlagType.Absolute, flag_range)

def GotoIfFlagRangeAnyOff(label: Label, flag_range: gt.FlagRangeOrSequence):
    return GotoIfFlagRangeState(label, RangeState.AnyOff, FlagType.Absolute, flag_range)


def GotoIfMultiplayerState(label: Label, state: MultiplayerState):
    instruction_info = (1003, 105, [0, 0])
    return numeric_instruction(instruction_info, label, state)

def GotoIfHost(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Host)

def GotoIfClient(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Client)

def GotoIfTryingToCreateSession(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.TryingToCreateSession)

def GotoIfTryingToJoinSession(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.TryingToJoinSession)

def GotoIfLeavingSession(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.LeavingSession)

def GotoIfFailedToCreateSession(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.FailedToCreateSession)


def GotoIfMapPresenceState(label: Label, game_map: gt.MapOrSequence, state: bool):
    instruction_info = (1003, 107, [0, 0, 0, 0])
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, label, state, area_id, block_id)

def GotoIfInsideMap(label: Label, game_map: gt.MapOrSequence):
    return GotoIfMapPresenceState(label, game_map, True)

def GotoIfOutsideMap(label: Label, game_map: gt.MapOrSequence):
    return GotoIfMapPresenceState(label, game_map, False)


def GotoIfCoopClientCountComparison(label: Label, comparison_type: ComparisonType, value: int):
    instruction_info = (1003, 109, [0, 0, 0])
    return numeric_instruction(instruction_info, label, comparison_type, value)


def TerminateIfCharacterSpecialEffectState(event_end_type: EventEndType, character: gt.CharacterInt,
                                           special_effect: int, state: bool,
                                           target_comparison_type: ComparisonType = ComparisonType.Equal,
                                           target_count: int = 1):
    instruction_info = (1003, 111)
    return numeric_instruction(instruction_info, event_end_type, character, special_effect, state,
                               target_comparison_type, target_count)

def EndIfCharacterSpecialEffectState(character: gt.CharacterInt, special_effect: int, state: bool):
    return TerminateIfCharacterSpecialEffectState(EventEndType.End, character, special_effect, state)

def EndIfCharacterHasSpecialEffect(character: gt.CharacterInt, special_effect: int):
    return TerminateIfCharacterSpecialEffectState(EventEndType.End, character, special_effect, True)

def EndIfCharacterDoesNotHaveSpecialEffect(character: gt.CharacterInt, special_effect: int):
    return TerminateIfCharacterSpecialEffectState(EventEndType.End, character, special_effect, False)

def RestartIfCharacterSpecialEffectState(character: gt.CharacterInt, special_effect: int, state: bool):
    return TerminateIfCharacterSpecialEffectState(EventEndType.Restart, character, special_effect, state)

def RestartIfCharacterHasSpecialEffect(character: gt.CharacterInt, special_effect: int):
    return TerminateIfCharacterSpecialEffectState(EventEndType.Restart, character, special_effect, True)

def RestartIfCharacterDoesNotHaveSpecialEffect(character: gt.CharacterInt, special_effect: int):
    return TerminateIfCharacterSpecialEffectState(EventEndType.Restart, character, special_effect, False)

def EndIfPlayerHasSpecialEffect(special_effect: int):
    return TerminateIfCharacterSpecialEffectState(EventEndType.End, PLAYER, special_effect, True)

def EndIfPlayerDoesNotHaveSpecialEffect(special_effect: int):
    return TerminateIfCharacterSpecialEffectState(EventEndType.End, PLAYER, special_effect, False)

def RestartIfPlayerHasSpecialEffect(special_effect: int):
    return TerminateIfCharacterSpecialEffectState(EventEndType.Restart, PLAYER, special_effect, True)

def RestartIfPlayerDoesNotHaveSpecialEffect(special_effect: int):
    return TerminateIfCharacterSpecialEffectState(EventEndType.Restart, PLAYER, special_effect, False)

def SkipLinesIfCharacterSpecialEffectState(line_count: int, character: gt.CharacterInt,
                                           special_effect: int, state: bool,
                                           target_comparison_type: ComparisonType = ComparisonType.Equal,
                                           target_count: int = 1):
    instruction_info = (1003, 112, [0, 0, -1, 0, 0, 0])
    return numeric_instruction(instruction_info, line_count, character, special_effect, state,
                               target_comparison_type, target_count)

def SkipLinesIfCharacterHasSpecialEffect(line_count: int, character: gt.CharacterInt, special_effect: int):
    return SkipLinesIfCharacterSpecialEffectState(line_count, character, special_effect, True)

def SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count: int, character: gt.CharacterInt, special_effect: int):
    return SkipLinesIfCharacterSpecialEffectState(line_count, character, special_effect, False)

def SkipLinesIfPlayerHasSpecialEffect(line_count: int, special_effect: int):
    return SkipLinesIfCharacterSpecialEffectState(line_count, PLAYER, special_effect, True)

def SkipLinesIfPlayerDoesNotHaveSpecialEffect(line_count: int, special_effect: int):
    return SkipLinesIfCharacterSpecialEffectState(line_count, PLAYER, special_effect, False)


def GotoIfCharacterRegionState(label: Label, state: bool, character: gt.CharacterInt, region: gt.RegionInt,
                               min_target_count: int = 1):
    """ EMEDF does not have the final new argument listed (it's the same as the other region/distance checks). """
    instruction_info = (1003, 200)
    return numeric_instruction(instruction_info, label, state, character, region, min_target_count)

def GotoIfCharacterInsideRegion(label: Label, character: gt.CharacterInt, region: gt.RegionInt):
    return GotoIfCharacterRegionState(label, True, character, region)

def GotoIfCharacterOutsideRegion(label: Label, character: gt.CharacterInt, region: gt.RegionInt):
    return GotoIfCharacterRegionState(label, False, character, region)


def TerminateIfCharacterRegionState(event_end_type: EventEndType, state: bool, character: gt.CharacterInt,
                                    region: gt.RegionInt, min_target_count: int = 1):
    instruction_info = (1003, 201)
    return numeric_instruction(instruction_info, event_end_type, state, character, region, min_target_count)

def EndIfCharacterRegionState(state: bool, character: gt.CharacterInt, region: gt.RegionInt):
    return TerminateIfCharacterRegionState(EventEndType.End, state, character, region)

def EndIfCharacterInsideRegion(character: gt.CharacterInt, region: gt.RegionInt):
    return TerminateIfCharacterRegionState(EventEndType.End, True, character, region)

def EndIfCharacterOutsideRegion(character: gt.CharacterInt, region: gt.RegionInt):
    return TerminateIfCharacterRegionState(EventEndType.End, False, character, region)

def RestartIfCharacterRegionState(state: bool, character: gt.CharacterInt, region: gt.RegionInt):
    return TerminateIfCharacterRegionState(EventEndType.Restart, state, character, region)

def RestartIfCharacterInsideRegion(character: gt.CharacterInt, region: gt.RegionInt):
    return TerminateIfCharacterRegionState(EventEndType.Restart, True, character, region)

def RestartIfCharacterOutsideRegion(character: gt.CharacterInt, region: gt.RegionInt):
    return TerminateIfCharacterRegionState(EventEndType.Restart, False, character, region)


def SkipLinesIfCharacterRegionState(line_count: int, state: bool, character: gt.CharacterInt, region: gt.RegionInt,
                                    min_target_count: int = 1):
    instruction_info = (1003, 202)
    return numeric_instruction(instruction_info, line_count, state, character, region, min_target_count)

def SkipLinesIfCharacterInsideRegion(line_count: int, character: gt.CharacterInt, region: gt.RegionInt):
    return SkipLinesIfCharacterRegionState(line_count, True, character, region)

def SkipLinesIfCharacterOutsideRegion(line_count: int, character: gt.CharacterInt, region: gt.RegionInt):
    return SkipLinesIfCharacterRegionState(line_count, False, character, region)


def GotoIfHollowArenaMatchType(label: Label, match_type: HollowArenaMatchType):
    instruction_info = (1003, 211)
    return numeric_instruction(instruction_info, label, match_type)


# 1005: CONTROL FLOW (OBJECTS)
# Adding new arguments.

def SkipLinesIfObjectDestructionState(line_count, obj: gt.ObjectInt, state: bool,
                                      target_comparison_type: ComparisonType = ComparisonType.Equal,
                                      target_count: float = 1.0):
    """ Note change in argument order. """
    instruction_info = (1005, 1)
    return numeric_instruction(instruction_info, line_count, state, obj, target_comparison_type, target_count)

def SkipLinesIfObjectDestroyed(line_count, obj: gt.ObjectInt):
    return SkipLinesIfObjectDestructionState(line_count, obj, True)

def SkipLinesIfObjectNotDestroyed(line_count, obj: gt.ObjectInt):
    return SkipLinesIfObjectDestructionState(line_count, obj, False)


def TerminateIfObjectDestructionState(event_end_type: EventEndType, obj: gt.ObjectInt, state: bool,
                                      target_comparison_type: ComparisonType = ComparisonType.Equal,
                                      target_count: float = 1.0):
    instruction_info = (1005, 2)
    return numeric_instruction(instruction_info, event_end_type, state, obj, target_comparison_type, target_count)

def EndIfObjectDestroyed(obj: gt.ObjectInt):
    return TerminateIfObjectDestructionState(EventEndType.End, obj, True)

def EndIfObjectNotDestroyed(obj: gt.ObjectInt):
    return TerminateIfObjectDestructionState(EventEndType.End, obj, False)

def RestartIfObjectDestroyed(obj: gt.ObjectInt):
    return TerminateIfObjectDestructionState(EventEndType.Restart, obj, True)

def RestartIfObjectNotDestroyed(obj: gt.ObjectInt):
    return TerminateIfObjectDestructionState(EventEndType.Restart, obj, False)


def GotoIfObjectDestructionState(label: Label, obj: gt.ObjectInt, state: bool,
                                 target_comparison_type: ComparisonType = ComparisonType.Equal,
                                 target_count: float = 1.0):
    """ Note change in argument order. """
    instruction_info = (1005, 101, [0, 0, 0, 0, 0])
    return numeric_instruction(instruction_info, label, state, obj, target_comparison_type, target_count)

def GotoIfObjectDestroyed(label: Label, obj: gt.ObjectInt):
    return GotoIfObjectDestructionState(label, obj, True)

def GotoIfObjectNotDestroyed(label: Label, obj: gt.ObjectInt):
    return GotoIfObjectDestructionState(label, obj, False)


# 1014: LABELS

def Label(label: Union[Label, int]):
    """ Ranges from 0 to 20, inclusive, for DS3. """
    if isinstance(Label, int) and not 0 <= label <= 20:
        raise ValueError("Label index must be between 0 and 20, inclusive.")
    instruction_info = (1014, label)
    return numeric_instruction(instruction_info)


# 2002: CUTSCENES

def PlayCutsceneAndMovePlayerAndSetTimePeriod(cutscene: int, cutscene_type: CutsceneType, region: gt.RegionInt,
                                              game_map: gt.MapOrSequence, player_id: int, time_period_id: int):
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


def PlayCutsceneAndMovePlayer_Dummy(region: gt.RegionInt, game_map: gt.MapOrSequence):
    """ Likely not used, doesn't even take a cutscene ID argument. """
    instruction_info = (2002, 8, [0, 0, 0])
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, region, area_id, block_id)


def PlayCutsceneAndMovePlayerAndSetMapCeremony(cutscene: int, cutscene_type: CutsceneType, ceremony_id: int,
                                               unknown: int, region: gt.RegionInt, game_map: gt.MapOrSequence,
                                               player_id: int):
    """ I assume that this must be a map that is already loaded, like in DS1, but possibly not.

    Contains an unknown argument that may always be zero. TODO: Check.
    """
    instruction_info = (2002, 9)
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, cutscene, cutscene_type, ceremony_id, unknown, region, area_id,
                               block_id, player_id)

def PlayCutsceneAndSetMapCeremony(cutscene: int, cutscene_type: CutsceneType, ceremony_id: int, unknown: int,
                                  player_id: int):
    instruction_info = (2002, 10, [-1, 0, -1, 0])
    return numeric_instruction(instruction_info, cutscene, cutscene_type, ceremony_id, unknown, player_id)

def PlayCutsceneAndMovePlayer_WithUnknowns(cutscene: int, cutscene_type: CutsceneType, region: gt.RegionInt,
                                           game_map: gt.MapOrSequence, player_id: int, unknown1: int, unknown2: int):
    """ Unknown arguments at the end. """
    instruction_info = (2002, 11, [0, 0, 0, 0, 0, 0, 0, 0])
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, cutscene, cutscene_type, region, area_id, block_id, player_id,
                               unknown1, unknown2)

def PlayCutsceneAndMovePlayer_WithSecondRegion(cutscene: int, cutscene_type: CutsceneType, region: gt.RegionInt,
                                               game_map: gt.MapOrSequence, player_id: int, other_region: gt.RegionInt):
    """ Takes a second Region argument with unknown purpose. """
    instruction_info = (2002, 12, [0, 0, 0, 0, 0, 0, 0])
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, cutscene, cutscene_type, region, area_id, block_id, player_id,
                               other_region)


# 2003: EVENT

def SetBossHealthBarState(character: gt.CharacterInt, name: gt.EventTextInt, slot, state: bool):
    """ Argument order changed.

    Note: slot number can be 0-2 in DS3.
    """
    instruction_info = (2003, 11)
    if isinstance(slot, int) and slot not in (0, 1, 2):
        raise ValueError("Boss health bar slot must be 0, 1, or 2.")
    return numeric_instruction(instruction_info, state, character, slot, name)

def EnableBossHealthBar(character: gt.CharacterInt, name: gt.EventTextInt, slot=0):
    """ The character's health bar will appear at the bottom of the screen, with a name. """
    return SetBossHealthBarState(character, name, slot, True)

def DisableBossHealthBar(character: gt.CharacterInt, name: gt.EventTextInt = 0, slot=0):
    """ The character's health bar will disappear from the bottom of the screen.

    TODO: Confirm the below is still true in DS3 (disabling one disables all).
    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter, so only the
    first argument actually does anything. You're welcome to specify the name for clarity anyway (and vanilla events
    will show it when decompiled). """
    return SetBossHealthBarState(character, name, slot, False)


def HandleMinibossDefeat(miniboss_id: int):
    instruction_info = (2003, 15, [0])
    return numeric_instruction(instruction_info, miniboss_id)


def ForceAnimation(entity: gt.AnimatedInt, animation_id: int, loop: bool = False, wait_for_completion: bool = False,
                   skip_transition: bool = False, unknown1: int = 0, unknown2: float = 0.0):
    """ TODO: Confirm default values for unknown1 and unknown2 so I can keep my other defaults and arg order. """
    instruction_info = (2003, 18, [0, -1, 0, 0, 0, 0, 0])
    return numeric_instruction(instruction_info, entity, animation_id, loop, wait_for_completion, skip_transition,
                               unknown1, unknown2)


def Unknown_2003_27(arg1: int):
    """ No information. """
    instruction_info = (2003, 27)
    return numeric_instruction(instruction_info, arg1)


def EventValueOperation(source_flag: gt.FlagInt, source_flag_bit_count: int, operand: int, target_flag: gt.FlagInt,
                        target_flag_bit_count: int, calculation_type: CalculationType):
    """ Performs a binary operation on the source flag and operand value, and stores the result in the target flag. """
    instruction_info = (2003, 41)
    return numeric_instruction(instruction_info, source_flag, source_flag_bit_count, operand, target_flag,
                               target_flag_bit_count, calculation_type)


def StoreItemAmountSpecifiedByFlagValue(item_type: ItemType, item: gt.ItemInt, flag: gt.FlagInt, bit_count: int):
    """ Stores some amount of items read from a flag array. """
    instruction_info = (2003, 42)
    return numeric_instruction(instruction_info, item_type, item, flag, bit_count)

def GivePlayerItemAmountSpecifiedByFlagValue(item_type: ItemType, item: gt.ItemInt, flag: gt.FlagInt, bit_count: int):
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


def SetMapHitGridCorrespondence(hitbox: gt.HitboxInt, level: int, grid_coord_x: int, grid_coord_y: int, state: bool):
    instruction_info = (2003, 45)
    return numeric_instruction(instruction_info, hitbox, level, grid_coord_x, grid_coord_y, state)

def EnableMapHitGridCorrespondence(hitbox: gt.HitboxInt, level: int, grid_coord_x: int, grid_coord_y: int):
    return SetMapHitGridCorrespondence(hitbox, level, grid_coord_x, grid_coord_y, True)

def DisableMapHitGridCorrespondence(hitbox: gt.HitboxInt, level: int, grid_coord_x: int, grid_coord_y: int):
    return SetMapHitGridCorrespondence(hitbox, level, grid_coord_x, grid_coord_y, False)


def SetMapContentImageDisplayState(content_image_part_id: int, state: bool):
    instruction_info = (2003, 46)
    return numeric_instruction(instruction_info, content_image_part_id, state)


def SetMapBoundariesDisplay(hierarchy: int, grid_coord_x: int, grid_coord_y: int, state: bool):
    instruction_info = (2003, 47)
    return numeric_instruction(instruction_info, hierarchy, grid_coord_x, grid_coord_y, state)


def SetAreaWind(region: gt.RegionInt, state: bool, duration: float, wind_parameter_id: int):
    instruction_info = (2003, 48)
    return numeric_instruction(instruction_info, region, state, duration, wind_parameter_id)


def MovePlayerToRespawnPoint(respawn_point_id: int):
    instruction_info = (2003, 49, [0])
    return numeric_instruction(instruction_info, respawn_point_id)


def StartEnemySpawner(spawner_id: int):
    instruction_info = (2003, 50, [-1])
    return numeric_instruction(instruction_info, spawner_id)


def SummonNPC(sign_type: Union[SingleplayerSummonSignType, int], character: gt.CharacterInt, region: gt.RegionInt,
              summon_flag: gt.FlagInt, dismissal_flag: gt.FlagInt):
    instruction_info = (2003, 51)
    return numeric_instruction(instruction_info, sign_type, character, region, summon_flag, dismissal_flag)


def InitializeWarpObject(warp_object_id: int):
    instruction_info = (2003, 52, [0])
    return numeric_instruction(instruction_info, warp_object_id)


def MakeEnemyAppear(character: gt.CharacterInt):
    instruction_info = (2003, 54)
    return numeric_instruction(instruction_info, character)


def SetCurrentMapCeremony(ceremony_id: int):
    instruction_info = (2003, 57)
    return numeric_instruction(instruction_info, ceremony_id)


def SetMapCeremony(game_map: gt.MapOrSequence, ceremony_id: int):
    instruction_info = (2003, 59)
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, area_id, block_id, ceremony_id)


def DisplayEpitaphMessage(message: gt.EventTextInt):
    instruction_info = (2003, 61)
    return numeric_instruction(instruction_info, message)


def SetNetworkConnectedFlagState(flag: gt.FlagInt, state: FlagState):
    instruction_info = (2003, 62)
    return numeric_instruction(instruction_info, flag, state)


def SetNetworkConnectedFlagRangeState(flag_range: gt.FlagRangeOrSequence, state: RangeState):
    instruction_info = (2003, 63)
    first_flag, last_flag = tuple(flag_range)
    return numeric_instruction(instruction_info, first_flag, last_flag, state)


def SetOmissionModeCounts(level_1_count: int, level_2_count: int):
    instruction_info = (2003, 64)
    return numeric_instruction(instruction_info, level_1_count, level_2_count)


def ResetOmissionModeCountsToDefault():
    instruction_info = (2003, 65)
    return numeric_instruction(instruction_info)


def InitializeCrowTrade(item_type: ItemType, item_id: gt.ItemInt, item_lot_id: gt.ItemLotInt,
                        trade_completed_flag: gt.FlagInt, crow_response_flag: gt.FlagInt):
    instruction_info = (2003, 66)
    return numeric_instruction(instruction_info, item_type, item_id, item_lot_id, trade_completed_flag,
                               crow_response_flag)


def InitializeCrowTradeRegion(region: gt.RegionInt):
    instruction_info = (2003, 67)
    return numeric_instruction(instruction_info, region)


def SetNetworkInteractionState(state: bool):
    instruction_info = (2003, 70)
    return numeric_instruction(instruction_info, state)


def SetHUDVisibility(is_invisible: bool):
    instruction_info = (2003, 71)
    return numeric_instruction(instruction_info, is_invisible)

def EnableHUDVisibility():
    return SetHUDVisibility(False)

def DisableHUDVisibility():
    return SetHUDVisibility(True)


def SetBonfireWarpingState(bonfire: gt.ObjectInt, animation: int, state: bool):
    """ I assume the bonfire entity should be the object. """
    instruction_info = (2003, 72)
    return numeric_instruction(instruction_info, bonfire, animation, state)

def EnableBonfireWarping(bonfire: gt.ObjectInt, animation: int):
    return SetBonfireWarpingState(bonfire, animation, True)

def DisableBonfireWarping(bonfire: gt.ObjectInt, animation: int):
    return SetBonfireWarpingState(bonfire, animation, False)


def SetAutogeneratedEventSpecificFlag_1(unknown1: int, unknown2: int):
    """ No idea, but probably relates to setting the flag whose ID matches the event ID. """
    instruction_info = (2003, 73)
    return numeric_instruction(instruction_info, unknown1, unknown2)


def HandleBossDefeatAndDisplayBanner(boss: int, banner: BannerType):
    """ Not sure if the 'boss' is a GameAreaParam or just Character. """
    instruction_info = (2003, 74)
    return numeric_instruction(instruction_info, boss, banner)


def SetAutogeneratedEventSpecificFlag_2(unknown1: int, unknown2: int):
    """ No idea, but probably relates to setting the flag whose ID matches the event ID. """
    instruction_info = (2003, 75)
    return numeric_instruction(instruction_info, unknown1, unknown2)


def SetLoadingScreenTipsState(tips_disabled: bool):
    instruction_info = (2003, 76)
    return numeric_instruction(instruction_info, tips_disabled)

def EnableLoadingScreenTips():
    return SetLoadingScreenTipsState(False)

def DisableLoadingScreenTips():
    return SetLoadingScreenTipsState(True)


def AwardGestureItem(gesture_id: int, item_type: ItemType, item_id: int):
    """ Not sure if this awards an actual gesture (then why multiple args?) or awards it based on a gesture (but then
    why not region-specific?). """
    instruction_info = (2003, 77)
    return numeric_instruction(instruction_info, gesture_id, item_type, item_id)


def SendNPCSummonHome(character: gt.CharacterInt):
    """ Identical to Bloodborne version, but with different index. """
    instruction_info = (2003, 78, [-1])
    return numeric_instruction(instruction_info, character)


def Unknown_2003_79(unknown1: int):
    instruction_info = (2003, 79)
    return numeric_instruction(instruction_info, unknown1)


def SetDecoratedBossHealthBarState(state: bool, character: gt.CharacterInt, slot: int, name: gt.EventTextInt,
                                   decoration: int):
    """ Pretty cool; not sure when this is used in the vanilla game or what decorations are available (apparently 255).
    As in Bloodborne, slot must be from 0 to 2. """
    if not 0 <= slot <= 2:
        raise ValueError("Boss health bar slot must be between 0 (lowermost) and 2 (uppermost). ")
    instruction_info = (2003, 80)
    return numeric_instruction(instruction_info, state, character, slot, name, decoration)

def EnableDecoratedBossHealthBar(character: gt.CharacterInt, slot: int, name: gt.EventTextInt, decoration: int):
    return SetDecoratedBossHealthBarState(True, character, slot, name, decoration)

def DisableDecoratedBossHealthBar(character: gt.CharacterInt, slot: int, name: gt.EventTextInt, decoration: int):
    return SetDecoratedBossHealthBarState(False, character, slot, name, decoration)


def PlaceNPCSummonSign_WithoutEmber(sign_type: SummonSignType, character: gt.CharacterInt, region: gt.RegionInt,
                                    summon_flag: gt.FlagInt, dismissal_flag: gt.FlagInt):
    instruction_info = (2003, 81)
    return numeric_instruction(instruction_info, sign_type, character, region, summon_flag, dismissal_flag)


# 2004: CHARACTER

def AddSpecialEffect(character: gt.CharacterInt, special_effect_id: int):
    """ 'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will do
    nothing if the character already has the special effect active (i.e. they do not stack or even reset timers).

    This version is the same as DS1, without the extra argument added in Bloodborne.
    """
    instruction_info = (2004, 8)
    return numeric_instruction(instruction_info, character, special_effect_id)


def RotateToFaceEntity(character: gt.CharacterInt, target_entity: gt.CoordEntityInt, animation: int,
                       wait_for_completion: bool = False):
    """ Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at least.)

    The Bloodborne version allows you to force an animation at the same time and optionally wait until that animation
    is completed. (I assume a value of -1 avoids it.)
    """
    instruction_info = (2004, 14, [0, 0, 0, 0])
    return numeric_instruction(instruction_info, character, target_entity, animation, wait_for_completion)


def ChangeCharacterCloth(character: gt.CharacterInt, bit_count: int, state_id: int):
    instruction_info = (2004, 48, [0, 0, 0])
    return numeric_instruction(instruction_info, character, bit_count, state_id)


def ChangePatrolBehavior(character: gt.CharacterInt, patrol_information_id: int):
    """ I don't know what a 'patrol_information_id' actually is. """
    instruction_info = (2004, 49, [0, 0])
    return numeric_instruction(instruction_info, character, patrol_information_id)


def SetLockOnPoint(character: gt.CharacterInt, lock_on_model_point: int, state: bool):
    """ Presumably changes the point that is locked on to by the player. """
    instruction_info = (2004, 50)
    return numeric_instruction(instruction_info, character, lock_on_model_point, state)


def Test_RequestRagdollRestraint(recipient_character: gt.CharacterInt, recipient_target_rigid_index: int,
                                 recipient_model_point: int, attachment_character: gt.CharacterInt,
                                 attachment_target_rigid_index: int, attachment_model_point: int):
    instruction_info = (2004, 51)
    return numeric_instruction(instruction_info, recipient_character, recipient_target_rigid_index,
                               recipient_model_point, attachment_character, attachment_target_rigid_index,
                               attachment_model_point)


def ChangePlayerCharacterInitParam(character_init_param: int):
    """ I assume this affects the player. """
    instruction_info = (2004, 52, [0])
    return numeric_instruction(instruction_info, character_init_param)


def AdaptSpecialEffectHealthChangeToNPCPart(character: gt.CharacterInt):
    instruction_info = (2004, 53, [-1])
    return numeric_instruction(instruction_info, character)


def ImmediateActivate(character: gt.CharacterInt, state: bool):
    """ Not sure. Sets draw state *really* quickly? """
    instruction_info = (2004, 54)
    return numeric_instruction(instruction_info, character, state)


def SetCharacterTalkRange(character: gt.CharacterInt, distance: float):
    instruction_info = (2004, 55)
    return numeric_instruction(instruction_info, character, distance)


def IncrementCharacterNewGameCycle(character: gt.CharacterInt):
    """ Interesting - apparently you can increase the NG+ level of a specific character. (No reset function, but it
    would probably reset on map reload.) """
    instruction_info = (2004, 57)
    return numeric_instruction(instruction_info, character)


def SetMultiplayerBuffs_NonBoss(character: gt.CharacterInt, state: bool):
    instruction_info = (2004, 58)
    return numeric_instruction(instruction_info, character, state)


def Unknown_2004_59(character: gt.CharacterInt, state: bool):
    """ Examine usage. """
    instruction_info = (2004, 59)
    return numeric_instruction(instruction_info, character, state)


def SetPlayerRemainingYoelLevels(level_count: int):
    instruction_info = (2004, 60)
    return numeric_instruction(instruction_info, level_count)


# 2005: OBJECT

def ExtinguishBurningObjects():
    instruction_info = (2005, 16)
    return numeric_instruction(instruction_info)


def ShowObjectByMapCeremony(obj: gt.ObjectInt, ceremony_id: int, unknown: int):
    instruction_info = (2005, 17)
    return numeric_instruction(instruction_info, obj, ceremony_id, unknown)


def DestroyObject_NoSlot(obj: gt.ObjectInt):
    """ No 'slot' argument here. """
    instruction_info = (2005, 19)
    return numeric_instruction(instruction_info, obj)


# 2007: MESSAGE

def DisplayDialogAndSetFlags(message: gt.EventTextInt, button_type: ButtonType, number_buttons: NumberButtons,
                             anchor_entity: gt.CoordEntityInt, display_distance: float, left_flag: gt.FlagInt,
                             right_flag: gt.FlagInt, cancel_flag: gt.FlagInt):
    """ Displays a dialog and enables one of three flags, depending on the player's response. Very useful. """
    instruction_info = (2007, 10, [0, 0, 0, -1, 0, 0, 0, 0])
    return numeric_instruction(instruction_info, message, button_type, number_buttons, anchor_entity, display_distance,
                               left_flag, right_flag, cancel_flag)


def DisplayAreaWelcomeMessage(message: gt.EventTextInt):
    """ Not sure what this looks like exactly. """
    instruction_info = (2007, 11)
    return numeric_instruction(instruction_info, message)


def DisplayHollowArenaMessage(message: gt.EventTextInt, unknown: int, pad_enabled: bool):
    instruction_info = (2007, 12)
    return numeric_instruction(instruction_info, message, unknown, pad_enabled)


# 2009: SCRIPT

def RegisterHealingFountain(flag: gt.FlagInt, obj: gt.ObjectInt, reaction_distance: float, reaction_angle: float,
                            initial_sword_number: int, sword_level: int):
    """ No idea what this is. Apparently DS1 also has a version of this with less arguments. """
    instruction_info = (2009, 5)
    return numeric_instruction(instruction_info, flag, obj, reaction_distance, reaction_angle, initial_sword_number,
                               sword_level)


def BanishInvaders(unknown: int):
    instruction_info = (2009, 8)
    return numeric_instruction(instruction_info, unknown)


def BanishPhantomsAndUpdateServerPvPStats(unknown: int):
    instruction_info = (2009, 10)
    return numeric_instruction(instruction_info, unknown)


def BanishPhantoms(unknown: int):
    instruction_info = (2009, 11)
    return numeric_instruction(instruction_info, unknown)


# 2010: SOUND

def SetBossMusicState(sound_id: int, state: bool):
    """ Not sure how this differs from the standard map sound instructions. """
    instruction_info = (2010, 4, [0, 0])
    return numeric_instruction(instruction_info, sound_id, state)

def EnableBossMusic(sound_id: int):
    return SetBossMusicState(sound_id, True)

def DisableBossMusic(sound_id: int):
    return SetBossMusicState(sound_id, False)


def NotifyDoorEventSoundDampening(entity_id: int, state: DoorState):
    """ No idea what this is or what entity the first argument is. Probably the door object. """
    instruction_info = (2010, 5, [0, 0])
    return numeric_instruction(instruction_info, entity_id, state)


def SetMapSoundWithFade(sound_id: int, state: bool, fade_duration: float):
    instruction_info = (2010, 6)
    return numeric_instruction(instruction_info, sound_id, state, fade_duration)

def EnableMapSoundWithFade(sound_id: int, fade_duration: float):
    return SetMapSoundWithFade(sound_id, True, fade_duration)

def DisableMapSoundWithFade(sound_id: int, fade_duration: float):
    return SetMapSoundWithFade(sound_id, False, fade_duration)


def Unknown_2010_07(entity: int):
    instruction_info = (2010, 7)
    return numeric_instruction(instruction_info, entity)


# 2011: HITBOX

def SetHitboxResState(hitbox: gt.HitboxInt, state: bool):
    """ No idea what this is. """
    instruction_info = (2011, 3, [-1, 0])
    return numeric_instruction(instruction_info, hitbox, state)


def ActivateHitboxAndCreateNavimesh(hitbox: gt.HitboxInt, state: bool):
    instruction_info = (2011, 4)
    return numeric_instruction(instruction_info, hitbox, state)


# MAP

# 2012: MAP

def SetAreaWelcomeMessageState(state: bool):
    instruction_info = (2012, 8)
    return numeric_instruction(instruction_info, state)

def EnableAreaWelcomeMessage():
    return SetAreaWelcomeMessageState(True)

def DisableAreaWelcomeMessage():
    return SetAreaWelcomeMessageState(False)


# 2013: PLAY LOG

def CreatePlayLog(name: gt.StringOffsetInt):
    instruction_info = (2013, 1, [0])
    return numeric_instruction(instruction_info, name)

def StartPlayLogMeasurement(measurement_id: int, name: gt.StringOffsetInt, overwrite: bool):
    instruction_info = (2013, 2, [0, 0, 0])
    return numeric_instruction(instruction_info, measurement_id, name, overwrite)

def StopPlayLogMeasurement(measurement_id: int):
    instruction_info = (2013, 3, [0])
    return numeric_instruction(instruction_info, measurement_id)

def PlayLogParameterOutput(category: PlayerPlayLogParameter, name: gt.StringOffsetInt,
                           output_multiplayer_state: PlayLogMultiplayerType):
    instruction_info = (2013, 4, [0, 0, 0])
    return numeric_instruction(instruction_info, category, name, output_multiplayer_state)
