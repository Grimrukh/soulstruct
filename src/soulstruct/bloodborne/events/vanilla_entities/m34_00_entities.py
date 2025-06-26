"""HUNTER'S NIGHTMARE"""
from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    13400010: ("Event13400010", "Event 13400010"),
    13400998: ("Event13400998", "Event 13400998"),
    13401250: ("Event13401250", "Event 13401250"),
    13401350: ("Event13401350", "Event 13401350"),
    13401500: ("Event13401500", "Event 13401500"),
    13401000: ("Event13401000", "Event 13401000"),
    13404700: ("Event13404700", "Event 13404700"),
    13404710: ("Event13404710", "Event 13404710"),
    13404720: ("Event13404720", "Event 13404720"),
    13404730: ("Event13404730", "Unused event."),
    13404740: ("Event13404740", "Event 13404740"),
    13404742: ("Event13404742", "Event 13404742"),
    13401800: ("LudwigDies", "Event 13401800"),
    13404811: ("Event13404811", "Event 13404811"),
    13401801: ("LudwigFirstTime", "Event 13401801"),
    13401802: ("ControlLudwigAnnouncer", "Event 13401802"),
    13401803: ("LudwigAnnouncerDies", "Event 13401803"),
    13401804: ("SummonStartLudwigBattle", "Event 13401804"),
    13404800: ("EnterLudwigFog", "Event 13404800"),
    13404801: ("EnterLudwigFogAsSummon", "Event 13404801"),
    13404802: ("StartLudwigBattle", "Event 13404802"),
    13404803: ("ControlLudwigMusic", "Event 13404803"),
    13404804: ("ControlLudwigCamera", "Event 13404804"),
    13404805: ("StopLudwigMusic", "Event 13404805"),
    13404806: ("Event13404806", "Event 13404806"),
    13404807: ("Event13404807", "Event 13404807"),
    13404820: ("Event13404820", "Event 13404820"),
    13404821: ("Event13404821", "Event 13404821"),
    13404822: ("Event13404822", "Event 13404822"),
    13404823: ("Event13404823", "Event 13404823"),
    13404824: ("LudwigPhaseTwoMusicTrigger", "Allow music transition to begin before the phase transition finishes."),
    13404825: ("LudwigPhaseTwoTrigger", "Event 13404825"),
    13404830: ("LudwigTheAccursedLimbDamage", "Event 13404830"),
    13404835: ("LudwigPhaseTwoStagger", "Ludwig is staggered at 35% (and gains new attacks), 6.6%, and 3.3% health."),
    13404840: ("LudwigDelayedJumpAttack", "Event 13404840"),
    13404841: ("Event13404841", "Event 13404841"),
    13401850: ("LaurenceDies", "Event 13401850"),
    13404861: ("LaurenceAwakens", "Event 13404861"),
    13401851: ("LaurenceFirstTime", "Event 13401851"),
    13401853: ("SummonStartLaurenceBattle", "Event 13401853"),
    13404850: ("EnterLaurenceFog", "Event 13404850"),
    13404851: ("EnterLaurenceFogAsSummon", "Event 13404851"),
    13404852: ("StartLaurenceBattle", "Event 13404852"),
    13404853: ("ControlLaurenceMusic", "Event 13404853"),
    13404854: ("ControlLaurenceCamera", "Event 13404854"),
    13404855: ("StopLaurenceMusic", "Event 13404855"),
    13404856: ("Event13404856", "Event 13404856"),
    13404857: ("Event13404857", "Event 13404857"),
    13404870: ("LaurenceLimbDamage", "Event 13404870"),
    13404875: ("RemoveLaurenceLegCollision", "Event 13404875"),
    13401200: ("Event13401200", "Event 13401200"),
    13401210: ("Event13401210", "Event 13401210"),
    13401220: ("Event13401220", "Event 13401220"),
    13400100: ("Event13400100", "Event 13400100"),
    13400220: ("Event13400220", "Event 13400220"),
    13400310: ("Event13400310", "Event 13400310"),
    13400320: ("Event13400320", "Event 13400320"),
    13400330: ("Event13400330", "Event 13400330"),
    13404799: ("Event13404799", "Event 13404799"),
    13405100: ("Event13405100", "Event 13405100"),
    13405103: ("Event13405103", "Event 13405103"),
    13405105: ("Event13405105", "Event 13405105"),
    13405110: ("Event13405110", "Event 13405110"),
    13405112: ("Event13405112", "Event 13405112"),
    13405113: ("Event13405113", "Event 13405113"),
    13405115: ("Event13405115", "Event 13405115"),
    13405140: ("Event13405140", "Event 13405140"),
    13405145: ("Event13405145", "Event 13405145"),
    13405155: ("Event13405155", "Event 13405155"),
    13405160: ("Event13405160", "Event 13405160"),
    13405200: ("Event13405200", "Event 13405200"),
    13405211: ("Event13405211", "Event 13405211"),
    13405216: ("Event13405216", "Event 13405216"),
    13405218: ("Event13405218", "Event 13405218"),
    13405220: ("Event13405220", "Event 13405220"),
    13405300: ("Event13405300", "Event 13405300"),
    13405350: ("Event13405350", "Event 13405350"),
    13405480: ("Event13405480", "Event 13405480"),
    13405510: ("Event13405510", "Event 13405510"),
    13405520: ("Event13405520", "Event 13405520"),
    13405530: ("Event13405530", "Event 13405530"),
    13405540: ("Event13405540", "Event 13405540"),
    13405550: ("Event13405550", "Event 13405550"),
    13405570: ("Event13405570", "Event 13405570"),
    13405610: ("Event13405610", "Event 13405610"),
    13405620: ("Event13405620", "Event 13405620"),
    13405630: ("Event13405630", "Event 13405630"),
    13405640: ("Event13405640", "Event 13405640"),
    13405650: ("Event13405650", "Event 13405650"),
    13405680: ("Event13405680", "Event 13405680"),
    13400940: ("Event13400940", "Event 13400940"),
    13400941: ("Event13400941", "Event 13400941"),
    13400942: ("Event13400942", "Event 13400942"),
    13400943: ("Event13400943", "Event 13400943"),
    13400944: ("Event13400944", "Event 13400944"),
    13400900: ("Event13400900", "Event 13400900"),
    13400910: ("Event13400910", "Event 13400910"),
    13400920: ("Event13400920", "Event 13400920"),
    13400930: ("Event13400930", "Event 13400930"),
    13400950: ("Event13400950", "Event 13400950"),
    13400951: ("Event13400951", "Event 13400951"),
    13400953: ("Event13400953", "Event 13400953"),
    13400970: ("Event13400970", "Event 13400970"),
    13400980: ("Event13400980", "Event 13400980"),
    13400990: ("Event13400990", "Event 13400990"),
    13400995: ("Event13400995", "Event 13400995"),
    13404450: ("Event13404450", "Event 13404450"),
    13404401: ("Event13404401", "Event 13404401"),
    13404402: ("Event13404402", "Event 13404402"),
    13404403: ("Event13404403", "Event 13404403"),
    13404404: ("Event13404404", "Event 13404404"),
    13404405: ("Event13404405", "Event 13404405"),
    13404406: ("Event13404406", "Event 13404406"),
    13404410: ("Event13404410", "Event 13404410"),
    13404460: ("Event13404460", "Event 13404460"),
    13404490: ("Event13404490", "Event 13404490"),
}


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


class Cutscenes(Cutscene):
    LaurenceAwakening = 34000010
    LudwigTransformation = 34000030
