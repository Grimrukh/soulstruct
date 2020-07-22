from soulstruct.game_types import *


class FLAG(Flag):
    pass


class CHR(Character):
    PrinceLorianWithoutLothric = 3410832
    PrinceLorianWithLothric = 3410830
    PrinceLothric = 3410831


class TEXT(Text):
    PrinceLorianName = 905250
    PrinceLothicName = 905251


class SOUND(SFXSound):
    BossDeath = 777777777


EVENT_NAMES = {
    13415830: "StartTwinPrincesBossFight",
    13415841: "MoveLothricToLorian",
    13410832: "TwinPrincesDeath",
    # Common functions. These event IDs are generally contiguous, so I assume they don't use flags.
    # Numerous variants of AI triggers. All of them trigger AI, and all of them trigger if the character in question is
    # attacked. The variants allow you to trigger them based on a radius from the player and/or when the player enters a
    # region, with an optional animation, with or without the addition of a gravity trigger (e.g. for falling slimes) or
    # a forced animation. There's also one that triggers if an arbitrary character's AI is in the Battle state, and one
    # that triggers on attack only (e.g. a sleeping enemy).
    20005110: "TriggerAIWithRegion",
    20005111: "TriggerAIAndAnimationWithRegion",
    20005112: "TriggerAIAndGravityWithRegion",
    20005113: "TriggerAIAndGravityWithRegionAfterDelay",
    20005114: "TriggerAIWithRegionAfterDelay",
    20005119: "TriggerAIWithRegions",
    20005120: "TriggerAIWithinDistance",
    20005121: "TriggerAIWithinDistanceAfterDelay",
    20005122: "TriggerAIAndAnimationWithinDistance",
    20005130: "TriggerAIWithinDistanceAndRegion",
    20005131: "TriggerAIAndAnimationWithinDistanceOrRegion",
    20005132: "TriggerAIWithinDistanceOrRegion",
    20005133: "TriggerAIAndAnimationWithinDistanceOrRegion",
    20005134: "TriggerAIWithinDistanceOrRegionWithAnimationInRegionOnly",
    20005140: "TriggerAIWithinRegionOrIfCharacterIsFighting",
    20005150: "TriggerAIOnAttackOnly",
    20005192: "RemoveSpEffect99006WithinRegion",
    20005190: "RemoveSpEffect99006WithinDistance",
    20005191: "RemoveSpEffect99006OnAttackOnly",
    20005200: "InterruptAnimationWithinRegion",
    20005350: "AwardItemLotOnCharacterDeath",
    20005530: "BurnObject",
    20005611: "EnableFlagWhenObjectActivated",
}
