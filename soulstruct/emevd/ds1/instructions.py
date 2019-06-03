""" Full instruction set for DS1 and DSR. I haven't yet put any restrictions on using the new DSR instructions in
PTDE, so beware of that. """

from __future__ import annotations
from soulstruct.emevd.shared.instructions import *
from soulstruct.emevd.game_types import *
from soulstruct.emevd.ds1.enums import *


# MULTIPLAYER STATE

def SkipLinesIfMultiplayerState(line_count, state: MultiplayerState):
    event_format = ('1003', '05', 'Bb')
    return format_instruction(event_format, line_count, state)

def SkipLinesIfHost(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Host)

def SkipLinesIfClient(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Client)

def SkipLinesIfMultiplayer(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Multiplayer)


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

def IfSingleplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Singleplayer)


# BOSS

def SetBossHealthBarState(character: CharacterInt, name: TextInt, slot, state: bool):
    """ Note: slot number can be 0-1 in DS1. """
    event_format = ('2003', '11', 'bihh')
    if isinstance(slot, int) and slot not in (0, 1):
        raise ValueError("Boss health bar slot must be 0 or 1.")
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


# MISC.

def ActivateKillplaneForModel(game_map: Map, y_threshold, target_model_id):
    """ Not used much. Activates a horizontal killplane that only affects a particular model ID. """
    event_format = ('2003', '41', 'iifi')
    return format_instruction(event_format, game_map.area_id, game_map.block_id, y_threshold, target_model_id)


def AddSpecialEffect(character: CharacterInt, special_effect_id: int):
    """ 'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will do
    nothing if the character already has the special effect active (i.e. they do not stack or even reset timers). """
    event_format = ('2004', '08', 'ii')
    return format_instruction(event_format, character, special_effect_id)


def RotateToFaceEntity(character: CharacterInt, target_entity: MapEntityInt):
    """ Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at least.)
    """
    event_format = ('2004', '14', 'ii')
    return format_instruction(event_format, character, target_entity)


def RegisterHealingFountain(flag: FlagInt, obj: ObjectInt):
    """ No idea what this is. Clearly unused. The Bloodborne version has more arguments. """
    event_format = ('2009', '05', 'ii')
    return format_instruction(event_format, flag, obj)


# REMASTERED ONLY
def Unknown_3_23(condition: int, arg1: int, arg2: int):
    """ Unknown command. 'arg1' and 'arg2' appear to both always be zero. """
    event_format = ('   3', '23', 'bBB')
    return format_instruction(event_format, condition, arg1, arg2)


# REMASTERED ONLY
def IfMultiplayerCount(condition: int, arg1: int, arg2: int):
    """ Unknown arguments. Useful for Battle of Stoicism only, so probably useless to you. """
    event_format = ('   3', '24', 'bBB')
    return format_instruction(event_format, condition, arg1, arg2)


# REMASTERED ONLY
def Unknown_4_15(condition: int, arg1: int):
    event_format = ('   4', '15', 'bI')
    return format_instruction(event_format, condition, arg1)


# REMASTERED ONLY
def Unknown_4_16(condition: int, arg1: int, arg2: int, arg3: int):
    event_format = ('   4', '16', 'bBBB')
    return format_instruction(event_format, condition, arg1, arg2, arg3)


# REMASTERED ONLY
def IfArenaMatchmaking(condition: int):
    event_format = ('   4', '17', 'b')
    return format_instruction(event_format, condition)


# REMASTERED ONLY
def Unknown_2000_06(arg1: int):
    event_format = ('2000', '06', 'i')
    return format_instruction(event_format, arg1)


# REMASTERED ONLY
def PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect1(condition: int, playback_method: CutsceneType,
                                                         first_region: Region, last_region: Region, game_map: GameMap):
    event_format = ('2002', '06', 'biIIiBB')
    area_id, block_id = tuple(game_map)
    return format_instruction(event_format, condition, playback_method, first_region, last_region, area_id, block_id)


# REMASTERED ONLY
def PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect2(condition: int, playback_method: CutsceneType,
                                                         first_region: RegionInt, last_region: RegionInt,
                                                         game_map: GameMap):
    event_format = ('2002', '07', 'biIIiBB')
    area_id, block_id = tuple(game_map)
    return format_instruction(event_format, condition, playback_method, first_region, last_region, area_id, block_id)


# REMASTERED ONLY
def CopyEventValue(source_flag: FlagInt, destination_flag: FlagInt, bit_count: int):
    event_format = ('2003', '42', 'iiB')
    return format_instruction(event_format, source_flag, destination_flag, bit_count)


# REMASTERED ONLY
def Unknown_2003_43(flag: FlagInt, bit_count: int, arg1: int, arg2: int):
    event_format = ('2003', '43', 'iiBB')
    return format_instruction(event_format, flag, bit_count, arg1, arg2)


# REMASTERED ONLY
def ForceAnimation_WithUnknownEffect1(entity: AnimatedInt, animation: int, loop: bool, wait_for_completion: bool,
                                      skip_transition: bool, arg1: int):
    event_format = ('2003', '44', 'iiBBBB')
    return format_instruction(event_format, entity, animation, loop, wait_for_completion, skip_transition, arg1)


# REMASTERED ONLY
def ForceAnimation_WithUnknownEffect2(entity: AnimatedInt, animation: int, loop: bool, wait_for_completion: bool,
                                      skip_transition: bool, arg1: float):
    event_format = ('2003', '46', 'iiBBBf')
    return format_instruction(event_format, entity, animation, loop, wait_for_completion, skip_transition, arg1)


# REMASTERED ONLY
def Unknown_2003_48(entity: AnimatedInt, arg1: int, model_point: int, magic_id: int, shoot_angle_x: int,
                    shoot_angle_y: int, shoot_angle_z: int):
    event_format = ('2003', '48', 'iiiiiii')
    return format_instruction(event_format, entity, arg1, model_point, magic_id, shoot_angle_x, shoot_angle_y,
                              shoot_angle_z)


# REMASTERED ONLY
def EraseNPCSummonSign(summoned_character: CharacterInt):
    event_format = ('2003', '49', 'i')
    return format_instruction(event_format, summoned_character)


# REMASTERED ONLY
def FadeOutCharacter(character: CharacterInt, duration: float):
    event_format = ('2004', '48', 'if')
    return format_instruction(event_format, character, duration)


# REMASTERED ONLY
def FadeInCharacter(character: CharacterInt, duration: float):
    event_format = ('2004', '49', 'if')
    return format_instruction(event_format, character, duration)
