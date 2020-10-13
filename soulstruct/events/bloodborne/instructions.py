"""Full instruction set for Bloodborne."""
from __future__ import annotations

from typing import Union

from soulstruct.game_types import *
from soulstruct.events.numeric import to_numeric
from soulstruct.events.shared.instructions import *
from soulstruct.enums.bloodborne import *

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
    # Bloodborne extra instructions (tests mixed in)
    "IfDamageType",
    "IfActionButtonInRegion",
    "IfPlayerArmorType",
    "IfPlayerInsightAmountComparison",
    "IfPlayerInsightAmountEqual",
    "IfPlayerInsightAmountNotEqual",
    "IfPlayerInsightAmountGreaterThan",
    "IfPlayerInsightAmountLessThan",
    "IfPlayerInsightAmountGreaterThanOrEqual",
    "IfPlayerInsightAmountLessThanOrEqual",
    "IfDialogChoice",
    "IfPlayGoState",
    "IfClientTypeCountComparison",
    "IfCharacterDrawGroupState",
    "IfCharacterDrawGroupActive",
    "IfCharacterDrawGroupInactive",
    "GotoIfConditionState",
    "GotoIfConditionTrue",
    "GotoIfConditionFalse",
    "Goto",
    "GotoIfValueComparison",
    "GotoIfFinishedConditionState",
    "GotoIfFinishedConditionTrue",
    "GotoIfFinishedConditionFalse",
    "SkipLinesIfCoopClientCountComparison",
    "TerminateIfCoopClientCountComparison",
    "EndIfCoopClientCountComparison",
    "RestartIfCoopClientCountComparison",
    "SkipLinesIfPlayerGender",
    "GotoIfPlayerGender",
    "TerminateIfPlayerGender",
    "EndIfPlayerGender",
    "RestartIfPlayerGender",
    "SkipLinesIfClientTypeCountComparison",
    "GotoIfClientTypeCountComparison",
    "TerminateIfClientTypeCountComparison",
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
    "GotoIfMultiplayer",
    "GotoIfConnectingMultiplayer",
    "GotoIfSingleplayer",
    "GotoIfMapPresenceState",
    "GotoIfInsideMap",
    "GotoIfOutsideMap",
    "GotoIfCoopClientCountComparison",
    "GotoIfObjectDestructionState",
    "GotoIfObjectDestroyed",
    "GotoIfObjectNotDestroyed",
    "SkipLinesIfMultiplayerState",
    "SkipLinesIfHost",
    "SkipLinesIfClient",
    "SkipLinesIfMultiplayer",
    "SkipLinesIfConnectingMultiplayer",
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
    "IfConnectingMultiplayer",
    "IfSingleplayer",
    "DefineLabel",
    "PlayCutsceneAndMovePlayerAndSetTimePeriod",
    "PlayCutsceneAndSetTimePeriod",
    "PlayCutsceneAndMovePlayer_Dummy",
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
    "BossDefeat",
    "SendNPCSummonHome",
    "AddSpecialEffect",
    "RotateToFaceEntity",
    "ChangeCharacterCloth",
    "ChangePatrolBehavior",
    "SetDistanceLimitForConversationStateChanges",
    "Test_RequestRagdollRestraint",
    "ChangePlayerCharacterInitParam",
    "AdaptSpecialEffectHealthChangeToNPCPart",
    "SetGravityAndCollisionExcludingOwnWorld",
    "AddSpecialEffect_WithUnknownEffect",
    "ActivateObjectWithSpecificCharacter",
    "SetObjectDamageShieldState",
    "RegisterLantern",
    "SetBossMusicState",
    "EnableBossMusic",
    "DisableBossMusic",
    "NotifyDoorEventSoundDampening",
    "SetCollisionResState",
    "CreatePlayLog",
    "StartPlayLogMeasurement",
    "StopPlayLogMeasurement",
    "PlayLogParameterOutput",
]

from soulstruct.game_types import ItemTyping, ArmorTyping


def IfDamageType(
    condition: int, attacked_entity: AnimatedTyping, attacking_character: CharacterTyping, damage_type: DamageType
):
    """Similar to IsAttackedBy, but requires a certain damage type."""
    instruction_info = (3, 23, [0, 0, -1, 0])
    return to_numeric(instruction_info, condition, attacked_entity, attacking_character, damage_type)


def IfActionButtonInRegion(condition: int, action_button_id: int, region: RegionTyping):
    """Probably a simplified version of `IfActionButton`. Used with boss fog."""
    instruction_info = (3, 24, [0, -1, -1])
    return to_numeric(instruction_info, condition, action_button_id, region)


def IfPlayerArmorType(
    condition: int, armor_type: ArmorTyping, required_armor_range_first: ArmorTyping,
    required_armor_range_last: ArmorTyping,
):
    instruction_info = (3, 25, [0])
    return to_numeric(instruction_info, condition, armor_type, required_armor_range_first, required_armor_range_last)


def IfPlayerInsightAmountComparison(condition: int, value: int, comparison_type: ComparisonType):
    """Note change in argument order."""
    instruction_info = (3, 26, [0, 0, 0])
    return to_numeric(instruction_info, condition, value, comparison_type)


def IfPlayerInsightAmountEqual(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.Equal)


def IfPlayerInsightAmountNotEqual(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.NotEqual)


def IfPlayerInsightAmountGreaterThan(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.GreaterThan)


def IfPlayerInsightAmountLessThan(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.LessThan)


def IfPlayerInsightAmountGreaterThanOrEqual(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.GreaterThanOrEqual)


def IfPlayerInsightAmountLessThanOrEqual(condition: int, value: int):
    return IfPlayerInsightAmountComparison(condition, value, ComparisonType.LessThanOrEqual)


def IfDialogChoice(condition: int, dialog_result: DialogResult):
    instruction_info = (3, 27, [0, 0])
    return to_numeric(instruction_info, condition, dialog_result)


def IfPlayGoState(condition: int, playgo_state: PlayGoState):
    """No idea what PlayGo state is but this doesn't sound like it would be used very often."""
    instruction_info = (3, 28, [0, 0])
    return to_numeric(instruction_info, condition, playgo_state)


def IfClientTypeCountComparison(condition: int, client_type: ClientType, comparison_type: ComparisonType, value):
    """Value should only range between 0 and 4 (the maximum number of clients)."""
    instruction_info = (3, 29, [0, 0, 0, 0])
    return to_numeric(instruction_info, condition, client_type, comparison_type, value)


def IfCharacterDrawGroupState(condition: int, character: CharacterTyping, state: bool):
    """Tests if character's draw group is currently active or inactive."""
    instruction_info = (4, 15, [0, 0, 0])
    return to_numeric(instruction_info, condition, character, state)


def IfCharacterDrawGroupActive(condition: int, character: CharacterTyping):
    return IfCharacterDrawGroupState(condition, character, True)


def IfCharacterDrawGroupInactive(condition: int, character: CharacterTyping):
    return IfCharacterDrawGroupState(condition, character, False)


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


def SkipLinesIfCoopClientCountComparison(skip_lines: int, comparison_type: ComparisonType, value: int):
    """Value should be from 0 to 4."""
    instruction_info = (1003, 9, [0, 0, 0])
    return to_numeric(instruction_info, skip_lines, comparison_type, value)


def TerminateIfCoopClientCountComparison(event_end_type: EventEndType, comparison_type: ComparisonType, value: int):
    instruction_info = (1003, 10, [0, 0, 0])
    return to_numeric(instruction_info, event_end_type, comparison_type, value)


def EndIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return TerminateIfCoopClientCountComparison(EventEndType.End, comparison_type, value)


def RestartIfCoopClientCountComparison(comparison_type: ComparisonType, value: int):
    return TerminateIfCoopClientCountComparison(EventEndType.Restart, comparison_type, value)


def SkipLinesIfPlayerGender(skip_lines: int, gender: Gender):
    instruction_info = (1003, 11)
    return to_numeric(instruction_info, skip_lines, gender)


def GotoIfPlayerGender(label: Label, gender: Gender):
    instruction_info = (1003, 12)
    return to_numeric(instruction_info, label, gender)


def TerminateIfPlayerGender(event_end_type: EventEndType, gender: Gender):
    instruction_info = (1003, 13)
    return to_numeric(instruction_info, event_end_type, gender)


def EndIfPlayerGender(gender: Gender):
    return TerminateIfPlayerGender(EventEndType.End, gender)


def RestartIfPlayerGender(gender: Gender):
    return TerminateIfPlayerGender(EventEndType.Restart, gender)


def SkipLinesIfClientTypeCountComparison(
    skip_lines: int, client_type: ClientType, comparison_type: ComparisonType, value: int
):
    """Value from 0 to 4."""
    instruction_info = (1003, 14, [0, 0, 0, 0])
    return to_numeric(instruction_info, skip_lines, client_type, comparison_type, value)


def GotoIfClientTypeCountComparison(label: Label, client_type: ClientType, comparison_type: ComparisonType, value: int):
    """Value from 0 to 4."""
    instruction_info = (1003, 15, [0, 0, 0, 0])
    return to_numeric(instruction_info, label, client_type, comparison_type, value)


def TerminateIfClientTypeCountComparison(
    event_end_type: EventEndType, client_type: ClientType, comparison_type: ComparisonType, value: int
):
    """Value from 0 to 4."""
    instruction_info = (1003, 16, [0, 0, 0, 0])
    return to_numeric(instruction_info, event_end_type, client_type, comparison_type, value)


def EndIfClientTypeCountComparison(client_type: ClientType, comparison_type: ComparisonType, value: int):
    """Value from 0 to 4."""
    return TerminateIfClientTypeCountComparison(EventEndType.End, client_type, comparison_type, value)


def RestartIfClientTypeCountComparison(client_type: ClientType, comparison_type: ComparisonType, value: int):
    """Value from 0 to 4."""
    return TerminateIfClientTypeCountComparison(EventEndType.Restart, client_type, comparison_type, value)


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


def GotoIfMultiplayer(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Multiplayer)


def GotoIfConnectingMultiplayer(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.ConnnectingMultplayer)


def GotoIfSingleplayer(label: Label):
    return GotoIfMultiplayerState(label, MultiplayerState.Singleplayer)


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


def GotoIfObjectDestructionState(label: Label, obj: ObjectTyping, state: bool):
    """Note change in argument order."""
    instruction_info = (1005, 101, [0, 0, -1])
    return to_numeric(instruction_info, label, state, obj)


def GotoIfObjectDestroyed(label: Label, obj: ObjectTyping):
    return GotoIfObjectDestructionState(label, obj, True)


def GotoIfObjectNotDestroyed(label: Label, obj: ObjectTyping):
    return GotoIfObjectDestructionState(label, obj, False)


# MULTIPLAYER


def SkipLinesIfMultiplayerState(line_count, state: MultiplayerState):
    instruction_info = (1003, 5)
    return to_numeric(instruction_info, line_count, state)


def SkipLinesIfHost(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Host)


def SkipLinesIfClient(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Client)


def SkipLinesIfMultiplayer(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Multiplayer)


def SkipLinesIfConnectingMultiplayer(skip_lines: int):
    return SkipLinesIfMultiplayerState(skip_lines, MultiplayerState.ConnectingMultiplayer)


def SkipLinesIfSingleplayer(line_count):
    return SkipLinesIfMultiplayerState(line_count, MultiplayerState.Singleplayer)


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


def RestartIfHost():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Host)


def RestartIfClient():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Client)


def RestartIfMultiplayer():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Multiplayer)


def RestartIfSingleplayer():
    return TerminateIfMultiplayerState(EventEndType.Restart, MultiplayerState.Singleplayer)


def IfMultiplayerState(condition: int, state: MultiplayerState):
    instruction_info = (3, 6)
    return to_numeric(instruction_info, condition, state)


def IfHost(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Host)


def IfClient(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Client)


def IfMultiplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Multiplayer)


def IfConnectingMultiplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.ConnectingMultiplayer)


def IfSingleplayer(condition: int):
    return IfMultiplayerState(condition, MultiplayerState.Singleplayer)


def DefineLabel(label: Union[Label, int]):
    if isinstance(Label, int) and not 0 <= label <= 9:
        raise ValueError("Label index must be between 0 and 9, inclusive.")
    instruction_info = (1014, label)
    return to_numeric(instruction_info)


def PlayCutsceneAndMovePlayerAndSetTimePeriod(
    cutscene: int,
    cutscene_type: CutsceneType,
    region: RegionTyping,
    game_map: MapTyping,
    player_id: int,
    time_period_id: int,
):
    """Warp a particular player to a region and set the time period. I assume that this must be a map that is
    already loaded, like in DS1, but possibly not.

    It's probably used to warp to Bergenwerth after Rom, so either that map is already loaded when you defeat Rom, or
    this event *is* capable of warping to an entirely new map.
    """
    instruction_info = (2002, 6)
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, cutscene, cutscene_type, region, area_id, block_id, player_id, time_period_id)


def PlayCutsceneAndSetTimePeriod(cutscene: int, cutscene_type: CutsceneType, player_id: int, time_period_id: int):
    """Probably used when you examine Laurence's skull, etc."""
    instruction_info = (2002, 7, [-1, 0, -1, 0])
    return to_numeric(instruction_info, cutscene, cutscene_type, player_id, time_period_id)


def PlayCutsceneAndMovePlayer_Dummy(region: RegionTyping, game_map: MapTyping):
    """Likely not used, doesn't even take a cutscene ID argument."""
    instruction_info = (2002, 8, [0, 0, 0])
    area_id, block_id = tuple(game_map)
    return to_numeric(instruction_info, region, area_id, block_id)


def SetBossHealthBarState(character: CharacterTyping, name: EventTextTyping, slot, state: bool):
    """Note: slot number can be 0-2 in Bloodborne."""
    instruction_info = (2003, 11)
    if isinstance(slot, int) and slot not in (0, 1, 2):
        raise ValueError("Boss health bar slot must be 0, 1, or 2.")
    return to_numeric(instruction_info, state, character, slot, name)


def EnableBossHealthBar(character: CharacterTyping, name: EventTextTyping, slot=0):
    """The character's health bar will appear at the bottom of the screen, with a name."""
    return SetBossHealthBarState(character, name, slot, True)


def DisableBossHealthBar(character: CharacterTyping, name: EventTextTyping = 0, slot=0):
    """The character's health bar will disappear from the bottom of the screen.

    WARNING: Disabling either boss health will disable both of them, and the name_id doesn't matter, so only the
    first argument actually does anything. You're welcome to specify the name for clarity anyway (and vanilla events
    will show it when decompiled)."""
    return SetBossHealthBarState(character, name, slot, False)


def HandleMinibossDefeat(miniboss_id: int):
    """Called instead of "KillBoss" for bosses that aren't the final boss of the area.

    Note that outside of Chalice Dungeons, this is ONLY used when you have defeated Gehrman and are about to fight Moon
    Presence."""
    instruction_info = (2003, 15, [0])
    return to_numeric(instruction_info, miniboss_id)


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
    collision: CollisionTyping,
    level: int,
    grid_coord_x: int,
    grid_coord_y: int,
    state: bool,
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
    sign_type: Union[SingleplayerSummonSignType, int],
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


def BossDefeat(boss_id: int, banner_type: BannerType):
    """Handle boss defeat and display banner. 'boss_id' is probably similar to GameAreaParam from DS1."""
    instruction_info = (2003, 53)
    return to_numeric(instruction_info, boss_id, banner_type)


def SendNPCSummonHome(character: CharacterTyping):
    instruction_info = (2003, 54, [-1])
    return to_numeric(instruction_info, character)


def AddSpecialEffect(character: CharacterTyping, special_effect_id: int, affect_npc_part_hp: bool):
    """'Special effect' as in a buff/debuff, not graphical effects (though they may come with one). This will do
    nothing if the character already has the special effect active (i.e. they do not stack or even reset timers).

    The Bloodborne version has an additional argument that determines whether any HP changes caused by the special
    effect should also affect NPC parts.
    """
    instruction_info = (2004, 8)
    return to_numeric(instruction_info, character, special_effect_id, affect_npc_part_hp)


def RotateToFaceEntity(
    character: CharacterTyping, target_entity: CoordEntityTyping, animation: int, wait_for_completion: bool = False
):
    """Rotate a character to face a target map entity of any type.
    WARNING: This instruction will crash its event script (silently) if used on a disabled character! (In DS1 at least.)

    The Bloodborne version allows you to force an animation at the same time (post-rotation) and optionally wait until
    that animation is completed. (I assume a value of -1 avoids it.)
    """
    instruction_info = (2004, 14, [0, 0, -1, 0])
    return to_numeric(instruction_info, character, target_entity, animation, wait_for_completion)


def ChangeCharacterCloth(character: CharacterTyping, bit_count: int, state_id: int):
    instruction_info = (2004, 48, [0, 0, 0])
    return to_numeric(instruction_info, character, bit_count, state_id)


def ChangePatrolBehavior(character: CharacterTyping, patrol_information_id: int):
    """I don't know what a 'patrol_information_id' actually is."""
    instruction_info = (2004, 49, [0, -1])
    return to_numeric(instruction_info, character, patrol_information_id)


def SetDistanceLimitForConversationStateChanges(character: CharacterTyping, distance: float):
    instruction_info = (2004, 50)
    return to_numeric(instruction_info, character, distance)


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


def SetGravityAndCollisionExcludingOwnWorld(character: CharacterTyping, state: bool):
    """I assume "own world" refers to the world you're hosting."""
    instruction_info = (2004, 54, [-1, 0])
    return to_numeric(instruction_info, character, state)


def AddSpecialEffect_WithUnknownEffect(character: CharacterTyping, special_effect: int, affect_npc_parts_hp: bool):
    """Unknown additional affect from the standard instruction, presumably."""
    instruction_info = (2004, 55)
    return to_numeric(instruction_info, character, special_effect, affect_npc_parts_hp)


def ActivateObjectWithSpecificCharacter(
    obj: ObjectTyping,
    objact_id: int,
    relative_index: int,
    character: CharacterTyping,
):
    """The standard version of this 'grabs' the nearest character and uses them in the ObjAct (e.g. Patches pulling the
    lever in the Catacombs in DS1). I presume this version lets you specify which character should be involved in the
    ObjAct."""
    instruction_info = (2005, 16, [-1, 0, 0, -1])
    return to_numeric(instruction_info, obj, objact_id, relative_index, character)


def SetObjectDamageShieldState(obj: ObjectTyping, state: bool):
    """Not sure how this differs from object invulnerability."""
    instruction_info = (2005, 17, [-1, 0])
    return to_numeric(instruction_info, obj, state)


def RegisterLantern(
    flag: FlagInt,
    obj: ObjectTyping,
    reaction_distance: float,
    reaction_angle: float,
    initial_sword_number: int = 0,
    sword_level: int = 0,
):
    """Register a Lantern. Used instead of the bonfire registration.

    No idea what the 'sword' arguments do, but they default to zero.
    """
    instruction_info = (2009, 5)
    return to_numeric(instruction_info, flag, obj, reaction_distance, reaction_angle, initial_sword_number, sword_level)


def SetBossMusicState(sound_id: int, state: bool):
    """Not sure how this differs from the standard map sound instructions, but my guess is that it fades the music out
    rather than abruptly stopping it.

    TODO: Can probably be used to fade out ANY music. Not sure why it would only work for boss music.
    TODO: Argument -1 is sometimes used. Fades out ALL music?
    """
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


def SetCollisionResState(collision: CollisionTyping, state: bool):
    """No idea what this is."""
    instruction_info = (2011, 3, [-1, 0])
    return to_numeric(instruction_info, collision, state)


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
