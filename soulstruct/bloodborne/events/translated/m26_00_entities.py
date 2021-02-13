"""NIGHTMARE OF MENSIS"""
from soulstruct.game_types import *


class Flags(Flag):
    MergosWetNurseDead = 12601800
    MergosWetNurseFirstTimeDone = 12601802
    MergosWetNurseFogEntered = 12604800
    MergosWetNurseBattleStarted = 12604802

    MicolashDead = 12601850
    MicolashFirstTimeDone = 12601852
    MicolashFogEntered = 12604850
    MicolashBattleStarted = 12604852
    MicolashPhaseTwo = 12604856
    DismissMicolashPuppets = 12604857
    RequestStopMicolashMusic = 12604858
    MicolashTrapGateShut = 12604879


class Characters(Character):
    MergosWetNurse = 2600800
    MergosWetNurseClone1 = 2600801
    MergosWetNurseClone2 = 2600802
    Micolash = 2600850


class Objects(Object):
    MicolashBridge = 2601250
    MergosWetNurseFog = 2601800
    MicolashFog1 = 2601850
    MicolashFog2 = 2601851
    MicolashTrapGate = 2601852
    MicolashFog3 = 2601859


class Regions(Region):
    MicolashFinalRoom = 2602066


class VFX(VFXEvent):
    MergosWetNurseFog = 2603800
    MicolashFog1 = 2603850
    MicolashFog2 = 2603851
    MicolashFog3 = 2603859


class Cutscenes(IntEnum):
    MicolashBridgeCutscene = 26000000
    MicolashIntro = 26000060


class Music(MusicSound):
    MicolashPhase1 = 2603852
    MicolashPhase2 = 2603853
