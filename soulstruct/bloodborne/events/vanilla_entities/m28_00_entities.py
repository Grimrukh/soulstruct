from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    50: ("Preconstructor", "Event 50"),
    12804500: ("Event12804500", "Event 12804500"),
    12805020: ("Event12805020", "Event 12805020"),
    12805030: ("Event12805030", "Event 12805030"),
    12805040: ("Event12805040", "Event 12805040"),
    12805050: ("Event12805050", "Event 12805050"),
    12805140: ("Event12805140", "Event 12805140"),
    12805160: ("Event12805160", "Event 12805160"),
    12805180: ("Event12805180", "Event 12805180"),
    12805460: ("Event12805460", "Event 12805460"),
    12805470: ("Event12805470", "Event 12805470"),
    12805480: ("Event12805480", "Event 12805480"),
    12805490: ("Event12805490", "Event 12805490"),
    12805500: ("Event12805500", "Event 12805500"),
    12805550: ("Event12805550", "Event 12805550"),
    12805570: ("Event12805570", "Event 12805570"),
    12805600: ("Event12805600", "Event 12805600"),
    12805650: ("Event12805650", "Event 12805650"),
    12805660: ("Event12805660", "Event 12805660"),
    12805670: ("Event12805670", "Event 12805670"),
    12805680: ("Event12805680", "Event 12805680"),
    12805700: ("Event12805700", "Event 12805700"),
    12805900: ("Event12805900", "Event 12805900"),
    12805918: ("Event12805918", "Event 12805918"),
    12805920: ("Event12805920", "Event 12805920"),
    12805930: ("Event12805930", "Event 12805930"),
    12804000: ("Event12804000", "Event 12804000"),
    12800100: ("Event12800100", "Event 12800100"),
    12800120: ("Event12800120", "Event 12800120"),
    12800140: ("Event12800140", "Event 12800140"),
    12800160: ("Event12800160", "Event 12800160"),
    12800400: ("Event12800400", "Event 12800400"),
    12800401: ("Event12800401", "Event 12800401"),
    12800402: ("Event12800402", "Event 12800402"),
    12800403: ("Event12800403", "Event 12800403"),
    12800430: ("Event12800430", "Event 12800430"),
    12800431: ("Event12800431", "Event 12800431"),
    12800432: ("Event12800432", "Event 12800432"),
    12800433: ("Event12800433", "Event 12800433"),
    12800435: ("Event12800435", "Event 12800435"),
    12800436: ("Event12800436", "Event 12800436"),
    12800460: ("Event12800460", "Event 12800460"),
    12800470: ("Event12800470", "Event 12800470"),
    12800480: ("Event12800480", "Event 12800480"),
    12800490: ("Event12800490", "Event 12800490"),
    12800500: ("Event12800500", "Event 12800500"),
    12800600: ("Event12800600", "Event 12800600"),
    12800601: ("Event12800601", "Event 12800601"),
    12800602: ("Event12800602", "Event 12800602"),
    12800604: ("Event12800604", "Event 12800604"),
    12800606: ("Event12800606", "Event 12800606"),
    12800607: ("Event12800607", "Event 12800607"),
    12800608: ("Event12800608", "Event 12800608"),
    12800620: ("Event12800620", "Event 12800620"),
    12800700: ("Event12800700", "Event 12800700"),
    12800999: ("Event12800999", "Event 12800999"),
    12801800: ("OneRebornDies", "Event 12801800"),
    12801801: ("PlayOneRebornDeathSound", "Event 12801801"),
    12801802: ("OneRebornFirstTime", "Event 12801802"),
    12801803: ("SummonStartOneRebornBattle", "Event 12801803"),
    12804880: ("EnterOneRebornFog", "Event 12804880"),
    12804881: ("EnterOneRebornFogAsSummon", "Event 12804881"),
    12804882: ("Event12804882", "Event 12804882"),
    12804883: ("Event12804883", "Event 12804883"),
    12804802: ("StartOneRebornBattle", "Event 12804802"),
    12804803: ("ControlOneRebornMusic", "Event 12804803"),
    12804804: ("ControlOneRebornCamera", "Event 12804804"),
    12804805: ("StopOneRebornMusic", "Event 12804805"),
    12804806: ("KeepOneRebornHumanPartAttached", "Event 12804806"),
    12804807: ("MonitorOneRebornStunned", "The flag managed here is only checked once. Everything else just checks the effect directly."),
    12804820: ("OneRebornLimbDamage", "Event 12804820"),
    12804830: ("OneRebornSingleRainOfFlesh", "Event 12804830"),
    12804831: ("OneRebornExplosion", "Event 12804831"),
    12804832: ("OneRebornFootBlast1", "Event 12804832"),
    12804834: ("OneRebornFootBlast2", "Event 12804834"),
    12804835: ("OneRebornFootBlast3", "Event 12804835"),
    12804836: ("OneRebornFootBlast4", "Event 12804836"),
    12804837: ("OneRebornRepeatedRainOfFlesh", "Event 12804837"),
    12804838: ("OneRebornSummonsRepeatedRainOfFlesh", "Event 12804838"),
    12804840: ("OneRebornBuffMaidenDies", "One Reborn gets AI command 1 for 30 seconds after this Maiden is killed."),
    12804850: ("CountDeadOneRebornMaidens", "Event 12804850"),
    12804870: ("OneRebornTakesFirstDamage", "The One Reborn and all Maidens receive AI command 1 when One Reborn's health goes below 100%."),
    12804871: ("OneRebornPhaseTwoTrigger", "The One Reborn goes to phase two at 50% health or when 3+ Maidens are killed."),
    12800990: ("Event12800990", "Event 12800990"),
    12800901: ("Event12800901", "Event 12800901"),
    12800902: ("Event12800902", "Event 12800902"),
    12800903: ("Event12800903", "Event 12800903"),
    12800904: ("Event12800904", "Event 12800904"),
    12800905: ("Event12800905", "Event 12800905"),
    12800906: ("Event12800906", "Event 12800906"),
    12800908: ("Event12800908", "Event 12800908"),
    12800909: ("Event12800909", "Event 12800909"),
    12800910: ("Event12800910", "Event 12800910"),
    12800911: ("Event12800911", "Event 12800911"),
    12800920: ("Event12800920", "Event 12800920"),
    12804450: ("Event12804450", "Event 12804450"),
    12804400: ("Event12804400", "Event 12804400"),
    12804401: ("Event12804401", "Event 12804401"),
    12804410: ("Event12804410", "Event 12804410"),
    12804460: ("Event12804460", "Event 12804460"),
}


class Flags(Flag):
    OneRebornDead = 12801800
    OneRebornFirstTimeDone = 12801802
    OneRebornFogEntered = 12804800
    OneRebornBattleStarted = 12804802
    OneRebornStunned = 12804808
    OneRebornPhaseTwo = 12804871


class Characters(Character):
    OneRebornMaiden1 = 2800520
    OneRebornMaiden2 = 2800522
    OneRebornMaiden3 = 2800524
    OneRebornMaiden4 = 2800525
    OneRebornMaiden5 = 2800527
    OneRebornMaiden6 = 2800529
    OneRebornMain = 2800800
    OneRebornHumanPart = 2800801
    OneRebornBulletCreator = 2800802
    OneRebornHealthPool = 2800803


class Objects(Object):
    OneRebornFog1 = 2801800
    OneRebornFog2 = 2801801


class VFX(VFXEvent):
    OneRebornFog1 = 2803800
    OneRebornFog2 = 2803801


class Cutscenes(Cutscene):
    OneRebornAppears = 28000000


class Effects(SpecialEffectParam):
    OneRebornStunned = 489
