"""FISHING HAMLET"""
from soulstruct.game_types import *


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


class FX(FXEvent):
    OrphanFog1 = 3603800
    OrphanFog2 = 3603801


class Cutscenes(IntEnum):
    OrphanBirth = 36000000
    OrphanSpiritDeath = 36000010
