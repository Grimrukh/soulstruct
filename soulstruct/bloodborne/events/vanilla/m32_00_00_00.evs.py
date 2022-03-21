"""
linked:
140

strings:
0: PC情報_大学到達時
22: クリア時間_通し
40: クリア時間_1プレイ
62: ボス戦_撃破時間
80: ボス_撃破
92: PC情報_ボス撃破_白痴の蜘蛛
124: ボス_戦闘開始
140: N:\\SPRJ\\data\\Param\\event\\common.emevd
216: 
218: 
220: 
222: 
"""
from soulstruct.bloodborne.events import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=45, args=(3200950, 3201950, 999, 13207800))
    RunEvent(7000, slot=46, args=(3200951, 3201951, 999, 13207820))
    RunEvent(7000, slot=47, args=(3200952, 3201952, 13201803, 13207840))
    RunEvent(7000, slot=48, args=(3200953, 3201953, 999, 13207860))
    RunEvent(7100, slot=45, args=(73200200, 3201950))
    RunEvent(7100, slot=46, args=(73200201, 3201951))
    RunEvent(7100, slot=47, args=(73200202, 3201952))
    RunEvent(7100, slot=48, args=(73200203, 3201953))
    RunEvent(7200, slot=45, args=(73200100, 3201950, 2102951))
    RunEvent(7200, slot=46, args=(73200101, 3201951, 2102953))
    RunEvent(7200, slot=47, args=(73200102, 3201952, 2102951))
    RunEvent(7200, slot=48, args=(73200103, 3201953, 2102953))
    RunEvent(7300, slot=45, args=(72103200, 3201950))
    RunEvent(7300, slot=46, args=(72103201, 3201951))
    RunEvent(7300, slot=47, args=(72103202, 3201952))
    RunEvent(7300, slot=48, args=(72103203, 3201953))
    RunEvent(7600, slot=70, args=(3201999, 3203999))
    RunEvent(9200, slot=9, args=(3203900,))
    RunEvent(9220, slot=8, args=(3200710, 13204220, 13204221, 3200, 32, 0), arg_types="iiiiBB")
    RunEvent(9240, slot=8, args=(3200710, 13204220, 13204221, 13204222, 32, 0), arg_types="iiiiBB")
    RunEvent(9260, slot=8, args=(3200710, 13204220, 13204221, 13204222, 32, 0), arg_types="iiiiBB")
    RunEvent(9280, slot=8, args=(3200710, 13204220, 13204221, 3200, 13204800, 32, 0), arg_types="iiiiiBB")
    RegisterLadder(start_climbing_flag=13200000, stop_climbing_flag=13200001, obj=3201130)
    RegisterLadder(start_climbing_flag=13200002, stop_climbing_flag=13200003, obj=3201131)
    RunEvent(13200990)
    RunEvent(13200950)
    RunEvent(13200960)
    CreateObjectVFX(900130, obj=3201000, model_point=200)
    CreateObjectVFX(900130, obj=3201001, model_point=200)
    CreateObjectVFX(900130, obj=3201002, model_point=200)
    CreateObjectVFX(900130, obj=3201003, model_point=200)
    CreateObjectVFX(900130, obj=3201004, model_point=200)
    CreateObjectVFX(900130, obj=3201005, model_point=200)
    DeleteVFX(3203910, erase_root_only=False)
    DeleteVFX(3203911, erase_root_only=False)
    DeleteVFX(3203912, erase_root_only=False)
    RunEvent(13204400, slot=0, args=(13204440, 3203910, 13204420, 13204430, 13201800, 6001))
    RunEvent(13204401, slot=0, args=(13204441, 3203911, 13204421, 13204431, 13201800, 13204420))
    RunEvent(13204402, slot=0, args=(13204442, 3203912, 13204422, 13204432, 13201800, 13204420))
    RunEvent(13204410, slot=0, args=(0, 3200910, 3202910, 13204420, 13204430, 13204440, 13201800, 10566))
    RunEvent(13204410, slot=1, args=(5, 3200911, 3202913, 13204421, 13204431, 13204441, 13201800, 10565))
    RunEvent(13204410, slot=2, args=(5, 3200912, 3202914, 13204422, 13204432, 13204442, 13201800, 10561))
    RunEvent(13204450, slot=0, args=(3200910, 3202911, 13204420, 13204430, 13204800))
    RunEvent(13204450, slot=1, args=(3200911, 3202915, 13204421, 13204431, 13204800))
    RunEvent(13204450, slot=2, args=(3200912, 3202916, 13204422, 13204432, 13204800))
    RunEvent(13204460, slot=0, args=(3200910, 3202911, 3202800, 3202809, 101130, 13204450, 3202809))
    RunEvent(13204460, slot=1, args=(3200911, 3202915, 3202800, 3202809, 101130, 13204451, 3202809))
    RunEvent(13204460, slot=2, args=(3200912, 3202916, 3202800, 3202809, 101130, 13204452, 3202809))
    RunEvent(13204470, slot=0, args=(3200910,))
    RunEvent(13204470, slot=1, args=(3200911,))
    RunEvent(13204470, slot=2, args=(3200912,))
    RunEvent(13204832)
    RunEvent(13204833)
    RunEvent(13204834)
    RunEvent(13201800)
    RunEvent(13201801)
    RunEvent(13201802)
    RunEvent(13201803)
    RunEvent(13204830)
    RunEvent(13204831)
    RunEvent(13204802)
    RunEvent(13204803)
    RunEvent(13204804)
    RunEvent(13204805)
    RunEvent(13204807)
    RunEvent(13204808)
    RunEvent(13204809)
    RunEvent(13204810)
    RunEvent(13204820)
    RunEvent(13204821)
    RunEvent(13201804)
    RunEvent(13204000, slot=0, args=(3200200, 13204802))
    RunEvent(13204000, slot=1, args=(3200201, 13204802))
    RunEvent(13204000, slot=2, args=(3200202, 13204802))
    RunEvent(13204000, slot=3, args=(3200203, 13204802))
    RunEvent(13204000, slot=4, args=(3200204, 13204802))
    RunEvent(13204000, slot=5, args=(3200205, 13204802))
    RunEvent(13204000, slot=6, args=(3200206, 13204802))
    RunEvent(13204000, slot=7, args=(3200207, 13204802))
    RunEvent(13204000, slot=8, args=(3200208, 13204802))
    RunEvent(13204000, slot=9, args=(3200209, 13204802))
    RunEvent(13204000, slot=10, args=(3200210, 13204811))
    RunEvent(13204000, slot=11, args=(3200211, 13204811))
    RunEvent(13204000, slot=12, args=(3200212, 13204811))
    RunEvent(13204000, slot=13, args=(3200213, 13204811))
    RunEvent(13204000, slot=14, args=(3200214, 13204811))
    RunEvent(13204000, slot=15, args=(3200215, 13204811))
    RunEvent(13204000, slot=16, args=(3200216, 13204811))
    RunEvent(13204000, slot=17, args=(3200217, 13204811))
    RunEvent(13204000, slot=18, args=(3200218, 13204811))
    RunEvent(13204000, slot=19, args=(3200219, 13204811))
    RunEvent(13204000, slot=20, args=(3200220, 13204812))
    RunEvent(13204000, slot=21, args=(3200221, 13204812))
    RunEvent(13204000, slot=22, args=(3200222, 13204812))
    RunEvent(13204000, slot=23, args=(3200223, 13204812))
    RunEvent(13204000, slot=24, args=(3200224, 13204812))
    RunEvent(13204000, slot=25, args=(3200225, 13204812))
    RunEvent(13204000, slot=26, args=(3200226, 13204812))
    RunEvent(13204000, slot=27, args=(3200227, 13204812))
    RunEvent(13204000, slot=28, args=(3200228, 13204812))
    RunEvent(13204000, slot=29, args=(3200229, 13204812))
    RunEvent(13204050, slot=0, args=(3200200, 13204802))
    RunEvent(13204050, slot=1, args=(3200201, 13204802))
    RunEvent(13204050, slot=2, args=(3200202, 13204802))
    RunEvent(13204050, slot=3, args=(3200203, 13204802))
    RunEvent(13204050, slot=4, args=(3200204, 13204802))
    RunEvent(13204050, slot=5, args=(3200205, 13204802))
    RunEvent(13204050, slot=6, args=(3200206, 13204802))
    RunEvent(13204050, slot=7, args=(3200207, 13204802))
    RunEvent(13204050, slot=8, args=(3200208, 13204802))
    RunEvent(13204050, slot=9, args=(3200209, 13204802))
    RunEvent(13204050, slot=10, args=(3200210, 13204811))
    RunEvent(13204050, slot=11, args=(3200211, 13204811))
    RunEvent(13204050, slot=12, args=(3200212, 13204811))
    RunEvent(13204050, slot=13, args=(3200213, 13204811))
    RunEvent(13204050, slot=14, args=(3200214, 13204811))
    RunEvent(13204050, slot=15, args=(3200215, 13204811))
    RunEvent(13204050, slot=16, args=(3200216, 13204811))
    RunEvent(13204050, slot=17, args=(3200217, 13204811))
    RunEvent(13204050, slot=18, args=(3200218, 13204811))
    RunEvent(13204050, slot=19, args=(3200219, 13204811))
    RunEvent(13204050, slot=20, args=(3200220, 13204812))
    RunEvent(13204050, slot=21, args=(3200221, 13204812))
    RunEvent(13204050, slot=22, args=(3200222, 13204812))
    RunEvent(13204050, slot=23, args=(3200223, 13204812))
    RunEvent(13204050, slot=24, args=(3200224, 13204812))
    RunEvent(13204050, slot=25, args=(3200225, 13204812))
    RunEvent(13204050, slot=26, args=(3200226, 13204812))
    RunEvent(13204050, slot=27, args=(3200227, 13204812))
    RunEvent(13204050, slot=28, args=(3200228, 13204812))
    RunEvent(13204050, slot=29, args=(3200229, 13204812))
    RunEvent(13204730, slot=0, args=(3200200,))
    RunEvent(13204730, slot=1, args=(3200201,))
    RunEvent(13204730, slot=2, args=(3200202,))
    RunEvent(13204730, slot=3, args=(3200203,))
    RunEvent(13204730, slot=4, args=(3200204,))
    RunEvent(13204730, slot=5, args=(3200205,))
    RunEvent(13204730, slot=6, args=(3200206,))
    RunEvent(13204730, slot=7, args=(3200207,))
    RunEvent(13204730, slot=8, args=(3200208,))
    RunEvent(13204730, slot=9, args=(3200209,))
    RunEvent(13204730, slot=10, args=(3200210,))
    RunEvent(13204730, slot=11, args=(3200211,))
    RunEvent(13204730, slot=12, args=(3200212,))
    RunEvent(13204730, slot=13, args=(3200213,))
    RunEvent(13204730, slot=14, args=(3200214,))
    RunEvent(13204730, slot=15, args=(3200215,))
    RunEvent(13204730, slot=16, args=(3200216,))
    RunEvent(13204730, slot=17, args=(3200217,))
    RunEvent(13204730, slot=18, args=(3200218,))
    RunEvent(13204730, slot=19, args=(3200219,))
    RunEvent(13204730, slot=20, args=(3200220,))
    RunEvent(13204730, slot=21, args=(3200221,))
    RunEvent(13204730, slot=22, args=(3200222,))
    RunEvent(13204730, slot=23, args=(3200223,))
    RunEvent(13204730, slot=24, args=(3200224,))
    RunEvent(13204730, slot=25, args=(3200225,))
    RunEvent(13204730, slot=26, args=(3200226,))
    RunEvent(13204730, slot=27, args=(3200227,))
    RunEvent(13204730, slot=28, args=(3200228,))
    RunEvent(13204730, slot=29, args=(3200229,))
    RunEvent(13200010, slot=0, args=(3201110, 1, 13200100, 3201100, 100))
    RunEvent(13200020, slot=0, args=(7030, 7031, 3201110, 13200010))
    RunEvent(13200030, slot=0, args=(3201100, 7100, 10010172, 13200010))
    RunEvent(13200040, slot=0, args=(3201120, 13200120, 1, 3200040))
    RunEvent(13200040, slot=1, args=(3201122, 13200122, 1, 31))
    RunEvent(13200040, slot=2, args=(3201201, 13200203, 1, 31))
    RunEvent(13200040, slot=3, args=(3201210, 13200211, 1, 31))
    RunEvent(13200050, slot=0, args=(7030, 3201122, 13200041))
    RunEvent(13200050, slot=1, args=(7030, 3201201, 13200042))
    RunEvent(13200055, slot=0, args=(7030, 3201210, 13200043))
    RunEvent(13200060, slot=0, args=(3201200, 13200200, 13200201, 1, 30, 31))
    RunEvent(13200060, slot=2, args=(3201202, 13200204, 13200205, 1, 30, 31))
    RunEvent(13200060, slot=3, args=(3201203, 13200206, 13200207, 1, 3200030, 31))
    RunEvent(13200060, slot=4, args=(3201204, 13200208, 13200209, 1, 30, 31))
    RunEvent(13200060, slot=6, args=(3201211, 13200212, 13200213, 1, 30, 31))
    RunEvent(13200060, slot=7, args=(3201212, 13200214, 13200215, 1, 30, 31))
    RunEvent(13200060, slot=8, args=(3201213, 13200216, 13200217, 1, 30, 31))
    RunEvent(13200060, slot=9, args=(3201214, 13200218, 13200219, 1, 30, 31))
    RunEvent(13200060, slot=10, args=(3201220, 13200220, 13200221, 1, 30, 31))
    RunEvent(13200060, slot=11, args=(3201221, 13200222, 13200223, 1, 30, 31))
    RunEvent(13200060, slot=12, args=(3201222, 13200224, 13200225, 1, 30, 31))
    RunEvent(13200060, slot=13, args=(3201223, 13200226, 13200227, 1, 30, 31))
    RunEvent(13200060, slot=14, args=(3201224, 13200228, 13200229, 1, 30, 31))
    RunEvent(13200060, slot=17, args=(3201232, 13200234, 13200235, 1, 30, 31))
    RunEvent(13200060, slot=18, args=(3201233, 13200236, 13200237, 1, 30, 31))
    RunEvent(13200060, slot=19, args=(3201234, 13200238, 13200239, 1, 30, 31))
    RunEvent(13200200, slot=0, args=(3201050, 13200050))
    RunEvent(13200200, slot=1, args=(3201051, 13200051))
    RunEvent(13200200, slot=3, args=(3201053, 13200053))
    RunEvent(13200200, slot=4, args=(3201054, 13200054))
    RunEvent(13200200, slot=10, args=(3201060, 13200060))
    RunEvent(13200200, slot=12, args=(3201062, 13200062))
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagOff(1, 6325)
    EnableFlag(13201999)
    SkipLinesIfFlagOn(5, 13201999)
    EnableObject(3201500)
    DisableObject(3201501)
    EnableTreasure(3201500)
    DisableTreasure(3201501)
    SkipLines(4)
    DisableObject(3201500)
    EnableObject(3201501)
    DisableTreasure(3201500)
    EnableTreasure(3201501)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagOff(1, 6326)
    EnableFlag(13201998)
    SkipLinesIfFlagOn(6, 13201998)
    EnableObject(3201064)
    DisableObject(3201065)
    EnableObjectActivation(3201064, obj_act_id=9942)
    DisableObjectActivation(3201065, obj_act_id=9942)
    RunEvent(13200200, slot=14, args=(3201064, 13200064))
    SkipLines(5)
    DisableObject(3201064)
    EnableObject(3201065)
    DisableObjectActivation(3201064, obj_act_id=9942)
    EnableObjectActivation(3201065, obj_act_id=9942)
    RunEvent(13200200, slot=15, args=(3201065, 13200065))
    RunEvent(13204100, slot=0, args=(3201000, 7407, 10012007))
    RunEvent(13204100, slot=1, args=(3201001, 7408, 10012008))
    RunEvent(13204100, slot=2, args=(3201002, 7409, 10012009))
    RunEvent(13204100, slot=3, args=(3201003, 7410, 10012010))
    RunEvent(13204100, slot=4, args=(3201004, 7411, 10012011))
    RunEvent(13204100, slot=5, args=(3201005, 7412, 10012012))
    RunEvent(13200400)
    RunEvent(13200500, slot=0, args=(3200110,))
    RunEvent(13205000, slot=0, args=(3200500, 3202500, 0, 2.0, 3203500), arg_types="iiifi")
    RunEvent(13205000, slot=1, args=(3200501, 3202501, 0, 2.0, 3203501), arg_types="iiifi")
    RunEvent(13205000, slot=11, args=(3200315, 3202315, 0, 2.0, 3203315), arg_types="iiifi")
    RunEvent(13205000, slot=12, args=(3200337, 3202337, 0, 2.0, 3203337), arg_types="iiifi")
    RunEvent(13205000, slot=13, args=(3200340, 3202337, 0, 2.0, 3203340), arg_types="iiifi")
    RunEvent(13205000, slot=14, args=(3200341, 3202337, 0, 2.0, 3203341), arg_types="iiifi")
    RunEvent(13205000, slot=15, args=(3200345, 3202337, 0, 2.0, 3203345), arg_types="iiifi")
    RunEvent(13205000, slot=16, args=(3200343, 3202342, 0, 2.0, 3203343), arg_types="iiifi")
    RunEvent(13205000, slot=17, args=(3200110, 3202110, 0, 2.0, 3203110), arg_types="iiifi")
    RunEvent(13205000, slot=18, args=(3200620, 3202620, 0, 2.0, 3203620), arg_types="iiifi")
    RunEvent(13205200)
    RunEvent(13205040, slot=0, args=(3200505, 3202505, 2.0, 0.0, 3202506), arg_types="iiffi")
    RunEvent(13205040, slot=1, args=(3200508, 3202505, 2.0, 1.0, 3202507), arg_types="iiffi")
    RunEvent(13205080, slot=0, args=(3200333, 3202334, 7000, 7001, 0, 0))
    RunEvent(13205080, slot=1, args=(3200336, 3202336, 7002, 7003, 1, 53200110))
    RunEvent(13205080, slot=2, args=(3200342, 3202342, 7000, 7001, 0, 0))
    RunEvent(13205080, slot=3, args=(3200346, 3202315, 7000, 7001, 0, 0))
    RunEvent(13205100, slot=0, args=(3200300, 0))
    RunEvent(13205100, slot=1, args=(3200301, 0))
    RunEvent(13205100, slot=2, args=(3200302, 0))
    RunEvent(13205100, slot=3, args=(3200303, 0))
    RunEvent(13205100, slot=4, args=(3200304, 0))
    RunEvent(13205100, slot=5, args=(3200305, 0))
    RunEvent(13205100, slot=6, args=(3200306, 0))
    RunEvent(13205100, slot=7, args=(3200307, 0))
    RunEvent(13205100, slot=8, args=(3200308, 0))
    RunEvent(13205100, slot=9, args=(3200309, 0))
    RunEvent(13205100, slot=10, args=(3200310, 0))
    RunEvent(13205100, slot=11, args=(3200311, 0))
    RunEvent(13205100, slot=12, args=(3200312, 0))
    RunEvent(13205100, slot=13, args=(3200313, 0))
    RunEvent(13205100, slot=14, args=(3200314, 0))
    RunEvent(13205100, slot=16, args=(3200316, 0))
    RunEvent(13205100, slot=17, args=(3200317, 0))
    RunEvent(13205100, slot=18, args=(3200318, 0))
    RunEvent(13205100, slot=19, args=(3200319, 0))
    RunEvent(13205100, slot=20, args=(3200320, 0))
    RunEvent(13205100, slot=21, args=(3200321, 0))
    RunEvent(13205100, slot=22, args=(3200322, 0))
    RunEvent(13205100, slot=23, args=(3200323, 0))
    RunEvent(13205100, slot=24, args=(3200324, 0))
    RunEvent(13205100, slot=25, args=(3200325, 0))
    RunEvent(13205100, slot=26, args=(3200326, 0))
    RunEvent(13205100, slot=27, args=(3200327, 0))
    RunEvent(13205100, slot=28, args=(3200328, 0))
    RunEvent(13205100, slot=29, args=(3200329, 0))
    RunEvent(13205100, slot=30, args=(3200330, 0))
    RunEvent(13205100, slot=31, args=(3200331, 0))
    RunEvent(13205140, slot=0, args=(3200347, 3202347))
    RunEvent(13205600, slot=0, args=(3290, 3290, 8, 7000, 5907, 13205700, 13205760, 3200420), arg_types="hihiiiii")
    RunEvent(13205600, slot=1, args=(3291, 3291, 9, 7022, 5907, 13205700, 13205760, 3200420), arg_types="hihiiiii")
    RunEvent(13205600, slot=2, args=(3292, 3292, 10, 7023, 5907, 13205700, 13205760, 3200420), arg_types="hihiiiii")
    RunEvent(13205600, slot=3, args=(3290, 3290, 8, 7000, 5907, 13205701, 13205761, 3200421), arg_types="hihiiiii")
    RunEvent(13205600, slot=4, args=(3291, 3291, 9, 7022, 5907, 13205701, 13205761, 3200421), arg_types="hihiiiii")
    RunEvent(13205600, slot=5, args=(3292, 3292, 10, 7023, 5907, 13205701, 13205761, 3200421), arg_types="hihiiiii")
    RunEvent(13205630, slot=0, args=(3290, 3290, 8, 40, 13205700, 3200420), arg_types="hihiii")
    RunEvent(13205630, slot=1, args=(3291, 3291, 9, 40, 13205700, 3200420), arg_types="hihiii")
    RunEvent(13205630, slot=2, args=(3292, 3292, 10, 40, 13205700, 3200420), arg_types="hihiii")
    RunEvent(13205630, slot=3, args=(3290, 3290, 8, 40, 13205701, 3200421), arg_types="hihiii")
    RunEvent(13205630, slot=4, args=(3291, 3291, 9, 40, 13205701, 3200421), arg_types="hihiii")
    RunEvent(13205630, slot=5, args=(3292, 3292, 10, 40, 13205701, 3200421), arg_types="hihiii")
    RunEvent(13205660, slot=0, args=(30, 40, 13205760, 3200420, 1, 11), arg_types="iiiiBB")
    RunEvent(13205660, slot=1, args=(50, 40, 13205760, 3200420, 2, 12), arg_types="iiiiBB")
    RunEvent(13205660, slot=2, args=(60, 40, 13205760, 3200420, 3, 13), arg_types="iiiiBB")
    RunEvent(13205660, slot=3, args=(30, 40, 13205761, 3200421, 1, 11), arg_types="iiiiBB")
    RunEvent(13205660, slot=4, args=(50, 40, 13205761, 3200421, 2, 12), arg_types="iiiiBB")
    RunEvent(13205660, slot=5, args=(60, 40, 13205761, 3200421, 3, 13), arg_types="iiiiBB")
    RunEvent(13200310)
    RunEvent(13200311)


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(13200100)
    RunEvent(13200102)
    RunEvent(13200103)
    RunEvent(13200105)
    RunEvent(13200106)
    RunEvent(13200107)
    RunEvent(13200108)
    RunEvent(13200109)
    RunEvent(13200110)
    RunEvent(13200120)
    RunEvent(13200121)
    SkipLinesIfFlagOff(3, 1420)
    DisableGravity(3200101)
    DisableCharacterCollision(3200101)
    RunEvent(13200102)


def Event13200010(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13200010: Event 13200010 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_0_3, arg_4_7)
    DisableObjectActivation(arg_12_15, obj_act_id=arg_16_19)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_8_11)
    DisableObjectActivation(arg_12_15, obj_act_id=arg_16_19)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    Wait(0.0)


def Event13200020(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13200020: Event 13200020 """
    DisableNetworkSync()
    EndIfFlagOn(arg_12_15)
    IfActionButtonParam(1, action_button_id=arg_0_3, entity=arg_8_11)
    IfActionButtonParam(2, action_button_id=arg_4_7, entity=arg_8_11)
    IfFlagOn(3, arg_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    DisplayDialog(
        10010160,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event13200030(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13200030: Event 13200030 """
    DisableNetworkSync()
    IfFlagOn(1, arg_12_15)
    IfActionButtonParam(1, action_button_id=arg_4_7, entity=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        arg_8_11,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event13200040(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13200040: Event 13200040 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_0_3, arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    Wait(0.0)


def Event13200050(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13200050: Event 13200050 """
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
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Restart()


def Event13200055(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13200055: Event 13200055 """
    DisableNetworkSync()
    EndIfFlagOn(arg_8_11)
    IfFlagOff(1, 1420)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParam(1, action_button_id=arg_0_3, entity=arg_4_7)
    IfFlagOn(2, arg_8_11)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(
        10010161,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


def Event13200060(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13200060: Event 13200060 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_0_3, arg_12_15)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_16_19)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_20_23)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(1, obj_act_id=arg_4_7)
    IfObjectActivated(2, obj_act_id=arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_16_19)
    SkipLines(1)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_20_23)


def Event13200100():
    """ 13200100: Event 13200100 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(13200101)
    EndIfFlagOff(1420)
    DisableAnimations(3200101)
    IfCharacterInsideRegion(0, PLAYER, region=3202850)
    EnableFlag(13200101)
    EnableAnimations(3200101)
    IfCharacterOutsideRegion(0, PLAYER, region=3202850)
    Restart()


def Event13200102():
    """ 13200102: Event 13200102 """
    GotoIfFlagOn(Label.L0, 1431)
    GotoIfFlagOn(Label.L0, 1430)
    GotoIfFlagOn(Label.L0, 1423)
    GotoIfFlagOn(Label.L0, 1422)
    GotoIfFlagOn(Label.L0, 1421)
    GotoIfFlagOn(Label.L1, 1420)

    # --- 0 --- #
    DefineLabel(0)
    PostDestruction(3201300)
    PostDestruction(3201301)
    PostDestruction(3201302)
    PostDestruction(3201303)
    PostDestruction(3201304)
    PostDestruction(3201305)
    PostDestruction(3201306)
    PostDestruction(3201307)
    PostDestruction(3201308)
    PostDestruction(3201309)
    PostDestruction(3201310)
    PostDestruction(3201311)
    PostDestruction(3201312)
    PostDestruction(3201313)
    PostDestruction(3201314)
    PostDestruction(3201315)
    PostDestruction(3201316)
    PostDestruction(3201317)
    PostDestruction(3201318)
    PostDestruction(3201319)
    PostDestruction(3201320)
    SetNest(3200101, 3202852)
    Move(3200101, destination=3202852, destination_type=CoordEntityType.Region, short_move=True)
    AddSpecialEffect(3200101, 5327, affect_npc_part_hp=False)
    AddSpecialEffect(3200101, 5403, affect_npc_part_hp=False)
    IfFlagOn(-1, 1423)
    IfFlagOn(-1, 1432)
    SkipLinesIfConditionFalse(1, -1)
    DisableBackread(3200101)
    SkipLinesIfFlagOff(1, 1431)
    DropMandatoryTreasure(3200101)
    End()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(3200101, 7010, loop=True)
    Move(3200101, destination=3202851, destination_type=CoordEntityType.Region, short_move=True)
    DisableObjectActivation(3201210, obj_act_id=31)


def Event13200103():
    """ 13200103: Event 13200103 """
    EndIfFlagRangeAnyOn((1421, 1437))
    DisableFlag(73200327)
    IfFlagOn(1, 1420)
    IfFlagOn(1, 73200327)
    IfAttackedWithDamageType(2, attacked_entity=3200101, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(1, 2)
    EnableFlag(13200104)
    SetNest(3200101, 3202852)
    AddSpecialEffect(3200101, 5327, affect_npc_part_hp=False)
    ForceAnimation(3200101, 7011)
    WaitFrames(54)
    EnableGravity(3200101)
    EnableCharacterCollision(3200101)
    EnableObjectActivation(3201210, obj_act_id=31)


def Event13200105():
    """ 13200105: Event 13200105 """
    IfFlagOn(1, 1420)
    IfFlagOn(-1, 73200321)
    IfFlagOn(2, 13200104)
    IfFlagOn(2, 73200321)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1420, 1437))
    EnableFlag(1421)
    SaveRequest()


def Event13200106():
    """ 13200106: Event 13200106 """
    EndIfThisEventOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 13200101)
    IfEntityWithinDistance(1, PLAYER, 3200101, radius=5.0)
    IfConditionTrue(0, input_condition=1)
    RunEvent(9350, slot=0, args=(2,))


def Event13200107():
    """ 13200107: Event 13200107 """
    IfFlagOn(1, 9466)
    IfFlagOn(1, 9461)
    IfFlagOn(1, 1421)
    IfFlagOn(1, 73200324)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1420, 1437))
    EnableFlag(1422)


def Event13200108():
    """ 13200108: Event 13200108 """
    EndIfFlagOn(1430)
    EndIfFlagOn(1431)
    IfFlagOn(-1, 1421)
    IfFlagOn(-1, 1422)
    IfConditionTrue(1, input_condition=-1)
    IfHealthLessThan(1, 3200101, 0.5)
    IfAttacked(1, 3200101, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(3200101, 3000)
    DisableFlagRange((1420, 1437))
    EnableFlag(1430)
    SaveRequest()


def Event13200109():
    """ 13200109: Event 13200109 """
    EndIfFlagOn(1431)
    SetTeamType(3200101, TeamType.FriendlyNPC)
    IfFlagOn(0, 1430)
    SetTeamType(3200101, TeamType.HostileNPC)


def Event13200110():
    """ 13200110: Event 13200110 """
    GotoIfFlagOff(Label.L0, 1431)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3200101)
    DisableFlagRange((1420, 1437))
    EnableFlag(1431)
    SaveRequest()


def Event13200120():
    """ 13200120: Event 13200120 """
    GotoIfFlagOff(Label.L0, 1061)
    DisableCharacter(3200100)
    DropMandatoryTreasure(3200100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3200100)
    DisableFlagRange((1060, 1079))
    EnableFlag(1061)
    SaveRequest()


def Event13200121():
    """ 13200121: Event 13200121 """
    EndIfFlagOn(1061)
    IfFlagOn(1, 73200300)
    IfCharacterHasSpecialEffect(1, 3200100, 151)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(73200300)
    ForceAnimation(3200100, 7010)
    SkipLinesIfThisEventOn(1)
    RunEvent(9350, slot=0, args=(2,))
    Restart()


def Event13200200(_, arg_0_3: int, arg_4_7: int):
    """ 13200200: Event 13200200 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


def Event13200310():
    """ 13200310: Event 13200310 """
    IfObjectActivated(0, obj_act_id=13200124)
    CreateTemporaryVFX(932201, anchor_entity=3202001, anchor_type=CoordEntityType.Region)
    Wait(6.0)
    WarpPlayerToRespawnPoint(2602959)


def Event13200311():
    """ 13200311: Event 13200311 """
    IfObjectActivated(0, obj_act_id=13200123)
    CreateTemporaryVFX(932201, anchor_entity=3202000, anchor_type=CoordEntityType.Region)
    Wait(6.0)
    WarpPlayerToRespawnPoint(3302959)


def Event13200400():
    """ 13200400: Event 13200400 """
    EndIfFlagOn(53200810)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    CreateObjectVFX(900201, obj=3201010, model_point=200)
    IfActionButtonParam(0, action_button_id=3200010, entity=3201010)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(3200810, host_only=False)
    DeleteObjectVFX(3201010, erase_root=True)


def Event13200500(_, arg_0_3: int):
    """ 13200500: Event 13200500 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    Wait(0.0)


def Event13200990():
    """ 13200990: Event 13200990 """
    EndIfThisEventOn()
    IfStandingOnCollision(0, 3204000)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 0, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 0, PlayLogMultiplayerType.HostOnly)


def Event13201800():
    """ 13201800: Event 13201800 """
    GotoIfThisEventOff(Label.L0)
    DisableSoundEvent(3203802)
    DisableSoundEvent(3203803)
    DisableCharacter(3200800)
    Kill(3200800, award_souls=False)
    DisableObject(3201800)
    DeleteVFX(3203800, erase_root_only=False)
    DisableMapCollision(3204010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 3200800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3201800)
    DeleteVFX(3203800, erase_root_only=True)
    DisableMapCollision(3204010)
    SetLockedCameraSlot(game_map=BYRGENWERTH, camera_slot=0)
    Wait(3.0)
    KillBoss(3200800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
    AwardAchievement(17)
    AwardItemLot(51001900, host_only=False)
    EnableFlag(3200)
    EnableFlag(9465)
    StartPlayLogMeasurement(3200000, 22, overwrite=False)
    StartPlayLogMeasurement(3200001, 40, overwrite=False)
    StartPlayLogMeasurement(3200010, 62, overwrite=False)
    CreatePlayLog(80)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 92, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 92, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 92, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 92, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def Event13201801():
    """ 13201801: Event 13201801 """
    DisableNetworkSync()
    EndIfFlagOn(13201800)
    IfFlagOn(1, 13201800)
    IfCharacterBackreadDisabled(2, 3200800)
    IfHealthLessThanOrEqual(2, 3200800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=3202800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def Event13201802():
    """ 13201802: Event 13201802 """
    EndIfFlagOn(13201800)
    EndIfThisEventOn()
    IfFlagOff(1, 13201800)
    IfThisEventOff(1)
    IfAttackedWithDamageType(1, attacked_entity=3200800)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13204800)
    EndIfFlagOn(9303)
    RunEvent(9350, slot=0, args=(2,))
    EnableFlag(9303)


@RestartOnRest
def Event13201803():
    """ 13201803: Event 13201803 """
    GotoIfThisEventOff(Label.L0)
    DisableCharacter(3200801)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(3200801)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfConditionFalse(1, 1)
    SetNetworkUpdateAuthority(3200801, UpdateAuthority.Forced)
    GotoIfFlagOn(Label.L1, 13201800)
    IfCharacterHuman(2, PLAYER)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    IfFlagOn(0, 13201800)
    IfCharacterHuman(3, PLAYER)
    IfCharacterInsideRegion(3, PLAYER, region=3202811)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3202812)
    IfCharacterHuman(5, PLAYER)
    IfCharacterInsideRegion(5, PLAYER, region=3202813)
    IfCharacterHuman(6, PLAYER)
    IfCharacterInsideRegion(6, PLAYER, region=3202814)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(8, 3)
    SkipLinesIfFinishedConditionTrue(5, 4)
    SkipLinesIfFinishedConditionTrue(2, 5)
    Move(3200801, destination=3202815, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    Move(3200801, destination=3202816, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    Move(3200801, destination=3202817, destination_type=CoordEntityType.Region, short_move=True)
    Goto(Label.L1)
    Move(3200801, destination=3202818, destination_type=CoordEntityType.Region, short_move=True)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(3200801, 7001)
    IfCharacterHuman(8, PLAYER)
    IfEntityWithinDistance(8, PLAYER, 3200801, radius=12.0)
    IfConditionTrue(0, input_condition=8)
    EnableFlag(9180)
    WaitFrames(1)
    PlayCutsceneAndSetTimePeriod(32000000, CutsceneType.Skippable, player_id=PLAYER, time_period_id=3)
    WaitFrames(1)
    DisableFlag(9180)
    EnableFlag(70002802)
    WarpPlayerToRespawnPoint(2802958)
    End()

    # --- 2 --- #
    DefineLabel(2)
    IfFlagOn(0, 6001)
    Wait(0.0)


def Event13201804():
    """ 13201804: Event 13201804 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 13204800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(13204800)
    EnableFlag(13201802)


def Event13204000(_, arg_0_3: int, arg_4_7: int):
    """ 13204000: Event 13204000 """
    EndIfThisEventSlotOn()
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    IfFlagOn(1, arg_4_7)
    IfRandomTimeElapsed(-1, min_seconds=2.0, max_seconds=3.0)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(2, 3.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(arg_0_3)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=7000, wait_for_completion=True)
    EnableGravity(arg_0_3)


def Event13204050(_, arg_0_3: int, arg_4_7: int):
    """ 13204050: Event 13204050 """
    GotoIfFlagOff(Label.L0, 13201800)
    DisableCharacter(arg_0_3)
    Kill(arg_0_3, award_souls=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(1, arg_4_7)
    IfCharacterDead(1, 3200800)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=0.0, max_seconds=1.0)
    Kill(arg_0_3, award_souls=False)


def Event13204100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13204100: Event 13204100 """
    DisableNetworkSync()
    IfActionButtonParam(0, action_button_id=arg_4_7, entity=arg_0_3)
    DisplayDialog(
        arg_8_11,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event13204730(_, arg_0_3: int):
    """ 13204730: Event 13204730 """
    EndIfFlagOn(13201800)
    IfFlagOn(0, 13204802)
    SetCharacterEventTarget(arg_0_3, 3200800)


def Event13204830():
    """ 13204830: Event 13204830 """
    EndIfFlagOn(13201800)
    GotoIfFlagOn(Label.L0, 13201802)
    SkipLinesIfClient(2)
    DisableObject(3201800)
    DeleteVFX(3203800, erase_root_only=False)
    DisableMapCollision(3204010)
    IfFlagOff(1, 13201800)
    IfFlagOn(1, 13201802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(3201800)
    CreateVFX(3203800)
    EnableMapCollision(3204010)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 13201800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=3200800, entity=3201800)
    IfFlagOn(3, 13201800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 3202800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3202809)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    Restart()


def Event13204831():
    """ 13204831: Event 13204831 """
    DisableNetworkSync()
    EndIfFlagOn(13201800)
    IfFlagOff(1, 13201800)
    IfFlagOn(1, 13201802)
    IfFlagOn(1, 13204800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParam(1, action_button_id=3200800, entity=3201800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3202800, animation=101130)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=3202801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    Restart()


def Event13204832():
    """ 13204832: Event 13204832 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 3201800, radius=2.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event13204833():
    """ 13204833: Event 13204833 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, 3201800, radius=2.0)
    IfEntityWithinDistance(1, PLAYER, 3201800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def Event13204834():
    """ 13204834: Event 13204834 """
    IfEntityWithinDistance(0, 3200110, 3201800, radius=2.0)
    SetGravityAndCollisionExcludingOwnWorld(3200110, False)
    IfEntityBeyondDistance(0, 3200110, 3201800, radius=2.0)
    SetGravityAndCollisionExcludingOwnWorld(3200110, True)
    Restart()


def Event13204802():
    """ 13204802: Event 13204802 """
    EndIfFlagOn(13201800)
    DisableAI(3200800)
    DisableHealthBar(3200800)
    EnableImmortality(3200800)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(1, 13201802)
    IfFlagOn(1, 13204800)
    IfConditionTrue(0, input_condition=1)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3200800, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13204800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(3200800, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3200800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(3200800, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3200800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(3200800)
    DisableImmortality(3200800)
    AddSpecialEffect(3200800, 3011, affect_npc_part_hp=True)
    EnableBossHealthBar(3200800, name=510000, slot=0)
    SetNetworkUpdateRate(3200800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreatePlayLog(124)
    StartPlayLogMeasurement(3200010, 62, overwrite=True)


def Event13204803():
    """ 13204803: Event 13204803 """
    DisableNetworkSync()
    EndIfFlagOn(13201800)
    GotoIfThisEventOn(Label.L0)
    DisableSoundEvent(3203802)
    DisableSoundEvent(3203803)
    IfFlagOff(1, 13201800)
    IfFlagOn(1, 13204802)
    SkipLinesIfHost(1)
    IfFlagOn(1, 13204801)
    IfCharacterInsideRegion(1, PLAYER, region=3202801)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(3203802)
    IfHasTAEEvent(2, 3200800, tae_event_id=10)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 13201800)
    IfFlagOn(2, 13204802)
    SkipLinesIfHost(1)
    IfFlagOn(2, 13204801)
    IfCharacterInsideRegion(2, PLAYER, region=3202801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(3203802)
    WaitFrames(0)
    EnableBossMusic(3203803)


def Event13204804():
    """ 13204804: Event 13204804 """
    DisableNetworkSync()
    EndIfFlagOn(13201800)
    IfHealthGreaterThan(1, 3200800, 0.0)
    IfEntityWithinDistance(1, PLAYER, 3200800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=BYRGENWERTH, camera_slot=1)
    IfHealthGreaterThan(2, 3200800, 0.0)
    IfEntityBeyondDistance(2, PLAYER, 3200800, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=BYRGENWERTH, camera_slot=0)
    Restart()


def Event13204805():
    """ 13204805: Event 13204805 """
    DisableNetworkSync()
    EndIfFlagOn(13201800)
    IfFlagOn(0, 13201800)
    DisableBossMusic(3203802)
    DisableBossMusic(3203803)
    DisableBossMusic(-1)


def Event13204807():
    """ 13204807: Event 13204807 """
    EndIfFlagOn(13201800)
    IfHealthLessThanOrEqual(0, 3200800, 0.75)
    AICommand(3200800, command_id=100, slot=0)
    ReplanAI(3200800)
    IfHasTAEEvent(0, 3200800, tae_event_id=10)
    DisableCharacter(3200800)
    Wait(3.0)
    Move(3200800, destination=3202806, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(3200800)
    ForceAnimation(3200800, 3021)
    AICommand(3200800, command_id=101, slot=0)
    ReplanAI(3200800)
    EnableFlag(13204811)
    IfHealthLessThanOrEqual(0, 3200800, 0.5)
    AICommand(3200800, command_id=110, slot=0)
    ReplanAI(3200800)
    IfHasTAEEvent(0, 3200800, tae_event_id=10)
    DisableCharacter(3200800)
    Wait(3.0)
    Move(3200800, destination=3202807, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(3200800)
    ForceAnimation(3200800, 3021)
    AICommand(3200800, command_id=111, slot=0)
    ReplanAI(3200800)
    EnableFlag(13204812)


def Event13204808():
    """ 13204808: Event 13204808 """
    EndIfFlagOn(13201800)
    CreateNPCPart(
        3200800,
        npc_part_id=3201,
        part_index=NPCPartType.Part2,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(3200800, npc_part_id=3201, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, 3200800, npc_part_id=3201, value=0)
    IfHealthLessThanOrEqual(2, 3200800, 0.0)
    IfHasTAEEvent(3, 3200800, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    ResetAnimation(3200800, disable_interpolation=False)
    ForceAnimation(3200800, 7000)
    SetNPCPartHealth(3200800, npc_part_id=3201, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, 3200800, npc_part_id=3201, value=0)
    IfHealthLessThanOrEqual(5, 3200800, 0.0)
    IfHasTAEEvent(6, 3200800, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    ResetAnimation(3200800, disable_interpolation=False)
    ForceAnimation(3200800, 7001)
    SetNPCPartHealth(3200800, npc_part_id=3201, desired_health=25, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, 3200800, npc_part_id=3201, value=0)
    IfHealthLessThanOrEqual(8, 3200800, 0.0)
    IfHasTAEEvent(9, 3200800, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(8)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=9)
    ResetAnimation(3200800, disable_interpolation=False)
    ForceAnimation(3200800, 7002)
    CreateNPCPart(
        3200800,
        npc_part_id=3201,
        part_index=NPCPartType.Part2,
        part_health=9999,
        damage_correction=1.0,
        body_damage_correction=1.25,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(3200800, npc_part_id=3201, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(3200800)
    IfTimeElapsed(0, 30.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(3200800, npc_part_id=3201, desired_health=-1, overwrite_max=True)
    ReplanAI(2420800)
    WaitFrames(10)
    Restart()


def Event13204809():
    """ 13204809: Event 13204809 """
    EndIfFlagOn(13201800)
    CreateNPCPart(
        3200800,
        npc_part_id=3202,
        part_index=NPCPartType.Part3,
        part_health=100,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(3200800, npc_part_id=3202, material_sfx_id=59, material_vfx_id=59)
    IfCharacterPartHealthLessThanOrEqual(1, 3200800, npc_part_id=3202, value=0)
    IfHealthLessThanOrEqual(2, 3200800, 0.0)
    IfHasTAEEvent(3, 3200800, tae_event_id=20)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=3)
    ResetAnimation(3200800, disable_interpolation=False)
    ForceAnimation(3200800, 7005)
    SetNPCPartHealth(3200800, npc_part_id=3202, desired_health=50, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(4, 3200800, npc_part_id=3202, value=0)
    IfHealthLessThanOrEqual(5, 3200800, 0.0)
    IfHasTAEEvent(6, 3200800, tae_event_id=20)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(5)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=6)
    ResetAnimation(3200800, disable_interpolation=False)
    ForceAnimation(3200800, 7006)
    SetNPCPartHealth(3200800, npc_part_id=3202, desired_health=25, overwrite_max=True)
    IfCharacterPartHealthLessThanOrEqual(7, 3200800, npc_part_id=3, value=0)
    IfHealthLessThanOrEqual(8, 3200800, 0.0)
    IfHasTAEEvent(9, 3200800, tae_event_id=20)
    IfConditionTrue(-3, input_condition=7)
    IfConditionTrue(-3, input_condition=8)
    IfConditionTrue(-3, input_condition=9)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(8)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=9)
    ResetAnimation(3200800, disable_interpolation=False)
    ForceAnimation(3200800, 7007)
    CreateNPCPart(
        3200800,
        npc_part_id=3202,
        part_index=NPCPartType.Part3,
        part_health=9999,
        damage_correction=1.0,
        body_damage_correction=1.2999999523162842,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(3200800, npc_part_id=3202, material_sfx_id=60, material_vfx_id=60)
    ReplanAI(3200800)
    IfTimeElapsed(0, 30.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNPCPartHealth(3200800, npc_part_id=3202, desired_health=-1, overwrite_max=True)
    ReplanAI(2420800)
    WaitFrames(10)
    Restart()


def Event13204810():
    """ 13204810: Event 13204810 """
    EndIfFlagOn(13201800)
    CreateNPCPart(
        3200800,
        npc_part_id=3200,
        part_index=NPCPartType.Part1,
        part_health=50,
        damage_correction=0.5,
        body_damage_correction=0.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(3200800, npc_part_id=3200, material_sfx_id=61, material_vfx_id=61)
    IfCharacterPartHealthLessThanOrEqual(0, 3200800, npc_part_id=3200, value=0)
    Restart()


def Event13204820():
    """ 13204820: Event 13204820 """
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3202800)
    IfConditionTrue(0, input_condition=1)
    GotoIfClient(Label.L0)
    EnableInvincibility(PLAYER)
    CreateTemporaryVFX(932210, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=246)

    # --- 0 --- #
    DefineLabel(0)
    Wait(5.0)
    DisableInvincibility(PLAYER)
    SkipLinesIfFlagOff(1, 13201802)
    EnableFlag(13204800)
    Restart()


def Event13204821():
    """ 13204821: Event 13204821 """
    DisableNetworkSync()
    IfFlagOn(1, 13204800)
    IfCharacterInsideRegion(1, PLAYER, region=3202800)
    IfConditionTrue(0, input_condition=1)
    EnableInvincibility(PLAYER)
    CreateTemporaryVFX(932210, anchor_entity=PLAYER, anchor_type=CoordEntityType.Character, model_point=246)
    Wait(5.0)
    DisableInvincibility(PLAYER)
    EnableFlag(13204801)
    Restart()


@RestartOnRest
def Event13205000(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: int):
    """ 13205000: Event 13205000 """
    GotoIfThisEventSlotOn(Label.L0)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=-1)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_8_11)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_12_15)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_16_19)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13205040(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float, arg_16_19: int):
    """ 13205040: Event 13205040 """
    EndIfThisEventSlotOn()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=2)
    EnableAI(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Wait(arg_12_15)
    EnableAI(arg_0_3)
    SetNest(arg_0_3, arg_16_19)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_16_19)
    ForceAnimation(arg_0_3, 3013)
    WaitFrames(34)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13205050(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13205050: Event 13205050 """
    GotoIfThisEventSlotOn(Label.L0)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=-1)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_8_11)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13205060(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13205060: Event 13205060 """
    IfCharacterInsideRegion(-1, arg_0_3, region=arg_4_7)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_8_11)


@RestartOnRest
def Event13205080(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13205080: Event 13205080 """
    EndIfThisEventSlotOn()
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, arg_8_11, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    SkipLinesIfEqual(1, left=arg_16_19, right=0)
    IfFlagOn(1, arg_20_23)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableGravity(arg_0_3)
    EnableAI(arg_0_3)
    ForceAnimation(arg_0_3, arg_12_15, wait_for_completion=True)
    EnableCharacterCollision(arg_0_3)


@RestartOnRest
def Event13205100(_, arg_0_3: int, arg_4_7: int):
    """ 13205100: Event 13205100 """
    EndIfThisEventSlotOn()
    IfCharacterBackreadEnabled(0, arg_0_3)
    ForceAnimation(arg_0_3, 7004, loop=True)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 7005)
    WaitFrames(59)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=3011)


@RestartOnRest
def Event13205140(_, arg_0_3: int, arg_4_7: int):
    """ 13205140: Event 13205140 """
    EndIfThisEventSlotOn()
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(-1)
    EndIfFinishedConditionTrue(2)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=3002)


@RestartOnRest
def Event13205200():
    """ 13205200: Event 13205200 """
    GotoIfThisEventSlotOn(Label.L0)
    DisableCharacter(3200621)
    IfHealthEqual(1, 3200620, 0.0)
    IfHasTAEEvent(1, 3200620, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    Move(
        3200621,
        destination=3200620,
        destination_type=CoordEntityType.Character,
        model_point=90,
        copy_draw_parent=3200620,
    )
    EnableCharacter(3200621)

    # --- 0 --- #
    DefineLabel(0)
    DropMandatoryTreasure(3200621)


@RestartOnRest
def Event13205300(_, arg_0_3: int, arg_4_5: short, arg_8_11: int):
    """ 13205300: Event 13205300 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    CreateNPCPart(
        arg_0_3,
        npc_part_id=arg_4_5,
        part_index=NPCPartType.Part1,
        part_health=30,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_0_3, npc_part_id=arg_8_11, material_sfx_id=61, material_vfx_id=61)
    IfCharacterPartHealthLessThanOrEqual(0, arg_0_3, npc_part_id=arg_8_11, value=0)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ForceAnimation(arg_0_3, 9930)
    SetNPCPartHealth(arg_0_3, npc_part_id=arg_8_11, desired_health=-1, overwrite_max=False)
    Restart()


def Event13205600(
    _,
    arg_0_1: short,
    arg_4_7: int,
    arg_8_9: short,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 13205600: Event 13205600 """
    IfFlagOn(0, arg_20_23)
    IfCharacterPartHealthLessThanOrEqual(1, arg_28_31, npc_part_id=arg_4_7, value=0)
    IfAttacked(1, arg_28_31, attacker=PLAYER)
    IfFlagOn(1, arg_24_27)
    IfHealthLessThanOrEqual(2, arg_28_31, 0.0)
    IfFlagOn(2, arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOn(2, arg_20_23)
    SetNPCPartHealth(arg_28_31, npc_part_id=arg_4_7, desired_health=1, overwrite_max=False)
    Restart()
    CreateNPCPart(
        arg_28_31,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=999999,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_28_31, npc_part_id=arg_4_7, material_sfx_id=65, material_vfx_id=65)
    ResetAnimation(arg_28_31, disable_interpolation=False)
    ForceAnimation(arg_28_31, arg_12_15)
    IfHasTAEEvent(0, arg_28_31, tae_event_id=400)
    AddSpecialEffect(arg_28_31, arg_16_19, affect_npc_part_hp=False)
    DisableFlag(arg_24_27)
    IfHasTAEEvent(0, arg_28_31, tae_event_id=300)
    SetNPCPartHealth(arg_28_31, npc_part_id=arg_4_7, desired_health=80, overwrite_max=True)
    SetNPCPartEffects(arg_28_31, npc_part_id=arg_4_7, material_sfx_id=64, material_vfx_id=64)
    CancelSpecialEffect(arg_28_31, arg_16_19)
    AICommand(arg_28_31, command_id=-1, slot=0)
    ReplanAI(arg_28_31)
    WaitFrames(10)
    Restart()


def Event13205630(_, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13205630: Event 13205630 """
    IfEntityWithinDistance(1, arg_20_23, PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(
        arg_20_23,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_20_23, npc_part_id=arg_4_7, material_sfx_id=64, material_vfx_id=64)
    EnableFlag(arg_16_19)


def Event13205660(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar, arg_17_17: uchar):
    """ 13205660: Event 13205660 """
    SetCollisionMask(arg_12_15, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(arg_12_15, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    IfHasTAEEvent(0, arg_12_15, tae_event_id=arg_0_3)
    EnableFlag(arg_8_11)
    SetCollisionMask(arg_12_15, bit_index=arg_16_16, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_12_15, bit_index=arg_17_17, switch_type=OnOffChange.On)
    IfHasTAEEvent(0, arg_12_15, tae_event_id=arg_4_7)
    DisableFlag(arg_8_11)
    Restart()


def Event13200950():
    """ 13200950: Event 13200950 """
    IfCharacterHuman(1, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    IfStandingOnCollision(2, 3204001)
    IfFlagOn(2, 12800434)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(12800434)
    AddSpecialEffect(PLAYER, 110, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 111, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 112, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 113, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 114, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 115, affect_npc_part_hp=False)
    AddSpecialEffect(PLAYER, 116, affect_npc_part_hp=False)
    EndIfThisEventOn()
    RunEvent(9350, slot=0, args=(2,))
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(0, 6001)
    Wait(0.0)


def Event13200960():
    """ 13200960: Event 13200960 """
    EndIfThisEventOn()
    IfCharacterHuman(1, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    IfStandingOnCollision(-1, 3204001)
    IfStandingOnCollision(-1, 3204002)
    IfConditionTrue(0, input_condition=-1)
    AwardAchievement(13)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOn(0, 6001)
    Wait(0.0)


@RestartOnRest
def Event13204450(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13204450: Event 13204450 """
    EndIfThisEventSlotOn()
    EndIfClient()
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=1.0)
    IfFlagOn(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOn(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)


def Event13204470(_, arg_0_3: int):
    """ 13204470: Event 13204470 """
    IfCharacterInsideRegion(0, arg_0_3, region=3202800)
    EnableInvincibility(arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    Wait(5.0)
    DisableInvincibility(arg_0_3)


@RestartOnRest
def Event13204400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13204400: Event 13204400 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOff(1, 13204421)
    IfFlagOff(1, 13204422)
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
    IfFlagOff(2, 13204421)
    IfFlagOff(2, 13204422)
    IfFlagOff(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event13204401(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13204401: Event 13204401 """
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
def Event13204402(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13204402: Event 13204402 """
    GotoIfFlagOn(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, arg_8_11)
    IfFlagOff(1, arg_12_15)
    IfFlagOff(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagOn(-4, 12410803)
    IfFlagOn(-4, 12410804)
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
    IfFlagOn(-5, 12410803)
    IfFlagOn(-5, 12410804)
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
def Event13204410(
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
    """ 13204410: Event 13204410 """
    SetBackreadStateAlternate(arg_4_7, state=True)
    SetNetworkUpdateRate(arg_4_7, is_fixed=True, update_rate=CharacterUpdateRate.Always)
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
def Event13204460(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
):
    """ 13204460: Event 13204460 """
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
