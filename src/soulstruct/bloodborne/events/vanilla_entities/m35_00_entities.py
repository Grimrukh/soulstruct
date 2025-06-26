"""RESEARCH HALL"""
from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    13500000: ("Event13500000", "Event 13500000"),
    13504700: ("Event13504700", "Event 13504700"),
    13504710: ("Event13504710", "Event 13504710"),
    13504720: ("Event13504720", "Event 13504720"),
    13504730: ("Event13504730", "Event 13504730"),
    13501800: ("LadyMariaDies", "Event 13501800"),
    13501801: ("LadyMariaFirstTime", "Event 13501801"),
    13501802: ("OpenAstralClocktower", "Event 13501802"),
    13501803: ("LadyMariaItemDrop", "Event 13501803"),
    13501804: ("Event13501804", "UNUSED. Probably said that the Clock was already open."),
    13501805: ("LadyMariaObjectDestroyed", "Event 13501805"),
    13501807: ("ControlLadyMariaInChair", "Event 13501807"),
    13501810: ("Event13501810", "Event 13501810"),
    13504800: ("EnterLadyMariaFog", "Event 13504800"),
    13504801: ("EnterLadyMariaFogAsSummon", "Event 13504801"),
    13504802: ("StartLadyMariaBattle", "Event 13504802"),
    13504803: ("ControlLadyMariaMusic", "Event 13504803"),
    13504804: ("ControlLadyMariaCamera", "Event 13504804"),
    13504805: ("StopLadyMariaMusic", "Event 13504805"),
    13504806: ("Event13504806", "Event 13504806"),
    13504807: ("Event13504807", "Event 13504807"),
    13504822: ("CancelLadyMariaBuff", "Event 13504822"),
    13501850: ("LivingFailuresDie", "Event 13501850"),
    13501851: ("LivingFailuresFirstTime", "Event 13501851"),
    13501852: ("SummonStartLivingFailuresBattle", "Event 13501852"),
    13504850: ("EnterLivingFailuresFog", "Event 13504850"),
    13504851: ("EnterLivingFailuresFogAsSummon", "Event 13504851"),
    13504852: ("StartLivingFailuresBattle", "Event 13504852"),
    13504853: ("ControlLivingFailuresMusic", "Event 13504853"),
    13504854: ("ControlLivingFailuresCamera", "Event 13504854"),
    13504855: ("StopLivingFailuresMusic", "Event 13504855"),
    13504856: ("Event13504856", "Event 13504856"),
    13504857: ("Event13504857", "Event 13504857"),
    13504865: ("LivingFailuresMeteorAttackRequest", "Event 13504865"),
    13504880: ("LivingFailuresMeteorAttackRoll", "Event 13504880"),
    13504881: ("LivingFailuresMeteorAttackFinished", "Event 13504881"),
    13504885: ("LivingFailureMagicOrb", "Pretty sure this triggers the \"spirit bomb\" attack (used only by two of the Failures)."),
    13504890: ("LivingFailureMeteorSummon", "Triggered when any flag between 4875 and 4878 is enabled."),
    13504895: ("KillRemainingLivingFailure", "Event 13504895"),
    13505655: ("LivingFailuresSpawnRequest", "Event 13505655"),
    13505656: ("RequestActiveLivingFailureCountOnSpawnAndDeath", "Requests a Living Failure recount every time this Living Failure spawns or dies."),
    13505662: ("SpawnLivingFailure", "Event 13505662"),
    13505670: ("Event13505670", "Event 13505670"),
    13501100: ("Event13501100", "Event 13501100"),
    13501101: ("Event13501101", "Event 13501101"),
    13501102: ("Event13501102", "Event 13501102"),
    13501103: ("Event13501103", "Event 13501103"),
    13501104: ("Event13501104", "Event 13501104"),
    13501105: ("Event13501105", "Event 13501105"),
    13501140: ("Event13501140", "Event 13501140"),
    13501141: ("Event13501141", "Event 13501141"),
    13501142: ("Event13501142", "Event 13501142"),
    13501110: ("Event13501110", "Event 13501110"),
    13501111: ("Event13501111", "Event 13501111"),
    13501112: ("Event13501112", "Event 13501112"),
    13501113: ("Event13501113", "Event 13501113"),
    13501114: ("Event13501114", "Event 13501114"),
    13501115: ("Event13501115", "Event 13501115"),
    13501120: ("Event13501120", "Event 13501120"),
    13501121: ("Event13501121", "Event 13501121"),
    13501122: ("Event13501122", "Event 13501122"),
    13501123: ("Event13501123", "Event 13501123"),
    13501124: ("Event13501124", "Event 13501124"),
    13501125: ("Event13501125", "Event 13501125"),
    13501200: ("Event13501200", "Event 13501200"),
    13501250: ("Event13501250", "Event 13501250"),
    13501400: ("Event13501400", "Event 13501400"),
    13504799: ("Event13504799", "Event 13504799"),
    13500100: ("Event13500100", "Event 13500100"),
    13500105: ("Event13500105", "Event 13500105"),
    13500106: ("Event13500106", "Event 13500106"),
    13500110: ("Event13500110", "Event 13500110"),
    13500111: ("Event13500111", "Event 13500111"),
    13500120: ("Event13500120", "Event 13500120"),
    13500130: ("Event13500130", "Event 13500130"),
    13500140: ("Event13500140", "Event 13500140"),
    13500150: ("Event13500150", "Event 13500150"),
    13500400: ("Event13500400", "Event 13500400"),
    13500410: ("Event13500410", "Event 13500410"),
    13500418: ("Event13500418", "Event 13500418"),
    13500420: ("Event13500420", "Event 13500420"),
    13500430: ("Event13500430", "Event 13500430"),
    13500450: ("Event13500450", "Event 13500450"),
    13500460: ("Event13500460", "Event 13500460"),
    13500500: ("Event13500500", "Event 13500500"),
    13505050: ("Event13505050", "Event 13505050"),
    13505060: ("Event13505060", "Event 13505060"),
    13505100: ("Event13505100", "Event 13505100"),
    13505110: ("Event13505110", "Event 13505110"),
    13505200: ("Event13505200", "Event 13505200"),
    13505300: ("Event13505300", "Event 13505300"),
    13505400: ("Event13505400", "Event 13505400"),
    13505410: ("Event13505410", "Event 13505410"),
    13505450: ("Event13505450", "Event 13505450"),
    13505470: ("Event13505470", "Event 13505470"),
    13505510: ("Event13505510", "Event 13505510"),
    13505570: ("Event13505570", "Event 13505570"),
    13505580: ("Event13505580", "Event 13505580"),
    13505590: ("Event13505590", "Event 13505590"),
    13505610: ("Event13505610", "Event 13505610"),
    13505630: ("Event13505630", "Event 13505630"),
    13505640: ("Event13505640", "Event 13505640"),
    13505650: ("Event13505650", "Event 13505650"),
    13505700: ("Event13505700", "Event 13505700"),
    13505740: ("Event13505740", "Event 13505740"),
    13505750: ("Event13505750", "Event 13505750"),
    13505780: ("Event13505780", "Event 13505780"),
    13505797: ("Event13505797", "Event 13505797"),
    13505800: ("Event13505800", "Event 13505800"),
    13505810: ("Event13505810", "Event 13505810"),
    13505820: ("Event13505820", "Event 13505820"),
    13500900: ("Event13500900", "Event 13500900"),
    13500910: ("Event13500910", "Event 13500910"),
    13500920: ("Event13500920", "Event 13500920"),
    13500940: ("Event13500940", "Event 13500940"),
    13500942: ("Event13500942", "Event 13500942"),
    13500941: ("Event13500941", "Event 13500941"),
    13500943: ("Event13500943", "Event 13500943"),
    13500944: ("Event13500944", "Event 13500944"),
    13500945: ("Event13500945", "Event 13500945"),
    13500946: ("Event13500946", "Event 13500946"),
    13500948: ("Event13500948", "Event 13500948"),
    13500949: ("Event13500949", "Event 13500949"),
    13500950: ("Event13500950", "Event 13500950"),
    13500951: ("Event13500951", "Event 13500951"),
    13500952: ("Event13500952", "Event 13500952"),
    13500953: ("Event13500953", "Event 13500953"),
    13500960: ("Event13500960", "Event 13500960"),
    13500963: ("Event13500963", "Event 13500963"),
    13500965: ("Event13500965", "Event 13500965"),
    13500966: ("Event13500966", "Event 13500966"),
    13500967: ("Event13500967", "Event 13500967"),
    13500968: ("Event13500968", "Event 13500968"),
    13500977: ("Event13500977", "Event 13500977"),
    13500978: ("Event13500978", "Event 13500978"),
    13500980: ("Event13500980", "Event 13500980"),
    13500990: ("Event13500990", "Event 13500990"),
    13500994: ("Event13500994", "Event 13500994"),
    13500998: ("Event13500998", "Event 13500998"),
    13500999: ("Event13500999", "Event 13500999"),
    13501900: ("Event13501900", "Event 13501900"),
    13501915: ("Event13501915", "Event 13501915"),
    13501920: ("Event13501920", "Event 13501920"),
    13501940: ("Event13501940", "Event 13501940"),
    13501960: ("Event13501960", "Event 13501960"),
    13505900: ("Event13505900", "Event 13505900"),
    13505901: ("Event13505901", "Event 13505901"),
    13505902: ("Event13505902", "Event 13505902"),
    13505903: ("Event13505903", "Event 13505903"),
    13505904: ("Event13505904", "Event 13505904"),
    13504400: ("Event13504400", "Event 13504400"),
    13504410: ("Event13504410", "Event 13504410"),
    13504450: ("Event13504450", "Event 13504450"),
    13504460: ("Event13504460", "Event 13504460"),
}


class Flags(Flag):
    LadyMariaDead = 13501800
    LadyMariaFirstTimeDone = 13501801
    LadyMariaFogEntered = 13504808
    LadyMariaBattleStarted = 13504802

    LivingFailuresDead = 13501850
    LivingFailuresFirstTimeDone = 13501851
    LivingFailuresFogEntered = 13504858
    LivingFailuresBattleStarted = 13504860
    LivingFailuresMeteorRequest = 13504866  # enabled while meteor attack is ongoing
    LivingFailuresFirstMeteorAttackDone = 13504868
    LivingFailuresMeteorAttackAvailable = 13504869  # at 60% HP
    RemainingLivingFailuresKilled = 13504895  # basically equivalent to Dead flag; enabled by first slot of LF cleanup
    LivingFailureSpawnRequest = 13505668
    ActiveLivingFailuresCountRequest = 13505669
    LivingFailuresPhaseTwo = 13504870  # enabled when meteor attack is first used


class Characters(Character):
    LadyMaria = 3500800
    LadyMariaFriendly = 3500905

    LivingFailuresHealthPool = 3500850
    LivingFailure1 = 3500851
    LivingFailure2 = 3500852
    LivingFailure3 = 3500853
    LivingFailure4 = 3500854
    LivingFailureMeteorCreator = 3500860


class Objects(Object):
    LadyMariaFog = 3501800
    LivingFailuresFog = 3501810


class VFX(VFXEvent):
    LadyMariaFog = 3503800
    LivingFailuresFog = 3503810


class Cutscenes(Cutscene):
    LadyMariaAwakening = 35000010
