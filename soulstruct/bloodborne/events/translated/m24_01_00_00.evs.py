"""CENTRAL YHARNAM

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
# from .common import ArriveAtLantern, LightLantern, ReturnToHuntersDream, GainInsight, ToggleLantern
from .common_entities import *
from .m24_01_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=15, args=(2410950, 2411950, CommonFlags.HuntersDreamVisited, 12417800))
    RunEvent(7000, slot=16, args=(2410951, 2411951, 999, 12417820))
    RunEvent(7000, slot=17, args=(2410952, 2411952, Flags.ClericBeastDead, 12417840))
    RunEvent(7000, slot=18, args=(2410953, 2411953, Flags.GascoigneDead, 12417860))
    Event12411010()
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
    RunEvent(9220, slot=3, args=(2410750, 12414220, 12414221, 2410, 24, 1), arg_types="iiiiBB")
    RunEvent(9240, slot=3, args=(2410750, 12414220, 12414221, 12414222, 24, 1), arg_types="iiiiBB")
    RunEvent(9260, slot=3, args=(2410750, 12414220, 12414221, 12414222, 24, 1), arg_types="iiiiBB")
    RunEvent(9280, slot=3, args=(2410750, 12414220, 12414221, 2410, 12414223, 24, 1), arg_types="iiiiiBB")
    EnableFlag2410IfBossesDead()
    Event12410310()
    CreateObjectVFX(900130, obj=2411000, model_point=200)
    CreateObjectVFX(900130, obj=2411001, model_point=200)
    CreateObjectVFX(900130, obj=2411004, model_point=200)
    DeleteVFX(2413230, erase_root_only=False)
    DeleteVFX(2413233, erase_root_only=False)
    RunEvent(12414400, slot=0, args=(12414440, 2413230, 12414420, 12414430, Flags.ClericBeastDead, 6001))
    RunEvent(12414401, slot=0, args=(12414441, 2413233, 12414421, 12414431, Flags.ClericBeastDead, 6001))
    RunEvent(12414410, slot=0, args=(7, 2410158, 2412920, 12414420, 12414430, 12414440, Flags.ClericBeastDead, 10575))
    RunEvent(12414410, slot=1, args=(0, 2410740, 2412921, 12414421, 12414431, 12414441, Flags.ClericBeastDead, 10576))
    RunEvent(12414450, slot=0, args=(2410158, 2412710, 12414420, 12414430, Flags.ClericBeastFogEntered))
    RunEvent(12414450, slot=1, args=(2410740, 2412711, 12414421, 12414431, Flags.ClericBeastFogEntered))
    RunEvent(12414460, slot=0, args=(2410158, 2412710, 2412800, 2412801, 7014, 12414450, 2412801))
    RunEvent(12414460, slot=1, args=(2410740, 2412711, 2412800, 2412801, 101130, 12414451, 2412801))
    Event12414470()
    Event12414480()
    Event12414490()
    GotoIfFlagDisabled(Label.L0, 12410999)
    EnableFlag(9400)
    EnableFlag(CommonFlags.HuntersDreamVisited)
    AddSpecialEffect(2410015, 5591, affect_npc_part_hp=False)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, 12410999)
    RunEvent(12410286, slot=0, args=(12410400, 12410401, 2411204, 2411316))
    Event12410820()

    # --- 1 --- #
    DefineLabel(1)
    StartPlayLogMeasurement(2410000, 0, overwrite=False)
    StartPlayLogMeasurement(2410001, 18, overwrite=True)
    Event12410990()
    Event12410900()
    TriggerEnemyAI(0, 2410112, 2412000, 2412001, 4.0)
    TriggerEnemyAI(1, 2410113, 2412000, 2412001, 4.0)
    TriggerEnemyAI(2, 2410114, 2412000, 2412001, 4.0)
    TriggerEnemyAI(3, 2410115, 2412000, 2412001, 4.0)
    TriggerEnemyAI(4, 2410116, 2412000, 2412001, 4.0)
    TriggerEnemyAI(10, 2410121, 2412120, 0, 4.0)
    TriggerEnemyAI(11, 2410125, 2412120, 0, 4.0)
    TriggerEnemyAI(12, 2410126, 2412120, 0, 4.0)
    TriggerEnemyAI(13, 2410127, 2412120, 0, 4.0)
    TriggerEnemyAI(15, 2410161, 2412120, 0, 4.0)
    RunEvent(12415080, slot=3, args=(2410178, 7010, 7011, 2412154, 263496, 263431, 2.0), arg_types="iiiiiif")
    RunEvent(12415460, slot=0, args=(2410019, 7020, 7021, 2412251, 1.0, 2412010, 2411219), arg_types="iiiifii")
    RunEvent(12415461, slot=0, args=(2411219, 0, 1))
    RunEvent(12410160, slot=2, args=(2412032, 2412037, 0, 20011002))
    RunEvent(12410160, slot=4, args=(2412122, 2412035, 0, 20011001))
    RunEvent(12410160, slot=5, args=(2412033, 2412038, 1, 500007600))
    RunEvent(12415010, slot=0, args=(2412039, 0, 20011001, 300.0), arg_types="iiif")
    Event12415700()
    RunEvent(12415435, slot=12, args=(2410172, 2412122))
    RunEvent(12415435, slot=13, args=(2410173, 2412122))
    RunEvent(12415435, slot=17, args=(2410186, 2412122))
    RunEvent(12415435, slot=18, args=(2410187, 2412122))
    RunEvent(12415435, slot=19, args=(2410188, 2412122))
    RunEvent(12415435, slot=20, args=(2410189, 2412122))
    RunEvent(12415435, slot=22, args=(2410191, 2412122))
    RunEvent(12415435, slot=23, args=(2410192, 2412122))
    RunEvent(12415475, slot=0, args=(2410194, 7012, 7013, 2412050))
    RunEvent(12415476, slot=0, args=(2410194, 7013))
    RunEvent(12415478, slot=0, args=(2410194,))
    RunEvent(12415477, slot=0, args=(2410113,))
    RunEvent(12415479, slot=0, args=(2410194,))
    RunEvent(12415420, slot=0, args=(2410272, 2412262, 12410379))
    RunEvent(12415420, slot=1, args=(2410278, 2412260, 0))
    RunEvent(12415420, slot=2, args=(2410275, 2412261, 0))
    RunEvent(12415420, slot=3, args=(2410277, 2412263, 0))
    RunEvent(12415420, slot=4, args=(2410271, 2412264, 12410378))
    RunEvent(12415420, slot=5, args=(2410279, 2412265, 0))
    RunEvent(12415225, slot=0, args=(2410015, 3004, 50.0), arg_types="iif")
    RunEvent(12415225, slot=1, args=(2410102, 3027, 50.0), arg_types="iif")
    RunEvent(12415228, slot=0, args=(2410016, 3028, 6.0), arg_types="iif")
    RunEvent(12415232, slot=0, args=(2410178, 2412086))
    RunEvent(12415233, slot=0, args=(2412122, 2410196, 2412136))
    RunEvent(12415250, slot=1, args=(2410182, 7001, 5.0, 10.0, 2412075), arg_types="iiffi")
    RunEvent(12415255, slot=1, args=(2410183,))
    RunEvent(12415255, slot=2, args=(2410182,))
    RunEvent(12415255, slot=4, args=(2410181,))
    RunEvent(12415295, slot=0, args=(2410183, 2412120, 2.0, 2412074), arg_types="iifi")
    RunEvent(12415295, slot=1, args=(2410182, 2412120, 2.0, 2412075), arg_types="iifi")
    RunEvent(12415300, slot=0, args=(12415295, 2410183, 2412074, 2412121, 2.0), arg_types="iiiif")
    RunEvent(12415300, slot=1, args=(12415296, 2410182, 2412075, 2412121, 2.0), arg_types="iiiif")
    RunEvent(12415305, slot=0, args=(12415300, 2410183, 2412121, 2412122, 2.0, 2412084), arg_types="iiiifi")
    RunEvent(12415305, slot=1, args=(12415301, 2410182, 2412121, 2412122, 2.0, 2412085), arg_types="iiiifi")
    RunEvent(12415310, slot=0, args=(12415305, 2410183, 2412084, 2412122, 2.0, 2413500), arg_types="iiiifi")
    RunEvent(12415310, slot=1, args=(12415306, 2410182, 2412085, 2412122, 2.0, 2413500), arg_types="iiiifi")
    RunEvent(12415315, slot=0, args=(2410210, 2412120, 2.0, 2412130), arg_types="iifi")
    RunEvent(12415315, slot=1, args=(2410211, 2412120, 2.0, 2412132), arg_types="iifi")
    RunEvent(12415320, slot=0, args=(12415315, 2410210, 2412130, 2412122, 2413505))
    RunEvent(12415320, slot=1, args=(12415316, 2410211, 2412132, 2412122, 2413505))
    RunEvent(12415325, slot=0, args=(12415320, 2410210, 2412122, 2413502))
    RunEvent(12415325, slot=1, args=(12415321, 2410211, 2412122, 2413501))
    RunEvent(12415330, slot=0, args=(2410213, 2412124, 2412123, 2.0, 2412125), arg_types="iiifi")
    RunEvent(12415335, slot=0, args=(12415330, 2410213, 2412134, 2412122, 2413503))
    RunEvent(12415340, slot=0, args=(2410018, 2412120, 2.0, 2412096), arg_types="iifi")
    RunEvent(12415340, slot=2, args=(2410181, 2412121, 2.0, 2412083), arg_types="iifi")
    RunEvent(12415345, slot=0, args=(12415340, 2410018, 2412096, 0, 2.0, 0, -1), arg_types="iiiifii")
    RunEvent(12415345, slot=2, args=(12415342, 2410181, 2412083, 2412122, 2.0, 1, 2413500), arg_types="iiiifii")
    RunEvent(12410450, slot=0, args=(2410400, 52410990))
    RunEvent(12410450, slot=1, args=(2410401, 52410980))
    RunEvent(12410450, slot=2, args=(2410402, 52410970))
    RunEvent(12410450, slot=3, args=(2410403, 52410960))
    RunEvent(12410450, slot=4, args=(2410404, 52410950))
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
    Event12410290()
    CreateHazard(
        12410430,
        2411205,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=1.5,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12410431,
        2411206,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12410432,
        2411207,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    CreateHazard(
        12410433,
        2411208,
        model_point=100,
        behavior_param_id=6110,
        target_type=DamageTargetType.Character,
        radius=0.6000000238418579,
        life=0.0,
        repetition_time=1.0,
    )
    RunEvent(12410200, slot=0, args=(2411300, 2411310, 12410200))
    RunEvent(12410200, slot=2, args=(2411302, 2411312, 12410202))
    RunEvent(12410200, slot=3, args=(2411303, 2411313, 12410203))
    RunEvent(12410200, slot=5, args=(2411305, 2411315, 12410205))
    RunEvent(12415020, slot=0, args=(7000, 2411305, 12410205, CommonEventTexts.Locked))
    RunEvent(12415020, slot=2, args=(2410021, 2411300, 12410200, 10010160))
    RunEvent(12415020, slot=3, args=(2410021, 2411302, 12410202, 10010160))
    RunEvent(12415020, slot=4, args=(2410021, 2411303, 12410203, 10010160))
    RunEvent(12410100, slot=1, args=(2410011, 2410701, 12410112, 10010161))
    RunEvent(12410100, slot=2, args=(2410050, 2411301, 12410117, 10010161))
    RunEvent(12410110, slot=2, args=(2410701, 12411301, 2, 2410010))
    RunEvent(12410110, slot=3, args=(2411308, 12411302, 2, 2410010))
    RunEvent(12410110, slot=4, args=(2411306, 12411304, 1, 2410030))
    RunEvent(12410110, slot=5, args=(2411304, 12411307, 1, 2410080))
    RunEvent(12410110, slot=6, args=(2411309, 12411308, 1, 2410010))
    RunEvent(12410110, slot=7, args=(2411301, 12411309, 1, 2410090))
    Event12410120()
    RunEvent(12410130, slot=0, args=(12411306,))
    Event12410151()
    Event12410140()
    RunEvent(7600, slot=30, args=(2411999, 2413999))
    RunEvent(7600, slot=31, args=(2411998, 2413998))
    RunEvent(7600, slot=32, args=(2411997, 2413997))
    RunEvent(12415390, slot=0, args=(2410202,))

    # CLERIC BEAST
    Event12414732()
    Event12414733()
    ClericBeastDies()
    PlayClericBeastDeathSound()
    ClericBeastFirstTime()
    EnterClericBeastFog()
    EnterClericBeastFogAsSummon()
    StartClericBeastBattle()
    ControlClericBeastMusic()
    ControlClericBeastCamera()
    StopClericBeastMusic()
    SummonStartClericBeastBattle()
    ClericBeastPhaseTwoTrigger()
    ControlClericBeastCloth()
    ClericBeastLimbDamage(0, 2410, 2410, 1, 20, 480, 490, 8020)
    ClericBeastLimbDamage(1, 2411, 2411, 2, 120, 481, 491, 8000)
    ClericBeastLimbDamage(2, 2412, 2412, 3, 300, 482, 492, 8010)
    ClericBeastLimbDamage(3, 2413, 2413, 4, 200, 483, 493, 8030)
    ClericBeastLimbDamage(4, 2414, 2414, 5, 200, 484, 494, 8040)
    ClericBeastLimbAppearance(0, 480, 490, 5, 10)
    ClericBeastLimbAppearance(1, 481, 491, 6, 11)
    ClericBeastLimbAppearance(2, 482, 492, 7, 12)
    ClericBeastLimbAppearance(3, 483, 493, 8, 13)
    ClericBeastLimbAppearance(4, 484, 494, 9, 14)

    GotoIfFlagEnabled(Label.L2, 12410999)
    FirstAwakening()
    RunEvent(12410285, slot=0, args=(12410400, 12410401, 2411204, 2411316))
    Event12410995()

    # --- 2 --- #
    DefineLabel(2)
    Event12410170()
    RunEvent(12415150, slot=0, args=(2410100, 7010, 7011, 6.0, 263499, 263450), arg_types="iiifii")
    RunEvent(12415150, slot=1, args=(2410101, 7014, 7015, 7.0, 263499, 263440), arg_types="iiifii")
    RunEvent(12415150, slot=2, args=(2410103, 7010, 7011, 4.0, 263499, 263450), arg_types="iiifii")
    RunEvent(12410160, slot=1, args=(2412031, 2412036, 0, 240002600))
    RunEvent(12415160, slot=0, args=(2410130, 9002, 3001))
    RunEvent(12415160, slot=1, args=(2410131, 9000, 3001))
    RunEvent(12415160, slot=2, args=(2410132, 9000, 0))
    RunEvent(12415160, slot=3, args=(2410133, 9001, 0))
    RunEvent(12415160, slot=4, args=(2410134, 9002, 3001))
    RunEvent(12415160, slot=5, args=(2410136, 9001, 0))
    RunEvent(12415160, slot=6, args=(2410137, 9001, 3001))
    RunEvent(12415160, slot=7, args=(2410138, 9001, 0))
    RunEvent(12415160, slot=8, args=(2410139, 9001, 0))
    RunEvent(12415130, slot=0, args=(2410140, 9000, 9061, 52410270, 112499, 112400, 1))
    RunEvent(12415130, slot=1, args=(2410141, 9000, 9061, 52410270, 112499, 112400, 0))
    RunEvent(12415130, slot=3, args=(2410143, 9000, 9061, 52410270, 112499, 112400, 0))
    RunEvent(12415130, slot=4, args=(2410144, 9000, 9061, 52410270, 112499, 112400, 1))
    RunEvent(12415130, slot=6, args=(2410146, 9000, 9061, 52410270, 112499, 112400, 0))
    RunEvent(12415130, slot=7, args=(2410147, 9000, 9061, 52410270, 112499, 112400, 0))
    RunEvent(12415130, slot=8, args=(2410148, 9000, 9061, 52410270, 112499, 112400, 1))
    RunEvent(12415130, slot=9, args=(2410149, 9000, 9061, 52410270, 112499, 112400, 1))
    RunEvent(12415130, slot=10, args=(2410150, 9000, 9061, 52410270, 112499, 112400, 0))
    RunEvent(12415130, slot=14, args=(2410154, 9000, 9061, 52410270, 112499, 112400, 1))
    RunEvent(12410155, slot=0, args=(2410157, 2412020, 2412021, 2412022))
    RunEvent(12410156, slot=0, args=(2410040, 2410500, 2410501))
    RunEvent(12410340, slot=0, args=(2410220, 2412230, 10, 2412220))
    RunEvent(12410340, slot=1, args=(2410221, 2412231, 10, 2412220))
    RunEvent(12410340, slot=2, args=(2410222, 2412232, 10, 2412220))
    RunEvent(12410340, slot=3, args=(2410223, 2412233, 10, 2412220))
    RunEvent(12410340, slot=4, args=(2410224, 2412234, 10, 2412220))
    RunEvent(12410340, slot=5, args=(2410225, 2412235, 10, 2412220))
    RunEvent(12410340, slot=6, args=(2410226, 2412236, 10, 2412220))
    RunEvent(12410340, slot=7, args=(2410227, 2412237, 10, 2412220))
    RunEvent(12410340, slot=8, args=(2410228, 2412238, 10, 2412220))
    RunEvent(12410378, slot=0, args=(2410271, 3021, 2411270, 2412046))
    RunEvent(12410378, slot=1, args=(2410272, 3021, 2411271, 2412045))
    RunEvent(12410380, slot=0, args=(2410275, 3020))
    RunEvent(12410380, slot=1, args=(2410277, 3020))
    RunEvent(12410380, slot=2, args=(2410278, 3020))
    RunEvent(12410380, slot=3, args=(2410279, 3020))
    Event12410370()
    RunEvent(12415372, slot=0, args=(2410023,))
    RunEvent(12415372, slot=1, args=(2410024,))
    RunEvent(12415372, slot=2, args=(2410025,))
    RunEvent(12415372, slot=3, args=(2410026,))
    RunEvent(12415372, slot=4, args=(2410027,))
    RunEvent(12410321, slot=0, args=(12415350, 12410350, 12410351, 12410330, 2411320, 2411317, 2411318))
    RunEvent(12410325, slot=0, args=(12415350, 12410350, 12410351, 12410330))
    RunEvent(12410322, slot=0, args=(12415350, 12410350, 12410351, 12410330, 2412322, 12410320))
    RunEvent(12410323, slot=0, args=(12415350, 12410350, 12410351, 12410330, 2412321, 12410321))
    RunEvent(12410324, slot=0, args=(12415350, 12410350, 12410330, 2411317, 2411318))
    RunEvent(12410330, slot=0, args=(12410330, 2412323, 2411317, 2411318))
    RunEvent(12410490, slot=0, args=(2411510, 2411500, 12410490))
    RunEvent(12410490, slot=1, args=(2411511, 2411501, 12410491))
    Event12410010()
    Event12410011()
    Event12410012()
    RunEvent(12410600, slot=1, args=(12411202, 2411102, 9942))
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagDisabled(1, 6630)
    EnableFlag(12411999)
    SkipLinesIfFlagEnabled(6, 12411999)
    EnableObject(2411100)
    DisableObject(2411103)
    EnableObjectActivation(2411100, obj_act_id=9942)
    DisableObjectActivation(2411103, obj_act_id=9942)
    RunEvent(12410600, slot=2, args=(12411200, 2411100, 9942))
    SkipLines(5)
    DisableObject(2411100)
    EnableObject(2411103)
    DisableObjectActivation(2411100, obj_act_id=9942)
    EnableObjectActivation(2411103, obj_act_id=9942)
    RunEvent(12410600, slot=3, args=(12411203, 2411103, 9942))
    IfCharacterHuman(14, PLAYER)
    SkipLinesIfConditionFalse(2, 14)
    SkipLinesIfFlagDisabled(1, 6640)
    EnableFlag(12411998)
    SkipLinesIfFlagEnabled(5, 12411998)
    EnableObject(2411450)
    DisableObject(2411451)
    EnableTreasure(2411450)
    DisableTreasure(2411451)
    SkipLines(4)
    DisableObject(2411450)
    EnableObject(2411451)
    DisableTreasure(2411450)
    EnableTreasure(2411451)
    IfCharacterHuman(13, PLAYER)
    SkipLinesIfConditionFalse(2, 13)
    SkipLinesIfFlagDisabled(1, 6312)
    EnableFlag(12411997)
    SkipLinesIfFlagEnabled(6, 12411997)
    EnableObject(2411102)
    DisableObject(2411104)
    EnableObjectActivation(2411102, obj_act_id=9942)
    DisableObjectActivation(2411104, obj_act_id=9942)
    RunEvent(12410600, slot=4, args=(12411202, 2411102, 9942))
    SkipLines(5)
    DisableObject(2411102)
    EnableObject(2411104)
    DisableObjectActivation(2411102, obj_act_id=9942)
    EnableObjectActivation(2411104, obj_act_id=9942)
    RunEvent(12410600, slot=5, args=(12411204, 2411104, 9942))

    # FATHER GASCOIGNE
    Event12414812()
    Event12414813()
    GascoigneDies()
    PlayFatherGascoigneDeathSound()
    FatherGascoigneFirstTime()
    EnterFatherGascoigneFog()
    EnterFatherGascoigneFogAsSummon()
    StartFatherGascoigneBattle()
    ControlFatherGascoigneMusic()
    ControlFatherGascoigneCamera()
    StopFatherGascoigneMusic()
    FatherGascoignePhaseTwoTrigger()
    GascoigneHumanAffectedByMusicBox()
    GascoigneBeastAffectedByMusicBox()
    SummonStartFatherGascoigneBattle()
    PlayerOnRoofInGascoigneBattle(0, 2412820, Characters.GascoigneHuman, 2412821, 2412824, 2412822)
    PlayerOnRoofInGascoigneBattle(1, 2412820, Characters.GascoigneBeast, 2412821, 2412824, 2412822)

    RunEvent(12410850, slot=0, args=(70000050, 6030, 2410870))
    RunEvent(12410850, slot=1, args=(70000051, 6030, 2410871))
    RunEvent(12410850, slot=2, args=(70000070, 6030, 2410872))
    RunEvent(12410850, slot=3, args=(70000071, 6030, 2410873))
    RunEvent(12410860, slot=0, args=(2410770, 103089))
    RunEvent(12410870, slot=0, args=(2410770, 103082, 153))
    RunEvent(12410880, slot=0, args=(2410770, 103086))
    Event12410702()
    Event12410704()
    Event12410705()
    Event12410706()
    Event12410710()
    Event12410713()
    Event12410715()
    Event12410716()
    Event12410703()
    DisableFlag(72410330)
    DisableFlag(72410335)
    DisableFlag(72410323)
    Event12410650()
    Event12410651()
    Event12410652()
    Event12410653()
    Event12410654()
    Event12410655()
    Event12410656()
    Event12410657()
    Event12410658()
    Event12410659()
    Event12410661()
    RunEvent(12410662, slot=0, args=(1163, 72410331, 72410338))
    RunEvent(12410662, slot=1, args=(1204, 72410331, 72410339))
    RunEvent(12410662, slot=2, args=(1268, 72410332, 72410340))
    RunEvent(12410662, slot=3, args=(1190, 72410332, 72410341))
    RunEvent(12410662, slot=4, args=(1223, 72410332, 72410342))
    RunEvent(12410662, slot=5, args=(1309, 72410332, 72410343))
    Event12410668()
    RunEvent(12410669, slot=0, args=(2410290, 1124, 0))
    RunEvent(12410669, slot=1, args=(2410291, 1163, 0))
    RunEvent(12410669, slot=2, args=(2410292, 1204, 7001))
    RunEvent(12410669, slot=3, args=(2410293, 1268, 0))
    RunEvent(12410669, slot=4, args=(2410294, 1190, 0))
    RunEvent(12410669, slot=5, args=(2410295, 1223, 7000))
    RunEvent(12410669, slot=6, args=(2410296, 1309, 7002))
    Event12410676()
    Event12410677()
    AggroEmissary(0, 2410290)
    AggroEmissary(1, 2410291)
    AggroEmissary(2, 2410292)
    AggroEmissary(3, 2410293)
    AggroEmissary(4, 2410294)
    AggroEmissary(5, 2410295)
    AggroEmissary(6, 2410296)
    RunEvent(12410687, slot=0, args=(12410687, 72410347))
    RunEvent(12410687, slot=1, args=(12410688, 72410348))
    RunEvent(12410687, slot=2, args=(12410689, 72410349))
    RunEvent(12410687, slot=3, args=(12410690, 72410350))
    RunEvent(12410687, slot=4, args=(12410691, 72410351))
    RunEvent(12410687, slot=5, args=(12410692, 72410352))
    RunEvent(12410693, slot=0, args=(12410693, 72410353))
    RunEvent(12410693, slot=1, args=(12410694, 72410354))
    RunEvent(12410693, slot=2, args=(12410695, 72410355))
    RunEvent(12410693, slot=3, args=(12410696, 72410356))
    RunEvent(12410693, slot=4, args=(12410697, 72410357))
    RunEvent(12410693, slot=5, args=(12410698, 72410358))
    Event12410700()
    Event12410721()
    Event12410730()
    Event12410731()
    Event12410732()
    Event12410733()
    Event12410734()
    Event12410736()
    Event12410737()
    Event12410738()
    Event12410739()
    Event12410785()
    Event12410786()
    Event12410787()
    Event12410740()
    Event12410741()
    Event12410742()
    Event12410743()
    Event12410746()
    Event12410747()
    Event12410748()
    Event12410749()
    RunEvent(12410750, slot=0, args=(72410392, 6030, 2410732))
    Event12410760()
    Event12410761()
    Event12410763()
    RunEvent(12410770, slot=0, args=(2410290,))
    RunEvent(12410770, slot=1, args=(2410291,))
    RunEvent(12410770, slot=2, args=(2410292,))
    RunEvent(12410770, slot=3, args=(2410293,))
    RunEvent(12410770, slot=4, args=(2410294,))
    RunEvent(12410770, slot=5, args=(2410295,))
    RunEvent(12410770, slot=6, args=(2410296,))
    Event12410809()
    Event12410810()
    Event12410811()
    Event12410831()
    Event12410833()
    Event12410834()
    Event12410835()
    Event12410812()
    Event12410813()
    Event12410814()
    Event12410510()
    RunEvent(12415750, slot=0, args=(2413710, 1439, 70000050, 9801))
    RunEvent(12415750, slot=1, args=(2413711, 1439, 70000051, 9801))
    RunEvent(12415750, slot=2, args=(2413712, 1439, 70000070, 9802))
    RunEvent(12415750, slot=3, args=(2413713, 1439, 70000071, 9802))
    RunEvent(12415759, slot=0, args=(2413714, 1439, 70000140, 9802))
    RunEvent(12415770, slot=0, args=(2411250, 9802, 924110))
    RunEvent(12415770, slot=1, args=(2411251, 9802, 924113))
    RunEvent(12415770, slot=2, args=(2411252, 9802, 924110))
    RunEvent(12415770, slot=3, args=(2411253, 9802, 924113))
    RunEvent(12415779, slot=0, args=(2411254,))
    RunEvent(12414100, slot=0, args=(2411000, 7400, 10012000))
    RunEvent(12414100, slot=1, args=(2411001, 7401, 10012001))
    RunEvent(12414100, slot=4, args=(2411004, 7404, 10012004))


def Preconstructor():
    """ 50: Event 50 """

    SkipLinesIfFlagEnabled(2, Flags.FirstAwakeningDone)
    EnableFlag(CommonFlags.CutsceneActive)
    DisableSoundEvent(2413900)

    SkipLinesIfFlagDisabled(1, 12410998)
    EnableFlag(12410999)

    RunEvent(12410005, slot=0, args=(12410999,))

    DisableAnimations(2413950)
    DisableGravity(2413950)
    DisableCharacterCollision(2413950)
    DisableAnimations(2413951)
    DisableGravity(2413951)
    DisableCharacterCollision(2413951)
    DisableAnimations(2413952)
    DisableGravity(2413952)
    DisableCharacterCollision(2413952)
    Event12410744()
    Event12410745()
    Event12410762()
    Event12410800()
    Event12410645()
    Event12410729()
    Event12410830()
    Event12410701()
    Event12410780()

    # TODO: Not sure how flag 12411000 is ever enabled (if it ever is).
    SkipLinesIfFlagDisabled(11, 12411000)
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


def FirstAwakening():
    """ 12410000: Player wakes up in Iosekfa's Clinic for the first time. """
    EndIfThisEventFlagEnabled()
    EndIfOutsideMap(game_map=CENTRAL_YHARNAM)
    SkipLinesIfPlayerGender(2, Gender.Male)
    PlayCutscene(Cutscenes.FirstAwakeningMale, skippable=True, fade_out=True, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(Cutscenes.FirstAwakeningFemale, skippable=True, fade_out=True, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    SetRespawnPoint(RespawnPoints.FirstAwakening)


def Event12411010():
    """ 12411010: Event 12411010 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, 7015)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12417810)


@RestartOnRest
def EnableCharacterIfHighInsightAndClose(_, character: CharacterTyping, insight_threshold: uchar, distance: float):
    """ 12414000: Enable the given character if the player is human, has enough insight, and is within some distance.

    Character plays animation 6200 when they appear, which faintly implies it's an NPC character.
    """
    # TODO: Unused event. Would have permanently enabled some character when the player got close enough with enough
    #  insight.
    EndIfThisEventSlotFlagEnabled()
    DisableCharacter(character)
    IfPlayerInsightAmountGreaterThanOrEqual(1, insight_threshold)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, character, radius=distance)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(character)
    ForceAnimation(character, 6200, wait_for_completion=True)


@RestartOnRest
def KillCharacterIfLowInsight(_, character: CharacterTyping, insight_threshold: uchar, required_flag: int):
    """ 12414010: Event 12414010 """
    # TODO: Unused event. Would have PERMANENTLY killed (without souls) some character given a flag AND low insight.
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(1, required_flag)
    IfPlayerInsightAmountLessThanOrEqual(1, insight_threshold)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    Kill(character, award_souls=False)


def Event12414100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12414100: Event 12414100 """
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


def Event12410005(_, arg_0_3: int):
    """ 12410005: Event 12410005 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableMapPiece(2414220)
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

    # --- 0 --- #
    DefineLabel(0)
    EnableMapPiece(2414220)
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


@RestartOnRest
def TriggerEnemyAI(_, enemy: CharacterTyping, trigger_region_1: RegionTyping, trigger_region_2: RegionTyping,
                   trigger_distance: float):
    """ 12415060: Enemy AI is activated by one of two trigger regions, a distance threshold, or being attacked.

    Either region slot can be set to 0 to be ignored.
    """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(enemy)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=trigger_region_1)
    IfCharacterInsideRegion(-2, PLAYER, region=trigger_region_2)
    IfEntityWithinDistance(-2, PLAYER, enemy, radius=trigger_distance)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(2, attacked_entity=enemy, attacker=PLAYER)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableAI(enemy)


@RestartOnRest
def Event12415080(
    _, enemy: CharacterTyping, standby_anim: int, death_anim: int, trigger_region: int, standby_ai_param: int,
    normal_ai_param: int, trigger_distance: float,
):
    """ 12415080: Event 12415080 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(enemy, normal_ai_param)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(enemy, standby_anim, loop=True, skip_transition=True)
    SetAIParamID(enemy, standby_ai_param)
    DisableGravity(enemy)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=trigger_region)
    IfEntityWithinDistance(-2, PLAYER, enemy, radius=trigger_distance)
    IfConditionTrue(1, input_condition=-2)
    IfHasAIStatus(2, enemy, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(3, attacked_entity=enemy, attacker=PLAYER)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    EnableGravity(enemy)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    WaitRandomFrames(min_frames=20, max_frames=100)
    IfHealthLessThan(4, enemy, 1.0)
    GotoIfConditionTrue(Label.L1, input_condition=4)
    ForceAnimation(enemy, death_anim, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    SetAIParamID(enemy, normal_ai_param)


def Event12415020(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12415020: Event 12415020 """
    DisableNetworkSync()
    IfActionButtonParamActivated(-1, action_button_id=arg_0_3, entity=arg_4_7)
    IfFlagEnabled(-1, arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagEnabled(arg_8_11)
    DisplayDialog(
        arg_12_15,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12410200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410200: Event 12410200 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, 1)
    Wait(1.0)
    DisableObjectActivation(arg_4_7, obj_act_id=2410000)
    DisableObjectActivation(arg_4_7, obj_act_id=2410001)
    IfActionButtonParamActivated(0, action_button_id=7100, entity=arg_4_7)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_8_11)
    ForceAnimation(arg_0_3, 1)
    DisableNetworkSync()
    SkipLinesIfValueNotEqual(1, left=arg_4_7, right=2411314)
    DisplayDialog(
        10010850,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12410100(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410100: Event 12410100 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_8_11)
    IfActionButtonParamActivated(1, action_button_id=arg_0_3, entity=arg_4_7)
    IfFlagEnabled(2, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(
        arg_12_15,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(1.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Wait(1.0)
    Restart()


def Event12410110(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410110: Event 12410110 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    Wait(0.0)


def Event12410120():
    """ 12410120: Event 12410120 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=2412300)
    IfCharacterInsideRegion(2, PLAYER, region=2412301)
    IfFlagEnabled(2, 12410130)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150, affect_npc_part_hp=False)
    Wait(3.0)
    Restart()


def Event12410130(_, arg_0_3: int):
    """ 12410130: Event 12410130 """
    DisableNetworkSync()
    EndIfThisEventSlotFlagEnabled()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    End()


def Event12410150():
    """ 12410150: Event 12410150 """
    DisableNetworkSync()
    EndIfThisEventFlagEnabled()
    IfObjectActivated(0, obj_act_id=12411307)
    DisplayDialog(
        10010850,
        anchor_entity=2411304,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.OneButton,
    )


def Event12410151():
    """ 12410151: Event 12410151 """
    DisableNetworkSync()
    IfFlagEnabled(0, Flags.GascoigneDead)
    EndIfFlagEnabled(12410150)
    EndIfClient()
    IfFlagDisabled(1, 12411000)
    EndIfConditionTrue(1)
    DisableObjectActivation(2411304, obj_act_id=2410080)
    IfActionButtonParamActivated(0, action_button_id=7002, entity=2411304)
    IfPlayGoState(2, PlayGoState.DownloadedFirstChunk)
    GotoIfConditionFalse(Label.L0, input_condition=2)
    DisplayDialog(
        10010180,
        anchor_entity=2411304,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    DisplayDialog(
        10010181,
        anchor_entity=2411304,
        display_distance=3.0,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


@RestartOnRest
def Event12410160(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410160: Event 12410160 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=arg_4_7, sound_type=arg_8_11, sound_id=arg_12_15)


@RestartOnRest
def Event12410140():
    """ 12410140: Event 12410140 """
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1140, 1144))
    GotoIfFlagEnabled(Label.L1, 70000240)
    IfObjectActivated(0, obj_act_id=12411300)
    EnableFlag(70000240)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EndOfAnimation(2411307, 2)
    DisableObjectActivation(2411307, obj_act_id=2410010)
    NotifyDoorEventSoundDampening(2411307, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-1, CommonFlags.HuntersDreamVisited)
    IfFlagEnabled(-1, 9800)
    IfConditionTrue(0, input_condition=-1)
    EndOfAnimation(2411307, 0)
    EnableObjectActivation(2411307, obj_act_id=2410010)
    NotifyDoorEventSoundDampening(2411307, state=DoorState.DoorClosing)
    DisableFlag(62411300)
    DisableFlag(72410329)
    DisableFlag(72410344)
    DisableFlag(72410345)
    DisableFlag(72410346)


def Event12410337(_, arg_0_3: int):
    """ 12410337: Event 12410337 """
    IfObjectActivated(0, obj_act_id=12411303)
    EnableNavmeshType(arg_0_3, NavmeshType.Solid)


@RestartOnRest
def Event12415420(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12415420: Event 12415420 """
    SkipLinesIfValueEqual(1, left=arg_8_11, right=0)
    EndIfFlagEnabled(arg_8_11)
    IfCharacterBackreadEnabled(1, arg_0_3)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    EnableImmortality(arg_0_3)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfCharacterInsideRegion(2, arg_0_3, region=arg_4_7)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(arg_0_3, 5915, affect_npc_part_hp=False)
    Kill(arg_0_3, award_souls=True)


@RestartOnRest
def Event12415430(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 12415430: Event 12415430 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfAttackedWithDamageType(2, attacked_entity=arg_4_7, attacker=PLAYER)
    IfEntityWithinDistance(3, arg_0_3, PLAYER, radius=arg_12_15)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 2)
    Wait(arg_8_11)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12415435(_, arg_0_3: int, arg_4_7: int):
    """ 12415435: Event 12415435 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfConditionTrue(0, input_condition=1)
    WaitRandomFrames(min_frames=0, max_frames=10)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12415460(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float, arg_20_23: int, arg_24_27: int
):
    """ 12415460: Event 12415460 """
    WaitFrames(10)
    Move(arg_0_3, destination=arg_20_23, model_point=-1, destination_type=CoordEntityType.Region)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    DisableGravity(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_12_15)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_16_19)
    IfConditionTrue(1, input_condition=-2)
    IfHasAIStatus(2, arg_0_3, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(3, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    EnableGravity(arg_0_3)
    ForceAnimation(arg_24_27, 1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    End()


@RestartOnRest
def Event12415461(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12415461: Event 12415461 """
    GotoIfFlagEnabled(Label.L0, 12410170)
    ForceAnimation(arg_0_3, arg_4_7)
    IfCharacterHasTAEEvent(1, 2410019, tae_event_id=10)
    IfFlagEnabled(2, 12410170)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(arg_0_3, arg_8_11)
    End()

    # --- 1 --- #
    DefineLabel(1)
    Restart()


def Event12415470(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12415470: Event 12415470 """
    EndIfFlagEnabled(12415234)
    DisableAI(arg_0_3)
    IfHasAIStatus(1, 2410200, ai_status=AIStatusType.Battle)
    IfHasAIStatus(1, 2410201, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=-1)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfEntityWithinDistance(3, arg_0_3, PLAYER, radius=8.0)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionFalse(1, 1)
    Wait(10.0)
    EnableAI(arg_0_3)
    WaitFrames(10)
    SetNest(arg_0_3, arg_4_7)
    AICommand(arg_0_3, command_id=arg_8_11, slot=0)
    ResetAnimation(arg_0_3, disable_interpolation=True)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(-1, arg_0_3, region=arg_4_7)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfConditionTrue(0, input_condition=-1)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12415475(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12415475: Event 12415475 """
    EndIfThisEventFlagEnabled()
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfFlagEnabled(3, 12415477)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(2411202, 0, loop=True)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    SkipLinesIfFinishedConditionTrue(1, 3)
    End()
    SetNest(arg_0_3, 2412051)


@RestartOnRest
def Event12415476(_, arg_0_3: int, arg_4_7: int):
    """ 12415476: Event 12415476 """
    EndIfThisEventSlotFlagEnabled()
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    ForceAnimation(2411202, 0, loop=True)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)


@RestartOnRest
def Event12415477(_, arg_0_3: int):
    """ 12415477: Event 12415477 """
    IfHost(0)
    SetNetworkUpdateAuthority(arg_0_3, UpdateAuthority.Forced)
    DisableFlag(12415477)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12415477)
    ForceAnimation(arg_0_3, 3021, wait_for_completion=True)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event12415478(_, arg_0_3: int):
    """ 12415478: Event 12415478 """
    IfCharacterAlive(1, arg_0_3)
    IfCharacterHasTAEEvent(1, arg_0_3, tae_event_id=10)
    IfFlagEnabled(2, 12415475)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    SetObjectDamageShieldState(2411202, state=True)
    ForceAnimation(2411202, 1, loop=True, skip_transition=True)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    SetObjectDamageShieldState(2411202, state=False)
    ForceAnimation(2411202, 0, loop=True)
    End()


@RestartOnRest
def Event12415479(_, arg_0_3: int):
    """ 12415479: Event 12415479 """
    IfFlagEnabled(1, 12415475)
    IfFlagEnabled(1, 12415477)
    IfConditionTrue(0, input_condition=1)
    SetNest(arg_0_3, 2412051)
    IfFlagDisabled(0, 12415477)
    SetNest(arg_0_3, 2412240)
    Restart()


@RestartOnRest
def Event12415480(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12415480: Event 12415480 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetAIParamID(arg_0_3, arg_16_19)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterBackreadEnabled(0, arg_0_3)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    SetAIParamID(arg_0_3, arg_12_15)
    DisableGravity(arg_0_3)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfFlagEnabled(2, 12415477)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableGravity(arg_0_3)
    SkipLinesIfFinishedConditionTrue(2, 1)
    WaitRandomFrames(min_frames=20, max_frames=100)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event12415498(_, arg_0_3: int, arg_4_7: int):
    """ 12415498: Event 12415498 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomFrames(min_frames=0, max_frames=30)
    ForceAnimation(arg_0_3, 3010, wait_for_completion=True)
    IfFramesElapsed(-2, 51)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, 1)
    ShootProjectile(
        owner_entity=arg_0_3,
        projectile_id=arg_0_3,
        model_point=7,
        behavior_id=arg_4_7,
        launch_angle_x=90,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ForceAnimation(arg_0_3, 7004, wait_for_completion=True)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    Restart()


def Event12410815():
    """ 12410815: Event 12410815 """
    AddSpecialEffect(2410600, 5686, affect_npc_part_hp=False)
    WaitFrames(10)
    IfFlagEnabled(-1, 9802)
    IfPlayerInsightAmountGreaterThanOrEqual(-1, 20)
    IfConditionTrue(0, input_condition=-1)
    SetDisplayMask(2410600, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2410600, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2410600, bit_index=10, switch_type=OnOffChange.Off)
    EnableCharacter(2410600)
    RemoveSpecialEffect(2410600, 5686)
    IfPlayerInsightAmountLessThanOrEqual(1, 18)
    IfFlagDisabled(1, 9802)
    IfConditionTrue(0, input_condition=1)
    Restart()


def Event12410820():
    """ 12410820: Event 12410820 """
    DisableMapCollisionBackreadMask(2414400)
    DisableMapCollisionBackreadMask(2414401)
    DisableMapCollisionBackreadMask(2414402)
    DisableMapCollisionBackreadMask(2414410)
    DisableMapCollisionBackreadMask(2414420)
    DisableMapCollisionBackreadMask(2414421)


@RestartOnRest
def Event12410450(_, arg_0_3: int, arg_4_7: int):
    """ 12410450: Event 12410450 """
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


def EnableFlag2410IfBossesDead():
    """ 12411899: Enables flag 2410 when both Central Yharnam bosses are dead. Multiplayer permission? """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, Flags.GascoigneDead)
    IfFlagEnabled(1, Flags.ClericBeastDead)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(2410)


def ClericBeastDies():
    """ 12411700: Cleric Beast is killed. """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(2413802)
    DisableSoundEvent(2413803)
    DisableCharacter(Characters.ClericBeast)
    Kill(Characters.ClericBeast, award_souls=False)
    DisableObject(Objects.ClericBeastFog)
    DeleteVFX(VFX.ClericBeastFog, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, Characters.ClericBeast)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.ClericBeastFog)
    DeleteVFX(VFX.ClericBeastFog, erase_root_only=True)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Wait(3.0)
    KillBoss(Characters.ClericBeast)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(3,))
    AwardAchievement(Achievements.ClericBeastDefeated)
    SkipLinesIfFlagEnabled(1, 6645)
    AwardItemLot(50000010, host_only=False)
    EnableFlag(2411)
    EnableFlag(9456)
    StopPlayLogMeasurement(2410000)
    StopPlayLogMeasurement(2410001)
    StopPlayLogMeasurement(2410010)
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


def PlayClericBeastDeathSound():
    """ 12411701: Event 12411701 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.ClericBeastDead)
    IfFlagEnabled(1, Flags.ClericBeastDead)
    IfCharacterBackreadDisabled(2, Characters.ClericBeast)
    IfHealthLessThanOrEqual(2, Characters.ClericBeast, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2412800, sound_type=SoundType.c_CharacterMotion, sound_id=500099999)


def ClericBeastFirstTime():
    """ 12411702: Event 12411702 """
    EndIfFlagEnabled(Flags.ClericBeastDead)
    GotoIfThisEventFlagDisabled(Label.L0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(Characters.ClericBeast)
    DisableGravity(Characters.ClericBeast)
    DisableCharacterCollision(Characters.ClericBeast)
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2412805)
    IfConditionTrue(0, input_condition=1)
    Move(Characters.ClericBeast, destination=2412831, destination_type=CoordEntityType.Region,
         short_move=True)
    EnableFlag(72410511)
    EnableCharacter(Characters.ClericBeast)
    ForceAnimation(Characters.ClericBeast, 3028)
    WaitFrames(110)
    EnableGravity(Characters.ClericBeast)
    EnableCharacterCollision(Characters.ClericBeast)
    EnableFlag(Flags.ClericBeastFogEntered)
    EnableFlag(12414223)
    EndIfFlagEnabled(9300)
    RunEvent(9350, 0, args=(1,))
    EnableFlag(9300)


def SummonStartClericBeastBattle():
    """ 12411703: Event 12411703 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.ClericBeastFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(Characters.ClericBeast)
    EnableFlag(Flags.ClericBeastFogEntered)
    EnableFlag(Flags.ClericBeastFirstTimeDone)


def EnterClericBeastFog():
    """ 12414730: Event 12414730 """
    EndIfFlagEnabled(Flags.ClericBeastDead)
    GotoIfFlagEnabled(Label.L0, Flags.ClericBeastFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.ClericBeastFog)
    DeleteVFX(VFX.ClericBeastFog, erase_root_only=False)
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfFlagEnabled(1, Flags.ClericBeastFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.ClericBeastFog)
    CreateVFX(VFX.ClericBeastFog)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.ClericBeastDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2410040, entity=Objects.ClericBeastFog)
    IfFlagEnabled(3, Flags.ClericBeastDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2412800, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2412801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, 5)
    EnableFlag(Flags.ClericBeastFogEntered)
    EnableFlag(12414223)
    Restart()


def EnterClericBeastFogAsSummon():
    """ 12414731: Event 12414731 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.ClericBeastDead)
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfFlagEnabled(1, Flags.ClericBeastFirstTimeDone)
    IfFlagEnabled(1, Flags.ClericBeastFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2410040, entity=Objects.ClericBeastFog)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2412800, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2412801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12414701)
    Restart()


def Event12414732():
    """ 12414732: Event 12414732 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.ClericBeastFog, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12414733():
    """ 12414733: Event 12414733 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.ClericBeastFog, radius=4.0)
    IfEntityWithinDistance(1, PLAYER, Objects.ClericBeastFog, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def StartClericBeastBattle():
    """ 12414702: Event 12414702 """
    EndIfFlagEnabled(Flags.ClericBeastDead)
    DisableAI(Characters.ClericBeast)
    DisableHealthBar(Characters.ClericBeast)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(-1, Flags.ClericBeastFogEntered)
    IfFlagEnabled(-1, 12415400)
    IfConditionTrue(0, input_condition=-1)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.ClericBeast, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(Flags.ClericBeastFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.ClericBeast, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.ClericBeast)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.ClericBeast, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.ClericBeast)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(Characters.ClericBeast)
    EnableBossHealthBar(Characters.ClericBeast, name=500000, slot=0)
    CreatePlayLog(80)
    StartPlayLogMeasurement(2410010, 96, overwrite=True)


def ControlClericBeastMusic():
    """ 12414703: Event 12414703 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.ClericBeastDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2413802)
    DisableSoundEvent(2413803)
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfFlagEnabled(1, Flags.ClericBeastBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 12414701)
    IfCharacterInsideRegion(1, PLAYER, region=2412801)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2413802)
    IfCharacterHasTAEEvent(2, Characters.ClericBeast, tae_event_id=100)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.ClericBeastDead)
    IfFlagEnabled(2, Flags.ClericBeastBattleStarted)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 12414701)
    IfCharacterInsideRegion(2, PLAYER, region=2412801)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2413802)
    WaitFrames(0)
    EnableBossMusic(2413803)


def ControlClericBeastCamera():
    """ 12414704: Event 12414704 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.ClericBeastDead)
    IfHealthGreaterThan(1, Characters.ClericBeast, 0.0)
    IfEntityWithinDistance(1, PLAYER, Characters.ClericBeast, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=1)
    IfHealthGreaterThan(2, Characters.ClericBeast, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.ClericBeast, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Restart()


def StopClericBeastMusic():
    """ 12414705: Event 12414705 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.ClericBeastDead)
    IfFlagEnabled(0, Flags.ClericBeastDead)
    DisableBossMusic(2413802)
    DisableBossMusic(2413803)
    DisableBossMusic(-1)


def ClericBeastPhaseTwoTrigger():
    """ 12414707: Event 12414707 """
    EndIfFlagEnabled(Flags.ClericBeastDead)
    IfHealthLessThan(0, Characters.ClericBeast, 0.699999988079071)
    AICommand(Characters.ClericBeast, command_id=1, slot=1)
    ReplanAI(Characters.ClericBeast)
    IfCharacterHasTAEEvent(0, Characters.ClericBeast, tae_event_id=100)
    AICommand(Characters.ClericBeast, command_id=-1, slot=1)
    ReplanAI(Characters.ClericBeast)


def ControlClericBeastCloth():
    """ 12414708: Event 12414708 """
    EndIfFlagEnabled(Flags.ClericBeastDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHasSpecialEffect(0, Characters.ClericBeast, 482)

    # --- 0 --- #
    DefineLabel(0)
    ChangeCharacterCloth(Characters.ClericBeast, 15, state_id=2)


@RestartOnRest
def ClericBeastLimbDamage(
    _, arg_0_1: short, arg_4_7: int, arg_8_9: short, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12414710: Event 12414710 """
    EndIfFlagEnabled(Flags.ClericBeastDead)
    CreateNPCPart(
        Characters.ClericBeast,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=arg_12_15,
        damage_correction=1.0,
        body_damage_correction=1.0,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.ClericBeast, npc_part_id=arg_4_7, material_sfx_id=72, material_vfx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, Characters.ClericBeast, npc_part_id=arg_4_7, value=0)
    IfHealthLessThanOrEqual(3, Characters.ClericBeast, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(
        Characters.ClericBeast,
        npc_part_id=arg_0_1,
        part_index=arg_8_9,
        part_health=9999999,
        damage_correction=1.0,
        body_damage_correction=1.5,
        is_invincible=False,
        start_in_stop_state=False,
    )
    SetNPCPartEffects(Characters.ClericBeast, npc_part_id=arg_4_7, material_sfx_id=73, material_vfx_id=73)
    ForceAnimation(Characters.ClericBeast, arg_24_27)
    AddSpecialEffect(Characters.ClericBeast, arg_16_19, affect_npc_part_hp=False)
    RemoveSpecialEffect(Characters.ClericBeast, arg_20_23)
    ReplanAI(Characters.ClericBeast)
    Wait(30.0)
    AICommand(Characters.ClericBeast, command_id=1, slot=0)
    ReplanAI(Characters.ClericBeast)
    IfCharacterHasTAEEvent(0, Characters.ClericBeast, tae_event_id=300)
    SetNPCPartHealth(Characters.ClericBeast, npc_part_id=arg_4_7, desired_health=-1, overwrite_max=True)
    AddSpecialEffect(Characters.ClericBeast, arg_20_23, affect_npc_part_hp=False)
    RemoveSpecialEffect(Characters.ClericBeast, arg_16_19)
    AICommand(Characters.ClericBeast, command_id=-1, slot=0)
    ReplanAI(Characters.ClericBeast)
    WaitFrames(10)
    Restart()


def ClericBeastLimbAppearance(_, arg_0_3: int, arg_4_7: int, arg_8_8: uchar, arg_9_9: uchar):
    """ 12414720: Event 12414720 """
    EndIfFlagEnabled(Flags.ClericBeastDead)
    IfCharacterHasSpecialEffect(1, Characters.ClericBeast, arg_0_3)
    IfCharacterDoesNotHaveSpecialEffect(1, Characters.ClericBeast, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(Characters.ClericBeast, bit_index=arg_9_9, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.ClericBeast, bit_index=arg_8_8, switch_type=OnOffChange.Off)
    IfCharacterDoesNotHaveSpecialEffect(2, Characters.ClericBeast, arg_0_3)
    IfCharacterHasSpecialEffect(2, Characters.ClericBeast, arg_4_7)
    IfConditionTrue(0, input_condition=2)
    SetDisplayMask(Characters.ClericBeast, bit_index=arg_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(Characters.ClericBeast, bit_index=arg_9_9, switch_type=OnOffChange.Off)
    WaitFrames(10)
    Restart()


def GascoigneDies():
    """ 12411800: Father Gascoigne is killed. """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(2413812)
    DisableSoundEvent(2413813)
    DisableCharacter(Characters.GascoigneHuman)
    DisableCharacter(Characters.GascoigneBeast)
    Kill(Characters.GascoigneHuman, award_souls=False)
    Kill(Characters.GascoigneBeast, award_souls=False)
    DisableObject(2411810)
    DeleteVFX(2413810, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, Characters.GascoigneHuman)
    IfCharacterDead(2, Characters.GascoigneBeast)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2411810)
    DeleteVFX(2413810, erase_root_only=True)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, 2)
    KillBoss(Characters.GascoigneHuman)
    SkipLines(1)
    KillBoss(Characters.GascoigneBeast)
    SetNetworkUpdateRate(Characters.GascoigneBeast, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, 0, args=(2,))
    AwardAchievement(14)
    AwardItemLot(31000, host_only=False)
    EnableFlag(2412)
    EnableFlag(9457)
    EnableFlag(5910)
    StopPlayLogMeasurement(2410000)
    StopPlayLogMeasurement(2410001)
    StopPlayLogMeasurement(2410010)
    CreatePlayLog(40)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 114, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 114, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 114, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 114, PlayLogMultiplayerType.HostOnly)
    End()

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def PlayFatherGascoigneDeathSound():
    """ 12411801: Event 12411801 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GascoigneDead)
    IfFlagEnabled(1, Flags.GascoigneDead)
    IfCharacterBackreadDisabled(2, Characters.GascoigneHuman)
    IfHealthLessThanOrEqual(2, Characters.GascoigneHuman, 0.0)
    IfCharacterBackreadDisabled(3, Characters.GascoigneBeast)
    IfHealthLessThanOrEqual(3, Characters.GascoigneBeast, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2412810, sound_type=SoundType.c_CharacterMotion, sound_id=500099999)


def FatherGascoigneFirstTime():
    """ 12411802: Event 12411802 """
    EndIfFlagEnabled(Flags.GascoigneDead)
    EndIfThisEventFlagEnabled()
    DisableCharacter(Characters.GascoigneHuman)
    IfFlagDisabled(1, Flags.GascoigneDead)
    IfThisEventFlagDisabled(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2412815)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12414223)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(CommonFlags.CutsceneActive)
    WaitFrames(1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(Cutscenes.GascoigneFirstFight, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(Cutscenes.GascoigneFirstFight, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    Move(Characters.GascoigneHuman, destination=2412830, destination_type=CoordEntityType.Region,
         short_move=True)
    EnableCharacter(Characters.GascoigneHuman)
    EnableFlag(Flags.GascoigneFogEntered)
    EndIfFlagEnabled(9336)
    RunEvent(9350, 0, args=(1,))
    EnableFlag(9336)


def SummonStartFatherGascoigneBattle():
    """ 12411803: Event 12411803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.GascoigneFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(Characters.GascoigneHuman)
    EnableFlag(Flags.GascoigneFogEntered)
    EnableFlag(Flags.GascoigneFirstTimeDone)


def EnterFatherGascoigneFog():
    """ 12414810: Event 12414810 """
    EndIfFlagEnabled(Flags.GascoigneDead)
    GotoIfFlagEnabled(Label.L0, Flags.GascoigneFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(2411810)
    DeleteVFX(2413810, erase_root_only=False)
    IfFlagDisabled(1, Flags.GascoigneDead)
    IfFlagEnabled(1, Flags.GascoigneFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2411810)
    CreateVFX(2413810)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.GascoigneDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=2410041, entity=2411810)
    IfFlagEnabled(3, Flags.GascoigneDead)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2412810, animation=101130, wait_for_completion=False)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2412811)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(Flags.GascoigneFogEntered)
    Restart()


def EnterFatherGascoigneFogAsSummon():
    """ 12414811: Event 12414811 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GascoigneDead)
    IfFlagDisabled(1, Flags.GascoigneDead)
    IfFlagEnabled(1, Flags.GascoigneFirstTimeDone)
    IfFlagEnabled(1, Flags.GascoigneFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=2410041, entity=2411810)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2412810, animation=101130, wait_for_completion=False)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2412811)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(Flags.GascoigneFogEnteredAsSummon)
    Restart()


def Event12414812():
    """ 12414812: Event 12414812 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2411810, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12414813():
    """ 12414813: Event 12414813 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, 2411810, radius=4.0)
    IfEntityWithinDistance(1, PLAYER, 2411810, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def StartFatherGascoigneBattle():
    """ 12414802: Event 12414802 """
    EndIfFlagEnabled(Flags.GascoigneDead)
    DisableAI(Characters.GascoigneHuman)
    DisableAI(Characters.GascoigneBeast)
    DisableHealthBar(Characters.GascoigneHuman)
    DisableHealthBar(Characters.GascoigneBeast)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.GascoigneFogEntered)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 12414223)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.GascoigneHuman, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.GascoigneBeast, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12414223)
    EnableFlag(Flags.GascoigneFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.GascoigneHuman, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.GascoigneBeast, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.GascoigneHuman)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.GascoigneBeast)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.GascoigneHuman, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.GascoigneBeast, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.GascoigneHuman)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.GascoigneBeast)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    ReferDamageToEntity(Characters.GascoigneHuman, Characters.GascoigneBeast)
    GotoIfFlagEnabled(Label.L5, Flags.GascoignePhaseTwo)
    EnableAI(Characters.GascoigneHuman)
    EnableBossHealthBar(Characters.GascoigneHuman, name=271000, slot=0)
    Goto(Label.L6)

    # --- 5 --- #
    DefineLabel(5)
    EnableAI(Characters.GascoigneBeast)
    EnableBossHealthBar(Characters.GascoigneBeast, name=272000, slot=0)

    # --- 6 --- #
    DefineLabel(6)
    CreatePlayLog(80)
    StartPlayLogMeasurement(2410010, 96, overwrite=True)


def ControlFatherGascoigneMusic():
    """ 12414803: Event 12414803 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GascoigneDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(2413812)
    DisableSoundEvent(2413813)
    IfFlagDisabled(1, Flags.GascoigneDead)
    IfFlagEnabled(1, 12414802)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, Flags.GascoigneFogEnteredAsSummon)
    IfCharacterInsideRegion(1, PLAYER, region=2412812)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(2413812)
    IfFlagEnabled(2, Flags.GascoignePhaseTwo)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.GascoigneDead)
    IfFlagEnabled(2, 12414802)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, Flags.GascoigneFogEnteredAsSummon)
    IfCharacterInsideRegion(2, PLAYER, region=2412812)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(2413812)
    WaitFrames(0)
    EnableBossMusic(2413813)


def ControlFatherGascoigneCamera():
    """ 12414804: Event 12414804 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GascoigneDead)
    GotoIfFlagEnabled(Label.L0, Flags.GascoignePhaseTwo)
    IfHealthGreaterThan(1, Characters.GascoigneHuman, 0.0)
    IfEntityWithinDistance(1, PLAYER, Characters.GascoigneHuman, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=1)
    IfHealthGreaterThan(2, Characters.GascoigneHuman, 0.0)
    IfEntityBeyondDistance(2, PLAYER, Characters.GascoigneHuman, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthGreaterThan(3, Characters.GascoigneBeast, 0.0)
    IfEntityWithinDistance(3, PLAYER, Characters.GascoigneBeast, radius=5.5)
    IfConditionTrue(0, input_condition=3)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=1)
    IfHealthGreaterThan(4, Characters.GascoigneBeast, 0.0)
    IfEntityBeyondDistance(4, PLAYER, Characters.GascoigneBeast, radius=6.0)
    IfConditionTrue(0, input_condition=4)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Restart()


def StopFatherGascoigneMusic():
    """ 12414805: Event 12414805 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.GascoigneDead)
    IfFlagEnabled(0, Flags.GascoigneDead)
    DisableBossMusic(2413812)
    DisableBossMusic(2413813)
    DisableBossMusic(-1)


def FatherGascoignePhaseTwoTrigger():
    """ 12414807: Event 12414807 """
    EndIfFlagEnabled(Flags.GascoigneDead)
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(Characters.GascoigneHuman)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(Characters.GascoigneBeast)
    IfHealthLessThan(1, Characters.GascoigneHuman, 0.3400000035762787)
    IfCharacterHasTAEEvent(2, Characters.GascoigneHuman, tae_event_id=30)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    AICommand(Characters.GascoigneHuman, command_id=40, slot=0)
    SkipLinesIfFinishedConditionTrue(1, 2)
    IfCharacterHasTAEEvent(0, Characters.GascoigneHuman, tae_event_id=30)
    WaitFrames(5)
    DisableCharacter(Characters.GascoigneHuman)
    EnableGravity(Characters.GascoigneBeast)
    SetNetworkUpdateRate(Characters.GascoigneBeast, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        Characters.GascoigneBeast,
        destination=Characters.GascoigneHuman,
        destination_type=CoordEntityType.Character,
        model_point=203,
        copy_draw_parent=Characters.GascoigneHuman,
    )
    ForceAnimation(Characters.GascoigneBeast, 3030, wait_for_completion=True)
    EnableAI(Characters.GascoigneBeast)
    EnableBossHealthBar(Characters.GascoigneBeast, name=272000, slot=0)
    EndIfFlagEnabled(9337)
    RunEvent(9350, 0, args=(1,))
    EnableFlag(9337)


def GascoigneHumanAffectedByMusicBox():
    """ 12414808: Event 12414808 """
    IfCharacterHasSpecialEffect(1, Characters.GascoigneHuman, Effects.MusicBox)
    IfHealthGreaterThanOrEqual(1, Characters.GascoigneHuman, 0.3400000035762787)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.GascoigneHuman, command_id=60, slot=0)
    ReplanAI(Characters.GascoigneHuman)
    IfCharacterHasTAEEvent(0, Characters.GascoigneHuman, tae_event_id=10)
    AICommand(Characters.GascoigneHuman, command_id=-1, slot=0)
    ReplanAI(Characters.GascoigneHuman)
    Wait(10.0)
    IfCharacterHasSpecialEffect(1, Characters.GascoigneHuman, Effects.MusicBox)
    IfHealthGreaterThanOrEqual(1, Characters.GascoigneHuman, 0.3400000035762787)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.GascoigneHuman, command_id=60, slot=0)
    ReplanAI(Characters.GascoigneHuman)
    IfCharacterHasTAEEvent(0, Characters.GascoigneHuman, tae_event_id=10)
    AICommand(Characters.GascoigneHuman, command_id=-1, slot=0)
    ReplanAI(Characters.GascoigneHuman)
    Wait(10.0)
    IfCharacterHasSpecialEffect(1, Characters.GascoigneHuman, Effects.MusicBox)
    IfHealthGreaterThanOrEqual(1, Characters.GascoigneHuman, 0.3400000035762787)
    IfConditionTrue(0, input_condition=1)
    AICommand(Characters.GascoigneHuman, command_id=60, slot=0)
    ReplanAI(Characters.GascoigneHuman)
    IfCharacterHasTAEEvent(0, Characters.GascoigneHuman, tae_event_id=10)
    AICommand(Characters.GascoigneHuman, command_id=40, slot=0)
    ReplanAI(Characters.GascoigneHuman)


def GascoigneBeastAffectedByMusicBox():
    """ 12414809: Event 12414809 """
    IfFlagEnabled(0, Flags.GascoignePhaseTwo)
    Wait(3.0)
    IfCharacterHasSpecialEffect(0, Characters.GascoigneBeast, Effects.MusicBox)
    AICommand(Characters.GascoigneBeast, command_id=50, slot=0)
    ReplanAI(Characters.GascoigneBeast)
    IfCharacterHasTAEEvent(0, Characters.GascoigneBeast, tae_event_id=20)
    AICommand(Characters.GascoigneBeast, command_id=-1, slot=0)
    ReplanAI(Characters.GascoigneBeast)


@RestartOnRest
def Event12415225(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12415225: Event 12415225 """
    EndIfThisEventSlotFlagEnabled()
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(arg_0_3, arg_4_7)


@RestartOnRest
def Event12415228(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 12415228: Event 12415228 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_8_11)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableAI(arg_0_3)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(arg_0_3, arg_4_7)


@RestartOnRest
def Event12415232(_, arg_0_3: int, arg_4_7: int):
    """ 12415232: Event 12415232 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_4_7)


@RestartOnRest
def Event12415233(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12415233: Event 12415233 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_4_7, arg_8_11)


def Event12415234(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12415234: Event 12415234 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterDead(1, arg_0_3)
    IfCharacterDead(1, arg_4_7)
    IfCharacterAlive(1, arg_8_11)
    IfEntityWithinDistance(2, arg_8_11, PLAYER, radius=10.0)
    IfEntityBeyondDistance(3, arg_8_11, PLAYER, radius=10.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EndIfFinishedConditionTrue(2)
    IfEntityWithinDistance(0, PLAYER, 0, radius=0.0)
    WaitFrames(10)


def Event12415236(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12415236: Event 12415236 """
    IfFlagEnabled(15, 12415236)
    IfClient(15)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    DisableCharacter(arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_12_15)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, arg_0_3)
    IfFlagEnabled(1, 12415234)
    IfCharacterAlive(1, arg_8_11)
    IfAllPlayersInsideRegion(1, region=2412143)
    IfHealthLessThanOrEqual(-2, arg_4_7, 0.5)
    IfTimeElapsed(-2, 40.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EndIfFlagEnabled(Flags.ClericBeastDead)
    EnableFlag(12415236)
    DisableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(arg_12_15, UpdateAuthority.Forced)
    Wait(1.0)
    SetNest(arg_12_15, arg_16_19)
    AICommand(arg_12_15, command_id=10, slot=0)
    ReplanAI(arg_12_15)
    DisableGravity(arg_12_15)
    DisableCharacterCollision(arg_12_15)
    DisableAnimations(arg_12_15)
    IfEntityWithinDistance(-3, arg_12_15, Characters.ClericBeast, radius=3.0)
    IfCharacterInsideRegion(-3, arg_12_15, region=2412801)
    IfConditionTrue(0, input_condition=-3)
    AICommand(arg_12_15, command_id=-1, slot=0)
    ClearTargetList(arg_12_15)
    ReplanAI(arg_12_15)
    EnableCharacterCollision(arg_12_15)
    EnableAnimations(arg_12_15)
    EnableGravity(arg_12_15)


@RestartOnRest
def PlayerOnRoofInGascoigneBattle(_, on_roof: int, gascoigne: int, below_roof: int, on_stairs: int, off_roof: int):
    """ 12415238: Makes either version of Gascoigne go up above roof if player is on it and Gascoigne is below it. """
    IfCharacterInsideRegion(1, gascoigne, region=below_roof)
    IfAllPlayersInsideRegion(1, region=on_roof)
    IfConditionTrue(0, input_condition=1)
    SetNest(gascoigne, on_stairs)
    AICommand(gascoigne, command_id=10, slot=0)
    ReplanAI(gascoigne)
    IfCharacterInsideRegion(-1, gascoigne, region=off_roof)
    IfAttackedWithDamageType(-1, attacked_entity=gascoigne, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    AICommand(gascoigne, command_id=-1, slot=0)
    ReplanAI(gascoigne)
    Restart()


@RestartOnRest
def Event12415250(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float, arg_16_19: int):
    """ 12415250: Event 12415250 """
    IfCharacterInsideRegion(0, arg_0_3, region=arg_16_19)
    WaitRandomSeconds(min_seconds=arg_8_11, max_seconds=arg_12_15)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event12415255(_, arg_0_3: int):
    """ 12415255: Event 12415255 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfHasAIStatus(2, arg_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    RestartIfFinishedConditionTrue(1)
    AICommand(arg_0_3, command_id=20, slot=0)
    ReplanAI(arg_0_3)
    Restart()


@RestartOnRest
def Event12415260(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12415260: Event 12415260 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(arg_0_3, arg_24_27)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=2413500)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    SetNest(arg_0_3, arg_12_15)
    AICommand(arg_0_3, command_id=20, slot=0)
    IfCharacterInsideRegion(2, arg_0_3, region=arg_12_15)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-3)
    IfCharacterInsideRegion(-4, PLAYER, region=arg_16_19)
    IfEntityWithinDistance(-4, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(2, input_condition=-4)
    IfConditionTrue(0, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    AICommand(arg_0_3, command_id=-1, slot=0)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterType(-4, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-4)
    IfCharacterInsideRegion(-5, PLAYER, region=arg_16_19)
    IfCharacterInsideRegion(-5, PLAYER, region=arg_20_23)
    IfEntityWithinDistance(-5, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(3, input_condition=-5)
    IfConditionTrue(0, input_condition=3)
    WaitRandomFrames(min_frames=0, max_frames=300)

    # --- 1 --- #
    DefineLabel(1)
    SetNest(arg_0_3, arg_24_27)
    AICommand(arg_0_3, command_id=20, slot=0)
    IfCharacterInsideRegion(4, arg_0_3, region=arg_24_27)
    IfCharacterHuman(-6, PLAYER)
    IfCharacterType(-6, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(5, input_condition=-6)
    IfCharacterInsideRegion(-7, PLAYER, region=arg_20_23)
    IfEntityWithinDistance(-7, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(5, input_condition=-7)
    IfConditionTrue(0, input_condition=5)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=2413500)


@RestartOnRest
def Event12415295(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 12415295: Event 12415295 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(arg_0_3, arg_12_15)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    SetNest(arg_0_3, arg_12_15)
    AICommand(arg_0_3, command_id=20, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12415300(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float):
    """ 12415300: Event 12415300 """
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, arg_0_3)
    IfCharacterInsideRegion(2, arg_4_7, region=arg_8_11)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_12_15)
    IfEntityWithinDistance(-2, PLAYER, arg_4_7, radius=arg_16_19)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event12415305(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float, arg_20_23: int):
    """ 12415305: Event 12415305 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(arg_4_7, arg_20_23)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_12_15)
    IfEntityWithinDistance(-2, PLAYER, arg_4_7, radius=arg_16_19)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    WaitRandomFrames(min_frames=0, max_frames=30)

    # --- 1 --- #
    DefineLabel(1)
    SetNest(arg_4_7, arg_20_23)
    AICommand(arg_4_7, command_id=20, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event12415310(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float, arg_20_23: int):
    """ 12415310: Event 12415310 """
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, arg_0_3)
    IfCharacterInsideRegion(2, arg_4_7, region=arg_8_11)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_12_15)
    IfEntityWithinDistance(-2, PLAYER, arg_4_7, radius=arg_16_19)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    ChangePatrolBehavior(arg_4_7, patrol_information_id=arg_20_23)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)


@RestartOnRest
def Event12415315(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 12415315: Event 12415315 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(arg_0_3, arg_12_15)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(3, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EnableAI(arg_0_3)
    SetNest(arg_0_3, arg_12_15)


@RestartOnRest
def Event12415320(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12415320: Event 12415320 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(1, arg_0_3)
    IfCharacterInsideRegion(2, arg_4_7, region=arg_8_11)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=arg_12_15)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(arg_4_7, patrol_information_id=arg_16_19)


@RestartOnRest
def Event12415325(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12415325: Event 12415325 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(1, arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=arg_8_11)
    IfConditionTrue(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(arg_4_7, patrol_information_id=arg_12_15)


@RestartOnRest
def Event12415330(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: int):
    """ 12415330: Event 12415330 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(3, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(4, PLAYER, region=arg_16_19)
    IfEntityWithinDistance(5, PLAYER, arg_0_3, radius=arg_12_15)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=5)
    Wait(10.0)

    # --- 1 --- #
    DefineLabel(1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12415335(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12415335: Event 12415335 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(1, arg_0_3)
    IfCharacterInsideRegion(2, arg_4_7, region=arg_8_11)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=arg_12_15)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(arg_4_7, patrol_information_id=arg_16_19)


@RestartOnRest
def Event12415340(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int):
    """ 12415340: Event 12415340 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(arg_0_3, arg_12_15)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(3, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(4, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=4)
    AICommand(arg_0_3, command_id=20, slot=0)

    # --- 1 --- #
    DefineLabel(1)
    WaitFrames(10)
    SetNest(arg_0_3, arg_12_15)


@RestartOnRest
def Event12415345(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float, arg_20_23: int, arg_24_27: int
):
    """ 12415345: Event 12415345 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfFlagEnabled(1, arg_0_3)
    IfCharacterInsideRegion(2, arg_4_7, region=arg_8_11)
    IfAttackedWithDamageType(3, attacked_entity=arg_4_7, attacker=-1)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(4, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_12_15)
    IfEntityWithinDistance(-2, PLAYER, arg_4_7, radius=arg_16_19)
    IfConditionTrue(4, input_condition=-2)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_4_7, command_id=-1, slot=0)
    ReplanAI(arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    EndIfValueEqual(left=arg_20_23, right=0)
    ChangePatrolBehavior(arg_4_7, patrol_information_id=arg_24_27)


def Event12410286(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410286: Event 12410286 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_8_11, 2)
    Wait(1.0)
    RegisterLadder(start_climbing_flag=arg_0_3, stop_climbing_flag=arg_4_7, obj=arg_8_11)
    DisableObjectActivation(arg_12_15, obj_act_id=2410000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObjectActivation(arg_12_15, obj_act_id=2410000)
    ForceAnimation(arg_8_11, 2)
    RegisterLadder(start_climbing_flag=arg_0_3, stop_climbing_flag=arg_4_7, obj=arg_8_11)


def Event12410290():
    """ 12410290: Event 12410290 """
    DeleteVFX(2413110, erase_root_only=False)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2412150)
    IfConditionTrue(0, input_condition=1)
    CreateVFX(2413110)


def Event12415360(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12415360: Event 12415360 """
    EndIfThisEventSlotFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_0_3)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_4_7, arg_8_11)


def Event12415390(_, arg_0_3: int):
    """ 12415390: Event 12415390 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetNest(arg_0_3, 2412242)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    SetNest(arg_0_3, 2412241)
    Restart()


@RestartOnRest
def Event12415700():
    """ 12415700: Event 12415700 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2410270, PLAYER, radius=8.0)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(2410270, patrol_information_id=2413510)
    ReplanAI(2410270)


@RestartOnRest
def Event12415750(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12415750: Event 12415750 """
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
def Event12415759(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12415759: Event 12415759 """
    DisableSoundEvent(arg_0_3)
    EndIfFlagEnabled(1245)
    EndIfFlagEnabled(1246)
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
def Event12415770(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12415770: Event 12415770 """
    DeleteObjectVFX(arg_0_3, erase_root=True)
    EndIfFlagEnabled(arg_4_7)
    CreateObjectVFX(arg_8_11, obj=arg_0_3, model_point=200)


@RestartOnRest
def Event12415779(_, arg_0_3: int):
    """ 12415779: Event 12415779 """
    CreateObjectVFX(924113, obj=arg_0_3, model_point=200)
    IfFlagEnabled(1, 1180)
    IfFlagEnabled(1, 1193)
    IfFlagEnabled(1, 1194)
    IfConditionTrue(0, input_condition=1)
    DeleteObjectVFX(arg_0_3, erase_root=True)


def Event12410900():
    """ 12410900: Event 12410900 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2412911)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9403)


def Event12410310():
    """ 12410310: Event 12410310 """
    GotoIfFlagEnabled(Label.L2, 9802)
    GotoIfFlagEnabled(Label.L1, 9801)
    GotoIfFlagEnabled(Label.L0, 9800)
    EnableMapPiece(2414010)
    DisableMapPiece(2414011)
    DisableMapPiece(2414012)
    DisableMapPiece(2414013)
    DisableMapPiece(2414070)
    DisableMapPiece(2414071)
    DeleteVFX(2413350, erase_root_only=False)
    DeleteVFX(2413380, erase_root_only=False)
    Goto(Label.L3)

    # --- 0 --- #
    DefineLabel(0)
    DisableMapPiece(2414010)
    EnableMapPiece(2414011)
    DisableMapPiece(2414012)
    DisableMapPiece(2414013)
    DisableMapPiece(2414070)
    DisableMapPiece(2414071)
    DeleteVFX(2413350, erase_root_only=False)
    DeleteVFX(2413380, erase_root_only=False)
    Goto(Label.L3)

    # --- 1 --- #
    DefineLabel(1)
    DisableMapPiece(2414010)
    DisableMapPiece(2414011)
    EnableMapPiece(2414012)
    DisableMapPiece(2414013)
    DisableMapPiece(2414050)
    DisableMapPiece(2414051)
    DeleteVFX(2413300, erase_root_only=False)
    DeleteVFX(2413301, erase_root_only=False)
    DeleteVFX(2413302, erase_root_only=False)
    DeleteVFX(2413303, erase_root_only=False)
    DeleteVFX(2413304, erase_root_only=False)
    DeleteVFX(2413305, erase_root_only=False)
    DeleteVFX(2413380, erase_root_only=False)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    DisableMapPiece(2414010)
    DisableMapPiece(2414011)
    DisableMapPiece(2414012)
    EnableMapPiece(2414013)
    DisableMapPiece(2414050)
    DisableMapPiece(2414051)
    DeleteVFX(2413350, erase_root_only=False)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagChange(-1, 9800)
    IfFlagChange(-1, 9801)
    IfFlagChange(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


def Event12410010():
    """ 12410010: Event 12410010 """
    EndIfFlagEnabled(CommonFlags.HuntersDreamVisited)
    DisableSoapstoneMessage(2413601)
    DisableSoapstoneMessage(2413604)


def Event12410011():
    """ 12410011: Event 12410011 """
    End()
    EndIfThisEventFlagEnabled()
    DisableSoapstoneMessage(2413603)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagEnabled(1, 52410120)
    IfConditionTrue(0, input_condition=1)
    EnableSoapstoneMessage(2413603)


def Event12410012():
    """ 12410012: Event 12410012 """
    EndIfThisEventFlagEnabled()
    DisableSoapstoneMessage(2413610)
    DisableSoapstoneMessage(2413611)
    IfFlagEnabled(0, CommonFlags.HuntersDreamVisited)
    EnableSoapstoneMessage(2413610)
    EnableSoapstoneMessage(2413611)


@RestartOnRest
def Event12410170():
    """ 12410170: Event 12410170 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2410019)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableHealthBar(2410019)
    AddSpecialEffect(2410019, 5617, affect_npc_part_hp=False)
    AddSpecialEffect(2410019, 5708, affect_npc_part_hp=False)
    Wait(3.0)
    EnableHealthBar(2410019)
    IfCharacterDead(0, 2410019)
    End()


@RestartOnRest
def Event12415100(_, arg_0_3: int):
    """ 12415100: Event 12415100 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7000)
    DisableGravity(arg_0_3)
    IfHasAIStatus(-1, 2410019, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2410019, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, 2)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=3.0)
    ForceAnimation(arg_0_3, 7002)
    EnableAI(arg_0_3)
    EnableGravity(arg_0_3)


def Event12410510():
    """ 12410510: Event 12410510 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventFlagEnabled()
    GotoIfFlagEnabled(Label.L0, 12410511)
    IfCharacterInsideRegion(0, PLAYER, region=2412350)
    EnableFlag(12410511)

    # --- 0 --- #
    DefineLabel(0)
    CreateObjectVFX(900201, obj=2411200, model_point=200)
    IfActionButtonParamActivated(0, action_button_id=2410060, entity=2411200)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2410990, host_only=False)
    DeleteObjectVFX(2411200, erase_root=True)


def Event12410030(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12410030: Event 12410030 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    SetAIParamID(arg_0_3, arg_16_19)
    DisableGravity(arg_0_3)
    IfHasAIStatus(-1, arg_12_15, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_12_15, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    EnableGravity(arg_0_3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(arg_12_15, 3021)
    WaitRandomFrames(min_frames=20, max_frames=70)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_20_23)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_8_11)


def Event12410040(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12410040: Event 12410040 """
    SetAIParamID(arg_0_3, arg_4_7)
    IfHasAIStatus(-1, arg_16_19, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_16_19, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-2)
    ForceAnimation(arg_16_19, arg_20_23, wait_for_completion=True)
    IfHealthEqual(1, arg_16_19, 1.0)
    IfHealthLessThan(2, arg_16_19, 1.0)
    IfConditionTrue(-4, input_condition=1)
    IfConditionTrue(-4, input_condition=2)
    IfConditionTrue(0, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    SetAIParamID(arg_0_3, arg_8_11)
    WaitFrames(100)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_12_15)


def Event12410050(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12410050: Event 12410050 """
    SetAIParamID(arg_0_3, arg_4_7)
    IfHasAIStatus(-1, arg_16_19, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_16_19, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_16_19, arg_20_23)
    SetAIParamID(arg_0_3, arg_8_11)
    Wait(300.0)
    SetAIParamID(arg_0_3, arg_12_15)


@RestartOnRest
def Event12415160(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12415160: Event 12415160 """
    WaitRandomFrames(min_frames=0, max_frames=50)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    DisableGravity(arg_0_3)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableGravity(arg_0_3)
    WaitRandomFrames(min_frames=0, max_frames=30)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)


@RestartOnRest
def Event12410600(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410600: Event 12410600 """
    SkipLinesIfThisEventSlotFlagDisabled(4)
    EndOfAnimation(arg_4_7, 0)
    DisableObjectActivation(arg_4_7, obj_act_id=arg_8_11)
    EnableTreasure(arg_4_7)
    End()
    IfObjectActivated(0, obj_act_id=arg_0_3)
    WaitFrames(10)
    EnableTreasure(arg_4_7)


@RestartOnRest
def Event12410630(_, arg_0_3: int, arg_4_7: int):
    """ 12410630: Event 12410630 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventSlotFlagEnabled()
    IfCharacterDead(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)


@RestartOnRest
def Event12410645():
    """ 12410645: Event 12410645 """
    EnableImmortality(2410703)
    DisableHealthBar(2410703)
    IfFlagEnabled(10, 1140)
    GotoIfConditionFalse(Label.L9, input_condition=10)
    DisableBackread(2410703)

    # --- 9 --- #
    DefineLabel(9)
    IfFlagEnabled(1, 1141)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    EnableBackread(2410710)
    DisableBackread(2410711)
    DisableAnimations(2410710)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(2, 1142)
    GotoIfConditionFalse(Label.L7, input_condition=2)
    EnableBackread(2410710)
    DisableBackread(2410711)
    DisableAnimations(2410710)

    # --- 7 --- #
    DefineLabel(7)
    IfFlagEnabled(8, 1143)
    GotoIfConditionFalse(Label.L8, input_condition=8)
    EnableBackread(2410710)
    DisableBackread(2410711)

    # --- 8 --- #
    DefineLabel(8)
    IfFlagEnabled(9, 1144)
    GotoIfConditionFalse(Label.L1, input_condition=9)
    EnableBackread(2410710)
    DisableBackread(2410711)
    DisableAnimations(2410710)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 1145)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableBackread(2410703)
    EnableBackread(2410710)
    DisableBackread(2410711)
    Move(2410710, destination=2412172, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SetNest(2410710, 2412172)
    SetTeamType(2410710, TeamType.Enemy1)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(4, 1146)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableBackread(2410703)
    DisableBackread(2410710)
    EnableBackread(2410711)
    ForceAnimation(2410711, 103000)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(5, 1147)
    GotoIfConditionFalse(Label.L4, input_condition=5)
    DisableBackread(2410703)
    DisableBackread(2410710)
    DisableBackread(2410711)
    DisableBackread(2410703)

    # --- 4 --- #
    DefineLabel(4)
    IfFlagEnabled(6, 1148)
    GotoIfConditionFalse(Label.L5, input_condition=6)
    DisableBackread(2410703)
    DisableBackread(2410710)
    DisableBackread(2410711)
    Move(2410710, destination=2412172, destination_type=CoordEntityType.Region, set_draw_parent=0)
    WaitFrames(1)
    DropMandatoryTreasure(2410710)

    # --- 5 --- #
    DefineLabel(5)
    IfFlagEnabled(7, 1149)
    EndIfConditionFalse(7)
    DisableBackread(2410703)
    DisableBackread(2410710)
    EnableBackread(2410711)
    EzstateAIRequest(2410711, command_id=0, slot=1)
    DropMandatoryTreasure(2410711)


@RestartOnRest
def Event12410650():
    """ 12410650: Event 12410650 """

    # --- 0 --- #
    DefineLabel(0)
    IfFlagRangeAllDisabled(0, (1141, 1159))
    DisableBackread(2410710)
    DisableFlagRange((1140, 1159))
    EnableFlag(1140)


@RestartOnRest
def Event12410651():
    """ 12410651: Event 12410651 """
    EndIfFlagEnabled(1148)
    EndIfFlagEnabled(1149)
    EndIfFlagEnabled(1141)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 9800)
    EnableBackread(2410703)
    EnableBackread(2410710)
    DisableAnimations(2410710)
    DisableFlagRange((1140, 1159))
    EnableFlag(1141)


@RestartOnRest
def Event12410652():
    """ 12410652: Event 12410652 """
    EndIfFlagEnabled(1148)
    EndIfFlagEnabled(1149)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 72410320)
    IfFlagEnabled(1, 1141)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1140, 1159))
    EnableFlag(1142)


@RestartOnRest
def Event12410653():
    """ 12410653: Event 12410653 """
    EndIfFlagEnabled(1148)
    EndIfFlagEnabled(1149)
    EndIfFlagEnabled(1145)
    EndIfFlagEnabled(1146)
    IfCharacterInsideRegion(1, PLAYER, region=2412170)
    IfFlagDisabled(1, 1140)
    IfFlagDisabled(1, 1145)
    IfFlagDisabled(1, 1146)
    IfFlagDisabled(1, 1147)
    IfFlagDisabled(1, 1148)
    IfFlagDisabled(1, 1149)
    IfCharacterAlive(1, 2410710)
    IfConditionTrue(0, input_condition=1)
    SetDistanceLimitForConversationStateChanges(2410710, distance=40.5)
    DisableFlagRange((1140, 1159))
    EnableFlag(1143)
    Restart()


@RestartOnRest
def Event12410654():
    """ 12410654: Event 12410654 """
    EndIfFlagEnabled(1148)
    EndIfFlagEnabled(1149)
    EndIfFlagEnabled(1145)
    EndIfFlagEnabled(1146)
    IfFlagEnabled(1, 1143)
    IfCharacterInsideRegion(1, PLAYER, region=2412171)
    IfConditionTrue(0, input_condition=1)
    SetDistanceLimitForConversationStateChanges(2410710, distance=17.0)
    DisableFlagRange((1140, 1159))
    EnableFlag(1144)
    Restart()


@RestartOnRest
def Event12410655():
    """ 12410655: Event 12410655 """
    EndIfFlagEnabled(1148)
    EndIfFlagEnabled(1149)

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(2410710)
    IfCharacterInsideRegion(1, PLAYER, region=2412190)
    IfFlagDisabled(1, 1140)
    IfFlagDisabled(1, 1146)
    IfFlagDisabled(1, 1147)
    IfFlagDisabled(1, 1148)
    IfFlagDisabled(1, 1149)
    IfConditionTrue(0, input_condition=1)
    EnableAI(2410710)
    SetTeamType(2410710, TeamType.Enemy1)
    DisableFlagRange((1140, 1159))
    EnableFlag(1145)
    SaveRequest()


@RestartOnRest
def Event12410656():
    """ 12410656: Event 12410656 """
    EndIfFlagEnabled(1148)
    EndIfFlagEnabled(1149)
    IfFlagEnabled(1, 9802)
    IfCharacterAlive(1, 2410710)
    IfConditionTrue(0, input_condition=1)
    DisableBackread(2410703)
    DisableBackread(2410710)
    EnableBackread(2410711)
    ForceAnimation(2410711, 103000)
    EnableAnimations(2410711)
    DisableFlagRange((1140, 1159))
    EnableFlag(1146)


@RestartOnRest
def Event12410657():
    """ 12410657: Event 12410657 """
    EndIfFlagEnabled(1148)
    EndIfFlagEnabled(1149)
    EndIfFlagEnabled(1147)
    IfFlagEnabled(0, 72410326)
    DisableBackread(2410703)
    DisableFlagRange((1140, 1159))
    EnableFlag(1147)
    SaveRequest()


@RestartOnRest
def Event12410658():
    """ 12410658: Event 12410658 """
    EndIfFlagEnabled(1149)
    IfHealthLessThanOrEqual(1, 2410710, 0.0)
    IfFlagEnabled(1, 1145)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1140, 1159))
    EnableFlag(1148)
    SaveRequest()


@RestartOnRest
def Event12410659():
    """ 12410659: Event 12410659 """
    IfCharacterInsideRegion(1, PLAYER, region=2412170)
    IfFlagEnabled(1, 1143)
    IfCharacterInsideRegion(2, PLAYER, region=2412171)
    IfFlagDisabled(2, 62411300)
    IfFlagEnabled(2, 1144)
    IfCharacterInsideRegion(3, PLAYER, region=2412171)
    IfFlagEnabled(3, 1147)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    Move(2410710, destination=2412172, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SetNest(2410710, 2412172)
    EnableFlag(72410337)
    EnableAnimations(2410710)
    DisableBackread(2410703)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    Move(2410710, destination=2412173, destination_type=CoordEntityType.Region, set_draw_parent=0)
    SetNest(2410710, 2412173)
    DisableFlag(72410337)
    DisableAnimations(2410710)
    EnableBackread(2410703)
    Restart()

    # --- 1 --- #
    DefineLabel(1)
    DisableBackread(2410710)


@RestartOnRest
def Event12410661():
    """ 12410661: Event 12410661 """
    IfEventValueComparison(0, 12410646, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=4)
    EnableFlag(72410328)


@RestartOnRest
def Event12410662(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410662: Event 12410662 """
    EndIfThisEventSlotFlagEnabled()
    IfFlagEnabled(1, arg_0_3)
    IfFlagEnabled(1, 1142)
    IfFlagEnabled(2, arg_0_3)
    IfFlagEnabled(2, 1144)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    IncrementEventValue(12410646, bit_count=4, max_value=10)
    EnableFlag(arg_8_11)
    DisableFlagRange((72410331, 72410332))
    EnableFlag(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IncrementEventValue(12410646, bit_count=4, max_value=10)
    EnableFlag(arg_8_11)
    DisableFlagRange((72410331, 72410332))
    EnableFlag(72410334)


@RestartOnRest
def Event12410668():
    """ 12410668: Event 12410668 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 1163)
    IfFlagEnabled(1, 1204)
    IfFlagEnabled(1, 1268)
    IfFlagEnabled(1, 1190)
    IfFlagEnabled(1, 1223)
    IfFlagEnabled(1, 1309)
    IfFlagEnabled(1, 72410336)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((72410331, 72410332))
    EnableFlag(72410333)


@RestartOnRest
def Event12410669(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410669: Event 12410669 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EnableCharacter(arg_0_3)
    WaitFrames(1)
    ForceAnimation(arg_0_3, arg_8_11, loop=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_0_3)
    IfFlagEnabled(0, arg_4_7)
    EnableCharacter(arg_0_3)
    WaitFrames(1)
    ForceAnimation(arg_0_3, arg_8_11, loop=True)


@RestartOnRest
def Event12410676():
    """ 12410676: Event 12410676 """
    IfCharacterHuman(1, PLAYER)
    IfAttackedWithDamageType(1, attacked_entity=2410703, attacker=PLAYER)
    IfFlagEnabled(-1, 1141)
    IfFlagEnabled(-1, 1142)
    IfFlagEnabled(-1, 1144)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagRangeState(Label.L0, RangeState.AllOn, FlagType.Absolute, (72410344, 72410346))
    GotoIfFlagDisabled(Label.L3, 72410320)
    GotoIfFlagDisabled(Label.L2, 72410344)
    GotoIfFlagDisabled(Label.L1, 72410345)
    EnableFlag(72410346)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(72410345)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(72410344)

    # --- 3 --- #
    DefineLabel(3)
    EnableFlag(72410329)
    IfFlagDisabled(0, 72410329)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(72410329)
    SaveRequest()


def Event12410677():
    """ 12410677: Event 12410677 """
    EndIfFlagEnabled(1148)
    EndIfFlagEnabled(1149)
    IfFlagEnabled(1, 1146)
    IfAttacked(1, 2410711, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2410711, 103001)
    Kill(2410711, award_souls=True)
    DisableFlagRange((1140, 1159))
    EnableFlag(1149)
    SaveRequest()


def AggroEmissary(_, enemy: CharacterTyping):
    """ 12410680: Attack a Small Celestial Emissary and aggravate it. """
    IfAttacked(0, enemy, attacker=PLAYER)
    SetAIParamID(enemy, 250000)


def Event12410687(_, arg_0_3: int, arg_4_7: int):
    """ 12410687: Event 12410687 """
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_4_7)
    RunEvent(9350, 0, args=(1,))


def Event12410693(_, arg_0_3: int, arg_4_7: int):
    """ 12410693: Event 12410693 """
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(0, arg_4_7)
    RunEvent(9350, 0, args=(2,))


def Event12410700():
    """ 12410700: Event 12410700 """
    IfCharacterHuman(1, PLAYER)
    IfCharacterOutsideRegion(1, PLAYER, region=2412174)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(12410700)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2412174)
    IfConditionTrue(0, input_condition=1)
    Restart()


def Event12410701():
    """ 12410701: Event 12410701 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(9, 1261)
    IfFlagEnabled(9, 9800)
    GotoIfConditionFalse(Label.L8, input_condition=9)
    DisableFlagRange((1260, 1279))
    EnableFlag(1262)

    # --- 8 --- #
    DefineLabel(8)
    IfFlagEnabled(1, 1260)
    IfFlagEnabled(1, 9801)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableFlagRange((1260, 1279))
    EnableFlag(1270)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-1, 1260)
    IfFlagEnabled(-1, 1261)
    IfFlagEnabled(-1, 1262)
    IfConditionTrue(2, input_condition=-1)
    IfFlagEnabled(2, 9801)
    GotoIfConditionFalse(Label.L9, input_condition=2)
    DisableFlagRange((1260, 1279))
    EnableFlag(1263)

    # --- 9 --- #
    DefineLabel(9)
    IfFlagEnabled(10, 1263)
    IfFlagEnabled(-3, 9802)
    IfFlagEnabled(-3, 72410407)
    IfConditionTrue(10, input_condition=-3)
    GotoIfConditionFalse(Label.L1, input_condition=10)
    DisableFlagRange((1260, 1279))
    EnableFlag(1269)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 1264)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1260, 1279))
    EnableFlag(1267)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(4, 1265)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableFlagRange((1260, 1279))
    EnableFlag(1267)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(5, 1266)
    GotoIfConditionFalse(Label.L4, input_condition=5)
    DisableFlagRange((1260, 1279))
    EnableFlag(1268)

    # --- 4 --- #
    DefineLabel(4)
    IfFlagEnabled(6, 1270)
    IfFlagEnabled(-2, 9802)
    IfFlagEnabled(-2, 72410415)
    IfConditionTrue(6, input_condition=-2)
    GotoIfConditionFalse(Label.L7, input_condition=6)
    DisableFlagRange((1260, 1279))
    EnableFlag(1269)

    # --- 7 --- #
    DefineLabel(7)
    IfFlagEnabled(12, 9802)
    IfFlagEnabled(-4, 1267)
    IfConditionTrue(12, input_condition=-4)
    GotoIfConditionFalse(Label.L5, input_condition=12)
    DisableFlagRange((1260, 1279))
    EnableFlag(1271)

    # --- 5 --- #
    DefineLabel(5)
    IfFlagEnabled(7, 1272)
    GotoIfConditionFalse(Label.L6, input_condition=7)
    DisableFlagRange((1260, 1279))
    EnableFlag(1273)

    # --- 6 --- #
    DefineLabel(6)


def Event12410702():
    """ 12410702: Event 12410702 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    DisableFlag(72410414)

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(2410761)
    DisableHealthBar(2410762)
    EnableImmortality(2410762)
    GotoIfFlagEnabled(Label.L1, 1273)
    DisableObject(2410851)
    DisableTreasure(2410851)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableObject(2410851)
    EnableTreasure(2410851)
    PostDestruction(2410852)
    End()


def Event12410703():
    """ 12410703: Event 12410703 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, Flags.GascoigneFirstTimeDone)
    IfFlagEnabled(1, 1260)
    IfFlagEnabled(1, 72410413)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1260, 1279))
    EnableFlag(1261)


def Event12410704():
    """ 12410704: Event 12410704 """
    IfFlagEnabled(0, 72410403)
    DisableFlag(72410403)
    DisableFlagRange((1260, 1279))
    EnableFlag(1264)


def Event12410705():
    """ 12410705: Event 12410705 """
    IfFlagEnabled(0, 72410404)
    DisableFlag(72410404)
    DisableFlagRange((1260, 1279))
    EnableFlag(1265)


def Event12410706():
    """ 12410706: Event 12410706 """
    IfFlagEnabled(0, 72410405)
    DisableFlag(72410405)
    DisableFlagRange((1260, 1279))
    EnableFlag(1266)


def Event12410710():
    """ 12410710: Event 12410710 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72410406)
    DisableHealthBar(2410762)
    IfAttacked(0, 2410762, attacker=PLAYER)
    EnableFlag(72410406)
    Wait(2.0)
    Restart()


def Event12410713():
    """ 12410713: Event 12410713 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EnableFlag(72410410)
    IfFlagEnabled(-1, 1271)
    IfFlagEnabled(-1, 1267)
    IfConditionTrue(0, input_condition=-1)
    IfPlayerDoesNotHaveGood(1, 4904, including_box=False)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(72410410)


def Event12410715():
    """ 12410715: Event 12410715 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagDisabled(Label.L0, 1269)
    DisableSoundEvent(2413100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagDisabled(Label.L1, 72410402)
    DisableSoundEvent(2413100)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableSoundEvent(2413100)
    DisableFlag(72410412)
    IfFlagDisabled(1, 1270)
    IfFlagEnabled(1, 72410412)
    IfConditionTrue(0, input_condition=1)
    DisableSoundEvent(2413100)


def Event12410716():
    """ 12410716: Event 12410716 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L1, 1267)
    GotoIfFlagEnabled(Label.L1, 1268)
    GotoIfFlagEnabled(Label.L1, 1269)
    GotoIfFlagEnabled(Label.L1, 1273)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DeleteVFX(2413701, erase_root_only=False)


def Event12410721():
    """ 12410721: Event 12410721 """
    IfFlagEnabled(0, 72410421)
    DisableFlag(72410421)
    DisableFlagRange((1260, 1279))
    EnableFlag(1272)


@RestartOnRest
def Event12410729():
    """ 12410729: Event 12410729 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EnableImmortality(2410702)
    DisableHealthBar(2410702)
    IfFlagEnabled(1, 1120)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableBackread(2410702)
    DisableCharacter(2410700)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(2, 1121)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    EnableBackread(2410702)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(3, 1122)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    EnableBackread(2410702)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(4, 1123)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableBackread(2410702)
    DisableBackread(2410700)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(5, 1124)
    EndIfConditionFalse(5)
    DisableBackread(2410702)
    DisableBackread(2410700)


@RestartOnRest
def Event12410730():
    """ 12410730: Event 12410730 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, CommonFlags.HuntersDreamVisited)
    IfFlagEnabled(1, 1120)
    IfConditionTrue(0, input_condition=1)
    EnableBackread(2410702)
    DisableFlagRange((1120, 1124))
    EnableFlag(1121)


@RestartOnRest
def Event12410731():
    """ 12410731: Event 12410731 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 72410305)
    IfFlagEnabled(1, 1121)
    IfFlagEnabled(2, 1123)
    IfFlagEnabled(3, 1124)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionFalse(1)
    DisableFlagRange((1120, 1124))
    EnableFlag(1122)


@RestartOnRest
def Event12410732():
    """ 12410732: Event 12410732 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 72410309)
    IfFlagEnabled(-2, 1121)
    IfFlagEnabled(-2, 1122)
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(2, 1123)
    IfFlagEnabled(3, 1124)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionFalse(1)
    DisableBackread(2410702)
    DisableFlagRange((1120, 1124))
    EnableFlag(1123)


@RestartOnRest
def Event12410733():
    """ 12410733: Event 12410733 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 9800)
    DisableFlagRange((1120, 1124))
    EnableFlag(1124)
    DisableCharacter(2410700)
    DisableBackread(2410702)


@RestartOnRest
def Event12410734():
    """ 12410734: Event 12410734 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttacked(0, 2410702, attacker=PLAYER)
    EnableFlag(72410306)
    Wait(2.0)
    Restart()


def Event12410736():
    """ 12410736: Event 12410736 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 72410301)
    IfFlagDisabled(2, 72410301)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    DisableFlag(72410301)


def Event12410737():
    """ 12410737: Event 12410737 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableCharacter(2410700)
    IfFlagEnabled(-1, 1121)
    IfFlagEnabled(-1, 1122)
    IfFlagEnabled(-1, 1123)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacter(2410700)
    DisableAnimations(2410700)


def Event12410738():
    """ 12410738: Event 12410738 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, 72410311)
    IfCharacterBackreadDisabled(1, 2410700)
    IfFlagEnabled(1, 72410311)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    DisableFlag(72410311)
    Restart()


def Event12410739():
    """ 12410739: Event 12410739 """
    IfCharacterInsideRegion(1, PLAYER, region=2412170)
    IfFlagEnabled(-3, 1143)
    IfFlagRangeAnyEnabled(-3, (1145, 1149))
    IfConditionTrue(1, input_condition=-3)
    IfFlagEnabled(1, 9800)
    IfCharacterBackreadDisabled(1, 2410290)
    IfCharacterInsideRegion(2, PLAYER, region=2412171)
    IfFlagDisabled(2, 62411300)
    IfFlagEnabled(2, 1144)
    IfFlagEnabled(2, 9800)
    IfCharacterBackreadEnabled(2, 2410290)
    IfFlagEnabled(-2, 1141)
    IfFlagEnabled(-2, 1142)
    IfConditionTrue(3, input_condition=-2)
    IfCharacterBackreadEnabled(3, 2410290)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    EnableBackread(2410290)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2410290)
    Restart()


def Event12410740():
    """ 12410740: Event 12410740 """
    EndIfClient()
    GotoIfFlagEnabled(Label.L1, 1180)
    End()

    # --- 1 --- #
    DefineLabel(1)


def Event12410741():
    """ 12410741: Event 12410741 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 1180)
    IfFlagEnabled(1, 9802)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1180, 1199))
    EnableFlag(1195)
    SaveRequest()


def Event12410742():
    """ 12410742: Event 12410742 """
    IfFlagEnabled(0, 72410390)
    DisableFlag(72410390)
    DisableFlagRange((1180, 1199))
    EnableFlag(1193)


def Event12410743():
    """ 12410743: Event 12410743 """
    IfFlagEnabled(0, 72410391)
    DisableFlag(72410391)
    DisableFlagRange((1180, 1199))
    EnableFlag(1194)


def Event12410744():
    """ 12410744: Event 12410744 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, 1193)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1180, 1199))
    EnableFlag(1181)


def Event12410745():
    """ 12410745: Event 12410745 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, 1194)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1180, 1199))
    EnableFlag(1190)


def Event12410746():
    """ 12410746: Event 12410746 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagEnabled(Label.L0, 72410382)
    GotoIfFlagEnabled(Label.L0, 9802)
    DisableAI(2410111)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2410111)


def Event12410747():
    """ 12410747: Event 12410747 """
    IfEntityWithinDistance(-1, PLAYER, 2410111, radius=3.0)
    IfAttackedWithDamageType(-1, attacked_entity=2410111, attacker=-1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2410111)


def Event12410748():
    """ 12410748: Event 12410748 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72410393)
    IfCharacterInsideRegion(1, PLAYER, region=2412280)
    IfCharacterDead(1, 2410111)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(30)
    EnableFlag(72410393)
    IfCharacterOutsideRegion(0, PLAYER, region=2412280)
    DisableFlag(72410393)
    Restart()


def Event12410749():
    """ 12410749: Event 12410749 """
    IfCharacterBackreadEnabled(0, 2410111)
    IfHasAIStatus(-1, 2410111, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2410111, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, 2410111, ai_status=AIStatusType.Battle)
    GotoIfConditionFalse(Label.L0, input_condition=-1)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2410111, 3023, wait_for_completion=True)
    IfRandomFramesElapsed(0, min_frames=30, max_frames=60)
    Restart()


def Event12410750(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410750: Event 12410750 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, 72410382)
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


def Event12410760():
    """ 12410760: Event 12410760 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    DisableFlag(72410513)
    DisableFlag(72410514)
    DisableFlag(72410515)
    DisableFlag(72410516)

    # --- 0 --- #
    DefineLabel(0)
    DisableHealthBar(2410782)
    EnableImmortality(2410782)
    GotoIfFlagEnabled(Label.L1, 1240)
    GotoIfFlagEnabled(Label.L1, 1241)
    GotoIfFlagEnabled(Label.L1, 1242)
    GotoIfFlagEnabled(Label.L1, 1243)
    GotoIfFlagEnabled(Label.L1, 1244)
    GotoIfFlagEnabled(Label.L2, 1246)
    GotoIfFlagEnabled(Label.L3, 1245)
    DisableBackread(2410781)
    DeleteVFX(2413700, erase_root_only=False)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableBackread(2410781)
    End()

    # --- 2 --- #
    DefineLabel(2)
    EnableBackread(2410781)
    DestroyObject(2410784)
    DeleteVFX(2413700, erase_root_only=False)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(2410781)
    DestroyObject(2410784)
    DeleteVFX(2413700, erase_root_only=False)
    DropMandatoryTreasure(2410781)
    End()


def Event12410761():
    """ 12410761: Event 12410761 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(1, 2410781)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1240, 1259))
    EnableFlag(1245)
    SaveRequest()


def Event12410762():
    """ 12410762: Event 12410762 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1245)
    IfFlagEnabled(-1, 9800)
    IfFlagEnabled(-1, 9801)
    IfFlagEnabled(-1, 9802)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(1, 1240)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1240, 1259))
    EnableFlag(1241)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(-2, 9801)
    IfFlagEnabled(-2, 9802)
    IfConditionTrue(2, input_condition=-2)
    IfFlagEnabled(2, 1241)
    GotoIfConditionTrue(Label.L2, input_condition=2)
    Goto(Label.L3)

    # --- 2 --- #
    DefineLabel(2)
    DisableFlagRange((1240, 1259))
    EnableFlag(1242)

    # --- 3 --- #
    DefineLabel(3)
    IfFlagEnabled(3, 1242)
    IfFlagEnabled(3, 72410504)
    IfConditionTrue(-3, input_condition=3)
    IfFlagEnabled(-3, 9802)
    GotoIfConditionTrue(Label.L4, input_condition=-3)
    Goto(Label.L5)

    # --- 4 --- #
    DefineLabel(4)
    DisableFlagRange((1240, 1259))
    EnableFlag(1243)

    # --- 5 --- #
    DefineLabel(5)
    IfFlagEnabled(4, 9802)
    IfFlagEnabled(4, 1243)
    GotoIfConditionTrue(Label.L6, input_condition=4)
    End()

    # --- 6 --- #
    DefineLabel(6)
    DisableFlagRange((1240, 1259))
    EnableFlag(1246)


def Event12410763():
    """ 12410763: Event 12410763 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttackedWithDamageType(1, attacked_entity=2410782, attacker=-1)
    IfFlagEnabled(-1, 1240)
    IfFlagEnabled(-1, 1241)
    IfFlagEnabled(-1, 1242)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagRangeState(Label.L0, RangeState.AllOn, FlagType.Absolute, (72410515, 72410516))
    GotoIfFlagDisabled(Label.L2, 72410500)
    GotoIfFlagDisabled(Label.L1, 72410515)
    EnableFlag(72410516)

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(72410515)

    # --- 2 --- #
    DefineLabel(2)
    EnableFlag(72410513)
    IfFlagEnabled(0, 72410514)
    IfFlagDisabled(0, 72410514)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(72410513)
    DisableFlagRange((1240, 1259))
    EnableFlag(1244)
    SaveRequest()


def Event12410770(_, arg_0_3: int):
    """ 12410770: Event 12410770 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DisableCharacter(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, arg_0_3)
    WaitFrames(1)


@RestartOnRest
def Event12410780():
    """ 12410780: Event 12410780 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1293)
    GotoIfFlagEnabled(Label.L0, 12410785)
    DisableFlagRange((1280, 1299))
    EnableFlag(1290)
    Goto(Label.L9)

    # --- 0 --- #
    DefineLabel(0)
    DisableFlagRange((1280, 1299))
    EnableFlag(1291)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    SetDistanceLimitForConversationStateChanges(Characters.GascoigneHuman, distance=80.0)
    End()


@RestartOnRest
def Event12410785():
    """ 12410785: Event 12410785 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1293)
    IfFlagEnabled(1, 1290)
    IfFlagEnabled(1, 72410530)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1280, 1299))
    EnableFlag(1291)


@RestartOnRest
def Event12410786():
    """ 12410786: Event 12410786 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1293)
    IfFlagEnabled(-1, 1290)
    IfFlagEnabled(-1, 1291)
    IfFlagEnabled(1, Flags.GascoignePhaseTwo)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1290, 1299))
    EnableFlag(1292)


@RestartOnRest
def Event12410787():
    """ 12410787: Event 12410787 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, Flags.GascoigneDead)
    DisableFlagRange((1290, 1299))
    EnableFlag(1293)
    SetDistanceLimitForConversationStateChanges(Characters.GascoigneHuman, distance=17.0)
    SaveRequest()


def Event12410800():
    """ 12410800: Event 12410800 """
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1370, 1375))
    GotoIfFlagEnabled(Label.L1, 1369)
    GotoIfFlagEnabled(Label.L2, 1368)
    GotoIfFlagEnabled(Label.L3, 1367)
    GotoIfFlagEnabled(Label.L4, 1366)
    GotoIfFlagEnabled(Label.L5, 1365)
    GotoIfFlagEnabled(Label.L6, 1364)
    GotoIfFlagRangeState(Label.L7, RangeState.AnyOn, FlagType.Absolute, (1362, 1363))
    GotoIfFlagRangeState(Label.L8, RangeState.AnyOn, FlagType.Absolute, (1360, 1361))

    # --- 0 --- #
    DefineLabel(0)
    DisableBackread(2410900)
    Goto(Label.L9)

    # --- 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagDisabled(2, 1705)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 1704)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 1701)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(4, 1703)
    Move(2410900, destination=2412334, destination_type=CoordEntityType.Region, set_draw_parent=2414124)
    SetNest(2410900, 2412334)
    SetTeamType(2410900, TeamType.HostileNPC)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(4, 1702)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, set_draw_parent=2414122)
    SetNest(2410900, 2412332)
    SetTeamType(2410900, TeamType.HostileNPC)
    Goto(Label.L9)
    SetNest(2410900, 2412332)
    SetTeamType(2410900, TeamType.HostileNPC)
    Goto(Label.L9)

    # --- 2 --- #
    DefineLabel(2)
    SkipLinesIfFlagDisabled(2, 1705)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 1704)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(2, 1701)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(6, 1703)
    DisableBackread(2410900)
    DisableCharacter(2410900)
    Move(2410900, destination=2412334, destination_type=CoordEntityType.Region, set_draw_parent=2414124)
    WaitFrames(1)
    DropMandatoryTreasure(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagDisabled(6, 1702)
    DisableBackread(2410900)
    DisableCharacter(2410900)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, set_draw_parent=2414122)
    WaitFrames(1)
    DropMandatoryTreasure(2410900)
    Goto(Label.L9)
    DisableBackread(2410900)
    DisableCharacter(2410900)
    DropMandatoryTreasure(2410900)
    Goto(Label.L9)

    # --- 3 --- #
    DefineLabel(3)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, set_draw_parent=2414122)
    SetNest(2410900, 2412332)
    DisableFlag(72410546)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    Move(2410900, destination=2412334, destination_type=CoordEntityType.Region, set_draw_parent=2414124)
    SetNest(2410900, 2412334)
    DisableFlag(72410546)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, set_draw_parent=2414122)
    SetNest(2410900, 2412332)
    SetTeamType(2410900, TeamType.CoopNPC)
    EnableFlag(72410546)
    WaitFrames(2)
    AddSpecialEffect(2410900, 7608, affect_npc_part_hp=False)
    Goto(Label.L9)

    # --- 6 --- #
    DefineLabel(6)
    DisableCharacter(2410900)
    Goto(Label.L9)

    # --- 7 --- #
    DefineLabel(7)
    DisableBackread(2410900)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    ForceAnimation(2410900, 103030)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    Event12410801()
    Event12410803()
    Event12410804()
    Event12410805()
    Event12410806()
    Event12410807()
    Event12410808()


def Event12410801():
    """ 12410801: Event 12410801 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 1360)
    IfFlagEnabled(1, 72410540)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1361)


def Event12410803():
    """ 12410803: Event 12410803 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(1, 1363)
    IfCharacterDead(1, 2410901)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1366)


def Event12410804():
    """ 12410804: Event 12410804 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(-1, 1364)
    IfFlagEnabled(-1, 1365)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterDead(1, 2410901)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1367)


def Event12410805():
    """ 12410805: Event 12410805 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(0, 2410900)
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


def Event12410806():
    """ 12410806: Event 12410806 """
    EndIfThisEventFlagEnabled()
    IfCharacterAlive(1, 2410900)
    IfFlagEnabled(1, 72410544)
    IfConditionTrue(0, input_condition=1)
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
    EnableFlag(1369)
    SetTeamType(2410900, TeamType.HostileNPC)
    SaveRequest()


def Event12410807():
    """ 12410807: Event 12410807 """
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(-1, 1364)
    IfFlagDisabled(-1, 1365)
    IfConditionTrue(1, input_condition=-1)
    IfAttacked(1, 2410900, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    IfFlagDisabled(-2, 1364)
    IfFlagDisabled(-2, 1365)
    IfConditionTrue(2, input_condition=-2)
    IfAttacked(2, 2410900, attacker=PLAYER)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(1)
    IfFlagDisabled(-3, 1364)
    IfFlagDisabled(-3, 1365)
    IfConditionTrue(3, input_condition=-3)
    IfAttacked(3, 2410900, attacker=PLAYER)
    IfConditionTrue(0, input_condition=3)
    WaitFrames(1)


@RestartOnRest
def Event12410808():
    """ 12410808: Event 12410808 """
    IfFlagEnabled(0, 72410545)
    ReplanAI(2410900)
    AICommand(2410900, command_id=30, slot=0)
    IfFlagDisabled(-1, 72410545)
    IfHasAIStatus(-1, 2410900, ai_status=AIStatusType.Battle)
    IfEntityBeyondDistance(-1, 2410900, PLAYER, radius=5.0)
    IfConditionTrue(0, input_condition=-1)
    ReplanAI(2410900)
    AICommand(2410900, command_id=-1, slot=0)
    DisableFlag(72410545)
    Restart()


def Event12410809():
    """ 12410809: Event 12410809 """
    DisableBackread(2410901)
    EndIfFlagEnabled(12410810)
    EndIfFlagEnabled(1366)
    EndIfFlagEnabled(1367)
    EndIfFlagEnabled(9467)
    EndIfFlagEnabled(9802)
    IfFlagEnabled(-1, 1363)
    IfFlagEnabled(-1, 1364)
    IfFlagEnabled(-1, 1365)
    IfFlagEnabled(-2, 1701)
    IfFlagEnabled(-2, 1702)
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(-3, 1368)
    IfFlagEnabled(-3, 1369)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableBackread(2410901)


def Event12410810():
    """ 12410810: Event 12410810 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableBackread(2410901)
    DisableCharacter(2410901)
    DropMandatoryTreasure(2410901)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfHealthEqual(0, 2410901, 0.0)
    SetAIParamID(2410900, 6163)
    AICommand(2410900, command_id=11, slot=0)
    ClearTargetList(2410900)
    ReplanAI(2410900)
    IfCharacterDead(0, 2410901)
    EnableFlag(5912)
    SetTeamType(2410900, TeamType.FriendlyNPC)
    DisableFlag(72410546)
    SaveRequest()


@RestartOnRest
def Event12410811():
    """ 12410811: Event 12410811 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(-1, 1363)
    IfFlagEnabled(-1, 1364)
    IfConditionTrue(1, input_condition=-1)
    IfHasAIStatus(1, 2410901, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=1)
    EnableBackread(2410900)
    Move(
        2410900, destination=2412333, destination_type=CoordEntityType.Region, copy_draw_parent=2414123
    )
    SetNest(2410900, 2412334)
    SetTeamType(2410900, TeamType.CoopNPC)
    WaitFrames(2)
    ForceAnimation(2410900, 101290)
    AddSpecialEffect(2410900, 7608, affect_npc_part_hp=False)
    SetAIParamID(2410900, 6162)
    AICommand(2410900, command_id=10, slot=0)
    ReplanAI(2410900)
    DisableFlagRange((1360, 1379))
    EnableFlag(1365)
    IfCharacterInsideRegion(0, 2410900, region=2412334)
    AICommand(2410900, command_id=-1, slot=0)
    ReplanAI(2410900)


def Event12410812():
    """ 12410812: Event 12410812 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagDisabled(Label.L0, 1169)
    DisableFlagRange((1160, 1179))
    EnableFlag(1163)

    # --- 0 --- #
    DefineLabel(0)
    End()


def Event12410813():
    """ 12410813: Event 12410813 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagDisabled(Label.L0, 1314)
    DisableFlagRange((1300, 1319))
    EnableFlag(1309)

    # --- 0 --- #
    DefineLabel(0)
    End()


def Event12410814():
    """ 12410814: Event 12410814 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagDisabled(Label.L0, 1209)
    DisableFlagRange((1200, 1219))
    EnableFlag(1204)

    # --- 0 --- #
    DefineLabel(0)
    End()


def Event12410830():
    """ 12410830: Event 12410830 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    GotoIfFlagDisabled(Label.L2, 1233)
    DisableFlagRange((1220, 1239))
    EnableFlag(1223)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(2, 1228)
    IfFlagEnabled(2, 72400486)
    GotoIfConditionFalse(Label.L3, input_condition=2)
    DisableFlagRange((1220, 1239))
    EnableFlag(1229)

    # --- 3 --- #
    DefineLabel(3)

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(2410770)
    DisableCharacterCollision(2410770)
    GotoIfFlagEnabled(Label.L0, 1228)
    GotoIfFlagEnabled(Label.L0, 1229)
    GotoIfFlagEnabled(Label.L1, 1235)
    GotoIfFlagEnabled(Label.L2, 1236)
    DisableCharacter(2410770)
    DisableBackread(2410771)
    DisableObject(2411280)
    EnableObject(2411281)
    End()

    # --- 0 --- #
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

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    EzstateAIRequest(2410770, command_id=5, slot=1)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2410770)
    DropMandatoryTreasure(2410771)
    End()

    # --- 2 --- #
    DefineLabel(2)
    EnableBackread(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    EzstateAIRequest(2410770, command_id=4, slot=1)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, short_move=True)
    DropMandatoryTreasure(2410770)
    DropMandatoryTreasure(2410771)
    End()


def Event12410831():
    """ 12410831: Event 12410831 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1235)
    EndIfFlagEnabled(1236)
    IfCharacterDead(1, 2410770)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1220, 1239))
    EnableFlag(1235)
    SaveRequest()


def Event12410833():
    """ 12410833: Event 12410833 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(1235)
    EndIfFlagEnabled(1236)
    IfHealthEqual(1, 2410771, 0.0)
    IfHealthNotEqual(1, 2410770, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1220, 1239))
    EnableFlag(1236)
    WaitFrames(1)
    ForceAnimation(2410770, 103083)
    SaveRequest()


def Event12410834():
    """ 12410834: Event 12410834 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(10)
    IfFlagEnabled(-1, 1228)
    IfFlagEnabled(-1, 1229)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2412302)
    IfConditionTrue(0, input_condition=1)
    RunEvent(9350, 0, args=(3,))
    EnableFlag(72400956)


def Event12410835():
    """ 12410835: Event 12410835 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterBackreadEnabled(1, 2410770)
    IfFlagEnabled(1, 1228)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    DisableAI(2410771)
    ForceAnimation(2410770, 103082)
    ForceAnimation(2410771, 7010, loop=True)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, short_move=True)
    End()


def Event12410850(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410850: Event 12410850 """
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


def Event12410860(_, arg_0_3: int, arg_4_7: int):
    """ 12410860: Event 12410860 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, arg_4_7)
    Restart()


def Event12410870(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410870: Event 12410870 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, arg_0_3, arg_8_11)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, arg_4_7)
    WaitFrames(5)
    Restart()


def Event12410880(_, arg_0_3: int, arg_4_7: int):
    """ 12410880: Event 12410880 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, arg_4_7)


@RestartOnRest
def Event12415130(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12415130: Event 12415130 """
    EndIfThisEventSlotFlagEnabled()
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    SetAIParamID(arg_0_3, arg_16_19)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    SkipLinesIfValueEqual(1, left=0, right=arg_24_27)
    IfFlagEnabled(-1, arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomFrames(min_frames=0, max_frames=60)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    SetAIParamID(arg_0_3, arg_20_23)


@RestartOnRest
def Event12415150(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: int, arg_20_23: int):
    """ 12415150: Event 12415150 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    SetAIParamID(arg_0_3, arg_16_19)
    DisableGravity(arg_0_3)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, arg_8_11)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_20_23)
    EnableGravity(arg_0_3)


@RestartOnRest
def Event12410155(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410155: Event 12410155 """
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12410156(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410156: Event 12410156 """
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfHasAIStatus(-2, arg_4_7, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, arg_4_7, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, arg_4_7, ai_status=AIStatusType.Battle)
    IfConditionTrue(2, input_condition=-2)
    IfHasAIStatus(-3, arg_8_11, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-3, arg_8_11, ai_status=AIStatusType.Search)
    IfHasAIStatus(-3, arg_8_11, ai_status=AIStatusType.Battle)
    IfConditionTrue(3, input_condition=-3)
    IfConditionTrue(-15, input_condition=1)
    IfConditionTrue(-15, input_condition=2)
    IfConditionTrue(-15, input_condition=3)
    IfConditionTrue(0, input_condition=-15)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)

    # --- 0 --- #
    DefineLabel(0)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SetNest(arg_0_3, 2412225)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(-4, arg_0_3, region=2412225)
    IfHasAIStatus(-4, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-4)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    End()

    # --- 2 --- #
    DefineLabel(2)
    SetNest(arg_0_3, 2412226)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(-5, arg_0_3, region=2412226)
    IfHasAIStatus(-5, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-5)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    End()


def Event12410321(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12410321: Event 12410321 """
    EndIfFlagEnabled(arg_0_3)
    GotoIfFlagEnabled(Label.L0, arg_12_15)
    DisableFlag(arg_4_7)
    DisableFlag(arg_8_11)
    EndOfAnimation(arg_16_19, 2)
    DisableObjectActivation(arg_20_23, obj_act_id=100)
    DisableObjectActivation(arg_24_27, obj_act_id=100)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, arg_4_7)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(arg_8_11)
    EndOfAnimation(arg_16_19, 2)
    EnableObjectActivation(arg_20_23, obj_act_id=100)
    DisableObjectActivation(arg_24_27, obj_act_id=100)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_8_11)
    EndOfAnimation(arg_16_19, 0)
    DisableObjectActivation(arg_20_23, obj_act_id=100)
    EnableObjectActivation(arg_24_27, obj_act_id=100)


def Event12410325(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410325: Event 12410325 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, arg_12_15)
    IfFlagEnabled(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, arg_4_7)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(arg_8_11)
    SkipLines(1)
    EnableFlag(arg_8_11)
    IfCharacterHuman(3, PLAYER)
    IfFlagEnabled(3, arg_12_15)
    IfFlagDisabled(3, arg_0_3)
    IfConditionTrue(0, input_condition=3)
    Restart()


def Event12410322(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12410322: Event 12410322 """
    IfFlagEnabled(3, arg_0_3)
    IfFlagEnabled(3, arg_4_7)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    EndOfAnimation(2411320, 3)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, arg_12_15)
    IfFlagDisabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfObjectActivated(-1, obj_act_id=arg_20_23)
    IfFlagChange(2, arg_8_11)
    IfFlagEnabled(2, arg_8_11)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    EnableFlag(arg_4_7)
    ForceAnimation(2411320, 6, wait_for_completion=True)
    ForceAnimation(2411320, 3, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=2412321)
    ForceAnimation(2411320, 7, wait_for_completion=True)
    DisableObjectActivation(2411317, obj_act_id=100)
    EnableObjectActivation(2411318, obj_act_id=100)
    DisableFlag(arg_0_3)
    Restart()


def Event12410323(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12410323: Event 12410323 """
    IfFlagEnabled(3, arg_0_3)
    IfFlagDisabled(3, arg_4_7)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    EndOfAnimation(2411320, 1)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, arg_12_15)
    IfFlagDisabled(1, arg_0_3)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfObjectActivated(-1, obj_act_id=arg_20_23)
    IfFlagChange(2, arg_8_11)
    IfFlagDisabled(2, arg_8_11)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)
    DisableFlag(arg_4_7)
    ForceAnimation(2411320, 4, wait_for_completion=True)
    ForceAnimation(2411320, 1, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=2412322)
    ForceAnimation(2411320, 5, wait_for_completion=True)
    EnableObjectActivation(2411317, obj_act_id=100)
    DisableObjectActivation(2411318, obj_act_id=100)
    DisableFlag(arg_0_3)
    Restart()


def Event12410324(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12410324: Event 12410324 """
    DisableNetworkSync()
    IfFlagDisabled(1, arg_8_11)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=arg_12_15)
    IfFlagDisabled(2, arg_8_11)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=arg_16_19)
    IfFlagEnabled(3, arg_0_3)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=arg_12_15)
    IfFlagEnabled(4, arg_0_3)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=arg_16_19)
    IfFlagEnabled(5, arg_4_7)
    IfActionButtonParamActivated(5, action_button_id=7100, entity=arg_12_15)
    IfFlagDisabled(6, arg_4_7)
    IfActionButtonParamActivated(6, action_button_id=7100, entity=arg_16_19)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event12410330(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410330: Event 12410330 """
    EndIfFlagEnabled(arg_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    EnableObjectActivation(arg_8_11, obj_act_id=100)
    DisableObjectActivation(arg_12_15, obj_act_id=100)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(arg_0_3)


def Event12410460(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12410460: Event 12410460 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    SetAIParamID(arg_0_3, arg_12_15)
    DisableGravity(arg_0_3)
    IfHasAIStatus(1, arg_20_23, ai_status=AIStatusType.Battle)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableGravity(arg_0_3)
    SkipLinesIfFinishedConditionTrue(2, 2)
    WaitRandomFrames(min_frames=20, max_frames=100)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event12414450(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12414450: Event 12414450 """
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
def Event12414470():
    """ 12414470: Event 12414470 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(1, 12414420)
    IfFlagDisabled(1, 12414430)
    IfCharacterInsideRegion(-1, 2410158, region=2412705)
    IfCharacterInsideRegion(-1, 2410158, region=2412706)
    IfCharacterInsideRegion(-1, 2410158, region=2412707)
    IfCharacterInsideRegion(-1, 2410158, region=2412708)
    IfCharacterInsideRegion(-1, 2410158, region=2412709)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2410158, command_id=992, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414480():
    """ 12414480: Event 12414480 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHasTAEEvent(0, 2410158, tae_event_id=1000)

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(2410158)
    SendNPCSummonHome(2410158)


@RestartOnRest
def Event12414490():
    """ 12414490: Event 12414490 """
    DisableNetworkSync()
    IfHost(1)
    IfFlagEnabled(1, 12414421)
    IfFlagDisabled(1, 12414431)
    IfFlagEnabled(1, Flags.ClericBeastFogEntered)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect_WithUnknownEffect(2410740, 35, affect_npc_parts_hp=False)
    WaitFrames(1)
    Restart()


@RestartOnRest
def Event12414400(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12414400: Event 12414400 """
    GotoIfFlagEnabled(Label.L0, arg_0_3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagDisabled(1, Flags.GascoigneFirstTimeDone)
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
    IfFlagDisabled(2, Flags.GascoigneFirstTimeDone)
    IfFlagDisabled(-3, arg_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(arg_0_3)
    DeleteVFX(arg_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12414401(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12414401: Event 12414401 """
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
def Event12414410(
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
    """ 12414410: Event 12414410 """
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
def Event12414460(
    _, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, arg_24_27: int
):
    """ 12414460: Event 12414460 """
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
def Event12414500():
    """ 12414500: Event 12414500 """
    # TODO: Unused.
    GotoIfThisEventFlagDisabled(Label.L0)
    SetBackreadStateAlternate(2410740, state=True)
    AddSpecialEffect(2410740, 9006, affect_npc_part_hp=False)
    EnableCharacter(2410740)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2410740)
    DisableAI(2410740)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    SetNetworkUpdateAuthority(2410740, UpdateAuthority.Forced)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12414608)
    IfCharacterInsideRegion(2, PLAYER, region=2412722)
    IfCharacterInsideRegion(3, PLAYER, region=2412723)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfFlagEnabled(1, 72400461)  # TODO: Cathedral Ward dialogue flag?
    IfFlagRangeAnyEnabled(1, (1340, 1341))
    IfConditionTrue(0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    Move(2410740, destination=2412720, destination_type=CoordEntityType.Region, set_draw_parent=0)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    Move(2410740, destination=2412721, destination_type=CoordEntityType.Region, set_draw_parent=2414021)

    # --- 2 --- #
    DefineLabel(2)
    Wait(5.0)
    EnableFlag(12414506)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.f_MenuEffect, sound_id=100000009)
    Wait(5.0)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.f_MenuEffect, sound_id=100000020)
    SetBackreadStateAlternate(2410740, state=True)
    AddSpecialEffect(2410740, 9006, affect_npc_part_hp=False)
    EnableCharacter(2410740)
    ForceAnimation(2410740, 101201, wait_for_completion=True)
    EnableAI(2410740)
    DisableMapCollision(2414200)


@RestartOnRest
def Event12414501():
    """ 12414501: Event 12414501 """
    # TODO: Unused.
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(Flags.ClericBeastDead)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 12414502)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2410740)
    SetBackreadStateAlternate(2410740, state=False)


@RestartOnRest
def Event12414502():
    """ 12414502: Event 12414502 """
    # TODO: Unused. Character 2410740 disappears given certain flags.
    EndIfFlagEnabled(Flags.ClericBeastDead)
    EndIfFlagEnabled(12414501)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 12414500)
    IfFlagDisabled(1, 12414501)
    IfFlagEnabled(1, Flags.ClericBeastDead)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2410740, command_id=991, slot=0)
    ReplanAI(2410740)
    Wait(1.0)
    AddSpecialEffect(2410740, 5560, affect_npc_part_hp=False)
    CreateTemporaryVFX(121, anchor_entity=2410740, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(2.0)
    DisableCharacter(2410740)


@RestartOnRest
def Event12414503():
    """ 12414503: Event 12414503 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagEnabled(Flags.ClericBeastDead)
    EndIfFlagEnabled(12414501)
    EndIfFlagEnabled(12414505)
    EndIfThisEventFlagEnabled()
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfFlagEnabled(1, 12414500)
    IfFlagDisabled(1, 12414501)
    IfFlagEnabled(1, Flags.ClericBeastFirstTimeDone)
    IfFlagEnabled(1, Flags.ClericBeastFogEntered)
    IfCharacterOutsideRegion(1, 2410740, region=2412801)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    SetEventPoint(2410740, region=2412710, reaction_range=1.0)
    AICommand(2410740, command_id=990, slot=0)
    ReplanAI(2410740)


@RestartOnRest
def Event12414504():
    """ 12414504: Event 12414504 """
    EndIfFlagEnabled(Flags.ClericBeastDead)
    EndIfFlagEnabled(12414501)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 12414503)
    IfCharacterInsideRegion(1, 2410740, region=2412710)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(2410740, disable_interpolation=False)
    RotateToFaceEntity(2410740, 2412800, animation=101130, wait_for_completion=True)
    AICommand(2410740, command_id=-1, slot=0)
    ReplanAI(2410740)


@RestartOnRest
def Event12414505():
    """ 12414505: Event 12414505 """
    DisableSoapstoneMessage(2413221)
    DisableSoapstoneMessage(2413223)
    DeleteVFX(2413231, erase_root_only=False)
    DeleteVFX(2413233, erase_root_only=False)
    EndIfThisEventFlagEnabled()
    IfPlayerHasGood(1, 200, including_box=False)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfFlagEnabled(1, 72400461)
    IfFlagRangeAnyEnabled(1, (1340, 1341))
    IfConditionTrue(0, input_condition=1)
    EnableSoapstoneMessage(2413221)
    EnableSoapstoneMessage(2413223)
    CreateVFX(2413231)
    CreateVFX(2413233)
    IfFlagEnabled(-1, 12414506)
    IfFlagEnabled(-1, Flags.ClericBeastDead)
    IfConditionTrue(0, input_condition=-1)
    DisableSoapstoneMessage(2413221)
    DisableSoapstoneMessage(2413223)
    DeleteVFX(2413231, erase_root_only=True)
    DeleteVFX(2413233, erase_root_only=True)


@RestartOnRest
def Event12414600():
    """ 12414600: Event 12414600 """
    GotoIfThisEventFlagDisabled(Label.L0)
    SetBackreadStateAlternate(2410158, state=True)
    AddSpecialEffect(2410158, 9006, affect_npc_part_hp=False)
    EnableCharacter(2410158)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2410158)
    DisableAI(2410158)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    SetNetworkUpdateAuthority(2410158, UpdateAuthority.Forced)
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 12414608)
    IfCharacterInsideRegion(2, PLAYER, region=2412700)
    IfCharacterInsideRegion(3, PLAYER, region=2412701)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfFlagDisabled(1, Flags.GascoigneFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    Move(2410158, destination=2412702, destination_type=CoordEntityType.Region, set_draw_parent=2414020)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    Move(2410158, destination=2412703, destination_type=CoordEntityType.Region, set_draw_parent=2414021)

    # --- 2 --- #
    DefineLabel(2)
    Wait(5.0)
    EnableFlag(12414609)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.f_MenuEffect, sound_id=100000009)
    Wait(5.0)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.f_MenuEffect, sound_id=100000020)
    SetBackreadStateAlternate(2410158, state=True)
    AddSpecialEffect(2410158, 9006, affect_npc_part_hp=False)
    EnableCharacter(2410158)
    ForceAnimation(2410158, 7010, wait_for_completion=True)
    EnableAI(2410158)
    DisableMapCollision(2414200)


@RestartOnRest
def Event12414601():
    """ 12414601: Event 12414601 """
    GotoIfThisEventFlagEnabled(Label.L0)
    IfCharacterHasTAEEvent(0, 2410158, tae_event_id=1000)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(2410158)
    SetBackreadStateAlternate(2410158, state=False)
    EnableMapCollision(2414200)


@RestartOnRest
def Event12414602():
    """ 12414602: Event 12414602 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(1, 12414600)
    IfFlagDisabled(1, 12414601)
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfFlagDisabled(1, Flags.GascoigneFirstTimeDone)
    IfCharacterDead(1, Characters.ClericBeast)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2410158, command_id=991, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414603():
    """ 12414603: Event 12414603 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(1, 12414600)
    IfFlagDisabled(1, 12414601)
    IfCharacterInsideRegion(-1, 2410158, region=2412705)
    IfCharacterInsideRegion(-1, 2410158, region=2412706)
    IfCharacterInsideRegion(-1, 2410158, region=2412707)
    IfCharacterInsideRegion(-1, 2410158, region=2412708)
    IfCharacterInsideRegion(-1, 2410158, region=2412709)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(2410158, command_id=992, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414604():
    """ 12414604: Event 12414604 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, Flags.ClericBeastFirstTimeDone)
    IfFlagEnabled(1, Flags.ClericBeastFogEntered)
    IfCharacterOutsideRegion(1, 2410158, region=2412801)
    IfConditionTrue(0, input_condition=1)
    SetEventPoint(2410158, region=2412710, reaction_range=1.0)
    AICommand(2410158, command_id=990, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414605():
    """ 12414605: Event 12414605 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 12414604)
    IfCharacterInsideRegion(1, 2410158, region=2412710)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(2410158, disable_interpolation=False)
    RotateToFaceEntity(2410158, 2412800, animation=7014, wait_for_completion=True)
    AICommand(2410158, command_id=-1, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414606():
    """ 12414606: Event 12414606 """
    DisableSoapstoneMessage(2413220)
    DisableSoapstoneMessage(2413222)
    DeleteVFX(2413230, erase_root_only=False)
    DeleteVFX(2413232, erase_root_only=False)
    EndIfThisEventFlagEnabled()
    IfPlayerHasGood(1, 200, including_box=False)
    IfCharacterHuman(1, PLAYER)
    IfFlagDisabled(1, Flags.ClericBeastDead)
    IfFlagDisabled(1, Flags.GascoigneFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableSoapstoneMessage(2413220)
    EnableSoapstoneMessage(2413222)
    CreateVFX(2413230)
    CreateVFX(2413232)
    IfFlagEnabled(-1, 12414609)
    IfFlagEnabled(-1, Flags.ClericBeastDead)
    IfFlagEnabled(-1, Flags.GascoigneFirstTimeDone)
    IfConditionTrue(0, input_condition=-1)
    DisableSoapstoneMessage(2413220)
    DisableSoapstoneMessage(2413222)
    DeleteVFX(2413230, erase_root_only=True)
    DeleteVFX(2413232, erase_root_only=True)


@RestartOnRest
def Event12414607():
    """ 12414607: Event 12414607 """
    IfCharacterHuman(1, PLAYER)
    IfCharacterHasSpecialEffect(1, PLAYER, 9000)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(12414608)
    WaitFrames(1)
    DisableFlag(12414608)
    IfCharacterHuman(2, PLAYER)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 9000)
    IfConditionTrue(0, input_condition=2)
    Restart()


@RestartOnRest
def Event12414610():
    """ 12414610: Event 12414610 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 12414600)
    IfFlagDisabled(1, 12414601)
    IfHealthGreaterThan(1, 2410158, 0.0)
    IfCharacterHasSpecialEffect(1, 2410158, Effects.MusicBox)
    IfConditionTrue(0, input_condition=1)
    Wait(2.0)
    IfFlagEnabled(2, 12414600)
    IfFlagDisabled(2, 12414601)
    IfHealthGreaterThan(2, 2410158, 0.0)
    EndIfConditionFalse(2)
    PlaySoundEffect(anchor_entity=2410158, sound_type=SoundType.v_Voice, sound_id=242100402)


def Event12410220(_, arg_0_3: int, arg_4_7: float):
    """ 12410220: Event 12410220 """
    DisableAI(arg_0_3)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)


def Event12410234():
    """ 12410234: Event 12410234 """
    IfCharacterDead(0, 2410158)
    End()


def Event12410237(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 12410237: Event 12410237 """
    DisableCharacter(arg_12_15)
    IfFlagEnabled(0, arg_0_3)
    IfHealthLessThanOrEqual(-1, arg_4_7, 0.5)
    IfTimeElapsed(-1, 40.0)
    IfFlagEnabled(1, 12410235)
    IfCharacterAlive(1, arg_8_11)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EndIfFlagEnabled(Flags.GascoigneDead)
    DisableCharacter(arg_8_11)
    EnableCharacter(arg_12_15)
    Wait(1.0)
    SetNest(arg_12_15, arg_16_19)
    AICommand(arg_12_15, command_id=10, slot=0)
    ReplanAI(arg_12_15)
    DisableGravity(arg_12_15)
    DisableCharacterCollision(arg_12_15)
    DisableAnimations(arg_12_15)
    IfEntityWithinDistance(-2, arg_12_15, Characters.GascoigneHuman, radius=3.0)
    IfCharacterInsideRegion(-2, arg_12_15, region=2412811)
    IfConditionTrue(0, input_condition=-2)
    AICommand(arg_12_15, command_id=-1, slot=0)
    ClearTargetList(arg_12_15)
    ReplanAI(arg_12_15)
    EnableCharacterCollision(arg_12_15)
    EnableAnimations(arg_12_15)
    EnableGravity(arg_12_15)


def Event12410238():
    """ 12410238: Event 12410238 """
    IfFlagEnabled(-1, 12410234)
    IfFlagEnabled(-1, Flags.GascoigneFirstTimeDone)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(10)
    DisableCharacter(2410158)


def Event12410239(_, arg_0_3: int):
    """ 12410239: Event 12410239 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(5)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-2)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(5)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-3)
    IfAttackedWithDamageType(3, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=3)
    WaitFrames(5)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterType(-4, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(4, input_condition=-4)
    IfAttackedWithDamageType(4, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=4)
    WaitFrames(5)

    # --- 0 --- #
    DefineLabel(0)
    StopEvent(12415234)
    DisableFlag(12415234)
    RemoveSpecialEffect(arg_0_3, 5590)
    SetTeamType(arg_0_3, TeamType.Indiscriminate)


def Event12410240(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 12410240: Event 12410240 """
    WaitRandomSeconds(min_seconds=arg_8_11, max_seconds=arg_12_15)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    Restart()


def Event12410285(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410285: Event 12410285 """
    SkipLinesIfThisEventSlotFlagDisabled(7)
    EndOfAnimation(arg_8_11, 2)
    Wait(1.0)
    RegisterLadder(start_climbing_flag=arg_0_3, stop_climbing_flag=arg_4_7, obj=arg_8_11)
    DisableObjectActivation(arg_12_15, obj_act_id=2410000)
    IfActionButtonParamActivated(0, action_button_id=7100, entity=arg_12_15)
    DisplayDialog(
        10010172,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()
    IfObjectActivated(0, obj_act_id=12410206)
    ForceAnimation(arg_8_11, 1)
    WaitFrames(40)
    ForceAnimation(arg_8_11, 2)
    RegisterLadder(start_climbing_flag=arg_0_3, stop_climbing_flag=arg_4_7, obj=arg_8_11)
    Restart()


def Event12410287(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410287: Event 12410287 """
    SkipLinesIfThisEventSlotFlagDisabled(2)
    CreateObjectVFX(8028, obj=arg_0_3, model_point=100)
    End()
    CreateObjectVFX(8029, obj=arg_0_3, model_point=100)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    ForceAnimation(arg_0_3, 1000000)
    WaitFrames(30)
    DeleteObjectVFX(arg_0_3, erase_root=True)
    CreateObjectVFX(8028, obj=arg_0_3, model_point=100)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.a_Ambient, sound_id=600000000)
    CreatePlayLog(arg_8_11)


def Event12410340(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410340: Event 12410340 """
    IfCharacterInsideRegion(0, PLAYER, region=arg_12_15)
    SetNest(arg_0_3, arg_4_7)
    AICommand(arg_0_3, command_id=arg_8_11, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(-1, arg_0_3, region=arg_4_7)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12410370():
    """ 12410370: Event 12410370 """
    IfCharacterDead(-10, 2410028)
    IfCharacterDead(-10, 2410030)
    GotoIfConditionTrue(Label.L0, input_condition=-10)
    IfObjectDestroyed(10, 2411221)
    GotoIfConditionTrue(Label.L0, input_condition=10)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(2411220)
    PostDestruction(2411221)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableObject(2411221)
    ForceAnimation(2411220, 0)
    IfCharacterInsideRegion(1, PLAYER, region=2412210)
    IfCharacterInsideRegion(2, PLAYER, region=2412211)
    IfFlagEnabled(3, 12415371)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(12415371)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    IfEntityWithinDistance(-3, 2411220, PLAYER, radius=10.0)
    IfRandomTimeElapsed(-3, min_seconds=4.0, max_seconds=12.0)
    IfAttacked(-3, 2410028, attacker=PLAYER)
    IfAttacked(-3, 2410030, attacker=PLAYER)
    IfConditionTrue(0, input_condition=-3)

    # --- 2 --- #
    DefineLabel(2)
    ForceAnimation(2410028, 3008)
    ForceAnimation(2410030, 3009)
    WaitFrames(40)
    EnableInvincibility(2410028)
    EnableInvincibility(2410030)
    CreateObjectVFX(900260, obj=2411220, model_point=100)
    CreateHazard(
        12410376,
        2411220,
        model_point=100,
        behavior_param_id=6111,
        target_type=DamageTargetType.Character,
        radius=1.600000023841858,
        life=9999.0,
        repetition_time=0.0,
    )
    ForceAnimation(2411220, 1)
    WaitFrames(6)
    DisableInvincibility(2410028)
    DisableInvincibility(2410030)
    WaitFrames(206)
    RemoveObjectFlag(12410376)
    DeleteObjectVFX(2411220, erase_root=True)
    EnableObject(2411221)
    DisableObject(2411220)
    DestroyObject(2411221)


@RestartOnRest
def Event12415372(_, arg_0_3: int):
    """ 12415372: Event 12415372 """
    IfFlagEnabled(0, 12415371)
    EnableFlag(12415371)
    SetNest(arg_0_3, 2412212)
    AICommand(arg_0_3, command_id=10, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterInsideRegion(-1, arg_0_3, region=2412212)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event12410378(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12410378: Event 12410378 """
    SkipLinesIfThisEventSlotFlagDisabled(3)
    EndOfAnimation(arg_8_11, 2)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    End()
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=2412031)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    WaitRandomFrames(min_frames=50, max_frames=70)
    IfHealthValueLessThanOrEqual(0, arg_0_3, 2)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, wait_for_completion=True, skip_transition=True)
    WaitFrames(76)
    IfHealthValueLessThanOrEqual(0, arg_0_3, 2)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, wait_for_completion=True, skip_transition=True)
    WaitRandomFrames(min_frames=76, max_frames=100)
    IfHealthValueLessThanOrEqual(0, arg_0_3, 2)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    EnableInvincibility(arg_0_3)
    DisableImmortality(arg_0_3)
    RemoveSpecialEffect(arg_0_3, 5915)
    ForceAnimation(arg_8_11, 1)
    ForceAnimation(arg_0_3, 3001)
    WaitFrames(16)
    EnableAI(arg_0_3)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    DisableInvincibility(arg_0_3)


@RestartOnRest
def Event12410380(_, arg_0_3: int, arg_4_7: int):
    """ 12410380: Event 12410380 """
    DisableAI(arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=2412031)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    WaitRandomFrames(min_frames=55, max_frames=200)
    IfHealthValueGreaterThanOrEqual(2, arg_0_3, 1)
    SkipLinesIfConditionTrue(2, 2)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, wait_for_completion=True, skip_transition=True)
    Restart()
    End()


@RestartOnRest
def Event12410384(_, arg_0_3: int):
    """ 12410384: Event 12410384 """
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    Kill(arg_0_3, award_souls=True)


def Event12410490(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12410490: Event 12410490 """
    SkipLinesIfFlagDisabled(2, 100)
    DisableFlag(100)
    DisableFlag(arg_8_11)
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    PostDestruction(arg_0_3)
    ForceAnimation(arg_4_7, 2)
    EnableTreasure(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    CreateObjectVFX(900201, obj=arg_4_7, model_point=90)
    ForceAnimation(arg_4_7, 0)
    IfObjectDestroyed(0, arg_0_3)
    ForceAnimation(arg_4_7, 1, wait_for_completion=True)
    DeleteObjectVFX(arg_4_7, erase_root=True)
    EnableTreasure(arg_4_7)
    EnableFlag(arg_8_11)
    IfFlagEnabled(0, 100)
    RestoreObject(arg_0_3)
    ForceAnimation(arg_4_7, 0)
    DisableTreasure(arg_4_7)
    Restart()


def Event12410990():
    """ 12410990: Event 12410990 """
    EndIfThisEventFlagEnabled()
    IfPlayerStandingOnCollision(0, 2413500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 148, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 148, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 148, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 148, PlayLogMultiplayerType.HostOnly)


def Event12410995():
    """ 12410995: Event 12410995 """
    EndIfThisEventFlagEnabled()
    EndIfClient()
    IfPlayerStandingOnCollision(1, 2414110)
    IfCharacterOutsideRegion(1, PLAYER, region=2412900)
    IfConditionTrue(0, input_condition=1)
    RunEvent(9350, 0, args=(1,))


@RestartOnRest
def Event12415010(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float):
    """ 12415010: Event 12415010 """
    DisableNetworkSync()
    Wait(arg_12_15)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=arg_4_7, sound_id=arg_8_11)
    WaitFrames(440)
    IfFlagDisabled(1, 9801)
    IfFlagDisabled(1, 9802)
    SkipLinesIfConditionTrue(1, 1)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=arg_4_7, sound_id=arg_8_11)
    Restart()
