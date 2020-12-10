"""RESEARCH HALL"""
from soulstruct.game_types import *


class Flags(Flag):
    LadyMariaDead = 13501800
    LadyMariaFirstTimeDone = 13501801
    LadyMariaFogEntered = 13504808
    LadyMariaBattleStarted = 13504802

    LivingFailuresDead = 13501850
    LivingFailuresFirstTimeDone = 13501851
    LivingFailuresFogEntered = 13504858
    LivingFailuresBattleStarted = 13504860
    LivingFailuresMeteorRequest = 13504866  # enabled while meteor attack is ongoing
    LivingFailuresFirstMeteorAttackDone = 13504868
    LivingFailuresMeteorAttackAvailable = 13504869  # at 60% HP
    RemainingLivingFailuresKilled = 13504895  # basically equivalent to Dead flag; enabled by first slot of LF cleanup
    LivingFailureSpawnRequest = 13505668
    ActiveLivingFailuresCountRequest = 13505669
    LivingFailuresPhaseTwo = 13504870  # enabled when meteor attack is first used


class Characters(Character):
    LadyMaria = 3500800
    LadyMariaFriendly = 3500905

    LivingFailuresHealthPool = 3500850
    LivingFailure1 = 3500851
    LivingFailure2 = 3500852
    LivingFailure3 = 3500853
    LivingFailure4 = 3500854
    LivingFailureMeteorCreator = 3500860


class Objects(Object):
    LadyMariaFog = 3501800
    LivingFailuresFog = 3501810


class FX(FXEvent):
    LadyMariaFog = 3503800
    LivingFailuresFog = 3503810


class Cutscenes(IntEnum):
    LadyMariaAwakening = 35000010
