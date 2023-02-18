"""BYRGENWERTH"""
from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    13200010: ("Event13200010", "Event 13200010"),
    13200020: ("Event13200020", "Event 13200020"),
    13200030: ("Event13200030", "Event 13200030"),
    13200040: ("Event13200040", "Event 13200040"),
    13200050: ("Event13200050", "Event 13200050"),
    13200055: ("Event13200055", "Event 13200055"),
    13200060: ("Event13200060", "Event 13200060"),
    13200100: ("Event13200100", "Event 13200100"),
    13200102: ("Event13200102", "Event 13200102"),
    13200103: ("Event13200103", "Event 13200103"),
    13200105: ("Event13200105", "Event 13200105"),
    13200106: ("Event13200106", "Event 13200106"),
    13200107: ("Event13200107", "Event 13200107"),
    13200108: ("Event13200108", "Event 13200108"),
    13200109: ("Event13200109", "Event 13200109"),
    13200110: ("Event13200110", "Event 13200110"),
    13200120: ("Event13200120", "Event 13200120"),
    13200121: ("Event13200121", "Event 13200121"),
    13200200: ("Event13200200", "Event 13200200"),
    13200310: ("Event13200310", "Event 13200310"),
    13200311: ("Event13200311", "Event 13200311"),
    13200400: ("Event13200400", "Event 13200400"),
    13200500: ("Event13200500", "Event 13200500"),
    13200990: ("Event13200990", "Event 13200990"),
    13201800: ("RomDies", "Event 13201800"),
    13201801: ("PlayRomDeathSound", "Event 13201801"),
    13201802: ("RomFirstTime", "Event 13201802"),
    13201803: ("TriggerBloodMoon", "Trigger blood moon by approaching Queen Yharnam after Rom is defeated."),
    13201804: ("SummonStartRomBattle", "Event 13201804"),
    13204050: ("KillRomSpider", "Event 13204050"),
    13204100: ("Event13204100", "Event 13204100"),
    13204730: ("SetSpiderEventTarget", "Event 13204730"),
    13204830: ("EnterRomFog", "Event 13204830"),
    13204831: ("EnterRomFogAsSummon", "Event 13204831"),
    13204832: ("Event13204832", "Event 13204832"),
    13204833: ("Event13204833", "Event 13204833"),
    13204834: ("Event13204834", "Event 13204834"),
    13204802: ("StartRomBattle", "Event 13204802"),
    13204803: ("ControlRomMusic", "Event 13204803"),
    13204804: ("ControlRomCamera", "Event 13204804"),
    13204805: ("StopRomMusic", "Event 13204805"),
    13204807: ("RomTeleportsAway", "Rom teleports away at 75% then 50% health."),
    13204808: ("RomWeakPoint1Damage", "Not sure exactly which body part this refers to. Tail?"),
    13204809: ("RomWeakPoint2Damage", "Event 13204809"),
    13204810: ("RomHeadDamage", "Guessing this is the head from the 0.5 damage multipliers."),
    13204820: ("FallIntoMoonsideLake", "Event 13204820"),
    13204821: ("FallIntoMoonsideAsSummon", "Event 13204821"),
    13205000: ("Event13205000", "Event 13205000"),
    13205040: ("Event13205040", "Event 13205040"),
    13205050: ("Event13205050", "Event 13205050"),
    13205060: ("Event13205060", "Event 13205060"),
    13205080: ("Event13205080", "Event 13205080"),
    13205100: ("Event13205100", "Event 13205100"),
    13205140: ("Event13205140", "Event 13205140"),
    13205200: ("Event13205200", "Event 13205200"),
    13205300: ("Event13205300", "Event 13205300"),
    13205600: ("Event13205600", "Event 13205600"),
    13205630: ("Event13205630", "Event 13205630"),
    13205660: ("Event13205660", "Event 13205660"),
    13200950: ("Event13200950", "Event 13200950"),
    13200960: ("Event13200960", "Event 13200960"),
    13204450: ("Event13204450", "Event 13204450"),
    13204470: ("Event13204470", "Event 13204470"),
    13204400: ("Event13204400", "Event 13204400"),
    13204401: ("Event13204401", "Event 13204401"),
    13204402: ("Event13204402", "Event 13204402"),
    13204410: ("Event13204410", "Event 13204410"),
    13204460: ("Event13204460", "Event 13204460"),
}


class Flags(Flag):
    RomDead = 13201800
    RomFirstTimeDone = 13201802
    RomLakeEntered = 13204800  # instead of FogEntered
    RomBattleStarted = 13204802
    RomTeleportedOnce = 13204811
    RomTeleportedTwice = 13204812


class Characters(Character):
    Rom = 3200800
    QueenYharnam = 3200801


class Objects(Object):
    RomFog = 3201800


class Regions(Region):
    RomSecondPoint = 3202806
    RomThirdPoint = 3202807


class VFX(VFXEvent):
    RomFog = 3203800
