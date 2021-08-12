"""Full instruction set for DS1 (both PTD and DSR). 

I haven't yet put any restrictions on using the new DSR instructions in PTD, so beware of that.
"""
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
    "SetObjectInvulnerabilityState",
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
    "CreateVFX",
    "DeleteVFX",
    "CreateTemporaryVFX",
    "CreateObjectVFX",
    "DeleteObjectVFX",
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
    "SetSoapstoneMessageState",
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
    "SetNetworkSyncState",
    "EnableNetworkSync",
    "DisableNetworkSync",
    "ClearMainCondition",
    "IssuePrefetchRequest",
    "SaveRequest",
    "TriggerMultiplayerEvent",
    "SetVagrantSpawningState",
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
    "Return",
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
    "ReturnIfConditionState",
    "EndIfConditionTrue",
    "EndIfConditionFalse",
    "RestartIfConditionTrue",
    "RestartIfConditionFalse",
    "ReturnIfFinishedConditionState",
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
    "ReturnIfMapPresenceState",
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
    "ReturnIfFlagState",
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
    "ReturnIfFlagRangeState",
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
    "ReturnIfObjectDestructionState",
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
    "ReturnIfComparison",
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
    # Special additions
    "SendToScript",

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
    "ReturnIfMultiplayerState",
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
    "RegisterHealingFountain",
]

from soulstruct.base.events.emevd.numeric import to_numeric
from soulstruct.game_types import *
from soulstruct.base.events.emevd.instructions import *

from .enums import *


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


def ReturnIfMultiplayerState(event_return_type: EventReturnType, state: MultiplayerState):
    instruction_info = (1003, 6)
    return to_numeric(instruction_info, event_return_type, state)


def EndIfHost():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.Host)


def EndIfClient():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.Client)


def EndIfMultiplayer():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.Multiplayer)


def EndIfSingleplayer():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.Singleplayer)


def RestartIfHost():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.Host)


def RestartIfClient():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.Client)


def RestartIfMultiplayer():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.Multiplayer)


def RestartIfSingleplayer():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.Singleplayer)


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


# BOSS


def SetBossHealthBarState(character: CharacterTyping, name: NPCNameTyping, slot, state: bool):
    """ Note: slot number can be 0-1 in DS1. """
    instruction_info = (2003, 11)
    if isinstance(slot, int) and slot not in (0, 1):
        raise ValueError("Boss health bar slot must be 0 or 1.")
    return to_numeric(instruction_info, state, character, slot, name)


def EnableBossHealthBar(character: CharacterTyping, name: NPCNameTyping, slot=0):
    """ The character's health bar will appear at the bottom of the screen, with a name. """
    return SetBossHealthBarState(character, name, slot, True)


def DisableBossHealthBar(character: CharacterTyping, name: NPCNameTyping = 0, slot=0):
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
