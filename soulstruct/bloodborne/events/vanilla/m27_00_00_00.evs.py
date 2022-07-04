"""
linked:
164

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス_撃破
52: PC情報_ボス撃破_闇の旅団
82: ボス_戦闘開始
98: ボス戦_撃破時間
116: ギミック_エレベーター起動
144: PC情報_森到達時
164: N:\\SPRJ\\data\\Param\\event\\common.emevd
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunEvent(7000, slot=35, args=(2700950, 2701950, 999, 12707800))
    RunEvent(7000, slot=36, args=(2700951, 2701951, 12701800, 12707820))
    RunEvent(7100, slot=35, args=(72700200, 2701950))
    RunEvent(7100, slot=36, args=(72700201, 2701951))
    RunEvent(7200, slot=35, args=(72700100, 2701950, 2102951))
    RunEvent(7200, slot=36, args=(72700101, 2701951, 2102951))
    RunEvent(7300, slot=35, args=(72102700, 2701950))
    RunEvent(7300, slot=36, args=(72102701, 2701951))
    RunEvent(7600, slot=50, args=(2701999, 2703999))
    RunEvent(7600, slot=51, args=(2701998, 2703998))
    RunEvent(9200, slot=7, args=(2703900,))
    RunEvent(9220, slot=6, args=(2700710, 12704220, 12704221, 2700, 27, 0), arg_types="iiiiBB")
    RunEvent(9240, slot=6, args=(2700710, 12704220, 12704221, 12704222, 27, 0), arg_types="iiiiBB")
    RunEvent(9260, slot=6, args=(2700710, 12704220, 12704221, 12704222, 27, 0), arg_types="iiiiBB")
    RunEvent(9280, slot=6, args=(2700710, 12704220, 12704221, 2700, 12704800, 27, 0), arg_types="iiiiiBB")
    DeleteVFX(2703910, erase_root_only=False)
    DeleteVFX(2703911, erase_root_only=False)
    DeleteVFX(2703912, erase_root_only=False)
    Event_12704400(0, flag=12704440, vfx_id=2703910, flag_1=12704420, flag_2=12704430, flag_3=12701800, flag_4=6001)
    Event_12704401(0, flag=12704441, vfx_id=2703911, flag_1=12704421, flag_2=12704431, flag_3=12701800, flag_4=6001)
    Event_12704410(
        0,
        sign_type=5,
        character=2700920,
        region=2702910,
        summon_flag=12704420,
        dismissal_flag=12704430,
        flag=12704440,
        flag_1=12701800,
        action_button_id=10561
    )
    Event_12704410(
        1,
        sign_type=5,
        character=2700921,
        region=2702913,
        summon_flag=12704421,
        dismissal_flag=12704431,
        flag=12704441,
        flag_1=12701800,
        action_button_id=10565
    )
    Event_12704450(0, character=2700920, region=2702914, flag=12704420, flag_1=12704430, flag_2=12704800)
    Event_12704450(1, character=2700921, region=2702911, flag=12704421, flag_1=12704431, flag_2=12704800)
    Event_12704460(
        0,
        character=2700920,
        region=2702914,
        region_1=2702800,
        region_2=2702801,
        animation=101130,
        flag=12704800,
        region_3=2702801
    )
    Event_12704460(
        1,
        character=2700921,
        region=2702911,
        region_1=2702800,
        region_2=2702801,
        animation=101130,
        flag=12704800,
        region_3=2702801
    )
    RegisterLadder(start_climbing_flag=12700602, stop_climbing_flag=12700603, obj=2701071)
    RegisterLadder(start_climbing_flag=12700604, stop_climbing_flag=12700605, obj=2701072)
    RegisterLadder(start_climbing_flag=12700606, stop_climbing_flag=12700607, obj=2701073)
    CreateHazard(
        obj_flag=12700050,
        obj=2701080,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12700050,
        obj=2701081,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12700050,
        obj=2701082,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12700050,
        obj=2701083,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12700050,
        obj=2701084,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12700050,
        obj=2701085,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12700050,
        obj=2701086,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12701100,
        obj=2701300,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12701101,
        obj=2701301,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12701102,
        obj=2701302,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12701103,
        obj=2701303,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12701104,
        obj=2701304,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12701105,
        obj=2701305,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12701106,
        obj=2701306,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    StartPlayLogMeasurement(measurement_id=2700000, name=0, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2700001, name=18, overwrite=True)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6316)
    EnableFlag(12701999)
    SkipLinesIfFlagEnabled(5, 12701999)
    EnableObject(2701500)
    DisableObject(2701501)
    EnableTreasure(obj=2701500)
    DisableTreasure(obj=2701501)
    SkipLines(4)
    DisableObject(2701500)
    EnableObject(2701501)
    DisableTreasure(obj=2701500)
    EnableTreasure(obj=2701501)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6317)
    EnableFlag(12701998)
    SkipLinesIfFlagEnabled(5, 12701998)
    EnableObject(2701502)
    DisableObject(2701503)
    EnableTreasure(obj=2701502)
    DisableTreasure(obj=2701503)
    SkipLines(4)
    DisableObject(2701502)
    EnableObject(2701503)
    DisableTreasure(obj=2701502)
    EnableTreasure(obj=2701503)
    IfCharacterHuman(13, PLAYER)
    SkipLinesIfConditionFalse(2, 13)
    SkipLinesIfFlagDisabled(1, 6318)
    EnableFlag(12701997)
    SkipLinesIfFlagEnabled(5, 12701997)
    EnableObject(2701504)
    DisableObject(2701505)
    EnableTreasure(obj=2701504)
    DisableTreasure(obj=2701505)
    SkipLines(4)
    DisableObject(2701504)
    EnableObject(2701505)
    DisableTreasure(obj=2701504)
    EnableTreasure(obj=2701505)
    IfCharacterHuman(12, PLAYER)
    SkipLinesIfConditionFalse(2, 12)
    SkipLinesIfFlagDisabled(1, 6319)
    EnableFlag(12701996)
    SkipLinesIfFlagEnabled(5, 12701996)
    EnableObject(2701506)
    DisableObject(2701507)
    EnableTreasure(obj=2701506)
    DisableTreasure(obj=2701507)
    SkipLines(4)
    DisableObject(2701506)
    EnableObject(2701507)
    DisableTreasure(obj=2701506)
    EnableTreasure(obj=2701507)
    IfCharacterHuman(11, PLAYER)
    SkipLinesIfConditionFalse(2, 11)
    SkipLinesIfFlagDisabled(1, 6320)
    EnableFlag(12701995)
    SkipLinesIfFlagEnabled(5, 12701995)
    EnableObject(2701508)
    DisableObject(2701509)
    EnableTreasure(obj=2701508)
    DisableTreasure(obj=2701509)
    SkipLines(4)
    DisableObject(2701508)
    EnableObject(2701509)
    DisableTreasure(obj=2701508)
    EnableTreasure(obj=2701509)
    Event_12704842()
    Event_12704843()
    Event_12701800()
    Event_12701801()
    Event_12701802()
    Event_12704840()
    Event_12704841()
    Event_12704802()
    Event_12704803()
    Event_12704804()
    Event_12704805()
    Event_12704806()
    Event_12701803()
    Event_12704807(0, character=2700803, entity=2705001)
    Event_12704807(1, character=2700804, entity=2705002)
    Event_12704807(2, character=2700805, entity=2705003)
    Event_12704812(0, character=2700800, character_1=2700801, character_2=2700802)
    Event_12704812(1, character=2700801, character_1=2700802, character_2=2700800)
    Event_12704812(2, character=2700802, character_1=2700800, character_2=2700801)
    Event_12704815(0, character=2700810, character__set_draw_parent=2700800, model_point=60)
    Event_12704815(1, character=2700811, character__set_draw_parent=2700800, model_point=61)
    Event_12704815(3, character=2700813, character__set_draw_parent=2700801, model_point=61)
    Event_12704815(4, character=2700814, character__set_draw_parent=2700802, model_point=60)
    Event_12704825(0, character=2700801, special_effect_id=5536)
    Event_12704825(1, character=2700802, special_effect_id=5537)
    Event_12704830(0, character=2700803, entity=2705001, event_slot=0)
    Event_12704830(1, character=2700804, entity=2705002, event_slot=1)
    Event_12704830(2, character=2700805, entity=2705003, event_slot=2)
    Event_12700000(0, character=2700250, flag=52700990)
    Event_12700000(1, character=2700253, flag=52700980)
    Event_12700000(2, character=2700256, flag=52700970)
    Event_12700000(3, character=2700257, flag=52700960)
    Event_12700100(0, action_button_id=2700003, anchor_entity=2701010, flag=12700110)
    Event_12700100(1, action_button_id=2700001, anchor_entity=2701011, flag=12700111)
    Event_12700100(2, action_button_id=2700001, anchor_entity=2701012, flag=12700112)
    Event_12700110(0, obj=2701010, obj_act_id=12705720, animation_id=1, obj_act_id_1=2700030)
    Event_12700110(1, obj=2701011, obj_act_id=12705721, animation_id=1, obj_act_id_1=2700010)
    Event_12700110(2, obj=2701012, obj_act_id=12705722, animation_id=1, obj_act_id_1=2700010)
    Event_12700130()
    Event_12700131()
    Event_12700132()
    Event_12700133()
    Event_12700136()
    Event_12700137()
    Event_12700140()
    Event_12700141()
    Event_12700142()
    Event_12700143()
    Event_12700146()
    Event_12700147()
    Event_12700150()
    Event_12700170()
    Event_12700171()
    Event_12700172()
    Event_12700176()
    Event_12700990()
    Event_12700180(0, character=2700550, character_1=2700600)
    Event_12700180(1, character=2700552, character_1=2700601)
    Event_12700190(0, character=2700550, character_1=2700600)
    Event_12700190(1, character=2700552, character_1=2700601)
    Event_12700200(0, character=2700550, character_1=2700600)
    Event_12700200(1, character=2700552, character_1=2700601)
    Event_12700700()
    Event_12700704()
    Event_12700705()
    Event_12700701()
    Event_12700703()
    Event_12700706()
    Event_12700707()
    Event_12700708()
    Event_12700709()
    Event_12700722()
    Event_12700723()
    Event_12705550()
    Event_12700702()
    Event_12705552()
    Event_12700710()
    Event_12705175()
    Event_12705000(0, 2700655, 2702020, 5.0)
    Event_12705000(1, 2700103, 2702022, 5.0)
    Event_12705000(2, 2700104, 2702022, 5.0)
    Event_12705000(3, 2700653, 2702022, 15.0)
    Event_12705000(4, 2700110, 2702023, 10.0)
    Event_12705000(5, 2700111, 2702023, 10.0)
    Event_12705000(6, 2700651, 2702024, 5.0)
    Event_12705000(7, 2700320, 2702025, 5.0)
    Event_12705000(8, 2700321, 2702025, 5.0)
    Event_12705000(9, 2700513, 2702027, 10.0)
    Event_12705000(10, 2700500, 2702028, 5.0)
    Event_12705000(11, 2700700, 2702030, 10.0)
    Event_12705000(12, 2700435, 2702030, 5.0)
    Event_12705000(13, 2700401, 2702030, 5.0)
    Event_12705000(14, 2700352, 2702031, 5.0)
    Event_12705000(15, 2700904, 2702032, 15.0)
    Event_12705000(16, 2700915, 2702033, 15.0)
    Event_12705000(17, 2700450, 2702034, 15.0)
    Event_12705000(18, 2700451, 2702035, 15.0)
    Event_12705000(19, 2700555, 2702036, 10.0)
    Event_12705000(20, 2700131, 2702037, 12.0)
    Event_12705000(21, 2700652, 2702038, 5.0)
    Event_12705000(22, 2700134, 2702039, 5.0)
    Event_12705000(23, 2700100, 2702042, 8.0)
    Event_12705000(24, 2700146, 2702043, 7.0)
    Event_12705000(25, 2700660, 2702044, 7.0)
    Event_12705000(26, 2700659, 2702044, 7.0)
    Event_12705000(28, 2700440, 2702212, 5.0)
    Event_12705000(29, 2700441, 2702212, 5.0)
    Event_12705000(30, 2700113, 2702231, 8.0)
    Event_12705000(31, 2700611, 2702237, 6.0)
    Event_12705000(32, 2700620, 2702237, 6.0)
    Event_12705000(33, 2700616, 2702237, 6.0)
    Event_12705000(34, 2700618, 2702237, 6.0)
    Event_12705000(35, 2700625, 2702238, 8.0)
    Event_12705000(36, 2700621, 2702238, 8.0)
    Event_12705000(37, 2700613, 2702238, 8.0)
    Event_12705000(38, 2700614, 2702238, 8.0)
    Event_12705000(39, 2700615, 2702238, 8.0)
    Event_12705000(40, 2700751, 2702240, 8.0)
    Event_12705000(41, 2700752, 2702240, 8.0)
    Event_12705000(42, 2700705, 2702241, 6.0)
    Event_12705000(43, 2700515, 2702243, 8.0)
    Event_12705090(0, 2701000, 12705060, 12705061, 12705062, 2702050, 9.0)
    Event_12705090(1, 2701001, 12705063, 12705064, 12705065, 2702051, 5.0)
    Event_12705070(0, entity=2701000, region=2702050, entity_1=2701100, animation_id=1, animation_id_1=2)
    Event_12705070(1, entity=2701001, region=2702051, entity_1=2701101, animation_id=3, animation_id_1=4)
    Event_12705080(0, flag=12705070, obj_flag=12705060, obj_flag_1=12705061, obj_flag_2=12705062)
    Event_12705080(1, flag=12705071, obj_flag=12705063, obj_flag_1=12705064, obj_flag_2=12705065)
    Event_12701190(0, region=2702130, obj=2701050)
    Event_12701191(0, region=2702131, obj=2701051)
    Event_12705200()
    Event_12705201()
    Event_12705290(0, 2700137, 2702142, 2.0, 7012, 7013, 263098, 263052)
    Event_12705290(1, 2700138, 2702142, 2.0, 7014, 7015, 263098, 263052)
    Event_12705098()
    Event_12705099()
    Event_12705100(0, character=2700750, character_1=2700751)
    Event_12705100(1, character=2700750, character_1=2700610)
    Event_12705100(2, character=2700750, character_1=2700611)
    Event_12705100(3, character=2700750, character_1=2700612)
    Event_12705100(4, character=2700750, character_1=2700613)
    Event_12705100(5, character=2700750, character_1=2700614)
    Event_12705100(6, character=2700750, character_1=2700615)
    Event_12705100(7, character=2700750, character_1=2700616)
    Event_12705100(8, character=2700750, character_1=2700617)
    Event_12705100(9, character=2700750, character_1=2700618)
    Event_12705100(10, character=2700750, character_1=2700619)
    Event_12705100(11, character=2700750, character_1=2700620)
    Event_12705100(12, character=2700750, character_1=2700621)
    Event_12705100(13, character=2700750, character_1=2700622)
    Event_12705100(14, character=2700750, character_1=2700623)
    Event_12705100(15, character=2700750, character_1=2700624)
    Event_12705100(16, character=2700750, character_1=2700625)
    Event_12705100(17, character=2700750, character_1=2700626)
    Event_12705100(18, character=2700750, character_1=2700627)
    Event_12705100(19, character=2700750, character_1=2700628)
    Event_12705100(20, character=2700750, character_1=2700629)
    Event_12705100(21, character=2700750, character_1=2700630)
    Event_12705300(0, obj_act_id=12705095, character=2700900, obj=2701200)
    Event_12705301(0, 2700139, 2701200, 5.0, 2702244)
    Event_12705320(0, 2700427, 2702161, 0.5, 7000)
    Event_12705350()
    Event_12705360()
    Event_12705370(0, 2700400, 0.0, 2700501, 2700907)
    Event_12705370(1, 2700403, 0.30000001192092896, 2700501, 2700908)
    Event_12705370(2, 2700406, 0.20000000298023224, 2700501, 2700909)
    Event_12705370(3, 2700413, 0.6000000238418579, 2700501, 2700910)
    Event_12705370(4, 2700414, 0.30000001192092896, 2700502, 2700916)
    Event_12705370(5, 2700415, 1.0, 2700502, 2700917)
    Event_12705370(6, 2700424, 0.5, 2700502, 2700918)
    Event_12705370(7, 2700431, 0.6000000238418579, 2700502, 2700919)
    Event_12705400()
    Event_12705440(0, 2700116, 2702230, 5.0, 7004, 7005)
    Event_12705440(1, 2700117, 2702231, 5.0, 7005, 7006)
    Event_12705460(0, character=2700513)
    Event_12705460(1, character=2700515)
    Event_12705480(0, 2700301, 3021, 125, 2702250, 4.0)
    Event_12705480(1, 2700302, 3021, 150, 2702251, 10.0)
    Event_12705480(2, 2700303, 3021, 100, 2702252, 10.0)
    Event_12705480(3, 2700308, 3021, 175, 2702253, 10.0)
    Event_12705480(4, 2700309, 3021, 200, 2702254, 10.0)
    Event_12705480(5, 2700310, 3021, 225, 2702255, 10.0)
    Event_12705490()
    Event_12705491()
    Event_12705500(0, flag=12705480, character=2700301, event_slot=0, entity=2701110)
    Event_12705500(1, flag=12705481, character=2700302, event_slot=1, entity=2701112)
    Event_12705500(3, flag=12705483, character=2700308, event_slot=3, entity=2701113)
    Event_12705500(4, flag=12705484, character=2700309, event_slot=4, entity=2701114)
    Event_12705510(0, character=2700301, flag=12705500)
    Event_12705510(1, character=2700302, flag=12705501)
    Event_12705510(3, character=2700308, flag=12705503)
    Event_12705510(4, character=2700309, flag=12705504)
    Event_12705520(0, character=2700301, destination=2702046, obj=2701110, event_slot=0)
    Event_12705520(1, character=2700302, destination=2702047, obj=2701112, event_slot=1)
    Event_12705530(1, character=2700308, obj=2701113)
    Event_12705530(2, character=2700309, obj=2701114)
    Event_12705540(0, character=2700301, flag=12705500)
    Event_12705540(1, character=2700302, flag=12705501)
    Event_12705540(3, character=2700308, flag=12705503)
    Event_12705540(4, character=2700309, flag=12705504)
    Event_12705600(
        0,
        npc_part_id=2790,
        npc_part_id_1=2790,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=12705700,
        flag_1=12705760,
        character=2700750
    )
    Event_12705600(
        1,
        npc_part_id=2791,
        npc_part_id_1=2791,
        part_index=9,
        animation_id=7022,
        special_effect_id=5907,
        flag=12705700,
        flag_1=12705760,
        character=2700750
    )
    Event_12705600(
        2,
        npc_part_id=2792,
        npc_part_id_1=2792,
        part_index=10,
        animation_id=7023,
        special_effect_id=5907,
        flag=12705700,
        flag_1=12705760,
        character=2700750
    )
    Event_12705600(
        3,
        npc_part_id=2790,
        npc_part_id_1=2790,
        part_index=8,
        animation_id=7000,
        special_effect_id=5907,
        flag=12705701,
        flag_1=12705761,
        character=2700751
    )
    Event_12705600(
        4,
        npc_part_id=2791,
        npc_part_id_1=2791,
        part_index=9,
        animation_id=7022,
        special_effect_id=5907,
        flag=12705701,
        flag_1=12705761,
        character=2700751
    )
    Event_12705600(
        5,
        npc_part_id=2792,
        npc_part_id_1=2792,
        part_index=10,
        animation_id=7023,
        special_effect_id=5907,
        flag=12705701,
        flag_1=12705761,
        character=2700751
    )
    Event_12705630(
        0,
        npc_part_id=2790,
        npc_part_id_1=2790,
        part_index=8,
        part_health=40,
        flag=12705700,
        character=2700750
    )
    Event_12705630(
        1,
        npc_part_id=2791,
        npc_part_id_1=2791,
        part_index=9,
        part_health=40,
        flag=12705700,
        character=2700750
    )
    Event_12705630(
        2,
        npc_part_id=2792,
        npc_part_id_1=2792,
        part_index=10,
        part_health=40,
        flag=12705700,
        character=2700750
    )
    Event_12705630(
        3,
        npc_part_id=2790,
        npc_part_id_1=2790,
        part_index=8,
        part_health=40,
        flag=12705701,
        character=2700751
    )
    Event_12705630(
        4,
        npc_part_id=2791,
        npc_part_id_1=2791,
        part_index=9,
        part_health=40,
        flag=12705701,
        character=2700751
    )
    Event_12705630(
        5,
        npc_part_id=2792,
        npc_part_id_1=2792,
        part_index=10,
        part_health=40,
        flag=12705701,
        character=2700751
    )
    Event_12705660(0, tae_event_id=30, tae_event_id_1=40, flag=12705760, character=2700750, bit_index=1, bit_index_1=11)
    Event_12705660(1, tae_event_id=50, tae_event_id_1=40, flag=12705760, character=2700750, bit_index=2, bit_index_1=12)
    Event_12705660(2, tae_event_id=60, tae_event_id_1=40, flag=12705760, character=2700750, bit_index=3, bit_index_1=13)
    Event_12705660(3, tae_event_id=30, tae_event_id_1=40, flag=12705761, character=2700751, bit_index=1, bit_index_1=11)
    Event_12705660(4, tae_event_id=50, tae_event_id_1=40, flag=12705761, character=2700751, bit_index=2, bit_index_1=12)
    Event_12705660(5, tae_event_id=60, tae_event_id_1=40, flag=12705761, character=2700751, bit_index=3, bit_index_1=13)
    Event_12700500()
    Event_1270501()
    Event_12701000()
    Event_12701001()
    Event_12701002()
    Event_12700902(0, obj=2701912)
    Event_12700903(0, character=2700912, first_flag=1790, last_flag=1809, last_flag_1=1799, flag=1790)
    Event_12700904(0, attacked_entity=2700912, flag=72700320)
    Event_12700905(0, character=2700912, flag=72700320, first_flag=1790, last_flag=1809, flag_1=1805)
    Event_12700906(0, flag=72700321, item_lot_param_id=43120, flag_1=6676)
    Event_12700906(1, flag=72700322, item_lot_param_id=43130, flag_1=6678)
    Event_12700908(0, flag=1790, flag_1=72700330, item_lot_param_id=43110)
    Event_12700910()
    Event_12700909()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableAnimations(2703950)
    DisableGravity(2703950)
    DisableCharacterCollision(2703950)
    DisableAnimations(2703951)
    DisableGravity(2703951)
    DisableCharacterCollision(2703951)
    Event_12700720()
    DisableAI(2700756)
    DisableGravity(2700756)
    Event_12700901(0, character=2700912, obj=2701912)
    Event_12700175()


@NeverRestart(12701800)
def Event_12701800():
    """Event 12701800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(2700800)
    DisableCharacter(2700801)
    DisableCharacter(2700802)
    Kill(2700800)
    Kill(2700801)
    Kill(2700802)
    DisableObject(2701800)
    DisableObject(2701801)
    DeleteVFX(2703800)
    DeleteVFX(2703801)
    DeleteVFX(2703805)
    DisableSpawner(entity=2705001)
    DisableSpawner(entity=2705002)
    DisableSpawner(entity=2705003)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, 2700800)
    IfCharacterDead(1, 2700801)
    IfCharacterDead(1, 2700802)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2701800)
    DisableObject(2701801)
    DeleteVFX(2703800)
    DeleteVFX(2703801)
    DisableSpawner(entity=2705001)
    DisableSpawner(entity=2705002)
    DisableSpawner(entity=2705003)
    Wait(3.0)
    KillBoss(game_area_param_id=2700800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
    AwardAchievement(achievement_id=16)
    SkipLinesIfFlagEnabled(2, 6321)
    AwardItemLot(2700990, host_only=False)
    SkipLines(1)
    AwardItemLot(2700995, host_only=False)
    EnableFlag(2700)
    EnableFlag(2701)
    EnableFlag(9463)
    StopPlayLogMeasurement(measurement_id=2700000)
    StopPlayLogMeasurement(measurement_id=2700001)
    StopPlayLogMeasurement(measurement_id=2700010)
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

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(12701801)
def Event_12701801():
    """Event 12701801"""
    DisableNetworkSync()
    EndIfFlagEnabled(12701800)
    IfFlagEnabled(1, 12701800)
    IfCharacterBackreadDisabled(2, 2420800)
    IfCharacterBackreadDisabled(2, 2420801)
    IfCharacterBackreadDisabled(2, 2420802)
    IfHealthLessThanOrEqual(2, 2420800, value=0.0)
    IfHealthLessThanOrEqual(2, 2420801, value=0.0)
    IfHealthLessThanOrEqual(2, 2420802, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2702800, 500099999, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12701802)
def Event_12701802():
    """Event 12701802"""
    EndIfFlagEnabled(12701800)
    GotoIfThisEventFlagDisabled(Label.L0)
    Move(2700800, destination=2702236, destination_type=CoordEntityType.Region, short_move=True)
    Move(2700801, destination=2702235, destination_type=CoordEntityType.Region, short_move=True)
    Move(2700802, destination=2702234, destination_type=CoordEntityType.Region, short_move=True)
    DeleteVFX(2703805)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2700800, 7001, loop=True)
    ForceAnimation(2700801, 7001, loop=True)
    ForceAnimation(2700802, 7001, loop=True)
    IfFlagDisabled(1, 12701800)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2702805)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12704800)
    ForceAnimation(2700800, 7000)
    ForceAnimation(2700801, 7000)
    ForceAnimation(2700802, 7000)
    DeleteVFX(2703805)


@NeverRestart(12701803)
def Event_12701803():
    """Event 12701803"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12704800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    DeleteVFX(2703805)
    EnableFlag(12704800)
    EnableFlag(12701802)


@NeverRestart(12704840)
def Event_12704840():
    """Event 12704840"""
    EndIfFlagEnabled(12701800)
    GotoIfFlagEnabled(Label.L0, flag=12701800)
    SkipLinesIfClient(2)
    DisableObject(2701800)
    DeleteVFX(2703800)
    IfFlagDisabled(1, 12701800)
    IfFlagEnabled(1, 12701802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2701800)
    CreateVFX(2703800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12701800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=2700004, entity=2701800)
    IfFlagEnabled(3, 12701800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2702800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2702801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12704800)
    Restart()


@NeverRestart(12704841)
def Event_12704841():
    """Event 12704841"""
    DisableNetworkSync()
    EndIfFlagEnabled(12701800)
    IfFlagDisabled(1, 12701800)
    IfFlagEnabled(1, 12701802)
    IfFlagEnabled(1, 12704800)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParam(1, action_button_id=2700004, entity=2701800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2702800, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2702801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12704801)
    Restart()


@NeverRestart(12704842)
def Event_12704842():
    """Event 12704842"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2701800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12704843)
def Event_12704843():
    """Event 12704843"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=2701800, radius=4.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2701800, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12704802)
def Event_12704802():
    """Event 12704802"""
    EndIfFlagEnabled(12701800)
    DisableAI(2700800)
    DisableAI(2700801)
    DisableAI(2700802)
    DisableHealthBar(2700800)
    DisableHealthBar(2700801)
    DisableHealthBar(2700802)
    DisableSpawner(entity=2705001)
    DisableSpawner(entity=2705002)
    DisableSpawner(entity=2705003)
    DisableAI(2700803)
    DisableAI(2700804)
    DisableAI(2700805)
    DisableCharacter(2700803)
    DisableCharacter(2700804)
    DisableCharacter(2700805)
    EnableInvincibility(2700803)
    EnableInvincibility(2700804)
    EnableInvincibility(2700805)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12704800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2700800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2700801, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2700802, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12704800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2700800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2700801, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2700802, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700802)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2700800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2700801, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2700802, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700802)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2700800)
    EnableAI(2700801)
    EnableAI(2700802)
    EnableBossHealthBar(2700800, name=212010, bar_slot=2)
    EnableBossHealthBar(2700801, name=212020, bar_slot=1)
    EnableBossHealthBar(2700802, name=212030)
    CreatePlayLog(name=82)
    StartPlayLogMeasurement(measurement_id=2700010, name=98, overwrite=True)


@NeverRestart(12704803)
def Event_12704803():
    """Event 12704803"""
    DisableNetworkSync()
    EndIfFlagEnabled(12701800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2703802)
    DisableSoundEvent(sound_id=2703803)
    IfFlagDisabled(1, 12701800)
    IfFlagEnabled(1, 12704802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12704801)
    IfCharacterInsideRegion(1, PLAYER, region=2702802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=2703802)
    IfFlagEnabled(2, 12704808)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12701800)
    IfFlagEnabled(2, 12704802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12704801)
    IfCharacterInsideRegion(2, PLAYER, region=2702802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2703802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2703803)


@NeverRestart(12704804)
def Event_12704804():
    """Event 12704804"""
    DisableNetworkSync()
    EndIfFlagEnabled(12701800)
    IfFlagEnabled(0, 12704802)
    SetLockedCameraSlot(game_map=FORBIDDEN_WOODS, camera_slot=1)
    IfFlagEnabled(0, 12701800)
    SetLockedCameraSlot(game_map=FORBIDDEN_WOODS, camera_slot=0)


@NeverRestart(12704805)
def Event_12704805():
    """Event 12704805"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=12701800)
    DisableSoundEvent(sound_id=2703802)
    DisableSoundEvent(sound_id=2703803)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 12701800)
    DisableBossMusic(sound_id=2703802)
    DisableBossMusic(sound_id=2703803)
    DisableBossMusic(sound_id=-1)


@RestartOnRest(12704806)
def Event_12704806():
    """Event 12704806"""
    IfCharacterDead(1, 2700800)
    IfCharacterDead(1, 2700801)
    IfCharacterHasSpecialEffect(1, 2700802, 5539)
    IfCharacterDead(2, 2700801)
    IfCharacterDead(2, 2700802)
    IfCharacterHasSpecialEffect(2, 2700800, 5539)
    IfCharacterDead(3, 2700802)
    IfCharacterDead(3, 2700800)
    IfCharacterHasSpecialEffect(3, 2700801, 5536)
    IfHealthLessThanOrEqual(4, 2700800, value=0.30000001192092896)
    IfHealthLessThanOrEqual(4, 2700801, value=0.30000001192092896)
    IfHealthLessThanOrEqual(4, 2700802, value=0.30000001192092896)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    AICommand(2700800, command_id=10, command_slot=1)
    AICommand(2700801, command_id=10, command_slot=1)
    AICommand(2700802, command_id=10, command_slot=1)
    ReplanAI(2700800)
    ReplanAI(2700801)
    ReplanAI(2700802)
    IfCharacterHasTAEEvent(-2, 2700800, tae_event_id=40)
    IfCharacterHasTAEEvent(-2, 2700801, tae_event_id=40)
    IfCharacterHasTAEEvent(-2, 2700802, tae_event_id=40)
    IfConditionTrue(0, input_condition=-2)
    AICommand(2700800, command_id=30, command_slot=1)
    AICommand(2700801, command_id=30, command_slot=1)
    AICommand(2700802, command_id=30, command_slot=1)
    ReplanAI(2700800)
    ReplanAI(2700801)
    ReplanAI(2700802)
    Wait(10.0)
    Restart()


@RestartOnRest(12704807)
def Event_12704807(_, character: int, entity: int):
    """Event 12704807"""
    SkipLinesIfThisEventSlotFlagEnabled(3)
    DisableSpawner(entity=entity)
    DisableAI(character)
    DisableCharacter(character)
    IfCharacterHasTAEEvent(-1, 2700800, tae_event_id=20)
    IfCharacterHasTAEEvent(-1, 2700801, tae_event_id=20)
    IfCharacterHasTAEEvent(-1, 2700802, tae_event_id=20)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacter(character)
    EnableSpawner(entity=entity)
    EnableAI(character)
    ReplanAI(character)
    IfCharacterHasTAEEvent(1, character, tae_event_id=10)
    IfTimeElapsed(2, seconds=5.0)
    IfCharacterDoesNotHaveSpecialEffect(2, character, 5546)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    DisableSpawner(entity=entity)
    Kill(character)
    Restart()


@RestartOnRest(12704810)
def Event_12704810():
    """Event 12704810"""
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=2700800, radius=7.300000190734863)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=2700801, radius=7.300000190734863)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=2700802, radius=8.800000190734863)
    IfCharacterHasSpecialEffect(2, 2700800, 5535)
    IfCharacterHasSpecialEffect(2, 2700801, 5535)
    IfConditionTrue(-1, input_condition=2)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=2700800, radius=7.300000190734863)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=2700801, radius=7.300000190734863)
    IfEntityWithinDistance(3, entity=PLAYER, other_entity=2700802, radius=8.800000190734863)
    IfCharacterHasSpecialEffect(3, 2700801, 5535)
    IfCharacterHasSpecialEffect(3, 2700802, 5535)
    IfConditionTrue(-1, input_condition=3)
    IfEntityWithinDistance(4, entity=PLAYER, other_entity=2700800, radius=7.300000190734863)
    IfEntityWithinDistance(4, entity=PLAYER, other_entity=2700801, radius=7.300000190734863)
    IfEntityWithinDistance(4, entity=PLAYER, other_entity=2700802, radius=8.800000190734863)
    IfCharacterHasSpecialEffect(4, 2700802, 5535)
    IfCharacterHasSpecialEffect(4, 2700800, 5535)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    AICommand(2700800, command_id=50, command_slot=0)
    AICommand(2700801, command_id=50, command_slot=0)
    AICommand(2700802, command_id=50, command_slot=0)
    ReplanAI(2700800)
    ReplanAI(2700801)
    ReplanAI(2700802)
    Wait(2.0)
    AICommand(2700800, command_id=-1, command_slot=0)
    AICommand(2700801, command_id=-1, command_slot=0)
    AICommand(2700802, command_id=-1, command_slot=0)
    ReplanAI(2700800)
    ReplanAI(2700801)
    ReplanAI(2700802)
    Wait(5.0)
    Restart()


@RestartOnRest(12704811)
def Event_12704811():
    """Event 12704811"""
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2700800, radius=7.300000190734863)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2700801, radius=7.300000190734863)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2700802, radius=8.800000190734863)
    IfCharacterHasSpecialEffect(1, 2700800, 5535)
    IfCharacterHasSpecialEffect(1, 2700801, 5535)
    IfCharacterHasSpecialEffect(1, 2700802, 5535)
    IfConditionTrue(0, input_condition=1)
    AICommand(2700800, command_id=40, command_slot=0)
    ReplanAI(2700800)
    Wait(0.20000000298023224)
    AICommand(2700801, command_id=40, command_slot=0)
    ReplanAI(2700801)
    Wait(0.20000000298023224)
    AICommand(2700802, command_id=40, command_slot=0)
    ReplanAI(2700802)
    Wait(0.0010000000474974513)
    AICommand(2700800, command_id=-1, command_slot=0)
    AICommand(2700801, command_id=-1, command_slot=0)
    AICommand(2700802, command_id=-1, command_slot=0)
    ReplanAI(2700800)
    ReplanAI(2700801)
    ReplanAI(2700802)
    Restart()


@RestartOnRest(12704812)
def Event_12704812(_, character: int, character_1: int, character_2: int):
    """Event 12704812"""
    IfHealthLessThanOrEqual(1, character, value=0.5)
    IfHealthLessThanOrEqual(1, character_1, value=0.5)
    IfHealthLessThanOrEqual(1, character_2, value=0.5)
    IfConditionTrue(-1, input_condition=1)
    IfHealthLessThanOrEqual(-1, character, value=0.30000001192092896)
    IfHealthLessThanOrEqual(-1, character_1, value=0.30000001192092896)
    IfHealthLessThanOrEqual(-1, character_2, value=0.30000001192092896)
    IfConditionTrue(0, input_condition=-1)
    AICommand(character, command_id=50, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(0, character, tae_event_id=50)
    AICommand(character, command_id=20, command_slot=1)
    ReplanAI(character)
    SkipLinesIfEqual(1, left=character, right=2700801)
    AddSpecialEffect(character, 5539)
    IfCharacterHasTAEEvent(0, character, tae_event_id=30)
    AICommand(character, command_id=40, command_slot=1)
    ReplanAI(character)
    IfCharacterHasTAEEvent(2, character, tae_event_id=10)
    IfTimeElapsed(3, seconds=5.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    End()
    Restart()


@RestartOnRest(12704815)
def Event_12704815(_, character: int, character__set_draw_parent: int, model_point: int):
    """Event 12704815"""
    SkipLinesIfThisEventSlotFlagEnabled(4)
    IfCharacterBackreadEnabled(0, character)
    DisableCharacter(character)
    DisableGravity(character)
    IfCharacterHasTAEEvent(0, character__set_draw_parent, tae_event_id=50)
    IfHealthLessThanOrEqual(1, character__set_draw_parent, value=0.0)
    SkipLinesIfConditionFalse(1, 1)
    Kill(character)
    EnableCharacter(character)
    Move(
        character,
        destination=character__set_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        set_draw_parent=character__set_draw_parent,
    )
    SkipLinesIfThisEventSlotFlagEnabled(1)
    ForceAnimation(character, 7000)
    Restart()


@RestartOnRest(12704825)
def Event_12704825(_, character: int, special_effect_id: int):
    """Event 12704825"""
    IfCharacterHasTAEEvent(0, character, tae_event_id=40)
    CancelSpecialEffect(character, special_effect_id)
    IfFramesElapsed(-1, frames=70)
    IfAttackedWithDamageType(-1, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(character, special_effect_id)
    Restart()


@RestartOnRest(12704830)
def Event_12704830(_, character: int, entity: int, event_slot: int):
    """Event 12704830"""
    IfHealthLessThanOrEqual(1, 2700800, value=0.0)
    IfHealthLessThanOrEqual(1, 2700801, value=0.0)
    IfHealthLessThanOrEqual(1, 2700802, value=0.0)
    IfConditionTrue(0, input_condition=1)
    DisableSpawner(entity=entity)
    StopEvent(event_id=12704807, event_slot=event_slot)
    IfCharacterHasSpecialEffect(2, character, 5546)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    Kill(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    WaitRandomFrames(min_frames=0, max_frames=25)
    ForceAnimation(character, 7000, wait_for_completion=True)
    Kill(character)


@RestartOnRest(12700000)
def Event_12700000(_, character: int, flag: int):
    """Event 12700000"""
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


@NeverRestart(12700100)
def Event_12700100(_, action_button_id: int, anchor_entity: int, flag: int):
    """Event 12700100"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfActionButtonParam(1, action_button_id=action_button_id, entity=anchor_entity)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(text=10010161, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)
    Restart()


@NeverRestart(12700110)
def Event_12700110(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 12700110"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@RestartOnRest(12700130)
def Event_12700130():
    """Event 12700130"""
    EndIfFlagEnabled(12700135)
    IfFlagEnabled(1, 12700134)
    IfFlagDisabled(2, 12700134)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, condition=1)
    EndOfAnimation(obj=2701032, animation_id=0)
    DisableObjectActivation(2701030, obj_act_id=2700000)
    EnableObjectActivation(2701031, obj_act_id=2700000)
    SkipLines(3)
    EndOfAnimation(obj=2701032, animation_id=4)
    EnableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)
    SkipLinesIfFlagEnabled(4, 12700137)
    EndOfAnimation(obj=2701032, animation_id=4)
    EnableFlag(12700134)
    DisableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)


@RestartOnRest(12700131)
def Event_12700131():
    """Event 12700131"""
    IfFlagDisabled(3, 12700134)
    IfFlagEnabled(3, 12700135)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagEnabled(0, 12700137)
    IfFlagDisabled(1, 12700134)
    IfFlagDisabled(1, 12700135)
    IfCharacterInsideRegion(1, PLAYER, region=2702000)
    IfFlagDisabled(2, 12700134)
    IfFlagDisabled(2, 12700135)
    IfObjectActivated(2, obj_act_id=12700123)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12700135)
    ForceAnimation(2701032, 1)
    ForceAnimation(2701032, 2)
    WaitFrames(frames=156)
    IfAllPlayersOutsideRegion(0, region=2702001)
    ForceAnimation(2701032, 3)
    WaitFrames(frames=7)
    DisableObjectActivation(2701031, obj_act_id=2700000)
    EnableFlag(12700134)
    DisableFlag(12700135)
    EnableObjectActivation(2701030, obj_act_id=2700000)
    Restart()


@RestartOnRest(12700132)
def Event_12700132():
    """Event 12700132"""
    IfFlagEnabled(3, 12700134)
    IfFlagEnabled(3, 12700135)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagEnabled(0, 12700137)
    IfFlagEnabled(1, 12700134)
    IfFlagDisabled(1, 12700135)
    IfCharacterInsideRegion(1, PLAYER, region=2702001)
    IfFlagEnabled(2, 12700134)
    IfFlagDisabled(2, 12700135)
    IfObjectActivated(2, obj_act_id=12700122)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12700135)
    ForceAnimation(2701032, 5)
    ForceAnimation(2701032, 6)
    WaitFrames(frames=156)
    IfAllPlayersOutsideRegion(0, region=2702000)
    ForceAnimation(2701032, 7)
    WaitFrames(frames=7)
    DisableObjectActivation(2701030, obj_act_id=2700000)
    DisableFlag(12700134)
    DisableFlag(12700135)
    EnableObjectActivation(2701031, obj_act_id=2700000)
    Restart()


@RestartOnRest(12700133)
def Event_12700133():
    """Event 12700133"""
    DisableNetworkSync()
    IfFlagDisabled(-1, 12700134)
    IfFlagEnabled(-1, 12700135)
    IfFlagDisabled(-1, 12700137)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParam(1, action_button_id=7100, entity=2701030)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12700136)
def Event_12700136():
    """Event 12700136"""
    DisableNetworkSync()
    IfFlagEnabled(-1, 12700134)
    IfFlagEnabled(-1, 12700135)
    IfFlagDisabled(-1, 12700137)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParam(1, action_button_id=7100, entity=2701031)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12700137)
def Event_12700137():
    """Event 12700137"""
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)
    IfCharacterInsideRegion(0, PLAYER, region=2702002)
    CreatePlayLog(name=116)
    EnableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)


@NeverRestart(12700140)
def Event_12700140():
    """Event 12700140"""
    IfFlagEnabled(1, 12700144)
    IfFlagDisabled(2, 12700144)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, condition=1)
    EndOfAnimation(obj=2701042, animation_id=0)
    DisableObjectActivation(2701040, obj_act_id=2700000)
    EnableObjectActivation(2701041, obj_act_id=2700000)
    SkipLines(3)
    EndOfAnimation(obj=2701042, animation_id=10)
    EnableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)
    SkipLinesIfFlagEnabled(4, 12700147)
    EndOfAnimation(obj=2701042, animation_id=10)
    EnableFlag(12700144)
    DisableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)


@NeverRestart(12700141)
def Event_12700141():
    """Event 12700141"""
    IfFlagEnabled(3, 12700145)
    IfFlagDisabled(3, 12700144)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagEnabled(0, 12700147)
    IfFlagDisabled(1, 12700144)
    IfFlagDisabled(1, 12700145)
    IfCharacterInsideRegion(1, PLAYER, region=2702010)
    IfFlagDisabled(2, 12700144)
    IfFlagDisabled(2, 12700145)
    IfObjectActivated(2, obj_act_id=12700121)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12700145)
    ForceAnimation(2701042, 1)
    ForceAnimation(2701042, 8)
    WaitFrames(frames=257)
    IfAllPlayersOutsideRegion(0, region=2702011)
    ForceAnimation(2701042, 9)
    WaitFrames(frames=7)
    DisableObjectActivation(2701041, obj_act_id=2700000)
    EnableFlag(12700144)
    DisableFlag(12700145)
    EnableObjectActivation(2701040, obj_act_id=2700000)
    Restart()


@NeverRestart(12700142)
def Event_12700142():
    """Event 12700142"""
    IfFlagEnabled(3, 12700144)
    IfFlagEnabled(3, 12700145)
    GotoIfConditionTrue(Label.L0, input_condition=3)
    IfFlagEnabled(0, 12700147)
    IfFlagEnabled(1, 12700144)
    IfFlagDisabled(1, 12700145)
    IfCharacterInsideRegion(1, PLAYER, region=2702011)
    IfFlagEnabled(2, 12700144)
    IfFlagDisabled(2, 12700145)
    IfObjectActivated(2, obj_act_id=12700120)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12700145)
    ForceAnimation(2701042, 11)
    ForceAnimation(2701042, 12)
    WaitFrames(frames=257)
    IfAllPlayersOutsideRegion(0, region=2702010)
    ForceAnimation(2701042, 7)
    WaitFrames(frames=7)
    DisableObjectActivation(2701040, obj_act_id=2700000)
    DisableFlag(12700144)
    DisableFlag(12700145)
    EnableObjectActivation(2701041, obj_act_id=2700000)
    Restart()


@NeverRestart(12700143)
def Event_12700143():
    """Event 12700143"""
    DisableNetworkSync()
    IfFlagDisabled(-1, 12700144)
    IfFlagEnabled(-1, 12700145)
    IfFlagDisabled(-1, 12700147)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParam(1, action_button_id=7100, entity=2701040)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12700146)
def Event_12700146():
    """Event 12700146"""
    DisableNetworkSync()
    IfFlagEnabled(-1, 12700144)
    IfFlagEnabled(-1, 12700145)
    IfFlagDisabled(-1, 12700147)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParam(1, action_button_id=7100, entity=2701041)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12700147)
def Event_12700147():
    """Event 12700147"""
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)
    IfCharacterInsideRegion(0, PLAYER, region=2702012)
    CreatePlayLog(name=116)
    EnableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)


@NeverRestart(12700150)
def Event_12700150():
    """Event 12700150"""
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(obj=2701150, animation_id=0)
    DisableObjectActivation(2701150, obj_act_id=9942)
    EnableTreasure(obj=2701150)
    End()
    IfObjectActivated(0, obj_act_id=12700900)
    WaitFrames(frames=10)
    EnableTreasure(obj=2701150)


@RestartOnRest(12700170)
def Event_12700170():
    """Event 12700170"""
    DisableFlag(0)
    IfFlagDisabled(1, 12700175)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfFlagEnabled(2, 12700173)
    GotoIfConditionTrue(Label.L1, input_condition=2)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2701013, animation_id=3)
    DisableFlag(12700173)
    DisableNavmeshType(navmesh_id=2703050, navmesh_type=NavmeshType.Solid)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    EndOfAnimation(obj=2701013, animation_id=0)
    EnableFlag(12700173)
    EnableNavmeshType(navmesh_id=2703050, navmesh_type=NavmeshType.Solid)

    # --- 2 --- #
    DefineLabel(2)


@RestartOnRest(12700171)
def Event_12700171():
    """Event 12700171"""
    IfFlagEnabled(1, 12700173)
    IfFlagDisabled(1, 12700174)
    IfObjectActivated(1, obj_act_id=12700010)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12700173)
    EnableFlag(12700174)
    ForceAnimation(2701013, 1)
    WaitFrames(frames=100)
    DisableFlag(12700174)
    EnableObjectActivation(2701090, obj_act_id=2700000)
    DisableNavmeshType(navmesh_id=2703050, navmesh_type=NavmeshType.Solid)
    Restart()


@RestartOnRest(12700172)
def Event_12700172():
    """Event 12700172"""
    IfFlagDisabled(1, 12700173)
    IfFlagDisabled(1, 12700174)
    IfObjectActivated(1, obj_act_id=12700010)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12700173)
    EnableFlag(12700174)
    ForceAnimation(2701013, 2)
    EnableNavmeshType(navmesh_id=2703050, navmesh_type=NavmeshType.Solid)
    WaitFrames(frames=100)
    DisableFlag(12700174)
    EnableObjectActivation(2701090, obj_act_id=2700000)
    Restart()


@RestartOnRest(12700175)
def Event_12700175():
    """Event 12700175"""
    GotoIfThisEventFlagDisabled(Label.L0)
    Kill(2700145)
    DisableCharacter(2700145)
    DisableBackread(2700145)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2700145)
    WaitFrames(frames=1)


@RestartOnRest(12700176)
def Event_12700176():
    """Event 12700176"""
    DisableNetworkSync()
    IfFlagEnabled(1, 12700174)
    IfActionButtonParam(1, action_button_id=7100, entity=2701090)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart(12700180)
def Event_12700180(_, character: int, character_1: int):
    """Event 12700180"""
    DisableNetworkSync()
    IfCharacterAlive(1, character)
    IfCharacterBackreadEnabled(1, character)
    IfConditionTrue(0, input_condition=1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=40,
        short_move=True,
    )
    Restart()


@RestartOnRest(12700190)
def Event_12700190(_, character: int, character_1: int):
    """Event 12700190"""
    IfHealthLessThanOrEqual(0, character, value=0.0)
    Wait(1.0)
    ForceAnimation(character_1, 2200, wait_for_completion=True)
    DisableCharacter(character_1)


@NeverRestart(12700200)
def Event_12700200(_, character: int, character_1: int):
    """Event 12700200"""
    AddSpecialEffect(character, 5609)
    DisableGravity(character_1)


@RestartOnRest(12700500)
def Event_12700500():
    """Event 12700500"""
    IfCharacterHuman(2, PLAYER)
    EndIfConditionFalse(2)
    IfCharacterAlive(1, 2700680)
    IfAttacked(1, attacked_entity=PLAYER, attacker=2700680)
    IfHealthEqual(1, PLAYER, value=0.0)
    IfFlagEnabled(1, 9401)
    IfFlagEnabled(1, 9404)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9420)


@RestartOnRest(1270501)
def Event_1270501():
    """Event 1270501"""
    GotoIfFlagEnabled(Label.L0, flag=9802)
    EndIfFlagEnabled(9453)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2700680)


@NeverRestart(12700700)
def Event_12700700():
    """Event 12700700"""
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=15)
    DisableFlag(72700440)
    DisableFlag(72700445)
    DisableFlag(72700361)
    DisableFlag(72700364)

    # --- 9 --- #
    DefineLabel(9)
    ForceAnimation(2700756, 7002)
    GotoIfFlagEnabled(Label.L1, flag=1200)
    GotoIfFlagEnabled(Label.L2, flag=1201)
    GotoIfFlagEnabled(Label.L2, flag=1202)
    GotoIfFlagEnabled(Label.L3, flag=1203)
    GotoIfFlagEnabled(Label.L4, flag=1208)
    GotoIfFlagEnabled(Label.L4, flag=1209)
    DisableBackread(2700755)
    DisableBackread(2700756)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(2700755)
    EnableBackread(2700756)
    GotoIfFlagEnabled(Label.L5, flag=12705552)
    ForceAnimation(2700755, 103070)
    End()

    # --- 5 --- #
    DefineLabel(5)
    ForceAnimation(2700755, 103072)
    End()

    # --- 2 --- #
    DefineLabel(2)
    EnableBackread(2700755)
    EnableBackread(2700756)
    Move(2700755, destination=2702302, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2700755, 103072)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableBackread(2700755)
    DisableCharacter(2700755)
    DisableBackread(2700756)
    DisableCharacter(2700756)
    DropMandatoryTreasure(2700755)
    End()

    # --- 4 --- #
    DefineLabel(4)
    EnableBackread(2700755)
    EnableBackread(2700756)
    Move(2700755, destination=2702302, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2700755, 103072)
    End()


@NeverRestart(12700701)
def Event_12700701():
    """Event 12700701"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(-1, 2700755)
    IfCharacterDead(-1, 2700756)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1200, 1219))
    EnableFlag(1203)
    SaveRequest()


@NeverRestart(12700702)
def Event_12700702():
    """Event 12700702"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 1205)
    DisableBackread(2700755)
    DisableBackread(2700756)


@NeverRestart(12700703)
def Event_12700703():
    """Event 12700703"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthLessThan(1, 2700755, value=0.5)
    IfHealthNotEqual(1, 2700755, value=0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12705551)


@NeverRestart(12700704)
def Event_12700704():
    """Event 12700704"""
    IfFlagEnabled(0, 72700451)
    DisableFlag(72700451)
    DisableFlagRange((1200, 1219))
    EnableFlag(1209)


@NeverRestart(12700705)
def Event_12700705():
    """Event 12700705"""
    IfFlagEnabled(0, 72700450)
    DisableFlag(72700450)
    DisableFlagRange((1200, 1219))
    EnableFlag(1208)


@NeverRestart(12700706)
def Event_12700706():
    """Event 12700706"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, 2700755, value=0.0)
    IfCharacterHasSpecialEffect(1, 2700755, 151)
    IfFlagEnabled(-1, 1200)
    IfFlagEnabled(-1, 1204)
    IfFlagEnabled(-1, 1205)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2700755, 103132)


@NeverRestart(12700707)
def Event_12700707():
    """Event 12700707"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2700755)
    IfHealthGreaterThanOrEqual(1, 2700755, value=0.5)
    IfHealthNotEqual(1, 2700755, value=0.0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHasSpecialEffect(2, 2700755, 153)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    IfCharacterHasSpecialEffect(3, 2700755, 151)
    GotoIfConditionTrue(Label.L1, input_condition=3)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2700755, 103079)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(2700755, 103131)
    Restart()


@NeverRestart(12700708)
def Event_12700708():
    """Event 12700708"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2700755, 154)
    IfConditionTrue(1, input_condition=-1)
    IfHealthGreaterThanOrEqual(1, 2700755, value=0.5)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2700755, 103072)
    Restart()


@NeverRestart(12700709)
def Event_12700709():
    """Event 12700709"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2700755, 152)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2700755, 103072)
    Restart()


@NeverRestart(12700710)
def Event_12700710():
    """Event 12700710"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2702300)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9467)
    Wait(0.0)


@NeverRestart(12700720)
def Event_12700720():
    """Event 12700720"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(-1, 1200)
    IfFlagEnabled(-1, 1202)
    IfConditionTrue(3, input_condition=-1)
    IfFlagEnabled(3, 9802)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1200, 1219))
    EnableFlag(1211)

    # --- 2 --- #
    DefineLabel(2)


@NeverRestart(12700722)
def Event_12700722():
    """Event 12700722"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(frames=30)
    IfFlagEnabled(1, 1202)
    IfAttackedWithDamageType(-1, attacked_entity=2700755, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=2702301)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, 2700755, value=0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12705551)


@NeverRestart(12700723)
def Event_12700723():
    """Event 12700723"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2700755, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(2, attacked_entity=2700755, attacker=PLAYER)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(3, attacked_entity=2700755, attacker=PLAYER)
    IfHealthNotEqual(3, 2700755, value=0.0)
    IfConditionTrue(0, input_condition=3)
    EnableFlag(12705551)


@NeverRestart(12700901)
def Event_12700901(_, character: int, obj: int):
    """Event 12700901"""
    IfCharacterHuman(-1, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-1)
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1790, 1809))
    DisableFlagRange((1790, 1809))
    EnableFlag(1800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 1800)
    IfFlagEnabled(1, 72700304)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1790, 1809))
    EnableFlag(1801)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(2, 1801)
    IfFlagEnabled(2, 72700306)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    DisableFlagRange((1790, 1809))
    EnableFlag(1791)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(3, 1791)
    IfFlagEnabled(3, 12700902)
    GotoIfConditionFalse(Label.L8, input_condition=3)
    DisableFlagRange((1790, 1809))
    EnableFlag(1792)

    # --- 8 --- #
    DefineLabel(8)

    # --- 9 --- #
    DefineLabel(9)
    DisableObject(obj)
    GotoIfFlagEnabled(Label.L0, flag=1800)
    GotoIfFlagEnabled(Label.L0, flag=1801)
    GotoIfFlagEnabled(Label.L1, flag=1805)
    GotoIfFlagEnabled(Label.L2, flag=1790)
    GotoIfFlagEnabled(Label.L3, flag=1791)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.Ally)
    ForceAnimation(character, 103140)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    EnableObject(obj)
    EnableObjectInvulnerability(obj)
    CreateObjectVFX(obj, vfx_id=200, model_point=900201)
    End()

    # --- 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@NeverRestart(12700902)
def Event_12700902(_, obj: int):
    """Event 12700902"""
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    EndIfFlagEnabled(12700902)
    IfFlagEnabled(1, 1791)
    IfActionButtonParam(1, action_button_id=2700005, entity=obj)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(43100, host_only=False)
    EnableFlag(6813)
    DisableObject(obj)
    DeleteObjectVFX(obj)


@NeverRestart(12700903)
def Event_12700903(_, character: int, first_flag: int, last_flag: int, last_flag_1: int, flag: int):
    """Event 12700903"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled(flag_range=(first_flag, last_flag_1))
    IfCharacterDead(1, character)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SaveRequest()


@NeverRestart(12700904)
def Event_12700904(_, attacked_entity: int, flag: int):
    """Event 12700904"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    IfAttackedWithDamageType(0, attacked_entity=attacked_entity, attacker=PLAYER)
    WaitFrames(frames=1)
    EnableFlag(flag)


@NeverRestart(12700905)
def Event_12700905(_, character: int, flag: int, first_flag: int, last_flag: int, flag_1: int):
    """Event 12700905"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(flag)
    IfFlagEnabled(-1, flag)
    IfHealthLessThanOrEqual(-1, character, value=0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, character, value=0.0)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(character, TeamType.HostileNPC)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    SaveRequest()


@NeverRestart(12700906)
def Event_12700906(_, flag: int, item_lot_param_id: int, flag_1: int):
    """Event 12700906"""
    EndIfFlagEnabled(flag_1)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, flag)
    AwardItemLot(item_lot_param_id, host_only=False)


@NeverRestart(12700910)
def Event_12700910():
    """Event 12700910"""
    GotoIfThisEventFlagEnabled(Label.L0)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    Move(2700930, destination=2702920, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(2700930)
    DisableAI(2700930)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(-1, 12700902)
    IfFlagEnabled(-1, 1790)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(2700930)
    EnableAI(2700930)
    ChangePatrolBehavior(2700930, patrol_information_id=2703920)


@NeverRestart(12700908)
def Event_12700908(_, flag: int, flag_1: int, item_lot_param_id: int):
    """Event 12700908"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, flag_1)
    AwardItemLot(item_lot_param_id, host_only=False)
    SaveRequest()


@NeverRestart(12700909)
def Event_12700909():
    """Event 12700909"""
    GotoIfThisEventFlagEnabled(Label.L0)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2700930)
    DisableBackread(2700930)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterDead(1, 2700930)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    AwardItemLot(43840, host_only=False)
    SaveRequest()


@NeverRestart(12701000)
def Event_12701000():
    """Event 12701000"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 1367)
    IfFlagEnabled(1, 12700710)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1373)


@NeverRestart(12701001)
def Event_12701001():
    """Event 12701001"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(-1, 1361)
    IfFlagEnabled(-1, 1363)
    IfFlagEnabled(-1, 1364)
    IfFlagEnabled(-1, 1365)
    IfFlagEnabled(-1, 1369)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 12700710)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1374)


@NeverRestart(12701002)
def Event_12701002():
    """Event 12701002"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(-1, 1360)
    IfFlagEnabled(-1, 1362)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 12700710)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1375)


@RestartOnRest(12705000)
def Event_12705000(_, character: int, region: int, radius: float):
    """Event 12705000"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AICommand(character, command_id=30, command_slot=0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(2, input_condition=-1)
    IfAttacked(3, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(3, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12705098)
def Event_12705098():
    """Event 12705098"""
    ForceAnimation(0, 7010)
    SetAIParamID(0, ai_param_id=73420)


@RestartOnRest(12705099)
def Event_12705099():
    """Event 12705099"""
    IfThisEventFlagEnabled(0)
    ForceAnimation(2700750, 7012)
    SetAIParamID(2700750, ai_param_id=273400)
    ReplanAI(2700750)


@RestartOnRest(12705100)
def Event_12705100(_, character: int, character_1: int):
    """Event 12705100"""
    ForceAnimation(character, 7010, loop=True)
    SetAIParamID(character, ai_param_id=273420)
    IfAttackedWithDamageType(-1, attacked_entity=character, attacker=PLAYER)
    IfCharacterInsideRegion(-2, character_1, region=2709093)
    IfCharacterInsideRegion(-2, PLAYER, region=2709093)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(1, attacked_entity=character_1, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12705099)


@RestartOnRest(12705070)
def Event_12705070(_, entity: int, region: int, entity_1: int, animation_id: int, animation_id_1: int):
    """Event 12705070"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(entity, 0, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(entity_1, 1, wait_for_completion=True)
    ForceAnimation(entity, animation_id, wait_for_completion=True)
    ForceAnimation(entity, animation_id_1, loop=True)
    WaitFrames(frames=1)


@RestartOnRest(12705080)
def Event_12705080(_, flag: int, obj_flag: int, obj_flag_1: int, obj_flag_2: int):
    """Event 12705080"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(0, flag)

    # --- 0 --- #
    DefineLabel(0)
    RemoveObjectFlag(obj_flag=obj_flag)
    RemoveObjectFlag(obj_flag=obj_flag_1)
    RemoveObjectFlag(obj_flag=obj_flag_2)


@RestartOnRest(12705090)
def Event_12705090(_, obj: int, obj_flag: int, obj_flag_1: int, obj_flag_2: int, region: int, life: float):
    """Event 12705090"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    WaitFrames(frames=0)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=101,
        behavior_param_id=6100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=life,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=102,
        behavior_param_id=6100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=life,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=103,
        behavior_param_id=6100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=life,
        repetition_time=0.0,
    )


@RestartOnRest(12705175)
def Event_12705175():
    """Event 12705175"""
    IfCharacterBackreadEnabled(0, 2700118)
    ForceAnimation(2700118, 7010, loop=True)
    DisableAnimations(2700118)
    DisableGravity(2700118)


@RestartOnRest(12701190)
def Event_12701190(_, region: int, obj: int):
    """Event 12701190"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    PostDestruction(obj)
    RegisterLadder(start_climbing_flag=12700600, stop_climbing_flag=12700601, obj=2701070)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=region)
    DestroyObject(obj)
    PlaySoundEffect(obj, 997400000, sound_type=SoundType.o_Object)
    RegisterLadder(start_climbing_flag=12700600, stop_climbing_flag=12700601, obj=2701070)


@RestartOnRest(12701191)
def Event_12701191(_, region: int, obj: int):
    """Event 12701191"""
    SkipLinesIfThisEventSlotFlagDisabled(2)
    PostDestruction(obj)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=region)
    DestroyObject(obj)
    PlaySoundEffect(obj, 997400000, sound_type=SoundType.o_Object)


@RestartOnRest(12705200)
def Event_12705200():
    """Event 12705200"""
    ForceAnimation(2700135, 7010)
    SetAIParamID(2700135, ai_param_id=263098)
    IfHasAIStatus(-1, 2700135, ai_status=AIStatusType.Search)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=2700135, radius=2.5)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(2700135, ai_param_id=263097)
    ForceAnimation(2700135, 7016)
    IfHasAIStatus(0, 2700135, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest(12705201)
def Event_12705201():
    """Event 12705201"""
    GotoIfThisEventFlagDisabled(Label.L0)
    SetAIParamID(2700135, ai_param_id=263050)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(-1, 2700135, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2700135, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(-1, attacked_entity=2700135)
    IfConditionTrue(0, input_condition=-1)
    StopEvent(event_id=12705200)
    WaitFrames(frames=1)
    SetAIParamID(2700135, ai_param_id=263050)
    ForceAnimation(2700135, 7011)


@RestartOnRest(12705290)
def Event_12705290(
    _,
    character: int,
    region: int,
    radius: float,
    animation_id: int,
    animation_id_1: int,
    ai_param_id: int,
    ai_param_id_1: int,
):
    """Event 12705290"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(2, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(character, animation_id_1, wait_for_completion=True)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ReplanAI(character)


@NeverRestart(12705300)
def Event_12705300(_, obj_act_id: int, character: int, obj: int):
    """Event 12705300"""
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(2.299999952316284)
    Move(character, destination=obj, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    AddSpecialEffect(character, 5580)
    ForceAnimation(obj, 1)
    Wait(1.0)
    CancelSpecialEffect(character, 5580)
    WaitFrames(frames=30)
    EnableObjectActivation(obj, obj_act_id=9800)
    Restart()


@NeverRestart(12705301)
def Event_12705301(_, character: int, obj: int, radius: float, region: int):
    """Event 12705301"""
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=character, other_entity=obj, radius=radius)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(-3, PLAYER, region=region)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(3, input_condition=2)
    IfConditionFalse(4, input_condition=3)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(-4, input_condition=4)
    IfConditionTrue(0, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=4)
    ActivateObjectWithSpecificCharacter(obj=obj, objact_id=9800, relative_index=-1, character=character)

    # --- 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


@RestartOnRest(12705320)
def Event_12705320(_, character: int, region: int, seconds: float, animation_id: int):
    """Event 12705320"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableGravity(character)
    DisableAI(character)
    ForceAnimation(character, animation_id, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=character)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    Wait(seconds)
    ForceAnimation(character, -1)

    # --- 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableAI(character)


@RestartOnRest(12705350)
def Event_12705350():
    """Event 12705350"""
    IfCharacterInsideRegion(0, 2700352, region=2702180)
    Wait(10.0)
    ChangePatrolBehavior(2700352, patrol_information_id=2703011)
    IfCharacterInsideRegion(0, 2700352, region=2702181)
    Wait(10.0)
    ChangePatrolBehavior(2700352, patrol_information_id=2703010)
    Restart()


@RestartOnRest(12705360)
def Event_12705360():
    """Event 12705360"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2702190)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SetNest(2700514, region=2702190)
    AICommand(2700514, command_id=10, command_slot=0)
    ReplanAI(2700514)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterWhitePhantom(-3, PLAYER)
    IfConditionTrue(1, input_condition=-3)
    IfEntityWithinDistance(1, entity=2700514, other_entity=PLAYER, radius=7.0)
    IfConditionTrue(-1, input_condition=1)
    IfCharacterInsideRegion(-1, 2700514, region=2702190)
    IfAttackedWithDamageType(-1, attacked_entity=2700514)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(2700514, PLAYER, animation=3008)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2700514, command_id=-1, command_slot=0)
    ReplanAI(2700514)


@RestartOnRest(12705370)
def Event_12705370(_, character: int, seconds: float, character_1: int, copy_draw_parent: int):
    """Event 12705370"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EnableAI(character)
    EnableCharacter(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(character)
    DisableCharacter(character)
    IfHasAIStatus(-1, character_1, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character_1, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(character_1, 3014)
    Wait(seconds)
    Move(
        character,
        destination=copy_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=21,
        copy_draw_parent=copy_draw_parent,
    )
    WaitFrames(frames=75)
    ForceAnimation(character, 6200)
    EnableCharacter(character)
    ForceAnimation(character, 6200)
    EnableAI(character)
    ReplanAI(character)


@RestartOnRest(12705400)
def Event_12705400():
    """Event 12705400"""
    IfAllPlayersOutsideRegion(1, region=2702200)
    IfCharacterInsideRegion(1, 2700450, region=2702200)
    IfHasAIStatus(1, 2700450, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    SetAIParamID(2700450, ai_param_id=127501)
    IfCharacterInsideRegion(0, PLAYER, region=2702200)
    SetAIParamID(2700450, ai_param_id=127500)
    Restart()


@RestartOnRest(12705440)
def Event_12705440(_, character: int, region: int, radius: float, animation_id: int, animation_id_1: int):
    """Event 12705440"""
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(character, animation_id, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(2, input_condition=-1)
    IfAttackedWithDamageType(3, attacked_entity=character)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=3)
    ForceAnimation(character, animation_id_1)
    ReplanAI(character)


@RestartOnRest(12705460)
def Event_12705460(_, character: int):
    """Event 12705460"""
    SetCollisionMask(character, bit_index=6, switch_type=OnOffChange.Off)
    IfCharacterHasTAEEvent(0, character, tae_event_id=10)
    SetCollisionMask(character, bit_index=6, switch_type=OnOffChange.On)


@RestartOnRest(12705480)
def Event_12705480(_, character: int, animation_id: int, frames: int, destination: int, radius: float):
    """Event 12705480"""
    SkipLinesIfThisEventSlotFlagEnabled(1)
    ForceAnimation(character, 7000, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=radius)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfHealthValueLessThan(0, character, value=0)
    ForceAnimation(character, 7001, wait_for_completion=True)
    WaitFrames(frames=60)
    IfHealthValueLessThan(0, character, value=0)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(frames=frames)
    Restart()


@RestartOnRest(12705490)
def Event_12705490():
    """Event 12705490"""
    EndIfFlagEnabled(12700175)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2702040)
    IfCharacterInsideRegion(1, 2700145, region=2702045)
    IfHealthGreaterThan(1, 2700145, value=0.0)
    IfFlagDisabled(1, 12700173)
    IfFlagDisabled(1, 12700174)
    IfFlagEnabled(2, 12700175)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EndIfFinishedConditionTrue(input_condition=2)
    StopEvent(event_id=12705491)
    RotateToFaceEntity(2700145, 2701090, animation=7100)
    ForceAnimation(2701090, 1)
    WaitFrames(frames=55)
    EnableNavmeshType(navmesh_id=2703050, navmesh_type=NavmeshType.Solid)
    ForceAnimation(2701013, 2)
    EnableFlag(12700173)
    EnableFlag(12700174)
    WaitFrames(frames=55)
    EnableFlag(12705495)
    RotateToFaceEntity(2700145, PLAYER, animation=3009)
    WaitFrames(frames=45)
    DisableFlag(12700174)


@RestartOnRest(12705491)
def Event_12705491():
    """Event 12705491"""
    EndIfFlagEnabled(12700175)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 12700173)
    IfFlagDisabled(1, 12700174)
    IfCharacterInsideRegion(1, PLAYER, region=2702040)
    IfCharacterInsideRegion(1, 2700145, region=2702045)
    IfHealthGreaterThan(1, 2700145, value=0.0)
    IfFlagEnabled(2, 12700175)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EndIfFinishedConditionTrue(input_condition=2)
    StopEvent(event_id=12705490)
    ForceAnimation(2700145, 3009)
    EnableFlag(12705495)


@RestartOnRest(12705500)
def Event_12705500(_, flag: int, character: int, event_slot: int, entity: int):
    """Event 12705500"""
    EndIfFlagEnabled(12700175)
    EndIfFlagEnabled(12705495)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(character)
    IfFlagEnabled(0, 12705495)

    # --- 0 --- #
    DefineLabel(0)
    StopEvent(event_id=12705480, event_slot=event_slot)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    ForceAnimation(character, 7001, wait_for_completion=True)
    WaitFrames(frames=60)

    # --- 1 --- #
    DefineLabel(1)
    StopEvent(event_id=12705480, event_slot=event_slot)
    ForceAnimation(entity, 1)
    ForceAnimation(character, 3014)
    WaitFrames(frames=17)
    DisableInvincibility(character)
    EnableGravity(character)
    EnableCharacterCollision(character)
    EnableAI(character)
    SetNest(character, region=2702041)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12705510)
def Event_12705510(_, character: int, flag: int):
    """Event 12705510"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=character, attacker=PLAYER)
    IfCharacterInsideRegion(-1, character, region=2702041)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12705520)
def Event_12705520(_, character: int, destination: int, obj: int, event_slot: int):
    """Event 12705520"""
    EndIfFlagDisabled(12700175)
    StopEvent(event_id=12705480, event_slot=event_slot)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EndOfAnimation(obj=obj, animation_id=1)


@RestartOnRest(12705530)
def Event_12705530(_, character: int, obj: int):
    """Event 12705530"""
    EndIfFlagDisabled(12700175)
    Kill(character)
    DisableCharacter(character)
    DisableBackread(character)
    EndOfAnimation(obj=obj, animation_id=1)


@RestartOnRest(12705540)
def Event_12705540(_, character: int, flag: int):
    """Event 12705540"""
    EndIfFlagEnabled(12700175)
    IfFlagDisabled(1, flag)
    IfAttackedWithDamageType(1, attacked_entity=character)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(character, 5915)
    Kill(character, award_souls=True)


@NeverRestart(12705550)
def Event_12705550():
    """Event 12705550"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(2700755)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 12705551)
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionTrue(Label.L1, input_condition=15)
    WaitFrames(frames=60)
    DisableCharacter(2700755)
    End()

    # --- 1 --- #
    DefineLabel(1)
    ForceAnimation(2700755, 103073, wait_for_completion=True)
    DisableCharacter(2700755)
    Move(
        2700756,
        destination=2700755,
        destination_type=CoordEntityType.Character,
        model_point=245,
        copy_draw_parent=2700755,
    )
    EnableGravity(2700756)
    EnableAI(2700756)
    ForceAnimation(2700756, 3030)
    DisableFlagRange((1200, 1219))
    EnableFlag(1202)
    SaveRequest()


@NeverRestart(12705552)
def Event_12705552():
    """Event 12705552"""
    IfCharacterHasSpecialEffect(0, 2700755, 153)
    WaitFrames(frames=0)


@NeverRestart(12705600)
def Event_12705600(
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
    """Event 12705600"""
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
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=999999)
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


@NeverRestart(12705630)
def Event_12705630(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    part_health: int,
    flag: int,
    character: int,
):
    """Event 12705630"""
    IfEntityWithinDistance(1, entity=character, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    EnableFlag(flag)


@NeverRestart(12705660)
def Event_12705660(
    _,
    tae_event_id: int,
    tae_event_id_1: int,
    flag: int,
    character: int,
    bit_index: uchar,
    bit_index_1: uchar,
):
    """Event 12705660"""
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.On)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.Off)
    IfCharacterHasTAEEvent(0, character, tae_event_id=tae_event_id)
    EnableFlag(flag)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    IfCharacterHasTAEEvent(0, character, tae_event_id=tae_event_id_1)
    DisableFlag(flag)
    Restart()


@NeverRestart(12700990)
def Event_12700990():
    """Event 12700990"""
    EndIfThisEventFlagEnabled()
    IfStandingOnCollision(0, 2703500)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=144,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=144,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=144,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=144,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )


@RestartOnRest(12704450)
def Event_12704450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 12704450"""
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(character, region=region, reaction_range=1.0)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12704400)
def Event_12704400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12704400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(-4, 12410803)
    IfFlagEnabled(-4, 12410804)
    IfConditionTrue(1, input_condition=-4)
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
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagEnabled(-5, 12410803)
    IfFlagEnabled(-5, 12410804)
    IfConditionTrue(2, input_condition=-5)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12704401)
def Event_12704401(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12704401"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagDisabled(1, 6813)
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
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagDisabled(2, 6813)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12704410)
def Event_12704410(
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
    """Event 12704410"""
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
    IfActionButtonParam(2, action_button_id=action_button_id, entity=character)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682)
    SummonNPC(sign_type, character, region=region, summon_flag=summon_flag, dismissal_flag=dismissal_flag)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest(12704460)
def Event_12704460(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 12704460"""
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
