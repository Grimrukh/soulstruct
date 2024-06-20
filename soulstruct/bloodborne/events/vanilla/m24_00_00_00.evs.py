"""
Cathedral Ward

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


@ContinueOnRest(0)
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
    RunEvent(9220, slot=2, args=(2400710, 12404220, 12404221, 2400, 24))
    RunEvent(9240, slot=2, args=(2400710, 12404220, 12404221, 12404222, 24))
    RunEvent(9260, slot=2, args=(2400710, 12404220, 12404221, 12404222, 24))
    RunEvent(9280, slot=2, args=(2400710, 12404220, 12404221, 2400, 12404223, 24))
    SkipLinesIfFlagEnabled(7, 12400160)
    EnableFlag(2400)
    EnableFlag(2401)
    EnableFlag(2405)
    EnableFlag(2406)
    DisableFlag(2402)
    DisableFlag(2407)
    SkipLines(14)
    if FlagDisabled(12401800):
        DisableFlag(2400)
        DisableFlag(2401)
        DisableFlag(2405)
        DisableFlag(2406)
        DisableFlag(2402)
        DisableFlag(2407)
    else:
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
        action_button_id=10567,
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
        region_3=2402801,
    )
    Event_12404490()
    CreateObjectVFX(2401900, vfx_id=200, dummy_id=900130)
    CreateObjectVFX(2401901, vfx_id=200, dummy_id=900130)
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
        dummy_id=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12400191,
        obj=2401018,
        dummy_id=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    AND_15.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_15)
    if FlagEnabled(6646):
        EnableFlag(12401999)
    if FlagDisabled(12401999):
        EnableObject(2401501)
        DisableObject(2401505)
        EnableObjectActivation(2401501, obj_act_id=9942)
        DisableObjectActivation(2401505, obj_act_id=9942)
        Event_12400350(4, obj=2401501, obj_act_id=12400451)
    else:
        DisableObject(2401501)
        EnableObject(2401505)
        DisableObjectActivation(2401501, obj_act_id=9942)
        EnableObjectActivation(2401505, obj_act_id=9942)
        Event_12400350(5, obj=2401505, obj_act_id=12400455)
    AND_14.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_14)
    if FlagEnabled(6310):
        EnableFlag(12401998)
    if FlagDisabled(12401998):
        EnableObject(2401502)
        DisableObject(2401508)
        EnableObjectActivation(2401502, obj_act_id=9942)
        DisableObjectActivation(2401508, obj_act_id=9942)
        Event_12400350(7, obj=2401502, obj_act_id=12400452)
    else:
        DisableObject(2401502)
        EnableObject(2401508)
        DisableObjectActivation(2401502, obj_act_id=9942)
        EnableObjectActivation(2401508, obj_act_id=9942)
        Event_12400350(8, obj=2401508, obj_act_id=12400458)
    AND_13.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_13)
    if FlagEnabled(6311):
        EnableFlag(12401997)
    if FlagDisabled(12401997):
        EnableObject(2401504)
        DisableObject(2401507)
        EnableObjectActivation(2401504, obj_act_id=9942)
        DisableObjectActivation(2401507, obj_act_id=9942)
        Event_12400350(9, obj=2401504, obj_act_id=12400454)
    else:
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
    Event_12400850(
        0,
        vfx_id=2407020,
        vfx_id_1=2407021,
        vfx_id_2=2407022,
        flag=12400130,
        obj_act_id=0,
        seconds=0.0,
        anchor_entity=0,
        vfx_id_3=0,
    )
    Event_12400850(
        1,
        vfx_id=2407025,
        vfx_id_1=2407026,
        vfx_id_2=2407027,
        flag=12400132,
        obj_act_id=0,
        seconds=0.0,
        anchor_entity=0,
        vfx_id_3=0,
    )
    Event_12400850(
        2,
        vfx_id=2407028,
        vfx_id_1=2407029,
        vfx_id_2=2407030,
        flag=12400131,
        obj_act_id=0,
        seconds=0.0,
        anchor_entity=0,
        vfx_id_3=0,
    )
    Event_12400850(
        3,
        vfx_id=2406700,
        vfx_id_1=2406701,
        vfx_id_2=2406702,
        flag=12400133,
        obj_act_id=0,
        seconds=0.0,
        anchor_entity=0,
        vfx_id_3=0,
    )
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
    Event_12405210(1, character=2400116, special_effect=5696)
    Event_12405210(2, character=2400122, special_effect=5696)
    Event_12405210(4, character=2400125, special_effect=5696)
    Event_12405210(5, character=2400127, special_effect=5696)
    Event_12405210(7, character=2400161, special_effect=5696)
    Event_12405220(0, character=2400137, special_effect=5552, special_effect_1=5553, special_effect_2=5554)
    Event_12405220(1, character=2400210, special_effect=5555, special_effect_1=5556, special_effect_2=0)
    Event_12405220(2, character=2400211, special_effect=5555, special_effect_1=5556, special_effect_2=0)
    Event_12404100(0, entity=2401900, action_button_id=7405, text=10012005)
    Event_12404100(1, entity=2401901, action_button_id=7406, text=10012006)
    AICommand(2400420, command_id=100, command_slot=0)
    Event_12405600(1, character=2400400, region=2402022, radius=5.0, seconds=0.0)
    Event_12405600(2, character=2400400, region=2402017, radius=5.0, seconds=0.0)
    Event_12405600(3, character=2400126, region=2402012, radius=5.0, seconds=0.0)
    Event_12405600(4, character=2400127, region=2402013, radius=5.0, seconds=0.0)
    Event_12405600(5, character=2400128, region=2402013, radius=5.0, seconds=0.0)
    Event_12405600(6, character=2400136, region=2402015, radius=5.0, seconds=0.0)
    Event_12405600(7, character=2400137, region=2402015, radius=5.0, seconds=0.0)
    Event_12405600(8, character=2400125, region=2404302, radius=5.0, seconds=0.0)
    Event_12405600(10, character=2400231, region=2404312, radius=5.0, seconds=0.0)
    Event_12405600(11, character=2400508, region=2404320, radius=5.0, seconds=0.0)
    Event_12405600(12, character=2400508, region=2404310, radius=5.0, seconds=0.0)
    Event_12405600(13, character=2400120, region=2402073, radius=5.0, seconds=0.0)
    Event_12405600(14, character=2400121, region=2402073, radius=5.0, seconds=0.0)
    Event_12405600(15, character=2400392, region=2402016, radius=5.0, seconds=0.0)
    Event_12405600(18, character=2400401, region=2402029, radius=5.0, seconds=0.0)
    Event_12405600(19, character=2400401, region=2402017, radius=5.0, seconds=0.0)
    Event_12405600(20, character=2400106, region=2404310, radius=5.0, seconds=0.0)
    Event_12405600(22, character=2400122, region=2402081, radius=5.0, seconds=0.0)
    Event_12405600(23, character=2400116, region=2404302, radius=5.0, seconds=0.0)
    Event_12405600(24, character=2400211, region=2402075, radius=5.0, seconds=0.0)
    Event_12405660()
    Event_12405350(
        0,
        character=2400391,
        region=2402310,
        region_1=2409015,
        patrol_information_id=2403105,
        region_2=2402311,
    )
    Event_12405195()
    Event_12405370(0, character=2400210)
    Event_12405370(1, character=2400211)
    Event_12405670(0, character=2400203, region=2404332, region_1=2404301, radius=5.0, seconds=0.0)
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
    Event_12405682(0, character=2400107, region=2400002, seconds=6.0, flag=12405686, seconds_1=0.0)
    Event_12405682(2, character=2400109, region=2400001, seconds=1.0, flag=12405688, seconds_1=0.0)
    Event_12405682(3, character=2400110, region=2400004, seconds=1.0, flag=12405689, seconds_1=0.0)
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
    Event_12405600(41, character=2400410, region=2402028, radius=3.0, seconds=0.0)
    Event_12405600(42, character=2400420, region=2402511, radius=3.0, seconds=0.0)
    Event_12405600(43, character=2400423, region=2402511, radius=3.0, seconds=0.0)
    Event_12405600(44, character=2400501, region=2402157, radius=3.0, seconds=0.0)
    Event_12405600(45, character=2400502, region=2402157, radius=3.0, seconds=0.0)
    Event_12405600(46, character=2400503, region=2402157, radius=3.0, seconds=0.0)
    Event_12405600(47, character=2400504, region=2402157, radius=3.0, seconds=0.0)
    Event_12405600(48, character=2400505, region=2402157, radius=3.0, seconds=0.0)
    Event_12405600(49, character=2400506, region=2402157, radius=3.0, seconds=0.0)
    Event_12405600(50, character=2400507, region=2402157, radius=3.0, seconds=0.0)
    Event_12405700()
    Event_12405701(0, character=2400398, region=2404370)
    Event_12405701(1, character=2400399, region=2404371)
    Event_12405600(52, character=2400600, region=2402500, radius=1.0, seconds=0.0)
    Event_12405600(53, character=2400601, region=2402500, radius=1.0, seconds=0.0)
    Event_12405600(54, character=2400602, region=2402500, radius=1.0, seconds=0.0)
    Event_12405600(55, character=2400603, region=2402507, radius=5.0, seconds=0.0)
    Event_12405600(56, character=2400603, region=2402508, radius=5.0, seconds=0.0)
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
        ai_param_id_1=273140,
    )
    Event_12405000(
        1,
        character=2400156,
        animation_id=7014,
        animation_id_1=7018,
        ai_param_id=263252,
        ai_param_id_1=263251,
    )
    Event_12405010(0, character=2400205, animation_id=7012, event_slot=0, ai_param_id=273130)
    Event_12405010(1, character=2400156, animation_id=7015, event_slot=1, ai_param_id=263250)
    Event_12405020(
        0,
        character=2400207,
        animation_id=7010,
        animation_id_1=7013,
        ai_param_id=273120,
        ai_param_id_1=273110,
    )
    Event_12405020(
        1,
        character=2400126,
        animation_id=7010,
        animation_id_1=7013,
        ai_param_id=273120,
        ai_param_id_1=273110,
    )
    Event_12405020(
        2,
        character=2400203,
        animation_id=7010,
        animation_id_1=7013,
        ai_param_id=273120,
        ai_param_id_1=273110,
    )
    Event_12405020(
        4,
        character=2400119,
        animation_id=7010,
        animation_id_1=7013,
        ai_param_id=273120,
        ai_param_id_1=273110,
    )
    Event_12405030(0, character=2400207, animation_id=7012, event_slot=0, ai_param_id=273100)
    Event_12405030(1, character=2400126, animation_id=7012, event_slot=1, ai_param_id=273100)
    Event_12405030(2, character=2400203, animation_id=7012, event_slot=2, ai_param_id=273100)
    Event_12405030(4, character=2400119, animation_id=7012, event_slot=4, ai_param_id=273100)
    Event_12405335()
    Event_12405120(1, character=2400156, special_effect=5569)
    Event_12405120(2, character=2400162, special_effect=5569)
    Event_12405120(3, character=2400220, special_effect=5557)
    Event_12405120(4, character=2400116, special_effect=5557)
    Event_12405120(5, character=2400114, special_effect=5557)
    Event_12405120(6, character=2400127, special_effect=5557)
    Event_12405120(8, character=2400139, special_effect=5557)
    Event_12405120(9, character=2400137, special_effect=5557)
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
        character=2400114,
    )
    Event_12405430(
        1,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405500,
        character=2400114,
    )
    Event_12405430(
        2,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405501,
        character=2400126,
    )
    Event_12405430(
        3,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405501,
        character=2400126,
    )
    Event_12405430(
        6,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405503,
        character=2400133,
    )
    Event_12405430(
        7,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405503,
        character=2400133,
    )
    Event_12405430(
        8,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405504,
        character=2400203,
    )
    Event_12405430(
        9,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405504,
        character=2400203,
    )
    Event_12405430(
        10,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405505,
        character=2400205,
    )
    Event_12405430(
        11,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405505,
        character=2400205,
    )
    Event_12405430(
        14,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405507,
        character=2400207,
    )
    Event_12405430(
        15,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405507,
        character=2400207,
    )
    Event_12405430(
        16,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        part_health=40,
        flag=12405508,
        character=2400603,
    )
    Event_12405430(
        17,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        part_health=40,
        flag=12405508,
        character=2400603,
    )
    Event_12405400(
        0,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect=5907,
        flag=12405500,
        flag_1=12405530,
        character=2400114,
    )
    Event_12405400(
        1,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect=5907,
        flag=12405500,
        flag_1=12405560,
        character=2400114,
    )
    Event_12405400(
        2,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect=5907,
        flag=12405501,
        flag_1=12405531,
        character=2400126,
    )
    Event_12405400(
        3,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect=5907,
        flag=12405501,
        flag_1=12405561,
        character=2400126,
    )
    Event_12405400(
        6,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect=5907,
        flag=12405503,
        flag_1=12405533,
        character=2400133,
    )
    Event_12405400(
        7,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect=5907,
        flag=12405503,
        flag_1=12405563,
        character=2400133,
    )
    Event_12405400(
        8,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect=5907,
        flag=12405504,
        flag_1=12405534,
        character=2400203,
    )
    Event_12405400(
        9,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect=5907,
        flag=12405504,
        flag_1=12405564,
        character=2400203,
    )
    Event_12405400(
        10,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect=5907,
        flag=12405505,
        flag_1=12405535,
        character=2400205,
    )
    Event_12405400(
        11,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect=5907,
        flag=12405505,
        flag_1=12405565,
        character=2400205,
    )
    Event_12405400(
        14,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect=5907,
        flag=12405507,
        flag_1=12405537,
        character=2400207,
    )
    Event_12405400(
        15,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect=5907,
        flag=12405507,
        flag_1=12405567,
        character=2400207,
    )
    Event_12405400(
        16,
        npc_part_id=2490,
        npc_part_id_1=2490,
        part_index=7,
        animation_id=7003,
        special_effect=5907,
        flag=12405508,
        flag_1=12405538,
        character=2400603,
    )
    Event_12405400(
        17,
        npc_part_id=2491,
        npc_part_id_1=2491,
        part_index=8,
        animation_id=7000,
        special_effect=5907,
        flag=12405508,
        flag_1=12405568,
        character=2400603,
    )
    Event_12405460(0, tae_event_id=10, tae_event_id_1=40, flag=12405530, character=2400114, bit_index=0, bit_index_1=10)
    Event_12405460(1, tae_event_id=30, tae_event_id_1=40, flag=12405560, character=2400114, bit_index=1, bit_index_1=11)
    Event_12405460(2, tae_event_id=10, tae_event_id_1=40, flag=12405531, character=2400126, bit_index=0, bit_index_1=10)
    Event_12405460(3, tae_event_id=30, tae_event_id_1=40, flag=12405561, character=2400126, bit_index=1, bit_index_1=11)
    Event_12405460(6, tae_event_id=10, tae_event_id_1=40, flag=12405533, character=2400133, bit_index=0, bit_index_1=10)
    Event_12405460(7, tae_event_id=30, tae_event_id_1=40, flag=12405563, character=2400133, bit_index=1, bit_index_1=11)
    Event_12405460(8, tae_event_id=10, tae_event_id_1=40, flag=12405534, character=2400203, bit_index=0, bit_index_1=10)
    Event_12405460(9, tae_event_id=30, tae_event_id_1=40, flag=12405564, character=2400203, bit_index=1, bit_index_1=11)
    Event_12405460(
        10,
        tae_event_id=10,
        tae_event_id_1=40,
        flag=12405535,
        character=2400205,
        bit_index=0,
        bit_index_1=10,
    )
    Event_12405460(
        11,
        tae_event_id=30,
        tae_event_id_1=40,
        flag=12405565,
        character=2400205,
        bit_index=1,
        bit_index_1=11,
    )
    Event_12405460(
        14,
        tae_event_id=10,
        tae_event_id_1=40,
        flag=12405537,
        character=2400207,
        bit_index=0,
        bit_index_1=10,
    )
    Event_12405460(
        15,
        tae_event_id=30,
        tae_event_id_1=40,
        flag=12405567,
        character=2400207,
        bit_index=1,
        bit_index_1=11,
    )
    Event_12405460(
        16,
        tae_event_id=10,
        tae_event_id_1=40,
        flag=12405538,
        character=2400603,
        bit_index=0,
        bit_index_1=10,
    )
    Event_12405460(
        17,
        tae_event_id=30,
        tae_event_id_1=40,
        flag=12405568,
        character=2400603,
        bit_index=1,
        bit_index_1=11,
    )
    Event_12405790(0, obj=2401150, flag=9802, dummy_id=924110)
    Event_12405790(1, obj=2401151, flag=9801, dummy_id=924110)
    Event_12405790(2, obj=2401152, flag=6001, dummy_id=924113)
    Event_12405790(3, obj=2401153, flag=9802, dummy_id=924110)
    Event_12405790(4, obj=2401154, flag=9801, dummy_id=924113)
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
        special_effect=480,
        special_effect_1=490,
        animation_id=8020,
    )
    Event_12404810(
        1,
        npc_part_id=2401,
        npc_part_id_1=2401,
        part_index=2,
        part_health=150,
        special_effect=481,
        special_effect_1=491,
        animation_id=8000,
    )
    Event_12404810(
        2,
        npc_part_id=2402,
        npc_part_id_1=2402,
        part_index=3,
        part_health=150,
        special_effect=482,
        special_effect_1=492,
        animation_id=8010,
    )
    Event_12404810(
        3,
        npc_part_id=2403,
        npc_part_id_1=2403,
        part_index=4,
        part_health=200,
        special_effect=483,
        special_effect_1=493,
        animation_id=8030,
    )
    Event_12404810(
        4,
        npc_part_id=2404,
        npc_part_id_1=2404,
        part_index=5,
        part_health=200,
        special_effect=484,
        special_effect_1=494,
        animation_id=8040,
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

    # --- Label 0 --- #
    DefineLabel(0)


@ContinueOnRest(50)
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
    AND_1.Add(CharacterHuman(PLAYER))
    if not AND_1:
        return
    AND_2.Add(PlayerInsightAmount() < 50)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableFlag(12404001)
    EnableFlag(12404002)
    EnableFlag(12404003)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(PlayerInsightAmount() < 40)
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    EnableFlag(12404001)
    EnableFlag(12404002)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_4.Add(PlayerInsightAmount() < 15)
    if AND_4:
        return
    EnableFlag(12404002)


@ContinueOnRest(12404100)
def Event_12404100(_, entity: int, action_button_id: int, text: int):
    """Event 12404100"""
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    DisplayDialog(text=text, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12400070)
def Event_12400070(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 12400070"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    Wait(0.0)


@ContinueOnRest(12400080)
def Event_12400080(_, entity: int, flag: int, flag_1: int, action_button_id: int):
    """Event 12400080"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    AND_3.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_3)
    DisplayDialog(text=10010160, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12400095)
def Event_12400095(_, entity: int):
    """Event 12400095"""
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2400040, entity=entity))
    
    DisplayDialog(text=10010171, anchor_entity=PLAYER, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12400100)
def Event_12400100(_, obj: int, obj_act_id: int, obj_act_id_1: int, obj_act_id_2: int):
    """Event 12400100"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_2)


@ContinueOnRest(12400125)
def Event_12400125():
    """Event 12400125"""
    OR_1.Add(ObjectActivated(obj_act_id=12400162))
    OR_1.Add(ObjectActivated(obj_act_id=12400163))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(12400177))
    AND_1.Add(FlagDisabled(12400178))
    
    MAIN.Await(AND_1)
    
    EnableFlag(12400177)
    EnableFlag(12400178)
    ForceAnimation(2401207, 1)
    Wait(1.0)
    CreateObjectVFX(2401207, vfx_id=200, dummy_id=920204)
    CreateObjectVFX(2401207, vfx_id=201, dummy_id=920205)
    Wait(3.0)
    DisableFlag(12400178)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    Restart()


@ContinueOnRest(12400126)
def Event_12400126():
    """Event 12400126"""
    OR_2.Add(ObjectActivated(obj_act_id=12400162))
    OR_2.Add(ObjectActivated(obj_act_id=12400163))
    AND_1.Add(OR_2)
    AND_1.Add(FlagEnabled(12400177))
    AND_1.Add(FlagDisabled(12400178))
    
    MAIN.Await(AND_1)
    
    DisableFlag(12400177)
    EnableFlag(12400178)
    ForceAnimation(2401207, 2)
    Wait(1.0)
    CreateObjectVFX(2401207, vfx_id=200, dummy_id=920204)
    CreateObjectVFX(2401207, vfx_id=201, dummy_id=920205)
    Wait(3.0)
    DisableFlag(12400178)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    Restart()


@ContinueOnRest(12400127)
def Event_12400127():
    """Event 12400127"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(12400178))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401006))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12400128)
def Event_12400128():
    """Event 12400128"""
    GotoIfFlagEnabled(Label.L0, flag=12400177)
    EndOfAnimation(obj=2401207, animation_id=2)
    EnableObjectActivation(2401006, obj_act_id=2400000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2401207, animation_id=1)
    EnableObjectActivation(2401006, obj_act_id=2400000)


@ContinueOnRest(12400130)
def Event_12400130(_, obj: int, animation_id: int, obj_act_id: int, flag: int):
    """Event 12400130"""
    if FlagEnabled(flag):
        EndOfAnimation(obj=obj, animation_id=animation_id)
        DisableObjectActivation(obj, obj_act_id=-1)
        NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=0)


@ContinueOnRest(12400146)
def Event_12400146():
    """Event 12400146"""
    AND_1.Add(FlagEnabled(12400150))
    AND_2.Add(FlagDisabled(12400150))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(4, input_condition=AND_1)
    EndOfAnimation(obj=2401101, animation_id=15)
    EnableObjectActivation(2401003, obj_act_id=2400000)
    DisableObjectActivation(2401004, obj_act_id=2400000)
    SkipLines(3)
    EndOfAnimation(obj=2401101, animation_id=0)
    DisableObjectActivation(2401003, obj_act_id=2400000)
    EnableObjectActivation(2401004, obj_act_id=2400000)


@ContinueOnRest(12400147)
def Event_12400147():
    """Event 12400147"""
    AND_3.Add(FlagEnabled(12400150))
    AND_3.Add(FlagEnabled(12400151))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    AND_1.Add(FlagEnabled(12400150))
    AND_1.Add(FlagDisabled(12400151))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402054))
    AND_2.Add(FlagEnabled(12400150))
    AND_2.Add(FlagDisabled(12400151))
    AND_2.Add(ObjectActivated(obj_act_id=12400161))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12400151)
    ForceAnimation(2401101, 1, wait_for_completion=True)
    ForceAnimation(2401101, 13, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2402055))
    
    ForceAnimation(2401101, 14, wait_for_completion=True)
    DisableFlag(12400150)
    DisableFlag(12400151)
    EnableObjectActivation(2401003, obj_act_id=2400000)
    DisableObjectActivation(2401004, obj_act_id=2400000)
    Restart()


@ContinueOnRest(12400148)
def Event_12400148():
    """Event 12400148"""
    AND_3.Add(FlagDisabled(12400150))
    AND_3.Add(FlagEnabled(12400151))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    AND_1.Add(FlagDisabled(12400150))
    AND_1.Add(FlagDisabled(12400151))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402055))
    AND_2.Add(FlagDisabled(12400150))
    AND_2.Add(FlagDisabled(12400151))
    AND_2.Add(ObjectActivated(obj_act_id=12400160))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12400151)
    ForceAnimation(2401101, 16, wait_for_completion=True)
    ForceAnimation(2401101, 17, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2402054))
    
    ForceAnimation(2401101, 7, wait_for_completion=True)
    EnableFlag(12400150)
    DisableFlag(12400151)
    DisableObjectActivation(2401003, obj_act_id=2400000)
    EnableObjectActivation(2401004, obj_act_id=2400000)
    Restart()


@ContinueOnRest(12400149)
def Event_12400149():
    """Event 12400149"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(12400150))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401003))
    AND_2.Add(FlagDisabled(12400150))
    AND_2.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401004))
    AND_3.Add(FlagEnabled(12400151))
    AND_3.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401003))
    AND_4.Add(FlagEnabled(12400151))
    AND_4.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401004))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12400155)
def Event_12400155():
    """Event 12400155"""
    OR_1.Add(ObjectActivated(obj_act_id=12400164))
    OR_1.Add(ObjectActivated(obj_act_id=12400165))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(12400157))
    AND_1.Add(FlagDisabled(12405179))
    
    MAIN.Await(AND_1)
    
    EnableFlag(12400157)
    EnableFlag(12405179)
    ForceAnimation(2401208, 1)
    Wait(1.0)
    CreateObjectVFX(2401208, vfx_id=200, dummy_id=920204)
    CreateObjectVFX(2401208, vfx_id=201, dummy_id=920205)
    Wait(3.0)
    DisableFlag(12405179)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    Restart()


@ContinueOnRest(12400156)
def Event_12400156():
    """Event 12400156"""
    OR_2.Add(ObjectActivated(obj_act_id=12400164))
    OR_2.Add(ObjectActivated(obj_act_id=12400165))
    AND_1.Add(OR_2)
    AND_1.Add(FlagEnabled(12400157))
    AND_1.Add(FlagDisabled(12405179))
    
    MAIN.Await(AND_1)
    
    DisableFlag(12400157)
    EnableFlag(12405179)
    ForceAnimation(2401208, 2)
    Wait(1.0)
    CreateObjectVFX(2401208, vfx_id=200, dummy_id=920204)
    CreateObjectVFX(2401208, vfx_id=201, dummy_id=920205)
    Wait(3.0)
    DisableFlag(12405179)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    Restart()


@ContinueOnRest(12400158)
def Event_12400158():
    """Event 12400158"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(12405179))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401008))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12400159)
def Event_12400159():
    """Event 12400159"""
    GotoIfFlagEnabled(Label.L0, flag=12400157)
    EndOfAnimation(obj=2401208, animation_id=2)
    EnableObjectActivation(2401008, obj_act_id=2400000)
    End()

    # --- Label 0 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2400650, 7022, loop=True)
    AND_1.Add(PlayerDoesNotHaveGood(4011))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2400030, entity=2401220))
    AND_2.Add(PlayerHasGood(4011))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2400030, entity=2401220))
    AND_3.Add(ObjectActivated(obj_act_id=12400170))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_1)
    GotoIfLastConditionResultTrue(Label.L2, input_condition=AND_2)
    DisableObjectActivation(2401014, obj_act_id=2400000)
    ForceAnimation(2400650, 7024)
    WaitFrames(frames=74)
    ForceAnimation(2400650, 7020, loop=True)
    WaitFrames(frames=31)
    ForceAnimation(2401220, 1)
    WaitFrames(frames=30)
    CreateObjectVFX(2401220, vfx_id=200, dummy_id=920204)
    CreateObjectVFX(2401220, vfx_id=201, dummy_id=920205)
    EnableFlag(12400160)
    if FlagEnabled(12401800):
        return
    DisableFlag(2400)
    DisableFlag(2401)
    DisableFlag(2405)
    DisableFlag(2406)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableObjectActivation(2401014, obj_act_id=2400000)
    FaceEntity(PLAYER, 2401014, animation=101310)
    Wait(1.0)
    ForceAnimation(2400650, 7023)
    ForceAnimation(2401014, 1)
    WaitFrames(frames=105)
    ForceAnimation(2401220, 1)
    WaitFrames(frames=24)
    ForceAnimation(2400650, 7022, loop=True)
    WaitFrames(frames=6)
    CreateObjectVFX(2401220, vfx_id=200, dummy_id=920204)
    CreateObjectVFX(2401220, vfx_id=201, dummy_id=920205)
    DisplayDialog(text=10010174, number_buttons=NumberButtons.OneButton)
    EnableFlag(12400160)
    if FlagEnabled(12401800):
        return
    DisableFlag(2400)
    DisableFlag(2401)
    DisableFlag(2405)
    DisableFlag(2406)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisplayDialog(text=10010173, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12400161)
def Event_12400161():
    """Event 12400161"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(12400160))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401014))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12400174)
def Event_12400174():
    """Event 12400174"""
    GotoIfFlagEnabled(Label.L0, flag=12400168)
    EnableFlag(12400167)

    # --- Label 0 --- #
    DefineLabel(0)


@ContinueOnRest(12400175)
def Event_12400175():
    """Event 12400175"""
    GotoIfFlagDisabled(Label.L0, flag=12400168)
    EndOfAnimation(obj=2401209, animation_id=2)
    EnableFlag(12400169)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(ObjectActivated(obj_act_id=12400172))
    OR_1.Add(ObjectActivated(obj_act_id=12400173))
    
    MAIN.Await(OR_1)
    
    DisableFlag(12400167)
    EnableFlag(12400169)
    EnableFlag(12400168)
    EnableFlag(12405175)
    DisableObjectActivation(2401015, obj_act_id=2400000)
    DisableObjectActivation(2401016, obj_act_id=2400000)
    ForceAnimation(2401209, 2)
    Wait(1.0)
    CreateObjectVFX(2401209, vfx_id=200, dummy_id=920204)
    CreateObjectVFX(2401209, vfx_id=201, dummy_id=920205)
    Wait(3.0)
    DisableFlag(12405175)
    EnableObjectActivation(2401015, obj_act_id=2400000)
    EnableObjectActivation(2401016, obj_act_id=2400000)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(ObjectActivated(obj_act_id=12400172))
    OR_2.Add(ObjectActivated(obj_act_id=12400173))
    
    MAIN.Await(OR_2)
    
    EnableFlag(12400167)
    DisableFlag(12400168)
    EnableFlag(12405175)
    DisableObjectActivation(2401015, obj_act_id=2400000)
    DisableObjectActivation(2401016, obj_act_id=2400000)
    ForceAnimation(2401209, 1)
    Wait(1.0)
    CreateObjectVFX(2401209, vfx_id=200, dummy_id=920204)
    CreateObjectVFX(2401209, vfx_id=201, dummy_id=920205)
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
    AND_1.Add(FlagEnabled(12405175))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=entity))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, display_distance=0.0, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12400185)
def Event_12400185():
    """Event 12400185"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2401012, animation_id=1)
    DisableObjectActivation(2401013, obj_act_id=2400000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=12400123))
    
    ForceAnimation(2401012, 1)


@ContinueOnRest(12400200)
def Event_12400200(_, character: int, flag: int):
    """Event 12400200"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterHuman(PLAYER))
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(0.0)


@ContinueOnRest(12400250)
def Event_12400250(_, obj_act_id: int, text: int, anchor_entity: int):
    """Event 12400250"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    DisplayDialog(text=text, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)


@ContinueOnRest(12400300)
def Event_12400300():
    """Event 12400300"""
    GotoIfFlagEnabled(Label.L2, flag=9802)
    GotoIfFlagEnabled(Label.L1, flag=9801)
    GotoIfFlagEnabled(Label.L0, flag=9800)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2404000)
    DisableMapPiece(map_piece_id=2404001)
    DisableMapPiece(map_piece_id=2404002)
    DisableCharacter(2400321)
    DisableCharacter(2400322)
    DisableMapPiece(map_piece_id=2404750)
    DisableMapPiece(map_piece_id=2404751)
    Goto(Label.L3)

    # --- Label 1 --- #
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

    # --- Label 2 --- #
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

    # --- Label 3 --- #
    DefineLabel(3)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9800))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9801))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9802))
    
    MAIN.Await(OR_1)
    
    Restart()


@ContinueOnRest(12400765)
def Event_12400765():
    """Event 12400765"""
    OR_1.Add(FlagEnabled(9802))
    OR_1.Add(FlagEnabled(12404001))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    DisableObject(2400898)
    ForceAnimation(2400898, 0, loop=True)
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.On)
    AddSpecialEffect(2400899, 5686)
    EnableFlag(12405263)
    End()

    # --- Label 0 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(12400401)
def Event_12400401():
    """Event 12400401"""
    AND_1.Add(FlagEnabled(72400440))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1400, 1402))
    EnableFlag(1401)
    ForceAnimation(2401200, 1, wait_for_completion=True)
    EnableFlag(12400131)
    SaveRequest()


@ContinueOnRest(12400402)
def Event_12400402():
    """Event 12400402"""
    AND_1.Add(FlagEnabled(72400440))
    
    MAIN.Await(AND_1)
    
    Move(2400830, destination=2402033, destination_type=CoordEntityType.Region, short_move=True)


@ContinueOnRest(12400403)
def Event_12400403():
    """Event 12400403"""
    if ThisEventFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(72400441))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(37000, host_only=False)


@ContinueOnRest(12400410)
def Event_12400410():
    """Event 12400410"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterHuman(PLAYER))
    if not AND_1:
        return
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 6421))
    
    RunEvent(9350, slot=0, args=(1,))


@ContinueOnRest(12400420)
def Event_12400420():
    """Event 12400420"""
    DisableSoundEvent(sound_id=2406831)
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(9801))
    
    Wait(4.0)
    EnableSoundEvent(sound_id=2406831)


@ContinueOnRest(12400750)
def Event_12400750():
    """Event 12400750"""
    DisableSoundEvent(sound_id=2406832)
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=7030, entity=2401210))
    
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

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2401210, animation_id=2)
    NotifyDoorEventSoundDampening(obj=2401210, state=DoorState.DoorOpening)


@RestartOnRest(12400780)
def Event_12400780(_, attacker__character: int):
    """Event 12400780"""
    AND_2.Add(CharacterHuman(PLAYER))
    if not AND_2:
        return
    AND_1.Add(CharacterAlive(attacker__character))
    AND_1.Add(Attacked(attacked_entity=PLAYER, attacker=attacker__character))
    AND_1.Add(HealthRatio(PLAYER) == 0.0)
    AND_1.Add(FlagEnabled(9401))
    AND_1.Add(FlagEnabled(9404))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9420)


@RestartOnRest(12400791)
def Event_12400791(_, character: int):
    """Event 12400791"""
    GotoIfFlagEnabled(Label.L0, flag=9802)
    if FlagEnabled(9453):
        return

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBackread(character)


@RestartOnRest(12400797)
def Event_12400797():
    """Event 12400797"""
    GotoIfFlagEnabled(Label.L0, flag=9802)
    if FlagEnabled(9453):
        DisableBackread(2400350)
        DisableBackread(2400351)
        DisableBackread(2400352)
        End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBackread(2400362)


@ContinueOnRest(12400823)
def Event_12400823():
    """Event 12400823"""
    AND_1.Add(FlagEnabled(12400827))
    AND_2.Add(FlagDisabled(12400827))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(4, input_condition=AND_1)
    EndOfAnimation(obj=2401102, animation_id=30)
    EnableObjectActivation(2401104, obj_act_id=2400000)
    DisableObjectActivation(2401103, obj_act_id=2400000)
    SkipLines(3)
    EndOfAnimation(obj=2401102, animation_id=0)
    DisableObjectActivation(2401104, obj_act_id=2400000)
    EnableObjectActivation(2401103, obj_act_id=2400000)


@ContinueOnRest(12400824)
def Event_12400824():
    """Event 12400824"""
    AND_3.Add(FlagEnabled(12400827))
    AND_3.Add(FlagEnabled(12400828))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    AND_1.Add(FlagEnabled(12400827))
    AND_1.Add(FlagDisabled(12400828))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402058))
    AND_2.Add(FlagEnabled(12400827))
    AND_2.Add(FlagDisabled(12400828))
    AND_2.Add(ObjectActivated(obj_act_id=12400169))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12400828)
    ForceAnimation(2401102, 1, wait_for_completion=True)
    ForceAnimation(2401102, 28, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2402059))
    
    ForceAnimation(2401102, 29, wait_for_completion=True)
    DisableFlag(12400827)
    DisableFlag(12400828)
    EnableObjectActivation(2401104, obj_act_id=2400000)
    DisableObjectActivation(2401103, obj_act_id=2400000)
    Restart()


@ContinueOnRest(12400825)
def Event_12400825():
    """Event 12400825"""
    AND_3.Add(FlagDisabled(12400827))
    AND_3.Add(FlagEnabled(12400828))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    AND_1.Add(FlagDisabled(12400827))
    AND_1.Add(FlagDisabled(12400828))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402059))
    AND_2.Add(FlagDisabled(12400827))
    AND_2.Add(FlagDisabled(12400828))
    AND_2.Add(ObjectActivated(obj_act_id=12400168))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12400828)
    ForceAnimation(2401102, 31, wait_for_completion=True)
    ForceAnimation(2401102, 32, wait_for_completion=True)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2402058))
    
    ForceAnimation(2401102, 7, wait_for_completion=True)
    EnableFlag(12400827)
    DisableFlag(12400828)
    DisableObjectActivation(2401104, obj_act_id=2400000)
    EnableObjectActivation(2401103, obj_act_id=2400000)
    Restart()


@ContinueOnRest(12400826)
def Event_12400826():
    """Event 12400826"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(12400827))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401104))
    AND_2.Add(FlagDisabled(12400827))
    AND_2.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401103))
    AND_3.Add(FlagEnabled(12400828))
    AND_3.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401104))
    AND_4.Add(FlagEnabled(12400828))
    AND_4.Add(ActionButtonParamActivated(action_button_id=7100, entity=2401103))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
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
    if FlagEnabled(flag):
        CreateVFX(vfx_id_1)
        CreateVFX(vfx_id_2)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
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
    if FlagEnabled(12400133):
        CreateVFX(2406712)
        CreateVFX(2406713)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=12400112))
    
    Wait(6.0)
    CreateVFX(2406711)
    CreateTemporaryVFX(vfx_id=920206, anchor_entity=2401204, dummy_id=200, anchor_type=CoordEntityType.Object)
    CreateTemporaryVFX(vfx_id=920207, anchor_entity=2401204, dummy_id=201, anchor_type=CoordEntityType.Object)
    Wait(4.0)
    CreateVFX(2406712)
    CreateVFX(2406713)


@RestartOnRest(12405000)
def Event_12405000(_, character: int, animation_id: int, animation_id_1: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12405000"""
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id, loop=True)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.0))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    
    MAIN.Await(OR_1)
    
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ForceAnimation(character, animation_id_1, loop=True)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    Restart()


@RestartOnRest(12405010)
def Event_12405010(_, character: int, animation_id: int, event_slot: int, ai_param_id: int):
    """Event 12405010"""
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id)
    StopEvent(event_id=12405000, event_slot=event_slot)


@ContinueOnRest(12405020)
def Event_12405020(_, character: int, animation_id: int, animation_id_1: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12405020"""
    MAIN.Await(FlagEnabled(9801))
    
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id, loop=True)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=1.0))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    
    MAIN.Await(OR_1)
    
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ForceAnimation(character, animation_id_1, loop=True)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    Restart()


@ContinueOnRest(12405030)
def Event_12405030(_, character: int, animation_id: int, event_slot: int, ai_param_id: int):
    """Event 12405030"""
    MAIN.Await(FlagEnabled(9801))
    
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id)
    StopEvent(event_id=12405020, event_slot=event_slot)


@RestartOnRest(12405060)
def Event_12405060(_, character: int, animation_id: int, animation_id_1: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12405060"""
    SetAIParamID(character, ai_param_id=ai_param_id)
    ForceAnimation(character, animation_id, loop=True)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.0))
    AND_1.Add(HasAIStatus(2400160, ai_status=AIStatusType.Battle))
    AND_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_2)
    ForceAnimation(character, animation_id_1)


@RestartOnRest(12405080)
def Event_12405080(_, flag: int, character: int, region: int, radius: float):
    """Event 12405080"""
    MAIN.Await(FlagEnabled(flag))
    
    AICommand(character, command_id=10, command_slot=0)
    SetNest(character, region=region)
    OR_1.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405100)
def Event_12405100(_, character: int, region: int, region_1: int):
    """Event 12405100"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2404306))
    AND_2.Add(FlagEnabled(12405431))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    MAIN.Await(AND_3)
    
    DisableAI(character)
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_2)
    SetNest(character, region=region)
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_1)
    SetNest(character, region=region_1)
    AICommand(character, command_id=10, command_slot=0)
    EnableAI(character)
    ReplanAI(character)
    OR_2.Add(CharacterInsideRegion(character, region=region))
    OR_2.Add(CharacterInsideRegion(character, region=region_1))
    
    MAIN.Await(OR_2)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405110)
def Event_12405110(_, region: int, obj: int, vfx_id: int, obj_1: int, launch_angle_y: int, flag: int, name: int):
    """Event 12405110"""
    MAIN.Await(ObjectNotDestroyed(obj_1))
    
    DisableFlag(flag)
    SkipLinesIfFlagDisabled(2, flag)
    EndOfAnimation(obj=obj, animation_id=0)
    SkipLines(9)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(ObjectNotDestroyed(obj_1))
    AND_1.Add(OR_1)
    AND_2.Add(ObjectDestroyed(obj_1))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_2)
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_1)
    ForceAnimation(obj, 0, wait_for_completion=True)
    End()
    PlaySoundEffect(obj, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(obj, 0, wait_for_completion=True)
    EnableFlag(flag)
    CreateTemporaryVFX(vfx_id=150005, anchor_entity=obj, dummy_id=101, anchor_type=CoordEntityType.Object)
    DeleteVFX(vfx_id, erase_root_only=False)
    EndIfLastConditionResultTrue(input_condition=AND_2)
    Wait(0.20000000298023224)
    CreatePlayLog(name=name)
    ShootProjectile(
        owner_entity=2400000,
        source_entity=obj_1,
        dummy_id=101,
        behavior_id=5071,
        launch_angle_x=0,
        launch_angle_y=launch_angle_y,
        launch_angle_z=0,
    )
    PlaySoundEffect(obj_1, 243007000, sound_type=SoundType.a_Ambient)
    CreateTemporaryVFX(vfx_id=929208, anchor_entity=obj_1, dummy_id=101, anchor_type=CoordEntityType.Object)
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=2400000,
        source_entity=obj_1,
        dummy_id=101,
        behavior_id=5071,
        launch_angle_x=0,
        launch_angle_y=launch_angle_y,
        launch_angle_z=0,
    )
    PlaySoundEffect(obj_1, 243007000, sound_type=SoundType.a_Ambient)
    CreateTemporaryVFX(vfx_id=929208, anchor_entity=obj_1, dummy_id=101, anchor_type=CoordEntityType.Object)
    Wait(0.699999988079071)
    ShootProjectile(
        owner_entity=2400000,
        source_entity=obj_1,
        dummy_id=101,
        behavior_id=5071,
        launch_angle_x=0,
        launch_angle_y=launch_angle_y,
        launch_angle_z=0,
    )
    PlaySoundEffect(obj_1, 243007000, sound_type=SoundType.a_Ambient)
    CreateTemporaryVFX(vfx_id=929208, anchor_entity=obj_1, dummy_id=101, anchor_type=CoordEntityType.Object)
    Wait(3.0)
    AND_3.Add(CharacterOutsideRegion(PLAYER, region=region))
    AND_3.Add(ObjectNotDestroyed(obj_1))
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    PlaySoundEffect(obj_1, 243007001, sound_type=SoundType.a_Ambient)
    PlaySoundEffect(obj, 990100001, sound_type=SoundType.o_Object)
    ForceAnimation(obj, 1, wait_for_completion=True)
    Restart()


@ContinueOnRest(12405120)
def Event_12405120(_, character: int, special_effect: int):
    """Event 12405120"""
    WaitFrames(frames=1)
    AddSpecialEffect(character, special_effect)


@RestartOnRest(12405130)
def Event_12405130(_, character: int, event_id: int, event_slot: int):
    """Event 12405130"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402151))
    
    MAIN.Await(AND_1)
    
    EnableAI(character)
    StopEvent(event_id=event_id, event_slot=event_slot)


@RestartOnRest(12405140)
def Event_12405140():
    """Event 12405140"""
    GotoIfThisEventFlagDisabled(Label.L0)
    SetAIParamID(2400111, ai_param_id=263381)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterBackreadEnabled(2400111))
    
    DisableAI(2400111)
    AND_1.Add(FlagEnabled(12405681))
    AND_2.Add(AttackedWithDamageType(attacked_entity=2400111, attacker=PLAYER))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_1)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=2400111, radius=5.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableAI(2400111)
    EndIfLastConditionResultFalse(input_condition=AND_1)
    SetAIParamID(2400111, ai_param_id=263380)
    OR_2.Add(CharacterInsideRegion(2400111, region=2402046))
    OR_2.Add(AttackedWithDamageType(attacked_entity=2400111, attacker=PLAYER))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=2400111, radius=5.0))
    
    MAIN.Await(OR_2)
    
    SetAIParamID(2400111, ai_param_id=263381)
    ReplanAI(2400111)


@ContinueOnRest(12405150)
def Event_12405150(_, character: int, flag: int):
    """Event 12405150"""
    WaitFrames(frames=10)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    if FlagEnabled(1210):
        return
    EnableBackread(2400756)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableBackread(2400756)
    EnableInvincibility(character)
    
    MAIN.Await(CharacterBackreadEnabled(2400756))
    
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionTrue(Label.L1, input_condition=AND_15)
    WaitFrames(frames=60)
    DisableBackread(character)
    End()

    # --- Label 1 --- #
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


@ContinueOnRest(12405157)
def Event_12405157():
    """Event 12405157"""
    OR_1.Add(CharacterHasSpecialEffect(2400755, 153))
    OR_1.Add(CharacterHasSpecialEffect(2400759, 153))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=0)


@ContinueOnRest(12405158)
def Event_12405158():
    """Event 12405158"""
    MAIN.Await(EventValue(flag=72400372, bit_count=2) != 0)
    
    WaitFrames(frames=0)


@ContinueOnRest(12405159)
def Event_12405159():
    """Event 12405159"""
    MAIN.Await(CharacterHasSpecialEffect(2400760, 151))
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(2400760, 151))
    
    AND_2.Add(CharacterBackreadDisabled(2400760))
    if AND_2:
        return RESTART
    EnableFlag(12405160)


@RestartOnRest(12405195)
def Event_12405195():
    """Event 12405195"""
    AND_1.Add(CharacterInsideRegion(2400203, region=2402411))
    AND_2.Add(CharacterInsideRegion(2400203, region=2402412))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_2)
    
    MAIN.Await(CharacterInsideRegion(2400203, region=2402411))
    
    MAIN.Await(CharacterInsideRegion(2400203, region=2402406))
    
    AND_3.Add(FlagEnabled(12400169))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    ChangePatrolBehavior(2400203, patrol_information_id=2403111)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(2400203, patrol_information_id=2403112)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterInsideRegion(2400203, region=2402412))
    
    MAIN.Await(CharacterInsideRegion(2400203, region=2402407))
    
    AND_4.Add(FlagEnabled(12400169))
    GotoIfConditionTrue(Label.L2, input_condition=AND_4)
    ChangePatrolBehavior(2400203, patrol_information_id=2403110)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    ChangePatrolBehavior(2400203, patrol_information_id=2403113)

    # --- Label 3 --- #
    DefineLabel(3)
    Restart()


@RestartOnRest(12405200)
def Event_12405200():
    """Event 12405200"""
    MAIN.Await(FlagDisabled(12400168))
    
    WaitFrames(frames=1)
    ActivateObjectWithSpecificCharacter(obj=2401015, objact_id=2400000, relative_index=-1, character=2400113)
    Restart()


@RestartOnRest(12405210)
def Event_12405210(_, character: int, special_effect: int):
    """Event 12405210"""
    AND_1.Add(FlagDisabled(12404002))
    if AND_1:
        return
    SetDisplayMask(character, bit_index=3, switch_type=OnOffChange.On)
    SetDisplayMask(character, bit_index=4, switch_type=OnOffChange.Off)
    AddSpecialEffect(character, special_effect)


@RestartOnRest(12405220)
def Event_12405220(_, character: int, special_effect: int, special_effect_1: int, special_effect_2: int):
    """Event 12405220"""
    AND_1.Add(FlagDisabled(12404002))
    if AND_1:
        return
    AddSpecialEffect(character, special_effect)
    AddSpecialEffect(character, special_effect_1)
    AddSpecialEffect(character, special_effect_2)


@RestartOnRest(12405240)
def Event_12405240():
    """Event 12405240"""
    AND_1.Add(CharacterInsideRegion(2400203, region=2404311))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2404311))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    AND_5.Add(OR_1)
    AND_3.Add(CharacterNotTargeting(targeting_character=2400203, targeted_character=PLAYER))
    AND_4.Add(CharacterTargeting(targeting_character=2400203, targeted_character=PLAYER))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    AND_5.Add(OR_2)
    AND_5.Add(FlagDisabled(9801))
    
    MAIN.Await(AND_5)
    
    PlaySoundEffect(2404290, 20011002, sound_type=SoundType.a_Ambient)
    WaitFrames(frames=40)
    EndIfLastConditionResultTrue(input_condition=AND_4)
    ForceAnimation(2400203, 3039)


@RestartOnRest(12405241)
def Event_12405241():
    """Event 12405241"""
    AND_1.Add(FlagEnabled(12404003))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisableBackread(2400650)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(2400650)


@RestartOnRest(12405250)
def Event_12405250(_, flag: int, navmesh_id: int, flag_1: int):
    """Event 12405250"""
    AND_1.Add(FlagDisabled(flag))
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    RemoveNavmeshFaceFlag(navmesh_id=navmesh_id, navmesh_type=NavmeshFlag.Disable)
    SkipLines(1)
    AddNavmeshFaceFlag(navmesh_id=navmesh_id, navmesh_type=NavmeshFlag.Disable)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Restart()


@RestartOnRest(12405251)
def Event_12405251(_, flag: int, navmesh_id: int, flag_1: int):
    """Event 12405251"""
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(FlagDisabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    RemoveNavmeshFaceFlag(navmesh_id=navmesh_id, navmesh_type=NavmeshFlag.Disable)
    SkipLines(1)
    AddNavmeshFaceFlag(navmesh_id=navmesh_id, navmesh_type=NavmeshFlag.Disable)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    Restart()


@RestartOnRest(12405259)
def Event_12405259():
    """Event 12405259"""
    DisableNetworkSync()
    AND_1.Add(CharacterHasTAEEvent(2400899, tae_event_id=700))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 5577))
    
    MAIN.Await(AND_1)
    
    DisplayBanner(BannerType.YouLose)
    Restart()


@RestartOnRest(12405260)
def Event_12405260():
    """Event 12405260"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402018))
    
    MAIN.Await(AND_1)
    
    CreatePlayLog(name=2)
    ForceAnimation(2400899, 3000)
    WaitFrames(frames=250)
    Restart()


@RestartOnRest(12405261)
def Event_12405261():
    """Event 12405261"""
    MAIN.Await(Attacked(attacked_entity=PLAYER, attacker=2402018))
    
    Wait(3.0)
    ForceAnimation(PLAYER, 9580, wait_for_completion=True)
    Restart()


@RestartOnRest(12405262)
def Event_12405262():
    """Event 12405262"""
    AND_1.Add(FlagEnabled(12405263))
    AND_1.Add(CharacterHasTAEEvent(2400899, tae_event_id=10))
    
    MAIN.Await(AND_1)
    
    SetDisplayMask(2400899, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2400899, bit_index=10, switch_type=OnOffChange.Off)
    AddSpecialEffect(2400899, 5687)
    RemoveSpecialEffect(2400899, 5686)
    
    MAIN.Await(CharacterHasTAEEvent(2400899, tae_event_id=20))
    
    AddSpecialEffect(2400899, 5686)
    RemoveSpecialEffect(2400899, 5687)
    Restart()


@RestartOnRest(12405263)
def Event_12405263():
    """Event 12405263"""
    AND_1.Add(CharacterHasTAEEvent(2400899, tae_event_id=710))
    AND_1.Add(PlayerHasGood(4311))
    
    MAIN.Await(AND_1)
    
    EnableImmortality(PLAYER)
    WaitFrames(frames=30)
    EnableFlag(9180)
    WaitFrames(frames=1)
    GotoIfMultiplayer(Label.L0)
    PlayCutscene(24000000, cutscene_flags=0, player_id=10000)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    PlayCutscene(24000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableFlag(9180)
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    EnableFlag(12401000)
    WarpPlayerToRespawnPoint(3402959)


@RestartOnRest(12405270)
def Event_12405270():
    """Event 12405270"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2402190))
    
    CreatePlayLog(name=26)


@RestartOnRest(12405271)
def Event_12405271():
    """Event 12405271"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2402191))
    
    CreatePlayLog(name=56)


@RestartOnRest(12405272)
def Event_12405272():
    """Event 12405272"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2402192))
    
    CreatePlayLog(name=90)


@RestartOnRest(12405273)
def Event_12405273():
    """Event 12405273"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2402193))
    
    CreatePlayLog(name=2)


@RestartOnRest(12405289)
def Event_12405289():
    """Event 12405289"""
    SetTeamType(2400000, TeamType.Human)


@RestartOnRest(12405300)
def Event_12405300(_, character: int, region: int, patrol_information_id: int, flag: int):
    """Event 12405300"""
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    DisableFlag(flag)


@RestartOnRest(12405320)
def Event_12405320():
    """Event 12405320"""
    AND_1.Add(FlagEnabled(12405300))
    AND_2.Add(FlagEnabled(12405301))
    AND_3.Add(FlagEnabled(12405302))
    AND_4.Add(FlagEnabled(12405303))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    MAIN.Await(CharacterBackreadDisabled(2400300))
    
    MAIN.Await(CharacterBackreadEnabled(2400300))
    
    AND_5.Add(FlagEnabled(12405300))
    AND_6.Add(FlagEnabled(12405301))
    AND_7.Add(FlagEnabled(12405302))
    AND_8.Add(FlagEnabled(12405303))
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(2.0)
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_5)
    ChangePatrolBehavior(2400300, patrol_information_id=2403101)
    Restart()
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_6)
    ChangePatrolBehavior(2400300, patrol_information_id=2403102)
    Restart()
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_7)
    ChangePatrolBehavior(2400300, patrol_information_id=2403103)
    Restart()
    SkipLinesIfLastConditionResultFalse(2, input_condition=AND_8)
    ChangePatrolBehavior(2400300, patrol_information_id=2403104)
    Restart()


@RestartOnRest(12405330)
def Event_12405330(_, character: int):
    """Event 12405330"""
    ForceAnimation(character, 7000, loop=True)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=4.0))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, 7001)
    ReplanAI(character)


@RestartOnRest(12405335)
def Event_12405335():
    """Event 12405335"""
    MAIN.Await(CharacterBackreadEnabled(2400421))
    
    DisableAI(2400421)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402031))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=2400421, radius=5.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_2)
    ForceAnimation(2400421, 3011)
    EnableAI(2400421)


@RestartOnRest(12405350)
def Event_12405350(_, character: int, region: int, region_1: int, patrol_information_id: int, region_2: int):
    """Event 12405350"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region_2))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(character, region=region_1)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    if ThisEventSlotFlagEnabled():
        return
    ReplanAI(character)


@RestartOnRest(12405360)
def Event_12405360():
    """Event 12405360"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterBackreadEnabled(2400371))
    
    AddSpecialEffect(2400371, 5000)
    
    MAIN.Await(HasAIStatus(2400371, ai_status=AIStatusType.Battle))

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(2400371, region=2404085)
    ChangePatrolBehavior(2400371, patrol_information_id=2403106)
    
    MAIN.Await(CharacterInsideRegion(2400371, region=2404085))
    
    RemoveSpecialEffect(2400371, 5000)
    AICommand(2400371, command_id=-1, command_slot=0)
    ReplanAI(2400371)


@RestartOnRest(12405365)
def Event_12405365(_, character: int, region: int, patrol_information_id: int):
    """Event 12405365"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    AddSpecialEffect(character, 5000)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(character, region=region)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    RemoveSpecialEffect(character, 5000)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405370)
def Event_12405370(_, character: int):
    """Event 12405370"""
    MAIN.Await(FlagEnabled(9802))
    
    DisableBackread(character)


@ContinueOnRest(12405380)
def Event_12405380(_, character: int, region: int, region_1: int):
    """Event 12405380"""
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    SetNest(character, region=region)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    SetNest(character, region=region_1)
    Restart()


@ContinueOnRest(12400865)
def Event_12400865(_, character: int):
    """Event 12400865"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    DisableCharacter(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    Wait(0.0)


@RestartOnRest(12405400)
def Event_12405400(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    animation_id: int,
    special_effect: int,
    flag: int,
    flag_1: int,
    character: int,
):
    """Event 12405400"""
    MAIN.Await(FlagEnabled(flag))
    
    AND_1.Add(CharacterPartHealth(character, npc_part_id=npc_part_id_1) <= 0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(HealthRatio(character) <= 0.0)
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    if FlagDisabled(flag):
        SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=1, overwrite_max=False)
        Restart()
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=9999999)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=65, material_vfx_id=65)
    ResetAnimation(character)
    ForceAnimation(character, animation_id)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=400))
    
    AddSpecialEffect(character, special_effect)
    DisableFlag(flag_1)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=300))
    
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=80, overwrite_max=True)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    RemoveSpecialEffect(character, special_effect)
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
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
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
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=tae_event_id))
    
    EnableFlag(flag)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=tae_event_id_1))
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(12405790)
def Event_12405790(_, obj: int, flag: int, dummy_id: int):
    """Event 12405790"""
    DeleteObjectVFX(obj)
    if FlagEnabled(flag):
        return
    CreateObjectVFX(obj, vfx_id=200, dummy_id=dummy_id)


@RestartOnRest(12405800)
def Event_12405800(_, sound_id: int, flag: int, flag_1: int, flag_2: int):
    """Event 12405800"""
    DisableSoundEvent(sound_id=sound_id)
    if FlagEnabled(flag_2):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=sound_id)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(OR_1)
    
    DisableSoundEvent(sound_id=sound_id)
    Restart()


@RestartOnRest(12405810)
def Event_12405810(_, character: int, region: int, region_1: int, command_id: int, flag: int):
    """Event 12405810"""
    if FlagEnabled(flag):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(character, region=region_1)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405820)
def Event_12405820(_, character: int, region: int):
    """Event 12405820"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterInsideRegion(character, region=region))

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405840)
def Event_12405840(_, character: int, command_id: int, flag: int):
    """Event 12405840"""
    if FlagEnabled(flag):
        return
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    AND_2.Add(FlagEnabled(flag))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    AND_3.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    AND_4.Add(FlagEnabled(flag))
    OR_3.Add(AND_3)
    OR_3.Add(AND_4)
    
    MAIN.Await(OR_3)
    
    EndIfLastConditionResultTrue(input_condition=AND_4)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12405850)
def Event_12405850(_, character: int, obj: int, region: int, command_id: int, flag: int):
    """Event 12405850"""
    if FlagEnabled(flag):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, 7013, loop=True)
    OR_1.Add(ObjectDestroyed(obj))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=4.0))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=0)
    ForceAnimation(character, 7012)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(character, region=region)
    ForceAnimation(character, 7011)
    ForceAnimation(character, 7012)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)


@ContinueOnRest(12400860)
def Event_12400860():
    """Event 12400860"""
    GotoIfFlagDisabled(Label.L0, flag=12400861)
    DisableCharacter(2400450)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(2400450))
    
    if FlagDisabled(6333):
        AwardItemLot(75002400, host_only=False)
    else:
        AwardItemLot(75002405, host_only=False)
    EnableFlag(12400861)


@RestartOnRest(12405600)
def Event_12405600(_, character: int, region: int, radius: float, seconds: float):
    """Event 12405600"""
    DisableAI(character)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(OR_2)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(OR_2)
    AND_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(2, input_condition=AND_2)
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_3)
    Wait(seconds)
    EnableAI(character)
    WaitFrames(frames=1)
    ReplanAI(character)


@RestartOnRest(12405660)
def Event_12405660():
    """Event 12405660"""
    DisableAI(2400114)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    OR_3.Add(CharacterInsideRegion(PLAYER, region=2402082))
    OR_3.Add(EntityWithinDistance(entity=2400114, other_entity=PLAYER, radius=5.0))
    AND_1.Add(OR_2)
    AND_1.Add(OR_3)
    OR_1.Add(CharacterInsideRegion(2400122, region=2404151))
    OR_1.Add(Attacked(attacked_entity=2400114, attacker=PLAYER))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableAI(2400114)
    ReplanAI(2400114)


@RestartOnRest(12405670)
def Event_12405670(_, character: int, region: int, region_1: int, radius: float, seconds: float):
    """Event 12405670"""
    DisableAI(character)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(OR_2)
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    AND_2.Add(OR_2)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_3.Add(OR_2)
    AND_4.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    Wait(seconds)
    EnableAI(character)
    WaitFrames(frames=1)
    ReplanAI(character)


@RestartOnRest(12405675)
def Event_12405675(_, character: int):
    """Event 12405675"""
    DisableAI(character)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2404332))
    OR_1.Add(AND_1)
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=3.0))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    WaitFrames(frames=1)
    ReplanAI(character)


@RestartOnRest(12405680)
def Event_12405680():
    """Event 12405680"""
    MAIN.Await(CharacterTargeting(targeting_character=2400106, targeted_character=PLAYER))
    
    WaitFrames(frames=1)
    ForceAnimation(2400106, 3010, wait_for_completion=True)
    WaitFrames(frames=75)
    
    MAIN.Await(HealthRatio(2400106) == 1.0)
    
    EnableFlag(12405681)
    ForceAnimation(2400106, 3009, wait_for_completion=True)


@RestartOnRest(12405682)
def Event_12405682(_, character: int, region: int, seconds: float, flag: int, seconds_1: float):
    """Event 12405682"""
    DisableAI(character)
    DisableAnimations(region)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_3)
    AND_2.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=10.0))
    AND_3.Add(FlagEnabled(12405681))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    SkipLinesIfFlagDisabled(24, 12405681)
    Wait(seconds)
    SetEventPoint(character, region=region, reaction_range=1.0)
    AICommand(character, command_id=90, command_slot=0)
    ReplanAI(character)
    AND_4.Add(EntityWithinDistance(entity=character, other_entity=region, radius=4.0))
    OR_4.Add(CharacterHuman(PLAYER))
    OR_4.Add(CharacterWhitePhantom(PLAYER))
    AND_5.Add(OR_4)
    AND_5.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=3.0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfLastConditionResultTrue(9, input_condition=AND_2)
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
    if FlagDisabled(flag):
        WaitRandomSeconds(min_seconds=1.0, max_seconds=2.0)
    Wait(seconds_1)
    RemoveSpecialEffect(character, 4662)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405686)
def Event_12405686(_, character: int):
    """Event 12405686"""
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=2.0))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)


@RestartOnRest(12405690)
def Event_12405690():
    """Event 12405690"""
    MAIN.Await(CharacterInsideRegion(2400106, region=2404111))
    
    AddSpecialEffect(2400106, 5002)
    
    MAIN.Await(CharacterInsideRegion(2400106, region=2404113))
    
    WaitFrames(frames=30)
    RemoveSpecialEffect(2400106, 5002)
    Restart()


@ContinueOnRest(12400500)
def Event_12400500():
    """Event 12400500"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L6, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L1, flag=1193)
    DisableFlagRange((1180, 1199))
    EnableFlag(1181)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(1181))
    AND_1.Add(FlagEnabled(9801))
    GotoIfConditionFalse(Label.L2, input_condition=AND_1)
    DisableFlagRange((1180, 1199))
    EnableFlag(1185)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(FlagEnabled(9467))
    AND_2.Add(FlagEnabled(1185))
    GotoIfConditionFalse(Label.L3, input_condition=AND_2)
    DisableFlagRange((1180, 1199))
    EnableFlag(1186)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_5.Add(FlagEnabled(1186))
    AND_5.Add(FlagEnabled(72400900))
    GotoIfConditionFalse(Label.L9, input_condition=AND_5)
    DisableFlagRange((1180, 1199))
    EnableFlag(1187)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_3.Add(FlagEnabled(1187))
    AND_3.Add(FlagEnabled(72400919))
    GotoIfConditionFalse(Label.L4, input_condition=AND_3)
    if FlagDisabled(72400918):
        EnableFlag(72400918)
        Goto(Label.L4)
    DisableFlagRange((1180, 1199))
    EnableFlag(1188)

    # --- Label 4 --- #
    DefineLabel(4)
    AND_4.Add(FlagEnabled(1188))
    AND_4.Add(FlagEnabled(72400350))
    GotoIfConditionFalse(Label.L5, input_condition=AND_4)
    DisableFlagRange((1180, 1199))
    EnableFlag(1189)

    # --- Label 5 --- #
    DefineLabel(5)
    DisableFlag(72400348)
    DisableFlag(72400356)

    # --- Label 6 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    ForceAnimation(2400730, 103060, loop=True, skip_transition=True)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    ForceAnimation(2400730, 103066, loop=True, skip_transition=True)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    EzstateAIRequest(2400730, command_id=3, command_slot=1)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400730)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableBackread(2400730)
    EnableBackread(2400732)
    EnableObject(2400731)
    PostDestruction(2400731)
    EzstateAIRequest(2400732, command_id=10, command_slot=1)
    Move(2400732, destination=2404382, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400732)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    RestoreObject(2400731)
    EzstateAIRequest(2400730, command_id=3, command_slot=1)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400730)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    PostDestruction(2400731)
    End()


@ContinueOnRest(12400501)
def Event_12400501():
    """Event 12400501"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1183):
        return
    if FlagEnabled(1189):
        return
    if FlagEnabled(1191):
        return
    AND_1.Add(CharacterDead(2400730))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1180, 1199))
    EnableFlag(1183)
    SaveRequest()


@ContinueOnRest(12400505)
def Event_12400505():
    """Event 12400505"""
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=1191)
    DisableMapPiece(map_piece_id=2404602)
    
    MAIN.Await(FlagEnabled(6001))
    
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2404602)
    End()


@ContinueOnRest(12400507)
def Event_12400507():
    """Event 12400507"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=2400730))
    AND_1.Add(HealthRatio(2400730) != 0.0)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=1185)
    ForceAnimation(2400730, 103063)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2400730, 103067)
    Restart()


@ContinueOnRest(12400508)
def Event_12400508():
    """Event 12400508"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(2400730) == 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2400730, 103064)


@ContinueOnRest(12400512)
def Event_12400512():
    """Event 12400512"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    OR_1.Add(CharacterHasSpecialEffect(2400730, 151))
    OR_1.Add(CharacterHasSpecialEffect(2400730, 153))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(2400730) != 0.0)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=1185)
    GotoIfFlagEnabled(Label.L1, flag=9432)
    ForceAnimation(2400730, 103060)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(2400730, 103061)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2400730, 103066)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=5)
    Restart()


@ContinueOnRest(12400513)
def Event_12400513():
    """Event 12400513"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(9432))
    OR_1.Add(FlagEnabled(1181))
    OR_1.Add(FlagEnabled(1184))
    OR_1.Add(FlagEnabled(1186))
    OR_1.Add(FlagEnabled(1187))
    OR_1.Add(FlagEnabled(1188))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2400730, 103061)
    
    MAIN.Await(FlagDisabled(9432))
    
    ForceAnimation(2400730, 103060)
    Restart()


@ContinueOnRest(12400514)
def Event_12400514():
    """Event 12400514"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagEnabled(Label.L0, flag=1187)
    GotoIfFlagEnabled(Label.L1, flag=1189)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2400020, entity=2400731))
    
    DisplayDialog(text=14001000, anchor_entity=2400731, number_buttons=NumberButtons.OneButton)
    EnableFlag(72400919)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2400020, entity=2400731))
    
    DisplayDialog(text=14001001, anchor_entity=2400731, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12400520)
def Event_12400520():
    """Event 12400520"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L7, input_condition=AND_15)
    AND_1.Add(FlagEnabled(1232))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableFlagRange((1220, 1239))
    EnableFlag(1224)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagEnabled(1233))
    GotoIfConditionFalse(Label.L1, input_condition=AND_2)
    DisableFlagRange((1220, 1239))
    EnableFlag(1223)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(FlagEnabled(9802))
    AND_3.Add(FlagEnabled(1224))
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    DisableFlagRange((1220, 1239))
    EnableFlag(1225)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_4.Add(FlagEnabled(1225))
    AND_4.Add(FlagEnabled(9464))
    GotoIfConditionFalse(Label.L3, input_condition=AND_4)
    DisableFlagRange((1220, 1239))
    EnableFlag(1226)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_5.Add(FlagEnabled(1226))
    AND_5.Add(FlagEnabled(9461))
    GotoIfConditionFalse(Label.L5, input_condition=AND_5)
    DisableFlagRange((1220, 1239))
    EnableFlag(1228)

    # --- Label 5 --- #
    DefineLabel(5)
    AND_7.Add(FlagEnabled(1220))
    AND_7.Add(FlagEnabled(9802))
    GotoIfConditionFalse(Label.L6, input_condition=AND_7)
    DisableFlagRange((1220, 1239))
    EnableFlag(1234)

    # --- Label 6 --- #
    DefineLabel(6)

    # --- Label 7 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    EnableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400750, 103080)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    EnableBackread(2400754)
    DisableBackread(2400757)
    ForceAnimation(2400754, 103081)
    Move(2400754, destination=2404504, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    EnableBackread(2400757)
    ForceAnimation(2400757, 103081)
    Move(2400757, destination=2404504, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    EnableObject(2400748)
    EnableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    End()

    # --- Label 5 --- #
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

    # --- Label 6 --- #
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


@ContinueOnRest(12400521)
def Event_12400521():
    """Event 12400521"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1222):
        return
    if FlagEnabled(1230):
        return
    if FlagEnabled(1231):
        return
    OR_1.Add(CharacterDead(2400750))
    OR_1.Add(CharacterDead(2400754))
    OR_1.Add(CharacterDead(2400757))
    OR_1.Add(CharacterDead(2400758))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1220, 1239))
    EnableFlag(1222)
    SaveRequest()


@ContinueOnRest(12400522)
def Event_12400522():
    """Event 12400522"""
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=1230)
    GotoIfFlagEnabled(Label.L0, flag=1231)
    DisableMapPiece(map_piece_id=2404600)
    
    MAIN.Await(FlagEnabled(6001))
    
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2404600)
    End()


@ContinueOnRest(12400523)
def Event_12400523():
    """Event 12400523"""
    MAIN.Await(FlagEnabled(72400510))
    
    DisableFlag(72400510)
    DisableFlagRange((1220, 1239))
    EnableFlag(1232)


@ContinueOnRest(12400524)
def Event_12400524():
    """Event 12400524"""
    MAIN.Await(FlagEnabled(72400511))
    
    DisableFlag(72400511)
    DisableFlagRange((1220, 1239))
    EnableFlag(1233)


@ContinueOnRest(12400525)
def Event_12400525():
    """Event 12400525"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(72400499))
    
    DisableFlag(72400499)
    GotoIfFlagDisabled(Label.L0, flag=72400950)
    GotoIfFlagDisabled(Label.L1, flag=72400951)
    GotoIfFlagDisabled(Label.L2, flag=72400952)
    GotoIfFlagDisabled(Label.L3, flag=72400953)
    GotoIfFlagDisabled(Label.L4, flag=72400954)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableFlag(72400954)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableFlag(72400953)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(72400952)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(72400951)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(72400950)
    OR_1.Add(FlagEnabled(1304))
    OR_1.Add(FlagEnabled(1305))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagDisabled(Label.L5, flag=72400940)
    GotoIfFlagDisabled(Label.L6, flag=72400941)
    GotoIfFlagDisabled(Label.L7, flag=72400942)
    GotoIfFlagDisabled(Label.L8, flag=72400943)
    GotoIfFlagDisabled(Label.L9, flag=72400944)

    # --- Label 9 --- #
    DefineLabel(9)
    EnableFlag(72400944)

    # --- Label 8 --- #
    DefineLabel(8)
    EnableFlag(72400943)

    # --- Label 7 --- #
    DefineLabel(7)
    EnableFlag(72400942)

    # --- Label 6 --- #
    DefineLabel(6)
    EnableFlag(72400941)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableFlag(72400940)


@ContinueOnRest(12400531)
def Event_12400531():
    """Event 12400531"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(PlayerHasGood(701))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisableFlag(72400498)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@ContinueOnRest(12400560)
def Event_12400560():
    """Event 12400560"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L3, input_condition=AND_15)
    AND_1.Add(FlagEnabled(1168))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableFlagRange((1160, 1179))
    EnableFlag(1164)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagEnabled(1169))
    GotoIfConditionFalse(Label.L1, input_condition=AND_2)
    DisableFlagRange((1160, 1179))
    EnableFlag(1163)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(FlagEnabled(9802))
    AND_3.Add(FlagEnabled(1164))
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    DisableFlagRange((1160, 1179))
    EnableFlag(1165)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_4.Add(FlagEnabled(1160))
    AND_4.Add(FlagEnabled(9802))
    GotoIfConditionFalse(Label.L3, input_condition=AND_4)
    DisableFlagRange((1160, 1179))
    EnableFlag(1170)

    # --- Label 3 --- #
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

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(2400765)
    ForceAnimation(2400765, 103050)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(2400765)
    EzstateAIRequest(2400765, command_id=2, command_slot=1)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400765)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    EnableBackread(2400765)
    EzstateAIRequest(2400765, command_id=2, command_slot=1)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400765)
    End()


@ContinueOnRest(12400561)
def Event_12400561():
    """Event 12400561"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1161):
        return
    if FlagEnabled(1166):
        return
    AND_1.Add(CharacterDead(2400765))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1160, 1179))
    EnableFlag(1161)
    SaveRequest()


@ContinueOnRest(12400563)
def Event_12400563():
    """Event 12400563"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagEnabled(Label.L0, flag=72400330)
    OR_1.Add(FlagEnabled(1304))
    OR_1.Add(FlagEnabled(1305))
    OR_1.Add(FlagEnabled(1306))
    OR_1.Add(FlagEnabled(1307))
    OR_1.Add(FlagEnabled(1308))
    OR_2.Add(FlagEnabled(1224))
    OR_2.Add(FlagEnabled(1225))
    OR_2.Add(FlagEnabled(1226))
    OR_2.Add(FlagEnabled(1227))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableFlag(72400330)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_3.Add(FlagEnabled(1312))
    OR_3.Add(FlagEnabled(1303))
    OR_3.Add(FlagEnabled(1317))
    OR_4.Add(FlagEnabled(1228))
    OR_4.Add(FlagEnabled(1229))
    OR_4.Add(FlagEnabled(1235))
    OR_4.Add(FlagEnabled(1236))
    OR_4.Add(FlagEnabled(1230))
    OR_4.Add(FlagEnabled(1231))
    OR_4.Add(FlagEnabled(1222))
    OR_5.Add(OR_3)
    OR_5.Add(OR_4)
    
    MAIN.Await(OR_5)
    
    DisableFlag(72400330)


@ContinueOnRest(12400564)
def Event_12400564():
    """Event 12400564"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagEnabled(Label.L0, flag=72400331)
    AND_1.Add(FlagEnabled(1188))
    AND_1.Add(FlagEnabled(1164))
    
    MAIN.Await(AND_1)
    
    EnableFlag(72400331)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(1189))
    OR_1.Add(FlagEnabled(1191))
    OR_1.Add(FlagEnabled(1183))
    
    MAIN.Await(OR_1)
    
    DisableFlag(72400331)


@ContinueOnRest(12400565)
def Event_12400565():
    """Event 12400565"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagEnabled(Label.L0, flag=72400332)
    OR_1.Add(FlagEnabled(1100))
    OR_1.Add(FlagEnabled(1101))
    OR_1.Add(FlagEnabled(1102))
    OR_1.Add(FlagEnabled(1103))
    OR_1.Add(FlagEnabled(1104))
    OR_1.Add(FlagEnabled(1105))
    
    MAIN.Await(OR_1)
    
    EnableFlag(72400332)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(FlagEnabled(1108))
    OR_2.Add(FlagEnabled(1106))
    
    MAIN.Await(OR_2)
    
    DisableFlag(72400332)


@ContinueOnRest(12400566)
def Event_12400566():
    """Event 12400566"""
    MAIN.Await(FlagEnabled(72400970))
    
    DisableFlag(72400970)
    DisableFlagRange((1160, 1179))
    EnableFlag(1168)
    Restart()


@ContinueOnRest(12400567)
def Event_12400567():
    """Event 12400567"""
    MAIN.Await(FlagEnabled(72400971))
    
    DisableFlag(72400971)
    DisableFlagRange((1160, 1179))
    EnableFlag(1169)
    Restart()


@ContinueOnRest(12400568)
def Event_12400568():
    """Event 12400568"""
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=1166)
    DisableMapPiece(map_piece_id=2404603)
    
    MAIN.Await(FlagEnabled(6001))
    
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2404603)
    End()


@ContinueOnRest(12400569)
def Event_12400569():
    """Event 12400569"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1161):
        return
    if FlagEnabled(1166):
        return
    AND_1.Add(HealthRatio(2400765) == 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2400765, 103053)


@ContinueOnRest(12400570)
def Event_12400570():
    """Event 12400570"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=2400765))
    AND_1.Add(HealthRatio(2400765) != 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2400765, 103052)
    Restart()


@ContinueOnRest(12400571)
def Event_12400571():
    """Event 12400571"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(2400765, 151))
    AND_1.Add(HealthRatio(2400765) != 0.0)
    
    MAIN.Await(AND_1)
    
    AND_2.Add(FlagEnabled(9432))
    AND_2.Add(FlagDisabled(1165))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    ForceAnimation(2400765, 103050)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2400765, 103051)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=5)
    Restart()


@ContinueOnRest(12400572)
def Event_12400572():
    """Event 12400572"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(9432))
    AND_1.Add(FlagDisabled(1165))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2400765, 103051)
    
    MAIN.Await(FlagDisabled(9432))
    
    ForceAnimation(2400765, 103050)
    Restart()


@ContinueOnRest(12400580)
def Event_12400580():
    """Event 12400580"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402280))
    AND_2.Add(FlagEnabled(72400400))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    EnableSoundEvent(sound_id=2403300)


@ContinueOnRest(12400581)
def Event_12400581():
    """Event 12400581"""
    MAIN.Await(FlagEnabled(72400400))
    
    DisableSoundEvent(sound_id=2403300)


@ContinueOnRest(12400582)
def Event_12400582():
    """Event 12400582"""
    EnableMapPiece(map_piece_id=2404010)
    
    MAIN.Await(FlagEnabled(12401802))
    
    DisableMapPiece(map_piece_id=2404010)


@ContinueOnRest(12400590)
def Event_12400590():
    """Event 12400590"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    AND_1.Add(FlagEnabled(1340))
    AND_1.Add(FlagEnabled(9801))
    GotoIfConditionFalse(Label.L1, input_condition=AND_1)
    DisableFlagRange((1340, 1359))
    EnableFlag(1344)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(1351))
    AND_2.Add(FlagEnabled(72500359))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    DisableFlagRange((1340, 1359))
    EnableFlag(1343)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlag(72400471)

    # --- Label 0 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    GotoIfFlagEnabled(Label.L7, flag=12405160)
    ForceAnimation(2400760, 103020, loop=True, skip_transition=True)
    End()

    # --- Label 7 --- #
    DefineLabel(7)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    SetTeamType(2400760, TeamType.HostileNPC)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    DisableCharacter(2400760)
    DropMandatoryTreasure(2400760)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(2400760)
    EnableBackread(2400762)
    DisableBackread(2400763)
    EnableObject(2400761)
    Move(2400762, destination=2404508, destination_type=CoordEntityType.Region, short_move=True)
    EzstateAIRequest(2400762, command_id=11, command_slot=1)
    DropMandatoryTreasure(2400762)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableBackread(2400760)
    DisableBackread(2400762)
    EnableBackread(2400763)
    DisableObject(2400761)
    SetTeamType(2400763, TeamType.FriendlyNPC)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    DisableBackread(2400760)
    DisableBackread(2400762)
    EnableBackread(2400763)
    DisableObject(2400761)
    SetTeamType(2400763, TeamType.HostileNPC)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableBackread(2400760)
    DisableBackread(2400762)
    DisableBackread(2400763)
    DisableObject(2400761)
    DisableCharacter(2400763)
    DropMandatoryTreasure(2400763)
    End()


@ContinueOnRest(12400591)
def Event_12400591():
    """Event 12400591"""
    MAIN.Await(FlagEnabled(72400465))
    
    DisableFlag(72400465)
    DisableFlagRange((1340, 1359))
    EnableFlag(1347)
    SaveRequest()


@ContinueOnRest(12400592)
def Event_12400592(_, attacked_entity: int, flag: int):
    """Event 12400592"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    DisableFlag(flag)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    EnableFlag(flag)


@ContinueOnRest(12400593)
def Event_12400593(_, character: int, flag: int, flag_1: int):
    """Event 12400593"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableFlagRange((1340, 1359))
    EnableFlag(flag)
    SaveRequest()


@ContinueOnRest(12400594)
def Event_12400594(_, character: int, flag: int):
    """Event 12400594"""
    if ThisEventSlotFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(CharacterDead(character))
    
    DisableFlagRange((1340, 1359))
    EnableFlag(flag)
    SaveRequest()


@ContinueOnRest(12400610)
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

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(EventValue(flag=72400372, bit_count=2) != 0)
    OR_1.Add(FlagEnabled(12405158))
    GotoIfConditionTrue(Label.L2, input_condition=OR_1)
    DisableBackread(2400755)
    EnableBackread(2400759)
    DisableBackread(2400220)
    GotoIfFlagEnabled(Label.L5, flag=12405157)
    ForceAnimation(2400759, 103074)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    ForceAnimation(2400759, 103072)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(2400755)
    DisableBackread(2400759)
    DisableBackread(2400220)
    GotoIfFlagEnabled(Label.L4, flag=12405157)
    ForceAnimation(2400755, 103074)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    ForceAnimation(2400755, 103072)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(2400755)
    DisableBackread(2400759)
    DisableBackread(2400220)
    ForceAnimation(2400755, 103072)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(2400755)
    DisableCharacter(2400755)
    DisableBackread(2400759)
    DisableCharacter(2400759)
    DisableBackread(2400220)
    DisableCharacter(2400220)
    DropMandatoryTreasure(2400755)
    End()


@ContinueOnRest(12400611)
def Event_12400611():
    """Event 12400611"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1210):
        return
    OR_1.Add(CharacterDead(2400755))
    OR_1.Add(CharacterDead(2400756))
    OR_1.Add(CharacterDead(2400759))
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((1200, 1219))
    EnableFlag(1210)
    AND_1.Add(CharacterDead(2400756))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableFlag(9432)

    # --- Label 0 --- #
    DefineLabel(0)
    SaveRequest()


@ContinueOnRest(12400612)
def Event_12400612(_, character: int, flag: int):
    """Event 12400612"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(character) < 0.5)
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@ContinueOnRest(12400614)
def Event_12400614(_, character: int, animation_id: int):
    """Event 12400614"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(character) == 0.0)
    AND_1.Add(CharacterHasSpecialEffect(character, 155))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id)


@ContinueOnRest(12400616)
def Event_12400616(_, character: int):
    """Event 12400616"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(HealthRatio(character) != 0.0)
    AND_1.Add(HealthRatio(character) > 0.5)
    
    MAIN.Await(AND_1)
    
    OR_2.Add(CharacterHasSpecialEffect(character, 153))
    GotoIfConditionTrue(Label.L0, input_condition=OR_2)
    OR_3.Add(CharacterHasSpecialEffect(character, 155))
    GotoIfConditionTrue(Label.L1, input_condition=OR_3)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 103079)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 103130)
    Restart()


@ContinueOnRest(12400618)
def Event_12400618(_, character: int):
    """Event 12400618"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 154))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 103072)
    Restart()


@ContinueOnRest(12400620)
def Event_12400620(_, character: int):
    """Event 12400620"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 156))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 103072)


@ContinueOnRest(12400622)
def Event_12400622():
    """Event 12400622"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(1208))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlagRange((1200, 1219))
    EnableFlag(1205)


@ContinueOnRest(12400623)
def Event_12400623():
    """Event 12400623"""
    if Client():
        return
    AND_1.Add(FlagEnabled(1209))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlagRange((1200, 1219))
    EnableFlag(1204)


@ContinueOnRest(12400624)
def Event_12400624():
    """Event 12400624"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagDisabled(1205):
        return
    OR_1.Add(FlagEnabled(1106))
    OR_1.Add(FlagEnabled(1108))
    OR_2.Add(FlagEnabled(1222))
    OR_2.Add(FlagEnabled(1223))
    OR_2.Add(FlagEnabled(1230))
    OR_2.Add(FlagEnabled(1231))
    OR_2.Add(FlagEnabled(1235))
    OR_2.Add(FlagEnabled(1228))
    OR_2.Add(FlagEnabled(1229))
    OR_2.Add(FlagEnabled(1234))
    OR_3.Add(FlagEnabled(1303))
    OR_3.Add(FlagEnabled(1308))
    OR_3.Add(FlagEnabled(1309))
    OR_3.Add(FlagEnabled(1315))
    OR_3.Add(FlagEnabled(1310))
    OR_3.Add(FlagEnabled(1312))
    OR_3.Add(FlagEnabled(1316))
    OR_4.Add(FlagEnabled(1163))
    OR_4.Add(FlagEnabled(1161))
    OR_4.Add(FlagEnabled(1166))
    OR_4.Add(FlagEnabled(1170))
    OR_5.Add(FlagEnabled(1183))
    OR_5.Add(FlagEnabled(1190))
    OR_5.Add(FlagEnabled(1189))
    OR_5.Add(FlagEnabled(1191))
    OR_5.Add(FlagEnabled(1195))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    AND_1.Add(OR_3)
    AND_1.Add(OR_4)
    AND_1.Add(OR_5)
    AND_1.Add(FlagDisabled(72400934))
    AND_1.Add(FlagDisabled(72400935))
    AND_1.Add(FlagDisabled(72400936))
    AND_1.Add(FlagDisabled(72400937))
    AND_1.Add(FlagDisabled(72400938))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1200, 1219))
    EnableFlag(1211)


@ContinueOnRest(12400625)
def Event_12400625(_, character: int, flag: int):
    """Event 12400625"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagDisabled(1207):
        return
    WaitFrames(frames=30)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=2404383))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1207))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@ContinueOnRest(12400627)
def Event_12400627(_, character: int, flag: int):
    """Event 12400627"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_2)
    
    WaitFrames(frames=1)
    AND_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_3.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_3)
    
    EnableFlag(flag)


@ContinueOnRest(12400629)
def Event_12400629():
    """Event 12400629"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    OR_1.Add(FlagEnabled(1208))
    OR_1.Add(FlagEnabled(1205))
    OR_1.Add(FlagEnabled(1207))
    GotoIfConditionFalse(Label.L6, input_condition=OR_1)
    GotoIfFlagEnabled(Label.L0, flag=1208)
    GotoIfFlagDisabled(Label.L5, flag=72400360)
    GotoIfFlagRangeAllDisabled(Label.L5, flag_range=(70000200, 70000202))

    # --- Label 0 --- #
    DefineLabel(0)
    OR_2.Add(FlagEnabled(1164))
    OR_2.Add(FlagEnabled(1165))
    GotoIfConditionFalse(Label.L1, input_condition=OR_2)
    DisableFlagRange((1160, 1179))
    EnableFlag(1166)
    EnableFlag(72400934)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_3.Add(FlagEnabled(1181))
    OR_3.Add(FlagEnabled(1184))
    OR_3.Add(FlagEnabled(1185))
    OR_3.Add(FlagEnabled(1186))
    OR_3.Add(FlagEnabled(1187))
    OR_3.Add(FlagEnabled(1188))
    GotoIfConditionFalse(Label.L2, input_condition=OR_3)
    DisableFlagRange((1180, 1199))
    EnableFlag(1191)
    EnableFlag(72400935)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_4.Add(FlagEnabled(1304))
    OR_4.Add(FlagEnabled(1305))
    OR_4.Add(FlagEnabled(1306))
    OR_4.Add(FlagEnabled(1307))
    GotoIfConditionFalse(Label.L3, input_condition=OR_4)
    DisableFlagRange((1300, 1319))
    EnableFlag(1312)
    EnableFlag(72400936)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    OR_5.Add(FlagEnabled(1100))
    OR_5.Add(FlagEnabled(1101))
    OR_5.Add(FlagEnabled(1102))
    OR_5.Add(FlagEnabled(1103))
    OR_5.Add(FlagEnabled(1104))
    OR_5.Add(FlagEnabled(1105))
    GotoIfConditionFalse(Label.L4, input_condition=OR_5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1108)
    EnableFlag(72400937)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    OR_6.Add(FlagEnabled(1224))
    OR_6.Add(FlagEnabled(1225))
    OR_6.Add(FlagEnabled(1226))
    OR_6.Add(FlagEnabled(1228))
    OR_6.Add(FlagEnabled(1229))
    GotoIfConditionFalse(Label.L5, input_condition=OR_6)
    DisableFlagRange((1220, 1239))
    EnableFlag(1231)
    EnableFlag(72400938)
    Goto(Label.L9)

    # --- Label 9 --- #
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

    # --- Label 5 --- #
    DefineLabel(5)
    End()


@ContinueOnRest(12400630)
def Event_12400630(_, character: int):
    """Event 12400630"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    AND_1.Add(HealthRatio(character) == 0.0)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    MAIN.Await(CharacterDead(character))
    
    EnableFlag(9432)
    EnableFlag(72400490)


@ContinueOnRest(12400650)
def Event_12400650():
    """Event 12400650"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    AND_1.Add(FlagEnabled(1362))
    AND_1.Add(FlagEnabled(72400520))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1363)
    AND_2.Add(FlagEnabled(72400524))
    SkipLinesIfConditionFalse(3, AND_2)
    DisableFlagRange((1360, 1379))
    EnableFlag(1368)
    EnableFlag(1376)

    # --- Label 0 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableBackread(2400900)
    EnableBackread(2400902)
    SetTeamType(2400902, TeamType.HostileNPC)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableBackread(2400900)
    DisableBackread(2400902)
    EnableBackread(2400903)
    ForceAnimation(2400903, 103031, loop=True)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(2400900)
    DisableBackread(2400902)
    EnableBackread(2400903)
    ForceAnimation(2400903, 103031, loop=True)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    if FlagEnabled(1705):
        DisableBackread(2400900)
        EnableBackread(2400902)
        SetTeamType(2400902, TeamType.HostileNPC)
        DisableBackread(2400903)
        Goto(Label.L9)
    if FlagEnabled(1704):
        DisableBackread(2400900)
        DisableBackread(2400902)
        EnableBackread(2400903)
        SetTeamType(2400903, TeamType.HostileNPC)
        Goto(Label.L9)
    if FlagEnabled(1701):
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

    # --- Label 5 --- #
    DefineLabel(5)
    DisableBackread(2400900)
    DisableCharacter(2400900)
    DisableBackread(2400902)
    DisableCharacter(2400902)
    DisableBackread(2400903)
    DisableCharacter(2400903)
    if FlagEnabled(1705):
        DropMandatoryTreasure(2400902)
        Goto(Label.L9)
    if FlagEnabled(1704):
        DropMandatoryTreasure(2400903)
        Goto(Label.L9)
    if FlagEnabled(1701):
        DropMandatoryTreasure(2400900)
        Goto(Label.L9)
    if FlagEnabled(1703):
        Goto(Label.L9)
    if FlagEnabled(1702):
        Goto(Label.L9)
    Goto(Label.L9)

    # --- Label 6 --- #
    DefineLabel(6)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- Label 7 --- #
    DefineLabel(7)
    EnableBackread(2400900)
    ForceAnimation(2400900, 103030, loop=True)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- Label 8 --- #
    DefineLabel(8)
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)
    Goto(Label.L9)

    # --- Label 9 --- #
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


@ContinueOnRest(12400651)
def Event_12400651():
    """Event 12400651"""
    AND_1.Add(FlagEnabled(1360))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2404390))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1360, 1379))
    EnableFlag(1362)
    EnableBackread(2400900)
    ForceAnimation(2400900, 103030, loop=True)
    DisableBackread(2400902)
    DisableBackread(2400903)


@ContinueOnRest(12400652)
def Event_12400652():
    """Event 12400652"""
    AND_1.Add(FlagEnabled(1361))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2404390))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1360, 1379))
    EnableFlag(1363)
    EnableBackread(2400900)
    ForceAnimation(2400900, 103030, loop=True)
    DisableBackread(2400902)
    DisableBackread(2400903)


@ContinueOnRest(12400653)
def Event_12400653():
    """Event 12400653"""
    if ThisEventFlagEnabled():
        return
    DisableMapPiece(map_piece_id=2404610)
    
    MAIN.Await(FlagEnabled(1370))
    
    EnableMapPiece(map_piece_id=2404610)


@ContinueOnRest(12400654)
def Event_12400654():
    """Event 12400654"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2400901)
    DisableCharacter(2400901)
    DropMandatoryTreasure(2400901)
    End()
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(2400901))
    
    if FlagDisabled(1370):
        return
    DisableFlagRange((1360, 1379))
    EnableFlag(1371)


@ContinueOnRest(12400655)
def Event_12400655():
    """Event 12400655"""
    if ThisEventFlagEnabled():
        return
    DisableBackread(2400901)
    
    MAIN.Await(FlagEnabled(1370))
    
    EnableBackread(2400901)


@ContinueOnRest(12400656)
def Event_12400656():
    """Event 12400656"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(1374))
    AND_1.Add(FlagEnabled(9802))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1360, 1379))
    EnableFlag(1372)
    DisableBackread(2400900)
    EnableBackread(2400902)
    SetTeamType(2400902, TeamType.HostileNPC)
    DisableBackread(2400903)


@ContinueOnRest(12400657)
def Event_12400657():
    """Event 12400657"""
    if ThisEventFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterDead(2400900))
    AND_2.Add(CharacterDead(2400902))
    AND_3.Add(CharacterDead(2400903))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
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


@ContinueOnRest(12400658)
def Event_12400658():
    """Event 12400658"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(72400526))
    
    DisableFlagRange((1700, 1705))
    SkipLinesIfFlagRangeAllDisabled(1, (1362, 1364))
    EnableFlag(1701)
    SkipLinesIfFlagRangeAllDisabled(1, (1370, 1371))
    EnableFlag(1704)
    if FlagEnabled(1372):
        EnableFlag(1705)
    DisableFlagRange((1360, 1379))
    EnableFlag(1369)
    SetTeamType(2400900, TeamType.HostileNPC)
    SaveRequest()


@ContinueOnRest(12400659)
def Event_12400659():
    """Event 12400659"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(Attacked(attacked_entity=2400900, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(Attacked(attacked_entity=2400900, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(Attacked(attacked_entity=2400900, attacker=PLAYER))
    
    WaitFrames(frames=1)


@ContinueOnRest(12400660)
def Event_12400660():
    """Event 12400660"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(1373))
    
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@ContinueOnRest(12400661)
def Event_12400661():
    """Event 12400661"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(1374))
    
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@ContinueOnRest(12400662)
def Event_12400662():
    """Event 12400662"""
    AND_1.Add(FlagEnabled(1370))
    AND_1.Add(FlagEnabled(72400530))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2400903, 103034, loop=True)
    
    MAIN.Await(FlagDisabled(72400530))
    
    ForceAnimation(2400903, 103031, loop=True)
    Restart()


@ContinueOnRest(12400663)
def Event_12400663():
    """Event 12400663"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagEnabled(1370))
    OR_1.Add(FlagEnabled(1371))
    AND_1.Add(OR_1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=2400903, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2400903, 103032)
    Kill(2400903, award_souls=True)


@ContinueOnRest(12400665)
def Event_12400665():
    """Event 12400665"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagEnabled(1365))
    OR_1.Add(FlagEnabled(1366))
    OR_1.Add(FlagEnabled(1367))
    
    MAIN.Await(OR_1)
    
    DisableBackread(2400900)
    DisableBackread(2400902)
    DisableBackread(2400903)


@RestartOnRest(12400700)
def Event_12400700():
    """Event 12400700"""
    AND_1.Add(FlagEnabled(1106))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    ForceAnimation(2400700, 2250)
    DropMandatoryTreasure(2400700)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagEnabled(1108))
    GotoIfConditionFalse(Label.L1, input_condition=AND_2)
    DisableBackread(2400700)
    DropMandatoryTreasure(2400700)
    EnableMapPiece(map_piece_id=2404604)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(FlagEnabled(1109))
    if not AND_3:
        return
    DisableFlag(1109)


@RestartOnRest(12400701)
def Event_12400701():
    """Event 12400701"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(72400300))
    
    DisableFlagRange((1100, 1119))
    EnableFlag(1101)


@RestartOnRest(12400702)
def Event_12400702():
    """Event 12400702"""
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(1106):
        return
    if FlagEnabled(1108):
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(12400720, 12400724)))
    AND_2.Add(FlagEnabled(1106))
    AND_3.Add(FlagEnabled(1108))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultFalse(input_condition=AND_1)
    DisableFlagRange((1100, 1119))
    EnableFlag(1102)


@RestartOnRest(12400703)
def Event_12400703():
    """Event 12400703"""
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(1106):
        return
    if FlagEnabled(1108):
        return
    AND_1.Add(FlagEnabled(72400985))
    AND_2.Add(FlagEnabled(1106))
    AND_3.Add(FlagEnabled(1108))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultFalse(input_condition=AND_1)
    DisableFlagRange((1100, 1119))
    EnableFlag(1103)


@RestartOnRest(12400704)
def Event_12400704():
    """Event 12400704"""
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(1106):
        return
    if FlagEnabled(1108):
        return
    OR_1.Add(FlagEnabled(1164))
    OR_1.Add(FlagEnabled(1165))
    OR_1.Add(FlagEnabled(1167))
    OR_2.Add(FlagEnabled(1181))
    OR_2.Add(FlagEnabled(1185))
    OR_2.Add(FlagEnabled(1186))
    OR_2.Add(FlagEnabled(1188))
    OR_3.Add(FlagEnabled(1224))
    OR_3.Add(FlagEnabled(1225))
    OR_3.Add(FlagEnabled(1226))
    OR_4.Add(FlagEnabled(1304))
    OR_4.Add(FlagEnabled(1305))
    OR_4.Add(FlagEnabled(1307))
    OR_4.Add(FlagEnabled(1308))
    OR_5.Add(FlagEnabled(1106))
    OR_5.Add(FlagEnabled(1108))
    AND_2.Add(OR_1)
    AND_2.Add(OR_2)
    AND_2.Add(OR_3)
    AND_2.Add(OR_4)
    OR_6.Add(AND_2)
    OR_6.Add(OR_5)
    
    MAIN.Await(OR_6)
    
    EndIfLastConditionResultTrue(input_condition=OR_5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1104)


@RestartOnRest(12400705)
def Event_12400705():
    """Event 12400705"""
    if ThisEventFlagEnabled():
        return
    if FlagEnabled(1106):
        return
    if FlagEnabled(1108):
        return
    AND_1.Add(FlagDisabled(1164))
    AND_1.Add(FlagDisabled(1165))
    AND_1.Add(FlagDisabled(1167))
    AND_2.Add(FlagDisabled(1181))
    AND_2.Add(FlagDisabled(1185))
    AND_2.Add(FlagDisabled(1186))
    AND_2.Add(FlagDisabled(1188))
    AND_3.Add(FlagDisabled(1224))
    AND_3.Add(FlagDisabled(1225))
    AND_3.Add(FlagDisabled(1226))
    AND_4.Add(FlagDisabled(1304))
    AND_4.Add(FlagDisabled(1305))
    AND_4.Add(FlagDisabled(1307))
    AND_4.Add(FlagDisabled(1308))
    OR_3.Add(FlagEnabled(1106))
    OR_3.Add(FlagEnabled(1108))
    AND_5.Add(OR_3)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    AND_6.Add(OR_1)
    AND_6.Add(FlagRangeAllEnabled(flag_range=(12400708, 12400711)))
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    
    MAIN.Await(OR_2)
    
    EndIfLastConditionResultTrue(input_condition=AND_5)
    DisableFlagRange((1100, 1119))
    EnableFlag(1105)


@RestartOnRest(12400706)
def Event_12400706():
    """Event 12400706"""
    if FlagEnabled(1106):
        return

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterDead(2400700))
    AND_1.Add(FlagDisabled(1108))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1100, 1119))
    EnableFlag(1106)
    SaveRequest()


@RestartOnRest(12400707)
def Event_12400707():
    """Event 12400707"""
    MAIN.Await(EventValue(flag=12400733, bit_count=3) >= 3)
    
    EnableFlag(72400309)


@RestartOnRest(12400708)
def Event_12400708(_, flag: int, flag_1: int, flag_2: int, flag_3: int, left: int):
    """Event 12400708"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_3))
    if ValueEqual(left=left, right=1):
        OR_1.Add(FlagEnabled(1315))
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultFalse(input_condition=AND_1)
    IncrementEventValue(12400733, bit_count=3, max_value=5)
    EnableFlag(72400313)
    DisableFlagRange((72400314, 72400319))
    EnableFlag(flag_1)


@RestartOnRest(12400713)
def Event_12400713(_, flag: int, flag_1: int):
    """Event 12400713"""
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultFalse(Label.L0, input_condition=AND_1)
    DisableFlag(72400308)
    EnableFlag(72400307)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(72400307)
    EnableFlag(72400308)


@RestartOnRest(12400720)
def Event_12400720():
    """Event 12400720"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagEnabled(1161))
    OR_1.Add(FlagEnabled(1166))
    
    MAIN.Await(OR_1)
    
    EnableFlag(12400724)
    StopEvent(event_id=12400721)
    StopEvent(event_id=12400722)
    StopEvent(event_id=12400723)
    StopEvent(event_id=12400728)


@RestartOnRest(12400721)
def Event_12400721():
    """Event 12400721"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagEnabled(1183))
    OR_1.Add(FlagEnabled(1189))
    OR_1.Add(FlagEnabled(1191))
    
    MAIN.Await(OR_1)
    
    EnableFlag(12400725)
    StopEvent(event_id=12400720)
    StopEvent(event_id=12400722)
    StopEvent(event_id=12400723)
    StopEvent(event_id=12400729)


@RestartOnRest(12400722)
def Event_12400722():
    """Event 12400722"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagEnabled(1222))
    OR_1.Add(FlagEnabled(1230))
    OR_1.Add(FlagEnabled(1231))
    
    MAIN.Await(OR_1)
    
    EnableFlag(12400726)
    StopEvent(event_id=12400720)
    StopEvent(event_id=12400721)
    StopEvent(event_id=12400723)
    StopEvent(event_id=12400730)


@RestartOnRest(12400723)
def Event_12400723():
    """Event 12400723"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagEnabled(1303))
    OR_1.Add(FlagEnabled(1312))
    
    MAIN.Await(OR_1)
    
    EnableFlag(12400727)
    StopEvent(event_id=12400720)
    StopEvent(event_id=12400721)
    StopEvent(event_id=12400722)
    StopEvent(event_id=12400731)


@RestartOnRest(12400728)
def Event_12400728():
    """Event 12400728"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(12400720, 12400723)))
    
    OR_1.Add(FlagEnabled(1161))
    OR_1.Add(FlagEnabled(1166))
    
    MAIN.Await(OR_1)
    
    EnableFlag(72400985)
    StopEvent(event_id=12400729)
    StopEvent(event_id=12400730)
    StopEvent(event_id=12400731)


@RestartOnRest(12400729)
def Event_12400729():
    """Event 12400729"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(12400720, 12400723)))
    
    OR_1.Add(FlagEnabled(1183))
    OR_1.Add(FlagEnabled(1189))
    OR_1.Add(FlagEnabled(1191))
    
    MAIN.Await(OR_1)
    
    EnableFlag(72400985)
    StopEvent(event_id=12400728)
    StopEvent(event_id=12400730)
    StopEvent(event_id=12400731)


@RestartOnRest(12400730)
def Event_12400730():
    """Event 12400730"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(12400720, 12400723)))
    
    OR_1.Add(FlagEnabled(1222))
    OR_1.Add(FlagEnabled(1230))
    OR_1.Add(FlagEnabled(1231))
    
    MAIN.Await(OR_1)
    
    EnableFlag(72400985)
    StopEvent(event_id=12400728)
    StopEvent(event_id=12400729)
    StopEvent(event_id=12400731)


@RestartOnRest(12400731)
def Event_12400731():
    """Event 12400731"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(12400720, 12400723)))
    
    OR_1.Add(FlagEnabled(1303))
    OR_1.Add(FlagEnabled(1312))
    
    MAIN.Await(OR_1)
    
    EnableFlag(72400985)
    StopEvent(event_id=12400728)
    StopEvent(event_id=12400729)
    StopEvent(event_id=12400730)


@RestartOnRest(12400732)
def Event_12400732():
    """Event 12400732"""
    AND_1.Add(AttackedWithDamageType(attacked_entity=2400700))
    AND_1.Add(FlagEnabled(72400981))
    
    MAIN.Await(AND_1)
    
    EnableFlag(1109)


@RestartOnRest(12400737)
def Event_12400737():
    """Event 12400737"""
    if FlagEnabled(1108):
        return
    DisableMapPiece(map_piece_id=2404604)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(1108))
    
    EnableMapPiece(map_piece_id=2404604)
    DropMandatoryTreasure(2400700)


@RestartOnRest(12400738)
def Event_12400738():
    """Event 12400738"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(9432))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(2400700, 5401)
    WaitFrames(frames=1)
    ForceAnimation(2400700, 7000)
    
    MAIN.Await(FlagDisabled(9432))
    
    AddSpecialEffect(2400700, 5402)
    WaitFrames(frames=1)
    ForceAnimation(2400700, 0)
    Restart()


@ContinueOnRest(12400900)
def Event_12400900():
    """Event 12400900"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L6, input_condition=AND_15)
    AND_1.Add(FlagEnabled(1313))
    GotoIfConditionFalse(Label.L1, input_condition=AND_1)
    DisableFlagRange((1300, 1319))
    EnableFlag(1304)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(FlagEnabled(72400942))
    AND_3.Add(FlagEnabled(72400380))
    OR_1.Add(FlagEnabled(1304))
    OR_1.Add(FlagEnabled(1305))
    AND_3.Add(OR_1)
    OR_2.Add(FlagEnabled(1224))
    OR_2.Add(FlagEnabled(1225))
    OR_2.Add(FlagEnabled(1226))
    OR_2.Add(FlagEnabled(1227))
    AND_3.Add(OR_2)
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    DisableFlagRange((1300, 1319))
    EnableFlag(1306)
    DisableFlagRange((1220, 1239))
    EnableFlag(1230)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L5, flag=9802)
    GotoIfFlagEnabled(Label.L3, flag=1304)
    GotoIfFlagEnabled(Label.L3, flag=1305)
    GotoIfFlagEnabled(Label.L4, flag=1306)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableFlagRange((1300, 1319))
    EnableFlag(1308)
    Goto(Label.L5)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlagRange((1300, 1319))
    EnableFlag(1307)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    DisableFlag(72400393)

    # --- Label 6 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    ForceAnimation(2400770, 103096, loop=True, skip_transition=True)
    Move(2400770, destination=2404503, destination_type=CoordEntityType.Region, short_move=True)
    if Client():
        return
    EnableFlag(72400491)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableBackread(2400770)
    DisableBackread(2400772)
    EnableBackread(2400774)
    DisableBackread(2400775)
    PostDestruction(2400773)
    ForceAnimation(2400774, 103096, loop=True, skip_transition=True)
    Move(2400774, destination=2404503, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableBackread(2400770)
    EnableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    ForceAnimation(2400772, 103096, loop=True, skip_transition=True)
    Move(2400772, destination=2404503, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 2 --- #
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

    # --- Label 3 --- #
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

    # --- Label 5 --- #
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

    # --- Label 6 --- #
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


@ContinueOnRest(12400901)
def Event_12400901():
    """Event 12400901"""
    MAIN.Await(FlagEnabled(72400394))
    
    DisableFlag(72400394)
    AND_1.Add(FlagEnabled(1304))
    AND_1.Add(FlagEnabled(72400380))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlagRange((1300, 1319))
    EnableFlag(1305)


@ContinueOnRest(12400940)
def Event_12400940(_, character: int):
    """Event 12400940"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(72400955))
    
    AND_1.Add(CharacterHasSpecialEffect(character, 157))
    AND_1.Add(FlagDisabled(72400955))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 103106)
    Restart()


@ContinueOnRest(12400903)
def Event_12400903():
    """Event 12400903"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1317):
        return
    if FlagEnabled(1312):
        return
    if FlagEnabled(1303):
        return
    OR_1.Add(CharacterDead(2400770))
    OR_1.Add(CharacterDead(2400772))
    OR_1.Add(CharacterDead(2400774))
    OR_1.Add(CharacterDead(2400775))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=1308)
    DisableFlagRange((1300, 1319))
    EnableFlag(1303)
    SaveRequest()
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlagRange((1300, 1319))
    EnableFlag(1317)
    SaveRequest()
    End()


@ContinueOnRest(12400904)
def Event_12400904():
    """Event 12400904"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(1308))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2404380))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=2400775))
    
    MAIN.Await(OR_1)
    
    EnableFlag(72400397)
    EnableAI(2400775)


@ContinueOnRest(12400910)
def Event_12400910(_, character: int):
    """Event 12400910"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=character))
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterHasSpecialEffect(character, 151))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(CharacterHasSpecialEffect(character, 158))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    ForceAnimation(character, 103134)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 103098)
    WaitFrames(frames=20)
    Restart()


@ContinueOnRest(12400915)
def Event_12400915(_, character: int):
    """Event 12400915"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1317):
        return
    if FlagEnabled(1312):
        return
    if FlagEnabled(1303):
        return
    AND_1.Add(HealthRatio(character) == 0.0)
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterHasSpecialEffect(character, 151))
    OR_1.Add(CharacterHasSpecialEffect(character, 158))
    AND_1.Add(OR_1)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    ForceAnimation(character, 103135)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 103099)
    End()


@ContinueOnRest(12400920)
def Event_12400920(_, character: int):
    """Event 12400920"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagDisabled(72400955))
    
    MAIN.Await(FlagEnabled(72400955))
    
    AND_1.Add(CharacterHasSpecialEffect(character, 151))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    ForceAnimation(character, 103104)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 103101)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 152))
    
    ForceAnimation(character, 103104)
    Restart()


@ContinueOnRest(12400925)
def Event_12400925(_, character: int):
    """Event 12400925"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    OR_1.Add(CharacterHasSpecialEffect(character, 153))
    OR_1.Add(CharacterHasSpecialEffect(character, 159))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    AND_1.Add(CharacterHasSpecialEffect(character, 153))
    GotoIfConditionTrue(Label.L2, input_condition=AND_1)
    AND_2.Add(CharacterHasSpecialEffect(character, 159))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(FlagEnabled(9432))
    AND_3.Add(FlagDisabled(1307))
    AND_3.Add(FlagDisabled(1306))
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    ForceAnimation(character, 103102, loop=True)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 103103, loop=True)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_4.Add(FlagEnabled(9432))
    AND_4.Add(FlagDisabled(1307))
    AND_4.Add(FlagDisabled(1306))
    GotoIfConditionTrue(Label.L3, input_condition=AND_4)
    ForceAnimation(character, 103096, loop=True)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    ForceAnimation(character, 103097, loop=True)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=5)
    Restart()


@ContinueOnRest(12400930)
def Event_12400930(_, character: int):
    """Event 12400930"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(character, 156))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 103102)
    Restart()


@ContinueOnRest(12400935)
def Event_12400935(_, character: int):
    """Event 12400935"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    AND_1.Add(CharacterHasSpecialEffect(character, 151))
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, 103101, wait_for_completion=True)


@ContinueOnRest(12400952)
def Event_12400952():
    """Event 12400952"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=1306)
    GotoIfFlagEnabled(Label.L0, flag=1308)
    GotoIfFlagEnabled(Label.L0, flag=1312)
    
    MAIN.Await(FlagEnabled(6001))
    
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DestroyObject(2400773)
    End()


@ContinueOnRest(12400953)
def Event_12400953():
    """Event 12400953"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(2400770) != 0.0)
    AND_1.Add(HealthRatio(2400774) != 0.0)
    AND_1.Add(FlagEnabled(9432))
    
    MAIN.Await(AND_1)
    
    OR_1.Add(CharacterHasSpecialEffect(2400770, 151))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    ForceAnimation(2400770, 103103)
    
    MAIN.Await(FlagDisabled(9432))
    
    ForceAnimation(2400770, 103102)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2400770, 103097)
    
    MAIN.Await(FlagDisabled(9432))
    
    ForceAnimation(2400770, 103096)
    Restart()


@ContinueOnRest(12400954)
def Event_12400954():
    """Event 12400954"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(PlayerHasGood(702))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisableFlag(72400392)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@ContinueOnRest(12400800)
def Event_12400800():
    """Event 12400800"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=2400765, attacker=PLAYER))
    AND_1.Add(HealthRatio(2400765) == 0.0)
    AND_2.Add(AttackedWithDamageType(attacked_entity=2400730, attacker=PLAYER))
    AND_2.Add(HealthRatio(2400730) == 0.0)
    AND_3.Add(AttackedWithDamageType(attacked_entity=2400750, attacker=PLAYER))
    AND_3.Add(HealthRatio(2400750) == 0.0)
    AND_4.Add(AttackedWithDamageType(attacked_entity=2400754, attacker=PLAYER))
    AND_4.Add(HealthRatio(2400754) == 0.0)
    AND_5.Add(AttackedWithDamageType(attacked_entity=2400757, attacker=PLAYER))
    AND_5.Add(HealthRatio(2400757) == 0.0)
    AND_7.Add(AttackedWithDamageType(attacked_entity=2400770, attacker=PLAYER))
    AND_7.Add(HealthRatio(2400770) == 0.0)
    AND_8.Add(AttackedWithDamageType(attacked_entity=2400772, attacker=PLAYER))
    AND_8.Add(HealthRatio(2400772) == 0.0)
    AND_9.Add(AttackedWithDamageType(attacked_entity=2400774, attacker=PLAYER))
    AND_9.Add(HealthRatio(2400774) == 0.0)
    AND_13.Add(AttackedWithDamageType(attacked_entity=2400700, attacker=PLAYER))
    AND_13.Add(HealthRatio(2400700) == 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_7)
    OR_1.Add(AND_8)
    OR_1.Add(AND_9)
    OR_1.Add(AND_13)
    
    MAIN.Await(OR_1)
    
    EnableFlag(9432)
    EnableFlag(72400490)


@ContinueOnRest(12400801)
def Event_12400801():
    """Event 12400801"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagDisabled(Label.L0, flag=1166)
    DisableBackread(2400765)
    Move(2400765, destination=2404500, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400765)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=1191)
    DisableBackread(2400730)
    DisableBackread(2400732)
    EnableObject(2400731)
    Move(2400730, destination=2404501, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400730)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, flag=1231)
    EnableObject(2400748)
    DisableMapPiece(map_piece_id=2404601)
    DisableBackread(2400750)
    DisableBackread(2400754)
    DisableBackread(2400757)
    Move(2400750, destination=2404502, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400750)

    # --- Label 2 --- #
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

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L4, flag=1312)
    DisableBackread(2400770)
    DisableBackread(2400772)
    DisableBackread(2400774)
    DisableBackread(2400775)
    Move(2400770, destination=2404506, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2400770)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagDisabled(Label.L4, flag=1108)
    EnableMapPiece(map_piece_id=2404604)
    DropMandatoryTreasure(2400700)
    DisableBackread(2400700)

    # --- Label 5 --- #
    DefineLabel(5)


@ContinueOnRest(12400805)
def Event_12400805(_, character: int, animation_id: int, special_effect: int):
    """Event 12400805"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id)
    WaitFrames(frames=5)
    Restart()


@ContinueOnRest(12400810)
def Event_12400810(_, character: int, animation_id: int):
    """Event 12400810"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(character) != 0.0)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id)
    Restart()


@ContinueOnRest(12400830)
def Event_12400830(_, character: int, animation_id: int):
    """Event 12400830"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(character) == 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id)


@ContinueOnRest(12400840)
def Event_12400840(_, flag: int, action_button_id: int, destination: int):
    """Event 12400840"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    DisableFlag(flag)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=destination))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, dummy_id=210, short_move=True)
    ForceAnimation(PLAYER, 101320)
    WaitFrames(frames=25)
    WaitFrames(frames=20)
    EnableFlag(flag)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@RestartOnRest(12405700)
def Event_12405700():
    """Event 12405700"""
    AND_1.Add(CharacterDead(2400393))
    AND_1.Add(CharacterDead(2400410))
    AND_2.Add(CharacterDead(2400393))
    AND_2.Add(CharacterDead(2400396))
    AND_3.Add(CharacterDead(2400410))
    AND_3.Add(CharacterDead(2400396))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfConditionTrue(Label.L2, input_condition=AND_3)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(2400396, command_id=10, command_slot=0)
    SetNest(2400396, region=2409007)
    ReplanAI(2400396)

    # --- Label 1 --- #
    DefineLabel(1)
    AICommand(2400410, command_id=10, command_slot=0)
    SetNest(2400410, region=2409007)
    ReplanAI(2400410)

    # --- Label 2 --- #
    DefineLabel(2)
    AICommand(2400393, command_id=10, command_slot=0)
    SetNest(2400393, region=2409007)
    ReplanAI(2400393)
    OR_2.Add(CharacterInsideRegion(2400393, region=2402030))
    OR_2.Add(CharacterInsideRegion(2400396, region=2402030))
    OR_2.Add(CharacterInsideRegion(2400410, region=2402030))
    
    MAIN.Await(OR_2)
    
    OR_3.Add(EntityWithinDistance(entity=2400393, other_entity=PLAYER, radius=5.0))
    OR_3.Add(EntityWithinDistance(entity=2400396, other_entity=PLAYER, radius=5.0))
    OR_3.Add(EntityWithinDistance(entity=2400410, other_entity=PLAYER, radius=5.0))
    
    MAIN.Await(OR_3)
    
    AICommand(2400393, command_id=-1, command_slot=0)
    ReplanAI(2400393)
    AICommand(2400396, command_id=-1, command_slot=0)
    ReplanAI(2400396)
    AICommand(2400410, command_id=-1, command_slot=0)
    ReplanAI(2400410)


@RestartOnRest(12405701)
def Event_12405701(_, character: int, region: int):
    """Event 12405701"""
    OR_1.Add(CharacterInsideRegion(2400393, region=2402030))
    OR_1.Add(CharacterInsideRegion(2400396, region=2402030))
    OR_1.Add(CharacterInsideRegion(2400410, region=2402030))
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=10, command_slot=0)
    SetNest(character, region=region)
    ReplanAI(character)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402030))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12405710)
def Event_12405710():
    """Event 12405710"""
    GotoIfFlagDisabled(Label.L0, flag=9453)
    EndOfAnimation(obj=2401202, animation_id=1)
    NotifyDoorEventSoundDampening(obj=2401202, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=7000, entity=2401202))
    
    DisplayDialog(text=10010171, anchor_entity=2401202, display_distance=5.0, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12405750)
def Event_12405750(_, attacked_entity: int, animation_id: int, radius: float):
    """Event 12405750"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(EntityWithinDistance(entity=attacked_entity, other_entity=PLAYER, radius=radius))
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EndIfLastConditionResultTrue(input_condition=AND_2)
    ForceAnimation(attacked_entity, animation_id)


@ContinueOnRest(12401800)
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

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(2400800))
    
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2401800)
    DeleteVFX(2403800)
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2400800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
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

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterWhitePhantom(PLAYER))
    
    Wait(0.0)
    if Client():
        return


@ContinueOnRest(12401801)
def Event_12401801():
    """Event 12401801"""
    DisableNetworkSync()
    if FlagEnabled(12401800):
        return
    AND_1.Add(FlagEnabled(12401800))
    AND_2.Add(CharacterBackreadDisabled(2400800))
    AND_2.Add(HealthRatio(2400800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_1)
    PlaySoundEffect(2402800, 0, sound_type=SoundType.c_CharacterMotion)


@ContinueOnRest(12401802)
def Event_12401802():
    """Event 12401802"""
    if FlagEnabled(12401800):
        return
    DisableObject(2400801)
    if ThisEventFlagEnabled():
        return
    DisableCharacter(2400800)
    EnableObject(2400801)
    EnableObjectInvulnerability(2400801)
    AND_1.Add(FlagDisabled(12401800))
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402805))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12404223)
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_2:
        return
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
    if FlagEnabled(9301):
        return
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9301)


@ContinueOnRest(12401803)
def Event_12401803():
    """Event 12401803"""
    DeleteVFX(2403413, erase_root_only=False)
    if ThisEventFlagEnabled():
        return
    GotoIfFlagEnabled(Label.L0, flag=12401800)
    
    MAIN.Await(FlagEnabled(12401800))

    # --- Label 0 --- #
    DefineLabel(0)
    CreateVFX(2403413)
    if Client():
        return
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2400010, entity=2401801))
    
    MAIN.Await(AND_1)
    
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


@ContinueOnRest(12401804)
def Event_12401804():
    """Event 12401804"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12404800))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableCharacter(2400800)
    EnableFlag(12404800)
    EnableFlag(12401802)


@ContinueOnRest(12404840)
def Event_12404840():
    """Event 12404840"""
    if FlagEnabled(12401800):
        return
    GotoIfFlagEnabled(Label.L0, flag=12401802)
    SkipLinesIfClient(2)
    DisableObject(2401800)
    DeleteVFX(2403800, erase_root_only=False)
    AND_1.Add(FlagDisabled(12401800))
    AND_1.Add(FlagEnabled(12401802))
    
    MAIN.Await(AND_1)
    
    EnableObject(2401800)
    CreateVFX(2403800)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12401800))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2400800, entity=2401800))
    AND_3.Add(FlagEnabled(12401800))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_3)
    FaceEntity(PLAYER, 2402800, animation=101130)
    AND_4.Add(CharacterHuman(PLAYER))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=2402801))
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(TimeElapsed(seconds=2.0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_5)
    EnableFlag(12404800)
    Restart()


@ContinueOnRest(12404841)
def Event_12404841():
    """Event 12404841"""
    DisableNetworkSync()
    if FlagEnabled(12401800):
        return
    AND_1.Add(FlagDisabled(12401800))
    AND_1.Add(FlagEnabled(12401802))
    AND_1.Add(FlagEnabled(12404800))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2400800, entity=2401800))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, 2402800, animation=101130)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2402801))
    AND_3.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfLastConditionResultTrue(1, input_condition=AND_3)
    EnableFlag(12404801)
    Restart()


@ContinueOnRest(12404842)
def Event_12404842():
    """Event 12404842"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2401800, radius=6.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12404843)
def Event_12404843():
    """Event 12404843"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2401800, radius=6.0))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2401800, radius=12.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12404802)
def Event_12404802():
    """Event 12404802"""
    if FlagEnabled(12401800):
        return
    DisableAI(2400800)
    DisableHealthBar(2400800)
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(12404800))
    
    GotoIfClient(Label.L0)
    if FlagDisabled(12404223):
        NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2400800, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12404223)
    EnableFlag(12404800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2400800, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2400800)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2400800, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2400800)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableAI(2400800)
    EnableBossHealthBar(2400800, name=502000)
    ForceAnimation(2400800, 7002)
    CreatePlayLog(name=160)
    StartPlayLogMeasurement(measurement_id=2410010, name=176, overwrite=True)


@ContinueOnRest(12404803)
def Event_12404803():
    """Event 12404803"""
    DisableNetworkSync()
    if FlagEnabled(12401800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2403802)
    DisableSoundEvent(sound_id=2403803)
    AND_1.Add(FlagDisabled(12401800))
    AND_1.Add(FlagEnabled(12404802))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(12404801))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2402802))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=2403802)
    AND_2.Add(CharacterHasTAEEvent(2400800, tae_event_id=100))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12401800))
    AND_2.Add(FlagEnabled(12404802))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(12404801))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2402802))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=2403802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2403803)


@ContinueOnRest(12404804)
def Event_12404804():
    """Event 12404804"""
    DisableNetworkSync()
    if FlagEnabled(12401800):
        return
    AND_1.Add(HealthRatio(2400800) > 0.0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2400800, radius=5.5))
    
    MAIN.Await(AND_1)
    
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=1)
    AND_2.Add(HealthRatio(2400800) > 0.0)
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2400800, radius=6.0))
    
    MAIN.Await(AND_2)
    
    SetLockedCameraSlot(game_map=CATHEDRAL_WARD, camera_slot=0)
    Restart()


@ContinueOnRest(12404805)
def Event_12404805():
    """Event 12404805"""
    DisableNetworkSync()
    if FlagEnabled(12401800):
        return
    
    MAIN.Await(FlagEnabled(12401800))
    
    DisableBossMusic(sound_id=2403802)
    DisableBossMusic(sound_id=2403803)
    DisableBossMusic(sound_id=-1)


@ContinueOnRest(12404807)
def Event_12404807():
    """Event 12404807"""
    if FlagEnabled(12401800):
        return
    
    MAIN.Await(HealthRatio(2400800) < 0.5)
    
    AICommand(2400800, command_id=100, command_slot=1)
    ReplanAI(2400800)
    
    MAIN.Await(CharacterHasTAEEvent(2400800, tae_event_id=100))
    
    AICommand(2400800, command_id=-1, command_slot=1)
    ReplanAI(2400800)


@ContinueOnRest(12404808)
def Event_12404808():
    """Event 12404808"""
    if FlagEnabled(12401800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterHasSpecialEffect(2400800, 482))

    # --- Label 0 --- #
    DefineLabel(0)
    ChangeCharacterCloth(2400800, bit_count=15, state_id=2)


@RestartOnRest(12404810)
def Event_12404810(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect: int,
    special_effect_1: int,
    animation_id: int,
):
    """Event 12404810"""
    if FlagEnabled(12401800):
        return
    CreateNPCPart(2400800, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(2400800, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    AND_2.Add(CharacterPartHealth(2400800, npc_part_id=npc_part_id_1) <= 0)
    AND_3.Add(HealthRatio(2400800) <= 0.0)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfLastConditionResultTrue(input_condition=AND_3)
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
    AddSpecialEffect(2400800, special_effect)
    RemoveSpecialEffect(2400800, special_effect_1)
    ReplanAI(2400800)
    Wait(30.0)
    AICommand(2400800, command_id=1, command_slot=0)
    ReplanAI(2400800)
    
    MAIN.Await(CharacterHasTAEEvent(2400800, tae_event_id=300))
    
    SetNPCPartHealth(2400800, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(2400800, special_effect_1)
    RemoveSpecialEffect(2400800, special_effect)
    AICommand(2400800, command_id=-1, command_slot=0)
    ReplanAI(2400800)
    WaitFrames(frames=10)
    Restart()


@ContinueOnRest(12404820)
def Event_12404820(_, special_effect: int, special_effect_1: int, bit_index: uchar, bit_index_1: uchar):
    """Event 12404820"""
    if FlagEnabled(12401800):
        return
    AND_1.Add(CharacterHasSpecialEffect(2400800, special_effect))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(2400800, special_effect_1))
    
    MAIN.Await(AND_1)
    
    SetDisplayMask(2400800, bit_index=bit_index_1, switch_type=OnOffChange.On)
    SetDisplayMask(2400800, bit_index=bit_index, switch_type=OnOffChange.Off)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(2400800, special_effect))
    AND_2.Add(CharacterHasSpecialEffect(2400800, special_effect_1))
    
    MAIN.Await(AND_2)
    
    SetDisplayMask(2400800, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(2400800, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(12404830)
def Event_12404830():
    """Event 12404830"""
    AND_1.Add(CharacterHasSpecialEffect(2400800, 2150))
    AND_1.Add(CharacterHasSpecialEffect(2400800, 5639))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2400800, 3035)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(12406900)
def Event_12406900(_, region: int, anchor_entity: int, sound_id: int):
    """Event 12406900"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    PlaySoundEffect(anchor_entity, sound_id, sound_type=SoundType.a_Ambient)
    WaitFrames(frames=1)


@ContinueOnRest(12400990)
def Event_12400990():
    """Event 12400990"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(PlayerStandingOnCollision(2404101))
    
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


@ContinueOnRest(12407020)
def Event_12407020(_, flag: int, destination: int):
    """Event 12407020"""
    MAIN.Await(FlagEnabled(flag))
    
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, dummy_id=200, short_move=True)
    ForceAnimation(PLAYER, 101160, skip_transition=True)
    Wait(4.0)
    DisableFlag(flag)


@ContinueOnRest(12407040)
def Event_12407040(_, flag: int, respawn_point_id: int, flag_1: int):
    """Event 12407040"""
    MAIN.Await(FlagEnabled(flag))
    
    DisableFlag(flag)
    WarpPlayerToRespawnPoint(respawn_point_id)
    EnableFlag(flag_1)


@RestartOnRest(12407050)
def Event_12407050(_, flag: int, character: int, destination: int):
    """Event 12407050"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    Move(character, destination=destination, destination_type=CoordEntityType.Object, dummy_id=250, short_move=True)
    ForceAnimation(character, 101165, loop=True)
    Wait(1.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Object, dummy_id=250, short_move=True)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(character, 101166, wait_for_completion=True)
    DisableCharacter(character)


@ContinueOnRest(12407000)
def Event_12407000():
    """Event 12407000"""
    SkipLinesIfFlagRangeAnyEnabled(1, (9001, 9010))
    End()
    EnableFlag(9210)
    
    MAIN.Await(FlagDisabled(9210))
    
    if FlagEnabled(9001):
        EnableFlag(12407811)
        EnableFlag(12407810)
        SetRespawnPoint(respawn_point=2402950)
    if FlagEnabled(9002):
        EnableFlag(12407831)
        EnableFlag(12407830)
        SetRespawnPoint(respawn_point=2402951)
    if FlagEnabled(9003):
        EnableFlag(12407851)
        EnableFlag(12407850)
        SetRespawnPoint(respawn_point=2402952)
    if FlagEnabled(9004):
        EnableFlag(12407871)
        EnableFlag(12407870)
        SetRespawnPoint(respawn_point=2402953)
    if FlagEnabled(9005):
        EnableFlag(12407891)
        EnableFlag(12407890)
        SetRespawnPoint(respawn_point=2402954)
    if FlagEnabled(9006):
        EnableFlag(12407911)
        EnableFlag(12407910)
        SetRespawnPoint(respawn_point=2402955)
    if FlagEnabled(9007):
        EnableFlag(12407931)
        EnableFlag(12407930)
        SetRespawnPoint(respawn_point=2402956)
    if FlagEnabled(9008):
        EnableFlag(12407951)
        EnableFlag(12407950)
        SetRespawnPoint(respawn_point=2402957)
    if FlagEnabled(9009):
        EnableFlag(12407971)
        EnableFlag(12407970)
        SetRespawnPoint(respawn_point=2402958)
    if FlagEnabled(9010):
        EnableFlag(12407991)
        EnableFlag(12407990)
        SetRespawnPoint(respawn_point=2402959)
    DisableFlagRange((9000, 9010))


@RestartOnRest(12404450)
def Event_12404450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 12404450"""
    if ThisEventSlotFlagEnabled():
        return
    if Client():
        return
    SetEventPoint(character, region=region, reaction_range=1.0)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12404400)
def Event_12404400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12404400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(FlagDisabled(2400))
    AND_1.Add(FlagDisabled(2401))
    OR_1.Add(FlagDisabled(flag_4))
    AND_1.Add(OR_1)
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)
    CreateVFX(vfx_id)
    AND_2.Add(PlayerHasGood(4312))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagDisabled(flag_3))
    AND_2.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_2.Add(FlagDisabled(2400))
    AND_2.Add(FlagDisabled(2401))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
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
    if FlagDisabled(summon_flag):
        DisableCharacter(character)
    SkipLinesIfFlagEnabled(3, dismissal_flag)
    AND_1.Add(Client())
    AND_1.Add(FlagEnabled(summon_flag))
    SkipLinesIfConditionTrue(1, AND_1)
    DisableCharacter(character)
    if FlagEnabled(flag_1):
        return
    AND_3.Add(Client())
    SkipLinesIfConditionTrue(1, AND_3)
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    AND_2.Add(PlayerHasGood(4312))
    AND_2.Add(FlagDisabled(summon_flag))
    AND_2.Add(FlagDisabled(dismissal_flag))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagDisabled(flag_1))
    AND_2.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=character))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682)
    SummonNPC(sign_type, character, region=region, summon_flag=summon_flag, dismissal_flag=dismissal_flag)
    RemoveSpecialEffect(PLAYER, 9005)
    RemoveSpecialEffect(PLAYER, 9025)
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
    if Client():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterInsideRegion(character, region=region))
    
    MAIN.Await(AND_1)
    
    ResetAnimation(character)
    FaceEntity(character, region_1, animation=animation, wait_for_completion=True)
    AND_2.Add(CharacterInsideRegion(character, region=region_2))
    if not AND_2:
        return RESTART
    SetEventPoint(character, region=region_1, reaction_range=1.0)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region_3))
    
    EnableGravity(character)
    EnableCharacterCollision(character)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12404490)
def Event_12404490():
    """Event 12404490"""
    DisableNetworkSync()
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(12404420))
    AND_1.Add(FlagDisabled(12404430))
    AND_1.Add(FlagEnabled(12404800))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect_WithUnknownEffect(2400910, 35)
    WaitFrames(frames=1)
    Restart()
