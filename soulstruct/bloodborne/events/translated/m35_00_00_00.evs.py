"""
linked:
180

strings:
0: ボス撃破_女性ハンター
24: PC情報_ボス撃破_女性ハンター
58: ボス_戦闘開始
74: ボス_撃破時間
90: ボス撃破_患者B
108: PC情報_ボス撃破_患者B
136: ボス戦闘開始_患者B
158: ボス撃破時間_患者B
180: N:\\SPRJ\\data\\Param\\event\\common.emevd
"""
from soulstruct.bloodborne.events import *
from .common_entities import *
from .m35_00_entities import *


def Constructor():
    """ 0: Event 0 """
    Event13501810()
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    AddSpecialEffect(PLAYER, 9920, affect_npc_part_hp=False)
    SkipLinesIfClient(2)
    SkipLinesIfFlagDisabled(1, 13500100)
    EnableFlag(13500101)
    RunEvent(7000, slot=60, args=(3500950, 3501950, 999, 13507800))
    RunEvent(7000, slot=61, args=(3500951, 3501951, Flags.LivingFailuresDead, 13507820))
    RunEvent(7000, slot=62, args=(3500952, 3501952, Flags.LadyMariaDead, 13507840))
    RunEvent(7100, slot=60, args=(73500200, 3501950))
    RunEvent(7100, slot=61, args=(73500201, 3501951))
    RunEvent(7100, slot=62, args=(73500202, 3501952))
    RunEvent(7200, slot=60, args=(73500100, 3501950, 2102953))
    RunEvent(7200, slot=61, args=(73500101, 3501951, 2102953))
    RunEvent(7200, slot=62, args=(73500102, 3501952, 2102953))
    RunEvent(7300, slot=60, args=(72103500, 3501950))
    RunEvent(7300, slot=61, args=(72103501, 3501951))
    RunEvent(7300, slot=62, args=(72103502, 3501952))
    RunEvent(7600, slot=71, args=(3501990, 3503990))
    DisableMapCollision(3504810)
    DisableMapCollision(3504811)
    DisableMapCollision(3504812)
    SetCollisionResState(3504813, state=False)
    SetCollisionResState(3504814, state=False)
    EnableFlag(3510)
    EnableFlag(3511)
    DisableFlag(3512)
    DisableFlag(3513)
    EnableFlag(3515)
    EnableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    DisableMapCollision(3504812)
    DisableMapCollision(3504813)
    EnableMapCollision(3504814)
    SkipLinesIfFlagDisabled(11, 9470)
    DisableFlag(3510)
    DisableFlag(3511)
    DisableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    DisableMapCollision(3504812)
    DisableMapCollision(3504813)
    EnableMapCollision(3504814)
    SkipLinesIfFlagDisabled(11, Flags.LivingFailuresDead)
    EnableFlag(3510)
    EnableFlag(3511)
    EnableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    EnableFlag(3517)
    DisableFlag(3518)
    EnableMapCollision(3504812)
    DisableMapCollision(3504813)
    DisableMapCollision(3504814)
    SkipLinesIfFlagDisabled(11, Flags.LadyMariaFirstTimeDone)
    EnableFlag(3510)
    EnableFlag(3511)
    DisableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    DisableMapCollision(3504812)
    EnableMapCollision(3504813)
    DisableMapCollision(3504814)
    SkipLinesIfFlagDisabled(11, Flags.LadyMariaDead)
    EnableFlag(3510)
    EnableFlag(3511)
    EnableFlag(3512)
    EnableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    DisableMapCollision(3504812)
    EnableMapCollision(3504813)
    DisableMapCollision(3504814)
    RegisterLadder(start_climbing_flag=13501300, stop_climbing_flag=13501301, obj=3501080)
    RegisterLadder(start_climbing_flag=13501302, stop_climbing_flag=13501303, obj=3501081)
    RegisterLadder(start_climbing_flag=13501304, stop_climbing_flag=13501305, obj=3501082)
    RegisterLadder(start_climbing_flag=13501306, stop_climbing_flag=13501307, obj=3501083)
    RegisterLadder(start_climbing_flag=13501308, stop_climbing_flag=13501309, obj=3501084)
    RunEvent(13504700, slot=0, args=(3500790, 13504701, 13504711, 3510, 999))
    RunEvent(13504700, slot=5, args=(3500791, 13504702, 12604712, 3511, 999))
    RunEvent(13504710, slot=0, args=(3500790, 13504701, 13504711, 13504721))
    RunEvent(13504710, slot=5, args=(3500791, 13504702, 13504712, 13504722))
    RunEvent(13504720, slot=0, args=(3500790, 13504701, 13504711, 13504721))
    RunEvent(13504720, slot=5, args=(3500791, 13504702, 13504712, 13504722))
    RunEvent(13504730, slot=0, args=(3500790, 13504701, 13504711, 3510, 13504810, 999, 999, 13504712))
    RunEvent(13504730, slot=5, args=(3500791, 13504702, 13504712, 3511, 13504860, 999, 999, 13504711))
    Event13504740()
    Event13504742()

    # LADY MARIA OF THE ASTRAL CLOCKTOWER
    LadyMariaDies()
    LadyMariaFirstTime()
    EnterLadyMariaFog()
    EnterLadyMariaFogAsSummon()
    StartLadyMariaBattle()
    ControlLadyMariaMusic()
    ControlLadyMariaCamera()
    StopLadyMariaMusic()
    Event13504806()
    Event13504807()
    ControlLadyMariaInChair()
    OpenAstralClocktower()
    LadyMariaItemDrop()
    LadyMariaObjectDestroyed(0, 3501906)
    LadyMariaObjectDestroyed(1, 3501910)
    CancelLadyMariaBuff()
    
    # LIVING FAILURES
    LivingFailuresDie()
    LivingFailuresFirstTime()
    SummonStartLivingFailuresBattle()
    EnterLivingFailuresFog()
    EnterLivingFailuresFogAsSummon()
    StartLivingFailuresBattle()
    ControlLivingFailuresMusic()
    ControlLivingFailuresCamera()
    StopLivingFailuresMusic()
    Event13504856()
    Event13504857()
    LivingFailuresMeteorAttackRoll()
    LivingFailuresMeteorAttackFinished()
    LivingFailureMagicOrb(1, Characters.LivingFailure2, 13504873)
    LivingFailureMagicOrb(2, Characters.LivingFailure3, 13504874)
    LivingFailureMeteorSummon(0, Characters.LivingFailure1)
    LivingFailureMeteorSummon(1, Characters.LivingFailure2)
    LivingFailureMeteorSummon(2, Characters.LivingFailure3)
    LivingFailureMeteorSummon(3, Characters.LivingFailure4)
    LivingFailuresMeteorAttackRequest()
    LivingFailuresSpawnRequest()
    RequestActiveLivingFailureCountOnSpawnAndDeath(0, Characters.LivingFailure1)
    RequestActiveLivingFailureCountOnSpawnAndDeath(1, Characters.LivingFailure2)
    RequestActiveLivingFailureCountOnSpawnAndDeath(2, Characters.LivingFailure3)
    RequestActiveLivingFailureCountOnSpawnAndDeath(3, Characters.LivingFailure4)
    CountActiveLivingFailures()
    SpawnLivingFailure()
    CommandLivingFailuresMeteorCreator()
    KillRemainingLivingFailure(0, Characters.LivingFailure1)
    KillRemainingLivingFailure(1, Characters.LivingFailure2)
    KillRemainingLivingFailure(2, Characters.LivingFailure3)
    KillRemainingLivingFailure(3, Characters.LivingFailure4)

    Event13501100()
    Event13501105()
    Event13501104()
    Event13501140()
    Event13501141()
    Event13501142()
    SkipLinesIfFlagDisabled(3, 13501108)
    Event13501101()
    Event13501102()
    Event13501103()
    EnableFlag(13501118)
    Event13501110()
    Event13501111()
    Event13501112()
    Event13501113()
    Event13501114()
    Event13501115()
    Event13501120()
    Event13501121()
    Event13501122()
    Event13501123()
    Event13501124()
    Event13501125()
    RunEvent(13501200, slot=0, args=(3501120, 13504220, 1, 3500020, 0, 4294967295))
    RunEvent(13501200, slot=1, args=(3501130, 13504230, 1, 3500030, 0, 4294967295))
    RunEvent(13501200, slot=2, args=(3501141, 13504241, 2, 3500040, 0, 4294967295))
    RunEvent(13501200, slot=3, args=(3501142, 13504242, 2, 3500040, 0, 4294967295))
    RunEvent(13501200, slot=4, args=(3501145, 13504245, 2, 3500041, 0, 4294967295))
    RunEvent(13501200, slot=5, args=(3501146, 13504246, 2, 3500040, 0, 4294967295))
    RunEvent(13501200, slot=6, args=(3501140, 13504242, 2, 3500040, 0, 4294967295))
    RunEvent(13501200, slot=7, args=(3501161, 13504261, 1, 3500062, 13504271, 3500063))
    RunEvent(13501200, slot=8, args=(3501162, 13504262, 1, 3500062, 13504272, 3500063))
    RunEvent(13501200, slot=9, args=(3501163, 13504263, 1, 3500062, 13504273, 3500063))
    RunEvent(13501200, slot=10, args=(3501164, 13504264, 1, 3500062, 13504274, 3500063))
    RunEvent(13501200, slot=11, args=(3501165, 13504265, 1, 3500062, 13504275, 3500063))
    RunEvent(13501200, slot=12, args=(3501166, 13504266, 1, 3500062, 13504276, 3500063))
    RunEvent(13501200, slot=13, args=(3501170, 13504270, 1, 3500070, 0, 4294967295))
    Event13501250()
    RunEvent(13501400, slot=0, args=(3501350, 13500020, 9942))
    RunEvent(13501400, slot=1, args=(3501351, 13500021, 9942))
    RunEvent(13501400, slot=2, args=(3501352, 13500022, 9942))
    Event13504799()
    Event13500100()
    Event13500105()
    Event13500106()
    Event13500110()
    Event13500111()
    Event13500130()
    Event13500150()
    RunEvent(13500410, slot=0, args=(3500310, 3500339))
    RunEvent(13500410, slot=1, args=(3500337, 3500340))
    RunEvent(13500410, slot=2, args=(3500351, 3500341))
    RunEvent(13500410, slot=3, args=(3500921, 3500923))
    RunEvent(13500410, slot=4, args=(3500935, 3500933))
    RunEvent(13500410, slot=5, args=(3500661, 3500663))
    RunEvent(13500420, slot=0, args=(3500310, 9000, 40))
    RunEvent(13500420, slot=1, args=(3500337, 9000, 10))
    RunEvent(13500430, slot=0, args=(13500420, 3500310, 9060))
    RunEvent(13500430, slot=1, args=(13500421, 3500337, 9060))
    RunEvent(13500450, slot=0, args=(3500740, 53501700))
    RunEvent(13500450, slot=1, args=(3500741, 53501710))
    RunEvent(13500450, slot=2, args=(3500742, 53501720))
    RunEvent(13500450, slot=3, args=(3500781, 53508100))
    RunEvent(13500460, slot=0, args=(3500930, 103170, 13501900))
    RunEvent(13500500, slot=0, args=(3501500, 3500200, 10010611))
    RunEvent(13500500, slot=1, args=(3501501, 3500200, 10010611))
    RunEvent(13500500, slot=2, args=(3501502, 3500200, 10010620))
    RunEvent(13500500, slot=3, args=(3501503, 3500200, 10010620))
    RunEvent(13500500, slot=4, args=(3501510, 3500200, 10010616))
    RunEvent(13500500, slot=5, args=(3501511, 3500200, 10010616))
    RunEvent(13500500, slot=6, args=(3501512, 3500200, 10010616))
    RunEvent(13500500, slot=7, args=(3501513, 3500200, 10010616))
    RunEvent(13500500, slot=8, args=(3501514, 3500200, 10010612))
    RunEvent(13500500, slot=9, args=(3501515, 3500200, 10010612))
    RunEvent(13500500, slot=10, args=(3501520, 3500200, 10010617))
    RunEvent(13500500, slot=11, args=(3501521, 3500200, 10010617))
    RunEvent(13500500, slot=12, args=(3501522, 3500200, 10010613))
    RunEvent(13500500, slot=13, args=(3501523, 3500200, 10010613))
    RunEvent(13500500, slot=14, args=(3501530, 3500200, 10010618))
    RunEvent(13500500, slot=15, args=(3501531, 3500200, 10010618))
    RunEvent(13500500, slot=16, args=(3501532, 3500200, 10010618))
    RunEvent(13500500, slot=17, args=(3501533, 3500200, 10010618))
    RunEvent(13500500, slot=18, args=(3501534, 3500200, 10010614))
    RunEvent(13500500, slot=19, args=(3501535, 3500200, 10010614))
    RunEvent(13500500, slot=20, args=(3501540, 3500200, 10010619))
    RunEvent(13500500, slot=21, args=(3501541, 3500200, 10010619))
    RunEvent(13500500, slot=22, args=(3501542, 3500200, 10010615))
    RunEvent(13500500, slot=23, args=(3501543, 3500200, 10010615))
    RunEvent(13505050, slot=0, args=(3500451,))
    Event13505060()
    Event13505410()
    RunEvent(13505110, slot=0, args=(3500934, 3502343))
    RunEvent(13505300, slot=0, args=(3500661,))
    RunEvent(13505300, slot=1, args=(3500921,))
    RunEvent(13505300, slot=2, args=(3500935,))
    RunEvent(13505300, slot=3, args=(3500600,))
    RunEvent(13505300, slot=4, args=(3500301,))
    RunEvent(13505300, slot=5, args=(3500302,))
    RunEvent(13505300, slot=6, args=(3500306,))
    RunEvent(13505300, slot=7, args=(3500308,))
    RunEvent(13505300, slot=8, args=(3500309,))
    RunEvent(13505300, slot=9, args=(3500310,))
    RunEvent(13505300, slot=10, args=(3500311,))
    RunEvent(13505300, slot=11, args=(3500312,))
    RunEvent(13505300, slot=12, args=(3500313,))
    RunEvent(13505300, slot=13, args=(3500314,))
    RunEvent(13505300, slot=14, args=(3500315,))
    RunEvent(13505300, slot=15, args=(3500316,))
    RunEvent(13505300, slot=16, args=(3500321,))
    RunEvent(13505300, slot=17, args=(3500322,))
    RunEvent(13505300, slot=18, args=(3500323,))
    RunEvent(13505300, slot=19, args=(3500324,))
    RunEvent(13505300, slot=20, args=(3500325,))
    RunEvent(13505300, slot=21, args=(3500326,))
    RunEvent(13505300, slot=22, args=(3500327,))
    RunEvent(13505300, slot=23, args=(3500328,))
    RunEvent(13505300, slot=24, args=(3500331,))
    RunEvent(13505300, slot=25, args=(3500334,))
    RunEvent(13505300, slot=26, args=(3500335,))
    RunEvent(13505300, slot=27, args=(3500336,))
    RunEvent(13505300, slot=28, args=(3500337,))
    RunEvent(13505300, slot=29, args=(3500339,))
    RunEvent(13505300, slot=30, args=(3500340,))
    RunEvent(13505300, slot=31, args=(3500341,))
    RunEvent(13505300, slot=32, args=(3500342,))
    RunEvent(13505300, slot=33, args=(3500343,))
    RunEvent(13505300, slot=34, args=(3500344,))
    RunEvent(13505300, slot=35, args=(3500346,))
    RunEvent(13505300, slot=36, args=(3500347,))
    RunEvent(13505300, slot=37, args=(3500348,))
    RunEvent(13505300, slot=38, args=(3500349,))
    RunEvent(13505300, slot=39, args=(3500351,))
    RunEvent(13505300, slot=40, args=(3500353,))
    RunEvent(13505300, slot=41, args=(3500360,))
    RunEvent(13505300, slot=42, args=(3500362,))
    RunEvent(13505300, slot=43, args=(3500364,))
    RunEvent(13505300, slot=44, args=(3500365,))
    RunEvent(13505300, slot=45, args=(3500366,))
    RunEvent(13505300, slot=46, args=(3500371,))
    RunEvent(13505300, slot=47, args=(3500389,))
    RunEvent(13505300, slot=48, args=(3500392,))
    RunEvent(13505300, slot=49, args=(3500393,))
    RunEvent(13505300, slot=50, args=(3500395,))
    RunEvent(13505300, slot=51, args=(3500400,))
    RunEvent(13505300, slot=52, args=(3500401,))
    RunEvent(13505300, slot=53, args=(3500451,))
    RunEvent(13505300, slot=54, args=(3500452,))
    RunEvent(13505300, slot=55, args=(3500500,))
    RunEvent(13505300, slot=56, args=(3500501,))
    RunEvent(13505300, slot=57, args=(3500502,))
    RunEvent(13505300, slot=58, args=(3500771,))
    RunEvent(13505300, slot=59, args=(3500777,))
    RunEvent(13505400, slot=0, args=(3500658, 3502251, 0.0, 3502255), arg_types="iifi")
    RunEvent(13505470, slot=0, args=(3500312, 9005, 2004, 402020))
    RunEvent(13505470, slot=2, args=(3500390, 9001, 2004, 402020))
    RunEvent(13505470, slot=3, args=(3500396, 9003, 2004, 402020))
    RunEvent(13505470, slot=4, args=(3500397, 9006, 2004, 402020))
    RunEvent(13505470, slot=5, args=(3500398, 9002, 2004, 402020))
    RunEvent(13505470, slot=6, args=(3500502, 7001, 0, 402035))
    RunEvent(13505470, slot=7, args=(3500503, 7001, 0, 402035))
    RunEvent(13505510, slot=0, args=(3500350, 3502301, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=2, args=(3500360, 3502301, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=3, args=(3500361, 3502301, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=4, args=(3500363, 3502301, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=5, args=(3500364, 3502301, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=6, args=(3500366, 3502301, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=7, args=(3500301, 3502312, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=8, args=(3500302, 3502312, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=9, args=(3500303, 3502305, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=10, args=(3500409, 3502305, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=11, args=(3500450, 3502305, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=12, args=(3500346, 3502306, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=13, args=(3500347, 3502306, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=14, args=(3500348, 3502306, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=15, args=(3500349, 3502306, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=16, args=(3500371, 3502306, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=17, args=(3500750, 3502307, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=18, args=(3500760, 3502307, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=19, args=(3500313, 3502309, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=20, args=(3500314, 3502309, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=21, args=(3500313, 3502310, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=22, args=(3500314, 3502310, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=23, args=(3500452, 3502313, 5.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=24, args=(3500356, 3502314, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=25, args=(3500357, 3502314, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=26, args=(3500359, 3502314, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=27, args=(3500933, 3502304, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=28, args=(3500935, 3502304, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=35, args=(3500315, 3502321, 2.0, 1.0), arg_types="iiff")
    RunEvent(13505510, slot=36, args=(3500316, 3502321, 2.0, 1.0), arg_types="iiff")
    RunEvent(13505510, slot=37, args=(3500353, 3502325, 1.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=38, args=(3500770, 3502311, 5.0, 1.0), arg_types="iiff")
    RunEvent(13505510, slot=39, args=(3500772, 3502311, 5.0, 1.0), arg_types="iiff")
    RunEvent(13505510, slot=40, args=(3500311, 3502302, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=41, args=(3500773, 3502329, 3.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=43, args=(3500776, 3502329, 3.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=44, args=(3500335, 3502315, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=46, args=(3500334, 3502315, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=47, args=(3500601, 3502336, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=48, args=(3500607, 3502337, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=49, args=(3500610, 3502337, 2.0, 1.0), arg_types="iiff")
    RunEvent(13505510, slot=50, args=(3500606, 3502337, 2.0, 1.0), arg_types="iiff")
    RunEvent(13505510, slot=51, args=(3500613, 3502339, 3.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=52, args=(3500614, 3502339, 3.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=53, args=(3500400, 3502341, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=54, args=(3500401, 3502335, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505510, slot=55, args=(3500600, 3502391, 2.0, 1.0), arg_types="iiff")
    RunEvent(13505510, slot=56, args=(3500329, 3502312, 2.0, 0.0), arg_types="iiff")
    RunEvent(13505200, slot=0, args=(3500301, 3503431))
    RunEvent(13505200, slot=1, args=(3500302, 3503431))
    RunEvent(13505200, slot=2, args=(3500313, 3503431))
    RunEvent(13505200, slot=3, args=(3500314, 3503431))
    RunEvent(13505200, slot=4, args=(3500364, 3503430))
    RunEvent(13505200, slot=5, args=(3500366, 3503430))
    RunEvent(13505200, slot=6, args=(3500452, 3503432))
    RunEvent(13505570, slot=0, args=(3500310, 3502301, 2.0, 0.0, 3502380, 3502306, 3503380), arg_types="iiffiii")
    RunEvent(13505570, slot=2, args=(3500362, 3502301, 2.0, 0.0, 3502381, 3502321, 3503380), arg_types="iiffiii")
    RunEvent(13505570, slot=3, args=(3500365, 3502301, 2.0, 0.0, 3502381, 3502321, 3503380), arg_types="iiffiii")
    RunEvent(13505450, slot=0, args=(3500781, 3502317, 2.0, 3001), arg_types="iifi")
    RunEvent(13505590, slot=0, args=(3500389, 3502303, 2.0, 9006, 0, 0.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=1, args=(3500780, 3502316, 2.0, 0, 3005, 0.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=7, args=(3500360, 3502326, 2.0, 9000, 9060, 0.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=8, args=(3500306, 3502302, 3.0, 9006, 0, 0.0, 0.0, 3502321), arg_types="iifiiffi")
    RunEvent(13505590, slot=10, args=(3500308, 3502302, 3.0, 9000, 9060, 0.0, 0.0, 3502321), arg_types="iifiiffi")
    RunEvent(13505590, slot=11, args=(3500309, 3502302, 3.0, 9002, 0, 0.0, 0.0, 3502321), arg_types="iifiiffi")
    RunEvent(13505590, slot=12, args=(3500337, 3502301, 3.0, 9002, 0, 0.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=13, args=(3500605, 3502337, 0.0, 7000, 7001, 1.0, 2.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=14, args=(3500609, 3502337, 0.0, 7000, 7001, 2.0, 3.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=15, args=(3500612, 3502337, 0.0, 7000, 7001, 2.0, 3.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=16, args=(3500342, 3502319, 6.0, 9006, 0, 0.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=17, args=(3500343, 3502319, 6.0, 9003, 0, 3.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=18, args=(3500344, 3502319, 6.0, 9005, 0, 3.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=19, args=(3500336, 0, 7.0, 9006, 0, 2.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=20, args=(3500351, 3502301, 7.0, 9006, 0, 0.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505590, slot=22, args=(3500340, 0, 10.0, 9006, 0, 0.0, 0.0, 0), arg_types="iifiiffi")
    RunEvent(13505610, slot=0, args=(3500659, 3502251, 2.0, 9001, 9061, 1.0, 1.0), arg_types="iifiiff")
    RunEvent(13505610, slot=1, args=(3500655, 3502251, 2.0, 9001, 9061, 3.0, 3.0), arg_types="iifiiff")
    RunEvent(13505610, slot=2, args=(3500656, 3502251, 2.0, 9001, 9061, 2.0, 2.0), arg_types="iifiiff")
    RunEvent(13505640, slot=0, args=(3500550, 9013))
    RunEvent(13505640, slot=1, args=(3500551, 9014))
    RunEvent(13505640, slot=3, args=(3500553, 9001))
    RunEvent(13505640, slot=4, args=(3500554, 9000))
    RunEvent(13505640, slot=5, args=(3500555, 9011))
    RunEvent(13505640, slot=6, args=(3500556, 9010))
    RunEvent(13505700, slot=0, args=(3500400, 3022))
    RunEvent(13505700, slot=1, args=(3500401, 3022))
    RunEvent(13505750, slot=4, args=(3500303, 3502312, 0, 3503420, 0.0, 0), arg_types="iiiifi")
    RunEvent(13505750, slot=8, args=(3500380, 3502312, 0, 3503420, 8.0, 0), arg_types="iiiifi")
    RunEvent(13505750, slot=9, args=(3500381, 3502312, 0, 3503420, 7.0, 0), arg_types="iiiifi")
    RunEvent(13505780, slot=1, args=(3500601,))
    RunEvent(13505780, slot=2, args=(3500602,))
    RunEvent(13505780, slot=3, args=(3500603,))
    RunEvent(13505780, slot=4, args=(3500604,))
    RunEvent(13505780, slot=5, args=(3500605,))
    RunEvent(13505780, slot=6, args=(3500606,))
    RunEvent(13505780, slot=7, args=(3500607,))
    RunEvent(13505780, slot=8, args=(3500608,))
    RunEvent(13505780, slot=9, args=(3500609,))
    RunEvent(13505780, slot=10, args=(3500610,))
    RunEvent(13505780, slot=11, args=(3500611,))
    RunEvent(13505780, slot=12, args=(3500612,))
    RunEvent(13505780, slot=13, args=(3500342,))
    RunEvent(13505780, slot=14, args=(3500343,))
    RunEvent(13505780, slot=15, args=(3500344,))
    RunEvent(13505780, slot=16, args=(3500345,))
    RunEvent(13505780, slot=17, args=(3500613,))
    RunEvent(13505780, slot=18, args=(3500614,))
    RunEvent(13505797, slot=0, args=(3501270,))
    RunEvent(13505797, slot=1, args=(3501271,))
    RunEvent(13505797, slot=2, args=(3501272,))
    RunEvent(13505800, slot=0, args=(3502600, 3501600, 0, 3501601, 3500751))
    RunEvent(13505800, slot=1, args=(3502610, 3501610, 0, 3501611, 0))
    RunEvent(13505800, slot=2, args=(3502640, 3501640, 0, 3501641, 0))
    RunEvent(13505810, slot=0, args=(3502630, 3501630, 0, 3501631, 3501621, 3500764))
    RunEvent(13505820, slot=0, args=(3500321, 9014, 9064, 10, 3503421, 3502431))
    RunEvent(13505820, slot=1, args=(3500322, 9015, 0, 80, 3503422, 3502432))
    RunEvent(13505820, slot=2, args=(3500323, 9014, 9064, 5, 3503423, 3502433))
    RunEvent(13505820, slot=3, args=(3500324, 9015, 0, 45, 3503424, 3502434))
    RunEvent(13505820, slot=4, args=(3500325, 9014, 9064, 8, 3503425, 3502435))
    RunEvent(13505820, slot=5, args=(3500326, 9014, 9064, 3, 3503426, 3502436))
    RunEvent(13505820, slot=6, args=(3500327, 9015, 0, 62, 3503427, 3502437))
    RunEvent(13505820, slot=7, args=(3500328, 9014, 9064, 12, 3503428, 3502438))
    RunEvent(13500942, slot=0, args=(10000, 3502902, 73500410))
    RunEvent(13500943, slot=0, args=(3500901,))
    RunEvent(13500944, slot=0, args=(3500901,))
    Event13500941()
    RunEvent(13500978, slot=0, args=(1730, 73500415, 3500938))
    RunEvent(13505900, slot=0, args=(13505910, 13505911, 13505912, 3502890, 0, 6001))
    RunEvent(13505901, slot=0, args=(13505910, 13505911, 13505912, 3502891, 0))
    RunEvent(13505902, slot=0, args=(3500936, 13505911, 13505912, 3502892, 3502896, 13505910, 13505913, 3502893))
    RunEvent(13505903, slot=0, args=(3500936, 13505911, 13505912, 3502894, 3502895, 13505913))
    RunEvent(13505904, slot=0, args=(3500936, 13505911, 13505912, 43710, 3500937))
    Event13501960()
    RunEvent(13500963, slot=0, args=(3500910, 1750, 1769, 1752, 1750))
    RunEvent(13500963, slot=1, args=(3500910, 1750, 1769, 1752, 1752))
    Event13500965()
    Event13500966()
    RunEvent(13500968, slot=0, args=(3500910,))
    Event13500998()
    Event13500999()
    RunEvent(13500951, slot=0, args=(3500900, 73500621, 1722))
    RunEvent(13500952, slot=0, args=(3500900,))
    RunEvent(13500946, slot=0, args=(Characters.LadyMariaFriendly, 3501905))
    RunEvent(13500948, slot=0, args=(3501905,))
    RunEvent(13500949, slot=0, args=(Characters.LadyMariaFriendly, 73500505))
    SetDistanceLimitForConversationStateChanges(3500552, distance=25.0)
    RunEvent(13500980, slot=0, args=(73500910, 73500911, 10.0), arg_types="iif")
    RunEvent(13500980, slot=1, args=(73500945, 73500946, 10.0), arg_types="iif")
    RunEvent(13500990, slot=0, args=(3500661, 73500971, 6000))
    RunEvent(13500990, slot=1, args=(3500662, 73500976, 6000))
    RunEvent(13500990, slot=2, args=(3500911, 73500327, 1762))
    RunEvent(13500990, slot=3, args=(3500663, 73500971, 6000))
    RunEvent(13500994, slot=0, args=(3500661, 3500921, 50002400, 73500974, 6000, 2.0, 2.0, 7010), arg_types="iiiiiffi")
    RunEvent(13500994, slot=1, args=(3500662, 3500920, 50002450, 73500979, 6000, 2.0, 2.0, 7010), arg_types="iiiiiffi")
    RunEvent(13500994, slot=2, args=(3500911, 3500922, 50002270, 73500339, 1762, 2.0, 2.0, 7010), arg_types="iiiiiffi")
    RunEvent(13500994, slot=3, args=(3500663, 3500921, 50002400, 73500974, 6000, 2.0, 2.0, 7010), arg_types="iiiiiffi")
    EnableImmortality(3500661)
    EnableImmortality(3500662)
    EnableImmortality(3500911)
    EnableImmortality(3500663)
    DisableFlag(73500970)
    DisableFlag(73500975)
    DisableFlag(73500971)
    DisableFlag(73500976)
    DisableFlag(73500974)
    DisableFlag(73500979)
    RunEvent(13500900, slot=0, args=(3500900, 1710, 1729, 1719, 1712))
    RunEvent(13500900, slot=1, args=(Characters.LadyMariaFriendly, 1650, 1669, 1659, 1650))
    RunEvent(13500900, slot=2, args=(3500901, 1730, 1749, 1734, 1730))
    RunEvent(13500910, slot=0, args=(3500900, 73500620))
    RunEvent(13500920, slot=0, args=(3500900, 73500620, 1710, 1729, 1727))
    RunEvent(13501900, slot=0, args=(3500930,))
    RunEvent(13501900, slot=1, args=(3500931,))
    RunEvent(13501900, slot=2, args=(3500932,))
    RunEvent(13501900, slot=3, args=(3500934,))
    RunEvent(13501900, slot=4, args=(3500935,))
    RunEvent(13501900, slot=6, args=(3500550,))
    RunEvent(13501900, slot=7, args=(3500551,))
    RunEvent(13501900, slot=8, args=(3500552,))
    RunEvent(13501900, slot=9, args=(3500553,))
    RunEvent(13501900, slot=10, args=(3500554,))
    RunEvent(13501900, slot=11, args=(3500555,))
    RunEvent(13501900, slot=12, args=(3500556,))
    Event13500977()
    RunEvent(13501915, slot=0, args=(3500933, 13501904))
    RunEvent(13500953, slot=0, args=(1712, 73500630, 43200))
    RunEvent(13501920, slot=1, args=(73500321, 43010))
    RunEvent(13501920, slot=2, args=(73500322, 43020))
    RunEvent(13501920, slot=3, args=(13501900, 43830))
    RunEvent(13501920, slot=4, args=(13501903, 43820))
    RunEvent(13501920, slot=5, args=(13501905, 43710))
    RunEvent(13501940, slot=0, args=(73500320, 43000))
    DeleteVFX(3503910, erase_root_only=False)
    RunEvent(13504400, slot=0, args=(13504440, 3503910, 13504420, 13504430, Flags.LivingFailuresDead, 6001))
    RunEvent(13504410, slot=0, args=(5, 3500940, 3502920, 13504420, 13504430, 13504440, Flags.LivingFailuresDead, 10564))
    RunEvent(13504450, slot=0, args=(3500940, 3502930, 13504420, 13504430, Flags.LivingFailuresFogEntered))
    RunEvent(13504460, slot=0, args=(3500940, 3502930, 3502810, 3502811, 101130, 13504450, 3502813))
    Event13500000()


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(13500940, slot=0, args=(3500901,))
    RunEvent(13500950, slot=0, args=(3500900,))
    RunEvent(13500945, slot=0, args=(Characters.LadyMariaFriendly, 3501905, 3501906, 3501907, 3501908, 3501909, Flags.LadyMariaFirstTimeDone))
    RunEvent(13500960, slot=0, args=(3500910, 3500911))
    RunEvent(13500400, slot=0, args=(3500331, 3502354, 3502350))
    RunEvent(13505630, slot=0, args=(3500771, 3502318, 0.0, 5.0), arg_types="iiff")
    RunEvent(13505630, slot=1, args=(3500777, 3502318, 3.0, 5.0), arg_types="iiff")


def Event13500000():
    """ 13500000: Event 13500000 """
    GotoIfFlagEnabled(Label.L0, 9471)
    EnableInvincibility(3500930)
    DisableHealthBar(3500930)
    IfFlagEnabled(0, 9471)

    # --- 0 --- #
    DefineLabel(0)
    DisableInvincibility(3500930)
    EnableHealthBar(3500930)


@RestartOnRest
def Event13504700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13504700: Event 13504700 """
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
    IfInsideMap(1, game_map=RESEARCH_HALL)
    IfCharacterHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, 30)
    SkipLinesIfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, arg_16_19)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(arg_0_3, 7011)
    WaitFrames(59)
    EnableAI(arg_0_3)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event13504710(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13504710: Event 13504710 """
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_8_11)
    IfInsideMap(1, game_map=RESEARCH_HALL)
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
def Event13504720(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13504720: Event 13504720 """
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_12_15)
    IfFlagEnabled(-1, arg_8_11)
    IfClientTypeCountComparison(-1, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfOutsideMap(-1, game_map=RESEARCH_HALL)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(arg_0_3, 9100)
    ReplanAI(arg_0_3)
    DisableFlag(arg_12_15)
    Restart()


@RestartOnRest
def Event13504730(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int, arg_28_31: int):
    """ 13504730: Event 13504730 """
    IfFlagEnabled(-15, arg_8_11)
    IfFlagEnabled(-15, arg_12_15)
    IfFlagEnabled(-15, arg_16_19)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_24_27)
    IfHealthEqual(2, arg_0_3, 0.0)
    IfFlagEnabled(-2, arg_16_19)
    IfFlagEnabled(-2, arg_28_31)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=-2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_8_11)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-2)
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
def Event13504740():
    """ 13504740: Enables a flag as long as player is standing on one of five collisions. Can't find anywhere this
    flag is referenced, though. """
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 3504000)
    IfPlayerStandingOnCollision(-1, 3504001)
    IfPlayerStandingOnCollision(-1, 3504002)
    IfPlayerStandingOnCollision(-1, 3504003)
    IfPlayerStandingOnCollision(-1, 3504004)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504741)
    IfCharacterHuman(2, PLAYER)
    IfPlayerStandingOnCollision(-2, 3504000)
    IfPlayerStandingOnCollision(-2, 3504001)
    IfPlayerStandingOnCollision(-2, 3504002)
    IfPlayerStandingOnCollision(-2, 3504003)
    IfPlayerStandingOnCollision(-2, 3504004)
    IfConditionFalse(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13504741)
    Restart()


@RestartOnRest
def Event13504742():
    """ 13504742: Enables a flag as long as player is standing on one of 21 collisions. Can't find anywhere this
    flag is referenced, though. """
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 3504020)
    IfPlayerStandingOnCollision(-1, 3504021)
    IfPlayerStandingOnCollision(-1, 3504022)
    IfPlayerStandingOnCollision(-1, 3504023)
    IfPlayerStandingOnCollision(-1, 3504024)
    IfPlayerStandingOnCollision(-1, 3504025)
    IfPlayerStandingOnCollision(-1, 3504026)
    IfPlayerStandingOnCollision(-1, 3504027)
    IfPlayerStandingOnCollision(-1, 3504028)
    IfPlayerStandingOnCollision(-1, 3504029)
    IfPlayerStandingOnCollision(-1, 3504030)
    IfPlayerStandingOnCollision(-1, 3504031)
    IfPlayerStandingOnCollision(-1, 3504032)
    IfPlayerStandingOnCollision(-1, 3504033)
    IfPlayerStandingOnCollision(-1, 3504034)
    IfPlayerStandingOnCollision(-1, 3504035)
    IfPlayerStandingOnCollision(-1, 3504036)
    IfPlayerStandingOnCollision(-1, 3504037)
    IfPlayerStandingOnCollision(-1, 3504038)
    IfPlayerStandingOnCollision(-1, 3504039)
    IfPlayerStandingOnCollision(-1, 3504040)
    IfPlayerStandingOnCollision(-1, 3504041)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504743)
    IfCharacterHuman(2, PLAYER)
    IfPlayerStandingOnCollision(-2, 3504020)
    IfPlayerStandingOnCollision(-2, 3504021)
    IfPlayerStandingOnCollision(-2, 3504022)
    IfPlayerStandingOnCollision(-2, 3504023)
    IfPlayerStandingOnCollision(-2, 3504024)
    IfPlayerStandingOnCollision(-2, 3504025)
    IfPlayerStandingOnCollision(-2, 3504026)
    IfPlayerStandingOnCollision(-2, 3504027)
    IfPlayerStandingOnCollision(-2, 3504028)
    IfPlayerStandingOnCollision(-2, 3504029)
    IfPlayerStandingOnCollision(-2, 3504030)
    IfPlayerStandingOnCollision(-2, 3504031)
    IfPlayerStandingOnCollision(-2, 3504032)
    IfPlayerStandingOnCollision(-2, 3504033)
    IfPlayerStandingOnCollision(-2, 3504034)
    IfPlayerStandingOnCollision(-2, 3504035)
    IfPlayerStandingOnCollision(-2, 3504036)
    IfPlayerStandingOnCollision(-2, 3504037)
    IfPlayerStandingOnCollision(-2, 3504038)
    IfPlayerStandingOnCollision(-2, 3504039)
    IfPlayerStandingOnCollision(-2, 3504040)
    IfPlayerStandingOnCollision(-2, 3504041)
    IfConditionFalse(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13504743)
    Restart()


def LadyMariaDies():
    """ 13501800: Event 13501800 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(Characters.LadyMaria)
    Kill(Characters.LadyMaria, award_souls=False)
    DisableObject(Objects.LadyMariaFog)
    DeleteVFX(VFX.LadyMariaFog, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, Characters.LadyMaria)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.LadyMariaFog)
    DeleteVFX(VFX.LadyMariaFog, erase_root_only=True)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=0)
    Wait(3.0)
    KillBoss(Characters.LadyMaria)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    AwardAchievement(Achievements.LadyMariaDefeated)
    RunEvent(9350, slot=0, args=(3,))
    EnableFlag(6675)
    EnableFlag(3510)
    EnableFlag(3511)
    EnableFlag(3512)
    EnableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    StopPlayLogMeasurement(3500000)
    StopPlayLogMeasurement(3500001)
    StopPlayLogMeasurement(3500010)
    CreatePlayLog(0)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 24, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 24, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 24, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 24, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def LadyMariaFirstTime():
    """ 13501801: Event 13501801 """
    IfFlagDisabled(1, Flags.LadyMariaDead)
    IfThisEventFlagDisabled(1)
    GotoIfConditionTrue(Label.L5, input_condition=1)
    DeleteVFX(3503820, erase_root_only=False)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableCharacter(Characters.LadyMaria)
    DisableFlag(13500947)
    IfFlagEnabled(0, 13500947)
    DeleteObjectVFX(3501905, erase_root=False)
    DeleteVFX(3503820, erase_root_only=False)
    EnableFlag(9180)
    WaitFrames(1)
    GotoIfFlagEnabled(Label.L0, 1651)
    PlayCutscene(35000010, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=3502808, 
                 move_to_map=RESEARCH_HALL)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(35000010, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=3502808, 
                 move_to_map=RESEARCH_HALL)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlag(9180)
    EnableCharacter(Characters.LadyMaria)
    DisableCharacter(Characters.LadyMariaFriendly)  # Isn't she already disabled (cut content)?
    DisableBackread(Characters.LadyMariaFriendly)
    DisableObjectInvulnerability(3501906)
    DisableObject(3501907)  # Lady Maria in chair
    DisableObject(3501908)  # Lady Maria in chair
    EnableFlag(Flags.LadyMariaFogEntered)
    EnableFlag(3510)
    EnableFlag(3511)
    DisableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    DisableFlag(3517)
    DisableFlag(3518)
    EndIfFlagEnabled(9346)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9346)


@RestartOnRest
def OpenAstralClocktower():
    """ 13501802: Event 13501802 """
    DisableSoundEvent(3503204)
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(3501200, 3)
    DisableMapCollision(3504800)
    DisableObjectActivation(3501201, obj_act_id=3500100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfPlayerHasGood(1, 4021, including_box=False)
    IfCharacterOutsideRegion(1, PLAYER, region=3502803)
    IfActionButtonParamActivated(1, action_button_id=3500912, entity=3501802)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3501802, animation=101340)
    WaitFrames(120)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.a_Ambient, sound_id=350000012)
    WaitFrames(60)
    ForceAnimation(3501200, 2, wait_for_completion=True)
    DisableMapCollision(3504800)
    EnableFlag(9468)


def LadyMariaItemDrop():
    """ 13501803: Event 13501803 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfFlagEnabled(0, Flags.LadyMariaDead)
    CreateObjectVFX(900201, obj=3501801, model_point=200)
    IfActionButtonParamActivated(0, action_button_id=3500911, entity=3501801)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(3501800, host_only=False)
    DeleteObjectVFX(3501801, erase_root=True)


def Event13501804():
    """ 13501804: UNUSED. Probably said that the Clock was already open. """
    DisableNetworkSync()
    IfFlagEnabled(1, 13501802)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=3501201)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Restart()


def LadyMariaObjectDestroyed(_, obj: int):
    """ 13501805: Event 13501805 """
    IfFlagEnabled(1, Flags.LadyMariaDead)
    IfThisEventSlotFlagEnabled(1)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfObjectDestroyed(0, obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(obj)
    End()


def ControlLadyMariaInChair():
    """ 13501807: Event 13501807 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.LadyMariaFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(Characters.LadyMaria)
    DisableCharacter(Characters.LadyMariaFriendly)
    DisableBackread(Characters.LadyMariaFriendly)
    DisableObjectInvulnerability(3501906)  # chair
    DisableObject(3501907)  # unknown
    DisableObject(3501908)  # unknown
    EnableFlag(Flags.LadyMariaFogEntered)
    EnableFlag(Flags.LadyMariaFirstTimeDone)


def Event13501810():
    """ 13501810: Event 13501810 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerStandingOnCollision(0, 3504020)
    RunEvent(9350, slot=0, args=(2,))


def EnterLadyMariaFog():
    """ 13504800: Event 13504800 """
    EndIfFlagEnabled(Flags.LadyMariaDead)
    GotoIfFlagEnabled(Label.L0, Flags.LadyMariaFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.LadyMariaFog)
    DeleteVFX(VFX.LadyMariaFog, erase_root_only=False)
    IfFlagDisabled(1, Flags.LadyMariaDead)
    IfFlagEnabled(1, Flags.LadyMariaFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.LadyMariaFog)
    CreateVFX(VFX.LadyMariaFog)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.LadyMariaDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=3500800, entity=Objects.LadyMariaFog)
    IfFlagEnabled(3, Flags.LadyMariaDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 3502800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3502801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.LadyMariaFogEntered)
    Restart()


def EnterLadyMariaFogAsSummon():
    """ 13504801: Event 13504801 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.LadyMariaDead)
    IfFlagDisabled(1, Flags.LadyMariaDead)
    IfFlagEnabled(1, Flags.LadyMariaFirstTimeDone)
    IfFlagEnabled(1, Flags.LadyMariaFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=3500800, entity=Objects.LadyMariaFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3502800, animation=101130)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=3502801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(13504809)
    Restart()


def StartLadyMariaBattle():
    """ 13504802: Event 13504802 """
    EndIfFlagEnabled(Flags.LadyMariaDead)
    DisableAI(Characters.LadyMaria)
    DisableHealthBar(Characters.LadyMaria)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.LadyMariaFogEntered)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 13504810)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.LadyMaria, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13504810)
    EnableFlag(Flags.LadyMariaFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.LadyMaria, 7500, affect_npc_part_hp=False)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.LadyMaria)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.LadyMaria, 7501, affect_npc_part_hp=False)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.LadyMaria)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.LadyMaria)
    EnableBossHealthBar(Characters.LadyMaria, name=452000, slot=0)
    DisableInvincibility(Characters.LadyMaria)
    SetCharacterEventTarget(Characters.LadyMaria, 3500801)
    CreatePlayLog(58)
    StartPlayLogMeasurement(3500010, 74, overwrite=True)


def ControlLadyMariaMusic():
    """ 13504803: Event 13504803 """
    DisableNetworkSync()
    DisableSoundEvent(3503802)
    DisableSoundEvent(3503803)
    DisableSoundEvent(3503804)
    DeleteVFX(3503501, erase_root_only=False)
    EndIfFlagEnabled(Flags.LadyMariaDead)
    GotoIfThisEventFlagEnabled(Label.L1)
    GotoIfFlagEnabled(Label.L0, 13504811)
    IfFlagDisabled(1, Flags.LadyMariaDead)
    IfFlagEnabled(1, Flags.LadyMariaBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 13504809)
    IfCharacterInsideRegion(1, PLAYER, region=3502802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(3503802)
    IfCharacterHasTAEEvent(2, Characters.LadyMaria, tae_event_id=100)  # Phase two

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.LadyMariaDead)
    IfFlagEnabled(2, Flags.LadyMariaBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 13504809)
    IfCharacterInsideRegion(2, PLAYER, region=3502802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(3503802)
    WaitFrames(0)
    EnableBossMusic(3503803)
    CreateVFX(3503501)
    DeleteVFX(3503500, erase_root_only=True)
    EnableFlag(13504811)
    IfCharacterHasTAEEvent(3, Characters.LadyMaria, tae_event_id=300)  # Phase three

    # --- 1 --- #
    DefineLabel(1)
    IfFlagDisabled(3, Flags.LadyMariaDead)
    IfFlagEnabled(3, Flags.LadyMariaBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(3, 13504809)
    IfCharacterInsideRegion(3, PLAYER, region=3502802)
    IfConditionTrue(0, input_condition=3)
    DisableBossMusic(3503803)
    WaitFrames(0)
    EnableBossMusic(3503804)


def ControlLadyMariaCamera():
    """ 13504804: Event 13504804 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.LadyMariaDead)
    IfCharacterAlive(1, Characters.LadyMaria)
    IfEntityWithinDistance(1, PLAYER, Characters.LadyMaria, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=1)
    IfCharacterDead(-1, Characters.LadyMaria)
    IfEntityBeyondDistance(-1, PLAYER, Characters.LadyMaria, radius=10.0)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=0)
    Restart()


def StopLadyMariaMusic():
    """ 13504805: Event 13504805 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.LadyMariaDead)
    IfCharacterDead(0, Characters.LadyMaria)
    DisableBossMusic(3503802)
    DisableBossMusic(3503803)
    DisableBossMusic(3503804)
    DisableBossMusic(-1)
    CreateVFX(3503500)  # Also handles these VFX.
    DeleteVFX(3503501, erase_root_only=True)


def Event13504806():
    """ 13504806: Event 13504806 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.LadyMariaFog, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event13504807():
    """ 13504807: Event 13504807 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.LadyMariaFog, radius=6.0)
    IfEntityWithinDistance(1, PLAYER, Objects.LadyMariaFog, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def CancelLadyMariaBuff():
    """ 13504822: Event 13504822 """
    EndIfFlagEnabled(Flags.LadyMariaDead)
    IfCharacterHasTAEEvent(0, Characters.LadyMaria, tae_event_id=20)
    CancelSpecialEffect(Characters.LadyMaria, 5526)
    Wait(0.10000000149011612)
    Restart()


def LivingFailuresDie():
    """ 13501850: Event 13501850 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(Characters.LivingFailuresHealthPool)
    DisableCharacter(Characters.LivingFailure1)
    DisableCharacter(Characters.LivingFailure2)
    DisableCharacter(Characters.LivingFailure3)
    DisableCharacter(Characters.LivingFailure4)
    Kill(Characters.LivingFailuresHealthPool, award_souls=False)
    Kill(Characters.LivingFailure1, award_souls=False)
    Kill(Characters.LivingFailure2, award_souls=False)
    Kill(Characters.LivingFailure3, award_souls=False)
    Kill(Characters.LivingFailure4, award_souls=False)
    DisableObject(Objects.LivingFailuresFog)
    DeleteVFX(VFX.LivingFailuresFog, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthEqual(0, Characters.LivingFailuresHealthPool, 0.0)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.LivingFailuresFog)
    DeleteVFX(VFX.LivingFailuresFog, erase_root_only=True)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=0)
    EnableMapCollision(3504812)
    DisableMapCollision(3504814)
    Wait(3.0)
    KillBoss(Characters.LivingFailuresHealthPool)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    AwardAchievement(38)
    RunEvent(9350, slot=0, args=(2,))
    AwardItemLot(3501850, host_only=False)
    EnableFlag(3510)
    EnableFlag(3511)
    EnableFlag(3512)
    DisableFlag(3513)
    DisableFlag(3515)
    DisableFlag(3516)
    EnableFlag(3517)
    DisableFlag(3518)
    StopPlayLogMeasurement(3500002)
    StopPlayLogMeasurement(3500003)
    StopPlayLogMeasurement(3500011)
    CreatePlayLog(90)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 108, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 108, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 108, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 108, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def LivingFailuresFirstTime():
    """ 13501851: Event 13501851 """
    DisableSoundEvent(3503211)
    DisableSoundEvent(3503212)
    EndIfFlagEnabled(Flags.LivingFailuresDead)
    EndIfThisEventFlagEnabled()
    ForceAnimation(Characters.LivingFailure1, 9000, loop=True)
    IfFlagDisabled(1, Flags.LivingFailuresDead)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3502815)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.a_Ambient, sound_id=350000020)
    ForceAnimation(Characters.LivingFailure1, 9060)
    ReplanAI(Characters.LivingFailure1)
    EnableFlag(Flags.LivingFailuresFogEntered)
    EndIfFlagEnabled(9348)
    RunEvent(9350, slot=0, args=(2,))
    EnableFlag(9348)


def SummonStartLivingFailuresBattle():
    """ 13501852: Event 13501852 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.LivingFailuresFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(Flags.LivingFailuresFogEntered)
    EnableFlag(Flags.LivingFailuresFirstTimeDone)


def EnterLivingFailuresFog():
    """ 13504850: Event 13504850 """
    EndIfFlagEnabled(Flags.LivingFailuresDead)
    GotoIfFlagEnabled(Label.L0, Flags.LivingFailuresFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.LivingFailuresFog)
    DeleteVFX(VFX.LivingFailuresFog, erase_root_only=False)
    IfFlagDisabled(1, Flags.LivingFailuresDead)
    IfFlagEnabled(1, Flags.LivingFailuresFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.LivingFailuresFog)
    CreateVFX(VFX.LivingFailuresFog)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.LivingFailuresDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=3500850, entity=Objects.LivingFailuresFog)
    IfFlagEnabled(3, Flags.LivingFailuresDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 3502810, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3502811)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.LivingFailuresFogEntered)
    Restart()


def EnterLivingFailuresFogAsSummon():
    """ 13504851: Event 13504851 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.LivingFailuresDead)
    IfFlagDisabled(1, Flags.LivingFailuresDead)
    IfFlagEnabled(1, Flags.LivingFailuresFirstTimeDone)
    IfFlagEnabled(1, Flags.LivingFailuresFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=3500850, entity=Objects.LivingFailuresFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3502810, animation=101130)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=3502811)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(13504859)
    Restart()


def StartLivingFailuresBattle():
    """ 13504852: Event 13504852 """
    EndIfFlagEnabled(Flags.LivingFailuresDead)
    DisableGravity(Characters.LivingFailuresHealthPool)
    DisableAI(Characters.LivingFailuresHealthPool)
    DisableAI(Characters.LivingFailure1)
    DisableAI(Characters.LivingFailure2)
    DisableAI(Characters.LivingFailure3)
    DisableAI(Characters.LivingFailure4)
    DisableAI(Characters.LivingFailureMeteorCreator)
    DisableHealthBar(Characters.LivingFailuresHealthPool)
    DisableHealthBar(Characters.LivingFailure1)
    DisableHealthBar(Characters.LivingFailure2)
    DisableHealthBar(Characters.LivingFailure3)
    DisableHealthBar(Characters.LivingFailure4)
    ReferDamageToEntity(Characters.LivingFailure1, Characters.LivingFailuresHealthPool)
    ReferDamageToEntity(Characters.LivingFailure2, Characters.LivingFailuresHealthPool)
    ReferDamageToEntity(Characters.LivingFailure3, Characters.LivingFailuresHealthPool)
    ReferDamageToEntity(Characters.LivingFailure4, Characters.LivingFailuresHealthPool)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.LivingFailuresFogEntered)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 13504860)
    NotifyBossBattleStart()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13504860)
    EnableFlag(Flags.LivingFailuresFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.LivingFailuresHealthPool, 7500, affect_npc_part_hp=False)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.LivingFailuresHealthPool)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.LivingFailuresHealthPool, 7501, affect_npc_part_hp=False)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.LivingFailuresHealthPool)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.LivingFailure1)
    EnableAI(Characters.LivingFailure2)
    EnableAI(Characters.LivingFailure3)
    EnableAI(Characters.LivingFailure4)
    EnableAI(Characters.LivingFailureMeteorCreator)
    SkipLinesIfClient(5)
    SetNetworkUpdateAuthority(Characters.LivingFailure1, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.LivingFailure2, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.LivingFailure3, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.LivingFailure4, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.LivingFailureMeteorCreator, UpdateAuthority.Forced)
    EnableBossHealthBar(Characters.LivingFailuresHealthPool, name=403000, slot=0)
    CreatePlayLog(136)
    StartPlayLogMeasurement(3500011, 158, overwrite=True)


def ControlLivingFailuresMusic():
    """ 13504853: Event 13504853 """
    DisableNetworkSync()
    DisableSoundEvent(3503812)
    DisableSoundEvent(3503813)
    DisableSoundEvent(3503814)
    EndIfFlagEnabled(Flags.LadyMariaDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagDisabled(1, Flags.LivingFailuresDead)
    IfFlagEnabled(1, Flags.LivingFailuresBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 13504859)
    IfCharacterInsideRegion(1, PLAYER, region=3502812)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(3503812)
    IfFlagEnabled(2, Flags.LivingFailuresPhaseTwo)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.LivingFailuresDead)
    IfFlagEnabled(2, Flags.LivingFailuresBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 13504859)
    IfCharacterInsideRegion(2, PLAYER, region=3502812)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(3503812)
    WaitFrames(0)
    EnableBossMusic(3503813)


def ControlLivingFailuresCamera():
    """ 13504854: Event 13504854 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.LivingFailuresDead)
    IfCharacterAlive(1, Characters.LivingFailuresHealthPool)
    IfEntityWithinDistance(-1, PLAYER, Characters.LivingFailure1, radius=8.0)
    IfEntityWithinDistance(-1, PLAYER, Characters.LivingFailure2, radius=8.0)
    IfEntityWithinDistance(-1, PLAYER, Characters.LivingFailure3, radius=8.0)
    IfEntityWithinDistance(-1, PLAYER, Characters.LivingFailure4, radius=8.0)
    IfConditionTrue(2, input_condition=1)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=1)
    IfCharacterDead(-3, Characters.LivingFailuresHealthPool)
    IfEntityBeyondDistance(3, PLAYER, Characters.LivingFailure1, radius=10.0)
    IfEntityBeyondDistance(3, PLAYER, Characters.LivingFailure2, radius=10.0)
    IfEntityBeyondDistance(3, PLAYER, Characters.LivingFailure3, radius=10.0)
    IfEntityBeyondDistance(3, PLAYER, Characters.LivingFailure4, radius=10.0)
    IfConditionTrue(-4, input_condition=-3)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(0, input_condition=-4)
    SetLockedCameraSlot(game_map=RESEARCH_HALL, camera_slot=0)
    Restart()


def StopLivingFailuresMusic():
    """ 13504855: Event 13504855 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.LivingFailuresDead)
    IfCharacterDead(0, Characters.LivingFailuresHealthPool)
    DisableBossMusic(3503812)
    DisableBossMusic(3503813)
    DisableBossMusic(-1)


def Event13504856():
    """ 13504856: Event 13504856 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.LivingFailuresFog, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event13504857():
    """ 13504857: Event 13504857 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.LivingFailuresFog, radius=6.0)
    IfEntityWithinDistance(1, PLAYER, Objects.LivingFailuresFog, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def LivingFailuresMeteorAttackRequest():
    """ 13504865: Event 13504865 """
    IfCharacterHasTAEEvent(-15, Characters.LivingFailure1, tae_event_id=50)
    IfCharacterHasTAEEvent(-15, Characters.LivingFailure2, tae_event_id=50)
    IfCharacterHasTAEEvent(-15, Characters.LivingFailure3, tae_event_id=50)
    IfCharacterHasTAEEvent(-15, Characters.LivingFailure4, tae_event_id=50)
    IfConditionTrue(15, input_condition=-15)
    IfCharacterHuman(15, PLAYER)
    IfConditionTrue(0, input_condition=15)
    EnableFlag(Flags.LivingFailuresPhaseTwo)
    IfCharacterHasTAEEvent(-1, Characters.LivingFailure1, tae_event_id=30)
    IfCharacterHasTAEEvent(-1, Characters.LivingFailure2, tae_event_id=30)
    IfCharacterHasTAEEvent(-1, Characters.LivingFailure3, tae_event_id=30)
    IfCharacterHasTAEEvent(-1, Characters.LivingFailure4, tae_event_id=30)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 8035, affect_npc_part_hp=False)
    CreateVFX(3503854)
    EnableFlag(Flags.LivingFailuresMeteorRequest)
    IfFlagDisabled(0, Flags.LivingFailuresMeteorRequest)

    # --- 0 --- #
    DefineLabel(0)
    DeleteVFX(3503854, erase_root_only=True)
    CancelSpecialEffect(PLAYER, 8035)
    Restart()


def LivingFailuresMeteorAttackRoll():
    """ 13504880: Event 13504880 """
    DisableNetworkSync()
    DeleteVFX(3503850, erase_root_only=False)
    DeleteVFX(3503851, erase_root_only=False)
    DeleteVFX(3503852, erase_root_only=False)
    DeleteVFX(3503853, erase_root_only=False)
    DeleteVFX(3503854, erase_root_only=False)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, Flags.LivingFailuresMeteorAttackAvailable)
    EnableRandomFlagInRange((13504873, 13504874))  # triggers magic orb from LF 2 or 3
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, Flags.LivingFailuresFirstMeteorAttackDone)
    EnableRandomFlagInRange((13504875, 13504878))  # 100% trigger meteor
    EnableFlag(Flags.LivingFailuresFirstMeteorAttackDone)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    EnableRandomFlagInRange((13504873, 13504878))  # 40% chance of meteor, 60% chance of magic orb from LF 2 or 3
    Goto(Label.L2)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagRangeAllDisabled(0, (13504873, 13504878))  # wait for request to be resolved
    WaitFrames(900)  # 30 seconds at 30 fps
    Restart()


def LivingFailuresMeteorAttackFinished():
    """ 13504881: Event 13504881 """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagRangeAnyEnabled(0, (13504873, 13504878))
    Wait(5.0)
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.LivingFailure1, 8069)  # summoning meteors
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.LivingFailure2, 8069)
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.LivingFailure3, 8069)
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.LivingFailure4, 8069)
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.LivingFailure1, 8070)  # meteors ongoing
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.LivingFailure2, 8070)
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.LivingFailure3, 8070)
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.LivingFailure4, 8070)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((13504873, 13504878))  # meteor request flag roll range
    ReplanAI(Characters.LivingFailure1)
    ReplanAI(Characters.LivingFailure2)
    ReplanAI(Characters.LivingFailure3)
    ReplanAI(Characters.LivingFailure4)
    Restart()


def LivingFailureMagicOrb(_, living_failure: int, trigger_flag: int):
    """ 13504885: Pretty sure this triggers the "spirit bomb" attack (used only by two of the Failures). """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, trigger_flag)
    AICommand(living_failure, command_id=110, slot=0)
    ReplanAI(living_failure)
    IfFlagDisabled(0, trigger_flag)
    AICommand(living_failure, command_id=-1, slot=0)
    ReplanAI(living_failure)
    Restart()


def LivingFailureMeteorSummon(_, living_failure: int):
    """ 13504890: Triggered when any flag between 4875 and 4878 is enabled. """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagRangeAnyEnabled(0, (13504875, 13504878))
    IfCharacterHasSpecialEffect(-1, living_failure, 52)  # parried
    IfCharacterHasSpecialEffect(-1, living_failure, 57)  # riposted
    SkipLinesIfConditionTrue(1, -1)
    ForceAnimation(living_failure, 3013)
    AICommand(living_failure, command_id=120, slot=0)
    ReplanAI(living_failure)
    IfFlagRangeAllDisabled(0, (13504875, 13504878))
    AICommand(living_failure, command_id=-1, slot=0)
    ReplanAI(living_failure)
    Restart()


def KillRemainingLivingFailure(_, living_failure: int):
    """ 13504895: Event 13504895 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.LivingFailuresDead)
    IfHealthEqual(0, Characters.LivingFailuresHealthPool, 0.0)
    Kill(living_failure, award_souls=True)


def LivingFailuresSpawnRequest():
    """ 13505655: Event 13505655 """
    DisableNetworkSync()
    GotoIfFlagEnabled(Label.L1, Flags.LivingFailuresDead)
    GotoIfThisEventFlagEnabled(Label.L0)

    # FIRST SPAWN (up to label 0)
    IfFlagEnabled(0, Flags.LivingFailuresBattleStarted)
    EnableFlag(Flags.ActiveLivingFailuresCountRequest)
    Wait(3.0)
    IfTimeElapsed(-1, 5.0)
    IfEventValueEqual(1, 13505690, bit_count=3, value=0)
    IfFlagDisabled(1, Flags.ActiveLivingFailuresCountRequest)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)  # continue after five seconds or when active LF count is 0
    GotoIfFlagEnabled(Label.L1, Flags.RemainingLivingFailuresKilled)
    EnableFlag(Flags.LivingFailureSpawnRequest)
    Wait(1.0)
    IfTimeElapsed(-3, 20.0)
    IfTimeElapsed(2, 10.0)
    IfEventValueEqual(2, 13505690, bit_count=3, value=1)
    IfFlagDisabled(2, Flags.ActiveLivingFailuresCountRequest)
    IfEventValueEqual(3, 13505690, bit_count=3, value=0)
    IfFlagDisabled(3, Flags.ActiveLivingFailuresCountRequest)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFlagEnabled(Label.L1, Flags.RemainingLivingFailuresKilled)
    EnableFlag(Flags.LivingFailureSpawnRequest)
    Wait(1.0)
    IfTimeElapsed(-5, 20.0)
    IfTimeElapsed(4, 10.0)
    IfEventValueEqual(4, 13505690, bit_count=3, value=2)
    IfFlagDisabled(4, Flags.ActiveLivingFailuresCountRequest)
    IfTimeElapsed(5, 5.0)
    IfEventValueEqual(5, 13505690, bit_count=3, value=1)
    IfFlagDisabled(5, Flags.ActiveLivingFailuresCountRequest)
    IfEventValueEqual(6, 13505690, bit_count=3, value=0)
    IfFlagDisabled(6, Flags.ActiveLivingFailuresCountRequest)
    IfConditionTrue(-5, input_condition=4)
    IfConditionTrue(-5, input_condition=5)
    IfConditionTrue(-5, input_condition=6)
    IfConditionTrue(0, input_condition=-5)
    GotoIfFlagEnabled(Label.L1, Flags.RemainingLivingFailuresKilled)
    EnableFlag(Flags.LivingFailureSpawnRequest)
    Wait(1.0)
    IfTimeElapsed(7, 15.0)
    IfEventValueEqual(7, 13505690, bit_count=3, value=3)
    IfFlagDisabled(7, Flags.ActiveLivingFailuresCountRequest)
    IfTimeElapsed(8, 10.0)
    IfEventValueEqual(8, 13505690, bit_count=3, value=2)
    IfFlagDisabled(8, Flags.ActiveLivingFailuresCountRequest)
    IfTimeElapsed(9, 5.0)
    IfEventValueEqual(9, 13505690, bit_count=3, value=1)
    IfFlagDisabled(9, Flags.ActiveLivingFailuresCountRequest)
    IfEventValueEqual(10, 13505690, bit_count=3, value=0)
    IfFlagDisabled(10, Flags.ActiveLivingFailuresCountRequest)
    IfConditionTrue(-7, input_condition=7)
    IfConditionTrue(-7, input_condition=8)
    IfConditionTrue(-7, input_condition=9)
    IfConditionTrue(-7, input_condition=10)
    IfConditionTrue(0, input_condition=-7)
    GotoIfFlagEnabled(Label.L1, Flags.RemainingLivingFailuresKilled)
    EnableFlag(Flags.LivingFailureSpawnRequest)

    # --- 0 --- #
    DefineLabel(0)
    Wait(1.0)
    IfTimeElapsed(12, 9.0)
    IfEventValueEqual(12, 13505690, bit_count=3, value=3)
    IfFlagDisabled(12, Flags.ActiveLivingFailuresCountRequest)
    IfTimeElapsed(13, 6.0)
    IfEventValueEqual(13, 13505690, bit_count=3, value=2)
    IfFlagDisabled(13, Flags.ActiveLivingFailuresCountRequest)
    IfTimeElapsed(14, 3.0)
    IfEventValueEqual(14, 13505690, bit_count=3, value=1)
    IfFlagDisabled(14, Flags.ActiveLivingFailuresCountRequest)
    IfEventValueEqual(15, 13505690, bit_count=3, value=0)
    IfFlagDisabled(15, Flags.ActiveLivingFailuresCountRequest)
    IfConditionTrue(-13, input_condition=12)  # wait 9 seconds to spawn 4th LF
    IfConditionTrue(-13, input_condition=13)  # wait 6 seconds to spawn 3rd LF
    IfConditionTrue(-13, input_condition=14)  # wait 3 seconds to spawn 2nd LF
    IfConditionTrue(-13, input_condition=15)  # wait 0 seconds to spawn 1st LF
    IfConditionTrue(0, input_condition=-13)
    GotoIfFlagEnabled(Label.L1, Flags.RemainingLivingFailuresKilled)
    EnableFlag(Flags.LivingFailureSpawnRequest)
    IfHealthLessThan(-15, Characters.LivingFailuresHealthPool, 0.6000000238418579)
    SkipLinesIfConditionFalse(1, -15)
    EnableFlag(Flags.LivingFailuresMeteorAttackAvailable)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    DisableSpawner(3503814)
    DisableSpawner(3503815)
    DisableSpawner(3503816)
    DisableSpawner(3503817)
    End()


def RequestActiveLivingFailureCountOnSpawnAndDeath(_, living_failure: int):
    """ 13505656: Requests a Living Failure recount every time this Living Failure spawns or dies. """
    DisableNetworkSync()
    IfCharacterAlive(1, living_failure)
    IfHasAIStatus(1, living_failure, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(Flags.ActiveLivingFailuresCountRequest)
    IfCharacterDead(0, living_failure)
    EnableFlag(Flags.ActiveLivingFailuresCountRequest)
    Restart()


def CountActiveLivingFailures():
    """ 13505661: Whenever the request flag is enabled, this counts the number of non-dead Living Failures that are
    in battle mode, stores the result in a three-bit integer at 13505690, then disables the request flag. """
    DisableNetworkSync()
    IfFlagEnabled(0, Flags.ActiveLivingFailuresCountRequest)
    ClearEventValue(13505690, bit_count=3)
    IfHasAIStatus(1, Characters.LivingFailure1, ai_status=AIStatusType.Battle)
    IfCharacterAlive(1, Characters.LivingFailure1)
    SkipLinesIfConditionFalse(1, 1)
    IncrementEventValue(13505690, bit_count=3, max_value=6)
    IfHasAIStatus(2, Characters.LivingFailure2, ai_status=AIStatusType.Battle)
    IfCharacterAlive(2, Characters.LivingFailure2)
    SkipLinesIfConditionFalse(1, 2)
    IncrementEventValue(13505690, bit_count=3, max_value=6)
    IfHasAIStatus(3, Characters.LivingFailure3, ai_status=AIStatusType.Battle)
    IfCharacterAlive(3, Characters.LivingFailure3)
    SkipLinesIfConditionFalse(1, 3)
    IncrementEventValue(13505690, bit_count=3, max_value=6)
    IfHasAIStatus(4, Characters.LivingFailure4, ai_status=AIStatusType.Battle)
    IfCharacterAlive(4, Characters.LivingFailure4)
    SkipLinesIfConditionFalse(1, 4)
    IncrementEventValue(13505690, bit_count=3, max_value=6)
    DisableFlag(Flags.ActiveLivingFailuresCountRequest)
    Wait(1.0)
    Restart()


def SpawnLivingFailure():
    """ 13505662: Event 13505662 """
    IfFlagEnabled(0, Flags.LivingFailureSpawnRequest)
    IfCharacterHuman(2, PLAYER)
    IfHasAIStatus(2, Characters.LivingFailure2, ai_status=AIStatusType.Battle)
    IfCharacterAlive(2, Characters.LivingFailure2)
    SkipLinesIfConditionTrue(2, 2)
    EnableSpawner(3503815)
    Goto(Label.L0)
    IfCharacterHuman(3, PLAYER)
    IfHasAIStatus(3, Characters.LivingFailure3, ai_status=AIStatusType.Battle)
    IfCharacterAlive(3, Characters.LivingFailure3)
    SkipLinesIfConditionTrue(2, 3)
    EnableSpawner(3503816)
    Goto(Label.L0)
    IfCharacterHuman(4, PLAYER)
    IfHasAIStatus(4, Characters.LivingFailure4, ai_status=AIStatusType.Battle)
    IfCharacterAlive(4, Characters.LivingFailure4)
    SkipLinesIfConditionTrue(2, 4)
    EnableSpawner(3503817)
    Goto(Label.L0)
    IfCharacterHuman(1, PLAYER)
    IfHasAIStatus(1, Characters.LivingFailure1, ai_status=AIStatusType.Battle)
    IfCharacterAlive(1, Characters.LivingFailure1)
    SkipLinesIfConditionTrue(2, 1)
    EnableSpawner(3503814)
    Goto(Label.L0)

    # --- 0 --- #
    DefineLabel(0)
    Wait(3.0)
    DisableSpawner(3503814)
    DisableSpawner(3503815)
    DisableSpawner(3503816)
    DisableSpawner(3503817)
    EnableFlag(Flags.ActiveLivingFailuresCountRequest)
    DisableFlag(Flags.LivingFailureSpawnRequest)
    Restart()


def Event13505670(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13505670: Event 13505670 """
    IfFlagEnabled(1, Flags.LivingFailuresMeteorRequest)
    IfCharacterAlive(1, arg_12_15)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(arg_8_11)
    ShootProjectile(owner_entity=arg_12_15, projectile_id=arg_0_3, model_point=200, behavior_id=arg_4_7, 
                    launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)
    WaitFrames(180)
    Restart()


def CommandLivingFailuresMeteorCreator():
    """ 13505680: Counts the number of Living Failures doing the summoning animation (effect 8070) and commands the
    meteor creator character to spawn an appropriate number of meteors. """
    DisableNetworkSync()
    IfCharacterHuman(15, PLAYER)
    IfFlagEnabled(15, Flags.LivingFailuresMeteorRequest)
    IfConditionTrue(0, input_condition=15)
    ClearEventValue(13505694, bit_count=3)
    IfCharacterHasSpecialEffect(-1, Characters.LivingFailure1, 8070)
    SkipLinesIfConditionFalse(1, -1)
    IncrementEventValue(13505694, bit_count=3, max_value=10)
    IfCharacterHasSpecialEffect(-2, Characters.LivingFailure2, 8070)
    SkipLinesIfConditionFalse(1, -2)
    IncrementEventValue(13505694, bit_count=3, max_value=10)
    IfCharacterHasSpecialEffect(-3, Characters.LivingFailure3, 8070)
    SkipLinesIfConditionFalse(1, -3)
    IncrementEventValue(13505694, bit_count=3, max_value=10)
    IfCharacterHasSpecialEffect(-4, Characters.LivingFailure4, 8070)
    SkipLinesIfConditionFalse(1, -4)
    IncrementEventValue(13505694, bit_count=3, max_value=10)
    IfEventValueEqual(1, 13505694, bit_count=3, value=1)
    SkipLinesIfConditionFalse(1, 1)
    AICommand(Characters.LivingFailureMeteorCreator, command_id=10, slot=0)
    IfEventValueEqual(2, 13505694, bit_count=3, value=2)
    SkipLinesIfConditionFalse(1, 2)
    AICommand(Characters.LivingFailureMeteorCreator, command_id=20, slot=0)
    IfEventValueEqual(3, 13505694, bit_count=3, value=3)
    SkipLinesIfConditionFalse(1, 3)
    AICommand(Characters.LivingFailureMeteorCreator, command_id=30, slot=0)
    IfEventValueEqual(4, 13505694, bit_count=3, value=4)
    SkipLinesIfConditionFalse(1, 4)
    AICommand(Characters.LivingFailureMeteorCreator, command_id=40, slot=0)
    ReplanAI(Characters.LivingFailureMeteorCreator)
    IfCharacterDoesNotHaveSpecialEffect(5, Characters.LivingFailure1, 8070)
    IfCharacterDoesNotHaveSpecialEffect(5, Characters.LivingFailure2, 8070)
    IfCharacterDoesNotHaveSpecialEffect(5, Characters.LivingFailure3, 8070)
    IfCharacterDoesNotHaveSpecialEffect(5, Characters.LivingFailure4, 8070)
    IfCharacterHasTAEEvent(-5, Characters.LivingFailure1, tae_event_id=40)
    IfCharacterHasTAEEvent(-5, Characters.LivingFailure2, tae_event_id=40)
    IfCharacterHasTAEEvent(-5, Characters.LivingFailure3, tae_event_id=40)
    IfCharacterHasTAEEvent(-5, Characters.LivingFailure4, tae_event_id=40)
    IfConditionTrue(-6, input_condition=5)
    IfConditionTrue(-6, input_condition=-5)
    IfConditionTrue(0, input_condition=-6)
    SkipLinesIfFinishedConditionTrue(1, 5)
    WaitFrames(600)  # 20 seconds at 30 fps
    AICommand(Characters.LivingFailureMeteorCreator, command_id=-1, slot=0)
    ReplanAI(Characters.LivingFailureMeteorCreator)
    ForceAnimation(Characters.LivingFailureMeteorCreator, 0)
    DisableFlag(Flags.LivingFailuresMeteorRequest)
    Restart()


def Event13501100():
    """ 13501100: Event 13501100 """
    SkipLinesIfFlagDisabled(3, 13504100)
    SetCollisionResState(3504100, state=False)
    SetCollisionResState(3504101, state=False)
    End()
    GotoIfFlagEnabled(Label.L0, 13501108)
    DisableFlag(13501106)
    DisableFlag(13501107)
    EndOfAnimation(3501100, 0)
    EndOfAnimation(3501104, 0)
    EndOfAnimation(3501108, 0)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    SetCollisionResState(3504101, state=False)
    DisableMapCollision(3504301)
    DisableMapCollision(3504302)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501106)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(13501107)
    EndOfAnimation(3501100, 0)
    EndOfAnimation(3501104, 0)
    EndOfAnimation(3501108, 0)
    EnableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    SetCollisionResState(3504101, state=False)
    DisableMapCollision(3504301)
    DisableMapCollision(3504302)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(13501107)
    EndOfAnimation(3501100, 2)
    EndOfAnimation(3501104, 2)
    EndOfAnimation(3501108, 2)
    DisableObjectActivation(3501101, obj_act_id=100)
    EnableObjectActivation(3501102, obj_act_id=100)
    EnableObjectActivation(3501103, obj_act_id=100)
    SetCollisionResState(3504100, state=False)
    DisableMapCollision(3504300)
    DisableMapCollision(3504301)


def Event13501101():
    """ 13501101: Event 13501101 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13501108)
    IfFlagEnabled(1, 13504100)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, 13501106)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(13501107)
    SkipLines(1)
    EnableFlag(13501107)
    IfCharacterHuman(3, PLAYER)
    IfFlagEnabled(3, 13501108)
    IfFlagDisabled(3, 13504100)
    IfConditionTrue(0, input_condition=3)
    Restart()


def Event13501102():
    """ 13501102: Event 13501102 """
    IfFlagEnabled(4, 13504100)
    IfFlagEnabled(4, 13501106)
    GotoIfConditionFalse(Label.L0, input_condition=4)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    EnableMapCollision(3504301)
    EnableMapCollision(3504302)
    SetCollisionResState(3504100, state=False)
    SetCollisionResState(3504101, state=True)
    DisableMapCollision(3504300)
    DisableMapCollision(3504301)
    EndOfAnimation(3501108, 1)
    EndOfAnimation(3501104, 1)
    EndOfAnimation(3501100, 1)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501108)
    IfFlagDisabled(1, 13504100)
    IfFlagDisabled(1, 13501106)
    IfCharacterInsideRegion(-1, PLAYER, region=3502102)
    IfCharacterInsideRegion(-1, PLAYER, region=3502103)
    IfObjectActivated(-1, obj_act_id=13504101)
    IfFlagChange(2, 13501107)
    IfFlagEnabled(2, 13501107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504100)
    EnableFlag(13501106)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    EnableMapCollision(3504301)
    EnableMapCollision(3504302)
    ForceAnimation(3501108, 1)
    ForceAnimation(3501104, 1)
    ForceAnimation(3501100, 1, wait_for_completion=True)
    SetCollisionResState(3504100, state=False)
    SetCollisionResState(3504101, state=True)
    DisableMapCollision(3504300)
    DisableMapCollision(3504301)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(3, region=3502101)
    IfAllPlayersOutsideRegion(3, region=3502102)
    IfConditionTrue(0, input_condition=3)
    Wait(1.0)
    DisableFlag(13504100)
    DisableObjectActivation(3501101, obj_act_id=100)
    EnableObjectActivation(3501102, obj_act_id=100)
    EnableObjectActivation(3501103, obj_act_id=100)
    Restart()


def Event13501103():
    """ 13501103: Event 13501103 """
    IfFlagEnabled(4, 13504100)
    IfFlagDisabled(4, 13501106)
    GotoIfConditionFalse(Label.L0, input_condition=4)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    EnableMapCollision(3504300)
    EnableMapCollision(3504301)
    SetCollisionResState(3504101, state=False)
    SetCollisionResState(3504100, state=True)
    DisableMapCollision(3504301)
    DisableMapCollision(3504302)
    EndOfAnimation(3501108, 3)
    EndOfAnimation(3501104, 3)
    EndOfAnimation(3501100, 3)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501108)
    IfFlagDisabled(1, 13504100)
    IfFlagEnabled(1, 13501106)
    IfCharacterInsideRegion(-1, PLAYER, region=3502101)
    IfObjectActivated(-1, obj_act_id=13504102)
    IfObjectActivated(-1, obj_act_id=13504103)
    IfFlagChange(2, 13501107)
    IfFlagDisabled(2, 13501107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504100)
    DisableFlag(13501106)
    DisableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    EnableMapCollision(3504300)
    EnableMapCollision(3504301)
    ForceAnimation(3501108, 3)
    ForceAnimation(3501104, 3)
    ForceAnimation(3501100, 3, wait_for_completion=True)
    SetCollisionResState(3504101, state=False)
    SetCollisionResState(3504100, state=True)
    DisableMapCollision(3504301)
    DisableMapCollision(3504302)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(3, region=3502102)
    IfAllPlayersOutsideRegion(3, region=3502103)
    IfConditionTrue(0, input_condition=3)
    Wait(1.0)
    DisableFlag(13504100)
    EnableObjectActivation(3501101, obj_act_id=100)
    DisableObjectActivation(3501102, obj_act_id=100)
    DisableObjectActivation(3501103, obj_act_id=100)
    Restart()


def Event13501104():
    """ 13501104: Event 13501104 """
    DisableNetworkSync()
    IfFlagDisabled(1, 13501108)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=3501101)
    IfFlagDisabled(2, 13501108)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=3501102)
    IfFlagDisabled(3, 13501108)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=3501103)
    IfFlagEnabled(4, 13504100)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=3501101)
    IfFlagEnabled(5, 13504100)
    IfActionButtonParamActivated(5, action_button_id=7100, entity=3501102)
    IfFlagEnabled(6, 13504100)
    IfActionButtonParamActivated(6, action_button_id=7100, entity=3501103)
    IfFlagEnabled(7, 13501106)
    IfActionButtonParamActivated(7, action_button_id=7100, entity=3501101)
    IfFlagDisabled(8, 13501106)
    IfActionButtonParamActivated(8, action_button_id=7100, entity=3501102)
    IfFlagDisabled(9, 13501106)
    IfActionButtonParamActivated(9, action_button_id=7100, entity=3501103)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Restart()


def Event13501105():
    """ 13501105: Event 13501105 """
    EndIfFlagEnabled(13501108)
    IfPlayerHasGood(1, 4017, including_box=False)
    IfActionButtonParamActivated(1, action_button_id=3500101, entity=3501100)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(35000000, skippable=True, fade_out=False, player_id=PLAYER, move_to_region=3502104, 
                 move_to_map=RESEARCH_HALL)
    Goto(Label.L0)
    IfCharacterHuman(2, PLAYER)
    SkipLinesIfConditionFalse(2, 2)
    PlayCutscene(35000000, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=3502104, 
                 move_to_map=RESEARCH_HALL)
    Goto(Label.L0)
    IfCharacterInsideRegion(3, PLAYER, region=3502102)
    SkipLinesIfConditionTrue(2, 3)
    PlayCutscene(35000000, skippable=False, fade_out=False, player_id=PLAYER)
    Goto(Label.L0)
    EnableRandomFlagInRange((13505830, 13505833))
    SkipLinesIfFlagDisabled(2, 13505830)
    PlayCutscene(35000000, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=3502124, 
                 move_to_map=RESEARCH_HALL)
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(2, 13505831)
    PlayCutscene(35000000, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=3502125, 
                 move_to_map=RESEARCH_HALL)
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(2, 13505832)
    PlayCutscene(35000000, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=3502126, 
                 move_to_map=RESEARCH_HALL)
    Goto(Label.L0)
    SkipLinesIfFlagDisabled(2, 13505833)
    PlayCutscene(35000000, skippable=False, fade_out=False, player_id=PLAYER, move_to_region=3502127, 
                 move_to_map=RESEARCH_HALL)
    Goto(Label.L0)

    # --- 0 --- #
    DefineLabel(0)
    WaitFrames(1)
    DisableFlag(9180)
    EndOfAnimation(3501100, 2)
    EndOfAnimation(3501104, 2)
    EndOfAnimation(3501108, 2)
    EnableFlag(13501106)
    EnableFlag(13501107)
    DisableObjectActivation(3501101, obj_act_id=100)
    EnableObjectActivation(3501102, obj_act_id=100)
    SetCollisionResState(3504100, state=False)
    SetCollisionResState(3504101, state=True)
    DisableMapCollision(3504300)
    EnableMapCollision(3504302)
    EnableFlag(13501108)
    Event13501101()
    Event13501102()
    Event13501103()
    RestartEvent(13501104)


def Event13501140():
    """ 13501140: Event 13501140 """
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerDoesNotHaveGood(1, 4017, including_box=False)
    IfFlagDisabled(1, 13501105)
    IfActionButtonParamActivated(1, action_button_id=3500100, entity=3501100)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010601, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Restart()


def Event13501141():
    """ 13501141: Event 13501141 """
    GotoIfFlagEnabled(Label.L0, 53502000)
    IfCharacterHuman(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=3500102, entity=3501104)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(3502000, host_only=False)
    EnableFlag(13401852)
    DisableFlag(3400)
    DisableFlag(3401)
    EnableFlag(3402)
    DisableFlag(3403)

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(3501104)


def Event13501142():
    """ 13501142: Event 13501142 """
    GotoIfFlagEnabled(Label.L0, 53502000)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    CreateObjectVFX(900201, obj=3501104, model_point=200)
    IfFlagEnabled(0, 53502000)

    # --- 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(3501104, erase_root=True)


def Event13501110():
    """ 13501110: Event 13501110 """
    EndIfFlagEnabled(13504110)
    GotoIfFlagEnabled(Label.L0, 13501118)
    EnableFlag(13501116)
    EnableFlag(13501117)
    EndOfAnimation(3501105, 0)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501116)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(13501117)
    EndOfAnimation(3501105, 4)
    EnableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(13501117)
    EndOfAnimation(3501105, 0)
    DisableObjectActivation(3501106, obj_act_id=100)
    EnableObjectActivation(3501107, obj_act_id=100)


def Event13501111():
    """ 13501111: Event 13501111 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13501118)
    IfFlagEnabled(1, 13504110)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, 13501116)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(13501117)
    SkipLines(1)
    EnableFlag(13501117)
    IfCharacterHuman(3, PLAYER)
    IfFlagEnabled(3, 13501118)
    IfFlagDisabled(3, 13504110)
    IfConditionTrue(0, input_condition=3)
    Restart()


def Event13501112():
    """ 13501112: Event 13501112 """
    IfFlagEnabled(3, 13504110)
    IfFlagEnabled(3, 13501116)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    EndOfAnimation(3501105, 6)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501118)
    IfFlagDisabled(1, 13504110)
    IfFlagDisabled(1, 13501116)
    IfCharacterInsideRegion(-1, PLAYER, region=3502107)
    IfObjectActivated(-1, obj_act_id=13504111)
    IfFlagChange(2, 13501117)
    IfFlagEnabled(2, 13501117)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504110)
    EnableFlag(13501116)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    ForceAnimation(3501105, 5, wait_for_completion=True)
    ForceAnimation(3501105, 6, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3502106)
    DisableFlag(13504110)
    ForceAnimation(3501105, 7, wait_for_completion=True)
    DisableObjectActivation(3501106, obj_act_id=100)
    EnableObjectActivation(3501107, obj_act_id=100)
    Restart()


def Event13501113():
    """ 13501113: Event 13501113 """
    IfFlagEnabled(3, 13504110)
    IfFlagDisabled(3, 13501116)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    EndOfAnimation(3501105, 2)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501118)
    IfFlagDisabled(1, 13504110)
    IfFlagEnabled(1, 13501116)
    IfCharacterInsideRegion(-1, PLAYER, region=3502106)
    IfObjectActivated(-1, obj_act_id=13504112)
    IfFlagChange(2, 13501117)
    IfFlagDisabled(2, 13501117)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504110)
    DisableFlag(13501116)
    DisableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    ForceAnimation(3501105, 1, wait_for_completion=True)
    ForceAnimation(3501105, 2, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3502107)
    DisableFlag(13504110)
    ForceAnimation(3501105, 3, wait_for_completion=True)
    EnableObjectActivation(3501106, obj_act_id=100)
    DisableObjectActivation(3501107, obj_act_id=100)
    Restart()


def Event13501114():
    """ 13501114: Event 13501114 """
    DisableNetworkSync()
    IfFlagDisabled(1, 13501118)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=3501106)
    IfFlagDisabled(2, 13501118)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=3501107)
    IfFlagEnabled(3, 13504110)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=3501106)
    IfFlagEnabled(4, 13504110)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=3501107)
    IfFlagEnabled(5, 13501116)
    IfActionButtonParamActivated(5, action_button_id=7100, entity=3501106)
    IfFlagDisabled(6, 13501116)
    IfActionButtonParamActivated(6, action_button_id=7100, entity=3501107)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Restart()


def Event13501115():
    """ 13501115: Event 13501115 """
    EndIfFlagEnabled(13501118)
    IfCharacterInsideRegion(0, PLAYER, region=3502105)
    DisableObjectActivation(3501106, obj_act_id=100)
    EnableObjectActivation(3501107, obj_act_id=100)
    EnableFlag(13501118)


def Event13501120():
    """ 13501120: Event 13501120 """
    EndIfFlagEnabled(13504120)
    GotoIfFlagEnabled(Label.L0, 13501128)
    EnableFlag(13501126)
    EnableFlag(13501127)
    EndOfAnimation(3501110, 0)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501126)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(13501127)
    EndOfAnimation(3501110, 4)
    EnableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(13501127)
    EndOfAnimation(3501110, 0)
    DisableObjectActivation(3501111, obj_act_id=100)
    EnableObjectActivation(3501112, obj_act_id=100)


def Event13501121():
    """ 13501121: Event 13501121 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13501128)
    IfFlagEnabled(1, 13504120)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, 13501126)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(13501127)
    SkipLines(1)
    EnableFlag(13501127)
    IfCharacterHuman(3, PLAYER)
    IfFlagEnabled(3, 13501128)
    IfFlagDisabled(3, 13504120)
    IfConditionTrue(0, input_condition=3)
    Restart()


def Event13501122():
    """ 13501122: Event 13501122 """
    IfFlagEnabled(3, 13504120)
    IfFlagEnabled(3, 13501126)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    EndOfAnimation(3501110, 6)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501128)
    IfFlagDisabled(1, 13504120)
    IfFlagDisabled(1, 13501126)
    IfCharacterInsideRegion(-1, PLAYER, region=3502112)
    IfObjectActivated(-1, obj_act_id=13504121)
    IfFlagChange(2, 13501127)
    IfFlagEnabled(2, 13501127)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504120)
    EnableFlag(13501126)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    ForceAnimation(3501110, 5, wait_for_completion=True)
    ForceAnimation(3501110, 6, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3502111)
    DisableFlag(13504120)
    ForceAnimation(3501110, 7, wait_for_completion=True)
    DisableObjectActivation(3501111, obj_act_id=100)
    EnableObjectActivation(3501112, obj_act_id=100)
    Restart()


def Event13501123():
    """ 13501123: Event 13501123 """
    IfFlagEnabled(3, 13504120)
    IfFlagDisabled(3, 13501126)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    EndOfAnimation(3501110, 2)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13501128)
    IfFlagDisabled(1, 13504120)
    IfFlagEnabled(1, 13501126)
    IfCharacterInsideRegion(-1, PLAYER, region=3502111)
    IfObjectActivated(-1, obj_act_id=13504122)
    IfFlagChange(2, 13501127)
    IfFlagDisabled(2, 13501127)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13504120)
    DisableFlag(13501126)
    DisableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    ForceAnimation(3501110, 1, wait_for_completion=True)
    ForceAnimation(3501110, 2, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3502112)
    DisableFlag(13504120)
    ForceAnimation(3501110, 3, wait_for_completion=True)
    EnableObjectActivation(3501111, obj_act_id=100)
    DisableObjectActivation(3501112, obj_act_id=100)
    Restart()


def Event13501124():
    """ 13501124: Event 13501124 """
    DisableNetworkSync()
    IfFlagDisabled(1, 13501128)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=3501111)
    IfFlagDisabled(2, 13501128)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=3501112)
    IfFlagEnabled(3, 13504120)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=3501111)
    IfFlagEnabled(4, 13504120)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=3501112)
    IfFlagEnabled(5, 13501126)
    IfActionButtonParamActivated(5, action_button_id=7100, entity=3501111)
    IfFlagDisabled(6, 13501126)
    IfActionButtonParamActivated(6, action_button_id=7100, entity=3501112)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Restart()


def Event13501125():
    """ 13501125: Event 13501125 """
    EndIfFlagEnabled(13501128)
    IfCharacterInsideRegion(-1, PLAYER, region=3502110)
    IfFlagEnabled(-1, 13500100)
    IfConditionTrue(0, input_condition=-1)
    DisableObjectActivation(3501111, obj_act_id=100)
    EnableObjectActivation(3501112, obj_act_id=100)
    EnableFlag(13501128)


def Event13501200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13501200: Event 13501200 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_20_23)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(-1, obj_act_id=arg_4_7)
    IfObjectActivated(-1, obj_act_id=arg_16_19)
    IfConditionTrue(0, input_condition=-1)
    Wait(1.0)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_20_23)


def Event13501250():
    """ 13501250: Event 13501250 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(3501160, 1)
    DisableObjectActivation(3501160, obj_act_id=3500062)
    DisableObjectActivation(3501160, obj_act_id=3500061)
    NotifyDoorEventSoundDampening(3501160, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(1, obj_act_id=13504269)
    IfFlagEnabled(2, 13500100)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=2)

    # --- 1 --- #
    DefineLabel(1)
    Wait(1.0)
    DisableObjectActivation(3501160, obj_act_id=3500062)
    DisableObjectActivation(3501160, obj_act_id=3500061)
    End()

    # --- 2 --- #
    DefineLabel(2)
    ForceAnimation(3501160, 1)
    DisableObjectActivation(3501160, obj_act_id=3500062)
    DisableObjectActivation(3501160, obj_act_id=3500061)
    NotifyDoorEventSoundDampening(3501160, state=DoorState.DoorOpening)
    End()


def Event13501400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13501400: Event 13501400 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event13504799():
    """ 13504799: Event 13504799 """
    CreateProjectileOwner(3500799)


def Event13500100():
    """ 13500100: Event 13500100 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableObjectActivation(3501210, obj_act_id=3500110)
    EndOfAnimation(3501210, 3)
    EndOfAnimation(3501211, 2)
    EndOfAnimation(3501212, 2)
    EndOfAnimation(3501220, 2)
    EndOfAnimation(3501221, 2)
    EndOfAnimation(3501231, 2)
    EndOfAnimation(3501232, 2)
    EndOfAnimation(3501233, 2)
    EndOfAnimation(3501234, 2)
    EndOfAnimation(3501235, 2)
    SetCollisionResState(3504200, state=False)
    SetCollisionResState(3504201, state=False)
    SetCollisionResState(3504202, state=False)
    SetCollisionResState(3504203, state=False)
    SetCollisionResState(3504204, state=False)
    SetCollisionResState(3504210, state=False)
    SetCollisionResState(3504211, state=False)
    SetCollisionResState(3504212, state=False)
    SetCollisionResState(3504213, state=False)
    SetCollisionResState(3504214, state=False)
    DisableMapCollision(3504210)
    DisableMapCollision(3504211)
    DisableMapCollision(3504212)
    DisableMapCollision(3504213)
    DisableMapCollision(3504214)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetCollisionResState(3504205, state=False)
    SetCollisionResState(3504206, state=False)
    SetCollisionResState(3504207, state=False)
    SetCollisionResState(3504208, state=False)
    SetCollisionResState(3504209, state=False)
    SetCollisionResState(3504215, state=False)
    SetCollisionResState(3504216, state=False)
    SetCollisionResState(3504217, state=False)
    SetCollisionResState(3504218, state=False)
    SetCollisionResState(3504219, state=False)
    DisableMapCollision(3504215)
    DisableMapCollision(3504216)
    DisableMapCollision(3504217)
    DisableMapCollision(3504218)
    DisableMapCollision(3504219)
    IfObjectActivated(0, obj_act_id=13504280)
    EnableFlag(13505500)
    ForceAnimation(3501210, 2)
    ForceAnimation(3501211, 1)
    ForceAnimation(3501212, 1)
    ForceAnimation(3501220, 1)
    ForceAnimation(3501221, 1)
    ForceAnimation(3501231, 1)
    ForceAnimation(3501232, 1)
    ForceAnimation(3501233, 1)
    ForceAnimation(3501234, 1)
    ForceAnimation(3501235, 1, wait_for_completion=True)
    SetCollisionResState(3504200, state=False)
    SetCollisionResState(3504201, state=False)
    SetCollisionResState(3504202, state=False)
    SetCollisionResState(3504203, state=False)
    SetCollisionResState(3504204, state=False)
    SetCollisionResState(3504210, state=False)
    SetCollisionResState(3504211, state=False)
    SetCollisionResState(3504212, state=False)
    SetCollisionResState(3504213, state=False)
    SetCollisionResState(3504214, state=False)
    DisableMapCollision(3504210)
    DisableMapCollision(3504211)
    DisableMapCollision(3504212)
    DisableMapCollision(3504213)
    DisableMapCollision(3504214)
    SetCollisionResState(3504205, state=True)
    SetCollisionResState(3504206, state=True)
    SetCollisionResState(3504207, state=True)
    SetCollisionResState(3504208, state=True)
    SetCollisionResState(3504209, state=True)
    EnableMapCollision(3504215)
    EnableMapCollision(3504216)
    EnableMapCollision(3504217)
    EnableMapCollision(3504218)
    EnableMapCollision(3504219)
    DisableFlag(13505500)
    End()


def Event13500105():
    """ 13500105: Event 13500105 """
    DisableSoundEvent(3503202)
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(1, 3504020)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.a_Ambient, sound_id=350000010)


def Event13500106():
    """ 13500106: Event 13500106 """
    DisableSoundEvent(3503203)
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(1, 3504815)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.a_Ambient, sound_id=350000011)


@RestartOnRest
def Event13500110():
    """ 13500110: Event 13500110 """
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableObject(3501751)
    IfFlagEnabled(0, 9469)
    EnableObject(3501751)

    # --- 0 --- #
    DefineLabel(0)
    DisableMapPiece(3501750)
    End()


@RestartOnRest
def Event13500111():
    """ 13500111: Event 13500111 """
    DisableNetworkSync()
    GotoIfThisEventFlagDisabled(Label.L0)
    DeleteVFX(3503120, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfEntityWithinDistance(0, PLAYER, 3502120, radius=7.0)
    DeleteVFX(3503120, erase_root_only=True)


@RestartOnRest
def Event13500120():
    """ 13500120: Event 13500120 """
    GotoIfFlagDisabled(Label.L0, 53500840)
    EndOfAnimation(3501280, 2)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3501280, 0, loop=True)
    IfFlagEnabled(0, 53500840)
    ForceAnimation(3501280, 1, wait_for_completion=True)
    End()


@RestartOnRest
def Event13500130():
    """ 13500130: Event 13500130 """
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, 13500101)
    Move(3500552, destination=3502420, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(3500552, 9008, loop=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3500552, 9008, loop=True)
    IfFlagEnabled(0, 13500100)
    ForceAnimation(3500552, 2004)
    ChangePatrolBehavior(3500552, patrol_information_id=3503320)
    ReplanAI(3500552)
    IfCharacterInsideRegion(0, 3500552, region=3502420)
    ForceAnimation(3500552, 9008, loop=True)


@RestartOnRest
def Event13500140():
    """ 13500140: Event 13500140 """
    IfHasAIStatus(0, 3500764, ai_status=AIStatusType.Battle)
    ForceAnimation(3500764, 3010, loop=True)
    IfHasAIStatus(-1, 3500764, ai_status=AIStatusType.Normal)
    IfHasAIStatus(-1, 3500764, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 3500764, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(3500764, 0, loop=True)
    Restart()


@RestartOnRest
def Event13500150():
    """ 13500150: Event 13500150 """
    ForceAnimation(3500932, 103020, loop=True)
    AddSpecialEffect(3500932, 8015, affect_npc_part_hp=False)
    DisableAI(3500932)
    DisableAI(3500931)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3502308)
    IfEntityWithinDistance(-2, PLAYER, 3500932, radius=5.0)
    IfAttackedWithDamageType(-2, attacked_entity=3500932, attacker=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=3502328)
    IfEntityWithinDistance(-3, PLAYER, 3500931, radius=2.0)
    IfAttackedWithDamageType(-3, attacked_entity=3500931, attacker=-1)
    IfConditionTrue(4, input_condition=-3)
    IfConditionTrue(-4, input_condition=1)
    IfConditionTrue(-4, input_condition=2)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(-4, input_condition=4)
    IfConditionTrue(0, input_condition=-4)
    ForceAnimation(3500932, 103023)
    EnableAI(3500932)
    IfFramesElapsed(0, 40)
    EnableAI(3500931)


@RestartOnRest
def Event13500400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500400: Event 13500400 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    Kill(arg_0_3, award_souls=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfConditionTrue(0, input_condition=1)

    # --- 1 --- #
    DefineLabel(1)
    EnableCharacter(arg_0_3)


@RestartOnRest
def Event13500410(_, arg_0_3: int, arg_4_7: int):
    """ 13500410: Event 13500410 """
    GotoIfFlagEnabled(Label.L0, 13500101)
    DisableBackread(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(arg_0_3)
    End()


@RestartOnRest
def Event13500418(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500418: Event 13500418 """
    GotoIfFlagEnabled(Label.L0, 13500101)
    DisableAI(arg_4_7)
    EnableGravity(arg_4_7)
    DisableHealthBar(arg_4_7)
    EnableImmortality(arg_4_7)
    ReferDamageToEntity(arg_0_3, arg_4_7)
    IfFlagEnabled(1, 13500100)
    IfCharacterAlive(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_0_3)
    EnableAI(arg_4_7)
    DisableGravity(arg_4_7)
    EnableHealthBar(arg_4_7)
    DisableImmortality(arg_4_7)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Region, set_draw_parent=0)
    ReplanAI(arg_4_7)
    End()


@RestartOnRest
def Event13500420(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500420: Event 13500420 """
    EndIfFlagEnabled(13500101)
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=13504280)
    WaitFrames(arg_8_11)
    ForceAnimation(arg_0_3, arg_4_7)


@RestartOnRest
def Event13500430(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500430: Event 13500430 """
    EndIfFlagEnabled(arg_0_3)
    IfAttackedWithDamageType(1, attacked_entity=arg_4_7, attacker=-1)
    IfConditionTrue(-1, input_condition=1)
    IfHasAIStatus(-1, arg_4_7, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_4_7, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_4_7, ai_status=AIStatusType.Battle)
    IfConditionTrue(2, input_condition=-1)
    IfFlagEnabled(2, arg_0_3)
    IfConditionTrue(0, input_condition=2)
    EndIfFinishedConditionTrue(1)
    ForceAnimation(arg_4_7, arg_8_11)


@RestartOnRest
def Event13500450(_, arg_0_3: int, arg_4_7: int):
    """ 13500450: Event 13500450 """
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
def Event13500460(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500460: Event 13500460 """
    GotoIfFlagEnabled(Label.L0, arg_8_11)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=-1)
    Kill(arg_0_3, award_souls=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetDistanceLimitForConversationStateChanges(arg_0_3, distance=1.0)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)


def Event13500500(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500500: Event 13500500 """
    DisableNetworkSync()
    IfActionButtonParamActivated(0, action_button_id=arg_4_7, entity=arg_0_3)
    DisplayDialog(arg_8_11, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest
def Event13505050(_, arg_0_3: int):
    """ 13505050: Event 13505050 """
    AddSpecialEffect(arg_0_3, 5410, affect_npc_part_hp=False)
    SetAIParamID(arg_0_3, 402040)
    ReplanAI(arg_0_3)
    IfObjectDestroyed(-1, 3501700)
    IfObjectDestroyed(-1, 3501701)
    IfObjectDestroyed(-1, 3501702)
    IfObjectDestroyed(-1, 3501703)
    IfObjectDestroyed(-1, 3501704)
    IfObjectDestroyed(-1, 3501705)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(0, input_condition=-3)
    CancelSpecialEffect(arg_0_3, 5410)
    SetCharacterEventTarget(arg_0_3, 10000)
    SetAIParamID(arg_0_3, 402005)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13505060():
    """ 13505060: Event 13505060 """
    IfCharacterTargeting(-1, 3500750, PLAYER)
    IfCharacterTargeting(-1, 3500760, PLAYER)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(3500750, 270352)
    SetAIParamID(3500760, 262912)


@RestartOnRest
def Event13505100(_, arg_0_3: int):
    """ 13505100: Event 13505100 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(arg_0_3, 8014, affect_npc_part_hp=False)

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Normal)
    IfCharacterDead(-2, arg_0_3)
    IfCharacterBackreadDisabled(-2, arg_0_3)
    IfConditionTrue(0, input_condition=-2)
    CancelSpecialEffect(arg_0_3, 8014)
    Restart()


@RestartOnRest
def Event13505110(_, arg_0_3: int, arg_4_7: int):
    """ 13505110: Event 13505110 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    EnableInvincibility(arg_0_3)
    DisableAI(arg_0_3)
    DisableHealthBar(arg_0_3)
    DisableAnimations(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    DisableInvincibility(arg_0_3)
    EnableAI(arg_0_3)
    EnableHealthBar(arg_0_3)
    EnableAnimations(arg_0_3)


@RestartOnRest
def Event13505200(_, arg_0_3: int, arg_4_7: int):
    """ 13505200: Event 13505200 """
    IfFlagEnabled(0, 13500100)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_4_7)
    ReplanAI(arg_0_3)


def Event13505300(_, arg_0_3: int):
    """ 13505300: Event 13505300 """
    EndIfFlagEnabled(13500101)
    IfFlagEnabled(1, 13505500)
    IfCharacterInsideRegion(1, arg_0_3, region=3502390)
    IfConditionTrue(0, input_condition=1)
    SetBackreadStateAlternate(arg_0_3, state=True)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    IfFlagDisabled(0, 13505500)
    EnableAI(arg_0_3)
    SetBackreadStateAlternate(arg_0_3, state=False)
    SetNetworkUpdateRate(arg_0_3, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    ReplanAI(arg_0_3)
    End()


@RestartOnRest
def Event13505400(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 13505400: Event 13505400 """
    IfThisEventSlotFlagDisabled(5)
    IfCharacterAlive(5, arg_0_3)
    GotoIfConditionTrue(Label.L0, input_condition=5)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacterCollision(arg_0_3)
    DisableGravity(arg_0_3)
    ForceAnimation(arg_0_3, 9000, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(arg_0_3, 9060, wait_for_completion=True)
    EnableGravity(arg_0_3)
    WaitFrames(15)
    EnableCharacterCollision(arg_0_3)


@RestartOnRest
def Event13505410():
    """ 13505410: Event 13505410 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3502342)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    SetTeamType(3500764, TeamType.Enemy2)
    Wait(1.0)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-3)
    IfCharacterInsideRegion(2, PLAYER, region=3502342)
    IfConditionTrue(-4, input_condition=2)
    IfConditionFalse(0, input_condition=-4)
    SetTeamType(3500764, TeamType.Enemy1)
    Restart()


@RestartOnRest
def Event13505450(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 13505450: Event 13505450 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EnableAI(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(arg_0_3, arg_12_15)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13505470(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13505470: Event 13505470 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, arg_4_7)
    SetAIParamID(arg_0_3, 402040)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-1, input_condition=1)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(arg_0_3, arg_8_11)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_12_15)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13505510(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 13505510: Event 13505510 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    Wait(arg_12_15)
    EnableAI(arg_0_3)


@RestartOnRest
def Event13505570(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int):
    """ 13505570: Event 13505570 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    Wait(arg_12_15)
    EnableAI(arg_0_3)
    IfCharacterInsideRegion(4, arg_0_3, region=arg_16_19)
    IfHasAIStatus(4, arg_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=4)
    DisableAI(arg_0_3)
    IfCharacterHuman(-5, PLAYER)
    IfCharacterType(-5, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(5, input_condition=-5)
    IfCharacterInsideRegion(5, PLAYER, region=arg_20_23)
    IfEntityWithinDistance(-6, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-6, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-7, input_condition=5)
    IfConditionTrue(-7, input_condition=-6)
    IfConditionTrue(0, input_condition=-7)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_24_27)
    EnableAI(arg_0_3)


@RestartOnRest
def Event13505580(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 13505580: Event 13505580 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfFlagEnabled(0, 13500100)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(arg_0_3, 0)
    EnableAI(arg_0_3)


@RestartOnRest
def Event13505590(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: int, arg_20_23: float, 
                  arg_24_27: float, arg_28_31: int):
    """ 13505590: Event 13505590 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, arg_12_15)
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=arg_28_31)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    Wait(arg_20_23)
    ForceAnimation(arg_0_3, arg_16_19)
    Wait(arg_24_27)
    EnableAI(arg_0_3)


@RestartOnRest
def Event13505610(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: int, arg_20_23: float, 
                  arg_24_27: float):
    """ 13505610: Event 13505610 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, arg_12_15)
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    IfFlagEnabled(0, 53500820)
    IfTimeElapsed(0, arg_20_23)
    ForceAnimation(arg_0_3, arg_16_19)
    IfTimeElapsed(0, arg_24_27)
    EnableAI(arg_0_3)


@RestartOnRest
def Event13505630(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 13505630: Event 13505630 """
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(arg_0_3)
    EndIfFlagEnabled(13500101)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_8_11)
    EndIfFlagEnabled(13500100)
    EnableCharacter(arg_0_3)
    EnableInvincibility(arg_0_3)
    Wait(arg_12_15)
    DisableInvincibility(arg_0_3)


@RestartOnRest
def Event13505640(_, arg_0_3: int, arg_4_7: int):
    """ 13505640: Event 13505640 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    AddSpecialEffect(arg_0_3, 5300, affect_npc_part_hp=False)


@RestartOnRest
def Event13505650(_, arg_0_3: int):
    """ 13505650: Event 13505650 """
    AddSpecialEffect(arg_0_3, 5410, affect_npc_part_hp=False)
    IfHasAIStatus(-1, 0, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 0, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, 0, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(arg_0_3, 5410)


@RestartOnRest
def Event13505700(_, arg_0_3: int, arg_4_7: int):
    """ 13505700: Event 13505700 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    SetAIParamID(arg_0_3, 402011)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13505740(_, arg_0_3: int):
    """ 13505740: Event 13505740 """
    Kill(arg_0_3, award_souls=False)


@RestartOnRest
def Event13505750(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float, arg_20_23: int):
    """ 13505750: Event 13505750 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_16_19)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfValueEqual(1, left=arg_20_23, right=0)
    AddSpecialEffect(arg_0_3, 5000, affect_npc_part_hp=False)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_12_15)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13505780(_, arg_0_3: int):
    """ 13505780: Event 13505780 """
    EndIfFlagEnabled(13500100)
    DisableCharacter(arg_0_3)
    IfFlagEnabled(0, 13500100)
    EnableCharacter(arg_0_3)


@RestartOnRest
def Event13505797(_, arg_0_3: int):
    """ 13505797: Event 13505797 """
    EndIfFlagEnabled(13500100)
    DisableObject(arg_0_3)
    DisableTreasure(arg_0_3)
    IfFlagEnabled(0, 13500100)
    EnableObject(arg_0_3)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event13505800(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13505800: Event 13505800 """
    RestoreObject(arg_8_11)
    ForceAnimation(arg_4_7, 2)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    WaitFrames(25)
    DestroyObject(arg_8_11)
    SkipLinesIfFlagEnabled(2, 6603)
    ShootProjectile(owner_entity=3500799, projectile_id=arg_12_15, model_point=200, behavior_id=6350, launch_angle_x=0, 
                    launch_angle_y=0, launch_angle_z=0)
    Goto(Label.L1)
    ShootProjectile(owner_entity=3500799, projectile_id=arg_12_15, model_point=200, behavior_id=6352, launch_angle_x=0, 
                    launch_angle_y=0, launch_angle_z=0)

    # --- 1 --- #
    DefineLabel(1)
    SetCharacterEventTarget(arg_16_19, 10000)
    ReplanAI(arg_16_19)


@RestartOnRest
def Event13505810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13505810: Event 13505810 """
    RestoreObject(arg_8_11)
    ForceAnimation(arg_4_7, 2)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    WaitFrames(25)
    ShootProjectile(owner_entity=3500799, projectile_id=arg_12_15, model_point=200, behavior_id=6350, launch_angle_x=0, 
                    launch_angle_y=0, launch_angle_z=0)
    WaitFrames(20)
    ShootProjectile(owner_entity=3500799, projectile_id=arg_16_19, model_point=200, behavior_id=6350, launch_angle_x=0, 
                    launch_angle_y=0, launch_angle_z=0)
    SetCharacterEventTarget(arg_20_23, 10000)
    ReplanAI(arg_20_23)


@RestartOnRest
def Event13505820(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13505820: Event 13505820 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfCharacterInsideRegion(-1, PLAYER, region=3502322)
    IfCharacterInsideRegion(-1, PLAYER, region=3502323)
    IfCharacterInsideRegion(-1, PLAYER, region=3502324)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(arg_12_15)
    ForceAnimation(arg_0_3, arg_8_11)
    SetCharacterEventTarget(arg_0_3, 10000)
    ReplanAI(arg_0_3)
    WaitFrames(arg_12_15)
    IfCharacterOutsideRegion(0, PLAYER, region=3502327)
    WaitFrames(20)
    ClearTargetList(arg_0_3)
    ReplanAI(arg_0_3)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_16_19)
    WaitFrames(120)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_20_23)
    WaitFrames(20)
    Restart()


def Event13500900(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13500900: Event 13500900 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled((arg_4_7, arg_12_15))
    IfCharacterDead(1, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_16_19)
    SaveRequest()


def Event13500910(_, arg_0_3: int, arg_4_7: int):
    """ 13500910: Event 13500910 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    EnableFlag(arg_4_7)


def Event13500920(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13500920: Event 13500920 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(arg_4_7)
    IfFlagEnabled(-1, arg_4_7)
    IfHealthLessThanOrEqual(-1, arg_0_3, 0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    DisableFlagRange((arg_8_11, arg_12_15))
    EnableFlag(arg_16_19)
    SaveRequest()


def Event13500940(_, arg_0_3: int):
    """ 13500940: Event 13500940 """
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1730, 1749))
    EnableFlag(1735)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, 1730)
    GotoIfFlagEnabled(Label.L6, 1735)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(arg_0_3)
    DisableAnimations(arg_0_3)
    DisableGravity(3500938)
    DropMandatoryTreasure(3500938)
    ForceAnimation(arg_0_3, 103162, loop=True, skip_transition=True)
    End()

    # --- 6 --- #
    DefineLabel(6)
    ForceAnimation(arg_0_3, 103160, loop=True, skip_transition=True)
    DisableGravity(3500938)
    EndIfFlagEnabled(73500412)
    EnableInvincibility(arg_0_3)
    End()


def Event13500942(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500942: Event 13500942 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled((1730, 1734))
    DisableFlag(arg_8_11)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)
    EnableFlag(arg_8_11)
    IfCharacterOutsideRegion(0, arg_0_3, region=arg_4_7)
    DisableFlag(arg_8_11)
    Restart()


def Event13500941():
    """ 13500941: Event 13500941 """
    GotoIfFlagDisabled(Label.L0, 73500412)
    EndOfAnimation(3501300, 2)
    DisableObjectActivation(3501300, obj_act_id=3500010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=13504245)
    DisableInvincibility(3500901)
    DisableObjectActivation(3501300, obj_act_id=3500010)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    Wait(2.0)
    EnableFlag(73500412)


def Event13500943(_, arg_0_3: int):
    """ 13500943: Event 13500943 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled((1730, 1734))
    DisableFlag(73500411)
    GotoIfFlagEnabled(Label.L0, 13601400)
    ForceAnimation(arg_0_3, 103164, loop=True, skip_transition=True)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 103160, loop=True, skip_transition=True)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(0, 73500411)
    IfHealthEqual(1, arg_0_3, 0.0)
    EndIfConditionTrue(1)
    ForceAnimation(arg_0_3, 103161, loop=True, skip_transition=True)
    IfFlagDisabled(0, 73500411)
    IfHealthEqual(1, arg_0_3, 0.0)
    EndIfConditionTrue(1)
    Restart()


def Event13500944(_, arg_0_3: int):
    """ 13500944: Event 13500944 """
    EndIfFlagRangeAnyEnabled((1730, 1734))
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=1)
    Kill(arg_0_3, award_souls=True)
    ForceAnimation(arg_0_3, 103162, skip_transition=True)


def Event13500945(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int):
    """ 13500945: Event 13500945 """
    IfCharacterHuman(-15, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-15)
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1650, 1669))
    DisableFlagRange((1650, 1669))
    EnableFlag(1651)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 1660)
    IfFlagRangeAnyEnabled(1, (1722, 1723))
    IfFlagEnabled(1, 73500602)
    GotoIfConditionFalse(Label.L8, input_condition=1)
    DisableFlagRange((1650, 1669))
    EnableFlag(1651)

    # --- 8 --- #
    DefineLabel(8)

    # --- 9 --- #
    DefineLabel(9)
    DisableObject(arg_4_7)
    DisableObject(arg_12_15)
    DisableObject(arg_16_19)
    DisableObject(arg_20_23)
    GotoIfFlagEnabled(Label.L0, 1660)
    GotoIfFlagEnabled(Label.L1, 1650)
    GotoIfFlagEnabled(Label.L2, 1651)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(arg_0_3, TeamType.Ally)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    ForceAnimation(arg_0_3, 7000)
    EnableObjectInvulnerability(arg_8_11)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    EndIfFlagEnabled(arg_24_27)
    CreateObjectVFX(900201, obj=arg_4_7, model_point=200)
    EnableObjectInvulnerability(arg_8_11)
    EnableObject(arg_12_15)
    EnableObjectInvulnerability(arg_12_15)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    EnableObject(arg_20_23)
    EnableObjectInvulnerability(arg_20_23)
    EndIfFlagEnabled(arg_24_27)
    EnableObjectInvulnerability(arg_8_11)
    EnableObject(arg_16_19)
    EnableObjectInvulnerability(arg_16_19)
    End()


def Event13500946(_, arg_0_3: int, arg_4_7: int):
    """ 13500946: Event 13500946 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagEnabled(1, 1660)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=1)
    Kill(arg_0_3, award_souls=True)
    IfFlagEnabled(0, 1650)
    CreateObjectVFX(900201, obj=arg_4_7, model_point=200)


def Event13500948(_, arg_0_3: int):
    """ 13500948: Event 13500948 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    EndIfFlagEnabled(Flags.LadyMariaFirstTimeDone)
    IfFlagRangeAnyEnabled(1, (1650, 1651))
    IfActionButtonParamActivated(1, action_button_id=3500910, entity=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13500947)


def Event13500949(_, arg_0_3: int, arg_4_7: int):
    """ 13500949: Event 13500949 """
    DisableFlag(arg_4_7)
    IfFlagEnabled(0, arg_4_7)
    IfHealthEqual(1, arg_0_3, 0.0)
    EndIfConditionTrue(1)
    ForceAnimation(arg_0_3, 7003, loop=True, skip_transition=True)
    IfFlagDisabled(0, arg_4_7)
    IfHealthEqual(2, arg_0_3, 0.0)
    EndIfConditionTrue(2)
    ForceAnimation(arg_0_3, 7000, loop=True, skip_transition=True)
    Restart()


def Event13500950(_, arg_0_3: int):
    """ 13500950: Event 13500950 """
    IfCharacterHuman(-15, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-1)
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1710, 1729))
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagRangeAnyEnabled(1, (1720, 1721))
    IfFlagEnabled(1, 73400403)
    IfFlagEnabled(1, 13500100)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1710, 1729))
    EnableFlag(1722)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 1722)
    IfFlagEnabled(-3, Flags.LadyMariaDead)
    IfConditionTrue(3, input_condition=-3)
    IfFlagEnabled(3, 73500602)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagRangeAnyEnabled(4, (1720, 1722))
    IfFlagEnabled(4, 73400403)
    IfFlagEnabled(4, Flags.LadyMariaDead)
    GotoIfConditionFalse(Label.L8, input_condition=4)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 8 --- #
    DefineLabel(8)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, 1722)
    GotoIfFlagEnabled(Label.L1, 1727)
    GotoIfFlagEnabled(Label.L2, 1712)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(arg_0_3, TeamType.Ally)
    ForceAnimation(arg_0_3, 103150)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()


def Event13500951(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500951: Event 13500951 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(arg_4_7)
    IfFlagEnabled(1, arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterHasSpecialEffect(1, arg_0_3, 151)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 103155)
    IfFlagEnabled(2, arg_8_11)
    IfFlagDisabled(2, arg_4_7)
    IfCharacterHasSpecialEffect(2, arg_0_3, 152)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(arg_0_3, 103150)
    Restart()


def Event13500952(_, arg_0_3: int):
    """ 13500952: Event 13500952 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagRangeAnyEnabled(1, (1720, 1722))
    IfFlagEnabled(1, Flags.LadyMariaDead)
    IfFlagEnabled(1, 73400403)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)


def Event13500953(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500953: Event 13500953 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    GotoIfFlagDisabled(Label.L0, arg_0_3)
    GotoIfFlagDisabled(Label.L1, arg_4_7)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, arg_4_7)
    AwardItemLot(arg_8_11, host_only=False)
    SaveRequest()


def Event13500960(_, arg_0_3: int, arg_4_7: int):
    """ 13500960: Event 13500960 """
    IfCharacterHuman(-1, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-1)
    GotoIfFlagRangeState(Label.L1, RangeState.AnyOn, FlagType.Absolute, (1750, 1769))
    DisableFlagRange((1750, 1769))
    EnableFlag(1760)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(1, 73500301)
    IfFlagEnabled(1, 1760)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    GotoIfFlagDisabled(Label.L2, 73500330)
    GotoIfFlagDisabled(Label.L3, 73500331)
    DisableFlagRange((1750, 1769))
    EnableFlag(1761)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(73500331)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(73500330)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(2, 73500309)
    IfFlagEnabled(2, 1761)
    GotoIfConditionFalse(Label.L4, input_condition=2)
    GotoIfFlagDisabled(Label.L2, 73500335)
    GotoIfFlagDisabled(Label.L3, 73500336)
    DisableFlagRange((1750, 1769))
    EnableFlag(1762)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(73500336)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(73500335)

    # --- 4 --- #
    DefineLabel(4)
    DisableFlag(73500305)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, 1760)
    GotoIfFlagEnabled(Label.L1, 1761)
    GotoIfFlagEnabled(Label.L2, 1762)
    GotoIfFlagEnabled(Label.L3, 1750)
    GotoIfFlagEnabled(Label.L4, 1751)
    GotoIfFlagEnabled(Label.L5, 1752)
    DisableCharacter(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    End()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(arg_0_3, 7002, loop=True, skip_transition=True)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    EnableCharacter(arg_4_7)
    DisableBackread(arg_0_3)
    EnableBackread(arg_4_7)
    End()

    # --- 3 --- #
    DefineLabel(3)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 2250, loop=True, skip_transition=True)
    DisableCharacter(arg_4_7)
    EnableBackread(arg_0_3)
    DisableBackread(arg_4_7)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 4 --- #
    DefineLabel(4)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    EnableInvincibility(arg_4_7)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableCharacter(arg_0_3)
    EnableCharacter(arg_4_7)
    DisableBackread(arg_0_3)
    EnableBackread(arg_4_7)
    ForceAnimation(arg_4_7, 7011, loop=True, skip_transition=True)
    End()


def Event13500963(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13500963: Event 13500963 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled((arg_4_7, arg_12_15))
    IfCharacterDead(1, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_16_19)
    SaveRequest()


def Event13500965():
    """ 13500965: Event 13500965 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1752)
    IfFlagEnabled(0, 73500318)
    DisableFlagRange((1750, 1769))
    EnableFlag(1752)
    EnableInvincibility(3500911)
    ForceAnimation(3500911, 7002, skip_transition=True)
    WaitFrames(178)
    ForceAnimation(3500911, 7011, loop=True, skip_transition=True)
    SaveRequest()


def Event13500966():
    """ 13500966: Event 13500966 """
    EndIfThisEventFlagEnabled()
    DisableObject(3500912)
    DisableObject(3500913)
    IfFlagEnabled(0, 1762)
    EnableObject(3500912)
    EnableObject(3500913)


def Event13500967(_, arg_0_3: int):
    """ 13500967: Event 13500967 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagDisabled(0, 73500325)
    IfHealthEqual(1, arg_0_3, 0.0)
    EndIfConditionTrue(1)
    ForceAnimation(arg_0_3, 0, loop=True, skip_transition=True)
    IfFlagEnabled(0, 73500325)
    IfHealthEqual(2, arg_0_3, 0.0)
    EndIfConditionTrue(2)
    ForceAnimation(arg_0_3, 7000, loop=True, skip_transition=True)
    Restart()


def Event13500968(_, arg_0_3: int):
    """ 13500968: Event 13500968 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(73500326)
    IfFlagEnabled(0, 73500326)
    IfHealthEqual(1, arg_0_3, 0.0)
    EndIfConditionTrue(1)
    ForceAnimation(arg_0_3, 7001, loop=True)
    IfFlagDisabled(0, 73500326)
    IfHealthEqual(2, arg_0_3, 0.0)
    EndIfConditionTrue(2)
    ForceAnimation(arg_0_3, 0, loop=True, skip_transition=True)
    DisableFlag(73500326)


def Event13500977():
    """ 13500977: Event 13500977 """
    GotoIfFlagEnabled(Label.L0, 13500101)
    SetEventPoint(3500935, region=3502907, reaction_range=3.0)
    IfFlagEnabled(0, 13500100)
    SetEventPoint(3500935, region=3502909, reaction_range=3.0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetEventPoint(3500933, region=3502909, reaction_range=3.0)


def Event13500978(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500978: Event 13500978 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    GotoIfFlagDisabled(Label.L0, arg_0_3)
    GotoIfFlagDisabled(Label.L1, arg_4_7)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(1, 3500901)
    IfConditionTrue(0, input_condition=1)
    DropMandatoryTreasure(arg_8_11)
    SaveRequest()


@RestartOnRest
def Event13500980(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 13500980: Event 13500980 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, arg_4_7)
    Wait(arg_8_11)
    DisableFlag(arg_4_7)
    Restart()


def Event13500990(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13500990: Event 13500990 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagDisabled(arg_8_11)
    IfFlagDisabled(0, arg_4_7)
    IfHealthEqual(1, arg_0_3, 0.0)
    EndIfConditionTrue(1)
    ForceAnimation(arg_0_3, 7013, loop=True, skip_transition=True)
    IfFlagEnabled(0, arg_4_7)
    EndIfFlagDisabled(arg_8_11)
    IfHealthEqual(2, arg_0_3, 0.0)
    EndIfConditionTrue(2)
    ForceAnimation(arg_0_3, 9002, loop=True, skip_transition=True)
    Restart()


def Event13500994(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: float, 
                  arg_24_27: float, arg_28_31: int):
    """ 13500994: Event 13500994 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagDisabled(arg_16_19)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_12_15)
    WaitFrames(1)
    ForceAnimation(arg_0_3, arg_28_31, skip_transition=True)
    WaitFrames(74)
    ForceAnimation(arg_0_3, 7011, loop=True, skip_transition=True)
    GotoIfFlagEnabled(Label.L0, arg_8_11)
    Move(arg_4_7, destination=arg_0_3, destination_type=CoordEntityType.Character, model_point=90, short_move=True)
    WaitFrames(1)
    DropMandatoryTreasure(arg_4_7)
    IfFlagEnabled(0, arg_8_11)
    Wait(arg_20_23)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    Wait(arg_24_27)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(arg_0_3, 7012, skip_transition=True)
    WaitFrames(109)
    ForceAnimation(arg_0_3, 7013, loop=True, skip_transition=True)
    DisableFlag(arg_12_15)
    Restart()


def Event13500998():
    """ 13500998: Event 13500998 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(73500338)
    IfCharacterInsideRegion(0, PLAYER, region=3502911)
    EnableFlag(73500338)
    IfCharacterOutsideRegion(0, PLAYER, region=3502911)
    DisableFlag(73500338)
    Restart()


def Event13500999():
    """ 13500999: Event 13500999 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 73500317)
    RunEvent(9350, slot=0, args=(2,))


def Event13501900(_, arg_0_3: int):
    """ 13501900: Event 13501900 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    Wait(0.0)


def Event13501915(_, arg_0_3: int, arg_4_7: int):
    """ 13501915: Event 13501915 """
    IfFlagEnabled(-1, arg_4_7)
    IfThisEventFlagEnabled(-1)
    GotoIfConditionFalse(Label.L0, input_condition=-1)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    EnableFlag(13501904)


def Event13501920(_, arg_0_3: int, arg_4_7: int):
    """ 13501920: Event 13501920 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfFlagEnabled(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)


def Event13501940(_, arg_0_3: int, arg_4_7: int):
    """ 13501940: Event 13501940 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, arg_0_3)
    DisableFlag(arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)
    End()


@RestartOnRest
def Event13501960():
    """ 13501960: Event 13501960 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfPlayerHasGood(0, 4015, including_box=False)

    # --- 0 --- #
    DefineLabel(0)
    Kill(3500750, award_souls=False)
    Kill(3500760, award_souls=False)


@RestartOnRest
def Event13505900(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13505900: Event 13505900 """
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_4_7)
    IfPlayerHasGood(1, 4015, including_box=False)
    IfFlagDisabled(1, 1730)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_20_23)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)


@RestartOnRest
def Event13505901(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13505901: Event 13505901 """
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_4_7)
    IfPlayerHasGood(1, 4015, including_box=False)
    IfFlagDisabled(1, 1730)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfFlagEnabled(1, arg_0_3)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=10306)
    WaitRandomSeconds(min_seconds=2.0, max_seconds=4.0)
    Restart()


@RestartOnRest
def Event13505902(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int, arg_28_31: int):
    """ 13505902: Event 13505902 """
    AICommand(arg_0_3, command_id=30, slot=0)
    ReplanAI(arg_0_3)
    EnableInvincibility(arg_0_3)
    DisableAnimations(arg_0_3)
    AddSpecialEffect(arg_0_3, 5560, affect_npc_part_hp=False)
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_4_7)
    IfPlayerHasGood(1, 4015, including_box=False)
    IfFlagDisabled(1, 1730)
    IfFlagEnabled(1, arg_20_23)
    IfFlagDisabled(1, arg_8_11)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=arg_12_15)
    IfConditionTrue(-1, input_condition=2)
    IfCharacterInsideRegion(3, PLAYER, region=arg_16_19)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, 3)
    Move(arg_0_3, destination=arg_28_31, destination_type=CoordEntityType.Region,
         set_draw_parent=3504000)
    SkipLines(1)
    Move(arg_0_3, destination=3502897, destination_type=CoordEntityType.Region, set_draw_parent=3504000)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    DisableInvincibility(arg_0_3)
    EnableAnimations(arg_0_3)
    CancelSpecialEffect(arg_0_3, 5560)
    AddSpecialEffect(arg_0_3, 8060, affect_npc_part_hp=False)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    ForceAnimation(arg_0_3, 101203)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    DisableInvincibility(arg_0_3)
    EnableAnimations(arg_0_3)
    CancelSpecialEffect(arg_0_3, 5560)
    EnableFlag(arg_4_7)
    DisableFlag(arg_24_27)
    IfFlagEnabled(0, arg_24_27)
    Restart()


@RestartOnRest
def Event13505903(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13505903: Event 13505903 """
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfCharacterInsideRegion(-1, PLAYER, region=3502898)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=30, slot=0)
    ReplanAI(arg_0_3)
    Wait(2.0)
    EnableInvincibility(arg_0_3)
    DisableAnimations(arg_0_3)
    AddSpecialEffect(arg_0_3, 5560, affect_npc_part_hp=False)
    CancelSpecialEffect(arg_0_3, 8060)
    CancelSpecialEffect(arg_0_3, 1130)
    CancelSpecialEffect(arg_0_3, 1150)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=122)
    Wait(4.0)
    EnableFlag(arg_20_23)
    DisableFlag(arg_4_7)
    IfFlagEnabled(0, arg_4_7)
    Restart()


@RestartOnRest
def Event13505904(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13505904: Event 13505904 """
    DisableBackread(arg_16_19)
    GotoIfFlagDisabled(Label.L0, 1730)
    DropMandatoryTreasure(arg_16_19)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(1, arg_0_3)
    IfFlagEnabled(2, 1730)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    CancelSpecialEffect(arg_0_3, 8060)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=122)
    EnableFlag(arg_8_11)
    IfCharacterHuman(2, PLAYER)
    EndIfConditionFalse(2)
    AwardItemLot(arg_12_15, host_only=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DropMandatoryTreasure(arg_16_19)


def Event13504400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13504400: Event 13504400 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(1, 13501900)
    IfFlagEnabled(1, 13500100)
    IfFlagDisabled(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateVFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagDisabled(2, arg_8_11)
    IfFlagDisabled(2, arg_12_15)
    IfFlagDisabled(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagEnabled(2, 13501900)
    IfFlagEnabled(2, 13500100)
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


def Event13504410(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int, arg_28_31: int):
    """ 13504410: Event 13504410 """
    SkipLinesIfFlagEnabled(1, arg_12_15)
    DisableCharacter(arg_4_7)
    SkipLinesIfFlagEnabled(3, arg_16_19)
    IfClient(1)
    IfFlagEnabled(1, arg_12_15)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(arg_4_7)
    EndIfFlagEnabled(arg_24_27)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(arg_4_7, UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagDisabled(2, arg_12_15)
    IfFlagDisabled(2, arg_16_19)
    IfFlagEnabled(2, arg_20_23)
    IfFlagDisabled(2, arg_24_27)
    IfActionButtonParamActivated(2, action_button_id=arg_28_31, entity=arg_4_7)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682, affect_npc_part_hp=False)
    SummonNPC(arg_0_3, arg_4_7, arg_8_11, summon_flag=arg_12_15, dismissal_flag=arg_16_19)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


def Event13504450(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13504450: Event 13504450 """
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=1.0)
    IfFlagEnabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)


def Event13504460(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int):
    """ 13504460: Event 13504460 """
    EndIfClient()
    IfFlagEnabled(1, arg_20_23)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    RotateToFaceEntity(arg_0_3, arg_8_11, animation=arg_16_19, wait_for_completion=True)
    IfCharacterInsideRegion(2, arg_0_3, region=arg_12_15)
    RestartIfConditionFalse(2)
    SetEventPoint(arg_0_3, region=arg_8_11, reaction_range=1.0)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_24_27)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
