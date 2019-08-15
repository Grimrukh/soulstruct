"""Full instruction set for DS1 (both PTD and DSR). 

I haven't yet put any restrictions on using the new DSR instructions in PTD, so beware of that.
"""
from __future__ import annotations
from soulstruct.events.core import set_instruction_arg_types
from soulstruct.events.shared.instructions import *
from soulstruct.enums.darksouls1 import *


INSTRUCTION_ARG_TYPES = {
    2000: {
        0: 'iII', 1: 'iI', 2: 'B', 3: 'B', 4: 'I', 5: 'B'},
    2001: {},
    2002: {
        1: 'iI', 2: 'iIiBB', 3: 'iIi', 4: 'iIiBBi', 5: 'iIffifi'},
    2003: {
        1: 'iiBB', 2: 'iB', 3: 'iB', 4: 'i', 
        5: 'iiiiiii', 6: 'iB', 7: 'iB', 8: 'iiB', 9: 'i', 
        10: 'h', 11: 'bihh', 12: 'i', 13: 'iIB', 14: 'BBi', 
        15: 'i', 16: 'I', 17: 'IIB', 18: 'iiBBB', 19: 'hh', 
        20: 'i', 21: 'B', 22: 'iiB', 23: 'i', 24: 'iii', 
        25: 'iiiii', 26: 'iB', 27: 'B', 28: 'i', 29: 'Bb', 
        30: 'B', 31: 'iII', 32: 'iI', 33: 'i', 34: 'iiii', 
        35: 'ii', 36: 'i', 37: '', 38: '', 39: '', 
        40: '', 41: 'iifi', 49: 'i'},
    2004: {
        1: 'iB', 2: 'iB', 3: 'iBii', 4: 'iB', 
        5: 'iB', 6: 'iiB', 7: 'i', 8: 'ii', 9: 'iiiiii', 
        10: 'iB', 11: 'ii', 12: 'iB', 13: 'ii', 14: 'ii', 
        15: 'iB', 16: 'i', 17: 'iiB', 18: 'iif', 19: 'ii', 
        20: 'i', 21: 'ii', 22: 'ihhiffBB', 23: 'iiiB', 24: 'iiii', 
        25: 'iif', 26: 'iBB', 27: 'iBB', 28: 'ii', 29: 'iB', 
        30: 'iB', 31: 'iB', 32: 'iiBii', 33: 'ii', 34: 'iBb', 
        35: 'iB', 36: 'iii', 37: 'i', 38: 'B', 39: 'iB', 
        40: 'iBiii', 41: 'iBii', 42: 'iBiii', 43: 'iB', 44: 'iB', 
        45: 'ii', 46: 'B', 47: ''},
    2005: {
        1: 'ib', 2: 'i', 3: 'iB', 4: 'iB', 
        5: 'iii', 6: 'iiB', 7: 'ii', 8: 'ib', 9: 'iiiiifff', 
        10: 'iBBB', 11: 'iih', 12: 'i', 13: 'iB', 14: 'iiiB', 
        15: 'i'},
    2006: {
        1: 'iB', 2: 'i', 3: 'iiii', 4: 'iii', 5: 'ii'},
    2007: {
        1: 'ihhif', 2: 'B', 3: 'iB', 4: 'iB', 
        5: 'i', 6: 'i', 7: 'i', 8: 'i', 9: 'i'},
    2008: {
        1: 'ii', 2: 'iiiiff', 3: 'BBH'},
    2009: {
        0: 'iii', 1: 'iii', 2: 'iii', 3: 'iiffi', 4: 'i', 5: 'ii', 6: 'B'},
    2010: {
        1: 'BHiii', 2: 'iii', 3: 'iB'},
    2011: {
        1: 'iB', 2: 'iB'},
    2012: {
        1: 'iB'},
    1000: {
        0: 'Bb', 1: 'BBb', 2: 'BBb', 3: 'B', 4: 'B', 
        5: 'Bbii', 6: 'Bbii', 7: 'BBb', 8: 'BBb', 9: 'f'},
    1001: {
        0: 'f', 1: 'i', 2: 'ff', 3: 'ii'},
    1003: {
        0: 'BBi', 1: 'BBBi', 2: 'BBBi', 3: 'BBBii', 4: 'BBBii', 
        5: 'Bb', 6: 'Bb', 7: 'BBBB', 8: 'BBBB'},
    1005: {
        0: 'Bi', 1: 'BBi', 2: 'BBi'},
    0: {
        0: 'bBb', 1: 'bbii'},
    1: {
        0: 'bf', 1: 'bi', 2: 'bff', 3: 'bii'},
    3: {
        0: 'bBBi', 1: 'bBBii', 2: 'bBii', 3: 'bBiif', 4: 'bBiB', 
        5: 'biifhfiBi', 6: 'bb', 7: 'bBi', 8: 'bBBB', 9: 'bI', 
        10: 'bBiibi', 11: 'bBBB', 12: 'biBBI', 13: 'biifhfiBi', 14: 'bi', 
        15: 'bii', 16: 'bBiB', 17: 'bBB', 18: 'biifhfiBii', 19: 'biifhfiBii', 
        20: 'biBBiB', 21: 'bB', 22: 'bB'},
    4: {0: 'biB', 1: 'bii', 2: 'bibf', 3: 'bib', 4: 'biiB', 
        5: 'biiB', 6: 'biiib', 7: 'biB', 8: 'biiB', 9: 'biB', 
        10: 'bB', 11: 'bB', 12: 'bB', 13: 'bBI', 14: 'biBi'},
    5: {
        0: 'bBi', 1: 'bii', 2: 'bi', 3: 'bibi'},
    11: {
        0: 'bi', 1: 'bi', 2: 'bi'}
}


set_instruction_arg_types(INSTRUCTION_ARG_TYPES)


def IfCharacterRegionState(condition, entity: gt.AnimatedInt, region: gt.RegionInt, state: bool):
    instruction_info = (3, 2)
    return numeric_instruction(instruction_info, condition, state, entity, region)

def IfCharacterInsideRegion(condition: int, entity: gt.AnimatedInt, region: gt.RegionInt):
    return IfCharacterRegionState(condition, entity, region, True)

def IfCharacterOutsideRegion(condition: int, entity: gt.AnimatedInt, region: gt.RegionInt):
    return IfCharacterRegionState(condition, entity, region, False)

def IfPlayerInsideRegion(condition: int, region: gt.RegionInt):
    return IfCharacterRegionState(condition, PLAYER, region, True)

def IfPlayerOutsideRegion(condition: int, region: gt.RegionInt):
    return IfCharacterRegionState(condition, PLAYER, region, False)


# MULTIPLAYER STATE

def SkipLinesIfMultiplayerState(line_count, state: MultiplayerState):
    instruction_info = (1003, 5)
    return numeric_instruction(instruction_info, line_count, state)

def SkipLinesIfHost(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Host)

def SkipLinesIfClient(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Client)

def SkipLinesIfMultiplayer(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Multiplayer)


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

def IfSingleplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Singleplayer)


# BOSS

def SetBossHealthBarState(character: gt.CharacterInt, name: gt.EventTextInt, slot, state: bool):
    """ Note: slot number can be 0-1 in DS1. """
    instruction_info = (2003, 11)
    if isinstance(slot, int) and slot not in (0, 1):
        raise ValueError("Boss health bar slot must be 0 or 1.")
    return numeric_instruction(instruction_info, state, character, slot, name)

def EnableBossHealthBar(character: gt.CharacterInt, name: gt.EventTextInt, slot=0):
    """ The character's health bar will appear at the bottom of the screen, with a name. """
    return SetBossHealthBarState(character, name, slot, True)

def DisableBossHealthBar(character: gt.CharacterInt, name: gt.EventTextInt = 0, slot=0):
    """ The character's health bar will disappear from the bottom of the screen.

    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter, so only the
    first argument actually does anything. You're welcome to specify the name for clarity anyway (and vanilla events
    will show it when decompiled). """
    return SetBossHealthBarState(character, name, slot, False)


# MISC.

def ActivateKillplaneForModel(game_map: gt.MapOrSequence, y_threshold, target_model_id):
    """ Not used much. Activates a horizontal killplane that only affects a particular model ID. """
    instruction_info = (2003, 41)
    return numeric_instruction(instruction_info, game_map.area_id, game_map.block_id, y_threshold, target_model_id)


def AddSpecialEffect(character: gt.CharacterInt, special_effect_id: int):
    """ 'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will do
    nothing if the character already has the special effect active (i.e. they do not stack or even reset timers). """
    instruction_info = (2004, 8)
    return numeric_instruction(instruction_info, character, special_effect_id)


def RotateToFaceEntity(character: gt.CharacterInt, target_entity: gt.CoordEntityInt):
    """ Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at least.)
    """
    instruction_info = (2004, 14)
    return numeric_instruction(instruction_info, character, target_entity)


def RegisterHealingFountain(flag: gt.FlagInt, obj: gt.ObjectInt):
    """ No idea what this is. Clearly unused. The Bloodborne version has more arguments. """
    instruction_info = (2009, 5)
    return numeric_instruction(instruction_info, flag, obj)


# REMASTERED ONLY
def Unknown_3_23(condition: int, arg1: int, arg2: int):
    """ Unknown command. 'arg1' and 'arg2' appear to both always be zero. """
    instruction_info = (3, 23)
    return numeric_instruction(instruction_info, condition, arg1, arg2)


# REMASTERED ONLY
def IfMultiplayerCount(condition: int, arg1: int, arg2: int):
    """ Unknown arguments. Useful for Battle of Stoicism only, so probably useless to you. """
    instruction_info = (3, 24)
    return numeric_instruction(instruction_info, condition, arg1, arg2)


# REMASTERED ONLY
def Unknown_4_15(condition: int, arg1: int):
    instruction_info = (4, 15)
    return numeric_instruction(instruction_info, condition, arg1)


# REMASTERED ONLY
def Unknown_4_16(condition: int, arg1: int, arg2: int, arg3: int):
    instruction_info = (4, 16)
    return numeric_instruction(instruction_info, condition, arg1, arg2, arg3)


# REMASTERED ONLY
def IfArenaMatchmaking(condition: int):
    instruction_info = (4, 17)
    return numeric_instruction(instruction_info, condition)


# REMASTERED ONLY
def Unknown_2000_06(arg1: int):
    instruction_info = (2000, 6)
    return numeric_instruction(instruction_info, arg1)


# REMASTERED ONLY
def PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect1(condition: int, playback_method: CutsceneType,
                                                         first_region: gt.RegionInt, last_region: gt.RegionInt,
                                                         game_map: gt.MapOrSequence):
    instruction_info = (2002, 6)
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, condition, playback_method, first_region, last_region, area_id, 
                               block_id)


# REMASTERED ONLY
def PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect2(condition: int, playback_method: CutsceneType,
                                                         first_region: gt.RegionInt, last_region: gt.RegionInt,
                                                         game_map: gt.MapOrSequence):
    instruction_info = (2002, 7)
    area_id, block_id = tuple(game_map)
    return numeric_instruction(instruction_info, condition, playback_method, first_region, last_region, area_id, 
                               block_id)


# REMASTERED ONLY
def CopyEventValue(source_flag: gt.FlagInt, destination_flag: gt.FlagInt, bit_count: int):
    instruction_info = (2003, 42)
    return numeric_instruction(instruction_info, source_flag, destination_flag, bit_count)


# REMASTERED ONLY
def Unknown_2003_43(flag: gt.FlagInt, bit_count: int, arg1: int, arg2: int):
    instruction_info = (2003, 43)
    return numeric_instruction(instruction_info, flag, bit_count, arg1, arg2)


# REMASTERED ONLY
def ForceAnimation_WithUnknownEffect1(entity: gt.AnimatedInt, animation: int, loop: bool, wait_for_completion: bool,
                                      skip_transition: bool, arg1: int):
    instruction_info = (2003, 44)
    return numeric_instruction(instruction_info, entity, animation, loop, wait_for_completion, skip_transition, arg1)


# REMASTERED ONLY
def ForceAnimation_WithUnknownEffect2(entity: gt.AnimatedInt, animation: int, loop: bool, wait_for_completion: bool,
                                      skip_transition: bool, arg1: float):
    instruction_info = (2003, 46)
    return numeric_instruction(instruction_info, entity, animation, loop, wait_for_completion, skip_transition, arg1)


# REMASTERED ONLY
def Unknown_2003_48(entity: gt.AnimatedInt, arg1: int, model_point: int, magic_id: int, shoot_angle_x: int,
                    shoot_angle_y: int, shoot_angle_z: int):
    instruction_info = (2003, 48)
    return numeric_instruction(instruction_info, entity, arg1, model_point, magic_id, shoot_angle_x, shoot_angle_y,
                               shoot_angle_z)


# REMASTERED ONLY
def EraseNPCSummonSign(summoned_character: gt.CharacterInt):
    instruction_info = (2003, 49)
    return numeric_instruction(instruction_info, summoned_character)


# REMASTERED ONLY
def FadeOutCharacter(character: gt.CharacterInt, duration: float):
    instruction_info = (2004, 48)
    return numeric_instruction(instruction_info, character, duration)


# REMASTERED ONLY
def FadeInCharacter(character: gt.CharacterInt, duration: float):
    instruction_info = (2004, 49)
    return numeric_instruction(instruction_info, character, duration)
