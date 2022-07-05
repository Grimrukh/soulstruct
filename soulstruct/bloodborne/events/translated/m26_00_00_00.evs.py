"""NIGHTMARE OF MENSIS

linked:
300

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス_撃破
52: PC情報_ボス撃破_死と闇レッサー
88: ボス_戦闘開始
104: ボス戦_撃破時間
122: トラップロード_闇魔法_解除状態
156: トラップロード_闇魔法_発動状態
190: PC情報_ボス撃破_トラップロード中ボス
232: トラップロード_中ボス戦_撃破時間
268: PC情報_トラップロード到達時
300: N:\\SPRJ\\data\\Param\\event\\common.emevd
376: 
378: 
380: 
382: 
"""
from soulstruct.bloodborne.events import *
# from .common import GainInsight
from .common_entities import *
from .m26_00_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=30, args=(2600950, 2601950, 999, 12607800))
    RunEvent(7000, slot=31, args=(2600951, 2601951, Flags.MergosWetNurseDead, 12607820))
    RunEvent(7000, slot=32, args=(2600952, 2601952, 999, 12607840))
    RunEvent(7000, slot=33, args=(2600953, 2601953, 999, 12607860))
    RunEvent(7100, slot=30, args=(72600200, 2601950))
    RunEvent(7100, slot=31, args=(72600201, 2601951))
    RunEvent(7100, slot=32, args=(72600202, 2601952))
    RunEvent(7100, slot=33, args=(72600203, 2601953))
    RunEvent(7200, slot=30, args=(72600100, 2601950, 2102953))
    RunEvent(7200, slot=31, args=(72600101, 2601951, 2102953))
    RunEvent(7200, slot=32, args=(72600102, 2601952, 2102953))
    RunEvent(7200, slot=33, args=(72600103, 2601953, 2102953))
    RunEvent(7300, slot=30, args=(72102600, 2601950))
    RunEvent(7300, slot=31, args=(72102601, 2601951))
    RunEvent(7300, slot=32, args=(72102602, 2601952))
    RunEvent(7300, slot=33, args=(72102603, 2601953))
    RunEvent(9200, slot=6, args=(2603900,))
    StartPlayLogMeasurement(2600000, 0, overwrite=False)
    StartPlayLogMeasurement(2600001, 18, overwrite=True)
    Event12600990()
    RunEvent(12604700, slot=0, args=(2600700, 12604701, 12604711, 2600, 12604741, 12601700))
    RunEvent(12604700, slot=5, args=(2600701, 12604702, 12604712, 2601, 12604743, 12601701))
    RunEvent(12604710, slot=0, args=(2600700, 12604701, 12604711, 12604721, 12604741))
    RunEvent(12604710, slot=5, args=(2600701, 12604702, 12604712, 12604722, 12604743))
    RunEvent(12604720, slot=0, args=(2600700, 12604701, 12604711, 12604721, 12604741))
    RunEvent(12604720, slot=5, args=(2600701, 12604702, 12604712, 12604722, 12604743))
    RunEvent(12604730, slot=0, args=(2600700, 12604701, 12604711, 2600, 12604731, 12601700, 12604741))
    RunEvent(12604730, slot=5, args=(2600701, 12604702, 12604712, 2601, 12604732, 12601701, 12604743))
    Event12604740()
    Event12604742()

    # MERGO'S WET NURSE
    Event12604847()
    Event12604848()
    MergosWetNurseDies()
    PlayMergosWetNurseDeathSound()
    MergosWetNurseFirstTime()
    EnterMergosWetNurseFog()
    EnterMergosWetNurseFogAsSummon()
    StartMergosWetNurseBattle()
    ControlMergosWetNurseMusic()
    ControlMergosWetNurseCamera()
    StopMergosWetNurseMusic()
    LogPlayerEffect5630()
    SummonStartMergosWetNurseBattle()
    ChooseMergosWetNurseTeleport(0, Characters.MergosWetNurse, 12605880, 12605885)
    MergosWetNurseTeleport(0, Characters.MergosWetNurse, 12605880, 2602830, 2602831)
    MergosWetNurseTeleport(1, Characters.MergosWetNurse, 12605881, 2602831, 2602832)
    MergosWetNurseTeleport(2, Characters.MergosWetNurse, 12605882, 2602832, 2602830)
    MergosWetNurseTeleport(3, Characters.MergosWetNurse, 12605883, 2602833, 2602834)
    MergosWetNurseTeleport(4, Characters.MergosWetNurse, 12605884, 2602834, 2602835)
    MergosWetNurseTeleport(5, Characters.MergosWetNurse, 12605885, 2602835, 2602833)
    DisableWetNurseClone()
    WetNurseReactsToPlayerEffect5630()
    MergosWetNurseNightmareMode()
    PlayWetNurseAmbientSound()

    # MICOLASH, HOST OF THE NIGHTMARE
    Event12604862()
    Event12604863()
    MicolashDies()
    PlayMicolashDeathSound()
    MicolashFirstTime()
    OpenMicolashTrapGate()
    EnterMicolashFog()
    EnterMicolashFogAsSummon()
    StartMicolashBattle()
    ControlMicolashMusic()
    ControlMicolashCamera()
    StopMicolashMusic()
    MicolashPhaseTwoTrigger()
    Event12604985()
    Event12604986()
    TriggerMicolashBridgeCutscene()
    SummonStartMicolashBattle()
    # These control Micolash's behavior at the six corners/intersections in the Phase 1 area.
    MicolashRunsAwayPhase1(0, 2602040, 2602042, 2602041, 2602042, 2602042, 12604942, 12604941, 12604942)
    MicolashRunsAwayPhase1(1, 2602041, 2602043, 2602040, 2602043, 2602043, 12604943, 12604940, 12604943)
    MicolashRunsAwayPhase1(2, 2602042, 2602040, 2602044, 2602040, 2602044, 12604940, 12604944, 12604940)
    MicolashRunsAwayPhase1(3, 2602043, 2602046, 2602045, 2602041, 2602046, 12604946, 12604945, 12604941)
    MicolashRunsAwayPhase1(4, 2602044, 2602042, 2602042, 2602045, 2602042, 12604942, 12604942, 12604945)
    MicolashRunsAwayPhase1(5, 2602045, 2602043, 2602043, 2602044, 2602043, 12604943, 12604943, 12604944)
    Event12604877()
    Event12604888()
    MicolashMirrorTeleport()
    MicolashRunsAwayPhase2(0, 2602060, 2602062, 2602061, 2602062, 12604952, 12604951, 12604952, 2602070)
    MicolashRunsAwayPhase2(1, 2602061, 2602065, 2602060, 2602065, 12604955, 12604950, 12604955, 2602070)
    MicolashRunsAwayPhase2(2, 2602062, 2602063, 2602063, 2602060, 12604953, 12604953, 12604950, 2602070)
    MicolashRunsAwayPhase2(3, 2602063, 2602064, 2602064, 2602064, 12604954, 12604954, 12604954, 2602070)
    MicolashRunsAwayPhase2(  # Requires flag from `PointlessMicolashEvent`.
        4, 2602065, Regions.MicolashFinalRoom, 2602067, 2602061, 12604956, 12604957, 12604951, 2602079)
    MicolashRunsAwayPhase2(5, 2602067, 2602065, 2602065, 2602068, 12604955, 12604955, 12604958, 2602070)
    MicolashRunsAwayPhase2(6, 2602068, 2602069, 2602069, 2602067, 12604959, 12604959, 12604957, 2602070)
    MicolashRunsAwayPhase2(7, 2602059, 2602065, 2602065, 2602065, 12604955, 12604955, 12604955, 2602070)
    PointlessMicolashEvent()
    ShutMicolashTrapGate()
    MicolashWaitsInFinalRoom()
    MicolashDisappearsWhenHitInPhase2()
    KillMicolashPuppet(1, 2600161, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(2, 2600162, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(3, 2600163, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(4, 2600164, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(5, 2600165, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(7, 2600167, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(9, 2600169, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(10, 2600170, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(11, 2600171, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(12, 2600172, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(13, 2600173, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(15, 2600175, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(16, 2600176, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(17, 2600177, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(18, 2600178, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    KillMicolashPuppet(19, 2600179, Flags.MicolashDead, Flags.DismissMicolashPuppets)
    AnimateMicolashPuppet(1, 2600161, Flags.MicolashDead)
    AnimateMicolashPuppet(2, 2600162, Flags.MicolashDead)
    AnimateMicolashPuppet(3, 2600163, Flags.MicolashDead)
    AnimateMicolashPuppet(4, 2600164, Flags.MicolashDead)
    AnimateMicolashPuppet(5, 2600165, Flags.MicolashDead)
    AnimateMicolashPuppet(7, 2600167, Flags.MicolashDead)
    AnimateMicolashPuppet(9, 2600169, Flags.MicolashDead)
    AnimateMicolashPuppet(10, 2600170, Flags.MicolashDead)
    AnimateMicolashPuppet(11, 2600171, Flags.MicolashDead)
    AnimateMicolashPuppet(12, 2600172, Flags.MicolashDead)
    AnimateMicolashPuppet(13, 2600173, Flags.MicolashDead)
    AnimateMicolashPuppet(15, 2600175, Flags.MicolashDead)
    AnimateMicolashPuppet(16, 2600176, Flags.MicolashDead)
    AnimateMicolashPuppet(17, 2600177, Flags.MicolashDead)
    AnimateMicolashPuppet(18, 2600178, Flags.MicolashDead)
    AnimateMicolashPuppet(19, 2600179, Flags.MicolashDead)
    AggravateMicolashEarly(0, 12604946, Flags.MicolashPhaseTwo)
    AggravateMicolashEarly(1, 12604956, Flags.MicolashDead)  # Requires flag from `PointlessMicolashEvent`.
    PlayMicolashDialoguePhase1(0, 2602040)
    PlayMicolashDialoguePhase1(1, 2602041)
    PlayMicolashDialoguePhase1(2, 2602042)
    PlayMicolashDialoguePhase1(3, 2602043)
    PlayMicolashDialoguePhase1(4, 2602044)
    PlayMicolashDialoguePhase1(5, 2602045)
    PlayMicolashDialoguePhase1(6, 2602046)
    PlayMicolashDialoguePhase2(0, 2602060)
    PlayMicolashDialoguePhase2(1, 2602061)
    PlayMicolashDialoguePhase2(2, 2602062)
    PlayMicolashDialoguePhase2(3, 2602063)
    PlayMicolashDialoguePhase2(4, 2602064)
    PlayMicolashDialoguePhase2(5, 2602065)
    PlayMicolashDialoguePhase2(6, Regions.MicolashFinalRoom)
    PlayMicolashDialoguePhase2(7, 2602067)
    PlayMicolashDialoguePhase2(8, 2602068)
    PlayMicolashDialoguePhase2(9, 2602059)
    PlayRandomMicolashTAEDialogue(0, 20, 72600307, 72600311, 72600307, 72600311, 72600311, 72600306)
    PlayRandomMicolashTAEDialogue(1, 10, 72600312, 72600316, 72600312, 72600316, 72600316, 72600306)

    RunEvent(12600020, slot=0, args=(2600100, 2600101))
    Event12600021()
    Event12600025()
    Event12600026()
    Event12600027()
    Event12600028()
    Event12600029()
    RunEvent(12600500, slot=0, args=(2600720,))
    Event12600030()
    Event12600031()
    DisableSoundEvent(2603100)
    RunEvent(12600010, slot=0, args=(2602301, 260000001, 0))
    RunEvent(12600010, slot=1, args=(2602302, 260000001, 0))
    RunEvent(12600010, slot=2, args=(2602303, 260000001, 0))
    RunEvent(12600010, slot=3, args=(2602304, 260000001, 0))
    RunEvent(12600010, slot=4, args=(2602305, 260000001, 0))
    RunEvent(12600010, slot=5, args=(2602310, 2603100, 1))
    RunEvent(12600130, slot=0, args=(10000,))
    RunEvent(12600130, slot=1, args=(10000,))
    RunEvent(12600130, slot=2, args=(10000,))
    RunEvent(12600130, slot=3, args=(2600104,))
    RunEvent(12600130, slot=4, args=(2600113,))
    RunEvent(12600130, slot=5, args=(2600150,))
    RunEvent(12600130, slot=6, args=(2600153,))
    RunEvent(12600130, slot=7, args=(2600155,))
    RunEvent(12600130, slot=8, args=(2600201,))
    RunEvent(12600130, slot=9, args=(2600180,))
    RunEvent(12600130, slot=10, args=(2600181,))
    RunEvent(12600130, slot=11, args=(2600182,))
    RunEvent(12600130, slot=12, args=(2600183,))
    RunEvent(12600130, slot=13, args=(2600103,))
    RunEvent(12600150, slot=0, args=(10000,))
    RunEvent(12600150, slot=1, args=(2600104,))
    RunEvent(12600150, slot=2, args=(2600113,))
    RunEvent(12600150, slot=3, args=(2600150,))
    RunEvent(12600150, slot=4, args=(2600153,))
    RunEvent(12600150, slot=5, args=(2600155,))
    RunEvent(12600150, slot=6, args=(2600201,))
    RunEvent(12600150, slot=7, args=(2600180,))
    RunEvent(12600150, slot=8, args=(2600181,))
    RunEvent(12600150, slot=9, args=(2600182,))
    RunEvent(12600150, slot=10, args=(2600183,))
    RunEvent(12600150, slot=11, args=(2600103,))
    Event12601294()
    RunEvent(12601295, slot=0, args=(2601211, 12601294, 12605250, 12601250, 0), arg_types="iiiiB")
    RunEvent(12601295, slot=1, args=(2601212, 12601294, 12605250, 12601250, 1), arg_types="iiiiB")
    RunEvent(12601295, slot=2, args=(2601221, 12601331, 12605251, 12601251, 0), arg_types="iiiiB")
    RunEvent(12601295, slot=3, args=(2601222, 12601331, 12605251, 12601251, 1), arg_types="iiiiB")
    RunEvent(12601295, slot=4, args=(2601231, 12601294, 12605252, 12601252, 0), arg_types="iiiiB")
    RunEvent(12601295, slot=5, args=(2601232, 12601294, 12605252, 12601252, 1), arg_types="iiiiB")
    RunEvent(12601295, slot=6, args=(2601241, 12601323, 12605256, 12601256, 1), arg_types="iiiiB")
    RunEvent(12601295, slot=7, args=(2601242, 12601323, 12605256, 12601256, 0), arg_types="iiiiB")
    RunEvent(12601295, slot=8, args=(2601281, 12601334, 12605253, 12601254, 0), arg_types="iiiiB")
    RunEvent(12601295, slot=9, args=(2601282, 12601334, 12605253, 12601254, 1), arg_types="iiiiB")
    RunEvent(12601295, slot=10, args=(2601291, 12601335, 12605254, 12601255, 0), arg_types="iiiiB")
    RunEvent(12601295, slot=11, args=(2601292, 12601335, 12605254, 12601255, 1), arg_types="iiiiB")
    RunEvent(12601340, slot=0, args=(12601331, 12601251, 2601221))
    RunEvent(12601340, slot=1, args=(12601334, 12601254, 2601281))
    RunEvent(12601340, slot=2, args=(12601335, 12601255, 2601291))
    RunEvent(12601310, slot=0, args=(12601250, 2601210, 2601211, 2601212, 12601294))
    RunEvent(12601310, slot=1, args=(12601251, 2601220, 2601221, 2601222, 12601331))
    RunEvent(12601310, slot=2, args=(12601252, 2601230, 2601231, 2601232, 12601294))
    RunEvent(12601315, slot=0, args=(12601256, 2601240, 2601241, 2601242, 12601323))
    RunEvent(12601310, slot=3, args=(12601254, 2601280, 2601281, 2601282, 12601334))
    RunEvent(12601310, slot=4, args=(12601255, 2601290, 2601291, 2601292, 12601335))
    RunEvent(12601320, slot=0, args=(12605250, 12601250, 2602211, 2602212, 2601211, 2601212, 2601210, 12601211))
    RunEvent(12601330, slot=0, args=(12605250, 12601250, 2602211, 2602212, 2601211, 2601212, 2601210, 12601211))
    RunEvent(12601320, slot=1, args=(12605251, 12601251, 2602221, 2602222, 2601221, 2601222, 2601220, 12601221))
    RunEvent(12601330, slot=1, args=(12605251, 12601251, 2602221, 2602222, 2601221, 2601222, 2601220, 12601221))
    RunEvent(12601320, slot=2, args=(12605252, 12601252, 2602231, 2602232, 2601231, 2601232, 2601230, 12601231))
    RunEvent(12601330, slot=2, args=(12605252, 12601252, 2602231, 2602232, 2601231, 2601232, 2601230, 12601231))
    RunEvent(12601320, slot=3, args=(12605256, 12601256, 2602252, 2602251, 2601242, 2601241, 2601240, 12601241))
    RunEvent(12601330, slot=3, args=(12605256, 12601256, 2602252, 2602251, 2601242, 2601241, 2601240, 12601241))
    RunEvent(12601320, slot=4, args=(12605253, 12601254, 2602281, 2602282, 2601281, 2601282, 2601280, 12601281))
    RunEvent(12601330, slot=4, args=(12605253, 12601254, 2602281, 2602282, 2601281, 2601282, 2601280, 12601281))
    RunEvent(12601320, slot=5, args=(12605254, 12601255, 2602291, 2602292, 2601291, 2601292, 2601290, 12601291))
    RunEvent(12601330, slot=5, args=(12605254, 12601255, 2602291, 2602292, 2601291, 2601292, 2601290, 12601291))
    RunEvent(12601351, slot=0, args=(Flags.MicolashDead, 2601260, 2601261))
    Event12601352()
    RunEvent(12605200, slot=0, args=(2600300, 2600310))
    RunEvent(12605200, slot=1, args=(2600301, 2600311))
    RunEvent(12605200, slot=2, args=(2600302, 2600312))
    RunEvent(12605200, slot=3, args=(2600303, 2600313))
    RunEvent(12600080, slot=0, args=(2600183, 7011, 7013, 7014))
    RunEvent(12600040, slot=0, args=(2602001, 2600105, 2602004, 10000, 2602015))
    RunEvent(12600041, slot=0, args=(2600105,))
    RunEvent(12600041, slot=1, args=(2600111,))
    RunEvent(12600041, slot=2, args=(2600106,))
    RunEvent(12600041, slot=3, args=(2600195,))
    RunEvent(12600041, slot=4, args=(2600196,))
    RunEvent(12600041, slot=5, args=(2600197,))
    RunEvent(12600047, slot=1, args=(2600109,))
    RunEvent(12600047, slot=2, args=(2600110,))
    RunEvent(12600047, slot=3, args=(2600198,))
    RunEvent(12600180, slot=0, args=(2600106, 22502610))
    RunEvent(12600400, slot=0, args=(2600400, 52600990))
    RunEvent(12600400, slot=1, args=(2600401, 52600980))
    RunEvent(12600400, slot=2, args=(2600402, 52600970))
    RunEvent(12600400, slot=3, args=(2600403, 52600960))
    RunEvent(12600400, slot=4, args=(2600404, 52600950))
    Event12600410()
    RunEvent(12600050, slot=0, args=(2600134, 2602020))
    RunEvent(12600050, slot=1, args=(2600135, 2602020))
    RunEvent(12600050, slot=2, args=(2600136, 2602020))
    RunEvent(12600050, slot=3, args=(2600137, 2602020))
    RunEvent(12600050, slot=4, args=(2600138, 2602031))
    RunEvent(12600050, slot=5, args=(2600139, 2602031))
    RunEvent(12600050, slot=6, args=(2600140, 2602020))
    RunEvent(12600050, slot=7, args=(2600141, 2602031))
    RunEvent(12600050, slot=8, args=(2600102, 2602020))
    RunEvent(12600035, slot=0, args=(2600104,))
    RunEvent(12600035, slot=1, args=(2600201,))
    RunEvent(12600035, slot=2, args=(2600190,))
    RunEvent(12600035, slot=3, args=(2600220,))
    RunEvent(12600035, slot=4, args=(2600221,))
    RunEvent(12600190, slot=0, args=(2600191, 2600192))
    RunEvent(12600190, slot=1, args=(2600192, 2600191))
    RunEvent(12600110, slot=0, args=(2600104, 2600210, 2600211))
    RunEvent(12600110, slot=1, args=(2600113, 2600212, 2600213))
    RunEvent(12600110, slot=2, args=(2600201, 2600214, 2600215))
    RunEvent(12600110, slot=3, args=(2600103, 2600216, 2600217))
    RunEvent(12600070, slot=0, args=(2600114, 2602012, 16.0), arg_types="iif")
    RunEvent(12600070, slot=3, args=(2600117, 2602013, 15.0), arg_types="iif")
    RunEvent(12600070, slot=4, args=(2600118, 2602014, 15.0), arg_types="iif")
    RunEvent(12600070, slot=5, args=(2600119, 2602014, 15.0), arg_types="iif")
    RunEvent(12600105, slot=0, args=(2600123, 7010, 7011, 2600120, 2600121, 2600122))
    RunEvent(12600105, slot=1, args=(2600145, 7010, 7011, 2600125, 2600126, 0))
    RunEvent(12600060, slot=0, args=(2600120, 9001, 9060))
    RunEvent(12600060, slot=1, args=(2600121, 9000, 9060))
    RunEvent(12600060, slot=2, args=(2600122, 9000, 9060))
    RunEvent(12600060, slot=3, args=(2600125, 9000, 9060))
    RunEvent(12600060, slot=4, args=(2600126, 9001, 9060))
    RunEvent(12600060, slot=5, args=(2600129, 9000, 9060))
    RunEvent(12600090, slot=0, args=(2600107, 2602008))
    RunEvent(12600090, slot=1, args=(2600108, 2602009))
    RunEvent(12600090, slot=2, args=(2600116, 2602009))
    RunEvent(12600090, slot=3, args=(2600202, 2602005))
    RunEvent(12600120, slot=0, args=(12601000, 2601005))
    RunEvent(12600120, slot=1, args=(12601001, 2601006))
    RunEvent(12600120, slot=2, args=(12601002, 2601007))
    RunEvent(12600120, slot=3, args=(12601003, 2601009))
    RunEvent(12600125, slot=0, args=(2601008, 2600570))
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6314)
    EnableFlag(12601999)
    SkipLinesIfFlagEnabled(5, 12601999)
    EnableObject(2601500)
    DisableObject(2601501)
    EnableTreasure(2601500)
    DisableTreasure(2601501)
    SkipLines(4)
    DisableObject(2601500)
    EnableObject(2601501)
    DisableTreasure(2601500)
    EnableTreasure(2601501)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6315)
    EnableFlag(12601998)
    SkipLinesIfFlagEnabled(5, 12601998)
    EnableObject(2601502)
    DisableObject(2601503)
    EnableTreasure(2601502)
    DisableTreasure(2601503)
    SkipLines(4)
    DisableObject(2601502)
    EnableObject(2601503)
    DisableTreasure(2601502)
    EnableTreasure(2601503)
    Event12601050()
    Event12601051()
    Event12600701()
    Event12600703()


@RestartOnRest
def Event12604700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12604700: Event 12604700 """
    GotoIfFlagDisabled(Label.L0, arg_8_11)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(arg_4_7)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010, loop=True)
    IfOnline(1)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfCharacterHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, 30)
    SkipLinesIfFlagDisabled(1, arg_20_23)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, arg_20_23)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(arg_0_3, 7011)
    WaitFrames(59)
    EnableAI(arg_0_3)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event12604710(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12604710: Event 12604710 """
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_8_11)
    IfFlagEnabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, value=0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    IfRandomTimeElapsed(2, min_seconds=10.0, max_seconds=10.0)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(PLAYER, 9020, affect_npc_part_hp=False)
    AddSpecialEffect(arg_0_3, 9100, affect_npc_part_hp=False)
    ReplanAI(arg_0_3)
    EnableFlag(arg_12_15)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    Restart()


@RestartOnRest
def Event12604720(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12604720: Event 12604720 """
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_12_15)
    IfFlagEnabled(-1, arg_8_11)
    IfClientTypeCountComparison(-1, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfFlagDisabled(-1, arg_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(arg_0_3, 9100)
    ReplanAI(arg_0_3)
    DisableFlag(arg_12_15)
    Restart()


@RestartOnRest
def Event12604730(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12604730: Event 12604730 """
    IfFlagEnabled(-15, arg_8_11)
    IfFlagEnabled(-15, arg_12_15)
    IfFlagEnabled(-15, arg_16_19)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_24_27)
    IfHealthEqual(2, arg_0_3, 0.0)
    IfFlagEnabled(3, arg_16_19)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_8_11)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    EnableFlag(arg_20_23)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7012)
    WaitFrames(88)
    ForceAnimation(arg_0_3, 7010)


@RestartOnRest
def Event12604740():
    """ 12604740: Event 12604740 """
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2604000)
    IfPlayerStandingOnCollision(-1, 2604001)
    IfPlayerStandingOnCollision(-1, 2604002)
    IfPlayerStandingOnCollision(-1, 2604003)
    IfPlayerStandingOnCollision(-1, 2604004)
    IfPlayerStandingOnCollision(-1, 2604005)
    IfPlayerStandingOnCollision(-1, 2604006)
    IfPlayerStandingOnCollision(-1, 2604007)
    IfPlayerStandingOnCollision(-1, 2604008)
    IfPlayerStandingOnCollision(-1, 2604009)
    IfPlayerStandingOnCollision(-1, 2604010)
    IfPlayerStandingOnCollision(-1, 2604011)
    IfPlayerStandingOnCollision(-1, 2604012)
    IfPlayerStandingOnCollision(-1, 2604013)
    IfPlayerStandingOnCollision(-1, 2604014)
    IfPlayerStandingOnCollision(-1, 2604015)
    IfPlayerStandingOnCollision(-1, 2604016)
    IfPlayerStandingOnCollision(-1, 2604017)
    IfPlayerStandingOnCollision(-1, 2604018)
    IfPlayerStandingOnCollision(-1, 2604019)
    IfPlayerStandingOnCollision(-1, 2604020)
    IfPlayerStandingOnCollision(-1, 2604021)
    IfPlayerStandingOnCollision(-1, 2604022)
    IfPlayerStandingOnCollision(-1, 2604023)
    IfPlayerStandingOnCollision(-1, 2604024)
    IfPlayerStandingOnCollision(-1, 2604025)
    IfPlayerStandingOnCollision(-1, 2604026)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12604741)
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2604000)
    IfPlayerStandingOnCollision(-1, 2604001)
    IfPlayerStandingOnCollision(-1, 2604002)
    IfPlayerStandingOnCollision(-1, 2604003)
    IfPlayerStandingOnCollision(-1, 2604004)
    IfPlayerStandingOnCollision(-1, 2604005)
    IfPlayerStandingOnCollision(-1, 2604006)
    IfPlayerStandingOnCollision(-1, 2604007)
    IfPlayerStandingOnCollision(-1, 2604008)
    IfPlayerStandingOnCollision(-1, 2604009)
    IfPlayerStandingOnCollision(-1, 2604010)
    IfPlayerStandingOnCollision(-1, 2604011)
    IfPlayerStandingOnCollision(-1, 2604012)
    IfPlayerStandingOnCollision(-1, 2604013)
    IfPlayerStandingOnCollision(-1, 2604014)
    IfPlayerStandingOnCollision(-1, 2604015)
    IfPlayerStandingOnCollision(-1, 2604016)
    IfPlayerStandingOnCollision(-1, 2604017)
    IfPlayerStandingOnCollision(-1, 2604018)
    IfPlayerStandingOnCollision(-1, 2604019)
    IfPlayerStandingOnCollision(-1, 2604020)
    IfPlayerStandingOnCollision(-1, 2604021)
    IfPlayerStandingOnCollision(-1, 2604022)
    IfPlayerStandingOnCollision(-1, 2604023)
    IfPlayerStandingOnCollision(-1, 2604024)
    IfPlayerStandingOnCollision(-1, 2604025)
    IfPlayerStandingOnCollision(-1, 2604026)
    IfConditionFalse(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12604741)
    Restart()


@RestartOnRest
def Event12604742():
    """ 12604742: Event 12604742 """
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2604100)
    IfPlayerStandingOnCollision(-1, 2604101)
    IfPlayerStandingOnCollision(-1, 2604102)
    IfPlayerStandingOnCollision(-1, 2604103)
    IfPlayerStandingOnCollision(-1, 2604104)
    IfPlayerStandingOnCollision(-1, 2604105)
    IfPlayerStandingOnCollision(-1, 2604106)
    IfPlayerStandingOnCollision(-1, 2604107)
    IfPlayerStandingOnCollision(-1, 2604108)
    IfPlayerStandingOnCollision(-1, 2604109)
    IfPlayerStandingOnCollision(-1, 2604110)
    IfPlayerStandingOnCollision(-1, 2604111)
    IfPlayerStandingOnCollision(-1, 2604112)
    IfPlayerStandingOnCollision(-1, 2604113)
    IfPlayerStandingOnCollision(-1, 2604114)
    IfPlayerStandingOnCollision(-1, 2604115)
    IfPlayerStandingOnCollision(-1, 2604116)
    IfPlayerStandingOnCollision(-1, 2604117)
    IfPlayerStandingOnCollision(-1, 2604118)
    IfPlayerStandingOnCollision(-1, 2604119)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12604743)
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 2604100)
    IfPlayerStandingOnCollision(-1, 2604101)
    IfPlayerStandingOnCollision(-1, 2604102)
    IfPlayerStandingOnCollision(-1, 2604103)
    IfPlayerStandingOnCollision(-1, 2604104)
    IfPlayerStandingOnCollision(-1, 2604105)
    IfPlayerStandingOnCollision(-1, 2604106)
    IfPlayerStandingOnCollision(-1, 2604107)
    IfPlayerStandingOnCollision(-1, 2604108)
    IfPlayerStandingOnCollision(-1, 2604109)
    IfPlayerStandingOnCollision(-1, 2604110)
    IfPlayerStandingOnCollision(-1, 2604111)
    IfPlayerStandingOnCollision(-1, 2604112)
    IfPlayerStandingOnCollision(-1, 2604113)
    IfPlayerStandingOnCollision(-1, 2604114)
    IfPlayerStandingOnCollision(-1, 2604115)
    IfPlayerStandingOnCollision(-1, 2604116)
    IfPlayerStandingOnCollision(-1, 2604117)
    IfPlayerStandingOnCollision(-1, 2604118)
    IfPlayerStandingOnCollision(-1, 2604119)
    IfConditionFalse(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12604743)
    Restart()


def MergosWetNurseDies():
    """ 12601800: Event 12601800 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(2603802)
    DisableSoundEvent(2603803)
    DisableCharacter(Characters.MergosWetNurse)
    DisableCharacter(Characters.MergosWetNurseClone1)
    DisableCharacter(Characters.MergosWetNurseClone2)
    DisableObject(Objects.MergosWetNurseFog)
    DeleteVFX(VFX.MergosWetNurseFog, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthLessThanOrEqual(0, Characters.MergosWetNurseClone2, 0.0)
    ResetAnimation(Characters.MergosWetNurse, disable_interpolation=True)
    ResetAnimation(Characters.MergosWetNurseClone1, disable_interpolation=True)
    Kill(Characters.MergosWetNurse, award_souls=False)
    Kill(Characters.MergosWetNurseClone1, award_souls=False)
    IfCharacterDead(0, Characters.MergosWetNurse)
    EnableFlag(12604808)
    Wait(3.0)
    PlaySoundEffect(anchor_entity=2602300, sound_type=SoundType.a_Ambient, sound_id=260000004)  # Mergo crying.
    Wait(18.0)
    DisplayBanner(BannerType.NightmareSlain)
    DisableObject(Objects.MergosWetNurseFog)
    DeleteVFX(VFX.MergosWetNurseFog, erase_root_only=True)
    SetLockedCameraSlot(game_map=NIGHTMARE_OF_MENSIS, camera_slot=0)
    CancelSpecialEffect(PLAYER, 5630)
    Wait(3.0)
    KillBoss(2600803)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(3,))
    AwardAchievement(20)
    AwardItemLot(55100000, host_only=False)
    EnableFlag(2601)
    EnableFlag(9462)
    StopPlayLogMeasurement(2600000)
    StopPlayLogMeasurement(2600001)
    StopPlayLogMeasurement(2600010)
    CreatePlayLog(40)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 52, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayMergosWetNurseDeathSound():
    """ 12601801: Event 12601801 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MergosWetNurseDead)
    IfFlagEnabled(1, Flags.MergosWetNurseDead)
    IfCharacterBackreadDisabled(2, Characters.MergosWetNurse)
    IfHealthLessThanOrEqual(2, Characters.MergosWetNurseClone2, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2602800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def MergosWetNurseFirstTime():
    """ 12601802: Event 12601802 """
    EndIfFlagEnabled(Flags.MergosWetNurseDead)
    EndIfThisEventFlagEnabled()
    DisableCharacter(Characters.MergosWetNurse)
    DisableCharacter(Characters.MergosWetNurseClone1)
    EnableObjectInvulnerability(2601856)
    IfFlagDisabled(1, Flags.MergosWetNurseDead)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2602805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12604732)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(CommonFlags.CutsceneActive)
    DisableSoundEvent(2603100)
    WaitFrames(1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(26000010, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(26000010, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    DisableObjectInvulnerability(2601856)
    PostDestruction(2601856)
    EnableFlag(Flags.MergosWetNurseFogEntered)
    EnableCharacter(Characters.MergosWetNurse)
    EndIfFlagEnabled(9306)
    RunEvent(9350, 0, args=(3,))
    EnableFlag(9306)


def SummonStartMergosWetNurseBattle():
    """ 12601803: Event 12601803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.MergosWetNurseFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    DisableObjectInvulnerability(2601856)
    PostDestruction(2601856)
    EnableCharacter(Characters.MergosWetNurse)
    EnableFlag(Flags.MergosWetNurseFogEntered)
    EnableFlag(Flags.MergosWetNurseFirstTimeDone)


def EnterMergosWetNurseFog():
    """ 12604845: Event 12604845 """
    EndIfFlagEnabled(Flags.MergosWetNurseDead)
    GotoIfFlagEnabled(Label.L0, Flags.MergosWetNurseFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.MergosWetNurseFog)
    DeleteVFX(VFX.MergosWetNurseFog, erase_root_only=False)
    IfFlagDisabled(1, Flags.MergosWetNurseDead)
    IfFlagEnabled(1, Flags.MergosWetNurseFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.MergosWetNurseFog)
    CreateVFX(VFX.MergosWetNurseFog)

    # --- 0 --- #
    DefineLabel(0)
    PostDestruction(2601856)
    IfFlagDisabled(2, Flags.MergosWetNurseDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2600800, entity=Objects.MergosWetNurseFog)
    IfFlagEnabled(3, Flags.MergosWetNurseDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2602800, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2602801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.MergosWetNurseFogEntered)
    Restart()


def EnterMergosWetNurseFogAsSummon():
    """ 12604846: Event 12604846 """
    DisableNetworkSync()
    IfFlagDisabled(1, Flags.MergosWetNurseDead)
    IfFlagEnabled(1, Flags.MergosWetNurseFirstTimeDone)
    IfFlagEnabled(1, Flags.MergosWetNurseFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2600800, entity=Objects.MergosWetNurseFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2602800, animation=101130, wait_for_completion=True)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2602801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12604801)
    Restart()


def Event12604847():
    """ 12604847: Event 12604847 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.MergosWetNurseFog, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12604848():
    """ 12604848: Event 12604848 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.MergosWetNurseFog, radius=4.0)
    IfEntityWithinDistance(1, PLAYER, Objects.MergosWetNurseFog, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def StartMergosWetNurseBattle():
    """ 12604802: Event 12604802 """
    EndIfFlagEnabled(Flags.MergosWetNurseDead)
    DisableAI(Characters.MergosWetNurse)
    DisableAI(Characters.MergosWetNurseClone1)
    DisableAI(Characters.MergosWetNurseClone2)
    DisableHealthBar(Characters.MergosWetNurse)
    DisableHealthBar(Characters.MergosWetNurseClone1)
    DisableHealthBar(Characters.MergosWetNurseClone2)
    DisableGravity(Characters.MergosWetNurseClone2)
    EnableImmortality(Characters.MergosWetNurse)
    EnableImmortality(Characters.MergosWetNurseClone1)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.MergosWetNurseFogEntered)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 12604732)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.MergosWetNurse, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.MergosWetNurseClone1, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.MergosWetNurseClone2, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12604732)
    EnableFlag(Flags.MergosWetNurseFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.MergosWetNurse, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.MergosWetNurseClone1, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.MergosWetNurseClone2, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.MergosWetNurse)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.MergosWetNurseClone1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.MergosWetNurseClone2)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.MergosWetNurse, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.MergosWetNurseClone1, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.MergosWetNurseClone2, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.MergosWetNurse)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.MergosWetNurseClone1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.MergosWetNurseClone2)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.MergosWetNurse)
    EnableAI(Characters.MergosWetNurseClone1)
    EnableBossHealthBar(Characters.MergosWetNurseClone2, name=551000, slot=0)
    ReferDamageToEntity(Characters.MergosWetNurse, Characters.MergosWetNurseClone2)
    ReferDamageToEntity(Characters.MergosWetNurseClone1, Characters.MergosWetNurseClone2)
    CreatePlayLog(88)
    StartPlayLogMeasurement(2600010, 104, overwrite=True)


def ControlMergosWetNurseMusic():
    """ 12604803: Event 12604803 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MergosWetNurseDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2603802)
    DisableSoundEvent(2603803)
    IfFlagDisabled(1, Flags.MergosWetNurseDead)
    IfFlagEnabled(1, Flags.MergosWetNurseBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12604801)
    IfCharacterInsideRegion(1, PLAYER, region=2602801)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2603802)
    EnableFlag(12604815)
    IfHealthLessThan(0, Characters.MergosWetNurseClone2, 0.699999988079071)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.MergosWetNurseDead)
    IfFlagEnabled(2, Flags.MergosWetNurseBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12604801)
    IfCharacterInsideRegion(2, PLAYER, region=2602801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2603802)
    WaitFrames(0)
    EnableBossMusic(2603803)


def ControlMergosWetNurseCamera():
    """ 12604804: Event 12604804 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MergosWetNurseDead)
    IfFlagEnabled(1, Flags.MergosWetNurseFogEntered)
    IfCharacterAlive(1, 2600803)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=NIGHTMARE_OF_MENSIS, camera_slot=1)


def StopMergosWetNurseMusic():
    """ 12604805: Event 12604805 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MergosWetNurseDead)
    IfFlagEnabled(0, 12604808)
    DisableBossMusic(2603802)
    DisableBossMusic(2603803)
    DisableBossMusic(-1)


def DisableWetNurseClone():
    """ 12604806: Event 12604806 """
    DisableCharacter(Characters.MergosWetNurseClone1)
    DisableGravity(Characters.MergosWetNurseClone1)
    DisableCharacterCollision(Characters.MergosWetNurseClone1)


def LogPlayerEffect5630():
    """ 12604807: Logs when player does not and does have effect 5630 in Wet Nurse battle. """
    DisableNetworkSync()
    IfFlagEnabled(1, Flags.MergosWetNurseBattleStarted)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 5630)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(122)
    IfFlagEnabled(2, Flags.MergosWetNurseBattleStarted)
    IfCharacterHasSpecialEffect(2, PLAYER, 5630)
    IfConditionTrue(0, input_condition=2)
    CreatePlayLog(156)
    Restart()


def WetNurseReactsToPlayerEffect5630():
    """ 12604810: Event 12604810 """
    IfCharacterHasSpecialEffect(0, PLAYER, 5630)
    AddSpecialEffect(Characters.MergosWetNurse, 5631, affect_npc_part_hp=False)
    AICommand(Characters.MergosWetNurse, command_id=100, slot=0)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 5630)
    AICommand(Characters.MergosWetNurse, command_id=110, slot=0)
    Restart()


def PlayWetNurseAmbientSound():
    """ 12604815: Event 12604815 """
    DisableNetworkSync()
    IfThisEventFlagEnabled(1)
    IfFlagEnabled(2, Flags.MergosWetNurseDead)
    IfHealthLessThanOrEqual(3, Characters.MergosWetNurse, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EndIfFinishedConditionTrue(3)
    PlaySoundEffect(anchor_entity=Characters.MergosWetNurse, sound_type=SoundType.a_Ambient, sound_id=260000003)
    WaitRandomSeconds(min_seconds=5.0, max_seconds=10.0)
    Restart()


def ChooseMergosWetNurseTeleport(_, wet_nurse: int, first_flag: uint, last_flag: uint):
    """ 12604820: Event 12604820 """
    IfCharacterHasTAEEvent(0, wet_nurse, tae_event_id=10)
    EnableRandomFlagInRange((first_flag, last_flag))
    Wait(1.0)
    Restart()


def MergosWetNurseTeleport(_, wet_nurse: int, trigger_flag: int, target_region: int, backup_region: int):
    """ 12604830: Event 12604830 """
    DisableFlag(trigger_flag)
    IfFlagEnabled(0, trigger_flag)
    IfCharacterInsideRegion(1, wet_nurse, region=target_region)
    SkipLinesIfConditionTrue(3, 1)
    DisableCharacter(wet_nurse)
    Move(wet_nurse, destination=target_region, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SkipLines(2)
    DisableCharacter(wet_nurse)
    Move(wet_nurse, destination=backup_region, destination_type=CoordEntityType.Region, set_draw_parent=0)
    Wait(2.0)
    EnableCharacter(wet_nurse)
    RequestAnimation(wet_nurse, 7000, loop=False, wait_for_completion=True)
    Restart()


def MergosWetNurseNightmareMode():
    """ 12604840: Event 12604840 """
    IfFlagEnabled(1, 12604803)
    IfCharacterHasTAEEvent(1, Characters.MergosWetNurse, tae_event_id=20)
    IfCharacterHasSpecialEffect(1, Characters.MergosWetNurse, 5631)
    IfConditionTrue(0, input_condition=1)
    MoveObjectToCharacter(2601857, character=PLAYER, model_point=245)
    WaitFrames(1)
    EnableCharacter(Characters.MergosWetNurseClone1)
    ResetAnimation(Characters.MergosWetNurseClone1, disable_interpolation=False)
    DisableFlagRange((12604841, 12604844))
    EnableRandomFlagInRange((12604841, 12604844))
    GotoIfFlagEnabled(Label.L0, 12604841)
    GotoIfFlagEnabled(Label.L1, 12604842)
    GotoIfFlagEnabled(Label.L2, 12604843)
    GotoIfFlagEnabled(Label.L3, 12604844)

    # --- 0 --- #
    DefineLabel(0)
    Move(Characters.MergosWetNurseClone1, destination=2601857, destination_type=CoordEntityType.Object,
         model_point=4, short_move=True)
    Goto(Label.L4)

    # --- 1 --- #
    DefineLabel(1)
    Move(Characters.MergosWetNurseClone1, destination=2601857, destination_type=CoordEntityType.Object,
         model_point=104, short_move=True)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    Move(Characters.MergosWetNurseClone1, destination=2601857, destination_type=CoordEntityType.Object,
         model_point=10, short_move=True)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    Move(Characters.MergosWetNurseClone1, destination=2601857, destination_type=CoordEntityType.Object,
         model_point=110, short_move=True)

    # --- 4 --- #
    DefineLabel(4)
    WaitFrames(1)
    CreateTemporaryVFX(
        655105, anchor_entity=Characters.MergosWetNurseClone1, anchor_type=CoordEntityType.Character, model_point=220)
    ReplanAI(Characters.MergosWetNurseClone1)
    AICommand(Characters.MergosWetNurseClone1, command_id=100, slot=0)
    AddSpecialEffect(Characters.MergosWetNurseClone1, 5631, affect_npc_part_hp=False)
    IfCharacterHasTAEEvent(-1, Characters.MergosWetNurseClone1, tae_event_id=20)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.MergosWetNurseClone1, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    CreateTemporaryVFX(
        655105, anchor_entity=Characters.MergosWetNurseClone1, anchor_type=CoordEntityType.Character, model_point=220)
    WaitFrames(10)
    DisableCharacter(Characters.MergosWetNurseClone1)
    Restart()


def MicolashDies():
    """ 12601850: Event 12601850 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(Music.MicolashPhase1)
    DisableSoundEvent(Music.MicolashPhase2)
    DisableCharacter(Characters.Micolash)
    Kill(Characters.Micolash, award_souls=False)
    DisableObject(Objects.MicolashFog1)
    DisableObject(Objects.MicolashFog2)
    DisableObject(Objects.MicolashFog3)
    DeleteVFX(VFX.MicolashFog1, erase_root_only=False)
    DeleteVFX(VFX.MicolashFog2, erase_root_only=False)
    DeleteVFX(VFX.MicolashFog3, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthEqual(0, Characters.Micolash, 0.0)
    EnableFlag(Flags.RequestStopMicolashMusic)
    IfCharacterDead(0, Characters.Micolash)
    EnableFlag(Flags.DismissMicolashPuppets)
    IfFlagEnabled(0, 72600301)  # Wait for Micolash's dying "I'll forget everything" lament to finish.
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.MicolashFog1)
    DisableObject(Objects.MicolashFog2)
    DisableObject(Objects.MicolashFog3)
    DeleteVFX(VFX.MicolashFog1, erase_root_only=True)
    DeleteVFX(VFX.MicolashFog2, erase_root_only=True)
    DeleteVFX(VFX.MicolashFog3, erase_root_only=True)
    SetBackreadStateAlternate(Characters.Micolash, state=False)
    SetNetworkUpdateRate(Characters.Micolash, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Wait(3.0)
    KillBoss(Characters.Micolash)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    AwardAchievement(Achievements.MicolashDefeated)
    AwardItemLot(21000, host_only=False)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(2,))
    EnableFlag(2600)
    EnableFlag(9461)
    DisableFlagRange((1080, 1099))
    EnableFlag(1082)
    CreatePlayLog(40)
    StopPlayLogMeasurement(2601000)
    StopPlayLogMeasurement(2601001)
    StopPlayLogMeasurement(2601010)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 190, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 190, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 190, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 190, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayMicolashDeathSound():
    """ 12601851: Event 12601851 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagEnabled(1, Flags.MergosWetNurseDead)
    IfCharacterBackreadDisabled(2, Characters.Micolash)
    IfHealthLessThanOrEqual(2, Characters.Micolash, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2602850, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def MicolashFirstTime():
    """ 12601852: Event 12601852 """
    EndIfFlagEnabled(Flags.MicolashDead)
    EndIfThisEventFlagEnabled()
    DisableCharacter(Characters.Micolash)
    IfFlagDisabled(1, Flags.MicolashDead)
    IfThisEventSlotFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Characters.Micolash, radius=32.0)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12604731)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    GotoIfMultiplayer(Label.L0)
    PlayCutscene(Cutscenes.MicolashIntro, skippable=True, fade_out=False, player_id=PLAYER)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(Cutscenes.MicolashIntro, skippable=False, fade_out=False, player_id=PLAYER)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    EnableFlag(Flags.MicolashFogEntered)
    EnableCharacter(Characters.Micolash)
    EnableObject(Objects.MicolashFog1)
    CreateVFX(VFX.MicolashFog1)
    EnableObject(Objects.MicolashFog3)
    CreateVFX(VFX.MicolashFog3)
    EndIfFlagEnabled(9342)
    RunEvent(9350, 0, args=(2,))
    EnableFlag(9342)


def OpenMicolashTrapGate():
    """ 12601853: Event 12601853 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(Objects.MicolashTrapGate, 2)
    DisableObjectActivation(2601251, obj_act_id=2600000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(2601251, obj_act_id=2600000)
    IfFlagEnabled(0, Flags.MicolashDead)
    EndIfFlagDisabled(Flags.MicolashTrapGateShut)
    EnableObjectActivation(2601251, obj_act_id=2600000)
    IfObjectActivated(0, obj_act_id=12601261)
    ForceAnimation(Objects.MicolashTrapGate, 1)


def TriggerMicolashBridgeCutscene():
    """ 12601854: Event 12601854 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(Objects.MicolashBridge, 1)
    EndOfAnimation(Objects.MicolashTrapGate, 1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfClient()
    IfFlagEnabled(1, Flags.MicolashDead)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=2602853)
    IfCharacterInsideRegion(-1, PLAYER, region=2602854)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Wait(3.0)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    GotoIfFlagDisabled(Label.L1, Flags.MicolashTrapGateShut)
    PlayCutscene(Cutscenes.MicolashBridgeCutscene, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EndOfAnimation(Objects.MicolashBridge, 1)
    ForceAnimation(Objects.MicolashTrapGate, 2)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    PlayCutscene(26000005, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    EndOfAnimation(Objects.MicolashBridge, 1)

    # --- 2 --- #
    DefineLabel(2)
    DisableFlag(CommonFlags.CutsceneActive)


def SummonStartMicolashBattle():
    """ 12601855: Event 12601855 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.MicolashFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(Flags.MicolashFogEntered)
    EnableCharacter(Characters.Micolash)
    EnableObject(Objects.MicolashFog1)
    CreateVFX(VFX.MicolashFog1)
    EnableObject(Objects.MicolashFog3)
    CreateVFX(VFX.MicolashFog3)
    EnableFlag(Flags.MicolashFogEntered)
    EnableFlag(Flags.MicolashFirstTimeDone)


def EnterMicolashFog():
    """ 12604860: Event 12604860 """
    EndIfFlagEnabled(Flags.MicolashDead)
    GotoIfFlagEnabled(Label.L0, Flags.MicolashFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.MicolashFog1)
    DeleteVFX(VFX.MicolashFog1, erase_root_only=False)
    DisableObject(Objects.MicolashFog3)
    DeleteVFX(VFX.MicolashFog3, erase_root_only=False)
    IfFlagDisabled(1, Flags.MicolashDead)
    IfFlagEnabled(1, Flags.MicolashFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.MicolashFog1)
    CreateVFX(VFX.MicolashFog1)
    EnableObject(Objects.MicolashFog3)
    CreateVFX(VFX.MicolashFog3)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.MicolashDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2600850, entity=Objects.MicolashFog1)
    IfFlagEnabled(3, Flags.MicolashDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2602850, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2602851)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.MicolashFogEntered)
    Restart()


def EnterMicolashFogAsSummon():
    """ 12604861: Event 12604861 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagDisabled(1, Flags.MicolashDead)
    IfFlagEnabled(1, Flags.MicolashFirstTimeDone)
    IfFlagEnabled(1, Flags.MicolashFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2600850, entity=Objects.MicolashFog1)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2602850, animation=101130, wait_for_completion=True)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2602851)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12604851)
    Restart()


def Event12604862():
    """ 12604862: Event 12604862 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.MicolashFog1, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12604863():
    """ 12604863: Event 12604863 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.MicolashFog1, radius=4.0)
    IfEntityWithinDistance(1, PLAYER, Objects.MicolashFog1, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def StartMicolashBattle():
    """ 12604852: Event 12604852 """
    EndIfFlagEnabled(Flags.MicolashDead)
    DisableAI(Characters.Micolash)
    DisableHealthBar(Characters.Micolash)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.MicolashFogEntered)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 12604731)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.Micolash, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12604731)
    EnableFlag(Flags.MicolashFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.Micolash, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Micolash)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.Micolash, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Micolash)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    SetBackreadStateAlternate(Characters.Micolash, state=True)
    SetNetworkUpdateRate(Characters.Micolash, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(Characters.Micolash)
    EnableBossHealthBar(Characters.Micolash, name=899000, slot=0)
    SetDistanceLimitForConversationStateChanges(Characters.Micolash, distance=100.0)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    CreatePlayLog(88)
    StartPlayLogMeasurement(2601010, 232, overwrite=True)


def ControlMicolashMusic():
    """ 12604853: Event 12604853 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MicolashDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(Music.MicolashPhase1)
    DisableSoundEvent(Music.MicolashPhase2)
    IfFlagDisabled(1, Flags.MicolashDead)
    IfFlagEnabled(1, Flags.MicolashBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12604851)
    IfCharacterInsideRegion(1, PLAYER, region=2602852)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(Music.MicolashPhase1)
    IfFlagEnabled(0, 72600300)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.MicolashDead)
    IfFlagEnabled(2, Flags.MicolashBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12604851)
    IfCharacterInsideRegion(2, PLAYER, region=2602852)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(Music.MicolashPhase1)
    WaitFrames(0)
    EnableBossMusic(Music.MicolashPhase2)


def ControlMicolashCamera():
    """ 12604854: Event 12604854 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagEnabled(1, Flags.MicolashFogEntered)
    IfCharacterDead(1, Characters.Micolash)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=NIGHTMARE_OF_MENSIS, camera_slot=1)


def StopMicolashMusic():
    """ 12604855: Event 12604855 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagEnabled(0, Flags.RequestStopMicolashMusic)
    DisableBossMusic(Music.MicolashPhase1)
    DisableBossMusic(Music.MicolashPhase2)
    DisableBossMusic(-1)


def MicolashPhaseTwoTrigger():
    """ 12604856: Event 12604856 """
    EndIfFlagEnabled(Flags.MicolashDead)
    EnableImmortality(Characters.Micolash)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfHealthLessThanOrEqual(0, Characters.Micolash, 0.5)
    DisableBossHealthBar(Characters.Micolash, name=899000, slot=0)
    EnableFlag(12604985)
    IfFlagEnabled(0, 12604986)
    EnableBossHealthBar(Characters.Micolash, name=899000, slot=0)
    Move(Characters.Micolash, destination=2602062, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    ResetAnimation(Characters.Micolash, disable_interpolation=True)

    # --- 0 --- #
    DefineLabel(0)
    DisableImmortality(Characters.Micolash)
    SetNest(Characters.Micolash, 2602062)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(12604952)
    ReplanAI(Characters.Micolash)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableObject(Objects.MicolashFog2)
    DeleteVFX(VFX.MicolashFog2, erase_root_only=True)


def Event12604985():
    """ 12604985: Event 12604985 """
    EndIfFlagEnabled(Flags.MicolashDead)
    EndIfFlagEnabled(Flags.MicolashPhaseTwo)
    IfFlagEnabled(1, 12604986)
    IfThisEventFlagEnabled(2)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    EzstateAIRequest(Characters.Micolash, command_id=12, slot=1)
    WaitFrames(10)
    Restart()


def Event12604986():
    """ 12604986: Event 12604986 """
    EndIfFlagEnabled(Flags.MicolashDead)
    EndIfThisEventFlagEnabled()
    IfCharacterHasTAEEvent(0, Characters.Micolash, tae_event_id=50)
    StopEvent(12604985)
    Wait(6.0)
    End()


def MicolashRunsAwayPhase1(
    _,
    trigger_region: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12604870: Event 12604870 """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagDisabled(1, 12604946)
    IfCharacterInsideRegion(1, Characters.Micolash, region=trigger_region)
    IfEntityWithinDistance(1, PLAYER, Characters.Micolash, radius=9.0)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(4, input_condition=1)
    IfConditionTrue(5, input_condition=1)
    IfCharacterInsideRegion(2, PLAYER, region=2602050)
    IfCharacterInsideRegion(3, PLAYER, region=2602051)
    IfCharacterInsideRegion(4, PLAYER, region=2602052)
    IfEntityWithinDistance(5, PLAYER, Characters.Micolash, radius=3.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterInsideRegion(7, Characters.Micolash, region=2602043)
    GotoIfConditionTrue(Label.L7, input_condition=7)
    DisableFlagRange((12604870, 12604873))
    EnableRandomFlagInRange((12604870, 12604873))
    GotoIfFlagEnabled(Label.L8, 12604870)

    # --- 7 --- #
    DefineLabel(7)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=5)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterOutsideRegion(6, Characters.Micolash, region=2602042)
    GotoIfConditionTrue(Label.L6, input_condition=6)
    DisableFlagRange((12604870, 12604871))
    EnableRandomFlagInRange((12604870, 12604871))
    GotoIfFlagEnabled(Label.L4, 12604870)

    # --- 6 --- #
    DefineLabel(6)
    SetNest(Characters.Micolash, arg_4_7)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(arg_20_23)
    Wait(2.0)
    Restart()

    # --- 4 --- #
    DefineLabel(4)
    SetNest(Characters.Micolash, arg_16_19)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(arg_24_27)
    Wait(2.0)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    SetNest(Characters.Micolash, arg_8_11)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(arg_24_27)
    Wait(2.0)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    SetNest(Characters.Micolash, arg_12_15)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(arg_28_31)
    Wait(2.0)
    Restart()

    # --- 3 --- #
    DefineLabel(3)
    DisableFlagRange((12604870, 12604871))
    EnableRandomFlagInRange((12604870, 12604871))
    GotoIfFlagEnabled(Label.L5, 12604870)
    SetNest(Characters.Micolash, arg_8_11)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(arg_24_27)
    Wait(2.0)
    Restart()

    # --- 5 --- #
    DefineLabel(5)
    SetNest(Characters.Micolash, arg_12_15)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(arg_28_31)
    Wait(2.0)
    Restart()

    # --- 8 --- #
    DefineLabel(8)
    SetNest(Characters.Micolash, 2602043)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(12604943)
    Wait(2.0)
    Restart()


def Event12604877():
    """ 12604877: Event 12604877 """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagDisabled(1, Flags.MicolashPhaseTwo)
    IfHealthLessThan(1, Characters.Micolash, 0.699999988079071)
    IfFlagDisabled(1, 12604946)
    IfFlagDisabled(2, Flags.MicolashPhaseTwo)
    IfCharacterInsideRegion(2, Characters.Micolash, region=2602046)
    IfFlagEnabled(2, 12604946)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    SetNest(Characters.Micolash, 2602046)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604940, 12604946))
    EnableFlag(12604946)
    IfCharacterInsideRegion(0, Characters.Micolash, region=2602046)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(Characters.Micolash, command_id=-1, slot=0)


def MicolashMirrorTeleport():
    """ 12604878: Event 12604878 """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, Characters.Micolash, region=2602064)
    IfCharacterHuman(2, PLAYER)
    IfCharacterInsideRegion(2, Characters.Micolash, region=2602069)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisableCharacterCollision(Characters.Micolash)
    DisableGravity(Characters.Micolash)
    EnableInvincibility(Characters.Micolash)
    SkipLinesIfFinishedConditionTrue(1, 1)
    SkipLinesIfFinishedConditionTrue(3, 2)
    CreateTemporaryVFX(926201, anchor_entity=2601853, anchor_type=CoordEntityType.Object, model_point=800)
    ForceAnimation(Characters.Micolash, 103122, wait_for_completion=True)
    SkipLines(2)
    CreateTemporaryVFX(926201, anchor_entity=2601854, anchor_type=CoordEntityType.Object, model_point=800)
    ForceAnimation(Characters.Micolash, 103122, wait_for_completion=True)
    Move(Characters.Micolash, destination=2602073, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    SetNest(Characters.Micolash, 2602065)
    WaitFrames(5)
    CreateTemporaryVFX(926201, anchor_entity=2601855, anchor_type=CoordEntityType.Object, model_point=800)
    ForceAnimation(Characters.Micolash, 103120)
    EnableCharacterCollision(Characters.Micolash)
    EnableGravity(Characters.Micolash)
    DisableInvincibility(Characters.Micolash)
    Restart()


def PointlessMicolashEvent():
    """ 12604956: Only ends when its own flag is enabled, which never seems to happen anywhere in EMEVD. """
    IfThisEventFlagEnabled(0)
    End()


def ShutMicolashTrapGate():
    """ 12604879: Event 12604879 """
    GotoIfFlagEnabled(Label.L0, Flags.MicolashDead)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, Characters.Micolash, region=Regions.MicolashFinalRoom)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(Flags.MicolashTrapGateShut)
    ForceAnimation(Objects.MicolashTrapGate, 3)
    Wait(1.0)
    AICommand(Characters.Micolash, command_id=-1, slot=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=0)
    Wait(0.0)


def MicolashRunsAwayPhase2(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12604880: Event 12604880 """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagDisabled(1, 12604956)
    IfCharacterInsideRegion(1, Characters.Micolash, region=arg_0_3)
    IfEntityWithinDistance(1, PLAYER, Characters.Micolash, radius=9.0)
    IfFlagDisabled(6, 12604956)
    IfCharacterInsideRegion(6, Characters.Micolash, region=arg_0_3)
    IfCharacterInsideRegion(6, Characters.Micolash, region=2602063)
    IfAttackedWithDamageType(6, attacked_entity=Characters.Micolash, attacker=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(4, input_condition=-2)
    IfConditionTrue(5, input_condition=-2)
    IfCharacterInsideRegion(2, PLAYER, region=arg_28_31)
    IfCharacterInsideRegion(3, PLAYER, region=2602071)
    IfCharacterInsideRegion(4, PLAYER, region=2602072)
    IfEntityWithinDistance(5, PLAYER, Characters.Micolash, radius=3.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterInsideRegion(-3, Characters.Micolash, region=2602059)
    IfCharacterInsideRegion(-3, Characters.Micolash, region=2602063)
    IfCharacterInsideRegion(-3, Characters.Micolash, region=2602068)
    IfCharacterInsideRegion(-3, Characters.Micolash, region=2602065)
    GotoIfConditionTrue(Label.L9, input_condition=-3)
    DisableFlagRange((12604865, 12604868))
    EnableRandomFlagInRange((12604865, 12604868))
    GotoIfFlagEnabled(Label.L5, 12604865)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L3, input_condition=5)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(Characters.Micolash, arg_4_7)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(arg_16_19)
    Wait(2.0)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    SetNest(Characters.Micolash, arg_8_11)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(arg_20_23)
    Wait(2.0)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    SetNest(Characters.Micolash, arg_12_15)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(arg_24_27)
    Wait(2.0)
    Restart()

    # --- 3 --- #
    DefineLabel(3)
    DisableFlagRange((12604880, 12604881))
    EnableRandomFlagInRange((12604880, 12604881))
    GotoIfFlagEnabled(Label.L4, 12604880)
    SetNest(Characters.Micolash, arg_8_11)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(arg_20_23)
    Wait(2.0)
    Restart()

    # --- 4 --- #
    DefineLabel(4)
    SetNest(Characters.Micolash, arg_12_15)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(arg_24_27)
    Wait(2.0)
    Restart()

    # --- 5 --- #
    DefineLabel(5)
    SetNest(Characters.Micolash, 2602059)
    AICommand(Characters.Micolash, command_id=10, slot=0)
    DisableFlagRange((12604949, 12604959))
    EnableFlag(12604949)
    Wait(2.0)
    Restart()


def Event12604888():
    """ 12604888: Event 12604888 """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfCharacterHuman(1, PLAYER)
    IfAttackedWithDamageType(1, attacked_entity=Characters.Micolash, attacker=-1)
    IfFlagDisabled(1, 12604946)
    IfFlagDisabled(1, Flags.MicolashPhaseTwo)
    IfHealthGreaterThan(1, Characters.Micolash, 0.5)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(15)
    RestartIfFlagEnabled(12604946)
    ForceAnimation(Characters.Micolash, 103120)
    CreateTemporaryVFX(926210, anchor_entity=Characters.Micolash, anchor_type=CoordEntityType.Character, model_point=200)
    GotoIfFlagEnabled(Label.L0, 12604940)
    GotoIfFlagEnabled(Label.L1, 12604941)
    GotoIfFlagEnabled(Label.L2, 12604942)
    GotoIfFlagEnabled(Label.L3, 12604943)
    GotoIfFlagEnabled(Label.L4, 12604944)
    GotoIfFlagEnabled(Label.L5, 12604945)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Move(Characters.Micolash, destination=2602040, destination_type=CoordEntityType.Region, set_draw_parent=2604800)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    Move(Characters.Micolash, destination=2602041, destination_type=CoordEntityType.Region, set_draw_parent=2604800)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    Move(Characters.Micolash, destination=2602042, destination_type=CoordEntityType.Region, set_draw_parent=2604801)
    Restart()

    # --- 3 --- #
    DefineLabel(3)
    Move(Characters.Micolash, destination=2602043, destination_type=CoordEntityType.Region, set_draw_parent=2604801)
    Restart()

    # --- 4 --- #
    DefineLabel(4)
    Move(Characters.Micolash, destination=2602044, destination_type=CoordEntityType.Region, set_draw_parent=2604802)
    Restart()

    # --- 5 --- #
    DefineLabel(5)
    Move(Characters.Micolash, destination=2602045, destination_type=CoordEntityType.Region, set_draw_parent=2604802)
    Restart()


def MicolashDisappearsWhenHitInPhase2():
    """ 12604889: Event 12604889 """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfCharacterHuman(1, PLAYER)
    IfAttackedWithDamageType(1, attacked_entity=Characters.Micolash, attacker=-1)
    IfFlagDisabled(1, 12604956)
    IfFlagEnabled(1, Flags.MicolashPhaseTwo)
    IfHealthGreaterThan(1, Characters.Micolash, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterInsideRegion(2, Characters.Micolash, region=2602063)
    RestartIfConditionTrue(2)
    WaitFrames(15)
    ForceAnimation(Characters.Micolash, 103120)
    CreateTemporaryVFX(926210, anchor_entity=Characters.Micolash, anchor_type=CoordEntityType.Character, model_point=200)
    SkipLinesIfFlagEnabled(10, 12604949)
    SkipLinesIfFlagEnabled(11, 12604950)
    SkipLinesIfFlagEnabled(12, 12604951)
    SkipLinesIfFlagEnabled(13, 12604952)
    SkipLinesIfFlagEnabled(14, 12604953)
    SkipLinesIfFlagEnabled(15, 12604954)
    SkipLinesIfFlagEnabled(16, 12604955)
    SkipLinesIfFlagEnabled(17, 12604956)
    SkipLinesIfFlagEnabled(18, 12604957)
    SkipLinesIfFlagEnabled(19, 12604958)
    SkipLinesIfFlagEnabled(20, 12604959)
    Move(Characters.Micolash, destination=2602059, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    Restart()
    Move(Characters.Micolash, destination=2602060, destination_type=CoordEntityType.Region, set_draw_parent=2604812)
    Restart()
    Move(Characters.Micolash, destination=2602061, destination_type=CoordEntityType.Region, set_draw_parent=2604812)
    Restart()
    Move(Characters.Micolash, destination=2602062, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    Restart()
    Move(Characters.Micolash, destination=2602063, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    Restart()
    Move(Characters.Micolash, destination=2602077, destination_type=CoordEntityType.Region, set_draw_parent=2604810)
    Restart()
    Move(Characters.Micolash, destination=2602065, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    Restart()
    Move(Characters.Micolash, destination=Regions.MicolashFinalRoom, set_draw_parent=2604813)
    Restart()
    Move(Characters.Micolash, destination=2602067, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    Restart()
    Move(Characters.Micolash, destination=2602068, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    Restart()
    Move(Characters.Micolash, destination=2602078, destination_type=CoordEntityType.Region, set_draw_parent=2604811)
    Restart()


def KillMicolashPuppet(_, puppet_chr: int, disable_flag: int, dismiss_flag: int):
    """ 12604890: Event 12604890 """
    GotoIfFlagDisabled(Label.L0, disable_flag)
    DisableCharacter(puppet_chr)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableImmortality(puppet_chr)
    IfFlagEnabled(0, dismiss_flag)
    AddSpecialEffect(puppet_chr, 5914, affect_npc_part_hp=False)
    ForceAnimation(puppet_chr, 7002)


def AnimateMicolashPuppet(_, arg_0_3: int, arg_4_7: int):
    """ 12604910: Event 12604910 """
    EndIfFlagEnabled(arg_4_7)
    EndIfThisEventSlotFlagEnabled()
    DisableGravity(arg_0_3)
    ForceAnimation(arg_0_3, 7000, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=7.0)
    IfFlagEnabled(2, arg_4_7)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    CancelSpecialEffect(arg_0_3, 5914)
    EnableGravity(arg_0_3)
    ForceAnimation(arg_0_3, 7001)


def MicolashWaitsInFinalRoom():
    """ 12604930: Event 12604930 """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagEnabled(0, Flags.MicolashTrapGateShut)
    DisableAI(Characters.Micolash)
    IfCharacterInsideRegion(-1, PLAYER, region=2602007)
    IfAttackedWithDamageType(-1, attacked_entity=Characters.Micolash, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(Characters.Micolash)


def AggravateMicolashEarly(_, required_flag: int, ignore_flag: int):
    """ 12604931: Aggravate Micolash after three consecutive hits if `required_flag` is on and `ignore_flag` is off. """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagEnabled(1, required_flag)
    IfAttackedWithDamageType(1, attacked_entity=Characters.Micolash, attacker=-1)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    IfFlagEnabled(2, required_flag)
    IfAttackedWithDamageType(2, attacked_entity=Characters.Micolash, attacker=-1)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(1)
    IfFlagEnabled(3, required_flag)
    IfAttackedWithDamageType(3, attacked_entity=Characters.Micolash, attacker=-1)
    IfConditionTrue(0, input_condition=3)
    WaitFrames(1)
    EndIfFlagEnabled(ignore_flag)
    AICommand(Characters.Micolash, command_id=-1, slot=0)
    ReplanAI(Characters.Micolash)


def PlayMicolashDialoguePhase1(_, trigger_region: int):
    """ 12604960: Event 12604960 """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagEnabled(3, Flags.MicolashBattleStarted)
    IfFlagDisabled(3, 72600300)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(72600302)
    IfCharacterInsideRegion(1, Characters.Micolash, region=trigger_region)
    IfFlagDisabled(1, 72600302)
    IfConditionTrue(0, input_condition=1)
    IfTimeElapsed(0, 20.0)
    IfCharacterInsideRegion(2, Characters.Micolash, region=trigger_region)
    IfEntityBeyondDistance(2, Characters.Micolash, PLAYER, radius=15.0)
    RestartIfConditionFalse(2)
    EnableFlag(72600302)
    EnableRandomFlagInRange((72600303, 72600305))
    IfFlagDisabled(0, 72600302)
    DisableFlagRange((72600303, 72600305))
    Restart()


def PlayMicolashDialoguePhase2(_, trigger_region: int):
    """ 12604970: Event 12604970 """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagEnabled(3, Flags.MicolashBattleStarted)
    IfFlagEnabled(3, 72600300)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(72600302)
    IfCharacterInsideRegion(1, Characters.Micolash, region=trigger_region)
    IfFlagDisabled(1, 72600302)
    IfConditionTrue(0, input_condition=1)
    IfTimeElapsed(0, 20.0)
    IfCharacterInsideRegion(2, Characters.Micolash, region=trigger_region)
    IfEntityBeyondDistance(2, Characters.Micolash, PLAYER, radius=15.0)
    RestartIfConditionFalse(2)
    EnableFlag(72600302)
    GotoIfFlagDisabled(Label.L0, Flags.MicolashTrapGateShut)
    EnableFlag(72600317)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    EnableRandomFlagInRange((72600303, 72600305))

    # --- 1 --- #
    DefineLabel(1)
    IfFlagDisabled(0, 72600302)
    DisableFlagRange((72600303, 72600305))
    DisableFlag(72600317)
    Restart()


def PlayRandomMicolashTAEDialogue(
    _,
    tae_event: int,
    first_flag: int,
    last_flag: int,
    first_random_flag: uint,
    last_random_flag: uint,
    required_flag: int,
    dialogue_request_flag: int,
):
    """ 12604980: Rolls a dice to enable a certain `dialogue_request_flag` when the given Micolash `tae_event`
    occurs. In usage, the odds of the flag being enabled are 20%.
    """
    EndIfFlagEnabled(Flags.MicolashDead)
    IfFlagEnabled(0, Flags.MicolashBattleStarted)
    DisableFlagRange((first_flag, last_flag))
    IfCharacterHasTAEEvent(1, Characters.Micolash, tae_event_id=tae_event)
    IfFlagDisabled(1, dialogue_request_flag)
    IfConditionTrue(0, input_condition=1)
    EnableRandomFlagInRange((first_random_flag, last_random_flag))
    RestartIfFlagDisabled(required_flag)
    EnableFlag(dialogue_request_flag)
    IfFlagDisabled(0, dialogue_request_flag)
    Restart()


@RestartOnRest
def Event12604000(_, arg_0_3: int, arg_4_4: uchar, arg_8_11: float):
    """ 12604000: Event 12604000 """
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(arg_0_3)
    IfPlayerInsightAmountGreaterThanOrEqual(1, arg_4_4)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 6200, wait_for_completion=True)


@RestartOnRest
def Event12604005(_, arg_0_3: int, arg_4_4: uchar, arg_8_11: int):
    """ 12604005: Event 12604005 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(1, arg_8_11)
    IfPlayerInsightAmountLessThanOrEqual(1, arg_4_4)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    Kill(arg_0_3, award_souls=False)


@RestartOnRest
def Event12600500(_, arg_0_3: int):
    """ 12600500: Event 12600500 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DropMandatoryTreasure(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    End()


@RestartOnRest
def Event12600020(_, arg_0_3: int, arg_4_7: int):
    """ 12600020: Event 12600020 """
    DisableGravity(arg_0_3)
    DisableGravity(arg_4_7)
    EnableInvincibility(arg_0_3)
    EnableInvincibility(arg_4_7)
    SetBackreadStateAlternate(arg_0_3, state=True)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(arg_0_3, UpdateAuthority.Forced)
    DisableAnimations(arg_0_3)
    DeleteVFX(2603000, erase_root_only=False)


@RestartOnRest
def Event12600021():
    """ 12600021: Event 12600021 """
    IfCharacterInsideRegion(0, PLAYER, region=2602017)
    Move(2600100, destination=2602019, destination_type=CoordEntityType.Region, short_move=True)
    IfAllPlayersOutsideRegion(0, region=2602017)
    Move(2600100, destination=2602018, destination_type=CoordEntityType.Region, short_move=True)
    Restart()


def Event12600130(_, arg_0_3: int):
    """ 12600130: Event 12600130 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(10, arg_0_3, 4691)
    GotoIfConditionTrue(Label.L0, input_condition=10)
    IfCharacterHasSpecialEffect(0, arg_0_3, 4690)
    Wait(2.0)
    IfCharacterHasSpecialEffect(1, arg_0_3, 4690)
    IfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, 4690)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFinishedConditionTrue(2)

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect_WithUnknownEffect(arg_0_3, 4691, affect_npc_parts_hp=False)
    Restart()


def Event12600150(_, arg_0_3: int):
    """ 12600150: Event 12600150 """
    DisableNetworkSync()
    IfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, 4690)
    IfCharacterHasSpecialEffect(1, arg_0_3, 4691)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(arg_0_3, 4691)
    Restart()


def Event12600025():
    """ 12600025: Event 12600025 """
    IfCharacterHuman(1, PLAYER)
    IfHasAIStatus(-1, 2600100, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2600100, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, 2600100, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    CreateVFX(2603000)
    IfCharacterHuman(2, PLAYER)
    IfHasAIStatus(2, 2600100, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=2)
    DeleteVFX(2603000, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12600026():
    """ 12600026: Event 12600026 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfActionButtonParamActivated(0, action_button_id=7100, entity=2601271)
    DeleteVFX(2603050, erase_root_only=False)
    DeleteVFX(2603051, erase_root_only=False)
    DeleteVFX(2603052, erase_root_only=False)
    DeleteVFX(2603053, erase_root_only=False)
    DeleteVFX(2603054, erase_root_only=False)
    DeleteVFX(2603055, erase_root_only=False)
    DeleteVFX(2603056, erase_root_only=False)
    DeleteVFX(2603057, erase_root_only=False)
    DeleteVFX(2603058, erase_root_only=False)
    DeleteVFX(2603059, erase_root_only=False)
    DeleteVFX(2603060, erase_root_only=False)
    DeleteVFX(2603061, erase_root_only=False)
    DeleteVFX(2603062, erase_root_only=False)
    DeleteVFX(2603063, erase_root_only=False)
    DeleteVFX(2603064, erase_root_only=False)
    DeleteVFX(2603065, erase_root_only=False)
    DeleteVFX(2603066, erase_root_only=False)
    DeleteVFX(2603067, erase_root_only=False)
    DeleteVFX(2603068, erase_root_only=False)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(26000040, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(26000040, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    CreateVFX(2603050)
    CreateVFX(2603051)
    CreateVFX(2603052)
    CreateVFX(2603053)
    CreateVFX(2603054)
    CreateVFX(2603055)
    CreateVFX(2603056)
    CreateVFX(2603057)
    CreateVFX(2603058)
    CreateVFX(2603059)
    CreateVFX(2603060)
    CreateVFX(2603061)
    CreateVFX(2603062)
    CreateVFX(2603063)
    CreateVFX(2603064)
    CreateVFX(2603065)
    CreateVFX(2603066)
    CreateVFX(2603067)
    CreateVFX(2603068)

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(2601271, obj_act_id=2600000)
    DisableAI(2600100)
    DisableAI(2600101)
    DisableCharacter(2600100)
    DisableCharacter(2600101)
    DeleteVFX(2603000, erase_root_only=True)


@RestartOnRest
def Event12600027():
    """ 12600027: Event 12600027 """
    DisableCharacter(2600129)
    GotoIfThisEventFlagDisabled(Label.L0)
    EnableCharacter(2600129)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 12600026)
    EnableCharacter(2600129)


def Event12600028():
    """ 12600028: Event 12600028 """
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfFlagEnabled(1, 12600027)
    IfCharacterInsideRegion(1, PLAYER, region=2602022)
    IfCharacterHasSpecialEffect(1, PLAYER, 164)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagEnabled(Label.L0, 6336)
    AwardItemLot(2605000, host_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    AwardItemLot(2605005, host_only=False)
    End()


@RestartOnRest
def Event12600029():
    """ 12600029: Event 12600029 """
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfFlagEnabled(1, 12600027)
    IfHealthEqual(1, 2600129, 0.0)
    IfAttackedWithDamageType(1, attacked_entity=2600129, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(2605010, host_only=False)
    EnableFlag(5913)
    WaitFrames(0)


def Event12600010(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12600010: Event 12600010 """
    EndIfFlagEnabled(Flags.MergosWetNurseFirstTimeDone)
    IfHost(1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    GotoIfValueComparison(Label.L0, ComparisonType.Equal, left=arg_8_11, right=1)
    PlaySoundEffect(anchor_entity=2602300, sound_type=SoundType.a_Ambient, sound_id=arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableSoundEvent(arg_4_7)
    End()


def Event12600030():
    """ 12600030: Event 12600030 """
    SetTeamType(2600500, TeamType.FriendlyNPC)
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2600500)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, Flags.MergosWetNurseDead)
    ForceAnimation(2600500, 7005)
    IfFlagEnabled(0, Flags.MergosWetNurseDead)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(2600500, 0)
    IfEntityWithinDistance(1, 2600500, PLAYER, radius=10.0)
    IfHealthGreaterThan(1, 2600500, 0.0)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(2600500)
    ForceAnimation(2600500, 7006)
    Wait(2.0)
    DisableCharacter(2600500)


def Event12600031():
    """ 12600031: Event 12600031 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2600500)
    End()

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect(2600500, 5915, affect_npc_part_hp=False)
    IfAttackedWithDamageType(0, attacked_entity=2600500, attacker=-1)
    Kill(2600500, award_souls=False)


def Event12600035(_, arg_0_3: int):
    """ 12600035: Event 12600035 """
    ForceAnimation(arg_0_3, 7000)
    IfCharacterTargeting(-1, arg_0_3, PLAYER)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(1)
    ForceAnimation(arg_0_3, 7001)


def Event12600040(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12600040: Event 12600040 """
    DisableAI(arg_4_7)
    IfCharacterInsideRegion(-2, arg_12_15, region=arg_0_3)
    IfCharacterInsideRegion(-2, arg_12_15, region=arg_16_19)
    IfConditionTrue(0, input_condition=-2)
    EnableAI(arg_4_7)
    SetNest(arg_4_7, arg_8_11)
    AICommand(arg_4_7, command_id=20, slot=0)
    IfAttackedWithDamageType(-1, attacked_entity=arg_4_7, attacker=PLAYER)
    IfHealthLessThan(-1, arg_4_7, 1.0)
    IfCharacterInsideRegion(-1, arg_4_7, region=arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)


def Event12600041(_, arg_0_3: int):
    """ 12600041: Event 12600041 """
    AddSpecialEffect(arg_0_3, 5641, affect_npc_part_hp=False)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    CancelSpecialEffect(arg_0_3, 5641)
    ReplanAI(arg_0_3)


def Event12600047(_, arg_0_3: int):
    """ 12600047: Event 12600047 """
    AICommand(arg_0_3, command_id=40, slot=0)
    IfHasAIStatus(0, 2600202, ai_status=AIStatusType.Battle)
    ReplanAI(arg_0_3)
    AICommand(arg_0_3, command_id=10, slot=0)
    SetNest(arg_0_3, 2602005)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)
    ReplanAI(arg_0_3)
    AICommand(arg_0_3, command_id=-1, slot=0)


def Event12600180(_, arg_0_3: int, arg_4_7: int):
    """ 12600180: Event 12600180 """
    DisableNetworkSync()
    EndIfClient()
    AddSpecialEffect(arg_0_3, 5001, affect_npc_part_hp=False)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    Wait(60.0)
    MoveObjectToCharacter(2601040, character=arg_0_3, model_point=-1)
    CreateObjectVFX(900201, obj=2601040, model_point=200)
    IfActionButtonParamActivated(1, action_button_id=2600030, entity=2601040)
    IfTimeElapsed(2, 15.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DeleteObjectVFX(2601040, erase_root=True)
    RestartIfFinishedConditionTrue(2)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(arg_4_7, host_only=False)
    Restart()


def Event12600050(_, arg_0_3: int, arg_4_7: int):
    """ 12600050: Event 12600050 """
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7000)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomFrames(min_frames=10, max_frames=60)
    ForceAnimation(arg_0_3, 7001)
    EnableAI(arg_0_3)


def Event12600060(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12600060: Event 12600060 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_8_11)


def Event12600070(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12600070: Event 12600070 """
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=arg_8_11)
    SetNest(arg_0_3, arg_4_7)
    AICommand(arg_0_3, command_id=20, slot=0)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


def Event12600080(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12600080: Event 12600080 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((12600080, 12600081))
    EnableRandomFlagInRange((12600080, 12600081))
    SkipLinesIfFlagEnabled(1, 12600080)
    SkipLinesIfFlagEnabled(2, 12600081)
    ForceAnimation(arg_0_3, arg_8_11)
    End()
    ForceAnimation(arg_0_3, arg_12_15)
    End()


def Event12600090(_, arg_0_3: int, arg_4_7: int):
    """ 12600090: Event 12600090 """
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)


def Event12600105(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12600105: Event 12600105 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfHasAIStatus(-1, arg_12_15, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, arg_16_19, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, arg_20_23, ai_status=AIStatusType.Battle)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(5, 1)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=-1)
    IfTimeElapsed(3, 10.0)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(arg_0_3, arg_8_11)


@RestartOnRest
def Event12600110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12600110: Event 12600110 """
    DisableCharacter(arg_4_7)
    DisableCharacter(arg_8_11)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=100)
    WaitFrames(5)
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_4_7)
    ForceAnimation(arg_4_7, 7000)
    WaitFrames(15)
    Move(
        arg_8_11,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=30,
        copy_draw_parent=arg_0_3,
    )
    EnableCharacter(arg_8_11)
    ForceAnimation(arg_8_11, 7000)


@RestartOnRest
def Event12600120(_, arg_0_3: int, arg_4_7: int):
    """ 12600120: Event 12600120 """
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(arg_4_7, 0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1)
    EnableTreasure(arg_4_7)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    WaitFrames(10)
    EnableTreasure(arg_4_7)


@RestartOnRest
def Event12600125(_, arg_0_3: int, arg_4_7: int):
    """ 12600125: Event 12600125 """
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    CreateObjectVFX(900201, obj=arg_0_3, model_point=200)
    IfActionButtonParamActivated(0, action_button_id=2600030, entity=arg_0_3)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(arg_4_7, host_only=False)
    DeleteObjectVFX(arg_0_3, erase_root=True)


@RestartOnRest
def Event12600190(_, arg_0_3: int, arg_4_7: int):
    """ 12600190: Event 12600190 """
    DisableAI(arg_0_3)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=30.0)
    SkipLinesIfEqual(1, left=arg_4_7, right=0)
    IfEntityWithinDistance(-1, arg_4_7, PLAYER, radius=30.0)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12600400(_, arg_0_3: int, arg_4_7: int):
    """ 12600400: Event 12600400 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@RestartOnRest
def Event12600410():
    """ 12600410: Event 12600410 """
    EndIfFlagEnabled(12600403)
    IfHasAIStatus(-1, 2600403, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2600403, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, 2600403, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetNest(2600403, 2602029)
    AICommand(2600403, command_id=10, slot=0)
    IfCharacterInsideRegion(0, 2600403, region=2602029)
    AICommand(2600403, command_id=-1, slot=0)


@RestartOnRest
def Event12600701():
    """ 12600701: Event 12600701 """
    IfFlagEnabled(1, 1080)
    IfFlagEnabled(1, 72600300)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1080, 1099))
    EnableFlag(1081)


@RestartOnRest
def Event12600703():
    """ 12600703: Event 12600703 """
    IfFlagDisabled(0, 1082)
    DisableFlagRange((1080, 1099))
    EnableFlag(1080)
    DisableFlag(72600300)
    DisableFlagRange((72600300, 72600319))


def Event12601294():
    """ 12601294: Event 12601294 """
    WaitFrames(0)


def Event12601295(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar):
    """ 12601295: Event 12601295 """
    DisableNetworkSync()
    IfFlagDisabled(1, arg_4_7)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=arg_0_3)
    IfFlagEnabled(2, arg_8_11)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=arg_0_3)
    IfFlagState(3, state=arg_16_16, flag_type=FlagType.Absolute, flag=arg_12_15)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12601310(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12601310: Event 12601310 """
    SkipLinesIfFlagEnabled(7, arg_0_3)
    EndOfAnimation(arg_4_7, 4)
    Wait(1.0)
    DisableObjectActivation(arg_8_11, obj_act_id=2600000)
    EnableObjectActivation(arg_12_15, obj_act_id=2600000)
    EndIfFlagEnabled(arg_16_19)
    DisableObjectActivation(arg_12_15, obj_act_id=2600000)
    End()
    EndOfAnimation(arg_4_7, 0)
    Wait(1.0)
    EnableObjectActivation(arg_8_11, obj_act_id=2600000)
    DisableObjectActivation(arg_12_15, obj_act_id=2600000)


def Event12601315(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12601315: Event 12601315 """
    SkipLinesIfFlagEnabled(7, arg_0_3)
    EndOfAnimation(arg_4_7, 4)
    Wait(1.0)
    EnableObjectActivation(arg_8_11, obj_act_id=2600000)
    DisableObjectActivation(arg_12_15, obj_act_id=2600000)
    EndIfFlagEnabled(arg_16_19)
    DisableObjectActivation(arg_8_11, obj_act_id=2600000)
    End()
    EndOfAnimation(arg_4_7, 0)
    Wait(1.0)
    DisableObjectActivation(arg_8_11, obj_act_id=2600000)
    EnableObjectActivation(arg_12_15, obj_act_id=2600000)


def Event12601320(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12601320: Event 12601320 """
    IfFlagDisabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfFlagDisabled(2, arg_0_3)
    IfFlagDisabled(2, arg_4_7)
    IfObjectActivated(2, obj_act_id=arg_28_31)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    DisableObjectActivation(arg_20_23, obj_act_id=2600000)
    ForceAnimation(arg_24_27, 5, wait_for_completion=True)
    ForceAnimation(arg_24_27, 6, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_12_15)
    ForceAnimation(arg_24_27, 7, wait_for_completion=True)
    DisableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    EnableObjectActivation(arg_16_19, obj_act_id=2600000)
    Restart()


def Event12601330(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12601330: Event 12601330 """
    IfFlagDisabled(1, arg_0_3)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfFlagDisabled(2, arg_0_3)
    IfFlagEnabled(2, arg_4_7)
    IfObjectActivated(2, obj_act_id=arg_28_31)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_0_3)
    DisableObjectActivation(arg_16_19, obj_act_id=2600000)
    ForceAnimation(arg_24_27, 1, wait_for_completion=True)
    ForceAnimation(arg_24_27, 2, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=arg_8_11)
    ForceAnimation(arg_24_27, 3, wait_for_completion=True)
    DisableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    EnableObjectActivation(arg_20_23, obj_act_id=2600000)
    Restart()


def Event12601340(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12601340: Event 12601340 """
    EndIfFlagEnabled(arg_0_3)
    EnableFlag(arg_4_7)
    Wait(2.0)
    DisableObjectActivation(arg_8_11, obj_act_id=2600000)


def Event12601351(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12601351: Event 12601351 """
    SkipLinesIfFlagEnabled(3, arg_0_3)
    EndOfAnimation(arg_4_7, 0)
    EndOfAnimation(arg_8_11, 1)
    IfFlagEnabled(0, arg_0_3)
    SkipLinesIfFlagDisabled(3, 12601253)
    EndOfAnimation(arg_4_7, 2)
    EndOfAnimation(arg_8_11, 4)
    End()
    EndOfAnimation(arg_4_7, 4)
    EndOfAnimation(arg_8_11, 2)
    End()


def Event12601352():
    """ 12601352: Event 12601352 """
    IfFlagEnabled(0, 12601351)
    GotoIfFlagEnabled(Label.L0, 12601253)
    IfCharacterInsideRegion(-1, PLAYER, region=2602241)
    IfCharacterInsideRegion(-1, PLAYER, region=2602244)
    IfFlagDisabled(1, 12601253)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(2601261, 6)
    ForceAnimation(2601260, 8, wait_for_completion=True)
    ForceAnimation(2601261, 3)
    ForceAnimation(2601260, 5, wait_for_completion=True)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(-2, PLAYER, region=2602242)
    IfCharacterInsideRegion(-2, PLAYER, region=2602243)
    IfFlagEnabled(3, 12601253)
    IfConditionTrue(4, input_condition=-2)
    IfConditionTrue(4, input_condition=3)
    IfConditionTrue(0, input_condition=4)
    ForceAnimation(2601261, 8)
    ForceAnimation(2601260, 6, wait_for_completion=True)
    ForceAnimation(2601261, 5)
    ForceAnimation(2601260, 3, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterOutsideRegion(5, PLAYER, region=2602241)
    IfCharacterOutsideRegion(5, PLAYER, region=2602242)
    IfCharacterOutsideRegion(5, PLAYER, region=2602243)
    IfCharacterOutsideRegion(5, PLAYER, region=2602244)
    IfConditionTrue(0, input_condition=5)
    GotoIfFlagEnabled(Label.L2, 12601253)
    ForceAnimation(2601261, 9)
    ForceAnimation(2601260, 7, wait_for_completion=True)
    EnableFlag(12601253)
    Restart()

    # --- 2 --- #
    DefineLabel(2)
    ForceAnimation(2601261, 7)
    ForceAnimation(2601260, 9, wait_for_completion=True)
    DisableFlag(12601253)
    Restart()


@RestartOnRest
def Event12605200(_, arg_0_3: int, arg_4_7: int):
    """ 12605200: Event 12605200 """
    DisableGravity(arg_4_7)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfCharacterBackreadEnabled(0, arg_0_3)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    SkipLinesIfConditionFalse(2, 1)
    DisableBackread(arg_4_7)
    End()
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=100,
        set_draw_parent=arg_0_3,
    )
    Restart()


def Event12600990():
    """ 12600990: Event 12600990 """
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfPlayerStandingOnCollision(0, 2604000)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 268, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 268, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 268, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 268, PlayLogMultiplayerType.HostOnly)
    RunEvent(9350, 0, args=(3,))


def Event12601050():
    """ 12601050: Event 12601050 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(2601050, 1)
    DisableObjectActivation(2601050, obj_act_id=2600010)
    NotifyDoorEventSoundDampening(2601050, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12600200)
    Wait(0.0)


def Event12601051():
    """ 12601051: Event 12601051 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(2601051, 0)
    DisableObjectActivation(2601051, obj_act_id=2600020)
    DisableObjectActivation(2601051, obj_act_id=2600021)
    NotifyDoorEventSoundDampening(2601051, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(-1, obj_act_id=12600201)
    IfObjectActivated(-1, obj_act_id=12600202)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectActivation(2601051, obj_act_id=2600020)
    DisableObjectActivation(2601051, obj_act_id=2600021)
    Wait(0.0)


def Event12607010(_, arg_0_3: int, arg_4_7: int):
    """ 12607010: Event 12607010 """
    IfFlagEnabled(0, arg_0_3)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    ForceAnimation(PLAYER, 101160, skip_transition=True)
    Wait(4.0)
    DisableFlag(arg_0_3)


def Event12607020(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12607020: Event 12607020 """
    IfFlagEnabled(0, arg_0_3)
    DisableFlag(arg_0_3)
    WarpPlayerToRespawnPoint(arg_4_7)
    EnableFlag(arg_8_11)


def Event12607040():
    """ 12607040: Event 12607040 """
    SkipLinesIfFlagRangeAnyEnabled(1, (9001, 9010))
    End()
    EnableFlag(9210)
    IfFlagDisabled(0, 9210)
    SkipLinesIfFlagDisabled(2, 9001)
    EnableFlag(12607810)
    EnableFlag(12607811)
    SkipLinesIfFlagDisabled(2, 9002)
    EnableFlag(12607830)
    EnableFlag(12607831)
    SkipLinesIfFlagDisabled(2, 9003)
    EnableFlag(12607850)
    EnableFlag(12607851)
    SkipLinesIfFlagDisabled(2, 9004)
    EnableFlag(12607870)
    EnableFlag(12607871)
    SkipLinesIfFlagDisabled(2, 9005)
    EnableFlag(12607890)
    EnableFlag(12607891)
    SkipLinesIfFlagDisabled(2, 9006)
    EnableFlag(12607910)
    EnableFlag(12607911)
    SkipLinesIfFlagDisabled(2, 9007)
    EnableFlag(12607930)
    EnableFlag(12607931)
    SkipLinesIfFlagDisabled(2, 9008)
    EnableFlag(12607950)
    EnableFlag(12607951)
    SkipLinesIfFlagDisabled(2, 9009)
    EnableFlag(12607970)
    EnableFlag(12607971)
    SkipLinesIfFlagDisabled(2, 9010)
    EnableFlag(12607990)
    EnableFlag(12607991)
    DisableFlagRange((9000, 9010))


def Event12607050(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12607050: Event 12607050 """
    EndIfFlagEnabled(arg_0_3)
    DisableGravity(arg_4_7)
    IfCharacterBackreadEnabled(0, arg_4_7)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    ForceAnimation(arg_4_7, 101165, loop=True)
    Wait(1.0)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    IfFlagEnabled(0, arg_0_3)
    ForceAnimation(arg_4_7, 101166, wait_for_completion=True)
    DisableCharacter(arg_4_7)
