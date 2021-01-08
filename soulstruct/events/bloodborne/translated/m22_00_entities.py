"""HEMWICK CHARNEL LANE"""
from soulstruct.game_types import *


class Flags(Flag):
    WitchesOfHemwickDead = 12201800
    WitchesOfHemwickFirstTimeDone = 12201802
    WitchesOfHemwickFogEntered = 12204800
    WitchesOfHemwickFogEnteredAsSummon = 12204801
    WitchesOfHemwickBattleStarted = 12204802
    PlayerHasZeroInsight = 12204845


class Characters(Character):
    WomanInWitchAbode1 = 2200270
    WomanInWitchAbode2 = 2200271
    WomanInWitchAbode3 = 2200272
    Executioner1 = 2200340
    Executioner2 = 2200341
    Executioner3 = 2200280  # guarding chest
    FirstWitchOfHemwick = 2200800
    SecondWitchOfHemwick = 2200801
    BossMadOne1 = 2200811
    BossMadOne2 = 2200812
    BossMadOne3 = 2200813


class Objects(Object):
    GateToCharnelLane = 2201001
    ShortcutGate = 2201002
    DoorToRuneTool = 2201060
    CorpseWithRuneTool = 2201151
    ShortcutElevatorUpperLever = 2201200
    ShortcutElevatorLowerLever = 2201201
    ShortcutElevator = 2201210
    ShortcutGateLever = 2201220
    CainhurstCarriage = 2201310
    BossEntryFogGate = 2201800
    BossExitFogGate = 2201801


class ItemLots(ItemLotParam):
    WitchesOfHemwickReward = 21002950


class VFX(VFXEvent):
    BossEntryFog = 2203800
    BossExitFog = 2203801


class Music(MusicSound):
    BossPhase1 = 2203802
    BossPhase2 = 2203803
