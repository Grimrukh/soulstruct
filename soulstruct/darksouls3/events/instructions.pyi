"""AUTOMATICALLY GENERATED. Do not edit this module.

Import this into any EVS script to have full access to instructions.
Make sure you also do `from soulstruct.{game}.events import *` to get all enums, constants, and tests.
"""

__all__ = [
    # Basics:
    "NeverRestart",
    "RestartOnRest",
    "UnknownRestart",
    "EVENTS",
    "Condition",
    "HeldCondition",
    "END",
    "RESTART",
    "Await",
    "MAIN",
    "OR_1",
    "OR_2",
    "OR_3",
    "OR_4",
    "OR_5",
    "OR_6",
    "OR_7",
    "OR_8",
    "OR_9",
    "OR_10",
    "OR_11",
    "OR_12",
    "OR_13",
    "OR_14",
    "OR_15",
    "AND_1",
    "AND_2",
    "AND_3",
    "AND_4",
    "AND_5",
    "AND_6",
    "AND_7",
    "AND_8",
    "AND_9",
    "AND_10",
    "AND_11",
    "AND_12",
    "AND_13",
    "AND_14",
    "AND_15",
    # Built-in instructions:
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
    "IfWhiteWorldTendencyGreaterThan",
    "IfBlackWorldTendencyGreaterThan",
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
    "SkipLinesIfValueComparison",  # 1000[5]
    "SkipLinesIfValueEqual",
    "SkipLinesIfValueNotEqual",
    "SkipLinesIfValueGreaterThan",
    "SkipLinesIfValueLessThan",
    "SkipLinesIfValueGreaterThanOrEqual",
    "SkipLinesIfValueLessThanOrEqual",
    "ReturnIfValueComparison",  # 1000[6]
    "EndIfValueEqual",
    "EndIfValueNotEqual",
    "EndIfValueGreaterThan",
    "EndIfValueLessThan",
    "EndIfValueGreaterThanOrEqual",
    "EndIfValueLessThanOrEqual",
    "RestartIfValueEqual",
    "RestartIfValueNotEqual",
    "RestartIfValueGreaterThan",
    "RestartIfValueLessThan",
    "RestartIfValueGreaterThanOrEqual",
    "RestartIfValueLessThanOrEqual",
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
    "IfSteamConnectionState",  # 3[38]
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
    # Custom instructions from `compiler`:
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
    # Boolean test functions:
    "ValueComparison",
    "ValueEqual",
    "ValueNotEqual",
    "ValueGreaterThan",
    "ValueLessThan",
    "ValueGreaterThanOrEqual",
    "ValueLessThanOrEqual",
    "TimeElapsed",
    "FramesElapsed",
    "RandomTimeElapsed",
    "RandomFramesElapsed",
    "FlagState",
    "FlagEnabled",
    "FlagDisabled",
    "ThisEventFlagEnabled",
    "ThisEventFlagDisabled",
    "ThisEventSlotFlagEnabled",
    "ThisEventSlotFlagDisabled",
    "FlagRangeState",
    "FlagRangeAllEnabled",
    "FlagRangeAllDisabled",
    "FlagRangeAnyEnabled",
    "FlagRangeAnyDisabled",
    "CharacterRegionState",
    "PlayerInsideRegion",
    "PlayerOutsideRegion",
    "CharacterInsideRegion",
    "CharacterOutsideRegion",
    "EntityDistanceState",
    "PlayerWithinDistance",
    "PlayerBeyondDistance",
    "EntityWithinDistance",
    "EntityBeyondDistance",
    "PlayerItemStateExcludingStorage",
    "ActionButtonBasic",
    "MultiplayerState",
    "Host",
    "Client",
    "TryingToCreateSession",
    "TryingToJoinSession",
    "LeavingSession",
    "FailedToCreateSession",
    "AllPlayersRegionState",
    "AllPlayersInsideRegion",
    "AllPlayersOutsideRegion",
    "MapPresenceState",
    "InsideMap",
    "OutsideMap",
    "MultiplayerEvent",
    "TrueFlagCountComparison",
    "TrueFlagCountEqual",
    "TrueFlagCountNotEqual",
    "TrueFlagCountGreaterThan",
    "TrueFlagCountLessThan",
    "TrueFlagCountGreaterThanOrEqual",
    "TrueFlagCountLessThanOrEqual",
    "WorldTendencyComparison",
    "WhiteWorldTendencyComparison",
    "BlackWorldTendencyComparison",
    "WhiteWorldTendencyGreaterThan",
    "BlackWorldTendencyGreaterThan",
    "EventValueComparison",
    "EventValueEqual",
    "EventValueNotEqual",
    "EventValueGreaterThan",
    "EventValueLessThan",
    "EventValueGreaterThanOrEqual",
    "EventValueLessThanOrEqual",
    "ActionButtonBoss",
    "AnyItemDroppedInRegion",
    "ItemDropped",
    "PlayerItemStateIncludingStorage",
    "NewGameCycleComparison",
    "NewGameCycleEqual",
    "NewGameCycleNotEqual",
    "NewGameCycleGreaterThan",
    "NewGameCycleLessThan",
    "NewGameCycleGreaterThanOrEqual",
    "NewGameCycleLessThanOrEqual",
    "ActionButtonBasicLineIntersect",
    "ActionButtonBossLineIntersect",
    "EventsComparison",
    "DLCState",
    "DLCOwned",
    "DLCNotOwned",
    "OnlineState",
    "Online",
    "Offline",
    "CharacterDeathState",
    "CharacterDead",
    "CharacterAlive",
    "Attacked",
    "HealthComparison",
    "HealthEqual",
    "HealthNotEqual",
    "HealthGreaterThan",
    "HealthLessThan",
    "HealthGreaterThanOrEqual",
    "HealthLessThanOrEqual",
    "CharacterType",
    "CharacterHuman",
    "CharacterWhitePhantom",
    "CharacterHollow",
    "CharacterTargetingState",
    "CharacterTargeting",
    "CharacterNotTargeting",
    "CharacterSpecialEffectState",
    "PlayerHasSpecialEffect",
    "PlayerDoesNotHaveSpecialEffect",
    "CharacterHasSpecialEffect",
    "CharacterDoesNotHaveSpecialEffect",
    "CharacterPartHealthComparison",
    "CharacterPartHealthLessThanOrEqual",
    "CharacterBackreadState",
    "CharacterBackreadEnabled",
    "CharacterBackreadDisabled",
    "CharacterTAEEventState",
    "CharacterHasTAEEvent",
    "CharacterDoesNotHaveTAEEvent",
    "HasAIStatus",
    "SkullLanternState",
    "SkullLanternActive",
    "SkullLanternInactive",
    "PlayerClass",
    "PlayerCovenant",
    "PlayerLevelComparison",
    "PlayerLevelEqual",
    "PlayerLevelNotEqual",
    "PlayerLevelGreaterThan",
    "PlayerLevelLessThan",
    "PlayerLevelGreaterThanOrEqual",
    "PlayerLevelLessThanOrEqual",
    "HealthValueComparison",
    "HealthValueEqual",
    "HealthValueNotEqual",
    "HealthValueGreaterThan",
    "HealthValueLessThan",
    "HealthValueGreaterThanOrEqual",
    "HealthValueLessThanOrEqual",
    "ObjectDestructionState",
    "ObjectDestroyed",
    "ObjectNotDestroyed",
    "ObjectDamaged",
    "ObjectActivated",
    "ObjectHealthValueComparison",
    "PlayerMovingOnCollision",
    "PlayerRunningOnCollision",
    "PlayerStandingOnCollision",
    "AttackedWithDamageType",
    "ActionButtonParamActivated",
    "PlayerOwnWorldState",
    "PlayerInOwnWorld",
    "PlayerNotInOwnWorld",
    "MapCeremonyState",
    "MapInCeremony",
    "MapNotInCeremony",
    "MultiplayerNetworkPenalized",
    "PlayerGender",
    "OngoingCutsceneFinished",
    "HollowArenaMatchReadyState",
    "HollowArenaSoloResults",
    "HollowArenaSoloScoreComparison",
    "HollowArenaTeamResults",
    "SteamConnectionState",
    "AllyPhantomCountComparison",
    "CharacterDrawGroupState",
    "CharacterDrawGroupEnabled",
    "CharacterDrawGroupDisabled",
    "PlayerRemainingYoelLevelComparison",
    "CharacterInvadeType",
    "CharacterChameleonState",
    "ObjectBurnState",
    "ObjectBackreadState",
    "ObjectBackreadEnabled",
    "ObjectBackreadDisabled",
    "ObjectBackreadState_Alternate",
    "ActionButton",
    "PlayerHasWeapon",
    "PlayerHasArmor",
    "PlayerHasRing",
    "PlayerHasGood",
]

import typing as tp

from soulstruct.darksouls3.game_types import *
from .emevd.compiler import *
from .emevd.enums import *

# Restart decorators. They can be used as names (not function calls) or have an event ID argument.
def NeverRestart(event_id_or_func: tp.Union[tp.Callable, int]): ...
def RestartOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...
def UnknownRestart(event_id_or_func: tp.Union[tp.Callable, int]): ...

# Dummy enum for accessing event flags defined by events.
class EVENTS(Flag): ...

# Dummy class for creating conditions.
class Condition:
    def __init__(self, condition, hold: bool = False): ...

class HeldCondition:
    def __init__(self, condition): ...

# Terminators.
END = ...
RESTART = ...

# The Await function. Equivalent to using the 'await' built-in Python keyword or `MAIN.Await()`.
def Await(condition): ...

MAIN = ConditionGroup.MAIN
OR_1 = ConditionGroup.OR_1
OR_2 = ConditionGroup.OR_2
OR_3 = ConditionGroup.OR_3
OR_4 = ConditionGroup.OR_4
OR_5 = ConditionGroup.OR_5
OR_6 = ConditionGroup.OR_6
OR_7 = ConditionGroup.OR_7
OR_8 = ConditionGroup.OR_8
OR_9 = ConditionGroup.OR_9
OR_10 = ConditionGroup.OR_10
OR_11 = ConditionGroup.OR_11
OR_12 = ConditionGroup.OR_12
OR_13 = ConditionGroup.OR_13
OR_14 = ConditionGroup.OR_14
OR_15 = ConditionGroup.OR_15
AND_1 = ConditionGroup.AND_1
AND_2 = ConditionGroup.AND_2
AND_3 = ConditionGroup.AND_3
AND_4 = ConditionGroup.AND_4
AND_5 = ConditionGroup.AND_5
AND_6 = ConditionGroup.AND_6
AND_7 = ConditionGroup.AND_7
AND_8 = ConditionGroup.AND_8
AND_9 = ConditionGroup.AND_9
AND_10 = ConditionGroup.AND_10
AND_11 = ConditionGroup.AND_11
AND_12 = ConditionGroup.AND_12
AND_13 = ConditionGroup.AND_13
AND_14 = ConditionGroup.AND_14
AND_15 = ConditionGroup.AND_15


def IfConditionState(
    condition: ConditionGroup | int,
    state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    TODO
    """


def IfConditionTrue(condition: ConditionGroup | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfConditionState` with `state=True`.
    """


def IfConditionFalse(condition: ConditionGroup | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfConditionState` with `state=False`.
    """


def IfValueComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
    event_layers=(),
):
    """
    TODO
    """


def IfValueEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=0`.
    """


def IfValueNotEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=1`.
    """


def IfValueGreaterThan(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=2`.
    """


def IfValueLessThan(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=3`.
    """


def IfValueGreaterThanOrEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=4`.
    """


def IfValueLessThanOrEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=5`.
    """


def IfTimeElapsed(condition: ConditionGroup | int, seconds: float, event_layers=()):
    """
    Time since event started.
    """


def IfFramesElapsed(condition: ConditionGroup | int, frames: int, event_layers=()):
    """
    Frames since event started.
    """


def IfRandomTimeElapsed(condition: ConditionGroup | int, min_seconds: float, max_seconds: float, event_layers=()):
    """
    Not used in vanilla DS1. Requires a random amount of time since event began.
    """


def IfRandomFramesElapsed(condition: ConditionGroup | int, min_frames: int, max_frames: int, event_layers=()):
    """
    Not used in vanilla DS1. Requires a random amount of frames since event began.
    """


def IfFlagState(
    condition: ConditionGroup | int,
    state: FlagSetting | int,
    flag_type: FlagType | int,
    flag: Flag | int,
    event_layers=(),
):
    """
    TODO
    """


def IfFlagEnabled(condition: ConditionGroup | int, flag: Flag | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=0`.
    """


def IfFlagDisabled(condition: ConditionGroup | int, flag: Flag | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=0`.
    """


def IfThisEventFlagEnabled(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


def IfThisEventFlagDisabled(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


def IfThisEventSlotFlagEnabled(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


def IfThisEventSlotFlagDisabled(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


def IfFlagRangeState(
    condition: ConditionGroup | int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def IfFlagRangeAllEnabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `IfFlagRangeState` with `state=0`, `flag_type=0`.
    """


def IfFlagRangeAllDisabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `IfFlagRangeState` with `state=1`, `flag_type=0`.
    """


def IfFlagRangeAnyEnabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `IfFlagRangeState` with `state=2`, `flag_type=0`.
    """


def IfFlagRangeAnyDisabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `IfFlagRangeState` with `state=3`, `flag_type=0`.
    """


def IfCharacterRegionState(
    condition: ConditionGroup | int,
    state: bool | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    New argument with unknown purpose. Always 1 in vanilla resources. Probably for debug.
    """


def IfPlayerInsideRegion(
    condition: ConditionGroup | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfCharacterRegionState` with `state=True`, `character=10000`.
    """


def IfPlayerOutsideRegion(
    condition: ConditionGroup | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfCharacterRegionState` with `state=False`, `character=10000`.
    """


def IfCharacterInsideRegion(
    condition: ConditionGroup | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfCharacterRegionState` with `state=True`.
    """


def IfCharacterOutsideRegion(
    condition: ConditionGroup | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfCharacterRegionState` with `state=False`.
    """


def IfEntityDistanceState(
    condition: ConditionGroup | int,
    state: bool | int,
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Same new argument as region test, with unknown purpose, and again always 1 in EMEVD resources.
    """


def IfPlayerWithinDistance(
    condition: ConditionGroup | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=True`, `entity=10000`.
    """


def IfPlayerBeyondDistance(
    condition: ConditionGroup | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=False`, `entity=10000`.
    """


def IfEntityWithinDistance(
    condition: ConditionGroup | int,
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=True`.
    """


def IfEntityBeyondDistance(
    condition: ConditionGroup | int,
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=False`.
    """


def IfPlayerItemStateExcludingStorage(
    condition: ConditionGroup | int,
    item: BaseItemParam | int,
    state: bool | int,
    item_type: ItemType | int = None,
    event_layers=(),
):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


def IfActionButtonBasic(
    condition: ConditionGroup | int,
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    event_layers=(),
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Basic (not "boss") version with no line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def IfMultiplayerState(condition: ConditionGroup | int, state: MultiplayerState | int, event_layers=()):
    """
    TODO
    """


def IfHost(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=0`.
    """


def IfClient(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=1`.
    """


def IfTryingToCreateSession(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=2`.
    """


def IfTryingToJoinSession(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=3`.
    """


def IfLeavingSession(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=4`.
    """


def IfFailedToCreateSession(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=5`.
    """


def IfAllPlayersRegionState(condition: ConditionGroup | int, state: bool | int, region: Region | int, event_layers=()):
    """
    TODO
    """


def IfAllPlayersInsideRegion(condition: ConditionGroup | int, region: Region | int, event_layers=()):
    """
    Calls `IfAllPlayersRegionState` with `state=True`.
    """


def IfAllPlayersOutsideRegion(condition: ConditionGroup | int, region: Region | int, event_layers=()):
    """
    Calls `IfAllPlayersRegionState` with `state=False`.
    """


def IfMapPresenceState(
    condition: ConditionGroup | int,
    state: bool | int,
    game_map: Map | tuple | list,
    event_layers=(),
):
    """
    Conditions upon player's presence in a particular game map.
    """


def IfInsideMap(condition: ConditionGroup | int, game_map: Map | tuple | list, event_layers=()):
    """
    Calls `IfMapPresenceState` with `state=True`.
    """


def IfOutsideMap(condition: ConditionGroup | int, game_map: Map | tuple | list, event_layers=()):
    """
    Calls `IfMapPresenceState` with `state=False`.
    """


def IfMultiplayerEvent(condition: ConditionGroup | int, event_id: int, event_layers=()):
    """
    TODO
    """


def IfTrueFlagCountComparison(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    comparison_type: ComparisonType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Conditions upon a comparison with the number of enabled flags in the given range (inclusive).
    """


def IfTrueFlagCountEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=0`.
    """


def IfTrueFlagCountNotEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=1`.
    """


def IfTrueFlagCountGreaterThan(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=2`.
    """


def IfTrueFlagCountLessThan(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=3`.
    """


def IfTrueFlagCountGreaterThanOrEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=4`.
    """


def IfTrueFlagCountLessThanOrEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfTrueFlagCountComparison` with `comparison_type=5`.
    """


def IfWorldTendencyComparison(
    condition: ConditionGroup | int,
    world_tendency_type: WorldTendencyType | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    TODO
    """


def IfWhiteWorldTendencyComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=0`.
    """


def IfBlackWorldTendencyComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=1`.
    """


def IfWhiteWorldTendencyGreaterThan(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=0`, `comparison_type=2`.
    """


def IfBlackWorldTendencyGreaterThan(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=1`, `comparison_type=2`.
    """


def IfEventValueComparison(
    condition: ConditionGroup | int,
    flag: Flag | int,
    bit_count: int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    TODO
    """


def IfEventValueEqual(condition: ConditionGroup | int, flag: Flag | int, bit_count: int, value: int, event_layers=()):
    """
    Calls `IfEventValueComparison` with `comparison_type=0`.
    """


def IfEventValueNotEqual(
    condition: ConditionGroup | int,
    flag: Flag | int,
    bit_count: int,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEventValueComparison` with `comparison_type=1`.
    """


def IfEventValueGreaterThan(
    condition: ConditionGroup | int,
    flag: Flag | int,
    bit_count: int,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEventValueComparison` with `comparison_type=2`.
    """


def IfEventValueLessThan(
    condition: ConditionGroup | int,
    flag: Flag | int,
    bit_count: int,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEventValueComparison` with `comparison_type=3`.
    """


def IfEventValueGreaterThanOrEqual(
    condition: ConditionGroup | int,
    flag: Flag | int,
    bit_count: int,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEventValueComparison` with `comparison_type=4`.
    """


def IfEventValueLessThanOrEqual(
    condition: ConditionGroup | int,
    flag: Flag | int,
    bit_count: int,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEventValueComparison` with `comparison_type=5`.
    """


def IfActionButtonBoss(
    condition: ConditionGroup | int,
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    event_layers=(),
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Boss (not "basic") version with no line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def IfAnyItemDroppedInRegion(condition: ConditionGroup | int, region: Region | int, event_layers=()):
    """
    Check if any item has been dropped in the specified region. Not sensitive to what the item is.
    """


def IfItemDropped(
    condition: ConditionGroup | int,
    item: BaseItemParam | int,
    item_type: ItemType | int = None,
    event_layers=(),
):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


def IfPlayerItemStateIncludingStorage(
    condition: ConditionGroup | int,
    item: BaseItemParam | int,
    state: bool | int,
    item_type: ItemType | int = None,
    event_layers=(),
):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


def IfNewGameCycleComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    completion_count: int,
    event_layers=(),
):
    """
    TODO
    """


def IfNewGameCycleEqual(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=0`.
    """


def IfNewGameCycleNotEqual(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=1`.
    """


def IfNewGameCycleGreaterThan(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=2`.
    """


def IfNewGameCycleLessThan(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=3`.
    """


def IfNewGameCycleGreaterThanOrEqual(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=4`.
    """


def IfNewGameCycleLessThanOrEqual(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=5`.
    """


def IfActionButtonBasicLineIntersect(
    condition: ConditionGroup | int,
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    event_layers=(),
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Basic (not "boss") version with a line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def IfActionButtonBossLineIntersect(
    condition: ConditionGroup | int,
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    event_layers=(),
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Boss (not "basic") version with a line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def IfEventsComparison(
    condition: ConditionGroup | int,
    left_flag: Flag | int,
    left_bit_count: int,
    comparison_type: ComparisonType | int,
    right_flag: Flag | int,
    right_bit_count: int,
    event_layers=(),
):
    """
    Check comparison of two event flag values. Haven't bothered adding shortcut functions for this.
    """


def IfDLCState(condition: ConditionGroup | int, is_owned: bool | int, event_layers=()):
    """
    TODO
    """


def IfDLCOwned(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfDLCState` with `is_owned=True`.
    """


def IfDLCNotOwned(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfDLCState` with `is_owned=False`.
    """


def IfOnlineState(condition: ConditionGroup | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def IfOnline(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfOnlineState` with `state=True`.
    """


def IfOffline(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfOnlineState` with `state=False`.
    """


def IfCharacterDeathState(
    condition: ConditionGroup | int,
    character: Character | int,
    is_dead: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterDead(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterDeathState` with `is_dead=True`.
    """


def IfCharacterAlive(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterDeathState` with `is_dead=False`.
    """


def IfAttacked(
    condition: ConditionGroup | int,
    attacked_entity: Character | int,
    attacker: Character | int,
    event_layers=(),
):
    """
    TODO
    """


def IfHealthComparison(
    condition: ConditionGroup | int,
    character: Character | int,
    comparison_type: ComparisonType | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Conditions upon a comparison to character health ratio (0-1).
    """


def IfHealthEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthComparison` with `comparison_type=0`.
    """


def IfHealthNotEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthComparison` with `comparison_type=1`.
    """


def IfHealthGreaterThan(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthComparison` with `comparison_type=2`.
    """


def IfHealthLessThan(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthComparison` with `comparison_type=3`.
    """


def IfHealthGreaterThanOrEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthComparison` with `comparison_type=4`.
    """


def IfHealthLessThanOrEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthComparison` with `comparison_type=5`.
    """


def IfCharacterType(
    condition: ConditionGroup | int,
    character: Character | int,
    character_type: CharacterType | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterHuman(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterType` with `character_type=0`.
    """


def IfCharacterWhitePhantom(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterType` with `character_type=1`.
    """


def IfCharacterHollow(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterType` with `character_type=8`.
    """


def IfCharacterTargetingState(
    condition: ConditionGroup | int,
    targeting_character: Character | int,
    targeted_character: Character | int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterTargeting(
    condition: ConditionGroup | int,
    targeting_character: Character | int,
    targeted_character: Character | int,
    event_layers=(),
):
    """
    Calls `IfCharacterTargetingState` with `state=True`.
    """


def IfCharacterNotTargeting(
    condition: ConditionGroup | int,
    targeting_character: Character | int,
    targeted_character: Character | int,
    event_layers=(),
):
    """
    Calls `IfCharacterTargetingState` with `state=False`.
    """


def IfCharacterSpecialEffectState(
    condition: ConditionGroup | int,
    character: Character | int,
    special_effect: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfPlayerHasSpecialEffect(
    condition: ConditionGroup | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterSpecialEffectState` with `character=10000`, `state=True`.
    """


def IfPlayerDoesNotHaveSpecialEffect(
    condition: ConditionGroup | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterSpecialEffectState` with `character=10000`, `state=False`.
    """


def IfCharacterHasSpecialEffect(
    condition: ConditionGroup | int,
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterSpecialEffectState` with `state=True`.
    """


def IfCharacterDoesNotHaveSpecialEffect(
    condition: ConditionGroup | int,
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterSpecialEffectState` with `state=False`.
    """


def IfCharacterPartHealthComparison(
    condition: ConditionGroup | int,
    character: Character | int,
    npc_part_id: int,
    value: float,
    comparison_type: ComparisonType | int,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterPartHealthLessThanOrEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    npc_part_id: int,
    value: float,
    event_layers=(),
):
    """
    Calls `IfCharacterPartHealthComparison` with `comparison_type=5`.
    """


def IfCharacterBackreadState(
    condition: ConditionGroup | int,
    character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterBackreadEnabled(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterBackreadState` with `state=True`.
    """


def IfCharacterBackreadDisabled(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterBackreadState` with `state=False`.
    """


def IfCharacterTAEEventState(
    condition: ConditionGroup | int,
    character: Character | int,
    tae_event_id: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterHasTAEEvent(
    condition: ConditionGroup | int,
    character: Character | int,
    tae_event_id: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterTAEEventState` with `state=True`.
    """


def IfCharacterDoesNotHaveTAEEvent(
    condition: ConditionGroup | int,
    character: Character | int,
    tae_event_id: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterTAEEventState` with `state=False`.
    """


def IfHasAIStatus(
    condition: ConditionGroup | int,
    character: Character | int,
    ai_status: AIStatusType | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfSkullLanternState(condition: ConditionGroup | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def IfSkullLanternActive(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfSkullLanternState` with `state=True`.
    """


def IfSkullLanternInactive(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfSkullLanternState` with `state=False`.
    """


def IfPlayerClass(condition: ConditionGroup | int, class_type: ClassType | int, event_layers=()):
    """
    TODO
    """


def IfPlayerCovenant(condition: ConditionGroup | int, covenant: Covenant | int, event_layers=()):
    """
    TODO
    """


def IfPlayerLevelComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    TODO
    """


def IfPlayerLevelEqual(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=0`.
    """


def IfPlayerLevelNotEqual(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=1`.
    """


def IfPlayerLevelGreaterThan(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=2`.
    """


def IfPlayerLevelLessThan(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=3`.
    """


def IfPlayerLevelGreaterThanOrEqual(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=4`.
    """


def IfPlayerLevelLessThanOrEqual(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=5`.
    """


def IfHealthValueComparison(
    condition: ConditionGroup | int,
    character: Character | int,
    comparison_type: ComparisonType | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfHealthValueEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=0`.
    """


def IfHealthValueNotEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=1`.
    """


def IfHealthValueGreaterThan(
    condition: ConditionGroup | int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=2`.
    """


def IfHealthValueLessThan(
    condition: ConditionGroup | int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=3`.
    """


def IfHealthValueGreaterThanOrEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=4`.
    """


def IfHealthValueLessThanOrEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthValueComparison` with `comparison_type=5`.
    """


def IfObjectDestructionState(
    condition: ConditionGroup | int,
    state: bool | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfObjectDestroyed(
    condition: ConditionGroup | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfObjectDestructionState` with `state=True`.
    """


def IfObjectNotDestroyed(
    condition: ConditionGroup | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfObjectDestructionState` with `state=False`.
    """


def IfObjectDamaged(condition: ConditionGroup | int, obj: Object | int, attacker: Character | int, event_layers=()):
    """
    TODO
    """


def IfObjectActivated(condition: ConditionGroup | int, obj_act_id: int, event_layers=()):
    """
    TODO
    """


def IfObjectHealthValueComparison(
    condition: ConditionGroup | int,
    obj: Object | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    TODO
    """


def IfPlayerMovingOnCollision(condition: ConditionGroup | int, collision: Collision | int, event_layers=()):
    """
    TODO
    """


def IfPlayerRunningOnCollision(condition: ConditionGroup | int, collision: Collision | int, event_layers=()):
    """
    TODO
    """


def IfPlayerStandingOnCollision(condition: ConditionGroup | int, collision: Collision | int, event_layers=()):
    """
    TODO
    """


def AwaitConditionState(state: bool | int, condition: ConditionGroup | int, event_layers=()):
    """
    Not sure if this is ever really used over `IfConditionState`.
    """


def AwaitConditionTrue(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `AwaitConditionState` with `state=True`.
    """


def AwaitConditionFalse(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `AwaitConditionState` with `state=False`.
    """


def SkipLinesIfConditionState(line_count: int, state: bool | int, condition: ConditionGroup | int, event_layers=()):
    """
    TODO
    """


def SkipLinesIfConditionTrue(line_count: int, condition: ConditionGroup | int, event_layers=()):
    """
    Calls `SkipLinesIfConditionState` with `state=True`.
    """


def SkipLinesIfConditionFalse(line_count: int, condition: ConditionGroup | int, event_layers=()):
    """
    Calls `SkipLinesIfConditionState` with `state=False`.
    """


def ReturnIfConditionState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    TODO
    """


def EndIfConditionTrue(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfConditionState` with `event_return_type=0`, `state=True`.
    """


def EndIfConditionFalse(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfConditionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfConditionTrue(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfConditionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfConditionFalse(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfConditionState` with `event_return_type=1`, `state=False`.
    """


def SkipLines(line_count: int, event_layers=()):
    """
    Unconditional line skip.
    """


def Return(event_return_type: EventReturnType | int, event_layers=()):
    """
    TODO
    """


def End(event_layers=()):
    """
    Calls `Return` with `event_return_type=0`.
    """


def Restart(event_layers=()):
    """
    Calls `Return` with `event_return_type=1`.
    """


def SkipLinesIfValueComparison(
    line_count: int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfValueEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=0`.
    """


def SkipLinesIfValueNotEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=1`.
    """


def SkipLinesIfValueGreaterThan(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=2`.
    """


def SkipLinesIfValueLessThan(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=3`.
    """


def SkipLinesIfValueGreaterThanOrEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=4`.
    """


def SkipLinesIfValueLessThanOrEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=5`.
    """


def ReturnIfValueComparison(
    event_return_type: EventReturnType | int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
    event_layers=(),
):
    """
    TODO
    """


def EndIfValueEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=0`.
    """


def EndIfValueNotEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=1`.
    """


def EndIfValueGreaterThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=2`.
    """


def EndIfValueLessThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=3`.
    """


def EndIfValueGreaterThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=4`.
    """


def EndIfValueLessThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=5`.
    """


def RestartIfValueEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=0`.
    """


def RestartIfValueNotEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=1`.
    """


def RestartIfValueGreaterThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=2`.
    """


def RestartIfValueLessThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=3`.
    """


def RestartIfValueGreaterThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=4`.
    """


def RestartIfValueLessThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=5`.
    """


def SkipLinesIfFinishedConditionState(
    line_count: int,
    state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    This command is used instead of 1000[01] when conditions are being checked *after* they have already been
    uploaded into the MAIN condition. For example, you might want to continue MAIN if either AND(01) or AND(02)
    are true, but then afterwards, act conditionally on exactly which one of those two registers caused you to
    continue.
    """


def SkipLinesIfFinishedConditionTrue(line_count: int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `SkipLinesIfFinishedConditionState` with `state=True`.
    """


def SkipLinesIfFinishedConditionFalse(line_count: int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `SkipLinesIfFinishedConditionState` with `state=False`.
    """


def ReturnIfFinishedConditionState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    TODO
    """


def EndIfFinishedConditionTrue(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfFinishedConditionState` with `event_return_type=0`, `state=True`.
    """


def EndIfFinishedConditionFalse(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfFinishedConditionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfFinishedConditionTrue(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfFinishedConditionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfFinishedConditionFalse(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfFinishedConditionState` with `event_return_type=1`, `state=False`.
    """


def WaitForNetworkApproval(max_seconds: float, event_layers=()):
    """
    Wait for network to approve event (up to `max_seconds` seconds).
    """


def Wait(seconds: float, event_layers=()):
    """
    Wait for some number of seconds.
    """


def WaitFrames(frames: int, event_layers=()):
    """
    Wait for some number of frames.
    """


def WaitRandomSeconds(min_seconds: float, max_seconds: float, event_layers=()):
    """
    Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
    """


def WaitRandomFrames(min_frames: int, max_frames: int, event_layers=()):
    """
    Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
    """


def AwaitFlagState(state: FlagSetting | int, flag_type: FlagType | int, flag: Flag | int, event_layers=()):
    """
    Not sure if this is really used rather than `IfFlagState` with MAIN condition (0).
    """


def AwaitFlagEnabled(flag: Flag | int, event_layers=()):
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=0`.
    """


def AwaitFlagDisabled(flag: Flag | int, event_layers=()):
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=0`.
    """


def AwaitThisEventOn(event_layers=()):
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


def AwaitThisEventOff(event_layers=()):
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


def AwaitThisEventSlotOn(event_layers=()):
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


def AwaitThisEventSlotOff(event_layers=()):
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


def SkipLinesIfFlagState(
    line_count: int,
    state: FlagSetting | int,
    flag_type: FlagType | int,
    flag: Flag | int,
    event_layers=(),
):
    """
    Skip some number of lines if the specified flag (absolute, event-relative, or slot-relative) has the
    specified state.
    """


def SkipLinesIfFlagEnabled(line_count: int, flag: Flag | int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=0`.
    """


def SkipLinesIfFlagDisabled(line_count: int, flag: Flag | int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=0`.
    """


def SkipLinesIfThisEventFlagEnabled(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


def SkipLinesIfThisEventFlagDisabled(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


def SkipLinesIfThisEventSlotFlagEnabled(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


def SkipLinesIfThisEventSlotFlagDisabled(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


def ReturnIfFlagState(
    event_return_type: EventReturnType | int,
    state: FlagSetting | int,
    flag_type: FlagType | int,
    flag: Flag | int,
    event_layers=(),
):
    """
    TODO
    """


def EndIfFlagEnabled(flag: Flag | int, event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=0`.
    """


def EndIfFlagDisabled(flag: Flag | int, event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=0`.
    """


def EndIfThisEventFlagEnabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=1`, `flag=0`.
    """


def EndIfThisEventFlagDisabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=1`, `flag=0`.
    """


def EndIfThisEventSlotFlagEnabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=2`, `flag=0`.
    """


def EndIfThisEventSlotFlagDisabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=2`, `flag=0`.
    """


def RestartIfFlagEnabled(flag: Flag | int, event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=0`.
    """


def RestartIfFlagDisabled(flag: Flag | int, event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=0`.
    """


def RestartIfThisEventFlagEnabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=1`, `flag=0`.
    """


def RestartIfThisEventFlagDisabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=1`, `flag=0`.
    """


def RestartIfThisEventSlotFlagEnabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=2`, `flag=0`.
    """


def RestartIfThisEventSlotFlagDisabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=2`, `flag=0`.
    """


def SkipLinesIfFlagRangeState(
    line_count: int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfFlagRangeAllEnabled(line_count: int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=0`, `flag_type=0`.
    """


def SkipLinesIfFlagRangeAllDisabled(line_count: int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=1`, `flag_type=0`.
    """


def SkipLinesIfFlagRangeAnyEnabled(line_count: int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=2`, `flag_type=0`.
    """


def SkipLinesIfFlagRangeAnyDisabled(line_count: int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=3`, `flag_type=0`.
    """


def ReturnIfFlagRangeState(
    event_return_type: EventReturnType | int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def EndIfFlagRangeAllEnabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=0`, `flag_type=0`.
    """


def EndIfFlagRangeAllDisabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=1`, `flag_type=0`.
    """


def EndIfFlagRangeAnyEnabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=2`, `flag_type=0`.
    """


def EndIfFlagRangeAnyDisabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=3`, `flag_type=0`.
    """


def RestartIfFlagRangeAllEnabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=0`, `flag_type=0`.
    """


def RestartIfFlagRangeAllDisabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=1`, `flag_type=0`.
    """


def RestartIfFlagRangeAnyEnabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=2`, `flag_type=0`.
    """


def RestartIfFlagRangeAnyDisabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=3`, `flag_type=0`.
    """


def SkipLinesIfMapPresenceState(line_count: int, state: bool | int, game_map: Map | tuple | list, event_layers=()):
    """
    TODO
    """


def SkipLinesIfInsideMap(line_count: int, game_map: Map | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=True`.
    """


def SkipLinesIfOutsideMap(line_count: int, game_map: Map | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=False`.
    """


def ReturnIfMapPresenceState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    game_map: Map | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def EndIfInsideMap(game_map: Map | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=True`.
    """


def EndIfOutsideMap(game_map: Map | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=False`.
    """


def RestartIfInsideMap(game_map: Map | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=True`.
    """


def RestartIfOutsideMap(game_map: Map | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=False`.
    """


def AwaitObjectDestructionState(state: bool | int, obj: Object | int, event_layers=()):
    """
    TODO
    """


def AwaitObjectDestroyed(obj: Object | int, event_layers=()):
    """
    Calls `AwaitObjectDestructionState` with `state=True`.
    """


def AwaitObjectNotDestroyed(obj: Object | int, event_layers=()):
    """
    Calls `AwaitObjectDestructionState` with `state=False`.
    """


def SkipLinesIfObjectDestructionState(
    line_count: int,
    state: bool | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfObjectDestroyed(
    line_count: int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `SkipLinesIfObjectDestructionState` with `state=True`.
    """


def SkipLinesIfObjectNotDestroyed(
    line_count: int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
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
    event_layers=(),
):
    """
    TODO
    """


def EndIfObjectDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=0`, `state=True`.
    """


def EndIfObjectNotDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfObjectDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfObjectNotDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=1`, `state=False`.
    """


# Instruction `RunEvent` is manually defined in the `compiler` module.


def TerminateEvent(event_slot: int, event_id: int, event_layers=()):
    """
    Delete an instance (slot) of an event script.
    """


def SetNetworkSyncState(state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableNetworkSync(event_layers=()):
    """
    Calls `SetNetworkSyncState` with `state=True`.
    """


def DisableNetworkSync(event_layers=()):
    """
    Calls `SetNetworkSyncState` with `state=False`.
    """


def ClearMainCondition(dummy: int = 0, event_layers=()):
    """
    Likely clears all conditions currently loaded into the main condition (0).
    """


def IssuePrefetchRequest(request_id: int, event_layers=()):
    """
    No idea what this does.
    """


def SaveRequest(dummy: int = 0, event_layers=()):
    """
    Request the game to save player progress.
    """


def RunCommonEvent(event_id: int, args: tuple = (0,), arg_types: str = "", event_layers=()):
    """
    Initialize an instance of an event script from `common_func` with the given arguments.
    """


def PlayCutsceneToAll(cutscene_id: int, cutscene_flags: CutsceneFlags | int, event_layers=()):
    """
    TODO
    """


def PlayCutsceneAndMovePlayer(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    game_map: Map | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def PlayCutsceneToPlayer(cutscene_id: int, cutscene_flags: CutsceneFlags | int, player_id: int, event_layers=()):
    """
    TODO
    """


def PlayCutsceneAndMoveSpecificPlayer(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    game_map: Map | tuple | list,
    player_id: int,
    event_layers=(),
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
    event_layers=(),
):
    """
    TODO
    """


def RequestAnimation(
    entity: Character | Object | int,
    animation_id: int,
    loop: bool | int = False,
    wait_for_completion: bool | int = False,
    event_layers=(),
):
    """
    Not used very often, in favor of ForceAnimation below.
    """


def SetFlagState(flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    Enable, disable, or toggle (change) a binary flag.
    """


def EnableFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetFlagState` with `state=1`.
    """


def DisableFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetFlagState` with `state=0`.
    """


def ToggleFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetFlagState` with `state=2`.
    """


def SetSpawnerState(entity: Object | Region | Character | int, state: bool | int, event_layers=()):
    """
    e.g. the baby skeletons in Tomb of the Giants.
    """


def EnableSpawner(entity: Object | Region | Character | int, event_layers=()):
    """
    Calls `SetSpawnerState` with `state=True`.
    """


def DisableSpawner(entity: Object | Region | Character | int, event_layers=()):
    """
    Calls `SetSpawnerState` with `state=False`.
    """


def AwardItemLotToAllPlayers(item_lot_param_id: int, event_layers=()):
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
    event_layers=(),
):
    """
    The owner entity sets the 'team' of the projectile (i.e. who it can hurt).
    
    You can use this to directly spawn bullets by setting `source_entity` to `owner_entity`.
    
    Note that the angle arguments are all integers.
    """


def SetEventState(event_id: int, event_return_type: EventReturnType | int, event_slot: int = 0, event_layers=()):
    """
    Stop or restart a particular slot (default of 0) of the given event ID. Note that you cannot restart events
    that have already ended.
    """


def StopEvent(event_id: int, event_slot: int = 0, event_layers=()):
    """
    Calls `SetEventState` with `event_return_type=0`.
    Force a running event to stop.
    """


def RestartEvent(event_id: int, event_slot: int = 0, event_layers=()):
    """
    Calls `SetEventState` with `event_return_type=1`.
    
    Force a running event to restart. Note that the event must be active (i.e. not finished) for this
    to work. If you plan to have an event restarted, make sure it doesn't return until you no longer
    need it.
    """


def SetBossHealthBarState(
    character: Character | int,
    state: bool | int,
    name: NPCName | int = 0,
    bar_slot: int = 0,
    event_layers=(),
):
    """
    Note: slot number can be 0-2 in DS3.
    """


def EnableBossHealthBar(character: Character | int, name: NPCName | int = 0, bar_slot: int = 0, event_layers=()):
    """
    Calls `SetBossHealthBarState` with `state=True`.
    The character's health bar will appear at the bottom of the screen, with a name.
    """


def DisableBossHealthBar(character: Character | int, name: NPCName | int = 0, bar_slot: int = 0, event_layers=()):
    """
    Calls `SetBossHealthBarState` with `state=False`.
    
    The character's health bar will disappear from the bottom of the screen.
    
    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter,
    so only the first argument actually does anything. You're welcome to specify the name for
    clarity anyway (and vanilla events will show it when decompiled).
    """


def KillBoss(game_area_param_id: int, event_layers=()):
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


def SetNavmeshType(
    navmesh_id: NavigationEvent | int,
    navmesh_type: NavmeshType | int,
    operation: BitOperation | int,
    event_layers=(),
):
    """
    Set given navmesh type.
    """


def EnableNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int, event_layers=()):
    """
    Calls `SetNavmeshType` with `operation=0`.
    """


def DisableNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int, event_layers=()):
    """
    Calls `SetNavmeshType` with `operation=1`.
    """


def ToggleNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int, event_layers=()):
    """
    Calls `SetNavmeshType` with `operation=2`.
    """


def WarpToMap(game_map: Map | tuple | list, player_start: PlayerStart | int = -1, event_layers=()):
    """
    Warp the main player to the given player entity ID, which is in the Players tab of the MSB, in some map. By
    default, this warps to the 'default position' in the map (-1), which is the same point you would spawn at if
    the game lost track of your stable footing (e.g. in 'wrong warp' glitches).
    """


def HandleMinibossDefeat(miniboss_id: int, event_layers=()):
    """
    Called instead of `KillBoss` for bosses that aren't the final boss of the area.
    
    Note that outside of Chalice Dungeons, this is ONLY used when you have defeated Gehrman and are about to
    fight Moon Presence.
    """


def TriggerMultiplayerEvent(event_id: int, event_layers=()):
    """
    Used to make the Bell of Awakening sounds, for example.
    """


def SetRandomFlagInRange(flag_range: FlagRange | tuple | list, state: FlagSetting | int, event_layers=()):
    """
    Set the state of a random flag from a given range (inclusive).
    """


def EnableRandomFlagInRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetRandomFlagInRange` with `state=1`.
    """


def DisableRandomFlagInRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetRandomFlagInRange` with `state=0`.
    """


def ToggleRandomFlagInRange(flag_range: FlagRange | tuple | list, event_layers=()):
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
    event_layers=(),
):
    """
    Used a lot. Standard way to make a Character or Object perform an animation.
    """


def SetMapDrawParamSlot(map_area_id: int, draw_param_slot: int, event_layers=()):
    """
    Each map area (NOT each map) can have two sets of DrawParams (0 and 1), and this can be used to switch
    between them. Originally only used for Dark Anor Londo.
    
    Note that there's some funny business with how this works in m15 in Dark Souls Remastered, presumably
    because the developers didn't want to bother modifying both slots when they re-did all the DrawParams.
    """


def IncrementNewGameCycle(dummy_arg: int, event_layers=()):
    """
    This is manually called at the end of the game. You can call it anytime, but note that there is no way to
    decrement it with events.
    
    The dummy argument is always 0 or 1; not sure if or how it matters.
    """


def SetFlagRangeState(flag_range: FlagRange | tuple | list, state: FlagSetting | int, event_layers=()):
    """
    Set the state of an entire flag range (inclusive).
    """


def EnableFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetFlagRangeState` with `state=1`.
    """


def DisableFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetFlagRangeState` with `state=0`.
    """


def ToggleFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetFlagRangeState` with `state=2`.
    """


def SetRespawnPoint(respawn_point: int, event_layers=()):
    """
    Respawn point is an event set in the MSB.
    """


def RemoveItemFromPlayer(
    item: BaseItemParam | int,
    quantity: int = 0,
    item_type: ItemType | int = None,
    event_layers=(),
):
    """
    Item type is automatically detected. This instruction has a 'quantity' argument, but it seems broken, so you
    always have to remove *all* instances of the item. (Strangely, the similar command used in EzState doesn't
    seem to have this bug.)
    
    WARNING: don't confuse 'Item' with the specific item type 'Good'.
    
    item_type: Auto-detected from `item` type by default.
    """


def RemoveWeaponFromPlayer(item: BaseItemParam | int, quantity: int = 0, event_layers=()):
    """
    Calls `RemoveItemFromPlayer` with `item_type=0`.
    """


def RemoveArmorFromPlayer(item: BaseItemParam | int, quantity: int = 0, event_layers=()):
    """
    Calls `RemoveItemFromPlayer` with `item_type=1`.
    """


def RemoveRingFromPlayer(item: BaseItemParam | int, quantity: int = 0, event_layers=()):
    """
    Calls `RemoveItemFromPlayer` with `item_type=2`.
    """


def RemoveGoodFromPlayer(item: BaseItemParam | int, quantity: int = 0, event_layers=()):
    """
    Calls `RemoveItemFromPlayer` with `item_type=3`.
    """


def PlaceSummonSign(
    sign_type: SummonSignType | int,
    character: Character | int,
    region: Region | int,
    summon_flag: Flag | int,
    dismissal_flag: Flag | int,
    event_layers=(),
):
    """
    If you set a black summon sign, the specified NPC will try to invade automatically.
    """


def SetSoapstoneMessageState(message_id: int, state: bool | int, event_layers=()):
    """
    Enable or disable developer message.
    """


def EnableSoapstoneMessage(message_id: int, event_layers=()):
    """
    Calls `SetSoapstoneMessageState` with `state=True`.
    """


def DisableSoapstoneMessage(message_id: int, event_layers=()):
    """
    Calls `SetSoapstoneMessageState` with `state=False`.
    """


def AwardAchievement(achievement_id: int, event_layers=()):
    """
    For obvious reasons, I *highly* discourage you from abusing this, except in the interest of maintaining the
    accessibility of existing achievements. This interacts with Steam, which is always dangerous.
    """


def SetVagrantSpawningState(spawning_disabled: bool | int, event_layers=()):
    """
    Note inverted bool.
    """


def EnableVagrantSpawning(event_layers=()):
    """
    Calls `SetVagrantSpawningState` with `spawning_disabled=False`.
    """


def DisableVagrantSpawning(event_layers=()):
    """
    Calls `SetVagrantSpawningState` with `spawning_disabled=True`.
    """


def IncrementEventValue(flag: Flag | int, bit_count: int, max_value: int, event_layers=()):
    """
    You can use a contiguous array of flags as a single value. Use this to increment that value by 1.
    
    The array begins at `flag` and extends for `bit_count`. For example, a 'bit_count' of 8 gives you a
    theoretical maximum of 256. You can set a 'max_value' less than that to limit the value. (I'm not sure if it
    ticks over back to zero if `max_value` is greater than the possible value given the bit count.)
    
    The most significant bit is represented at `flag`, and the least significant bit at `flag + bit_count - 1`.
    
    This is used for counters in the vanilla game, such as the number of bosses killed while Rhea is at Undead
    Parish.
    """


def ClearEventValue(flag: Flag | int, bit_count: int, event_layers=()):
    """
    Clears the given multi-flag. This is basically like disabling `bit_count` flags in a row, starting at
    `flag`.
    """


def SetNextSnugglyTrade(flag: Flag | int, event_layers=()):
    """
    Sets the flag for the next drop based on the item you deposit into the nest.
    """


def SnugglyItemDrop(
    item_lot: ItemLotParam | int,
    region: Region | int,
    flag: Flag | int,
    collision: Collision | int,
    event_layers=(),
):
    """
    Makes Snuggly drop an item. There are complex limitations to this in the engine, so be careful. (The list of
    available Snuggly flags is a hard-coded limit, for example.)
    """


def MoveRemains(source_region: Region | int, destination_region: Region | int, event_layers=()):
    """
    Move all bloodstains and dropped items from one region to another (I assume). Used to move your
    remains out of Gwyndolin's endless corridor.
    """


def AwardItemLotToHostOnly(item_lot_param_id: int, event_layers=()):
    """
    You can simply call AwardItemLot() with the same argument, which will redirect here, as you'll almost never
    *not* want to award an item lot to the host only.
    """


def ArenaRankingRequest1v1(event_layers=()):
    """
    TODO
    """


def ArenaRankingRequest2v2(event_layers=()):
    """
    TODO
    """


def ArenaRankingRequestFFA(event_layers=()):
    """
    TODO
    """


def ArenaExitRequest(event_layers=()):
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
    event_layers=(),
):
    """
    Performs a binary operation on the source flag and operand value, and stores the result in the target flag.
    """


def SetAIState(character: Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableAI(character: Character | int, event_layers=()):
    """
    Calls `SetAIState` with `state=True`.
    """


def DisableAI(character: Character | int, event_layers=()):
    """
    Calls `SetAIState` with `state=False`.
    """


def SetTeamType(character: Character | int, new_team: TeamType | int, event_layers=()):
    """
    TODO
    """


def MoveToEntity(
    character: Character | int,
    destination: Object | Region | Character | int,
    model_point: int = -1,
    destination_type: CoordEntityType | int = None,
    event_layers=(),
):
    """
    Basic move. I recommend you use the combined `Move` function.
    destination_type: Auto-detected from `destination` type by default.
    """


def Kill(character: Character | int, award_souls: bool | int = False, event_layers=()):
    """
    Technically a kill 'request.'
    """


def SetCharacterState(character: Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableCharacter(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterState` with `state=True`.
    """


def DisableCharacter(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterState` with `state=False`.
    """


def EzstateAIRequest(character: Character | int, command_id: int, command_slot: int, event_layers=()):
    """
    Slot number ranges from 0 to 3.
    """


def CreateProjectileOwner(entity: Object | Region | Character | int, event_layers=()):
    """
    A 'bullet owner' that will spawn things according to the Spawner section of the MSB.
    """


def AddSpecialEffect(character: Character | int, special_effect_id: int, event_layers=()):
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
    event_layers=(),
):
    """
    Sets entity's default standby animations. -1 is default for each category.
    """


def ResetStandbyAnimationSettings(character: Character | int, event_layers=()):
    """
    Calls `SetStandbyAnimationSettings` with `standby_animation=-1`, `damage_animation=-1`, `cancel_animation=-1`,
    `death_animation=-1`, `standby_exit_animation=1`.
    """


def SetGravityState(character: Character | int, state: bool | int, event_layers=()):
    """
    Simply determines if the character loses height as it moves around. They will still gain height by running
    up slopes.
    """


def EnableGravity(character: Character | int, event_layers=()):
    """
    Calls `SetGravityState` with `state=True`.
    """


def DisableGravity(character: Character | int, event_layers=()):
    """
    Calls `SetGravityState` with `state=False`.
    """


def SetCharacterEventTarget(character: Character | int, region: Region | int, event_layers=()):
    """
    Likely refers to patrolling behavior.
    """


def SetImmortalityState(character: Character | int, state: bool | int, event_layers=()):
    """
    Character will take damage, but not die (i.e. cannot go below 1 HP).
    """


def EnableImmortality(character: Character | int, event_layers=()):
    """
    Calls `SetImmortalityState` with `state=True`.
    """


def DisableImmortality(character: Character | int, event_layers=()):
    """
    Calls `SetImmortalityState` with `state=False`.
    """


def SetNest(character: Character | int, region: Region | int, event_layers=()):
    """
    Home point for entity AI.
    """


def RotateToFaceEntity(
    character: Character | int,
    target_entity: Object | Region | Character | int,
    animation: int = -1,
    wait_for_completion: bool | int = False,
    event_layers=(),
):
    """
    Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at
    least.)
    
    The Bloodborne+ version allows you to force an animation at the same time (post-rotation) and optionally
    wait until that animation is completed. (I assume a value of -1 avoids it.)
    """


def SetInvincibilityState(character: Character | int, state: bool | int, event_layers=()):
    """
    Character cannot take damage or die.
    """


def EnableInvincibility(character: Character | int, event_layers=()):
    """
    Calls `SetInvincibilityState` with `state=True`.
    """


def DisableInvincibility(character: Character | int, event_layers=()):
    """
    Calls `SetInvincibilityState` with `state=False`.
    """


def ClearTargetList(character: Character | int, event_layers=()):
    """
    Clear list of targets from character AI.
    """


def AICommand(character: Character | int, command_id: int, command_slot: int, event_layers=()):
    """
    The given `command_id` can be accessed in AI Lua scripts with `ai:GetEventRequest(slot)`.
    """


def SetEventPoint(character: Character | int, region: Region | int, reaction_range: float, event_layers=()):
    """
    Not sure what the usage of this is, but it is likely used to change patrol behavior.
    """


def SetAIParamID(character: Character | int, ai_param_id: int, event_layers=()):
    """
    Change character's AI parameter index.
    """


def ReplanAI(character: Character | int, event_layers=()):
    """
    Clear current AI goal list and force character to replan it.
    """


def CancelSpecialEffect(character: Character | int, special_effect_id: int, event_layers=()):
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
    event_layers=(),
):
    """
    Complex. Sets specific damage parameters for part of an NPC model. Further changes to the specific part can
    be made using the events below. The part is specified using the NPCPartType slot. Look at usage in tail cut
    events to understand these more.
    """


def SetNPCPartHealth(
    character: Character | int,
    npc_part_id: int,
    desired_health: int,
    overwrite_max: bool | int,
    event_layers=(),
):
    """
    You must create the part first.
    """


def SetNPCPartEffects(
    character: Character | int,
    npc_part_id: int,
    material_sfx_id: int,
    material_vfx_id: int,
    event_layers=(),
):
    """
    Attach material effects to an NPC part.
    """


def SetNPCPartBulletDamageScaling(
    character: Character | int,
    npc_part_id: int,
    desired_scaling: float,
    event_layers=(),
):
    """
    Scale the damage dealt to the part. Usually used to set damage to zero, e.g. Smough's hammer.
    """


def SetDisplayMask(character: Character | int, bit_index: int, switch_type: OnOffChange | int, event_layers=()):
    """
    Different bits correspond to different parts of the character model. You can see the initial values for
    these in the NPC params. This is generally used to disable tails when they are cut off.
    
    `switch_type` can be 0 (off), 1 (on), or 2 (change).
    """


def SetCollisionMask(character: Character | int, bit_index: int, switch_type: OnOffChange | int, event_layers=()):
    """
    See above. This affects the NPC's Collision, not appearance.
    """


def SetNetworkUpdateAuthority(character: Character | int, authority_level: UpdateAuthority | int, event_layers=()):
    """
    Complex; look at existing usage. Authority level must be 'Normal' or 'Forced'.
    """


def SetBackreadState(character: Character | int, remove: bool | int, event_layers=()):
    """
    I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread'
    of a character has a larger effect on game resources. It is used, for example, to disable the Fair Lady and
    Eingyi during the Demon Firesage boss fight.
    
    Also note reversed bool.
    """


def EnableBackread(character: Character | int, event_layers=()):
    """
    Calls `SetBackreadState` with `remove=False`.
    """


def DisableBackread(character: Character | int, event_layers=()):
    """
    Calls `SetBackreadState` with `remove=True`.
    """


def SetHealthBarState(character: Character | int, state: bool | int, event_layers=()):
    """
    Normal health bar that appears above character.
    """


def EnableHealthBar(character: Character | int, event_layers=()):
    """
    Calls `SetHealthBarState` with `state=True`.
    """


def DisableHealthBar(character: Character | int, event_layers=()):
    """
    Calls `SetHealthBarState` with `state=False`.
    """


def SetCharacterCollisionState(character: Character | int, is_disabled: bool | int, event_layers=()):
    """
    Note that the bool is inverted from what you might expect.
    """


def EnableCharacterCollision(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterCollisionState` with `is_disabled=False`.
    """


def DisableCharacterCollision(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterCollisionState` with `is_disabled=True`.
    """


def AIEvent(
    character: Character | int,
    command_id: int,
    command_slot: int,
    first_event_flag: Flag | int,
    last_event_flag: Flag | int,
    event_layers=(),
):
    """
    I have no idea what this does.
    """


def ReferDamageToEntity(character: Character | int, target_entity: Character | int, event_layers=()):
    """
    All damage dealt to the first character will *also* (not *only*) be dealt to the target entity. I'm not 100%
    sure if the target entity can be an Object.
    
    Only used by the Four Kings in the vanilla game.
    """


def SetNetworkUpdateRate(
    character: Character | int,
    is_fixed: bool | int,
    update_rate: CharacterUpdateRate | int,
    event_layers=(),
):
    """
    Not sure what 'is_fixed' does. I believe only 'Always' and 'Never' are used in the vanilla game.
    """


def SetBackreadStateAlternate(character: Character | int, state: bool | int, event_layers=()):
    """
    I have no idea how this differs from the standard backread function above.
    """


def HellkiteBreathControl(character: Character | int, obj: Object | int, animation_id: int, event_layers=()):
    """
    I don't recommend you mess with this. It seems to be used to create the fire VFX and damaging effect when
    the Hellkite breathes fire on the bridge, with (otherwise invisible) object model o1060. It may simply
    trigger a certain behavior param ID.
    
    Unclear whether the animation applies to the character or object (which is probably an invisible "burning"
    plane).
    """


def DropMandatoryTreasure(character: Character | int, event_layers=()):
    """
    This will disable the character and spawn any treasure they would drop. It's possible that it only spawns
    treasure that has a 100% drop rate, hence the name, but I haven't confirmed this.
    """


def BetrayCurrentCovenant(dummy: int = 0, event_layers=()):
    """
    Dummy argument does nothing.
    """


def SetAnimationsState(entity: Character | Object | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableAnimations(entity: Character | Object | int, event_layers=()):
    """
    Calls `SetAnimationsState` with `state=True`.
    """


def DisableAnimations(entity: Character | Object | int, event_layers=()):
    """
    Calls `SetAnimationsState` with `state=False`.
    """


def MoveAndSetDrawParent(
    character: Character | int,
    destination: Object | Region | Character | int,
    set_draw_parent: MapPart | int,
    model_point: int = -1,
    destination_type: CoordEntityType | int = None,
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


def ResetAnimation(character: Character | int, disable_interpolation: bool | int = False, event_layers=()):
    """
    Cancels an animation. Note the inverted bool for controlling interpolation.
    """


def SetTeamTypeAndExitStandbyAnimation(character: Character | int, team_type: TeamType | int, event_layers=()):
    """
    Two for the price of one. Often used when NPCs with resting animations become hostile.
    """


def HumanityRegistration(character: Character | int, event_flag: Flag | int, event_layers=()):
    """
    I believe this designates the first event flag in a range of eight, which tracks how much humanity an NPC
    has for draining with Dark Hand. These flags are all in the 8000 range, and tightly packed, so you'll need
    to find your own range if you want to replicate this.
    
    I can confirm that NOT doing this for a new NPC means you can't drain any humanity from them, rather than
    being able to drain unlimited humanity.
    """


def IncrementPvPSin(dummy: int = 0, event_layers=()):
    """
    Normally only happens when you kill an NPC.
    """


def EqualRecovery(event_layers=()):
    """
    Unknown effect. Only used in Battle of Stoicism, so likely useless to you.
    """


def DestroyObject(obj: Object | int, request_slot: int = 1, event_layers=()):
    """
    Technically 'requests' the object's destruction. No idea what the slot number does.
    """


def RestoreObject(obj: Object | int, event_layers=()):
    """
    The opposite of destruction. Restores it to its original MSB coordinates.
    """


def SetObjectState(obj: Object | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableObject(obj: Object | int, event_layers=()):
    """
    Calls `SetObjectState` with `state=True`.
    """


def DisableObject(obj: Object | int, event_layers=()):
    """
    Calls `SetObjectState` with `state=False`.
    """


def SetTreasureState(obj: Object | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableTreasure(obj: Object | int, event_layers=()):
    """
    Calls `SetTreasureState` with `state=True`.
    Enables any treasure attached to this object by MSB events.
    """


def DisableTreasure(obj: Object | int, event_layers=()):
    """
    Calls `SetTreasureState` with `state=False`.
    
    Disables any treasure attached to this object by MSB events.
    
    If you want to disable treasure by default, you can do it in the MSB by changing a certain event
    value to 255.
    """


def ActivateObject(obj: Object | int, obj_act_id: int, relative_index: int, event_layers=()):
    """
    Manually call a specific ObjAct event attached to this object. I believe 'relative_index' refers to the
    points on the object at which it can be activated (e.g. which side of a gate you are on).
    
    Note that this will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how
    the game gets Patches to pull the lever in the Catacombs.
    """


def SetObjectActivation(obj: Object | int, obj_act_id: int, state: bool | int, event_layers=()):
    """
    Sets whether the object can be activated (1) or not activated (0).
    """


def EndOfAnimation(obj: Object | int, animation_id: int, event_layers=()):
    """
    Sets entity to whatever state it would have after the given animation. Used often to open doors that have
    already been opened when you reload the map, etc. I doubt it can be used with characters, but haven't
    confirmed.
    """


def PostDestruction(obj: Object | int, request_slot: int = 1, event_layers=()):
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
    event_layers=(),
):
    """
    Turn an object into an environmental hazard. It deals damage when touched according to the NPC Behavior
    params you give it. The model_point determines which part of the object is hazardous (with the given radius
    and life, relative to the time this instruction occurs).
    
    An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.
    
    'target_type' determines what the hazard can damage (Character and/or Map).
    """


def RegisterStatue(obj: Object | int, game_map: Map | tuple | list, statue_type: StatueType | int, event_layers=()):
    """
    Creates a petrified or crystallized statue. I believe this is so it can be seen by other players online.
    """


def MoveObjectToCharacter(obj: Object | int, character: Character | int, model_point: int = -1, event_layers=()):
    """
    Move an object to a character.
    """


def RemoveObjectFlag(obj_flag: Flag | int, event_layers=()):
    """
    No idea what this does. I believe it might undo the CreateHazard instruction, at least.
    """


def SetObjectInvulnerabilityState(obj: Object | int, state: bool | int, event_layers=()):
    """
    1 = invulnerable.
    """


def EnableObjectInvulnerability(obj: Object | int, event_layers=()):
    """
    Calls `SetObjectInvulnerabilityState` with `state=True`.
    """


def DisableObjectInvulnerability(obj: Object | int, event_layers=()):
    """
    Calls `SetObjectInvulnerabilityState` with `state=False`.
    """


def SetObjectActivationWithIdx(
    obj: Object | int,
    obj_act_id: int,
    relative_index: int,
    state: bool | int,
    event_layers=(),
):
    """
    Similar to SetObjectActivation, but you can provide the relative index to disable (e.g. one side of a door).
    """


def EnableTreasureCollection(obj: Object | int, event_layers=()):
    """
    Forces an object to spawn its treasure, even if the treasure's ItemLot flag is already enabled.
    
    Useful if you want some treasure to reappear (after, say, taking it from the player and disabling the
    ItemLot flag) without the player needing to reload the map.
    """


def DeleteVFX(vfx_id: VFXEvent | int, erase_root_only: bool = True, event_layers=()):
    """
    Delete visual VFX. If 'erase_root_only' is True (default), effect particles already emitted will live out
    the rest of their lifetimes (e.g. making a fog gate disappear organically). The ID is given in the MSB.
    """


def CreateVFX(vfx_id: VFXEvent | int, event_layers=()):
    """
    Create visual VFX. The ID is given in the MSB (e.g. fog effect for boss gates and checkpoints).
    """


def CreateTemporaryVFX(
    vfx_id: int,
    anchor_entity: Object | Region | Character | int,
    model_point: int = -1,
    anchor_type: CoordEntityType | int = None,
    event_layers=(),
):
    """
    Create one-off visual VFX (an FFX ID) attached to the given 'anchor_entity'. The VFX, of course, must be
    currently loaded (or in common effects).
    
    anchor_type: Auto-detected from `anchor_entity` type by default. Sets `Character` type for `PLAYER`.
    """


def CreateObjectVFX(obj: Object | int, vfx_id: int, model_point: int, event_layers=()):
    """
    TODO
    """


def DeleteObjectVFX(obj: Object | int, erase_root: bool = True, event_layers=()):
    """
    Note `erase_root` vs. `erase_root_only` for map SFX.
    """


def DisplayDialog(
    text: EventText | int,
    anchor_entity: Object | Region | Character | int = -1,
    display_distance: float = 3.0,
    button_type: ButtonType | int = ButtonType.OK_or_Cancel,
    number_buttons: NumberButtons | int = NumberButtons.NoButton,
    event_layers=(),
):
    """
    Display a dialog box at the bottom of the screen. You can't use this to get player input, but you can
    display short simple messages. It defaults to a box with no buttons (which is still dismissed when you press
    A).
    
    The 'display_distance' argument specifies how far you can move away from the 'anchor_entity' before the
    message automatically disappears. If `anchor_entity=-1` (default), some kind of default anchor is used
    (probably just the position where the player was standing).
    """


def DisplayBanner(banner_type: BannerType | int, event_layers=()):
    """
    Display a pre-rendered banner. You'll have to change the textures (in menu_local.tpf) to change them.
    """


def DisplayStatus(text: EventText | int, pad_enabled: bool = True, event_layers=()):
    """
    Displays a large message that appears at the top of the screen, such as the message that tells you how to
    remove your curse, or that the golden fog gates block your path. If 'pad_enabled' is False, you can't get
    rid of the message until it times out on its own.
    """


def DisplayBattlefieldMessage(text: EventText | int, display_location_index: int, event_layers=()):
    """
    Displays a flashing messages at the bottom of the screen that does not block player input.
    """


def ArenaSetNametag1(player_id: int, event_layers=()):
    """
    TODO
    """


def ArenaSetNametag2(player_id: int, event_layers=()):
    """
    TODO
    """


def ArenaSetNametag3(player_id: int, event_layers=()):
    """
    TODO
    """


def ArenaSetNametag4(player_id: int, event_layers=()):
    """
    TODO
    """


def DisplayArenaDissolutionMessage(text: EventText | int, event_layers=()):
    """
    TODO
    """


def ChangeCamera(normal_camera_id: int, locked_camera_id: int, event_layers=()):
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
    event_layers=(),
):
    """
    TODO
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


def SetLockedCameraSlot(game_map: Map | tuple | list, camera_slot: int, event_layers=()):
    """
    Switch between one of two camera slots associated with the player's current collision in the MSB.
    """


def RegisterLadder(start_climbing_flag: Flag | int, stop_climbing_flag: Flag | int, obj: Object | int, event_layers=()):
    """
    Don't mess with these flags, generally; you can just delay when this is called after map load to disable
    certain ladders (which is kind of weird anyway).
    """


def InitializeWanderingDemon(
    flag: Flag | int,
    demon_entity: Character | int,
    appearance_flag: Flag | int,
    event_layers=(),
):
    """
    Unused. Probably a Demon's Souls remnant.
    """


def RegisterWanderingDemon(
    flag: Flag | int,
    demon_entity: Character | int,
    unknown_entity: Object | Region | Character | int,
    event_layers=(),
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
    event_layers=(),
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


def ActivateMultiplayerBuffs(character: Character | int, event_layers=()):
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
    event_layers=(),
):
    """
    No idea what this is. Apparently DS1 also has a version of this with less arguments.
    """


def NotifyBossBattleStart(dummy: int = 0, event_layers=()):
    """
    Sends the message to all summons that the host has challenged the boss.
    """


def SetBackgroundMusic(
    state: bool | int,
    music_slot: int,
    entity: Object | Region | Character | int,
    sound_type: SoundType | int,
    sound_id: int,
    event_layers=(),
):
    """
    TODO
    """


def PlaySoundEffect(
    anchor_entity: Object | Region | Character | int,
    sound_id: int,
    sound_type: SoundType | int = None,
    event_layers=(),
):
    """
    Anchor entity determines sound position and the sound type is used to look up the source.
    """


def SetSoundEventState(sound_id: int, state: bool | int, event_layers=()):
    """
    The sound ID is in the MSB. Includes boss music, which is obviously the most common use, and ambiance.
    """


def EnableSoundEvent(sound_id: int, event_layers=()):
    """
    Calls `SetSoundEventState` with `state=True`.
    """


def DisableSoundEvent(sound_id: int, event_layers=()):
    """
    Calls `SetSoundEventState` with `state=False`.
    """


def SetMapCollisionState(collision: Collision | int, state: bool | int, event_layers=()):
    """
    Enable or disable a map collision (HKX). The ID is specified in the MSB. Note that a Collision doesn't have
    to be solid ground, but could be anything triggered by collision, such as a kill plane (which this is often
    used to disable).
    """


def EnableMapCollision(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionState` with `state=True`.
    """


def DisableMapCollision(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionState` with `state=False`.
    """


def SetMapCollisionBackreadMaskState(collision: Collision | int, state: bool | int, event_layers=()):
    """
    Unused.
    """


def EnableMapCollisionBackreadMask(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionBackreadMaskState` with `state=True`.
    """


def DisableMapCollisionBackreadMask(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionBackreadMaskState` with `state=False`.
    """


def SetMapPieceState(map_piece_id: MapPiece | int, state: bool | int, event_layers=()):
    """
    Set the visibility of individual map pieces (e.g. all the crystals in Seath's tower).
    """


def EnableMapPiece(map_piece_id: MapPiece | int, event_layers=()):
    """
    Calls `SetMapPieceState` with `state=True`.
    """


def DisableMapPiece(map_piece_id: MapPiece | int, event_layers=()):
    """
    Calls `SetMapPieceState` with `state=False`.
    """


def IfAttackedWithDamageType(
    condition: ConditionGroup | int,
    attacked_entity: Character | int,
    attacker: Character | int = -1,
    damage_type: DamageType | int = DamageType.Unspecified,
    event_layers=(),
):
    """
    TODO
    """


def IfActionButtonParamActivated(
    condition: ConditionGroup | int,
    action_button_id: int,
    entity: Object | Region | Character | int,
    event_layers=(),
):
    """
    TODO
    """


def IfPlayerOwnWorldState(condition: ConditionGroup | int, not_in_own_world: bool | int, event_layers=()):
    """
    Excluding Arena.
    """


def IfPlayerInOwnWorld(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfPlayerOwnWorldState` with `not_in_own_world=False`.
    """


def IfPlayerNotInOwnWorld(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfPlayerOwnWorldState` with `not_in_own_world=True`.
    """


def IfMapCeremonyState(
    condition: ConditionGroup | int,
    state: bool | int,
    game_map: Map | tuple | list,
    ceremony_id: int,
    event_layers=(),
):
    """
    Ceremony states are unused except for Untended Graves, I believe.
    """


def IfMapInCeremony(condition: ConditionGroup | int, game_map: Map | tuple | list, ceremony_id: int, event_layers=()):
    """
    Calls `IfMapCeremonyState` with `state=True`.
    """


def IfMapNotInCeremony(
    condition: ConditionGroup | int,
    game_map: Map | tuple | list,
    ceremony_id: int,
    event_layers=(),
):
    """
    Calls `IfMapCeremonyState` with `state=False`.
    """


def IfMultiplayerNetworkPenalized(condition: ConditionGroup | int, event_layers=()):
    """
    TODO
    """


def IfPlayerGender(condition: ConditionGroup | int, gender: Gender | int, event_layers=()):
    """
    Note that this condition version of the gender test was absent in Bloodborne.
    """


def IfOngoingCutsceneFinished(condition: ConditionGroup | int, cutscene_id: int, event_layers=()):
    """
    TODO
    """


def IfHollowArenaMatchReadyState(condition: ConditionGroup | int, is_ready: bool | int, event_layers=()):
    """
    TODO
    """


def IfHollowArenaSoloResults(condition: ConditionGroup | int, result: HollowArenaResult | int, event_layers=()):
    """
    TODO
    """


def IfHollowArenaSoloScoreComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    value: int,
    unknown: int,
    event_layers=(),
):
    """
    Unknown fourth argument.
    """


def IfHollowArenaTeamResults(condition: ConditionGroup | int, result: HollowArenaResult | int, event_layers=()):
    """
    TODO
    """


def IfSteamConnectionState(condition: ConditionGroup | int, is_disconnected: bool | int, event_layers=()):
    """
    TODO
    """


def IfAllyPhantomCountComparison(
    condition: ConditionGroup | int,
    comparison_state: bool | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Note that there's a 'comparison_state' bool that can be used to invert the operation (kind of pointless).
    """


def IfCharacterDrawGroupState(
    condition: ConditionGroup | int,
    character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Tests if character's draw group is currently enabled or disabled.
    """


def IfCharacterDrawGroupEnabled(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterDrawGroupState` with `state=True`.
    """


def IfCharacterDrawGroupDisabled(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterDrawGroupState` with `state=False`.
    """


def IfPlayerRemainingYoelLevelComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Tests the number of remaining levels available from Yoel, I presume.
    """


def IfCharacterInvadeType(
    condition: ConditionGroup | int,
    character: Character | int,
    invade_type: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    'invade_type' has an unknown type in the EMEDF. Probably refers to the invader's covenant.
    """


def IfCharacterChameleonState(
    condition: ConditionGroup | int,
    character: Character | int,
    chameleon_vfx_id: int,
    is_transformed: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def IfObjectBurnState(
    condition: ConditionGroup | int,
    obj: Object | int,
    comparison_type: ComparisonType | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    This test is used exactly once, in the High Wall of Lothric, where the 'comparison_type' is GreaterThan. I
    have no idea what that argument does. However, it's possible that 'state' isn't actually a bool, but some
    measure of the intensity of the burn state, because the event it's used in strongly suggests that a fire
    effect is created as long as the burn state is 'greater than zero'.
    """


def IfObjectBackreadState(
    condition: ConditionGroup | int,
    obj: Object | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfObjectBackreadEnabled(
    condition: ConditionGroup | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfObjectBackreadState` with `state=True`.
    """


def IfObjectBackreadDisabled(
    condition: ConditionGroup | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfObjectBackreadState` with `state=False`.
    """


def IfObjectBackreadState_Alternate(
    condition: ConditionGroup | int,
    obj: Object | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    The fact they added this suggests that the 'alternate' version that already existed for characters is
    actually useful in some way (and they did use it in DS1).
    """


def GotoIfConditionState(
    label: Label | int,
    required_state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    TODO
    """


def GotoIfConditionTrue(label: Label | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `GotoIfConditionState` with `required_state=True`.
    """


def GotoIfConditionFalse(label: Label | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `GotoIfConditionState` with `required_state=False`.
    """


def Goto(label: Label | int, event_layers=()):
    """
    Unconditional GOTO.
    """


def GotoIfValueComparison(
    label: Label | int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
    event_layers=(),
):
    """
    TODO
    """


def GotoIfFinishedConditionState(
    label: Label | int,
    required_state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    Finished version.
    """


def GotoIfFinishedConditionTrue(label: Label | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `GotoIfFinishedConditionState` with `required_state=True`.
    """


def GotoIfFinishedConditionFalse(label: Label | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `GotoIfFinishedConditionState` with `required_state=False`.
    """


def WaitHollowArenaHalftime(match_type: HollowArenaMatchType | int, is_second_half: bool | int, event_layers=()):
    """
    'StayParam lookup'.
    """


def SkipLinesIfMultiplayerState(line_count: int, state: MultiplayerState | int, event_layers=()):
    """
    TODO
    """


def SkipLinesIfHost(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=0`.
    """


def SkipLinesIfClient(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=1`.
    """


def SkipLinesIfTryingToCreateSession(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=2`.
    """


def SkipLinesIfTryingToJoinSession(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=3`.
    """


def SkipLinesIfLeavingSession(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=4`.
    """


def SkipLinesIfFailedToCreateSession(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=5`.
    """


def ReturnIfMultiplayerState(event_return_type: EventReturnType | int, state: MultiplayerState | int, event_layers=()):
    """
    TODO
    """


def EndIfHost(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=0`.
    """


def EndIfClient(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=1`.
    """


def EndIfTryingToCreateSession(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=2`.
    """


def EndIfTryingToJoinSession(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=3`.
    """


def EndIfLeavingSession(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=4`.
    """


def EndIfFailedToCreateSession(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=5`.
    """


def RestartIfHost(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=0`.
    """


def RestartIfClient(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=1`.
    """


def RestartIfTryingToCreateSession(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=2`.
    """


def RestartIfTryingToJoinSession(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=3`.
    """


def RestartIfLeavingSession(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=4`.
    """


def RestartIfFailedToCreateSession(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=5`.
    """


def SkipLinesIfCoopClientCountComparison(
    skip_lines: int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Value should be from 0 to 4.
    """


def ReturnIfCoopClientCountComparison(
    event_return_type: EventReturnType | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    TODO
    """


def EndIfCoopClientCountComparison(comparison_type: ComparisonType | int, value: int, event_layers=()):
    """
    Calls `ReturnIfCoopClientCountComparison` with `event_return_type=0`.
    """


def RestartIfCoopClientCountComparison(comparison_type: ComparisonType | int, value: int, event_layers=()):
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
    event_layers=(),
):
    """
    Note that 'target_count' is now an integer again...
    """


def GotoIfPlayerHasSpecialEffect(
    label: Label | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `GotoIfCharacterSpecialEffectState` with `character=10000`, `state=True`.
    """


def GotoIfPlayerDoesNotHaveSpecialEffect(
    label: Label | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
):
    """
    Calls `GotoIfCharacterSpecialEffectState` with `state=False`.
    """


def GotoIfPlayerOwnWorldState(label: Label | int, not_in_own_world: bool | int, event_layers=()):
    """
    TODO
    """


def GotoIfPlayerInOwnWorld(label: Label | int, event_layers=()):
    """
    Calls `GotoIfPlayerOwnWorldState` with `not_in_own_world=False`.
    """


def GotoIfPlayerNotInOwnWorld(label: Label | int, event_layers=()):
    """
    Calls `GotoIfPlayerOwnWorldState` with `not_in_own_world=True`.
    """


def ReturnIfPlayerOwnWorldState(
    event_return_type: EventReturnType | int,
    not_in_own_world: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def EndIfPlayerInOwnWorld(event_layers=()):
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=0`, `not_in_own_world=False`.
    """


def EndIfPlayerNotInOwnWorld(event_layers=()):
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=0`, `not_in_own_world=True`.
    """


def RestartIfPlayerInOwnWorld(event_layers=()):
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=1`, `not_in_own_world=False`.
    """


def RestartIfPlayerNotInOwnWorld(event_layers=()):
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=1`, `not_in_own_world=True`.
    """


def SkipLinesIfClientTypeCountComparison(
    skip_lines: int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Value from 0 to 4.
    """


def GotoIfClientTypeCountComparison(
    label: Label | int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Value from 0 to 4.
    """


def ReturnIfClientTypeCountComparison(
    event_return_type: EventReturnType | int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Value from 0 to 4.
    """


def EndIfClientTypeCountComparison(
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Calls `ReturnIfClientTypeCountComparison` with `event_return_type=0`.
    """


def RestartIfClientTypeCountComparison(
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Calls `ReturnIfClientTypeCountComparison` with `event_return_type=1`.
    """


def GotoIfFlagState(
    label: Label | int,
    state: bool | int,
    flag_type: FlagType | int,
    flag: Flag | int,
    event_layers=(),
):
    """
    TODO
    """


def GotoIfThisEventFlagEnabled(label: Label | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=1`, `flag=0`.
    """


def GotoIfThisEventFlagDisabled(label: Label | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=1`, `flag=0`.
    """


def GotoIfThisEventSlotFlagEnabled(label: Label | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=2`, `flag=0`.
    """


def GotoIfThisEventSlotFlagDisabled(label: Label | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=2`, `flag=0`.
    """


def GotoIfFlagEnabled(label: Label | int, flag: Flag | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=0`.
    """


def GotoIfFlagDisabled(label: Label | int, flag: Flag | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=0`.
    """


def GotoIfFlagRangeState(
    label: Label | int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def GotoIfFlagRangeAllEnabled(label: Label | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `GotoIfFlagRangeState` with `state=0`, `flag_type=0`.
    """


def GotoIfFlagRangeAllDisabled(label: Label | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `GotoIfFlagRangeState` with `state=1`, `flag_type=0`.
    """


def GotoIfFlagRangeAnyEnabled(label: Label | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `GotoIfFlagRangeState` with `state=2`, `flag_type=0`.
    """


def GotoIfFlagRangeAnyDisabled(label: Label | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `GotoIfFlagRangeState` with `state=3`, `flag_type=0`.
    """


def GotoIfMultiplayerState(label: Label | int, state: MultiplayerState | int, event_layers=()):
    """
    TODO
    """


def GotoIfHost(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=0`.
    """


def GotoIfClient(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=1`.
    """


def GotoIfTryingToCreateSession(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=2`.
    """


def GotoIfTryingToJoinSession(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=3`.
    """


def GotoIfLeavingSession(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=4`.
    """


def GotoIfFailedToCreateSession(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=5`.
    """


def GotoIfMapPresenceState(label: Label | int, state: bool | int, game_map: Map | tuple | list, event_layers=()):
    """
    TODO
    """


def GotoIfInsideMap(label: Label | int, game_map: Map | tuple | list, event_layers=()):
    """
    Calls `GotoIfMapPresenceState` with `state=True`.
    """


def GotoIfOutsideMap(label: Label | int, game_map: Map | tuple | list, event_layers=()):
    """
    Calls `GotoIfMapPresenceState` with `state=False`.
    """


def GotoIfCoopClientCountComparison(
    label: Label | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
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
    event_layers=(),
):
    """
    TODO
    """


def EndIfPlayerHasSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `character=10000`, `state=True`.
    """


def EndIfPlayerDoesNotHaveSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `character=10000`, `state=False`.
    """


def RestartIfPlayerHasSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=1`, `character=10000`, `state=True`.
    """


def RestartIfPlayerDoesNotHaveSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=1`, `character=10000`, `state=False`.
    """


def EndIfCharacterHasSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `state=True`.
    """


def EndIfCharacterDoesNotHaveSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `state=False`.
    """


def RestartIfCharacterHasSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=1`, `state=True`.
    """


def RestartIfCharacterDoesNotHaveSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
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
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfPlayerHasSpecialEffect(
    line_count: int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `SkipLinesIfCharacterSpecialEffectState` with `character=10000`, `state=True`.
    """


def SkipLinesIfPlayerDoesNotHaveSpecialEffect(
    line_count: int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
):
    """
    EMEDF does not have the final new argument listed (it's the same as the other region/distance checks).
    """


def GotoIfPlayerInsideRegion(label: Label | int, region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `GotoIfCharacterRegionState` with `character=10000`, `state=True`.
    """


def GotoIfPlayerOutsideRegion(label: Label | int, region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `GotoIfCharacterRegionState` with `character=10000`, `state=False`.
    """


def GotoIfCharacterInsideRegion(
    label: Label | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `GotoIfCharacterRegionState` with `state=True`.
    """


def GotoIfCharacterOutsideRegion(
    label: Label | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
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
    event_layers=(),
):
    """
    TODO
    """


def EndIfPlayerInsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `character=10000`, `state=True`.
    """


def EndIfPlayerOutsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `character=10000`, `state=False`.
    """


def RestartIfPlayerInsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `character=10000`, `state=True`.
    """


def RestartIfPlayerOutsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `character=10000`, `state=False`.
    """


def EndIfCharacterInsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `state=True`.
    """


def EndIfCharacterOutsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfCharacterInsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfCharacterOutsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `state=False`.
    """


def SkipLinesIfCharacterRegionState(
    line_count: int,
    state: bool | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfPlayerInsideRegion(line_count: int, region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=True`, `character=10000`.
    """


def SkipLinesIfPlayerOutsideRegion(line_count: int, region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=False`, `character=10000`.
    """


def SkipLinesIfCharacterInsideRegion(
    line_count: int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=True`.
    """


def SkipLinesIfCharacterOutsideRegion(
    line_count: int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=False`.
    """


def GotoIfHollowArenaMatchType(label: Label | int, match_type: HollowArenaMatchType | int, event_layers=()):
    """
    TODO
    """


def GotoIfObjectDestructionState(
    label: Label | int,
    state: bool | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Note change in argument order.
    """


def GotoIfObjectDestroyed(
    label: Label | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `GotoIfObjectDestructionState` with `state=True`.
    """


def GotoIfObjectNotDestroyed(
    label: Label | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `GotoIfObjectDestructionState` with `state=False`.
    """


def DefineLabel_0(event_layers=()):
    """
    Define position of label 0 for Goto instructions.
    """


def DefineLabel_1(event_layers=()):
    """
    Define position of label 1 for Goto instructions.
    """


def DefineLabel_2(event_layers=()):
    """
    Define position of label 2 for Goto instructions.
    """


def DefineLabel_3(event_layers=()):
    """
    Define position of label 3 for Goto instructions.
    """


def DefineLabel_4(event_layers=()):
    """
    Define position of label 4 for Goto instructions.
    """


def DefineLabel_5(event_layers=()):
    """
    Define position of label 5 for Goto instructions.
    """


def DefineLabel_6(event_layers=()):
    """
    Define position of label 6 for Goto instructions.
    """


def DefineLabel_7(event_layers=()):
    """
    Define position of label 7 for Goto instructions.
    """


def DefineLabel_8(event_layers=()):
    """
    Define position of label 8 for Goto instructions.
    """


def DefineLabel_9(event_layers=()):
    """
    Define position of label 9 for Goto instructions.
    """


def DefineLabel_10(event_layers=()):
    """
    Define position of label 10 for Goto instructions.
    """


def DefineLabel_11(event_layers=()):
    """
    Define position of label 11 for Goto instructions.
    """


def DefineLabel_12(event_layers=()):
    """
    Define position of label 12 for Goto instructions.
    """


def DefineLabel_13(event_layers=()):
    """
    Define position of label 13 for Goto instructions.
    """


def DefineLabel_14(event_layers=()):
    """
    Define position of label 14 for Goto instructions.
    """


def DefineLabel_15(event_layers=()):
    """
    Define position of label 15 for Goto instructions.
    """


def DefineLabel_16(event_layers=()):
    """
    Define position of label 16 for Goto instructions.
    """


def DefineLabel_17(event_layers=()):
    """
    Define position of label 17 for Goto instructions.
    """


def DefineLabel_18(event_layers=()):
    """
    Define position of label 18 for Goto instructions.
    """


def DefineLabel_19(event_layers=()):
    """
    Define position of label 19 for Goto instructions.
    """


def DefineLabel_20(event_layers=()):
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
    event_layers=(),
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
    event_layers=(),
):
    """
    Probably used when you examine Laurence's skull, etc.
    """


def PlayCutsceneAndMovePlayer_Dummy(move_to_region: Region | int, game_map: Map | tuple | list, event_layers=()):
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
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
):
    """
    TODO
    """


def Unknown_2003_27(arg1: int, event_layers=()):
    """
    No information. Used exactly once, after the cutscene that played when Ludwig's first phase was defeated
    with the Old Hunters DLC demo flag enabled. Unknown effect. Maybe just terminated the whole DLC demo.
    """


def StoreItemAmountSpecifiedByFlagValue(
    item_type: ItemType | int,
    item: BaseItemParam | int,
    flag: Flag | int,
    bit_count: int,
    event_layers=(),
):
    """
    Stores some amount of items read from a flag array.
    """


def GivePlayerItemAmountSpecifiedByFlagValue(
    item_type: ItemType | int,
    item: BaseItemParam | int,
    flag: Flag | int,
    bit_count: int,
    event_layers=(),
):
    """
    Gives player some amount of items read from a flag array. Probably used when taking items out of storage
    (i.e. the reverse of the above instruction).
    """


def SetDirectionDisplayState(state: bool | int, event_layers=()):
    """
    Not sure what this is.
    """


def EnableDirectionDisplayState(event_layers=()):
    """
    Calls `SetDirectionDisplayState` with `state=True`.
    """


def DisableDirectionDisplayState(event_layers=()):
    """
    Calls `SetDirectionDisplayState` with `state=False`.
    """


def SetMapHitGridCorrespondence(
    collision: Collision | int,
    level: int,
    grid_coord_x: int,
    grid_coord_y: int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def EnableMapHitGridCorrespondence(
    collision: Collision | int,
    level: int,
    grid_coord_x: int,
    grid_coord_y: int,
    event_layers=(),
):
    """
    Calls `SetMapHitGridCorrespondence` with `state=True`.
    """


def DisableMapHitGridCorrespondence(
    collision: Collision | int,
    level: int,
    grid_coord_x: int,
    grid_coord_y: int,
    event_layers=(),
):
    """
    Calls `SetMapHitGridCorrespondence` with `state=False`.
    """


def SetMapContentImageDisplayState(content_image_part_id: int, state: bool | int, event_layers=()):
    """
    TODO
    """


def SetMapBoundariesDisplay(hierarchy: int, grid_coord_x: int, grid_coord_y: int, state: bool | int, event_layers=()):
    """
    TODO
    """


def SetAreaWind(region: Region | int, state: bool | int, duration: float, wind_parameter_id: int, event_layers=()):
    """
    TODO
    """


def WarpPlayerToRespawnPoint(respawn_point_id: int, event_layers=()):
    """
    TODO
    """


def StartEnemySpawner(spawner_id: int, event_layers=()):
    """
    TODO
    """


def SummonNPC(
    sign_type: SingleplayerSummonSignType | int,
    character: Character | int,
    region: Region | int,
    summon_flag: Flag | int,
    dismissal_flag: Flag | int,
    event_layers=(),
):
    """
    TODO
    """


def InitializeWarpObject(warp_object_id: int, event_layers=()):
    """
    TODO
    """


def MakeEnemyAppear(character: Character | int, event_layers=()):
    """
    TODO
    """


def SetCurrentMapCeremony(ceremony_id: int, event_layers=()):
    """
    TODO
    """


def SetMapCeremony(game_map: Map | tuple | list, ceremony_id: int, event_layers=()):
    """
    TODO
    """


def DisplayEpitaphMessage(message: EventText | int, event_layers=()):
    """
    TODO
    """


def SetNetworkConnectedFlagState(flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    TODO
    """


def SetNetworkConnectedFlagRangeState(flag_range: FlagRange | tuple | list, state: FlagSetting | int, event_layers=()):
    """
    Network-synchronized variant of `SetFlagRangeState` (2003[22]).
    """


def EnableNetworkConnectedFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetNetworkConnectedFlagRangeState` with `state=1`.
    """


def DisableNetworkConnectedFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetNetworkConnectedFlagRangeState` with `state=0`.
    """


def ToggleNetworkConnectedFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetNetworkConnectedFlagRangeState` with `state=2`.
    """


def SetOmissionModeCounts(level_1_count: int, level_2_count: int, event_layers=()):
    """
    TODO
    """


def ResetOmissionModeCountsToDefault(event_layers=()):
    """
    TODO
    """


def InitializeCrowTrade(
    item_type: ItemType | int,
    item_id: BaseItemParam | int,
    item_lot_id: ItemLotParam | int,
    trade_completed_flag: Flag | int,
    crow_response_flag: Flag | int,
    event_layers=(),
):
    """
    TODO
    """


def InitializeCrowTradeRegion(region: Region | int, event_layers=()):
    """
    TODO
    """


def SetNetworkInteractionState(state: bool | int, event_layers=()):
    """
    TODO
    """


def SetHUDVisibilityState(is_invisible: bool | int, event_layers=()):
    """
    TODO
    """


def EnableHUDVisibility(event_layers=()):
    """
    Calls `SetHUDVisibilityState` with `is_invisible=False`.
    """


def DisableHUDVisibility(event_layers=()):
    """
    Calls `SetHUDVisibilityState` with `is_invisible=True`.
    """


def SetBonfireWarpingState(bonfire_obj: Object | int, animation: int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableBonfireWarping(bonfire_obj: Object | int, animation: int, event_layers=()):
    """
    Calls `SetBonfireWarpingState` with `state=True`.
    """


def DisableBonfireWarping(bonfire_obj: Object | int, animation: int, event_layers=()):
    """
    Calls `SetBonfireWarpingState` with `state=False`.
    """


def SetAutogeneratedEventSpecificFlag_1(unknown1: int, unknown2: int, event_layers=()):
    """
    No idea, but probably relates to setting the flag whose ID matches the event ID.
    """


def HandleBossDefeatAndDisplayBanner(boss: int, banner: BannerType | int, event_layers=()):
    """
    Not sure if the 'boss' is a GameAreaParam or just Character.
    """


def SetAutogeneratedEventSpecificFlag_2(unknown1: int, unknown2: int, event_layers=()):
    """
    No idea, but probably relates to setting the flag whose ID matches the event ID.
    """


def SetLoadingScreenTipsState(tips_disabled: bool | int, event_layers=()):
    """
    TODO
    """


def EnableLoadingScreenTips(event_layers=()):
    """
    Calls `SetLoadingScreenTipsState` with `tips_disabled=False`.
    """


def DisableLoadingScreenTips(event_layers=()):
    """
    Calls `SetLoadingScreenTipsState` with `tips_disabled=True`.
    """


def AwardGestureItem(gesture_id: int, item_type: ItemType | int, item_id: int, event_layers=()):
    """
    Not sure if this awards an actual gesture (then why multiple args?) or awards it based on a gesture (but
    then why not region-specific?).
    """


def SendNPCSummonHome(character: Character | int, event_layers=()):
    """
    Identical to Bloodborne version, but with different index.
    """


def Unknown_2003_79(unknown1: int, event_layers=()):
    """
    TODO
    """


def SetDecoratedBossHealthBarState(
    state: bool | int,
    character: Character | int,
    slot: int,
    name: EventText | int,
    decoration: int,
    event_layers=(),
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
    event_layers=(),
):
    """
    TODO
    """


def ChangeCharacterCloth(character: Character | int, bit_count: int, state_id: int, event_layers=()):
    """
    TODO
    """


def ChangePatrolBehavior(character: Character | int, patrol_information_id: int, event_layers=()):
    """
    I don't know what a 'patrol_information_id' actually is.
    """


def SetLockOnPoint(character: Character | int, lock_on_model_point: int, state: bool | int, event_layers=()):
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
    event_layers=(),
):
    """
    TODO
    """


def ChangePlayerCharacterInitParam(character_init_param: int, event_layers=()):
    """
    I assume this affects the player.
    """


def AdaptSpecialEffectHealthChangeToNPCPart(character: Character | int, event_layers=()):
    """
    TODO
    """


def ImmediateActivate(character: Character | int, state: bool | int, event_layers=()):
    """
    Not sure. Sets draw state *really* quickly?
    """


def SetCharacterTalkRange(character: Character | int, distance: float, event_layers=()):
    """
    TODO
    """


def IncrementCharacterNewGameCycle(character: Character | int, event_layers=()):
    """
    Interesting - apparently you can increase the NG+ level of a specific character. (No reset function, but it
    would probably reset on map reload.)
    """


def SetMultiplayerBuffs_NonBoss(character: Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def Unknown_2004_59(character: Character | int, state: bool | int, event_layers=()):
    """
    Examine usage.
    """


def SetPlayerRemainingYoelLevels(level_count: int, event_layers=()):
    """
    TODO
    """


def ExtinguishBurningObjects(event_layers=()):
    """
    TODO
    """


def ShowObjectByMapCeremony(obj: Object | int, ceremony_id: int, unknown: int, event_layers=()):
    """
    TODO
    """


def DestroyObject_NoSlot(obj: Object | int, event_layers=()):
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
    event_layers=(),
):
    """
    Displays a dialog and enables one of three flags, depending on the player's response. Very useful.
    """


def DisplayAreaWelcomeMessage(message: EventText | int, event_layers=()):
    """
    Not sure what this looks like exactly.
    """


def DisplayHollowArenaMessage(message: EventText | int, unknown: int, pad_enabled: bool | int, event_layers=()):
    """
    TODO
    """


def BanishInvaders(unknown: int, event_layers=()):
    """
    TODO
    """


def BanishPhantomsAndUpdateServerPvPStats(unknown: int, event_layers=()):
    """
    TODO
    """


def BanishPhantoms(unknown: int, event_layers=()):
    """
    TODO
    """


def SetBossMusicState(sound_id: int, state: bool | int, event_layers=()):
    """
    Not sure how this differs from the standard map sound instructions, but my guess is that it fades the music
    out rather than abruptly stopping it.
    
    TODO: Can probably be used to fade out ANY music. Not sure why it would only work for boss music.
    TODO: Argument -1 is sometimes used. Fades out ALL music?
    """


def EnableBossMusic(sound_id: int, event_layers=()):
    """
    Calls `SetBossMusicState` with `state=True`.
    """


def DisableBossMusic(sound_id: int, event_layers=()):
    """
    Calls `SetBossMusicState` with `state=False`.
    """


def NotifyDoorEventSoundDampening(obj: Object | int, state: DoorState | int, event_layers=()):
    """
    No idea what this is or what entity the first argument is. Probably the door object.
    """


def SetSoundEventWithFade(sound_id: int, state: bool | int, fade_duration: float, event_layers=()):
    """
    TODO
    """


def EnableSoundEventWithFade(sound_id: int, fade_duration: float, event_layers=()):
    """
    Calls `SetSoundEventWithFade` with `state=True`.
    """


def DisableSoundEventWithFade(sound_id: int, fade_duration: float, event_layers=()):
    """
    Calls `SetSoundEventWithFade` with `state=False`.
    """


def Unknown_2010_07(sound_id: int, event_layers=()):
    """
    Unknown SoundEvent instruction.
    """


def SetCollisionResState(collision: Collision | int, state: bool | int, event_layers=()):
    """
    No idea what this is.
    """


def ActivateCollisionAndCreateNavmesh(collision: Collision | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def SetAreaWelcomeMessageState(state: bool | int, event_layers=()):
    """
    TODO
    """


def CreatePlayLog(name: StringOffset | int, event_layers=()):
    """
    TODO
    """


def StartPlayLogMeasurement(measurement_id: int, name: StringOffset | int, overwrite: bool | int, event_layers=()):
    """
    TODO
    """


def StopPlayLogMeasurement(measurement_id: int, event_layers=()):
    """
    TODO
    """


def PlayLogParameterOutput(
    category: PlayerPlayLogParameter | int,
    name: StringOffset | int,
    output_multiplayer_state: PlayLogMultiplayerType | int,
    event_layers=(),
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


def ValueComparison(comparison_type: ComparisonType | int, left: int, right: int, event_layers=()) -> bool:
    ...


def ValueEqual(left: int, right: int, event_layers=()) -> bool:
    ...


def ValueNotEqual(left: int, right: int, event_layers=()) -> bool:
    ...


def ValueGreaterThan(left: int, right: int, event_layers=()) -> bool:
    ...


def ValueLessThan(left: int, right: int, event_layers=()) -> bool:
    ...


def ValueGreaterThanOrEqual(left: int, right: int, event_layers=()) -> bool:
    ...


def ValueLessThanOrEqual(left: int, right: int, event_layers=()) -> bool:
    ...


def TimeElapsed(seconds: float, event_layers=()) -> bool:
    ...


def FramesElapsed(frames: int, event_layers=()) -> bool:
    ...


def RandomTimeElapsed(min_seconds: float, max_seconds: float, event_layers=()) -> bool:
    ...


def RandomFramesElapsed(min_frames: int, max_frames: int, event_layers=()) -> bool:
    ...


def FlagState(state: FlagSetting | int, flag_type: FlagType | int, flag: Flag | int, event_layers=()) -> bool:
    ...


def FlagEnabled(flag: Flag | int, event_layers=()) -> bool:
    ...


def FlagDisabled(flag: Flag | int, event_layers=()) -> bool:
    ...


def ThisEventFlagEnabled(event_layers=()) -> bool:
    ...


def ThisEventFlagDisabled(event_layers=()) -> bool:
    ...


def ThisEventSlotFlagEnabled(event_layers=()) -> bool:
    ...


def ThisEventSlotFlagDisabled(event_layers=()) -> bool:
    ...


def FlagRangeState(
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    event_layers=(),
) -> bool:
    ...


def FlagRangeAllEnabled(flag_range: FlagRange | tuple | list, event_layers=()) -> bool:
    ...


def FlagRangeAllDisabled(flag_range: FlagRange | tuple | list, event_layers=()) -> bool:
    ...


def FlagRangeAnyEnabled(flag_range: FlagRange | tuple | list, event_layers=()) -> bool:
    ...


def FlagRangeAnyDisabled(flag_range: FlagRange | tuple | list, event_layers=()) -> bool:
    ...


def CharacterRegionState(
    state: bool | int,
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def PlayerInsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()) -> bool:
    ...


def PlayerOutsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()) -> bool:
    ...


def CharacterInsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def CharacterOutsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def EntityDistanceState(
    state: bool | int,
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def PlayerWithinDistance(
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def PlayerBeyondDistance(
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def EntityWithinDistance(
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def EntityBeyondDistance(
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def PlayerItemStateExcludingStorage(
    item: BaseItemParam | int,
    state: bool | int,
    item_type: ItemType | int = None,
    event_layers=(),
) -> bool:
    ...


def ActionButtonBasic(
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    event_layers=(),
) -> bool:
    ...


def MultiplayerState(state: MultiplayerState | int, event_layers=()) -> bool:
    ...


def Host(event_layers=()) -> bool:
    ...


def Client(event_layers=()) -> bool:
    ...


def TryingToCreateSession(event_layers=()) -> bool:
    ...


def TryingToJoinSession(event_layers=()) -> bool:
    ...


def LeavingSession(event_layers=()) -> bool:
    ...


def FailedToCreateSession(event_layers=()) -> bool:
    ...


def AllPlayersRegionState(state: bool | int, region: Region | int, event_layers=()) -> bool:
    ...


def AllPlayersInsideRegion(region: Region | int, event_layers=()) -> bool:
    ...


def AllPlayersOutsideRegion(region: Region | int, event_layers=()) -> bool:
    ...


def MapPresenceState(state: bool | int, game_map: Map | tuple | list, event_layers=()) -> bool:
    ...


def InsideMap(game_map: Map | tuple | list, event_layers=()) -> bool:
    ...


def OutsideMap(game_map: Map | tuple | list, event_layers=()) -> bool:
    ...


def MultiplayerEvent(event_id: int, event_layers=()) -> bool:
    ...


def TrueFlagCountComparison(
    flag_type: FlagType | int,
    comparison_type: ComparisonType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def TrueFlagCountEqual(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int, event_layers=()) -> bool:
    ...


def TrueFlagCountNotEqual(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def TrueFlagCountGreaterThan(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def TrueFlagCountLessThan(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def TrueFlagCountGreaterThanOrEqual(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def TrueFlagCountLessThanOrEqual(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def WorldTendencyComparison(
    world_tendency_type: WorldTendencyType | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
) -> bool:
    ...


def WhiteWorldTendencyComparison(comparison_type: ComparisonType | int, value: int, event_layers=()) -> bool:
    ...


def BlackWorldTendencyComparison(comparison_type: ComparisonType | int, value: int, event_layers=()) -> bool:
    ...


def WhiteWorldTendencyGreaterThan(value: int, event_layers=()) -> bool:
    ...


def BlackWorldTendencyGreaterThan(value: int, event_layers=()) -> bool:
    ...


def EventValueComparison(
    flag: Flag | int,
    bit_count: int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
) -> bool:
    ...


def EventValueEqual(flag: Flag | int, bit_count: int, value: int, event_layers=()) -> bool:
    ...


def EventValueNotEqual(flag: Flag | int, bit_count: int, value: int, event_layers=()) -> bool:
    ...


def EventValueGreaterThan(flag: Flag | int, bit_count: int, value: int, event_layers=()) -> bool:
    ...


def EventValueLessThan(flag: Flag | int, bit_count: int, value: int, event_layers=()) -> bool:
    ...


def EventValueGreaterThanOrEqual(flag: Flag | int, bit_count: int, value: int, event_layers=()) -> bool:
    ...


def EventValueLessThanOrEqual(flag: Flag | int, bit_count: int, value: int, event_layers=()) -> bool:
    ...


def ActionButtonBoss(
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    event_layers=(),
) -> bool:
    ...


def AnyItemDroppedInRegion(region: Region | int, event_layers=()) -> bool:
    ...


def ItemDropped(item: BaseItemParam | int, item_type: ItemType | int = None, event_layers=()) -> bool:
    ...


def PlayerItemStateIncludingStorage(
    item: BaseItemParam | int,
    state: bool | int,
    item_type: ItemType | int = None,
    event_layers=(),
) -> bool:
    ...


def NewGameCycleComparison(comparison_type: ComparisonType | int, completion_count: int, event_layers=()) -> bool:
    ...


def NewGameCycleEqual(completion_count: int, event_layers=()) -> bool:
    ...


def NewGameCycleNotEqual(completion_count: int, event_layers=()) -> bool:
    ...


def NewGameCycleGreaterThan(completion_count: int, event_layers=()) -> bool:
    ...


def NewGameCycleLessThan(completion_count: int, event_layers=()) -> bool:
    ...


def NewGameCycleGreaterThanOrEqual(completion_count: int, event_layers=()) -> bool:
    ...


def NewGameCycleLessThanOrEqual(completion_count: int, event_layers=()) -> bool:
    ...


def ActionButtonBasicLineIntersect(
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    event_layers=(),
) -> bool:
    ...


def ActionButtonBossLineIntersect(
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    model_point: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    event_layers=(),
) -> bool:
    ...


def EventsComparison(
    left_flag: Flag | int,
    left_bit_count: int,
    comparison_type: ComparisonType | int,
    right_flag: Flag | int,
    right_bit_count: int,
    event_layers=(),
) -> bool:
    ...


def DLCState(is_owned: bool | int, event_layers=()) -> bool:
    ...


def DLCOwned(event_layers=()) -> bool:
    ...


def DLCNotOwned(event_layers=()) -> bool:
    ...


def OnlineState(state: bool | int, event_layers=()) -> bool:
    ...


def Online(event_layers=()) -> bool:
    ...


def Offline(event_layers=()) -> bool:
    ...


def CharacterDeathState(
    character: Character | int,
    is_dead: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterDead(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterAlive(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def Attacked(attacked_entity: Character | int, attacker: Character | int, event_layers=()) -> bool:
    ...


def HealthComparison(
    character: Character | int,
    comparison_type: ComparisonType | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthEqual(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthNotEqual(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthGreaterThan(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthLessThan(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthGreaterThanOrEqual(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthLessThanOrEqual(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterType(
    character: Character | int,
    character_type: CharacterType | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterHuman(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterWhitePhantom(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterHollow(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterTargetingState(
    targeting_character: Character | int,
    targeted_character: Character | int,
    state: bool | int,
    event_layers=(),
) -> bool:
    ...


def CharacterTargeting(targeting_character: Character | int, targeted_character: Character | int, event_layers=()) -> bool:
    ...


def CharacterNotTargeting(targeting_character: Character | int, targeted_character: Character | int, event_layers=()) -> bool:
    ...


def CharacterSpecialEffectState(
    character: Character | int,
    special_effect: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def PlayerHasSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def PlayerDoesNotHaveSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterHasSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterDoesNotHaveSpecialEffect(
    character: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterPartHealthComparison(
    character: Character | int,
    npc_part_id: int,
    value: float,
    comparison_type: ComparisonType | int,
    event_layers=(),
) -> bool:
    ...


def CharacterPartHealthLessThanOrEqual(character: Character | int, npc_part_id: int, value: float, event_layers=()) -> bool:
    ...


def CharacterBackreadState(
    character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterBackreadEnabled(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterBackreadDisabled(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterTAEEventState(
    character: Character | int,
    tae_event_id: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterHasTAEEvent(
    character: Character | int,
    tae_event_id: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterDoesNotHaveTAEEvent(
    character: Character | int,
    tae_event_id: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HasAIStatus(
    character: Character | int,
    ai_status: AIStatusType | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def SkullLanternState(state: bool | int, event_layers=()) -> bool:
    ...


def SkullLanternActive(event_layers=()) -> bool:
    ...


def SkullLanternInactive(event_layers=()) -> bool:
    ...


def PlayerClass(class_type: ClassType | int, event_layers=()) -> bool:
    ...


def PlayerCovenant(covenant: Covenant | int, event_layers=()) -> bool:
    ...


def PlayerLevelComparison(comparison_type: ComparisonType | int, value: int, event_layers=()) -> bool:
    ...


def PlayerLevelEqual(value: int, event_layers=()) -> bool:
    ...


def PlayerLevelNotEqual(value: int, event_layers=()) -> bool:
    ...


def PlayerLevelGreaterThan(value: int, event_layers=()) -> bool:
    ...


def PlayerLevelLessThan(value: int, event_layers=()) -> bool:
    ...


def PlayerLevelGreaterThanOrEqual(value: int, event_layers=()) -> bool:
    ...


def PlayerLevelLessThanOrEqual(value: int, event_layers=()) -> bool:
    ...


def HealthValueComparison(
    character: Character | int,
    comparison_type: ComparisonType | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthValueEqual(
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthValueNotEqual(
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthValueGreaterThan(
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthValueLessThan(
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthValueGreaterThanOrEqual(
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthValueLessThanOrEqual(
    character: Character | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ObjectDestructionState(
    state: bool | int,
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ObjectDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ObjectNotDestroyed(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ObjectDamaged(obj: Object | int, attacker: Character | int, event_layers=()) -> bool:
    ...


def ObjectActivated(obj_act_id: int, event_layers=()) -> bool:
    ...


def ObjectHealthValueComparison(
    obj: Object | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
) -> bool:
    ...


def PlayerMovingOnCollision(collision: Collision | int, event_layers=()) -> bool:
    ...


def PlayerRunningOnCollision(collision: Collision | int, event_layers=()) -> bool:
    ...


def PlayerStandingOnCollision(collision: Collision | int, event_layers=()) -> bool:
    ...


def AttackedWithDamageType(
    attacked_entity: Character | int,
    attacker: Character | int = -1,
    damage_type: DamageType | int = DamageType.Unspecified,
    event_layers=(),
) -> bool:
    ...


def ActionButtonParamActivated(action_button_id: int, entity: Object | Region | Character | int, event_layers=()) -> bool:
    ...


def PlayerOwnWorldState(not_in_own_world: bool | int, event_layers=()) -> bool:
    ...


def PlayerInOwnWorld(event_layers=()) -> bool:
    ...


def PlayerNotInOwnWorld(event_layers=()) -> bool:
    ...


def MapCeremonyState(state: bool | int, game_map: Map | tuple | list, ceremony_id: int, event_layers=()) -> bool:
    ...


def MapInCeremony(game_map: Map | tuple | list, ceremony_id: int, event_layers=()) -> bool:
    ...


def MapNotInCeremony(game_map: Map | tuple | list, ceremony_id: int, event_layers=()) -> bool:
    ...


def MultiplayerNetworkPenalized(event_layers=()) -> bool:
    ...


def PlayerGender(gender: Gender | int, event_layers=()) -> bool:
    ...


def OngoingCutsceneFinished(cutscene_id: int, event_layers=()) -> bool:
    ...


def HollowArenaMatchReadyState(is_ready: bool | int, event_layers=()) -> bool:
    ...


def HollowArenaSoloResults(result: HollowArenaResult | int, event_layers=()) -> bool:
    ...


def HollowArenaSoloScoreComparison(comparison_type: ComparisonType | int, value: int, unknown: int, event_layers=()) -> bool:
    ...


def HollowArenaTeamResults(result: HollowArenaResult | int, event_layers=()) -> bool:
    ...


def SteamConnectionState(is_disconnected: bool | int, event_layers=()) -> bool:
    ...


def AllyPhantomCountComparison(
    comparison_state: bool | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
) -> bool:
    ...


def CharacterDrawGroupState(
    character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterDrawGroupEnabled(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterDrawGroupDisabled(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def PlayerRemainingYoelLevelComparison(comparison_type: ComparisonType | int, value: int, event_layers=()) -> bool:
    ...


def CharacterInvadeType(
    character: Character | int,
    invade_type: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterChameleonState(
    character: Character | int,
    chameleon_vfx_id: int,
    is_transformed: bool | int,
    event_layers=(),
) -> bool:
    ...


def ObjectBurnState(
    obj: Object | int,
    comparison_type: ComparisonType | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ObjectBackreadState(
    obj: Object | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ObjectBackreadEnabled(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ObjectBackreadDisabled(
    obj: Object | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ObjectBackreadState_Alternate(
    obj: Object | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ActionButton(
    prompt_text: EventText | int,
    anchor_entity: Object | Region | Character | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    max_distance: float = None,
    model_point: int = -1,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    boss_version: bool = False,
    line_intersects: Object | Region | Character | int = None,
    event_layers=(),
) -> bool:
    """
    Calls `compiler.IfActionButton`.
    """
    ...


def PlayerHasWeapon(weapon: WeaponParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerHasWeapon`.
    """
    ...


def PlayerHasArmor(armor: ArmorParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerHasArmor`.
    """
    ...


def PlayerHasRing(ring: AccessoryParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerHasRing`.
    """
    ...


def PlayerHasGood(good: GoodParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerHasGood`.
    """
    ...
