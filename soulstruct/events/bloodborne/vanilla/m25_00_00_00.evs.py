"""
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
from soulstruct.events.bloodborne import *


def Constructor():
    """ 0: Event 0 """
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
    RunEvent(9220, slot=5, args=(2500710, 12504220, 12504221, 2500, 25, 0), arg_types='iiiiBB')
    RunEvent(9240, slot=5, args=(2500710, 12504220, 12504221, 12504222, 25, 0), arg_types='iiiiBB')
    RunEvent(9260, slot=5, args=(2500710, 12504220, 12504221, 12504222, 25, 0), arg_types='iiiiBB')
    RunEvent(9280, slot=5, args=(2500710, 12504220, 12504221, 2500, 12504223, 25, 0), arg_types='iiiiiBB')
    StartPlayLogMeasurement(2500000, 0, overwrite=False)
    StartPlayLogMeasurement(2500001, 18, overwrite=True)
    RunEvent(12500090)
    RunEvent(101)
    RunEvent(12500001)
    RunEvent(12500011)
    RunEvent(12500012)
    RunEvent(12500013)
    RunEvent(12500014)
    RunEvent(12500015)
    RunEvent(12500016)
    RunEvent(12500018)
    RunEvent(12500019)
    RunEvent(12500020)
    RunEvent(12500021)
    RunEvent(12500052, slot=0, args=(2500790, 72500358))
    RunEvent(12500051)
    RunEvent(12500053, slot=0, args=(2500790, 1349, 72500358))
    RunEvent(12500054, slot=0, args=(2500790, 1350))
    RunEvent(12500072, slot=0, args=(2501011, 0), arg_types='iB')
    RunEvent(12500072, slot=1, args=(2501012, 1), arg_types='iB')
    RunEvent(12500075)
    RunEvent(12500076)
    RunEvent(12500077)
    RegisterLadder(start_climbing_flag=12500992, stop_climbing_flag=12500993, obj=2501502)
    RunEvent(12500620, slot=0, args=(2500115, 7000, 7003, 12500898))
    RunEvent(12500620, slot=1, args=(2500116, 7000, 7003, 12500898))
    RunEvent(12500620, slot=2, args=(2500118, 7000, 7003, 12500898))
    RunEvent(12500620, slot=3, args=(2500119, 7010, 7013, 12500898))
    RunEvent(12500620, slot=4, args=(2500126, 7000, 7003, 12500898))
    RunEvent(12500740, slot=0, args=(2500115,))
    RunEvent(12500740, slot=1, args=(2500116,))
    RunEvent(12500740, slot=2, args=(2500118,))
    RunEvent(12500740, slot=3, args=(2500119,))
    RunEvent(12500740, slot=4, args=(2500126,))
    RunEvent(12500630, slot=0, args=(2500127, 7000, 7001))
    RunEvent(12500630, slot=1, args=(2500128, 7010, 7011))
    RunEvent(12500630, slot=2, args=(2500129, 7000, 7001))
    RunEvent(12500630, slot=3, args=(2500132, 7010, 7011))
    RunEvent(12500630, slot=4, args=(2500137, 7010, 7011))
    RunEvent(12500630, slot=5, args=(2500138, 7000, 7001))
    RunEvent(12500454, slot=0, args=(2500172, 7023, 7013, 2502020, 4294967295, 122008, 122009, 150))
    RunEvent(12500454, slot=1, args=(2500173, 7010, 7017, 2502021, 4294967295, 122008, 122009, 150))
    RunEvent(12500454, slot=2, args=(2500182, 7028, 7018, 2502024, 4294967295, 122008, 122009, 150))
    RunEvent(12500454, slot=3, args=(2500183, 7029, 7019, 2502024, 4294967295, 122008, 122009, 150))
    RunEvent(12500458, slot=0, args=(2500160, 7015, 2502022, 100, 2502023, 7025))
    RunEvent(12500458, slot=1, args=(2500161, 7016, 2502023, 100, 2502022, 7026))
    RunEvent(12500640, slot=0, args=(2500200,))
    RunEvent(12500640, slot=1, args=(2500201,))
    RunEvent(12500640, slot=2, args=(2500202,))
    RunEvent(12500640, slot=3, args=(2500203,))
    RunEvent(12500640, slot=4, args=(2500204,))
    RunEvent(12500640, slot=5, args=(2500205,))
    RunEvent(12500640, slot=6, args=(2500207,))
    RunEvent(12500640, slot=7, args=(2500208,))
    RunEvent(12500640, slot=8, args=(2500209,))
    RunEvent(12500640, slot=9, args=(2500210,))
    RunEvent(12500640, slot=10, args=(2500211,))
    RunEvent(12500640, slot=11, args=(2500212,))
    RunEvent(12500640, slot=12, args=(2500213,))
    RunEvent(12500640, slot=13, args=(2500217,))
    RunEvent(12500640, slot=14, args=(2500218,))
    RunEvent(12500640, slot=15, args=(2500219,))
    RunEvent(12500640, slot=16, args=(2500220,))
    RunEvent(12500640, slot=17, args=(2500222,))
    RunEvent(12500640, slot=18, args=(2500223,))
    RunEvent(12500640, slot=19, args=(2500224,))
    RunEvent(12500640, slot=20, args=(2500230,))
    RunEvent(12500640, slot=21, args=(2500231,))
    RunEvent(12500640, slot=22, args=(2500232,))
    RunEvent(12500640, slot=23, args=(2500233,))
    RunEvent(12500640, slot=24, args=(2500234,))
    RunEvent(12500640, slot=25, args=(2500236,))
    RunEvent(12500640, slot=26, args=(2500237,))
    RunEvent(12500640, slot=27, args=(2500238,))
    RunEvent(12500640, slot=28, args=(2500240,))
    RunEvent(12500640, slot=29, args=(2500241,))
    RunEvent(12500640, slot=30, args=(2500243,))
    RunEvent(12500640, slot=31, args=(2500245,))
    RunEvent(12500640, slot=32, args=(2500246,))
    RunEvent(12500640, slot=33, args=(2500248,))
    RunEvent(12500640, slot=34, args=(2500249,))
    RunEvent(12500640, slot=35, args=(2500250,))
    RunEvent(12500640, slot=36, args=(2500251,))
    RunEvent(12500640, slot=37, args=(2500252,))
    RunEvent(12500640, slot=38, args=(2500254,))
    RunEvent(12500640, slot=39, args=(2500255,))
    RunEvent(12500640, slot=40, args=(2500256,))
    RunEvent(12500640, slot=41, args=(2500272,))
    RunEvent(12500640, slot=42, args=(2500273,))
    RunEvent(12500640, slot=43, args=(2500274,))
    RunEvent(12500640, slot=44, args=(2500275,))
    RunEvent(12500640, slot=45, args=(2500276,))
    RunEvent(12500078)
    RunEvent(12500896, slot=0, args=(2502102,))
    RunEvent(12500898, slot=0, args=(52500200, 52500210, 52500220, 52500230))
    RunEvent(12500900, slot=0, args=(2500200, 12500898, 12505200))
    RunEvent(12500900, slot=1, args=(2500201, 12500898, 12505201))
    RunEvent(12500900, slot=2, args=(2500202, 12500898, 12505202))
    RunEvent(12500900, slot=3, args=(2500203, 12500898, 12505203))
    RunEvent(12500900, slot=4, args=(2500204, 12500898, 12505204))
    RunEvent(12500900, slot=5, args=(2500205, 12500898, 12505205))
    RunEvent(12500900, slot=6, args=(2500207, 12500898, 12505207))
    RunEvent(12500900, slot=7, args=(2500208, 12500898, 12505208))
    RunEvent(12500900, slot=8, args=(2500209, 12500898, 12505209))
    RunEvent(12500900, slot=9, args=(2500210, 12500898, 12505210))
    RunEvent(12500900, slot=10, args=(2500211, 12500898, 12505211))
    RunEvent(12500900, slot=11, args=(2500212, 12500898, 12505212))
    RunEvent(12500900, slot=12, args=(2500213, 12500898, 12505213))
    RunEvent(12500900, slot=13, args=(2500217, 12500896, 12505217))
    RunEvent(12500900, slot=14, args=(2500218, 12500896, 12505218))
    RunEvent(12500900, slot=15, args=(2500219, 12500896, 12505219))
    RunEvent(12500900, slot=16, args=(2500220, 12500896, 12505220))
    RunEvent(12500900, slot=17, args=(2500222, 12500896, 12505222))
    RunEvent(12500900, slot=18, args=(2500223, 12500896, 12505223))
    RunEvent(12500900, slot=19, args=(2500224, 12500896, 12505224))
    RunEvent(12500900, slot=20, args=(2500230, 12500078, 12505230))
    RunEvent(12500900, slot=21, args=(2500231, 12500078, 12505231))
    RunEvent(12500900, slot=22, args=(2500232, 12500078, 12505232))
    RunEvent(12500900, slot=23, args=(2500233, 12500078, 12505233))
    RunEvent(12500900, slot=24, args=(2500234, 12500078, 12505234))
    RunEvent(12500900, slot=25, args=(2500236, 12500078, 12505236))
    RunEvent(12500900, slot=26, args=(2500237, 12500078, 12505237))
    RunEvent(12500900, slot=27, args=(2500238, 12500078, 12505238))
    RunEvent(12500900, slot=28, args=(2500240, 12500078, 12505240))
    RunEvent(12500900, slot=29, args=(2500241, 12500078, 12505241))
    RunEvent(12500900, slot=30, args=(2500243, 12500078, 12505243))
    RunEvent(12500900, slot=31, args=(2500245, 12500078, 12505245))
    RunEvent(12500900, slot=32, args=(2500246, 12500078, 12505246))
    RunEvent(12500900, slot=33, args=(2500248, 12500078, 12505248))
    RunEvent(12500900, slot=34, args=(2500249, 12500078, 12505249))
    RunEvent(12500900, slot=35, args=(2500250, 12500078, 12505250))
    RunEvent(12500900, slot=36, args=(2500251, 12500078, 12505251))
    RunEvent(12500900, slot=37, args=(2500252, 12500898, 12505252))
    RunEvent(12500900, slot=38, args=(2500254, 12500898, 12505254))
    RunEvent(12500900, slot=39, args=(2500255, 12500898, 12505255))
    RunEvent(12500900, slot=40, args=(2500256, 12500898, 12505256))
    RunEvent(12500900, slot=41, args=(2500272, 12500078, 12505272))
    RunEvent(12500900, slot=42, args=(2500273, 12500078, 12505273))
    RunEvent(12500900, slot=43, args=(2500274, 12500078, 12505274))
    RunEvent(12500900, slot=44, args=(2500275, 12500078, 12505275))
    RunEvent(12500900, slot=45, args=(2500276, 12500078, 12505276))
    RunEvent(12505000, slot=0, args=(2500200, 12505200))
    RunEvent(12505000, slot=1, args=(2500201, 12505201))
    RunEvent(12505000, slot=2, args=(2500202, 12505202))
    RunEvent(12505000, slot=3, args=(2500203, 12505203))
    RunEvent(12505000, slot=4, args=(2500204, 12505204))
    RunEvent(12505000, slot=5, args=(2500205, 12505205))
    RunEvent(12505000, slot=6, args=(2500207, 12505207))
    RunEvent(12505000, slot=7, args=(2500208, 12505208))
    RunEvent(12505000, slot=8, args=(2500209, 12505209))
    RunEvent(12505000, slot=9, args=(2500210, 12505210))
    RunEvent(12505000, slot=10, args=(2500211, 12505211))
    RunEvent(12505000, slot=11, args=(2500212, 12505212))
    RunEvent(12505000, slot=12, args=(2500213, 12505213))
    RunEvent(12505000, slot=13, args=(2500217, 12505217))
    RunEvent(12505000, slot=14, args=(2500218, 12505218))
    RunEvent(12505000, slot=15, args=(2500219, 12505219))
    RunEvent(12505000, slot=16, args=(2500220, 12505220))
    RunEvent(12505000, slot=17, args=(2500222, 12505222))
    RunEvent(12505000, slot=18, args=(2500223, 12505223))
    RunEvent(12505000, slot=19, args=(2500224, 12505224))
    RunEvent(12505000, slot=20, args=(2500230, 12505230))
    RunEvent(12505000, slot=21, args=(2500231, 12505231))
    RunEvent(12505000, slot=22, args=(2500232, 12505232))
    RunEvent(12505000, slot=23, args=(2500233, 12505233))
    RunEvent(12505000, slot=24, args=(2500234, 12505234))
    RunEvent(12505000, slot=25, args=(2500236, 12505236))
    RunEvent(12505000, slot=26, args=(2500237, 12505237))
    RunEvent(12505000, slot=27, args=(2500238, 12505238))
    RunEvent(12505000, slot=28, args=(2500240, 12505240))
    RunEvent(12505000, slot=29, args=(2500241, 12505241))
    RunEvent(12505000, slot=30, args=(2500243, 12505243))
    RunEvent(12505000, slot=31, args=(2500245, 12505245))
    RunEvent(12505000, slot=32, args=(2500246, 12505246))
    RunEvent(12505000, slot=33, args=(2500248, 12505248))
    RunEvent(12505000, slot=34, args=(2500249, 12505249))
    RunEvent(12505000, slot=35, args=(2500250, 12505250))
    RunEvent(12505000, slot=36, args=(2500251, 12505251))
    RunEvent(12505000, slot=37, args=(2500252, 12505252))
    RunEvent(12505000, slot=38, args=(2500254, 12505254))
    RunEvent(12505000, slot=39, args=(2500255, 12505255))
    RunEvent(12505000, slot=40, args=(2500256, 12505256))
    RunEvent(12505000, slot=41, args=(2500272, 12505272))
    RunEvent(12505000, slot=42, args=(2500273, 12505273))
    RunEvent(12505000, slot=43, args=(2500274, 12505274))
    RunEvent(12505000, slot=44, args=(2500275, 12505275))
    RunEvent(12505000, slot=45, args=(2500276, 12505276))
    RunEvent(12505300, slot=0, args=(12505200,))
    RunEvent(12505300, slot=1, args=(12505201,))
    RunEvent(12505300, slot=2, args=(12505202,))
    RunEvent(12505300, slot=3, args=(12505203,))
    RunEvent(12505300, slot=4, args=(12505204,))
    RunEvent(12505300, slot=5, args=(12505205,))
    RunEvent(12505300, slot=6, args=(12505207,))
    RunEvent(12505300, slot=7, args=(12505208,))
    RunEvent(12505300, slot=8, args=(12505209,))
    RunEvent(12505300, slot=9, args=(12505210,))
    RunEvent(12505300, slot=10, args=(12505211,))
    RunEvent(12505300, slot=11, args=(12505212,))
    RunEvent(12505300, slot=12, args=(12505213,))
    RunEvent(12505300, slot=13, args=(12505217,))
    RunEvent(12505300, slot=14, args=(12505218,))
    RunEvent(12505300, slot=15, args=(12505219,))
    RunEvent(12505300, slot=16, args=(12505220,))
    RunEvent(12505300, slot=17, args=(12505222,))
    RunEvent(12505300, slot=18, args=(12505223,))
    RunEvent(12505300, slot=19, args=(12505224,))
    RunEvent(12505300, slot=20, args=(12505230,))
    RunEvent(12505300, slot=21, args=(12505231,))
    RunEvent(12505300, slot=22, args=(12505232,))
    RunEvent(12505300, slot=23, args=(12505233,))
    RunEvent(12505300, slot=24, args=(12505234,))
    RunEvent(12505300, slot=25, args=(12505236,))
    RunEvent(12505300, slot=26, args=(12505237,))
    RunEvent(12505300, slot=27, args=(12505238,))
    RunEvent(12505300, slot=28, args=(12505240,))
    RunEvent(12505300, slot=29, args=(12505241,))
    RunEvent(12505300, slot=30, args=(12505243,))
    RunEvent(12505300, slot=31, args=(12505245,))
    RunEvent(12505300, slot=32, args=(12505246,))
    RunEvent(12505300, slot=33, args=(12505248,))
    RunEvent(12505300, slot=34, args=(12505249,))
    RunEvent(12505300, slot=35, args=(12505250,))
    RunEvent(12505300, slot=36, args=(12505251,))
    RunEvent(12505300, slot=37, args=(12505252,))
    RunEvent(12505300, slot=38, args=(12505254,))
    RunEvent(12505300, slot=39, args=(12505255,))
    RunEvent(12505300, slot=40, args=(12505256,))
    RunEvent(12505300, slot=41, args=(12505272,))
    RunEvent(12505300, slot=42, args=(12505273,))
    RunEvent(12505300, slot=43, args=(12505274,))
    RunEvent(12505300, slot=44, args=(12505275,))
    RunEvent(12505300, slot=45, args=(12505276,))
    RunEvent(12501000, slot=0, args=(2500200,))
    RunEvent(12501000, slot=1, args=(2500201,))
    RunEvent(12501000, slot=2, args=(2500202,))
    RunEvent(12501000, slot=3, args=(2500203,))
    RunEvent(12501000, slot=4, args=(2500204,))
    RunEvent(12501000, slot=5, args=(2500205,))
    RunEvent(12501000, slot=6, args=(2500207,))
    RunEvent(12501000, slot=7, args=(2500208,))
    RunEvent(12501000, slot=8, args=(2500209,))
    RunEvent(12501000, slot=9, args=(2500210,))
    RunEvent(12501000, slot=10, args=(2500211,))
    RunEvent(12501000, slot=11, args=(2500212,))
    RunEvent(12501000, slot=12, args=(2500213,))
    RunEvent(12501000, slot=13, args=(2500217,))
    RunEvent(12501000, slot=14, args=(2500218,))
    RunEvent(12501000, slot=15, args=(2500219,))
    RunEvent(12501000, slot=16, args=(2500220,))
    RunEvent(12501000, slot=17, args=(2500222,))
    RunEvent(12501000, slot=18, args=(2500223,))
    RunEvent(12501000, slot=19, args=(2500224,))
    RunEvent(12501000, slot=20, args=(2500230,))
    RunEvent(12501000, slot=21, args=(2500231,))
    RunEvent(12501000, slot=22, args=(2500232,))
    RunEvent(12501000, slot=23, args=(2500233,))
    RunEvent(12501000, slot=24, args=(2500234,))
    RunEvent(12501000, slot=25, args=(2500236,))
    RunEvent(12501000, slot=26, args=(2500237,))
    RunEvent(12501000, slot=27, args=(2500238,))
    RunEvent(12501000, slot=28, args=(2500240,))
    RunEvent(12501000, slot=29, args=(2500243,))
    RunEvent(12501000, slot=32, args=(2500248,))
    RunEvent(12501000, slot=33, args=(2500249,))
    RunEvent(12501000, slot=34, args=(2500250,))
    RunEvent(12501000, slot=35, args=(2500251,))
    RunEvent(12501000, slot=36, args=(2500252,))
    RunEvent(12501000, slot=37, args=(2500254,))
    RunEvent(12501000, slot=38, args=(2500255,))
    RunEvent(12501000, slot=39, args=(2500256,))
    RunEvent(12501000, slot=40, args=(2500272,))
    RunEvent(12501000, slot=41, args=(2500273,))
    RunEvent(12501000, slot=42, args=(2500274,))
    RunEvent(12501000, slot=43, args=(2500275,))
    RunEvent(12500030)
    RunEvent(12500031, slot=0, args=(12501200, 2501200))
    RunEvent(12500031, slot=1, args=(12501204, 2501204))
    RunEvent(12500031, slot=2, args=(12501205, 2501205))
    RunEvent(12500031, slot=3, args=(12501208, 2501208))
    RunEvent(12500031, slot=4, args=(12501209, 2501209))
    RunEvent(12500031, slot=5, args=(12501210, 2501210))
    RunEvent(12500031, slot=6, args=(12501211, 2501211))
    RunEvent(12500200, slot=0, args=(12500250, 12500259))
    RunEvent(12500200, slot=1, args=(12500270, 12500279))
    RunEvent(12500206, slot=0, args=(2500114, 12500250, 12500270))
    RunEvent(12500220, slot=0, args=(2500114, 12500270))
    RunEvent(12500206, slot=1, args=(2500115, 12500251, 12500271))
    RunEvent(12500220, slot=1, args=(2500115, 12500271))
    RunEvent(12500206, slot=2, args=(2500116, 12500252, 12500272))
    RunEvent(12500220, slot=2, args=(2500116, 12500272))
    RunEvent(12500206, slot=4, args=(2500118, 12500254, 12500274))
    RunEvent(12500220, slot=4, args=(2500118, 12500274))
    RunEvent(12500206, slot=5, args=(2500122, 12500255, 12500275))
    RunEvent(12500220, slot=5, args=(2500122, 12500275))
    RunEvent(12500206, slot=6, args=(2500123, 12500256, 12500276))
    RunEvent(12500220, slot=6, args=(2500123, 12500276))
    RunEvent(12500206, slot=7, args=(2500124, 12500257, 12500277))
    RunEvent(12500220, slot=7, args=(2500124, 12500277))
    RunEvent(12500206, slot=8, args=(2500132, 12500259, 12500279))
    RunEvent(12500220, slot=8, args=(2500132, 12500279))
    RunEvent(12500520, slot=0, args=(2500211, 7000, 7001, 3.0, 3.0), arg_types='iiiff')
    RunEvent(12500520, slot=1, args=(2500208, 7000, 7001, 3.0, 3.0), arg_types='iiiff')
    RunEvent(12500520, slot=2, args=(2500204, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=3, args=(2500200, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=4, args=(2500255, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=5, args=(2500207, 7000, 7001, 3.0, 3.0), arg_types='iiiff')
    RunEvent(12500520, slot=6, args=(2500217, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=7, args=(2500220, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=8, args=(2500224, 7000, 7001, 3.0, 3.0), arg_types='iiiff')
    RunEvent(12500520, slot=9, args=(2500230, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=10, args=(2500231, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=11, args=(2500238, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=12, args=(2500236, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=13, args=(2500272, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=14, args=(2500275, 7000, 7001, 3.0, 3.0), arg_types='iiiff')
    RunEvent(12500520, slot=15, args=(2500274, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=16, args=(2500250, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=17, args=(2500249, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=18, args=(2500243, 7000, 7001, 3.0, 3.0), arg_types='iiiff')
    RunEvent(12500520, slot=19, args=(2500251, 7000, 7001, 3.0, 3.0), arg_types='iiiff')
    RunEvent(12500520, slot=20, args=(2500245, 7002, 0, 5.0, 15.0), arg_types='iiiff')
    RunEvent(12500520, slot=21, args=(2500104, 7001, 7007, 10.0, 10.0), arg_types='iiiff')
    RunEvent(12500520, slot=22, args=(2500105, 7001, 7007, 10.0, 10.0), arg_types='iiiff')
    RunEvent(12500520, slot=23, args=(2500106, 7002, 0, 5.0, 5.0), arg_types='iiiff')
    RunEvent(12500100, slot=0, args=(2500280, 8.0), arg_types='if')
    RunEvent(12500100, slot=1, args=(2500281, 16.0), arg_types='if')
    RunEvent(12500100, slot=2, args=(2500282, 9.0), arg_types='if')
    RunEvent(12500100, slot=3, args=(2500284, 8.0), arg_types='if')
    RunEvent(12500100, slot=4, args=(2500285, 7.0), arg_types='if')
    RunEvent(12500100, slot=5, args=(2500292, 8.0), arg_types='if')
    RunEvent(12500100, slot=6, args=(2500293, 7.0), arg_types='if')
    RunEvent(12500100, slot=7, args=(2500294, 9.0), arg_types='if')
    RunEvent(12500070, slot=0, args=(2501020, 2502030))
    RunEvent(12500070, slot=1, args=(2501207, 2502031))
    RunEvent(12505100, slot=0, args=(2500101, 7020, 2502050, 2502030))
    RunEvent(12505100, slot=1, args=(2500102, 7021, 2502051, 2502031))
    RunEvent(12505100, slot=2, args=(2500103, 7022, 2502052, 2502032))
    RunEvent(12500285, slot=0, args=(2500352, 18.0, 2500308), arg_types='ifi')
    RunEvent(12500285, slot=1, args=(2500308, 50.0, 0), arg_types='ifi')
    RunEvent(12500285, slot=2, args=(2500353, 22.0, 2500352), arg_types='ifi')
    RunEvent(12500285, slot=3, args=(2500354, 18.0, 2500353), arg_types='ifi')
    RunEvent(12500235, slot=0, args=(2500210, 12500898))
    RunEvent(12500390, slot=0, args=(2500180,))
    RunEvent(12500435, slot=0, args=(2500133, 2502150))
    RunEvent(12500440, slot=0, args=(2500134, 2500135))
    RunEvent(12500501)
    RunEvent(12500502, slot=0, args=(2500136, 52500190, 2502409))
    RunEvent(12500400, slot=0, args=(2500400, 52500990))
    RunEvent(12500400, slot=1, args=(2500401, 52500980))
    RunEvent(12500400, slot=2, args=(2500402, 52500970))
    RunEvent(12500400, slot=3, args=(2500403, 52500960))
    RunEvent(12500400, slot=4, args=(2500404, 52500950))
    RunEvent(12504812)
    RunEvent(12504813)
    RunEvent(12501800)
    RunEvent(12501801)
    RunEvent(12501802)
    RunEvent(12504810)
    RunEvent(12504811)
    RunEvent(12504802)
    RunEvent(12504803)
    RunEvent(12504804)
    RunEvent(12504805)
    RunEvent(12504806)
    RunEvent(12504806)
    RunEvent(12504807)
    RunEvent(12504808)
    RunEvent(12501804)
    RunEvent(12500810)
    RunEvent(12501803)
    RunEvent(12500600)


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(12500010)
    RunEvent(12500050)
    DisableSoundEvent(2503900)
    RunEvent(12500000)


def Event12500000():
    """ 12500000: Event 12500000 """
    EndIfThisEventOn()
    EndIfClient()
    EnableFlag(9180)
    WaitFrames(1)
    EnableFlag(12200134)
    PlayCutscene(25000000, skippable=True, fade_out=True, player_id=PLAYER)
    WaitFrames(1)
    AwardAchievement(10)
    DisableFlag(9180)


def Event12500001():
    """ 12500001: Event 12500001 """
    EndIfThisEventOn()
    EndIfClient()
    IfCharacterInsideRegion(0, PLAYER, region=2502500)
    RunEvent(9350, slot=0, args=(2,))


def Event12500010():
    """ 12500010: Event 12500010 """
    GotoIfClient(Label.L0)
    IfFlagOn(1, 1041)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1040, 1059))
    EnableFlag(1042)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(2, 1042)
    IfFlagOn(2, 72500328)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    DisableFlag(72500328)
    DisableFlagRange((1040, 1059))
    EnableFlag(1040)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagOn(3, 1040)
    IfFlagOn(-1, 1347)
    IfFlagOn(-1, 1348)
    IfFlagOn(-1, 1349)
    IfConditionTrue(3, input_condition=-1)
    GotoIfConditionFalse(Label.L3, input_condition=3)
    DisableFlagRange((1040, 1059))
    EnableFlag(1042)

    # --- 3 --- #
    DefineLabel(3)
    DisableFlag(72500320)
    DisableFlag(72500312)
    DisableFlag(72500312)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacterCollision(2500600)
    EnableImmortality(2500600)
    DisableHealthBar(2500600)
    SetDistanceLimitForConversationStateChanges(2500600, distance=60.0)
    GotoIfFlagOn(Label.L0, 1040)
    GotoIfFlagOn(Label.L0, 1041)
    GotoIfFlagOn(Label.L1, 1042)

    # --- 0 --- #
    DefineLabel(0)
    EnableBackread(2500600)
    EnableObject(2501015)
    DisableObject(2501016)
    EndIfClient()
    ForceAnimation(2500600, 103010, loop=True, skip_transition=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableBackread(2500600)
    DisableObject(2501015)
    EnableObject(2501016)
    End()


def Event12500011():
    """ 12500011: Event 12500011 """
    EndIfClient()
    DisableFlag(72500330)
    IfCharacterInsideRegion(0, PLAYER, region=2502501)
    EnableFlag(72500330)
    IfCharacterOutsideRegion(0, PLAYER, region=2502501)
    DisableFlag(72500330)
    Restart()


def Event12500012():
    """ 12500012: Event 12500012 """
    EndIfClient()
    DisableFlag(72500329)
    IfFlagOn(0, 72500329)
    RotateToFaceEntity(PLAYER, 2500600, animation=101260, wait_for_completion=False)
    IfFlagOff(0, 72500329)
    ForceAnimation(PLAYER, 101262)
    Restart()


def Event12500013():
    """ 12500013: Event 12500013 """
    EndIfClient()
    DisableFlag(72500339)
    IfFlagOn(0, 72500339)
    ForceAnimation(2500600, 103013)
    ForceAnimation(PLAYER, 101263)
    WaitFrames(180)
    DisableFlag(72500339)
    Restart()


def Event12500014():
    """ 12500014: Event 12500014 """
    EndIfClient()
    DisableFlag(72500337)
    IfFlagOn(0, 72500337)
    ForceAnimation(2500600, 103013)
    ForceAnimation(PLAYER, 101263)
    WaitFrames(180)
    DisableFlag(72500337)
    Restart()


def Event12500015():
    """ 12500015: Event 12500015 """
    EndIfClient()
    IfDamageType(0, attacked_entity=2500600, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IncrementEventValue(72500304, bit_count=6, max_value=50)
    IfEventValueComparison(1, 72500304, bit_count=6, comparison_type=ComparisonType.GreaterThanOrEqual, value=50)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    ForceAnimation(2500600, 103014)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(2500600, 103011)
    DisableFlagRange((1040, 1059))
    EnableFlag(1041)
    SaveRequest()
    Restart()


def Event12500016():
    """ 12500016: Event 12500016 """
    EndIfClient()
    IfCharacterHasSpecialEffect(1, 2500600, 151)
    IfEventValueComparison(1, 72500304, bit_count=6, comparison_type=ComparisonType.LessThan, value=50)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(2500600, 103010)
    WaitFrames(5)
    Restart()


def Event12500018():
    """ 12500018: Event 12500018 """
    EndIfClient()
    EndIfThisEventOn()
    IfCharacterInsideRegion(1, PLAYER, region=2502500)
    IfFlagOn(1, 1042)
    RunEvent(9350, slot=0, args=(3,))


def Event12500019():
    """ 12500019: Event 12500019 """
    EndIfClient()
    DisableFlag(72500333)
    IfFlagOn(0, 72500333)
    DisableFlag(72500333)
    EndIfFlagOff(72500332)
    IncrementEventValue(72500317, bit_count=3, max_value=5)
    IfEventValueComparison(1, 72500317, bit_count=3, comparison_type=ComparisonType.GreaterThanOrEqual, value=5)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(72500335)


def Event12500020():
    """ 12500020: Event 12500020 """
    EndIfClient()
    IfFlagOn(0, 1042)
    IfBossFogActivated(0, boss_entity_id=2500020, fog_object_id=2501016)
    IfPlayerDoesNotHaveGood(1, 4305, including_box=False)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    DisplayDialog(10010150, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    ForceAnimation(PLAYER, 101140)
    EnableFlag(9043)
    Restart()


def Event12500021():
    """ 12500021: Event 12500021 """
    EndIfClient()
    DisableFlag(72500331)
    IfCharacterInsideRegion(0, PLAYER, region=2502500)
    EnableFlag(72500331)
    IfCharacterOutsideRegion(0, PLAYER, region=2502500)
    DisableFlag(72500331)
    Restart()


def Event12500030():
    """ 12500030: Event 12500030 """
    IfInsideMap(0, game_map=CASTLE_CAINHURST)
    AddSpecialEffect(PLAYER, 4650, affect_npc_part_hp=False)


@RestartOnRest
def Event12500031(arg_0_3: int, arg_4_7: int):
    """ 12500031: Event 12500031 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_4_7, 0)
    DisableObjectActivation(arg_4_7, obj_act_id=-1)
    EnableTreasure(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_0_3)
    WaitFrames(10)
    EnableTreasure(arg_4_7)


def Event12500050():
    """ 12500050: Event 12500050 """
    GotoIfClient(Label.L0)
    IfFlagOn(1, 1347)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1340, 1359))
    EnableFlag(1348)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagOn(2, 1351)
    IfFlagOn(2, 72500359)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    DisableFlagRange((1340, 1359))
    EnableFlag(1343)

    # --- 2 --- #
    DefineLabel(2)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagOn(Label.L0, 1348)
    GotoIfFlagOn(Label.L2, 1349)
    GotoIfFlagOn(Label.L3, 1350)
    GotoIfFlagOn(Label.L1, 1351)
    DisableBackread(2500790)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableBackread(2500790)
    EndIfClient()
    ForceAnimation(2500790, 103021)
    SetDistanceLimitForConversationStateChanges(2500790, distance=60.0)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableBackread(2500790)
    End()

    # --- 2 --- #
    DefineLabel(2)
    EnableBackread(2500790)
    EndIfClient()
    SetTeamType(2500790, TeamType.HostileNPC)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableBackread(2500790)
    DisableCharacter(2500790)
    EndIfClient()
    DropMandatoryTreasure(2500790)
    End()


def Event12500051():
    """ 12500051: Event 12500051 """
    EndIfClient()
    WaitFrames(10)
    IfFlagOn(1, 72500357)
    IfFlagOn(1, 1348)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(72500357)
    SetDistanceLimitForConversationStateChanges(2500790, distance=17.0)
    ForceAnimation(2500790, 103022)
    DisableFlagRange((1340, 1359))
    EnableFlag(1351)
    SaveRequest()


def Event12500052(arg_0_3: int, arg_4_7: int):
    """ 12500052: Event 12500052 """
    EndIfClient()
    DisableFlag(arg_4_7)
    IfDamageType(0, attacked_entity=arg_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    WaitFrames(1)
    IfDamageType(0, attacked_entity=arg_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    WaitFrames(1)
    IfDamageType(0, attacked_entity=arg_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    WaitFrames(1)
    EnableFlag(arg_4_7)


def Event12500053(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12500053: Event 12500053 """
    EndIfClient()
    IfFlagOn(-1, arg_8_11)
    IfHealthLessThanOrEqual(-1, 2500790, 0.8999999761581421)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, 2500790, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(arg_8_11)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    DisableFlagRange((1340, 1359))
    EnableFlag(arg_4_7)
    SaveRequest()


def Event12500054(arg_0_3: int, arg_4_7: int):
    """ 12500054: Event 12500054 """
    EndIfClient()
    EndIfThisEventSlotOn()
    IfCharacterDead(0, arg_0_3)
    DisableFlagRange((1340, 1359))
    EnableFlag(arg_4_7)
    SaveRequest()


def Event12500070(arg_0_3: int, arg_4_7: int):
    """ 12500070: Event 12500070 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(arg_0_3, 0)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=arg_4_7)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    NotifyDoorEventSoundDampening(arg_0_3, state=DoorState.DoorOpening)


def Event12500072(arg_0_3: int, arg_4_4: uchar):
    """ 12500072: Event 12500072 """
    DisableNetworkSync()
    IfFlagRangeAllOff(1, (12500076, 12500077))
    IfBossFogActivated(1, boss_entity_id=2500010, fog_object_id=arg_0_3)
    IfFlagOn(2, 12505074)
    IfBossFogActivated(2, boss_entity_id=2500010, fog_object_id=arg_0_3)
    IfFlagState(3, state=arg_4_4, flag_type=FlagType.Absolute, flag=12500074)
    IfBossFogActivated(3, boss_entity_id=2500010, fog_object_id=arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    DisplayDialog(10010172, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, 
                  number_buttons=NumberButtons.OneButton)
    Restart()


def Event12500075():
    """ 12500075: Event 12500075 """
    GotoIfFlagOff(Label.L0, 12500074)
    EndOfAnimation(2501010, 1)
    Wait(1.0)
    EnableObjectActivation(2501011, obj_act_id=2500010)
    DisableObjectActivation(2501012, obj_act_id=2500010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndOfAnimation(2501010, 11)
    Wait(1.0)
    DisableObjectActivation(2501011, obj_act_id=2500010)
    EnableObjectActivation(2501012, obj_act_id=2500010)
    EndIfFlagRangeAnyOn((12500076, 12500077))
    DisableObjectActivation(2501012, obj_act_id=2500010)


def Event12500076():
    """ 12500076: Event 12500076 """
    IfFlagOff(1, 12505074)
    IfFlagOn(1, 12500074)
    IfCharacterInsideRegion(1, PLAYER, region=2502000)
    IfFlagOff(2, 12505074)
    IfFlagOn(2, 12500074)
    IfObjectActivated(2, obj_act_id=12500501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12505074)
    DisableObjectActivation(2501011, obj_act_id=2500010)
    ForceAnimation(2501010, 10, wait_for_completion=True)
    IfCharacterOutsideRegion(0, PLAYER, region=2502001)
    ForceAnimation(2501010, 11, wait_for_completion=True)
    DisableFlag(12505074)
    DisableFlag(12500074)
    EnableObjectActivation(2501012, obj_act_id=2500010)
    Restart()


def Event12500077():
    """ 12500077: Event 12500077 """
    IfFlagOff(1, 12505074)
    IfFlagOff(1, 12500074)
    IfCharacterInsideRegion(1, PLAYER, region=2502001)
    IfFlagOff(2, 12505074)
    IfFlagOff(2, 12500074)
    IfObjectActivated(2, obj_act_id=12500501)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(12505074)
    DisableObjectActivation(2501012, obj_act_id=2500010)
    ForceAnimation(2501010, 0, wait_for_completion=True)
    IfCharacterOutsideRegion(0, PLAYER, region=2502000)
    ForceAnimation(2501010, 1, wait_for_completion=True)
    DisableFlag(12505074)
    EnableFlag(12500074)
    EnableObjectActivation(2501011, obj_act_id=2500010)
    Restart()


def Event12500078():
    """ 12500078: Event 12500078 """
    WaitFrames(0)


@RestartOnRest
def Event12505100(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12505100: Event 12505100 """
    GotoIfThisEventSlotOff(Label.L0)
    SetNest(arg_0_3, arg_8_11)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_12_15)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    IfCharacterInsideRegion(-1, PLAYER, region=2502207)
    IfDamageType(-1, attacked_entity=arg_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    SetNetworkUpdateRate(arg_0_3, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    WaitRandomFrames(min_frames=30, max_frames=45)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)
    EnableAI(arg_0_3)
    WaitFrames(1)
    SetNest(arg_0_3, arg_8_11)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_12_15)
    SetNetworkUpdateRate(arg_0_3, is_fixed=False, update_rate=CharacterUpdateRate.Always)


def Event12500100(arg_0_3: int, arg_4_7: float):
    """ 12500100: Event 12500100 """
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    IfEntityWithinDistance(0, arg_0_3, PLAYER, radius=arg_4_7)
    ForceAnimation(arg_0_3, 7000)
    EnableGravity(arg_0_3)
    WaitFrames(14)
    EnableCharacterCollision(arg_0_3)


@RestartOnRest
def Event12500200(arg_0_3: int, arg_4_7: int):
    """ 12500200: Event 12500200 """
    DisableFlagRange((arg_0_3, arg_4_7))


def Event12500206(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12500206: Event 12500206 """
    IfDamageType(0, attacked_entity=PLAYER, attacking_character=arg_0_3, damage_type=DamageType.Unspecified)
    EnableFlag(arg_4_7)
    EnableFlag(arg_8_11)
    IfCharacterDead(-1, arg_0_3)
    IfFlagOff(-1, arg_8_11)
    IfConditionTrue(0, input_condition=-1)
    DisableFlag(arg_4_7)
    Restart()


def Event12500220(arg_0_3: int, arg_4_7: int):
    """ 12500220: Event 12500220 """
    SkipLinesIfFlagOn(3, arg_4_7)
    IfDamageType(0, attacked_entity=PLAYER, attacking_character=arg_0_3, damage_type=DamageType.Unspecified)
    EnableFlag(arg_4_7)
    Wait(1.0)
    IfDamageType(1, attacked_entity=PLAYER, attacking_character=arg_0_3, damage_type=DamageType.Unspecified)
    IfTimeElapsed(2, 300.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfCharacterDead(-1, arg_0_3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 1)
    DisableFlag(arg_4_7)
    Restart()


def Event12500235(arg_0_3: int, arg_4_7: int):
    """ 12500235: Event 12500235 """
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    IfFlagOn(0, arg_4_7)
    ForceAnimation(arg_0_3, 6200, wait_for_completion=True)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)


def Event12500285(arg_0_3: int, arg_4_7: float, arg_8_11: int):
    """ 12500285: Event 12500285 """
    DisableAI(arg_0_3)
    IfEntityWithinDistance(-1, arg_0_3, PLAYER, radius=arg_4_7)
    IfAttacked(-1, arg_0_3, attacking_character=PLAYER)
    IfHasAIStatus(-1, arg_8_11, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(arg_0_3)


@RestartOnRest
def Event12500390(arg_0_3: int):
    """ 12500390: Event 12500390 """
    ForceAnimation(arg_0_3, 7010, loop=True)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 7012)


@RestartOnRest
def Event12500400(arg_0_3: int, arg_4_7: int):
    """ 12500400: Event 12500400 """
    GotoIfThisEventSlotOff(Label.L0)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterHuman(1, PLAYER)
    SkipLinesIfClient(1)
    IfFlagOn(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Wait(0.0)


@RestartOnRest
def Event12500430(arg_0_3: int, arg_4_7: int):
    """ 12500430: Event 12500430 """
    ForceAnimation(arg_4_7, 7010, loop=True)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Battle)
    IfDamageType(2, attacked_entity=arg_4_7, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_4_7, 7012)


@RestartOnRest
def Event12500435(arg_0_3: int, arg_4_7: int):
    """ 12500435: Event 12500435 """
    ForceAnimation(arg_0_3, 7010, loop=True, skip_transition=True)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfDamageType(2, attacked_entity=arg_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    ForceAnimation(arg_0_3, 7012)


@RestartOnRest
def Event12500440(arg_0_3: int, arg_4_7: int):
    """ 12500440: Event 12500440 """
    ForceAnimation(arg_0_3, 7010, loop=True)
    ForceAnimation(arg_4_7, 7010, loop=True)
    IfDamageType(-1, attacked_entity=arg_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfDamageType(-1, attacked_entity=arg_4_7, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHasAIStatus(1, arg_0_3, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=8.0)
    IfHasAIStatus(2, arg_4_7, ai_status=AIStatusType.Battle)
    IfEntityWithinDistance(2, arg_4_7, PLAYER, radius=8.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 7011)
    Wait(1.0)
    ForceAnimation(arg_4_7, 7011)


@RestartOnRest
def Event12500454(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int, 
                  arg_24_27: int, arg_28_31: int):
    """ 12500454: Event 12500454 """
    ForceAnimation(arg_0_3, arg_4_7)
    SetAIParamID(arg_0_3, arg_20_23)
    IfCharacterInsideRegion(1, PLAYER, region=arg_12_15)
    IfDamageType(2, attacked_entity=arg_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(7, 2)
    ForceAnimation(arg_0_3, arg_8_11)
    SkipLinesIfNotEqual(2, left=arg_12_15, right=2502021)
    SetNest(arg_0_3, arg_12_15)
    WaitFrames(arg_28_31)
    SetAIParamID(arg_0_3, arg_24_27)
    End()
    ForceAnimation(arg_0_3, arg_16_19)
    SetAIParamID(arg_0_3, arg_24_27)


@RestartOnRest
def Event12500458(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 12500458: Event 12500458 """
    ForceAnimation(arg_0_3, arg_20_23)
    DisableCharacterCollision(arg_0_3)
    IfCharacterInsideRegion(1, PLAYER, region=arg_8_11)
    IfCharacterInsideRegion(2, PLAYER, region=arg_16_19)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(3, 1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_8_11)
    IfTimeElapsed(-2, 10.0)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(arg_0_3, arg_4_7)
    SetNest(arg_0_3, arg_8_11)
    WaitFrames(arg_12_15)
    EnableCharacterCollision(arg_0_3)


def Event12500501():
    """ 12500501: Event 12500501 """
    SkipLinesIfThisEventSlotOff(5)
    EndOfAnimation(2501500, 0)
    RegisterLadder(start_climbing_flag=12500996, stop_climbing_flag=12500997, obj=2501510)
    DisableObjectActivation(2501501, obj_act_id=2500000)
    EndOfAnimation(2501501, 0)
    End()
    IfObjectActivated(0, obj_act_id=12500500)
    ForceAnimation(2501500, 0, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=12500996, stop_climbing_flag=12500997, obj=2501510)


def Event12500502(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12500502: Event 12500502 """
    DisableGravity(arg_0_3)
    ForceAnimation(arg_0_3, 7010, loop=True)
    SkipLinesIfThisEventSlotOff(5)
    IfCharacterInsideRegion(0, PLAYER, region=arg_8_11)
    ForceAnimation(arg_0_3, 7011)
    WaitFrames(35)
    EnableGravity(arg_0_3)
    End()
    IfFlagOn(-1, arg_4_7)
    IfDamageType(-1, attacked_entity=arg_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, 7011, skip_transition=True)
    WaitFrames(35)
    EnableGravity(arg_0_3)


def Event12500503():
    """ 12500503: Event 12500503 """
    IfHasAIStatus(-1, 2500124, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, 2500241, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, 2500276, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    SetAIParamID(2500124, 233022)
    SetNest(2500124, 2502411)
    AICommand(2500124, command_id=10, slot=0)
    IfCharacterInsideRegion(-2, 2500124, region=2502411)
    IfTimeElapsed(-2, 8.0)
    IfConditionTrue(0, input_condition=-2)
    ReplanAI(2500124)
    AICommand(2500124, command_id=-1, slot=0)


def Event12500520(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float, arg_16_19: float):
    """ 12500520: Event 12500520 """
    WaitRandomFrames(min_frames=0, max_frames=100)
    ForceAnimation(arg_0_3, arg_4_7)
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 4652)
    IfEntityWithinDistance(1, arg_0_3, PLAYER, radius=arg_12_15)
    IfCharacterHasSpecialEffect(2, PLAYER, 4652)
    IfEntityWithinDistance(2, arg_0_3, PLAYER, radius=arg_16_19)
    IfHasAIStatus(3, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    ForceAnimation(arg_0_3, arg_8_11)


@RestartOnRest
def Event12500620(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12500620: Event 12500620 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    EndIfFlagOn(arg_12_15)
    IfDamageType(1, attacked_entity=arg_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfFlagOn(2, arg_12_15)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(2, 1)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True, skip_transition=True)
    End()
    EndIfFlagOn(arg_12_15)
    IfFlagOn(0, arg_12_15)
    ForceAnimation(arg_0_3, 7021, wait_for_completion=True, skip_transition=True)


@RestartOnRest
def Event12500630(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12500630: Event 12500630 """
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    IfDamageType(-1, attacked_entity=arg_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    ResetAnimation(arg_0_3, disable_interpolation=False)
    ForceAnimation(arg_0_3, arg_8_11)


def Event12500640(arg_0_3: int):
    """ 12500640: Event 12500640 """
    IfCharacterAlive(0, arg_0_3)
    IfCharacterDead(0, arg_0_3)
    ClearTargetList(arg_0_3)
    Restart()


def Event12500740(arg_0_3: int):
    """ 12500740: Event 12500740 """
    IfCharacterBackreadEnabled(0, arg_0_3)
    AICommand(arg_0_3, command_id=100, slot=0)


@RestartOnRest
def Event12504000(arg_0_3: int, arg_4_4: uchar, arg_8_11: float):
    """ 12504000: Event 12504000 """
    EndIfThisEventSlotOn()
    DisableCharacter(arg_0_3)
    IfPlayerInsightAmountGreaterThanOrEqual(1, arg_4_4)
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(0, input_condition=1)
    EnableCharacter(arg_0_3)
    ForceAnimation(arg_0_3, 6200, wait_for_completion=True)


@RestartOnRest
def Event12504005(arg_0_3: int, arg_4_4: uchar, arg_8_11: int):
    """ 12504005: Event 12504005 """
    GotoIfThisEventSlotOn(Label.L0)
    IfFlagOn(1, arg_8_11)
    IfPlayerInsightAmountLessThanOrEqual(1, arg_4_4)
    IfConditionTrue(0, input_condition=1)

    # --- 0 --- #
    DefineLabel(0)
    Kill(arg_0_3, award_souls=False)


def Event101():
    """ 101: Event 101 """
    IfFlagOn(0, 100)
    EnableMapPiece(2506001)
    IfFlagOff(0, 100)
    DisableMapPiece(2506001)
    Restart()


def Event12500810():
    """ 12500810: Event 12500810 """
    GotoIfThisEventOff(Label.L0)
    DisableObject(2501810)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableMapPiece(2506000)
    DisableMapPiece(2506001)
    DisableMapPiece(2506002)
    DisableMapPiece(2506003)
    DisableMapPiece(2506004)
    DisableMapPiece(2506005)
    DisableMapPiece(2506006)
    DisableMapPiece(2506007)
    DisableMapPiece(2506008)
    DisableMapPiece(2506009)
    DisableMapPiece(2506010)
    DisableMapPiece(2506011)
    DisableMapPiece(2506012)
    DisableMapPiece(2506013)
    DisableMapPiece(2506014)
    DisableMapPiece(2506015)
    DisableMapPiece(2506016)
    DisableMapPiece(2506017)
    DisableMapPiece(2506070)
    DisableMapPiece(2506071)
    DisableMapPiece(2506072)
    DisableMapPiece(2506073)
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
    DisableCollision(2506037)
    DisableCollision(2506038)
    DisableCharacter(2500600)
    DeleteFX(2503300, erase_root_only=False)
    DeleteFX(2503301, erase_root_only=False)
    DeleteFX(2503302, erase_root_only=False)
    DeleteFX(2503303, erase_root_only=False)
    DeleteFX(2503304, erase_root_only=False)
    DeleteFX(2503305, erase_root_only=False)
    DeleteFX(2503306, erase_root_only=False)
    DeleteFX(2503307, erase_root_only=False)
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12501800)
    IfCharacterInsideRegion(1, PLAYER, region=2502806)
    IfPlayerArmorType(1, armor_type=ArmorType.Head, required_armor_range_first=250000, required_armor_range_last=250000)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EnableFlag(9180)
    WaitFrames(1)
    PlayCutscene(25000010, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    EnableMapPiece(2506000)
    EnableMapPiece(2506001)
    EnableMapPiece(2506002)
    EnableMapPiece(2506003)
    EnableMapPiece(2506004)
    EnableMapPiece(2506005)
    EnableMapPiece(2506006)
    EnableMapPiece(2506007)
    EnableMapPiece(2506008)
    EnableMapPiece(2506009)
    EnableMapPiece(2506010)
    EnableMapPiece(2506011)
    EnableMapPiece(2506012)
    EnableMapPiece(2506013)
    EnableMapPiece(2506014)
    EnableMapPiece(2506015)
    EnableMapPiece(2506016)
    EnableMapPiece(2506017)
    EnableMapPiece(2506070)
    EnableMapPiece(2506071)
    EnableMapPiece(2506072)
    EnableMapPiece(2506073)
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
    EnableCollision(2506037)
    EnableCollision(2506038)
    EnableCharacter(2500600)
    DisableObject(2501810)
    CreateFX(2503300)
    CreateFX(2503301)
    CreateFX(2503302)
    CreateFX(2503303)
    CreateFX(2503304)
    CreateFX(2503305)
    CreateFX(2503306)
    CreateFX(2503307)


def Event12501800():
    """ 12501800: Event 12501800 """
    GotoIfThisEventOff(Label.L0)
    DisableSoundEvent(2503802)
    DisableSoundEvent(2503803)
    DisableCharacter(2500800)
    DisableCharacter(2500801)
    DisableCharacter(2500802)
    Kill(2500800, award_souls=False)
    Kill(2500801, award_souls=False)
    Kill(2500802, award_souls=False)
    DisableObject(2501800)
    DeleteFX(2503800, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(0, 2500800)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(2501800)
    DeleteFX(2503800, erase_root_only=True)
    SetLockedCameraSlot(game_map=CASTLE_CAINHURST, camera_slot=0)
    Wait(3.0)
    KillBoss(2500800)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    RunEvent(9350, slot=0, args=(3,))
    AwardAchievement(26)
    EnableFlag(2500)
    EnableFlag(9460)
    StopPlayLogMeasurement(2500000)
    StopPlayLogMeasurement(2500001)
    StopPlayLogMeasurement(2500010)
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


def Event12501801():
    """ 12501801: Event 12501801 """
    DisableNetworkSync()
    EndIfFlagOn(12501800)
    IfFlagOn(1, 12501800)
    IfCharacterBackreadDisabled(2, 2500800)
    IfHealthLessThanOrEqual(2, 2500800, 0.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(1)
    PlaySoundEffect(anchor_entity=2502800, sound_type=SoundType.c_CharacterMotion, sound_id=0)


def Event12501802():
    """ 12501802: Event 12501802 """
    EndIfFlagOn(12501800)
    SkipLinesIfThisEventSlotOn(1)
    ForceAnimation(2500800, 7000)
    IfFlagOff(1, 12501800)
    IfThisEventSlotOff(1)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=2502805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(12504223)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    EnableFlag(9180)
    WaitFrames(1)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(25000020, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(25000020, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    EnableFlag(12504800)
    EndIfFlagOn(9341)
    RunEvent(9350, slot=0, args=(1,))
    EnableFlag(9341)


def Event12501803():
    """ 12501803: Event 12501803 """
    EndIfClient()
    EndIfThisEventOn()
    IfFlagOn(0, 12501800)
    CreateObjectFX(900201, obj=2500850, model_point=200)
    IfBossFogActivated(0, boss_entity_id=2500030, fog_object_id=2500850)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2502000, host_only=False)
    DeleteObjectFX(2500850, erase_root=True)


def Event12501804():
    """ 12501804: Event 12501804 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 12504800)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableFlag(12504800)
    EnableFlag(12501802)


def Event12500600():
    """ 12500600: Event 12500600 """
    EndIfClient()
    EndIfThisEventOn()
    IfFlagOn(0, 12500810)
    CreateObjectFX(900201, obj=2500851, model_point=200)
    IfBossFogActivated(0, boss_entity_id=2500040, fog_object_id=2500851)
    ForceAnimation(PLAYER, 101140)
    AwardItemLot(2500910, host_only=False)
    DeleteObjectFX(2500851, erase_root=True)


def Event12504810():
    """ 12504810: Event 12504810 """
    EndIfFlagOn(12501800)
    GotoIfFlagOn(Label.L0, 12501802)
    SkipLinesIfClient(2)
    DisableObject(2501800)
    DeleteFX(2503800, erase_root_only=False)
    IfFlagOff(1, 12501800)
    IfFlagOn(1, 12501802)
    IfConditionTrue(0, input_condition=1)
    EnableObject(2501800)
    CreateFX(2503800)

    # --- 0 --- #
    DefineLabel(0)
    Move(2500800, destination=2502807, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    ForceAnimation(2500800, 0)
    IfFlagOff(1, 12501800)
    IfCharacterHuman(2, PLAYER)
    IfBossFogActivated(2, boss_entity_id=2500800, fog_object_id=2501800)
    IfFlagOn(3, 12501800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 2502800, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=2502801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(12504800)
    Restart()


def Event12504811():
    """ 12504811: Event 12504811 """
    DisableNetworkSync()
    EndIfFlagOn(12501800)
    IfFlagOff(1, 12501800)
    IfFlagOn(1, 12501802)
    IfFlagOn(1, 12504800)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfBossFogActivated(1, boss_entity_id=2500800, fog_object_id=2501800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 2502500, animation=101130, wait_for_completion=True)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=2502801)
    IfCharacterType(3, PLAYER, CharacterType.WhitePhantom)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(12504801)
    Restart()


def Event12504812():
    """ 12504812: Event 12504812 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, 2501800, radius=2.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event12504813():
    """ 12504813: Event 12504813 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, 2501800, radius=2.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def Event12504802():
    """ 12504802: Event 12504802 """
    EndIfFlagOn(12501800)
    DisableAI(2500800)
    DisableAI(2500801)
    DisableHealthBar(2500800)
    DisableHealthBar(2500801)
    EnableImmortality(2500801)
    DisableCharacter(2500801)
    CreateProjectileOwner(2500802)
    DisableCharacter(2500802)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 12504800)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagOn(1, 12504223)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(2500800, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(2500801, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(12504223)
    EnableFlag(12504800)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(2500800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2500801, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(2500802, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2500800)
    AdaptSpecialEffectHealthChangeToNPCPart(2500801)
    AdaptSpecialEffectHealthChangeToNPCPart(2500802)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(2500800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2500801, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(2500802, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(2500800)
    AdaptSpecialEffectHealthChangeToNPCPart(2500801)
    AdaptSpecialEffectHealthChangeToNPCPart(2500802)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableAI(2500800)
    EnableBossHealthBar(2500800, name=232000, slot=0)
    CreatePlayLog(82)
    StartPlayLogMeasurement(2500010, 98, overwrite=True)


def Event12504803():
    """ 12504803: Event 12504803 """
    DisableNetworkSync()
    EndIfFlagOn(12501800)
    GotoIfThisEventOn(Label.L0)
    DisableSoundEvent(2503802)
    DisableSoundEvent(2503803)
    IfFlagOff(1, 12501800)
    IfFlagOn(1, 12504802)
    SkipLinesIfHost(1)
    IfFlagOn(1, 12504801)
    IfCharacterInsideRegion(1, PLAYER, region=2502802)
    IfConditionTrue(0, input_condition=1)
    SetBossMusicState(2503802, state=True)
    IfCharacterHasSpecialEffect(2, 2500800, 5633)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagOff(2, 12501800)
    IfFlagOn(2, 12504802)
    SkipLinesIfHost(1)
    IfFlagOn(2, 12504801)
    IfCharacterInsideRegion(2, PLAYER, region=2502802)
    IfConditionTrue(0, input_condition=2)
    SetBossMusicState(2503802, state=False)
    WaitFrames(0)
    SetBossMusicState(2503803, state=True)


def Event12504804():
    """ 12504804: Event 12504804 """
    DisableNetworkSync()
    EndIfFlagOn(12501800)
    IfHasTAEEvent(0, 2500800, tae_event_id=100)
    SetLockedCameraSlot(game_map=CASTLE_CAINHURST, camera_slot=1)
    IfCharacterHasSpecialEffect(0, 2500801, 5610)
    SetLockedCameraSlot(game_map=CASTLE_CAINHURST, camera_slot=0)
    Restart()


def Event12504805():
    """ 12504805: Event 12504805 """
    DisableNetworkSync()
    EndIfFlagOn(12501800)
    IfFlagOn(0, 12501800)
    SetBossMusicState(2503802, state=False)
    SetBossMusicState(2503803, state=False)
    SetBossMusicState(-1, state=False)


def Event12504806():
    """ 12504806: Event 12504806 """
    EndIfFlagOn(12501800)
    IfHasTAEEvent(0, 2500800, tae_event_id=100)
    AICommand(2500800, command_id=1, slot=0)
    ReplanAI(2500800)
    StartPlayLogMeasurement(2501000, 116, overwrite=True)
    Move(2500801, destination=2500800, destination_type=CoordEntityType.Character, model_point=100, 
         copy_draw_parent=2500800)
    EnableCharacter(2500801)
    Wait(1.0)
    EnableAI(2500801)
    IfDamageType(-1, attacked_entity=2500801, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfTimeElapsed(-1, 60.0)
    IfCharacterDead(-1, 2500800)
    IfConditionTrue(0, input_condition=-1)
    AICommand(2500800, command_id=-1, slot=0)
    ReplanAI(2500800)
    StopPlayLogMeasurement(2501000)
    CreateTemporaryFX(623206, anchor_entity=2500801, anchor_type=CoordEntityType.Character, model_point=100)
    AddSpecialEffect(2500801, 5610, affect_npc_part_hp=False)
    DisableCharacter(2500801)
    DisableAI(2500801)
    Restart()


def Event12504807():
    """ 12504807: Event 12504807 """
    DisableNetworkSync()
    EndIfFlagOn(12501800)
    IfCharacterHasSpecialEffect(0, 2500800, 5633)
    ShootProjectile(owner_entity=2500802, projectile_id=2500800, model_point=6, behavior_id=223200590, 
                    launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)
    Wait(1.0)
    Restart()


def Event12504808():
    """ 12504808: Event 12504808 """
    EndIfFlagOn(12501800)
    IfCharacterHasSpecialEffect(1, 2500800, 5633)
    IfHasTAEEvent(1, 2500800, tae_event_id=10)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(2500800, 5633)
    CancelSpecialEffect(2500800, 5599)
    WaitFrames(1)
    ForceAnimation(2500800, 2100, wait_for_completion=True)
    Restart()


def Event12500896(arg_0_3: int):
    """ 12500896: Event 12500896 """
    GotoIfThisEventOff(Label.L0)
    DeleteFX(2503200, erase_root_only=False)
    DeleteFX(2503201, erase_root_only=False)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    DeleteFX(2503200, erase_root_only=True)
    DeleteFX(2503201, erase_root_only=True)
    WaitFrames(10)


def Event12500898(arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 12500898: Event 12500898 """
    IfFlagOn(-1, arg_0_3)
    IfFlagOn(-1, arg_4_7)
    IfFlagOn(-1, arg_8_11)
    IfFlagOn(-1, arg_12_15)
    IfConditionTrue(0, input_condition=-1)
    WaitFrames(10)
    EnableFlag(12500898)
    SkipLinesIfFlagOff(1, arg_0_3)
    CreatePlayLog(146)
    SkipLinesIfFlagOff(1, arg_4_7)
    CreatePlayLog(180)
    SkipLinesIfFlagOff(1, arg_8_11)
    CreatePlayLog(214)
    SkipLinesIfFlagOff(1, arg_12_15)
    CreatePlayLog(248)


def Event12500900(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12500900: Event 12500900 """
    GotoIfFlagOn(Label.L0, arg_4_7)
    DisableAI(arg_0_3)
    DisableAnimations(arg_0_3)
    AddSpecialEffect_WithUnknownEffect(arg_0_3, 5686, affect_npc_parts_hp=False)
    CancelSpecialEffect(arg_0_3, 5684)
    IfFlagOn(0, arg_4_7)
    WaitRandomFrames(min_frames=10, max_frames=70)
    EnableAI(arg_0_3)
    CancelSpecialEffect(arg_0_3, 5686)
    AddSpecialEffect(arg_0_3, 5684, affect_npc_part_hp=False)

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect_WithUnknownEffect(arg_0_3, 5685, affect_npc_parts_hp=False)
    DisableAnimations(arg_0_3)
    IfFlagOn(0, arg_8_11)
    CancelSpecialEffect(arg_0_3, 5685)
    EnableAnimations(arg_0_3)
    IfFlagOff(0, arg_8_11)
    Restart()


def Event12501000(arg_0_3: int):
    """ 12501000: Event 12501000 """
    IfCharacterHasSpecialEffect(0, PLAYER, 4652)
    SetAIParamID(arg_0_3, 215001)
    IfCharacterDoesNotHaveSpecialEffect(0, PLAYER, 4652)
    SetAIParamID(arg_0_3, 215001)
    Restart()


@RestartOnRest
def Event12505000(arg_0_3: int, arg_4_7: int):
    """ 12505000: Event 12505000 """
    DisableNetworkSync()
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Search)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_4_7)
    WaitFrames(3)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    DisableFlag(arg_4_7)
    Restart()


@RestartOnRest
def Event12505300(arg_0_3: int):
    """ 12505300: Event 12505300 """
    IfFlagOn(0, arg_0_3)
    EnableFlag(arg_0_3)
    IfFlagOff(0, arg_0_3)
    DisableFlag(arg_0_3)
    Restart()


def Event12500090():
    """ 12500090: Event 12500090 """
    EndIfThisEventOn()
    EndIfClient()
    IfStandingOnCollision(0, 2503500)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 282, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 282, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 282, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 282, PlayLogMultiplayerType.HostOnly)
    RunEvent(9350, slot=0, args=(2,))


def Event12507010(arg_0_3: int, arg_4_7: int):
    """ 12507010: Event 12507010 """
    IfFlagOn(0, arg_0_3)
    Move(PLAYER, destination=arg_4_7, destination_type=CoordEntityType.Object, model_point=200, short_move=True)
    ForceAnimation(PLAYER, 101160, skip_transition=True)
    Wait(4.0)
    DisableFlag(arg_0_3)


def Event12507020(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12507020: Event 12507020 """
    IfFlagOn(0, arg_0_3)
    DisableFlag(arg_0_3)
    WarpPlayerToRespawnPoint(arg_4_7)
    EnableFlag(arg_8_11)


def Event12507040():
    """ 12507040: Event 12507040 """
    SkipLinesIfFlagRangeAnyOn(1, (9001, 9010))
    End()
    EnableFlag(9210)
    IfFlagOff(0, 9210)
    SkipLinesIfFlagOff(3, 9001)
    EnableFlag(12507811)
    EnableFlag(12507810)
    SetRespawnPoint(2502950)
    SkipLinesIfFlagOff(3, 9002)
    EnableFlag(12507831)
    EnableFlag(12507830)
    SetRespawnPoint(2502951)
    SkipLinesIfFlagOff(3, 9003)
    EnableFlag(12507851)
    EnableFlag(12507850)
    SetRespawnPoint(2502952)
    SkipLinesIfFlagOff(3, 9004)
    EnableFlag(12507871)
    EnableFlag(12507870)
    SetRespawnPoint(2502953)
    SkipLinesIfFlagOff(3, 9005)
    EnableFlag(12507891)
    EnableFlag(12507890)
    SetRespawnPoint(2502954)
    SkipLinesIfFlagOff(3, 9006)
    EnableFlag(12507911)
    EnableFlag(12507910)
    SetRespawnPoint(2502955)
    SkipLinesIfFlagOff(3, 9007)
    EnableFlag(12507931)
    EnableFlag(12507930)
    SetRespawnPoint(2502956)
    SkipLinesIfFlagOff(3, 9008)
    EnableFlag(12507951)
    EnableFlag(12507950)
    SetRespawnPoint(2502957)
    SkipLinesIfFlagOff(3, 9009)
    EnableFlag(12507971)
    EnableFlag(12507970)
    SetRespawnPoint(2502958)
    SkipLinesIfFlagOff(3, 9010)
    EnableFlag(12507991)
    EnableFlag(12507990)
    SetRespawnPoint(2502959)
    DisableFlagRange((9000, 9010))


def Event12507050(arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 12507050: Event 12507050 """
    EndIfFlagOn(arg_0_3)
    DisableGravity(arg_4_7)
    IfCharacterBackreadEnabled(0, arg_4_7)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    ForceAnimation(arg_4_7, 101165, loop=True)
    Wait(1.0)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Object, model_point=250, short_move=True)
    IfFlagOn(0, arg_0_3)
    ForceAnimation(arg_4_7, 101166, wait_for_completion=True)
    DisableCharacter(arg_4_7)
