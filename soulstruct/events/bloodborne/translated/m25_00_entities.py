from soulstruct.game_types import *


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


class FX(FXEvent):
    BossFog = 2503800
