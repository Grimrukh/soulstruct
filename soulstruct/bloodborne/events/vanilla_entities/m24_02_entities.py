"""UPPER CATHEDRAL WARD"""
from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    12420700: ("Event12420700", "Event 12420700"),
    12421800: ("EbrietasDies", "Ebrietas, Daughter of the Cosmos is defeated."),
    12421801: ("Event12421801", "Event 12421801"),
    12421802: ("EbrietasFirstTime", "Event 12421802"),
    12421803: ("SummonStartEbrietasBattle", "Event 12421803"),
    12424810: ("EnterEbrietasFog", "Event 12424810"),
    12424811: ("EnterEbrietasFogAsSummon", "Event 12424811"),
    12424812: ("Event12424812", "Event 12424812"),
    12424813: ("Event12424813", "Event 12424813"),
    12424802: ("StartEbrietasBattle", "Event 12424802"),
    12424803: ("ControlEbrietasMusic", "Event 12424803"),
    12424804: ("ControlEbrietasCamera", "Event 12424804"),
    12424805: ("StopEbrietasMusic", "Event 12424805"),
    12424870: ("EbrietasHeadDamage", "Event 12424870"),
    12424871: ("EbrietasLimbDamage", "Event 12424871"),
    12424980: ("EbrietasPhaseTwoTrigger", "Event 12424980"),
    12424990: ("DismissEbrietasStarsOnDeath", "Event 12424990"),
    12421700: ("CelestialEmissaryDies", "Event 12421700"),
    12421701: ("PlayCelestialEmissaryDeathSound", "Event 12421701"),
    12421702: ("CelestialEmissaryFirstTime", "Event 12421702"),
    12421703: ("SummonStartCelestialEmissaryBattle", "Event 12421703"),
    12424710: ("EnterCelestialEmissaryFog", "Event 12424710"),
    12424711: ("EnterCelestialEmissaryFogAsSummon", "Event 12424711"),
    12424712: ("Event12424712", "Event 12424712"),
    12424713: ("Event12424713", "Event 12424713"),
    12424702: ("StartCelestialEmissaryBattle", "Event 12424702"),
    12424703: ("ControlCelestialEmissaryMusic", "Event 12424703"),
    12424704: ("ControlCelestialEmissaryCamera", "Event 12424704"),
    12424705: ("StopCelestialEmissaryMusic", "Event 12424705"),
    12424770: ("Event12424770", "Event 12424770"),
    12424780: ("ApplyCelestialEmissaryAura", "Minion aliens get buff from Celestial Emissary action."),
    12424785: ("Event12424785", "Event 12424785"),
    12424787: ("Event12424787", "Event 12424787"),
    12424784: ("Event12424784", "Event 12424784"),
    12424790: ("CelestialEmissaryPhaseTwoTrigger", "Event 12424790"),
    12424791: ("ControlCelestialEmissaryTendrils", "Event 12424791"),
    12424792: ("CelestialEmissaryTendrilAttack", "Event 12424792"),
    12424795: ("Event12424795", "Event 12424795"),
    12420000: ("Event12420000", "Event 12420000"),
    12420030: ("Event12420030", "Event 12420030"),
    12420050: ("Event12420050", "Event 12420050"),
    12420100: ("Event12420100", "Event 12420100"),
    12420123: ("Event12420123", "Event 12420123"),
    12420124: ("Event12420124", "Event 12420124"),
    12420130: ("Event12420130", "Event 12420130"),
    12420140: ("Event12420140", "Event 12420140"),
    12420150: ("Event12420150", "Event 12420150"),
    12420151: ("Event12420151", "Event 12420151"),
    12420152: ("Event12420152", "Event 12420152"),
    12420153: ("Event12420153", "Event 12420153"),
    12420156: ("Event12420156", "Event 12420156"),
    12420280: ("Event12420280", "Event 12420280"),
    12420285: ("Event12420285", "Event 12420285"),
    12420300: ("Event12420300", "Event 12420300"),
    12420310: ("Event12420310", "Event 12420310"),
    12420320: ("Event12420320", "Event 12420320"),
    12420400: ("Event12420400", "Event 12420400"),
    12420500: ("Event12420500", "Event 12420500"),
    12420850: ("Event12420850", "Event 12420850"),
    12420853: ("Event12420853", "Event 12420853"),
    12420854: ("Event12420854", "Event 12420854"),
    12425200: ("Event12425200", "Event 12425200"),
    12425210: ("Event12425210", "Event 12425210"),
    12425221: ("Event12425221", "Event 12425221"),
    12425250: ("Event12425250", "Event 12425250"),
    12425225: ("Event12425225", "Event 12425225"),
    12425245: ("Event12425245", "Event 12425245"),
    12425290: ("Event12425290", "Event 12425290"),
    12425300: ("Event12425300", "Event 12425300"),
    12425305: ("Event12425305", "Event 12425305"),
    12425310: ("Event12425310", "Event 12425310"),
    12425320: ("Event12425320", "Event 12425320"),
    12425350: ("Event12425350", "Event 12425350"),
    12425500: ("Event12425500", "Event 12425500"),
    12425600: ("Event12425600", "Event 12425600"),
    12425601: ("Event12425601", "Event 12425601"),
    12425602: ("Event12425602", "Event 12425602"),
    12425603: ("Event12425603", "Event 12425603"),
    12425400: ("Event12425400", "Event 12425400"),
    12420990: ("Event12420990", "Event 12420990"),
    12424450: ("Event12424450", "Event 12424450"),
    12424400: ("Event12424400", "Event 12424400"),
    12424410: ("Event12424410", "Event 12424410"),
    12424460: ("Event12424460", "Event 12424460"),
}


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
