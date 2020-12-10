"""Full instruction set for DS1 (both PTD and DSR). 

I haven't yet put any restrictions on using the new DSR instructions in PTD, so beware of that.
"""
from soulstruct.events.numeric import to_numeric
from soulstruct.game_types import *
from soulstruct.events.darksouls1.enums import *
from soulstruct.events.shared.instructions import *

__all__ = [
    # Shared
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
    # "IfCharacterRegionState" and shortcut versions overridden in Dark Souls 1.
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
    # Dark Souls 1
    "IfCharacterRegionState",
    "IfCharacterInsideRegion",
    "IfCharacterOutsideRegion",
    "IfPlayerInsideRegion",
    "IfPlayerOutsideRegion",
    "SkipLinesIfMultiplayerState",
    "SkipLinesIfHost",
    "SkipLinesIfClient",
    "SkipLinesIfMultiplayer",
    "SkipLinesIfSingleplayer",
    "TerminateIfMultiplayerState",
    "EndIfHost",
    "EndIfClient",
    "EndIfMultiplayer",
    "EndIfSingleplayer",
    "RestartIfHost",
    "RestartIfClient",
    "RestartIfMultiplayer",
    "RestartIfSingleplayer",
    "IfMultiplayerState",
    "IfHost",
    "IfClient",
    "IfMultiplayer",
    "IfSingleplayer",
    "SetBossHealthBarState",
    "EnableBossHealthBar",
    "DisableBossHealthBar",
    "ActivateKillplaneForModel",
    "AddSpecialEffect",
    "RotateToFaceEntity",
    # REMASTERED ONLY (mostly Arena events - no warning given if you try to use these in PTDE!)
    "SkipLinesIfUnknownPlayerType4",
    "SkipLinesIfUnknownPlayerType5",
    "RestartIfUnknownPlayerType4",
    "RestartIfUnknownPlayerType5",
    "EndIfUnknownPlayerType4",
    "EndIfUnknownPlayerType5",
    "IfUnknownPlayerType4",
    "IfUnknownPlayerType5",
    "RegisterHealingFountain",
    "Unknown_3_23",
    "IfMultiplayerCount",
    "Unknown_4_15",
    "Unknown_4_16",
    "IfArenaMatchmaking",
    "Unknown_2000_06",
    "PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect1",
    "PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect2",
    "CopyEventValue",
    "Unknown_2003_43",
    "ForceAnimation_WithUnknownEffect1",
    "ForceAnimation_WithUnknownEffect2",
    "Unknown_2003_47",
    "Unknown_2003_48",
    "EraseNPCSummonSign",
    "FadeOutCharacter",
    "FadeInCharacter",
    "Unknown_2004_50",
    "Unknown_2004_51",
    "Unknown_2004_52",
    "DisplayConcatenatedMessage",
    "Unknown_2007_13",
    "Unknown_2008_4",
]


def IfCharacterRegionState(condition, entity: AnimatedTyping, region: RegionTyping, state: bool):
    instruction_info = (3, 2)
    return to_numeric(instruction_info, condition, state, entity, region)


def IfCharacterInsideRegion(condition: int, entity: AnimatedTyping, region: RegionTyping):
    return IfCharacterRegionState(condition, entity, region, True)


def IfCharacterOutsideRegion(condition: int, entity: AnimatedTyping, region: RegionTyping):
    return IfCharacterRegionState(condition, entity, region, False)


def IfPlayerInsideRegion(condition: int, region: RegionTyping):
    return IfCharacterRegionState(condition, PLAYER, region, True)


def IfPlayerOutsideRegion(condition: int, region: RegionTyping):
    return IfCharacterRegionState(condition, PLAYER, region, False)


# MULTIPLAYER STATE


def SkipLinesIfMultiplayerState(line_count, state: MultiplayerState):
    instruction_info = (1003, 5)
    return to_numeric(instruction_info, line_count, state)


def SkipLinesIfHost(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Host)


def SkipLinesIfClient(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Client)


def SkipLinesIfMultiplayer(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Multiplayer)


def SkipLinesIfSingleplayer(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Singleplayer)


# REMASTERED ONLY
def SkipLinesIfUnknownPlayerType4(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.UnknownPlayerType4)


# REMASTERED ONLY
def SkipLinesIfUnknownPlayerType5(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.UnknownPlayerType5)


def TerminateIfMultiplayerState(event_end_type: EventEndType, state: MultiplayerState):
    instruction_info = (1003, 6)
    return to_numeric(instruction_info, event_end_type, state)


def EndIfHost():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Host)


def EndIfClient():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Client)


def EndIfMultiplayer():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Multiplayer)


def EndIfSingleplayer():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.Singleplayer)


# REMASTERED ONLY
def EndIfUnknownPlayerType4():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.UnknownPlayerType4)


# REMASTERED ONLY
def EndIfUnknownPlayerType5():
    return TerminateIfMultiplayerState(EventEndType.End, MultiplayerState.UnknownPlayerType5)


def RestartIfHost():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Host)


def RestartIfClient():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Client)


def RestartIfMultiplayer():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Multiplayer)


def RestartIfSingleplayer():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Singleplayer)


# REMASTERED ONLY
def RestartIfUnknownPlayerType4():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.UnknownPlayerType4)


# REMASTERED ONLY
def RestartIfUnknownPlayerType5():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.UnknownPlayerType5)


def IfMultiplayerState(condition: int, state: MultiplayerState):
    instruction_info = (3, 6)
    return to_numeric(instruction_info, condition, state)


def IfHost(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Host)


def IfClient(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Client)


def IfMultiplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Multiplayer)


def IfSingleplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Singleplayer)


# REMASTERED ONLY
def IfUnknownPlayerType4(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.UnknownPlayerType4)


# REMASTERED ONLY
def IfUnknownPlayerType5(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.UnknownPlayerType5)


# BOSS


def SetBossHealthBarState(character: CharacterTyping, name: EventTextTyping, slot, state: bool):
    """ Note: slot number can be 0-1 in DS1. """
    instruction_info = (2003, 11)
    if isinstance(slot, int) and slot not in (0, 1):
        raise ValueError("Boss health bar slot must be 0 or 1.")
    return to_numeric(instruction_info, state, character, slot, name)


def EnableBossHealthBar(character: CharacterTyping, name: EventTextTyping, slot=0):
    """ The character's health bar will appear at the bottom of the screen, with a name. """
    return SetBossHealthBarState(character, name, slot, True)


def DisableBossHealthBar(character: CharacterTyping, name: EventTextTyping = 0, slot=0):
    """ The character's health bar will disappear from the bottom of the screen.

    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter, so only the
    first argument actually does anything. You're welcome to specify the name for clarity anyway (and vanilla events
    will show it when decompiled). """
    return SetBossHealthBarState(character, name, slot, False)


# MISC.


def ActivateKillplaneForModel(game_map: MapTyping, y_threshold, target_model_id):
    """ Not used much. Activates a horizontal killplane that only affects a particular model ID. """
    instruction_info = (2003, 41)
    return to_numeric(instruction_info, game_map.area_id, game_map.block_id, y_threshold, target_model_id)


def AddSpecialEffect(character: CharacterTyping, special_effect_id: int):
    """ 'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will do
    nothing if the character already has the special effect active (i.e. they do not stack or even reset timers). """
    instruction_info = (2004, 8)
    return to_numeric(instruction_info, character, special_effect_id)


def RotateToFaceEntity(character: CharacterTyping, target_entity: CoordEntityTyping):
    """ Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at least.)
    """
    instruction_info = (2004, 14)
    return to_numeric(instruction_info, character, target_entity)


def RegisterHealingFountain(flag: FlagInt, obj: ObjectTyping):
    """ No idea what this is. Clearly unused. The Bloodborne version has more arguments. """
    instruction_info = (2009, 5)
    return to_numeric(instruction_info, flag, obj)


# REMASTERED ONLY
def Unknown_3_23(condition: int, arg1: int, arg2: int):
    """ Unknown command. 'arg1' and 'arg2' appear to both always be zero. """
    instruction_info = (3, 23)
    return to_numeric(instruction_info, condition, arg1, arg2)


# REMASTERED ONLY
def IfMultiplayerCount(condition: int, arg1: int, arg2: int):
    """ Unknown arguments. Useful for Battle of Stoicism only, so probably useless to you. """
    instruction_info = (3, 24)
    return to_numeric(instruction_info, condition, arg1, arg2)


# REMASTERED ONLY
def Unknown_4_15(condition: int, arg1: int):
    instruction_info = (4, 15)
    return to_numeric(instruction_info, condition, arg1)


# REMASTERED ONLY
def Unknown_4_16(condition: int, arg1: int, arg2: int, arg3: int):
    instruction_info = (4, 16)
    return to_numeric(instruction_info, condition, arg1, arg2, arg3)


# REMASTERED ONLY
def IfArenaMatchmaking(condition: int):
    instruction_info = (4, 17)
    return to_numeric(instruction_info, condition)


# REMASTERED ONLY
def Unknown_2000_06(arg1: int):
    instruction_info = (2000, 6)
    return to_numeric(instruction_info, arg1)


# REMASTERED ONLY
def PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect1(
    condition: int,
    playback_method: CutsceneType,
    first_region: RegionTyping,
    last_region: RegionTyping,
    game_map: MapTyping,
):
    instruction_info = (2002, 6)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, condition, playback_method, first_region, last_region, area_id, block_id)


# REMASTERED ONLY
def PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect2(
    condition: int,
    playback_method: CutsceneType,
    first_region: RegionTyping,
    last_region: RegionTyping,
    game_map: MapTyping,
):
    instruction_info = (2002, 7)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, condition, playback_method, first_region, last_region, area_id, block_id)


# REMASTERED ONLY
def CopyEventValue(source_flag: FlagInt, destination_flag: FlagInt, bit_count: int):
    instruction_info = (2003, 42)
    return to_numeric(instruction_info, source_flag, destination_flag, bit_count)


# REMASTERED ONLY
def Unknown_2003_43(flag: FlagInt, bit_count: int, arg1: int, arg2: int):
    instruction_info = (2003, 43)
    return to_numeric(instruction_info, flag, bit_count, arg1, arg2)


# REMASTERED ONLY
def ForceAnimation_WithUnknownEffect1(
    entity: AnimatedTyping, animation: int, loop: bool, wait_for_completion: bool, skip_transition: bool, arg1: int
):
    instruction_info = (2003, 44)
    return to_numeric(instruction_info, entity, animation, loop, wait_for_completion, skip_transition, arg1)


# REMASTERED ONLY
def ForceAnimation_WithUnknownEffect2(
    entity: AnimatedTyping, animation: int, loop: bool, wait_for_completion: bool, skip_transition: bool, arg1: float
):
    instruction_info = (2003, 46)
    return to_numeric(instruction_info, entity, animation, loop, wait_for_completion, skip_transition, arg1)


# REMASTERED ONLY
def Unknown_2003_47():
    instruction_info = (2003, 47)
    return to_numeric(instruction_info)


# REMASTERED ONLY
def Unknown_2003_48(
    entity: AnimatedTyping,
    arg1: int,
    model_point: int,
    magic_id: int,
    shoot_angle_x: int,
    shoot_angle_y: int,
    shoot_angle_z: int,
):
    instruction_info = (2003, 48)
    return to_numeric(
        instruction_info, entity, arg1, model_point, magic_id, shoot_angle_x, shoot_angle_y, shoot_angle_z
    )


# REMASTERED ONLY
def EraseNPCSummonSign(summoned_character: CharacterTyping):
    instruction_info = (2003, 49)
    return to_numeric(instruction_info, summoned_character)


# REMASTERED ONLY
def FadeOutCharacter(character: CharacterTyping, duration: float):
    instruction_info = (2004, 48)
    return to_numeric(instruction_info, character, duration)


# REMASTERED ONLY
def FadeInCharacter(character: CharacterTyping, duration: float):
    instruction_info = (2004, 49)
    return to_numeric(instruction_info, character, duration)


"""
[50] - UNKNOWN 2004[50] (DS1R ONLY)
 [51] - UNKNOWN 2004[51] (DS1R ONLY)
      i  Unknown [ENUM: BOOL]
 [52] - UNKNOWN 2004[52] (DS1R ONLY)
"""

# REMASTERED ONLY
def Unknown_2004_50():
    instruction_info = (2004, 50)
    return to_numeric(instruction_info)


# REMASTERED ONLY
def Unknown_2004_51(arg1: int):
    instruction_info = (2004, 51)
    return to_numeric(instruction_info, arg1)


# REMASTERED ONLY
def Unknown_2004_52():
    instruction_info = (2004, 52)
    return to_numeric(instruction_info)


# REMASTERED ONLY
def DisplayConcatenatedMessage(message_id: Text, pad_enabled: bool, concatenator_base_flag: Flag, bit_count: int):
    instruction_info = (2007, 12)
    return to_numeric(instruction_info, message_id, pad_enabled, concatenator_base_flag, bit_count)


# REMASTERED ONLY
def Unknown_2007_13(arg1: int):
    instruction_info = (2007, 13)
    return to_numeric(instruction_info, arg1)


# REMASTERED ONLY
def Unknown_2008_4():
    instruction_info = (2008, 4)
    return to_numeric(instruction_info)
