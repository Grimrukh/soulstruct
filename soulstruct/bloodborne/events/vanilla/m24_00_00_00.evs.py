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
220: N:\\SPRJ\\data\\Param\\event\\common.emevd
296: 
298: 
300: 
302: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
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
    SkipLinesIfFlagEnabled(7, 12401800)
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
    Event_12404400(0, flag=12404440, vfx_id=2403910, flag_1=12404420, flag_2=12404430, flag_3=12401800, flag_4=6001)
    Event_12404410(
        0,
        sign_type=0,
        character=2400910,
        region=2402910,
        summon_flag=12404420,
        dismissal_flag=12404430,
        flag=12404440,
        flag_1=12401800,
        action_button_id=10567
    )
    Event_12404450(0, character=2400910, region=2402911, flag=12404420, flag_1=12404430, flag_2=12404800)
    Event_12404460(
        0,
        character=2400910,
        region=2402911,
        region_1=2402800,
        region_2=2402801,
        animation=101130,
        flag=12404450,
        region_3=2402801
    )
    Event_12404490()
    CreateObjectVFX(2401900, vfx_id=200, model_point=900130)
    CreateObjectVFX(2401901, vfx_id=200, model_point=900130)
    RegisterLadder(start_climbing_flag=12400600, stop_climbing_flag=12400601, obj=2401020)
    RegisterLadder(start_climbing_flag=12400602, stop_climbing_flag=12400603, obj=2401021)
    RegisterLadder(start_climbing_flag=12400604, stop_climbing_flag=12400605, obj=2401022)
    RegisterLadder(start_climbing_flag=12400606, stop_climbing_flag=12400607, obj=2401023)
    RegisterLadder(start_climbing_flag=12400608, stop_climbing_flag=12400609, obj=2401024)
    CreateProjectileOwner(entity=2400000)
    CreateProjectileOwner(entity=2402070)
    CreateProjectileOwner(entity=2402071)
    CreateProjectileOwner(entity=2402072)
    DisableGravity(2400899)
    DisableCharacterCollision(2400899)
    CreateHazard(
        obj_flag=12400190,
        obj=2401017,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12400191,
        obj=2401018,
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
    Event_12400350(4, obj=2401501, obj_act_id=12400451)
    SkipLines(5)
    DisableObject(2401501)
    EnableObject(2401505)
    DisableObjectActivation(2401501, obj_act_id=9942)
    EnableObjectActivation(2401505, obj_act_id=9942)
    Event_12400350(5, obj=2401505, obj_act_id=12400455)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6310)
    EnableFlag(12401998)
    SkipLinesIfFlagEnabled(6, 12401998)
    EnableObject(2401502)
    DisableObject(2401508)
    EnableObjectActivation(2401502, obj_act_id=9942)
    DisableObjectActivation(2401508, obj_act_id=9942)
    Event_12400350(7, obj=2401502, obj_act_id=12400452)
    SkipLines(5)
    DisableObject(2401502)
    EnableObject(2401508)
    DisableObjectActivation(2401502, obj_act_id=9942)
    EnableObjectActivation(2401508, obj_act_id=9942)
    Event_12400350(8, obj=2401508, obj_act_id=12400458)
    IfCharacterHuman(13, PLAYER)
    SkipLinesIfConditionFalse(2, 13)
    SkipLinesIfFlagDisabled(1, 6311)
    EnableFlag(12401997)
    SkipLinesIfFlagEnabled(6, 12401997)
    EnableObject(2401504)
    DisableObject(2401507)
    EnableObjectActivation(2401504, obj_act_id=9942)
    DisableObjectActivation(2401507, obj_act_id=9942)
    Event_12400350(9, obj=2401504, obj_act_id=12400454)
    SkipLines(5)
    DisableObject(2401504)
    EnableObject(2401507)
    DisableObjectActivation(2401504, obj_act_id=9942)
    EnableObjectActivation(2401507, obj_act_id=9942)
    Event_12400350(10, obj=2401507, obj_act_id=12400457)
    Event_12400070(0, obj=2421201, obj_act_id=1, animation_id=2420020, obj_act_id_1=12420120)
    Event_12400080(0, entity=2401207, flag=12400177, flag_1=12400178, action_button_id=2400050)
    Event_12400080(1, entity=2401207, flag=12400177, flag_1=12400178, action_button_id=2400051)
    Event_12400080(2, entity=2401208, flag=12400157, flag_1=12405179, action_button_id=2400050)
    Event_12400080(3, entity=2401208, flag=12400157, flag_1=12405179, action_button_id=2400051)
    Event_12400080(4, entity=2401220, flag=12400160, flag_1=12400160, action_button_id=2400031)
    Event_12400080(5, entity=2401209, flag=12400167, flag_1=12405175, action_button_id=2400050)
    Event_12400080(6, entity=2401209, flag=12400167, flag_1=12405175, action_button_id=2400051)
    Event_12400095(0, entity=2401095)
    Event_12400100(0, obj=2401040, obj_act_id=12400190, obj_act_id_1=9921, obj_act_id_2=19921)
    Event_12400100(1, obj=2401040, obj_act_id=12400191, obj_act_id_1=9921, obj_act_id_2=19921)
    Event_12400125()
    Event_12400126()
    Event_12400127()
    Event_12400128()
    Event_12400130(0, obj=2401204, animation_id=1, obj_act_id=12400112, flag=12400130)
    Event_12400130(1, obj=2401200, animation_id=2, obj_act_id=12400113, flag=12400131)
    Event_12400130(2, obj=2101201, animation_id=1, obj_act_id=12400102, flag=12400132)
    Event_12400130(3, obj=2101202, animation_id=2, obj_act_id=12400103, flag=12400133)
    Event_12400130(5, obj=2401211, animation_id=1, obj_act_id=12400190, flag=12400135)
    Event_12400130(6, obj=2401212, animation_id=1, obj_act_id=12400191, flag=12400136)
    Event_12400130(7, obj=2401201, animation_id=1, obj_act_id=12400114, flag=12400137)
    Event_12400130(8, obj=2401213, animation_id=2, obj_act_id=12400200, flag=12400138)
    Event_12400146()
    Event_12400147()
    Event_12400148()
    Event_12400149()
    Event_12400159()
    Event_12400155()
    Event_12400156()
    Event_12400158()
    Event_12400161()
    Event_12400174()
    Event_12400175()
    Event_12400179(0, entity=2401015)
    Event_12400179(1, entity=2401016)
    Event_12400185()
    Event_12400200(2, character=2400344, flag=52400980)
    Event_12400200(3, character=2400371, flag=52400960)
    Event_12400200(4, character=2400372, flag=52400990)
    Event_12400200(5, character=2400373, flag=52400970)
    Event_12400200(6, character=2400374, flag=52400950)
    Event_12400200(7, character=2400375, flag=52400940)
    Event_12400300()
    Event_12400350(0, obj=2401500, obj_act_id=12400450)
    Event_12400350(2, obj=2401503, obj_act_id=12400453)
    Event_12400350(3, obj=2401504, obj_act_id=12400454)
    Event_12400350(6, obj=2401506, obj_act_id=12400456)
    Event_12400750()
    Event_12400765()
    Event_12400760()
    Event_12400420()
    Event_12400823()
    Event_12400824()
    Event_12400825()
    Event_12400826()
    Event_12400850(0, 2407020, 2407021, 2407022, 12400130, 0, 0.0, 0, 0)
    Event_12400850(1, 2407025, 2407026, 2407027, 12400132, 0, 0.0, 0, 0)
    Event_12400850(2, 2407028, 2407029, 2407030, 12400131, 0, 0.0, 0, 0)
    Event_12400850(3, 2406700, 2406701, 2406702, 12400133, 0, 0.0, 0, 0)
    Event_12400854()
    Event_12400860()
    Event_12405710()
    Event_12400865(0, character=2400660)
    Event_12400865(1, character=2400661)
    Event_12400780(0, attacker__character=2400360)
    Event_12400780(1, attacker__character=2400361)
    Event_12400780(2, attacker__character=2400362)
    Event_12400780(3, attacker__character=2400363)
    Event_12400791(0, character=2400360)
    Event_12400791(1, character=2400361)
    Event_12400791(2, character=2400363)
    Event_12400797()
    Event_12405210(1, character=2400116, special_effect_id=5696)
    Event_12405210(2, character=2400122, special_effect_id=5696)
    Event_12405210(4, character=2400125, special_effect_id=5696)
    Event_12405210(5, character=2400127, special_effect_id=5696)
    Event_12405210(7, character=2400161, special_effect_id=5696)
    Event_12405220(0, character=2400137, special_effect_id=5552, special_effect_id_1=5553, special_effect_id_2=5554)
    Event_12405220(1, character=2400210, special_effect_id=5555, special_effect_id_1=5556, special_effect_id_2=0)
    Event_12405220(2, character=2400211, special_effect_id=5555, special_effect_id_1=5556, special_effect_id_2=0)
    Event_12404100(0, entity=2401900, action_button_id=7405, text=10012005)
    Event_12404100(1, entity=2401901, action_button_id=7406, text=10012006)
    AICommand(2400420, command_id=100, command_slot=0)
    Event_12405600(1, 2400400, 2402022, 5.0, 0.0)
    Event_12405600(2, 2400400, 2402017, 5.0, 0.0)
    Event_12405600(3, 2400126, 2402012, 5.0, 0.0)
    Event_12405600(4, 2400127, 2402013, 5.0, 0.0)
    Event_12405600(5, 2400128, 2402013, 5.0, 0.0)
    Event_12405600(6, 2400136, 2402015, 5.0, 0.0)
    Event_12405600(7, 2400137, 2402015, 5.0, 0.0)
    Event_12405600(8, 2400125, 2404302, 5.0, 0.0)
    Event_12405600(10, 2400231, 2404312, 5.0, 0.0)
    Event_12405600(11, 2400508, 2404320, 5.0, 0.0)
    Event_12405600(12, 2400508, 2404310, 5.0, 0.0)
    Event_12405600(13, 2400120, 2402073, 5.0, 0.0)
    Event_12405600(14, 2400121, 2402073, 5.0, 0.0)
    Event_12405600(15, 2400392, 2402016, 5.0, 0.0)
    Event_12405600(18, 2400401, 2402029, 5.0, 0.0)
    Event_12405600(19, 2400401, 2402017, 5.0, 0.0)
    Event_12405600(20, 2400106, 2404310, 5.0, 0.0)
    Event_12405600(22, 2400122, 2402081, 5.0, 0.0)
    Event_12405600(23, 2400116, 2404302, 5.0, 0.0)
    Event_12405600(24, 2400211, 2402075, 5.0, 0.0)
    Event_12405660()
    Event_12405350(
        0,
        character=2400391,
        region=2402310,
        region_1=2409015,
        patrol_information_id=2403105,
        region_2=2402311
    )
    Event_12405195()
    Event_12405370(0, character=2400210)
    Event_12405370(1, character=2400211)
    Event_12405670(0, 2400203, 2404332, 2404301, 5.0, 0.0)
    Event_12405330(0, character=2400500)
    Event_12405360()
    Event_12405365(0, character=2400374, region=2404087, patrol_information_id=2403108)
    Event_12405365(1, character=2400375, region=2404086, patrol_information_id=2403107)
    Event_12405850(0, character=2400450, obj=2401652, region=2402061, command_id=10, flag=12405521)
    Event_12405810(0, character=2400408, region=2402022, region_1=2404083, command_id=10, flag=12405520)
    Event_12405820(0, character=2400408, region=2404083)
    Event_12405820(1, character=2400450, region=2402061)
    Event_12405840(0, character=2400408, command_id=10, flag=12405520)
    Event_12405840(1, character=2400450, command_id=10, flag=12405521)
    Event_12405240()
    Event_12405241()
    Event_12405680()
    Event_12405682(0, 2400107, 2400002, 6.0, 12405686, 0.0)
    Event_12405682(2, 2400109, 2400001, 1.0, 12405688, 0.0)
    Event_12405682(3, 2400110, 2400004, 1.0, 12405689, 0.0)
    Event_12405140()
    Event_12405686(0, character=2400107)
    Event_12405686(2, character=2400109)
    Event_12405686(3, character=2400110)
    Event_12405690()
    Event_12405130(0, character=2400107, event_id=12405682, event_slot=0)
    Event_12405130(1, character=2400111, event_id=12405140, event_slot=0)
    Event_12405130(2, character=2400109, event_id=12405682, event_slot=2)
    Event_12405130(3, character=2400110, event_id=12405682, event_slot=3)
    Event_12405130(4, character=2400106, event_id=12405680, event_slot=0)
    Event_12405600(41, 2400410, 2402028, 3.0, 0.0)
    Event_12405600(42, 2400420, 2402511, 3.0, 0.0)
    Event_12405600(43, 2400423, 2402511, 3.0, 0.0)
    Event_12405600(44, 2400501, 2402157, 3.0, 0.0)
    Event_12405600(45, 2400502, 2402157, 3.0, 0.0)
    Event_12405600(46, 2400503, 2402157, 3.0, 0.0)
    Event_12405600(47, 2400504, 2402157, 3.0, 0.0)
    Event_12405600(48, 2400505, 2402157, 3.0, 0.0)
    Event_12405600(49, 2400506, 2402157, 3.0, 0.0)
    Event_12405600(50, 2400507, 2402157, 3.0, 0.0)
    Event_12405700()
    Event_12405701(0, character=2400398, region=2404370)
    Event_12405701(1, character=2400399, region=2404371)
    Event_12405600(52, 2400600, 2402500, 1.0, 0.0)
    Event_12405600(53, 2400601, 2402500, 1.0, 0.0)
    Event_12405600(54, 2400602, 2402500, 1.0, 0.0)
    Event_12405600(55, 2400603, 2402507, 5.0, 0.0)
    Event_12405600(56, 2400603, 2402508, 5.0, 0.0)
    Event_12405380(0, character=2400604, region=2402509, region_1=2402502)
    Event_12406900(0, region=2402103, anchor_entity=2402101, sound_id=20011001)
    Event_12406900(1, region=2402104, anchor_entity=2402101, sound_id=20011001)
    Event_12406900(3, region=2402107, anchor_entity=2402101, sound_id=20011001)
    Event_12406900(4, region=2404301, anchor_entity=2402101, sound_id=20011001)
    Event_12405000(
        0,
        character=2400205,
        animation_id=7010,
        animation_id_1=7013,
        ai_param_id=273150,
        ai_param_id_1=273140
    )
    Event_12405000(
        1,
        character=2400156,
        animation_id=7014,
        animation_id_1=7018,
        ai_param_id=263252,
        ai_param_id_1=263251
    )
    Event_12405010(0, character=2400205, animation_id=7012, event_slot=0, ai_param_id=273130)
    Event_12405010(1, character=2400156, animation_id=7015, event_slot=1, ai_param_id=263250)
    Event_12405020(
        0,
        character=2400207,
        animation_id=7010,
        animation_id_1=7013,
        ai_param_id=273120,
        ai_param_id_1=273110
    )
    Event_12405020(
        1,
        character=2400126,
        animation_id=7010,
        animation_id_1=7013,
        ai_param_id=273120,
        ai_param_id_1=273110
    )
    Event_12405020(
        2,
        character=2400203,
        animation_id=7010,
        animation_id_1=7013,
        ai_param_id=273120,
        ai_param_id_1=273110
    )
    Event_12405020(
        4,
        character=2400119,
        animation_id=7010,
        animation_id_1=7013,
        ai_param_id=273120,
        ai_param_id_1=273110
    )
    Event_12405030(0, character=2400207, animation_id=7012, event_slot=0, ai_param_id=273100)
    Event_12405030(1, character=2400126, animation_id=7012, event_slot=1, ai_param_id=273100)
    Event_12405030(2, character=2400203, animation_id=7012, event_slot=2, ai_param_id=273100)
    Event_12405030(4, character=2400119, animation_id=7012, event_slot=4, ai_param_id=273100)
    Event_12405335()
    Event_12405120(1, character=2400156, special_effect_id=5569)
    Event_12405120(2, character=2400162, special_effect_id=5569)
    Event_12405120(3, character=2400220, special_effect_id=5557)
    Event_12405120(4, character=2400116, special_effect_id=5557)
    Event_12405120(5, character=2400114, special_effect_id=5557)
    Event_12405120(6, character=2400127, special_effect_id=5557)
    Event_12405120(8, character=2400139, special_effect_id=5557)
    Event_12405120(9, character=2400137, special_effect_id=5557)
    Event_12405320()
    Event_12405250(0, flag=12400168, navmesh_id=2406790, flag_1=12405175)
    Event_12405251(0, flag=12400177, navmesh_id=2406791, flag_1=12400178)
    Event_12405251(1, flag=12400157, navmesh_id=2406792, flag_1=12405179)
    Event_12405259()
    Event_12405260()
    Event_12405262()
    Event_12400410()
    Event_12405263()
    Event_12405430(
        0,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405500,
        character=2400114
    )
    Event_12405430(
        1,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405500,
        character=2400114
    )
    Event_12405430(
        2,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405501,
        character=2400126
    )
    Event_12405430(
        3,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405501,
        character=2400126
    )
    Event_12405430(
        6,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405503,
        character=2400133
    )
    Event_12405430(
        7,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405503,
        character=2400133
    )
    Event_12405430(
        8,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405504,
        character=2400203
    )
    Event_12405430(
        9,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405504,
        character=2400203
    )
    Event_12405430(
        10,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405505,
        character=2400205
    )
    Event_12405430(
        11,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405505,
        character=2400205
    )
    Event_12405430(
        14,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405507,
        character=2400207
    )
    Event_12405430(
        15,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405507,
        character=2400207
    )
    Event_12405430(
        16,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405508,
        character=2400603
    )
    Event_12405430(
        17,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405508,
        character=2400603
    )
    Event_12405400(
        0,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect_id=5907,
        flag=12405500,
        flag_1=12405530,
        character=2400114
    )
    Event_12405400(
        1,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=12405500,
        flag_1=12405560,
        character=2400114
    )
    Event_12405400(
        2,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect_id=5907,
        flag=12405501,
        flag_1=12405531,
        character=2400126
    )
    Event_12405400(
        3,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=12405501,
        flag_1=12405561,
        character=2400126
    )
    Event_12405400(
        6,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect_id=5907,
        flag=12405503,
        flag_1=12405533,
        character=2400133
    )
    Event_12405400(
        7,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=12405503,
        flag_1=12405563,
        character=2400133
    )
    Event_12405400(
        8,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect_id=5907,
        flag=12405504,
        flag_1=12405534,
        character=2400203
    )
    Event_12405400(
        9,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=12405504,
        flag_1=12405564,
        character=2400203
    )
    Event_12405400(
        10,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect_id=5907,
        flag=12405505,
        flag_1=12405535,
        character=2400205
    )
    Event_12405400(
        11,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=12405505,
        flag_1=12405565,
        character=2400205
    )
    Event_12405400(
        14,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect_id=5907,
        flag=12405507,
        flag_1=12405537,
        character=2400207
    )
    Event_12405400(
        15,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=12405507,
        flag_1=12405567,
        character=2400207
    )
    Event_12405400(
        16,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect_id=5907,
        flag=12405508,
        flag_1=12405538,
        character=2400603
    )
    Event_12405400(
        17,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=12405508,
        flag_1=12405568,
        character=2400603
    )
    Event_12405460(0, tae_event_id=10, tae_event_id_1=40, flag=12405530, character=2400114, bit_index=0, bit_index_1=10)
    Event_12405460(1, tae_event_id=30, tae_event_id_1=40, flag=12405560, character=2400114, bit_index=1, bit_index_1=11)
    Event_12405460(2, tae_event_id=10, tae_event_id_1=40, flag=12405531, character=2400126, bit_index=0, bit_index_1=10)
    Event_12405460(3, tae_event_id=30, tae_event_id_1=40, flag=12405561, character=2400126, bit_index=1, bit_index_1=11)
    Event_12405460(6, tae_event_id=10, tae_event_id_1=40, flag=12405533, character=2400133, bit_index=0, bit_index_1=10)
    Event_12405460(7, tae_event_id=30, tae_event_id_1=40, flag=12405563, character=2400133, bit_index=1, bit_index_1=11)
    Event_12405460(8, tae_event_id=10, tae_event_id_1=40, flag=12405534, character=2400203, bit_index=0, bit_index_1=10)
    Event_12405460(9, tae_event_id=30, tae_event_id_1=40, flag=12405564, character=2400203, bit_index=1, bit_index_1=11)
    Event_12405460(10, tae_event_id=10, tae_event_id_1=40, flag=12405535, character=2400205, bit_index=0, bit_index_1=10)
    Event_12405460(11, tae_event_id=30, tae_event_id_1=40, flag=12405565, character=2400205, bit_index=1, bit_index_1=11)
    Event_12405460(14, tae_event_id=10, tae_event_id_1=40, flag=12405537, character=2400207, bit_index=0, bit_index_1=10)
    Event_12405460(15, tae_event_id=30, tae_event_id_1=40, flag=12405567, character=2400207, bit_index=1, bit_index_1=11)
    Event_12405460(16, tae_event_id=10, tae_event_id_1=40, flag=12405538, character=2400603, bit_index=0, bit_index_1=10)
    Event_12405460(17, tae_event_id=30, tae_event_id_1=40, flag=12405568, character=2400603, bit_index=1, bit_index_1=11)
    Event_12405790(0, obj=2401150, flag=9802, model_point=924110)
    Event_12405790(1, obj=2401151, flag=9801, model_point=924110)
    Event_12405790(2, obj=2401152, flag=6001, model_point=924113)
    Event_12405790(3, obj=2401153, flag=9802, model_point=924110)
    Event_12405790(4, obj=2401154, flag=9801, model_point=924113)
    Event_12405800(0, sound_id=2403310, flag=1439, flag_1=70000052, flag_2=9802)
    Event_12405800(1, sound_id=2403311, flag=1439, flag_1=70000053, flag_2=9801)
    Event_12405800(2, sound_id=2403312, flag=1439, flag_1=70000054, flag_2=6001)
    Event_12405800(3, sound_id=2403313, flag=1439, flag_1=70000072, flag_2=9802)
    Event_12405800(4, sound_id=2403314, flag=1439, flag_1=70000073, flag_2=9801)
    Event_12404842()
    Event_12404843()
    Event_12401800()
    Event_12401801()
    Event_12401802()
    Event_12401803()
    Event_12404840()
    Event_12404841()
    Event_12404802()
    Event_12404803()
    Event_12404804()
    Event_12404805()
    Event_12404807()
    Event_12404808()
    Event_12404830()
    Event_12401804()
    Event_12404810(
        0,
        npc_part_id=2400,
        npc_part_id_1=2400,
        part_index=1,
        part_health=80,
        special_effect_id=480,
        special_effect_id_1=490,
        animation_id=8020
    )
    Event_12404810(
        1,
        npc_part_id=2401,
        npc_part_id_1=2401,
        part_index=2,
        part_health=150,
        special_effect_id=481,
        special_effect_id_1=491,
        animation_id=8000
    )
    Event_12404810(
        2,
        npc_part_id=2402,
        npc_part_id_1=2402,
        part_index=3,
        part_health=150,
        special_effect_id=482,
        special_effect_id_1=492,
        animation_id=8010
    )
    Event_12404810(
        3,
        npc_part_id=2403,
        npc_part_id_1=2403,
        part_index=4,
        part_health=200,
        special_effect_id=483,
        special_effect_id_1=493,
        animation_id=8030
    )
    Event_12404810(
        4,
        npc_part_id=2404,
        npc_part_id_1=2404,
        part_index=5,
        part_health=200,
        special_effect_id=484,
        special_effect_id_1=494,
        animation_id=8040
    )
    Event_12404820(0, special_effect=480, special_effect_1=490, bit_index=5, bit_index_1=10)
    Event_12404820(1, special_effect=481, special_effect_1=491, bit_index=6, bit_index_1=11)
    Event_12404820(2, special_effect=482, special_effect_1=492, bit_index=7, bit_index_1=12)
    Event_12404820(3, special_effect=483, special_effect_1=493, bit_index=8, bit_index_1=13)
    Event_12404820(4, special_effect=484, special_effect_1=494, bit_index=9, bit_index_1=14)
    Event_12400800()
    Event_12400801()
    Event_12400840(1, flag=70000052, action_button_id=6030, destination=2400860)
    Event_12400840(2, flag=70000053, action_button_id=6030, destination=2400861)
    Event_12400840(3, flag=70000054, action_button_id=6030, destination=2400862)
    Event_12400840(4, flag=70000072, action_button_id=6030, destination=2400863)
    Event_12400840(5, flag=70000073, action_button_id=6030, destination=2400864)
    Event_12400840(6, flag=72400513, action_button_id=6030, destination=2400749)
    Event_12400630(0, character=2400765)
    Event_12400630(1, character=2400730)
    Event_12400630(2, character=2400754)
    Event_12400630(3, character=2400757)
    Event_12400630(4, character=2400750)
    Event_12400630(5, character=2400770)
    Event_12400630(6, character=2400772)
    Event_12400630(7, character=2400774)
    Event_12400630(8, character=2400700)
    Event_12400501()
    RunEvent(12400504, slot=0, args=(0,))
    Event_12400507()
    Event_12400512()
    Event_12400508()
    Event_12400513()
    Event_12400514()
    Event_12400505()
    Event_12400901()
    Event_12400903()
    Event_12400904()
    Event_12400952()
    Event_12400953()
    Event_12400954()
    Event_12400940(0, character=2400770)
    Event_12400940(1, character=2400774)
    Event_12400910(0, character=2400770)
    Event_12400910(1, character=2400772)
    Event_12400910(2, character=2400774)
    Event_12400915(0, character=2400770)
    Event_12400915(1, character=2400772)
    Event_12400915(2, character=2400774)
    Event_12400920(0, character=2400770)
    Event_12400920(1, character=2400774)
    Event_12400925(0, character=2400770)
    Event_12400925(1, character=2400772)
    Event_12400925(2, character=2400774)
    Event_12400930(0, character=2400770)
    Event_12400930(1, character=2400774)
    Event_12400935(0, character=2400770)
    Event_12400935(1, character=2400774)
    Event_12400521()
    Event_12400525()
    Event_12400523()
    Event_12400524()
    Event_12400531()
    Event_12400522()
    Event_12400810(0, character=2400750, animation_id=103085)
    Event_12400810(1, character=2400754, animation_id=103088)
    Event_12400810(2, character=2400757, animation_id=103088)
    Event_12400810(3, character=2400758, animation_id=103089)
    Event_12400805(0, character=2400750, animation_id=103080, special_effect=151)
    Event_12400805(1, character=2400754, animation_id=103081, special_effect=152)
    Event_12400805(2, character=2400757, animation_id=103081, special_effect=152)
    Event_12400805(3, character=2400758, animation_id=103082, special_effect=153)
    Event_12400830(0, character=2400750, animation_id=103086)
    Event_12400830(1, character=2400754, animation_id=103086)
    Event_12400830(2, character=2400757, animation_id=103086)
    Event_12400830(3, character=2400758, animation_id=103086)
    Event_12400610()
    Event_12400611()
    Event_12405150(0, character=2400755, flag=12405155)
    Event_12405150(1, character=2400759, flag=12405156)
    Event_12400612(0, character=2400755, flag=12405155)
    Event_12400612(1, character=2400759, flag=12405156)
    Event_12400614(0, character=2400755, animation_id=103076)
    Event_12400614(1, character=2400759, animation_id=103076)
    Event_12400616(0, character=2400755)
    Event_12400616(1, character=2400759)
    Event_12400618(0, character=2400755)
    Event_12400618(1, character=2400759)
    Event_12400620(0, character=2400755)
    Event_12400620(1, character=2400759)
    Event_12400625(0, character=2400755, flag=12405155)
    Event_12400627(0, character=2400755, flag=12405155)
    Event_12400627(1, character=2400759, flag=12405156)
    Event_12405157()
    Event_12405158()
    Event_12405159()
    Event_12400561()
    Event_12400563()
    Event_12400564()
    Event_12400565()
    Event_12400566()
    Event_12400567()
    Event_12400569()
    Event_12400570()
    Event_12400571()
    Event_12400572()
    Event_12400568()
    DisableFlag(72400310)
    DisableFlag(72400311)
    SetTeamType(2400700, TeamType.Ally)
    Event_12400701()
    Event_12400702()
    Event_12400703()
    Event_12400704()
    Event_12400705()
    Event_12400706()
    Event_12400707()
    Event_12400708(0, flag=1164, flag_1=72400316, flag_2=1163, flag_3=1161, left=0)
    Event_12400708(1, flag=1181, flag_1=72400317, flag_2=1190, flag_3=1183, left=0)
    Event_12400708(2, flag=1304, flag_1=72400318, flag_2=1309, flag_3=1303, left=1)
    Event_12400708(3, flag=1224, flag_1=72400319, flag_2=1223, flag_3=1222, left=0)
    Event_12400713(0, flag=1164, flag_1=1163)
    Event_12400713(1, flag=1181, flag_1=1190)
    Event_12400713(2, flag=1304, flag_1=1309)
    Event_12400713(3, flag=1224, flag_1=1223)
    Event_12400720()
    Event_12400721()
    Event_12400722()
    Event_12400723()
    Event_12400728()
    Event_12400729()
    Event_12400730()
    Event_12400731()
    Event_12400732(slot=3)
    Event_12400737()
    Event_12400738()
    Event_12400580()
    Event_12400581()
    Event_12400582()
    Event_12400401()
    Event_12400402()
    Event_12400403()
    Event_12400591()
    Event_12400592(0, attacked_entity=2400760, flag=72400475)
    Event_12400592(1, attacked_entity=2400763, flag=72400476)
    Event_12400593(0, character=2400760, flag=1341, flag_1=72400475)
    Event_12400593(1, character=2400763, flag=1345, flag_1=72400476)
    Event_12400594(0, character=2400760, flag=1342)
    Event_12400594(1, character=2400763, flag=1346)
    Event_12405271()
    Event_12405272()
    Event_12400990()
    GotoIfFlagDisabled(Label.L0, flag=12401800)
    DisableMapCollision(collision=2404121)

    # --- 0 --- #
    DefineLabel(0)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
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
    Event_12404000()
    Event_12400500()
    Event_12400560()
    Event_12400900()
    Event_12400520()
    Event_12400622()
    Event_12400624()
    Event_12400629()
    Event_12400650()
    Event_12400700()
    Event_12400590()
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


@RestartOnRest(12404000)
def Event_12404000():
    """Event 12404000"""
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerInsightAmountLessThan(2, value=50)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    EnableFlag(12404001)
    EnableFlag(12404002)
    EnableFlag(12404003)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfPlayerInsightAmountLessThan(3, value=40)
    GotoIfConditionTrue(Label.L1, input_condition=3)
    EnableFlag(12404001)
    EnableFlag(12404002)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfPlayerInsightAmountLessThan(4, value=15)
    EndIfConditionTrue(4)
    EnableFlag(12404002)


@NeverRestart(12404100)
def Event_12404100(_, entity: int, action_button_id: int, text: int):
    """Event 12404100"""
    DisableNetworkSync()
    IfActionButtonParamActivated(0, action_button_id=action_button_id, entity=entity)
    DisplayDialog(text=text, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12400070)
def Event_12400070(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 12400070"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@NeverRestart(12400080)
def Event_12400080(_, entity: int, flag: int, flag_1: int, action_button_id: int):
    """Event 12400080"""
    DisableNetworkSync()
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    IfActionButtonParamActivated(2, action_button_id=action_button_id, entity=entity)
    IfFlagState(3, FlagState.Change, FlagType.Absolute, flag)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    DisplayDialog(text=10010160, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12400095)
def Event_12400095(_, entity: int):
    """Event 12400095"""
    DisableNetworkSync()
    IfActionButtonParamActivated(0, action_button_id=2400040, entity=entity)
    DisplayDialog(text=10010171, anchor_entity=PLAYER, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12400100)
def Event_12400100(_, obj: int, obj_act_id: int, obj_act_id_1: int, obj_act_id_2: int):
    """Event 12400100"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)


@NeverRestart(12400125)
def Event_12400125():
    """Event 12400125"""
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
    CreateObjectVFX(2401207, vfx_id=200, model_point=920204)
    CreateObjectVFX(2401207, vfx_id=201, model_point=920205)
    Wait(3.0)
    DisableFlag(12400178)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    Restart()


@NeverRestart(12400126)
def Event_12400126():
    """Event 12400126"""
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
    CreateObjectVFX(2401207, vfx_id=200, model_point=920204)
    CreateObjectVFX(2401207, vfx_id=201, model_point=920205)
    Wait(3.0)
    DisableFlag(12400178)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    Restart()


@NeverRestart(12400127)
def Event_12400127():
    """Event 12400127"""
    DisableNetworkSync()
    IfFlagEnabled(1, 12400178)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2401006)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12400128)
def Event_12400128():
    """Event 12400128"""
    GotoIfFlagEnabled(Label.L0, flag=12400177)
    EndOfAnimation(obj=2401207, animation_id=2)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2401207, animation_id=1)
    EnableObjectActivation(2401006, obj_act_id=2400000)


@NeverRestart(12400130)
def Event_12400130(_, obj: int, animation_id: int, obj_act_id: int, flag: int):
    """Event 12400130"""
    SkipLinesIfFlagDisabled(4, flag)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=-1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=0)


@NeverRestart(12400146)
def Event_12400146():
    """Event 12400146"""
    IfFlagEnabled(1, 12400150)
    IfFlagDisabled(2, 12400150)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, condition=1)
    EndOfAnimation(obj=2401101, animation_id=15)
    EnableObjectActivation(2401003, obj_act_id=2400000)
    DisableObjectActivation(2401004, obj_act_id=2400000)
    SkipLines(3)
    EndOfAnimation(obj=2401101, animation_id=0)
    DisableObjectActivation(2401003, obj_act_id=2400000)
    EnableObjectActivation(2401004, obj_act_id=2400000)


@NeverRestart(12400147)
def Event_12400147():
    """Event 12400147"""
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


@NeverRestart(12400148)
def Event_12400148():
    """Event 12400148"""
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


@NeverRestart(12400149)
def Event_12400149():
    """Event 12400149"""
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
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12400155)
def Event_12400155():
    """Event 12400155"""
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
    CreateObjectVFX(2401208, vfx_id=200, model_point=920204)
    CreateObjectVFX(2401208, vfx_id=201, model_point=920205)
    Wait(3.0)
    DisableFlag(12405179)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    Restart()


@NeverRestart(12400156)
def Event_12400156():
    """Event 12400156"""
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
    CreateObjectVFX(2401208, vfx_id=200, model_point=920204)
    CreateObjectVFX(2401208, vfx_id=201, model_point=920205)
    Wait(3.0)
    DisableFlag(12405179)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    Restart()


@NeverRestart(12400158)
def Event_12400158():
    """Event 12400158"""
    DisableNetworkSync()
    IfFlagEnabled(1, 12405179)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2401008)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12400159)
def Event_12400159():
    """Event 12400159"""
    GotoIfFlagEnabled(Label.L0, flag=12400157)
    EndOfAnimation(obj=2401208, animation_id=2)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2401208, animation_id=1)
    EnableObjectActivation(2401008, obj_act_id=2400000)


@RestartOnRest(12400760)
def Event_12400760():
    """Event 12400760"""
    GotoIfFlagDisabled(Label.L0, flag=12400160)
    ForceAnimation(2400650, 7020, loop=True)
    EndOfAnimation(obj=2401220, animation_id=1)
    DisableObjectActivation(2401014, obj_act_id=2400000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2400650, 7022, loop=True)
    IfPlayerDoesNotHaveGood(1, 4011)
    IfActionButtonParamActivated(1, action_button_id=2400030, entity=2401220)
    IfPlayerHasGood(2, 4011)
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
    WaitFrames(frames=74)
    ForceAnimation(2400650, 7020, loop=True)
    WaitFrames(frames=31)
    ForceAnimation(2401220, 1)
    WaitFrames(frames=30)
    CreateObjectVFX(2401220, vfx_id=200, model_point=920204)
    CreateObjectVFX(2401220, vfx_id=201, model_point=920205)
    EnableFlag(12400160)
    EndIfFlagEnabled(12401800)
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
    WaitFrames(frames=105)
    ForceAnimation(2401220, 1)
    WaitFrames(frames=24)
    ForceAnimation(2400650, 7022, loop=True)
    WaitFrames(frames=6)
    CreateObjectVFX(2401220, vfx_id=200, model_point=920204)
    CreateObjectVFX(2401220, vfx_id=201, model_point=920205)
    DisplayDialog(text=10010174, number_buttons=NumberButtons.OneButton)
    EnableFlag(12400160)
    EndIfFlagEnabled(12401800)
    DisableFlag(2400)
    DisableFlag(2401)
    DisableFlag(2405)
    DisableFlag(2406)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisplayDialog(text=10010173, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12400161)
def Event_12400161():
    """Event 12400161"""
    DisableNetworkSync()
    IfFlagEnabled(1, 12400160)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2401014)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12400174)
def Event_12400174():
    """Event 12400174"""
    GotoIfFlagEnabled(Label.L0, flag=12400168)
    EnableFlag(12400167)

    # --- 0 --- #
    DefineLabel(0)


@NeverRestart(12400175)
def Event_12400175():
    """Event 12400175"""
    GotoIfFlagDisabled(Label.L0, flag=12400168)
    EndOfAnimation(obj=2401209, animation_id=2)
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
    CreateObjectVFX(2401209, vfx_id=200, model_point=920204)
    CreateObjectVFX(2401209, vfx_id=201, model_point=920205)
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
    CreateObjectVFX(2401209, vfx_id=200, model_point=920204)
    CreateObjectVFX(2401209, vfx_id=201, model_point=920205)
    Wait(3.0)
    DisableFlag(12400169)
    DisableFlag(12405175)
    EnableObjectActivation(2401015, obj_act_id=2400000)
    EnableObjectActivation(2401016, obj_act_id=2400000)
    Restart()


@RestartOnRest(12400179)
def Event_12400179(_, entity: int):
    """Event 12400179"""
    DisableNetworkSync()
    IfFlagEnabled(1, 12405175)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=entity)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, display_distance=0.0, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12400185)
def Event_12400185():
    """Event 12400185"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2401012, animation_id=1)
    DisableObjectActivation(2401013, obj_act_id=2400000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=12400123)
    ForceAnimation(2401012, 1)


@NeverRestart(12400200)
def Event_12400200(_, character: int, flag: int):
    """Event 12400200"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@NeverRestart(12400250)
def Event_12400250(_, obj_act_id: int, text: int, anchor_entity: int):
    """Event 12400250"""
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    DisplayDialog(text=text, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)


@NeverRestart(12400300)
def Event_12400300():
    """Event 12400300"""
    GotoIfFlagEnabled(Label.L2, flag=9802)
    GotoIfFlagEnabled(Label.L1, flag=9801)
    GotoIfFlagEnabled(Label.L0, flag=9800)

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2404000)
    DisableMapPiece(map_piece_id=2404001)
    DisableMapPiece(map_piece_id=2404002)
    DisableCharacter(2400321)
    DisableCharacter(2400322)
    DisableMapPiece(map_piece_id=2404750)
    DisableMapPiece(map_piece_id=2404751)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    DisableMapPiece(map_piece_id=2404000)
    EnableMapPiece(map_piece_id=2404001)
    DisableMapPiece(map_piece_id=2404002)
    EnableCharacter(2400321)
    EnableCharacter(2400322)
    DisableBackread(2400350)
    DisableBackread(2400351)
    DisableBackread(2400352)
    DisableBackread(2400220)
    DisableBackread(2400116)
    DisableBackread(2400125)
    DisableMapPiece(map_piece_id=2404700)
    DisableMapPiece(map_piece_id=2404701)
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
    DisableMapPiece(map_piece_id=2404000)
    DisableMapPiece(map_piece_id=2404001)
    EnableMapPiece(map_piece_id=2404002)
    EnableCharacter(2400321)
    EnableCharacter(2400322)
    DisableBackread(2400350)
    DisableBackread(2400351)
    DisableBackread(2400352)
    DisableBackread(2400220)
    DisableBackread(2400116)
    DisableBackread(2400125)
    DisableMapPiece(map_piece_id=2404700)
    DisableMapPiece(map_piece_id=2404701)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagState(-1, FlagState.Change, FlagType.Absolute, 9800)
    IfFlagState(-1, FlagState.Change, FlagType.Absolute, 9801)
    IfFlagState(-1, FlagState.Change, FlagType.Absolute, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@NeverRestart(12400765)
def Event_12400765():
    """Event 12400765"""
    IfFlagEnabled(-1, 9802)
    IfFlagEnabled(-1, 12404001)
    GotoIfConditionTrue(Label.L0, input_condition=-1)
    DisableObject(2400898)
    ForceAnimation(2400898, 0, loop=True)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.On)
    AddSpecialEffect(2400899, 5686)
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


@RestartOnRest(12400350)
def Event_12400350(_, obj: int, obj_act_id: int):
    """Event 12400350"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=-1)
    EnableTreasure(obj=obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(12400401)
def Event_12400401():
    """Event 12400401"""
    IfFlagEnabled(1, 72400440)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1400, 1402))
    EnableFlag(1401)
    ForceAnimation(2401200, 1, wait_for_completion=True)
    EnableFlag(12400131)
    SaveRequest()


@NeverRestart(12400402)
def Event_12400402():
    """Event 12400402"""
    IfFlagEnabled(1, 72400440)
    IfConditionTrue(0, input_condition=1)
    Move(2400830, destination=2402033, destination_type=CoordEntityType.Region, short_move=True)


@NeverRestart(12400403)
def Event_12400403():
    """Event 12400403"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 72400441)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(37000, host_only=False)


@NeverRestart(12400410)
def Event_12400410():
    """Event 12400410"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfCharacterHasSpecialEffect(0, PLAYER, 6421)
    RunEvent(9350, slot=0, args=(1,))


@NeverRestart(12400420)
def Event_12400420():
    """Event 12400420"""
    DisableSoundEvent(sound_id=2406831)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 9801)
    Wait(4.0)
    EnableSoundEvent(sound_id=2406831)


@NeverRestart(12400750)
def Event_12400750():
    """Event 12400750"""
    DisableSoundEvent(sound_id=2406832)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfActionButtonParamActivated(0, action_button_id=7030, entity=2401210)
    EnableFlag(9180)
    WaitFrames(frames=1)
    PlayCutsceneAndMovePlayerAndSetTimePeriod(
        cutscene=24000020,
        cutscene_flags=0,
        move_to_region=2402200,
        game_map=CATHEDRAL_WARD,
        player_id=10000,
        time_period_id=1,
    )
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableSoundEvent(sound_id=2406832)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2401210, animation_id=2)
    NotifyDoorEventSoundDampening(obj=2401210, state=DoorState.DoorOpening)


@RestartOnRest(12400780)
def Event_12400780(_, attacker__character: int):
    """Event 12400780"""
    IfCharacterHuman(2, PLAYER)
    EndIfConditionFalse(2)
    IfCharacterAlive(1, attacker__character)
    IfAttacked(1, attacked_entity=PLAYER, attacker=attacker__character)
    IfHealthEqual(1, PLAYER, value=0.0)
    IfFlagEnabled(1, 9401)
    IfFlagEnabled(1, 9404)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9420)


@RestartOnRest(12400791)
def Event_12400791(_, character: int):
    """Event 12400791"""
    GotoIfFlagEnabled(Label.L0, flag=9802)
    EndIfFlagEnabled(9453)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(character)


@RestartOnRest(12400797)
def Event_12400797():
    """Event 12400797"""
    GotoIfFlagEnabled(Label.L0, flag=9802)
    SkipLinesIfFlagDisabled(4, 9453)
    DisableBackread(2400350)
    DisableBackread(2400351)
    DisableBackread(2400352)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2400362)


@NeverRestart(12400823)
def Event_12400823():
    """Event 12400823"""
    IfFlagEnabled(1, 12400827)
    IfFlagDisabled(2, 12400827)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, condition=1)
    EndOfAnimation(obj=2401102, animation_id=30)
    EnableObjectActivation(2401104, obj_act_id=2400000)
    DisableObjectActivation(2401103, obj_act_id=2400000)
    SkipLines(3)
    EndOfAnimation(obj=2401102, animation_id=0)
    DisableObjectActivation(2401104, obj_act_id=2400000)
    EnableObjectActivation(2401103, obj_act_id=2400000)


@NeverRestart(12400824)
def Event_12400824():
    """Event 12400824"""
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


@NeverRestart(12400825)
def Event_12400825():
    """Event 12400825"""
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


@NeverRestart(12400826)
def Event_12400826():
    """Event 12400826"""
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
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12400850)
def Event_12400850(
    _,
    vfx_id: int,
    vfx_id_1: int,
    vfx_id_2: int,
    flag: int,
    obj_act_id: int,
    seconds: float,
    anchor_entity: int,
    vfx_id_3: int,
):
    """Event 12400850"""
    DeleteVFX(vfx_id, erase_root_only=False)
    DeleteVFX(vfx_id_1, erase_root_only=False)
    DeleteVFX(vfx_id_2, erase_root_only=False)
    SkipLinesIfFlagDisabled(3, flag)
    CreateVFX(vfx_id_1)
    CreateVFX(vfx_id_2)
    End()
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(seconds)
    CreateVFX(vfx_id)
    CreateTemporaryVFX(vfx_id=vfx_id_3, anchor_entity=anchor_entity, anchor_type=CoordEntityType.Region)
    Wait(4.0)
    CreateVFX(vfx_id_1)
    CreateVFX(vfx_id_2)


@RestartOnRest(12400854)
def Event_12400854():
    """Event 12400854"""
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
    CreateTemporaryVFX(vfx_id=920206, anchor_entity=2401204, model_point=200, anchor_type=CoordEntityType.Object)
    CreateTemporaryVFX(vfx_id=920207, anchor_entity=2401204, model_point=201, anchor_type=CoordEntityType.Object)
    Wait(4.0)
    CreateVFX(2406712)
    CreateVFX(2406713)


@RestartOnRest(12405000)
def Event_12405000(_, character: int, animation_id: int, animation_id_1: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12405000"""
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id, loop=True)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=character, radius=3.0)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ForceAnimation(character, animation_id_1, loop=True)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest(12405010)
def Event_12405010(_, character: int, animation_id: int, event_slot: int, ai_param_id: int):
    """Event 12405010"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id)
    StopEvent(event_id=12405000, event_slot=event_slot)


@NeverRestart(12405020)
def Event_12405020(_, character: int, animation_id: int, animation_id_1: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12405020"""
    IfFlagEnabled(0, 9801)
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id, loop=True)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=character, radius=1.0)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ForceAnimation(character, animation_id_1, loop=True)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Normal)
    Restart()


@NeverRestart(12405030)
def Event_12405030(_, character: int, animation_id: int, event_slot: int, ai_param_id: int):
    """Event 12405030"""
    IfFlagEnabled(0, 9801)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id)
    StopEvent(event_id=12405020, event_slot=event_slot)


@RestartOnRest(12405060)
def Event_12405060(_, character: int, animation_id: int, animation_id_1: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12405060"""
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id, loop=True)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=3.0)
    IfHasAIStatus(1, 2400160, ai_status=AIStatusType.Battle)
    IfAttacked(2, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    ForceAnimation(character, animation_id_1)


@RestartOnRest(12405080)
def Event_12405080(_, flag: int, character: int, region: int, radius: float):
    """Event 12405080"""
    IfFlagEnabled(0, flag)
    AICommand(character, command_id=10, command_slot=0)
    SetNest(character, region=region)
    IfCharacterInsideRegion(-1, character, region=region)
    IfEntityWithinDistance(-1, entity=character, other_entity=PLAYER, radius=radius)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405100)
def Event_12405100(_, character: int, region: int, region_1: int):
    """Event 12405100"""
    IfCharacterInsideRegion(1, PLAYER, region=2404306)
    IfFlagEnabled(2, 12405431)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(3, input_condition=-1)
    IfHasAIStatus(3, character, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=3)
    DisableAI(character)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    SetNest(character, region=region)
    SkipLinesIfFinishedConditionTrue(1, condition=1)
    SetNest(character, region=region_1)
    AICommand(character, command_id=10, command_slot=0)
    EnableAI(character)
    ReplanAI(character)
    IfCharacterInsideRegion(-2, character, region=region)
    IfCharacterInsideRegion(-2, character, region=region_1)
    IfConditionTrue(0, input_condition=-2)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405110)
def Event_12405110(
    _,
    region: int,
    obj: int,
    vfx_id: int,
    obj__source_entity: int,
    launch_angle_y: int,
    flag: int,
    name: int,
):
    """Event 12405110"""
    IfObjectNotDestroyed(0, obj__source_entity)
    DisableFlag(flag)
    SkipLinesIfFlagDisabled(2, flag)
    EndOfAnimation(obj=obj, animation_id=0)
    SkipLines(9)
    IfCharacterInsideRegion(-1, PLAYER, region=region)
    IfObjectNotDestroyed(1, obj__source_entity)
    IfConditionTrue(1, input_condition=-1)
    IfObjectDestroyed(2, obj__source_entity)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    SkipLinesIfFinishedConditionTrue(2, condition=1)
    ForceAnimation(obj, 0, wait_for_completion=True)
    End()
    PlaySoundEffect(obj, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(obj, 0, wait_for_completion=True)
    EnableFlag(flag)
    CreateTemporaryVFX(vfx_id=150005, anchor_entity=obj, model_point=101, anchor_type=CoordEntityType.Object)
    DeleteVFX(vfx_id, erase_root_only=False)
    EndIfFinishedConditionTrue(input_condition=2)
    Wait(0.20000000298023224)
    CreatePlayLog(name=name)
    ShootProjectile(
        owner_entity=2400000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=5071,
        launch_angle_x=0,
        launch_angle_y=launch_angle_y,
        launch_angle_z=0,
    )
    PlaySoundEffect(obj__source_entity, 243007000, sound_type=SoundType.a_Ambient)
    CreateTemporaryVFX(
        vfx_id=929208,
        anchor_entity=obj__source_entity,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=2400000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=5071,
        launch_angle_x=0,
        launch_angle_y=launch_angle_y,
        launch_angle_z=0,
    )
    PlaySoundEffect(obj__source_entity, 243007000, sound_type=SoundType.a_Ambient)
    CreateTemporaryVFX(
        vfx_id=929208,
        anchor_entity=obj__source_entity,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=2400000,
        source_entity=obj__source_entity,
        model_point=101,
        behavior_id=5071,
        launch_angle_x=0,
        launch_angle_y=launch_angle_y,
        launch_angle_z=0,
    )
    PlaySoundEffect(obj__source_entity, 243007000, sound_type=SoundType.a_Ambient)
    CreateTemporaryVFX(
        vfx_id=929208,
        anchor_entity=obj__source_entity,
        model_point=101,
        anchor_type=CoordEntityType.Object,
    )
    Wait(3.0)
    IfCharacterOutsideRegion(3, PLAYER, region=region)
    IfObjectNotDestroyed(3, obj__source_entity)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    PlaySoundEffect(obj__source_entity, 243007001, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(obj, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(obj, 1, wait_for_completion=True)
    Restart()


@NeverRestart(12405120)
def Event_12405120(_, character: int, special_effect_id: int):
    """Event 12405120"""
    WaitFrames(frames=1)
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(12405130)
def Event_12405130(_, character: int, event_id: int, event_slot: int):
    """Event 12405130"""
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2402151)
    IfConditionTrue(0, input_condition=1)
    EnableAI(character)
    StopEvent(event_id=event_id, event_slot=event_slot)


@RestartOnRest(12405140)
def Event_12405140():
    """Event 12405140"""
    GotoIfThisEventFlagDisabled(Label.L0)
    SetAIParamID(2400111, ai_param_id=263381)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterBackreadEnabled(0, 2400111)
    DisableAI(2400111)
    IfFlagEnabled(1, 12405681)
    IfAttackedWithDamageType(2, attacked_entity=2400111, attacker=PLAYER)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(3, input_condition=-1)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=2400111, radius=5.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2400111)
    EndIfFinishedConditionFalse(input_condition=1)
    SetAIParamID(2400111, ai_param_id=263380)
    IfCharacterInsideRegion(-2, 2400111, region=2402046)
    IfAttackedWithDamageType(-2, attacked_entity=2400111, attacker=PLAYER)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=2400111, radius=5.0)
    IfConditionTrue(0, input_condition=-2)
    SetAIParamID(2400111, ai_param_id=263381)
    ReplanAI(2400111)


@NeverRestart(12405150)
def Event_12405150(_, character: int, flag: int):
    """Event 12405150"""
    WaitFrames(frames=10)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndIfFlagEnabled(1210)
    EnableBackread(2400756)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, flag)
    EnableBackread(2400756)
    EnableInvincibility(character)
    IfCharacterBackreadEnabled(0, 2400756)
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionTrue(Label.L1, input_condition=15)
    WaitFrames(frames=60)
    DisableBackread(character)
    End()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 103073, wait_for_completion=True)
    DisableBackread(character)
    MoveToEntity(2400756, destination=2404507, destination_type=CoordEntityType.Region)
    EnableGravity(2400756)
    ForceAnimation(2400756, 3030)
    EnableAI(2400756)
    SetNest(2400756, region=2404507)
    DisableFlagRange((1200, 1219))
    EnableFlag(1207)
    EnableFlag(9432)
    SaveRequest()


@NeverRestart(12405157)
def Event_12405157():
    """Event 12405157"""
    IfCharacterHasSpecialEffect(-1, 2400755, 153)
    IfCharacterHasSpecialEffect(-1, 2400759, 153)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=0)


@NeverRestart(12405158)
def Event_12405158():
    """Event 12405158"""
    IfEventValueNotEqual(0, flag=72400372, bit_count=2, value=0)
    WaitFrames(frames=0)


@NeverRestart(12405159)
def Event_12405159():
    """Event 12405159"""
    IfCharacterHasSpecialEffect(0, 2400760, 151)
    IfCharacterDoesNotHaveSpecialEffect(0, 2400760, 151)
    IfCharacterBackreadDisabled(2, 2400760)
    RestartIfConditionTrue(2)
    EnableFlag(12405160)


@RestartOnRest(12405195)
def Event_12405195():
    """Event 12405195"""
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


@RestartOnRest(12405200)
def Event_12405200():
    """Event 12405200"""
    IfFlagDisabled(0, 12400168)
    WaitFrames(frames=1)
    ActivateObjectWithSpecificCharacter(obj=2401015, objact_id=2400000, relative_index=-1, character=2400113)
    Restart()


@RestartOnRest(12405210)
def Event_12405210(_, character: int, special_effect_id: int):
    """Event 12405210"""
    IfFlagDisabled(1, 12404002)
    EndIfConditionTrue(1)
    SetDisplayMask(character, bit_index=3, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=4, switch_type=OnOffChange.Off)
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(12405220)
def Event_12405220(_, character: int, special_effect_id: int, special_effect_id_1: int, special_effect_id_2: int):
    """Event 12405220"""
    IfFlagDisabled(1, 12404002)
    EndIfConditionTrue(1)
    AddSpecialEffect(character, special_effect_id)
    AddSpecialEffect(character, special_effect_id_1)
    AddSpecialEffect(character, special_effect_id_2)


@RestartOnRest(12405240)
def Event_12405240():
    """Event 12405240"""
    IfCharacterInsideRegion(1, 2400203, region=2404311)
    IfCharacterInsideRegion(2, PLAYER, region=2404311)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(5, input_condition=-1)
    IfCharacterNotTargeting(3, targeting_character=2400203, targeted_character=PLAYER)
    IfCharacterTargeting(4, targeting_character=2400203, targeted_character=PLAYER)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(5, input_condition=-2)
    IfFlagDisabled(5, 9801)
    IfConditionTrue(0, input_condition=5)
    PlaySoundEffect(2404290, 20011002, sound_type=SoundType.a_Ambient)
    WaitFrames(frames=40)
    EndIfFinishedConditionTrue(input_condition=4)
    ForceAnimation(2400203, 3039)


@RestartOnRest(12405241)
def Event_12405241():
    """Event 12405241"""
    IfFlagEnabled(1, 12404003)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableBackread(2400650)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableBackread(2400650)


@RestartOnRest(12405250)
def Event_12405250(_, flag: int, navmesh_id: int, flag_1: int):
    """Event 12405250"""
    IfFlagDisabled(1, flag)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    SkipLines(1)
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(0, flag_1)
    Restart()


@RestartOnRest(12405251)
def Event_12405251(_, flag: int, navmesh_id: int, flag_1: int):
    """Event 12405251"""
    IfFlagEnabled(1, flag)
    IfFlagDisabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    DisableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    SkipLines(1)
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)
    IfFlagEnabled(0, flag_1)
    Restart()


@RestartOnRest(12405259)
def Event_12405259():
    """Event 12405259"""
    DisableNetworkSync()
    IfCharacterHasTAEEvent(1, 2400899, tae_event_id=700)
    IfCharacterHasSpecialEffect(1, PLAYER, 5577)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.YouLose)
    Restart()


@RestartOnRest(12405260)
def Event_12405260():
    """Event 12405260"""
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2402018)
    IfConditionTrue(0, input_condition=1)
    CreatePlayLog(name=2)
    ForceAnimation(2400899, 3000)
    WaitFrames(frames=250)
    Restart()


@RestartOnRest(12405261)
def Event_12405261():
    """Event 12405261"""
    IfAttacked(0, attacked_entity=PLAYER, attacker=2402018)
    Wait(3.0)
    ForceAnimation(PLAYER, 9580, wait_for_completion=True)
    Restart()


@RestartOnRest(12405262)
def Event_12405262():
    """Event 12405262"""
    IfFlagEnabled(1, 12405263)
    IfCharacterHasTAEEvent(1, 2400899, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.Off)
    AddSpecialEffect(2400899, 5687)
    CancelSpecialEffect(2400899, 5686)
    IfCharacterHasTAEEvent(0, 2400899, tae_event_id=20)
    AddSpecialEffect(2400899, 5686)
    CancelSpecialEffect(2400899, 5687)
    Restart()


@RestartOnRest(12405263)
def Event_12405263():
    """Event 12405263"""
    IfCharacterHasTAEEvent(1, 2400899, tae_event_id=710)
    IfPlayerHasGood(1, 4311)
    IfConditionTrue(0, input_condition=1)
    EnableImmortality(PLAYER)
    WaitFrames(frames=30)
    EnableFlag(9180)
    WaitFrames(frames=1)
    GotoIfMultiplayer(Label.L0)
    PlayCutscene(24000000, cutscene_flags=0, player_id=10000)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    PlayCutscene(24000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableFlag(9180)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EnableFlag(12401000)
    WarpPlayerToRespawnPoint(3402959)


@RestartOnRest(12405270)
def Event_12405270():
    """Event 12405270"""
    IfCharacterInsideRegion(0, PLAYER, region=2402190)
    CreatePlayLog(name=26)


@RestartOnRest(12405271)
def Event_12405271():
    """Event 12405271"""
    IfCharacterInsideRegion(0, PLAYER, region=2402191)
    CreatePlayLog(name=56)


@RestartOnRest(12405272)
def Event_12405272():
    """Event 12405272"""
    IfCharacterInsideRegion(0, PLAYER, region=2402192)
    CreatePlayLog(name=90)


@RestartOnRest(12405273)
def Event_12405273():
    """Event 12405273"""
    IfCharacterInsideRegion(0, PLAYER, region=2402193)
    CreatePlayLog(name=2)


@RestartOnRest(12405289)
def Event_12405289():
    """Event 12405289"""
    SetTeamType(2400000, TeamType.Human)


@RestartOnRest(12405300)
def Event_12405300(_, character: int, region: int, patrol_information_id: int, flag: int):
    """Event 12405300"""
    IfCharacterInsideRegion(0, character, region=region)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    DisableFlag(flag)


@RestartOnRest(12405320)
def Event_12405320():
    """Event 12405320"""
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
    SkipLinesIfFinishedConditionFalse(2, condition=5)
    ChangePatrolBehavior(2400300, patrol_information_id=2403101)
    Restart()
    SkipLinesIfFinishedConditionFalse(2, condition=6)
    ChangePatrolBehavior(2400300, patrol_information_id=2403102)
    Restart()
    SkipLinesIfFinishedConditionFalse(2, condition=7)
    ChangePatrolBehavior(2400300, patrol_information_id=2403103)
    Restart()
    SkipLinesIfFinishedConditionFalse(2, condition=8)
    ChangePatrolBehavior(2400300, patrol_information_id=2403104)
    Restart()


@RestartOnRest(12405330)
def Event_12405330(_, character: int):
    """Event 12405330"""
    ForceAnimation(character, 7000, loop=True)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=4.0)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=character)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character, 7001)
    ReplanAI(character)


@RestartOnRest(12405335)
def Event_12405335():
    """Event 12405335"""
    IfCharacterBackreadEnabled(0, 2400421)
    DisableAI(2400421)
    IfCharacterInsideRegion(1, PLAYER, region=2402031)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=2400421, radius=5.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=2)
    ForceAnimation(2400421, 3011)
    EnableAI(2400421)


@RestartOnRest(12405350)
def Event_12405350(_, character: int, region: int, region_1: int, patrol_information_id: int, region_2: int):
    """Event 12405350"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfCharacterInsideRegion(-2, PLAYER, region=region_2)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(character, region=region_1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    EndIfThisEventSlotFlagEnabled()
    ReplanAI(character)


@RestartOnRest(12405360)
def Event_12405360():
    """Event 12405360"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterBackreadEnabled(0, 2400371)
    AddSpecialEffect(2400371, 5000)
    IfHasAIStatus(0, 2400371, ai_status=AIStatusType.Battle)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(2400371, region=2404085)
    ChangePatrolBehavior(2400371, patrol_information_id=2403106)
    IfCharacterInsideRegion(0, 2400371, region=2404085)
    CancelSpecialEffect(2400371, 5000)
    AICommand(2400371, command_id=-1, command_slot=0)
    ReplanAI(2400371)


@RestartOnRest(12405365)
def Event_12405365(_, character: int, region: int, patrol_information_id: int):
    """Event 12405365"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterBackreadEnabled(0, character)
    AddSpecialEffect(character, 5000)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Battle)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(character, region=region)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)
    IfCharacterInsideRegion(0, character, region=region)
    CancelSpecialEffect(character, 5000)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405370)
def Event_12405370(_, character: int):
    """Event 12405370"""
    IfFlagEnabled(0, 9802)
    DisableBackread(character)


@NeverRestart(12405380)
def Event_12405380(_, character: int, region: int, region_1: int):
    """Event 12405380"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetNest(character, region=region)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Normal)
    SetNest(character, region=region_1)
    Restart()


@NeverRestart(12400865)
def Event_12400865(_, character: int):
    """Event 12400865"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    DisableCharacter(character)
    DropMandatoryTreasure(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, character)
    Wait(0.0)


@RestartOnRest(12405400)
def Event_12405400(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    animation_id: int,
    special_effect_id: int,
    flag: int,
    flag_1: int,
    character: int,
):
    """Event 12405400"""
    IfFlagEnabled(0, flag)
    IfCharacterPartHealthLessThanOrEqual(1, character, npc_part_id=npc_part_id_1, value=0)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfFlagEnabled(1, flag_1)
    IfHealthLessThanOrEqual(2, character, value=0.0)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    SkipLinesIfFlagEnabled(2, flag)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=1, overwrite_max=False)
    Restart()
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=9999999)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    IfCharacterHasTAEEvent(0, character, tae_event_id=400)
    AddSpecialEffect(character, special_effect_id)
    DisableFlag(flag_1)
    IfCharacterHasTAEEvent(0, character, tae_event_id=300)
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=80, overwrite_max=True)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    CancelSpecialEffect(character, special_effect_id)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(12405430)
def Event_12405430(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    flag: int,
    character: int,
):
    """Event 12405430"""
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    EnableFlag(flag)


@RestartOnRest(12405460)
def Event_12405460(
    _,
    tae_event_id: int,
    tae_event_id_1: int,
    flag: int,
    character: int,
    bit_index: uchar,
    bit_index_1: uchar,
):
    """Event 12405460"""
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    IfCharacterHasTAEEvent(0, character, tae_event_id=tae_event_id)
    EnableFlag(flag)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    IfCharacterHasTAEEvent(0, character, tae_event_id=tae_event_id_1)
    DisableFlag(flag)
    Restart()


@RestartOnRest(12405790)
def Event_12405790(_, obj: int, flag: int, model_point: int):
    """Event 12405790"""
    DeleteObjectVFX(obj)
    EndIfFlagEnabled(flag)
    CreateObjectVFX(obj, vfx_id=200, model_point=model_point)


@RestartOnRest(12405800)
def Event_12405800(_, sound_id: int, flag: int, flag_1: int, flag_2: int):
    """Event 12405800"""
    DisableSoundEvent(sound_id=sound_id)
    EndIfFlagEnabled(flag_2)
    IfFlagDisabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfConditionTrue(0, input_condition=1)
    EnableSoundEvent(sound_id=sound_id)
    IfFlagEnabled(-1, flag)
    IfFlagEnabled(-1, flag_1)
    IfConditionTrue(0, input_condition=-1)
    DisableSoundEvent(sound_id=sound_id)
    Restart()


@RestartOnRest(12405810)
def Event_12405810(_, character: int, region: int, region_1: int, command_id: int, flag: int):
    """Event 12405810"""
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(character, region=region_1)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405820)
def Event_12405820(_, character: int, region: int):
    """Event 12405820"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterInsideRegion(0, character, region=region)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405840)
def Event_12405840(_, character: int, command_id: int, flag: int):
    """Event 12405840"""
    EndIfFlagEnabled(flag)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=2)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    IfHasAIStatus(3, character, ai_status=AIStatusType.Normal)
    IfFlagEnabled(4, flag)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=4)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12405850)
def Event_12405850(_, character: int, obj: int, region: int, command_id: int, flag: int):
    """Event 12405850"""
    EndIfFlagEnabled(flag)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, 7013, loop=True)
    IfObjectDestroyed(-1, obj)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=character, radius=4.0)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=0)
    ForceAnimation(character, 7012)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(character, region=region)
    ForceAnimation(character, 7011)
    ForceAnimation(character, 7012)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)


@NeverRestart(12400860)
def Event_12400860():
    """Event 12400860"""
    GotoIfFlagDisabled(Label.L0, flag=12400861)
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


@RestartOnRest(12405600)
def Event_12405600(_, character: int, region: int, radius: float, seconds: float):
    """Event 12405600"""
    DisableAI(character)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(2, input_condition=-2)
    IfAttacked(3, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, condition=2)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    Wait(seconds)
    EnableAI(character)
    WaitFrames(frames=1)
    ReplanAI(character)


@RestartOnRest(12405660)
def Event_12405660():
    """Event 12405660"""
    DisableAI(2400114)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfCharacterInsideRegion(-3, PLAYER, region=2402082)
    IfEntityWithinDistance(-3, entity=2400114, other_entity=PLAYER, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(1, input_condition=-3)
    IfCharacterInsideRegion(-1, 2400122, region=2404151)
    IfAttacked(-1, attacked_entity=2400114, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2400114)
    ReplanAI(2400114)


@RestartOnRest(12405670)
def Event_12405670(_, character: int, region: int, region_1: int, radius: float, seconds: float):
    """Event 12405670"""
    DisableAI(character)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(2, PLAYER, region=region_1)
    IfConditionTrue(2, input_condition=-2)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(3, input_condition=-2)
    IfAttacked(4, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    Wait(seconds)
    EnableAI(character)
    WaitFrames(frames=1)
    ReplanAI(character)


@RestartOnRest(12405675)
def Event_12405675(_, character: int):
    """Event 12405675"""
    DisableAI(character)
    IfCharacterInsideRegion(1, PLAYER, region=2404332)
    IfConditionTrue(-1, input_condition=1)
    IfAttacked(-1, attacked_entity=character, attacker=PLAYER)
    IfEntityWithinDistance(-1, entity=character, other_entity=PLAYER, radius=3.0)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(character)
    WaitFrames(frames=1)
    ReplanAI(character)


@RestartOnRest(12405680)
def Event_12405680():
    """Event 12405680"""
    IfCharacterTargeting(0, targeting_character=2400106, targeted_character=PLAYER)
    WaitFrames(frames=1)
    ForceAnimation(2400106, 3010, wait_for_completion=True)
    WaitFrames(frames=75)
    IfHealthEqual(0, 2400106, value=1.0)
    EnableFlag(12405681)
    ForceAnimation(2400106, 3009, wait_for_completion=True)


@RestartOnRest(12405682)
def Event_12405682(_, character: int, region: int, seconds: float, flag: int, seconds_1: float):
    """Event 12405682"""
    DisableAI(character)
    DisableAnimations(region)
    IfAttacked(1, attacked_entity=character, attacker=PLAYER)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterWhitePhantom(-3, PLAYER)
    IfConditionTrue(2, input_condition=-3)
    IfEntityWithinDistance(2, entity=character, other_entity=PLAYER, radius=10.0)
    IfFlagEnabled(3, 12405681)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(character)
    SkipLinesIfFlagDisabled(24, 12405681)
    Wait(seconds)
    SetEventPoint(character, region=region, reaction_range=1.0)
    AICommand(character, command_id=90, command_slot=0)
    ReplanAI(character)
    IfEntityWithinDistance(4, entity=character, other_entity=region, radius=4.0)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterWhitePhantom(-4, PLAYER)
    IfConditionTrue(5, input_condition=-4)
    IfEntityWithinDistance(5, entity=character, other_entity=PLAYER, radius=3.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(9, condition=2)
    AddSpecialEffect(character, 4662)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(9, flag)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(7, flag)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(5, flag)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(3, flag)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    SkipLinesIfFlagEnabled(1, flag)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    Wait(seconds_1)
    CancelSpecialEffect(character, 4662)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405686)
def Event_12405686(_, character: int):
    """Event 12405686"""
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=2.0)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=character, attacker=PLAYER)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(frames=1)


@RestartOnRest(12405690)
def Event_12405690():
    """Event 12405690"""
    IfCharacterInsideRegion(0, 2400106, region=2404111)
    AddSpecialEffect(2400106, 5002)
    IfCharacterInsideRegion(0, 2400106, region=2404113)
    WaitFrames(frames=30)
    CancelSpecialEffect(2400106, 5002)
    Restart()


@NeverRestart(12400500)
def Event_12400500():
    """Event 12400500"""
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L6, input_condition=15)
    GotoIfFlagDisabled(Label.L1, flag=1193)
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
    GotoIfFlagEnabled(Label.L0, flag=1181)
    GotoIfFlagEnabled(Label.L0, flag=1184)
    GotoIfFlagEnabled(Label.L5, flag=1185)
    GotoIfFlagEnabled(Label.L0, flag=1186)
    GotoIfFlagEnabled(Label.L0, flag=1188)
    GotoIfFlagEnabled(Label.L1, flag=1191)
    GotoIfFlagEnabled(Label.L2, flag=1189)
    GotoIfFlagEnabled(Label.L3, flag=1183)
    GotoIfFlagEnabled(Label.L4, flag=1189)
    GotoIfFlagEnabled(Label.L4, flag=1187)
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
    EzstateAIRequest(2400730, command_id=3, command_slot=1)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400730)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableBackread(2400730)
    EnableBackread(2400732)
    EnableObject(2400731)
    PostDestruction(2400731)
    EzstateAIRequest(2400732, command_id=10, command_slot=1)
    Move(2400732, destination=2404382, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400732)
    End()

    # --- 3 --- #
    DefineLabel(3)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    EzstateAIRequest(2400730, command_id=3, command_slot=1)
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


@NeverRestart(12400501)
def Event_12400501():
    """Event 12400501"""
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


@NeverRestart(12400505)
def Event_12400505():
    """Event 12400505"""
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=1191)
    DisableMapPiece(map_piece_id=2404602)
    IfFlagEnabled(0, 6001)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2404602)
    End()


@NeverRestart(12400507)
def Event_12400507():
    """Event 12400507"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2400730)
    IfHealthNotEqual(1, 2400730, value=0.0)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagEnabled(Label.L0, flag=1185)
    ForceAnimation(2400730, 103063)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2400730, 103067)
    Restart()


@NeverRestart(12400508)
def Event_12400508():
    """Event 12400508"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, 2400730, value=0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400730, 103064)


@NeverRestart(12400512)
def Event_12400512():
    """Event 12400512"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(-1, 2400730, 151)
    IfCharacterHasSpecialEffect(-1, 2400730, 153)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, 2400730, value=0.0)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagEnabled(Label.L0, flag=1185)
    GotoIfFlagEnabled(Label.L1, flag=9432)
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
    WaitFrames(frames=5)
    Restart()


@NeverRestart(12400513)
def Event_12400513():
    """Event 12400513"""
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


@NeverRestart(12400514)
def Event_12400514():
    """Event 12400514"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, flag=1187)
    GotoIfFlagEnabled(Label.L1, flag=1189)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfActionButtonParamActivated(0, action_button_id=2400020, entity=2400731)
    DisplayDialog(text=14001000, anchor_entity=2400731, number_buttons=NumberButtons.OneButton)
    EnableFlag(72400919)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    IfActionButtonParamActivated(0, action_button_id=2400020, entity=2400731)
    DisplayDialog(text=14001001, anchor_entity=2400731, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12400520)
def Event_12400520():
    """Event 12400520"""
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
    GotoIfFlagEnabled(Label.L0, flag=1220)
    GotoIfFlagEnabled(Label.L1, flag=1224)
    GotoIfFlagEnabled(Label.L2, flag=1225)
    GotoIfFlagEnabled(Label.L3, flag=1226)
    GotoIfFlagEnabled(Label.L4, flag=1228)
    GotoIfFlagEnabled(Label.L4, flag=1229)
    GotoIfFlagEnabled(Label.L4, flag=1235)
    GotoIfFlagEnabled(Label.L5, flag=1222)
    GotoIfFlagEnabled(Label.L5, flag=1230)
    GotoIfFlagEnabled(Label.L6, flag=1231)
    DisableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    EnableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400750, 103080)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 2 --- #
    DefineLabel(2)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    EnableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400754, 103081)
    Move(2400754, destination=2404504, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 3 --- #
    DefineLabel(3)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    EnableBackread(2400757)
    ForceAnimation(2400757, 103081)
    Move(2400757, destination=2404504, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(2400748)
    EnableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    EnableBackread(2400750)
    EnableCharacter(2400750)
    DisableBackread(2400754)
    DisableCharacter(2400754)
    DisableBackread(2400757)
    DisableCharacter(2400757)
    EzstateAIRequest(2400750, command_id=5, command_slot=1)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400750)
    End()

    # --- 6 --- #
    DefineLabel(6)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableCharacter(2400750)
    DisableBackread(2400754)
    DisableCharacter(2400754)
    DisableBackread(2400757)
    DisableCharacter(2400757)
    DropMandatoryTreasure(2400750)
    End()


@NeverRestart(12400521)
def Event_12400521():
    """Event 12400521"""
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


@NeverRestart(12400522)
def Event_12400522():
    """Event 12400522"""
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=1230)
    GotoIfFlagEnabled(Label.L0, flag=1231)
    DisableMapPiece(map_piece_id=2404600)
    IfFlagEnabled(0, 6001)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2404600)
    End()


@NeverRestart(12400523)
def Event_12400523():
    """Event 12400523"""
    IfFlagEnabled(0, 72400510)
    DisableFlag(72400510)
    DisableFlagRange((1220, 1239))
    EnableFlag(1232)


@NeverRestart(12400524)
def Event_12400524():
    """Event 12400524"""
    IfFlagEnabled(0, 72400511)
    DisableFlag(72400511)
    DisableFlagRange((1220, 1239))
    EnableFlag(1233)


@NeverRestart(12400525)
def Event_12400525():
    """Event 12400525"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 72400499)
    DisableFlag(72400499)
    GotoIfFlagDisabled(Label.L0, flag=72400950)
    GotoIfFlagDisabled(Label.L1, flag=72400951)
    GotoIfFlagDisabled(Label.L2, flag=72400952)
    GotoIfFlagDisabled(Label.L3, flag=72400953)
    GotoIfFlagDisabled(Label.L4, flag=72400954)

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
    GotoIfFlagDisabled(Label.L5, flag=72400940)
    GotoIfFlagDisabled(Label.L6, flag=72400941)
    GotoIfFlagDisabled(Label.L7, flag=72400942)
    GotoIfFlagDisabled(Label.L8, flag=72400943)
    GotoIfFlagDisabled(Label.L9, flag=72400944)

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


@NeverRestart(12400531)
def Event_12400531():
    """Event 12400531"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerHasGood(1, 701)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableFlag(72400498)
    End()

    # --- 0 --- #
    DefineLabel(0)
    End()


@NeverRestart(12400560)
def Event_12400560():
    """Event 12400560"""
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
    GotoIfFlagEnabled(Label.L4, flag=1161)
    GotoIfFlagEnabled(Label.L1, flag=1164)
    GotoIfFlagEnabled(Label.L1, flag=1165)
    GotoIfFlagEnabled(Label.L3, flag=1166)
    GotoIfFlagEnabled(Label.L2, flag=1167)
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
    EzstateAIRequest(2400765, command_id=2, command_slot=1)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400765)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableBackread(2400765)
    EzstateAIRequest(2400765, command_id=2, command_slot=1)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400765)
    End()


@NeverRestart(12400561)
def Event_12400561():
    """Event 12400561"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1161)
    EndIfFlagEnabled(1166)
    IfCharacterDead(1, 2400765)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1160, 1179))
    EnableFlag(1161)
    SaveRequest()


@NeverRestart(12400563)
def Event_12400563():
    """Event 12400563"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, flag=72400330)
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


@NeverRestart(12400564)
def Event_12400564():
    """Event 12400564"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, flag=72400331)
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


@NeverRestart(12400565)
def Event_12400565():
    """Event 12400565"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, flag=72400332)
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


@NeverRestart(12400566)
def Event_12400566():
    """Event 12400566"""
    IfFlagEnabled(0, 72400970)
    DisableFlag(72400970)
    DisableFlagRange((1160, 1179))
    EnableFlag(1168)
    Restart()


@NeverRestart(12400567)
def Event_12400567():
    """Event 12400567"""
    IfFlagEnabled(0, 72400971)
    DisableFlag(72400971)
    DisableFlagRange((1160, 1179))
    EnableFlag(1169)
    Restart()


@NeverRestart(12400568)
def Event_12400568():
    """Event 12400568"""
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=1166)
    DisableMapPiece(map_piece_id=2404603)
    IfFlagEnabled(0, 6001)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2404603)
    End()


@NeverRestart(12400569)
def Event_12400569():
    """Event 12400569"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1161)
    EndIfFlagEnabled(1166)
    IfHealthEqual(1, 2400765, value=0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400765, 103053)


@NeverRestart(12400570)
def Event_12400570():
    """Event 12400570"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2400765)
    IfHealthNotEqual(1, 2400765, value=0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400765, 103052)
    Restart()


@NeverRestart(12400571)
def Event_12400571():
    """Event 12400571"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2400765, 151)
    IfHealthNotEqual(1, 2400765, value=0.0)
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
    WaitFrames(frames=5)
    Restart()


@NeverRestart(12400572)
def Event_12400572():
    """Event 12400572"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 9432)
    IfFlagDisabled(1, 1165)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400765, 103051)
    IfFlagDisabled(0, 9432)
    ForceAnimation(2400765, 103050)
    Restart()


@NeverRestart(12400580)
def Event_12400580():
    """Event 12400580"""
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(1, PLAYER, region=2402280)
    IfFlagEnabled(2, 72400400)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    EnableSoundEvent(sound_id=2403300)


@NeverRestart(12400581)
def Event_12400581():
    """Event 12400581"""
    IfFlagEnabled(0, 72400400)
    DisableSoundEvent(sound_id=2403300)


@NeverRestart(12400582)
def Event_12400582():
    """Event 12400582"""
    EnableMapPiece(map_piece_id=2404010)
    IfFlagEnabled(0, 12401802)
    DisableMapPiece(map_piece_id=2404010)


@NeverRestart(12400590)
def Event_12400590():
    """Event 12400590"""
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
    GotoIfFlagEnabled(Label.L0, flag=1340)
    GotoIfFlagEnabled(Label.L1, flag=1341)
    GotoIfFlagEnabled(Label.L2, flag=1342)
    GotoIfFlagEnabled(Label.L3, flag=1343)
    GotoIfFlagEnabled(Label.L4, flag=1344)
    GotoIfFlagEnabled(Label.L5, flag=1345)
    GotoIfFlagEnabled(Label.L6, flag=1346)
    GotoIfFlagEnabled(Label.L4, flag=1347)
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
    GotoIfFlagEnabled(Label.L7, flag=12405160)
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
    EzstateAIRequest(2400762, command_id=11, command_slot=1)
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


@NeverRestart(12400591)
def Event_12400591():
    """Event 12400591"""
    IfFlagEnabled(0, 72400465)
    DisableFlag(72400465)
    DisableFlagRange((1340, 1359))
    EnableFlag(1347)
    SaveRequest()


@NeverRestart(12400592)
def Event_12400592(_, attacked_entity: int, flag: int):
    """Event 12400592"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(flag)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    EnableFlag(flag)


@NeverRestart(12400593)
def Event_12400593(_, character: int, flag: int, flag_1: int):
    """Event 12400593"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(-1, flag_1)
    IfHealthLessThanOrEqual(-1, character, value=0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(character, TeamType.HostileNPC)
    DisableFlagRange((1340, 1359))
    EnableFlag(flag)
    SaveRequest()


@NeverRestart(12400594)
def Event_12400594(_, character: int, flag: int):
    """Event 12400594"""
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(0, character)
    DisableFlagRange((1340, 1359))
    EnableFlag(flag)
    SaveRequest()


@NeverRestart(12400610)
def Event_12400610():
    """Event 12400610"""
    DisableFlag(72400362)
    DisableFlag(72400921)
    DisableFlag(72400924)
    DisableGravity(2400756)
    ForceAnimation(2400756, 7002, loop=True)
    DisableAI(2400756)
    DisableBackread(2400756)
    GotoIfFlagEnabled(Label.L0, flag=1205)
    GotoIfFlagEnabled(Label.L1, flag=1206)
    GotoIfFlagEnabled(Label.L1, flag=1207)
    GotoIfFlagEnabled(Label.L3, flag=1210)
    DisableBackread(2400755)
    DisableBackread(2400759)
    EnableBackread(2400220)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfEventValueNotEqual(-1, flag=72400372, bit_count=2, value=0)
    IfFlagEnabled(-1, 12405158)
    GotoIfConditionTrue(Label.L2, input_condition=-1)
    DisableBackread(2400755)
    EnableBackread(2400759)
    DisableBackread(2400220)
    GotoIfFlagEnabled(Label.L5, flag=12405157)
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
    GotoIfFlagEnabled(Label.L4, flag=12405157)
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


@NeverRestart(12400611)
def Event_12400611():
    """Event 12400611"""
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


@NeverRestart(12400612)
def Event_12400612(_, character: int, flag: int):
    """Event 12400612"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthLessThan(1, character, value=0.5)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag)


@NeverRestart(12400614)
def Event_12400614(_, character: int, animation_id: int):
    """Event 12400614"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, character, value=0.0)
    IfCharacterHasSpecialEffect(1, character, 155)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, animation_id)


@NeverRestart(12400616)
def Event_12400616(_, character: int):
    """Event 12400616"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=character, attacker=PLAYER)
    IfHealthNotEqual(1, character, value=0.0)
    IfHealthGreaterThan(1, character, value=0.5)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(-2, character, 153)
    GotoIfConditionTrue(Label.L0, input_condition=-2)
    IfCharacterHasSpecialEffect(-3, character, 155)
    GotoIfConditionTrue(Label.L1, input_condition=-3)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 103079)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 103130)
    Restart()


@NeverRestart(12400618)
def Event_12400618(_, character: int):
    """Event 12400618"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, character, 154)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 103072)
    Restart()


@NeverRestart(12400620)
def Event_12400620(_, character: int):
    """Event 12400620"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, character, 156)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 103072)


@NeverRestart(12400622)
def Event_12400622():
    """Event 12400622"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 1208)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1200, 1219))
    EnableFlag(1205)


@NeverRestart(12400623)
def Event_12400623():
    """Event 12400623"""
    EndIfClient()
    IfFlagEnabled(1, 1209)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1200, 1219))
    EnableFlag(1204)


@NeverRestart(12400624)
def Event_12400624():
    """Event 12400624"""
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


@NeverRestart(12400625)
def Event_12400625(_, character: int, flag: int):
    """Event 12400625"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagDisabled(1207)
    WaitFrames(frames=30)
    IfAttackedWithDamageType(-1, attacked_entity=character, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=2404383)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 1207)
    IfCharacterBackreadEnabled(1, character)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(flag)


@NeverRestart(12400627)
def Event_12400627(_, character: int, flag: int):
    """Event 12400627"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(2, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(3, attacked_entity=character, attacker=PLAYER)
    IfHealthNotEqual(3, character, value=0.0)
    IfConditionTrue(0, input_condition=3)
    EnableFlag(flag)


@NeverRestart(12400629)
def Event_12400629():
    """Event 12400629"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(-1, 1208)
    IfFlagEnabled(-1, 1205)
    IfFlagEnabled(-1, 1207)
    GotoIfConditionFalse(Label.L6, input_condition=-1)
    GotoIfFlagEnabled(Label.L0, flag=1208)
    GotoIfFlagDisabled(Label.L5, flag=72400360)
    GotoIfFlagRangeAllDisabled(Label.L5, flag_range=(70000200, 70000202))

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
    GotoIfFlagEnabled(Label.L5, flag=1208)
    EventValueOperation(
        source_flag=70000200,
        source_flag_bit_count=3,
        operand=1,
        target_flag=0,
        target_flag_bit_count=1,
        calculation_type=CalculationType.Subtract,
    )

    # --- 5 --- #
    DefineLabel(5)
    End()


@NeverRestart(12400630)
def Event_12400630(_, character: int):
    """Event 12400630"""
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    IfHealthEqual(1, character, value=0.0)
    IfAttackedWithDamageType(1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    IfCharacterDead(0, character)
    EnableFlag(9432)
    EnableFlag(72400490)


@NeverRestart(12400650)
def Event_12400650():
    """Event 12400650"""
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
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1373, 1375))
    GotoIfFlagEnabled(Label.L1, flag=1372)
    GotoIfFlagEnabled(Label.L2, flag=1371)
    GotoIfFlagEnabled(Label.L3, flag=1370)
    GotoIfFlagEnabled(Label.L4, flag=1369)
    GotoIfFlagEnabled(Label.L5, flag=1368)
    GotoIfFlagRangeAnyEnabled(Label.L6, flag_range=(1365, 1367))
    GotoIfFlagRangeAnyEnabled(Label.L7, flag_range=(1362, 1364))
    GotoIfFlagRangeAnyEnabled(Label.L8, flag_range=(1360, 1361))

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
    Event_12400651()
    Event_12400652()
    Event_12400653()
    Event_12400654()
    Event_12400655()
    Event_12400657()
    Event_12400658()
    Event_12400659()
    Event_12400660()
    Event_12400661()
    Event_12400662()
    Event_12400663()
    Event_12400665()


@NeverRestart(12400651)
def Event_12400651():
    """Event 12400651"""
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


@NeverRestart(12400652)
def Event_12400652():
    """Event 12400652"""
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


@NeverRestart(12400653)
def Event_12400653():
    """Event 12400653"""
    EndIfThisEventFlagEnabled()
    DisableMapPiece(map_piece_id=2404610)
    IfFlagEnabled(0, 1370)
    EnableMapPiece(map_piece_id=2404610)


@NeverRestart(12400654)
def Event_12400654():
    """Event 12400654"""
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


@NeverRestart(12400655)
def Event_12400655():
    """Event 12400655"""
    EndIfThisEventFlagEnabled()
    DisableBackread(2400901)
    IfFlagEnabled(0, 1370)
    EnableBackread(2400901)


@NeverRestart(12400656)
def Event_12400656():
    """Event 12400656"""
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


@NeverRestart(12400657)
def Event_12400657():
    """Event 12400657"""
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


@NeverRestart(12400658)
def Event_12400658():
    """Event 12400658"""
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


@NeverRestart(12400659)
def Event_12400659():
    """Event 12400659"""
    EndIfThisEventFlagEnabled()
    IfAttacked(0, attacked_entity=2400900, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttacked(0, attacked_entity=2400900, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttacked(0, attacked_entity=2400900, attacker=PLAYER)
    WaitFrames(frames=1)


@NeverRestart(12400660)
def Event_12400660():
    """Event 12400660"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 1373)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@NeverRestart(12400661)
def Event_12400661():
    """Event 12400661"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 1374)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@NeverRestart(12400662)
def Event_12400662():
    """Event 12400662"""
    IfFlagEnabled(1, 1370)
    IfFlagEnabled(1, 72400530)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400903, 103034, loop=True)
    IfFlagDisabled(0, 72400530)
    ForceAnimation(2400903, 103031, loop=True)
    Restart()


@NeverRestart(12400663)
def Event_12400663():
    """Event 12400663"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1370)
    IfFlagEnabled(-1, 1371)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(1, attacked_entity=2400903, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400903, 103032)
    Kill(2400903, award_souls=True)


@NeverRestart(12400665)
def Event_12400665():
    """Event 12400665"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1365)
    IfFlagEnabled(-1, 1366)
    IfFlagEnabled(-1, 1367)
    IfConditionTrue(0, input_condition=-1)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@RestartOnRest(12400700)
def Event_12400700():
    """Event 12400700"""
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
    EnableMapPiece(map_piece_id=2404604)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 1109)
    EndIfConditionFalse(3)
    DisableFlag(1109)


@RestartOnRest(12400701)
def Event_12400701():
    """Event 12400701"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 72400300)
    DisableFlagRange((1100, 1119))
    EnableFlag(1101)


@RestartOnRest(12400702)
def Event_12400702():
    """Event 12400702"""
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(1106)
    EndIfFlagEnabled(1108)
    IfFlagRangeAnyEnabled(1, flag_range=(12400720, 12400724))
    IfFlagEnabled(2, 1106)
    IfFlagEnabled(3, 1108)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionFalse(input_condition=1)
    DisableFlagRange((1100, 1119))
    EnableFlag(1102)


@RestartOnRest(12400703)
def Event_12400703():
    """Event 12400703"""
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
    EndIfFinishedConditionFalse(input_condition=1)
    DisableFlagRange((1100, 1119))
    EnableFlag(1103)


@RestartOnRest(12400704)
def Event_12400704():
    """Event 12400704"""
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
    EndIfFinishedConditionTrue(input_condition=-5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1104)


@RestartOnRest(12400705)
def Event_12400705():
    """Event 12400705"""
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
    IfFlagRangeAllEnabled(6, flag_range=(12400708, 12400711))
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(-2, input_condition=6)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1105)


@RestartOnRest(12400706)
def Event_12400706():
    """Event 12400706"""
    EndIfFlagEnabled(1106)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, 2400700)
    IfFlagDisabled(1, 1108)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1100, 1119))
    EnableFlag(1106)
    SaveRequest()


@RestartOnRest(12400707)
def Event_12400707():
    """Event 12400707"""
    IfEventValueGreaterThanOrEqual(0, flag=12400733, bit_count=3, value=3)
    EnableFlag(72400309)


@RestartOnRest(12400708)
def Event_12400708(_, flag: int, flag_1: int, flag_2: int, flag_3: int, left: int):
    """Event 12400708"""
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, flag)
    IfConditionTrue(-1, input_condition=1)
    IfFlagEnabled(-1, flag_2)
    IfFlagEnabled(-1, flag_3)
    SkipLinesIfNotEqual(1, left=left, right=1)
    IfFlagEnabled(-1, 1315)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionFalse(input_condition=1)
    IncrementEventValue(12400733, bit_count=3, max_value=5)
    EnableFlag(72400313)
    DisableFlagRange((72400314, 72400319))
    EnableFlag(flag_1)


@RestartOnRest(12400713)
def Event_12400713(_, flag: int, flag_1: int):
    """Event 12400713"""
    IfFlagEnabled(1, flag)
    IfFlagEnabled(2, flag_1)
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


@RestartOnRest(12400720)
def Event_12400720():
    """Event 12400720"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1161)
    IfFlagEnabled(-1, 1166)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400724)
    StopEvent(event_id=12400721)
    StopEvent(event_id=12400722)
    StopEvent(event_id=12400723)
    StopEvent(event_id=12400728)


@RestartOnRest(12400721)
def Event_12400721():
    """Event 12400721"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1183)
    IfFlagEnabled(-1, 1189)
    IfFlagEnabled(-1, 1191)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400725)
    StopEvent(event_id=12400720)
    StopEvent(event_id=12400722)
    StopEvent(event_id=12400723)
    StopEvent(event_id=12400729)


@RestartOnRest(12400722)
def Event_12400722():
    """Event 12400722"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1222)
    IfFlagEnabled(-1, 1230)
    IfFlagEnabled(-1, 1231)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400726)
    StopEvent(event_id=12400720)
    StopEvent(event_id=12400721)
    StopEvent(event_id=12400723)
    StopEvent(event_id=12400730)


@RestartOnRest(12400723)
def Event_12400723():
    """Event 12400723"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1303)
    IfFlagEnabled(-1, 1312)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12400727)
    StopEvent(event_id=12400720)
    StopEvent(event_id=12400721)
    StopEvent(event_id=12400722)
    StopEvent(event_id=12400731)


@RestartOnRest(12400728)
def Event_12400728():
    """Event 12400728"""
    EndIfThisEventFlagEnabled()
    IfFlagRangeAnyEnabled(0, flag_range=(12400720, 12400723))
    IfFlagEnabled(-1, 1161)
    IfFlagEnabled(-1, 1166)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(event_id=12400729)
    StopEvent(event_id=12400730)
    StopEvent(event_id=12400731)


@RestartOnRest(12400729)
def Event_12400729():
    """Event 12400729"""
    EndIfThisEventFlagEnabled()
    IfFlagRangeAnyEnabled(0, flag_range=(12400720, 12400723))
    IfFlagEnabled(-1, 1183)
    IfFlagEnabled(-1, 1189)
    IfFlagEnabled(-1, 1191)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(event_id=12400728)
    StopEvent(event_id=12400730)
    StopEvent(event_id=12400731)


@RestartOnRest(12400730)
def Event_12400730():
    """Event 12400730"""
    EndIfThisEventFlagEnabled()
    IfFlagRangeAnyEnabled(0, flag_range=(12400720, 12400723))
    IfFlagEnabled(-1, 1222)
    IfFlagEnabled(-1, 1230)
    IfFlagEnabled(-1, 1231)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(event_id=12400728)
    StopEvent(event_id=12400729)
    StopEvent(event_id=12400731)


@RestartOnRest(12400731)
def Event_12400731():
    """Event 12400731"""
    EndIfThisEventFlagEnabled()
    IfFlagRangeAnyEnabled(0, flag_range=(12400720, 12400723))
    IfFlagEnabled(-1, 1303)
    IfFlagEnabled(-1, 1312)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400985)
    StopEvent(event_id=12400728)
    StopEvent(event_id=12400729)
    StopEvent(event_id=12400730)


@RestartOnRest(12400732)
def Event_12400732():
    """Event 12400732"""
    IfAttackedWithDamageType(1, attacked_entity=2400700)
    IfFlagEnabled(1, 72400981)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(1109)


@RestartOnRest(12400737)
def Event_12400737():
    """Event 12400737"""
    EndIfFlagEnabled(1108)
    DisableMapPiece(map_piece_id=2404604)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 1108)
    EnableMapPiece(map_piece_id=2404604)
    DropMandatoryTreasure(2400700)


@RestartOnRest(12400738)
def Event_12400738():
    """Event 12400738"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 9432)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(2400700, 5401)
    WaitFrames(frames=1)
    ForceAnimation(2400700, 7000)
    IfFlagDisabled(0, 9432)
    AddSpecialEffect(2400700, 5402)
    WaitFrames(frames=1)
    ForceAnimation(2400700, 0)
    Restart()


@NeverRestart(12400900)
def Event_12400900():
    """Event 12400900"""
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
    GotoIfFlagDisabled(Label.L5, flag=9802)
    GotoIfFlagEnabled(Label.L3, flag=1304)
    GotoIfFlagEnabled(Label.L3, flag=1305)
    GotoIfFlagEnabled(Label.L4, flag=1306)
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
    GotoIfFlagEnabled(Label.L0, flag=1304)
    GotoIfFlagEnabled(Label.L0, flag=1305)
    GotoIfFlagEnabled(Label.L4, flag=1306)
    GotoIfFlagEnabled(Label.L1, flag=1307)
    GotoIfFlagEnabled(Label.L2, flag=1308)
    GotoIfFlagEnabled(Label.L3, flag=1312)
    GotoIfFlagEnabled(Label.L5, flag=1317)
    GotoIfFlagEnabled(Label.L6, flag=1303)
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
    EzstateAIRequest(2400770, command_id=8, command_slot=1)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(frames=1)
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
    WaitFrames(frames=1)
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
    EzstateAIRequest(2400770, command_id=8, command_slot=1)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(frames=1)
    DropMandatoryTreasure(2400770)
    End()


@NeverRestart(12400901)
def Event_12400901():
    """Event 12400901"""
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


@NeverRestart(12400940)
def Event_12400940(_, character: int):
    """Event 12400940"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 72400955)
    IfCharacterHasSpecialEffect(1, character, 157)
    IfFlagDisabled(1, 72400955)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 103106)
    Restart()


@NeverRestart(12400903)
def Event_12400903():
    """Event 12400903"""
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
    GotoIfFlagEnabled(Label.L0, flag=1308)
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


@NeverRestart(12400904)
def Event_12400904():
    """Event 12400904"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 1308)
    IfCharacterInsideRegion(1, PLAYER, region=2404380)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=2400775)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(72400397)
    EnableAI(2400775)


@NeverRestart(12400910)
def Event_12400910(_, character: int):
    """Event 12400910"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=character)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(2, character, 151)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    IfCharacterHasSpecialEffect(3, character, 158)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    ForceAnimation(character, 103134)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 103098)
    WaitFrames(frames=20)
    Restart()


@NeverRestart(12400915)
def Event_12400915(_, character: int):
    """Event 12400915"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1317)
    EndIfFlagEnabled(1312)
    EndIfFlagEnabled(1303)
    IfHealthEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(-1, character, 151)
    IfCharacterHasSpecialEffect(-1, character, 158)
    IfConditionTrue(1, input_condition=-1)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(character, 103135)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 103099)
    End()


@NeverRestart(12400920)
def Event_12400920(_, character: int):
    """Event 12400920"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagDisabled(0, 72400955)
    IfFlagEnabled(0, 72400955)
    IfCharacterHasSpecialEffect(1, character, 151)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(character, 103104)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 103101)
    IfCharacterHasSpecialEffect(0, character, 152)
    ForceAnimation(character, 103104)
    Restart()


@NeverRestart(12400925)
def Event_12400925(_, character: int):
    """Event 12400925"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(-1, character, 153)
    IfCharacterHasSpecialEffect(-1, character, 159)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(1, character, 153)
    GotoIfConditionTrue(Label.L2, input_condition=1)
    IfCharacterHasSpecialEffect(2, character, 159)
    GotoIfConditionTrue(Label.L0, input_condition=2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(3, 9432)
    IfFlagDisabled(3, 1307)
    IfFlagDisabled(3, 1306)
    GotoIfConditionTrue(Label.L1, input_condition=3)
    ForceAnimation(character, 103102, loop=True)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 103103, loop=True)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(4, 9432)
    IfFlagDisabled(4, 1307)
    IfFlagDisabled(4, 1306)
    GotoIfConditionTrue(Label.L3, input_condition=4)
    ForceAnimation(character, 103096, loop=True)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 103097, loop=True)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    WaitFrames(frames=5)
    Restart()


@NeverRestart(12400930)
def Event_12400930(_, character: int):
    """Event 12400930"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, character, 156)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 103102)
    Restart()


@NeverRestart(12400935)
def Event_12400935(_, character: int):
    """Event 12400935"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=5.0)
    IfCharacterHasSpecialEffect(1, character, 151)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, 103101, wait_for_completion=True)


@NeverRestart(12400952)
def Event_12400952():
    """Event 12400952"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=1306)
    GotoIfFlagEnabled(Label.L0, flag=1308)
    GotoIfFlagEnabled(Label.L0, flag=1312)
    IfFlagEnabled(0, 6001)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DestroyObject(2400773)
    End()


@NeverRestart(12400953)
def Event_12400953():
    """Event 12400953"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthNotEqual(1, 2400770, value=0.0)
    IfHealthNotEqual(1, 2400774, value=0.0)
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


@NeverRestart(12400954)
def Event_12400954():
    """Event 12400954"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfPlayerHasGood(1, 702)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisableFlag(72400392)
    End()

    # --- 0 --- #
    DefineLabel(0)
    End()


@NeverRestart(12400800)
def Event_12400800():
    """Event 12400800"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2400765, attacker=PLAYER)
    IfHealthEqual(1, 2400765, value=0.0)
    IfAttackedWithDamageType(2, attacked_entity=2400730, attacker=PLAYER)
    IfHealthEqual(2, 2400730, value=0.0)
    IfAttackedWithDamageType(3, attacked_entity=2400750, attacker=PLAYER)
    IfHealthEqual(3, 2400750, value=0.0)
    IfAttackedWithDamageType(4, attacked_entity=2400754, attacker=PLAYER)
    IfHealthEqual(4, 2400754, value=0.0)
    IfAttackedWithDamageType(5, attacked_entity=2400757, attacker=PLAYER)
    IfHealthEqual(5, 2400757, value=0.0)
    IfAttackedWithDamageType(7, attacked_entity=2400770, attacker=PLAYER)
    IfHealthEqual(7, 2400770, value=0.0)
    IfAttackedWithDamageType(8, attacked_entity=2400772, attacker=PLAYER)
    IfHealthEqual(8, 2400772, value=0.0)
    IfAttackedWithDamageType(9, attacked_entity=2400774, attacker=PLAYER)
    IfHealthEqual(9, 2400774, value=0.0)
    IfAttackedWithDamageType(13, attacked_entity=2400700, attacker=PLAYER)
    IfHealthEqual(13, 2400700, value=0.0)
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


@NeverRestart(12400801)
def Event_12400801():
    """Event 12400801"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagDisabled(Label.L0, flag=1166)
    DisableBackread(2400765)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400765)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=1191)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400730)

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, flag=1231)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400750)

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L3, flag=1230)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    EnableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400750, 103087)
    EzstateAIRequest(2400750, command_id=5, command_slot=1)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400750)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L4, flag=1312)
    DisableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400770)

    # --- 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L4, flag=1108)
    EnableMapPiece(map_piece_id=2404604)
    DropMandatoryTreasure(2400700)
    DisableBackread(2400700)

    # --- 5 --- #
    DefineLabel(5)


@NeverRestart(12400805)
def Event_12400805(_, character: int, animation_id: int, special_effect: int):
    """Event 12400805"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, character, special_effect)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, animation_id)
    WaitFrames(frames=5)
    Restart()


@NeverRestart(12400810)
def Event_12400810(_, character: int, animation_id: int):
    """Event 12400810"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthNotEqual(1, character, value=0.0)
    IfAttackedWithDamageType(1, attacked_entity=character)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, animation_id)
    Restart()


@NeverRestart(12400830)
def Event_12400830(_, character: int, animation_id: int):
    """Event 12400830"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(character, animation_id)


@NeverRestart(12400840)
def Event_12400840(_, flag: int, action_button_id: int, destination: int):
    """Event 12400840"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(flag)
    IfFlagDisabled(1, flag)
    IfActionButtonParamActivated(1, action_button_id=action_button_id, entity=destination)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=210, short_move=True)
    ForceAnimation(PLAYER, 101320)
    WaitFrames(frames=25)
    WaitFrames(frames=20)
    EnableFlag(flag)
    IfFlagDisabled(0, flag)
    Restart()


@RestartOnRest(12405700)
def Event_12405700():
    """Event 12405700"""
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
    AICommand(2400396, command_id=10, command_slot=0)
    SetNest(2400396, region=2409007)
    ReplanAI(2400396)

    # --- 1 --- #
    DefineLabel(1)
    AICommand(2400410, command_id=10, command_slot=0)
    SetNest(2400410, region=2409007)
    ReplanAI(2400410)

    # --- 2 --- #
    DefineLabel(2)
    AICommand(2400393, command_id=10, command_slot=0)
    SetNest(2400393, region=2409007)
    ReplanAI(2400393)
    IfCharacterInsideRegion(-2, 2400393, region=2402030)
    IfCharacterInsideRegion(-2, 2400396, region=2402030)
    IfCharacterInsideRegion(-2, 2400410, region=2402030)
    IfConditionTrue(0, input_condition=-2)
    IfEntityWithinDistance(-3, entity=2400393, other_entity=PLAYER, radius=5.0)
    IfEntityWithinDistance(-3, entity=2400396, other_entity=PLAYER, radius=5.0)
    IfEntityWithinDistance(-3, entity=2400410, other_entity=PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=-3)
    AICommand(2400393, command_id=-1, command_slot=0)
    ReplanAI(2400393)
    AICommand(2400396, command_id=-1, command_slot=0)
    ReplanAI(2400396)
    AICommand(2400410, command_id=-1, command_slot=0)
    ReplanAI(2400410)


@RestartOnRest(12405701)
def Event_12405701(_, character: int, region: int):
    """Event 12405701"""
    IfCharacterInsideRegion(-1, 2400393, region=2402030)
    IfCharacterInsideRegion(-1, 2400396, region=2402030)
    IfCharacterInsideRegion(-1, 2400410, region=2402030)
    IfConditionTrue(0, input_condition=-1)
    AICommand(character, command_id=10, command_slot=0)
    SetNest(character, region=region)
    ReplanAI(character)
    IfCharacterInsideRegion(1, PLAYER, region=2402030)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=5.0)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405710)
def Event_12405710():
    """Event 12405710"""
    GotoIfFlagDisabled(Label.L0, flag=9453)
    EndOfAnimation(obj=2401202, animation_id=1)
    NotifyDoorEventSoundDampening(obj=2401202, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    IfActionButtonParamActivated(0, action_button_id=7000, entity=2401202)
    DisplayDialog(text=10010171, anchor_entity=2401202, display_distance=5.0, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12405750)
def Event_12405750(_, attacked_entity: int, animation_id: int, radius: float):
    """Event 12405750"""
    EndIfThisEventSlotFlagEnabled()
    IfEntityWithinDistance(1, entity=attacked_entity, other_entity=PLAYER, radius=radius)
    IfAttackedWithDamageType(2, attacked_entity=attacked_entity, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=2)
    ForceAnimation(attacked_entity, animation_id)


@NeverRestart(12401800)
def Event_12401800():
    """Event 12401800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2403802)
    DisableSoundEvent(sound_id=2403803)
    DisableCharacter(2400800)
    DisableObject(2400801)
    Kill(2400800)
    DisableObject(2401800)
    DeleteVFX(2403800, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2400800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2401800)
    DeleteVFX(2403800)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2400800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(achievement_id=15)
    AwardItemLot(50000001, host_only=False)
    EnableFlag(2400)
    EnableFlag(2401)
    EnableFlag(9455)
    EnableFlag(2402)
    EnableFlag(72400512)
    StopPlayLogMeasurement(measurement_id=2400000)
    StopPlayLogMeasurement(measurement_id=2400001)
    StopPlayLogMeasurement(measurement_id=2400010)
    CreatePlayLog(name=114)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=126,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=126,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=126,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=126,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)
    EndIfClient()


@NeverRestart(12401801)
def Event_12401801():
    """Event 12401801"""
    DisableNetworkSync()
    EndIfFlagEnabled(12401800)
    IfFlagEnabled(1, 12401800)
    IfCharacterBackreadDisabled(2, 2400800)
    IfHealthLessThanOrEqual(2, 2400800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2402800, 0, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12401802)
def Event_12401802():
    """Event 12401802"""
    EndIfFlagEnabled(12401800)
    DisableObject(2400801)
    EndIfThisEventFlagEnabled()
    DisableCharacter(2400800)
    EnableObject(2400801)
    EnableObjectInvulnerability(2400801)
    IfFlagDisabled(1, 12401800)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2402805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12404223)
    IfCharacterType(2, PLAYER, character_type=CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)
    WaitFrames(frames=1)
    EnableFlag(72400400)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(24000060, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(24000060, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableObject(2400801)
    DisableFlag(9180)
    EnableCharacter(2400800)
    ForceAnimation(2400800, 7000)
    ForceAnimation(2400800, 7001)
    EnableFlag(12404800)
    EndIfFlagEnabled(9301)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9301)


@NeverRestart(12401803)
def Event_12401803():
    """Event 12401803"""
    DeleteVFX(2403413, erase_root_only=False)
    EndIfThisEventFlagEnabled()
    GotoIfFlagEnabled(Label.L0, flag=12401800)
    IfFlagEnabled(0, 12401800)

    # --- 0 --- #
    DefineLabel(0)
    CreateVFX(2403413)
    EndIfClient()
    IfCharacterHuman(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2400010, entity=2401801)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9180)
    WaitFrames(frames=1)
    DeleteVFX(2403413)
    PlayCutsceneAndMovePlayerAndSetTimePeriod(
        cutscene=24000030,
        cutscene_flags=0,
        move_to_region=-1,
        game_map=CATHEDRAL_WARD,
        player_id=10000,
        time_period_id=2,
    )
    WaitFrames(frames=1)
    DisableFlag(9180)


@NeverRestart(12401804)
def Event_12401804():
    """Event 12401804"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12404800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(2400800)
    EnableFlag(12404800)
    EnableFlag(12401802)


@NeverRestart(12404840)
def Event_12404840():
    """Event 12404840"""
    EndIfFlagEnabled(12401800)
    GotoIfFlagEnabled(Label.L0, flag=12401802)
    SkipLinesIfClient(2)
    DisableObject(2401800)
    DeleteVFX(2403800, erase_root_only=False)
    IfFlagDisabled(1, 12401800)
    IfFlagEnabled(1, 12401802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2401800)
    CreateVFX(2403800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12401800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2400800, entity=2401800)
    IfFlagEnabled(3, 12401800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2402800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2402801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12404800)
    Restart()


@NeverRestart(12404841)
def Event_12404841():
    """Event 12404841"""
    DisableNetworkSync()
    EndIfFlagEnabled(12401800)
    IfFlagDisabled(1, 12401800)
    IfFlagEnabled(1, 12401802)
    IfFlagEnabled(1, 12404800)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2400800, entity=2401800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2402800, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2402801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12404801)
    Restart()


@NeverRestart(12404842)
def Event_12404842():
    """Event 12404842"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2401800, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12404843)
def Event_12404843():
    """Event 12404843"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=2401800, radius=6.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2401800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12404802)
def Event_12404802():
    """Event 12404802"""
    EndIfFlagEnabled(12401800)
    DisableAI(2400800)
    DisableHealthBar(2400800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12404800)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 12404223)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2400800, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12404223)
    EnableFlag(12404800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2400800, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2400800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2400800, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2400800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2400800)
    EnableBossHealthBar(2400800, name=502000)
    ForceAnimation(2400800, 7002)
    CreatePlayLog(name=160)
    StartPlayLogMeasurement(measurement_id=2410010, name=176, overwrite=True)


@NeverRestart(12404803)
def Event_12404803():
    """Event 12404803"""
    DisableNetworkSync()
    EndIfFlagEnabled(12401800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2403802)
    DisableSoundEvent(sound_id=2403803)
    IfFlagDisabled(1, 12401800)
    IfFlagEnabled(1, 12404802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12404801)
    IfCharacterInsideRegion(1, PLAYER, region=2402802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=2403802)
    IfCharacterHasTAEEvent(2, 2400800, tae_event_id=100)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12401800)
    IfFlagEnabled(2, 12404802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12404801)
    IfCharacterInsideRegion(2, PLAYER, region=2402802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2403802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2403803)


@NeverRestart(12404804)
def Event_12404804():
    """Event 12404804"""
    DisableNetworkSync()
    EndIfFlagEnabled(12401800)
    IfHealthGreaterThan(1, 2400800, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2400800, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=1)
    IfHealthGreaterThan(2, 2400800, value=0.0)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=2400800, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=0)
    Restart()


@NeverRestart(12404805)
def Event_12404805():
    """Event 12404805"""
    DisableNetworkSync()
    EndIfFlagEnabled(12401800)
    IfFlagEnabled(0, 12401800)
    DisableBossMusic(sound_id=2403802)
    DisableBossMusic(sound_id=2403803)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12404807)
def Event_12404807():
    """Event 12404807"""
    EndIfFlagEnabled(12401800)
    IfHealthLessThan(0, 2400800, value=0.5)
    AICommand(2400800, command_id=100, command_slot=1)
    ReplanAI(2400800)
    IfCharacterHasTAEEvent(0, 2400800, tae_event_id=100)
    AICommand(2400800, command_id=-1, command_slot=1)
    ReplanAI(2400800)


@NeverRestart(12404808)
def Event_12404808():
    """Event 12404808"""
    EndIfFlagEnabled(12401800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHasSpecialEffect(0, 2400800, 482)

    # --- 0 --- #
    DefineLabel(0)
    ChangeCharacterCloth(2400800, bit_count=15, state_id=2)


@RestartOnRest(12404810)
def Event_12404810(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect_id: int,
    special_effect_id_1: int,
    animation_id: int,
):
    """Event 12404810"""
    EndIfFlagEnabled(12401800)
    CreateNPCPart(2400800, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(2400800, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, 2400800, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, 2400800, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    CreateNPCPart(
        2400800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(2400800, npc_part_id=npc_part_id_1, material_sfx_id=73, material_vfx_id=73)
    WaitFrames(frames=1)
    ResetAnimation(2400800)
    ForceAnimation(2400800, animation_id)
    AddSpecialEffect(2400800, special_effect_id)
    CancelSpecialEffect(2400800, special_effect_id_1)
    ReplanAI(2400800)
    Wait(30.0)
    AICommand(2400800, command_id=1, command_slot=0)
    ReplanAI(2400800)
    IfCharacterHasTAEEvent(0, 2400800, tae_event_id=300)
    SetNPCPartHealth(2400800, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(2400800, special_effect_id_1)
    CancelSpecialEffect(2400800, special_effect_id)
    AICommand(2400800, command_id=-1, command_slot=0)
    ReplanAI(2400800)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(12404820)
def Event_12404820(_, special_effect: int, special_effect_1: int, bit_index: uchar, bit_index_1: uchar):
    """Event 12404820"""
    EndIfFlagEnabled(12401800)
    IfCharacterHasSpecialEffect(1, 2400800, special_effect)
    IfCharacterDoesNotHaveSpecialEffect(1, 2400800, special_effect_1)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(2400800, bit_index=bit_index_1, switch_type=OnOffChange.On)
    SetDisplayMask(2400800, bit_index=bit_index, switch_type=OnOffChange.Off)
    IfCharacterDoesNotHaveSpecialEffect(2, 2400800, special_effect)
    IfCharacterHasSpecialEffect(2, 2400800, special_effect_1)
    IfConditionTrue(0, input_condition=2)
    SetDisplayMask(2400800, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(2400800, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(12404830)
def Event_12404830():
    """Event 12404830"""
    IfCharacterHasSpecialEffect(1, 2400800, 2150)
    IfCharacterHasSpecialEffect(1, 2400800, 5639)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2400800, 3035)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(12406900)
def Event_12406900(_, region: int, anchor_entity: int, sound_id: int):
    """Event 12406900"""
    IfCharacterInsideRegion(0, PLAYER, region=region)
    PlaySoundEffect(anchor_entity, sound_id, sound_type=SoundType.a_Ambient)
    WaitFrames(frames=1)


@NeverRestart(12400990)
def Event_12400990():
    """Event 12400990"""
    EndIfThisEventFlagEnabled()
    IfPlayerStandingOnCollision(0, 2404101)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=194,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=194,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=194,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=194,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )


@NeverRestart(12407020)
def Event_12407020(_, flag: int, destination: int):
    """Event 12407020"""
    IfFlagEnabled(0, flag)
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    ForceAnimation(PLAYER, 101160, skip_transition=True)
    Wait(4.0)
    DisableFlag(flag)


@NeverRestart(12407040)
def Event_12407040(_, flag: int, respawn_point_id: int, flag_1: int):
    """Event 12407040"""
    IfFlagEnabled(0, flag)
    DisableFlag(flag)
    WarpPlayerToRespawnPoint(respawn_point_id)
    EnableFlag(flag_1)


@RestartOnRest(12407050)
def Event_12407050(_, flag: int, character: int, destination: int):
    """Event 12407050"""
    EndIfFlagEnabled(flag)
    IfCharacterBackreadEnabled(0, character)
    Move(character, destination=destination, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    ForceAnimation(character, 101165, loop=True)
    Wait(1.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    IfFlagEnabled(0, flag)
    ForceAnimation(character, 101166, wait_for_completion=True)
    DisableCharacter(character)


@NeverRestart(12407000)
def Event_12407000():
    """Event 12407000"""
    SkipLinesIfFlagRangeAnyEnabled(1, (9001, 9010))
    End()
    EnableFlag(9210)
    IfFlagDisabled(0, 9210)
    SkipLinesIfFlagDisabled(3, 9001)
    EnableFlag(12407811)
    EnableFlag(12407810)
    SetRespawnPoint(respawn_point=2402950)
    SkipLinesIfFlagDisabled(3, 9002)
    EnableFlag(12407831)
    EnableFlag(12407830)
    SetRespawnPoint(respawn_point=2402951)
    SkipLinesIfFlagDisabled(3, 9003)
    EnableFlag(12407851)
    EnableFlag(12407850)
    SetRespawnPoint(respawn_point=2402952)
    SkipLinesIfFlagDisabled(3, 9004)
    EnableFlag(12407871)
    EnableFlag(12407870)
    SetRespawnPoint(respawn_point=2402953)
    SkipLinesIfFlagDisabled(3, 9005)
    EnableFlag(12407891)
    EnableFlag(12407890)
    SetRespawnPoint(respawn_point=2402954)
    SkipLinesIfFlagDisabled(3, 9006)
    EnableFlag(12407911)
    EnableFlag(12407910)
    SetRespawnPoint(respawn_point=2402955)
    SkipLinesIfFlagDisabled(3, 9007)
    EnableFlag(12407931)
    EnableFlag(12407930)
    SetRespawnPoint(respawn_point=2402956)
    SkipLinesIfFlagDisabled(3, 9008)
    EnableFlag(12407951)
    EnableFlag(12407950)
    SetRespawnPoint(respawn_point=2402957)
    SkipLinesIfFlagDisabled(3, 9009)
    EnableFlag(12407971)
    EnableFlag(12407970)
    SetRespawnPoint(respawn_point=2402958)
    SkipLinesIfFlagDisabled(3, 9010)
    EnableFlag(12407991)
    EnableFlag(12407990)
    SetRespawnPoint(respawn_point=2402959)
    DisableFlagRange((9000, 9010))


@RestartOnRest(12404450)
def Event_12404450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 12404450"""
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(character, region=region, reaction_range=1.0)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12404400)
def Event_12404400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12404400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagDisabled(1, 2400)
    IfFlagDisabled(1, 2401)
    IfFlagDisabled(-1, flag_4)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, flag_1)
    IfFlagDisabled(2, flag_2)
    IfFlagDisabled(2, flag_3)
    IfClientTypeCountComparison(2, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagDisabled(2, 2400)
    IfFlagDisabled(2, 2401)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12404410)
def Event_12404410(
    _,
    sign_type: int,
    character: int,
    region: int,
    summon_flag: int,
    dismissal_flag: int,
    flag: int,
    flag_1: int,
    action_button_id: int,
):
    """Event 12404410"""
    SkipLinesIfFlagEnabled(1, summon_flag)
    DisableCharacter(character)
    SkipLinesIfFlagEnabled(3, dismissal_flag)
    IfClient(1)
    IfFlagEnabled(1, summon_flag)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(character)
    EndIfFlagEnabled(flag_1)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312)
    IfFlagDisabled(2, summon_flag)
    IfFlagDisabled(2, dismissal_flag)
    IfFlagEnabled(2, flag)
    IfFlagDisabled(2, flag_1)
    IfActionButtonParamActivated(2, action_button_id=action_button_id, entity=character)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682)
    SummonNPC(sign_type, character, region=region, summon_flag=summon_flag, dismissal_flag=dismissal_flag)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)
    DisableMapCollision(collision=2404120)


@RestartOnRest(12404460)
def Event_12404460(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 12404460"""
    EndIfClient()
    IfFlagEnabled(1, flag)
    IfCharacterInsideRegion(1, character, region=region)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(character)
    RotateToFaceEntity(character, region_1, animation=animation, wait_for_completion=True)
    IfCharacterInsideRegion(2, character, region=region_2)
    RestartIfConditionFalse(2)
    SetEventPoint(character, region=region_1, reaction_range=1.0)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    IfCharacterInsideRegion(0, character, region=region_3)
    EnableGravity(character)
    EnableCharacterCollision(character)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12404490)
def Event_12404490():
    """Event 12404490"""
    DisableNetworkSync()
    IfHost(1)
    IfFlagEnabled(1, 12404420)
    IfFlagDisabled(1, 12404430)
    IfFlagEnabled(1, 12404800)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect_WithUnknownEffect(2400910, 35)
    WaitFrames(frames=1)
    Restart()
