"""AUTOMATICALLY GENERATED. Do not edit this module manually.

Import this into any EVS script to have full access to instructions.
Make sure you also do `from soulstruct.{game}.events import *` to get all enums, constants, and tests.
You will likely also want `from soulstruct.{game}.game_types import *`.
"""

__all__ = [
    # Basics:
    "ContinueOnRest",
    "RestartOnRest",
    "EndOnRest",
    "EVENTS",
    "Condition",
    "HeldCondition",
    "LastResult",
    "Await",
    "END",
    "RESTART",
    "RunEvent",
    # Condition groups:
    "OR_15",
    "OR_14",
    "OR_13",
    "OR_12",
    "OR_11",
    "OR_10",
    "OR_9",
    "OR_8",
    "OR_7",
    "OR_6",
    "OR_5",
    "OR_4",
    "OR_3",
    "OR_2",
    "OR_1",
    "MAIN",
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
    "IfMultiplayer",
    "IfConnectingMultiplayer",
    "IfSingleplayer",
    "IfAllPlayersRegionState",  # 3[7]
    "IfAllPlayersInsideRegion",
    "IfAllPlayersOutsideRegion",
    "IfMapPresenceState",  # 3[8]
    "IfInsideMap",
    "IfOutsideMap",
    "IfMultiplayerEvent",  # 3[9]
    "IfEnabledFlagCountComparison",  # 3[10]
    "IfEnabledFlagCountEqual",
    "IfEnabledFlagCountNotEqual",
    "IfEnabledFlagCountGreaterThan",
    "IfEnabledFlagCountLessThan",
    "IfEnabledFlagCountGreaterThanOrEqual",
    "IfEnabledFlagCountLessThanOrEqual",
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
    "IfAttackedWithDamageType",  # 3[23]
    "IfActionButtonParamActivated",  # 3[24]
    "IfPlayerArmorInRange",  # 3[25]
    "IfPlayerInsightAmountComparison",  # 3[26]
    "IfPlayerInsightAmountEqual",
    "IfPlayerInsightAmountNotEqual",
    "IfPlayerInsightAmountGreaterThan",
    "IfPlayerInsightAmountLessThan",
    "IfPlayerInsightAmountGreaterThanOrEqual",
    "IfPlayerInsightAmountLessThanOrEqual",
    "IfDialogChoice",  # 3[27]
    "IfPlayGoState",  # 3[28]
    "IfClientTypeCountComparison",  # 3[29]
    "IfCharacterDeathState",  # 4[0]
    "IfCharacterDead",
    "IfCharacterAlive",
    "IfAttacked",  # 4[1]
    "IfHealthRatioComparison",  # 4[2]
    "IfHealthRatioEqual",
    "IfHealthRatioNotEqual",
    "IfHealthRatioGreaterThan",
    "IfHealthRatioLessThan",
    "IfHealthRatioGreaterThanOrEqual",
    "IfHealthRatioLessThanOrEqual",
    "IfCharacterIsType",  # 4[3]
    "IfCharacterIsHuman",
    "IfCharacterIsWhitePhantom",
    "IfCharacterIsHollow",
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
    "IfCharacterDrawGroupState",  # 4[15]
    "IfCharacterDrawGroupEnabled",
    "IfCharacterDrawGroupDisabled",
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
    "SkipLinesIfLastConditionResultState",  # 1000[7]
    "SkipLinesIfLastConditionResultTrue",
    "SkipLinesIfLastConditionResultFalse",
    "ReturnIfLastConditionResultState",  # 1000[8]
    "EndIfLastConditionResultTrue",
    "EndIfLastConditionResultFalse",
    "RestartIfLastConditionResultTrue",
    "RestartIfLastConditionResultFalse",
    "WaitForNetworkApproval",  # 1000[9]
    "GotoIfConditionState",  # 1000[101]
    "GotoIfConditionTrue",
    "GotoIfConditionFalse",
    "Goto",  # 1000[103]
    "GotoIfValueComparison",  # 1000[105]
    "GotoIfLastConditionResultState",  # 1000[107]
    "GotoIfLastConditionResultTrue",
    "GotoIfLastConditionResultFalse",
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
    "SkipLinesIfMultiplayerState",  # 1003[5]
    "SkipLinesIfHost",
    "SkipLinesIfClient",
    "SkipLinesIfMultiplayer",
    "SkipLinesIfConnectingMultiplayer",
    "SkipLinesIfSingleplayer",
    "ReturnIfMultiplayerState",  # 1003[6]
    "EndIfHost",
    "EndIfClient",
    "EndIfMultiplayer",
    "EndIfConnectingMultiplayer",
    "EndIfSingleplayer",
    "RestartIfHost",
    "RestartIfClient",
    "RestartIfMultiplayer",
    "RestartIfConnectingMultiplayer",
    "RestartIfSingleplayer",
    "SkipLinesIfMapPresenceState",  # 1003[7]
    "SkipLinesIfInsideMap",
    "SkipLinesIfOutsideMap",
    "ReturnIfMapPresenceState",  # 1003[8]
    "EndIfInsideMap",
    "EndIfOutsideMap",
    "RestartIfInsideMap",
    "RestartIfOutsideMap",
    "SkipLinesIfCoopClientCountComparison",  # 1003[9]
    "ReturnIfCoopClientCountComparison",  # 1003[10]
    "EndIfCoopClientCountComparison",
    "RestartIfCoopClientCountComparison",
    "SkipLinesIfPlayerGender",  # 1003[11]
    "GotoIfPlayerGender",  # 1003[12]
    "ReturnIfPlayerGender",  # 1003[13]
    "EndIfPlayerGender",
    "RestartIfPlayerGender",
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
    "GotoIfMultiplayer",
    "GotoIfConnectingMultiplayer",
    "GotoIfSingleplayer",
    "GotoIfMapPresenceState",  # 1003[107]
    "GotoIfInsideMap",
    "GotoIfOutsideMap",
    "GotoIfCoopClientCountComparison",  # 1003[109]
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
    "GotoIfObjectDestructionState",  # 1005[101]
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
    "TerminateEvent",  # 2000[1]
    "SetNetworkSyncState",  # 2000[2]
    "EnableNetworkSync",
    "DisableNetworkSync",
    "ClearMainCondition",  # 2000[3]
    "IssuePrefetchRequest",  # 2000[4]
    "SaveRequest",  # 2000[5]
    "PlayCutsceneToAll",  # 2002[1]
    "PlayCutsceneAndMovePlayer",  # 2002[2]
    "PlayCutsceneToPlayer",  # 2002[3]
    "PlayCutsceneAndMoveSpecificPlayer",  # 2002[4]
    "PlayCutsceneAndRotatePlayer",  # 2002[5]
    "PlayCutsceneAndMovePlayerAndSetTimePeriod",  # 2002[6]
    "PlayCutsceneAndSetTimePeriod",  # 2002[7]
    "PlayCutsceneAndMovePlayer_Dummy",  # 2002[8]
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
    "SetNavmeshFaceFlag",  # 2003[13]
    "AddNavmeshFaceFlag",
    "RemoveNavmeshFaceFlag",
    "ToggleNavmeshFaceFlag",
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
    "RemoveRuneFromPlayer",
    "RemoveGoodFromPlayer",
    "PlaceSummonSign",  # 2003[25]
    "SetSoapstoneMessageState",  # 2003[26]
    "EnableSoapstoneMessage",
    "DisableSoapstoneMessage",
    "Unknown_2003_27",  # 2003[27]
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
    "BossDefeat",  # 2003[53]
    "SendNPCSummonHome",  # 2003[54]
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
    "FaceEntityAndForceAnimation",  # 2004[14]
    "SetInvincibilityState",  # 2004[15]
    "EnableInvincibility",
    "DisableInvincibility",
    "ClearTargetList",  # 2004[16]
    "AICommand",  # 2004[17]
    "SetEventPoint",  # 2004[18]
    "SetAIParamID",  # 2004[19]
    "ReplanAI",  # 2004[20]
    "RemoveSpecialEffect",  # 2004[21]
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
    "ChangeCharacterCloth",  # 2004[48]
    "ChangePatrolBehavior",  # 2004[49]
    "SetDistanceLimitForConversationStateChanges",  # 2004[50]
    "Test_RequestRagdollRestraint",  # 2004[51]
    "ChangePlayerCharacterInitParam",  # 2004[52]
    "AdaptSpecialEffectHealthChangeToNPCPart",  # 2004[53]
    "SetGravityAndCollisionExcludingOwnWorld",  # 2004[54]
    "AddSpecialEffect_WithUnknownEffect",  # 2004[55]
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
    "ActivateObjectWithSpecificCharacter",  # 2005[16]
    "SetObjectDamageShieldState",  # 2005[17]
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
    "RegisterLantern",  # 2009[5]
    "NotifyBossBattleStart",  # 2009[6]
    "SetBackgroundMusic",  # 2010[1]
    "PlaySoundEffect",  # 2010[2]
    "SetSoundEventState",  # 2010[3]
    "EnableSoundEvent",
    "DisableSoundEvent",
    "SetBossMusicState",  # 2010[4]
    "EnableBossMusic",
    "DisableBossMusic",
    "NotifyDoorEventSoundDampening",  # 2010[5]
    "SetMapCollisionState",  # 2011[1]
    "EnableMapCollision",
    "DisableMapCollision",
    "SetMapCollisionBackreadMaskState",  # 2011[2]
    "EnableMapCollisionBackreadMask",
    "DisableMapCollisionBackreadMask",
    "SetCollisionResState",  # 2011[3]
    "SetMapPieceState",  # 2012[1]
    "EnableMapPiece",
    "DisableMapPiece",
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
    "IfPlayerHasRune",
    "IfPlayerHasGood",
    "IfPlayerDoesNotHaveItem",
    "IfPlayerDoesNotHaveWeapon",
    "IfPlayerDoesNotHaveArmor",
    "IfPlayerDoesNotHaveRune",
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
    "Multiplayer",
    "ConnectingMultiplayer",
    "Singleplayer",
    "AllPlayersRegionState",
    "AllPlayersInsideRegion",
    "AllPlayersOutsideRegion",
    "MapPresenceState",
    "InsideMap",
    "OutsideMap",
    "MultiplayerEvent",
    "EnabledFlagCountComparison",
    "EnabledFlagCountEqual",
    "EnabledFlagCountNotEqual",
    "EnabledFlagCountGreaterThan",
    "EnabledFlagCountLessThan",
    "EnabledFlagCountGreaterThanOrEqual",
    "EnabledFlagCountLessThanOrEqual",
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
    "AttackedWithDamageType",
    "ActionButtonParamActivated",
    "PlayerArmorInRange",
    "PlayerInsightAmountComparison",
    "PlayerInsightAmountEqual",
    "PlayerInsightAmountNotEqual",
    "PlayerInsightAmountGreaterThan",
    "PlayerInsightAmountLessThan",
    "PlayerInsightAmountGreaterThanOrEqual",
    "PlayerInsightAmountLessThanOrEqual",
    "DialogChoice",
    "PlayGoState",
    "ClientTypeCountComparison",
    "CharacterDeathState",
    "CharacterDead",
    "CharacterAlive",
    "Attacked",
    "HealthRatioComparison",
    "HealthRatioEqual",
    "HealthRatioNotEqual",
    "HealthRatioGreaterThan",
    "HealthRatioLessThan",
    "HealthRatioGreaterThanOrEqual",
    "HealthRatioLessThanOrEqual",
    "CharacterIsType",
    "CharacterIsHuman",
    "CharacterIsWhitePhantom",
    "CharacterIsHollow",
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
    "CharacterDrawGroupState",
    "CharacterDrawGroupEnabled",
    "CharacterDrawGroupDisabled",
    "ObjectDestructionState",
    "ObjectDestroyed",
    "ObjectNotDestroyed",
    "ObjectDamaged",
    "ObjectActivated",
    "ObjectHealthValueComparison",
    "PlayerMovingOnCollision",
    "PlayerRunningOnCollision",
    "PlayerStandingOnCollision",
    "ActionButton",
    "PlayerHasWeapon",
    "PlayerHasArmor",
    "PlayerHasRune",
    "PlayerHasGood",
    "PlayerDoesNotHaveWeapon",
    "PlayerDoesNotHaveArmor",
    "PlayerDoesNotHaveRune",
    "PlayerDoesNotHaveGood",
    "EnabledFlagCount",
    "WorldTendency",
    "EventValue",
    "PlayerInsightAmount",
    "ClientTypeCount",
    "HealthRatio",
    "CharacterPartHealth",
    "PlayerLevel",
    "HealthValue",
    "ObjectHealthValue",
]

import typing as tp

from soulstruct.bloodborne.game_types import *
from .emevd.compiler import *
from .enums import *

# Restart decorators. They can be used as names (not function calls) or have an event ID argument.
def ContinueOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...
def RestartOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...
def EndOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...

# Dummy enum for accessing event flags defined by events.
class EVENTS(Flag): ...


class Condition:
    """
    Create a condition group for use in `Await` or `If` instructions.
    
    If `hold = True`, the EVS parser will NOT permit the internal condition group slot assigned to this `Condition` to
    be automatically re-used once it is evaluated by the game engine and marked as OLD (e.g. by a `Main.AWAIT()` call).    
    """
    def __init__(self, condition, hold: bool = False): ...


class HeldCondition(Condition):
    """
    Alternative syntax for `Condition(condition, hold=True)`. (See above.)
    """
    def __init__(self, condition): ...


def LastResult(condition_group: ConditionGroup | Condition):
    """
    Wrap a naked condition group like `AND_1` with this to tell EVS/EMEVD that you want to check the LAST RESULT of
    this condition group rather than actively re-evaluating it.
    """    


def Await(condition):
    """
    The Await function. Equivalent to `MAIN.Await()`, which the EVS decompiler will prefer.
    
    You can also use the built-in 'await' Python keyword, but Python linters might complain about this (e.g. because
    you haven't declared your function with `async def` or because of the type being passed to `await`).
    """
    ...


# Terminators that can be returned by events as cleaner syntax.
END = ...  # use with `return END`, identical to `return` or `End()`
RESTART = ...  # use with `return RESTART`, identical to `Restart()`


# Condition groups:
OR_15 = ConditionGroup.OR_15
OR_14 = ConditionGroup.OR_14
OR_13 = ConditionGroup.OR_13
OR_12 = ConditionGroup.OR_12
OR_11 = ConditionGroup.OR_11
OR_10 = ConditionGroup.OR_10
OR_9 = ConditionGroup.OR_9
OR_8 = ConditionGroup.OR_8
OR_7 = ConditionGroup.OR_7
OR_6 = ConditionGroup.OR_6
OR_5 = ConditionGroup.OR_5
OR_4 = ConditionGroup.OR_4
OR_3 = ConditionGroup.OR_3
OR_2 = ConditionGroup.OR_2
OR_1 = ConditionGroup.OR_1
MAIN = ConditionGroup.MAIN
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


def RunEvent(event_id: int | tp.Callable, slot: int = 0, args = (0,), arg_types = ""):
    """Run an event by its ID or function. In Bloodborne, this could be a event defined in `common`."""
    ...


# (0, 0)
def IfConditionState(condition: ConditionGroup | int, state: bool | int, input_condition: ConditionGroup | int):
    """
    TODO
    """


# (0, 0)
def IfConditionTrue(condition: ConditionGroup | int, input_condition: ConditionGroup | int):
    """
    Calls `IfConditionState` with `state=True`.
    """


# (0, 0)
def IfConditionFalse(condition: ConditionGroup | int, input_condition: ConditionGroup | int):
    """
    Calls `IfConditionState` with `state=False`.
    """


# (0, 1)
def IfValueComparison(condition: ConditionGroup | int, comparison_type: ComparisonType | int, left: int, right: int):
    """
    TODO
    """


# (0, 1)
def IfValueEqual(condition: ConditionGroup | int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=0`.
    """


# (0, 1)
def IfValueNotEqual(condition: ConditionGroup | int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=1`.
    """


# (0, 1)
def IfValueGreaterThan(condition: ConditionGroup | int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=2`.
    """


# (0, 1)
def IfValueLessThan(condition: ConditionGroup | int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=3`.
    """


# (0, 1)
def IfValueGreaterThanOrEqual(condition: ConditionGroup | int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=4`.
    """


# (0, 1)
def IfValueLessThanOrEqual(condition: ConditionGroup | int, left: int, right: int):
    """
    Calls `IfValueComparison` with `comparison_type=5`.
    """


# (1, 0)
def IfTimeElapsed(condition: ConditionGroup | int, seconds: float):
    """
    Time since event started.
    """


# (1, 1)
def IfFramesElapsed(condition: ConditionGroup | int, frames: int):
    """
    Frames since event started.
    """


# (1, 2)
def IfRandomTimeElapsed(condition: ConditionGroup | int, min_seconds: float, max_seconds: float):
    """
    Not used in vanilla DS1. Requires a random amount of time since event began.
    """


# (1, 3)
def IfRandomFramesElapsed(condition: ConditionGroup | int, min_frames: int, max_frames: int):
    """
    Not used in vanilla DS1. Requires a random amount of frames since event began.
    """


# (3, 0)
def IfFlagState(condition: ConditionGroup | int, state: FlagSetting | int, flag_type: FlagType | int, flag: Flag | int):
    """
    TODO
    """


# (3, 0)
def IfFlagEnabled(condition: ConditionGroup | int, flag: Flag | int):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=0`.
    """


# (3, 0)
def IfFlagDisabled(condition: ConditionGroup | int, flag: Flag | int):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=0`.
    """


# (3, 0)
def IfThisEventFlagEnabled(condition: ConditionGroup | int):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


# (3, 0)
def IfThisEventFlagDisabled(condition: ConditionGroup | int):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


# (3, 0)
def IfThisEventSlotFlagEnabled(condition: ConditionGroup | int):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


# (3, 0)
def IfThisEventSlotFlagDisabled(condition: ConditionGroup | int):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


# (3, 1)
def IfFlagRangeState(
    condition: ConditionGroup | int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
):
    """
    TODO
    """


# (3, 1)
def IfFlagRangeAllEnabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list):
    """
    Calls `IfFlagRangeState` with `state=0`, `flag_type=0`.
    """


# (3, 1)
def IfFlagRangeAllDisabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list):
    """
    Calls `IfFlagRangeState` with `state=1`, `flag_type=0`.
    """


# (3, 1)
def IfFlagRangeAnyEnabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list):
    """
    Calls `IfFlagRangeState` with `state=2`, `flag_type=0`.
    """


# (3, 1)
def IfFlagRangeAnyDisabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list):
    """
    Calls `IfFlagRangeState` with `state=3`, `flag_type=0`.
    """


# (3, 2)
def IfCharacterRegionState(
    condition: ConditionGroup | int,
    state: bool | int,
    character: Object | Character | int,
    region: Region | int,
):
    """
    Not sure if this works for objects.
    """


# (3, 2)
def IfPlayerInsideRegion(condition: ConditionGroup | int, region: Region | int):
    """
    Calls `IfCharacterRegionState` with `state=True`, `character=10000`.
    """


# (3, 2)
def IfPlayerOutsideRegion(condition: ConditionGroup | int, region: Region | int):
    """
    Calls `IfCharacterRegionState` with `state=False`, `character=10000`.
    """


# (3, 2)
def IfCharacterInsideRegion(condition: ConditionGroup | int, character: Object | Character | int, region: Region | int):
    """
    Calls `IfCharacterRegionState` with `state=True`.
    """


# (3, 2)
def IfCharacterOutsideRegion(
    condition: ConditionGroup | int,
    character: Object | Character | int,
    region: Region | int,
):
    """
    Calls `IfCharacterRegionState` with `state=False`.
    """


# (3, 3)
def IfEntityDistanceState(
    condition: ConditionGroup | int,
    state: bool | int,
    entity: Object | Character | Region | int,
    other_entity: Object | Character | Region | int,
    radius: float,
):
    """
    TODO
    """


# (3, 3)
def IfPlayerWithinDistance(
    condition: ConditionGroup | int,
    other_entity: Object | Character | Region | int,
    radius: float,
):
    """
    Calls `IfEntityDistanceState` with `state=True`, `entity=10000`.
    """


# (3, 3)
def IfPlayerBeyondDistance(
    condition: ConditionGroup | int,
    other_entity: Object | Character | Region | int,
    radius: float,
):
    """
    Calls `IfEntityDistanceState` with `state=False`, `entity=10000`.
    """


# (3, 3)
def IfEntityWithinDistance(
    condition: ConditionGroup | int,
    entity: Object | Character | Region | int,
    other_entity: Object | Character | Region | int,
    radius: float,
):
    """
    Calls `IfEntityDistanceState` with `state=True`.
    """


# (3, 3)
def IfEntityBeyondDistance(
    condition: ConditionGroup | int,
    entity: Object | Character | Region | int,
    other_entity: Object | Character | Region | int,
    radius: float,
):
    """
    Calls `IfEntityDistanceState` with `state=False`.
    """


# (3, 4)
def IfPlayerItemStateExcludingStorage(
    condition: ConditionGroup | int,
    item: BaseItemParam | int,
    state: bool | int,
    item_type: ItemType | int = None,
):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


# (3, 5)
def IfActionButtonBasic(
    condition: ConditionGroup | int,
    prompt_text: EventText | int,
    anchor_entity: Object | Character | Region | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    dummy_id: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Basic (not "boss") version with no line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


# (3, 6)
def IfMultiplayerState(condition: ConditionGroup | int, state: MultiplayerState | int):
    """
    TODO
    """


# (3, 6)
def IfHost(condition: ConditionGroup | int):
    """
    Calls `IfMultiplayerState` with `state=0`.
    """


# (3, 6)
def IfClient(condition: ConditionGroup | int):
    """
    Calls `IfMultiplayerState` with `state=1`.
    """


# (3, 6)
def IfMultiplayer(condition: ConditionGroup | int):
    """
    Calls `IfMultiplayerState` with `state=2`.
    """


# (3, 6)
def IfConnectingMultiplayer(condition: ConditionGroup | int):
    """
    Calls `IfMultiplayerState` with `state=3`.
    """


# (3, 6)
def IfSingleplayer(condition: ConditionGroup | int):
    """
    Calls `IfMultiplayerState` with `state=4`.
    """


# (3, 7)
def IfAllPlayersRegionState(condition: ConditionGroup | int, state: bool | int, region: Region | int):
    """
    TODO
    """


# (3, 7)
def IfAllPlayersInsideRegion(condition: ConditionGroup | int, region: Region | int):
    """
    Calls `IfAllPlayersRegionState` with `state=True`.
    """


# (3, 7)
def IfAllPlayersOutsideRegion(condition: ConditionGroup | int, region: Region | int):
    """
    Calls `IfAllPlayersRegionState` with `state=False`.
    """


# (3, 8)
def IfMapPresenceState(condition: ConditionGroup | int, state: bool | int, game_map: Map | tuple | list):
    """
    Conditions upon player's presence in a particular game map.
    """


# (3, 8)
def IfInsideMap(condition: ConditionGroup | int, game_map: Map | tuple | list):
    """
    Calls `IfMapPresenceState` with `state=True`.
    """


# (3, 8)
def IfOutsideMap(condition: ConditionGroup | int, game_map: Map | tuple | list):
    """
    Calls `IfMapPresenceState` with `state=False`.
    """


# (3, 9)
def IfMultiplayerEvent(condition: ConditionGroup | int, event_id: int):
    """
    TODO
    """


# (3, 10)
def IfEnabledFlagCountComparison(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    comparison_type: ComparisonType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Conditions upon a comparison with the number of enabled flags in the given range (inclusive).
    """


# (3, 10)
def IfEnabledFlagCountEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=0`.
    """


# (3, 10)
def IfEnabledFlagCountNotEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=1`.
    """


# (3, 10)
def IfEnabledFlagCountGreaterThan(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=2`.
    """


# (3, 10)
def IfEnabledFlagCountLessThan(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=3`.
    """


# (3, 10)
def IfEnabledFlagCountGreaterThanOrEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=4`.
    """


# (3, 10)
def IfEnabledFlagCountLessThanOrEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=5`.
    """


# (3, 11)
def IfWorldTendencyComparison(
    condition: ConditionGroup | int,
    world_tendency_type: WorldTendencyType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    TODO
    """


# (3, 11)
def IfWhiteWorldTendencyComparison(condition: ConditionGroup | int, comparison_type: ComparisonType | int, value: int):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=0`.
    """


# (3, 11)
def IfBlackWorldTendencyComparison(condition: ConditionGroup | int, comparison_type: ComparisonType | int, value: int):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=1`.
    """


# (3, 11)
def IfWhiteWorldTendencyGreaterThan(condition: ConditionGroup | int, value: int):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=0`, `comparison_type=2`.
    """


# (3, 11)
def IfBlackWorldTendencyGreaterThan(condition: ConditionGroup | int, value: int):
    """
    Calls `IfWorldTendencyComparison` with `world_tendency_type=1`, `comparison_type=2`.
    """


# (3, 12)
def IfEventValueComparison(
    condition: ConditionGroup | int,
    flag: Flag | int,
    bit_count: int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    TODO
    """


# (3, 12)
def IfEventValueEqual(condition: ConditionGroup | int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=0`.
    """


# (3, 12)
def IfEventValueNotEqual(condition: ConditionGroup | int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=1`.
    """


# (3, 12)
def IfEventValueGreaterThan(condition: ConditionGroup | int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=2`.
    """


# (3, 12)
def IfEventValueLessThan(condition: ConditionGroup | int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=3`.
    """


# (3, 12)
def IfEventValueGreaterThanOrEqual(condition: ConditionGroup | int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=4`.
    """


# (3, 12)
def IfEventValueLessThanOrEqual(condition: ConditionGroup | int, flag: Flag | int, bit_count: int, value: int):
    """
    Calls `IfEventValueComparison` with `comparison_type=5`.
    """


# (3, 13)
def IfActionButtonBoss(
    condition: ConditionGroup | int,
    prompt_text: EventText | int,
    anchor_entity: Object | Character | Region | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    dummy_id: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Boss (not "basic") version with no line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


# (3, 14)
def IfAnyItemDroppedInRegion(condition: ConditionGroup | int, region: Region | int):
    """
    Check if any item has been dropped in the specified region. Not sensitive to what the item is.
    """


# (3, 15)
def IfItemDropped(condition: ConditionGroup | int, item: BaseItemParam | int, item_type: ItemType | int = None):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


# (3, 16)
def IfPlayerItemStateIncludingStorage(
    condition: ConditionGroup | int,
    item: BaseItemParam | int,
    state: bool | int,
    item_type: ItemType | int = None,
):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


# (3, 17)
def IfNewGameCycleComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    completion_count: int,
):
    """
    TODO
    """


# (3, 17)
def IfNewGameCycleEqual(condition: ConditionGroup | int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=0`.
    """


# (3, 17)
def IfNewGameCycleNotEqual(condition: ConditionGroup | int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=1`.
    """


# (3, 17)
def IfNewGameCycleGreaterThan(condition: ConditionGroup | int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=2`.
    """


# (3, 17)
def IfNewGameCycleLessThan(condition: ConditionGroup | int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=3`.
    """


# (3, 17)
def IfNewGameCycleGreaterThanOrEqual(condition: ConditionGroup | int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=4`.
    """


# (3, 17)
def IfNewGameCycleLessThanOrEqual(condition: ConditionGroup | int, completion_count: int):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=5`.
    """


# (3, 18)
def IfActionButtonBasicLineIntersect(
    condition: ConditionGroup | int,
    prompt_text: EventText | int,
    anchor_entity: Object | Character | Region | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    dummy_id: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Basic (not "boss") version with a line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


# (3, 19)
def IfActionButtonBossLineIntersect(
    condition: ConditionGroup | int,
    prompt_text: EventText | int,
    anchor_entity: Object | Character | Region | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    dummy_id: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
):
    """
    Generates an 'action button' prompt and waits for the player to activate it.
    
    Boss (not "basic") version with a line intersection check.
    
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


# (3, 20)
def IfEventsComparison(
    condition: ConditionGroup | int,
    left_flag: Flag | int,
    left_bit_count: int,
    comparison_type: ComparisonType | int,
    right_flag: Flag | int,
    right_bit_count: int,
):
    """
    Check comparison of two event flag values. Haven't bothered adding shortcut functions for this.
    """


# (3, 21)
def IfDLCState(condition: ConditionGroup | int, is_owned: bool):
    """
    TODO
    """


# (3, 21)
def IfDLCOwned(condition: ConditionGroup | int):
    """
    Calls `IfDLCState` with `is_owned=True`.
    """


# (3, 21)
def IfDLCNotOwned(condition: ConditionGroup | int):
    """
    Calls `IfDLCState` with `is_owned=False`.
    """


# (3, 22)
def IfOnlineState(condition: ConditionGroup | int, state: bool | int):
    """
    TODO
    """


# (3, 22)
def IfOnline(condition: ConditionGroup | int):
    """
    Calls `IfOnlineState` with `state=True`.
    """


# (3, 22)
def IfOffline(condition: ConditionGroup | int):
    """
    Calls `IfOnlineState` with `state=False`.
    """


# (3, 23)
def IfAttackedWithDamageType(
    condition: ConditionGroup | int,
    attacked_entity: Character | int,
    attacker: Character | int = -1,
    damage_type: DamageType | int = DamageType.Unspecified,
):
    """
    TODO
    """


# (3, 24)
def IfActionButtonParamActivated(
    condition: ConditionGroup | int,
    action_button_id: int,
    entity: Object | Character | Region | int,
):
    """
    TODO
    """


# (3, 25)
def IfPlayerArmorInRange(
    condition: ConditionGroup | int,
    armor_type: ArmorType | int,
    required_armor_range_first: ArmorParam | int,
    required_armor_range_last: ArmorParam | int,
):
    """
    TODO
    """


# (3, 26)
def IfPlayerInsightAmountComparison(condition: ConditionGroup | int, value: int, comparison_type: ComparisonType | int):
    """
    TODO
    """


# (3, 26)
def IfPlayerInsightAmountEqual(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerInsightAmountComparison` with `comparison_type=0`.
    """


# (3, 26)
def IfPlayerInsightAmountNotEqual(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerInsightAmountComparison` with `comparison_type=1`.
    """


# (3, 26)
def IfPlayerInsightAmountGreaterThan(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerInsightAmountComparison` with `comparison_type=2`.
    """


# (3, 26)
def IfPlayerInsightAmountLessThan(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerInsightAmountComparison` with `comparison_type=3`.
    """


# (3, 26)
def IfPlayerInsightAmountGreaterThanOrEqual(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerInsightAmountComparison` with `comparison_type=4`.
    """


# (3, 26)
def IfPlayerInsightAmountLessThanOrEqual(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerInsightAmountComparison` with `comparison_type=5`.
    """


# (3, 27)
def IfDialogChoice(condition: ConditionGroup | int, dialog_result: DialogResult | int):
    """
    TODO
    """


# (3, 28)
def IfPlayGoState(condition: ConditionGroup | int, playgo_state: PlayGoState | int):
    """
    Blocks off areas of the game (namely, beyond Father Gascoigne) that have not been downloaded/installed yet.
    """


# (3, 29)
def IfClientTypeCountComparison(
    condition: ConditionGroup | int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Value should only range between 0 and 4 (the maximum number of clients).
    """


# (4, 0)
def IfCharacterDeathState(condition: ConditionGroup | int, character: Character | int, is_dead: bool | int):
    """
    TODO
    """


# (4, 0)
def IfCharacterDead(condition: ConditionGroup | int, character: Character | int):
    """
    Calls `IfCharacterDeathState` with `is_dead=True`.
    """


# (4, 0)
def IfCharacterAlive(condition: ConditionGroup | int, character: Character | int):
    """
    Calls `IfCharacterDeathState` with `is_dead=False`.
    """


# (4, 1)
def IfAttacked(condition: ConditionGroup | int, attacked_entity: Character | int, attacker: Character | int):
    """
    TODO
    """


# (4, 2)
def IfHealthRatioComparison(
    condition: ConditionGroup | int,
    character: Character | int,
    comparison_type: ComparisonType | int,
    value: float,
):
    """
    Conditions upon a comparison to character health ratio (0-1).
    """


# (4, 2)
def IfHealthRatioEqual(condition: ConditionGroup | int, character: Character | int, value: float):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=0`.
    """


# (4, 2)
def IfHealthRatioNotEqual(condition: ConditionGroup | int, character: Character | int, value: float):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=1`.
    """


# (4, 2)
def IfHealthRatioGreaterThan(condition: ConditionGroup | int, character: Character | int, value: float):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=2`.
    """


# (4, 2)
def IfHealthRatioLessThan(condition: ConditionGroup | int, character: Character | int, value: float):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=3`.
    """


# (4, 2)
def IfHealthRatioGreaterThanOrEqual(condition: ConditionGroup | int, character: Character | int, value: float):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=4`.
    """


# (4, 2)
def IfHealthRatioLessThanOrEqual(condition: ConditionGroup | int, character: Character | int, value: float):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=5`.
    """


# (4, 3)
def IfCharacterIsType(condition: ConditionGroup | int, character: Character | int, character_type: CharacterType | int):
    """
    TODO
    """


# (4, 3)
def IfCharacterIsHuman(condition: ConditionGroup | int, character: Character | int):
    """
    Calls `IfCharacterIsType` with `character_type=0`.
    """


# (4, 3)
def IfCharacterIsWhitePhantom(condition: ConditionGroup | int, character: Character | int):
    """
    Calls `IfCharacterIsType` with `character_type=1`.
    """


# (4, 3)
def IfCharacterIsHollow(condition: ConditionGroup | int, character: Character | int):
    """
    Calls `IfCharacterIsType` with `character_type=8`.
    """


# (4, 4)
def IfCharacterTargetingState(
    condition: ConditionGroup | int,
    targeting_character: Character | int,
    targeted_character: Character | int,
    state: bool | int,
):
    """
    TODO
    """


# (4, 4)
def IfCharacterTargeting(
    condition: ConditionGroup | int,
    targeting_character: Character | int,
    targeted_character: Character | int,
):
    """
    Calls `IfCharacterTargetingState` with `state=True`.
    """


# (4, 4)
def IfCharacterNotTargeting(
    condition: ConditionGroup | int,
    targeting_character: Character | int,
    targeted_character: Character | int,
):
    """
    Calls `IfCharacterTargetingState` with `state=False`.
    """


# (4, 5)
def IfCharacterSpecialEffectState(
    condition: ConditionGroup | int,
    character: Character | int,
    special_effect: int,
    state: bool | int,
):
    """
    TODO
    """


# (4, 5)
def IfPlayerHasSpecialEffect(condition: ConditionGroup | int, special_effect: int):
    """
    Calls `IfCharacterSpecialEffectState` with `character=10000`, `state=True`.
    """


# (4, 5)
def IfPlayerDoesNotHaveSpecialEffect(condition: ConditionGroup | int, special_effect: int):
    """
    Calls `IfCharacterSpecialEffectState` with `character=10000`, `state=False`.
    """


# (4, 5)
def IfCharacterHasSpecialEffect(condition: ConditionGroup | int, character: Character | int, special_effect: int):
    """
    Calls `IfCharacterSpecialEffectState` with `state=True`.
    """


# (4, 5)
def IfCharacterDoesNotHaveSpecialEffect(
    condition: ConditionGroup | int,
    character: Character | int,
    special_effect: int,
):
    """
    Calls `IfCharacterSpecialEffectState` with `state=False`.
    """


# (4, 6)
def IfCharacterPartHealthComparison(
    condition: ConditionGroup | int,
    character: Character | int,
    npc_part_id: int,
    value: float,
    comparison_type: ComparisonType | int,
):
    """
    TODO
    """


# (4, 6)
def IfCharacterPartHealthLessThanOrEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    npc_part_id: int,
    value: float,
):
    """
    Calls `IfCharacterPartHealthComparison` with `comparison_type=5`.
    """


# (4, 7)
def IfCharacterBackreadState(condition: ConditionGroup | int, character: Character | int, state: bool | int):
    """
    TODO
    """


# (4, 7)
def IfCharacterBackreadEnabled(condition: ConditionGroup | int, character: Character | int):
    """
    Calls `IfCharacterBackreadState` with `state=True`.
    """


# (4, 7)
def IfCharacterBackreadDisabled(condition: ConditionGroup | int, character: Character | int):
    """
    Calls `IfCharacterBackreadState` with `state=False`.
    """


# (4, 8)
def IfCharacterTAEEventState(
    condition: ConditionGroup | int,
    character: Character | int,
    tae_event_id: int,
    state: bool | int,
):
    """
    TODO
    """


# (4, 8)
def IfCharacterHasTAEEvent(condition: ConditionGroup | int, character: Character | int, tae_event_id: int):
    """
    Calls `IfCharacterTAEEventState` with `state=True`.
    """


# (4, 8)
def IfCharacterDoesNotHaveTAEEvent(condition: ConditionGroup | int, character: Character | int, tae_event_id: int):
    """
    Calls `IfCharacterTAEEventState` with `state=False`.
    """


# (4, 9)
def IfHasAIStatus(condition: ConditionGroup | int, character: Character | int, ai_status: AIStatusType | int):
    """
    TODO
    """


# (4, 10)
def IfSkullLanternState(condition: ConditionGroup | int, state: bool | int):
    """
    TODO
    """


# (4, 10)
def IfSkullLanternActive(condition: ConditionGroup | int):
    """
    Calls `IfSkullLanternState` with `state=True`.
    """


# (4, 10)
def IfSkullLanternInactive(condition: ConditionGroup | int):
    """
    Calls `IfSkullLanternState` with `state=False`.
    """


# (4, 11)
def IfPlayerClass(condition: ConditionGroup | int, class_type: ClassType | int):
    """
    TODO
    """


# (4, 12)
def IfPlayerCovenant(condition: ConditionGroup | int, covenant: Covenant | int):
    """
    TODO
    """


# (4, 13)
def IfPlayerLevelComparison(condition: ConditionGroup | int, comparison_type: ComparisonType | int, value: int):
    """
    TODO
    """


# (4, 13)
def IfPlayerLevelEqual(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=0`.
    """


# (4, 13)
def IfPlayerLevelNotEqual(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=1`.
    """


# (4, 13)
def IfPlayerLevelGreaterThan(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=2`.
    """


# (4, 13)
def IfPlayerLevelLessThan(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=3`.
    """


# (4, 13)
def IfPlayerLevelGreaterThanOrEqual(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=4`.
    """


# (4, 13)
def IfPlayerLevelLessThanOrEqual(condition: ConditionGroup | int, value: int):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=5`.
    """


# (4, 14)
def IfHealthValueComparison(
    condition: ConditionGroup | int,
    character: Character | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    TODO
    """


# (4, 14)
def IfHealthValueEqual(condition: ConditionGroup | int, character: Character | int, value: int):
    """
    Calls `IfHealthValueComparison` with `comparison_type=0`.
    """


# (4, 14)
def IfHealthValueNotEqual(condition: ConditionGroup | int, character: Character | int, value: int):
    """
    Calls `IfHealthValueComparison` with `comparison_type=1`.
    """


# (4, 14)
def IfHealthValueGreaterThan(condition: ConditionGroup | int, character: Character | int, value: int):
    """
    Calls `IfHealthValueComparison` with `comparison_type=2`.
    """


# (4, 14)
def IfHealthValueLessThan(condition: ConditionGroup | int, character: Character | int, value: int):
    """
    Calls `IfHealthValueComparison` with `comparison_type=3`.
    """


# (4, 14)
def IfHealthValueGreaterThanOrEqual(condition: ConditionGroup | int, character: Character | int, value: int):
    """
    Calls `IfHealthValueComparison` with `comparison_type=4`.
    """


# (4, 14)
def IfHealthValueLessThanOrEqual(condition: ConditionGroup | int, character: Character | int, value: int):
    """
    Calls `IfHealthValueComparison` with `comparison_type=5`.
    """


# (4, 15)
def IfCharacterDrawGroupState(condition: ConditionGroup | int, character: Character | int, state: bool | int):
    """
    Tests if character's draw group is currently enabled or disabled.
    """


# (4, 15)
def IfCharacterDrawGroupEnabled(condition: ConditionGroup | int, character: Character | int):
    """
    Calls `IfCharacterDrawGroupState` with `state=True`.
    """


# (4, 15)
def IfCharacterDrawGroupDisabled(condition: ConditionGroup | int, character: Character | int):
    """
    Calls `IfCharacterDrawGroupState` with `state=False`.
    """


# (5, 0)
def IfObjectDestructionState(condition: ConditionGroup | int, state: bool | int, obj: Object | int):
    """
    TODO
    """


# (5, 0)
def IfObjectDestroyed(condition: ConditionGroup | int, obj: Object | int):
    """
    Calls `IfObjectDestructionState` with `state=True`.
    """


# (5, 0)
def IfObjectNotDestroyed(condition: ConditionGroup | int, obj: Object | int):
    """
    Calls `IfObjectDestructionState` with `state=False`.
    """


# (5, 1)
def IfObjectDamaged(condition: ConditionGroup | int, obj: Object | int, attacker: Character | int):
    """
    TODO
    """


# (5, 2)
def IfObjectActivated(condition: ConditionGroup | int, obj_act_id: int):
    """
    TODO
    """


# (5, 3)
def IfObjectHealthValueComparison(
    condition: ConditionGroup | int,
    obj: Object | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    TODO
    """


# (11, 0)
def IfPlayerMovingOnCollision(condition: ConditionGroup | int, collision: Collision | int):
    """
    TODO
    """


# (11, 1)
def IfPlayerRunningOnCollision(condition: ConditionGroup | int, collision: Collision | int):
    """
    TODO
    """


# (11, 2)
def IfPlayerStandingOnCollision(condition: ConditionGroup | int, collision: Collision | int):
    """
    TODO
    """


# (1000, 0)
def AwaitConditionState(state: bool | int, input_condition: ConditionGroup | int):
    """
    Not sure if this is ever really used over `IfConditionState`.
    """


# (1000, 0)
def AwaitConditionTrue(input_condition: ConditionGroup | int):
    """
    Calls `AwaitConditionState` with `state=True`.
    """


# (1000, 0)
def AwaitConditionFalse(input_condition: ConditionGroup | int):
    """
    Calls `AwaitConditionState` with `state=False`.
    """


# (1000, 1)
def SkipLinesIfConditionState(line_count: int, state: bool | int, input_condition: ConditionGroup | int):
    """
    TODO
    """


# (1000, 1)
def SkipLinesIfConditionTrue(line_count: int, input_condition: ConditionGroup | int):
    """
    Calls `SkipLinesIfConditionState` with `state=True`.
    """


# (1000, 1)
def SkipLinesIfConditionFalse(line_count: int, input_condition: ConditionGroup | int):
    """
    Calls `SkipLinesIfConditionState` with `state=False`.
    """


# (1000, 2)
def ReturnIfConditionState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    input_condition: ConditionGroup | int,
):
    """
    TODO
    """


# (1000, 2)
def EndIfConditionTrue(input_condition: ConditionGroup | int):
    """
    Calls `ReturnIfConditionState` with `event_return_type=0`, `state=True`.
    """


# (1000, 2)
def EndIfConditionFalse(input_condition: ConditionGroup | int):
    """
    Calls `ReturnIfConditionState` with `event_return_type=0`, `state=False`.
    """


# (1000, 2)
def RestartIfConditionTrue(input_condition: ConditionGroup | int):
    """
    Calls `ReturnIfConditionState` with `event_return_type=1`, `state=True`.
    """


# (1000, 2)
def RestartIfConditionFalse(input_condition: ConditionGroup | int):
    """
    Calls `ReturnIfConditionState` with `event_return_type=1`, `state=False`.
    """


# (1000, 3)
def SkipLines(line_count: int):
    """
    Unconditional line skip.
    """


# (1000, 4)
def Return(event_return_type: EventReturnType | int):
    """
    TODO
    """


# (1000, 4)
def End():
    """
    Calls `Return` with `event_return_type=0`.
    """


# (1000, 4)
def Restart():
    """
    Calls `Return` with `event_return_type=1`.
    """


# (1000, 5)
def SkipLinesIfValueComparison(line_count: int, comparison_type: ComparisonType | int, left: int, right: int):
    """
    TODO
    """


# (1000, 5)
def SkipLinesIfValueEqual(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=0`.
    """


# (1000, 5)
def SkipLinesIfValueNotEqual(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=1`.
    """


# (1000, 5)
def SkipLinesIfValueGreaterThan(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=2`.
    """


# (1000, 5)
def SkipLinesIfValueLessThan(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=3`.
    """


# (1000, 5)
def SkipLinesIfValueGreaterThanOrEqual(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=4`.
    """


# (1000, 5)
def SkipLinesIfValueLessThanOrEqual(line_count: int, left: int, right: int):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=5`.
    """


# (1000, 6)
def ReturnIfValueComparison(
    event_return_type: EventReturnType | int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
):
    """
    TODO
    """


# (1000, 6)
def EndIfValueEqual(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=0`.
    """


# (1000, 6)
def EndIfValueNotEqual(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=1`.
    """


# (1000, 6)
def EndIfValueGreaterThan(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=2`.
    """


# (1000, 6)
def EndIfValueLessThan(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=3`.
    """


# (1000, 6)
def EndIfValueGreaterThanOrEqual(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=4`.
    """


# (1000, 6)
def EndIfValueLessThanOrEqual(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=5`.
    """


# (1000, 6)
def RestartIfValueEqual(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=0`.
    """


# (1000, 6)
def RestartIfValueNotEqual(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=1`.
    """


# (1000, 6)
def RestartIfValueGreaterThan(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=2`.
    """


# (1000, 6)
def RestartIfValueLessThan(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=3`.
    """


# (1000, 6)
def RestartIfValueGreaterThanOrEqual(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=4`.
    """


# (1000, 6)
def RestartIfValueLessThanOrEqual(left: int, right: int):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=5`.
    """


# (1000, 7)
def SkipLinesIfLastConditionResultState(line_count: int, state: bool | int, input_condition: ConditionGroup | int):
    """
    Skip some number of lines if the last result of the given condition (without re-evaluating) is `state`.
    """


# (1000, 7)
def SkipLinesIfLastConditionResultTrue(line_count: int, input_condition: ConditionGroup | int):
    """
    Calls `SkipLinesIfLastConditionResultState` with `state=True`.
    """


# (1000, 7)
def SkipLinesIfLastConditionResultFalse(line_count: int, input_condition: ConditionGroup | int):
    """
    Calls `SkipLinesIfLastConditionResultState` with `state=False`.
    """


# (1000, 8)
def ReturnIfLastConditionResultState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    input_condition: ConditionGroup | int,
):
    """
    End or restart event if last condition result (without re-evaluating) is the given `state`.
    """


# (1000, 8)
def EndIfLastConditionResultTrue(input_condition: ConditionGroup | int):
    """
    Calls `ReturnIfLastConditionResultState` with `event_return_type=0`, `state=True`.
    """


# (1000, 8)
def EndIfLastConditionResultFalse(input_condition: ConditionGroup | int):
    """
    Calls `ReturnIfLastConditionResultState` with `event_return_type=0`, `state=False`.
    """


# (1000, 8)
def RestartIfLastConditionResultTrue(input_condition: ConditionGroup | int):
    """
    Calls `ReturnIfLastConditionResultState` with `event_return_type=1`, `state=True`.
    """


# (1000, 8)
def RestartIfLastConditionResultFalse(input_condition: ConditionGroup | int):
    """
    Calls `ReturnIfLastConditionResultState` with `event_return_type=1`, `state=False`.
    """


# (1000, 9)
def WaitForNetworkApproval(max_seconds: float):
    """
    Wait for network to approve event (up to `max_seconds` seconds).
    """


# (1000, 101)
def GotoIfConditionState(label: Label | int, required_state: bool | int, input_condition: ConditionGroup | int):
    """
    TODO
    """


# (1000, 101)
def GotoIfConditionTrue(label: Label | int, input_condition: ConditionGroup | int):
    """
    Calls `GotoIfConditionState` with `required_state=True`.
    """


# (1000, 101)
def GotoIfConditionFalse(label: Label | int, input_condition: ConditionGroup | int):
    """
    Calls `GotoIfConditionState` with `required_state=False`.
    """


# (1000, 103)
def Goto(label: Label | int):
    """
    Unconditional GOTO.
    """


# (1000, 105)
def GotoIfValueComparison(label: Label | int, comparison_type: ComparisonType | int, left: int, right: int):
    """
    TODO
    """


# (1000, 107)
def GotoIfLastConditionResultState(
    label: Label | int,
    required_state: bool | int,
    input_condition: ConditionGroup | int,
):
    """
    Go to label if the last result of the given condition (without re-evaluating) is `required_state`.
    """


# (1000, 107)
def GotoIfLastConditionResultTrue(label: Label | int, input_condition: ConditionGroup | int):
    """
    Calls `GotoIfLastConditionResultState` with `required_state=True`.
    """


# (1000, 107)
def GotoIfLastConditionResultFalse(label: Label | int, input_condition: ConditionGroup | int):
    """
    Calls `GotoIfLastConditionResultState` with `required_state=False`.
    """


# (1001, 0)
def Wait(seconds: float):
    """
    Wait for some number of seconds.
    """


# (1001, 1)
def WaitFrames(frames: int):
    """
    Wait for some number of frames.
    """


# (1001, 2)
def WaitRandomSeconds(min_seconds: float, max_seconds: float):
    """
    Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
    """


# (1001, 3)
def WaitRandomFrames(min_frames: int, max_frames: int):
    """
    Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
    """


# (1003, 0)
def AwaitFlagState(state: FlagSetting | int, flag_type: FlagType | int, flag: Flag | int):
    """
    Not sure if this is really used rather than `IfFlagState` with MAIN condition (0).
    """


# (1003, 0)
def AwaitFlagEnabled(flag: Flag | int):
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=0`.
    """


# (1003, 0)
def AwaitFlagDisabled(flag: Flag | int):
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=0`.
    """


# (1003, 0)
def AwaitThisEventOn():
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


# (1003, 0)
def AwaitThisEventOff():
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


# (1003, 0)
def AwaitThisEventSlotOn():
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


# (1003, 0)
def AwaitThisEventSlotOff():
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


# (1003, 1)
def SkipLinesIfFlagState(line_count: int, state: FlagSetting | int, flag_type: FlagType | int, flag: Flag | int):
    """
    Skip some number of lines if the specified flag (absolute, event-relative, or slot-relative) has the
    specified state.
    """


# (1003, 1)
def SkipLinesIfFlagEnabled(line_count: int, flag: Flag | int):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=0`.
    """


# (1003, 1)
def SkipLinesIfFlagDisabled(line_count: int, flag: Flag | int):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=0`.
    """


# (1003, 1)
def SkipLinesIfThisEventFlagEnabled(line_count: int):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


# (1003, 1)
def SkipLinesIfThisEventFlagDisabled(line_count: int):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


# (1003, 1)
def SkipLinesIfThisEventSlotFlagEnabled(line_count: int):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


# (1003, 1)
def SkipLinesIfThisEventSlotFlagDisabled(line_count: int):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


# (1003, 2)
def ReturnIfFlagState(
    event_return_type: EventReturnType | int,
    state: FlagSetting | int,
    flag_type: FlagType | int,
    flag: Flag | int,
):
    """
    TODO
    """


# (1003, 2)
def EndIfFlagEnabled(flag: Flag | int):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=0`.
    """


# (1003, 2)
def EndIfFlagDisabled(flag: Flag | int):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=0`.
    """


# (1003, 2)
def EndIfThisEventFlagEnabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=1`, `flag=0`.
    """


# (1003, 2)
def EndIfThisEventFlagDisabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=1`, `flag=0`.
    """


# (1003, 2)
def EndIfThisEventSlotFlagEnabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=2`, `flag=0`.
    """


# (1003, 2)
def EndIfThisEventSlotFlagDisabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=2`, `flag=0`.
    """


# (1003, 2)
def RestartIfFlagEnabled(flag: Flag | int):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=0`.
    """


# (1003, 2)
def RestartIfFlagDisabled(flag: Flag | int):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=0`.
    """


# (1003, 2)
def RestartIfThisEventFlagEnabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=1`, `flag=0`.
    """


# (1003, 2)
def RestartIfThisEventFlagDisabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=1`, `flag=0`.
    """


# (1003, 2)
def RestartIfThisEventSlotFlagEnabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=2`, `flag=0`.
    """


# (1003, 2)
def RestartIfThisEventSlotFlagDisabled():
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=2`, `flag=0`.
    """


# (1003, 3)
def SkipLinesIfFlagRangeState(
    line_count: int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
):
    """
    TODO
    """


# (1003, 3)
def SkipLinesIfFlagRangeAllEnabled(line_count: int, flag_range: FlagRange | tuple | list):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=0`, `flag_type=0`.
    """


# (1003, 3)
def SkipLinesIfFlagRangeAllDisabled(line_count: int, flag_range: FlagRange | tuple | list):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=1`, `flag_type=0`.
    """


# (1003, 3)
def SkipLinesIfFlagRangeAnyEnabled(line_count: int, flag_range: FlagRange | tuple | list):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=2`, `flag_type=0`.
    """


# (1003, 3)
def SkipLinesIfFlagRangeAnyDisabled(line_count: int, flag_range: FlagRange | tuple | list):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=3`, `flag_type=0`.
    """


# (1003, 4)
def ReturnIfFlagRangeState(
    event_return_type: EventReturnType | int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
):
    """
    TODO
    """


# (1003, 4)
def EndIfFlagRangeAllEnabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=0`, `flag_type=0`.
    """


# (1003, 4)
def EndIfFlagRangeAllDisabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=1`, `flag_type=0`.
    """


# (1003, 4)
def EndIfFlagRangeAnyEnabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=2`, `flag_type=0`.
    """


# (1003, 4)
def EndIfFlagRangeAnyDisabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=3`, `flag_type=0`.
    """


# (1003, 4)
def RestartIfFlagRangeAllEnabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=0`, `flag_type=0`.
    """


# (1003, 4)
def RestartIfFlagRangeAllDisabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=1`, `flag_type=0`.
    """


# (1003, 4)
def RestartIfFlagRangeAnyEnabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=2`, `flag_type=0`.
    """


# (1003, 4)
def RestartIfFlagRangeAnyDisabled(flag_range: FlagRange | tuple | list):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=3`, `flag_type=0`.
    """


# (1003, 5)
def SkipLinesIfMultiplayerState(line_count: int, state: MultiplayerState | int):
    """
    TODO
    """


# (1003, 5)
def SkipLinesIfHost(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=0`.
    """


# (1003, 5)
def SkipLinesIfClient(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=1`.
    """


# (1003, 5)
def SkipLinesIfMultiplayer(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=2`.
    """


# (1003, 5)
def SkipLinesIfConnectingMultiplayer(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=3`.
    """


# (1003, 5)
def SkipLinesIfSingleplayer(line_count: int):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=4`.
    """


# (1003, 6)
def ReturnIfMultiplayerState(event_return_type: EventReturnType | int, state: MultiplayerState | int):
    """
    TODO
    """


# (1003, 6)
def EndIfHost():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=0`.
    """


# (1003, 6)
def EndIfClient():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=1`.
    """


# (1003, 6)
def EndIfMultiplayer():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=2`.
    """


# (1003, 6)
def EndIfConnectingMultiplayer():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=3`.
    """


# (1003, 6)
def EndIfSingleplayer():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=4`.
    """


# (1003, 6)
def RestartIfHost():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=0`.
    """


# (1003, 6)
def RestartIfClient():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=1`.
    """


# (1003, 6)
def RestartIfMultiplayer():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=2`.
    """


# (1003, 6)
def RestartIfConnectingMultiplayer():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=3`.
    """


# (1003, 6)
def RestartIfSingleplayer():
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=4`.
    """


# (1003, 7)
def SkipLinesIfMapPresenceState(line_count: int, state: bool | int, game_map: Map | tuple | list):
    """
    TODO
    """


# (1003, 7)
def SkipLinesIfInsideMap(line_count: int, game_map: Map | tuple | list):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=True`.
    """


# (1003, 7)
def SkipLinesIfOutsideMap(line_count: int, game_map: Map | tuple | list):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=False`.
    """


# (1003, 8)
def ReturnIfMapPresenceState(event_return_type: EventReturnType | int, state: bool | int, game_map: Map | tuple | list):
    """
    TODO
    """


# (1003, 8)
def EndIfInsideMap(game_map: Map | tuple | list):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=True`.
    """


# (1003, 8)
def EndIfOutsideMap(game_map: Map | tuple | list):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=False`.
    """


# (1003, 8)
def RestartIfInsideMap(game_map: Map | tuple | list):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=True`.
    """


# (1003, 8)
def RestartIfOutsideMap(game_map: Map | tuple | list):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=False`.
    """


# (1003, 9)
def SkipLinesIfCoopClientCountComparison(skip_lines: int, comparison_type: ComparisonType | int, value: int):
    """
    Value should be from 0 to 4.
    """


# (1003, 10)
def ReturnIfCoopClientCountComparison(
    event_return_type: EventReturnType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    TODO
    """


# (1003, 10)
def EndIfCoopClientCountComparison(comparison_type: ComparisonType | int, value: int):
    """
    Calls `ReturnIfCoopClientCountComparison` with `event_return_type=0`.
    """


# (1003, 10)
def RestartIfCoopClientCountComparison(comparison_type: ComparisonType | int, value: int):
    """
    Calls `ReturnIfCoopClientCountComparison` with `event_return_type=1`.
    """


# (1003, 11)
def SkipLinesIfPlayerGender(skip_lines: int, gender: Gender | int):
    """
    TODO
    """


# (1003, 12)
def GotoIfPlayerGender(label: Label | int, gender: Gender | int):
    """
    TODO
    """


# (1003, 13)
def ReturnIfPlayerGender(event_return_type: EventReturnType | int, gender: Gender | int):
    """
    TODO
    """


# (1003, 13)
def EndIfPlayerGender(gender: Gender | int):
    """
    Calls `ReturnIfPlayerGender` with `event_return_type=0`.
    """


# (1003, 13)
def RestartIfPlayerGender(gender: Gender | int):
    """
    Calls `ReturnIfPlayerGender` with `event_return_type=1`.
    """


# (1003, 14)
def SkipLinesIfClientTypeCountComparison(
    skip_lines: int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Value from 0 to 4.
    """


# (1003, 15)
def GotoIfClientTypeCountComparison(
    label: Label | int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Value from 0 to 4.
    """


# (1003, 16)
def ReturnIfClientTypeCountComparison(
    event_return_type: EventReturnType | int,
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Value from 0 to 4.
    """


# (1003, 16)
def EndIfClientTypeCountComparison(client_type: ClientType | int, comparison_type: ComparisonType | int, value: int):
    """
    Calls `ReturnIfClientTypeCountComparison` with `event_return_type=0`.
    """


# (1003, 16)
def RestartIfClientTypeCountComparison(
    client_type: ClientType | int,
    comparison_type: ComparisonType | int,
    value: int,
):
    """
    Calls `ReturnIfClientTypeCountComparison` with `event_return_type=1`.
    """


# (1003, 101)
def GotoIfFlagState(label: Label | int, state: bool | int, flag_type: FlagType | int, flag: Flag | int):
    """
    TODO
    """


# (1003, 101)
def GotoIfThisEventFlagEnabled(label: Label | int):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=1`, `flag=0`.
    """


# (1003, 101)
def GotoIfThisEventFlagDisabled(label: Label | int):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=1`, `flag=0`.
    """


# (1003, 101)
def GotoIfThisEventSlotFlagEnabled(label: Label | int):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=2`, `flag=0`.
    """


# (1003, 101)
def GotoIfThisEventSlotFlagDisabled(label: Label | int):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=2`, `flag=0`.
    """


# (1003, 101)
def GotoIfFlagEnabled(label: Label | int, flag: Flag | int):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=0`.
    """


# (1003, 101)
def GotoIfFlagDisabled(label: Label | int, flag: Flag | int):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=0`.
    """


# (1003, 103)
def GotoIfFlagRangeState(
    label: Label | int,
    state: RangeState | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
):
    """
    TODO
    """


# (1003, 103)
def GotoIfFlagRangeAllEnabled(label: Label | int, flag_range: FlagRange | tuple | list):
    """
    Calls `GotoIfFlagRangeState` with `state=0`, `flag_type=0`.
    """


# (1003, 103)
def GotoIfFlagRangeAllDisabled(label: Label | int, flag_range: FlagRange | tuple | list):
    """
    Calls `GotoIfFlagRangeState` with `state=1`, `flag_type=0`.
    """


# (1003, 103)
def GotoIfFlagRangeAnyEnabled(label: Label | int, flag_range: FlagRange | tuple | list):
    """
    Calls `GotoIfFlagRangeState` with `state=2`, `flag_type=0`.
    """


# (1003, 103)
def GotoIfFlagRangeAnyDisabled(label: Label | int, flag_range: FlagRange | tuple | list):
    """
    Calls `GotoIfFlagRangeState` with `state=3`, `flag_type=0`.
    """


# (1003, 105)
def GotoIfMultiplayerState(label: Label | int, state: MultiplayerState | int):
    """
    TODO
    """


# (1003, 105)
def GotoIfHost(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=0`.
    """


# (1003, 105)
def GotoIfClient(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=1`.
    """


# (1003, 105)
def GotoIfMultiplayer(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=2`.
    """


# (1003, 105)
def GotoIfConnectingMultiplayer(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=3`.
    """


# (1003, 105)
def GotoIfSingleplayer(label: Label | int):
    """
    Calls `GotoIfMultiplayerState` with `state=4`.
    """


# (1003, 107)
def GotoIfMapPresenceState(label: Label | int, state: bool | int, game_map: Map | tuple | list):
    """
    TODO
    """


# (1003, 107)
def GotoIfInsideMap(label: Label | int, game_map: Map | tuple | list):
    """
    Calls `GotoIfMapPresenceState` with `state=True`.
    """


# (1003, 107)
def GotoIfOutsideMap(label: Label | int, game_map: Map | tuple | list):
    """
    Calls `GotoIfMapPresenceState` with `state=False`.
    """


# (1003, 109)
def GotoIfCoopClientCountComparison(label: Label | int, comparison_type: ComparisonType | int, value: int):
    """
    TODO
    """


# (1005, 0)
def AwaitObjectDestructionState(state: bool | int, obj: Object | int):
    """
    TODO
    """


# (1005, 0)
def AwaitObjectDestroyed(obj: Object | int):
    """
    Calls `AwaitObjectDestructionState` with `state=True`.
    """


# (1005, 0)
def AwaitObjectNotDestroyed(obj: Object | int):
    """
    Calls `AwaitObjectDestructionState` with `state=False`.
    """


# (1005, 1)
def SkipLinesIfObjectDestructionState(line_count: int, state: bool | int, obj: Object | int):
    """
    TODO
    """


# (1005, 1)
def SkipLinesIfObjectDestroyed(line_count: int, obj: Object | int):
    """
    Calls `SkipLinesIfObjectDestructionState` with `state=True`.
    """


# (1005, 1)
def SkipLinesIfObjectNotDestroyed(line_count: int, obj: Object | int):
    """
    Calls `SkipLinesIfObjectDestructionState` with `state=False`.
    """


# (1005, 2)
def ReturnIfObjectDestructionState(event_return_type: EventReturnType | int, state: bool | int, obj: Object | int):
    """
    TODO
    """


# (1005, 2)
def EndIfObjectDestroyed(obj: Object | int):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=0`, `state=True`.
    """


# (1005, 2)
def EndIfObjectNotDestroyed(obj: Object | int):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=0`, `state=False`.
    """


# (1005, 2)
def RestartIfObjectDestroyed(obj: Object | int):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=1`, `state=True`.
    """


# (1005, 2)
def RestartIfObjectNotDestroyed(obj: Object | int):
    """
    Calls `ReturnIfObjectDestructionState` with `event_return_type=1`, `state=False`.
    """


# (1005, 101)
def GotoIfObjectDestructionState(label: Label | int, state: bool | int, obj: Object | int):
    """
    TODO
    """


# (1014, 0)
def DefineLabel_0():
    """
    Define position of label 0 for Goto instructions.
    """


# (1014, 1)
def DefineLabel_1():
    """
    Define position of label 1 for Goto instructions.
    """


# (1014, 2)
def DefineLabel_2():
    """
    Define position of label 2 for Goto instructions.
    """


# (1014, 3)
def DefineLabel_3():
    """
    Define position of label 3 for Goto instructions.
    """


# (1014, 4)
def DefineLabel_4():
    """
    Define position of label 4 for Goto instructions.
    """


# (1014, 5)
def DefineLabel_5():
    """
    Define position of label 5 for Goto instructions.
    """


# (1014, 6)
def DefineLabel_6():
    """
    Define position of label 6 for Goto instructions.
    """


# (1014, 7)
def DefineLabel_7():
    """
    Define position of label 7 for Goto instructions.
    """


# (1014, 8)
def DefineLabel_8():
    """
    Define position of label 8 for Goto instructions.
    """


# (1014, 9)
def DefineLabel_9():
    """
    Define position of label 9 for Goto instructions.
    """


# Instruction `RunEvent` (2000, 0) is defined in the `compiler` module.


# (2000, 1)
def TerminateEvent(event_slot: int, event_id: int):
    """
    Delete an instance (slot) of an event script.
    """


# (2000, 2)
def SetNetworkSyncState(state: bool | int):
    """
    TODO
    """


# (2000, 2)
def EnableNetworkSync():
    """
    Calls `SetNetworkSyncState` with `state=True`.
    """


# (2000, 2)
def DisableNetworkSync():
    """
    Calls `SetNetworkSyncState` with `state=False`.
    """


# (2000, 3)
def ClearMainCondition(dummy: int = 0):
    """
    Likely clears all conditions currently loaded into the main condition (0).
    """


# (2000, 4)
def IssuePrefetchRequest(request_id: int):
    """
    No idea what this does.
    """


# (2000, 5)
def SaveRequest(dummy: int = 0):
    """
    Request the game to save player progress.
    """


# (2002, 1)
def PlayCutsceneToAll(cutscene_id: int, cutscene_flags: CutsceneFlags | int):
    """
    TODO
    """


# (2002, 2)
def PlayCutsceneAndMovePlayer(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    game_map: Map | tuple | list,
):
    """
    TODO
    """


# (2002, 3)
def PlayCutsceneToPlayer(cutscene_id: int, cutscene_flags: CutsceneFlags | int, player_id: int):
    """
    TODO
    """


# (2002, 4)
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


# (2002, 5)
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


# (2002, 6)
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


# (2002, 7)
def PlayCutsceneAndSetTimePeriod(
    cutscene: int,
    cutscene_flags: CutsceneFlags | int,
    player_id: int,
    time_period_id: int,
):
    """
    Probably used when you examine Laurence's skull, etc.
    """


# (2002, 8)
def PlayCutsceneAndMovePlayer_Dummy(move_to_region: Region | int, game_map: Map | tuple | list):
    """
    Likely not used, doesn't even take a cutscene ID argument.
    """


# (2003, 1)
def RequestAnimation(
    entity: Object | Character | int,
    animation_id: int,
    loop: bool | int = False,
    wait_for_completion: bool | int = False,
):
    """
    Not used very often, in favor of ForceAnimation below.
    """


# (2003, 2)
def SetFlagState(flag: Flag | int, state: FlagSetting | int):
    """
    Enable, disable, or toggle (change) a binary flag.
    """


# (2003, 2)
def EnableFlag(flag: Flag | int):
    """
    Calls `SetFlagState` with `state=1`.
    """


# (2003, 2)
def DisableFlag(flag: Flag | int):
    """
    Calls `SetFlagState` with `state=0`.
    """


# (2003, 2)
def ToggleFlag(flag: Flag | int):
    """
    Calls `SetFlagState` with `state=2`.
    """


# (2003, 3)
def SetSpawnerState(entity: Object | Character | Region | int, state: bool | int):
    """
    e.g. the baby skeletons in Tomb of the Giants.
    """


# (2003, 3)
def EnableSpawner(entity: Object | Character | Region | int):
    """
    Calls `SetSpawnerState` with `state=True`.
    """


# (2003, 3)
def DisableSpawner(entity: Object | Character | Region | int):
    """
    Calls `SetSpawnerState` with `state=False`.
    """


# (2003, 4)
def AwardItemLotToAllPlayers(item_lot: int):
    """
    TODO
    """


# (2003, 5)
def ShootProjectile(
    owner_entity: Object | Character | Region | int,
    source_entity: Object | Character | Region | int,
    dummy_id: int,
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


# (2003, 8)
def SetEventState(event_id: int, event_return_type: EventReturnType | int, event_slot: int = 0):
    """
    Stop or restart a particular slot (default of 0) of the given event ID. Note that you cannot restart events
    that have already ended.
    """


# (2003, 8)
def StopEvent(event_id: int, event_slot: int = 0):
    """
    Calls `SetEventState` with `event_return_type=0`.
    Force a running event to stop.
    """


# (2003, 8)
def RestartEvent(event_id: int, event_slot: int = 0):
    """
    Calls `SetEventState` with `event_return_type=1`.
    
    Force a running event to restart. Note that the event must be active (i.e. not finished) for this
    to work. If you plan to have an event restarted, make sure it doesn't return until you no longer
    need it.
    """


# (2003, 11)
def SetBossHealthBarState(character: Character | int, state: bool | int, name: NPCName | int = 0, bar_slot: int = 0):
    """
    Note: slot number can be 0-2 in BB.
    """


# (2003, 11)
def EnableBossHealthBar(character: Character | int, name: NPCName | int = 0, bar_slot: int = 0):
    """
    Calls `SetBossHealthBarState` with `state=True`.
    The character's health bar will appear at the bottom of the screen, with a name.
    """


# (2003, 11)
def DisableBossHealthBar(character: Character | int, name: NPCName | int = 0, bar_slot: int = 0):
    """
    Calls `SetBossHealthBarState` with `state=False`.
    
    The character's health bar will disappear from the bottom of the screen.
    
    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter,
    so only the first argument actually does anything. You're welcome to specify the name for
    clarity anyway (and vanilla events will show it when decompiled).
    """


# (2003, 12)
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


# (2003, 13)
def SetNavmeshFaceFlag(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int, operation: BitOperation | int):
    """
    Set given navmesh type.
    """


# (2003, 13)
def AddNavmeshFaceFlag(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int):
    """
    Calls `SetNavmeshFaceFlag` with `operation=0`.
    """


# (2003, 13)
def RemoveNavmeshFaceFlag(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int):
    """
    Calls `SetNavmeshFaceFlag` with `operation=1`.
    """


# (2003, 13)
def ToggleNavmeshFaceFlag(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int):
    """
    Calls `SetNavmeshFaceFlag` with `operation=2`.
    """


# (2003, 14)
def WarpToMap(game_map: Map | tuple | list, player_start: PlayerStart | int = -1):
    """
    Warp the main player to the given player entity ID, which is in the Players tab of the MSB, in some map. By
    default, this warps to the 'default position' in the map (-1), which is the same point you would spawn at if
    the game lost track of your stable footing (e.g. in 'wrong warp' glitches).
    """


# (2003, 15)
def HandleMinibossDefeat(miniboss_id: int):
    """
    Called instead of `KillBoss` for bosses that aren't the final boss of the area.
    
    Note that outside of Chalice Dungeons, this is ONLY used when you have defeated Gehrman and are about to
    fight Moon Presence.
    """


# (2003, 16)
def TriggerMultiplayerEvent(event_id: int):
    """
    Used to make the Bell of Awakening sounds, for example.
    """


# (2003, 17)
def SetRandomFlagInRange(flag_range: FlagRange | tuple | list, state: FlagSetting | int):
    """
    Set the state of a random flag from a given range (inclusive).
    """


# (2003, 17)
def EnableRandomFlagInRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetRandomFlagInRange` with `state=1`.
    """


# (2003, 17)
def DisableRandomFlagInRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetRandomFlagInRange` with `state=0`.
    """


# (2003, 17)
def ToggleRandomFlagInRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetRandomFlagInRange` with `state=2`.
    """


# (2003, 18)
def ForceAnimation(
    entity: Object | Character | int,
    animation_id: int,
    loop: bool | int = False,
    wait_for_completion: bool | int = False,
    skip_transition: bool | int = False,
):
    """
    Used a lot. Standard way to make a Character or Object perform an animation.
    """


# (2003, 19)
def SetMapDrawParamSlot(map_area_id: int, draw_param_slot: int):
    """
    Each map area (NOT each map) can have two sets of DrawParams (0 and 1), and this can be used to switch
    between them. Originally only used for Dark Anor Londo.
    
    Note that there's some funny business with how this works in m15 in Dark Souls Remastered, presumably
    because the developers didn't want to bother modifying both slots when they re-did all the DrawParams.
    """


# (2003, 21)
def IncrementNewGameCycle(dummy_arg: int):
    """
    This is manually called at the end of the game. You can call it anytime, but note that there is no way to
    decrement it with events.
    
    The dummy argument is always 0 or 1; not sure if or how it matters.
    """


# (2003, 22)
def SetFlagRangeState(flag_range: FlagRange | tuple | list, state: FlagSetting | int):
    """
    Set the state of an entire flag range (inclusive).
    """


# (2003, 22)
def EnableFlagRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetFlagRangeState` with `state=1`.
    """


# (2003, 22)
def DisableFlagRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetFlagRangeState` with `state=0`.
    """


# (2003, 22)
def ToggleFlagRange(flag_range: FlagRange | tuple | list):
    """
    Calls `SetFlagRangeState` with `state=2`.
    """


# (2003, 23)
def SetRespawnPoint(respawn_point: int):
    """
    Respawn point is an event set in the MSB.
    """


# (2003, 24)
def RemoveItemFromPlayer(item: BaseItemParam | int, quantity: int = 0, item_type: ItemType | int = None):
    """
    Item type is automatically detected. This instruction has a 'quantity' argument, but it seems broken, so you
    always have to remove *all* instances of the item. (Strangely, the similar command used in EzState doesn't
    seem to have this bug.)
    
    WARNING: don't confuse 'Item' with the specific item type 'Good'.
    
    item_type: Auto-detected from `item` type by default.
    """


# (2003, 24)
def RemoveWeaponFromPlayer(item: BaseItemParam | int, quantity: int = 0):
    """
    Calls `RemoveItemFromPlayer` with `item_type=0`.
    """


# (2003, 24)
def RemoveArmorFromPlayer(item: BaseItemParam | int, quantity: int = 0):
    """
    Calls `RemoveItemFromPlayer` with `item_type=1`.
    """


# (2003, 24)
def RemoveRuneFromPlayer(item: BaseItemParam | int, quantity: int = 0):
    """
    Calls `RemoveItemFromPlayer` with `item_type=2`.
    """


# (2003, 24)
def RemoveGoodFromPlayer(item: BaseItemParam | int, quantity: int = 0):
    """
    Calls `RemoveItemFromPlayer` with `item_type=3`.
    """


# (2003, 25)
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


# (2003, 26)
def SetSoapstoneMessageState(message_id: int, state: bool | int):
    """
    Enable or disable developer message.
    """


# (2003, 26)
def EnableSoapstoneMessage(message_id: int):
    """
    Calls `SetSoapstoneMessageState` with `state=True`.
    """


# (2003, 26)
def DisableSoapstoneMessage(message_id: int):
    """
    Calls `SetSoapstoneMessageState` with `state=False`.
    """


# (2003, 27)
def Unknown_2003_27(arg1: int):
    """
    No information. Used exactly once, after the cutscene that played when Ludwig's first phase was defeated
    with the Old Hunters DLC demo flag enabled. Unknown effect. Maybe just terminated the whole DLC demo.
    """


# (2003, 28)
def AwardAchievement(achievement_id: int):
    """
    For obvious reasons, I *highly* discourage you from abusing this, except in the interest of maintaining the
    accessibility of existing achievements. This interacts with Steam, which is always dangerous.
    """


# (2003, 30)
def SetVagrantSpawningState(spawning_disabled: bool | int):
    """
    Note inverted bool.
    """


# (2003, 30)
def EnableVagrantSpawning():
    """
    Calls `SetVagrantSpawningState` with `spawning_disabled=False`.
    """


# (2003, 30)
def DisableVagrantSpawning():
    """
    Calls `SetVagrantSpawningState` with `spawning_disabled=True`.
    """


# (2003, 31)
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


# (2003, 32)
def ClearEventValue(flag: Flag | int, bit_count: int):
    """
    Clears the given multi-flag. This is basically like disabling `bit_count` flags in a row, starting at
    `flag`.
    """


# (2003, 33)
def SetNextSnugglyTrade(flag: Flag | int):
    """
    Sets the flag for the next drop based on the item you deposit into the nest.
    """


# (2003, 34)
def SnugglyItemDrop(item_lot: ItemLotParam | int, region: Region | int, flag: Flag | int, collision: Collision | int):
    """
    Makes Snuggly drop an item. There are complex limitations to this in the engine, so be careful. (The list of
    available Snuggly flags is a hard-coded limit, for example.)
    """


# (2003, 35)
def MoveRemains(source_region: Region | int, destination_region: Region | int):
    """
    Move all bloodstains and dropped items from one region to another (I assume). Used to move your
    remains out of Gwyndolin's endless corridor.
    """


# (2003, 36)
def AwardItemLotToHostOnly(item_lot: int):
    """
    You can simply call AwardItemLot() with the same argument, which will redirect here, as you'll almost never
    *not* want to award an item lot to the host only.
    """


# (2003, 37)
def ArenaRankingRequest1v1():
    """
    TODO
    """


# (2003, 38)
def ArenaRankingRequest2v2():
    """
    TODO
    """


# (2003, 39)
def ArenaRankingRequestFFA():
    """
    TODO
    """


# (2003, 40)
def ArenaExitRequest():
    """
    TODO
    """


# (2003, 41)
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


# (2003, 42)
def StoreItemAmountSpecifiedByFlagValue(
    item_type: ItemType | int,
    item: BaseItemParam | int,
    flag: Flag | int,
    bit_count: int,
):
    """
    Stores some amount of items read from a flag array.
    """


# (2003, 43)
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


# (2003, 44)
def SetDirectionDisplayState(state: bool | int):
    """
    Not sure what this is.
    """


# (2003, 44)
def EnableDirectionDisplayState():
    """
    Calls `SetDirectionDisplayState` with `state=True`.
    """


# (2003, 44)
def DisableDirectionDisplayState():
    """
    Calls `SetDirectionDisplayState` with `state=False`.
    """


# (2003, 45)
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


# (2003, 45)
def EnableMapHitGridCorrespondence(collision: Collision | int, level: int, grid_coord_x: int, grid_coord_y: int):
    """
    Calls `SetMapHitGridCorrespondence` with `state=True`.
    """


# (2003, 45)
def DisableMapHitGridCorrespondence(collision: Collision | int, level: int, grid_coord_x: int, grid_coord_y: int):
    """
    Calls `SetMapHitGridCorrespondence` with `state=False`.
    """


# (2003, 46)
def SetMapContentImageDisplayState(content_image_part_id: int, state: bool | int):
    """
    TODO
    """


# (2003, 47)
def SetMapBoundariesDisplay(hierarchy: int, grid_coord_x: int, grid_coord_y: int, state: bool | int):
    """
    TODO
    """


# (2003, 48)
def SetAreaWind(region: Region | int, state: bool | int, duration: float, wind_parameter_id: int):
    """
    TODO
    """


# (2003, 49)
def WarpPlayerToRespawnPoint(respawn_point_id: int):
    """
    TODO
    """


# (2003, 50)
def StartEnemySpawner(spawner_id: int):
    """
    TODO
    """


# (2003, 51)
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


# (2003, 52)
def InitializeWarpObject(warp_object_id: int):
    """
    TODO
    """


# (2003, 53)
def BossDefeat(boss_id: int, banner_type: BannerType | int):
    """
    Handle boss defeat and display banner. 'boss_id' is probably similar to GameAreaParam from DS1.
    """


# (2003, 54)
def SendNPCSummonHome(character: Character | int):
    """
    TODO
    """


# (2004, 1)
def SetAIState(character: Character | int, state: bool | int):
    """
    TODO
    """


# (2004, 1)
def EnableAI(character: Character | int):
    """
    Calls `SetAIState` with `state=True`.
    """


# (2004, 1)
def DisableAI(character: Character | int):
    """
    Calls `SetAIState` with `state=False`.
    """


# (2004, 2)
def SetTeamType(character: Character | int, new_team: TeamType | int):
    """
    TODO
    """


# (2004, 3)
def MoveToEntity(
    character: Character | int,
    destination: Object | Character | Region | int,
    dummy_id: int = -1,
    destination_type: CoordEntityType | int = None,
):
    """
    Basic move. I recommend you use the combined `Move` function.
    destination_type: Auto-detected from `destination` type by default.
    """


# (2004, 4)
def Kill(character: Character | int, award_souls: bool | int = False):
    """
    Technically a kill 'request.'
    """


# (2004, 5)
def SetCharacterState(character: Character | int, state: bool | int):
    """
    TODO
    """


# (2004, 5)
def EnableCharacter(character: Character | int):
    """
    Calls `SetCharacterState` with `state=True`.
    """


# (2004, 5)
def DisableCharacter(character: Character | int):
    """
    Calls `SetCharacterState` with `state=False`.
    """


# (2004, 6)
def EzstateAIRequest(character: Character | int, command_id: int, command_slot: int):
    """
    Slot number ranges from 0 to 3.
    """


# (2004, 7)
def CreateProjectileOwner(entity: Object | Character | Region | int):
    """
    A 'bullet owner' that will spawn things according to the Spawner section of the MSB.
    """


# (2004, 8)
def AddSpecialEffect(character: Character | int, special_effect: int, affect_npc_part_hp: bool | int = False):
    """
    'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will
    do nothing if the character already has the special effect active (i.e. they do not stack or reset timers).
    
    The Bloodborne version has an additional argument that determines whether any HP changes caused by the
    special effect should also affect NPC parts, which I set to `False` by default (more common).
    """


# (2004, 9)
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


# (2004, 9)
def ResetStandbyAnimationSettings(character: Character | int):
    """
    Calls `SetStandbyAnimationSettings` with `standby_animation=-1`, `damage_animation=-1`, `cancel_animation=-1`,
    `death_animation=-1`, `standby_exit_animation=-1`.
    """


# (2004, 10)
def SetGravityState(character: Character | int, state: bool | int):
    """
    Simply determines if the character loses height as it moves around. They will still gain height by running
    up slopes.
    """


# (2004, 10)
def EnableGravity(character: Character | int):
    """
    Calls `SetGravityState` with `state=True`.
    """


# (2004, 10)
def DisableGravity(character: Character | int):
    """
    Calls `SetGravityState` with `state=False`.
    """


# (2004, 11)
def SetCharacterEventTarget(character: Character | int, entity: Object | Character | Region | int):
    """
    Likely refers to patrolling behavior.
    """


# (2004, 12)
def SetImmortalityState(character: Character | int, state: bool | int):
    """
    Character will take damage, but not die (i.e. cannot go below 1 HP).
    """


# (2004, 12)
def EnableImmortality(character: Character | int):
    """
    Calls `SetImmortalityState` with `state=True`.
    """


# (2004, 12)
def DisableImmortality(character: Character | int):
    """
    Calls `SetImmortalityState` with `state=False`.
    """


# (2004, 13)
def SetNest(character: Character | int, region: Region | int):
    """
    Home point for entity AI.
    """


# (2004, 14)
def FaceEntityAndForceAnimation(
    character: Character | int,
    target_entity: Object | Character | Region | int,
    animation: int = -1,
    wait_for_completion: bool | int = False,
):
    """
    Rotate a character to face a target map entity of any type, then optionally force an animation.
    
    WARNING: This may crash an event script if `character` is currently disabled!
    """


# (2004, 15)
def SetInvincibilityState(character: Character | int, state: bool | int):
    """
    Character cannot take damage or die.
    """


# (2004, 15)
def EnableInvincibility(character: Character | int):
    """
    Calls `SetInvincibilityState` with `state=True`.
    """


# (2004, 15)
def DisableInvincibility(character: Character | int):
    """
    Calls `SetInvincibilityState` with `state=False`.
    """


# (2004, 16)
def ClearTargetList(character: Character | int):
    """
    Clear list of targets from character AI.
    """


# (2004, 17)
def AICommand(character: Character | int, command_id: int, command_slot: int):
    """
    The given `command_id` can be accessed in AI Lua scripts with `ai:GetEventRequest(slot)`.
    """


# (2004, 18)
def SetEventPoint(character: Character | int, region: Region | int, reaction_range: float):
    """
    Not sure what the usage of this is, but it is likely used to change patrol behavior.
    """


# (2004, 19)
def SetAIParamID(character: Character | int, ai_param_id: int):
    """
    Change character's AI parameter index.
    """


# (2004, 20)
def ReplanAI(character: Character | int):
    """
    Clear current AI goal list and force character to replan it.
    """


# (2004, 21)
def RemoveSpecialEffect(character: Character | int, special_effect: int):
    """
    'Special effect' as in a buff/debuff, not graphical effects (though they may come with one).
    """


# (2004, 22)
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


# (2004, 23)
def SetNPCPartHealth(character: Character | int, npc_part_id: int, desired_health: int, overwrite_max: bool):
    """
    You must create the part first.
    """


# (2004, 24)
def SetNPCPartEffects(character: Character | int, npc_part_id: int, material_sfx_id: int, material_vfx_id: int):
    """
    Attach material effects to an NPC part.
    """


# (2004, 25)
def SetNPCPartBulletDamageScaling(character: Character | int, npc_part_id: int, desired_scaling: float):
    """
    Scale the damage dealt to the part. Usually used to set damage to zero, e.g. Smough's hammer.
    """


# (2004, 26)
def SetDisplayMask(character: Character | int, bit_index: int, switch_type: OnOffChange | int):
    """
    Different bits correspond to different parts of the character model. You can see the initial values for
    these in the NPC params. This is generally used to disable tails when they are cut off.
    
    `switch_type` can be 0 (off), 1 (on), or 2 (change).
    """


# (2004, 27)
def SetCollisionMask(character: Character | int, bit_index: int, switch_type: OnOffChange | int):
    """
    See above. This affects the NPC's Collision, not appearance.
    """


# (2004, 28)
def SetNetworkUpdateAuthority(character: Character | int, authority_level: UpdateAuthority | int):
    """
    Complex; look at existing usage. Authority level must be 'Normal' or 'Forced'.
    """


# (2004, 29)
def SetBackreadState(character: Character | int, remove: bool):
    """
    I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread'
    of a character has a larger effect on game resources. It is used, for example, to disable the Fair Lady and
    Eingyi during the Demon Firesage boss fight.
    
    Also note reversed bool.
    """


# (2004, 29)
def EnableBackread(character: Character | int):
    """
    Calls `SetBackreadState` with `remove=False`.
    """


# (2004, 29)
def DisableBackread(character: Character | int):
    """
    Calls `SetBackreadState` with `remove=True`.
    """


# (2004, 30)
def SetHealthBarState(character: Character | int, state: bool | int):
    """
    Normal health bar that appears above character.
    """


# (2004, 30)
def EnableHealthBar(character: Character | int):
    """
    Calls `SetHealthBarState` with `state=True`.
    """


# (2004, 30)
def DisableHealthBar(character: Character | int):
    """
    Calls `SetHealthBarState` with `state=False`.
    """


# (2004, 31)
def SetCharacterCollisionState(character: Character | int, is_disabled: bool):
    """
    Note that the bool is inverted from what you might expect.
    """


# (2004, 31)
def EnableCharacterCollision(character: Character | int):
    """
    Calls `SetCharacterCollisionState` with `is_disabled=False`.
    """


# (2004, 31)
def DisableCharacterCollision(character: Character | int):
    """
    Calls `SetCharacterCollisionState` with `is_disabled=True`.
    """


# (2004, 32)
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


# (2004, 33)
def ReferDamageToEntity(character: Character | int, target_entity: Character | int):
    """
    All damage dealt to the first character will *also* (not *only*) be dealt to the target entity. I'm not 100%
    sure if the target entity can be an Object.
    
    Only used by the Four Kings in the vanilla game.
    """


# (2004, 34)
def SetNetworkUpdateRate(character: Character | int, is_fixed: bool, update_rate: CharacterUpdateRate | int):
    """
    Not sure what 'is_fixed' does. I believe only 'Always' and 'Never' are used in the vanilla game.
    """


# (2004, 35)
def SetBackreadStateAlternate(character: Character | int, state: bool | int):
    """
    I have no idea how this differs from the standard backread function above.
    """


# (2004, 36)
def HellkiteBreathControl(character: Character | int, obj: Object | int, animation_id: int):
    """
    I don't recommend you mess with this. It seems to be used to create the fire VFX and damaging effect when
    the Hellkite breathes fire on the bridge, with (otherwise invisible) object model o1060. It may simply
    trigger a certain behavior param ID.
    
    Unclear whether the animation applies to the character or object (which is probably an invisible "burning"
    plane).
    """


# (2004, 37)
def DropMandatoryTreasure(character: Character | int):
    """
    This will disable the character and spawn any treasure they would drop. It's possible that it only spawns
    treasure that has a 100% drop rate, hence the name, but I haven't confirmed this.
    """


# (2004, 38)
def BetrayCurrentCovenant(dummy: int = 0):
    """
    Dummy argument does nothing.
    """


# (2004, 39)
def SetAnimationsState(entity: Object | Character | int, state: bool | int):
    """
    TODO
    """


# (2004, 39)
def EnableAnimations(entity: Object | Character | int):
    """
    Calls `SetAnimationsState` with `state=True`.
    """


# (2004, 39)
def DisableAnimations(entity: Object | Character | int):
    """
    Calls `SetAnimationsState` with `state=False`.
    """


# (2004, 40)
def MoveAndSetDrawParent(
    character: Character | int,
    destination: Object | Character | Region | int,
    set_draw_parent: MapPart | int,
    dummy_id: int = -1,
    destination_type: CoordEntityType | int = None,
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


# (2004, 41)
def ShortMove(
    character: Character | int,
    destination: Object | Character | Region | int,
    dummy_id: int = -1,
    destination_type: CoordEntityType | int = None,
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


# (2004, 42)
def MoveAndCopyDrawParent(
    character: Character | int,
    destination: Object | Character | Region | int,
    copy_draw_parent: Object | Character | int,
    dummy_id: int = -1,
    destination_type: CoordEntityType | int = None,
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


# (2004, 43)
def ResetAnimation(character: Character | int, disable_interpolation: bool | int = False):
    """
    Cancels an animation. Note the inverted bool for controlling interpolation.
    """


# (2004, 44)
def SetTeamTypeAndExitStandbyAnimation(character: Character | int, team_type: TeamType | int):
    """
    Two for the price of one. Often used when NPCs with resting animations become hostile.
    """


# (2004, 45)
def HumanityRegistration(character: Character | int, event_flag: Flag | int):
    """
    I believe this designates the first event flag in a range of eight, which tracks how much humanity an NPC
    has for draining with Dark Hand. These flags are all in the 8000 range, and tightly packed, so you'll need
    to find your own range if you want to replicate this.
    
    I can confirm that NOT doing this for a new NPC means you can't drain any humanity from them, rather than
    being able to drain unlimited humanity.
    """


# (2004, 46)
def IncrementPvPSin(dummy: int = 0):
    """
    Normally only happens when you kill an NPC.
    """


# (2004, 47)
def EqualRecovery():
    """
    Unknown effect. Only used in Battle of Stoicism, so likely useless to you.
    """


# (2004, 48)
def ChangeCharacterCloth(character: Character | int, bit_count: int, state_id: int):
    """
    TODO
    """


# (2004, 49)
def ChangePatrolBehavior(character: Character | int, patrol_information_id: int):
    """
    I don't know what a 'patrol_information_id' actually is.
    """


# (2004, 50)
def SetDistanceLimitForConversationStateChanges(character: Character | int, distance: float):
    """
    TODO
    """


# (2004, 51)
def Test_RequestRagdollRestraint(
    recipient_character: Character | int,
    recipient_target_rigid_index: int,
    recipient_dummy_id: int,
    attachment_character: Character | int,
    attachment_target_rigid_index: int,
    attachment_dummy_id: int,
):
    """
    TODO
    """


# (2004, 52)
def ChangePlayerCharacterInitParam(character_init_param: int):
    """
    I assume this affects the player.
    """


# (2004, 53)
def AdaptSpecialEffectHealthChangeToNPCPart(character: Character | int):
    """
    TODO
    """


# (2004, 54)
def SetGravityAndCollisionExcludingOwnWorld(character: Character | int, state: bool | int):
    """
    I assume "own world" refers to the world you're hosting.
    """


# (2004, 55)
def AddSpecialEffect_WithUnknownEffect(
    character: Character | int,
    special_effect: int,
    affect_npc_parts_hp: bool | int = False,
):
    """
    Unknown additional affect from the standard instruction, presumably.
    """


# (2005, 1)
def DestroyObject(obj: Object | int, request_slot: int = 1):
    """
    Technically 'requests' the object's destruction. No idea what the slot number does.
    """


# (2005, 2)
def RestoreObject(obj: Object | int):
    """
    The opposite of destruction. Restores it to its original MSB coordinates.
    """


# (2005, 3)
def SetObjectState(obj: Object | int, state: bool | int):
    """
    TODO
    """


# (2005, 3)
def EnableObject(obj: Object | int):
    """
    Calls `SetObjectState` with `state=True`.
    """


# (2005, 3)
def DisableObject(obj: Object | int):
    """
    Calls `SetObjectState` with `state=False`.
    """


# (2005, 4)
def SetTreasureState(obj: Object | int, state: bool | int):
    """
    TODO
    """


# (2005, 4)
def EnableTreasure(obj: Object | int):
    """
    Calls `SetTreasureState` with `state=True`.
    Enables any treasure attached to this object by MSB events.
    """


# (2005, 4)
def DisableTreasure(obj: Object | int):
    """
    Calls `SetTreasureState` with `state=False`.
    
    Disables any treasure attached to this object by MSB events.
    
    If you want to disable treasure by default, you can do it in the MSB by changing a certain event
    value to 255.
    """


# (2005, 5)
def ActivateObject(obj: Object | int, obj_act_id: int, relative_index: int):
    """
    Manually call a specific ObjAct event attached to this object. I believe 'relative_index' refers to the
    points on the object at which it can be activated (e.g. which side of a gate you are on).
    
    Note that this will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how
    the game gets Patches to pull the lever in the Catacombs.
    """


# (2005, 6)
def SetObjectActivation(obj: Object | int, obj_act_id: int, state: bool | int):
    """
    Sets whether the object can be activated (1) or not activated (0).
    """


# (2005, 7)
def EndOfAnimation(obj: Object | int, animation_id: int):
    """
    Sets entity to whatever state it would have after the given animation. Used often to open doors that have
    already been opened when you reload the map, etc. I doubt it can be used with characters, but haven't
    confirmed.
    """


# (2005, 8)
def PostDestruction(obj: Object | int, request_slot: int = 1):
    """
    Sets the object to whatever appearance it would have after being destroyed. Again, not sure what 'slot'
    does, but it's literally *always* 1 in vanilla scripts (and from my testing, the instruction doesn't work
    with `slot=0`).
    """


# (2005, 9)
def CreateHazard(
    obj_flag: Flag | int,
    obj: Object | int,
    dummy_id: int,
    behavior_param_id: int,
    target_type: DamageTargetType | int,
    radius: float,
    life: float,
    repetition_time: float,
):
    """
    Turn an object into an environmental hazard. It deals damage when touched according to the NPC Behavior
    params you give it. The dummy_id determines which part of the object is hazardous (with the given radius
    and life, relative to the time this instruction occurs).
    
    An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.
    
    'target_type' determines what the hazard can damage (Character and/or Map).
    """


# (2005, 10)
def RegisterStatue(obj: Object | int, game_map: Map | tuple | list, statue_type: StatueType | int):
    """
    Creates a petrified or crystallized statue. I believe this is so it can be seen by other players online.
    """


# (2005, 11)
def MoveObjectToCharacter(obj: Object | int, character: Character | int, dummy_id: int = -1):
    """
    Move an object to a character.
    """


# (2005, 12)
def RemoveObjectFlag(obj_flag: Flag | int):
    """
    No idea what this does. I believe it might undo the CreateHazard instruction, at least.
    """


# (2005, 13)
def SetObjectInvulnerabilityState(obj: Object | int, state: bool | int):
    """
    1 = invulnerable.
    """


# (2005, 13)
def EnableObjectInvulnerability(obj: Object | int):
    """
    Calls `SetObjectInvulnerabilityState` with `state=True`.
    """


# (2005, 13)
def DisableObjectInvulnerability(obj: Object | int):
    """
    Calls `SetObjectInvulnerabilityState` with `state=False`.
    """


# (2005, 14)
def SetObjectActivationWithIdx(obj: Object | int, obj_act_id: int, relative_index: int, state: bool | int):
    """
    Similar to SetObjectActivation, but you can provide the relative index to disable (e.g. one side of a door).
    """


# (2005, 15)
def EnableTreasureCollection(obj: Object | int):
    """
    Forces an object to spawn its treasure, even if the treasure's ItemLot flag is already enabled.
    
    Useful if you want some treasure to reappear (after, say, taking it from the player and disabling the
    ItemLot flag) without the player needing to reload the map.
    """


# (2005, 16)
def ActivateObjectWithSpecificCharacter(
    obj: Object | int,
    objact_id: int,
    relative_index: int,
    character: Character | int,
):
    """
    The standard version of this 'grabs' the nearest character and uses them in the ObjAct (e.g. Patches pulling
    the lever in the Catacombs in DS1). I presume this version lets you specify which character should be
    involved in the ObjAct.
    """


# (2005, 17)
def SetObjectDamageShieldState(obj: Object | int, state: bool | int):
    """
    Not sure how this differs from object invulnerability.
    """


# (2006, 1)
def DeleteVFX(vfx_id: VFXEvent | int, erase_root_only: bool = True):
    """
    Delete visual VFX. If 'erase_root_only' is True (default), effect particles already emitted will live out
    the rest of their lifetimes (e.g. making a fog gate disappear organically). The ID is given in the MSB.
    """


# (2006, 2)
def CreateVFX(vfx_id: VFXEvent | int):
    """
    Create visual VFX. The ID is given in the MSB (e.g. fog effect for boss gates and checkpoints).
    """


# (2006, 3)
def CreateTemporaryVFX(
    vfx_id: int,
    anchor_entity: Object | Character | Region | int,
    dummy_id: int = -1,
    anchor_type: CoordEntityType | int = None,
):
    """
    Create one-off visual VFX (an FFX ID) attached to the given 'anchor_entity'. The VFX, of course, must be
    currently loaded (or in common effects).
    
    anchor_type: Auto-detected from `anchor_entity` type by default. Sets `Character` type for `PLAYER`.
    """


# (2006, 4)
def CreateObjectVFX(obj: Object | int, vfx_id: int, dummy_id: int):
    """
    TODO
    """


# (2006, 5)
def DeleteObjectVFX(obj: Object | int, erase_root: bool = True):
    """
    Note `erase_root` vs. `erase_root_only` for map SFX.
    """


# (2007, 1)
def DisplayDialog(
    text: EventText | int,
    anchor_entity: Object | Character | Region | int = -1,
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


# (2007, 2)
def DisplayBanner(banner_type: BannerType | int):
    """
    Display a pre-rendered banner. You'll have to change the textures (in menu_local.tpf) to change them.
    """


# (2007, 3)
def DisplayStatus(text: EventText | int, pad_enabled: bool = True):
    """
    Displays a large message that appears at the top of the screen, such as the message that tells you how to
    remove your curse, or that the golden fog gates block your path. If 'pad_enabled' is False, you can't get
    rid of the message until it times out on its own.
    """


# (2007, 4)
def DisplayBattlefieldMessage(text: EventText | int, display_location_index: int):
    """
    Displays a flashing messages at the bottom of the screen that does not block player input.
    """


# (2007, 5)
def ArenaSetNametag1(player_id: int):
    """
    TODO
    """


# (2007, 6)
def ArenaSetNametag2(player_id: int):
    """
    TODO
    """


# (2007, 7)
def ArenaSetNametag3(player_id: int):
    """
    TODO
    """


# (2007, 8)
def ArenaSetNametag4(player_id: int):
    """
    TODO
    """


# (2007, 9)
def DisplayArenaDissolutionMessage(text: EventText | int):
    """
    TODO
    """


# (2008, 1)
def ChangeCamera(normal_camera_id: int, locked_camera_id: int):
    """
    TODO
    """


# (2008, 2)
def SetCameraVibration(
    vibration_id: int,
    anchor_entity: Object | Character | Region | int,
    dummy_id: int = -1,
    decay_start_distance: float = 999.0,
    decay_end_distance: float = 999.0,
    anchor_type: CoordEntityType | int = None,
):
    """
    TODO
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


# (2008, 3)
def SetLockedCameraSlot(game_map: Map | tuple | list, camera_slot: int):
    """
    Switch between one of two camera slots associated with the player's current collision in the MSB.
    """


# (2009, 0)
def RegisterLadder(start_climbing_flag: Flag | int, stop_climbing_flag: Flag | int, obj: Object | int):
    """
    Don't mess with these flags, generally; you can just delay when this is called after map load to disable
    certain ladders (which is kind of weird anyway).
    """


# (2009, 1)
def InitializeWanderingDemon(flag: Flag | int, demon_entity: Character | int, appearance_flag: Flag | int):
    """
    Unused. Probably a Demon's Souls remnant.
    """


# (2009, 2)
def RegisterWanderingDemon(
    flag: Flag | int,
    demon_entity: Character | int,
    unknown_entity: Object | Character | Region | int,
):
    """
    Unused. Probably a Demon's Souls remnant.
    """


# (2009, 3)
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


# (2009, 4)
def ActivateMultiplayerBuffs(character: Character | int):
    """
    Used to strengthen bosses based on the number of summons you have. Not sure if it works for every NPC. It
    could also be tied to certain special effects; haven't checked that yet.
    """


# (2009, 5)
def RegisterLantern(
    flag: Flag | int,
    obj: Object | int,
    reaction_distance: float,
    reaction_angle: float,
    initial_sword_number: int = 0,
    sword_level: int = 0,
):
    """
    Register a Lantern. Used instead of the bonfire registration.
    
    No idea what the 'sword' arguments do, but they default to zero and are always zero when this is called.
    """


# (2009, 6)
def NotifyBossBattleStart(dummy: int = 0):
    """
    Sends the message to all summons that the host has challenged the boss.
    """


# (2010, 1)
def SetBackgroundMusic(
    state: bool | int,
    music_slot: int,
    entity: Object | Character | Region | int,
    sound_type: SoundType | int,
    sound_id: int,
):
    """
    TODO
    """


# (2010, 2)
def PlaySoundEffect(
    anchor_entity: Object | Character | Region | int,
    sound_id: int,
    sound_type: SoundType | int = None,
):
    """
    Anchor entity determines sound position and the sound type is used to look up the source.
    """


# (2010, 3)
def SetSoundEventState(sound_id: SoundEvent | int, state: bool | int):
    """
    The sound ID is in the MSB. Includes boss music, which is obviously the most common use, and ambiance.
    """


# (2010, 3)
def EnableSoundEvent(sound_id: SoundEvent | int):
    """
    Calls `SetSoundEventState` with `state=True`.
    """


# (2010, 3)
def DisableSoundEvent(sound_id: SoundEvent | int):
    """
    Calls `SetSoundEventState` with `state=False`.
    """


# (2010, 4)
def SetBossMusicState(sound_id: SoundEvent | int, state: bool | int):
    """
    Not sure how this differs from the standard map sound instructions, but my guess is that it fades the music
    out rather than abruptly stopping it.
    
    TODO: Can probably be used to fade out ANY music. Not sure why it would only work for boss music.
    TODO: Argument -1 is sometimes used. Fades out ALL music?
    """


# (2010, 4)
def EnableBossMusic(sound_id: SoundEvent | int):
    """
    Calls `SetBossMusicState` with `state=True`.
    """


# (2010, 4)
def DisableBossMusic(sound_id: SoundEvent | int):
    """
    Calls `SetBossMusicState` with `state=False`.
    """


# (2010, 5)
def NotifyDoorEventSoundDampening(obj: Object | int, state: DoorState | int):
    """
    No idea what this is or what entity the first argument is. Probably the door object.
    """


# (2011, 1)
def SetMapCollisionState(collision: Collision | int, state: bool | int):
    """
    Enable or disable a map collision (HKX). The ID is specified in the MSB. Note that a Collision doesn't have
    to be solid ground, but could be anything triggered by collision, such as a kill plane (which this is often
    used to disable).
    """


# (2011, 1)
def EnableMapCollision(collision: Collision | int):
    """
    Calls `SetMapCollisionState` with `state=True`.
    """


# (2011, 1)
def DisableMapCollision(collision: Collision | int):
    """
    Calls `SetMapCollisionState` with `state=False`.
    """


# (2011, 2)
def SetMapCollisionBackreadMaskState(collision: Collision | int, state: bool | int):
    """
    Unused.
    """


# (2011, 2)
def EnableMapCollisionBackreadMask(collision: Collision | int):
    """
    Calls `SetMapCollisionBackreadMaskState` with `state=True`.
    """


# (2011, 2)
def DisableMapCollisionBackreadMask(collision: Collision | int):
    """
    Calls `SetMapCollisionBackreadMaskState` with `state=False`.
    """


# (2011, 3)
def SetCollisionResState(collision: Collision | int, state: bool | int):
    """
    No idea what this is.
    """


# (2012, 1)
def SetMapPieceState(map_piece_id: MapPiece | int, state: bool | int):
    """
    Set the visibility of individual map pieces (e.g. all the crystals in Seath's tower).
    """


# (2012, 1)
def EnableMapPiece(map_piece_id: MapPiece | int):
    """
    Calls `SetMapPieceState` with `state=True`.
    """


# (2012, 1)
def DisableMapPiece(map_piece_id: MapPiece | int):
    """
    Calls `SetMapPieceState` with `state=False`.
    """


# (2013, 1)
def CreatePlayLog(name: StringOffset | int):
    """
    TODO
    """


# (2013, 2)
def StartPlayLogMeasurement(measurement_id: int, name: StringOffset | int, overwrite: bool | int):
    """
    TODO
    """


# (2013, 3)
def StopPlayLogMeasurement(measurement_id: int):
    """
    TODO
    """


# (2013, 4)
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


def ValueComparison(comparison_type: ComparisonType | int, left: int, right: int) -> bool:
    ...


def ValueEqual(left: int, right: int) -> bool:
    ...


def ValueNotEqual(left: int, right: int) -> bool:
    ...


def ValueGreaterThan(left: int, right: int) -> bool:
    ...


def ValueLessThan(left: int, right: int) -> bool:
    ...


def ValueGreaterThanOrEqual(left: int, right: int) -> bool:
    ...


def ValueLessThanOrEqual(left: int, right: int) -> bool:
    ...


def TimeElapsed(seconds: float) -> bool:
    ...


def FramesElapsed(frames: int) -> bool:
    ...


def RandomTimeElapsed(min_seconds: float, max_seconds: float) -> bool:
    ...


def RandomFramesElapsed(min_frames: int, max_frames: int) -> bool:
    ...


def FlagState(state: FlagSetting | int, flag_type: FlagType | int, flag: Flag | int) -> bool:
    ...


def FlagEnabled(flag: Flag | int) -> bool:
    ...


def FlagDisabled(flag: Flag | int) -> bool:
    ...


def ThisEventFlagEnabled() -> bool:
    ...


def ThisEventFlagDisabled() -> bool:
    ...


def ThisEventSlotFlagEnabled() -> bool:
    ...


def ThisEventSlotFlagDisabled() -> bool:
    ...


def FlagRangeState(state: RangeState | int, flag_type: FlagType | int, flag_range: FlagRange | tuple | list) -> bool:
    ...


def FlagRangeAllEnabled(flag_range: FlagRange | tuple | list) -> bool:
    ...


def FlagRangeAllDisabled(flag_range: FlagRange | tuple | list) -> bool:
    ...


def FlagRangeAnyEnabled(flag_range: FlagRange | tuple | list) -> bool:
    ...


def FlagRangeAnyDisabled(flag_range: FlagRange | tuple | list) -> bool:
    ...


def CharacterRegionState(state: bool | int, character: Object | Character | int, region: Region | int) -> bool:
    ...


def PlayerInsideRegion(region: Region | int) -> bool:
    ...


def PlayerOutsideRegion(region: Region | int) -> bool:
    ...


def CharacterInsideRegion(character: Object | Character | int, region: Region | int) -> bool:
    ...


def CharacterOutsideRegion(character: Object | Character | int, region: Region | int) -> bool:
    ...


def EntityDistanceState(
    state: bool | int,
    entity: Object | Character | Region | int,
    other_entity: Object | Character | Region | int,
    radius: float,
) -> bool:
    ...


def PlayerWithinDistance(other_entity: Object | Character | Region | int, radius: float) -> bool:
    ...


def PlayerBeyondDistance(other_entity: Object | Character | Region | int, radius: float) -> bool:
    ...


def EntityWithinDistance(
    entity: Object | Character | Region | int,
    other_entity: Object | Character | Region | int,
    radius: float,
) -> bool:
    ...


def EntityBeyondDistance(
    entity: Object | Character | Region | int,
    other_entity: Object | Character | Region | int,
    radius: float,
) -> bool:
    ...


def PlayerItemStateExcludingStorage(item: BaseItemParam | int, state: bool | int, item_type: ItemType | int = None) -> bool:
    ...


def ActionButtonBasic(
    prompt_text: EventText | int,
    anchor_entity: Object | Character | Region | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    dummy_id: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
) -> bool:
    ...


def MultiplayerState(state: MultiplayerState | int) -> bool:
    ...


def Host() -> bool:
    ...


def Client() -> bool:
    ...


def Multiplayer() -> bool:
    ...


def ConnectingMultiplayer() -> bool:
    ...


def Singleplayer() -> bool:
    ...


def AllPlayersRegionState(state: bool | int, region: Region | int) -> bool:
    ...


def AllPlayersInsideRegion(region: Region | int) -> bool:
    ...


def AllPlayersOutsideRegion(region: Region | int) -> bool:
    ...


def MapPresenceState(state: bool | int, game_map: Map | tuple | list) -> bool:
    ...


def InsideMap(game_map: Map | tuple | list) -> bool:
    ...


def OutsideMap(game_map: Map | tuple | list) -> bool:
    ...


def MultiplayerEvent(event_id: int) -> bool:
    ...


def EnabledFlagCountComparison(
    flag_type: FlagType | int,
    comparison_type: ComparisonType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
) -> bool:
    ...


def EnabledFlagCountEqual(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int) -> bool:
    ...


def EnabledFlagCountNotEqual(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int) -> bool:
    ...


def EnabledFlagCountGreaterThan(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int) -> bool:
    ...


def EnabledFlagCountLessThan(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int) -> bool:
    ...


def EnabledFlagCountGreaterThanOrEqual(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int) -> bool:
    ...


def EnabledFlagCountLessThanOrEqual(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int) -> bool:
    ...


def WorldTendencyComparison(
    world_tendency_type: WorldTendencyType | int,
    comparison_type: ComparisonType | int,
    value: int,
) -> bool:
    ...


def WhiteWorldTendencyComparison(comparison_type: ComparisonType | int, value: int) -> bool:
    ...


def BlackWorldTendencyComparison(comparison_type: ComparisonType | int, value: int) -> bool:
    ...


def WhiteWorldTendencyGreaterThan(value: int) -> bool:
    ...


def BlackWorldTendencyGreaterThan(value: int) -> bool:
    ...


def EventValueComparison(flag: Flag | int, bit_count: int, comparison_type: ComparisonType | int, value: int) -> bool:
    ...


def EventValueEqual(flag: Flag | int, bit_count: int, value: int) -> bool:
    ...


def EventValueNotEqual(flag: Flag | int, bit_count: int, value: int) -> bool:
    ...


def EventValueGreaterThan(flag: Flag | int, bit_count: int, value: int) -> bool:
    ...


def EventValueLessThan(flag: Flag | int, bit_count: int, value: int) -> bool:
    ...


def EventValueGreaterThanOrEqual(flag: Flag | int, bit_count: int, value: int) -> bool:
    ...


def EventValueLessThanOrEqual(flag: Flag | int, bit_count: int, value: int) -> bool:
    ...


def ActionButtonBoss(
    prompt_text: EventText | int,
    anchor_entity: Object | Character | Region | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    dummy_id: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
) -> bool:
    ...


def AnyItemDroppedInRegion(region: Region | int) -> bool:
    ...


def ItemDropped(item: BaseItemParam | int, item_type: ItemType | int = None) -> bool:
    ...


def PlayerItemStateIncludingStorage(item: BaseItemParam | int, state: bool | int, item_type: ItemType | int = None) -> bool:
    ...


def NewGameCycleComparison(comparison_type: ComparisonType | int, completion_count: int) -> bool:
    ...


def NewGameCycleEqual(completion_count: int) -> bool:
    ...


def NewGameCycleNotEqual(completion_count: int) -> bool:
    ...


def NewGameCycleGreaterThan(completion_count: int) -> bool:
    ...


def NewGameCycleLessThan(completion_count: int) -> bool:
    ...


def NewGameCycleGreaterThanOrEqual(completion_count: int) -> bool:
    ...


def NewGameCycleLessThanOrEqual(completion_count: int) -> bool:
    ...


def ActionButtonBasicLineIntersect(
    prompt_text: EventText | int,
    anchor_entity: Object | Character | Region | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    dummy_id: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
) -> bool:
    ...


def ActionButtonBossLineIntersect(
    prompt_text: EventText | int,
    anchor_entity: Object | Character | Region | int,
    line_intersects: int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    dummy_id: int = -1,
    max_distance: float = None,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
) -> bool:
    ...


def EventsComparison(
    left_flag: Flag | int,
    left_bit_count: int,
    comparison_type: ComparisonType | int,
    right_flag: Flag | int,
    right_bit_count: int,
) -> bool:
    ...


def DLCState(is_owned: bool) -> bool:
    ...


def DLCOwned() -> bool:
    ...


def DLCNotOwned() -> bool:
    ...


def OnlineState(state: bool | int) -> bool:
    ...


def Online() -> bool:
    ...


def Offline() -> bool:
    ...


def AttackedWithDamageType(
    attacked_entity: Character | int,
    attacker: Character | int = -1,
    damage_type: DamageType | int = DamageType.Unspecified,
) -> bool:
    ...


def ActionButtonParamActivated(action_button_id: int, entity: Object | Character | Region | int) -> bool:
    ...


def PlayerArmorInRange(
    armor_type: ArmorType | int,
    required_armor_range_first: ArmorParam | int,
    required_armor_range_last: ArmorParam | int,
) -> bool:
    ...


def PlayerInsightAmountComparison(value: int, comparison_type: ComparisonType | int) -> bool:
    ...


def PlayerInsightAmountEqual(value: int) -> bool:
    ...


def PlayerInsightAmountNotEqual(value: int) -> bool:
    ...


def PlayerInsightAmountGreaterThan(value: int) -> bool:
    ...


def PlayerInsightAmountLessThan(value: int) -> bool:
    ...


def PlayerInsightAmountGreaterThanOrEqual(value: int) -> bool:
    ...


def PlayerInsightAmountLessThanOrEqual(value: int) -> bool:
    ...


def DialogChoice(dialog_result: DialogResult | int) -> bool:
    ...


def PlayGoState(playgo_state: PlayGoState | int) -> bool:
    ...


def ClientTypeCountComparison(client_type: ClientType | int, comparison_type: ComparisonType | int, value: int) -> bool:
    ...


def CharacterDeathState(character: Character | int, is_dead: bool | int) -> bool:
    ...


def CharacterDead(character: Character | int) -> bool:
    ...


def CharacterAlive(character: Character | int) -> bool:
    ...


def Attacked(attacked_entity: Character | int, attacker: Character | int) -> bool:
    ...


def HealthRatioComparison(character: Character | int, comparison_type: ComparisonType | int, value: float) -> bool:
    ...


def HealthRatioEqual(character: Character | int, value: float) -> bool:
    ...


def HealthRatioNotEqual(character: Character | int, value: float) -> bool:
    ...


def HealthRatioGreaterThan(character: Character | int, value: float) -> bool:
    ...


def HealthRatioLessThan(character: Character | int, value: float) -> bool:
    ...


def HealthRatioGreaterThanOrEqual(character: Character | int, value: float) -> bool:
    ...


def HealthRatioLessThanOrEqual(character: Character | int, value: float) -> bool:
    ...


def CharacterIsType(character: Character | int, character_type: CharacterType | int) -> bool:
    ...


def CharacterIsHuman(character: Character | int) -> bool:
    ...


def CharacterIsWhitePhantom(character: Character | int) -> bool:
    ...


def CharacterIsHollow(character: Character | int) -> bool:
    ...


def CharacterTargetingState(
    targeting_character: Character | int,
    targeted_character: Character | int,
    state: bool | int,
) -> bool:
    ...


def CharacterTargeting(targeting_character: Character | int, targeted_character: Character | int) -> bool:
    ...


def CharacterNotTargeting(targeting_character: Character | int, targeted_character: Character | int) -> bool:
    ...


def CharacterSpecialEffectState(character: Character | int, special_effect: int, state: bool | int) -> bool:
    ...


def PlayerHasSpecialEffect(special_effect: int) -> bool:
    ...


def PlayerDoesNotHaveSpecialEffect(special_effect: int) -> bool:
    ...


def CharacterHasSpecialEffect(character: Character | int, special_effect: int) -> bool:
    ...


def CharacterDoesNotHaveSpecialEffect(character: Character | int, special_effect: int) -> bool:
    ...


def CharacterPartHealthComparison(
    character: Character | int,
    npc_part_id: int,
    value: float,
    comparison_type: ComparisonType | int,
) -> bool:
    ...


def CharacterPartHealthLessThanOrEqual(character: Character | int, npc_part_id: int, value: float) -> bool:
    ...


def CharacterBackreadState(character: Character | int, state: bool | int) -> bool:
    ...


def CharacterBackreadEnabled(character: Character | int) -> bool:
    ...


def CharacterBackreadDisabled(character: Character | int) -> bool:
    ...


def CharacterTAEEventState(character: Character | int, tae_event_id: int, state: bool | int) -> bool:
    ...


def CharacterHasTAEEvent(character: Character | int, tae_event_id: int) -> bool:
    ...


def CharacterDoesNotHaveTAEEvent(character: Character | int, tae_event_id: int) -> bool:
    ...


def HasAIStatus(character: Character | int, ai_status: AIStatusType | int) -> bool:
    ...


def SkullLanternState(state: bool | int) -> bool:
    ...


def SkullLanternActive() -> bool:
    ...


def SkullLanternInactive() -> bool:
    ...


def PlayerClass(class_type: ClassType | int) -> bool:
    ...


def PlayerCovenant(covenant: Covenant | int) -> bool:
    ...


def PlayerLevelComparison(comparison_type: ComparisonType | int, value: int) -> bool:
    ...


def PlayerLevelEqual(value: int) -> bool:
    ...


def PlayerLevelNotEqual(value: int) -> bool:
    ...


def PlayerLevelGreaterThan(value: int) -> bool:
    ...


def PlayerLevelLessThan(value: int) -> bool:
    ...


def PlayerLevelGreaterThanOrEqual(value: int) -> bool:
    ...


def PlayerLevelLessThanOrEqual(value: int) -> bool:
    ...


def HealthValueComparison(character: Character | int, comparison_type: ComparisonType | int, value: int) -> bool:
    ...


def HealthValueEqual(character: Character | int, value: int) -> bool:
    ...


def HealthValueNotEqual(character: Character | int, value: int) -> bool:
    ...


def HealthValueGreaterThan(character: Character | int, value: int) -> bool:
    ...


def HealthValueLessThan(character: Character | int, value: int) -> bool:
    ...


def HealthValueGreaterThanOrEqual(character: Character | int, value: int) -> bool:
    ...


def HealthValueLessThanOrEqual(character: Character | int, value: int) -> bool:
    ...


def CharacterDrawGroupState(character: Character | int, state: bool | int) -> bool:
    ...


def CharacterDrawGroupEnabled(character: Character | int) -> bool:
    ...


def CharacterDrawGroupDisabled(character: Character | int) -> bool:
    ...


def ObjectDestructionState(state: bool | int, obj: Object | int) -> bool:
    ...


def ObjectDestroyed(obj: Object | int) -> bool:
    ...


def ObjectNotDestroyed(obj: Object | int) -> bool:
    ...


def ObjectDamaged(obj: Object | int, attacker: Character | int) -> bool:
    ...


def ObjectActivated(obj_act_id: int) -> bool:
    ...


def ObjectHealthValueComparison(obj: Object | int, comparison_type: ComparisonType | int, value: int) -> bool:
    ...


def PlayerMovingOnCollision(collision: Collision | int) -> bool:
    ...


def PlayerRunningOnCollision(collision: Collision | int) -> bool:
    ...


def PlayerStandingOnCollision(collision: Collision | int) -> bool:
    ...


def ActionButton(
    prompt_text: EventText | int,
    anchor_entity: Object | Character | Region | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    max_distance: float = None,
    dummy_id: int = -1,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    boss_version: bool = False,
    line_intersects: Object | Character | Region | int = None,
) -> bool:
    """
    Calls `compiler.IfActionButton`.
    """
    ...


def PlayerHasWeapon(weapon: WeaponParam | int, including_storage: bool = False) -> bool:
    """
    Calls `compiler.IfPlayerHasWeapon`.
    """
    ...


def PlayerHasArmor(armor: ArmorParam | int, including_storage: bool = False) -> bool:
    """
    Calls `compiler.IfPlayerHasArmor`.
    """
    ...


def PlayerHasRune(rune: AccessoryParam | int, including_storage: bool = False) -> bool:
    """
    Calls `compiler.IfPlayerHasRune`.
    """
    ...


def PlayerHasGood(good: GoodParam | int, including_storage: bool = False) -> bool:
    """
    Calls `compiler.IfPlayerHasGood`.
    """
    ...


def PlayerDoesNotHaveWeapon(weapon: WeaponParam | int, including_storage: bool = False) -> bool:
    """
    Calls `compiler.IfPlayerDoesNotHaveWeapon`.
    """
    ...


def PlayerDoesNotHaveArmor(armor: ArmorParam | int, including_storage: bool = False) -> bool:
    """
    Calls `compiler.IfPlayerDoesNotHaveArmor`.
    """
    ...


def PlayerDoesNotHaveRune(ring: AccessoryParam | int, including_storage: bool = False) -> bool:
    """
    Calls `compiler.IfPlayerDoesNotHaveRune`.
    """
    ...


def PlayerDoesNotHaveGood(good: GoodParam | int, including_storage: bool = False) -> bool:
    """
    Calls `compiler.IfPlayerDoesNotHaveGood`.
    """
    ...


def EnabledFlagCount(flag_type: FlagType | int, flag_range: FlagRange | tuple | list) -> int:
    """
    Compare output to a value as a shortcut for calling `EnabledFlagCountComparison(...)`.
    """
    ...


def WorldTendency(world_tendency_type: WorldTendencyType | int) -> int:
    """
    Compare output to a value as a shortcut for calling `WorldTendencyComparison(...)`.
    """
    ...


def EventValue(flag: Flag | int, bit_count: int) -> int:
    """
    Compare output to a value as a shortcut for calling `EventValueComparison(...)`.
    """
    ...


def PlayerInsightAmount() -> int:
    """
    Compare output to a value as a shortcut for calling `PlayerInsightAmountComparison(...)`.
    """
    ...


def ClientTypeCount(client_type: ClientType | int) -> int:
    """
    Compare output to a value as a shortcut for calling `ClientTypeCountComparison(...)`.
    """
    ...


def HealthRatio(character: Character | int) -> float:
    """
    Compare output to a value as a shortcut for calling `HealthRatioComparison(...)`.
    """
    ...


def CharacterPartHealth(character: Character | int, npc_part_id: int) -> float:
    """
    Compare output to a value as a shortcut for calling `CharacterPartHealthComparison(...)`.
    """
    ...


def PlayerLevel() -> int:
    """
    Compare output to a value as a shortcut for calling `PlayerLevelComparison(...)`.
    """
    ...


def HealthValue(character: Character | int) -> int:
    """
    Compare output to a value as a shortcut for calling `HealthValueComparison(...)`.
    """
    ...


def ObjectHealthValue(obj: Object | int) -> int:
    """
    Compare output to a value as a shortcut for calling `ObjectHealthValueComparison(...)`.
    """
    ...
