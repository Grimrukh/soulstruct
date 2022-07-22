"""
Forbidden Woods

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


@ContinueOnRest(0)
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
    RunEvent(9220, slot=6, args=(2700710, 12704220, 12704221, 2700, 27))
    RunEvent(9240, slot=6, args=(2700710, 12704220, 12704221, 12704222, 27))
    RunEvent(9260, slot=6, args=(2700710, 12704220, 12704221, 12704222, 27))
    RunEvent(9280, slot=6, args=(2700710, 12704220, 12704221, 2700, 12704800, 27))
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
        action_button_id=10561,
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
        action_button_id=10565,
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
        region_3=2702801,
    )
    Event_12704460(
        1,
        character=2700921,
        region=2702911,
        region_1=2702800,
        region_2=2702801,
        animation=101130,
        flag=12704800,
        region_3=2702801,
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
    AND_15.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_15)
    if FlagEnabled(6316):
        EnableFlag(12701999)
    if FlagDisabled(12701999):
        EnableObject(2701500)
        DisableObject(2701501)
        EnableTreasure(obj=2701500)
        DisableTreasure(obj=2701501)
    else:
        DisableObject(2701500)
        EnableObject(2701501)
        DisableTreasure(obj=2701500)
        EnableTreasure(obj=2701501)
    AND_14.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_14)
    if FlagEnabled(6317):
        EnableFlag(12701998)
    if FlagDisabled(12701998):
        EnableObject(2701502)
        DisableObject(2701503)
        EnableTreasure(obj=2701502)
        DisableTreasure(obj=2701503)
    else:
        DisableObject(2701502)
        EnableObject(2701503)
        DisableTreasure(obj=2701502)
        EnableTreasure(obj=2701503)
    AND_13.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_13)
    if FlagEnabled(6318):
        EnableFlag(12701997)
    if FlagDisabled(12701997):
        EnableObject(2701504)
        DisableObject(2701505)
        EnableTreasure(obj=2701504)
        DisableTreasure(obj=2701505)
    else:
        DisableObject(2701504)
        EnableObject(2701505)
        DisableTreasure(obj=2701504)
        EnableTreasure(obj=2701505)
    AND_12.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_12)
    if FlagEnabled(6319):
        EnableFlag(12701996)
    if FlagDisabled(12701996):
        EnableObject(2701506)
        DisableObject(2701507)
        EnableTreasure(obj=2701506)
        DisableTreasure(obj=2701507)
    else:
        DisableObject(2701506)
        EnableObject(2701507)
        DisableTreasure(obj=2701506)
        EnableTreasure(obj=2701507)
    AND_11.Add(CharacterHuman(PLAYER))
    SkipLinesIfConditionFalse(2, AND_11)
    if FlagEnabled(6320):
        EnableFlag(12701995)
    if FlagDisabled(12701995):
        EnableObject(2701508)
        DisableObject(2701509)
        EnableTreasure(obj=2701508)
        DisableTreasure(obj=2701509)
    else:
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
    Event_12705000(0, character=2700655, region=2702020, radius=5.0)
    Event_12705000(1, character=2700103, region=2702022, radius=5.0)
    Event_12705000(2, character=2700104, region=2702022, radius=5.0)
    Event_12705000(3, character=2700653, region=2702022, radius=15.0)
    Event_12705000(4, character=2700110, region=2702023, radius=10.0)
    Event_12705000(5, character=2700111, region=2702023, radius=10.0)
    Event_12705000(6, character=2700651, region=2702024, radius=5.0)
    Event_12705000(7, character=2700320, region=2702025, radius=5.0)
    Event_12705000(8, character=2700321, region=2702025, radius=5.0)
    Event_12705000(9, character=2700513, region=2702027, radius=10.0)
    Event_12705000(10, character=2700500, region=2702028, radius=5.0)
    Event_12705000(11, character=2700700, region=2702030, radius=10.0)
    Event_12705000(12, character=2700435, region=2702030, radius=5.0)
    Event_12705000(13, character=2700401, region=2702030, radius=5.0)
    Event_12705000(14, character=2700352, region=2702031, radius=5.0)
    Event_12705000(15, character=2700904, region=2702032, radius=15.0)
    Event_12705000(16, character=2700915, region=2702033, radius=15.0)
    Event_12705000(17, character=2700450, region=2702034, radius=15.0)
    Event_12705000(18, character=2700451, region=2702035, radius=15.0)
    Event_12705000(19, character=2700555, region=2702036, radius=10.0)
    Event_12705000(20, character=2700131, region=2702037, radius=12.0)
    Event_12705000(21, character=2700652, region=2702038, radius=5.0)
    Event_12705000(22, character=2700134, region=2702039, radius=5.0)
    Event_12705000(23, character=2700100, region=2702042, radius=8.0)
    Event_12705000(24, character=2700146, region=2702043, radius=7.0)
    Event_12705000(25, character=2700660, region=2702044, radius=7.0)
    Event_12705000(26, character=2700659, region=2702044, radius=7.0)
    Event_12705000(28, character=2700440, region=2702212, radius=5.0)
    Event_12705000(29, character=2700441, region=2702212, radius=5.0)
    Event_12705000(30, character=2700113, region=2702231, radius=8.0)
    Event_12705000(31, character=2700611, region=2702237, radius=6.0)
    Event_12705000(32, character=2700620, region=2702237, radius=6.0)
    Event_12705000(33, character=2700616, region=2702237, radius=6.0)
    Event_12705000(34, character=2700618, region=2702237, radius=6.0)
    Event_12705000(35, character=2700625, region=2702238, radius=8.0)
    Event_12705000(36, character=2700621, region=2702238, radius=8.0)
    Event_12705000(37, character=2700613, region=2702238, radius=8.0)
    Event_12705000(38, character=2700614, region=2702238, radius=8.0)
    Event_12705000(39, character=2700615, region=2702238, radius=8.0)
    Event_12705000(40, character=2700751, region=2702240, radius=8.0)
    Event_12705000(41, character=2700752, region=2702240, radius=8.0)
    Event_12705000(42, character=2700705, region=2702241, radius=6.0)
    Event_12705000(43, character=2700515, region=2702243, radius=8.0)
    Event_12705090(
        0,
        obj=2701000,
        obj_flag=12705060,
        obj_flag_1=12705061,
        obj_flag_2=12705062,
        region=2702050,
        life=9.0,
    )
    Event_12705090(
        1,
        obj=2701001,
        obj_flag=12705063,
        obj_flag_1=12705064,
        obj_flag_2=12705065,
        region=2702051,
        life=5.0,
    )
    Event_12705070(0, entity=2701000, region=2702050, entity_1=2701100, animation_id=1, animation_id_1=2)
    Event_12705070(1, entity=2701001, region=2702051, entity_1=2701101, animation_id=3, animation_id_1=4)
    Event_12705080(0, flag=12705070, obj_flag=12705060, obj_flag_1=12705061, obj_flag_2=12705062)
    Event_12705080(1, flag=12705071, obj_flag=12705063, obj_flag_1=12705064, obj_flag_2=12705065)
    Event_12701190(0, region=2702130, obj=2701050)
    Event_12701191(0, region=2702131, obj=2701051)
    Event_12705200()
    Event_12705201()
    Event_12705290(
        0,
        character=2700137,
        region=2702142,
        radius=2.0,
        animation_id=7012,
        animation_id_1=7013,
        ai_param_id=263098,
        ai_param_id_1=263052,
    )
    Event_12705290(
        1,
        character=2700138,
        region=2702142,
        radius=2.0,
        animation_id=7014,
        animation_id_1=7015,
        ai_param_id=263098,
        ai_param_id_1=263052,
    )
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
    Event_12705301(0, character=2700139, obj=2701200, radius=5.0, region=2702244)
    Event_12705320(0, character=2700427, region=2702161, seconds=0.5, animation_id=7000)
    Event_12705350()
    Event_12705360()
    Event_12705370(0, character=2700400, seconds=0.0, character_1=2700501, copy_draw_parent=2700907)
    Event_12705370(1, character=2700403, seconds=0.30000001192092896, character_1=2700501, copy_draw_parent=2700908)
    Event_12705370(2, character=2700406, seconds=0.20000000298023224, character_1=2700501, copy_draw_parent=2700909)
    Event_12705370(3, character=2700413, seconds=0.6000000238418579, character_1=2700501, copy_draw_parent=2700910)
    Event_12705370(4, character=2700414, seconds=0.30000001192092896, character_1=2700502, copy_draw_parent=2700916)
    Event_12705370(5, character=2700415, seconds=1.0, character_1=2700502, copy_draw_parent=2700917)
    Event_12705370(6, character=2700424, seconds=0.5, character_1=2700502, copy_draw_parent=2700918)
    Event_12705370(7, character=2700431, seconds=0.6000000238418579, character_1=2700502, copy_draw_parent=2700919)
    Event_12705400()
    Event_12705440(0, character=2700116, region=2702230, radius=5.0, animation_id=7004, animation_id_1=7005)
    Event_12705440(1, character=2700117, region=2702231, radius=5.0, animation_id=7005, animation_id_1=7006)
    Event_12705460(0, character=2700513)
    Event_12705460(1, character=2700515)
    Event_12705480(0, character=2700301, animation_id=3021, frames=125, destination=2702250, radius=4.0)
    Event_12705480(1, character=2700302, animation_id=3021, frames=150, destination=2702251, radius=10.0)
    Event_12705480(2, character=2700303, animation_id=3021, frames=100, destination=2702252, radius=10.0)
    Event_12705480(3, character=2700308, animation_id=3021, frames=175, destination=2702253, radius=10.0)
    Event_12705480(4, character=2700309, animation_id=3021, frames=200, destination=2702254, radius=10.0)
    Event_12705480(5, character=2700310, animation_id=3021, frames=225, destination=2702255, radius=10.0)
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
        character=2700750,
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
        character=2700750,
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
        character=2700750,
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
        character=2700751,
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
        character=2700751,
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
        character=2700751,
    )
    Event_12705630(
        0,
        npc_part_id=2790,
        npc_part_id_1=2790,
        part_index=8,
        part_health=40,
        flag=12705700,
        character=2700750,
    )
    Event_12705630(
        1,
        npc_part_id=2791,
        npc_part_id_1=2791,
        part_index=9,
        part_health=40,
        flag=12705700,
        character=2700750,
    )
    Event_12705630(
        2,
        npc_part_id=2792,
        npc_part_id_1=2792,
        part_index=10,
        part_health=40,
        flag=12705700,
        character=2700750,
    )
    Event_12705630(
        3,
        npc_part_id=2790,
        npc_part_id_1=2790,
        part_index=8,
        part_health=40,
        flag=12705701,
        character=2700751,
    )
    Event_12705630(
        4,
        npc_part_id=2791,
        npc_part_id_1=2791,
        part_index=9,
        part_health=40,
        flag=12705701,
        character=2700751,
    )
    Event_12705630(
        5,
        npc_part_id=2792,
        npc_part_id_1=2792,
        part_index=10,
        part_health=40,
        flag=12705701,
        character=2700751,
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


@ContinueOnRest(50)
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


@ContinueOnRest(12701800)
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

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterDead(2700800))
    AND_1.Add(CharacterDead(2700801))
    AND_1.Add(CharacterDead(2700802))
    
    MAIN.Await(AND_1)
    
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
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RunEvent(9350, slot=0, args=(2,))
    AwardAchievement(achievement_id=16)
    if FlagDisabled(6321):
        AwardItemLot(2700990, host_only=False)
    else:
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

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(CharacterWhitePhantom(PLAYER))
    
    Wait(0.0)


@ContinueOnRest(12701801)
def Event_12701801():
    """Event 12701801"""
    DisableNetworkSync()
    if FlagEnabled(12701800):
        return
    AND_1.Add(FlagEnabled(12701800))
    AND_2.Add(CharacterBackreadDisabled(2420800))
    AND_2.Add(CharacterBackreadDisabled(2420801))
    AND_2.Add(CharacterBackreadDisabled(2420802))
    AND_2.Add(HealthRatio(2420800) <= 0.0)
    AND_2.Add(HealthRatio(2420801) <= 0.0)
    AND_2.Add(HealthRatio(2420802) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    PlaySoundEffect(2702800, 500099999, sound_type=SoundType.c_CharacterMotion)


@ContinueOnRest(12701802)
def Event_12701802():
    """Event 12701802"""
    if FlagEnabled(12701800):
        return
    GotoIfThisEventFlagDisabled(Label.L0)
    Move(2700800, destination=2702236, destination_type=CoordEntityType.Region, short_move=True)
    Move(2700801, destination=2702235, destination_type=CoordEntityType.Region, short_move=True)
    Move(2700802, destination=2702234, destination_type=CoordEntityType.Region, short_move=True)
    DeleteVFX(2703805)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2700800, 7001, loop=True)
    ForceAnimation(2700801, 7001, loop=True)
    ForceAnimation(2700802, 7001, loop=True)
    AND_1.Add(FlagDisabled(12701800))
    AND_1.Add(ThisEventFlagDisabled())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2702805))
    
    MAIN.Await(AND_1)
    
    EnableFlag(12704800)
    ForceAnimation(2700800, 7000)
    ForceAnimation(2700801, 7000)
    ForceAnimation(2700802, 7000)
    DeleteVFX(2703805)


@ContinueOnRest(12701803)
def Event_12701803():
    """Event 12701803"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12704800))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    DeleteVFX(2703805)
    EnableFlag(12704800)
    EnableFlag(12701802)


@ContinueOnRest(12704840)
def Event_12704840():
    """Event 12704840"""
    if FlagEnabled(12701800):
        return
    GotoIfFlagEnabled(Label.L0, flag=12701800)
    SkipLinesIfClient(2)
    DisableObject(2701800)
    DeleteVFX(2703800)
    AND_1.Add(FlagDisabled(12701800))
    AND_1.Add(FlagEnabled(12701802))
    
    MAIN.Await(AND_1)
    
    EnableObject(2701800)
    CreateVFX(2703800)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12701800))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2700004, entity=2701800))
    AND_3.Add(FlagEnabled(12701800))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    RotateToFaceEntity(PLAYER, 2702800, animation=101130)
    AND_4.Add(CharacterHuman(PLAYER))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=2702801))
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(TimeElapsed(seconds=2.0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_5)
    EnableFlag(12704800)
    Restart()


@ContinueOnRest(12704841)
def Event_12704841():
    """Event 12704841"""
    DisableNetworkSync()
    if FlagEnabled(12701800):
        return
    AND_1.Add(FlagDisabled(12701800))
    AND_1.Add(FlagEnabled(12701802))
    AND_1.Add(FlagEnabled(12704800))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2700004, entity=2701800))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 2702800, animation=101130)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2702801))
    AND_3.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    EnableFlag(12704801)
    Restart()


@ContinueOnRest(12704842)
def Event_12704842():
    """Event 12704842"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2701800, radius=4.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12704843)
def Event_12704843():
    """Event 12704843"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2701800, radius=4.0))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2701800, radius=8.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12704802)
def Event_12704802():
    """Event 12704802"""
    if FlagEnabled(12701800):
        return
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
    
    MAIN.Await(FlagEnabled(12704800))
    
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2700800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2700801, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2700802, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12704800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2700800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2700801, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2700802, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700802)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2700800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2700801, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2700802, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2700802)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableAI(2700800)
    EnableAI(2700801)
    EnableAI(2700802)
    EnableBossHealthBar(2700800, name=212010, bar_slot=2)
    EnableBossHealthBar(2700801, name=212020, bar_slot=1)
    EnableBossHealthBar(2700802, name=212030)
    CreatePlayLog(name=82)
    StartPlayLogMeasurement(measurement_id=2700010, name=98, overwrite=True)


@ContinueOnRest(12704803)
def Event_12704803():
    """Event 12704803"""
    DisableNetworkSync()
    if FlagEnabled(12701800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2703802)
    DisableSoundEvent(sound_id=2703803)
    AND_1.Add(FlagDisabled(12701800))
    AND_1.Add(FlagEnabled(12704802))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(12704801))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2702802))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=2703802)
    AND_2.Add(FlagEnabled(12704808))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12701800))
    AND_2.Add(FlagEnabled(12704802))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(12704801))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2702802))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=2703802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2703803)


@ContinueOnRest(12704804)
def Event_12704804():
    """Event 12704804"""
    DisableNetworkSync()
    if FlagEnabled(12701800):
        return
    
    MAIN.Await(FlagEnabled(12704802))
    
    SetLockedCameraSlot(game_map=FORBIDDEN_WOODS, camera_slot=1)
    
    MAIN.Await(FlagEnabled(12701800))
    
    SetLockedCameraSlot(game_map=FORBIDDEN_WOODS, camera_slot=0)


@ContinueOnRest(12704805)
def Event_12704805():
    """Event 12704805"""
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, flag=12701800)
    DisableSoundEvent(sound_id=2703802)
    DisableSoundEvent(sound_id=2703803)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(12701800))
    
    DisableBossMusic(sound_id=2703802)
    DisableBossMusic(sound_id=2703803)
    DisableBossMusic(sound_id=-1)


@RestartOnRest(12704806)
def Event_12704806():
    """Event 12704806"""
    AND_1.Add(CharacterDead(2700800))
    AND_1.Add(CharacterDead(2700801))
    AND_1.Add(CharacterHasSpecialEffect(2700802, 5539))
    AND_2.Add(CharacterDead(2700801))
    AND_2.Add(CharacterDead(2700802))
    AND_2.Add(CharacterHasSpecialEffect(2700800, 5539))
    AND_3.Add(CharacterDead(2700802))
    AND_3.Add(CharacterDead(2700800))
    AND_3.Add(CharacterHasSpecialEffect(2700801, 5536))
    AND_4.Add(HealthRatio(2700800) <= 0.30000001192092896)
    AND_4.Add(HealthRatio(2700801) <= 0.30000001192092896)
    AND_4.Add(HealthRatio(2700802) <= 0.30000001192092896)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    AICommand(2700800, command_id=10, command_slot=1)
    AICommand(2700801, command_id=10, command_slot=1)
    AICommand(2700802, command_id=10, command_slot=1)
    ReplanAI(2700800)
    ReplanAI(2700801)
    ReplanAI(2700802)
    OR_2.Add(CharacterHasTAEEvent(2700800, tae_event_id=40))
    OR_2.Add(CharacterHasTAEEvent(2700801, tae_event_id=40))
    OR_2.Add(CharacterHasTAEEvent(2700802, tae_event_id=40))
    
    MAIN.Await(OR_2)
    
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
    if ThisEventSlotFlagDisabled():
        DisableSpawner(entity=entity)
        DisableAI(character)
        DisableCharacter(character)
    OR_1.Add(CharacterHasTAEEvent(2700800, tae_event_id=20))
    OR_1.Add(CharacterHasTAEEvent(2700801, tae_event_id=20))
    OR_1.Add(CharacterHasTAEEvent(2700802, tae_event_id=20))
    
    MAIN.Await(OR_1)
    
    EnableCharacter(character)
    EnableSpawner(entity=entity)
    EnableAI(character)
    ReplanAI(character)
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    AND_2.Add(TimeElapsed(seconds=5.0))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5546))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    DisableSpawner(entity=entity)
    Kill(character)
    Restart()


@RestartOnRest(12704810)
def Event_12704810():
    """Event 12704810"""
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700800, radius=7.300000190734863))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700801, radius=7.300000190734863))
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700802, radius=8.800000190734863))
    AND_2.Add(CharacterHasSpecialEffect(2700800, 5535))
    AND_2.Add(CharacterHasSpecialEffect(2700801, 5535))
    OR_1.Add(AND_2)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700800, radius=7.300000190734863))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700801, radius=7.300000190734863))
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700802, radius=8.800000190734863))
    AND_3.Add(CharacterHasSpecialEffect(2700801, 5535))
    AND_3.Add(CharacterHasSpecialEffect(2700802, 5535))
    OR_1.Add(AND_3)
    AND_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700800, radius=7.300000190734863))
    AND_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700801, radius=7.300000190734863))
    AND_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700802, radius=8.800000190734863))
    AND_4.Add(CharacterHasSpecialEffect(2700802, 5535))
    AND_4.Add(CharacterHasSpecialEffect(2700800, 5535))
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
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
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700800, radius=7.300000190734863))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700801, radius=7.300000190734863))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700802, radius=8.800000190734863))
    AND_1.Add(CharacterHasSpecialEffect(2700800, 5535))
    AND_1.Add(CharacterHasSpecialEffect(2700801, 5535))
    AND_1.Add(CharacterHasSpecialEffect(2700802, 5535))
    
    MAIN.Await(AND_1)
    
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
    AND_1.Add(HealthRatio(character) <= 0.5)
    AND_1.Add(HealthRatio(character_1) <= 0.5)
    AND_1.Add(HealthRatio(character_2) <= 0.5)
    OR_1.Add(AND_1)
    OR_1.Add(HealthRatio(character) <= 0.30000001192092896)
    OR_1.Add(HealthRatio(character_1) <= 0.30000001192092896)
    OR_1.Add(HealthRatio(character_2) <= 0.30000001192092896)
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=50, command_slot=1)
    ReplanAI(character)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=50))
    
    AICommand(character, command_id=20, command_slot=1)
    ReplanAI(character)
    if ValueNotEqual(left=character, right=2700801):
        AddSpecialEffect(character, 5539)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=30))
    
    AICommand(character, command_id=40, command_slot=1)
    ReplanAI(character)
    AND_2.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    AND_3.Add(TimeElapsed(seconds=5.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    End()
    Restart()


@RestartOnRest(12704815)
def Event_12704815(_, character: int, character__set_draw_parent: int, model_point: int):
    """Event 12704815"""
    if ThisEventSlotFlagDisabled():
        MAIN.Await(CharacterBackreadEnabled(character))
    
        DisableCharacter(character)
        DisableGravity(character)
    
        MAIN.Await(CharacterHasTAEEvent(character__set_draw_parent, tae_event_id=50))
    AND_1.Add(HealthRatio(character__set_draw_parent) <= 0.0)
    SkipLinesIfConditionFalse(1, AND_1)
    Kill(character)
    EnableCharacter(character)
    Move(
        character,
        destination=character__set_draw_parent,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        set_draw_parent=character__set_draw_parent,
    )
    if ThisEventSlotFlagDisabled():
        ForceAnimation(character, 7000)
    Restart()


@RestartOnRest(12704825)
def Event_12704825(_, character: int, special_effect_id: int):
    """Event 12704825"""
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=40))
    
    RemoveSpecialEffect(character, special_effect_id)
    OR_1.Add(FramesElapsed(frames=70))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(character, special_effect_id)
    Restart()


@RestartOnRest(12704830)
def Event_12704830(_, character: int, entity: int, event_slot: int):
    """Event 12704830"""
    AND_1.Add(HealthRatio(2700800) <= 0.0)
    AND_1.Add(HealthRatio(2700801) <= 0.0)
    AND_1.Add(HealthRatio(2700802) <= 0.0)
    
    MAIN.Await(AND_1)
    
    DisableSpawner(entity=entity)
    StopEvent(event_id=12704807, event_slot=event_slot)
    AND_2.Add(CharacterHasSpecialEffect(character, 5546))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Kill(character)
    End()

    # --- Label 0 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(CharacterHuman(PLAYER))
    SkipLinesIfClient(1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    Wait(0.0)


@ContinueOnRest(12700100)
def Event_12700100(_, action_button_id: int, anchor_entity: int, flag: int):
    """Event 12700100"""
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
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(0.0)
    Restart()


@ContinueOnRest(12700110)
def Event_12700110(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 12700110"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    Wait(0.0)


@RestartOnRest(12700130)
def Event_12700130():
    """Event 12700130"""
    if FlagEnabled(12700135):
        return
    AND_1.Add(FlagEnabled(12700134))
    AND_2.Add(FlagDisabled(12700134))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(4, input_condition=AND_1)
    EndOfAnimation(obj=2701032, animation_id=0)
    DisableObjectActivation(2701030, obj_act_id=2700000)
    EnableObjectActivation(2701031, obj_act_id=2700000)
    SkipLines(3)
    EndOfAnimation(obj=2701032, animation_id=4)
    EnableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)
    if FlagDisabled(12700137):
        EndOfAnimation(obj=2701032, animation_id=4)
        EnableFlag(12700134)
        DisableObjectActivation(2701030, obj_act_id=2700000)
        DisableObjectActivation(2701031, obj_act_id=2700000)


@RestartOnRest(12700131)
def Event_12700131():
    """Event 12700131"""
    AND_3.Add(FlagDisabled(12700134))
    AND_3.Add(FlagEnabled(12700135))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    
    MAIN.Await(FlagEnabled(12700137))
    
    AND_1.Add(FlagDisabled(12700134))
    AND_1.Add(FlagDisabled(12700135))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2702000))
    AND_2.Add(FlagDisabled(12700134))
    AND_2.Add(FlagDisabled(12700135))
    AND_2.Add(ObjectActivated(obj_act_id=12700123))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12700135)
    ForceAnimation(2701032, 1)
    ForceAnimation(2701032, 2)
    WaitFrames(frames=156)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2702001))
    
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
    AND_3.Add(FlagEnabled(12700134))
    AND_3.Add(FlagEnabled(12700135))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    
    MAIN.Await(FlagEnabled(12700137))
    
    AND_1.Add(FlagEnabled(12700134))
    AND_1.Add(FlagDisabled(12700135))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2702001))
    AND_2.Add(FlagEnabled(12700134))
    AND_2.Add(FlagDisabled(12700135))
    AND_2.Add(ObjectActivated(obj_act_id=12700122))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12700135)
    ForceAnimation(2701032, 5)
    ForceAnimation(2701032, 6)
    WaitFrames(frames=156)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2702000))
    
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
    OR_1.Add(FlagDisabled(12700134))
    OR_1.Add(FlagEnabled(12700135))
    OR_1.Add(FlagDisabled(12700137))
    AND_1.Add(OR_1)
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2701030))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12700136)
def Event_12700136():
    """Event 12700136"""
    DisableNetworkSync()
    OR_1.Add(FlagEnabled(12700134))
    OR_1.Add(FlagEnabled(12700135))
    OR_1.Add(FlagDisabled(12700137))
    AND_1.Add(OR_1)
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2701031))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest(12700137)
def Event_12700137():
    """Event 12700137"""
    if ThisEventSlotFlagEnabled():
        return
    DisableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2702002))
    
    CreatePlayLog(name=116)
    EnableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)


@ContinueOnRest(12700140)
def Event_12700140():
    """Event 12700140"""
    AND_1.Add(FlagEnabled(12700144))
    AND_2.Add(FlagDisabled(12700144))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(4, input_condition=AND_1)
    EndOfAnimation(obj=2701042, animation_id=0)
    DisableObjectActivation(2701040, obj_act_id=2700000)
    EnableObjectActivation(2701041, obj_act_id=2700000)
    SkipLines(3)
    EndOfAnimation(obj=2701042, animation_id=10)
    EnableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)
    if FlagDisabled(12700147):
        EndOfAnimation(obj=2701042, animation_id=10)
        EnableFlag(12700144)
        DisableObjectActivation(2701040, obj_act_id=2700000)
        DisableObjectActivation(2701041, obj_act_id=2700000)


@ContinueOnRest(12700141)
def Event_12700141():
    """Event 12700141"""
    AND_3.Add(FlagEnabled(12700145))
    AND_3.Add(FlagDisabled(12700144))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    
    MAIN.Await(FlagEnabled(12700147))
    
    AND_1.Add(FlagDisabled(12700144))
    AND_1.Add(FlagDisabled(12700145))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2702010))
    AND_2.Add(FlagDisabled(12700144))
    AND_2.Add(FlagDisabled(12700145))
    AND_2.Add(ObjectActivated(obj_act_id=12700121))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12700145)
    ForceAnimation(2701042, 1)
    ForceAnimation(2701042, 8)
    WaitFrames(frames=257)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2702011))
    
    ForceAnimation(2701042, 9)
    WaitFrames(frames=7)
    DisableObjectActivation(2701041, obj_act_id=2700000)
    EnableFlag(12700144)
    DisableFlag(12700145)
    EnableObjectActivation(2701040, obj_act_id=2700000)
    Restart()


@ContinueOnRest(12700142)
def Event_12700142():
    """Event 12700142"""
    AND_3.Add(FlagEnabled(12700144))
    AND_3.Add(FlagEnabled(12700145))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    
    MAIN.Await(FlagEnabled(12700147))
    
    AND_1.Add(FlagEnabled(12700144))
    AND_1.Add(FlagDisabled(12700145))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2702011))
    AND_2.Add(FlagEnabled(12700144))
    AND_2.Add(FlagDisabled(12700145))
    AND_2.Add(ObjectActivated(obj_act_id=12700120))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12700145)
    ForceAnimation(2701042, 11)
    ForceAnimation(2701042, 12)
    WaitFrames(frames=257)
    
    MAIN.Await(AllPlayersOutsideRegion(region=2702010))
    
    ForceAnimation(2701042, 7)
    WaitFrames(frames=7)
    DisableObjectActivation(2701040, obj_act_id=2700000)
    DisableFlag(12700144)
    DisableFlag(12700145)
    EnableObjectActivation(2701041, obj_act_id=2700000)
    Restart()


@ContinueOnRest(12700143)
def Event_12700143():
    """Event 12700143"""
    DisableNetworkSync()
    OR_1.Add(FlagDisabled(12700144))
    OR_1.Add(FlagEnabled(12700145))
    OR_1.Add(FlagDisabled(12700147))
    AND_1.Add(OR_1)
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2701040))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12700146)
def Event_12700146():
    """Event 12700146"""
    DisableNetworkSync()
    OR_1.Add(FlagEnabled(12700144))
    OR_1.Add(FlagEnabled(12700145))
    OR_1.Add(FlagDisabled(12700147))
    AND_1.Add(OR_1)
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2701041))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12700147)
def Event_12700147():
    """Event 12700147"""
    if ThisEventSlotFlagEnabled():
        return
    DisableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2702012))
    
    CreatePlayLog(name=116)
    EnableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)


@ContinueOnRest(12700150)
def Event_12700150():
    """Event 12700150"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=2701150, animation_id=0)
        DisableObjectActivation(2701150, obj_act_id=9942)
        EnableTreasure(obj=2701150)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=12700900))
    
    WaitFrames(frames=10)
    EnableTreasure(obj=2701150)


@RestartOnRest(12700170)
def Event_12700170():
    """Event 12700170"""
    DisableFlag(0)
    AND_1.Add(FlagDisabled(12700175))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(12700173))
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2701013, animation_id=3)
    DisableFlag(12700173)
    DisableNavmeshType(navmesh_id=2703050, navmesh_type=NavmeshType.Solid)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(obj=2701013, animation_id=0)
    EnableFlag(12700173)
    EnableNavmeshType(navmesh_id=2703050, navmesh_type=NavmeshType.Solid)

    # --- Label 2 --- #
    DefineLabel(2)


@RestartOnRest(12700171)
def Event_12700171():
    """Event 12700171"""
    AND_1.Add(FlagEnabled(12700173))
    AND_1.Add(FlagDisabled(12700174))
    AND_1.Add(ObjectActivated(obj_act_id=12700010))
    
    MAIN.Await(AND_1)
    
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
    AND_1.Add(FlagDisabled(12700173))
    AND_1.Add(FlagDisabled(12700174))
    AND_1.Add(ObjectActivated(obj_act_id=12700010))
    
    MAIN.Await(AND_1)
    
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

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(2700145))
    
    WaitFrames(frames=1)


@RestartOnRest(12700176)
def Event_12700176():
    """Event 12700176"""
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(12700174))
    AND_1.Add(ActionButtonParamActivated(action_button_id=7100, entity=2701090))
    
    MAIN.Await(AND_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12700180)
def Event_12700180(_, character: int, character_1: int):
    """Event 12700180"""
    DisableNetworkSync()
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
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
    MAIN.Await(HealthRatio(character) <= 0.0)
    
    Wait(1.0)
    ForceAnimation(character_1, 2200, wait_for_completion=True)
    DisableCharacter(character_1)


@ContinueOnRest(12700200)
def Event_12700200(_, character: int, character_1: int):
    """Event 12700200"""
    AddSpecialEffect(character, 5609)
    DisableGravity(character_1)


@RestartOnRest(12700500)
def Event_12700500():
    """Event 12700500"""
    AND_2.Add(CharacterHuman(PLAYER))
    if not AND_2:
        return
    AND_1.Add(CharacterAlive(2700680))
    AND_1.Add(Attacked(attacked_entity=PLAYER, attacker=2700680))
    AND_1.Add(HealthRatio(PLAYER) == 0.0)
    AND_1.Add(FlagEnabled(9401))
    AND_1.Add(FlagEnabled(9404))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9420)


@RestartOnRest(1270501)
def Event_1270501():
    """Event 1270501"""
    GotoIfFlagEnabled(Label.L0, flag=9802)
    if FlagEnabled(9453):
        return

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBackread(2700680)


@ContinueOnRest(12700700)
def Event_12700700():
    """Event 12700700"""
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L9, input_condition=AND_15)
    DisableFlag(72700440)
    DisableFlag(72700445)
    DisableFlag(72700361)
    DisableFlag(72700364)

    # --- Label 9 --- #
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

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(2700755)
    EnableBackread(2700756)
    GotoIfFlagEnabled(Label.L5, flag=12705552)
    ForceAnimation(2700755, 103070)
    End()

    # --- Label 5 --- #
    DefineLabel(5)
    ForceAnimation(2700755, 103072)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(2700755)
    EnableBackread(2700756)
    Move(2700755, destination=2702302, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2700755, 103072)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(2700755)
    DisableCharacter(2700755)
    DisableBackread(2700756)
    DisableCharacter(2700756)
    DropMandatoryTreasure(2700755)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    EnableBackread(2700755)
    EnableBackread(2700756)
    Move(2700755, destination=2702302, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2700755, 103072)
    End()


@ContinueOnRest(12700701)
def Event_12700701():
    """Event 12700701"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    OR_1.Add(CharacterDead(2700755))
    OR_1.Add(CharacterDead(2700756))
    AND_1.Add(OR_1)
    AND_1.Add(Host())
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1200, 1219))
    EnableFlag(1203)
    SaveRequest()


@ContinueOnRest(12700702)
def Event_12700702():
    """Event 12700702"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(1205))
    
    DisableBackread(2700755)
    DisableBackread(2700756)


@ContinueOnRest(12700703)
def Event_12700703():
    """Event 12700703"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(2700755) < 0.5)
    AND_1.Add(HealthRatio(2700755) != 0.0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(12705551)


@ContinueOnRest(12700704)
def Event_12700704():
    """Event 12700704"""
    MAIN.Await(FlagEnabled(72700451))
    
    DisableFlag(72700451)
    DisableFlagRange((1200, 1219))
    EnableFlag(1209)


@ContinueOnRest(12700705)
def Event_12700705():
    """Event 12700705"""
    MAIN.Await(FlagEnabled(72700450))
    
    DisableFlag(72700450)
    DisableFlagRange((1200, 1219))
    EnableFlag(1208)


@ContinueOnRest(12700706)
def Event_12700706():
    """Event 12700706"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(HealthRatio(2700755) == 0.0)
    AND_1.Add(CharacterHasSpecialEffect(2700755, 151))
    OR_1.Add(FlagEnabled(1200))
    OR_1.Add(FlagEnabled(1204))
    OR_1.Add(FlagEnabled(1205))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2700755, 103132)


@ContinueOnRest(12700707)
def Event_12700707():
    """Event 12700707"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=2700755))
    AND_1.Add(HealthRatio(2700755) >= 0.5)
    AND_1.Add(HealthRatio(2700755) != 0.0)
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterHasSpecialEffect(2700755, 153))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(CharacterHasSpecialEffect(2700755, 151))
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2700755, 103079)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(2700755, 103131)
    Restart()


@ContinueOnRest(12700708)
def Event_12700708():
    """Event 12700708"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(2700755, 154))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(2700755) >= 0.5)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2700755, 103072)
    Restart()


@ContinueOnRest(12700709)
def Event_12700709():
    """Event 12700709"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(CharacterHasSpecialEffect(2700755, 152))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2700755, 103072)
    Restart()


@ContinueOnRest(12700710)
def Event_12700710():
    """Event 12700710"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2702300))
    
    MAIN.Await(AND_1)
    
    EnableFlag(9467)
    Wait(0.0)


@ContinueOnRest(12700720)
def Event_12700720():
    """Event 12700720"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return

    # --- Label 1 --- #
    DefineLabel(1)
    OR_1.Add(FlagEnabled(1200))
    OR_1.Add(FlagEnabled(1202))
    AND_3.Add(OR_1)
    AND_3.Add(FlagEnabled(9802))
    GotoIfConditionFalse(Label.L2, input_condition=AND_3)
    DisableFlagRange((1200, 1219))
    EnableFlag(1211)

    # --- Label 2 --- #
    DefineLabel(2)


@ContinueOnRest(12700722)
def Event_12700722():
    """Event 12700722"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    WaitFrames(frames=30)
    AND_1.Add(FlagEnabled(1202))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2700755, attacker=PLAYER))
    OR_1.Add(CharacterInsideRegion(PLAYER, region=2702301))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(2700755) != 0.0)
    
    MAIN.Await(AND_1)
    
    EnableFlag(12705551)


@ContinueOnRest(12700723)
def Event_12700723():
    """Event 12700723"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=2700755, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    AND_2.Add(AttackedWithDamageType(attacked_entity=2700755, attacker=PLAYER))
    
    MAIN.Await(AND_2)
    
    WaitFrames(frames=1)
    AND_3.Add(AttackedWithDamageType(attacked_entity=2700755, attacker=PLAYER))
    AND_3.Add(HealthRatio(2700755) != 0.0)
    
    MAIN.Await(AND_3)
    
    EnableFlag(12705551)


@ContinueOnRest(12700901)
def Event_12700901(_, character: int, obj: int):
    """Event 12700901"""
    OR_1.Add(CharacterHuman(PLAYER))
    GotoIfConditionFalse(Label.L9, input_condition=OR_1)
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(1790, 1809))
    DisableFlagRange((1790, 1809))
    EnableFlag(1800)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(1800))
    AND_1.Add(FlagEnabled(72700304))
    GotoIfConditionFalse(Label.L1, input_condition=AND_1)
    DisableFlagRange((1790, 1809))
    EnableFlag(1801)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(1801))
    AND_2.Add(FlagEnabled(72700306))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    DisableFlagRange((1790, 1809))
    EnableFlag(1791)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_3.Add(FlagEnabled(1791))
    AND_3.Add(FlagEnabled(12700902))
    GotoIfConditionFalse(Label.L8, input_condition=AND_3)
    DisableFlagRange((1790, 1809))
    EnableFlag(1792)

    # --- Label 8 --- #
    DefineLabel(8)

    # --- Label 9 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    SetTeamType(character, TeamType.Ally)
    ForceAnimation(character, 103140)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    EnableObject(obj)
    EnableObjectInvulnerability(obj)
    CreateObjectVFX(obj, vfx_id=200, model_point=900201)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@ContinueOnRest(12700902)
def Event_12700902(_, obj: int):
    """Event 12700902"""
    OR_15.Add(CharacterHuman(PLAYER))
    if not OR_15:
        return
    if FlagEnabled(12700902):
        return
    AND_1.Add(FlagEnabled(1791))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2700005, entity=obj))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(43100, host_only=False)
    EnableFlag(6813)
    DisableObject(obj)
    DeleteObjectVFX(obj)


@ContinueOnRest(12700903)
def Event_12700903(_, character: int, first_flag: int, last_flag: int, last_flag_1: int, flag: int):
    """Event 12700903"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    EndIfFlagRangeAnyEnabled(flag_range=(first_flag, last_flag_1))
    AND_1.Add(CharacterDead(character))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag)
    SaveRequest()


@ContinueOnRest(12700904)
def Event_12700904(_, attacked_entity: int, flag: int):
    """Event 12700904"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    EnableFlag(flag)


@ContinueOnRest(12700905)
def Event_12700905(_, character: int, flag: int, first_flag: int, last_flag: int, flag_1: int):
    """Event 12700905"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    DisableFlag(flag)
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(HealthRatio(character) <= 0.8999999761581421)
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableFlagRange((first_flag, last_flag))
    EnableFlag(flag_1)
    SaveRequest()


@ContinueOnRest(12700906)
def Event_12700906(_, flag: int, item_lot_param_id: int, flag_1: int):
    """Event 12700906"""
    if FlagEnabled(flag_1):
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    AwardItemLot(item_lot_param_id, host_only=False)


@ContinueOnRest(12700910)
def Event_12700910():
    """Event 12700910"""
    GotoIfThisEventFlagEnabled(Label.L0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    Move(2700930, destination=2702920, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(2700930)
    DisableAI(2700930)
    AND_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(FlagEnabled(12700902))
    OR_1.Add(FlagEnabled(1790))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableCharacter(2700930)
    EnableAI(2700930)
    ChangePatrolBehavior(2700930, patrol_information_id=2703920)


@ContinueOnRest(12700908)
def Event_12700908(_, flag: int, flag_1: int, item_lot_param_id: int):
    """Event 12700908"""
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    GotoIfFlagDisabled(Label.L0, flag=flag)
    GotoIfFlagDisabled(Label.L1, flag=flag_1)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(flag_1)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    AwardItemLot(item_lot_param_id, host_only=False)
    SaveRequest()


@ContinueOnRest(12700909)
def Event_12700909():
    """Event 12700909"""
    GotoIfThisEventFlagEnabled(Label.L0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(2700930)
    DisableBackread(2700930)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(CharacterDead(2700930))
    
    MAIN.Await(AND_1)
    
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AwardItemLot(43840, host_only=False)
    SaveRequest()


@ContinueOnRest(12701000)
def Event_12701000():
    """Event 12701000"""
    if ThisEventFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    AND_1.Add(FlagEnabled(1367))
    AND_1.Add(FlagEnabled(12700710))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1360, 1379))
    EnableFlag(1373)


@ContinueOnRest(12701001)
def Event_12701001():
    """Event 12701001"""
    if ThisEventFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    OR_1.Add(FlagEnabled(1361))
    OR_1.Add(FlagEnabled(1363))
    OR_1.Add(FlagEnabled(1364))
    OR_1.Add(FlagEnabled(1365))
    OR_1.Add(FlagEnabled(1369))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(12700710))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1360, 1379))
    EnableFlag(1374)


@ContinueOnRest(12701002)
def Event_12701002():
    """Event 12701002"""
    if ThisEventFlagEnabled():
        return
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    OR_1.Add(FlagEnabled(1360))
    OR_1.Add(FlagEnabled(1362))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(12700710))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((1360, 1379))
    EnableFlag(1375)


@RestartOnRest(12705000)
def Event_12705000(_, character: int, region: int, radius: float):
    """Event 12705000"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AICommand(character, command_id=30, command_slot=0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(OR_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(OR_1)
    AND_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_3.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
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
    MAIN.Await(ThisEventFlagEnabled())
    
    ForceAnimation(2700750, 7012)
    SetAIParamID(2700750, ai_param_id=273400)
    ReplanAI(2700750)


@RestartOnRest(12705100)
def Event_12705100(_, character: int, character_1: int):
    """Event 12705100"""
    ForceAnimation(character, 7010, loop=True)
    SetAIParamID(character, ai_param_id=273420)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_2.Add(CharacterInsideRegion(character_1, region=2709093))
    OR_2.Add(CharacterInsideRegion(PLAYER, region=2709093))
    AND_1.Add(OR_2)
    AND_1.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=PLAYER))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    EnableFlag(12705099)


@RestartOnRest(12705070)
def Event_12705070(_, entity: int, region: int, entity_1: int, animation_id: int, animation_id_1: int):
    """Event 12705070"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(entity, 0, loop=True)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(entity_1, 1, wait_for_completion=True)
    ForceAnimation(entity, animation_id, wait_for_completion=True)
    ForceAnimation(entity, animation_id_1, loop=True)
    WaitFrames(frames=1)


@RestartOnRest(12705080)
def Event_12705080(_, flag: int, obj_flag: int, obj_flag_1: int, obj_flag_2: int):
    """Event 12705080"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(flag))

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveObjectFlag(obj_flag=obj_flag)
    RemoveObjectFlag(obj_flag=obj_flag_1)
    RemoveObjectFlag(obj_flag=obj_flag_2)


@RestartOnRest(12705090)
def Event_12705090(_, obj: int, obj_flag: int, obj_flag_1: int, obj_flag_2: int, region: int, life: float):
    """Event 12705090"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
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
    MAIN.Await(CharacterBackreadEnabled(2700118))
    
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

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    DestroyObject(obj)
    PlaySoundEffect(obj, 997400000, sound_type=SoundType.o_Object)
    RegisterLadder(start_climbing_flag=12700600, stop_climbing_flag=12700601, obj=2701070)


@RestartOnRest(12701191)
def Event_12701191(_, region: int, obj: int):
    """Event 12701191"""
    if ThisEventSlotFlagEnabled():
        PostDestruction(obj)
        End()
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    DestroyObject(obj)
    PlaySoundEffect(obj, 997400000, sound_type=SoundType.o_Object)


@RestartOnRest(12705200)
def Event_12705200():
    """Event 12705200"""
    ForceAnimation(2700135, 7010)
    SetAIParamID(2700135, ai_param_id=263098)
    OR_1.Add(HasAIStatus(2700135, ai_status=AIStatusType.Search))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2700135, radius=2.5))
    
    MAIN.Await(OR_1)
    
    SetAIParamID(2700135, ai_param_id=263097)
    ForceAnimation(2700135, 7016)
    
    MAIN.Await(HasAIStatus(2700135, ai_status=AIStatusType.Normal))
    
    Restart()


@RestartOnRest(12705201)
def Event_12705201():
    """Event 12705201"""
    GotoIfThisEventFlagDisabled(Label.L0)
    SetAIParamID(2700135, ai_param_id=263050)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(HasAIStatus(2700135, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(2700135, ai_status=AIStatusType.Battle))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2700135))
    
    MAIN.Await(OR_1)
    
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
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(OR_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    ForceAnimation(character, animation_id_1, wait_for_completion=True)

    # --- Label 0 --- #
    DefineLabel(0)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ReplanAI(character)


@ContinueOnRest(12705300)
def Event_12705300(_, obj_act_id: int, character: int, obj: int):
    """Event 12705300"""
    MAIN.Await(ObjectActivated(obj_act_id=obj_act_id))
    
    Wait(2.299999952316284)
    Move(character, destination=obj, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    AddSpecialEffect(character, 5580)
    ForceAnimation(obj, 1)
    Wait(1.0)
    RemoveSpecialEffect(character, 5580)
    WaitFrames(frames=30)
    EnableObjectActivation(obj, obj_act_id=9800)
    Restart()


@ContinueOnRest(12705301)
def Event_12705301(_, character: int, obj: int, radius: float, region: int):
    """Event 12705301"""
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=obj, radius=radius))
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_2)
    OR_3.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(OR_3)
    AND_3.Add(AND_1)
    AND_3.Add(AND_2)
    AND_4.Add(not AND_3)
    OR_4.Add(AND_3)
    OR_4.Add(AND_4)
    
    MAIN.Await(OR_4)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_4)
    ActivateObjectWithSpecificCharacter(obj=obj, objact_id=9800, relative_index=-1, character=character)

    # --- Label 0 --- #
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
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(OR_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    ForceAnimation(character, -1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableAI(character)


@RestartOnRest(12705350)
def Event_12705350():
    """Event 12705350"""
    MAIN.Await(CharacterInsideRegion(2700352, region=2702180))
    
    Wait(10.0)
    ChangePatrolBehavior(2700352, patrol_information_id=2703011)
    
    MAIN.Await(CharacterInsideRegion(2700352, region=2702181))
    
    Wait(10.0)
    ChangePatrolBehavior(2700352, patrol_information_id=2703010)
    Restart()


@RestartOnRest(12705360)
def Event_12705360():
    """Event 12705360"""
    if ThisEventFlagEnabled():
        return
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2702190))
    AND_2.Add(OR_2)
    
    MAIN.Await(AND_2)
    
    SetNest(2700514, region=2702190)
    AICommand(2700514, command_id=10, command_slot=0)
    ReplanAI(2700514)
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_3)
    AND_1.Add(EntityWithinDistance(entity=2700514, other_entity=PLAYER, radius=7.0))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterInsideRegion(2700514, region=2702190))
    OR_1.Add(AttackedWithDamageType(attacked_entity=2700514))
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionFalse(Label.L0, input_condition=AND_1)
    RotateToFaceEntity(2700514, PLAYER, animation=3008)

    # --- Label 0 --- #
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

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    DisableCharacter(character)
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
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
    AND_1.Add(AllPlayersOutsideRegion(region=2702200))
    AND_1.Add(CharacterInsideRegion(2700450, region=2702200))
    AND_1.Add(HasAIStatus(2700450, ai_status=AIStatusType.Normal))
    
    MAIN.Await(AND_1)
    
    SetAIParamID(2700450, ai_param_id=127501)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2702200))
    
    SetAIParamID(2700450, ai_param_id=127500)
    Restart()


@RestartOnRest(12705440)
def Event_12705440(_, character: int, region: int, radius: float, animation_id: int, animation_id_1: int):
    """Event 12705440"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_1.Add(OR_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    AND_2.Add(OR_1)
    AND_3.Add(AttackedWithDamageType(attacked_entity=character))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    
    MAIN.Await(OR_2)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    ForceAnimation(character, animation_id_1)
    ReplanAI(character)


@RestartOnRest(12705460)
def Event_12705460(_, character: int):
    """Event 12705460"""
    SetCollisionMask(character, bit_index=6, switch_type=OnOffChange.Off)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=10))
    
    SetCollisionMask(character, bit_index=6, switch_type=OnOffChange.On)


@RestartOnRest(12705480)
def Event_12705480(_, character: int, animation_id: int, frames: int, destination: int, radius: float):
    """Event 12705480"""
    if ThisEventSlotFlagDisabled():
        ForceAnimation(character, 7000, loop=True)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    
    MAIN.Await(AND_1)
    
    if ThisEventSlotFlagDisabled():
        MAIN.Await(HealthValue(character) < 0)
    
        ForceAnimation(character, 7001, wait_for_completion=True)
    WaitFrames(frames=60)
    
    MAIN.Await(HealthValue(character) < 0)
    
    ForceAnimation(character, animation_id, wait_for_completion=True)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(frames=frames)
    Restart()


@RestartOnRest(12705490)
def Event_12705490():
    """Event 12705490"""
    if FlagEnabled(12700175):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2702040))
    AND_1.Add(CharacterInsideRegion(2700145, region=2702045))
    AND_1.Add(HealthRatio(2700145) > 0.0)
    AND_1.Add(FlagDisabled(12700173))
    AND_1.Add(FlagDisabled(12700174))
    AND_2.Add(FlagEnabled(12700175))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    EndIfFinishedConditionTrue(input_condition=AND_2)
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
    if FlagEnabled(12700175):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(12700173))
    AND_1.Add(FlagDisabled(12700174))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2702040))
    AND_1.Add(CharacterInsideRegion(2700145, region=2702045))
    AND_1.Add(HealthRatio(2700145) > 0.0)
    AND_2.Add(FlagEnabled(12700175))
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    EndIfFinishedConditionTrue(input_condition=AND_2)
    StopEvent(event_id=12705490)
    ForceAnimation(2700145, 3009)
    EnableFlag(12705495)


@RestartOnRest(12705500)
def Event_12705500(_, flag: int, character: int, event_slot: int, entity: int):
    """Event 12705500"""
    if FlagEnabled(12700175):
        return
    if FlagEnabled(12705495):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(character)
    
    MAIN.Await(FlagEnabled(12705495))

    # --- Label 0 --- #
    DefineLabel(0)
    StopEvent(event_id=12705480, event_slot=event_slot)
    GotoIfFlagEnabled(Label.L1, flag=flag)
    ForceAnimation(character, 7001, wait_for_completion=True)
    WaitFrames(frames=60)

    # --- Label 1 --- #
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
    OR_2.Add(CharacterHuman(PLAYER))
    OR_2.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=5.0))
    AND_1.Add(OR_2)
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(CharacterInsideRegion(character, region=2702041))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12705520)
def Event_12705520(_, character: int, destination: int, obj: int, event_slot: int):
    """Event 12705520"""
    if FlagDisabled(12700175):
        return
    StopEvent(event_id=12705480, event_slot=event_slot)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    EndOfAnimation(obj=obj, animation_id=1)


@RestartOnRest(12705530)
def Event_12705530(_, character: int, obj: int):
    """Event 12705530"""
    if FlagDisabled(12700175):
        return
    Kill(character)
    DisableCharacter(character)
    DisableBackread(character)
    EndOfAnimation(obj=obj, animation_id=1)


@RestartOnRest(12705540)
def Event_12705540(_, character: int, flag: int):
    """Event 12705540"""
    if FlagEnabled(12700175):
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(AttackedWithDamageType(attacked_entity=character))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 5915)
    Kill(character, award_souls=True)


@ContinueOnRest(12705550)
def Event_12705550():
    """Event 12705550"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(2700755)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(FlagEnabled(12705551))
    
    AND_15.Add(CharacterHuman(PLAYER))
    GotoIfConditionTrue(Label.L1, input_condition=AND_15)
    WaitFrames(frames=60)
    DisableCharacter(2700755)
    End()

    # --- Label 1 --- #
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


@ContinueOnRest(12705552)
def Event_12705552():
    """Event 12705552"""
    MAIN.Await(CharacterHasSpecialEffect(2700755, 153))
    
    WaitFrames(frames=0)


@ContinueOnRest(12705600)
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
    MAIN.Await(FlagEnabled(flag))
    
    AND_1.Add(CharacterPartHealth(character, npc_part_id=npc_part_id_1) <= 0)
    AND_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(FlagEnabled(flag_1))
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
    
    AddSpecialEffect(character, special_effect_id)
    DisableFlag(flag_1)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=300))
    
    SetNPCPartHealth(character, npc_part_id=npc_part_id_1, desired_health=80, overwrite_max=True)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    RemoveSpecialEffect(character, special_effect_id)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    WaitFrames(frames=10)
    Restart()


@ContinueOnRest(12705630)
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
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=10.0))
    
    MAIN.Await(AND_1)
    
    CreateNPCPart(character, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(character, npc_part_id=npc_part_id_1, material_sfx_id=64, material_vfx_id=64)
    EnableFlag(flag)


@ContinueOnRest(12705660)
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
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=tae_event_id))
    
    EnableFlag(flag)
    SetCollisionMask(character, bit_index=bit_index, switch_type=OnOffChange.Off)
    SetCollisionMask(character, bit_index=bit_index_1, switch_type=OnOffChange.On)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=tae_event_id_1))
    
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12700990)
def Event_12700990():
    """Event 12700990"""
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(PlayerStandingOnCollision(2703500))
    
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


@RestartOnRest(12704400)
def Event_12704400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12704400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    OR_4.Add(FlagEnabled(12410803))
    OR_4.Add(FlagEnabled(12410804))
    AND_1.Add(OR_4)
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
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    OR_5.Add(FlagEnabled(12410803))
    OR_5.Add(FlagEnabled(12410804))
    AND_2.Add(OR_5)
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12704401)
def Event_12704401(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12704401"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    AND_1.Add(PlayerHasGood(4312))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagDisabled(flag_2))
    AND_1.Add(FlagDisabled(flag_3))
    AND_1.Add(ClientTypeCountComparison(client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_1.Add(FlagDisabled(6813))
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
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 6142))
    AND_2.Add(FlagDisabled(6813))
    OR_3.Add(FlagDisabled(flag_4))
    AND_2.Add(OR_3)
    AND_3.Add(Host())
    AND_3.Add(not AND_2)
    
    MAIN.Await(AND_3)
    
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
