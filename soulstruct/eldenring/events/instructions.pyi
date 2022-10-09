"""AUTOMATICALLY GENERATED. Do not edit this module.

Import this into any EVS script to have full access to instructions.
Make sure you also do `from soulstruct.{game}.events import *` to get all enums, constants, and tests.
"""

__all__ = [
    # Basics:
    "ContinueOnRest",
    "RestartOnRest",
    "EndOnRest",
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
    "IfTimeOfDay",  # 1[4]
    "IfTimeOfDayInRange",  # 1[5]
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
    "IfMultiplayerPending",
    "IfSingleplayer",
    "IfInvasion",
    "IfInvasionPending",
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
    "IfHealthRatioComparison",  # 4[2]
    "IfHealthRatioEqual",
    "IfHealthRatioNotEqual",
    "IfHealthRatioGreaterThan",
    "IfHealthRatioLessThan",
    "IfHealthRatioGreaterThanOrEqual",
    "IfHealthRatioLessThanOrEqual",
    "IfCharacterType",  # 4[3]
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
    "IfAssetDestructionState",  # 5[0]
    "IfAssetDestroyed",
    "IfAssetNotDestroyed",
    "IfAssetDamaged",  # 5[1]
    "IfAssetActivated",  # 5[2]
    "IfAssetHealthValueComparison",  # 5[3]
    "IfAssetHealthValueEqual",
    "IfAssetHealthValueNotEqual",
    "IfAssetHealthValueGreaterThan",
    "IfAssetHealthValueLessThan",
    "IfAssetHealthValueGreaterThanOrEqual",
    "IfAssetHealthValueLessThanOrEqual",
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
    "SkipLinesIfAssetDestructionState",  # 1005[1]
    "SkipLinesIfAssetDestroyed",
    "SkipLinesIfAssetNotDestroyed",
    "ReturnIfAssetDestructionState",  # 1005[2]
    "EndIfAssetDestroyed",
    "EndIfAssetNotDestroyed",
    "RestartIfAssetDestroyed",
    "RestartIfAssetNotDestroyed",
    "TerminateEvent",  # 2000[1]
    "SetNetworkSyncState",  # 2000[2]
    "EnableNetworkSync",
    "DisableNetworkSync",
    "ClearMainCondition",  # 2000[3]
    "IssuePrefetchRequest",  # 2000[4]
    "SaveRequest",  # 2000[5]
    "StartPS5Activity",  # 2000[7]
    "EndPS5Activity",  # 2000[8]
    "PlayCutsceneToAll",  # 2002[1]
    "PlayCutsceneToPlayer",  # 2002[3]
    "SetSpawnerState",  # 2003[3]
    "EnableSpawner",
    "DisableSpawner",
    "AwardItemLotToAllPlayers",  # 2003[4]
    "ShootProjectile",  # 2003[5]
    "SetBossHealthBarState",  # 2003[11]
    "EnableBossHealthBar",
    "DisableBossHealthBar",
    "KillBossAndDisplayBanner",  # 2003[12]
    "SetNavmeshType",  # 2003[13]
    "EnableNavmeshType",
    "DisableNavmeshType",
    "ToggleNavmeshType",
    "WarpToMap",  # 2003[14]
    "TriggerMultiplayerEvent",  # 2003[16]
    "SetRandomFlagInRange",  # 2003[17]
    "EnableRandomFlagInRange",
    "DisableRandomFlagInRange",
    "ToggleRandomFlagInRange",
    "ForceAnimation",  # 2003[18]
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
    "AwardAchievement",  # 2003[28]
    "IncrementEventValue",  # 2003[31]
    "ClearEventValue",  # 2003[32]
    "MoveRemains",  # 2003[35]
    "AwardItemLotToHostOnly",  # 2003[36]
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
    "DropMandatoryTreasure",  # 2004[37]
    "SetAnimationsState",  # 2004[39]
    "EnableAnimations",
    "DisableAnimations",
    "MoveAndSetDrawParent",  # 2004[40]
    "ShortMove",  # 2004[41]
    "MoveAndCopyDrawParent",  # 2004[42]
    "ResetAnimation",  # 2004[43]
    "SetTeamTypeAndExitStandbyAnimation",  # 2004[44]
    "EqualRecovery",  # 2004[47]
    "DestroyAsset",  # 2005[1]
    "RestoreAsset",  # 2005[2]
    "SetAssetState",  # 2005[3]
    "EnableAsset",
    "DisableAsset",
    "SetTreasureState",  # 2005[4]
    "EnableTreasure",
    "DisableTreasure",
    "ActivateAsset",  # 2005[5]
    "SetAssetActivation",  # 2005[6]
    "EndOfAnimation",  # 2005[7]
    "PostDestruction",  # 2005[8]
    "CreateHazard",  # 2005[9]
    "MoveAssetToCharacter",  # 2005[11]
    "RemoveAssetFlag",  # 2005[12]
    "SetAssetInvulnerabilityState",  # 2005[13]
    "EnableAssetInvulnerability",
    "DisableAssetInvulnerability",
    "SetAssetActivationWithIdx",  # 2005[14]
    "EnableTreasureCollection",  # 2005[15]
    "DeleteVFX",  # 2006[1]
    "CreateVFX",  # 2006[2]
    "CreateTemporaryVFX",  # 2006[3]
    "CreateAssetVFX",  # 2006[4]
    "DeleteAssetVFX",  # 2006[5]
    "DisplayDialog",  # 2007[1]
    "DisplayBanner",  # 2007[2]
    "DisplayStatus",  # 2007[3]
    "DisplayFlashingMessage",  # 2007[4]
    "DisplayFullScreenMessage",  # 2007[9]
    "ChangeCamera",  # 2008[1]
    "SetCameraVibration",  # 2008[2]
    "SetLockedCameraSlot",  # 2008[3]
    "RegisterLadder",  # 2009[0]
    "RegisterGrace",  # 2009[3]
    "ActivateMultiplayerBuffs",  # 2009[4]
    "NotifyBossBattleStart",  # 2009[6]
    "PlaySoundEffect",  # 2010[2]
    "SetMapCollisionState",  # 2011[1]
    "EnableMapCollision",
    "DisableMapCollision",
    "SetMapCollisionBackreadMaskState",  # 2011[2]
    "EnableMapCollisionBackreadMask",
    "DisableMapCollisionBackreadMask",
    "SetMapPieceState",  # 2012[1]
    "EnableMapPiece",
    "DisableMapPiece",
    "IfUnsignedComparison",  # 0[2]
    "IfUnsignedEqual",
    "IfUnsignedNotEqual",
    "IfUnsignedGreaterThan",
    "IfUnsignedLessThan",
    "IfUnsignedGreaterThanOrEqual",
    "IfUnsignedLessThanOrEqual",
    "IfAttackedWithDamageType",  # 3[23]
    "IfActionButtonParamActivated",  # 3[24]
    "IfPlayerOwnWorldState",  # 3[26]
    "IfPlayerInOwnWorld",
    "IfPlayerNotInOwnWorld",
    "IfMapLoaded",  # 3[30]
    "IfWeatherState",  # 3[31]
    "IfMapUpdatePermissionState",  # 3[32]
    "IfMapHasUpdatePermission",
    "IfMapDoesNotHaveUpdatePermission",
    "IfFieldBattleMusicState",  # 3[33]
    "IfFieldBattleMusicEnabled",
    "IfFieldBattleMusicDisabled",
    "IfPlayerHasArmorEquipped",  # 3[34]
    "IfPlayerHasHeadArmorEquipped",
    "IfPlayerHasBodyArmorEquipped",
    "IfPlayerHasArmsArmorEquipped",
    "IfPlayerHasLegsArmorEquipped",
    "IfCeremonyState",  # 3[35]
    "IfCeremonyActive",
    "IfCeremonyInactive",
    "IfWeatherLotState",  # 3[37]
    "IfWeatherLotActive",
    "IfWeatherLotInactive",
    "IfPlayerGender",  # 3[38]
    "IfAllyPhantomCountComparison",  # 3[39]
    "IfCharacterProportionDeathState",  # 4[15]
    "IfCharacterProportionDead",
    "IfCharacterProportionAlive",
    "IfCharacterProportionSpecialEffectState",  # 4[19]
    "IfCharacterProportionHasSpecialEffect",
    "IfCharacterProportionDoesNotHaveSpecialEffect",
    "IfPlayerTargeted",  # 4[28]
    "IfNPCPartAttackedWithDamageType",  # 4[30]
    "IfCharacterInvadeType",  # 4[31]
    "IfCharacterMountState",  # 4[32]
    "IfCharacterMounted",
    "IfCharacterNotMounted",
    "IfCharacterStateInfoState",  # 4[34]
    "IfCharacterHasStateInfo",
    "IfCharacterDoesNotHaveStateInfo",
    "IfSpecialStandbyEndedFlagState",  # 4[35]
    "IfSpecialStandbyEndedFlagEnabled",
    "IfSpecialStandbyEndedFlagDisabled",
    "IfAssetProportionDestructionState",  # 5[6]
    "IfAssetBackreadState",  # 5[10]
    "IfAssetBackreadEnabled",
    "IfAssetBackreadDisabled",
    "SkipLinesIfUnsignedComparison",  # 1000[10]
    "SkipLinesIfUnsignedEqual",
    "SkipLinesIfUnsignedNotEqual",
    "SkipLinesIfUnsignedGreaterThan",
    "SkipLinesIfUnsignedLessThan",
    "SkipLinesIfUnsignedGreaterThanOrEqual",
    "SkipLinesIfUnsignedLessThanOrEqual",
    "ReturnIfUnsignedComparison",  # 1000[11]
    "EndIfUnsignedEqual",
    "EndIfUnsignedNotEqual",
    "EndIfUnsignedGreaterThan",
    "EndIfUnsignedLessThan",
    "EndIfUnsignedGreaterThanOrEqual",
    "EndIfUnsignedLessThanOrEqual",
    "RestartIfUnsignedEqual",
    "RestartIfUnsignedNotEqual",
    "RestartIfUnsignedGreaterThan",
    "RestartIfUnsignedLessThan",
    "RestartIfUnsignedGreaterThanOrEqual",
    "RestartIfUnsignedLessThanOrEqual",
    "GotoIfConditionState",  # 1000[101]
    "GotoIfConditionTrue",
    "GotoIfConditionFalse",
    "Goto",  # 1000[103]
    "GotoIfValueComparison",  # 1000[105]
    "GotoIfFinishedConditionState",  # 1000[107]
    "GotoIfFinishedConditionTrue",
    "GotoIfFinishedConditionFalse",
    "GotoIfUnsignedComparison",  # 1000[108]
    "GotoIfUnsignedEqual",
    "GotoIfUnsignedNotEqual",
    "GotoIfUnsignedGreaterThan",
    "GotoIfUnsignedLessThan",
    "GotoIfUnsignedGreaterThanOrEqual",
    "GotoIfUnsignedLessThanOrEqual",
    "WaitUntilRandomTimeOfDay",  # 1001[5]
    "WaitFramesAfterCutscene",  # 1001[6]
    "SkipLinesIfMultiplayerState",  # 1003[5]
    "SkipLinesIfHost",
    "SkipLinesIfClient",
    "SkipLinesIfMultiplayer",
    "SkipLinesIfMultiplayerPending",
    "SkipLinesIfSingleplayer",
    "SkipLinesIfInvasion",
    "SkipLinesIfInvasionPending",
    "ReturnIfMultiplayerState",  # 1003[6]
    "EndIfHost",
    "EndIfClient",
    "EndIfMultiplayer",
    "EndIfMultiplayerPending",
    "EndIfSingleplayer",
    "EndIfInvasion",
    "EndIfInvasionPending",
    "RestartIfHost",
    "RestartIfClient",
    "RestartIfMultiplayer",
    "RestartIfMultiplayerPending",
    "RestartIfSingleplayer",
    "RestartIfInvasion",
    "RestartIfInvasionPending",
    "SkipLinesIfCoopClientCountComparison",  # 1003[9]
    "ReturnIfCoopClientCountComparison",  # 1003[10]
    "EndIfCoopClientCountComparison",
    "RestartIfCoopClientCountComparison",
    "SkipLinesIfPlayerOwnWorldState",  # 1003[12]
    "SkipLinesIfPlayerInOwnWorld",
    "SkipLinesIfPlayerNotInOwnWorld",
    "GotoIfPlayerOwnWorldState",  # 1003[13]
    "GotoIfPlayerInOwnWorld",
    "GotoIfPlayerNotInOwnWorld",
    "ReturnIfPlayerOwnWorldState",  # 1003[14]
    "EndIfPlayerInOwnWorld",
    "EndIfPlayerNotInOwnWorld",
    "RestartIfPlayerInOwnWorld",
    "RestartIfPlayerNotInOwnWorld",
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
    "GotoIfMultiplayerPending",
    "GotoIfSingleplayer",
    "GotoIfInvasion",
    "GotoIfInvasionPending",
    "GotoIfMapPresenceState",  # 1003[107]
    "GotoIfInsideMap",
    "GotoIfOutsideMap",
    "GotoIfCoopClientCountComparison",  # 1003[109]
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
    "SkipLinesIfMapUpdatePermissionState",  # 1003[203]
    "SkipLinesIfMapHasUpdatePermission",
    "SkipLinesIfMapDoesNotHaveUpdatePermission",
    "GotoIfMapUpdatePermissionState",  # 1003[204]
    "GotoIfMapHasUpdatePermission",
    "GotoIfMapDoesNotHaveUpdatePermission",
    "ReturnIfMapUpdatePermissionState",  # 1003[205]
    "EndIfMapHasUpdatePermission",
    "EndIfMapDoesNotHaveUpdatePermission",
    "RestartIfMapHasUpdatePermission",
    "RestartIfMapDoesNotHaveUpdatePermission",
    "SkipLinesIfCeremonyState",  # 1003[206]
    "SkipLinesIfCeremonyActive",
    "SkipLinesIfCeremonyInactive",
    "GotoIfCeremonyState",  # 1003[207]
    "GotoIfCeremonyActive",
    "GotoIfCeremonyInactive",
    "ReturnIfCeremonyState",  # 1003[208]
    "EndIfCeremonyActive",
    "EndIfCeremonyInactive",
    "RestartIfCeremonyActive",
    "RestartIfCeremonyInactive",
    "SkipLinesIfCharacterSpecialEffectState",  # 1004[0]
    "SkipLinesIfPlayerHasSpecialEffect",
    "SkipLinesIfPlayerDoesNotHaveSpecialEffect",
    "SkipLinesIfCharacterHasSpecialEffect",
    "SkipLinesIfCharacterDoesNotHaveSpecialEffect",
    "GotoIfCharacterSpecialEffectState",  # 1004[1]
    "GotoIfPlayerHasSpecialEffect",
    "GotoIfPlayerDoesNotHaveSpecialEffect",
    "GotoIfCharacterHasSpecialEffect",
    "GotoIfCharacterDoesNotHaveSpecialEffect",
    "ReturnIfCharacterSpecialEffectState",  # 1004[2]
    "EndIfPlayerHasSpecialEffect",
    "EndIfPlayerDoesNotHaveSpecialEffect",
    "RestartIfPlayerHasSpecialEffect",
    "RestartIfPlayerDoesNotHaveSpecialEffect",
    "EndIfCharacterHasSpecialEffect",
    "EndIfCharacterDoesNotHaveSpecialEffect",
    "RestartIfCharacterHasSpecialEffect",
    "RestartIfCharacterDoesNotHaveSpecialEffect",
    "SkipLinesIfSpecialStandbyEndedFlagState",  # 1004[3]
    "SkipLinesIfSpecialStandbyEndedFlagEnabled",
    "SkipLinesIfSpecialStandbyEndedFlagDisabled",
    "GotoIfSpecialStandbyEndedFlagState",  # 1004[4]
    "GotoIfSpecialStandbyEndedFlagEnabled",
    "GotoIfSpecialStandbyEndedFlagDisabled",
    "ReturnIfSpecialStandbyEndedFlagState",  # 1004[5]
    "EndIffSpecialStandbyEndedFlagEnabled",
    "EndIffSpecialStandbyEndedFlagDisabled",
    "RestartIffSpecialStandbyEndedFlagEnabled",
    "RestartIffSpecialStandbyEndedFlagDisabled",
    "AwaitAssetDestrucionState",  # 1005[0]
    "AwaitAssetDestroyed",
    "AwaitAssetNotDestroyed",
    "GotoIfAssetDestructionState",  # 1005[101]
    "GotoIfAssetDestroyed",
    "GotoIfAssetNotDestroyed",
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
    "SetCurrentTime",  # 2001[4]
    "SetTimeFreezeState",  # 2001[5]
    "FreezeTime",
    "UnfreezeTime",
    "PlayCutsceneToPlayerWithWeatherAndTime",  # 2002[10]
    "PlayCutsceneToPlayerAndWarp",  # 2002[11]
    "PlayCutsceneToPlayerAndWarpWithWeatherAndTime",  # 2002[12]
    "PlayCutsceneToPlayerAndWarpWithStablePositionUpdate",  # 2002[13]
    "StoreItemAmountSpecifiedByFlagValue",  # 2003[42]
    "GivePlayerItemAmountSpecifiedByFlagValue",  # 2003[43]
    "WarpPlayerToRespawnPoint",  # 2003[49]
    "StartEnemySpawner",  # 2003[50]
    "SummonNPC",  # 2003[51]
    "TriggerAISound",  # 2003[52]
    "ForceSpawnerToSpawn",  # 2003[54]
    "SetNetworkConnectedFlagRangeState",  # 2003[63]
    "EnableNetworkConnectedFlagRange",
    "DisableNetworkConnectedFlagRange",
    "ToggleNetworkConnectedFlagRange",
    "SetFlagState",  # 2003[66]
    "EnableFlag",
    "DisableFlag",
    "ToggleFlag",
    "SetAbsoluteFlagState",
    "EnableThisSlotFlag",
    "DisableThisSlotFlag",
    "SetWeather",  # 2003[68]
    "SetNetworkFlagState",  # 2003[69]
    "EnableNetworkFlag",
    "DisableNetworkFlag",
    "ToggleNetworkFlag",
    "SetAbsoluteNetworkFlagState",
    "EnableThisNetworkFlag",
    "DisableThisNetworkFlag",
    "EnableThisNetworkSlotFlag",
    "DisableThisNetworSlotFlag",
    "SetNetworkInteractionState",  # 2003[70]
    "AwardGesture",  # 2003[71]
    "MultiplyBloodstainSouls",  # 2003[72]
    "IncreaseCharacterSoulReward",  # 2003[73]
    "IssueEndOfPseudoMultiplayerNotification",  # 2003[74]
    "UseFarViewCamera",  # 2003[75]
    "SetPlayerPositionDisplay",  # 2003[76]
    "SetPseudoMultiplayerReturnPosition",  # 2003[77]
    "OpenWorldMapPoint",  # 2003[78]
    "SendNPCSummonHome",  # 2003[79]
    "ShowLoadingScreenText",  # 2003[80]
    "EnableLoadingScreenText",
    "DisableLoadingScreenText",
    "RemoveGesture",  # 2003[81]
    "EraseNPCSummonSign",  # 2003[82]
    "ChangeCharacterCloth",  # 2004[48]
    "ChangePatrolBehavior",  # 2004[49]
    "SetLockOnPoint",  # 2004[50]
    "SetCharacterTalkRange",  # 2004[55]
    "ConnectCharacterToCaravan",  # 2004[60]
    "Unknown_2004_61",  # 2004[61]
    "SetCharacterEnableDistance",  # 2004[63]
    "CopyPlayerCharacterData",  # 2004[67]
    "AttachAssetToCharacter",  # 2004[68]
    "SetCharacterDisableOnCollisionUnload",  # 2004[69]
    "SetDistanceBasedNetworkAuthorityUpdate",  # 2004[70]
    "Unknown_2004_71",  # 2004[71]
    "SetCharacterFadeOnEnable",  # 2004[73]
    "MoveCharacterAndCopyDrawParentWithFadeout",  # 2004[74]
    "SetCharacterFaceParamOverride",  # 2004[75]
    "Unknown_2004_76",  # 2004[76]
    "FadeToBlack",  # 2004[77]
    "CopyPlayerCharacterDataFromOnlinePlayers",  # 2004[78]
    "RequestPlayerCharacterDataFromOnlinePlayers",  # 2004[79]
    "SendPlayerCharacterDataToOnlinePlayers",  # 2004[80]
    "ResetCharacterPosition",  # 2004[81]
    "SetSpecialStandbyEndedFlag",  # 2004[83]
    "SetCharacterEnableDistanceWithUnknown",  # 2004[84]
    "AttachCaravanToController",  # 2005[17]
    "AttachAssetToAsset",  # 2005[18]
    "DestroyAsset_NoSlot",  # 2005[19]
    "CreateBigHazardousAsset",  # 2005[20]
    "SetWindVFX",  # 2006[6]
    "DisplayDialogAndSetFlags",  # 2007[10]
    "DisplayFlashingMessageWithPriority",  # 2007[12]
    "DisplaySubareaWelcomeMessage",  # 2007[13]
    "DisplayAreaWelcomeMessage",  # 2007[14]
    "DisplayTutorialMessage",  # 2007[15]
    "DisplayNetworkMessage",  # 2007[16]
    "SetCameraAngle",  # 2008[4]
    "BanishInvaders",  # 2009[8]
    "BanishPhantoms",  # 2009[11]
    "SuppressSoundEvent",  # 2010[7]
    "UnknownSound_2010_8",  # 2010[8]
    "SetBossMusic",  # 2010[10]
    "SuppressSoundForFogGate",  # 2010[11]
    "SetFieldBattleMusicHeatUp",  # 2010[12]
    "EnableFieldBattleMusicHeatUp",
    "DisableFieldBattleMusicHeatUp",
    "SetAreaWelcomeMessageState",  # 2012[8]
    "ActivateGparamOverride",  # 2012[11]
    "DeactivateGparamOverride",  # 2012[12]
    "EnableThisFlag",
    "DisableThisFlag",
    # Custom instructions from `compiler`:
    "compile_game_object_test",
    "RunEvent",
    "RunCommonEvent",
    "EnableAssetActivation",
    "DisableAssetActivation",
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
    "TimeOfDay",
    "TimeOfDayInRange",
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
    "MultiplayerPending",
    "Singleplayer",
    "Invasion",
    "InvasionPending",
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
    "HealthRatioComparison",
    "HealthRatioEqual",
    "HealthRatioNotEqual",
    "HealthRatioGreaterThan",
    "HealthRatioLessThan",
    "HealthRatioGreaterThanOrEqual",
    "HealthRatioLessThanOrEqual",
    "CharacterType",
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
    "AssetDestructionState",
    "AssetDestroyed",
    "AssetNotDestroyed",
    "AssetDamaged",
    "AssetActivated",
    "AssetHealthValueComparison",
    "AssetHealthValueEqual",
    "AssetHealthValueNotEqual",
    "AssetHealthValueGreaterThan",
    "AssetHealthValueLessThan",
    "AssetHealthValueGreaterThanOrEqual",
    "AssetHealthValueLessThanOrEqual",
    "PlayerMovingOnCollision",
    "PlayerRunningOnCollision",
    "PlayerStandingOnCollision",
    "UnsignedComparison",
    "UnsignedEqual",
    "UnsignedNotEqual",
    "UnsignedGreaterThan",
    "UnsignedLessThan",
    "UnsignedGreaterThanOrEqual",
    "UnsignedLessThanOrEqual",
    "AttackedWithDamageType",
    "ActionButtonParamActivated",
    "PlayerOwnWorldState",
    "PlayerInOwnWorld",
    "PlayerNotInOwnWorld",
    "MapLoaded",
    "WeatherState",
    "MapUpdatePermissionState",
    "MapHasUpdatePermission",
    "MapDoesNotHaveUpdatePermission",
    "FieldBattleMusicState",
    "FieldBattleMusicEnabled",
    "FieldBattleMusicDisabled",
    "PlayerHasArmorEquipped",
    "PlayerHasHeadArmorEquipped",
    "PlayerHasBodyArmorEquipped",
    "PlayerHasArmsArmorEquipped",
    "PlayerHasLegsArmorEquipped",
    "CeremonyState",
    "CeremonyActive",
    "CeremonyInactive",
    "WeatherLotState",
    "WeatherLotActive",
    "WeatherLotInactive",
    "PlayerGender",
    "AllyPhantomCountComparison",
    "CharacterProportionDeathState",
    "CharacterProportionDead",
    "CharacterProportionAlive",
    "CharacterProportionSpecialEffectState",
    "CharacterProportionHasSpecialEffect",
    "CharacterProportionDoesNotHaveSpecialEffect",
    "PlayerTargeted",
    "NPCPartAttackedWithDamageType",
    "CharacterInvadeType",
    "CharacterMountState",
    "CharacterMounted",
    "CharacterNotMounted",
    "CharacterStateInfoState",
    "CharacterHasStateInfo",
    "CharacterDoesNotHaveStateInfo",
    "SpecialStandbyEndedFlagState",
    "SpecialStandbyEndedFlagEnabled",
    "SpecialStandbyEndedFlagDisabled",
    "AssetProportionDestructionState",
    "AssetBackreadState",
    "AssetBackreadEnabled",
    "AssetBackreadDisabled",
    "ActionButton",
    "PlayerHasWeapon",
    "PlayerHasArmor",
    "PlayerHasRing",
    "PlayerHasGood",
    "PlayerDoesNotHaveWeapon",
    "PlayerDoesNotHaveArmor",
    "PlayerDoesNotHaveRing",
    "PlayerDoesNotHaveGood",
    "EnabledFlagCount",
    "EventValue",
    "HealthRatio",
    "CharacterPartHealth",
    "PlayerLevel",
    "HealthValue",
    "AssetHealthValue",
    "AllyPhantomCount",
]

import typing as tp

from soulstruct.eldenring.game_types import *
from .emevd.compiler import *
from .emevd.enums import *

# Restart decorators. They can be used as names (not function calls) or have an event ID argument.
def ContinueOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...
def RestartOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...
def EndOnRest(event_id_or_func: tp.Union[tp.Callable, int]): ...

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


def IfTimeOfDay(condition: ConditionGroup | int, time: tuple, event_layers=()):
    """
    Checks if current in-game time is EXACTLY the given time, down to the second.
    """


def IfTimeOfDayInRange(condition: ConditionGroup | int, earliest: tuple, latest: tuple, event_layers=()):
    """
    Checks if current in-game time is between an earliest and latest time, each specified down to the second.
    
    Note that ranges will loop over midnight as expected, so checking, e.g., if the time is within the three-
    hour range between hour 23 (PM) and hour 2 (AM) is straightforward: `earliest=(23, 0, 0), latest=(2, 0, 0)`.
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
    entity: Asset | Region | Character | int,
    other_entity: Asset | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Same new argument as region test, with unknown purpose, and again always 1 in EMEVD resources.
    """


def IfPlayerWithinDistance(
    condition: ConditionGroup | int,
    other_entity: Asset | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=True`, `entity=10000`.
    """


def IfPlayerBeyondDistance(
    condition: ConditionGroup | int,
    other_entity: Asset | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=False`, `entity=10000`.
    """


def IfEntityWithinDistance(
    condition: ConditionGroup | int,
    entity: Asset | Region | Character | int,
    other_entity: Asset | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=True`.
    """


def IfEntityBeyondDistance(
    condition: ConditionGroup | int,
    entity: Asset | Region | Character | int,
    other_entity: Asset | Region | Character | int,
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
    anchor_entity: Asset | Region | Character | int,
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


def IfMultiplayer(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=2`.
    """


def IfMultiplayerPending(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=3`.
    """


def IfSingleplayer(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=4`.
    """


def IfInvasion(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=5`.
    """


def IfInvasionPending(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=6`.
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
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Conditions upon player's presence in a particular game map.
    """


def IfInsideMap(condition: ConditionGroup | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `IfMapPresenceState` with `state=True`.
    """


def IfOutsideMap(condition: ConditionGroup | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `IfMapPresenceState` with `state=False`.
    """


def IfMultiplayerEvent(condition: ConditionGroup | int, event_id: int, event_layers=()):
    """
    TODO
    """


def IfEnabledFlagCountComparison(
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


def IfEnabledFlagCountEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=0`.
    """


def IfEnabledFlagCountNotEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=1`.
    """


def IfEnabledFlagCountGreaterThan(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=2`.
    """


def IfEnabledFlagCountLessThan(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=3`.
    """


def IfEnabledFlagCountGreaterThanOrEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=4`.
    """


def IfEnabledFlagCountLessThanOrEqual(
    condition: ConditionGroup | int,
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=5`.
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
    anchor_entity: Asset | Region | Character | int,
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
    anchor_entity: Asset | Region | Character | int,
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
    anchor_entity: Asset | Region | Character | int,
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


def IfHealthRatioComparison(
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


def IfHealthRatioEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=0`.
    """


def IfHealthRatioNotEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=1`.
    """


def IfHealthRatioGreaterThan(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=2`.
    """


def IfHealthRatioLessThan(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=3`.
    """


def IfHealthRatioGreaterThanOrEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=4`.
    """


def IfHealthRatioLessThanOrEqual(
    condition: ConditionGroup | int,
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfHealthRatioComparison` with `comparison_type=5`.
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


def IfCharacterTargetingState(
    condition: ConditionGroup | int,
    targeting_character: Character | int,
    targeted_character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterTargeting(
    condition: ConditionGroup | int,
    targeting_character: Character | int,
    targeted_character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterTargetingState` with `state=True`.
    """


def IfCharacterNotTargeting(
    condition: ConditionGroup | int,
    targeting_character: Character | int,
    targeted_character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
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


def IfPlayerClass(condition: ConditionGroup | int, class_type: ClassType | int, event_layers=()):
    """
    TODO
    """


def IfPlayerCovenant(condition: ConditionGroup | int, covenant: int, event_layers=()):
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


def IfAssetDestructionState(
    condition: ConditionGroup | int,
    state: bool | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfAssetDestroyed(
    condition: ConditionGroup | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetDestructionState` with `state=True`.
    """


def IfAssetNotDestroyed(
    condition: ConditionGroup | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetDestructionState` with `state=False`.
    """


def IfAssetDamaged(condition: ConditionGroup | int, asset: Asset | int, attacker: Character | int, event_layers=()):
    """
    TODO
    """


def IfAssetActivated(condition: ConditionGroup | int, obj_act_id: int, event_layers=()):
    """
    TODO
    """


def IfAssetHealthValueComparison(
    condition: ConditionGroup | int,
    asset: Asset | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    TODO
    """


def IfAssetHealthValueEqual(condition: ConditionGroup | int, asset: Asset | int, value: int, event_layers=()):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=0`.
    """


def IfAssetHealthValueNotEqual(condition: ConditionGroup | int, asset: Asset | int, value: int, event_layers=()):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=1`.
    """


def IfAssetHealthValueGreaterThan(condition: ConditionGroup | int, asset: Asset | int, value: int, event_layers=()):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=2`.
    """


def IfAssetHealthValueLessThan(condition: ConditionGroup | int, asset: Asset | int, value: int, event_layers=()):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=3`.
    """


def IfAssetHealthValueGreaterThanOrEqual(
    condition: ConditionGroup | int,
    asset: Asset | int,
    value: int,
    event_layers=(),
):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=4`.
    """


def IfAssetHealthValueLessThanOrEqual(condition: ConditionGroup | int, asset: Asset | int, value: int, event_layers=()):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=5`.
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


def SkipLinesIfMapPresenceState(
    line_count: int,
    state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfInsideMap(line_count: int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=True`.
    """


def SkipLinesIfOutsideMap(line_count: int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=False`.
    """


def ReturnIfMapPresenceState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def EndIfInsideMap(game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=True`.
    """


def EndIfOutsideMap(game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=False`.
    """


def RestartIfInsideMap(game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=True`.
    """


def RestartIfOutsideMap(game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=False`.
    """


def SkipLinesIfAssetDestructionState(
    line_count: int,
    state: bool | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfAssetDestroyed(
    line_count: int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `SkipLinesIfAssetDestructionState` with `state=True`.
    """


def SkipLinesIfAssetNotDestroyed(
    line_count: int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `SkipLinesIfAssetDestructionState` with `state=False`.
    """


def ReturnIfAssetDestructionState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def EndIfAssetDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfAssetDestructionState` with `event_return_type=0`, `state=True`.
    """


def EndIfAssetNotDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfAssetDestructionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfAssetDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfAssetDestructionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfAssetNotDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfAssetDestructionState` with `event_return_type=1`, `state=False`.
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


# Instruction `RunCommonEvent` is manually defined in the `compiler` module.


def StartPS5Activity(activity_id: int, event_layers=()):
    """
    TODO
    """


def EndPS5Activity(activity_id: int, event_layers=()):
    """
    TODO
    """


def PlayCutsceneToAll(cutscene_id: int, cutscene_flags: CutsceneFlags | int, event_layers=()):
    """
    TODO
    """


def PlayCutsceneToPlayer(cutscene_id: int, cutscene_flags: CutsceneFlags | int, player_id: int, event_layers=()):
    """
    TODO
    """


def SetSpawnerState(entity: Asset | Region | Character | int, state: bool | int, event_layers=()):
    """
    e.g. the baby skeletons in Tomb of the Giants.
    """


def EnableSpawner(entity: Asset | Region | Character | int, event_layers=()):
    """
    Calls `SetSpawnerState` with `state=True`.
    """


def DisableSpawner(entity: Asset | Region | Character | int, event_layers=()):
    """
    Calls `SetSpawnerState` with `state=False`.
    """


def AwardItemLotToAllPlayers(item_lot: int, event_layers=()):
    """
    TODO
    """


def ShootProjectile(
    owner_entity: Asset | Region | Character | int,
    source_entity: Asset | Region | Character | int,
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


def KillBossAndDisplayBanner(character: Character | int, banner_type: BannerType | int, event_layers=()):
    """
    TODO
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


def WarpToMap(
    game_map: Map | MapTile | tuple | list,
    player_start: PlayerStart | int = -1,
    unk_8_12: int = 0,
    event_layers=(),
):
    """
    Warp the main player to the given player entity ID, which is in the Players tab of the MSB, in some map. By
    default, this warps to the 'default position' in the map (-1), which is the same point you would spawn at if
    the game lost track of your stable footing (e.g. in 'wrong warp' glitches).
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
    entity: Character | Asset | int,
    animation_id: int,
    loop: bool | int = False,
    wait_for_completion: bool | int = False,
    skip_transition: bool | int = False,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Used a lot. Standard way to make a Character or Asset perform an animation.
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
    unknown: int,
    event_layers=(),
):
    """
    If you set a black summon sign, the specified NPC will try to invade automatically.
    
    New unknown argument in Elden Ring.
    """


def AwardAchievement(achievement_id: int, event_layers=()):
    """
    For obvious reasons, I *highly* discourage you from abusing this, except in the interest of maintaining the
    accessibility of existing achievements. This interacts with Steam, which is always dangerous.
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


def MoveRemains(source_region: Region | int, destination_region: Region | int, event_layers=()):
    """
    Move all bloodstains and dropped items from one region to another (I assume). Used to move your
    remains out of Gwyndolin's endless corridor.
    """


def AwardItemLotToHostOnly(item_lot: int, event_layers=()):
    """
    You can simply call AwardItemLot() with the same argument, which will redirect here, as you'll almost never
    *not* want to award an item lot to the host only.
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
    destination: Asset | Region | Character | int,
    model_point: int = -1,
    destination_type: CoordEntityType | int = None,
    event_layers=(),
):
    """
    Basic move. I recommend you use the combined `Move` function.
    destination_type: Auto-detected from `destination` type by default.
    """


def Kill(character: Character | int, award_runes: bool | int = False, event_layers=()):
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


def CreateProjectileOwner(entity: Asset | Region | Character | int, event_layers=()):
    """
    A 'bullet owner' that will spawn things according to the Spawner section of the MSB.
    """


def AddSpecialEffect(character: Character | int, special_effect: int, event_layers=()):
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


def SetCharacterEventTarget(character: Character | int, entity: Asset | Region | Character | int, event_layers=()):
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
    target_entity: Asset | Region | Character | int,
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


def RemoveSpecialEffect(character: Character | int, special_effect: int, event_layers=()):
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
    unk_16_20: int,
    unk_20_24: int,
    unk_24_28: int,
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


def SetCharacterCollisionState(character: Character | int, state: bool | int, event_layers=()):
    """
    Note that the bool is no longer inverted, as in older games.
    """


def EnableCharacterCollision(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterCollisionState` with `state=True`.
    """


def DisableCharacterCollision(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterCollisionState` with `state=False`.
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
    sure if the target entity can be an Asset.
    
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


def DropMandatoryTreasure(character: Character | int, event_layers=()):
    """
    This will disable the character and spawn any treasure they would drop. It's possible that it only spawns
    treasure that has a 100% drop rate, hence the name, but I haven't confirmed this.
    """


def SetAnimationsState(entity: Character | Asset | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableAnimations(entity: Character | Asset | int, event_layers=()):
    """
    Calls `SetAnimationsState` with `state=True`.
    """


def DisableAnimations(entity: Character | Asset | int, event_layers=()):
    """
    Calls `SetAnimationsState` with `state=False`.
    """


def MoveAndSetDrawParent(
    character: Character | int,
    destination: Asset | Region | Character | int,
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
    destination: Asset | Region | Character | int,
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
    destination: Asset | Region | Character | int,
    copy_draw_parent: Character | Asset | int,
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


def EqualRecovery(event_layers=()):
    """
    Unknown effect. Only used in Battle of Stoicism, so likely useless to you.
    """


def DestroyAsset(asset: Asset | int, request_slot: int = 1, event_layers=()):
    """
    Technically 'requests' the asset's destruction. No idea what the slot number does.
    """


def RestoreAsset(asset: Asset | int, event_layers=()):
    """
    The opposite of destruction. Restores it to its original MSB coordinates.
    """


def SetAssetState(asset: Asset | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableAsset(asset: Asset | int, event_layers=()):
    """
    Calls `SetAssetState` with `state=True`.
    """


def DisableAsset(asset: Asset | int, event_layers=()):
    """
    Calls `SetAssetState` with `state=False`.
    """


def SetTreasureState(asset: Asset | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableTreasure(asset: Asset | int, event_layers=()):
    """
    Calls `SetTreasureState` with `state=True`.
    Enables any treasure attached to this asset by MSB events.
    """


def DisableTreasure(asset: Asset | int, event_layers=()):
    """
    Calls `SetTreasureState` with `state=False`.
    
    Disables any treasure attached to this asset by MSB events.
    
    If you want to disable treasure by default, you can do it in the MSB by changing a certain event
    value to 255.
    """


def ActivateAsset(asset: Asset | int, obj_act_id: int, relative_index: int, event_layers=()):
    """
    Manually call a specific ObjAct event attached to this asset. I believe 'relative_index' refers to the
    points on the asset at which it can be activated (e.g. which side of a gate you are on).
    
    Note that this will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how
    the game gets Patches to pull the lever in the Catacombs.
    """


def SetAssetActivation(asset: Asset | int, obj_act_id: int, state: bool | int, event_layers=()):
    """
    Sets whether the asset can be activated (1) or not activated (0).
    """


def EndOfAnimation(asset: Asset | int, animation_id: int, event_layers=()):
    """
    Sets entity to whatever state it would have after the given animation. Used often to open doors that have
    already been opened when you reload the map, etc. I doubt it can be used with characters, but haven't
    confirmed.
    """


def PostDestruction(asset: Asset | int, request_slot: int = 1, event_layers=()):
    """
    Sets the asset to whatever appearance it would have after being destroyed. Again, not sure what 'slot'
    does, but it's literally *always* 1 in vanilla scripts (and from my testing, the instruction doesn't work
    with `slot=0`).
    """


def CreateHazard(
    asset_flag: Flag | int,
    asset: Asset | int,
    model_point: int,
    behavior_param_id: int,
    target_type: DamageTargetType | int,
    radius: float,
    life: float,
    repetition_time: float,
    event_layers=(),
):
    """
    Turn an asset into an environmental hazard. It deals damage when touched according to the NPC Behavior
    params you give it. The model_point determines which part of the asset is hazardous (with the given radius
    and life, relative to the time this instruction occurs).
    
    An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.
    
    'target_type' determines what the hazard can damage (Character and/or Map).
    """


def MoveAssetToCharacter(asset: Asset | int, character: Character | int, model_point: int = -1, event_layers=()):
    """
    Move an asset to a character.
    """


def RemoveAssetFlag(asset_flag: Flag | int, event_layers=()):
    """
    No idea what this does. I believe it might undo the CreateHazard instruction, at least.
    """


def SetAssetInvulnerabilityState(asset: Asset | int, state: bool | int, event_layers=()):
    """
    1 = invulnerable.
    """


def EnableAssetInvulnerability(asset: Asset | int, event_layers=()):
    """
    Calls `SetAssetInvulnerabilityState` with `state=True`.
    """


def DisableAssetInvulnerability(asset: Asset | int, event_layers=()):
    """
    Calls `SetAssetInvulnerabilityState` with `state=False`.
    """


def SetAssetActivationWithIdx(
    asset: Asset | int,
    obj_act_id: int,
    relative_index: int,
    state: bool | int,
    event_layers=(),
):
    """
    Similar to SetAssetActivation, but you can provide the relative index to disable (e.g. one side of a door).
    """


def EnableTreasureCollection(asset: Asset | int, event_layers=()):
    """
    Forces an asset to spawn its treasure, even if the treasure's ItemLot flag is already enabled.
    
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
    anchor_entity: Asset | Region | Character | int,
    model_point: int = -1,
    anchor_type: CoordEntityType | int = None,
    event_layers=(),
):
    """
    Create one-off visual VFX (an FFX ID) attached to the given 'anchor_entity'. The VFX, of course, must be
    currently loaded (or in common effects).
    
    anchor_type: Auto-detected from `anchor_entity` type by default. Sets `Character` type for `PLAYER`.
    """


def CreateAssetVFX(asset: Asset | int, vfx_id: int, model_point: int, event_layers=()):
    """
    TODO
    """


def DeleteAssetVFX(asset: Asset | int, erase_root: bool = True, event_layers=()):
    """
    Note `erase_root` vs. `erase_root_only` for map SFX.
    """


def DisplayDialog(
    text: EventText | int,
    anchor_entity: Asset | Region | Character | int = 4294967295,
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


def DisplayFlashingMessage(text: EventText | int, event_layers=()):
    """
    Displays a flashing messages at the bottom of the screen that does not block player input.
    """


def DisplayFullScreenMessage(text: EventText | int, event_layers=()):
    """
    TODO
    """


def ChangeCamera(normal_camera_id: int, locked_camera_id: int, event_layers=()):
    """
    TODO
    """


def SetCameraVibration(
    vibration_id: int,
    anchor_entity: Asset | Region | Character | int,
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


def SetLockedCameraSlot(area_id: int, block_id: int, camera_slot: int, event_layers=()):
    """
    Switch between one of two camera slots associated with the player's current collision in the MSB.
    
    Applies to area and block, not specific map CC/DD values.
    """


def RegisterLadder(
    start_climbing_flag: Flag | int,
    stop_climbing_flag: Flag | int,
    asset: Asset | int,
    event_layers=(),
):
    """
    Don't mess with these flags, generally; you can just delay when this is called after map load to disable
    certain ladders (which is kind of weird anyway).
    """


def RegisterGrace(
    grace_flag: Flag | int,
    asset: Asset | int,
    reaction_distance: float = 0.0,
    reaction_angle: float = 0.0,
    initial_kindle_level: int = 0,
    enemy_block_distance: float = 5.0,
    event_layers=(),
):
    """
    Register a Site of Grace, which creates the VFX and allows you to interact with it via the MSB character
    with ID `(asset + 1000)`.
    
    I believe the grace flag tells the game where to keep track of its kindle level, or something like that. I
    don't recommend messing around with this much. The reaction distance, angle, and initial kindle level are
    all set to their standard defaults.
    
    You can also use `enemy_block_distance` to set the minimum distance that enemies must be at to allow the
    Grace to be interacted with.
    """


def ActivateMultiplayerBuffs(character: Character | int, event_layers=()):
    """
    Used to strengthen bosses based on the number of summons you have. Not sure if it works for every NPC. It
    could also be tied to certain special effects; haven't checked that yet.
    """


def NotifyBossBattleStart(dummy: int = 0, event_layers=()):
    """
    Sends the message to all summons that the host has challenged the boss.
    """


def PlaySoundEffect(
    anchor_entity: Asset | Region | Character | int,
    sound_id: int,
    sound_type: SoundType | int = None,
    event_layers=(),
):
    """
    Anchor entity determines sound position and the sound type is used to look up the source.
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


def IfUnsignedComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
    event_layers=(),
):
    """
    TODO
    """


def IfUnsignedEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=0`.
    """


def IfUnsignedNotEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=1`.
    """


def IfUnsignedGreaterThan(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=2`.
    """


def IfUnsignedLessThan(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=3`.
    """


def IfUnsignedGreaterThanOrEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=4`.
    """


def IfUnsignedLessThanOrEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=5`.
    """


def IfAttackedWithDamageType(
    condition: ConditionGroup | int,
    attacked_entity: Character | int,
    attacker: Character | int = 0,
    damage_type: DamageType | int = DamageType.Unspecified,
    event_layers=(),
):
    """
    TODO
    """


def IfActionButtonParamActivated(
    condition: ConditionGroup | int,
    action_button_id: int,
    entity: Asset | Region | Character | int,
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


def IfMapLoaded(condition: ConditionGroup | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Only used in Radahn fight, I believe, with map tiles.
    """


def IfWeatherState(
    condition: ConditionGroup | int,
    weather: Weather | int,
    unk_4_8: float,
    unk_8_12: float,
    event_layers=(),
):
    """
    TODO
    """


def IfMapUpdatePermissionState(
    condition: ConditionGroup | int,
    state: bool | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def IfMapHasUpdatePermission(
    condition: ConditionGroup | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `IfMapUpdatePermissionState` with `state=True`.
    """


def IfMapDoesNotHaveUpdatePermission(
    condition: ConditionGroup | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `IfMapUpdatePermissionState` with `state=False`.
    """


def IfFieldBattleMusicState(condition: ConditionGroup | int, npc_threat_level: int, state: bool | int, event_layers=()):
    """
    TODO
    """


def IfFieldBattleMusicEnabled(condition: ConditionGroup | int, npc_threat_level: int, event_layers=()):
    """
    Calls `IfFieldBattleMusicState` with `state=True`.
    """


def IfFieldBattleMusicDisabled(condition: ConditionGroup | int, npc_threat_level: int, event_layers=()):
    """
    Calls `IfFieldBattleMusicState` with `state=False`.
    """


def IfPlayerHasArmorEquipped(
    condition: ConditionGroup | int,
    armor_type: ArmorType | int,
    armor: ArmorParam | int,
    unk_8_12: int = -1,
    event_layers=(),
):
    """
    TODO
    """


def IfPlayerHasHeadArmorEquipped(
    condition: ConditionGroup | int,
    armor: ArmorParam | int,
    unk_8_12: int = -1,
    event_layers=(),
):
    """
    Calls `IfPlayerHasArmorEquipped` with `armor_type=0`.
    """


def IfPlayerHasBodyArmorEquipped(
    condition: ConditionGroup | int,
    armor: ArmorParam | int,
    unk_8_12: int = -1,
    event_layers=(),
):
    """
    Calls `IfPlayerHasArmorEquipped` with `armor_type=1`.
    """


def IfPlayerHasArmsArmorEquipped(
    condition: ConditionGroup | int,
    armor: ArmorParam | int,
    unk_8_12: int = -1,
    event_layers=(),
):
    """
    Calls `IfPlayerHasArmorEquipped` with `armor_type=2`.
    """


def IfPlayerHasLegsArmorEquipped(
    condition: ConditionGroup | int,
    armor: ArmorParam | int,
    unk_8_12: int = -1,
    event_layers=(),
):
    """
    Calls `IfPlayerHasArmorEquipped` with `armor_type=3`.
    """


def IfCeremonyState(condition: ConditionGroup | int, state: bool | int, ceremony: int, event_layers=()):
    """
    TODO
    """


def IfCeremonyActive(condition: ConditionGroup | int, ceremony: int, event_layers=()):
    """
    Calls `IfCeremonyState` with `state=True`.
    """


def IfCeremonyInactive(condition: ConditionGroup | int, ceremony: int, event_layers=()):
    """
    Calls `IfCeremonyState` with `state=False`.
    """


def IfWeatherLotState(condition: ConditionGroup | int, weather_lot_param_id: int, state: bool | int, event_layers=()):
    """
    TODO
    """


def IfWeatherLotActive(condition: ConditionGroup | int, weather_lot_param_id: int, event_layers=()):
    """
    Calls `IfWeatherLotState` with `state=True`.
    """


def IfWeatherLotInactive(condition: ConditionGroup | int, weather_lot_param_id: int, event_layers=()):
    """
    Calls `IfWeatherLotState` with `state=False`.
    """


def IfPlayerGender(condition: ConditionGroup | int, gender: Gender | int, event_layers=()):
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


def IfCharacterProportionDeathState(
    condition: ConditionGroup | int,
    character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
):
    """
    Checks if a proportion (0-1) of given characters (group entity ID) are dead or alive.
    """


def IfCharacterProportionDead(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterProportionDeathState` with `state=True`.
    """


def IfCharacterProportionAlive(
    condition: ConditionGroup | int,
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterProportionDeathState` with `state=False`.
    """


def IfCharacterProportionSpecialEffectState(
    condition: ConditionGroup | int,
    character_group: Character | int,
    special_effect: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
):
    """
    Checks if a certain proportion of the given characters (group entity ID) have or do not have a given
    special effect, rather than a certain absolute count.
    """


def IfCharacterProportionHasSpecialEffect(
    condition: ConditionGroup | int,
    character_group: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterProportionSpecialEffectState` with `state=True`.
    """


def IfCharacterProportionDoesNotHaveSpecialEffect(
    condition: ConditionGroup | int,
    character_group: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterProportionSpecialEffectState` with `state=False`.
    """


def IfPlayerTargeted(
    condition: ConditionGroup | int,
    min_npc_threat_level: int,
    max_npc_threat_level: int,
    ai_status: AIStatusType | int,
    event_layers=(),
):
    """
    TODO
    """


def IfNPCPartAttackedWithDamageType(
    condition: ConditionGroup | int,
    character: Character | int,
    npc_part_id: int,
    attacker: Character | int = -1,
    damage_type: DamageType | int = DamageType.Unspecified,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterInvadeType(
    condition: ConditionGroup | int,
    character: Character | int,
    invade_type: CharacterType | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterMountState(
    condition: ConditionGroup | int,
    character: Character | int,
    is_mounted: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def IfCharacterMounted(condition: ConditionGroup | int, character: Character | int, event_layers=()):
    """
    Calls `IfCharacterMountState` with `is_mounted=True`.
    """


def IfCharacterNotMounted(condition: ConditionGroup | int, character: Character | int, event_layers=()):
    """
    Calls `IfCharacterMountState` with `is_mounted=False`.
    """


def IfCharacterStateInfoState(
    condition: ConditionGroup | int,
    character: Character | int,
    state_info: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Checks if character has or does not have the given `state_info` (from a SpEffect).
    """


def IfCharacterHasStateInfo(
    condition: ConditionGroup | int,
    character: Character | int,
    state_info: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterStateInfoState` with `state=True`.
    """


def IfCharacterDoesNotHaveStateInfo(
    condition: ConditionGroup | int,
    character: Character | int,
    state_info: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfCharacterStateInfoState` with `state=False`.
    """


def IfSpecialStandbyEndedFlagState(
    condition: ConditionGroup | int,
    character: Character | int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def IfSpecialStandbyEndedFlagEnabled(condition: ConditionGroup | int, character: Character | int, event_layers=()):
    """
    Calls `IfSpecialStandbyEndedFlagState` with `state=True`.
    """


def IfSpecialStandbyEndedFlagDisabled(condition: ConditionGroup | int, character: Character | int, event_layers=()):
    """
    Calls `IfSpecialStandbyEndedFlagState` with `state=False`.
    """


def IfAssetProportionDestructionState(
    condition: ConditionGroup | int,
    state: bool | int,
    asset_group: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
):
    """
    Check if a certain proportion of given assets (group entity ID) have or have not been destroyed.
    """


def IfAssetBackreadState(
    condition: ConditionGroup | int,
    asset: Asset | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def IfAssetBackreadEnabled(
    condition: ConditionGroup | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetBackreadState` with `state=True`.
    """


def IfAssetBackreadDisabled(
    condition: ConditionGroup | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetBackreadState` with `state=False`.
    """


def SkipLinesIfUnsignedComparison(
    line_count: int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfUnsignedEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=0`.
    """


def SkipLinesIfUnsignedNotEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=1`.
    """


def SkipLinesIfUnsignedGreaterThan(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=2`.
    """


def SkipLinesIfUnsignedLessThan(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=3`.
    """


def SkipLinesIfUnsignedGreaterThanOrEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=4`.
    """


def SkipLinesIfUnsignedLessThanOrEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=5`.
    """


def ReturnIfUnsignedComparison(
    event_return_type: EventReturnType | int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
    event_layers=(),
):
    """
    TODO
    """


def EndIfUnsignedEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=0`.
    """


def EndIfUnsignedNotEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=1`.
    """


def EndIfUnsignedGreaterThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=2`.
    """


def EndIfUnsignedLessThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=3`.
    """


def EndIfUnsignedGreaterThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=4`.
    """


def EndIfUnsignedLessThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=5`.
    """


def RestartIfUnsignedEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=0`.
    """


def RestartIfUnsignedNotEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=1`.
    """


def RestartIfUnsignedGreaterThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=2`.
    """


def RestartIfUnsignedLessThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=3`.
    """


def RestartIfUnsignedGreaterThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=4`.
    """


def RestartIfUnsignedLessThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=5`.
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


def GotoIfUnsignedComparison(
    label: Label | int,
    comparison_type: ComparisonType | int,
    left: int,
    right: int,
    event_layers=(),
):
    """
    TODO
    """


def GotoIfUnsignedEqual(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=0`.
    """


def GotoIfUnsignedNotEqual(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=1`.
    """


def GotoIfUnsignedGreaterThan(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=2`.
    """


def GotoIfUnsignedLessThan(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=3`.
    """


def GotoIfUnsignedGreaterThanOrEqual(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=4`.
    """


def GotoIfUnsignedLessThanOrEqual(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=5`.
    """


def WaitUntilRandomTimeOfDay(earliest: tuple, latest: tuple, event_layers=()):
    """
    Pause event script until a random time of day chosen between the given earliest/latest times.
    """


def WaitFramesAfterCutscene(frames: int, event_layers=()):
    """
    Always used after cutscene instructions with argument `frames=1`.
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


def SkipLinesIfMultiplayer(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=2`.
    """


def SkipLinesIfMultiplayerPending(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=3`.
    """


def SkipLinesIfSingleplayer(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=4`.
    """


def SkipLinesIfInvasion(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=5`.
    """


def SkipLinesIfInvasionPending(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=6`.
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


def EndIfMultiplayer(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=2`.
    """


def EndIfMultiplayerPending(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=3`.
    """


def EndIfSingleplayer(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=4`.
    """


def EndIfInvasion(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=5`.
    """


def EndIfInvasionPending(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=6`.
    """


def RestartIfHost(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=0`.
    """


def RestartIfClient(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=1`.
    """


def RestartIfMultiplayer(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=2`.
    """


def RestartIfMultiplayerPending(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=3`.
    """


def RestartIfSingleplayer(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=4`.
    """


def RestartIfInvasion(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=5`.
    """


def RestartIfInvasionPending(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=6`.
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


def SkipLinesIfPlayerOwnWorldState(line_count: int, not_in_own_world: bool | int, event_layers=()):
    """
    TODO
    """


def SkipLinesIfPlayerInOwnWorld(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfPlayerOwnWorldState` with `not_in_own_world=False`.
    """


def SkipLinesIfPlayerNotInOwnWorld(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfPlayerOwnWorldState` with `not_in_own_world=True`.
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


def GotoIfMultiplayer(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=2`.
    """


def GotoIfMultiplayerPending(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=3`.
    """


def GotoIfSingleplayer(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=4`.
    """


def GotoIfInvasion(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=5`.
    """


def GotoIfInvasionPending(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=6`.
    """


def GotoIfMapPresenceState(
    label: Label | int,
    state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def GotoIfInsideMap(label: Label | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `GotoIfMapPresenceState` with `state=True`.
    """


def GotoIfOutsideMap(label: Label | int, game_map: Map | MapTile | tuple | list, event_layers=()):
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


def SkipLinesIfMapUpdatePermissionState(
    line_count: int,
    state: bool | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfMapHasUpdatePermission(
    line_count: int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `SkipLinesIfMapUpdatePermissionState` with `state=True`.
    """


def SkipLinesIfMapDoesNotHaveUpdatePermission(
    line_count: int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `SkipLinesIfMapUpdatePermissionState` with `state=False`.
    """


def GotoIfMapUpdatePermissionState(
    label: Label | int,
    state: bool | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def GotoIfMapHasUpdatePermission(
    label: Label | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `GotoIfMapUpdatePermissionState` with `state=True`.
    """


def GotoIfMapDoesNotHaveUpdatePermission(
    label: Label | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `GotoIfMapUpdatePermissionState` with `state=False`.
    """


def ReturnIfMapUpdatePermissionState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


def EndIfMapHasUpdatePermission(unk_state: bool | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapUpdatePermissionState` with `event_return_type=0`, `state=True`.
    """


def EndIfMapDoesNotHaveUpdatePermission(unk_state: bool | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapUpdatePermissionState` with `event_return_type=0`, `state=False`.
    """


def RestartIfMapHasUpdatePermission(unk_state: bool | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapUpdatePermissionState` with `event_return_type=1`, `state=True`.
    """


def RestartIfMapDoesNotHaveUpdatePermission(
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `ReturnIfMapUpdatePermissionState` with `event_return_type=1`, `state=False`.
    """


def SkipLinesIfCeremonyState(line_count: int, state: bool | int, ceremony: int, event_layers=()):
    """
    TODO
    """


def SkipLinesIfCeremonyActive(line_count: int, ceremony: int, event_layers=()):
    """
    Calls `SkipLinesIfCeremonyState` with `state=True`.
    """


def SkipLinesIfCeremonyInactive(line_count: int, ceremony: int, event_layers=()):
    """
    Calls `SkipLinesIfCeremonyState` with `state=False`.
    """


def GotoIfCeremonyState(label: Label | int, state: bool | int, ceremony: int, event_layers=()):
    """
    TODO
    """


def GotoIfCeremonyActive(label: Label | int, ceremony: int, event_layers=()):
    """
    Calls `GotoIfCeremonyState` with `state=True`.
    """


def GotoIfCeremonyInactive(label: Label | int, ceremony: int, event_layers=()):
    """
    Calls `GotoIfCeremonyState` with `state=False`.
    """


def ReturnIfCeremonyState(event_return_type: EventReturnType | int, state: bool | int, ceremony: int, event_layers=()):
    """
    TODO
    """


def EndIfCeremonyActive(ceremony: int, event_layers=()):
    """
    Calls `ReturnIfCeremonyState` with `event_return_type=0`, `state=True`.
    """


def EndIfCeremonyInactive(ceremony: int, event_layers=()):
    """
    Calls `ReturnIfCeremonyState` with `event_return_type=0`, `state=False`.
    """


def RestartIfCeremonyActive(ceremony: int, event_layers=()):
    """
    Calls `ReturnIfCeremonyState` with `event_return_type=1`, `state=True`.
    """


def RestartIfCeremonyInactive(ceremony: int, event_layers=()):
    """
    Calls `ReturnIfCeremonyState` with `event_return_type=1`, `state=False`.
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
    Note that the same instruction appeared in DS3 as 1003[112].
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
    Note that the same instruction appeared in DS3 as 1003[11].
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
    Note that the same instruction appeared in DS3 as 1003[111].
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


def SkipLinesIfSpecialStandbyEndedFlagState(
    line_count: int,
    character: Character | int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def SkipLinesIfSpecialStandbyEndedFlagEnabled(line_count: int, character: Character | int, event_layers=()):
    """
    Calls `SkipLinesIfSpecialStandbyEndedFlagState` with `state=True`.
    """


def SkipLinesIfSpecialStandbyEndedFlagDisabled(line_count: int, character: Character | int, event_layers=()):
    """
    Calls `SkipLinesIfSpecialStandbyEndedFlagState` with `state=False`.
    """


def GotoIfSpecialStandbyEndedFlagState(
    label: Label | int,
    character: Character | int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def GotoIfSpecialStandbyEndedFlagEnabled(label: Label | int, character: Character | int, event_layers=()):
    """
    Calls `GotoIfSpecialStandbyEndedFlagState` with `state=True`.
    """


def GotoIfSpecialStandbyEndedFlagDisabled(label: Label | int, character: Character | int, event_layers=()):
    """
    Calls `GotoIfSpecialStandbyEndedFlagState` with `state=False`.
    """


def ReturnIfSpecialStandbyEndedFlagState(
    event_return_type: EventReturnType | int,
    character: Character | int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def EndIffSpecialStandbyEndedFlagEnabled(character: Character | int, event_layers=()):
    """
    Calls `ReturnIfSpecialStandbyEndedFlagState` with `event_return_type=0`, `state=True`.
    """


def EndIffSpecialStandbyEndedFlagDisabled(character: Character | int, event_layers=()):
    """
    Calls `ReturnIfSpecialStandbyEndedFlagState` with `event_return_type=0`, `state=False`.
    """


def RestartIffSpecialStandbyEndedFlagEnabled(character: Character | int, event_layers=()):
    """
    Calls `ReturnIfSpecialStandbyEndedFlagState` with `event_return_type=1`, `state=True`.
    """


def RestartIffSpecialStandbyEndedFlagDisabled(character: Character | int, event_layers=()):
    """
    Calls `ReturnIfSpecialStandbyEndedFlagState` with `event_return_type=1`, `state=False`.
    """


def AwaitAssetDestrucionState(
    state: bool | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


def AwaitAssetDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `AwaitAssetDestrucionState` with `state=True`.
    """


def AwaitAssetNotDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `AwaitAssetDestrucionState` with `state=False`.
    """


def GotoIfAssetDestructionState(
    label: Label | int,
    state: bool | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Note change in argument order.
    """


def GotoIfAssetDestroyed(
    label: Label | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `GotoIfAssetDestructionState` with `state=True`.
    """


def GotoIfAssetNotDestroyed(
    label: Label | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `GotoIfAssetDestructionState` with `state=False`.
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


def SetCurrentTime(
    time: tuple,
    fade_transition: bool | int,
    wait_for_completion: bool | int,
    show_clock: bool | int,
    clock_start_delay: float,
    clock_change_duration: float,
    clock_finish_delay: float,
    event_layers=(),
):
    """
    TODO
    """


def SetTimeFreezeState(state: bool | int, event_layers=()):
    """
    TODO
    """


def FreezeTime(event_layers=()):
    """
    Calls `SetTimeFreezeState` with `state=True`.
    """


def UnfreezeTime(event_layers=()):
    """
    Calls `SetTimeFreezeState` with `state=False`.
    """


def PlayCutsceneToPlayerWithWeatherAndTime(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    player_id: int,
    change_weather: bool | int = False,
    weather: Weather | int = 0,
    weather_duration: float = -1.0,
    change_time: bool | int = False,
    time: tuple = (0, 0, 0),
    event_layers=(),
):
    """
    TODO
    """


def PlayCutsceneToPlayerAndWarp(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    map_id: int,
    player_id: int,
    unk_20_24: int,
    unk_24_25: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def PlayCutsceneToPlayerAndWarpWithWeatherAndTime(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    map_id: int,
    player_id: int,
    unk_20_24: int,
    unk_24_25: bool | int,
    change_weather: bool | int,
    weather: Weather | int = 0,
    weather_duration: float = -1.0,
    change_time: bool | int = False,
    time: tuple = (0, 0, 0),
    event_layers=(),
):
    """
    TODO
    """


def PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    move_to_region: Region | int,
    map_id: int,
    player_id: int,
    unk_16_20: int,
    unk_20_21: bool | int,
    update_stable_position: bool | int,
    event_layers=(),
):
    """
    TODO
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


def WarpPlayerToRespawnPoint(respawn_point_id: int, event_layers=()):
    """
    Not used in vanilla Elden Ring events, but keeping in case it still works (seems useful).
    """


def StartEnemySpawner(spawner_id: int, event_layers=()):
    """
    Not used in vanilla Elden Ring events, but keeping in case it still works (seems useful).
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
    Not used in vanilla Elden Ring events, but keeping in case it still works (seems useful).
    """


def TriggerAISound(
    ai_sound_param_id: int,
    anchor_entity: Asset | Region | Character | int,
    unk_8_12: int,
    event_layers=(),
):
    """
    TODO
    """


def ForceSpawnerToSpawn(spawner: SpawnerEvent | int, event_layers=()):
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


def SetFlagState(flag_type: FlagType | int, flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    Predominant flag-setting instruction in Elden Ring. It can set relative flags, unlike the old 2003[2].
    """


def EnableFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=0`, `state=1`.
    """


def DisableFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=0`, `state=0`.
    """


def ToggleFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=0`, `state=2`.
    """


def SetAbsoluteFlagState(flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=0`.
    """


def EnableThisSlotFlag(event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=2`, `flag=0`, `state=1`.
    """


def DisableThisSlotFlag(event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=2`, `flag=0`, `state=0`.
    """


def SetWeather(weather: Weather | int, duration: float, immediate_change: bool | int, event_layers=()):
    """
    TODO
    """


def SetNetworkFlagState(flag_type: FlagType | int, flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    Enable, disable, or toggle (change) a binary flag for all network-connected players.
    """


def EnableNetworkFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=0`, `state=1`.
    """


def DisableNetworkFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=0`, `state=0`.
    """


def ToggleNetworkFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=0`, `state=2`.
    """


def SetAbsoluteNetworkFlagState(flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=0`.
    """


def EnableThisNetworkFlag(event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=1`, `flag=0`, `state=1`.
    """


def DisableThisNetworkFlag(event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=1`, `flag=0`, `state=0`.
    """


def EnableThisNetworkSlotFlag(event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=2`, `flag=0`, `state=1`.
    """


def DisableThisNetworSlotFlag(event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=2`, `flag=0`, `state=0`.
    """


def SetNetworkInteractionState(state: bool | int, event_layers=()):
    """
    TODO
    """


def AwardGesture(gesture_param_id: int, event_layers=()):
    """
    Awards a Gesture item to player.
    """


def MultiplyBloodstainSouls(multiplier: float, bloodstain_save_slot_id: int, event_layers=()):
    """
    Apply a multiplier to the amount of souls/echoes/runes waiting to be retrieved from the bloodstain with
    the given save slot ID.
    """


def IncreaseCharacterSoulReward(
    character: Character | int,
    fixed_increase_amount: int,
    soul_amount_load_slot_id: int,
    event_layers=(),
):
    """
    TODO
    """


def IssueEndOfPseudoMultiplayerNotification(success: bool | int, event_layers=()):
    """
    TODO
    """


def UseFarViewCamera(far_view_id: int, asset: Asset | int, model_point: int = -1, event_layers=()):
    """
    TODO
    """


def SetPlayerPositionDisplay(
    state: bool | int,
    aboveground: bool | int,
    game_map: Map | MapTile | tuple | list,
    x: float,
    y: float,
    z: float,
    event_layers=(),
):
    """
    TODO
    """


def SetPseudoMultiplayerReturnPosition(region: Region | int, event_layers=()):
    """
    TODO
    """


def OpenWorldMapPoint(world_map_point_param_id: int, distance: float, event_layers=()):
    """
    TODO
    """


def SendNPCSummonHome(character: Character | int, event_layers=()):
    """
    TODO
    """


def ShowLoadingScreenText(state: bool | int, event_layers=()):
    """
    Enable or disable text on loading screens.
    """


def EnableLoadingScreenText(event_layers=()):
    """
    Calls `ShowLoadingScreenText` with `state=True`.
    """


def DisableLoadingScreenText(event_layers=()):
    """
    Calls `ShowLoadingScreenText` with `state=False`.
    """


def RemoveGesture(gesture_param_id: int, event_layers=()):
    """
    Remove given Gesture from player's inventory'.
    """


def EraseNPCSummonSign(character: Character | int, event_layers=()):
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


def SetCharacterTalkRange(character: Character | int, distance: float, event_layers=()):
    """
    TODO
    """


def ConnectCharacterToCaravan(character: Character | int, caravan_asset: Asset | int, event_layers=()):
    """
    Used to connect trolls to the caravans they pull.
    """


def Unknown_2004_61(unk_0_4: int, event_layers=()):
    """
    Used only once: in Stranded Graveyard with argument 9999.
    """


def SetCharacterEnableDistance(character: Character | int, distance: float, event_layers=()):
    """
    TODO
    """


def CopyPlayerCharacterData(source_character: Character | int, dest_character: Character | int, event_layers=()):
    """
    Used, for example, to initialize Mimics and set up Gideon's boss loadout.
    """


def AttachAssetToCharacter(character: Character | int, model_point: int, asset: Asset | int, event_layers=()):
    """
    TODO
    """


def SetCharacterDisableOnCollisionUnload(character: Character | int, state: bool | int, event_layers=()):
    """
    I believe this will, if enabled for a character, cause that character to be disabled when the collision they
    are standing on (or possibly their draw parent) is unloaded.
    """


def SetDistanceBasedNetworkAuthorityUpdate(character: Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def Unknown_2004_71(
    unk_0_4: int,
    entity_a: Asset | Region | Character | int,
    entity_b: Asset | Region | Character | int,
    event_layers=(),
):
    """
    TODO
    """


def SetCharacterFadeOnEnable(character: Character | int, state: bool | int, event_layers=()):
    """
    Determines if character will fade-in when enabled, I believe.
    """


def MoveCharacterAndCopyDrawParentWithFadeout(
    character: Character | int,
    destination_type: CoordEntityType | int,
    destination: Asset | Region | Character | int,
    model_point: int,
    copy_draw_parent: Asset | Region | Character | int,
    use_bonfire_effect: bool | int,
    reset_camera: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def SetCharacterFaceParamOverride(character: Character | int, override_slot: int, face_param_id: int, event_layers=()):
    """
    TODO
    """


def Unknown_2004_76(flag: Flag | int, item_lot: int, event_layers=()):
    """
    TODO
    """


def FadeToBlack(
    strength: float,
    duration: float,
    freeze_player: bool | int,
    freeze_player_delay: float,
    event_layers=(),
):
    """
    TODO
    """


def CopyPlayerCharacterDataFromOnlinePlayers(
    pool_type: int,
    failcase_player_param_id: int,
    target_character: Character | int,
    event_layers=(),
):
    """
    TODO
    """


def RequestPlayerCharacterDataFromOnlinePlayers(pool_type: int, data_count: int, event_layers=()):
    """
    TODO
    """


def SendPlayerCharacterDataToOnlinePlayers(pool_type: int, event_layers=()):
    """
    TODO
    """


def ResetCharacterPosition(character: Character | int, event_layers=()):
    """
    Resets character position to MSB coordinates, I assume.
    """


def SetSpecialStandbyEndedFlag(character: Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


def SetCharacterEnableDistanceWithUnknown(
    character: Character | int,
    enable_distance: float,
    unknown_distance: float,
    event_layers=(),
):
    """
    TODO
    """


def AttachCaravanToController(caravan_asset: Asset | int, character: Character | int, event_layers=()):
    """
    Attaches caravan to trolls pulling it, presuamably (there is also an inverse event).
    """


def AttachAssetToAsset(
    child_asset: Asset | int,
    parent_asset: Asset | int,
    parent_model_point: int = -1,
    event_layers=(),
):
    """
    TODO
    """


def DestroyAsset_NoSlot(asset: Asset | int, event_layers=()):
    """
    No 'slot' argument here.
    """


def CreateBigHazardousAsset(
    asset_flag: Flag | int,
    asset: int,
    model_point_start: int,
    model_point_end: int,
    behaviour_id: int,
    target_type: DamageTargetType | int,
    radius: float,
    life: float,
    repetition_time: float,
    event_layers=(),
):
    """
    TODO
    """


def SetWindVFX(wind_vfx_id: int, event_layers=()):
    """
    Not sure if argument is an MSB VFX Event ID (more likely) or an absolute VFX asset ID.
    """


def DisplayDialogAndSetFlags(
    message: EventText | int,
    button_type: ButtonType | int,
    number_buttons: NumberButtons | int,
    anchor_entity: Asset | Region | Character | int,
    display_distance: float,
    left_flag: Flag | int,
    right_flag: Flag | int,
    cancel_flag: Flag | int,
    event_layers=(),
):
    """
    Displays a dialog and enables one of three flags, depending on the player's response. Very useful.
    """


def DisplayFlashingMessageWithPriority(
    text: EventText | int,
    priority: int,
    should_interrupt: bool | int,
    event_layers=(),
):
    """
    TODO
    """


def DisplaySubareaWelcomeMessage(text: EventText | int, event_layers=()):
    """
    TODO
    """


def DisplayAreaWelcomeMessage(text: EventText | int, event_layers=()):
    """
    TODO
    """


def DisplayTutorialMessage(tutorial_param_id: int, unk_4_5: bool | int, unk_5_6: bool | int, event_layers=()):
    """
    TODO
    """


def DisplayNetworkMessage(text: EventText | int, unk_4_5: bool | int, event_layers=()):
    """
    TODO
    """


def SetCameraAngle(x_angle: float, y_angle: float, event_layers=()):
    """
    Used very often, presumably to gently push the camera to a specific latitude/longitude.
    """


def BanishInvaders(unknown: int, event_layers=()):
    """
    TODO
    """


def BanishPhantoms(unknown: int, event_layers=()):
    """
    TODO
    """


def SuppressSoundEvent(sound_id: int, unk_4_8: int, suppression_active: bool | int, event_layers=()):
    """
    TODO
    """


def UnknownSound_2010_8(sound_id: int, event_layers=()):
    """
    TODO
    """


def SetBossMusic(bgm_boss_conv_param_id: int, state: BossMusicState | int, event_layers=()):
    """
    TODO
    """


def SuppressSoundForFogGate(duration: float, event_layers=()):
    """
    TODO
    """


def SetFieldBattleMusicHeatUp(npc_threat_level: int, state: bool | int, event_layers=()):
    """
    TODO
    """


def EnableFieldBattleMusicHeatUp(npc_threat_level: int, event_layers=()):
    """
    Calls `SetFieldBattleMusicHeatUp` with `state=True`.
    """


def DisableFieldBattleMusicHeatUp(npc_threat_level: int, event_layers=()):
    """
    Calls `SetFieldBattleMusicHeatUp` with `state=False`.
    """


def SetAreaWelcomeMessageState(state: bool | int, event_layers=()):
    """
    TODO
    """


def ActivateGparamOverride(gparam_sub_id: int, change_duration: float, event_layers=()):
    """
    TODO
    """


def DeactivateGparamOverride(change_duration: float, event_layers=()):
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


def TimeOfDay(time: tuple, event_layers=()) -> bool:
    ...


def TimeOfDayInRange(earliest: tuple, latest: tuple, event_layers=()) -> bool:
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
    entity: Asset | Region | Character | int,
    other_entity: Asset | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def PlayerWithinDistance(
    other_entity: Asset | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def PlayerBeyondDistance(
    other_entity: Asset | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def EntityWithinDistance(
    entity: Asset | Region | Character | int,
    other_entity: Asset | Region | Character | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def EntityBeyondDistance(
    entity: Asset | Region | Character | int,
    other_entity: Asset | Region | Character | int,
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
    anchor_entity: Asset | Region | Character | int,
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


def Multiplayer(event_layers=()) -> bool:
    ...


def MultiplayerPending(event_layers=()) -> bool:
    ...


def Singleplayer(event_layers=()) -> bool:
    ...


def Invasion(event_layers=()) -> bool:
    ...


def InvasionPending(event_layers=()) -> bool:
    ...


def AllPlayersRegionState(state: bool | int, region: Region | int, event_layers=()) -> bool:
    ...


def AllPlayersInsideRegion(region: Region | int, event_layers=()) -> bool:
    ...


def AllPlayersOutsideRegion(region: Region | int, event_layers=()) -> bool:
    ...


def MapPresenceState(state: bool | int, game_map: Map | MapTile | tuple | list, event_layers=()) -> bool:
    ...


def InsideMap(game_map: Map | MapTile | tuple | list, event_layers=()) -> bool:
    ...


def OutsideMap(game_map: Map | MapTile | tuple | list, event_layers=()) -> bool:
    ...


def MultiplayerEvent(event_id: int, event_layers=()) -> bool:
    ...


def EnabledFlagCountComparison(
    flag_type: FlagType | int,
    comparison_type: ComparisonType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def EnabledFlagCountEqual(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def EnabledFlagCountNotEqual(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def EnabledFlagCountGreaterThan(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def EnabledFlagCountLessThan(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def EnabledFlagCountGreaterThanOrEqual(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
    ...


def EnabledFlagCountLessThanOrEqual(
    flag_type: FlagType | int,
    flag_range: FlagRange | tuple | list,
    value: int,
    event_layers=(),
) -> bool:
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
    anchor_entity: Asset | Region | Character | int,
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
    anchor_entity: Asset | Region | Character | int,
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
    anchor_entity: Asset | Region | Character | int,
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


def HealthRatioComparison(
    character: Character | int,
    comparison_type: ComparisonType | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthRatioEqual(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthRatioNotEqual(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthRatioGreaterThan(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthRatioLessThan(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthRatioGreaterThanOrEqual(
    character: Character | int,
    value: float,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def HealthRatioLessThanOrEqual(
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


def CharacterTargetingState(
    targeting_character: Character | int,
    targeted_character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterTargeting(
    targeting_character: Character | int,
    targeted_character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterNotTargeting(
    targeting_character: Character | int,
    targeted_character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
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


def PlayerClass(class_type: ClassType | int, event_layers=()) -> bool:
    ...


def PlayerCovenant(covenant: int, event_layers=()) -> bool:
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


def AssetDestructionState(
    state: bool | int,
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetNotDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetDamaged(asset: Asset | int, attacker: Character | int, event_layers=()) -> bool:
    ...


def AssetActivated(obj_act_id: int, event_layers=()) -> bool:
    ...


def AssetHealthValueComparison(
    asset: Asset | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
) -> bool:
    ...


def AssetHealthValueEqual(asset: Asset | int, value: int, event_layers=()) -> bool:
    ...


def AssetHealthValueNotEqual(asset: Asset | int, value: int, event_layers=()) -> bool:
    ...


def AssetHealthValueGreaterThan(asset: Asset | int, value: int, event_layers=()) -> bool:
    ...


def AssetHealthValueLessThan(asset: Asset | int, value: int, event_layers=()) -> bool:
    ...


def AssetHealthValueGreaterThanOrEqual(asset: Asset | int, value: int, event_layers=()) -> bool:
    ...


def AssetHealthValueLessThanOrEqual(asset: Asset | int, value: int, event_layers=()) -> bool:
    ...


def PlayerMovingOnCollision(collision: Collision | int, event_layers=()) -> bool:
    ...


def PlayerRunningOnCollision(collision: Collision | int, event_layers=()) -> bool:
    ...


def PlayerStandingOnCollision(collision: Collision | int, event_layers=()) -> bool:
    ...


def UnsignedComparison(comparison_type: ComparisonType | int, left: int, right: int, event_layers=()) -> bool:
    ...


def UnsignedEqual(left: int, right: int, event_layers=()) -> bool:
    ...


def UnsignedNotEqual(left: int, right: int, event_layers=()) -> bool:
    ...


def UnsignedGreaterThan(left: int, right: int, event_layers=()) -> bool:
    ...


def UnsignedLessThan(left: int, right: int, event_layers=()) -> bool:
    ...


def UnsignedGreaterThanOrEqual(left: int, right: int, event_layers=()) -> bool:
    ...


def UnsignedLessThanOrEqual(left: int, right: int, event_layers=()) -> bool:
    ...


def AttackedWithDamageType(
    attacked_entity: Character | int,
    attacker: Character | int = 0,
    damage_type: DamageType | int = DamageType.Unspecified,
    event_layers=(),
) -> bool:
    ...


def ActionButtonParamActivated(action_button_id: int, entity: Asset | Region | Character | int, event_layers=()) -> bool:
    ...


def PlayerOwnWorldState(not_in_own_world: bool | int, event_layers=()) -> bool:
    ...


def PlayerInOwnWorld(event_layers=()) -> bool:
    ...


def PlayerNotInOwnWorld(event_layers=()) -> bool:
    ...


def MapLoaded(game_map: Map | MapTile | tuple | list, event_layers=()) -> bool:
    ...


def WeatherState(weather: Weather | int, unk_4_8: float, unk_8_12: float, event_layers=()) -> bool:
    ...


def MapUpdatePermissionState(
    state: bool | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
) -> bool:
    ...


def MapHasUpdatePermission(unk_state: bool | int, game_map: Map | MapTile | tuple | list, event_layers=()) -> bool:
    ...


def MapDoesNotHaveUpdatePermission(unk_state: bool | int, game_map: Map | MapTile | tuple | list, event_layers=()) -> bool:
    ...


def FieldBattleMusicState(npc_threat_level: int, state: bool | int, event_layers=()) -> bool:
    ...


def FieldBattleMusicEnabled(npc_threat_level: int, event_layers=()) -> bool:
    ...


def FieldBattleMusicDisabled(npc_threat_level: int, event_layers=()) -> bool:
    ...


def PlayerHasArmorEquipped(armor_type: ArmorType | int, armor: ArmorParam | int, unk_8_12: int = -1, event_layers=()) -> bool:
    ...


def PlayerHasHeadArmorEquipped(armor: ArmorParam | int, unk_8_12: int = -1, event_layers=()) -> bool:
    ...


def PlayerHasBodyArmorEquipped(armor: ArmorParam | int, unk_8_12: int = -1, event_layers=()) -> bool:
    ...


def PlayerHasArmsArmorEquipped(armor: ArmorParam | int, unk_8_12: int = -1, event_layers=()) -> bool:
    ...


def PlayerHasLegsArmorEquipped(armor: ArmorParam | int, unk_8_12: int = -1, event_layers=()) -> bool:
    ...


def CeremonyState(state: bool | int, ceremony: int, event_layers=()) -> bool:
    ...


def CeremonyActive(ceremony: int, event_layers=()) -> bool:
    ...


def CeremonyInactive(ceremony: int, event_layers=()) -> bool:
    ...


def WeatherLotState(weather_lot_param_id: int, state: bool | int, event_layers=()) -> bool:
    ...


def WeatherLotActive(weather_lot_param_id: int, event_layers=()) -> bool:
    ...


def WeatherLotInactive(weather_lot_param_id: int, event_layers=()) -> bool:
    ...


def PlayerGender(gender: Gender | int, event_layers=()) -> bool:
    ...


def AllyPhantomCountComparison(
    comparison_state: bool | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
) -> bool:
    ...


def CharacterProportionDeathState(
    character: Character | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterProportionDead(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterProportionAlive(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterProportionSpecialEffectState(
    character_group: Character | int,
    special_effect: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterProportionHasSpecialEffect(
    character_group: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterProportionDoesNotHaveSpecialEffect(
    character_group: Character | int,
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def PlayerTargeted(
    min_npc_threat_level: int,
    max_npc_threat_level: int,
    ai_status: AIStatusType | int,
    event_layers=(),
) -> bool:
    ...


def NPCPartAttackedWithDamageType(
    character: Character | int,
    npc_part_id: int,
    attacker: Character | int = -1,
    damage_type: DamageType | int = DamageType.Unspecified,
    event_layers=(),
) -> bool:
    ...


def CharacterInvadeType(
    character: Character | int,
    invade_type: CharacterType | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterMountState(character: Character | int, is_mounted: bool | int, event_layers=()) -> bool:
    ...


def CharacterMounted(character: Character | int, event_layers=()) -> bool:
    ...


def CharacterNotMounted(character: Character | int, event_layers=()) -> bool:
    ...


def CharacterStateInfoState(
    character: Character | int,
    state_info: int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterHasStateInfo(
    character: Character | int,
    state_info: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def CharacterDoesNotHaveStateInfo(
    character: Character | int,
    state_info: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def SpecialStandbyEndedFlagState(character: Character | int, state: bool | int, event_layers=()) -> bool:
    ...


def SpecialStandbyEndedFlagEnabled(character: Character | int, event_layers=()) -> bool:
    ...


def SpecialStandbyEndedFlagDisabled(character: Character | int, event_layers=()) -> bool:
    ...


def AssetProportionDestructionState(
    state: bool | int,
    asset_group: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_proportion: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetBackreadState(
    asset: Asset | int,
    state: bool | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetBackreadEnabled(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetBackreadDisabled(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def ActionButton(
    prompt_text: EventText | int,
    anchor_entity: Asset | Region | Character | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    max_distance: float = None,
    model_point: int = -1,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    boss_version: bool = False,
    line_intersects: Asset | Region | Character | int = None,
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


def PlayerDoesNotHaveWeapon(weapon: WeaponParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerDoesNotHaveWeapon`.
    """
    ...


def PlayerDoesNotHaveArmor(armor: ArmorParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerDoesNotHaveArmor`.
    """
    ...


def PlayerDoesNotHaveRing(ring: AccessoryParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerDoesNotHaveRing`.
    """
    ...


def PlayerDoesNotHaveGood(good: GoodParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerDoesNotHaveGood`.
    """
    ...


def EnabledFlagCount(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, event_layers=()) -> int:
    """
    Compare output to a value as a shortcut for calling `EnabledFlagCountComparison(...)`.
    """
    ...


def EventValue(flag: Flag | int, bit_count: int, event_layers=()) -> int:
    """
    Compare output to a value as a shortcut for calling `EventValueComparison(...)`.
    """
    ...


def HealthRatio(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> float:
    """
    Compare output to a value as a shortcut for calling `HealthRatioComparison(...)`.
    """
    ...


def CharacterPartHealth(character: Character | int, npc_part_id: int, event_layers=()) -> float:
    """
    Compare output to a value as a shortcut for calling `CharacterPartHealthComparison(...)`.
    """
    ...


def PlayerLevel(event_layers=()) -> int:
    """
    Compare output to a value as a shortcut for calling `PlayerLevelComparison(...)`.
    """
    ...


def HealthValue(
    character: Character | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> int:
    """
    Compare output to a value as a shortcut for calling `HealthValueComparison(...)`.
    """
    ...


def AssetHealthValue(asset: Asset | int, event_layers=()) -> int:
    """
    Compare output to a value as a shortcut for calling `AssetHealthValueComparison(...)`.
    """
    ...


def AllyPhantomCount(comparison_state: bool | int, event_layers=()) -> int:
    """
    Compare output to a value as a shortcut for calling `AllyPhantomCountComparison(...)`.
    """
    ...
