"""
Castle Cainhurst

linked:
304

strings:
0: クリア時間_通し
18: クリア時間_1プレイ
40: ボス_撃破
52: PC情報_ボス撃破_王の死神
82: ボス_戦闘開始
98: ボス戦_撃破時間
116: 古城_ボス戦_大魔法持続時間
146: 古城_アイテム取得順_アイテムA
180: 古城_アイテム取得順_アイテムB
214: 古城_アイテム取得順_アイテムC
248: 古城_アイテム取得順_アイテムD
282: PC情報_古城到達時
304: N:\\SPRJ\\data\\Param\\event\\common.emevd
380: 
382: 
"""
from soulstruct.bloodborne.events import *
from soulstruct.bloodborne.events.instructions import *


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RunEvent(7000, slot=25, args=(2500950, 2501950, 999, 12507800))
    RunEvent(7000, slot=26, args=(2500951, 2501951, 999, 12507820))
    RunEvent(7000, slot=27, args=(2500952, 2501952, 12501800, 12507840))
    RunEvent(7100, slot=25, args=(72500200, 2501950))
    RunEvent(7100, slot=26, args=(72500201, 2501951))
    RunEvent(7100, slot=27, args=(72500202, 2501952))
    RunEvent(7200, slot=25, args=(72500100, 2501950, 2102952))
    RunEvent(7200, slot=26, args=(72500101, 2501951, 2102952))
    RunEvent(7200, slot=27, args=(72500102, 2501952, 2102952))
    RunEvent(7300, slot=25, args=(72102500, 2501950))
    RunEvent(7300, slot=26, args=(72102501, 2501951))
    RunEvent(7300, slot=27, args=(72102502, 2501952))
    RunEvent(9200, slot=5, args=(2503900,))
    RunEvent(9220, slot=5, args=(2500710, 12504220, 12504221, 2500, 25))
    RunEvent(9240, slot=5, args=(2500710, 12504220, 12504221, 12504222, 25))
    RunEvent(9260, slot=5, args=(2500710, 12504220, 12504221, 12504222, 25))
    RunEvent(9280, slot=5, args=(2500710, 12504220, 12504221, 2500, 12504223, 25))
    StartPlayLogMeasurement(measurement_id=2500000, name=0, overwrite=False)
    StartPlayLogMeasurement(measurement_id=2500001, name=18, overwrite=True)
    Event_12500090()
    Event_101()
    Event_12500001()
    Event_12500011()
    Event_12500012()
    Event_12500013()
    Event_12500014()
    Event_12500015()
    Event_12500016()
    Event_12500018()
    Event_12500019()
    Event_12500020()
    Event_12500021()
    Event_12500052(0, attacked_entity=2500790, flag=72500358)
    Event_12500051()
    Event_12500053(0, character=2500790, flag=1349, flag_1=72500358)
    Event_12500054(0, character=2500790, flag=1350)
    Event_12500072(0, entity=2501011, state=0)
    Event_12500072(1, entity=2501012, state=1)
    Event_12500075()
    Event_12500076()
    Event_12500077()
    RegisterLadder(start_climbing_flag=12500992, stop_climbing_flag=12500993, obj=2501502)
    Event_12500620(0, attacked_entity=2500115, animation_id=7000, animation_id_1=7003, flag=12500898)
    Event_12500620(1, attacked_entity=2500116, animation_id=7000, animation_id_1=7003, flag=12500898)
    Event_12500620(2, attacked_entity=2500118, animation_id=7000, animation_id_1=7003, flag=12500898)
    Event_12500620(3, attacked_entity=2500119, animation_id=7010, animation_id_1=7013, flag=12500898)
    Event_12500620(4, attacked_entity=2500126, animation_id=7000, animation_id_1=7003, flag=12500898)
    Event_12500740(0, character=2500115)
    Event_12500740(1, character=2500116)
    Event_12500740(2, character=2500118)
    Event_12500740(3, character=2500119)
    Event_12500740(4, character=2500126)
    Event_12500630(0, character=2500127, animation_id=7000, animation_id_1=7001)
    Event_12500630(1, character=2500128, animation_id=7010, animation_id_1=7011)
    Event_12500630(2, character=2500129, animation_id=7000, animation_id_1=7001)
    Event_12500630(3, character=2500132, animation_id=7010, animation_id_1=7011)
    Event_12500630(4, character=2500137, animation_id=7010, animation_id_1=7011)
    Event_12500630(5, character=2500138, animation_id=7000, animation_id_1=7001)
    Event_12500454(0, 2500172, 7023, 7013, 2502020, -1, 122008, 122009, 150)
    Event_12500454(1, 2500173, 7010, 7017, 2502021, -1, 122008, 122009, 150)
    Event_12500454(2, 2500182, 7028, 7018, 2502024, -1, 122008, 122009, 150)
    Event_12500454(3, 2500183, 7029, 7019, 2502024, -1, 122008, 122009, 150)
    Event_12500458(
        0,
        character=2500160,
        animation_id=7015,
        region=2502022,
        frames=100,
        region_1=2502023,
        animation_id_1=7025,
    )
    Event_12500458(
        1,
        character=2500161,
        animation_id=7016,
        region=2502023,
        frames=100,
        region_1=2502022,
        animation_id_1=7026,
    )
    Event_12500640(0, character=2500200)
    Event_12500640(1, character=2500201)
    Event_12500640(2, character=2500202)
    Event_12500640(3, character=2500203)
    Event_12500640(4, character=2500204)
    Event_12500640(5, character=2500205)
    Event_12500640(6, character=2500207)
    Event_12500640(7, character=2500208)
    Event_12500640(8, character=2500209)
    Event_12500640(9, character=2500210)
    Event_12500640(10, character=2500211)
    Event_12500640(11, character=2500212)
    Event_12500640(12, character=2500213)
    Event_12500640(13, character=2500217)
    Event_12500640(14, character=2500218)
    Event_12500640(15, character=2500219)
    Event_12500640(16, character=2500220)
    Event_12500640(17, character=2500222)
    Event_12500640(18, character=2500223)
    Event_12500640(19, character=2500224)
    Event_12500640(20, character=2500230)
    Event_12500640(21, character=2500231)
    Event_12500640(22, character=2500232)
    Event_12500640(23, character=2500233)
    Event_12500640(24, character=2500234)
    Event_12500640(25, character=2500236)
    Event_12500640(26, character=2500237)
    Event_12500640(27, character=2500238)
    Event_12500640(28, character=2500240)
    Event_12500640(29, character=2500241)
    Event_12500640(30, character=2500243)
    Event_12500640(31, character=2500245)
    Event_12500640(32, character=2500246)
    Event_12500640(33, character=2500248)
    Event_12500640(34, character=2500249)
    Event_12500640(35, character=2500250)
    Event_12500640(36, character=2500251)
    Event_12500640(37, character=2500252)
    Event_12500640(38, character=2500254)
    Event_12500640(39, character=2500255)
    Event_12500640(40, character=2500256)
    Event_12500640(41, character=2500272)
    Event_12500640(42, character=2500273)
    Event_12500640(43, character=2500274)
    Event_12500640(44, character=2500275)
    Event_12500640(45, character=2500276)
    Event_12500078()
    Event_12500896(0, region=2502102)
    Event_12500898(0, flag=52500200, flag_1=52500210, flag_2=52500220, flag_3=52500230)
    Event_12500900(0, character=2500200, flag=12500898, flag_1=12505200)
    Event_12500900(1, character=2500201, flag=12500898, flag_1=12505201)
    Event_12500900(2, character=2500202, flag=12500898, flag_1=12505202)
    Event_12500900(3, character=2500203, flag=12500898, flag_1=12505203)
    Event_12500900(4, character=2500204, flag=12500898, flag_1=12505204)
    Event_12500900(5, character=2500205, flag=12500898, flag_1=12505205)
    Event_12500900(6, character=2500207, flag=12500898, flag_1=12505207)
    Event_12500900(7, character=2500208, flag=12500898, flag_1=12505208)
    Event_12500900(8, character=2500209, flag=12500898, flag_1=12505209)
    Event_12500900(9, character=2500210, flag=12500898, flag_1=12505210)
    Event_12500900(10, character=2500211, flag=12500898, flag_1=12505211)
    Event_12500900(11, character=2500212, flag=12500898, flag_1=12505212)
    Event_12500900(12, character=2500213, flag=12500898, flag_1=12505213)
    Event_12500900(13, character=2500217, flag=12500896, flag_1=12505217)
    Event_12500900(14, character=2500218, flag=12500896, flag_1=12505218)
    Event_12500900(15, character=2500219, flag=12500896, flag_1=12505219)
    Event_12500900(16, character=2500220, flag=12500896, flag_1=12505220)
    Event_12500900(17, character=2500222, flag=12500896, flag_1=12505222)
    Event_12500900(18, character=2500223, flag=12500896, flag_1=12505223)
    Event_12500900(19, character=2500224, flag=12500896, flag_1=12505224)
    Event_12500900(20, character=2500230, flag=12500078, flag_1=12505230)
    Event_12500900(21, character=2500231, flag=12500078, flag_1=12505231)
    Event_12500900(22, character=2500232, flag=12500078, flag_1=12505232)
    Event_12500900(23, character=2500233, flag=12500078, flag_1=12505233)
    Event_12500900(24, character=2500234, flag=12500078, flag_1=12505234)
    Event_12500900(25, character=2500236, flag=12500078, flag_1=12505236)
    Event_12500900(26, character=2500237, flag=12500078, flag_1=12505237)
    Event_12500900(27, character=2500238, flag=12500078, flag_1=12505238)
    Event_12500900(28, character=2500240, flag=12500078, flag_1=12505240)
    Event_12500900(29, character=2500241, flag=12500078, flag_1=12505241)
    Event_12500900(30, character=2500243, flag=12500078, flag_1=12505243)
    Event_12500900(31, character=2500245, flag=12500078, flag_1=12505245)
    Event_12500900(32, character=2500246, flag=12500078, flag_1=12505246)
    Event_12500900(33, character=2500248, flag=12500078, flag_1=12505248)
    Event_12500900(34, character=2500249, flag=12500078, flag_1=12505249)
    Event_12500900(35, character=2500250, flag=12500078, flag_1=12505250)
    Event_12500900(36, character=2500251, flag=12500078, flag_1=12505251)
    Event_12500900(37, character=2500252, flag=12500898, flag_1=12505252)
    Event_12500900(38, character=2500254, flag=12500898, flag_1=12505254)
    Event_12500900(39, character=2500255, flag=12500898, flag_1=12505255)
    Event_12500900(40, character=2500256, flag=12500898, flag_1=12505256)
    Event_12500900(41, character=2500272, flag=12500078, flag_1=12505272)
    Event_12500900(42, character=2500273, flag=12500078, flag_1=12505273)
    Event_12500900(43, character=2500274, flag=12500078, flag_1=12505274)
    Event_12500900(44, character=2500275, flag=12500078, flag_1=12505275)
    Event_12500900(45, character=2500276, flag=12500078, flag_1=12505276)
    Event_12505000(0, character=2500200, flag=12505200)
    Event_12505000(1, character=2500201, flag=12505201)
    Event_12505000(2, character=2500202, flag=12505202)
    Event_12505000(3, character=2500203, flag=12505203)
    Event_12505000(4, character=2500204, flag=12505204)
    Event_12505000(5, character=2500205, flag=12505205)
    Event_12505000(6, character=2500207, flag=12505207)
    Event_12505000(7, character=2500208, flag=12505208)
    Event_12505000(8, character=2500209, flag=12505209)
    Event_12505000(9, character=2500210, flag=12505210)
    Event_12505000(10, character=2500211, flag=12505211)
    Event_12505000(11, character=2500212, flag=12505212)
    Event_12505000(12, character=2500213, flag=12505213)
    Event_12505000(13, character=2500217, flag=12505217)
    Event_12505000(14, character=2500218, flag=12505218)
    Event_12505000(15, character=2500219, flag=12505219)
    Event_12505000(16, character=2500220, flag=12505220)
    Event_12505000(17, character=2500222, flag=12505222)
    Event_12505000(18, character=2500223, flag=12505223)
    Event_12505000(19, character=2500224, flag=12505224)
    Event_12505000(20, character=2500230, flag=12505230)
    Event_12505000(21, character=2500231, flag=12505231)
    Event_12505000(22, character=2500232, flag=12505232)
    Event_12505000(23, character=2500233, flag=12505233)
    Event_12505000(24, character=2500234, flag=12505234)
    Event_12505000(25, character=2500236, flag=12505236)
    Event_12505000(26, character=2500237, flag=12505237)
    Event_12505000(27, character=2500238, flag=12505238)
    Event_12505000(28, character=2500240, flag=12505240)
    Event_12505000(29, character=2500241, flag=12505241)
    Event_12505000(30, character=2500243, flag=12505243)
    Event_12505000(31, character=2500245, flag=12505245)
    Event_12505000(32, character=2500246, flag=12505246)
    Event_12505000(33, character=2500248, flag=12505248)
    Event_12505000(34, character=2500249, flag=12505249)
    Event_12505000(35, character=2500250, flag=12505250)
    Event_12505000(36, character=2500251, flag=12505251)
    Event_12505000(37, character=2500252, flag=12505252)
    Event_12505000(38, character=2500254, flag=12505254)
    Event_12505000(39, character=2500255, flag=12505255)
    Event_12505000(40, character=2500256, flag=12505256)
    Event_12505000(41, character=2500272, flag=12505272)
    Event_12505000(42, character=2500273, flag=12505273)
    Event_12505000(43, character=2500274, flag=12505274)
    Event_12505000(44, character=2500275, flag=12505275)
    Event_12505000(45, character=2500276, flag=12505276)
    Event_12505300(0, flag=12505200)
    Event_12505300(1, flag=12505201)
    Event_12505300(2, flag=12505202)
    Event_12505300(3, flag=12505203)
    Event_12505300(4, flag=12505204)
    Event_12505300(5, flag=12505205)
    Event_12505300(6, flag=12505207)
    Event_12505300(7, flag=12505208)
    Event_12505300(8, flag=12505209)
    Event_12505300(9, flag=12505210)
    Event_12505300(10, flag=12505211)
    Event_12505300(11, flag=12505212)
    Event_12505300(12, flag=12505213)
    Event_12505300(13, flag=12505217)
    Event_12505300(14, flag=12505218)
    Event_12505300(15, flag=12505219)
    Event_12505300(16, flag=12505220)
    Event_12505300(17, flag=12505222)
    Event_12505300(18, flag=12505223)
    Event_12505300(19, flag=12505224)
    Event_12505300(20, flag=12505230)
    Event_12505300(21, flag=12505231)
    Event_12505300(22, flag=12505232)
    Event_12505300(23, flag=12505233)
    Event_12505300(24, flag=12505234)
    Event_12505300(25, flag=12505236)
    Event_12505300(26, flag=12505237)
    Event_12505300(27, flag=12505238)
    Event_12505300(28, flag=12505240)
    Event_12505300(29, flag=12505241)
    Event_12505300(30, flag=12505243)
    Event_12505300(31, flag=12505245)
    Event_12505300(32, flag=12505246)
    Event_12505300(33, flag=12505248)
    Event_12505300(34, flag=12505249)
    Event_12505300(35, flag=12505250)
    Event_12505300(36, flag=12505251)
    Event_12505300(37, flag=12505252)
    Event_12505300(38, flag=12505254)
    Event_12505300(39, flag=12505255)
    Event_12505300(40, flag=12505256)
    Event_12505300(41, flag=12505272)
    Event_12505300(42, flag=12505273)
    Event_12505300(43, flag=12505274)
    Event_12505300(44, flag=12505275)
    Event_12505300(45, flag=12505276)
    Event_12501000(0, character=2500200)
    Event_12501000(1, character=2500201)
    Event_12501000(2, character=2500202)
    Event_12501000(3, character=2500203)
    Event_12501000(4, character=2500204)
    Event_12501000(5, character=2500205)
    Event_12501000(6, character=2500207)
    Event_12501000(7, character=2500208)
    Event_12501000(8, character=2500209)
    Event_12501000(9, character=2500210)
    Event_12501000(10, character=2500211)
    Event_12501000(11, character=2500212)
    Event_12501000(12, character=2500213)
    Event_12501000(13, character=2500217)
    Event_12501000(14, character=2500218)
    Event_12501000(15, character=2500219)
    Event_12501000(16, character=2500220)
    Event_12501000(17, character=2500222)
    Event_12501000(18, character=2500223)
    Event_12501000(19, character=2500224)
    Event_12501000(20, character=2500230)
    Event_12501000(21, character=2500231)
    Event_12501000(22, character=2500232)
    Event_12501000(23, character=2500233)
    Event_12501000(24, character=2500234)
    Event_12501000(25, character=2500236)
    Event_12501000(26, character=2500237)
    Event_12501000(27, character=2500238)
    Event_12501000(28, character=2500240)
    Event_12501000(29, character=2500243)
    Event_12501000(32, character=2500248)
    Event_12501000(33, character=2500249)
    Event_12501000(34, character=2500250)
    Event_12501000(35, character=2500251)
    Event_12501000(36, character=2500252)
    Event_12501000(37, character=2500254)
    Event_12501000(38, character=2500255)
    Event_12501000(39, character=2500256)
    Event_12501000(40, character=2500272)
    Event_12501000(41, character=2500273)
    Event_12501000(42, character=2500274)
    Event_12501000(43, character=2500275)
    Event_12500030()
    Event_12500031(0, obj_act_id=12501200, obj=2501200)
    Event_12500031(1, obj_act_id=12501204, obj=2501204)
    Event_12500031(2, obj_act_id=12501205, obj=2501205)
    Event_12500031(3, obj_act_id=12501208, obj=2501208)
    Event_12500031(4, obj_act_id=12501209, obj=2501209)
    Event_12500031(5, obj_act_id=12501210, obj=2501210)
    Event_12500031(6, obj_act_id=12501211, obj=2501211)
    Event_12500200(0, first_flag=12500250, last_flag=12500259)
    Event_12500200(1, first_flag=12500270, last_flag=12500279)
    Event_12500206(0, attacker__character=2500114, flag=12500250, flag_1=12500270)
    Event_12500220(0, attacker__character=2500114, flag=12500270)
    Event_12500206(1, attacker__character=2500115, flag=12500251, flag_1=12500271)
    Event_12500220(1, attacker__character=2500115, flag=12500271)
    Event_12500206(2, attacker__character=2500116, flag=12500252, flag_1=12500272)
    Event_12500220(2, attacker__character=2500116, flag=12500272)
    Event_12500206(4, attacker__character=2500118, flag=12500254, flag_1=12500274)
    Event_12500220(4, attacker__character=2500118, flag=12500274)
    Event_12500206(5, attacker__character=2500122, flag=12500255, flag_1=12500275)
    Event_12500220(5, attacker__character=2500122, flag=12500275)
    Event_12500206(6, attacker__character=2500123, flag=12500256, flag_1=12500276)
    Event_12500220(6, attacker__character=2500123, flag=12500276)
    Event_12500206(7, attacker__character=2500124, flag=12500257, flag_1=12500277)
    Event_12500220(7, attacker__character=2500124, flag=12500277)
    Event_12500206(8, attacker__character=2500132, flag=12500259, flag_1=12500279)
    Event_12500220(8, attacker__character=2500132, flag=12500279)
    Event_12500520(0, character=2500211, animation_id=7000, animation_id_1=7001, radius=3.0, radius_1=3.0)
    Event_12500520(1, character=2500208, animation_id=7000, animation_id_1=7001, radius=3.0, radius_1=3.0)
    Event_12500520(2, character=2500204, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(3, character=2500200, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(4, character=2500255, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(5, character=2500207, animation_id=7000, animation_id_1=7001, radius=3.0, radius_1=3.0)
    Event_12500520(6, character=2500217, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(7, character=2500220, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(8, character=2500224, animation_id=7000, animation_id_1=7001, radius=3.0, radius_1=3.0)
    Event_12500520(9, character=2500230, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(10, character=2500231, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(11, character=2500238, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(12, character=2500236, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(13, character=2500272, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(14, character=2500275, animation_id=7000, animation_id_1=7001, radius=3.0, radius_1=3.0)
    Event_12500520(15, character=2500274, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(16, character=2500250, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(17, character=2500249, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(18, character=2500243, animation_id=7000, animation_id_1=7001, radius=3.0, radius_1=3.0)
    Event_12500520(19, character=2500251, animation_id=7000, animation_id_1=7001, radius=3.0, radius_1=3.0)
    Event_12500520(20, character=2500245, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=15.0)
    Event_12500520(21, character=2500104, animation_id=7001, animation_id_1=7007, radius=10.0, radius_1=10.0)
    Event_12500520(22, character=2500105, animation_id=7001, animation_id_1=7007, radius=10.0, radius_1=10.0)
    Event_12500520(23, character=2500106, animation_id=7002, animation_id_1=0, radius=5.0, radius_1=5.0)
    Event_12500100(0, character=2500280, radius=8.0)
    Event_12500100(1, character=2500281, radius=16.0)
    Event_12500100(2, character=2500282, radius=9.0)
    Event_12500100(3, character=2500284, radius=8.0)
    Event_12500100(4, character=2500285, radius=7.0)
    Event_12500100(5, character=2500292, radius=8.0)
    Event_12500100(6, character=2500293, radius=7.0)
    Event_12500100(7, character=2500294, radius=9.0)
    Event_12500070(0, obj=2501020, region=2502030)
    Event_12500070(1, obj=2501207, region=2502031)
    Event_12505100(0, character=2500101, animation_id=7020, region=2502050, patrol_information_id=2502030)
    Event_12505100(1, character=2500102, animation_id=7021, region=2502051, patrol_information_id=2502031)
    Event_12505100(2, character=2500103, animation_id=7022, region=2502052, patrol_information_id=2502032)
    Event_12500285(0, character=2500352, radius=18.0, character_1=2500308)
    Event_12500285(1, character=2500308, radius=50.0, character_1=0)
    Event_12500285(2, character=2500353, radius=22.0, character_1=2500352)
    Event_12500285(3, character=2500354, radius=18.0, character_1=2500353)
    Event_12500235(0, character=2500210, flag=12500898)
    Event_12500390(0, character=2500180)
    Event_12500435(0, attacked_entity=2500133, region=2502150)
    Event_12500440(0, character=2500134, character_1=2500135)
    Event_12500501()
    Event_12500502(0, character=2500136, flag=52500190, region=2502409)
    Event_12500400(0, character=2500400, flag=52500990)
    Event_12500400(1, character=2500401, flag=52500980)
    Event_12500400(2, character=2500402, flag=52500970)
    Event_12500400(3, character=2500403, flag=52500960)
    Event_12500400(4, character=2500404, flag=52500950)
    Event_12504812()
    Event_12504813()
    Event_12501800()
    Event_12501801()
    Event_12501802()
    Event_12504810()
    Event_12504811()
    Event_12504802()
    Event_12504803()
    Event_12504804()
    Event_12504805()
    Event_12504806()
    Event_12504806()
    Event_12504807()
    Event_12504808()
    Event_12501804()
    Event_12500810()
    Event_12501803()
    Event_12500600()


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_12500010()
    Event_12500050()
    DisableSoundEvent(sound_id=2503900)
    Event_12500000()


@ContinueOnRest(12500000)
def Event_12500000():
    """Event 12500000"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    EnableFlag(9180)
    WaitFrames(frames=1)
    EnableFlag(12200134)
    PlayCutscene(25000000, cutscene_flags=CutsceneFlags.FadeOut, player_id=10000)
    WaitFrames(frames=1)
    AwardAchievement(achievement_id=10)
    DisableFlag(9180)


@ContinueOnRest(12500001)
def Event_12500001():
    """Event 12500001"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2502500))
    
    RunEvent(9350, slot=0, args=(2,))


@ContinueOnRest(12500010)
def Event_12500010():
    """Event 12500010"""
    GotoIfClient(Label.L0)
    AND_1.Add(FlagEnabled(1041))
    GotoIfConditionFalse(Label.L1, input_condition=AND_1)
    DisableFlagRange((1040, 1059))
    EnableFlag(1042)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(1042))
    AND_2.Add(FlagEnabled(72500328))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    DisableFlag(72500328)
    DisableFlagRange((1040, 1059))
    EnableFlag(1040)

    # --- Label 2 --- #
    DefineLabel(2)
    AND_3.Add(FlagEnabled(1040))
    OR_1.Add(FlagEnabled(1347))
    OR_1.Add(FlagEnabled(1348))
    OR_1.Add(FlagEnabled(1349))
    AND_3.Add(OR_1)
    GotoIfConditionFalse(Label.L3, input_condition=AND_3)
    DisableFlagRange((1040, 1059))
    EnableFlag(1042)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableFlag(72500320)
    DisableFlag(72500312)
    DisableFlag(72500312)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacterCollision(2500600)
    EnableImmortality(2500600)
    DisableHealthBar(2500600)
    SetDistanceLimitForConversationStateChanges(character=2500600, distance=60.0)
    GotoIfFlagEnabled(Label.L0, flag=1040)
    GotoIfFlagEnabled(Label.L0, flag=1041)
    GotoIfFlagEnabled(Label.L1, flag=1042)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(2500600)
    EnableObject(2501015)
    DisableObject(2501016)
    if Client():
        return
    ForceAnimation(2500600, 103010, loop=True, skip_transition=True)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableBackread(2500600)
    DisableObject(2501015)
    EnableObject(2501016)
    End()


@ContinueOnRest(12500011)
def Event_12500011():
    """Event 12500011"""
    if Client():
        return
    DisableFlag(72500330)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2502501))
    
    EnableFlag(72500330)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=2502501))
    
    DisableFlag(72500330)
    Restart()


@ContinueOnRest(12500012)
def Event_12500012():
    """Event 12500012"""
    if Client():
        return
    DisableFlag(72500329)
    
    MAIN.Await(FlagEnabled(72500329))
    
    RotateToFaceEntity(PLAYER, 2500600, animation=101260)
    
    MAIN.Await(FlagDisabled(72500329))
    
    ForceAnimation(PLAYER, 101262)
    Restart()


@ContinueOnRest(12500013)
def Event_12500013():
    """Event 12500013"""
    if Client():
        return
    DisableFlag(72500339)
    
    MAIN.Await(FlagEnabled(72500339))
    
    ForceAnimation(2500600, 103013)
    ForceAnimation(PLAYER, 101263)
    WaitFrames(frames=180)
    DisableFlag(72500339)
    Restart()


@ContinueOnRest(12500014)
def Event_12500014():
    """Event 12500014"""
    if Client():
        return
    DisableFlag(72500337)
    
    MAIN.Await(FlagEnabled(72500337))
    
    ForceAnimation(2500600, 103013)
    ForceAnimation(PLAYER, 101263)
    WaitFrames(frames=180)
    DisableFlag(72500337)
    Restart()


@ContinueOnRest(12500015)
def Event_12500015():
    """Event 12500015"""
    if Client():
        return
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=2500600, attacker=PLAYER))
    
    IncrementEventValue(72500304, bit_count=6, max_value=50)
    AND_1.Add(EventValue(flag=72500304, bit_count=6) >= 50)
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    ForceAnimation(2500600, 103014)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(2500600, 103011)
    DisableFlagRange((1040, 1059))
    EnableFlag(1041)
    SaveRequest()
    Restart()


@ContinueOnRest(12500016)
def Event_12500016():
    """Event 12500016"""
    if Client():
        return
    AND_1.Add(CharacterHasSpecialEffect(2500600, 151))
    AND_1.Add(EventValue(flag=72500304, bit_count=6) < 50)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(2500600, 103010)
    WaitFrames(frames=5)
    Restart()


@ContinueOnRest(12500018)
def Event_12500018():
    """Event 12500018"""
    if Client():
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2502500))
    AND_1.Add(FlagEnabled(1042))
    RunEvent(9350, slot=0, args=(3,))


@ContinueOnRest(12500019)
def Event_12500019():
    """Event 12500019"""
    if Client():
        return
    DisableFlag(72500333)
    
    MAIN.Await(FlagEnabled(72500333))
    
    DisableFlag(72500333)
    if FlagDisabled(72500332):
        return
    IncrementEventValue(72500317, bit_count=3, max_value=5)
    AND_1.Add(EventValue(flag=72500317, bit_count=3) >= 5)
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(72500335)


@ContinueOnRest(12500020)
def Event_12500020():
    """Event 12500020"""
    if Client():
        return
    
    MAIN.Await(FlagEnabled(1042))
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2500020, entity=2501016))
    
    AND_1.Add(PlayerDoesNotHaveGood(4305))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisplayDialog(text=10010150, number_buttons=NumberButtons.OneButton)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(PLAYER, 101140)
    EnableFlag(9043)
    Restart()


@ContinueOnRest(12500021)
def Event_12500021():
    """Event 12500021"""
    if Client():
        return
    DisableFlag(72500331)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=2502500))
    
    EnableFlag(72500331)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=2502500))
    
    DisableFlag(72500331)
    Restart()


@ContinueOnRest(12500030)
def Event_12500030():
    """Event 12500030"""
    MAIN.Await(InsideMap(game_map=CASTLE_CAINHURST))
    
    AddSpecialEffect(PLAYER, 4650)


@RestartOnRest(12500031)
def Event_12500031(_, obj_act_id: int, obj: int):
    """Event 12500031"""
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


@ContinueOnRest(12500050)
def Event_12500050():
    """Event 12500050"""
    GotoIfClient(Label.L0)
    AND_1.Add(FlagEnabled(1347))
    GotoIfConditionFalse(Label.L1, input_condition=AND_1)
    DisableFlagRange((1340, 1359))
    EnableFlag(1348)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_2.Add(FlagEnabled(1351))
    AND_2.Add(FlagEnabled(72500359))
    GotoIfConditionFalse(Label.L2, input_condition=AND_2)
    DisableFlagRange((1340, 1359))
    EnableFlag(1343)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L0, flag=1348)
    GotoIfFlagEnabled(Label.L2, flag=1349)
    GotoIfFlagEnabled(Label.L3, flag=1350)
    GotoIfFlagEnabled(Label.L1, flag=1351)
    DisableBackread(2500790)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableBackread(2500790)
    if Client():
        return
    ForceAnimation(2500790, 103021)
    SetDistanceLimitForConversationStateChanges(character=2500790, distance=60.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableBackread(2500790)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableBackread(2500790)
    if Client():
        return
    SetTeamType(2500790, TeamType.HostileNPC)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableBackread(2500790)
    DisableCharacter(2500790)
    if Client():
        return
    DropMandatoryTreasure(2500790)
    End()


@ContinueOnRest(12500051)
def Event_12500051():
    """Event 12500051"""
    if Client():
        return
    WaitFrames(frames=10)
    AND_1.Add(FlagEnabled(72500357))
    AND_1.Add(FlagEnabled(1348))
    
    MAIN.Await(AND_1)
    
    DisableFlag(72500357)
    SetDistanceLimitForConversationStateChanges(character=2500790, distance=17.0)
    ForceAnimation(2500790, 103022)
    DisableFlagRange((1340, 1359))
    EnableFlag(1351)
    SaveRequest()


@ContinueOnRest(12500052)
def Event_12500052(_, attacked_entity: int, flag: int):
    """Event 12500052"""
    if Client():
        return
    DisableFlag(flag)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    WaitFrames(frames=1)
    EnableFlag(flag)


@ContinueOnRest(12500053)
def Event_12500053(_, character: int, flag: int, flag_1: int):
    """Event 12500053"""
    if Client():
        return
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(HealthRatio(2500790) <= 0.8999999761581421)
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(2500790) != 0.0)
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag_1)
    SetTeamType(character, TeamType.HostileNPC)
    DisableFlagRange((1340, 1359))
    EnableFlag(flag)
    SaveRequest()


@ContinueOnRest(12500054)
def Event_12500054(_, character: int, flag: int):
    """Event 12500054"""
    if Client():
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterDead(character))
    
    DisableFlagRange((1340, 1359))
    EnableFlag(flag)
    SaveRequest()


@ContinueOnRest(12500070)
def Event_12500070(_, obj: int, region: int):
    """Event 12500070"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(obj=obj, animation_id=0)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    ForceAnimation(obj, 0, wait_for_completion=True)
    NotifyDoorEventSoundDampening(obj=obj, state=DoorState.DoorOpening)


@ContinueOnRest(12500072)
def Event_12500072(_, entity: int, state: uchar):
    """Event 12500072"""
    DisableNetworkSync()
    AND_1.Add(FlagRangeAllDisabled(flag_range=(12500076, 12500077)))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2500010, entity=entity))
    AND_2.Add(FlagEnabled(12505074))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2500010, entity=entity))
    AND_3.Add(FlagState(state, FlagType.Absolute, 12500074))
    AND_3.Add(ActionButtonParamActivated(action_button_id=2500010, entity=entity))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    DisplayDialog(text=10010172, number_buttons=NumberButtons.OneButton)
    Restart()


@ContinueOnRest(12500075)
def Event_12500075():
    """Event 12500075"""
    GotoIfFlagDisabled(Label.L0, flag=12500074)
    EndOfAnimation(obj=2501010, animation_id=1)
    Wait(1.0)
    EnableObjectActivation(2501011, obj_act_id=2500010)
    DisableObjectActivation(2501012, obj_act_id=2500010)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=2501010, animation_id=11)
    Wait(1.0)
    DisableObjectActivation(2501011, obj_act_id=2500010)
    EnableObjectActivation(2501012, obj_act_id=2500010)
    EndIfFlagRangeAnyEnabled(flag_range=(12500076, 12500077))
    DisableObjectActivation(2501012, obj_act_id=2500010)


@ContinueOnRest(12500076)
def Event_12500076():
    """Event 12500076"""
    AND_1.Add(FlagDisabled(12505074))
    AND_1.Add(FlagEnabled(12500074))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2502000))
    AND_2.Add(FlagDisabled(12505074))
    AND_2.Add(FlagEnabled(12500074))
    AND_2.Add(ObjectActivated(obj_act_id=12500501))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(12505074)
    DisableObjectActivation(2501011, obj_act_id=2500010)
    ForceAnimation(2501010, 10, wait_for_completion=True)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=2502001))
    
    ForceAnimation(2501010, 11, wait_for_completion=True)
    DisableFlag(12505074)
    DisableFlag(12500074)
    EnableObjectActivation(2501012, obj_act_id=2500010)
    Restart()


@ContinueOnRest(12500077)
def Event_12500077():
    """Event 12500077"""
    AND_1.Add(FlagDisabled(12505074))
    AND_1.Add(FlagDisabled(12500074))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2502001))
    AND_2.Add(FlagDisabled(12505074))
    AND_2.Add(FlagDisabled(12500074))
    AND_2.Add(ObjectActivated(obj_act_id=12500501))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EnableFlag(12505074)
    DisableObjectActivation(2501012, obj_act_id=2500010)
    ForceAnimation(2501010, 0, wait_for_completion=True)
    
    MAIN.Await(CharacterOutsideRegion(PLAYER, region=2502000))
    
    ForceAnimation(2501010, 1, wait_for_completion=True)
    DisableFlag(12505074)
    EnableFlag(12500074)
    EnableObjectActivation(2501011, obj_act_id=2500010)
    Restart()


@ContinueOnRest(12500078)
def Event_12500078():
    """Event 12500078"""
    WaitFrames(frames=0)


@RestartOnRest(12505100)
def Event_12505100(_, character: int, animation_id: int, region: int, patrol_information_id: int):
    """Event 12505100"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    SetNest(character, region=region)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(character)
    DisableGravity(character)
    DisableCharacterCollision(character)
    OR_1.Add(CharacterInsideRegion(PLAYER, region=2502207))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitRandomFrames(min_frames=30, max_frames=45)
    ForceAnimation(character, animation_id, wait_for_completion=True)
    EnableGravity(character)
    EnableCharacterCollision(character)
    EnableAI(character)
    WaitFrames(frames=1)
    SetNest(character, region=region)
    ChangePatrolBehavior(character, patrol_information_id=patrol_information_id)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@ContinueOnRest(12500100)
def Event_12500100(_, character: int, radius: float):
    """Event 12500100"""
    DisableGravity(character)
    DisableCharacterCollision(character)
    
    MAIN.Await(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    
    ForceAnimation(character, 7000)
    EnableGravity(character)
    WaitFrames(frames=14)
    EnableCharacterCollision(character)


@RestartOnRest(12500200)
def Event_12500200(_, first_flag: int, last_flag: int):
    """Event 12500200"""
    DisableFlagRange((first_flag, last_flag))


@ContinueOnRest(12500206)
def Event_12500206(_, attacker__character: int, flag: int, flag_1: int):
    """Event 12500206"""
    MAIN.Await(AttackedWithDamageType(attacked_entity=PLAYER, attacker=attacker__character))
    
    EnableFlag(flag)
    EnableFlag(flag_1)
    OR_1.Add(CharacterDead(attacker__character))
    OR_1.Add(FlagDisabled(flag_1))
    
    MAIN.Await(OR_1)
    
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12500220)
def Event_12500220(_, attacker__character: int, flag: int):
    """Event 12500220"""
    if FlagDisabled(flag):
        MAIN.Await(AttackedWithDamageType(attacked_entity=PLAYER, attacker=attacker__character))
    
        EnableFlag(flag)
        Wait(1.0)
    AND_1.Add(AttackedWithDamageType(attacked_entity=PLAYER, attacker=attacker__character))
    AND_2.Add(TimeElapsed(seconds=300.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(CharacterDead(attacker__character))
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_1)
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12500235)
def Event_12500235(_, character: int, flag: int):
    """Event 12500235"""
    DisableGravity(character)
    DisableCharacterCollision(character)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(character, 6200, wait_for_completion=True)
    EnableGravity(character)
    EnableCharacterCollision(character)


@ContinueOnRest(12500285)
def Event_12500285(_, character: int, radius: float, character_1: int):
    """Event 12500285"""
    DisableAI(character)
    OR_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    OR_1.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)


@RestartOnRest(12500390)
def Event_12500390(_, character: int):
    """Event 12500390"""
    ForceAnimation(character, 7010, loop=True)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, 7012)


@RestartOnRest(12500400)
def Event_12500400(_, character: int, flag: int):
    """Event 12500400"""
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


@RestartOnRest(12500430)
def Event_12500430(_, character: int, attacked_entity: int):
    """Event 12500430"""
    ForceAnimation(attacked_entity, 7010, loop=True)
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    ForceAnimation(attacked_entity, 7012)


@RestartOnRest(12500435)
def Event_12500435(_, attacked_entity: int, region: int):
    """Event 12500435"""
    ForceAnimation(attacked_entity, 7010, loop=True, skip_transition=True)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_2)
    ForceAnimation(attacked_entity, 7012)


@RestartOnRest(12500440)
def Event_12500440(_, character: int, character_1: int):
    """Event 12500440"""
    ForceAnimation(character, 7010, loop=True)
    ForceAnimation(character_1, 7010, loop=True)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=PLAYER))
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=8.0))
    AND_2.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=character_1, other_entity=PLAYER, radius=8.0))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, 7011)
    Wait(1.0)
    ForceAnimation(character_1, 7011)


@RestartOnRest(12500454)
def Event_12500454(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    region: int,
    animation_id_2: int,
    ai_param_id: int,
    ai_param_id_1: int,
    frames: int,
):
    """Event 12500454"""
    ForceAnimation(character, animation_id)
    SetAIParamID(character, ai_param_id=ai_param_id)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(7, input_condition=AND_2)
    ForceAnimation(character, animation_id_1)
    if ValueEqual(left=region, right=2502021):
        SetNest(character, region=region)
        WaitFrames(frames=frames)
    SetAIParamID(character, ai_param_id=ai_param_id_1)
    End()
    ForceAnimation(character, animation_id_2)
    SetAIParamID(character, ai_param_id=ai_param_id_1)


@RestartOnRest(12500458)
def Event_12500458(_, character: int, animation_id: int, region: int, frames: int, region_1: int, animation_id_1: int):
    """Event 12500458"""
    ForceAnimation(character, animation_id_1)
    DisableCharacterCollision(character)
    AND_1.Add(CharacterInsideRegion(PLAYER, region=region))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=region_1))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(3, input_condition=AND_1)
    OR_2.Add(CharacterInsideRegion(PLAYER, region=region))
    OR_2.Add(TimeElapsed(seconds=10.0))
    
    MAIN.Await(OR_2)
    
    ForceAnimation(character, animation_id)
    SetNest(character, region=region)
    WaitFrames(frames=frames)
    EnableCharacterCollision(character)


@ContinueOnRest(12500501)
def Event_12500501():
    """Event 12500501"""
    if ThisEventSlotFlagEnabled():
        EndOfAnimation(obj=2501500, animation_id=0)
        RegisterLadder(start_climbing_flag=12500996, stop_climbing_flag=12500997, obj=2501510)
        DisableObjectActivation(2501501, obj_act_id=2500000)
        EndOfAnimation(obj=2501501, animation_id=0)
        End()
    
    MAIN.Await(ObjectActivated(obj_act_id=12500500))
    
    ForceAnimation(2501500, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=12500996, stop_climbing_flag=12500997, obj=2501510)


@ContinueOnRest(12500502)
def Event_12500502(_, character: int, flag: int, region: int):
    """Event 12500502"""
    DisableGravity(character)
    ForceAnimation(character, 7010, loop=True)
    if ThisEventSlotFlagEnabled():
        MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
        ForceAnimation(character, 7011)
        WaitFrames(frames=35)
        EnableGravity(character)
        End()
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, 7011, skip_transition=True)
    WaitFrames(frames=35)
    EnableGravity(character)


@ContinueOnRest(12500503)
def Event_12500503():
    """Event 12500503"""
    OR_1.Add(HasAIStatus(2500124, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(2500241, ai_status=AIStatusType.Battle))
    OR_1.Add(HasAIStatus(2500276, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    SetAIParamID(2500124, ai_param_id=233022)
    SetNest(2500124, region=2502411)
    AICommand(2500124, command_id=10, command_slot=0)
    OR_2.Add(CharacterInsideRegion(2500124, region=2502411))
    OR_2.Add(TimeElapsed(seconds=8.0))
    
    MAIN.Await(OR_2)
    
    ReplanAI(2500124)
    AICommand(2500124, command_id=-1, command_slot=0)


@ContinueOnRest(12500520)
def Event_12500520(_, character: int, animation_id: int, animation_id_1: int, radius: float, radius_1: float):
    """Event 12500520"""
    WaitRandomFrames(min_frames=0, max_frames=100)
    ForceAnimation(character, animation_id)
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 4652))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius))
    AND_2.Add(CharacterHasSpecialEffect(PLAYER, 4652))
    AND_2.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=radius_1))
    AND_3.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    ForceAnimation(character, animation_id_1)


@RestartOnRest(12500620)
def Event_12500620(_, attacked_entity: int, animation_id: int, animation_id_1: int, flag: int):
    """Event 12500620"""
    ForceAnimation(attacked_entity, animation_id, loop=True, skip_transition=True)
    if FlagEnabled(flag):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    AND_2.Add(FlagEnabled(flag))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_1)
    ForceAnimation(attacked_entity, animation_id_1, wait_for_completion=True, skip_transition=True)
    End()
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(attacked_entity, 7021, wait_for_completion=True, skip_transition=True)


@RestartOnRest(12500630)
def Event_12500630(_, character: int, animation_id: int, animation_id_1: int):
    """Event 12500630"""
    ForceAnimation(character, animation_id, loop=True, skip_transition=True)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    ResetAnimation(character)
    ForceAnimation(character, animation_id_1)


@ContinueOnRest(12500640)
def Event_12500640(_, character: int):
    """Event 12500640"""
    MAIN.Await(CharacterAlive(character))
    
    MAIN.Await(CharacterDead(character))
    
    ClearTargetList(character)
    Restart()


@ContinueOnRest(12500740)
def Event_12500740(_, character: int):
    """Event 12500740"""
    MAIN.Await(CharacterBackreadEnabled(character))
    
    AICommand(character, command_id=100, command_slot=0)


@RestartOnRest(12504000)
def Event_12504000(_, character: int, value: uchar, radius: float):
    """Event 12504000"""
    if ThisEventSlotFlagEnabled():
        return
    DisableCharacter(character)
    AND_1.Add(PlayerInsightAmount() >= value)
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character)
    ForceAnimation(character, 6200, wait_for_completion=True)


@RestartOnRest(12504005)
def Event_12504005(_, character: int, value: uchar, flag: int):
    """Event 12504005"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(PlayerInsightAmount() <= value)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(character)


@ContinueOnRest(101)
def Event_101():
    """Event 101"""
    MAIN.Await(FlagEnabled(100))
    
    EnableMapPiece(map_piece_id=2506001)
    
    MAIN.Await(FlagDisabled(100))
    
    DisableMapPiece(map_piece_id=2506001)
    Restart()


@ContinueOnRest(12500810)
def Event_12500810():
    """Event 12500810"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableObject(2501810)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableMapPiece(map_piece_id=2506000)
    DisableMapPiece(map_piece_id=2506001)
    DisableMapPiece(map_piece_id=2506002)
    DisableMapPiece(map_piece_id=2506003)
    DisableMapPiece(map_piece_id=2506004)
    DisableMapPiece(map_piece_id=2506005)
    DisableMapPiece(map_piece_id=2506006)
    DisableMapPiece(map_piece_id=2506007)
    DisableMapPiece(map_piece_id=2506008)
    DisableMapPiece(map_piece_id=2506009)
    DisableMapPiece(map_piece_id=2506010)
    DisableMapPiece(map_piece_id=2506011)
    DisableMapPiece(map_piece_id=2506012)
    DisableMapPiece(map_piece_id=2506013)
    DisableMapPiece(map_piece_id=2506014)
    DisableMapPiece(map_piece_id=2506015)
    DisableMapPiece(map_piece_id=2506016)
    DisableMapPiece(map_piece_id=2506017)
    DisableMapPiece(map_piece_id=2506070)
    DisableMapPiece(map_piece_id=2506071)
    DisableMapPiece(map_piece_id=2506072)
    DisableMapPiece(map_piece_id=2506073)
    DisableObject(2506018)
    DisableObject(2506019)
    DisableObject(2506020)
    DisableObject(2506021)
    DisableObject(2506022)
    DisableObject(2506023)
    DisableObject(2506024)
    DisableObject(2506025)
    DisableObject(2506026)
    DisableObject(2506027)
    DisableObject(2506028)
    DisableObject(2506029)
    DisableObject(2506030)
    DisableObject(2506031)
    DisableObject(2506032)
    DisableObject(2506033)
    DisableObject(2506034)
    DisableObject(2506035)
    DisableObject(2506036)
    DisableObject(2506039)
    DisableObject(2506040)
    DisableObject(2506041)
    DisableObject(2506042)
    DisableObject(2506043)
    DisableObject(2506044)
    DisableObject(2506045)
    DisableObject(2506046)
    DisableObject(2506047)
    DisableObject(2506048)
    DisableObject(2506049)
    DisableObject(2506050)
    DisableObject(2506051)
    DisableObject(2506052)
    DisableObject(2506053)
    DisableObject(2506054)
    DisableObject(2506055)
    DisableObject(2506056)
    DisableObject(2506057)
    DisableObject(2506058)
    DisableObject(2506059)
    DisableObject(2506060)
    DisableObject(2506061)
    DisableObject(2506062)
    DisableObject(2506063)
    DisableObject(2506064)
    DisableObject(2506065)
    DisableObject(2506066)
    DisableObject(2506067)
    DisableMapCollision(collision=2506037)
    DisableMapCollision(collision=2506038)
    DisableCharacter(2500600)
    DeleteVFX(2503300, erase_root_only=False)
    DeleteVFX(2503301, erase_root_only=False)
    DeleteVFX(2503302, erase_root_only=False)
    DeleteVFX(2503303, erase_root_only=False)
    DeleteVFX(2503304, erase_root_only=False)
    DeleteVFX(2503305, erase_root_only=False)
    DeleteVFX(2503306, erase_root_only=False)
    DeleteVFX(2503307, erase_root_only=False)
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12501800))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2502806))
    AND_1.Add(PlayerArmorInRange(armor_type=ArmorType.Head, required_armor_range_first=250000, required_armor_range_last=250000))
    
    MAIN.Await(AND_1)
    
    AND_15.Add(CharacterHuman(PLAYER))
    if not AND_15:
        return
    EnableFlag(9180)
    WaitFrames(frames=1)
    PlayCutscene(25000010, cutscene_flags=0, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableMapPiece(map_piece_id=2506000)
    EnableMapPiece(map_piece_id=2506001)
    EnableMapPiece(map_piece_id=2506002)
    EnableMapPiece(map_piece_id=2506003)
    EnableMapPiece(map_piece_id=2506004)
    EnableMapPiece(map_piece_id=2506005)
    EnableMapPiece(map_piece_id=2506006)
    EnableMapPiece(map_piece_id=2506007)
    EnableMapPiece(map_piece_id=2506008)
    EnableMapPiece(map_piece_id=2506009)
    EnableMapPiece(map_piece_id=2506010)
    EnableMapPiece(map_piece_id=2506011)
    EnableMapPiece(map_piece_id=2506012)
    EnableMapPiece(map_piece_id=2506013)
    EnableMapPiece(map_piece_id=2506014)
    EnableMapPiece(map_piece_id=2506015)
    EnableMapPiece(map_piece_id=2506016)
    EnableMapPiece(map_piece_id=2506017)
    EnableMapPiece(map_piece_id=2506070)
    EnableMapPiece(map_piece_id=2506071)
    EnableMapPiece(map_piece_id=2506072)
    EnableMapPiece(map_piece_id=2506073)
    EnableObject(2506018)
    EnableObject(2506019)
    EnableObject(2506020)
    EnableObject(2506021)
    EnableObject(2506022)
    EnableObject(2506023)
    EnableObject(2506024)
    EnableObject(2506025)
    EnableObject(2506026)
    EnableObject(2506027)
    EnableObject(2506028)
    EnableObject(2506029)
    EnableObject(2506030)
    EnableObject(2506031)
    EnableObject(2506032)
    EnableObject(2506033)
    EnableObject(2506034)
    EnableObject(2506035)
    EnableObject(2506036)
    EnableObject(2506039)
    EnableObject(2506040)
    EnableObject(2506041)
    EnableObject(2506042)
    EnableObject(2506043)
    EnableObject(2506044)
    EnableObject(2506045)
    EnableObject(2506046)
    EnableObject(2506047)
    EnableObject(2506048)
    EnableObject(2506049)
    EnableObject(2506050)
    EnableObject(2506051)
    EnableObject(2506052)
    EnableObject(2506053)
    EnableObject(2506054)
    EnableObject(2506055)
    EnableObject(2506056)
    EnableObject(2506057)
    EnableObject(2506058)
    EnableObject(2506059)
    EnableObject(2506060)
    EnableObject(2506061)
    EnableObject(2506062)
    EnableObject(2506063)
    EnableObject(2506064)
    EnableObject(2506065)
    EnableObject(2506066)
    EnableObject(2506067)
    EnableMapCollision(collision=2506037)
    EnableMapCollision(collision=2506038)
    EnableCharacter(2500600)
    DisableObject(2501810)
    CreateVFX(2503300)
    CreateVFX(2503301)
    CreateVFX(2503302)
    CreateVFX(2503303)
    CreateVFX(2503304)
    CreateVFX(2503305)
    CreateVFX(2503306)
    CreateVFX(2503307)


@ContinueOnRest(12501800)
def Event_12501800():
    """Event 12501800"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableSoundEvent(sound_id=2503802)
    DisableSoundEvent(sound_id=2503803)
    DisableCharacter(2500800)
    DisableCharacter(2500801)
    DisableCharacter(2500802)
    Kill(2500800)
    Kill(2500801)
    Kill(2500802)
    DisableObject(2501800)
    DeleteVFX(2503800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(2500800))
    
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2501800)
    DeleteVFX(2503800)
    SetLockedCameraSlot(game_map=CASTLE_CAINHURST, camera_slot=0)
    Wait(3.0)
    KillBoss(game_area_param_id=2500800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    
    MAIN.Await(CharacterHuman(PLAYER))
    
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(achievement_id=26)
    EnableFlag(2500)
    EnableFlag(9460)
    StopPlayLogMeasurement(measurement_id=2500000)
    StopPlayLogMeasurement(measurement_id=2500001)
    StopPlayLogMeasurement(measurement_id=2500010)
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


@ContinueOnRest(12501801)
def Event_12501801():
    """Event 12501801"""
    DisableNetworkSync()
    if FlagEnabled(12501800):
        return
    AND_1.Add(FlagEnabled(12501800))
    AND_2.Add(CharacterBackreadDisabled(2500800))
    AND_2.Add(HealthRatio(2500800) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_1)
    PlaySoundEffect(2502800, 0, sound_type=SoundType.c_CharacterMotion)


@ContinueOnRest(12501802)
def Event_12501802():
    """Event 12501802"""
    if FlagEnabled(12501800):
        return
    if ThisEventSlotFlagDisabled():
        ForceAnimation(2500800, 7000)
    AND_1.Add(FlagDisabled(12501800))
    AND_1.Add(ThisEventSlotFlagDisabled())
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2502805))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12504223)
    AND_2.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_2:
        return
    EnableFlag(9180)
    WaitFrames(frames=1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(25000020, cutscene_flags=0, player_id=10000)
    SkipLines(1)
    PlayCutscene(25000020, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(9180)
    EnableFlag(12504800)
    if FlagEnabled(9341):
        return
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9341)


@ContinueOnRest(12501803)
def Event_12501803():
    """Event 12501803"""
    if Client():
        return
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(12501800))
    
    CreateObjectVFX(2500850, vfx_id=200, model_point=900201)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2500030, entity=2500850))
    
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2502000, host_only=False)
    DeleteObjectVFX(2500850)


@ContinueOnRest(12501804)
def Event_12501804():
    """Event 12501804"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(FlagEnabled(12504800))
    
    MAIN.Await(AND_1)
    
    if Host():
        return
    EnableFlag(12504800)
    EnableFlag(12501802)


@ContinueOnRest(12500600)
def Event_12500600():
    """Event 12500600"""
    if Client():
        return
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(12500810))
    
    CreateObjectVFX(2500851, vfx_id=200, model_point=900201)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=2500040, entity=2500851))
    
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2500910, host_only=False)
    DeleteObjectVFX(2500851)


@ContinueOnRest(12504810)
def Event_12504810():
    """Event 12504810"""
    if FlagEnabled(12501800):
        return
    GotoIfFlagEnabled(Label.L0, flag=12501802)
    SkipLinesIfClient(2)
    DisableObject(2501800)
    DeleteVFX(2503800, erase_root_only=False)
    AND_1.Add(FlagDisabled(12501800))
    AND_1.Add(FlagEnabled(12501802))
    
    MAIN.Await(AND_1)
    
    EnableObject(2501800)
    CreateVFX(2503800)

    # --- Label 0 --- #
    DefineLabel(0)
    Move(2500800, destination=2502807, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(2500800, 0)
    AND_1.Add(FlagDisabled(12501800))
    AND_2.Add(CharacterHuman(PLAYER))
    AND_2.Add(ActionButtonParamActivated(action_button_id=2500800, entity=2501800))
    AND_3.Add(FlagEnabled(12501800))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    EndIfFinishedConditionTrue(input_condition=AND_3)
    RotateToFaceEntity(PLAYER, 2502800, animation=101130, wait_for_completion=True)
    AND_4.Add(CharacterHuman(PLAYER))
    AND_4.Add(CharacterInsideRegion(PLAYER, region=2502801))
    AND_5.Add(CharacterHuman(PLAYER))
    AND_5.Add(TimeElapsed(seconds=2.0))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_5)
    EnableFlag(12504800)
    Restart()


@ContinueOnRest(12504811)
def Event_12504811():
    """Event 12504811"""
    DisableNetworkSync()
    if FlagEnabled(12501800):
        return
    AND_1.Add(FlagDisabled(12501800))
    AND_1.Add(FlagEnabled(12501802))
    AND_1.Add(FlagEnabled(12504800))
    AND_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(ActionButtonParamActivated(action_button_id=2500800, entity=2501800))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, 2502500, animation=101130, wait_for_completion=True)
    AND_2.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2502801))
    AND_3.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(TimeElapsed(seconds=2.0))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_3)
    EnableFlag(12504801)
    Restart()


@ContinueOnRest(12504812)
def Event_12504812():
    """Event 12504812"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=2501800, radius=2.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=False)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12504813)
def Event_12504813():
    """Event 12504813"""
    AND_1.Add(CharacterHuman(PLAYER))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=2501800, radius=2.0))
    
    MAIN.Await(AND_1)
    
    SetGravityAndCollisionExcludingOwnWorld(character=PLAYER, state=True)
    WaitFrames(frames=6)
    Restart()


@ContinueOnRest(12504802)
def Event_12504802():
    """Event 12504802"""
    if FlagEnabled(12501800):
        return
    DisableAI(2500800)
    DisableAI(2500801)
    DisableHealthBar(2500800)
    DisableHealthBar(2500801)
    EnableImmortality(2500801)
    DisableCharacter(2500801)
    CreateProjectileOwner(entity=2500802)
    DisableCharacter(2500802)
    GotoIfThisEventFlagEnabled(Label.L0)
    
    MAIN.Await(FlagEnabled(12504800))
    
    GotoIfClient(Label.L0)
    if FlagDisabled(12504223):
        NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2500800, authority_level=UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2500801, authority_level=UpdateAuthority.Forced)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(12504223)
    EnableFlag(12504800)
    GotoIfCoopClientCountComparison(Label.L1, comparison_type=ComparisonType.Equal, value=0)
    GotoIfCoopClientCountComparison(Label.L2, comparison_type=ComparisonType.Equal, value=1)
    GotoIfCoopClientCountComparison(Label.L3, comparison_type=ComparisonType.Equal, value=2)

    # --- Label 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2500800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2500801, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2500802, 7500, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2500800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2500801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2500802)
    Goto(Label.L4)

    # --- Label 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2500800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2500801, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2500802, 7501, affect_npc_part_hp=True)
    WaitFrames(frames=1)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2500800)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2500801)
    AdaptSpecialEffectHealthChangeToNPCPart(character=2500802)
    Goto(Label.L4)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableAI(2500800)
    EnableBossHealthBar(2500800, name=232000)
    CreatePlayLog(name=82)
    StartPlayLogMeasurement(measurement_id=2500010, name=98, overwrite=True)


@ContinueOnRest(12504803)
def Event_12504803():
    """Event 12504803"""
    DisableNetworkSync()
    if FlagEnabled(12501800):
        return
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableSoundEvent(sound_id=2503802)
    DisableSoundEvent(sound_id=2503803)
    AND_1.Add(FlagDisabled(12501800))
    AND_1.Add(FlagEnabled(12504802))
    SkipLinesIfHost(1)
    AND_1.Add(FlagEnabled(12504801))
    AND_1.Add(CharacterInsideRegion(PLAYER, region=2502802))
    
    MAIN.Await(AND_1)
    
    EnableBossMusic(sound_id=2503802)
    AND_2.Add(CharacterHasSpecialEffect(2500800, 5633))

    # --- Label 0 --- #
    DefineLabel(0)
    AND_2.Add(FlagDisabled(12501800))
    AND_2.Add(FlagEnabled(12504802))
    SkipLinesIfHost(1)
    AND_2.Add(FlagEnabled(12504801))
    AND_2.Add(CharacterInsideRegion(PLAYER, region=2502802))
    
    MAIN.Await(AND_2)
    
    DisableBossMusic(sound_id=2503802)
    WaitFrames(frames=0)
    EnableBossMusic(sound_id=2503803)


@ContinueOnRest(12504804)
def Event_12504804():
    """Event 12504804"""
    DisableNetworkSync()
    if FlagEnabled(12501800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(2500800, tae_event_id=100))
    
    SetLockedCameraSlot(game_map=CASTLE_CAINHURST, camera_slot=1)
    
    MAIN.Await(CharacterHasSpecialEffect(2500801, 5610))
    
    SetLockedCameraSlot(game_map=CASTLE_CAINHURST, camera_slot=0)
    Restart()


@ContinueOnRest(12504805)
def Event_12504805():
    """Event 12504805"""
    DisableNetworkSync()
    if FlagEnabled(12501800):
        return
    
    MAIN.Await(FlagEnabled(12501800))
    
    DisableBossMusic(sound_id=2503802)
    DisableBossMusic(sound_id=2503803)
    DisableBossMusic(sound_id=-1)


@ContinueOnRest(12504806)
def Event_12504806():
    """Event 12504806"""
    if FlagEnabled(12501800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(2500800, tae_event_id=100))
    
    AICommand(2500800, command_id=1, command_slot=0)
    ReplanAI(2500800)
    StartPlayLogMeasurement(measurement_id=2501000, name=116, overwrite=True)
    Move(
        2500801,
        destination=2500800,
        destination_type=CoordEntityType.Character,
        model_point=100,
        copy_draw_parent=2500800,
    )
    EnableCharacter(2500801)
    Wait(1.0)
    EnableAI(2500801)
    OR_1.Add(AttackedWithDamageType(attacked_entity=2500801))
    OR_1.Add(TimeElapsed(seconds=60.0))
    OR_1.Add(CharacterDead(2500800))
    
    MAIN.Await(OR_1)
    
    AICommand(2500800, command_id=-1, command_slot=0)
    ReplanAI(2500800)
    StopPlayLogMeasurement(measurement_id=2501000)
    CreateTemporaryVFX(vfx_id=623206, anchor_entity=2500801, model_point=100, anchor_type=CoordEntityType.Character)
    AddSpecialEffect(2500801, 5610)
    DisableCharacter(2500801)
    DisableAI(2500801)
    Restart()


@ContinueOnRest(12504807)
def Event_12504807():
    """Event 12504807"""
    DisableNetworkSync()
    if FlagEnabled(12501800):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(2500800, 5633))
    
    ShootProjectile(
        owner_entity=2500802,
        source_entity=2500800,
        model_point=6,
        behavior_id=223200590,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(1.0)
    Restart()


@ContinueOnRest(12504808)
def Event_12504808():
    """Event 12504808"""
    if FlagEnabled(12501800):
        return
    AND_1.Add(CharacterHasSpecialEffect(2500800, 5633))
    AND_1.Add(CharacterHasTAEEvent(2500800, tae_event_id=10))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(2500800, 5633)
    RemoveSpecialEffect(2500800, 5599)
    WaitFrames(frames=1)
    ForceAnimation(2500800, 2100, wait_for_completion=True)
    Restart()


@ContinueOnRest(12500896)
def Event_12500896(_, region: int):
    """Event 12500896"""
    GotoIfThisEventFlagDisabled(Label.L0)
    DeleteVFX(2503200, erase_root_only=False)
    DeleteVFX(2503201, erase_root_only=False)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterInsideRegion(PLAYER, region=region))
    
    DeleteVFX(2503200)
    DeleteVFX(2503201)
    WaitFrames(frames=10)


@ContinueOnRest(12500898)
def Event_12500898(_, flag: int, flag_1: int, flag_2: int, flag_3: int):
    """Event 12500898"""
    OR_1.Add(FlagEnabled(flag))
    OR_1.Add(FlagEnabled(flag_1))
    OR_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_3))
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=10)
    EnableFlag(12500898)
    if FlagEnabled(flag):
        CreatePlayLog(name=146)
    if FlagEnabled(flag_1):
        CreatePlayLog(name=180)
    if FlagEnabled(flag_2):
        CreatePlayLog(name=214)
    if FlagEnabled(flag_3):
        CreatePlayLog(name=248)


@ContinueOnRest(12500900)
def Event_12500900(_, character: int, flag: int, flag_1: int):
    """Event 12500900"""
    GotoIfFlagEnabled(Label.L0, flag=flag)
    DisableAI(character)
    DisableAnimations(character)
    AddSpecialEffect_WithUnknownEffect(character, 5686)
    RemoveSpecialEffect(character, 5684)
    
    MAIN.Await(FlagEnabled(flag))
    
    WaitRandomFrames(min_frames=10, max_frames=70)
    EnableAI(character)
    RemoveSpecialEffect(character, 5686)
    AddSpecialEffect(character, 5684)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect_WithUnknownEffect(character, 5685)
    DisableAnimations(character)
    
    MAIN.Await(FlagEnabled(flag_1))
    
    RemoveSpecialEffect(character, 5685)
    EnableAnimations(character)
    
    MAIN.Await(FlagDisabled(flag_1))
    
    Restart()


@ContinueOnRest(12501000)
def Event_12501000(_, character: int):
    """Event 12501000"""
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 4652))
    
    SetAIParamID(character, ai_param_id=215001)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(PLAYER, 4652))
    
    SetAIParamID(character, ai_param_id=215001)
    Restart()


@RestartOnRest(12505000)
def Event_12505000(_, character: int, flag: int):
    """Event 12505000"""
    DisableNetworkSync()
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    EnableFlag(flag)
    WaitFrames(frames=3)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Normal))
    
    DisableFlag(flag)
    Restart()


@RestartOnRest(12505300)
def Event_12505300(_, flag: int):
    """Event 12505300"""
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag)
    
    MAIN.Await(FlagDisabled(flag))
    
    DisableFlag(flag)
    Restart()


@ContinueOnRest(12500090)
def Event_12500090():
    """Event 12500090"""
    if ThisEventFlagEnabled():
        return
    if Client():
        return
    
    MAIN.Await(PlayerStandingOnCollision(2503500))
    
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.PrimaryParameters,
        name=282,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.TemporaryParameters,
        name=282,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Weapon,
        name=282,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    PlayLogParameterOutput(
        category=PlayerPlayLogParameter.Armor,
        name=282,
        output_multiplayer_state=PlayLogMultiplayerType.HostOnly,
    )
    RunEvent(9350, slot=0, args=(2,))


@ContinueOnRest(12507010)
def Event_12507010(_, flag: int, destination: int):
    """Event 12507010"""
    MAIN.Await(FlagEnabled(flag))
    
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    ForceAnimation(PLAYER, 101160, skip_transition=True)
    Wait(4.0)
    DisableFlag(flag)


@ContinueOnRest(12507020)
def Event_12507020(_, flag: int, respawn_point_id: int, flag_1: int):
    """Event 12507020"""
    MAIN.Await(FlagEnabled(flag))
    
    DisableFlag(flag)
    WarpPlayerToRespawnPoint(respawn_point_id)
    EnableFlag(flag_1)


@ContinueOnRest(12507040)
def Event_12507040():
    """Event 12507040"""
    SkipLinesIfFlagRangeAnyEnabled(1, (9001, 9010))
    End()
    EnableFlag(9210)
    
    MAIN.Await(FlagDisabled(9210))
    
    if FlagEnabled(9001):
        EnableFlag(12507811)
        EnableFlag(12507810)
        SetRespawnPoint(respawn_point=2502950)
    if FlagEnabled(9002):
        EnableFlag(12507831)
        EnableFlag(12507830)
        SetRespawnPoint(respawn_point=2502951)
    if FlagEnabled(9003):
        EnableFlag(12507851)
        EnableFlag(12507850)
        SetRespawnPoint(respawn_point=2502952)
    if FlagEnabled(9004):
        EnableFlag(12507871)
        EnableFlag(12507870)
        SetRespawnPoint(respawn_point=2502953)
    if FlagEnabled(9005):
        EnableFlag(12507891)
        EnableFlag(12507890)
        SetRespawnPoint(respawn_point=2502954)
    if FlagEnabled(9006):
        EnableFlag(12507911)
        EnableFlag(12507910)
        SetRespawnPoint(respawn_point=2502955)
    if FlagEnabled(9007):
        EnableFlag(12507931)
        EnableFlag(12507930)
        SetRespawnPoint(respawn_point=2502956)
    if FlagEnabled(9008):
        EnableFlag(12507951)
        EnableFlag(12507950)
        SetRespawnPoint(respawn_point=2502957)
    if FlagEnabled(9009):
        EnableFlag(12507971)
        EnableFlag(12507970)
        SetRespawnPoint(respawn_point=2502958)
    if FlagEnabled(9010):
        EnableFlag(12507991)
        EnableFlag(12507990)
        SetRespawnPoint(respawn_point=2502959)
    DisableFlagRange((9000, 9010))


@ContinueOnRest(12507050)
def Event_12507050(_, flag: int, character: int, destination: int):
    """Event 12507050"""
    if FlagEnabled(flag):
        return
    DisableGravity(character)
    
    MAIN.Await(CharacterBackreadEnabled(character))
    
    Move(character, destination=destination, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    ForceAnimation(character, 101165, loop=True)
    Wait(1.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(character, 101166, wait_for_completion=True)
    DisableCharacter(character)
