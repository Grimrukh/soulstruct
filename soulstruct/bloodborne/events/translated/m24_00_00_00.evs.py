"""CATHEDRAL WARD

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
220: N:\\SPRJ\\data\\Param\\event\\common.emevd
296: 
298: 
300: 
302: 
"""
from soulstruct.bloodborne.events import *
from .common_entities import *
from .m24_00_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(7600, slot=20, args=(2401999, 2403999))
    RunEvent(7600, slot=21, args=(2401998, 2403998))
    RunEvent(7600, slot=22, args=(2401997, 2403997))
    RunEvent(7600, slot=23, args=(2401996, 2403996))
    RunEvent(7600, slot=24, args=(2401995, 2403995))
    RunEvent(7000, slot=10, args=(2400950, 2401950, 999, 12407800))
    RunEvent(7000, slot=11, args=(2400951, 2401951, Flags.VicarAmeliaDead, 12407820))
    RunEvent(7100, slot=10, args=(72400200, 2401950))
    RunEvent(7100, slot=11, args=(72400201, 2401951))
    RunEvent(7200, slot=10, args=(72400100, 2401950, 2102950))
    RunEvent(7200, slot=11, args=(72400101, 2401951, 2102950))
    RunEvent(7300, slot=10, args=(72102400, 2401950))
    RunEvent(7300, slot=11, args=(72102401, 2401951))
    RunEvent(9200, slot=2, args=(2403900,))
    RunEvent(9220, slot=2, args=(2400710, 12404220, 12404221, 2400, 24, 0), arg_types="iiiiBB")
    RunEvent(9240, slot=2, args=(2400710, 12404220, 12404221, 12404222, 24, 0), arg_types="iiiiBB")
    RunEvent(9260, slot=2, args=(2400710, 12404220, 12404221, 12404222, 24, 0), arg_types="iiiiBB")
    RunEvent(9280, slot=2, args=(2400710, 12404220, 12404221, 2400, 12404223, 24, 0), arg_types="iiiiiBB")
    SkipLinesIfFlagEnabled(7, 12400160)
    EnableFlag(2400)
    EnableFlag(2401)
    EnableFlag(2405)
    EnableFlag(2406)
    DisableFlag(2402)
    DisableFlag(2407)
    SkipLines(14)
    SkipLinesIfFlagEnabled(7, Flags.VicarAmeliaDead)
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
    DeleteVFX(2403910, erase_root_only=False)
    RunEvent(12404400, slot=0, args=(12404440, 2403910, 12404420, 12404430, Flags.VicarAmeliaDead, 6001))
    RunEvent(12404410, slot=0, args=(0, 2400910, 2402910, 12404420, 12404430, 12404440, Flags.VicarAmeliaDead, 10567))
    RunEvent(12404450, slot=0, args=(2400910, 2402911, 12404420, 12404430, Flags.VicarAmeliaFogEntered))
    RunEvent(12404460, slot=0, args=(2400910, 2402911, 2402800, 2402801, 101130, 12404450, 2402801))
    Event12404490()
    CreateObjectVFX(900130, obj=2401900, model_point=200)
    CreateObjectVFX(900130, obj=2401901, model_point=200)
    RegisterLadder(start_climbing_flag=12400600, stop_climbing_flag=12400601, obj=2401020)
    RegisterLadder(start_climbing_flag=12400602, stop_climbing_flag=12400603, obj=2401021)
    RegisterLadder(start_climbing_flag=12400604, stop_climbing_flag=12400605, obj=2401022)
    RegisterLadder(start_climbing_flag=12400606, stop_climbing_flag=12400607, obj=2401023)
    RegisterLadder(start_climbing_flag=12400608, stop_climbing_flag=12400609, obj=2401024)
    CreateProjectileOwner(2400000)
    CreateProjectileOwner(2402070)
    CreateProjectileOwner(2402071)
    CreateProjectileOwner(2402072)
    DisableGravity(2400899)
    DisableCharacterCollision(2400899)
    CreateHazard(
        12400190,
        2401017,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12400191,
        2401018,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6646)
    EnableFlag(12401999)
    SkipLinesIfFlagEnabled(6, 12401999)
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
    SkipLinesIfFlagDisabled(1, 6310)
    EnableFlag(12401998)
    SkipLinesIfFlagEnabled(6, 12401998)
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
    SkipLinesIfFlagDisabled(1, 6311)
    EnableFlag(12401997)
    SkipLinesIfFlagEnabled(6, 12401997)
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
    Event12400125()
    Event12400126()
    Event12400127()
    Event12400128()
    RunEvent(12400130, slot=0, args=(2401204, 1, 12400112, 12400130))
    RunEvent(12400130, slot=1, args=(2401200, 2, 12400113, 12400131))
    RunEvent(12400130, slot=2, args=(2101201, 1, 12400102, 12400132))
    RunEvent(12400130, slot=3, args=(2101202, 2, 12400103, 12400133))
    RunEvent(12400130, slot=5, args=(2401211, 1, 12400190, 12400135))
    RunEvent(12400130, slot=6, args=(2401212, 1, 12400191, 12400136))
    RunEvent(12400130, slot=7, args=(2401201, 1, 12400114, 12400137))
    RunEvent(12400130, slot=8, args=(2401213, 2, 12400200, 12400138))
    Event12400146()
    Event12400147()
    Event12400148()
    Event12400149()
    Event12400159()
    Event12400155()
    Event12400156()
    Event12400158()
    Event12400161()
    Event12400174()
    Event12400175()
    RunEvent(12400179, slot=0, args=(2401015,))
    RunEvent(12400179, slot=1, args=(2401016,))
    Event12400185()
    RunEvent(12400200, slot=2, args=(2400344, 52400980))
    RunEvent(12400200, slot=3, args=(2400371, 52400960))
    RunEvent(12400200, slot=4, args=(2400372, 52400990))
    RunEvent(12400200, slot=5, args=(2400373, 52400970))
    RunEvent(12400200, slot=6, args=(2400374, 52400950))
    RunEvent(12400200, slot=7, args=(2400375, 52400940))
    Event12400300()
    RunEvent(12400350, slot=0, args=(2401500, 12400450))
    RunEvent(12400350, slot=2, args=(2401503, 12400453))
    RunEvent(12400350, slot=3, args=(2401504, 12400454))
    RunEvent(12400350, slot=6, args=(2401506, 12400456))
    Event12400750()
    Event12400765()
    Event12400760()
    Event12400420()
    Event12400823()
    Event12400824()
    Event12400825()
    Event12400826()
    RunEvent(12400850, slot=0, args=(2407020, 2407021, 2407022, 12400130, 0, 0.0, 0, 0), arg_types="iiiiifii")
    RunEvent(12400850, slot=1, args=(2407025, 2407026, 2407027, 12400132, 0, 0.0, 0, 0), arg_types="iiiiifii")
    RunEvent(12400850, slot=2, args=(2407028, 2407029, 2407030, 12400131, 0, 0.0, 0, 0), arg_types="iiiiifii")
    RunEvent(12400850, slot=3, args=(2406700, 2406701, 2406702, 12400133, 0, 0.0, 0, 0), arg_types="iiiiifii")
    Event12400854()
    Event12400860()
    Event12405710()
    RunEvent(12400865, slot=0, args=(2400660,))
    RunEvent(12400865, slot=1, args=(2400661,))
    RunEvent(12400780, slot=0, args=(2400360,))
    RunEvent(12400780, slot=1, args=(2400361,))
    RunEvent(12400780, slot=2, args=(2400362,))
    RunEvent(12400780, slot=3, args=(2400363,))
    RunEvent(12400791, slot=0, args=(2400360,))
    RunEvent(12400791, slot=1, args=(2400361,))
    RunEvent(12400791, slot=2, args=(2400363,))
    Event12400797()
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
    RunEvent(12405600, slot=1, args=(2400400, 2402022, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=2, args=(2400400, 2402017, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=3, args=(2400126, 2402012, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=4, args=(2400127, 2402013, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=5, args=(2400128, 2402013, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=6, args=(2400136, 2402015, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=7, args=(2400137, 2402015, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=8, args=(2400125, 2404302, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=10, args=(2400231, 2404312, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=11, args=(2400508, 2404320, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=12, args=(2400508, 2404310, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=13, args=(2400120, 2402073, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=14, args=(2400121, 2402073, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=15, args=(2400392, 2402016, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=18, args=(2400401, 2402029, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=19, args=(2400401, 2402017, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=20, args=(2400106, 2404310, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=22, args=(2400122, 2402081, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=23, args=(2400116, 2404302, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=24, args=(2400211, 2402075, 5.0, 0.0), arg_types="iiff")
    Event12405660()
    RunEvent(12405350, slot=0, args=(2400391, 2402310, 2409015, 2403105, 2402311))
    Event12405195()
    RunEvent(12405370, slot=0, args=(2400210,))
    RunEvent(12405370, slot=1, args=(2400211,))
    RunEvent(12405670, slot=0, args=(2400203, 2404332, 2404301, 5.0, 0.0), arg_types="iiiff")
    RunEvent(12405330, slot=0, args=(2400500,))
    Event12405360()
    RunEvent(12405365, slot=0, args=(2400374, 2404087, 2403108))
    RunEvent(12405365, slot=1, args=(2400375, 2404086, 2403107))
    RunEvent(12405850, slot=0, args=(2400450, 2401652, 2402061, 10, 12405521))
    RunEvent(12405810, slot=0, args=(2400408, 2402022, 2404083, 10, 12405520))
    RunEvent(12405820, slot=0, args=(2400408, 2404083))
    RunEvent(12405820, slot=1, args=(2400450, 2402061))
    RunEvent(12405840, slot=0, args=(2400408, 10, 12405520))
    RunEvent(12405840, slot=1, args=(2400450, 10, 12405521))
    Event12405240()
    Event12405241()
    Event12405680()
    RunEvent(12405682, slot=0, args=(2400107, 2400002, 6.0, 12405686, 0.0), arg_types="iifif")
    RunEvent(12405682, slot=2, args=(2400109, 2400001, 1.0, 12405688, 0.0), arg_types="iifif")
    RunEvent(12405682, slot=3, args=(2400110, 2400004, 1.0, 12405689, 0.0), arg_types="iifif")
    Event12405140()
    RunEvent(12405686, slot=0, args=(2400107,))
    RunEvent(12405686, slot=2, args=(2400109,))
    RunEvent(12405686, slot=3, args=(2400110,))
    Event12405690()
    RunEvent(12405130, slot=0, args=(2400107, 12405682, 0))
    RunEvent(12405130, slot=1, args=(2400111, 12405140, 0))
    RunEvent(12405130, slot=2, args=(2400109, 12405682, 2))
    RunEvent(12405130, slot=3, args=(2400110, 12405682, 3))
    RunEvent(12405130, slot=4, args=(2400106, 12405680, 0))
    RunEvent(12405600, slot=41, args=(2400410, 2402028, 3.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=42, args=(2400420, 2402511, 3.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=43, args=(2400423, 2402511, 3.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=44, args=(2400501, 2402157, 3.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=45, args=(2400502, 2402157, 3.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=46, args=(2400503, 2402157, 3.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=47, args=(2400504, 2402157, 3.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=48, args=(2400505, 2402157, 3.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=49, args=(2400506, 2402157, 3.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=50, args=(2400507, 2402157, 3.0, 0.0), arg_types="iiff")
    Event12405700()
    RunEvent(12405701, slot=0, args=(2400398, 2404370))
    RunEvent(12405701, slot=1, args=(2400399, 2404371))
    RunEvent(12405600, slot=52, args=(2400600, 2402500, 1.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=53, args=(2400601, 2402500, 1.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=54, args=(2400602, 2402500, 1.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=55, args=(2400603, 2402507, 5.0, 0.0), arg_types="iiff")
    RunEvent(12405600, slot=56, args=(2400603, 2402508, 5.0, 0.0), arg_types="iiff")
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
    Event12405335()
    RunEvent(12405120, slot=1, args=(2400156, 5569))
    RunEvent(12405120, slot=2, args=(2400162, 5569))
    RunEvent(12405120, slot=3, args=(2400220, 5557))
    RunEvent(12405120, slot=4, args=(2400116, 5557))
    RunEvent(12405120, slot=5, args=(2400114, 5557))
    RunEvent(12405120, slot=6, args=(2400127, 5557))
    RunEvent(12405120, slot=8, args=(2400139, 5557))
    RunEvent(12405120, slot=9, args=(2400137, 5557))
    Event12405320()
    RunEvent(12405250, slot=0, args=(12400168, 2406790, 12405175))
    RunEvent(12405251, slot=0, args=(12400177, 2406791, 12400178))
    RunEvent(12405251, slot=1, args=(12400157, 2406792, 12405179))
    Event12405259()
    Event12405260()
    Event12405262()
    Event12400410()
    Event12405263()
    RunEvent(12405430, slot=0, args=(2490, 2490, 7, 40, 12405500, 2400114), arg_types="hihiii")
    RunEvent(12405430, slot=1, args=(2491, 2491, 8, 40, 12405500, 2400114), arg_types="hihiii")
    RunEvent(12405430, slot=2, args=(2490, 2490, 7, 40, 12405501, 2400126), arg_types="hihiii")
    RunEvent(12405430, slot=3, args=(2491, 2491, 8, 40, 12405501, 2400126), arg_types="hihiii")
    RunEvent(12405430, slot=6, args=(2490, 2490, 7, 40, 12405503, 2400133), arg_types="hihiii")
    RunEvent(12405430, slot=7, args=(2491, 2491, 8, 40, 12405503, 2400133), arg_types="hihiii")
    RunEvent(12405430, slot=8, args=(2490, 2490, 7, 40, 12405504, 2400203), arg_types="hihiii")
    RunEvent(12405430, slot=9, args=(2491, 2491, 8, 40, 12405504, 2400203), arg_types="hihiii")
    RunEvent(12405430, slot=10, args=(2490, 2490, 7, 40, 12405505, 2400205), arg_types="hihiii")
    RunEvent(12405430, slot=11, args=(2491, 2491, 8, 40, 12405505, 2400205), arg_types="hihiii")
    RunEvent(12405430, slot=14, args=(2490, 2490, 7, 40, 12405507, 2400207), arg_types="hihiii")
    RunEvent(12405430, slot=15, args=(2491, 2491, 8, 40, 12405507, 2400207), arg_types="hihiii")
    RunEvent(12405430, slot=16, args=(2490, 2490, 7, 40, 12405508, 2400603), arg_types="hihiii")
    RunEvent(12405430, slot=17, args=(2491, 2491, 8, 40, 12405508, 2400603), arg_types="hihiii")
    RunEvent(12405400, slot=0, args=(2490, 2490, 7, 7003, 5907, 12405500, 12405530, 2400114), arg_types="hihiiiii")
    RunEvent(12405400, slot=1, args=(2491, 2491, 8, 7000, 5907, 12405500, 12405560, 2400114), arg_types="hihiiiii")
    RunEvent(12405400, slot=2, args=(2490, 2490, 7, 7003, 5907, 12405501, 12405531, 2400126), arg_types="hihiiiii")
    RunEvent(12405400, slot=3, args=(2491, 2491, 8, 7000, 5907, 12405501, 12405561, 2400126), arg_types="hihiiiii")
    RunEvent(12405400, slot=6, args=(2490, 2490, 7, 7003, 5907, 12405503, 12405533, 2400133), arg_types="hihiiiii")
    RunEvent(12405400, slot=7, args=(2491, 2491, 8, 7000, 5907, 12405503, 12405563, 2400133), arg_types="hihiiiii")
    RunEvent(12405400, slot=8, args=(2490, 2490, 7, 7003, 5907, 12405504, 12405534, 2400203), arg_types="hihiiiii")
    RunEvent(12405400, slot=9, args=(2491, 2491, 8, 7000, 5907, 12405504, 12405564, 2400203), arg_types="hihiiiii")
    RunEvent(12405400, slot=10, args=(2490, 2490, 7, 7003, 5907, 12405505, 12405535, 2400205), arg_types="hihiiiii")
    RunEvent(12405400, slot=11, args=(2491, 2491, 8, 7000, 5907, 12405505, 12405565, 2400205), arg_types="hihiiiii")
    RunEvent(12405400, slot=14, args=(2490, 2490, 7, 7003, 5907, 12405507, 12405537, 2400207), arg_types="hihiiiii")
    RunEvent(12405400, slot=15, args=(2491, 2491, 8, 7000, 5907, 12405507, 12405567, 2400207), arg_types="hihiiiii")
    RunEvent(12405400, slot=16, args=(2490, 2490, 7, 7003, 5907, 12405508, 12405538, 2400603), arg_types="hihiiiii")
    RunEvent(12405400, slot=17, args=(2491, 2491, 8, 7000, 5907, 12405508, 12405568, 2400603), arg_types="hihiiiii")
    RunEvent(12405460, slot=0, args=(10, 40, 12405530, 2400114, 0, 10), arg_types="iiiiBB")
    RunEvent(12405460, slot=1, args=(30, 40, 12405560, 2400114, 1, 11), arg_types="iiiiBB")
    RunEvent(12405460, slot=2, args=(10, 40, 12405531, 2400126, 0, 10), arg_types="iiiiBB")
    RunEvent(12405460, slot=3, args=(30, 40, 12405561, 2400126, 1, 11), arg_types="iiiiBB")
    RunEvent(12405460, slot=6, args=(10, 40, 12405533, 2400133, 0, 10), arg_types="iiiiBB")
    RunEvent(12405460, slot=7, args=(30, 40, 12405563, 2400133, 1, 11), arg_types="iiiiBB")
    RunEvent(12405460, slot=8, args=(10, 40, 12405534, 2400203, 0, 10), arg_types="iiiiBB")
    RunEvent(12405460, slot=9, args=(30, 40, 12405564, 2400203, 1, 11), arg_types="iiiiBB")
    RunEvent(12405460, slot=10, args=(10, 40, 12405535, 2400205, 0, 10), arg_types="iiiiBB")
    RunEvent(12405460, slot=11, args=(30, 40, 12405565, 2400205, 1, 11), arg_types="iiiiBB")
    RunEvent(12405460, slot=14, args=(10, 40, 12405537, 2400207, 0, 10), arg_types="iiiiBB")
    RunEvent(12405460, slot=15, args=(30, 40, 12405567, 2400207, 1, 11), arg_types="iiiiBB")
    RunEvent(12405460, slot=16, args=(10, 40, 12405538, 2400603, 0, 10), arg_types="iiiiBB")
    RunEvent(12405460, slot=17, args=(30, 40, 12405568, 2400603, 1, 11), arg_types="iiiiBB")
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

    # VICAR AMELIA
    Event12404842()
    Event12404843()
    VicarAmeliaDies()
    PlayVicarAmeliaDeathSound()
    VicarAmeliaFirstTime()
    PlayMasterWillemCutscene()
    EnterVicarAmeliaBossFog()
    EnterVicarAmeliaBossFogAsSummon()
    StartVicarAmeliaBattle()
    ControlVicarAmeliaMusic()
    ControlVicarAmeliaCamera()
    StopVicarAmeliaMusic()
    VicarAmeliaPhaseTwoTrigger()
    ControlVicarAmeliaCloth()
    VicarAmeliaStopsHealing()
    SummonStartVicarAmeliaBattle()
    VicarAmeliaLimbDamage(0, 2400, 2400, 1, 80, 480, 490, 8020)
    VicarAmeliaLimbDamage(1, 2401, 2401, 2, 150, 481, 491, 8000)
    VicarAmeliaLimbDamage(2, 2402, 2402, 3, 150, 482, 492, 8010)
    VicarAmeliaLimbDamage(3, 2403, 2403, 4, 200, 483, 493, 8030)
    VicarAmeliaLimbDamage(4, 2404, 2404, 5, 200, 484, 494, 8040)
    VicarAmeliaLimbAppearance(0, 480, 490, 5, 10)
    VicarAmeliaLimbAppearance(1, 481, 491, 6, 11)
    VicarAmeliaLimbAppearance(2, 482, 492, 7, 12)
    VicarAmeliaLimbAppearance(3, 483, 493, 8, 13)
    VicarAmeliaLimbAppearance(4, 484, 494, 9, 14)

    Event12400800()
    Event12400801()
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
    Event12400501()
    # Event12400504()
    Event12400507()
    Event12400512()
    Event12400508()
    Event12400513()
    Event12400514()
    Event12400505()
    Event12400901()
    Event12400903()
    Event12400904()
    Event12400952()
    Event12400953()
    Event12400954()
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
    Event12400521()
    Event12400525()
    Event12400523()
    Event12400524()
    Event12400531()
    Event12400522()
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
    Event12400610()
    Event12400611()
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
    Event12405157()
    Event12405158()
    Event12405159()
    Event12400561()
    Event12400563()
    Event12400564()
    Event12400565()
    Event12400566()
    Event12400567()
    Event12400569()
    Event12400570()
    Event12400571()
    Event12400572()
    Event12400568()
    DisableFlag(72400310)
    DisableFlag(72400311)
    SetTeamType(2400700, TeamType.Ally)
    Event12400701()
    Event12400702()
    Event12400703()
    Event12400704()
    Event12400705()
    Event12400706()
    Event12400707()
    RunEvent(12400708, slot=0, args=(1164, 72400316, 1163, 1161, 0))
    RunEvent(12400708, slot=1, args=(1181, 72400317, 1190, 1183, 0))
    RunEvent(12400708, slot=2, args=(1304, 72400318, 1309, 1303, 1))
    RunEvent(12400708, slot=3, args=(1224, 72400319, 1223, 1222, 0))
    RunEvent(12400713, slot=0, args=(1164, 1163))
    RunEvent(12400713, slot=1, args=(1181, 1190))
    RunEvent(12400713, slot=2, args=(1304, 1309))
    RunEvent(12400713, slot=3, args=(1224, 1223))
    Event12400720()
    Event12400721()
    Event12400722()
    Event12400723()
    Event12400728()
    Event12400729()
    Event12400730()
    Event12400731()
    RunEvent(12400732, slot=3)
    Event12400737()
    Event12400738()
    Event12400580()
    Event12400581()
    Event12400582()
    Event12400401()
    Event12400402()
    Event12400403()
    Event12400591()
    RunEvent(12400592, slot=0, args=(2400760, 72400475))
    RunEvent(12400592, slot=1, args=(2400763, 72400476))
    RunEvent(12400593, slot=0, args=(2400760, 1341, 72400475))
    RunEvent(12400593, slot=1, args=(2400763, 1345, 72400476))
    RunEvent(12400594, slot=0, args=(2400760, 1342))
    RunEvent(12400594, slot=1, args=(2400763, 1346))
    Event12405271()
    Event12405272()
    Event12400990()
    GotoIfFlagDisabled(Label.L0, Flags.VicarAmeliaDead)
    DisableMapCollision(2404121)

    # --- 0 --- #
    DefineLabel(0)


def Preconstructor():
    """ 50: Event 50 """
    PostDestruction(2404301)
    DisableAnimations(2403950)
    DisableGravity(2403950)
    DisableCharacterCollision(2403950)
    DisableAnimations(2403951)
    DisableGravity(2403951)
    DisableCharacterCollision(2403951)
    DisableAnimations(2403952)
    DisableGravity(2403952)
    DisableCharacterCollision(2403952)
    Event12404000()
    Event12400500()
    Event12400560()
    Event12400900()
    Event12400520()
    Event12400622()
    Event12400624()
    Event12400629()
    Event12400650()
    Event12400700()
    Event12400590()
    DisableFlag(9432)
    DisableAnimations(2400899)
    DisableGravity(2400899)
    DisableCharacterCollision(2400899)
    SetNetworkUpdateRate(2400899, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.On)
    DisableAnimations(2400650)
    DisableGravity(2400650)
    DisableCharacterCollision(2400650)


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

    # --- 0 --- #
    DefineLabel(0)
    IfPlayerInsightAmountLessThan(3, 40)
    GotoIfConditionTrue(Label.L1, input_condition=3)
    EnableFlag(12404001)
    EnableFlag(12404002)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfPlayerInsightAmountLessThan(4, 15)
    EndIfConditionTrue(4)
    EnableFlag(12404002)


def Event12404100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12404100: Event 12404100 """
    DisableNetworkSync()
    IfActionButtonParamActivated(0, action_button_id=arg_4_7, entity=arg_0_3)
    DisplayDialog(
        arg_8_11,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12400070(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12400070: Event 12400070 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    Wait(0.0)


def Event12400080(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12400080: Event 12400080 """
    DisableNetworkSync()
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    IfActionButtonParamActivated(2, action_button_id=arg_12_15, entity=arg_0_3)
    IfFlagChange(3, arg_4_7)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 3)
    DisplayDialog(
        10010160,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12400095(_, arg_0_3: int):
    """ 12400095: Event 12400095 """
    DisableNetworkSync()
    IfActionButtonParamActivated(0, action_button_id=2400040, entity=arg_0_3)
    DisplayDialog(
        CommonEventTexts.Locked,
        anchor_entity=PLAYER,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12400100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12400100: Event 12400100 """
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)


def Event12400125():
    """ 12400125: Event 12400125 """
    IfObjectActivated(-1, obj_act_id=12400162)
    IfObjectActivated(-1, obj_act_id=12400163)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 12400177)
    IfFlagDisabled(1, 12400178)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12400177)
    EnableFlag(12400178)
    ForceAnimation(2401207, 1)
    Wait(1.0)
    CreateObjectVFX(920204, obj=2401207, model_point=200)
    CreateObjectVFX(920205, obj=2401207, model_point=201)
    Wait(3.0)
    DisableFlag(12400178)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    Restart()


def Event12400126():
    """ 12400126: Event 12400126 """
    IfObjectActivated(-2, obj_act_id=12400162)
    IfObjectActivated(-2, obj_act_id=12400163)
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(1, 12400177)
    IfFlagDisabled(1, 12400178)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12400177)
    EnableFlag(12400178)
    ForceAnimation(2401207, 2)
    Wait(1.0)
    CreateObjectVFX(920204, obj=2401207, model_point=200)
    CreateObjectVFX(920205, obj=2401207, model_point=201)
    Wait(3.0)
    DisableFlag(12400178)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    Restart()


def Event12400127():
    """ 12400127: Event 12400127 """
    DisableNetworkSync()
    IfFlagEnabled(1, 12400178)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2401006)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12400128():
    """ 12400128: Event 12400128 """
    GotoIfFlagEnabled(Label.L0, 12400177)
    EndOfAnimation(2401207, 2)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(2401207, 1)
    EnableObjectActivation(2401006, obj_act_id=2400000)


def Event12400130(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12400130: Event 12400130 """
    SkipLinesIfFlagDisabled(4, arg_12_15)
    EndOfAnimation(arg_0_3, arg_4_7)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()
    IfObjectActivated(0, obj_act_id=arg_8_11)
    WaitFrames(0)


def Event12400146():
    """ 12400146: Event 12400146 """
    IfFlagEnabled(1, 12400150)
    IfFlagDisabled(2, 12400150)
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


def Event12400147():
    """ 12400147: Event 12400147 """
    IfFlagEnabled(3, 12400150)
    IfFlagEnabled(3, 12400151)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagEnabled(1, 12400150)
    IfFlagDisabled(1, 12400151)
    IfCharacterInsideRegion(1, PLAYER, region=2402054)
    IfFlagEnabled(2, 12400150)
    IfFlagDisabled(2, 12400151)
    IfObjectActivated(2, obj_act_id=12400161)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
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


def Event12400148():
    """ 12400148: Event 12400148 """
    IfFlagDisabled(3, 12400150)
    IfFlagEnabled(3, 12400151)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagDisabled(1, 12400150)
    IfFlagDisabled(1, 12400151)
    IfCharacterInsideRegion(1, PLAYER, region=2402055)
    IfFlagDisabled(2, 12400150)
    IfFlagDisabled(2, 12400151)
    IfObjectActivated(2, obj_act_id=12400160)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
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


def Event12400149():
    """ 12400149: Event 12400149 """
    DisableNetworkSync()
    IfFlagEnabled(1, 12400150)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2401003)
    IfFlagDisabled(2, 12400150)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=2401004)
    IfFlagEnabled(3, 12400151)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=2401003)
    IfFlagEnabled(4, 12400151)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=2401004)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12400155():
    """ 12400155: Event 12400155 """
    IfObjectActivated(-1, obj_act_id=12400164)
    IfObjectActivated(-1, obj_act_id=12400165)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 12400157)
    IfFlagDisabled(1, 12405179)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12400157)
    EnableFlag(12405179)
    ForceAnimation(2401208, 1)
    Wait(1.0)
    CreateObjectVFX(920204, obj=2401208, model_point=200)
    CreateObjectVFX(920205, obj=2401208, model_point=201)
    Wait(3.0)
    DisableFlag(12405179)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    Restart()


def Event12400156():
    """ 12400156: Event 12400156 """
    IfObjectActivated(-2, obj_act_id=12400164)
    IfObjectActivated(-2, obj_act_id=12400165)
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(1, 12400157)
    IfFlagDisabled(1, 12405179)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12400157)
    EnableFlag(12405179)
    ForceAnimation(2401208, 2)
    Wait(1.0)
    CreateObjectVFX(920204, obj=2401208, model_point=200)
    CreateObjectVFX(920205, obj=2401208, model_point=201)
    Wait(3.0)
    DisableFlag(12405179)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    Restart()


def Event12400158():
    """ 12400158: Event 12400158 """
    DisableNetworkSync()
    IfFlagEnabled(1, 12405179)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2401008)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12400159():
    """ 12400159: Event 12400159 """
    GotoIfFlagEnabled(Label.L0, 12400157)
    EndOfAnimation(2401208, 2)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(2401208, 1)
    EnableObjectActivation(2401008, obj_act_id=2400000)


@RestartOnRest
def Event12400760():
    """ 12400760: Event 12400760 """
    GotoIfFlagDisabled(Label.L0, 12400160)
    ForceAnimation(2400650, 7020, loop=True)
    EndOfAnimation(2401220, 1)
    DisableObjectActivation(2401014, obj_act_id=2400000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2400650, 7022, loop=True)
    IfPlayerDoesNotHaveGood(1, 4011, including_box=False)
    IfActionButtonParamActivated(1, action_button_id=2400030, entity=2401220)
    IfPlayerHasGood(2, 4011, including_box=False)
    IfActionButtonParamActivated(2, action_button_id=2400030, entity=2401220)
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
    CreateObjectVFX(920204, obj=2401220, model_point=200)
    CreateObjectVFX(920205, obj=2401220, model_point=201)
    EnableFlag(12400160)
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    DisableFlag(2400)
    DisableFlag(2401)
    DisableFlag(2405)
    DisableFlag(2406)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableObjectActivation(2401014, obj_act_id=2400000)
    RotateToFaceEntity(PLAYER, 2401014, animation=101310)
    Wait(1.0)
    ForceAnimation(2400650, 7023)
    ForceAnimation(2401014, 1)
    WaitFrames(105)
    ForceAnimation(2401220, 1)
    WaitFrames(24)
    ForceAnimation(2400650, 7022, loop=True)
    WaitFrames(6)
    CreateObjectVFX(920204, obj=2401220, model_point=200)
    CreateObjectVFX(920205, obj=2401220, model_point=201)
    DisplayDialog(
        10010174,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    EnableFlag(12400160)
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    DisableFlag(2400)
    DisableFlag(2401)
    DisableFlag(2405)
    DisableFlag(2406)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisplayDialog(
        10010173,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


@RestartOnRest
def Event12400161():
    """ 12400161: Event 12400161 """
    DisableNetworkSync()
    IfFlagEnabled(1, 12400160)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2401014)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


@RestartOnRest
def Event12400174():
    """ 12400174: Event 12400174 """
    GotoIfFlagEnabled(Label.L0, 12400168)
    EnableFlag(12400167)

    # --- 0 --- #
    DefineLabel(0)


def Event12400175():
    """ 12400175: Event 12400175 """
    GotoIfFlagDisabled(Label.L0, 12400168)
    EndOfAnimation(2401209, 2)
    EnableFlag(12400169)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
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
    CreateObjectVFX(920204, obj=2401209, model_point=200)
    CreateObjectVFX(920205, obj=2401209, model_point=201)
    Wait(3.0)
    DisableFlag(12405175)
    EnableObjectActivation(2401015, obj_act_id=2400000)
    EnableObjectActivation(2401016, obj_act_id=2400000)

    # --- 1 --- #
    DefineLabel(1)
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
    CreateObjectVFX(920204, obj=2401209, model_point=200)
    CreateObjectVFX(920205, obj=2401209, model_point=201)
    Wait(3.0)
    DisableFlag(12400169)
    DisableFlag(12405175)
    EnableObjectActivation(2401015, obj_act_id=2400000)
    EnableObjectActivation(2401016, obj_act_id=2400000)
    Restart()


@RestartOnRest
def Event12400179(_, arg_0_3: int):
    """ 12400179: Event 12400179 """
    DisableNetworkSync()
    IfFlagEnabled(1, 12405175)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=0.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12400185():
    """ 12400185: Event 12400185 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(2401012, 1)
    DisableObjectActivation(2401013, obj_act_id=2400000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12400123)
    ForceAnimation(2401012, 1)


def Event12400200(_, arg_0_3: int, arg_4_7: int):
    """ 12400200: Event 12400200 """
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


def Event12400250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12400250: Event 12400250 """
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    DisplayDialog(
        arg_4_7,
        anchor_entity=arg_8_11,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )


def Event12400300():
    """ 12400300: Event 12400300 """
    GotoIfFlagEnabled(Label.L2, 9802)
    GotoIfFlagEnabled(Label.L1, 9801)
    GotoIfFlagEnabled(Label.L0, 9800)

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(2404000)
    DisableMapPiece(2404001)
    DisableMapPiece(2404002)
    DisableCharacter(2400321)
    DisableCharacter(2400322)
    DisableMapPiece(2404750)
    DisableMapPiece(2404751)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    DisableMapPiece(2404000)
    EnableMapPiece(2404001)
    DisableMapPiece(2404002)
    EnableCharacter(2400321)
    EnableCharacter(2400322)
    DisableBackread(2400350)
    DisableBackread(2400351)
    DisableBackread(2400352)
    DisableBackread(2400220)
    DisableBackread(2400116)
    DisableBackread(2400125)
    DisableMapPiece(2404700)
    DisableMapPiece(2404701)
    DeleteVFX(2403400, erase_root_only=False)
    DeleteVFX(2403401, erase_root_only=False)
    DeleteVFX(2403402, erase_root_only=False)
    DeleteVFX(2403403, erase_root_only=False)
    DeleteVFX(2403404, erase_root_only=False)
    DeleteVFX(2403405, erase_root_only=False)
    DeleteVFX(2403406, erase_root_only=False)
    DeleteVFX(2403407, erase_root_only=False)
    DeleteVFX(2403408, erase_root_only=False)
    DeleteVFX(2403409, erase_root_only=False)
    DeleteVFX(2403410, erase_root_only=False)
    DeleteVFX(2403411, erase_root_only=False)
    DeleteVFX(2403412, erase_root_only=False)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    DisableMapPiece(2404000)
    DisableMapPiece(2404001)
    EnableMapPiece(2404002)
    EnableCharacter(2400321)
    EnableCharacter(2400322)
    DisableBackread(2400350)
    DisableBackread(2400351)
    DisableBackread(2400352)
    DisableBackread(2400220)
    DisableBackread(2400116)
    DisableBackread(2400125)
    DisableMapPiece(2404700)
    DisableMapPiece(2404701)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagChange(-1, 9800)
    IfFlagChange(-1, 9801)
    IfFlagChange(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


def Event12400765():
    """ 12400765: Event 12400765 """
    IfFlagEnabled(-1, 9802)
    IfFlagEnabled(-1, 12404001)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    DisableObject(2400898)
    ForceAnimation(2400898, 0, loop=True)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.On)
    AddSpecialEffect(2400899, 5686, affect_npc_part_hp=False)
    EnableFlag(12405263)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableObject(2400898)
    ForceAnimation(2400898, 0, loop=True)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.Off)
    DisableFlag(12405263)


@RestartOnRest
def Event12400350(_, arg_0_3: int, arg_4_7: int):
    """ 12400350: Event 12400350 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=-1)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event12400401():
    """ 12400401: Event 12400401 """
    IfFlagEnabled(1, 72400440)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1400, 1402))
    EnableFlag(1401)
    ForceAnimation(2401200, 1, wait_for_completion=True)
    EnableFlag(12400131)
    SaveRequest()


def Event12400402():
    """ 12400402: Event 12400402 """
    IfFlagEnabled(1, 72400440)
    IfConditionTrue(0, input_condition=1)
    Move(2400830, destination=2402033, destination_type=CoordEntityType.Region, short_move=True)


def Event12400403():
    """ 12400403: Event 12400403 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 72400441)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(37000, host_only=False)


def Event12400410():
    """ 12400410: Event 12400410 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfCharacterHasSpecialEffect(0, PLAYER, 6421)
    RunEvent(9350, 0, args=(1,))


def Event12400420():
    """ 12400420: Event 12400420 """
    DisableSoundEvent(2406831)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 9801)
    Wait(4.0)
    EnableSoundEvent(2406831)


def Event12400750():
    """ 12400750: Event 12400750 """
    DisableSoundEvent(2406832)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfActionButtonParamActivated(0, action_button_id=7030, entity=2401210)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    PlayCutsceneAndMovePlayerAndSetTimePeriod(
        Cutscenes.CathedralWardFirstArrival, CutsceneFlags.Skippable, 2402200, CATHEDRAL_WARD, player_id=10000,
        time_period_id=1
    )
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    EnableSoundEvent(2406832)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(2401210, 2)
    NotifyDoorEventSoundDampening(2401210, state=DoorState.DoorOpening)


@RestartOnRest
def Event12400780(_, arg_0_3: int):
    """ 12400780: Event 12400780 """
    IfCharacterHuman(2, PLAYER)
    EndIfConditionFalse(2)
    IfCharacterAlive(1, arg_0_3)
    IfAttacked(1, PLAYER, attacker=arg_0_3)
    IfHealthEqual(1, PLAYER, 0.0)
    IfFlagEnabled(1, 9401)
    IfFlagEnabled(1, 9404)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9420)


@RestartOnRest
def Event12400791(_, arg_0_3: int):
    """ 12400791: Event 12400791 """
    GotoIfFlagEnabled(Label.L0, 9802)
    EndIfFlagEnabled(9453)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(arg_0_3)


@RestartOnRest
def Event12400797():
    """ 12400797: Event 12400797 """
    GotoIfFlagEnabled(Label.L0, 9802)
    SkipLinesIfFlagDisabled(4, 9453)
    DisableBackread(2400350)
    DisableBackread(2400351)
    DisableBackread(2400352)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2400362)


def Event12400823():
    """ 12400823: Event 12400823 """
    IfFlagEnabled(1, 12400827)
    IfFlagDisabled(2, 12400827)
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


def Event12400824():
    """ 12400824: Event 12400824 """
    IfFlagEnabled(3, 12400827)
    IfFlagEnabled(3, 12400828)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagEnabled(1, 12400827)
    IfFlagDisabled(1, 12400828)
    IfCharacterInsideRegion(1, PLAYER, region=2402058)
    IfFlagEnabled(2, 12400827)
    IfFlagDisabled(2, 12400828)
    IfObjectActivated(2, obj_act_id=12400169)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
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


def Event12400825():
    """ 12400825: Event 12400825 """
    IfFlagDisabled(3, 12400827)
    IfFlagEnabled(3, 12400828)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagDisabled(1, 12400827)
    IfFlagDisabled(1, 12400828)
    IfCharacterInsideRegion(1, PLAYER, region=2402059)
    IfFlagDisabled(2, 12400827)
    IfFlagDisabled(2, 12400828)
    IfObjectActivated(2, obj_act_id=12400168)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
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


def Event12400826():
    """ 12400826: Event 12400826 """
    DisableNetworkSync()
    IfFlagEnabled(1, 12400827)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2401104)
    IfFlagDisabled(2, 12400827)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=2401103)
    IfFlagEnabled(3, 12400828)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=2401104)
    IfFlagEnabled(4, 12400828)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=2401103)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


@RestartOnRest
def Event12400850(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: float,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 12400850: Event 12400850 """
    DeleteVFX(arg_0_3, erase_root_only=False)
    DeleteVFX(arg_4_7, erase_root_only=False)
    DeleteVFX(arg_8_11, erase_root_only=False)
    SkipLinesIfFlagDisabled(3, arg_12_15)
    CreateVFX(arg_4_7)
    CreateVFX(arg_8_11)
    End()
    IfObjectActivated(0, obj_act_id=arg_16_19)
    Wait(arg_20_23)
    CreateVFX(arg_0_3)
    CreateTemporaryVFX(arg_28_31, anchor_entity=arg_24_27, anchor_type=CoordEntityType.Region)
    Wait(4.0)
    CreateVFX(arg_4_7)
    CreateVFX(arg_8_11)


@RestartOnRest
def Event12400854():
    """ 12400854: Event 12400854 """
    DeleteVFX(2406711, erase_root_only=False)
    DeleteVFX(2406712, erase_root_only=False)
    DeleteVFX(2406713, erase_root_only=False)
    SkipLinesIfFlagDisabled(3, 12400133)
    CreateVFX(2406712)
    CreateVFX(2406713)
    End()
    IfObjectActivated(0, obj_act_id=12400112)
    Wait(6.0)
    CreateVFX(2406711)
    CreateTemporaryVFX(920206, anchor_entity=2401204, anchor_type=CoordEntityType.Object, model_point=200)
    CreateTemporaryVFX(920207, anchor_entity=2401204, anchor_type=CoordEntityType.Object, model_point=201)
    Wait(4.0)
    CreateVFX(2406712)
    CreateVFX(2406713)


@RestartOnRest
def Event12405000(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12405000: Event 12405000 """
    SetAIParamID(arg_0_3, arg_12_15)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfEntityWithinDistance(-1, PLAYER, arg_0_3, radius=3.0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_16_19)
    ForceAnimation(arg_0_3, arg_8_11, loop=True)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event12405010(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12405010: Event 12405010 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_12_15)
    ForceAnimation(arg_0_3, arg_4_7)
    StopEvent(12405000, slot=arg_8_11)


def Event12405020(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12405020: Event 12405020 """
    IfFlagEnabled(0, 9801)
    SetAIParamID(arg_0_3, arg_12_15)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfEntityWithinDistance(-1, PLAYER, arg_0_3, radius=1.0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_16_19)
    ForceAnimation(arg_0_3, arg_8_11, loop=True)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    Restart()


def Event12405030(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12405030: Event 12405030 """
    IfFlagEnabled(0, 9801)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_12_15)
    ForceAnimation(arg_0_3, arg_4_7)
    StopEvent(12405020, slot=arg_8_11)


@RestartOnRest
def Event12405060(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12405060: Event 12405060 """
    SetAIParamID(arg_0_3, arg_12_15)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=3.0)
    IfHasAIStatus(1, 2400160, ai_status=AIStatusType.Battle)
    IfAttacked(2, arg_0_3, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_16_19)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(arg_0_3, arg_8_11)


@RestartOnRest
def Event12405080(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float):
    """ 12405080: Event 12405080 """
    IfFlagEnabled(0, arg_0_3)
    AICommand(arg_4_7, command_id=10, slot=0)
    SetNest(arg_4_7, arg_8_11)
    IfCharacterInsideRegion(-1, arg_4_7, region=arg_8_11)
    IfEntityWithinDistance(-1, arg_4_7, PLAYER, radius=arg_12_15)
    IfAttacked(-1, arg_4_7, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event12405100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12405100: Event 12405100 """
    IfCharacterInsideRegion(1, PLAYER, region=2404306)
    IfFlagEnabled(2, 12405431)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfHasAIStatus(3, arg_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=3)
    DisableAI(arg_0_3)
    SkipLinesIfFinishedConditionTrue(1, 2)
    SetNest(arg_0_3, arg_4_7)
    SkipLinesIfFinishedConditionTrue(1, 1)
    SetNest(arg_0_3, arg_8_11)
    AICommand(arg_0_3, command_id=10, slot=0)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(-2, arg_0_3, region=arg_4_7)
    IfCharacterInsideRegion(-2, arg_0_3, region=arg_8_11)
    IfConditionTrue(0, input_condition=-2)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405110(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12405110: Event 12405110 """
    IfObjectNotDestroyed(0, arg_12_15)
    DisableFlag(arg_20_23)
    SkipLinesIfFlagDisabled(2, arg_20_23)
    EndOfAnimation(arg_4_7, 0)
    SkipLines(9)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_0_3)
    IfObjectNotDestroyed(1, arg_12_15)
    IfConditionTrue(1, input_condition=-1)
    IfObjectDestroyed(2, arg_12_15)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 2)
    SkipLinesIfFinishedConditionTrue(2, 1)
    ForceAnimation(arg_4_7, 0, wait_for_completion=True)
    End()
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(arg_4_7, 0, wait_for_completion=True)
    EnableFlag(arg_20_23)
    CreateTemporaryVFX(150005, anchor_entity=arg_4_7, anchor_type=CoordEntityType.Object, model_point=101)
    DeleteVFX(arg_8_11, erase_root_only=False)
    EndIfFinishedConditionTrue(2)
    Wait(0.20000000298023224)
    CreatePlayLog(arg_24_27)
    ShootProjectile(
        owner_entity=2400000,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5071,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    PlaySoundEffect(anchor_entity=arg_12_15, sound_type=SoundType.a_Ambient, sound_id=243007000)
    CreateTemporaryVFX(929208, anchor_entity=arg_12_15, anchor_type=CoordEntityType.Object, model_point=101)
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=2400000,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5071,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    PlaySoundEffect(anchor_entity=arg_12_15, sound_type=SoundType.a_Ambient, sound_id=243007000)
    CreateTemporaryVFX(929208, anchor_entity=arg_12_15, anchor_type=CoordEntityType.Object, model_point=101)
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=2400000,
        projectile_id=arg_12_15,
        model_point=101,
        behavior_id=5071,
        launch_angle_x=0,
        launch_angle_y=arg_16_19,
        launch_angle_z=0,
    )
    PlaySoundEffect(anchor_entity=arg_12_15, sound_type=SoundType.a_Ambient, sound_id=243007000)
    CreateTemporaryVFX(929208, anchor_entity=arg_12_15, anchor_type=CoordEntityType.Object, model_point=101)
    Wait(3.0)
    IfCharacterOutsideRegion(3, PLAYER, region=arg_0_3)
    IfObjectNotDestroyed(3, arg_12_15)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_20_23)
    PlaySoundEffect(anchor_entity=arg_12_15, sound_type=SoundType.a_Ambient, sound_id=243007001)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=990100001)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    Restart()


def Event12405120(_, arg_0_3: int, arg_4_7: int):
    """ 12405120: Event 12405120 """
    WaitFrames(1)
    AddSpecialEffect(arg_0_3, arg_4_7, affect_npc_part_hp=False)


@RestartOnRest
def Event12405130(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12405130: Event 12405130 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2402151)
    IfConditionTrue(0, input_condition=1)
    EnableAI(arg_0_3)
    StopEvent(arg_4_7, slot=arg_8_11)


@RestartOnRest
def Event12405140():
    """ 12405140: Event 12405140 """
    GotoIfThisEventFlagDisabled(Label.L0)
    SetAIParamID(2400111, 263381)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterBackreadEnabled(0, 2400111)
    DisableAI(2400111)
    IfFlagEnabled(1, 12405681)
    IfAttackedWithDamageType(2, attacked_entity=2400111, attacker=PLAYER)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfEntityWithinDistance(3, PLAYER, 2400111, radius=5.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2400111)
    EndIfFinishedConditionFalse(1)
    SetAIParamID(2400111, 263380)
    IfCharacterInsideRegion(-2, 2400111, region=2402046)
    IfAttackedWithDamageType(-2, attacked_entity=2400111, attacker=PLAYER)
    IfEntityWithinDistance(-2, PLAYER, 2400111, radius=5.0)
    IfConditionTrue(0, input_condition=-2)
    SetAIParamID(2400111, 263381)
    ReplanAI(2400111)


def Event12405150(_, arg_0_3: int, arg_4_7: int):
    """ 12405150: Event 12405150 """
    WaitFrames(10)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndIfFlagEnabled(1210)
    EnableBackread(2400756)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, arg_4_7)
    EnableBackread(2400756)
    EnableInvincibility(arg_0_3)
    IfCharacterBackreadEnabled(0, 2400756)
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionTrue(Label.L1, input_condition=15)
    WaitFrames(60)
    DisableBackread(arg_0_3)
    End()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(arg_0_3, 103073, wait_for_completion=True)
    DisableBackread(arg_0_3)
    Move(2400756, destination=2404507, model_point=-1, destination_type=CoordEntityType.Region)
    EnableGravity(2400756)
    ForceAnimation(2400756, 3030)
    EnableAI(2400756)
    SetNest(2400756, 2404507)
    DisableFlagRange((1200, 1219))
    EnableFlag(1207)
    EnableFlag(9432)
    SaveRequest()


def Event12405157():
    """ 12405157: Event 12405157 """
    IfCharacterHasSpecialEffect(-1, 2400755, 153)
    IfCharacterHasSpecialEffect(-1, 2400759, 153)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(0)


def Event12405158():
    """ 12405158: Event 12405158 """
    IfEventValueComparison(0, 72400372, bit_count=2, comparison_type=ComparisonType.NotEqual, value=0)
    WaitFrames(0)


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
    IfFlagEnabled(3, 12400169)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    ChangePatrolBehavior(2400203, patrol_information_id=2403111)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(2400203, patrol_information_id=2403112)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterInsideRegion(0, 2400203, region=2402412)
    IfCharacterInsideRegion(0, 2400203, region=2402407)
    IfFlagEnabled(4, 12400169)
    GotoIfConditionTrue(Label.L2, input_condition=4)
    ChangePatrolBehavior(2400203, patrol_information_id=2403110)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    ChangePatrolBehavior(2400203, patrol_information_id=2403113)

    # --- 3 --- #
    DefineLabel(3)
    Restart()


@RestartOnRest
def Event12405200():
    """ 12405200: Event 12405200 """
    IfFlagDisabled(0, 12400168)
    WaitFrames(1)
    ActivateObjectWithSpecificCharacter(2401015, objact_id=2400000, relative_index=-1, character=2400113)
    Restart()


@RestartOnRest
def Event12405210(_, arg_0_3: int, arg_4_7: int):
    """ 12405210: Event 12405210 """
    IfFlagDisabled(1, 12404002)
    EndIfConditionTrue(1)
    SetDisplayMask(arg_0_3, bit_index=3, switch_type=OnOffChange.On)
    SetDisplayMask(arg_0_3, bit_index=4, switch_type=OnOffChange.Off)
    AddSpecialEffect(arg_0_3, arg_4_7, affect_npc_part_hp=False)


@RestartOnRest
def Event12405220(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12405220: Event 12405220 """
    IfFlagDisabled(1, 12404002)
    EndIfConditionTrue(1)
    AddSpecialEffect(arg_0_3, arg_4_7, affect_npc_part_hp=False)
    AddSpecialEffect(arg_0_3, arg_8_11, affect_npc_part_hp=False)
    AddSpecialEffect(arg_0_3, arg_12_15, affect_npc_part_hp=False)


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
    IfFlagDisabled(5, 9801)
    IfConditionTrue(0, input_condition=5)
    PlaySoundEffect(anchor_entity=2404290, sound_type=SoundType.a_Ambient, sound_id=20011002)
    WaitFrames(40)
    EndIfFinishedConditionTrue(4)
    ForceAnimation(2400203, 3039)


@RestartOnRest
def Event12405241():
    """ 12405241: Event 12405241 """
    IfFlagEnabled(1, 12404003)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableBackread(2400650)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableBackread(2400650)


@RestartOnRest
def Event12405250(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12405250: Event 12405250 """
    IfFlagDisabled(1, arg_0_3)
    IfFlagEnabled(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisableNavmeshType(arg_4_7, NavmeshType.Solid)
    SkipLines(1)
    EnableNavmeshType(arg_4_7, NavmeshType.Solid)
    IfFlagEnabled(0, arg_8_11)
    Restart()


@RestartOnRest
def Event12405251(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12405251: Event 12405251 """
    IfFlagEnabled(1, arg_0_3)
    IfFlagDisabled(2, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    DisableNavmeshType(arg_4_7, NavmeshType.Solid)
    SkipLines(1)
    EnableNavmeshType(arg_4_7, NavmeshType.Solid)
    IfFlagEnabled(0, arg_8_11)
    Restart()


@RestartOnRest
def Event12405259():
    """ 12405259: Event 12405259 """
    DisableNetworkSync()
    IfCharacterHasTAEEvent(1, 2400899, tae_event_id=700)
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
    IfAttacked(0, PLAYER, attacker=2402018)
    Wait(3.0)
    ForceAnimation(PLAYER, 9580, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event12405262():
    """ 12405262: Event 12405262 """
    IfFlagEnabled(1, 12405263)
    IfCharacterHasTAEEvent(1, 2400899, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.Off)
    AddSpecialEffect(2400899, 5687, affect_npc_part_hp=False)
    RemoveSpecialEffect(2400899, 5686)
    IfCharacterHasTAEEvent(0, 2400899, tae_event_id=20)
    AddSpecialEffect(2400899, 5686, affect_npc_part_hp=False)
    RemoveSpecialEffect(2400899, 5687)
    Restart()


@RestartOnRest
def Event12405263():
    """ 12405263: Event 12405263 """
    IfCharacterHasTAEEvent(1, 2400899, tae_event_id=710)
    IfPlayerHasGood(1, 4311, including_box=False)
    IfConditionTrue(0, input_condition=1)
    EnableImmortality(PLAYER)
    WaitFrames(30)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    GotoIfMultiplayer(Label.L0)
    PlayCutscene(24000000, skippable=True, fade_out=False, player_id=PLAYER)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(24000000, skippable=False, fade_out=False, player_id=PLAYER)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EnableFlag(12401000)
    WarpPlayerToRespawnPoint(3402959)


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
def Event12405300(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12405300: Event 12405300 """
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_8_11)
    DisableFlag(arg_12_15)


@RestartOnRest
def Event12405320():
    """ 12405320: Event 12405320 """
    IfFlagEnabled(1, 12405300)
    IfFlagEnabled(2, 12405301)
    IfFlagEnabled(3, 12405302)
    IfFlagEnabled(4, 12405303)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    IfCharacterBackreadDisabled(0, 2400300)
    IfCharacterBackreadEnabled(0, 2400300)
    IfFlagEnabled(5, 12405300)
    IfFlagEnabled(6, 12405301)
    IfFlagEnabled(7, 12405302)
    IfFlagEnabled(8, 12405303)
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
def Event12405330(_, arg_0_3: int):
    """ 12405330: Event 12405330 """
    ForceAnimation(arg_0_3, 7000, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=4.0)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 7001)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405335():
    """ 12405335: Event 12405335 """
    IfCharacterBackreadEnabled(0, 2400421)
    DisableAI(2400421)
    IfCharacterInsideRegion(1, PLAYER, region=2402031)
    IfEntityWithinDistance(2, PLAYER, 2400421, radius=5.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(2400421, 3011)
    EnableAI(2400421)


@RestartOnRest
def Event12405350(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12405350: Event 12405350 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_16_19)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_8_11)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_12_15)
    EndIfThisEventSlotFlagEnabled()
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405360():
    """ 12405360: Event 12405360 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterBackreadEnabled(0, 2400371)
    AddSpecialEffect(2400371, 5000, affect_npc_part_hp=False)
    IfHasAIStatus(0, 2400371, ai_status=AIStatusType.Battle)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(2400371, 2404085)
    ChangePatrolBehavior(2400371, patrol_information_id=2403106)
    IfCharacterInsideRegion(0, 2400371, region=2404085)
    RemoveSpecialEffect(2400371, 5000)
    AICommand(2400371, command_id=-1, slot=0)
    ReplanAI(2400371)


@RestartOnRest
def Event12405365(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12405365: Event 12405365 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterBackreadEnabled(0, arg_0_3)
    AddSpecialEffect(arg_0_3, 5000, affect_npc_part_hp=False)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_4_7)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_8_11)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)
    RemoveSpecialEffect(arg_0_3, 5000)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405370(_, arg_0_3: int):
    """ 12405370: Event 12405370 """
    IfFlagEnabled(0, 9802)
    DisableBackread(arg_0_3)


def Event12405380(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12405380: Event 12405380 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetNest(arg_0_3, arg_4_7)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    SetNest(arg_0_3, arg_8_11)
    Restart()


def Event12400865(_, arg_0_3: int):
    """ 12400865: Event 12400865 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    Wait(0.0)


@RestartOnRest
def Event12405400(
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
    """ 12405400: Event 12405400 """
    IfFlagEnabled(0, arg_20_23)
    IfCharacterPartHealthLessThanOrEqual(1, arg_28_31, npc_part_id=arg_4_7, value=0)
    IfAttacked(1, arg_28_31, attacker=PLAYER)
    IfFlagEnabled(1, arg_24_27)
    IfHealthLessThanOrEqual(2, arg_28_31, 0.0)
    IfFlagEnabled(2, arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    SkipLinesIfFlagEnabled(2, arg_20_23)
    SetNPCPartHealth(arg_28_31, npc_part_id=arg_4_7, desired_health=1, overwrite_max=False)
    Restart()
    CreateNPCPart(
        arg_28_31,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(arg_28_31, npc_part_id=arg_4_7, material_sfx_id=65, material_vfx_id=65)
    ResetAnimation(arg_28_31, disable_interpolation=False)
    ForceAnimation(arg_28_31, arg_12_15)
    IfCharacterHasTAEEvent(0, arg_28_31, tae_event_id=400)
    AddSpecialEffect(arg_28_31, arg_16_19, affect_npc_part_hp=False)
    DisableFlag(arg_24_27)
    IfCharacterHasTAEEvent(0, arg_28_31, tae_event_id=300)
    SetNPCPartHealth(arg_28_31, npc_part_id=arg_4_7, desired_health=80, overwrite_max=True)
    SetNPCPartEffects(arg_28_31, npc_part_id=arg_4_7, material_sfx_id=64, material_vfx_id=64)
    RemoveSpecialEffect(arg_28_31, arg_16_19)
    AICommand(arg_28_31, command_id=-1, slot=0)
    ReplanAI(arg_28_31)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12405430(_, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12405430: Event 12405430 """
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


@RestartOnRest
def Event12405460(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar, arg_17_17: uchar):
    """ 12405460: Event 12405460 """
    SetCollisionMask(arg_12_15, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(arg_12_15, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    IfCharacterHasTAEEvent(0, arg_12_15, tae_event_id=arg_0_3)
    EnableFlag(arg_8_11)
    SetCollisionMask(arg_12_15, bit_index=arg_16_16, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_12_15, bit_index=arg_17_17, switch_type=OnOffChange.On)
    IfCharacterHasTAEEvent(0, arg_12_15, tae_event_id=arg_4_7)
    DisableFlag(arg_8_11)
    Restart()


@RestartOnRest
def Event12405790(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12405790: Event 12405790 """
    DeleteObjectVFX(arg_0_3, erase_root=True)
    EndIfFlagEnabled(arg_4_7)
    CreateObjectVFX(arg_8_11, obj=arg_0_3, model_point=200)


@RestartOnRest
def Event12405800(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12405800: Event 12405800 """
    DisableSoundEvent(arg_0_3)
    EndIfFlagEnabled(arg_12_15)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(arg_0_3)
    IfFlagEnabled(-1, arg_4_7)
    IfFlagEnabled(-1, arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(arg_0_3)
    Restart()


@RestartOnRest
def Event12405810(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12405810: Event 12405810 """
    EndIfFlagEnabled(arg_16_19)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_8_11)
    AICommand(arg_0_3, command_id=arg_12_15, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405820(_, arg_0_3: int, arg_4_7: int):
    """ 12405820: Event 12405820 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterInsideRegion(0, arg_0_3, region=arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405840(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12405840: Event 12405840 """
    EndIfFlagEnabled(arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(2, arg_8_11)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    IfHasAIStatus(3, arg_0_3, ai_status=AIStatusType.Normal)
    IfFlagEnabled(4, arg_8_11)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(4)
    AICommand(arg_0_3, command_id=arg_4_7, slot=0)
    ReplanAI(arg_0_3)
    Restart()


@RestartOnRest
def Event12405850(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12405850: Event 12405850 """
    EndIfFlagEnabled(arg_16_19)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, 7013, loop=True)
    IfObjectDestroyed(-1, arg_4_7)
    IfEntityWithinDistance(-1, PLAYER, arg_0_3, radius=4.0)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(0)
    ForceAnimation(arg_0_3, 7012)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_8_11)
    ForceAnimation(arg_0_3, 7011)
    ForceAnimation(arg_0_3, 7012)
    AICommand(arg_0_3, command_id=arg_12_15, slot=0)
    ReplanAI(arg_0_3)


def Event12400860():
    """ 12400860: Event 12400860 """
    GotoIfFlagDisabled(Label.L0, 12400861)
    DisableCharacter(2400450)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2400450)
    SkipLinesIfFlagEnabled(2, 6333)
    AwardItemLot(75002400, host_only=False)
    SkipLines(1)
    AwardItemLot(75002405, host_only=False)
    EnableFlag(12400861)


@RestartOnRest
def Event12405600(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 12405600: Event 12405600 """
    DisableAI(arg_0_3)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(2, input_condition=-2)
    IfAttacked(3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 2)
    SkipLinesIfFinishedConditionTrue(1, 3)
    Wait(arg_12_15)
    EnableAI(arg_0_3)
    WaitFrames(1)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405660():
    """ 12405660: Event 12405660 """
    DisableAI(2400114)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-3, PLAYER, region=2402082)
    IfEntityWithinDistance(-3, 2400114, PLAYER, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfCharacterInsideRegion(-1, 2400122, region=2404151)
    IfAttacked(-1, 2400114, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2400114)
    ReplanAI(2400114)


@RestartOnRest
def Event12405670(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: float):
    """ 12405670: Event 12405670 """
    DisableAI(arg_0_3)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(2, PLAYER, region=arg_8_11)
    IfConditionTrue(2, input_condition=-2)
    IfEntityWithinDistance(3, PLAYER, arg_0_3, radius=arg_12_15)
    IfConditionTrue(3, input_condition=-2)
    IfAttacked(4, arg_0_3, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    Wait(arg_16_19)
    EnableAI(arg_0_3)
    WaitFrames(1)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405675(_, arg_0_3: int):
    """ 12405675: Event 12405675 """
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=2404332)
    IfConditionTrue(-1, input_condition=1)
    IfAttacked(-1, arg_0_3, attacker=PLAYER)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=3.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    WaitFrames(1)
    ReplanAI(arg_0_3)


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
def Event12405682(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: float):
    """ 12405682: Event 12405682 """
    DisableAI(arg_0_3)
    DisableAnimations(arg_4_7)
    IfAttacked(1, arg_0_3, attacker=PLAYER)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-3)
    IfEntityWithinDistance(2, arg_0_3, PLAYER, radius=10.0)
    IfFlagEnabled(3, 12405681)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)
    SkipLinesIfFlagDisabled(24, 12405681)
    Wait(arg_8_11)
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=1.0)
    AICommand(arg_0_3, command_id=90, slot=0)
    ReplanAI(arg_0_3)
    IfEntityWithinDistance(4, arg_0_3, arg_4_7, radius=4.0)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterType(-4, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(5, input_condition=-4)
    IfEntityWithinDistance(5, arg_0_3, PLAYER, radius=3.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(9, 2)
    AddSpecialEffect(arg_0_3, 4662, affect_npc_part_hp=False)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(9, arg_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(7, arg_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(5, arg_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(3, arg_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(1, arg_12_15)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    Wait(arg_16_19)
    RemoveSpecialEffect(arg_0_3, 4662)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405686(_, arg_0_3: int):
    """ 12405686: Event 12405686 """
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(1)


@RestartOnRest
def Event12405690():
    """ 12405690: Event 12405690 """
    IfCharacterInsideRegion(0, 2400106, region=2404111)
    AddSpecialEffect(2400106, 5002, affect_npc_part_hp=False)
    IfCharacterInsideRegion(0, 2400106, region=2404113)
    WaitFrames(30)
    RemoveSpecialEffect(2400106, 5002)
    Restart()


def Event12400500():
    """ 12400500: Event 12400500 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L6, input_condition=15)
    GotoIfFlagDisabled(Label.L1, 1193)
    DisableFlagRange((1180, 1199))
    EnableFlag(1181)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(1, 1181)
    IfFlagEnabled(1, 9801)
    GotoIfConditionFalse(Label.L2, input_condition=1)
    DisableFlagRange((1180, 1199))
    EnableFlag(1185)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(2, 9467)
    IfFlagEnabled(2, 1185)
    GotoIfConditionFalse(Label.L3, input_condition=2)
    DisableFlagRange((1180, 1199))
    EnableFlag(1186)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(5, 1186)
    IfFlagEnabled(5, 72400900)
    GotoIfConditionFalse(Label.L9, input_condition=5)
    DisableFlagRange((1180, 1199))
    EnableFlag(1187)

    # --- 9 --- #
    DefineLabel(9)
    IfFlagEnabled(3, 1187)
    IfFlagEnabled(3, 72400919)
    GotoIfConditionFalse(Label.L4, input_condition=3)
    SkipLinesIfFlagEnabled(2, 72400918)
    EnableFlag(72400918)
    Goto(Label.L4)
    DisableFlagRange((1180, 1199))
    EnableFlag(1188)

    # --- 4 --- #
    DefineLabel(4)
    IfFlagEnabled(4, 1188)
    IfFlagEnabled(4, 72400350)
    GotoIfConditionFalse(Label.L5, input_condition=4)
    DisableFlagRange((1180, 1199))
    EnableFlag(1189)

    # --- 5 --- #
    DefineLabel(5)
    DisableFlag(72400348)
    DisableFlag(72400356)

    # --- 6 --- #
    DefineLabel(6)
    DisableGravity(2400730)
    DisableCharacterCollision(2400730)
    DisableGravity(2400732)
    DisableCharacterCollision(2400732)
    GotoIfFlagEnabled(Label.L0, 1181)
    GotoIfFlagEnabled(Label.L0, 1184)
    GotoIfFlagEnabled(Label.L5, 1185)
    GotoIfFlagEnabled(Label.L0, 1186)
    GotoIfFlagEnabled(Label.L0, 1188)
    GotoIfFlagEnabled(Label.L1, 1191)
    GotoIfFlagEnabled(Label.L2, 1189)
    GotoIfFlagEnabled(Label.L3, 1183)
    GotoIfFlagEnabled(Label.L4, 1189)
    GotoIfFlagEnabled(Label.L4, 1187)
    DisableBackread(2400730)
    DisableBackread(2400732)
    DisableObject(2400731)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    ForceAnimation(2400730, 103060, loop=True, skip_transition=True)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 5 --- #
    DefineLabel(5)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    ForceAnimation(2400730, 103066, loop=True, skip_transition=True)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    EzstateAIRequest(2400730, command_id=3, slot=1)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400730)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableBackread(2400730)
    EnableBackread(2400732)
    EnableObject(2400731)
    PostDestruction(2400731)
    EzstateAIRequest(2400732, command_id=10, slot=1)
    Move(2400732, destination=2404382, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400732)
    End()

    # --- 3 --- #
    DefineLabel(3)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    EzstateAIRequest(2400730, command_id=3, slot=1)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400730)
    End()

    # --- 4 --- #
    DefineLabel(4)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    PostDestruction(2400731)
    End()


def Event12400501():
    """ 12400501: Event 12400501 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1183)
    EndIfFlagEnabled(1189)
    EndIfFlagEnabled(1191)
    IfCharacterDead(1, 2400730)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1180, 1199))
    EnableFlag(1183)
    SaveRequest()


def Event12400505():
    """ 12400505: Event 12400505 """
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, 1191)
    DisableMapPiece(2404602)
    IfFlagEnabled(0, 6001)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(2404602)
    End()


def Event12400507():
    """ 12400507: Event 12400507 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2400730, attacker=-1)
    IfHealthNotEqual(1, 2400730, 0.0)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagEnabled(Label.L0, 1185)
    ForceAnimation(2400730, 103063)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2400730, 103067)
    Restart()


def Event12400508():
    """ 12400508: Event 12400508 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, 2400730, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400730, 103064)


def Event12400512():
    """ 12400512: Event 12400512 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(-1, 2400730, 151)
    IfCharacterHasSpecialEffect(-1, 2400730, 153)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, 2400730, 0.0)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagEnabled(Label.L0, 1185)
    GotoIfFlagEnabled(Label.L1, 9432)
    ForceAnimation(2400730, 103060)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(2400730, 103061)
    Goto(Label.L9)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2400730, 103066)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    WaitFrames(5)
    Restart()


def Event12400513():
    """ 12400513: Event 12400513 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 9432)
    IfFlagEnabled(-1, 1181)
    IfFlagEnabled(-1, 1184)
    IfFlagEnabled(-1, 1186)
    IfFlagEnabled(-1, 1187)
    IfFlagEnabled(-1, 1188)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400730, 103061)
    IfFlagDisabled(0, 9432)
    ForceAnimation(2400730, 103060)
    Restart()


def Event12400514():
    """ 12400514: Event 12400514 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, 1187)
    GotoIfFlagEnabled(Label.L1, 1189)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfActionButtonParamActivated(0, action_button_id=2400020, entity=2400731)
    DisplayDialog(
        14001000,
        anchor_entity=2400731,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    EnableFlag(72400919)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    IfActionButtonParamActivated(0, action_button_id=2400020, entity=2400731)
    DisplayDialog(
        14001001,
        anchor_entity=2400731,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12400520():
    """ 12400520: Event 12400520 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L7, input_condition=15)
    IfFlagEnabled(1, 1232)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableFlagRange((1220, 1239))
    EnableFlag(1224)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(2, 1233)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    DisableFlagRange((1220, 1239))
    EnableFlag(1223)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 9802)
    IfFlagEnabled(3, 1224)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1220, 1239))
    EnableFlag(1225)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(4, 1225)
    IfFlagEnabled(4, 9464)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableFlagRange((1220, 1239))
    EnableFlag(1226)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(5, 1226)
    IfFlagEnabled(5, 9461)
    GotoIfConditionFalse(Label.L5, input_condition=5)
    DisableFlagRange((1220, 1239))
    EnableFlag(1228)

    # --- 5 --- #
    DefineLabel(5)
    IfFlagEnabled(7, 1220)
    IfFlagEnabled(7, 9802)
    GotoIfConditionFalse(Label.L6, input_condition=7)
    DisableFlagRange((1220, 1239))
    EnableFlag(1234)

    # --- 6 --- #
    DefineLabel(6)

    # --- 7 --- #
    DefineLabel(7)
    DisableGravity(2400750)
    DisableCharacterCollision(2400750)
    DisableGravity(2400754)
    DisableCharacterCollision(2400754)
    DisableGravity(2400757)
    DisableCharacterCollision(2400757)
    GotoIfFlagEnabled(Label.L0, 1220)
    GotoIfFlagEnabled(Label.L1, 1224)
    GotoIfFlagEnabled(Label.L2, 1225)
    GotoIfFlagEnabled(Label.L3, 1226)
    GotoIfFlagEnabled(Label.L4, 1228)
    GotoIfFlagEnabled(Label.L4, 1229)
    GotoIfFlagEnabled(Label.L4, 1235)
    GotoIfFlagEnabled(Label.L5, 1222)
    GotoIfFlagEnabled(Label.L5, 1230)
    GotoIfFlagEnabled(Label.L6, 1231)
    DisableObject(2400748)
    DisableMapPiece(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(2400748)
    DisableMapPiece(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2400748)
    DisableMapPiece(2404601)
    EnableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400750, 103080)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2400748)
    DisableMapPiece(2404601)
    DisableBackread(2400750)
    EnableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400754, 103081)
    Move(2400754, destination=2404504, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2400748)
    DisableMapPiece(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    EnableBackread(2400757)
    ForceAnimation(2400757, 103081)
    Move(2400757, destination=2404504, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2400748)
    EnableMapPiece(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2400748)
    DisableMapPiece(2404601)
    EnableBackread(2400750)
    EnableCharacter(2400750)
    DisableBackread(2400754)
    DisableCharacter(2400754)
    DisableBackread(2400757)
    DisableCharacter(2400757)
    EzstateAIRequest(2400750, command_id=5, slot=1)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400750)
    End()

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2400748)
    DisableMapPiece(2404601)
    DisableBackread(2400750)
    DisableCharacter(2400750)
    DisableBackread(2400754)
    DisableCharacter(2400754)
    DisableBackread(2400757)
    DisableCharacter(2400757)
    DropMandatoryTreasure(2400750)
    End()


def Event12400521():
    """ 12400521: Event 12400521 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1222)
    EndIfFlagEnabled(1230)
    EndIfFlagEnabled(1231)
    IfCharacterDead(-1, 2400750)
    IfCharacterDead(-1, 2400754)
    IfCharacterDead(-1, 2400757)
    IfCharacterDead(-1, 2400758)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1220, 1239))
    EnableFlag(1222)
    SaveRequest()


def Event12400522():
    """ 12400522: Event 12400522 """
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, 1230)
    GotoIfFlagEnabled(Label.L0, 1231)
    DisableMapPiece(2404600)
    IfFlagEnabled(0, 6001)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(2404600)
    End()


def Event12400523():
    """ 12400523: Event 12400523 """
    IfFlagEnabled(0, 72400510)
    DisableFlag(72400510)
    DisableFlagRange((1220, 1239))
    EnableFlag(1232)


def Event12400524():
    """ 12400524: Event 12400524 """
    IfFlagEnabled(0, 72400511)
    DisableFlag(72400511)
    DisableFlagRange((1220, 1239))
    EnableFlag(1233)


def Event12400525():
    """ 12400525: Event 12400525 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 72400499)
    DisableFlag(72400499)
    GotoIfFlagDisabled(Label.L0, 72400950)
    GotoIfFlagDisabled(Label.L1, 72400951)
    GotoIfFlagDisabled(Label.L2, 72400952)
    GotoIfFlagDisabled(Label.L3, 72400953)
    GotoIfFlagDisabled(Label.L4, 72400954)

    # --- 4 --- #
    DefineLabel(4)
    EnableFlag(72400954)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(72400953)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(72400952)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(72400951)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(72400950)
    IfFlagEnabled(-1, 1304)
    IfFlagEnabled(-1, 1305)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFlagDisabled(Label.L5, 72400940)
    GotoIfFlagDisabled(Label.L6, 72400941)
    GotoIfFlagDisabled(Label.L7, 72400942)
    GotoIfFlagDisabled(Label.L8, 72400943)
    GotoIfFlagDisabled(Label.L9, 72400944)

    # --- 9 --- #
    DefineLabel(9)
    EnableFlag(72400944)

    # --- 8 --- #
    DefineLabel(8)
    EnableFlag(72400943)

    # --- 7 --- #
    DefineLabel(7)
    EnableFlag(72400942)

    # --- 6 --- #
    DefineLabel(6)
    EnableFlag(72400941)

    # --- 5 --- #
    DefineLabel(5)
    EnableFlag(72400940)


def Event12400531():
    """ 12400531: Event 12400531 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerHasGood(1, 701, including_box=False)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableFlag(72400498)
    End()

    # --- 0 --- #
    DefineLabel(0)
    End()


def Event12400560():
    """ 12400560: Event 12400560 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L3, input_condition=15)
    IfFlagEnabled(1, 1168)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableFlagRange((1160, 1179))
    EnableFlag(1164)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(2, 1169)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    DisableFlagRange((1160, 1179))
    EnableFlag(1163)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 9802)
    IfFlagEnabled(3, 1164)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1160, 1179))
    EnableFlag(1165)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(4, 1160)
    IfFlagEnabled(4, 9802)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableFlagRange((1160, 1179))
    EnableFlag(1170)

    # --- 3 --- #
    DefineLabel(3)
    DisableGravity(2400765)
    DisableCharacterCollision(2400765)
    GotoIfFlagEnabled(Label.L4, 1161)
    GotoIfFlagEnabled(Label.L1, 1164)
    GotoIfFlagEnabled(Label.L1, 1165)
    GotoIfFlagEnabled(Label.L3, 1166)
    GotoIfFlagEnabled(Label.L2, 1167)
    DisableBackread(2400765)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(2400765)
    ForceAnimation(2400765, 103050)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableBackread(2400765)
    EzstateAIRequest(2400765, command_id=2, slot=1)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400765)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableBackread(2400765)
    EzstateAIRequest(2400765, command_id=2, slot=1)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400765)
    End()


def Event12400561():
    """ 12400561: Event 12400561 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1161)
    EndIfFlagEnabled(1166)
    IfCharacterDead(1, 2400765)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1160, 1179))
    EnableFlag(1161)
    SaveRequest()


def Event12400563():
    """ 12400563: Event 12400563 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, 72400330)
    IfFlagEnabled(-1, 1304)
    IfFlagEnabled(-1, 1305)
    IfFlagEnabled(-1, 1306)
    IfFlagEnabled(-1, 1307)
    IfFlagEnabled(-1, 1308)
    IfFlagEnabled(-2, 1224)
    IfFlagEnabled(-2, 1225)
    IfFlagEnabled(-2, 1226)
    IfFlagEnabled(-2, 1227)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(72400330)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-3, 1312)
    IfFlagEnabled(-3, 1303)
    IfFlagEnabled(-3, 1317)
    IfFlagEnabled(-4, 1228)
    IfFlagEnabled(-4, 1229)
    IfFlagEnabled(-4, 1235)
    IfFlagEnabled(-4, 1236)
    IfFlagEnabled(-4, 1230)
    IfFlagEnabled(-4, 1231)
    IfFlagEnabled(-4, 1222)
    IfConditionTrue(-5, input_condition=-3)
    IfConditionTrue(-5, input_condition=-4)
    IfConditionTrue(0, input_condition=-5)
    DisableFlag(72400330)


def Event12400564():
    """ 12400564: Event 12400564 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, 72400331)
    IfFlagEnabled(1, 1188)
    IfFlagEnabled(1, 1164)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(72400331)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-1, 1189)
    IfFlagEnabled(-1, 1191)
    IfFlagEnabled(-1, 1183)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(72400331)


def Event12400565():
    """ 12400565: Event 12400565 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, 72400332)
    IfFlagEnabled(-1, 1100)
    IfFlagEnabled(-1, 1101)
    IfFlagEnabled(-1, 1102)
    IfFlagEnabled(-1, 1103)
    IfFlagEnabled(-1, 1104)
    IfFlagEnabled(-1, 1105)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400332)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-2, 1108)
    IfFlagEnabled(-2, 1106)
    IfConditionTrue(0, input_condition=-2)
    DisableFlag(72400332)


def Event12400566():
    """ 12400566: Event 12400566 """
    IfFlagEnabled(0, 72400970)
    DisableFlag(72400970)
    DisableFlagRange((1160, 1179))
    EnableFlag(1168)
    Restart()


def Event12400567():
    """ 12400567: Event 12400567 """
    IfFlagEnabled(0, 72400971)
    DisableFlag(72400971)
    DisableFlagRange((1160, 1179))
    EnableFlag(1169)
    Restart()


def Event12400568():
    """ 12400568: Event 12400568 """
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, 1166)
    DisableMapPiece(2404603)
    IfFlagEnabled(0, 6001)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(2404603)
    End()


def Event12400569():
    """ 12400569: Event 12400569 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1161)
    EndIfFlagEnabled(1166)
    IfHealthEqual(1, 2400765, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400765, 103053)


def Event12400570():
    """ 12400570: Event 12400570 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2400765, attacker=-1)
    IfHealthNotEqual(1, 2400765, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400765, 103052)
    Restart()


def Event12400571():
    """ 12400571: Event 12400571 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2400765, 151)
    IfHealthNotEqual(1, 2400765, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, 9432)
    IfFlagDisabled(2, 1165)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    ForceAnimation(2400765, 103050)
    Goto(Label.L9)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2400765, 103051)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    WaitFrames(5)
    Restart()


def Event12400572():
    """ 12400572: Event 12400572 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 9432)
    IfFlagDisabled(1, 1165)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400765, 103051)
    IfFlagDisabled(0, 9432)
    ForceAnimation(2400765, 103050)
    Restart()


def Event12400580():
    """ 12400580: Event 12400580 """
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(1, PLAYER, region=2402280)
    IfFlagEnabled(2, 72400400)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    EnableSoundEvent(2403300)


def Event12400581():
    """ 12400581: Event 12400581 """
    IfFlagEnabled(0, 72400400)
    DisableSoundEvent(2403300)


def Event12400582():
    """ 12400582: Event 12400582 """
    EnableMapPiece(2404010)
    IfFlagEnabled(0, Flags.VicarAmeliaFirstTimeDone)
    DisableMapPiece(2404010)


def Event12400590():
    """ 12400590: Event 12400590 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    IfFlagEnabled(1, 1340)
    IfFlagEnabled(1, 9801)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1340, 1359))
    EnableFlag(1344)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(2, 1351)
    IfFlagEnabled(2, 72500359)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    DisableFlagRange((1340, 1359))
    EnableFlag(1343)

    # --- 2 --- #
    DefineLabel(2)
    DisableFlag(72400471)

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(2400762)
    DisableCharacterCollision(2400762)
    GotoIfFlagEnabled(Label.L0, 1340)
    GotoIfFlagEnabled(Label.L1, 1341)
    GotoIfFlagEnabled(Label.L2, 1342)
    GotoIfFlagEnabled(Label.L3, 1343)
    GotoIfFlagEnabled(Label.L4, 1344)
    GotoIfFlagEnabled(Label.L5, 1345)
    GotoIfFlagEnabled(Label.L6, 1346)
    GotoIfFlagEnabled(Label.L4, 1347)
    DisableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    GotoIfFlagEnabled(Label.L7, 12405160)
    ForceAnimation(2400760, 103020, loop=True, skip_transition=True)
    End()

    # --- 7 --- #
    DefineLabel(7)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    SetTeamType(2400760, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    DisableCharacter(2400760)
    DropMandatoryTreasure(2400760)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableBackread(2400760)
    EnableBackread(2400762)
    DisableBackread(2400763)
    EnableObject(2400761)
    Move(2400762, destination=2404508, destination_type=CoordEntityType.Region, short_move=True)
    EzstateAIRequest(2400762, command_id=11, slot=1)
    DropMandatoryTreasure(2400762)
    End()

    # --- 4 --- #
    DefineLabel(4)
    DisableBackread(2400760)
    DisableBackread(2400762)
    EnableBackread(2400763)
    DisableObject(2400761)
    SetTeamType(2400763, TeamType.FriendlyNPC)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableBackread(2400760)
    DisableBackread(2400762)
    EnableBackread(2400763)
    DisableObject(2400761)
    SetTeamType(2400763, TeamType.HostileNPC)
    End()

    # --- 6 --- #
    DefineLabel(6)
    DisableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    DisableCharacter(2400763)
    DropMandatoryTreasure(2400763)
    End()


def Event12400591():
    """ 12400591: Event 12400591 """
    IfFlagEnabled(0, 72400465)
    DisableFlag(72400465)
    DisableFlagRange((1340, 1359))
    EnableFlag(1347)
    SaveRequest()


def Event12400592(_, arg_0_3: int, arg_4_7: int):
    """ 12400592: Event 12400592 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(arg_4_7)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    EnableFlag(arg_4_7)


def Event12400593(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12400593: Event 12400593 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(-1, arg_8_11)
    IfHealthLessThanOrEqual(-1, arg_0_3, 0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    DisableFlagRange((1340, 1359))
    EnableFlag(arg_4_7)
    SaveRequest()


def Event12400594(_, arg_0_3: int, arg_4_7: int):
    """ 12400594: Event 12400594 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(0, arg_0_3)
    DisableFlagRange((1340, 1359))
    EnableFlag(arg_4_7)
    SaveRequest()


def Event12400610():
    """ 12400610: Event 12400610 """
    DisableFlag(72400362)
    DisableFlag(72400921)
    DisableFlag(72400924)
    DisableGravity(2400756)
    ForceAnimation(2400756, 7002, loop=True)
    DisableAI(2400756)
    DisableBackread(2400756)
    GotoIfFlagEnabled(Label.L0, 1205)
    GotoIfFlagEnabled(Label.L1, 1206)
    GotoIfFlagEnabled(Label.L1, 1207)
    GotoIfFlagEnabled(Label.L3, 1210)
    DisableBackread(2400755)
    DisableBackread(2400759)
    EnableBackread(2400220)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfEventValueComparison(-1, 72400372, bit_count=2, comparison_type=ComparisonType.NotEqual, value=0)
    IfFlagEnabled(-1, 12405158)
    GotoIfConditionTrue(Label.L2, input_condition=-1)
    DisableBackread(2400755)
    EnableBackread(2400759)
    DisableBackread(2400220)
    GotoIfFlagEnabled(Label.L5, 12405157)
    ForceAnimation(2400759, 103074)
    End()

    # --- 5 --- #
    DefineLabel(5)
    ForceAnimation(2400759, 103072)
    End()

    # --- 2 --- #
    DefineLabel(2)
    EnableBackread(2400755)
    DisableBackread(2400759)
    DisableBackread(2400220)
    GotoIfFlagEnabled(Label.L4, 12405157)
    ForceAnimation(2400755, 103074)
    End()

    # --- 4 --- #
    DefineLabel(4)
    ForceAnimation(2400755, 103072)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(2400755)
    DisableBackread(2400759)
    DisableBackread(2400220)
    ForceAnimation(2400755, 103072)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableBackread(2400755)
    DisableCharacter(2400755)
    DisableBackread(2400759)
    DisableCharacter(2400759)
    DisableBackread(2400220)
    DisableCharacter(2400220)
    DropMandatoryTreasure(2400755)
    End()


def Event12400611():
    """ 12400611: Event 12400611 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1210)
    IfCharacterDead(-1, 2400755)
    IfCharacterDead(-1, 2400756)
    IfCharacterDead(-1, 2400759)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((1200, 1219))
    EnableFlag(1210)
    IfCharacterDead(1, 2400756)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableFlag(9432)

    # --- 0 --- #
    DefineLabel(0)
    SaveRequest()


def Event12400612(_, arg_0_3: int, arg_4_7: int):
    """ 12400612: Event 12400612 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthLessThan(1, arg_0_3, 0.5)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_4_7)


def Event12400614(_, arg_0_3: int, arg_4_7: int):
    """ 12400614: Event 12400614 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, arg_0_3, 0.0)
    IfCharacterHasSpecialEffect(1, arg_0_3, 155)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, arg_4_7)


def Event12400616(_, arg_0_3: int):
    """ 12400616: Event 12400616 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfHealthGreaterThan(1, arg_0_3, 0.5)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 153)
    GotoIfConditionTrue(Label.L0, input_condition=-2)
    IfCharacterHasSpecialEffect(-3, arg_0_3, 155)
    GotoIfConditionTrue(Label.L1, input_condition=-3)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 103079)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(arg_0_3, 103130)
    Restart()


def Event12400618(_, arg_0_3: int):
    """ 12400618: Event 12400618 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, arg_0_3, 154)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 103072)
    Restart()


def Event12400620(_, arg_0_3: int):
    """ 12400620: Event 12400620 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, arg_0_3, 156)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 103072)


def Event12400622():
    """ 12400622: Event 12400622 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 1208)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1200, 1219))
    EnableFlag(1205)


def Event12400623():
    """ 12400623: Event 12400623 """
    EndIfClient()
    IfFlagEnabled(1, 1209)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1200, 1219))
    EnableFlag(1204)


def Event12400624():
    """ 12400624: Event 12400624 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagDisabled(1205)
    IfFlagEnabled(-1, 1106)
    IfFlagEnabled(-1, 1108)
    IfFlagEnabled(-2, 1222)
    IfFlagEnabled(-2, 1223)
    IfFlagEnabled(-2, 1230)
    IfFlagEnabled(-2, 1231)
    IfFlagEnabled(-2, 1235)
    IfFlagEnabled(-2, 1228)
    IfFlagEnabled(-2, 1229)
    IfFlagEnabled(-2, 1234)
    IfFlagEnabled(-3, 1303)
    IfFlagEnabled(-3, 1308)
    IfFlagEnabled(-3, 1309)
    IfFlagEnabled(-3, 1315)
    IfFlagEnabled(-3, 1310)
    IfFlagEnabled(-3, 1312)
    IfFlagEnabled(-3, 1316)
    IfFlagEnabled(-4, 1163)
    IfFlagEnabled(-4, 1161)
    IfFlagEnabled(-4, 1166)
    IfFlagEnabled(-4, 1170)
    IfFlagEnabled(-5, 1183)
    IfFlagEnabled(-5, 1190)
    IfFlagEnabled(-5, 1189)
    IfFlagEnabled(-5, 1191)
    IfFlagEnabled(-5, 1195)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(1, input_condition=-4)
    IfConditionTrue(1, input_condition=-5)
    IfFlagDisabled(1, 72400934)
    IfFlagDisabled(1, 72400935)
    IfFlagDisabled(1, 72400936)
    IfFlagDisabled(1, 72400937)
    IfFlagDisabled(1, 72400938)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1200, 1219))
    EnableFlag(1211)


def Event12400625(_, arg_0_3: int, arg_4_7: int):
    """ 12400625: Event 12400625 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagDisabled(1207)
    WaitFrames(30)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=2404383)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 1207)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_4_7)


def Event12400627(_, arg_0_3: int, arg_4_7: int):
    """ 12400627: Event 12400627 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(1)
    IfAttackedWithDamageType(3, attacked_entity=arg_0_3, attacker=PLAYER)
    IfHealthNotEqual(3, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=3)
    EnableFlag(arg_4_7)


def Event12400629():
    """ 12400629: Event 12400629 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(-1, 1208)
    IfFlagEnabled(-1, 1205)
    IfFlagEnabled(-1, 1207)
    GotoIfConditionFalse(Label.L6, input_condition=-1)
    GotoIfFlagEnabled(Label.L0, 1208)
    GotoIfFlagDisabled(Label.L5, 72400360)
    GotoIfFlagRangeState(Label.L5, RangeState.AllOff, FlagType.Absolute, (70000200, 70000202))

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-2, 1164)
    IfFlagEnabled(-2, 1165)
    GotoIfConditionFalse(Label.L1, input_condition=-2)
    DisableFlagRange((1160, 1179))
    EnableFlag(1166)
    EnableFlag(72400934)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(-3, 1181)
    IfFlagEnabled(-3, 1184)
    IfFlagEnabled(-3, 1185)
    IfFlagEnabled(-3, 1186)
    IfFlagEnabled(-3, 1187)
    IfFlagEnabled(-3, 1188)
    GotoIfConditionFalse(Label.L2, input_condition=-3)
    DisableFlagRange((1180, 1199))
    EnableFlag(1191)
    EnableFlag(72400935)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(-4, 1304)
    IfFlagEnabled(-4, 1305)
    IfFlagEnabled(-4, 1306)
    IfFlagEnabled(-4, 1307)
    GotoIfConditionFalse(Label.L3, input_condition=-4)
    DisableFlagRange((1300, 1319))
    EnableFlag(1312)
    EnableFlag(72400936)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(-5, 1100)
    IfFlagEnabled(-5, 1101)
    IfFlagEnabled(-5, 1102)
    IfFlagEnabled(-5, 1103)
    IfFlagEnabled(-5, 1104)
    IfFlagEnabled(-5, 1105)
    GotoIfConditionFalse(Label.L4, input_condition=-5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1108)
    EnableFlag(72400937)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    IfFlagEnabled(-6, 1224)
    IfFlagEnabled(-6, 1225)
    IfFlagEnabled(-6, 1226)
    IfFlagEnabled(-6, 1228)
    IfFlagEnabled(-6, 1229)
    GotoIfConditionFalse(Label.L5, input_condition=-6)
    DisableFlagRange((1220, 1239))
    EnableFlag(1231)
    EnableFlag(72400938)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    IncrementEventValue(72400375, bit_count=3, max_value=7)
    IncrementEventValue(72400372, bit_count=2, max_value=2)
    EnableFlag(72400490)
    GotoIfFlagEnabled(Label.L5, 1208)
    EventValueOperation(70000200, 3, 1, 0, 1, CalculationType.Subtract)

    # --- 5 --- #
    DefineLabel(5)
    End()


def Event12400630(_, arg_0_3: int):
    """ 12400630: Event 12400630 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    IfHealthEqual(1, arg_0_3, 0.0)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(0, arg_0_3)
    EnableFlag(9432)
    EnableFlag(72400490)


def Event12400650():
    """ 12400650: Event 12400650 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    IfFlagEnabled(1, 1362)
    IfFlagEnabled(1, 72400520)
    SkipLinesIfConditionFalse(2, 1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1363)
    IfFlagEnabled(2, 72400524)
    SkipLinesIfConditionFalse(3, 2)
    DisableFlagRange((1360, 1379))
    EnableFlag(1368)
    EnableFlag(1376)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1373, 1375))
    GotoIfFlagEnabled(Label.L1, 1372)
    GotoIfFlagEnabled(Label.L2, 1371)
    GotoIfFlagEnabled(Label.L3, 1370)
    GotoIfFlagEnabled(Label.L4, 1369)
    GotoIfFlagEnabled(Label.L5, 1368)
    GotoIfFlagRangeState(Label.L6, RangeState.AnyOn, FlagType.Absolute, (1365, 1367))
    GotoIfFlagRangeState(Label.L7, RangeState.AnyOn, FlagType.Absolute, (1362, 1364))
    GotoIfFlagRangeState(Label.L8, RangeState.AnyOn, FlagType.Absolute, (1360, 1361))

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    DisableBackread(2400900)
    EnableBackread(2400902)
    SetTeamType(2400902, TeamType.HostileNPC)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    DisableBackread(2400900)
    DisableBackread(2400902)
    EnableBackread(2400903)
    ForceAnimation(2400903, 103031, loop=True)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    DisableBackread(2400900)
    DisableBackread(2400902)
    EnableBackread(2400903)
    ForceAnimation(2400903, 103031, loop=True)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    SkipLinesIfFlagDisabled(5, 1705)
    DisableBackread(2400900)
    EnableBackread(2400902)
    SetTeamType(2400902, TeamType.HostileNPC)
    DisableBackread(2400903)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(5, 1704)
    DisableBackread(2400900)
    DisableBackread(2400902)
    EnableBackread(2400903)
    SetTeamType(2400903, TeamType.HostileNPC)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(5, 1701)
    EnableBackread(2400900)
    SetTeamType(2400900, TeamType.HostileNPC)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(5, 1703)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(4, 1702)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    DisableBackread(2400900)
    DisableCharacter(2400900)
    DisableBackread(2400902)
    DisableCharacter(2400902)
    DisableBackread(2400903)
    DisableCharacter(2400903)
    SkipLinesIfFlagDisabled(2, 1705)
    DropMandatoryTreasure(2400902)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 1704)
    DropMandatoryTreasure(2400903)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 1701)
    DropMandatoryTreasure(2400900)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(1, 1703)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(1, 1702)
    Goto(Label.L9)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    EnableBackread(2400900)
    ForceAnimation(2400900, 103030, loop=True)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    Event12400651()
    Event12400652()
    Event12400653()
    Event12400654()
    Event12400655()
    Event12400657()
    Event12400658()
    Event12400659()
    Event12400660()
    Event12400661()
    Event12400662()
    Event12400663()
    Event12400665()


def Event12400651():
    """ 12400651: Event 12400651 """
    IfFlagEnabled(1, 1360)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2404390)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1362)
    EnableBackread(2400900)
    ForceAnimation(2400900, 103030, loop=True)
    DisableBackread(2400902)
    DisableBackread(2400903)


def Event12400652():
    """ 12400652: Event 12400652 """
    IfFlagEnabled(1, 1361)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2404390)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1363)
    EnableBackread(2400900)
    ForceAnimation(2400900, 103030, loop=True)
    DisableBackread(2400902)
    DisableBackread(2400903)


def Event12400653():
    """ 12400653: Event 12400653 """
    EndIfThisEventFlagEnabled()
    DisableMapPiece(2404610)
    IfFlagEnabled(0, 1370)
    EnableMapPiece(2404610)


def Event12400654():
    """ 12400654: Event 12400654 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2400901)
    DisableCharacter(2400901)
    DropMandatoryTreasure(2400901)
    End()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2400901)
    EndIfFlagDisabled(1370)
    DisableFlagRange((1360, 1379))
    EnableFlag(1371)


def Event12400655():
    """ 12400655: Event 12400655 """
    EndIfThisEventFlagEnabled()
    DisableBackread(2400901)
    IfFlagEnabled(0, 1370)
    EnableBackread(2400901)


def Event12400656():
    """ 12400656: Event 12400656 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 1374)
    IfFlagEnabled(1, 9802)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1372)
    DisableBackread(2400900)
    EnableBackread(2400902)
    SetTeamType(2400902, TeamType.HostileNPC)
    DisableBackread(2400903)


def Event12400657():
    """ 12400657: Event 12400657 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(1, 2400900)
    IfCharacterDead(2, 2400902)
    IfCharacterDead(3, 2400903)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFlagEnabled(7, 1369)
    DisableFlagRange((1700, 1705))
    SkipLinesIfFlagRangeAllDisabled(1, (1362, 1364))
    EnableFlag(1701)
    SkipLinesIfFlagRangeAllDisabled(1, (1370, 1371))
    EnableFlag(1704)
    SkipLinesIfFlagDisabled(1, 1372)
    EnableFlag(1705)
    DisableFlagRange((1360, 1379))
    EnableFlag(1368)
    SaveRequest()


def Event12400658():
    """ 12400658: Event 12400658 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 72400526)
    DisableFlagRange((1700, 1705))
    SkipLinesIfFlagRangeAllDisabled(1, (1362, 1364))
    EnableFlag(1701)
    SkipLinesIfFlagRangeAllDisabled(1, (1370, 1371))
    EnableFlag(1704)
    SkipLinesIfFlagDisabled(1, 1372)
    EnableFlag(1705)
    DisableFlagRange((1360, 1379))
    EnableFlag(1369)
    SetTeamType(2400900, TeamType.HostileNPC)
    SaveRequest()


def Event12400659():
    """ 12400659: Event 12400659 """
    EndIfThisEventFlagEnabled()
    IfAttacked(0, 2400900, attacker=PLAYER)
    WaitFrames(1)
    IfAttacked(0, 2400900, attacker=PLAYER)
    WaitFrames(1)
    IfAttacked(0, 2400900, attacker=PLAYER)
    WaitFrames(1)


def Event12400660():
    """ 12400660: Event 12400660 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 1373)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


def Event12400661():
    """ 12400661: Event 12400661 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 1374)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


def Event12400662():
    """ 12400662: Event 12400662 """
    IfFlagEnabled(1, 1370)
    IfFlagEnabled(1, 72400530)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400903, 103034, loop=True)
    IfFlagDisabled(0, 72400530)
    ForceAnimation(2400903, 103031, loop=True)
    Restart()


def Event12400663():
    """ 12400663: Event 12400663 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1370)
    IfFlagEnabled(-1, 1371)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(1, attacked_entity=2400903, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400903, 103032)
    Kill(2400903, award_souls=True)


def Event12400665():
    """ 12400665: Event 12400665 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1365)
    IfFlagEnabled(-1, 1366)
    IfFlagEnabled(-1, 1367)
    IfConditionTrue(0, input_condition=-1)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@RestartOnRest
def Event12400700():
    """ 12400700: Event 12400700 """
    IfFlagEnabled(1, 1106)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    ForceAnimation(2400700, 2250)
    DropMandatoryTreasure(2400700)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(2, 1108)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    DisableBackread(2400700)
    DropMandatoryTreasure(2400700)
    EnableMapPiece(2404604)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 1109)
    EndIfConditionFalse(3)
    DisableFlag(1109)


@RestartOnRest
def Event12400701():
    """ 12400701: Event 12400701 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 72400300)
    DisableFlagRange((1100, 1119))
    EnableFlag(1101)


@RestartOnRest
def Event12400702():
    """ 12400702: Event 12400702 """
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(1106)
    EndIfFlagEnabled(1108)
    IfFlagRangeAnyEnabled(1, (12400720, 12400724))
    IfFlagEnabled(2, 1106)
    IfFlagEnabled(3, 1108)
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
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(1106)
    EndIfFlagEnabled(1108)
    IfFlagEnabled(1, 72400985)
    IfFlagEnabled(2, 1106)
    IfFlagEnabled(3, 1108)
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
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(1106)
    EndIfFlagEnabled(1108)
    IfFlagEnabled(-1, 1164)
    IfFlagEnabled(-1, 1165)
    IfFlagEnabled(-1, 1167)
    IfFlagEnabled(-2, 1181)
    IfFlagEnabled(-2, 1185)
    IfFlagEnabled(-2, 1186)
    IfFlagEnabled(-2, 1188)
    IfFlagEnabled(-3, 1224)
    IfFlagEnabled(-3, 1225)
    IfFlagEnabled(-3, 1226)
    IfFlagEnabled(-4, 1304)
    IfFlagEnabled(-4, 1305)
    IfFlagEnabled(-4, 1307)
    IfFlagEnabled(-4, 1308)
    IfFlagEnabled(-5, 1106)
    IfFlagEnabled(-5, 1108)
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
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(1106)
    EndIfFlagEnabled(1108)
    IfFlagDisabled(1, 1164)
    IfFlagDisabled(1, 1165)
    IfFlagDisabled(1, 1167)
    IfFlagDisabled(2, 1181)
    IfFlagDisabled(2, 1185)
    IfFlagDisabled(2, 1186)
    IfFlagDisabled(2, 1188)
    IfFlagDisabled(3, 1224)
    IfFlagDisabled(3, 1225)
    IfFlagDisabled(3, 1226)
    IfFlagDisabled(4, 1304)
    IfFlagDisabled(4, 1305)
    IfFlagDisabled(4, 1307)
    IfFlagDisabled(4, 1308)
    IfFlagEnabled(-3, 1106)
    IfFlagEnabled(-3, 1108)
    IfConditionTrue(5, input_condition=-3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(6, input_condition=-1)
    IfFlagRangeAllEnabled(6, (12400708, 12400711))
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1105)


@RestartOnRest
def Event12400706():
    """ 12400706: Event 12400706 """
    EndIfFlagEnabled(1106)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, 2400700)
    IfFlagDisabled(1, 1108)
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
def Event12400708(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12400708: Event 12400708 """
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, arg_8_11)
    IfFlagEnabled(-1, arg_12_15)
    SkipLinesIfValueNotEqual(1, left=arg_16_19, right=1)
    IfFlagEnabled(-1, 1315)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionFalse(1)
    IncrementEventValue(12400733, bit_count=3, max_value=5)
    EnableFlag(72400313)
    DisableFlagRange((72400314, 72400319))
    EnableFlag(arg_4_7)


@RestartOnRest
def Event12400713(_, arg_0_3: int, arg_4_7: int):
    """ 12400713: Event 12400713 """
    IfFlagEnabled(1, arg_0_3)
    IfFlagEnabled(2, arg_4_7)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    DisableFlag(72400308)
    EnableFlag(72400307)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlag(72400307)
    EnableFlag(72400308)


@RestartOnRest
def Event12400720():
    """ 12400720: Event 12400720 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1161)
    IfFlagEnabled(-1, 1166)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400724)
    StopEvent(12400721)
    StopEvent(12400722)
    StopEvent(12400723)
    StopEvent(12400728)


@RestartOnRest
def Event12400721():
    """ 12400721: Event 12400721 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1183)
    IfFlagEnabled(-1, 1189)
    IfFlagEnabled(-1, 1191)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400725)
    StopEvent(12400720)
    StopEvent(12400722)
    StopEvent(12400723)
    StopEvent(12400729)


@RestartOnRest
def Event12400722():
    """ 12400722: Event 12400722 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1222)
    IfFlagEnabled(-1, 1230)
    IfFlagEnabled(-1, 1231)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400726)
    StopEvent(12400720)
    StopEvent(12400721)
    StopEvent(12400723)
    StopEvent(12400730)


@RestartOnRest
def Event12400723():
    """ 12400723: Event 12400723 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1303)
    IfFlagEnabled(-1, 1312)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400727)
    StopEvent(12400720)
    StopEvent(12400721)
    StopEvent(12400722)
    StopEvent(12400731)


@RestartOnRest
def Event12400728():
    """ 12400728: Event 12400728 """
    EndIfThisEventFlagEnabled()
    IfFlagRangeAnyEnabled(0, (12400720, 12400723))
    IfFlagEnabled(-1, 1161)
    IfFlagEnabled(-1, 1166)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(12400729)
    StopEvent(12400730)
    StopEvent(12400731)


@RestartOnRest
def Event12400729():
    """ 12400729: Event 12400729 """
    EndIfThisEventFlagEnabled()
    IfFlagRangeAnyEnabled(0, (12400720, 12400723))
    IfFlagEnabled(-1, 1183)
    IfFlagEnabled(-1, 1189)
    IfFlagEnabled(-1, 1191)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(12400728)
    StopEvent(12400730)
    StopEvent(12400731)


@RestartOnRest
def Event12400730():
    """ 12400730: Event 12400730 """
    EndIfThisEventFlagEnabled()
    IfFlagRangeAnyEnabled(0, (12400720, 12400723))
    IfFlagEnabled(-1, 1222)
    IfFlagEnabled(-1, 1230)
    IfFlagEnabled(-1, 1231)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(12400728)
    StopEvent(12400729)
    StopEvent(12400731)


@RestartOnRest
def Event12400731():
    """ 12400731: Event 12400731 """
    EndIfThisEventFlagEnabled()
    IfFlagRangeAnyEnabled(0, (12400720, 12400723))
    IfFlagEnabled(-1, 1303)
    IfFlagEnabled(-1, 1312)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(12400728)
    StopEvent(12400729)
    StopEvent(12400730)


@RestartOnRest
def Event12400732():
    """ 12400732: Event 12400732 """
    IfAttackedWithDamageType(1, attacked_entity=2400700, attacker=-1)
    IfFlagEnabled(1, 72400981)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(1109)


@RestartOnRest
def Event12400737():
    """ 12400737: Event 12400737 """
    EndIfFlagEnabled(1108)
    DisableMapPiece(2404604)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 1108)
    EnableMapPiece(2404604)
    DropMandatoryTreasure(2400700)


@RestartOnRest
def Event12400738():
    """ 12400738: Event 12400738 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 9432)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(2400700, 5401, affect_npc_part_hp=False)
    WaitFrames(1)
    ForceAnimation(2400700, 7000)
    IfFlagDisabled(0, 9432)
    AddSpecialEffect(2400700, 5402, affect_npc_part_hp=False)
    WaitFrames(1)
    ForceAnimation(2400700, 0)
    Restart()


def Event12400900():
    """ 12400900: Event 12400900 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L6, input_condition=15)
    IfFlagEnabled(1, 1313)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1300, 1319))
    EnableFlag(1304)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 72400942)
    IfFlagEnabled(3, 72400380)
    IfFlagEnabled(-1, 1304)
    IfFlagEnabled(-1, 1305)
    IfConditionTrue(3, input_condition=-1)
    IfFlagEnabled(-2, 1224)
    IfFlagEnabled(-2, 1225)
    IfFlagEnabled(-2, 1226)
    IfFlagEnabled(-2, 1227)
    IfConditionTrue(3, input_condition=-2)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1300, 1319))
    EnableFlag(1306)
    DisableFlagRange((1220, 1239))
    EnableFlag(1230)
    Goto(Label.L2)

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L5, 9802)
    GotoIfFlagEnabled(Label.L3, 1304)
    GotoIfFlagEnabled(Label.L3, 1305)
    GotoIfFlagEnabled(Label.L4, 1306)
    Goto(Label.L5)

    # --- 4 --- #
    DefineLabel(4)
    DisableFlagRange((1300, 1319))
    EnableFlag(1308)
    Goto(Label.L5)

    # --- 3 --- #
    DefineLabel(3)
    DisableFlagRange((1300, 1319))
    EnableFlag(1307)
    Goto(Label.L5)

    # --- 5 --- #
    DefineLabel(5)
    DisableFlag(72400393)

    # --- 6 --- #
    DefineLabel(6)
    DisableGravity(2400770)
    DisableCharacterCollision(2400770)
    DisableGravity(2400772)
    DisableCharacterCollision(2400772)
    DisableGravity(2400774)
    DisableCharacterCollision(2400774)
    GotoIfFlagEnabled(Label.L0, 1304)
    GotoIfFlagEnabled(Label.L0, 1305)
    GotoIfFlagEnabled(Label.L4, 1306)
    GotoIfFlagEnabled(Label.L1, 1307)
    GotoIfFlagEnabled(Label.L2, 1308)
    GotoIfFlagEnabled(Label.L3, 1312)
    GotoIfFlagEnabled(Label.L5, 1317)
    GotoIfFlagEnabled(Label.L6, 1303)
    DisableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    ForceAnimation(2400770, 103096, loop=True, skip_transition=True)
    Move(2400770, destination=2404503, destination_type=CoordEntityType.Region, short_move=True)
    EndIfClient()
    EnableFlag(72400491)
    End()

    # --- 4 --- #
    DefineLabel(4)
    DisableBackread(2400770)
    DisableBackread(2400772)
    EnableBackread(2400774)
    DisableBackread(2400775)
    PostDestruction(2400773)
    ForceAnimation(2400774, 103096, loop=True, skip_transition=True)
    Move(2400774, destination=2404503, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableBackread(2400770)
    EnableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    ForceAnimation(2400772, 103096, loop=True, skip_transition=True)
    Move(2400772, destination=2404503, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    EnableBackread(2400775)
    PostDestruction(2400773)
    DisableAI(2400775)
    Move(2400775, destination=2404381, destination_type=CoordEntityType.Region, set_draw_parent=2404100)
    SetTeamType(2400775, TeamType.HostileNPC)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableBackread(2400770)
    DisableCharacter(2400770)
    DisableBackread(2400772)
    DisableCharacter(2400772)
    DisableBackread(2400774)
    DisableCharacter(2400774)
    DisableBackread(2400775)
    DisableCharacter(2400775)
    PostDestruction(2400773)
    EzstateAIRequest(2400770, command_id=8, slot=1)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(1)
    DropMandatoryTreasure(2400770)
    End()

    # --- 5 --- #
    DefineLabel(5)
    DisableBackread(2400770)
    DisableCharacter(2400770)
    DisableBackread(2400772)
    DisableCharacter(2400772)
    DisableBackread(2400774)
    DisableCharacter(2400774)
    DisableBackread(2400775)
    DisableCharacter(2400775)
    PostDestruction(2400773)
    DisableAI(2400775)
    Move(2400775, destination=2404381, destination_type=CoordEntityType.Region, set_draw_parent=2404100)
    WaitFrames(1)
    DropMandatoryTreasure(2400775)
    End()

    # --- 6 --- #
    DefineLabel(6)
    EnableBackread(2400770)
    EnableCharacter(2400770)
    DisableBackread(2400772)
    DisableCharacter(2400772)
    DisableBackread(2400774)
    DisableCharacter(2400774)
    DisableBackread(2400775)
    DisableCharacter(2400775)
    PostDestruction(2400773)
    EzstateAIRequest(2400770, command_id=8, slot=1)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(1)
    DropMandatoryTreasure(2400770)
    End()


def Event12400901():
    """ 12400901: Event 12400901 """
    IfFlagEnabled(0, 72400394)
    DisableFlag(72400394)
    IfFlagEnabled(1, 1304)
    IfFlagEnabled(1, 72400380)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1300, 1319))
    EnableFlag(1305)


def Event12400940(_, arg_0_3: int):
    """ 12400940: Event 12400940 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 72400955)
    IfCharacterHasSpecialEffect(1, arg_0_3, 157)
    IfFlagDisabled(1, 72400955)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 103106)
    Restart()


def Event12400903():
    """ 12400903: Event 12400903 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1317)
    EndIfFlagEnabled(1312)
    EndIfFlagEnabled(1303)
    IfCharacterDead(-1, 2400770)
    IfCharacterDead(-1, 2400772)
    IfCharacterDead(-1, 2400774)
    IfCharacterDead(-1, 2400775)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagEnabled(Label.L0, 1308)
    DisableFlagRange((1300, 1319))
    EnableFlag(1303)
    SaveRequest()
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1300, 1319))
    EnableFlag(1317)
    SaveRequest()
    End()


def Event12400904():
    """ 12400904: Event 12400904 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 1308)
    IfCharacterInsideRegion(1, PLAYER, region=2404380)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=2400775, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400397)
    EnableAI(2400775)


def Event12400910(_, arg_0_3: int):
    """ 12400910: Event 12400910 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(2, arg_0_3, 151)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    IfCharacterHasSpecialEffect(3, arg_0_3, 158)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    ForceAnimation(arg_0_3, 103134)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 103098)
    WaitFrames(20)
    Restart()


def Event12400915(_, arg_0_3: int):
    """ 12400915: Event 12400915 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1317)
    EndIfFlagEnabled(1312)
    EndIfFlagEnabled(1303)
    IfHealthEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(-1, arg_0_3, 151)
    IfCharacterHasSpecialEffect(-1, arg_0_3, 158)
    IfConditionTrue(1, input_condition=-1)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(arg_0_3, 103135)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 103099)
    End()


def Event12400920(_, arg_0_3: int):
    """ 12400920: Event 12400920 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagDisabled(0, 72400955)
    IfFlagEnabled(0, 72400955)
    IfCharacterHasSpecialEffect(1, arg_0_3, 151)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(arg_0_3, 103104)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 103101)
    IfCharacterHasSpecialEffect(0, arg_0_3, 152)
    ForceAnimation(arg_0_3, 103104)
    Restart()


def Event12400925(_, arg_0_3: int):
    """ 12400925: Event 12400925 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(-1, arg_0_3, 153)
    IfCharacterHasSpecialEffect(-1, arg_0_3, 159)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(1, arg_0_3, 153)
    GotoIfConditionTrue(Label.L2, input_condition=1)
    IfCharacterHasSpecialEffect(2, arg_0_3, 159)
    GotoIfConditionTrue(Label.L0, input_condition=2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(3, 9432)
    IfFlagDisabled(3, 1307)
    IfFlagDisabled(3, 1306)
    GotoIfConditionTrue(Label.L1, input_condition=3)
    ForceAnimation(arg_0_3, 103102, loop=True)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(arg_0_3, 103103, loop=True)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(4, 9432)
    IfFlagDisabled(4, 1307)
    IfFlagDisabled(4, 1306)
    GotoIfConditionTrue(Label.L3, input_condition=4)
    ForceAnimation(arg_0_3, 103096, loop=True)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    ForceAnimation(arg_0_3, 103097, loop=True)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    WaitFrames(5)
    Restart()


def Event12400930(_, arg_0_3: int):
    """ 12400930: Event 12400930 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, arg_0_3, 156)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 103102)
    Restart()


def Event12400935(_, arg_0_3: int):
    """ 12400935: Event 12400935 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=5.0)
    IfCharacterHasSpecialEffect(1, arg_0_3, 151)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 103101, wait_for_completion=True)


def Event12400952():
    """ 12400952: Event 12400952 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, 1306)
    GotoIfFlagEnabled(Label.L0, 1308)
    GotoIfFlagEnabled(Label.L0, 1312)
    IfFlagEnabled(0, 6001)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DestroyObject(2400773)
    End()


def Event12400953():
    """ 12400953: Event 12400953 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthNotEqual(1, 2400770, 0.0)
    IfHealthNotEqual(1, 2400774, 0.0)
    IfFlagEnabled(1, 9432)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(-1, 2400770, 151)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    ForceAnimation(2400770, 103103)
    IfFlagDisabled(0, 9432)
    ForceAnimation(2400770, 103102)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2400770, 103097)
    IfFlagDisabled(0, 9432)
    ForceAnimation(2400770, 103096)
    Restart()


def Event12400954():
    """ 12400954: Event 12400954 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerHasGood(1, 702, including_box=False)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableFlag(72400392)
    End()

    # --- 0 --- #
    DefineLabel(0)
    End()


def Event12400800():
    """ 12400800: Event 12400800 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2400765, attacker=PLAYER)
    IfHealthEqual(1, 2400765, 0.0)
    IfAttackedWithDamageType(2, attacked_entity=2400730, attacker=PLAYER)
    IfHealthEqual(2, 2400730, 0.0)
    IfAttackedWithDamageType(3, attacked_entity=2400750, attacker=PLAYER)
    IfHealthEqual(3, 2400750, 0.0)
    IfAttackedWithDamageType(4, attacked_entity=2400754, attacker=PLAYER)
    IfHealthEqual(4, 2400754, 0.0)
    IfAttackedWithDamageType(5, attacked_entity=2400757, attacker=PLAYER)
    IfHealthEqual(5, 2400757, 0.0)
    IfAttackedWithDamageType(7, attacked_entity=2400770, attacker=PLAYER)
    IfHealthEqual(7, 2400770, 0.0)
    IfAttackedWithDamageType(8, attacked_entity=2400772, attacker=PLAYER)
    IfHealthEqual(8, 2400772, 0.0)
    IfAttackedWithDamageType(9, attacked_entity=2400774, attacker=PLAYER)
    IfHealthEqual(9, 2400774, 0.0)
    IfAttackedWithDamageType(13, attacked_entity=2400700, attacker=PLAYER)
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


def Event12400801():
    """ 12400801: Event 12400801 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagDisabled(Label.L0, 1166)
    DisableBackread(2400765)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400765)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, 1191)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400730)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, 1231)
    EnableObject(2400748)
    DisableMapPiece(2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400750)

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L3, 1230)
    EnableObject(2400748)
    DisableMapPiece(2404601)
    EnableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400750, 103087)
    EzstateAIRequest(2400750, command_id=5, slot=1)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400750)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L4, 1312)
    DisableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400770)

    # --- 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L4, 1108)
    EnableMapPiece(2404604)
    DropMandatoryTreasure(2400700)
    DisableBackread(2400700)

    # --- 5 --- #
    DefineLabel(5)


def Event12400805(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12400805: Event 12400805 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, arg_0_3, arg_8_11)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, arg_4_7)
    WaitFrames(5)
    Restart()


def Event12400810(_, arg_0_3: int, arg_4_7: int):
    """ 12400810: Event 12400810 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, arg_4_7)
    Restart()


def Event12400830(_, arg_0_3: int, arg_4_7: int):
    """ 12400830: Event 12400830 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, arg_4_7)


def Event12400840(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12400840: Event 12400840 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(arg_0_3)
    IfFlagDisabled(1, arg_0_3)
    IfActionButtonParamActivated(1, action_button_id=arg_4_7, entity=arg_8_11)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=210, short_move=True)
    ForceAnimation(PLAYER, 101320)
    WaitFrames(25)
    WaitFrames(20)
    EnableFlag(arg_0_3)
    IfFlagDisabled(0, arg_0_3)
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

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2400396, command_id=10, slot=0)
    SetNest(2400396, 2409007)
    ReplanAI(2400396)

    # --- 1 --- #
    DefineLabel(1)
    AICommand(2400410, command_id=10, slot=0)
    SetNest(2400410, 2409007)
    ReplanAI(2400410)

    # --- 2 --- #
    DefineLabel(2)
    AICommand(2400393, command_id=10, slot=0)
    SetNest(2400393, 2409007)
    ReplanAI(2400393)
    IfCharacterInsideRegion(-2, 2400393, region=2402030)
    IfCharacterInsideRegion(-2, 2400396, region=2402030)
    IfCharacterInsideRegion(-2, 2400410, region=2402030)
    IfConditionTrue(0, input_condition=-2)
    IfEntityWithinDistance(-3, 2400393, PLAYER, radius=5.0)
    IfEntityWithinDistance(-3, 2400396, PLAYER, radius=5.0)
    IfEntityWithinDistance(-3, 2400410, PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=-3)
    AICommand(2400393, command_id=-1, slot=0)
    ReplanAI(2400393)
    AICommand(2400396, command_id=-1, slot=0)
    ReplanAI(2400396)
    AICommand(2400410, command_id=-1, slot=0)
    ReplanAI(2400410)


@RestartOnRest
def Event12405701(_, arg_0_3: int, arg_4_7: int):
    """ 12405701: Event 12405701 """
    IfCharacterInsideRegion(-1, 2400393, region=2402030)
    IfCharacterInsideRegion(-1, 2400396, region=2402030)
    IfCharacterInsideRegion(-1, 2400410, region=2402030)
    IfConditionTrue(0, input_condition=-1)
    AICommand(arg_0_3, command_id=10, slot=0)
    SetNest(arg_0_3, arg_4_7)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=2402030)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=5.0)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12405710():
    """ 12405710: Event 12405710 """
    GotoIfFlagDisabled(Label.L0, 9453)
    EndOfAnimation(2401202, 1)
    NotifyDoorEventSoundDampening(2401202, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    IfActionButtonParamActivated(0, action_button_id=7000, entity=2401202)
    DisplayDialog(
        CommonEventTexts.Locked,
        anchor_entity=2401202,
        display_distance=5.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


@RestartOnRest
def Event12405750(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12405750: Event 12405750 """
    EndIfThisEventSlotFlagEnabled()
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_8_11)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(arg_0_3, arg_4_7)


def VicarAmeliaDies():
    """ 12401800: Event 12401800 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(2403802)
    DisableSoundEvent(2403803)
    DisableCharacter(2400800)
    DisableObject(2400801)
    Kill(2400800, award_souls=False)
    DisableObject(Objects.BossFog)
    DeleteVFX(VFX.BossFog, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2400800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.BossFog)
    DeleteVFX(VFX.BossFog, erase_root_only=True)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=0)
    Wait(3.0)
    KillBoss(2400800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(3,))
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

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)
    EndIfClient()


def PlayVicarAmeliaDeathSound():
    """ 12401801: Event 12401801 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    IfFlagEnabled(1, Flags.VicarAmeliaDead)
    IfCharacterBackreadDisabled(2, Characters.VicarAmelia)
    IfHealthLessThanOrEqual(2, Characters.VicarAmelia, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2402800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def VicarAmeliaFirstTime():
    """ 12401802: First time cutscene. """
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    DisableObject(2400801)
    EndIfThisEventFlagEnabled()
    DisableCharacter(Characters.VicarAmelia)
    EnableObject(2400801)
    EnableObjectInvulnerability(2400801)
    IfFlagDisabled(1, Flags.VicarAmeliaDead)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2402805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12404223)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    EnableFlag(72400400)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(24000060, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(24000060, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObject(2400801)
    DisableFlag(CommonFlags.CutsceneActive)
    EnableCharacter(Characters.VicarAmelia)
    ForceAnimation(Characters.VicarAmelia, 7000)
    ForceAnimation(Characters.VicarAmelia, 7001)
    EnableFlag(Flags.VicarAmeliaFogEntered)
    EndIfFlagEnabled(9301)
    RunEvent(9350, 0, args=(1,))
    EnableFlag(9301)


def PlayMasterWillemCutscene():
    """ 12401803: Play cutscene between Laurence and Master Willem at skull after Vicar Amelia is killed. """
    DeleteVFX(VFX.LaurenceSkull, erase_root_only=False)
    EndIfThisEventFlagEnabled()
    GotoIfFlagEnabled(Label.L0, Flags.VicarAmeliaDead)
    IfFlagEnabled(0, Flags.VicarAmeliaDead)

    # --- 0 --- #
    DefineLabel(0)
    CreateVFX(VFX.LaurenceSkull)
    EndIfClient()
    IfCharacterHuman(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2400010, entity=2401801)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    DeleteVFX(VFX.LaurenceSkull, erase_root_only=True)
    PlayCutsceneAndMovePlayerAndSetTimePeriod(
        Cutscenes.LaurenceFlashback, CutsceneFlags.Skippable, -1, CATHEDRAL_WARD, player_id=10000, time_period_id=2
    )
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)


def SummonStartVicarAmeliaBattle():
    """ 12401804: Event 12401804 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.VicarAmeliaFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(Characters.VicarAmelia)
    EnableFlag(Flags.VicarAmeliaFogEntered)
    EnableFlag(Flags.VicarAmeliaFirstTimeDone)


def EnterVicarAmeliaBossFog():
    """ 12404840: For some reason, this uses a different ID to the fog flag. """
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    GotoIfFlagEnabled(Label.L0, Flags.VicarAmeliaFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.BossFog)
    DeleteVFX(VFX.BossFog, erase_root_only=False)
    IfFlagDisabled(1, Flags.VicarAmeliaDead)
    IfFlagEnabled(1, Flags.VicarAmeliaFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.BossFog)
    CreateVFX(VFX.BossFog)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.VicarAmeliaDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2400800, entity=Objects.BossFog)
    IfFlagEnabled(3, Flags.VicarAmeliaDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2402800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2402801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.VicarAmeliaFogEntered)
    Restart()


def EnterVicarAmeliaBossFogAsSummon():
    """ 12404841: Event 12404841 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    IfFlagDisabled(1, Flags.VicarAmeliaDead)
    IfFlagEnabled(1, Flags.VicarAmeliaFirstTimeDone)
    IfFlagEnabled(1, Flags.VicarAmeliaFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2400800, entity=Objects.BossFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2402800, animation=101130)
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


def Event12404842():
    """ 12404842: Event 12404842 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.BossFog, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12404843():
    """ 12404843: Event 12404843 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.BossFog, radius=6.0)
    IfEntityWithinDistance(1, PLAYER, Objects.BossFog, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def StartVicarAmeliaBattle():
    """ 12404802: Event 12404802 """
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    DisableAI(Characters.VicarAmelia)
    DisableHealthBar(Characters.VicarAmelia)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.VicarAmeliaFogEntered)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 12404223)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.VicarAmelia, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12404223)
    EnableFlag(Flags.VicarAmeliaFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.VicarAmelia, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.VicarAmelia)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.VicarAmelia, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.VicarAmelia)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.VicarAmelia)
    EnableBossHealthBar(Characters.VicarAmelia, name=502000, slot=0)
    ForceAnimation(Characters.VicarAmelia, 7002)
    CreatePlayLog(160)
    StartPlayLogMeasurement(2410010, 176, overwrite=True)


def ControlVicarAmeliaMusic():
    """ 12404803: Event 12404803 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2403802)
    DisableSoundEvent(2403803)
    IfFlagDisabled(1, Flags.VicarAmeliaDead)
    IfFlagEnabled(1, Flags.VicarAmeliaBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12404801)
    IfCharacterInsideRegion(1, PLAYER, region=2402802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2403802)
    IfCharacterHasTAEEvent(2, Characters.VicarAmelia, tae_event_id=100)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.VicarAmeliaDead)
    IfFlagEnabled(2, Flags.VicarAmeliaBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12404801)
    IfCharacterInsideRegion(2, PLAYER, region=2402802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2403802)
    WaitFrames(0)
    EnableBossMusic(2403803)


def ControlVicarAmeliaCamera():
    """ 12404804: Event 12404804 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    IfHealthGreaterThan(1, Characters.VicarAmelia, 0.0)
    IfEntityWithinDistance(1, PLAYER, Characters.VicarAmelia, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=1)
    IfHealthGreaterThan(2, Characters.VicarAmelia, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.VicarAmelia, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=0)
    Restart()


def StopVicarAmeliaMusic():
    """ 12404805: Event 12404805 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    IfFlagEnabled(0, Flags.VicarAmeliaDead)
    DisableBossMusic(2403802)
    DisableBossMusic(2403803)
    DisableBossMusic(-1)


def VicarAmeliaPhaseTwoTrigger():
    """ 12404807: Event 12404807 """
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    IfHealthLessThan(0, Characters.VicarAmelia, 0.5)
    AICommand(Characters.VicarAmelia, command_id=100, slot=1)
    ReplanAI(Characters.VicarAmelia)
    IfCharacterHasTAEEvent(0, Characters.VicarAmelia, tae_event_id=100)
    AICommand(Characters.VicarAmelia, command_id=-1, slot=1)
    ReplanAI(Characters.VicarAmelia)


def ControlVicarAmeliaCloth():
    """ 12404808: Event 12404808 """
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHasSpecialEffect(0, Characters.VicarAmelia, 482)

    # --- 0 --- #
    DefineLabel(0)
    ChangeCharacterCloth(Characters.VicarAmelia, 15, state_id=2)


@RestartOnRest
def VicarAmeliaLimbDamage(
    _, npc_part_id: short, vulnerable_npc_part_id: int, part_index: short, part_health: int, wounded_effect: int,
    not_wounded_effect: int, wounded_animation: int
):
    """ 12404810: Event 12404810 """
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    CreateNPCPart(
        Characters.VicarAmelia,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=part_health,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.VicarAmelia, npc_part_id=vulnerable_npc_part_id, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, Characters.VicarAmelia, npc_part_id=vulnerable_npc_part_id, value=0)
    IfHealthLessThanOrEqual(3, Characters.VicarAmelia, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(
        Characters.VicarAmelia,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.VicarAmelia, npc_part_id=vulnerable_npc_part_id, material_sfx_id=73, material_vfx_id=73)
    WaitFrames(1)
    ResetAnimation(Characters.VicarAmelia, disable_interpolation=False)
    ForceAnimation(Characters.VicarAmelia, wounded_animation)
    AddSpecialEffect(Characters.VicarAmelia, wounded_effect, affect_npc_part_hp=False)
    RemoveSpecialEffect(Characters.VicarAmelia, not_wounded_effect)
    ReplanAI(Characters.VicarAmelia)
    Wait(30.0)
    AICommand(Characters.VicarAmelia, command_id=1, slot=0)
    ReplanAI(Characters.VicarAmelia)
    IfCharacterHasTAEEvent(0, Characters.VicarAmelia, tae_event_id=300)
    SetNPCPartHealth(Characters.VicarAmelia, npc_part_id=vulnerable_npc_part_id, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(Characters.VicarAmelia, not_wounded_effect, affect_npc_part_hp=False)
    RemoveSpecialEffect(Characters.VicarAmelia, wounded_effect)
    AICommand(Characters.VicarAmelia, command_id=-1, slot=0)
    ReplanAI(Characters.VicarAmelia)
    WaitFrames(10)
    Restart()


def VicarAmeliaLimbAppearance(
    _, wounded_effect: int, not_wounded_effect: int, wounded_bit_index: uchar, not_wounded_bit_index: uchar
):
    """ 12404820: Event 12404820 """
    EndIfFlagEnabled(Flags.VicarAmeliaDead)
    IfCharacterHasSpecialEffect(1, Characters.VicarAmelia, wounded_effect)
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.VicarAmelia, not_wounded_effect)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(Characters.VicarAmelia, bit_index=not_wounded_bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.VicarAmelia, bit_index=wounded_bit_index, switch_type=OnOffChange.Off)
    IfCharacterDoesNotHaveSpecialEffect(2, Characters.VicarAmelia, wounded_effect)
    IfCharacterHasSpecialEffect(2, Characters.VicarAmelia, not_wounded_effect)
    IfConditionTrue(0, input_condition=2)
    SetDisplayMask(Characters.VicarAmelia, bit_index=wounded_bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.VicarAmelia, bit_index=not_wounded_bit_index, switch_type=OnOffChange.Off)
    WaitFrames(10)
    Restart()


@RestartOnRest
def VicarAmeliaStopsHealing():
    """ 12404830: Vicar Amelia plays animation 3035 when she finishes healing or is hit by Numbing Mist. """
    IfCharacterHasSpecialEffect(1, Characters.VicarAmelia, 2150)  # Numbing Mist
    IfCharacterHasSpecialEffect(1, Characters.VicarAmelia, 5639)  # Amelia regeneration
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.VicarAmelia, 3035)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12406900(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12406900: Event 12406900 """
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.a_Ambient, sound_id=arg_8_11)
    WaitFrames(1)


def Event12400990():
    """ 12400990: Event 12400990 """
    EndIfThisEventFlagEnabled()
    IfPlayerStandingOnCollision(0, 2404101)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 194, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 194, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 194, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 194, PlayLogMultiplayerType.HostOnly)


def Event12407020(_, arg_0_3: int, arg_4_7: int):
    """ 12407020: Event 12407020 """
    IfFlagEnabled(0, arg_0_3)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    ForceAnimation(PLAYER, 101160, skip_transition=True)
    Wait(4.0)
    DisableFlag(arg_0_3)


def Event12407040(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12407040: Event 12407040 """
    IfFlagEnabled(0, arg_0_3)
    DisableFlag(arg_0_3)
    WarpPlayerToRespawnPoint(arg_4_7)
    EnableFlag(arg_8_11)


@RestartOnRest
def Event12407050(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12407050: Event 12407050 """
    EndIfFlagEnabled(arg_0_3)
    IfCharacterBackreadEnabled(0, arg_4_7)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    ForceAnimation(arg_4_7, 101165, loop=True)
    Wait(1.0)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    IfFlagEnabled(0, arg_0_3)
    ForceAnimation(arg_4_7, 101166, wait_for_completion=True)
    DisableCharacter(arg_4_7)


def Event12407000():
    """ 12407000: Event 12407000 """
    SkipLinesIfFlagRangeAnyEnabled(1, (9001, 9010))
    End()
    EnableFlag(9210)
    IfFlagDisabled(0, 9210)
    SkipLinesIfFlagDisabled(3, 9001)
    EnableFlag(12407811)
    EnableFlag(12407810)
    SetRespawnPoint(2402950)
    SkipLinesIfFlagDisabled(3, 9002)
    EnableFlag(12407831)
    EnableFlag(12407830)
    SetRespawnPoint(2402951)
    SkipLinesIfFlagDisabled(3, 9003)
    EnableFlag(12407851)
    EnableFlag(12407850)
    SetRespawnPoint(2402952)
    SkipLinesIfFlagDisabled(3, 9004)
    EnableFlag(12407871)
    EnableFlag(12407870)
    SetRespawnPoint(2402953)
    SkipLinesIfFlagDisabled(3, 9005)
    EnableFlag(12407891)
    EnableFlag(12407890)
    SetRespawnPoint(2402954)
    SkipLinesIfFlagDisabled(3, 9006)
    EnableFlag(12407911)
    EnableFlag(12407910)
    SetRespawnPoint(2402955)
    SkipLinesIfFlagDisabled(3, 9007)
    EnableFlag(12407931)
    EnableFlag(12407930)
    SetRespawnPoint(2402956)
    SkipLinesIfFlagDisabled(3, 9008)
    EnableFlag(12407951)
    EnableFlag(12407950)
    SetRespawnPoint(2402957)
    SkipLinesIfFlagDisabled(3, 9009)
    EnableFlag(12407971)
    EnableFlag(12407970)
    SetRespawnPoint(2402958)
    SkipLinesIfFlagDisabled(3, 9010)
    EnableFlag(12407991)
    EnableFlag(12407990)
    SetRespawnPoint(2402959)
    DisableFlagRange((9000, 9010))


@RestartOnRest
def Event12404450(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12404450: Event 12404450 """
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(arg_0_3, region=arg_4_7, reaction_range=1.0)
    IfFlagEnabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=990, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12404400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12404400: Event 12404400 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagDisabled(1, 2400)
    IfFlagDisabled(1, 2401)
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
    IfFlagDisabled(2, 2400)
    IfFlagDisabled(2, 2401)
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12404410(
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
    """ 12404410: Event 12404410 """
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
    RemoveSpecialEffect(PLAYER, 9005)
    RemoveSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)
    DisableMapCollision(2404120)


@RestartOnRest
def Event12404460(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12404460: Event 12404460 """
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


@RestartOnRest
def Event12404490():
    """ 12404490: Event 12404490 """
    DisableNetworkSync()
    IfHost(1)
    IfFlagEnabled(1, 12404420)
    IfFlagDisabled(1, 12404430)
    IfFlagEnabled(1, Flags.VicarAmeliaFogEntered)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect_WithUnknownEffect(2400910, 35, affect_npc_parts_hp=False)
    WaitFrames(1)
    Restart()
