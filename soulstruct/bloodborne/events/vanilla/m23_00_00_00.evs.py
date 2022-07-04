"""
linked:
220

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス_撃破
52: PC情報_ボス撃破_血に渇いた獣
86: ボス_戦闘開始
102: ボス戦_撃破時間
120: PC情報_ボス撃破_嵐の獣（骨）
154: PC情報_廃墟到達時
176: 廃墟_スナイパー領域侵入
202: 廃墟_ご神体破壊
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
    RunEvent(7000, slot=5, args=(2300950, 2301950, 999, 12307800))
    RunEvent(7000, slot=6, args=(2300951, 2301951, 12301800, 12307820))
    RunEvent(7000, slot=7, args=(2300952, 2301952, 12301700, 12307840))
    RunEvent(7100, slot=5, args=(72300200, 2301950))
    RunEvent(7100, slot=6, args=(72300201, 2301951))
    RunEvent(7100, slot=7, args=(72300202, 2301952))
    RunEvent(7200, slot=5, args=(72300100, 2301950, 2102950))
    RunEvent(7200, slot=6, args=(72300101, 2301951, 2102950))
    RunEvent(7200, slot=7, args=(72300102, 2301952, 2102950))
    RunEvent(7300, slot=5, args=(72102300, 2301950))
    RunEvent(7300, slot=6, args=(72102301, 2301951))
    RunEvent(7300, slot=7, args=(72102302, 2301952))
    RunEvent(7600, slot=10, args=(2301999, 2303999))
    RunEvent(9200, slot=1, args=(2303900,))
    RunEvent(9220, slot=1, args=(2300750, 12304220, 12304221, 2300, 23, 0), arg_types="iiiiBB")
    RunEvent(9240, slot=1, args=(2300750, 12304220, 12304221, 12304222, 23, 0), arg_types="iiiiBB")
    RunEvent(9260, slot=1, args=(2300750, 12304220, 12304221, 12304222, 23, 0), arg_types="iiiiBB")
    RunEvent(9280, slot=1, args=(2300750, 12304220, 12304221, 2300, 12304800, 23, 0), arg_types="iiiiiBB")
    DeleteVFX(2303400, erase_root_only=False)
    DeleteVFX(2303910, erase_root_only=False)
    DeleteVFX(2303911, erase_root_only=False)
    Event_12304400(0, flag=12304440, vfx_id=2303400, flag_1=12304420, flag_2=12304430, flag_3=12301800, flag_4=6001)
    Event_12304401(0, flag=12304441, vfx_id=2303910, flag_1=12304421, flag_2=12304431, flag_3=12301700, flag_4=12304422)
    Event_12304402(0, flag=12304442, vfx_id=2303911, flag_1=12304422, flag_2=12304432, flag_3=12301700, flag_4=12304421)
    Event_12304410(
        0,
        sign_type=0,
        character=2300740,
        region=2302720,
        summon_flag=12304420,
        dismissal_flag=12304430,
        flag=12304440,
        flag_1=12301800,
        action_button_id=10576
    )
    Event_12304410(
        1,
        sign_type=0,
        character=2300930,
        region=2302910,
        summon_flag=12304421,
        dismissal_flag=12304431,
        flag=12304441,
        flag_1=12301700,
        action_button_id=10568
    )
    Event_12304410(
        2,
        sign_type=5,
        character=2300931,
        region=2302913,
        summon_flag=12304422,
        dismissal_flag=12304432,
        flag=12304442,
        flag_1=12301700,
        action_button_id=10564
    )
    Event_12304450(0, character=2300740, region=2302722, flag=12304420, flag_1=12304430, flag_2=12304800)
    Event_12304450(1, character=2300930, region=2302911, flag=12304421, flag_1=12304431, flag_2=12304700)
    Event_12304450(2, character=2300931, region=2302914, flag=12304422, flag_1=12304432, flag_2=12304700)
    Event_12304460(
        0,
        character=2300740,
        region=2302722,
        region_1=2302800,
        region_2=2302801,
        animation=101130,
        flag=12304450,
        region_3=2302801
    )
    Event_12304460(
        1,
        character=2300930,
        region=2302911,
        region_1=2302810,
        region_2=2302811,
        animation=101130,
        flag=12304451,
        region_3=2302811
    )
    Event_12304460(
        2,
        character=2300931,
        region=2302914,
        region_1=2302810,
        region_2=2302811,
        animation=101130,
        flag=12304452,
        region_3=2302811
    )
    StartPlayLogMeasurement(measurement_id=2300000, name=0, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2300001, name=18, overwrite=True)
    RegisterLadder(start_climbing_flag=12301000, stop_climbing_flag=12301001, obj=2301100)
    RegisterLadder(start_climbing_flag=12301002, stop_climbing_flag=12301003, obj=2301101)
    RegisterLadder(start_climbing_flag=12301004, stop_climbing_flag=12301005, obj=2301102)
    RegisterLadder(start_climbing_flag=12301006, stop_climbing_flag=12301007, obj=2301103)
    RegisterLadder(start_climbing_flag=12301008, stop_climbing_flag=12301009, obj=2301104)
    RegisterLadder(start_climbing_flag=12301010, stop_climbing_flag=12301011, obj=2301105)
    CreateObjectVFX(2301200, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301201, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301202, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301203, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301204, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301205, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301206, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301207, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301208, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301209, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301210, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301211, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301212, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301213, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301214, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301215, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301216, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301217, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301218, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301219, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301230, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301221, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301222, vfx_id=1, model_point=923230)
    CreateObjectVFX(2301223, vfx_id=1, model_point=923230)
    CreateProjectileOwner(entity=2300270)
    CreateProjectileOwner(entity=2300271)
    CreateProjectileOwner(entity=2300272)
    CreateHazard(
        obj_flag=12300300,
        obj=2301400,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300301,
        obj=2301401,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300302,
        obj=2301402,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300303,
        obj=2301403,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300304,
        obj=2301404,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300305,
        obj=2301405,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300306,
        obj=2301406,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300307,
        obj=2301407,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300308,
        obj=2301408,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300309,
        obj=2301409,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300310,
        obj=2301410,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300311,
        obj=2301411,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300312,
        obj=2301412,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300313,
        obj=2301413,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300314,
        obj=2301414,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300315,
        obj=2301415,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300316,
        obj=2301416,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300317,
        obj=2301417,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300318,
        obj=2301418,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300319,
        obj=2301419,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300320,
        obj=2301420,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300321,
        obj=2301421,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300322,
        obj=2301422,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    Event_12304812()
    Event_12304813()
    Event_12301800()
    Event_12301801()
    Event_12301802()
    Event_12304810()
    Event_12304811()
    Event_12304802()
    Event_12304803()
    Event_12304804()
    Event_12304805()
    Event_12304807()
    Event_12304808()
    Event_12301803()
    Event_12304732()
    Event_12304733()
    Event_12301700()
    Event_12301701()
    Event_12301702()
    Event_12304730()
    Event_12304731()
    Event_12304702()
    Event_12304703()
    Event_12304704()
    Event_12304705()
    Event_12304707()
    Event_12301703()
    Event_12304715(
        0,
        npc_part_id=2300,
        npc_part_id_1=2300,
        part_index=1,
        special_effect_id=480,
        special_effect_id_1=490,
        animation_id=8000,
        part_health=130
    )
    Event_12304715(
        1,
        npc_part_id=2301,
        npc_part_id_1=2301,
        part_index=2,
        special_effect_id=481,
        special_effect_id_1=491,
        animation_id=8010,
        part_health=150
    )
    Event_12304715(
        2,
        npc_part_id=2302,
        npc_part_id_1=2302,
        part_index=3,
        special_effect_id=482,
        special_effect_id_1=492,
        animation_id=8030,
        part_health=150
    )
    Event_12304715(
        3,
        npc_part_id=2303,
        npc_part_id_1=2303,
        part_index=4,
        special_effect_id=483,
        special_effect_id_1=493,
        animation_id=8020,
        part_health=200
    )
    Event_12304715(
        4,
        npc_part_id=2304,
        npc_part_id_1=2304,
        part_index=5,
        special_effect_id=484,
        special_effect_id_1=494,
        animation_id=8040,
        part_health=200
    )
    Event_12300100()
    Event_12300110(0, action_button_id=7031, anchor_entity=2301701, flag=12300120)
    Event_12300110(1, action_button_id=7000, anchor_entity=2301700, flag=12300121)
    Event_12300110(2, action_button_id=2300031, anchor_entity=2301010, flag=12300122)
    Event_12300110(3, action_button_id=2300030, anchor_entity=2301020, flag=12300180)
    Event_12300120(0, obj=2301701, obj_act_id=12300212, animation_id=1, obj_act_id_1=2300000)
    Event_12300120(1, obj=2301700, obj_act_id=12300211, animation_id=1, obj_act_id_1=2300001)
    Event_12300120(2, obj=2301010, obj_act_id=12300213, animation_id=1, obj_act_id_1=2300010)
    Event_12300130()
    Event_12300140()
    Event_12300160()
    Event_12300180()
    Event_12300190()
    Event_12300201()
    Event_12300210()
    Event_12300220(0, character=2300250, flag=52300990)
    Event_12300220(1, character=2300251, flag=52300980)
    Event_12300220(2, character=2300252, flag=52300970)
    Event_12300230()
    Event_12300235()
    Event_12300240()
    Event_12300250()
    Event_12300300()
    Event_12300310(0, obj=2301050, obj_act_id=12300900, obj_act_id_1=9942)
    Event_12305000()
    Event_12305001()
    Event_12305010(0, character__projectile_id=2300304, animation_id=7008, event_slot=1, ai_param_id=109000)
    Event_12305010(1, character__projectile_id=2300402, animation_id=7002, event_slot=2, ai_param_id=109010)
    Event_12305020()
    Event_12305021()
    Event_12305022()
    Event_12305023()
    Event_12305030(0, region=2302032, obj=2301269, region_1=2300910)
    Event_12305030(1, region=2302033, obj=2301266, region_1=2300911)
    Event_12305030(2, region=2302034, obj=2301265, region_1=2300913)
    Event_12305030(3, region=2302035, obj=2301261, region_1=2300913)
    Event_12305040(0, obj__projectile_id=2301256, owner_entity=2300900)
    Event_12305040(1, obj__projectile_id=2301257, owner_entity=2300900)
    Event_12305040(2, obj__projectile_id=2301258, owner_entity=2300900)
    Event_12305040(3, obj__projectile_id=2301259, owner_entity=2300900)
    Event_12305040(4, obj__projectile_id=2301260, owner_entity=2300900)
    Event_12305040(5, obj__projectile_id=2301261, owner_entity=2300900)
    Event_12305040(6, obj__projectile_id=2301262, owner_entity=2300900)
    Event_12305040(7, obj__projectile_id=2301263, owner_entity=2300900)
    Event_12305040(8, obj__projectile_id=2301264, owner_entity=2300900)
    Event_12305040(9, obj__projectile_id=2301265, owner_entity=2300900)
    Event_12305040(10, obj__projectile_id=2301266, owner_entity=2300900)
    Event_12305040(11, obj__projectile_id=2301267, owner_entity=2300900)
    Event_12305040(12, obj__projectile_id=2301268, owner_entity=2300900)
    Event_12305040(13, obj__projectile_id=2301269, owner_entity=2300900)
    Event_12305070()
    Event_12305075(0, character__projectile_id=2300309, animation_id=7008, event_slot=3, ai_param_id=109000)
    Event_12305075(1, character__projectile_id=2300310, animation_id=7002, event_slot=4, ai_param_id=109000)
    Event_12305080()
    Event_12305081()
    Event_12305082()
    Event_12305090(0, frames=0, projectile_id=2300920)
    Event_12305090(1, frames=20, projectile_id=2300921)
    Event_12305100(0, character=2300408, region=2302211, frames=30)
    Event_12305100(1, character=2300409, region=2302213, frames=40)
    Event_12305100(2, character=2300410, region=2302215, frames=60)
    Event_12305110(0, character=2300320, frames=0)
    Event_12305110(1, character=2300321, frames=15)
    Event_12305110(2, character=2300322, frames=35)
    Event_12305110(3, character=2300323, frames=5)
    Event_12305110(4, character=2300324, frames=55)
    Event_12305120()
    Event_12305121(0, character__projectile_id=2300325, animation_id=7005, event_slot=12, ai_param_id=109000)
    Event_12305121(1, character__projectile_id=2300326, animation_id=7005, event_slot=13, ai_param_id=109000)
    Event_12305121(2, character__projectile_id=2300327, animation_id=7002, event_slot=14, ai_param_id=109000)
    Event_12305125()
    Event_12305130()
    Event_12305135(0, character__projectile_id=2300413, animation_id=7002, event_slot=15, ai_param_id=109010)
    Event_12305135(1, character__projectile_id=2300414, animation_id=7008, event_slot=16, ai_param_id=109010)
    Event_12305140(
        0,
        character=2300303,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        1,
        character=2300304,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109900,
        ai_param_id_1=109913
    )
    Event_12305140(
        2,
        character=2300402,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109900,
        ai_param_id_1=109913
    )
    Event_12305140(
        3,
        character=2300309,
        animation_id=7006,
        animation_id_1=7007,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        4,
        character=2300310,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        5,
        character=2300312,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        6,
        character=2300315,
        animation_id=7003,
        animation_id_1=7004,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        7,
        character=2300316,
        animation_id=7006,
        animation_id_1=7007,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        8,
        character=2300317,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        9,
        character=2300403,
        animation_id=7006,
        animation_id_1=7007,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        10,
        character=2300404,
        animation_id=7003,
        animation_id_1=7004,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        11,
        character=2300405,
        animation_id=7006,
        animation_id_1=7007,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        12,
        character=2300325,
        animation_id=7003,
        animation_id_1=7004,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        13,
        character=2300326,
        animation_id=7003,
        animation_id_1=7004,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        14,
        character=2300327,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        15,
        character=2300413,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        16,
        character=2300414,
        animation_id=7006,
        animation_id_1=7007,
        ai_param_id=109900,
        ai_param_id_1=109912
    )
    Event_12305140(
        17,
        character=2300500,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109015,
        ai_param_id_1=109015
    )
    Event_12305140(
        18,
        character=2300501,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109015,
        ai_param_id_1=109015
    )
    Event_12305140(
        19,
        character=2300502,
        animation_id=7000,
        animation_id_1=7001,
        ai_param_id=109015,
        ai_param_id_1=109015
    )
    Event_12305160(0, character__projectile_id=2300303, animation_id=7002, event_slot=0, ai_param_id=109000)
    Event_12305160(1, character__projectile_id=2300304, animation_id=7002, event_slot=1, ai_param_id=109000)
    Event_12305160(2, character__projectile_id=2300402, animation_id=7002, event_slot=2, ai_param_id=109010)
    Event_12305160(3, character__projectile_id=2300309, animation_id=7008, event_slot=3, ai_param_id=109000)
    Event_12305160(4, character__projectile_id=2300310, animation_id=7002, event_slot=4, ai_param_id=109000)
    Event_12305160(5, character__projectile_id=2300312, animation_id=7002, event_slot=5, ai_param_id=109000)
    Event_12305160(6, character__projectile_id=2300315, animation_id=7005, event_slot=6, ai_param_id=109000)
    Event_12305160(7, character__projectile_id=2300316, animation_id=7008, event_slot=7, ai_param_id=109000)
    Event_12305160(8, character__projectile_id=2300317, animation_id=7002, event_slot=8, ai_param_id=109000)
    Event_12305160(9, character__projectile_id=2300403, animation_id=7008, event_slot=9, ai_param_id=109010)
    Event_12305160(10, character__projectile_id=2300404, animation_id=7005, event_slot=10, ai_param_id=109010)
    Event_12305160(11, character__projectile_id=2300405, animation_id=7008, event_slot=11, ai_param_id=109010)
    Event_12305160(12, character__projectile_id=2300325, animation_id=7005, event_slot=12, ai_param_id=109000)
    Event_12305160(13, character__projectile_id=2300326, animation_id=7005, event_slot=13, ai_param_id=109000)
    Event_12305160(14, character__projectile_id=2300327, animation_id=7002, event_slot=14, ai_param_id=109000)
    Event_12305160(15, character__projectile_id=2300413, animation_id=7002, event_slot=15, ai_param_id=109010)
    Event_12305160(16, character__projectile_id=2300414, animation_id=7008, event_slot=16, ai_param_id=109010)
    Event_12305160(17, character__projectile_id=2300500, animation_id=7002, event_slot=17, ai_param_id=109010)
    Event_12305160(18, character__projectile_id=2300501, animation_id=7002, event_slot=18, ai_param_id=109010)
    Event_12305160(19, character__projectile_id=2300502, animation_id=7002, event_slot=19, ai_param_id=109010)
    Event_12305180(0, 2300300, 2302140, 15.0, 0.0)
    Event_12305180(1, 2300301, 2302141, 5.0, 0.0)
    Event_12305180(2, 2300302, 2302141, 5.0, 2.5)
    Event_12305180(3, 2300401, 2302147, 5.0, 0.0)
    Event_12305180(4, 2300201, 2302146, 10.0, 0.0)
    Event_12305180(5, 2300202, 2302146, 10.0, 0.0)
    Event_12305180(6, 2300205, 2302130, 10.0, 0.0)
    Event_12305180(7, 2300330, 2302148, 10.0, 0.0)
    Event_12305180(8, 2300331, 2302148, 10.0, 0.0)
    Event_12305180(9, 2300332, 2302148, 10.0, 0.0)
    Event_12305180(10, 2300333, 2302148, 10.0, 0.0)
    Event_12305180(11, 2300334, 2302148, 10.0, 0.0)
    Event_12305180(13, 2300607, 2302148, 10.0, 0.0)
    Event_12305180(14, 2300608, 2302148, 10.0, 0.0)
    Event_12305180(15, 2300600, 2302149, 3.0, 0.0)
    Event_12305190(0, character=2300200)
    Event_12305190(1, character=2300201)
    Event_12305190(2, character=2300202)
    Event_12305190(3, character=2300203)
    Event_12305190(4, character=2300204)
    Event_12305190(5, character=2300205)
    Event_12305190(6, character=2300206)
    Event_12305190(7, character=2300207)
    Event_12305190(8, character=2300208)
    Event_12305190(9, character=2300209)
    Event_12305190(10, character=2300210)
    Event_12305190(11, character=2300211)
    Event_12305190(12, character=2300212)
    Event_12305190(13, character=2300213)
    Event_12305190(14, character=2300214)
    Event_12305190(15, character=2300215)
    Event_12305190(16, character=2300216)
    Event_12305190(17, character=2300217)
    Event_12305190(18, character=2300218)
    Event_12305190(19, character=2300219)
    Event_12305190(20, character=2300220)
    Event_12305190(21, character=2300221)
    Event_12305190(22, character=2300222)
    Event_12305190(23, character=2300223)
    Event_12305190(24, character=2300224)
    Event_12305190(25, character=2300225)
    Event_12305190(26, character=2300226)
    Event_12305190(27, character=2300227)
    Event_12305190(28, character=2300228)
    Event_12305190(29, character=2300229)
    Event_12305190(30, character=2300230)
    Event_12305190(31, character=2300231)
    Event_12305190(32, character=2300232)
    Event_12305190(33, character=2300233)
    Event_12305190(34, character=2300234)
    Event_12305250()
    Event_12305300(0, 2300602, 2300309, 20.0)
    Event_12305300(1, 2300602, 2300310, 20.0)
    Event_12305300(2, 2300602, 2300311, 20.0)
    Event_12305300(3, 2300602, 2300312, 20.0)
    Event_12305300(4, 2300602, 2300313, 20.0)
    Event_12305300(5, 2300602, 2300314, 20.0)
    Event_12305300(6, 2300602, 2300315, 20.0)
    Event_12305300(7, 2300602, 2300316, 20.0)
    Event_12305300(8, 2300602, 2300317, 20.0)
    Event_12305300(9, 2300602, 2300318, 20.0)
    Event_12305300(10, 2300602, 2300319, 20.0)
    Event_12305300(11, 2300602, 2300320, 20.0)
    Event_12305300(12, 2300602, 2300321, 20.0)
    Event_12305300(13, 2300602, 2300322, 20.0)
    Event_12305300(14, 2300602, 2300323, 20.0)
    Event_12305300(15, 2300602, 2300324, 20.0)
    Event_12305300(16, 2300602, 2300403, 20.0)
    Event_12305300(17, 2300602, 2300404, 20.0)
    Event_12305300(18, 2300602, 2300405, 20.0)
    Event_12305300(19, 2300602, 2300406, 20.0)
    Event_12305300(20, 2300602, 2300407, 20.0)
    Event_12305300(21, 2300602, 2300408, 20.0)
    Event_12305300(22, 2300602, 2300409, 20.0)
    Event_12305300(23, 2300602, 2300410, 20.0)
    Event_12305300(24, 2300603, 2300309, 35.0)
    Event_12305300(25, 2300603, 2300310, 35.0)
    Event_12305300(26, 2300603, 2300311, 35.0)
    Event_12305300(27, 2300603, 2300312, 35.0)
    Event_12305300(28, 2300603, 2300313, 35.0)
    Event_12305300(29, 2300603, 2300314, 35.0)
    Event_12305300(30, 2300603, 2300315, 35.0)
    Event_12305300(31, 2300603, 2300316, 35.0)
    Event_12305300(32, 2300603, 2300317, 35.0)
    Event_12305300(33, 2300603, 2300318, 35.0)
    Event_12305300(34, 2300603, 2300319, 35.0)
    Event_12305300(35, 2300603, 2300320, 35.0)
    Event_12305300(36, 2300603, 2300321, 35.0)
    Event_12305300(37, 2300603, 2300322, 35.0)
    Event_12305300(38, 2300603, 2300323, 35.0)
    Event_12305300(39, 2300603, 2300324, 35.0)
    Event_12305300(40, 2300603, 2300403, 35.0)
    Event_12305300(41, 2300603, 2300404, 35.0)
    Event_12305300(42, 2300603, 2300405, 35.0)
    Event_12305300(43, 2300603, 2300406, 35.0)
    Event_12305300(44, 2300603, 2300407, 35.0)
    Event_12305300(45, 2300603, 2300408, 35.0)
    Event_12305300(46, 2300603, 2300409, 35.0)
    Event_12305300(47, 2300603, 2300410, 35.0)
    Event_12305300(48, 2300604, 2300318, 35.0)
    Event_12305300(49, 2300604, 2300319, 35.0)
    Event_12305300(50, 2300604, 2300320, 35.0)
    Event_12305300(51, 2300604, 2300321, 35.0)
    Event_12305300(52, 2300604, 2300322, 35.0)
    Event_12305300(53, 2300604, 2300323, 35.0)
    Event_12305300(54, 2300604, 2300324, 35.0)
    Event_12305300(55, 2300604, 2300406, 35.0)
    Event_12305300(56, 2300604, 2300407, 35.0)
    Event_12305300(57, 2300604, 2300408, 35.0)
    Event_12305300(58, 2300604, 2300409, 35.0)
    Event_12305300(59, 2300604, 2300410, 35.0)
    Event_12305300(60, 2300605, 2300318, 35.0)
    Event_12305300(61, 2300605, 2300319, 35.0)
    Event_12305300(62, 2300605, 2300320, 35.0)
    Event_12305300(63, 2300605, 2300321, 35.0)
    Event_12305300(64, 2300605, 2300322, 35.0)
    Event_12305300(65, 2300605, 2300323, 35.0)
    Event_12305300(66, 2300605, 2300324, 35.0)
    Event_12305300(67, 2300605, 2300406, 35.0)
    Event_12305300(68, 2300605, 2300407, 35.0)
    Event_12305300(69, 2300605, 2300408, 35.0)
    Event_12305300(70, 2300605, 2300409, 35.0)
    Event_12305300(71, 2300605, 2300410, 35.0)
    Event_12305300(72, 2300606, 2300325, 25.0)
    Event_12305300(73, 2300606, 2300326, 25.0)
    Event_12305300(74, 2300606, 2300327, 25.0)
    Event_12305300(75, 2300606, 2300201, 25.0)
    Event_12305300(76, 2300606, 2300202, 25.0)
    Event_12305300(77, 2300606, 2300203, 25.0)
    Event_12305300(78, 2300606, 2300204, 25.0)
    Event_12305300(79, 2300606, 2300205, 25.0)
    Event_12305440(0, character=2300309, special_effect_id=5522)
    Event_12305440(1, character=2300310, special_effect_id=5522)
    Event_12305440(2, character=2300311, special_effect_id=5522)
    Event_12305440(3, character=2300312, special_effect_id=5522)
    Event_12305440(4, character=2300313, special_effect_id=5522)
    Event_12305440(5, character=2300314, special_effect_id=5522)
    Event_12305440(6, character=2300315, special_effect_id=5522)
    Event_12305440(7, character=2300316, special_effect_id=5522)
    Event_12305440(8, character=2300317, special_effect_id=5522)
    Event_12305440(9, character=2300318, special_effect_id=5522)
    Event_12305440(10, character=2300319, special_effect_id=5522)
    Event_12305440(11, character=2300320, special_effect_id=5522)
    Event_12305440(12, character=2300321, special_effect_id=5522)
    Event_12305440(13, character=2300322, special_effect_id=5522)
    Event_12305440(14, character=2300323, special_effect_id=5522)
    Event_12305440(15, character=2300324, special_effect_id=5522)
    Event_12305440(16, character=2300325, special_effect_id=5522)
    Event_12305440(17, character=2300326, special_effect_id=5522)
    Event_12305440(18, character=2300327, special_effect_id=5522)
    Event_12305440(19, character=2300403, special_effect_id=5524)
    Event_12305440(20, character=2300404, special_effect_id=5524)
    Event_12305440(21, character=2300405, special_effect_id=5524)
    Event_12305440(22, character=2300406, special_effect_id=5524)
    Event_12305440(23, character=2300407, special_effect_id=5524)
    Event_12305440(24, character=2300408, special_effect_id=5524)
    Event_12305440(25, character=2300409, special_effect_id=5524)
    Event_12305440(26, character=2300410, special_effect_id=5524)
    Event_12305440(27, character=2300201, special_effect_id=5523)
    Event_12305440(28, character=2300202, special_effect_id=5523)
    Event_12305440(29, character=2300203, special_effect_id=5523)
    Event_12305440(30, character=2300204, special_effect_id=5523)
    Event_12305440(31, character=2300205, special_effect_id=5523)
    Event_12305480()
    Event_12305481()
    Event_12305482()
    Event_12305490(0, attacked_entity=2300320, animation_id=7010)
    Event_12305490(1, attacked_entity=2300321, animation_id=7010)
    Event_12305490(2, attacked_entity=2300322, animation_id=7010)
    Event_12305490(3, attacked_entity=2300323, animation_id=7010)
    Event_12305490(4, attacked_entity=2300324, animation_id=7010)
    Event_12305490(5, attacked_entity=2300408, animation_id=7010)
    Event_12305490(6, attacked_entity=2300409, animation_id=7010)
    Event_12305490(7, attacked_entity=2300410, animation_id=7010)
    Event_12305501()
    Event_12305502(0, region=2302200, event_slot=1)
    Event_12305502(1, region=2302060, event_slot=0)
    Event_12305510(0, character=2300320, region=2302220, region_1=2302210, ai_param_id=109008, ai_param_id_1=109006)
    Event_12305510(1, character=2300321, region=2302222, region_1=2302212, ai_param_id=109008, ai_param_id_1=109006)
    Event_12305510(2, character=2300322, region=2302224, region_1=2302214, ai_param_id=109008, ai_param_id_1=109006)
    Event_12305510(3, character=2300323, region=2302227, region_1=2302217, ai_param_id=109008, ai_param_id_1=109006)
    Event_12305510(4, character=2300324, region=2302226, region_1=2302216, ai_param_id=109008, ai_param_id_1=109006)
    Event_12305510(5, character=2300408, region=2302223, region_1=2302213, ai_param_id=109014, ai_param_id_1=109011)
    Event_12305510(6, character=2300409, region=2302221, region_1=2302211, ai_param_id=109014, ai_param_id_1=109011)
    Event_12305510(7, character=2300410, region=2302225, region_1=2302215, ai_param_id=109014, ai_param_id_1=109011)
    Event_12304020()
    Event_12304021()
    Event_12304022()
    Event_12300700()
    Event_12300701()
    Event_12300702()
    Event_12300703()
    Event_12300704()
    Event_12300705()
    Event_12305701()
    Event_12300707()
    Event_12300708()
    Event_12300710(0, attacked_entity=2300300)
    Event_12300710(1, attacked_entity=2300301)
    Event_12300710(2, attacked_entity=2300302)
    Event_12300710(3, attacked_entity=2300303)
    Event_12300710(4, attacked_entity=2300304)
    Event_12300710(5, attacked_entity=2300305)
    Event_12300710(6, attacked_entity=2300306)
    Event_12300710(7, attacked_entity=2300307)
    Event_12300710(8, attacked_entity=2300308)
    Event_12300710(9, attacked_entity=2300309)
    Event_12300710(10, attacked_entity=2300310)
    Event_12300710(11, attacked_entity=2300311)
    Event_12300710(12, attacked_entity=2300312)
    Event_12300710(13, attacked_entity=2300313)
    Event_12300710(14, attacked_entity=2300314)
    Event_12300710(15, attacked_entity=2300315)
    Event_12300710(16, attacked_entity=2300316)
    Event_12300710(17, attacked_entity=2300317)
    Event_12300710(18, attacked_entity=2300318)
    Event_12300710(19, attacked_entity=2300319)
    Event_12300710(20, attacked_entity=2300320)
    Event_12300710(21, attacked_entity=2300321)
    Event_12300710(22, attacked_entity=2300322)
    Event_12300710(23, attacked_entity=2300323)
    Event_12300710(24, attacked_entity=2300324)
    Event_12300710(25, attacked_entity=2300400)
    Event_12300710(26, attacked_entity=2300401)
    Event_12300710(27, attacked_entity=2300402)
    Event_12300710(28, attacked_entity=2300403)
    Event_12300710(29, attacked_entity=2300404)
    Event_12300710(30, attacked_entity=2300405)
    Event_12300710(31, attacked_entity=2300600)
    Event_12300710(32, attacked_entity=2300601)
    Event_12300710(33, attacked_entity=2300720)
    Event_12300750()
    Event_12300752()
    Event_12300753()
    Event_12300990()


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    DisableAnimations(2303950)
    DisableGravity(2303950)
    DisableCharacterCollision(2303950)
    DisableAnimations(2303951)
    DisableGravity(2303951)
    DisableCharacterCollision(2303951)


@NeverRestart(12301800)
def Event_12301800():
    """Event 12301800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2303802)
    DisableSoundEvent(sound_id=2303803)
    DisableCharacter(2300800)
    Kill(2300800)
    DisableObject(2301800)
    DeleteVFX(2303800, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2300800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2301800)
    DeleteVFX(2303800)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2300800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
    EnableFlag(72400512)
    AwardAchievement(achievement_id=22)
    AwardItemLot(80000000, host_only=False)
    EnableFlag(2300)
    EnableFlag(9453)
    StopPlayLogMeasurement(measurement_id=2300000)
    StopPlayLogMeasurement(measurement_id=2300001)
    StopPlayLogMeasurement(measurement_id=2300010)
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


@NeverRestart(12301801)
def Event_12301801():
    """Event 12301801"""
    DisableNetworkSync()
    EndIfFlagEnabled(12301800)
    IfFlagEnabled(1, 12301800)
    IfCharacterBackreadDisabled(2, 2300800)
    IfHealthLessThanOrEqual(2, 2300800, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2302800, 0, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12301802)
def Event_12301802():
    """Event 12301802"""
    EndIfFlagEnabled(12301800)
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(1, 12301800)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2302805)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2300800, 7001)
    EnableFlag(12304800)
    EndIfFlagEnabled(9339)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9339)


@NeverRestart(12301803)
def Event_12301803():
    """Event 12301803"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12304800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(12304800)
    EnableFlag(12301802)


@NeverRestart(12304810)
def Event_12304810():
    """Event 12304810"""
    EndIfFlagEnabled(12301800)
    GotoIfFlagEnabled(Label.L0, flag=12301802)
    SkipLinesIfClient(2)
    DisableObject(2301800)
    DeleteVFX(2303800, erase_root_only=False)
    IfFlagDisabled(1, 12301800)
    IfFlagEnabled(1, 12301802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2301800)
    CreateVFX(2303800)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=2300800, entity=2301800)
    IfFlagDisabled(2, 12301800)
    IfFlagEnabled(3, 12301800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2302800, animation=101130)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2302801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12304800)
    Restart()


@NeverRestart(12304811)
def Event_12304811():
    """Event 12304811"""
    DisableNetworkSync()
    EndIfFlagEnabled(12301800)
    IfFlagDisabled(1, 12301800)
    IfFlagEnabled(1, 12301802)
    IfFlagEnabled(1, 12304800)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParam(1, action_button_id=2300800, entity=2301800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2302800, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2302801)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12304801)
    Restart()


@NeverRestart(12304812)
def Event_12304812():
    """Event 12304812"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2301800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12304813)
def Event_12304813():
    """Event 12304813"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=2301800, radius=4.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2301800, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12304802)
def Event_12304802():
    """Event 12304802"""
    EndIfFlagEnabled(12301800)
    DisableAI(2300800)
    DisableHealthBar(2300800)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12304800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2300800, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12304800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2300800, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2300800)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2300800, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2300800)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2300800)
    EnableBossHealthBar(2300800, name=209000)
    CreatePlayLog(name=86)
    StartPlayLogMeasurement(measurement_id=2300010, name=102, overwrite=True)


@NeverRestart(12304803)
def Event_12304803():
    """Event 12304803"""
    DisableNetworkSync()
    EndIfFlagEnabled(12301800)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2303802)
    DisableSoundEvent(sound_id=2303803)
    IfFlagDisabled(1, 12301800)
    IfFlagEnabled(1, 12304802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12304801)
    IfCharacterInsideRegion(1, PLAYER, region=2302801)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=2303802)
    IfFlagEnabled(2, 12304808)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12301800)
    IfFlagEnabled(2, 12304802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12304801)
    IfCharacterInsideRegion(2, PLAYER, region=2302801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2303802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2303803)


@NeverRestart(12304804)
def Event_12304804():
    """Event 12304804"""
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12304800)
    IfCharacterWhitePhantom(2, PLAYER)
    IfFlagEnabled(2, 12304801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=1)


@NeverRestart(12304805)
def Event_12304805():
    """Event 12304805"""
    DisableNetworkSync()
    EndIfFlagEnabled(12301800)
    IfFlagEnabled(0, 12301800)
    DisableBossMusic(sound_id=2303802)
    DisableBossMusic(sound_id=2303803)
    DisableBossMusic(sound_id=-1)


@NeverRestart(12304807)
def Event_12304807():
    """Event 12304807"""
    EndIfFlagEnabled(12301800)
    EndIfThisEventFlagEnabled()
    IfHealthLessThan(0, 2300800, value=0.6700000166893005)
    Wait(0.10000000149011612)
    ResetAnimation(2300800, disable_interpolation=True)
    ForceAnimation(2300800, 7010)
    AICommand(2300800, command_id=100, command_slot=0)
    ReplanAI(2300800)
    IfCharacterHasTAEEvent(0, 2300800, tae_event_id=10)
    AICommand(2300800, command_id=-1, command_slot=0)
    ReplanAI(2300800)


@NeverRestart(12304808)
def Event_12304808():
    """Event 12304808"""
    EndIfFlagEnabled(12301800)
    EndIfThisEventFlagEnabled()
    IfHealthLessThan(1, 2300800, value=0.33000001311302185)
    IfFlagEnabled(1, 12304807)
    IfConditionTrue(0, input_condition=1)
    Wait(0.10000000149011612)
    ResetAnimation(2300800, disable_interpolation=True)
    ForceAnimation(2300800, 7011)
    AICommand(2300800, command_id=101, command_slot=0)
    ReplanAI(2300800)
    IfCharacterHasTAEEvent(0, 2300800, tae_event_id=20)
    AICommand(2300800, command_id=-1, command_slot=0)
    ReplanAI(2300800)


@NeverRestart(12301700)
def Event_12301700():
    """Event 12301700"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2303812)
    DisableSoundEvent(sound_id=2303813)
    DisableCharacter(2300810)
    Kill(2300810)
    DisableObject(2301810)
    DisableObject(2301811)
    DeleteVFX(2303810, erase_root_only=False)
    DeleteVFX(2303811, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2300810)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2301810)
    DisableObject(2301811)
    DeleteVFX(2303810)
    DeleteVFX(2303811)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2300810)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(achievement_id=24)
    SkipLinesIfFlagEnabled(2, 6644)
    AwardItemLot(50800000, host_only=False)
    SkipLines(1)
    AwardItemLot(50800005, host_only=False)
    EnableFlag(2301)
    EnableFlag(9454)
    StopPlayLogMeasurement(measurement_id=2300000)
    StopPlayLogMeasurement(measurement_id=2300001)
    StopPlayLogMeasurement(measurement_id=2300010)
    CreatePlayLog(name=40)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=120,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=120,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=120,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=120,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterWhitePhantom(0, PLAYER)
    Wait(0.0)


@NeverRestart(12301701)
def Event_12301701():
    """Event 12301701"""
    DisableNetworkSync()
    EndIfFlagEnabled(12301700)
    IfFlagEnabled(1, 12301700)
    IfCharacterBackreadDisabled(2, 2300810)
    IfHealthLessThanOrEqual(2, 2300810, value=0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=1)
    PlaySoundEffect(2302810, 0, sound_type=SoundType.c_CharacterMotion)


@NeverRestart(12301702)
def Event_12301702():
    """Event 12301702"""
    EndIfThisEventFlagEnabled()
    EndIfThisEventFlagEnabled()
    EnableInvincibility(2300810)
    ForceAnimation(2300810, 7000, loop=True)
    IfFlagDisabled(1, 12301700)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=2300810, other_entity=PLAYER, radius=16.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2300810, 7001)
    WaitFrames(frames=70)
    DisableInvincibility(2300810)
    EnableFlag(12304700)
    EndIfFlagEnabled(9340)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9340)


@NeverRestart(12301703)
def Event_12301703():
    """Event 12301703"""
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12304700)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    DisableInvincibility(2300810)
    EnableFlag(12304700)
    EnableFlag(12301702)


@NeverRestart(12304730)
def Event_12304730():
    """Event 12304730"""
    EndIfFlagEnabled(12301700)
    GotoIfFlagEnabled(Label.L0, flag=12301702)
    SkipLinesIfClient(2)
    DisableObject(2301810)
    DeleteVFX(2303810, erase_root_only=False)
    DisableObject(2301811)
    DeleteVFX(2303811, erase_root_only=False)
    IfFlagDisabled(1, 12301700)
    IfFlagEnabled(1, 12301702)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2301810)
    EnableObject(2301811)
    CreateVFX(2303810)
    CreateVFX(2303811)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParam(2, action_button_id=2300800, entity=2301810)
    IfFlagDisabled(2, 12301700)
    IfFlagEnabled(3, 12301700)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    RotateToFaceEntity(PLAYER, 2302810, animation=101130, wait_for_completion=True)
    SkipLinesIfThisEventFlagEnabled(1)
    RotateToFaceEntity(2300810, PLAYER, animation=3008)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2302811)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, seconds=2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=5)
    EnableFlag(12304700)
    Restart()


@NeverRestart(12304731)
def Event_12304731():
    """Event 12304731"""
    DisableNetworkSync()
    EndIfFlagEnabled(12301700)
    IfFlagDisabled(1, 12301700)
    IfFlagEnabled(1, 12301702)
    IfFlagEnabled(1, 12304700)
    IfCharacterWhitePhantom(1, PLAYER)
    IfActionButtonParam(1, action_button_id=2300800, entity=2301810)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2302810, animation=101130)
    IfCharacterWhitePhantom(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=2302811)
    IfCharacterWhitePhantom(3, PLAYER)
    IfTimeElapsed(3, seconds=2.0)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, condition=3)
    EnableFlag(12304701)
    Restart()


@NeverRestart(12304732)
def Event_12304732():
    """Event 12304732"""
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2301810, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12304733)
def Event_12304733():
    """Event 12304733"""
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, entity=PLAYER, other_entity=2301810, radius=4.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2301810, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@NeverRestart(12304702)
def Event_12304702():
    """Event 12304702"""
    EndIfFlagEnabled(12301700)
    DisableAI(2300810)
    DisableHealthBar(2300810)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12304700)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2300810, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12304700)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2300810, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2300810)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2300810, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2300810)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2300810)
    EnableBossHealthBar(2300810, name=508000)
    CreatePlayLog(name=86)
    StartPlayLogMeasurement(measurement_id=2300010, name=102, overwrite=True)


@NeverRestart(12304703)
def Event_12304703():
    """Event 12304703"""
    DisableNetworkSync()
    EndIfFlagEnabled(12301700)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2303812)
    DisableSoundEvent(sound_id=2303813)
    IfFlagDisabled(1, 12301700)
    IfFlagEnabled(1, 12304702)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12304701)
    IfCharacterInsideRegion(1, PLAYER, region=2302812)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(sound_id=2303812)
    IfCharacterHasTAEEvent(2, 2300810, tae_event_id=20)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, 12301700)
    IfFlagEnabled(2, 12304702)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12304701)
    IfCharacterInsideRegion(2, PLAYER, region=2302812)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(sound_id=2303812)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2303813)


@NeverRestart(12304704)
def Event_12304704():
    """Event 12304704"""
    DisableNetworkSync()
    EndIfFlagEnabled(12301700)
    IfHealthGreaterThan(1, 2300810, value=0.0)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=2300810, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=1)
    IfHealthGreaterThan(2, 2300810, value=0.0)
    IfEntityBeyondDistance(2, entity=PLAYER, other_entity=2300810, radius=12.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=0)
    Restart()


@NeverRestart(12304705)
def Event_12304705():
    """Event 12304705"""
    DisableNetworkSync()
    EndIfFlagEnabled(12301700)
    IfFlagEnabled(0, 12301700)
    DisableBossMusic(sound_id=2303812)
    DisableBossMusic(sound_id=2303813)
    DisableBossMusic(sound_id=-1)


@RestartOnRest(12304707)
def Event_12304707():
    """Event 12304707"""
    EndIfFlagEnabled(12301700)
    AICommand(2300810, command_id=2, command_slot=1)
    IfHealthLessThan(1, 2300810, value=0.6700000166893005)
    IfCharacterHasSpecialEffect(1, 2300810, 5402)
    IfConditionTrue(0, input_condition=1)
    Wait(0.10000000149011612)
    AICommand(2300810, command_id=100, command_slot=2)
    ReplanAI(2300810)
    IfCharacterHasTAEEvent(0, 2300810, tae_event_id=20)
    AICommand(2300810, command_id=-1, command_slot=2)
    ReplanAI(2300810)
    Wait(0.10000000149011612)
    AICommand(2300810, command_id=3, command_slot=1)


@RestartOnRest(12304715)
def Event_12304715(
    _,
    npc_part_id: short,
    npc_part_id_1: int,
    part_index: short,
    special_effect_id: int,
    special_effect_id_1: int,
    animation_id: int,
    part_health: int,
):
    """Event 12304715"""
    EndIfFlagEnabled(12301700)
    CreateNPCPart(2300810, npc_part_id=npc_part_id, part_index=part_index, part_health=part_health)
    SetNPCPartEffects(2300810, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, 2300810, npc_part_id=npc_part_id_1, value=0)
    IfHealthLessThanOrEqual(3, 2300810, value=0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=3)
    ChangeCharacterCloth(2300810, bit_count=10, state_id=2)
    CreateNPCPart(
        2300810,
        npc_part_id=npc_part_id,
        part_index=part_index,
        part_health=9999999,
        body_damage_correction=1.5,
    )
    SetNPCPartEffects(2300810, npc_part_id=npc_part_id_1, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(frames=1)
    ResetAnimation(2300810)
    ForceAnimation(2300810, animation_id)
    AddSpecialEffect(2300810, special_effect_id, affect_npc_part_hp=True)
    CancelSpecialEffect(2300810, special_effect_id_1)
    ReplanAI(2300810)
    Wait(10.0)
    AICommand(2300810, command_id=110, command_slot=0)
    ReplanAI(2300810)
    IfCharacterHasTAEEvent(0, 2300810, tae_event_id=300)
    SetNPCPartHealth(2300810, npc_part_id=npc_part_id_1, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(2300810, special_effect_id_1, affect_npc_part_hp=True)
    CancelSpecialEffect(2300810, special_effect_id)
    AICommand(2300810, command_id=-1, command_slot=0)
    ReplanAI(2300810)
    ChangeCharacterCloth(2300810, bit_count=10, state_id=1)
    WaitFrames(frames=10)
    Restart()


@RestartOnRest(12304450)
def Event_12304450(_, character: int, region: int, flag: int, flag_1: int, flag_2: int):
    """Event 12304450"""
    EndIfThisEventSlotFlagEnabled()
    EndIfClient()
    SetEventPoint(character, region=region, reaction_range=1.0)
    IfFlagEnabled(1, flag)
    IfFlagDisabled(1, flag_1)
    IfFlagEnabled(1, flag_2)
    IfConditionTrue(0, input_condition=1)
    AICommand(character, command_id=990, command_slot=0)
    ReplanAI(character)


@RestartOnRest(12304400)
def Event_12304400(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12304400"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfFlagEnabled(1, 72400461)
    IfFlagRangeAnyEnabled(1, flag_range=(1340, 1341))
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
    IfFlagEnabled(2, 72400461)
    IfFlagRangeAnyEnabled(2, flag_range=(1340, 1341))
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12304401)
def Event_12304401(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12304401"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
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
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12304402)
def Event_12304402(_, flag: int, vfx_id: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 12304402"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    IfPlayerHasGood(1, 4312)
    IfFlagDisabled(1, flag_1)
    IfFlagDisabled(1, flag_2)
    IfFlagDisabled(1, flag_3)
    IfClientTypeCountComparison(1, client_type=ClientType.Coop, comparison_type=ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(1, 13501900)
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
    IfFlagEnabled(2, 13501900)
    IfFlagDisabled(-3, flag_4)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(flag)
    DeleteVFX(vfx_id)
    Restart()


@RestartOnRest(12304410)
def Event_12304410(
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
    """Event 12304410"""
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


@RestartOnRest(12304460)
def Event_12304460(
    _,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    animation: int,
    flag: int,
    region_3: int,
):
    """Event 12304460"""
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


@RestartOnRest(12304500)
def Event_12304500():
    """Event 12304500"""
    GotoIfThisEventFlagDisabled(Label.L0)
    SetBackreadStateAlternate(2300740, True)
    AddSpecialEffect(2300740, 9006)
    EnableCharacter(2300740)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2300740)
    DisableAI(2300740)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    SetNetworkUpdateAuthority(2300740, authority_level=UpdateAuthority.Forced)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12304508)
    IfCharacterInsideRegion(1, PLAYER, region=2302721)
    IfFlagDisabled(1, 12301800)
    IfFlagEnabled(1, 72400461)
    IfFlagRangeAnyEnabled(1, flag_range=(1340, 1341))
    IfConditionTrue(0, input_condition=1)
    Wait(5.0)
    EnableFlag(12304509)
    PlaySoundEffect(PLAYER, 100000009, sound_type=SoundType.f_MenuEffect)
    Wait(5.0)
    PlaySoundEffect(PLAYER, 100000020, sound_type=SoundType.f_MenuEffect)
    SetBackreadStateAlternate(2300740, True)
    AddSpecialEffect(2300740, 9006)
    EnableCharacter(2300740)
    ForceAnimation(2300740, 101201, wait_for_completion=True)
    EnableAI(2300740)


@RestartOnRest(12304501)
def Event_12304501():
    """Event 12304501"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(12301800)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 12304502)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2300740)
    SetBackreadStateAlternate(2300740, False)


@RestartOnRest(12304502)
def Event_12304502():
    """Event 12304502"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(12301800)
    EndIfFlagEnabled(12304501)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 12304500)
    IfFlagDisabled(1, 12304501)
    IfFlagEnabled(1, 12301800)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2300740, command_id=991, command_slot=0)
    ReplanAI(2300740)
    Wait(1.0)
    AddSpecialEffect(2300740, 5560)
    CreateTemporaryVFX(vfx_id=121, anchor_entity=2300740, model_point=236, anchor_type=CoordEntityType.Character)
    Wait(2.0)
    DisableCharacter(2300740)


@RestartOnRest(12304504)
def Event_12304504():
    """Event 12304504"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(12301800)
    EndIfFlagEnabled(12304501)
    EndIfFlagEnabled(12304505)
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(1, 12301800)
    IfFlagEnabled(1, 12304500)
    IfFlagDisabled(1, 12304501)
    IfFlagEnabled(1, 12301802)
    IfFlagEnabled(1, 12304800)
    IfCharacterOutsideRegion(1, 2300740, region=2302801)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetEventPoint(2300740, region=2302722, reaction_range=1.0)
    AICommand(2300740, command_id=990, command_slot=0)
    ReplanAI(2300740)


@RestartOnRest(12304505)
def Event_12304505():
    """Event 12304505"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(12301800)
    EndIfFlagEnabled(12304501)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 12304504)
    IfCharacterInsideRegion(1, 2300740, region=2302722)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(2300740)
    RotateToFaceEntity(2300740, 2302800, animation=101130, wait_for_completion=True)
    AICommand(2300740, command_id=-1, command_slot=0)
    ReplanAI(2300740)


@RestartOnRest(12304506)
def Event_12304506():
    """Event 12304506"""
    DisableSoapstoneMessage(2303300)
    DeleteVFX(2303400, erase_root_only=False)
    EndIfThisEventFlagEnabled()
    IfPlayerHasGood(1, 200)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 12301800)
    IfFlagEnabled(1, 72400461)
    IfFlagRangeAnyEnabled(1, flag_range=(1340, 1341))
    IfConditionTrue(0, input_condition=1)
    EnableSoapstoneMessage(2303300)
    CreateVFX(2303400)
    IfFlagEnabled(-1, 12304509)
    IfFlagEnabled(-1, 12301800)
    IfConditionTrue(0, input_condition=-1)
    DisableSoapstoneMessage(2303300)
    DeleteVFX(2303400)


@RestartOnRest(12304507)
def Event_12304507():
    """Event 12304507"""
    IfCharacterHuman(1, PLAYER)
    IfCharacterHasSpecialEffect(1, PLAYER, 9000)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12304508)
    WaitFrames(frames=1)
    DisableFlag(12304508)
    IfCharacterHuman(2, PLAYER)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 9000)
    IfConditionTrue(0, input_condition=2)
    Restart()


@RestartOnRest(12300100)
def Event_12300100():
    """Event 12300100"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    Move(2300204, destination=2302300, destination_type=CoordEntityType.Region, set_draw_parent=2306000)
    PostDestruction(2301000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(2300204)
    DisableAI(2300204)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302000)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=2300204, radius=7.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=2300204)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(2300204, 7015)
    EnableGravity(2300204)
    EnableAI(2300204)
    SetNest(2300204, region=2302300)
    ReplanAI(2300204)


@NeverRestart(12300110)
def Event_12300110(_, action_button_id: int, anchor_entity: int, flag: int):
    """Event 12300110"""
    DisableNetworkSync()
    EndIfFlagEnabled(flag)
    IfActionButtonParam(1, action_button_id=action_button_id, entity=anchor_entity)
    IfFlagEnabled(2, flag)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(text=10010161, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(0.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)
    Restart()


@NeverRestart(12300120)
def Event_12300120(_, obj: int, obj_act_id: int, animation_id: int, obj_act_id_1: int):
    """Event 12300120"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=animation_id)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    Wait(0.0)


@NeverRestart(12300130)
def Event_12300130():
    """Event 12300130"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    CreateObjectVFX(2301500, vfx_id=200, model_point=900201)
    IfActionButtonParam(0, action_button_id=2300000, entity=2301500)
    AwardItemLot(2300170, host_only=False)
    DeleteObjectVFX(2301500)


@RestartOnRest(12300140)
def Event_12300140():
    """Event 12300140"""
    DeleteVFX(2303002)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterInsideRegion(0, PLAYER, region=2303000)
    DeleteVFX(2303010)
    CreateVFX(2303002)
    Wait(4.0)
    CreateVFX(2303010)


@RestartOnRest(12300160)
def Event_12300160():
    """Event 12300160"""
    GotoIfFlagEnabled(Label.L0, flag=12300240)
    IfHasAIStatus(-1, 2300605, ai_status=AIStatusType.Battle)
    IfFlagEnabled(-1, 12300240)
    IfFlagEnabled(-1, 12305392)
    IfFlagEnabled(-1, 12305393)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    DisableSoundEvent(sound_id=2304020)


@NeverRestart(12300180)
def Event_12300180():
    """Event 12300180"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(obj=2301020, animation_id=1)
    DisableObjectActivation(2301020, obj_act_id=2300011)
    NotifyDoorEventSoundDampening(obj=2301020, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(2301020, obj_act_id=2300011)
    IfFlagEnabled(0, 12300190)
    EnableObjectActivation(2301020, obj_act_id=2300011)
    IfObjectActivated(0, obj_act_id=12300214)
    Wait(0.0)


@NeverRestart(12300190)
def Event_12300190():
    """Event 12300190"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfActionButtonParam(1, action_button_id=2300020, entity=2301020)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    EndIfConditionFalse(2)
    DisplayDialog(text=10010165, anchor_entity=2301020, number_buttons=NumberButtons.OneButton)


@RestartOnRest(12300201)
def Event_12300201():
    """Event 12300201"""
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 12301800)
    EnableFlag(12300200)


@RestartOnRest(12300210)
def Event_12300210():
    """Event 12300210"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DropMandatoryTreasure(2300720)
    DisableBackread(2300720)
    DisableCharacter(2300720)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2300720)
    DisableBackread(2300720)


@RestartOnRest(12300220)
def Event_12300220(_, character: int, flag: int):
    """Event 12300220"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(character)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, flag)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@RestartOnRest(12300230)
def Event_12300230():
    """Event 12300230"""
    IfCharacterInsideRegion(-1, 2300720, region=2302180)
    IfCharacterInsideRegion(-1, 2300720, region=2302181)
    IfCharacterInsideRegion(-1, 2300720, region=2302182)
    IfConditionTrue(0, input_condition=-1)
    AICommand(2300720, command_id=100, command_slot=0)
    IfCharacterOutsideRegion(1, 2300720, region=2302180)
    IfCharacterOutsideRegion(1, 2300720, region=2302181)
    IfCharacterOutsideRegion(1, 2300720, region=2302182)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300720, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(12300235)
def Event_12300235():
    """Event 12300235"""
    IfCharacterOutsideRegion(0, 2300720, region=2302190)
    AICommand(2300720, command_id=110, command_slot=0)
    IfCharacterInsideRegion(0, 2300720, region=2302190)
    AICommand(2300720, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(12300240)
def Event_12300240():
    """Event 12300240"""
    GotoIfThisEventFlagDisabled(Label.L0)
    EnableNavmeshType(navmesh_id=2303070, navmesh_type=NavmeshType.Solid)
    EndOfAnimation(obj=2301322, animation_id=1)
    CreateObjectVFX(2301323, vfx_id=750, model_point=923240)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectDestroyed(0, 2301320)
    EnableNavmeshType(navmesh_id=2303070, navmesh_type=NavmeshType.Solid)
    ForceAnimation(2301322, 1, wait_for_completion=True)
    DisableObject(2301322)
    CreateObjectVFX(2301323, vfx_id=750, model_point=923240)


@RestartOnRest(12300250)
def Event_12300250():
    """Event 12300250"""
    IfFlagEnabled(0, 12300240)
    CreateHazard(
        obj_flag=12300251,
        obj=2301450,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=4.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300252,
        obj=2301451,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300253,
        obj=2301452,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300254,
        obj=2301453,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300255,
        obj=2301454,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300256,
        obj=2301455,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300257,
        obj=2301456,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300258,
        obj=2301457,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        obj_flag=12300259,
        obj=2301458,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
    )


@NeverRestart(12300300)
def Event_12300300():
    """Event 12300300"""
    GotoIfFlagEnabled(Label.L0, flag=9802)
    GotoIfFlagEnabled(Label.L0, flag=9801)
    EnableMapPiece(map_piece_id=2306010)
    DisableMapPiece(map_piece_id=2306011)
    DisableMapPiece(map_piece_id=2304000)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableMapPiece(map_piece_id=2306010)
    EnableMapPiece(map_piece_id=2306011)
    EnableMapPiece(map_piece_id=2304000)
    DeleteVFX(2303600, erase_root_only=False)
    DeleteVFX(2303601, erase_root_only=False)
    DeleteVFX(2303602, erase_root_only=False)
    DeleteVFX(2303603, erase_root_only=False)
    DeleteVFX(2303604, erase_root_only=False)
    DeleteVFX(2303605, erase_root_only=False)
    DeleteVFX(2303606, erase_root_only=False)
    DeleteVFX(2303607, erase_root_only=False)
    DeleteVFX(2303608, erase_root_only=False)
    DeleteVFX(2303609, erase_root_only=False)
    DeleteVFX(2303610, erase_root_only=False)
    DeleteVFX(2303611, erase_root_only=False)
    DeleteVFX(2303612, erase_root_only=False)
    DeleteVFX(2303613, erase_root_only=False)
    DeleteVFX(2303614, erase_root_only=False)
    Goto(Label.L1)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagState(-1, FlagState.Change, FlagType.Absolute, 9800)
    IfFlagState(-1, FlagState.Change, FlagType.Absolute, 9801)
    IfFlagState(-1, FlagState.Change, FlagType.Absolute, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@NeverRestart(12300310)
def Event_12300310(_, obj: int, obj_act_id: int, obj_act_id_1: int):
    """Event 12300310"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    DisableObjectActivation(obj, obj_act_id=obj_act_id_1)
    EnableTreasure(obj=obj)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=obj_act_id)
    WaitFrames(frames=10)
    EnableTreasure(obj=obj)


@RestartOnRest(12305000)
def Event_12305000():
    """Event 12305000"""
    EndIfFlagEnabled(12305001)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2300250)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=2300250, other_entity=PLAYER, radius=10.0)
    IfConditionTrue(-2, input_condition=1)
    IfAttackedWithDamageType(-2, attacked_entity=2300250)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(2300250)
    WaitFrames(frames=1)
    SetNest(2300250, region=2302310)
    AICommand(2300250, command_id=10, command_slot=0)
    ReplanAI(2300250)


@RestartOnRest(12305001)
def Event_12305001():
    """Event 12305001"""
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(0, 2300250, region=2302310)
    ForceAnimation(2300250, 3000)
    AICommand(2300250, command_id=-1, command_slot=0)
    ReplanAI(2300250)


@RestartOnRest(12305010)
def Event_12305010(_, character__projectile_id: int, animation_id: int, event_slot: int, ai_param_id: int):
    """Event 12305010"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    StopEvent(event_id=12305140, event_slot=event_slot)
    StopEvent(event_id=12305160, event_slot=event_slot)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(2, 2300305, ai_status=AIStatusType.Battle)
    IfCharacterAlive(2, 2300305)
    IfHasAIStatus(3, 2300305, ai_status=AIStatusType.Battle)
    IfCharacterAlive(3, 2300305)
    IfHasAIStatus(4, 2300401, ai_status=AIStatusType.Battle)
    IfCharacterAlive(4, 2300401)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterWhitePhantom(-3, PLAYER)
    IfConditionTrue(1, input_condition=-3)
    IfCharacterInsideRegion(1, PLAYER, region=2302147)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-1, input_condition=1)
    IfHasAIStatus(-1, character__projectile_id, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character__projectile_id, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-1, character__projectile_id, 4670)
    IfConditionTrue(0, input_condition=-1)
    Wait(3.0)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=character__projectile_id,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(character__projectile_id, animation_id)
    StopEvent(event_id=12305140, event_slot=event_slot)
    StopEvent(event_id=12305160, event_slot=event_slot)


@RestartOnRest(12305020)
def Event_12305020():
    """Event 12305020"""
    DisableAI(2300730)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302020)
    IfCharacterInsideRegion(-2, PLAYER, region=2302021)
    IfConditionTrue(1, input_condition=-2)
    IfFlagDisabled(1, 1325)
    IfCharacterAlive(1, 2300710)
    IfConditionTrue(0, input_condition=1)
    EnableAI(2300730)


@RestartOnRest(12305021)
def Event_12305021():
    """Event 12305021"""
    GotoIfFlagEnabled(Label.L0, flag=1324)
    IfCharacterDead(-1, 2300710)
    IfFlagEnabled(-1, 1324)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2300730, 7000, loop=True)


@RestartOnRest(12305022)
def Event_12305022():
    """Event 12305022"""
    DisableGravity(2300730)
    DisableCharacterCollision(2300730)


@RestartOnRest(12305023)
def Event_12305023():
    """Event 12305023"""
    IfHasAIStatus(1, 2300710, ai_status=AIStatusType.Battle)
    IfCharacterDead(2, 2300710)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(input_condition=2)
    ForceAnimation(2300730, 7000, loop=True)
    IfHasAIStatus(3, 2300710, ai_status=AIStatusType.Normal)
    IfCharacterDead(4, 2300710)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(input_condition=4)
    ForceAnimation(2300730, 7001, wait_for_completion=True)
    Restart()


@RestartOnRest(12305030)
def Event_12305030(_, region: int, obj: int, region_1: int):
    """Event 12305030"""
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfObjectNotDestroyed(1, obj)
    IfConditionTrue(0, input_condition=1)
    SetCharacterEventTarget(2300730, region=region_1)
    AICommand(2300730, command_id=100, command_slot=0)
    ReplanAI(2300730)
    IfCharacterHasTAEEvent(0, 2300730, tae_event_id=100)
    AICommand(2300730, command_id=-1, command_slot=0)
    ReplanAI(2300730)
    Restart()


@NeverRestart(12305040)
def Event_12305040(_, obj__projectile_id: int, owner_entity: int):
    """Event 12305040"""
    EndIfThisEventSlotFlagEnabled()
    IfAttackedWithDamageType(-1, attacked_entity=obj__projectile_id, damage_type=DamageType.Fire)
    IfAttackedWithDamageType(-1, attacked_entity=obj__projectile_id, damage_type=DamageType.NoType)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Magic)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Lightning)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Blunt)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Slash)
    IfAttackedWithDamageType(-2, attacked_entity=obj__projectile_id, damage_type=DamageType.Thrust)
    IfConditionTrue(2, input_condition=-2)
    IfObjectHealthValueComparison(2, obj__projectile_id, ComparisonType.LessThanOrEqual, value=999)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ShootProjectile(
        owner_entity=owner_entity,
        projectile_id=obj__projectile_id,
        model_point=-1,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(obj__projectile_id)
    PlaySoundEffect(obj__projectile_id, 299961000, sound_type=SoundType.o_Object)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=owner_entity,
        projectile_id=obj__projectile_id,
        model_point=-1,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=owner_entity,
        projectile_id=obj__projectile_id,
        model_point=-1,
        behavior_id=6071,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DestroyObject(obj__projectile_id)
    PlaySoundEffect(obj__projectile_id, 299961000, sound_type=SoundType.o_Object)


@RestartOnRest(12305070)
def Event_12305070():
    """Event 12305070"""
    GotoIfThisEventFlagDisabled(Label.L0)
    PostDestruction(2301310)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(2300601)
    DisableGravity(2300601)
    DisableCharacterCollision(2300601)
    DisableAnimations(2300601)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302040)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=2300601, radius=3.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=2300520)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(2300601, 7014)
    EnableAI(2300601)
    EnableAnimations(2300601)
    WaitFrames(frames=30)
    EnableGravity(2300601)
    EnableCharacterCollision(2300601)


@RestartOnRest(12305075)
def Event_12305075(_, character__projectile_id: int, animation_id: int, event_slot: int, ai_param_id: int):
    """Event 12305075"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    StopEvent(event_id=12305140, event_slot=event_slot)
    StopEvent(event_id=12305160, event_slot=event_slot)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-1, 12305070)
    IfHasAIStatus(-1, character__projectile_id, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character__projectile_id, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-1, character__projectile_id, 4670)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=character__projectile_id,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(character__projectile_id, animation_id)
    StopEvent(event_id=12305140, event_slot=event_slot)
    StopEvent(event_id=12305160, event_slot=event_slot)


@RestartOnRest(12305080)
def Event_12305080():
    """Event 12305080"""
    EndIfFlagRangeAnyEnabled(flag_range=(12305081, 12305082))
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfCharacterInsideRegion(-2, PLAYER, region=2302010)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=2300314, radius=10.0)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfFlagRangeAnyEnabled(2, flag_range=(12305081, 12305082))
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfAttackedWithDamageType(-3, attacked_entity=2300314)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=2)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(2300314, region=2302350)
    AICommand(2300314, command_id=10, command_slot=0)
    ReplanAI(2300314)


@RestartOnRest(12305081)
def Event_12305081():
    """Event 12305081"""
    EndIfFlagEnabled(12305082)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterInsideRegion(0, 2300314, region=2302050)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2300314, command_id=30, command_slot=0)
    ReplanAI(2300314)


@RestartOnRest(12305082)
def Event_12305082():
    """Event 12305082"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302011)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=2300314, radius=3.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300314, command_id=-1, command_slot=0)
    ReplanAI(2300314)


@NeverRestart(12305090)
def Event_12305090(_, frames: int, projectile_id: int):
    """Event 12305090"""
    EndIfFlagEnabled(12300240)
    IfFlagEnabled(0, 12300240)
    WaitFrames(frames=frames)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=projectile_id,
        model_point=101,
        behavior_id=6070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )


@RestartOnRest(12305100)
def Event_12305100(_, character: int, region: int, frames: int):
    """Event 12305100"""
    GotoIfFlagEnabled(Label.L0, flag=12300240)
    IfFlagEnabled(1, 12300240)
    IfCharacterInsideRegion(1, character, region=region)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=frames)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 7012, loop=True)


@RestartOnRest(12305110)
def Event_12305110(_, character: int, frames: int):
    """Event 12305110"""
    EndIfFlagEnabled(12300240)
    IfFlagEnabled(1, 12300240)
    IfHasAIStatus(1, character, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(frames=frames)
    Kill(character, award_souls=True)


@RestartOnRest(12305120)
def Event_12305120():
    """Event 12305120"""
    IfFlagEnabled(1, 12300240)
    IfHasAIStatus(1, 2300605, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    SetCharacterEventTarget(2300605, region=2300921)
    AICommand(2300605, command_id=60, command_slot=0)
    IfHasAIStatus(0, 2300605, ai_status=AIStatusType.Battle)
    AICommand(2300605, command_id=-1, command_slot=0)
    Restart()


@RestartOnRest(12305121)
def Event_12305121(_, character__projectile_id: int, animation_id: int, event_slot: int, ai_param_id: int):
    """Event 12305121"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    StopEvent(event_id=12305140, event_slot=event_slot)
    StopEvent(event_id=12305160, event_slot=event_slot)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(-1, 2300201, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, 2300202, ai_status=AIStatusType.Battle)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-1, character__projectile_id, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character__projectile_id, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-1, character__projectile_id, 4670)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=character__projectile_id,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(character__projectile_id, animation_id)
    StopEvent(event_id=12305140, event_slot=event_slot)
    StopEvent(event_id=12305160, event_slot=event_slot)


@RestartOnRest(12305125)
def Event_12305125():
    """Event 12305125"""
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(0, 2300201, ai_status=AIStatusType.Battle)
    RotateToFaceEntity(2300201, PLAYER, animation=3008)


@RestartOnRest(12305130)
def Event_12305130():
    """Event 12305130"""
    EndIfThisEventFlagEnabled()
    DisableGravity(2300203)
    DisableCharacterCollision(2300203)
    DisableAI(2300203)
    ForceAnimation(2300203, 7016, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302090)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=2300203, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=2300203)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(2300203, 7017)
    EnableGravity(2300203)
    EnableCharacterCollision(2300203)
    EnableAI(2300203)
    ReplanAI(2300203)


@RestartOnRest(12305135)
def Event_12305135(_, character__projectile_id: int, animation_id: int, event_slot: int, ai_param_id: int):
    """Event 12305135"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    StopEvent(event_id=12305140, event_slot=event_slot)
    StopEvent(event_id=12305160, event_slot=event_slot)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302148)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-2, character__projectile_id, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, character__projectile_id, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-2, character__projectile_id, 4670)
    IfConditionTrue(0, input_condition=-2)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=character__projectile_id,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(character__projectile_id, animation_id)
    StopEvent(event_id=12305140, event_slot=event_slot)
    StopEvent(event_id=12305160, event_slot=event_slot)


@RestartOnRest(12305140)
def Event_12305140(_, character: int, animation_id: int, animation_id_1: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12305140"""
    ForceAnimation(character, animation_id, loop=True)
    SetAIParamID(character, ai_param_id=ai_param_id)
    IfEntityWithinDistance(-1, entity=PLAYER, other_entity=character, radius=2.0)
    IfHasAIStatus(-1, character, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    ForceAnimation(character, animation_id_1, loop=True)
    IfHasAIStatus(0, character, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest(12305160)
def Event_12305160(_, character__projectile_id: int, animation_id: int, event_slot: int, ai_param_id: int):
    """Event 12305160"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(-1, character__projectile_id, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, character__projectile_id, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-1, character__projectile_id, 4670)
    IfConditionTrue(0, input_condition=-1)
    StopEvent(event_id=12305140, event_slot=event_slot)
    WaitFrames(frames=1)
    SetAIParamID(character__projectile_id, ai_param_id=ai_param_id)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=character__projectile_id,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(character__projectile_id, animation_id)


@RestartOnRest(12305180)
def Event_12305180(_, character: int, region: int, radius: float, seconds: float):
    """Event 12305180"""
    EndIfThisEventSlotFlagEnabled()
    DisableAI(character)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=region)
    IfEntityWithinDistance(-2, entity=PLAYER, other_entity=character, radius=radius)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttacked(-3, attacked_entity=character, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    Wait(seconds)
    EnableAI(character)


@RestartOnRest(12305190)
def Event_12305190(_, character: int):
    """Event 12305190"""
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(1, PLAYER, 404)
    IfEntityWithinDistance(1, entity=PLAYER, other_entity=character, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    ReplanAI(character)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 404)
    ReplanAI(character)
    Restart()


@RestartOnRest(12305250)
def Event_12305250():
    """Event 12305250"""
    IfCharacterInsideRegion(0, PLAYER, region=2302070)
    AICommand(2300200, command_id=100, command_slot=1)
    IfCharacterOutsideRegion(0, PLAYER, region=2302070)
    AICommand(2300200, command_id=-1, command_slot=1)
    Restart()


@RestartOnRest(12305300)
def Event_12305300(_, character: int, character_1: int, radius: float):
    """Event 12305300"""
    IfCharacterHasTAEEvent(1, character, tae_event_id=10)
    IfEntityWithinDistance(1, entity=character, other_entity=character_1, radius=radius)
    IfCharacterAlive(1, character_1)
    IfCharacterBackreadEnabled(1, character_1)
    IfConditionTrue(0, input_condition=1)
    AICommand(character_1, command_id=200, command_slot=1)
    IfCharacterHasTAEEvent(0, character_1, tae_event_id=20)
    AddSpecialEffect(character_1, 5645)
    AICommand(character_1, command_id=-1, command_slot=1)
    Restart()


@RestartOnRest(12305440)
def Event_12305440(_, character: int, special_effect_id: int):
    """Event 12305440"""
    IfCharacterHasSpecialEffect(0, character, 5645)
    AddSpecialEffect(character, special_effect_id)
    IfCharacterDoesNotHaveSpecialEffect(0, character, 5645)
    CancelSpecialEffect(character, special_effect_id)
    Restart()


@RestartOnRest(12305480)
def Event_12305480():
    """Event 12305480"""
    EndIfFlagEnabled(12305481)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302101)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, entity=2300406, other_entity=PLAYER, radius=3.0)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfAttackedWithDamageType(-3, attacked_entity=2300406)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(input_condition=2)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(2300406, region=2302410)
    AICommand(2300406, command_id=10, command_slot=0)
    ReplanAI(2300406)


@RestartOnRest(12305481)
def Event_12305481():
    """Event 12305481"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=2300406, other_entity=PLAYER, radius=3.0)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, 2300406, region=2302410)
    IfAttackedWithDamageType(-2, attacked_entity=2300406)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2300406, command_id=-1, command_slot=0)
    ReplanAI(2300406)


@RestartOnRest(12305482)
def Event_12305482():
    """Event 12305482"""
    GotoIfThisEventFlagEnabled(Label.L0)
    SetAIParamID(2300407, ai_param_id=109013)
    IfFlagEnabled(-1, 12305480)
    IfCharacterHasTAEEvent(-1, 2300407, tae_event_id=20)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(2300407, ai_param_id=109010)
    ReplanAI(2300407)


@RestartOnRest(12305490)
def Event_12305490(_, attacked_entity: int, animation_id: int):
    """Event 12305490"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(attacked_entity, animation_id, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, entity=attacked_entity, other_entity=PLAYER, radius=7.0)
    IfConditionTrue(-3, input_condition=1)
    IfCharacterHasTAEEvent(-2, 2300603, tae_event_id=10)
    IfCharacterHasTAEEvent(-2, 2300604, tae_event_id=10)
    IfCharacterHasTAEEvent(-2, 2300605, tae_event_id=10)
    IfConditionTrue(-3, input_condition=-2)
    IfAttackedWithDamageType(-3, attacked_entity=attacked_entity)
    IfConditionTrue(0, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(attacked_entity, 0)


@RestartOnRest(12305501)
def Event_12305501():
    """Event 12305501"""
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302130)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300606, command_id=40, command_slot=0)
    ReplanAI(2300606)
    IfHasAIStatus(0, 2300606, ai_status=AIStatusType.Battle)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2300606, command_id=-1, command_slot=0)


@RestartOnRest(12305502)
def Event_12305502(_, region: int, event_slot: int):
    """Event 12305502"""
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=region)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300605, command_id=40, command_slot=0)
    ReplanAI(2300605)
    IfCharacterHasTAEEvent(0, 2300605, tae_event_id=10)
    AICommand(2300605, command_id=-1, command_slot=0)
    StopEvent(event_id=12305502, event_slot=event_slot)


@RestartOnRest(12305510)
def Event_12305510(_, character: int, region: int, region_1: int, ai_param_id: int, ai_param_id_1: int):
    """Event 12305510"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302060)
    IfCharacterHasTAEEvent(1, 2300605, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    SetNest(character, region=region)
    SetAIParamID(character, ai_param_id=ai_param_id)
    Wait(20.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(character, region=region_1)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(12300700)
def Event_12300700():
    """Event 12300700"""
    GotoIfFlagEnabled(Label.L0, flag=1320)
    IfFlagDisabled(1, 1323)
    IfFlagDisabled(1, 1324)
    IfFlagDisabled(1, 1325)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2302711)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(2300710, TeamType.FriendlyNPC)
    DisableFlagRange((1320, 1325))
    EnableFlag(1320)


@RestartOnRest(12300701)
def Event_12300701():
    """Event 12300701"""
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(1323)
    EndIfFlagEnabled(1324)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302710)
    IfFlagEnabled(1, 1320)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(2300710, TeamType.Enemy1)
    DisableFlagRange((1320, 1325))
    EnableFlag(1321)


@RestartOnRest(12300702)
def Event_12300702():
    """Event 12300702"""
    GotoIfFlagDisabled(Label.L0, flag=1322)
    SetTeamType(2300710, TeamType.Enemy1)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(-1, PLAYER, region=2302020)
    IfCharacterInsideRegion(-1, PLAYER, region=2302021)
    IfCharacterInsideRegion(-1, PLAYER, region=2302714)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, 1323)
    IfFlagDisabled(1, 1325)
    IfCharacterAlive(1, 2300710)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(2300710, TeamType.Enemy1)
    DisableFlagRange((1320, 1325))
    EnableFlag(1322)


@RestartOnRest(12300703)
def Event_12300703():
    """Event 12300703"""
    GotoIfFlagEnabled(Label.L0, flag=1323)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 1320)
    IfAttackedWithDamageType(1, attacked_entity=2300710, attacker=PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfFlagEnabled(2, 1325)
    IfAttackedWithDamageType(2, attacked_entity=2300710, attacker=PLAYER)
    IfFlagEnabled(3, 1325)
    IfFlagRangeAnyEnabled(3, flag_range=(12300710, 12300739))
    IfFlagEnabled(4, 72300307)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(2300710, TeamType.Enemy1)
    ReplanAI(2300710)
    DisableFlagRange((1320, 1325))
    EnableFlag(1323)
    SaveRequest()


@RestartOnRest(12300704)
def Event_12300704():
    """Event 12300704"""
    GotoIfFlagDisabled(Label.L0, flag=1324)
    DisableCharacter(2300710)
    DropMandatoryTreasure(2300710)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2300710)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(frames=1)
    DisableFlagRange((1320, 1325))
    EnableFlag(1324)
    EnableFlag(5914)
    SaveRequest()


@RestartOnRest(12300705)
def Event_12300705():
    """Event 12300705"""
    GotoIfFlagDisabled(Label.L0, flag=1325)
    SetTeamType(2300710, TeamType.FriendlyNPC)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 1320)
    IfFlagEnabled(1, 72300305)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1320, 1325))
    EnableFlag(1325)


@RestartOnRest(12305701)
def Event_12305701():
    """Event 12305701"""
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(1324)
    ForceAnimation(2300710, 103041, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterWhitePhantom(-1, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302700)
    IfFlagEnabled(-2, 1321)
    IfFlagEnabled(-2, 1322)
    IfFlagEnabled(-2, 1323)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=2302701)
    IfFlagEnabled(-3, 1320)
    IfFlagEnabled(-3, 1325)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(-4, input_condition=1)
    IfConditionTrue(-4, input_condition=2)
    IfConditionTrue(0, input_condition=-4)
    RotateToFaceEntity(2300710, PLAYER, animation=103040)
    ChangePatrolBehavior(2300710, patrol_information_id=2303060)


@RestartOnRest(12300707)
def Event_12300707():
    """Event 12300707"""
    IfAllPlayersOutsideRegion(1, region=2302500)
    IfFlagEnabled(-1, 1321)
    IfFlagEnabled(-1, 1322)
    IfFlagEnabled(-1, 1323)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SetNest(2300710, region=2302320)
    AICommand(2300710, command_id=20, command_slot=0)
    ReplanAI(2300710)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterWhitePhantom(-2, PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302500)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300710, command_id=-1, command_slot=0)
    ReplanAI(2300710)
    Restart()


@RestartOnRest(12300708)
def Event_12300708():
    """Event 12300708"""
    IfCharacterInsideRegion(0, 2300710, region=2302502)
    AICommand(2300710, command_id=100, command_slot=1)
    IfCharacterOutsideRegion(0, 2300710, region=2302502)
    AICommand(2300710, command_id=-1, command_slot=1)
    Restart()


@RestartOnRest(12300710)
def Event_12300710(_, attacked_entity: int):
    """Event 12300710"""
    GotoIfFlagRangeAnyEnabled(Label.L0, flag_range=(12300710, 12300739))
    IfFlagEnabled(1, 1325)
    IfAttackedWithDamageType(1, attacked_entity=attacked_entity, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12300709)


@RestartOnRest(12300750)
def Event_12300750():
    """Event 12300750"""
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(12300751)
    IfCharacterOutsideRegion(1, PLAYER, region=2302160)
    IfCharacterOutsideRegion(1, PLAYER, region=2302161)
    IfCharacterHuman(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12300751)
    IfCharacterInsideRegion(-2, PLAYER, region=2302160)
    IfCharacterInsideRegion(-2, PLAYER, region=2302161)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterHuman(2, PLAYER)
    IfConditionTrue(0, input_condition=2)
    Restart()


@RestartOnRest(12300752)
def Event_12300752():
    """Event 12300752"""
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    SetNetworkUpdateAuthority(2300710, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2300730, authority_level=UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    SetNetworkUpdateRate(2300730, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(2300710, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(12300753)
def Event_12300753():
    """Event 12300753"""
    IfInsideMap(0, game_map=OLD_YHARNAM)
    SetDistanceLimitForConversationStateChanges(character=2300710, distance=130.0)
    IfOutsideMap(0, game_map=OLD_YHARNAM)
    SetDistanceLimitForConversationStateChanges(character=2300710, distance=17.0)
    Restart()


@NeverRestart(12300990)
def Event_12300990():
    """Event 12300990"""
    EndIfThisEventFlagEnabled()
    IfStandingOnCollision(0, 2303500)
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=154,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=154,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=154,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=154,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )


@NeverRestart(12304020)
def Event_12304020():
    """Event 12304020"""
    IfCharacterInsideRegion(0, PLAYER, region=2302900)
    CreatePlayLog(name=176)


@NeverRestart(12304021)
def Event_12304021():
    """Event 12304021"""
    IfCharacterInsideRegion(0, PLAYER, region=2302901)
    CreatePlayLog(name=202)


@NeverRestart(12304022)
def Event_12304022():
    """Event 12304022"""
    IfFlagEnabled(1, 12304830)
    IfCharacterHasSpecialEffect(1, PLAYER, 5660)
    IfConditionTrue(0, input_condition=1)
    StopPlayLogMeasurement(measurement_id=2301000)
