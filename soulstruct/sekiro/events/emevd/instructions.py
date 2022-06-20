"""Full instruction set for DS3.

Many instructions in DS3 have some added debug parameters called 'target_comparison_type' and 'target_count', each of
which are almost always set to '==' and '1' in the vanilla events. You probably don't want to change those, but if so,
I've only left access to them in the base instruction of each type (the ones that actually call `to_numeric`).
"""
__all__ = [
    # Shared instructions
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
    "SetMapCollisionState",
    "EnableMapCollision",
    "DisableMapCollision",
    "SetMapCollisionBackreadMaskState",
    "EnableMapCollisionBackreadMask",
    "DisableMapCollisionBackreadMask",
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
    # Dark Souls 3
    "RunCommonEvent",
    "IfMultiplayerState",
    "IfHost",
    "IfClient",
    "IfTryingToCreateSession",
    "IfTryingToJoinSession",
    "IfLeavingSession",
    "IfFailedToCreateSession",
    "IfAttackedWithDamageType",
    "IfActionButtonParam",
    "IfPlayerOwnWorldState",
    "IfPlayerInOwnWorld",
    "IfPlayerNotInOwnWorld",
    "IfMapCeremonyState",
    "IfMapInCeremony",
    "IfMapNotInCeremony",
    "IfMultiplayerNetworkPenalized",
    "IfPlayerGender",
    "IfOngoingCutsceneFinished",
    "IfHollowArenaMatchReadyState",
    "IfHollowArenaSoloResults",
    "IfHollowArenaSoloScoreComparison",
    "IfHollowArenaTeamResults",
    "IfSteamDisconnected",
    "IfAllyPhantomCountComparison",
    "IfPlayerHasSpecialEffect",
    "IfPlayerDoesNotHaveSpecialEffect",
    "IfCharacterDrawGroupState",
    "IfCharacterDrawGroupActive",
    "IfCharacterDrawGroupInactive",
    "IfPlayerRemainingYoelLevelComparison",
    "IfCharacterInvadeType",
    "IfCharacterChameleonState",
    "IfObjectBurnState",
    "IfObjectBackreadState",
    "IfObjectBackreadEnabled",
    "IfObjectBackreadDisabled",
    "IfObjectBackreadState_Alternate",
    "IfObjectBackreadEnabled_Alternate",
    "IfObjectBackreadDisabled_Alternate",
    "GotoIfConditionState",
    "GotoIfConditionTrue",
    "GotoIfConditionFalse",
    "Goto",
    "GotoIfValueComparison",
    "GotoIfFinishedConditionState",
    "GotoIfFinishedConditionTrue",
    "GotoIfFinishedConditionFalse",
    "WaitHollowArenaHalftime",
    "SkipLinesIfMultiplayerState",
    "SkipLinesIfHost",
    "SkipLinesIfClient",
    "SkipLinesIfTryingToCreateSession",
    "SkipLinesIfTryingToJoinSession",
    "SkipLinesIfLeavingSession",
    "SkipLinesIfFailedToCreateSession",
    "ReturnIfMultiplayerState",
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
    "SkipLinesIfCoopClientCountComparison",
    "ReturnIfCoopClientCountComparison",
    "EndIfCoopClientCountComparison",
    "RestartIfCoopClientCountComparison",
    "GotoIfCharacterSpecialEffectState",
    "GotoIfCharacterHasSpecialEffect",
    "GotoIfCharacterDoesNotHaveSpecialEffect",
    "GotoIfPlayerOwnWorldState",
    "GotoIfPlayerInOwnWorld",
    "GotoIfPlayerNotInOwnWorld",
    "ReturnIfPlayerOwnWorldState",
    "EndIfPlayerOwnWorldState",
    "EndIfPlayerInOwnWorld",
    "EndIfPlayerNotInOwnWorld",
    "RestartIfPlayerOwnWorldState",
    "RestartIfPlayerInOwnWorld",
    "RestartIfPlayerNotInOwnWorld",
    "SkipLinesIfClientTypeCountComparison",
    "GotoIfClientTypeCountComparison",
    "ReturnIfClientTypeCountComparison",
    "EndIfClientTypeCountComparison",
    "RestartIfClientTypeCountComparison",
    "GotoIfFlagState",
    "GotoIfThisEventOn",
    "GotoIfThisEventOff",
    "GotoIfThisEventSlotOn",
    "GotoIfThisEventSlotOff",
    "GotoIfFlagOn",
    "GotoIfFlagOff",
    "GotoIfFlagRangeState",
    "GotoIfFlagRangeAllOn",
    "GotoIfFlagRangeAllOff",
    "GotoIfFlagRangeAnyOn",
    "GotoIfFlagRangeAnyOff",
    "GotoIfMultiplayerState",
    "GotoIfHost",
    "GotoIfClient",
    "GotoIfTryingToCreateSession",
    "GotoIfTryingToJoinSession",
    "GotoIfLeavingSession",
    "GotoIfFailedToCreateSession",
    "GotoIfMapPresenceState",
    "GotoIfInsideMap",
    "GotoIfOutsideMap",
    "GotoIfCoopClientCountComparison",
    "ReturnIfCharacterSpecialEffectState",
    "EndIfCharacterSpecialEffectState",
    "EndIfCharacterHasSpecialEffect",
    "EndIfCharacterDoesNotHaveSpecialEffect",
    "RestartIfCharacterSpecialEffectState",
    "RestartIfCharacterHasSpecialEffect",
    "RestartIfCharacterDoesNotHaveSpecialEffect",
    "EndIfPlayerHasSpecialEffect",
    "EndIfPlayerDoesNotHaveSpecialEffect",
    "RestartIfPlayerHasSpecialEffect",
    "RestartIfPlayerDoesNotHaveSpecialEffect",
    "SkipLinesIfCharacterSpecialEffectState",
    "SkipLinesIfCharacterHasSpecialEffect",
    "SkipLinesIfCharacterDoesNotHaveSpecialEffect",
    "SkipLinesIfPlayerHasSpecialEffect",
    "SkipLinesIfPlayerDoesNotHaveSpecialEffect",
    "GotoIfCharacterRegionState",
    "GotoIfCharacterInsideRegion",
    "GotoIfCharacterOutsideRegion",
    "ReturnIfCharacterRegionState",
    "EndIfCharacterRegionState",
    "EndIfCharacterInsideRegion",
    "EndIfCharacterOutsideRegion",
    "RestartIfCharacterRegionState",
    "RestartIfCharacterInsideRegion",
    "RestartIfCharacterOutsideRegion",
    "SkipLinesIfCharacterRegionState",
    "SkipLinesIfCharacterInsideRegion",
    "SkipLinesIfCharacterOutsideRegion",
    "GotoIfHollowArenaMatchType",
    "GotoIfObjectDestructionState",
    "GotoIfObjectDestroyed",
    "GotoIfObjectNotDestroyed",
    "DefineLabel",
    "PlayCutsceneAndMovePlayerAndSetTimePeriod",
    "PlayCutsceneAndSetTimePeriod",
    "PlayCutsceneAndMovePlayer_Dummy",
    "PlayCutsceneAndMovePlayerAndSetMapCeremony",
    "PlayCutsceneAndSetMapCeremony",
    "PlayCutsceneAndMovePlayer_WithUnknowns",
    "PlayCutsceneAndMovePlayer_WithSecondRegion",
    "SetBossHealthBarState",
    "EnableBossHealthBar",
    "DisableBossHealthBar",
    "HandleMinibossDefeat",
    "Unknown_2003_27",
    "EventValueOperation",
    "StoreItemAmountSpecifiedByFlagValue",
    "GivePlayerItemAmountSpecifiedByFlagValue",
    "SetDirectionDisplayState",
    "EnableDirectionDisplay",
    "DisableDirectionDisplay",
    "SetMapHitGridCorrespondence",
    "EnableMapHitGridCorrespondence",
    "DisableMapHitGridCorrespondence",
    "SetMapContentImageDisplayState",
    "SetMapBoundariesDisplay",
    "SetAreaWind",
    "WarpPlayerToRespawnPoint",
    "StartEnemySpawner",
    "SummonNPC",
    "InitializeWarpObject",
    "MakeEnemyAppear",
    "SetCurrentMapCeremony",
    "SetMapCeremony",
    "DisplayEpitaphMessage",
    "SetNetworkConnectedFlagState",
    "SetNetworkConnectedFlagRangeState",
    "SetOmissionModeCounts",
    "ResetOmissionModeCountsToDefault",
    "InitializeCrowTrade",
    "InitializeCrowTradeRegion",
    "SetNetworkInteractionState",
    "SetHUDVisibilityState",
    "EnableHUDVisibility",
    "DisableHUDVisibility",
    "SetBonfireWarpingState",
    "EnableBonfireWarping",
    "DisableBonfireWarping",
    "SetAutogeneratedEventSpecificFlag_1",
    "HandleBossDefeatAndDisplayBanner",
    "SetAutogeneratedEventSpecificFlag_2",
    "SetLoadingScreenTipsState",
    "EnableLoadingScreenTips",
    "DisableLoadingScreenTips",
    "AwardGestureItem",
    "SendNPCSummonHome",
    "Unknown_2003_79",
    "SetDecoratedBossHealthBarState",
    "EnableDecoratedBossHealthBar",
    "DisableDecoratedBossHealthBar",
    "PlaceNPCSummonSign_WithoutEmber",
    "AddSpecialEffect",
    "RotateToFaceEntity",
    "ChangeCharacterCloth",
    "ChangePatrolBehavior",
    "SetLockOnPoint",
    "Test_RequestRagdollRestraint",
    "ChangePlayerCharacterInitParam",
    "AdaptSpecialEffectHealthChangeToNPCPart",
    "ImmediateActivate",
    "SetCharacterTalkRange",
    "IncrementCharacterNewGameCycle",
    "SetMultiplayerBuffs_NonBoss",
    "Unknown_2004_59",
    "SetPlayerRemainingYoelLevels",
    "ExtinguishBurningObjects",
    "ShowObjectByMapCeremony",
    "DestroyObject_NoSlot",
    "DisplayDialogAndSetFlags",
    "DisplayAreaWelcomeMessage",
    "DisplayHollowArenaMessage",
    "RegisterHealingFountain",
    "BanishInvaders",
    "BanishPhantomsAndUpdateServerPvPStats",
    "BanishPhantoms",
    "SetBossMusicState",
    "EnableBossMusic",
    "DisableBossMusic",
    "NotifyDoorEventSoundDampening",
    "SetSoundEventWithFade",
    "EnableSoundEventWithFade",
    "DisableSoundEventWithFade",
    "Unknown_2010_07",
    "SetCollisionResState",
    "ActivateCollisionAndCreateNavmesh",
    "SetAreaWelcomeMessageState",
    "EnableAreaWelcomeMessage",
    "DisableAreaWelcomeMessage",
    "CreatePlayLog",
    "StartPlayLogMeasurement",
    "StopPlayLogMeasurement",
    "PlayLogParameterOutput",
]

import typing as tp

from soulstruct.base.events.emevd.instructions import *
from soulstruct.base.events.emevd.numeric import to_numeric
from soulstruct.game_types import *
from .enums import *


# 2000: SYSTEM


def RunCommonEvent(event_id: int, args=(0,), arg_types=None, event_layers=None):
    """Same as `RunEvent`, but takes an `event_id` defined in an imported script (generally `common_func`) and takes no
    `slot` argument (unique instances of the event appear to be generated automatically, with no flag being enabled
    when the common event ends).

    As with `RunEvent`, the `event_layers` keyword is supported here for intellisense purposes, but will always be
    handled separately by the EVS parser.
    """
    instruction_info = (2000, 6)  # List for this instruction only, as it may required modification.
    if arg_types is None:
        arg_types = "I" * len(args)
    if len(args) != len(arg_types):
        raise ValueError("Number of event arguments does not match length of argument type string.")
    format_string = "I" + str(arg_types[0])
    if len(arg_types) > 1:
        format_string += f"|{arg_types[1:]}"
    return to_numeric(instruction_info, event_id, *args, arg_types=format_string, event_layers=event_layers)


# 3: CONDITIONS (EVENT)


def IfCharacterRegionState(
    condition,
    entity: AnimatedTyping,
    region: RegionTyping,
    state: bool,
    min_target_count: int = 1,
):
    """New argument with unknown purpose. Always 1 in vanilla resources. Probably for debug."""
    instruction_info = (3, 2)
    return to_numeric(instruction_info, condition, state, entity, region, min_target_count)


def IfCharacterInsideRegion(condition: int, entity: AnimatedTyping, region: RegionTyping):
    return IfCharacterRegionState(condition, entity, region, True)


def IfCharacterOutsideRegion(condition: int, entity: AnimatedTyping, region: RegionTyping):
    return IfCharacterRegionState(condition, entity, region, False)


def IfPlayerInsideRegion(condition: int, region: RegionTyping):
    return IfCharacterRegionState(condition, PLAYER, region, True)


def IfPlayerOutsideRegion(condition: int, region: RegionTyping):
    return IfCharacterRegionState(condition, PLAYER, region, False)


def IfEntityDistanceState(
    condition: int,
    entity: CoordEntityTyping,
    other_entity: CoordEntityTyping,
    radius: float,
    state: bool,
    min_target_count: int = 1,
):
    """Same new argument as region test, with unknown purpose, and again always 1 in EMEVD resources."""
    instruction_info = (3, 3)
    return to_numeric(instruction_info, condition, state, entity, other_entity, radius, min_target_count)


def IfEntityWithinDistance(
    condition: int, entity: CoordEntityTyping, other_entity: CoordEntityTyping, radius: float, min_target_count: int = 1
):
    return IfEntityDistanceState(condition, entity, other_entity, radius, True, min_target_count)


def IfEntityBeyondDistance(
    condition: int, entity: CoordEntityTyping, other_entity: CoordEntityTyping, radius: float, min_target_count: int = 1
):
    return IfEntityDistanceState(condition, entity, other_entity, radius, False, min_target_count)


def IfPlayerWithinDistance(condition: int, other_entity: CoordEntityTyping, radius: float, min_target_count: int = 1):
    return IfEntityDistanceState(condition, PLAYER, other_entity, radius, True, min_target_count)


def IfPlayerBeyondDistance(condition: int, other_entity: CoordEntityTyping, radius: float, min_target_count: int = 1):
    return IfEntityDistanceState(condition, PLAYER, other_entity, radius, False, min_target_count)


def IfMultiplayerState(condition: int, state: MultiplayerState):
    instruction_info = (3, 6)
    return to_numeric(instruction_info, condition, state)


def IfHost(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Host)


def IfClient(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Client)


def IfTryingToCreateSession(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.TryingToCreateSession)


def IfTryingToJoinSession(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.TryingToJoinSession)


def IfLeavingSession(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.LeavingSession)


def IfFailedToCreateSession(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.FailedToCreateSession)


def IfAttackedWithDamageType(
    condition: int,
    attacked_entity: AnimatedTyping,
    attacker: CharacterTyping,
    damage_type: DamageType = DamageType.Unspecified,
):
    """Similar to IsAttackedBy, but requires a certain damage type."""
    instruction_info = (3, 23, [0, 0, -1, 0])
    return to_numeric(instruction_info, condition, attacked_entity, attacker, damage_type)


def IfActionButtonParam(condition: int, action_button_id: int, entity: CoordEntityTyping):
    """Streamlined version of `IfActionButton` that uses information from an `ActionButtonParam` entry."""
    instruction_info = (3, 24, [0, -1, -1])
    return to_numeric(instruction_info, condition, action_button_id, entity)


def IfPlayerOwnWorldState(condition: int, not_in_own_world: bool):
    """Excluding Arena."""
    instruction_info = (3, 26)
    return to_numeric(instruction_info, condition, not_in_own_world)


def IfPlayerInOwnWorld(condition: int):
    return IfPlayerOwnWorldState(condition, False)


def IfPlayerNotInOwnWorld(condition: int):
    return IfPlayerOwnWorldState(condition, True)


def IfMapCeremonyState(condition: int, state: bool, game_map: MapTyping, ceremony_id: int):
    """Ceremony states are unused (except for Untended Graves, I believe)."""
    instruction_info = (3, 28)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, condition, state, area_id, block_id, ceremony_id)


def IfMapInCeremony(condition: int, game_map: MapTyping, ceremony_id: int):
    return IfMapCeremonyState(condition, True, game_map, ceremony_id)


def IfMapNotInCeremony(condition: int, game_map: MapTyping, ceremony_id: int):
    return IfMapCeremonyState(condition, False, game_map, ceremony_id)


def IfMultiplayerNetworkPenalized(condition: int):
    instruction_info = (3, 29)
    return to_numeric(instruction_info, condition)


def IfPlayerGender(condition: int, gender: Gender):
    """Note that this condition version of the gender test was absent in Bloodborne."""
    instruction_info = (3, 30)
    return to_numeric(instruction_info, condition, gender)


def IfOngoingCutsceneFinished(condition: int, cutscene_id: int):
    instruction_info = (3, 31)
    return to_numeric(instruction_info, condition, cutscene_id)


def IfHollowArenaMatchReadyState(condition: int, is_ready: bool):
    instruction_info = (3, 32)
    return to_numeric(instruction_info, condition, is_ready)


def IfHollowArenaSoloResults(condition: int, result: HollowArenaResult):
    instruction_info = (3, 33)
    return to_numeric(instruction_info, condition, result)


def IfHollowArenaSoloScoreComparison(condition: int, comparison_type: ComparisonType, value: int):
    """EMEDF incorrectly says that the value size is 'B'."""
    instruction_info = (3, 34)
    return to_numeric(instruction_info, condition, comparison_type, value)


def IfHollowArenaTeamResults(condition: int, result: HollowArenaResult):
    instruction_info = (3, 35)
    return to_numeric(instruction_info, condition, result)


def IfSteamDisconnected(condition: int, is_disconnected: bool):
    instruction_info = (3, 38)
    return to_numeric(instruction_info, condition, is_disconnected)


def IfAllyPhantomCountComparison(condition: int, comparison_state: bool, comparison_type: ComparisonType, value: int):
    """Note that there's a 'comparison_state' bool that can be used to invert the operation (kind of pointless)."""
    instruction_info = (3, 39)
    return to_numeric(instruction_info, condition, comparison_state, comparison_type, value)


# 4: CONDITIONS (CHARACTER)
# New 'comparison_type' and 'target_count' arguments added to many of them; unknown purpose.
# To make things even weirder, the 'target_count' usually seems to be a float.


def IfCharacterDeathState(
    condition: int,
    character: CharacterTyping,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (4, 0)
    return to_numeric(instruction_info, condition, character, state, target_comparison_type, target_count)


def IfCharacterDead(
    condition: int,
    character: CharacterTyping,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    return IfCharacterDeathState(condition, character, True, target_comparison_type, target_count)


def IfCharacterAlive(
    condition: int,
    character: CharacterTyping,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    return IfCharacterDeathState(condition, character, False, target_comparison_type, target_count)


def IfHealthComparison(
    condition: int,
    character: CharacterTyping,
    comparison_type: ComparisonType,
    value,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (4, 2)
    return to_numeric(
        instruction_info, condition, character, comparison_type, value, target_comparison_type, target_count
    )


def IfHealthEqual(condition: int, character: CharacterTyping, value):
    return IfHealthComparison(condition, character, ComparisonType.Equal, value)


def IfHealthNotEqual(condition: int, character: CharacterTyping, value):
    return IfHealthComparison(condition, character, ComparisonType.NotEqual, value)


def IfHealthGreaterThan(condition: int, character: CharacterTyping, value):
    return IfHealthComparison(condition, character, ComparisonType.GreaterThan, value)


def IfHealthLessThan(condition: int, character: CharacterTyping, value):
    return IfHealthComparison(condition, character, ComparisonType.LessThan, value)


def IfHealthGreaterThanOrEqual(condition: int, character: CharacterTyping, value):
    return IfHealthComparison(condition, character, ComparisonType.GreaterThanOrEqual, value)


def IfHealthLessThanOrEqual(condition: int, character: CharacterTyping, value):
    return IfHealthComparison(condition, character, ComparisonType.LessThanOrEqual, value)


def IfCharacterType(
    condition: int,
    character: CharacterTyping,
    character_type: CharacterType,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (4, 3)
    return to_numeric(instruction_info, condition, character, character_type, target_comparison_type, target_count)


def IfCharacterHollow(condition: int, character: CharacterTyping):
    return IfCharacterType(condition, character, CharacterType.Hollow)


def IfCharacterHuman(condition: int, character: CharacterTyping):
    return IfCharacterType(condition, character, CharacterType.Human)


def IfCharacterSpecialEffectState(
    condition: int,
    character: CharacterTyping,
    special_effect: int,
    state,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (4, 5, [0, 0, -1, 0, 0, 0])
    return to_numeric(
        instruction_info, condition, character, special_effect, state, target_comparison_type, target_count
    )


def IfCharacterHasSpecialEffect(condition: int, character: CharacterTyping, special_effect):
    return IfCharacterSpecialEffectState(condition, character, special_effect, True)


def IfCharacterDoesNotHaveSpecialEffect(condition: int, character: CharacterTyping, special_effect):
    return IfCharacterSpecialEffectState(condition, character, special_effect, False)


def IfPlayerHasSpecialEffect(condition: int, special_effect):
    return IfCharacterSpecialEffectState(condition, PLAYER, special_effect, True)


def IfPlayerDoesNotHaveSpecialEffect(condition: int, special_effect):
    return IfCharacterSpecialEffectState(condition, PLAYER, special_effect, False)


def IfCharacterBackreadState(
    condition: int,
    character: CharacterTyping,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (4, 7)
    return to_numeric(instruction_info, condition, character, state, target_comparison_type, target_count)


def IfCharacterBackreadEnabled(condition: int, character: CharacterTyping):
    return IfCharacterBackreadState(condition, character, True)


def IfCharacterBackreadDisabled(condition: int, character: CharacterTyping):
    return IfCharacterBackreadState(condition, character, False)


def IfTAEEventState(
    condition: int,
    character: CharacterTyping,
    tae_event_id: int,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (4, 8, [0, 0, -1, 0, 0, 0])
    return to_numeric(instruction_info, condition, character, tae_event_id, state, target_comparison_type, target_count)


def IfHasTAEEvent(condition: int, character: CharacterTyping, tae_event_id: int):
    return IfTAEEventState(condition, character, tae_event_id, True)


def IfDoesNotHaveTAEEvent(condition: int, character: CharacterTyping, tae_event_id: int):
    return IfTAEEventState(condition, character, tae_event_id, False)


def IfHasAIStatus(
    condition: int,
    character: CharacterTyping,
    ai_status: AIStatusType,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (4, 9)
    return to_numeric(instruction_info, condition, character, ai_status, target_comparison_type, target_count)


def IfHealthValueComparison(
    condition: int,
    character: CharacterTyping,
    comparison_type: ComparisonType,
    value,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (4, 14)
    return to_numeric(
        instruction_info, condition, character, comparison_type, value, target_comparison_type, target_count
    )


def IfHealthValueEqual(condition: int, character: CharacterTyping, value):
    return IfHealthValueComparison(condition, character, ComparisonType.Equal, value)


def IfHealthValueNotEqual(condition: int, character: CharacterTyping, value):
    return IfHealthValueComparison(condition, character, ComparisonType.NotEqual, value)


def IfHealthValueGreaterThan(condition: int, character: CharacterTyping, value):
    return IfHealthValueComparison(condition, character, ComparisonType.GreaterThan, value)


def IfHealthValueLessThan(condition: int, character: CharacterTyping, value):
    return IfHealthValueComparison(condition, character, ComparisonType.LessThan, value)


def IfHealthValueGreaterThanOrEqual(condition: int, character: CharacterTyping, value):
    return IfHealthValueComparison(condition, character, ComparisonType.GreaterThanOrEqual, value)


def IfHealthValueLessThanOrEqual(condition: int, character: CharacterTyping, value):
    return IfHealthValueComparison(condition, character, ComparisonType.LessThanOrEqual, value)


def IfCharacterDrawGroupState(
    condition: int,
    character: CharacterTyping,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """Tests if character's draw group is currently active or inactive."""
    instruction_info = (4, 15, [0, 0, 0, 0, 0])
    return to_numeric(instruction_info, condition, character, state, target_comparison_type, target_count)


def IfCharacterDrawGroupActive(condition: int, character: CharacterTyping):
    return IfCharacterDrawGroupState(condition, character, True)


def IfCharacterDrawGroupInactive(condition: int, character: CharacterTyping):
    return IfCharacterDrawGroupState(condition, character, False)


def IfPlayerRemainingYoelLevelComparison(condition: int, comparison_type: ComparisonType, value: int):
    """Tests the number of remaining levels available from Yoel, I presume."""
    instruction_info = (4, 26)
    return to_numeric(instruction_info, condition, comparison_type, value)


def IfCharacterInvadeType(
    condition: int,
    character: CharacterTyping,
    invade_type: int,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """'invade_type' has an unknown type in the EMEDF. Probably refers to the invader's covenant."""
    instruction_info = (4, 27)
    return to_numeric(instruction_info, condition, character, invade_type, target_comparison_type, target_count)


def IfCharacterChameleonState(condition: int, character: CharacterTyping, chameleon_vfx_id: int, is_transformed: bool):
    instruction_info = (4, 28)
    return to_numeric(instruction_info, condition, character, chameleon_vfx_id, is_transformed)


# 5: CONDITIONS (OBJECT)
# Same new arguments as characters for the destruction test and all new tests.


def IfObjectDestructionState(
    condition: int,
    obj: ObjectTyping,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (5, 0)
    return to_numeric(instruction_info, condition, state, obj, target_comparison_type, target_count)


def IfObjectDestroyed(condition: int, obj: ObjectTyping):
    return IfObjectDestructionState(condition, obj, True)


def IfObjectNotDestroyed(condition: int, obj: ObjectTyping):
    return IfObjectDestructionState(condition, obj, False)


def IfObjectBurnState(
    condition: int,
    obj: ObjectTyping,
    comparison_type: ComparisonType,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """This test is used exactly once, in the High Wall of Lothric, where the 'comparison_type' is GreaterThan. I have
    no idea what that argument does. However, it's possible that 'state' isn't actually a bool, but some measure of the
    intensity of the burn state, because the event it's used in strongly suggests that a fire effect is created as long
    as the burn state is 'greater than zero'."""
    instruction_info = (5, 9)
    return to_numeric(instruction_info, condition, obj, comparison_type, state, target_comparison_type, target_count)


def IfObjectBackreadState(
    condition: int,
    obj: ObjectTyping,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (5, 10)
    return to_numeric(instruction_info, condition, obj, state, target_comparison_type, target_count)


def IfObjectBackreadEnabled(condition: int, obj: ObjectTyping):
    return IfObjectBackreadState(condition, obj, True)


def IfObjectBackreadDisabled(condition: int, obj: ObjectTyping):
    return IfObjectBackreadState(condition, obj, False)


def IfObjectBackreadState_Alternate(
    condition: int,
    obj: ObjectTyping,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """The fact they added this suggests that the 'alternate' version that already existed for characters is actually
    useful in some way (and they did use it in DS1)."""
    instruction_info = (5, 11)
    return to_numeric(instruction_info, condition, obj, state, target_comparison_type, target_count)


def IfObjectBackreadEnabled_Alternate(condition: int, obj: ObjectTyping):
    return IfObjectBackreadState_Alternate(condition, obj, True)


def IfObjectBackreadDisabled_Alternate(condition: int, obj: ObjectTyping):
    return IfObjectBackreadState_Alternate(condition, obj, False)


# 1000: CONTROL FLOW (BASIC)


def GotoIfConditionState(label: Label, required_state: bool, input_condition: int):
    instruction_info = (1000, 101, [0, 0, 0])
    return to_numeric(instruction_info, label, required_state, input_condition)


def GotoIfConditionTrue(label: Label, input_condition: int):
    return GotoIfConditionState(label, True, input_condition)


def GotoIfConditionFalse(label: Label, input_condition: int):
    return GotoIfConditionState(label, False, input_condition)


def Goto(label: Label):
    """Unconditional GOTO."""
    instruction_info = (1000, 103, [0])
    return to_numeric(instruction_info, label)


def GotoIfValueComparison(label: Label, comparison_type: ComparisonType, left: int, right: int):
    instruction_info = (1000, 105)
    return to_numeric(instruction_info, label, comparison_type, left, right)


def GotoIfFinishedConditionState(label: Label, required_state: bool, input_condition: int):
    """Finished version."""
    instruction_info = (1000, 107, [0, 0, 0])
    return to_numeric(instruction_info, label, required_state, input_condition)


def GotoIfFinishedConditionTrue(label: Label, input_condition: int):
    return GotoIfFinishedConditionState(label, True, input_condition)


def GotoIfFinishedConditionFalse(label: Label, input_condition: int):
    return GotoIfFinishedConditionState(label, False, input_condition)


# 1001: CONTROL FLOW (TIMER)


def WaitHollowArenaHalftime(match_type: HollowArenaMatchType, is_second_half: bool):
    """'StayParam lookup'."""
    instruction_info = (1001, 4)
    return to_numeric(instruction_info, match_type, is_second_half)


# 1003: CONTROL FLOW (EVENT)


def SkipLinesIfMultiplayerState(line_count, state: MultiplayerState):
    instruction_info = (1003, 5)
    return to_numeric(instruction_info, line_count, state)


def SkipLinesIfHost(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Host)


def SkipLinesIfClient(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Client)


def SkipLinesIfTryingToCreateSession(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.TryingToCreateSession)


def SkipLinesIfTryingToJoinSession(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.TryingToJoinSession)


def SkipLinesIfLeavingSession(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.LeavingSession)


def SkipLinesIfFailedToCreateSession(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.FailedToCreateSession)


def ReturnIfMultiplayerState(event_return_type: EventReturnType, state: MultiplayerState):
    instruction_info = (1003, 6)
    return to_numeric(instruction_info, event_return_type, state)


def EndIfHost():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.Host)


def EndIfClient():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.Client)


def EndIfTryingToCreateSession():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.TryingToCreateSession)


def EndIfTryingToJoinSession():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.TryingToJoinSession)


def EndIfLeavingSession():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.LeavingSession)


def EndIfFailedToCreateSession():
    return ReturnIfMultiplayerState(EventReturnType.End, MultiplayerState.FailedToCreateSession)


def RestartIfHost():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.Host)


def RestartIfClient():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.Client)


def RestartIfTryingToCreateSession():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.TryingToCreateSession)


def RestartIfTryingToJoinSession():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.TryingToJoinSession)


def RestartIfLeavingSession():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.LeavingSession)


def RestartIfFailedToCreateSession():
    return ReturnIfMultiplayerState(EventReturnType.Restart, MultiplayerState.FailedToCreateSession)


def SkipLinesIfCoopClientCountComparison(line_count: int, comparison_type: ComparisonType, value: int):
    """Value should be from 0 to 4."""
    instruction_info = (1003, 9, [0, 0, 0])
    return to_numeric(instruction_info, line_count, comparison_type, value)


def ReturnIfCoopClientCountComparison(event_return_type: EventReturnType, comparison_type: ComparisonType, value: int):
    instruction_info = (1003, 10, [0, 0, 0])
    return to_numeric(instruction_info, event_return_type, comparison_type, value)


def EndIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return ReturnIfCoopClientCountComparison(EventReturnType.End, comparison_type, value)


def RestartIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return ReturnIfCoopClientCountComparison(EventReturnType.Restart, comparison_type, value)


def GotoIfCharacterSpecialEffectState(
    label: Label,
    character: CharacterTyping,
    special_effect: int,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: int = 1,
):
    """Note that 'target_count' is now an integer again..."""
    instruction_info = (1003, 11)
    return to_numeric(instruction_info, label, character, special_effect, state, target_comparison_type, target_count)


def GotoIfCharacterHasSpecialEffect(
    label: Label,
    character: CharacterTyping,
    special_effect: int,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: int = 1,
):
    return GotoIfCharacterSpecialEffectState(
        label, character, special_effect, True, target_comparison_type, target_count
    )


def GotoIfCharacterDoesNotHaveSpecialEffect(
    label: Label,
    character: CharacterTyping,
    special_effect: int,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: int = 1,
):
    return GotoIfCharacterSpecialEffectState(
        label, character, special_effect, False, target_comparison_type, target_count
    )


def GotoIfPlayerOwnWorldState(label: Label, not_in_own_world: bool):
    instruction_info = (1003, 12)
    return to_numeric(instruction_info, label, not_in_own_world)


def GotoIfPlayerInOwnWorld(label: Label):
    return GotoIfPlayerOwnWorldState(label, False)


def GotoIfPlayerNotInOwnWorld(label: Label):
    return GotoIfPlayerOwnWorldState(label, True)


def ReturnIfPlayerOwnWorldState(event_return_type: EventReturnType, not_in_own_world: bool):
    instruction_info = (1003, 13)
    return to_numeric(instruction_info, event_return_type, not_in_own_world)


def EndIfPlayerOwnWorldState(not_in_own_world: bool):
    return ReturnIfPlayerOwnWorldState(EventReturnType.End, not_in_own_world)


def EndIfPlayerInOwnWorld():
    return ReturnIfPlayerOwnWorldState(EventReturnType.End, False)


def EndIfPlayerNotInOwnWorld():
    return ReturnIfPlayerOwnWorldState(EventReturnType.End, True)


def RestartIfPlayerOwnWorldState(not_in_own_world: bool):
    return ReturnIfPlayerOwnWorldState(EventReturnType.Restart, not_in_own_world)


def RestartIfPlayerInOwnWorld():
    return ReturnIfPlayerOwnWorldState(EventReturnType.Restart, False)


def RestartIfPlayerNotInOwnWorld():
    return ReturnIfPlayerOwnWorldState(EventReturnType.Restart, True)


def SkipLinesIfClientTypeCountComparison(
    line_count: int, client_type: ClientType, comparison_type: ComparisonType, value: int
):
    """Value from 0 to 4."""
    instruction_info = (1003, 14, [0, 0, 0, 0])
    return to_numeric(instruction_info, line_count, client_type, comparison_type, value)


def GotoIfClientTypeCountComparison(label: Label, client_type: ClientType, comparison_type: ComparisonType, value: int):
    """Value from 0 to 4."""
    instruction_info = (1003, 15, [0, 0, 0, 0])
    return to_numeric(instruction_info, label, client_type, comparison_type, value)


def ReturnIfClientTypeCountComparison(
    event_return_type: EventReturnType, client_type: ClientType, comparison_type: ComparisonType, value: int
):
    """Value from 0 to 4."""
    instruction_info = (1003, 16, [0, 0, 0, 0])
    return to_numeric(instruction_info, event_return_type, client_type, comparison_type, value)


def EndIfClientTypeCountComparison(client_type: ClientType, comparison_type: ComparisonType, value: int):
    """Value from 0 to 4."""
    return ReturnIfClientTypeCountComparison(EventReturnType.End, client_type, comparison_type, value)


def RestartIfClientTypeCountComparison(client_type: ClientType, comparison_type: ComparisonType, value: int):
    """Value from 0 to 4."""
    return ReturnIfClientTypeCountComparison(EventReturnType.Restart, client_type, comparison_type, value)


def GotoIfFlagState(label: Label, state: bool, flag_type: FlagType, flag: FlagInt):
    instruction_info = (1003, 101)
    return to_numeric(instruction_info, label, state, flag_type, flag)


def GotoIfThisEventOn(label: Label):
    return GotoIfFlagState(label, True, FlagType.RelativeToThisEvent, 0)


def GotoIfThisEventOff(label: Label):
    return GotoIfFlagState(label, False, FlagType.RelativeToThisEvent, 0)


def GotoIfThisEventSlotOn(label: Label):
    return GotoIfFlagState(label, True, FlagType.RelativeToThisEventSlot, 0)


def GotoIfThisEventSlotOff(label: Label):
    return GotoIfFlagState(label, False, FlagType.RelativeToThisEventSlot, 0)


def GotoIfFlagOn(label: Label, flag: FlagInt):
    return GotoIfFlagState(label, True, FlagType.Absolute, flag)


def GotoIfFlagOff(label: Label, flag: FlagInt):
    return GotoIfFlagState(label, False, FlagType.Absolute, flag)


def GotoIfFlagRangeState(label: Label, state: RangeState, flag_type: FlagType, flag_range: FlagRangeTyping):
    instruction_info = (1003, 103)
    first_flag, last_flag = tuple(flag_range)
    return to_numeric(instruction_info, label, state, flag_type, first_flag, last_flag)


def GotoIfFlagRangeAllOn(label: Label, flag_range: FlagRangeTyping):
    return GotoIfFlagRangeState(label, RangeState.AllOn, FlagType.Absolute, flag_range)


def GotoIfFlagRangeAllOff(label: Label, flag_range: FlagRangeTyping):
    return GotoIfFlagRangeState(label, RangeState.AllOff, FlagType.Absolute, flag_range)


def GotoIfFlagRangeAnyOn(label: Label, flag_range: FlagRangeTyping):
    return GotoIfFlagRangeState(label, RangeState.AnyOn, FlagType.Absolute, flag_range)


def GotoIfFlagRangeAnyOff(label: Label, flag_range: FlagRangeTyping):
    return GotoIfFlagRangeState(label, RangeState.AnyOff, FlagType.Absolute, flag_range)


def GotoIfMultiplayerState(label: Label, state: MultiplayerState):
    instruction_info = (1003, 105, [0, 0])
    return to_numeric(instruction_info, label, state)


def GotoIfHost(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Host)


def GotoIfClient(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Client)


def GotoIfTryingToCreateSession(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.TryingToCreateSession)


def GotoIfTryingToJoinSession(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.TryingToJoinSession)


def GotoIfLeavingSession(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.LeavingSession)


def GotoIfFailedToCreateSession(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.FailedToCreateSession)


def GotoIfMapPresenceState(label: Label, game_map: MapTyping, state: bool):
    instruction_info = (1003, 107, [0, 0, 0, 0])
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, label, state, area_id, block_id)


def GotoIfInsideMap(label: Label, game_map: MapTyping):
    return GotoIfMapPresenceState(label, game_map, True)


def GotoIfOutsideMap(label: Label, game_map: MapTyping):
    return GotoIfMapPresenceState(label, game_map, False)


def GotoIfCoopClientCountComparison(label: Label, comparison_type: ComparisonType, value: int):
    instruction_info = (1003, 109, [0, 0, 0])
    return to_numeric(instruction_info, label, comparison_type, value)


def ReturnIfCharacterSpecialEffectState(
    event_return_type: EventReturnType,
    character: CharacterTyping,
    special_effect: int,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: int = 1,
):
    instruction_info = (1003, 111)
    return to_numeric(
        instruction_info, event_return_type, character, special_effect, state, target_comparison_type, target_count
    )


def EndIfCharacterSpecialEffectState(character: CharacterTyping, special_effect: int, state: bool):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.End, character, special_effect, state)


def EndIfCharacterHasSpecialEffect(character: CharacterTyping, special_effect: int):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.End, character, special_effect, True)


def EndIfCharacterDoesNotHaveSpecialEffect(character: CharacterTyping, special_effect: int):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.End, character, special_effect, False)


def RestartIfCharacterSpecialEffectState(character: CharacterTyping, special_effect: int, state: bool):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.Restart, character, special_effect, state)


def RestartIfCharacterHasSpecialEffect(character: CharacterTyping, special_effect: int):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.Restart, character, special_effect, True)


def RestartIfCharacterDoesNotHaveSpecialEffect(character: CharacterTyping, special_effect: int):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.Restart, character, special_effect, False)


def EndIfPlayerHasSpecialEffect(special_effect: int):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.End, PLAYER, special_effect, True)


def EndIfPlayerDoesNotHaveSpecialEffect(special_effect: int):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.End, PLAYER, special_effect, False)


def RestartIfPlayerHasSpecialEffect(special_effect: int):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.Restart, PLAYER, special_effect, True)


def RestartIfPlayerDoesNotHaveSpecialEffect(special_effect: int):
    return ReturnIfCharacterSpecialEffectState(EventReturnType.Restart, PLAYER, special_effect, False)


def SkipLinesIfCharacterSpecialEffectState(
    line_count: int,
    character: CharacterTyping,
    special_effect: int,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: int = 1,
):
    instruction_info = (1003, 112, [0, 0, -1, 0, 0, 0])
    return to_numeric(
        instruction_info, line_count, character, special_effect, state, target_comparison_type, target_count
    )


def SkipLinesIfCharacterHasSpecialEffect(line_count: int, character: CharacterTyping, special_effect: int):
    return SkipLinesIfCharacterSpecialEffectState(line_count, character, special_effect, True)


def SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count: int, character: CharacterTyping, special_effect: int):
    return SkipLinesIfCharacterSpecialEffectState(line_count, character, special_effect, False)


def SkipLinesIfPlayerHasSpecialEffect(line_count: int, special_effect: int):
    return SkipLinesIfCharacterSpecialEffectState(line_count, PLAYER, special_effect, True)


def SkipLinesIfPlayerDoesNotHaveSpecialEffect(line_count: int, special_effect: int):
    return SkipLinesIfCharacterSpecialEffectState(line_count, PLAYER, special_effect, False)


def GotoIfCharacterRegionState(
    label: Label, state: bool, character: CharacterTyping, region: RegionTyping, min_target_count: int = 1
):
    """EMEDF does not have the final new argument listed (it's the same as the other region/distance checks)."""
    instruction_info = (1003, 200)
    return to_numeric(instruction_info, label, state, character, region, min_target_count)


def GotoIfCharacterInsideRegion(label: Label, character: CharacterTyping, region: RegionTyping):
    return GotoIfCharacterRegionState(label, True, character, region)


def GotoIfCharacterOutsideRegion(label: Label, character: CharacterTyping, region: RegionTyping):
    return GotoIfCharacterRegionState(label, False, character, region)


def ReturnIfCharacterRegionState(
    event_return_type: EventReturnType,
    state: bool,
    character: CharacterTyping,
    region: RegionTyping,
    min_target_count: int = 1,
):
    instruction_info = (1003, 201)
    return to_numeric(instruction_info, event_return_type, state, character, region, min_target_count)


def EndIfCharacterRegionState(state: bool, character: CharacterTyping, region: RegionTyping):
    return ReturnIfCharacterRegionState(EventReturnType.End, state, character, region)


def EndIfCharacterInsideRegion(character: CharacterTyping, region: RegionTyping):
    return ReturnIfCharacterRegionState(EventReturnType.End, True, character, region)


def EndIfCharacterOutsideRegion(character: CharacterTyping, region: RegionTyping):
    return ReturnIfCharacterRegionState(EventReturnType.End, False, character, region)


def RestartIfCharacterRegionState(state: bool, character: CharacterTyping, region: RegionTyping):
    return ReturnIfCharacterRegionState(EventReturnType.Restart, state, character, region)


def RestartIfCharacterInsideRegion(character: CharacterTyping, region: RegionTyping):
    return ReturnIfCharacterRegionState(EventReturnType.Restart, True, character, region)


def RestartIfCharacterOutsideRegion(character: CharacterTyping, region: RegionTyping):
    return ReturnIfCharacterRegionState(EventReturnType.Restart, False, character, region)


def SkipLinesIfCharacterRegionState(
    line_count: int, state: bool, character: CharacterTyping, region: RegionTyping, min_target_count: int = 1
):
    instruction_info = (1003, 202)
    return to_numeric(instruction_info, line_count, state, character, region, min_target_count)


def SkipLinesIfCharacterInsideRegion(line_count: int, character: CharacterTyping, region: RegionTyping):
    return SkipLinesIfCharacterRegionState(line_count, True, character, region)


def SkipLinesIfCharacterOutsideRegion(line_count: int, character: CharacterTyping, region: RegionTyping):
    return SkipLinesIfCharacterRegionState(line_count, False, character, region)


def GotoIfHollowArenaMatchType(label: Label, match_type: HollowArenaMatchType):
    instruction_info = (1003, 211)
    return to_numeric(instruction_info, label, match_type)


# 1005: CONTROL FLOW (OBJECTS)
# Adding new arguments.


def SkipLinesIfObjectDestructionState(
    line_count,
    obj: ObjectTyping,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """Note change in argument order."""
    instruction_info = (1005, 1)
    return to_numeric(instruction_info, line_count, state, obj, target_comparison_type, target_count)


def SkipLinesIfObjectDestroyed(line_count, obj: ObjectTyping):
    return SkipLinesIfObjectDestructionState(line_count, obj, True)


def SkipLinesIfObjectNotDestroyed(line_count, obj: ObjectTyping):
    return SkipLinesIfObjectDestructionState(line_count, obj, False)


def ReturnIfObjectDestructionState(
    event_return_type: EventReturnType,
    obj: ObjectTyping,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    instruction_info = (1005, 2)
    return to_numeric(instruction_info, event_return_type, state, obj, target_comparison_type, target_count)


def EndIfObjectDestroyed(obj: ObjectTyping):
    return ReturnIfObjectDestructionState(EventReturnType.End, obj, True)


def EndIfObjectNotDestroyed(obj: ObjectTyping):
    return ReturnIfObjectDestructionState(EventReturnType.End, obj, False)


def RestartIfObjectDestroyed(obj: ObjectTyping):
    return ReturnIfObjectDestructionState(EventReturnType.Restart, obj, True)


def RestartIfObjectNotDestroyed(obj: ObjectTyping):
    return ReturnIfObjectDestructionState(EventReturnType.Restart, obj, False)


def GotoIfObjectDestructionState(
    label: Label,
    obj: ObjectTyping,
    state: bool,
    target_comparison_type: ComparisonType = ComparisonType.Equal,
    target_count: float = 1.0,
):
    """Note change in argument order."""
    instruction_info = (1005, 101, [0, 0, 0, 0, 0])
    return to_numeric(instruction_info, label, state, obj, target_comparison_type, target_count)


def GotoIfObjectDestroyed(label: Label, obj: ObjectTyping):
    return GotoIfObjectDestructionState(label, obj, True)


def GotoIfObjectNotDestroyed(label: Label, obj: ObjectTyping):
    return GotoIfObjectDestructionState(label, obj, False)


# 1014: LABELS


def DefineLabel(label: tp.Union[Label, int]):
    """Ranges from 0 to 20, inclusive, for DS3."""
    if isinstance(Label, int) and not 0 <= label <= 20:
        raise ValueError("Label index must be between 0 and 20, inclusive.")
    instruction_info = (1014, label)
    return to_numeric(instruction_info)


# 2002: CUTSCENES


def PlayCutsceneAndMovePlayerAndSetTimePeriod(
    cutscene: int,
    cutscene_type: CutsceneFlags,
    move_to_region: RegionTyping,
    move_to_map: MapTyping,
    player_id: int,
    time_period_id: int,
):
    """Warp a particular player to a region and set the time period. I assume that this must be a map that is
    already loaded, like in DS1, but possibly not.

    It's probably used to warp to Bergenwerth after Rom, so either that map is already loaded when you defeat Rom, or
    this event *is* capable of warping to an entirely new map.
    """
    instruction_info = (2002, 6)
    area_id, block_id = tuple(move_to_map)
    return to_numeric(
        instruction_info, cutscene, cutscene_type, move_to_region, area_id, block_id, player_id, time_period_id
    )


def PlayCutsceneAndSetTimePeriod(cutscene: int, cutscene_type: CutsceneFlags, player_id: int, time_period_id: int):
    """Probably used when you examine Laurence's skull, etc."""
    instruction_info = (2002, 7, [-1, 0, -1, 0])
    return to_numeric(instruction_info, cutscene, cutscene_type, player_id, time_period_id)


def PlayCutsceneAndMovePlayer_Dummy(move_to_region: RegionTyping, move_to_map: MapTyping):
    """Likely not used, doesn't even take a cutscene ID argument."""
    instruction_info = (2002, 8, [0, 0, 0])
    area_id, block_id = tuple(move_to_map)
    return to_numeric(instruction_info, move_to_region, area_id, block_id)


def PlayCutsceneAndMovePlayerAndSetMapCeremony(
    cutscene: int,
    cutscene_type: CutsceneFlags,
    ceremony_id: int,
    unknown: int,
    move_to_region: RegionTyping,
    move_to_map: MapTyping,
    player_id: int,
):
    """I assume that this must be a map that is already loaded, like in DS1, but possibly not.

    Contains an unknown argument that may always be zero. TODO: Check.
    """
    instruction_info = (2002, 9)
    area_id, block_id = tuple(move_to_map)
    return to_numeric(
        instruction_info, cutscene, cutscene_type, ceremony_id, unknown, move_to_region, area_id, block_id, player_id
    )


def PlayCutsceneAndSetMapCeremony(
    cutscene: int, cutscene_type: CutsceneFlags, ceremony_id: int, unknown: int, player_id: int
):
    instruction_info = (2002, 10, [-1, 0, -1, 0])
    return to_numeric(instruction_info, cutscene, cutscene_type, ceremony_id, unknown, player_id)


def PlayCutsceneAndMovePlayer_WithUnknowns(
    cutscene: int,
    cutscene_type: CutsceneFlags,
    move_to_region: RegionTyping,
    move_to_map: MapTyping,
    player_id: int,
    unknown1: int,
    unknown2: int,
):
    """Unknown arguments at the end."""
    instruction_info = (2002, 11, [0, 0, 0, 0, 0, 0, 0, 0])
    area_id, block_id = tuple(move_to_map)
    return to_numeric(
        instruction_info, cutscene, cutscene_type, move_to_region, area_id, block_id, player_id, unknown1, unknown2
    )


def PlayCutsceneAndMovePlayer_WithSecondRegion(
    cutscene: int,
    cutscene_type: CutsceneFlags,
    move_to_region: RegionTyping,
    move_to_map: MapTyping,
    player_id: int,
    other_region: RegionTyping,
):
    """Takes a second Region argument with unknown purpose."""
    instruction_info = (2002, 12, [0, 0, 0, 0, 0, 0, 0])
    area_id, block_id = tuple(move_to_map)
    return to_numeric(
        instruction_info, cutscene, cutscene_type, move_to_region, area_id, block_id, player_id, other_region
    )


# 2003: EVENT


def SetBossHealthBarState(character: CharacterTyping, name: NPCNameTyping, slot, state: bool):
    """Argument order changed.

    Note: slot number can be 0-2 in DS3.
    """
    instruction_info = (2003, 11)
    if isinstance(slot, int) and slot not in (0, 1, 2):
        raise ValueError("Boss health bar slot must be 0, 1, or 2.")
    return to_numeric(instruction_info, state, character, slot, name)


def EnableBossHealthBar(character: CharacterTyping, name: NPCNameTyping, slot=0):
    """The character's health bar will appear at the bottom of the screen, with a name."""
    return SetBossHealthBarState(character, name, slot, True)


def DisableBossHealthBar(character: CharacterTyping, name: NPCNameTyping = 0, slot=0):
    """The character's health bar will disappear from the bottom of the screen.

    TODO: Confirm the below is still true in DS3 (disabling one disables all).
    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter, so only the
    first argument actually does anything. You're welcome to specify the name for clarity anyway (and vanilla events
    will show it when decompiled)."""
    return SetBossHealthBarState(character, name, slot, False)


def HandleMinibossDefeat(miniboss_id: int):
    instruction_info = (2003, 15, [0])
    return to_numeric(instruction_info, miniboss_id)


def ForceAnimation(
    entity: AnimatedTyping,
    animation_id: int,
    loop: bool = False,
    wait_for_completion: bool = False,
    skip_transition: bool = False,
    unknown1: int = 0,
    unknown2: float = 0.0,
):
    """TODO: Confirm default values for unknown1 and unknown2 so I can keep my other defaults and arg order."""
    instruction_info = (2003, 18, [0, -1, 0, 0, 0, 0, 0])
    return to_numeric(
        instruction_info, entity, animation_id, loop, wait_for_completion, skip_transition, unknown1, unknown2
    )


def Unknown_2003_27(arg1: int):
    """No information."""
    instruction_info = (2003, 27)
    return to_numeric(instruction_info, arg1)


def EventValueOperation(
    source_flag: FlagInt,
    source_flag_bit_count: int,
    operand: int,
    target_flag: FlagInt,
    target_flag_bit_count: int,
    calculation_type: CalculationType,
):
    """Performs a binary operation on the source flag and operand value, and stores the result in the target flag."""
    instruction_info = (2003, 41)
    return to_numeric(
        instruction_info,
        source_flag,
        source_flag_bit_count,
        operand,
        target_flag,
        target_flag_bit_count,
        calculation_type,
    )


def StoreItemAmountSpecifiedByFlagValue(item_type: ItemType, item: ItemTyping, flag: FlagInt, bit_count: int):
    """Stores some amount of items read from a flag array."""
    instruction_info = (2003, 42)
    return to_numeric(instruction_info, item_type, item, flag, bit_count)


def GivePlayerItemAmountSpecifiedByFlagValue(item_type: ItemType, item: ItemTyping, flag: FlagInt, bit_count: int):
    """Gives player some amount of items read from a flag array. Probably used when taking items out of storage
    (i.e. the reverse of the above instruction)."""
    instruction_info = (2003, 43)
    return to_numeric(instruction_info, item_type, item, flag, bit_count)


def SetDirectionDisplayState(state: bool):
    """Not sure what this is."""
    instruction_info = (2003, 44)
    return to_numeric(instruction_info, state)


def EnableDirectionDisplay():
    return SetDirectionDisplayState(True)


def DisableDirectionDisplay():
    return SetDirectionDisplayState(False)


def SetMapHitGridCorrespondence(
    collision: CollisionTyping, level: int, grid_coord_x: int, grid_coord_y: int, state: bool
):
    instruction_info = (2003, 45)
    return to_numeric(instruction_info, collision, level, grid_coord_x, grid_coord_y, state)


def EnableMapHitGridCorrespondence(collision: CollisionTyping, level: int, grid_coord_x: int, grid_coord_y: int):
    return SetMapHitGridCorrespondence(collision, level, grid_coord_x, grid_coord_y, True)


def DisableMapHitGridCorrespondence(collision: CollisionTyping, level: int, grid_coord_x: int, grid_coord_y: int):
    return SetMapHitGridCorrespondence(collision, level, grid_coord_x, grid_coord_y, False)


def SetMapContentImageDisplayState(content_image_part_id: int, state: bool):
    instruction_info = (2003, 46)
    return to_numeric(instruction_info, content_image_part_id, state)


def SetMapBoundariesDisplay(hierarchy: int, grid_coord_x: int, grid_coord_y: int, state: bool):
    instruction_info = (2003, 47)
    return to_numeric(instruction_info, hierarchy, grid_coord_x, grid_coord_y, state)


def SetAreaWind(region: RegionTyping, state: bool, duration: float, wind_parameter_id: int):
    instruction_info = (2003, 48)
    return to_numeric(instruction_info, region, state, duration, wind_parameter_id)


def WarpPlayerToRespawnPoint(respawn_point_id: int):
    instruction_info = (2003, 49, [0])
    return to_numeric(instruction_info, respawn_point_id)


def StartEnemySpawner(spawner_id: int):
    instruction_info = (2003, 50, [-1])
    return to_numeric(instruction_info, spawner_id)


def SummonNPC(
    sign_type: tp.Union[SingleplayerSummonSignType, int],
    character: CharacterTyping,
    region: RegionTyping,
    summon_flag: FlagInt,
    dismissal_flag: FlagInt,
):
    instruction_info = (2003, 51)
    return to_numeric(instruction_info, sign_type, character, region, summon_flag, dismissal_flag)


def InitializeWarpObject(warp_object_id: int):
    instruction_info = (2003, 52, [0])
    return to_numeric(instruction_info, warp_object_id)


def MakeEnemyAppear(character: CharacterTyping):
    instruction_info = (2003, 54)
    return to_numeric(instruction_info, character)


def SetCurrentMapCeremony(ceremony_id: int):
    instruction_info = (2003, 57)
    return to_numeric(instruction_info, ceremony_id)


def SetMapCeremony(game_map: MapTyping, ceremony_id: int):
    instruction_info = (2003, 59)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, area_id, block_id, ceremony_id)


def DisplayEpitaphMessage(message: EventTextTyping):
    instruction_info = (2003, 61)
    return to_numeric(instruction_info, message)


def SetNetworkConnectedFlagState(flag: FlagInt, state: FlagState):
    instruction_info = (2003, 62)
    return to_numeric(instruction_info, flag, state)


def SetNetworkConnectedFlagRangeState(flag_range: FlagRangeTyping, state: RangeState):
    instruction_info = (2003, 63)
    first_flag, last_flag = tuple(flag_range)
    return to_numeric(instruction_info, first_flag, last_flag, state)


def SetOmissionModeCounts(level_1_count: int, level_2_count: int):
    instruction_info = (2003, 64)
    return to_numeric(instruction_info, level_1_count, level_2_count)


def ResetOmissionModeCountsToDefault():
    instruction_info = (2003, 65)
    return to_numeric(instruction_info)


def InitializeCrowTrade(
    item_type: ItemType,
    item_id: ItemTyping,
    item_lot_id: ItemLotTyping,
    trade_completed_flag: FlagInt,
    crow_response_flag: FlagInt,
):
    instruction_info = (2003, 66)
    return to_numeric(instruction_info, item_type, item_id, item_lot_id, trade_completed_flag, crow_response_flag)


def InitializeCrowTradeRegion(region: RegionTyping):
    instruction_info = (2003, 67)
    return to_numeric(instruction_info, region)


def SetNetworkInteractionState(state: bool):
    instruction_info = (2003, 70)
    return to_numeric(instruction_info, state)


def SetHUDVisibilityState(is_invisible: bool):
    instruction_info = (2003, 71)
    return to_numeric(instruction_info, is_invisible)


def EnableHUDVisibility():
    return SetHUDVisibilityState(False)


def DisableHUDVisibility():
    return SetHUDVisibilityState(True)


def SetBonfireWarpingState(bonfire_obj: ObjectTyping, animation: int, state: bool):
    instruction_info = (2003, 72)
    return to_numeric(instruction_info, bonfire_obj, animation, state)


def EnableBonfireWarping(bonfire_obj: ObjectTyping, animation: int):
    return SetBonfireWarpingState(bonfire_obj, animation, True)


def DisableBonfireWarping(bonfire_obj: ObjectTyping, animation: int):
    return SetBonfireWarpingState(bonfire_obj, animation, False)


def SetAutogeneratedEventSpecificFlag_1(unknown1: int, unknown2: int):
    """No idea, but probably relates to setting the flag whose ID matches the event ID."""
    instruction_info = (2003, 73)
    return to_numeric(instruction_info, unknown1, unknown2)


def HandleBossDefeatAndDisplayBanner(boss: int, banner: BannerType):
    """Not sure if the 'boss' is a GameAreaParam or just Character."""
    instruction_info = (2003, 74)
    return to_numeric(instruction_info, boss, banner)


def SetAutogeneratedEventSpecificFlag_2(unknown1: int, unknown2: int):
    """No idea, but probably relates to setting the flag whose ID matches the event ID."""
    instruction_info = (2003, 75)
    return to_numeric(instruction_info, unknown1, unknown2)


def SetLoadingScreenTipsState(tips_disabled: bool):
    instruction_info = (2003, 76)
    return to_numeric(instruction_info, tips_disabled)


def EnableLoadingScreenTips():
    return SetLoadingScreenTipsState(False)


def DisableLoadingScreenTips():
    return SetLoadingScreenTipsState(True)


def AwardGestureItem(gesture_id: int, item_type: ItemType, item_id: int):
    """Not sure if this awards an actual gesture (then why multiple args?) or awards it based on a gesture (but then
    why not region-specific?)."""
    instruction_info = (2003, 77)
    return to_numeric(instruction_info, gesture_id, item_type, item_id)


def SendNPCSummonHome(character: CharacterTyping):
    """Identical to Bloodborne version, but with different index."""
    instruction_info = (2003, 78, [-1])
    return to_numeric(instruction_info, character)


def Unknown_2003_79(unknown1: int):
    instruction_info = (2003, 79)
    return to_numeric(instruction_info, unknown1)


def SetDecoratedBossHealthBarState(
    state: bool, character: CharacterTyping, slot: int, name: EventTextTyping, decoration: int
):
    """Pretty cool; not sure when this is used in the vanilla game or what decorations are available (apparently 255).
    As in Bloodborne, slot must be from 0 to 2."""
    if not 0 <= slot <= 2:
        raise ValueError("Boss health bar slot must be between 0 (lowermost) and 2 (uppermost). ")
    instruction_info = (2003, 80)
    return to_numeric(instruction_info, state, character, slot, name, decoration)


def EnableDecoratedBossHealthBar(character: CharacterTyping, slot: int, name: EventTextTyping, decoration: int):
    return SetDecoratedBossHealthBarState(True, character, slot, name, decoration)


def DisableDecoratedBossHealthBar(character: CharacterTyping, slot: int, name: EventTextTyping, decoration: int):
    return SetDecoratedBossHealthBarState(False, character, slot, name, decoration)


def PlaceNPCSummonSign_WithoutEmber(
    sign_type: SummonSignType,
    character: CharacterTyping,
    region: RegionTyping,
    summon_flag: FlagInt,
    dismissal_flag: FlagInt,
):
    instruction_info = (2003, 81)
    return to_numeric(instruction_info, sign_type, character, region, summon_flag, dismissal_flag)


# 2004: CHARACTER


def AddSpecialEffect(character: CharacterTyping, special_effect_id: int):
    """'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will do
    nothing if the character already has the special effect active (i.e. they do not stack or even reset timers).

    This version is the same as DS1, without the extra argument added in Bloodborne.
    """
    instruction_info = (2004, 8)
    return to_numeric(instruction_info, character, special_effect_id)


def RotateToFaceEntity(
    character: CharacterTyping, target_entity: CoordEntityTyping, animation: int, wait_for_completion: bool = False
):
    """Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at least.)

    The Bloodborne version allows you to force an animation at the same time and optionally wait until that animation
    is completed. (I assume a value of -1 avoids it.)
    """
    instruction_info = (2004, 14, [0, 0, 0, 0])
    return to_numeric(instruction_info, character, target_entity, animation, wait_for_completion)


def ChangeCharacterCloth(character: CharacterTyping, bit_count: int, state_id: int):
    instruction_info = (2004, 48, [0, 0, 0])
    return to_numeric(instruction_info, character, bit_count, state_id)


def ChangePatrolBehavior(character: CharacterTyping, patrol_information_id: int):
    """I don't know what a 'patrol_information_id' actually is."""
    instruction_info = (2004, 49, [0, 0])
    return to_numeric(instruction_info, character, patrol_information_id)


def SetLockOnPoint(character: CharacterTyping, lock_on_model_point: int, state: bool):
    """Presumably changes the point that is locked on to by the player."""
    instruction_info = (2004, 50)
    return to_numeric(instruction_info, character, lock_on_model_point, state)


def Test_RequestRagdollRestraint(
    recipient_character: CharacterTyping,
    recipient_target_rigid_index: int,
    recipient_model_point: int,
    attachment_character: CharacterTyping,
    attachment_target_rigid_index: int,
    attachment_model_point: int,
):
    instruction_info = (2004, 51)
    return to_numeric(
        instruction_info,
        recipient_character,
        recipient_target_rigid_index,
        recipient_model_point,
        attachment_character,
        attachment_target_rigid_index,
        attachment_model_point,
    )


def ChangePlayerCharacterInitParam(character_init_param: int):
    """I assume this affects the player."""
    instruction_info = (2004, 52, [0])
    return to_numeric(instruction_info, character_init_param)


def AdaptSpecialEffectHealthChangeToNPCPart(character: CharacterTyping):
    instruction_info = (2004, 53, [-1])
    return to_numeric(instruction_info, character)


def ImmediateActivate(character: CharacterTyping, state: bool):
    """Not sure. Sets draw state *really* quickly?"""
    instruction_info = (2004, 54)
    return to_numeric(instruction_info, character, state)


def SetCharacterTalkRange(character: CharacterTyping, distance: float):
    instruction_info = (2004, 55)
    return to_numeric(instruction_info, character, distance)


def IncrementCharacterNewGameCycle(character: CharacterTyping):
    """Interesting - apparently you can increase the NG+ level of a specific character. (No reset function, but it
    would probably reset on map reload.)"""
    instruction_info = (2004, 57)
    return to_numeric(instruction_info, character)


def SetMultiplayerBuffs_NonBoss(character: CharacterTyping, state: bool):
    instruction_info = (2004, 58)
    return to_numeric(instruction_info, character, state)


def Unknown_2004_59(character: CharacterTyping, state: bool):
    """Examine usage."""
    instruction_info = (2004, 59)
    return to_numeric(instruction_info, character, state)


def SetPlayerRemainingYoelLevels(level_count: int):
    instruction_info = (2004, 60)
    return to_numeric(instruction_info, level_count)


# 2005: OBJECT


def ExtinguishBurningObjects():
    instruction_info = (2005, 16)
    return to_numeric(instruction_info)


def ShowObjectByMapCeremony(obj: ObjectTyping, ceremony_id: int, unknown: int):
    instruction_info = (2005, 17)
    return to_numeric(instruction_info, obj, ceremony_id, unknown)


def DestroyObject_NoSlot(obj: ObjectTyping):
    """No 'slot' argument here."""
    instruction_info = (2005, 19)
    return to_numeric(instruction_info, obj)


# 2007: MESSAGE


def DisplayDialogAndSetFlags(
    message: EventTextTyping,
    button_type: ButtonType,
    number_buttons: NumberButtons,
    anchor_entity: CoordEntityTyping,
    display_distance: float,
    left_flag: FlagInt,
    right_flag: FlagInt,
    cancel_flag: FlagInt,
):
    """Displays a dialog and enables one of three flags, depending on the player's response. Very useful."""
    instruction_info = (2007, 10, [0, 0, 0, -1, 0, 0, 0, 0])
    return to_numeric(
        instruction_info,
        message,
        button_type,
        number_buttons,
        anchor_entity,
        display_distance,
        left_flag,
        right_flag,
        cancel_flag,
    )


def DisplayAreaWelcomeMessage(message: EventTextTyping):
    """Not sure what this looks like exactly."""
    instruction_info = (2007, 11)
    return to_numeric(instruction_info, message)


def DisplayHollowArenaMessage(message: EventTextTyping, unknown: int, pad_enabled: bool):
    instruction_info = (2007, 12)
    return to_numeric(instruction_info, message, unknown, pad_enabled)


# 2009: SCRIPT


def RegisterHealingFountain(
    flag: FlagInt,
    obj: ObjectTyping,
    reaction_distance: float,
    reaction_angle: float,
    initial_sword_number: int,
    sword_level: int,
):
    """No idea what this is. Apparently DS1 also has a version of this with less arguments."""
    instruction_info = (2009, 5)
    return to_numeric(instruction_info, flag, obj, reaction_distance, reaction_angle, initial_sword_number, sword_level)


def BanishInvaders(unknown: int):
    instruction_info = (2009, 8)
    return to_numeric(instruction_info, unknown)


def BanishPhantomsAndUpdateServerPvPStats(unknown: int):
    instruction_info = (2009, 10)
    return to_numeric(instruction_info, unknown)


def BanishPhantoms(unknown: int):
    instruction_info = (2009, 11)
    return to_numeric(instruction_info, unknown)


# 2010: SOUND


def SetBossMusicState(sound_id: int, state: bool):
    """Not sure how this differs from the standard map sound instructions."""
    instruction_info = (2010, 4, [0, 0])
    return to_numeric(instruction_info, sound_id, state)


def EnableBossMusic(sound_id: int):
    return SetBossMusicState(sound_id, True)


def DisableBossMusic(sound_id: int):
    return SetBossMusicState(sound_id, False)


def NotifyDoorEventSoundDampening(entity_id: int, state: DoorState):
    """No idea what this is or what entity the first argument is. Probably the door object."""
    instruction_info = (2010, 5, [0, 0])
    return to_numeric(instruction_info, entity_id, state)


def SetSoundEventWithFade(sound_id: int, state: bool, fade_duration: float):
    instruction_info = (2010, 6)
    return to_numeric(instruction_info, sound_id, state, fade_duration)


def EnableSoundEventWithFade(sound_id: int, fade_duration: float):
    return SetSoundEventWithFade(sound_id, True, fade_duration)


def DisableSoundEventWithFade(sound_id: int, fade_duration: float):
    return SetSoundEventWithFade(sound_id, False, fade_duration)


def Unknown_2010_07(sound_id: int):
    """Unknown SoundEvent instruction."""
    instruction_info = (2010, 7)
    return to_numeric(instruction_info, sound_id)


# 2011: Collision


def SetCollisionResState(collision: CollisionTyping, state: bool):
    """No idea what this is."""
    instruction_info = (2011, 3, [-1, 0])
    return to_numeric(instruction_info, collision, state)


def ActivateCollisionAndCreateNavmesh(collision: CollisionTyping, state: bool):
    instruction_info = (2011, 4)
    return to_numeric(instruction_info, collision, state)


# MAP

# 2012: MAP


def SetAreaWelcomeMessageState(state: bool):
    instruction_info = (2012, 8)
    return to_numeric(instruction_info, state)


def EnableAreaWelcomeMessage():
    return SetAreaWelcomeMessageState(True)


def DisableAreaWelcomeMessage():
    return SetAreaWelcomeMessageState(False)


# 2013: PLAY LOG


def CreatePlayLog(name: StringOffsetTyping):
    instruction_info = (2013, 1, [0])
    return to_numeric(instruction_info, name)


def StartPlayLogMeasurement(measurement_id: int, name: StringOffsetTyping, overwrite: bool):
    instruction_info = (2013, 2, [0, 0, 0])
    return to_numeric(instruction_info, measurement_id, name, overwrite)


def StopPlayLogMeasurement(measurement_id: int):
    instruction_info = (2013, 3, [0])
    return to_numeric(instruction_info, measurement_id)


def PlayLogParameterOutput(
    category: PlayerPlayLogParameter, name: StringOffsetTyping, output_multiplayer_state: PlayLogMultiplayerType
):
    instruction_info = (2013, 4, [0, 0, 0])
    return to_numeric(instruction_info, category, name, output_multiplayer_state)
