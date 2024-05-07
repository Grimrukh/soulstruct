"""
Yahar'gul, Unseen Village

linked:
298

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: 生贄の街_テレポーター使用_00
74: 生贄の街_テレポーター使用_01
108: 生贄の街_テレポーター領域侵入_00
146: 生贄の街_テレポーター領域侵入_01
184: 
186: ボス_撃破
198: PC情報_ボス撃破_なりそこないの邪神
238: ボス_戦闘開始
254: ボス戦_撃破時間
272: PC情報_生贄の街到達時
298: N:\\SPRJ\\data\\Param\\event\\common.emevd
374: 
376: 
378: 
380: 
382: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterLadder(start_climbing_flag=12800350, stop_climbing_flag=12800351, obj=2801250)
    RunEvent(7600, slot=60, args=(2801999, 2803999))
    RunEvent(7600, slot=61, args=(2801998, 2803998))
    RunEvent(7000, slot=40, args=(2800950, 2801950, 999, 12807800))
    RunEvent(7000, slot=41, args=(2800951, 2801951, 12801800, 12807820))
    if FlagDisabled(9802):
        RunEvent(7000, slot=42, args=(2800952, 2801952, 999, 12807840))
    RunEvent(7000, slot=43, args=(2800953, 2801953, 999, 12807860))
    RunEvent(7100, slot=40, args=(72800200, 2801950))
    RunEvent(7100, slot=41, args=(72800201, 2801951))
    if FlagDisabled(9802):
        RunEvent(7100, slot=42, args=(72800202, 2801952))
    RunEvent(7100, slot=43, args=(72800203, 2801953))
    RunEvent(7200, slot=40, args=(72800100, 2801950, 2102952))
    RunEvent(7200, slot=41, args=(72800101, 2801951, 2102952))
    if FlagDisabled(9802):
        RunEvent(7200, slot=42, args=(72800102, 2801952, 2102952))
    RunEvent(7200, slot=43, args=(72800103, 2801953, 2102953))
    RunEvent(7300, slot=40, args=(72102800, 2801950))
    RunEvent(7300, slot=41, args=(72102801, 2801951))
    if FlagDisabled(9802):
        RunEvent(7300, slot=42, args=(72102802, 2801952))
    RunEvent(7300, slot=43, args=(72102803, 2801953))
    Event_12800140()
    RunEvent(9200, slot=8, args=(2803900,))
    Event_12800160()
    RunEvent(9220, slot=7, args=(2800710, 12804220, 12804221, 2800, 28))
    RunEvent(9240, slot=7, args=(2800710, 12804220, 12804221, 12804222, 28))
    RunEvent(9260, slot=7, args=(2800710, 12804220, 12804221, 12804222, 28))
    RunEvent(9280, slot=7, args=(2800710, 12804220, 12804221, 2800, 12804223, 28))
    Event_12800999()
    Event_12800435()
    Event_12800436()
    Event_12800400()
    Event_12800401()
    Event_12800402()
    Event_12800403()
    CreateObjectVFX(2801010, vfx_id=200, dummy_id=900130)
    StartPlayLogMeasurement(measurement_id=2800000, name=0, overwrite=True)
    StartPlayLogMeasurement(measurement_id=2800001, name=18, overwrite=True)
    Event_12800990()
    AND_15.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_15)
    if FlagEnabled(6322):
        EnableFlag(12801999)
    if FlagDisabled(12801999):
        EnableObject(2801550)
        DisableObject(2801551)
        EnableTreasure(obj=2801550)
        DisableTreasure(obj=2801551)
    else:
        DisableObject(2801550)
        EnableObject(2801551)
        DisableTreasure(obj=2801550)
        EnableTreasure(obj=2801551)
    AND_14.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_14)
    if FlagEnabled(6323):
        EnableFlag(12801998)
    if FlagDisabled(12801998):
        EnableObject(2801552)
        DisableObject(2801553)
        EnableTreasure(obj=2801552)
        DisableTreasure(obj=2801553)
    else:
        DisableObject(2801552)
        EnableObject(2801553)
        DisableTreasure(obj=2801552)
        EnableTreasure(obj=2801553)
    AND_13.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_13)
    if FlagEnabled(6324):
        EnableFlag(12801997)
    if FlagDisabled(12801997):
        EnableObject(2801554)
        DisableObject(2801555)
        EnableTreasure(obj=2801554)
        DisableTreasure(obj=2801555)
    else:
        DisableObject(2801554)
        EnableObject(2801555)
        DisableTreasure(obj=2801554)
        EnableTreasure(obj=2801555)
    Event_12800901()
    Event_12800902()
    Event_12800903()
    Event_12800904()
    Event_12800905()
    Event_12800906()
    Event_12800908()
    Event_12800909()
    Event_12800910()
    DeleteVFX(2803920, erase_root_only=False)
    DeleteVFX(2803921, erase_root_only=False)
    Event_12804400(0, flag=12804440, vfx_id=2803920, flag_1=12804420, flag_2=12804430, flag_3=12801800, flag_4=12804421)
    Event_12804401(0, flag=12804441, vfx_id=2803921, flag_1=12804421, flag_2=12804431, flag_3=12801800, flag_4=12804420)
    Event_12804410(
        0,
        sign_type=5,
        character=2800910,
        region=2802910,
        summon_flag=12804420,
        dismissal_flag=12804430,
        flag=12804440,
        flag_1=12801800,
        action_button_id=10564,
    )
    Event_12804410(
        1,
        sign_type=0,
        character=2800911,
        region=2802913,
        summon_flag=12804421,
        dismissal_flag=12804431,
        flag=12804441,
        flag_1=12801800,
        action_button_id=10568,
    )
    Event_12804450(0, character=2800910, region=2802911, flag=12804420, flag_1=12804430, flag_2=12804800)
    Event_12804450(1, character=2800911, region=2802914, flag=12804421, flag_1=12804431, flag_2=12804800)
    Event_12804460(
        0,
        character=2800910,
        region=2802911,
        region_1=2802800,
        region_2=2802801,
        animation=101130,
        flag=12804450,
        region_3=2802801,
    )
    Event_12804460(
        1,
        character=2800911,
        region=2802914,
        region_1=2802800,
        region_2=2802801,
        animation=101130,
        flag=12804451,
        region_3=2802801,
    )
    Event_12804882()
    Event_12804883()
    Event_12801800()
    Event_12801801()
    Event_12801802()
    Event_12804880()
    Event_12804881()
    Event_12804802()
    Event_12804803()
    Event_12804804()
    Event_12804805()
    Event_12804806()
    Event_12804807()
    Event_12801803()
    Event_12804820(
        0,
        npc_part_id=2800,
        npc_part_id_1=2800,
        part_index=1,
        part_health=100,
        special_effect=480,
        special_effect_1=490,
        animation_id=7000,
    )
    Event_12804820(
        1,
        npc_part_id=2801,
        npc_part_id_1=2801,
        part_index=2,
        part_health=200,
        special_effect=481,
        special_effect_1=491,
        animation_id=7001,
    )
    Event_12804820(
        2,
        npc_part_id=2802,
        npc_part_id_1=2802,
        part_index=3,
        part_health=200,
        special_effect=482,
        special_effect_1=492,
        animation_id=7002,
    )
    Event_12804820(
        3,
        npc_part_id=2803,
        npc_part_id_1=2803,
        part_index=4,
        part_health=100,
        special_effect=483,
        special_effect_1=493,
        animation_id=7003,
    )
    Event_12804820(
        4,
        npc_part_id=2804,
        npc_part_id_1=2804,
        part_index=5,
        part_health=200,
        special_effect=484,
        special_effect_1=494,
        animation_id=7004,
    )
    Event_12804820(
        5,
        npc_part_id=2805,
        npc_part_id_1=2805,
        part_index=6,
        part_health=200,
        special_effect=485,
        special_effect_1=495,
        animation_id=7005,
    )
    Event_12804820(
        6,
        npc_part_id=2806,
        npc_part_id_1=2806,
        part_index=7,
        part_health=100,
        special_effect=486,
        special_effect_1=496,
        animation_id=7006,
    )
    Event_12804830()
    Event_12804831()
    Event_12804832()
    Event_12804834()
    Event_12804835()
    Event_12804836()
    Event_12804837()
    Event_12804838()
    Event_12804840(0, character=2800522)
    Event_12804840(1, character=2800527)
    Event_12804850(0, character=2800520)
    Event_12804850(2, character=2800522)
    Event_12804850(4, character=2800524)
    Event_12804850(5, character=2800525)
    Event_12804850(7, character=2800527)
    Event_12804850(9, character=2800529)
    Event_12804870()
    Event_12804871()
    Event_12800100(0, obj=2801350, obj_act_id=12800250)
    Event_12800100(1, obj=2801351, obj_act_id=12800251)
    Event_12800100(2, obj=2801352, obj_act_id=12800252)
    Event_12800100(3, obj=2801353, obj_act_id=12800253)
    Event_12800100(4, obj=2801354, obj_act_id=12800254)
    Event_12800100(5, obj=2801355, obj_act_id=12800255)
    Event_12800120(0, entity=2801010, action_button_id=7413, text=10012013)
    Event_12800480(0, obj=2801200, obj_act_id=12800201, animation_id=1, obj_act_id_1=31)
    Event_12800480(1, obj=2801202, obj_act_id=12800202, animation_id=1, obj_act_id_1=30)
    Event_12800480(2, obj=2801203, obj_act_id=12800203, animation_id=1, obj_act_id_1=30)
    Event_12800480(3, obj=2801206, obj_act_id=12800206, animation_id=1, obj_act_id_1=30)
    Event_12800480(4, obj=2801208, obj_act_id=12800209, animation_id=1, obj_act_id_1=2800020)
    Event_12800490(0, action_button_id=7030, anchor_entity=2801200, flag=12800480)
    Event_12800490(1, action_button_id=7031, anchor_entity=2801202, flag=12800481)
    Event_12800490(2, action_button_id=7031, anchor_entity=2801203, flag=12800482)
    Event_12800490(3, action_button_id=7031, anchor_entity=2801206, flag=12800483)
    Event_12800490(4, action_button_id=7030, anchor_entity=2801208, flag=12800484)
    Event_12800430()
    Event_12800431()
    Event_12800432()
    Event_12800433(0, character=2800740)
    Event_12800433(1, character=2800745)
    Event_12805160(0, character=2800244, region=2802230, radius=1.0)
    Event_12805160(1, character=2800245, region=2802230, radius=1.0)
    Event_12805160(2, character=2800243, region=2802230, radius=1.0)
    Event_12805180(2, character=2800210, region=2802270)
    Event_12805470(
        0,
        npc_part_id=11,
        npc_part_id_1=11,
        part_index=7,
        animation_id=7003,
        special_effect=5907,
        flag=12805655,
        flag_1=12805665,
        character=2800210,
    )
    Event_12805470(
        1,
        npc_part_id=12,
        npc_part_id_1=12,
        part_index=8,
        animation_id=7000,
        special_effect=5907,
        flag=12805655,
        flag_1=12805665,
        character=2800210,
    )
    Event_12805480(0, npc_part_id=11, npc_part_id_1=11, part_index=7, part_health=80, flag=12805655, character=2800210)
    Event_12805480(1, npc_part_id=12, npc_part_id_1=12, part_index=8, part_health=80, flag=12805655, character=2800210)
    Event_12805490(0, tae_event_id=10, tae_event_id_1=40, flag=12805665, character=2800210)
    Event_12805490(1, tae_event_id=30, tae_event_id_1=40, flag=12805665, character=2800210)
    Event_12800500(1, character=2800721, flag=52800980)
    Event_12800500(2, character=2800722, flag=52800970)
    Event_12800500(0, character=2800720, flag=52800990)
    Event_12800500(3, character=2800723, flag=52800960)
    GotoIfFlagDisabled(Label.L4, flag=9802)
    Event_12800600(
        0,
        flag=12804700,
        flag_1=12800610,
        flag_2=12800611,
        flag_3=12800612,
        obj=2801400,
        obj_1=2801401,
        obj_2=2801402,
    )
    Event_12800601(0, flag=12804700, flag_1=12800610, flag_2=12800611, flag_3=12800612)
    Event_12800602(
        0,
        flag=12804700,
        flag_1=12800610,
        flag_2=12800611,
        flag_3=12800612,
        region=2802102,
        obj_act_id=12800280,
    )
    Event_12800604(
        0,
        flag=12804700,
        flag_1=12800610,
        flag_2=12800611,
        flag_3=12800612,
        region=2802101,
        obj_act_id=12800281,
    )
    Event_12800606(0, flag=12804700, flag_1=12800610, flag_2=12800612, entity=2801401, entity_1=2801402)
    Event_12800607(0, flag=12800612, region=2802100, obj=2801401, obj_1=2801402)
    Event_12800470(0, entity=2800742, animation_id=7000)
    Event_12800470(1, entity=2800743, animation_id=7001)
    Event_12800470(2, entity=2800744, animation_id=7003)
    Event_12800460(0, entity=2801100, move_to_region=2802001, name=40)
    Event_12800460(1, entity=2801101, move_to_region=2802000, name=74)
    Event_12800620(0, region=2802880, name=108)
    Event_12800620(1, region=2802881, name=146)
    Event_12800700(0, character=2800700)
    Event_12800700(1, character=2800701)
    Event_12800700(2, character=2800702)
    Event_12805500(0, character=2800482, region=2802483, patrol_information_id=2803482, seconds=0.0)
    Event_12805500(1, character=2800483, region=2802483, patrol_information_id=2803483, seconds=0.0)
    Event_12805500(2, character=2800562, region=2802562, patrol_information_id=2803562, seconds=0.0)
    Event_12805500(3, character=2800570, region=2802570, patrol_information_id=2803570, seconds=0.0)
    Event_12805500(4, character=2800571, region=2802570, patrol_information_id=2803571, seconds=0.0)
    Event_12805500(5, character=2800540, region=2802540, patrol_information_id=2803540, seconds=0.0)
    Event_12805500(6, character=2800542, region=2802542, patrol_information_id=2803542, seconds=0.0)
    Event_12805500(7, character=2800543, region=2802543, patrol_information_id=2803543, seconds=0.0)
    Event_12805500(8, character=2800301, region=2802301, patrol_information_id=2803301, seconds=0.0)
    Event_12805500(9, character=2800308, region=2802602, patrol_information_id=2803308, seconds=0.0)
    Event_12805500(10, character=2800309, region=2802602, patrol_information_id=2803309, seconds=0.0)
    Event_12805500(11, character=2800310, region=2802602, patrol_information_id=2803310, seconds=0.0)
    Event_12805500(12, character=2800311, region=2802602, patrol_information_id=2803311, seconds=0.0)
    Event_12805500(13, character=2800312, region=2802602, patrol_information_id=2803312, seconds=0.0)
    Event_12805500(14, character=2800313, region=2802602, patrol_information_id=2803313, seconds=0.0)
    Event_12805500(15, character=2800314, region=2802602, patrol_information_id=2803314, seconds=0.0)
    Event_12805500(16, character=2800315, region=2802602, patrol_information_id=2803315, seconds=0.0)
    Event_12805500(17, character=2800316, region=2802502, patrol_information_id=2803316, seconds=1.0)
    Event_12805500(18, character=2800317, region=2802502, patrol_information_id=2803317, seconds=3.0)
    Event_12805500(19, character=2800404, region=2802507, patrol_information_id=2803404, seconds=0.0)
    Event_12805500(20, character=2800405, region=2802507, patrol_information_id=2803405, seconds=0.0)
    Event_12805500(21, character=2800406, region=2802507, patrol_information_id=2803406, seconds=0.0)
    Event_12805500(22, character=2800407, region=2802507, patrol_information_id=2803407, seconds=0.0)
    Event_12805500(23, character=2800461, region=2802461, patrol_information_id=2803461, seconds=0.0)
    Event_12805600(
        0,
        character=2800400,
        animation_id=7010,
        ai_param_id=261800,
        animation__animation_id=7011,
        ai_param_id_1=261800,
        region=2802400,
        flag=12805042,
        left=1,
    )
    Event_12805600(
        1,
        character=2800401,
        animation_id=7012,
        ai_param_id=261840,
        animation__animation_id=7013,
        ai_param_id_1=261840,
        region=2802400,
        flag=12805042,
        left=1,
    )
    Event_12805600(
        2,
        character=2800402,
        animation_id=7011,
        ai_param_id=261811,
        animation__animation_id=0,
        ai_param_id_1=261811,
        region=2802400,
        flag=12805042,
        left=1,
    )
    Event_12805600(
        3,
        character=2800403,
        animation_id=7012,
        ai_param_id=261810,
        animation__animation_id=7013,
        ai_param_id_1=261810,
        region=2802400,
        flag=12805042,
        left=1,
    )
    Event_12805600(
        4,
        character=2800408,
        animation_id=7010,
        ai_param_id=261800,
        animation__animation_id=7011,
        ai_param_id_1=261800,
        region=0,
        flag=12805042,
        left=0,
    )
    Event_12805600(
        6,
        character=2800410,
        animation_id=7010,
        ai_param_id=261840,
        animation__animation_id=7011,
        ai_param_id_1=261840,
        region=0,
        flag=12805042,
        left=0,
    )
    Event_12805600(
        7,
        character=2800411,
        animation_id=7012,
        ai_param_id=261810,
        animation__animation_id=7013,
        ai_param_id_1=261810,
        region=0,
        flag=12805042,
        left=0,
    )
    Event_12805600(
        10,
        character=2800382,
        animation_id=7010,
        ai_param_id=264801,
        animation__animation_id=7011,
        ai_param_id_1=264800,
        region=0,
        flag=12805042,
        left=0,
    )
    Event_12805600(
        30,
        character=2800318,
        animation_id=0,
        ai_param_id=263851,
        animation__animation_id=3013,
        ai_param_id_1=263850,
        region=0,
        flag=12805040,
        left=1,
    )
    Event_12805600(
        31,
        character=2800305,
        animation_id=0,
        ai_param_id=263851,
        animation__animation_id=3013,
        ai_param_id_1=263850,
        region=0,
        flag=12805040,
        left=1,
    )
    Event_12805650(0, character=2800400, region=2802400, region_1=2802401, command_id=10, flag=12805660)
    Event_12805650(1, character=2800401, region=2802400, region_1=2802402, command_id=10, flag=12805661)
    Event_12805650(2, character=2800402, region=2802400, region_1=2802403, command_id=10, flag=12805662)
    Event_12805650(3, character=2800403, region=2802400, region_1=2802404, command_id=10, flag=12805663)
    Event_12805650(4, character=2800480, region=2802480, region_1=2802481, command_id=10, flag=12805664)
    Event_12805650(6, character=2800329, region=2802329, region_1=2802330, command_id=10, flag=12805666)
    Event_12805660(0, character=2800400, region=2802401)
    Event_12805660(1, character=2800401, region=2802402)
    Event_12805660(2, character=2800402, region=2802403)
    Event_12805660(3, character=2800403, region=2802404)
    Event_12805660(4, character=2800480, region=2802481)
    Event_12805660(6, character=2800329, region=2802330)
    Event_12805670(0, character=2800400, command_id=10, flag=12805660, left=0, radius=0.0)
    Event_12805670(1, character=2800401, command_id=10, flag=12805661, left=0, radius=0.0)
    Event_12805670(2, character=2800402, command_id=10, flag=12805662, left=0, radius=0.0)
    Event_12805670(3, character=2800403, command_id=10, flag=12805663, left=0, radius=0.0)
    Event_12805670(4, character=2800480, command_id=10, flag=12805664, left=0, radius=0.0)
    Event_12805670(6, character=2800329, command_id=10, flag=12805666, left=1, radius=2.0)
    Event_12805680(0, character=2800501, region=2802506, radius=1.0)
    DisableSpawner(entity=2803000)
    DisableSpawner(entity=2803001)
    DisableSpawner(entity=2803002)
    DisableSpawner(entity=2803003)
    DisableSpawner(entity=2803004)
    DisableSpawner(entity=2803005)
    DisableSpawner(entity=2803006)
    DisableSpawner(entity=2803007)
    DisableSpawner(entity=2803008)
    DisableSpawner(entity=2803009)
    DisableSpawner(entity=2803010)
    DisableSpawner(entity=2803011)
    DisableSpawner(entity=2803012)
    DisableSpawner(entity=2803013)
    DisableSpawner(entity=2803014)
    DisableSpawner(entity=2803015)
    DisableSpawner(entity=2803016)
    DisableSpawner(entity=2803017)
    DisableSpawner(entity=2803018)
    DisableSpawner(entity=2803019)
    DisableSpawner(entity=2803020)
    DisableSpawner(entity=2803021)
    DisableSpawner(entity=2803022)
    DisableSpawner(entity=2803023)
    DisableSpawner(entity=2803024)
    DisableSpawner(entity=2803025)
    DisableSpawner(entity=2803026)
    DisableSpawner(entity=2803028)
    DisableSpawner(entity=2803080)
    DisableSpawner(entity=2803082)
    DisableSpawner(entity=2803083)
    DisableSpawner(entity=2803084)
    DisableSpawner(entity=2803100)
    DisableSpawner(entity=2803101)
    DisableSpawner(entity=2803102)
    DisableSpawner(entity=2803103)
    DisableSpawner(entity=2803104)
    DisableSpawner(entity=2803105)
    DisableSpawner(entity=2803106)
    DisableSpawner(entity=2803107)
    DisableSpawner(entity=2803108)
    DisableSpawner(entity=2803110)
    DisableSpawner(entity=2803111)
    DisableSpawner(entity=2803160)
    DisableSpawner(entity=2803161)
    DisableSpawner(entity=2803162)
    DisableSpawner(entity=2803163)
    DisableSpawner(entity=2803180)
    DisableSpawner(entity=2803181)
    DisableSpawner(entity=2803182)
    DisableSpawner(entity=2803183)
    Event_12804500(2, flag=12805030, entity=2803002, flag_1=12805040, character=2800302, left=0, flag_2=0, seconds=0.0)
    Event_12804500(3, flag=12805030, entity=2803003, flag_1=12805040, character=2800303, left=0, flag_2=0, seconds=1.0)
    Event_12804500(1, flag=9802, entity=2803001, flag_1=12805040, character=2800301, left=0, flag_2=0, seconds=0.0)
    Event_12804500(0, flag=9802, entity=2803000, flag_1=12805040, character=2800300, left=0, flag_2=0, seconds=0.0)
    Event_12804500(160, flag=9802, entity=2803160, flag_1=12805040, character=2800460, left=0, flag_2=0, seconds=1.0)
    Event_12804500(4, flag=9802, entity=2803004, flag_1=12805044, character=2800304, left=0, flag_2=0, seconds=1.0)
    Event_12804500(5, flag=9802, entity=2803005, flag_1=12805044, character=2800305, left=0, flag_2=0, seconds=0.0)
    Event_12804500(6, flag=9802, entity=2803006, flag_1=12805044, character=2800306, left=0, flag_2=0, seconds=0.0)
    Event_12804500(7, flag=9802, entity=2803007, flag_1=12805044, character=2800307, left=0, flag_2=0, seconds=1.0)
    Event_12804500(182, flag=9802, entity=2803182, flag_1=12805044, character=2800482, left=0, flag_2=0, seconds=0.0)
    Event_12804500(183, flag=9802, entity=2803183, flag_1=12805044, character=2800483, left=0, flag_2=0, seconds=0.0)
    Event_12804500(8, flag=9802, entity=2803008, flag_1=12805040, character=2800308, left=0, flag_2=0, seconds=0.0)
    Event_12804500(9, flag=9802, entity=2803009, flag_1=12805040, character=2800309, left=0, flag_2=0, seconds=0.0)
    Event_12804500(10, flag=9802, entity=2803010, flag_1=12805040, character=2800310, left=0, flag_2=0, seconds=0.0)
    Event_12804500(11, flag=9802, entity=2803011, flag_1=12805040, character=2800311, left=0, flag_2=0, seconds=0.0)
    Event_12804500(12, flag=9802, entity=2803012, flag_1=12805040, character=2800312, left=0, flag_2=0, seconds=0.0)
    Event_12804500(13, flag=9802, entity=2803013, flag_1=12805040, character=2800313, left=0, flag_2=0, seconds=0.0)
    Event_12804500(14, flag=9802, entity=2803014, flag_1=12805040, character=2800314, left=0, flag_2=0, seconds=0.0)
    Event_12804500(15, flag=9802, entity=2803015, flag_1=12805040, character=2800315, left=0, flag_2=0, seconds=0.0)
    Event_12804500(16, flag=12805031, entity=2803016, flag_1=12805040, character=2800316, left=0, flag_2=0, seconds=0.0)
    Event_12804500(17, flag=12805031, entity=2803017, flag_1=12805040, character=2800317, left=0, flag_2=0, seconds=1.0)
    Event_12804500(18, flag=9802, entity=2803018, flag_1=12805040, character=2800318, left=0, flag_2=0, seconds=0.0)
    Event_12804500(20, flag=12805021, entity=2803020, flag_1=12805041, character=2800320, left=0, flag_2=0, seconds=0.0)
    Event_12804500(21, flag=12805021, entity=2803021, flag_1=12805041, character=2800321, left=0, flag_2=0, seconds=0.5)
    Event_12804500(80, flag=12805021, entity=2803080, flag_1=12805041, character=2800380, left=0, flag_2=0, seconds=1.0)
    Event_12804500(19, flag=12805022, entity=2803019, flag_1=12805041, character=2800319, left=0, flag_2=0, seconds=0.0)
    Event_12804500(
        162,
        flag=12805022,
        entity=2803162,
        flag_1=12805041,
        character=2800462,
        left=0,
        flag_2=0,
        seconds=1.0,
    )
    Event_12804500(100, flag=9802, entity=2803100, flag_1=12805042, character=2800400, left=0, flag_2=0, seconds=0.0)
    Event_12804500(101, flag=9802, entity=2803101, flag_1=12805042, character=2800401, left=0, flag_2=0, seconds=0.0)
    Event_12804500(102, flag=9802, entity=2803102, flag_1=12805042, character=2800402, left=0, flag_2=0, seconds=0.0)
    Event_12804500(103, flag=9802, entity=2803103, flag_1=12805042, character=2800403, left=0, flag_2=0, seconds=0.0)
    Event_12804500(108, flag=9802, entity=2803108, flag_1=12805042, character=2800408, left=0, flag_2=0, seconds=0.0)
    Event_12804500(110, flag=9802, entity=2803110, flag_1=12805042, character=2800410, left=0, flag_2=0, seconds=0.0)
    Event_12804500(111, flag=9802, entity=2803111, flag_1=12805042, character=2800411, left=0, flag_2=0, seconds=0.0)
    Event_12804500(82, flag=9802, entity=2803082, flag_1=12805042, character=2800382, left=0, flag_2=0, seconds=0.0)
    Event_12804500(83, flag=9802, entity=2803083, flag_1=12805042, character=2800383, left=0, flag_2=0, seconds=0.0)
    Event_12804500(161, flag=9802, entity=2803161, flag_1=12805042, character=2800461, left=0, flag_2=0, seconds=0.0)
    Event_12804500(104, flag=9802, entity=2803104, flag_1=12805042, character=2800404, left=0, flag_2=0, seconds=0.0)
    Event_12804500(105, flag=9802, entity=2803105, flag_1=12805042, character=2800405, left=0, flag_2=0, seconds=0.5)
    Event_12804500(106, flag=9802, entity=2803106, flag_1=12805042, character=2800406, left=0, flag_2=0, seconds=1.0)
    Event_12804500(107, flag=9802, entity=2803107, flag_1=12805042, character=2800407, left=0, flag_2=0, seconds=1.5)
    Event_12804500(22, flag=12805023, entity=2803022, flag_1=12805043, character=2800322, left=0, flag_2=0, seconds=0.5)
    Event_12804500(23, flag=12805023, entity=2803023, flag_1=12805043, character=2800323, left=0, flag_2=0, seconds=0.0)
    Event_12804500(84, flag=12805023, entity=2803084, flag_1=12805043, character=2800384, left=0, flag_2=0, seconds=1.0)
    Event_12804500(24, flag=9802, entity=2803024, flag_1=12805043, character=2800324, left=0, flag_2=0, seconds=0.0)
    Event_12804500(25, flag=9802, entity=2803025, flag_1=12805043, character=2800325, left=0, flag_2=0, seconds=0.0)
    Event_12804500(180, flag=9802, entity=2803180, flag_1=12805043, character=2800480, left=0, flag_2=0, seconds=0.0)
    Event_12804500(181, flag=9802, entity=2803181, flag_1=12805043, character=2800481, left=0, flag_2=0, seconds=0.0)
    Event_12804500(26, flag=12805033, entity=2803026, flag_1=12805045, character=2800326, left=0, flag_2=0, seconds=0.0)
    Event_12804500(27, flag=12805033, entity=2803027, flag_1=12805045, character=2800327, left=0, flag_2=0, seconds=0.5)
    Event_12804500(28, flag=12805025, entity=2803028, flag_1=12805045, character=2800328, left=0, flag_2=0, seconds=1.0)
    Event_12805020(0, character=2800500, region=2802504)
    Event_12805020(1, character=2800501, region=2802505)
    Event_12805020(2, character=2800501, region=2802506)
    Event_12805020(3, character=2800503, region=2802509)
    Event_12805020(4, character=2800504, region=2802514)
    Event_12805020(5, character=2800505, region=2802513)
    Event_12805030(0, region=2802500, anchor_entity=2802501, flag=12805030, flag_1=12805040)
    Event_12805030(1, region=2802502, anchor_entity=2802503, flag=12805031, flag_1=12805040)
    Event_12805030(2, region=2802507, anchor_entity=2802508, flag=12805032, flag_1=12805042)
    Event_12805030(3, region=2802511, anchor_entity=2802512, flag=12805033, flag_1=12805045)
    Event_12805040(0, character=2800500)
    Event_12805040(1, character=2800501)
    Event_12805040(2, character=2800502)
    Event_12805040(3, character=2800503)
    Event_12805040(4, character=2800504)
    Event_12805040(5, character=2800505)
    Event_12805700(0, character=2800500, character_1=2800300, left=0, character_2=0)
    Event_12805700(1, character=2800500, character_1=2800301, left=0, character_2=0)
    Event_12805700(2, character=2800500, character_1=2800302, left=0, character_2=0)
    Event_12805700(3, character=2800500, character_1=2800303, left=0, character_2=0)
    Event_12805700(4, character=2800504, character_1=2800304, left=0, character_2=0)
    Event_12805700(5, character=2800504, character_1=2800305, left=0, character_2=0)
    Event_12805700(6, character=2800504, character_1=2800306, left=0, character_2=0)
    Event_12805700(7, character=2800504, character_1=2800307, left=0, character_2=0)
    Event_12805700(8, character=2800500, character_1=2800308, left=0, character_2=0)
    Event_12805700(9, character=2800500, character_1=2800309, left=0, character_2=0)
    Event_12805700(10, character=2800500, character_1=2800310, left=0, character_2=0)
    Event_12805700(11, character=2800500, character_1=2800311, left=0, character_2=0)
    Event_12805700(12, character=2800500, character_1=2800312, left=0, character_2=0)
    Event_12805700(13, character=2800500, character_1=2800313, left=0, character_2=0)
    Event_12805700(14, character=2800500, character_1=2800314, left=0, character_2=0)
    Event_12805700(15, character=2800500, character_1=2800315, left=0, character_2=0)
    Event_12805700(16, character=2800500, character_1=2800316, left=0, character_2=0)
    Event_12805700(17, character=2800500, character_1=2800317, left=0, character_2=0)
    Event_12805700(18, character=2800500, character_1=2800318, left=0, character_2=0)
    Event_12805700(19, character=2800501, character_1=2800319, left=0, character_2=0)
    Event_12805700(20, character=2800501, character_1=2800320, left=0, character_2=0)
    Event_12805700(21, character=2800501, character_1=2800321, left=0, character_2=0)
    Event_12805700(22, character=2800503, character_1=2800322, left=0, character_2=0)
    Event_12805700(23, character=2800503, character_1=2800323, left=0, character_2=0)
    Event_12805700(24, character=2800503, character_1=2800324, left=0, character_2=0)
    Event_12805700(25, character=2800503, character_1=2800325, left=0, character_2=0)
    Event_12805700(26, character=2800505, character_1=2800326, left=0, character_2=0)
    Event_12805700(27, character=2800505, character_1=2800327, left=0, character_2=0)
    Event_12805700(28, character=2800505, character_1=2800328, left=0, character_2=0)
    Event_12805700(80, character=2800501, character_1=2800380, left=0, character_2=0)
    Event_12805700(82, character=2800502, character_1=2800382, left=0, character_2=0)
    Event_12805700(83, character=2800502, character_1=2800383, left=0, character_2=0)
    Event_12805700(84, character=2800503, character_1=2800384, left=0, character_2=0)
    Event_12805700(100, character=2800502, character_1=2800400, left=0, character_2=0)
    Event_12805700(101, character=2800502, character_1=2800401, left=0, character_2=0)
    Event_12805700(102, character=2800502, character_1=2800402, left=0, character_2=0)
    Event_12805700(103, character=2800502, character_1=2800403, left=0, character_2=0)
    Event_12805700(104, character=2800502, character_1=2800404, left=0, character_2=0)
    Event_12805700(105, character=2800502, character_1=2800405, left=0, character_2=0)
    Event_12805700(106, character=2800502, character_1=2800406, left=0, character_2=0)
    Event_12805700(107, character=2800502, character_1=2800407, left=0, character_2=0)
    Event_12805700(108, character=2800502, character_1=2800408, left=0, character_2=0)
    Event_12805700(110, character=2800502, character_1=2800410, left=0, character_2=0)
    Event_12805700(111, character=2800502, character_1=2800411, left=0, character_2=0)
    Event_12805700(160, character=2800500, character_1=2800460, left=0, character_2=0)
    Event_12805700(161, character=2800502, character_1=2800461, left=0, character_2=0)
    Event_12805700(162, character=2800501, character_1=2800462, left=0, character_2=0)
    Event_12805700(180, character=2800503, character_1=2800480, left=0, character_2=0)
    Event_12805700(181, character=2800503, character_1=2800481, left=0, character_2=0)
    Event_12805700(182, character=2800504, character_1=2800482, left=0, character_2=0)
    Event_12805700(183, character=2800504, character_1=2800483, left=0, character_2=0)
    Event_12804000(0, character=2800300)
    Event_12804000(1, character=2800301)
    Event_12804000(2, character=2800302)
    Event_12804000(3, character=2800303)
    Event_12804000(4, character=2800304)
    Event_12804000(5, character=2800305)
    Event_12804000(6, character=2800306)
    Event_12804000(7, character=2800307)
    Event_12804000(8, character=2800308)
    Event_12804000(9, character=2800309)
    Event_12804000(10, character=2800310)
    Event_12804000(11, character=2800311)
    Event_12804000(12, character=2800312)
    Event_12804000(13, character=2800313)
    Event_12804000(14, character=2800314)
    Event_12804000(15, character=2800315)
    Event_12804000(16, character=2800316)
    Event_12804000(17, character=2800317)
    Event_12804000(18, character=2800318)
    Event_12804000(19, character=2800319)
    Event_12804000(20, character=2800320)
    Event_12804000(21, character=2800321)
    Event_12804000(22, character=2800322)
    Event_12804000(23, character=2800323)
    Event_12804000(24, character=2800324)
    Event_12804000(25, character=2800325)
    Event_12804000(26, character=2800326)
    Event_12804000(27, character=2800327)
    Event_12804000(28, character=2800328)
    Event_12804000(80, character=2800380)
    Event_12804000(82, character=2800382)
    Event_12804000(83, character=2800383)
    Event_12804000(84, character=2800384)
    Event_12804000(100, character=2800400)
    Event_12804000(101, character=2800401)
    Event_12804000(102, character=2800402)
    Event_12804000(103, character=2800403)
    Event_12804000(104, character=2800404)
    Event_12804000(105, character=2800405)
    Event_12804000(106, character=2800406)
    Event_12804000(107, character=2800407)
    Event_12804000(108, character=2800408)
    Event_12804000(110, character=2800410)
    Event_12804000(111, character=2800411)
    Event_12804000(160, character=2800460)
    Event_12804000(161, character=2800461)
    Event_12804000(162, character=2800462)
    Event_12804000(180, character=2800480)
    Event_12804000(181, character=2800481)
    Event_12804000(182, character=2800482)
    Event_12804000(183, character=2800483)
    Event_12805918()
    Event_12805900(0, character=2800562)
    Event_12805900(1, character=2800563)
    Event_12805900(2, character=2800564)
    Event_12805900(4, character=2800566)
    Event_12805900(5, character=2800567)
    Event_12805900(7, character=2800569)
    Event_12805900(8, character=2800570)
    Event_12805900(9, character=2800571)
    Event_12805900(10, character=2800572)
    Event_12805900(11, character=2800573)
    Event_12805920(0, obj=2801600, flag=12805942)
    Event_12805920(1, obj=2801601, flag=12805947)
    Event_12805920(2, obj=2801602, flag=12805952)
    Event_12805920(3, obj=2801603, flag=12805957)
    Event_12805930(0, flag=12805940, flag_1=12805942, other_entity=2801600)
    Event_12805930(1, flag=12805945, flag_1=12805947, other_entity=2801601)
    Event_12805930(2, flag=12805950, flag_1=12805952, other_entity=2801602)
    Event_12805930(3, flag=12805955, flag_1=12805957, other_entity=2801603)
    Event_12805050()
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    Event_12800608()
    Event_12805460(
        4,
        character=2800104,
        animation_id=7012,
        animation_id_1=7013,
        radius=2.0,
        ai_param_id=263899,
        ai_param_id_1=263890,
    )
    Event_12805460(
        5,
        character=2800105,
        animation_id=7014,
        animation_id_1=7015,
        radius=2.0,
        ai_param_id=263899,
        ai_param_id_1=263890,
    )
    Event_12805460(
        6,
        character=2800106,
        animation_id=7010,
        animation_id_1=7011,
        radius=2.0,
        ai_param_id=263899,
        ai_param_id_1=263890,
    )
    Event_12805460(
        7,
        character=2800107,
        animation_id=7012,
        animation_id_1=7013,
        radius=2.0,
        ai_param_id=263899,
        ai_param_id_1=263890,
    )
    Event_12805460(
        8,
        character=2800108,
        animation_id=7014,
        animation_id_1=7015,
        radius=2.0,
        ai_param_id=263899,
        ai_param_id_1=263890,
    )
    Event_12805460(
        9,
        character=2800109,
        animation_id=7010,
        animation_id_1=7011,
        radius=2.0,
        ai_param_id=263899,
        ai_param_id_1=263890,
    )
    Event_12805500(30, character=2800160, region=2802160, patrol_information_id=2803160, seconds=0.0)
    Event_12805500(31, character=2800140, region=2802140, patrol_information_id=2803140, seconds=0.0)
    Event_12805500(32, character=2800141, region=2802140, patrol_information_id=2803141, seconds=0.0)
    Event_12805500(33, character=2800200, region=2802200, patrol_information_id=2803200, seconds=0.0)
    Event_12805550(6, character=2800608, region=2802608, radius=8.0)
    Event_12805650(6, character=2800160, region=2802160, region_1=2802161, command_id=10, flag=12805666)
    Event_12805660(6, character=2800160, region=2802161)
    Event_12805670(6, character=2800160, command_id=10, flag=12805666, left=0, radius=0.0)

    # --- Label 5 --- #
    DefineLabel(5)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableAnimations(2800740)
    DisableGravity(2800740)
    DisableCharacterCollision(2800740)
    SetNetworkUpdateRate(2800740, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800741)
    DisableGravity(2800741)
    DisableCharacterCollision(2800741)
    SetNetworkUpdateRate(2800741, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800742)
    DisableGravity(2800742)
    DisableCharacterCollision(2800742)
    SetNetworkUpdateRate(2800742, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800743)
    DisableGravity(2800743)
    DisableCharacterCollision(2800743)
    SetNetworkUpdateRate(2800743, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800744)
    DisableGravity(2800744)
    DisableCharacterCollision(2800744)
    SetNetworkUpdateRate(2800744, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableAnimations(2800745)
    DisableGravity(2800745)
    DisableCharacterCollision(2800745)
    SetNetworkUpdateRate(2800745, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetDisplayMask(2800745, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2800745, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2800745, bit_index=10, switch_type=OnOffChange.On)
    DisableAnimations(2800990)
    DisableGravity(2800990)
    DisableCharacterCollision(2800990)
    SetNetworkUpdateRate(2800990, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetBackreadStateAlternate(2800990, True)
    DisableAnimations(2800991)
    DisableGravity(2800991)
    DisableCharacterCollision(2800991)
    SetNetworkUpdateRate(2800991, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetBackreadStateAlternate(2800991, True)
    Event_12800911()


@RestartOnRest(12804500)
def Event_12804500(_, flag: int, entity: int, flag_1: int, character: int, left: int, flag_2: int, seconds: float):
    """Event 12804500"""
    GotoIfFlagEnabled(Label.L1, flag=flag_1)
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(flag))
    
    Wait(seconds)
    EnableCharacter(character)
    ForceAnimation(character, 6200, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableSpawner(entity=entity)
    AND_1.Add(FlagEnabled(flag_1))
    if ValueNotEqual(left=left, right=0):
        AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableSpawner(entity=entity)


@RestartOnRest(12805020)
def Event_12805020(_, character: int, region: int):
    """Event 12805020"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, 3010)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=30))
    
    Wait(0.0)


@RestartOnRest(12805030)
def Event_12805030(_, region: int, anchor_entity: int, flag: int, flag_1: int):
    """Event 12805030"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(AND_1)
    
    PlaySoundEffect(anchor_entity, 105006003, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=20)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    EnableFlag(flag)
    WaitFrames(frames=13)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=9)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=7)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=11)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=7)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=9)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=6)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=9)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=8)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)
    WaitFrames(frames=11)
    PlaySoundEffect(anchor_entity, 105006102, sound_type=SoundType.c_CharacterMotion)


@RestartOnRest(12805040)
def Event_12805040(_, character: int):
    """Event 12805040"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(character))
    
    Wait(0.0)


@RestartOnRest(12805050)
def Event_12805050():
    """Event 12805050"""
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2800563)
    
    MAIN.Await(CharacterBackreadEnabled(2800563))
    
    Move(2800563, destination=2802564, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2800563, 7005, loop=True)
    ForceAnimation(2801965, 1, loop=True)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2802563))
    
    MAIN.Await(AND_1)
    
    Move(2800563, destination=2802564, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2800563, 7006)
    ForceAnimation(2801965, 2, wait_for_completion=True)
    EnableAI(2800563)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2801965, 3, loop=True)
    SetNest(2800563, region=2802565)


@ContinueOnRest(12805140)
def Event_12805140(_, character: int, region: int, radius: float):
    """Event 12805140"""
    DisableAI(character)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    ReplanAI(character)


@ContinueOnRest(12805160)
def Event_12805160(_, character: int, region: int, radius: float):
    """Event 12805160"""
    DisableAI(character)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    ReplanAI(character)


@RestartOnRest(12805180)
def Event_12805180(_, character: int, region: int):
    """Event 12805180"""
    DisableAI(character)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=4.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    ReplanAI(character)


@RestartOnRest(12805460)
def Event_12805460(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    ai_param_id: int,
    ai_param_id_1: int,
):
    """Event 12805460"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    DisableGravity(character)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    EnableGravity(character)
    ForceAnimation(character, animation_id_1)


@RestartOnRest(12805470)
def Event_12805470(
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
    """Event 12805470"""
    MAIN.Await(FlagEnabled(flag))
    
    AND_1.Add(CharacterPartHealth(character, npc_part_id=npc_part_id_1) <= 0)
    AND_2.Add(HealthRatio(character) <= 0.0)
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    if FlagDisabled(flag):
        SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=1, overwrite_max=False)
        Restart()
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=999999)
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


@RestartOnRest(12805480)
def Event_12805480(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    flag: int,
    character: int,
):
    """Event 12805480"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    EnableFlag(flag)


@RestartOnRest(12805490)
def Event_12805490(_, tae_event_id: int, tae_event_id_1: int, flag: int, character: int):
    """Event 12805490"""
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=tae_event_id))
    
    EnableFlag(flag)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=tae_event_id_1))
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(12805500)
def Event_12805500(_, character: int, region: int, patrol_information_id: int, seconds: float):
    """Event 12805500"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(seconds)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    ReplanAI(character)
    
    MAIN.Await(CharacterDead(character))
    
    MAIN.Await(CharacterAlive(character))
    
    Restart()


@RestartOnRest(12805550)
def Event_12805550(_, character: int, region: int, radius: float):
    """Event 12805550"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableAI(character)


@RestartOnRest(12805570)
def Event_12805570(_, character: int, region: int, region_1: int):
    """Event 12805570"""
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    DisableAI(character)
    Move(character, destination=region, destination_type=CoordEntityType.Region, short_move=True)
    Wait(15.0)
    EnableAI(character)
    
    MAIN.Await(CharacterInsideRegion(character, region=region_1))
    
    DisableAI(character)
    Move(character, destination=region_1, destination_type=CoordEntityType.Region, short_move=True)
    Wait(15.0)
    EnableAI(character)
    Restart()


@RestartOnRest(12805600)
def Event_12805600(
    _,
    character: int,
    animation_id: int,
    ai_param_id: int,
    animation__animation_id: int,
    ai_param_id_1: int,
    region: int,
    flag: int,
    left: int,
):
    """Event 12805600"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(AND_1)
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)
    if ValueNotEqual(left=left, right=1):
        ForceAnimation(character, animation__animation_id)
    else:
        RotateToFaceEntity(character, PLAYER, animation=animation__animation_id)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 0)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(12805650)
def Event_12805650(_, character: int, region: int, region_1: int, command_id: int, flag: int):
    """Event 12805650"""
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


@RestartOnRest(12805660)
def Event_12805660(_, character: int, region: int):
    """Event 12805660"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterInsideRegion(character, region=region))

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12805670)
def Event_12805670(_, character: int, command_id: int, flag: int, left: int, radius: float):
    """Event 12805670"""
    if FlagEnabled(flag):
        return
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=left, right=1)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(flag))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    AND_3.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    AND_4.Add(FlagEnabled(flag))
    OR_3.Add(AND_3)
    OR_3.Add(AND_4)
    
    MAIN.Await(OR_3)
    
    EndIfFinishedConditionTrue(input_condition=AND_4)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12805680)
def Event_12805680(_, character: int, region: int, radius: float):
    """Event 12805680"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_2)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    EnableAI(character)


@RestartOnRest(12805700)
def Event_12805700(_, character: int, character_1: int, left: int, character_2: int):
    """Event 12805700"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    AddSpecialEffect(character_1, 4672)
    RemoveSpecialEffect(character_1, 4671)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfValueComparison(Label.L1, comparison_type=ComparisonType.Equal, left=left, right=1)
    
    MAIN.Await(CharacterDead(character))
    
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    AddSpecialEffect(character_1, 4672)
    RemoveSpecialEffect(character_1, 4671)
    WaitFrames(frames=1)
    ForceAnimation(character_1, 7025, wait_for_completion=True)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(CharacterDead(character))
    AND_2.Add(CharacterDead(character_2))
    
    MAIN.Await(AND_2)
    
    WaitRandomSeconds(min_seconds=0.0, max_seconds=1.0)
    AddSpecialEffect(character_1, 4672)
    RemoveSpecialEffect(character_1, 4671)
    WaitFrames(frames=1)
    ForceAnimation(character_1, 7025, wait_for_completion=True)

    # --- Label 2 --- #
    DefineLabel(2)
    
    MAIN.Await(CharacterDead(character_1))
    
    MAIN.Await(CharacterAlive(character_1))
    
    Restart()


@RestartOnRest(12805900)
def Event_12805900(_, character: int):
    """Event 12805900"""
    MAIN.Await(CharacterHasSpecialEffect(character, 5510))
    
    WaitFrames(frames=1)
    ResetAnimation(character)
    ForceAnimation(character, 7010)
    AddSpecialEffect(character, 5511)
    Wait(1.899999976158142)
    ReplanAI(character)


@RestartOnRest(12805918)
def Event_12805918():
    """Event 12805918"""
    SetTeamType(2800560, TeamType.Boss)
    CreateProjectileOwner(entity=2800560)


@RestartOnRest(12805920)
def Event_12805920(_, obj: int, flag: int):
    """Event 12805920"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DeleteObjectVFX(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    if ThisEventSlotFlagDisabled():
        CreateObjectVFX(obj, vfx_id=100, dummy_id=928020)
    ShootProjectile(
        owner_entity=2800560,
        source_entity=obj,
        dummy_id=100,
        behavior_id=6032,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(2.0)
    Restart()


@RestartOnRest(12805930)
def Event_12805930(_, flag: int, flag_1: int, other_entity: int):
    """Event 12805930"""
    if FlagEnabled(flag_1):
        return
    OR_1.Add(CharacterHasSpecialEffect(PLAYER, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800562, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800563, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800564, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800566, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800567, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800569, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800570, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800571, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800572, 5510))
    OR_1.Add(CharacterHasSpecialEffect(2800573, 5510))
    AND_1.Add(OR_1)
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800562, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800563, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800564, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800566, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800567, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800569, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800570, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800571, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800572, other_entity=other_entity, radius=2.0))
    OR_2.Add(EntityWithinDistance(entity=2800573, other_entity=other_entity, radius=2.0))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    IncrementEventValue(flag, bit_count=2, max_value=3)
    AND_1.Add(EventValue(flag=flag, bit_count=2) == 3)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(flag_1)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(12804000)
def Event_12804000(_, character: int):
    """Event 12804000"""
    DisableNetworkSync()
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    RemoveSpecialEffect(character, 4673)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    Wait(1.0)
    AddSpecialEffect(character, 5560)
    
    MAIN.Await(CharacterAlive(character))
    
    AddSpecialEffect(character, 5025)
    Restart()


@ContinueOnRest(12800100)
def Event_12800100(_, obj: int, obj_act_id: int):
    """Event 12800100"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=-1)
        EnableTreasure(obj=obj)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@ContinueOnRest(12800120)
def Event_12800120(_, entity: int, action_button_id: int, text: int):
    """Event 12800120"""
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    DisplayDialog(text=text, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12800140)
def Event_12800140():
    """Event 12800140"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    AND_1.Add(FlagEnabled(13201803))
    AND_1.Add(FramesElapsed(frames=55))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13207850)
    DisplayDialog(text=10012014, number_buttons=NumberButtons.OneButton)


@ContinueOnRest(12800160)
def Event_12800160():
    """Event 12800160"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(9802))
    AND_1.Add(InsideMap(game_map=YAHARGUL))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(PLAYER, 9120)
    AddSpecialEffect(PLAYER, 9121)
    AND_2.Add(FlagDisabled(9802))
    AND_2.Add(InsideMap(game_map=YAHARGUL))
    
    MAIN.Await(not AND_2)
    
    RemoveSpecialEffect(PLAYER, 9120)
    RemoveSpecialEffect(PLAYER, 9121)
    Restart()


@RestartOnRest(12800400)
def Event_12800400():
    """Event 12800400"""
    EnableFlag(2800)
    GotoIfFlagEnabled(Label.L2, flag=9802)
    GotoIfFlagEnabled(Label.L1, flag=9801)
    GotoIfFlagEnabled(Label.L0, flag=9800)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2804000)
    DisableMapPiece(map_piece_id=2804001)
    DisableMapPiece(map_piece_id=2804002)
    DisableObject(2801000)
    DeleteVFX(2803910, erase_root_only=False)
    DeleteVFX(2803911, erase_root_only=False)
    Goto(Label.L4)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableMapPiece(map_piece_id=2804000)
    EnableMapPiece(map_piece_id=2804001)
    DisableMapPiece(map_piece_id=2804002)
    DeleteVFX(2803911, erase_root_only=False)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableObject(2801000)
    DisableObject(2801052)
    DisableObject(2801140)
    DisableObject(2801141)
    DisableObject(2801142)
    DisableObject(2801143)
    DisableObject(2801144)
    DisableObject(2801145)
    DisableCharacter(2800740)
    DisableCharacter(2800741)
    DisableCharacter(2800742)
    DisableCharacter(2800743)
    DisableCharacter(2800744)
    DisableBackread(2800700)
    DisableBackread(2800701)
    DisableBackread(2800702)
    DisableBackread(2800500)
    DisableBackread(2800501)
    DisableBackread(2800502)
    DisableBackread(2800503)
    DisableBackread(2800504)
    DisableBackread(2800505)
    DisableBackread(2800480)
    DisableBackread(2800481)
    DisableBackread(2800482)
    DisableBackread(2800483)
    DisableBackread(2800400)
    DisableBackread(2800401)
    DisableBackread(2800402)
    DisableBackread(2800403)
    DisableBackread(2800404)
    DisableBackread(2800405)
    DisableBackread(2800406)
    DisableBackread(2800407)
    DisableBackread(2800408)
    DisableBackread(2800410)
    DisableBackread(2800411)
    DisableBackread(2800460)
    DisableBackread(2800461)
    DisableBackread(2800462)
    DisableBackread(2800300)
    DisableBackread(2800301)
    DisableBackread(2800302)
    DisableBackread(2800303)
    DisableBackread(2800304)
    DisableBackread(2800305)
    DisableBackread(2800306)
    DisableBackread(2800307)
    DisableBackread(2800308)
    DisableBackread(2800309)
    DisableBackread(2800310)
    DisableBackread(2800311)
    DisableBackread(2800312)
    DisableBackread(2800313)
    DisableBackread(2800314)
    DisableBackread(2800315)
    DisableBackread(2800316)
    DisableBackread(2800317)
    DisableBackread(2800318)
    DisableBackread(2800319)
    DisableBackread(2800320)
    DisableBackread(2800321)
    DisableBackread(2800322)
    DisableBackread(2800323)
    DisableBackread(2800324)
    DisableBackread(2800325)
    DisableBackread(2800326)
    DisableBackread(2800327)
    DisableBackread(2800328)
    DisableBackread(2800329)
    DisableBackread(2800380)
    DisableBackread(2800382)
    DisableBackread(2800383)
    DisableBackread(2800384)
    DisableBackread(2800560)
    DisableBackread(2800562)
    DisableBackread(2800563)
    DisableBackread(2800564)
    DisableBackread(2800566)
    DisableBackread(2800567)
    DisableBackread(2800569)
    DisableBackread(2800570)
    DisableBackread(2800571)
    DisableBackread(2800572)
    DisableBackread(2800573)
    DisableBackread(2800540)
    DisableBackread(2800541)
    DisableBackread(2800542)
    DisableBackread(2800543)
    DisableBackread(2800544)
    DisableBackread(2800721)
    DisableBackread(2800722)
    DisableObject(2801600)
    DisableObject(2801601)
    DisableObject(2801602)
    DisableObject(2801603)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(12801800):
        EnableFlag(2800)
    else:
        DisableFlag(2800)
    DisableMapPiece(map_piece_id=2804000)
    DisableMapPiece(map_piece_id=2804001)
    EnableMapPiece(map_piece_id=2804002)
    EnableObject(2801000)
    DeleteVFX(2803910, erase_root_only=False)
    EnableObject(2801052)
    DisableObject(2801952)
    DisableCharacter(2800952)
    DisableCharacter(2803952)
    EnableFlag(70002802)
    EnableTreasure(obj=2801140)
    EnableTreasure(obj=2801141)
    EnableTreasure(obj=2801142)
    EnableTreasure(obj=2801143)
    EnableTreasure(obj=2801144)
    EnableTreasure(obj=2801145)
    DisableBackread(2800140)
    DisableBackread(2800141)
    DisableBackread(2800142)
    DisableBackread(2800143)
    DisableBackread(2800144)
    DisableBackread(2800145)
    DisableBackread(2800160)
    DisableBackread(2800161)
    DisableBackread(2800162)
    DisableBackread(2800163)
    DisableBackread(2800104)
    DisableBackread(2800105)
    DisableBackread(2800106)
    DisableBackread(2800107)
    DisableBackread(2800108)
    DisableBackread(2800109)
    DisableBackread(2800180)
    DisableBackread(2800181)
    DisableBackread(2800182)
    DisableBackread(2800183)
    DisableBackread(2800184)
    DisableBackread(2800185)
    DisableBackread(2800186)
    DisableBackread(2800187)
    DisableBackread(2800188)
    DisableBackread(2800189)
    DisableBackread(2800190)
    DisableBackread(2800191)
    DisableBackread(2800200)
    DisableBackread(2800201)
    DisableBackread(2800720)
    DisableBackread(2800723)

    # --- Label 3 --- #
    DefineLabel(3)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9800))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9801))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9802))
    
    MAIN.Await(OR_1)
    
    Restart()


@ContinueOnRest(12800401)
def Event_12800401():
    """Event 12800401"""
    OR_1.Add(FlagEnabled(9802))
    OR_1.Add(PlayerInsightAmount() >= 40)
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    SetDisplayMask(2800745, bit_index=0, switch_type=OnOffChange.On)
    SetDisplayMask(2800745, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(2800745, bit_index=10, switch_type=OnOffChange.On)
    AddSpecialEffect(2800745, 5686)
    EnableFlag(12800435)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetDisplayMask(2800745, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2800745, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2800745, bit_index=10, switch_type=OnOffChange.Off)
    DisableFlag(12800435)


@RestartOnRest(12800402)
def Event_12800402():
    """Event 12800402"""
    GotoIfFlagDisabled(Label.L0, flag=9802)
    EndOfAnimation(obj=2801300, animation_id=1)
    NotifyDoorEventSoundDampening(obj=2801300, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2800000, entity=2801300))
    
    DisplayDialog(text=10010171, anchor_entity=2801300, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12800403)
def Event_12800403():
    """Event 12800403"""
    GotoIfFlagDisabled(Label.L0, flag=9802)
    EndOfAnimation(obj=2801150, animation_id=1)
    NotifyDoorEventSoundDampening(obj=2801150, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2800001, entity=2801150))
    
    DisplayDialog(text=10010171, anchor_entity=2801150, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12800430)
def Event_12800430():
    """Event 12800430"""
    if Client():
        return
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2800020, entity=2801500))
    
    Move(PLAYER, destination=2801500, destination_type=CoordEntityType.Object, dummy_id=220, short_move=True)
    ForceAnimation(PLAYER, 101169)
    WaitFrames(frames=180)
    WarpPlayerToRespawnPoint(3202959)


@ContinueOnRest(12800431)
def Event_12800431():
    """Event 12800431"""
    AND_1.Add(CharacterHasTAEEvent(2800745, tae_event_id=10))
    AND_1.Add(PlayerHasGood(4310))
    
    MAIN.Await(AND_1)
    
    EnableImmortality(PLAYER)
    WaitFrames(frames=30)
    EnableFlag(9180)
    WaitFrames(frames=1)
    GotoIfMultiplayer(Label.L0)
    SkipLinesIfPlayerGender(skip_lines=2, gender=Gender.Male)
    PlayCutscene(28000040, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(28001040, cutscene_flags=0, player_id=10000)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfPlayerGender(skip_lines=2, gender=Gender.Male)
    PlayCutscene(28000040, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    SkipLines(1)
    PlayCutscene(28001040, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableFlag(12800434)
    WarpPlayerToRespawnPoint(3202958)


@RestartOnRest(12800432)
def Event_12800432():
    """Event 12800432"""
    AND_1.Add(FlagEnabled(12800435))
    AND_1.Add(CharacterHasTAEEvent(2800745, tae_event_id=20))
    
    MAIN.Await(AND_1)
    
    SetDisplayMask(2800745, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2800745, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2800745, bit_index=10, switch_type=OnOffChange.Off)
    AddSpecialEffect(2800745, 5687)
    RemoveSpecialEffect(2800745, 5686)
    AND_2.Add(CharacterHasTAEEvent(2800745, tae_event_id=30))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(2800745, 5686)
    RemoveSpecialEffect(2800745, 5687)
    Restart()


@RestartOnRest(12800433)
def Event_12800433(_, character: int):
    """Event 12800433"""
    DisableNetworkSync()
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=700))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 5577))
    
    MAIN.Await(AND_1)
    
    DisplayBanner(BannerType.YouLose)
    Restart()


@ContinueOnRest(12800435)
def Event_12800435():
    """Event 12800435"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=2803600)
    AND_1.Add(FlagDisabled(9802))
    AND_1.Add(InsideMap(game_map=YAHARGUL))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=2802650))
    
    MAIN.Await(AND_1)
    
    EnableSoundEvent(sound_id=2803600)
    OR_1.Add(FlagEnabled(9802))
    OR_1.Add(OutsideMap(game_map=YAHARGUL))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=2802650))
    
    MAIN.Await(OR_1)
    
    DisableSoundEvent(sound_id=2803600)
    Restart()


@ContinueOnRest(12800436)
def Event_12800436():
    """Event 12800436"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2802020))
    AND_1.Add(FlagDisabled(9802))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=2803600)
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2802021))
    AND_2.Add(FlagDisabled(9802))
    
    MAIN.Await(AND_2)
    
    EnableSoundEvent(sound_id=2803600)
    Restart()


@ContinueOnRest(12800460)
def Event_12800460(_, entity: int, move_to_region: int, name: int):
    """Event 12800460"""
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2800030, entity=entity))
    
    CreatePlayLog(name=name)
    ForceAnimation(PLAYER, 101167)
    WaitFrames(frames=150)
    PlayCutsceneAndMovePlayer_Dummy(move_to_region=move_to_region, game_map=YAHARGUL)
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 101168)
    WaitFrames(frames=120)
    Restart()


@ContinueOnRest(12800470)
def Event_12800470(_, entity: int, animation_id: int):
    """Event 12800470"""
    ForceAnimation(entity, animation_id, loop=True)
    
    MAIN.Await(FlagEnabled(0))
    
    Wait(10.0)


@ContinueOnRest(12800480)
def Event_12800480(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 12800480"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    Wait(0.0)


@ContinueOnRest(12800490)
def Event_12800490(_, action_button_id: int, anchor_entity: int, flag: int):
    """Event 12800490"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=anchor_entity))
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    DisplayDialog(text=10010161, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)


@RestartOnRest(12800500)
def Event_12800500(_, character: int, flag: int):
    """Event 12800500"""
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


@ContinueOnRest(12800600)
def Event_12800600(_, flag: int, flag_1: int, flag_2: int, flag_3: int, obj: int, obj_1: int, obj_2: int):
    """Event 12800600"""
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    EndOfAnimation(obj=obj, animation_id=3)
    DisableObjectActivation(obj_1, obj_act_id=100)
    DisableObjectActivation(obj_2, obj_act_id=100)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_1))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    DisableFlag(flag_2)
    EndOfAnimation(obj=obj, animation_id=3)
    EnableObjectActivation(obj_1, obj_act_id=100)
    DisableObjectActivation(obj_2, obj_act_id=100)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_2)
    EndOfAnimation(obj=obj, animation_id=13)
    DisableObjectActivation(obj_1, obj_act_id=100)
    EnableObjectActivation(obj_2, obj_act_id=100)

    # --- Label 2 --- #
    DefineLabel(2)
    End()
    DisableFlag(flag)


@ContinueOnRest(12800601)
def Event_12800601(_, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12800601"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(flag_3))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(FlagEnabled(flag_1))
    SkipLinesIfConditionTrue(2, AND_2)
    DisableFlag(flag_2)
    SkipLines(1)
    EnableFlag(flag_2)
    AND_3.Add(CharacterHuman(PLAYER))
    AND_3.Add(FlagEnabled(flag_3))
    AND_3.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_3)
    
    Restart()


@ContinueOnRest(12800602)
def Event_12800602(_, flag: int, flag_1: int, flag_2: int, flag_3: int, region: int, obj_act_id: int):
    """Event 12800602"""
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(FlagEnabled(flag_1))
    GotoIfConditionFalse(Label.L0, input_condition=AND_3)
    EndOfAnimation(obj=2801400, animation_id=12)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_3))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    AND_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    AND_2.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    ForceAnimation(2801400, 11, wait_for_completion=True)
    ForceAnimation(2801400, 12, wait_for_completion=True)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2802101))
    
    ForceAnimation(2801400, 13, wait_for_completion=True)
    DisableObjectActivation(2801401, obj_act_id=100)
    EnableObjectActivation(2801402, obj_act_id=100)
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12800604)
def Event_12800604(_, flag: int, flag_1: int, flag_2: int, flag_3: int, region: int, obj_act_id: int):
    """Event 12800604"""
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(FlagDisabled(flag_1))
    GotoIfConditionFalse(Label.L0, input_condition=AND_3)
    EndOfAnimation(obj=2801400, animation_id=2)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_3))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(ObjectActivated(obj_act_id=obj_act_id))
    AND_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    AND_2.Add(FlagDisabled(flag_2))
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    DisableFlag(flag_1)
    ForceAnimation(2801400, 1, wait_for_completion=True)
    ForceAnimation(2801400, 2, wait_for_completion=True)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2802102))
    
    ForceAnimation(2801400, 3, wait_for_completion=True)
    EnableObjectActivation(2801401, obj_act_id=100)
    DisableObjectActivation(2801402, obj_act_id=100)
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12800606)
def Event_12800606(_, flag: int, flag_1: int, flag_2: int, entity: int, entity_1: int):
    """Event 12800606"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=entity))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(ActionButtonParamActivated(action_button_id=7100, entity=entity_1))
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(ActionButtonParamActivated(action_button_id=7100, entity=entity))
    AND_4.Add(FlagEnabled(flag))
    AND_4.Add(ActionButtonParamActivated(action_button_id=7100, entity=entity_1))
    AND_5.Add(FlagEnabled(flag_1))
    AND_5.Add(ActionButtonParamActivated(action_button_id=7100, entity=entity))
    AND_6.Add(FlagDisabled(flag_1))
    AND_6.Add(ActionButtonParamActivated(action_button_id=7100, entity=entity_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    OR_1.Add(AND_5)
    OR_1.Add(AND_6)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12800607)
def Event_12800607(_, flag: int, region: int, obj: int, obj_1: int):
    """Event 12800607"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    EnableObjectActivation(obj, obj_act_id=100)
    DisableObjectActivation(obj_1, obj_act_id=100)
    EnableFlag(flag)


@ContinueOnRest(12800608)
def Event_12800608():
    """Event 12800608"""
    EndOfAnimation(obj=2801400, animation_id=0)
    DisableObjectActivation(2801401, obj_act_id=100)
    DisableObjectActivation(2801402, obj_act_id=100)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=7100, entity=2801402))
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12800620)
def Event_12800620(_, region: int, name: int):
    """Event 12800620"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    CreatePlayLog(name=name)


@ContinueOnRest(12800700)
def Event_12800700(_, character: int):
    """Event 12800700"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    Wait(0.0)


@RestartOnRest(12800999)
def Event_12800999():
    """Event 12800999"""
    DisableCharacter(2800509)
    SetBackreadStateAlternate(2800509, True)


@ContinueOnRest(12801800)
def Event_12801800():
    """Event 12801800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2803802)
    DisableSoundEvent(sound_id=2803803)
    DisableSoundEvent(sound_id=2803804)
    DisableCharacter(2800800)
    DisableCharacter(2800801)
    DisableCharacter(2800802)
    DisableCharacter(2800803)
    Kill(2800800)
    Kill(2800801)
    Kill(2800802)
    Kill(2800803)
    DisableBackread(2800520)
    DisableBackread(2800522)
    DisableBackread(2800524)
    DisableBackread(2800525)
    DisableBackread(2800527)
    DisableBackread(2800529)
    DisableObject(2801800)
    DisableObject(2801801)
    DeleteVFX(2803800, erase_root_only=False)
    DeleteVFX(2803801, erase_root_only=False)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthRatio(2800803) <= 0.0)
    
    ResetAnimation(2800800, disable_interpolation=True)
    ResetAnimation(2800801, disable_interpolation=True)
    Kill(2800800)
    Kill(2800801)
    
    MAIN.Await(CharacterDead(2800800))
    
    Kill(2800520, award_souls=True)
    Kill(2800522, award_souls=True)
    Kill(2800524, award_souls=True)
    Kill(2800525, award_souls=True)
    Kill(2800527, award_souls=True)
    Kill(2800529, award_souls=True)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2801800)
    DisableObject(2801801)
    DeleteVFX(2803800)
    DeleteVFX(2803801)
    SetLockedCameraSlot(game_map=YAHARGUL, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2800803)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(achievement_id=18)
    AwardItemLot(50700000, host_only=False)
    EnableFlag(2800)
    EnableFlag(9464)
    CreatePlayLog(name=186)
    StopPlayLogMeasurement(measurement_id=2800000)
    StopPlayLogMeasurement(measurement_id=2800001)
    StopPlayLogMeasurement(measurement_id=2800010)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=198,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=198,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=198,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=198,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterWhitePhantom(PLAYER))
    
    Wait(0.0)


@ContinueOnRest(12801801)
def Event_12801801():
    """Event 12801801"""
    DisableNetworkSync()
    if FlagEnabled(12801800):
        return
    AND_1.Add(FlagEnabled(12801800))
    AND_2.Add(CharacterBackreadDisabled(2800800))
    AND_2.Add(HealthRatio(2800803) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    PlaySoundEffect(2802800, 0, sound_type=SoundType.c_CharacterMotion)


@ContinueOnRest(12801802)
def Event_12801802():
    """Event 12801802"""
    if FlagEnabled(12801800):
        return
    if ThisEventFlagEnabled():
        return
    DisableCharacter(2800800)
    DisableCharacter(2800801)
    AND_1.Add(FlagDisabled(12801800))
    AND_1.Add(ThisEventSlotFlagDisabled())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2802805))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12804223)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_2:
        return
    EnableFlag(9180)
    WaitFrames(frames=1)
    DeleteVFX(2803911, erase_root_only=False)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(28000000, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(28000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    CreateVFX(2803911)
    EnableFlag(12804800)
    EnableCharacter(2800800)
    EnableCharacter(2800801)
    if FlagEnabled(9305):
        return
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9305)


@ContinueOnRest(12801803)
def Event_12801803():
    """Event 12801803"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12804800))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableCharacter(2800800)
    EnableCharacter(2800801)
    EnableFlag(12804800)
    EnableFlag(12801802)


@ContinueOnRest(12804880)
def Event_12804880():
    """Event 12804880"""
    if FlagEnabled(12801800):
        return
    GotoIfFlagEnabled(Label.L0, flag=12801802)
    SkipLinesIfClient(2)
    DisableObject(2801800)
    DeleteVFX(2803800, erase_root_only=False)
    DisableObject(2801801)
    DeleteVFX(2803801, erase_root_only=False)
    AND_1.Add(FlagDisabled(12801800))
    AND_1.Add(FlagEnabled(12801802))
    
    MAIN.Await(AND_1)
    
    EnableObject(2801800)
    CreateVFX(2803800)
    EnableObject(2801801)
    CreateVFX(2803801)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12801800))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2800800, entity=2801800))
    AND_3.Add(FlagEnabled(12801800))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    RotateToFaceEntity(PLAYER, 2802800, animation=101130, wait_for_completion=True)
    AND_4.Add(CharacterHuman(PLAYER))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=2802801))
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(TimeElapsed(seconds=2.0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_5)
    EnableFlag(12804800)
    Restart()


@ContinueOnRest(12804881)
def Event_12804881():
    """Event 12804881"""
    DisableNetworkSync()
    if FlagEnabled(12801800):
        return
    AND_1.Add(FlagDisabled(12801800))
    AND_1.Add(FlagEnabled(12801802))
    AND_1.Add(FlagEnabled(12804800))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2800800, entity=2801800))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 2802800, animation=101130, wait_for_completion=True)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2802801))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    EnableFlag(12804801)
    Restart()


@ContinueOnRest(12804882)
def Event_12804882():
    """Event 12804882"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2801800, radius=6.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12804883)
def Event_12804883():
    """Event 12804883"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2801800, radius=6.0))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2801800, radius=12.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12804802)
def Event_12804802():
    """Event 12804802"""
    if FlagEnabled(12801800):
        return
    DisableAI(2800800)
    DisableAI(2800801)
    DisableAI(2800802)
    DisableAI(2800803)
    DisableAI(2800520)
    DisableAI(2800522)
    DisableAI(2800524)
    DisableAI(2800525)
    DisableAI(2800527)
    DisableAI(2800529)
    DisableHealthBar(2800800)
    DisableHealthBar(2800801)
    DisableHealthBar(2800802)
    DisableHealthBar(2800803)
    DisableGravity(2800801)
    DisableGravity(2800802)
    DisableGravity(2800803)
    EnableImmortality(2800800)
    EnableImmortality(2800801)
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(12804800))
    
    GotoIfClient(Label.L0)
    if FlagDisabled(12804223):
        NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2800800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2800801, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2800802, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2800803, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12804223)
    EnableFlag(12804800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2800800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800801, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800802, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2800803, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800802)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800803)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2800800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800801, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800802, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2800803, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800802)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2800803)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableAI(2800800)
    EnableAI(2800801)
    EnableAI(2800802)
    EnableAI(2800803)
    EnableAI(2800520)
    EnableAI(2800522)
    EnableAI(2800524)
    EnableAI(2800525)
    EnableAI(2800527)
    EnableAI(2800529)
    EnableBossHealthBar(2800803, name=507000)
    ReferDamageToEntity(2800800, target_entity=2800803)
    ReferDamageToEntity(2800801, target_entity=2800803)
    SetCharacterEventTarget(2800800, entity=2800803)
    SetCharacterEventTarget(2800801, entity=2800803)
    CreatePlayLog(name=238)
    StartPlayLogMeasurement(measurement_id=2800010, name=254, overwrite=True)


@ContinueOnRest(12804803)
def Event_12804803():
    """Event 12804803"""
    DisableNetworkSync()
    if FlagEnabled(12801800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2803802)
    DisableSoundEvent(sound_id=2803803)
    AND_1.Add(FlagDisabled(12801800))
    AND_1.Add(FlagEnabled(12804802))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(12804801))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2802802))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=2803804)
    EnableBossMusic(sound_id=2803802)
    AND_2.Add(CharacterHasTAEEvent(2800800, tae_event_id=300))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12801800))
    AND_2.Add(FlagEnabled(12804802))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(12804801))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2802802))
    
    MAIN.Await(AND_2)
    
    DisableSoundEvent(sound_id=2803804)
    DisableBossMusic(sound_id=2803802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2803803)


@ContinueOnRest(12804804)
def Event_12804804():
    """Event 12804804"""
    DisableNetworkSync()
    if FlagEnabled(12801800):
        return
    AND_1.Add(HealthRatio(2800803) > 0.0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2800800, radius=12.0))
    
    MAIN.Await(AND_1)
    
    SetLockedCameraSlot(game_map=YAHARGUL, camera_slot=1)
    AND_2.Add(HealthRatio(2800803) > 0.0)
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2800800, radius=12.5))
    
    MAIN.Await(AND_2)
    
    SetLockedCameraSlot(game_map=YAHARGUL, camera_slot=0)
    Restart()


@ContinueOnRest(12804805)
def Event_12804805():
    """Event 12804805"""
    DisableNetworkSync()
    if FlagEnabled(12801800):
        return
    
    MAIN.Await(FlagEnabled(12801800))
    
    DisableBossMusic(sound_id=2803802)
    DisableBossMusic(sound_id=2803803)
    DisableBossMusic(sound_id=-1)


@ContinueOnRest(12804806)
def Event_12804806():
    """Event 12804806"""
    if FlagEnabled(12801800):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterBackreadEnabled(2800800))
    
    DisableGravity(2800801)
    Wait(1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    Move(
        2800801,
        destination=2800800,
        destination_type=CoordEntityType.Character,
        dummy_id=100,
        set_draw_parent=2800801,
    )
    Restart()


@ContinueOnRest(12804807)
def Event_12804807():
    """Event 12804807"""
    if FlagEnabled(12801800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(2800800, 489))
    
    EnableFlag(12804808)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(2800800, 489))
    
    DisableFlag(12804808)
    Restart()


@ContinueOnRest(12804820)
def Event_12804820(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect: int,
    special_effect_1: int,
    animation_id: int,
):
    """Event 12804820"""
    if FlagEnabled(12801800):
        return
    CreateNPCPart(2800800, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(2800800, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    AND_1.Add(CharacterPartHealth(2800800, npc_part_id=npc_part_id_1) <= 0)
    AND_2.Add(HealthRatio(2800800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    if FlagEnabled(12804808):
        SetNPCPartHealth(2800800, npc_part_id=npc_part_id_1, desired_health=50, overwrite_max=False)
        Restart()
    CreateNPCPart(
        2800800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(2800800, npc_part_id=npc_part_id_1, material_sfx_id=60, material_vfx_id=60)
    ResetAnimation(2800800)
    ResetAnimation(2800801)
    ForceAnimation(2800800, animation_id)
    ForceAnimation(2800801, 7000)
    AddSpecialEffect(2800800, special_effect, affect_npc_part_hp=True)
    RemoveSpecialEffect(2800800, special_effect_1)
    AND_3.Add(CharacterHasSpecialEffect(2800800, 489))
    SkipLinesIfConditionTrue(1, AND_3)
    ReplanAI(2800800)
    Wait(30.0)
    AND_4.Add(CharacterHasSpecialEffect(2800800, 489))
    SkipLinesIfConditionTrue(1, AND_4)
    ReplanAI(2800800)
    
    MAIN.Await(CharacterHasTAEEvent(2800800, tae_event_id=300))
    
    CreateNPCPart(2800800, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(2800800, npc_part_id=npc_part_id_1, material_sfx_id=59, material_vfx_id=59)
    AddSpecialEffect(2800800, special_effect_1, affect_npc_part_hp=True)
    RemoveSpecialEffect(2800800, special_effect)
    AND_5.Add(CharacterHasSpecialEffect(2800800, 489))
    SkipLinesIfConditionTrue(1, AND_5)
    ReplanAI(2800800)
    WaitFrames(frames=10)
    Restart()


@ContinueOnRest(12804830)
def Event_12804830():
    """Event 12804830"""
    if FlagEnabled(12801800):
        return
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(CharacterTargeting(targeting_character=2800801, targeted_character=PLAYER))
    AND_1.Add(CharacterHasTAEEvent(2800801, tae_event_id=10))
    
    MAIN.Await(AND_1)
    
    Move(2800802, destination=PLAYER, destination_type=CoordEntityType.Character, dummy_id=246, short_move=True)
    AICommand(2800802, command_id=200, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Restart()


@ContinueOnRest(12804831)
def Event_12804831():
    """Event 12804831"""
    if FlagEnabled(12801800):
        return
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(CharacterTargeting(targeting_character=2800801, targeted_character=PLAYER))
    AND_1.Add(CharacterHasTAEEvent(2800801, tae_event_id=20))
    
    MAIN.Await(AND_1)
    
    Move(2800802, destination=2800800, destination_type=CoordEntityType.Character, dummy_id=100, short_move=True)
    AICommand(2800802, command_id=210, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Restart()


@ContinueOnRest(12804832)
def Event_12804832():
    """Event 12804832"""
    if FlagEnabled(12801800):
        return
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(CharacterTargeting(targeting_character=2800801, targeted_character=PLAYER))
    AND_1.Add(CharacterHasTAEEvent(2800801, tae_event_id=30))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(2800800, 5585)
    
    MAIN.Await(TimeElapsed(seconds=1.100000023841858))
    
    RemoveSpecialEffect(2800800, 5585)
    Move(2800802, destination=2800800, destination_type=CoordEntityType.Character, dummy_id=10, short_move=True)
    AICommand(2800802, command_id=220, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Restart()


@ContinueOnRest(12804834)
def Event_12804834():
    """Event 12804834"""
    if FlagEnabled(12801800):
        return
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(CharacterTargeting(targeting_character=2800801, targeted_character=PLAYER))
    AND_1.Add(CharacterHasTAEEvent(2800801, tae_event_id=40))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(2800800, 5586)
    
    MAIN.Await(TimeElapsed(seconds=1.100000023841858))
    
    RemoveSpecialEffect(2800800, 5586)
    Move(2800802, destination=2800800, destination_type=CoordEntityType.Character, dummy_id=15, short_move=True)
    AICommand(2800802, command_id=220, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Restart()


@ContinueOnRest(12804835)
def Event_12804835():
    """Event 12804835"""
    if FlagEnabled(12801800):
        return
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(CharacterTargeting(targeting_character=2800801, targeted_character=PLAYER))
    AND_1.Add(CharacterHasTAEEvent(2800801, tae_event_id=50))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(2800800, 5587)
    
    MAIN.Await(TimeElapsed(seconds=1.100000023841858))
    
    RemoveSpecialEffect(2800800, 5587)
    Move(2800802, destination=2800800, destination_type=CoordEntityType.Character, dummy_id=50, short_move=True)
    AICommand(2800802, command_id=220, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Restart()


@ContinueOnRest(12804836)
def Event_12804836():
    """Event 12804836"""
    if FlagEnabled(12801800):
        return
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(CharacterTargeting(targeting_character=2800801, targeted_character=PLAYER))
    AND_1.Add(CharacterHasTAEEvent(2800801, tae_event_id=60))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(2800800, 5588)
    
    MAIN.Await(TimeElapsed(seconds=1.100000023841858))
    
    RemoveSpecialEffect(2800800, 5588)
    Move(2800802, destination=2800800, destination_type=CoordEntityType.Character, dummy_id=55, short_move=True)
    AICommand(2800802, command_id=220, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Restart()


@ContinueOnRest(12804837)
def Event_12804837():
    """Event 12804837"""
    if FlagEnabled(12801800):
        return
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(CharacterTargeting(targeting_character=2800801, targeted_character=PLAYER))
    AND_1.Add(CharacterHasTAEEvent(2800801, tae_event_id=100))
    
    MAIN.Await(AND_1)
    
    Move(2800802, destination=PLAYER, destination_type=CoordEntityType.Character, dummy_id=246, short_move=True)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=100, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Wait(0.800000011920929)
    Move(2800802, destination=PLAYER, destination_type=CoordEntityType.Character, dummy_id=246, short_move=True)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=100, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Wait(1.0)
    Move(2800802, destination=PLAYER, destination_type=CoordEntityType.Character, dummy_id=246, short_move=True)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=100, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Wait(1.2000000476837158)
    Move(2800802, destination=PLAYER, destination_type=CoordEntityType.Character, dummy_id=246, short_move=True)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=100, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Wait(1.399999976158142)
    Move(2800802, destination=PLAYER, destination_type=CoordEntityType.Character, dummy_id=246, short_move=True)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=100, command_slot=0)
    ReplanAI(2800802)
    WaitFrames(frames=1)
    AICommand(2800802, command_id=-1, command_slot=0)
    ReplanAI(2800802)
    Wait(1.600000023841858)
    Restart()


@RestartOnRest(12804838)
def Event_12804838():
    """Event 12804838"""
    if FlagEnabled(12801800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(2800800, tae_event_id=100))
    
    ForceAnimation(2800801, 3000)
    AICommand(2800801, command_id=1, command_slot=1)
    ReplanAI(2800801)
    
    MAIN.Await(CharacterHasTAEEvent(2800800, tae_event_id=300))
    
    AND_1.Add(CharacterHasSpecialEffect(2800800, 489))
    SkipLinesIfConditionTrue(1, AND_1)
    ReplanAI(2800800)
    Wait(10.0)
    AICommand(2800801, command_id=-1, command_slot=1)
    ReplanAI(2800801)
    Restart()


@RestartOnRest(12804840)
def Event_12804840(_, character: int):
    """Event 12804840"""
    if FlagEnabled(12801800):
        return
    SetCharacterEventTarget(character, entity=2800801)
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2800801, 7010)
    AICommand(2800800, command_id=1, command_slot=2)
    AICommand(2800801, command_id=1, command_slot=2)
    AND_2.Add(CharacterHasSpecialEffect(2800800, 489))
    SkipLinesIfConditionTrue(1, AND_2)
    ReplanAI(2800800)
    ReplanAI(2800801)
    Wait(30.0)
    AICommand(2800800, command_id=-1, command_slot=2)
    AICommand(2800801, command_id=-1, command_slot=2)
    AND_3.Add(CharacterHasSpecialEffect(2800800, 489))
    SkipLinesIfConditionTrue(1, AND_3)
    ReplanAI(2800800)
    ReplanAI(2800801)


@RestartOnRest(12804850)
def Event_12804850(_, character: int):
    """Event 12804850"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    IncrementEventValue(12804860, bit_count=4, max_value=10)


@RestartOnRest(12804870)
def Event_12804870():
    """Event 12804870"""
    AND_1.Add(FlagEnabled(12804802))
    AND_1.Add(HealthRatio(2800803) < 1.0)
    
    MAIN.Await(AND_1)
    
    if FlagDisabled(12804871):
        AICommand(2800800, command_id=1, command_slot=0)
        AICommand(2800801, command_id=1, command_slot=0)
    AICommand(2800520, command_id=1, command_slot=0)
    AICommand(2800522, command_id=1, command_slot=0)
    AICommand(2800524, command_id=1, command_slot=0)
    AICommand(2800525, command_id=1, command_slot=0)
    AICommand(2800527, command_id=1, command_slot=0)
    AICommand(2800529, command_id=1, command_slot=0)
    AND_2.Add(CharacterHasSpecialEffect(2800800, 489))
    SkipLinesIfConditionTrue(1, AND_2)
    ReplanAI(2800800)
    ReplanAI(2800801)
    ReplanAI(2800520)
    ReplanAI(2800522)
    ReplanAI(2800524)
    ReplanAI(2800525)
    ReplanAI(2800527)
    ReplanAI(2800529)


@RestartOnRest(12804871)
def Event_12804871():
    """Event 12804871"""
    AND_1.Add(FlagEnabled(12804802))
    OR_1.Add(HealthRatio(2800803) < 0.5)
    OR_1.Add(EventValue(flag=12804860, bit_count=4) >= 3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AICommand(2800800, command_id=2, command_slot=0)
    AICommand(2800801, command_id=2, command_slot=0)
    AICommand(2800800, command_id=1, command_slot=1)
    AND_2.Add(CharacterHasSpecialEffect(2800800, 489))
    SkipLinesIfConditionTrue(1, AND_2)
    ReplanAI(2800800)


@ContinueOnRest(12800990)
def Event_12800990():
    """Event 12800990"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(PlayerStandingOnCollision(2803500))
    
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=272,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=272,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=272,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=272,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )


@ContinueOnRest(12800901)
def Event_12800901():
    """Event 12800901"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1315):
        return
    if FlagEnabled(1310):
        return
    
    MAIN.Await(CharacterDead(2800670))
    
    DisableFlagRange((1300, 1319))
    EnableFlag(1315)
    SaveRequest()


@ContinueOnRest(12800902)
def Event_12800902():
    """Event 12800902"""
    MAIN.Await(FlagEnabled(72800312))
    
    DisableFlag(72800312)
    DisableFlagRange((1300, 1319))
    EnableFlag(1301)
    ForceAnimation(2800670, 103107, loop=True, skip_transition=True)
    SaveRequest()


@ContinueOnRest(12800903)
def Event_12800903():
    """Event 12800903"""
    MAIN.Await(FlagEnabled(72800314))
    
    DisableFlag(72800314)
    DisableFlagRange((1300, 1319))
    EnableFlag(1313)


@ContinueOnRest(12800904)
def Event_12800904():
    """Event 12800904"""
    MAIN.Await(FlagEnabled(72800315))
    
    DisableFlag(72800315)
    DisableFlagRange((1300, 1319))
    EnableFlag(1314)


@ContinueOnRest(12800905)
def Event_12800905():
    """Event 12800905"""
    MAIN.Await(FlagEnabled(72800316))
    
    DisableFlag(72800316)
    DisableFlagRange((1300, 1319))
    EnableFlag(1311)


@ContinueOnRest(12800906)
def Event_12800906():
    """Event 12800906"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    DisableFlag(72800310)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2802450))
    
    EnableFlag(72800310)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=2802450))
    
    Restart()


@ContinueOnRest(12800908)
def Event_12800908():
    """Event 12800908"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=2800670))
    AND_1.Add(HealthRatio(2800670) != 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2800670, 103093)
    Restart()


@ContinueOnRest(12800909)
def Event_12800909():
    """Event 12800909"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagDisabled(1310))
    AND_1.Add(HealthRatio(2800670) == 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2800670, 103094)


@ContinueOnRest(12800910)
def Event_12800910():
    """Event 12800910"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(2800670, 151))
    AND_1.Add(HealthRatio(2800670) != 0.0)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=1300)
    ForceAnimation(2800670, 103091)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2800670, 103092)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=5)
    Restart()


@ContinueOnRest(12800911)
def Event_12800911():
    """Event 12800911"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L4, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L0, flag=1313)
    DisableFlagRange((1300, 1319))
    EnableFlag(1304)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=1314)
    DisableFlagRange((1300, 1319))
    EnableFlag(1309)

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L2, flag=1311)
    GotoIfFlagDisabled(Label.L4, flag=72800317)
    GotoIfFlagDisabled(Label.L5, flag=72800318)
    DisableFlagRange((1300, 1319))
    EnableFlag(1310)
    Goto(Label.L2)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableFlag(72800317)
    Goto(Label.L2)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableFlag(72800318)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    OR_1.Add(FlagEnabled(1300))
    OR_1.Add(FlagEnabled(1301))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(9802))
    GotoIfConditionFalse(Label.L3, input_condition=AND_1)
    DisableFlagRange((1300, 1319))
    EnableFlag(1316)
    Goto(Label.L3)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlag(72800308)

    # --- Label 4 --- #
    DefineLabel(4)
    GotoIfFlagEnabled(Label.L0, flag=1300)
    GotoIfFlagEnabled(Label.L1, flag=1301)
    GotoIfFlagEnabled(Label.L1, flag=1311)
    GotoIfFlagEnabled(Label.L2, flag=1310)
    GotoIfFlagEnabled(Label.L3, flag=1315)
    GotoIfFlagEnabled(Label.L1, flag=1313)
    GotoIfFlagEnabled(Label.L1, flag=1314)
    DisableBackread(2800670)
    DisableBackread(2800671)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(2800670)
    DisableBackread(2800671)
    ForceAnimation(2800670, 103092, loop=True, skip_transition=True)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(2800670)
    DisableBackread(2800671)
    ForceAnimation(2800670, 103091, loop=True, skip_transition=True)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableBackread(2800670)
    EnableBackread(2800671)
    EzstateAIRequest(2800671, command_id=6, command_slot=1)
    DropMandatoryTreasure(2800671)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    EnableBackread(2800670)
    DisableBackread(2800671)
    Move(2800670, destination=2802452, destination_type=CoordEntityType.Region, short_move=True)
    EzstateAIRequest(2800670, command_id=7, command_slot=1)
    WaitFrames(frames=1)
    DropMandatoryTreasure(2800670)
    End()


@ContinueOnRest(12800920)
def Event_12800920(_, flag: int, flag_1: int, flag_2: int, obj: int, item_lot: int):
    """Event 12800920"""
    if Client():
        return
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(OR_1)
    
    CreateObjectVFX(obj, vfx_id=200, dummy_id=900201)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=7500, entity=obj))
    
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(item_lot, host_only=False)
    DeleteObjectVFX(obj)


@RestartOnRest(12804450)
def Event_12804450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 12804450"""
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


@RestartOnRest(12804400)
def Event_12804400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12804400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(FlagEnabled(9802))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_1.Add(FlagEnabled(13501900))
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
    AND_2.Add(FlagEnabled(9802))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_1.Add(FlagEnabled(13501900))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12804401)
def Event_12804401(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12804401"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(FlagEnabled(9802))
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
    AND_2.Add(FlagEnabled(9802))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12804410)
def Event_12804410(
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
    """Event 12804410"""
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


@RestartOnRest(12804460)
def Event_12804460(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 12804460"""
    if Client():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(CharacterInsideRegion(character, region=region))
    
    MAIN.Await(AND_1)
    
    ResetAnimation(character)
    RotateToFaceEntity(character, region_1, animation=animation, wait_for_completion=True)
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
    SetCharacterEventTarget(character, entity=2800800)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
