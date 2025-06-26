"""NIGHTMARE FRONTIER"""
from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    13304700: ("Event13304700", "Event 13304700"),
    13304710: ("Event13304710", "Event 13304710"),
    13304720: ("Event13304720", "Event 13304720"),
    13304730: ("Event13304730", "Event 13304730"),
    13301800: ("AmygdalaDies", "Event 13301800"),
    13301801: ("PlayAmygdalaDeathSound", "Event 13301801"),
    13301802: ("AmygdalaFirstTime", "Event 13301802"),
    13301803: ("SummonStartAmygdalaBattle", "Event 13301803"),
    13304870: ("EnterAmygdalaFog", "Event 13304870"),
    13304871: ("EnterAmygdalaFogAsSummon", "Event 13304871"),
    13304872: ("Event13304872", "Event 13304872"),
    13304873: ("Event13304873", "Event 13304873"),
    13304802: ("StartAmygdalaBattle", "Event 13304802"),
    13304803: ("ControlAmygdalaMusic", "Event 13304803"),
    13304804: ("ControlAmygdalaCamera", "Event 13304804"),
    13304805: ("StopAmygdalaMusic", "Event 13304805"),
    13304807: ("AmygdalaPhaseTwoTrigger", "Event 13304807"),
    13304808: ("AmygdalaPhaseThreeTrigger", "Event 13304808"),
    13304820: ("AmygdalaHoldingOwnArm", "Event 13304820"),
    13304830: ("AmygdalaLimbDamage", "Event 13304830"),
    13304840: ("AmygdalaHeadDamage", "Event 13304840"),
    13300100: ("Event13300100", "Event 13300100"),
    13300110: ("Event13300110", "Event 13300110"),
    13300111: ("Event13300111", "Event 13300111"),
    13300112: ("Event13300112", "Event 13300112"),
    13300113: ("Event13300113", "Event 13300113"),
    13300120: ("Event13300120", "Event 13300120"),
    13300130: ("Event13300130", "Event 13300130"),
    13300200: ("Event13300200", "Event 13300200"),
    13300210: ("Event13300210", "Event 13300210"),
    13300220: ("Event13300220", "Event 13300220"),
    13305150: ("Event13305150", "Event 13305150"),
    13305030: ("Event13305030", "Event 13305030"),
    13305040: ("Event13305040", "Event 13305040"),
    13305041: ("Event13305041", "Event 13305041"),
    13305200: ("Event13305200", "Event 13305200"),
    13305210: ("Event13305210", "Event 13305210"),
    13305220: ("Event13305220", "Event 13305220"),
    13305230: ("Event13305230", "Event 13305230"),
    13305250: ("Event13305250", "Event 13305250"),
    13305255: ("Event13305255", "Event 13305255"),
    13300700: ("Event13300700", "Event 13300700"),
    13300990: ("Event13300990", "Event 13300990"),
}


class Flags(Flag):
    AmygdalaDead = 13301800
    AmygdalaFirstTimeDone = 13301802
    AmygdalaFogEntered = 13304800
    AmygdalaBattleStarted = 13304802
    AmygdalaPhaseTwo = 13304807
    AmygdalaPhaseThree = 13304808


class Characters(Character):
    Amygdala = 3300800


class Objects(Object):
    AmygdalaFog1 = 3301800
    AmygdalaFog2 = 3301801


class VFX(VFXEvent):
    AmygdalaFog1 = 3303800
    AmygdalaFog2 = 3303801
