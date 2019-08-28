"""
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
174: N:\\SPRJ\\data\\Param\\event\\common.events
250: 
252: 
254: 
"""
from soulstruct.events.bloodborne import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=15, args=(2410950, 2411950, 9401, 12417800))
    RunEvent(7000, slot=16, args=(2410951, 2411951, 999, 12417820))
    RunEvent(7000, slot=17, args=(2410952, 2411952, 12411700, 12417840))
    RunEvent(7000, slot=18, args=(2410953, 2411953, 12411800, 12417860))
    RunEvent(12411010)
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
    RunEvent(9220, slot=3, args=(2410750, 12414220, 12414221, 2410, 24, 1), arg_types='iiiiBB')
    RunEvent(9240, slot=3, args=(2410750, 12414220, 12414221, 12414222, 24, 1), arg_types='iiiiBB')
    RunEvent(9260, slot=3, args=(2410750, 12414220, 12414221, 12414222, 24, 1), arg_types='iiiiBB')
    RunEvent(9280, slot=3, args=(2410750, 12414220, 12414221, 2410, 12414223, 24, 1), arg_types='iiiiiBB')
    RunEvent(12411899)
    RunEvent(12410310)
    CreateObjectFX(900130, obj=2411000, model_point=200)
    CreateObjectFX(900130, obj=2411001, model_point=200)
    CreateObjectFX(900130, obj=2411004, model_point=200)
    DeleteFX(2413230, erase_root_only=False)
    DeleteFX(2413233, erase_root_only=False)
    RunEvent(12414400, slot=0, args=(12414440, 2413230, 12414420, 12414430, 12411700, 6001))
    RunEvent(12414401, slot=0, args=(12414441, 2413233, 12414421, 12414431, 12411700, 6001))
    RunEvent(12414410, slot=0, args=(7, 2410158, 2412920, 12414420, 12414430, 12414440, 12411700, 10575))
    RunEvent(12414410, slot=1, args=(0, 2410740, 2412921, 12414421, 12414431, 12414441, 12411700, 10576))
    RunEvent(12414450, slot=0, args=(2410158, 2412710, 12414420, 12414430, 12414700))
    RunEvent(12414450, slot=1, args=(2410740, 2412711, 12414421, 12414431, 12414700))
    RunEvent(12414460, slot=0, args=(2410158, 2412710, 2412800, 2412801, 7014, 12414450, 2412801))
    RunEvent(12414460, slot=1, args=(2410740, 2412711, 2412800, 2412801, 101130, 12414451, 2412801))
    RunEvent(12414470)
    RunEvent(12414480)
    RunEvent(12414490)
    GotoIfFlagOff(Label.L0, 12410999)
    EnableFlag(9400)
    EnableFlag(9401)
    AddSpecialEffect(2410015, 5591, affect_npc_part_hp=False)
    Label(0)
    GotoIfFlagOff(Label.L1, 12410999)
    RunEvent(12410286, slot=0, args=(12410400, 12410401, 2411204, 2411316))
    RunEvent(12410820)
    Label(1)
    StartPlayLogMeasurement(2410000, 0, overwrite=False)
    StartPlayLogMeasurement(2410001, 18, overwrite=True)
    RunEvent(12410990)
    RunEvent(12410900)
    RunEvent(12415060, slot=0, args=(2410112, 2412000, 2412001, 4.0), arg_types='iiif')
    RunEvent(12415060, slot=1, args=(2410113, 2412000, 2412001, 4.0), arg_types='iiif')
    RunEvent(12415060, slot=2, args=(2410114, 2412000, 2412001, 4.0), arg_types='iiif')
    RunEvent(12415060, slot=3, args=(2410115, 2412000, 2412001, 4.0), arg_types='iiif')
    RunEvent(12415060, slot=4, args=(2410116, 2412000, 2412001, 4.0), arg_types='iiif')
    RunEvent(12415060, slot=10, args=(2410121, 2412120, 0, 4.0), arg_types='iiif')
    RunEvent(12415060, slot=11, args=(2410125, 2412120, 0, 4.0), arg_types='iiif')
    RunEvent(12415060, slot=12, args=(2410126, 2412120, 0, 4.0), arg_types='iiif')
    RunEvent(12415060, slot=13, args=(2410127, 2412120, 0, 4.0), arg_types='iiif')
    RunEvent(12415060, slot=15, args=(2410161, 2412120, 0, 4.0), arg_types='iiif')
    RunEvent(12415080, slot=3, args=(2410178, 7010, 7011, 2412154, 263496, 263431, 2.0), arg_types='iiiiiif')
    RunEvent(12415460, slot=0, args=(2410019, 7020, 7021, 2412251, 1.0, 2412010, 2411219), arg_types='iiiifii')
    RunEvent(12415461, slot=0, args=(2411219, 0, 1))
    RunEvent(12410160, slot=2, args=(2412032, 2412037, 0, 20011002))
    RunEvent(12410160, slot=4, args=(2412122, 2412035, 0, 20011001))
    RunEvent(12410160, slot=5, args=(2412033, 2412038, 1, 500007600))
    RunEvent(12415010, slot=0, args=(2412039, 0, 20011001, 300.0), arg_types='iiif')
    RunEvent(12415700)
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
    RunEvent(12415225, slot=0, args=(2410015, 3004, 50.0), arg_types='iif')
    RunEvent(12415225, slot=1, args=(2410102, 3027, 50.0), arg_types='iif')
    RunEvent(12415228, slot=0, args=(2410016, 3028, 6.0), arg_types='iif')
    RunEvent(12415232, slot=0, args=(2410178, 2412086))
    RunEvent(12415233, slot=0, args=(2412122, 2410196, 2412136))
    RunEvent(12415250, slot=1, args=(2410182, 7001, 5.0, 10.0, 2412075), arg_types='iiffi')
    RunEvent(12415255, slot=1, args=(2410183,))
    RunEvent(12415255, slot=2, args=(2410182,))
    RunEvent(12415255, slot=4, args=(2410181,))
    RunEvent(12415295, slot=0, args=(2410183, 2412120, 2.0, 2412074), arg_types='iifi')
    RunEvent(12415295, slot=1, args=(2410182, 2412120, 2.0, 2412075), arg_types='iifi')
    RunEvent(12415300, slot=0, args=(12415295, 2410183, 2412074, 2412121, 2.0), arg_types='iiiif')
    RunEvent(12415300, slot=1, args=(12415296, 2410182, 2412075, 2412121, 2.0), arg_types='iiiif')
    RunEvent(12415305, slot=0, args=(12415300, 2410183, 2412121, 2412122, 2.0, 2412084), arg_types='iiiifi')
    RunEvent(12415305, slot=1, args=(12415301, 2410182, 2412121, 2412122, 2.0, 2412085), arg_types='iiiifi')
    RunEvent(12415310, slot=0, args=(12415305, 2410183, 2412084, 2412122, 2.0, 2413500), arg_types='iiiifi')
    RunEvent(12415310, slot=1, args=(12415306, 2410182, 2412085, 2412122, 2.0, 2413500), arg_types='iiiifi')
    RunEvent(12415315, slot=0, args=(2410210, 2412120, 2.0, 2412130), arg_types='iifi')
    RunEvent(12415315, slot=1, args=(2410211, 2412120, 2.0, 2412132), arg_types='iifi')
    RunEvent(12415320, slot=0, args=(12415315, 2410210, 2412130, 2412122, 2413505))
    RunEvent(12415320, slot=1, args=(12415316, 2410211, 2412132, 2412122, 2413505))
    RunEvent(12415325, slot=0, args=(12415320, 2410210, 2412122, 2413502))
    RunEvent(12415325, slot=1, args=(12415321, 2410211, 2412122, 2413501))
    RunEvent(12415330, slot=0, args=(2410213, 2412124, 2412123, 2.0, 2412125), arg_types='iiifi')
    RunEvent(12415335, slot=0, args=(12415330, 2410213, 2412134, 2412122, 2413503))
    RunEvent(12415340, slot=0, args=(2410018, 2412120, 2.0, 2412096), arg_types='iifi')
    RunEvent(12415340, slot=2, args=(2410181, 2412121, 2.0, 2412083), arg_types='iifi')
    RunEvent(12415345, slot=0, args=(12415340, 2410018, 2412096, 0, 2.0, 0, -1), arg_types='iiiifii')
    RunEvent(12415345, slot=2, args=(12415342, 2410181, 2412083, 2412122, 2.0, 1, 2413500), arg_types='iiiifii')
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
    RunEvent(12410290)
    CreateHazard(12410430, 2411205, model_point=100, behavior_param_id=6110, target_type=DamageTargetType.Character, radius=1.5, life=0.0, repetition_time=1.0)
    CreateHazard(12410431, 2411206, model_point=100, behavior_param_id=6110, target_type=DamageTargetType.Character, radius=0.6000000238418579, life=0.0, repetition_time=1.0)
    CreateHazard(12410432, 2411207, model_point=100, behavior_param_id=6110, target_type=DamageTargetType.Character, radius=0.6000000238418579, life=0.0, repetition_time=1.0)
    CreateHazard(12410433, 2411208, model_point=100, behavior_param_id=6110, target_type=DamageTargetType.Character, radius=0.6000000238418579, life=0.0, repetition_time=1.0)
    RunEvent(12410200, slot=0, args=(2411300, 2411310, 12410200))
    RunEvent(12410200, slot=2, args=(2411302, 2411312, 12410202))
    RunEvent(12410200, slot=3, args=(2411303, 2411313, 12410203))
    RunEvent(12410200, slot=5, args=(2411305, 2411315, 12410205))
    RunEvent(12415020, slot=0, args=(7000, 2411305, 12410205, 10010171))
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
    RunEvent(12410120)
    RunEvent(12410130, slot=0, args=(12411306,))
    RunEvent(12410151)
    RunEvent(12410140)
    RunEvent(7600, slot=30, args=(2411999, 2413999))
    RunEvent(7600, slot=31, args=(2411998, 2413998))
    RunEvent(7600, slot=32, args=(2411997, 2413997))
    RunEvent(12415390, slot=0, args=(2410202,))
    RunEvent(12414732)
    RunEvent(12414733)
    RunEvent(12411700)
    RunEvent(12411701)
    RunEvent(12411702)
    RunEvent(12414730)
    RunEvent(12414731)
    RunEvent(12414702)
    RunEvent(12414703)
    RunEvent(12414704)
    RunEvent(12414705)
    RunEvent(12411703)
    RunEvent(12414707)
    RunEvent(12414708)
    RunEvent(12414710, slot=0, args=(2410, 2410, 1, 20, 480, 490, 8020), arg_types='hihiiii')
    RunEvent(12414710, slot=1, args=(2411, 2411, 2, 120, 481, 491, 8000), arg_types='hihiiii')
    RunEvent(12414710, slot=2, args=(2412, 2412, 3, 300, 482, 492, 8010), arg_types='hihiiii')
    RunEvent(12414710, slot=3, args=(2413, 2413, 4, 200, 483, 493, 8030), arg_types='hihiiii')
    RunEvent(12414710, slot=4, args=(2414, 2414, 5, 200, 484, 494, 8040), arg_types='hihiiii')
    RunEvent(12414720, slot=0, args=(480, 490, 5, 10), arg_types='iiBB')
    RunEvent(12414720, slot=1, args=(481, 491, 6, 11), arg_types='iiBB')
    RunEvent(12414720, slot=2, args=(482, 492, 7, 12), arg_types='iiBB')
    RunEvent(12414720, slot=3, args=(483, 493, 8, 13), arg_types='iiBB')
    RunEvent(12414720, slot=4, args=(484, 494, 9, 14), arg_types='iiBB')
    GotoIfFlagOn(Label.L2, 12410999)
    RunEvent(12410000)
    RunEvent(12410285, slot=0, args=(12410400, 12410401, 2411204, 2411316))
    RunEvent(12410995)
    Label(2)
    RunEvent(12410170)
    RunEvent(12415150, slot=0, args=(2410100, 7010, 7011, 6.0, 263499, 263450), arg_types='iiifii')
    RunEvent(12415150, slot=1, args=(2410101, 7014, 7015, 7.0, 263499, 263440), arg_types='iiifii')
    RunEvent(12415150, slot=2, args=(2410103, 7010, 7011, 4.0, 263499, 263450), arg_types='iiifii')
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
    RunEvent(12410370)
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
    RunEvent(12410010)
    RunEvent(12410011)
    RunEvent(12410012)
    RunEvent(12410600, slot=1, args=(12411202, 2411102, 9942))
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(2, 15)
    SkipLinesIfFlagOff(1, 6630)
    EnableFlag(12411999)
    SkipLinesIfFlagOn(6, 12411999)
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
    SkipLinesIfFlagOff(1, 6640)
    EnableFlag(12411998)
    SkipLinesIfFlagOn(5, 12411998)
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
    SkipLinesIfFlagOff(1, 6312)
    EnableFlag(12411997)
    SkipLinesIfFlagOn(6, 12411997)
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
    RunEvent(12414812)
    RunEvent(12414813)
    RunEvent(12411800)
    RunEvent(12411801)
    RunEvent(12411802)
    RunEvent(12414810)
    RunEvent(12414811)
    RunEvent(12414802)
    RunEvent(12414803)
    RunEvent(12414804)
    RunEvent(12414805)
    RunEvent(12414807)
    RunEvent(12414808)
    RunEvent(12414809)
    RunEvent(12411803)
    RunEvent(12415238, slot=0, args=(2412820, 2410810, 2412821, 2412824, 2412822))
    RunEvent(12415238, slot=1, args=(2412820, 2410811, 2412821, 2412824, 2412822))
    RunEvent(12410850, slot=0, args=(70000050, 6030, 2410870))
    RunEvent(12410850, slot=1, args=(70000051, 6030, 2410871))
    RunEvent(12410850, slot=2, args=(70000070, 6030, 2410872))
    RunEvent(12410850, slot=3, args=(70000071, 6030, 2410873))
    RunEvent(12410860, slot=0, args=(2410770, 103089))
    RunEvent(12410870, slot=0, args=(2410770, 103082, 153))
    RunEvent(12410880, slot=0, args=(2410770, 103086))
    RunEvent(12410702)
    RunEvent(12410704)
    RunEvent(12410705)
    RunEvent(12410706)
    RunEvent(12410710)
    RunEvent(12410713)
    RunEvent(12410715)
    RunEvent(12410716)
    RunEvent(12410703)
    DisableFlag(72410330)
    DisableFlag(72410335)
    DisableFlag(72410323)
    RunEvent(12410650)
    RunEvent(12410651)
    RunEvent(12410652)
    RunEvent(12410653)
    RunEvent(12410654)
    RunEvent(12410655)
    RunEvent(12410656)
    RunEvent(12410657)
    RunEvent(12410658)
    RunEvent(12410659)
    RunEvent(12410661)
    RunEvent(12410662, slot=0, args=(1163, 72410331, 72410338))
    RunEvent(12410662, slot=1, args=(1204, 72410331, 72410339))
    RunEvent(12410662, slot=2, args=(1268, 72410332, 72410340))
    RunEvent(12410662, slot=3, args=(1190, 72410332, 72410341))
    RunEvent(12410662, slot=4, args=(1223, 72410332, 72410342))
    RunEvent(12410662, slot=5, args=(1309, 72410332, 72410343))
    RunEvent(12410668)
    RunEvent(12410669, slot=0, args=(2410290, 1124, 0))
    RunEvent(12410669, slot=1, args=(2410291, 1163, 0))
    RunEvent(12410669, slot=2, args=(2410292, 1204, 7001))
    RunEvent(12410669, slot=3, args=(2410293, 1268, 0))
    RunEvent(12410669, slot=4, args=(2410294, 1190, 0))
    RunEvent(12410669, slot=5, args=(2410295, 1223, 7000))
    RunEvent(12410669, slot=6, args=(2410296, 1309, 7002))
    RunEvent(12410676)
    RunEvent(12410677)
    RunEvent(12410680, slot=0, args=(2410290,))
    RunEvent(12410680, slot=1, args=(2410291,))
    RunEvent(12410680, slot=2, args=(2410292,))
    RunEvent(12410680, slot=3, args=(2410293,))
    RunEvent(12410680, slot=4, args=(2410294,))
    RunEvent(12410680, slot=5, args=(2410295,))
    RunEvent(12410680, slot=6, args=(2410296,))
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
    RunEvent(12410700)
    RunEvent(12410721)
    RunEvent(12410730)
    RunEvent(12410731)
    RunEvent(12410732)
    RunEvent(12410733)
    RunEvent(12410734)
    RunEvent(12410736)
    RunEvent(12410737)
    RunEvent(12410738)
    RunEvent(12410739)
    RunEvent(12410785)
    RunEvent(12410786)
    RunEvent(12410787)
    RunEvent(12410740)
    RunEvent(12410741)
    RunEvent(12410742)
    RunEvent(12410743)
    RunEvent(12410746)
    RunEvent(12410747)
    RunEvent(12410748)
    RunEvent(12410749)
    RunEvent(12410750, slot=0, args=(72410392, 6030, 2410732))
    RunEvent(12410760)
    RunEvent(12410761)
    RunEvent(12410763)
    RunEvent(12410770, slot=0, args=(2410290,))
    RunEvent(12410770, slot=1, args=(2410291,))
    RunEvent(12410770, slot=2, args=(2410292,))
    RunEvent(12410770, slot=3, args=(2410293,))
    RunEvent(12410770, slot=4, args=(2410294,))
    RunEvent(12410770, slot=5, args=(2410295,))
    RunEvent(12410770, slot=6, args=(2410296,))
    RunEvent(12410809)
    RunEvent(12410810)
    RunEvent(12410811)
    RunEvent(12410831)
    RunEvent(12410833)
    RunEvent(12410834)
    RunEvent(12410835)
    RunEvent(12410812)
    RunEvent(12410813)
    RunEvent(12410814)
    RunEvent(12410510)
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


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    SkipLinesIfFlagOn(2, 12410000)
    EnableFlag(9180)
    DisableMapSound(2413900)
    SkipLinesIfFlagOff(1, 12410998)
    EnableFlag(12410999)
    RunEvent(12410005, slot=0, args=(12410999,))
    DisableAnimations(2413950)
    DisableGravity(2413950)
    DisableCollision(2413950)
    DisableAnimations(2413951)
    DisableGravity(2413951)
    DisableCollision(2413951)
    DisableAnimations(2413952)
    DisableGravity(2413952)
    DisableCollision(2413952)
    RunEvent(12410744)
    RunEvent(12410745)
    RunEvent(12410762)
    RunEvent(12410800)
    RunEvent(12410645)
    RunEvent(12410729)
    RunEvent(12410830)
    RunEvent(12410701)
    RunEvent(12410780)
    SkipLinesIfFlagOff(11, 12411000)
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


@NeverRestart
def Event12410000():
    """ 12410000: Event 12410000 """
    EndIfThisEventOn()
    EndIfOutsideMap(game_map=CENTRAL_YHARNAM)
    SkipLinesIfPlayerGender(2, Gender.Female)
    PlayCutscene(24010005, skippable=True, fade_out=True, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(24011005, skippable=True, fade_out=True, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    SetRespawnPoint(2412959)


@NeverRestart
def Event12411010():
    """ 12411010: Event 12411010 """
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 7015)
    Label(0)
    EnableFlag(12417810)


@RestartOnRest
def Event12414000(ARG_0_3: int, ARG_4_4: uchar, ARG_8_11: float):
    """ 12414000: Event 12414000 """
    EndIfThisEventSlotOn()
    DisableCharacter(ARG_0_3)
    IfPlayerInsightAmountGreaterThanOrEqual(1, ARG_4_4)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(ARG_0_3)
    ForceAnimation(ARG_0_3, 6200, wait_for_completion=True)


@RestartOnRest
def Event12414010(ARG_0_3: int, ARG_4_4: uchar, ARG_8_11: int):
    """ 12414010: Event 12414010 """
    GotoIfThisEventSlotOn(Label.L0)
    IfFlagOn(1, ARG_8_11)
    IfPlayerInsightAmountLessThanOrEqual(1, ARG_4_4)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    Kill(ARG_0_3, award_souls=False)


@NeverRestart
def Event12414100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12414100: Event 12414100 """
    DisableNetworkSync()
    IfActionButtonInRegion(0, action_button_id=ARG_4_7, region=ARG_0_3)
    DisplayDialog(ARG_8_11, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12410005(ARG_0_3: int):
    """ 12410005: Event 12410005 """
    GotoIfFlagOn(Label.L0, ARG_0_3)
    DisableMapPart(2414220)
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
    Label(0)
    EnableMapPart(2414220)
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
def Event12415060(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: float):
    """ 12415060: Event 12415060 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_8_11)
    IfEntityWithinDistance(-2, 10000, ARG_0_3, radius=ARG_12_15)
    IfConditionTrue(1, input_condition=-2)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event12415080(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: float):
    """ 12415080: Event 12415080 """
    GotoIfThisEventSlotOff(Label.L0)
    SetAIParamID(ARG_0_3, ARG_20_23)
    End()
    Label(0)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, skip_transition=True)
    SetAIParamID(ARG_0_3, ARG_16_19)
    DisableGravity(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_12_15)
    IfEntityWithinDistance(-2, 10000, ARG_0_3, radius=ARG_24_27)
    IfConditionTrue(1, input_condition=-2)
    IfHasAIStatus(2, ARG_0_3, ai_status=AIStatusType.Battle)
    IfDamageType(3, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    EnableGravity(ARG_0_3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    WaitRandomFrames(min_frames=20, max_frames=100)
    IfHealthLessThan(4, ARG_0_3, 1.0)
    GotoIfConditionTrue(Label.L1, input_condition=4)
    ForceAnimation(ARG_0_3, ARG_8_11, wait_for_completion=True)
    Label(1)
    SetAIParamID(ARG_0_3, ARG_20_23)


@NeverRestart
def Event12415020(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12415020: Event 12415020 """
    DisableNetworkSync()
    IfActionButtonInRegion(-1, action_button_id=ARG_0_3, region=ARG_4_7)
    IfFlagOn(-1, ARG_8_11)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagOn(ARG_8_11)
    DisplayDialog(ARG_12_15, anchor_entity=ARG_4_7, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12410200(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410200: Event 12410200 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_0_3, 1)
    Wait(1.0)
    DisableObjectActivation(ARG_4_7, obj_act_id=2410000)
    DisableObjectActivation(ARG_4_7, obj_act_id=2410001)
    IfActionButtonInRegion(0, action_button_id=7100, region=ARG_4_7)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()
    Label(0)
    IfObjectActivated(0, obj_act_id=ARG_8_11)
    ForceAnimation(ARG_0_3, 1)
    DisableNetworkSync()
    SkipLinesIfNotEqual(1, left=ARG_4_7, right=2411314)
    DisplayDialog(10010850, anchor_entity=ARG_4_7, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12410100(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410100: Event 12410100 """
    DisableNetworkSync()
    EndIfFlagOn(ARG_8_11)
    IfActionButtonInRegion(1, action_button_id=ARG_0_3, region=ARG_4_7)
    IfFlagOn(2, ARG_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    DisplayDialog(ARG_12_15, anchor_entity=ARG_4_7, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Wait(1.0)
    Restart()
    Label(0)
    Wait(1.0)
    Restart()


@NeverRestart
def Event12410110(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410110: Event 12410110 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_0_3, ARG_8_11)
    DisableObjectActivation(ARG_0_3, obj_act_id=ARG_12_15)
    NotifyDoorEventSoundDampening(ARG_0_3, state=DoorState.DoorOpening)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    Wait(0.0)


@NeverRestart
def Event12410120():
    """ 12410120: Event 12410120 """
    DisableNetworkSync()
    IfCharacterInsideRegion(1, PLAYER, region=2412300)
    IfCharacterInsideRegion(2, PLAYER, region=2412301)
    IfFlagOn(2, 12410130)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    AddSpecialEffect(PLAYER, 4150, affect_npc_part_hp=False)
    Wait(3.0)
    Restart()


@NeverRestart
def Event12410130(ARG_0_3: int):
    """ 12410130: Event 12410130 """
    DisableNetworkSync()
    EndIfThisEventSlotOn()
    IfObjectActivated(0, obj_act_id=ARG_0_3)
    End()


@NeverRestart
def Event12410150():
    """ 12410150: Event 12410150 """
    DisableNetworkSync()
    EndIfThisEventOn()
    IfObjectActivated(0, obj_act_id=12411307)
    DisplayDialog(10010850, anchor_entity=2411304, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.OneButton)


@NeverRestart
def Event12410151():
    """ 12410151: Event 12410151 """
    DisableNetworkSync()
    IfFlagOn(0, 12411800)
    EndIfFlagOn(12410150)
    EndIfClient()
    IfFlagOff(1, 12411000)
    EndIfConditionTrue(1)
    DisableObjectActivation(2411304, obj_act_id=2410080)
    IfActionButtonInRegion(0, action_button_id=7002, region=2411304)
    IfPlayGoState(2, PlayGoState.DownloadedFirstChunk)
    GotoIfConditionFalse(Label.L0, input_condition=2)
    DisplayDialog(10010180, anchor_entity=2411304, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.OneButton)
    Restart()
    Label(0)
    DisplayDialog(10010181, anchor_entity=2411304, display_distance=3.0, button_type=ButtonType.Yes_or_No, number_buttons=NumberButtons.OneButton)
    Restart()


@RestartOnRest
def Event12410160(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410160: Event 12410160 """
    EndIfThisEventSlotOn()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=ARG_4_7, sound_type=ARG_8_11, sound_id=ARG_12_15)


@RestartOnRest
def Event12410140():
    """ 12410140: Event 12410140 """
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1140, 1144))
    GotoIfFlagOn(Label.L1, 70000240)
    IfObjectActivated(0, obj_act_id=12411300)
    EnableFlag(70000240)
    End()
    Label(1)
    EndOfAnimation(2411307, 2)
    DisableObjectActivation(2411307, obj_act_id=2410010)
    NotifyDoorEventSoundDampening(2411307, state=DoorState.DoorOpening)
    End()
    Label(0)
    IfFlagOn(-1, 9401)
    IfFlagOn(-1, 9800)
    IfConditionTrue(0, input_condition=-1)
    EndOfAnimation(2411307, 0)
    EnableObjectActivation(2411307, obj_act_id=2410010)
    NotifyDoorEventSoundDampening(2411307, state=DoorState.DoorClosing)
    DisableFlag(62411300)
    DisableFlag(72410329)
    DisableFlag(72410344)
    DisableFlag(72410345)
    DisableFlag(72410346)


@NeverRestart
def Event12410337(ARG_0_3: int):
    """ 12410337: Event 12410337 """
    IfObjectActivated(0, obj_act_id=12411303)
    EnableNavmeshType(ARG_0_3, NavmeshType.Solid)


@RestartOnRest
def Event12415420(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12415420: Event 12415420 """
    SkipLinesIfEqual(1, left=ARG_8_11, right=0)
    EndIfFlagOn(ARG_8_11)
    IfCharacterBackreadEnabled(1, ARG_0_3)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    EnableImmortality(ARG_0_3)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfCharacterInsideRegion(2, ARG_0_3, region=ARG_4_7)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(ARG_0_3, 5915, affect_npc_part_hp=False)
    Kill(ARG_0_3, award_souls=True)


@RestartOnRest
def Event12415430(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: float):
    """ 12415430: Event 12415430 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfDamageType(2, attacked_entity=ARG_4_7, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfEntityWithinDistance(3, ARG_0_3, 10000, radius=ARG_12_15)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 2)
    Wait(ARG_8_11)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event12415435(ARG_0_3: int, ARG_4_7: int):
    """ 12415435: Event 12415435 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    WaitRandomFrames(min_frames=0, max_frames=10)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event12415460(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: float, ARG_20_23: int, ARG_24_27: int):
    """ 12415460: Event 12415460 """
    WaitFrames(10)
    Move(ARG_0_3, destination=ARG_20_23, model_point=-1, destination_type=CoordEntityType.Region)
    GotoIfThisEventSlotOff(Label.L0)
    End()
    Label(0)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, skip_transition=True)
    DisableGravity(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_12_15)
    IfEntityWithinDistance(-2, 10000, ARG_0_3, radius=ARG_16_19)
    IfConditionTrue(1, input_condition=-2)
    IfHasAIStatus(2, ARG_0_3, ai_status=AIStatusType.Battle)
    IfDamageType(3, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    EnableGravity(ARG_0_3)
    ForceAnimation(ARG_24_27, 1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    ForceAnimation(ARG_0_3, ARG_8_11, wait_for_completion=True)
    Label(1)
    End()


@RestartOnRest
def Event12415461(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12415461: Event 12415461 """
    GotoIfFlagOn(Label.L0, 12410170)
    ForceAnimation(ARG_0_3, ARG_4_7)
    IfHasTAEEvent(1, 2410019, tae_event_id=10)
    IfFlagOn(2, 12410170)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=1)
    Label(0)
    ForceAnimation(ARG_0_3, ARG_8_11)
    End()
    Label(1)
    Restart()


@NeverRestart
def Event12415470(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12415470: Event 12415470 """
    EndIfFlagOn(12415234)
    DisableAI(ARG_0_3)
    IfHasAIStatus(1, 2410200, ai_status=AIStatusType.Battle)
    IfHasAIStatus(1, 2410201, ai_status=AIStatusType.Battle)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfEntityWithinDistance(3, ARG_0_3, 10000, radius=8.0)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionFalse(1, 1)
    Wait(10.0)
    EnableAI(ARG_0_3)
    WaitFrames(10)
    SetNest(ARG_0_3, ARG_4_7)
    AICommand(ARG_0_3, command_id=ARG_8_11, slot=0)
    ResetAnimation(ARG_0_3, disable_interpolation=True)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(-1, ARG_0_3, region=ARG_4_7)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfConditionTrue(0, input_condition=-1)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12415475(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12415475: Event 12415475 """
    EndIfThisEventOn()
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, skip_transition=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_12_15)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfFlagOn(3, 12415477)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 2)
    ForceAnimation(2411202, 0, loop=True)
    ForceAnimation(ARG_0_3, ARG_8_11, wait_for_completion=True)
    SkipLinesIfFinishedConditionTrue(1, 3)
    End()
    SetNest(ARG_0_3, 2412051)


@RestartOnRest
def Event12415476(ARG_0_3: int, ARG_4_7: int):
    """ 12415476: Event 12415476 """
    EndIfThisEventSlotOn()
    IfDamageType(0, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    ForceAnimation(2411202, 0, loop=True)
    ForceAnimation(ARG_0_3, ARG_4_7, wait_for_completion=True)


@RestartOnRest
def Event12415477(ARG_0_3: int):
    """ 12415477: Event 12415477 """
    IfHost(0)
    SetNetworkUpdateAuthority(ARG_0_3, UpdateAuthority.Forced)
    DisableFlag(12415477)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12415477)
    ForceAnimation(ARG_0_3, 3021, wait_for_completion=True)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event12415478(ARG_0_3: int):
    """ 12415478: Event 12415478 """
    IfCharacterAlive(1, ARG_0_3)
    IfHasTAEEvent(1, ARG_0_3, tae_event_id=10)
    IfFlagOn(2, 12415475)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    SetObjectDamageShieldState(2411202, state=True)
    ForceAnimation(2411202, 1, loop=True, skip_transition=True)
    Restart()
    Label(0)
    SetObjectDamageShieldState(2411202, state=False)
    ForceAnimation(2411202, 0, loop=True)
    End()


@RestartOnRest
def Event12415479(ARG_0_3: int):
    """ 12415479: Event 12415479 """
    IfFlagOn(1, 12415475)
    IfFlagOn(1, 12415477)
    IfConditionTrue(0, input_condition=1)
    SetNest(ARG_0_3, 2412051)
    IfFlagOff(0, 12415477)
    SetNest(ARG_0_3, 2412240)
    Restart()


@RestartOnRest
def Event12415480(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12415480: Event 12415480 """
    GotoIfThisEventSlotOff(Label.L0)
    SetAIParamID(ARG_0_3, ARG_16_19)
    End()
    Label(0)
    IfCharacterBackreadEnabled(0, ARG_0_3)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, skip_transition=True)
    SetAIParamID(ARG_0_3, ARG_12_15)
    DisableGravity(ARG_0_3)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfFlagOn(2, 12415477)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableGravity(ARG_0_3)
    SkipLinesIfFinishedConditionTrue(2, 1)
    WaitRandomFrames(min_frames=20, max_frames=100)
    ForceAnimation(ARG_0_3, ARG_8_11, wait_for_completion=True)
    SetAIParamID(ARG_0_3, ARG_16_19)


@RestartOnRest
def Event12415498(ARG_0_3: int, ARG_4_7: int):
    """ 12415498: Event 12415498 """
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomFrames(min_frames=0, max_frames=30)
    ForceAnimation(ARG_0_3, 3010, wait_for_completion=True)
    IfFramesElapsed(-2, 51)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, 1)
    ShootProjectile(owner_entity=ARG_0_3, projectile_id=ARG_0_3, model_point=7, behavior_id=ARG_4_7, launch_angle_x=90, launch_angle_y=0, launch_angle_z=0)
    ForceAnimation(ARG_0_3, 7004, wait_for_completion=True)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Normal)
    Restart()


@NeverRestart
def Event12410815():
    """ 12410815: Event 12410815 """
    AddSpecialEffect(2410600, 5686, affect_npc_part_hp=False)
    WaitFrames(10)
    IfFlagOn(-1, 9802)
    IfPlayerInsightAmountGreaterThanOrEqual(-1, 20)
    IfConditionTrue(0, input_condition=-1)
    SetDisplayMask(2410600, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(2410600, bit_index=2, switch_type=OnOffChange.Off)
    SetDisplayMask(2410600, bit_index=10, switch_type=OnOffChange.Off)
    EnableCharacter(2410600)
    CancelSpecialEffect(2410600, 5686)
    IfPlayerInsightAmountLessThanOrEqual(1, 18)
    IfFlagOff(1, 9802)
    IfConditionTrue(0, input_condition=1)
    Restart()


@NeverRestart
def Event12410820():
    """ 12410820: Event 12410820 """
    DisableHitboxBackreadMask(2414400)
    DisableHitboxBackreadMask(2414401)
    DisableHitboxBackreadMask(2414402)
    DisableHitboxBackreadMask(2414410)
    DisableHitboxBackreadMask(2414420)
    DisableHitboxBackreadMask(2414421)


@RestartOnRest
def Event12410450(ARG_0_3: int, ARG_4_7: int):
    """ 12410450: Event 12410450 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableCharacter(ARG_0_3)
    End()
    Label(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagOn(1, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@NeverRestart
def Event12411899():
    """ 12411899: Event 12411899 """
    EndIfThisEventOn()
    IfFlagOn(1, 12411800)
    IfFlagOn(1, 12411700)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(2410)


@NeverRestart
def Event12411700():
    """ 12411700: Event 12411700 """
    GotoIfThisEventOff(Label.L0)
    DisableMapSound(2413802)
    DisableMapSound(2413803)
    DisableCharacter(2410800)
    Kill(2410800, award_souls=False)
    DisableObject(2411800)
    DeleteFX(2413800, erase_root_only=False)
    End()
    Label(0)
    IfCharacterDead(0, 2410800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2411800)
    DeleteFX(2413800, erase_root_only=True)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Wait(3.0)
    KillBoss(2410800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(21)
    SkipLinesIfFlagOn(1, 6645)
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
    Label(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


@NeverRestart
def Event12411701():
    """ 12411701: Event 12411701 """
    DisableNetworkSync()
    EndIfFlagOn(12411700)
    IfFlagOn(1, 12411700)
    IfCharacterBackreadDisabled(2, 2410800)
    IfHealthLessThanOrEqual(2, 2410800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2412800, sound_type=SoundType.c_CharacterMotion, sound_id=500099999)


@NeverRestart
def Event12411702():
    """ 12411702: Event 12411702 """
    EndIfFlagOn(12411700)
    GotoIfThisEventOff(Label.L0)
    End()
    Label(0)
    DisableCharacter(2410800)
    DisableGravity(2410800)
    DisableCollision(2410800)
    IfFlagOff(1, 12411700)
    IfThisEventOff(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2412805)
    IfConditionTrue(0, input_condition=1)
    Move(2410800, destination=2412831, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    EnableFlag(72410511)
    EnableCharacter(2410800)
    ForceAnimation(2410800, 3028)
    WaitFrames(110)
    EnableGravity(2410800)
    EnableCollision(2410800)
    EnableFlag(12414700)
    EnableFlag(12414223)
    EndIfFlagOn(9300)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9300)


@NeverRestart
def Event12411703():
    """ 12411703: Event 12411703 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12414700)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(2410800)
    EnableFlag(12414700)
    EnableFlag(12411702)


@NeverRestart
def Event12414730():
    """ 12414730: Event 12414730 """
    EndIfFlagOn(12411700)
    GotoIfFlagOn(Label.L0, 12411702)
    SkipLinesIfClient(2)
    DisableObject(2411800)
    DeleteFX(2413800, erase_root_only=False)
    IfFlagOff(1, 12411700)
    IfFlagOn(1, 12411702)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2411800)
    CreateFX(2413800)
    Label(0)
    IfFlagOff(2, 12411700)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonInRegion(2, action_button_id=2410040, region=2411800)
    IfFlagOn(3, 12411700)
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
    EnableFlag(12414700)
    EnableFlag(12414223)
    Restart()


@NeverRestart
def Event12414731():
    """ 12414731: Event 12414731 """
    DisableNetworkSync()
    EndIfFlagOn(12411700)
    IfFlagOff(1, 12411700)
    IfFlagOn(1, 12411702)
    IfFlagOn(1, 12414700)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonInRegion(1, action_button_id=2410040, region=2411800)
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


@NeverRestart
def Event12414732():
    """ 12414732: Event 12414732 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, 10000, 2411800, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12414733():
    """ 12414733: Event 12414733 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, 10000, 2411800, radius=4.0)
    IfEntityWithinDistance(1, 10000, 2411800, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12414702():
    """ 12414702: Event 12414702 """
    EndIfFlagOn(12411700)
    DisableAI(2410800)
    DisableHealthBar(2410800)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(-1, 12414700)
    IfFlagOn(-1, 12415400)
    IfConditionTrue(0, input_condition=-1)
    GotoIfClient(Label.L0)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2410800, UpdateAuthority.Forced)
    Label(0)
    EnableFlag(12414700)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)
    Label(1)
    Goto(Label.L4)
    Label(2)
    AddSpecialEffect(2410800, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2410800)
    Goto(Label.L4)
    Label(3)
    AddSpecialEffect(2410800, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2410800)
    Goto(Label.L4)
    Label(4)
    EnableAI(2410800)
    EnableBossHealthBar(2410800, name=500000, slot=0)
    CreatePlayLog(80)
    StartPlayLogMeasurement(2410010, 96, overwrite=True)


@NeverRestart
def Event12414703():
    """ 12414703: Event 12414703 """
    DisableNetworkSync()
    EndIfFlagOn(12411700)
    GotoIfThisEventOn(Label.L0)
    DisableMapSound(2413802)
    DisableMapSound(2413803)
    IfFlagOff(1, 12411700)
    IfFlagOn(1, 12414702)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12414701)
    IfCharacterInsideRegion(1, PLAYER, region=2412801)
    IfConditionTrue(0, input_condition=1)
    SetBossMusicState(2413802, state=True)
    IfHasTAEEvent(2, 2410800, tae_event_id=100)
    Label(0)
    IfFlagOff(2, 12411700)
    IfFlagOn(2, 12414702)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12414701)
    IfCharacterInsideRegion(2, PLAYER, region=2412801)
    IfConditionTrue(0, input_condition=2)
    SetBossMusicState(2413802, state=False)
    WaitFrames(0)
    SetBossMusicState(2413803, state=True)


@NeverRestart
def Event12414704():
    """ 12414704: Event 12414704 """
    DisableNetworkSync()
    EndIfFlagOn(12411700)
    IfHealthGreaterThan(1, 2410800, 0.0)
    IfEntityWithinDistance(1, 10000, 2410800, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=1)
    IfHealthGreaterThan(2, 2410800, 0.0)
    IfEntityBeyondDistance(2, 10000, 2410800, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Restart()


@NeverRestart
def Event12414705():
    """ 12414705: Event 12414705 """
    DisableNetworkSync()
    EndIfFlagOn(12411700)
    IfFlagOn(0, 12411700)
    SetBossMusicState(2413802, state=False)
    SetBossMusicState(2413803, state=False)
    SetBossMusicState(-1, state=False)


@NeverRestart
def Event12414707():
    """ 12414707: Event 12414707 """
    EndIfFlagOn(12411700)
    IfHealthLessThan(0, 2410800, 0.699999988079071)
    AICommand(2410800, command_id=1, slot=1)
    ReplanAI(2410800)
    IfHasTAEEvent(0, 2410800, tae_event_id=100)
    AICommand(2410800, command_id=-1, slot=1)
    ReplanAI(2410800)


@NeverRestart
def Event12414708():
    """ 12414708: Event 12414708 """
    EndIfFlagOn(12411700)
    GotoIfThisEventOn(Label.L0)
    IfCharacterHasSpecialEffect(0, 2410800, 482)
    Label(0)
    ChangeCharacterCloth(2410800, 15, state_id=2)


@RestartOnRest
def Event12414710(ARG_0_1: short, ARG_4_7: int, ARG_8_9: short, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12414710: Event 12414710 """
    EndIfFlagOn(12411700)
    CreateNPCPart(2410800, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=ARG_12_15, damage_correction=1.0, body_damage_correction=1.0, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(2410800, npc_part_id=ARG_4_7, material_special_effect_id=72, material_fx_id=72)
    IfCharacterPartHealthLessThanOrEqual(2, 2410800, npc_part_id=ARG_4_7, value=0)
    IfHealthLessThanOrEqual(3, 2410800, 0.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    CreateNPCPart(2410800, npc_part_id=ARG_0_1, part_index=ARG_8_9, part_health=9999999, damage_correction=1.0, body_damage_correction=1.5, is_invincible=False, start_in_stop_state=False)
    SetNPCPartEffects(2410800, npc_part_id=ARG_4_7, material_special_effect_id=73, material_fx_id=73)
    ForceAnimation(2410800, ARG_24_27)
    AddSpecialEffect(2410800, ARG_16_19, affect_npc_part_hp=False)
    CancelSpecialEffect(2410800, ARG_20_23)
    ReplanAI(2410800)
    Wait(30.0)
    AICommand(2410800, command_id=1, slot=0)
    ReplanAI(2410800)
    IfHasTAEEvent(0, 2410800, tae_event_id=300)
    SetNPCPartHealth(2410800, npc_part_id=ARG_4_7, desired_hp=-1, overwrite_max=True)
    AddSpecialEffect(2410800, ARG_20_23, affect_npc_part_hp=False)
    CancelSpecialEffect(2410800, ARG_16_19)
    AICommand(2410800, command_id=-1, slot=0)
    ReplanAI(2410800)
    WaitFrames(10)
    Restart()


@NeverRestart
def Event12414720(ARG_0_3: int, ARG_4_7: int, ARG_8_8: uchar, ARG_9_9: uchar):
    """ 12414720: Event 12414720 """
    EndIfFlagOn(12411700)
    IfCharacterHasSpecialEffect(1, 2410800, ARG_0_3)
    IfCharacterDoesNotHaveSpecialEffect(1, 2410800, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    SetDisplayMask(2410800, bit_index=ARG_9_9, switch_type=OnOffChange.On)
    SetDisplayMask(2410800, bit_index=ARG_8_8, switch_type=OnOffChange.Off)
    IfCharacterDoesNotHaveSpecialEffect(2, 2410800, ARG_0_3)
    IfCharacterHasSpecialEffect(2, 2410800, ARG_4_7)
    IfConditionTrue(0, input_condition=2)
    SetDisplayMask(2410800, bit_index=ARG_8_8, switch_type=OnOffChange.On)
    SetDisplayMask(2410800, bit_index=ARG_9_9, switch_type=OnOffChange.Off)
    WaitFrames(10)
    Restart()


@NeverRestart
def Event12411800():
    """ 12411800: Event 12411800 """
    GotoIfThisEventOff(Label.L0)
    DisableMapSound(2413812)
    DisableMapSound(2413813)
    DisableCharacter(2410810)
    DisableCharacter(2410811)
    Kill(2410810, award_souls=False)
    Kill(2410811, award_souls=False)
    DisableObject(2411810)
    DeleteFX(2413810, erase_root_only=False)
    End()
    Label(0)
    IfCharacterDead(1, 2410810)
    IfCharacterDead(2, 2410811)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2411810)
    DeleteFX(2413810, erase_root_only=True)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, 2)
    KillBoss(2410810)
    SkipLines(1)
    KillBoss(2410811)
    SetNetworkUpdateRate(2410811, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(2,))
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
    Label(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


@NeverRestart
def Event12411801():
    """ 12411801: Event 12411801 """
    DisableNetworkSync()
    EndIfFlagOn(12411800)
    IfFlagOn(1, 12411800)
    IfCharacterBackreadDisabled(2, 2410810)
    IfHealthLessThanOrEqual(2, 2410810, 0.0)
    IfCharacterBackreadDisabled(3, 2410811)
    IfHealthLessThanOrEqual(3, 2410811, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2412810, sound_type=SoundType.c_CharacterMotion, sound_id=500099999)


@NeverRestart
def Event12411802():
    """ 12411802: Event 12411802 """
    EndIfFlagOn(12411800)
    EndIfThisEventOn()
    DisableCharacter(2410810)
    IfFlagOff(1, 12411800)
    IfThisEventOff(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2412815)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12414223)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)
    WaitFrames(1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(24010010, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(24010010, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    Move(2410810, destination=2412830, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    EnableCharacter(2410810)
    EnableFlag(12414800)
    EndIfFlagOn(9336)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9336)


@NeverRestart
def Event12411803():
    """ 12411803: Event 12411803 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12414800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(2410810)
    EnableFlag(12414800)
    EnableFlag(12411802)


@NeverRestart
def Event12414810():
    """ 12414810: Event 12414810 """
    EndIfFlagOn(12411800)
    GotoIfFlagOn(Label.L0, 12411802)
    SkipLinesIfClient(2)
    DisableObject(2411810)
    DeleteFX(2413810, erase_root_only=False)
    IfFlagOff(1, 12411800)
    IfFlagOn(1, 12411802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2411810)
    CreateFX(2413810)
    Label(0)
    IfFlagOff(2, 12411800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonInRegion(2, action_button_id=2410041, region=2411810)
    IfFlagOn(3, 12411800)
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
    EnableFlag(12414800)
    Restart()


@NeverRestart
def Event12414811():
    """ 12414811: Event 12414811 """
    DisableNetworkSync()
    EndIfFlagOn(12411800)
    IfFlagOff(1, 12411800)
    IfFlagOn(1, 12411802)
    IfFlagOn(1, 12414800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonInRegion(1, action_button_id=2410041, region=2411810)
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
    EnableFlag(12414801)
    Restart()


@NeverRestart
def Event12414812():
    """ 12414812: Event 12414812 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, 10000, 2411810, radius=4.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12414813():
    """ 12414813: Event 12414813 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, 10000, 2411810, radius=4.0)
    IfEntityWithinDistance(1, 10000, 2411810, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event12414802():
    """ 12414802: Event 12414802 """
    EndIfFlagOn(12411800)
    DisableAI(2410810)
    DisableAI(2410811)
    DisableHealthBar(2410810)
    DisableHealthBar(2410811)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 12414800)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagOn(1, 12414223)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2410810, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2410811, UpdateAuthority.Forced)
    Label(0)
    EnableFlag(12414223)
    EnableFlag(12414800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)
    Label(1)
    Goto(Label.L4)
    Label(2)
    AddSpecialEffect(2410810, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2410811, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2410810)
    AdaptSpecialEffectHealthChangeToNPCPart(2410811)
    Goto(Label.L4)
    Label(3)
    AddSpecialEffect(2410810, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2410811, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2410810)
    AdaptSpecialEffectHealthChangeToNPCPart(2410811)
    Goto(Label.L4)
    Label(4)
    ReferDamageToEntity(2410810, 2410811)
    GotoIfFlagOn(Label.L5, 12414807)
    EnableAI(2410810)
    EnableBossHealthBar(2410810, name=271000, slot=0)
    Goto(Label.L6)
    Label(5)
    EnableAI(2410811)
    EnableBossHealthBar(2410811, name=272000, slot=0)
    Label(6)
    CreatePlayLog(80)
    StartPlayLogMeasurement(2410010, 96, overwrite=True)


@NeverRestart
def Event12414803():
    """ 12414803: Event 12414803 """
    DisableNetworkSync()
    EndIfFlagOn(12411800)
    GotoIfThisEventOn(Label.L0)
    DisableMapSound(2413812)
    DisableMapSound(2413813)
    IfFlagOff(1, 12411800)
    IfFlagOn(1, 12414802)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12414801)
    IfCharacterInsideRegion(1, PLAYER, region=2412812)
    IfConditionTrue(0, input_condition=1)
    SetBossMusicState(2413812, state=True)
    IfFlagOn(2, 12414807)
    Label(0)
    IfFlagOff(2, 12411800)
    IfFlagOn(2, 12414802)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12414801)
    IfCharacterInsideRegion(2, PLAYER, region=2412812)
    IfConditionTrue(0, input_condition=2)
    SetBossMusicState(2413812, state=False)
    WaitFrames(0)
    SetBossMusicState(2413813, state=True)


@NeverRestart
def Event12414804():
    """ 12414804: Event 12414804 """
    DisableNetworkSync()
    EndIfFlagOn(12411800)
    GotoIfFlagOn(Label.L0, 12414807)
    IfHealthGreaterThan(1, 2410810, 0.0)
    IfEntityWithinDistance(1, 10000, 2410810, radius=5.5)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=1)
    IfHealthGreaterThan(2, 2410810, 0.0)
    IfEntityBeyondDistance(2, 10000, 2410810, radius=6.0)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Restart()
    Label(0)
    IfHealthGreaterThan(3, 2410811, 0.0)
    IfEntityWithinDistance(3, 10000, 2410811, radius=5.5)
    IfConditionTrue(0, input_condition=3)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=1)
    IfHealthGreaterThan(4, 2410811, 0.0)
    IfEntityBeyondDistance(4, 10000, 2410811, radius=6.0)
    IfConditionTrue(0, input_condition=4)
    SetLockedCameraSlot(game_map=CENTRAL_YHARNAM, camera_slot=0)
    Restart()


@NeverRestart
def Event12414805():
    """ 12414805: Event 12414805 """
    DisableNetworkSync()
    EndIfFlagOn(12411800)
    IfFlagOn(0, 12411800)
    SetBossMusicState(2413812, state=False)
    SetBossMusicState(2413813, state=False)
    SetBossMusicState(-1, state=False)


@NeverRestart
def Event12414807():
    """ 12414807: Event 12414807 """
    EndIfFlagOn(12411800)
    GotoIfThisEventOff(Label.L0)
    DisableCharacter(2410810)
    End()
    Label(0)
    DisableGravity(2410811)
    IfHealthLessThan(1, 2410810, 0.3400000035762787)
    IfHasTAEEvent(2, 2410810, tae_event_id=30)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    AICommand(2410810, command_id=40, slot=0)
    SkipLinesIfFinishedConditionTrue(1, 2)
    IfHasTAEEvent(0, 2410810, tae_event_id=30)
    WaitFrames(5)
    DisableCharacter(2410810)
    EnableGravity(2410811)
    SetNetworkUpdateRate(2410811, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(2410811, destination=2410810, destination_type=CoordEntityType.Character, model_point=203, copy_draw_hitbox=2410810)
    ForceAnimation(2410811, 3030, wait_for_completion=True)
    EnableAI(2410811)
    EnableBossHealthBar(2410811, name=272000, slot=0)
    EndIfFlagOn(9337)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9337)


@NeverRestart
def Event12414808():
    """ 12414808: Event 12414808 """
    IfCharacterHasSpecialEffect(1, 2410810, 4640)
    IfHealthGreaterThanOrEqual(1, 2410810, 0.3400000035762787)
    IfConditionTrue(0, input_condition=1)
    AICommand(2410810, command_id=60, slot=0)
    ReplanAI(2410810)
    IfHasTAEEvent(0, 2410810, tae_event_id=10)
    AICommand(2410810, command_id=-1, slot=0)
    ReplanAI(2410810)
    Wait(10.0)
    IfCharacterHasSpecialEffect(1, 2410810, 4640)
    IfHealthGreaterThanOrEqual(1, 2410810, 0.3400000035762787)
    IfConditionTrue(0, input_condition=1)
    AICommand(2410810, command_id=60, slot=0)
    ReplanAI(2410810)
    IfHasTAEEvent(0, 2410810, tae_event_id=10)
    AICommand(2410810, command_id=-1, slot=0)
    ReplanAI(2410810)
    Wait(10.0)
    IfCharacterHasSpecialEffect(1, 2410810, 4640)
    IfHealthGreaterThanOrEqual(1, 2410810, 0.3400000035762787)
    IfConditionTrue(0, input_condition=1)
    AICommand(2410810, command_id=60, slot=0)
    ReplanAI(2410810)
    IfHasTAEEvent(0, 2410810, tae_event_id=10)
    AICommand(2410810, command_id=40, slot=0)
    ReplanAI(2410810)


@NeverRestart
def Event12414809():
    """ 12414809: Event 12414809 """
    IfFlagOn(0, 12414807)
    Wait(3.0)
    IfCharacterHasSpecialEffect(0, 2410811, 4640)
    AICommand(2410811, command_id=50, slot=0)
    ReplanAI(2410811)
    IfHasTAEEvent(0, 2410811, tae_event_id=20)
    AICommand(2410811, command_id=-1, slot=0)
    ReplanAI(2410811)


@RestartOnRest
def Event12415225(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float):
    """ 12415225: Event 12415225 """
    EndIfThisEventSlotOn()
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=ARG_8_11)
    IfConditionTrue(1, input_condition=-1)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(ARG_0_3, ARG_4_7)


@RestartOnRest
def Event12415228(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float):
    """ 12415228: Event 12415228 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=ARG_8_11)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    EnableAI(ARG_0_3)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(ARG_0_3, ARG_4_7)


@RestartOnRest
def Event12415232(ARG_0_3: int, ARG_4_7: int):
    """ 12415232: Event 12415232 """
    GotoIfThisEventSlotOn(Label.L0)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    Label(0)
    SetNest(ARG_0_3, ARG_4_7)


@RestartOnRest
def Event12415233(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12415233: Event 12415233 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    SetNest(ARG_4_7, ARG_8_11)


@NeverRestart
def Event12415234(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12415234: Event 12415234 """
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterDead(1, ARG_0_3)
    IfCharacterDead(1, ARG_4_7)
    IfCharacterAlive(1, ARG_8_11)
    IfEntityWithinDistance(2, ARG_8_11, 10000, radius=10.0)
    IfEntityBeyondDistance(3, ARG_8_11, 10000, radius=10.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EndIfFinishedConditionTrue(2)
    IfEntityWithinDistance(0, 10000, 0, radius=0.0)
    WaitFrames(10)


@NeverRestart
def Event12415236(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12415236: Event 12415236 """
    IfFlagOn(15, 12415236)
    IfClient(15)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    DisableCharacter(ARG_8_11)
    End()
    Label(0)
    DisableCharacter(ARG_12_15)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, ARG_0_3)
    IfFlagOn(1, 12415234)
    IfCharacterAlive(1, ARG_8_11)
    IfAllPlayersInsideRegion(1, region=2412143)
    IfHealthLessThanOrEqual(-2, ARG_4_7, 0.5)
    IfTimeElapsed(-2, 40.0)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EndIfFlagOn(12411700)
    EnableFlag(12415236)
    DisableCharacter(ARG_8_11)
    EnableCharacter(ARG_12_15)
    SkipLinesIfClient(1)
    SetNetworkUpdateAuthority(ARG_12_15, UpdateAuthority.Forced)
    Wait(1.0)
    SetNest(ARG_12_15, ARG_16_19)
    AICommand(ARG_12_15, command_id=10, slot=0)
    ReplanAI(ARG_12_15)
    DisableGravity(ARG_12_15)
    DisableCollision(ARG_12_15)
    DisableAnimations(ARG_12_15)
    IfEntityWithinDistance(-3, ARG_12_15, 2410800, radius=3.0)
    IfCharacterInsideRegion(-3, ARG_12_15, region=2412801)
    IfConditionTrue(0, input_condition=-3)
    AICommand(ARG_12_15, command_id=-1, slot=0)
    ClearTargetList(ARG_12_15)
    ReplanAI(ARG_12_15)
    EnableCollision(ARG_12_15)
    EnableAnimations(ARG_12_15)
    EnableGravity(ARG_12_15)


@RestartOnRest
def Event12415238(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12415238: Event 12415238 """
    IfCharacterInsideRegion(1, ARG_4_7, region=ARG_8_11)
    IfAllPlayersInsideRegion(1, region=ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    SetNest(ARG_4_7, ARG_12_15)
    AICommand(ARG_4_7, command_id=10, slot=0)
    ReplanAI(ARG_4_7)
    IfCharacterInsideRegion(-1, ARG_4_7, region=ARG_16_19)
    IfDamageType(-1, attacked_entity=ARG_4_7, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    AICommand(ARG_4_7, command_id=-1, slot=0)
    ReplanAI(ARG_4_7)
    Restart()


@RestartOnRest
def Event12415250(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: float, ARG_16_19: int):
    """ 12415250: Event 12415250 """
    IfCharacterInsideRegion(0, ARG_0_3, region=ARG_16_19)
    WaitRandomSeconds(min_seconds=ARG_8_11, max_seconds=ARG_12_15)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Normal)
    ForceAnimation(ARG_0_3, ARG_4_7, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event12415255(ARG_0_3: int):
    """ 12415255: Event 12415255 """
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfHasAIStatus(2, ARG_0_3, ai_status=AIStatusType.Normal)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    RestartIfFinishedConditionTrue(1)
    AICommand(ARG_0_3, command_id=20, slot=0)
    ReplanAI(ARG_0_3)
    Restart()


@RestartOnRest
def Event12415260(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12415260: Event 12415260 """
    GotoIfThisEventSlotOff(Label.L0)
    SetNest(ARG_0_3, ARG_24_27)
    ChangePatrolBehavior(ARG_0_3, patrol_information_id=2413500)
    End()
    Label(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_4_7)
    IfEntityWithinDistance(-2, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    SetNest(ARG_0_3, ARG_12_15)
    AICommand(ARG_0_3, command_id=20, slot=0)
    IfCharacterInsideRegion(2, ARG_0_3, region=ARG_12_15)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-3)
    IfCharacterInsideRegion(-4, PLAYER, region=ARG_16_19)
    IfEntityWithinDistance(-4, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(2, input_condition=-4)
    IfConditionTrue(0, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterType(-4, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-4)
    IfCharacterInsideRegion(-5, PLAYER, region=ARG_16_19)
    IfCharacterInsideRegion(-5, PLAYER, region=ARG_20_23)
    IfEntityWithinDistance(-5, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(3, input_condition=-5)
    IfConditionTrue(0, input_condition=3)
    WaitRandomFrames(min_frames=0, max_frames=300)
    Label(1)
    SetNest(ARG_0_3, ARG_24_27)
    AICommand(ARG_0_3, command_id=20, slot=0)
    IfCharacterInsideRegion(4, ARG_0_3, region=ARG_24_27)
    IfCharacterHuman(-6, PLAYER)
    IfCharacterType(-6, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(5, input_condition=-6)
    IfCharacterInsideRegion(-7, PLAYER, region=ARG_20_23)
    IfEntityWithinDistance(-7, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(5, input_condition=-7)
    IfConditionTrue(0, input_condition=5)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ChangePatrolBehavior(ARG_0_3, patrol_information_id=2413500)


@RestartOnRest
def Event12415295(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int):
    """ 12415295: Event 12415295 """
    GotoIfThisEventSlotOff(Label.L0)
    SetNest(ARG_0_3, ARG_12_15)
    End()
    Label(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_4_7)
    IfEntityWithinDistance(-2, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    SetNest(ARG_0_3, ARG_12_15)
    AICommand(ARG_0_3, command_id=20, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12415300(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: float):
    """ 12415300: Event 12415300 """
    EndIfThisEventSlotOn()
    IfFlagOn(1, ARG_0_3)
    IfCharacterInsideRegion(2, ARG_4_7, region=ARG_8_11)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_12_15)
    IfEntityWithinDistance(-2, 10000, ARG_4_7, radius=ARG_16_19)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_4_7, command_id=-1, slot=0)
    ReplanAI(ARG_4_7)


@RestartOnRest
def Event12415305(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: float, ARG_20_23: int):
    """ 12415305: Event 12415305 """
    GotoIfThisEventSlotOff(Label.L0)
    SetNest(ARG_4_7, ARG_20_23)
    End()
    Label(0)
    IfFlagOn(1, ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_8_11)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_12_15)
    IfEntityWithinDistance(-2, 10000, ARG_4_7, radius=ARG_16_19)
    IfConditionTrue(2, input_condition=-2)
    IfConditionTrue(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    WaitRandomFrames(min_frames=0, max_frames=30)
    Label(1)
    SetNest(ARG_4_7, ARG_20_23)
    AICommand(ARG_4_7, command_id=20, slot=0)
    ReplanAI(ARG_4_7)


@RestartOnRest
def Event12415310(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: float, ARG_20_23: int):
    """ 12415310: Event 12415310 """
    EndIfThisEventSlotOn()
    IfFlagOn(1, ARG_0_3)
    IfCharacterInsideRegion(2, ARG_4_7, region=ARG_8_11)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_12_15)
    IfEntityWithinDistance(-2, 10000, ARG_4_7, radius=ARG_16_19)
    IfConditionTrue(3, input_condition=-2)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    ChangePatrolBehavior(ARG_4_7, patrol_information_id=ARG_20_23)
    AICommand(ARG_4_7, command_id=-1, slot=0)
    ReplanAI(ARG_4_7)


@RestartOnRest
def Event12415315(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int):
    """ 12415315: Event 12415315 """
    GotoIfThisEventSlotOff(Label.L0)
    SetNest(ARG_0_3, ARG_12_15)
    End()
    Label(0)
    DisableAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=ARG_4_7)
    IfEntityWithinDistance(3, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    EnableAI(ARG_0_3)
    SetNest(ARG_0_3, ARG_12_15)


@RestartOnRest
def Event12415320(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12415320: Event 12415320 """
    GotoIfThisEventSlotOn(Label.L0)
    IfFlagOn(1, ARG_0_3)
    IfCharacterInsideRegion(2, ARG_4_7, region=ARG_8_11)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=ARG_12_15)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    ChangePatrolBehavior(ARG_4_7, patrol_information_id=ARG_16_19)


@RestartOnRest
def Event12415325(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12415325: Event 12415325 """
    GotoIfThisEventSlotOn(Label.L0)
    IfFlagOn(1, ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=ARG_8_11)
    IfConditionTrue(1, input_condition=2)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    ChangePatrolBehavior(ARG_4_7, patrol_information_id=ARG_12_15)


@RestartOnRest
def Event12415330(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: float, ARG_16_19: int):
    """ 12415330: Event 12415330 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(3, PLAYER, region=ARG_8_11)
    IfCharacterInsideRegion(4, PLAYER, region=ARG_16_19)
    IfEntityWithinDistance(5, 10000, ARG_0_3, radius=ARG_12_15)
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
    Label(1)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event12415335(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12415335: Event 12415335 """
    GotoIfThisEventSlotOn(Label.L0)
    IfFlagOn(1, ARG_0_3)
    IfCharacterInsideRegion(2, ARG_4_7, region=ARG_8_11)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-1)
    IfCharacterInsideRegion(3, PLAYER, region=ARG_12_15)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    ChangePatrolBehavior(ARG_4_7, patrol_information_id=ARG_16_19)


@RestartOnRest
def Event12415340(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int):
    """ 12415340: Event 12415340 """
    GotoIfThisEventSlotOff(Label.L0)
    SetNest(ARG_0_3, ARG_12_15)
    End()
    Label(0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=ARG_4_7)
    IfEntityWithinDistance(3, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfDamageType(4, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=4)
    AICommand(ARG_0_3, command_id=20, slot=0)
    Label(1)
    WaitFrames(10)
    SetNest(ARG_0_3, ARG_12_15)


@RestartOnRest
def Event12415345(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: float, ARG_20_23: int, ARG_24_27: int):
    """ 12415345: Event 12415345 """
    GotoIfThisEventSlotOn(Label.L0)
    IfFlagOn(1, ARG_0_3)
    IfCharacterInsideRegion(2, ARG_4_7, region=ARG_8_11)
    IfDamageType(3, attacked_entity=ARG_4_7, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(4, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_12_15)
    IfEntityWithinDistance(-2, 10000, ARG_4_7, radius=ARG_16_19)
    IfConditionTrue(4, input_condition=-2)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_4_7, command_id=-1, slot=0)
    ReplanAI(ARG_4_7)
    Label(0)
    EndIfEqual(left=ARG_20_23, right=0)
    ChangePatrolBehavior(ARG_4_7, patrol_information_id=ARG_24_27)


@NeverRestart
def Event12410286(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410286: Event 12410286 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_8_11, 2)
    Wait(1.0)
    RegisterLadder(start_climbing_flag=ARG_0_3, stop_climbing_flag=ARG_4_7, obj=ARG_8_11)
    DisableObjectActivation(ARG_12_15, obj_act_id=2410000)
    End()
    Label(0)
    DisableObjectActivation(ARG_12_15, obj_act_id=2410000)
    ForceAnimation(ARG_8_11, 2)
    RegisterLadder(start_climbing_flag=ARG_0_3, stop_climbing_flag=ARG_4_7, obj=ARG_8_11)


@NeverRestart
def Event12410290():
    """ 12410290: Event 12410290 """
    DeleteFX(2413110, erase_root_only=False)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2412150)
    IfConditionTrue(0, input_condition=1)
    CreateFX(2413110)


@NeverRestart
def Event12415360(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12415360: Event 12415360 """
    EndIfThisEventSlotOn()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_4_7, ARG_8_11)


@NeverRestart
def Event12415390(ARG_0_3: int):
    """ 12415390: Event 12415390 """
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetNest(ARG_0_3, 2412242)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Normal)
    SetNest(ARG_0_3, 2412241)
    Restart()


@RestartOnRest
def Event12415700():
    """ 12415700: Event 12415700 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(1, 2410270, 10000, radius=8.0)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    ChangePatrolBehavior(2410270, patrol_information_id=2413510)
    ReplanAI(2410270)


@RestartOnRest
def Event12415750(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12415750: Event 12415750 """
    DisableMapSound(ARG_0_3)
    EndIfFlagOn(ARG_12_15)
    IfFlagOff(1, ARG_4_7)
    IfFlagOff(1, ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(ARG_0_3)
    IfFlagOn(-1, ARG_4_7)
    IfFlagOn(-1, ARG_8_11)
    IfConditionTrue(0, input_condition=-1)
    DisableMapSound(ARG_0_3)
    Restart()


@RestartOnRest
def Event12415759(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12415759: Event 12415759 """
    DisableMapSound(ARG_0_3)
    EndIfFlagOn(1245)
    EndIfFlagOn(1246)
    EndIfFlagOn(ARG_12_15)
    IfFlagOff(1, ARG_4_7)
    IfFlagOff(1, ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableMapSound(ARG_0_3)
    IfFlagOn(-1, ARG_4_7)
    IfFlagOn(-1, ARG_8_11)
    IfConditionTrue(0, input_condition=-1)
    DisableMapSound(ARG_0_3)
    Restart()


@RestartOnRest
def Event12415770(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12415770: Event 12415770 """
    DeleteObjectFX(ARG_0_3, erase_root=True)
    EndIfFlagOn(ARG_4_7)
    CreateObjectFX(ARG_8_11, obj=ARG_0_3, model_point=200)


@RestartOnRest
def Event12415779(ARG_0_3: int):
    """ 12415779: Event 12415779 """
    CreateObjectFX(924113, obj=ARG_0_3, model_point=200)
    IfFlagOn(1, 1180)
    IfFlagOn(1, 1193)
    IfFlagOn(1, 1194)
    IfConditionTrue(0, input_condition=1)
    DeleteObjectFX(ARG_0_3, erase_root=True)


@NeverRestart
def Event12410900():
    """ 12410900: Event 12410900 """
    EndIfThisEventOn()
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2412911)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(9403)


@NeverRestart
def Event12410310():
    """ 12410310: Event 12410310 """
    GotoIfFlagOn(Label.L2, 9802)
    GotoIfFlagOn(Label.L1, 9801)
    GotoIfFlagOn(Label.L0, 9800)
    EnableMapPart(2414010)
    DisableMapPart(2414011)
    DisableMapPart(2414012)
    DisableMapPart(2414013)
    DisableMapPart(2414070)
    DisableMapPart(2414071)
    DeleteFX(2413350, erase_root_only=False)
    DeleteFX(2413380, erase_root_only=False)
    Goto(Label.L3)
    Label(0)
    DisableMapPart(2414010)
    EnableMapPart(2414011)
    DisableMapPart(2414012)
    DisableMapPart(2414013)
    DisableMapPart(2414070)
    DisableMapPart(2414071)
    DeleteFX(2413350, erase_root_only=False)
    DeleteFX(2413380, erase_root_only=False)
    Goto(Label.L3)
    Label(1)
    DisableMapPart(2414010)
    DisableMapPart(2414011)
    EnableMapPart(2414012)
    DisableMapPart(2414013)
    DisableMapPart(2414050)
    DisableMapPart(2414051)
    DeleteFX(2413300, erase_root_only=False)
    DeleteFX(2413301, erase_root_only=False)
    DeleteFX(2413302, erase_root_only=False)
    DeleteFX(2413303, erase_root_only=False)
    DeleteFX(2413304, erase_root_only=False)
    DeleteFX(2413305, erase_root_only=False)
    DeleteFX(2413380, erase_root_only=False)
    Goto(Label.L3)
    Label(2)
    DisableMapPart(2414010)
    DisableMapPart(2414011)
    DisableMapPart(2414012)
    EnableMapPart(2414013)
    DisableMapPart(2414050)
    DisableMapPart(2414051)
    DeleteFX(2413350, erase_root_only=False)
    Label(3)
    IfFlagChange(-1, 9800)
    IfFlagChange(-1, 9801)
    IfFlagChange(-1, 9802)
    IfConditionTrue(0, input_condition=-1)
    Restart()


@NeverRestart
def Event12410010():
    """ 12410010: Event 12410010 """
    EndIfFlagOn(9401)
    DisableDeveloperMessage(2413601)
    DisableDeveloperMessage(2413604)


@NeverRestart
def Event12410011():
    """ 12410011: Event 12410011 """
    End()
    EndIfThisEventOn()
    DisableDeveloperMessage(2413603)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagOn(1, 52410120)
    IfConditionTrue(0, input_condition=1)
    EnableDeveloperMessage(2413603)


@NeverRestart
def Event12410012():
    """ 12410012: Event 12410012 """
    EndIfThisEventOn()
    DisableDeveloperMessage(2413610)
    DisableDeveloperMessage(2413611)
    IfFlagOn(0, 9401)
    EnableDeveloperMessage(2413610)
    EnableDeveloperMessage(2413611)


@RestartOnRest
def Event12410170():
    """ 12410170: Event 12410170 """
    GotoIfThisEventOff(Label.L0)
    DisableBackread(2410019)
    End()
    Label(0)
    DisableHealthBar(2410019)
    AddSpecialEffect(2410019, 5617, affect_npc_part_hp=False)
    AddSpecialEffect(2410019, 5708, affect_npc_part_hp=False)
    Wait(3.0)
    EnableHealthBar(2410019)
    IfCharacterDead(0, 2410019)
    End()


@RestartOnRest
def Event12415100(ARG_0_3: int):
    """ 12415100: Event 12415100 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    ForceAnimation(ARG_0_3, 7000)
    DisableGravity(ARG_0_3)
    IfHasAIStatus(-1, 2410019, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2410019, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(2, 2)
    WaitRandomSeconds(min_seconds=1.0, max_seconds=3.0)
    ForceAnimation(ARG_0_3, 7002)
    EnableAI(ARG_0_3)
    EnableGravity(ARG_0_3)


@NeverRestart
def Event12410510():
    """ 12410510: Event 12410510 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventOn()
    GotoIfFlagOn(Label.L0, 12410511)
    IfCharacterInsideRegion(0, PLAYER, region=2412350)
    EnableFlag(12410511)
    Label(0)
    CreateObjectFX(900201, obj=2411200, model_point=200)
    IfActionButtonInRegion(0, action_button_id=2410060, region=2411200)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2410990, host_only=False)
    DeleteObjectFX(2411200, erase_root=True)


@NeverRestart
def Event12410030(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12410030: Event 12410030 """
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, skip_transition=True)
    SetAIParamID(ARG_0_3, ARG_16_19)
    DisableGravity(ARG_0_3)
    IfHasAIStatus(-1, ARG_12_15, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_12_15, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Battle)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(0, input_condition=-3)
    EnableGravity(ARG_0_3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(ARG_12_15, 3021)
    WaitRandomFrames(min_frames=20, max_frames=70)
    Label(0)
    SetAIParamID(ARG_0_3, ARG_20_23)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    ForceAnimation(ARG_0_3, ARG_8_11)


@NeverRestart
def Event12410040(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12410040: Event 12410040 """
    SetAIParamID(ARG_0_3, ARG_4_7)
    IfHasAIStatus(-1, ARG_16_19, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_16_19, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(-3, input_condition=-1)
    IfConditionTrue(-3, input_condition=-2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-2)
    ForceAnimation(ARG_16_19, ARG_20_23, wait_for_completion=True)
    IfHealthEqual(1, ARG_16_19, 1.0)
    IfHealthLessThan(2, ARG_16_19, 1.0)
    IfConditionTrue(-4, input_condition=1)
    IfConditionTrue(-4, input_condition=2)
    IfConditionTrue(0, input_condition=-4)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    SetAIParamID(ARG_0_3, ARG_8_11)
    WaitFrames(100)
    Label(0)
    SetAIParamID(ARG_0_3, ARG_12_15)


@NeverRestart
def Event12410050(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12410050: Event 12410050 """
    SetAIParamID(ARG_0_3, ARG_4_7)
    IfHasAIStatus(-1, ARG_16_19, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_16_19, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(ARG_16_19, ARG_20_23)
    SetAIParamID(ARG_0_3, ARG_8_11)
    Wait(300.0)
    SetAIParamID(ARG_0_3, ARG_12_15)


@RestartOnRest
def Event12415160(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12415160: Event 12415160 """
    WaitRandomFrames(min_frames=0, max_frames=50)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, skip_transition=True)
    DisableGravity(ARG_0_3)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableGravity(ARG_0_3)
    WaitRandomFrames(min_frames=0, max_frames=30)
    ForceAnimation(ARG_0_3, ARG_8_11, wait_for_completion=True)


@RestartOnRest
def Event12410600(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410600: Event 12410600 """
    SkipLinesIfThisEventSlotOff(4)
    EndOfAnimation(ARG_4_7, 0)
    DisableObjectActivation(ARG_4_7, obj_act_id=ARG_8_11)
    EnableTreasure(ARG_4_7)
    End()
    IfObjectActivated(0, obj_act_id=ARG_0_3)
    WaitFrames(10)
    EnableTreasure(ARG_4_7)


@RestartOnRest
def Event12410630(ARG_0_3: int, ARG_4_7: int):
    """ 12410630: Event 12410630 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventSlotOn()
    IfCharacterDead(0, ARG_0_3)
    AwardItemLot(ARG_4_7, host_only=False)


@RestartOnRest
def Event12410645():
    """ 12410645: Event 12410645 """
    EnableImmortality(2410703)
    DisableHealthBar(2410703)
    IfFlagOn(10, 1140)
    GotoIfConditionFalse(Label.L9, input_condition=10)
    DisableBackread(2410703)
    Label(9)
    IfFlagOn(1, 1141)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    EnableBackread(2410710)
    DisableBackread(2410711)
    DisableAnimations(2410710)
    Label(0)
    IfFlagOn(2, 1142)
    GotoIfConditionFalse(Label.L7, input_condition=2)
    EnableBackread(2410710)
    DisableBackread(2410711)
    DisableAnimations(2410710)
    Label(7)
    IfFlagOn(8, 1143)
    GotoIfConditionFalse(Label.L8, input_condition=8)
    EnableBackread(2410710)
    DisableBackread(2410711)
    Label(8)
    IfFlagOn(9, 1144)
    GotoIfConditionFalse(Label.L1, input_condition=9)
    EnableBackread(2410710)
    DisableBackread(2410711)
    DisableAnimations(2410710)
    Label(1)
    IfFlagOn(3, 1145)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableBackread(2410703)
    EnableBackread(2410710)
    DisableBackread(2410711)
    Move(2410710, destination=2412172, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=0)
    SetNest(2410710, 2412172)
    SetTeamType(2410710, TeamType.Enemy1)
    Label(2)
    IfFlagOn(4, 1146)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableBackread(2410703)
    DisableBackread(2410710)
    EnableBackread(2410711)
    ForceAnimation(2410711, 103000)
    Label(3)
    IfFlagOn(5, 1147)
    GotoIfConditionFalse(Label.L4, input_condition=5)
    DisableBackread(2410703)
    DisableBackread(2410710)
    DisableBackread(2410711)
    DisableBackread(2410703)
    Label(4)
    IfFlagOn(6, 1148)
    GotoIfConditionFalse(Label.L5, input_condition=6)
    DisableBackread(2410703)
    DisableBackread(2410710)
    DisableBackread(2410711)
    Move(2410710, destination=2412172, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=0)
    WaitFrames(1)
    DropMandatoryTreasure(2410710)
    Label(5)
    IfFlagOn(7, 1149)
    EndIfConditionFalse(7)
    DisableBackread(2410703)
    DisableBackread(2410710)
    EnableBackread(2410711)
    EzstateAIRequest(2410711, command_id=0, slot=1)
    DropMandatoryTreasure(2410711)


@RestartOnRest
def Event12410650():
    """ 12410650: Event 12410650 """
    Label(0)
    IfFlagRangeAllOff(0, (1141, 1159))
    DisableBackread(2410710)
    DisableFlagRange((1140, 1159))
    EnableFlag(1140)


@RestartOnRest
def Event12410651():
    """ 12410651: Event 12410651 """
    EndIfFlagOn(1148)
    EndIfFlagOn(1149)
    EndIfFlagOn(1141)
    EndIfThisEventOn()
    IfFlagOn(0, 9800)
    EnableBackread(2410703)
    EnableBackread(2410710)
    DisableAnimations(2410710)
    DisableFlagRange((1140, 1159))
    EnableFlag(1141)


@RestartOnRest
def Event12410652():
    """ 12410652: Event 12410652 """
    EndIfFlagOn(1148)
    EndIfFlagOn(1149)
    EndIfThisEventOn()
    IfFlagOn(1, 72410320)
    IfFlagOn(1, 1141)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1140, 1159))
    EnableFlag(1142)


@RestartOnRest
def Event12410653():
    """ 12410653: Event 12410653 """
    EndIfFlagOn(1148)
    EndIfFlagOn(1149)
    EndIfFlagOn(1145)
    EndIfFlagOn(1146)
    IfCharacterInsideRegion(1, PLAYER, region=2412170)
    IfFlagOff(1, 1140)
    IfFlagOff(1, 1145)
    IfFlagOff(1, 1146)
    IfFlagOff(1, 1147)
    IfFlagOff(1, 1148)
    IfFlagOff(1, 1149)
    IfCharacterAlive(1, 2410710)
    IfConditionTrue(0, input_condition=1)
    SetDistanceLimitForConversationStateChanges(2410710, distance=40.5)
    DisableFlagRange((1140, 1159))
    EnableFlag(1143)
    Restart()


@RestartOnRest
def Event12410654():
    """ 12410654: Event 12410654 """
    EndIfFlagOn(1148)
    EndIfFlagOn(1149)
    EndIfFlagOn(1145)
    EndIfFlagOn(1146)
    IfFlagOn(1, 1143)
    IfCharacterInsideRegion(1, PLAYER, region=2412171)
    IfConditionTrue(0, input_condition=1)
    SetDistanceLimitForConversationStateChanges(2410710, distance=17.0)
    DisableFlagRange((1140, 1159))
    EnableFlag(1144)
    Restart()


@RestartOnRest
def Event12410655():
    """ 12410655: Event 12410655 """
    EndIfFlagOn(1148)
    EndIfFlagOn(1149)
    Label(0)
    DisableAI(2410710)
    IfCharacterInsideRegion(1, PLAYER, region=2412190)
    IfFlagOff(1, 1140)
    IfFlagOff(1, 1146)
    IfFlagOff(1, 1147)
    IfFlagOff(1, 1148)
    IfFlagOff(1, 1149)
    IfConditionTrue(0, input_condition=1)
    EnableAI(2410710)
    SetTeamType(2410710, TeamType.Enemy1)
    DisableFlagRange((1140, 1159))
    EnableFlag(1145)
    SaveRequest()


@RestartOnRest
def Event12410656():
    """ 12410656: Event 12410656 """
    EndIfFlagOn(1148)
    EndIfFlagOn(1149)
    IfFlagOn(1, 9802)
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
    EndIfFlagOn(1148)
    EndIfFlagOn(1149)
    EndIfFlagOn(1147)
    IfFlagOn(0, 72410326)
    DisableBackread(2410703)
    DisableFlagRange((1140, 1159))
    EnableFlag(1147)
    SaveRequest()


@RestartOnRest
def Event12410658():
    """ 12410658: Event 12410658 """
    EndIfFlagOn(1149)
    IfHealthLessThanOrEqual(1, 2410710, 0.0)
    IfFlagOn(1, 1145)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1140, 1159))
    EnableFlag(1148)
    SaveRequest()


@RestartOnRest
def Event12410659():
    """ 12410659: Event 12410659 """
    IfCharacterInsideRegion(1, PLAYER, region=2412170)
    IfFlagOn(1, 1143)
    IfCharacterInsideRegion(2, PLAYER, region=2412171)
    IfFlagOff(2, 62411300)
    IfFlagOn(2, 1144)
    IfCharacterInsideRegion(3, PLAYER, region=2412171)
    IfFlagOn(3, 1147)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    Move(2410710, destination=2412172, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=0)
    SetNest(2410710, 2412172)
    EnableFlag(72410337)
    EnableAnimations(2410710)
    DisableBackread(2410703)
    Restart()
    Label(0)
    Move(2410710, destination=2412173, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=0)
    SetNest(2410710, 2412173)
    DisableFlag(72410337)
    DisableAnimations(2410710)
    EnableBackread(2410703)
    Restart()
    Label(1)
    DisableBackread(2410710)


@RestartOnRest
def Event12410661():
    """ 12410661: Event 12410661 """
    IfEventValueComparison(0, 12410646, bit_count=4, comparison_type=ComparisonType.GreaterThanOrEqual, value=4)
    EnableFlag(72410328)


@RestartOnRest
def Event12410662(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410662: Event 12410662 """
    EndIfThisEventSlotOn()
    IfFlagOn(1, ARG_0_3)
    IfFlagOn(1, 1142)
    IfFlagOn(2, ARG_0_3)
    IfFlagOn(2, 1144)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    IncrementEventValue(12410646, bit_count=4, max_value=10)
    EnableFlag(ARG_8_11)
    DisableFlagRange((72410331, 72410332))
    EnableFlag(ARG_4_7)
    End()
    Label(0)
    IncrementEventValue(12410646, bit_count=4, max_value=10)
    EnableFlag(ARG_8_11)
    DisableFlagRange((72410331, 72410332))
    EnableFlag(72410334)


@RestartOnRest
def Event12410668():
    """ 12410668: Event 12410668 """
    EndIfThisEventOn()
    IfFlagOn(1, 1163)
    IfFlagOn(1, 1204)
    IfFlagOn(1, 1268)
    IfFlagOn(1, 1190)
    IfFlagOn(1, 1223)
    IfFlagOn(1, 1309)
    IfFlagOn(1, 72410336)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((72410331, 72410332))
    EnableFlag(72410333)


@RestartOnRest
def Event12410669(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410669: Event 12410669 """
    GotoIfThisEventSlotOff(Label.L0)
    EnableCharacter(ARG_0_3)
    WaitFrames(1)
    ForceAnimation(ARG_0_3, ARG_8_11, loop=True)
    End()
    Label(0)
    DisableCharacter(ARG_0_3)
    IfFlagOn(0, ARG_4_7)
    EnableCharacter(ARG_0_3)
    WaitFrames(1)
    ForceAnimation(ARG_0_3, ARG_8_11, loop=True)


@RestartOnRest
def Event12410676():
    """ 12410676: Event 12410676 """
    IfCharacterHuman(1, PLAYER)
    IfDamageType(1, attacked_entity=2410703, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfFlagOn(-1, 1141)
    IfFlagOn(-1, 1142)
    IfFlagOn(-1, 1144)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagRangeState(Label.L0, RangeState.AllOn, FlagType.Absolute, (72410344, 72410346))
    GotoIfFlagOff(Label.L3, 72410320)
    GotoIfFlagOff(Label.L2, 72410344)
    GotoIfFlagOff(Label.L1, 72410345)
    EnableFlag(72410346)
    Label(1)
    EnableFlag(72410345)
    Label(2)
    EnableFlag(72410344)
    Label(3)
    EnableFlag(72410329)
    IfFlagOff(0, 72410329)
    Restart()
    Label(0)
    EnableFlag(72410329)
    SaveRequest()


@NeverRestart
def Event12410677():
    """ 12410677: Event 12410677 """
    EndIfFlagOn(1148)
    EndIfFlagOn(1149)
    IfFlagOn(1, 1146)
    IfAttacked(1, 2410711, attacking_character=10000)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2410711, 103001)
    Kill(2410711, award_souls=True)
    DisableFlagRange((1140, 1159))
    EnableFlag(1149)
    SaveRequest()


@NeverRestart
def Event12410680(ARG_0_3: int):
    """ 12410680: Event 12410680 """
    IfAttacked(0, ARG_0_3, attacking_character=10000)
    SetAIParamID(ARG_0_3, 250000)


@NeverRestart
def Event12410687(ARG_0_3: int, ARG_4_7: int):
    """ 12410687: Event 12410687 """
    EndIfFlagOn(ARG_0_3)
    IfFlagOn(0, ARG_4_7)
    RunEvent(9350, slot=0, args=(1,))


@NeverRestart
def Event12410693(ARG_0_3: int, ARG_4_7: int):
    """ 12410693: Event 12410693 """
    EndIfFlagOn(ARG_0_3)
    IfFlagOn(0, ARG_4_7)
    RunEvent(9350, slot=0, args=(2,))


@NeverRestart
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


@NeverRestart
def Event12410701():
    """ 12410701: Event 12410701 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(9, 1261)
    IfFlagOn(9, 9800)
    GotoIfConditionFalse(Label.L8, input_condition=9)
    DisableFlagRange((1260, 1279))
    EnableFlag(1262)
    Label(8)
    IfFlagOn(1, 1260)
    IfFlagOn(1, 9801)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableFlagRange((1260, 1279))
    EnableFlag(1270)
    Label(0)
    IfFlagOn(-1, 1260)
    IfFlagOn(-1, 1261)
    IfFlagOn(-1, 1262)
    IfConditionTrue(2, input_condition=-1)
    IfFlagOn(2, 9801)
    GotoIfConditionFalse(Label.L9, input_condition=2)
    DisableFlagRange((1260, 1279))
    EnableFlag(1263)
    Label(9)
    IfFlagOn(10, 1263)
    IfFlagOn(-3, 9802)
    IfFlagOn(-3, 72410407)
    IfConditionTrue(10, input_condition=-3)
    GotoIfConditionFalse(Label.L1, input_condition=10)
    DisableFlagRange((1260, 1279))
    EnableFlag(1269)
    Label(1)
    IfFlagOn(3, 1264)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    DisableFlagRange((1260, 1279))
    EnableFlag(1267)
    Label(2)
    IfFlagOn(4, 1265)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableFlagRange((1260, 1279))
    EnableFlag(1267)
    Label(3)
    IfFlagOn(5, 1266)
    GotoIfConditionFalse(Label.L4, input_condition=5)
    DisableFlagRange((1260, 1279))
    EnableFlag(1268)
    Label(4)
    IfFlagOn(6, 1270)
    IfFlagOn(-2, 9802)
    IfFlagOn(-2, 72410415)
    IfConditionTrue(6, input_condition=-2)
    GotoIfConditionFalse(Label.L7, input_condition=6)
    DisableFlagRange((1260, 1279))
    EnableFlag(1269)
    Label(7)
    IfFlagOn(12, 9802)
    IfFlagOn(-4, 1267)
    IfConditionTrue(12, input_condition=-4)
    GotoIfConditionFalse(Label.L5, input_condition=12)
    DisableFlagRange((1260, 1279))
    EnableFlag(1271)
    Label(5)
    IfFlagOn(7, 1272)
    GotoIfConditionFalse(Label.L6, input_condition=7)
    DisableFlagRange((1260, 1279))
    EnableFlag(1273)
    Label(6)


@NeverRestart
def Event12410702():
    """ 12410702: Event 12410702 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    DisableFlag(72410414)
    Label(0)
    DisableObject(2410761)
    DisableHealthBar(2410762)
    EnableImmortality(2410762)
    GotoIfFlagOn(Label.L1, 1273)
    DisableObject(2410851)
    DisableTreasure(2410851)
    End()
    Label(1)
    EnableObject(2410851)
    EnableTreasure(2410851)
    PostDestruction(2410852, slot=1)
    End()


@NeverRestart
def Event12410703():
    """ 12410703: Event 12410703 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 12411802)
    IfFlagOn(1, 1260)
    IfFlagOn(1, 72410413)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1260, 1279))
    EnableFlag(1261)


@NeverRestart
def Event12410704():
    """ 12410704: Event 12410704 """
    IfFlagOn(0, 72410403)
    DisableFlag(72410403)
    DisableFlagRange((1260, 1279))
    EnableFlag(1264)


@NeverRestart
def Event12410705():
    """ 12410705: Event 12410705 """
    IfFlagOn(0, 72410404)
    DisableFlag(72410404)
    DisableFlagRange((1260, 1279))
    EnableFlag(1265)


@NeverRestart
def Event12410706():
    """ 12410706: Event 12410706 """
    IfFlagOn(0, 72410405)
    DisableFlag(72410405)
    DisableFlagRange((1260, 1279))
    EnableFlag(1266)


@NeverRestart
def Event12410710():
    """ 12410710: Event 12410710 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(72410406)
    DisableHealthBar(2410762)
    IfAttacked(0, 2410762, attacking_character=10000)
    EnableFlag(72410406)
    Wait(2.0)
    Restart()


@NeverRestart
def Event12410713():
    """ 12410713: Event 12410713 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EnableFlag(72410410)
    IfFlagOn(-1, 1271)
    IfFlagOn(-1, 1267)
    IfConditionTrue(0, input_condition=-1)
    IfPlayerDoesNotHaveGood(1, 4904, including_box=False)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(72410410)


@NeverRestart
def Event12410715():
    """ 12410715: Event 12410715 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOff(Label.L0, 1269)
    DisableMapSound(2413100)
    End()
    Label(0)
    GotoIfFlagOff(Label.L1, 72410402)
    DisableMapSound(2413100)
    End()
    Label(1)
    EnableMapSound(2413100)
    DisableFlag(72410412)
    IfFlagOff(1, 1270)
    IfFlagOn(1, 72410412)
    IfConditionTrue(0, input_condition=1)
    DisableMapSound(2413100)


@NeverRestart
def Event12410716():
    """ 12410716: Event 12410716 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L1, 1267)
    GotoIfFlagOn(Label.L1, 1268)
    GotoIfFlagOn(Label.L1, 1269)
    GotoIfFlagOn(Label.L1, 1273)
    End()
    Label(1)
    DeleteFX(2413701, erase_root_only=False)


@NeverRestart
def Event12410721():
    """ 12410721: Event 12410721 """
    IfFlagOn(0, 72410421)
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
    IfFlagOn(1, 1120)
    GotoIfConditionFalse(Label.L0, input_condition=1)
    DisableBackread(2410702)
    DisableCharacter(2410700)
    Label(0)
    IfFlagOn(2, 1121)
    GotoIfConditionFalse(Label.L1, input_condition=2)
    EnableBackread(2410702)
    Label(1)
    IfFlagOn(3, 1122)
    GotoIfConditionFalse(Label.L2, input_condition=3)
    EnableBackread(2410702)
    Label(2)
    IfFlagOn(4, 1123)
    GotoIfConditionFalse(Label.L3, input_condition=4)
    DisableBackread(2410702)
    DisableBackread(2410700)
    Label(3)
    IfFlagOn(5, 1124)
    EndIfConditionFalse(5)
    DisableBackread(2410702)
    DisableBackread(2410700)


@RestartOnRest
def Event12410730():
    """ 12410730: Event 12410730 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 9401)
    IfFlagOn(1, 1120)
    IfConditionTrue(0, input_condition=1)
    EnableBackread(2410702)
    DisableFlagRange((1120, 1124))
    EnableFlag(1121)


@RestartOnRest
def Event12410731():
    """ 12410731: Event 12410731 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 72410305)
    IfFlagOn(1, 1121)
    IfFlagOn(2, 1123)
    IfFlagOn(3, 1124)
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
    IfFlagOn(1, 72410309)
    IfFlagOn(-2, 1121)
    IfFlagOn(-2, 1122)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(2, 1123)
    IfFlagOn(3, 1124)
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
    IfFlagOn(0, 9800)
    DisableFlagRange((1120, 1124))
    EnableFlag(1124)
    DisableCharacter(2410700)
    DisableBackread(2410702)


@RestartOnRest
def Event12410734():
    """ 12410734: Event 12410734 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfAttacked(0, 2410702, attacking_character=10000)
    EnableFlag(72410306)
    Wait(2.0)
    Restart()


@NeverRestart
def Event12410736():
    """ 12410736: Event 12410736 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 72410301)
    IfFlagOff(2, 72410301)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    DisableFlag(72410301)


@NeverRestart
def Event12410737():
    """ 12410737: Event 12410737 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableCharacter(2410700)
    IfFlagOn(-1, 1121)
    IfFlagOn(-1, 1122)
    IfFlagOn(-1, 1123)
    IfConditionTrue(0, input_condition=-1)
    EnableCharacter(2410700)
    DisableAnimations(2410700)


@NeverRestart
def Event12410738():
    """ 12410738: Event 12410738 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L0, 72410311)
    IfCharacterBackreadDisabled(1, 2410700)
    IfFlagOn(1, 72410311)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    DisableFlag(72410311)
    Restart()


@NeverRestart
def Event12410739():
    """ 12410739: Event 12410739 """
    IfCharacterInsideRegion(1, PLAYER, region=2412170)
    IfFlagOn(-3, 1143)
    IfFlagRangeAnyOn(-3, (1145, 1149))
    IfConditionTrue(1, input_condition=-3)
    IfFlagOn(1, 9800)
    IfCharacterBackreadDisabled(1, 2410290)
    IfCharacterInsideRegion(2, PLAYER, region=2412171)
    IfFlagOff(2, 62411300)
    IfFlagOn(2, 1144)
    IfFlagOn(2, 9800)
    IfCharacterBackreadEnabled(2, 2410290)
    IfFlagOn(-2, 1141)
    IfFlagOn(-2, 1142)
    IfConditionTrue(3, input_condition=-2)
    IfCharacterBackreadEnabled(3, 2410290)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=1)
    EnableBackread(2410290)
    Restart()
    Label(0)
    DisableBackread(2410290)
    Restart()


@NeverRestart
def Event12410740():
    """ 12410740: Event 12410740 """
    EndIfClient()
    GotoIfFlagOn(Label.L1, 1180)
    End()
    Label(1)


@NeverRestart
def Event12410741():
    """ 12410741: Event 12410741 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 1180)
    IfFlagOn(1, 9802)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1180, 1199))
    EnableFlag(1195)
    SaveRequest()


@NeverRestart
def Event12410742():
    """ 12410742: Event 12410742 """
    IfFlagOn(0, 72410390)
    DisableFlag(72410390)
    DisableFlagRange((1180, 1199))
    EnableFlag(1193)


@NeverRestart
def Event12410743():
    """ 12410743: Event 12410743 """
    IfFlagOn(0, 72410391)
    DisableFlag(72410391)
    DisableFlagRange((1180, 1199))
    EnableFlag(1194)


@NeverRestart
def Event12410744():
    """ 12410744: Event 12410744 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L0, 1193)
    End()
    Label(0)
    DisableFlagRange((1180, 1199))
    EnableFlag(1181)


@NeverRestart
def Event12410745():
    """ 12410745: Event 12410745 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L0, 1194)
    End()
    Label(0)
    DisableFlagRange((1180, 1199))
    EnableFlag(1190)


@NeverRestart
def Event12410746():
    """ 12410746: Event 12410746 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOn(Label.L0, 72410382)
    GotoIfFlagOn(Label.L0, 9802)
    DisableAI(2410111)
    End()
    Label(0)
    DisableBackread(2410111)


@NeverRestart
def Event12410747():
    """ 12410747: Event 12410747 """
    IfEntityWithinDistance(-1, 10000, 2410111, radius=3.0)
    IfDamageType(-1, attacked_entity=2410111, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(2410111)


@NeverRestart
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


@NeverRestart
def Event12410749():
    """ 12410749: Event 12410749 """
    IfCharacterBackreadEnabled(0, 2410111)
    IfHasAIStatus(-1, 2410111, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 2410111, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, 2410111, ai_status=AIStatusType.Battle)
    GotoIfConditionFalse(Label.L0, input_condition=-1)
    End()
    Label(0)
    ForceAnimation(2410111, 3023, wait_for_completion=True)
    IfRandomFramesElapsed(0, min_frames=30, max_frames=60)
    Restart()


@NeverRestart
def Event12410750(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410750: Event 12410750 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 72410382)
    DisableFlag(ARG_0_3)
    IfFlagOff(1, ARG_0_3)
    IfActionButtonInRegion(1, action_button_id=ARG_4_7, region=ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=ARG_8_11, destination_type=CoordEntityType.Object, model_point=210, short_move=True)
    ForceAnimation(PLAYER, 101320)
    WaitFrames(25)
    WaitFrames(20)
    EnableFlag(ARG_0_3)
    IfFlagOff(0, ARG_0_3)
    Restart()


@NeverRestart
def Event12410760():
    """ 12410760: Event 12410760 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    DisableFlag(72410513)
    DisableFlag(72410514)
    DisableFlag(72410515)
    DisableFlag(72410516)
    Label(0)
    DisableHealthBar(2410782)
    EnableImmortality(2410782)
    GotoIfFlagOn(Label.L1, 1240)
    GotoIfFlagOn(Label.L1, 1241)
    GotoIfFlagOn(Label.L1, 1242)
    GotoIfFlagOn(Label.L1, 1243)
    GotoIfFlagOn(Label.L1, 1244)
    GotoIfFlagOn(Label.L2, 1246)
    GotoIfFlagOn(Label.L3, 1245)
    DisableBackread(2410781)
    DeleteFX(2413700, erase_root_only=False)
    End()
    Label(1)
    DisableBackread(2410781)
    End()
    Label(2)
    EnableBackread(2410781)
    DestroyObject(2410784, slot=1)
    DeleteFX(2413700, erase_root_only=False)
    End()
    Label(3)
    DisableCharacter(2410781)
    DestroyObject(2410784, slot=1)
    DeleteFX(2413700, erase_root_only=False)
    DropMandatoryTreasure(2410781)
    End()


@NeverRestart
def Event12410761():
    """ 12410761: Event 12410761 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(1, 2410781)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1240, 1259))
    EnableFlag(1245)
    SaveRequest()


@NeverRestart
def Event12410762():
    """ 12410762: Event 12410762 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1245)
    IfFlagOn(-1, 9800)
    IfFlagOn(-1, 9801)
    IfFlagOn(-1, 9802)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOn(1, 1240)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    Goto(Label.L1)
    Label(0)
    DisableFlagRange((1240, 1259))
    EnableFlag(1241)
    Label(1)
    IfFlagOn(-2, 9801)
    IfFlagOn(-2, 9802)
    IfConditionTrue(2, input_condition=-2)
    IfFlagOn(2, 1241)
    GotoIfConditionTrue(Label.L2, input_condition=2)
    Goto(Label.L3)
    Label(2)
    DisableFlagRange((1240, 1259))
    EnableFlag(1242)
    Label(3)
    IfFlagOn(3, 1242)
    IfFlagOn(3, 72410504)
    IfConditionTrue(-3, input_condition=3)
    IfFlagOn(-3, 9802)
    GotoIfConditionTrue(Label.L4, input_condition=-3)
    Goto(Label.L5)
    Label(4)
    DisableFlagRange((1240, 1259))
    EnableFlag(1243)
    Label(5)
    IfFlagOn(4, 9802)
    IfFlagOn(4, 1243)
    GotoIfConditionTrue(Label.L6, input_condition=4)
    End()
    Label(6)
    DisableFlagRange((1240, 1259))
    EnableFlag(1246)


@NeverRestart
def Event12410763():
    """ 12410763: Event 12410763 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfDamageType(1, attacked_entity=2410782, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfFlagOn(-1, 1240)
    IfFlagOn(-1, 1241)
    IfFlagOn(-1, 1242)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfFlagRangeState(Label.L0, RangeState.AllOn, FlagType.Absolute, (72410515, 72410516))
    GotoIfFlagOff(Label.L2, 72410500)
    GotoIfFlagOff(Label.L1, 72410515)
    EnableFlag(72410516)
    Label(1)
    EnableFlag(72410515)
    Label(2)
    EnableFlag(72410513)
    IfFlagOn(0, 72410514)
    IfFlagOff(0, 72410514)
    Restart()
    Label(0)
    EnableFlag(72410513)
    DisableFlagRange((1240, 1259))
    EnableFlag(1244)
    SaveRequest()


@NeverRestart
def Event12410770(ARG_0_3: int):
    """ 12410770: Event 12410770 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableCharacter(ARG_0_3)
    DropMandatoryTreasure(ARG_0_3)
    End()
    Label(0)
    IfCharacterDead(0, ARG_0_3)
    WaitFrames(1)


@RestartOnRest
def Event12410780():
    """ 12410780: Event 12410780 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1293)
    GotoIfFlagOn(Label.L0, 12410785)
    DisableFlagRange((1280, 1299))
    EnableFlag(1290)
    Goto(Label.L9)
    Label(0)
    DisableFlagRange((1280, 1299))
    EnableFlag(1291)
    Goto(Label.L9)
    Label(9)
    SetDistanceLimitForConversationStateChanges(2410810, distance=80.0)
    End()


@RestartOnRest
def Event12410785():
    """ 12410785: Event 12410785 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1293)
    IfFlagOn(1, 1290)
    IfFlagOn(1, 72410530)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1280, 1299))
    EnableFlag(1291)


@RestartOnRest
def Event12410786():
    """ 12410786: Event 12410786 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1293)
    IfFlagOn(-1, 1290)
    IfFlagOn(-1, 1291)
    IfFlagOn(1, 12414807)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1290, 1299))
    EnableFlag(1292)


@RestartOnRest
def Event12410787():
    """ 12410787: Event 12410787 """
    EndIfThisEventOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, 12411800)
    DisableFlagRange((1290, 1299))
    EnableFlag(1293)
    SetDistanceLimitForConversationStateChanges(2410810, distance=17.0)
    SaveRequest()


@NeverRestart
def Event12410800():
    """ 12410800: Event 12410800 """
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1370, 1375))
    GotoIfFlagOn(Label.L1, 1369)
    GotoIfFlagOn(Label.L2, 1368)
    GotoIfFlagOn(Label.L3, 1367)
    GotoIfFlagOn(Label.L4, 1366)
    GotoIfFlagOn(Label.L5, 1365)
    GotoIfFlagOn(Label.L6, 1364)
    GotoIfFlagRangeState(Label.L7, RangeState.AnyOn, FlagType.Absolute, (1362, 1363))
    GotoIfFlagRangeState(Label.L8, RangeState.AnyOn, FlagType.Absolute, (1360, 1361))
    Label(0)
    DisableBackread(2410900)
    Goto(Label.L9)
    Label(1)
    SkipLinesIfFlagOff(2, 1705)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagOff(2, 1704)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagOff(2, 1701)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagOff(4, 1703)
    Move(2410900, destination=2412334, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414124)
    SetNest(2410900, 2412334)
    SetTeamType(2410900, TeamType.HostileNPC)
    Goto(Label.L9)
    SkipLinesIfFlagOff(4, 1702)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414122)
    SetNest(2410900, 2412332)
    SetTeamType(2410900, TeamType.HostileNPC)
    Goto(Label.L9)
    SetNest(2410900, 2412332)
    SetTeamType(2410900, TeamType.HostileNPC)
    Goto(Label.L9)
    Label(2)
    SkipLinesIfFlagOff(2, 1705)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagOff(2, 1704)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagOff(2, 1701)
    DisableBackread(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagOff(6, 1703)
    DisableBackread(2410900)
    DisableCharacter(2410900)
    Move(2410900, destination=2412334, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414124)
    WaitFrames(1)
    DropMandatoryTreasure(2410900)
    Goto(Label.L9)
    SkipLinesIfFlagOff(6, 1702)
    DisableBackread(2410900)
    DisableCharacter(2410900)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414122)
    WaitFrames(1)
    DropMandatoryTreasure(2410900)
    Goto(Label.L9)
    DisableBackread(2410900)
    DisableCharacter(2410900)
    DropMandatoryTreasure(2410900)
    Goto(Label.L9)
    Label(3)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414122)
    SetNest(2410900, 2412332)
    DisableFlag(72410546)
    Goto(Label.L9)
    Label(4)
    Move(2410900, destination=2412334, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414124)
    SetNest(2410900, 2412334)
    DisableFlag(72410546)
    Goto(Label.L9)
    Label(5)
    Move(2410900, destination=2412332, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414122)
    SetNest(2410900, 2412332)
    SetTeamType(2410900, TeamType.CoopNPC)
    EnableFlag(72410546)
    WaitFrames(2)
    AddSpecialEffect(2410900, 7608, affect_npc_part_hp=False)
    Goto(Label.L9)
    Label(6)
    DisableCharacter(2410900)
    Goto(Label.L9)
    Label(7)
    DisableBackread(2410900)
    Goto(Label.L9)
    Label(8)
    ForceAnimation(2410900, 103030)
    Goto(Label.L9)
    Label(9)
    RunEvent(12410801)
    RunEvent(12410803)
    RunEvent(12410804)
    RunEvent(12410805)
    RunEvent(12410806)
    RunEvent(12410807)
    RunEvent(12410808)


@NeverRestart
def Event12410801():
    """ 12410801: Event 12410801 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 1360)
    IfFlagOn(1, 72410540)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1361)


@NeverRestart
def Event12410803():
    """ 12410803: Event 12410803 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(1, 1363)
    IfCharacterDead(1, 2410901)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1366)


@NeverRestart
def Event12410804():
    """ 12410804: Event 12410804 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(-1, 1364)
    IfFlagOn(-1, 1365)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterDead(1, 2410901)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1360, 1379))
    EnableFlag(1367)


@NeverRestart
def Event12410805():
    """ 12410805: Event 12410805 """
    EndIfThisEventOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterDead(0, 2410900)
    SkipLinesIfFlagOn(9, 1369)
    DisableFlagRange((1700, 1705))
    SkipLinesIfFlagRangeAllOff(1, (1360, 1361))
    EnableFlag(1700)
    SkipLinesIfFlagOff(1, 1365)
    EnableFlag(1702)
    SkipLinesIfFlagOff(1, 1366)
    EnableFlag(1703)
    SkipLinesIfFlagOff(1, 1367)
    EnableFlag(1702)
    DisableFlagRange((1360, 1379))
    EnableFlag(1368)
    SaveRequest()


@NeverRestart
def Event12410806():
    """ 12410806: Event 12410806 """
    EndIfThisEventOn()
    IfCharacterAlive(1, 2410900)
    IfFlagOn(1, 72410544)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1700, 1705))
    SkipLinesIfFlagRangeAllOff(1, (1360, 1361))
    EnableFlag(1700)
    SkipLinesIfFlagOff(1, 1365)
    EnableFlag(1702)
    SkipLinesIfFlagOff(1, 1366)
    EnableFlag(1703)
    SkipLinesIfFlagOff(1, 1367)
    EnableFlag(1702)
    DisableFlagRange((1360, 1379))
    EnableFlag(1369)
    SetTeamType(2410900, TeamType.HostileNPC)
    SaveRequest()


@NeverRestart
def Event12410807():
    """ 12410807: Event 12410807 """
    EndIfThisEventOn()
    IfFlagOff(-1, 1364)
    IfFlagOff(-1, 1365)
    IfConditionTrue(1, input_condition=-1)
    IfAttacked(1, 2410900, attacking_character=10000)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    IfFlagOff(-2, 1364)
    IfFlagOff(-2, 1365)
    IfConditionTrue(2, input_condition=-2)
    IfAttacked(2, 2410900, attacking_character=10000)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(1)
    IfFlagOff(-3, 1364)
    IfFlagOff(-3, 1365)
    IfConditionTrue(3, input_condition=-3)
    IfAttacked(3, 2410900, attacking_character=10000)
    IfConditionTrue(0, input_condition=3)
    WaitFrames(1)


@RestartOnRest
def Event12410808():
    """ 12410808: Event 12410808 """
    IfFlagOn(0, 72410545)
    ReplanAI(2410900)
    AICommand(2410900, command_id=30, slot=0)
    IfFlagOff(-1, 72410545)
    IfHasAIStatus(-1, 2410900, ai_status=AIStatusType.Battle)
    IfEntityBeyondDistance(-1, 2410900, 10000, radius=5.0)
    IfConditionTrue(0, input_condition=-1)
    ReplanAI(2410900)
    AICommand(2410900, command_id=-1, slot=0)
    DisableFlag(72410545)
    Restart()


@NeverRestart
def Event12410809():
    """ 12410809: Event 12410809 """
    DisableBackread(2410901)
    EndIfFlagOn(12410810)
    EndIfFlagOn(1366)
    EndIfFlagOn(1367)
    EndIfFlagOn(9467)
    EndIfFlagOn(9802)
    IfFlagOn(-1, 1363)
    IfFlagOn(-1, 1364)
    IfFlagOn(-1, 1365)
    IfFlagOn(-2, 1701)
    IfFlagOn(-2, 1702)
    IfConditionTrue(1, input_condition=-2)
    IfFlagOn(-3, 1368)
    IfFlagOn(-3, 1369)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    EnableBackread(2410901)


@NeverRestart
def Event12410810():
    """ 12410810: Event 12410810 """
    GotoIfThisEventOff(Label.L0)
    DisableBackread(2410901)
    DisableCharacter(2410901)
    DropMandatoryTreasure(2410901)
    End()
    Label(0)
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
    EndIfThisEventOn()
    IfFlagOn(-1, 1363)
    IfFlagOn(-1, 1364)
    IfConditionTrue(1, input_condition=-1)
    IfHasAIStatus(1, 2410901, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=1)
    EnableBackread(2410900)
    Move(2410900, destination=2412333, destination_type=CoordEntityType.Region, model_point=-1, copy_draw_hitbox=2414123)
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


@NeverRestart
def Event12410812():
    """ 12410812: Event 12410812 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOff(Label.L0, 1169)
    DisableFlagRange((1160, 1179))
    EnableFlag(1163)
    Label(0)
    End()


@NeverRestart
def Event12410813():
    """ 12410813: Event 12410813 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOff(Label.L0, 1314)
    DisableFlagRange((1300, 1319))
    EnableFlag(1309)
    Label(0)
    End()


@NeverRestart
def Event12410814():
    """ 12410814: Event 12410814 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfFlagOff(Label.L0, 1209)
    DisableFlagRange((1200, 1219))
    EnableFlag(1204)
    Label(0)
    End()


@NeverRestart
def Event12410830():
    """ 12410830: Event 12410830 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    GotoIfFlagOff(Label.L2, 1233)
    DisableFlagRange((1220, 1239))
    EnableFlag(1223)
    Label(2)
    IfFlagOn(2, 1228)
    IfFlagOn(2, 72400486)
    GotoIfConditionFalse(Label.L3, input_condition=2)
    DisableFlagRange((1220, 1239))
    EnableFlag(1229)
    Label(3)
    Label(0)
    DisableGravity(2410770)
    DisableCollision(2410770)
    GotoIfFlagOn(Label.L0, 1228)
    GotoIfFlagOn(Label.L0, 1229)
    GotoIfFlagOn(Label.L1, 1235)
    GotoIfFlagOn(Label.L2, 1236)
    DisableCharacter(2410770)
    DisableBackread(2410771)
    DisableObject(2411280)
    EnableObject(2411281)
    End()
    Label(0)
    EnableBackread(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    DisableAI(2410771)
    ForceAnimation(2410770, 103082)
    ForceAnimation(2410771, 7010, loop=True)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    Label(1)
    EnableBackread(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    EzstateAIRequest(2410770, command_id=5, slot=1)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2410770)
    DropMandatoryTreasure(2410771)
    End()
    Label(2)
    EnableBackread(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    EzstateAIRequest(2410770, command_id=4, slot=1)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    DropMandatoryTreasure(2410770)
    DropMandatoryTreasure(2410771)
    End()


@NeverRestart
def Event12410831():
    """ 12410831: Event 12410831 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1235)
    EndIfFlagOn(1236)
    IfCharacterDead(1, 2410770)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1220, 1239))
    EnableFlag(1235)
    SaveRequest()


@NeverRestart
def Event12410833():
    """ 12410833: Event 12410833 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(1235)
    EndIfFlagOn(1236)
    IfHealthEqual(1, 2410771, 0.0)
    IfHealthNotEqual(1, 2410770, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlagRange((1220, 1239))
    EnableFlag(1236)
    WaitFrames(1)
    ForceAnimation(2410770, 103083)
    SaveRequest()


@NeverRestart
def Event12410834():
    """ 12410834: Event 12410834 """
    EndIfThisEventOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    WaitFrames(10)
    IfFlagOn(-1, 1228)
    IfFlagOn(-1, 1229)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=2412302)
    IfConditionTrue(0, input_condition=1)
    RunEvent(9350, slot=0, args=(3,))
    EnableFlag(72400956)


@NeverRestart
def Event12410835():
    """ 12410835: Event 12410835 """
    EndIfThisEventOn()
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterBackreadEnabled(1, 2410770)
    IfFlagOn(1, 1228)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(2410770)
    EnableBackread(2410771)
    EnableObject(2411280)
    DisableObject(2411281)
    DisableAI(2410771)
    ForceAnimation(2410770, 103082)
    ForceAnimation(2410771, 7010, loop=True)
    Move(2410770, destination=2412281, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()


@NeverRestart
def Event12410850(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410850: Event 12410850 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    DisableFlag(ARG_0_3)
    IfFlagOff(1, ARG_0_3)
    IfActionButtonInRegion(1, action_button_id=ARG_4_7, region=ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    Move(PLAYER, destination=ARG_8_11, destination_type=CoordEntityType.Object, model_point=210, short_move=True)
    ForceAnimation(PLAYER, 101320)
    WaitFrames(25)
    WaitFrames(20)
    EnableFlag(ARG_0_3)
    IfFlagOff(0, ARG_0_3)
    Restart()


@NeverRestart
def Event12410860(ARG_0_3: int, ARG_4_7: int):
    """ 12410860: Event 12410860 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, ARG_4_7)
    Restart()


@NeverRestart
def Event12410870(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410870: Event 12410870 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfCharacterHasSpecialEffect(1, ARG_0_3, ARG_8_11)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, ARG_4_7)
    WaitFrames(5)
    Restart()


@NeverRestart
def Event12410880(ARG_0_3: int, ARG_4_7: int):
    """ 12410880: Event 12410880 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfHealthEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, ARG_4_7)


@RestartOnRest
def Event12415130(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12415130: Event 12415130 """
    EndIfThisEventSlotOn()
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, skip_transition=True)
    SetAIParamID(ARG_0_3, ARG_16_19)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    SkipLinesIfEqual(1, left=0, right=ARG_24_27)
    IfFlagOn(-1, ARG_12_15)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomFrames(min_frames=0, max_frames=60)
    ForceAnimation(ARG_0_3, ARG_8_11, wait_for_completion=True)
    SetAIParamID(ARG_0_3, ARG_20_23)


@RestartOnRest
def Event12415150(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: float, ARG_16_19: int, ARG_20_23: int):
    """ 12415150: Event 12415150 """
    GotoIfThisEventSlotOn(Label.L0)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, skip_transition=True)
    SetAIParamID(ARG_0_3, ARG_16_19)
    DisableGravity(ARG_0_3)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, ARG_0_3, 10000, radius=ARG_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(ARG_0_3, ARG_8_11)
    Label(0)
    SetAIParamID(ARG_0_3, ARG_20_23)
    EnableGravity(ARG_0_3)


@RestartOnRest
def Event12410155(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410155: Event 12410155 """
    DisableAI(ARG_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_8_11)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_12_15)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event12410156(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410156: Event 12410156 """
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(1, input_condition=-1)
    IfHasAIStatus(-2, ARG_4_7, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-2, ARG_4_7, ai_status=AIStatusType.Search)
    IfHasAIStatus(-2, ARG_4_7, ai_status=AIStatusType.Battle)
    IfConditionTrue(2, input_condition=-2)
    IfHasAIStatus(-3, ARG_8_11, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-3, ARG_8_11, ai_status=AIStatusType.Search)
    IfHasAIStatus(-3, ARG_8_11, ai_status=AIStatusType.Battle)
    IfConditionTrue(3, input_condition=-3)
    IfConditionTrue(-15, input_condition=1)
    IfConditionTrue(-15, input_condition=2)
    IfConditionTrue(-15, input_condition=3)
    IfConditionTrue(0, input_condition=-15)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=2)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    Label(0)
    End()
    Label(1)
    SetNest(ARG_0_3, 2412225)
    AICommand(ARG_0_3, command_id=10, slot=0)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(-4, ARG_0_3, region=2412225)
    IfHasAIStatus(-4, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-4)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    End()
    Label(2)
    SetNest(ARG_0_3, 2412226)
    AICommand(ARG_0_3, command_id=10, slot=0)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(-5, ARG_0_3, region=2412226)
    IfHasAIStatus(-5, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-5)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    End()


@NeverRestart
def Event12410321(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12410321: Event 12410321 """
    EndIfFlagOn(ARG_0_3)
    GotoIfFlagOn(Label.L0, ARG_12_15)
    DisableFlag(ARG_4_7)
    DisableFlag(ARG_8_11)
    EndOfAnimation(ARG_16_19, 2)
    DisableObjectActivation(ARG_20_23, obj_act_id=100)
    DisableObjectActivation(ARG_24_27, obj_act_id=100)
    End()
    Label(0)
    IfFlagOn(1, ARG_4_7)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(ARG_8_11)
    EndOfAnimation(ARG_16_19, 2)
    EnableObjectActivation(ARG_20_23, obj_act_id=100)
    DisableObjectActivation(ARG_24_27, obj_act_id=100)
    End()
    Label(1)
    EnableFlag(ARG_8_11)
    EndOfAnimation(ARG_16_19, 0)
    DisableObjectActivation(ARG_20_23, obj_act_id=100)
    EnableObjectActivation(ARG_24_27, obj_act_id=100)


@NeverRestart
def Event12410325(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410325: Event 12410325 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, ARG_12_15)
    IfFlagOn(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    IfFlagOn(2, ARG_4_7)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(ARG_8_11)
    SkipLines(1)
    EnableFlag(ARG_8_11)
    IfCharacterHuman(3, PLAYER)
    IfFlagOn(3, ARG_12_15)
    IfFlagOff(3, ARG_0_3)
    IfConditionTrue(0, input_condition=3)
    Restart()


@NeverRestart
def Event12410322(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12410322: Event 12410322 """
    IfFlagOn(3, ARG_0_3)
    IfFlagOn(3, ARG_4_7)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    EndOfAnimation(2411320, 3)
    Goto(Label.L1)
    Label(0)
    IfFlagOn(1, ARG_12_15)
    IfFlagOff(1, ARG_0_3)
    IfFlagOff(1, ARG_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_16_19)
    IfObjectActivated(-1, obj_act_id=ARG_20_23)
    IfFlagChange(2, ARG_8_11)
    IfFlagOn(2, ARG_8_11)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(ARG_0_3)
    EnableFlag(ARG_4_7)
    ForceAnimation(2411320, 6, wait_for_completion=True)
    ForceAnimation(2411320, 3, wait_for_completion=True)
    Label(1)
    IfAllPlayersOutsideRegion(0, region=2412321)
    ForceAnimation(2411320, 7, wait_for_completion=True)
    DisableObjectActivation(2411317, obj_act_id=100)
    EnableObjectActivation(2411318, obj_act_id=100)
    DisableFlag(ARG_0_3)
    Restart()


@NeverRestart
def Event12410323(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12410323: Event 12410323 """
    IfFlagOn(3, ARG_0_3)
    IfFlagOff(3, ARG_4_7)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    EndOfAnimation(2411320, 1)
    Goto(Label.L1)
    Label(0)
    IfFlagOn(1, ARG_12_15)
    IfFlagOff(1, ARG_0_3)
    IfFlagOn(1, ARG_4_7)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_16_19)
    IfObjectActivated(-1, obj_act_id=ARG_20_23)
    IfFlagChange(2, ARG_8_11)
    IfFlagOff(2, ARG_8_11)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(ARG_0_3)
    DisableFlag(ARG_4_7)
    ForceAnimation(2411320, 4, wait_for_completion=True)
    ForceAnimation(2411320, 1, wait_for_completion=True)
    Label(1)
    IfAllPlayersOutsideRegion(0, region=2412322)
    ForceAnimation(2411320, 5, wait_for_completion=True)
    EnableObjectActivation(2411317, obj_act_id=100)
    DisableObjectActivation(2411318, obj_act_id=100)
    DisableFlag(ARG_0_3)
    Restart()


@NeverRestart
def Event12410324(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12410324: Event 12410324 """
    DisableNetworkSync()
    IfFlagOff(1, ARG_8_11)
    IfActionButtonInRegion(1, action_button_id=7100, region=ARG_12_15)
    IfFlagOff(2, ARG_8_11)
    IfActionButtonInRegion(2, action_button_id=7100, region=ARG_16_19)
    IfFlagOn(3, ARG_0_3)
    IfActionButtonInRegion(3, action_button_id=7100, region=ARG_12_15)
    IfFlagOn(4, ARG_0_3)
    IfActionButtonInRegion(4, action_button_id=7100, region=ARG_16_19)
    IfFlagOn(5, ARG_4_7)
    IfActionButtonInRegion(5, action_button_id=7100, region=ARG_12_15)
    IfFlagOff(6, ARG_4_7)
    IfActionButtonInRegion(6, action_button_id=7100, region=ARG_16_19)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(-1, input_condition=4)
    IfConditionTrue(-1, input_condition=5)
    IfConditionTrue(-1, input_condition=6)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event12410330(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410330: Event 12410330 """
    EndIfFlagOn(ARG_0_3)
    IfCharacterInsideRegion(0, PLAYER, region=ARG_4_7)
    EnableObjectActivation(ARG_8_11, obj_act_id=100)
    DisableObjectActivation(ARG_12_15, obj_act_id=100)
    Label(0)
    EnableFlag(ARG_0_3)


@NeverRestart
def Event12410460(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12410460: Event 12410460 """
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, skip_transition=True)
    SetAIParamID(ARG_0_3, ARG_12_15)
    DisableGravity(ARG_0_3)
    IfHasAIStatus(1, ARG_20_23, ai_status=AIStatusType.Battle)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableGravity(ARG_0_3)
    SkipLinesIfFinishedConditionTrue(2, 2)
    WaitRandomFrames(min_frames=20, max_frames=100)
    ForceAnimation(ARG_0_3, ARG_8_11, wait_for_completion=True)
    SetAIParamID(ARG_0_3, ARG_16_19)


@RestartOnRest
def Event12414450(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12414450: Event 12414450 """
    EndIfThisEventSlotOn()
    EndIfClient()
    SetEventPoint(ARG_0_3, region=ARG_4_7, reaction_range=1.0)
    IfFlagOn(1, ARG_8_11)
    IfFlagOff(1, ARG_12_15)
    IfFlagOn(1, ARG_16_19)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_0_3, command_id=990, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12414470():
    """ 12414470: Event 12414470 """
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(1, 12414420)
    IfFlagOff(1, 12414430)
    IfCharacterInsideRegion(-1, 2410158, region=2412705)
    IfCharacterInsideRegion(-1, 2410158, region=2412706)
    IfCharacterInsideRegion(-1, 2410158, region=2412707)
    IfCharacterInsideRegion(-1, 2410158, region=2412708)
    IfCharacterInsideRegion(-1, 2410158, region=2412709)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    AICommand(2410158, command_id=992, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414480():
    """ 12414480: Event 12414480 """
    GotoIfThisEventOn(Label.L0)
    IfHasTAEEvent(0, 2410158, tae_event_id=1000)
    Label(0)
    DisableAI(2410158)
    SendNPCSummonHome(2410158)


@RestartOnRest
def Event12414490():
    """ 12414490: Event 12414490 """
    DisableNetworkSync()
    IfHost(1)
    IfFlagOn(1, 12414421)
    IfFlagOff(1, 12414431)
    IfFlagOn(1, 12414700)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect_WithUnknownEffect(2410740, 35, affect_npc_parts_hp=False)
    WaitFrames(1)
    Restart()


@RestartOnRest
def Event12414400(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12414400: Event 12414400 """
    GotoIfFlagOn(Label.L0, ARG_0_3)
    DisableFlag(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, ARG_8_11)
    IfFlagOff(1, ARG_12_15)
    IfFlagOff(1, ARG_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOff(1, 12411802)
    IfFlagOff(-1, ARG_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    EnableFlag(ARG_0_3)
    CreateFX(ARG_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, ARG_8_11)
    IfFlagOff(2, ARG_12_15)
    IfFlagOff(2, ARG_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOff(2, 12411802)
    IfFlagOff(-3, ARG_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12414401(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 12414401: Event 12414401 """
    GotoIfFlagOn(Label.L0, ARG_0_3)
    DisableFlag(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)
    IfPlayerHasGood(1, 4312, including_box=False)
    IfFlagOff(1, ARG_8_11)
    IfFlagOff(1, ARG_12_15)
    IfFlagOff(1, ARG_16_19)
    IfClientTypeCountComparison(1, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOn(1, 72400461)
    IfFlagRangeAnyOn(1, (1340, 1341))
    IfFlagOff(-1, ARG_20_23)
    IfConditionTrue(1, input_condition=-1)
    IfHost(1)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    EnableFlag(ARG_0_3)
    CreateFX(ARG_4_7)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, ARG_8_11)
    IfFlagOff(2, ARG_12_15)
    IfFlagOff(2, ARG_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.LessThan, value=2)
    IfFlagOn(2, 72400461)
    IfFlagRangeAnyOn(2, (1340, 1341))
    IfFlagOff(-3, ARG_20_23)
    IfConditionTrue(2, input_condition=-3)
    IfHost(3)
    IfConditionFalse(3, input_condition=2)
    IfConditionTrue(0, input_condition=3)
    DisableFlag(ARG_0_3)
    DeleteFX(ARG_4_7, erase_root_only=True)
    Restart()


@RestartOnRest
def Event12414410(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 12414410: Event 12414410 """
    SkipLinesIfFlagOn(1, ARG_12_15)
    DisableCharacter(ARG_4_7)
    SkipLinesIfFlagOn(3, ARG_16_19)
    IfClient(1)
    IfFlagOn(1, ARG_12_15)
    SkipLinesIfConditionTrue(1, 1)
    DisableCharacter(ARG_4_7)
    EndIfFlagOn(ARG_24_27)
    IfClient(3)
    SkipLinesIfConditionTrue(1, 3)
    SetNetworkUpdateAuthority(ARG_4_7, UpdateAuthority.Forced)
    IfPlayerHasGood(2, 4312, including_box=False)
    IfFlagOff(2, ARG_12_15)
    IfFlagOff(2, ARG_16_19)
    IfFlagOn(2, ARG_20_23)
    IfFlagOff(2, ARG_24_27)
    IfActionButtonInRegion(2, action_button_id=ARG_28_31, region=ARG_4_7)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(PLAYER, 100111)
    AddSpecialEffect(PLAYER, 4682, affect_npc_part_hp=False)
    SummonNPC(ARG_0_3, ARG_4_7, ARG_8_11, summon_flag=ARG_12_15, dismissal_flag=ARG_16_19)
    CancelSpecialEffect(PLAYER, 9005)
    CancelSpecialEffect(PLAYER, 9025)
    Wait(5.0)
    DisplayBattlefieldMessage(100051, display_location_index=0)


@RestartOnRest
def Event12414460(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int):
    """ 12414460: Event 12414460 """
    EndIfClient()
    IfFlagOn(1, ARG_20_23)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(ARG_0_3, disable_interpolation=False)
    RotateToFaceEntity(ARG_0_3, ARG_8_11, animation=ARG_16_19, wait_for_completion=True)
    IfCharacterInsideRegion(2, ARG_0_3, region=ARG_12_15)
    RestartIfConditionFalse(2)
    SetEventPoint(ARG_0_3, region=ARG_8_11, reaction_range=1.0)
    AICommand(ARG_0_3, command_id=990, slot=0)
    ReplanAI(ARG_0_3)
    DisableGravity(ARG_0_3)
    DisableCollision(ARG_0_3)
    IfCharacterInsideRegion(0, ARG_0_3, region=ARG_24_27)
    EnableGravity(ARG_0_3)
    EnableCollision(ARG_0_3)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12414500():
    """ 12414500: Event 12414500 """
    GotoIfThisEventOff(Label.L0)
    SetBackreadStateAlternate(2410740, state=True)
    AddSpecialEffect(2410740, 9006, affect_npc_part_hp=False)
    EnableCharacter(2410740)
    End()
    Label(0)
    DisableCharacter(2410740)
    DisableAI(2410740)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    SetNetworkUpdateAuthority(2410740, UpdateAuthority.Forced)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12414608)
    IfCharacterInsideRegion(2, PLAYER, region=2412722)
    IfCharacterInsideRegion(3, PLAYER, region=2412723)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 12411700)
    IfFlagOn(1, 72400461)
    IfFlagRangeAnyOn(1, (1340, 1341))
    IfConditionTrue(0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    Move(2410740, destination=2412720, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=0)
    Goto(Label.L2)
    Label(1)
    Move(2410740, destination=2412721, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414021)
    Label(2)
    Wait(5.0)
    EnableFlag(12414506)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.f_MenuEffect, sound_id=100000009)
    Wait(5.0)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.f_MenuEffect, sound_id=100000020)
    SetBackreadStateAlternate(2410740, state=True)
    AddSpecialEffect(2410740, 9006, affect_npc_part_hp=False)
    EnableCharacter(2410740)
    ForceAnimation(2410740, 101201, wait_for_completion=True)
    EnableAI(2410740)
    DisableHitbox(2414200)


@RestartOnRest
def Event12414501():
    """ 12414501: Event 12414501 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(12411700)
    EndIfThisEventOn()
    IfFlagOn(0, 12414502)
    Label(0)
    DisableCharacter(2410740)
    SetBackreadStateAlternate(2410740, state=False)


@RestartOnRest
def Event12414502():
    """ 12414502: Event 12414502 """
    EndIfFlagOn(12411700)
    EndIfFlagOn(12414501)
    EndIfThisEventOn()
    IfFlagOn(1, 12414500)
    IfFlagOff(1, 12414501)
    IfFlagOn(1, 12411700)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    AICommand(2410740, command_id=991, slot=0)
    ReplanAI(2410740)
    Wait(1.0)
    AddSpecialEffect(2410740, 5560, affect_npc_part_hp=False)
    CreateTemporaryFX(121, anchor_entity=2410740, anchor_type=CoordEntityType.Character, model_point=236)
    Wait(2.0)
    DisableCharacter(2410740)


@RestartOnRest
def Event12414503():
    """ 12414503: Event 12414503 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagOn(12411700)
    EndIfFlagOn(12414501)
    EndIfFlagOn(12414505)
    EndIfThisEventOn()
    IfFlagOff(1, 12411700)
    IfFlagOn(1, 12414500)
    IfFlagOff(1, 12414501)
    IfFlagOn(1, 12411702)
    IfFlagOn(1, 12414700)
    IfCharacterOutsideRegion(1, 2410740, region=2412801)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    SetEventPoint(2410740, region=2412710, reaction_range=1.0)
    AICommand(2410740, command_id=990, slot=0)
    ReplanAI(2410740)


@RestartOnRest
def Event12414504():
    """ 12414504: Event 12414504 """
    EndIfFlagOn(12411700)
    EndIfFlagOn(12414501)
    EndIfThisEventOn()
    IfFlagOn(1, 12414503)
    IfCharacterInsideRegion(1, 2410740, region=2412710)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(2410740, disable_interpolation=False)
    RotateToFaceEntity(2410740, 2412800, animation=101130, wait_for_completion=True)
    AICommand(2410740, command_id=-1, slot=0)
    ReplanAI(2410740)


@RestartOnRest
def Event12414505():
    """ 12414505: Event 12414505 """
    DisableDeveloperMessage(2413221)
    DisableDeveloperMessage(2413223)
    DeleteFX(2413231, erase_root_only=False)
    DeleteFX(2413233, erase_root_only=False)
    EndIfThisEventOn()
    IfPlayerHasGood(1, 200, including_box=False)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 12411700)
    IfFlagOn(1, 72400461)
    IfFlagRangeAnyOn(1, (1340, 1341))
    IfConditionTrue(0, input_condition=1)
    EnableDeveloperMessage(2413221)
    EnableDeveloperMessage(2413223)
    CreateFX(2413231)
    CreateFX(2413233)
    IfFlagOn(-1, 12414506)
    IfFlagOn(-1, 12411700)
    IfConditionTrue(0, input_condition=-1)
    DisableDeveloperMessage(2413221)
    DisableDeveloperMessage(2413223)
    DeleteFX(2413231, erase_root_only=True)
    DeleteFX(2413233, erase_root_only=True)


@RestartOnRest
def Event12414600():
    """ 12414600: Event 12414600 """
    GotoIfThisEventOff(Label.L0)
    SetBackreadStateAlternate(2410158, state=True)
    AddSpecialEffect(2410158, 9006, affect_npc_part_hp=False)
    EnableCharacter(2410158)
    End()
    Label(0)
    DisableCharacter(2410158)
    DisableAI(2410158)
    IfCharacterHuman(15, PLAYER)
    SkipLinesIfConditionFalse(1, 15)
    SetNetworkUpdateAuthority(2410158, UpdateAuthority.Forced)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12414608)
    IfCharacterInsideRegion(2, PLAYER, region=2412700)
    IfCharacterInsideRegion(3, PLAYER, region=2412701)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfFlagOff(1, 12411700)
    IfFlagOff(1, 12411802)
    IfConditionTrue(0, input_condition=1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=3)
    Move(2410158, destination=2412702, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414020)
    Goto(Label.L2)
    Label(1)
    Move(2410158, destination=2412703, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=2414021)
    Label(2)
    Wait(5.0)
    EnableFlag(12414609)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.f_MenuEffect, sound_id=100000009)
    Wait(5.0)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.f_MenuEffect, sound_id=100000020)
    SetBackreadStateAlternate(2410158, state=True)
    AddSpecialEffect(2410158, 9006, affect_npc_part_hp=False)
    EnableCharacter(2410158)
    ForceAnimation(2410158, 7010, wait_for_completion=True)
    EnableAI(2410158)
    DisableHitbox(2414200)


@RestartOnRest
def Event12414601():
    """ 12414601: Event 12414601 """
    GotoIfThisEventOn(Label.L0)
    IfHasTAEEvent(0, 2410158, tae_event_id=1000)
    Label(0)
    DisableCharacter(2410158)
    SetBackreadStateAlternate(2410158, state=False)
    EnableHitbox(2414200)


@RestartOnRest
def Event12414602():
    """ 12414602: Event 12414602 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(1, 12414600)
    IfFlagOff(1, 12414601)
    IfFlagOff(1, 12411700)
    IfFlagOff(1, 12411802)
    IfCharacterDead(1, 2410800)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    AICommand(2410158, command_id=991, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414603():
    """ 12414603: Event 12414603 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(1, 12414600)
    IfFlagOff(1, 12414601)
    IfCharacterInsideRegion(-1, 2410158, region=2412705)
    IfCharacterInsideRegion(-1, 2410158, region=2412706)
    IfCharacterInsideRegion(-1, 2410158, region=2412707)
    IfCharacterInsideRegion(-1, 2410158, region=2412708)
    IfCharacterInsideRegion(-1, 2410158, region=2412709)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Label(0)
    AICommand(2410158, command_id=992, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414604():
    """ 12414604: Event 12414604 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfThisEventOn()
    IfFlagOn(1, 12411702)
    IfFlagOn(1, 12414700)
    IfCharacterOutsideRegion(1, 2410158, region=2412801)
    IfConditionTrue(0, input_condition=1)
    SetEventPoint(2410158, region=2412710, reaction_range=1.0)
    AICommand(2410158, command_id=990, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414605():
    """ 12414605: Event 12414605 """
    EndIfThisEventOn()
    IfFlagOn(1, 12414604)
    IfCharacterInsideRegion(1, 2410158, region=2412710)
    IfConditionTrue(0, input_condition=1)
    ResetAnimation(2410158, disable_interpolation=False)
    RotateToFaceEntity(2410158, 2412800, animation=7014, wait_for_completion=True)
    AICommand(2410158, command_id=-1, slot=0)
    ReplanAI(2410158)


@RestartOnRest
def Event12414606():
    """ 12414606: Event 12414606 """
    DisableDeveloperMessage(2413220)
    DisableDeveloperMessage(2413222)
    DeleteFX(2413230, erase_root_only=False)
    DeleteFX(2413232, erase_root_only=False)
    EndIfThisEventOn()
    IfPlayerHasGood(1, 200, including_box=False)
    IfCharacterHuman(1, PLAYER)
    IfFlagOff(1, 12411700)
    IfFlagOff(1, 12411802)
    IfConditionTrue(0, input_condition=1)
    EnableDeveloperMessage(2413220)
    EnableDeveloperMessage(2413222)
    CreateFX(2413230)
    CreateFX(2413232)
    IfFlagOn(-1, 12414609)
    IfFlagOn(-1, 12411700)
    IfFlagOn(-1, 12411802)
    IfConditionTrue(0, input_condition=-1)
    DisableDeveloperMessage(2413220)
    DisableDeveloperMessage(2413222)
    DeleteFX(2413230, erase_root_only=True)
    DeleteFX(2413232, erase_root_only=True)


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
    EndIfThisEventOn()
    IfFlagOn(1, 12414600)
    IfFlagOff(1, 12414601)
    IfHealthGreaterThan(1, 2410158, 0.0)
    IfCharacterHasSpecialEffect(1, 2410158, 4640)
    IfConditionTrue(0, input_condition=1)
    Wait(2.0)
    IfFlagOn(2, 12414600)
    IfFlagOff(2, 12414601)
    IfHealthGreaterThan(2, 2410158, 0.0)
    EndIfConditionFalse(2)
    PlaySoundEffect(anchor_entity=2410158, sound_type=SoundType.v_Voice, sound_id=242100402)


@NeverRestart
def Event12410220(ARG_0_3: int, ARG_4_7: float):
    """ 12410220: Event 12410220 """
    DisableAI(ARG_0_3)
    IfEntityWithinDistance(-1, ARG_0_3, 10000, radius=ARG_4_7)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(ARG_0_3)


@NeverRestart
def Event12410234():
    """ 12410234: Event 12410234 """
    IfCharacterDead(0, 2410158)
    End()


@NeverRestart
def Event12410237(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 12410237: Event 12410237 """
    DisableCharacter(ARG_12_15)
    IfFlagOn(0, ARG_0_3)
    IfHealthLessThanOrEqual(-1, ARG_4_7, 0.5)
    IfTimeElapsed(-1, 40.0)
    IfFlagOn(1, 12410235)
    IfCharacterAlive(1, ARG_8_11)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EndIfFlagOn(12411800)
    DisableCharacter(ARG_8_11)
    EnableCharacter(ARG_12_15)
    Wait(1.0)
    SetNest(ARG_12_15, ARG_16_19)
    AICommand(ARG_12_15, command_id=10, slot=0)
    ReplanAI(ARG_12_15)
    DisableGravity(ARG_12_15)
    DisableCollision(ARG_12_15)
    DisableAnimations(ARG_12_15)
    IfEntityWithinDistance(-2, ARG_12_15, 2410810, radius=3.0)
    IfCharacterInsideRegion(-2, ARG_12_15, region=2412811)
    IfConditionTrue(0, input_condition=-2)
    AICommand(ARG_12_15, command_id=-1, slot=0)
    ClearTargetList(ARG_12_15)
    ReplanAI(ARG_12_15)
    EnableCollision(ARG_12_15)
    EnableAnimations(ARG_12_15)
    EnableGravity(ARG_12_15)


@NeverRestart
def Event12410238():
    """ 12410238: Event 12410238 """
    IfFlagOn(-1, 12410234)
    IfFlagOn(-1, 12411802)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(10)
    DisableCharacter(2410158)


@NeverRestart
def Event12410239(ARG_0_3: int):
    """ 12410239: Event 12410239 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(5)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-2)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=2)
    WaitFrames(5)
    IfCharacterHuman(-3, PLAYER)
    IfCharacterType(-3, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(3, input_condition=-3)
    IfDamageType(3, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=3)
    WaitFrames(5)
    IfCharacterHuman(-4, PLAYER)
    IfCharacterType(-4, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(4, input_condition=-4)
    IfDamageType(4, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=4)
    WaitFrames(5)
    Label(0)
    StopEvent(12415234, slot=0)
    DisableFlag(12415234)
    CancelSpecialEffect(ARG_0_3, 5590)
    SetTeamType(ARG_0_3, TeamType.Indiscriminate)


@NeverRestart
def Event12410240(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: float):
    """ 12410240: Event 12410240 """
    WaitRandomSeconds(min_seconds=ARG_8_11, max_seconds=ARG_12_15)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Normal)
    ForceAnimation(ARG_0_3, ARG_4_7, wait_for_completion=True)
    Restart()


@NeverRestart
def Event12410285(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410285: Event 12410285 """
    SkipLinesIfThisEventSlotOff(7)
    EndOfAnimation(ARG_8_11, 2)
    Wait(1.0)
    RegisterLadder(start_climbing_flag=ARG_0_3, stop_climbing_flag=ARG_4_7, obj=ARG_8_11)
    DisableObjectActivation(ARG_12_15, obj_act_id=2410000)
    IfActionButtonInRegion(0, action_button_id=7100, region=ARG_12_15)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()
    IfObjectActivated(0, obj_act_id=12410206)
    ForceAnimation(ARG_8_11, 1)
    WaitFrames(40)
    ForceAnimation(ARG_8_11, 2)
    RegisterLadder(start_climbing_flag=ARG_0_3, stop_climbing_flag=ARG_4_7, obj=ARG_8_11)
    Restart()


@NeverRestart
def Event12410287(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410287: Event 12410287 """
    SkipLinesIfThisEventSlotOff(2)
    CreateObjectFX(8028, obj=ARG_0_3, model_point=100)
    End()
    CreateObjectFX(8029, obj=ARG_0_3, model_point=100)
    IfCharacterInsideRegion(0, PLAYER, region=ARG_4_7)
    ForceAnimation(ARG_0_3, 1000000)
    WaitFrames(30)
    DeleteObjectFX(ARG_0_3, erase_root=True)
    CreateObjectFX(8028, obj=ARG_0_3, model_point=100)
    PlaySoundEffect(anchor_entity=ARG_0_3, sound_type=SoundType.a_Ambient, sound_id=600000000)
    CreatePlayLog(ARG_8_11)


@NeverRestart
def Event12410340(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410340: Event 12410340 """
    IfCharacterInsideRegion(0, PLAYER, region=ARG_12_15)
    SetNest(ARG_0_3, ARG_4_7)
    AICommand(ARG_0_3, command_id=ARG_8_11, slot=0)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(-1, ARG_0_3, region=ARG_4_7)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12410370():
    """ 12410370: Event 12410370 """
    IfCharacterDead(-10, 2410028)
    IfCharacterDead(-10, 2410030)
    GotoIfConditionTrue(Label.L0, input_condition=-10)
    IfObjectDestroyed(10, 2411221)
    GotoIfConditionTrue(Label.L0, input_condition=10)
    Goto(Label.L1)
    Label(0)
    DisableObject(2411220)
    PostDestruction(2411221, slot=1)
    End()
    Label(1)
    DisableObject(2411221)
    ForceAnimation(2411220, 0)
    IfCharacterInsideRegion(1, PLAYER, region=2412210)
    IfCharacterInsideRegion(2, PLAYER, region=2412211)
    IfFlagOn(3, 12415371)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    EnableFlag(12415371)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=3)
    IfEntityWithinDistance(-3, 2411220, 10000, radius=10.0)
    IfRandomTimeElapsed(-3, min_seconds=4.0, max_seconds=12.0)
    IfAttacked(-3, 2410028, attacking_character=10000)
    IfAttacked(-3, 2410030, attacking_character=10000)
    IfConditionTrue(0, input_condition=-3)
    Label(2)
    ForceAnimation(2410028, 3008)
    ForceAnimation(2410030, 3009)
    WaitFrames(40)
    EnableInvincibility(2410028)
    EnableInvincibility(2410030)
    CreateObjectFX(900260, obj=2411220, model_point=100)
    CreateHazard(12410376, 2411220, model_point=100, behavior_param_id=6111, target_type=DamageTargetType.Character, radius=1.600000023841858, life=9999.0, repetition_time=0.0)
    ForceAnimation(2411220, 1)
    WaitFrames(6)
    DisableInvincibility(2410028)
    DisableInvincibility(2410030)
    WaitFrames(206)
    RemoveObjectFlag(12410376)
    DeleteObjectFX(2411220, erase_root=True)
    EnableObject(2411221)
    DisableObject(2411220)
    DestroyObject(2411221, slot=1)


@RestartOnRest
def Event12415372(ARG_0_3: int):
    """ 12415372: Event 12415372 """
    IfFlagOn(0, 12415371)
    EnableFlag(12415371)
    SetNest(ARG_0_3, 2412212)
    AICommand(ARG_0_3, command_id=10, slot=0)
    ReplanAI(ARG_0_3)
    IfCharacterInsideRegion(-1, ARG_0_3, region=2412212)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event12410378(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 12410378: Event 12410378 """
    SkipLinesIfThisEventSlotOff(3)
    EndOfAnimation(ARG_8_11, 2)
    Move(ARG_0_3, destination=ARG_12_15, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    End()
    DisableAI(ARG_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=2412031)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    WaitRandomFrames(min_frames=50, max_frames=70)
    IfHealthValueLessThanOrEqual(0, ARG_0_3, 2)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, wait_for_completion=True, skip_transition=True)
    WaitFrames(76)
    IfHealthValueLessThanOrEqual(0, ARG_0_3, 2)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, wait_for_completion=True, skip_transition=True)
    WaitRandomFrames(min_frames=76, max_frames=100)
    IfHealthValueLessThanOrEqual(0, ARG_0_3, 2)
    DisableGravity(ARG_0_3)
    DisableCollision(ARG_0_3)
    EnableInvincibility(ARG_0_3)
    DisableImmortality(ARG_0_3)
    CancelSpecialEffect(ARG_0_3, 5915)
    ForceAnimation(ARG_8_11, 1)
    ForceAnimation(ARG_0_3, 3001)
    WaitFrames(16)
    EnableAI(ARG_0_3)
    EnableGravity(ARG_0_3)
    EnableCollision(ARG_0_3)
    DisableInvincibility(ARG_0_3)


@RestartOnRest
def Event12410380(ARG_0_3: int, ARG_4_7: int):
    """ 12410380: Event 12410380 """
    DisableAI(ARG_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=2412031)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    WaitRandomFrames(min_frames=55, max_frames=200)
    IfHealthValueGreaterThanOrEqual(2, ARG_0_3, 1)
    SkipLinesIfConditionTrue(2, 2)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True, wait_for_completion=True, skip_transition=True)
    Restart()
    End()


@RestartOnRest
def Event12410384(ARG_0_3: int):
    """ 12410384: Event 12410384 """
    IfDamageType(0, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    Kill(ARG_0_3, award_souls=True)


@NeverRestart
def Event12410490(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 12410490: Event 12410490 """
    SkipLinesIfFlagOff(2, 100)
    DisableFlag(100)
    DisableFlag(ARG_8_11)
    GotoIfThisEventSlotOff(Label.L0)
    PostDestruction(ARG_0_3, slot=1)
    ForceAnimation(ARG_4_7, 2)
    EnableTreasure(ARG_4_7)
    End()
    Label(0)
    CreateObjectFX(900201, obj=ARG_4_7, model_point=90)
    ForceAnimation(ARG_4_7, 0)
    IfObjectDestroyed(0, ARG_0_3)
    ForceAnimation(ARG_4_7, 1, wait_for_completion=True)
    DeleteObjectFX(ARG_4_7, erase_root=True)
    EnableTreasure(ARG_4_7)
    EnableFlag(ARG_8_11)
    IfFlagOn(0, 100)
    RestoreObject(ARG_0_3)
    ForceAnimation(ARG_4_7, 0)
    DisableTreasure(ARG_4_7)
    Restart()


@NeverRestart
def Event12410990():
    """ 12410990: Event 12410990 """
    EndIfThisEventOn()
    IfStandingOnHitbox(0, 2413500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 148, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 148, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 148, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 148, PlayLogMultiplayerType.HostOnly)


@NeverRestart
def Event12410995():
    """ 12410995: Event 12410995 """
    EndIfThisEventOn()
    EndIfClient()
    IfStandingOnHitbox(1, 2414110)
    IfCharacterOutsideRegion(1, PLAYER, region=2412900)
    IfConditionTrue(0, input_condition=1)
    RunEvent(9350, slot=0, args=(1,))


@RestartOnRest
def Event12415010(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: float):
    """ 12415010: Event 12415010 """
    DisableNetworkSync()
    Wait(ARG_12_15)
    PlaySoundEffect(anchor_entity=ARG_0_3, sound_type=ARG_4_7, sound_id=ARG_8_11)
    WaitFrames(440)
    IfFlagOff(1, 9801)
    IfFlagOff(1, 9802)
    SkipLinesIfConditionTrue(1, 1)
    PlaySoundEffect(anchor_entity=ARG_0_3, sound_type=ARG_4_7, sound_id=ARG_8_11)
    Restart()
