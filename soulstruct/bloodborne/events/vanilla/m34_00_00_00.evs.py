"""
linked:
110

strings:
0: ボス_撃破
12: PC情報_ボス撃破_ルドウイーク
46: ボス_戦闘開始
62: ボス戦_撃破時間
80: PC情報_ボス撃破_教区長Ω
110: N:\\SPRJ\\data\\Param\\event\\common.emevd
186: 
188: 
190: 
"""
from soulstruct.bloodborne.events import *


def Constructor():
    """ 0: Event 0 """
    GotoIfFlagOn(Label.L0, 13400999)
    RunEvent(7000, slot=55, args=(3400950, 3401950, 999, 13407800))
    RunEvent(7000, slot=56, args=(3400951, 3401951, 999, 13407820))
    RunEvent(7000, slot=57, args=(3400952, 3401952, 13401800, 13407840))
    RunEvent(7000, slot=58, args=(3400953, 3401953, 13401850, 13407860))
    RunEvent(7100, slot=55, args=(73400200, 3401950))
    RunEvent(7100, slot=56, args=(73400201, 3401951))
    RunEvent(7100, slot=57, args=(73400202, 3401952))
    RunEvent(7100, slot=58, args=(73400203, 3401953))
    RunEvent(7200, slot=55, args=(73400100, 3401950, 2102953))
    RunEvent(7200, slot=56, args=(73400101, 3401951, 2102953))
    RunEvent(7200, slot=57, args=(73400102, 3401952, 2102953))
    RunEvent(7200, slot=58, args=(73400103, 3401953, 2102953))
    RunEvent(7300, slot=55, args=(72103400, 3401950))
    RunEvent(7300, slot=56, args=(72103401, 3401951))
    RunEvent(7300, slot=57, args=(72103402, 3401952))
    RunEvent(7300, slot=58, args=(72103403, 3401953))
    DisableObject(3401999)
    DeleteVFX(3403999, erase_root_only=False)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(3400950)
    DisableCharacter(3400951)
    DisableCharacter(3400952)
    DisableCharacter(3400953)
    DisableObject(3401950)
    DisableObject(3401951)
    DisableObject(3401952)
    DisableObject(3401953)
    SetRespawnPoint(3402955)
    EnableFlag(9401)
    EnableFlag(9404)

    # --- 1 --- #
    DefineLabel(1)
    DisableFlag(3400)
    DisableFlag(3401)
    DisableFlag(3402)
    EnableFlag(3403)
    SkipLinesIfFlagOff(4, 13401800)
    EnableFlag(3400)
    EnableFlag(3401)
    EnableFlag(3402)
    EnableFlag(3403)
    SkipLinesIfFlagOff(4, 13401852)
    DisableFlag(3400)
    DisableFlag(3401)
    EnableFlag(3402)
    DisableFlag(3403)
    SkipLinesIfFlagOff(4, 13401850)
    EnableFlag(3400)
    EnableFlag(3401)
    EnableFlag(3402)
    EnableFlag(3403)
    RunEvent(13400010)
    RunEvent(13401000)
    RegisterLadder(start_climbing_flag=13400000, stop_climbing_flag=13400001, obj=3401000)
    RegisterLadder(start_climbing_flag=13400002, stop_climbing_flag=13400003, obj=3401001)
    RunEvent(13401500)
    RunEvent(13404700, slot=0, args=(3400790, 13404701, 13404711, 3400, 999))
    RunEvent(13404700, slot=5, args=(3400791, 13404702, 13404712, 3400, 999))
    RunEvent(13404710, slot=0, args=(3400790, 13404701, 13404711, 13404721))
    RunEvent(13404710, slot=5, args=(3400701, 13404702, 13404712, 13404722))
    RunEvent(13404720, slot=0, args=(3400790, 13404701, 13404711, 13404721))
    RunEvent(13404720, slot=5, args=(3400791, 13404702, 13404712, 13404722))
    RunEvent(13404730, slot=0, args=(3400790, 13404701, 13404711, 3400, 13404810, 999, 999, 13404712))
    RunEvent(13404730, slot=5, args=(3400791, 13404702, 13404712, 3400, 13404810, 999, 999, 13404711))
    RunEvent(13404740)
    RunEvent(13404742)
    RunEvent(13401800)
    RunEvent(13404811)
    RunEvent(13401801)
    RunEvent(13404800)
    RunEvent(13404801)
    RunEvent(13404802)
    RunEvent(13404803)
    RunEvent(13404804)
    RunEvent(13404805)
    RunEvent(13404806)
    RunEvent(13404807)
    RunEvent(13401802)
    RunEvent(13401803)
    RunEvent(13404820)
    RunEvent(13404821)
    RunEvent(13404822)
    RunEvent(13404823)
    RunEvent(13404840)
    RunEvent(13401804)
    SkipLinesIfFlagOn(8, 13400999)
    RunEvent(13404824)
    RunEvent(13404825)
    RunEvent(13404830, slot=0, args=(3400, 3400, 1, 300, 480, 7001, 152), arg_types="hihiiii")
    RunEvent(13404830, slot=1, args=(3401, 3401, 2, 150, 482, 7004, 72), arg_types="hihiiii")
    RunEvent(13404830, slot=2, args=(3402, 3402, 3, 150, 481, 7002, 72), arg_types="hihiiii")
    RunEvent(13404835)
    RunEvent(13404841)
    SkipLines(3)
    RunEvent(13404830, slot=0, args=(3400, 3400, 1, 400, 480, 7001, 152), arg_types="hihiiii")
    RunEvent(13404830, slot=1, args=(3401, 3401, 2, 200, 482, 7004, 72), arg_types="hihiiii")
    RunEvent(13404830, slot=2, args=(3402, 3402, 3, 200, 481, 7002, 72), arg_types="hihiiii")
    RunEvent(13401850)
    RunEvent(13404861)
    RunEvent(13401851)
    RunEvent(13404850)
    RunEvent(13404851)
    RunEvent(13404852)
    RunEvent(13404853)
    RunEvent(13404854)
    RunEvent(13404855)
    RunEvent(13404856)
    RunEvent(13404857)
    RunEvent(13404870, slot=0, args=(3450, 3450, 1, 480, 490, 60, 8020), arg_types="hihiiii")
    RunEvent(13404870, slot=1, args=(3451, 3451, 2, 481, 491, 150, 8000), arg_types="hihiiii")
    RunEvent(13404870, slot=2, args=(3452, 3452, 3, 482, 492, 150, 8010), arg_types="hihiiii")
    RunEvent(13404870, slot=3, args=(3453, 3453, 4, 483, 493, 250, 8030), arg_types="hihiiii")
    RunEvent(13404870, slot=4, args=(3454, 3454, 5, 484, 494, 250, 8040), arg_types="hihiiii")
    RunEvent(13404875)
    RunEvent(13401853)
    RunEvent(13401200, slot=0, args=(3400950, 3401020, 13401211))
    RunEvent(13401210, slot=0, args=(3401010, 13400000, 1, 3400000))
    RunEvent(13401210, slot=1, args=(3401020, 13400001, 1, 3400010))
    RunEvent(13401220)
    RunEvent(13400100)
    RunEvent(13400220, slot=0, args=(3400680, 53401710))
    RunEvent(13400220, slot=1, args=(3400681, 53401720))
    RunEvent(13405103)
    RunEvent(13400310, slot=0, args=(3400590, 3402341))
    RunEvent(13400320)
    RunEvent(13404799)
    RunEvent(13405100, slot=0, args=(3401400, 3402531, 3402554))
    RunEvent(13405105, slot=0, args=(3402370, 3401350, 3401351, 0, 0, 0))
    RunEvent(13405115, slot=0, args=(3401366, 13405130, 0, 50, 6280, 6281, 6282, 6283))
    RunEvent(13405115, slot=1, args=(3401356, 13405131, 0, 60, 6284, 6285, 6286, 6287))
    RunEvent(13405115, slot=2, args=(3401359, 13405132, 0, 70, 6280, 6281, 6282, 6283))
    RunEvent(13405115, slot=3, args=(3401363, 13405132, 20, 80, 6280, 6281, 6282, 6283))
    RunEvent(13405115, slot=4, args=(3401364, 13405132, 10, 40, 6280, 6281, 6282, 6283))
    RunEvent(13405115, slot=5, args=(3401365, 13405132, 30, 50, 6280, 6281, 6282, 6283))
    RunEvent(13405115, slot=6, args=(3401364, 13405133, 10, 60, 6280, 6281, 6282, 6283))
    RunEvent(13405115, slot=7, args=(3401359, 13405135, 20, 40, 6280, 6281, 6282, 6283))
    RunEvent(13405115, slot=9, args=(3401363, 13405135, 10, 70, 6280, 6281, 6282, 6283))
    RunEvent(13405115, slot=10, args=(3401364, 13405135, 17, 60, 6280, 6281, 6282, 6283))
    RunEvent(13405115, slot=11, args=(3401365, 13405135, 6, 50, 6280, 6281, 6282, 6283))
    RunEvent(13405113, slot=0, args=(3401360, 13405136, 6, 50, 6280, 6281, 6282, 6283))
    RunEvent(13405140, slot=1, args=(3400207, 3402510, 13405132, 3402371, 3401367, 30))
    RunEvent(13405140, slot=2, args=(3400207, 3402376, 13405133, 3402371, 3401367, 10))
    RunEvent(13405140, slot=4, args=(3400210, 3402377, 13405136, 3402374, 3401368, 20))
    RunEvent(13405145, slot=0, args=(3402374, 3401368, 13405130))
    RunEvent(13405145, slot=1, args=(3402372, 3401357, 13405131))
    RunEvent(13405145, slot=2, args=(3402371, 3401367, 13405135))
    RunEvent(13405145, slot=3, args=(3402374, 3401368, 13405136))
    RunEvent(13405155, slot=0, args=(3402515,))
    RunEvent(13405160, slot=0, args=(3401330,))
    RunEvent(13405160, slot=1, args=(3401331,))
    RunEvent(13405160, slot=2, args=(3401332,))
    RunEvent(13405160, slot=3, args=(3401333,))
    RunEvent(13405160, slot=4, args=(3401334,))
    RunEvent(13405160, slot=5, args=(3401335,))
    RunEvent(13405160, slot=6, args=(3401336,))
    RunEvent(13405160, slot=7, args=(3401337,))
    RunEvent(13405160, slot=8, args=(3401338,))
    RunEvent(13405160, slot=9, args=(3401339,))
    RunEvent(13405160, slot=10, args=(3401340,))
    RunEvent(13405160, slot=11, args=(3401341,))
    RunEvent(13405160, slot=12, args=(3401342,))
    RunEvent(13405160, slot=13, args=(3401343,))
    RunEvent(13405160, slot=14, args=(3401344,))
    RunEvent(13405110)
    RunEvent(13405112)
    RunEvent(13405200, slot=0, args=(3400300, 3402600, 3004, 3402601))
    RunEvent(13400330, slot=0, args=(3400650,))
    RunEvent(13405211, slot=1, args=(3402301,))
    RunEvent(13405211, slot=2, args=(3402302,))
    RunEvent(13405220, slot=0, args=(3400152, 7015, 109900, 7016, 109955, 0, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13405220, slot=2, args=(3400154, 7015, 109900, 7016, 109955, 0, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13405220, slot=16, args=(3400315, 7001, 400010, 7002, 400010, 3402555, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13405220, slot=17, args=(3400169, 7015, 109900, 7016, 109955, 0, 0.0, 2.0), arg_types="iiiiiiff")
    RunEvent(13405220, slot=18, args=(3400170, 7015, 109900, 7016, 109955, 0, 0.0, 2.0), arg_types="iiiiiiff")
    RunEvent(13405220, slot=19, args=(3400171, 7015, 109900, 7016, 109955, 0, 0.0, 2.0), arg_types="iiiiiiff")
    RunEvent(13405220, slot=20, args=(3400172, 7015, 109900, 7016, 109955, 0, 0.0, 2.0), arg_types="iiiiiiff")
    RunEvent(13405220, slot=3, args=(3400350, 7000, 6550, 0, 6550, 0, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13405550, slot=4, args=(3400141, 7000, 109900, 7002, 109950, 2.0, 3.0), arg_types="iiiiiff")
    RunEvent(13405550, slot=5, args=(3400146, 7000, 109900, 7002, 109950, 2.0, 4.0), arg_types="iiiiiff")
    RunEvent(13405550, slot=7, args=(3400147, 7003, 109900, 7005, 109953, 4.0, 6.0), arg_types="iiiiiff")
    RunEvent(13405550, slot=8, args=(3400148, 7006, 109900, 7008, 109953, 0.0, 0.0), arg_types="iiiiiff")
    RunEvent(13405300, slot=1, args=(3400208, 0, 3.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=2, args=(3400209, 0, 3.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=3, args=(3400207, 0, 3.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=4, args=(3400210, 0, 3.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=7, args=(3400160, 3402506, 10.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=8, args=(3400309, 3402508, 10.0, 2.0), arg_types="iiff")
    RunEvent(13405300, slot=9, args=(3400280, 3402510, 10.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=10, args=(3400281, 3402510, 10.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=15, args=(3400664, 3402536, 10.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=16, args=(3400510, 3402539, 10.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=17, args=(3400550, 3402538, 10.0, 0.0), arg_types="iiff")
    RunEvent(13405300, slot=18, args=(3400580, 3402544, 5.0, 0.0), arg_types="iiff")
    RunEvent(13405350, slot=0, args=(3400405, 3402512, 0, 3403303, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=1, args=(3400204, 3402315, 0, 3403353, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=2, args=(3400253, 3402315, 0, 3403354, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=3, args=(3400508, 3402504, 0, 3403335, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=4, args=(3400203, 3402504, 0, 3403335, 1.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=5, args=(3400200, 3402534, 0, 3403351, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=6, args=(3400105, 3402512, 0, 3403356, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=7, args=(3400106, 3402512, 0, 3403356, 4.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=8, args=(3400202, 3402505, 0, 3403339, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=9, args=(3400252, 3402505, 0, 3403339, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=10, args=(3400411, 3402360, 0, 3403310, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=11, args=(3400601, 3402650, 0, 3403347, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=12, args=(3400552, 3402558, 0, 3403348, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=13, args=(3400105, 3402559, 0, 3403305, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=14, args=(3400106, 3402559, 0, 3403305, 2.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=15, args=(3400665, 3402315, 0, 3403336, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=16, args=(3400601, 3402555, 0, 3403347, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=17, args=(3400137, 3402502, 0, 3403301, 1.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=18, args=(3400107, 3402513, 0, 3403352, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=19, args=(3400412, 3402553, 0, 3403343, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=20, args=(3400165, 3402526, 0, 3403311, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=24, args=(3400166, 3402526, 0, 3403311, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=25, args=(3400167, 3402526, 0, 3403311, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=26, args=(3400168, 3402526, 0, 3403311, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=27, args=(3400611, 3402561, 0, 3403315, 2.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=34, args=(3400158, 3402560, 0, 3403304, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=35, args=(3400159, 3402560, 0, 3403304, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=36, args=(3400160, 3402560, 0, 3403304, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=37, args=(3400161, 3402560, 0, 3403304, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=38, args=(3400162, 3402560, 0, 3403304, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=39, args=(3400403, 3402517, 0, 3403302, 8.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=40, args=(3400303, 3402517, 0, 3403309, 16.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=41, args=(3400205, 3402304, 0, 3403307, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=42, args=(3400206, 3402304, 0, 3403308, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=43, args=(3400111, 3402552, 0, 3403355, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=44, args=(3400112, 3402511, 0, 3403355, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=45, args=(3400113, 3402511, 0, 3403355, 4.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=46, args=(3400130, 3402517, 0, 3403301, 8.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=47, args=(3400131, 3402500, 0, 3403306, 2.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=48, args=(3400132, 3402517, 0, 3403301, 9.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=49, args=(3400133, 3402517, 0, 3403301, 9.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=50, args=(3400134, 3402517, 0, 3403301, 8.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=51, args=(3400135, 3402502, 0, 3403301, 2.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=52, args=(3400137, 3402517, 0, 3403301, 9.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=53, args=(3400140, 3402517, 0, 3403301, 2.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=54, args=(3400149, 3402517, 0, 3403301, 7.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=55, args=(3400178, 3402517, 0, 3403314, 15.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=56, args=(3400179, 3402517, 0, 3403314, 15.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=57, args=(3400180, 3402517, 0, 3403314, 15.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=58, args=(3400181, 3402517, 0, 3403314, 9.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=59, args=(3400182, 3402517, 0, 3403314, 15.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=60, args=(3400183, 3402517, 0, 3403314, 15.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=61, args=(3400139, 3402508, 0, 3403358, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=62, args=(3400136, 3402508, 0, 3403358, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=63, args=(3400173, 3402500, 0, 3403312, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=64, args=(3400610, 3402503, 0, 3403313, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=65, args=(3400204, 3402316, 0, 3403353, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=66, args=(3400253, 3402316, 0, 3403354, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=21, args=(3400401, 3402535, 0, 3403331, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=22, args=(3400143, 3402537, 0, 3403340, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=23, args=(3400145, 3402537, 0, 3403340, 2.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=28, args=(3400110, 3402545, 0, 3403341, 5.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=29, args=(3400109, 3402545, 0, 3403341, 1.0, 1), arg_types="iiiifi")
    RunEvent(13405350, slot=30, args=(3400144, 3402537, 0, 3403340, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=32, args=(3400550, 3402555, 0, 3403346, 0.0, 0), arg_types="iiiifi")
    RunEvent(13405350, slot=33, args=(3400580, 3402544, 0, 3403342, 0.0, 1), arg_types="iiiifi")
    RunEvent(13405510, slot=1, args=(3400141,))
    RunEvent(13405510, slot=2, args=(3400142,))
    RunEvent(13405510, slot=3, args=(3400143,))
    RunEvent(13405510, slot=4, args=(3400144,))
    RunEvent(13405510, slot=5, args=(3400145,))
    RunEvent(13405510, slot=6, args=(3400146,))
    RunEvent(13405510, slot=7, args=(3400147,))
    RunEvent(13405510, slot=8, args=(3400148,))
    RunEvent(13405610, slot=0, args=(3400169,))
    RunEvent(13405610, slot=1, args=(3400170,))
    RunEvent(13405610, slot=2, args=(3400171,))
    RunEvent(13405610, slot=3, args=(3400172,))
    RunEvent(13405520, slot=1, args=(3400141, 3402541))
    RunEvent(13405520, slot=2, args=(3400142, 3402541))
    RunEvent(13405520, slot=3, args=(3400143, 3402541))
    RunEvent(13405520, slot=4, args=(3400144, 3402541))
    RunEvent(13405520, slot=5, args=(3400145, 3402541))
    RunEvent(13405520, slot=6, args=(3400146, 3402541))
    RunEvent(13405520, slot=7, args=(3400147, 3402541))
    RunEvent(13405520, slot=8, args=(3400148, 3402541))
    RunEvent(13405530, slot=0, args=(3400143, 3402549))
    RunEvent(13405530, slot=1, args=(3400144, 3402549))
    RunEvent(13405530, slot=2, args=(3400145, 3402549))
    RunEvent(13405540, slot=1, args=(3400142, 3403340, 2, 1, 0.0), arg_types="iiIif")
    RunEvent(13405540, slot=2, args=(3400155, 3403345, 2, 1, 2.0), arg_types="iiIif")
    RunEvent(13405540, slot=3, args=(3400316, 3403344, 4, 0, 0.0), arg_types="iiIif")
    RunEvent(13405640, slot=0, args=(3400404, 7000, 400028, 7001, 400028, 0.0, 0.0), arg_types="iiiiiff")
    RunEvent(13405680, slot=0, args=(3400165, 3400166, 13.0), arg_types="iif")
    RunEvent(13405680, slot=1, args=(3400165, 3400167, 13.0), arg_types="iif")
    RunEvent(13405680, slot=2, args=(3400165, 3400168, 13.0), arg_types="iif")
    RunEvent(13405216, slot=0, args=(3400509, 3402542, 0, 3403338, 1.0, 0), arg_types="iiiifi")
    RunEvent(13405480, slot=0, args=(3400207, 3402515, 3.0, 3010, 0.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=1, args=(3400105, 3402512, 5.0, 7002, 0.0, 1), arg_types="iififB")
    RunEvent(13405480, slot=2, args=(3400106, 3402512, 5.0, 7003, 4.0, 1), arg_types="iififB")
    RunEvent(13405480, slot=3, args=(3400107, 3402513, 3.0, 7004, 0.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=4, args=(3400505, 3402553, 3.0, 700, 1.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=5, args=(3400506, 3402553, 3.0, 700, 0.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=6, args=(3400282, 3402303, 3.0, 3006, 0.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=8, args=(3400507, 3402553, 3.0, 605, 0.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=9, args=(3400468, 3402562, 0.0, 3001, 1.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=10, args=(3400469, 3402562, 0.0, 3001, 0.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=13, args=(3400472, 3402562, 0.0, 3001, 2.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=11, args=(3400315, 3402540, 1.0, 702, 2.0, 0), arg_types="iififB")
    RunEvent(13405480, slot=12, args=(3400409, 3402552, 1.0, 3012, 0.0, 0), arg_types="iififB")
    RunEvent(13400930)
    RunEvent(13400900, slot=2, args=(3400902, 1710, 1729, 1719, 1710))
    RunEvent(13400900, slot=3, args=(3400903, 1710, 1729, 1719, 1711))
    RunEvent(13400910, slot=2, args=(3400902, 73400420))
    RunEvent(13400910, slot=3, args=(3400903, 73400421))
    RunEvent(13400920, slot=2, args=(3400902, 73400420, 1710, 1729, 1725))
    RunEvent(13400920, slot=3, args=(3400903, 73400421, 1710, 1729, 1726))
    RunEvent(13400970, slot=0, args=(3400910,))
    RunEvent(13400970, slot=1, args=(3400911,))
    RunEvent(13400980, slot=0, args=(73400424, 43211))
    RunEvent(13400953, slot=0, args=(1710, 73400430, 43200))
    RunEvent(13400953, slot=1, args=(1711, 73400431, 43210))
    RunEvent(13400995, slot=0, args=(13400970, 43800, 43802, 6671))
    RunEvent(13400980, slot=1, args=(13400971, 43810))
    GotoIfFlagOn(Label.L2, 13400999)
    RunEvent(13400941)
    RunEvent(13400942, slot=0, args=(73400512,))
    RunEvent(13400943, slot=0, args=(3400900,))
    RunEvent(13400944)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(3400900)

    # --- 3 --- #
    DefineLabel(3)
    RunEvent(13400951, slot=0, args=(3400902, 73400422, 1720))
    RunEvent(13400951, slot=1, args=(3400903, 73400423, 1721))
    DeleteVFX(3403911, erase_root_only=False)
    DeleteVFX(3403912, erase_root_only=False)
    DeleteVFX(3403913, erase_root_only=False)
    DeleteVFX(3403914, erase_root_only=False)
    DeleteVFX(3403915, erase_root_only=False)
    DeleteVFX(3403916, erase_root_only=False)
    RunEvent(13404401, slot=0, args=(13404441, 3403911, 13404421, 13404431, 13401800, 6001))
    RunEvent(13404402, slot=0, args=(13404442, 3403912, 13404422, 13404432, 13401800, 13404421))
    RunEvent(13404403, slot=0, args=(13404443, 3403913, 13404423, 13404433, 13401800, 13404421))
    RunEvent(13404404, slot=0, args=(13404444, 3403914, 13404424, 13404434, 13401800, 13404421))
    RunEvent(13404405, slot=0, args=(13404445, 3403915, 13404425, 13404435, 13401850, 13404421))
    RunEvent(13404406, slot=0, args=(13404446, 3403916, 13404426, 13404436, 13401850, 13404421))
    RunEvent(13404410, slot=1, args=(0, 3400921, 3402921, 13404421, 13404431, 13404441, 13401800, 10567))
    RunEvent(13404410, slot=2, args=(6, 3400922, 3402922, 13404422, 13404432, 13404442, 13401800, 10562))
    RunEvent(13404410, slot=3, args=(6, 3400923, 3402923, 13404423, 13404433, 13404443, 13401800, 10563))
    RunEvent(13404410, slot=4, args=(5, 3400924, 3402924, 13404424, 13404434, 13404444, 13401800, 10565))
    RunEvent(13404410, slot=5, args=(6, 3400925, 3402925, 13404425, 13404435, 13404445, 13401850, 10562))
    RunEvent(13404410, slot=6, args=(6, 3400926, 3402926, 13404426, 13404436, 13404446, 13401850, 10563))
    RunEvent(13404450, slot=1, args=(3400921, 3402930, 13404421, 13404431, 13404808))
    RunEvent(13404450, slot=2, args=(3400922, 3402931, 13404422, 13404432, 13404808))
    RunEvent(13404450, slot=3, args=(3400923, 3402931, 13404423, 13404433, 13404808))
    RunEvent(13404450, slot=4, args=(3400924, 3402932, 13404424, 13404434, 13404808))
    RunEvent(13404450, slot=5, args=(3400925, 3402935, 13404425, 13404435, 13404858))
    RunEvent(13404450, slot=6, args=(3400926, 3402935, 13404426, 13404436, 13404858))
    RunEvent(13404460, slot=1, args=(3400921, 3402930, 3402800, 3402801, 101130, 13404451, 3402801))
    RunEvent(13404460, slot=2, args=(3400922, 3402931, 3402800, 3402801, 101130, 13404452, 3402801))
    RunEvent(13404460, slot=3, args=(3400923, 3402931, 3402800, 3402801, 101130, 13404453, 3402801))
    RunEvent(13404460, slot=4, args=(3400924, 3402932, 3402800, 3402801, 101130, 13404454, 3402801))
    RunEvent(13404460, slot=5, args=(3400925, 3402935, 3402850, 3402851, 101130, 13404455, 3402851))
    RunEvent(13404460, slot=6, args=(3400926, 3402935, 3402850, 3402851, 101130, 13404456, 3402851))
    RunEvent(13404490, slot=0, args=(3400925, 13404425, 13404435, 13404858))
    RunEvent(13404490, slot=1, args=(3400926, 13404426, 13404436, 13404858))
    SetEventPoint(3400911, region=3402910, reaction_range=0.0)
    RunEvent(13401250, slot=0, args=(3401250, 0))
    RunEvent(13401250, slot=1, args=(3401251, 0))
    RunEvent(13401250, slot=2, args=(3401252, 0))
    RunEvent(13401250, slot=3, args=(3401253, 0))
    RunEvent(13401250, slot=4, args=(3401254, 0))
    RunEvent(13401250, slot=5, args=(3401255, 0))
    RunEvent(13401250, slot=6, args=(3401256, 0))
    RunEvent(13401250, slot=7, args=(3401257, 0))
    RunEvent(13401250, slot=8, args=(3401258, 0))
    RunEvent(13401250, slot=9, args=(3401259, 0))
    RunEvent(13401250, slot=10, args=(3401260, 0))
    RunEvent(13401250, slot=11, args=(3401261, 0))
    RunEvent(13401250, slot=12, args=(3401262, 0))
    RunEvent(13401250, slot=13, args=(3401263, 0))
    RunEvent(13401250, slot=14, args=(3401264, 0))
    RunEvent(13401250, slot=15, args=(3401265, 0))
    RunEvent(13401250, slot=16, args=(3401266, 0))
    RunEvent(13401250, slot=17, args=(3401267, 0))
    RunEvent(13401250, slot=18, args=(3401268, 0))
    RunEvent(13401250, slot=19, args=(3401269, 0))
    RunEvent(13401250, slot=20, args=(3401270, 0))
    RunEvent(13401250, slot=21, args=(3401271, 0))
    RunEvent(13401250, slot=22, args=(3401272, 0))
    RunEvent(13401250, slot=23, args=(3401273, 0))
    RunEvent(13401250, slot=24, args=(3401274, 0))
    RunEvent(13401250, slot=25, args=(3401275, 0))
    RunEvent(13401250, slot=26, args=(3401276, 0))
    RunEvent(13401250, slot=27, args=(3401277, 0))
    RunEvent(13401250, slot=28, args=(3401278, 0))
    RunEvent(13401250, slot=29, args=(3401279, 0))
    RunEvent(13401250, slot=30, args=(3401280, 0))
    RunEvent(13401250, slot=31, args=(3401281, 0))
    RunEvent(13401250, slot=32, args=(3401282, 0))
    RunEvent(13401250, slot=33, args=(3401283, 0))
    RunEvent(13401250, slot=34, args=(3401284, 0))
    RunEvent(13401250, slot=35, args=(3401285, 0))
    RunEvent(13401250, slot=36, args=(3401286, 0))
    RunEvent(13401250, slot=37, args=(3401287, 0))
    RunEvent(13401250, slot=38, args=(3401288, 0))
    RunEvent(13401250, slot=39, args=(3401289, 0))
    RunEvent(13401250, slot=40, args=(3401290, 0))
    RunEvent(13401250, slot=41, args=(3401291, 0))
    RunEvent(13401250, slot=42, args=(3401292, 0))
    RunEvent(13401250, slot=43, args=(3401293, 0))
    RunEvent(13401350, slot=0, args=(3401294, 0, 3402547))
    RunEvent(13401350, slot=1, args=(3401295, 0, 3402547))
    RunEvent(13401350, slot=2, args=(3401296, 0, 3402547))
    RunEvent(13401350, slot=3, args=(3401297, 0, 3402547))
    RunEvent(13401350, slot=4, args=(3401298, 0, 3402547))
    RunEvent(13401350, slot=5, args=(3401299, 0, 3402547))
    RunEvent(13401350, slot=6, args=(3401300, 0, 3402547))
    RunEvent(13401350, slot=7, args=(3401301, 0, 3402547))
    RunEvent(13401350, slot=8, args=(3401302, 0, 3402547))
    RunEvent(13401350, slot=9, args=(3401303, 0, 3402547))
    RunEvent(13401350, slot=10, args=(3401304, 0, 3402547))
    RunEvent(13400998)


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(13400940)
    RunEvent(13400950, slot=0, args=(3400902, 3400903))


def Event13400010():
    """ 13400010: Event 13400010 """
    DisableNetworkSync()
    DisableObject(3401801)
    DeleteVFX(3403801, erase_root_only=True)
    IfConnectingMultiplayer(-1)
    IfMultiplayer(-1)
    IfFlagOff(-1, 9471)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(3401801)
    CreateVFX(3403801)
    IfConnectingMultiplayer(-2)
    IfMultiplayer(-2)
    IfConditionFalse(1, input_condition=-2)
    IfFlagOn(1, 9471)
    IfConditionTrue(0, input_condition=1)
    Restart()


@RestartOnRest
def Event13400998():
    """ 13400998: Event 13400998 """
    GotoIfFlagOn(Label.L0, 13400999)
    DisableCharacter(3400316)
    DisableCharacter(3400509)
    DisableCharacter(3400550)
    DisableCharacter(3400143)
    DisableCharacter(3400144)
    DisableCharacter(3400142)
    DisableCharacter(3400141)
    DisableCharacter(3400145)
    DisableCharacter(3400146)
    DisableCharacter(3400147)
    DisableCharacter(3400148)
    DisableCharacter(3400155)
    DisableCharacter(3400452)
    DisableCharacter(3400453)
    DisableCharacter(3400461)
    DisableCharacter(3400462)
    DisableCharacter(3400470)
    DisableCharacter(3400471)
    DisableObject(3401180)
    DisableObject(3401181)
    DisableObject(3401182)
    DisableObject(3401183)
    DisableObject(3401184)
    DisableObject(3401185)
    DisableObject(3401186)
    DisableObject(3401187)
    DisableObject(3401188)
    DisableObject(3401189)
    DisableObject(3401190)
    DisableObject(3401191)
    DisableObject(3401192)
    DisableObject(3401193)
    DisableObject(3401194)
    DisableTreasure(3401180)
    DisableTreasure(3401181)
    DisableTreasure(3401182)
    DisableTreasure(3401183)
    DisableTreasure(3401184)
    DisableTreasure(3401185)
    DisableTreasure(3401186)
    DisableTreasure(3401187)
    DisableTreasure(3401188)
    DisableTreasure(3401189)
    DisableTreasure(3401190)
    DisableTreasure(3401191)
    DisableTreasure(3401192)
    DisableTreasure(3401193)
    DisableCharacter(3400920)
    DeleteVFX(3403910, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(3400601)
    DisableCharacter(3400552)
    DisableCharacter(3400511)
    DisableCharacter(3400409)
    DisableCharacter(3400412)
    DisableCharacter(3400413)
    DisableCharacter(3400510)
    DisableCharacter(3400465)
    DisableCharacter(3400466)
    DisableCharacter(3400467)
    DisableCharacter(3400468)
    DisableCharacter(3400469)
    DisableCharacter(3400655)
    DisableObject(3401195)
    DisableObject(3401196)
    DisableObject(3401197)
    DisableObject(3401198)
    DisableObject(3401199)
    DisableObject(3401200)
    DisableObject(3401201)
    DisableObject(3401202)
    DisableObject(3401203)
    DisableObject(3401204)
    DisableObject(3401205)
    DisableObject(3401206)
    DisableObject(3401207)
    DisableTreasure(3401195)
    DisableTreasure(3401196)
    DisableTreasure(3401197)
    DisableTreasure(3401198)
    DisableTreasure(3401199)
    DisableTreasure(3401200)
    DisableTreasure(3401201)
    DisableTreasure(3401202)
    DisableTreasure(3401203)
    DisableTreasure(3401204)
    DisableTreasure(3401205)
    DisableTreasure(3401206)
    DisableTreasure(3401207)


def Event13401250(_, arg_0_3: int, arg_4_7: int):
    """ 13401250: Event 13401250 """
    DisableNetworkSync()
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=5.0)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(arg_0_3, 6, wait_for_completion=True)
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=5.0)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    Restart()


def Event13401350(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13401350: Event 13401350 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(arg_0_3, 6, wait_for_completion=True)
    IfEntityWithinDistance(0, PLAYER, arg_0_3, radius=5.0)

    # --- 0 --- #
    DefineLabel(0)
    WaitRandomFrames(min_frames=0, max_frames=75)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    Restart()


def Event13401500():
    """ 13401500: Event 13401500 """
    GotoIfFlagOn(Label.L0, 9469)
    DisableObject(3400600)
    IfFlagOn(0, 9469)

    # --- 0 --- #
    DefineLabel(0)
    DisableMapPiece(3404200)
    DisableMapPiece(3404201)
    DisableMapPiece(3404202)
    DisableMapPiece(3404203)
    DeleteVFX(3403600, erase_root_only=True)
    DeleteVFX(3403601, erase_root_only=True)
    DeleteVFX(3403602, erase_root_only=True)
    EnableObject(3400600)


def Event13401000():
    """ 13401000: Event 13401000 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 12401000)
    DisableFlag(12401000)
    AddSpecialEffect(PLAYER, 110, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 111, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 112, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 113, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 114, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 115, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 116, affect_npc_part_hp=False)
    SetRespawnPoint(3402958)
    EndIfThisEventOn()
    RunEvent(9350, slot=0, args=(2,))


@RestartOnRest
def Event13404700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13404700: Event 13404700 """
    GotoIfFlagOff(Label.L0, arg_8_11)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagOn(arg_4_7)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010, loop=True)
    IfOnline(1)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfInsideMap(1, game_map=HUNTERS_NIGHTMARE)
    IfCharacterHuman(2, PLAYER)
    IfPlayerSoulLevelGreaterThanOrEqual(2, 30)
    SkipLinesIfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    SkipLinesIfFlagOff(1, arg_16_19)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(arg_0_3, 7011)
    WaitFrames(59)
    EnableAI(arg_0_3)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event13404710(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13404710: Event 13404710 """
    EndIfFlagOn(arg_8_11)
    IfFlagOn(1, arg_4_7)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_8_11)
    IfInsideMap(1, game_map=HUNTERS_NIGHTMARE)
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
def Event13404720(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13404720: Event 13404720 """
    EndIfFlagOn(arg_8_11)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(1, arg_12_15)
    IfFlagOn(-1, arg_8_11)
    IfClientTypeCountComparison(-1, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfOutsideMap(-1, game_map=HUNTERS_NIGHTMARE)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(arg_0_3, 9100)
    ReplanAI(arg_0_3)
    DisableFlag(arg_12_15)
    Restart()


@RestartOnRest
def Event13404730(
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
    """ 13404730: Event 13404730 """
    IfFlagOn(-15, arg_8_11)
    IfFlagOn(-15, arg_12_15)
    IfFlagOn(-15, arg_16_19)
    EndIfConditionTrue(-15)
    IfFlagOn(1, arg_4_7)
    IfFlagOn(1, arg_24_27)
    IfHealthEqual(2, arg_0_3, 0.0)
    IfFlagOn(-1, arg_16_19)
    IfFlagOn(-1, 13404860)
    IfFlagOn(-1, arg_28_31)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_8_11)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-1)
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
def Event13404740():
    """ 13404740: Event 13404740 """
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(-1, 3404000)
    IfStandingOnCollision(-1, 3404001)
    IfStandingOnCollision(-1, 3404002)
    IfStandingOnCollision(-1, 3404003)
    IfStandingOnCollision(-1, 3404004)
    IfStandingOnCollision(-1, 3404005)
    IfStandingOnCollision(-1, 3404006)
    IfStandingOnCollision(-1, 3404007)
    IfStandingOnCollision(-1, 3404008)
    IfStandingOnCollision(-1, 3404009)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13404741)
    IfCharacterHuman(2, PLAYER)
    IfStandingOnCollision(-2, 3404000)
    IfStandingOnCollision(-2, 3404001)
    IfStandingOnCollision(-2, 3404002)
    IfStandingOnCollision(-2, 3404003)
    IfStandingOnCollision(-2, 3404004)
    IfStandingOnCollision(-2, 3404005)
    IfStandingOnCollision(-2, 3404006)
    IfStandingOnCollision(-2, 3404007)
    IfStandingOnCollision(-2, 3404008)
    IfStandingOnCollision(-2, 3404009)
    IfConditionFalse(2, input_condition=-1)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13404741)
    Restart()


@RestartOnRest
def Event13404742():
    """ 13404742: Event 13404742 """
    IfCharacterHuman(1, PLAYER)
    IfStandingOnCollision(-1, 3404020)
    IfStandingOnCollision(-1, 3404021)
    IfStandingOnCollision(-1, 3404022)
    IfStandingOnCollision(-1, 3404023)
    IfStandingOnCollision(-1, 3404024)
    IfStandingOnCollision(-1, 3404025)
    IfStandingOnCollision(-1, 3404026)
    IfStandingOnCollision(-1, 3404027)
    IfStandingOnCollision(-1, 3404028)
    IfStandingOnCollision(-1, 3404029)
    IfStandingOnCollision(-1, 3404030)
    IfStandingOnCollision(-1, 3404031)
    IfStandingOnCollision(-1, 3404032)
    IfStandingOnCollision(-1, 3404033)
    IfStandingOnCollision(-1, 3404034)
    IfStandingOnCollision(-1, 3404035)
    IfStandingOnCollision(-1, 3404036)
    IfStandingOnCollision(-1, 3404037)
    IfStandingOnCollision(-1, 3404038)
    IfStandingOnCollision(-1, 3404039)
    IfStandingOnCollision(-1, 3404040)
    IfStandingOnCollision(-1, 3404041)
    IfStandingOnCollision(-1, 3404042)
    IfStandingOnCollision(-1, 3404043)
    IfStandingOnCollision(-1, 3404044)
    IfStandingOnCollision(-1, 3404045)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13404743)
    IfCharacterHuman(2, PLAYER)
    IfStandingOnCollision(-2, 3404020)
    IfStandingOnCollision(-2, 3404021)
    IfStandingOnCollision(-2, 3404022)
    IfStandingOnCollision(-2, 3404023)
    IfStandingOnCollision(-2, 3404024)
    IfStandingOnCollision(-2, 3404025)
    IfStandingOnCollision(-2, 3404026)
    IfStandingOnCollision(-2, 3404027)
    IfStandingOnCollision(-2, 3404028)
    IfStandingOnCollision(-2, 3404029)
    IfStandingOnCollision(-2, 3404030)
    IfStandingOnCollision(-2, 3404031)
    IfStandingOnCollision(-2, 3404032)
    IfStandingOnCollision(-2, 3404033)
    IfStandingOnCollision(-2, 3404034)
    IfStandingOnCollision(-2, 3404035)
    IfStandingOnCollision(-2, 3404036)
    IfStandingOnCollision(-2, 3404037)
    IfStandingOnCollision(-2, 3404038)
    IfStandingOnCollision(-2, 3404039)
    IfStandingOnCollision(-2, 3404040)
    IfStandingOnCollision(-2, 3404041)
    IfStandingOnCollision(-2, 3404042)
    IfStandingOnCollision(-2, 3404043)
    IfStandingOnCollision(-2, 3404044)
    IfStandingOnCollision(-2, 3404045)
    IfConditionFalse(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13404743)
    Restart()


def Event13401800():
    """ 13401800: Event 13401800 """
    GotoIfFlagOff(Label.L0, 9471)
    DisableCharacter(3400800)
    DisableCharacter(3400801)
    Kill(3400800, award_souls=False)
    Kill(3400801, award_souls=False)
    DisableObject(3401800)
    DeleteVFX(3403800, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, 3400800)
    IfConditionTrue(-1, input_condition=1)
    SkipLinesIfFlagOn(2, 13400999)
    IfCharacterDead(2, 3400801)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3401800)
    DeleteVFX(3403800, erase_root_only=True)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, 2)
    KillBoss(3400800)
    SkipLines(1)
    KillBoss(3400801)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    SkipLinesIfFlagOff(4, 13400999)
    Wait(3.0)
    PlayCutscene(34000040, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    Unknown_2003_27(0)
    AwardAchievement(36)
    RunEvent(9350, slot=0, args=(3,))
    SkipLinesIfFlagOn(2, 6674)
    AwardItemLot(3401800, host_only=False)
    SkipLines(1)
    AwardItemLot(3401802, host_only=False)
    EnableFlag(3400)
    EnableFlag(3401)
    EnableFlag(3402)
    EnableFlag(3403)
    EnableFlag(9471)
    StopPlayLogMeasurement(9340000)
    StopPlayLogMeasurement(9340001)
    StopPlayLogMeasurement(9340010)
    CreatePlayLog(0)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 12, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 12, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 12, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 12, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def Event13404811():
    """ 13404811: Event 13404811 """
    EndIfFlagOn(9471)
    EndIfFlagOn(13401801)
    DisableCharacter(3400800)
    IfFlagOff(1, 13401800)
    IfFlagOff(1, 13401801)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3402805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13404810)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)


def Event13401801():
    """ 13401801: Event 13401801 """
    EndIfFlagOn(9471)
    EndIfThisEventOn()
    IfCharacterType(1, PLAYER, CharacterType.BlackPhantom)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfFlagOff(2, 13401800)
    IfThisEventOff(2)
    IfFlagOn(2, 13404811)
    IfCharacterHuman(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3402805)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(34000020, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(34000020, skippable=False, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(34000020, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    EnableFlag(13404808)
    EnableCharacter(3400800)
    EndIfFlagOn(9344)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9344)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(0, 6001)
    Wait(0.0)


def Event13401802():
    """ 13401802: Event 13401802 """
    EndIfFlagOn(13401803)
    EndIfFlagOn(13401800)
    EnableInvincibility(3400810)
    IfFlagOn(0, 13401801)
    AddSpecialEffect(3400810, 5401, affect_npc_part_hp=False)
    DisableInvincibility(3400810)
    ForceAnimation(3400810, 3000)
    IfCharacterAlive(1, 3400810)
    IfFlagOn(1, 13401800)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(3400810, 7000)


@RestartOnRest
def Event13401803():
    """ 13401803: Event 13401803 """
    GotoIfThisEventOff(Label.L0)
    DropMandatoryTreasure(3400810)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3400810)
    Wait(0.0)


def Event13401804():
    """ 13401804: Event 13401804 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 13404808)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(3400800)
    EnableFlag(13404808)
    EnableFlag(13401801)


def Event13404800():
    """ 13404800: Event 13404800 """
    EndIfFlagOn(9471)
    GotoIfFlagOn(Label.L0, 13401801)
    SkipLinesIfClient(2)
    DisableObject(3401800)
    DeleteVFX(3403800, erase_root_only=False)
    IfFlagOff(1, 13401800)
    IfFlagOn(1, 13401801)
    IfConditionTrue(0, input_condition=1)
    EnableObject(3401800)
    CreateVFX(3403800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 13401800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=3400800, entity=3401800)
    IfFlagOn(3, 13401800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 3402800, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3402801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(13404808)
    Restart()


def Event13404801():
    """ 13404801: Event 13404801 """
    DisableNetworkSync()
    EndIfFlagOn(9471)
    IfFlagOff(1, 13401800)
    IfFlagOn(1, 13401801)
    IfFlagOn(1, 13404808)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParam(1, action_button_id=3400800, entity=3401800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3402800, animation=101130, wait_for_completion=True)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=3402801)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(13404809)
    Restart()


def Event13404802():
    """ 13404802: Event 13404802 """
    EndIfFlagOn(9471)
    DisableAI(3400800)
    DisableAI(3400801)
    DisableHealthBar(3400800)
    DisableHealthBar(3400801)
    ReferDamageToEntity(3400800, 3400801)
    SkipLinesIfFlagOff(2, 13400999)
    AddSpecialEffect(3400800, 8040, affect_npc_part_hp=False)
    AddSpecialEffect(3400801, 8040, affect_npc_part_hp=False)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 13404808)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagOn(1, 13404810)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3400800, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3400801, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13404810)
    EnableFlag(13404808)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3400800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(3400801, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3400800)
    AdaptSpecialEffectHealthChangeToNPCPart(3400801)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3400800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(3400801, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3400800)
    AdaptSpecialEffectHealthChangeToNPCPart(3400801)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    SkipLinesIfFlagOn(5, 13404825)
    EnableAI(3400800)
    SetNetworkUpdateRate(3400800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3400801, is_fixed=True, update_rate=CharacterUpdateRate.EveryTwoFrames)
    EnableBossHealthBar(3400800, name=451000, slot=0)
    SkipLines(4)
    EnableAI(3400801)
    SetNetworkUpdateRate(3400800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(3400801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3400801, name=451005, slot=0)
    CreatePlayLog(46)
    StartPlayLogMeasurement(3400010, 62, overwrite=True)


def Event13404803():
    """ 13404803: Event 13404803 """
    DisableNetworkSync()
    DisableSoundEvent(3403802)
    DisableSoundEvent(3403803)
    EndIfFlagOn(9471)
    GotoIfThisEventOn(Label.L0)
    IfFlagOff(1, 13401800)
    IfFlagOn(1, 13404802)
    SkipLinesIfHost(1)
    IfFlagOn(1, 13404809)
    IfCharacterInsideRegion(1, PLAYER, region=3402802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(3403802)
    IfFlagOn(2, 13404824)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 13401800)
    IfFlagOn(2, 13404802)
    SkipLinesIfHost(1)
    IfFlagOn(2, 13404809)
    IfCharacterInsideRegion(2, PLAYER, region=3402802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(3403802)
    WaitFrames(0)
    EnableBossMusic(3403803)


def Event13404804():
    """ 13404804: Event 13404804 """
    DisableNetworkSync()
    EndIfFlagOn(9471)
    IfFlagOn(0, 13404825)
    IfCharacterAlive(3, 3400801)
    IfEntityWithinDistance(3, PLAYER, 3400801, radius=9.0)
    IfConditionTrue(0, input_condition=3)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(4, 3400801)
    IfEntityBeyondDistance(4, PLAYER, 3400801, radius=12.0)
    IfConditionTrue(0, input_condition=4)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Restart()


def Event13404805():
    """ 13404805: Event 13404805 """
    DisableNetworkSync()
    EndIfFlagOn(9471)
    IfFlagOn(0, 13401800)
    DisableBossMusic(3403802)
    DisableBossMusic(3403803)
    DisableBossMusic(-1)


def Event13404806():
    """ 13404806: Event 13404806 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 3401800, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event13404807():
    """ 13404807: Event 13404807 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, 3401800, radius=6.0)
    IfEntityWithinDistance(1, PLAYER, 3401800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def Event13404820():
    """ 13404820: Event 13404820 """
    EndIfFlagOn(9471)
    IfFlagOn(1, 13400999)
    IfHealthLessThan(1, 3400800, 0.8999999761581421)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOff(2, 13400999)
    IfHealthLessThan(2, 3400800, 0.8999999761581421)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfHasTAEEvent(3, 3400800, tae_event_id=10)
    IfHasTAEEvent(4, 3400800, tae_event_id=20)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    AICommand(3400800, command_id=100, slot=0)
    IfHasTAEEvent(0, 3400800, tae_event_id=20)
    AICommand(3400800, command_id=-1, slot=0)


def Event13404821():
    """ 13404821: Event 13404821 """
    EndIfFlagOn(9471)
    IfFlagOn(1, 13400999)
    IfHealthLessThan(1, 3400800, 0.800000011920929)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOff(2, 13400999)
    IfHealthLessThan(2, 3400800, 0.8500000238418579)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfHasTAEEvent(3, 3400800, tae_event_id=10)
    IfFlagOn(3, 13404820)
    IfHasTAEEvent(4, 3400800, tae_event_id=30)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    AICommand(3400800, command_id=101, slot=0)
    IfHasTAEEvent(0, 3400800, tae_event_id=30)
    AICommand(3400800, command_id=-1, slot=0)


def Event13404822():
    """ 13404822: Event 13404822 """
    EndIfFlagOn(9471)
    IfFlagOn(1, 13400999)
    IfHealthLessThan(1, 3400800, 0.699999988079071)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOff(2, 13400999)
    IfHealthLessThan(2, 3400800, 0.800000011920929)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfHasTAEEvent(3, 3400800, tae_event_id=10)
    IfFlagOn(3, 13404821)
    IfHasTAEEvent(4, 3400800, tae_event_id=40)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    AICommand(3400800, command_id=102, slot=0)
    IfHasTAEEvent(0, 3400800, tae_event_id=40)
    AICommand(3400800, command_id=-1, slot=0)


def Event13404823():
    """ 13404823: Event 13404823 """
    EndIfFlagOn(9471)
    IfFlagOn(1, 13400999)
    IfHealthLessThan(1, 3400800, 0.5)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOff(2, 13400999)
    IfHealthLessThan(2, 3400800, 0.75)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfHasTAEEvent(3, 3400800, tae_event_id=10)
    IfFlagOn(3, 13404822)
    IfHasTAEEvent(4, 3400800, tae_event_id=50)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    AICommand(3400800, command_id=103, slot=0)
    IfHasTAEEvent(0, 3400800, tae_event_id=50)
    AICommand(3400800, command_id=-1, slot=0)


def Event13404824():
    """ 13404824: Event 13404824 """
    EndIfFlagOn(9471)
    EndIfFlagOn(13404825)
    IfHealthLessThan(1, 3400800, 0.5)
    IfHealthGreaterThan(1, 3400800, 0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)


def Event13404825():
    """ 13404825: Event 13404825 """
    EndIfFlagOn(9471)
    GotoIfThisEventOff(Label.L0)
    DisableCharacter(3400800)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(3400801)
    DisableAnimations(3400801)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 13404824)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        34000030,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=3402807,
        move_to_map=HUNTERS_NIGHTMARE,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        34000030,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=3402807,
        move_to_map=HUNTERS_NIGHTMARE,
    )
    SkipLines(1)
    PlayCutscene(34000030, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableBossHealthBar(3400800, name=451000, slot=0)
    DisableFlag(9180)
    DisableCharacter(3400800)
    SetNetworkUpdateRate(3400801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3400800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    Move(3400800, destination=3402900, destination_type=CoordEntityType.Region)
    Move(3400801, destination=3402806, destination_type=CoordEntityType.Region, copy_draw_parent=3400800)
    EnableGravity(3400801)
    EnableAnimations(3400801)
    ForceAnimation(3400801, 7000)
    WaitFrames(96)
    CancelSpecialEffect(3400801, 5300)
    AddSpecialEffect(3400801, 5333, affect_npc_part_hp=False)
    EnableAI(3400801)
    EnableBossHealthBar(3400801, name=451005, slot=0)


def Event13404830(
    _,
    arg_0_1: short,
    arg_4_7: int,
    arg_8_9: short,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 13404830: Event 13404830 """
    EndIfFlagOn(9471)
    CreateNPCPart(
        3400800,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(3400800, npc_part_id=arg_4_7, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, 3400800, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(-1, 3400800, 0.0)
    IfFlagOn(-1, 13404825)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(-1)
    CreateNPCPart(
        3400800,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=9999999,
        damage_correction=1.5,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(3400800, npc_part_id=arg_4_7, material_sfx_id=73, material_vfx_id=73)
    ForceAnimation(3400800, arg_20_23)
    AddSpecialEffect(3400800, arg_16_19, affect_npc_part_hp=False)
    WaitFrames(arg_24_27)
    IfFramesElapsed(3, arg_24_27)
    IfHealthLessThanOrEqual(-3, 3400800, 0.0)
    IfFlagOn(-3, 13404825)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(-4, input_condition=-3)
    IfConditionTrue(0, input_condition=-4)
    EndIfFinishedConditionTrue(-3)
    ReplanAI(3400800)
    IfTimeElapsed(4, 5.0)
    IfHealthLessThanOrEqual(-5, 3400800, 0.0)
    IfFlagOn(-5, 13404825)
    IfConditionTrue(-6, input_condition=4)
    IfConditionTrue(-6, input_condition=-5)
    IfConditionTrue(0, input_condition=-6)
    EndIfFinishedConditionTrue(-5)
    SetNPCPartHealth(3400800, npc_part_id=arg_4_7, desired_health=-1, overwrite_max=True)
    CancelSpecialEffect(3400800, arg_16_19)
    WaitFrames(10)
    IfFramesElapsed(5, 10)
    IfHealthLessThanOrEqual(-7, 3400800, 0.0)
    IfFlagOn(-7, 13404825)
    IfConditionTrue(-8, input_condition=5)
    IfConditionTrue(-8, input_condition=-7)
    IfConditionTrue(0, input_condition=-8)
    EndIfFinishedConditionTrue(-7)
    Restart()


def Event13404835():
    """ 13404835: Event 13404835 """
    EndIfFlagOn(9471)
    IfHealthLessThan(1, 3400801, 0.3499999940395355)
    IfHealthGreaterThan(1, 3400801, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(3400801, 7002)
    AICommand(3400801, command_id=110, slot=0)
    ReplanAI(3400801)
    IfHealthLessThan(3, 3400801, 0.06700000166893005)
    IfHealthGreaterThan(3, 3400801, 0.0)
    IfConditionTrue(0, input_condition=3)
    ForceAnimation(3400801, 7003)
    IfHealthLessThan(4, 3400801, 0.032999999821186066)
    IfHealthGreaterThan(4, 3400801, 0.0)
    IfConditionTrue(0, input_condition=4)
    ForceAnimation(3400801, 7002)


def Event13404840():
    """ 13404840: Event 13404840 """
    EndIfFlagOn(9471)
    IfHasTAEEvent(0, 3400800, tae_event_id=100)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(0.5)
    DisableCharacter(3400800)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(0.10000000149011612)
    CreateTemporaryVFX(645114, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(1.2000000476837158)
    EnableCharacter(3400800)
    Move(3400800, destination=10000, destination_type=CoordEntityType.Character, model_point=236, short_move=True)
    ForceAnimation(3400800, 3017)
    Restart()


def Event13404841():
    """ 13404841: Event 13404841 """
    EndIfFlagOn(9471)
    IfHasTAEEvent(0, 3400801, tae_event_id=300)
    AICommand(3400801, command_id=-1, slot=0)
    ReplanAI(3400801)


def Event13401850():
    """ 13401850: Event 13401850 """
    GotoIfThisEventOff(Label.L0)
    DisableSoundEvent(3403802)
    DisableSoundEvent(3403803)
    DisableCharacter(3400850)
    Kill(3400850, award_souls=True)
    DisableObject(3401850)
    DeleteVFX(3403850, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3400850)
    EnableFlag(3400)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3401850)
    DeleteVFX(3403850, erase_root_only=True)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Wait(3.0)
    KillBoss(3400850)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    AwardAchievement(39)
    RunEvent(9350, slot=0, args=(3,))
    SkipLinesIfFlagOn(2, 6673)
    AwardItemLot(3401850, host_only=False)
    SkipLines(1)
    AwardItemLot(3401852, host_only=False)
    EnableFlag(3400)
    EnableFlag(3401)
    EnableFlag(3402)
    EnableFlag(3403)
    StopPlayLogMeasurement(3400020)
    StopPlayLogMeasurement(3400021)
    StopPlayLogMeasurement(3400030)
    CreatePlayLog(0)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 80, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 80, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 80, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 80, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


@RestartOnRest
def Event13404861():
    """ 13404861: Event 13404861 """
    EndIfFlagOn(13401850)
    GotoIfFlagOff(Label.L0, 13401851)
    Move(3400850, destination=3402853, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacterCollision(3400850)
    DisableGravity(3400850)
    EnableInvincibility(3400850)
    ForceAnimation(3400850, 7002, loop=True)
    IfFlagOff(1, 13401850)
    IfFlagOff(1, 13401851)
    IfPlayerHasGood(1, 4014, including_box=False)
    IfCharacterInsideRegion(1, PLAYER, region=3402855)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13404860)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)


@RestartOnRest
def Event13401851():
    """ 13401851: Event 13401851 """
    EndIfFlagOn(13401850)
    EndIfThisEventOn()
    IfCharacterType(1, PLAYER, CharacterType.BlackPhantom)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfFlagOff(2, 13401850)
    IfFlagOff(2, 13401851)
    IfFlagOn(2, 13404861)
    IfPlayerHasGood(2, 4014, including_box=False)
    IfCharacterInsideRegion(2, PLAYER, region=3402855)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(
        34000010,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=3402856,
        move_to_map=HUNTERS_NIGHTMARE,
    )
    SkipLines(4)
    SkipLinesIfClient(2)
    PlayCutscene(
        34000010,
        skippable=False,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=3402856,
        move_to_map=HUNTERS_NIGHTMARE,
    )
    SkipLines(1)
    PlayCutscene(34000010, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    EnableFlag(13404858)
    Move(3400850, destination=3402853, destination_type=CoordEntityType.Region, short_move=True)
    EnableGravity(3400850)
    DisableInvincibility(3400850)
    EnableCharacterCollision(3400850)
    ForceAnimation(3400850, 3029)
    EndIfFlagOn(9302)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9302)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(0, 6001)
    Wait(0.0)


def Event13401853():
    """ 13401853: Event 13401853 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 13404858)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableGravity(3400850)
    DisableInvincibility(3400850)
    EnableCharacterCollision(3400850)
    EnableFlag(13404858)
    EnableFlag(13401851)


def Event13404850():
    """ 13404850: Event 13404850 """
    EndIfFlagOn(13401850)
    GotoIfFlagOn(Label.L0, 13401851)
    SkipLinesIfClient(2)
    DisableObject(3401850)
    DeleteVFX(3403850, erase_root_only=False)
    IfFlagOff(1, 13401850)
    IfFlagOn(1, 13401851)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableObject(3401850)
    CreateVFX(3403850)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(3, PLAYER)
    IfActionButtonParam(3, action_button_id=3400850, entity=3401850)
    IfFlagOff(3, 13401850)
    IfFlagOn(4, 13401850)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    RotateToFaceEntity(PLAYER, 3402850, animation=101130)
    IfCharacterHuman(5, PLAYER)
    IfCharacterInsideRegion(5, PLAYER, region=3402851)
    IfCharacterHuman(6, PLAYER)
    IfTimeElapsed(6, 2.0)
    IfConditionTrue(-3, input_condition=5)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(1, 6)
    EnableFlag(13404858)
    Restart()


def Event13404851():
    """ 13404851: Event 13404851 """
    DisableNetworkSync()
    EndIfFlagOn(13401850)
    IfFlagOff(1, 13401850)
    IfFlagOn(1, 13401851)
    IfFlagOn(1, 13404858)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParam(1, action_button_id=3400850, entity=3401850)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3402850, animation=101130)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=3402851)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(13404859)
    Restart()


@RestartOnRest
def Event13404852():
    """ 13404852: Event 13404852 """
    EndIfFlagOn(13401850)
    DisableAI(3400850)
    DisableHealthBar(3400850)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 13404858)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagOn(1, 13404860)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3400850, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13404860)
    EnableFlag(13404858)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3400850, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3400850)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3400850, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3400850)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(3400850)
    EnableBossHealthBar(3400850, name=450000, slot=0)
    CreatePlayLog(46)
    StartPlayLogMeasurement(3400030, 62, overwrite=True)


def Event13404853():
    """ 13404853: Event 13404853 """
    DisableNetworkSync()
    DisableSoundEvent(3403852)
    DisableSoundEvent(3403853)
    EndIfFlagOn(13401850)
    GotoIfThisEventOn(Label.L0)
    IfFlagOff(1, 13401850)
    IfFlagOn(1, 13404852)
    SkipLinesIfHost(1)
    IfFlagOn(1, 13404859)
    IfCharacterInsideRegion(1, PLAYER, region=3402852)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(3403852)
    IfHasTAEEvent(2, 3400850, tae_event_id=400)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 13401850)
    IfFlagOn(2, 13404852)
    SkipLinesIfHost(1)
    IfFlagOn(2, 13404859)
    IfCharacterInsideRegion(2, PLAYER, region=3402852)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(3403852)
    WaitFrames(0)
    EnableBossMusic(3403853)


def Event13404854():
    """ 13404854: Event 13404854 """
    DisableNetworkSync()
    EndIfFlagOn(13401850)
    IfCharacterAlive(1, 3400850)
    IfEntityWithinDistance(1, PLAYER, 3400850, radius=14.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(2, 3400850)
    IfEntityBeyondDistance(2, PLAYER, 3400850, radius=17.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=0)
    Restart()


def Event13404855():
    """ 13404855: Event 13404855 """
    DisableNetworkSync()
    EndIfFlagOn(13401850)
    IfFlagOn(0, 13401850)
    DisableBossMusic(3403852)
    DisableBossMusic(3403853)
    DisableBossMusic(-1)


def Event13404856():
    """ 13404856: Event 13404856 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 3401850, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event13404857():
    """ 13404857: Event 13404857 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, 3401850, radius=6.0)
    IfEntityWithinDistance(1, PLAYER, 3401850, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


@RestartOnRest
def Event13404870(
    _,
    arg_0_1: short,
    arg_4_7: int,
    arg_8_9: short,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 13404870: Event 13404870 """
    EndIfFlagOn(13401850)
    CreateNPCPart(
        3400850,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_20_23,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(3400850, npc_part_id=arg_4_7, material_sfx_id=64, material_vfx_id=64)
    IfCharacterPartHealthLessThanOrEqual(1, 3400850, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(2, 3400850, 0.0)
    IfCharacterHasSpecialEffect(3, 3400850, 5402)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(
        3400850,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(3400850, npc_part_id=arg_4_7, material_sfx_id=65, material_vfx_id=65)
    ForceAnimation(3400850, arg_24_27)
    AddSpecialEffect(3400850, arg_12_15, affect_npc_part_hp=False)
    CancelSpecialEffect(3400850, arg_16_19)
    ReplanAI(3400850)
    IfTimeElapsed(4, 30.0)
    IfCharacterHasSpecialEffect(5, 3400850, 5402)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(5)
    AICommand(3400850, command_id=100, slot=1)
    ReplanAI(3400850)
    IfHasTAEEvent(6, 3400850, tae_event_id=300)
    IfCharacterHasSpecialEffect(7, 3400850, 5402)
    IfConditionTrue(-3, input_condition=6)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=7)
    SetNPCPartHealth(3400850, npc_part_id=arg_4_7, desired_health=-1, overwrite_max=True)
    CancelSpecialEffect(3400850, arg_12_15)
    AddSpecialEffect(3400850, arg_16_19, affect_npc_part_hp=False)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(3400850, command_id=-1, slot=1)
    ReplanAI(3400850)
    WaitFrames(10)
    Restart()


def Event13404875():
    """ 13404875: Event 13404875 """
    GotoIfThisEventOn(Label.L0)
    IfHasTAEEvent(0, 3400850, tae_event_id=400)

    # --- 0 --- #
    DefineLabel(0)
    SetCollisionMask(3400850, bit_index=10, switch_type=OnOffChange.Off)


def Event13401200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13401200: Event 13401200 """
    DisableNetworkSync()
    EndIfFlagOn(arg_8_11)
    IfActionButtonParam(1, action_button_id=arg_0_3, entity=arg_4_7)
    IfFlagOn(2, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(
        10010161,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(0.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)
    Restart()


def Event13401210(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13401210: Event 13401210 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_0_3, arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    Wait(0.0)


def Event13401220():
    """ 13401220: Event 13401220 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(3401100, 1)
    DisableObjectActivation(3401110, obj_act_id=3400020)
    NotifyDoorEventSoundDampening(3401100, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=13400002)
    DisableObjectActivation(3401110, obj_act_id=3400020)
    ForceAnimation(3401100, 1)
    Wait(0.0)


def Event13400100():
    """ 13400100: Event 13400100 """
    EndIfThisEventOn()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfStandingOnCollision(0, 3404000)
    RunEvent(9350, slot=0, args=(2,))


@RestartOnRest
def Event13400220(_, arg_0_3: int, arg_4_7: int):
    """ 13400220: Event 13400220 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@RestartOnRest
def Event13400310(_, arg_0_3: int, arg_4_7: int):
    """ 13400310: Event 13400310 """
    DisableGravity(arg_0_3)
    GotoIfThisEventSlotOff(Label.L0)
    ForceAnimation(arg_0_3, 7004, loop=True, skip_transition=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 7005, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 7003, wait_for_completion=True)


@RestartOnRest
def Event13400320():
    """ 13400320: Event 13400320 """
    EndIfFlagOn(9470)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    CreateObjectVFX(900201, obj=3401500, model_point=200)
    IfActionButtonParam(0, action_button_id=3400100, entity=3401500)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(3401810, host_only=False)
    DeleteObjectVFX(3401500, erase_root=True)


@RestartOnRest
def Event13400330(_, arg_0_3: int):
    """ 13400330: Event 13400330 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    Wait(0.0)


@RestartOnRest
def Event13404799():
    """ 13404799: Event 13404799 """
    CreateProjectileOwner(3400799)


@RestartOnRest
def Event13405100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13405100: Event 13405100 """
    WaitFrames(1)
    IfCharacterDead(-10, 3400206)
    IfCharacterDead(-10, 3400205)
    IfObjectDestroyed(-10, 3401401)
    IfThisEventSlotOn(-10)
    GotoIfConditionTrue(Label.L0, input_condition=-10)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    RemoveObjectFlag(13405101)
    DeleteObjectVFX(arg_0_3, erase_root=True)
    EnableObject(3401401)
    DisableObject(arg_0_3)
    DestroyObject(3401401)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableObject(3401401)
    ForceAnimation(arg_0_3, 0, loop=True)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(2, PLAYER, region=arg_8_11)
    IfFlagOn(3, 13405101)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(13405101)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    IfEntityWithinDistance(-3, arg_0_3, PLAYER, radius=22.0)
    IfTimeElapsed(-3, 4.0)
    IfConditionTrue(0, input_condition=-3)

    # --- 2 --- #
    DefineLabel(2)
    CreateObjectVFX(900260, obj=arg_0_3, model_point=100)
    CreateHazard(
        13405101,
        arg_0_3,
        model_point=100,
        behavior_param_id=6291,
        target_type=DamageTargetType.Character,
        radius=1.600000023841858,
        life=9999.0,
        repetition_time=0.0,
    )
    PlaySoundEffect(anchor_entity=3402531, sound_type=SoundType.a_Ambient, sound_id=411005001)
    WaitFrames(30)
    ForceAnimation(arg_0_3, 1, wait_for_completion=True)
    ForceAnimation(arg_0_3, 2, loop=True)
    RemoveObjectFlag(13405101)
    DeleteObjectVFX(arg_0_3, erase_root=True)
    EnableObject(3401401)
    DisableObject(arg_0_3)
    DestroyObject(3401401)


@RestartOnRest
def Event13405103():
    """ 13405103: Event 13405103 """
    IfThisEventSlotOn(-10)
    IfCharacterDead(-10, 3400551)
    GotoIfConditionTrue(Label.L0, input_condition=-10)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(3401010, 11, loop=True)
    EndOfAnimation(3401010, 11)
    EnableAI(3400551)
    SetNest(3400551, 3402310)
    ReplanAI(3400551)
    DisableObjectActivation(3401010, obj_act_id=3400000)
    NotifyDoorEventSoundDampening(3401010, state=DoorState.DoorOpening)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableAI(3400551)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=3402300)
    IfEntityWithinDistance(-2, PLAYER, 3400551, radius=7.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=3400551)
    IfConditionTrue(0, input_condition=-3)
    PlaySoundEffect(anchor_entity=3402300, sound_type=SoundType.a_Ambient, sound_id=340000000)
    ForceAnimation(3400551, 7015)
    ForceAnimation(3401010, 10)
    WaitFrames(260)
    EnableAI(3400551)
    SetNest(3400551, 3402310)
    ReplanAI(3400551)
    DisableObjectActivation(3401010, obj_act_id=3400000)


@RestartOnRest
def Event13405105(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13405105: Event 13405105 """
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    IfObjectNotDestroyed(0, arg_8_11)
    ForceAnimation(arg_8_11, 1)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_8_11,
        model_point=200,
        behavior_id=6280,
        launch_angle_x=arg_12_15,
        launch_angle_y=arg_16_19,
        launch_angle_z=arg_20_23,
    )
    WaitFrames(2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_8_11,
        model_point=200,
        behavior_id=6281,
        launch_angle_x=arg_12_15,
        launch_angle_y=arg_16_19,
        launch_angle_z=arg_20_23,
    )
    WaitFrames(2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_8_11,
        model_point=200,
        behavior_id=6282,
        launch_angle_x=arg_12_15,
        launch_angle_y=arg_16_19,
        launch_angle_z=arg_20_23,
    )
    WaitFrames(2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_8_11,
        model_point=200,
        behavior_id=6283,
        launch_angle_x=arg_12_15,
        launch_angle_y=arg_16_19,
        launch_angle_z=arg_20_23,
    )
    WaitFrames(2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_8_11,
        model_point=200,
        behavior_id=6280,
        launch_angle_x=arg_12_15,
        launch_angle_y=arg_16_19,
        launch_angle_z=arg_20_23,
    )
    WaitFrames(60)
    IfAllPlayersOutsideRegion(0, region=arg_0_3)
    ForceAnimation(arg_4_7, 0, loop=True)
    Restart()


@RestartOnRest
def Event13405110():
    """ 13405110: Event 13405110 """
    GotoIfThisEventSlotOff(Label.L0)
    SetAIParamID(3400200, 263757)
    ReplanAI(3400200)
    SetAIParamID(3400406, 400002)
    ReplanAI(3400406)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHasTAEEvent(0, 3400200, tae_event_id=10)
    ReplanAI(3400406)
    SetAIParamID(3400406, 400018)
    SetAIParamID(3400200, 263757)
    ReplanAI(3400200)
    SkipLinesIfEqual(1, left=1, right=0)
    AddSpecialEffect(3400406, 5000, affect_npc_part_hp=False)
    ChangePatrolBehavior(3400406, patrol_information_id=3403350)
    Wait(3.0)
    SetAIParamID(3400406, 400002)
    ReplanAI(3400406)


@RestartOnRest
def Event13405112():
    """ 13405112: Event 13405112 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableObject(3401320)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=3402533)
    ForceAnimation(3401352, 1, wait_for_completion=True)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=3401320,
        model_point=10,
        behavior_id=6290,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    WaitFrames(80)
    DisableObject(3401320)


@RestartOnRest
def Event13405113(
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
    """ 13405113: Event 13405113 """
    IfFlagOn(1, arg_4_7)
    IfObjectNotDestroyed(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    IfFramesElapsed(0, arg_8_11)
    ForceAnimation(arg_0_3, 1)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_16_19,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_20_23,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_24_27,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_28_31,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_16_19,
        launch_angle_x=340,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    IfFramesElapsed(0, arg_12_15)
    Restart()


@RestartOnRest
def Event13405115(
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
    """ 13405115: Event 13405115 """
    IfFlagOn(1, arg_4_7)
    IfObjectNotDestroyed(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    IfFramesElapsed(0, arg_8_11)
    ForceAnimation(arg_0_3, 1)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_16_19,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_20_23,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_24_27,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_28_31,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=200,
        behavior_id=arg_16_19,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfFramesElapsed(0, 2)
    IfFramesElapsed(0, arg_12_15)
    Restart()


@RestartOnRest
def Event13405140(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13405140: Event 13405140 """
    IfCharacterAlive(1, arg_0_3)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_12_15)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_16_19, 1, wait_for_completion=True)
    IfFramesElapsed(0, arg_20_23)
    IfCharacterAlive(2, arg_0_3)
    IfCharacterInsideRegion(2, arg_0_3, region=arg_12_15)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    RestartIfConditionFalse(2)
    EnableFlag(arg_8_11)
    IfCharacterDead(-1, arg_0_3)
    IfCharacterOutsideRegion(-1, arg_0_3, region=arg_12_15)
    IfCharacterOutsideRegion(-1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(10)
    ForceAnimation(arg_16_19, 0, loop=True)
    DisableFlag(arg_8_11)
    Restart()


@RestartOnRest
def Event13405145(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13405145: Event 13405145 """
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    EnableFlag(arg_8_11)
    IfAllPlayersOutsideRegion(0, region=arg_0_3)
    WaitFrames(10)
    ForceAnimation(arg_4_7, 0, loop=True)
    DisableFlag(arg_8_11)
    Restart()


@RestartOnRest
def Event13405155(_, arg_0_3: int):
    """ 13405155: Event 13405155 """
    GotoIfThisEventSlotOff(Label.L0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    PlaySoundEffect(anchor_entity=3402515, sound_type=SoundType.a_Ambient, sound_id=411005002)


@RestartOnRest
def Event13405160(_, arg_0_3: int):
    """ 13405160: Event 13405160 """
    EndIfThisEventSlotOn()
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, damage_type=DamageType.Fire)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, damage_type=DamageType.NoType)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Magic)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Lightning)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Blunt)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Slash)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, damage_type=DamageType.Thrust)
    IfConditionTrue(2, input_condition=-2)
    IfObjectHealthValueComparison(2, arg_0_3, ComparisonType.LessThanOrEqual, 999)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=3400799,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6292,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)


@RestartOnRest
def Event13405200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13405200: Event 13405200 """
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Normal)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfHealthLessThanOrEqual(3, arg_0_3, 0.0)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(3)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterOutsideRegion(2, arg_0_3, region=arg_12_15)
    IfHealthLessThanOrEqual(4, arg_0_3, 0.0)
    IfConditionTrue(-2, input_condition=-1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    RestartIfFinishedConditionTrue(2)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event13405211(_, arg_0_3: int):
    """ 13405211: Event 13405211 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.a_Ambient, sound_id=340000000)


@RestartOnRest
def Event13405216(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float, arg_20_23: int):
    """ 13405216: Event 13405216 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterInsideRegion(-2, 3400316, region=arg_4_7)
    IfCharacterInsideRegion(-2, 3400316, region=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_16_19)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfEqual(1, left=arg_20_23, right=0)
    AddSpecialEffect(arg_0_3, 5000, affect_npc_part_hp=False)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_12_15)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13405218():
    """ 13405218: Event 13405218 """
    GotoIfThisEventOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3402553)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    DisableMapCollision(3404250)


@RestartOnRest
def Event13405220(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: float,
    arg_28_31: float,
):
    """ 13405220: Event 13405220 """
    GotoIfThisEventSlotOn(Label.L0)
    WaitRandomFrames(min_frames=0, max_frames=180)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=arg_20_23)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    WaitRandomSeconds(min_seconds=arg_24_27, max_seconds=arg_28_31)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event13405300(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 13405300: Event 13405300 """
    EndIfThisEventSlotOn()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    Wait(arg_12_15)
    EnableAI(arg_0_3)


@RestartOnRest
def Event13405350(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float, arg_20_23: int):
    """ 13405350: Event 13405350 """
    GotoIfThisEventSlotOn(Label.L0)
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
    SkipLinesIfEqual(1, left=arg_20_23, right=0)
    AddSpecialEffect(arg_0_3, 5000, affect_npc_part_hp=False)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_12_15)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13405480(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: float, arg_20_20: uchar):
    """ 13405480: Event 13405480 """
    GotoIfThisEventSlotOff(Label.L0)
    EnableAI(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetAIState(arg_0_3, state=arg_20_20)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(3, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(4, attacked_entity=arg_0_3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionTrue(3, 3)
    SkipLinesIfFinishedConditionTrue(2, 4)
    Wait(arg_16_19)
    ForceAnimation(arg_0_3, arg_12_15)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13405510(_, arg_0_3: int):
    """ 13405510: Event 13405510 """
    IfCharacterDead(0, arg_0_3)
    IncrementEventValue(13405500, bit_count=4, max_value=15)


@RestartOnRest
def Event13405520(_, arg_0_3: int, arg_4_7: int):
    """ 13405520: Event 13405520 """
    IfEventValueComparison(0, 13405500, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=4)
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=0.5)
    AICommand(arg_0_3, command_id=100, slot=2)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13405530(_, arg_0_3: int, arg_4_7: int):
    """ 13405530: Event 13405530 """
    IfEventValueComparison(0, 13405500, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=0.5)
    AICommand(arg_0_3, command_id=100, slot=3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13405540(_, arg_0_3: int, arg_4_7: int, arg_8_11: uint, arg_12_15: int, arg_16_19: float):
    """ 13405540: Event 13405540 """
    IfEventValueComparison(0, 13405500, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=arg_8_11)
    SkipLinesIfEqual(1, left=arg_12_15, right=0)
    AddSpecialEffect(arg_0_3, 5000, affect_npc_part_hp=False)
    Wait(arg_16_19)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_4_7)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13405550(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: float,
    arg_24_27: float,
):
    """ 13405550: Event 13405550 """
    GotoIfThisEventSlotOn(Label.L0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfEventValueComparison(0, 13405500, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    WaitRandomSeconds(min_seconds=arg_20_23, max_seconds=arg_24_27)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event13405570(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar):
    """ 13405570: Event 13405570 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=0.5)
    ReplanAI(arg_0_3)
    AICommand(arg_0_3, command_id=arg_12_15, slot=arg_16_16)


@RestartOnRest
def Event13405610(_, arg_0_3: int):
    """ 13405610: Event 13405610 """
    IfCharacterDead(0, arg_0_3)
    IncrementEventValue(13405600, bit_count=4, max_value=15)


@RestartOnRest
def Event13405620(_, arg_0_3: int, arg_4_7: int):
    """ 13405620: Event 13405620 """
    IfEventValueComparison(0, 13405600, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=4)
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=0.5)
    AICommand(arg_0_3, command_id=100, slot=2)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13405630(_, arg_0_3: int, arg_4_7: int):
    """ 13405630: Event 13405630 """
    IfEventValueComparison(0, 13405600, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=0.5)
    AICommand(arg_0_3, command_id=100, slot=3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13405640(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: float,
    arg_24_27: float,
):
    """ 13405640: Event 13405640 """
    GotoIfThisEventSlotOn(Label.L0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_8_11)
    IfEventValueComparison(0, 13405600, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=1)
    WaitRandomSeconds(min_seconds=arg_20_23, max_seconds=arg_24_27)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_16_19)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13405650(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: float,
    arg_24_27: float,
):
    """ 13405650: Event 13405650 """
    GotoIfThisEventSlotOn(Label.L0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfEventValueComparison(0, 13405600, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=2)
    WaitRandomSeconds(min_seconds=arg_20_23, max_seconds=arg_24_27)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event13405680(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 13405680: Event 13405680 """
    IfHasTAEEvent(1, arg_0_3, tae_event_id=10)
    IfEntityWithinDistance(1, arg_0_3, arg_4_7, radius=arg_8_11)
    IfCharacterAlive(1, arg_4_7)
    IfCharacterBackreadEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_4_7, command_id=200, slot=1)
    IfHasTAEEvent(0, arg_4_7, tae_event_id=20)
    AddSpecialEffect(arg_4_7, 5645, affect_npc_part_hp=False)
    AICommand(arg_4_7, command_id=-1, slot=1)
    Restart()


def Event13400940():
    """ 13400940: Event 13400940 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    GotoIfFlagRangeAnyOn(Label.L1, (1670, 1689))
    DisableFlagRange((1670, 1689))
    EnableFlag(1680)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(1, 13401800)
    IfFlagRangeAllOff(1, (1670, 1674))
    GotoIfConditionFalse(Label.L2, input_condition=1)
    DisableFlagRange((1670, 1689))
    EnableFlag(1681)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagOn(2, 1681)
    IfFlagOn(-1, 1720)
    IfFlagOn(-1, 1721)
    IfConditionTrue(2, input_condition=-1)
    IfFlagOn(2, 73400513)
    IfFlagOn(2, 73400403)
    GotoIfConditionFalse(Label.L3, input_condition=2)
    DisableFlagRange((1670, 1689))
    EnableFlag(1671)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagOn(3, 13500100)
    IfFlagOn(-2, 1720)
    IfFlagOn(-2, 1721)
    IfFlagOn(-2, 1724)
    IfFlagOn(-2, 1722)
    IfConditionTrue(3, input_condition=-2)
    IfFlagOn(3, 73400403)
    IfFlagOn(4, 1681)
    IfFlagOff(4, 73400512)
    IfConditionTrue(-3, input_condition=4)
    IfFlagOn(-3, 1671)
    IfConditionTrue(3, input_condition=-3)
    GotoIfConditionFalse(Label.L4, input_condition=3)
    DisableFlagRange((1670, 1689))
    EnableFlag(1672)

    # --- 4 --- #
    DefineLabel(4)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagOn(Label.L5, 1670)
    GotoIfFlagOn(Label.L6, 1671)
    GotoIfFlagOn(Label.L7, 1672)
    GotoIfFlagOn(Label.L8, 1680)
    GotoIfFlagOn(Label.L9, 1681)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    End()

    # --- 8 --- #
    DefineLabel(8)
    EnableBackread(3400900)
    DisableCharacter(3400900)
    DisableObject(3400907)
    DisableObject(3400908)
    EnableBackread(3400906)
    DisableCharacter(3400906)
    End()

    # --- 9 --- #
    DefineLabel(9)
    EnableBackread(3400900)
    EnableCharacter(3400900)
    DisableObject(3400907)
    DisableObject(3400908)
    EnableBackread(3400906)
    EnableCharacter(3400906)
    EnableImmortality(3400900)
    IfFlagOff(7, 50002360)
    IfFlagOn(7, 73400512)
    SkipLinesIfConditionFalse(1, 7)
    DropMandatoryTreasure(3400906)
    SkipLinesIfFlagOff(1, 73400512)
    ForceAnimation(3400900, 7002, loop=True, skip_transition=True)
    End()

    # --- 6 --- #
    DefineLabel(6)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    EnableObject(3400907)
    DisableObject(3400908)
    DisableBackread(3400906)
    DisableCharacter(3400906)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    DisableObject(3400907)
    EnableObject(3400908)
    SkipLinesIfFlagOn(4, 50002360)
    EnableBackread(3400906)
    EnableCharacter(3400906)
    DropMandatoryTreasure(3400906)
    End()
    DisableBackread(3400906)
    DisableCharacter(3400906)
    End()

    # --- 7 --- #
    DefineLabel(7)
    DisableBackread(3400900)
    DisableCharacter(3400900)
    EnableObject(3400907)
    DisableObject(3400908)
    SkipLinesIfFlagOn(4, 50002360)
    EnableBackread(3400906)
    EnableCharacter(3400906)
    DropMandatoryTreasure(3400906)
    End()
    DisableBackread(3400906)
    DisableCharacter(3400906)
    End()


def Event13400941():
    """ 13400941: Event 13400941 """
    EndIfFlagOff(1680)
    IfCharacterDead(-1, 3400800)
    IfCharacterDead(-1, 3400801)
    IfConditionTrue(0, input_condition=-1)
    IfAllPlayersOutsideRegion(1, region=3402915)
    IfCharacterOutsideRegion(1, 3400921, region=3402915)
    IfCharacterOutsideRegion(1, 3400922, region=3402915)
    IfCharacterOutsideRegion(1, 3400923, region=3402915)
    IfCharacterOutsideRegion(1, 3400924, region=3402915)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    Move(3400900, destination=3402911, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- 0 --- #
    DefineLabel(0)
    IfAllPlayersOutsideRegion(2, region=3402916)
    IfCharacterOutsideRegion(2, 3400921, region=3402916)
    IfCharacterOutsideRegion(2, 3400922, region=3402916)
    IfCharacterOutsideRegion(2, 3400923, region=3402916)
    IfCharacterOutsideRegion(2, 3400924, region=3402916)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    Move(3400900, destination=3402912, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(3, region=3402917)
    IfCharacterOutsideRegion(3, 3400921, region=3402917)
    IfCharacterOutsideRegion(3, 3400922, region=3402917)
    IfCharacterOutsideRegion(3, 3400923, region=3402917)
    IfCharacterOutsideRegion(3, 3400924, region=3402917)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    Move(3400900, destination=3402913, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    Move(3400900, destination=34029134, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlagRange((1670, 1689))
    EnableFlag(1681)

    # --- 8 --- #
    DefineLabel(8)
    EnableCharacter(3400900)
    EnableImmortality(3400900)


def Event13400942(_, arg_0_3: int):
    """ 13400942: Event 13400942 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventSlotOn()
    EndIfFlagRangeAllOff((1680, 1681))
    EndIfFlagOn(arg_0_3)
    EndIfFlagOn(73400519)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(-1, arg_0_3)
    IfFlagOn(-1, 73400519)
    IfCharacterDead(-1, 3400900)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacter(3400906)
    Move(3400906, destination=3400900, destination_type=CoordEntityType.Character, model_point=10, short_move=True)
    WaitFrames(1)
    DropMandatoryTreasure(3400906)
    EndIfFlagOn(73400519)
    ForceAnimation(3400900, 7002, loop=True, skip_transition=True)


def Event13400943(_, arg_0_3: int):
    """ 13400943: Event 13400943 """
    IfFlagOn(-1, 1681)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1670, 1689))
    EnableFlag(1670)
    SaveRequest()
    WaitFrames(1)
    ForceAnimation(arg_0_3, 7010, skip_transition=True)
    WaitFrames(119)
    ForceAnimation(arg_0_3, 7011, loop=True, skip_transition=True)
    EnableFlag(73400519)


def Event13400944():
    """ 13400944: Event 13400944 """
    DisableFlag(73400510)
    IfFlagOn(-1, 1670)
    IfFlagOn(-1, 1671)
    IfFlagOn(-1, 1672)
    IfFlagOn(-1, 73400512)
    EndIfConditionTrue(-1)
    IfFlagOn(0, 73400510)
    IfHealthEqual(-2, 3400900, 0.0)
    IfFlagOn(-2, 73400512)
    IfFlagOn(-2, 1670)
    EndIfConditionTrue(-2)
    ForceAnimation(3400900, 7001, loop=True, skip_transition=True)
    IfFlagOff(0, 73400510)
    IfHealthEqual(-3, 3400900, 0.0)
    IfFlagOn(-3, 73400512)
    IfFlagOn(-3, 1670)
    EndIfConditionTrue(-3)
    ForceAnimation(3400900, 0, loop=True, skip_transition=True)
    Restart()


def Event13400900(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13400900: Event 13400900 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyOn((arg_4_7, arg_12_15))
    IfCharacterDead(1, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_16_19)
    SaveRequest()


def Event13400910(_, arg_0_3: int, arg_4_7: int):
    """ 13400910: Event 13400910 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    EnableFlag(arg_4_7)


def Event13400920(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13400920: Event 13400920 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(arg_4_7)
    IfFlagOn(-1, arg_4_7)
    IfHealthLessThanOrEqual(-1, arg_0_3, 0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    DisableFlagRange((arg_8_11, arg_12_15))
    EnableFlag(arg_16_19)
    SaveRequest()


def Event13400930():
    """ 13400930: Event 13400930 """
    DisableAI(3400910)
    IfCharacterInsideRegion(-1, PLAYER, region=3402949)
    IfAttackedWithDamageType(-1, attacked_entity=3400910, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(3400910)


def Event13400950(_, arg_0_3: int, arg_4_7: int):
    """ 13400950: Event 13400950 """
    IfCharacterHuman(-15, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-15)
    GotoIfFlagRangeAnyOn(Label.L0, (1710, 1729))
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)
    Goto(Label.L8)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagOff(Label.L1, 1724)
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(1, 1720)
    IfFlagOn(-1, 1681)
    IfFlagOn(-1, 1671)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 73400403)
    IfFlagOn(1, 73400513)
    IfConditionTrue(-2, input_condition=1)
    IfFlagOn(2, 1720)
    IfFlagOn(2, 73400403)
    IfFlagOn(2, 1670)
    IfConditionTrue(-2, input_condition=2)
    GotoIfConditionFalse(Label.L2, input_condition=-2)
    DisableFlagRange((1710, 1729))
    EnableFlag(1721)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagRangeAnyOn(3, (1720, 1721))
    IfFlagOn(3, 73400403)
    IfFlagOn(3, 13500100)
    GotoIfConditionFalse(Label.L3, input_condition=3)
    DisableFlagRange((1710, 1729))
    EnableFlag(1722)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagRangeAnyOn(4, (1720, 1722))
    IfFlagOn(4, 73400403)
    IfFlagOn(4, 1650)
    GotoIfConditionFalse(Label.L8, input_condition=4)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 8 --- #
    DefineLabel(8)

    # --- 9 --- #
    DefineLabel(9)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    GotoIfFlagOn(Label.L0, 1720)
    GotoIfFlagOn(Label.L1, 1725)
    GotoIfFlagOn(Label.L2, 1710)
    GotoIfFlagOn(Label.L3, 1721)
    GotoIfFlagOn(Label.L4, 1726)
    GotoIfFlagOn(Label.L5, 1711)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableCharacter(arg_0_3)
    EnableBackread(arg_0_3)
    SetTeamType(arg_0_3, TeamType.Ally)
    ForceAnimation(arg_0_3, 103150)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableCharacter(arg_0_3)
    EnableBackread(arg_0_3)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 3 --- #
    DefineLabel(3)
    EnableCharacter(arg_4_7)
    EnableBackread(arg_4_7)
    SetTeamType(arg_4_7, TeamType.Ally)
    ForceAnimation(arg_4_7, 103150)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableCharacter(arg_4_7)
    EnableBackread(arg_4_7)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DropMandatoryTreasure(arg_4_7)
    End()


def Event13400951(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13400951: Event 13400951 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(arg_4_7)
    EndIfFlagOff(arg_8_11)
    IfFlagOn(1, arg_8_11)
    IfFlagOn(1, arg_4_7)
    IfCharacterHasSpecialEffect(1, arg_0_3, 151)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 103155)
    IfFlagOn(2, arg_8_11)
    IfFlagOff(2, arg_4_7)
    IfCharacterHasSpecialEffect(2, arg_0_3, 152)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(arg_0_3, 103150)
    Restart()


def Event13400953(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13400953: Event 13400953 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOff(Label.L0, arg_0_3)
    GotoIfFlagOff(Label.L1, arg_4_7)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(0, arg_4_7)
    AwardItemLot(arg_8_11, host_only=False)


def Event13400970(_, arg_0_3: int):
    """ 13400970: Event 13400970 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    Wait(0.0)


def Event13400980(_, arg_0_3: int, arg_4_7: int):
    """ 13400980: Event 13400980 """
    EndIfThisEventSlotOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)


def Event13400990(_, arg_0_3: int, arg_4_7: int):
    """ 13400990: Event 13400990 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, arg_0_3)
    DisableFlag(arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)
    Restart()


def Event13400995(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13400995: Event 13400995 """
    EndIfFlagOn(arg_0_3)
    EndIfClient()
    IfFlagOn(0, arg_0_3)
    SkipLinesIfFlagOn(2, arg_12_15)
    AwardItemLot(arg_4_7, host_only=False)
    SkipLines(1)
    AwardItemLot(arg_8_11, host_only=False)


@RestartOnRest
def Event13404450(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13404450: Event 13404450 """
    EndIfThisEventSlotOn()
    EndIfClient()
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=1.0)
    IfFlagOn(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOn(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13404401(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13404401: Event 13404401 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagRangeAllOff(1, (13404422, 13404426))
    IfFlagOff(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateVFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_8_11)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagRangeAllOff(2, (13404422, 13404426))
    IfFlagOff(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event13404402(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13404402: Event 13404402 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagOn(-4, 1800)
    IfFlagOn(-4, 1801)
    IfConditionTrue(1, input_condition=-4)
    IfFlagOff(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateVFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_8_11)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagOn(-5, 1800)
    IfFlagOn(-5, 1801)
    IfConditionTrue(2, input_condition=-5)
    IfFlagOff(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event13404403(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13404403: Event 13404403 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagOn(1, 6813)
    IfFlagOff(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateVFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_8_11)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagOn(2, 6813)
    IfFlagOff(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event13404404(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13404404: Event 13404404 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagOff(1, 6813)
    IfFlagOff(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateVFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_8_11)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagOff(2, 6813)
    IfFlagOff(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event13404405(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13404405: Event 13404405 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfPlayerHasGood(1, 4014, including_box=False)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagOn(-4, 1800)
    IfFlagOn(-4, 1801)
    IfConditionTrue(1, input_condition=-4)
    IfFlagOff(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateVFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_8_11)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfPlayerHasGood(2, 4014, including_box=False)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagOn(-5, 1800)
    IfFlagOn(-5, 1801)
    IfConditionTrue(2, input_condition=-5)
    IfFlagOff(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event13404406(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13404406: Event 13404406 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfPlayerHasGood(1, 4014, including_box=False)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagOn(1, 6813)
    IfFlagOff(-1, arg_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)
    CreateVFX(arg_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_8_11)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfPlayerHasGood(2, 4014, including_box=False)
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagOn(2, 6813)
    IfFlagOff(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event13404410(
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
    """ 13404410: Event 13404410 """
    SkipLinesIfFlagOn(1, arg_12_15)
    DisableCharacter(arg_4_7)
    SkipLinesIfFlagOn(3, arg_16_19)
    IfClient(1)
    IfFlagOn(1, arg_12_15)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(arg_4_7)
    EndIfFlagOn(arg_24_27)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(arg_4_7, UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, arg_12_15)
    IfFlagOff(2, arg_16_19)
    IfFlagOn(2, arg_20_23)
    IfFlagOff(2, arg_24_27)
    IfActionButtonParam(2, action_button_id=arg_28_31, entity=arg_4_7)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682, affect_npc_part_hp=False)
    SummonNPC(arg_0_3, arg_4_7, arg_8_11, summon_flag=arg_12_15, dismissal_flag=arg_16_19)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest
def Event13404460(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 13404460: Event 13404460 """
    EndIfClient()
    IfFlagOn(1, arg_20_23)
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


@RestartOnRest
def Event13404490(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13404490: Event 13404490 """
    DisableNetworkSync()
    IfHost(1)
    IfFlagOn(1, arg_4_7)
    IfFlagOff(1, arg_8_11)
    IfFlagOn(1, arg_12_15)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect_WithUnknownEffect(arg_0_3, 35, affect_npc_parts_hp=False)
    WaitFrames(1)
    Restart()
