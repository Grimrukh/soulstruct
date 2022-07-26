"""
Central Yharnam / Iosekfa's Clinic

linked:
174

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス_撃破
52: PC情報_ボス撃破_教区長
80: ボス_戦闘開始
96: ボス戦_撃破時間
114: PC情報_ボス撃破_ガスコイン
146: 
148: PC情報_聖堂街B到達時
174: N:\\SPRJ\\data\\Param\\event\\common.emevd
250: 
252: 
254: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RunEvent(7000, slot=15, args=(2410950, 2411950, 9401, 12417800))
    RunEvent(7000, slot=16, args=(2410951, 2411951, 999, 12417820))
    RunEvent(7000, slot=17, args=(2410952, 2411952, 12411700, 12417840))
    RunEvent(7000, slot=18, args=(2410953, 2411953, 12411800, 12417860))
    Event_12411010()
    RunEvent(7100, slot=15, args=(72410200, 2411950))
    RunEvent(7100, slot=16, args=(72410201, 2411951))
    RunEvent(7100, slot=17, args=(72410202, 2411952))
    RunEvent(7100, slot=18, args=(72410203, 2411953))
    RunEvent(7200, slot=15, args=(72410100, 2411950, 2102950))
    RunEvent(7200, slot=16, args=(72410101, 2411951, 2102950))
    RunEvent(7200, slot=17, args=(72410102, 2411952, 2102950))
    RunEvent(7200, slot=18, args=(72410103, 2411953, 2102950))
    RunEvent(7300, slot=15, args=(72102410, 2411950))
    RunEvent(7300, slot=16, args=(72102411, 2411951))
    RunEvent(7300, slot=17, args=(72102412, 2411952))
    RunEvent(7300, slot=18, args=(72102413, 2411953))
    RunEvent(9200, slot=3, args=(2413900,))
    RunEvent(9220, slot=3, args=(2410750, 12414220, 12414221, 2410, 280))
    RunEvent(9240, slot=3, args=(2410750, 12414220, 12414221, 12414222, 280))
    RunEvent(9260, slot=3, args=(2410750, 12414220, 12414221, 12414222, 280))
    RunEvent(9280, slot=3, args=(2410750, 12414220, 12414221, 2410, 12414223, 280))
    Event_12411899()
    Event_12410310()
    CreateObjectVFX(2411000, vfx_id=200, model_point=900130)
    CreateObjectVFX(2411001, vfx_id=200, model_point=900130)
    CreateObjectVFX(2411004, vfx_id=200, model_point=900130)
    DeleteVFX(2413230, erase_root_only=False)
    DeleteVFX(2413233, erase_root_only=False)
    Event_12414400(0, flag=12414440, vfx_id=2413230, flag_1=12414420, flag_2=12414430, flag_3=12411700, flag_4=6001)
    Event_12414401(0, flag=12414441, vfx_id=2413233, flag_1=12414421, flag_2=12414431, flag_3=12411700, flag_4=6001)
    Event_12414410(
        0,
        sign_type=7,
        character=2410158,
        region=2412920,
        summon_flag=12414420,
        dismissal_flag=12414430,
        flag=12414440,
        flag_1=12411700,
        action_button_id=10575,
    )
    Event_12414410(
        1,
        sign_type=0,
        character=2410740,
        region=2412921,
        summon_flag=12414421,
        dismissal_flag=12414431,
        flag=12414441,
        flag_1=12411700,
        action_button_id=10576,
    )
    Event_12414450(0, character=2410158, region=2412710, flag=12414420, flag_1=12414430, flag_2=12414700)
    Event_12414450(1, character=2410740, region=2412711, flag=12414421, flag_1=12414431, flag_2=12414700)
    Event_12414460(
        0,
        character=2410158,
        region=2412710,
        region_1=2412800,
        region_2=2412801,
        animation=7014,
        flag=12414450,
        region_3=2412801,
    )
    Event_12414460(
        1,
        character=2410740,
        region=2412711,
        region_1=2412800,
        region_2=2412801,
        animation=101130,
        flag=12414451,
        region_3=2412801,
    )
    Event_12414470()
    Event_12414480()
    Event_12414490()
    GotoIfFlagDisabled(Label.L0, flag=12410999)
    EnableFlag(9400)
    EnableFlag(9401)
    AddSpecialEffect(2410015, 5591)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=12410999)
    Event_12410286(0, start_climbing_flag=12410400, stop_climbing_flag=12410401, obj=2411204, obj_1=2411316)
    Event_12410820()

    # --- Label 1 --- #
    DefineLabel(1)
    StartPlayLogMeasurement(measurement_id=2410000, name=0, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2410001, name=18, overwrite=True)
    Event_12410990()
    Event_12410900()
    Event_12415060(0, character=2410112, region=2412000, region_1=2412001, radius=4.0)
    Event_12415060(1, character=2410113, region=2412000, region_1=2412001, radius=4.0)
    Event_12415060(2, character=2410114, region=2412000, region_1=2412001, radius=4.0)
    Event_12415060(3, character=2410115, region=2412000, region_1=2412001, radius=4.0)
    Event_12415060(4, character=2410116, region=2412000, region_1=2412001, radius=4.0)
    Event_12415060(10, character=2410121, region=2412120, region_1=0, radius=4.0)
    Event_12415060(11, character=2410125, region=2412120, region_1=0, radius=4.0)
    Event_12415060(12, character=2410126, region=2412120, region_1=0, radius=4.0)
    Event_12415060(13, character=2410127, region=2412120, region_1=0, radius=4.0)
    Event_12415060(15, character=2410161, region=2412120, region_1=0, radius=4.0)
    Event_12415080(
        3,
        character=2410178,
        animation_id=7010,
        animation_id_1=7011,
        region=2412154,
        ai_param_id=263496,
        ai_param_id_1=263431,
        radius=2.0,
    )
    Event_12415460(
        0,
        character=2410019,
        animation_id=7020,
        animation_id_1=7021,
        region=2412251,
        radius=1.0,
        destination=2412010,
        entity=2411219,
    )
    Event_12415461(0, entity=2411219, animation_id=0, animation_id_1=1)
    Event_12410160(2, region=2412032, anchor_entity=2412037, sound_type=0, sound_id=20011002)
    Event_12410160(4, region=2412122, anchor_entity=2412035, sound_type=0, sound_id=20011001)
    Event_12410160(5, region=2412033, anchor_entity=2412038, sound_type=1, sound_id=500007600)
    Event_12415010(0, anchor_entity=2412039, sound_type=0, sound_id=20011001, seconds=300.0)
    Event_12415700()
    Event_12415435(12, character=2410172, region=2412122)
    Event_12415435(13, character=2410173, region=2412122)
    Event_12415435(17, character=2410186, region=2412122)
    Event_12415435(18, character=2410187, region=2412122)
    Event_12415435(19, character=2410188, region=2412122)
    Event_12415435(20, character=2410189, region=2412122)
    Event_12415435(22, character=2410191, region=2412122)
    Event_12415435(23, character=2410192, region=2412122)
    Event_12415475(0, character=2410194, animation_id=7012, animation_id_1=7013, region=2412050)
    Event_12415476(0, attacked_entity=2410194, animation_id=7013)
    Event_12415478(0, character=2410194)
    Event_12415477(0, character=2410113)
    Event_12415479(0, character=2410194)
    Event_12415420(0, character=2410272, region=2412262, left=12410379)
    Event_12415420(1, character=2410278, region=2412260, left=0)
    Event_12415420(2, character=2410275, region=2412261, left=0)
    Event_12415420(3, character=2410277, region=2412263, left=0)
    Event_12415420(4, character=2410271, region=2412264, left=12410378)
    Event_12415420(5, character=2410279, region=2412265, left=0)
    Event_12415225(0, character=2410015, animation_id=3004, radius=50.0)
    Event_12415225(1, character=2410102, animation_id=3027, radius=50.0)
    Event_12415228(0, character=2410016, animation_id=3028, radius=6.0)
    Event_12415232(0, character=2410178, region=2412086)
    Event_12415233(0, region=2412122, character=2410196, region_1=2412136)
    Event_12415250(1, character=2410182, animation_id=7001, min_seconds=5.0, max_seconds=10.0, region=2412075)
    Event_12415255(1, character=2410183)
    Event_12415255(2, character=2410182)
    Event_12415255(4, character=2410181)
    Event_12415295(0, character=2410183, region=2412120, radius=2.0, region_1=2412074)
    Event_12415295(1, character=2410182, region=2412120, radius=2.0, region_1=2412075)
    Event_12415300(0, flag=12415295, character=2410183, region=2412074, region_1=2412121, radius=2.0)
    Event_12415300(1, flag=12415296, character=2410182, region=2412075, region_1=2412121, radius=2.0)
    Event_12415305(0, flag=12415300, character=2410183, region=2412121, region_1=2412122, radius=2.0, region_2=2412084)
    Event_12415305(1, flag=12415301, character=2410182, region=2412121, region_1=2412122, radius=2.0, region_2=2412085)
    Event_12415310(
        0,
        flag=12415305,
        character=2410183,
        region=2412084,
        region_1=2412122,
        radius=2.0,
        patrol_information_id=2413500,
    )
    Event_12415310(
        1,
        flag=12415306,
        character=2410182,
        region=2412085,
        region_1=2412122,
        radius=2.0,
        patrol_information_id=2413500,
    )
    Event_12415315(0, character=2410210, region=2412120, radius=2.0, region_1=2412130)
    Event_12415315(1, character=2410211, region=2412120, radius=2.0, region_1=2412132)
    Event_12415320(0, flag=12415315, character=2410210, region=2412130, region_1=2412122, patrol_information_id=2413505)
    Event_12415320(1, flag=12415316, character=2410211, region=2412132, region_1=2412122, patrol_information_id=2413505)
    Event_12415325(0, flag=12415320, character=2410210, region=2412122, patrol_information_id=2413502)
    Event_12415325(1, flag=12415321, character=2410211, region=2412122, patrol_information_id=2413501)
    Event_12415330(0, character=2410213, region=2412124, region_1=2412123, radius=2.0, region_2=2412125)
    Event_12415335(0, flag=12415330, character=2410213, region=2412134, region_1=2412122, patrol_information_id=2413503)
    Event_12415340(0, character=2410018, region=2412120, radius=2.0, region_1=2412096)
    Event_12415340(2, character=2410181, region=2412121, radius=2.0, region_1=2412083)
    Event_12415345(
        0,
        flag=12415340,
        character=2410018,
        region=2412096,
        region_1=0,
        radius=2.0,
        left=0,
        patrol_information_id=-1,
    )
    Event_12415345(
        2,
        flag=12415342,
        character=2410181,
        region=2412083,
        region_1=2412122,
        radius=2.0,
        left=1,
        patrol_information_id=2413500,
    )
    Event_12410450(0, character=2410400, flag=52410990)
    Event_12410450(1, character=2410401, flag=52410980)
    Event_12410450(2, character=2410402, flag=52410970)
    Event_12410450(3, character=2410403, flag=52410960)
    Event_12410450(4, character=2410404, flag=52410950)
    RegisterLadder(start_climbing_flag=12410402, stop_climbing_flag=12410403, obj=2411210)
    RegisterLadder(start_climbing_flag=12410404, stop_climbing_flag=12410405, obj=2411211)
    RegisterLadder(start_climbing_flag=12410406, stop_climbing_flag=12410407, obj=2411212)
    RegisterLadder(start_climbing_flag=12410408, stop_climbing_flag=12410409, obj=2411213)
    RegisterLadder(start_climbing_flag=12410410, stop_climbing_flag=12410411, obj=2411214)
    RegisterLadder(start_climbing_flag=12410412, stop_climbing_flag=12410413, obj=2411215)
    RegisterLadder(start_climbing_flag=12410414, stop_climbing_flag=12410415, obj=2411216)
    RegisterLadder(start_climbing_flag=12410416, stop_climbing_flag=12410417, obj=2411217)
    RegisterLadder(start_climbing_flag=12410418, stop_climbing_flag=12410419, obj=2411218)
    RegisterLadder(start_climbing_flag=12410420, stop_climbing_flag=12410421, obj=2411225)
    RegisterLadder(start_climbing_flag=12410422, stop_climbing_flag=12410423, obj=2411226)
    RegisterLadder(start_climbing_flag=12410424, stop_climbing_flag=12410425, obj=2411227)
    Event_12410290()
    CreateHazard(
        obj_flag=12410430,
        obj=2411205,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12410431,
        obj=2411206,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12410432,
        obj=2411207,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12410433,
        obj=2411208,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    Event_12410200(0, obj=2411300, obj_1=2411310, obj_act_id=12410200)
    Event_12410200(2, obj=2411302, obj_1=2411312, obj_act_id=12410202)
    Event_12410200(3, obj=2411303, obj_1=2411313, obj_act_id=12410203)
    Event_12410200(5, obj=2411305, obj_1=2411315, obj_act_id=12410205)
    Event_12415020(0, action_button_id=7000, anchor_entity=2411305, flag=12410205, text=10010171)
    Event_12415020(2, action_button_id=2410021, anchor_entity=2411300, flag=12410200, text=10010160)
    Event_12415020(3, action_button_id=2410021, anchor_entity=2411302, flag=12410202, text=10010160)
    Event_12415020(4, action_button_id=2410021, anchor_entity=2411303, flag=12410203, text=10010160)
    Event_12410100(1, action_button_id=2410011, anchor_entity=2410701, flag=12410112, text=10010161)
    Event_12410100(2, action_button_id=2410050, anchor_entity=2411301, flag=12410117, text=10010161)
    Event_12410110(2, obj=2410701, obj_act_id=12411301, animation_id=2, obj_act_id_1=2410010)
    Event_12410110(3, obj=2411308, obj_act_id=12411302, animation_id=2, obj_act_id_1=2410010)
    Event_12410110(4, obj=2411306, obj_act_id=12411304, animation_id=1, obj_act_id_1=2410030)
    Event_12410110(5, obj=2411304, obj_act_id=12411307, animation_id=1, obj_act_id_1=2410080)
    Event_12410110(6, obj=2411309, obj_act_id=12411308, animation_id=1, obj_act_id_1=2410010)
    Event_12410110(7, obj=2411301, obj_act_id=12411309, animation_id=1, obj_act_id_1=2410090)
    Event_12410120()
    Event_12410130(0, obj_act_id=12411306)
    Event_12410151()
    Event_12410140()
    RunEvent(7600, slot=30, args=(2411999, 2413999))
    RunEvent(7600, slot=31, args=(2411998, 2413998))
    RunEvent(7600, slot=32, args=(2411997, 2413997))
    Event_12415390(0, character=2410202)
    Event_12414732()
    Event_12414733()
    Event_12411700()
    Event_12411701()
    Event_12411702()
    Event_12414730()
    Event_12414731()
    Event_12414702()
    Event_12414703()
    Event_12414704()
    Event_12414705()
    Event_12411703()
    Event_12414707()
    Event_12414708()
    Event_12414710(
        0,
        npc_part_id=2410,
        npc_part_id_1=2410,
        part_index=1,
        part_health=20,
        special_effect_id=480,
        special_effect_id_1=490,
        animation_id=8020,
    )
    Event_12414710(
        1,
        npc_part_id=2411,
        npc_part_id_1=2411,
        part_index=2,
        part_health=120,
        special_effect_id=481,
        special_effect_id_1=491,
        animation_id=8000,
    )
    Event_12414710(
        2,
        npc_part_id=2412,
        npc_part_id_1=2412,
        part_index=3,
        part_health=300,
        special_effect_id=482,
        special_effect_id_1=492,
        animation_id=8010,
    )
    Event_12414710(
        3,
        npc_part_id=2413,
        npc_part_id_1=2413,
        part_index=4,
        part_health=200,
        special_effect_id=483,
        special_effect_id_1=493,
        animation_id=8030,
    )
    Event_12414710(
        4,
        npc_part_id=2414,
        npc_part_id_1=2414,
        part_index=5,
        part_health=200,
        special_effect_id=484,
        special_effect_id_1=494,
        animation_id=8040,
    )
    Event_12414720(0, special_effect=480, special_effect_1=490, bit_index=5, bit_index_1=10)
    Event_12414720(1, special_effect=481, special_effect_1=491, bit_index=6, bit_index_1=11)
    Event_12414720(2, special_effect=482, special_effect_1=492, bit_index=7, bit_index_1=12)
    Event_12414720(3, special_effect=483, special_effect_1=493, bit_index=8, bit_index_1=13)
    Event_12414720(4, special_effect=484, special_effect_1=494, bit_index=9, bit_index_1=14)
    GotoIfFlagEnabled(Label.L2, flag=12410999)
    Event_12410000()
    Event_12410285(0, start_climbing_flag=12410400, stop_climbing_flag=12410401, obj=2411204, obj_1=2411316)
    Event_12410995()

    # --- Label 2 --- #
    DefineLabel(2)
    Event_12410170()
    Event_12415150(
        0,
        character=2410100,
        animation_id=7010,
        animation_id_1=7011,
        radius=6.0,
        ai_param_id=263499,
        ai_param_id_1=263450,
    )
    Event_12415150(
        1,
        character=2410101,
        animation_id=7014,
        animation_id_1=7015,
        radius=7.0,
        ai_param_id=263499,
        ai_param_id_1=263440,
    )
    Event_12415150(
        2,
        character=2410103,
        animation_id=7010,
        animation_id_1=7011,
        radius=4.0,
        ai_param_id=263499,
        ai_param_id_1=263450,
    )
    Event_12410160(1, region=2412031, anchor_entity=2412036, sound_type=0, sound_id=240002600)
    Event_12415160(0, character=2410130, animation_id=9002, animation_id_1=3001)
    Event_12415160(1, character=2410131, animation_id=9000, animation_id_1=3001)
    Event_12415160(2, character=2410132, animation_id=9000, animation_id_1=0)
    Event_12415160(3, character=2410133, animation_id=9001, animation_id_1=0)
    Event_12415160(4, character=2410134, animation_id=9002, animation_id_1=3001)
    Event_12415160(5, character=2410136, animation_id=9001, animation_id_1=0)
    Event_12415160(6, character=2410137, animation_id=9001, animation_id_1=3001)
    Event_12415160(7, character=2410138, animation_id=9001, animation_id_1=0)
    Event_12415160(8, character=2410139, animation_id=9001, animation_id_1=0)
    Event_12415130(
        0,
        character=2410140,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=1,
    )
    Event_12415130(
        1,
        character=2410141,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=0,
    )
    Event_12415130(
        3,
        character=2410143,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=0,
    )
    Event_12415130(
        4,
        character=2410144,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=1,
    )
    Event_12415130(
        6,
        character=2410146,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=0,
    )
    Event_12415130(
        7,
        character=2410147,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=0,
    )
    Event_12415130(
        8,
        character=2410148,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=1,
    )
    Event_12415130(
        9,
        character=2410149,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=1,
    )
    Event_12415130(
        10,
        character=2410150,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=0,
    )
    Event_12415130(
        14,
        character=2410154,
        animation_id=9000,
        animation_id_1=9061,
        flag=52410270,
        ai_param_id=112499,
        ai_param_id_1=112400,
        right=1,
    )
    Event_12410155(0, character=2410157, region=2412020, region_1=2412021, region_2=2412022)
    Event_12410156(0, character=2410040, character_1=2410500, character_2=2410501)
    Event_12410340(0, character=2410220, region=2412230, command_id=10, region_1=2412220)
    Event_12410340(1, character=2410221, region=2412231, command_id=10, region_1=2412220)
    Event_12410340(2, character=2410222, region=2412232, command_id=10, region_1=2412220)
    Event_12410340(3, character=2410223, region=2412233, command_id=10, region_1=2412220)
    Event_12410340(4, character=2410224, region=2412234, command_id=10, region_1=2412220)
    Event_12410340(5, character=2410225, region=2412235, command_id=10, region_1=2412220)
    Event_12410340(6, character=2410226, region=2412236, command_id=10, region_1=2412220)
    Event_12410340(7, character=2410227, region=2412237, command_id=10, region_1=2412220)
    Event_12410340(8, character=2410228, region=2412238, command_id=10, region_1=2412220)
    Event_12410378(0, character=2410271, animation_id=3021, obj=2411270, destination=2412046)
    Event_12410378(1, character=2410272, animation_id=3021, obj=2411271, destination=2412045)
    Event_12410380(0, character=2410275, animation_id=3020)
    Event_12410380(1, character=2410277, animation_id=3020)
    Event_12410380(2, character=2410278, animation_id=3020)
    Event_12410380(3, character=2410279, animation_id=3020)
    Event_12410370()
    Event_12415372(0, character=2410023)
    Event_12415372(1, character=2410024)
    Event_12415372(2, character=2410025)
    Event_12415372(3, character=2410026)
    Event_12415372(4, character=2410027)
    Event_12410321(
        0,
        flag=12415350,
        flag_1=12410350,
        flag_2=12410351,
        flag_3=12410330,
        obj=2411320,
        obj_1=2411317,
        obj_2=2411318,
    )
    Event_12410325(0, flag=12415350, flag_1=12410350, flag_2=12410351, flag_3=12410330)
    Event_12410322(
        0,
        flag=12415350,
        flag_1=12410350,
        flag_2=12410351,
        flag_3=12410330,
        region=2412322,
        obj_act_id=12410320,
    )
    Event_12410323(
        0,
        flag=12415350,
        flag_1=12410350,
        flag_2=12410351,
        flag_3=12410330,
        region=2412321,
        obj_act_id=12410321,
    )
    Event_12410324(0, flag=12415350, flag_1=12410350, flag_2=12410330, entity=2411317, entity_1=2411318)
    Event_12410330(0, flag=12410330, region=2412323, obj=2411317, obj_1=2411318)
    Event_12410490(0, obj=2411510, obj_1=2411500, flag=12410490)
    Event_12410490(1, obj=2411511, obj_1=2411501, flag=12410491)
    Event_12410010()
    Event_12410011()
    Event_12410012()
    Event_12410600(1, obj_act_id=12411202, obj=2411102, obj_act_id_1=9942)
    AND_15.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_15)
    if FlagEnabled(6630):
        EnableFlag(12411999)
    if FlagDisabled(12411999):
        EnableObject(2411100)
        DisableObject(2411103)
        EnableObjectActivation(2411100, obj_act_id=9942)
        DisableObjectActivation(2411103, obj_act_id=9942)
        Event_12410600(2, obj_act_id=12411200, obj=2411100, obj_act_id_1=9942)
    else:
        DisableObject(2411100)
        EnableObject(2411103)
        DisableObjectActivation(2411100, obj_act_id=9942)
        EnableObjectActivation(2411103, obj_act_id=9942)
        Event_12410600(3, obj_act_id=12411203, obj=2411103, obj_act_id_1=9942)
    AND_14.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_14)
    if FlagEnabled(6640):
        EnableFlag(12411998)
    if FlagDisabled(12411998):
        EnableObject(2411450)
        DisableObject(2411451)
        EnableTreasure(obj=2411450)
        DisableTreasure(obj=2411451)
    else:
        DisableObject(2411450)
        EnableObject(2411451)
        DisableTreasure(obj=2411450)
        EnableTreasure(obj=2411451)
    AND_13.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_13)
    if FlagEnabled(6312):
        EnableFlag(12411997)
    if FlagDisabled(12411997):
        EnableObject(2411102)
        DisableObject(2411104)
        EnableObjectActivation(2411102, obj_act_id=9942)
        DisableObjectActivation(2411104, obj_act_id=9942)
        Event_12410600(4, obj_act_id=12411202, obj=2411102, obj_act_id_1=9942)
    else:
        DisableObject(2411102)
        EnableObject(2411104)
        DisableObjectActivation(2411102, obj_act_id=9942)
        EnableObjectActivation(2411104, obj_act_id=9942)
        Event_12410600(5, obj_act_id=12411204, obj=2411104, obj_act_id_1=9942)
    Event_12414812()
    Event_12414813()
    Event_12411800()
    Event_12411801()
    Event_12411802()
    Event_12414810()
    Event_12414811()
    Event_12414802()
    Event_12414803()
    Event_12414804()
    Event_12414805()
    Event_12414807()
    Event_12414808()
    Event_12414809()
    Event_12411803()
    Event_12415238(0, region=2412820, character=2410810, region_1=2412821, region_2=2412824, region_3=2412822)
    Event_12415238(1, region=2412820, character=2410811, region_1=2412821, region_2=2412824, region_3=2412822)
    Event_12410850(0, flag=70000050, action_button_id=6030, destination=2410870)
    Event_12410850(1, flag=70000051, action_button_id=6030, destination=2410871)
    Event_12410850(2, flag=70000070, action_button_id=6030, destination=2410872)
    Event_12410850(3, flag=70000071, action_button_id=6030, destination=2410873)
    Event_12410860(0, character=2410770, animation_id=103089)
    Event_12410870(0, character=2410770, animation_id=103082, special_effect=153)
    Event_12410880(0, character=2410770, animation_id=103086)
    Event_12410702()
    Event_12410704()
    Event_12410705()
    Event_12410706()
    Event_12410710()
    Event_12410713()
    Event_12410715()
    Event_12410716()
    Event_12410703()
    DisableFlag(72410330)
    DisableFlag(72410335)
    DisableFlag(72410323)
    Event_12410650()
    Event_12410651()
    Event_12410652()
    Event_12410653()
    Event_12410654()
    Event_12410655()
    Event_12410656()
    Event_12410657()
    Event_12410658()
    Event_12410659()
    Event_12410661()
    Event_12410662(0, flag=1163, flag_1=72410331, flag_2=72410338)
    Event_12410662(1, flag=1204, flag_1=72410331, flag_2=72410339)
    Event_12410662(2, flag=1268, flag_1=72410332, flag_2=72410340)
    Event_12410662(3, flag=1190, flag_1=72410332, flag_2=72410341)
    Event_12410662(4, flag=1223, flag_1=72410332, flag_2=72410342)
    Event_12410662(5, flag=1309, flag_1=72410332, flag_2=72410343)
    Event_12410668()
    Event_12410669(0, character=2410290, flag=1124, animation_id=0)
    Event_12410669(1, character=2410291, flag=1163, animation_id=0)
    Event_12410669(2, character=2410292, flag=1204, animation_id=7001)
    Event_12410669(3, character=2410293, flag=1268, animation_id=0)
    Event_12410669(4, character=2410294, flag=1190, animation_id=0)
    Event_12410669(5, character=2410295, flag=1223, animation_id=7000)
    Event_12410669(6, character=2410296, flag=1309, animation_id=7002)
    Event_12410676()
    Event_12410677()
    Event_12410680(0, character=2410290)
    Event_12410680(1, character=2410291)
    Event_12410680(2, character=2410292)
    Event_12410680(3, character=2410293)
    Event_12410680(4, character=2410294)
    Event_12410680(5, character=2410295)
    Event_12410680(6, character=2410296)
    Event_12410687(0, flag=12410687, flag_1=72410347)
    Event_12410687(1, flag=12410688, flag_1=72410348)
    Event_12410687(2, flag=12410689, flag_1=72410349)
    Event_12410687(3, flag=12410690, flag_1=72410350)
    Event_12410687(4, flag=12410691, flag_1=72410351)
    Event_12410687(5, flag=12410692, flag_1=72410352)
    Event_12410693(0, flag=12410693, flag_1=72410353)
    Event_12410693(1, flag=12410694, flag_1=72410354)
    Event_12410693(2, flag=12410695, flag_1=72410355)
    Event_12410693(3, flag=12410696, flag_1=72410356)
    Event_12410693(4, flag=12410697, flag_1=72410357)
    Event_12410693(5, flag=12410698, flag_1=72410358)
    Event_12410700()
    Event_12410721()
    Event_12410730()
    Event_12410731()
    Event_12410732()
    Event_12410733()
    Event_12410734()
    Event_12410736()
    Event_12410737()
    Event_12410738()
    Event_12410739()
    Event_12410785()
    Event_12410786()
    Event_12410787()
    Event_12410740()
    Event_12410741()
    Event_12410742()
    Event_12410743()
    Event_12410746()
    Event_12410747()
    Event_12410748()
    Event_12410749()
    Event_12410750(0, flag=72410392, action_button_id=6030, destination=2410732)
    Event_12410760()
    Event_12410761()
    Event_12410763()
    Event_12410770(0, character=2410290)
    Event_12410770(1, character=2410291)
    Event_12410770(2, character=2410292)
    Event_12410770(3, character=2410293)
    Event_12410770(4, character=2410294)
    Event_12410770(5, character=2410295)
    Event_12410770(6, character=2410296)
    Event_12410809()
    Event_12410810()
    Event_12410811()
    Event_12410831()
    Event_12410833()
    Event_12410834()
    Event_12410835()
    Event_12410812()
    Event_12410813()
    Event_12410814()
    Event_12410510()
    Event_12415750(0, sound_id=2413710, flag=1439, flag_1=70000050, flag_2=9801)
    Event_12415750(1, sound_id=2413711, flag=1439, flag_1=70000051, flag_2=9801)
    Event_12415750(2, sound_id=2413712, flag=1439, flag_1=70000070, flag_2=9802)
    Event_12415750(3, sound_id=2413713, flag=1439, flag_1=70000071, flag_2=9802)
    Event_12415759(0, sound_id=2413714, flag=1439, flag_1=70000140, flag_2=9802)
    Event_12415770(0, obj=2411250, flag=9802, model_point=924110)
    Event_12415770(1, obj=2411251, flag=9802, model_point=924113)
    Event_12415770(2, obj=2411252, flag=9802, model_point=924110)
    Event_12415770(3, obj=2411253, flag=9802, model_point=924113)
    Event_12415779(0, obj=2411254)
    Event_12414100(0, entity=2411000, action_button_id=7400, text=10012000)
    Event_12414100(1, entity=2411001, action_button_id=7401, text=10012001)
    Event_12414100(4, entity=2411004, action_button_id=7404, text=10012004)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    if FlagDisabled(12410000):
        EnableFlag(9180)
        DisableSoundEvent(sound_id=2413900)
    if FlagEnabled(12410998):
        EnableFlag(12410999)
    Event_12410005(0, flag=12410999)
    DisableAnimations(2413950)
    DisableGravity(2413950)
    DisableCharacterCollision(2413950)
    DisableAnimations(2413951)
    DisableGravity(2413951)
    DisableCharacterCollision(2413951)
    DisableAnimations(2413952)
    DisableGravity(2413952)
    DisableCharacterCollision(2413952)
    Event_12410744()
    Event_12410745()
    Event_12410762()
    Event_12410800()
    Event_12410645()
    Event_12410729()
    Event_12410830()
    Event_12410701()
    Event_12410780()
    if FlagEnabled(12411000):
        DisableBackread(2410901)
        DisableBackread(2410740)
        DisableBackread(2410710)
        DisableBackread(2410290)
        DisableBackread(2410291)
        DisableBackread(2410292)
        DisableBackread(2410293)
        DisableBackread(2410294)
        DisableBackread(2410295)
        DisableBackread(2410296)
        DisableBackread(2410781)


@ContinueOnRest(12410000)
def Event_12410000():
    """Event 12410000"""
    if ThisEventFlagEnabled():
        return
    if OutsideMap(game_map=CENTRAL_YHARNAM):
        return
    SkipLinesIfPlayerGender(skip_lines=2, gender=Gender.Male)
    PlayCutscene(24010005, cutscene_flags=CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(24011005, cutscene_flags=CutsceneFlags.FadeOut, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    SetRespawnPoint(respawn_point=2412959)


@ContinueOnRest(12411010)
def Event_12411010():
    """Event 12411010"""
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(7015))

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12417810)


@RestartOnRest(12414000)
def Event_12414000(_, character: int, value: uchar, radius: float):
    """Event 12414000"""
    if ThisEventSlotFlagEnabled():
        return
    DisableCharacter(character)
    AND_1.Add(PlayerInsightAmount() >= value)
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    ForceAnimation(character, 6200, wait_for_completion=True)


@RestartOnRest(12414010)
def Event_12414010(_, character: int, value: uchar, flag: int):
    """Event 12414010"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(PlayerInsightAmount() <= value)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(character)


@ContinueOnRest(12414100)
def Event_12414100(_, entity: int, action_button_id: int, text: int):
    """Event 12414100"""
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=action_button_id, entity=entity))
    
    DisplayDialog(text=text, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12410005)
def Event_12410005(_, flag: int):
    """Event 12410005"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableMapPiece(map_piece_id=2414220)
    DisableObject(2411700)
    DisableObject(2411701)
    DisableObject(2411702)
    DisableObject(2411703)
    DisableObject(2411704)
    DisableObject(2411705)
    DisableObject(2411706)
    DisableObject(2411707)
    DisableObject(2411708)
    DisableObject(2411709)
    DisableObject(2411710)
    DisableObject(2411711)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableMapPiece(map_piece_id=2414220)
    DisableObject(2411316)
    DisableCharacter(2410951)
    DisableCharacter(2410195)
    EnableObject(2411700)
    EnableObject(2411701)
    EnableObject(2411702)
    EnableObject(2411703)
    EnableObject(2411704)
    EnableObject(2411705)
    EnableObject(2411706)
    EnableObject(2411707)
    EnableObject(2411708)
    EnableObject(2411709)
    EnableObject(2411710)
    EnableObject(2411711)
    DisableBackread(2410260)
    DisableBackread(2410261)
    DisableBackread(2410300)
    DisableBackread(2410301)
    DisableBackread(2410302)
    DisableBackread(2410303)
    DisableBackread(2410304)
    DisableBackread(2410305)
    DisableBackread(2410306)
    DisableBackread(2410307)
    DisableBackread(2410308)
    DisableBackread(2410271)
    DisableBackread(2410272)
    DisableBackread(2410275)
    DisableBackread(2410277)
    DisableBackread(2410278)
    DisableBackread(2410279)


@RestartOnRest(12415060)
def Event_12415060(_, character: int, region: int, region_1: int, radius: float):
    """Event 12415060"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_2)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    EnableAI(character)


@RestartOnRest(12415080)
def Event_12415080(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    region: int,
    ai_param_id: int,
    ai_param_id_1: int,
    radius: float,
):
    """Event 12415080"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    DisableGravity(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_2)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    EnableGravity(character)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_3)
    WaitRandomFrames(min_frames=20, max_frames=100)
    AND_4.Add(HealthRatio(character) < 1.0)
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)

    # --- Label 1 --- #
    DefineLabel(1)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@ContinueOnRest(12415020)
def Event_12415020(_, action_button_id: int, anchor_entity: int, flag: int, text: int):
    """Event 12415020"""
    DisableNetworkSync()
    OR_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=anchor_entity))
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(flag):
        return
    DisplayDialog(text=text, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12410200)
def Event_12410200(_, obj: int, obj_1: int, obj_act_id: int):
    """Event 12410200"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=1)
    Wait(1.0)
    DisableObjectActivation(obj_1, obj_act_id=2410000)
    DisableObjectActivation(obj_1, obj_act_id=2410001)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=7100, entity=obj_1))
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    ForceAnimation(obj, 1)
    DisableNetworkSync()
    if ValueEqual(left=obj_1, right=2411314):
        DisplayDialog(text=10010850, anchor_entity=obj_1, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12410100)
def Event_12410100(_, action_button_id: int, anchor_entity: int, flag: int, text: int):
    """Event 12410100"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=anchor_entity))
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    DisplayDialog(text=text, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


@ContinueOnRest(12410110)
def Event_12410110(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 12410110"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    Wait(0.0)


@ContinueOnRest(12410120)
def Event_12410120():
    """Event 12410120"""
    DisableNetworkSync()
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412300))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412301))
    AND_2.Add(FlagEnabled(12410130))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@ContinueOnRest(12410130)
def Event_12410130(_, obj_act_id: int):
    """Event 12410130"""
    DisableNetworkSync()
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    End()


@ContinueOnRest(12410150)
def Event_12410150():
    """Event 12410150"""
    DisableNetworkSync()
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(ObjectActivated(obj_act_id=12411307))
    
    DisplayDialog(
        text=10010850,
        anchor_entity=2411304,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.OneButton,
    )


@ContinueOnRest(12410151)
def Event_12410151():
    """Event 12410151"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(12411800))
    
    if FlagEnabled(12410150):
        return
    if Client():
        return
    AND_1.Add(FlagDisabled(12411000))
    if AND_1:
        return
    DisableObjectActivation(2411304, obj_act_id=2410080)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=7002, entity=2411304))
    
    AND_2.Add(PlayGoState(playgo_state=PlayGoState.DownloadedFirstChunk))
    GotoIfConditionFalse(Label.L0, input_condition=AND_2)
    DisplayDialog(
        text=10010180,
        anchor_entity=2411304,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisplayDialog(
        text=10010181,
        anchor_entity=2411304,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


@RestartOnRest(12410160)
def Event_12410160(_, region: int, anchor_entity: int, sound_type: int, sound_id: int):
    """Event 12410160"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    PlaySoundEffect(anchor_entity, sound_id, sound_type=sound_type)


@RestartOnRest(12410140)
def Event_12410140():
    """Event 12410140"""
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1140, 1144))
    GotoIfFlagEnabled(Label.L1, flag=70000240)
    
    MAIN.Await(ObjectActivated(obj_act_id=12411300))
    
    EnableFlag(70000240)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(obj=2411307, animation_id=2)
    DisableObjectActivation(2411307, obj_act_id=2410010)
    NotifyDoorEventSoundDampening(obj=2411307, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(9401))
    OR_1.Add(FlagEnabled(9800))
    
    MAIN.Await(OR_1)
    
    EndOfAnimation(obj=2411307, animation_id=0)
    EnableObjectActivation(2411307, obj_act_id=2410010)
    NotifyDoorEventSoundDampening(obj=2411307, state=DoorState.DoorClosing)
    DisableFlag(62411300)
    DisableFlag(72410329)
    DisableFlag(72410344)
    DisableFlag(72410345)
    DisableFlag(72410346)


@ContinueOnRest(12410337)
def Event_12410337(_, navmesh_id: int):
    """Event 12410337"""
    MAIN.Await(ObjectActivated(obj_act_id=12411303))
    
    EnableNavmeshType(navmesh_id=navmesh_id, navmesh_type=NavmeshType.Solid)


@RestartOnRest(12415420)
def Event_12415420(_, character: int, region: int, left: int):
    """Event 12415420"""
    if ValueNotEqual(left=left, right=0):
        if FlagEnabled(left):
            return
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterInsideRegion(character, region=region))
    
    MAIN.Await(AND_1)
    
    EnableImmortality(character)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(CharacterInsideRegion(character, region=region))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(character, 5915)
    Kill(character, award_souls=True)


@RestartOnRest(12415430)
def Event_12415430(_, character: int, region: int, seconds: float, radius: float):
    """Event 12415430"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(AttackedWithDamageType(attacked_entity=region, attacker=PLAYER))
    AND_3.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    Wait(seconds)
    EnableAI(character)


@RestartOnRest(12415435)
def Event_12415435(_, character: int, region: int):
    """Event 12415435"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    WaitRandomFrames(min_frames=0, max_frames=10)
    EnableAI(character)


@RestartOnRest(12415460)
def Event_12415460(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    region: int,
    radius: float,
    destination: int,
    entity: int,
):
    """Event 12415460"""
    WaitFrames(frames=10)
    MoveToEntity(character, destination=destination, destination_type=CoordEntityType.Region)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    DisableGravity(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_2)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_3.Add(AND_1)
    OR_3.Add(AND_2)
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    EnableGravity(character)
    ForceAnimation(entity, 1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_3)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest(12415461)
def Event_12415461(_, entity: int, animation_id: int, animation_id_1: int):
    """Event 12415461"""
    GotoIfFlagEnabled(Label.L0, flag=12410170)
    ForceAnimation(entity, animation_id)
    AND_1.Add(CharacterHasTAEEvent(2410019, tae_event_id=10))
    AND_2.Add(FlagEnabled(12410170))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(entity, animation_id_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    Restart()


@ContinueOnRest(12415470)
def Event_12415470(_, character: int, region: int, command_id: int):
    """Event 12415470"""
    if FlagEnabled(12415234):
        return
    DisableAI(character)
    AND_1.Add(HasAIStatus(2410200, ai_status=AIStatusType.Battle))
    AND_1.Add(HasAIStatus(2410201, ai_status=AIStatusType.Battle))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_1)
    AND_3.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=8.0))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    Wait(10.0)
    EnableAI(character)
    WaitFrames(frames=10)
    SetNest(character, region=region)
    AICommand(character, command_id=command_id, command_slot=0)
    ResetAnimation(character, disable_interpolation=True)
    ReplanAI(character)
    OR_1.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12415475)
def Event_12415475(_, character: int, animation_id: int, animation_id_1: int, region: int):
    """Event 12415475"""
    if ThisEventFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_3.Add(FlagEnabled(12415477))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    ForceAnimation(2411202, 0, loop=True)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    End()
    SetNest(character, region=2412051)


@RestartOnRest(12415476)
def Event_12415476(_, attacked_entity: int, animation_id: int):
    """Event 12415476"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    ForceAnimation(2411202, 0, loop=True)
    ForceAnimation(attacked_entity, animation_id, wait_for_completion=True)


@RestartOnRest(12415477)
def Event_12415477(_, character: int):
    """Event 12415477"""
    MAIN.Await(Host())
    
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    DisableFlag(12415477)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    EnableFlag(12415477)
    ForceAnimation(character, 3021, wait_for_completion=True)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    Restart()


@RestartOnRest(12415478)
def Event_12415478(_, character: int):
    """Event 12415478"""
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    AND_2.Add(FlagEnabled(12415475))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    SetObjectDamageShieldState(obj=2411202, state=True)
    ForceAnimation(2411202, 1, loop=True, skip_transition=True)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetObjectDamageShieldState(obj=2411202, state=False)
    ForceAnimation(2411202, 0, loop=True)
    End()


@RestartOnRest(12415479)
def Event_12415479(_, character: int):
    """Event 12415479"""
    AND_1.Add(FlagEnabled(12415475))
    AND_1.Add(FlagEnabled(12415477))
    
    MAIN.Await(AND_1)
    
    SetNest(character, region=2412051)
    
    MAIN.Await(FlagDisabled(12415477))
    
    SetNest(character, region=2412240)
    Restart()


@RestartOnRest(12415480)
def Event_12415480(_, character: int, animation_id: int, animation_id_1: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12415480"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    DisableGravity(character)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(FlagEnabled(12415477))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableGravity(character)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    WaitRandomFrames(min_frames=20, max_frames=100)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(12415498)
def Event_12415498(_, character: int, behavior_id: int):
    """Event 12415498"""
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    WaitRandomFrames(min_frames=0, max_frames=30)
    ForceAnimation(character, 3010, wait_for_completion=True)
    OR_2.Add(FramesElapsed(frames=51))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    ShootProjectile(
        owner_entity=character,
        source_entity=character,
        model_point=7,
        behavior_id=behavior_id,
        launch_angle_x=90,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(character, 7004, wait_for_completion=True)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    Restart()


@ContinueOnRest(12410815)
def Event_12410815():
    """Event 12410815"""
    AddSpecialEffect(2410600, 5686)
    WaitFrames(frames=10)
    OR_1.Add(FlagEnabled(9802))
    OR_1.Add(PlayerInsightAmount() >= 20)
    
    MAIN.Await(OR_1)
    
    SetDisplayMask(2410600, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2410600, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2410600, bit_index=10, switch_type=OnOffChange.Off)
    EnableCharacter(2410600)
    RemoveSpecialEffect(2410600, 5686)
    AND_1.Add(PlayerInsightAmount() <= 18)
    AND_1.Add(FlagDisabled(9802))
    
    MAIN.Await(AND_1)
    
    Restart()


@ContinueOnRest(12410820)
def Event_12410820():
    """Event 12410820"""
    DisableMapCollisionBackreadMask(collision=2414400)
    DisableMapCollisionBackreadMask(collision=2414401)
    DisableMapCollisionBackreadMask(collision=2414402)
    DisableMapCollisionBackreadMask(collision=2414410)
    DisableMapCollisionBackreadMask(collision=2414420)
    DisableMapCollisionBackreadMask(collision=2414421)


@RestartOnRest(12410450)
def Event_12410450(_, character: int, flag: int):
    """Event 12410450"""
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


@ContinueOnRest(12411899)
def Event_12411899():
    """Event 12411899"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(12411800))
    AND_1.Add(FlagEnabled(12411700))
    
    MAIN.Await(AND_1)
    
    EnableFlag(2410)


@ContinueOnRest(12411700)
def Event_12411700():
    """Event 12411700"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2413802)
    DisableSoundEvent(sound_id=2413803)
    DisableCharacter(2410800)
    Kill(2410800)
    DisableObject(2411800)
    DeleteVFX(2413800, erase_root_only=False)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(2410800))
    
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2411800)
    DeleteVFX(2413800)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2410800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(achievement_id=21)
    if FlagDisabled(6645):
        AwardItemLot(50000010, host_only=False)
    EnableFlag(2411)
    EnableFlag(9456)
    StopPlayLogMeasurement(measurement_id=2410000)
    StopPlayLogMeasurement(measurement_id=2410001)
    StopPlayLogMeasurement(measurement_id=2410010)
    CreatePlayLog(name=40)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=52,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterWhitePhantom(PLAYER))
    
    Wait(0.0)


@ContinueOnRest(12411701)
def Event_12411701():
    """Event 12411701"""
    DisableNetworkSync()
    if FlagEnabled(12411700):
        return
    AND_1.Add(FlagEnabled(12411700))
    AND_2.Add(CharacterBackreadDisabled(2410800))
    AND_2.Add(HealthRatio(2410800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    PlaySoundEffect(2412800, 500099999, sound_type=SoundType.c_CharacterMotion)


@ContinueOnRest(12411702)
def Event_12411702():
    """Event 12411702"""
    if FlagEnabled(12411700):
        return
    GotoIfThisEventFlagDisabled(Label.L0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(2410800)
    DisableGravity(2410800)
    DisableCharacterCollision(2410800)
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412805))
    
    MAIN.Await(AND_1)
    
    Move(2410800, destination=2412831, destination_type=CoordEntityType.Region, short_move=True)
    EnableFlag(72410511)
    EnableCharacter(2410800)
    ForceAnimation(2410800, 3028)
    WaitFrames(frames=110)
    EnableGravity(2410800)
    EnableCharacterCollision(2410800)
    EnableFlag(12414700)
    EnableFlag(12414223)
    if FlagEnabled(9300):
        return
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9300)


@ContinueOnRest(12411703)
def Event_12411703():
    """Event 12411703"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12414700))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableCharacter(2410800)
    EnableFlag(12414700)
    EnableFlag(12411702)


@ContinueOnRest(12414730)
def Event_12414730():
    """Event 12414730"""
    if FlagEnabled(12411700):
        return
    GotoIfFlagEnabled(Label.L0, flag=12411702)
    SkipLinesIfClient(2)
    DisableObject(2411800)
    DeleteVFX(2413800, erase_root_only=False)
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(FlagEnabled(12411702))
    
    MAIN.Await(AND_1)
    
    EnableObject(2411800)
    CreateVFX(2413800)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12411700))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2410040, entity=2411800))
    AND_3.Add(FlagEnabled(12411700))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    RotateToFaceEntity(PLAYER, 2412800, animation=101130)
    AND_4.Add(CharacterHuman(PLAYER))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=2412801))
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(TimeElapsed(seconds=2.0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_5)
    EnableFlag(12414700)
    EnableFlag(12414223)
    Restart()


@ContinueOnRest(12414731)
def Event_12414731():
    """Event 12414731"""
    DisableNetworkSync()
    if FlagEnabled(12411700):
        return
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(FlagEnabled(12411702))
    AND_1.Add(FlagEnabled(12414700))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2410040, entity=2411800))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 2412800, animation=101130)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412801))
    AND_3.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    EnableFlag(12414701)
    Restart()


@ContinueOnRest(12414732)
def Event_12414732():
    """Event 12414732"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2411800, radius=4.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12414733)
def Event_12414733():
    """Event 12414733"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2411800, radius=4.0))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2411800, radius=8.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12414702)
def Event_12414702():
    """Event 12414702"""
    if FlagEnabled(12411700):
        return
    DisableAI(2410800)
    DisableHealthBar(2410800)
    GotoIfThisEventFlagEnabled(Label.L0)
    OR_1.Add(FlagEnabled(12414700))
    OR_1.Add(FlagEnabled(12415400))
    
    MAIN.Await(OR_1)
    
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2410800, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12414700)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2410800, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2410800)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2410800, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2410800)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableAI(2410800)
    EnableBossHealthBar(2410800, name=500000)
    CreatePlayLog(name=80)
    StartPlayLogMeasurement(measurement_id=2410010, name=96, overwrite=True)


@ContinueOnRest(12414703)
def Event_12414703():
    """Event 12414703"""
    DisableNetworkSync()
    if FlagEnabled(12411700):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2413802)
    DisableSoundEvent(sound_id=2413803)
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(FlagEnabled(12414702))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(12414701))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412801))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=2413802)
    AND_2.Add(CharacterHasTAEEvent(2410800, tae_event_id=100))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12411700))
    AND_2.Add(FlagEnabled(12414702))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(12414701))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412801))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=2413802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2413803)


@ContinueOnRest(12414704)
def Event_12414704():
    """Event 12414704"""
    DisableNetworkSync()
    if FlagEnabled(12411700):
        return
    AND_1.Add(HealthRatio(2410800) > 0.0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2410800, radius=5.5))
    
    MAIN.Await(AND_1)
    
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=1)
    AND_2.Add(HealthRatio(2410800) > 0.0)
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2410800, radius=6.0))
    
    MAIN.Await(AND_2)
    
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Restart()


@ContinueOnRest(12414705)
def Event_12414705():
    """Event 12414705"""
    DisableNetworkSync()
    if FlagEnabled(12411700):
        return
    
    MAIN.Await(FlagEnabled(12411700))
    
    DisableBossMusic(sound_id=2413802)
    DisableBossMusic(sound_id=2413803)
    DisableBossMusic(sound_id=-1)


@ContinueOnRest(12414707)
def Event_12414707():
    """Event 12414707"""
    if FlagEnabled(12411700):
        return
    
    MAIN.Await(HealthRatio(2410800) < 0.699999988079071)
    
    AICommand(2410800, command_id=1, command_slot=1)
    ReplanAI(2410800)
    
    MAIN.Await(CharacterHasTAEEvent(2410800, tae_event_id=100))
    
    AICommand(2410800, command_id=-1, command_slot=1)
    ReplanAI(2410800)


@ContinueOnRest(12414708)
def Event_12414708():
    """Event 12414708"""
    if FlagEnabled(12411700):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterHasSpecialEffect(2410800, 482))

    # --- Label 0 --- #
    DefineLabel(0)
    ChangeCharacterCloth(2410800, bit_count=15, state_id=2)


@RestartOnRest(12414710)
def Event_12414710(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    special_effect_id: int,
    special_effect_id_1: int,
    animation_id: int,
):
    """Event 12414710"""
    if FlagEnabled(12411700):
        return
    CreateNPCPart(2410800, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(2410800, npc_part_id=npc_part_id_1, material_sfx_id=72, material_vfx_id=72)
    AND_2.Add(CharacterPartHealth(2410800, npc_part_id=npc_part_id_1) <= 0)
    AND_3.Add(HealthRatio(2410800) <= 0.0)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    CreateNPCPart(
        2410800,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(2410800, npc_part_id=npc_part_id_1, material_sfx_id=73, material_vfx_id=73)
    ForceAnimation(2410800, animation_id)
    AddSpecialEffect(2410800, special_effect_id)
    RemoveSpecialEffect(2410800, special_effect_id_1)
    ReplanAI(2410800)
    Wait(30.0)
    AICommand(2410800, command_id=1, command_slot=0)
    ReplanAI(2410800)
    
    MAIN.Await(CharacterHasTAEEvent(2410800, tae_event_id=300))
    
    SetNPCPartHealth(2410800, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(2410800, special_effect_id_1)
    RemoveSpecialEffect(2410800, special_effect_id)
    AICommand(2410800, command_id=-1, command_slot=0)
    ReplanAI(2410800)
    WaitFrames(frames=10)
    Restart()


@ContinueOnRest(12414720)
def Event_12414720(_, special_effect: int, special_effect_1: int, bit_index: uchar, bit_index_1: uchar):
    """Event 12414720"""
    if FlagEnabled(12411700):
        return
    AND_1.Add(CharacterHasSpecialEffect(2410800, special_effect))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(2410800, special_effect_1))
    
    MAIN.Await(AND_1)
    
    SetDisplayMask(2410800, bit_index=bit_index_1, switch_type=OnOffChange.On)
    SetDisplayMask(2410800, bit_index=bit_index, switch_type=OnOffChange.Off)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(2410800, special_effect))
    AND_2.Add(CharacterHasSpecialEffect(2410800, special_effect_1))
    
    MAIN.Await(AND_2)
    
    SetDisplayMask(2410800, bit_index=bit_index, switch_type=OnOffChange.On)
    SetDisplayMask(2410800, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    WaitFrames(frames=10)
    Restart()


@ContinueOnRest(12411800)
def Event_12411800():
    """Event 12411800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2413812)
    DisableSoundEvent(sound_id=2413813)
    DisableCharacter(2410810)
    DisableCharacter(2410811)
    Kill(2410810)
    Kill(2410811)
    DisableObject(2411810)
    DeleteVFX(2413810, erase_root_only=False)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterDead(2410810))
    AND_2.Add(CharacterDead(2410811))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2411810)
    DeleteVFX(2413810)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    KillBoss(game_area_param_id=2410810)
    SkipLines(1)
    KillBoss(game_area_param_id=2410811)
    SetNetworkUpdateRate(2410811, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RunEvent(9350, slot=0, args=(2,))
    AwardAchievement(achievement_id=14)
    AwardItemLot(31000, host_only=False)
    EnableFlag(2412)
    EnableFlag(9457)
    EnableFlag(5910)
    StopPlayLogMeasurement(measurement_id=2410000)
    StopPlayLogMeasurement(measurement_id=2410001)
    StopPlayLogMeasurement(measurement_id=2410010)
    CreatePlayLog(name=40)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=114,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=114,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=114,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=114,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterWhitePhantom(PLAYER))
    
    Wait(0.0)


@ContinueOnRest(12411801)
def Event_12411801():
    """Event 12411801"""
    DisableNetworkSync()
    if FlagEnabled(12411800):
        return
    AND_1.Add(FlagEnabled(12411800))
    AND_2.Add(CharacterBackreadDisabled(2410810))
    AND_2.Add(HealthRatio(2410810) <= 0.0)
    AND_3.Add(CharacterBackreadDisabled(2410811))
    AND_3.Add(HealthRatio(2410811) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    PlaySoundEffect(2412810, 500099999, sound_type=SoundType.c_CharacterMotion)


@ContinueOnRest(12411802)
def Event_12411802():
    """Event 12411802"""
    if FlagEnabled(12411800):
        return
    if ThisEventFlagEnabled():
        return
    DisableCharacter(2410810)
    AND_1.Add(FlagDisabled(12411800))
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412815))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12414223)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_2:
        return
    EnableFlag(9180)
    WaitFrames(frames=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(24010010, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(24010010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    Move(2410810, destination=2412830, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(2410810)
    EnableFlag(12414800)
    if FlagEnabled(9336):
        return
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9336)


@ContinueOnRest(12411803)
def Event_12411803():
    """Event 12411803"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12414800))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableCharacter(2410810)
    EnableFlag(12414800)
    EnableFlag(12411802)


@ContinueOnRest(12414810)
def Event_12414810():
    """Event 12414810"""
    if FlagEnabled(12411800):
        return
    GotoIfFlagEnabled(Label.L0, flag=12411802)
    SkipLinesIfClient(2)
    DisableObject(2411810)
    DeleteVFX(2413810, erase_root_only=False)
    AND_1.Add(FlagDisabled(12411800))
    AND_1.Add(FlagEnabled(12411802))
    
    MAIN.Await(AND_1)
    
    EnableObject(2411810)
    CreateVFX(2413810)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12411800))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2410041, entity=2411810))
    AND_3.Add(FlagEnabled(12411800))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    RotateToFaceEntity(PLAYER, 2412810, animation=101130)
    AND_4.Add(CharacterHuman(PLAYER))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=2412811))
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(TimeElapsed(seconds=2.0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_5)
    EnableFlag(12414800)
    Restart()


@ContinueOnRest(12414811)
def Event_12414811():
    """Event 12414811"""
    DisableNetworkSync()
    if FlagEnabled(12411800):
        return
    AND_1.Add(FlagDisabled(12411800))
    AND_1.Add(FlagEnabled(12411802))
    AND_1.Add(FlagEnabled(12414800))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2410041, entity=2411810))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 2412810, animation=101130)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412811))
    AND_3.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    EnableFlag(12414801)
    Restart()


@ContinueOnRest(12414812)
def Event_12414812():
    """Event 12414812"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2411810, radius=4.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12414813)
def Event_12414813():
    """Event 12414813"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2411810, radius=4.0))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2411810, radius=8.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12414802)
def Event_12414802():
    """Event 12414802"""
    if FlagEnabled(12411800):
        return
    DisableAI(2410810)
    DisableAI(2410811)
    DisableHealthBar(2410810)
    DisableHealthBar(2410811)
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(12414800))
    
    GotoIfClient(Label.L0)
    if FlagDisabled(12414223):
        NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2410810, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2410811, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12414223)
    EnableFlag(12414800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2410810, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2410811, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2410810)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2410811)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2410810, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2410811, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2410810)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2410811)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    ReferDamageToEntity(2410810, target_entity=2410811)
    GotoIfFlagEnabled(Label.L5, flag=12414807)
    EnableAI(2410810)
    EnableBossHealthBar(2410810, name=271000)
    Goto(Label.L6)

    # --- Label 5 --- #
    DefineLabel(5)
    EnableAI(2410811)
    EnableBossHealthBar(2410811, name=272000)

    # --- Label 6 --- #
    DefineLabel(6)
    CreatePlayLog(name=80)
    StartPlayLogMeasurement(measurement_id=2410010, name=96, overwrite=True)


@ContinueOnRest(12414803)
def Event_12414803():
    """Event 12414803"""
    DisableNetworkSync()
    if FlagEnabled(12411800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2413812)
    DisableSoundEvent(sound_id=2413813)
    AND_1.Add(FlagDisabled(12411800))
    AND_1.Add(FlagEnabled(12414802))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(12414801))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412812))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=2413812)
    AND_2.Add(FlagEnabled(12414807))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12411800))
    AND_2.Add(FlagEnabled(12414802))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(12414801))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412812))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=2413812)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2413813)


@ContinueOnRest(12414804)
def Event_12414804():
    """Event 12414804"""
    DisableNetworkSync()
    if FlagEnabled(12411800):
        return
    GotoIfFlagEnabled(Label.L0, flag=12414807)
    AND_1.Add(HealthRatio(2410810) > 0.0)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2410810, radius=5.5))
    
    MAIN.Await(AND_1)
    
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=1)
    AND_2.Add(HealthRatio(2410810) > 0.0)
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2410810, radius=6.0))
    
    MAIN.Await(AND_2)
    
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_3.Add(HealthRatio(2410811) > 0.0)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=2410811, radius=5.5))
    
    MAIN.Await(AND_3)
    
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=1)
    AND_4.Add(HealthRatio(2410811) > 0.0)
    AND_4.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2410811, radius=6.0))
    
    MAIN.Await(AND_4)
    
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Restart()


@ContinueOnRest(12414805)
def Event_12414805():
    """Event 12414805"""
    DisableNetworkSync()
    if FlagEnabled(12411800):
        return
    
    MAIN.Await(FlagEnabled(12411800))
    
    DisableBossMusic(sound_id=2413812)
    DisableBossMusic(sound_id=2413813)
    DisableBossMusic(sound_id=-1)


@ContinueOnRest(12414807)
def Event_12414807():
    """Event 12414807"""
    if FlagEnabled(12411800):
        return
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(2410810)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(2410811)
    AND_1.Add(HealthRatio(2410810) < 0.3400000035762787)
    AND_2.Add(CharacterHasTAEEvent(2410810, tae_event_id=30))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    AICommand(2410810, command_id=40, command_slot=0)
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_2)
    
    MAIN.Await(CharacterHasTAEEvent(2410810, tae_event_id=30))
    
    WaitFrames(frames=5)
    DisableCharacter(2410810)
    EnableGravity(2410811)
    SetNetworkUpdateRate(2410811, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        2410811,
        destination=2410810,
        destination_type=CoordEntityType.Character,
        model_point=203,
        copy_draw_parent=2410810,
    )
    ForceAnimation(2410811, 3030, wait_for_completion=True)
    EnableAI(2410811)
    EnableBossHealthBar(2410811, name=272000)
    if FlagEnabled(9337):
        return
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9337)


@ContinueOnRest(12414808)
def Event_12414808():
    """Event 12414808"""
    AND_1.Add(CharacterHasSpecialEffect(2410810, 4640))
    AND_1.Add(HealthRatio(2410810) >= 0.3400000035762787)
    
    MAIN.Await(AND_1)
    
    AICommand(2410810, command_id=60, command_slot=0)
    ReplanAI(2410810)
    
    MAIN.Await(CharacterHasTAEEvent(2410810, tae_event_id=10))
    
    AICommand(2410810, command_id=-1, command_slot=0)
    ReplanAI(2410810)
    Wait(10.0)
    AND_1.Add(CharacterHasSpecialEffect(2410810, 4640))
    AND_1.Add(HealthRatio(2410810) >= 0.3400000035762787)
    
    MAIN.Await(AND_1)
    
    AICommand(2410810, command_id=60, command_slot=0)
    ReplanAI(2410810)
    
    MAIN.Await(CharacterHasTAEEvent(2410810, tae_event_id=10))
    
    AICommand(2410810, command_id=-1, command_slot=0)
    ReplanAI(2410810)
    Wait(10.0)
    AND_1.Add(CharacterHasSpecialEffect(2410810, 4640))
    AND_1.Add(HealthRatio(2410810) >= 0.3400000035762787)
    
    MAIN.Await(AND_1)
    
    AICommand(2410810, command_id=60, command_slot=0)
    ReplanAI(2410810)
    
    MAIN.Await(CharacterHasTAEEvent(2410810, tae_event_id=10))
    
    AICommand(2410810, command_id=40, command_slot=0)
    ReplanAI(2410810)


@ContinueOnRest(12414809)
def Event_12414809():
    """Event 12414809"""
    MAIN.Await(FlagEnabled(12414807))
    
    Wait(3.0)
    
    MAIN.Await(CharacterHasSpecialEffect(2410811, 4640))
    
    AICommand(2410811, command_id=50, command_slot=0)
    ReplanAI(2410811)
    
    MAIN.Await(CharacterHasTAEEvent(2410811, tae_event_id=20))
    
    AICommand(2410811, command_id=-1, command_slot=0)
    ReplanAI(2410811)


@RestartOnRest(12415225)
def Event_12415225(_, character: int, animation_id: int, radius: float):
    """Event 12415225"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    AND_1.Add(OR_1)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ForceAnimation(character, animation_id)


@RestartOnRest(12415228)
def Event_12415228(_, character: int, animation_id: int, radius: float):
    """Event 12415228"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    EnableAI(character)
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ForceAnimation(character, animation_id)


@RestartOnRest(12415232)
def Event_12415232(_, character: int, region: int):
    """Event 12415232"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(character, region=region)


@RestartOnRest(12415233)
def Event_12415233(_, region: int, character: int, region_1: int):
    """Event 12415233"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(character, region=region_1)


@ContinueOnRest(12415234)
def Event_12415234(_, character: int, character_1: int, character_2: int):
    """Event 12415234"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterDead(character))
    AND_1.Add(CharacterDead(character_1))
    AND_1.Add(CharacterAlive(character_2))
    AND_2.Add(EntityWithinDistance(entity=character_2, other_entity=PLAYER, radius=10.0))
    AND_3.Add(EntityBeyondDistance(entity=character_2, other_entity=PLAYER, radius=10.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=0, radius=0.0))
    
    WaitFrames(frames=10)


@ContinueOnRest(12415236)
def Event_12415236(_, flag: int, character: int, character_1: int, character_2: int, region: int):
    """Event 12415236"""
    AND_15.Add(FlagEnabled(12415236))
    AND_15.Add(Client())
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    DisableCharacter(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_2)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(12415234))
    AND_1.Add(CharacterAlive(character_1))
    AND_1.Add(AllPlayersInsideRegion(region=2412143))
    OR_2.Add(HealthRatio(character) <= 0.5)
    OR_2.Add(TimeElapsed(seconds=40.0))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(12411700):
        return
    EnableFlag(12415236)
    DisableCharacter(character_1)
    EnableCharacter(character_2)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(character_2, authority_level=UpdateAuthority.Forced)
    Wait(1.0)
    SetNest(character_2, region=region)
    AICommand(character_2, command_id=10, command_slot=0)
    ReplanAI(character_2)
    DisableGravity(character_2)
    DisableCharacterCollision(character_2)
    DisableAnimations(character_2)
    OR_3.Add(EntityWithinDistance(entity=character_2, other_entity=2410800, radius=3.0))
    OR_3.Add(CharacterInsideRegion(character_2, region=2412801))
    
    MAIN.Await(OR_3)
    
    AICommand(character_2, command_id=-1, command_slot=0)
    ClearTargetList(character_2)
    ReplanAI(character_2)
    EnableCharacterCollision(character_2)
    EnableAnimations(character_2)
    EnableGravity(character_2)


@RestartOnRest(12415238)
def Event_12415238(_, region: int, character: int, region_1: int, region_2: int, region_3: int):
    """Event 12415238"""
    AND_1.Add(CharacterInsideRegion(character, region=region_1))
    AND_1.Add(AllPlayersInsideRegion(region=region))
    
    MAIN.Await(AND_1)
    
    SetNest(character, region=region_2)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    OR_1.Add(CharacterInsideRegion(character, region=region_3))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12415250)
def Event_12415250(_, character: int, animation_id: int, min_seconds: float, max_seconds: float, region: int):
    """Event 12415250"""
    MAIN.Await(CharacterInsideRegion(character, region=region))
    
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    ForceAnimation(character, animation_id, wait_for_completion=True)
    Restart()


@RestartOnRest(12415255)
def Event_12415255(_, character: int):
    """Event 12415255"""
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character))
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    RestartIfFinishedConditionTrue(input_condition=AND_1)
    AICommand(character, command_id=20, command_slot=0)
    ReplanAI(character)
    Restart()


@RestartOnRest(12415260)
def Event_12415260(
    _,
    character: int,
    region: int,
    radius: float,
    region_1: int,
    region_2: int,
    region_3: int,
    region_4: int,
):
    """Event 12415260"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(character, region=region_4)
    ChangePatrolBehavior(character, patrol_information_id=2413500)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    SetNest(character, region=region_1)
    AICommand(character, command_id=20, command_slot=0)
    AND_2.Add(CharacterInsideRegion(character, region=region_1))
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_3)
    OR_4.Add(CharacterInsideRegion(PLAYER, region=region_2))
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(OR_4)
    
    MAIN.Await(AND_2)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)
    AICommand(character, command_id=-1, command_slot=0)
    OR_4.Add(CharacterHuman(PLAYER))
    OR_4.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_4)
    OR_5.Add(CharacterInsideRegion(PLAYER, region=region_2))
    OR_5.Add(CharacterInsideRegion(PLAYER, region=region_3))
    OR_5.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_3.Add(OR_5)
    
    MAIN.Await(AND_3)
    
    WaitRandomFrames(min_frames=0, max_frames=300)

    # --- Label 1 --- #
    DefineLabel(1)
    SetNest(character, region=region_4)
    AICommand(character, command_id=20, command_slot=0)
    AND_4.Add(CharacterInsideRegion(character, region=region_4))
    OR_6.Add(CharacterHuman(PLAYER))
    OR_6.Add(CharacterWhitePhantom(PLAYER))
    AND_5.Add(OR_6)
    OR_7.Add(CharacterInsideRegion(PLAYER, region=region_3))
    OR_7.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_5.Add(OR_7)
    
    MAIN.Await(AND_5)
    
    AICommand(character, command_id=-1, command_slot=0)
    ChangePatrolBehavior(character, patrol_information_id=2413500)


@RestartOnRest(12415295)
def Event_12415295(_, character: int, region: int, radius: float, region_1: int):
    """Event 12415295"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(character, region=region_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    SetNest(character, region=region_1)
    AICommand(character, command_id=20, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12415300)
def Event_12415300(_, flag: int, character: int, region: int, region_1: int, radius: float):
    """Event 12415300"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_3.Add(OR_2)
    OR_3.Add(AND_2)
    OR_3.Add(AND_3)
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12415305)
def Event_12415305(_, flag: int, character: int, region: int, region_1: int, radius: float, region_2: int):
    """Event 12415305"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(character, region=region_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(OR_2)
    AND_1.Add(AND_2)
    
    MAIN.Await(AND_1)
    
    WaitRandomFrames(min_frames=0, max_frames=30)

    # --- Label 1 --- #
    DefineLabel(1)
    SetNest(character, region=region_2)
    AICommand(character, command_id=20, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12415310)
def Event_12415310(_, flag: int, character: int, region: int, region_1: int, radius: float, patrol_information_id: int):
    """Event 12415310"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_3.Add(OR_2)
    OR_3.Add(AND_2)
    OR_3.Add(AND_3)
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12415315)
def Event_12415315(_, character: int, region: int, radius: float, region_1: int):
    """Event 12415315"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(character, region=region_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    EnableAI(character)
    SetNest(character, region=region_1)


@RestartOnRest(12415320)
def Event_12415320(_, flag: int, character: int, region: int, region_1: int, patrol_information_id: int):
    """Event 12415320"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_1)
    AND_3.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@RestartOnRest(12415325)
def Event_12415325(_, flag: int, character: int, region: int, patrol_information_id: int):
    """Event 12415325"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(flag))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(AND_2)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@RestartOnRest(12415330)
def Event_12415330(_, character: int, region: int, region_1: int, radius: float, region_2: int):
    """Event 12415330"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=region_1))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=region_2))
    AND_5.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_5)
    Wait(10.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)


@RestartOnRest(12415335)
def Event_12415335(_, flag: int, character: int, region: int, region_1: int, patrol_information_id: int):
    """Event 12415335"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_1)
    AND_3.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@RestartOnRest(12415340)
def Event_12415340(_, character: int, region: int, radius: float, region_1: int):
    """Event 12415340"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(character, region=region_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    AND_1.Add(OR_2)
    AND_4.Add(AttackedWithDamageType(attacked_entity=character))
    OR_3.Add(AND_1)
    OR_3.Add(AND_4)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_4)
    AICommand(character, command_id=20, command_slot=0)

    # --- Label 1 --- #
    DefineLabel(1)
    WaitFrames(frames=10)
    SetNest(character, region=region_1)


@RestartOnRest(12415345)
def Event_12415345(
    _,
    flag: int,
    character: int,
    region: int,
    region_1: int,
    radius: float,
    left: int,
    patrol_information_id: int,
):
    """Event 12415345"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(flag))
    AND_2.Add(CharacterInsideRegion(character, region=region))
    AND_3.Add(AttackedWithDamageType(attacked_entity=character))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_4.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_4.Add(OR_2)
    OR_3.Add(AND_2)
    OR_3.Add(AND_3)
    OR_3.Add(AND_4)
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)

    # --- Label 0 --- #
    DefineLabel(0)
    if ValueEqual(left=left, right=0):
        return
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)


@ContinueOnRest(12410286)
def Event_12410286(_, start_climbing_flag: int, stop_climbing_flag: int, obj: int, obj_1: int):
    """Event 12410286"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=2)
    Wait(1.0)
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)
    DisableObjectActivation(obj_1, obj_act_id=2410000)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(obj_1, obj_act_id=2410000)
    ForceAnimation(obj, 2)
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)


@ContinueOnRest(12410290)
def Event_12410290():
    """Event 12410290"""
    DeleteVFX(2413110, erase_root_only=False)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412150))
    
    MAIN.Await(AND_1)
    
    CreateVFX(2413110)


@ContinueOnRest(12415360)
def Event_12415360(_, region: int, entity: int, animation_id: int):
    """Event 12415360"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity, animation_id)


@ContinueOnRest(12415390)
def Event_12415390(_, character: int):
    """Event 12415390"""
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    SetNest(character, region=2412242)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    SetNest(character, region=2412241)
    Restart()


@RestartOnRest(12415700)
def Event_12415700():
    """Event 12415700"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=2410270, other_entity=PLAYER, radius=8.0))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(2410270, patrol_information_id=2413510)
    ReplanAI(2410270)


@RestartOnRest(12415750)
def Event_12415750(_, sound_id: int, flag: int, flag_1: int, flag_2: int):
    """Event 12415750"""
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


@RestartOnRest(12415759)
def Event_12415759(_, sound_id: int, flag: int, flag_1: int, flag_2: int):
    """Event 12415759"""
    DisableSoundEvent(sound_id=sound_id)
    if FlagEnabled(1245):
        return
    if FlagEnabled(1246):
        return
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


@RestartOnRest(12415770)
def Event_12415770(_, obj: int, flag: int, model_point: int):
    """Event 12415770"""
    DeleteObjectVFX(obj)
    if FlagEnabled(flag):
        return
    CreateObjectVFX(obj, vfx_id=200, model_point=model_point)


@RestartOnRest(12415779)
def Event_12415779(_, obj: int):
    """Event 12415779"""
    CreateObjectVFX(obj, vfx_id=200, model_point=924113)
    AND_1.Add(FlagEnabled(1180))
    AND_1.Add(FlagEnabled(1193))
    AND_1.Add(FlagEnabled(1194))
    
    MAIN.Await(AND_1)
    
    DeleteObjectVFX(obj)


@ContinueOnRest(12410900)
def Event_12410900():
    """Event 12410900"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412911))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9403)


@ContinueOnRest(12410310)
def Event_12410310():
    """Event 12410310"""
    GotoIfFlagEnabled(Label.L2, flag=9802)
    GotoIfFlagEnabled(Label.L1, flag=9801)
    GotoIfFlagEnabled(Label.L0, flag=9800)
    EnableMapPiece(map_piece_id=2414010)
    DisableMapPiece(map_piece_id=2414011)
    DisableMapPiece(map_piece_id=2414012)
    DisableMapPiece(map_piece_id=2414013)
    DisableMapPiece(map_piece_id=2414070)
    DisableMapPiece(map_piece_id=2414071)
    DeleteVFX(2413350, erase_root_only=False)
    DeleteVFX(2413380, erase_root_only=False)
    Goto(Label.L3)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableMapPiece(map_piece_id=2414010)
    EnableMapPiece(map_piece_id=2414011)
    DisableMapPiece(map_piece_id=2414012)
    DisableMapPiece(map_piece_id=2414013)
    DisableMapPiece(map_piece_id=2414070)
    DisableMapPiece(map_piece_id=2414071)
    DeleteVFX(2413350, erase_root_only=False)
    DeleteVFX(2413380, erase_root_only=False)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableMapPiece(map_piece_id=2414010)
    DisableMapPiece(map_piece_id=2414011)
    EnableMapPiece(map_piece_id=2414012)
    DisableMapPiece(map_piece_id=2414013)
    DisableMapPiece(map_piece_id=2414050)
    DisableMapPiece(map_piece_id=2414051)
    DeleteVFX(2413300, erase_root_only=False)
    DeleteVFX(2413301, erase_root_only=False)
    DeleteVFX(2413302, erase_root_only=False)
    DeleteVFX(2413303, erase_root_only=False)
    DeleteVFX(2413304, erase_root_only=False)
    DeleteVFX(2413305, erase_root_only=False)
    DeleteVFX(2413380, erase_root_only=False)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableMapPiece(map_piece_id=2414010)
    DisableMapPiece(map_piece_id=2414011)
    DisableMapPiece(map_piece_id=2414012)
    EnableMapPiece(map_piece_id=2414013)
    DisableMapPiece(map_piece_id=2414050)
    DisableMapPiece(map_piece_id=2414051)
    DeleteVFX(2413350, erase_root_only=False)

    # --- Label 3 --- #
    DefineLabel(3)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9800))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9801))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 9802))
    
    MAIN.Await(OR_1)
    
    Restart()


@ContinueOnRest(12410010)
def Event_12410010():
    """Event 12410010"""
    if FlagEnabled(9401):
        return
    DisableSoapstoneMessage(2413601)
    DisableSoapstoneMessage(2413604)


@ContinueOnRest(12410011)
def Event_12410011():
    """Event 12410011"""
    End()
    if ThisEventFlagEnabled():
        return
    DisableSoapstoneMessage(2413603)
    AND_1.Add(CharacterHuman(PLAYER))
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(52410120))
    
    MAIN.Await(AND_1)
    
    EnableSoapstoneMessage(2413603)


@ContinueOnRest(12410012)
def Event_12410012():
    """Event 12410012"""
    if ThisEventFlagEnabled():
        return
    DisableSoapstoneMessage(2413610)
    DisableSoapstoneMessage(2413611)
    
    MAIN.Await(FlagEnabled(9401))
    
    EnableSoapstoneMessage(2413610)
    EnableSoapstoneMessage(2413611)


@RestartOnRest(12410170)
def Event_12410170():
    """Event 12410170"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2410019)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableHealthBar(2410019)
    AddSpecialEffect(2410019, 5617)
    AddSpecialEffect(2410019, 5708)
    Wait(3.0)
    EnableHealthBar(2410019)
    
    MAIN.Await(CharacterDead(2410019))
    
    End()


@RestartOnRest(12415100)
def Event_12415100(_, character: int):
    """Event 12415100"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    ForceAnimation(character, 7000)
    DisableGravity(character)
    OR_1.Add(HasAIStatus(2410019, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(2410019, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=3.0)
    ForceAnimation(character, 7002)
    EnableAI(character)
    EnableGravity(character)


@ContinueOnRest(12410510)
def Event_12410510():
    """Event 12410510"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if ThisEventFlagEnabled():
        return
    GotoIfFlagEnabled(Label.L0, flag=12410511)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2412350))
    
    EnableFlag(12410511)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(2411200, vfx_id=200, model_point=900201)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2410060, entity=2411200))
    
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2410990, host_only=False)
    DeleteObjectVFX(2411200)


@ContinueOnRest(12410030)
def Event_12410030(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    character_1: int,
    ai_param_id: int,
    ai_param_id_1: int,
):
    """Event 12410030"""
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    DisableGravity(character)
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    OR_3.Add(AND_1)
    
    MAIN.Await(OR_3)
    
    EnableGravity(character)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    ForceAnimation(character_1, 3021)
    WaitRandomFrames(min_frames=20, max_frames=70)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ResetAnimation(character)
    ForceAnimation(character, animation_id_1)


@ContinueOnRest(12410040)
def Event_12410040(
    _,
    character: int,
    ai_param_id: int,
    ai_param_id_1: int,
    ai_param_id_2: int,
    character_1: int,
    animation_id: int,
):
    """Event 12410040"""
    SetAIParamID(character, ai_param_id=ai_param_id)
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    ForceAnimation(character_1, animation_id, wait_for_completion=True)
    AND_1.Add(HealthRatio(character_1) == 1.0)
    AND_2.Add(HealthRatio(character_1) < 1.0)
    OR_4.Add(AND_1)
    OR_4.Add(AND_2)
    
    MAIN.Await(OR_4)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    WaitFrames(frames=100)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_2)


@ContinueOnRest(12410050)
def Event_12410050(
    _,
    character: int,
    ai_param_id: int,
    ai_param_id_1: int,
    ai_param_id_2: int,
    character_1: int,
    animation_id: int,
):
    """Event 12410050"""
    SetAIParamID(character, ai_param_id=ai_param_id)
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character_1, animation_id)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    Wait(300.0)
    SetAIParamID(character, ai_param_id=ai_param_id_2)


@RestartOnRest(12415160)
def Event_12415160(_, character: int, animation_id: int, animation_id_1: int):
    """Event 12415160"""
    WaitRandomFrames(min_frames=0, max_frames=50)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    DisableGravity(character)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    EnableGravity(character)
    WaitRandomFrames(min_frames=0, max_frames=30)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)


@RestartOnRest(12410600)
def Event_12410600(_, obj_act_id: int, obj: int, obj_act_id_1: int):
    """Event 12410600"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=0)
        DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
        EnableTreasure(obj=obj)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(12410630)
def Event_12410630(_, character: int, item_lot: int):
    """Event 12410630"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(character))
    
    AwardItemLot(item_lot, host_only=False)


@RestartOnRest(12410645)
def Event_12410645():
    """Event 12410645"""
    EnableImmortality(2410703)
    DisableHealthBar(2410703)
    AND_10.Add(FlagEnabled(1140))
    GotoIfConditionFalse(Label.L9, input_condition=AND_10)
    DisableBackread(2410703)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_1.Add(FlagEnabled(1141))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    EnableBackread(2410710)
    DisableBackread(2410711)
    DisableAnimations(2410710)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagEnabled(1142))
    GotoIfConditionFalse(Label.L7, input_condition=AND_2)
    EnableBackread(2410710)
    DisableBackread(2410711)
    DisableAnimations(2410710)

    # --- Label 7 --- #
    DefineLabel(7)
    AND_8.Add(FlagEnabled(1143))
    GotoIfConditionFalse(Label.L8, input_condition=AND_8)
    EnableBackread(2410710)
    DisableBackread(2410711)

    # --- Label 8 --- #
    DefineLabel(8)
    AND_9.Add(FlagEnabled(1144))
    GotoIfConditionFalse(Label.L1, input_condition=AND_9)
    EnableBackread(2410710)
    DisableBackread(2410711)
    DisableAnimations(2410710)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(FlagEnabled(1145))
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    DisableBackread(2410703)
    EnableBackread(2410710)
    DisableBackread(2410711)
    Move(2410710, destination=2412172, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SetNest(2410710, region=2412172)
    SetTeamType(2410710, TeamType.Enemy1)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_4.Add(FlagEnabled(1146))
    GotoIfConditionFalse(Label.L3, input_condition=AND_4)
    DisableBackread(2410703)
    DisableBackread(2410710)
    EnableBackread(2410711)
    ForceAnimation(2410711, 103000)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_5.Add(FlagEnabled(1147))
    GotoIfConditionFalse(Label.L4, input_condition=AND_5)
    DisableBackread(2410703)
    DisableBackread(2410710)
    DisableBackread(2410711)
    DisableBackread(2410703)

    # --- Label 4 --- #
    DefineLabel(4)
    AND_6.Add(FlagEnabled(1148))
    GotoIfConditionFalse(Label.L5, input_condition=AND_6)
    DisableBackread(2410703)
    DisableBackread(2410710)
    DisableBackread(2410711)
    Move(2410710, destination=2412172, destination_type=CoordEntityType.Region, set_draw_parent=0)
    WaitFrames(frames=1)
    DropMandatoryTreasure(2410710)

    # --- Label 5 --- #
    DefineLabel(5)
    AND_7.Add(FlagEnabled(1149))
    if not AND_7:
        return
    DisableBackread(2410703)
    DisableBackread(2410710)
    EnableBackread(2410711)
    EzstateAIRequest(2410711, command_id=0, command_slot=1)
    DropMandatoryTreasure(2410711)


@RestartOnRest(12410650)
def Event_12410650():
    """Event 12410650"""

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagRangeAllDisabled(flag_range=(1141, 1159)))
    
    DisableBackread(2410710)
    DisableFlagRange((1140, 1159))
    EnableFlag(1140)


@RestartOnRest(12410651)
def Event_12410651():
    """Event 12410651"""
    if FlagEnabled(1148):
        return
    if FlagEnabled(1149):
        return
    if FlagEnabled(1141):
        return
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(9800))
    
    EnableBackread(2410703)
    EnableBackread(2410710)
    DisableAnimations(2410710)
    DisableFlagRange((1140, 1159))
    EnableFlag(1141)


@RestartOnRest(12410652)
def Event_12410652():
    """Event 12410652"""
    if FlagEnabled(1148):
        return
    if FlagEnabled(1149):
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(72410320))
    AND_1.Add(FlagEnabled(1141))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1140, 1159))
    EnableFlag(1142)


@RestartOnRest(12410653)
def Event_12410653():
    """Event 12410653"""
    if FlagEnabled(1148):
        return
    if FlagEnabled(1149):
        return
    if FlagEnabled(1145):
        return
    if FlagEnabled(1146):
        return
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412170))
    AND_1.Add(FlagDisabled(1140))
    AND_1.Add(FlagDisabled(1145))
    AND_1.Add(FlagDisabled(1146))
    AND_1.Add(FlagDisabled(1147))
    AND_1.Add(FlagDisabled(1148))
    AND_1.Add(FlagDisabled(1149))
    AND_1.Add(CharacterAlive(2410710))
    
    MAIN.Await(AND_1)
    
    SetDistanceLimitForConversationStateChanges(character=2410710, distance=40.5)
    DisableFlagRange((1140, 1159))
    EnableFlag(1143)
    Restart()


@RestartOnRest(12410654)
def Event_12410654():
    """Event 12410654"""
    if FlagEnabled(1148):
        return
    if FlagEnabled(1149):
        return
    if FlagEnabled(1145):
        return
    if FlagEnabled(1146):
        return
    AND_1.Add(FlagEnabled(1143))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412171))
    
    MAIN.Await(AND_1)
    
    SetDistanceLimitForConversationStateChanges(character=2410710, distance=17.0)
    DisableFlagRange((1140, 1159))
    EnableFlag(1144)
    Restart()


@RestartOnRest(12410655)
def Event_12410655():
    """Event 12410655"""
    if FlagEnabled(1148):
        return
    if FlagEnabled(1149):
        return

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2410710)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412190))
    AND_1.Add(FlagDisabled(1140))
    AND_1.Add(FlagDisabled(1146))
    AND_1.Add(FlagDisabled(1147))
    AND_1.Add(FlagDisabled(1148))
    AND_1.Add(FlagDisabled(1149))
    
    MAIN.Await(AND_1)
    
    EnableAI(2410710)
    SetTeamType(2410710, TeamType.Enemy1)
    DisableFlagRange((1140, 1159))
    EnableFlag(1145)
    SaveRequest()


@RestartOnRest(12410656)
def Event_12410656():
    """Event 12410656"""
    if FlagEnabled(1148):
        return
    if FlagEnabled(1149):
        return
    AND_1.Add(FlagEnabled(9802))
    AND_1.Add(CharacterAlive(2410710))
    
    MAIN.Await(AND_1)
    
    DisableBackread(2410703)
    DisableBackread(2410710)
    EnableBackread(2410711)
    ForceAnimation(2410711, 103000)
    EnableAnimations(2410711)
    DisableFlagRange((1140, 1159))
    EnableFlag(1146)


@RestartOnRest(12410657)
def Event_12410657():
    """Event 12410657"""
    if FlagEnabled(1148):
        return
    if FlagEnabled(1149):
        return
    if FlagEnabled(1147):
        return
    
    MAIN.Await(FlagEnabled(72410326))
    
    DisableBackread(2410703)
    DisableFlagRange((1140, 1159))
    EnableFlag(1147)
    SaveRequest()


@RestartOnRest(12410658)
def Event_12410658():
    """Event 12410658"""
    if FlagEnabled(1149):
        return
    AND_1.Add(HealthRatio(2410710) <= 0.0)
    AND_1.Add(FlagEnabled(1145))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1140, 1159))
    EnableFlag(1148)
    SaveRequest()


@RestartOnRest(12410659)
def Event_12410659():
    """Event 12410659"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412170))
    AND_1.Add(FlagEnabled(1143))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412171))
    AND_2.Add(FlagDisabled(62411300))
    AND_2.Add(FlagEnabled(1144))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=2412171))
    AND_3.Add(FlagEnabled(1147))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_3)
    Move(2410710, destination=2412172, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SetNest(2410710, region=2412172)
    EnableFlag(72410337)
    EnableAnimations(2410710)
    DisableBackread(2410703)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(2410710, destination=2412173, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SetNest(2410710, region=2412173)
    DisableFlag(72410337)
    DisableAnimations(2410710)
    EnableBackread(2410703)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableBackread(2410710)


@RestartOnRest(12410661)
def Event_12410661():
    """Event 12410661"""
    MAIN.Await(EventValue(flag=12410646, bit_count=4) >= 4)
    
    EnableFlag(72410328)


@RestartOnRest(12410662)
def Event_12410662(_, flag: int, flag_1: int, flag_2: int):
    """Event 12410662"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(1142))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(1144))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionFalse(Label.L0, input_condition=AND_1)
    IncrementEventValue(12410646, bit_count=4, max_value=10)
    EnableFlag(flag_2)
    DisableFlagRange((72410331, 72410332))
    EnableFlag(flag_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    IncrementEventValue(12410646, bit_count=4, max_value=10)
    EnableFlag(flag_2)
    DisableFlagRange((72410331, 72410332))
    EnableFlag(72410334)


@RestartOnRest(12410668)
def Event_12410668():
    """Event 12410668"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(1163))
    AND_1.Add(FlagEnabled(1204))
    AND_1.Add(FlagEnabled(1268))
    AND_1.Add(FlagEnabled(1190))
    AND_1.Add(FlagEnabled(1223))
    AND_1.Add(FlagEnabled(1309))
    AND_1.Add(FlagEnabled(72410336))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((72410331, 72410332))
    EnableFlag(72410333)


@RestartOnRest(12410669)
def Event_12410669(_, character: int, flag: int, animation_id: int):
    """Event 12410669"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EnableCharacter(character)
    WaitFrames(frames=1)
    ForceAnimation(character, animation_id, loop=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableCharacter(character)
    WaitFrames(frames=1)
    ForceAnimation(character, animation_id, loop=True)


@RestartOnRest(12410676)
def Event_12410676():
    """Event 12410676"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(AttackedWithDamageType(attacked_entity=2410703, attacker=PLAYER))
    OR_1.Add(FlagEnabled(1141))
    OR_1.Add(FlagEnabled(1142))
    OR_1.Add(FlagEnabled(1144))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagRangeAllEnabled(Label.L0, flag_range=(72410344, 72410346))
    GotoIfFlagDisabled(Label.L3, flag=72410320)
    GotoIfFlagDisabled(Label.L2, flag=72410344)
    GotoIfFlagDisabled(Label.L1, flag=72410345)
    EnableFlag(72410346)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(72410345)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(72410344)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableFlag(72410329)
    
    MAIN.Await(FlagDisabled(72410329))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(72410329)
    SaveRequest()


@ContinueOnRest(12410677)
def Event_12410677():
    """Event 12410677"""
    if FlagEnabled(1148):
        return
    if FlagEnabled(1149):
        return
    AND_1.Add(FlagEnabled(1146))
    AND_1.Add(Attacked(attacked_entity=2410711, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2410711, 103001)
    Kill(2410711, award_souls=True)
    DisableFlagRange((1140, 1159))
    EnableFlag(1149)
    SaveRequest()


@ContinueOnRest(12410680)
def Event_12410680(_, character: int):
    """Event 12410680"""
    MAIN.Await(Attacked(attacked_entity=character, attacker=PLAYER))
    
    SetAIParamID(character, ai_param_id=250000)


@ContinueOnRest(12410687)
def Event_12410687(_, flag: int, flag_1: int):
    """Event 12410687"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    RunEvent(9350, slot=0, args=(1,))


@ContinueOnRest(12410693)
def Event_12410693(_, flag: int, flag_1: int):
    """Event 12410693"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag_1))
    
    RunEvent(9350, slot=0, args=(2,))


@ContinueOnRest(12410700)
def Event_12410700():
    """Event 12410700"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=2412174))
    
    MAIN.Await(AND_1)
    
    DisableFlag(12410700)
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412174))
    
    MAIN.Await(AND_1)
    
    Restart()


@ContinueOnRest(12410701)
def Event_12410701():
    """Event 12410701"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_9.Add(FlagEnabled(1261))
    AND_9.Add(FlagEnabled(9800))
    GotoIfConditionFalse(Label.L8, input_condition=AND_9)
    DisableFlagRange((1260, 1279))
    EnableFlag(1262)

    # --- Label 8 --- #
    DefineLabel(8)
    AND_1.Add(FlagEnabled(1260))
    AND_1.Add(FlagEnabled(9801))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableFlagRange((1260, 1279))
    EnableFlag(1270)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(1260))
    OR_1.Add(FlagEnabled(1261))
    OR_1.Add(FlagEnabled(1262))
    AND_2.Add(OR_1)
    AND_2.Add(FlagEnabled(9801))
    GotoIfConditionFalse(Label.L9, input_condition=AND_2)
    DisableFlagRange((1260, 1279))
    EnableFlag(1263)

    # --- Label 9 --- #
    DefineLabel(9)
    AND_10.Add(FlagEnabled(1263))
    OR_3.Add(FlagEnabled(9802))
    OR_3.Add(FlagEnabled(72410407))
    AND_10.Add(OR_3)
    GotoIfConditionFalse(Label.L1, input_condition=AND_10)
    DisableFlagRange((1260, 1279))
    EnableFlag(1269)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(FlagEnabled(1264))
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    DisableFlagRange((1260, 1279))
    EnableFlag(1267)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_4.Add(FlagEnabled(1265))
    GotoIfConditionFalse(Label.L3, input_condition=AND_4)
    DisableFlagRange((1260, 1279))
    EnableFlag(1267)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_5.Add(FlagEnabled(1266))
    GotoIfConditionFalse(Label.L4, input_condition=AND_5)
    DisableFlagRange((1260, 1279))
    EnableFlag(1268)

    # --- Label 4 --- #
    DefineLabel(4)
    AND_6.Add(FlagEnabled(1270))
    OR_2.Add(FlagEnabled(9802))
    OR_2.Add(FlagEnabled(72410415))
    AND_6.Add(OR_2)
    GotoIfConditionFalse(Label.L7, input_condition=AND_6)
    DisableFlagRange((1260, 1279))
    EnableFlag(1269)

    # --- Label 7 --- #
    DefineLabel(7)
    AND_12.Add(FlagEnabled(9802))
    OR_4.Add(FlagEnabled(1267))
    AND_12.Add(OR_4)
    GotoIfConditionFalse(Label.L5, input_condition=AND_12)
    DisableFlagRange((1260, 1279))
    EnableFlag(1271)

    # --- Label 5 --- #
    DefineLabel(5)
    AND_7.Add(FlagEnabled(1272))
    GotoIfConditionFalse(Label.L6, input_condition=AND_7)
    DisableFlagRange((1260, 1279))
    EnableFlag(1273)

    # --- Label 6 --- #
    DefineLabel(6)


@ContinueOnRest(12410702)
def Event_12410702():
    """Event 12410702"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    DisableFlag(72410414)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(2410761)
    DisableHealthBar(2410762)
    EnableImmortality(2410762)
    GotoIfFlagEnabled(Label.L1, flag=1273)
    DisableObject(2410851)
    DisableTreasure(obj=2410851)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableObject(2410851)
    EnableTreasure(obj=2410851)
    PostDestruction(2410852)
    End()


@ContinueOnRest(12410703)
def Event_12410703():
    """Event 12410703"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(12411802))
    AND_1.Add(FlagEnabled(1260))
    AND_1.Add(FlagEnabled(72410413))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1260, 1279))
    EnableFlag(1261)


@ContinueOnRest(12410704)
def Event_12410704():
    """Event 12410704"""
    MAIN.Await(FlagEnabled(72410403))
    
    DisableFlag(72410403)
    DisableFlagRange((1260, 1279))
    EnableFlag(1264)


@ContinueOnRest(12410705)
def Event_12410705():
    """Event 12410705"""
    MAIN.Await(FlagEnabled(72410404))
    
    DisableFlag(72410404)
    DisableFlagRange((1260, 1279))
    EnableFlag(1265)


@ContinueOnRest(12410706)
def Event_12410706():
    """Event 12410706"""
    MAIN.Await(FlagEnabled(72410405))
    
    DisableFlag(72410405)
    DisableFlagRange((1260, 1279))
    EnableFlag(1266)


@ContinueOnRest(12410710)
def Event_12410710():
    """Event 12410710"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    DisableFlag(72410406)
    DisableHealthBar(2410762)
    
    MAIN.Await(Attacked(attacked_entity=2410762, attacker=PLAYER))
    
    EnableFlag(72410406)
    Wait(2.0)
    Restart()


@ContinueOnRest(12410713)
def Event_12410713():
    """Event 12410713"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    EnableFlag(72410410)
    OR_1.Add(FlagEnabled(1271))
    OR_1.Add(FlagEnabled(1267))
    
    MAIN.Await(OR_1)
    
    AND_1.Add(PlayerDoesNotHaveGood(4904))
    
    MAIN.Await(AND_1)
    
    DisableFlag(72410410)


@ContinueOnRest(12410715)
def Event_12410715():
    """Event 12410715"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagDisabled(Label.L0, flag=1269)
    DisableSoundEvent(sound_id=2413100)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, flag=72410402)
    DisableSoundEvent(sound_id=2413100)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableSoundEvent(sound_id=2413100)
    DisableFlag(72410412)
    AND_1.Add(FlagDisabled(1270))
    AND_1.Add(FlagEnabled(72410412))
    
    MAIN.Await(AND_1)
    
    DisableSoundEvent(sound_id=2413100)


@ContinueOnRest(12410716)
def Event_12410716():
    """Event 12410716"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=1267)
    GotoIfFlagEnabled(Label.L1, flag=1268)
    GotoIfFlagEnabled(Label.L1, flag=1269)
    GotoIfFlagEnabled(Label.L1, flag=1273)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DeleteVFX(2413701, erase_root_only=False)


@ContinueOnRest(12410721)
def Event_12410721():
    """Event 12410721"""
    MAIN.Await(FlagEnabled(72410421))
    
    DisableFlag(72410421)
    DisableFlagRange((1260, 1279))
    EnableFlag(1272)


@RestartOnRest(12410729)
def Event_12410729():
    """Event 12410729"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    EnableImmortality(2410702)
    DisableHealthBar(2410702)
    AND_1.Add(FlagEnabled(1120))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableBackread(2410702)
    DisableCharacter(2410700)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagEnabled(1121))
    GotoIfConditionFalse(Label.L1, input_condition=AND_2)
    EnableBackread(2410702)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(FlagEnabled(1122))
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    EnableBackread(2410702)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_4.Add(FlagEnabled(1123))
    GotoIfConditionFalse(Label.L3, input_condition=AND_4)
    DisableBackread(2410702)
    DisableBackread(2410700)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_5.Add(FlagEnabled(1124))
    if not AND_5:
        return
    DisableBackread(2410702)
    DisableBackread(2410700)


@RestartOnRest(12410730)
def Event_12410730():
    """Event 12410730"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(9401))
    AND_1.Add(FlagEnabled(1120))
    
    MAIN.Await(AND_1)
    
    EnableBackread(2410702)
    DisableFlagRange((1120, 1124))
    EnableFlag(1121)


@RestartOnRest(12410731)
def Event_12410731():
    """Event 12410731"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(72410305))
    AND_1.Add(FlagEnabled(1121))
    AND_2.Add(FlagEnabled(1123))
    AND_3.Add(FlagEnabled(1124))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionFalse(input_condition=AND_1)
    DisableFlagRange((1120, 1124))
    EnableFlag(1122)


@RestartOnRest(12410732)
def Event_12410732():
    """Event 12410732"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(72410309))
    OR_2.Add(FlagEnabled(1121))
    OR_2.Add(FlagEnabled(1122))
    AND_1.Add(OR_2)
    AND_2.Add(FlagEnabled(1123))
    AND_3.Add(FlagEnabled(1124))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionFalse(input_condition=AND_1)
    DisableBackread(2410702)
    DisableFlagRange((1120, 1124))
    EnableFlag(1123)


@RestartOnRest(12410733)
def Event_12410733():
    """Event 12410733"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(9800))
    
    DisableFlagRange((1120, 1124))
    EnableFlag(1124)
    DisableCharacter(2410700)
    DisableBackread(2410702)


@RestartOnRest(12410734)
def Event_12410734():
    """Event 12410734"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(Attacked(attacked_entity=2410702, attacker=PLAYER))
    
    EnableFlag(72410306)
    Wait(2.0)
    Restart()


@ContinueOnRest(12410736)
def Event_12410736():
    """Event 12410736"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(72410301))
    AND_2.Add(FlagDisabled(72410301))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    DisableFlag(72410301)


@ContinueOnRest(12410737)
def Event_12410737():
    """Event 12410737"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    DisableCharacter(2410700)
    OR_1.Add(FlagEnabled(1121))
    OR_1.Add(FlagEnabled(1122))
    OR_1.Add(FlagEnabled(1123))
    
    MAIN.Await(OR_1)
    
    EnableCharacter(2410700)
    DisableAnimations(2410700)


@ContinueOnRest(12410738)
def Event_12410738():
    """Event 12410738"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagEnabled(Label.L0, flag=72410311)
    AND_1.Add(CharacterBackreadDisabled(2410700))
    AND_1.Add(FlagEnabled(72410311))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlag(72410311)
    Restart()


@ContinueOnRest(12410739)
def Event_12410739():
    """Event 12410739"""
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412170))
    OR_3.Add(FlagEnabled(1143))
    OR_3.Add(FlagRangeAnyEnabled(flag_range=(1145, 1149)))
    AND_1.Add(OR_3)
    AND_1.Add(FlagEnabled(9800))
    AND_1.Add(CharacterBackreadDisabled(2410290))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412171))
    AND_2.Add(FlagDisabled(62411300))
    AND_2.Add(FlagEnabled(1144))
    AND_2.Add(FlagEnabled(9800))
    AND_2.Add(CharacterBackreadEnabled(2410290))
    OR_2.Add(FlagEnabled(1141))
    OR_2.Add(FlagEnabled(1142))
    AND_3.Add(OR_2)
    AND_3.Add(CharacterBackreadEnabled(2410290))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionFalse(Label.L0, input_condition=AND_1)
    EnableBackread(2410290)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBackread(2410290)
    Restart()


@ContinueOnRest(12410740)
def Event_12410740():
    """Event 12410740"""
    if Client():
        return
    GotoIfFlagEnabled(Label.L1, flag=1180)
    End()

    # --- Label 1 --- #
    DefineLabel(1)


@ContinueOnRest(12410741)
def Event_12410741():
    """Event 12410741"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(1180))
    AND_1.Add(FlagEnabled(9802))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1180, 1199))
    EnableFlag(1195)
    SaveRequest()


@ContinueOnRest(12410742)
def Event_12410742():
    """Event 12410742"""
    MAIN.Await(FlagEnabled(72410390))
    
    DisableFlag(72410390)
    DisableFlagRange((1180, 1199))
    EnableFlag(1193)


@ContinueOnRest(12410743)
def Event_12410743():
    """Event 12410743"""
    MAIN.Await(FlagEnabled(72410391))
    
    DisableFlag(72410391)
    DisableFlagRange((1180, 1199))
    EnableFlag(1194)


@ContinueOnRest(12410744)
def Event_12410744():
    """Event 12410744"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagEnabled(Label.L0, flag=1193)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlagRange((1180, 1199))
    EnableFlag(1181)


@ContinueOnRest(12410745)
def Event_12410745():
    """Event 12410745"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagEnabled(Label.L0, flag=1194)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlagRange((1180, 1199))
    EnableFlag(1190)


@ContinueOnRest(12410746)
def Event_12410746():
    """Event 12410746"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagEnabled(Label.L0, flag=72410382)
    GotoIfFlagEnabled(Label.L0, flag=9802)
    DisableAI(2410111)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBackread(2410111)


@ContinueOnRest(12410747)
def Event_12410747():
    """Event 12410747"""
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2410111, radius=3.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2410111))
    
    MAIN.Await(OR_1)
    
    EnableAI(2410111)


@ContinueOnRest(12410748)
def Event_12410748():
    """Event 12410748"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    DisableFlag(72410393)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412280))
    AND_1.Add(CharacterDead(2410111))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=30)
    EnableFlag(72410393)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=2412280))
    
    DisableFlag(72410393)
    Restart()


@ContinueOnRest(12410749)
def Event_12410749():
    """Event 12410749"""
    MAIN.Await(CharacterBackreadEnabled(2410111))
    
    OR_1.Add(HasAIStatus(2410111, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(2410111, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(2410111, ai_status=AIStatusType.Battle))
    GotoIfConditionFalse(Label.L0, input_condition=OR_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2410111, 3023, wait_for_completion=True)
    
    MAIN.Await(RandomFramesElapsed(min_frames=30, max_frames=60))
    
    Restart()


@ContinueOnRest(12410750)
def Event_12410750(_, flag: int, action_button_id: int, destination: int):
    """Event 12410750"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(72410382))
    
    DisableFlag(flag)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=destination))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=210, short_move=True)
    ForceAnimation(PLAYER, 101320)
    WaitFrames(frames=25)
    WaitFrames(frames=20)
    EnableFlag(flag)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(12410760)
def Event_12410760():
    """Event 12410760"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    DisableFlag(72410513)
    DisableFlag(72410514)
    DisableFlag(72410515)
    DisableFlag(72410516)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableHealthBar(2410782)
    EnableImmortality(2410782)
    GotoIfFlagEnabled(Label.L1, flag=1240)
    GotoIfFlagEnabled(Label.L1, flag=1241)
    GotoIfFlagEnabled(Label.L1, flag=1242)
    GotoIfFlagEnabled(Label.L1, flag=1243)
    GotoIfFlagEnabled(Label.L1, flag=1244)
    GotoIfFlagEnabled(Label.L2, flag=1246)
    GotoIfFlagEnabled(Label.L3, flag=1245)
    DisableBackread(2410781)
    DeleteVFX(2413700, erase_root_only=False)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableBackread(2410781)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(2410781)
    DestroyObject(2410784)
    DeleteVFX(2413700, erase_root_only=False)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(2410781)
    DestroyObject(2410784)
    DeleteVFX(2413700, erase_root_only=False)
    DropMandatoryTreasure(2410781)
    End()


@ContinueOnRest(12410761)
def Event_12410761():
    """Event 12410761"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterDead(2410781))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1240, 1259))
    EnableFlag(1245)
    SaveRequest()


@ContinueOnRest(12410762)
def Event_12410762():
    """Event 12410762"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1245):
        return
    OR_1.Add(FlagEnabled(9800))
    OR_1.Add(FlagEnabled(9801))
    OR_1.Add(FlagEnabled(9802))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(1240))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlagRange((1240, 1259))
    EnableFlag(1241)

    # --- Label 1 --- #
    DefineLabel(1)
    OR_2.Add(FlagEnabled(9801))
    OR_2.Add(FlagEnabled(9802))
    AND_2.Add(OR_2)
    AND_2.Add(FlagEnabled(1241))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    Goto(Label.L3)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableFlagRange((1240, 1259))
    EnableFlag(1242)

    # --- Label 3 --- #
    DefineLabel(3)
    AND_3.Add(FlagEnabled(1242))
    AND_3.Add(FlagEnabled(72410504))
    OR_3.Add(AND_3)
    OR_3.Add(FlagEnabled(9802))
    GotoIfConditionTrue(Label.L4, input_condition=OR_3)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    DisableFlagRange((1240, 1259))
    EnableFlag(1243)

    # --- Label 5 --- #
    DefineLabel(5)
    AND_4.Add(FlagEnabled(9802))
    AND_4.Add(FlagEnabled(1243))
    GotoIfConditionTrue(Label.L6, input_condition=AND_4)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableFlagRange((1240, 1259))
    EnableFlag(1246)


@ContinueOnRest(12410763)
def Event_12410763():
    """Event 12410763"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=2410782))
    OR_1.Add(FlagEnabled(1240))
    OR_1.Add(FlagEnabled(1241))
    OR_1.Add(FlagEnabled(1242))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagRangeAllEnabled(Label.L0, flag_range=(72410515, 72410516))
    GotoIfFlagDisabled(Label.L2, flag=72410500)
    GotoIfFlagDisabled(Label.L1, flag=72410515)
    EnableFlag(72410516)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(72410515)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(72410513)
    
    MAIN.Await(FlagEnabled(72410514))
    
    MAIN.Await(FlagDisabled(72410514))
    
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(72410513)
    DisableFlagRange((1240, 1259))
    EnableFlag(1244)
    SaveRequest()


@ContinueOnRest(12410770)
def Event_12410770(_, character: int):
    """Event 12410770"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character))
    
    WaitFrames(frames=1)


@RestartOnRest(12410780)
def Event_12410780():
    """Event 12410780"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1293):
        return
    GotoIfFlagEnabled(Label.L0, flag=12410785)
    DisableFlagRange((1280, 1299))
    EnableFlag(1290)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableFlagRange((1280, 1299))
    EnableFlag(1291)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    SetDistanceLimitForConversationStateChanges(character=2410810, distance=80.0)
    End()


@RestartOnRest(12410785)
def Event_12410785():
    """Event 12410785"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1293):
        return
    AND_1.Add(FlagEnabled(1290))
    AND_1.Add(FlagEnabled(72410530))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1280, 1299))
    EnableFlag(1291)


@RestartOnRest(12410786)
def Event_12410786():
    """Event 12410786"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1293):
        return
    OR_1.Add(FlagEnabled(1290))
    OR_1.Add(FlagEnabled(1291))
    AND_1.Add(FlagEnabled(12414807))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1290, 1299))
    EnableFlag(1292)


@RestartOnRest(12410787)
def Event_12410787():
    """Event 12410787"""
    if ThisEventFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(12411800))
    
    DisableFlagRange((1290, 1299))
    EnableFlag(1293)
    SetDistanceLimitForConversationStateChanges(character=2410810, distance=17.0)
    SaveRequest()


@ContinueOnRest(12410800)
def Event_12410800():
    """Event 12410800"""
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1370, 1375))
    GotoIfFlagEnabled(Label.L1, flag=1369)
    GotoIfFlagEnabled(Label.L2, flag=1368)
    GotoIfFlagEnabled(Label.L3, flag=1367)
    GotoIfFlagEnabled(Label.L4, flag=1366)
    GotoIfFlagEnabled(Label.L5, flag=1365)
    GotoIfFlagEnabled(Label.L6, flag=1364)
    GotoIfFlagRangeAnyEnabled(Label.L7, flag_range=(1362, 1363))
    GotoIfFlagRangeAnyEnabled(Label.L8, flag_range=(1360, 1361))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBackread(2410900)
    Goto(Label.L9)

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(1705):
        DisableBackread(2410900)
        Goto(Label.L9)
    if FlagEnabled(1704):
        DisableBackread(2410900)
        Goto(Label.L9)
    if FlagEnabled(1701):
        DisableBackread(2410900)
        Goto(Label.L9)
    if FlagEnabled(1703):
        Move(2410900, destination=2412334, destination_type=CoordEntityType.Region, set_draw_parent=2414124)
        SetNest(2410900, region=2412334)
        SetTeamType(2410900, TeamType.HostileNPC)
        Goto(Label.L9)
    if FlagEnabled(1702):
        Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, set_draw_parent=2414122)
        SetNest(2410900, region=2412332)
        SetTeamType(2410900, TeamType.HostileNPC)
        Goto(Label.L9)
    SetNest(2410900, region=2412332)
    SetTeamType(2410900, TeamType.HostileNPC)
    Goto(Label.L9)

    # --- Label 2 --- #
    DefineLabel(2)
    if FlagEnabled(1705):
        DisableBackread(2410900)
        Goto(Label.L9)
    if FlagEnabled(1704):
        DisableBackread(2410900)
        Goto(Label.L9)
    if FlagEnabled(1701):
        DisableBackread(2410900)
        Goto(Label.L9)
    if FlagEnabled(1703):
        DisableBackread(2410900)
        DisableCharacter(2410900)
        Move(2410900, destination=2412334, destination_type=CoordEntityType.Region, set_draw_parent=2414124)
        WaitFrames(frames=1)
        DropMandatoryTreasure(2410900)
        Goto(Label.L9)
    if FlagEnabled(1702):
        DisableBackread(2410900)
        DisableCharacter(2410900)
        Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, set_draw_parent=2414122)
        WaitFrames(frames=1)
        DropMandatoryTreasure(2410900)
        Goto(Label.L9)
    DisableBackread(2410900)
    DisableCharacter(2410900)
    DropMandatoryTreasure(2410900)
    Goto(Label.L9)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, set_draw_parent=2414122)
    SetNest(2410900, region=2412332)
    DisableFlag(72410546)
    Goto(Label.L9)

    # --- Label 4 --- #
    DefineLabel(4)
    Move(2410900, destination=2412334, destination_type=CoordEntityType.Region, set_draw_parent=2414124)
    SetNest(2410900, region=2412334)
    DisableFlag(72410546)
    Goto(Label.L9)

    # --- Label 5 --- #
    DefineLabel(5)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, set_draw_parent=2414122)
    SetNest(2410900, region=2412332)
    SetTeamType(2410900, TeamType.CoopNPC)
    EnableFlag(72410546)
    WaitFrames(frames=2)
    AddSpecialEffect(2410900, 7608)
    Goto(Label.L9)

    # --- Label 6 --- #
    DefineLabel(6)
    DisableCharacter(2410900)
    Goto(Label.L9)

    # --- Label 7 --- #
    DefineLabel(7)
    DisableBackread(2410900)
    Goto(Label.L9)

    # --- Label 8 --- #
    DefineLabel(8)
    ForceAnimation(2410900, 103030)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    Event_12410801()
    Event_12410803()
    Event_12410804()
    Event_12410805()
    Event_12410806()
    Event_12410807()
    Event_12410808()


@ContinueOnRest(12410801)
def Event_12410801():
    """Event 12410801"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(1360))
    AND_1.Add(FlagEnabled(72410540))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1360, 1379))
    EnableFlag(1361)


@ContinueOnRest(12410803)
def Event_12410803():
    """Event 12410803"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(1363))
    AND_1.Add(CharacterDead(2410901))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1360, 1379))
    EnableFlag(1366)


@ContinueOnRest(12410804)
def Event_12410804():
    """Event 12410804"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    OR_1.Add(FlagEnabled(1364))
    OR_1.Add(FlagEnabled(1365))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterDead(2410901))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1360, 1379))
    EnableFlag(1367)


@ContinueOnRest(12410805)
def Event_12410805():
    """Event 12410805"""
    if ThisEventFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(CharacterDead(2410900))
    
    SkipLinesIfFlagEnabled(9, 1369)
    DisableFlagRange((1700, 1705))
    SkipLinesIfFlagRangeAllDisabled(1, (1360, 1361))
    EnableFlag(1700)
    SkipLinesIfFlagDisabled(1, 1365)
    EnableFlag(1702)
    SkipLinesIfFlagDisabled(1, 1366)
    EnableFlag(1703)
    SkipLinesIfFlagDisabled(1, 1367)
    EnableFlag(1702)
    DisableFlagRange((1360, 1379))
    EnableFlag(1368)
    SaveRequest()


@ContinueOnRest(12410806)
def Event_12410806():
    """Event 12410806"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterAlive(2410900))
    AND_1.Add(FlagEnabled(72410544))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1700, 1705))
    SkipLinesIfFlagRangeAllDisabled(1, (1360, 1361))
    EnableFlag(1700)
    if FlagEnabled(1365):
        EnableFlag(1702)
    if FlagEnabled(1366):
        EnableFlag(1703)
    if FlagEnabled(1367):
        EnableFlag(1702)
    DisableFlagRange((1360, 1379))
    EnableFlag(1369)
    SetTeamType(2410900, TeamType.HostileNPC)
    SaveRequest()


@ContinueOnRest(12410807)
def Event_12410807():
    """Event 12410807"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagDisabled(1364))
    OR_1.Add(FlagDisabled(1365))
    AND_1.Add(OR_1)
    AND_1.Add(Attacked(attacked_entity=2410900, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    OR_2.Add(FlagDisabled(1364))
    OR_2.Add(FlagDisabled(1365))
    AND_2.Add(OR_2)
    AND_2.Add(Attacked(attacked_entity=2410900, attacker=PLAYER))
    
    MAIN.Await(AND_2)
    
    WaitFrames(frames=1)
    OR_3.Add(FlagDisabled(1364))
    OR_3.Add(FlagDisabled(1365))
    AND_3.Add(OR_3)
    AND_3.Add(Attacked(attacked_entity=2410900, attacker=PLAYER))
    
    MAIN.Await(AND_3)
    
    WaitFrames(frames=1)


@RestartOnRest(12410808)
def Event_12410808():
    """Event 12410808"""
    MAIN.Await(FlagEnabled(72410545))
    
    ReplanAI(2410900)
    AICommand(2410900, command_id=30, command_slot=0)
    OR_1.Add(FlagDisabled(72410545))
    OR_1.Add(HasAIStatus(2410900, ai_status=AIStatusType.Battle))
    OR_1.Add(EntityBeyondDistance(entity=2410900, other_entity=PLAYER, radius=5.0))
    
    MAIN.Await(OR_1)
    
    ReplanAI(2410900)
    AICommand(2410900, command_id=-1, command_slot=0)
    DisableFlag(72410545)
    Restart()


@ContinueOnRest(12410809)
def Event_12410809():
    """Event 12410809"""
    DisableBackread(2410901)
    if FlagEnabled(12410810):
        return
    if FlagEnabled(1366):
        return
    if FlagEnabled(1367):
        return
    if FlagEnabled(9467):
        return
    if FlagEnabled(9802):
        return
    OR_1.Add(FlagEnabled(1363))
    OR_1.Add(FlagEnabled(1364))
    OR_1.Add(FlagEnabled(1365))
    OR_2.Add(FlagEnabled(1701))
    OR_2.Add(FlagEnabled(1702))
    AND_1.Add(OR_2)
    OR_3.Add(FlagEnabled(1368))
    OR_3.Add(FlagEnabled(1369))
    AND_1.Add(OR_3)
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableBackread(2410901)


@ContinueOnRest(12410810)
def Event_12410810():
    """Event 12410810"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2410901)
    DisableCharacter(2410901)
    DropMandatoryTreasure(2410901)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(HealthRatio(2410901) == 0.0)
    
    SetAIParamID(2410900, ai_param_id=6163)
    AICommand(2410900, command_id=11, command_slot=0)
    ClearTargetList(2410900)
    ReplanAI(2410900)
    
    MAIN.Await(CharacterDead(2410901))
    
    EnableFlag(5912)
    SetTeamType(2410900, TeamType.FriendlyNPC)
    DisableFlag(72410546)
    SaveRequest()


@RestartOnRest(12410811)
def Event_12410811():
    """Event 12410811"""
    if ThisEventFlagEnabled():
        return
    OR_1.Add(FlagEnabled(1363))
    OR_1.Add(FlagEnabled(1364))
    AND_1.Add(OR_1)
    AND_1.Add(HasAIStatus(2410901, ai_status=AIStatusType.Battle))
    
    MAIN.Await(AND_1)
    
    EnableBackread(2410900)
    Move(2410900, destination=2412333, destination_type=CoordEntityType.Region, copy_draw_parent=2414123)
    SetNest(2410900, region=2412334)
    SetTeamType(2410900, TeamType.CoopNPC)
    WaitFrames(frames=2)
    ForceAnimation(2410900, 101290)
    AddSpecialEffect(2410900, 7608)
    SetAIParamID(2410900, ai_param_id=6162)
    AICommand(2410900, command_id=10, command_slot=0)
    ReplanAI(2410900)
    DisableFlagRange((1360, 1379))
    EnableFlag(1365)
    
    MAIN.Await(CharacterInsideRegion(2410900, region=2412334))
    
    AICommand(2410900, command_id=-1, command_slot=0)
    ReplanAI(2410900)


@ContinueOnRest(12410812)
def Event_12410812():
    """Event 12410812"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagDisabled(Label.L0, flag=1169)
    DisableFlagRange((1160, 1179))
    EnableFlag(1163)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@ContinueOnRest(12410813)
def Event_12410813():
    """Event 12410813"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagDisabled(Label.L0, flag=1314)
    DisableFlagRange((1300, 1319))
    EnableFlag(1309)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@ContinueOnRest(12410814)
def Event_12410814():
    """Event 12410814"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagDisabled(Label.L0, flag=1209)
    DisableFlagRange((1200, 1219))
    EnableFlag(1204)

    # --- Label 0 --- #
    DefineLabel(0)
    End()


@ContinueOnRest(12410830)
def Event_12410830():
    """Event 12410830"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L0, input_condition=AND_15)
    GotoIfFlagDisabled(Label.L2, flag=1233)
    DisableFlagRange((1220, 1239))
    EnableFlag(1223)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_2.Add(FlagEnabled(1228))
    AND_2.Add(FlagEnabled(72400486))
    GotoIfConditionFalse(Label.L3, input_condition=AND_2)
    DisableFlagRange((1220, 1239))
    EnableFlag(1229)

    # --- Label 3 --- #
    DefineLabel(3)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(2410770)
    DisableCharacterCollision(2410770)
    GotoIfFlagEnabled(Label.L0, flag=1228)
    GotoIfFlagEnabled(Label.L0, flag=1229)
    GotoIfFlagEnabled(Label.L1, flag=1235)
    GotoIfFlagEnabled(Label.L2, flag=1236)
    DisableCharacter(2410770)
    DisableBackread(2410771)
    DisableObject(2411280)
    EnableObject(2411281)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    DisableAI(2410771)
    ForceAnimation(2410770, 103082)
    ForceAnimation(2410771, 7010, loop=True)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    EzstateAIRequest(2410770, command_id=5, command_slot=1)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2410770)
    DropMandatoryTreasure(2410771)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    EzstateAIRequest(2410770, command_id=4, command_slot=1)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2410770)
    DropMandatoryTreasure(2410771)
    End()


@ContinueOnRest(12410831)
def Event_12410831():
    """Event 12410831"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1235):
        return
    if FlagEnabled(1236):
        return
    AND_1.Add(CharacterDead(2410770))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1220, 1239))
    EnableFlag(1235)
    SaveRequest()


@ContinueOnRest(12410833)
def Event_12410833():
    """Event 12410833"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(1235):
        return
    if FlagEnabled(1236):
        return
    AND_1.Add(HealthRatio(2410771) == 0.0)
    AND_1.Add(HealthRatio(2410770) != 0.0)
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1220, 1239))
    EnableFlag(1236)
    WaitFrames(frames=1)
    ForceAnimation(2410770, 103083)
    SaveRequest()


@ContinueOnRest(12410834)
def Event_12410834():
    """Event 12410834"""
    if ThisEventFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    WaitFrames(frames=10)
    OR_1.Add(FlagEnabled(1228))
    OR_1.Add(FlagEnabled(1229))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412302))
    
    MAIN.Await(AND_1)
    
    RunEvent(9350, slot=0, args=(3,))
    EnableFlag(72400956)


@ContinueOnRest(12410835)
def Event_12410835():
    """Event 12410835"""
    if ThisEventFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterBackreadEnabled(2410770))
    AND_1.Add(FlagEnabled(1228))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    DisableAI(2410771)
    ForceAnimation(2410770, 103082)
    ForceAnimation(2410771, 7010, loop=True)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, short_move=True)
    End()


@ContinueOnRest(12410850)
def Event_12410850(_, flag: int, action_button_id: int, destination: int):
    """Event 12410850"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    DisableFlag(flag)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=destination))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=210, short_move=True)
    ForceAnimation(PLAYER, 101320)
    WaitFrames(frames=25)
    WaitFrames(frames=20)
    EnableFlag(flag)
    
    MAIN.Await(FlagDisabled(flag))
    
    Restart()


@ContinueOnRest(12410860)
def Event_12410860(_, character: int, animation_id: int):
    """Event 12410860"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(character) != 0.0)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id)
    Restart()


@ContinueOnRest(12410870)
def Event_12410870(_, character: int, animation_id: int, special_effect: int):
    """Event 12410870"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id)
    WaitFrames(frames=5)
    Restart()


@ContinueOnRest(12410880)
def Event_12410880(_, character: int, animation_id: int):
    """Event 12410880"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(character) == 0.0)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id)


@RestartOnRest(12415130)
def Event_12415130(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    flag: int,
    ai_param_id: int,
    ai_param_id_1: int,
    right: int,
):
    """Event 12415130"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    if ValueNotEqual(left=0, right=right):
        OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    WaitRandomFrames(min_frames=0, max_frames=60)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(12415150)
def Event_12415150(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    radius: float,
    ai_param_id: int,
    ai_param_id_1: int,
):
    """Event 12415150"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
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
    
    ForceAnimation(character, animation_id_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    EnableGravity(character)


@RestartOnRest(12410155)
def Event_12410155(_, character: int, region: int, region_1: int, region_2: int):
    """Event 12410155"""
    DisableAI(character)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=region_2))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)


@RestartOnRest(12410156)
def Event_12410156(_, character: int, character_1: int, character_2: int):
    """Event 12410156"""
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    OR_2.Add(HasAIStatus(character_1, ai_status=AIStatusType.Caution))
    OR_2.Add(HasAIStatus(character_1, ai_status=AIStatusType.Search))
    OR_2.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    AND_2.Add(OR_2)
    OR_3.Add(HasAIStatus(character_2, ai_status=AIStatusType.Caution))
    OR_3.Add(HasAIStatus(character_2, ai_status=AIStatusType.Search))
    OR_3.Add(HasAIStatus(character_2, ai_status=AIStatusType.Battle))
    AND_3.Add(OR_3)
    OR_15.Add(AND_1)
    OR_15.Add(AND_2)
    OR_15.Add(AND_3)
    
    MAIN.Await(OR_15)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_3)

    # --- Label 0 --- #
    DefineLabel(0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SetNest(character, region=2412225)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    OR_4.Add(CharacterInsideRegion(character, region=2412225))
    OR_4.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_4)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    SetNest(character, region=2412226)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    OR_5.Add(CharacterInsideRegion(character, region=2412226))
    OR_5.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_5)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    End()


@ContinueOnRest(12410321)
def Event_12410321(_, flag: int, flag_1: int, flag_2: int, flag_3: int, obj: int, obj_1: int, obj_2: int):
    """Event 12410321"""
    if FlagEnabled(flag):
        return
    GotoIfFlagEnabled(Label.L0, flag=flag_3)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    EndOfAnimation(obj=obj, animation_id=2)
    DisableObjectActivation(obj_1, obj_act_id=100)
    DisableObjectActivation(obj_2, obj_act_id=100)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_1))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    DisableFlag(flag_2)
    EndOfAnimation(obj=obj, animation_id=2)
    EnableObjectActivation(obj_1, obj_act_id=100)
    DisableObjectActivation(obj_2, obj_act_id=100)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_2)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj_1, obj_act_id=100)
    EnableObjectActivation(obj_2, obj_act_id=100)


@ContinueOnRest(12410325)
def Event_12410325(_, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12410325"""
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


@ContinueOnRest(12410322)
def Event_12410322(_, flag: int, flag_1: int, flag_2: int, flag_3: int, region: int, obj_act_id: int):
    """Event 12410322"""
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(FlagEnabled(flag_1))
    GotoIfConditionFalse(Label.L0, input_condition=AND_3)
    EndOfAnimation(obj=2411320, animation_id=3)
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
    ForceAnimation(2411320, 6, wait_for_completion=True)
    ForceAnimation(2411320, 3, wait_for_completion=True)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2412321))
    
    ForceAnimation(2411320, 7, wait_for_completion=True)
    DisableObjectActivation(2411317, obj_act_id=100)
    EnableObjectActivation(2411318, obj_act_id=100)
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12410323)
def Event_12410323(_, flag: int, flag_1: int, flag_2: int, flag_3: int, region: int, obj_act_id: int):
    """Event 12410323"""
    AND_3.Add(FlagEnabled(flag))
    AND_3.Add(FlagDisabled(flag_1))
    GotoIfConditionFalse(Label.L0, input_condition=AND_3)
    EndOfAnimation(obj=2411320, animation_id=1)
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
    ForceAnimation(2411320, 4, wait_for_completion=True)
    ForceAnimation(2411320, 1, wait_for_completion=True)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2412322))
    
    ForceAnimation(2411320, 5, wait_for_completion=True)
    EnableObjectActivation(2411317, obj_act_id=100)
    DisableObjectActivation(2411318, obj_act_id=100)
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12410324)
def Event_12410324(_, flag: int, flag_1: int, flag_2: int, entity: int, entity_1: int):
    """Event 12410324"""
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


@ContinueOnRest(12410330)
def Event_12410330(_, flag: int, region: int, obj: int, obj_1: int):
    """Event 12410330"""
    if FlagEnabled(flag):
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    EnableObjectActivation(obj, obj_act_id=100)
    DisableObjectActivation(obj_1, obj_act_id=100)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(flag)


@ContinueOnRest(12410460)
def Event_12410460(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    ai_param_id: int,
    ai_param_id_1: int,
    character_1: int,
):
    """Event 12410460"""
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    DisableGravity(character)
    AND_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableGravity(character)
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_2)
    WaitRandomFrames(min_frames=20, max_frames=100)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(12414450)
def Event_12414450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 12414450"""
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


@RestartOnRest(12414470)
def Event_12414470():
    """Event 12414470"""
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(12414420))
    AND_1.Add(FlagDisabled(12414430))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412705))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412706))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412707))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412708))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412709))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(2410158, command_id=992, command_slot=0)
    ReplanAI(2410158)


@RestartOnRest(12414480)
def Event_12414480():
    """Event 12414480"""
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterHasTAEEvent(2410158, tae_event_id=1000))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(2410158)
    SendNPCSummonHome(character=2410158)


@RestartOnRest(12414490)
def Event_12414490():
    """Event 12414490"""
    DisableNetworkSync()
    AND_1.Add(Host())
    AND_1.Add(FlagEnabled(12414421))
    AND_1.Add(FlagDisabled(12414431))
    AND_1.Add(FlagEnabled(12414700))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect_WithUnknownEffect(2410740, 35)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(12414400)
def Event_12414400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12414400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(FlagDisabled(12411802))
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
    AND_2.Add(FlagDisabled(12411802))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12414401)
def Event_12414401(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12414401"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(FlagEnabled(72400461))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1340, 1341)))
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
    AND_2.Add(FlagEnabled(72400461))
    AND_2.Add(FlagRangeAnyEnabled(flag_range=(1340, 1341)))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12414410)
def Event_12414410(
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
    """Event 12414410"""
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


@RestartOnRest(12414460)
def Event_12414460(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 12414460"""
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
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12414500)
def Event_12414500():
    """Event 12414500"""
    GotoIfThisEventFlagDisabled(Label.L0)
    SetBackreadStateAlternate(2410740, True)
    AddSpecialEffect(2410740, 9006)
    EnableCharacter(2410740)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(2410740)
    DisableAI(2410740)
    AND_15.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(1, AND_15)
    SetNetworkUpdateAuthority(2410740, authority_level=UpdateAuthority.Forced)
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12414608))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412722))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=2412723))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(FlagEnabled(72400461))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1340, 1341)))
    
    MAIN.Await(AND_1)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_3)
    Move(2410740, destination=2412720, destination_type=CoordEntityType.Region, set_draw_parent=0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(2410740, destination=2412721, destination_type=CoordEntityType.Region, set_draw_parent=2414021)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(5.0)
    EnableFlag(12414506)
    PlaySoundEffect(PLAYER, 100000009, sound_type=SoundType.f_MenuEffect)
    Wait(5.0)
    PlaySoundEffect(PLAYER, 100000020, sound_type=SoundType.f_MenuEffect)
    SetBackreadStateAlternate(2410740, True)
    AddSpecialEffect(2410740, 9006)
    EnableCharacter(2410740)
    ForceAnimation(2410740, 101201, wait_for_completion=True)
    EnableAI(2410740)
    DisableMapCollision(collision=2414200)


@RestartOnRest(12414501)
def Event_12414501():
    """Event 12414501"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(12411700):
        return
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(12414502))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(2410740)
    SetBackreadStateAlternate(2410740, False)


@RestartOnRest(12414502)
def Event_12414502():
    """Event 12414502"""
    if FlagEnabled(12411700):
        return
    if FlagEnabled(12414501):
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(12414500))
    AND_1.Add(FlagDisabled(12414501))
    AND_1.Add(FlagEnabled(12411700))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(2410740, command_id=991, command_slot=0)
    ReplanAI(2410740)
    Wait(1.0)
    AddSpecialEffect(2410740, 5560)
    CreateTemporaryVFX(vfx_id=121, anchor_entity=2410740, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(2.0)
    DisableCharacter(2410740)


@RestartOnRest(12414503)
def Event_12414503():
    """Event 12414503"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if FlagEnabled(12411700):
        return
    if FlagEnabled(12414501):
        return
    if FlagEnabled(12414505):
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(FlagEnabled(12414500))
    AND_1.Add(FlagDisabled(12414501))
    AND_1.Add(FlagEnabled(12411702))
    AND_1.Add(FlagEnabled(12414700))
    AND_1.Add(CharacterOutsideRegion(2410740, region=2412801))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetEventPoint(2410740, region=2412710, reaction_range=1.0)
    AICommand(2410740, command_id=990, command_slot=0)
    ReplanAI(2410740)


@RestartOnRest(12414504)
def Event_12414504():
    """Event 12414504"""
    if FlagEnabled(12411700):
        return
    if FlagEnabled(12414501):
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(12414503))
    AND_1.Add(CharacterInsideRegion(2410740, region=2412710))
    
    MAIN.Await(AND_1)
    
    ResetAnimation(2410740)
    RotateToFaceEntity(2410740, 2412800, animation=101130, wait_for_completion=True)
    AICommand(2410740, command_id=-1, command_slot=0)
    ReplanAI(2410740)


@RestartOnRest(12414505)
def Event_12414505():
    """Event 12414505"""
    DisableSoapstoneMessage(2413221)
    DisableSoapstoneMessage(2413223)
    DeleteVFX(2413231, erase_root_only=False)
    DeleteVFX(2413233, erase_root_only=False)
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerHasGood(200))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(FlagEnabled(72400461))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1340, 1341)))
    
    MAIN.Await(AND_1)
    
    EnableSoapstoneMessage(2413221)
    EnableSoapstoneMessage(2413223)
    CreateVFX(2413231)
    CreateVFX(2413233)
    OR_1.Add(FlagEnabled(12414506))
    OR_1.Add(FlagEnabled(12411700))
    
    MAIN.Await(OR_1)
    
    DisableSoapstoneMessage(2413221)
    DisableSoapstoneMessage(2413223)
    DeleteVFX(2413231)
    DeleteVFX(2413233)


@RestartOnRest(12414600)
def Event_12414600():
    """Event 12414600"""
    GotoIfThisEventFlagDisabled(Label.L0)
    SetBackreadStateAlternate(2410158, True)
    AddSpecialEffect(2410158, 9006)
    EnableCharacter(2410158)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(2410158)
    DisableAI(2410158)
    AND_15.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(1, AND_15)
    SetNetworkUpdateAuthority(2410158, authority_level=UpdateAuthority.Forced)
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12414608))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412700))
    AND_3.Add(CharacterInsideRegion(PLAYER, region=2412701))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(FlagDisabled(12411802))
    
    MAIN.Await(AND_1)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_3)
    Move(2410158, destination=2412702, destination_type=CoordEntityType.Region, set_draw_parent=2414020)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Move(2410158, destination=2412703, destination_type=CoordEntityType.Region, set_draw_parent=2414021)

    # --- Label 2 --- #
    DefineLabel(2)
    Wait(5.0)
    EnableFlag(12414609)
    PlaySoundEffect(PLAYER, 100000009, sound_type=SoundType.f_MenuEffect)
    Wait(5.0)
    PlaySoundEffect(PLAYER, 100000020, sound_type=SoundType.f_MenuEffect)
    SetBackreadStateAlternate(2410158, True)
    AddSpecialEffect(2410158, 9006)
    EnableCharacter(2410158)
    ForceAnimation(2410158, 7010, wait_for_completion=True)
    EnableAI(2410158)
    DisableMapCollision(collision=2414200)


@RestartOnRest(12414601)
def Event_12414601():
    """Event 12414601"""
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterHasTAEEvent(2410158, tae_event_id=1000))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(2410158)
    SetBackreadStateAlternate(2410158, False)
    EnableMapCollision(collision=2414200)


@RestartOnRest(12414602)
def Event_12414602():
    """Event 12414602"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(12414600))
    AND_1.Add(FlagDisabled(12414601))
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(FlagDisabled(12411802))
    AND_1.Add(CharacterDead(2410800))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(2410158, command_id=991, command_slot=0)
    ReplanAI(2410158)


@RestartOnRest(12414603)
def Event_12414603():
    """Event 12414603"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(12414600))
    AND_1.Add(FlagDisabled(12414601))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412705))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412706))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412707))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412708))
    OR_1.Add(CharacterInsideRegion(2410158, region=2412709))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(2410158, command_id=992, command_slot=0)
    ReplanAI(2410158)


@RestartOnRest(12414604)
def Event_12414604():
    """Event 12414604"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(12411702))
    AND_1.Add(FlagEnabled(12414700))
    AND_1.Add(CharacterOutsideRegion(2410158, region=2412801))
    
    MAIN.Await(AND_1)
    
    SetEventPoint(2410158, region=2412710, reaction_range=1.0)
    AICommand(2410158, command_id=990, command_slot=0)
    ReplanAI(2410158)


@RestartOnRest(12414605)
def Event_12414605():
    """Event 12414605"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(12414604))
    AND_1.Add(CharacterInsideRegion(2410158, region=2412710))
    
    MAIN.Await(AND_1)
    
    ResetAnimation(2410158)
    RotateToFaceEntity(2410158, 2412800, animation=7014, wait_for_completion=True)
    AICommand(2410158, command_id=-1, command_slot=0)
    ReplanAI(2410158)


@RestartOnRest(12414606)
def Event_12414606():
    """Event 12414606"""
    DisableSoapstoneMessage(2413220)
    DisableSoapstoneMessage(2413222)
    DeleteVFX(2413230, erase_root_only=False)
    DeleteVFX(2413232, erase_root_only=False)
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerHasGood(200))
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagDisabled(12411700))
    AND_1.Add(FlagDisabled(12411802))
    
    MAIN.Await(AND_1)
    
    EnableSoapstoneMessage(2413220)
    EnableSoapstoneMessage(2413222)
    CreateVFX(2413230)
    CreateVFX(2413232)
    OR_1.Add(FlagEnabled(12414609))
    OR_1.Add(FlagEnabled(12411700))
    OR_1.Add(FlagEnabled(12411802))
    
    MAIN.Await(OR_1)
    
    DisableSoapstoneMessage(2413220)
    DisableSoapstoneMessage(2413222)
    DeleteVFX(2413230)
    DeleteVFX(2413232)


@RestartOnRest(12414607)
def Event_12414607():
    """Event 12414607"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 9000))
    
    MAIN.Await(AND_1)
    
    EnableFlag(12414608)
    WaitFrames(frames=1)
    DisableFlag(12414608)
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 9000))
    
    MAIN.Await(AND_2)
    
    Restart()


@RestartOnRest(12414610)
def Event_12414610():
    """Event 12414610"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(12414600))
    AND_1.Add(FlagDisabled(12414601))
    AND_1.Add(HealthRatio(2410158) > 0.0)
    AND_1.Add(CharacterHasSpecialEffect(2410158, 4640))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    AND_2.Add(FlagEnabled(12414600))
    AND_2.Add(FlagDisabled(12414601))
    AND_2.Add(HealthRatio(2410158) > 0.0)
    if not AND_2:
        return
    PlaySoundEffect(2410158, 242100402, sound_type=SoundType.v_Voice)


@ContinueOnRest(12410220)
def Event_12410220(_, character: int, radius: float):
    """Event 12410220"""
    DisableAI(character)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)


@ContinueOnRest(12410234)
def Event_12410234():
    """Event 12410234"""
    MAIN.Await(CharacterDead(2410158))
    
    End()


@ContinueOnRest(12410237)
def Event_12410237(_, flag: int, character: int, character_1: int, character_2: int, region: int):
    """Event 12410237"""
    DisableCharacter(character_2)
    
    MAIN.Await(FlagEnabled(flag))
    
    OR_1.Add(HealthRatio(character) <= 0.5)
    OR_1.Add(TimeElapsed(seconds=40.0))
    AND_1.Add(FlagEnabled(12410235))
    AND_1.Add(CharacterAlive(character_1))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(12411800):
        return
    DisableCharacter(character_1)
    EnableCharacter(character_2)
    Wait(1.0)
    SetNest(character_2, region=region)
    AICommand(character_2, command_id=10, command_slot=0)
    ReplanAI(character_2)
    DisableGravity(character_2)
    DisableCharacterCollision(character_2)
    DisableAnimations(character_2)
    OR_2.Add(EntityWithinDistance(entity=character_2, other_entity=2410810, radius=3.0))
    OR_2.Add(CharacterInsideRegion(character_2, region=2412811))
    
    MAIN.Await(OR_2)
    
    AICommand(character_2, command_id=-1, command_slot=0)
    ClearTargetList(character_2)
    ReplanAI(character_2)
    EnableCharacterCollision(character_2)
    EnableAnimations(character_2)
    EnableGravity(character_2)


@ContinueOnRest(12410238)
def Event_12410238():
    """Event 12410238"""
    OR_1.Add(FlagEnabled(12410234))
    OR_1.Add(FlagEnabled(12411802))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=10)
    DisableCharacter(2410158)


@ContinueOnRest(12410239)
def Event_12410239(_, character: int):
    """Event 12410239"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=5)
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_2)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_2)
    
    WaitFrames(frames=5)
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_3)
    AND_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_3)
    
    WaitFrames(frames=5)
    OR_4.Add(CharacterHuman(PLAYER))
    OR_4.Add(CharacterWhitePhantom(PLAYER))
    AND_4.Add(OR_4)
    AND_4.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(AND_4)
    
    WaitFrames(frames=5)

    # --- Label 0 --- #
    DefineLabel(0)
    StopEvent(event_id=12415234)
    DisableFlag(12415234)
    RemoveSpecialEffect(character, 5590)
    SetTeamType(character, TeamType.Indiscriminate)


@ContinueOnRest(12410240)
def Event_12410240(_, character: int, animation_id: int, min_seconds: float, max_seconds: float):
    """Event 12410240"""
    WaitRandomSeconds(min_seconds=min_seconds, max_seconds=max_seconds)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    ForceAnimation(character, animation_id, wait_for_completion=True)
    Restart()


@ContinueOnRest(12410285)
def Event_12410285(_, start_climbing_flag: int, stop_climbing_flag: int, obj: int, obj_1: int):
    """Event 12410285"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=2)
        Wait(1.0)
        RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)
        DisableObjectActivation(obj_1, obj_act_id=2410000)
    
        MAIN.Await(ActionButtonParamActivated(action_button_id=7100, entity=obj_1))
    
        DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
        Restart()
    
    MAIN.Await(ObjectActivated(obj_act_id=12410206))
    
    ForceAnimation(obj, 1)
    WaitFrames(frames=40)
    ForceAnimation(obj, 2)
    RegisterLadder(start_climbing_flag=start_climbing_flag, stop_climbing_flag=stop_climbing_flag, obj=obj)
    Restart()


@ContinueOnRest(12410287)
def Event_12410287(_, obj: int, region: int, name: int):
    """Event 12410287"""
    if ThisEventSlotFlagEnabled():
        CreateObjectVFX(obj, vfx_id=100, model_point=8028)
        End()
    CreateObjectVFX(obj, vfx_id=100, model_point=8029)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    ForceAnimation(obj, 1000000)
    WaitFrames(frames=30)
    DeleteObjectVFX(obj)
    CreateObjectVFX(obj, vfx_id=100, model_point=8028)
    PlaySoundEffect(obj, 600000000, sound_type=SoundType.a_Ambient)
    CreatePlayLog(name=name)


@ContinueOnRest(12410340)
def Event_12410340(_, character: int, region: int, command_id: int, region_1: int):
    """Event 12410340"""
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region_1))
    
    SetNest(character, region=region)
    AICommand(character, command_id=command_id, command_slot=0)
    ReplanAI(character)
    OR_1.Add(CharacterInsideRegion(character, region=region))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12410370)
def Event_12410370():
    """Event 12410370"""
    OR_10.Add(CharacterDead(2410028))
    OR_10.Add(CharacterDead(2410030))
    GotoIfConditionTrue(Label.L0, input_condition=OR_10)
    AND_10.Add(ObjectDestroyed(2411221))
    GotoIfConditionTrue(Label.L0, input_condition=AND_10)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(2411220)
    PostDestruction(2411221)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(2411221)
    ForceAnimation(2411220, 0)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412210))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2412211))
    AND_3.Add(FlagEnabled(12415371))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    EnableFlag(12415371)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_3)
    OR_3.Add(EntityWithinDistance(entity=2411220, other_entity=PLAYER, radius=10.0))
    OR_3.Add(RandomTimeElapsed(min_seconds=4.0, max_seconds=12.0))
    OR_3.Add(Attacked(attacked_entity=2410028, attacker=PLAYER))
    OR_3.Add(Attacked(attacked_entity=2410030, attacker=PLAYER))
    
    MAIN.Await(OR_3)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(2410028, 3008)
    ForceAnimation(2410030, 3009)
    WaitFrames(frames=40)
    EnableInvincibility(2410028)
    EnableInvincibility(2410030)
    CreateObjectVFX(2411220, vfx_id=100, model_point=900260)
    CreateHazard(
        obj_flag=12410376,
        obj=2411220,
        model_point=100,
        behavior_param_id=6111,
        target_type=DamageTargetType.Character,
        radius=1.600000023841858,
        life=9999.0,
        repetition_time=0.0,
    )
    ForceAnimation(2411220, 1)
    WaitFrames(frames=6)
    DisableInvincibility(2410028)
    DisableInvincibility(2410030)
    WaitFrames(frames=206)
    RemoveObjectFlag(obj_flag=12410376)
    DeleteObjectVFX(2411220)
    EnableObject(2411221)
    DisableObject(2411220)
    DestroyObject(2411221)


@RestartOnRest(12415372)
def Event_12415372(_, character: int):
    """Event 12415372"""
    MAIN.Await(FlagEnabled(12415371))
    
    EnableFlag(12415371)
    SetNest(character, region=2412212)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    OR_1.Add(CharacterInsideRegion(character, region=2412212))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12410378)
def Event_12410378(_, character: int, animation_id: int, obj: int, destination: int):
    """Event 12410378"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=obj, animation_id=2)
        Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
        End()
    DisableAI(character)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412031))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    WaitRandomFrames(min_frames=50, max_frames=70)
    
    MAIN.Await(HealthValue(character) <= 2)
    
    ForceAnimation(character, animation_id, loop=True, wait_for_completion=True, skip_transition=True)
    WaitFrames(frames=76)
    
    MAIN.Await(HealthValue(character) <= 2)
    
    ForceAnimation(character, animation_id, loop=True, wait_for_completion=True, skip_transition=True)
    WaitRandomFrames(min_frames=76, max_frames=100)
    
    MAIN.Await(HealthValue(character) <= 2)
    
    DisableGravity(character)
    DisableCharacterCollision(character)
    EnableInvincibility(character)
    DisableImmortality(character)
    RemoveSpecialEffect(character, 5915)
    ForceAnimation(obj, 1)
    ForceAnimation(character, 3001)
    WaitFrames(frames=16)
    EnableAI(character)
    EnableGravity(character)
    EnableCharacterCollision(character)
    DisableInvincibility(character)


@RestartOnRest(12410380)
def Event_12410380(_, character: int, animation_id: int):
    """Event 12410380"""
    DisableAI(character)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2412031))
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    WaitRandomFrames(min_frames=55, max_frames=200)
    AND_2.Add(HealthValue(character) >= 1)
    SkipLinesIfConditionTrue(2, AND_2)
    ForceAnimation(character, animation_id, loop=True, wait_for_completion=True, skip_transition=True)
    Restart()
    End()


@RestartOnRest(12410384)
def Event_12410384(_, character: int):
    """Event 12410384"""
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    Kill(character, award_souls=True)


@ContinueOnRest(12410490)
def Event_12410490(_, obj: int, obj_1: int, flag: int):
    """Event 12410490"""
    if FlagEnabled(100):
        DisableFlag(100)
        DisableFlag(flag)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    PostDestruction(obj)
    ForceAnimation(obj_1, 2)
    EnableTreasure(obj=obj_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateObjectVFX(obj_1, vfx_id=90, model_point=900201)
    ForceAnimation(obj_1, 0)
    
    MAIN.Await(ObjectDestroyed(obj))
    
    ForceAnimation(obj_1, 1, wait_for_completion=True)
    DeleteObjectVFX(obj_1)
    EnableTreasure(obj=obj_1)
    EnableFlag(flag)
    
    MAIN.Await(FlagEnabled(100))
    
    RestoreObject(obj)
    ForceAnimation(obj_1, 0)
    DisableTreasure(obj=obj_1)
    Restart()


@ContinueOnRest(12410990)
def Event_12410990():
    """Event 12410990"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(PlayerStandingOnCollision(2413500))
    
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=148,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=148,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=148,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=148,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )


@ContinueOnRest(12410995)
def Event_12410995():
    """Event 12410995"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    AND_1.Add(PlayerStandingOnCollision(2414110))
    AND_1.Add(CharacterOutsideRegion(PLAYER, region=2412900))
    
    MAIN.Await(AND_1)
    
    RunEvent(9350, slot=0, args=(1,))


@RestartOnRest(12415010)
def Event_12415010(_, anchor_entity: int, sound_type: int, sound_id: int, seconds: float):
    """Event 12415010"""
    DisableNetworkSync()
    Wait(seconds)
    PlaySoundEffect(anchor_entity, sound_id, sound_type=sound_type)
    WaitFrames(frames=440)
    AND_1.Add(FlagDisabled(9801))
    AND_1.Add(FlagDisabled(9802))
    SkipLinesIfConditionTrue(1, AND_1)
    PlaySoundEffect(anchor_entity, sound_id, sound_type=sound_type)
    Restart()
