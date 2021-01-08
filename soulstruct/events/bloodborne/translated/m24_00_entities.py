"""CATHEDRAL WARD"""
from soulstruct.game_types import *


class Flags(Flag):
    VicarAmeliaDead = 12401800
    VicarAmeliaFirstTimeDone = 12401802
    VicarAmeliaFogEntered = 12404800
    VicarAmeliaBattleStarted = 12404802


class Characters(Character):
    BallGiant = 2400205
    OgreWithStatue = 2400231
    VicarAmelia = 2400800
    Amygdala = 2400899


class Objects(Object):
    BossFog = 2401800


class VFX(VFXEvent):
    LaurenceSkull = 2403413  # enabled after fight and before cutscene
    BossFog = 2403800


class Cutscenes(IntEnum):
    CathedralWardFirstArrival = 24000020
    LaurenceFlashback = 24000030
