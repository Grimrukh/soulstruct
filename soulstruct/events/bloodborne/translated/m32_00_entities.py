"""BYRGENWERTH"""
from soulstruct.game_types import *


class Flags(Flag):
    RomDead = 13201800
    RomFirstTimeDone = 13201802
    RomLakeEntered = 13204800  # instead of FogEntered
    RomBattleStarted = 13204802
    RomTeleportedOnce = 13204811
    RomTeleportedTwice = 13204812


class Characters(Character):
    Rom = 3200800
    QueenYharnam = 3200801


class Objects(Object):
    RomFog = 3201800


class Regions(Region):
    RomSecondPoint = 3202806
    RomThirdPoint = 3202807


class FX(FXEvent):
    RomFog = 3203800
