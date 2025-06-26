from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    12301800: ("BloodStarvedBeastDies", "Event 12301800"),
    12301801: ("PlayBloodStarvedBeastDeathSound", "Event 12301801"),
    12301802: ("BloodStarvedBeastFirstTime", "Event 12301802"),
    12301803: ("SummonStartBloodStarvedBeastBattle", "Event 12301803"),
    12304810: ("EnterBloodStarvedBeastFog", "Event 12304810"),
    12304811: ("EnterBloodStarvedBeastFogAsSummon", "Event 12304811"),
    12304812: ("Event12304812", "Event 12304812"),
    12304813: ("Event12304813", "Event 12304813"),
    12304802: ("Event12304802", "Event 12304802"),
    12304803: ("Event12304803", "Event 12304803"),
    12304804: ("Event12304804", "Event 12304804"),
    12304805: ("Event12304805", "Event 12304805"),
    12304807: ("Event12304807", "Event 12304807"),
    12304808: ("Event12304808", "Event 12304808"),
    12301700: ("DarkbeastPaarlDies", "Darkbeast Paarl is killed."),
    12301701: ("PlayDarkbeastPaarlDeathSound", "Event 12301701"),
    12301702: ("DarkbeastPaarlFirstTime", "Event 12301702"),
    12301703: ("SummonStartDarkbeastPaarlBattle", "Event 12301703"),
    12304730: ("Event12304730", "Event 12304730"),
    12304731: ("Event12304731", "Event 12304731"),
    12304732: ("Event12304732", "Event 12304732"),
    12304733: ("Event12304733", "Event 12304733"),
    12304702: ("Event12304702", "Event 12304702"),
    12304703: ("Event12304703", "Event 12304703"),
    12304704: ("Event12304704", "Event 12304704"),
    12304705: ("Event12304705", "Event 12304705"),
    12304707: ("Event12304707", "Event 12304707"),
    12304715: ("Event12304715", "Event 12304715"),
    12304450: ("Event12304450", "Event 12304450"),
    12304400: ("Event12304400", "Event 12304400"),
    12304401: ("Event12304401", "Event 12304401"),
    12304402: ("Event12304402", "Event 12304402"),
    12304410: ("Event12304410", "Event 12304410"),
    12304460: ("Event12304460", "Event 12304460"),
    12304500: ("Event12304500", "Event 12304500"),
    12304501: ("Event12304501", "Event 12304501"),
    12304502: ("Event12304502", "Event 12304502"),
    12304504: ("Event12304504", "Event 12304504"),
    12304505: ("Event12304505", "Event 12304505"),
    12304506: ("Event12304506", "Event 12304506"),
    12304507: ("Event12304507", "Event 12304507"),
    12300100: ("Event12300100", "Event 12300100"),
    12300110: ("Event12300110", "Event 12300110"),
    12300120: ("Event12300120", "Event 12300120"),
    12300130: ("Event12300130", "Event 12300130"),
    12300140: ("Event12300140", "Event 12300140"),
    12300160: ("Event12300160", "Event 12300160"),
    12300180: ("Event12300180", "Event 12300180"),
    12300190: ("Event12300190", "Event 12300190"),
    12300201: ("Event12300201", "Event 12300201"),
    12300210: ("Event12300210", "Event 12300210"),
    12300220: ("Event12300220", "Event 12300220"),
    12300230: ("Event12300230", "Event 12300230"),
    12300235: ("Event12300235", "Event 12300235"),
    12300240: ("Event12300240", "Event 12300240"),
    12300250: ("Event12300250", "Event 12300250"),
    12300300: ("Event12300300", "Event 12300300"),
    12300310: ("Event12300310", "Event 12300310"),
    12305000: ("Event12305000", "Event 12305000"),
    12305001: ("Event12305001", "Event 12305001"),
    12305010: ("Event12305010", "Event 12305010"),
    12305020: ("Event12305020", "Event 12305020"),
    12305021: ("Event12305021", "Event 12305021"),
    12305022: ("Event12305022", "Event 12305022"),
    12305023: ("Event12305023", "Event 12305023"),
    12305030: ("Event12305030", "Event 12305030"),
    12305040: ("Event12305040", "Event 12305040"),
    12305070: ("Event12305070", "Event 12305070"),
    12305075: ("Event12305075", "Event 12305075"),
    12305080: ("Event12305080", "Event 12305080"),
    12305081: ("Event12305081", "Event 12305081"),
    12305082: ("Event12305082", "Event 12305082"),
    12305090: ("Event12305090", "Event 12305090"),
    12305100: ("Event12305100", "Event 12305100"),
    12305110: ("Event12305110", "Event 12305110"),
    12305120: ("Event12305120", "Event 12305120"),
    12305121: ("Event12305121", "Event 12305121"),
    12305125: ("Event12305125", "Event 12305125"),
    12305130: ("Event12305130", "Event 12305130"),
    12305135: ("Event12305135", "Event 12305135"),
    12305140: ("Event12305140", "Event 12305140"),
    12305160: ("Event12305160", "Event 12305160"),
    12305180: ("Event12305180", "Event 12305180"),
    12305190: ("Event12305190", "Event 12305190"),
    12305250: ("Event12305250", "Event 12305250"),
    12305300: ("Event12305300", "Event 12305300"),
    12305440: ("Event12305440", "Event 12305440"),
    12305480: ("Event12305480", "Event 12305480"),
    12305481: ("Event12305481", "Event 12305481"),
    12305482: ("Event12305482", "Event 12305482"),
    12305490: ("Event12305490", "Event 12305490"),
    12305501: ("Event12305501", "Event 12305501"),
    12305502: ("Event12305502", "Event 12305502"),
    12305510: ("Event12305510", "Event 12305510"),
    12300700: ("Event12300700", "Event 12300700"),
    12300701: ("Event12300701", "Event 12300701"),
    12300702: ("Event12300702", "Event 12300702"),
    12300703: ("Event12300703", "Event 12300703"),
    12300704: ("Event12300704", "Event 12300704"),
    12300705: ("Event12300705", "Event 12300705"),
    12305701: ("Event12305701", "Event 12305701"),
    12300707: ("Event12300707", "Event 12300707"),
    12300708: ("Event12300708", "Event 12300708"),
    12300710: ("Event12300710", "Event 12300710"),
    12300750: ("Event12300750", "Event 12300750"),
    12300752: ("Event12300752", "Event 12300752"),
    12300753: ("Event12300753", "Event 12300753"),
    12300990: ("Event12300990", "Event 12300990"),
    12304020: ("Event12304020", "Event 12304020"),
    12304021: ("Event12304021", "Event 12304021"),
    12304022: ("Event12304022", "Event 12304022"),
}


class Flags(Flag):
    DarkbeastPaarlDead = 12301700
    DarkbeastPaarlFirstTimeDone = 12301702
    DarkbeastPaarlFogEntered = 12304700
    DarkbeastPaarlBattleStartedForSummon = 12304701
    DarkbeastPaarlBattleStarted = 123047

    BloodStarvedBeastDead = 12301800
    BloodStarvedBeastFirstTimeDone = 12301802
    BloodStarvedBeastFogEntered = 12304800
    BloodStarvedBeastBattleStartedForSummon = 12304801
    BloodStarvedBeastBattleStarted = 12304802


class Characters(Character):
    BloodStarvedBeast = 2300800
    DarkbeastPaarl = 2300810


class Objects(Object):
    BossFog = 2301800
    OldYharnamLantern = 2301950
    BloodStarvedBeastLantern = 2301951
    DarkbeastPaarlLantern = 2301952


class Regions(Region):
    BloodStarvedBeastFirstTimeTrigger = 2302805


class VFX(VFXEvent):
    BossFog = 2303800
