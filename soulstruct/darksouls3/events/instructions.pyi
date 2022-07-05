"""AUTOMATICALLY GENERATED. Do not edit this module.

Import this into any EVS script to have full access to instructions.
Make sure you also do `from soulstruct.{game}.events import *` to get all enums, constants, and tests.
"""

__all__ = [
    "IfConditionState",  # 0[0]
    "IfConditionTrue",
    "IfConditionFalse",
    "IfValueComparison",  # 0[1]
    "IfValueEqual",
    "IfValueNotEqual",
    "IfValueGreaterThan",
    "IfValueLessThan",
    "IfValueGreaterThanOrEqual",
    "IfValueLessThanOrEqual",
    "IfTimeElapsed",  # 1[0]
    "IfFramesElapsed",  # 1[1]
    "IfRandomTimeElapsed",  # 1[2]
    "IfRandomFramesElapsed",  # 1[3]
    "IfFlagState",  # 3[0]
    "IfFlagEnabled",
    "IfFlagDisabled",
    "IfThisEventFlagEnabled",
    "IfThisEventFlagDisabled",
    "IfThisEventSlotFlagEnabled",
    "IfThisEventSlotFlagDisabled",
    "IfFlagRangeState",  # 3[1]
    "IfFlagRangeAllEnabled",
    "IfFlagRangeAllDisabled",
    "IfFlagRangeAnyEnabled",
    "IfFlagRangeAnyDisabled",
    "IfCharacterRegionState",  # 3[2]
    "IfPlayerInsideRegion",
    "IfPlayerOutsideRegion",
    "IfCharacterInsideRegion",
    "IfCharacterOutsideRegion",
    "IfEntityDistanceState",  # 3[3]
    "IfPlayerWithinDistance",
    "IfPlayerBeyondDistance",
    "IfEntityWithinDistance",
    "IfEntityBeyondDistance",
    "IfPlayerItemStateExcludingStorage",  # 3[4]
    "IfActionButtonBasic",  # 3[5]
    "IfMultiplayerState",  # 3[6]
    "IfHost",
    "IfClient",
    "IfTryingToCreateSession",
    "IfTryingToJoinSession",
    "IfLeavingSession",
    "IfFailedToCreateSession",
    "IfAllPlayersRegionState",  # 3[7]
    "IfAllPlayersInsideRegion",
    "IfAllPlayersOutsideRegion",
    "IfMapPresenceState",  # 3[8]
    "IfInsideMap",
    "IfOutsideMap",
    "IfMultiplayerEvent",  # 3[9]
    "IfTrueFlagCountComparison",  # 3[10]
    "IfTrueFlagCountEqual",
    "IfTrueFlagCountNotEqual",
    "IfTrueFlagCountGreaterThan",
    "IfTrueFlagCountLessThan",
    "IfTrueFlagCountGreaterThanOrEqual",
    "IfTrueFlagCountLessThanOrEqual",
    "IfWorldTendencyComparison",  # 3[11]
    "IfWhiteWorldTendencyComparison",
    "IfBlackWorldTendencyComparison",
    "IfWhiteWorldTendencyGreaterThanOrEqual",
    "IfBlackWorldTendencyGreaterThanOrEqual",
    "IfEventValueComparison",  # 3[12]
    "IfEventValueEqual",
    "IfEventValueNotEqual",
    "IfEventValueGreaterThan",
    "IfEventValueLessThan",
    "IfEventValueGreaterThanOrEqual",
    "IfEventValueLessThanOrEqual",
    "IfActionButtonBoss",  # 3[13]
    "IfAnyItemDroppedInRegion",  # 3[14]
    "IfItemDropped",  # 3[15]
    "IfPlayerItemStateIncludingStorage",  # 3[16]
    "IfNewGameCycleComparison",  # 3[17]
    "IfNewGameCycleEqual",
    "IfNewGameCycleNotEqual",
    "IfNewGameCycleGreaterThan",
    "IfNewGameCycleLessThan",
    "IfNewGameCycleGreaterThanOrEqual",
    "IfNewGameCycleLessThanOrEqual",
    "IfActionButtonBasicLineIntersect",  # 3[18]
    "IfActionButtonBossLineIntersect",  # 3[19]
    "IfEventsComparison",  # 3[20]
    "IfDLCState",  # 3[21]
    "IfDLCOwned",
    "IfDLCNotOwned",
    "IfOnlineState",  # 3[22]
    "IfOnline",
    "IfOffline",
    "IfCharacterDeathState",  # 4[0]
    "IfCharacterDead",
    "IfCharacterAlive",
    "IfAttacked",  # 4[1]
    "IfHealthComparison",  # 4[2]
    "IfHealthEqual",
    "IfHealthNotEqual",
    "IfHealthGreaterThan",
    "IfHealthLessThan",
    "IfHealthGreaterThanOrEqual",
    "IfHealthLessThanOrEqual",
    "IfCharacterType",  # 4[3]
    "IfCharacterHuman",
    "IfCharacterWhitePhantom",
    "IfCharacterHollow",
    "IfCharacterTargetingState",  # 4[4]
    "IfCharacterTargeting",
    "IfCharacterNotTargeting",
    "IfCharacterSpecialEffectState",  # 4[5]
    "IfPlayerHasSpecialEffect",
    "IfPlayerDoesNotHaveSpecialEffect",
    "IfCharacterHasSpecialEffect",
    "IfCharacterDoesNotHaveSpecialEffect",
    "IfCharacterPartHealthComparison",  # 4[6]
    "IfCharacterPartHealthLessThanOrEqual",
    "IfCharacterBackreadState",  # 4[7]
    "IfCharacterBackreadEnabled",
    "IfCharacterBackreadDisabled",
    "IfCharacterTAEEventState",  # 4[8]
    "IfCharacterHasTAEEvent",
    "IfCharacterDoesNotHaveTAEEvent",
    "IfHasAIStatus",  # 4[9]
    "IfSkullLanternState",  # 4[10]
    "IfSkullLanternActive",
    "IfSkullLanternInactive",
    "IfPlayerClass",  # 4[11]
    "IfPlayerCovenant",  # 4[12]
    "IfPlayerLevelComparison",  # 4[13]
    "IfPlayerLevelEqual",
    "IfPlayerLevelNotEqual",
    "IfPlayerLevelGreaterThan",
    "IfPlayerLevelLessThan",
    "IfPlayerLevelGreaterThanOrEqual",
    "IfPlayerLevelLessThanOrEqual",
    "IfHealthValueComparison",  # 4[14]
    "IfHealthValueEqual",
    "IfHealthValueNotEqual",
    "IfHealthValueGreaterThan",
    "IfHealthValueLessThan",
    "IfHealthValueGreaterThanOrEqual",
    "IfHealthValueLessThanOrEqual",
    "IfObjectDestructionState",  # 5[0]
    "IfObjectDestroyed",
    "IfObjectNotDestroyed",
    "IfObjectDamaged",  # 5[1]
    "IfObjectActivated",  # 5[2]
    "IfObjectHealthValueComparison",  # 5[3]
    "IfPlayerMovingOnCollision",  # 11[0]
    "IfPlayerRunningOnCollision",  # 11[1]
    "IfPlayerStandingOnCollision",  # 11[2]
    "AwaitConditionState",  # 1000[0]
    "AwaitConditionTrue",
    "AwaitConditionFalse",
    "SkipLinesIfConditionState",  # 1000[1]
    "SkipLinesIfConditionTrue",
    "SkipLinesIfConditionFalse",
    "ReturnIfConditionState",  # 1000[2]
    "EndIfConditionTrue",
    "EndIfConditionFalse",
    "RestartIfConditionTrue",
    "RestartIfConditionFalse",
    "SkipLines",  # 1000[3]
    "Return",  # 1000[4]
    "End",
    "Restart",
    "SkipLinesIfComparison",  # 1000[5]
    "SkipLinesIfEqual",
    "SkipLinesIfNotEqual",
    "SkipLinesIfGreaterThan",
    "SkipLinesIfLessThan",
    "SkipLinesIfGreaterThanOrEqual",
    "SkipLinesIfLessThanOrEqual",
    "ReturnIfComparison",  # 1000[6]
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
    "SkipLinesIfFinishedConditionState",  # 1000[7]
    "SkipLinesIfFinishedConditionTrue",
    "SkipLinesIfFinishedConditionFalse",
    "ReturnIfFinishedConditionState",  # 1000[8]
    "EndIfFinishedConditionTrue",
    "EndIfFinishedConditionFalse",
    "RestartIfFinishedConditionTrue",
    "RestartIfFinishedConditionFalse",
    "WaitForNetworkApproval",  # 1000[9]
    "Wait",  # 1001[0]
    "WaitFrames",  # 1001[1]
    "WaitRandomSeconds",  # 1001[2]
    "WaitRandomFrames",  # 1001[3]
    "AwaitFlagState",  # 1003[0]
    "AwaitFlagEnabled",
    "AwaitFlagDisabled",
    "AwaitThisEventOn",
    "AwaitThisEventOff",
    "AwaitThisEventSlotOn",
    "AwaitThisEventSlotOff",
    "SkipLinesIfFlagState",  # 1003[1]
    "SkipLinesIfFlagEnabled",
    "SkipLinesIfFlagDisabled",
    "SkipLinesIfThisEventFlagEnabled",
    "SkipLinesIfThisEventFlagDisabled",
    "SkipLinesIfThisEventSlotFlagEnabled",
    "SkipLinesIfThisEventSlotFlagDisabled",
    "ReturnIfFlagState",  # 1003[2]
    "EndIfFlagEnabled",
    "EndIfFlagDisabled",
    "EndIfThisEventFlagEnabled",
    "EndIfThisEventFlagDisabled",
    "EndIfThisEventSlotFlagEnabled",
    "EndIfThisEventSlotFlagDisabled",
    "RestartIfFlagEnabled",
    "RestartIfFlagDisabled",
    "RestartIfThisEventFlagEnabled",
    "RestartIfThisEventFlagDisabled",
    "RestartIfThisEventSlotFlagEnabled",
    "RestartIfThisEventSlotFlagDisabled",
    "SkipLinesIfFlagRangeState",  # 1003[3]
    "SkipLinesIfFlagRangeAllEnabled",
    "SkipLinesIfFlagRangeAllDisabled",
    "SkipLinesIfFlagRangeAnyEnabled",
    "SkipLinesIfFlagRangeAnyDisabled",
    "ReturnIfFlagRangeState",  # 1003[4]
    "EndIfFlagRangeAllEnabled",
    "EndIfFlagRangeAllDisabled",
    "EndIfFlagRangeAnyEnabled",
    "EndIfFlagRangeAnyDisabled",
    "RestartIfFlagRangeAllEnabled",
    "RestartIfFlagRangeAllDisabled",
    "RestartIfFlagRangeAnyEnabled",
    "RestartIfFlagRangeAnyDisabled",
    "SkipLinesIfMapPresenceState",  # 1003[7]
    "SkipLinesIfInsideMap",
    "SkipLinesIfOutsideMap",
    "ReturnIfMapPresenceState",  # 1003[8]
    "EndIfInsideMap",
    "EndIfOutsideMap",
    "RestartIfInsideMap",
    "RestartIfOutsideMap",
    "AwaitObjectDestructionState",  # 1005[0]
    "AwaitObjectDestroyed",
    "AwaitObjectNotDestroyed",
    "SkipLinesIfObjectDestructionState",  # 1005[1]
    "SkipLinesIfObjectDestroyed",
    "SkipLinesIfObjectNotDestroyed",
    "ReturnIfObjectDestructionState",  # 1005[2]
    "EndIfObjectDestroyed",
    "EndIfObjectNotDestroyed",
    "RestartIfObjectDestroyed",
    "RestartIfObjectNotDestroyed",
    "TerminateEvent",  # 2000[1]
    "SetNetworkSyncState",  # 2000[2]
    "EnableNetworkSync",
    "DisableNetworkSync",
    "ClearMainCondition",  # 2000[3]
    "IssuePrefetchRequest",  # 2000[4]
    "SaveRequest",  # 2000[5]
    "RunCommonEvent",  # 2000[6]
    "PlayCutsceneToAll",  # 2002[1]
    "PlayCutsceneAndMovePlayer",  # 2002[2]
    "PlayCutsceneToPlayer",  # 2002[3]
    "PlayCutsceneAndMoveSpecificPlayer",  # 2002[4]
    "PlayCutsceneAndRotatePlayer",  # 2002[5]
    "RequestAnimation",  # 2003[1]
    "SetFlagState",  # 2003[2]
    "EnableFlag",
    "DisableFlag",
    "ToggleFlag",
    "SetSpawnerState",  # 2003[3]
    "EnableSpawner",
    "DisableSpawner",
    "AwardItemLotToAllPlayers",  # 2003[4]
    "ShootProjectile",  # 2003[5]
    "SetEventState",  # 2003[8]
    "StopEvent",
    "RestartEvent",
    "SetBossHealthBarState",  # 2003[11]
    "EnableBossHealthBar",
    "DisableBossHealthBar",
    "KillBoss",  # 2003[12]
    "SetNavmeshType",  # 2003[13]
    "EnableNavmeshType",
    "DisableNavmeshType",
    "ToggleNavmeshType",
    "WarpToMap",  # 2003[14]
    "HandleMinibossDefeat",  # 2003[15]
    "TriggerMultiplayerEvent",  # 2003[16]
    "SetRandomFlagInRange",  # 2003[17]
    "EnableRandomFlagInRange",
    "DisableRandomFlagInRange",
    "ToggleRandomFlagInRange",
    "ForceAnimation",  # 2003[18]
    "SetMapDrawParamSlot",  # 2003[19]
    "IncrementNewGameCycle",  # 2003[21]
    "SetFlagRangeState",  # 2003[22]
    "EnableFlagRange",
    "DisableFlagRange",
    "ToggleFlagRange",
    "SetRespawnPoint",  # 2003[23]
    "RemoveItemFromPlayer",  # 2003[24]
    "RemoveWeaponFromPlayer",
    "RemoveArmorFromPlayer",
    "RemoveRingFromPlayer",
    "RemoveGoodFromPlayer",
    "PlaceSummonSign",  # 2003[25]
    "SetSoapstoneMessageState",  # 2003[26]
    "EnableSoapstoneMessage",
    "DisableSoapstoneMessage",
    "AwardAchievement",  # 2003[28]
    "SetVagrantSpawningState",  # 2003[30]
    "EnableVagrantSpawning",
    "DisableVagrantSpawning",
    "IncrementEventValue",  # 2003[31]
    "ClearEventValue",  # 2003[32]
    "SetNextSnugglyTrade",  # 2003[33]
    "SnugglyItemDrop",  # 2003[34]
    "MoveRemains",  # 2003[35]
    "AwardItemLotToHostOnly",  # 2003[36]
    "ArenaRankingRequest1v1",  # 2003[37]
    "ArenaRankingRequest2v2",  # 2003[38]
    "ArenaRankingRequestFFA",  # 2003[39]
    "ArenaExitRequest",  # 2003[40]
    "EventValueOperation",  # 2003[41]
    "SetAIState",  # 2004[1]
    "EnableAI",
    "DisableAI",
    "SetTeamType",  # 2004[2]
    "MoveToEntity",  # 2004[3]
    "Kill",  # 2004[4]
    "SetCharacterState",  # 2004[5]
    "EnableCharacter",
    "DisableCharacter",
    "EzstateAIRequest",  # 2004[6]
    "CreateProjectileOwner",  # 2004[7]
    "AddSpecialEffect",  # 2004[8]
    "SetStandbyAnimationSettings",  # 2004[9]
    "ResetStandbyAnimationSettings",
    "SetGravityState",  # 2004[10]
    "EnableGravity",
    "DisableGravity",
    "SetCharacterEventTarget",  # 2004[11]
    "SetImmortalityState",  # 2004[12]
    "EnableImmortality",
    "DisableImmortality",
    "SetNest",  # 2004[13]
    "RotateToFaceEntity",  # 2004[14]
    "SetInvincibilityState",  # 2004[15]
    "EnableInvincibility",
    "DisableInvincibility",
    "ClearTargetList",  # 2004[16]
    "AICommand",  # 2004[17]
    "SetEventPoint",  # 2004[18]
    "SetAIParamID",  # 2004[19]
    "ReplanAI",  # 2004[20]
    "CancelSpecialEffect",  # 2004[21]
    "CreateNPCPart",  # 2004[22]
    "SetNPCPartHealth",  # 2004[23]
    "SetNPCPartEffects",  # 2004[24]
    "SetNPCPartBulletDamageScaling",  # 2004[25]
    "SetDisplayMask",  # 2004[26]
    "SetCollisionMask",  # 2004[27]
    "SetNetworkUpdateAuthority",  # 2004[28]
    "SetBackreadState",  # 2004[29]
    "EnableBackread",
    "DisableBackread",
    "SetHealthBarState",  # 2004[30]
    "EnableHealthBar",
    "DisableHealthBar",
    "SetCharacterCollisionState",  # 2004[31]
    "EnableCharacterCollision",
    "DisableCharacterCollision",
    "AIEvent",  # 2004[32]
    "ReferDamageToEntity",  # 2004[33]
    "SetNetworkUpdateRate",  # 2004[34]
    "SetBackreadStateAlternate",  # 2004[35]
    "HellkiteBreathControl",  # 2004[36]
    "DropMandatoryTreasure",  # 2004[37]
    "BetrayCurrentCovenant",  # 2004[38]
    "SetAnimationsState",  # 2004[39]
    "EnableAnimations",
    "DisableAnimations",
    "MoveAndSetDrawParent",  # 2004[40]
    "ShortMove",  # 2004[41]
    "MoveAndCopyDrawParent",  # 2004[42]
    "ResetAnimation",  # 2004[43]
    "SetTeamTypeAndExitStandbyAnimation",  # 2004[44]
    "HumanityRegistration",  # 2004[45]
    "IncrementPvPSin",  # 2004[46]
    "EqualRecovery",  # 2004[47]
    "DestroyObject",  # 2005[1]
    "RestoreObject",  # 2005[2]
    "SetObjectState",  # 2005[3]
    "EnableObject",
    "DisableObject",
    "SetTreasureState",  # 2005[4]
    "EnableTreasure",
    "DisableTreasure",
    "ActivateObject",  # 2005[5]
    "SetObjectActivation",  # 2005[6]
    "EndOfAnimation",  # 2005[7]
    "PostDestruction",  # 2005[8]
    "CreateHazard",  # 2005[9]
    "RegisterStatue",  # 2005[10]
    "MoveObjectToCharacter",  # 2005[11]
    "RemoveObjectFlag",  # 2005[12]
    "SetObjectInvulnerabilityState",  # 2005[13]
    "EnableObjectInvulnerability",
    "DisableObjectInvulnerability",
    "SetObjectActivationWithIdx",  # 2005[14]
    "EnableTreasureCollection",  # 2005[15]
    "DeleteVFX",  # 2006[1]
    "CreateVFX",  # 2006[2]
    "CreateTemporaryVFX",  # 2006[3]
    "CreateObjectVFX",  # 2006[4]
    "DeleteObjectVFX",  # 2006[5]
    "DisplayDialog",  # 2007[1]
    "DisplayBanner",  # 2007[2]
    "DisplayStatus",  # 2007[3]
    "DisplayBattlefieldMessage",  # 2007[4]
    "ArenaSetNametag1",  # 2007[5]
    "ArenaSetNametag2",  # 2007[6]
    "ArenaSetNametag3",  # 2007[7]
    "ArenaSetNametag4",  # 2007[8]
    "DisplayArenaDissolutionMessage",  # 2007[9]
    "ChangeCamera",  # 2008[1]
    "SetCameraVibration",  # 2008[2]
    "SetLockedCameraSlot",  # 2008[3]
    "RegisterLadder",  # 2009[0]
    "InitializeWanderingDemon",  # 2009[1]
    "RegisterWanderingDemon",  # 2009[2]
    "RegisterBonfire",  # 2009[3]
    "ActivateMultiplayerBuffs",  # 2009[4]
    "RegisterHealingFountain",  # 2009[5]
    "NotifyBossBattleStart",  # 2009[6]
    "SetBackgroundMusic",  # 2010[1]
    "PlaySoundEffect",  # 2010[2]
    "SetSoundEventState",  # 2010[3]
    "EnableSoundEvent",
    "DisableSoundEvent",
    "SetMapCollisionState",  # 2011[1]
    "EnableMapCollision",
    "DisableMapCollision",
    "SetMapCollisionBackreadMaskState",  # 2011[2]
    "EnableMapCollisionBackreadMask",
    "DisableMapCollisionBackreadMask",
    "SetMapPieceState",  # 2012[1]
    "EnableMapPiece",
    "DisableMapPiece",
    "IfAttackedWithDamageType",  # 3[23]
    "IfActionButtonParamActivated",  # 3[24]
    "IfPlayerOwnWorldState",  # 3[26]
    "IfPlayerInOwnWorld",
    "IfPlayerNotInOwnWorld",
    "IfMapCeremonyState",  # 3[28]
    "IfMapInCeremony",
    "IfMapNotInCeremony",
    "IfMultiplayerNetworkPenalized",  # 3[29]
    "IfPlayerGender",  # 3[30]
    "IfOngoingCutsceneFinished",  # 3[31]
    "IfHollowArenaMatchReadyState",  # 3[32]
    "IfHollowArenaSoloResults",  # 3[33]
    "IfHollowArenaSoloScoreComparison",  # 3[34]
    "IfHollowArenaTeamResults",  # 3[35]
    "IfSteamDisconnected",  # 3[38]
    "IfAllyPhantomCountComparison",  # 3[39]
    "IfCharacterDrawGroupState",  # 4[15]
    "IfCharacterDrawGroupEnabled",
    "IfCharacterDrawGroupDisabled",
    "IfPlayerRemainingYoelLevelComparison",  # 4[26]
    "IfCharacterInvadeType",  # 4[27]
    "IfCharacterChameleonState",  # 4[28]
    "IfObjectBurnState",  # 5[9]
    "IfObjectBackreadState",  # 5[10]
    "IfObjectBackreadEnabled",
    "IfObjectBackreadDisabled",
    "IfObjectBackreadState_Alternate",  # 5[11]
    "GotoIfConditionState",  # 1000[101]
    "GotoIfConditionTrue",
    "GotoIfConditionFalse",
    "Goto",  # 1000[103]
    "GotoIfValueComparison",  # 1000[105]
    "GotoIfFinishedConditionState",  # 1000[107]
    "GotoIfFinishedConditionTrue",
    "GotoIfFinishedConditionFalse",
    "WaitHollowArenaHalftime",  # 1001[4]
    "SkipLinesIfMultiplayerState",  # 1003[5]
    "SkipLinesIfHost",
    "SkipLinesIfClient",
    "SkipLinesIfTryingToCreateSession",
    "SkipLinesIfTryingToJoinSession",
    "SkipLinesIfLeavingSession",
    "SkipLinesIfFailedToCreateSession",
    "ReturnIfMultiplayerState",  # 1003[6]
    "EndIfHost",
    "EndIfClient",
    "EndIfTryingToCreateSession",
    "EndIfTryingToJoinSession",
    "EndIfLeavingSession",
    "EndIfFailedToCreateSession",
    "RestartIfHost",
    "RestartIfClient",
    "RestartIfTryingToCreateSession",
    "RestartIfTryingToJoinSession",
    "RestartIfLeavingSession",
    "RestartIfFailedToCreateSession",
    "SkipLinesIfCoopClientCountComparison",  # 1003[9]
    "ReturnIfCoopClientCountComparison",  # 1003[10]
    "EndIfCoopClientCountComparison",
    "RestartIfCoopClientCountComparison",
    "GotoIfCharacterSpecialEffectState",  # 1003[11]
    "GotoIfPlayerHasSpecialEffect",
    "GotoIfPlayerDoesNotHaveSpecialEffect",
    "GotoIfCharacterHasSpecialEffect",
    "GotoIfCharacterDoesNotHaveSpecialEffect",
    "GotoIfPlayerOwnWorldState",  # 1003[12]
    "GotoIfPlayerInOwnWorld",
    "GotoIfPlayerNotInOwnWorld",
    "ReturnIfPlayerOwnWorldState",  # 1003[13]
    "EndIfPlayerInOwnWorld",
    "EndIfPlayerNotInOwnWorld",
    "RestartIfPlayerInOwnWorld",
    "RestartIfPlayerNotInOwnWorld",
    "SkipLinesIfClientTypeCountComparison",  # 1003[14]
    "GotoIfClientTypeCountComparison",  # 1003[15]
    "ReturnIfClientTypeCountComparison",  # 1003[16]
    "EndIfClientTypeCountComparison",
    "RestartIfClientTypeCountComparison",
    "GotoIfFlagState",  # 1003[101]
    "GotoIfThisEventFlagEnabled",
    "GotoIfThisEventFlagDisabled",
    "GotoIfThisEventSlotFlagEnabled",
    "GotoIfThisEventSlotFlagDisabled",
    "GotoIfFlagEnabled",
    "GotoIfFlagDisabled",
    "GotoIfFlagRangeState",  # 1003[103]
    "GotoIfFlagRangeAllEnabled",
    "GotoIfFlagRangeAllDisabled",
    "GotoIfFlagRangeAnyEnabled",
    "GotoIfFlagRangeAnyDisabled",
    "GotoIfMultiplayerState",  # 1003[105]
    "GotoIfHost",
    "GotoIfClient",
    "GotoIfTryingToCreateSession",
    "GotoIfTryingToJoinSession",
    "GotoIfLeavingSession",
    "GotoIfFailedToCreateSession",
    "GotoIfMapPresenceState",  # 1003[107]
    "GotoIfInsideMap",
    "GotoIfOutsideMap",
    "GotoIfCoopClientCountComparison",  # 1003[109]
    "ReturnIfCharacterSpecialEffectState",  # 1003[111]
    "EndIfPlayerHasSpecialEffect",
    "EndIfPlayerDoesNotHaveSpecialEffect",
    "RestartIfPlayerHasSpecialEffect",
    "RestartIfPlayerDoesNotHaveSpecialEffect",
    "EndIfCharacterHasSpecialEffect",
    "EndIfCharacterDoesNotHaveSpecialEffect",
    "RestartIfCharacterHasSpecialEffect",
    "RestartIfCharacterDoesNotHaveSpecialEffect",
    "SkipLinesIfCharacterSpecialEffectState",  # 1003[112]
    "SkipLinesIfPlayerHasSpecialEffect",
    "SkipLinesIfPlayerDoesNotHaveSpecialEffect",
    "SkipLinesIfCharacterHasSpecialEffect",
    "SkipLinesIfCharacterDoesNotHaveSpecialEffect",
    "GotoIfCharacterRegionState",  # 1003[200]
    "GotoIfPlayerInsideRegion",
    "GotoIfPlayerOutsideRegion",
    "GotoIfCharacterInsideRegion",
    "GotoIfCharacterOutsideRegion",
    "ReturnIfCharacterRegionState",  # 1003[201]
    "EndIfPlayerInsideRegion",
    "EndIfPlayerOutsideRegion",
    "RestartIfPlayerInsideRegion",
    "RestartIfPlayerOutsideRegion",
    "EndIfCharacterInsideRegion",
    "EndIfCharacterOutsideRegion",
    "RestartIfCharacterInsideRegion",
    "RestartIfCharacterOutsideRegion",
    "SkipLinesIfCharacterRegionState",  # 1003[202]
    "SkipLinesIfPlayerInsideRegion",
    "SkipLinesIfPlayerOutsideRegion",
    "SkipLinesIfCharacterInsideRegion",
    "SkipLinesIfCharacterOutsideRegion",
    "GotoIfHollowArenaMatchType",  # 1003[211]
    "GotoIfObjectDestructionState",  # 1005[101]
    "GotoIfObjectDestroyed",
    "GotoIfObjectNotDestroyed",
    "DefineLabel_0",  # 1014[0]
    "DefineLabel_1",  # 1014[1]
    "DefineLabel_2",  # 1014[2]
    "DefineLabel_3",  # 1014[3]
    "DefineLabel_4",  # 1014[4]
    "DefineLabel_5",  # 1014[5]
    "DefineLabel_6",  # 1014[6]
    "DefineLabel_7",  # 1014[7]
    "DefineLabel_8",  # 1014[8]
    "DefineLabel_9",  # 1014[9]
    "DefineLabel_10",  # 1014[10]
    "DefineLabel_11",  # 1014[11]
    "DefineLabel_12",  # 1014[12]
    "DefineLabel_13",  # 1014[13]
    "DefineLabel_14",  # 1014[14]
    "DefineLabel_15",  # 1014[15]
    "DefineLabel_16",  # 1014[16]
    "DefineLabel_17",  # 1014[17]
    "DefineLabel_18",  # 1014[18]
    "DefineLabel_19",  # 1014[19]
    "DefineLabel_20",  # 1014[20]
    "PlayCutsceneAndMovePlayerAndSetTimePeriod",  # 2002[6]
    "PlayCutsceneAndSetTimePeriod",  # 2002[7]
    "PlayCutsceneAndMovePlayer_Dummy",  # 2002[8]
    "PlayCutsceneAndMovePlayerAndSetMapCeremony",  # 2002[9]
    "PlayCutsceneAndSetMapCeremony",  # 2002[10]
    "PlayCutsceneAndMoveSpecificPlayer_WithUnknowns",  # 2002[11]
    "PlayCutsceneAndMoveSpecificPlayer_WithOtherRegion",  # 2002[12]
    "Unknown_2003_27",  # 2003[27]
    "StoreItemAmountSpecifiedByFlagValue",  # 2003[42]
    "GivePlayerItemAmountSpecifiedByFlagValue",  # 2003[43]
    "SetDirectionDisplayState",  # 2003[44]
    "EnableDirectionDisplayState",
    "DisableDirectionDisplayState",
    "SetMapHitGridCorrespondence",  # 2003[45]
    "EnableMapHitGridCorrespondence",
    "DisableMapHitGridCorrespondence",
    "SetMapContentImageDisplayState",  # 2003[46]
    "SetMapBoundariesDisplay",  # 2003[47]
    "SetAreaWind",  # 2003[48]
    "WarpPlayerToRespawnPoint",  # 2003[49]
    "StartEnemySpawner",  # 2003[50]
    "SummonNPC",  # 2003[51]
    "InitializeWarpObject",  # 2003[52]
    "MakeEnemyAppear",  # 2003[54]
    "SetCurrentMapCeremony",  # 2003[57]
    "SetMapCeremony",  # 2003[59]
    "DisplayEpitaphMessage",  # 2003[61]
    "SetNetworkConnectedFlagState",  # 2003[62]
    "SetNetworkConnectedFlagRangeState",  # 2003[63]
    "EnableNetworkConnectedFlagRange",
    "DisableNetworkConnectedFlagRange",
    "ToggleNetworkConnectedFlagRange",
    "SetOmissionModeCounts",  # 2003[64]
    "ResetOmissionModeCountsToDefault",  # 2003[65]
    "InitializeCrowTrade",  # 2003[66]
    "InitializeCrowTradeRegion",  # 2003[67]
    "SetNetworkInteractionState",  # 2003[70]
    "SetHUDVisibilityState",  # 2003[71]
    "EnableHUDVisibility",
    "DisableHUDVisibility",
    "SetBonfireWarpingState",  # 2003[72]
    "EnableBonfireWarping",
    "DisableBonfireWarping",
    "SetAutogeneratedEventSpecificFlag_1",  # 2003[73]
    "HandleBossDefeatAndDisplayBanner",  # 2003[74]
    "SetAutogeneratedEventSpecificFlag_2",  # 2003[75]
    "SetLoadingScreenTipsState",  # 2003[76]
    "EnableLoadingScreenTips",
    "DisableLoadingScreenTips",
    "AwardGestureItem",  # 2003[77]
    "SendNPCSummonHome",  # 2003[78]
    "Unknown_2003_79",  # 2003[79]
    "SetDecoratedBossHealthBarState",  # 2003[80]
    "PlaceNPCSummonSign_WithoutEmber",  # 2003[81]
    "ChangeCharacterCloth",  # 2004[48]
    "ChangePatrolBehavior",  # 2004[49]
    "SetLockOnPoint",  # 2004[50]
    "Test_RequestRagdollRestraint",  # 2004[51]
    "ChangePlayerCharacterInitParam",  # 2004[52]
    "AdaptSpecialEffectHealthChangeToNPCPart",  # 2004[53]
    "ImmediateActivate",  # 2004[54]
    "SetCharacterTalkRange",  # 2004[55]
    "IncrementCharacterNewGameCycle",  # 2004[57]
    "SetMultiplayerBuffs_NonBoss",  # 2004[58]
    "Unknown_2004_59",  # 2004[59]
    "SetPlayerRemainingYoelLevels",  # 2004[60]
    "ExtinguishBurningObjects",  # 2005[16]
    "ShowObjectByMapCeremony",  # 2005[17]
    "DestroyObject_NoSlot",  # 2005[19]
    "DisplayDialogAndSetFlags",  # 2007[10]
    "DisplayAreaWelcomeMessage",  # 2007[11]
    "DisplayHollowArenaMessage",  # 2007[12]
    "BanishInvaders",  # 2009[8]
    "BanishPhantomsAndUpdateServerPvPStats",  # 2009[10]
    "BanishPhantoms",  # 2009[11]
    "SetBossMusicState",  # 2010[4]
    "EnableBossMusic",
    "DisableBossMusic",
    "NotifyDoorEventSoundDampening",  # 2010[5]
    "SetSoundEventWithFade",  # 2010[6]
    "EnableSoundEventWithFade",
    "DisableSoundEventWithFade",
    "Unknown_2010_07",  # 2010[7]
    "SetCollisionResState",  # 2011[3]
    "ActivateCollisionAndCreateNavmesh",  # 2011[4]
    "SetAreaWelcomeMessageState",  # 2012[8]
    "CreatePlayLog",  # 2013[1]
    "StartPlayLogMeasurement",  # 2013[2]
    "StopPlayLogMeasurement",  # 2013[3]
    "PlayLogParameterOutput",  # 2013[4]
    "EnableThisFlag",
    "DisableThisFlag",

    # From `compiler`:
    "compile_game_object_test",
    "RunEvent",
    "EnableObjectActivation",
    "DisableObjectActivation",
    "AwardItemLot",
    "PlayCutscene",
    "Move",
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
    "IfActionButton",
    "DefineLabel",
]

from soulstruct.darksouls3.game_types import *
from .emevd.compiler import *
from .emevd.enums import *


def IfConditionState(condition: int, state: bool | int, input_condition: int):
    """
    TODO
    """


def IfConditionTrue(condition: int, input_condition: int):
    """
    Calls `IfConditionState` with `state=True`.
    """


def IfConditionFalse(condition: int, input_condition: int):
    """
    Calls `IfConditionState` with `state=False`.
    """


def IfValueComparison(condition: int, comparison_type: ComparisonType | int, left: int, right: int):
    """
    TODO
    """


def IfValueEqual(condition: int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=0`.
    """


def IfValueNotEqual(condition: int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=1`.
    """


def IfValueGreaterThan(condition: int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=2`.
    """


def IfValueLessThan(condition: int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=3`.
    """


def IfValueGreaterThanOrEqual(condition: int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=4`.
    """


def IfValueLessThanOrEqual(condition: int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=5`.
    """


def IfTimeElapsed(condition: int, seconds: float):
    """
    Time since event started.
    """


def IfFramesElapsed(condition: int, frames: int):
    """
    Frames since event started.
    """


def IfRandomTimeElapsed(condition: int, min_seconds: float, max_seconds: float):
    """
    Not used in vanilla DS1. Requires a random amount of time since event began.
    """


def IfRandomFramesElapsed(condition: int, min_frames: int, max_frames: int):
    """
    Not used in vanilla DS1. Requires a random amount of frames since event began.
    """


def IfFlagState(condition: int, state: FlagState | int, flag_type: FlagType | int, flag: Flag | int):
    """
    TODO
    """


def IfFlagEnabled(condition: int, flag: Flag | int):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=0`.
    """


def IfFlagDisabled(condition: int, flag: Flag | int):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=0`.
    """


def IfThisEventFlagEnabled(condition: int):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


def IfThisEventFlagDisabled(condition: int):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


def IfThisEventSlotFlagEnabled(condition: int):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


def IfThisEventSlotFlagDisabled(condition: int):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


def IfFlagRangeState(
    condition: int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
):
    """
    TODO
    """


def IfFlagRangeAllEnabled(condition: int, flag_range: FlagRange | tuple | list):
    """
    Calls `IfFlagRangeState` with `state=0`, `flag_type=0`.
    """


def IfFlagRangeAllDisabled(condition: int, flag_range: FlagRange | tuple | list):
    """
    Calls `IfFlagRangeState` with `state=1`, `flag_type=0`.
    """


def IfFlagRangeAnyEnabled(condition: int, flag_range: FlagRange | tuple | list):
    """
    Calls `IfFlagRangeState` with `state=2`, `flag_type=0`.
    """


def IfFlagRangeAnyDisabled(condition: int, flag_range: FlagRange | tuple | list):
    """
    Calls `IfFlagRangeState` with `state=3`, `flag_type=0`.
    """


def IfCharacterRegionState(
    condition: int,
    state: bool | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    New argument with unknown purpose. Always 1 in vanilla resources. Probably for debug.
    """


def IfPlayerInsideRegion(condition: int, region: Region | int, min_target_count: int = 1):
    """
    Calls `IfCharacterRegionState` with `state=True`, `character=10000`.
    """


def IfPlayerOutsideRegion(condition: int, region: Region | int, min_target_count: int = 1):
    """
    Calls `IfCharacterRegionState` with `state=False`, `character=10000`.
    """


def IfCharacterInsideRegion(
    condition: int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    Calls `IfCharacterRegionState` with `state=True`.
    """


def IfCharacterOutsideRegion(
    condition: int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    Calls `IfCharacterRegionState` with `state=False`.
    """


def IfEntityDistanceState(
    condition: int,
    state: bool | int,
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
):
    """
    Same new argument as region test, with unknown purpose, and again always 1 in EMEVD resources.
    """


def IfPlayerWithinDistance(
    condition: int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
):
    """
    Calls `IfEntityDistanceState` with `state=True`, `entity=10000`.
    """


def IfPlayerBeyondDistance(
    condition: int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
):
    """
    Calls `IfEntityDistanceState` with `state=False`, `entity=10000`.
    """


def IfEntityWithinDistance(
    condition: int,
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
):
    """
    Calls `IfEntityDistanceState` with `state=True`.
    """


def IfEntityBeyondDistance(
    condition: int,
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
):
    """
    Calls `IfEntityDistanceState` with `state=False`.
    """


def IfPlayerItemStateExcludingStorage(
    condition: int,
    item: BaseItemParam | int,
    state: bool | int,
    item_type: ItemType | int = None,
):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


def IfActionButtonBasic(
    condition: int,
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = TriggerAttribute.Human_or_Hollow,
    button: int = 0,
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Basic (not "boss") version with no line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def IfMultiplayerState(condition: int, state: MultiplayerState | int):
    """
    TODO
    """


def IfHost(condition: int):
    """
    Calls `IfMultiplayerState` with `state=0`.
    """


def IfClient(condition: int):
    """
    Calls `IfMultiplayerState` with `state=1`.
    """


def IfTryingToCreateSession(condition: int):
    """
    Calls `IfMultiplayerState` with `state=2`.
    """


def IfTryingToJoinSession(condition: int):
    """
    Calls `IfMultiplayerState` with `state=3`.
    """


def IfLeavingSession(condition: int):
    """
    Calls `IfMultiplayerState` with `state=4`.
    """


def IfFailedToCreateSession(condition: int):
    """
    Calls `IfMultiplayerState` with `state=5`.
    """


def IfAllPlayersRegionState(condition: int, state: bool | int, region: Region | int):
    """
    TODO
    """


def IfAllPlayersInsideRegion(condition: int, region: Region | int):
    """
    Calls `IfAllPlayersRegionState` with `state=True`.
    """


def IfAllPlayersOutsideRegion(condition: int, region: Region | int):
    """
    Calls `IfAllPlayersRegionState` with `state=False`.
    """


def IfMapPresenceState(condition: int, state: bool | int, game_map: Map | tuple | list):
    """
    Conditions upon player's presence in a particular game map.
    """


def IfInsideMap(condition: int, game_map: Map | tuple | list):
    """
    Calls `IfMapPresenceState` with `state=True`.
    """


def IfOutsideMap(condition: int, game_map: Map | tuple | list):
    """
    Calls `IfMapPresenceState` with `state=False`.
    """


def IfMultiplayerEvent(condition: int, event_id: int):
    """
    TODO
    """


def IfTrueFlagCountComparison(
    condition: int,
    flag_type: FlagType | int,
    comparison_type: ComparisonType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Conditions upon a comparison with the number of enabled flags in the given range (inclusive).
    """


def IfTrueFlagCountEqual(condition: int, flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=0`.
    """


def IfTrueFlagCountNotEqual(
    condition: int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=1`.
    """


def IfTrueFlagCountGreaterThan(
    condition: int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=2`.
    """


def IfTrueFlagCountLessThan(
    condition: int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=3`.
    """


def IfTrueFlagCountGreaterThanOrEqual(
    condition: int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=4`.
    """


def IfTrueFlagCountLessThanOrEqual(
    condition: int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=5`.
    """


def IfWorldTendencyComparison(
    condition: int,
    world_tendency_type: WorldTendencyType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    TODO
    """


def IfWhiteWorldTendencyComparison(condition: int, comparison_type: ComparisonType | int, value: int):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=0`.
    """


def IfBlackWorldTendencyComparison(condition: int, comparison_type: ComparisonType | int, value: int):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=1`.
    """


def IfWhiteWorldTendencyGreaterThanOrEqual(condition: int, value: int):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=0`, `comparison_type=4`.
    """


def IfBlackWorldTendencyGreaterThanOrEqual(condition: int, value: int):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=1`, `comparison_type=4`.
    """


def IfEventValueComparison(
    condition: int,
    flag: Flag | int,
    bit_count: int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    TODO
    """


def IfEventValueEqual(condition: int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=0`.
    """


def IfEventValueNotEqual(condition: int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=1`.
    """


def IfEventValueGreaterThan(condition: int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=2`.
    """


def IfEventValueLessThan(condition: int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=3`.
    """


def IfEventValueGreaterThanOrEqual(condition: int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=4`.
    """


def IfEventValueLessThanOrEqual(condition: int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=5`.
    """


def IfActionButtonBoss(
    condition: int,
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = TriggerAttribute.Human_or_Hollow,
    button: int = 0,
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Boss (not "basic") version with no line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def IfAnyItemDroppedInRegion(condition: int, region: Region | int):
    """
    Check if any item has been dropped in the specified region. Not sensitive to what the item is.
    """


def IfItemDropped(condition: int, item: BaseItemParam | int, item_type: ItemType | int = None):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


def IfPlayerItemStateIncludingStorage(
    condition: int,
    item: BaseItemParam | int,
    state: bool | int,
    item_type: ItemType | int = None,
):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


def IfNewGameCycleComparison(condition: int, comparison_type: ComparisonType | int, completion_count: int):
    """
    TODO
    """


def IfNewGameCycleEqual(condition: int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=0`.
    """


def IfNewGameCycleNotEqual(condition: int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=1`.
    """


def IfNewGameCycleGreaterThan(condition: int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=2`.
    """


def IfNewGameCycleLessThan(condition: int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=3`.
    """


def IfNewGameCycleGreaterThanOrEqual(condition: int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=4`.
    """


def IfNewGameCycleLessThanOrEqual(condition: int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=5`.
    """


def IfActionButtonBasicLineIntersect(
    condition: int,
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = TriggerAttribute.Human_or_Hollow,
    button: int = 0,
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Basic (not "boss") version with a line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def IfActionButtonBossLineIntersect(
    condition: int,
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = TriggerAttribute.Human_or_Hollow,
    button: int = 0,
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Boss (not "basic") version with a line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def IfEventsComparison(
    condition: int,
    left_flag: Flag | int,
    left_bit_count: int,
    comparison_type: ComparisonType | int,
    right_flag: Flag | int,
    right_bit_count: int,
):
    """
    Check comparison of two event flag values. Haven't bothered adding shortcut functions for this.
    """


def IfDLCState(condition: int, is_owned: bool | int):
    """
    TODO
    """


def IfDLCOwned(condition: int):
    """
    Calls `IfDLCState` with `is_owned=True`.
    """


def IfDLCNotOwned(condition: int):
    """
    Calls `IfDLCState` with `is_owned=False`.
    """


def IfOnlineState(condition: int, state: bool | int):
    """
    TODO
    """


def IfOnline(condition: int):
    """
    Calls `IfOnlineState` with `state=True`.
    """


def IfOffline(condition: int):
    """
    Calls `IfOnlineState` with `state=False`.
    """


def IfCharacterDeathState(
    condition: int,
    character: Character | int,
    is_dead: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def IfCharacterDead(
    condition: int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterDeathState` with `is_dead=True`.
    """


def IfCharacterAlive(
    condition: int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterDeathState` with `is_dead=False`.
    """


def IfAttacked(condition: int, attacked_entity: Character | int, attacker: Character | int):
    """
    TODO
    """


def IfHealthComparison(
    condition: int,
    character: Character | int,
    comparison_type: ComparisonType | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Conditions upon a comparison to character health ratio (0-1).
    """


def IfHealthEqual(
    condition: int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthComparison` with `comparison_type=0`.
    """


def IfHealthNotEqual(
    condition: int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthComparison` with `comparison_type=1`.
    """


def IfHealthGreaterThan(
    condition: int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthComparison` with `comparison_type=2`.
    """


def IfHealthLessThan(
    condition: int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthComparison` with `comparison_type=3`.
    """


def IfHealthGreaterThanOrEqual(
    condition: int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthComparison` with `comparison_type=4`.
    """


def IfHealthLessThanOrEqual(
    condition: int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthComparison` with `comparison_type=5`.
    """


def IfCharacterType(
    condition: int,
    character: Character | int,
    character_type: CharacterType | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def IfCharacterHuman(
    condition: int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterType` with `character_type=0`.
    """


def IfCharacterWhitePhantom(
    condition: int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterType` with `character_type=1`.
    """


def IfCharacterHollow(
    condition: int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterType` with `character_type=8`.
    """


def IfCharacterTargetingState(
    condition: int,
    targeting_character: Character | int,
    targeted_character: Character | int,
    state: bool | int,
):
    """
    TODO
    """


def IfCharacterTargeting(condition: int, targeting_character: Character | int, targeted_character: Character | int):
    """
    Calls `IfCharacterTargetingState` with `state=True`.
    """


def IfCharacterNotTargeting(condition: int, targeting_character: Character | int, targeted_character: Character | int):
    """
    Calls `IfCharacterTargetingState` with `state=False`.
    """


def IfCharacterSpecialEffectState(
    condition: int,
    character: Character | int,
    special_effect: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def IfPlayerHasSpecialEffect(
    condition: int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterSpecialEffectState` with `character=10000`, `state=True`.
    """


def IfPlayerDoesNotHaveSpecialEffect(
    condition: int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterSpecialEffectState` with `character=10000`, `state=False`.
    """


def IfCharacterHasSpecialEffect(
    condition: int,
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterSpecialEffectState` with `state=True`.
    """


def IfCharacterDoesNotHaveSpecialEffect(
    condition: int,
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterSpecialEffectState` with `state=False`.
    """


def IfCharacterPartHealthComparison(
    condition: int,
    character: Character | int,
    npc_part_id: int,
    value: float,
    comparison_type: ComparisonType | int,
):
    """
    TODO
    """


def IfCharacterPartHealthLessThanOrEqual(condition: int, character: Character | int, npc_part_id: int, value: float):
    """
    Calls `IfCharacterPartHealthComparison` with `comparison_type=5`.
    """


def IfCharacterBackreadState(
    condition: int,
    character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def IfCharacterBackreadEnabled(
    condition: int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterBackreadState` with `state=True`.
    """


def IfCharacterBackreadDisabled(
    condition: int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterBackreadState` with `state=False`.
    """


def IfCharacterTAEEventState(
    condition: int,
    character: Character | int,
    tae_event_id: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def IfCharacterHasTAEEvent(
    condition: int,
    character: Character | int,
    tae_event_id: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterTAEEventState` with `state=True`.
    """


def IfCharacterDoesNotHaveTAEEvent(
    condition: int,
    character: Character | int,
    tae_event_id: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterTAEEventState` with `state=False`.
    """


def IfHasAIStatus(
    condition: int,
    character: Character | int,
    ai_status: AIStatusType | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def IfSkullLanternState(condition: int, state: bool | int):
    """
    TODO
    """


def IfSkullLanternActive(condition: int):
    """
    Calls `IfSkullLanternState` with `state=True`.
    """


def IfSkullLanternInactive(condition: int):
    """
    Calls `IfSkullLanternState` with `state=False`.
    """


def IfPlayerClass(condition: int, class_type: ClassType | int):
    """
    TODO
    """


def IfPlayerCovenant(condition: int, covenant: Covenant | int):
    """
    TODO
    """


def IfPlayerLevelComparison(condition: int, comparison_type: ComparisonType | int, value: int):
    """
    TODO
    """


def IfPlayerLevelEqual(condition: int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=0`.
    """


def IfPlayerLevelNotEqual(condition: int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=1`.
    """


def IfPlayerLevelGreaterThan(condition: int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=2`.
    """


def IfPlayerLevelLessThan(condition: int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=3`.
    """


def IfPlayerLevelGreaterThanOrEqual(condition: int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=4`.
    """


def IfPlayerLevelLessThanOrEqual(condition: int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=5`.
    """


def IfHealthValueComparison(
    condition: int,
    character: Character | int,
    comparison_type: ComparisonType | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def IfHealthValueEqual(
    condition: int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=0`.
    """


def IfHealthValueNotEqual(
    condition: int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=1`.
    """


def IfHealthValueGreaterThan(
    condition: int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=2`.
    """


def IfHealthValueLessThan(
    condition: int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=3`.
    """


def IfHealthValueGreaterThanOrEqual(
    condition: int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=4`.
    """


def IfHealthValueLessThanOrEqual(
    condition: int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=5`.
    """


def IfObjectDestructionState(
    condition: int,
    state: bool | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def IfObjectDestroyed(
    condition: int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfObjectDestructionState` with `state=True`.
    """


def IfObjectNotDestroyed(
    condition: int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfObjectDestructionState` with `state=False`.
    """


def IfObjectDamaged(condition: int, obj: Object | int, attacker: Character | int):
    """
    TODO
    """


def IfObjectActivated(condition: int, obj_act_id: int):
    """
    TODO
    """


def IfObjectHealthValueComparison(condition: int, obj: Object | int, comparison_type: ComparisonType | int, value: int):
    """
    TODO
    """


def IfPlayerMovingOnCollision(condition: int, collision: Collision | int):
    """
    TODO
    """


def IfPlayerRunningOnCollision(condition: int, collision: Collision | int):
    """
    TODO
    """


def IfPlayerStandingOnCollision(condition: int, collision: Collision | int):
    """
    TODO
    """


def AwaitConditionState(state: bool | int, condition: int):
    """
    Not sure if this is ever really used over `IfConditionState`.
    """


def AwaitConditionTrue(condition: int):
    """
    Calls `AwaitConditionState` with `state=True`.
    """


def AwaitConditionFalse(condition: int):
    """
    Calls `AwaitConditionState` with `state=False`.
    """


def SkipLinesIfConditionState(line_count: int, state: bool | int, condition: int):
    """
    TODO
    """


def SkipLinesIfConditionTrue(line_count: int, condition: int):
    """
    Calls `SkipLinesIfConditionState` with `state=True`.
    """


def SkipLinesIfConditionFalse(line_count: int, condition: int):
    """
    Calls `SkipLinesIfConditionState` with `state=False`.
    """


def ReturnIfConditionState(event_return_type: EventReturnType | int, state: bool | int, input_condition: int):
    """
    TODO
    """


def EndIfConditionTrue(input_condition: int):
    """
    Calls `ReturnIfConditionState` with `event_return_type=0`, `state=True`.
    """


def EndIfConditionFalse(input_condition: int):
    """
    Calls `ReturnIfConditionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfConditionTrue(input_condition: int):
    """
    Calls `ReturnIfConditionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfConditionFalse(input_condition: int):
    """
    Calls `ReturnIfConditionState` with `event_return_type=1`, `state=False`.
    """


def SkipLines(line_count: int):
    """
    Unconditional line skip.
    """


def Return(event_return_type: EventReturnType | int):
    """
    TODO
    """


def End():
    """
    Calls `Return` with `event_return_type=0`.
    """


def Restart():
    """
    Calls `Return` with `event_return_type=1`.
    """


def SkipLinesIfComparison(line_count: int, comparison_type: ComparisonType | int, left: int, right: int):
    """
    TODO
    """


def SkipLinesIfEqual(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfComparison` with `comparison_type=0`.
    """


def SkipLinesIfNotEqual(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfComparison` with `comparison_type=1`.
    """


def SkipLinesIfGreaterThan(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfComparison` with `comparison_type=2`.
    """


def SkipLinesIfLessThan(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfComparison` with `comparison_type=3`.
    """


def SkipLinesIfGreaterThanOrEqual(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfComparison` with `comparison_type=4`.
    """


def SkipLinesIfLessThanOrEqual(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfComparison` with `comparison_type=5`.
    """


def ReturnIfComparison(
    event_return_type: EventReturnType | int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
):
    """
    TODO
    """


def EndIfEqual(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=0`, `comparison_type=0`.
    """


def EndIfNotEqual(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=0`, `comparison_type=1`.
    """


def EndIfGreaterThan(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=0`, `comparison_type=2`.
    """


def EndIfLessThan(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=0`, `comparison_type=3`.
    """


def EndIfGreaterThanOrEqual(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=0`, `comparison_type=4`.
    """


def EndIfLessThanOrEqual(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=0`, `comparison_type=5`.
    """


def RestartIfEqual(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=1`, `comparison_type=0`.
    """


def RestartIfNotEqual(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=1`, `comparison_type=1`.
    """


def RestartIfGreaterThan(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=1`, `comparison_type=2`.
    """


def RestartIfLessThan(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=1`, `comparison_type=3`.
    """


def RestartIfGreaterThanOrEqual(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=1`, `comparison_type=4`.
    """


def RestartIfLessThanOrEqual(left: int, right: int):
    """
    Calls `ReturnIfComparison` with `event_return_type=1`, `comparison_type=5`.
    """


def SkipLinesIfFinishedConditionState(line_count: int, state: bool | int, condition: int):
    """
    This command is used instead of 1000[01] when conditions are being checked *after* they have already been
    uploaded into the MAIN condition. For example, you might want to continue MAIN if either AND(01) or AND(02)
    are true, but then afterwards, act conditionally on exactly which one of those two registers caused you to
    continue.
    """


def SkipLinesIfFinishedConditionTrue(line_count: int, condition: int):
    """
    Calls `SkipLinesIfFinishedConditionState` with `state=True`.
    """


def SkipLinesIfFinishedConditionFalse(line_count: int, condition: int):
    """
    Calls `SkipLinesIfFinishedConditionState` with `state=False`.
    """


def ReturnIfFinishedConditionState(event_return_type: EventReturnType | int, state: bool | int, input_condition: int):
    """
    TODO
    """


def EndIfFinishedConditionTrue(input_condition: int):
    """
    Calls `ReturnIfFinishedConditionState` with `event_return_type=0`, `state=True`.
    """


def EndIfFinishedConditionFalse(input_condition: int):
    """
    Calls `ReturnIfFinishedConditionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfFinishedConditionTrue(input_condition: int):
    """
    Calls `ReturnIfFinishedConditionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfFinishedConditionFalse(input_condition: int):
    """
    Calls `ReturnIfFinishedConditionState` with `event_return_type=1`, `state=False`.
    """


def WaitForNetworkApproval(max_seconds: float):
    """
    Wait for network to approve event (up to `max_seconds` seconds).
    """


def Wait(seconds: float):
    """
    Wait for some number of seconds.
    """


def WaitFrames(frames: int):
    """
    Wait for some number of frames.
    """


def WaitRandomSeconds(min_seconds: float, max_seconds: float):
    """
    Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
    """


def WaitRandomFrames(min_frames: int, max_frames: int):
    """
    Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
    """


def AwaitFlagState(state: FlagState | int, flag_type: FlagType | int, flag: Flag | int):
    """
    Not sure if this is really used rather than `IfFlagState` with MAIN condition (0).
    """


def AwaitFlagEnabled(flag: Flag | int):
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=0`.
    """


def AwaitFlagDisabled(flag: Flag | int):
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=0`.
    """


def AwaitThisEventOn():
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


def AwaitThisEventOff():
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


def AwaitThisEventSlotOn():
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


def AwaitThisEventSlotOff():
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


def SkipLinesIfFlagState(line_count: int, state: FlagState | int, flag_type: FlagType | int, flag: Flag | int):
    """
    Skip some number of lines if the specified flag (absolute, event-relative, or slot-relative) has the
    specified state.
    """


def SkipLinesIfFlagEnabled(line_count: int, flag: Flag | int):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=0`.
    """


def SkipLinesIfFlagDisabled(line_count: int, flag: Flag | int):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=0`.
    """


def SkipLinesIfThisEventFlagEnabled(line_count: int):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


def SkipLinesIfThisEventFlagDisabled(line_count: int):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


def SkipLinesIfThisEventSlotFlagEnabled(line_count: int):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


def SkipLinesIfThisEventSlotFlagDisabled(line_count: int):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


def ReturnIfFlagState(
    event_return_type: EventReturnType | int,
    state: FlagState | int,
    flag_type: FlagType | int,
    flag: Flag | int,
):
    """
    TODO
    """


def EndIfFlagEnabled(flag: Flag | int):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=0`.
    """


def EndIfFlagDisabled(flag: Flag | int):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=0`.
    """


def EndIfThisEventFlagEnabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=1`, `flag=0`.
    """


def EndIfThisEventFlagDisabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=1`, `flag=0`.
    """


def EndIfThisEventSlotFlagEnabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=2`, `flag=0`.
    """


def EndIfThisEventSlotFlagDisabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=2`, `flag=0`.
    """


def RestartIfFlagEnabled(flag: Flag | int):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=0`.
    """


def RestartIfFlagDisabled(flag: Flag | int):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=0`.
    """


def RestartIfThisEventFlagEnabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=1`, `flag=0`.
    """


def RestartIfThisEventFlagDisabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=1`, `flag=0`.
    """


def RestartIfThisEventSlotFlagEnabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=2`, `flag=0`.
    """


def RestartIfThisEventSlotFlagDisabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=2`, `flag=0`.
    """


def SkipLinesIfFlagRangeState(
    line_count: int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
):
    """
    TODO
    """


def SkipLinesIfFlagRangeAllEnabled(line_count: int, flag_range: FlagRange | tuple | list):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=0`, `flag_type=0`.
    """


def SkipLinesIfFlagRangeAllDisabled(line_count: int, flag_range: FlagRange | tuple | list):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=1`, `flag_type=0`.
    """


def SkipLinesIfFlagRangeAnyEnabled(line_count: int, flag_range: FlagRange | tuple | list):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=2`, `flag_type=0`.
    """


def SkipLinesIfFlagRangeAnyDisabled(line_count: int, flag_range: FlagRange | tuple | list):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=3`, `flag_type=0`.
    """


def ReturnIfFlagRangeState(
    event_return_type: EventReturnType | int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
):
    """
    TODO
    """


def EndIfFlagRangeAllEnabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=0`, `flag_type=0`.
    """


def EndIfFlagRangeAllDisabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=1`, `flag_type=0`.
    """


def EndIfFlagRangeAnyEnabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=2`, `flag_type=0`.
    """


def EndIfFlagRangeAnyDisabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=3`, `flag_type=0`.
    """


def RestartIfFlagRangeAllEnabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=0`, `flag_type=0`.
    """


def RestartIfFlagRangeAllDisabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=1`, `flag_type=0`.
    """


def RestartIfFlagRangeAnyEnabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=2`, `flag_type=0`.
    """


def RestartIfFlagRangeAnyDisabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=3`, `flag_type=0`.
    """


def SkipLinesIfMapPresenceState(line_count: int, state: bool | int, game_map: Map | tuple | list):
    """
    TODO
    """


def SkipLinesIfInsideMap(line_count: int, game_map: Map | tuple | list):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=True`.
    """


def SkipLinesIfOutsideMap(line_count: int, game_map: Map | tuple | list):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=False`.
    """


def ReturnIfMapPresenceState(event_return_type: EventReturnType | int, state: bool | int, game_map: Map | tuple | list):
    """
    TODO
    """


def EndIfInsideMap(game_map: Map | tuple | list):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=True`.
    """


def EndIfOutsideMap(game_map: Map | tuple | list):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=False`.
    """


def RestartIfInsideMap(game_map: Map | tuple | list):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=True`.
    """


def RestartIfOutsideMap(game_map: Map | tuple | list):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=False`.
    """


def AwaitObjectDestructionState(state: bool | int, obj: Object | int):
    """
    TODO
    """


def AwaitObjectDestroyed(obj: Object | int):
    """
    Calls `AwaitObjectDestructionState` with `state=True`.
    """


def AwaitObjectNotDestroyed(obj: Object | int):
    """
    Calls `AwaitObjectDestructionState` with `state=False`.
    """


def SkipLinesIfObjectDestructionState(
    line_count: int,
    state: bool | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def SkipLinesIfObjectDestroyed(
    line_count: int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `SkipLinesIfObjectDestructionState` with `state=True`.
    """


def SkipLinesIfObjectNotDestroyed(
    line_count: int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `SkipLinesIfObjectDestructionState` with `state=False`.
    """


def ReturnIfObjectDestructionState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def EndIfObjectDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=0`, `state=True`.
    """


def EndIfObjectNotDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfObjectDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfObjectNotDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=1`, `state=False`.
    """


# Instruction `RunEvent` is manually defined in the `compiler` module.


def TerminateEvent(event_slot: int, event_id: int):
    """
    Delete an instance (slot) of an event script.
    """


def SetNetworkSyncState(state: bool | int):
    """
    TODO
    """


def EnableNetworkSync():
    """
    Calls `SetNetworkSyncState` with `state=True`.
    """


def DisableNetworkSync():
    """
    Calls `SetNetworkSyncState` with `state=False`.
    """


def ClearMainCondition(dummy: int = 0):
    """
    Likely clears all conditions currently loaded into the main condition (0).
    """


def IssuePrefetchRequest(request_id: int):
    """
    No idea what this does.
    """


def SaveRequest(dummy: int = 0):
    """
    Request the game to save player progress.
    """


def RunCommonEvent(event_id: int, args: tuple = (0,)):
    """
    Initialize an instance of an event script from `common_func` with the given arguments.
    """


def PlayCutsceneToAll(cutscene_id: int, cutscene_flags: CutsceneFlags | int):
    """
    TODO
    """


def PlayCutsceneAndMovePlayer(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    game_map: Map | tuple | list,
):
    """
    TODO
    """


def PlayCutsceneToPlayer(cutscene_id: int, cutscene_flags: CutsceneFlags | int, player_id: int):
    """
    TODO
    """


def PlayCutsceneAndMoveSpecificPlayer(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    game_map: Map | tuple | list,
    player_id: int,
):
    """
    TODO
    """


def PlayCutsceneAndRotatePlayer(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    relative_rotation_axis_x: float = 0.0,
    relative_rotation_axis_z: float = 0.0,
    rotation: float = 0.0,
    vertical_translation: float = 0.0,
    player_id: int = 10000,
):
    """
    TODO
    """


def RequestAnimation(
    entity: Character | Object | int,
    animation_id: int,
    loop: bool | int = False,
    wait_for_completion: bool | int = False,
):
    """
    Not used very often, in favor of ForceAnimation below.
    """


def SetFlagState(flag: Flag | int, state: FlagState | int):
    """
    Enable, disable, or toggle (change) a binary flag.
    """


def EnableFlag(flag: Flag | int):
    """
    Calls `SetFlagState` with `state=1`.
    """


def DisableFlag(flag: Flag | int):
    """
    Calls `SetFlagState` with `state=0`.
    """


def ToggleFlag(flag: Flag | int):
    """
    Calls `SetFlagState` with `state=2`.
    """


def SetSpawnerState(entity: Object | Region | Character | int, state: bool | int):
    """
    e.g. the baby skeletons in Tomb of the Giants.
    """


def EnableSpawner(entity: Object | Region | Character | int):
    """
    Calls `SetSpawnerState` with `state=True`.
    """


def DisableSpawner(entity: Object | Region | Character | int):
    """
    Calls `SetSpawnerState` with `state=False`.
    """


def AwardItemLotToAllPlayers(item_lot_param_id: int):
    """
    TODO
    """


def ShootProjectile(
    owner_entity: Object | Region | Character | int,
    source_entity: Object | Region | Character | int,
    model_point: int,
    behavior_id: int,
    launch_angle_x: int,
    launch_angle_y: int,
    launch_angle_z: int,
):
    """
    The owner entity sets the 'team' of the projectile (i.e. who it can hurt).
    
    You can use this to directly spawn bullets by setting `source_entity` to `owner_entity`.
    
    Note that the angle arguments are all integers.
    """


def SetEventState(event_id: int, event_return_type: EventReturnType | int, event_slot: int = 0):
    """
    Stop or restart a particular slot (default of 0) of the given event ID. Note that you cannot restart events
    that have already ended.
    """


def StopEvent(event_id: int, event_slot: int = 0):
    """
    Calls `SetEventState` with `event_return_type=0`.
    Force a running event to stop.
    """


def RestartEvent(event_id: int, event_slot: int = 0):
    """
    Calls `SetEventState` with `event_return_type=1`.
    
    Force a running event to restart. Note that the event must be active (i.e. not finished) for this
    to work. If you plan to have an event restarted, make sure it doesn't return until you no longer
    need it.
    """


def SetBossHealthBarState(character: Character | int, state: bool | int, name: NPCName | int = 0, bar_slot: int = 0):
    """
    Note: slot number can be 0-2 in DS3.
    """


def EnableBossHealthBar(character: Character | int, name: NPCName | int = 0, bar_slot: int = 0):
    """
    Calls `SetBossHealthBarState` with `state=True`.
    The character's health bar will appear at the bottom of the screen, with a name.
    """


def DisableBossHealthBar(character: Character | int, name: NPCName | int = 0, bar_slot: int = 0):
    """
    Calls `SetBossHealthBarState` with `state=False`.
    
    The character's health bar will disappear from the bottom of the screen.
    
    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter,
    so only the first argument actually does anything. You're welcome to specify the name for
    clarity anyway (and vanilla events will show it when decompiled).
    """


def KillBoss(game_area_param_id: int):
    """
    The name is slightly misleading, as this doesn't actually kill any entity. Instead, it marks that you have
    cleared an 'area', as defined by the Game Area params, and is always manually called in EMEVD when you kill
    the boss of that area.
    
    Among other things, this awards your souls for killing the boss (which is why they are delayed and why the
    game will keep trying to give them to you on map load) and prevents you from summoning other players.
    
    The Game Area params ID is generally identical to the entity ID of the appropriate boss. This is just
    convention, but it's one you should stick to for a sensible setup (and for the name of the instruction to
    make sense).
    """


def SetNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int, operation: BitOperation | int):
    """
    Set given navmesh type.
    """


def EnableNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int):
    """
    Calls `SetNavmeshType` with `operation=0`.
    """


def DisableNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int):
    """
    Calls `SetNavmeshType` with `operation=1`.
    """


def ToggleNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int):
    """
    Calls `SetNavmeshType` with `operation=2`.
    """


def WarpToMap(game_map: Map | tuple | list, player_start: PlayerStart | int = -1):
    """
    Warp the main player to the given player entity ID, which is in the Players tab of the MSB, in some map. By
    default, this warps to the 'default position' in the map (-1), which is the same point you would spawn at if
    the game lost track of your stable footing (e.g. in 'wrong warp' glitches).
    """


def HandleMinibossDefeat(miniboss_id: int):
    """
    Called instead of `KillBoss` for bosses that aren't the final boss of the area.
    
    Note that outside of Chalice Dungeons, this is ONLY used when you have defeated Gehrman and are about to
    fight Moon Presence.
    """


def TriggerMultiplayerEvent(event_id: int):
    """
    Used to make the Bell of Awakening sounds, for example.
    """


def SetRandomFlagInRange(flag_range: FlagRange | tuple | list, state: FlagState | int):
    """
    Set the state of a random flag from a given range (inclusive).
    """


def EnableRandomFlagInRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetRandomFlagInRange` with `state=1`.
    """


def DisableRandomFlagInRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetRandomFlagInRange` with `state=0`.
    """


def ToggleRandomFlagInRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetRandomFlagInRange` with `state=2`.
    """


def ForceAnimation(
    entity: Character | Object | int,
    animation_id: int,
    loop: bool | int = False,
    wait_for_completion: bool | int = False,
    skip_transition: bool | int = False,
    unknown1: int = 0,
    unknown2: float = 0.0,
):
    """
    Used a lot. Standard way to make a Character or Object perform an animation.
    """


def SetMapDrawParamSlot(map_area_id: int, draw_param_slot: int):
    """
    Each map area (NOT each map) can have two sets of DrawParams (0 and 1), and this can be used to switch
    between them. Originally only used for Dark Anor Londo.
    
    Note that there's some funny business with how this works in m15 in Dark Souls Remastered, presumably
    because the developers didn't want to bother modifying both slots when they re-did all the DrawParams.
    """


def IncrementNewGameCycle(dummy_arg: int):
    """
    This is manually called at the end of the game. You can call it anytime, but note that there is no way to
    decrement it with events.
    
    The dummy argument is always 0 or 1; not sure if or how it matters.
    """


def SetFlagRangeState(flag_range: FlagRange | tuple | list, state: FlagState | int):
    """
    Set the state of an entire flag range (inclusive).
    """


def EnableFlagRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetFlagRangeState` with `state=1`.
    """


def DisableFlagRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetFlagRangeState` with `state=0`.
    """


def ToggleFlagRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetFlagRangeState` with `state=2`.
    """


def SetRespawnPoint(respawn_point: int):
    """
    Respawn point is an event set in the MSB.
    """


def RemoveItemFromPlayer(item: BaseItemParam | int, quantity: int = 0, item_type: ItemType | int = None):
    """
    Item type is automatically detected. This instruction has a 'quantity' argument, but it seems broken, so you
    always have to remove *all* instances of the item. (Strangely, the similar command used in EzState doesn't
    seem to have this bug.)
    
    WARNING: don't confuse 'Item' with the specific item type 'Good'.
    
    item_type: Auto-detected from `item` type by default.
    """


def RemoveWeaponFromPlayer(item: BaseItemParam | int, quantity: int = 0):
    """
    Calls `RemoveItemFromPlayer` with `item_type=0`.
    """


def RemoveArmorFromPlayer(item: BaseItemParam | int, quantity: int = 0):
    """
    Calls `RemoveItemFromPlayer` with `item_type=1`.
    """


def RemoveRingFromPlayer(item: BaseItemParam | int, quantity: int = 0):
    """
    Calls `RemoveItemFromPlayer` with `item_type=2`.
    """


def RemoveGoodFromPlayer(item: BaseItemParam | int, quantity: int = 0):
    """
    Calls `RemoveItemFromPlayer` with `item_type=3`.
    """


def PlaceSummonSign(
    sign_type: SummonSignType | int,
    character: Character | int,
    region: Region | int,
    summon_flag: Flag | int,
    dismissal_flag: Flag | int,
):
    """
    If you set a black summon sign, the specified NPC will try to invade automatically.
    """


def SetSoapstoneMessageState(message_id: int, state: bool | int):
    """
    Enable or disable developer message.
    """


def EnableSoapstoneMessage(message_id: int):
    """
    Calls `SetSoapstoneMessageState` with `state=True`.
    """


def DisableSoapstoneMessage(message_id: int):
    """
    Calls `SetSoapstoneMessageState` with `state=False`.
    """


def AwardAchievement(achievement_id: int):
    """
    For obvious reasons, I *highly* discourage you from abusing this, except in the interest of maintaining the
    accessibility of existing achievements. This interacts with Steam, which is always dangerous.
    """


def SetVagrantSpawningState(spawning_disabled: bool | int):
    """
    Note inverted bool.
    """


def EnableVagrantSpawning():
    """
    Calls `SetVagrantSpawningState` with `spawning_disabled=False`.
    """


def DisableVagrantSpawning():
    """
    Calls `SetVagrantSpawningState` with `spawning_disabled=True`.
    """


def IncrementEventValue(flag: Flag | int, bit_count: int, max_value: int):
    """
    You can use a contiguous array of flags as a single value. Use this to increment that value by 1.
    
    The array begins at `flag` and extends for `bit_count`. For example, a 'bit_count' of 8 gives you a
    theoretical maximum of 256. You can set a 'max_value' less than that to limit the value. (I'm not sure if it
    ticks over back to zero if `max_value` is greater than the possible value given the bit count.)
    
    The most significant bit is represented at `flag`, and the least significant bit at `flag + bit_count - 1`.
    
    This is used for counters in the vanilla game, such as the number of bosses killed while Rhea is at Undead
    Parish.
    """


def ClearEventValue(flag: Flag | int, bit_count: int):
    """
    Clears the given multi-flag. This is basically like disabling `bit_count` flags in a row, starting at
    `flag`.
    """


def SetNextSnugglyTrade(flag: Flag | int):
    """
    Sets the flag for the next drop based on the item you deposit into the nest.
    """


def SnugglyItemDrop(item_lot: ItemLotParam | int, region: Region | int, flag: Flag | int, collision: Collision | int):
    """
    Makes Snuggly drop an item. There are complex limitations to this in the engine, so be careful. (The list of
    available Snuggly flags is a hard-coded limit, for example.)
    """


def MoveRemains(source_region: Region | int, destination_region: Region | int):
    """
    Move all bloodstains and dropped items from one region to another (I assume). Used to move your
    remains out of Gwyndolin's endless corridor.
    """


def AwardItemLotToHostOnly(item_lot_param_id: int):
    """
    You can simply call AwardItemLot() with the same argument, which will redirect here, as you'll almost never
    *not* want to award an item lot to the host only.
    """


def ArenaRankingRequest1v1():
    """
    TODO
    """


def ArenaRankingRequest2v2():
    """
    TODO
    """


def ArenaRankingRequestFFA():
    """
    TODO
    """


def ArenaExitRequest():
    """
    TODO
    """


def EventValueOperation(
    source_flag: Flag | int,
    source_flag_bit_count: int,
    operand: int,
    target_flag: Flag | int,
    target_flag_bit_count: int,
    calculation_type: CalculationType | int,
):
    """
    Performs a binary operation on the source flag and operand value, and stores the result in the target flag.
    """


def SetAIState(character: Character | int, state: bool | int):
    """
    TODO
    """


def EnableAI(character: Character | int):
    """
    Calls `SetAIState` with `state=True`.
    """


def DisableAI(character: Character | int):
    """
    Calls `SetAIState` with `state=False`.
    """


def SetTeamType(character: Character | int, new_team: TeamType | int):
    """
    TODO
    """


def MoveToEntity(
    character: Character | int,
    destination: Object | Region | Character | int,
    model_point: int = -1,
    destination_type: CoordEntityType | int = None,
):
    """
    Basic move. I recommend you use the combined `Move` function.
    destination_type: Auto-detected from `destination` type by default.
    """


def Kill(character: Character | int, award_souls: bool | int = False):
    """
    Technically a kill 'request.'
    """


def SetCharacterState(character: Character | int, state: bool | int):
    """
    TODO
    """


def EnableCharacter(character: Character | int):
    """
    Calls `SetCharacterState` with `state=True`.
    """


def DisableCharacter(character: Character | int):
    """
    Calls `SetCharacterState` with `state=False`.
    """


def EzstateAIRequest(character: Character | int, command_id: int, command_slot: int):
    """
    Slot number ranges from 0 to 3.
    """


def CreateProjectileOwner(entity: Object | Region | Character | int):
    """
    A 'bullet owner' that will spawn things according to the Spawner section of the MSB.
    """


def AddSpecialEffect(character: Character | int, special_effect_id: int):
    """
    'Special effect' as in a buff/debuff, not graphical effects (though they may come with one).
    """


def SetStandbyAnimationSettings(
    character: Character | int,
    standby_animation: int = -1,
    damage_animation: int = -1,
    cancel_animation: int = -1,
    death_animation: int = -1,
    standby_exit_animation: int = -1,
):
    """
    Sets entity's default standby animations. -1 is default for each category.
    """


def ResetStandbyAnimationSettings(character: Character | int):
    """
    Calls `SetStandbyAnimationSettings` with `standby_animation=-1`, `damage_animation=-1`, `cancel_animation=-1`,
    `death_animation=-1`, `standby_exit_animation=1`.
    """


def SetGravityState(character: Character | int, state: bool | int):
    """
    Simply determines if the character loses height as it moves around. They will still gain height by running
    up slopes.
    """


def EnableGravity(character: Character | int):
    """
    Calls `SetGravityState` with `state=True`.
    """


def DisableGravity(character: Character | int):
    """
    Calls `SetGravityState` with `state=False`.
    """


def SetCharacterEventTarget(character: Character | int, region: Region | int):
    """
    Likely refers to patrolling behavior.
    """


def SetImmortalityState(character: Character | int, state: bool | int):
    """
    Character will take damage, but not die (i.e. cannot go below 1 HP).
    """


def EnableImmortality(character: Character | int):
    """
    Calls `SetImmortalityState` with `state=True`.
    """


def DisableImmortality(character: Character | int):
    """
    Calls `SetImmortalityState` with `state=False`.
    """


def SetNest(character: Character | int, region: Region | int):
    """
    Home point for entity AI.
    """


def RotateToFaceEntity(
    character: Character | int,
    target_entity: Object | Region | Character | int,
    animation: int = -1,
    wait_for_completion: bool | int = False,
):
    """
    Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at
    least.)
    
    The Bloodborne+ version allows you to force an animation at the same time (post-rotation) and optionally
    wait until that animation is completed. (I assume a value of -1 avoids it.)
    """


def SetInvincibilityState(character: Character | int, state: bool | int):
    """
    Character cannot take damage or die.
    """


def EnableInvincibility(character: Character | int):
    """
    Calls `SetInvincibilityState` with `state=True`.
    """


def DisableInvincibility(character: Character | int):
    """
    Calls `SetInvincibilityState` with `state=False`.
    """


def ClearTargetList(character: Character | int):
    """
    Clear list of targets from character AI.
    """


def AICommand(character: Character | int, command_id: int, command_slot: int):
    """
    The given `command_id` can be accessed in AI Lua scripts with `ai:GetEventRequest(slot)`.
    """


def SetEventPoint(character: Character | int, region: Region | int, reaction_range: float):
    """
    Not sure what the usage of this is, but it is likely used to change patrol behavior.
    """


def SetAIParamID(character: Character | int, ai_param_id: int):
    """
    Change character's AI parameter index.
    """


def ReplanAI(character: Character | int):
    """
    Clear current AI goal list and force character to replan it.
    """


def CancelSpecialEffect(character: Character | int, special_effect_id: int):
    """
    'Special effect' as in a buff/debuff, not graphical effects (though they may come with one).
    """


def CreateNPCPart(
    character: Character | int,
    npc_part_id: int,
    part_index: NPCPartType | int,
    part_health: int,
    damage_correction: float = 1.0,
    body_damage_correction: float = 1.0,
    is_invincible: bool | int = False,
    start_in_stop_state: bool | int = False,
):
    """
    Complex. Sets specific damage parameters for part of an NPC model. Further changes to the specific part can
    be made using the events below. The part is specified using the NPCPartType slot. Look at usage in tail cut
    events to understand these more.
    """


def SetNPCPartHealth(character: Character | int, npc_part_id: int, desired_health: int, overwrite_max: bool | int):
    """
    You must create the part first.
    """


def SetNPCPartEffects(character: Character | int, npc_part_id: int, material_sfx_id: int, material_vfx_id: int):
    """
    Attach material effects to an NPC part.
    """


def SetNPCPartBulletDamageScaling(character: Character | int, npc_part_id: int, desired_scaling: float):
    """
    Scale the damage dealt to the part. Usually used to set damage to zero, e.g. Smough's hammer.
    """


def SetDisplayMask(character: Character | int, bit_index: int, switch_type: OnOffChange | int):
    """
    Different bits correspond to different parts of the character model. You can see the initial values for
    these in the NPC params. This is generally used to disable tails when they are cut off.
    
    `switch_type` can be 0 (off), 1 (on), or 2 (change).
    """


def SetCollisionMask(character: Character | int, bit_index: int, switch_type: OnOffChange | int):
    """
    See above. This affects the NPC's Collision, not appearance.
    """


def SetNetworkUpdateAuthority(character: Character | int, authority_level: UpdateAuthority | int):
    """
    Complex; look at existing usage. Authority level must be 'Normal' or 'Forced'.
    """


def SetBackreadState(character: Character | int, remove: bool | int):
    """
    I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread'
    of a character has a larger effect on game resources. It is used, for example, to disable the Fair Lady and
    Eingyi during the Demon Firesage boss fight.
    
    Also note reversed bool.
    """


def EnableBackread(character: Character | int):
    """
    Calls `SetBackreadState` with `remove=False`.
    """


def DisableBackread(character: Character | int):
    """
    Calls `SetBackreadState` with `remove=True`.
    """


def SetHealthBarState(character: Character | int, state: bool | int):
    """
    Normal health bar that appears above character.
    """


def EnableHealthBar(character: Character | int):
    """
    Calls `SetHealthBarState` with `state=True`.
    """


def DisableHealthBar(character: Character | int):
    """
    Calls `SetHealthBarState` with `state=False`.
    """


def SetCharacterCollisionState(character: Character | int, is_disabled: bool | int):
    """
    Note that the bool is inverted from what you might expect.
    """


def EnableCharacterCollision(character: Character | int):
    """
    Calls `SetCharacterCollisionState` with `is_disabled=False`.
    """


def DisableCharacterCollision(character: Character | int):
    """
    Calls `SetCharacterCollisionState` with `is_disabled=True`.
    """


def AIEvent(
    character: Character | int,
    command_id: int,
    command_slot: int,
    first_event_flag: Flag | int,
    last_event_flag: Flag | int,
):
    """
    I have no idea what this does.
    """


def ReferDamageToEntity(character: Character | int, target_entity: Character | int):
    """
    All damage dealt to the first character will *also* (not *only*) be dealt to the target entity. I'm not 100%
    sure if the target entity can be an Object.
    
    Only used by the Four Kings in the vanilla game.
    """


def SetNetworkUpdateRate(character: Character | int, is_fixed: bool | int, update_rate: CharacterUpdateRate | int):
    """
    Not sure what 'is_fixed' does. I believe only 'Always' and 'Never' are used in the vanilla game.
    """


def SetBackreadStateAlternate(character: Character | int, state: bool | int):
    """
    I have no idea how this differs from the standard backread function above.
    """


def HellkiteBreathControl(character: Character | int, obj: Object | int, animation_id: int):
    """
    I don't recommend you mess with this. It seems to be used to create the fire VFX and damaging effect when
    the Hellkite breathes fire on the bridge, with (otherwise invisible) object model o1060. It may simply
    trigger a certain behavior param ID.
    
    Unclear whether the animation applies to the character or object (which is probably an invisible "burning"
    plane).
    """


def DropMandatoryTreasure(character: Character | int):
    """
    This will disable the character and spawn any treasure they would drop. It's possible that it only spawns
    treasure that has a 100% drop rate, hence the name, but I haven't confirmed this.
    """


def BetrayCurrentCovenant(dummy: int = 0):
    """
    Dummy argument does nothing.
    """


def SetAnimationsState(entity: Character | Object | int, state: bool | int):
    """
    TODO
    """


def EnableAnimations(entity: Character | Object | int):
    """
    Calls `SetAnimationsState` with `state=True`.
    """


def DisableAnimations(entity: Character | Object | int):
    """
    Calls `SetAnimationsState` with `state=False`.
    """


def MoveAndSetDrawParent(
    character: Character | int,
    destination: Object | Region | Character | int,
    set_draw_parent: MapPart | int,
    model_point: int = -1,
    destination_type: CoordEntityType | int = None,
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


def ShortMove(
    character: Character | int,
    destination: Object | Region | Character | int,
    model_point: int = -1,
    destination_type: CoordEntityType | int = None,
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


def MoveAndCopyDrawParent(
    character: Character | int,
    destination: Object | Region | Character | int,
    copy_draw_parent: Character | Object | int,
    model_point: int = -1,
    destination_type: CoordEntityType | int = None,
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


def ResetAnimation(character: Character | int, disable_interpolation: bool | int = False):
    """
    Cancels an animation. Note the inverted bool for controlling interpolation.
    """


def SetTeamTypeAndExitStandbyAnimation(character: Character | int, team_type: TeamType | int):
    """
    Two for the price of one. Often used when NPCs with resting animations become hostile.
    """


def HumanityRegistration(character: Character | int, event_flag: Flag | int):
    """
    I believe this designates the first event flag in a range of eight, which tracks how much humanity an NPC
    has for draining with Dark Hand. These flags are all in the 8000 range, and tightly packed, so you'll need
    to find your own range if you want to replicate this.
    
    I can confirm that NOT doing this for a new NPC means you can't drain any humanity from them, rather than
    being able to drain unlimited humanity.
    """


def IncrementPvPSin(dummy: int = 0):
    """
    Normally only happens when you kill an NPC.
    """


def EqualRecovery():
    """
    Unknown effect. Only used in Battle of Stoicism, so likely useless to you.
    """


def DestroyObject(obj: Object | int, request_slot: int = 1):
    """
    Technically 'requests' the object's destruction. No idea what the slot number does.
    """


def RestoreObject(obj: Object | int):
    """
    The opposite of destruction. Restores it to its original MSB coordinates.
    """


def SetObjectState(obj: Object | int, state: bool | int):
    """
    TODO
    """


def EnableObject(obj: Object | int):
    """
    Calls `SetObjectState` with `state=True`.
    """


def DisableObject(obj: Object | int):
    """
    Calls `SetObjectState` with `state=False`.
    """


def SetTreasureState(obj: Object | int, state: bool | int):
    """
    TODO
    """


def EnableTreasure(obj: Object | int):
    """
    Calls `SetTreasureState` with `state=True`.
    Enables any treasure attached to this object by MSB events.
    """


def DisableTreasure(obj: Object | int):
    """
    Calls `SetTreasureState` with `state=False`.
    
    Disables any treasure attached to this object by MSB events.
    
    If you want to disable treasure by default, you can do it in the MSB by changing a certain event
    value to 255.
    """


def ActivateObject(obj: Object | int, obj_act_id: int, relative_index: int):
    """
    Manually call a specific ObjAct event attached to this object. I believe 'relative_index' refers to the
    points on the object at which it can be activated (e.g. which side of a gate you are on).
    
    Note that this will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how
    the game gets Patches to pull the lever in the Catacombs.
    """


def SetObjectActivation(obj: Object | int, obj_act_id: int, state: bool | int):
    """
    Sets whether the object can be activated (1) or not activated (0).
    """


def EndOfAnimation(obj: Object | int, animation_id: int):
    """
    Sets entity to whatever state it would have after the given animation. Used often to open doors that have
    already been opened when you reload the map, etc. I doubt it can be used with characters, but haven't
    confirmed.
    """


def PostDestruction(obj: Object | int, request_slot: int = 1):
    """
    Sets the object to whatever appearance it would have after being destroyed. Again, not sure what 'slot'
    does, but it's literally *always* 1 in vanilla scripts (and from my testing, the instruction doesn't work
    with `slot=0`).
    """


def CreateHazard(
    obj_flag: Flag | int,
    obj: Object | int,
    model_point: int,
    behavior_param_id: int,
    target_type: DamageTargetType | int,
    radius: float,
    life: float,
    repetition_time: float,
):
    """
    Turn an object into an environmental hazard. It deals damage when touched according to the NPC Behavior
    params you give it. The model_point determines which part of the object is hazardous (with the given radius
    and life, relative to the time this instruction occurs).
    
    An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.
    
    'target_type' determines what the hazard can damage (Character and/or Map).
    """


def RegisterStatue(obj: Object | int, game_map: Map | tuple | list, statue_type: StatueType | int):
    """
    Creates a petrified or crystallized statue. I believe this is so it can be seen by other players online.
    """


def MoveObjectToCharacter(obj: Object | int, character: Character | int, model_point: int = -1):
    """
    Move an object to a character.
    """


def RemoveObjectFlag(obj_flag: Flag | int):
    """
    No idea what this does. I believe it might undo the CreateHazard instruction, at least.
    """


def SetObjectInvulnerabilityState(obj: Object | int, state: bool | int):
    """
    1 = invulnerable.
    """


def EnableObjectInvulnerability(obj: Object | int):
    """
    Calls `SetObjectInvulnerabilityState` with `state=True`.
    """


def DisableObjectInvulnerability(obj: Object | int):
    """
    Calls `SetObjectInvulnerabilityState` with `state=False`.
    """


def SetObjectActivationWithIdx(obj: Object | int, obj_act_id: int, relative_index: int, state: bool | int):
    """
    Similar to SetObjectActivation, but you can provide the relative index to disable (e.g. one side of a door).
    """


def EnableTreasureCollection(obj: Object | int):
    """
    Forces an object to spawn its treasure, even if the treasure's ItemLot flag is already enabled.
    
    Useful if you want some treasure to reappear (after, say, taking it from the player and disabling the
    ItemLot flag) without the player needing to reload the map.
    """


def DeleteVFX(vfx_id: VFXEvent | int, erase_root_only: bool = True):
    """
    Delete visual VFX. If 'erase_root_only' is True (default), effect particles already emitted will live out
    the rest of their lifetimes (e.g. making a fog gate disappear organically). The ID is given in the MSB.
    """


def CreateVFX(vfx_id: VFXEvent | int):
    """
    Create visual VFX. The ID is given in the MSB (e.g. fog effect for boss gates and checkpoints).
    """


def CreateTemporaryVFX(
    vfx_id: int,
    anchor_entity: Object | Region | Character | int,
    model_point: int = -1,
    anchor_type: CoordEntityType | int = None,
):
    """
    Create one-off visual VFX (an FFX ID) attached to the given 'anchor_entity'. The VFX, of course, must be
    currently loaded (or in common effects).
    
    anchor_type: Auto-detected from `anchor_entity` type by default. Sets `Character` type for `PLAYER`.
    """


def CreateObjectVFX(obj: Object | int, vfx_id: int, model_point: int):
    """
    TODO
    """


def DeleteObjectVFX(obj: Object | int, erase_root: bool = True):
    """
    Note `erase_root` vs. `erase_root_only` for map SFX.
    """


def DisplayDialog(
    text: EventText | int,
    anchor_entity: Object | Region | Character | int = -1,
    display_distance: float = 3.0,
    button_type: ButtonType | int = ButtonType.OK_or_Cancel,
    number_buttons: NumberButtons | int = NumberButtons.NoButton,
):
    """
    Display a dialog box at the bottom of the screen. You can't use this to get player input, but you can
    display short simple messages. It defaults to a box with no buttons (which is still dismissed when you press
    A).
    
    The 'display_distance' argument specifies how far you can move away from the 'anchor_entity' before the
    message automatically disappears. If `anchor_entity=-1` (default), some kind of default anchor is used
    (probably just the position where the player was standing).
    """


def DisplayBanner(banner_type: BannerType | int):
    """
    Display a pre-rendered banner. You'll have to change the textures (in menu_local.tpf) to change them.
    """


def DisplayStatus(text: EventText | int, pad_enabled: bool = True):
    """
    Displays a large message that appears at the top of the screen, such as the message that tells you how to
    remove your curse, or that the golden fog gates block your path. If 'pad_enabled' is False, you can't get
    rid of the message until it times out on its own.
    """


def DisplayBattlefieldMessage(text: EventText | int, display_location_index: int):
    """
    Used in the Battle of Stoicism. Probably useless to you.
    """


def ArenaSetNametag1(player_id: int):
    """
    TODO
    """


def ArenaSetNametag2(player_id: int):
    """
    TODO
    """


def ArenaSetNametag3(player_id: int):
    """
    TODO
    """


def ArenaSetNametag4(player_id: int):
    """
    TODO
    """


def DisplayArenaDissolutionMessage(text: EventText | int):
    """
    TODO
    """


def ChangeCamera(normal_camera_id: int, locked_camera_id: int):
    """
    TODO
    """


def SetCameraVibration(
    vibration_id: int,
    anchor_entity: Object | Region | Character | int,
    model_point: int = -1,
    decay_start_distance: float = 999.0,
    decay_end_distance: float = 999.0,
    anchor_type: CoordEntityType | int = None,
):
    """
    TODO
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def SetLockedCameraSlot(game_map: Map | tuple | list, camera_slot: int):
    """
    Switch between one of two camera slots associated with the player's current collision in the MSB.
    """


def RegisterLadder(start_climbing_flag: Flag | int, stop_climbing_flag: Flag | int, obj: Object | int):
    """
    Don't mess with these flags, generally; you can just delay when this is called after map load to disable
    certain ladders (which is kind of weird anyway).
    """


def InitializeWanderingDemon(flag: Flag | int, demon_entity: Character | int, appearance_flag: Flag | int):
    """
    Unused. Probably a Demon's Souls remnant.
    """


def RegisterWanderingDemon(
    flag: Flag | int,
    demon_entity: Character | int,
    unknown_entity: Object | Region | Character | int,
):
    """
    Unused. Probably a Demon's Souls remnant.
    """


def RegisterBonfire(
    bonfire_flag: Flag | int,
    obj: Object | int,
    reaction_distance: float = 2.0,
    reaction_angle: float = 180.0,
    initial_kindle_level: int = 0,
):
    """
    Register a bonfire, which creates the flame VFX and allows you to interact with it (via the MSB entity with
    ID (obj + 1000).
    
    I believe the bonfire flag tells the game where to keep track of its kindle level, or something like that. I
    don't recommend messing around with this much. The reaction distance, angle, and initial kindle level are
    all set to their standard defaults for bonfires.
    
    Note that, for some reason, kindle level is defined in increments of 10, so the number of Estus Flasks given
    is (initial_kindle_level / 2) + 5.
    
    There also seems to be an issue with registering a bonfire that has already been registered with a greater
    initial kindle level. Beware of this, if you find that you can't interact with bonfires or get them to even
    register.
    """


def ActivateMultiplayerBuffs(character: Character | int):
    """
    Used to strengthen bosses based on the number of summons you have. Not sure if it works for every NPC. It
    could also be tied to certain special effects; haven't checked that yet.
    """


def RegisterHealingFountain(
    flag: Flag | int,
    obj: Object | int,
    reaction_distance: float,
    reaction_angle: float,
    initial_sword_number: int,
    sword_level: int,
):
    """
    No idea what this is. Apparently DS1 also has a version of this with less arguments.
    """


def NotifyBossBattleStart(dummy: int = 0):
    """
    Sends the message to all summons that the host has challenged the boss.
    """


def SetBackgroundMusic(
    state: bool | int,
    music_slot: int,
    entity: Object | Region | Character | int,
    sound_type: SoundType | int,
    sound_id: int,
):
    """
    TODO
    """


def PlaySoundEffect(
    anchor_entity: Object | Region | Character | int,
    sound_id: int,
    sound_type: SoundType | int = None,
):
    """
    Anchor entity determines sound position and the sound type is used to look up the source.
    """


def SetSoundEventState(sound_id: int, state: bool | int):
    """
    The sound ID is in the MSB. Includes boss music, which is obviously the most common use, and ambiance.
    """


def EnableSoundEvent(sound_id: int):
    """
    Calls `SetSoundEventState` with `state=True`.
    """


def DisableSoundEvent(sound_id: int):
    """
    Calls `SetSoundEventState` with `state=False`.
    """


def SetMapCollisionState(collision: Collision | int, state: bool | int):
    """
    Enable or disable a map collision (HKX). The ID is specified in the MSB. Note that a Collision doesn't have
    to be solid ground, but could be anything triggered by collision, such as a kill plane (which this is often
    used to disable).
    """


def EnableMapCollision(collision: Collision | int):
    """
    Calls `SetMapCollisionState` with `state=True`.
    """


def DisableMapCollision(collision: Collision | int):
    """
    Calls `SetMapCollisionState` with `state=False`.
    """


def SetMapCollisionBackreadMaskState(collision: Collision | int, state: bool | int):
    """
    Unused.
    """


def EnableMapCollisionBackreadMask(collision: Collision | int):
    """
    Calls `SetMapCollisionBackreadMaskState` with `state=True`.
    """


def DisableMapCollisionBackreadMask(collision: Collision | int):
    """
    Calls `SetMapCollisionBackreadMaskState` with `state=False`.
    """


def SetMapPieceState(map_piece_id: MapPiece | int, state: bool | int):
    """
    Set the visibility of individual map pieces (e.g. all the crystals in Seath's tower).
    """


def EnableMapPiece(map_piece_id: MapPiece | int):
    """
    Calls `SetMapPieceState` with `state=True`.
    """


def DisableMapPiece(map_piece_id: MapPiece | int):
    """
    Calls `SetMapPieceState` with `state=False`.
    """


def IfAttackedWithDamageType(
    condition: int,
    attacked_entity: Character | int,
    attacker: Character | int = -1,
    damage_type: DamageType | int = DamageType.Unspecified,
):
    """
    TODO
    """


def IfActionButtonParamActivated(condition: int, action_button_id: int, entity: Object | Region | Character | int):
    """
    TODO
    """


def IfPlayerOwnWorldState(condition: int, not_in_own_world: bool | int):
    """
    Excluding Arena.
    """


def IfPlayerInOwnWorld(condition: int):
    """
    Calls `IfPlayerOwnWorldState` with `not_in_own_world=False`.
    """


def IfPlayerNotInOwnWorld(condition: int):
    """
    Calls `IfPlayerOwnWorldState` with `not_in_own_world=True`.
    """


def IfMapCeremonyState(condition: int, state: bool | int, game_map: Map | tuple | list, ceremony_id: int):
    """
    Ceremony states are unused except for Untended Graves, I believe.
    """


def IfMapInCeremony(condition: int, game_map: Map | tuple | list, ceremony_id: int):
    """
    Calls `IfMapCeremonyState` with `state=True`.
    """


def IfMapNotInCeremony(condition: int, game_map: Map | tuple | list, ceremony_id: int):
    """
    Calls `IfMapCeremonyState` with `state=False`.
    """


def IfMultiplayerNetworkPenalized(condition: int):
    """
    TODO
    """


def IfPlayerGender(condition: int, gender: Gender | int):
    """
    Note that this condition version of the gender test was absent in Bloodborne.
    """


def IfOngoingCutsceneFinished(condition: int, cutscene_id: int):
    """
    TODO
    """


def IfHollowArenaMatchReadyState(condition: int, is_ready: bool | int):
    """
    TODO
    """


def IfHollowArenaSoloResults(condition: int, result: HollowArenaResult | int):
    """
    TODO
    """


def IfHollowArenaSoloScoreComparison(condition: int, comparison_type: ComparisonType | int, value: int, unknown: int):
    """
    Unknown fourth argument.
    """


def IfHollowArenaTeamResults(condition: int, result: HollowArenaResult | int):
    """
    TODO
    """


def IfSteamDisconnected(condition: int, is_disconnected: bool | int):
    """
    TODO
    """


def IfAllyPhantomCountComparison(
    condition: int,
    comparison_state: bool | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Note that there's a 'comparison_state' bool that can be used to invert the operation (kind of pointless).
    """


def IfCharacterDrawGroupState(
    condition: int,
    character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Tests if character's draw group is currently enabled or disabled.
    """


def IfCharacterDrawGroupEnabled(
    condition: int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterDrawGroupState` with `state=True`.
    """


def IfCharacterDrawGroupDisabled(
    condition: int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfCharacterDrawGroupState` with `state=False`.
    """


def IfPlayerRemainingYoelLevelComparison(condition: int, comparison_type: ComparisonType | int, value: int):
    """
    Tests the number of remaining levels available from Yoel, I presume.
    """


def IfCharacterInvadeType(
    condition: int,
    character: Character | int,
    invade_type: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    'invade_type' has an unknown type in the EMEDF. Probably refers to the invader's covenant.
    """


def IfCharacterChameleonState(
    condition: int,
    character: Character | int,
    chameleon_vfx_id: int,
    is_transformed: bool | int,
):
    """
    TODO
    """


def IfObjectBurnState(
    condition: int,
    obj: Object | int,
    comparison_type: ComparisonType | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    This test is used exactly once, in the High Wall of Lothric, where the 'comparison_type' is GreaterThan. I
    have no idea what that argument does. However, it's possible that 'state' isn't actually a bool, but some
    measure of the intensity of the burn state, because the event it's used in strongly suggests that a fire
    effect is created as long as the burn state is 'greater than zero'.
    """


def IfObjectBackreadState(
    condition: int,
    obj: Object | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    TODO
    """


def IfObjectBackreadEnabled(
    condition: int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfObjectBackreadState` with `state=True`.
    """


def IfObjectBackreadDisabled(
    condition: int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `IfObjectBackreadState` with `state=False`.
    """


def IfObjectBackreadState_Alternate(
    condition: int,
    obj: Object | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    The fact they added this suggests that the 'alternate' version that already existed for characters is
    actually useful in some way (and they did use it in DS1).
    """


def GotoIfConditionState(label: Label | int, required_state: bool | int, input_condition: int):
    """
    TODO
    """


def GotoIfConditionTrue(label: Label | int, input_condition: int):
    """
    Calls `GotoIfConditionState` with `required_state=True`.
    """


def GotoIfConditionFalse(label: Label | int, input_condition: int):
    """
    Calls `GotoIfConditionState` with `required_state=False`.
    """


def Goto(label: Label | int):
    """
    Unconditional GOTO.
    """


def GotoIfValueComparison(label: Label | int, comparison_type: ComparisonType | int, left: int, right: int):
    """
    TODO
    """


def GotoIfFinishedConditionState(label: Label | int, required_state: bool | int, input_condition: int):
    """
    Finished version.
    """


def GotoIfFinishedConditionTrue(label: Label | int, input_condition: int):
    """
    Calls `GotoIfFinishedConditionState` with `required_state=True`.
    """


def GotoIfFinishedConditionFalse(label: Label | int, input_condition: int):
    """
    Calls `GotoIfFinishedConditionState` with `required_state=False`.
    """


def WaitHollowArenaHalftime(match_type: HollowArenaMatchType | int, is_second_half: bool | int):
    """
    'StayParam lookup'.
    """


def SkipLinesIfMultiplayerState(line_count: int, state: MultiplayerState | int):
    """
    TODO
    """


def SkipLinesIfHost(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=0`.
    """


def SkipLinesIfClient(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=1`.
    """


def SkipLinesIfTryingToCreateSession(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=2`.
    """


def SkipLinesIfTryingToJoinSession(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=3`.
    """


def SkipLinesIfLeavingSession(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=4`.
    """


def SkipLinesIfFailedToCreateSession(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=5`.
    """


def ReturnIfMultiplayerState(event_return_type: EventReturnType | int, state: MultiplayerState | int):
    """
    TODO
    """


def EndIfHost():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=0`.
    """


def EndIfClient():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=1`.
    """


def EndIfTryingToCreateSession():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=2`.
    """


def EndIfTryingToJoinSession():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=3`.
    """


def EndIfLeavingSession():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=4`.
    """


def EndIfFailedToCreateSession():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=5`.
    """


def RestartIfHost():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=0`.
    """


def RestartIfClient():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=1`.
    """


def RestartIfTryingToCreateSession():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=2`.
    """


def RestartIfTryingToJoinSession():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=3`.
    """


def RestartIfLeavingSession():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=4`.
    """


def RestartIfFailedToCreateSession():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=5`.
    """


def SkipLinesIfCoopClientCountComparison(skip_lines: int, comparison_type: ComparisonType | int, value: int):
    """
    Value should be from 0 to 4.
    """


def ReturnIfCoopClientCountComparison(
    event_return_type: EventReturnType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    TODO
    """


def EndIfCoopClientCountComparison(comparison_type: ComparisonType | int, value: int):
    """
    Calls `ReturnIfCoopClientCountComparison` with `event_return_type=0`.
    """


def RestartIfCoopClientCountComparison(comparison_type: ComparisonType | int, value: int):
    """
    Calls `ReturnIfCoopClientCountComparison` with `event_return_type=1`.
    """


def GotoIfCharacterSpecialEffectState(
    label: Label | int,
    character: Character | int,
    special_effect: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Note that 'target_count' is now an integer again...
    """


def GotoIfPlayerHasSpecialEffect(
    label: Label | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `GotoIfCharacterSpecialEffectState` with `character=10000`, `state=True`.
    """


def GotoIfPlayerDoesNotHaveSpecialEffect(
    label: Label | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `GotoIfCharacterSpecialEffectState` with `character=10000`, `state=False`.
    """


def GotoIfCharacterHasSpecialEffect(
    label: Label | int,
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `GotoIfCharacterSpecialEffectState` with `state=True`.
    """


def GotoIfCharacterDoesNotHaveSpecialEffect(
    label: Label | int,
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `GotoIfCharacterSpecialEffectState` with `state=False`.
    """


def GotoIfPlayerOwnWorldState(label: Label | int, not_in_own_world: bool | int):
    """
    TODO
    """


def GotoIfPlayerInOwnWorld(label: Label | int):
    """
    Calls `GotoIfPlayerOwnWorldState` with `not_in_own_world=False`.
    """


def GotoIfPlayerNotInOwnWorld(label: Label | int):
    """
    Calls `GotoIfPlayerOwnWorldState` with `not_in_own_world=True`.
    """


def ReturnIfPlayerOwnWorldState(event_return_type: EventReturnType | int, not_in_own_world: bool | int):
    """
    TODO
    """


def EndIfPlayerInOwnWorld():
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=0`, `not_in_own_world=False`.
    """


def EndIfPlayerNotInOwnWorld():
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=0`, `not_in_own_world=True`.
    """


def RestartIfPlayerInOwnWorld():
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=1`, `not_in_own_world=False`.
    """


def RestartIfPlayerNotInOwnWorld():
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=1`, `not_in_own_world=True`.
    """


def SkipLinesIfClientTypeCountComparison(
    skip_lines: int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Value from 0 to 4.
    """


def GotoIfClientTypeCountComparison(
    label: Label | int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Value from 0 to 4.
    """


def ReturnIfClientTypeCountComparison(
    event_return_type: EventReturnType | int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Value from 0 to 4.
    """


def EndIfClientTypeCountComparison(client_type: ClientType | int, comparison_type: ComparisonType | int, value: int):
    """
    Calls `ReturnIfClientTypeCountComparison` with `event_return_type=0`.
    """


def RestartIfClientTypeCountComparison(
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Calls `ReturnIfClientTypeCountComparison` with `event_return_type=1`.
    """


def GotoIfFlagState(label: Label | int, state: bool | int, flag_type: FlagType | int, flag: Flag | int):
    """
    TODO
    """


def GotoIfThisEventFlagEnabled(label: Label | int):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=1`, `flag=0`.
    """


def GotoIfThisEventFlagDisabled(label: Label | int):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=1`, `flag=0`.
    """


def GotoIfThisEventSlotFlagEnabled(label: Label | int):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=2`, `flag=0`.
    """


def GotoIfThisEventSlotFlagDisabled(label: Label | int):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=2`, `flag=0`.
    """


def GotoIfFlagEnabled(label: Label | int, flag: Flag | int):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=0`.
    """


def GotoIfFlagDisabled(label: Label | int, flag: Flag | int):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=0`.
    """


def GotoIfFlagRangeState(
    label: Label | int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
):
    """
    TODO
    """


def GotoIfFlagRangeAllEnabled(label: Label | int, flag_range: FlagRange | tuple | list):
    """
    Calls `GotoIfFlagRangeState` with `state=0`, `flag_type=0`.
    """


def GotoIfFlagRangeAllDisabled(label: Label | int, flag_range: FlagRange | tuple | list):
    """
    Calls `GotoIfFlagRangeState` with `state=1`, `flag_type=0`.
    """


def GotoIfFlagRangeAnyEnabled(label: Label | int, flag_range: FlagRange | tuple | list):
    """
    Calls `GotoIfFlagRangeState` with `state=2`, `flag_type=0`.
    """


def GotoIfFlagRangeAnyDisabled(label: Label | int, flag_range: FlagRange | tuple | list):
    """
    Calls `GotoIfFlagRangeState` with `state=3`, `flag_type=0`.
    """


def GotoIfMultiplayerState(label: Label | int, state: MultiplayerState | int):
    """
    TODO
    """


def GotoIfHost(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=0`.
    """


def GotoIfClient(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=1`.
    """


def GotoIfTryingToCreateSession(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=2`.
    """


def GotoIfTryingToJoinSession(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=3`.
    """


def GotoIfLeavingSession(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=4`.
    """


def GotoIfFailedToCreateSession(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=5`.
    """


def GotoIfMapPresenceState(label: Label | int, state: bool | int, game_map: Map | tuple | list):
    """
    TODO
    """


def GotoIfInsideMap(label: Label | int, game_map: Map | tuple | list):
    """
    Calls `GotoIfMapPresenceState` with `state=True`.
    """


def GotoIfOutsideMap(label: Label | int, game_map: Map | tuple | list):
    """
    Calls `GotoIfMapPresenceState` with `state=False`.
    """


def GotoIfCoopClientCountComparison(label: Label | int, comparison_type: ComparisonType | int, value: int):
    """
    TODO
    """


def ReturnIfCharacterSpecialEffectState(
    event_return_type: EventReturnType | int,
    character: Character | int,
    special_effect: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    TODO
    """


def EndIfPlayerHasSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `character=10000`, `state=True`.
    """


def EndIfPlayerDoesNotHaveSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `character=10000`, `state=False`.
    """


def RestartIfPlayerHasSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=1`, `character=10000`, `state=True`.
    """


def RestartIfPlayerDoesNotHaveSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=1`, `character=10000`, `state=False`.
    """


def EndIfCharacterHasSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `state=True`.
    """


def EndIfCharacterDoesNotHaveSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `state=False`.
    """


def RestartIfCharacterHasSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=1`, `state=True`.
    """


def RestartIfCharacterDoesNotHaveSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=1`, `state=False`.
    """


def SkipLinesIfCharacterSpecialEffectState(
    line_count: int,
    character: Character | int,
    special_effect: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    TODO
    """


def SkipLinesIfPlayerHasSpecialEffect(
    line_count: int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `SkipLinesIfCharacterSpecialEffectState` with `character=10000`, `state=True`.
    """


def SkipLinesIfPlayerDoesNotHaveSpecialEffect(
    line_count: int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `SkipLinesIfCharacterSpecialEffectState` with `character=10000`, `state=False`.
    """


def SkipLinesIfCharacterHasSpecialEffect(
    line_count: int,
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `SkipLinesIfCharacterSpecialEffectState` with `state=True`.
    """


def SkipLinesIfCharacterDoesNotHaveSpecialEffect(
    line_count: int,
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
):
    """
    Calls `SkipLinesIfCharacterSpecialEffectState` with `state=False`.
    """


def GotoIfCharacterRegionState(
    label: Label | int,
    state: bool | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    EMEDF does not have the final new argument listed (it's the same as the other region/distance checks).
    """


def GotoIfPlayerInsideRegion(label: Label | int, region: Region | int, min_target_count: int = 1):
    """
    Calls `GotoIfCharacterRegionState` with `character=10000`, `state=True`.
    """


def GotoIfPlayerOutsideRegion(label: Label | int, region: Region | int, min_target_count: int = 1):
    """
    Calls `GotoIfCharacterRegionState` with `character=10000`, `state=False`.
    """


def GotoIfCharacterInsideRegion(
    label: Label | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    Calls `GotoIfCharacterRegionState` with `state=True`.
    """


def GotoIfCharacterOutsideRegion(
    label: Label | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    Calls `GotoIfCharacterRegionState` with `state=False`.
    """


def ReturnIfCharacterRegionState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    TODO
    """


def EndIfPlayerInsideRegion(region: Region | int, min_target_count: int = 1):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `character=10000`, `state=True`.
    """


def EndIfPlayerOutsideRegion(region: Region | int, min_target_count: int = 1):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `character=10000`, `state=False`.
    """


def RestartIfPlayerInsideRegion(region: Region | int, min_target_count: int = 1):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `character=10000`, `state=True`.
    """


def RestartIfPlayerOutsideRegion(region: Region | int, min_target_count: int = 1):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `character=10000`, `state=False`.
    """


def EndIfCharacterInsideRegion(character: Character | int, region: Region | int, min_target_count: int = 1):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `state=True`.
    """


def EndIfCharacterOutsideRegion(character: Character | int, region: Region | int, min_target_count: int = 1):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfCharacterInsideRegion(character: Character | int, region: Region | int, min_target_count: int = 1):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfCharacterOutsideRegion(character: Character | int, region: Region | int, min_target_count: int = 1):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `state=False`.
    """


def SkipLinesIfCharacterRegionState(
    line_count: int,
    state: bool | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    TODO
    """


def SkipLinesIfPlayerInsideRegion(line_count: int, region: Region | int, min_target_count: int = 1):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=True`, `character=10000`.
    """


def SkipLinesIfPlayerOutsideRegion(line_count: int, region: Region | int, min_target_count: int = 1):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=False`, `character=10000`.
    """


def SkipLinesIfCharacterInsideRegion(
    line_count: int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=True`.
    """


def SkipLinesIfCharacterOutsideRegion(
    line_count: int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=False`.
    """


def GotoIfHollowArenaMatchType(label: Label | int, match_type: HollowArenaMatchType | int):
    """
    TODO
    """


def GotoIfObjectDestructionState(
    label: Label | int,
    obj: Object | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Note change in argument order.
    """


def GotoIfObjectDestroyed(
    label: Label | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `GotoIfObjectDestructionState` with `state=True`.
    """


def GotoIfObjectNotDestroyed(
    label: Label | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """
    Calls `GotoIfObjectDestructionState` with `state=False`.
    """


def DefineLabel_0():
    """
    Define position of label 0 for Goto instructions.
    """


def DefineLabel_1():
    """
    Define position of label 1 for Goto instructions.
    """


def DefineLabel_2():
    """
    Define position of label 2 for Goto instructions.
    """


def DefineLabel_3():
    """
    Define position of label 3 for Goto instructions.
    """


def DefineLabel_4():
    """
    Define position of label 4 for Goto instructions.
    """


def DefineLabel_5():
    """
    Define position of label 5 for Goto instructions.
    """


def DefineLabel_6():
    """
    Define position of label 6 for Goto instructions.
    """


def DefineLabel_7():
    """
    Define position of label 7 for Goto instructions.
    """


def DefineLabel_8():
    """
    Define position of label 8 for Goto instructions.
    """


def DefineLabel_9():
    """
    Define position of label 9 for Goto instructions.
    """


def DefineLabel_10():
    """
    Define position of label 10 for Goto instructions.
    """


def DefineLabel_11():
    """
    Define position of label 11 for Goto instructions.
    """


def DefineLabel_12():
    """
    Define position of label 12 for Goto instructions.
    """


def DefineLabel_13():
    """
    Define position of label 13 for Goto instructions.
    """


def DefineLabel_14():
    """
    Define position of label 14 for Goto instructions.
    """


def DefineLabel_15():
    """
    Define position of label 15 for Goto instructions.
    """


def DefineLabel_16():
    """
    Define position of label 16 for Goto instructions.
    """


def DefineLabel_17():
    """
    Define position of label 17 for Goto instructions.
    """


def DefineLabel_18():
    """
    Define position of label 18 for Goto instructions.
    """


def DefineLabel_19():
    """
    Define position of label 19 for Goto instructions.
    """


def DefineLabel_20():
    """
    Define position of label 20 for Goto instructions.
    """


def PlayCutsceneAndMovePlayerAndSetTimePeriod(
    cutscene: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    game_map: Map | tuple | list,
    player_id: int,
    time_period_id: int,
):
    """
    Warp a particular player to a region and set the time period. I assume that this must be a map that is
    already loaded, like in DS1, but possibly not.
    
    It's used only twice: to play the cutscene when you first reach Cathedral Ward (time period 1) and when you
    examine Laurence's skull after defeating Vicar Amelia (time period 2). It's NOT used after you defeat Rom,
    when the blood moon begins. The time period ID may in fact be unused.
    """


def PlayCutsceneAndSetTimePeriod(
    cutscene: int,
    cutscene_flags: CutsceneFlags | int,
    player_id: int,
    time_period_id: int,
):
    """
    Probably used when you examine Laurence's skull, etc.
    """


def PlayCutsceneAndMovePlayer_Dummy(move_to_region: Region | int, game_map: Map | tuple | list):
    """
    Likely not used, doesn't even take a cutscene ID argument.
    """


def PlayCutsceneAndMovePlayerAndSetMapCeremony(
    cutscene: int,
    cutscene_flags: CutsceneFlags | int,
    ceremony_id: int,
    unknown: int,
    move_to_region: Region | int,
    game_map: Map | tuple | list,
    player_id: int,
):
    """
    I assume that this must be a map that is already loaded, like in DS1, but possibly not.
    
    Contains an unknown argument that may always be zero. TODO: Check.
    """


def PlayCutsceneAndSetMapCeremony(
    cutscene: int,
    cutscene_flags: CutsceneFlags | int,
    ceremony_id: int,
    unknown: int,
    player_id: int,
):
    """
    TODO
    """


def PlayCutsceneAndMoveSpecificPlayer_WithUnknowns(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    game_map: Map | tuple | list,
    player_id: int,
    unknown1: int,
    unknown2: int,
):
    """
    TODO
    """


def PlayCutsceneAndMoveSpecificPlayer_WithOtherRegion(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    game_map: Map | tuple | list,
    player_id: int,
    other_region: Region | int,
):
    """
    TODO
    """


def Unknown_2003_27(arg1: int):
    """
    No information. Used exactly once, after the cutscene that played when Ludwig's first phase was defeated
    with the Old Hunters DLC demo flag enabled. Unknown effect. Maybe just terminated the whole DLC demo.
    """


def StoreItemAmountSpecifiedByFlagValue(
    item_type: ItemType | int,
    item: BaseItemParam | int,
    flag: Flag | int,
    bit_count: int,
):
    """
    Stores some amount of items read from a flag array.
    """


def GivePlayerItemAmountSpecifiedByFlagValue(
    item_type: ItemType | int,
    item: BaseItemParam | int,
    flag: Flag | int,
    bit_count: int,
):
    """
    Gives player some amount of items read from a flag array. Probably used when taking items out of storage
    (i.e. the reverse of the above instruction).
    """


def SetDirectionDisplayState(state: bool | int):
    """
    Not sure what this is.
    """


def EnableDirectionDisplayState():
    """
    Calls `SetDirectionDisplayState` with `state=True`.
    """


def DisableDirectionDisplayState():
    """
    Calls `SetDirectionDisplayState` with `state=False`.
    """


def SetMapHitGridCorrespondence(
    collision: Collision | int,
    level: int,
    grid_coord_x: int,
    grid_coord_y: int,
    state: bool | int,
):
    """
    TODO
    """


def EnableMapHitGridCorrespondence(collision: Collision | int, level: int, grid_coord_x: int, grid_coord_y: int):
    """
    Calls `SetMapHitGridCorrespondence` with `state=True`.
    """


def DisableMapHitGridCorrespondence(collision: Collision | int, level: int, grid_coord_x: int, grid_coord_y: int):
    """
    Calls `SetMapHitGridCorrespondence` with `state=False`.
    """


def SetMapContentImageDisplayState(content_image_part_id: int, state: bool | int):
    """
    TODO
    """


def SetMapBoundariesDisplay(hierarchy: int, grid_coord_x: int, grid_coord_y: int, state: bool | int):
    """
    TODO
    """


def SetAreaWind(region: Region | int, state: bool | int, duration: float, wind_parameter_id: int):
    """
    TODO
    """


def WarpPlayerToRespawnPoint(respawn_point_id: int):
    """
    TODO
    """


def StartEnemySpawner(spawner_id: int):
    """
    TODO
    """


def SummonNPC(
    sign_type: SingleplayerSummonSignType | int,
    character: Character | int,
    region: Region | int,
    summon_flag: Flag | int,
    dismissal_flag: Flag | int,
):
    """
    TODO
    """


def InitializeWarpObject(warp_object_id: int):
    """
    TODO
    """


def MakeEnemyAppear(character: Character | int):
    """
    TODO
    """


def SetCurrentMapCeremony(ceremony_id: int):
    """
    TODO
    """


def SetMapCeremony(game_map: Map | tuple | list, ceremony_id: int):
    """
    TODO
    """


def DisplayEpitaphMessage(message: EventText | int):
    """
    TODO
    """


def SetNetworkConnectedFlagState(flag: Flag | int, state: FlagState | int):
    """
    TODO
    """


def SetNetworkConnectedFlagRangeState(flag_range: FlagRange | tuple | list, state: FlagState | int):
    """
    Network-synchronized variant of `SetFlagRangeState` (2003[22]).
    """


def EnableNetworkConnectedFlagRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetNetworkConnectedFlagRangeState` with `state=1`.
    """


def DisableNetworkConnectedFlagRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetNetworkConnectedFlagRangeState` with `state=0`.
    """


def ToggleNetworkConnectedFlagRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetNetworkConnectedFlagRangeState` with `state=2`.
    """


def SetOmissionModeCounts(level_1_count: int, level_2_count: int):
    """
    TODO
    """


def ResetOmissionModeCountsToDefault():
    """
    TODO
    """


def InitializeCrowTrade(
    item_type: ItemType | int,
    item_id: BaseItemParam | int,
    item_lot_id: ItemLotParam | int,
    trade_completed_flag: Flag | int,
    crow_response_flag: Flag | int,
):
    """
    TODO
    """


def InitializeCrowTradeRegion(region: Region | int):
    """
    TODO
    """


def SetNetworkInteractionState(state: bool | int):
    """
    TODO
    """


def SetHUDVisibilityState(is_invisible: bool | int):
    """
    TODO
    """


def EnableHUDVisibility():
    """
    Calls `SetHUDVisibilityState` with `is_invisible=False`.
    """


def DisableHUDVisibility():
    """
    Calls `SetHUDVisibilityState` with `is_invisible=True`.
    """


def SetBonfireWarpingState(bonfire_obj: Object | int, animation: int, state: bool | int):
    """
    TODO
    """


def EnableBonfireWarping(bonfire_obj: Object | int, animation: int):
    """
    Calls `SetBonfireWarpingState` with `state=True`.
    """


def DisableBonfireWarping(bonfire_obj: Object | int, animation: int):
    """
    Calls `SetBonfireWarpingState` with `state=False`.
    """


def SetAutogeneratedEventSpecificFlag_1(unknown1: int, unknown2: int):
    """
    No idea, but probably relates to setting the flag whose ID matches the event ID.
    """


def HandleBossDefeatAndDisplayBanner(boss: int, banner: BannerType | int):
    """
    Not sure if the 'boss' is a GameAreaParam or just Character.
    """


def SetAutogeneratedEventSpecificFlag_2(unknown1: int, unknown2: int):
    """
    No idea, but probably relates to setting the flag whose ID matches the event ID.
    """


def SetLoadingScreenTipsState(tips_disabled: bool | int):
    """
    TODO
    """


def EnableLoadingScreenTips():
    """
    Calls `SetLoadingScreenTipsState` with `tips_disabled=False`.
    """


def DisableLoadingScreenTips():
    """
    Calls `SetLoadingScreenTipsState` with `tips_disabled=True`.
    """


def AwardGestureItem(gesture_id: int, item_type: ItemType | int, item_id: int):
    """
    Not sure if this awards an actual gesture (then why multiple args?) or awards it based on a gesture (but
    then why not region-specific?).
    """


def SendNPCSummonHome(character: Character | int):
    """
    Identical to Bloodborne version, but with different index.
    """


def Unknown_2003_79(unknown1: int):
    """
    TODO
    """


def SetDecoratedBossHealthBarState(
    state: bool | int,
    character: Character | int,
    slot: int,
    name: EventText | int,
    decoration: int,
):
    """
    Pretty cool; not sure when this is used in the vanilla game or what decorations are available (apparently
    255). As in Bloodborne, slot must be from 0 to 2.
    """


def PlaceNPCSummonSign_WithoutEmber(
    sign_type: SummonSignType | int,
    character: Character | int,
    region: Region | int,
    summon_flag: Flag | int,
    dismissal_flag: Flag | int,
):
    """
    TODO
    """


def ChangeCharacterCloth(character: Character | int, bit_count: int, state_id: int):
    """
    TODO
    """


def ChangePatrolBehavior(character: Character | int, patrol_information_id: int):
    """
    I don't know what a 'patrol_information_id' actually is.
    """


def SetLockOnPoint(character: Character | int, lock_on_model_point: int, state: bool | int):
    """
    Presumably changes the point that is locked on to by the player.
    """


def Test_RequestRagdollRestraint(
    recipient_character: Character | int,
    recipient_target_rigid_index: int,
    recipient_model_point: int,
    attachment_character: Character | int,
    attachment_target_rigid_index: int,
    attachment_model_point: int,
):
    """
    TODO
    """


def ChangePlayerCharacterInitParam(character_init_param: int):
    """
    I assume this affects the player.
    """


def AdaptSpecialEffectHealthChangeToNPCPart(character: Character | int):
    """
    TODO
    """


def ImmediateActivate(character: Character | int, state: bool | int):
    """
    Not sure. Sets draw state *really* quickly?
    """


def SetCharacterTalkRange(character: Character | int, distance: float):
    """
    TODO
    """


def IncrementCharacterNewGameCycle(character: Character | int):
    """
    Interesting - apparently you can increase the NG+ level of a specific character. (No reset function, but it
    would probably reset on map reload.)
    """


def SetMultiplayerBuffs_NonBoss(character: Character | int, state: bool | int):
    """
    TODO
    """


def Unknown_2004_59(character: Character | int, state: bool | int):
    """
    Examine usage.
    """


def SetPlayerRemainingYoelLevels(level_count: int):
    """
    TODO
    """


def ExtinguishBurningObjects():
    """
    TODO
    """


def ShowObjectByMapCeremony(obj: Object | int, ceremony_id: int, unknown: int):
    """
    TODO
    """


def DestroyObject_NoSlot(obj: Object | int):
    """
    No 'slot' argument here.
    """


def DisplayDialogAndSetFlags(
    message: EventText | int,
    button_type: ButtonType | int,
    number_buttons: NumberButtons | int,
    anchor_entity: Object | Region | Character | int,
    display_distance: float,
    left_flag: Flag | int,
    right_flag: Flag | int,
    cancel_flag: Flag | int,
):
    """
    Displays a dialog and enables one of three flags, depending on the player's response. Very useful.
    """


def DisplayAreaWelcomeMessage(message: EventText | int):
    """
    Not sure what this looks like exactly.
    """


def DisplayHollowArenaMessage(message: EventText | int, unknown: int, pad_enabled: bool | int):
    """
    TODO
    """


def BanishInvaders(unknown: int):
    """
    TODO
    """


def BanishPhantomsAndUpdateServerPvPStats(unknown: int):
    """
    TODO
    """


def BanishPhantoms(unknown: int):
    """
    TODO
    """


def SetBossMusicState(sound_id: int, state: bool | int):
    """
    Not sure how this differs from the standard map sound instructions, but my guess is that it fades the music
    out rather than abruptly stopping it.
    
    TODO: Can probably be used to fade out ANY music. Not sure why it would only work for boss music.
    TODO: Argument -1 is sometimes used. Fades out ALL music?
    """


def EnableBossMusic(sound_id: int):
    """
    Calls `SetBossMusicState` with `state=True`.
    """


def DisableBossMusic(sound_id: int):
    """
    Calls `SetBossMusicState` with `state=False`.
    """


def NotifyDoorEventSoundDampening(obj: Object | int, state: DoorState | int):
    """
    No idea what this is or what entity the first argument is. Probably the door object.
    """


def SetSoundEventWithFade(sound_id: int, state: bool | int, fade_duration: float):
    """
    TODO
    """


def EnableSoundEventWithFade(sound_id: int, fade_duration: float):
    """
    Calls `SetSoundEventWithFade` with `state=True`.
    """


def DisableSoundEventWithFade(sound_id: int, fade_duration: float):
    """
    Calls `SetSoundEventWithFade` with `state=False`.
    """


def Unknown_2010_07(sound_id: int):
    """
    Unknown SoundEvent instruction.
    """


def SetCollisionResState(collision: Collision | int, state: bool | int):
    """
    No idea what this is.
    """


def ActivateCollisionAndCreateNavmesh(collision: Collision | int, state: bool | int):
    """
    TODO
    """


def SetAreaWelcomeMessageState(state: bool | int):
    """
    TODO
    """


def CreatePlayLog(name: StringOffset | int):
    """
    TODO
    """


def StartPlayLogMeasurement(measurement_id: int, name: StringOffset | int, overwrite: bool | int):
    """
    TODO
    """


def StopPlayLogMeasurement(measurement_id: int):
    """
    TODO
    """


def PlayLogParameterOutput(
    category: PlayerPlayLogParameter | int,
    name: StringOffset | int,
    output_multiplayer_state: PlayLogMultiplayerType | int,
):
    """
    TODO
    """


def EnableThisFlag():
    """
    Enables the flag ID of the current event. Does not detect slot.
    """


def DisableThisFlag():
    """
    Disables the flag ID of the current event. Does not detect slot.
    """
