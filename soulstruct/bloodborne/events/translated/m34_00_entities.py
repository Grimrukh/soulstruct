"""HUNTER'S NIGHTMARE"""
from soulstruct.game_types import *


class Flags(Flag):
    LudwigDead = 13401800
    LudwigFirstTimeDone = 13401801
    LudwigAnnouncerDead = 13401803
    LudwigFogEntered = 13404808
    LudwigBattleStarted = 13404802
    LudwigPhaseTwo = 13404825

    LaurenceDead = 13401850
    LaurenceFirstTimeDone = 13401851
    LaurenceFogEntered = 13404858
    LaurenceBattleStarted = 13404860


class Characters(Character):
    LudwigTheAccursed = 3400800
    LudwigTheHolyBlade = 3400801
    LudwigAnnouncer = 3400810  # corpse in Ludwig's arena
    Laurence = 3400850
    LudwigHead = 3400900


class Objects(Object):
    LudwigFog = 3401800
    LaurenceFog = 3401850


class Regions(Region):
    LudwigPhaseTwoStart = 3402806
    PlayerStartAfterLudwigTransformation = 3402807
    LudwigTheAccursedRetires = 3402900


class VFX(VFXEvent):
    LudwigFog = 3403800
    LaurenceFog = 3403850


class Cutscenes(IntEnum):
    LaurenceAwakening = 34000010
    LudwigTransformation = 34000030
