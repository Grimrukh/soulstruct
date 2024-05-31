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
    "RunCommonEvent",
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
    "IfEventsComparison",  # 3[20]
    "IfOnlineState",  # 3[22]
    "IfOnline",
    "IfOffline",
    "IfCharacterDeathState",  # 4[0]
    "IfCharacterDead",
    "IfCharacterAlive",
    "IfHealthRatioComparison",  # 4[2]
    "IfHealthRatioEqual",
    "IfHealthRatioNotEqual",
    "IfHealthRatioGreaterThan",
    "IfHealthRatioLessThan",
    "IfHealthRatioGreaterThanOrEqual",
    "IfHealthRatioLessThanOrEqual",
    "IfCharacterIsType",  # 4[3]
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
    "SkipLinesIfLastConditionResultState",  # 1000[7]
    "SkipLinesIfLastConditionResultTrue",
    "SkipLinesIfLastConditionResultFalse",
    "ReturnIfLastConditionResultState",  # 1000[8]
    "EndIfLastConditionResultTrue",
    "EndIfLastConditionResultFalse",
    "RestartIfLastConditionResultTrue",
    "RestartIfLastConditionResultFalse",
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
    "SetNetworkSyncState",  # 2000[2]
    "EnableNetworkSync",
    "DisableNetworkSync",
    "ClearMainCondition",  # 2000[3]
    "SaveRequest",  # 2000[5]
    "StartPS5Activity",  # 2000[7]
    "EndPS5Activity",  # 2000[8]
    "PlayCutsceneToAll",  # 2002[1]
    "PlayCutsceneToPlayer",  # 2002[3]
    "PlayCutsceneToPlayer_Unknown_2002_04",  # 2002[4]
    "PlayCutsceneToPlayer_Unknown_2002_09",  # 2002[9]
    "SetSpawnerState",  # 2003[3]
    "EnableSpawner",
    "DisableSpawner",
    "AwardItemLotToAllPlayers",  # 2003[4]
    "ShootProjectile",  # 2003[5]
    "SetMapCollisionState_2003_06",  # 2003[6]
    "EnableMapCollision_2003_06",
    "DisableMapCollision_2003_06",
    "SetMapVisibilityState",  # 2003[7]
    "EnableMapVisibility",
    "DisableMapVisibility",
    "SetEventSlotState",  # 2003[8]
    "EndEventSlot",
    "EndEvent",
    "RestartEventSlot",
    "RestartEvent",
    "InvertFlag",  # 2003[9]
    "SetBossHealthBarState",  # 2003[11]
    "EnableBossHealthBar",
    "DisableBossHealthBar",
    "KillBossAndDisplayBanner",  # 2003[12]
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
    "IncrementNewGameCycle",  # 2003[21]
    "SetFlagRangeState",  # 2003[22]
    "EnableFlagRange",
    "DisableFlagRange",
    "ToggleFlagRange",
    "SetRespawnPoint",  # 2003[23]
    "RemoveItemFromPlayer",  # 2003[24]
    "RemoveWeaponFromPlayer",
    "RemoveArmorFromPlayer",
    "RemoveTalismanFromPlayer",
    "RemoveGoodFromPlayer",
    "PlaceSummonSign",  # 2003[25]
    "SetSoapstoneMessageState",  # 2003[26]
    "EnableSoapstoneMessage",
    "DisableSoapstoneMessage",
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
    "Kill",  # 2004[4]
    "SetCharacterState",  # 2004[5]
    "EnableCharacter",
    "DisableCharacter",
    "EzstateAIRequest",  # 2004[6]
    "CreateProjectileOwner",  # 2004[7]
    "AddSpecialEffect",  # 2004[8]
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
    "ReferDamageToEntity",  # 2004[33]
    "SetNetworkUpdateRate",  # 2004[34]
    "SetBackreadStateAlternate",  # 2004[35]
    "DropMandatoryTreasure",  # 2004[37]
    "BetrayCurrentCovenant",  # 2004[38]
    "SetAnimationsState",  # 2004[39]
    "EnableAnimations",
    "DisableAnimations",
    "MoveAndSetDrawParent",  # 2004[40]
    "ShortMove",  # 2004[41]
    "MoveAndCopyDrawParent",  # 2004[42]
    "ResetAnimation",  # 2004[43]
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
    "IfArenaMatchReadyState",  # 3[39]
    "IfArenaSoloResult",  # 3[40]
    "IfArenaSoloScoreComparison",  # 3[41]
    "IfArenaTeamResults",  # 3[42]
    "IfArenaTeamScoreComparison",  # 3[43]
    "IfArenaMatchType",  # 3[44]
    "IfPlayerRespawnedInArena",  # 3[45]
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
    "GotoIfLastConditionResultState",  # 1000[107]
    "GotoIfLastConditionResultTrue",
    "GotoIfLastConditionResultFalse",
    "GotoIfUnsignedComparison",  # 1000[108]
    "GotoIfUnsignedEqual",
    "GotoIfUnsignedNotEqual",
    "GotoIfUnsignedGreaterThan",
    "GotoIfUnsignedLessThan",
    "GotoIfUnsignedGreaterThanOrEqual",
    "GotoIfUnsignedLessThanOrEqual",
    "WaitUntilTimeOfDayInRange",  # 1001[5]
    "WaitRealFrames",  # 1001[6]
    "WaitUntilArenaHalfTime",  # 1001[8]
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
    "SkipLinesIfArenaMatchType",  # 1003[212]
    "GotoLinesIfArenaMatchType",  # 1003[213]
    "ReturnIfArenaMatchType",  # 1003[214]
    "EndIfArenaMatchType",
    "RestartIfArenaMatchType",
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
    "SetDirectionDisplay",  # 2003[44]
    "EnableDirectionDisplay",
    "DisableDirectionDisplay",
    "TriggerAISound",  # 2003[52]
    "ForceSpawnerToSpawn",  # 2003[54]
    "SetNetworkConnectedFlagRangeState",  # 2003[63]
    "EnableNetworkConnectedFlagRange",
    "DisableNetworkConnectedFlagRange",
    "ToggleNetworkConnectedFlagRange",
    "SetOmissionModeCounts",  # 2003[64]
    "ResetOmissionModeCountsToDefault",  # 2003[65]
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
    "Unknown_2003_83",  # 2003[83]
    "ChangeCharacterCloth",  # 2004[48]
    "ChangePatrolBehavior",  # 2004[49]
    "SetLockOnPoint",  # 2004[50]
    "ChangePlayerCharacterInitParam",  # 2004[52]
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
    "CreateBigHazardousAsset",  # 2005[20]
    "SetWindVFX",  # 2006[6]
    "AwaitDialogResponse",  # 2007[10]
    "DisplayFlashingMessageWithPriority",  # 2007[12]
    "DisplaySubareaWelcomeMessage",  # 2007[13]
    "DisplayAreaWelcomeMessage",  # 2007[14]
    "DisplayTutorialMessage",  # 2007[15]
    "DisplayNetworkMessage",  # 2007[16]
    "SetCameraAngle",  # 2008[4]
    "BanishInvaders",  # 2009[8]
    "BanishPhantoms",  # 2009[11]
    "BanishPhantomsAndUpdateServerPvPStats",  # 2009[12]
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
    "IfPlayerHasTalisman",
    "IfPlayerHasGood",
    "IfPlayerDoesNotHaveItem",
    "IfPlayerDoesNotHaveWeapon",
    "IfPlayerDoesNotHaveArmor",
    "IfPlayerDoesNotHaveTalisman",
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
    "EventsComparison",
    "OnlineState",
    "Online",
    "Offline",
    "CharacterDeathState",
    "CharacterDead",
    "CharacterAlive",
    "HealthRatioComparison",
    "HealthRatioEqual",
    "HealthRatioNotEqual",
    "HealthRatioGreaterThan",
    "HealthRatioLessThan",
    "HealthRatioGreaterThanOrEqual",
    "HealthRatioLessThanOrEqual",
    "CharacterIsType",
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
    "ArenaMatchReadyState",
    "ArenaSoloResult",
    "ArenaSoloScoreComparison",
    "ArenaTeamResults",
    "ArenaTeamScoreComparison",
    "ArenaMatchType",
    "PlayerRespawnedInArena",
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
    "PlayerHasTalisman",
    "PlayerHasGood",
    "PlayerDoesNotHaveWeapon",
    "PlayerDoesNotHaveArmor",
    "PlayerDoesNotHaveTalisman",
    "PlayerDoesNotHaveGood",
    "EnabledFlagCount",
    "EventValue",
    "HealthRatio",
    "CharacterPartHealth",
    "PlayerLevel",
    "HealthValue",
    "AssetHealthValue",
]

import typing as tp

from soulstruct.eldenring.game_types import *
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


def RunEvent(event_id: int | tp.Callable, slot: int = 0, args = (0,), arg_types = "", event_layers=()):
    """Run an event by its ID or function. This should NOT be an event defined in `common_func`."""
    ...


def RunCommonEvent(event_id: int | tp.Callable, slot: int = 0, args = (0,), arg_types = "", event_layers=()):
    """
     Run a common event by its ID or function. Also accepts slot, though the purpose of it is unclear. 

    This event is typically defined in `common_func` but may also be local.
    """
    ...


# (0, 0)
def IfConditionState(
    condition: ConditionGroup | int,
    state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    TODO
    """


# (0, 0)
def IfConditionTrue(condition: ConditionGroup | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfConditionState` with `state=True`.
    """


# (0, 0)
def IfConditionFalse(condition: ConditionGroup | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfConditionState` with `state=False`.
    """


# (0, 1)
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


# (0, 1)
def IfValueEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=0`.
    """


# (0, 1)
def IfValueNotEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=1`.
    """


# (0, 1)
def IfValueGreaterThan(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=2`.
    """


# (0, 1)
def IfValueLessThan(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=3`.
    """


# (0, 1)
def IfValueGreaterThanOrEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=4`.
    """


# (0, 1)
def IfValueLessThanOrEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfValueComparison` with `comparison_type=5`.
    """


# (1, 0)
def IfTimeElapsed(condition: ConditionGroup | int, seconds: float, event_layers=()):
    """
    Time since event started.
    """


# (1, 1)
def IfFramesElapsed(condition: ConditionGroup | int, frames: int, event_layers=()):
    """
    Frames since event started.
    """


# (1, 2)
def IfRandomTimeElapsed(condition: ConditionGroup | int, min_seconds: float, max_seconds: float, event_layers=()):
    """
    Not used in vanilla DS1. Requires a random amount of time since event began.
    """


# (1, 3)
def IfRandomFramesElapsed(condition: ConditionGroup | int, min_frames: int, max_frames: int, event_layers=()):
    """
    Not used in vanilla DS1. Requires a random amount of frames since event began.
    """


# (1, 4)
def IfTimeOfDay(condition: ConditionGroup | int, time: tuple, event_layers=()):
    """
    Checks if current in-game time is EXACTLY the given time, down to the second.
    """


# (1, 5)
def IfTimeOfDayInRange(condition: ConditionGroup | int, earliest: tuple, latest: tuple, event_layers=()):
    """
    Checks if current in-game time is between an earliest and latest time, each specified down to the second.
    
    Note that ranges will loop over midnight as expected, so checking, e.g., if the time is within the three-
    hour range between hour 23 (PM) and hour 2 (AM) is straightforward: `earliest=(23, 0, 0), latest=(2, 0, 0)`.
    """


# (3, 0)
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


# (3, 0)
def IfFlagEnabled(condition: ConditionGroup | int, flag: Flag | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=0`.
    """


# (3, 0)
def IfFlagDisabled(condition: ConditionGroup | int, flag: Flag | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=0`.
    """


# (3, 0)
def IfThisEventFlagEnabled(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


# (3, 0)
def IfThisEventFlagDisabled(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


# (3, 0)
def IfThisEventSlotFlagEnabled(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


# (3, 0)
def IfThisEventSlotFlagDisabled(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


# (3, 1)
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


# (3, 1)
def IfFlagRangeAllEnabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `IfFlagRangeState` with `state=0`, `flag_type=0`.
    """


# (3, 1)
def IfFlagRangeAllDisabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `IfFlagRangeState` with `state=1`, `flag_type=0`.
    """


# (3, 1)
def IfFlagRangeAnyEnabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `IfFlagRangeState` with `state=2`, `flag_type=0`.
    """


# (3, 1)
def IfFlagRangeAnyDisabled(condition: ConditionGroup | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `IfFlagRangeState` with `state=3`, `flag_type=0`.
    """


# (3, 2)
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


# (3, 2)
def IfPlayerInsideRegion(
    condition: ConditionGroup | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfCharacterRegionState` with `state=True`, `character=10000`.
    """


# (3, 2)
def IfPlayerOutsideRegion(
    condition: ConditionGroup | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfCharacterRegionState` with `state=False`, `character=10000`.
    """


# (3, 2)
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


# (3, 2)
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


# (3, 3)
def IfEntityDistanceState(
    condition: ConditionGroup | int,
    state: bool | int,
    entity: Asset | Character | Region | int,
    other_entity: Asset | Character | Region | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Same new argument as region test, with unknown purpose, and again always 1 in EMEVD resources.
    """


# (3, 3)
def IfPlayerWithinDistance(
    condition: ConditionGroup | int,
    other_entity: Asset | Character | Region | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=True`, `entity=10000`.
    """


# (3, 3)
def IfPlayerBeyondDistance(
    condition: ConditionGroup | int,
    other_entity: Asset | Character | Region | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=False`, `entity=10000`.
    """


# (3, 3)
def IfEntityWithinDistance(
    condition: ConditionGroup | int,
    entity: Asset | Character | Region | int,
    other_entity: Asset | Character | Region | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `IfEntityDistanceState` with `state=True`.
    """


# (3, 3)
def IfEntityBeyondDistance(
    condition: ConditionGroup | int,
    entity: Asset | Character | Region | int,
    other_entity: Asset | Character | Region | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
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
    event_layers=(),
):
    """
    TODO
    item_type: Auto-detected from `item` type by default.
    """


# (3, 6)
def IfMultiplayerState(condition: ConditionGroup | int, state: MultiplayerState | int, event_layers=()):
    """
    TODO
    """


# (3, 6)
def IfHost(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=0`.
    """


# (3, 6)
def IfClient(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=1`.
    """


# (3, 6)
def IfMultiplayer(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=2`.
    """


# (3, 6)
def IfMultiplayerPending(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=3`.
    """


# (3, 6)
def IfSingleplayer(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=4`.
    """


# (3, 6)
def IfInvasion(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=5`.
    """


# (3, 6)
def IfInvasionPending(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfMultiplayerState` with `state=6`.
    """


# (3, 7)
def IfAllPlayersRegionState(condition: ConditionGroup | int, state: bool | int, region: Region | int, event_layers=()):
    """
    TODO
    """


# (3, 7)
def IfAllPlayersInsideRegion(condition: ConditionGroup | int, region: Region | int, event_layers=()):
    """
    Calls `IfAllPlayersRegionState` with `state=True`.
    """


# (3, 7)
def IfAllPlayersOutsideRegion(condition: ConditionGroup | int, region: Region | int, event_layers=()):
    """
    Calls `IfAllPlayersRegionState` with `state=False`.
    """


# (3, 8)
def IfMapPresenceState(
    condition: ConditionGroup | int,
    state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Conditions upon player's presence in a particular game map.
    """


# (3, 8)
def IfInsideMap(condition: ConditionGroup | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `IfMapPresenceState` with `state=True`.
    """


# (3, 8)
def IfOutsideMap(condition: ConditionGroup | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `IfMapPresenceState` with `state=False`.
    """


# (3, 9)
def IfMultiplayerEvent(condition: ConditionGroup | int, event_id: int, event_layers=()):
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
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
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
    event_layers=(),
):
    """
    Calls `IfEnabledFlagCountComparison` with `comparison_type=5`.
    """


# (3, 12)
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


# (3, 12)
def IfEventValueEqual(condition: ConditionGroup | int, flag: Flag | int, bit_count: int, value: int, event_layers=()):
    """
    Calls `IfEventValueComparison` with `comparison_type=0`.
    """


# (3, 12)
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


# (3, 12)
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


# (3, 12)
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


# (3, 12)
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


# (3, 12)
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


# (3, 14)
def IfAnyItemDroppedInRegion(condition: ConditionGroup | int, region: Region | int, event_layers=()):
    """
    Check if any item has been dropped in the specified region. Not sensitive to what the item is.
    """


# (3, 15)
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


# (3, 16)
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


# (3, 17)
def IfNewGameCycleComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    completion_count: int,
    event_layers=(),
):
    """
    TODO
    """


# (3, 17)
def IfNewGameCycleEqual(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=0`.
    """


# (3, 17)
def IfNewGameCycleNotEqual(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=1`.
    """


# (3, 17)
def IfNewGameCycleGreaterThan(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=2`.
    """


# (3, 17)
def IfNewGameCycleLessThan(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=3`.
    """


# (3, 17)
def IfNewGameCycleGreaterThanOrEqual(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=4`.
    """


# (3, 17)
def IfNewGameCycleLessThanOrEqual(condition: ConditionGroup | int, completion_count: int, event_layers=()):
    """
    Calls `IfNewGameCycleComparison` with `comparison_type=5`.
    """


# (3, 20)
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


# (3, 22)
def IfOnlineState(condition: ConditionGroup | int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (3, 22)
def IfOnline(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfOnlineState` with `state=True`.
    """


# (3, 22)
def IfOffline(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfOnlineState` with `state=False`.
    """


# (4, 0)
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


# (4, 0)
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


# (4, 0)
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


# (4, 2)
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


# (4, 2)
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


# (4, 2)
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


# (4, 2)
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


# (4, 2)
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


# (4, 2)
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


# (4, 2)
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


# (4, 3)
def IfCharacterIsType(
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


# (4, 4)
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


# (4, 4)
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


# (4, 4)
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


# (4, 5)
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


# (4, 5)
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


# (4, 5)
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


# (4, 5)
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


# (4, 5)
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


# (4, 6)
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


# (4, 6)
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


# (4, 7)
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


# (4, 7)
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


# (4, 7)
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


# (4, 8)
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


# (4, 8)
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


# (4, 8)
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


# (4, 9)
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


# (4, 11)
def IfPlayerClass(condition: ConditionGroup | int, class_type: ClassType | int, event_layers=()):
    """
    TODO
    """


# (4, 12)
def IfPlayerCovenant(condition: ConditionGroup | int, covenant: int, event_layers=()):
    """
    TODO
    """


# (4, 13)
def IfPlayerLevelComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    TODO
    """


# (4, 13)
def IfPlayerLevelEqual(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=0`.
    """


# (4, 13)
def IfPlayerLevelNotEqual(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=1`.
    """


# (4, 13)
def IfPlayerLevelGreaterThan(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=2`.
    """


# (4, 13)
def IfPlayerLevelLessThan(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=3`.
    """


# (4, 13)
def IfPlayerLevelGreaterThanOrEqual(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=4`.
    """


# (4, 13)
def IfPlayerLevelLessThanOrEqual(condition: ConditionGroup | int, value: int, event_layers=()):
    """
    Calls `IfPlayerLevelComparison` with `comparison_type=5`.
    """


# (4, 14)
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


# (4, 14)
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


# (4, 14)
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


# (4, 14)
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


# (4, 14)
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


# (4, 14)
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


# (4, 14)
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


# (5, 0)
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


# (5, 0)
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


# (5, 0)
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


# (5, 1)
def IfAssetDamaged(condition: ConditionGroup | int, asset: Asset | int, attacker: Character | int, event_layers=()):
    """
    TODO
    """


# (5, 2)
def IfAssetActivated(condition: ConditionGroup | int, obj_act_id: int, event_layers=()):
    """
    TODO
    """


# (5, 3)
def IfAssetHealthValueComparison(
    condition: ConditionGroup | int,
    asset: Asset | int,
    comparison_type: ComparisonType | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    TODO
    """


# (5, 3)
def IfAssetHealthValueEqual(
    condition: ConditionGroup | int,
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=0`.
    """


# (5, 3)
def IfAssetHealthValueNotEqual(
    condition: ConditionGroup | int,
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=1`.
    """


# (5, 3)
def IfAssetHealthValueGreaterThan(
    condition: ConditionGroup | int,
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=2`.
    """


# (5, 3)
def IfAssetHealthValueLessThan(
    condition: ConditionGroup | int,
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=3`.
    """


# (5, 3)
def IfAssetHealthValueGreaterThanOrEqual(
    condition: ConditionGroup | int,
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=4`.
    """


# (5, 3)
def IfAssetHealthValueLessThanOrEqual(
    condition: ConditionGroup | int,
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `IfAssetHealthValueComparison` with `comparison_type=5`.
    """


# (11, 0)
def IfPlayerMovingOnCollision(condition: ConditionGroup | int, collision: Collision | int, event_layers=()):
    """
    TODO
    """


# (11, 1)
def IfPlayerRunningOnCollision(condition: ConditionGroup | int, collision: Collision | int, event_layers=()):
    """
    TODO
    """


# (11, 2)
def IfPlayerStandingOnCollision(condition: ConditionGroup | int, collision: Collision | int, event_layers=()):
    """
    TODO
    """


# (1000, 0)
def AwaitConditionState(state: bool | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Not sure if this is ever really used over `IfConditionState`.
    """


# (1000, 0)
def AwaitConditionTrue(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `AwaitConditionState` with `state=True`.
    """


# (1000, 0)
def AwaitConditionFalse(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `AwaitConditionState` with `state=False`.
    """


# (1000, 1)
def SkipLinesIfConditionState(
    line_count: int,
    state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    TODO
    """


# (1000, 1)
def SkipLinesIfConditionTrue(line_count: int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `SkipLinesIfConditionState` with `state=True`.
    """


# (1000, 1)
def SkipLinesIfConditionFalse(line_count: int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `SkipLinesIfConditionState` with `state=False`.
    """


# (1000, 2)
def ReturnIfConditionState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    TODO
    """


# (1000, 2)
def EndIfConditionTrue(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfConditionState` with `event_return_type=0`, `state=True`.
    """


# (1000, 2)
def EndIfConditionFalse(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfConditionState` with `event_return_type=0`, `state=False`.
    """


# (1000, 2)
def RestartIfConditionTrue(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfConditionState` with `event_return_type=1`, `state=True`.
    """


# (1000, 2)
def RestartIfConditionFalse(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfConditionState` with `event_return_type=1`, `state=False`.
    """


# (1000, 3)
def SkipLines(line_count: int, event_layers=()):
    """
    Unconditional line skip.
    """


# (1000, 4)
def Return(event_return_type: EventReturnType | int, event_layers=()):
    """
    TODO
    """


# (1000, 4)
def End(event_layers=()):
    """
    Calls `Return` with `event_return_type=0`.
    """


# (1000, 4)
def Restart(event_layers=()):
    """
    Calls `Return` with `event_return_type=1`.
    """


# (1000, 5)
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


# (1000, 5)
def SkipLinesIfValueEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=0`.
    """


# (1000, 5)
def SkipLinesIfValueNotEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=1`.
    """


# (1000, 5)
def SkipLinesIfValueGreaterThan(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=2`.
    """


# (1000, 5)
def SkipLinesIfValueLessThan(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=3`.
    """


# (1000, 5)
def SkipLinesIfValueGreaterThanOrEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=4`.
    """


# (1000, 5)
def SkipLinesIfValueLessThanOrEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfValueComparison` with `comparison_type=5`.
    """


# (1000, 6)
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


# (1000, 6)
def EndIfValueEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=0`.
    """


# (1000, 6)
def EndIfValueNotEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=1`.
    """


# (1000, 6)
def EndIfValueGreaterThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=2`.
    """


# (1000, 6)
def EndIfValueLessThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=3`.
    """


# (1000, 6)
def EndIfValueGreaterThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=4`.
    """


# (1000, 6)
def EndIfValueLessThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=0`, `comparison_type=5`.
    """


# (1000, 6)
def RestartIfValueEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=0`.
    """


# (1000, 6)
def RestartIfValueNotEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=1`.
    """


# (1000, 6)
def RestartIfValueGreaterThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=2`.
    """


# (1000, 6)
def RestartIfValueLessThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=3`.
    """


# (1000, 6)
def RestartIfValueGreaterThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=4`.
    """


# (1000, 6)
def RestartIfValueLessThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfValueComparison` with `event_return_type=1`, `comparison_type=5`.
    """


# (1000, 7)
def SkipLinesIfLastConditionResultState(
    line_count: int,
    state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    Skip some number of lines if the last result of the given condition (without re-evaluating) is `state`.
    """


# (1000, 7)
def SkipLinesIfLastConditionResultTrue(line_count: int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `SkipLinesIfLastConditionResultState` with `state=True`.
    """


# (1000, 7)
def SkipLinesIfLastConditionResultFalse(line_count: int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `SkipLinesIfLastConditionResultState` with `state=False`.
    """


# (1000, 8)
def ReturnIfLastConditionResultState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    End or restart event if last condition result (without re-evaluating) is the given `state`.
    """


# (1000, 8)
def EndIfLastConditionResultTrue(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfLastConditionResultState` with `event_return_type=0`, `state=True`.
    """


# (1000, 8)
def EndIfLastConditionResultFalse(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfLastConditionResultState` with `event_return_type=0`, `state=False`.
    """


# (1000, 8)
def RestartIfLastConditionResultTrue(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfLastConditionResultState` with `event_return_type=1`, `state=True`.
    """


# (1000, 8)
def RestartIfLastConditionResultFalse(input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `ReturnIfLastConditionResultState` with `event_return_type=1`, `state=False`.
    """


# (1001, 0)
def Wait(seconds: float, event_layers=()):
    """
    Wait for some number of seconds.
    """


# (1001, 1)
def WaitFrames(frames: int, event_layers=()):
    """
    Wait for some number of frames.
    """


# (1001, 2)
def WaitRandomSeconds(min_seconds: float, max_seconds: float, event_layers=()):
    """
    Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
    """


# (1001, 3)
def WaitRandomFrames(min_frames: int, max_frames: int, event_layers=()):
    """
    Wait for a random number of seconds between min and max. I assume the distribution is inclusive and uniform.
    """


# (1003, 0)
def AwaitFlagState(state: FlagSetting | int, flag_type: FlagType | int, flag: Flag | int, event_layers=()):
    """
    Not sure if this is really used rather than `IfFlagState` with MAIN condition (0).
    """


# (1003, 0)
def AwaitFlagEnabled(flag: Flag | int, event_layers=()):
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=0`.
    """


# (1003, 0)
def AwaitFlagDisabled(flag: Flag | int, event_layers=()):
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=0`.
    """


# (1003, 0)
def AwaitThisEventOn(event_layers=()):
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


# (1003, 0)
def AwaitThisEventOff(event_layers=()):
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


# (1003, 0)
def AwaitThisEventSlotOn(event_layers=()):
    """
    Calls `AwaitFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


# (1003, 0)
def AwaitThisEventSlotOff(event_layers=()):
    """
    Calls `AwaitFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


# (1003, 1)
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


# (1003, 1)
def SkipLinesIfFlagEnabled(line_count: int, flag: Flag | int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=0`.
    """


# (1003, 1)
def SkipLinesIfFlagDisabled(line_count: int, flag: Flag | int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=0`.
    """


# (1003, 1)
def SkipLinesIfThisEventFlagEnabled(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=1`, `flag=0`.
    """


# (1003, 1)
def SkipLinesIfThisEventFlagDisabled(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=1`, `flag=0`.
    """


# (1003, 1)
def SkipLinesIfThisEventSlotFlagEnabled(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=1`, `flag_type=2`, `flag=0`.
    """


# (1003, 1)
def SkipLinesIfThisEventSlotFlagDisabled(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfFlagState` with `state=0`, `flag_type=2`, `flag=0`.
    """


# (1003, 2)
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


# (1003, 2)
def EndIfFlagEnabled(flag: Flag | int, event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=0`.
    """


# (1003, 2)
def EndIfFlagDisabled(flag: Flag | int, event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=0`.
    """


# (1003, 2)
def EndIfThisEventFlagEnabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=1`, `flag=0`.
    """


# (1003, 2)
def EndIfThisEventFlagDisabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=1`, `flag=0`.
    """


# (1003, 2)
def EndIfThisEventSlotFlagEnabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=1`, `flag_type=2`, `flag=0`.
    """


# (1003, 2)
def EndIfThisEventSlotFlagDisabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=0`, `state=0`, `flag_type=2`, `flag=0`.
    """


# (1003, 2)
def RestartIfFlagEnabled(flag: Flag | int, event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=0`.
    """


# (1003, 2)
def RestartIfFlagDisabled(flag: Flag | int, event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=0`.
    """


# (1003, 2)
def RestartIfThisEventFlagEnabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=1`, `flag=0`.
    """


# (1003, 2)
def RestartIfThisEventFlagDisabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=1`, `flag=0`.
    """


# (1003, 2)
def RestartIfThisEventSlotFlagEnabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=1`, `flag_type=2`, `flag=0`.
    """


# (1003, 2)
def RestartIfThisEventSlotFlagDisabled(event_layers=()):
    """
    Calls `ReturnIfFlagState` with `event_return_type=1`, `state=0`, `flag_type=2`, `flag=0`.
    """


# (1003, 3)
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


# (1003, 3)
def SkipLinesIfFlagRangeAllEnabled(line_count: int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=0`, `flag_type=0`.
    """


# (1003, 3)
def SkipLinesIfFlagRangeAllDisabled(line_count: int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=1`, `flag_type=0`.
    """


# (1003, 3)
def SkipLinesIfFlagRangeAnyEnabled(line_count: int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=2`, `flag_type=0`.
    """


# (1003, 3)
def SkipLinesIfFlagRangeAnyDisabled(line_count: int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfFlagRangeState` with `state=3`, `flag_type=0`.
    """


# (1003, 4)
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


# (1003, 4)
def EndIfFlagRangeAllEnabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=0`, `flag_type=0`.
    """


# (1003, 4)
def EndIfFlagRangeAllDisabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=1`, `flag_type=0`.
    """


# (1003, 4)
def EndIfFlagRangeAnyEnabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=2`, `flag_type=0`.
    """


# (1003, 4)
def EndIfFlagRangeAnyDisabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=0`, `state=3`, `flag_type=0`.
    """


# (1003, 4)
def RestartIfFlagRangeAllEnabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=0`, `flag_type=0`.
    """


# (1003, 4)
def RestartIfFlagRangeAllDisabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=1`, `flag_type=0`.
    """


# (1003, 4)
def RestartIfFlagRangeAnyEnabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=2`, `flag_type=0`.
    """


# (1003, 4)
def RestartIfFlagRangeAnyDisabled(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `ReturnIfFlagRangeState` with `event_return_type=1`, `state=3`, `flag_type=0`.
    """


# (1003, 7)
def SkipLinesIfMapPresenceState(
    line_count: int,
    state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


# (1003, 7)
def SkipLinesIfInsideMap(line_count: int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=True`.
    """


# (1003, 7)
def SkipLinesIfOutsideMap(line_count: int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `SkipLinesIfMapPresenceState` with `state=False`.
    """


# (1003, 8)
def ReturnIfMapPresenceState(
    event_return_type: EventReturnType | int,
    state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


# (1003, 8)
def EndIfInsideMap(game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=True`.
    """


# (1003, 8)
def EndIfOutsideMap(game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=0`, `state=False`.
    """


# (1003, 8)
def RestartIfInsideMap(game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=True`.
    """


# (1003, 8)
def RestartIfOutsideMap(game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapPresenceState` with `event_return_type=1`, `state=False`.
    """


# (1005, 1)
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


# (1005, 1)
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


# (1005, 1)
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


# (1005, 2)
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


# (1005, 2)
def EndIfAssetDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfAssetDestructionState` with `event_return_type=0`, `state=True`.
    """


# (1005, 2)
def EndIfAssetNotDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfAssetDestructionState` with `event_return_type=0`, `state=False`.
    """


# (1005, 2)
def RestartIfAssetDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfAssetDestructionState` with `event_return_type=1`, `state=True`.
    """


# (1005, 2)
def RestartIfAssetNotDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `ReturnIfAssetDestructionState` with `event_return_type=1`, `state=False`.
    """


# Instruction `RunEvent` (2000, 0) is defined in the `compiler` module.


# (2000, 2)
def SetNetworkSyncState(state: bool | int, event_layers=()):
    """
    TODO
    """


# (2000, 2)
def EnableNetworkSync(event_layers=()):
    """
    Calls `SetNetworkSyncState` with `state=True`.
    """


# (2000, 2)
def DisableNetworkSync(event_layers=()):
    """
    Calls `SetNetworkSyncState` with `state=False`.
    """


# (2000, 3)
def ClearMainCondition(dummy: int = 0, event_layers=()):
    """
    Likely clears all conditions currently loaded into the main condition (0).
    """


# (2000, 5)
def SaveRequest(dummy: int = 0, event_layers=()):
    """
    Request the game to save player progress.
    """


# Instruction `RunCommonEvent` (2000, 6) is defined in the `compiler` module.


# (2000, 7)
def StartPS5Activity(activity_id: int, event_layers=()):
    """
    TODO
    """


# (2000, 8)
def EndPS5Activity(activity_id: int, event_layers=()):
    """
    TODO
    """


# (2002, 1)
def PlayCutsceneToAll(cutscene_id: int, cutscene_flags: CutsceneFlags | int, event_layers=()):
    """
    TODO
    """


# (2002, 3)
def PlayCutsceneToPlayer(cutscene_id: int, cutscene_flags: CutsceneFlags | int, player_id: int, event_layers=()):
    """
    TODO
    """


# (2002, 4)
def PlayCutsceneToPlayer_Unknown_2002_04(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    region: Region | int,
    unk_12_16: int,
    player_id: int,
    unk_20_24: int,
    event_layers=(),
):
    """
    TODO
    """


# (2002, 9)
def PlayCutsceneToPlayer_Unknown_2002_09(
    cutscene_id: int,
    cutscene_flags: CutsceneFlags | int,
    unk_8_12: int,
    unk_12_16: int,
    player_id: int,
    unk_20_24: int,
    unk_24_25: bool | int,
    unk_25_26: bool | int,
    unk_28_32: float,
    unk_33_34: bool | int,
    unk_34_35: bool | int,
    unk_35_36: bool | int,
    unk_36_37: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (2003, 3)
def SetSpawnerState(entity: Asset | Character | Region | int, state: bool | int, event_layers=()):
    """
    e.g. the baby skeletons in Tomb of the Giants.
    """


# (2003, 3)
def EnableSpawner(entity: Asset | Character | Region | int, event_layers=()):
    """
    Calls `SetSpawnerState` with `state=True`.
    """


# (2003, 3)
def DisableSpawner(entity: Asset | Character | Region | int, event_layers=()):
    """
    Calls `SetSpawnerState` with `state=False`.
    """


# (2003, 4)
def AwardItemLotToAllPlayers(item_lot: int, event_layers=()):
    """
    TODO
    """


# (2003, 5)
def ShootProjectile(
    owner_entity: Asset | Character | Region | int,
    source_entity: Asset | Character | Region | int,
    dummy_id: int,
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


# (2003, 6)
def SetMapCollisionState_2003_06(collision: Collision | int, state: bool | int, event_layers=()):
    """
    TODO: Unsure how this differs from `SetMapCollisionState`.
    """


# (2003, 6)
def EnableMapCollision_2003_06(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionState_2003_06` with `state=True`.
    """


# (2003, 6)
def DisableMapCollision_2003_06(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionState_2003_06` with `state=False`.
    """


# (2003, 7)
def SetMapVisibilityState(map_piece: MapPiece | int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (2003, 7)
def EnableMapVisibility(map_piece: MapPiece | int, event_layers=()):
    """
    Calls `SetMapVisibilityState` with `state=True`.
    """


# (2003, 7)
def DisableMapVisibility(map_piece: MapPiece | int, event_layers=()):
    """
    Calls `SetMapVisibilityState` with `state=False`.
    """


# (2003, 8)
def SetEventSlotState(event_id: int, slot: int, event_return_type: bool | int, event_layers=()):
    """
    Use to manually END or RESTART a given event ID and slot.
    """


# (2003, 8)
def EndEventSlot(event_id: int, slot: int, event_layers=()):
    """
    Calls `SetEventSlotState` with `event_return_type=0`.
    """


# (2003, 8)
def EndEvent(event_id: int, event_layers=()):
    """
    Calls `SetEventSlotState` with `slot=0`, `event_return_type=0`.
    """


# (2003, 8)
def RestartEventSlot(event_id: int, slot: int, event_layers=()):
    """
    Calls `SetEventSlotState` with `event_return_type=1`.
    """


# (2003, 8)
def RestartEvent(event_id: int, event_layers=()):
    """
    Calls `SetEventSlotState` with `slot=0`, `event_return_type=1`.
    """


# (2003, 9)
def InvertFlag(flag: Flag | int, event_layers=()):
    """
    Unclear how this differs from calling `ToggleFlag` (which calls `SetEventFlag` with `FlagSetting.Change`).
    """


# (2003, 11)
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


# (2003, 11)
def EnableBossHealthBar(character: Character | int, name: NPCName | int = 0, bar_slot: int = 0, event_layers=()):
    """
    Calls `SetBossHealthBarState` with `state=True`.
    The character's health bar will appear at the bottom of the screen, with a name.
    """


# (2003, 11)
def DisableBossHealthBar(character: Character | int, name: NPCName | int = 0, bar_slot: int = 0, event_layers=()):
    """
    Calls `SetBossHealthBarState` with `state=False`.
    
    The character's health bar will disappear from the bottom of the screen.
    
    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter,
    so only the first argument actually does anything. You're welcome to specify the name for
    clarity anyway (and vanilla events will show it when decompiled).
    """


# (2003, 12)
def KillBossAndDisplayBanner(character: Character | int, banner_type: BannerType | int, event_layers=()):
    """
    TODO
    """


# (2003, 13)
def SetNavmeshType(
    navmesh_id: NavigationEvent | int,
    navmesh_type: NavmeshType | int,
    operation: BitOperation | int,
    event_layers=(),
):
    """
    Set given navmesh type.
    """


# (2003, 13)
def EnableNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int, event_layers=()):
    """
    Calls `SetNavmeshType` with `operation=0`.
    """


# (2003, 13)
def DisableNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int, event_layers=()):
    """
    Calls `SetNavmeshType` with `operation=1`.
    """


# (2003, 13)
def ToggleNavmeshType(navmesh_id: NavigationEvent | int, navmesh_type: NavmeshType | int, event_layers=()):
    """
    Calls `SetNavmeshType` with `operation=2`.
    """


# (2003, 14)
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


# (2003, 15)
def HandleMinibossDefeat(character: Character | int, event_layers=()):
    """
    TODO
    """


# (2003, 16)
def TriggerMultiplayerEvent(event_id: int, event_layers=()):
    """
    Used to make the Bell of Awakening sounds, for example.
    """


# (2003, 17)
def SetRandomFlagInRange(flag_range: FlagRange | tuple | list, state: FlagSetting | int, event_layers=()):
    """
    Set the state of a random flag from a given range (inclusive).
    """


# (2003, 17)
def EnableRandomFlagInRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetRandomFlagInRange` with `state=1`.
    """


# (2003, 17)
def DisableRandomFlagInRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetRandomFlagInRange` with `state=0`.
    """


# (2003, 17)
def ToggleRandomFlagInRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetRandomFlagInRange` with `state=2`.
    """


# (2003, 18)
def ForceAnimation(
    entity: Asset | Character | int,
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


# (2003, 21)
def IncrementNewGameCycle(dummy: int = 0, event_layers=()):
    """
    Increase NG+ level by one.
    """


# (2003, 22)
def SetFlagRangeState(flag_range: FlagRange | tuple | list, state: FlagSetting | int, event_layers=()):
    """
    Set the state of an entire flag range (inclusive).
    """


# (2003, 22)
def EnableFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetFlagRangeState` with `state=1`.
    """


# (2003, 22)
def DisableFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetFlagRangeState` with `state=0`.
    """


# (2003, 22)
def ToggleFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetFlagRangeState` with `state=2`.
    """


# (2003, 23)
def SetRespawnPoint(respawn_point: int, event_layers=()):
    """
    Respawn point is an event set in the MSB.
    """


# (2003, 24)
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


# (2003, 24)
def RemoveWeaponFromPlayer(item: BaseItemParam | int, quantity: int = 0, event_layers=()):
    """
    Calls `RemoveItemFromPlayer` with `item_type=0`.
    """


# (2003, 24)
def RemoveArmorFromPlayer(item: BaseItemParam | int, quantity: int = 0, event_layers=()):
    """
    Calls `RemoveItemFromPlayer` with `item_type=1`.
    """


# (2003, 24)
def RemoveTalismanFromPlayer(item: BaseItemParam | int, quantity: int = 0, event_layers=()):
    """
    Calls `RemoveItemFromPlayer` with `item_type=2`.
    """


# (2003, 24)
def RemoveGoodFromPlayer(item: BaseItemParam | int, quantity: int = 0, event_layers=()):
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
    unknown: int,
    event_layers=(),
):
    """
    If you set a black summon sign, the specified NPC will try to invade automatically.
    
    New unknown argument in Elden Ring.
    """


# (2003, 26)
def SetSoapstoneMessageState(message_id: int, state: bool | int, event_layers=()):
    """
    Enable or disable developer message. Technically not a 'Soapstone' message anymore, but keeping the name.
    """


# (2003, 26)
def EnableSoapstoneMessage(message_id: int, event_layers=()):
    """
    Calls `SetSoapstoneMessageState` with `state=True`.
    """


# (2003, 26)
def DisableSoapstoneMessage(message_id: int, event_layers=()):
    """
    Calls `SetSoapstoneMessageState` with `state=False`.
    """


# (2003, 28)
def AwardAchievement(achievement_id: int, event_layers=()):
    """
    For obvious reasons, I *highly* discourage you from abusing this, except in the interest of maintaining the
    accessibility of existing achievements. This interacts with Steam, which is always dangerous.
    """


# (2003, 31)
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


# (2003, 32)
def ClearEventValue(flag: Flag | int, bit_count: int, event_layers=()):
    """
    Clears the given multi-flag. This is basically like disabling `bit_count` flags in a row, starting at
    `flag`.
    """


# (2003, 35)
def MoveRemains(source_region: Region | int, destination_region: Region | int, event_layers=()):
    """
    Move all bloodstains and dropped items from one region to another (I assume). Used to move your
    remains out of Gwyndolin's endless corridor.
    """


# (2003, 36)
def AwardItemLotToHostOnly(item_lot: int, event_layers=()):
    """
    You can simply call AwardItemLot() with the same argument, which will redirect here, as you'll almost never
    *not* want to award an item lot to the host only.
    """


# (2003, 41)
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


# (2004, 1)
def SetAIState(character: Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (2004, 1)
def EnableAI(character: Character | int, event_layers=()):
    """
    Calls `SetAIState` with `state=True`.
    """


# (2004, 1)
def DisableAI(character: Character | int, event_layers=()):
    """
    Calls `SetAIState` with `state=False`.
    """


# (2004, 2)
def SetTeamType(character: Character | int, new_team: TeamType | int, event_layers=()):
    """
    TODO
    """


# (2004, 4)
def Kill(character: Character | int, award_runes: bool | int = False, event_layers=()):
    """
    Technically a kill 'request.'
    """


# (2004, 5)
def SetCharacterState(character: Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (2004, 5)
def EnableCharacter(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterState` with `state=True`.
    """


# (2004, 5)
def DisableCharacter(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterState` with `state=False`.
    """


# (2004, 6)
def EzstateAIRequest(character: Character | int, command_id: int, command_slot: int, event_layers=()):
    """
    Slot number ranges from 0 to 3.
    """


# (2004, 7)
def CreateProjectileOwner(entity: Asset | Character | Region | int, event_layers=()):
    """
    A 'bullet owner' that will spawn things according to the Spawner section of the MSB.
    """


# (2004, 8)
def AddSpecialEffect(character: Character | int, special_effect: int, event_layers=()):
    """
    'Special effect' as in a buff/debuff, not graphical effects (though they may come with one).
    """


# (2004, 10)
def SetGravityState(character: Character | int, state: bool | int, event_layers=()):
    """
    Simply determines if the character loses height as it moves around. They will still gain height by running
    up slopes.
    """


# (2004, 10)
def EnableGravity(character: Character | int, event_layers=()):
    """
    Calls `SetGravityState` with `state=True`.
    """


# (2004, 10)
def DisableGravity(character: Character | int, event_layers=()):
    """
    Calls `SetGravityState` with `state=False`.
    """


# (2004, 11)
def SetCharacterEventTarget(character: Character | int, entity: Asset | Character | Region | int, event_layers=()):
    """
    Likely refers to patrolling behavior.
    """


# (2004, 12)
def SetImmortalityState(character: Character | int, state: bool | int, event_layers=()):
    """
    Character will take damage, but not die (i.e. cannot go below 1 HP).
    """


# (2004, 12)
def EnableImmortality(character: Character | int, event_layers=()):
    """
    Calls `SetImmortalityState` with `state=True`.
    """


# (2004, 12)
def DisableImmortality(character: Character | int, event_layers=()):
    """
    Calls `SetImmortalityState` with `state=False`.
    """


# (2004, 13)
def SetNest(character: Character | int, region: Region | int, event_layers=()):
    """
    Home point for entity AI.
    """


# (2004, 14)
def FaceEntityAndForceAnimation(
    character: Character | int,
    target_entity: Asset | Character | Region | int,
    animation: int = -1,
    wait_for_completion: bool | int = False,
    event_layers=(),
):
    """
    Rotate a character to face a target map entity of any type, then optionally force an animation.
    
    WARNING: This may crash an event script if `character` is currently disabled!
    """


# (2004, 15)
def SetInvincibilityState(character: Character | int, state: bool | int, event_layers=()):
    """
    Character cannot take damage or die.
    """


# (2004, 15)
def EnableInvincibility(character: Character | int, event_layers=()):
    """
    Calls `SetInvincibilityState` with `state=True`.
    """


# (2004, 15)
def DisableInvincibility(character: Character | int, event_layers=()):
    """
    Calls `SetInvincibilityState` with `state=False`.
    """


# (2004, 16)
def ClearTargetList(character: Character | int, event_layers=()):
    """
    Clear list of targets from character AI.
    """


# (2004, 17)
def AICommand(character: Character | int, command_id: int, command_slot: int, event_layers=()):
    """
    The given `command_id` can be accessed in AI Lua scripts with `ai:GetEventRequest(slot)`.
    """


# (2004, 18)
def SetEventPoint(character: Character | int, region: Region | int, reaction_range: float, event_layers=()):
    """
    Not sure what the usage of this is, but it is likely used to change patrol behavior.
    """


# (2004, 19)
def SetAIParamID(character: Character | int, ai_param_id: int, event_layers=()):
    """
    Change character's AI parameter index.
    """


# (2004, 20)
def ReplanAI(character: Character | int, event_layers=()):
    """
    Clear current AI goal list and force character to replan it.
    """


# (2004, 21)
def RemoveSpecialEffect(character: Character | int, special_effect: int, event_layers=()):
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
    event_layers=(),
):
    """
    Complex. Sets specific damage parameters for part of an NPC model. Further changes to the specific part can
    be made using the events below. The part is specified using the NPCPartType slot. Look at usage in tail cut
    events to understand these more.
    """


# (2004, 23)
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


# (2004, 24)
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


# (2004, 25)
def SetNPCPartBulletDamageScaling(
    character: Character | int,
    npc_part_id: int,
    desired_scaling: float,
    event_layers=(),
):
    """
    Scale the damage dealt to the part. Usually used to set damage to zero, e.g. Smough's hammer.
    """


# (2004, 26)
def SetDisplayMask(character: Character | int, bit_index: int, switch_type: OnOffChange | int, event_layers=()):
    """
    Different bits correspond to different parts of the character model. You can see the initial values for
    these in the NPC params. This is generally used to disable tails when they are cut off.
    
    `switch_type` can be 0 (off), 1 (on), or 2 (change).
    """


# (2004, 27)
def SetCollisionMask(character: Character | int, bit_index: int, switch_type: OnOffChange | int, event_layers=()):
    """
    See above. This affects the NPC's Collision, not appearance.
    """


# (2004, 28)
def SetNetworkUpdateAuthority(character: Character | int, authority_level: UpdateAuthority | int, event_layers=()):
    """
    Complex; look at existing usage. Authority level must be 'Normal' or 'Forced'.
    """


# (2004, 29)
def SetBackreadState(character: Character | int, remove: bool | int, event_layers=()):
    """
    I'm not 100% certain how this differs from the standard Enable(), but I imagine controlling the 'backread'
    of a character has a larger effect on game resources. It is used, for example, to disable the Fair Lady and
    Eingyi during the Demon Firesage boss fight.
    
    Also note reversed bool.
    """


# (2004, 29)
def EnableBackread(character: Character | int, event_layers=()):
    """
    Calls `SetBackreadState` with `remove=False`.
    """


# (2004, 29)
def DisableBackread(character: Character | int, event_layers=()):
    """
    Calls `SetBackreadState` with `remove=True`.
    """


# (2004, 30)
def SetHealthBarState(character: Character | int, state: bool | int, event_layers=()):
    """
    Normal health bar that appears above character.
    """


# (2004, 30)
def EnableHealthBar(character: Character | int, event_layers=()):
    """
    Calls `SetHealthBarState` with `state=True`.
    """


# (2004, 30)
def DisableHealthBar(character: Character | int, event_layers=()):
    """
    Calls `SetHealthBarState` with `state=False`.
    """


# (2004, 31)
def SetCharacterCollisionState(character: Character | int, state: bool | int, event_layers=()):
    """
    Note that the bool is no longer inverted, as in older games.
    """


# (2004, 31)
def EnableCharacterCollision(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterCollisionState` with `state=True`.
    """


# (2004, 31)
def DisableCharacterCollision(character: Character | int, event_layers=()):
    """
    Calls `SetCharacterCollisionState` with `state=False`.
    """


# (2004, 33)
def ReferDamageToEntity(character: Character | int, target_entity: Character | int, event_layers=()):
    """
    All damage dealt to the first character will *also* (not *only*) be dealt to the target entity. I'm not 100%
    sure if the target entity can be an Asset.
    
    Only used by the Four Kings in the vanilla game.
    """


# (2004, 34)
def SetNetworkUpdateRate(
    character: Character | int,
    is_fixed: bool | int,
    update_rate: CharacterUpdateRate | int,
    event_layers=(),
):
    """
    Not sure what 'is_fixed' does. I believe only 'Always' and 'Never' are used in the vanilla game.
    """


# (2004, 35)
def SetBackreadStateAlternate(character: Character | int, state: bool | int, event_layers=()):
    """
    I have no idea how this differs from the standard backread function above.
    """


# (2004, 37)
def DropMandatoryTreasure(character: Character | int, event_layers=()):
    """
    This will disable the character and spawn any treasure they would drop. It's possible that it only spawns
    treasure that has a 100% drop rate, hence the name, but I haven't confirmed this.
    """


# (2004, 38)
def BetrayCurrentCovenant(dummy: int = 0, event_layers=()):
    """
    Dummy argument does nothing.
    """


# (2004, 39)
def SetAnimationsState(entity: Asset | Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (2004, 39)
def EnableAnimations(entity: Asset | Character | int, event_layers=()):
    """
    Calls `SetAnimationsState` with `state=True`.
    """


# (2004, 39)
def DisableAnimations(entity: Asset | Character | int, event_layers=()):
    """
    Calls `SetAnimationsState` with `state=False`.
    """


# (2004, 40)
def MoveAndSetDrawParent(
    character: Character | int,
    destination: Asset | Character | Region | int,
    set_draw_parent: MapPart | int,
    dummy_id: int = -1,
    destination_type: CoordEntityType | int = None,
    event_layers=(),
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


# (2004, 41)
def ShortMove(
    character: Character | int,
    destination: Asset | Character | Region | int,
    dummy_id: int = -1,
    destination_type: CoordEntityType | int = None,
    event_layers=(),
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


# (2004, 42)
def MoveAndCopyDrawParent(
    character: Character | int,
    destination: Asset | Character | Region | int,
    copy_draw_parent: Asset | Character | int,
    dummy_id: int = -1,
    destination_type: CoordEntityType | int = None,
    event_layers=(),
):
    """
    TODO
    destination_type: Auto-detected from `destination` type by default.
    """


# (2004, 43)
def ResetAnimation(character: Character | int, disable_interpolation: bool | int = False, event_layers=()):
    """
    Cancels an animation. Note the inverted bool for controlling interpolation.
    """


# (2004, 47)
def EqualRecovery(event_layers=()):
    """
    Unknown effect. Only used in Battle of Stoicism, so likely useless to you.
    """


# (2005, 1)
def DestroyAsset(asset: Asset | int, request_slot: int = 1, event_layers=()):
    """
    Technically 'requests' the asset's destruction. No idea what the slot number does.
    """


# (2005, 2)
def RestoreAsset(asset: Asset | int, event_layers=()):
    """
    The opposite of destruction. Restores it to its original MSB coordinates.
    """


# (2005, 3)
def SetAssetState(asset: Asset | int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (2005, 3)
def EnableAsset(asset: Asset | int, event_layers=()):
    """
    Calls `SetAssetState` with `state=True`.
    """


# (2005, 3)
def DisableAsset(asset: Asset | int, event_layers=()):
    """
    Calls `SetAssetState` with `state=False`.
    """


# (2005, 4)
def SetTreasureState(asset: Asset | int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (2005, 4)
def EnableTreasure(asset: Asset | int, event_layers=()):
    """
    Calls `SetTreasureState` with `state=True`.
    Enables any treasure attached to this asset by MSB events.
    """


# (2005, 4)
def DisableTreasure(asset: Asset | int, event_layers=()):
    """
    Calls `SetTreasureState` with `state=False`.
    
    Disables any treasure attached to this asset by MSB events.
    
    If you want to disable treasure by default, you can do it in the MSB by changing a certain event
    value to 255.
    """


# (2005, 5)
def ActivateAsset(asset: Asset | int, obj_act_id: int, relative_index: int, event_layers=()):
    """
    Manually call a specific ObjAct event attached to this asset. I believe 'relative_index' refers to the
    points on the asset at which it can be activated (e.g. which side of a gate you are on).
    
    Note that this will 'grab' a nearby NPC and force the appropriate animation from ObjAct params, which is how
    the game gets Patches to pull the lever in the Catacombs.
    """


# (2005, 6)
def SetAssetActivation(asset: Asset | int, obj_act_id: int, state: bool | int, event_layers=()):
    """
    Sets whether the asset can be activated (1) or not activated (0).
    """


# (2005, 7)
def EndOfAnimation(asset: Asset | int, animation_id: int, event_layers=()):
    """
    Sets entity to whatever state it would have after the given animation. Used often to open doors that have
    already been opened when you reload the map, etc. I doubt it can be used with characters, but haven't
    confirmed.
    """


# (2005, 8)
def PostDestruction(asset: Asset | int, request_slot: int = 1, event_layers=()):
    """
    Sets the asset to whatever appearance it would have after being destroyed. Again, not sure what 'slot'
    does, but it's literally *always* 1 in vanilla scripts (and from my testing, the instruction doesn't work
    with `slot=0`).
    """


# (2005, 9)
def CreateHazard(
    asset_flag: Flag | int,
    asset: Asset | int,
    dummy_id: int,
    behavior_param_id: int,
    target_type: DamageTargetType | int,
    radius: float,
    life: float,
    repetition_time: float,
    event_layers=(),
):
    """
    Turn an asset into an environmental hazard. It deals damage when touched according to the NPC Behavior
    params you give it. The dummy_id determines which part of the asset is hazardous (with the given radius
    and life, relative to the time this instruction occurs).
    
    An example is the large fire in the Lower Undead Burg, or near the first Armored Tusk.
    
    'target_type' determines what the hazard can damage (Character and/or Map).
    """


# (2005, 11)
def MoveAssetToCharacter(asset: Asset | int, character: Character | int, dummy_id: int = -1, event_layers=()):
    """
    Move an asset to a character.
    """


# (2005, 12)
def RemoveAssetFlag(asset_flag: Flag | int, event_layers=()):
    """
    No idea what this does. I believe it might undo the CreateHazard instruction, at least.
    """


# (2005, 13)
def SetAssetInvulnerabilityState(asset: Asset | int, state: bool | int, event_layers=()):
    """
    1 = invulnerable.
    """


# (2005, 13)
def EnableAssetInvulnerability(asset: Asset | int, event_layers=()):
    """
    Calls `SetAssetInvulnerabilityState` with `state=True`.
    """


# (2005, 13)
def DisableAssetInvulnerability(asset: Asset | int, event_layers=()):
    """
    Calls `SetAssetInvulnerabilityState` with `state=False`.
    """


# (2005, 14)
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


# (2005, 15)
def EnableTreasureCollection(asset: Asset | int, event_layers=()):
    """
    Forces an asset to spawn its treasure, even if the treasure's ItemLot flag is already enabled.
    
    Useful if you want some treasure to reappear (after, say, taking it from the player and disabling the
    ItemLot flag) without the player needing to reload the map.
    """


# (2006, 1)
def DeleteVFX(vfx_id: VFXEvent | int, erase_root_only: bool = True, event_layers=()):
    """
    Delete visual VFX. If 'erase_root_only' is True (default), effect particles already emitted will live out
    the rest of their lifetimes (e.g. making a fog gate disappear organically). The ID is given in the MSB.
    """


# (2006, 2)
def CreateVFX(vfx_id: VFXEvent | int, event_layers=()):
    """
    Create visual VFX. The ID is given in the MSB (e.g. fog effect for boss gates and checkpoints).
    """


# (2006, 3)
def CreateTemporaryVFX(
    vfx_id: int,
    anchor_entity: Asset | Character | Region | int,
    dummy_id: int = -1,
    anchor_type: CoordEntityType | int = None,
    event_layers=(),
):
    """
    Create one-off visual VFX (an FFX ID) attached to the given 'anchor_entity'. The VFX, of course, must be
    currently loaded (or in common effects).
    
    anchor_type: Auto-detected from `anchor_entity` type by default. Sets `Character` type for `PLAYER`.
    """


# (2006, 4)
def CreateAssetVFX(asset: Asset | int, dummy_id: int, vfx_id: int, event_layers=()):
    """
    TODO
    """


# (2006, 5)
def DeleteAssetVFX(asset: Asset | int, erase_root: bool = True, event_layers=()):
    """
    Note `erase_root` vs. `erase_root_only` for map SFX.
    """


# (2007, 1)
def DisplayDialog(
    text: EventText | int,
    anchor_entity: Asset | Character | Region | int = 0,
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


# (2007, 2)
def DisplayBanner(banner_type: BannerType | int, event_layers=()):
    """
    Display a pre-rendered banner. You'll have to change the textures (in menu_local.tpf) to change them.
    """


# (2007, 3)
def DisplayStatus(text: EventText | int, pad_enabled: bool = True, event_layers=()):
    """
    Displays a large message that appears at the top of the screen, such as the message that tells you how to
    remove your curse, or that the golden fog gates block your path. If 'pad_enabled' is False, you can't get
    rid of the message until it times out on its own.
    """


# (2007, 4)
def DisplayFlashingMessage(text: EventText | int, event_layers=()):
    """
    Displays a flashing messages at the bottom of the screen that does not block player input.
    """


# (2007, 9)
def DisplayFullScreenMessage(text: EventText | int, event_layers=()):
    """
    TODO
    """


# (2008, 1)
def ChangeCamera(normal_camera_id: int, locked_camera_id: int, event_layers=()):
    """
    TODO
    """


# (2008, 2)
def SetCameraVibration(
    vibration_id: int,
    anchor_entity: Asset | Character | Region | int,
    dummy_id: int = -1,
    decay_start_distance: float = 999.0,
    decay_end_distance: float = 999.0,
    anchor_type: CoordEntityType | int = None,
    event_layers=(),
):
    """
    TODO
    anchor_type: Auto-detected from `anchor_entity` type by default.
    """


# (2008, 3)
def SetLockedCameraSlot(area_id: int, block_id: int, camera_slot: int, event_layers=()):
    """
    Switch between one of two camera slots associated with the player's current collision in the MSB.
    
    Applies to area and block, not specific map CC/DD values.
    """


# (2009, 0)
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


# (2009, 3)
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


# (2009, 4)
def ActivateMultiplayerBuffs(character: Character | int, event_layers=()):
    """
    Used to strengthen bosses based on the number of summons you have. Not sure if it works for every NPC. It
    could also be tied to certain special effects; haven't checked that yet.
    """


# (2009, 6)
def NotifyBossBattleStart(dummy: int = 0, event_layers=()):
    """
    Sends the message to all summons that the host has challenged the boss.
    """


# (2010, 2)
def PlaySoundEffect(
    anchor_entity: Asset | Character | Region | int,
    sound_id: int,
    sound_type: SoundType | int = None,
    event_layers=(),
):
    """
    Anchor entity determines sound position and the sound type is used to look up the source.
    """


# (2011, 1)
def SetMapCollisionState(collision: Collision | int, state: bool | int, event_layers=()):
    """
    Enable or disable a map collision (HKX). The ID is specified in the MSB. Note that a Collision doesn't have
    to be solid ground, but could be anything triggered by collision, such as a kill plane (which this is often
    used to disable).
    """


# (2011, 1)
def EnableMapCollision(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionState` with `state=True`.
    """


# (2011, 1)
def DisableMapCollision(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionState` with `state=False`.
    """


# (2011, 2)
def SetMapCollisionBackreadMaskState(collision: Collision | int, state: bool | int, event_layers=()):
    """
    Unused.
    """


# (2011, 2)
def EnableMapCollisionBackreadMask(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionBackreadMaskState` with `state=True`.
    """


# (2011, 2)
def DisableMapCollisionBackreadMask(collision: Collision | int, event_layers=()):
    """
    Calls `SetMapCollisionBackreadMaskState` with `state=False`.
    """


# (2012, 1)
def SetMapPieceState(map_piece_id: MapPiece | int, state: bool | int, event_layers=()):
    """
    Set the visibility of individual map pieces (e.g. all the crystals in Seath's tower).
    """


# (2012, 1)
def EnableMapPiece(map_piece_id: MapPiece | int, event_layers=()):
    """
    Calls `SetMapPieceState` with `state=True`.
    """


# (2012, 1)
def DisableMapPiece(map_piece_id: MapPiece | int, event_layers=()):
    """
    Calls `SetMapPieceState` with `state=False`.
    """


# (0, 2)
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


# (0, 2)
def IfUnsignedEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=0`.
    """


# (0, 2)
def IfUnsignedNotEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=1`.
    """


# (0, 2)
def IfUnsignedGreaterThan(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=2`.
    """


# (0, 2)
def IfUnsignedLessThan(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=3`.
    """


# (0, 2)
def IfUnsignedGreaterThanOrEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=4`.
    """


# (0, 2)
def IfUnsignedLessThanOrEqual(condition: ConditionGroup | int, left: int, right: int, event_layers=()):
    """
    Calls `IfUnsignedComparison` with `comparison_type=5`.
    """


# (3, 23)
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


# (3, 24)
def IfActionButtonParamActivated(
    condition: ConditionGroup | int,
    action_button_id: int,
    entity: Asset | Character | Region | int,
    event_layers=(),
):
    """
    TODO
    """


# (3, 26)
def IfPlayerOwnWorldState(condition: ConditionGroup | int, not_in_own_world: bool | int, event_layers=()):
    """
    Excluding Arena.
    """


# (3, 26)
def IfPlayerInOwnWorld(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfPlayerOwnWorldState` with `not_in_own_world=False`.
    """


# (3, 26)
def IfPlayerNotInOwnWorld(condition: ConditionGroup | int, event_layers=()):
    """
    Calls `IfPlayerOwnWorldState` with `not_in_own_world=True`.
    """


# (3, 30)
def IfMapLoaded(condition: ConditionGroup | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Only used in Radahn fight, I believe, with map tiles.
    """


# (3, 31)
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


# (3, 32)
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


# (3, 32)
def IfMapHasUpdatePermission(
    condition: ConditionGroup | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `IfMapUpdatePermissionState` with `state=True`.
    """


# (3, 32)
def IfMapDoesNotHaveUpdatePermission(
    condition: ConditionGroup | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `IfMapUpdatePermissionState` with `state=False`.
    """


# (3, 33)
def IfFieldBattleMusicState(condition: ConditionGroup | int, npc_threat_level: int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (3, 33)
def IfFieldBattleMusicEnabled(condition: ConditionGroup | int, npc_threat_level: int, event_layers=()):
    """
    Calls `IfFieldBattleMusicState` with `state=True`.
    """


# (3, 33)
def IfFieldBattleMusicDisabled(condition: ConditionGroup | int, npc_threat_level: int, event_layers=()):
    """
    Calls `IfFieldBattleMusicState` with `state=False`.
    """


# (3, 34)
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


# (3, 34)
def IfPlayerHasHeadArmorEquipped(
    condition: ConditionGroup | int,
    armor: ArmorParam | int,
    unk_8_12: int = -1,
    event_layers=(),
):
    """
    Calls `IfPlayerHasArmorEquipped` with `armor_type=0`.
    """


# (3, 34)
def IfPlayerHasBodyArmorEquipped(
    condition: ConditionGroup | int,
    armor: ArmorParam | int,
    unk_8_12: int = -1,
    event_layers=(),
):
    """
    Calls `IfPlayerHasArmorEquipped` with `armor_type=1`.
    """


# (3, 34)
def IfPlayerHasArmsArmorEquipped(
    condition: ConditionGroup | int,
    armor: ArmorParam | int,
    unk_8_12: int = -1,
    event_layers=(),
):
    """
    Calls `IfPlayerHasArmorEquipped` with `armor_type=2`.
    """


# (3, 34)
def IfPlayerHasLegsArmorEquipped(
    condition: ConditionGroup | int,
    armor: ArmorParam | int,
    unk_8_12: int = -1,
    event_layers=(),
):
    """
    Calls `IfPlayerHasArmorEquipped` with `armor_type=3`.
    """


# (3, 35)
def IfCeremonyState(condition: ConditionGroup | int, state: bool | int, ceremony: int, event_layers=()):
    """
    TODO
    """


# (3, 35)
def IfCeremonyActive(condition: ConditionGroup | int, ceremony: int, event_layers=()):
    """
    Calls `IfCeremonyState` with `state=True`.
    """


# (3, 35)
def IfCeremonyInactive(condition: ConditionGroup | int, ceremony: int, event_layers=()):
    """
    Calls `IfCeremonyState` with `state=False`.
    """


# (3, 37)
def IfWeatherLotState(condition: ConditionGroup | int, weather_lot_param_id: int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (3, 37)
def IfWeatherLotActive(condition: ConditionGroup | int, weather_lot_param_id: int, event_layers=()):
    """
    Calls `IfWeatherLotState` with `state=True`.
    """


# (3, 37)
def IfWeatherLotInactive(condition: ConditionGroup | int, weather_lot_param_id: int, event_layers=()):
    """
    Calls `IfWeatherLotState` with `state=False`.
    """


# (3, 38)
def IfPlayerGender(condition: ConditionGroup | int, gender: Gender | int, event_layers=()):
    """
    TODO
    """


# (3, 39)
def IfArenaMatchReadyState(condition: ConditionGroup | int, ready: bool | int, event_layers=()):
    """
    TODO
    """


# (3, 40)
def IfArenaSoloResult(condition: ConditionGroup | int, result: ArenaResult | int, event_layers=()):
    """
    TODO
    """


# (3, 41)
def IfArenaSoloScoreComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    score: int,
    event_layers=(),
):
    """
    TODO
    """


# (3, 42)
def IfArenaTeamResults(condition: ConditionGroup | int, result: ArenaResult | int, event_layers=()):
    """
    TODO
    """


# (3, 43)
def IfArenaTeamScoreComparison(
    condition: ConditionGroup | int,
    comparison_type: ComparisonType | int,
    score: int,
    event_layers=(),
):
    """
    TODO
    """


# (3, 44)
def IfArenaMatchType(
    condition: ConditionGroup | int,
    match_type: ArenaMatchType | int,
    has_spirit_summon: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (3, 45)
def IfPlayerRespawnedInArena(condition: ConditionGroup | int, event_layers=()):
    """
    TODO
    """


# (4, 15)
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


# (4, 15)
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


# (4, 15)
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


# (4, 19)
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


# (4, 19)
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


# (4, 19)
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


# (4, 28)
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


# (4, 30)
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


# (4, 31)
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


# (4, 32)
def IfCharacterMountState(
    condition: ConditionGroup | int,
    character: Character | int,
    is_mounted: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (4, 32)
def IfCharacterMounted(condition: ConditionGroup | int, character: Character | int, event_layers=()):
    """
    Calls `IfCharacterMountState` with `is_mounted=True`.
    """


# (4, 32)
def IfCharacterNotMounted(condition: ConditionGroup | int, character: Character | int, event_layers=()):
    """
    Calls `IfCharacterMountState` with `is_mounted=False`.
    """


# (4, 34)
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


# (4, 34)
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


# (4, 34)
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


# (4, 35)
def IfSpecialStandbyEndedFlagState(
    condition: ConditionGroup | int,
    character: Character | int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (4, 35)
def IfSpecialStandbyEndedFlagEnabled(condition: ConditionGroup | int, character: Character | int, event_layers=()):
    """
    Calls `IfSpecialStandbyEndedFlagState` with `state=True`.
    """


# (4, 35)
def IfSpecialStandbyEndedFlagDisabled(condition: ConditionGroup | int, character: Character | int, event_layers=()):
    """
    Calls `IfSpecialStandbyEndedFlagState` with `state=False`.
    """


# (5, 6)
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


# (5, 10)
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


# (5, 10)
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


# (5, 10)
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


# (1000, 10)
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


# (1000, 10)
def SkipLinesIfUnsignedEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=0`.
    """


# (1000, 10)
def SkipLinesIfUnsignedNotEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=1`.
    """


# (1000, 10)
def SkipLinesIfUnsignedGreaterThan(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=2`.
    """


# (1000, 10)
def SkipLinesIfUnsignedLessThan(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=3`.
    """


# (1000, 10)
def SkipLinesIfUnsignedGreaterThanOrEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=4`.
    """


# (1000, 10)
def SkipLinesIfUnsignedLessThanOrEqual(line_count: int, left: int, right: int, event_layers=()):
    """
    Calls `SkipLinesIfUnsignedComparison` with `comparison_type=5`.
    """


# (1000, 11)
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


# (1000, 11)
def EndIfUnsignedEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=0`.
    """


# (1000, 11)
def EndIfUnsignedNotEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=1`.
    """


# (1000, 11)
def EndIfUnsignedGreaterThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=2`.
    """


# (1000, 11)
def EndIfUnsignedLessThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=3`.
    """


# (1000, 11)
def EndIfUnsignedGreaterThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=4`.
    """


# (1000, 11)
def EndIfUnsignedLessThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=0`, `comparison_type=5`.
    """


# (1000, 11)
def RestartIfUnsignedEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=0`.
    """


# (1000, 11)
def RestartIfUnsignedNotEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=1`.
    """


# (1000, 11)
def RestartIfUnsignedGreaterThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=2`.
    """


# (1000, 11)
def RestartIfUnsignedLessThan(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=3`.
    """


# (1000, 11)
def RestartIfUnsignedGreaterThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=4`.
    """


# (1000, 11)
def RestartIfUnsignedLessThanOrEqual(left: int, right: int, event_layers=()):
    """
    Calls `ReturnIfUnsignedComparison` with `event_return_type=1`, `comparison_type=5`.
    """


# (1000, 101)
def GotoIfConditionState(
    label: Label | int,
    required_state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    TODO
    """


# (1000, 101)
def GotoIfConditionTrue(label: Label | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `GotoIfConditionState` with `required_state=True`.
    """


# (1000, 101)
def GotoIfConditionFalse(label: Label | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `GotoIfConditionState` with `required_state=False`.
    """


# (1000, 103)
def Goto(label: Label | int, event_layers=()):
    """
    Unconditional GOTO.
    """


# (1000, 105)
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


# (1000, 107)
def GotoIfLastConditionResultState(
    label: Label | int,
    required_state: bool | int,
    input_condition: ConditionGroup | int,
    event_layers=(),
):
    """
    Go to label if the last result of the given condition (without re-evaluating) is `required_state`.
    """


# (1000, 107)
def GotoIfLastConditionResultTrue(label: Label | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `GotoIfLastConditionResultState` with `required_state=True`.
    """


# (1000, 107)
def GotoIfLastConditionResultFalse(label: Label | int, input_condition: ConditionGroup | int, event_layers=()):
    """
    Calls `GotoIfLastConditionResultState` with `required_state=False`.
    """


# (1000, 108)
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


# (1000, 108)
def GotoIfUnsignedEqual(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=0`.
    """


# (1000, 108)
def GotoIfUnsignedNotEqual(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=1`.
    """


# (1000, 108)
def GotoIfUnsignedGreaterThan(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=2`.
    """


# (1000, 108)
def GotoIfUnsignedLessThan(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=3`.
    """


# (1000, 108)
def GotoIfUnsignedGreaterThanOrEqual(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=4`.
    """


# (1000, 108)
def GotoIfUnsignedLessThanOrEqual(label: Label | int, left: int, right: int, event_layers=()):
    """
    Calls `GotoIfUnsignedComparison` with `comparison_type=5`.
    """


# (1001, 5)
def WaitUntilTimeOfDayInRange(earliest: tuple, latest: tuple, event_layers=()):
    """
    Pause event script until time of day is between the given earliest/latest times.
    """


# (1001, 6)
def WaitRealFrames(frames: int, event_layers=()):
    """
    Wait a given number of real frames. Always used after cutscene instructions with argument `frames=1`.
    """


# (1001, 8)
def WaitUntilArenaHalfTime(match_type: ArenaMatchType | int, is_second_half: bool | int, event_layers=()):
    """
    TODO
    """


# (1003, 5)
def SkipLinesIfMultiplayerState(line_count: int, state: MultiplayerState | int, event_layers=()):
    """
    TODO
    """


# (1003, 5)
def SkipLinesIfHost(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=0`.
    """


# (1003, 5)
def SkipLinesIfClient(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=1`.
    """


# (1003, 5)
def SkipLinesIfMultiplayer(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=2`.
    """


# (1003, 5)
def SkipLinesIfMultiplayerPending(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=3`.
    """


# (1003, 5)
def SkipLinesIfSingleplayer(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=4`.
    """


# (1003, 5)
def SkipLinesIfInvasion(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=5`.
    """


# (1003, 5)
def SkipLinesIfInvasionPending(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfMultiplayerState` with `state=6`.
    """


# (1003, 6)
def ReturnIfMultiplayerState(event_return_type: EventReturnType | int, state: MultiplayerState | int, event_layers=()):
    """
    TODO
    """


# (1003, 6)
def EndIfHost(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=0`.
    """


# (1003, 6)
def EndIfClient(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=1`.
    """


# (1003, 6)
def EndIfMultiplayer(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=2`.
    """


# (1003, 6)
def EndIfMultiplayerPending(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=3`.
    """


# (1003, 6)
def EndIfSingleplayer(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=4`.
    """


# (1003, 6)
def EndIfInvasion(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=5`.
    """


# (1003, 6)
def EndIfInvasionPending(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=0`, `state=6`.
    """


# (1003, 6)
def RestartIfHost(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=0`.
    """


# (1003, 6)
def RestartIfClient(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=1`.
    """


# (1003, 6)
def RestartIfMultiplayer(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=2`.
    """


# (1003, 6)
def RestartIfMultiplayerPending(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=3`.
    """


# (1003, 6)
def RestartIfSingleplayer(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=4`.
    """


# (1003, 6)
def RestartIfInvasion(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=5`.
    """


# (1003, 6)
def RestartIfInvasionPending(event_layers=()):
    """
    Calls `ReturnIfMultiplayerState` with `event_return_type=1`, `state=6`.
    """


# (1003, 9)
def SkipLinesIfCoopClientCountComparison(
    skip_lines: int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    Value should be from 0 to 4.
    """


# (1003, 10)
def ReturnIfCoopClientCountComparison(
    event_return_type: EventReturnType | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    TODO
    """


# (1003, 10)
def EndIfCoopClientCountComparison(comparison_type: ComparisonType | int, value: int, event_layers=()):
    """
    Calls `ReturnIfCoopClientCountComparison` with `event_return_type=0`.
    """


# (1003, 10)
def RestartIfCoopClientCountComparison(comparison_type: ComparisonType | int, value: int, event_layers=()):
    """
    Calls `ReturnIfCoopClientCountComparison` with `event_return_type=1`.
    """


# (1003, 12)
def SkipLinesIfPlayerOwnWorldState(line_count: int, not_in_own_world: bool | int, event_layers=()):
    """
    TODO
    """


# (1003, 12)
def SkipLinesIfPlayerInOwnWorld(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfPlayerOwnWorldState` with `not_in_own_world=False`.
    """


# (1003, 12)
def SkipLinesIfPlayerNotInOwnWorld(line_count: int, event_layers=()):
    """
    Calls `SkipLinesIfPlayerOwnWorldState` with `not_in_own_world=True`.
    """


# (1003, 13)
def GotoIfPlayerOwnWorldState(label: Label | int, not_in_own_world: bool | int, event_layers=()):
    """
    TODO
    """


# (1003, 13)
def GotoIfPlayerInOwnWorld(label: Label | int, event_layers=()):
    """
    Calls `GotoIfPlayerOwnWorldState` with `not_in_own_world=False`.
    """


# (1003, 13)
def GotoIfPlayerNotInOwnWorld(label: Label | int, event_layers=()):
    """
    Calls `GotoIfPlayerOwnWorldState` with `not_in_own_world=True`.
    """


# (1003, 14)
def ReturnIfPlayerOwnWorldState(
    event_return_type: EventReturnType | int,
    not_in_own_world: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (1003, 14)
def EndIfPlayerInOwnWorld(event_layers=()):
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=0`, `not_in_own_world=False`.
    """


# (1003, 14)
def EndIfPlayerNotInOwnWorld(event_layers=()):
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=0`, `not_in_own_world=True`.
    """


# (1003, 14)
def RestartIfPlayerInOwnWorld(event_layers=()):
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=1`, `not_in_own_world=False`.
    """


# (1003, 14)
def RestartIfPlayerNotInOwnWorld(event_layers=()):
    """
    Calls `ReturnIfPlayerOwnWorldState` with `event_return_type=1`, `not_in_own_world=True`.
    """


# (1003, 101)
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


# (1003, 101)
def GotoIfThisEventFlagEnabled(label: Label | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=1`, `flag=0`.
    """


# (1003, 101)
def GotoIfThisEventFlagDisabled(label: Label | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=1`, `flag=0`.
    """


# (1003, 101)
def GotoIfThisEventSlotFlagEnabled(label: Label | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=2`, `flag=0`.
    """


# (1003, 101)
def GotoIfThisEventSlotFlagDisabled(label: Label | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=2`, `flag=0`.
    """


# (1003, 101)
def GotoIfFlagEnabled(label: Label | int, flag: Flag | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=True`, `flag_type=0`.
    """


# (1003, 101)
def GotoIfFlagDisabled(label: Label | int, flag: Flag | int, event_layers=()):
    """
    Calls `GotoIfFlagState` with `state=False`, `flag_type=0`.
    """


# (1003, 103)
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


# (1003, 103)
def GotoIfFlagRangeAllEnabled(label: Label | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `GotoIfFlagRangeState` with `state=0`, `flag_type=0`.
    """


# (1003, 103)
def GotoIfFlagRangeAllDisabled(label: Label | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `GotoIfFlagRangeState` with `state=1`, `flag_type=0`.
    """


# (1003, 103)
def GotoIfFlagRangeAnyEnabled(label: Label | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `GotoIfFlagRangeState` with `state=2`, `flag_type=0`.
    """


# (1003, 103)
def GotoIfFlagRangeAnyDisabled(label: Label | int, flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `GotoIfFlagRangeState` with `state=3`, `flag_type=0`.
    """


# (1003, 105)
def GotoIfMultiplayerState(label: Label | int, state: MultiplayerState | int, event_layers=()):
    """
    TODO
    """


# (1003, 105)
def GotoIfHost(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=0`.
    """


# (1003, 105)
def GotoIfClient(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=1`.
    """


# (1003, 105)
def GotoIfMultiplayer(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=2`.
    """


# (1003, 105)
def GotoIfMultiplayerPending(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=3`.
    """


# (1003, 105)
def GotoIfSingleplayer(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=4`.
    """


# (1003, 105)
def GotoIfInvasion(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=5`.
    """


# (1003, 105)
def GotoIfInvasionPending(label: Label | int, event_layers=()):
    """
    Calls `GotoIfMultiplayerState` with `state=6`.
    """


# (1003, 107)
def GotoIfMapPresenceState(
    label: Label | int,
    state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    TODO
    """


# (1003, 107)
def GotoIfInsideMap(label: Label | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `GotoIfMapPresenceState` with `state=True`.
    """


# (1003, 107)
def GotoIfOutsideMap(label: Label | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `GotoIfMapPresenceState` with `state=False`.
    """


# (1003, 109)
def GotoIfCoopClientCountComparison(
    label: Label | int,
    comparison_type: ComparisonType | int,
    value: int,
    event_layers=(),
):
    """
    TODO
    """


# (1003, 200)
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


# (1003, 200)
def GotoIfPlayerInsideRegion(label: Label | int, region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `GotoIfCharacterRegionState` with `character=10000`, `state=True`.
    """


# (1003, 200)
def GotoIfPlayerOutsideRegion(label: Label | int, region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `GotoIfCharacterRegionState` with `character=10000`, `state=False`.
    """


# (1003, 200)
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


# (1003, 200)
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


# (1003, 201)
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


# (1003, 201)
def EndIfPlayerInsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `character=10000`, `state=True`.
    """


# (1003, 201)
def EndIfPlayerOutsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `character=10000`, `state=False`.
    """


# (1003, 201)
def RestartIfPlayerInsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `character=10000`, `state=True`.
    """


# (1003, 201)
def RestartIfPlayerOutsideRegion(region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `character=10000`, `state=False`.
    """


# (1003, 201)
def EndIfCharacterInsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `state=True`.
    """


# (1003, 201)
def EndIfCharacterOutsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=0`, `state=False`.
    """


# (1003, 201)
def RestartIfCharacterInsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `state=True`.
    """


# (1003, 201)
def RestartIfCharacterOutsideRegion(
    character: Character | int,
    region: Region | int,
    min_target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterRegionState` with `event_return_type=1`, `state=False`.
    """


# (1003, 202)
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


# (1003, 202)
def SkipLinesIfPlayerInsideRegion(line_count: int, region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=True`, `character=10000`.
    """


# (1003, 202)
def SkipLinesIfPlayerOutsideRegion(line_count: int, region: Region | int, min_target_count: int = 1, event_layers=()):
    """
    Calls `SkipLinesIfCharacterRegionState` with `state=False`, `character=10000`.
    """


# (1003, 202)
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


# (1003, 202)
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


# (1003, 203)
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


# (1003, 203)
def SkipLinesIfMapHasUpdatePermission(
    line_count: int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `SkipLinesIfMapUpdatePermissionState` with `state=True`.
    """


# (1003, 203)
def SkipLinesIfMapDoesNotHaveUpdatePermission(
    line_count: int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `SkipLinesIfMapUpdatePermissionState` with `state=False`.
    """


# (1003, 204)
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


# (1003, 204)
def GotoIfMapHasUpdatePermission(
    label: Label | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `GotoIfMapUpdatePermissionState` with `state=True`.
    """


# (1003, 204)
def GotoIfMapDoesNotHaveUpdatePermission(
    label: Label | int,
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `GotoIfMapUpdatePermissionState` with `state=False`.
    """


# (1003, 205)
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


# (1003, 205)
def EndIfMapHasUpdatePermission(unk_state: bool | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapUpdatePermissionState` with `event_return_type=0`, `state=True`.
    """


# (1003, 205)
def EndIfMapDoesNotHaveUpdatePermission(unk_state: bool | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapUpdatePermissionState` with `event_return_type=0`, `state=False`.
    """


# (1003, 205)
def RestartIfMapHasUpdatePermission(unk_state: bool | int, game_map: Map | MapTile | tuple | list, event_layers=()):
    """
    Calls `ReturnIfMapUpdatePermissionState` with `event_return_type=1`, `state=True`.
    """


# (1003, 205)
def RestartIfMapDoesNotHaveUpdatePermission(
    unk_state: bool | int,
    game_map: Map | MapTile | tuple | list,
    event_layers=(),
):
    """
    Calls `ReturnIfMapUpdatePermissionState` with `event_return_type=1`, `state=False`.
    """


# (1003, 206)
def SkipLinesIfCeremonyState(line_count: int, state: bool | int, ceremony: int, event_layers=()):
    """
    TODO
    """


# (1003, 206)
def SkipLinesIfCeremonyActive(line_count: int, ceremony: int, event_layers=()):
    """
    Calls `SkipLinesIfCeremonyState` with `state=True`.
    """


# (1003, 206)
def SkipLinesIfCeremonyInactive(line_count: int, ceremony: int, event_layers=()):
    """
    Calls `SkipLinesIfCeremonyState` with `state=False`.
    """


# (1003, 207)
def GotoIfCeremonyState(label: Label | int, state: bool | int, ceremony: int, event_layers=()):
    """
    TODO
    """


# (1003, 207)
def GotoIfCeremonyActive(label: Label | int, ceremony: int, event_layers=()):
    """
    Calls `GotoIfCeremonyState` with `state=True`.
    """


# (1003, 207)
def GotoIfCeremonyInactive(label: Label | int, ceremony: int, event_layers=()):
    """
    Calls `GotoIfCeremonyState` with `state=False`.
    """


# (1003, 208)
def ReturnIfCeremonyState(event_return_type: EventReturnType | int, state: bool | int, ceremony: int, event_layers=()):
    """
    TODO
    """


# (1003, 208)
def EndIfCeremonyActive(ceremony: int, event_layers=()):
    """
    Calls `ReturnIfCeremonyState` with `event_return_type=0`, `state=True`.
    """


# (1003, 208)
def EndIfCeremonyInactive(ceremony: int, event_layers=()):
    """
    Calls `ReturnIfCeremonyState` with `event_return_type=0`, `state=False`.
    """


# (1003, 208)
def RestartIfCeremonyActive(ceremony: int, event_layers=()):
    """
    Calls `ReturnIfCeremonyState` with `event_return_type=1`, `state=True`.
    """


# (1003, 208)
def RestartIfCeremonyInactive(ceremony: int, event_layers=()):
    """
    Calls `ReturnIfCeremonyState` with `event_return_type=1`, `state=False`.
    """


# (1003, 212)
def SkipLinesIfArenaMatchType(
    line_count: int,
    match_type: ArenaMatchType | int,
    has_spirit_summon: bool | int,
    event_layers=(),
):
    """
    Skip some number of lines if the current arena match type is the given type.
    """


# (1003, 213)
def GotoLinesIfArenaMatchType(
    label: Label | int,
    match_type: ArenaMatchType | int,
    has_spirit_summon: bool | int,
    event_layers=(),
):
    """
    Go to label if the current arena match type is the given type.
    """


# (1003, 214)
def ReturnIfArenaMatchType(
    event_return_type: EventReturnType | int,
    match_type: ArenaMatchType | int,
    has_spirit_summon: bool | int,
    event_layers=(),
):
    """
    End or restart if the current arena match type is the given type.
    """


# (1003, 214)
def EndIfArenaMatchType(match_type: ArenaMatchType | int, has_spirit_summon: bool | int, event_layers=()):
    """
    Calls `ReturnIfArenaMatchType` with `event_return_type=0`.
    """


# (1003, 214)
def RestartIfArenaMatchType(match_type: ArenaMatchType | int, has_spirit_summon: bool | int, event_layers=()):
    """
    Calls `ReturnIfArenaMatchType` with `event_return_type=1`.
    """


# (1004, 0)
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


# (1004, 0)
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


# (1004, 0)
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


# (1004, 0)
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


# (1004, 0)
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


# (1004, 1)
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


# (1004, 1)
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


# (1004, 1)
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


# (1004, 1)
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


# (1004, 1)
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


# (1004, 2)
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


# (1004, 2)
def EndIfPlayerHasSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `character=10000`, `state=True`.
    """


# (1004, 2)
def EndIfPlayerDoesNotHaveSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=0`, `character=10000`, `state=False`.
    """


# (1004, 2)
def RestartIfPlayerHasSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=1`, `character=10000`, `state=True`.
    """


# (1004, 2)
def RestartIfPlayerDoesNotHaveSpecialEffect(
    special_effect: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: int = 1,
    event_layers=(),
):
    """
    Calls `ReturnIfCharacterSpecialEffectState` with `event_return_type=1`, `character=10000`, `state=False`.
    """


# (1004, 2)
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


# (1004, 2)
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


# (1004, 2)
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


# (1004, 2)
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


# (1004, 3)
def SkipLinesIfSpecialStandbyEndedFlagState(
    line_count: int,
    character: Character | int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (1004, 3)
def SkipLinesIfSpecialStandbyEndedFlagEnabled(line_count: int, character: Character | int, event_layers=()):
    """
    Calls `SkipLinesIfSpecialStandbyEndedFlagState` with `state=True`.
    """


# (1004, 3)
def SkipLinesIfSpecialStandbyEndedFlagDisabled(line_count: int, character: Character | int, event_layers=()):
    """
    Calls `SkipLinesIfSpecialStandbyEndedFlagState` with `state=False`.
    """


# (1004, 4)
def GotoIfSpecialStandbyEndedFlagState(
    label: Label | int,
    character: Character | int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (1004, 4)
def GotoIfSpecialStandbyEndedFlagEnabled(label: Label | int, character: Character | int, event_layers=()):
    """
    Calls `GotoIfSpecialStandbyEndedFlagState` with `state=True`.
    """


# (1004, 4)
def GotoIfSpecialStandbyEndedFlagDisabled(label: Label | int, character: Character | int, event_layers=()):
    """
    Calls `GotoIfSpecialStandbyEndedFlagState` with `state=False`.
    """


# (1004, 5)
def ReturnIfSpecialStandbyEndedFlagState(
    event_return_type: EventReturnType | int,
    character: Character | int,
    state: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (1004, 5)
def EndIffSpecialStandbyEndedFlagEnabled(character: Character | int, event_layers=()):
    """
    Calls `ReturnIfSpecialStandbyEndedFlagState` with `event_return_type=0`, `state=True`.
    """


# (1004, 5)
def EndIffSpecialStandbyEndedFlagDisabled(character: Character | int, event_layers=()):
    """
    Calls `ReturnIfSpecialStandbyEndedFlagState` with `event_return_type=0`, `state=False`.
    """


# (1004, 5)
def RestartIffSpecialStandbyEndedFlagEnabled(character: Character | int, event_layers=()):
    """
    Calls `ReturnIfSpecialStandbyEndedFlagState` with `event_return_type=1`, `state=True`.
    """


# (1004, 5)
def RestartIffSpecialStandbyEndedFlagDisabled(character: Character | int, event_layers=()):
    """
    Calls `ReturnIfSpecialStandbyEndedFlagState` with `event_return_type=1`, `state=False`.
    """


# (1005, 0)
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


# (1005, 0)
def AwaitAssetDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `AwaitAssetDestrucionState` with `state=True`.
    """


# (1005, 0)
def AwaitAssetNotDestroyed(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
):
    """
    Calls `AwaitAssetDestrucionState` with `state=False`.
    """


# (1005, 101)
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


# (1005, 101)
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


# (1005, 101)
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


# (1014, 0)
def DefineLabel_0(event_layers=()):
    """
    Define position of label 0 for Goto instructions.
    """


# (1014, 1)
def DefineLabel_1(event_layers=()):
    """
    Define position of label 1 for Goto instructions.
    """


# (1014, 2)
def DefineLabel_2(event_layers=()):
    """
    Define position of label 2 for Goto instructions.
    """


# (1014, 3)
def DefineLabel_3(event_layers=()):
    """
    Define position of label 3 for Goto instructions.
    """


# (1014, 4)
def DefineLabel_4(event_layers=()):
    """
    Define position of label 4 for Goto instructions.
    """


# (1014, 5)
def DefineLabel_5(event_layers=()):
    """
    Define position of label 5 for Goto instructions.
    """


# (1014, 6)
def DefineLabel_6(event_layers=()):
    """
    Define position of label 6 for Goto instructions.
    """


# (1014, 7)
def DefineLabel_7(event_layers=()):
    """
    Define position of label 7 for Goto instructions.
    """


# (1014, 8)
def DefineLabel_8(event_layers=()):
    """
    Define position of label 8 for Goto instructions.
    """


# (1014, 9)
def DefineLabel_9(event_layers=()):
    """
    Define position of label 9 for Goto instructions.
    """


# (1014, 10)
def DefineLabel_10(event_layers=()):
    """
    Define position of label 10 for Goto instructions.
    """


# (1014, 11)
def DefineLabel_11(event_layers=()):
    """
    Define position of label 11 for Goto instructions.
    """


# (1014, 12)
def DefineLabel_12(event_layers=()):
    """
    Define position of label 12 for Goto instructions.
    """


# (1014, 13)
def DefineLabel_13(event_layers=()):
    """
    Define position of label 13 for Goto instructions.
    """


# (1014, 14)
def DefineLabel_14(event_layers=()):
    """
    Define position of label 14 for Goto instructions.
    """


# (1014, 15)
def DefineLabel_15(event_layers=()):
    """
    Define position of label 15 for Goto instructions.
    """


# (1014, 16)
def DefineLabel_16(event_layers=()):
    """
    Define position of label 16 for Goto instructions.
    """


# (1014, 17)
def DefineLabel_17(event_layers=()):
    """
    Define position of label 17 for Goto instructions.
    """


# (1014, 18)
def DefineLabel_18(event_layers=()):
    """
    Define position of label 18 for Goto instructions.
    """


# (1014, 19)
def DefineLabel_19(event_layers=()):
    """
    Define position of label 19 for Goto instructions.
    """


# (1014, 20)
def DefineLabel_20(event_layers=()):
    """
    Define position of label 20 for Goto instructions.
    """


# (2001, 4)
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


# (2001, 5)
def SetTimeFreezeState(state: bool | int, event_layers=()):
    """
    TODO
    """


# (2001, 5)
def FreezeTime(event_layers=()):
    """
    Calls `SetTimeFreezeState` with `state=True`.
    """


# (2001, 5)
def UnfreezeTime(event_layers=()):
    """
    Calls `SetTimeFreezeState` with `state=False`.
    """


# (2002, 10)
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


# (2002, 11)
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


# (2002, 12)
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


# (2002, 13)
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


# (2003, 42)
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


# (2003, 43)
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


# (2003, 44)
def SetDirectionDisplay(state: bool | int, event_layers=()):
    """
    TODO
    """


# (2003, 44)
def EnableDirectionDisplay(event_layers=()):
    """
    Calls `SetDirectionDisplay` with `state=True`.
    """


# (2003, 44)
def DisableDirectionDisplay(event_layers=()):
    """
    Calls `SetDirectionDisplay` with `state=False`.
    """


# (2003, 52)
def TriggerAISound(
    ai_sound_param_id: int,
    anchor_entity: Asset | Character | Region | int,
    unk_8_12: int,
    event_layers=(),
):
    """
    TODO
    """


# (2003, 54)
def ForceSpawnerToSpawn(spawner: SpawnerEvent | int, event_layers=()):
    """
    TODO
    """


# (2003, 63)
def SetNetworkConnectedFlagRangeState(flag_range: FlagRange | tuple | list, state: FlagSetting | int, event_layers=()):
    """
    Network-synchronized variant of `SetFlagRangeState` (2003[22]).
    """


# (2003, 63)
def EnableNetworkConnectedFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetNetworkConnectedFlagRangeState` with `state=1`.
    """


# (2003, 63)
def DisableNetworkConnectedFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetNetworkConnectedFlagRangeState` with `state=0`.
    """


# (2003, 63)
def ToggleNetworkConnectedFlagRange(flag_range: FlagRange | tuple | list, event_layers=()):
    """
    Calls `SetNetworkConnectedFlagRangeState` with `state=2`.
    """


# (2003, 64)
def SetOmissionModeCounts(level_1_count: int, level_2_count: int, event_layers=()):
    """
    TODO
    """


# (2003, 65)
def ResetOmissionModeCountsToDefault(event_layers=()):
    """
    TODO
    """


# (2003, 66)
def SetFlagState(flag_type: FlagType | int, flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    Predominant flag-setting instruction in Elden Ring. It can set relative flags, unlike the old 2003[2].
    """


# (2003, 66)
def EnableFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=0`, `state=1`.
    """


# (2003, 66)
def DisableFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=0`, `state=0`.
    """


# (2003, 66)
def ToggleFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=0`, `state=2`.
    """


# (2003, 66)
def SetAbsoluteFlagState(flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=0`.
    """


# (2003, 66)
def EnableThisSlotFlag(event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=2`, `flag=0`, `state=1`.
    """


# (2003, 66)
def DisableThisSlotFlag(event_layers=()):
    """
    Calls `SetFlagState` with `flag_type=2`, `flag=0`, `state=0`.
    """


# (2003, 68)
def SetWeather(weather: Weather | int, duration: float, immediate_change: bool | int, event_layers=()):
    """
    TODO
    """


# (2003, 69)
def SetNetworkFlagState(flag_type: FlagType | int, flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    Enable, disable, or toggle (change) a binary flag for all network-connected players.
    """


# (2003, 69)
def EnableNetworkFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=0`, `state=1`.
    """


# (2003, 69)
def DisableNetworkFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=0`, `state=0`.
    """


# (2003, 69)
def ToggleNetworkFlag(flag: Flag | int, event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=0`, `state=2`.
    """


# (2003, 69)
def SetAbsoluteNetworkFlagState(flag: Flag | int, state: FlagSetting | int, event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=0`.
    """


# (2003, 69)
def EnableThisNetworkFlag(event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=1`, `flag=0`, `state=1`.
    """


# (2003, 69)
def DisableThisNetworkFlag(event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=1`, `flag=0`, `state=0`.
    """


# (2003, 69)
def EnableThisNetworkSlotFlag(event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=2`, `flag=0`, `state=1`.
    """


# (2003, 69)
def DisableThisNetworSlotFlag(event_layers=()):
    """
    Calls `SetNetworkFlagState` with `flag_type=2`, `flag=0`, `state=0`.
    """


# (2003, 70)
def SetNetworkInteractionState(state: bool | int, event_layers=()):
    """
    TODO
    """


# (2003, 71)
def AwardGesture(gesture_param_id: int, event_layers=()):
    """
    Awards a Gesture item to player.
    """


# (2003, 72)
def MultiplyBloodstainSouls(multiplier: float, bloodstain_save_slot_id: int, event_layers=()):
    """
    Apply a multiplier to the amount of souls/echoes/runes waiting to be retrieved from the bloodstain with
    the given save slot ID.
    """


# (2003, 73)
def IncreaseCharacterSoulReward(
    character: Character | int,
    fixed_increase_amount: int,
    soul_amount_load_slot_id: int,
    event_layers=(),
):
    """
    TODO
    """


# (2003, 74)
def IssueEndOfPseudoMultiplayerNotification(success: bool | int, event_layers=()):
    """
    TODO
    """


# (2003, 75)
def UseFarViewCamera(far_view_id: int, asset: Asset | int, dummy_id: int = -1, event_layers=()):
    """
    TODO
    """


# (2003, 76)
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


# (2003, 77)
def SetPseudoMultiplayerReturnPosition(region: Region | int, event_layers=()):
    """
    TODO
    """


# (2003, 78)
def OpenWorldMapPoint(world_map_point_param_id: int, distance: float, event_layers=()):
    """
    TODO
    """


# (2003, 79)
def SendNPCSummonHome(character: Character | int, event_layers=()):
    """
    TODO
    """


# (2003, 80)
def ShowLoadingScreenText(state: bool | int, event_layers=()):
    """
    Enable or disable text on loading screens.
    """


# (2003, 80)
def EnableLoadingScreenText(event_layers=()):
    """
    Calls `ShowLoadingScreenText` with `state=True`.
    """


# (2003, 80)
def DisableLoadingScreenText(event_layers=()):
    """
    Calls `ShowLoadingScreenText` with `state=False`.
    """


# (2003, 81)
def RemoveGesture(gesture_param_id: int, event_layers=()):
    """
    Remove given Gesture from player's inventory'.
    """


# (2003, 82)
def EraseNPCSummonSign(character: Character | int, event_layers=()):
    """
    TODO
    """


# (2003, 83)
def Unknown_2003_83(unk_0_1: bool | int, event_layers=()):
    """
    TODO
    """


# (2004, 48)
def ChangeCharacterCloth(character: Character | int, bit_count: int, state_id: int, event_layers=()):
    """
    TODO
    """


# (2004, 49)
def ChangePatrolBehavior(character: Character | int, patrol_information_id: int, event_layers=()):
    """
    I don't know what a 'patrol_information_id' actually is.
    """


# (2004, 50)
def SetLockOnPoint(character: Character | int, lock_on_dummy_id: int, state: bool | int, event_layers=()):
    """
    Presumably changes the point that is locked on to by the player.
    """


# (2004, 52)
def ChangePlayerCharacterInitParam(character_init_param: int, event_layers=()):
    """
    I assume this affects the player.
    """


# (2004, 55)
def SetCharacterTalkRange(character: Character | int, distance: float, event_layers=()):
    """
    TODO
    """


# (2004, 60)
def ConnectCharacterToCaravan(character: Character | int, caravan_asset: Asset | int, event_layers=()):
    """
    Used to connect trolls to the caravans they pull.
    """


# (2004, 61)
def Unknown_2004_61(unk_0_4: int, event_layers=()):
    """
    Used only once: in Stranded Graveyard with argument 9999.
    """


# (2004, 63)
def SetCharacterEnableDistance(character: Character | int, distance: float, event_layers=()):
    """
    TODO
    """


# (2004, 67)
def CopyPlayerCharacterData(source_character: Character | int, dest_character: Character | int, event_layers=()):
    """
    Used, for example, to initialize Mimics and set up Gideon's boss loadout.
    """


# (2004, 68)
def AttachAssetToCharacter(character: Character | int, dummy_id: int, asset: Asset | int, event_layers=()):
    """
    TODO
    """


# (2004, 69)
def SetCharacterDisableOnCollisionUnload(character: Character | int, state: bool | int, event_layers=()):
    """
    I believe this will, if enabled for a character, cause that character to be disabled when the collision they
    are standing on (or possibly their draw parent) is unloaded.
    """


# (2004, 70)
def SetDistanceBasedNetworkAuthorityUpdate(character: Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (2004, 71)
def Unknown_2004_71(
    unk_0_4: int,
    entity_a: Asset | Character | Region | int,
    entity_b: Asset | Character | Region | int,
    event_layers=(),
):
    """
    TODO
    """


# (2004, 73)
def SetCharacterFadeOnEnable(character: Character | int, state: bool | int, event_layers=()):
    """
    Determines if character will fade-in when enabled, I believe.
    """


# (2004, 74)
def MoveCharacterAndCopyDrawParentWithFadeout(
    character: Character | int,
    destination_type: CoordEntityType | int,
    destination: Asset | Character | Region | int,
    dummy_id: int,
    copy_draw_parent: Asset | Character | Region | int,
    use_bonfire_effect: bool | int,
    reset_camera: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (2004, 75)
def SetCharacterFaceParamOverride(character: Character | int, override_slot: int, face_param_id: int, event_layers=()):
    """
    TODO
    """


# (2004, 76)
def Unknown_2004_76(flag: Flag | int, item_lot: int, event_layers=()):
    """
    Unknown. `flag` appears to be a boss death flag and `item_lot` the reward for that boss.
    
    Called on the first line of boss-despawning common event 90005860 if an item lot was passed in.
    """


# (2004, 77)
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


# (2004, 78)
def CopyPlayerCharacterDataFromOnlinePlayers(
    pool_type: int,
    failcase_player_param_id: int,
    target_character: Character | int,
    event_layers=(),
):
    """
    TODO
    """


# (2004, 79)
def RequestPlayerCharacterDataFromOnlinePlayers(pool_type: int, data_count: int, event_layers=()):
    """
    TODO
    """


# (2004, 80)
def SendPlayerCharacterDataToOnlinePlayers(pool_type: int, event_layers=()):
    """
    TODO
    """


# (2004, 81)
def ResetCharacterPosition(character: Character | int, event_layers=()):
    """
    Resets character position to MSB coordinates, I assume.
    """


# (2004, 83)
def SetSpecialStandbyEndedFlag(character: Character | int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (2004, 84)
def SetCharacterEnableDistanceWithUnknown(
    character: Character | int,
    enable_distance: float,
    unknown_distance: float,
    event_layers=(),
):
    """
    TODO
    """


# (2005, 17)
def AttachCaravanToController(caravan_asset: Asset | int, character: Character | int, event_layers=()):
    """
    Attaches caravan to trolls pulling it, presuamably (there is also an inverse event).
    """


# (2005, 18)
def AttachAssetToAsset(child_asset: Asset | int, parent_asset: Asset | int, parent_dummy_id: int = -1, event_layers=()):
    """
    TODO
    """


# (2005, 20)
def CreateBigHazardousAsset(
    asset_flag: Flag | int,
    asset: int,
    dummy_id_start: int,
    dummy_id_end: int,
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


# (2006, 6)
def SetWindVFX(wind_vfx_id: int, event_layers=()):
    """
    Not sure if argument is an MSB VFX Event ID (more likely) or an absolute VFX asset ID.
    """


# (2007, 10)
def AwaitDialogResponse(
    message: EventText | int,
    button_type: ButtonType | int,
    number_buttons: NumberButtons | int,
    anchor_entity: Asset | Character | Region | int,
    display_distance: float,
    left_flag: Flag | int,
    right_flag: Flag | int,
    cancel_flag: Flag | int,
    event_layers=(),
):
    """
    Displays a dialog and enables one of three flags, depending on the player's response. Very useful. `right`
    and `cancel` flags are often identical.
    
    Halts execution until the player responds.
    """


# (2007, 12)
def DisplayFlashingMessageWithPriority(
    text: EventText | int,
    priority: int,
    should_interrupt: bool | int,
    event_layers=(),
):
    """
    TODO
    """


# (2007, 13)
def DisplaySubareaWelcomeMessage(place_name_id: PlaceName | int, event_layers=()):
    """
    Uses PlaceName FMG.
    """


# (2007, 14)
def DisplayAreaWelcomeMessage(place_name_id: PlaceName | int, event_layers=()):
    """
    Uses PlaceName FMG.
    """


# (2007, 15)
def DisplayTutorialMessage(tutorial_param_id: int, unk_4_5: bool | int, unk_5_6: bool | int, event_layers=()):
    """
    TODO
    """


# (2007, 16)
def DisplayNetworkMessage(text: EventText | int, unk_4_5: bool | int, event_layers=()):
    """
    TODO
    """


# (2008, 4)
def SetCameraAngle(x_angle: float, y_angle: float, event_layers=()):
    """
    Used very often, presumably to gently push the camera to a specific latitude/longitude.
    """


# (2009, 8)
def BanishInvaders(unknown: int, event_layers=()):
    """
    TODO
    """


# (2009, 11)
def BanishPhantoms(unknown: int, event_layers=()):
    """
    TODO
    """


# (2009, 12)
def BanishPhantomsAndUpdateServerPvPStats(unknown: int, event_layers=()):
    """
    TODO
    """


# (2010, 7)
def SuppressSoundEvent(sound_id: SoundEvent | int, unk_4_8: int, suppression_active: bool | int, event_layers=()):
    """
    TODO
    """


# (2010, 8)
def UnknownSound_2010_8(sound_id: SoundEvent | int, event_layers=()):
    """
    TODO
    """


# (2010, 10)
def SetBossMusic(bgm_boss_conv_param_id: int, state: BossMusicState | int, event_layers=()):
    """
    TODO
    """


# (2010, 11)
def SuppressSoundForFogGate(duration: float, event_layers=()):
    """
    TODO
    """


# (2010, 12)
def SetFieldBattleMusicHeatUp(npc_threat_level: int, state: bool | int, event_layers=()):
    """
    TODO
    """


# (2010, 12)
def EnableFieldBattleMusicHeatUp(npc_threat_level: int, event_layers=()):
    """
    Calls `SetFieldBattleMusicHeatUp` with `state=True`.
    """


# (2010, 12)
def DisableFieldBattleMusicHeatUp(npc_threat_level: int, event_layers=()):
    """
    Calls `SetFieldBattleMusicHeatUp` with `state=False`.
    """


# (2012, 8)
def SetAreaWelcomeMessageState(state: bool | int, event_layers=()):
    """
    TODO
    """


# (2012, 11)
def ActivateGparamOverride(gparam_sub_id: int, change_duration: float, event_layers=()):
    """
    TODO
    """


# (2012, 12)
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
    entity: Asset | Character | Region | int,
    other_entity: Asset | Character | Region | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def PlayerWithinDistance(
    other_entity: Asset | Character | Region | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def PlayerBeyondDistance(
    other_entity: Asset | Character | Region | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def EntityWithinDistance(
    entity: Asset | Character | Region | int,
    other_entity: Asset | Character | Region | int,
    radius: float,
    min_target_count: int = 1,
    event_layers=(),
) -> bool:
    ...


def EntityBeyondDistance(
    entity: Asset | Character | Region | int,
    other_entity: Asset | Character | Region | int,
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


def EventsComparison(
    left_flag: Flag | int,
    left_bit_count: int,
    comparison_type: ComparisonType | int,
    right_flag: Flag | int,
    right_bit_count: int,
    event_layers=(),
) -> bool:
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


def CharacterIsType(
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
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetHealthValueEqual(
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetHealthValueNotEqual(
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetHealthValueGreaterThan(
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetHealthValueLessThan(
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetHealthValueGreaterThanOrEqual(
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
    ...


def AssetHealthValueLessThanOrEqual(
    asset: Asset | int,
    value: int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> bool:
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


def ActionButtonParamActivated(action_button_id: int, entity: Asset | Character | Region | int, event_layers=()) -> bool:
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


def ArenaMatchReadyState(ready: bool | int, event_layers=()) -> bool:
    ...


def ArenaSoloResult(result: ArenaResult | int, event_layers=()) -> bool:
    ...


def ArenaSoloScoreComparison(comparison_type: ComparisonType | int, score: int, event_layers=()) -> bool:
    ...


def ArenaTeamResults(result: ArenaResult | int, event_layers=()) -> bool:
    ...


def ArenaTeamScoreComparison(comparison_type: ComparisonType | int, score: int, event_layers=()) -> bool:
    ...


def ArenaMatchType(match_type: ArenaMatchType | int, has_spirit_summon: bool | int, event_layers=()) -> bool:
    ...


def PlayerRespawnedInArena(event_layers=()) -> bool:
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
    anchor_entity: Asset | Character | Region | int,
    anchor_type: CoordEntityType | int = None,
    facing_angle: float = None,
    max_distance: float = None,
    dummy_id: int = -1,
    trigger_attribute: TriggerAttribute | int = 48,
    button: int = 0,
    boss_version: bool = False,
    line_intersects: Asset | Character | Region | int = None,
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


def PlayerHasTalisman(ring: AccessoryParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerHasTalisman`.
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


def PlayerDoesNotHaveTalisman(ring: AccessoryParam | int, including_storage: bool = False, event_layers=()) -> bool:
    """
    Calls `compiler.IfPlayerDoesNotHaveTalisman`.
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


def AssetHealthValue(
    asset: Asset | int,
    target_comparison_type: ComparisonType | int = ComparisonType.Equal,
    target_count: float = 1.0,
    event_layers=(),
) -> int:
    """
    Compare output to a value as a shortcut for calling `AssetHealthValueComparison(...)`.
    """
    ...
