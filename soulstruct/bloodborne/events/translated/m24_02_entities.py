"""UPPER CATHEDRAL WARD"""
from soulstruct.game_types import *


class Flags(Flag):
    EbrietasDead = 12421800
    EbrietasFirstTimeDone = 12421802
    EbrietasFogEntered = 12424800
    EbrietasBattleStarted = 12424802

    CelestialEmissaryDead = 12421700
    CelestialEmissaryFirstTimeDone = 12421702
    CelestialEmissaryFogEntered = 12424700
    CelestialEmissaryBattleStarted = 12424702
    CelestialEmissaryPhaseTwo = 12424790


class Characters(Character):
    CelestialMinion1 = 2420711
    CelestialMinion2 = 2420712
    CelestialMinion3 = 2420713
    CelestialMinion4 = 2420716
    CelestialMinion5 = 2420717
    CelestialMinion6 = 2420719
    CelestialMinion7 = 2420720

    Ebrietas = 2420800
    CelestialEmissarySmall = 2420810
    CelestialEmissaryGiant = 2420811


class Objects(Object):
    EbrietasFog = 2421800
    CelestialEmissaryEntranceFog = 2421700
    CelestialEmissaryExitFog = 2421701


class VFX(VFXEvent):
    EbrietasFog = 2423800
    CelestialEmissaryEntranceFog = 2423810
    CelestialEmissaryExitFog = 2423811


class Effects(SpecialEffectParam):
    CelestialEmissaryAura = 5530
    EbrietasStarsActive = 5650
