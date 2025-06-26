"""NIGHTMARE OF MENSIS"""
from soulstruct.bloodborne.game_types import *


EVENT_INFO = {
    0: ("Constructor", "Event 0"),
    12604700: ("Event12604700", "Event 12604700"),
    12604710: ("Event12604710", "Event 12604710"),
    12604720: ("Event12604720", "Event 12604720"),
    12604730: ("Event12604730", "Event 12604730"),
    12604740: ("Event12604740", "Event 12604740"),
    12604742: ("Event12604742", "Event 12604742"),
    12601800: ("MergosWetNurseDies", "Event 12601800"),
    12601801: ("PlayMergosWetNurseDeathSound", "Event 12601801"),
    12601802: ("MergosWetNurseFirstTime", "Event 12601802"),
    12601803: ("SummonStartMergosWetNurseBattle", "Event 12601803"),
    12604845: ("EnterMergosWetNurseFog", "Event 12604845"),
    12604846: ("EnterMergosWetNurseFogAsSummon", "Event 12604846"),
    12604847: ("Event12604847", "Event 12604847"),
    12604848: ("Event12604848", "Event 12604848"),
    12604802: ("StartMergosWetNurseBattle", "Event 12604802"),
    12604803: ("ControlMergosWetNurseMusic", "Event 12604803"),
    12604804: ("ControlMergosWetNurseCamera", "Event 12604804"),
    12604805: ("StopMergosWetNurseMusic", "Event 12604805"),
    12604806: ("DisableWetNurseClone", "Event 12604806"),
    12604807: ("LogPlayerEffect5630", "Logs when player does not and does have effect 5630 in Wet Nurse battle."),
    12604810: ("WetNurseReactsToPlayerEffect5630", "Event 12604810"),
    12604815: ("PlayWetNurseAmbientSound", "Event 12604815"),
    12604820: ("ChooseMergosWetNurseTeleport", "Event 12604820"),
    12604830: ("MergosWetNurseTeleport", "Event 12604830"),
    12604840: ("MergosWetNurseNightmareMode", "Event 12604840"),
    12601850: ("MicolashDies", "Event 12601850"),
    12601851: ("PlayMicolashDeathSound", "Event 12601851"),
    12601852: ("MicolashFirstTime", "Event 12601852"),
    12601853: ("OpenMicolashTrapGate", "Event 12601853"),
    12601854: ("TriggerMicolashBridgeCutscene", "Event 12601854"),
    12601855: ("SummonStartMicolashBattle", "Event 12601855"),
    12604860: ("EnterMicolashFog", "Event 12604860"),
    12604861: ("EnterMicolashFogAsSummon", "Event 12604861"),
    12604862: ("Event12604862", "Event 12604862"),
    12604863: ("Event12604863", "Event 12604863"),
    12604852: ("StartMicolashBattle", "Event 12604852"),
    12604853: ("ControlMicolashMusic", "Event 12604853"),
    12604854: ("ControlMicolashCamera", "Event 12604854"),
    12604855: ("StopMicolashMusic", "Event 12604855"),
    12604856: ("MicolashPhaseTwoTrigger", "Event 12604856"),
    12604985: ("Event12604985", "Event 12604985"),
    12604986: ("Event12604986", "Event 12604986"),
    12604870: ("MicolashRunsAwayPhase1", "Event 12604870"),
    12604877: ("Event12604877", "Event 12604877"),
    12604878: ("MicolashMirrorTeleport", "Event 12604878"),
    12604956: ("PointlessMicolashEvent", "Only ends when its own flag is enabled, which never seems to happen anywhere in EMEVD."),
    12604879: ("ShutMicolashTrapGate", "Event 12604879"),
    12604880: ("MicolashRunsAwayPhase2", "Event 12604880"),
    12604888: ("Event12604888", "Event 12604888"),
    12604889: ("MicolashDisappearsWhenHitInPhase2", "Event 12604889"),
    12604890: ("KillMicolashPuppet", "Event 12604890"),
    12604910: ("AnimateMicolashPuppet", "Event 12604910"),
    12604930: ("MicolashWaitsInFinalRoom", "Event 12604930"),
    12604931: ("AggravateMicolashEarly", "Aggravate Micolash after three consecutive hits if `required_flag` is on and `ignore_flag` is off."),
    12604960: ("PlayMicolashDialoguePhase1", "Event 12604960"),
    12604970: ("PlayMicolashDialoguePhase2", "Event 12604970"),
    12604000: ("Event12604000", "Event 12604000"),
    12604005: ("Event12604005", "Event 12604005"),
    12600500: ("Event12600500", "Event 12600500"),
    12600020: ("Event12600020", "Event 12600020"),
    12600021: ("Event12600021", "Event 12600021"),
    12600130: ("Event12600130", "Event 12600130"),
    12600150: ("Event12600150", "Event 12600150"),
    12600025: ("Event12600025", "Event 12600025"),
    12600026: ("Event12600026", "Event 12600026"),
    12600027: ("Event12600027", "Event 12600027"),
    12600028: ("Event12600028", "Event 12600028"),
    12600029: ("Event12600029", "Event 12600029"),
    12600010: ("Event12600010", "Event 12600010"),
    12600030: ("Event12600030", "Event 12600030"),
    12600031: ("Event12600031", "Event 12600031"),
    12600035: ("Event12600035", "Event 12600035"),
    12600040: ("Event12600040", "Event 12600040"),
    12600041: ("Event12600041", "Event 12600041"),
    12600047: ("Event12600047", "Event 12600047"),
    12600180: ("Event12600180", "Event 12600180"),
    12600050: ("Event12600050", "Event 12600050"),
    12600060: ("Event12600060", "Event 12600060"),
    12600070: ("Event12600070", "Event 12600070"),
    12600080: ("Event12600080", "Event 12600080"),
    12600090: ("Event12600090", "Event 12600090"),
    12600105: ("Event12600105", "Event 12600105"),
    12600110: ("Event12600110", "Event 12600110"),
    12600120: ("Event12600120", "Event 12600120"),
    12600125: ("Event12600125", "Event 12600125"),
    12600190: ("Event12600190", "Event 12600190"),
    12600400: ("Event12600400", "Event 12600400"),
    12600410: ("Event12600410", "Event 12600410"),
    12600701: ("Event12600701", "Event 12600701"),
    12600703: ("Event12600703", "Event 12600703"),
    12601294: ("Event12601294", "Event 12601294"),
    12601295: ("Event12601295", "Event 12601295"),
    12601310: ("Event12601310", "Event 12601310"),
    12601315: ("Event12601315", "Event 12601315"),
    12601320: ("Event12601320", "Event 12601320"),
    12601330: ("Event12601330", "Event 12601330"),
    12601340: ("Event12601340", "Event 12601340"),
    12601351: ("Event12601351", "Event 12601351"),
    12601352: ("Event12601352", "Event 12601352"),
    12605200: ("Event12605200", "Event 12605200"),
    12600990: ("Event12600990", "Event 12600990"),
    12601050: ("Event12601050", "Event 12601050"),
    12601051: ("Event12601051", "Event 12601051"),
    12607010: ("Event12607010", "Event 12607010"),
    12607020: ("Event12607020", "Event 12607020"),
    12607040: ("Event12607040", "Event 12607040"),
    12607050: ("Event12607050", "Event 12607050"),
}


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


class Cutscenes(Cutscene):
    MicolashBridgeCutscene = 26000000
    MicolashIntro = 26000060


class Music(MusicSound):
    MicolashPhase1 = 2603852
    MicolashPhase2 = 2603853
