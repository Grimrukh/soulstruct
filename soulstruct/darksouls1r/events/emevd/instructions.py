"""Extension of PTDE instruction set."""

__all__ = [
    # Base
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
    "ArenaSetNametag5",
    "ArenaSetNametag6",

    # DS1PTDE and DS1R
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

    # DS1R ONLY
    "SkipLinesIfUnknownPlayerType4",
    "SkipLinesIfUnknownPlayerType5",
    "RestartIfUnknownPlayerType4",
    "RestartIfUnknownPlayerType5",
    "EndIfUnknownPlayerType4",
    "EndIfUnknownPlayerType5",
    "IfUnknownPlayerType4",
    "IfUnknownPlayerType5",
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
    "Unknown_2008_04",

    # Special additions
    "SendToScript",
    "NightfallCameraResetRequest",
]

from soulstruct.base.events.emevd.numeric import to_numeric
from soulstruct.game_types import *
from soulstruct.darksouls1ptde.events.emevd.instructions import *
from soulstruct.darksouls1ptde.events.emevd.enums import *


def SkipLinesIfUnknownPlayerType4(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.UnknownPlayerType4)


def SkipLinesIfUnknownPlayerType5(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.UnknownPlayerType5)


def EndIfUnknownPlayerType4():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.UnknownPlayerType4)


def EndIfUnknownPlayerType5():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.UnknownPlayerType5)


def IfUnknownPlayerType4(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.UnknownPlayerType4)


def IfUnknownPlayerType5(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.UnknownPlayerType5)


def RestartIfUnknownPlayerType4():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.UnknownPlayerType4)


def RestartIfUnknownPlayerType5():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.UnknownPlayerType5)


def Unknown_3_23(condition: int, arg1: int, arg2: int):
    """ Unknown command. 'arg1' and 'arg2' appear to both always be zero. """
    instruction_info = (3, 23)
    return to_numeric(instruction_info, condition, arg1, arg2)


def IfMultiplayerCount(condition: int, arg1: int, arg2: int):
    """ Unknown arguments. Useful for Battle of Stoicism only, so probably useless to you. """
    instruction_info = (3, 24)
    return to_numeric(instruction_info, condition, arg1, arg2)


def Unknown_4_15(condition: int, arg1: int):
    instruction_info = (4, 15)
    return to_numeric(instruction_info, condition, arg1)


def Unknown_4_16(condition: int, arg1: int, arg2: int, arg3: int):
    instruction_info = (4, 16)
    return to_numeric(instruction_info, condition, arg1, arg2, arg3)


def IfArenaMatchmaking(condition: int):
    instruction_info = (4, 17)
    return to_numeric(instruction_info, condition)


def Unknown_2000_06(arg1: int):
    instruction_info = (2000, 6)
    return to_numeric(instruction_info, arg1)


def PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect1(
    condition: int,
    cutscene_type: CutsceneType,
    first_region: RegionTyping,
    last_region: RegionTyping,
    game_map: MapTyping,
):
    instruction_info = (2002, 6)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, condition, cutscene_type, first_region, last_region, area_id, block_id)


def PlayCutsceneAndRandomlyWarpPlayer_WithUnknownEffect2(
    condition: int,
    cutscene_type: CutsceneType,
    first_region: RegionTyping,
    last_region: RegionTyping,
    game_map: MapTyping,
):
    instruction_info = (2002, 7)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, condition, cutscene_type, first_region, last_region, area_id, block_id)


def CopyEventValue(source_flag: FlagInt, destination_flag: FlagInt, bit_count: int):
    instruction_info = (2003, 42)
    return to_numeric(instruction_info, source_flag, destination_flag, bit_count)


def Unknown_2003_43(flag: FlagInt, bit_count: int, arg1: int, arg2: int):
    instruction_info = (2003, 43)
    return to_numeric(instruction_info, flag, bit_count, arg1, arg2)


def ForceAnimation_WithUnknownEffect1(
    entity: AnimatedTyping, animation: int, loop: bool, wait_for_completion: bool, skip_transition: bool, arg1: int
):
    instruction_info = (2003, 44)
    return to_numeric(instruction_info, entity, animation, loop, wait_for_completion, skip_transition, arg1)


def ForceAnimation_WithUnknownEffect2(
    entity: AnimatedTyping, animation: int, loop: bool, wait_for_completion: bool, skip_transition: bool, arg1: float
):
    instruction_info = (2003, 46)
    return to_numeric(instruction_info, entity, animation, loop, wait_for_completion, skip_transition, arg1)


def Unknown_2003_47():
    instruction_info = (2003, 47)
    return to_numeric(instruction_info)


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


def EraseNPCSummonSign(summoned_character: CharacterTyping):
    instruction_info = (2003, 49)
    return to_numeric(instruction_info, summoned_character)


def FadeOutCharacter(character: CharacterTyping, duration: float):
    instruction_info = (2004, 48)
    return to_numeric(instruction_info, character, duration)


def FadeInCharacter(character: CharacterTyping, duration: float):
    instruction_info = (2004, 49)
    return to_numeric(instruction_info, character, duration)


def Unknown_2004_50():
    instruction_info = (2004, 50)
    return to_numeric(instruction_info)


def Unknown_2004_51(arg1: int):
    instruction_info = (2004, 51)
    return to_numeric(instruction_info, arg1)


def Unknown_2004_52():
    instruction_info = (2004, 52)
    return to_numeric(instruction_info)


def ArenaSetNametag5(player_id: int):
    instruction_info = (2007, 10)
    return to_numeric(instruction_info, player_id)


def ArenaSetNametag6(player_id: int):
    instruction_info = (2007, 11)
    return to_numeric(instruction_info, player_id)


def DisplayConcatenatedMessage(message_id: int, pad_enabled: bool, concatenator_base_flag: FlagInt, bit_count: int):
    instruction_info = (2007, 12)
    return to_numeric(instruction_info, message_id, pad_enabled, concatenator_base_flag, bit_count)


def Unknown_2007_13(arg1: int):
    instruction_info = (2007, 13)
    return to_numeric(instruction_info, arg1)


def Unknown_2008_04():
    instruction_info = (2008, 4)
    return to_numeric(instruction_info)


# SPECIAL ADDITIONS


def SendToScript(int1: int, int2: int, float1: float, float2: float):
    """Special instruction added by Horkrux for communication with `DarkSoulsScripting.dll`."""
    instruction_info = (2009, 7)
    return to_numeric(instruction_info, int1, int2, float1, float2)


def NightfallCameraResetRequest():
    """Special instruction added by Meowmaritus for camera manipulation in Nightfall."""
    instruction_info = (2009, 12)
    return to_numeric(instruction_info)
