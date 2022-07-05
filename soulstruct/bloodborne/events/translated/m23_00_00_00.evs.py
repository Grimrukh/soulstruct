"""OLD YHARNAM

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
from .m23_00_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=5, args=(2300950, Objects.OldYharnamLantern, 999, 12307800))
    RunEvent(7000, slot=6, args=(2300951, Objects.BloodStarvedBeastLantern, Flags.BloodStarvedBeastDead, 12307820))
    RunEvent(7000, slot=7, args=(2300952, Objects.DarkbeastPaarlLantern, Flags.DarkbeastPaarlDead, 12307840))
    RunEvent(7100, slot=5, args=(72300200, Objects.OldYharnamLantern))
    RunEvent(7100, slot=6, args=(72300201, Objects.BloodStarvedBeastLantern))
    RunEvent(7100, slot=7, args=(72300202, Objects.DarkbeastPaarlLantern))
    RunEvent(7200, slot=5, args=(72300100, Objects.OldYharnamLantern, 2102950))
    RunEvent(7200, slot=6, args=(72300101, Objects.BloodStarvedBeastLantern, 2102950))
    RunEvent(7200, slot=7, args=(72300102, Objects.DarkbeastPaarlLantern, 2102950))
    RunEvent(7300, slot=5, args=(72102300, Objects.OldYharnamLantern))
    RunEvent(7300, slot=6, args=(72102301, Objects.BloodStarvedBeastLantern))
    RunEvent(7300, slot=7, args=(72102302, Objects.DarkbeastPaarlLantern))
    RunEvent(7600, slot=10, args=(2301999, 2303999))
    RunEvent(9200, slot=1, args=(2303900,))
    RunEvent(9220, slot=1, args=(2300750, 12304220, 12304221, 2300, 23, 0), arg_types="iiiiBB")
    RunEvent(9240, slot=1, args=(2300750, 12304220, 12304221, 12304222, 23, 0), arg_types="iiiiBB")
    RunEvent(9260, slot=1, args=(2300750, 12304220, 12304221, 12304222, 23, 0), arg_types="iiiiBB")
    RunEvent(9280, slot=1, args=(2300750, 12304220, 12304221, 2300, 12304800, 23, 0), arg_types="iiiiiBB")
    DeleteVFX(2303400, erase_root_only=False)
    DeleteVFX(2303910, erase_root_only=False)
    DeleteVFX(2303911, erase_root_only=False)
    RunEvent(12304400, slot=0, args=(12304440, 2303400, 12304420, 12304430, Flags.BloodStarvedBeastDead, 6001))
    RunEvent(12304401, slot=0, args=(12304441, 2303910, 12304421, 12304431, Flags.DarkbeastPaarlDead, 12304422))
    RunEvent(12304402, slot=0, args=(12304442, 2303911, 12304422, 12304432, Flags.DarkbeastPaarlDead, 12304421))
    RunEvent(
        12304410, slot=0, args=(0, 2300740, 2302720, 12304420, 12304430, 12304440, Flags.BloodStarvedBeastDead, 10576))
    RunEvent(
        12304410, slot=1, args=(0, 2300930, 2302910, 12304421, 12304431, 12304441, Flags.DarkbeastPaarlDead, 10568))
    RunEvent(
        12304410, slot=2, args=(5, 2300931, 2302913, 12304422, 12304432, 12304442, Flags.DarkbeastPaarlDead, 10564))
    RunEvent(12304450, slot=0, args=(2300740, 2302722, 12304420, 12304430, 12304800))
    RunEvent(12304450, slot=1, args=(2300930, 2302911, 12304421, 12304431, 12304700))
    RunEvent(12304450, slot=2, args=(2300931, 2302914, 12304422, 12304432, 12304700))
    RunEvent(12304460, slot=0, args=(2300740, 2302722, 2302800, 2302801, 101130, 12304450, 2302801))
    RunEvent(12304460, slot=1, args=(2300930, 2302911, 2302810, 2302811, 101130, 12304451, 2302811))
    RunEvent(12304460, slot=2, args=(2300931, 2302914, 2302810, 2302811, 101130, 12304452, 2302811))
    StartPlayLogMeasurement(2300000, 0, overwrite=False)
    StartPlayLogMeasurement(2300001, 18, overwrite=True)
    RegisterLadder(start_climbing_flag=12301000, stop_climbing_flag=12301001, obj=2301100)
    RegisterLadder(start_climbing_flag=12301002, stop_climbing_flag=12301003, obj=2301101)
    RegisterLadder(start_climbing_flag=12301004, stop_climbing_flag=12301005, obj=2301102)
    RegisterLadder(start_climbing_flag=12301006, stop_climbing_flag=12301007, obj=2301103)
    RegisterLadder(start_climbing_flag=12301008, stop_climbing_flag=12301009, obj=2301104)
    RegisterLadder(start_climbing_flag=12301010, stop_climbing_flag=12301011, obj=2301105)
    CreateObjectVFX(923230, obj=2301200, model_point=1)
    CreateObjectVFX(923230, obj=2301201, model_point=1)
    CreateObjectVFX(923230, obj=2301202, model_point=1)
    CreateObjectVFX(923230, obj=2301203, model_point=1)
    CreateObjectVFX(923230, obj=2301204, model_point=1)
    CreateObjectVFX(923230, obj=2301205, model_point=1)
    CreateObjectVFX(923230, obj=2301206, model_point=1)
    CreateObjectVFX(923230, obj=2301207, model_point=1)
    CreateObjectVFX(923230, obj=2301208, model_point=1)
    CreateObjectVFX(923230, obj=2301209, model_point=1)
    CreateObjectVFX(923230, obj=2301210, model_point=1)
    CreateObjectVFX(923230, obj=2301211, model_point=1)
    CreateObjectVFX(923230, obj=2301212, model_point=1)
    CreateObjectVFX(923230, obj=2301213, model_point=1)
    CreateObjectVFX(923230, obj=2301214, model_point=1)
    CreateObjectVFX(923230, obj=2301215, model_point=1)
    CreateObjectVFX(923230, obj=2301216, model_point=1)
    CreateObjectVFX(923230, obj=2301217, model_point=1)
    CreateObjectVFX(923230, obj=2301218, model_point=1)
    CreateObjectVFX(923230, obj=2301219, model_point=1)
    CreateObjectVFX(923230, obj=2301230, model_point=1)
    CreateObjectVFX(923230, obj=2301221, model_point=1)
    CreateObjectVFX(923230, obj=2301222, model_point=1)
    CreateObjectVFX(923230, obj=2301223, model_point=1)
    CreateProjectileOwner(2300270)
    CreateProjectileOwner(2300271)
    CreateProjectileOwner(2300272)
    CreateHazard(
        12300300,
        2301400,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300301,
        2301401,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300302,
        2301402,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300303,
        2301403,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300304,
        2301404,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300305,
        2301405,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300306,
        2301406,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300307,
        2301407,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300308,
        2301408,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300309,
        2301409,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300310,
        2301410,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300311,
        2301411,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300312,
        2301412,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300313,
        2301413,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300314,
        2301414,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300315,
        2301415,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300316,
        2301416,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300317,
        2301417,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300318,
        2301418,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300319,
        2301419,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300320,
        2301420,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300321,
        2301421,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300322,
        2301422,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )

    # BLOOD-STARVED BEAST
    Event12304812()
    Event12304813()
    BloodStarvedBeastDies()
    PlayBloodStarvedBeastDeathSound()
    BloodStarvedBeastFirstTime()
    EnterBloodStarvedBeastFog()
    EnterBloodStarvedBeastFogAsSummon()
    Event12304802()
    Event12304803()
    Event12304804()
    Event12304805()
    Event12304807()
    Event12304808()
    SummonStartBloodStarvedBeastBattle()

    # DARKBEAST PAARL
    Event12304732()
    Event12304733()
    DarkbeastPaarlDies()
    PlayDarkbeastPaarlDeathSound()
    DarkbeastPaarlFirstTime()
    Event12304730()
    Event12304731()
    Event12304702()
    Event12304703()
    Event12304704()
    Event12304705()
    Event12304707()
    SummonStartDarkbeastPaarlBattle()

    RunEvent(12304715, slot=0, args=(2300, 2300, 1, 480, 490, 8000, 130), arg_types="hihiiii")
    RunEvent(12304715, slot=1, args=(2301, 2301, 2, 481, 491, 8010, 150), arg_types="hihiiii")
    RunEvent(12304715, slot=2, args=(2302, 2302, 3, 482, 492, 8030, 150), arg_types="hihiiii")
    RunEvent(12304715, slot=3, args=(2303, 2303, 4, 483, 493, 8020, 200), arg_types="hihiiii")
    RunEvent(12304715, slot=4, args=(2304, 2304, 5, 484, 494, 8040, 200), arg_types="hihiiii")
    Event12300100()
    RunEvent(12300110, slot=0, args=(7031, 2301701, 12300120))
    RunEvent(12300110, slot=1, args=(7000, 2301700, 12300121))
    RunEvent(12300110, slot=2, args=(2300031, 2301010, 12300122))
    RunEvent(12300110, slot=3, args=(2300030, 2301020, 12300180))
    RunEvent(12300120, slot=0, args=(2301701, 12300212, 1, 2300000))
    RunEvent(12300120, slot=1, args=(2301700, 12300211, 1, 2300001))
    RunEvent(12300120, slot=2, args=(2301010, 12300213, 1, 2300010))
    Event12300130()
    Event12300140()
    Event12300160()
    Event12300180()
    Event12300190()
    Event12300201()
    Event12300210()
    RunEvent(12300220, slot=0, args=(2300250, 52300990))
    RunEvent(12300220, slot=1, args=(2300251, 52300980))
    RunEvent(12300220, slot=2, args=(2300252, 52300970))
    Event12300230()
    Event12300235()
    Event12300240()
    Event12300250()
    Event12300300()
    RunEvent(12300310, slot=0, args=(2301050, 12300900, 9942))
    Event12305000()
    Event12305001()
    RunEvent(12305010, slot=0, args=(2300304, 7008, 1, 109000))
    RunEvent(12305010, slot=1, args=(2300402, 7002, 2, 109010))
    Event12305020()
    Event12305021()
    Event12305022()
    Event12305023()
    RunEvent(12305030, slot=0, args=(2302032, 2301269, 2300910))
    RunEvent(12305030, slot=1, args=(2302033, 2301266, 2300911))
    RunEvent(12305030, slot=2, args=(2302034, 2301265, 2300913))
    RunEvent(12305030, slot=3, args=(2302035, 2301261, 2300913))
    RunEvent(12305040, slot=0, args=(2301256, 2300900))
    RunEvent(12305040, slot=1, args=(2301257, 2300900))
    RunEvent(12305040, slot=2, args=(2301258, 2300900))
    RunEvent(12305040, slot=3, args=(2301259, 2300900))
    RunEvent(12305040, slot=4, args=(2301260, 2300900))
    RunEvent(12305040, slot=5, args=(2301261, 2300900))
    RunEvent(12305040, slot=6, args=(2301262, 2300900))
    RunEvent(12305040, slot=7, args=(2301263, 2300900))
    RunEvent(12305040, slot=8, args=(2301264, 2300900))
    RunEvent(12305040, slot=9, args=(2301265, 2300900))
    RunEvent(12305040, slot=10, args=(2301266, 2300900))
    RunEvent(12305040, slot=11, args=(2301267, 2300900))
    RunEvent(12305040, slot=12, args=(2301268, 2300900))
    RunEvent(12305040, slot=13, args=(2301269, 2300900))
    Event12305070()
    RunEvent(12305075, slot=0, args=(2300309, 7008, 3, 109000))
    RunEvent(12305075, slot=1, args=(2300310, 7002, 4, 109000))
    Event12305080()
    Event12305081()
    Event12305082()
    RunEvent(12305090, slot=0, args=(0, 2300920))
    RunEvent(12305090, slot=1, args=(20, 2300921))
    RunEvent(12305100, slot=0, args=(2300408, 2302211, 30))
    RunEvent(12305100, slot=1, args=(2300409, 2302213, 40))
    RunEvent(12305100, slot=2, args=(2300410, 2302215, 60))
    RunEvent(12305110, slot=0, args=(2300320, 0))
    RunEvent(12305110, slot=1, args=(2300321, 15))
    RunEvent(12305110, slot=2, args=(2300322, 35))
    RunEvent(12305110, slot=3, args=(2300323, 5))
    RunEvent(12305110, slot=4, args=(2300324, 55))
    Event12305120()
    RunEvent(12305121, slot=0, args=(2300325, 7005, 12, 109000))
    RunEvent(12305121, slot=1, args=(2300326, 7005, 13, 109000))
    RunEvent(12305121, slot=2, args=(2300327, 7002, 14, 109000))
    Event12305125()
    Event12305130()
    RunEvent(12305135, slot=0, args=(2300413, 7002, 15, 109010))
    RunEvent(12305135, slot=1, args=(2300414, 7008, 16, 109010))
    RunEvent(12305140, slot=0, args=(2300303, 7000, 7001, 109900, 109912))
    RunEvent(12305140, slot=1, args=(2300304, 7000, 7001, 109900, 109913))
    RunEvent(12305140, slot=2, args=(2300402, 7000, 7001, 109900, 109913))
    RunEvent(12305140, slot=3, args=(2300309, 7006, 7007, 109900, 109912))
    RunEvent(12305140, slot=4, args=(2300310, 7000, 7001, 109900, 109912))
    RunEvent(12305140, slot=5, args=(2300312, 7000, 7001, 109900, 109912))
    RunEvent(12305140, slot=6, args=(2300315, 7003, 7004, 109900, 109912))
    RunEvent(12305140, slot=7, args=(2300316, 7006, 7007, 109900, 109912))
    RunEvent(12305140, slot=8, args=(2300317, 7000, 7001, 109900, 109912))
    RunEvent(12305140, slot=9, args=(2300403, 7006, 7007, 109900, 109912))
    RunEvent(12305140, slot=10, args=(2300404, 7003, 7004, 109900, 109912))
    RunEvent(12305140, slot=11, args=(2300405, 7006, 7007, 109900, 109912))
    RunEvent(12305140, slot=12, args=(2300325, 7003, 7004, 109900, 109912))
    RunEvent(12305140, slot=13, args=(2300326, 7003, 7004, 109900, 109912))
    RunEvent(12305140, slot=14, args=(2300327, 7000, 7001, 109900, 109912))
    RunEvent(12305140, slot=15, args=(2300413, 7000, 7001, 109900, 109912))
    RunEvent(12305140, slot=16, args=(2300414, 7006, 7007, 109900, 109912))
    RunEvent(12305140, slot=17, args=(2300500, 7000, 7001, 109015, 109015))
    RunEvent(12305140, slot=18, args=(2300501, 7000, 7001, 109015, 109015))
    RunEvent(12305140, slot=19, args=(2300502, 7000, 7001, 109015, 109015))
    RunEvent(12305160, slot=0, args=(2300303, 7002, 0, 109000))
    RunEvent(12305160, slot=1, args=(2300304, 7002, 1, 109000))
    RunEvent(12305160, slot=2, args=(2300402, 7002, 2, 109010))
    RunEvent(12305160, slot=3, args=(2300309, 7008, 3, 109000))
    RunEvent(12305160, slot=4, args=(2300310, 7002, 4, 109000))
    RunEvent(12305160, slot=5, args=(2300312, 7002, 5, 109000))
    RunEvent(12305160, slot=6, args=(2300315, 7005, 6, 109000))
    RunEvent(12305160, slot=7, args=(2300316, 7008, 7, 109000))
    RunEvent(12305160, slot=8, args=(2300317, 7002, 8, 109000))
    RunEvent(12305160, slot=9, args=(2300403, 7008, 9, 109010))
    RunEvent(12305160, slot=10, args=(2300404, 7005, 10, 109010))
    RunEvent(12305160, slot=11, args=(2300405, 7008, 11, 109010))
    RunEvent(12305160, slot=12, args=(2300325, 7005, 12, 109000))
    RunEvent(12305160, slot=13, args=(2300326, 7005, 13, 109000))
    RunEvent(12305160, slot=14, args=(2300327, 7002, 14, 109000))
    RunEvent(12305160, slot=15, args=(2300413, 7002, 15, 109010))
    RunEvent(12305160, slot=16, args=(2300414, 7008, 16, 109010))
    RunEvent(12305160, slot=17, args=(2300500, 7002, 17, 109010))
    RunEvent(12305160, slot=18, args=(2300501, 7002, 18, 109010))
    RunEvent(12305160, slot=19, args=(2300502, 7002, 19, 109010))
    RunEvent(12305180, slot=0, args=(2300300, 2302140, 15.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=1, args=(2300301, 2302141, 5.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=2, args=(2300302, 2302141, 5.0, 2.5), arg_types="iiff")
    RunEvent(12305180, slot=3, args=(2300401, 2302147, 5.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=4, args=(2300201, 2302146, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=5, args=(2300202, 2302146, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=6, args=(2300205, 2302130, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=7, args=(2300330, 2302148, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=8, args=(2300331, 2302148, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=9, args=(2300332, 2302148, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=10, args=(2300333, 2302148, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=11, args=(2300334, 2302148, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=13, args=(2300607, 2302148, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=14, args=(2300608, 2302148, 10.0, 0.0), arg_types="iiff")
    RunEvent(12305180, slot=15, args=(2300600, 2302149, 3.0, 0.0), arg_types="iiff")
    RunEvent(12305190, slot=0, args=(2300200,))
    RunEvent(12305190, slot=1, args=(2300201,))
    RunEvent(12305190, slot=2, args=(2300202,))
    RunEvent(12305190, slot=3, args=(2300203,))
    RunEvent(12305190, slot=4, args=(2300204,))
    RunEvent(12305190, slot=5, args=(2300205,))
    RunEvent(12305190, slot=6, args=(2300206,))
    RunEvent(12305190, slot=7, args=(2300207,))
    RunEvent(12305190, slot=8, args=(2300208,))
    RunEvent(12305190, slot=9, args=(2300209,))
    RunEvent(12305190, slot=10, args=(2300210,))
    RunEvent(12305190, slot=11, args=(2300211,))
    RunEvent(12305190, slot=12, args=(2300212,))
    RunEvent(12305190, slot=13, args=(2300213,))
    RunEvent(12305190, slot=14, args=(2300214,))
    RunEvent(12305190, slot=15, args=(2300215,))
    RunEvent(12305190, slot=16, args=(2300216,))
    RunEvent(12305190, slot=17, args=(2300217,))
    RunEvent(12305190, slot=18, args=(2300218,))
    RunEvent(12305190, slot=19, args=(2300219,))
    RunEvent(12305190, slot=20, args=(2300220,))
    RunEvent(12305190, slot=21, args=(2300221,))
    RunEvent(12305190, slot=22, args=(2300222,))
    RunEvent(12305190, slot=23, args=(2300223,))
    RunEvent(12305190, slot=24, args=(2300224,))
    RunEvent(12305190, slot=25, args=(2300225,))
    RunEvent(12305190, slot=26, args=(2300226,))
    RunEvent(12305190, slot=27, args=(2300227,))
    RunEvent(12305190, slot=28, args=(2300228,))
    RunEvent(12305190, slot=29, args=(2300229,))
    RunEvent(12305190, slot=30, args=(2300230,))
    RunEvent(12305190, slot=31, args=(2300231,))
    RunEvent(12305190, slot=32, args=(2300232,))
    RunEvent(12305190, slot=33, args=(2300233,))
    RunEvent(12305190, slot=34, args=(2300234,))
    Event12305250()
    RunEvent(12305300, slot=0, args=(2300602, 2300309, 20.0), arg_types="iif")
    RunEvent(12305300, slot=1, args=(2300602, 2300310, 20.0), arg_types="iif")
    RunEvent(12305300, slot=2, args=(2300602, 2300311, 20.0), arg_types="iif")
    RunEvent(12305300, slot=3, args=(2300602, 2300312, 20.0), arg_types="iif")
    RunEvent(12305300, slot=4, args=(2300602, 2300313, 20.0), arg_types="iif")
    RunEvent(12305300, slot=5, args=(2300602, 2300314, 20.0), arg_types="iif")
    RunEvent(12305300, slot=6, args=(2300602, 2300315, 20.0), arg_types="iif")
    RunEvent(12305300, slot=7, args=(2300602, 2300316, 20.0), arg_types="iif")
    RunEvent(12305300, slot=8, args=(2300602, 2300317, 20.0), arg_types="iif")
    RunEvent(12305300, slot=9, args=(2300602, 2300318, 20.0), arg_types="iif")
    RunEvent(12305300, slot=10, args=(2300602, 2300319, 20.0), arg_types="iif")
    RunEvent(12305300, slot=11, args=(2300602, 2300320, 20.0), arg_types="iif")
    RunEvent(12305300, slot=12, args=(2300602, 2300321, 20.0), arg_types="iif")
    RunEvent(12305300, slot=13, args=(2300602, 2300322, 20.0), arg_types="iif")
    RunEvent(12305300, slot=14, args=(2300602, 2300323, 20.0), arg_types="iif")
    RunEvent(12305300, slot=15, args=(2300602, 2300324, 20.0), arg_types="iif")
    RunEvent(12305300, slot=16, args=(2300602, 2300403, 20.0), arg_types="iif")
    RunEvent(12305300, slot=17, args=(2300602, 2300404, 20.0), arg_types="iif")
    RunEvent(12305300, slot=18, args=(2300602, 2300405, 20.0), arg_types="iif")
    RunEvent(12305300, slot=19, args=(2300602, 2300406, 20.0), arg_types="iif")
    RunEvent(12305300, slot=20, args=(2300602, 2300407, 20.0), arg_types="iif")
    RunEvent(12305300, slot=21, args=(2300602, 2300408, 20.0), arg_types="iif")
    RunEvent(12305300, slot=22, args=(2300602, 2300409, 20.0), arg_types="iif")
    RunEvent(12305300, slot=23, args=(2300602, 2300410, 20.0), arg_types="iif")
    RunEvent(12305300, slot=24, args=(2300603, 2300309, 35.0), arg_types="iif")
    RunEvent(12305300, slot=25, args=(2300603, 2300310, 35.0), arg_types="iif")
    RunEvent(12305300, slot=26, args=(2300603, 2300311, 35.0), arg_types="iif")
    RunEvent(12305300, slot=27, args=(2300603, 2300312, 35.0), arg_types="iif")
    RunEvent(12305300, slot=28, args=(2300603, 2300313, 35.0), arg_types="iif")
    RunEvent(12305300, slot=29, args=(2300603, 2300314, 35.0), arg_types="iif")
    RunEvent(12305300, slot=30, args=(2300603, 2300315, 35.0), arg_types="iif")
    RunEvent(12305300, slot=31, args=(2300603, 2300316, 35.0), arg_types="iif")
    RunEvent(12305300, slot=32, args=(2300603, 2300317, 35.0), arg_types="iif")
    RunEvent(12305300, slot=33, args=(2300603, 2300318, 35.0), arg_types="iif")
    RunEvent(12305300, slot=34, args=(2300603, 2300319, 35.0), arg_types="iif")
    RunEvent(12305300, slot=35, args=(2300603, 2300320, 35.0), arg_types="iif")
    RunEvent(12305300, slot=36, args=(2300603, 2300321, 35.0), arg_types="iif")
    RunEvent(12305300, slot=37, args=(2300603, 2300322, 35.0), arg_types="iif")
    RunEvent(12305300, slot=38, args=(2300603, 2300323, 35.0), arg_types="iif")
    RunEvent(12305300, slot=39, args=(2300603, 2300324, 35.0), arg_types="iif")
    RunEvent(12305300, slot=40, args=(2300603, 2300403, 35.0), arg_types="iif")
    RunEvent(12305300, slot=41, args=(2300603, 2300404, 35.0), arg_types="iif")
    RunEvent(12305300, slot=42, args=(2300603, 2300405, 35.0), arg_types="iif")
    RunEvent(12305300, slot=43, args=(2300603, 2300406, 35.0), arg_types="iif")
    RunEvent(12305300, slot=44, args=(2300603, 2300407, 35.0), arg_types="iif")
    RunEvent(12305300, slot=45, args=(2300603, 2300408, 35.0), arg_types="iif")
    RunEvent(12305300, slot=46, args=(2300603, 2300409, 35.0), arg_types="iif")
    RunEvent(12305300, slot=47, args=(2300603, 2300410, 35.0), arg_types="iif")
    RunEvent(12305300, slot=48, args=(2300604, 2300318, 35.0), arg_types="iif")
    RunEvent(12305300, slot=49, args=(2300604, 2300319, 35.0), arg_types="iif")
    RunEvent(12305300, slot=50, args=(2300604, 2300320, 35.0), arg_types="iif")
    RunEvent(12305300, slot=51, args=(2300604, 2300321, 35.0), arg_types="iif")
    RunEvent(12305300, slot=52, args=(2300604, 2300322, 35.0), arg_types="iif")
    RunEvent(12305300, slot=53, args=(2300604, 2300323, 35.0), arg_types="iif")
    RunEvent(12305300, slot=54, args=(2300604, 2300324, 35.0), arg_types="iif")
    RunEvent(12305300, slot=55, args=(2300604, 2300406, 35.0), arg_types="iif")
    RunEvent(12305300, slot=56, args=(2300604, 2300407, 35.0), arg_types="iif")
    RunEvent(12305300, slot=57, args=(2300604, 2300408, 35.0), arg_types="iif")
    RunEvent(12305300, slot=58, args=(2300604, 2300409, 35.0), arg_types="iif")
    RunEvent(12305300, slot=59, args=(2300604, 2300410, 35.0), arg_types="iif")
    RunEvent(12305300, slot=60, args=(2300605, 2300318, 35.0), arg_types="iif")
    RunEvent(12305300, slot=61, args=(2300605, 2300319, 35.0), arg_types="iif")
    RunEvent(12305300, slot=62, args=(2300605, 2300320, 35.0), arg_types="iif")
    RunEvent(12305300, slot=63, args=(2300605, 2300321, 35.0), arg_types="iif")
    RunEvent(12305300, slot=64, args=(2300605, 2300322, 35.0), arg_types="iif")
    RunEvent(12305300, slot=65, args=(2300605, 2300323, 35.0), arg_types="iif")
    RunEvent(12305300, slot=66, args=(2300605, 2300324, 35.0), arg_types="iif")
    RunEvent(12305300, slot=67, args=(2300605, 2300406, 35.0), arg_types="iif")
    RunEvent(12305300, slot=68, args=(2300605, 2300407, 35.0), arg_types="iif")
    RunEvent(12305300, slot=69, args=(2300605, 2300408, 35.0), arg_types="iif")
    RunEvent(12305300, slot=70, args=(2300605, 2300409, 35.0), arg_types="iif")
    RunEvent(12305300, slot=71, args=(2300605, 2300410, 35.0), arg_types="iif")
    RunEvent(12305300, slot=72, args=(2300606, 2300325, 25.0), arg_types="iif")
    RunEvent(12305300, slot=73, args=(2300606, 2300326, 25.0), arg_types="iif")
    RunEvent(12305300, slot=74, args=(2300606, 2300327, 25.0), arg_types="iif")
    RunEvent(12305300, slot=75, args=(2300606, 2300201, 25.0), arg_types="iif")
    RunEvent(12305300, slot=76, args=(2300606, 2300202, 25.0), arg_types="iif")
    RunEvent(12305300, slot=77, args=(2300606, 2300203, 25.0), arg_types="iif")
    RunEvent(12305300, slot=78, args=(2300606, 2300204, 25.0), arg_types="iif")
    RunEvent(12305300, slot=79, args=(2300606, 2300205, 25.0), arg_types="iif")
    RunEvent(12305440, slot=0, args=(2300309, 5522))
    RunEvent(12305440, slot=1, args=(2300310, 5522))
    RunEvent(12305440, slot=2, args=(2300311, 5522))
    RunEvent(12305440, slot=3, args=(2300312, 5522))
    RunEvent(12305440, slot=4, args=(2300313, 5522))
    RunEvent(12305440, slot=5, args=(2300314, 5522))
    RunEvent(12305440, slot=6, args=(2300315, 5522))
    RunEvent(12305440, slot=7, args=(2300316, 5522))
    RunEvent(12305440, slot=8, args=(2300317, 5522))
    RunEvent(12305440, slot=9, args=(2300318, 5522))
    RunEvent(12305440, slot=10, args=(2300319, 5522))
    RunEvent(12305440, slot=11, args=(2300320, 5522))
    RunEvent(12305440, slot=12, args=(2300321, 5522))
    RunEvent(12305440, slot=13, args=(2300322, 5522))
    RunEvent(12305440, slot=14, args=(2300323, 5522))
    RunEvent(12305440, slot=15, args=(2300324, 5522))
    RunEvent(12305440, slot=16, args=(2300325, 5522))
    RunEvent(12305440, slot=17, args=(2300326, 5522))
    RunEvent(12305440, slot=18, args=(2300327, 5522))
    RunEvent(12305440, slot=19, args=(2300403, 5524))
    RunEvent(12305440, slot=20, args=(2300404, 5524))
    RunEvent(12305440, slot=21, args=(2300405, 5524))
    RunEvent(12305440, slot=22, args=(2300406, 5524))
    RunEvent(12305440, slot=23, args=(2300407, 5524))
    RunEvent(12305440, slot=24, args=(2300408, 5524))
    RunEvent(12305440, slot=25, args=(2300409, 5524))
    RunEvent(12305440, slot=26, args=(2300410, 5524))
    RunEvent(12305440, slot=27, args=(2300201, 5523))
    RunEvent(12305440, slot=28, args=(2300202, 5523))
    RunEvent(12305440, slot=29, args=(2300203, 5523))
    RunEvent(12305440, slot=30, args=(2300204, 5523))
    RunEvent(12305440, slot=31, args=(2300205, 5523))
    Event12305480()
    Event12305481()
    Event12305482()
    RunEvent(12305490, slot=0, args=(2300320, 7010))
    RunEvent(12305490, slot=1, args=(2300321, 7010))
    RunEvent(12305490, slot=2, args=(2300322, 7010))
    RunEvent(12305490, slot=3, args=(2300323, 7010))
    RunEvent(12305490, slot=4, args=(2300324, 7010))
    RunEvent(12305490, slot=5, args=(2300408, 7010))
    RunEvent(12305490, slot=6, args=(2300409, 7010))
    RunEvent(12305490, slot=7, args=(2300410, 7010))
    Event12305501()
    RunEvent(12305502, slot=0, args=(2302200, 1))
    RunEvent(12305502, slot=1, args=(2302060, 0))
    RunEvent(12305510, slot=0, args=(2300320, 2302220, 2302210, 109008, 109006))
    RunEvent(12305510, slot=1, args=(2300321, 2302222, 2302212, 109008, 109006))
    RunEvent(12305510, slot=2, args=(2300322, 2302224, 2302214, 109008, 109006))
    RunEvent(12305510, slot=3, args=(2300323, 2302227, 2302217, 109008, 109006))
    RunEvent(12305510, slot=4, args=(2300324, 2302226, 2302216, 109008, 109006))
    RunEvent(12305510, slot=5, args=(2300408, 2302223, 2302213, 109014, 109011))
    RunEvent(12305510, slot=6, args=(2300409, 2302221, 2302211, 109014, 109011))
    RunEvent(12305510, slot=7, args=(2300410, 2302225, 2302215, 109014, 109011))
    Event12304020()
    Event12304021()
    Event12304022()
    Event12300700()
    Event12300701()
    Event12300702()
    Event12300703()
    Event12300704()
    Event12300705()
    Event12305701()
    Event12300707()
    Event12300708()
    RunEvent(12300710, slot=0, args=(2300300,))
    RunEvent(12300710, slot=1, args=(2300301,))
    RunEvent(12300710, slot=2, args=(2300302,))
    RunEvent(12300710, slot=3, args=(2300303,))
    RunEvent(12300710, slot=4, args=(2300304,))
    RunEvent(12300710, slot=5, args=(2300305,))
    RunEvent(12300710, slot=6, args=(2300306,))
    RunEvent(12300710, slot=7, args=(2300307,))
    RunEvent(12300710, slot=8, args=(2300308,))
    RunEvent(12300710, slot=9, args=(2300309,))
    RunEvent(12300710, slot=10, args=(2300310,))
    RunEvent(12300710, slot=11, args=(2300311,))
    RunEvent(12300710, slot=12, args=(2300312,))
    RunEvent(12300710, slot=13, args=(2300313,))
    RunEvent(12300710, slot=14, args=(2300314,))
    RunEvent(12300710, slot=15, args=(2300315,))
    RunEvent(12300710, slot=16, args=(2300316,))
    RunEvent(12300710, slot=17, args=(2300317,))
    RunEvent(12300710, slot=18, args=(2300318,))
    RunEvent(12300710, slot=19, args=(2300319,))
    RunEvent(12300710, slot=20, args=(2300320,))
    RunEvent(12300710, slot=21, args=(2300321,))
    RunEvent(12300710, slot=22, args=(2300322,))
    RunEvent(12300710, slot=23, args=(2300323,))
    RunEvent(12300710, slot=24, args=(2300324,))
    RunEvent(12300710, slot=25, args=(2300400,))
    RunEvent(12300710, slot=26, args=(2300401,))
    RunEvent(12300710, slot=27, args=(2300402,))
    RunEvent(12300710, slot=28, args=(2300403,))
    RunEvent(12300710, slot=29, args=(2300404,))
    RunEvent(12300710, slot=30, args=(2300405,))
    RunEvent(12300710, slot=31, args=(2300600,))
    RunEvent(12300710, slot=32, args=(2300601,))
    RunEvent(12300710, slot=33, args=(2300720,))
    Event12300750()
    Event12300752()
    Event12300753()
    Event12300990()


def Preconstructor():
    """ 50: Event 50 """
    DisableAnimations(2303950)
    DisableGravity(2303950)
    DisableCharacterCollision(2303950)
    DisableAnimations(2303951)
    DisableGravity(2303951)
    DisableCharacterCollision(2303951)


def BloodStarvedBeastDies():
    """ 12301800: Event 12301800 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(2303802)
    DisableSoundEvent(2303803)
    DisableCharacter(2300800)
    Kill(Characters.BloodStarvedBeast, award_souls=False)
    DisableObject(Objects.BossFog)
    DeleteVFX(VFX.BossFog, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, Characters.BloodStarvedBeast)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.BossFog)
    DeleteVFX(VFX.BossFog, erase_root_only=True)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=0)
    Wait(3.0)
    KillBoss(Characters.BloodStarvedBeast)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(2,))
    EnableFlag(72400512)
    AwardAchievement(22)
    AwardItemLot(80000000, host_only=False)
    EnableFlag(2300)
    EnableFlag(9453)
    StopPlayLogMeasurement(2300000)
    StopPlayLogMeasurement(2300001)
    StopPlayLogMeasurement(2300010)
    CreatePlayLog(40)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 52, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 52, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayBloodStarvedBeastDeathSound():
    """ 12301801: Event 12301801 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    IfFlagEnabled(1, Flags.BloodStarvedBeastDead)
    IfCharacterBackreadDisabled(2, Characters.BloodStarvedBeast)
    IfHealthLessThanOrEqual(2, Characters.BloodStarvedBeast, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2302800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def BloodStarvedBeastFirstTime():
    """ 12301802: Event 12301802 """
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(1, Flags.BloodStarvedBeastDead)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=Regions.BloodStarvedBeastFirstTimeTrigger)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.BloodStarvedBeast, 7001)
    EnableFlag(12304800)
    EndIfFlagEnabled(9339)
    RunEvent(9350, 0, args=(1,))
    EnableFlag(9339)


def SummonStartBloodStarvedBeastBattle():
    """ 12301803: Event 12301803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12304800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(12304800)
    EnableFlag(Flags.BloodStarvedBeastFirstTimeDone)


def EnterBloodStarvedBeastFog():
    """ 12304810: Event 12304810 """
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    GotoIfFlagEnabled(Label.L0, Flags.BloodStarvedBeastFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.BossFog)
    DeleteVFX(VFX.BossFog, erase_root_only=False)
    IfFlagDisabled(1, Flags.BloodStarvedBeastDead)
    IfFlagEnabled(1, Flags.BloodStarvedBeastFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.BossFog)
    CreateVFX(VFX.BossFog)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2300800, entity=Objects.BossFog)
    IfFlagDisabled(2, Flags.BloodStarvedBeastDead)
    IfFlagEnabled(3, Flags.BloodStarvedBeastDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2302800, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2302801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(12304800)
    Restart()


def EnterBloodStarvedBeastFogAsSummon():
    """ 12304811: Event 12304811 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    IfFlagDisabled(1, Flags.BloodStarvedBeastDead)
    IfFlagEnabled(1, Flags.BloodStarvedBeastFirstTimeDone)
    IfFlagEnabled(1, 12304800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2300800, entity=Objects.BossFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2302800, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2302801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12304801)
    Restart()


def Event12304812():
    """ 12304812: Event 12304812 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.BossFog, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12304813():
    """ 12304813: Event 12304813 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.BossFog, radius=4.0)
    IfEntityWithinDistance(1, PLAYER, Objects.BossFog, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def Event12304802():
    """ 12304802: Event 12304802 """
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    DisableAI(Characters.BloodStarvedBeast)
    DisableHealthBar(Characters.BloodStarvedBeast)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12304800)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.BloodStarvedBeast, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12304800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.BloodStarvedBeast, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.BloodStarvedBeast)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.BloodStarvedBeast, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.BloodStarvedBeast)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.BloodStarvedBeast)
    EnableBossHealthBar(Characters.BloodStarvedBeast, name=209000, slot=0)
    CreatePlayLog(86)
    StartPlayLogMeasurement(2300010, 102, overwrite=True)


def Event12304803():
    """ 12304803: Event 12304803 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2303802)
    DisableSoundEvent(2303803)
    IfFlagDisabled(1, Flags.BloodStarvedBeastDead)
    IfFlagEnabled(1, 12304802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12304801)
    IfCharacterInsideRegion(1, PLAYER, region=2302801)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2303802)
    IfFlagEnabled(2, 12304808)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.BloodStarvedBeastDead)
    IfFlagEnabled(2, 12304802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12304801)
    IfCharacterInsideRegion(2, PLAYER, region=2302801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2303802)
    WaitFrames(0)
    EnableBossMusic(2303803)


def Event12304804():
    """ 12304804: Event 12304804 """
    DisableNetworkSync()
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12304800)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfFlagEnabled(2, 12304801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=1)


def Event12304805():
    """ 12304805: Event 12304805 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    IfFlagEnabled(0, Flags.BloodStarvedBeastDead)
    DisableBossMusic(2303802)
    DisableBossMusic(2303803)
    DisableBossMusic(-1)


def Event12304807():
    """ 12304807: Event 12304807 """
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    EndIfThisEventFlagEnabled()
    IfHealthLessThan(0, Characters.BloodStarvedBeast, 0.6700000166893005)
    Wait(0.10000000149011612)
    ResetAnimation(Characters.BloodStarvedBeast, disable_interpolation=True)
    ForceAnimation(Characters.BloodStarvedBeast, 7010)
    AICommand(Characters.BloodStarvedBeast, command_id=100, slot=0)
    ReplanAI(Characters.BloodStarvedBeast)
    IfCharacterHasTAEEvent(0, Characters.BloodStarvedBeast, tae_event_id=10)
    AICommand(Characters.BloodStarvedBeast, command_id=-1, slot=0)
    ReplanAI(Characters.BloodStarvedBeast)


def Event12304808():
    """ 12304808: Event 12304808 """
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    EndIfThisEventFlagEnabled()
    IfHealthLessThan(1, Characters.BloodStarvedBeast, 0.33000001311302185)
    IfFlagEnabled(1, 12304807)
    IfConditionTrue(0, input_condition=1)
    Wait(0.10000000149011612)
    ResetAnimation(Characters.BloodStarvedBeast, disable_interpolation=True)
    ForceAnimation(Characters.BloodStarvedBeast, 7011)
    AICommand(Characters.BloodStarvedBeast, command_id=101, slot=0)
    ReplanAI(Characters.BloodStarvedBeast)
    IfCharacterHasTAEEvent(0, Characters.BloodStarvedBeast, tae_event_id=20)
    AICommand(Characters.BloodStarvedBeast, command_id=-1, slot=0)
    ReplanAI(Characters.BloodStarvedBeast)


def DarkbeastPaarlDies():
    """ 12301700: Darkbeast Paarl is killed. """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(2303812)
    DisableSoundEvent(2303813)
    DisableCharacter(Characters.DarkbeastPaarl)
    Kill(Characters.DarkbeastPaarl, award_souls=False)
    DisableObject(2301810)
    DisableObject(2301811)
    DeleteVFX(2303810, erase_root_only=False)
    DeleteVFX(2303811, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, Characters.DarkbeastPaarl)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2301810)
    DisableObject(2301811)
    DeleteVFX(2303810, erase_root_only=True)
    DeleteVFX(2303811, erase_root_only=True)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=0)
    Wait(3.0)
    KillBoss(Characters.DarkbeastPaarl)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(3,))
    AwardAchievement(24)
    SkipLinesIfFlagEnabled(2, 6644)
    AwardItemLot(50800000, host_only=False)
    SkipLines(1)
    AwardItemLot(50800005, host_only=False)
    EnableFlag(2301)
    EnableFlag(9454)
    StopPlayLogMeasurement(2300000)
    StopPlayLogMeasurement(2300001)
    StopPlayLogMeasurement(2300010)
    CreatePlayLog(40)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 120, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 120, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 120, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 120, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayDarkbeastPaarlDeathSound():
    """ 12301701: Event 12301701 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.DarkbeastPaarlDead)
    IfFlagEnabled(1, Flags.DarkbeastPaarlDead)
    IfCharacterBackreadDisabled(2, Characters.DarkbeastPaarl)
    IfHealthLessThanOrEqual(2, Characters.DarkbeastPaarl, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2302810, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def DarkbeastPaarlFirstTime():
    """ 12301702: Event 12301702 """
    EndIfThisEventFlagEnabled()
    EndIfThisEventFlagEnabled()  # just in case, I guess
    EnableInvincibility(Characters.DarkbeastPaarl)
    ForceAnimation(Characters.DarkbeastPaarl, 7000, loop=True)
    IfFlagDisabled(1, Flags.DarkbeastPaarlDead)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, Characters.DarkbeastPaarl, PLAYER, radius=16.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(Characters.DarkbeastPaarl, 7001)
    WaitFrames(70)
    DisableInvincibility(Characters.DarkbeastPaarl)
    EnableFlag(12304700)
    EndIfFlagEnabled(9340)
    RunEvent(9350, 0, args=(1,))
    EnableFlag(9340)


def SummonStartDarkbeastPaarlBattle():
    """ 12301703: Event 12301703 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12304700)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    DisableInvincibility(Characters.DarkbeastPaarl)
    EnableFlag(12304700)
    EnableFlag(Flags.DarkbeastPaarlFirstTimeDone)


def Event12304730():
    """ 12304730: Event 12304730 """
    EndIfFlagEnabled(Flags.DarkbeastPaarlDead)
    GotoIfFlagEnabled(Label.L0, Flags.DarkbeastPaarlFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(2301810)
    DeleteVFX(2303810, erase_root_only=False)
    DisableObject(2301811)
    DeleteVFX(2303811, erase_root_only=False)
    IfFlagDisabled(1, Flags.DarkbeastPaarlDead)
    IfFlagEnabled(1, Flags.DarkbeastPaarlFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2301810)
    EnableObject(2301811)
    CreateVFX(2303810)
    CreateVFX(2303811)

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2300800, entity=2301810)
    IfFlagDisabled(2, Flags.DarkbeastPaarlDead)
    IfFlagEnabled(3, Flags.DarkbeastPaarlDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2302810, animation=101130, wait_for_completion=True)
    SkipLinesIfThisEventFlagEnabled(1)
    RotateToFaceEntity(Characters.DarkbeastPaarl, PLAYER, animation=3008, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2302811)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(12304700)
    Restart()


def Event12304731():
    """ 12304731: Event 12304731 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.DarkbeastPaarlDead)
    IfFlagDisabled(1, Flags.DarkbeastPaarlDead)
    IfFlagEnabled(1, Flags.DarkbeastPaarlFirstTimeDone)
    IfFlagEnabled(1, 12304700)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2300800, entity=2301810)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2302810, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2302811)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12304701)
    Restart()


def Event12304732():
    """ 12304732: Event 12304732 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2301810, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12304733():
    """ 12304733: Event 12304733 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, 2301810, radius=4.0)
    IfEntityWithinDistance(1, PLAYER, 2301810, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def Event12304702():
    """ 12304702: Event 12304702 """
    EndIfFlagEnabled(Flags.DarkbeastPaarlDead)
    DisableAI(Characters.DarkbeastPaarl)
    DisableHealthBar(Characters.DarkbeastPaarl)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 12304700)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.DarkbeastPaarl, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12304700)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.DarkbeastPaarl, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.DarkbeastPaarl)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.DarkbeastPaarl, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.DarkbeastPaarl)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.DarkbeastPaarl)
    EnableBossHealthBar(Characters.DarkbeastPaarl, name=508000, slot=0)
    CreatePlayLog(86)
    StartPlayLogMeasurement(2300010, 102, overwrite=True)


def Event12304703():
    """ 12304703: Event 12304703 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.DarkbeastPaarlDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2303812)
    DisableSoundEvent(2303813)
    IfFlagDisabled(1, Flags.DarkbeastPaarlDead)
    IfFlagEnabled(1, 12304702)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12304701)
    IfCharacterInsideRegion(1, PLAYER, region=2302812)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2303812)
    IfCharacterHasTAEEvent(2, Characters.DarkbeastPaarl, tae_event_id=20)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.DarkbeastPaarlDead)
    IfFlagEnabled(2, 12304702)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12304701)
    IfCharacterInsideRegion(2, PLAYER, region=2302812)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2303812)
    WaitFrames(0)
    EnableBossMusic(2303813)


def Event12304704():
    """ 12304704: Event 12304704 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.DarkbeastPaarlDead)
    IfHealthGreaterThan(1, Characters.DarkbeastPaarl, 0.0)
    IfEntityWithinDistance(1, PLAYER, Characters.DarkbeastPaarl, radius=10.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=1)
    IfHealthGreaterThan(2, Characters.DarkbeastPaarl, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.DarkbeastPaarl, radius=12.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=OLD_YHARNAM, camera_slot=0)
    Restart()


def Event12304705():
    """ 12304705: Event 12304705 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.DarkbeastPaarlDead)
    IfFlagEnabled(0, Flags.DarkbeastPaarlDead)
    DisableBossMusic(2303812)
    DisableBossMusic(2303813)
    DisableBossMusic(-1)


@RestartOnRest
def Event12304707():
    """ 12304707: Event 12304707 """
    EndIfFlagEnabled(Flags.DarkbeastPaarlDead)
    AICommand(Characters.DarkbeastPaarl, command_id=2, slot=1)
    IfHealthLessThan(1, Characters.DarkbeastPaarl, 0.6700000166893005)
    IfCharacterHasSpecialEffect(1, Characters.DarkbeastPaarl, 5402)
    IfConditionTrue(0, input_condition=1)
    Wait(0.10000000149011612)
    AICommand(Characters.DarkbeastPaarl, command_id=100, slot=2)
    ReplanAI(Characters.DarkbeastPaarl)
    IfCharacterHasTAEEvent(0, Characters.DarkbeastPaarl, tae_event_id=20)
    AICommand(Characters.DarkbeastPaarl, command_id=-1, slot=2)
    ReplanAI(Characters.DarkbeastPaarl)
    Wait(0.10000000149011612)
    AICommand(Characters.DarkbeastPaarl, command_id=3, slot=1)


@RestartOnRest
def Event12304715(
    _, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12304715: Event 12304715 """
    EndIfFlagEnabled(Flags.DarkbeastPaarlDead)
    CreateNPCPart(
        Characters.DarkbeastPaarl,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_24_27,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.DarkbeastPaarl, npc_part_id=arg_4_7, material_sfx_id=77, material_vfx_id=77)
    IfCharacterPartHealthLessThanOrEqual(2, Characters.DarkbeastPaarl, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(3, Characters.DarkbeastPaarl, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    ChangeCharacterCloth(Characters.DarkbeastPaarl, 10, state_id=2)
    CreateNPCPart(
        Characters.DarkbeastPaarl,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.DarkbeastPaarl, npc_part_id=arg_4_7, material_sfx_id=77, material_vfx_id=77)
    WaitFrames(1)
    ResetAnimation(Characters.DarkbeastPaarl, disable_interpolation=False)
    ForceAnimation(Characters.DarkbeastPaarl, arg_20_23)
    AddSpecialEffect(Characters.DarkbeastPaarl, arg_12_15, affect_npc_part_hp=True)
    CancelSpecialEffect(Characters.DarkbeastPaarl, arg_16_19)
    ReplanAI(Characters.DarkbeastPaarl)
    Wait(10.0)
    AICommand(Characters.DarkbeastPaarl, command_id=110, slot=0)
    ReplanAI(Characters.DarkbeastPaarl)
    IfCharacterHasTAEEvent(0, Characters.DarkbeastPaarl, tae_event_id=300)
    SetNPCPartHealth(Characters.DarkbeastPaarl, npc_part_id=arg_4_7, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(Characters.DarkbeastPaarl, arg_16_19, affect_npc_part_hp=True)
    CancelSpecialEffect(Characters.DarkbeastPaarl, arg_12_15)
    AICommand(Characters.DarkbeastPaarl, command_id=-1, slot=0)
    ReplanAI(Characters.DarkbeastPaarl)
    ChangeCharacterCloth(Characters.DarkbeastPaarl, 10, state_id=1)
    WaitFrames(10)
    Restart()


@RestartOnRest
def Event12304450(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12304450: Event 12304450 """
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
def Event12304400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12304400: Event 12304400 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagEnabled(1, 72400461)
    IfFlagRangeAnyEnabled(1, (1340, 1341))
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
    IfFlagEnabled(2, 72400461)
    IfFlagRangeAnyEnabled(2, (1340, 1341))
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12304401(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12304401: Event 12304401 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
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
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12304402(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12304402: Event 12304402 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(1, 13501900)
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
    IfCharacterHasSpecialEffect(2, PLAYER, 6142)
    IfFlagEnabled(2, 13501900)
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12304410(
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
    """ 12304410: Event 12304410 """
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
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest
def Event12304460(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12304460: Event 12304460 """
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
def Event12304500():
    """ 12304500: Event 12304500 """
    GotoIfThisEventFlagDisabled(Label.L0)
    SetBackreadStateAlternate(2300740, state=True)
    AddSpecialEffect(2300740, 9006, affect_npc_part_hp=False)
    EnableCharacter(2300740)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2300740)
    DisableAI(2300740)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    SetNetworkUpdateAuthority(2300740, UpdateAuthority.Forced)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12304508)
    IfCharacterInsideRegion(1, PLAYER, region=2302721)
    IfFlagDisabled(1, Flags.BloodStarvedBeastDead)
    IfFlagEnabled(1, 72400461)
    IfFlagRangeAnyEnabled(1, (1340, 1341))
    IfConditionTrue(0, input_condition=1)
    Wait(5.0)
    EnableFlag(12304509)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.f_MenuEffect, sound_id=100000009)
    Wait(5.0)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.f_MenuEffect, sound_id=100000020)
    SetBackreadStateAlternate(2300740, state=True)
    AddSpecialEffect(2300740, 9006, affect_npc_part_hp=False)
    EnableCharacter(2300740)
    ForceAnimation(2300740, 101201, wait_for_completion=True)
    EnableAI(2300740)


@RestartOnRest
def Event12304501():
    """ 12304501: Event 12304501 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 12304502)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2300740)
    SetBackreadStateAlternate(2300740, state=False)


@RestartOnRest
def Event12304502():
    """ 12304502: Event 12304502 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    EndIfFlagEnabled(12304501)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 12304500)
    IfFlagDisabled(1, 12304501)
    IfFlagEnabled(1, Flags.BloodStarvedBeastDead)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2300740, command_id=991, slot=0)
    ReplanAI(2300740)
    Wait(1.0)
    AddSpecialEffect(2300740, 5560, affect_npc_part_hp=False)
    CreateTemporaryVFX(121, anchor_entity=2300740, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(2.0)
    DisableCharacter(2300740)


@RestartOnRest
def Event12304504():
    """ 12304504: Event 12304504 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    EndIfFlagEnabled(12304501)
    EndIfFlagEnabled(12304505)
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(1, Flags.BloodStarvedBeastDead)
    IfFlagEnabled(1, 12304500)
    IfFlagDisabled(1, 12304501)
    IfFlagEnabled(1, Flags.BloodStarvedBeastFirstTimeDone)
    IfFlagEnabled(1, 12304800)
    IfCharacterOutsideRegion(1, 2300740, region=2302801)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetEventPoint(2300740, region=2302722, reaction_range=1.0)
    AICommand(2300740, command_id=990, slot=0)
    ReplanAI(2300740)


@RestartOnRest
def Event12304505():
    """ 12304505: Event 12304505 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(Flags.BloodStarvedBeastDead)
    EndIfFlagEnabled(12304501)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 12304504)
    IfCharacterInsideRegion(1, 2300740, region=2302722)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(2300740, disable_interpolation=False)
    RotateToFaceEntity(2300740, 2302800, animation=101130, wait_for_completion=True)
    AICommand(2300740, command_id=-1, slot=0)
    ReplanAI(2300740)


@RestartOnRest
def Event12304506():
    """ 12304506: Event 12304506 """
    DisableSoapstoneMessage(2303300)
    DeleteVFX(2303400, erase_root_only=False)
    EndIfThisEventFlagEnabled()
    IfPlayerHasGood(1, 200, including_box=False)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, Flags.BloodStarvedBeastDead)
    IfFlagEnabled(1, 72400461)
    IfFlagRangeAnyEnabled(1, (1340, 1341))
    IfConditionTrue(0, input_condition=1)
    EnableSoapstoneMessage(2303300)
    CreateVFX(2303400)
    IfFlagEnabled(-1, 12304509)
    IfFlagEnabled(-1, Flags.BloodStarvedBeastDead)
    IfConditionTrue(0, input_condition=-1)
    DisableSoapstoneMessage(2303300)
    DeleteVFX(2303400, erase_root_only=True)


@RestartOnRest
def Event12304507():
    """ 12304507: Event 12304507 """
    IfCharacterHuman(1, PLAYER)
    IfCharacterHasSpecialEffect(1, PLAYER, 9000)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12304508)
    WaitFrames(1)
    DisableFlag(12304508)
    IfCharacterHuman(2, PLAYER)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 9000)
    IfConditionTrue(0, input_condition=2)
    Restart()


@RestartOnRest
def Event12300100():
    """ 12300100: Event 12300100 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    Move(2300204, destination=2302300, destination_type=CoordEntityType.Region, set_draw_parent=2306000)
    PostDestruction(2301000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(2300204)
    DisableAI(2300204)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302000)
    IfEntityWithinDistance(-2, PLAYER, 2300204, radius=7.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=2300204, attacker=-1)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(2300204, 7015)
    EnableGravity(2300204)
    EnableAI(2300204)
    SetNest(2300204, 2302300)
    ReplanAI(2300204)


def Event12300110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12300110: Event 12300110 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_8_11)
    IfActionButtonParamActivated(1, action_button_id=arg_0_3, entity=arg_4_7)
    IfFlagEnabled(2, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(
        10010161,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(0.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)
    Restart()


def Event12300120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12300120: Event 12300120 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    Wait(0.0)


def Event12300130():
    """ 12300130: Event 12300130 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    CreateObjectVFX(900201, obj=2301500, model_point=200)
    IfActionButtonParamActivated(0, action_button_id=2300000, entity=2301500)
    AwardItemLot(2300170, host_only=False)
    DeleteObjectVFX(2301500, erase_root=True)


@RestartOnRest
def Event12300140():
    """ 12300140: Event 12300140 """
    DeleteVFX(2303002, erase_root_only=True)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterInsideRegion(0, PLAYER, region=2303000)
    DeleteVFX(2303010, erase_root_only=True)
    CreateVFX(2303002)
    Wait(4.0)
    CreateVFX(2303010)


@RestartOnRest
def Event12300160():
    """ 12300160: Event 12300160 """
    GotoIfFlagEnabled(Label.L0, 12300240)
    IfHasAIStatus(-1, 2300605, ai_status=AIStatusType.Battle)
    IfFlagEnabled(-1, 12300240)
    IfFlagEnabled(-1, 12305392)
    IfFlagEnabled(-1, 12305393)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    DisableSoundEvent(2304020)


def Event12300180():
    """ 12300180: Event 12300180 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(2301020, 1)
    DisableObjectActivation(2301020, obj_act_id=2300011)
    NotifyDoorEventSoundDampening(2301020, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(2301020, obj_act_id=2300011)
    IfFlagEnabled(0, 12300190)
    EnableObjectActivation(2301020, obj_act_id=2300011)
    IfObjectActivated(0, obj_act_id=12300214)
    Wait(0.0)


def Event12300190():
    """ 12300190: Event 12300190 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfActionButtonParamActivated(1, action_button_id=2300020, entity=2301020)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    EndIfConditionFalse(2)
    DisplayDialog(
        10010165,
        anchor_entity=2301020,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )


@RestartOnRest
def Event12300201():
    """ 12300201: Event 12300201 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, Flags.BloodStarvedBeastDead)
    EnableFlag(12300200)


@RestartOnRest
def Event12300210():
    """ 12300210: Event 12300210 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DropMandatoryTreasure(2300720)
    DisableBackread(2300720)
    DisableCharacter(2300720)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2300720)
    DisableBackread(2300720)


@RestartOnRest
def Event12300220(_, arg_0_3: int, arg_4_7: int):
    """ 12300220: Event 12300220 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@RestartOnRest
def Event12300230():
    """ 12300230: Event 12300230 """
    IfCharacterInsideRegion(-1, 2300720, region=2302180)
    IfCharacterInsideRegion(-1, 2300720, region=2302181)
    IfCharacterInsideRegion(-1, 2300720, region=2302182)
    IfConditionTrue(0, input_condition=-1)
    AICommand(2300720, command_id=100, slot=0)
    IfCharacterOutsideRegion(1, 2300720, region=2302180)
    IfCharacterOutsideRegion(1, 2300720, region=2302181)
    IfCharacterOutsideRegion(1, 2300720, region=2302182)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300720, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event12300235():
    """ 12300235: Event 12300235 """
    IfCharacterOutsideRegion(0, 2300720, region=2302190)
    AICommand(2300720, command_id=110, slot=0)
    IfCharacterInsideRegion(0, 2300720, region=2302190)
    AICommand(2300720, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event12300240():
    """ 12300240: Event 12300240 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EnableNavmeshType(2303070, NavmeshType.Solid)
    EndOfAnimation(2301322, 1)
    CreateObjectVFX(923240, obj=2301323, model_point=750)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectDestroyed(0, 2301320)
    EnableNavmeshType(2303070, NavmeshType.Solid)
    ForceAnimation(2301322, 1, wait_for_completion=True)
    DisableObject(2301322)
    CreateObjectVFX(923240, obj=2301323, model_point=750)


@RestartOnRest
def Event12300250():
    """ 12300250: Event 12300250 """
    IfFlagEnabled(0, 12300240)
    CreateHazard(
        12300251,
        2301450,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=4.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300252,
        2301451,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300253,
        2301452,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300254,
        2301453,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300255,
        2301454,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.2000000476837158,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300256,
        2301455,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300257,
        2301456,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.800000011920929,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300258,
        2301457,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12300259,
        2301458,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=0.0,
        repetition_time=1.0,
    )


def Event12300300():
    """ 12300300: Event 12300300 """
    GotoIfFlagEnabled(Label.L0, 9802)
    GotoIfFlagEnabled(Label.L0, 9801)
    EnableMapPiece(2306010)
    DisableMapPiece(2306011)
    DisableMapPiece(2304000)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableMapPiece(2306010)
    EnableMapPiece(2306011)
    EnableMapPiece(2304000)
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
    IfFlagChange(-1, 9800)
    IfFlagChange(-1, 9801)
    IfFlagChange(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


def Event12300310(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12300310: Event 12300310 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_8_11)
    EnableTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    WaitFrames(10)
    EnableTreasure(arg_0_3)


@RestartOnRest
def Event12305000():
    """ 12305000: Event 12305000 """
    EndIfFlagEnabled(12305001)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableAI(2300250)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2300250, PLAYER, radius=10.0)
    IfConditionTrue(-2, input_condition=1)
    IfAttackedWithDamageType(-2, attacked_entity=2300250, attacker=-1)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(2300250)
    WaitFrames(1)
    SetNest(2300250, 2302310)
    AICommand(2300250, command_id=10, slot=0)
    ReplanAI(2300250)


@RestartOnRest
def Event12305001():
    """ 12305001: Event 12305001 """
    EndIfThisEventFlagEnabled()
    IfCharacterInsideRegion(0, 2300250, region=2302310)
    ForceAnimation(2300250, 3000)
    AICommand(2300250, command_id=-1, slot=0)
    ReplanAI(2300250)


@RestartOnRest
def Event12305010(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12305010: Event 12305010 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(arg_0_3, arg_12_15)
    StopEvent(12305140, slot=arg_8_11)
    StopEvent(12305160, slot=arg_8_11)
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
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-3)
    IfCharacterInsideRegion(1, PLAYER, region=2302147)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-1, input_condition=1)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-1, arg_0_3, 4670)
    IfConditionTrue(0, input_condition=-1)
    Wait(3.0)
    SetAIParamID(arg_0_3, arg_12_15)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=arg_0_3,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(arg_0_3, arg_4_7)
    StopEvent(12305140, slot=arg_8_11)
    StopEvent(12305160, slot=arg_8_11)


@RestartOnRest
def Event12305020():
    """ 12305020: Event 12305020 """
    DisableAI(2300730)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302020)
    IfCharacterInsideRegion(-2, PLAYER, region=2302021)
    IfConditionTrue(1, input_condition=-2)
    IfFlagDisabled(1, 1325)
    IfCharacterAlive(1, 2300710)
    IfConditionTrue(0, input_condition=1)
    EnableAI(2300730)


@RestartOnRest
def Event12305021():
    """ 12305021: Event 12305021 """
    GotoIfFlagEnabled(Label.L0, 1324)
    IfCharacterDead(-1, 2300710)
    IfFlagEnabled(-1, 1324)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2300730, 7000, loop=True)


@RestartOnRest
def Event12305022():
    """ 12305022: Event 12305022 """
    DisableGravity(2300730)
    DisableCharacterCollision(2300730)


@RestartOnRest
def Event12305023():
    """ 12305023: Event 12305023 """
    IfHasAIStatus(1, 2300710, ai_status=AIStatusType.Battle)
    IfCharacterDead(2, 2300710)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(2300730, 7000, loop=True)
    IfHasAIStatus(3, 2300710, ai_status=AIStatusType.Normal)
    IfCharacterDead(4, 2300710)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(4)
    ForceAnimation(2300730, 7001, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event12305030(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12305030: Event 12305030 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfObjectNotDestroyed(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    SetCharacterEventTarget(2300730, arg_8_11)
    AICommand(2300730, command_id=100, slot=0)
    ReplanAI(2300730)
    IfCharacterHasTAEEvent(0, 2300730, tae_event_id=100)
    AICommand(2300730, command_id=-1, slot=0)
    ReplanAI(2300730)
    Restart()


def Event12305040(_, arg_0_3: int, arg_4_7: int):
    """ 12305040: Event 12305040 """
    EndIfThisEventSlotFlagEnabled()
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=-1, damage_type=DamageType.Fire)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=-1, damage_type=DamageType.NoType)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1, damage_type=DamageType.Magic)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1, damage_type=DamageType.Lightning)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1, damage_type=DamageType.Blunt)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1, damage_type=DamageType.Slash)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1, damage_type=DamageType.Thrust)
    IfConditionTrue(2, input_condition=-2)
    IfObjectHealthValueComparison(2, arg_0_3, ComparisonType.LessThanOrEqual, 999)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ShootProjectile(
        owner_entity=arg_4_7,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6051,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=arg_4_7,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6055,
        launch_angle_x=270,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=arg_4_7,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6071,
        launch_angle_x=0,
        launch_angle_y=90,
        launch_angle_z=0,
    )
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)


@RestartOnRest
def Event12305070():
    """ 12305070: Event 12305070 """
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
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302040)
    IfEntityWithinDistance(-2, PLAYER, 2300601, radius=3.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=2300520, attacker=-1)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(2300601, 7014)
    EnableAI(2300601)
    EnableAnimations(2300601)
    WaitFrames(30)
    EnableGravity(2300601)
    EnableCharacterCollision(2300601)


@RestartOnRest
def Event12305075(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12305075: Event 12305075 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(arg_0_3, arg_12_15)
    StopEvent(12305140, slot=arg_8_11)
    StopEvent(12305160, slot=arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-1, 12305070)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-1, arg_0_3, 4670)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_12_15)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=arg_0_3,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(arg_0_3, arg_4_7)
    StopEvent(12305140, slot=arg_8_11)
    StopEvent(12305160, slot=arg_8_11)


@RestartOnRest
def Event12305080():
    """ 12305080: Event 12305080 """
    EndIfFlagRangeAnyEnabled((12305081, 12305082))
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(-2, PLAYER, region=2302010)
    IfEntityWithinDistance(-2, PLAYER, 2300314, radius=10.0)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(1, input_condition=-2)
    IfFlagRangeAnyEnabled(2, (12305081, 12305082))
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfAttackedWithDamageType(-3, attacked_entity=2300314, attacker=-1)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(2)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(2300314, 2302350)
    AICommand(2300314, command_id=10, slot=0)
    ReplanAI(2300314)


@RestartOnRest
def Event12305081():
    """ 12305081: Event 12305081 """
    EndIfFlagEnabled(12305082)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterInsideRegion(0, 2300314, region=2302050)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2300314, command_id=30, slot=0)
    ReplanAI(2300314)


@RestartOnRest
def Event12305082():
    """ 12305082: Event 12305082 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302011)
    IfEntityWithinDistance(-2, PLAYER, 2300314, radius=3.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300314, command_id=-1, slot=0)
    ReplanAI(2300314)


def Event12305090(_, arg_0_3: int, arg_4_7: int):
    """ 12305090: Event 12305090 """
    EndIfFlagEnabled(12300240)
    IfFlagEnabled(0, 12300240)
    WaitFrames(arg_0_3)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=arg_4_7,
        model_point=101,
        behavior_id=6070,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )


@RestartOnRest
def Event12305100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12305100: Event 12305100 """
    GotoIfFlagEnabled(Label.L0, 12300240)
    IfFlagEnabled(1, 12300240)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(arg_8_11)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 7012, loop=True)


@RestartOnRest
def Event12305110(_, arg_0_3: int, arg_4_7: int):
    """ 12305110: Event 12305110 """
    EndIfFlagEnabled(12300240)
    IfFlagEnabled(1, 12300240)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(arg_4_7)
    Kill(arg_0_3, award_souls=True)


@RestartOnRest
def Event12305120():
    """ 12305120: Event 12305120 """
    IfFlagEnabled(1, 12300240)
    IfHasAIStatus(1, 2300605, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    SetCharacterEventTarget(2300605, 2300921)
    AICommand(2300605, command_id=60, slot=0)
    IfHasAIStatus(0, 2300605, ai_status=AIStatusType.Battle)
    AICommand(2300605, command_id=-1, slot=0)
    Restart()


@RestartOnRest
def Event12305121(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12305121: Event 12305121 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(arg_0_3, arg_12_15)
    StopEvent(12305140, slot=arg_8_11)
    StopEvent(12305160, slot=arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(-1, 2300201, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, 2300202, ai_status=AIStatusType.Battle)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-1, arg_0_3, 4670)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_12_15)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=arg_0_3,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(arg_0_3, arg_4_7)
    StopEvent(12305140, slot=arg_8_11)
    StopEvent(12305160, slot=arg_8_11)


@RestartOnRest
def Event12305125():
    """ 12305125: Event 12305125 """
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(0, 2300201, ai_status=AIStatusType.Battle)
    RotateToFaceEntity(2300201, PLAYER, animation=3008, wait_for_completion=False)


@RestartOnRest
def Event12305130():
    """ 12305130: Event 12305130 """
    EndIfThisEventFlagEnabled()
    DisableGravity(2300203)
    DisableCharacterCollision(2300203)
    DisableAI(2300203)
    ForceAnimation(2300203, 7016, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=2302090)
    IfEntityWithinDistance(-2, PLAYER, 2300203, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttackedWithDamageType(-3, attacked_entity=2300203, attacker=-1)
    IfConditionTrue(0, input_condition=-3)
    ForceAnimation(2300203, 7017)
    EnableGravity(2300203)
    EnableCharacterCollision(2300203)
    EnableAI(2300203)
    ReplanAI(2300203)


@RestartOnRest
def Event12305135(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12305135: Event 12305135 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(arg_0_3, arg_12_15)
    StopEvent(12305140, slot=arg_8_11)
    StopEvent(12305160, slot=arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302148)
    IfConditionTrue(-2, input_condition=1)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 4670)
    IfConditionTrue(0, input_condition=-2)
    SetAIParamID(arg_0_3, arg_12_15)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=arg_0_3,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(arg_0_3, arg_4_7)
    StopEvent(12305140, slot=arg_8_11)
    StopEvent(12305160, slot=arg_8_11)


@RestartOnRest
def Event12305140(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12305140: Event 12305140 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_12_15)
    IfEntityWithinDistance(-1, PLAYER, arg_0_3, radius=2.0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(arg_0_3, arg_16_19)
    ForceAnimation(arg_0_3, arg_8_11, loop=True)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event12305160(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12305160: Event 12305160 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(arg_0_3, arg_12_15)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHasSpecialEffect(-1, arg_0_3, 4670)
    IfConditionTrue(0, input_condition=-1)
    StopEvent(12305140, slot=arg_8_11)
    WaitFrames(1)
    SetAIParamID(arg_0_3, arg_12_15)
    ShootProjectile(
        owner_entity=2300900,
        projectile_id=arg_0_3,
        model_point=90,
        behavior_id=6031,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(arg_0_3, arg_4_7)


@RestartOnRest
def Event12305180(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 12305180: Event 12305180 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfAttacked(-3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)
    Wait(arg_12_15)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12305190(_, arg_0_3: int):
    """ 12305190: Event 12305190 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(1, PLAYER, 404)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    ReplanAI(arg_0_3)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 404)
    ReplanAI(arg_0_3)
    Restart()


@RestartOnRest
def Event12305250():
    """ 12305250: Event 12305250 """
    IfCharacterInsideRegion(0, PLAYER, region=2302070)
    AICommand(2300200, command_id=100, slot=1)
    IfCharacterOutsideRegion(0, PLAYER, region=2302070)
    AICommand(2300200, command_id=-1, slot=1)
    Restart()


@RestartOnRest
def Event12305300(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12305300: Event 12305300 """
    IfCharacterHasTAEEvent(1, arg_0_3, tae_event_id=10)
    IfEntityWithinDistance(1, arg_0_3, arg_4_7, radius=arg_8_11)
    IfCharacterAlive(1, arg_4_7)
    IfCharacterBackreadEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_4_7, command_id=200, slot=1)
    IfCharacterHasTAEEvent(0, arg_4_7, tae_event_id=20)
    AddSpecialEffect(arg_4_7, 5645, affect_npc_part_hp=False)
    AICommand(arg_4_7, command_id=-1, slot=1)
    Restart()


@RestartOnRest
def Event12305440(_, arg_0_3: int, arg_4_7: int):
    """ 12305440: Event 12305440 """
    IfCharacterHasSpecialEffect(0, arg_0_3, 5645)
    AddSpecialEffect(arg_0_3, arg_4_7, affect_npc_part_hp=False)
    IfCharacterDoesNotHaveSpecialEffect(0, arg_0_3, 5645)
    CancelSpecialEffect(arg_0_3, arg_4_7)
    Restart()


@RestartOnRest
def Event12305480():
    """ 12305480: Event 12305480 """
    EndIfFlagEnabled(12305481)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302101)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, 2300406, PLAYER, radius=3.0)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfAttackedWithDamageType(-3, attacked_entity=2300406, attacker=-1)
    IfConditionTrue(0, input_condition=-3)
    EndIfFinishedConditionTrue(2)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(2300406, 2302410)
    AICommand(2300406, command_id=10, slot=0)
    ReplanAI(2300406)


@RestartOnRest
def Event12305481():
    """ 12305481: Event 12305481 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2300406, PLAYER, radius=3.0)
    IfConditionTrue(-2, input_condition=1)
    IfCharacterInsideRegion(-2, 2300406, region=2302410)
    IfAttackedWithDamageType(-2, attacked_entity=2300406, attacker=-1)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2300406, command_id=-1, slot=0)
    ReplanAI(2300406)


@RestartOnRest
def Event12305482():
    """ 12305482: Event 12305482 """
    GotoIfThisEventFlagEnabled(Label.L0)
    SetAIParamID(2300407, 109013)
    IfFlagEnabled(-1, 12305480)
    IfCharacterHasTAEEvent(-1, 2300407, tae_event_id=20)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(2300407, 109010)
    ReplanAI(2300407)


@RestartOnRest
def Event12305490(_, arg_0_3: int, arg_4_7: int):
    """ 12305490: Event 12305490 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=7.0)
    IfConditionTrue(-3, input_condition=1)
    IfCharacterHasTAEEvent(-2, 2300603, tae_event_id=10)
    IfCharacterHasTAEEvent(-2, 2300604, tae_event_id=10)
    IfCharacterHasTAEEvent(-2, 2300605, tae_event_id=10)
    IfConditionTrue(-3, input_condition=-2)
    IfAttackedWithDamageType(-3, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=-3)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, 0)


@RestartOnRest
def Event12305501():
    """ 12305501: Event 12305501 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302130)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300606, command_id=40, slot=0)
    ReplanAI(2300606)
    IfHasAIStatus(0, 2300606, ai_status=AIStatusType.Battle)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2300606, command_id=-1, slot=0)


@RestartOnRest
def Event12305502(_, arg_0_3: int, arg_4_7: int):
    """ 12305502: Event 12305502 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300605, command_id=40, slot=0)
    ReplanAI(2300605)
    IfCharacterHasTAEEvent(0, 2300605, tae_event_id=10)
    AICommand(2300605, command_id=-1, slot=0)
    StopEvent(12305502, slot=arg_4_7)


@RestartOnRest
def Event12305510(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12305510: Event 12305510 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302060)
    IfCharacterHasTAEEvent(1, 2300605, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    SetNest(arg_0_3, arg_4_7)
    SetAIParamID(arg_0_3, arg_12_15)
    Wait(20.0)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_8_11)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event12300700():
    """ 12300700: Event 12300700 """
    GotoIfFlagEnabled(Label.L0, 1320)
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


@RestartOnRest
def Event12300701():
    """ 12300701: Event 12300701 """
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(1323)
    EndIfFlagEnabled(1324)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302710)
    IfFlagEnabled(1, 1320)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(2300710, TeamType.Enemy1)
    DisableFlagRange((1320, 1325))
    EnableFlag(1321)


@RestartOnRest
def Event12300702():
    """ 12300702: Event 12300702 """
    GotoIfFlagDisabled(Label.L0, 1322)
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


@RestartOnRest
def Event12300703():
    """ 12300703: Event 12300703 """
    GotoIfFlagEnabled(Label.L0, 1323)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 1320)
    IfAttackedWithDamageType(1, attacked_entity=2300710, attacker=PLAYER)
    IfConditionTrue(2, input_condition=-1)
    IfFlagEnabled(2, 1325)
    IfAttackedWithDamageType(2, attacked_entity=2300710, attacker=PLAYER)
    IfFlagEnabled(3, 1325)
    IfFlagRangeAnyEnabled(3, (12300710, 12300739))
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


@RestartOnRest
def Event12300704():
    """ 12300704: Event 12300704 """
    GotoIfFlagDisabled(Label.L0, 1324)
    DisableCharacter(2300710)
    DropMandatoryTreasure(2300710)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2300710)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(1)
    DisableFlagRange((1320, 1325))
    EnableFlag(1324)
    EnableFlag(5914)
    SaveRequest()


@RestartOnRest
def Event12300705():
    """ 12300705: Event 12300705 """
    GotoIfFlagDisabled(Label.L0, 1325)
    SetTeamType(2300710, TeamType.FriendlyNPC)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 1320)
    IfFlagEnabled(1, 72300305)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1320, 1325))
    EnableFlag(1325)


@RestartOnRest
def Event12305701():
    """ 12305701: Event 12305701 """
    EndIfThisEventFlagEnabled()
    EndIfFlagEnabled(1324)
    ForceAnimation(2300710, 103041, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
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
    RotateToFaceEntity(2300710, PLAYER, animation=103040, wait_for_completion=False)
    ChangePatrolBehavior(2300710, patrol_information_id=2303060)


@RestartOnRest
def Event12300707():
    """ 12300707: Event 12300707 """
    IfAllPlayersOutsideRegion(1, region=2302500)
    IfFlagEnabled(-1, 1321)
    IfFlagEnabled(-1, 1322)
    IfFlagEnabled(-1, 1323)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SetNest(2300710, 2302320)
    AICommand(2300710, command_id=20, slot=0)
    ReplanAI(2300710)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2302500)
    IfConditionTrue(0, input_condition=1)
    AICommand(2300710, command_id=-1, slot=0)
    ReplanAI(2300710)
    Restart()


@RestartOnRest
def Event12300708():
    """ 12300708: Event 12300708 """
    IfCharacterInsideRegion(0, 2300710, region=2302502)
    AICommand(2300710, command_id=100, slot=1)
    IfCharacterOutsideRegion(0, 2300710, region=2302502)
    AICommand(2300710, command_id=-1, slot=1)
    Restart()


@RestartOnRest
def Event12300710(_, arg_0_3: int):
    """ 12300710: Event 12300710 """
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (12300710, 12300739))
    IfFlagEnabled(1, 1325)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12300709)


@RestartOnRest
def Event12300750():
    """ 12300750: Event 12300750 """
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


@RestartOnRest
def Event12300752():
    """ 12300752: Event 12300752 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    SetNetworkUpdateAuthority(2300710, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2300730, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    SetNetworkUpdateRate(2300730, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(2300710, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest
def Event12300753():
    """ 12300753: Event 12300753 """
    IfInsideMap(0, game_map=OLD_YHARNAM)
    SetDistanceLimitForConversationStateChanges(2300710, distance=130.0)
    IfOutsideMap(0, game_map=OLD_YHARNAM)
    SetDistanceLimitForConversationStateChanges(2300710, distance=17.0)
    Restart()


def Event12300990():
    """ 12300990: Event 12300990 """
    EndIfThisEventFlagEnabled()
    IfPlayerStandingOnCollision(0, 2303500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 154, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 154, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 154, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 154, PlayLogMultiplayerType.HostOnly)


def Event12304020():
    """ 12304020: Event 12304020 """
    IfCharacterInsideRegion(0, PLAYER, region=2302900)
    CreatePlayLog(176)


def Event12304021():
    """ 12304021: Event 12304021 """
    IfCharacterInsideRegion(0, PLAYER, region=2302901)
    CreatePlayLog(202)


def Event12304022():
    """ 12304022: Event 12304022 """
    IfFlagEnabled(1, 12304830)
    IfCharacterHasSpecialEffect(1, PLAYER, 5660)
    IfConditionTrue(0, input_condition=1)
    StopPlayLogMeasurement(2301000)
