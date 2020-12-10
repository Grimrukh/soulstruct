"""NIGHTMARE FRONTIER"""
from soulstruct.game_types import *


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


class FX(FXEvent):
    AmygdalaFog1 = 3303800
    AmygdalaFog2 = 3303801
