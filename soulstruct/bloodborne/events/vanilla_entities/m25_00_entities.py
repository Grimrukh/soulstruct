from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    12500000: ("CainhurstFirstArrivalCutscene", "Event 12500000"),
    12500001: ("Event12500001", "Event 12500001"),
    12500010: ("Event12500010", "Event 12500010"),
    12500011: ("Event12500011", "Event 12500011"),
    12500012: ("Event12500012", "Event 12500012"),
    12500013: ("Event12500013", "Event 12500013"),
    12500014: ("Event12500014", "Event 12500014"),
    12500015: ("Event12500015", "Event 12500015"),
    12500016: ("Event12500016", "Event 12500016"),
    12500018: ("Event12500018", "Event 12500018"),
    12500019: ("Event12500019", "Event 12500019"),
    12500020: ("Event12500020", "Event 12500020"),
    12500021: ("Event12500021", "Event 12500021"),
    12500030: ("Event12500030", "Event 12500030"),
    12500031: ("Event12500031", "Event 12500031"),
    12500050: ("Event12500050", "Event 12500050"),
    12500051: ("Event12500051", "Event 12500051"),
    12500052: ("Event12500052", "Event 12500052"),
    12500053: ("Event12500053", "Event 12500053"),
    12500054: ("Event12500054", "Event 12500054"),
    12500070: ("Event12500070", "Event 12500070"),
    12500072: ("Event12500072", "Event 12500072"),
    12500075: ("Event12500075", "Event 12500075"),
    12500076: ("Event12500076", "Event 12500076"),
    12500077: ("Event12500077", "Event 12500077"),
    12500078: ("Event12500078", "Event 12500078"),
    12505100: ("Event12505100", "Event 12505100"),
    12500100: ("Event12500100", "Event 12500100"),
    12500200: ("Event12500200", "Event 12500200"),
    12500206: ("Event12500206", "Event 12500206"),
    12500220: ("Event12500220", "Event 12500220"),
    12500235: ("Event12500235", "Event 12500235"),
    12500285: ("Event12500285", "Event 12500285"),
    12500390: ("Event12500390", "Event 12500390"),
    12500400: ("Event12500400", "Event 12500400"),
    12500430: ("Event12500430", "Event 12500430"),
    12500435: ("Event12500435", "Event 12500435"),
    12500440: ("Event12500440", "Event 12500440"),
    12500454: ("Event12500454", "Event 12500454"),
    12500458: ("Event12500458", "Event 12500458"),
    12500501: ("Event12500501", "Event 12500501"),
    12500502: ("Event12500502", "Event 12500502"),
    12500503: ("Event12500503", "Event 12500503"),
    12500520: ("Event12500520", "Event 12500520"),
    12500620: ("Event12500620", "Event 12500620"),
    12500630: ("Event12500630", "Event 12500630"),
    12500640: ("Event12500640", "Event 12500640"),
    12500740: ("Event12500740", "Event 12500740"),
    12504000: ("Event12504000", "Event 12504000"),
    12504005: ("Event12504005", "Event 12504005"),
    101: ("Event101", "Event 101"),
    12500810: ("PlayerDiscoversVilebloodQueenChamber", "Event 12500810"),
    12501800: ("MartyrLogariusDies", "Event 12501800"),
    12501801: ("PlayMartyrLogariusDeathSound", "Event 12501801"),
    12501802: ("MartyrLogariusFirstTime", "Event 12501802"),
    12501803: ("GiftCrownOfIllusions", "Event 12501803"),
    12501804: ("SummonStartMartyrLogariusBattle", "Event 12501804"),
    12500600: ("Event12500600", "Event 12500600"),
    12504810: ("EnterMartyrLogariusFog", "Event 12504810"),
    12504811: ("EnterMartyrLogariusFogAsSummon", "Event 12504811"),
    12504812: ("Event12504812", "Event 12504812"),
    12504813: ("Event12504813", "Event 12504813"),
    12504802: ("StartMartyrLogariusBattle", "Event 12504802"),
    12504803: ("ControlMartyrLogariusMusic", "Event 12504803"),
    12504804: ("ControlMartyrLogariusCamera", "Event 12504804"),
    12504805: ("StopMartyrLogariusMusic", "Event 12504805"),
    12504806: ("CreateMartyrLogariusSword", "Event 12504806"),
    12504807: ("MartyrLogariusChargesUp", "Event 12504807"),
    12504808: ("CancelMartyrLogariusCharge", "Probably when he is knocked out of charging animation?"),
    12500896: ("Event12500896", "Event 12500896"),
    12500898: ("Event12500898", "Event 12500898"),
    12500900: ("Event12500900", "Event 12500900"),
    12501000: ("Event12501000", "Event 12501000"),
    12505000: ("Event12505000", "Event 12505000"),
    12505300: ("Event12505300", "Event 12505300"),
    12500090: ("Event12500090", "Event 12500090"),
    12507010: ("Event12507010", "Event 12507010"),
    12507020: ("Event12507020", "Event 12507020"),
    12507040: ("Event12507040", "Event 12507040"),
    12507050: ("Event12507050", "Event 12507050"),
}


class Flags(Flag):
    MartyrLogariusDead = 12501800
    MartyrLogariusFirstTimeDone = 12501802
    MartyrLogariusFogEntered = 12504800
    MartyrLogariusBattleStarted = 12504802


class Characters(Character):
    MartyrLogarius = 2500800
    MartyrLogariusSword = 2500801
    MartyrLogariusBulletOwner = 2500802


class Objects(Object):
    BossFog = 2501800


class VFX(VFXEvent):
    BossFog = 2503800
