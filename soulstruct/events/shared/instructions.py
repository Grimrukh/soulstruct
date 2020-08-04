"""EMEVD instructions shared by all FromSoft games supported by Soulstruct.

DO NOT IMPORT THIS FILE. Import the specific game package (e.g. "from soulstruct.events.darksouls1 import *") to get the
full set of instructions, enums, game types, etc. for that game.
"""
from __future__ import annotations

import logging
from typing import Optional, Union

from soulstruct.game_types import *
from soulstruct.enums.shared import *
from soulstruct.events.numeric import to_numeric

_LOGGER = logging.getLogger(__name__)

__all__ = [
    "RunEvent",
    "Wait",
    "WaitFrames",
    "WaitRandomSeconds",
    "WaitRandomFrames",
    "WaitForNetworkApproval",
    "SetCharacterState",
    "EnableCharacter",
    "DisableCharacter",
    "SetAIState",
    "EnableAI",
    "DisableAI",
    "SetTeamType",
    "Kill",
    "EzstateAIRequest",
    "CancelSpecialEffect",
    "ResetStandbyAnimationSettings",
    "SetStandbyAnimationSettings",
    "SetGravityState",
    "EnableGravity",
    "DisableGravity",
    "SetCharacterEventTarget",
    "SetImmortalityState",
    "EnableImmortality",
    "DisableImmortality",
    "SetNest",
    "SetInvincibilityState",
    "EnableInvincibility",
    "DisableInvincibility",
    "ClearTargetList",
    "AICommand",
    "SetEventPoint",
    "SetAIParamID",
    "ReplanAI",
    "CreateNPCPart",
    "SetNPCPartHealth",
    "SetNPCPartEffects",
    "SetNPCPartBulletDamageScaling",
    "SetDisplayMask",
    "SetCollisionMask",
    "SetNetworkUpdateAuthority",
    "SetBackreadState",
    "EnableBackread",
    "DisableBackread",
    "SetHealthBarState",
    "EnableHealthBar",
    "DisableHealthBar",
    "SetCharacterCollisionState",
    "EnableCharacterCollision",
    "DisableCharacterCollision",
    "AIEvent",
    "ReferDamageToEntity",
    "SetNetworkUpdateRate",
    "SetBackreadStateAlternate",
    "DropMandatoryTreasure",
    "SetTeamTypeAndExitStandbyAnimation",
    "HumanityRegistration",
    "ResetAnimation",
    "ActivateMultiplayerBuffs",
    "SetObjectState",
    "EnableObject",
    "DisableObject",
    "DestroyObject",
    "RestoreObject",
    "SetTreasureState",
    "EnableTreasure",
    "DisableTreasure",
    "ActivateObject",
    "SetObjectActivation",
    "SetObjectActivationWithIdx",
    "EnableObjectActivation",
    "DisableObjectActivation",
    "PostDestruction",
    "CreateHazard",
    "RegisterStatue",
    "RemoveObjectFlag",
    "SetObjectInvulnerability",
    "EnableObjectInvulnerability",
    "DisableObjectInvulnerability",
    "EnableTreasureCollection",
    "SetFlagState",
    "EnableFlag",
    "DisableFlag",
    "ToggleFlag",
    "SetRandomFlagInRange",
    "EnableRandomFlagInRange",
    "DisableRandomFlagInRange",
    "ToggleRandomFlagInRange",
    "SetFlagRangeState",
    "EnableFlagRange",
    "DisableFlagRange",
    "ChangeFlagRange",
    "IncrementEventValue",
    "ClearEventValue",
    "EnableThisFlag",
    "DisableThisFlag",
    "SetEventState",
    "StopEvent",
    "RestartEvent",
    "SetCollisionState",
    "EnableCollision",
    "DisableCollision",
    "SetCollisionBackreadMaskState",
    "EnableCollisionBackreadMask",
    "DisableCollisionBackreadMask",
    "AwardItemLot",
    "AwardItemLotToHostOnly",
    "RemoveItemFromPlayer",
    "RemoveWeaponFromPlayer",
    "RemoveArmorFromPlayer",
    "RemoveRingFromPlayer",
    "RemoveGoodFromPlayer",
    "SnugglyItemDrop",
    "SetNextSnugglyTrade",
    "RequestAnimation",
    "ForceAnimation",
    "SetAnimationsState",
    "EnableAnimations",
    "DisableAnimations",
    "EndOfAnimation",
    "CreateFX",
    "DeleteFX",
    "CreateTemporaryFX",
    "CreateObjectFX",
    "DeleteObjectFX",
    "SetBackgroundMusic",
    "PlaySoundEffect",
    "SetSoundEventState",
    "EnableSoundEvent",
    "DisableSoundEvent",
    "RegisterLadder",
    "RegisterBonfire",
    "SetMapPieceState",
    "DisableMapPiece",
    "EnableMapPiece",
    "PlaceSummonSign",
    "SetDeveloperMessageState",
    "EnableSoapstoneMessage",
    "DisableSoapstoneMessage",
    "DisplayDialog",
    "DisplayBanner",
    "DisplayStatus",
    "DisplayBattlefieldMessage",
    "PlayCutscene",
    "PlayCutsceneAndMovePlayer",
    "PlayCutsceneToPlayer",
    "PlayCutsceneAndMoveSpecificPlayer",
    "PlayCutsceneAndRotatePlayer",
    "SetNavmeshType",
    "EnableNavmeshType",
    "DisableNavmeshType",
    "ToggleNavmeshType",
    "SetNetworkSync",
    "EnableNetworkSync",
    "DisableNetworkSync",
    "ClearMainCondition",
    "IssuePrefetchRequest",
    "SaveRequest",
    "TriggerMultiplayerEvent",
    "SetVagrantSpawning",
    "EnableVagrantSpawning",
    "DisableVagrantSpawning",
    "IncrementPvPSin",
    "NotifyBossBattleStart",
    "SetSpawnerState",
    "EnableSpawner",
    "DisableSpawner",
    "ShootProjectile",
    "CreateProjectileOwner",
    "WarpToMap",
    "MoveRemains",
    "Move",
    "MoveToEntity",
    "MoveAndSetDrawParent",
    "ShortMove",
    "MoveAndCopyDrawParent",
    "MoveObjectToCharacter",
    "SetRespawnPoint",
    "KillBoss",
    "IncrementNewGameCycle",
    "AwardAchievement",
    "BetrayCurrentCovenant",
    "EqualRecovery",
    "ChangeCamera",
    "SetCameraVibration",
    "SetLockedCameraSlot",
    "HellkiteBreathControl",
    "SetMapDrawParamSlot",
    # Line-for-line control flow instructions (high-level Python blocks are recommended instead)
    "SkipLines",
    "Terminate",
    "End",
    "Restart",
    "IfValueComparison",
    "AwaitConditionState",
    "AwaitConditionTrue",
    "AwaitConditionFalse",
    "SkipLinesIfConditionState",
    "SkipLinesIfConditionTrue",
    "SkipLinesIfConditionFalse",
    "SkipLinesIfFinishedConditionState",
    "SkipLinesIfFinishedConditionTrue",
    "SkipLinesIfFinishedConditionFalse",
    "TerminateIfConditionState",
    "EndIfConditionTrue",
    "EndIfConditionFalse",
    "RestartIfConditionTrue",
    "RestartIfConditionFalse",
    "TerminateIfFinishedConditionState",
    "EndIfFinishedConditionTrue",
    "EndIfFinishedConditionFalse",
    "RestartIfFinishedConditionTrue",
    "RestartIfFinishedConditionFalse",
    "IfConditionState",
    "IfConditionTrue",
    "IfConditionFalse",
    "IfTimeElapsed",
    "IfFramesElapsed",
    "IfRandomTimeElapsed",
    "IfRandomFramesElapsed",
    "SkipLinesIfMapPresenceState",
    "SkipLinesIfInsideMap",
    "SkipLinesIfOutsideMap",
    "TerminateIfMapPresenceState",
    "EndIfInsideMap",
    "EndIfOutsideMap",
    "RestartIfInsideMap",
    "RestartIfOutsideMap",
    "IfMapPresenceState",
    "IfInsideMap",
    "IfOutsideMap",
    "IfMultiplayerEvent",
    "AwaitFlagState",
    "AwaitThisEventOn",
    "AwaitThisEventOff",
    "AwaitThisEventSlotOn",
    "AwaitThisEventSlotOff",
    "AwaitFlagOn",
    "AwaitFlagOff",
    "AwaitFlagChange",
    "SkipLinesIfFlagState",
    "SkipLinesIfThisEventOn",
    "SkipLinesIfThisEventOff",
    "SkipLinesIfThisEventSlotOn",
    "SkipLinesIfThisEventSlotOff",
    "SkipLinesIfFlagOn",
    "SkipLinesIfFlagOff",
    "TerminateIfFlagState",
    "EndIfThisEventOn",
    "EndIfThisEventOff",
    "EndIfThisEventSlotOn",
    "EndIfThisEventSlotOff",
    "EndIfFlagOn",
    "EndIfFlagOff",
    "RestartIfThisEventOn",
    "RestartIfThisEventOff",
    "RestartIfThisEventSlotOn",
    "RestartIfThisEventSlotOff",
    "RestartIfFlagOn",
    "RestartIfFlagOff",
    "IfFlagState",
    "IfThisEventOn",
    "IfThisEventOff",
    "IfThisEventSlotOn",
    "IfThisEventSlotOff",
    "IfFlagOn",
    "IfFlagOff",
    "IfFlagChange",
    "SkipLinesIfFlagRangeState",
    "SkipLinesIfFlagRangeAllOn",
    "SkipLinesIfFlagRangeAllOff",
    "SkipLinesIfFlagRangeAnyOn",
    "SkipLinesIfFlagRangeAnyOff",
    "TerminateIfFlagRangeState",
    "EndIfFlagRangeAllOn",
    "EndIfFlagRangeAllOff",
    "EndIfFlagRangeAnyOn",
    "EndIfFlagRangeAnyOff",
    "RestartIfFlagRangeAllOn",
    "RestartIfFlagRangeAllOff",
    "RestartIfFlagRangeAnyOn",
    "RestartIfFlagRangeAnyOff",
    "IfFlagRangeState",
    "IfFlagRangeAllOn",
    "IfFlagRangeAllOff",
    "IfFlagRangeAnyOn",
    "IfFlagRangeAnyOff",
    "IfTrueFlagCountComparison",
    "IfTrueFlagCountEqual",
    "IfTrueFlagCountNotEqual",
    "IfTrueFlagCountGreaterThan",
    "IfTrueFlagCountLessThan",
    "IfTrueFlagCountGreaterThanOrEqual",
    "IfTrueFlagCountLessThanOrEqual",
    "IfEventValueComparison",
    "IfEventValueEqual",
    "IfEventValueNotEqual",
    "IfEventValueGreaterThan",
    "IfEventValueLessThan",
    "IfEventValueGreaterThanOrEqual",
    "IfEventValueLessThanOrEqual",
    "IfEventsComparison",
    "IfCharacterRegionState",
    "IfCharacterInsideRegion",
    "IfCharacterOutsideRegion",
    "IfPlayerInsideRegion",
    "IfPlayerOutsideRegion",
    "IfAllPlayersRegionState",
    "IfAllPlayersInsideRegion",
    "IfAllPlayersOutsideRegion",
    "IfEntityDistanceState",
    "IfEntityWithinDistance",
    "IfEntityBeyondDistance",
    "IfPlayerWithinDistance",
    "IfPlayerBeyondDistance",
    "IfPlayerItemStateNoBox",
    "IfPlayerItemStateBox",
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
    "IfAnyItemDroppedInRegion",
    "IfItemDropped",
    "AwaitObjectDestructionState",
    "AwaitObjectDestroyed",
    "AwaitObjectNotDestroyed",
    "SkipLinesIfObjectDestructionState",
    "SkipLinesIfObjectDestroyed",
    "SkipLinesIfObjectNotDestroyed",
    "TerminateIfObjectDestructionState",
    "EndIfObjectDestroyed",
    "EndIfObjectNotDestroyed",
    "RestartIfObjectDestroyed",
    "RestartIfObjectNotDestroyed",
    "IfObjectDestructionState",
    "IfObjectDestroyed",
    "IfObjectNotDestroyed",
    "IfObjectDamagedBy",
    "IfObjectActivated",
    "IfObjectHealthValueComparison",
    "IfMovingOnCollision",
    "IfRunningOnCollision",
    "IfStandingOnCollision",
    "SkipLinesIfComparison",
    "SkipLinesIfEqual",
    "SkipLinesIfNotEqual",
    "SkipLinesIfGreaterThan",
    "SkipLinesIfLessThan",
    "SkipLinesIfGreaterThanOrEqual",
    "SkipLinesIfLessThanOrEqual",
    "TerminateIfComparison",
    "EndIfEqual",
    "EndIfNotEqual",
    "EndIfGreaterThan",
    "EndIfLessThan",
    "EndIfGreaterThanOrEqual",
    "EndIfLessThanOrEqual",
    "RestartIfEqual",
    "RestartIfNotEqual",
    "RestartIfGreaterThan",
    "RestartIfLessThan",
    "RestartIfGreaterThanOrEqual",
    "RestartIfLessThanOrEqual",
    "IfActionButton",
    "IfWorldTendencyComparison",
    "IfWhiteWorldTendencyComparison",
    "IfBlackWorldTendencyComparison",
    "IfWhiteWorldTendencyGreaterThanOrEqual",
    "IfBlackWorldTendencyGreaterThanOrEqual",
    "IfNewGameCycleComparison",
    "IfNewGameCycleEqual",
    "IfNewGameCycleGreaterThanOrEqual",
    "IfDLCState",
    "IfDLCOwned",
    "IfDLCNotOwned",
    "IfOnlineState",
    "IfOnline",
    "IfOffline",
    "IfCharacterDeathState",
    "IfCharacterDead",
    "IfCharacterAlive",
    "IfAttacked",
    "IfHealthComparison",
    "IfHealthEqual",
    "IfHealthNotEqual",
    "IfHealthGreaterThan",
    "IfHealthLessThan",
    "IfHealthGreaterThanOrEqual",
    "IfHealthLessThanOrEqual",
    "IfCharacterType",
    "IfCharacterHollow",
    "IfCharacterHuman",
    "IfCharacterTargetingState",
    "IfCharacterTargeting",
    "IfCharacterNotTargeting",
    "IfCharacterSpecialEffectState",
    "IfCharacterHasSpecialEffect",
    "IfCharacterDoesNotHaveSpecialEffect",
    "IfCharacterPartHealthComparison",
    "IfCharacterPartHealthLessThanOrEqual",
    "IfCharacterBackreadState",
    "IfCharacterBackreadEnabled",
    "IfCharacterBackreadDisabled",
    "IfTAEEventState",
    "IfHasTAEEvent",
    "IfDoesNotHaveTAEEvent",
    "IfHasAIStatus",
    "IfSkullLanternState",
    "IfSkullLanternActive",
    "IfSkullLanternInactive",
    "IfPlayerClass",
    "IfPlayerCovenant",
    "IfPlayerSoulLevelComparison",
    "IfPlayerSoulLevelGreaterThanOrEqual",
    "IfPlayerSoulLevelLessThanOrEqual",
    "IfHealthValueComparison",
    "IfHealthValueEqual",
    "IfHealthValueNotEqual",
    "IfHealthValueGreaterThan",
    "IfHealthValueLessThan",
    "IfHealthValueGreaterThanOrEqual",
    "IfHealthValueLessThanOrEqual",
    "ArenaRankingRequest1v1",
    "ArenaRankingRequest2v2",
    "ArenaRankingRequestFFA",
    "ArenaExitRequest",
    "ArenaSetNametag1",
    "ArenaSetNametag2",
    "ArenaSetNametag3",
    "ArenaSetNametag4",
    "DisplayArenaDissolutionMessage",
    "ArenaSetNametag5",
    "ArenaSetNametag6",
]


# RUN


def RunEvent(event_id, slot=0, args=(0,), arg_types=None, event_layers=None):
    """Run the given `event_id`, which must be defined in the same script.

    You can omit `arg_types` if all the arguments are unsigned integers (which is usually the case).

    Note that you can also call the name of the event directly and pass in the given arguments normally.

    Note that `event_layers` is supported as an argument here for intellisense purposes, as this is the instruction
    it will most commonly be used with, but it can be used with any instruction. The EVS parser handles this keyword
    argument separately, so it will never actually be passed to an instruction function like this one.
    """
    instruction_info = [2000, 0]  # Mutable list for this instruction only, as it may required modification.
    if arg_types is None:
        # Assume all unsigned integers.
        arg_types = "I" * len(args)
    if len(args) != len(arg_types):
        raise ValueError("Number of event arguments does not match length of argument type string in RunEvent.")
    format_string = "iI" + str(arg_types[0])
    if len(arg_types) > 1:
        format_string += f"|{arg_types[1:]}"
    return to_numeric(instruction_info, slot, event_id, *args, arg_types=format_string, event_layers=event_layers)


# WAITING


def Wait(seconds: float):
    """ Wait for some number of seconds. """
    instruction_info = (1001, 0)
    return to_numeric(instruction_info, seconds)


def WaitFrames(frames: int):
    """ Wait for some number of frames. """
    instruction_info = (1001, 1)
    return to_numeric(instruction_info, frames)


def WaitRandomSeconds(min_seconds: float, max_seconds: float):
    """ Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform. """
    instruction_info = (1001, 2)
    return to_numeric(instruction_info, min_seconds, max_seconds)


def WaitRandomFrames(min_frames: int, max_frames: int):
    """ Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform. """
    instruction_info = (1001, 3)
    return to_numeric(instruction_info, min_frames, max_frames)


def WaitForNetworkApproval(max_seconds: float):
    """ Wait for network to approve event (up to `max_seconds` seconds). """
    instruction_info = (1000, 9)
    return to_numeric(instruction_info, max_seconds)


# CHARACTERS


def SetCharacterState(character: CharacterInt, state: bool):
    instruction_info = (2004, 5)
    return to_numeric(instruction_info, character, state)


def EnableCharacter(character: CharacterInt):
    return SetCharacterState(character, True)


def DisableCharacter(character: CharacterInt):
    return SetCharacterState(character, False)


def SetAIState(character: CharacterInt, state: bool):
    instruction_info = (2004, 1)
    return to_numeric(instruction_info, character, state)


def EnableAI(character: CharacterInt):
    return SetAIState(character, True)


def DisableAI(character: CharacterInt):
    return SetAIState(character, False)


def SetTeamType(character: CharacterInt, new_team: Union[TeamType, int]):
    instruction_info = (2004, 2)
    return to_numeric(instruction_info, character, new_team)


def Kill(character: CharacterInt, award_souls: bool = False):
    """ Technically a kill 'request.' """
    instruction_info = (2004, 4)
    return to_numeric(instruction_info, character, award_souls)


def EzstateAIRequest(character: CharacterInt, command_id, slot):
    """ Slot number ranges from 0 to 3. """
    instruction_info = (2004, 6)
    return to_numeric(instruction_info, character, command_id, slot)


# AddSpecialEffect function has different arguments in different games and is therefore not shared.


def CancelSpecialEffect(character: CharacterInt, special_effect_id):
    """ 'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). """
    instruction_info = (2004, 21)
    return to_numeric(instruction_info, character, special_effect_id)


def ResetStandbyAnimationSettings(character: CharacterInt):
    """ Equivalent to calling `SetStandbyAnimationSettings` with no arguments, but clearer semantically. """
    return SetStandbyAnimationSettings(character)


def SetStandbyAnimationSettings(
    character: CharacterInt,
    standby_animation=-1,
    damage_animation=-1,
    cancel_animation=-1,
    death_animation=-1,
    standby_exit_animation=-1,
):
    """ Sets entity's default standby animations. -1 is default for each category. """
    instruction_info = (2004, 9, [0, -1, -1, -1, -1, -1, -1])
    return to_numeric(
        instruction_info,
        character,
        standby_animation,
        damage_animation,
        cancel_animation,
        death_animation,
        standby_exit_animation,
    )


def SetGravityState(character: CharacterInt, state: bool):
    """ Simply determines if the character loses height as it moves around. They will still gain height by running up
    slopes. """
    instruction_info = (2004, 10)
    return to_numeric(instruction_info, character, state)


def EnableGravity(character: CharacterInt):
    return SetGravityState(character, True)


def DisableGravity(character: CharacterInt):
    return SetGravityState(character, False)


def SetCharacterEventTarget(character: CharacterInt, region: RegionInt):
    """ Likely refers to patrolling behavior. """
    instruction_info = (2004, 11)
    return to_numeric(instruction_info, character, region)


def SetImmortalityState(character: CharacterInt, state: bool):
    """ Character will take damage, but not die (i.e. cannot go below 1 HP). """
    instruction_info = (2004, 12)
    return to_numeric(instruction_info, character, state)


def EnableImmortality(character: CharacterInt):
    return SetImmortalityState(character, True)


def DisableImmortality(character: CharacterInt):
    return SetImmortalityState(character, False)


def SetNest(character: CharacterInt, region: RegionInt):
    """ Home point for entity AI. """
    instruction_info = (2004, 13)
    return to_numeric(instruction_info, character, region)


# RotateToFaceEntity has different arguments in different games, and is therefore not shared.


def SetInvincibilityState(character: CharacterInt, state):
    """ Character cannot take damage or die. """
    instruction_info = (2004, 15)
    return to_numeric(instruction_info, character, state)


def EnableInvincibility(character: CharacterInt):
    """ Character HP cannot be changed (positively or negatively) by anything. """
    return SetInvincibilityState(character, True)


def DisableInvincibility(character: CharacterInt):
    return SetInvincibilityState(character, False)


def ClearTargetList(character: CharacterInt):
    """ Clear list of targets from character AI. """
    instruction_info = (2004, 16)
    return to_numeric(instruction_info, character)


def AICommand(character: CharacterInt, command_id, slot):
    """ These instructions can be accessed in AI Lua scripts. """
    instruction_info = (2004, 17)
    return to_numeric(instruction_info, character, command_id, slot)


def SetEventPoint(character: CharacterInt, region: RegionInt, reaction_range):
    """ Not sure what the usage of this is, but it is likely used to change patrol behavior. """
    instruction_info = (2004, 18)
    return to_numeric(instruction_info, character, region, reaction_range)


def SetAIParamID(character: CharacterInt, ai_param_id):
    """ Change character's AI parameter index. """
    instruction_info = (2004, 19)
    return to_numeric(instruction_info, character, ai_param_id)


def ReplanAI(character: CharacterInt):
    """ Clear current AI goal list and force character to replan it. """
    instruction_info = (2004, 20)
    return to_numeric(instruction_info, character)


def CreateNPCPart(
    character: CharacterInt,
    npc_part_id: int,
    part_index: Union[NPCPartType, int],
    part_health: int,
    damage_correction,
    body_damage_correction,
    is_invincible: bool,
    start_in_stop_state: bool,
):
    """ Complex. Sets specific damage parameters for part of an NPC model. Further changes to the specific part can be
    made using the events below. The part is specified using the NPCPartType slot. Look at usage in tail cut events to
    understand these more. """
    instruction_info = (2004, 22, [0, 0, 0, 0, 1.0, 1.0, 0, 0])
    return to_numeric(
        instruction_info,
        character,
        npc_part_id,
        part_index,
        part_health,
        damage_correction,
        body_damage_correction,
        is_invincible,
        start_in_stop_state,
    )


def SetNPCPartHealth(character: CharacterInt, npc_part_id: int, desired_hp: int, overwrite_max: bool):
    """ You must create the part first. """
    instruction_info = (2004, 23)
    return to_numeric(instruction_info, character, npc_part_id, desired_hp, overwrite_max)


def SetNPCPartEffects(character: CharacterInt, npc_part_id: int, material_special_effect_id: int, material_fx_id: int):
    """ Attach material effects to an NPC part. """
    instruction_info = (2004, 24)
    return to_numeric(instruction_info, character, npc_part_id, material_special_effect_id, material_fx_id)


def SetNPCPartBulletDamageScaling(character: CharacterInt, npc_part_id: int, desired_scaling):
    """ Scale the damage dealt to the part. Usually used to set damage to zero, e.g. Smough's hammer. """
    instruction_info = (2004, 25)
    return to_numeric(instruction_info, character, npc_part_id, desired_scaling)


def SetDisplayMask(character: CharacterInt, bit_index, switch_type):
    """ Different bits correspond to different parts of the character model. You can see the initial values for these
    in the NPC params. This is generally used to disable tails when they are cut off.

    'switch_type' can be 0 (off), 1 (on), or 2 (change). """
    instruction_info = (2004, 26)
    return to_numeric(instruction_info, character, bit_index, switch_type)


def SetCollisionMask(character: CharacterInt, bit_index, switch_type):
    """ See above. This affects the NPC's Collision, not appearance. """
    instruction_info = (2004, 27)
    return to_numeric(instruction_info, character, bit_index, switch_type)


def SetNetworkUpdateAuthority(character: CharacterInt, authority_level: UpdateAuthority):
    """ Complex; look at existing usage. Authority level must be 'Normal' or 'Forced'. """
    instruction_info = (2004, 28)
    return to_numeric(instruction_info, character, authority_level)


def SetBackreadState(character: CharacterInt, remove: bool):
    """ I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread' of
    a character has a larger effect on game resources. It is used, for example, to disable the Fair Lady and Eingyi
    during the Stray Demon boss fight.

    Also note reversed bool.
    """
    instruction_info = (2004, 29)
    return to_numeric(instruction_info, character, remove)


def EnableBackread(character: CharacterInt):
    return SetBackreadState(character, False)


def DisableBackread(character: CharacterInt):
    return SetBackreadState(character, True)


def SetHealthBarState(character: CharacterInt, state):
    """ Normal health bar that appears above character. """
    instruction_info = (2004, 30)
    return to_numeric(instruction_info, character, state)


def EnableHealthBar(character: CharacterInt):
    """ Not sure what effect this has on the boss health bar. """
    return SetHealthBarState(character, True)


def DisableHealthBar(character: CharacterInt):
    """ Note that the normal health bar is disabled automatically if you give them a boss health bar. """
    return SetHealthBarState(character, False)


# SetBossHealthBar takes different byte formats in different games.


def SetCharacterCollisionState(character: CharacterInt, is_disabled: bool):
    """ Note that the bool is inverted from what you might expect. """
    instruction_info = (2004, 31)
    return to_numeric(instruction_info, character, is_disabled)


def EnableCharacterCollision(character: CharacterInt):
    return SetCharacterCollisionState(character, False)


def DisableCharacterCollision(character: CharacterInt):
    return SetCharacterCollisionState(character, True)


def AIEvent(character: CharacterInt, command_id, slot, first_event_flag, last_event_flag):
    """ I have no idea what this does. """
    instruction_info = (2004, 32)
    return to_numeric(instruction_info, character, command_id, slot, first_event_flag, last_event_flag)


def ReferDamageToEntity(character: CharacterInt, target_entity):
    """ All damage dealt to the first character will *also* (not *only*) be dealt to the target entity. I'm not 100%
    sure if the target entity can be an Object.

    Only used by the Four Kings in the vanilla game. """
    instruction_info = (2004, 33)
    return to_numeric(instruction_info, character, target_entity)


def SetNetworkUpdateRate(character: CharacterInt, is_fixed: bool, update_rate: CharacterUpdateRate):
    """ Not sure what 'is_fixed' does. I believe only 'Always' and 'Never' are used in the vanilla game. """
    instruction_info = (2004, 34)
    return to_numeric(instruction_info, character, is_fixed, update_rate)


def SetBackreadStateAlternate(character: CharacterInt, state):
    """ I have no idea how this differs from the standard backread function above. """
    # TODO: Check and compare usage. If it's even used.
    instruction_info = (2004, 35)
    return to_numeric(instruction_info, character, state)


def DropMandatoryTreasure(character: CharacterInt):
    """ This will disable the character and spawn any treasure they would drop. It's possible that it only spawns
    treasure that has a 100% drop rate, hence the name, but I haven't confirmed this. """
    # TODO: Confirm it actually disables the character.
    instruction_info = (2004, 37)
    return to_numeric(instruction_info, character)


def SetTeamTypeAndExitStandbyAnimation(character: CharacterInt, team_type: TeamType):
    """ Two for the price of one. Often used when NPCs with resting animations become hostile. """
    instruction_info = (2004, 44)
    return to_numeric(instruction_info, character, team_type)


def HumanityRegistration(character: CharacterInt, event_flag: FlagInt):
    """ I believe this designates the first event flag in a range of eight, which tracks how much humanity an NPC has
    for draining with Dark Hand. These flags are all in the 8000 range, and tightly packed, so you'll need to find your
    own range if you want to replicate this.

    I can confirm that NOT doing this for a new NPC means you can't drain any humanity from them, rather than being able
    to drain unlimited humanity.
    """
    instruction_info = (2004, 45)
    return to_numeric(instruction_info, character, event_flag)


def ResetAnimation(character, disable_interpolation: bool = False):
    """ Cancels an animation. Note the inverted bool for controlling interpolation. """
    # 0 = interpolated, 1 = not interpolated
    instruction_info = (2004, 43)
    return to_numeric(instruction_info, character, disable_interpolation)


def ActivateMultiplayerBuffs(character: CharacterInt):
    """ Used to strengthen bosses based on the number of summons you have. Not sure if it works for every NPC. It
    could also be tied to certain special effects; haven't checked that yet. """
    instruction_info = (2009, 4)
    return to_numeric(instruction_info, character)


# OBJECTS


def SetObjectState(obj: ObjectInt, state: bool):
    instruction_info = (2005, 3)
    return to_numeric(instruction_info, obj, state)


def EnableObject(obj: ObjectInt):
    return SetObjectState(obj, True)


def DisableObject(obj: ObjectInt):
    return SetObjectState(obj, False)


def DestroyObject(obj: ObjectInt, slot: int = 0):
    """ Technically 'requests' the object's destruction. No idea what the slot number does. """
    instruction_info = (2005, 1)
    return to_numeric(instruction_info, obj, slot)


def RestoreObject(obj: ObjectInt):
    """ The opposite of destruction. Restores it to its original MSB coordinates. """
    instruction_info = (2005, 2)
    return to_numeric(instruction_info, obj)


def SetTreasureState(obj: ObjectInt, state: bool):
    instruction_info = (2005, 4)
    return to_numeric(instruction_info, obj, state)


def EnableTreasure(obj: ObjectInt):
    """ Enables any treasure attached to this object by MSB events. """
    return SetTreasureState(obj, True)


def DisableTreasure(obj: ObjectInt):
    """ Disables any treasure attached to this object by MSB events.

    If you want to disable treasure by default, you can do it in the MSB by changing a certain event value to 255.
    """
    return SetTreasureState(obj, False)


def ActivateObject(obj: ObjectInt, obj_act_id: int, relative_index: int):
    """ Manually call a specific ObjAct event attached to this object. I believe 'relative_index' refers to the points
    on the object at which it can be activated (e.g. which side of a gate you are on).

    Note that this will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how the
    game gets Patches to pull the lever in the Catacombs.
    """
    instruction_info = (2005, 5)
    return to_numeric(instruction_info, obj, obj_act_id, relative_index)


def SetObjectActivation(obj: ObjectInt, obj_act_id: int, state: bool):
    """ Sets whether the object can be activated (1) or not activated (0). """
    instruction_info = (2005, 6, [0, -1, 0])
    return to_numeric(instruction_info, obj, obj_act_id, state)


def SetObjectActivationWithIdx(obj: ObjectInt, obj_act_id: int, relative_index: int, state: bool):
    """ Similar to above, but you can provide the relative index to disable (e.g. one side of a door). """
    instruction_info = (2005, 14, [0, -1, 0, 0])
    return to_numeric(instruction_info, obj, obj_act_id, relative_index, state)


def EnableObjectActivation(obj: ObjectInt, obj_act_id, relative_index=None):
    """ Allows the given ObjAct to be performed with the object, optionally only at the given relative_index. I've
    combined two instructions into one here, as they're very similar. """
    if relative_index is None:
        return SetObjectActivation(obj, obj_act_id, True)
    return SetObjectActivationWithIdx(obj, obj_act_id, relative_index, True)


def DisableObjectActivation(obj: ObjectInt, obj_act_id, relative_index=None):
    """ Prevents the given ObjAct from being performed with the object. Used for doors that you can only open once,
    for example. Again, I've combined the relative index version here. """
    if relative_index is None:
        return SetObjectActivation(obj, obj_act_id, False)
    return SetObjectActivationWithIdx(obj, obj_act_id, relative_index, False)


def PostDestruction(obj: ObjectInt, slot: int):
    """ Sets the object to whatever appearance it would have after being destroyed. Again, not sure what 'slot'
    does. """
    instruction_info = (2005, 8)
    return to_numeric(instruction_info, obj, slot)


def CreateHazard(
    obj_flag: FlagInt,
    obj: ObjectInt,
    model_point: int,
    behavior_param_id: int,
    target_type: DamageTargetType,
    radius: float,
    life: float,
    repetition_time: float,
):
    """ Turn an object into an environmental hazard. It deals damage when touched according to the NPC Behavior params
    you give it. The model_point determines which part of the object is hazardous (with the given radius and life,
    relative to the time this instruction occurs).

    An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.

    'target_type' determines what the hazard can damage (Character and/or Map).
    """
    instruction_info = (2005, 9)
    return to_numeric(
        instruction_info, obj_flag, obj, model_point, behavior_param_id, target_type, radius, life, repetition_time
    )


def RegisterStatue(obj: ObjectInt, game_map: MapOrSequence, statue_type: StatueType):
    """ Creates a petrified or crystallized statue. I believe this is so it can be seen by other players online. """
    instruction_info = (2005, 10)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, obj, area_id, block_id, statue_type)


def RemoveObjectFlag(obj_flag: FlagInt):
    """ No idea what this does. I believe it might undo the CreateHazard instruction, at least. """
    instruction_info = (2005, 12)
    return to_numeric(instruction_info, obj_flag)


def SetObjectInvulnerability(obj: ObjectInt, state: bool):
    """ 1 = invulnerable. """
    instruction_info = (2005, 13)
    return to_numeric(instruction_info, obj, state)


def EnableObjectInvulnerability(obj: ObjectInt):
    return SetObjectInvulnerability(obj, True)


def DisableObjectInvulnerability(obj: ObjectInt):
    return SetObjectInvulnerability(obj, False)


def EnableTreasureCollection(obj: ObjectInt):
    """ Forces an object to spawn its treasure, even if the treasure's ItemLot flag is already enabled. Useful if
    you want some treasure to reappear (after, say, taking it from the player and disabling the ItemLot flag) without
    the player needing to reload the map. """
    instruction_info = (2005, 15)
    return to_numeric(instruction_info, obj)


# FLAGS


def SetFlagState(flag: FlagInt, state: FlagState):
    """ Enable, disable, or toggle (change) a binary flag. """
    instruction_info = (2003, 2)
    return to_numeric(instruction_info, flag, state)


def EnableFlag(flag: FlagInt):
    return SetFlagState(flag, FlagState.On)


def DisableFlag(flag: FlagInt):
    return SetFlagState(flag, FlagState.Off)


def ToggleFlag(flag: FlagInt):
    return SetFlagState(flag, FlagState.Change)


def SetRandomFlagInRange(flag_range: FlagRangeOrSequence, state: FlagState):
    """ Set the state of a random flag from a given range (inclusive). """
    instruction_info = (2003, 17)
    first_flag, last_flag = tuple(flag_range)
    return to_numeric(instruction_info, first_flag, last_flag, state)


def EnableRandomFlagInRange(flag_range: FlagRangeOrSequence):
    return SetRandomFlagInRange(flag_range, FlagState.On)


def DisableRandomFlagInRange(flag_range: FlagRangeOrSequence):
    return SetRandomFlagInRange(flag_range, FlagState.Off)


def ToggleRandomFlagInRange(flag_range: FlagRangeOrSequence):
    return SetRandomFlagInRange(flag_range, FlagState.Change)


def SetFlagRangeState(flag_range: FlagRangeOrSequence, state: FlagState):
    """ Set the state of an entire flag range (inclusive). """
    instruction_info = (2003, 22)
    first_flag, last_flag = tuple(flag_range)
    return to_numeric(instruction_info, first_flag, last_flag, state)


def EnableFlagRange(flag_range: FlagRangeOrSequence):
    return SetFlagRangeState(flag_range, FlagState.On)


def DisableFlagRange(flag_range: FlagRangeOrSequence):
    return SetFlagRangeState(flag_range, FlagState.Off)


def ChangeFlagRange(flag_range: FlagRangeOrSequence):
    return SetFlagRangeState(flag_range, FlagState.Change)


def IncrementEventValue(flag: FlagInt, bit_count: int, max_value: int):
    """ You can use a contiguous array of flags as a single value. Use this to increment that value. The array begins
    at 'flag' and extends for 'bit_count'. (For example, a 'bit_count' of 4 gives you a theoretical maximum of 256. You
    can set a 'max_value' less than that to limit the value. (I'm not sure if it ticks over back to zero if max_value is
    greater than the possible value given the bit count.)

    This is used for counters in the vanilla game, such as the number of bosses killed while Rhea is at Undead Parish.
    """
    instruction_info = (2003, 31, [0, 1, 0])
    return to_numeric(instruction_info, flag, bit_count, max_value)


def ClearEventValue(flag: FlagInt, bit_count: int):
    """ Clears the given multi-flag. This is basically like disabling 'bit_count' flags in a row, starting at
    'flag'. """
    instruction_info = (2003, 32)
    return to_numeric(instruction_info, flag, bit_count)


def EnableThisFlag():
    """ Handled directly by the compiler, which calls EnableFlag() with the current event ID as its argument. """
    pass


def DisableThisFlag():
    """ Handled directly by the compiler, which calls DisableFlag() with the current event ID as its argument. """
    pass


# EVENTS


def SetEventState(event_id, slot=0, end_type: EventEndType = None):
    """ Stop or restart a particular slot (default of 0) of the given event ID. Note that you cannot restart events that
    have already ended. """
    if end_type is None:
        raise ValueError("End type must be EventEndType.End (0) or EventEndType.Restart (1).")
    instruction_info = (2003, 8)
    return to_numeric(instruction_info, event_id, slot, end_type)


def StopEvent(event_id, slot=0):
    """ Force a running event to stop. """
    return SetEventState(event_id, slot, EventEndType.End)


def RestartEvent(event_id, slot=0):
    """ Force a running event to restart. Note that the event must be active (i.e. not finished) for this to work. If
    you plan to have an event restarted, make sure it doesn't terminate until you no longer need it. """
    return SetEventState(event_id, slot, EventEndType.Restart)


# Collisions


def SetCollisionState(collision: CollisionInt, state: bool):
    instruction_info = (2011, 1)
    return to_numeric(instruction_info, collision, state)


def EnableCollision(collision: CollisionInt):
    """Enable a collision (i.e. hitbox). The ID is specified in the MSB. Note that a Collision doesn't have to be solid
    ground, but could be anything triggered by collision, such as a kill plane (which this is often used to disable).
    """
    return SetCollisionState(collision, True)


def DisableCollision(collision: CollisionInt):
    """Disable a collision (i.e. hitbox). The ID is specified in the MSB. Note that a Collision doesn't have to be solid
    ground, but could be anything triggered by collision, such as a kill plane (which this is often used to disable).
    """
    return SetCollisionState(collision, False)


def SetCollisionBackreadMaskState(collision: CollisionInt, state: bool):
    """ Unused. """
    instruction_info = (2011, 2)
    return to_numeric(instruction_info, collision, state)


def EnableCollisionBackreadMask(collision: CollisionInt):
    return SetCollisionBackreadMaskState(collision, True)


def DisableCollisionBackreadMask(collision: CollisionInt):
    return SetCollisionBackreadMaskState(collision, False)


# ITEMS


def AwardItemLot(item_lot_param_id, host_only: bool = True):
    """ Directly award an item lot to the player. By default, only the host receives the item. """
    instruction_info = (2003, 4)
    if host_only:
        return AwardItemLotToHostOnly(item_lot_param_id)
    return to_numeric(instruction_info, item_lot_param_id)


def AwardItemLotToHostOnly(item_lot_param_id):
    """ You can simply call AwardItemLot() with the same argument, which will redirect here, as you'll almost never
    *not* want to award an item lot to the host only. """
    instruction_info = (2003, 36)
    return to_numeric(instruction_info, item_lot_param_id)


def RemoveItemFromPlayer(item: ItemInt, item_type=None, quantity=0):
    """ Item type is automatically detected. This instruction has a 'quantity' argument, but it seems broken, so you
    always have to remove *all* instances of the item. (Strangely, the similar command used in EzState doesn't seem to
    have this bug.)

    WARNING: don't confuse 'Item' with the specific item type 'Good'.
    """
    instruction_info = (2003, 24)
    if item_type is None:
        item_type = item.item_type
    return to_numeric(instruction_info, item_type, item, quantity)


def RemoveWeaponFromPlayer(weapon: WeaponInt, quantity=0):
    """ Weapons only. """
    return RemoveItemFromPlayer(weapon, ItemType.Weapon, quantity)


def RemoveArmorFromPlayer(armor: ArmorInt, quantity=0):
    """ Armor only. """
    return RemoveItemFromPlayer(armor, ItemType.Armor, quantity)


def RemoveRingFromPlayer(ring: RingInt, quantity=0):
    """ Rings only. """
    return RemoveItemFromPlayer(ring, ItemType.Ring, quantity)


def RemoveGoodFromPlayer(good: GoodInt, quantity=0):
    """ Goods only. """
    return RemoveItemFromPlayer(good, ItemType.Good, quantity)


def SnugglyItemDrop(item_lot: ItemLotInt, region: RegionInt, flag: FlagInt, collision: CollisionInt):
    """ Makes Snuggly drop an item. There are complex limitations to this in the engine, so be careful. (The list of
    available Snuggly flags is a hard-coded limit, for example.) """
    instruction_info = (2003, 34)
    return to_numeric(instruction_info, item_lot, region, flag, collision)


def SetNextSnugglyTrade(flag: FlagInt):
    """ Sets the flag for the next drop based on the item you deposit into the nest. """
    instruction_info = (2003, 33)
    return to_numeric(instruction_info, flag)


# ANIMATIONS


def RequestAnimation(entity: AnimatedInt, animation_id: int, loop: bool = False, wait_for_completion: bool = False):
    """ Not used very often, in favor of ForceAnimation below. """
    instruction_info = (2003, 1)
    return to_numeric(instruction_info, entity, animation_id, loop, wait_for_completion)


def ForceAnimation(
    entity: AnimatedInt,
    animation_id: int,
    loop: bool = False,
    wait_for_completion: bool = False,
    skip_transition: bool = False,
):
    """ Used a lot. Standard way to make a Character or Object perform an animation. """
    instruction_info = (2003, 18, [0, -1, 0, 0, 0])
    return to_numeric(instruction_info, entity, animation_id, loop, wait_for_completion, skip_transition)


def SetAnimationsState(entity: AnimatedInt, state: bool):
    instruction_info = (2004, 39)
    return to_numeric(instruction_info, entity, state)


def EnableAnimations(entity: AnimatedInt):
    return SetAnimationsState(entity, True)


def DisableAnimations(entity: AnimatedInt):
    return SetAnimationsState(entity, False)


def EndOfAnimation(obj: AnimatedInt, animation_id):
    """ Sets entity to whatever state it would have after the given animation. Used often to open doors that have
    already been opened when you reload the map, etc. I doubt it can be used with characters, but haven't confirmed. """
    instruction_info = (2005, 7)
    return to_numeric(instruction_info, obj, animation_id)


# FX


def CreateFX(fx_id: int):
    """ Create visual FX. The ID is given in the MSB (e.g. fog effect for boss gates and checkpoints) """
    instruction_info = (2006, 2)
    return to_numeric(instruction_info, fx_id)


def DeleteFX(fx_id: int, erase_root_only: bool = True):
    """ Delete visual FX. If 'erase_root_only' is True (default), effect particles already emitted will live out the
    rest of their lifetimes (e.g. making a fog gate disappear organically). The ID is given in the MSB. """
    instruction_info = (2006, 1)
    return to_numeric(instruction_info, fx_id, erase_root_only)


def CreateTemporaryFX(fx_id: int, anchor_entity: CoordEntityInt, model_point: int, anchor_type=None):
    """ Create one-off visual FX attached to the given 'anchor_entity'. The FX type argument is determined from the
    Entity category. The FX, of course, must be current loaded (or in common effects). """
    instruction_info = (2006, 3, [0, 0, -1, 0])
    if anchor_type is None:
        try:
            anchor_type = anchor_entity.coord_entity_type
        except AttributeError:
            raise AttributeError("anchor_type not detected. Use the keyword 'anchor_type' or a typed anchor_entity.")
    return to_numeric(instruction_info, anchor_type, anchor_entity, model_point, fx_id)


def CreateObjectFX(fx_id: int, obj: ObjectInt, model_point: int):
    instruction_info = (2006, 4)
    return to_numeric(instruction_info, obj, model_point, fx_id)


def DeleteObjectFX(obj: ObjectInt, erase_root: bool = True):
    """ Note `erase_root` vs. `erase_root_only` for map SFX. """
    instruction_info = (2006, 5)
    return to_numeric(instruction_info, obj, erase_root)


# AUDIO


def SetBackgroundMusic(state: bool, slot: int, entity: CoordEntityInt, sound_type: SoundType, sound_id: int):
    instruction_info = (2010, 1)
    return to_numeric(instruction_info, state, slot, entity, sound_type, sound_id)


def PlaySoundEffect(
    anchor_entity: CoordEntityInt, sound_type: Union[None, SoundType, int] = None, sound_id: Union[Sound, int] = -1
):
    """ Anchor entity determines the localization of the sound, and the sound type is used to look up the source. """
    instruction_info = (2010, 2)
    if sound_id == -1:
        # For legacy reasons, the keyword argument order here isn't optimal.
        raise ValueError("A non-negative sound_id must be given.")
    if sound_type is None:
        try:
            sound_type = sound_id.sound_type
        except AttributeError:
            raise ValueError(f"Cannot detect sound type from sound ID. Use `sound_type` or pass a `Sound` instance.")
    return to_numeric(instruction_info, anchor_entity, sound_type, sound_id)


def SetSoundEventState(sound_id: int, state: bool):
    """ The sound ID is in the MSB. Includes boss music, which is obviously the most common use, and ambiance. """
    instruction_info = (2010, 3)
    return to_numeric(instruction_info, sound_id, state)


def EnableSoundEvent(sound_id: int):
    """ The sound ID is in the MSB. Used for boss music and ambiance. """
    return SetSoundEventState(sound_id, True)


def DisableSoundEvent(sound_id: int):
    """ The sound ID is in the MSB. Used for boss music and ambiance. """
    return SetSoundEventState(sound_id, False)


# MAP


def RegisterLadder(start_climbing_flag: FlagInt, stop_climbing_flag: FlagInt, obj: ObjectInt):
    """ Don't mess with these flags, generally; you can just delay when this is called after map load to disable
    certain ladders (which is kind of weird anyway). """
    instruction_info = (2009, 0)
    return to_numeric(instruction_info, start_climbing_flag, stop_climbing_flag, obj)


def RegisterBonfire(
    bonfire_flag: FlagInt, obj: ObjectInt, reaction_distance=2.0, reaction_angle=180.0, initial_kindle_level=0
):
    """ Register a bonfire, which creates the flame FX and allows you to interact with it (via the MSB entity with ID
    (obj + 1000).

    I believe the bonfire flag tells the game where to keep track of its kindle level, or something like that. I
    don't recommend messing around with this much. The reaction distance, angle, and initial kindle level are all set
    to their standard defaults for bonfires.

    Note that, for some reason, kindle level is defined in increments of 10, so the number of Estus Flasks given is
    (initial_kindle_level / 2) + 5.

    There also seems to be an issue with registering a bonfire that has already been registered with a greater initial
    kindle level. Beware of this, if you find that you can't interact with bonfires or get them to even register.
    """
    instruction_info = (2009, 3)
    return to_numeric(instruction_info, bonfire_flag, obj, reaction_distance, reaction_angle, initial_kindle_level)


def SetMapPieceState(map_part_id, state: bool):
    """ Set the visibility of individual map parts (e.g. all the crystals in Seath's tower). """
    instruction_info = (2012, 1)
    return to_numeric(instruction_info, map_part_id, state)


def DisableMapPiece(map_part_id):
    return SetMapPieceState(map_part_id, False)


def EnableMapPiece(map_part_id: MapPieceInt):
    return SetMapPieceState(map_part_id, True)


# MESSAGES


def PlaceSummonSign(
    sign_type, character: CharacterInt, region: RegionInt, summon_flag: FlagInt, dismissal_flag: FlagInt
):
    """ If you set a black summon sign, the specified NPC will try to invade automatically. """
    instruction_info = (2003, 25)
    return to_numeric(instruction_info, sign_type, character, region, summon_flag, dismissal_flag)


def SetDeveloperMessageState(message_id, state: bool):
    """ Enable or disable developer message. """
    instruction_info = (2003, 26)
    return to_numeric(instruction_info, message_id, state)


def EnableSoapstoneMessage(message_id):
    """ Enable a developer message that has been added to the MSB. The text ID is set in the MSB as well. """
    return SetDeveloperMessageState(message_id, True)


def DisableSoapstoneMessage(message_id):
    """ Disable a developer message that has been added to the MSB. The text ID is set in the MSB as well. """
    return SetDeveloperMessageState(message_id, False)


def DisplayDialog(
    text: EventTextInt,
    anchor_entity: CoordEntityInt = -1,
    display_distance=3.0,
    button_type: ButtonType = ButtonType.OK_or_Cancel,
    number_buttons: NumberButtons = NumberButtons.NoButton,
):
    """ Display a dialog box at the bottom of the screen. You can't use this to get player input, but you can display
    short simple messages. It defaults to a box with no buttons (which is still dismissed when you press A).

    The 'display_distance' argument specifies how far you can move away from the 'anchor_entity' before the message
    automatically disappears. If `anchor_entity=-1` (default), some kind of default anchor is used (probably just the
    position where the player was standing). """
    instruction_info = (2007, 1, [0, 0, 0, -1, 0])
    return to_numeric(instruction_info, text, button_type, number_buttons, anchor_entity, display_distance)


def DisplayBanner(banner_type: BannerType):
    """ Display a pre-rendered banner. You'll have to change the textures (in menu_local.tpf) to change them. """
    instruction_info = (2007, 2)
    return to_numeric(instruction_info, banner_type)


def DisplayStatus(text: EventTextInt, pad_enabled: bool = True):
    """ Displays a large message that appears at the top of the screen, such as the message that tells you how to
    remove your curse, or that the golden fog gates block your path. If 'pad_enabled' is False, you can't get rid of
    the message until it times out on its own. """
    instruction_info = (2007, 3)
    return to_numeric(instruction_info, text, pad_enabled)


def DisplayBattlefieldMessage(text: EventTextInt, display_location_index):
    """ Used in the Battle of Stoicism. Probably useless to you. """
    instruction_info = (2007, 4)
    return to_numeric(instruction_info, text, display_location_index)


# CUTSCENE


def PlayCutscene(
    cutscene_id: int,
    skippable: bool = False,
    fade_out: bool = False,
    player_id: Optional[int] = None,
    move_to_map: Optional[MapOrSequence] = None,
    move_to_region: Optional[RegionInt] = None,
    rotation: int = 0,
    relative_rotation_axis_x: float = 0.0,
    relative_rotation_axis_z: float = 0.0,
    vertical_translation: float = 0.0,
):
    """ Unified instruction for playing cutscenes. You can specify a player (defaults to local player, 10000), control
    whether the cutscene is skippable (False by default) or fades out (False by default), and add extra move arguments
    or rotation arguments. (You can't supply both move and rotation arguments.)

    The move arguments require both a Map and a Region within that map. You can only use this to move to maps that
    have already loaded (i.e. this move does *not* act like bonfire warping and does *not* reload anything).

    The 'relative_rotation_axis_x' and 'relative_rotation_axis_z' arguments let you set where the (vertical) rotation
    axis is, relative to the player's current position.
    """
    if skippable:
        cutscene_type = CutsceneType.SkippableFadeOut if fade_out else CutsceneType.Skippable
    else:
        cutscene_type = CutsceneType.UnskippableFadeOut if fade_out else CutsceneType.Unskippable

    if move_to_map or move_to_region:
        if not (move_to_map and move_to_region):
            raise ValueError("You must set both 'move_to_map' and 'move_to_region' for cutscene moves.")
        if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
            raise ValueError("You cannot use move arguments *and* rotation/translation arguments with cutscenes.")
        if player_id is None:
            return PlayCutsceneAndMovePlayer(cutscene_id, cutscene_type, move_to_region, move_to_map)
        return PlayCutsceneAndMoveSpecificPlayer(cutscene_id, cutscene_type, move_to_region, move_to_map, player_id)

    if player_id is None:
        player_id = 10000

    if rotation or relative_rotation_axis_x or relative_rotation_axis_z or vertical_translation:
        return PlayCutsceneAndRotatePlayer(
            cutscene_id,
            cutscene_type,
            relative_rotation_axis_x,
            relative_rotation_axis_z,
            rotation,
            vertical_translation,
            player_id,
        )

    return PlayCutsceneToPlayer(cutscene_id, cutscene_type, player_id)


def PlayCutsceneAndMovePlayer(
    cutscene_id: int, playback_method: CutsceneType, region: RegionInt, game_map: MapOrSequence
):
    """ I recommend you use the PlayCutscene() wrapper instead of this or the ones below. """
    instruction_info = (2002, 2)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, cutscene_id, playback_method, region, area_id, block_id)


def PlayCutsceneToPlayer(cutscene_id: int, playback_method: CutsceneType, player_id: int):
    instruction_info = (2002, 3)
    return to_numeric(instruction_info, cutscene_id, playback_method, player_id)


def PlayCutsceneAndMoveSpecificPlayer(
    cutscene_id: int, playback_method: CutsceneType, region: RegionInt, game_map: MapOrSequence, player_id: int
):
    instruction_info = (2002, 4)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, cutscene_id, playback_method, region, area_id, block_id, player_id)


def PlayCutsceneAndRotatePlayer(
    cutscene_id: int,
    playback_method: CutsceneType,
    axis_x: float = 0.0,
    axis_z: float = 0.0,
    rotation: float = 0.0,
    vertical_translation: float = 0.0,
    player_id: int = 10000,
):
    instruction_info = (2002, 5)
    return to_numeric(
        instruction_info, cutscene_id, playback_method, axis_x, axis_z, rotation, vertical_translation, player_id
    )


# NAVMESH


def SetNavmeshType(navmesh_id: NavmeshEventInt, navmesh_type: NavmeshType, operation: BitOperation):
    """ Set given navmesh type. """
    instruction_info = (2003, 13)
    return to_numeric(instruction_info, navmesh_id, navmesh_type, operation)


def EnableNavmeshType(navmesh_id: NavmeshEventInt, navmesh_type: NavmeshType):
    """ Mark a given navmesh with the given type, which affects how character AI will interact with it. The navmesh
    ID is set in the MSB. """
    return SetNavmeshType(navmesh_id, navmesh_type, BitOperation.Add)


def DisableNavmeshType(navmesh_id: NavmeshEventInt, navmesh_type: NavmeshType):
    """ Remove the given type from the given navmesh. The navmesh ID is set in the MSB. """
    return SetNavmeshType(navmesh_id, navmesh_type, BitOperation.Delete)


def ToggleNavmeshType(navmesh_id: NavmeshEventInt, navmesh_type: NavmeshType):
    """ Set the given navmesh type to the opposite of whatever it currently is for the given navmesh. """
    return SetNavmeshType(navmesh_id, navmesh_type, BitOperation.Invert)


# NETWORK


def SetNetworkSync(state: bool):
    instruction_info = (2000, 2)
    return to_numeric(instruction_info, state)


def EnableNetworkSync():
    return SetNetworkSync(True)


def DisableNetworkSync():
    return SetNetworkSync(False)


def ClearMainCondition(dummy_arg: int):
    """ Likely clears all conditions currently loaded into the main condition (0). """
    instruction_info = (2000, 3)
    return to_numeric(instruction_info, dummy_arg)


def IssuePrefetchRequest(request_id: int):
    """ No idea what this does. """
    instruction_info = (2000, 4)
    return to_numeric(instruction_info, request_id)


def SaveRequest():
    """ The game saves often, but sometimes you need to save immediately, often after changing a spawn point, for
    example. (Sneaky logic will often save the game before the player realizes what's happened.) """
    instruction_info = (2000, 5)
    return to_numeric(instruction_info, 0)


def TriggerMultiplayerEvent(event_id: int):
    """ Used to make the Bell of Awakening sounds, for example. """
    instruction_info = (2003, 16)
    return to_numeric(instruction_info, event_id)


def SetVagrantSpawning(spawning_disabled: bool):
    """ Note inverted bool. """
    instruction_info = (2003, 30)
    return to_numeric(instruction_info, spawning_disabled)


def EnableVagrantSpawning():
    """ Allows Vagrants to spawn at all. """
    return SetVagrantSpawning(False)


def DisableVagrantSpawning():
    """ Prevents Vagrants from spawning at all. """
    return SetVagrantSpawning(True)


def IncrementPvPSin():
    """ Normally only happens when you kill an NPC. """
    instruction_info = (2004, 46)
    return to_numeric(instruction_info, 0)


def NotifyBossBattleStart():
    """ Sends the message to all summons that the host has challenged the boss. """
    instruction_info = (2009, 6)
    return to_numeric(instruction_info, 0)


# SPAWNER


def SetSpawnerState(entity: CoordEntityInt, state: bool):
    """ e.g. the baby skeletons in Tomb of the Giants. """
    instruction_info = (2003, 3)
    return to_numeric(instruction_info, entity, state)


def EnableSpawner(entity: CoordEntityInt):
    return SetSpawnerState(entity, True)


def DisableSpawner(entity: CoordEntityInt):
    return SetSpawnerState(entity, False)


def ShootProjectile(
    owner_entity: CoordEntityInt,
    projectile_id,
    model_point,
    behavior_id,
    launch_angle_x=0,
    launch_angle_y=0,
    launch_angle_z=0,
):
    """ The owner entity sets the 'team' of the projectile (i.e. who it can hurt). You can use this to
    directly spawn bullets by setting the projectile_id to the owner_entity. Note that the angle arguments
    are all integers. """
    instruction_info = (2003, 5, [0, 0, -1, 0, 0, 0, 0])
    return to_numeric(
        instruction_info,
        owner_entity,
        projectile_id,
        model_point,
        behavior_id,
        launch_angle_x,
        launch_angle_y,
        launch_angle_z,
    )


def CreateProjectileOwner(entity: CoordEntityInt):
    """ A 'bullet owner' that will spawn things according to the Spawner section of the MSB. """
    instruction_info = (2004, 7)
    return to_numeric(instruction_info, entity)


# WARP


def WarpToMap(game_map: MapOrSequence, destination_player_id=-1):
    """ Warp the main player to the given player entity ID, which is in the Players tab of the MSB, in some map. By
    default, this warps to the 'default position' in the map (-1), which is the same point you would spawn at if the
    game lost track of your stable footing (e.g. in 'wrong warp' glitches). """
    instruction_info = (2003, 14, [0, 0, -1])
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, area_id, block_id, destination_player_id)


def MoveRemains(source_region: RegionInt, destination_region: RegionInt):
    """ Move all bloodstains and dropped items from one region to another (I assume). Used to move your
    remains out of Gwyndolin's endless corridor. """
    instruction_info = (2003, 35)
    return to_numeric(instruction_info, source_region, destination_region)


def Move(
    character: CharacterInt,
    destination: CoordEntityInt,
    model_point=-1,
    copy_draw_parent: EntityInt = None,
    set_draw_parent: EntityInt = None,
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
        try:
            destination_type = destination.coord_entity_type
        except AttributeError:
            raise AttributeError(
                "Warp destination has no category. Use 'destination_type' keyword or a " "typed destination."
            )
    if copy_draw_parent is not None and set_draw_parent is not None:
        raise ValueError("You cannot copy and set the draw parent at the same time.")
    if short_move:
        if copy_draw_parent or set_draw_parent:
            raise ValueError("You cannot copy or set the draw parent during a short move.")
        return ShortMove(character, destination, model_point, destination_type)
    if copy_draw_parent is not None:
        return MoveAndCopyDrawParent(character, destination, copy_draw_parent, model_point, destination_type)
    if set_draw_parent is not None:
        return MoveAndSetDrawParent(character, destination, set_draw_parent, model_point, destination_type)
    return MoveToEntity(character, destination, model_point, destination_type)


def MoveToEntity(character: CharacterInt, destination: CoordEntityInt, model_point=-1, destination_type=None):
    """ Basic move. I recommend you use the easier 'Move' wrapper above. """
    if destination_type is None:
        try:
            destination_type = destination.coord_entity_type
        except AttributeError:
            raise AttributeError(
                "Move destination has no category. Use 'destination_type' keyword or a " "typed destination."
            )
    instruction_info = (2004, 3, [0, 0, 0, -1])
    return to_numeric(instruction_info, character, destination_type, destination, model_point)


def MoveAndSetDrawParent(
    character: CharacterInt, destination: CoordEntityInt, draw_parent: EntityInt, model_point=-1, destination_type=None
):
    if destination_type is None:
        try:
            destination_type = destination.coord_entity_type
        except AttributeError:
            raise AttributeError(
                "Move destination has no category. Use 'destination_type' keyword or a " "typed destination."
            )
    instruction_info = (2004, 40, [0, 0, 0, -1, 0])
    return to_numeric(instruction_info, character, destination_type, destination, model_point, draw_parent)


def ShortMove(character: CharacterInt, destination: CoordEntityInt, model_point=-1, destination_type=None):
    if destination_type is None:
        try:
            destination_type = destination.coord_entity_type
        except AttributeError:
            raise AttributeError(
                "Move destination has no category. Use 'destination_type' keyword or a " "typed destination."
            )
    instruction_info = (2004, 41, [0, 0, 0, -1])
    return to_numeric(instruction_info, character, destination_type, destination, model_point)


def MoveAndCopyDrawParent(
    character: CharacterInt,
    destination: CoordEntityInt,
    copy_draw_parent: AnimatedInt,
    model_point=-1,
    destination_type=None,
):
    if destination_type is None:
        try:
            destination_type = destination.coord_entity_type
        except AttributeError:
            raise AttributeError(
                "Move destination has no category. Use 'destination_type' keyword or a " "typed destination."
            )
    instruction_info = (2004, 42, [0, 0, 0, -1, 0])
    return to_numeric(instruction_info, character, destination_type, destination, model_point, copy_draw_parent)


def MoveObjectToCharacter(obj: ObjectInt, character: CharacterInt, model_point: int):
    """ Move an object to a character. """
    instruction_info = (2005, 11, [0, -1, -1])
    return to_numeric(instruction_info, obj, character, model_point)


def SetRespawnPoint(respawn_point: int):
    """ Respawn point is an event set in the MSB. """
    instruction_info = (2003, 23)
    return to_numeric(instruction_info, respawn_point)


# MISCELLANEOUS


def KillBoss(game_area_param_id: int):
    """ The name is slightly misleading, as this doesn't actually kill any entity. Instead, it marks that you have
    cleared an 'area', as defined by the Game Area params, and is always manually called in EMEVD when you kill the boss
    of that area.

    Among other things, this awards your souls for killing the boss (which is why they are delayed and why the game will
    keep trying to give them to you on map load) and prevents you from summoning other players.

    The Game Area params ID is generally identical to the entity ID of the appropriate boss. This is just convention,
    but it's one you should stick to for a sensible setup (and for the name of the instruction to make sense).
    """
    instruction_info = (2003, 12)
    return to_numeric(instruction_info, game_area_param_id)


def IncrementNewGameCycle(dummy_arg: int):
    """ This is manually called at the end of the game. You can call it anytime, but note that there is no way to
    decrement it with events.

    The dummy argument is always 0 or 1; not sure if or how it matters.
    """
    instruction_info = (2003, 21)
    return to_numeric(instruction_info, dummy_arg)


def AwardAchievement(achievement_id: int):
    """ For obvious reasons, I *highly* discourage you from abusing this, except in the interest of maintaining the
    accessibility of existing achievements. This interacts with Steam, which is always dangerous. """
    instruction_info = (2003, 28)
    return to_numeric(instruction_info, achievement_id)


def BetrayCurrentCovenant():
    """ You'll obviously want to make sure you know what covenant the player has when using this. """
    instruction_info = (2004, 38)
    return to_numeric(instruction_info, 0)


def EqualRecovery():
    """ Unknown effect. Only used in Battle of Stoicism, so likely useless to you. """
    instruction_info = (2004, 47)
    return to_numeric(instruction_info)


def ChangeCamera(normal_camera_id: int, locked_camera_id: int):
    instruction_info = (2008, 1, [-1, -1])
    return to_numeric(instruction_info, normal_camera_id, locked_camera_id)


def SetCameraVibration(
    vibration_id: int,
    anchor_entity: CoordEntityInt,
    model_point: int,
    decay_start_distance: float,
    decay_end_distance: float,
    anchor_type: Optional[CoordEntityType] = None,
):
    instruction_info = (2008, 2)
    if anchor_type is None:
        anchor_type = anchor_entity.coord_entity_type
    return to_numeric(
        instruction_info,
        vibration_id,
        anchor_type,
        anchor_entity,
        model_point,
        decay_start_distance,
        decay_end_distance,
    )


def SetLockedCameraSlot(game_map: MapOrSequence, camera_slot: int):
    """ This isn't used very often; standard camera control is done with camera params in the MSB. """
    instruction_info = (2008, 3)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, area_id, block_id, camera_slot)


def HellkiteBreathControl(character: CharacterInt, obj: ObjectInt, animation_id):
    """ I don't recommend you mess with this. It seems to be used to create the fire FX and damaging effect when the
    Hellkite breathes fire on the bridge. It may simply trigger a certain behavior params ID.

    Unclear whether the animation applies to the character or object (which is probably an invisible "burning" plane).
    """
    instruction_info = (2004, 36)
    return to_numeric(instruction_info, character, obj, animation_id)


def SetMapDrawParamSlot(map_area_id: int, slot: int):
    """ Each map block (NOT each map) can have two sets of DrawParams (0 and 1), and this can be used to switch
    between them. Originally only used for Dark Anor Londo. Note that there's some funny business with how this works
    in m15 in Dark Souls Remastered, presumably because the developers didn't want to bother modifying both slots when
    they re-did all the DrawParams. """
    if not isinstance(map_area_id, int):
        raise ValueError(
            "DrawParams can only be set for a whole map *area* (e.g. area 15 for Sen's Fortress and "
            "Anor Londo). I'm making you set the area ID alone so you don't forget this."
        )
    instruction_info = (2003, 19)
    return to_numeric(instruction_info, map_area_id, slot)


# CONTROL FLOW (LOW LEVEL)

# You can use Python 'if/else' blocks, the Await() instruction, and Condition() assignments for high-level event
# control flow, but in the interest of ensuring line-for-line correspondence with the EMEVD instruction table (and to
# allow straightforward 'decompiling'), the low-level control flow instructions are here as well.


# BASIC


def SkipLines(line_count):
    """ Unconditional line skip. """
    instruction_info = (1000, 3)
    return to_numeric(instruction_info, line_count)


def Terminate(event_end_type: EventEndType):
    # Unconditional event end (0) or restart (1).
    instruction_info = (1000, 4)
    return to_numeric(instruction_info, event_end_type)


def End():
    return Terminate(EventEndType.End)


def Restart():
    return Terminate(EventEndType.Restart)


def IfValueComparison(condition: int, comparison_type: ComparisonType, left: int, right: int):
    instruction_info = (0, 1)
    return to_numeric(instruction_info, condition, comparison_type, left, right)


# CONDITIONS


def AwaitConditionState(state: bool, condition: int):
    instruction_info = (1000, 0)
    return to_numeric(instruction_info, state, condition)


def AwaitConditionTrue(condition: int):
    return AwaitConditionState(True, condition)


def AwaitConditionFalse(condition: int):
    return AwaitConditionState(False, condition)


def SkipLinesIfConditionState(line_count, state: bool, condition: int):
    instruction_info = (1000, 1)
    return to_numeric(instruction_info, line_count, state, condition)


def SkipLinesIfConditionTrue(line_count, condition):
    return SkipLinesIfConditionState(line_count, True, condition)


def SkipLinesIfConditionFalse(line_count, condition):
    return SkipLinesIfConditionState(line_count, False, condition)


def SkipLinesIfFinishedConditionState(line_count, state: bool, input_condition: int):
    """ This command is used instead of 1000[01] when conditions are being checked *after* they have already been
    uploaded into the MAIN condition. For example, you might want to continue MAIN if either AND(01) or AND(02) are
    true, but then afterwards, act conditionally on exactly which one of those two registers caused you to
    continue. """
    instruction_info = (1000, 7)
    return to_numeric(instruction_info, line_count, state, input_condition)


def SkipLinesIfFinishedConditionTrue(line_count, condition):
    return SkipLinesIfFinishedConditionState(line_count, True, condition)


def SkipLinesIfFinishedConditionFalse(line_count, condition):
    return SkipLinesIfFinishedConditionState(line_count, False, condition)


def TerminateIfConditionState(event_end_type: EventEndType, state: bool, input_condition: int):
    instruction_info = (1000, 2)
    return to_numeric(instruction_info, event_end_type, state, input_condition)


def EndIfConditionTrue(input_condition: int):
    return TerminateIfConditionState(EventEndType.End, True, input_condition)


def EndIfConditionFalse(input_condition: int):
    return TerminateIfConditionState(EventEndType.End, False, input_condition)


def RestartIfConditionTrue(input_condition: int):
    return TerminateIfConditionState(EventEndType.Restart, True, input_condition)


def RestartIfConditionFalse(input_condition: int):
    return TerminateIfConditionState(EventEndType.Restart, False, input_condition)


def TerminateIfFinishedConditionState(event_end_type: EventEndType, state: bool, input_condition: int):
    instruction_info = (1000, 8)
    return to_numeric(instruction_info, event_end_type, state, input_condition)


def EndIfFinishedConditionTrue(finished_input_condition):
    return TerminateIfFinishedConditionState(EventEndType.End, True, finished_input_condition)


def EndIfFinishedConditionFalse(finished_input_condition):
    return TerminateIfFinishedConditionState(EventEndType.End, False, finished_input_condition)


def RestartIfFinishedConditionTrue(finished_input_condition):
    return TerminateIfFinishedConditionState(EventEndType.Restart, True, finished_input_condition)


def RestartIfFinishedConditionFalse(finished_input_condition):
    return TerminateIfFinishedConditionState(EventEndType.Restart, False, finished_input_condition)


def IfConditionState(output_condition: int, state: bool, input_condition: int):
    instruction_info = (0, 0)
    return to_numeric(instruction_info, output_condition, state, input_condition)


def IfConditionTrue(output_condition, input_condition):
    return IfConditionState(output_condition, True, input_condition)


def IfConditionFalse(output_condition, input_condition):
    return IfConditionState(output_condition, False, input_condition)


# TIME


def IfTimeElapsed(output_condition: int, seconds: float):
    """ Time since event started. """
    instruction_info = (1, 0)
    return to_numeric(instruction_info, output_condition, seconds)


def IfFramesElapsed(output_condition: int, frames: int):
    """ Frames since event started. """
    instruction_info = (1, 1)
    return to_numeric(instruction_info, output_condition, frames)


def IfRandomTimeElapsed(output_condition: int, min_seconds: float, max_seconds: float):
    """ Not used in vanilla DS1. Requires a random amount of time since event began. """
    instruction_info = (1, 2)
    return to_numeric(instruction_info, output_condition, min_seconds, max_seconds)


def IfRandomFramesElapsed(output_condition: int, min_frames: int, max_frames: int):
    """ Not used in vanilla DS1. Requires a random amount of frames since event began. """
    instruction_info = (1, 3)
    return to_numeric(instruction_info, output_condition, min_frames, max_frames)


# MAP


def SkipLinesIfMapPresenceState(line_count, state: bool, game_map: MapOrSequence):
    instruction_info = (1003, 7)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, line_count, state, area_id, block_id)


def SkipLinesIfInsideMap(line_count, game_map: MapOrSequence):
    return SkipLinesIfMapPresenceState(line_count, True, game_map)


def SkipLinesIfOutsideMap(line_count, game_map: MapOrSequence):
    return SkipLinesIfMapPresenceState(line_count, False, game_map)


def TerminateIfMapPresenceState(event_end_type: EventEndType, state: bool, game_map: MapOrSequence):
    instruction_info = (1003, 8)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, event_end_type, state, area_id, block_id)


def EndIfInsideMap(game_map: MapOrSequence):
    return TerminateIfMapPresenceState(EventEndType.End, True, game_map)


def EndIfOutsideMap(game_map: MapOrSequence):
    return TerminateIfMapPresenceState(EventEndType.End, False, game_map)


def RestartIfInsideMap(game_map: MapOrSequence):
    return TerminateIfMapPresenceState(EventEndType.Restart, True, game_map)


def RestartIfOutsideMap(game_map: MapOrSequence):
    return TerminateIfMapPresenceState(EventEndType.Restart, False, game_map)


def IfMapPresenceState(output_condition, state: bool, game_map: MapOrSequence):
    instruction_info = (3, 8, [0, 0, 10, 0])
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, output_condition, state, area_id, block_id)


def IfInsideMap(output_condition, game_map: MapOrSequence):
    return IfMapPresenceState(output_condition, True, game_map)


def IfOutsideMap(output_condition, game_map: MapOrSequence):
    return IfMapPresenceState(output_condition, False, game_map)


# Multiplayer state tests are game-specific.


def IfMultiplayerEvent(condition: int, event_id: int):
    instruction_info = (3, 9)
    return to_numeric(instruction_info, condition, event_id)


# FLAGS


def AwaitFlagState(state: FlagState, flag_type: FlagType, flag: FlagInt):
    instruction_info = (1003, 0)
    return to_numeric(instruction_info, state, flag_type, flag)


def AwaitThisEventOn():
    return AwaitFlagState(FlagState.On, FlagType.RelativeToThisEvent, 0)


def AwaitThisEventOff():
    return AwaitFlagState(FlagState.Off, FlagType.RelativeToThisEvent, 0)


def AwaitThisEventSlotOn():
    return AwaitFlagState(FlagState.On, FlagType.RelativeToThisEventSlot, 0)


def AwaitThisEventSlotOff():
    return AwaitFlagState(FlagState.Off, FlagType.RelativeToThisEventSlot, 0)


def AwaitFlagOn(flag: FlagInt):
    return AwaitFlagState(FlagState.On, FlagType.Absolute, flag)


def AwaitFlagOff(flag: FlagInt):
    return AwaitFlagState(FlagState.Off, FlagType.Absolute, flag)


def AwaitFlagChange(flag: FlagInt):
    return AwaitFlagState(FlagState.Change, FlagType.Absolute, flag)


def SkipLinesIfFlagState(line_count, state: FlagState, flag_type: FlagType, flag: FlagInt):
    """ Skip some number of lines if the specified flag (absolute, event-relative, or slot-relative) has the specified
    state. """
    instruction_info = (1003, 1)
    return to_numeric(instruction_info, line_count, state, flag_type, flag)


def SkipLinesIfThisEventOn(line_count):
    return SkipLinesIfFlagState(line_count, FlagState.On, FlagType.RelativeToThisEvent, 0)


def SkipLinesIfThisEventOff(line_count):
    return SkipLinesIfFlagState(line_count, FlagState.Off, FlagType.RelativeToThisEvent, 0)


def SkipLinesIfThisEventSlotOn(line_count):
    return SkipLinesIfFlagState(line_count, FlagState.On, FlagType.RelativeToThisEventSlot, 0)


def SkipLinesIfThisEventSlotOff(line_count):
    return SkipLinesIfFlagState(line_count, FlagState.Off, FlagType.RelativeToThisEventSlot, 0)


def SkipLinesIfFlagOn(line_count, flag: FlagInt):
    return SkipLinesIfFlagState(line_count, FlagState.On, FlagType.Absolute, flag)


def SkipLinesIfFlagOff(line_count, flag: FlagInt):
    return SkipLinesIfFlagState(line_count, FlagState.Off, FlagType.Absolute, flag)


def TerminateIfFlagState(event_end_type: EventEndType, state: FlagState, flag_type: FlagType, flag: FlagInt):
    instruction_info = (1003, 2)
    return to_numeric(instruction_info, event_end_type, state, flag_type, flag)


def EndIfThisEventOn():
    return TerminateIfFlagState(EventEndType.End, FlagState.On, FlagType.RelativeToThisEvent, 0)


def EndIfThisEventOff():
    return TerminateIfFlagState(EventEndType.End, FlagState.Off, FlagType.RelativeToThisEvent, 0)


def EndIfThisEventSlotOn():
    return TerminateIfFlagState(EventEndType.End, FlagState.On, FlagType.RelativeToThisEventSlot, 0)


def EndIfThisEventSlotOff():
    return TerminateIfFlagState(EventEndType.End, FlagState.Off, FlagType.RelativeToThisEventSlot, 0)


def EndIfFlagOn(flag: FlagInt):
    return TerminateIfFlagState(EventEndType.End, FlagState.On, FlagType.Absolute, flag)


def EndIfFlagOff(flag: FlagInt):
    return TerminateIfFlagState(EventEndType.End, FlagState.Off, FlagType.Absolute, flag)


def RestartIfThisEventOn():
    return TerminateIfFlagState(EventEndType.Restart, FlagState.On, FlagType.RelativeToThisEvent, 0)


def RestartIfThisEventOff():
    return TerminateIfFlagState(EventEndType.Restart, FlagState.Off, FlagType.RelativeToThisEvent, 0)


def RestartIfThisEventSlotOn():
    return TerminateIfFlagState(EventEndType.Restart, FlagState.On, FlagType.RelativeToThisEventSlot, 0)


def RestartIfThisEventSlotOff():
    return TerminateIfFlagState(EventEndType.Restart, FlagState.Off, FlagType.RelativeToThisEventSlot, 0)


def RestartIfFlagOn(flag: FlagInt):
    return TerminateIfFlagState(EventEndType.Restart, FlagState.On, FlagType.Absolute, flag)


def RestartIfFlagOff(flag: FlagInt):
    return TerminateIfFlagState(EventEndType.Restart, FlagState.Off, FlagType.Absolute, flag)


def IfFlagState(condition: int, state: FlagState, flag_type: FlagType, flag: FlagInt):
    instruction_info = (3, 0)
    return to_numeric(instruction_info, condition, state, flag_type, flag)


def IfThisEventOn(condition: int):
    return IfFlagState(condition, FlagState.On, FlagType.RelativeToThisEvent, 0)


def IfThisEventOff(condition: int):
    return IfFlagState(condition, FlagState.Off, FlagType.RelativeToThisEvent, 0)


def IfThisEventSlotOn(condition: int):
    return IfFlagState(condition, FlagState.On, FlagType.RelativeToThisEventSlot, 0)


def IfThisEventSlotOff(condition: int):
    return IfFlagState(condition, FlagState.Off, FlagType.RelativeToThisEventSlot, 0)


def IfFlagOn(condition: int, flag: FlagInt):
    return IfFlagState(condition, FlagState.On, FlagType.Absolute, flag)


def IfFlagOff(condition: int, flag: FlagInt):
    return IfFlagState(condition, FlagState.Off, FlagType.Absolute, flag)


def IfFlagChange(condition: int, flag: FlagInt):
    return IfFlagState(condition, FlagState.Change, FlagType.Absolute, flag)


def SkipLinesIfFlagRangeState(line_count, state: RangeState, flag_type: FlagType, flag_range: FlagRangeOrSequence):
    """ Skip lines (or end/restart, below) if a flag range is all on, all off, any on, or any off. There are also tests
    that allow exact numeric comparisons below. You probably have very little reason to use relative flag values for
    this test, but it is possible. """
    instruction_info = (1003, 3)
    first_flag, last_flag = tuple(flag_range)
    return to_numeric(instruction_info, line_count, state, flag_type, first_flag, last_flag)


def SkipLinesIfFlagRangeAllOn(line_count, flag_range: FlagRangeOrSequence):
    return SkipLinesIfFlagRangeState(line_count, RangeState.AllOn, FlagType.Absolute, flag_range)


def SkipLinesIfFlagRangeAllOff(line_count, flag_range: FlagRangeOrSequence):
    return SkipLinesIfFlagRangeState(line_count, RangeState.AllOff, FlagType.Absolute, flag_range)


def SkipLinesIfFlagRangeAnyOn(line_count, flag_range: FlagRangeOrSequence):
    return SkipLinesIfFlagRangeState(line_count, RangeState.AnyOn, FlagType.Absolute, flag_range)


def SkipLinesIfFlagRangeAnyOff(line_count, flag_range: FlagRangeOrSequence):
    return SkipLinesIfFlagRangeState(line_count, RangeState.AnyOff, FlagType.Absolute, flag_range)


def TerminateIfFlagRangeState(
    event_end_type: EventEndType, state: RangeState, flag_type: FlagType, flag_range: FlagRangeOrSequence
):
    instruction_info = (1003, 4)
    first_flag, last_flag = tuple(flag_range)
    return to_numeric(instruction_info, event_end_type, state, flag_type, first_flag, last_flag)


def EndIfFlagRangeAllOn(flag_range: FlagRangeOrSequence):
    return TerminateIfFlagRangeState(EventEndType.End, RangeState.AllOn, FlagType.Absolute, flag_range)


def EndIfFlagRangeAllOff(flag_range: FlagRangeOrSequence):
    return TerminateIfFlagRangeState(EventEndType.End, RangeState.AllOff, FlagType.Absolute, flag_range)


def EndIfFlagRangeAnyOn(flag_range: FlagRangeOrSequence):
    return TerminateIfFlagRangeState(EventEndType.End, RangeState.AnyOn, FlagType.Absolute, flag_range)


def EndIfFlagRangeAnyOff(flag_range: FlagRangeOrSequence):
    return TerminateIfFlagRangeState(EventEndType.End, RangeState.AnyOff, FlagType.Absolute, flag_range)


def RestartIfFlagRangeAllOn(flag_range: FlagRangeOrSequence):
    return TerminateIfFlagRangeState(EventEndType.Restart, RangeState.AllOn, FlagType.Absolute, flag_range)


def RestartIfFlagRangeAllOff(flag_range: FlagRangeOrSequence):
    return TerminateIfFlagRangeState(EventEndType.Restart, RangeState.AllOff, FlagType.Absolute, flag_range)


def RestartIfFlagRangeAnyOn(flag_range: FlagRangeOrSequence):
    return TerminateIfFlagRangeState(EventEndType.Restart, RangeState.AnyOn, FlagType.Absolute, flag_range)


def RestartIfFlagRangeAnyOff(flag_range: FlagRangeOrSequence):
    return TerminateIfFlagRangeState(EventEndType.Restart, RangeState.AnyOff, FlagType.Absolute, flag_range)


def IfFlagRangeState(condition: int, state: RangeState, flag_type: FlagType, flag_range: FlagRangeOrSequence):
    instruction_info = (3, 1)
    first_flag, last_flag = tuple(flag_range)
    return to_numeric(instruction_info, condition, state, flag_type, first_flag, last_flag)


def IfFlagRangeAllOn(condition: int, flag_range: FlagRangeOrSequence):
    return IfFlagRangeState(condition, RangeState.AllOn, FlagType.Absolute, flag_range)


def IfFlagRangeAllOff(condition: int, flag_range: FlagRangeOrSequence):
    return IfFlagRangeState(condition, RangeState.AllOff, FlagType.Absolute, flag_range)


def IfFlagRangeAnyOn(condition: int, flag_range: FlagRangeOrSequence):
    return IfFlagRangeState(condition, RangeState.AnyOn, FlagType.Absolute, flag_range)


def IfFlagRangeAnyOff(condition: int, flag_range: FlagRangeOrSequence):
    return IfFlagRangeState(condition, RangeState.AnyOff, FlagType.Absolute, flag_range)


def IfTrueFlagCountComparison(
    condition: int,
    value: int,
    flag_type: FlagType.Absolute,
    comparison_type: ComparisonType,
    flag_range: FlagRangeOrSequence,
):
    instruction_info = (3, 10)
    first_flag, last_flag = tuple(flag_range)
    return to_numeric(instruction_info, condition, flag_type, first_flag, last_flag, comparison_type, value)


def IfTrueFlagCountEqual(condition: int, value: int, flag_range):
    return IfTrueFlagCountComparison(condition, value, FlagType.Absolute, ComparisonType.Equal, flag_range)


def IfTrueFlagCountNotEqual(condition: int, value: int, flag_range):
    return IfTrueFlagCountComparison(condition, value, FlagType.Absolute, ComparisonType.NotEqual, flag_range)


def IfTrueFlagCountGreaterThan(condition: int, value: int, flag_range):
    return IfTrueFlagCountComparison(condition, value, FlagType.Absolute, ComparisonType.GreaterThan, flag_range)


def IfTrueFlagCountLessThan(condition: int, value: int, flag_range):
    return IfTrueFlagCountComparison(condition, value, FlagType.Absolute, ComparisonType.LessThan, flag_range)


def IfTrueFlagCountGreaterThanOrEqual(condition: int, value: int, flag_range):
    return IfTrueFlagCountComparison(condition, value, FlagType.Absolute, ComparisonType.GreaterThanOrEqual, flag_range)


def IfTrueFlagCountLessThanOrEqual(condition: int, value: int, flag_range):
    return IfTrueFlagCountComparison(condition, value, FlagType.Absolute, ComparisonType.LessThanOrEqual, flag_range)


def IfEventValueComparison(condition: int, flag: FlagInt, bit_count: int, comparison_type: ComparisonType, value: int):
    instruction_info = (3, 12, [0, 0, 1, 0, 0])
    return to_numeric(instruction_info, condition, flag, bit_count, comparison_type, value)


def IfEventValueEqual(condition: int, flag: FlagInt, bit_count: int, value: int):
    return IfEventValueComparison(condition, flag, bit_count, ComparisonType.Equal, value)


def IfEventValueNotEqual(condition: int, flag: FlagInt, bit_count: int, value: int):
    return IfEventValueComparison(condition, flag, bit_count, ComparisonType.NotEqual, value)


def IfEventValueGreaterThan(condition: int, flag: FlagInt, bit_count: int, value: int):
    return IfEventValueComparison(condition, flag, bit_count, ComparisonType.GreaterThan, value)


def IfEventValueLessThan(condition: int, flag: FlagInt, bit_count: int, value: int):
    return IfEventValueComparison(condition, flag, bit_count, ComparisonType.LessThan, value)


def IfEventValueGreaterThanOrEqual(condition: int, flag: FlagInt, bit_count: int, value: int):
    return IfEventValueComparison(condition, flag, bit_count, ComparisonType.GreaterThanOrEqual, value)


def IfEventValueLessThanOrEqual(condition: int, flag: FlagInt, bit_count: int, value: int):
    return IfEventValueComparison(condition, flag, bit_count, ComparisonType.LessThanOrEqual, value)


def IfEventsComparison(
    condition: int,
    left_flag: FlagInt,
    left_bit_count: int,
    comparison_type: ComparisonType,
    right_flag: FlagInt,
    right_bit_count: int,
):
    """ Check comparison of two event flag values. Haven't bothered adding shortcut functions for this. """
    instruction_info = (3, 20)
    return to_numeric(
        instruction_info, condition, left_flag, left_bit_count, comparison_type, right_flag, right_bit_count
    )


# REGIONS / DISTANCE


def IfCharacterRegionState(condition, entity: AnimatedInt, region: RegionInt, state: bool):
    """ Not sure if this works for objects. """
    instruction_info = (3, 2)
    return to_numeric(instruction_info, condition, state, entity, region)


def IfCharacterInsideRegion(condition: int, entity: AnimatedInt, region: RegionInt):
    return IfCharacterRegionState(condition, entity, region, True)


def IfCharacterOutsideRegion(condition: int, entity: AnimatedInt, region: RegionInt):
    return IfCharacterRegionState(condition, entity, region, False)


def IfPlayerInsideRegion(condition: int, region: RegionInt):
    return IfCharacterRegionState(condition, PLAYER, region, True)


def IfPlayerOutsideRegion(condition: int, region: RegionInt):
    return IfCharacterRegionState(condition, PLAYER, region, False)


def IfAllPlayersRegionState(condition: int, region: RegionInt, state: bool):
    instruction_info = (3, 7)
    return to_numeric(instruction_info, condition, state, region)


def IfAllPlayersInsideRegion(condition: int, region: RegionInt):
    return IfAllPlayersRegionState(condition, region, True)


def IfAllPlayersOutsideRegion(condition: int, region: RegionInt):
    return IfAllPlayersRegionState(condition, region, False)


def IfEntityDistanceState(
    condition: int, entity: CoordEntityInt, other_entity: CoordEntityInt, radius: float, state: bool
):
    instruction_info = (3, 3)
    return to_numeric(instruction_info, condition, state, entity, other_entity, radius)


def IfEntityWithinDistance(condition: int, entity: CoordEntityInt, other_entity: CoordEntityInt, radius: float):
    return IfEntityDistanceState(condition, entity, other_entity, radius, True)


def IfEntityBeyondDistance(condition: int, entity: CoordEntityInt, other_entity: CoordEntityInt, radius: float):
    return IfEntityDistanceState(condition, entity, other_entity, radius, False)


def IfPlayerWithinDistance(condition: int, other_entity: CoordEntityInt, radius: float):
    return IfEntityDistanceState(condition, PLAYER, other_entity, radius, True)


def IfPlayerBeyondDistance(condition: int, other_entity: CoordEntityInt, radius: float):
    return IfEntityDistanceState(condition, PLAYER, other_entity, radius, False)


# ITEMS


def IfPlayerItemStateNoBox(condition: int, item_type: ItemType, item: ItemInt, state: bool):
    instruction_info = (3, 4)
    return to_numeric(instruction_info, condition, item_type, item, state)


def IfPlayerItemStateBox(condition: int, item_type: ItemType, item: ItemInt, state: bool):
    instruction_info = (3, 16)
    return to_numeric(instruction_info, condition, item_type, item, state)


def IfPlayerItemState(
    condition: int, state: bool, item: ItemInt, item_type: Optional[ItemType] = None, including_box: bool = True
):
    """ My wrapper for the two versions that do and do not include the Bottomless Box in the test. """
    if item_type is None:
        try:
            item_type = item.item_type
        except AttributeError:
            raise AttributeError("Item type not detected. Use keyword or typed item.")
    if including_box:
        return IfPlayerItemStateBox(condition, item_type, item, state)
    else:
        return IfPlayerItemStateNoBox(condition, item_type, item, state)


def IfPlayerHasItem(condition: int, item: ItemInt, item_type: Optional[ItemType] = None, including_box: bool = True):
    return IfPlayerItemState(condition, True, item, item_type, including_box)


def IfPlayerHasWeapon(condition: int, weapon: WeaponInt, including_box: bool = True):
    return IfPlayerItemState(condition, True, weapon, ItemType.Weapon, including_box)


def IfPlayerHasArmor(condition: int, armor: ArmorInt, including_box: bool = True):
    return IfPlayerItemState(condition, True, armor, ItemType.Armor, including_box)


def IfPlayerHasRing(condition: int, ring: RingInt, including_box: bool = True):
    return IfPlayerItemState(condition, True, ring, ItemType.Ring, including_box)


def IfPlayerHasGood(condition: int, good: GoodInt, including_box: bool = True):
    return IfPlayerItemState(condition, True, good, ItemType.Good, including_box)


def IfPlayerDoesNotHaveItem(
    condition: int, item: ItemInt, item_type: Optional[ItemType] = None, including_box: bool = True
):
    return IfPlayerItemState(condition, False, item, item_type, including_box)


def IfPlayerDoesNotHaveWeapon(condition: int, weapon: WeaponInt, including_box: bool = True):
    return IfPlayerItemState(condition, False, weapon, ItemType.Weapon, including_box)


def IfPlayerDoesNotHaveArmor(condition: int, armor: ArmorInt, including_box: bool = True):
    return IfPlayerItemState(condition, False, armor, ItemType.Armor, including_box)


def IfPlayerDoesNotHaveRing(condition: int, ring: RingInt, including_box: bool = True):
    return IfPlayerItemState(condition, False, ring, ItemType.Ring, including_box)


def IfPlayerDoesNotHaveGood(condition: int, good: GoodInt, including_box: bool = True):
    return IfPlayerItemState(condition, False, good, ItemType.Good, including_box)


def IfAnyItemDroppedInRegion(condition: int, region: RegionInt):
    """ Check if any item has been dropped in the specified region. Not sensitive to what the item is. """
    instruction_info = (3, 14)
    return to_numeric(instruction_info, condition, region)


def IfItemDropped(condition: int, item: ItemInt, item_type: Union[ItemType, int, None] = None):
    """ Check if a certain item was (just) dropped. Not sensitive to region. """
    instruction_info = (3, 15)
    if item_type is None:
        try:
            item_type = item.item_type
        except AttributeError:
            raise AttributeError("Item type not detected. Use keyword or typed item.")
    return to_numeric(instruction_info, condition, item_type, item)


# OBJECTS


def AwaitObjectDestructionState(state: bool, obj: ObjectInt):
    instruction_info = (1005, 0)
    return to_numeric(instruction_info, state, obj)


def AwaitObjectDestroyed(obj: ObjectInt):
    return AwaitObjectDestructionState(True, obj)


def AwaitObjectNotDestroyed(obj: ObjectInt):
    return AwaitObjectDestructionState(False, obj)


def SkipLinesIfObjectDestructionState(line_count, obj: ObjectInt, state: bool):
    instruction_info = (1005, 1)
    return to_numeric(instruction_info, line_count, state, obj)


def SkipLinesIfObjectDestroyed(line_count, obj: ObjectInt):
    return SkipLinesIfObjectDestructionState(line_count, obj, True)


def SkipLinesIfObjectNotDestroyed(line_count, obj: ObjectInt):
    return SkipLinesIfObjectDestructionState(line_count, obj, False)


def TerminateIfObjectDestructionState(event_end_type: EventEndType, obj: ObjectInt, state: bool):
    instruction_info = (1005, 2)
    return to_numeric(instruction_info, event_end_type, state, obj)


def EndIfObjectDestroyed(obj: ObjectInt):
    return TerminateIfObjectDestructionState(EventEndType.End, obj, True)


def EndIfObjectNotDestroyed(obj: ObjectInt):
    return TerminateIfObjectDestructionState(EventEndType.End, obj, False)


def RestartIfObjectDestroyed(obj: ObjectInt):
    return TerminateIfObjectDestructionState(EventEndType.Restart, obj, True)


def RestartIfObjectNotDestroyed(obj: ObjectInt):
    return TerminateIfObjectDestructionState(EventEndType.Restart, obj, False)


def IfObjectDestructionState(condition: int, obj: ObjectInt, state: bool):
    instruction_info = (5, 0)
    return to_numeric(instruction_info, condition, state, obj)


def IfObjectDestroyed(condition: int, obj: ObjectInt):
    return IfObjectDestructionState(condition, obj, True)


def IfObjectNotDestroyed(condition: int, obj: ObjectInt):
    return IfObjectDestructionState(condition, obj, False)


def IfObjectDamagedBy(condition: int, obj: ObjectInt, attacker: CharacterInt):
    instruction_info = (5, 1)
    return to_numeric(instruction_info, condition, obj, attacker)


def IfObjectActivated(condition: int, obj_act_id: int):
    instruction_info = (5, 2)
    return to_numeric(instruction_info, condition, obj_act_id)


def IfObjectHealthValueComparison(condition: int, obj: ObjectInt, comparison_type: ComparisonType, value: int):
    instruction_info = (5, 3)
    return to_numeric(instruction_info, condition, obj, comparison_type, value)


# Collision


def IfMovingOnCollision(condition: int, collision: CollisionInt):
    instruction_info = (11, 0)
    return to_numeric(instruction_info, condition, collision)


def IfRunningOnCollision(condition: int, collision: CollisionInt):
    instruction_info = (11, 1)
    return to_numeric(instruction_info, condition, collision)


def IfStandingOnCollision(condition: int, collision: CollisionInt):
    instruction_info = (11, 2)
    return to_numeric(instruction_info, condition, collision)


# VALUE COMPARISONS


def SkipLinesIfComparison(line_count, comparison_type: ComparisonType, left: int, right: int):
    instruction_info = (1000, 5, [1, 0, 0, 0])
    return to_numeric(instruction_info, line_count, comparison_type, left, right)


def SkipLinesIfEqual(line_count, left: int, right: int):
    return SkipLinesIfComparison(line_count, ComparisonType.Equal, left, right)


def SkipLinesIfNotEqual(line_count, left: int, right: int):
    return SkipLinesIfComparison(line_count, ComparisonType.NotEqual, left, right)


def SkipLinesIfGreaterThan(line_count, left: int, right: int):
    return SkipLinesIfComparison(line_count, ComparisonType.GreaterThan, left, right)


def SkipLinesIfLessThan(line_count, left: int, right: int):
    return SkipLinesIfComparison(line_count, ComparisonType.LessThan, left, right)


def SkipLinesIfGreaterThanOrEqual(line_count, left: int, right: int):
    return SkipLinesIfComparison(line_count, ComparisonType.GreaterThanOrEqual, left, right)


def SkipLinesIfLessThanOrEqual(line_count, left: int, right: int):
    return SkipLinesIfComparison(line_count, ComparisonType.LessThanOrEqual, left, right)


def TerminateIfComparison(event_end_type: EventEndType, comparison_type: ComparisonType, left: int, right: int):
    instruction_info = (1000, 6)
    return to_numeric(instruction_info, event_end_type, comparison_type, left, right)


def EndIfEqual(left: int, right: int):
    return TerminateIfComparison(EventEndType.End, ComparisonType.Equal, left, right)


def EndIfNotEqual(left: int, right: int):
    return TerminateIfComparison(EventEndType.End, ComparisonType.NotEqual, left, right)


def EndIfGreaterThan(left: int, right: int):
    return TerminateIfComparison(EventEndType.End, ComparisonType.GreaterThan, left, right)


def EndIfLessThan(left: int, right: int):
    return TerminateIfComparison(EventEndType.End, ComparisonType.LessThan, left, right)


def EndIfGreaterThanOrEqual(left: int, right: int):
    return TerminateIfComparison(EventEndType.End, ComparisonType.GreaterThanOrEqual, left, right)


def EndIfLessThanOrEqual(left: int, right: int):
    return TerminateIfComparison(EventEndType.End, ComparisonType.LessThanOrEqual, left, right)


def RestartIfEqual(left: int, right: int):
    return TerminateIfComparison(EventEndType.Restart, ComparisonType.Equal, left, right)


def RestartIfNotEqual(left: int, right: int):
    return TerminateIfComparison(EventEndType.Restart, ComparisonType.NotEqual, left, right)


def RestartIfGreaterThan(left: int, right: int):
    return TerminateIfComparison(EventEndType.Restart, ComparisonType.GreaterThan, left, right)


def RestartIfLessThan(left: int, right: int):
    return TerminateIfComparison(EventEndType.Restart, ComparisonType.LessThan, left, right)


def RestartIfGreaterThanOrEqual(left: int, right: int):
    return TerminateIfComparison(EventEndType.Restart, ComparisonType.GreaterThanOrEqual, left, right)


def RestartIfLessThanOrEqual(left: int, right: int):
    return TerminateIfComparison(EventEndType.Restart, ComparisonType.LessThanOrEqual, left, right)


# ACTION PROMPT


def IfActionButton(
    condition: int,
    prompt_text: EventTextInt,
    anchor_entity: CoordEntityInt,
    anchor_type=None,
    facing_angle=None,
    max_distance=None,
    model_point=-1,
    trigger_attribute=TriggerAttribute.Human_or_Hollow,
    button=0,
    boss_version=False,
    line_intersects=None,
    human_or_hollow_only=None,  # DEPRECATED. Will be removed in a later release. Use `trigger_attribute` instead.
):
    if anchor_type is None:
        try:
            anchor_type = anchor_entity.coord_entity_type
        except AttributeError:
            raise ValueError(
                "The `anchor_type` keyword is needed if `anchor_entity` is not an `Object`, `Region`, or `Character`."
            )

    if facing_angle is None:
        facing_angle = 0.0 if anchor_type == CoordEntityType.Region else 180.0

    if max_distance is None:
        max_distance = 0.0 if anchor_type == CoordEntityType.Region else 2.0

    if human_or_hollow_only is not None:
        _LOGGER.warning(
            "The `human_or_hollow_only` argument of `IfActionButton` is deprecated and will be removed soon. "
            "Use `trigger_attribute` instead, or leave it as the defaults of `TriggerAttribute.Human_or_Hollow`."
        )
        if not human_or_hollow_only and trigger_attribute == TriggerAttribute.Human_or_Hollow:
            raise ValueError(
                "If deprecated argument `human_or_hollow_only` is False, desired `trigger_attribute` must be specified."
            )

    args = [
        condition,
        anchor_type,
        anchor_entity,
        facing_angle,
        model_point,
        max_distance,
        prompt_text,
        trigger_attribute,
        button,
    ]

    if boss_version:
        if line_intersects is None:
            instruction_info = (3, 13)
            return to_numeric(instruction_info, *args)
        else:
            instruction_info = (3, 19)
            return to_numeric(instruction_info, *args, line_intersects)
    else:
        if line_intersects is None:
            instruction_info = (3, 5)
            return to_numeric(instruction_info, *args)
        else:
            instruction_info = (3, 18)
            return to_numeric(instruction_info, *args, line_intersects)


# WORLD TENDENCY


def IfWorldTendencyComparison(
    condition: int, world_tendency_type: WorldTendencyType, comparison_type: ComparisonType, value: int
):
    instruction_info = (3, 11)
    return to_numeric(instruction_info, condition, world_tendency_type, comparison_type, value)


def IfWhiteWorldTendencyComparison(condition: int, comparison_type: ComparisonType, value):
    return IfWorldTendencyComparison(condition, WorldTendencyType.White, comparison_type, value)


def IfBlackWorldTendencyComparison(condition: int, comparison_type: ComparisonType, value):
    return IfWorldTendencyComparison(condition, WorldTendencyType.Black, comparison_type, value)


def IfWhiteWorldTendencyGreaterThanOrEqual(condition: int, value):
    return IfWorldTendencyComparison(condition, WorldTendencyType.White, ComparisonType.GreaterThanOrEqual, value)


def IfBlackWorldTendencyGreaterThanOrEqual(condition: int, value):
    return IfWorldTendencyComparison(condition, WorldTendencyType.Black, ComparisonType.GreaterThanOrEqual, value)


# NEW GAME CYCLE


def IfNewGameCycleComparison(condition: int, comparison_type: ComparisonType, completion_count: int):
    instruction_info = (3, 17)
    return to_numeric(instruction_info, condition, comparison_type, completion_count)


def IfNewGameCycleEqual(condition: int, completion_count):
    return IfNewGameCycleComparison(condition, ComparisonType.Equal, completion_count)


def IfNewGameCycleGreaterThanOrEqual(condition: int, completion_count):
    return IfNewGameCycleComparison(condition, ComparisonType.GreaterThanOrEqual, completion_count)


# SYSTEM


def IfDLCState(condition: int, is_owned: bool):
    instruction_info = (3, 21)
    return to_numeric(instruction_info, condition, is_owned)


def IfDLCOwned(condition: int):
    return IfDLCState(condition, True)


def IfDLCNotOwned(condition: int):
    return IfDLCState(condition, False)


def IfOnlineState(condition: int, state: bool):
    instruction_info = (3, 22)
    return to_numeric(instruction_info, condition, state)


def IfOnline(condition: int):
    return IfOnlineState(condition, True)


def IfOffline(condition: int):
    return IfOnlineState(condition, False)


# CHARACTER


def IfCharacterDeathState(condition: int, character: CharacterInt, state: bool):
    instruction_info = (4, 0)
    return to_numeric(instruction_info, condition, character, state)


def IfCharacterDead(condition: int, character: CharacterInt):
    return IfCharacterDeathState(condition, character, True)


def IfCharacterAlive(condition: int, character: CharacterInt):
    return IfCharacterDeathState(condition, character, False)


def IfAttacked(condition: int, attacked_entity: CharacterInt, attacking_character: CharacterInt):
    instruction_info = (4, 1)
    return to_numeric(instruction_info, condition, attacked_entity, attacking_character)


def IfHealthComparison(condition: int, character: CharacterInt, comparison_type: ComparisonType, value):
    instruction_info = (4, 2)
    return to_numeric(instruction_info, condition, character, comparison_type, value)


def IfHealthEqual(condition: int, character: CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.Equal, value)


def IfHealthNotEqual(condition: int, character: CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.NotEqual, value)


def IfHealthGreaterThan(condition: int, character: CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.GreaterThan, value)


def IfHealthLessThan(condition: int, character: CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.LessThan, value)


def IfHealthGreaterThanOrEqual(condition: int, character: CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.GreaterThanOrEqual, value)


def IfHealthLessThanOrEqual(condition: int, character: CharacterInt, value):
    return IfHealthComparison(condition, character, ComparisonType.LessThanOrEqual, value)


def IfCharacterType(condition: int, character: CharacterInt, character_type: CharacterType):
    instruction_info = (4, 3)
    return to_numeric(instruction_info, condition, character, character_type)


def IfCharacterHollow(condition: int, character: CharacterInt):
    return IfCharacterType(condition, character, CharacterType.Hollow)


def IfCharacterHuman(condition: int, character: CharacterInt):
    return IfCharacterType(condition, character, CharacterType.Human)


def IfCharacterTargetingState(
    condition: int, targeting_character: CharacterInt, targeted_character: CharacterInt, state: bool
):
    instruction_info = (4, 4)
    return to_numeric(instruction_info, condition, targeting_character, targeted_character, state)


def IfCharacterTargeting(condition: int, targeting_character: CharacterInt, targeted_character: CharacterInt):
    return IfCharacterTargetingState(condition, targeting_character, targeted_character, True)


def IfCharacterNotTargeting(condition: int, targeting_character: CharacterInt, targeted_character: CharacterInt):
    return IfCharacterTargetingState(condition, targeting_character, targeted_character, False)


def IfCharacterSpecialEffectState(condition: int, character: CharacterInt, special_effect: int, state: bool):
    instruction_info = (4, 5, [0, 0, -1, 0])
    return to_numeric(instruction_info, condition, character, special_effect, state)


def IfCharacterHasSpecialEffect(condition: int, character: CharacterInt, special_effect: int):
    return IfCharacterSpecialEffectState(condition, character, special_effect, True)


def IfCharacterDoesNotHaveSpecialEffect(condition: int, character: CharacterInt, special_effect: int):
    return IfCharacterSpecialEffectState(condition, character, special_effect, False)


def IfCharacterPartHealthComparison(
    condition: int, character: CharacterInt, npc_part_id: int, comparison_type: ComparisonType, value
):
    instruction_info = (4, 6)
    return to_numeric(instruction_info, condition, character, npc_part_id, value, comparison_type)


def IfCharacterPartHealthLessThanOrEqual(condition: int, character: CharacterInt, npc_part_id: int, value):
    return IfCharacterPartHealthComparison(condition, character, npc_part_id, ComparisonType.LessThanOrEqual, value)


def IfCharacterBackreadState(condition: int, character: CharacterInt, state: bool):
    instruction_info = (4, 7)
    return to_numeric(instruction_info, condition, character, state)


def IfCharacterBackreadEnabled(condition: int, character: CharacterInt):
    return IfCharacterBackreadState(condition, character, True)


def IfCharacterBackreadDisabled(condition: int, character: CharacterInt):
    return IfCharacterBackreadState(condition, character, False)


def IfTAEEventState(condition: int, character: CharacterInt, tae_event_id: int, state: bool):
    instruction_info = (4, 8, [0, 0, -1, 0])
    return to_numeric(instruction_info, condition, character, tae_event_id, state)


def IfHasTAEEvent(condition: int, character: CharacterInt, tae_event_id: int):
    return IfTAEEventState(condition, character, tae_event_id, True)


def IfDoesNotHaveTAEEvent(condition: int, character: CharacterInt, tae_event_id: int):
    return IfTAEEventState(condition, character, tae_event_id, False)


def IfHasAIStatus(condition: int, character: CharacterInt, ai_status: AIStatusType):
    instruction_info = (4, 9)
    return to_numeric(instruction_info, condition, character, ai_status)


def IfSkullLanternState(condition: int, state: bool):
    instruction_info = (4, 10)
    return to_numeric(instruction_info, condition, state)


def IfSkullLanternActive(condition: int):
    return IfSkullLanternState(condition, True)


def IfSkullLanternInactive(condition: int):
    return IfSkullLanternState(condition, False)


def IfPlayerClass(condition: int, class_type: ClassType):
    instruction_info = (4, 11)
    return to_numeric(instruction_info, condition, class_type)


def IfPlayerCovenant(condition: int, covenant: Covenant):
    instruction_info = (4, 12)
    return to_numeric(instruction_info, condition, covenant)


def IfPlayerSoulLevelComparison(condition: int, comparison_type: ComparisonType, value):
    instruction_info = (4, 13, [0, 0, 1])
    return to_numeric(instruction_info, condition, comparison_type, value)


def IfPlayerSoulLevelGreaterThanOrEqual(condition: int, value):
    return IfPlayerSoulLevelComparison(condition, ComparisonType.GreaterThanOrEqual, value)


def IfPlayerSoulLevelLessThanOrEqual(condition: int, value):
    return IfPlayerSoulLevelComparison(condition, ComparisonType.LessThanOrEqual, value)


def IfHealthValueComparison(condition: int, character: CharacterInt, comparison_type: ComparisonType, value):
    instruction_info = (4, 14)
    return to_numeric(instruction_info, condition, character, comparison_type, value)


def IfHealthValueEqual(condition: int, character: CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.Equal, value)


def IfHealthValueNotEqual(condition: int, character: CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.NotEqual, value)


def IfHealthValueGreaterThan(condition: int, character: CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.GreaterThan, value)


def IfHealthValueLessThan(condition: int, character: CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.LessThan, value)


def IfHealthValueGreaterThanOrEqual(condition: int, character: CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.GreaterThanOrEqual, value)


def IfHealthValueLessThanOrEqual(condition: int, character: CharacterInt, value):
    return IfHealthValueComparison(condition, character, ComparisonType.LessThanOrEqual, value)


# BATTLE OF STOICISM (DO NOT USE)


def ArenaRankingRequest1v1():
    instruction_info = (2003, 37)
    return to_numeric(instruction_info)


def ArenaRankingRequest2v2():
    instruction_info = (2003, 38)
    return to_numeric(instruction_info)


def ArenaRankingRequestFFA():
    instruction_info = (2003, 39)
    return to_numeric(instruction_info)


def ArenaExitRequest():
    instruction_info = (2003, 40)
    return to_numeric(instruction_info)


def ArenaSetNametag1(player_id: int):
    instruction_info = (2007, 5)
    return to_numeric(instruction_info, player_id)


def ArenaSetNametag2(player_id: int):
    instruction_info = (2007, 6)
    return to_numeric(instruction_info, player_id)


def ArenaSetNametag3(player_id: int):
    instruction_info = (2007, 7)
    return to_numeric(instruction_info, player_id)


def ArenaSetNametag4(player_id: int):
    instruction_info = (2007, 8)
    return to_numeric(instruction_info, player_id)


def DisplayArenaDissolutionMessage(text_id):
    instruction_info = (2007, 9)
    return to_numeric(instruction_info, text_id)


def ArenaSetNametag5(player_id: int):
    instruction_info = (2007, 10)
    return to_numeric(instruction_info, player_id)


def ArenaSetNametag6(player_id: int):
    instruction_info = (2007, 11)
    return to_numeric(instruction_info, player_id)
