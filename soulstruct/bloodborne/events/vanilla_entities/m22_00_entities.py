"""HEMWICK CHARNEL LANE"""
from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    12201800: ("WitchesOfHemwickDie", "Witches of Hemwick are killed."),
    12201801: ("PlayWitchesOfHemwickDeathSound", "Event 12201801"),
    12201803: ("DisableBossMadOneSpawners", "Disable spawners and kill remaining Mad Ones when boss is dead."),
    12201804: ("SummonStartWitchesOfHemwickBattle", "First Witch appears."),
    12204890: ("EnterWitchesOfHemwickBossFog", "Event 12204890"),
    12204891: ("EnterWitchesOfHemwickBossFogAsSummon", "Event 12204891"),
    12204892: ("Event12204892", "Event 12204892"),
    12204893: ("Event12204893", "Event 12204893"),
    12204802: ("StartWitchesOfHemwickBossBattle", "Event 12204802"),
    12204803: ("ControlWitchesOfHemwickMusic", "Event 12204803"),
    12204804: ("ToggleWitchesOfHemwickCamera", "Event 12204804"),
    12204805: ("StopWitchesOfHemwickBossMusic", "Event 12204805"),
    12204807: ("EnableSecondWitchOfHemwickHealthBar", "Event 12204807"),
    12204808: ("ControlWitchOpacity", "Event 12204808"),
    12204810: ("ActivateSecondWitchOfHemwick", "Event 12204810"),
    12204811: ("AggravateFirstWitchOfHemwick", "Event 12204811"),
    12204812: ("ResurrectWitch", "Resurrect (and warp) first witch after 45 seconds if second witch isn't dead."),
    12204814: ("RequestRandomWitchOfHemwickWarp", "Event 12204814"),
    12204830: ("MakeWitchReappear", "Event 12204830"),
    12204832: ("CountBossMadOneDeaths", "Event 12204832"),
    12204838: ("RespawnBossMadOne", "Event 12204838"),
    12204839: ("SpawnBossMadOnesForFirstTime", "Event 12204839"),
    12204840: ("WitchesSummonOneMadOne", "Event 12204840"),
    12204841: ("WitchesSummonTwoMadOnes", "Event 12204841"),
    12204842: ("WitchesSummonThreeMadOnes", "Event 12204842"),
    12204844: ("MonitorZeroInsight", "Enables a flag as long as player has 0 insight."),
    12200100: ("Event12200100", "Event 12200100"),
    12200101: ("Event12200101", "Event 12200101"),
    12200110: ("Event12200110", "Event 12200110"),
    12200111: ("Event12200111", "Event 12200111"),
    12200112: ("Event12200112", "Event 12200112"),
    12200120: ("Event12200120", "Event 12200120"),
    12200121: ("Event12200121", "Event 12200121"),
    12200122: ("Event12200122", "Event 12200122"),
    12200123: ("Event12200123", "Event 12200123"),
    12200124: ("Event12200124", "Event 12200124"),
    12200130: ("Event12200130", "Event 12200130"),
    12200131: ("Event12200131", "Event 12200131"),
    12200132: ("Event12200132", "Event 12200132"),
    12200150: ("Event12200150", "Event 12200150"),
    12200210: ("Event12200210", "Event 12200210"),
    12200220: ("Event12200220", "Event 12200220"),
    12200300: ("Event12200300", "Event 12200300"),
    12200310: ("Event12200310", "Event 12200310"),
    12204000: ("Event12204000", "Event 12204000"),
    12204010: ("Event12204010", "Event 12204010"),
    12205000: ("Event12205000", "Event 12205000"),
    12205001: ("Event12205001", "Event 12205001"),
    12205002: ("Event12205002", "Event 12205002"),
    12205003: ("Event12205003", "Event 12205003"),
    12205010: ("Event12205010", "Event 12205010"),
    12205015: ("Event12205015", "Event 12205015"),
    12205040: ("Event12205040", "Event 12205040"),
    12205041: ("Event12205041", "Event 12205041"),
    12205020: ("Event12205020", "Event 12205020"),
    12205030: ("Event12205030", "Event 12205030"),
    12205031: ("Event12205031", "Event 12205031"),
    12205050: ("Event12205050", "Event 12205050"),
    12205051: ("Event12205051", "Event 12205051"),
    12205060: ("Event12205060", "Event 12205060"),
    12205070: ("Event12205070", "Event 12205070"),
    12205080: ("Event12205080", "Event 12205080"),
    12205100: ("Event12205100", "Event 12205100"),
    12205105: ("Event12205105", "Event 12205105"),
    12205110: ("Event12205110", "Event 12205110"),
    12205120: ("Event12205120", "Event 12205120"),
    12205150: ("Event12205150", "Event 12205150"),
    12205160: ("Event12205160", "Event 12205160"),
    12205170: ("Event12205170", "Event 12205170"),
    12205200: ("Event12205200", "Event 12205200"),
    12205210: ("Event12205210", "Event 12205210"),
    12205220: ("Event12205220", "Event 12205220"),
    12205230: ("Event12205230", "Event 12205230"),
    12205240: ("Event12205240", "Event 12205240"),
    12205250: ("Event12205250", "Event 12205250"),
    12205260: ("Event12205260", "Event 12205260"),
    12205265: ("Event12205265", "Event 12205265"),
    12205270: ("Event12205270", "Event 12205270"),
    12205300: ("Event12205300", "Event 12205300"),
    12200990: ("Event12200990", "Event 12200990"),
}


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
