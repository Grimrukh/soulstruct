from soulstruct.game_types import *


class Flags(Flag):
    FirstAwakeningDone = 12410000

    ClericBeastDead = 12411700
    ClericBeastFirstTimeDone = 12411702
    ClericBeastFogEntered = 12414700
    ClericBeastBattleStarted = 12414702

    GascoigneDead = 12411800
    GascoigneFirstTimeDone = 12411802
    GascoigneFogEntered = 12414800
    GascoigneFogEnteredAsSummon = 12414801
    GascoignePhaseTwo = 12414807


class Characters(Character):
    GascoigneSummon = 2410158

    ClericBeast = 2410800
    GascoigneHuman = 2410810
    GascoigneBeast = 2410811


class Objects(Object):
    ClericBeastFog = 2411800


class Cutscenes(IntEnum):
    FirstAwakeningMale = 24010005
    FirstAwakeningFemale = 24011005
    GascoigneFirstFight = 24010010


class RespawnPoints(IntEnum):
    FirstAwakening = 2412959


class FX(FXEvent):
    ClericBeastFog = 2413800


class Effects(SpecialEffectParam):
    MusicBox = 4640
