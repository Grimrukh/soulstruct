"""FISHING HAMLET"""
from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    13604700: ("Event13604700", "Event 13604700"),
    13604710: ("Event13604710", "Event 13604710"),
    13604720: ("Event13604720", "Event 13604720"),
    13604730: ("Event13604730", "Event 13604730"),
    13604740: ("Event13604740", "Event 13604740"),
    13604742: ("Event13604742", "Event 13604742"),
    13600000: ("Event13600000", "Event 13600000"),
    13600010: ("Event13600010", "Event 13600010"),
    13601090: ("Event13601090", "Event 13601090"),
    13601100: ("Event13601100", "Event 13601100"),
    13601101: ("Event13601101", "Event 13601101"),
    13601102: ("Event13601102", "Event 13601102"),
    13601103: ("Event13601103", "Event 13601103"),
    13601104: ("Event13601104", "Event 13601104"),
    13601105: ("Event13601105", "Event 13601105"),
    13601140: ("Event13601140", "Event 13601140"),
    13601200: ("Event13601200", "Event 13601200"),
    13601312: ("Event13601312", "Event 13601312"),
    13601210: ("Event13601210", "Event 13601210"),
    13601400: ("Event13601400", "Event 13601400"),
    13604400: ("Event13604400", "Event 13604400"),
    13601800: ("OrphanDies", "Event 13601800"),
    13604811: ("OrphanFirstTimeTrigger", "Event 13604811"),
    13601801: ("OrphanFirstTimeCutscene", "Event 13601801"),
    13601802: ("ControlOrphanSpirit", "Event 13601802"),
    13601803: ("OrphanSpiritDies", "Trigger banner, cutscene, and moon swap when Orphan's immobile spirit is killed."),
    13601804: ("SummonStartOrphanBattle", "Event 13601804"),
    13604800: ("EnterOrphanFog", "Event 13604800"),
    13604801: ("EnterOrphanFogAsSummon", "Event 13604801"),
    13604802: ("StartOrphanBattle", "Event 13604802"),
    13604803: ("ControlOrphanMusic", "Event 13604803"),
    13604804: ("ControlOrphanCamera", "Event 13604804"),
    13604805: ("StopOrphanMusic", "Event 13604805"),
    13604806: ("Event13604806", "Event 13604806"),
    13604807: ("Event13604807", "Event 13604807"),
    13604820: ("OrphanPhaseTwoTrigger", "Event 13604820"),
    13604830: ("OrphanPhaseTwoLightning", "Event 13604830"),
    13604850: ("ControlOrphanPhaseTwoLightningCamera", "Event 13604850"),
    13605200: ("Event13605200", "Event 13605200"),
    13605400: ("Event13605400", "Event 13605400"),
    13605480: ("Event13605480", "Event 13605480"),
    13605490: ("Event13605490", "Event 13605490"),
    13605500: ("Event13605500", "Event 13605500"),
    13605520: ("Event13605520", "Event 13605520"),
    13605540: ("Event13605540", "Event 13605540"),
    13605560: ("Event13605560", "Event 13605560"),
    13605600: ("Event13605600", "Event 13605600"),
    13605605: ("Event13605605", "Event 13605605"),
    13605606: ("Event13605606", "Event 13605606"),
    13605700: ("Event13605700", "Event 13605700"),
    13605720: ("Event13605720", "Event 13605720"),
    13605730: ("Event13605730", "Event 13605730"),
    13605740: ("Event13605740", "Event 13605740"),
    13605750: ("Event13605750", "Event 13605750"),
    13605751: ("Event13605751", "Event 13605751"),
    13605752: ("Event13605752", "Event 13605752"),
    13605760: ("Event13605760", "Event 13605760"),
    13605761: ("Event13605761", "Event 13605761"),
    13605762: ("Event13605762", "Event 13605762"),
    13605770: ("Event13605770", "Event 13605770"),
    13605799: ("Event13605799", "Event 13605799"),
    13605900: ("Event13605900", "Event 13605900"),
    13605910: ("Event13605910", "Event 13605910"),
    13605920: ("Event13605920", "Event 13605920"),
    13605921: ("Event13605921", "Event 13605921"),
    13605930: ("Event13605930", "Event 13605930"),
    13605940: ("Event13605940", "Event 13605940"),
    13600900: ("Event13600900", "Event 13600900"),
    13600940: ("Event13600940", "Event 13600940"),
    13600943: ("Event13600943", "Event 13600943"),
    13600941: ("Event13600941", "Event 13600941"),
    13600942: ("Event13600942", "Event 13600942"),
    13600944: ("Event13600944", "Event 13600944"),
    13600950: ("Event13600950", "Event 13600950"),
    13600951: ("Event13600951", "Event 13600951"),
    13600952: ("Event13600952", "Event 13600952"),
    13600953: ("Event13600953", "Event 13600953"),
    13600954: ("Event13600954", "Event 13600954"),
    13600955: ("Event13600955", "Event 13600955"),
    13600956: ("Event13600956", "Event 13600956"),
    13600995: ("Event13600995", "Event 13600995"),
}


class Flags(Flag):
    OrphanDead = 13601800
    OrphanSpiritDead = 13601803
    OrphanFogEntered = 13604808
    OrphanPhaseTwo = 13604820


class Characters(Character):
    Orphan = 3600800
    OrphanWinged = 3600801
    OrphanSpirit = 3600802
    OrphanLightningCreator = 3600803


class Objects(Object):
    OrphanFog1 = 3601800
    OrphanFog2 = 3601801  # seems to be cut; maybe was originally out in the water?
    KosCorpse = 3601802
    MoonOrphanAlive = 3601810
    MoonOrphanDead = 3601811  # entire skybox actually


class VFX(VFXEvent):
    OrphanFog1 = 3603800
    OrphanFog2 = 3603801


class Cutscenes(Cutscene):
    OrphanBirth = 36000000
    OrphanSpiritDeath = 36000010
