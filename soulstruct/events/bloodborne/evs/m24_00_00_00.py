"""
linked:
220

strings:
0: 
2: 聖堂街A_邪神投げ開始
26: 聖堂街A_扉を閉じる領域侵入
56: 聖堂街A_ショートカット領域侵入
90: 聖堂街A_トラップ発動
114: ボス_撃破
126: PC情報_ボス撃破_聖女ビースト
160: ボス_戦闘開始
176: ボス戦_撃破時間
194: PC情報_聖堂街A到達時
220: N:\\SPRJ\\data\\Param\\event\\common.events
296: 
298: 
300: 
302: 
"""
from soulstruct.events.bloodborne import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RunEvent(7600, slot=20, args=(2401999, 2403999))
    RunEvent(7600, slot=21, args=(2401998, 2403998))
    RunEvent(7600, slot=22, args=(2401997, 2403997))
    RunEvent(7600, slot=23, args=(2401996, 2403996))
    RunEvent(7600, slot=24, args=(2401995, 2403995))
    RunEvent(7000, slot=10, args=(2400950, 2401950, 999, 12407800))
    RunEvent(7000, slot=11, args=(2400951, 2401951, 12401800, 12407820))
    RunEvent(7100, slot=10, args=(72400200, 2401950))
    RunEvent(7100, slot=11, args=(72400201, 2401951))
    RunEvent(7200, slot=10, args=(72400100, 2401950, 2102950))
    RunEvent(7200, slot=11, args=(72400101, 2401951, 2102950))
    RunEvent(7300, slot=10, args=(72102400, 2401950))
    RunEvent(7300, slot=11, args=(72102401, 2401951))
    RunEvent(9200, slot=2, args=(2403900,))
    RunEvent(9220, slot=2, args=(2400710, 12404220, 12404221, 2400, 24, 0), arg_types='iiiiBB')
    RunEvent(9240, slot=2, args=(2400710, 12404220, 12404221, 12404222, 24, 0), arg_types='iiiiBB')
    RunEvent(9260, slot=2, args=(2400710, 12404220, 12404221, 12404222, 24, 0), arg_types='iiiiBB')
    RunEvent(9280, slot=2, args=(2400710, 12404220, 12404221, 2400, 12404223, 24, 0), arg_types='iiiiiBB')
    SkipLinesIfFlagOn(7, 12400160)
    EnableFlag(2400)
    EnableFlag(2401)
    EnableFlag(2405)
    EnableFlag(2406)
    DisableFlag(2402)
    DisableFlag(2407)
    SkipLines(14)
    SkipLinesIfFlagOn(7, 12401800)
    DisableFlag(2400)
    DisableFlag(2401)
    DisableFlag(2405)
    DisableFlag(2406)
    DisableFlag(2402)
    DisableFlag(2407)
    SkipLines(6)
    EnableFlag(2400)
    EnableFlag(2401)
    DisableFlag(2405)
    DisableFlag(2406)
    EnableFlag(2402)
    DisableFlag(2407)
    DeleteFX(2403910, erase_root_only=False)
    RunEvent(12404400, slot=0, args=(12404440, 2403910, 12404420, 12404430, 12401800, 6001))
    RunEvent(12404410, slot=0, args=(0, 2400910, 2402910, 12404420, 12404430, 12404440, 12401800, 10567))
    RunEvent(12404450, slot=0, args=(2400910, 2402911, 12404420, 12404430, 12404800))
    RunEvent(12404460, slot=0, args=(2400910, 2402911, 2402800, 2402801, 101130, 12404450, 2402801))
    RunEvent(12404490)
    CreateObjectFX(900130, obj=2401900, model_point=200)
    CreateObjectFX(900130, obj=2401901, model_point=200)
    RegisterLadder(start_climbing_flag=12400600, stop_climbing_flag=12400601, obj=2401020)
    RegisterLadder(start_climbing_flag=12400602, stop_climbing_flag=12400603, obj=2401021)
    RegisterLadder(start_climbing_flag=12400604, stop_climbing_flag=12400605, obj=2401022)
    RegisterLadder(start_climbing_flag=12400606, stop_climbing_flag=12400607, obj=2401023)
    RegisterLadder(start_climbing_flag=12400608, stop_climbing_flag=12400609, obj=2401024)
    CreateSpawner(2400000)
    CreateSpawner(2402070)
    CreateSpawner(2402071)
    CreateSpawner(2402072)
    DisableGravity(2400899)
    DisableCollision(2400899)
    CreateHazard(12400190, 2401017, model_point=100, behavior_param_id=6110, target_type=DamageTargetType.Character, radius=0.6000000238418579, life=0.0, repetition_time=1.0)
    CreateHazard(12400191, 2401018, model_point=100, behavior_param_id=6110, target_type=DamageTargetType.Character, radius=0.6000000238418579, life=0.0, repetition_time=1.0)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagOff(1, 6646)
    EnableFlag(12401999)
    SkipLinesIfFlagOn(6, 12401999)
    EnableObject(2401501)
    DisableObject(2401505)
    EnableObjectActivation(2401501, obj_act_id=9942)
    DisableObjectActivation(2401505, obj_act_id=9942)
    RunEvent(12400350, slot=4, args=(2401501, 12400451))
    SkipLines(5)
    DisableObject(2401501)
    EnableObject(2401505)
    DisableObjectActivation(2401501, obj_act_id=9942)
    EnableObjectActivation(2401505, obj_act_id=9942)
    RunEvent(12400350, slot=5, args=(2401505, 12400455))
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagOff(1, 6310)
    EnableFlag(12401998)
    SkipLinesIfFlagOn(6, 12401998)
    EnableObject(2401502)
    DisableObject(2401508)
    EnableObjectActivation(2401502, obj_act_id=9942)
    DisableObjectActivation(2401508, obj_act_id=9942)
    RunEvent(12400350, slot=7, args=(2401502, 12400452))
    SkipLines(5)
    DisableObject(2401502)
    EnableObject(2401508)
    DisableObjectActivation(2401502, obj_act_id=9942)
    EnableObjectActivation(2401508, obj_act_id=9942)
    RunEvent(12400350, slot=8, args=(2401508, 12400458))
    IfCharacterHuman(13, PLAYER)
    SkipLinesIfConditionFalse(2, 13)
    SkipLinesIfFlagOff(1, 6311)
    EnableFlag(12401997)
    SkipLinesIfFlagOn(6, 12401997)
    EnableObject(2401504)
    DisableObject(2401507)
    EnableObjectActivation(2401504, obj_act_id=9942)
    DisableObjectActivation(2401507, obj_act_id=9942)
    RunEvent(12400350, slot=9, args=(2401504, 12400454))
    SkipLines(5)
    DisableObject(2401504)
    EnableObject(2401507)
    DisableObjectActivation(2401504, obj_act_id=9942)
    EnableObjectActivation(2401507, obj_act_id=9942)
    RunEvent(12400350, slot=10, args=(2401507, 12400457))
    RunEvent(12400070, slot=0, args=(2421201, 1, 2420020, 12420120))
    RunEvent(12400080, slot=0, args=(2401207, 12400177, 12400178, 2400050))
    RunEvent(12400080, slot=1, args=(2401207, 12400177, 12400178, 2400051))
    RunEvent(12400080, slot=2, args=(2401208, 12400157, 12405179, 2400050))
    RunEvent(12400080, slot=3, args=(2401208, 12400157, 12405179, 2400051))
    RunEvent(12400080, slot=4, args=(2401220, 12400160, 12400160, 2400031))
    RunEvent(12400080, slot=5, args=(2401209, 12400167, 12405175, 2400050))
    RunEvent(12400080, slot=6, args=(2401209, 12400167, 12405175, 2400051))
    RunEvent(12400095, slot=0, args=(2401095,))
    RunEvent(12400100, slot=0, args=(2401040, 12400190, 9921, 19921))
    RunEvent(12400100, slot=1, args=(2401040, 12400191, 9921, 19921))
    RunEvent(12400125)
    RunEvent(12400126)
    RunEvent(12400127)
    RunEvent(12400128)
    RunEvent(12400130, slot=0, args=(2401204, 1, 12400112, 12400130))
    RunEvent(12400130, slot=1, args=(2401200, 2, 12400113, 12400131))
    RunEvent(12400130, slot=2, args=(2101201, 1, 12400102, 12400132))
    RunEvent(12400130, slot=3, args=(2101202, 2, 12400103, 12400133))
    RunEvent(12400130, slot=5, args=(2401211, 1, 12400190, 12400135))
    RunEvent(12400130, slot=6, args=(2401212, 1, 12400191, 12400136))
    RunEvent(12400130, slot=7, args=(2401201, 1, 12400114, 12400137))
    RunEvent(12400130, slot=8, args=(2401213, 2, 12400200, 12400138))
    RunEvent(12400146)
    RunEvent(12400147)
    RunEvent(12400148)
    RunEvent(12400149)
    RunEvent(12400159)
    RunEvent(12400155)
    RunEvent(12400156)
    RunEvent(12400158)
    RunEvent(12400161)
    RunEvent(12400174)
    RunEvent(12400175)
    RunEvent(12400179, slot=0, args=(2401015,))
    RunEvent(12400179, slot=1, args=(2401016,))
    RunEvent(12400185)
    RunEvent(12400200, slot=2, args=(2400344, 52400980))
    RunEvent(12400200, slot=3, args=(2400371, 52400960))
    RunEvent(12400200, slot=4, args=(2400372, 52400990))
    RunEvent(12400200, slot=5, args=(2400373, 52400970))
    RunEvent(12400200, slot=6, args=(2400374, 52400950))
    RunEvent(12400200, slot=7, args=(2400375, 52400940))
    RunEvent(12400300)
    RunEvent(12400350, slot=0, args=(2401500, 12400450))
    RunEvent(12400350, slot=2, args=(2401503, 12400453))
    RunEvent(12400350, slot=3, args=(2401504, 12400454))
    RunEvent(12400350, slot=6, args=(2401506, 12400456))
    RunEvent(12400750)
    RunEvent(12400765)
    RunEvent(12400760)
    RunEvent(12400420)
    RunEvent(12400823)
    RunEvent(12400824)
    RunEvent(12400825)
    RunEvent(12400826)
    RunEvent(12400850, slot=0, args=(2407020, 2407021, 2407022, 12400130, 0, 0.0, 0, 0), arg_types='iiiiifii')
    RunEvent(12400850, slot=1, args=(2407025, 2407026, 2407027, 12400132, 0, 0.0, 0, 0), arg_types='iiiiifii')
    RunEvent(12400850, slot=2, args=(2407028, 2407029, 2407030, 12400131, 0, 0.0, 0, 0), arg_types='iiiiifii')
    RunEvent(12400850, slot=3, args=(2406700, 2406701, 2406702, 12400133, 0, 0.0, 0, 0), arg_types='iiiiifii')
    RunEvent(12400854)
    RunEvent(12400860)
    RunEvent(12405710)
    RunEvent(12400865, slot=0, args=(2400660,))
    RunEvent(12400865, slot=1, args=(2400661,))
    RunEvent(12400780, slot=0, args=(2400360,))
    RunEvent(12400780, slot=1, args=(2400361,))
    RunEvent(12400780, slot=2, args=(2400362,))
    RunEvent(12400780, slot=3, args=(2400363,))
    RunEvent(12400791, slot=0, args=(2400360,))
    RunEvent(12400791, slot=1, args=(2400361,))
    RunEvent(12400791, slot=2, args=(2400363,))
    RunEvent(12400797)
    RunEvent(12405210, slot=1, args=(2400116, 5696))
    RunEvent(12405210, slot=2, args=(2400122, 5696))
    RunEvent(12405210, slot=4, args=(2400125, 5696))
    RunEvent(12405210, slot=5, args=(2400127, 5696))
    RunEvent(12405210, slot=7, args=(2400161, 5696))
    RunEvent(12405220, slot=0, args=(2400137, 5552, 5553, 5554))
    RunEvent(12405220, slot=1, args=(2400210, 5555, 5556, 0))
    RunEvent(12405220, slot=2, args=(2400211, 5555, 5556, 0))
    RunEvent(12404100, slot=0, args=(2401900, 7405, 10012005))
    RunEvent(12404100, slot=1, args=(2401901, 7406, 10012006))
    AICommand(2400420, command_id=100, slot=0)
    RunEvent(12405600, slot=1, args=(2400400, 2402022, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=2, args=(2400400, 2402017, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=3, args=(2400126, 2402012, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=4, args=(2400127, 2402013, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=5, args=(2400128, 2402013, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=6, args=(2400136, 2402015, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=7, args=(2400137, 2402015, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=8, args=(2400125, 2404302, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=10, args=(2400231, 2404312, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=11, args=(2400508, 2404320, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=12, args=(2400508, 2404310, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=13, args=(2400120, 2402073, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=14, args=(2400121, 2402073, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=15, args=(2400392, 2402016, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=18, args=(2400401, 2402029, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=19, args=(2400401, 2402017, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=20, args=(2400106, 2404310, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=22, args=(2400122, 2402081, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=23, args=(2400116, 2404302, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=24, args=(2400211, 2402075, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405660)
    RunEvent(12405350, slot=0, args=(2400391, 2402310, 2409015, 2403105, 2402311))
    RunEvent(12405195)
    RunEvent(12405370, slot=0, args=(2400210,))
    RunEvent(12405370, slot=1, args=(2400211,))
    RunEvent(12405670, slot=0, args=(2400203, 2404332, 2404301, 5.0, 0.0), arg_types='iiiff')
    RunEvent(12405330, slot=0, args=(2400500,))
    RunEvent(12405360)
    RunEvent(12405365, slot=0, args=(2400374, 2404087, 2403108))
    RunEvent(12405365, slot=1, args=(2400375, 2404086, 2403107))
    RunEvent(12405850, slot=0, args=(2400450, 2401652, 2402061, 10, 12405521))
    RunEvent(12405810, slot=0, args=(2400408, 2402022, 2404083, 10, 12405520))
    RunEvent(12405820, slot=0, args=(2400408, 2404083))
    RunEvent(12405820, slot=1, args=(2400450, 2402061))
    RunEvent(12405840, slot=0, args=(2400408, 10, 12405520))
    RunEvent(12405840, slot=1, args=(2400450, 10, 12405521))
    RunEvent(12405240)
    RunEvent(12405241)
    RunEvent(12405680)
    RunEvent(12405682, slot=0, args=(2400107, 2400002, 6.0, 12405686, 0.0), arg_types='iifif')
    RunEvent(12405682, slot=2, args=(2400109, 2400001, 1.0, 12405688, 0.0), arg_types='iifif')
    RunEvent(12405682, slot=3, args=(2400110, 2400004, 1.0, 12405689, 0.0), arg_types='iifif')
    RunEvent(12405140)
    RunEvent(12405686, slot=0, args=(2400107,))
    RunEvent(12405686, slot=2, args=(2400109,))
    RunEvent(12405686, slot=3, args=(2400110,))
    RunEvent(12405690)
    RunEvent(12405130, slot=0, args=(2400107, 12405682, 0))
    RunEvent(12405130, slot=1, args=(2400111, 12405140, 0))
    RunEvent(12405130, slot=2, args=(2400109, 12405682, 2))
    RunEvent(12405130, slot=3, args=(2400110, 12405682, 3))
    RunEvent(12405130, slot=4, args=(2400106, 12405680, 0))
    RunEvent(12405600, slot=41, args=(2400410, 2402028, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=42, args=(2400420, 2402511, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=43, args=(2400423, 2402511, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=44, args=(2400501, 2402157, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=45, args=(2400502, 2402157, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=46, args=(2400503, 2402157, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=47, args=(2400504, 2402157, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=48, args=(2400505, 2402157, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=49, args=(2400506, 2402157, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=50, args=(2400507, 2402157, 3.0, 0.0), arg_types='iiff')
    RunEvent(12405700)
    RunEvent(12405701, slot=0, args=(2400398, 2404370))
    RunEvent(12405701, slot=1, args=(2400399, 2404371))
    RunEvent(12405600, slot=52, args=(2400600, 2402500, 1.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=53, args=(2400601, 2402500, 1.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=54, args=(2400602, 2402500, 1.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=55, args=(2400603, 2402507, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405600, slot=56, args=(2400603, 2402508, 5.0, 0.0), arg_types='iiff')
    RunEvent(12405380, slot=0, args=(2400604, 2402509, 2402502))
    RunEvent(12406900, slot=0, args=(2402103, 2402101, 20011001))
    RunEvent(12406900, slot=1, args=(2402104, 2402101, 20011001))
    RunEvent(12406900, slot=3, args=(2402107, 2402101, 20011001))
    RunEvent(12406900, slot=4, args=(2404301, 2402101, 20011001))
    RunEvent(12405000, slot=0, args=(2400205, 7010, 7013, 273150, 273140))
    RunEvent(12405000, slot=1, args=(2400156, 7014, 7018, 263252, 263251))
    RunEvent(12405010, slot=0, args=(2400205, 7012, 0, 273130))
    RunEvent(12405010, slot=1, args=(2400156, 7015, 1, 263250))
    RunEvent(12405020, slot=0, args=(2400207, 7010, 7013, 273120, 273110))
    RunEvent(12405020, slot=1, args=(2400126, 7010, 7013, 273120, 273110))
    RunEvent(12405020, slot=2, args=(2400203, 7010, 7013, 273120, 273110))
    RunEvent(12405020, slot=4, args=(2400119, 7010, 7013, 273120, 273110))
    RunEvent(12405030, slot=0, args=(2400207, 7012, 0, 273100))
    RunEvent(12405030, slot=1, args=(2400126, 7012, 1, 273100))
    RunEvent(12405030, slot=2, args=(2400203, 7012, 2, 273100))
    RunEvent(12405030, slot=4, args=(2400119, 7012, 4, 273100))
    RunEvent(12405335)
    RunEvent(12405120, slot=1, args=(2400156, 5569))
    RunEvent(12405120, slot=2, args=(2400162, 5569))
    RunEvent(12405120, slot=3, args=(2400220, 5557))
    RunEvent(12405120, slot=4, args=(2400116, 5557))
    RunEvent(12405120, slot=5, args=(2400114, 5557))
    RunEvent(12405120, slot=6, args=(2400127, 5557))
    RunEvent(12405120, slot=8, args=(2400139, 5557))
    RunEvent(12405120, slot=9, args=(2400137, 5557))
    RunEvent(12405320)
    RunEvent(12405250, slot=0, args=(12400168, 2406790, 12405175))
    RunEvent(12405251, slot=0, args=(12400177, 2406791, 12400178))
    RunEvent(12405251, slot=1, args=(12400157, 2406792, 12405179))
    RunEvent(12405259)
    RunEvent(12405260)
    RunEvent(12405262)
    RunEvent(12400410)
    RunEvent(12405263)
    RunEvent(12405430, slot=0, args=(2490, 2490, 7, 40, 12405500, 2400114), arg_types='hihiii')
    RunEvent(12405430, slot=1, args=(2491, 2491, 8, 40, 12405500, 2400114), arg_types='hihiii')
    RunEvent(12405430, slot=2, args=(2490, 2490, 7, 40, 12405501, 2400126), arg_types='hihiii')
    RunEvent(12405430, slot=3, args=(2491, 2491, 8, 40, 12405501, 2400126), arg_types='hihiii')
    RunEvent(12405430, slot=6, args=(2490, 2490, 7, 40, 12405503, 2400133), arg_types='hihiii')
    RunEvent(12405430, slot=7, args=(2491, 2491, 8, 40, 12405503, 2400133), arg_types='hihiii')
    RunEvent(12405430, slot=8, args=(2490, 2490, 7, 40, 12405504, 2400203), arg_types='hihiii')
    RunEvent(12405430, slot=9, args=(2491, 2491, 8, 40, 12405504, 2400203), arg_types='hihiii')
    RunEvent(12405430, slot=10, args=(2490, 2490, 7, 40, 12405505, 2400205), arg_types='hihiii')
    RunEvent(12405430, slot=11, args=(2491, 2491, 8, 40, 12405505, 2400205), arg_types='hihiii')
    RunEvent(12405430, slot=14, args=(2490, 2490, 7, 40, 12405507, 2400207), arg_types='hihiii')
    RunEvent(12405430, slot=15, args=(2491, 2491, 8, 40, 12405507, 2400207), arg_types='hihiii')
    RunEvent(12405430, slot=16, args=(2490, 2490, 7, 40, 12405508, 2400603), arg_types='hihiii')
    RunEvent(12405430, slot=17, args=(2491, 2491, 8, 40, 12405508, 2400603), arg_types='hihiii')
    RunEvent(12405400, slot=0, args=(2490, 2490, 7, 7003, 5907, 12405500, 12405530, 2400114), arg_types='hihiiiii')
    RunEvent(12405400, slot=1, args=(2491, 2491, 8, 7000, 5907, 12405500, 12405560, 2400114), arg_types='hihiiiii')
    RunEvent(12405400, slot=2, args=(2490, 2490, 7, 7003, 5907, 12405501, 12405531, 2400126), arg_types='hihiiiii')
    RunEvent(12405400, slot=3, args=(2491, 2491, 8, 7000, 5907, 12405501, 12405561, 2400126), arg_types='hihiiiii')
    RunEvent(12405400, slot=6, args=(2490, 2490, 7, 7003, 5907, 12405503, 12405533, 2400133), arg_types='hihiiiii')
    RunEvent(12405400, slot=7, args=(2491, 2491, 8, 7000, 5907, 12405503, 12405563, 2400133), arg_types='hihiiiii')
    RunEvent(12405400, slot=8, args=(2490, 2490, 7, 7003, 5907, 12405504, 12405534, 2400203), arg_types='hihiiiii')
    RunEvent(12405400, slot=9, args=(2491, 2491, 8, 7000, 5907, 12405504, 12405564, 2400203), arg_types='hihiiiii')
    RunEvent(12405400, slot=10, args=(2490, 2490, 7, 7003, 5907, 12405505, 12405535, 2400205), arg_types='hihiiiii')
    RunEvent(12405400, slot=11, args=(2491, 2491, 8, 7000, 5907, 12405505, 12405565, 2400205), arg_types='hihiiiii')
    RunEvent(12405400, slot=14, args=(2490, 2490, 7, 7003, 5907, 12405507, 12405537, 2400207), arg_types='hihiiiii')
    RunEvent(12405400, slot=15, args=(2491, 2491, 8, 7000, 5907, 12405507, 12405567, 2400207), arg_types='hihiiiii')
    RunEvent(12405400, slot=16, args=(2490, 2490, 7, 7003, 5907, 12405508, 12405538, 2400603), arg_types='hihiiiii')
    RunEvent(12405400, slot=17, args=(2491, 2491, 8, 7000, 5907, 12405508, 12405568, 2400603), arg_types='hihiiiii')
    RunEvent(12405460, slot=0, args=(10, 40, 12405530, 2400114, 0, 10), arg_types='iiiiBB')
    RunEvent(12405460, slot=1, args=(30, 40, 12405560, 2400114, 1, 11), arg_types='iiiiBB')
    RunEvent(12405460, slot=2, args=(10, 40, 12405531, 2400126, 0, 10), arg_types='iiiiBB')
    RunEvent(12405460, slot=3, args=(30, 40, 12405561, 2400126, 1, 11), arg_types='iiiiBB')
    RunEvent(12405460, slot=6, args=(10, 40, 12405533, 2400133, 0, 10), arg_types='iiiiBB')
    RunEvent(12405460, slot=7, args=(30, 40, 12405563, 2400133, 1, 11), arg_types='iiiiBB')
    RunEvent(12405460, slot=8, args=(10, 40, 12405534, 2400203, 0, 10), arg_types='iiiiBB')
    RunEvent(12405460, slot=9, args=(30, 40, 12405564, 2400203, 1, 11), arg_types='iiiiBB')
    RunEvent(12405460, slot=10, args=(10, 40, 12405535, 2400205, 0, 10), arg_types='iiiiBB')
    RunEvent(12405460, slot=11, args=(30, 40, 12405565, 2400205, 1, 11), arg_types='iiiiBB')
    RunEvent(12405460, slot=14, args=(10, 40, 12405537, 2400207, 0, 10), arg_types='iiiiBB')
    RunEvent(12405460, slot=15, args=(30, 40, 12405567, 2400207, 1, 11), arg_types='iiiiBB')
    RunEvent(12405460, slot=16, args=(10, 40, 12405538, 2400603, 0, 10), arg_types='iiiiBB')
    RunEvent(12405460, slot=17, args=(30, 40, 12405568, 2400603, 1, 11), arg_types='iiiiBB')
    RunEvent(12405790, slot=0, args=(2401150, 9802, 924110))
    RunEvent(12405790, slot=1, args=(2401151, 9801, 924110))
    RunEvent(12405790, slot=2, args=(2401152, 6001, 924113))
    RunEvent(12405790, slot=3, args=(2401153, 9802, 924110))
    RunEvent(12405790, slot=4, args=(2401154, 9801, 924113))
    RunEvent(12405800, slot=0, args=(2403310, 1439, 70000052, 9802))
    RunEvent(12405800, slot=1, args=(2403311, 1439, 70000053, 9801))
    RunEvent(12405800, slot=2, args=(2403312, 1439, 70000054, 6001))
    RunEvent(12405800, slot=3, args=(2403313, 1439, 70000072, 9802))
    RunEvent(12405800, slot=4, args=(2403314, 1439, 70000073, 9801))
    RunEvent(12404842)
    RunEvent(12404843)
    RunEvent(12401800)
    RunEvent(12401801)
    RunEvent(12401802)
    RunEvent(12401803)
    RunEvent(12404840)
    RunEvent(12404841)
    RunEvent(12404802)
    RunEvent(12404803)
    RunEvent(12404804)
    RunEvent(12404805)
    RunEvent(12404807)
    RunEvent(12404808)
    RunEvent(12404830)
    RunEvent(12401804)
    RunEvent(12404810, slot=0, args=(2400, 2400, 1, 80, 480, 490, 8020), arg_types='hihiiii')
    RunEvent(12404810, slot=1, args=(2401, 2401, 2, 150, 481, 491, 8000), arg_types='hihiiii')
    RunEvent(12404810, slot=2, args=(2402, 2402, 3, 150, 482, 492, 8010), arg_types='hihiiii')
    RunEvent(12404810, slot=3, args=(2403, 2403, 4, 200, 483, 493, 8030), arg_types='hihiiii')
    RunEvent(12404810, slot=4, args=(2404, 2404, 5, 200, 484, 494, 8040), arg_types='hihiiii')
    RunEvent(12404820, slot=0, args=(480, 490, 5, 10), arg_types='iiBB')
    RunEvent(12404820, slot=1, args=(481, 491, 6, 11), arg_types='iiBB')
    RunEvent(12404820, slot=2, args=(482, 492, 7, 12), arg_types='iiBB')
    RunEvent(12404820, slot=3, args=(483, 493, 8, 13), arg_types='iiBB')
    RunEvent(12404820, slot=4, args=(484, 494, 9, 14), arg_types='iiBB')
    RunEvent(12400800)
    RunEvent(12400801)
    RunEvent(12400840, slot=1, args=(70000052, 6030, 2400860))
    RunEvent(12400840, slot=2, args=(70000053, 6030, 2400861))
    RunEvent(12400840, slot=3, args=(70000054, 6030, 2400862))
    RunEvent(12400840, slot=4, args=(70000072, 6030, 2400863))
    RunEvent(12400840, slot=5, args=(70000073, 6030, 2400864))
    RunEvent(12400840, slot=6, args=(72400513, 6030, 2400749))
    RunEvent(12400630, slot=0, args=(2400765,))
    RunEvent(12400630, slot=1, args=(2400730,))
    RunEvent(12400630, slot=2, args=(2400754,))
    RunEvent(12400630, slot=3, args=(2400757,))
    RunEvent(12400630, slot=4, args=(2400750,))
    RunEvent(12400630, slot=5, args=(2400770,))
    RunEvent(12400630, slot=6, args=(2400772,))
    RunEvent(12400630, slot=7, args=(2400774,))
    RunEvent(12400630, slot=8, args=(2400700,))
    RunEvent(12400501)
    RunEvent(12400504)
    RunEvent(12400507)
    RunEvent(12400512)
    RunEvent(12400508)
    RunEvent(12400513)
    RunEvent(12400514)
    RunEvent(12400505)
    RunEvent(12400901)
    RunEvent(12400903)
    RunEvent(12400904)
    RunEvent(12400952)
    RunEvent(12400953)
    RunEvent(12400954)
    RunEvent(12400940, slot=0, args=(2400770,))
    RunEvent(12400940, slot=1, args=(2400774,))
    RunEvent(12400910, slot=0, args=(2400770,))
    RunEvent(12400910, slot=1, args=(2400772,))
    RunEvent(12400910, slot=2, args=(2400774,))
    RunEvent(12400915, slot=0, args=(2400770,))
    RunEvent(12400915, slot=1, args=(2400772,))
    RunEvent(12400915, slot=2, args=(2400774,))
    RunEvent(12400920, slot=0, args=(2400770,))
    RunEvent(12400920, slot=1, args=(2400774,))
    RunEvent(12400925, slot=0, args=(2400770,))
    RunEvent(12400925, slot=1, args=(2400772,))
    RunEvent(12400925, slot=2, args=(2400774,))
    RunEvent(12400930, slot=0, args=(2400770,))
    RunEvent(12400930, slot=1, args=(2400774,))
    RunEvent(12400935, slot=0, args=(2400770,))
    RunEvent(12400935, slot=1, args=(2400774,))
    RunEvent(12400521)
    RunEvent(12400525)
    RunEvent(12400523)
    RunEvent(12400524)
    RunEvent(12400531)
    RunEvent(12400522)
    RunEvent(12400810, slot=0, args=(2400750, 103085))
    RunEvent(12400810, slot=1, args=(2400754, 103088))
    RunEvent(12400810, slot=2, args=(2400757, 103088))
    RunEvent(12400810, slot=3, args=(2400758, 103089))
    RunEvent(12400805, slot=0, args=(2400750, 103080, 151))
    RunEvent(12400805, slot=1, args=(2400754, 103081, 152))
    RunEvent(12400805, slot=2, args=(2400757, 103081, 152))
    RunEvent(12400805, slot=3, args=(2400758, 103082, 153))
    RunEvent(12400830, slot=0, args=(2400750, 103086))
    RunEvent(12400830, slot=1, args=(2400754, 103086))
    RunEvent(12400830, slot=2, args=(2400757, 103086))
    RunEvent(12400830, slot=3, args=(2400758, 103086))
    RunEvent(12400610)
    RunEvent(12400611)
    RunEvent(12405150, slot=0, args=(2400755, 12405155))
    RunEvent(12405150, slot=1, args=(2400759, 12405156))
    RunEvent(12400612, slot=0, args=(2400755, 12405155))
    RunEvent(12400612, slot=1, args=(2400759, 12405156))
    RunEvent(12400614, slot=0, args=(2400755, 103076))
    RunEvent(12400614, slot=1, args=(2400759, 103076))
    RunEvent(12400616, slot=0, args=(2400755,))
    RunEvent(12400616, slot=1, args=(2400759,))
    RunEvent(12400618, slot=0, args=(2400755,))
    RunEvent(12400618, slot=1, args=(2400759,))
    RunEvent(12400620, slot=0, args=(2400755,))
    RunEvent(12400620, slot=1, args=(2400759,))
    RunEvent(12400625, slot=0, args=(2400755, 12405155))
    RunEvent(12400627, slot=0, args=(2400755, 12405155))
    RunEvent(12400627, slot=1, args=(2400759, 12405156))
    RunEvent(12405157)
    RunEvent(12405158)
    RunEvent(12405159)
    RunEvent(12400561)
    RunEvent(12400563)
    RunEvent(12400564)
    RunEvent(12400565)
    RunEvent(12400566)
    RunEvent(12400567)
    RunEvent(12400569)
    RunEvent(12400570)
    RunEvent(12400571)
    RunEvent(12400572)
    RunEvent(12400568)
    DisableFlag(72400310)
    DisableFlag(72400311)
    SetTeamType(2400700, TeamType.Ally)
    RunEvent(12400701)
    RunEvent(12400702)
    RunEvent(12400703)
    RunEvent(12400704)
    RunEvent(12400705)
    RunEvent(12400706)
    RunEvent(12400707)
    RunEvent(12400708, slot=0, args=(1164, 72400316, 1163, 1161, 0))
    RunEvent(12400708, slot=1, args=(1181, 72400317, 1190, 1183, 0))
    RunEvent(12400708, slot=2, args=(1304, 72400318, 1309, 1303, 1))
    RunEvent(12400708, slot=3, args=(1224, 72400319, 1223, 1222, 0))
    RunEvent(12400713, slot=0, args=(1164, 1163))
    RunEvent(12400713, slot=1, args=(1181, 1190))
    RunEvent(12400713, slot=2, args=(1304, 1309))
    RunEvent(12400713, slot=3, args=(1224, 1223))
    RunEvent(12400720)
    RunEvent(12400721)
    RunEvent(12400722)
    RunEvent(12400723)
    RunEvent(12400728)
    RunEvent(12400729)
    RunEvent(12400730)
    RunEvent(12400731)
    RunEvent(12400732, slot=3)
    RunEvent(12400737)
    RunEvent(12400738)
    RunEvent(12400580)
    RunEvent(12400581)
    RunEvent(12400582)
    RunEvent(12400401)
    RunEvent(12400402)
    RunEvent(12400403)
    RunEvent(12400591)
    RunEvent(12400592, slot=0, args=(2400760, 72400475))
    RunEvent(12400592, slot=1, args=(2400763, 72400476))
    RunEvent(12400593, slot=0, args=(2400760, 1341, 72400475))
    RunEvent(12400593, slot=1, args=(2400763, 1345, 72400476))
    RunEvent(12400594, slot=0, args=(2400760, 1342))
    RunEvent(12400594, slot=1, args=(2400763, 1346))
    RunEvent(12405271)
    RunEvent(12405272)
    RunEvent(12400990)
    GotoIfFlagOff(Label.L0, 12401800)
    DisableHitbox(2404121)
    Label(0)


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    PostDestruction(2404301, slot=1)
    DisableAnimations(2403950)
    DisableGravity(2403950)
    DisableCollision(2403950)
    DisableAnimations(2403951)
    DisableGravity(2403951)
    DisableCollision(2403951)
    DisableAnimations(2403952)
    DisableGravity(2403952)
    DisableCollision(2403952)
    RunEvent(12404000)
    RunEvent(12400500)
    RunEvent(12400560)
    RunEvent(12400900)
    RunEvent(12400520)
    RunEvent(12400622)
    RunEvent(12400624)
    RunEvent(12400629)
    RunEvent(12400650)
    RunEvent(12400700)
    RunEvent(12400590)
    DisableFlag(9432)
    DisableAnimations(2400899)
    DisableGravity(2400899)
    DisableCollision(2400899)
    SetNetworkUpdateRate(2400899, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.On)
    DisableAnimations(2400650)
    DisableGravity(2400650)
    DisableCollision(2400650)


@RestartOnRest
def Event12404000():
    """ 12404000: Event 12404000 """
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerInsightAmountLessThan(2, 50)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    EnableFlag(12404001)
    EnableFlag(12404002)
    EnableFlag(12404003)
    End()
    Label(0)
    IfPlayerInsightAmountLessThan(3, 40)
    GotoIfConditionTrue(Label.L1, input_condition=3)
    EnableFlag(12404001)
    EnableFlag(12404002)
    End()
    Label(1)
    IfPlayerInsightAmountLessThan(4, 15)
    EndIfConditionTrue(4)
    EnableFlag(12404002)


@NeverRestart
def Event12404100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12404100: Event 12404100 """
    DisableNetworkSync()
    IfActionButtonInRegion(0, action_button_id=ARG_4_7, region=ARG_0_3)
    DisplayDialog(ARG_8_11, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12400070(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12400070: Event 12400070 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_0_3, ARG_8_11)
    DisableObjectActivation(ARG_0_3, obj_act_id=ARG_12_15)
    NotifyDoorEventSoundDampening(ARG_0_3, state=DoorState.DoorOpening)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    Wait(0.0)


@NeverRestart
def Event12400080(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12400080: Event 12400080 """
    DisableNetworkSync()
    IfFlagOff(1, ARG_4_7)
    IfFlagOff(1, ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    IfActionButtonInRegion(2, action_button_id=ARG_12_15, region=ARG_0_3)
    IfFlagChange(3, ARG_4_7)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 3)
    DisplayDialog(10010160, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12400095(ARG_0_3: int):
    """ 12400095: Event 12400095 """
    DisableNetworkSync()
    IfActionButtonInRegion(0, action_button_id=2400040, region=ARG_0_3)
    DisplayDialog(10010171, anchor_entity=10000, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12400100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12400100: Event 12400100 """
    SkipLinesIfThisEventSlotOn(1)
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    DisableObjectActivation(ARG_0_3, obj_act_id=ARG_8_11)
    DisableObjectActivation(ARG_0_3, obj_act_id=ARG_12_15)


@NeverRestart
def Event12400125():
    """ 12400125: Event 12400125 """
    IfObjectActivated(-1, obj_act_id=12400162)
    IfObjectActivated(-1, obj_act_id=12400163)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 12400177)
    IfFlagOff(1, 12400178)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12400177)
    EnableFlag(12400178)
    ForceAnimation(2401207, 1)
    Wait(1.0)
    CreateObjectFX(920204, obj=2401207, model_point=200)
    CreateObjectFX(920205, obj=2401207, model_point=201)
    Wait(3.0)
    DisableFlag(12400178)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    Restart()


@NeverRestart
def Event12400126():
    """ 12400126: Event 12400126 """
    IfObjectActivated(-2, obj_act_id=12400162)
    IfObjectActivated(-2, obj_act_id=12400163)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(1, 12400177)
    IfFlagOff(1, 12400178)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12400177)
    EnableFlag(12400178)
    ForceAnimation(2401207, 2)
    Wait(1.0)
    CreateObjectFX(920204, obj=2401207, model_point=200)
    CreateObjectFX(920205, obj=2401207, model_point=201)
    Wait(3.0)
    DisableFlag(12400178)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    Restart()


@NeverRestart
def Event12400127():
    """ 12400127: Event 12400127 """
    DisableNetworkSync()
    IfFlagOn(1, 12400178)
    IfActionButtonInRegion(1, action_button_id=7100, region=2401006)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12400128():
    """ 12400128: Event 12400128 """
    GotoIfFlagOn(Label.L0, 12400177)
    EndOfAnimation(2401207, 2)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    End()
    Label(0)
    EndOfAnimation(2401207, 1)
    EnableObjectActivation(2401006, obj_act_id=2400000)


@NeverRestart
def Event12400130(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12400130: Event 12400130 """
    SkipLinesIfFlagOff(4, ARG_12_15)
    EndOfAnimation(ARG_0_3, ARG_4_7)
    DisableObjectActivation(ARG_0_3, obj_act_id=-1)
    NotifyDoorEventSoundDampening(ARG_0_3, state=DoorState.DoorOpening)
    End()
    IfObjectActivated(0, obj_act_id=ARG_8_11)
    WaitFrames(0)


@NeverRestart
def Event12400146():
    """ 12400146: Event 12400146 """
    IfFlagOn(1, 12400150)
    IfFlagOff(2, 12400150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 1)
    EndOfAnimation(2401101, 15)
    EnableObjectActivation(2401003, obj_act_id=2400000)
    DisableObjectActivation(2401004, obj_act_id=2400000)
    SkipLines(3)
    EndOfAnimation(2401101, 0)
    DisableObjectActivation(2401003, obj_act_id=2400000)
    EnableObjectActivation(2401004, obj_act_id=2400000)


@NeverRestart
def Event12400147():
    """ 12400147: Event 12400147 """
    IfFlagOn(3, 12400150)
    IfFlagOn(3, 12400151)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOn(1, 12400150)
    IfFlagOff(1, 12400151)
    IfCharacterInsideRegion(1, PLAYER, region=2402054)
    IfFlagOn(2, 12400150)
    IfFlagOff(2, 12400151)
    IfObjectActivated(2, obj_act_id=12400161)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
    EnableFlag(12400151)
    ForceAnimation(2401101, 1, wait_for_completion=True)
    ForceAnimation(2401101, 13, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=2402055)
    ForceAnimation(2401101, 14, wait_for_completion=True)
    DisableFlag(12400150)
    DisableFlag(12400151)
    EnableObjectActivation(2401003, obj_act_id=2400000)
    DisableObjectActivation(2401004, obj_act_id=2400000)
    Restart()


@NeverRestart
def Event12400148():
    """ 12400148: Event 12400148 """
    IfFlagOff(3, 12400150)
    IfFlagOn(3, 12400151)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOff(1, 12400150)
    IfFlagOff(1, 12400151)
    IfCharacterInsideRegion(1, PLAYER, region=2402055)
    IfFlagOff(2, 12400150)
    IfFlagOff(2, 12400151)
    IfObjectActivated(2, obj_act_id=12400160)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
    EnableFlag(12400151)
    ForceAnimation(2401101, 16, wait_for_completion=True)
    ForceAnimation(2401101, 17, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=2402054)
    ForceAnimation(2401101, 7, wait_for_completion=True)
    EnableFlag(12400150)
    DisableFlag(12400151)
    DisableObjectActivation(2401003, obj_act_id=2400000)
    EnableObjectActivation(2401004, obj_act_id=2400000)
    Restart()


@NeverRestart
def Event12400149():
    """ 12400149: Event 12400149 """
    DisableNetworkSync()
    IfFlagOn(1, 12400150)
    IfActionButtonInRegion(1, action_button_id=7100, region=2401003)
    IfFlagOff(2, 12400150)
    IfActionButtonInRegion(2, action_button_id=7100, region=2401004)
    IfFlagOn(3, 12400151)
    IfActionButtonInRegion(3, action_button_id=7100, region=2401003)
    IfFlagOn(4, 12400151)
    IfActionButtonInRegion(4, action_button_id=7100, region=2401004)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12400155():
    """ 12400155: Event 12400155 """
    IfObjectActivated(-1, obj_act_id=12400164)
    IfObjectActivated(-1, obj_act_id=12400165)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 12400157)
    IfFlagOff(1, 12405179)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12400157)
    EnableFlag(12405179)
    ForceAnimation(2401208, 1)
    Wait(1.0)
    CreateObjectFX(920204, obj=2401208, model_point=200)
    CreateObjectFX(920205, obj=2401208, model_point=201)
    Wait(3.0)
    DisableFlag(12405179)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    Restart()


@NeverRestart
def Event12400156():
    """ 12400156: Event 12400156 """
    IfObjectActivated(-2, obj_act_id=12400164)
    IfObjectActivated(-2, obj_act_id=12400165)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(1, 12400157)
    IfFlagOff(1, 12405179)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12400157)
    EnableFlag(12405179)
    ForceAnimation(2401208, 2)
    Wait(1.0)
    CreateObjectFX(920204, obj=2401208, model_point=200)
    CreateObjectFX(920205, obj=2401208, model_point=201)
    Wait(3.0)
    DisableFlag(12405179)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    Restart()


@NeverRestart
def Event12400158():
    """ 12400158: Event 12400158 """
    DisableNetworkSync()
    IfFlagOn(1, 12405179)
    IfActionButtonInRegion(1, action_button_id=7100, region=2401008)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12400159():
    """ 12400159: Event 12400159 """
    GotoIfFlagOn(Label.L0, 12400157)
    EndOfAnimation(2401208, 2)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    End()
    Label(0)
    EndOfAnimation(2401208, 1)
    EnableObjectActivation(2401008, obj_act_id=2400000)


@RestartOnRest
def Event12400760():
    """ 12400760: Event 12400760 """
    GotoIfFlagOff(Label.L0, 12400160)
    ForceAnimation(2400650, 7020, loop=True)
    EndOfAnimation(2401220, 1)
    DisableObjectActivation(2401014, obj_act_id=2400000)
    End()
    Label(0)
    ForceAnimation(2400650, 7022, loop=True)
    IfPlayerDoesNotHaveGood(1, 4011, including_box=False)
    IfActionButtonInRegion(1, action_button_id=2400030, region=2401220)
    IfPlayerHasGood(2, 4011, including_box=False)
    IfActionButtonInRegion(2, action_button_id=2400030, region=2401220)
    IfObjectActivated(3, obj_act_id=12400170)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=2)
    DisableObjectActivation(2401014, obj_act_id=2400000)
    ForceAnimation(2400650, 7024)
    WaitFrames(74)
    ForceAnimation(2400650, 7020, loop=True)
    WaitFrames(31)
    ForceAnimation(2401220, 1)
    WaitFrames(30)
    CreateObjectFX(920204, obj=2401220, model_point=200)
    CreateObjectFX(920205, obj=2401220, model_point=201)
    EnableFlag(12400160)
    EndIfFlagOn(12401800)
    DisableFlag(2400)
    DisableFlag(2401)
    DisableFlag(2405)
    DisableFlag(2406)
    End()
    Label(2)
    DisableObjectActivation(2401014, obj_act_id=2400000)
    RotateToFaceEntity(PLAYER, 2401014, animation=101310, wait_for_completion=False)
    Wait(1.0)
    ForceAnimation(2400650, 7023)
    ForceAnimation(2401014, 1)
    WaitFrames(105)
    ForceAnimation(2401220, 1)
    WaitFrames(24)
    ForceAnimation(2400650, 7022, loop=True)
    WaitFrames(6)
    CreateObjectFX(920204, obj=2401220, model_point=200)
    CreateObjectFX(920205, obj=2401220, model_point=201)
    DisplayDialog(10010174, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    EnableFlag(12400160)
    EndIfFlagOn(12401800)
    DisableFlag(2400)
    DisableFlag(2401)
    DisableFlag(2405)
    DisableFlag(2406)
    End()
    Label(1)
    DisplayDialog(10010173, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest
def Event12400161():
    """ 12400161: Event 12400161 """
    DisableNetworkSync()
    IfFlagOn(1, 12400160)
    IfActionButtonInRegion(1, action_button_id=7100, region=2401014)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest
def Event12400174():
    """ 12400174: Event 12400174 """
    GotoIfFlagOn(Label.L0, 12400168)
    EnableFlag(12400167)
    Label(0)


@NeverRestart
def Event12400175():
    """ 12400175: Event 12400175 """
    GotoIfFlagOff(Label.L0, 12400168)
    EndOfAnimation(2401209, 2)
    EnableFlag(12400169)
    Goto(Label.L1)
    Label(0)
    IfObjectActivated(-1, obj_act_id=12400172)
    IfObjectActivated(-1, obj_act_id=12400173)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(12400167)
    EnableFlag(12400169)
    EnableFlag(12400168)
    EnableFlag(12405175)
    DisableObjectActivation(2401015, obj_act_id=2400000)
    DisableObjectActivation(2401016, obj_act_id=2400000)
    ForceAnimation(2401209, 2)
    Wait(1.0)
    CreateObjectFX(920204, obj=2401209, model_point=200)
    CreateObjectFX(920205, obj=2401209, model_point=201)
    Wait(3.0)
    DisableFlag(12405175)
    EnableObjectActivation(2401015, obj_act_id=2400000)
    EnableObjectActivation(2401016, obj_act_id=2400000)
    Label(1)
    IfObjectActivated(-2, obj_act_id=12400172)
    IfObjectActivated(-2, obj_act_id=12400173)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(12400167)
    DisableFlag(12400168)
    EnableFlag(12405175)
    DisableObjectActivation(2401015, obj_act_id=2400000)
    DisableObjectActivation(2401016, obj_act_id=2400000)
    ForceAnimation(2401209, 1)
    Wait(1.0)
    CreateObjectFX(920204, obj=2401209, model_point=200)
    CreateObjectFX(920205, obj=2401209, model_point=201)
    Wait(3.0)
    DisableFlag(12400169)
    DisableFlag(12405175)
    EnableObjectActivation(2401015, obj_act_id=2400000)
    EnableObjectActivation(2401016, obj_act_id=2400000)
    Restart()


@RestartOnRest
def Event12400179(ARG_0_3: int):
    """ 12400179: Event 12400179 """
    DisableNetworkSync()
    IfFlagOn(1, 12405175)
    IfActionButtonInRegion(1, action_button_id=7100, region=ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=0.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12400185():
    """ 12400185: Event 12400185 """
    GotoIfThisEventOff(Label.L0)
    EndOfAnimation(2401012, 1)
    DisableObjectActivation(2401013, obj_act_id=2400000)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=12400123)
    ForceAnimation(2401012, 1)


@NeverRestart
def Event12400200(ARG_0_3: int, ARG_4_7: int):
    """ 12400200: Event 12400200 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableCharacter(ARG_0_3)
    End()
    Label(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagOn(1, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@NeverRestart
def Event12400250(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12400250: Event 12400250 """
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=ARG_0_3)
    DisplayDialog(ARG_4_7, anchor_entity=ARG_8_11, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)


@NeverRestart
def Event12400300():
    """ 12400300: Event 12400300 """
    GotoIfFlagOn(Label.L2, 9802)
    GotoIfFlagOn(Label.L1, 9801)
    GotoIfFlagOn(Label.L0, 9800)
    Label(0)
    EnableMapPart(2404000)
    DisableMapPart(2404001)
    DisableMapPart(2404002)
    DisableCharacter(2400321)
    DisableCharacter(2400322)
    DisableMapPart(2404750)
    DisableMapPart(2404751)
    Goto(Label.L3)
    Label(1)
    DisableMapPart(2404000)
    EnableMapPart(2404001)
    DisableMapPart(2404002)
    EnableCharacter(2400321)
    EnableCharacter(2400322)
    DisableBackread(2400350)
    DisableBackread(2400351)
    DisableBackread(2400352)
    DisableBackread(2400220)
    DisableBackread(2400116)
    DisableBackread(2400125)
    DisableMapPart(2404700)
    DisableMapPart(2404701)
    DeleteFX(2403400, erase_root_only=False)
    DeleteFX(2403401, erase_root_only=False)
    DeleteFX(2403402, erase_root_only=False)
    DeleteFX(2403403, erase_root_only=False)
    DeleteFX(2403404, erase_root_only=False)
    DeleteFX(2403405, erase_root_only=False)
    DeleteFX(2403406, erase_root_only=False)
    DeleteFX(2403407, erase_root_only=False)
    DeleteFX(2403408, erase_root_only=False)
    DeleteFX(2403409, erase_root_only=False)
    DeleteFX(2403410, erase_root_only=False)
    DeleteFX(2403411, erase_root_only=False)
    DeleteFX(2403412, erase_root_only=False)
    Goto(Label.L3)
    Label(2)
    DisableMapPart(2404000)
    DisableMapPart(2404001)
    EnableMapPart(2404002)
    EnableCharacter(2400321)
    EnableCharacter(2400322)
    DisableBackread(2400350)
    DisableBackread(2400351)
    DisableBackread(2400352)
    DisableBackread(2400220)
    DisableBackread(2400116)
    DisableBackread(2400125)
    DisableMapPart(2404700)
    DisableMapPart(2404701)
    Label(3)
    IfFlagChange(-1, 9800)
    IfFlagChange(-1, 9801)
    IfFlagChange(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@NeverRestart
def Event12400765():
    """ 12400765: Event 12400765 """
    IfFlagOn(-1, 9802)
    IfFlagOn(-1, 12404001)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    DisableObject(2400898)
    ForceAnimation(2400898, 0, loop=True)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.On)
    AddSpecialEffect(2400899, 5686, affect_npc_part_hp=False)
    EnableFlag(12405263)
    End()
    Label(0)
    EnableObject(2400898)
    ForceAnimation(2400898, 0, loop=True)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.Off)
    DisableFlag(12405263)


@RestartOnRest
def Event12400350(ARG_0_3: int, ARG_4_7: int):
    """ 12400350: Event 12400350 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_0_3, 0)
    DisableObjectActivation(ARG_0_3, obj_act_id=-1)
    EnableTreasure(ARG_0_3)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    WaitFrames(10)
    EnableTreasure(ARG_0_3)


@RestartOnRest
def Event12400401():
    """ 12400401: Event 12400401 """
    IfFlagOn(1, 72400440)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1400, 1402))
    EnableFlag(1401)
    ForceAnimation(2401200, 1, wait_for_completion=True)
    EnableFlag(12400131)
    SaveRequest()


@NeverRestart
def Event12400402():
    """ 12400402: Event 12400402 """
    IfFlagOn(1, 72400440)
    IfConditionTrue(0, input_condition=1)
    Move(2400830, destination=2402033, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)


@NeverRestart
def Event12400403():
    """ 12400403: Event 12400403 """
    EndIfThisEventOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 72400441)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(37000, host_only=False)


@NeverRestart
def Event12400410():
    """ 12400410: Event 12400410 """
    EndIfThisEventOn()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfCharacterHasSpecialEffect(0, PLAYER, 6421)
    RunEvent(9350, slot=0, args=(1,))


@NeverRestart
def Event12400420():
    """ 12400420: Event 12400420 """
    DisableMapSound(2406831)
    EndIfThisEventOn()
    IfFlagOn(0, 9801)
    Wait(4.0)
    EnableMapSound(2406831)


@NeverRestart
def Event12400750():
    """ 12400750: Event 12400750 """
    DisableMapSound(2406832)
    GotoIfThisEventOn(Label.L0)
    IfActionButtonInRegion(0, action_button_id=7030, region=2401210)
    EnableFlag(9180)
    WaitFrames(1)
    PlayCutsceneAndMovePlayerAndSetTimePeriod(24000020, CutsceneType.Skippable, 2402200, CATHEDRAL_WARD, player_id=10000, time_period_id=1)
    WaitFrames(1)
    DisableFlag(9180)
    EnableMapSound(2406832)
    Label(0)
    EndOfAnimation(2401210, 2)
    NotifyDoorEventSoundDampening(2401210, state=DoorState.DoorOpening)


@RestartOnRest
def Event12400780(ARG_0_3: int):
    """ 12400780: Event 12400780 """
    IfCharacterHuman(2, PLAYER)
    EndIfConditionFalse(2)
    IfCharacterAlive(1, ARG_0_3)
    IfAttacked(1, 10000, attacking_character=ARG_0_3)
    IfHealthEqual(1, PLAYER, 0.0)
    IfFlagOn(1, 9401)
    IfFlagOn(1, 9404)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9420)


@RestartOnRest
def Event12400791(ARG_0_3: int):
    """ 12400791: Event 12400791 """
    GotoIfFlagOn(Label.L0, 9802)
    EndIfFlagOn(9453)
    Label(0)
    DisableBackread(ARG_0_3)


@RestartOnRest
def Event12400797():
    """ 12400797: Event 12400797 """
    GotoIfFlagOn(Label.L0, 9802)
    SkipLinesIfFlagOff(4, 9453)
    DisableBackread(2400350)
    DisableBackread(2400351)
    DisableBackread(2400352)
    End()
    Label(0)
    DisableBackread(2400362)


@NeverRestart
def Event12400823():
    """ 12400823: Event 12400823 """
    IfFlagOn(1, 12400827)
    IfFlagOff(2, 12400827)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 1)
    EndOfAnimation(2401102, 30)
    EnableObjectActivation(2401104, obj_act_id=2400000)
    DisableObjectActivation(2401103, obj_act_id=2400000)
    SkipLines(3)
    EndOfAnimation(2401102, 0)
    DisableObjectActivation(2401104, obj_act_id=2400000)
    EnableObjectActivation(2401103, obj_act_id=2400000)


@NeverRestart
def Event12400824():
    """ 12400824: Event 12400824 """
    IfFlagOn(3, 12400827)
    IfFlagOn(3, 12400828)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOn(1, 12400827)
    IfFlagOff(1, 12400828)
    IfCharacterInsideRegion(1, PLAYER, region=2402058)
    IfFlagOn(2, 12400827)
    IfFlagOff(2, 12400828)
    IfObjectActivated(2, obj_act_id=12400169)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
    EnableFlag(12400828)
    ForceAnimation(2401102, 1, wait_for_completion=True)
    ForceAnimation(2401102, 28, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=2402059)
    ForceAnimation(2401102, 29, wait_for_completion=True)
    DisableFlag(12400827)
    DisableFlag(12400828)
    EnableObjectActivation(2401104, obj_act_id=2400000)
    DisableObjectActivation(2401103, obj_act_id=2400000)
    Restart()


@NeverRestart
def Event12400825():
    """ 12400825: Event 12400825 """
    IfFlagOff(3, 12400827)
    IfFlagOn(3, 12400828)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagOff(1, 12400827)
    IfFlagOff(1, 12400828)
    IfCharacterInsideRegion(1, PLAYER, region=2402059)
    IfFlagOff(2, 12400827)
    IfFlagOff(2, 12400828)
    IfObjectActivated(2, obj_act_id=12400168)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
    EnableFlag(12400828)
    ForceAnimation(2401102, 31, wait_for_completion=True)
    ForceAnimation(2401102, 32, wait_for_completion=True)
    IfAllPlayersOutsideRegion(0, region=2402058)
    ForceAnimation(2401102, 7, wait_for_completion=True)
    EnableFlag(12400827)
    DisableFlag(12400828)
    DisableObjectActivation(2401104, obj_act_id=2400000)
    EnableObjectActivation(2401103, obj_act_id=2400000)
    Restart()


@NeverRestart
def Event12400826():
    """ 12400826: Event 12400826 """
    DisableNetworkSync()
    IfFlagOn(1, 12400827)
    IfActionButtonInRegion(1, action_button_id=7100, region=2401104)
    IfFlagOff(2, 12400827)
    IfActionButtonInRegion(2, action_button_id=7100, region=2401103)
    IfFlagOn(3, 12400828)
    IfActionButtonInRegion(3, action_button_id=7100, region=2401104)
    IfFlagOn(4, 12400828)
    IfActionButtonInRegion(4, action_button_id=7100, region=2401103)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest
def Event12400850(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: float, ARG_24_27: int, ARG_28_31: int):
    """ 12400850: Event 12400850 """
    DeleteFX(ARG_0_3, erase_root_only=False)
    DeleteFX(ARG_4_7, erase_root_only=False)
    DeleteFX(ARG_8_11, erase_root_only=False)
    SkipLinesIfFlagOff(3, ARG_12_15)
    CreateFX(ARG_4_7)
    CreateFX(ARG_8_11)
    End()
    IfObjectActivated(0, obj_act_id=ARG_16_19)
    Wait(ARG_20_23)
    CreateFX(ARG_0_3)
    CreateTemporaryFX(ARG_28_31, anchor_entity=ARG_24_27, anchor_type=CoordEntityType.Region, model_point=-1)
    Wait(4.0)
    CreateFX(ARG_4_7)
    CreateFX(ARG_8_11)


@RestartOnRest
def Event12400854():
    """ 12400854: Event 12400854 """
    DeleteFX(2406711, erase_root_only=False)
    DeleteFX(2406712, erase_root_only=False)
    DeleteFX(2406713, erase_root_only=False)
    SkipLinesIfFlagOff(3, 12400133)
    CreateFX(2406712)
    CreateFX(2406713)
    End()
    IfObjectActivated(0, obj_act_id=12400112)
    Wait(6.0)
    CreateFX(2406711)
    CreateTemporaryFX(920206, anchor_entity=2401204, anchor_type=CoordEntityType.Object, model_point=200)
    CreateTemporaryFX(920207, anchor_entity=2401204, anchor_type=CoordEntityType.Object, model_point=201)
    Wait(4.0)
    CreateFX(2406712)
    CreateFX(2406713)


@RestartOnRest
def Event12405000(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12405000: Event 12405000 """
    SetAIParamID(ARG_0_3, ARG_12_15)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True)
    IfEntityWithinDistance(-1, 10000, ARG_0_3, radius=3.0)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(ARG_0_3, ARG_16_19)
    ForceAnimation(ARG_0_3, ARG_8_11, loop=True)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event12405010(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12405010: Event 12405010 """
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(ARG_0_3, ARG_12_15)
    ForceAnimation(ARG_0_3, ARG_4_7)
    StopEvent(12405000, slot=ARG_8_11)


@NeverRestart
def Event12405020(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12405020: Event 12405020 """
    IfFlagOn(0, 9801)
    SetAIParamID(ARG_0_3, ARG_12_15)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True)
    IfEntityWithinDistance(-1, 10000, ARG_0_3, radius=1.0)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(ARG_0_3, ARG_16_19)
    ForceAnimation(ARG_0_3, ARG_8_11, loop=True)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Normal)
    Restart()


@NeverRestart
def Event12405030(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12405030: Event 12405030 """
    IfFlagOn(0, 9801)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(ARG_0_3, ARG_12_15)
    ForceAnimation(ARG_0_3, ARG_4_7)
    StopEvent(12405020, slot=ARG_8_11)


@RestartOnRest
def Event12405060(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12405060: Event 12405060 """
    SetAIParamID(ARG_0_3, ARG_12_15)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True)
    IfEntityWithinDistance(1, 10000, ARG_0_3, radius=3.0)
    IfHasAIStatus(1, 2400160, ai_status=AIStatusType.Battle)
    IfAttacked(2, ARG_0_3, attacking_character=10000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(ARG_0_3, ARG_16_19)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(ARG_0_3, ARG_8_11)


@RestartOnRest
def Event12405080(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: float):
    """ 12405080: Event 12405080 """
    IfFlagOn(0, ARG_0_3)
    AICommand(ARG_4_7, command_id=10, slot=0)
    SetNest(ARG_4_7, ARG_8_11)
    IfCharacterInsideRegion(-1, ARG_4_7, region=ARG_8_11)
    IfEntityWithinDistance(-1, ARG_4_7, 10000, radius=ARG_12_15)
    IfAttacked(-1, ARG_4_7, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    AICommand(ARG_4_7, command_id=-1, slot=0)
    ReplanAI(ARG_4_7)


@RestartOnRest
def Event12405100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12405100: Event 12405100 """
    IfCharacterInsideRegion(1, PLAYER, region=2404306)
    IfFlagOn(2, 12405431)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfHasAIStatus(3, ARG_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=3)
    DisableAI(ARG_0_3)
    SkipLinesIfFinishedConditionTrue(1, 2)
    SetNest(ARG_0_3, ARG_4_7)
    SkipLinesIfFinishedConditionTrue(1, 1)
    SetNest(ARG_0_3, ARG_8_11)
    AICommand(ARG_0_3, command_id=10, slot=0)
    EnableAI(ARG_0_3)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(-2, ARG_0_3, region=ARG_4_7)
    IfCharacterInsideRegion(-2, ARG_0_3, region=ARG_8_11)
    IfConditionTrue(0, input_condition=-2)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405110(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12405110: Event 12405110 """
    IfObjectNotDestroyed(0, ARG_12_15)
    DisableFlag(ARG_20_23)
    SkipLinesIfFlagOff(2, ARG_20_23)
    EndOfAnimation(ARG_4_7, 0)
    SkipLines(9)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_0_3)
    IfObjectNotDestroyed(1, ARG_12_15)
    IfConditionTrue(1, input_condition=-1)
    IfObjectDestroyed(2, ARG_12_15)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 2)
    SkipLinesIfFinishedConditionTrue(2, 1)
    ForceAnimation(ARG_4_7, 0, wait_for_completion=True)
    End()
    PlaySoundEffect(anchor_entity=ARG_4_7, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(ARG_4_7, 0, wait_for_completion=True)
    EnableFlag(ARG_20_23)
    CreateTemporaryFX(150005, anchor_entity=ARG_4_7, anchor_type=CoordEntityType.Object, model_point=101)
    DeleteFX(ARG_8_11, erase_root_only=False)
    EndIfFinishedConditionTrue(2)
    Wait(0.20000000298023224)
    CreatePlayLog(ARG_24_27)
    ShootProjectile(owner_entity=2400000, projectile_id=ARG_12_15, model_point=101, behavior_id=5071, launch_angle_x=0, launch_angle_y=ARG_16_19, launch_angle_z=0)
    PlaySoundEffect(anchor_entity=ARG_12_15, sound_type=SoundType.a_Ambient, sound_id=243007000)
    CreateTemporaryFX(929208, anchor_entity=ARG_12_15, anchor_type=CoordEntityType.Object, model_point=101)
    Wait(0.699999988079071)
    ShootProjectile(owner_entity=2400000, projectile_id=ARG_12_15, model_point=101, behavior_id=5071, launch_angle_x=0, launch_angle_y=ARG_16_19, launch_angle_z=0)
    PlaySoundEffect(anchor_entity=ARG_12_15, sound_type=SoundType.a_Ambient, sound_id=243007000)
    CreateTemporaryFX(929208, anchor_entity=ARG_12_15, anchor_type=CoordEntityType.Object, model_point=101)
    Wait(0.699999988079071)
    ShootProjectile(owner_entity=2400000, projectile_id=ARG_12_15, model_point=101, behavior_id=5071, launch_angle_x=0, launch_angle_y=ARG_16_19, launch_angle_z=0)
    PlaySoundEffect(anchor_entity=ARG_12_15, sound_type=SoundType.a_Ambient, sound_id=243007000)
    CreateTemporaryFX(929208, anchor_entity=ARG_12_15, anchor_type=CoordEntityType.Object, model_point=101)
    Wait(3.0)
    IfCharacterOutsideRegion(3, PLAYER, region=ARG_0_3)
    IfObjectNotDestroyed(3, ARG_12_15)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(ARG_20_23)
    PlaySoundEffect(anchor_entity=ARG_12_15, sound_type=SoundType.a_Ambient, sound_id=243007001)
    PlaySoundEffect(anchor_entity=ARG_4_7, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(ARG_4_7, 1, wait_for_completion=True)
    Restart()


@NeverRestart
def Event12405120(ARG_0_3: int, ARG_4_7: int):
    """ 12405120: Event 12405120 """
    WaitFrames(1)
    AddSpecialEffect(ARG_0_3, ARG_4_7, affect_npc_part_hp=False)


@RestartOnRest
def Event12405130(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12405130: Event 12405130 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2402151)
    IfConditionTrue(0, input_condition=1)
    EnableAI(ARG_0_3)
    StopEvent(ARG_4_7, slot=ARG_8_11)


@RestartOnRest
def Event12405140():
    """ 12405140: Event 12405140 """
    GotoIfThisEventOff(Label.L0)
    SetAIParamID(2400111, 263381)
    End()
    Label(0)
    IfCharacterBackreadEnabled(0, 2400111)
    DisableAI(2400111)
    IfFlagOn(1, 12405681)
    IfDamageType(2, attacked_entity=2400111, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfEntityWithinDistance(3, 10000, 2400111, radius=5.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2400111)
    EndIfFinishedConditionFalse(1)
    SetAIParamID(2400111, 263380)
    IfCharacterInsideRegion(-2, 2400111, region=2402046)
    IfDamageType(-2, attacked_entity=2400111, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfEntityWithinDistance(-2, 10000, 2400111, radius=5.0)
    IfConditionTrue(0, input_condition=-2)
    SetAIParamID(2400111, 263381)
    ReplanAI(2400111)


@NeverRestart
def Event12405150(ARG_0_3: int, ARG_4_7: int):
    """ 12405150: Event 12405150 """
    WaitFrames(10)
    GotoIfThisEventSlotOff(Label.L0)
    EndIfFlagOn(1210)
    EnableBackread(2400756)
    DisableBackread(ARG_0_3)
    End()
    Label(0)
    IfFlagOn(0, ARG_4_7)
    EnableBackread(2400756)
    EnableInvincibility(ARG_0_3)
    IfCharacterBackreadEnabled(0, 2400756)
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionTrue(Label.L1, input_condition=15)
    WaitFrames(60)
    DisableBackread(ARG_0_3)
    End()
    Label(1)
    ForceAnimation(ARG_0_3, 103073, wait_for_completion=True)
    DisableBackread(ARG_0_3)
    Move(2400756, destination=2404507, model_point=-1, destination_type=CoordEntityType.Region)
    EnableGravity(2400756)
    ForceAnimation(2400756, 3030)
    EnableAI(2400756)
    SetNest(2400756, 2404507)
    DisableFlagRange((1200, 1219))
    EnableFlag(1207)
    EnableFlag(9432)
    SaveRequest()


@NeverRestart
def Event12405157():
    """ 12405157: Event 12405157 """
    IfCharacterHasSpecialEffect(-1, 2400755, 153)
    IfCharacterHasSpecialEffect(-1, 2400759, 153)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(0)


@NeverRestart
def Event12405158():
    """ 12405158: Event 12405158 """
    IfEventValueComparison(0, 72400372, bit_count=2, comparison_type=ComparisonType.NotEqual, value=0)
    WaitFrames(0)


@NeverRestart
def Event12405159():
    """ 12405159: Event 12405159 """
    IfCharacterHasSpecialEffect(0, 2400760, 151)
    IfCharacterDoesNotHaveSpecialEffect(0, 2400760, 151)
    IfCharacterBackreadDisabled(2, 2400760)
    RestartIfConditionTrue(2)
    EnableFlag(12405160)


@RestartOnRest
def Event12405195():
    """ 12405195: Event 12405195 """
    IfCharacterInsideRegion(1, 2400203, region=2402411)
    IfCharacterInsideRegion(2, 2400203, region=2402412)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    IfCharacterInsideRegion(0, 2400203, region=2402411)
    IfCharacterInsideRegion(0, 2400203, region=2402406)
    IfFlagOn(3, 12400169)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    ChangePatrolBehavior(2400203, patrol_information_id=2403111)
    Goto(Label.L1)
    Label(0)
    ChangePatrolBehavior(2400203, patrol_information_id=2403112)
    Restart()
    Label(1)
    IfCharacterInsideRegion(0, 2400203, region=2402412)
    IfCharacterInsideRegion(0, 2400203, region=2402407)
    IfFlagOn(4, 12400169)
    GotoIfConditionTrue(Label.L2, input_condition=4)
    ChangePatrolBehavior(2400203, patrol_information_id=2403110)
    Goto(Label.L3)
    Label(2)
    ChangePatrolBehavior(2400203, patrol_information_id=2403113)
    Label(3)
    Restart()


@RestartOnRest
def Event12405200():
    """ 12405200: Event 12405200 """
    IfFlagOff(0, 12400168)
    WaitFrames(1)
    ActivateObjectWithSpecificCharacter(2401015, objact_id=2400000, relative_index=-1, character=2400113)
    Restart()


@RestartOnRest
def Event12405210(ARG_0_3: int, ARG_4_7: int):
    """ 12405210: Event 12405210 """
    IfFlagOff(1, 12404002)
    EndIfConditionTrue(1)
    SetDisplayMask(ARG_0_3, bit_index=3, switch_type=OnOffChange.On)
    SetDisplayMask(ARG_0_3, bit_index=4, switch_type=OnOffChange.Off)
    AddSpecialEffect(ARG_0_3, ARG_4_7, affect_npc_part_hp=False)


@RestartOnRest
def Event12405220(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12405220: Event 12405220 """
    IfFlagOff(1, 12404002)
    EndIfConditionTrue(1)
    AddSpecialEffect(ARG_0_3, ARG_4_7, affect_npc_part_hp=False)
    AddSpecialEffect(ARG_0_3, ARG_8_11, affect_npc_part_hp=False)
    AddSpecialEffect(ARG_0_3, ARG_12_15, affect_npc_part_hp=False)


@RestartOnRest
def Event12405240():
    """ 12405240: Event 12405240 """
    IfCharacterInsideRegion(1, 2400203, region=2404311)
    IfCharacterInsideRegion(2, PLAYER, region=2404311)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(5, input_condition=-1)
    IfCharacterNotTargeting(3, 2400203, PLAYER)
    IfCharacterTargeting(4, 2400203, PLAYER)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(5, input_condition=-2)
    IfFlagOff(5, 9801)
    IfConditionTrue(0, input_condition=5)
    PlaySoundEffect(anchor_entity=2404290, sound_type=SoundType.a_Ambient, sound_id=20011002)
    WaitFrames(40)
    EndIfFinishedConditionTrue(4)
    ForceAnimation(2400203, 3039)


@RestartOnRest
def Event12405241():
    """ 12405241: Event 12405241 """
    IfFlagOn(1, 12404003)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableBackread(2400650)
    End()
    Label(0)
    EnableBackread(2400650)


@RestartOnRest
def Event12405250(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12405250: Event 12405250 """
    IfFlagOff(1, ARG_0_3)
    IfFlagOn(2, ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisableNavmeshType(ARG_4_7, NavmeshType.Solid)
    SkipLines(1)
    EnableNavmeshType(ARG_4_7, NavmeshType.Solid)
    IfFlagOn(0, ARG_8_11)
    Restart()


@RestartOnRest
def Event12405251(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12405251: Event 12405251 """
    IfFlagOn(1, ARG_0_3)
    IfFlagOff(2, ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisableNavmeshType(ARG_4_7, NavmeshType.Solid)
    SkipLines(1)
    EnableNavmeshType(ARG_4_7, NavmeshType.Solid)
    IfFlagOn(0, ARG_8_11)
    Restart()


@RestartOnRest
def Event12405259():
    """ 12405259: Event 12405259 """
    DisableNetworkSync()
    IfHasTAEEvent(1, 2400899, tae_event_id=700)
    IfCharacterHasSpecialEffect(1, PLAYER, 5577)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.YouLose)
    Restart()


@RestartOnRest
def Event12405260():
    """ 12405260: Event 12405260 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2402018)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(2)
    ForceAnimation(2400899, 3000)
    WaitFrames(250)
    Restart()


@RestartOnRest
def Event12405261():
    """ 12405261: Event 12405261 """
    IfAttacked(0, 10000, attacking_character=2402018)
    Wait(3.0)
    ForceAnimation(PLAYER, 9580, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event12405262():
    """ 12405262: Event 12405262 """
    IfFlagOn(1, 12405263)
    IfHasTAEEvent(1, 2400899, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.Off)
    AddSpecialEffect(2400899, 5687, affect_npc_part_hp=False)
    CancelSpecialEffect(2400899, 5686)
    IfHasTAEEvent(0, 2400899, tae_event_id=20)
    AddSpecialEffect(2400899, 5686, affect_npc_part_hp=False)
    CancelSpecialEffect(2400899, 5687)
    Restart()


@RestartOnRest
def Event12405263():
    """ 12405263: Event 12405263 """
    IfHasTAEEvent(1, 2400899, tae_event_id=710)
    IfPlayerHasGood(1, 4311, including_box=False)
    IfConditionTrue(0, input_condition=1)
    EnableImmortality(PLAYER)
    WaitFrames(30)
    EnableFlag(9180)
    WaitFrames(1)
    GotoIfMultiplayer(Label.L0)
    PlayCutscene(24000000, skippable=True, fade_out=False, player_id=PLAYER)
    Goto(Label.L1)
    Label(0)
    PlayCutscene(24000000, skippable=False, fade_out=False, player_id=PLAYER)
    Label(1)
    WaitFrames(1)
    DisableFlag(9180)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EnableFlag(12401000)
    MovePlayerToRespawnPoint(3402959)


@RestartOnRest
def Event12405270():
    """ 12405270: Event 12405270 """
    IfCharacterInsideRegion(0, PLAYER, region=2402190)
    CreatePlayLog(26)


@RestartOnRest
def Event12405271():
    """ 12405271: Event 12405271 """
    IfCharacterInsideRegion(0, PLAYER, region=2402191)
    CreatePlayLog(56)


@RestartOnRest
def Event12405272():
    """ 12405272: Event 12405272 """
    IfCharacterInsideRegion(0, PLAYER, region=2402192)
    CreatePlayLog(90)


@RestartOnRest
def Event12405273():
    """ 12405273: Event 12405273 """
    IfCharacterInsideRegion(0, PLAYER, region=2402193)
    CreatePlayLog(2)


@RestartOnRest
def Event12405289():
    """ 12405289: Event 12405289 """
    SetTeamType(2400000, TeamType.Human)


@RestartOnRest
def Event12405300(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12405300: Event 12405300 """
    IfCharacterInsideRegion(0, ARG_0_3, region=ARG_4_7)
    ChangePatrolBehavior(ARG_0_3, patrol_information_id=ARG_8_11)
    DisableFlag(ARG_12_15)


@RestartOnRest
def Event12405320():
    """ 12405320: Event 12405320 """
    IfFlagOn(1, 12405300)
    IfFlagOn(2, 12405301)
    IfFlagOn(3, 12405302)
    IfFlagOn(4, 12405303)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterBackreadDisabled(0, 2400300)
    IfCharacterBackreadEnabled(0, 2400300)
    IfFlagOn(5, 12405300)
    IfFlagOn(6, 12405301)
    IfFlagOn(7, 12405302)
    IfFlagOn(8, 12405303)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(-2, input_condition=7)
    IfConditionTrue(-2, input_condition=8)
    IfConditionTrue(0, input_condition=-2)
    Wait(2.0)
    SkipLinesIfFinishedConditionFalse(2, 5)
    ChangePatrolBehavior(2400300, patrol_information_id=2403101)
    Restart()
    SkipLinesIfFinishedConditionFalse(2, 6)
    ChangePatrolBehavior(2400300, patrol_information_id=2403102)
    Restart()
    SkipLinesIfFinishedConditionFalse(2, 7)
    ChangePatrolBehavior(2400300, patrol_information_id=2403103)
    Restart()
    SkipLinesIfFinishedConditionFalse(2, 8)
    ChangePatrolBehavior(2400300, patrol_information_id=2403104)
    Restart()


@RestartOnRest
def Event12405330(ARG_0_3: int):
    """ 12405330: Event 12405330 """
    ForceAnimation(ARG_0_3, 7000, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=4.0)
    IfConditionTrue(-1, input_condition=1)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(ARG_0_3, 7001)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405335():
    """ 12405335: Event 12405335 """
    IfCharacterBackreadEnabled(0, 2400421)
    DisableAI(2400421)
    IfCharacterInsideRegion(1, PLAYER, region=2402031)
    IfEntityWithinDistance(2, 10000, 2400421, radius=5.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(2400421, 3011)
    EnableAI(2400421)


@RestartOnRest
def Event12405350(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12405350: Event 12405350 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_16_19)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    SetNest(ARG_0_3, ARG_8_11)
    ChangePatrolBehavior(ARG_0_3, patrol_information_id=ARG_12_15)
    EndIfThisEventSlotOn()
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405360():
    """ 12405360: Event 12405360 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterBackreadEnabled(0, 2400371)
    AddSpecialEffect(2400371, 5000, affect_npc_part_hp=False)
    IfHasAIStatus(0, 2400371, ai_status=AIStatusType.Battle)
    Label(0)
    SetNest(2400371, 2404085)
    ChangePatrolBehavior(2400371, patrol_information_id=2403106)
    IfCharacterInsideRegion(0, 2400371, region=2404085)
    CancelSpecialEffect(2400371, 5000)
    AICommand(2400371, command_id=-1, slot=0)
    ReplanAI(2400371)


@RestartOnRest
def Event12405365(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12405365: Event 12405365 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterBackreadEnabled(0, ARG_0_3)
    AddSpecialEffect(ARG_0_3, 5000, affect_npc_part_hp=False)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Battle)
    Label(0)
    SetNest(ARG_0_3, ARG_4_7)
    ChangePatrolBehavior(ARG_0_3, patrol_information_id=ARG_8_11)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(0, ARG_0_3, region=ARG_4_7)
    CancelSpecialEffect(ARG_0_3, 5000)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405370(ARG_0_3: int):
    """ 12405370: Event 12405370 """
    IfFlagOn(0, 9802)
    DisableBackread(ARG_0_3)


@NeverRestart
def Event12405380(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12405380: Event 12405380 """
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetNest(ARG_0_3, ARG_4_7)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Normal)
    SetNest(ARG_0_3, ARG_8_11)
    Restart()


@NeverRestart
def Event12400865(ARG_0_3: int):
    """ 12400865: Event 12400865 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableBackread(ARG_0_3)
    DisableCharacter(ARG_0_3)
    DropMandatoryTreasure(ARG_0_3)
    End()
    Label(0)
    IfCharacterDead(0, ARG_0_3)
    Wait(0.0)


@RestartOnRest
def Event12405400(ARG_0_1: short, ARG_4_7: int, ARG_8_9: short, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 12405400: Event 12405400 """
    IfFlagOn(0, ARG_20_23)
    IfCharacterPartHealthLessThanOrEqual(1, ARG_28_31, npc_part_id=ARG_4_7, value=0)
    IfAttacked(1, ARG_28_31, attacking_character=10000)
    IfFlagOn(1, ARG_24_27)
    IfHealthLessThanOrEqual(2, ARG_28_31, 0.0)
    IfFlagOn(2, ARG_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagOn(2, ARG_20_23)
    SetNPCPartHealth(ARG_28_31, npc_part_id=ARG_4_7, desired_hp=1, overwrite_max=False)
    Restart()
    CreateNPCPart(ARG_28_31, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=9999999, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(ARG_28_31, npc_part_id=ARG_4_7, material_special_effect_id=65, material_fx_id=65)
    ResetAnimation(ARG_28_31, disable_interpolation=False)
    ForceAnimation(ARG_28_31, ARG_12_15)
    IfHasTAEEvent(0, ARG_28_31, tae_event_id=400)
    AddSpecialEffect(ARG_28_31, ARG_16_19, affect_npc_part_hp=False)
    DisableFlag(ARG_24_27)
    IfHasTAEEvent(0, ARG_28_31, tae_event_id=300)
    SetNPCPartHealth(ARG_28_31, npc_part_id=ARG_4_7, desired_hp=80, overwrite_max=True)
    SetNPCPartEffects(ARG_28_31, npc_part_id=ARG_4_7, material_special_effect_id=64, material_fx_id=64)
    CancelSpecialEffect(ARG_28_31, ARG_16_19)
    AICommand(ARG_28_31, command_id=-1, slot=0)
    ReplanAI(ARG_28_31)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12405430(ARG_0_1: short, ARG_4_7: int, ARG_8_9: short, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12405430: Event 12405430 """
    IfEntityWithinDistance(1, ARG_20_23, 10000, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(ARG_20_23, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=ARG_12_15, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(ARG_20_23, npc_part_id=ARG_4_7, material_special_effect_id=64, material_fx_id=64)
    EnableFlag(ARG_16_19)


@RestartOnRest
def Event12405460(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_16: uchar, ARG_17_17: uchar):
    """ 12405460: Event 12405460 """
    SetHitboxMask(ARG_12_15, bit_index=ARG_16_16, switch_type=OnOffChange.On)
    SetHitboxMask(ARG_12_15, bit_index=ARG_17_17, switch_type=OnOffChange.Off)
    IfHasTAEEvent(0, ARG_12_15, tae_event_id=ARG_0_3)
    EnableFlag(ARG_8_11)
    SetHitboxMask(ARG_12_15, bit_index=ARG_16_16, switch_type=OnOffChange.Off)
    SetHitboxMask(ARG_12_15, bit_index=ARG_17_17, switch_type=OnOffChange.On)
    IfHasTAEEvent(0, ARG_12_15, tae_event_id=ARG_4_7)
    DisableFlag(ARG_8_11)
    Restart()


@RestartOnRest
def Event12405790(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12405790: Event 12405790 """
    DeleteObjectFX(ARG_0_3, erase_root=True)
    EndIfFlagOn(ARG_4_7)
    CreateObjectFX(ARG_8_11, obj=ARG_0_3, model_point=200)


@RestartOnRest
def Event12405800(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12405800: Event 12405800 """
    DisableMapSound(ARG_0_3)
    EndIfFlagOn(ARG_12_15)
    IfFlagOff(1, ARG_4_7)
    IfFlagOff(1, ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(ARG_0_3)
    IfFlagOn(-1, ARG_4_7)
    IfFlagOn(-1, ARG_8_11)
    IfConditionTrue(0, input_condition=-1)
    DisableMapSound(ARG_0_3)
    Restart()


@RestartOnRest
def Event12405810(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12405810: Event 12405810 """
    EndIfFlagOn(ARG_16_19)
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    SetNest(ARG_0_3, ARG_8_11)
    AICommand(ARG_0_3, command_id=ARG_12_15, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405820(ARG_0_3: int, ARG_4_7: int):
    """ 12405820: Event 12405820 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterInsideRegion(0, ARG_0_3, region=ARG_4_7)
    Label(0)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405840(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12405840: Event 12405840 """
    EndIfFlagOn(ARG_8_11)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(2, ARG_8_11)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    IfHasAIStatus(3, ARG_0_3, ai_status=AIStatusType.Normal)
    IfFlagOn(4, ARG_8_11)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(4)
    AICommand(ARG_0_3, command_id=ARG_4_7, slot=0)
    ReplanAI(ARG_0_3)
    Restart()


@RestartOnRest
def Event12405850(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12405850: Event 12405850 """
    EndIfFlagOn(ARG_16_19)
    GotoIfThisEventSlotOn(Label.L0)
    ForceAnimation(ARG_0_3, 7013, loop=True)
    IfObjectDestroyed(-1, ARG_4_7)
    IfEntityWithinDistance(-1, 10000, ARG_0_3, radius=4.0)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(0)
    ForceAnimation(ARG_0_3, 7012)
    Label(0)
    SetNest(ARG_0_3, ARG_8_11)
    ForceAnimation(ARG_0_3, 7011)
    ForceAnimation(ARG_0_3, 7012)
    AICommand(ARG_0_3, command_id=ARG_12_15, slot=0)
    ReplanAI(ARG_0_3)


@NeverRestart
def Event12400860():
    """ 12400860: Event 12400860 """
    GotoIfFlagOff(Label.L0, 12400861)
    DisableCharacter(2400450)
    End()
    Label(0)
    IfCharacterDead(0, 2400450)
    SkipLinesIfFlagOn(2, 6333)
    AwardItemLot(75002400, host_only=False)
    SkipLines(1)
    AwardItemLot(75002405, host_only=False)
    EnableFlag(12400861)


@RestartOnRest
def Event12405600(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: float):
    """ 12405600: Event 12405600 """
    DisableAI(ARG_0_3)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(2, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(2, input_condition=-2)
    IfAttacked(3, ARG_0_3, attacking_character=10000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    SkipLinesIfFinishedConditionTrue(1, 3)
    Wait(ARG_12_15)
    EnableAI(ARG_0_3)
    WaitFrames(1)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405660():
    """ 12405660: Event 12405660 """
    DisableAI(2400114)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-3, PLAYER, region=2402082)
    IfEntityWithinDistance(-3, 2400114, 10000, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfCharacterInsideRegion(-1, 2400122, region=2404151)
    IfAttacked(-1, 2400114, attacking_character=10000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2400114)
    ReplanAI(2400114)


@RestartOnRest
def Event12405670(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: float, ARG_16_19: float):
    """ 12405670: Event 12405670 """
    DisableAI(ARG_0_3)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(2, PLAYER, region=ARG_8_11)
    IfConditionTrue(2, input_condition=-2)
    IfEntityWithinDistance(3, 10000, ARG_0_3, radius=ARG_12_15)
    IfConditionTrue(3, input_condition=-2)
    IfAttacked(4, ARG_0_3, attacking_character=10000)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    Wait(ARG_16_19)
    EnableAI(ARG_0_3)
    WaitFrames(1)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405675(ARG_0_3: int):
    """ 12405675: Event 12405675 """
    DisableAI(ARG_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=2404332)
    IfConditionTrue(-1, input_condition=1)
    IfAttacked(-1, ARG_0_3, attacking_character=10000)
    IfEntityWithinDistance(-1, ARG_0_3, 10000, radius=3.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(ARG_0_3)
    WaitFrames(1)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405680():
    """ 12405680: Event 12405680 """
    IfCharacterTargeting(0, 2400106, PLAYER)
    WaitFrames(1)
    ForceAnimation(2400106, 3010, wait_for_completion=True)
    WaitFrames(75)
    IfHealthEqual(0, 2400106, 1.0)
    EnableFlag(12405681)
    ForceAnimation(2400106, 3009, wait_for_completion=True)


@RestartOnRest
def Event12405682(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int, ARG_16_19: float):
    """ 12405682: Event 12405682 """
    DisableAI(ARG_0_3)
    DisableAnimations(ARG_4_7)
    IfAttacked(1, ARG_0_3, attacking_character=10000)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-3)
    IfEntityWithinDistance(2, ARG_0_3, 10000, radius=10.0)
    IfFlagOn(3, 12405681)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(ARG_0_3)
    SkipLinesIfFlagOff(24, 12405681)
    Wait(ARG_8_11)
    SetEventPoint(ARG_0_3, region=ARG_4_7, reaction_range=1.0)
    AICommand(ARG_0_3, command_id=90, slot=0)
    ReplanAI(ARG_0_3)
    IfEntityWithinDistance(4, ARG_0_3, ARG_4_7, radius=4.0)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterType(-4, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(5, input_condition=-4)
    IfEntityWithinDistance(5, ARG_0_3, 10000, radius=3.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(9, 2)
    AddSpecialEffect(ARG_0_3, 4662, affect_npc_part_hp=False)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagOn(9, ARG_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagOn(7, ARG_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagOn(5, ARG_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagOn(3, ARG_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagOn(1, ARG_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    Wait(ARG_16_19)
    CancelSpecialEffect(ARG_0_3, 4662)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405686(ARG_0_3: int):
    """ 12405686: Event 12405686 """
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)


@RestartOnRest
def Event12405690():
    """ 12405690: Event 12405690 """
    IfCharacterInsideRegion(0, 2400106, region=2404111)
    AddSpecialEffect(2400106, 5002, affect_npc_part_hp=False)
    IfCharacterInsideRegion(0, 2400106, region=2404113)
    WaitFrames(30)
    CancelSpecialEffect(2400106, 5002)
    Restart()


@NeverRestart
def Event12400500():
    """ 12400500: Event 12400500 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L6, input_condition=15)
    GotoIfFlagOff(Label.L1, 1193)
    DisableFlagRange((1180, 1199))
    EnableFlag(1181)
    Label(1)
    IfFlagOn(1, 1181)
    IfFlagOn(1, 9801)
    GotoIfConditionFalse(Label.L2, input_condition=1)
    DisableFlagRange((1180, 1199))
    EnableFlag(1185)
    Label(2)
    IfFlagOn(2, 9467)
    IfFlagOn(2, 1185)
    GotoIfConditionFalse(Label.L3, input_condition=2)
    DisableFlagRange((1180, 1199))
    EnableFlag(1186)
    Label(3)
    IfFlagOn(5, 1186)
    IfFlagOn(5, 72400900)
    GotoIfConditionFalse(Label.L9, input_condition=5)
    DisableFlagRange((1180, 1199))
    EnableFlag(1187)
    Label(9)
    IfFlagOn(3, 1187)
    IfFlagOn(3, 72400919)
    GotoIfConditionFalse(Label.L4, input_condition=3)
    SkipLinesIfFlagOn(2, 72400918)
    EnableFlag(72400918)
    Goto(Label.L4)
    DisableFlagRange((1180, 1199))
    EnableFlag(1188)
    Label(4)
    IfFlagOn(4, 1188)
    IfFlagOn(4, 72400350)
    GotoIfConditionFalse(Label.L5, input_condition=4)
    DisableFlagRange((1180, 1199))
    EnableFlag(1189)
    Label(5)
    DisableFlag(72400348)
    DisableFlag(72400356)
    Label(6)
    DisableGravity(2400730)
    DisableCollision(2400730)
    DisableGravity(2400732)
    DisableCollision(2400732)
    GotoIfFlagOn(Label.L0, 1181)
    GotoIfFlagOn(Label.L0, 1184)
    GotoIfFlagOn(Label.L5, 1185)
    GotoIfFlagOn(Label.L0, 1186)
    GotoIfFlagOn(Label.L0, 1188)
    GotoIfFlagOn(Label.L1, 1191)
    GotoIfFlagOn(Label.L2, 1189)
    GotoIfFlagOn(Label.L3, 1183)
    GotoIfFlagOn(Label.L4, 1189)
    GotoIfFlagOn(Label.L4, 1187)
    DisableBackread(2400730)
    DisableBackread(2400732)
    DisableObject(2400731)
    End()
    Label(0)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    ForceAnimation(2400730, 103060, loop=True, skip_transition=True)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    Label(5)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    ForceAnimation(2400730, 103066, loop=True, skip_transition=True)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    Label(1)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    EzstateAIRequest(2400730, command_id=3, slot=1)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400730)
    End()
    Label(2)
    DisableBackread(2400730)
    EnableBackread(2400732)
    EnableObject(2400731)
    PostDestruction(2400731, slot=1)
    EzstateAIRequest(2400732, command_id=10, slot=1)
    Move(2400732, destination=2404382, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400732)
    End()
    Label(3)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    EzstateAIRequest(2400730, command_id=3, slot=1)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400730)
    End()
    Label(4)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    PostDestruction(2400731, slot=1)
    End()


@NeverRestart
def Event12400501():
    """ 12400501: Event 12400501 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1183)
    EndIfFlagOn(1189)
    EndIfFlagOn(1191)
    IfCharacterDead(1, 2400730)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1180, 1199))
    EnableFlag(1183)
    SaveRequest()


@NeverRestart
def Event12400505():
    """ 12400505: Event 12400505 """
    GotoIfThisEventOn(Label.L0)
    GotoIfFlagOn(Label.L0, 1191)
    DisableMapPart(2404602)
    IfFlagOn(0, 6001)
    End()
    Label(0)
    EnableMapPart(2404602)
    End()


@NeverRestart
def Event12400507():
    """ 12400507: Event 12400507 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfDamageType(1, attacked_entity=2400730, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfHealthNotEqual(1, 2400730, 0.0)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagOn(Label.L0, 1185)
    ForceAnimation(2400730, 103063)
    Restart()
    Label(0)
    ForceAnimation(2400730, 103067)
    Restart()


@NeverRestart
def Event12400508():
    """ 12400508: Event 12400508 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, 2400730, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400730, 103064)


@NeverRestart
def Event12400512():
    """ 12400512: Event 12400512 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(-1, 2400730, 151)
    IfCharacterHasSpecialEffect(-1, 2400730, 153)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, 2400730, 0.0)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagOn(Label.L0, 1185)
    GotoIfFlagOn(Label.L1, 9432)
    ForceAnimation(2400730, 103060)
    Goto(Label.L9)
    Label(1)
    ForceAnimation(2400730, 103061)
    Goto(Label.L9)
    Label(0)
    ForceAnimation(2400730, 103066)
    Goto(Label.L9)
    Label(9)
    WaitFrames(5)
    Restart()


@NeverRestart
def Event12400513():
    """ 12400513: Event 12400513 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 9432)
    IfFlagOn(-1, 1181)
    IfFlagOn(-1, 1184)
    IfFlagOn(-1, 1186)
    IfFlagOn(-1, 1187)
    IfFlagOn(-1, 1188)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400730, 103061)
    IfFlagOff(0, 9432)
    ForceAnimation(2400730, 103060)
    Restart()


@NeverRestart
def Event12400514():
    """ 12400514: Event 12400514 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L0, 1187)
    GotoIfFlagOn(Label.L1, 1189)
    End()
    Label(0)
    IfActionButtonInRegion(0, action_button_id=2400020, region=2400731)
    DisplayDialog(14001000, anchor_entity=2400731, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    EnableFlag(72400919)
    Restart()
    Label(1)
    IfActionButtonInRegion(0, action_button_id=2400020, region=2400731)
    DisplayDialog(14001001, anchor_entity=2400731, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12400520():
    """ 12400520: Event 12400520 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L7, input_condition=15)
    IfFlagOn(1, 1232)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableFlagRange((1220, 1239))
    EnableFlag(1224)
    Label(0)
    IfFlagOn(2, 1233)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    DisableFlagRange((1220, 1239))
    EnableFlag(1223)
    Label(1)
    IfFlagOn(3, 9802)
    IfFlagOn(3, 1224)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1220, 1239))
    EnableFlag(1225)
    Label(2)
    IfFlagOn(4, 1225)
    IfFlagOn(4, 9464)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableFlagRange((1220, 1239))
    EnableFlag(1226)
    Label(3)
    IfFlagOn(5, 1226)
    IfFlagOn(5, 9461)
    GotoIfConditionFalse(Label.L5, input_condition=5)
    DisableFlagRange((1220, 1239))
    EnableFlag(1228)
    Label(5)
    IfFlagOn(7, 1220)
    IfFlagOn(7, 9802)
    GotoIfConditionFalse(Label.L6, input_condition=7)
    DisableFlagRange((1220, 1239))
    EnableFlag(1234)
    Label(6)
    Label(7)
    DisableGravity(2400750)
    DisableCollision(2400750)
    DisableGravity(2400754)
    DisableCollision(2400754)
    DisableGravity(2400757)
    DisableCollision(2400757)
    GotoIfFlagOn(Label.L0, 1220)
    GotoIfFlagOn(Label.L1, 1224)
    GotoIfFlagOn(Label.L2, 1225)
    GotoIfFlagOn(Label.L3, 1226)
    GotoIfFlagOn(Label.L4, 1228)
    GotoIfFlagOn(Label.L4, 1229)
    GotoIfFlagOn(Label.L4, 1235)
    GotoIfFlagOn(Label.L5, 1222)
    GotoIfFlagOn(Label.L5, 1230)
    GotoIfFlagOn(Label.L6, 1231)
    DisableObject(2400748)
    DisableMapPart(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()
    Label(0)
    DisableObject(2400748)
    DisableMapPart(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()
    Label(1)
    EnableObject(2400748)
    DisableMapPart(2404601)
    EnableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400750, 103080)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    Label(2)
    EnableObject(2400748)
    DisableMapPart(2404601)
    DisableBackread(2400750)
    EnableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400754, 103081)
    Move(2400754, destination=2404504, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    Label(3)
    EnableObject(2400748)
    DisableMapPart(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    EnableBackread(2400757)
    ForceAnimation(2400757, 103081)
    Move(2400757, destination=2404504, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    Label(4)
    EnableObject(2400748)
    EnableMapPart(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()
    Label(5)
    EnableObject(2400748)
    DisableMapPart(2404601)
    EnableBackread(2400750)
    EnableCharacter(2400750)
    DisableBackread(2400754)
    DisableCharacter(2400754)
    DisableBackread(2400757)
    DisableCharacter(2400757)
    EzstateAIRequest(2400750, command_id=5, slot=1)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400750)
    End()
    Label(6)
    EnableObject(2400748)
    DisableMapPart(2404601)
    DisableBackread(2400750)
    DisableCharacter(2400750)
    DisableBackread(2400754)
    DisableCharacter(2400754)
    DisableBackread(2400757)
    DisableCharacter(2400757)
    DropMandatoryTreasure(2400750)
    End()


@NeverRestart
def Event12400521():
    """ 12400521: Event 12400521 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1222)
    EndIfFlagOn(1230)
    EndIfFlagOn(1231)
    IfCharacterDead(-1, 2400750)
    IfCharacterDead(-1, 2400754)
    IfCharacterDead(-1, 2400757)
    IfCharacterDead(-1, 2400758)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1220, 1239))
    EnableFlag(1222)
    SaveRequest()


@NeverRestart
def Event12400522():
    """ 12400522: Event 12400522 """
    GotoIfThisEventOn(Label.L0)
    GotoIfFlagOn(Label.L0, 1230)
    GotoIfFlagOn(Label.L0, 1231)
    DisableMapPart(2404600)
    IfFlagOn(0, 6001)
    End()
    Label(0)
    EnableMapPart(2404600)
    End()


@NeverRestart
def Event12400523():
    """ 12400523: Event 12400523 """
    IfFlagOn(0, 72400510)
    DisableFlag(72400510)
    DisableFlagRange((1220, 1239))
    EnableFlag(1232)


@NeverRestart
def Event12400524():
    """ 12400524: Event 12400524 """
    IfFlagOn(0, 72400511)
    DisableFlag(72400511)
    DisableFlagRange((1220, 1239))
    EnableFlag(1233)


@NeverRestart
def Event12400525():
    """ 12400525: Event 12400525 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 72400499)
    DisableFlag(72400499)
    GotoIfFlagOff(Label.L0, 72400950)
    GotoIfFlagOff(Label.L1, 72400951)
    GotoIfFlagOff(Label.L2, 72400952)
    GotoIfFlagOff(Label.L3, 72400953)
    GotoIfFlagOff(Label.L4, 72400954)
    Label(4)
    EnableFlag(72400954)
    Label(3)
    EnableFlag(72400953)
    Label(2)
    EnableFlag(72400952)
    Label(1)
    EnableFlag(72400951)
    Label(0)
    EnableFlag(72400950)
    IfFlagOn(-1, 1304)
    IfFlagOn(-1, 1305)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFlagOff(Label.L5, 72400940)
    GotoIfFlagOff(Label.L6, 72400941)
    GotoIfFlagOff(Label.L7, 72400942)
    GotoIfFlagOff(Label.L8, 72400943)
    GotoIfFlagOff(Label.L9, 72400944)
    Label(9)
    EnableFlag(72400944)
    Label(8)
    EnableFlag(72400943)
    Label(7)
    EnableFlag(72400942)
    Label(6)
    EnableFlag(72400941)
    Label(5)
    EnableFlag(72400940)


@NeverRestart
def Event12400531():
    """ 12400531: Event 12400531 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerHasGood(1, 701, including_box=False)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableFlag(72400498)
    End()
    Label(0)
    End()


@NeverRestart
def Event12400560():
    """ 12400560: Event 12400560 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L3, input_condition=15)
    IfFlagOn(1, 1168)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableFlagRange((1160, 1179))
    EnableFlag(1164)
    Label(0)
    IfFlagOn(2, 1169)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    DisableFlagRange((1160, 1179))
    EnableFlag(1163)
    Label(1)
    IfFlagOn(3, 9802)
    IfFlagOn(3, 1164)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1160, 1179))
    EnableFlag(1165)
    Label(2)
    IfFlagOn(4, 1160)
    IfFlagOn(4, 9802)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableFlagRange((1160, 1179))
    EnableFlag(1170)
    Label(3)
    DisableGravity(2400765)
    DisableCollision(2400765)
    GotoIfFlagOn(Label.L4, 1161)
    GotoIfFlagOn(Label.L1, 1164)
    GotoIfFlagOn(Label.L1, 1165)
    GotoIfFlagOn(Label.L3, 1166)
    GotoIfFlagOn(Label.L2, 1167)
    DisableBackread(2400765)
    End()
    Label(1)
    EnableBackread(2400765)
    ForceAnimation(2400765, 103050)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    Label(3)
    DisableBackread(2400765)
    EzstateAIRequest(2400765, command_id=2, slot=1)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400765)
    End()
    Label(4)
    EnableBackread(2400765)
    EzstateAIRequest(2400765, command_id=2, slot=1)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400765)
    End()


@NeverRestart
def Event12400561():
    """ 12400561: Event 12400561 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1161)
    EndIfFlagOn(1166)
    IfCharacterDead(1, 2400765)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1160, 1179))
    EnableFlag(1161)
    SaveRequest()


@NeverRestart
def Event12400563():
    """ 12400563: Event 12400563 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L0, 72400330)
    IfFlagOn(-1, 1304)
    IfFlagOn(-1, 1305)
    IfFlagOn(-1, 1306)
    IfFlagOn(-1, 1307)
    IfFlagOn(-1, 1308)
    IfFlagOn(-2, 1224)
    IfFlagOn(-2, 1225)
    IfFlagOn(-2, 1226)
    IfFlagOn(-2, 1227)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(72400330)
    Label(0)
    IfFlagOn(-3, 1312)
    IfFlagOn(-3, 1303)
    IfFlagOn(-3, 1317)
    IfFlagOn(-4, 1228)
    IfFlagOn(-4, 1229)
    IfFlagOn(-4, 1235)
    IfFlagOn(-4, 1236)
    IfFlagOn(-4, 1230)
    IfFlagOn(-4, 1231)
    IfFlagOn(-4, 1222)
    IfConditionTrue(-5, input_condition=-3)
    IfConditionTrue(-5, input_condition=-4)
    IfConditionTrue(0, input_condition=-5)
    DisableFlag(72400330)


@NeverRestart
def Event12400564():
    """ 12400564: Event 12400564 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L0, 72400331)
    IfFlagOn(1, 1188)
    IfFlagOn(1, 1164)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(72400331)
    Label(0)
    IfFlagOn(-1, 1189)
    IfFlagOn(-1, 1191)
    IfFlagOn(-1, 1183)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(72400331)


@NeverRestart
def Event12400565():
    """ 12400565: Event 12400565 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L0, 72400332)
    IfFlagOn(-1, 1100)
    IfFlagOn(-1, 1101)
    IfFlagOn(-1, 1102)
    IfFlagOn(-1, 1103)
    IfFlagOn(-1, 1104)
    IfFlagOn(-1, 1105)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400332)
    Label(0)
    IfFlagOn(-2, 1108)
    IfFlagOn(-2, 1106)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(72400332)


@NeverRestart
def Event12400566():
    """ 12400566: Event 12400566 """
    IfFlagOn(0, 72400970)
    DisableFlag(72400970)
    DisableFlagRange((1160, 1179))
    EnableFlag(1168)
    Restart()


@NeverRestart
def Event12400567():
    """ 12400567: Event 12400567 """
    IfFlagOn(0, 72400971)
    DisableFlag(72400971)
    DisableFlagRange((1160, 1179))
    EnableFlag(1169)
    Restart()


@NeverRestart
def Event12400568():
    """ 12400568: Event 12400568 """
    GotoIfThisEventOn(Label.L0)
    GotoIfFlagOn(Label.L0, 1166)
    DisableMapPart(2404603)
    IfFlagOn(0, 6001)
    End()
    Label(0)
    EnableMapPart(2404603)
    End()


@NeverRestart
def Event12400569():
    """ 12400569: Event 12400569 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1161)
    EndIfFlagOn(1166)
    IfHealthEqual(1, 2400765, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400765, 103053)


@NeverRestart
def Event12400570():
    """ 12400570: Event 12400570 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfDamageType(1, attacked_entity=2400765, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfHealthNotEqual(1, 2400765, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400765, 103052)
    Restart()


@NeverRestart
def Event12400571():
    """ 12400571: Event 12400571 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2400765, 151)
    IfHealthNotEqual(1, 2400765, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfFlagOn(2, 9432)
    IfFlagOff(2, 1165)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    ForceAnimation(2400765, 103050)
    Goto(Label.L9)
    Label(0)
    ForceAnimation(2400765, 103051)
    Goto(Label.L9)
    Label(9)
    WaitFrames(5)
    Restart()


@NeverRestart
def Event12400572():
    """ 12400572: Event 12400572 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 9432)
    IfFlagOff(1, 1165)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400765, 103051)
    IfFlagOff(0, 9432)
    ForceAnimation(2400765, 103050)
    Restart()


@NeverRestart
def Event12400580():
    """ 12400580: Event 12400580 """
    EndIfThisEventOn()
    IfCharacterInsideRegion(1, PLAYER, region=2402280)
    IfFlagOn(2, 72400400)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EnableMapSound(2403300)


@NeverRestart
def Event12400581():
    """ 12400581: Event 12400581 """
    IfFlagOn(0, 72400400)
    DisableMapSound(2403300)


@NeverRestart
def Event12400582():
    """ 12400582: Event 12400582 """
    EnableMapPart(2404010)
    IfFlagOn(0, 12401802)
    DisableMapPart(2404010)


@NeverRestart
def Event12400590():
    """ 12400590: Event 12400590 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    IfFlagOn(1, 1340)
    IfFlagOn(1, 9801)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1340, 1359))
    EnableFlag(1344)
    Label(1)
    IfFlagOn(2, 1351)
    IfFlagOn(2, 72500359)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    DisableFlagRange((1340, 1359))
    EnableFlag(1343)
    Label(2)
    DisableFlag(72400471)
    Label(0)
    DisableGravity(2400762)
    DisableCollision(2400762)
    GotoIfFlagOn(Label.L0, 1340)
    GotoIfFlagOn(Label.L1, 1341)
    GotoIfFlagOn(Label.L2, 1342)
    GotoIfFlagOn(Label.L3, 1343)
    GotoIfFlagOn(Label.L4, 1344)
    GotoIfFlagOn(Label.L5, 1345)
    GotoIfFlagOn(Label.L6, 1346)
    GotoIfFlagOn(Label.L4, 1347)
    DisableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    End()
    Label(0)
    EnableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    GotoIfFlagOn(Label.L7, 12405160)
    ForceAnimation(2400760, 103020, loop=True, skip_transition=True)
    End()
    Label(7)
    End()
    Label(1)
    EnableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    SetTeamType(2400760, TeamType.HostileNPC)
    End()
    Label(2)
    DisableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    DisableCharacter(2400760)
    DropMandatoryTreasure(2400760)
    End()
    Label(3)
    DisableBackread(2400760)
    EnableBackread(2400762)
    DisableBackread(2400763)
    EnableObject(2400761)
    Move(2400762, destination=2404508, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    EzstateAIRequest(2400762, command_id=11, slot=1)
    DropMandatoryTreasure(2400762)
    End()
    Label(4)
    DisableBackread(2400760)
    DisableBackread(2400762)
    EnableBackread(2400763)
    DisableObject(2400761)
    SetTeamType(2400763, TeamType.FriendlyNPC)
    End()
    Label(5)
    DisableBackread(2400760)
    DisableBackread(2400762)
    EnableBackread(2400763)
    DisableObject(2400761)
    SetTeamType(2400763, TeamType.HostileNPC)
    End()
    Label(6)
    DisableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    DisableCharacter(2400763)
    DropMandatoryTreasure(2400763)
    End()


@NeverRestart
def Event12400591():
    """ 12400591: Event 12400591 """
    IfFlagOn(0, 72400465)
    DisableFlag(72400465)
    DisableFlagRange((1340, 1359))
    EnableFlag(1347)
    SaveRequest()


@NeverRestart
def Event12400592(ARG_0_3: int, ARG_4_7: int):
    """ 12400592: Event 12400592 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(ARG_4_7)
    IfDamageType(0, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    WaitFrames(1)
    IfDamageType(0, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    WaitFrames(1)
    IfDamageType(0, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    WaitFrames(1)
    EnableFlag(ARG_4_7)


@NeverRestart
def Event12400593(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12400593: Event 12400593 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(-1, ARG_8_11)
    IfHealthLessThanOrEqual(-1, ARG_0_3, 0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(ARG_0_3, TeamType.HostileNPC)
    DisableFlagRange((1340, 1359))
    EnableFlag(ARG_4_7)
    SaveRequest()


@NeverRestart
def Event12400594(ARG_0_3: int, ARG_4_7: int):
    """ 12400594: Event 12400594 """
    EndIfThisEventSlotOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(0, ARG_0_3)
    DisableFlagRange((1340, 1359))
    EnableFlag(ARG_4_7)
    SaveRequest()


@NeverRestart
def Event12400610():
    """ 12400610: Event 12400610 """
    DisableFlag(72400362)
    DisableFlag(72400921)
    DisableFlag(72400924)
    DisableGravity(2400756)
    ForceAnimation(2400756, 7002, loop=True)
    DisableAI(2400756)
    DisableBackread(2400756)
    GotoIfFlagOn(Label.L0, 1205)
    GotoIfFlagOn(Label.L1, 1206)
    GotoIfFlagOn(Label.L1, 1207)
    GotoIfFlagOn(Label.L3, 1210)
    DisableBackread(2400755)
    DisableBackread(2400759)
    EnableBackread(2400220)
    End()
    Label(0)
    IfEventValueComparison(-1, 72400372, bit_count=2, comparison_type=ComparisonType.NotEqual, value=0)
    IfFlagOn(-1, 12405158)
    GotoIfConditionTrue(Label.L2, input_condition=-1)
    DisableBackread(2400755)
    EnableBackread(2400759)
    DisableBackread(2400220)
    GotoIfFlagOn(Label.L5, 12405157)
    ForceAnimation(2400759, 103074)
    End()
    Label(5)
    ForceAnimation(2400759, 103072)
    End()
    Label(2)
    EnableBackread(2400755)
    DisableBackread(2400759)
    DisableBackread(2400220)
    GotoIfFlagOn(Label.L4, 12405157)
    ForceAnimation(2400755, 103074)
    End()
    Label(4)
    ForceAnimation(2400755, 103072)
    End()
    Label(1)
    EnableBackread(2400755)
    DisableBackread(2400759)
    DisableBackread(2400220)
    ForceAnimation(2400755, 103072)
    End()
    Label(3)
    DisableBackread(2400755)
    DisableCharacter(2400755)
    DisableBackread(2400759)
    DisableCharacter(2400759)
    DisableBackread(2400220)
    DisableCharacter(2400220)
    DropMandatoryTreasure(2400755)
    End()


@NeverRestart
def Event12400611():
    """ 12400611: Event 12400611 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1210)
    IfCharacterDead(-1, 2400755)
    IfCharacterDead(-1, 2400756)
    IfCharacterDead(-1, 2400759)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((1200, 1219))
    EnableFlag(1210)
    IfCharacterDead(1, 2400756)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableFlag(9432)
    Label(0)
    SaveRequest()


@NeverRestart
def Event12400612(ARG_0_3: int, ARG_4_7: int):
    """ 12400612: Event 12400612 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthLessThan(1, ARG_0_3, 0.5)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(ARG_4_7)


@NeverRestart
def Event12400614(ARG_0_3: int, ARG_4_7: int):
    """ 12400614: Event 12400614 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, ARG_0_3, 0.0)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 155)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, ARG_4_7)


@NeverRestart
def Event12400616(ARG_0_3: int):
    """ 12400616: Event 12400616 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfHealthGreaterThan(1, ARG_0_3, 0.5)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(-2, ARG_0_3, 153)
    GotoIfConditionTrue(Label.L0, input_condition=-2)
    IfCharacterHasSpecialEffect(-3, ARG_0_3, 155)
    GotoIfConditionTrue(Label.L1, input_condition=-3)
    Restart()
    Label(0)
    ForceAnimation(ARG_0_3, 103079)
    Restart()
    Label(1)
    ForceAnimation(ARG_0_3, 103130)
    Restart()


@NeverRestart
def Event12400618(ARG_0_3: int):
    """ 12400618: Event 12400618 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 154)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, 103072)
    Restart()


@NeverRestart
def Event12400620(ARG_0_3: int):
    """ 12400620: Event 12400620 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 156)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, 103072)


@NeverRestart
def Event12400622():
    """ 12400622: Event 12400622 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 1208)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()
    Label(0)
    DisableFlagRange((1200, 1219))
    EnableFlag(1205)


@NeverRestart
def Event12400623():
    """ 12400623: Event 12400623 """
    EndIfClient()
    IfFlagOn(1, 1209)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()
    Label(0)
    DisableFlagRange((1200, 1219))
    EnableFlag(1204)


@NeverRestart
def Event12400624():
    """ 12400624: Event 12400624 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOff(1205)
    IfFlagOn(-1, 1106)
    IfFlagOn(-1, 1108)
    IfFlagOn(-2, 1222)
    IfFlagOn(-2, 1223)
    IfFlagOn(-2, 1230)
    IfFlagOn(-2, 1231)
    IfFlagOn(-2, 1235)
    IfFlagOn(-2, 1228)
    IfFlagOn(-2, 1229)
    IfFlagOn(-2, 1234)
    IfFlagOn(-3, 1303)
    IfFlagOn(-3, 1308)
    IfFlagOn(-3, 1309)
    IfFlagOn(-3, 1315)
    IfFlagOn(-3, 1310)
    IfFlagOn(-3, 1312)
    IfFlagOn(-3, 1316)
    IfFlagOn(-4, 1163)
    IfFlagOn(-4, 1161)
    IfFlagOn(-4, 1166)
    IfFlagOn(-4, 1170)
    IfFlagOn(-5, 1183)
    IfFlagOn(-5, 1190)
    IfFlagOn(-5, 1189)
    IfFlagOn(-5, 1191)
    IfFlagOn(-5, 1195)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(1, input_condition=-4)
    IfConditionTrue(1, input_condition=-5)
    IfFlagOff(1, 72400934)
    IfFlagOff(1, 72400935)
    IfFlagOff(1, 72400936)
    IfFlagOff(1, 72400937)
    IfFlagOff(1, 72400938)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1200, 1219))
    EnableFlag(1211)


@NeverRestart
def Event12400625(ARG_0_3: int, ARG_4_7: int):
    """ 12400625: Event 12400625 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOff(1207)
    WaitFrames(30)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfCharacterInsideRegion(-1, PLAYER, region=2404383)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 1207)
    IfCharacterBackreadEnabled(1, ARG_0_3)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(ARG_4_7)


@NeverRestart
def Event12400627(ARG_0_3: int, ARG_4_7: int):
    """ 12400627: Event 12400627 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(1)
    IfDamageType(3, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthNotEqual(3, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=3)
    EnableFlag(ARG_4_7)


@NeverRestart
def Event12400629():
    """ 12400629: Event 12400629 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(-1, 1208)
    IfFlagOn(-1, 1205)
    IfFlagOn(-1, 1207)
    GotoIfConditionFalse(Label.L6, input_condition=-1)
    GotoIfFlagOn(Label.L0, 1208)
    GotoIfFlagOff(Label.L5, 72400360)
    GotoIfFlagRangeState(Label.L5, RangeState.AllOff, FlagType.Absolute, (70000200, 70000202))
    Label(0)
    IfFlagOn(-2, 1164)
    IfFlagOn(-2, 1165)
    GotoIfConditionFalse(Label.L1, input_condition=-2)
    DisableFlagRange((1160, 1179))
    EnableFlag(1166)
    EnableFlag(72400934)
    Goto(Label.L9)
    Label(1)
    IfFlagOn(-3, 1181)
    IfFlagOn(-3, 1184)
    IfFlagOn(-3, 1185)
    IfFlagOn(-3, 1186)
    IfFlagOn(-3, 1187)
    IfFlagOn(-3, 1188)
    GotoIfConditionFalse(Label.L2, input_condition=-3)
    DisableFlagRange((1180, 1199))
    EnableFlag(1191)
    EnableFlag(72400935)
    Goto(Label.L9)
    Label(2)
    IfFlagOn(-4, 1304)
    IfFlagOn(-4, 1305)
    IfFlagOn(-4, 1306)
    IfFlagOn(-4, 1307)
    GotoIfConditionFalse(Label.L3, input_condition=-4)
    DisableFlagRange((1300, 1319))
    EnableFlag(1312)
    EnableFlag(72400936)
    Goto(Label.L9)
    Label(3)
    IfFlagOn(-5, 1100)
    IfFlagOn(-5, 1101)
    IfFlagOn(-5, 1102)
    IfFlagOn(-5, 1103)
    IfFlagOn(-5, 1104)
    IfFlagOn(-5, 1105)
    GotoIfConditionFalse(Label.L4, input_condition=-5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1108)
    EnableFlag(72400937)
    Goto(Label.L9)
    Label(4)
    IfFlagOn(-6, 1224)
    IfFlagOn(-6, 1225)
    IfFlagOn(-6, 1226)
    IfFlagOn(-6, 1228)
    IfFlagOn(-6, 1229)
    GotoIfConditionFalse(Label.L5, input_condition=-6)
    DisableFlagRange((1220, 1239))
    EnableFlag(1231)
    EnableFlag(72400938)
    Goto(Label.L9)
    Label(9)
    IncrementEventValue(72400375, bit_count=3, max_value=7)
    IncrementEventValue(72400372, bit_count=2, max_value=2)
    EnableFlag(72400490)
    GotoIfFlagOn(Label.L5, 1208)
    EventValueOperation(70000200, 3, 1, 0, 1, CalculationType.Subtract)
    Label(5)
    End()


@NeverRestart
def Event12400630(ARG_0_3: int):
    """ 12400630: Event 12400630 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    IfHealthEqual(1, ARG_0_3, 0.0)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(0, ARG_0_3)
    EnableFlag(9432)
    EnableFlag(72400490)


@NeverRestart
def Event12400650():
    """ 12400650: Event 12400650 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    IfFlagOn(1, 1362)
    IfFlagOn(1, 72400520)
    SkipLinesIfConditionFalse(2, 1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1363)
    IfFlagOn(2, 72400524)
    SkipLinesIfConditionFalse(3, 2)
    DisableFlagRange((1360, 1379))
    EnableFlag(1368)
    EnableFlag(1376)
    Label(0)
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1373, 1375))
    GotoIfFlagOn(Label.L1, 1372)
    GotoIfFlagOn(Label.L2, 1371)
    GotoIfFlagOn(Label.L3, 1370)
    GotoIfFlagOn(Label.L4, 1369)
    GotoIfFlagOn(Label.L5, 1368)
    GotoIfFlagRangeState(Label.L6, RangeState.AnyOn, FlagType.Absolute, (1365, 1367))
    GotoIfFlagRangeState(Label.L7, RangeState.AnyOn, FlagType.Absolute, (1362, 1364))
    GotoIfFlagRangeState(Label.L8, RangeState.AnyOn, FlagType.Absolute, (1360, 1361))
    Label(0)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    Label(1)
    DisableBackread(2400900)
    EnableBackread(2400902)
    SetTeamType(2400902, TeamType.HostileNPC)
    DisableBackread(2400903)
    Goto(Label.L9)
    Label(2)
    DisableBackread(2400900)
    DisableBackread(2400902)
    EnableBackread(2400903)
    ForceAnimation(2400903, 103031, loop=True)
    Goto(Label.L9)
    Label(3)
    DisableBackread(2400900)
    DisableBackread(2400902)
    EnableBackread(2400903)
    ForceAnimation(2400903, 103031, loop=True)
    Goto(Label.L9)
    Label(4)
    SkipLinesIfFlagOff(5, 1705)
    DisableBackread(2400900)
    EnableBackread(2400902)
    SetTeamType(2400902, TeamType.HostileNPC)
    DisableBackread(2400903)
    Goto(Label.L9)
    SkipLinesIfFlagOff(5, 1704)
    DisableBackread(2400900)
    DisableBackread(2400902)
    EnableBackread(2400903)
    SetTeamType(2400903, TeamType.HostileNPC)
    Goto(Label.L9)
    SkipLinesIfFlagOff(5, 1701)
    EnableBackread(2400900)
    SetTeamType(2400900, TeamType.HostileNPC)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    SkipLinesIfFlagOff(5, 1703)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    SkipLinesIfFlagOff(4, 1702)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    Label(5)
    DisableBackread(2400900)
    DisableCharacter(2400900)
    DisableBackread(2400902)
    DisableCharacter(2400902)
    DisableBackread(2400903)
    DisableCharacter(2400903)
    SkipLinesIfFlagOff(2, 1705)
    DropMandatoryTreasure(2400902)
    Goto(Label.L9)
    SkipLinesIfFlagOff(2, 1704)
    DropMandatoryTreasure(2400903)
    Goto(Label.L9)
    SkipLinesIfFlagOff(2, 1701)
    DropMandatoryTreasure(2400900)
    Goto(Label.L9)
    SkipLinesIfFlagOff(1, 1703)
    Goto(Label.L9)
    SkipLinesIfFlagOff(1, 1702)
    Goto(Label.L9)
    Goto(Label.L9)
    Label(6)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    Label(7)
    EnableBackread(2400900)
    ForceAnimation(2400900, 103030, loop=True)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    Label(8)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    Label(9)
    RunEvent(12400651)
    RunEvent(12400652)
    RunEvent(12400653)
    RunEvent(12400654)
    RunEvent(12400655)
    RunEvent(12400657)
    RunEvent(12400658)
    RunEvent(12400659)
    RunEvent(12400660)
    RunEvent(12400661)
    RunEvent(12400662)
    RunEvent(12400663)
    RunEvent(12400665)


@NeverRestart
def Event12400651():
    """ 12400651: Event 12400651 """
    IfFlagOn(1, 1360)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2404390)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1362)
    EnableBackread(2400900)
    ForceAnimation(2400900, 103030, loop=True)
    DisableBackread(2400902)
    DisableBackread(2400903)


@NeverRestart
def Event12400652():
    """ 12400652: Event 12400652 """
    IfFlagOn(1, 1361)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2404390)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1363)
    EnableBackread(2400900)
    ForceAnimation(2400900, 103030, loop=True)
    DisableBackread(2400902)
    DisableBackread(2400903)


@NeverRestart
def Event12400653():
    """ 12400653: Event 12400653 """
    EndIfThisEventOn()
    DisableMapPart(2404610)
    IfFlagOn(0, 1370)
    EnableMapPart(2404610)


@NeverRestart
def Event12400654():
    """ 12400654: Event 12400654 """
    GotoIfThisEventOff(Label.L0)
    DisableBackread(2400901)
    DisableCharacter(2400901)
    DropMandatoryTreasure(2400901)
    End()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    Label(0)
    IfCharacterDead(0, 2400901)
    EndIfFlagOff(1370)
    DisableFlagRange((1360, 1379))
    EnableFlag(1371)


@NeverRestart
def Event12400655():
    """ 12400655: Event 12400655 """
    EndIfThisEventOn()
    DisableBackread(2400901)
    IfFlagOn(0, 1370)
    EnableBackread(2400901)


@NeverRestart
def Event12400656():
    """ 12400656: Event 12400656 """
    EndIfThisEventOn()
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 1374)
    IfFlagOn(1, 9802)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1372)
    DisableBackread(2400900)
    EnableBackread(2400902)
    SetTeamType(2400902, TeamType.HostileNPC)
    DisableBackread(2400903)


@NeverRestart
def Event12400657():
    """ 12400657: Event 12400657 """
    EndIfThisEventOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(1, 2400900)
    IfCharacterDead(2, 2400902)
    IfCharacterDead(3, 2400903)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagOn(7, 1369)
    DisableFlagRange((1700, 1705))
    SkipLinesIfFlagRangeAllOff(1, (1362, 1364))
    EnableFlag(1701)
    SkipLinesIfFlagRangeAllOff(1, (1370, 1371))
    EnableFlag(1704)
    SkipLinesIfFlagOff(1, 1372)
    EnableFlag(1705)
    DisableFlagRange((1360, 1379))
    EnableFlag(1368)
    SaveRequest()


@NeverRestart
def Event12400658():
    """ 12400658: Event 12400658 """
    EndIfThisEventOn()
    IfFlagOn(0, 72400526)
    DisableFlagRange((1700, 1705))
    SkipLinesIfFlagRangeAllOff(1, (1362, 1364))
    EnableFlag(1701)
    SkipLinesIfFlagRangeAllOff(1, (1370, 1371))
    EnableFlag(1704)
    SkipLinesIfFlagOff(1, 1372)
    EnableFlag(1705)
    DisableFlagRange((1360, 1379))
    EnableFlag(1369)
    SetTeamType(2400900, TeamType.HostileNPC)
    SaveRequest()


@NeverRestart
def Event12400659():
    """ 12400659: Event 12400659 """
    EndIfThisEventOn()
    IfAttacked(0, 2400900, attacking_character=10000)
    WaitFrames(1)
    IfAttacked(0, 2400900, attacking_character=10000)
    WaitFrames(1)
    IfAttacked(0, 2400900, attacking_character=10000)
    WaitFrames(1)


@NeverRestart
def Event12400660():
    """ 12400660: Event 12400660 """
    EndIfThisEventOn()
    IfFlagOn(0, 1373)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@NeverRestart
def Event12400661():
    """ 12400661: Event 12400661 """
    EndIfThisEventOn()
    IfFlagOn(0, 1374)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@NeverRestart
def Event12400662():
    """ 12400662: Event 12400662 """
    IfFlagOn(1, 1370)
    IfFlagOn(1, 72400530)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400903, 103034, loop=True)
    IfFlagOff(0, 72400530)
    ForceAnimation(2400903, 103031, loop=True)
    Restart()


@NeverRestart
def Event12400663():
    """ 12400663: Event 12400663 """
    EndIfThisEventOn()
    IfFlagOn(-1, 1370)
    IfFlagOn(-1, 1371)
    IfConditionTrue(1, input_condition=-1)
    IfDamageType(1, attacked_entity=2400903, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400903, 103032)
    Kill(2400903, award_souls=True)


@NeverRestart
def Event12400665():
    """ 12400665: Event 12400665 """
    EndIfThisEventOn()
    IfFlagOn(-1, 1365)
    IfFlagOn(-1, 1366)
    IfFlagOn(-1, 1367)
    IfConditionTrue(0, input_condition=-1)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@RestartOnRest
def Event12400700():
    """ 12400700: Event 12400700 """
    IfFlagOn(1, 1106)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    ForceAnimation(2400700, 2250)
    DropMandatoryTreasure(2400700)
    Label(0)
    IfFlagOn(2, 1108)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    DisableBackread(2400700)
    DropMandatoryTreasure(2400700)
    EnableMapPart(2404604)
    Label(1)
    IfFlagOn(3, 1109)
    EndIfConditionFalse(3)
    DisableFlag(1109)


@RestartOnRest
def Event12400701():
    """ 12400701: Event 12400701 """
    EndIfThisEventOn()
    IfFlagOn(0, 72400300)
    DisableFlagRange((1100, 1119))
    EnableFlag(1101)


@RestartOnRest
def Event12400702():
    """ 12400702: Event 12400702 """
    EndIfThisEventOn()
    EndIfFlagOn(1106)
    EndIfFlagOn(1108)
    IfFlagRangeAnyOn(1, (12400720, 12400724))
    IfFlagOn(2, 1106)
    IfFlagOn(3, 1108)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionFalse(1)
    DisableFlagRange((1100, 1119))
    EnableFlag(1102)


@RestartOnRest
def Event12400703():
    """ 12400703: Event 12400703 """
    EndIfThisEventOn()
    EndIfFlagOn(1106)
    EndIfFlagOn(1108)
    IfFlagOn(1, 72400985)
    IfFlagOn(2, 1106)
    IfFlagOn(3, 1108)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionFalse(1)
    DisableFlagRange((1100, 1119))
    EnableFlag(1103)


@RestartOnRest
def Event12400704():
    """ 12400704: Event 12400704 """
    EndIfThisEventOn()
    EndIfFlagOn(1106)
    EndIfFlagOn(1108)
    IfFlagOn(-1, 1164)
    IfFlagOn(-1, 1165)
    IfFlagOn(-1, 1167)
    IfFlagOn(-2, 1181)
    IfFlagOn(-2, 1185)
    IfFlagOn(-2, 1186)
    IfFlagOn(-2, 1188)
    IfFlagOn(-3, 1224)
    IfFlagOn(-3, 1225)
    IfFlagOn(-3, 1226)
    IfFlagOn(-4, 1304)
    IfFlagOn(-4, 1305)
    IfFlagOn(-4, 1307)
    IfFlagOn(-4, 1308)
    IfFlagOn(-5, 1106)
    IfFlagOn(-5, 1108)
    IfConditionTrue(2, input_condition=-1)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(2, input_condition=-4)
    IfConditionTrue(-6, input_condition=2)
    IfConditionTrue(-6, input_condition=-5)
    IfConditionTrue(0, input_condition=-6)
    EndIfFinishedConditionTrue(-5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1104)


@RestartOnRest
def Event12400705():
    """ 12400705: Event 12400705 """
    EndIfThisEventOn()
    EndIfFlagOn(1106)
    EndIfFlagOn(1108)
    IfFlagOff(1, 1164)
    IfFlagOff(1, 1165)
    IfFlagOff(1, 1167)
    IfFlagOff(2, 1181)
    IfFlagOff(2, 1185)
    IfFlagOff(2, 1186)
    IfFlagOff(2, 1188)
    IfFlagOff(3, 1224)
    IfFlagOff(3, 1225)
    IfFlagOff(3, 1226)
    IfFlagOff(4, 1304)
    IfFlagOff(4, 1305)
    IfFlagOff(4, 1307)
    IfFlagOff(4, 1308)
    IfFlagOn(-3, 1106)
    IfFlagOn(-3, 1108)
    IfConditionTrue(5, input_condition=-3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(6, input_condition=-1)
    IfFlagRangeAllOn(6, (12400708, 12400711))
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1105)


@RestartOnRest
def Event12400706():
    """ 12400706: Event 12400706 """
    EndIfFlagOn(1106)
    Label(0)
    IfCharacterDead(1, 2400700)
    IfFlagOff(1, 1108)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1100, 1119))
    EnableFlag(1106)
    SaveRequest()


@RestartOnRest
def Event12400707():
    """ 12400707: Event 12400707 """
    IfEventValueComparison(0, 12400733, bit_count=3, comparison_type=ComparisonType.GreaterThanOrEqual, value=3)
    EnableFlag(72400309)


@RestartOnRest
def Event12400708(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12400708: Event 12400708 """
    EndIfThisEventSlotOn()
    IfFlagOn(1, ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfFlagOn(-1, ARG_8_11)
    IfFlagOn(-1, ARG_12_15)
    SkipLinesIfNotEqual(1, left=ARG_16_19, right=1)
    IfFlagOn(-1, 1315)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionFalse(1)
    IncrementEventValue(12400733, bit_count=3, max_value=5)
    EnableFlag(72400313)
    DisableFlagRange((72400314, 72400319))
    EnableFlag(ARG_4_7)


@RestartOnRest
def Event12400713(ARG_0_3: int, ARG_4_7: int):
    """ 12400713: Event 12400713 """
    IfFlagOn(1, ARG_0_3)
    IfFlagOn(2, ARG_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    DisableFlag(72400308)
    EnableFlag(72400307)
    End()
    Label(0)
    DisableFlag(72400307)
    EnableFlag(72400308)


@RestartOnRest
def Event12400720():
    """ 12400720: Event 12400720 """
    EndIfThisEventOn()
    IfFlagOn(-1, 1161)
    IfFlagOn(-1, 1166)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400724)
    StopEvent(12400721, slot=0)
    StopEvent(12400722, slot=0)
    StopEvent(12400723, slot=0)
    StopEvent(12400728, slot=0)


@RestartOnRest
def Event12400721():
    """ 12400721: Event 12400721 """
    EndIfThisEventOn()
    IfFlagOn(-1, 1183)
    IfFlagOn(-1, 1189)
    IfFlagOn(-1, 1191)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400725)
    StopEvent(12400720, slot=0)
    StopEvent(12400722, slot=0)
    StopEvent(12400723, slot=0)
    StopEvent(12400729, slot=0)


@RestartOnRest
def Event12400722():
    """ 12400722: Event 12400722 """
    EndIfThisEventOn()
    IfFlagOn(-1, 1222)
    IfFlagOn(-1, 1230)
    IfFlagOn(-1, 1231)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400726)
    StopEvent(12400720, slot=0)
    StopEvent(12400721, slot=0)
    StopEvent(12400723, slot=0)
    StopEvent(12400730, slot=0)


@RestartOnRest
def Event12400723():
    """ 12400723: Event 12400723 """
    EndIfThisEventOn()
    IfFlagOn(-1, 1303)
    IfFlagOn(-1, 1312)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400727)
    StopEvent(12400720, slot=0)
    StopEvent(12400721, slot=0)
    StopEvent(12400722, slot=0)
    StopEvent(12400731, slot=0)


@RestartOnRest
def Event12400728():
    """ 12400728: Event 12400728 """
    EndIfThisEventOn()
    IfFlagRangeAnyOn(0, (12400720, 12400723))
    IfFlagOn(-1, 1161)
    IfFlagOn(-1, 1166)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(12400729, slot=0)
    StopEvent(12400730, slot=0)
    StopEvent(12400731, slot=0)


@RestartOnRest
def Event12400729():
    """ 12400729: Event 12400729 """
    EndIfThisEventOn()
    IfFlagRangeAnyOn(0, (12400720, 12400723))
    IfFlagOn(-1, 1183)
    IfFlagOn(-1, 1189)
    IfFlagOn(-1, 1191)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(12400728, slot=0)
    StopEvent(12400730, slot=0)
    StopEvent(12400731, slot=0)


@RestartOnRest
def Event12400730():
    """ 12400730: Event 12400730 """
    EndIfThisEventOn()
    IfFlagRangeAnyOn(0, (12400720, 12400723))
    IfFlagOn(-1, 1222)
    IfFlagOn(-1, 1230)
    IfFlagOn(-1, 1231)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(12400728, slot=0)
    StopEvent(12400729, slot=0)
    StopEvent(12400731, slot=0)


@RestartOnRest
def Event12400731():
    """ 12400731: Event 12400731 """
    EndIfThisEventOn()
    IfFlagRangeAnyOn(0, (12400720, 12400723))
    IfFlagOn(-1, 1303)
    IfFlagOn(-1, 1312)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(12400728, slot=0)
    StopEvent(12400729, slot=0)
    StopEvent(12400730, slot=0)


@RestartOnRest
def Event12400732():
    """ 12400732: Event 12400732 """
    IfDamageType(1, attacked_entity=2400700, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfFlagOn(1, 72400981)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(1109)


@RestartOnRest
def Event12400737():
    """ 12400737: Event 12400737 """
    EndIfFlagOn(1108)
    DisableMapPart(2404604)
    Label(0)
    IfFlagOn(0, 1108)
    EnableMapPart(2404604)
    DropMandatoryTreasure(2400700)


@RestartOnRest
def Event12400738():
    """ 12400738: Event 12400738 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 9432)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(2400700, 5401, affect_npc_part_hp=False)
    WaitFrames(1)
    ForceAnimation(2400700, 7000)
    IfFlagOff(0, 9432)
    AddSpecialEffect(2400700, 5402, affect_npc_part_hp=False)
    WaitFrames(1)
    ForceAnimation(2400700, 0)
    Restart()


@NeverRestart
def Event12400900():
    """ 12400900: Event 12400900 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L6, input_condition=15)
    IfFlagOn(1, 1313)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1300, 1319))
    EnableFlag(1304)
    Label(1)
    IfFlagOn(3, 72400942)
    IfFlagOn(3, 72400380)
    IfFlagOn(-1, 1304)
    IfFlagOn(-1, 1305)
    IfConditionTrue(3, input_condition=-1)
    IfFlagOn(-2, 1224)
    IfFlagOn(-2, 1225)
    IfFlagOn(-2, 1226)
    IfFlagOn(-2, 1227)
    IfConditionTrue(3, input_condition=-2)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1300, 1319))
    EnableFlag(1306)
    DisableFlagRange((1220, 1239))
    EnableFlag(1230)
    Goto(Label.L2)
    Label(2)
    GotoIfFlagOff(Label.L5, 9802)
    GotoIfFlagOn(Label.L3, 1304)
    GotoIfFlagOn(Label.L3, 1305)
    GotoIfFlagOn(Label.L4, 1306)
    Goto(Label.L5)
    Label(4)
    DisableFlagRange((1300, 1319))
    EnableFlag(1308)
    Goto(Label.L5)
    Label(3)
    DisableFlagRange((1300, 1319))
    EnableFlag(1307)
    Goto(Label.L5)
    Label(5)
    DisableFlag(72400393)
    Label(6)
    DisableGravity(2400770)
    DisableCollision(2400770)
    DisableGravity(2400772)
    DisableCollision(2400772)
    DisableGravity(2400774)
    DisableCollision(2400774)
    GotoIfFlagOn(Label.L0, 1304)
    GotoIfFlagOn(Label.L0, 1305)
    GotoIfFlagOn(Label.L4, 1306)
    GotoIfFlagOn(Label.L1, 1307)
    GotoIfFlagOn(Label.L2, 1308)
    GotoIfFlagOn(Label.L3, 1312)
    GotoIfFlagOn(Label.L5, 1317)
    GotoIfFlagOn(Label.L6, 1303)
    DisableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    End()
    Label(0)
    EnableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    ForceAnimation(2400770, 103096, loop=True, skip_transition=True)
    Move(2400770, destination=2404503, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    EndIfClient()
    EnableFlag(72400491)
    End()
    Label(4)
    DisableBackread(2400770)
    DisableBackread(2400772)
    EnableBackread(2400774)
    DisableBackread(2400775)
    PostDestruction(2400773, slot=1)
    ForceAnimation(2400774, 103096, loop=True, skip_transition=True)
    Move(2400774, destination=2404503, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    Label(1)
    DisableBackread(2400770)
    EnableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    ForceAnimation(2400772, 103096, loop=True, skip_transition=True)
    Move(2400772, destination=2404503, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    Label(2)
    DisableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    EnableBackread(2400775)
    PostDestruction(2400773, slot=1)
    DisableAI(2400775)
    Move(2400775, destination=2404381, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2404100)
    SetTeamType(2400775, TeamType.HostileNPC)
    End()
    Label(3)
    DisableBackread(2400770)
    DisableCharacter(2400770)
    DisableBackread(2400772)
    DisableCharacter(2400772)
    DisableBackread(2400774)
    DisableCharacter(2400774)
    DisableBackread(2400775)
    DisableCharacter(2400775)
    PostDestruction(2400773, slot=1)
    EzstateAIRequest(2400770, command_id=8, slot=1)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    WaitFrames(1)
    DropMandatoryTreasure(2400770)
    End()
    Label(5)
    DisableBackread(2400770)
    DisableCharacter(2400770)
    DisableBackread(2400772)
    DisableCharacter(2400772)
    DisableBackread(2400774)
    DisableCharacter(2400774)
    DisableBackread(2400775)
    DisableCharacter(2400775)
    PostDestruction(2400773, slot=1)
    DisableAI(2400775)
    Move(2400775, destination=2404381, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2404100)
    WaitFrames(1)
    DropMandatoryTreasure(2400775)
    End()
    Label(6)
    EnableBackread(2400770)
    EnableCharacter(2400770)
    DisableBackread(2400772)
    DisableCharacter(2400772)
    DisableBackread(2400774)
    DisableCharacter(2400774)
    DisableBackread(2400775)
    DisableCharacter(2400775)
    PostDestruction(2400773, slot=1)
    EzstateAIRequest(2400770, command_id=8, slot=1)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    WaitFrames(1)
    DropMandatoryTreasure(2400770)
    End()


@NeverRestart
def Event12400901():
    """ 12400901: Event 12400901 """
    IfFlagOn(0, 72400394)
    DisableFlag(72400394)
    IfFlagOn(1, 1304)
    IfFlagOn(1, 72400380)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()
    Label(0)
    DisableFlagRange((1300, 1319))
    EnableFlag(1305)


@NeverRestart
def Event12400940(ARG_0_3: int):
    """ 12400940: Event 12400940 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 72400955)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 157)
    IfFlagOff(1, 72400955)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, 103106)
    Restart()


@NeverRestart
def Event12400903():
    """ 12400903: Event 12400903 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1317)
    EndIfFlagOn(1312)
    EndIfFlagOn(1303)
    IfCharacterDead(-1, 2400770)
    IfCharacterDead(-1, 2400772)
    IfCharacterDead(-1, 2400774)
    IfCharacterDead(-1, 2400775)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagOn(Label.L0, 1308)
    DisableFlagRange((1300, 1319))
    EnableFlag(1303)
    SaveRequest()
    End()
    Label(0)
    DisableFlagRange((1300, 1319))
    EnableFlag(1317)
    SaveRequest()
    End()


@NeverRestart
def Event12400904():
    """ 12400904: Event 12400904 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 1308)
    IfCharacterInsideRegion(1, PLAYER, region=2404380)
    IfConditionTrue(-1, input_condition=1)
    IfDamageType(-1, attacked_entity=2400775, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400397)
    EnableAI(2400775)


@NeverRestart
def Event12400910(ARG_0_3: int):
    """ 12400910: Event 12400910 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 151)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    IfCharacterHasSpecialEffect(3, ARG_0_3, 158)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    ForceAnimation(ARG_0_3, 103134)
    Restart()
    Label(0)
    ForceAnimation(ARG_0_3, 103098)
    WaitFrames(20)
    Restart()


@NeverRestart
def Event12400915(ARG_0_3: int):
    """ 12400915: Event 12400915 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1317)
    EndIfFlagOn(1312)
    EndIfFlagOn(1303)
    IfHealthEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(-1, ARG_0_3, 151)
    IfCharacterHasSpecialEffect(-1, ARG_0_3, 158)
    IfConditionTrue(1, input_condition=-1)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(ARG_0_3, 103135)
    End()
    Label(0)
    ForceAnimation(ARG_0_3, 103099)
    End()


@NeverRestart
def Event12400920(ARG_0_3: int):
    """ 12400920: Event 12400920 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOff(0, 72400955)
    IfFlagOn(0, 72400955)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 151)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(ARG_0_3, 103104)
    Restart()
    Label(0)
    ForceAnimation(ARG_0_3, 103101)
    IfCharacterHasSpecialEffect(0, ARG_0_3, 152)
    ForceAnimation(ARG_0_3, 103104)
    Restart()


@NeverRestart
def Event12400925(ARG_0_3: int):
    """ 12400925: Event 12400925 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(-1, ARG_0_3, 153)
    IfCharacterHasSpecialEffect(-1, ARG_0_3, 159)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 153)
    GotoIfConditionTrue(Label.L2, input_condition=1)
    IfCharacterHasSpecialEffect(2, ARG_0_3, 159)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    Label(0)
    IfFlagOn(3, 9432)
    IfFlagOff(3, 1307)
    IfFlagOff(3, 1306)
    GotoIfConditionTrue(Label.L1, input_condition=3)
    ForceAnimation(ARG_0_3, 103102, loop=True)
    Goto(Label.L9)
    Label(1)
    ForceAnimation(ARG_0_3, 103103, loop=True)
    Goto(Label.L9)
    Label(2)
    IfFlagOn(4, 9432)
    IfFlagOff(4, 1307)
    IfFlagOff(4, 1306)
    GotoIfConditionTrue(Label.L3, input_condition=4)
    ForceAnimation(ARG_0_3, 103096, loop=True)
    Goto(Label.L9)
    Label(3)
    ForceAnimation(ARG_0_3, 103097, loop=True)
    Goto(Label.L9)
    Label(9)
    WaitFrames(5)
    Restart()


@NeverRestart
def Event12400930(ARG_0_3: int):
    """ 12400930: Event 12400930 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 156)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, 103102)
    Restart()


@NeverRestart
def Event12400935(ARG_0_3: int):
    """ 12400935: Event 12400935 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfEntityWithinDistance(1, 10000, ARG_0_3, radius=5.0)
    IfCharacterHasSpecialEffect(1, ARG_0_3, 151)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, 103101, wait_for_completion=True)


@NeverRestart
def Event12400952():
    """ 12400952: Event 12400952 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfThisEventOn(Label.L0)
    GotoIfFlagOn(Label.L0, 1306)
    GotoIfFlagOn(Label.L0, 1308)
    GotoIfFlagOn(Label.L0, 1312)
    IfFlagOn(0, 6001)
    End()
    Label(0)
    DestroyObject(2400773, slot=1)
    End()


@NeverRestart
def Event12400953():
    """ 12400953: Event 12400953 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthNotEqual(1, 2400770, 0.0)
    IfHealthNotEqual(1, 2400774, 0.0)
    IfFlagOn(1, 9432)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(-1, 2400770, 151)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    ForceAnimation(2400770, 103103)
    IfFlagOff(0, 9432)
    ForceAnimation(2400770, 103102)
    Restart()
    Label(0)
    ForceAnimation(2400770, 103097)
    IfFlagOff(0, 9432)
    ForceAnimation(2400770, 103096)
    Restart()


@NeverRestart
def Event12400954():
    """ 12400954: Event 12400954 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerHasGood(1, 702, including_box=False)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableFlag(72400392)
    End()
    Label(0)
    End()


@NeverRestart
def Event12400800():
    """ 12400800: Event 12400800 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfDamageType(1, attacked_entity=2400765, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthEqual(1, 2400765, 0.0)
    IfDamageType(2, attacked_entity=2400730, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthEqual(2, 2400730, 0.0)
    IfDamageType(3, attacked_entity=2400750, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthEqual(3, 2400750, 0.0)
    IfDamageType(4, attacked_entity=2400754, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthEqual(4, 2400754, 0.0)
    IfDamageType(5, attacked_entity=2400757, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthEqual(5, 2400757, 0.0)
    IfDamageType(7, attacked_entity=2400770, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthEqual(7, 2400770, 0.0)
    IfDamageType(8, attacked_entity=2400772, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthEqual(8, 2400772, 0.0)
    IfDamageType(9, attacked_entity=2400774, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthEqual(9, 2400774, 0.0)
    IfDamageType(13, attacked_entity=2400700, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHealthEqual(13, 2400700, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=7)
    IfConditionTrue(-1, input_condition=8)
    IfConditionTrue(-1, input_condition=9)
    IfConditionTrue(-1, input_condition=13)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(9432)
    EnableFlag(72400490)


@NeverRestart
def Event12400801():
    """ 12400801: Event 12400801 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOff(Label.L0, 1166)
    DisableBackread(2400765)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400765)
    Label(0)
    GotoIfFlagOff(Label.L1, 1191)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400730)
    Label(1)
    GotoIfFlagOff(Label.L2, 1231)
    EnableObject(2400748)
    DisableMapPart(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400750)
    Label(2)
    GotoIfFlagOff(Label.L3, 1230)
    EnableObject(2400748)
    DisableMapPart(2404601)
    EnableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400750, 103087)
    EzstateAIRequest(2400750, command_id=5, slot=1)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400750)
    Label(3)
    GotoIfFlagOff(Label.L4, 1312)
    DisableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2400770)
    Label(4)
    GotoIfFlagOff(Label.L4, 1108)
    EnableMapPart(2404604)
    DropMandatoryTreasure(2400700)
    DisableBackread(2400700)
    Label(5)


@NeverRestart
def Event12400805(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12400805: Event 12400805 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, ARG_0_3, ARG_8_11)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, ARG_4_7)
    WaitFrames(5)
    Restart()


@NeverRestart
def Event12400810(ARG_0_3: int, ARG_4_7: int):
    """ 12400810: Event 12400810 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, ARG_4_7)
    Restart()


@NeverRestart
def Event12400830(ARG_0_3: int, ARG_4_7: int):
    """ 12400830: Event 12400830 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, ARG_4_7)


@NeverRestart
def Event12400840(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12400840: Event 12400840 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(ARG_0_3)
    IfFlagOff(1, ARG_0_3)
    IfActionButtonInRegion(1, action_button_id=ARG_4_7, region=ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=ARG_8_11, destination_type=CoordEntityType.Object, model_point=210, short_move=True)
    ForceAnimation(PLAYER, 101320)
    WaitFrames(25)
    WaitFrames(20)
    EnableFlag(ARG_0_3)
    IfFlagOff(0, ARG_0_3)
    Restart()


@RestartOnRest
def Event12405700():
    """ 12405700: Event 12405700 """
    IfCharacterDead(1, 2400393)
    IfCharacterDead(1, 2400410)
    IfCharacterDead(2, 2400393)
    IfCharacterDead(2, 2400396)
    IfCharacterDead(3, 2400410)
    IfCharacterDead(3, 2400396)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    GotoIfConditionTrue(Label.L1, input_condition=2)
    GotoIfConditionTrue(Label.L2, input_condition=3)
    Label(0)
    AICommand(2400396, command_id=10, slot=0)
    SetNest(2400396, 2409007)
    ReplanAI(2400396)
    Label(1)
    AICommand(2400410, command_id=10, slot=0)
    SetNest(2400410, 2409007)
    ReplanAI(2400410)
    Label(2)
    AICommand(2400393, command_id=10, slot=0)
    SetNest(2400393, 2409007)
    ReplanAI(2400393)
    IfCharacterInsideRegion(-2, 2400393, region=2402030)
    IfCharacterInsideRegion(-2, 2400396, region=2402030)
    IfCharacterInsideRegion(-2, 2400410, region=2402030)
    IfConditionTrue(0, input_condition=-2)
    IfEntityWithinDistance(-3, 2400393, 10000, radius=5.0)
    IfEntityWithinDistance(-3, 2400396, 10000, radius=5.0)
    IfEntityWithinDistance(-3, 2400410, 10000, radius=5.0)
    IfConditionTrue(0, input_condition=-3)
    AICommand(2400393, command_id=-1, slot=0)
    ReplanAI(2400393)
    AICommand(2400396, command_id=-1, slot=0)
    ReplanAI(2400396)
    AICommand(2400410, command_id=-1, slot=0)
    ReplanAI(2400410)


@RestartOnRest
def Event12405701(ARG_0_3: int, ARG_4_7: int):
    """ 12405701: Event 12405701 """
    IfCharacterInsideRegion(-1, 2400393, region=2402030)
    IfCharacterInsideRegion(-1, 2400396, region=2402030)
    IfCharacterInsideRegion(-1, 2400410, region=2402030)
    IfConditionTrue(0, input_condition=-1)
    AICommand(ARG_0_3, command_id=10, slot=0)
    SetNest(ARG_0_3, ARG_4_7)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=2402030)
    IfEntityWithinDistance(1, 10000, ARG_0_3, radius=5.0)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12405710():
    """ 12405710: Event 12405710 """
    GotoIfFlagOff(Label.L0, 9453)
    EndOfAnimation(2401202, 1)
    NotifyDoorEventSoundDampening(2401202, state=DoorState.DoorOpening)
    End()
    Label(0)
    DisableNetworkSync()
    IfActionButtonInRegion(0, action_button_id=7000, region=2401202)
    DisplayDialog(10010171, anchor_entity=2401202, display_distance=5.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest
def Event12405750(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float):
    """ 12405750: Event 12405750 """
    EndIfThisEventSlotOn()
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=ARG_8_11)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(ARG_0_3, ARG_4_7)


@NeverRestart
def Event12401800():
    """ 12401800: Event 12401800 """
    GotoIfThisEventOff(Label.L0)
    DisableMapSound(2403802)
    DisableMapSound(2403803)
    DisableCharacter(2400800)
    DisableObject(2400801)
    Kill(2400800, award_souls=False)
    DisableObject(2401800)
    DeleteFX(2403800, erase_root_only=False)
    End()
    Label(0)
    IfCharacterDead(0, 2400800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2401800)
    DeleteFX(2403800, erase_root_only=True)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=0)
    Wait(3.0)
    KillBoss(2400800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(15)
    AwardItemLot(50000001, host_only=False)
    EnableFlag(2400)
    EnableFlag(2401)
    EnableFlag(9455)
    EnableFlag(2402)
    EnableFlag(72400512)
    StopPlayLogMeasurement(2400000)
    StopPlayLogMeasurement(2400001)
    StopPlayLogMeasurement(2400010)
    CreatePlayLog(114)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 126, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 126, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 126, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 126, PlayLogMultiplayerType.HostOnly)
    End()
    Label(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)
    EndIfClient()


@NeverRestart
def Event12401801():
    """ 12401801: Event 12401801 """
    DisableNetworkSync()
    EndIfFlagOn(12401800)
    IfFlagOn(1, 12401800)
    IfCharacterBackreadDisabled(2, 2400800)
    IfHealthLessThanOrEqual(2, 2400800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2402800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


@NeverRestart
def Event12401802():
    """ 12401802: Event 12401802 """
    EndIfFlagOn(12401800)
    DisableObject(2400801)
    EndIfThisEventOn()
    DisableCharacter(2400800)
    EnableObject(2400801)
    EnableObjectInvulnerability(2400801)
    IfFlagOff(1, 12401800)
    IfThisEventOff(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2402805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12404223)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)
    WaitFrames(1)
    EnableFlag(72400400)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(24000060, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(24000060, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObject(2400801)
    DisableFlag(9180)
    EnableCharacter(2400800)
    ForceAnimation(2400800, 7000)
    ForceAnimation(2400800, 7001)
    EnableFlag(12404800)
    EndIfFlagOn(9301)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9301)


@NeverRestart
def Event12401803():
    """ 12401803: Event 12401803 """
    DeleteFX(2403413, erase_root_only=False)
    EndIfThisEventOn()
    GotoIfFlagOn(Label.L0, 12401800)
    IfFlagOn(0, 12401800)
    Label(0)
    CreateFX(2403413)
    EndIfClient()
    IfCharacterHuman(1, PLAYER)
    IfActionButtonInRegion(1, action_button_id=2400010, region=2401801)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(1)
    DeleteFX(2403413, erase_root_only=True)
    PlayCutsceneAndMovePlayerAndSetTimePeriod(24000030, CutsceneType.Skippable, -1, CATHEDRAL_WARD, player_id=10000, time_period_id=2)
    WaitFrames(1)
    DisableFlag(9180)


@NeverRestart
def Event12401804():
    """ 12401804: Event 12401804 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12404800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(2400800)
    EnableFlag(12404800)
    EnableFlag(12401802)


@NeverRestart
def Event12404840():
    """ 12404840: Event 12404840 """
    EndIfFlagOn(12401800)
    GotoIfFlagOn(Label.L0, 12401802)
    SkipLinesIfClient(2)
    DisableObject(2401800)
    DeleteFX(2403800, erase_root_only=False)
    IfFlagOff(1, 12401800)
    IfFlagOn(1, 12401802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2401800)
    CreateFX(2403800)
    Label(0)
    IfFlagOff(2, 12401800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonInRegion(2, action_button_id=2400800, region=2401800)
    IfFlagOn(3, 12401800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2402800, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2402801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(12404800)
    Restart()


@NeverRestart
def Event12404841():
    """ 12404841: Event 12404841 """
    DisableNetworkSync()
    EndIfFlagOn(12401800)
    IfFlagOff(1, 12401800)
    IfFlagOn(1, 12401802)
    IfFlagOn(1, 12404800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonInRegion(1, action_button_id=2400800, region=2401800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2402800, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2402801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12404801)
    Restart()


@NeverRestart
def Event12404842():
    """ 12404842: Event 12404842 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, 10000, 2401800, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12404843():
    """ 12404843: Event 12404843 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, 10000, 2401800, radius=6.0)
    IfEntityWithinDistance(1, 10000, 2401800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12404802():
    """ 12404802: Event 12404802 """
    EndIfFlagOn(12401800)
    DisableAI(2400800)
    DisableHealthBar(2400800)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 12404800)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagOn(1, 12404223)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2400800, UpdateAuthority.Forced)
    Label(0)
    EnableFlag(12404223)
    EnableFlag(12404800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)
    Label(1)
    Goto(Label.L4)
    Label(2)
    AddSpecialEffect(2400800, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2400800)
    Goto(Label.L4)
    Label(3)
    AddSpecialEffect(2400800, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2400800)
    Goto(Label.L4)
    Label(4)
    EnableAI(2400800)
    EnableBossHealthBar(2400800, name=502000, slot=0)
    ForceAnimation(2400800, 7002)
    CreatePlayLog(160)
    StartPlayLogMeasurement(2410010, 176, overwrite=True)


@NeverRestart
def Event12404803():
    """ 12404803: Event 12404803 """
    DisableNetworkSync()
    EndIfFlagOn(12401800)
    GotoIfThisEventOn(Label.L0)
    DisableMapSound(2403802)
    DisableMapSound(2403803)
    IfFlagOff(1, 12401800)
    IfFlagOn(1, 12404802)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12404801)
    IfCharacterInsideRegion(1, PLAYER, region=2402802)
    IfConditionTrue(0, input_condition=1)
    SetBossMusicState(2403802, state=True)
    IfHasTAEEvent(2, 2400800, tae_event_id=100)
    Label(0)
    IfFlagOff(2, 12401800)
    IfFlagOn(2, 12404802)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12404801)
    IfCharacterInsideRegion(2, PLAYER, region=2402802)
    IfConditionTrue(0, input_condition=2)
    SetBossMusicState(2403802, state=False)
    WaitFrames(0)
    SetBossMusicState(2403803, state=True)


@NeverRestart
def Event12404804():
    """ 12404804: Event 12404804 """
    DisableNetworkSync()
    EndIfFlagOn(12401800)
    IfHealthGreaterThan(1, 2400800, 0.0)
    IfEntityWithinDistance(1, 10000, 2400800, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=1)
    IfHealthGreaterThan(2, 2400800, 0.0)
    IfEntityBeyondDistance(2, 10000, 2400800, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=0)
    Restart()


@NeverRestart
def Event12404805():
    """ 12404805: Event 12404805 """
    DisableNetworkSync()
    EndIfFlagOn(12401800)
    IfFlagOn(0, 12401800)
    SetBossMusicState(2403802, state=False)
    SetBossMusicState(2403803, state=False)
    SetBossMusicState(-1, state=False)


@NeverRestart
def Event12404807():
    """ 12404807: Event 12404807 """
    EndIfFlagOn(12401800)
    IfHealthLessThan(0, 2400800, 0.5)
    AICommand(2400800, command_id=100, slot=1)
    ReplanAI(2400800)
    IfHasTAEEvent(0, 2400800, tae_event_id=100)
    AICommand(2400800, command_id=-1, slot=1)
    ReplanAI(2400800)


@NeverRestart
def Event12404808():
    """ 12404808: Event 12404808 """
    EndIfFlagOn(12401800)
    GotoIfThisEventOn(Label.L0)
    IfCharacterHasSpecialEffect(0, 2400800, 482)
    Label(0)
    ChangeCharacterCloth(2400800, 15, state_id=2)


@RestartOnRest
def Event12404810(ARG_0_1: short, ARG_4_7: int, ARG_8_9: short, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12404810: Event 12404810 """
    EndIfFlagOn(12401800)
    CreateNPCPart(2400800, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=ARG_12_15, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(2400800, npc_part_id=ARG_4_7, material_special_effect_id=72, material_fx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, 2400800, npc_part_id=ARG_4_7, value=0)
    IfHealthLessThanOrEqual(3, 2400800, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(2400800, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=9999999, damage_correction=1.0, body_damage_correction=1.5, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(2400800, npc_part_id=ARG_4_7, material_special_effect_id=73, material_fx_id=73)
    WaitFrames(1)
    ResetAnimation(2400800, disable_interpolation=False)
    ForceAnimation(2400800, ARG_24_27)
    AddSpecialEffect(2400800, ARG_16_19, affect_npc_part_hp=False)
    CancelSpecialEffect(2400800, ARG_20_23)
    ReplanAI(2400800)
    Wait(30.0)
    AICommand(2400800, command_id=1, slot=0)
    ReplanAI(2400800)
    IfHasTAEEvent(0, 2400800, tae_event_id=300)
    SetNPCPartHealth(2400800, npc_part_id=ARG_4_7, desired_hp=-1, overwrite_max=True)
    AddSpecialEffect(2400800, ARG_20_23, affect_npc_part_hp=False)
    CancelSpecialEffect(2400800, ARG_16_19)
    AICommand(2400800, command_id=-1, slot=0)
    ReplanAI(2400800)
    WaitFrames(10)
    Restart()


@NeverRestart
def Event12404820(ARG_0_3: int, ARG_4_7: int, ARG_8_8: uchar, ARG_9_9: uchar):
    """ 12404820: Event 12404820 """
    EndIfFlagOn(12401800)
    IfCharacterHasSpecialEffect(1, 2400800, ARG_0_3)
    IfCharacterDoesNotHaveSpecialEffect(1, 2400800, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(2400800, bit_index=ARG_9_9, switch_type=OnOffChange.On)
    SetDisplayMask(2400800, bit_index=ARG_8_8, switch_type=OnOffChange.Off)
    IfCharacterDoesNotHaveSpecialEffect(2, 2400800, ARG_0_3)
    IfCharacterHasSpecialEffect(2, 2400800, ARG_4_7)
    IfConditionTrue(0, input_condition=2)
    SetDisplayMask(2400800, bit_index=ARG_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(2400800, bit_index=ARG_9_9, switch_type=OnOffChange.Off)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12404830():
    """ 12404830: Event 12404830 """
    IfCharacterHasSpecialEffect(1, 2400800, 2150)
    IfCharacterHasSpecialEffect(1, 2400800, 5639)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400800, 3035)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12406900(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12406900: Event 12406900 """
    IfCharacterInsideRegion(0, PLAYER, region=ARG_0_3)
    PlaySoundEffect(anchor_entity=ARG_4_7, sound_type=SoundType.a_Ambient, sound_id=ARG_8_11)
    WaitFrames(1)


@NeverRestart
def Event12400990():
    """ 12400990: Event 12400990 """
    EndIfThisEventOn()
    IfStandingOnHitbox(0, 2404101)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 194, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 194, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 194, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 194, PlayLogMultiplayerType.HostOnly)


@NeverRestart
def Event12407020(ARG_0_3: int, ARG_4_7: int):
    """ 12407020: Event 12407020 """
    IfFlagOn(0, ARG_0_3)
    Move(PLAYER, destination=ARG_4_7, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    ForceAnimation(PLAYER, 101160, skip_transition=True)
    Wait(4.0)
    DisableFlag(ARG_0_3)


@NeverRestart
def Event12407040(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12407040: Event 12407040 """
    IfFlagOn(0, ARG_0_3)
    DisableFlag(ARG_0_3)
    MovePlayerToRespawnPoint(ARG_4_7)
    EnableFlag(ARG_8_11)


@RestartOnRest
def Event12407050(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12407050: Event 12407050 """
    EndIfFlagOn(ARG_0_3)
    IfCharacterBackreadEnabled(0, ARG_4_7)
    Move(ARG_4_7, destination=ARG_8_11, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    ForceAnimation(ARG_4_7, 101165, loop=True)
    Wait(1.0)
    Move(ARG_4_7, destination=ARG_8_11, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    IfFlagOn(0, ARG_0_3)
    ForceAnimation(ARG_4_7, 101166, wait_for_completion=True)
    DisableCharacter(ARG_4_7)


@NeverRestart
def Event12407000():
    """ 12407000: Event 12407000 """
    SkipLinesIfFlagRangeAnyOn(1, (9001, 9010))
    End()
    EnableFlag(9210)
    IfFlagOff(0, 9210)
    SkipLinesIfFlagOff(3, 9001)
    EnableFlag(12407811)
    EnableFlag(12407810)
    SetRespawnPoint(2402950)
    SkipLinesIfFlagOff(3, 9002)
    EnableFlag(12407831)
    EnableFlag(12407830)
    SetRespawnPoint(2402951)
    SkipLinesIfFlagOff(3, 9003)
    EnableFlag(12407851)
    EnableFlag(12407850)
    SetRespawnPoint(2402952)
    SkipLinesIfFlagOff(3, 9004)
    EnableFlag(12407871)
    EnableFlag(12407870)
    SetRespawnPoint(2402953)
    SkipLinesIfFlagOff(3, 9005)
    EnableFlag(12407891)
    EnableFlag(12407890)
    SetRespawnPoint(2402954)
    SkipLinesIfFlagOff(3, 9006)
    EnableFlag(12407911)
    EnableFlag(12407910)
    SetRespawnPoint(2402955)
    SkipLinesIfFlagOff(3, 9007)
    EnableFlag(12407931)
    EnableFlag(12407930)
    SetRespawnPoint(2402956)
    SkipLinesIfFlagOff(3, 9008)
    EnableFlag(12407951)
    EnableFlag(12407950)
    SetRespawnPoint(2402957)
    SkipLinesIfFlagOff(3, 9009)
    EnableFlag(12407971)
    EnableFlag(12407970)
    SetRespawnPoint(2402958)
    SkipLinesIfFlagOff(3, 9010)
    EnableFlag(12407991)
    EnableFlag(12407990)
    SetRespawnPoint(2402959)
    DisableFlagRange((9000, 9010))


@RestartOnRest
def Event12404450(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12404450: Event 12404450 """
    EndIfThisEventSlotOn()
    EndIfClient()
    SetEventPoint(ARG_0_3, region=ARG_4_7, reaction_range=1.0)
    IfFlagOn(1, ARG_8_11)
    IfFlagOff(1, ARG_12_15)
    IfFlagOn(1, ARG_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_0_3, command_id=990, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12404400(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12404400: Event 12404400 """
    GotoIfFlagOn(Label.L0, ARG_0_3)
    DisableFlag(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, ARG_8_11)
    IfFlagOff(1, ARG_12_15)
    IfFlagOff(1, ARG_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOff(1, 2400)
    IfFlagOff(1, 2401)
    IfFlagOff(-1, ARG_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    EnableFlag(ARG_0_3)
    CreateFX(ARG_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, ARG_8_11)
    IfFlagOff(2, ARG_12_15)
    IfFlagOff(2, ARG_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOff(2, 2400)
    IfFlagOff(2, 2401)
    IfFlagOff(-3, ARG_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12404410(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 12404410: Event 12404410 """
    SkipLinesIfFlagOn(1, ARG_12_15)
    DisableCharacter(ARG_4_7)
    SkipLinesIfFlagOn(3, ARG_16_19)
    IfClient(1)
    IfFlagOn(1, ARG_12_15)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(ARG_4_7)
    EndIfFlagOn(ARG_24_27)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(ARG_4_7, UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, ARG_12_15)
    IfFlagOff(2, ARG_16_19)
    IfFlagOn(2, ARG_20_23)
    IfFlagOff(2, ARG_24_27)
    IfActionButtonInRegion(2, action_button_id=ARG_28_31, region=ARG_4_7)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682, affect_npc_part_hp=False)
    SummonNPC(ARG_0_3, ARG_4_7, ARG_8_11, summon_flag=ARG_12_15, dismissal_flag=ARG_16_19)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)
    DisableHitbox(2404120)


@RestartOnRest
def Event12404460(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12404460: Event 12404460 """
    EndIfClient()
    IfFlagOn(1, ARG_20_23)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    RotateToFaceEntity(ARG_0_3, ARG_8_11, animation=ARG_16_19, wait_for_completion=True)
    IfCharacterInsideRegion(2, ARG_0_3, region=ARG_12_15)
    RestartIfConditionFalse(2)
    SetEventPoint(ARG_0_3, region=ARG_8_11, reaction_range=1.0)
    AICommand(ARG_0_3, command_id=990, slot=0)
    ReplanAI(ARG_0_3)
    DisableGravity(ARG_0_3)
    DisableCollision(ARG_0_3)
    IfCharacterInsideRegion(0, ARG_0_3, region=ARG_24_27)
    EnableGravity(ARG_0_3)
    EnableCollision(ARG_0_3)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12404490():
    """ 12404490: Event 12404490 """
    DisableNetworkSync()
    IfHost(1)
    IfFlagOn(1, 12404420)
    IfFlagOff(1, 12404430)
    IfFlagOn(1, 12404800)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect_WithUnknownEffect(2400910, 35, affect_npc_parts_hp=False)
    WaitFrames(1)
    Restart()
