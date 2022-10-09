"""FORBIDDEN WOODS

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
from .common_entities import *
from .m27_00_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=35, args=(2700950, 2701950, 999, 12707800))
    RunEvent(7000, slot=36, args=(2700951, 2701951, Flags.ShadowsOfYharnamDead, 12707820))
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
    RunEvent(9280, slot=6, args=(2700710, 12704220, 12704221, 2700, Flags.ShadowsOfYharnamFogEntered, 27, 0), arg_types="iiiiiBB")
    DeleteVFX(2703910, erase_root_only=False)
    DeleteVFX(2703911, erase_root_only=False)
    DeleteVFX(2703912, erase_root_only=False)
    RunEvent(12704400, slot=0, args=(12704440, 2703910, 12704420, 12704430, Flags.ShadowsOfYharnamDead, 6001))
    RunEvent(12704401, slot=0, args=(12704441, 2703911, 12704421, 12704431, Flags.ShadowsOfYharnamDead, 6001))
    RunEvent(12704410, slot=0, args=(5, 2700920, 2702910, 12704420, 12704430, 12704440, Flags.ShadowsOfYharnamDead, 10561))
    RunEvent(12704410, slot=1, args=(5, 2700921, 2702913, 12704421, 12704431, 12704441, Flags.ShadowsOfYharnamDead, 10565))
    RunEvent(12704450, slot=0, args=(2700920, 2702914, 12704420, 12704430, Flags.ShadowsOfYharnamFogEntered))
    RunEvent(12704450, slot=1, args=(2700921, 2702911, 12704421, 12704431, Flags.ShadowsOfYharnamFogEntered))
    RunEvent(12704460, slot=0, args=(2700920, 2702914, 2702800, 2702801, 101130, Flags.ShadowsOfYharnamFogEntered, 2702801))
    RunEvent(12704460, slot=1, args=(2700921, 2702911, 2702800, 2702801, 101130, Flags.ShadowsOfYharnamFogEntered, 2702801))
    RegisterLadder(start_climbing_flag=12700602, stop_climbing_flag=12700603, obj=2701071)
    RegisterLadder(start_climbing_flag=12700604, stop_climbing_flag=12700605, obj=2701072)
    RegisterLadder(start_climbing_flag=12700606, stop_climbing_flag=12700607, obj=2701073)
    CreateHazard(
        12700050,
        2701080,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12700050,
        2701081,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12700050,
        2701082,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12700050,
        2701083,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12700050,
        2701084,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12700050,
        2701085,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12700050,
        2701086,
        model_point=100,
        behavior_param_id=6010,
        target_type=DamageTargetType.Character,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12701100,
        2701300,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12701101,
        2701301,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12701102,
        2701302,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12701103,
        2701303,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12701104,
        2701304,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12701105,
        2701305,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12701106,
        2701306,
        model_point=200,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.699999988079071,
        life=0.0,
        repetition_time=1.0,
    )
    StartPlayLogMeasurement(2700000, 0, overwrite=False)
    StartPlayLogMeasurement(2700001, 18, overwrite=True)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6316)
    EnableFlag(12701999)
    SkipLinesIfFlagEnabled(5, 12701999)
    EnableObject(2701500)
    DisableObject(2701501)
    EnableTreasure(2701500)
    DisableTreasure(2701501)
    SkipLines(4)
    DisableObject(2701500)
    EnableObject(2701501)
    DisableTreasure(2701500)
    EnableTreasure(2701501)
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6317)
    EnableFlag(12701998)
    SkipLinesIfFlagEnabled(5, 12701998)
    EnableObject(2701502)
    DisableObject(2701503)
    EnableTreasure(2701502)
    DisableTreasure(2701503)
    SkipLines(4)
    DisableObject(2701502)
    EnableObject(2701503)
    DisableTreasure(2701502)
    EnableTreasure(2701503)
    IfCharacterHuman(13, PLAYER)
    SkipLinesIfConditionFalse(2, 13)
    SkipLinesIfFlagDisabled(1, 6318)
    EnableFlag(12701997)
    SkipLinesIfFlagEnabled(5, 12701997)
    EnableObject(2701504)
    DisableObject(2701505)
    EnableTreasure(2701504)
    DisableTreasure(2701505)
    SkipLines(4)
    DisableObject(2701504)
    EnableObject(2701505)
    DisableTreasure(2701504)
    EnableTreasure(2701505)
    IfCharacterHuman(12, PLAYER)
    SkipLinesIfConditionFalse(2, 12)
    SkipLinesIfFlagDisabled(1, 6319)
    EnableFlag(12701996)
    SkipLinesIfFlagEnabled(5, 12701996)
    EnableObject(2701506)
    DisableObject(2701507)
    EnableTreasure(2701506)
    DisableTreasure(2701507)
    SkipLines(4)
    DisableObject(2701506)
    EnableObject(2701507)
    DisableTreasure(2701506)
    EnableTreasure(2701507)
    IfCharacterHuman(11, PLAYER)
    SkipLinesIfConditionFalse(2, 11)
    SkipLinesIfFlagDisabled(1, 6320)
    EnableFlag(12701995)
    SkipLinesIfFlagEnabled(5, 12701995)
    EnableObject(2701508)
    DisableObject(2701509)
    EnableTreasure(2701508)
    DisableTreasure(2701509)
    SkipLines(4)
    DisableObject(2701508)
    EnableObject(2701509)
    DisableTreasure(2701508)
    EnableTreasure(2701509)

    # SHADOWS OF YHARNAM
    Event12704842()
    Event12704843()
    ShadowsOfYharnamDie()
    PlayShadowsOfYharnamDeathSound()
    ShadowsOfYharnamFirstTime()
    EnterShadowsOfYharnamFog()
    EnterShadowsOfYharnamFogAsSummon()
    StartShadowsOfYharnamBattle()
    ControlShadowsOfYharnamMusic()
    ControlShadowsOfYharnamCamera()
    StopShadowsOfYharnamMusic()
    ShadowsOfYharnamSnakeSummon()
    SummonStartShadowsOfYharnamBattle()
    SummonGiantSnakeInShadowsBattle(0, Characters.ShadowGiantSnake1, 2705001)
    SummonGiantSnakeInShadowsBattle(1, Characters.ShadowGiantSnake2, 2705002)
    SummonGiantSnakeInShadowsBattle(2, Characters.ShadowGiantSnake3, 2705003)
    ShadowOfYharnamPhaseTwoTrigger(0, Characters.Shadow1, Characters.Shadow2, Characters.Shadow3)
    ShadowOfYharnamPhaseTwoTrigger(1, Characters.Shadow2, Characters.Shadow3, Characters.Shadow1)
    ShadowOfYharnamPhaseTwoTrigger(2, Characters.Shadow3, Characters.Shadow1, Characters.Shadow2)
    ShadowOfYharnamSummonSmallSnake(0, Characters.ShadowSmallSnake1, Characters.Shadow1, 60)
    ShadowOfYharnamSummonSmallSnake(1, Characters.ShadowSmallSnake2, Characters.Shadow1, 61)
    ShadowOfYharnamSummonSmallSnake(3, Characters.ShadowSmallSnake3, Characters.Shadow2, 61)
    ShadowOfYharnamSummonSmallSnake(4, Characters.ShadowSmallSnake4, Characters.Shadow3, 60)
    GiveShadowEffectWhenAttacked(0, Characters.Shadow2, 5536)
    GiveShadowEffectWhenAttacked(1, Characters.Shadow3, 5537)
    DisableShadowGiantSnake(0, Characters.ShadowGiantSnake1, 2705001, 0)
    DisableShadowGiantSnake(1, Characters.ShadowGiantSnake2, 2705002, 1)
    DisableShadowGiantSnake(2, Characters.ShadowGiantSnake3, 2705003, 2)

    RunEvent(12700000, slot=0, args=(2700250, 52700990))
    RunEvent(12700000, slot=1, args=(2700253, 52700980))
    RunEvent(12700000, slot=2, args=(2700256, 52700970))
    RunEvent(12700000, slot=3, args=(2700257, 52700960))
    RunEvent(12700100, slot=0, args=(2700003, 2701010, 12700110))
    RunEvent(12700100, slot=1, args=(2700001, 2701011, 12700111))
    RunEvent(12700100, slot=2, args=(2700001, 2701012, 12700112))
    RunEvent(12700110, slot=0, args=(2701010, 12705720, 1, 2700030))
    RunEvent(12700110, slot=1, args=(2701011, 12705721, 1, 2700010))
    RunEvent(12700110, slot=2, args=(2701012, 12705722, 1, 2700010))
    Event12700130()
    Event12700131()
    Event12700132()
    Event12700133()
    Event12700136()
    Event12700137()
    Event12700140()
    Event12700141()
    Event12700142()
    Event12700143()
    Event12700146()
    Event12700147()
    Event12700150()
    Event12700170()
    Event12700171()
    Event12700172()
    Event12700176()
    Event12700990()
    RunEvent(12700180, slot=0, args=(2700550, 2700600))
    RunEvent(12700180, slot=1, args=(2700552, 2700601))
    RunEvent(12700190, slot=0, args=(2700550, 2700600))
    RunEvent(12700190, slot=1, args=(2700552, 2700601))
    RunEvent(12700200, slot=0, args=(2700550, 2700600))
    RunEvent(12700200, slot=1, args=(2700552, 2700601))
    Event12700700()
    Event12700704()
    Event12700705()
    Event12700701()
    Event12700703()
    Event12700706()
    Event12700707()
    Event12700708()
    Event12700709()
    Event12700722()
    Event12700723()
    Event12705550()
    Event12700702()
    Event12705552()
    Event12700710()
    Event12705175()
    RunEvent(12705000, slot=0, args=(2700655, 2702020, 5.0), arg_types="iif")
    RunEvent(12705000, slot=1, args=(2700103, 2702022, 5.0), arg_types="iif")
    RunEvent(12705000, slot=2, args=(2700104, 2702022, 5.0), arg_types="iif")
    RunEvent(12705000, slot=3, args=(2700653, 2702022, 15.0), arg_types="iif")
    RunEvent(12705000, slot=4, args=(2700110, 2702023, 10.0), arg_types="iif")
    RunEvent(12705000, slot=5, args=(2700111, 2702023, 10.0), arg_types="iif")
    RunEvent(12705000, slot=6, args=(2700651, 2702024, 5.0), arg_types="iif")
    RunEvent(12705000, slot=7, args=(2700320, 2702025, 5.0), arg_types="iif")
    RunEvent(12705000, slot=8, args=(2700321, 2702025, 5.0), arg_types="iif")
    RunEvent(12705000, slot=9, args=(2700513, 2702027, 10.0), arg_types="iif")
    RunEvent(12705000, slot=10, args=(2700500, 2702028, 5.0), arg_types="iif")
    RunEvent(12705000, slot=11, args=(2700700, 2702030, 10.0), arg_types="iif")
    RunEvent(12705000, slot=12, args=(2700435, 2702030, 5.0), arg_types="iif")
    RunEvent(12705000, slot=13, args=(2700401, 2702030, 5.0), arg_types="iif")
    RunEvent(12705000, slot=14, args=(2700352, 2702031, 5.0), arg_types="iif")
    RunEvent(12705000, slot=15, args=(2700904, 2702032, 15.0), arg_types="iif")
    RunEvent(12705000, slot=16, args=(2700915, 2702033, 15.0), arg_types="iif")
    RunEvent(12705000, slot=17, args=(2700450, 2702034, 15.0), arg_types="iif")
    RunEvent(12705000, slot=18, args=(2700451, 2702035, 15.0), arg_types="iif")
    RunEvent(12705000, slot=19, args=(2700555, 2702036, 10.0), arg_types="iif")
    RunEvent(12705000, slot=20, args=(2700131, 2702037, 12.0), arg_types="iif")
    RunEvent(12705000, slot=21, args=(2700652, 2702038, 5.0), arg_types="iif")
    RunEvent(12705000, slot=22, args=(2700134, 2702039, 5.0), arg_types="iif")
    RunEvent(12705000, slot=23, args=(2700100, 2702042, 8.0), arg_types="iif")
    RunEvent(12705000, slot=24, args=(2700146, 2702043, 7.0), arg_types="iif")
    RunEvent(12705000, slot=25, args=(2700660, 2702044, 7.0), arg_types="iif")
    RunEvent(12705000, slot=26, args=(2700659, 2702044, 7.0), arg_types="iif")
    RunEvent(12705000, slot=28, args=(2700440, 2702212, 5.0), arg_types="iif")
    RunEvent(12705000, slot=29, args=(2700441, 2702212, 5.0), arg_types="iif")
    RunEvent(12705000, slot=30, args=(2700113, 2702231, 8.0), arg_types="iif")
    RunEvent(12705000, slot=31, args=(2700611, 2702237, 6.0), arg_types="iif")
    RunEvent(12705000, slot=32, args=(2700620, 2702237, 6.0), arg_types="iif")
    RunEvent(12705000, slot=33, args=(2700616, 2702237, 6.0), arg_types="iif")
    RunEvent(12705000, slot=34, args=(2700618, 2702237, 6.0), arg_types="iif")
    RunEvent(12705000, slot=35, args=(2700625, 2702238, 8.0), arg_types="iif")
    RunEvent(12705000, slot=36, args=(2700621, 2702238, 8.0), arg_types="iif")
    RunEvent(12705000, slot=37, args=(2700613, 2702238, 8.0), arg_types="iif")
    RunEvent(12705000, slot=38, args=(2700614, 2702238, 8.0), arg_types="iif")
    RunEvent(12705000, slot=39, args=(2700615, 2702238, 8.0), arg_types="iif")
    RunEvent(12705000, slot=40, args=(2700751, 2702240, 8.0), arg_types="iif")
    RunEvent(12705000, slot=41, args=(2700752, 2702240, 8.0), arg_types="iif")
    RunEvent(12705000, slot=42, args=(2700705, 2702241, 6.0), arg_types="iif")
    RunEvent(12705000, slot=43, args=(2700515, 2702243, 8.0), arg_types="iif")
    RunEvent(12705090, slot=0, args=(2701000, 12705060, 12705061, 12705062, 2702050, 9.0), arg_types="iiiiif")
    RunEvent(12705090, slot=1, args=(2701001, 12705063, 12705064, 12705065, 2702051, 5.0), arg_types="iiiiif")
    RunEvent(12705070, slot=0, args=(2701000, 2702050, 2701100, 1, 2))
    RunEvent(12705070, slot=1, args=(2701001, 2702051, 2701101, 3, 4))
    RunEvent(12705080, slot=0, args=(12705070, 12705060, 12705061, 12705062))
    RunEvent(12705080, slot=1, args=(12705071, 12705063, 12705064, 12705065))
    RunEvent(12701190, slot=0, args=(2702130, 2701050))
    RunEvent(12701191, slot=0, args=(2702131, 2701051))
    Event12705200()
    Event12705201()
    RunEvent(12705290, slot=0, args=(2700137, 2702142, 2.0, 7012, 7013, 263098, 263052), arg_types="iifiiii")
    RunEvent(12705290, slot=1, args=(2700138, 2702142, 2.0, 7014, 7015, 263098, 263052), arg_types="iifiiii")
    Event12705098()
    Event12705099()
    RunEvent(12705100, slot=0, args=(2700750, 2700751))
    RunEvent(12705100, slot=1, args=(2700750, 2700610))
    RunEvent(12705100, slot=2, args=(2700750, 2700611))
    RunEvent(12705100, slot=3, args=(2700750, 2700612))
    RunEvent(12705100, slot=4, args=(2700750, 2700613))
    RunEvent(12705100, slot=5, args=(2700750, 2700614))
    RunEvent(12705100, slot=6, args=(2700750, 2700615))
    RunEvent(12705100, slot=7, args=(2700750, 2700616))
    RunEvent(12705100, slot=8, args=(2700750, 2700617))
    RunEvent(12705100, slot=9, args=(2700750, 2700618))
    RunEvent(12705100, slot=10, args=(2700750, 2700619))
    RunEvent(12705100, slot=11, args=(2700750, 2700620))
    RunEvent(12705100, slot=12, args=(2700750, 2700621))
    RunEvent(12705100, slot=13, args=(2700750, 2700622))
    RunEvent(12705100, slot=14, args=(2700750, 2700623))
    RunEvent(12705100, slot=15, args=(2700750, 2700624))
    RunEvent(12705100, slot=16, args=(2700750, 2700625))
    RunEvent(12705100, slot=17, args=(2700750, 2700626))
    RunEvent(12705100, slot=18, args=(2700750, 2700627))
    RunEvent(12705100, slot=19, args=(2700750, 2700628))
    RunEvent(12705100, slot=20, args=(2700750, 2700629))
    RunEvent(12705100, slot=21, args=(2700750, 2700630))
    RunEvent(12705300, slot=0, args=(12705095, 2700900, 2701200))
    RunEvent(12705301, slot=0, args=(2700139, 2701200, 5.0, 2702244), arg_types="iifi")
    RunEvent(12705320, slot=0, args=(2700427, 2702161, 0.5, 7000), arg_types="iifi")
    Event12705350()
    Event12705360()
    RunEvent(12705370, slot=0, args=(2700400, 0.0, 2700501, 2700907), arg_types="ifii")
    RunEvent(12705370, slot=1, args=(2700403, 0.30000001192092896, 2700501, 2700908), arg_types="ifii")
    RunEvent(12705370, slot=2, args=(2700406, 0.20000000298023224, 2700501, 2700909), arg_types="ifii")
    RunEvent(12705370, slot=3, args=(2700413, 0.6000000238418579, 2700501, 2700910), arg_types="ifii")
    RunEvent(12705370, slot=4, args=(2700414, 0.30000001192092896, 2700502, 2700916), arg_types="ifii")
    RunEvent(12705370, slot=5, args=(2700415, 1.0, 2700502, 2700917), arg_types="ifii")
    RunEvent(12705370, slot=6, args=(2700424, 0.5, 2700502, 2700918), arg_types="ifii")
    RunEvent(12705370, slot=7, args=(2700431, 0.6000000238418579, 2700502, 2700919), arg_types="ifii")
    Event12705400()
    RunEvent(12705440, slot=0, args=(2700116, 2702230, 5.0, 7004, 7005), arg_types="iifii")
    RunEvent(12705440, slot=1, args=(2700117, 2702231, 5.0, 7005, 7006), arg_types="iifii")
    RunEvent(12705460, slot=0, args=(2700513,))
    RunEvent(12705460, slot=1, args=(2700515,))
    RunEvent(12705480, slot=0, args=(2700301, 3021, 125, 2702250, 4.0), arg_types="iiiif")
    RunEvent(12705480, slot=1, args=(2700302, 3021, 150, 2702251, 10.0), arg_types="iiiif")
    RunEvent(12705480, slot=2, args=(2700303, 3021, 100, 2702252, 10.0), arg_types="iiiif")
    RunEvent(12705480, slot=3, args=(2700308, 3021, 175, 2702253, 10.0), arg_types="iiiif")
    RunEvent(12705480, slot=4, args=(2700309, 3021, 200, 2702254, 10.0), arg_types="iiiif")
    RunEvent(12705480, slot=5, args=(2700310, 3021, 225, 2702255, 10.0), arg_types="iiiif")
    Event12705490()
    Event12705491()
    RunEvent(12705500, slot=0, args=(12705480, 2700301, 0, 2701110))
    RunEvent(12705500, slot=1, args=(12705481, 2700302, 1, 2701112))
    RunEvent(12705500, slot=3, args=(12705483, 2700308, 3, 2701113))
    RunEvent(12705500, slot=4, args=(12705484, 2700309, 4, 2701114))
    RunEvent(12705510, slot=0, args=(2700301, 12705500))
    RunEvent(12705510, slot=1, args=(2700302, 12705501))
    RunEvent(12705510, slot=3, args=(2700308, 12705503))
    RunEvent(12705510, slot=4, args=(2700309, 12705504))
    RunEvent(12705520, slot=0, args=(2700301, 2702046, 2701110, 0))
    RunEvent(12705520, slot=1, args=(2700302, 2702047, 2701112, 1))
    RunEvent(12705530, slot=1, args=(2700308, 2701113))
    RunEvent(12705530, slot=2, args=(2700309, 2701114))
    RunEvent(12705540, slot=0, args=(2700301, 12705500))
    RunEvent(12705540, slot=1, args=(2700302, 12705501))
    RunEvent(12705540, slot=3, args=(2700308, 12705503))
    RunEvent(12705540, slot=4, args=(2700309, 12705504))
    RunEvent(12705600, slot=0, args=(2790, 2790, 8, 7000, 5907, 12705700, 12705760, 2700750), arg_types="hihiiiii")
    RunEvent(12705600, slot=1, args=(2791, 2791, 9, 7022, 5907, 12705700, 12705760, 2700750), arg_types="hihiiiii")
    RunEvent(12705600, slot=2, args=(2792, 2792, 10, 7023, 5907, 12705700, 12705760, 2700750), arg_types="hihiiiii")
    RunEvent(12705600, slot=3, args=(2790, 2790, 8, 7000, 5907, 12705701, 12705761, 2700751), arg_types="hihiiiii")
    RunEvent(12705600, slot=4, args=(2791, 2791, 9, 7022, 5907, 12705701, 12705761, 2700751), arg_types="hihiiiii")
    RunEvent(12705600, slot=5, args=(2792, 2792, 10, 7023, 5907, 12705701, 12705761, 2700751), arg_types="hihiiiii")
    RunEvent(12705630, slot=0, args=(2790, 2790, 8, 40, 12705700, 2700750), arg_types="hihiii")
    RunEvent(12705630, slot=1, args=(2791, 2791, 9, 40, 12705700, 2700750), arg_types="hihiii")
    RunEvent(12705630, slot=2, args=(2792, 2792, 10, 40, 12705700, 2700750), arg_types="hihiii")
    RunEvent(12705630, slot=3, args=(2790, 2790, 8, 40, 12705701, 2700751), arg_types="hihiii")
    RunEvent(12705630, slot=4, args=(2791, 2791, 9, 40, 12705701, 2700751), arg_types="hihiii")
    RunEvent(12705630, slot=5, args=(2792, 2792, 10, 40, 12705701, 2700751), arg_types="hihiii")
    RunEvent(12705660, slot=0, args=(30, 40, 12705760, 2700750, 1, 11), arg_types="iiiiBB")
    RunEvent(12705660, slot=1, args=(50, 40, 12705760, 2700750, 2, 12), arg_types="iiiiBB")
    RunEvent(12705660, slot=2, args=(60, 40, 12705760, 2700750, 3, 13), arg_types="iiiiBB")
    RunEvent(12705660, slot=3, args=(30, 40, 12705761, 2700751, 1, 11), arg_types="iiiiBB")
    RunEvent(12705660, slot=4, args=(50, 40, 12705761, 2700751, 2, 12), arg_types="iiiiBB")
    RunEvent(12705660, slot=5, args=(60, 40, 12705761, 2700751, 3, 13), arg_types="iiiiBB")
    Event12700500()
    RunEvent(1270501)
    Event12701000()
    Event12701001()
    Event12701002()
    RunEvent(12700902, slot=0, args=(2701912,))
    RunEvent(12700903, slot=0, args=(2700912, 1790, 1809, 1799, 1790))
    RunEvent(12700904, slot=0, args=(2700912, 72700320))
    RunEvent(12700905, slot=0, args=(2700912, 72700320, 1790, 1809, 1805))
    RunEvent(12700906, slot=0, args=(72700321, 43120, 6676))
    RunEvent(12700906, slot=1, args=(72700322, 43130, 6678))
    RunEvent(12700908, slot=0, args=(1790, 72700330, 43110))
    Event12700910()
    Event12700909()


def Preconstructor():
    """ 50: Event 50 """
    DisableAnimations(2703950)
    DisableGravity(2703950)
    DisableCharacterCollision(2703950)
    DisableAnimations(2703951)
    DisableGravity(2703951)
    DisableCharacterCollision(2703951)
    Event12700720()
    DisableAI(2700756)
    DisableGravity(2700756)
    RunEvent(12700901, slot=0, args=(2700912, 2701912))
    Event12700175()


def ShadowsOfYharnamDie():
    """ 12701800: Event 12701800 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(Characters.Shadow1)
    DisableCharacter(Characters.Shadow2)
    DisableCharacter(Characters.Shadow3)
    Kill(Characters.Shadow1, award_souls=False)
    Kill(Characters.Shadow2, award_souls=False)
    Kill(Characters.Shadow3, award_souls=False)
    DisableObject(2701800)
    DisableObject(2701801)
    DeleteVFX(2703800, erase_root_only=True)
    DeleteVFX(2703801, erase_root_only=True)
    DeleteVFX(2703805, erase_root_only=True)
    DisableSpawner(2705001)
    DisableSpawner(2705002)
    DisableSpawner(2705003)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, Characters.Shadow1)
    IfCharacterDead(1, Characters.Shadow2)
    IfCharacterDead(1, Characters.Shadow3)
    IfConditionTrue(0, input_condition=1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2701800)
    DisableObject(2701801)
    DeleteVFX(2703800, erase_root_only=True)
    DeleteVFX(2703801, erase_root_only=True)
    DisableSpawner(2705001)
    DisableSpawner(2705002)
    DisableSpawner(2705003)
    Wait(3.0)
    KillBoss(Characters.Shadow1)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(2,))
    AwardAchievement(Achievements.ShadowsOfYharnamDefeated)
    SkipLinesIfFlagEnabled(2, 6321)
    AwardItemLot(2700990, host_only=False)
    SkipLines(1)
    AwardItemLot(2700995, host_only=False)
    EnableFlag(2700)
    EnableFlag(2701)
    EnableFlag(9463)
    StopPlayLogMeasurement(2700000)
    StopPlayLogMeasurement(2700001)
    StopPlayLogMeasurement(2700010)
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


def PlayShadowsOfYharnamDeathSound():
    """ 12701801: TODO: What are these references to 2420800? Ebrietas? Were Shadows originally in UCW?"""
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.ShadowsOfYharnamDead)
    IfFlagEnabled(1, Flags.ShadowsOfYharnamDead)
    IfCharacterBackreadDisabled(2, 2420800)
    IfCharacterBackreadDisabled(2, 2420801)
    IfCharacterBackreadDisabled(2, 2420802)
    IfHealthLessThanOrEqual(2, 2420800, 0.0)
    IfHealthLessThanOrEqual(2, 2420801, 0.0)
    IfHealthLessThanOrEqual(2, 2420802, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2702800, sound_type=SoundType.c_CharacterMotion, sound_id=500099999)


def ShadowsOfYharnamFirstTime():
    """ 12701802: Event 12701802 """
    EndIfFlagEnabled(Flags.ShadowsOfYharnamDead)
    GotoIfThisEventFlagDisabled(Label.L0)
    Move(Characters.Shadow1, destination=2702236, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.Shadow2, destination=2702235, destination_type=CoordEntityType.Region, short_move=True)
    Move(Characters.Shadow3, destination=2702234, destination_type=CoordEntityType.Region, short_move=True)
    DeleteVFX(2703805, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(Characters.Shadow1, 7001, loop=True)
    ForceAnimation(Characters.Shadow2, 7001, loop=True)
    ForceAnimation(Characters.Shadow3, 7001, loop=True)
    IfFlagDisabled(1, Flags.ShadowsOfYharnamDead)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2702805)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(Flags.ShadowsOfYharnamFogEntered)
    ForceAnimation(Characters.Shadow1, 7000)
    ForceAnimation(Characters.Shadow2, 7000)
    ForceAnimation(Characters.Shadow3, 7000)
    DeleteVFX(2703805, erase_root_only=True)


def SummonStartShadowsOfYharnamBattle():
    """ 12701803: Event 12701803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.ShadowsOfYharnamFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    DeleteVFX(2703805, erase_root_only=True)
    EnableFlag(Flags.ShadowsOfYharnamFogEntered)
    EnableFlag(Flags.ShadowsOfYharnamFirstTimeDone)


def EnterShadowsOfYharnamFog():
    """ 12704840: Event 12704840 """
    EndIfFlagEnabled(Flags.ShadowsOfYharnamDead)
    GotoIfFlagEnabled(Label.L0, Flags.ShadowsOfYharnamDead)
    SkipLinesIfClient(2)
    DisableObject(2701800)
    DeleteVFX(2703800, erase_root_only=True)
    IfFlagDisabled(1, Flags.ShadowsOfYharnamDead)
    IfFlagEnabled(1, Flags.ShadowsOfYharnamFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2701800)
    CreateVFX(2703800)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.ShadowsOfYharnamDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2700004, entity=2701800)
    IfFlagEnabled(3, Flags.ShadowsOfYharnamDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2702800, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2702801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.ShadowsOfYharnamFogEntered)
    Restart()


def EnterShadowsOfYharnamFogAsSummon():
    """ 12704841: Event 12704841 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.ShadowsOfYharnamDead)
    IfFlagDisabled(1, Flags.ShadowsOfYharnamDead)
    IfFlagEnabled(1, Flags.ShadowsOfYharnamFirstTimeDone)
    IfFlagEnabled(1, Flags.ShadowsOfYharnamFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2700004, entity=2701800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2702800, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2702801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12704801)
    Restart()


def Event12704842():
    """ 12704842: Event 12704842 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2701800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12704843():
    """ 12704843: Event 12704843 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, 2701800, radius=4.0)
    IfEntityWithinDistance(1, PLAYER, 2701800, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def StartShadowsOfYharnamBattle():
    """ 12704802: Event 12704802 """
    EndIfFlagEnabled(Flags.ShadowsOfYharnamDead)
    DisableAI(Characters.Shadow1)
    DisableAI(Characters.Shadow2)
    DisableAI(Characters.Shadow3)
    DisableHealthBar(Characters.Shadow1)
    DisableHealthBar(Characters.Shadow2)
    DisableHealthBar(Characters.Shadow3)
    DisableSpawner(2705001)
    DisableSpawner(2705002)
    DisableSpawner(2705003)
    DisableAI(Characters.ShadowGiantSnake1)
    DisableAI(Characters.ShadowGiantSnake2)
    DisableAI(Characters.ShadowGiantSnake3)
    DisableCharacter(Characters.ShadowGiantSnake1)
    DisableCharacter(Characters.ShadowGiantSnake2)
    DisableCharacter(Characters.ShadowGiantSnake3)
    EnableInvincibility(Characters.ShadowGiantSnake1)
    EnableInvincibility(Characters.ShadowGiantSnake2)
    EnableInvincibility(Characters.ShadowGiantSnake3)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.ShadowsOfYharnamFogEntered)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.Shadow1, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.Shadow2, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.Shadow3, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(Flags.ShadowsOfYharnamFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.Shadow1, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.Shadow2, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.Shadow3, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Shadow1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Shadow2)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Shadow3)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.Shadow1, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.Shadow2, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.Shadow3, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Shadow1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Shadow2)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Shadow3)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.Shadow1)
    EnableAI(Characters.Shadow2)
    EnableAI(Characters.Shadow3)
    EnableBossHealthBar(Characters.Shadow1, name=212010, slot=2)
    EnableBossHealthBar(Characters.Shadow2, name=212020, slot=1)
    EnableBossHealthBar(Characters.Shadow3, name=212030, slot=0)
    CreatePlayLog(82)
    StartPlayLogMeasurement(2700010, 98, overwrite=True)


def ControlShadowsOfYharnamMusic():
    """ 12704803: Event 12704803 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.ShadowsOfYharnamDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2703802)
    DisableSoundEvent(2703803)
    IfFlagDisabled(1, Flags.ShadowsOfYharnamDead)
    IfFlagEnabled(1, Flags.ShadowsOfYharnamBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12704801)
    IfCharacterInsideRegion(1, PLAYER, region=2702802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2703802)
    IfFlagEnabled(2, 12704808)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.ShadowsOfYharnamDead)
    IfFlagEnabled(2, Flags.ShadowsOfYharnamBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12704801)
    IfCharacterInsideRegion(2, PLAYER, region=2702802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2703802)
    WaitFrames(0)
    EnableBossMusic(2703803)


def ControlShadowsOfYharnamCamera():
    """ 12704804: Event 12704804 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.ShadowsOfYharnamDead)
    IfFlagEnabled(0, Flags.ShadowsOfYharnamBattleStarted)
    SetLockedCameraSlot(game_map=FORBIDDEN_WOODS, camera_slot=1)
    IfFlagEnabled(0, Flags.ShadowsOfYharnamDead)
    SetLockedCameraSlot(game_map=FORBIDDEN_WOODS, camera_slot=0)


def StopShadowsOfYharnamMusic():
    """ 12704805: Event 12704805 """
    DisableNetworkSync()
    GotoIfFlagDisabled(Label.L0, Flags.ShadowsOfYharnamDead)
    DisableSoundEvent(2703802)
    DisableSoundEvent(2703803)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, Flags.ShadowsOfYharnamDead)
    DisableBossMusic(2703802)
    DisableBossMusic(2703803)
    DisableBossMusic(-1)


@RestartOnRest
def ShadowsOfYharnamSnakeSummon():
    """ 12704806: Shadows summon snakes every 10 seconds if two are dead and the third is in phase two, or all three
    have 30% or less health.
    """
    IfCharacterDead(1, Characters.Shadow1)
    IfCharacterDead(1, Characters.Shadow2)
    IfCharacterHasSpecialEffect(1, Characters.Shadow3, 5539)
    IfCharacterDead(2, Characters.Shadow2)
    IfCharacterDead(2, Characters.Shadow3)
    IfCharacterHasSpecialEffect(2, Characters.Shadow1, 5539)
    IfCharacterDead(3, Characters.Shadow3)
    IfCharacterDead(3, Characters.Shadow1)
    IfCharacterHasSpecialEffect(3, Characters.Shadow2, 5536)
    IfHealthLessThanOrEqual(4, Characters.Shadow1, 0.30000001192092896)
    IfHealthLessThanOrEqual(4, Characters.Shadow2, 0.30000001192092896)
    IfHealthLessThanOrEqual(4, Characters.Shadow3, 0.30000001192092896)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    AICommand(Characters.Shadow1, command_id=10, slot=1)
    AICommand(Characters.Shadow2, command_id=10, slot=1)
    AICommand(Characters.Shadow3, command_id=10, slot=1)
    ReplanAI(Characters.Shadow1)
    ReplanAI(Characters.Shadow2)
    ReplanAI(Characters.Shadow3)
    IfCharacterHasTAEEvent(-2, Characters.Shadow1, tae_event_id=40)
    IfCharacterHasTAEEvent(-2, Characters.Shadow2, tae_event_id=40)
    IfCharacterHasTAEEvent(-2, Characters.Shadow3, tae_event_id=40)
    IfConditionTrue(0, input_condition=-2)
    AICommand(Characters.Shadow1, command_id=30, slot=1)
    AICommand(Characters.Shadow2, command_id=30, slot=1)
    AICommand(Characters.Shadow3, command_id=30, slot=1)
    ReplanAI(Characters.Shadow1)
    ReplanAI(Characters.Shadow2)
    ReplanAI(Characters.Shadow3)
    Wait(10.0)
    Restart()


@RestartOnRest
def SummonGiantSnakeInShadowsBattle(_, snake: int, snake_spawner: int):
    """ 12704807: Event 12704807 """
    SkipLinesIfThisEventSlotFlagEnabled(3)
    DisableSpawner(snake_spawner)
    DisableAI(snake)
    DisableCharacter(snake)
    IfCharacterHasTAEEvent(-1, Characters.Shadow1, tae_event_id=20)
    IfCharacterHasTAEEvent(-1, Characters.Shadow2, tae_event_id=20)
    IfCharacterHasTAEEvent(-1, Characters.Shadow3, tae_event_id=20)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacter(snake)
    EnableSpawner(snake_spawner)
    EnableAI(snake)
    ReplanAI(snake)
    IfCharacterHasTAEEvent(1, snake, tae_event_id=10)
    IfTimeElapsed(2, 5.0)
    IfCharacterDoesNotHaveSpecialEffect(2, snake, 5546)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    DisableSpawner(snake_spawner)
    Kill(snake, award_souls=False)
    Restart()


@RestartOnRest
def UnusedShadowsBehavior1():
    """ 12704810: Event 12704810 """
    IfEntityWithinDistance(2, PLAYER, Characters.Shadow1, radius=7.300000190734863)
    IfEntityWithinDistance(2, PLAYER, Characters.Shadow2, radius=7.300000190734863)
    IfEntityWithinDistance(2, PLAYER, Characters.Shadow3, radius=8.800000190734863)
    IfCharacterHasSpecialEffect(2, Characters.Shadow1, 5535)
    IfCharacterHasSpecialEffect(2, Characters.Shadow2, 5535)
    IfConditionTrue(-1, input_condition=2)
    IfEntityWithinDistance(3, PLAYER, Characters.Shadow1, radius=7.300000190734863)
    IfEntityWithinDistance(3, PLAYER, Characters.Shadow2, radius=7.300000190734863)
    IfEntityWithinDistance(3, PLAYER, Characters.Shadow3, radius=8.800000190734863)
    IfCharacterHasSpecialEffect(3, Characters.Shadow2, 5535)
    IfCharacterHasSpecialEffect(3, Characters.Shadow3, 5535)
    IfConditionTrue(-1, input_condition=3)
    IfEntityWithinDistance(4, PLAYER, Characters.Shadow1, radius=7.300000190734863)
    IfEntityWithinDistance(4, PLAYER, Characters.Shadow2, radius=7.300000190734863)
    IfEntityWithinDistance(4, PLAYER, Characters.Shadow3, radius=8.800000190734863)
    IfCharacterHasSpecialEffect(4, Characters.Shadow3, 5535)
    IfCharacterHasSpecialEffect(4, Characters.Shadow1, 5535)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(0, input_condition=-1)
    AICommand(Characters.Shadow1, command_id=50, slot=0)
    AICommand(Characters.Shadow2, command_id=50, slot=0)
    AICommand(Characters.Shadow3, command_id=50, slot=0)
    ReplanAI(Characters.Shadow1)
    ReplanAI(Characters.Shadow2)
    ReplanAI(Characters.Shadow3)
    Wait(2.0)
    AICommand(Characters.Shadow1, command_id=-1, slot=0)
    AICommand(Characters.Shadow2, command_id=-1, slot=0)
    AICommand(Characters.Shadow3, command_id=-1, slot=0)
    ReplanAI(Characters.Shadow1)
    ReplanAI(Characters.Shadow2)
    ReplanAI(Characters.Shadow3)
    Wait(5.0)
    Restart()


@RestartOnRest
def UnusedShadowsBehavior2():
    """ 12704811: Event 12704811 """
    IfEntityWithinDistance(1, PLAYER, Characters.Shadow1, radius=7.300000190734863)
    IfEntityWithinDistance(1, PLAYER, Characters.Shadow2, radius=7.300000190734863)
    IfEntityWithinDistance(1, PLAYER, Characters.Shadow3, radius=8.800000190734863)
    IfCharacterHasSpecialEffect(1, Characters.Shadow1, 5535)
    IfCharacterHasSpecialEffect(1, Characters.Shadow2, 5535)
    IfCharacterHasSpecialEffect(1, Characters.Shadow3, 5535)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.Shadow1, command_id=40, slot=0)
    ReplanAI(Characters.Shadow1)
    Wait(0.20000000298023224)
    AICommand(Characters.Shadow2, command_id=40, slot=0)
    ReplanAI(Characters.Shadow2)
    Wait(0.20000000298023224)
    AICommand(Characters.Shadow3, command_id=40, slot=0)
    ReplanAI(Characters.Shadow3)
    Wait(0.0010000000474974513)
    AICommand(Characters.Shadow1, command_id=-1, slot=0)
    AICommand(Characters.Shadow2, command_id=-1, slot=0)
    AICommand(Characters.Shadow3, command_id=-1, slot=0)
    ReplanAI(Characters.Shadow1)
    ReplanAI(Characters.Shadow2)
    ReplanAI(Characters.Shadow3)
    Restart()


@RestartOnRest
def ShadowOfYharnamPhaseTwoTrigger(_, shadow_to_transform: int, other_shadow_1: int, other_shadow_2: int):
    """ 12704812: Shadow triggers when they all have 50% or less health, or one has 30% or less health. """
    IfHealthLessThanOrEqual(1, shadow_to_transform, 0.5)
    IfHealthLessThanOrEqual(1, other_shadow_1, 0.5)
    IfHealthLessThanOrEqual(1, other_shadow_2, 0.5)
    IfConditionTrue(-1, input_condition=1)
    IfHealthLessThanOrEqual(-1, shadow_to_transform, 0.30000001192092896)
    IfHealthLessThanOrEqual(-1, other_shadow_1, 0.30000001192092896)
    IfHealthLessThanOrEqual(-1, other_shadow_2, 0.30000001192092896)
    IfConditionTrue(0, input_condition=-1)
    AICommand(shadow_to_transform, command_id=50, slot=1)
    ReplanAI(shadow_to_transform)
    IfCharacterHasTAEEvent(0, shadow_to_transform, tae_event_id=50)
    AICommand(shadow_to_transform, command_id=20, slot=1)
    ReplanAI(shadow_to_transform)
    SkipLinesIfValueEqual(1, left=shadow_to_transform, right=Characters.Shadow2)
    AddSpecialEffect(shadow_to_transform, 5539, affect_npc_part_hp=False)
    IfCharacterHasTAEEvent(0, shadow_to_transform, tae_event_id=30)
    AICommand(shadow_to_transform, command_id=40, slot=1)
    ReplanAI(shadow_to_transform)
    IfCharacterHasTAEEvent(2, shadow_to_transform, tae_event_id=10)  # Transformation completed successfully.
    IfTimeElapsed(3, 5.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    End()
    Restart()


@RestartOnRest
def ShadowOfYharnamSummonSmallSnake(_, small_snake: int, shadow: int, model_point: int):
    """ 12704815: Event 12704815 """
    SkipLinesIfThisEventSlotFlagEnabled(4)
    IfCharacterBackreadEnabled(0, small_snake)
    DisableCharacter(small_snake)
    DisableGravity(small_snake)
    IfCharacterHasTAEEvent(0, shadow, tae_event_id=50)
    IfHealthLessThanOrEqual(1, shadow, 0.0)
    SkipLinesIfConditionFalse(1, 1)
    Kill(small_snake, award_souls=False)
    EnableCharacter(small_snake)
    Move(
        small_snake,
        destination=shadow,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        set_draw_parent=shadow,
    )
    SkipLinesIfThisEventSlotFlagEnabled(1)
    ForceAnimation(small_snake, 7000)
    Restart()


@RestartOnRest
def GiveShadowEffectWhenAttacked(_, shadow: int, effect: int):
    """ 12704825: Event 12704825 """
    IfCharacterHasTAEEvent(0, shadow, tae_event_id=40)
    RemoveSpecialEffect(shadow, effect)
    IfFramesElapsed(-1, 70)
    IfAttackedWithDamageType(-1, attacked_entity=shadow, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(shadow, effect, affect_npc_part_hp=False)
    Restart()


@RestartOnRest
def DisableShadowGiantSnake(_, giant_snake: int, spawner: int, event_slot: int):
    """ 12704830: Event 12704830 """
    IfHealthLessThanOrEqual(1, Characters.Shadow1, 0.0)
    IfHealthLessThanOrEqual(1, Characters.Shadow2, 0.0)
    IfHealthLessThanOrEqual(1, Characters.Shadow3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableSpawner(spawner)
    StopEvent(12704807, slot=event_slot)
    IfCharacterHasSpecialEffect(2, giant_snake, 5546)
    GotoIfConditionTrue(Label.L0, input_condition=2)
    Kill(giant_snake, award_souls=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    WaitRandomFrames(min_frames=0, max_frames=25)
    ForceAnimation(giant_snake, 7000, wait_for_completion=True)
    Kill(giant_snake, award_souls=False)


@RestartOnRest
def Event12700000(_, arg_0_3: int, arg_4_7: int):
    """ 12700000: Event 12700000 """
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


def Event12700100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12700100: Event 12700100 """
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
    Wait(1.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Wait(0.0)
    Restart()


def Event12700110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12700110: Event 12700110 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    Wait(0.0)


@RestartOnRest
def Event12700130():
    """ 12700130: Event 12700130 """
    EndIfFlagEnabled(12700135)
    IfFlagEnabled(1, 12700134)
    IfFlagDisabled(2, 12700134)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 1)
    EndOfAnimation(2701032, 0)
    DisableObjectActivation(2701030, obj_act_id=2700000)
    EnableObjectActivation(2701031, obj_act_id=2700000)
    SkipLines(3)
    EndOfAnimation(2701032, 4)
    EnableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)
    SkipLinesIfFlagEnabled(4, 12700137)
    EndOfAnimation(2701032, 4)
    EnableFlag(12700134)
    DisableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)


@RestartOnRest
def Event12700131():
    """ 12700131: Event 12700131 """
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
    WaitFrames(156)
    IfAllPlayersOutsideRegion(0, region=2702001)
    ForceAnimation(2701032, 3)
    WaitFrames(7)
    DisableObjectActivation(2701031, obj_act_id=2700000)
    EnableFlag(12700134)
    DisableFlag(12700135)
    EnableObjectActivation(2701030, obj_act_id=2700000)
    Restart()


@RestartOnRest
def Event12700132():
    """ 12700132: Event 12700132 """
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
    WaitFrames(156)
    IfAllPlayersOutsideRegion(0, region=2702000)
    ForceAnimation(2701032, 7)
    WaitFrames(7)
    DisableObjectActivation(2701030, obj_act_id=2700000)
    DisableFlag(12700134)
    DisableFlag(12700135)
    EnableObjectActivation(2701031, obj_act_id=2700000)
    Restart()


@RestartOnRest
def Event12700133():
    """ 12700133: Event 12700133 """
    DisableNetworkSync()
    IfFlagDisabled(-1, 12700134)
    IfFlagEnabled(-1, 12700135)
    IfFlagDisabled(-1, 12700137)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2701030)
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
def Event12700136():
    """ 12700136: Event 12700136 """
    DisableNetworkSync()
    IfFlagEnabled(-1, 12700134)
    IfFlagEnabled(-1, 12700135)
    IfFlagDisabled(-1, 12700137)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2701031)
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
def Event12700137():
    """ 12700137: Event 12700137 """
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)
    IfCharacterInsideRegion(0, PLAYER, region=2702002)
    CreatePlayLog(116)
    EnableObjectActivation(2701030, obj_act_id=2700000)
    DisableObjectActivation(2701031, obj_act_id=2700000)


def Event12700140():
    """ 12700140: Event 12700140 """
    IfFlagEnabled(1, 12700144)
    IfFlagDisabled(2, 12700144)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(4, 1)
    EndOfAnimation(2701042, 0)
    DisableObjectActivation(2701040, obj_act_id=2700000)
    EnableObjectActivation(2701041, obj_act_id=2700000)
    SkipLines(3)
    EndOfAnimation(2701042, 10)
    EnableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)
    SkipLinesIfFlagEnabled(4, 12700147)
    EndOfAnimation(2701042, 10)
    EnableFlag(12700144)
    DisableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)


def Event12700141():
    """ 12700141: Event 12700141 """
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
    WaitFrames(257)
    IfAllPlayersOutsideRegion(0, region=2702011)
    ForceAnimation(2701042, 9)
    WaitFrames(7)
    DisableObjectActivation(2701041, obj_act_id=2700000)
    EnableFlag(12700144)
    DisableFlag(12700145)
    EnableObjectActivation(2701040, obj_act_id=2700000)
    Restart()


def Event12700142():
    """ 12700142: Event 12700142 """
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
    WaitFrames(257)
    IfAllPlayersOutsideRegion(0, region=2702010)
    ForceAnimation(2701042, 7)
    WaitFrames(7)
    DisableObjectActivation(2701040, obj_act_id=2700000)
    DisableFlag(12700144)
    DisableFlag(12700145)
    EnableObjectActivation(2701041, obj_act_id=2700000)
    Restart()


def Event12700143():
    """ 12700143: Event 12700143 """
    DisableNetworkSync()
    IfFlagDisabled(-1, 12700144)
    IfFlagEnabled(-1, 12700145)
    IfFlagDisabled(-1, 12700147)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2701040)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12700146():
    """ 12700146: Event 12700146 """
    DisableNetworkSync()
    IfFlagEnabled(-1, 12700144)
    IfFlagEnabled(-1, 12700145)
    IfFlagDisabled(-1, 12700147)
    IfConditionTrue(1, input_condition=-1)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2701041)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12700147():
    """ 12700147: Event 12700147 """
    EndIfThisEventSlotFlagEnabled()
    DisableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)
    IfCharacterInsideRegion(0, PLAYER, region=2702012)
    CreatePlayLog(116)
    EnableObjectActivation(2701040, obj_act_id=2700000)
    DisableObjectActivation(2701041, obj_act_id=2700000)


def Event12700150():
    """ 12700150: Event 12700150 """
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(2701150, 0)
    DisableObjectActivation(2701150, obj_act_id=9942)
    EnableTreasure(2701150)
    End()
    IfObjectActivated(0, obj_act_id=12700900)
    WaitFrames(10)
    EnableTreasure(2701150)


@RestartOnRest
def Event12700170():
    """ 12700170: Event 12700170 """
    DisableFlag(0)
    IfFlagDisabled(1, 12700175)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfFlagEnabled(2, 12700173)
    GotoIfConditionTrue(Label.L1, input_condition=2)

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(2701013, 3)
    DisableFlag(12700173)
    DisableNavmeshType(2703050, NavmeshType.Solid)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    EndOfAnimation(2701013, 0)
    EnableFlag(12700173)
    EnableNavmeshType(2703050, NavmeshType.Solid)

    # --- 2 --- #
    DefineLabel(2)


@RestartOnRest
def Event12700171():
    """ 12700171: Event 12700171 """
    IfFlagEnabled(1, 12700173)
    IfFlagDisabled(1, 12700174)
    IfObjectActivated(1, obj_act_id=12700010)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12700173)
    EnableFlag(12700174)
    ForceAnimation(2701013, 1)
    WaitFrames(100)
    DisableFlag(12700174)
    EnableObjectActivation(2701090, obj_act_id=2700000)
    DisableNavmeshType(2703050, NavmeshType.Solid)
    Restart()


@RestartOnRest
def Event12700172():
    """ 12700172: Event 12700172 """
    IfFlagDisabled(1, 12700173)
    IfFlagDisabled(1, 12700174)
    IfObjectActivated(1, obj_act_id=12700010)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12700173)
    EnableFlag(12700174)
    ForceAnimation(2701013, 2)
    EnableNavmeshType(2703050, NavmeshType.Solid)
    WaitFrames(100)
    DisableFlag(12700174)
    EnableObjectActivation(2701090, obj_act_id=2700000)
    Restart()


@RestartOnRest
def Event12700175():
    """ 12700175: Event 12700175 """
    GotoIfThisEventFlagDisabled(Label.L0)
    Kill(2700145, award_souls=False)
    DisableCharacter(2700145)
    DisableBackread(2700145)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2700145)
    WaitFrames(1)


@RestartOnRest
def Event12700176():
    """ 12700176: Event 12700176 """
    DisableNetworkSync()
    IfFlagEnabled(1, 12700174)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=2701090)
    IfConditionTrue(0, input_condition=1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12700180(_, arg_0_3: int, arg_4_7: int):
    """ 12700180: Event 12700180 """
    DisableNetworkSync()
    IfCharacterAlive(1, arg_0_3)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    Move(arg_4_7, destination=arg_0_3, destination_type=CoordEntityType.Character, model_point=40, short_move=True)
    Restart()


@RestartOnRest
def Event12700190(_, arg_0_3: int, arg_4_7: int):
    """ 12700190: Event 12700190 """
    IfHealthLessThanOrEqual(0, arg_0_3, 0.0)
    Wait(1.0)
    ForceAnimation(arg_4_7, 2200, wait_for_completion=True)
    DisableCharacter(arg_4_7)


def Event12700200(_, arg_0_3: int, arg_4_7: int):
    """ 12700200: Event 12700200 """
    AddSpecialEffect(arg_0_3, 5609, affect_npc_part_hp=False)
    DisableGravity(arg_4_7)


@RestartOnRest
def Event12700500():
    """ 12700500: Event 12700500 """
    IfCharacterHuman(2, PLAYER)
    EndIfConditionFalse(2)
    IfCharacterAlive(1, 2700680)
    IfAttacked(1, PLAYER, attacker=2700680)
    IfHealthEqual(1, PLAYER, 0.0)
    IfFlagEnabled(1, 9401)
    IfFlagEnabled(1, 9404)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9420)


@RestartOnRest
def Event1270501():
    """ 1270501: Event 1270501 """
    GotoIfFlagEnabled(Label.L0, 9802)
    EndIfFlagEnabled(9453)

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2700680)


def Event12700700():
    """ 12700700: Event 12700700 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=15)
    DisableFlag(72700440)
    DisableFlag(72700445)
    DisableFlag(72700361)
    DisableFlag(72700364)

    # --- 9 --- #
    DefineLabel(9)
    ForceAnimation(2700756, 7002)
    GotoIfFlagEnabled(Label.L1, 1200)
    GotoIfFlagEnabled(Label.L2, 1201)
    GotoIfFlagEnabled(Label.L2, 1202)
    GotoIfFlagEnabled(Label.L3, 1203)
    GotoIfFlagEnabled(Label.L4, 1208)
    GotoIfFlagEnabled(Label.L4, 1209)
    DisableBackread(2700755)
    DisableBackread(2700756)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(2700755)
    EnableBackread(2700756)
    GotoIfFlagEnabled(Label.L5, 12705552)
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


def Event12700701():
    """ 12700701: Event 12700701 """
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


def Event12700702():
    """ 12700702: Event 12700702 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 1205)
    DisableBackread(2700755)
    DisableBackread(2700756)


def Event12700703():
    """ 12700703: Event 12700703 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthLessThan(1, 2700755, 0.5)
    IfHealthNotEqual(1, 2700755, 0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12705551)


def Event12700704():
    """ 12700704: Event 12700704 """
    IfFlagEnabled(0, 72700451)
    DisableFlag(72700451)
    DisableFlagRange((1200, 1219))
    EnableFlag(1209)


def Event12700705():
    """ 12700705: Event 12700705 """
    IfFlagEnabled(0, 72700450)
    DisableFlag(72700450)
    DisableFlagRange((1200, 1219))
    EnableFlag(1208)


def Event12700706():
    """ 12700706: Event 12700706 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, 2700755, 0.0)
    IfCharacterHasSpecialEffect(1, 2700755, 151)
    IfFlagEnabled(-1, 1200)
    IfFlagEnabled(-1, 1204)
    IfFlagEnabled(-1, 1205)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2700755, 103132)


def Event12700707():
    """ 12700707: Event 12700707 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2700755, attacker=-1)
    IfHealthGreaterThanOrEqual(1, 2700755, 0.5)
    IfHealthNotEqual(1, 2700755, 0.0)
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


def Event12700708():
    """ 12700708: Event 12700708 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2700755, 154)
    IfConditionTrue(1, input_condition=-1)
    IfHealthGreaterThanOrEqual(1, 2700755, 0.5)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2700755, 103072)
    Restart()


def Event12700709():
    """ 12700709: Event 12700709 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, 2700755, 152)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2700755, 103072)
    Restart()


def Event12700710():
    """ 12700710: Event 12700710 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2702300)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9467)
    Wait(0.0)


def Event12700720():
    """ 12700720: Event 12700720 """
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


def Event12700722():
    """ 12700722: Event 12700722 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(30)
    IfFlagEnabled(1, 1202)
    IfAttackedWithDamageType(-1, attacked_entity=2700755, attacker=PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=2702301)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, 2700755, 0.0)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12705551)


def Event12700723():
    """ 12700723: Event 12700723 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2700755, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    IfAttackedWithDamageType(2, attacked_entity=2700755, attacker=PLAYER)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(1)
    IfAttackedWithDamageType(3, attacked_entity=2700755, attacker=PLAYER)
    IfHealthNotEqual(3, 2700755, 0.0)
    IfConditionTrue(0, input_condition=3)
    EnableFlag(12705551)


def Event12700901(_, arg_0_3: int, arg_4_7: int):
    """ 12700901: Event 12700901 """
    IfCharacterHuman(-1, PLAYER)
    GotoIfConditionFalse(Label.L9, input_condition=-1)
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1790, 1809))
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
    DisableObject(arg_4_7)
    GotoIfFlagEnabled(Label.L0, 1800)
    GotoIfFlagEnabled(Label.L0, 1801)
    GotoIfFlagEnabled(Label.L1, 1805)
    GotoIfFlagEnabled(Label.L2, 1790)
    GotoIfFlagEnabled(Label.L3, 1791)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(arg_0_3, TeamType.Ally)
    ForceAnimation(arg_0_3, 103140)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    EnableObject(arg_4_7)
    EnableObjectInvulnerability(arg_4_7)
    CreateObjectVFX(900201, obj=arg_4_7, model_point=200)
    End()

    # --- 4 --- #
    DefineLabel(4)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()


def Event12700902(_, arg_0_3: int):
    """ 12700902: Event 12700902 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    EndIfFlagEnabled(12700902)
    IfFlagEnabled(1, 1791)
    IfActionButtonParamActivated(1, action_button_id=2700005, entity=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(43100, host_only=False)
    EnableFlag(6813)
    DisableObject(arg_0_3)
    DeleteObjectVFX(arg_0_3, erase_root=True)


def Event12700903(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12700903: Event 12700903 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled((arg_4_7, arg_12_15))
    IfCharacterDead(1, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_16_19)
    SaveRequest()


def Event12700904(_, arg_0_3: int, arg_4_7: int):
    """ 12700904: Event 12700904 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    EnableFlag(arg_4_7)


def Event12700905(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12700905: Event 12700905 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(arg_4_7)
    IfFlagEnabled(-1, arg_4_7)
    IfHealthLessThanOrEqual(-1, arg_0_3, 0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    DisableFlagRange((arg_8_11, arg_12_15))
    EnableFlag(arg_16_19)
    SaveRequest()


def Event12700906(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12700906: Event 12700906 """
    EndIfFlagEnabled(arg_8_11)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)


def Event12700910():
    """ 12700910: Event 12700910 """
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


def Event12700908(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12700908: Event 12700908 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagDisabled(Label.L0, arg_0_3)
    GotoIfFlagDisabled(Label.L1, arg_4_7)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, arg_4_7)
    AwardItemLot(arg_8_11, host_only=False)
    SaveRequest()


def Event12700909():
    """ 12700909: Event 12700909 """
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


def Event12701000():
    """ 12701000: Event 12701000 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 1367)
    IfFlagEnabled(1, 12700710)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1373)


def Event12701001():
    """ 12701001: Event 12701001 """
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


def Event12701002():
    """ 12701002: Event 12701002 """
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


@RestartOnRest
def Event12705000(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12705000: Event 12705000 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AICommand(arg_0_3, command_id=30, slot=0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(2, input_condition=-1)
    IfAttacked(3, arg_0_3, attacker=PLAYER)
    IfConditionTrue(3, input_condition=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12705098():
    """ 12705098: Event 12705098 """
    ForceAnimation(0, 7010)
    SetAIParamID(0, 73420)


@RestartOnRest
def Event12705099():
    """ 12705099: Event 12705099 """
    IfThisEventFlagEnabled(0)
    ForceAnimation(2700750, 7012)
    SetAIParamID(2700750, 273400)
    ReplanAI(2700750)


@RestartOnRest
def Event12705100(_, arg_0_3: int, arg_4_7: int):
    """ 12705100: Event 12705100 """
    ForceAnimation(arg_0_3, 7010, loop=True)
    SetAIParamID(arg_0_3, 273420)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfCharacterInsideRegion(-2, arg_4_7, region=2709093)
    IfCharacterInsideRegion(-2, PLAYER, region=2709093)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(1, attacked_entity=arg_4_7, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12705099)


@RestartOnRest
def Event12705070(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12705070: Event 12705070 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, 0, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_8_11, 1, wait_for_completion=True)
    ForceAnimation(arg_0_3, arg_12_15, wait_for_completion=True)
    ForceAnimation(arg_0_3, arg_16_19, loop=True)
    WaitFrames(1)


@RestartOnRest
def Event12705080(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12705080: Event 12705080 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(0, arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    RemoveObjectFlag(arg_4_7)
    RemoveObjectFlag(arg_8_11)
    RemoveObjectFlag(arg_12_15)


@RestartOnRest
def Event12705090(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: float):
    """ 12705090: Event 12705090 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_16_19)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    WaitFrames(0)
    CreateHazard(
        arg_4_7,
        arg_0_3,
        model_point=101,
        behavior_param_id=6100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=arg_20_23,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_8_11,
        arg_0_3,
        model_point=102,
        behavior_param_id=6100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=arg_20_23,
        repetition_time=0.0,
    )
    CreateHazard(
        arg_12_15,
        arg_0_3,
        model_point=103,
        behavior_param_id=6100,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=arg_20_23,
        repetition_time=0.0,
    )


@RestartOnRest
def Event12705175():
    """ 12705175: Event 12705175 """
    IfCharacterBackreadEnabled(0, 2700118)
    ForceAnimation(2700118, 7010, loop=True)
    DisableAnimations(2700118)
    DisableGravity(2700118)


@RestartOnRest
def Event12701190(_, arg_0_3: int, arg_4_7: int):
    """ 12701190: Event 12701190 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    PostDestruction(arg_4_7)
    RegisterLadder(start_climbing_flag=12700600, stop_climbing_flag=12700601, obj=2701070)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    DestroyObject(arg_4_7)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=997400000)
    RegisterLadder(start_climbing_flag=12700600, stop_climbing_flag=12700601, obj=2701070)


@RestartOnRest
def Event12701191(_, arg_0_3: int, arg_4_7: int):
    """ 12701191: Event 12701191 """
    SkipLinesIfThisEventSlotFlagDisabled(2)
    PostDestruction(arg_4_7)
    End()
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    DestroyObject(arg_4_7)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=SoundType.o_Object, sound_id=997400000)


@RestartOnRest
def Event12705200():
    """ 12705200: Event 12705200 """
    ForceAnimation(2700135, 7010)
    SetAIParamID(2700135, 263098)
    IfHasAIStatus(-1, 2700135, ai_status=AIStatusType.Search)
    IfEntityWithinDistance(-1, PLAYER, 2700135, radius=2.5)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(2700135, 263097)
    ForceAnimation(2700135, 7016)
    IfHasAIStatus(0, 2700135, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event12705201():
    """ 12705201: Event 12705201 """
    GotoIfThisEventFlagDisabled(Label.L0)
    SetAIParamID(2700135, 263050)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(-1, 2700135, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2700135, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(-1, attacked_entity=2700135, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    StopEvent(12705200)
    WaitFrames(1)
    SetAIParamID(2700135, 263050)
    ForceAnimation(2700135, 7011)


@RestartOnRest
def Event12705290(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12705290: Event 12705290 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, arg_12_15, loop=True)
    SetAIParamID(arg_0_3, arg_20_23)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(2, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(arg_0_3, arg_16_19, wait_for_completion=True)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_24_27)
    ReplanAI(arg_0_3)


def Event12705300(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12705300: Event 12705300 """
    IfObjectActivated(0, obj_act_id=arg_0_3)
    Wait(2.299999952316284)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    AddSpecialEffect(arg_4_7, 5580, affect_npc_part_hp=False)
    ForceAnimation(arg_8_11, 1)
    Wait(1.0)
    RemoveSpecialEffect(arg_4_7, 5580)
    WaitFrames(30)
    EnableObjectActivation(arg_8_11, obj_act_id=9800)
    Restart()


def Event12705301(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 12705301: Event 12705301 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, arg_0_3, arg_4_7, radius=arg_8_11)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-2)
    IfCharacterInsideRegion(-3, PLAYER, region=arg_12_15)
    IfConditionTrue(2, input_condition=-3)
    IfConditionTrue(3, input_condition=1)
    IfConditionTrue(3, input_condition=2)
    IfConditionFalse(4, input_condition=3)
    IfConditionTrue(-4, input_condition=3)
    IfConditionTrue(-4, input_condition=4)
    IfConditionTrue(0, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=4)
    ActivateObjectWithSpecificCharacter(arg_4_7, objact_id=9800, relative_index=-1, character=arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event12705320(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 12705320: Event 12705320 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableGravity(arg_0_3)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, arg_12_15, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(-2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    Wait(arg_8_11)
    ForceAnimation(arg_0_3, -1)

    # --- 0 --- #
    DefineLabel(0)
    EnableGravity(arg_0_3)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12705350():
    """ 12705350: Event 12705350 """
    IfCharacterInsideRegion(0, 2700352, region=2702180)
    Wait(10.0)
    ChangePatrolBehavior(2700352, patrol_information_id=2703011)
    IfCharacterInsideRegion(0, 2700352, region=2702181)
    Wait(10.0)
    ChangePatrolBehavior(2700352, patrol_information_id=2703010)
    Restart()


@RestartOnRest
def Event12705360():
    """ 12705360: Event 12705360 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2702190)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    SetNest(2700514, 2702190)
    AICommand(2700514, command_id=10, slot=0)
    ReplanAI(2700514)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-3)
    IfEntityWithinDistance(1, 2700514, PLAYER, radius=7.0)
    IfConditionTrue(-1, input_condition=1)
    IfCharacterInsideRegion(-1, 2700514, region=2702190)
    IfAttackedWithDamageType(-1, attacked_entity=2700514, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    RotateToFaceEntity(2700514, PLAYER, animation=3008, wait_for_completion=False)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2700514, command_id=-1, slot=0)
    ReplanAI(2700514)


@RestartOnRest
def Event12705370(_, arg_0_3: int, arg_4_7: float, arg_8_11: int, arg_12_15: int):
    """ 12705370: Event 12705370 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EnableAI(arg_0_3)
    EnableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    DisableCharacter(arg_0_3)
    IfHasAIStatus(-1, arg_8_11, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_8_11, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_8_11, 3014)
    Wait(arg_4_7)
    Move(
        arg_0_3,
        destination=arg_12_15,
        destination_type=CoordEntityType.Character,
        model_point=21,
        copy_draw_parent=arg_12_15,
    )
    WaitFrames(75)
    ForceAnimation(arg_0_3, 6200)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 6200)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12705400():
    """ 12705400: Event 12705400 """
    IfAllPlayersOutsideRegion(1, region=2702200)
    IfCharacterInsideRegion(1, 2700450, region=2702200)
    IfHasAIStatus(1, 2700450, ai_status=AIStatusType.Normal)
    IfConditionTrue(0, input_condition=1)
    SetAIParamID(2700450, 127501)
    IfCharacterInsideRegion(0, PLAYER, region=2702200)
    SetAIParamID(2700450, 127500)
    Restart()


@RestartOnRest
def Event12705440(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: int):
    """ 12705440: Event 12705440 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, arg_12_15, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(2, input_condition=-1)
    IfAttackedWithDamageType(3, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(3)
    ForceAnimation(arg_0_3, arg_16_19)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12705460(_, arg_0_3: int):
    """ 12705460: Event 12705460 """
    SetCollisionMask(arg_0_3, bit_index=6, switch_type=OnOffChange.Off)
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=10)
    SetCollisionMask(arg_0_3, bit_index=6, switch_type=OnOffChange.On)


@RestartOnRest
def Event12705480(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """ 12705480: Event 12705480 """
    SkipLinesIfThisEventSlotFlagEnabled(1)
    ForceAnimation(arg_0_3, 7000, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_16_19)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfHealthValueLessThan(0, arg_0_3, 0)
    ForceAnimation(arg_0_3, 7001, wait_for_completion=True)
    WaitFrames(60)
    IfHealthValueLessThan(0, arg_0_3, 0)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    WaitFrames(arg_8_11)
    Restart()


@RestartOnRest
def Event12705490():
    """ 12705490: Event 12705490 """
    EndIfFlagEnabled(12700175)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2702040)
    IfCharacterInsideRegion(1, 2700145, region=2702045)
    IfHealthGreaterThan(1, 2700145, 0.0)
    IfFlagDisabled(1, 12700173)
    IfFlagDisabled(1, 12700174)
    IfFlagEnabled(2, 12700175)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EndIfFinishedConditionTrue(2)
    StopEvent(12705491)
    RotateToFaceEntity(2700145, 2701090, animation=7100, wait_for_completion=False)
    ForceAnimation(2701090, 1)
    WaitFrames(55)
    EnableNavmeshType(2703050, NavmeshType.Solid)
    ForceAnimation(2701013, 2)
    EnableFlag(12700173)
    EnableFlag(12700174)
    WaitFrames(55)
    EnableFlag(12705495)
    RotateToFaceEntity(2700145, PLAYER, animation=3009, wait_for_completion=False)
    WaitFrames(45)
    DisableFlag(12700174)


@RestartOnRest
def Event12705491():
    """ 12705491: Event 12705491 """
    EndIfFlagEnabled(12700175)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 12700173)
    IfFlagDisabled(1, 12700174)
    IfCharacterInsideRegion(1, PLAYER, region=2702040)
    IfCharacterInsideRegion(1, 2700145, region=2702045)
    IfHealthGreaterThan(1, 2700145, 0.0)
    IfFlagEnabled(2, 12700175)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    EndIfFinishedConditionTrue(2)
    StopEvent(12705490)
    ForceAnimation(2700145, 3009)
    EnableFlag(12705495)


@RestartOnRest
def Event12705500(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12705500: Event 12705500 """
    EndIfFlagEnabled(12700175)
    EndIfFlagEnabled(12705495)
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(arg_4_7)
    IfFlagEnabled(0, 12705495)

    # --- 0 --- #
    DefineLabel(0)
    StopEvent(12705480, slot=arg_8_11)
    GotoIfFlagEnabled(Label.L1, arg_0_3)
    ForceAnimation(arg_4_7, 7001, wait_for_completion=True)
    WaitFrames(60)

    # --- 1 --- #
    DefineLabel(1)
    StopEvent(12705480, slot=arg_8_11)
    ForceAnimation(arg_12_15, 1)
    ForceAnimation(arg_4_7, 3014)
    WaitFrames(17)
    DisableInvincibility(arg_4_7)
    EnableGravity(arg_4_7)
    EnableCharacterCollision(arg_4_7)
    EnableAI(arg_4_7)
    SetNest(arg_4_7, 2702041)
    AICommand(arg_4_7, command_id=10, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event12705510(_, arg_0_3: int, arg_4_7: int):
    """ 12705510: Event 12705510 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=5.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(-1, input_condition=1)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfCharacterInsideRegion(-1, arg_0_3, region=2702041)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12705520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12705520: Event 12705520 """
    EndIfFlagDisabled(12700175)
    StopEvent(12705480, slot=arg_12_15)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    EndOfAnimation(arg_8_11, 1)


@RestartOnRest
def Event12705530(_, arg_0_3: int, arg_4_7: int):
    """ 12705530: Event 12705530 """
    EndIfFlagDisabled(12700175)
    Kill(arg_0_3, award_souls=False)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    EndOfAnimation(arg_4_7, 1)


@RestartOnRest
def Event12705540(_, arg_0_3: int, arg_4_7: int):
    """ 12705540: Event 12705540 """
    EndIfFlagEnabled(12700175)
    IfFlagDisabled(1, arg_4_7)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(arg_0_3, 5915, affect_npc_part_hp=False)
    Kill(arg_0_3, award_souls=True)


def Event12705550():
    """ 12705550: Event 12705550 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(2700755)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 12705551)
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionTrue(Label.L1, input_condition=15)
    WaitFrames(60)
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


def Event12705552():
    """ 12705552: Event 12705552 """
    IfCharacterHasSpecialEffect(0, 2700755, 153)
    WaitFrames(0)


def Event12705600(
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
    """ 12705600: Event 12705600 """
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
        part_health=999999,
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


def Event12705630(_, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12705630: Event 12705630 """
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


def Event12705660(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_16: uchar, arg_17_17: uchar):
    """ 12705660: Event 12705660 """
    SetCollisionMask(arg_12_15, bit_index=arg_16_16, switch_type=OnOffChange.On)
    SetCollisionMask(arg_12_15, bit_index=arg_17_17, switch_type=OnOffChange.Off)
    IfCharacterHasTAEEvent(0, arg_12_15, tae_event_id=arg_0_3)
    EnableFlag(arg_8_11)
    SetCollisionMask(arg_12_15, bit_index=arg_16_16, switch_type=OnOffChange.Off)
    SetCollisionMask(arg_12_15, bit_index=arg_17_17, switch_type=OnOffChange.On)
    IfCharacterHasTAEEvent(0, arg_12_15, tae_event_id=arg_4_7)
    DisableFlag(arg_8_11)
    Restart()


def Event12700990():
    """ 12700990: Event 12700990 """
    EndIfThisEventFlagEnabled()
    IfPlayerStandingOnCollision(0, 2703500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 144, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 144, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 144, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 144, PlayLogMultiplayerType.HostOnly)


@RestartOnRest
def Event12704450(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12704450: Event 12704450 """
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
def Event12704400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12704400: Event 12704400 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagEnabled(-4, 12410803)
    IfFlagEnabled(-4, 12410804)
    IfConditionTrue(1, input_condition=-4)
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
    IfFlagEnabled(-5, 12410803)
    IfFlagEnabled(-5, 12410804)
    IfConditionTrue(2, input_condition=-5)
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12704401(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12704401: Event 12704401 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfCharacterHasSpecialEffect(1, PLAYER, 6142)
    IfFlagDisabled(1, 6813)
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
    IfFlagDisabled(2, 6813)
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12704410(
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
    """ 12704410: Event 12704410 """
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


@RestartOnRest
def Event12704460(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12704460: Event 12704460 """
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
