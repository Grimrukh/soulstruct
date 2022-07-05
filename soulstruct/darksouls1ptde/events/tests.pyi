"""AUTOMATICALLY GENERATED. Do not edit this module.

Import this into any EVS script to have full access to tests.
Make sure you also do `from soulstruct.{game}.events import *` to get all enums and constants.
"""

__all__ = [
    "ValueEqual",
    "ValueNotEqual",
    "ValueGreaterThan",
    "ValueLessThan",
    "ValueGreaterThanOrEqual",
    "ValueLessThanOrEqual",
    "FlagEnabled",
    "FlagDisabled",
    "ThisEventFlagEnabled",
    "ThisEventFlagDisabled",
    "ThisEventSlotFlagEnabled",
    "ThisEventSlotFlagDisabled",
    "FlagRangeAllEnabled",
    "FlagRangeAllDisabled",
    "FlagRangeAnyEnabled",
    "FlagRangeAnyDisabled",
    "PlayerInsideRegion",
    "PlayerOutsideRegion",
    "CharacterInsideRegion",
    "CharacterOutsideRegion",
    "PlayerWithinDistance",
    "PlayerBeyondDistance",
    "EntityWithinDistance",
    "EntityBeyondDistance",
    "Host",
    "Client",
    "Multiplayer",
    "Singleplayer",
    "AllPlayersInsideRegion",
    "AllPlayersOutsideRegion",
    "InsideMap",
    "OutsideMap",
    "TrueFlagCountEqual",
    "TrueFlagCountNotEqual",
    "TrueFlagCountGreaterThan",
    "TrueFlagCountLessThan",
    "TrueFlagCountGreaterThanOrEqual",
    "TrueFlagCountLessThanOrEqual",
    "WhiteWorldTendencyComparison",
    "BlackWorldTendencyComparison",
    "WhiteWorldTendencyGreaterThanOrEqual",
    "BlackWorldTendencyGreaterThanOrEqual",
    "EventValueEqual",
    "EventValueNotEqual",
    "EventValueGreaterThan",
    "EventValueLessThan",
    "EventValueGreaterThanOrEqual",
    "EventValueLessThanOrEqual",
    "NewGameCycleEqual",
    "NewGameCycleNotEqual",
    "NewGameCycleGreaterThan",
    "NewGameCycleLessThan",
    "NewGameCycleGreaterThanOrEqual",
    "NewGameCycleLessThanOrEqual",
    "DLCOwned",
    "DLCNotOwned",
    "Online",
    "Offline",
    "CharacterDead",
    "CharacterAlive",
    "HealthEqual",
    "HealthNotEqual",
    "HealthGreaterThan",
    "HealthLessThan",
    "HealthGreaterThanOrEqual",
    "HealthLessThanOrEqual",
    "CharacterHuman",
    "CharacterWhitePhantom",
    "CharacterHollow",
    "CharacterTargeting",
    "CharacterNotTargeting",
    "PlayerHasSpecialEffect",
    "PlayerDoesNotHaveSpecialEffect",
    "CharacterHasSpecialEffect",
    "CharacterDoesNotHaveSpecialEffect",
    "CharacterPartHealthLessThanOrEqual",
    "CharacterBackreadEnabled",
    "CharacterBackreadDisabled",
    "CharacterHasTAEEvent",
    "CharacterDoesNotHaveTAEEvent",
    "SkullLanternActive",
    "SkullLanternInactive",
    "PlayerLevelEqual",
    "PlayerLevelNotEqual",
    "PlayerLevelGreaterThan",
    "PlayerLevelLessThan",
    "PlayerLevelGreaterThanOrEqual",
    "PlayerLevelLessThanOrEqual",
    "HealthValueEqual",
    "HealthValueNotEqual",
    "HealthValueGreaterThan",
    "HealthValueLessThan",
    "HealthValueGreaterThanOrEqual",
    "HealthValueLessThanOrEqual",
    "ObjectDestroyed",
    "ObjectNotDestroyed",
]

from soulstruct.darksouls1ptde.game_types import *
from .emevd.compiler import *
from .emevd.enums import *


def ValueEqual(left: int, right: int):
    ...


def ValueNotEqual(left: int, right: int):
    ...


def ValueGreaterThan(left: int, right: int):
    ...


def ValueLessThan(left: int, right: int):
    ...


def ValueGreaterThanOrEqual(left: int, right: int):
    ...


def ValueLessThanOrEqual(left: int, right: int):
    ...


def FlagEnabled(flag: Flag | int):
    ...


def FlagDisabled(flag: Flag | int):
    ...


def ThisEventFlagEnabled():
    ...


def ThisEventFlagDisabled():
    ...


def ThisEventSlotFlagEnabled():
    ...


def ThisEventSlotFlagDisabled():
    ...


def FlagRangeAllEnabled(flag_range: FlagRange | tuple | list):
    ...


def FlagRangeAllDisabled(flag_range: FlagRange | tuple | list):
    ...


def FlagRangeAnyEnabled(flag_range: FlagRange | tuple | list):
    ...


def FlagRangeAnyDisabled(flag_range: FlagRange | tuple | list):
    ...


def PlayerInsideRegion(region: Region | int):
    ...


def PlayerOutsideRegion(region: Region | int):
    ...


def CharacterInsideRegion(character: Character | Object | int, region: Region | int):
    ...


def CharacterOutsideRegion(character: Character | Object | int, region: Region | int):
    ...


def PlayerWithinDistance(other_entity: Object | Region | Character | int, radius: float):
    ...


def PlayerBeyondDistance(other_entity: Object | Region | Character | int, radius: float):
    ...


def EntityWithinDistance(
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
):
    ...


def EntityBeyondDistance(
    entity: Object | Region | Character | int,
    other_entity: Object | Region | Character | int,
    radius: float,
):
    ...


def Host():
    ...


def Client():
    ...


def Multiplayer():
    ...


def Singleplayer():
    ...


def AllPlayersInsideRegion(region: Region | int):
    ...


def AllPlayersOutsideRegion(region: Region | int):
    ...


def InsideMap(game_map: Map | tuple | list):
    ...


def OutsideMap(game_map: Map | tuple | list):
    ...


def TrueFlagCountEqual(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int):
    ...


def TrueFlagCountNotEqual(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int):
    ...


def TrueFlagCountGreaterThan(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int):
    ...


def TrueFlagCountLessThan(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int):
    ...


def TrueFlagCountGreaterThanOrEqual(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int):
    ...


def TrueFlagCountLessThanOrEqual(flag_type: FlagType | int, flag_range: FlagRange | tuple | list, value: int):
    ...


def WhiteWorldTendencyComparison(comparison_type: ComparisonType | int, value: int):
    ...


def BlackWorldTendencyComparison(comparison_type: ComparisonType | int, value: int):
    ...


def WhiteWorldTendencyGreaterThanOrEqual(value: int):
    ...


def BlackWorldTendencyGreaterThanOrEqual(value: int):
    ...


def EventValueEqual(flag: Flag | int, bit_count: int, value: int):
    ...


def EventValueNotEqual(flag: Flag | int, bit_count: int, value: int):
    ...


def EventValueGreaterThan(flag: Flag | int, bit_count: int, value: int):
    ...


def EventValueLessThan(flag: Flag | int, bit_count: int, value: int):
    ...


def EventValueGreaterThanOrEqual(flag: Flag | int, bit_count: int, value: int):
    ...


def EventValueLessThanOrEqual(flag: Flag | int, bit_count: int, value: int):
    ...


def NewGameCycleEqual(completion_count: int):
    ...


def NewGameCycleNotEqual(completion_count: int):
    ...


def NewGameCycleGreaterThan(completion_count: int):
    ...


def NewGameCycleLessThan(completion_count: int):
    ...


def NewGameCycleGreaterThanOrEqual(completion_count: int):
    ...


def NewGameCycleLessThanOrEqual(completion_count: int):
    ...


def DLCOwned():
    ...


def DLCNotOwned():
    ...


def Online():
    ...


def Offline():
    ...


def CharacterDead(character: Character | int):
    ...


def CharacterAlive(character: Character | int):
    ...


def HealthEqual(character: Character | int, value: float):
    ...


def HealthNotEqual(character: Character | int, value: float):
    ...


def HealthGreaterThan(character: Character | int, value: float):
    ...


def HealthLessThan(character: Character | int, value: float):
    ...


def HealthGreaterThanOrEqual(character: Character | int, value: float):
    ...


def HealthLessThanOrEqual(character: Character | int, value: float):
    ...


def CharacterHuman(character: Character | int):
    ...


def CharacterWhitePhantom(character: Character | int):
    ...


def CharacterHollow(character: Character | int):
    ...


def CharacterTargeting(targeting_character: Character | int, targeted_character: Character | int):
    ...


def CharacterNotTargeting(targeting_character: Character | int, targeted_character: Character | int):
    ...


def PlayerHasSpecialEffect(special_effect: int):
    ...


def PlayerDoesNotHaveSpecialEffect(special_effect: int):
    ...


def CharacterHasSpecialEffect(character: Character | int, special_effect: int):
    ...


def CharacterDoesNotHaveSpecialEffect(character: Character | int, special_effect: int):
    ...


def CharacterPartHealthLessThanOrEqual(character: Character | int, npc_part_id: int, value: float):
    ...


def CharacterBackreadEnabled(character: Character | int):
    ...


def CharacterBackreadDisabled(character: Character | int):
    ...


def CharacterHasTAEEvent(character: Character | int, tae_event_id: int):
    ...


def CharacterDoesNotHaveTAEEvent(character: Character | int, tae_event_id: int):
    ...


def SkullLanternActive():
    ...


def SkullLanternInactive():
    ...


def PlayerLevelEqual(value: int):
    ...


def PlayerLevelNotEqual(value: int):
    ...


def PlayerLevelGreaterThan(value: int):
    ...


def PlayerLevelLessThan(value: int):
    ...


def PlayerLevelGreaterThanOrEqual(value: int):
    ...


def PlayerLevelLessThanOrEqual(value: int):
    ...


def HealthValueEqual(character: Character | int, value: int):
    ...


def HealthValueNotEqual(character: Character | int, value: int):
    ...


def HealthValueGreaterThan(character: Character | int, value: int):
    ...


def HealthValueLessThan(character: Character | int, value: int):
    ...


def HealthValueGreaterThanOrEqual(character: Character | int, value: int):
    ...


def HealthValueLessThanOrEqual(character: Character | int, value: int):
    ...


def ObjectDestroyed(obj: Object | int):
    ...


def ObjectNotDestroyed(obj: Object | int):
    ...
