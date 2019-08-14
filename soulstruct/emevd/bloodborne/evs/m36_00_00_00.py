"""
linked:
76

strings:
0: ボス_撃破
12: PC情報_ボス撃破_ラスボス
42: ボス_戦闘開始
58: ボス戦_撃破時間
76: N:\\SPRJ\\data\\Param\\event\\common.emevd
152: 
154: 
156: 
158: 
"""
from soulstruct.emevd.bloodborne import *


@NeverRestart
def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=65, args=(3600950, 3601950, 999, 13607800))
    RunEvent(7000, slot=66, args=(3600951, 3601951, 999, 13607820))
    RunEvent(7000, slot=67, args=(3600952, 3601952, 13601800, 13607840))
    RunEvent(7100, slot=65, args=(73600200, 3601950))
    RunEvent(7100, slot=66, args=(73600201, 3601951))
    RunEvent(7100, slot=67, args=(73600202, 3601952))
    RunEvent(7200, slot=65, args=(73600100, 3601950, 2102953))
    RunEvent(7200, slot=66, args=(73600101, 3601951, 2102953))
    RunEvent(7200, slot=67, args=(73600102, 3601952, 2102953))
    RunEvent(7300, slot=65, args=(72103600, 3601950))
    RunEvent(7300, slot=66, args=(72103601, 3601951))
    RunEvent(7300, slot=67, args=(72103602, 3601952))
    RunEvent(13604700, slot=0, args=(3600790, 13604701, 13604711, 3600, 999))
    RunEvent(13604700, slot=5, args=(3600791, 13604702, 13604712, 3600, 999))
    RunEvent(13604710, slot=0, args=(3600790, 13604701, 13604711, 13604721))
    RunEvent(13604710, slot=5, args=(3600791, 13604702, 13604712, 13604722))
    RunEvent(13604720, slot=0, args=(3600790, 13604701, 13604711, 13604721))
    RunEvent(13604720, slot=5, args=(3600791, 13604702, 13604712, 13604722))
    RunEvent(13604730, slot=0, args=(3600790, 13604701, 13604711, 3600, 13604810, 999, 999, 13604712))
    RunEvent(13604730, slot=5, args=(3600791, 13604702, 13604712, 3600, 13604810, 999, 999, 13604711))
    RunEvent(13604740)
    RunEvent(13604742)
    RunEvent(13600000)
    RunEvent(13600010)
    RunEvent(13601090)
    RunEvent(13601100)
    RunEvent(13601101)
    RunEvent(13601102)
    RunEvent(13601103)
    RunEvent(13601104)
    RunEvent(13601105)
    RunEvent(13601200, slot=0, args=(3601200, 13604200, 1, 10))
    RunEvent(13601200, slot=1, args=(3601201, 13604201, 1, 10))
    RunEvent(13601210, slot=0, args=(7030, 3601200, 13601200))
    RunEvent(13601210, slot=1, args=(7030, 3601201, 13601201))
    RegisterLadder(start_climbing_flag=13601300, stop_climbing_flag=13601301, obj=3601300)
    RegisterLadder(start_climbing_flag=13601302, stop_climbing_flag=13601303, obj=3601301)
    RegisterLadder(start_climbing_flag=13601304, stop_climbing_flag=13601305, obj=3601302)
    RegisterLadder(start_climbing_flag=13601306, stop_climbing_flag=13601307, obj=3601303)
    RegisterLadder(start_climbing_flag=13601308, stop_climbing_flag=13601309, obj=3601304)
    RunEvent(13601312)
    RunEvent(13601140, slot=0, args=(3601110, 3604110))
    RunEvent(13601140, slot=1, args=(3601111, 3604111))
    RunEvent(13601140, slot=2, args=(3601112, 3604112))
    RunEvent(13601140, slot=3, args=(3601113, 3604113))
    RunEvent(13601400)
    RunEvent(13604400, slot=0, args=(3601400,))
    RunEvent(13604400, slot=1, args=(3601401,))
    RunEvent(13604400, slot=2, args=(3601402,))
    RunEvent(13604400, slot=3, args=(3601403,))
    RunEvent(13604400, slot=4, args=(3601404,))
    RunEvent(13604400, slot=5, args=(3601405,))
    RunEvent(13604400, slot=6, args=(3601406,))
    RunEvent(13604400, slot=7, args=(3601407,))
    RunEvent(13604400, slot=8, args=(3601408,))
    RunEvent(13604400, slot=9, args=(3601409,))
    RunEvent(13604400, slot=10, args=(3601410,))
    RunEvent(13604400, slot=11, args=(3601411,))
    RunEvent(13604400, slot=12, args=(3601412,))
    RunEvent(13604400, slot=13, args=(3601413,))
    RunEvent(13604400, slot=20, args=(3601420,))
    RunEvent(13604400, slot=21, args=(3601421,))
    RunEvent(13604400, slot=22, args=(3601422,))
    RunEvent(13604400, slot=23, args=(3601423,))
    RunEvent(13604400, slot=24, args=(3601424,))
    RunEvent(13604400, slot=25, args=(3601425,))
    RunEvent(13604400, slot=26, args=(3601426,))
    RunEvent(13604400, slot=27, args=(3601427,))
    RunEvent(13604400, slot=28, args=(3601428,))
    RunEvent(13604400, slot=29, args=(3601429,))
    RunEvent(13604400, slot=30, args=(3601430,))
    RunEvent(13604400, slot=31, args=(3601431,))
    RunEvent(13604400, slot=40, args=(3601440,))
    RunEvent(13604400, slot=41, args=(3601441,))
    RunEvent(13604400, slot=42, args=(3601442,))
    RunEvent(13604400, slot=43, args=(3601443,))
    RunEvent(13604400, slot=44, args=(3601444,))
    RunEvent(13604400, slot=45, args=(3601445,))
    RunEvent(13604400, slot=46, args=(3601446,))
    RunEvent(13604400, slot=47, args=(3601447,))
    RunEvent(13604400, slot=50, args=(3601450,))
    RunEvent(13604400, slot=51, args=(3601451,))
    RunEvent(13604400, slot=52, args=(3601452,))
    RunEvent(13604400, slot=53, args=(3601453,))
    RunEvent(13604400, slot=54, args=(3601454,))
    RunEvent(13604400, slot=55, args=(3601455,))
    RunEvent(13604400, slot=56, args=(3601456,))
    RunEvent(13604400, slot=57, args=(3601457,))
    RunEvent(13604400, slot=60, args=(3601460,))
    RunEvent(13604400, slot=61, args=(3601461,))
    RunEvent(13604400, slot=62, args=(3601462,))
    RunEvent(13604400, slot=63, args=(3601463,))
    RunEvent(13604400, slot=64, args=(3601464,))
    RunEvent(13604400, slot=65, args=(3601465,))
    RunEvent(13604400, slot=66, args=(3601466,))
    RunEvent(13604400, slot=67, args=(3601467,))
    RunEvent(13601800)
    RunEvent(13604811)
    RunEvent(13601801)
    RunEvent(13604800)
    RunEvent(13604801)
    RunEvent(13604802)
    RunEvent(13604803)
    RunEvent(13604805)
    RunEvent(13604806)
    RunEvent(13604807)
    RunEvent(13604820)
    RunEvent(13604830)
    RunEvent(13604840)
    RunEvent(13604850)
    RunEvent(13601802)
    RunEvent(13601803)
    RunEvent(13601804)
    RunEvent(13605200, slot=0, args=(3600200, 3602200, 0, 3603200, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=1, args=(3600202, 3602202, 0, 3603202, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=2, args=(3600203, 3602202, 3602203, 3603203, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=3, args=(3600204, 3602202, 3602203, 3603204, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=4, args=(3600208, 3602208, 0, 3603208, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=5, args=(3600209, 3602208, 0, 3603209, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=6, args=(3600210, 3602210, 0, 3603210, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=7, args=(3600300, 3602300, 0, 3603300, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=8, args=(3600213, 3602213, 0, 3603213, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=9, args=(3600214, 3602213, 0, 3603214, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=10, args=(3600217, 3602215, 0, 3603217, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=11, args=(3600229, 3602229, 0, 3603229, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=12, args=(3600231, 3602231, 3602232, 3603231, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=13, args=(3600232, 3602231, 3602232, 3603232, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=14, args=(3600233, 3602231, 3602232, 3603233, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=15, args=(3600610, 3602610, 0, 3603610, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=16, args=(3600611, 3602231, 3602232, 3603611, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=17, args=(3600301, 3602301, 0, 3603301, 0.0, 1), arg_types='iiiifi')
    RunEvent(13605200, slot=18, args=(3600310, 3602310, 0, 3603310, 0.0, 1), arg_types='iiiifi')
    RunEvent(13605200, slot=19, args=(3600700, 3602700, 0, 3603700, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=20, args=(3600710, 3602710, 0, 3603710, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=21, args=(3600251, 3602251, 0, 3603251, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=23, args=(3600253, 3602252, 0, 3603253, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=25, args=(3600314, 3602314, 0, 3603314, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=26, args=(3600455, 3602455, 0, 3603455, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=27, args=(3600456, 3602455, 0, 3603456, 1.0, 1), arg_types='iiiifi')
    RunEvent(13605200, slot=28, args=(3600474, 3602474, 0, 3603474, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=29, args=(3600475, 3602474, 0, 3603475, 1.0, 1), arg_types='iiiifi')
    RunEvent(13605200, slot=30, args=(3600302, 3602302, 0, 3603302, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=31, args=(3600312, 3602312, 0, 3603312, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=32, args=(3600470, 3602470, 0, 3603470, 0.0, 1), arg_types='iiiifi')
    RunEvent(13605200, slot=33, args=(3600500, 3602470, 0, 3603500, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=34, args=(3600501, 3602501, 0, 3603501, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605200, slot=35, args=(3600920, 3602940, 0, 3603920, 0.0, 0), arg_types='iiiifi')
    RunEvent(13605400, slot=0, args=(3600206, 7004, 404002, 7005, 404002, 3602206, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=1, args=(3600211, 7012, 404000, 7013, 404000, 3602211, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=2, args=(3600218, 0, 404011, 3005, 404010, 3602218, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=3, args=(3600222, 7016, 404031, 7017, 404030, 3602222, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=4, args=(3600230, 7004, 404000, 7005, 404000, 3602230, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=5, args=(3600239, 7012, 404008, 7013, 404008, 3602240, 0.75, 0.75), arg_types='iiiiiiff')
    RunEvent(13605400, slot=6, args=(3600240, 7012, 404004, 7013, 404004, 3602240, 0.25, 0.25), arg_types='iiiiiiff')
    RunEvent(13605400, slot=7, args=(3600241, 7012, 404008, 7013, 404008, 3602240, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=8, args=(3600242, 7012, 404004, 7013, 404004, 3602240, 0.5, 0.5), arg_types='iiiiiiff')
    RunEvent(13605400, slot=9, args=(3600244, 7014, 404014, 7015, 404014, 3602244, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=10, args=(3600245, 0, 404035, 3026, 404034, 3602245, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=11, args=(3600246, 7018, 404034, 7019, 404034, 3602246, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=12, args=(3600247, 7018, 404014, 7019, 404014, 3602246, 0.5, 0.5), arg_types='iiiiiiff')
    RunEvent(13605400, slot=13, args=(3600260, 7012, 404018, 7013, 404019, 3602260, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=14, args=(3600261, 7012, 404018, 7013, 404019, 3602261, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=15, args=(3600262, 7012, 404018, 7013, 404019, 3602262, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=16, args=(3600265, 7012, 404018, 7013, 404019, 3602265, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=17, args=(3600400, 7010, 407022, 3001, 407020, 3602400, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=18, args=(3600401, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=19, args=(3600402, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=20, args=(3600403, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=21, args=(3600404, 7010, 407022, 3001, 407020, 3602400, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=22, args=(3600405, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=25, args=(3600408, 7010, 407022, 3001, 407020, 3602408, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=26, args=(3600409, 7010, 407012, 7001, 407010, 3602408, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=27, args=(3600410, 7010, 407022, 3001, 407020, 3602408, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=28, args=(3600411, 7010, 407012, 7001, 407010, 3602408, 0.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=29, args=(3600412, 7010, 407012, 7001, 407010, 3602412, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=30, args=(3600413, 7010, 407012, 7001, 407010, 3602412, 1.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=33, args=(3600416, 7010, 407022, 3001, 407020, 3602416, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=34, args=(3600417, 7010, 407012, 7001, 407010, 3602416, 1.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=35, args=(3600418, 7010, 407012, 7001, 407010, 3602416, 0.5, 0.5), arg_types='iiiiiiff')
    RunEvent(13605400, slot=36, args=(3600419, 7010, 407012, 7001, 407010, 3602419, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=37, args=(3600424, 7010, 407022, 3001, 407020, 3602424, 0.5, 0.5), arg_types='iiiiiiff')
    RunEvent(13605400, slot=38, args=(3600425, 7010, 407012, 7001, 407010, 3602424, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=39, args=(3600426, 7010, 407012, 7001, 407010, 3602424, 1.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=40, args=(3600440, 7010, 407022, 7001, 407020, 3602440, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605400, slot=41, args=(3600441, 7010, 407022, 3001, 407020, 3602440, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605480, slot=0, args=(3600223, 7008, 404032, 7009, 404030, 3602223, 0.0, 33), arg_types='iiiiiifi')
    RunEvent(13605480, slot=1, args=(3600476, 7012, 407000, 7013, 407000, 3602476, 0.0, 30), arg_types='iiiiiifi')
    RunEvent(13605480, slot=2, args=(3600477, 7014, 407000, 7015, 407000, 3602476, 0.5, 30), arg_types='iiiiiifi')
    RunEvent(13605480, slot=3, args=(3600478, 7016, 407000, 7017, 407000, 3602478, 0.0, 30), arg_types='iiiiiifi')
    RunEvent(13605490, slot=0, args=(3600313, 9000, 405003, 9060, 405003, 3600314, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605490, slot=1, args=(3600266, 7012, 404018, 7013, 404019, 3600314, 0.5, 0.5), arg_types='iiiiiiff')
    RunEvent(13605490, slot=2, args=(3600267, 7014, 404018, 7015, 404019, 3600314, 1.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605490, slot=3, args=(3600263, 7012, 404018, 7013, 404019, 3600265, 0.5, 0.5), arg_types='iiiiiiff')
    RunEvent(13605490, slot=4, args=(3600264, 7012, 404018, 7013, 404019, 3600265, 1.0, 1.0), arg_types='iiiiiiff')
    RunEvent(13605500, slot=1, args=(3600207, 7006, 404002, 7007, 404002, 3602206, 4.0, 4.0), arg_types='iiiiiiff')
    RunEvent(13605500, slot=2, args=(3600212, 7006, 404016, 7007, 404010, 3602211, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605500, slot=3, args=(3600216, 7006, 404003, 7007, 404000, 3602215, 0.0, 0.0), arg_types='iiiiiiff')
    RunEvent(13605520, slot=1, args=(3600310, 3602310, 405001, 405000))
    RunEvent(13605540, slot=0, args=(3600210, 0, 8.0, 404040, 404000), arg_types='iifii')
    RunEvent(13605540, slot=1, args=(3600300, 0, 8.0, 406001, 406000), arg_types='iifii')
    RunEvent(13605540, slot=2, args=(3600500, 3602470, 4.0, 256901, 256900), arg_types='iifii')
    RunEvent(13605540, slot=3, args=(3600501, 3602470, 4.0, 256901, 256900), arg_types='iifii')
    RunEvent(13605540, slot=4, args=(3600218, 0, 1.0, 404011, 404010), arg_types='iifii')
    RunEvent(13605540, slot=5, args=(3600220, 0, 4.0, 404011, 404010), arg_types='iifii')
    RunEvent(13605540, slot=6, args=(3600221, 0, 4.0, 404011, 404010), arg_types='iifii')
    RunEvent(13605560, slot=0, args=(3600331, 3602331, 4.0), arg_types='iif')
    RunEvent(13605600, slot=0, args=(3600500, 3600510))
    RunEvent(13605600, slot=1, args=(3600501, 3600511))
    RunEvent(13605605)
    RunEvent(13605606)
    RunEvent(13605799)
    RunEvent(13605720, slot=0, args=(3600206,))
    RunEvent(13605720, slot=1, args=(3600314,))
    RunEvent(13605740, slot=0, args=(3600215, 3602215, 3600720, 2.0), arg_types='iiif')
    RunEvent(13605740, slot=1, args=(3600219, 3602218, 3600721, 2.0), arg_types='iiif')
    RunEvent(13605740, slot=2, args=(3600250, 3602250, 3600722, 2.0), arg_types='iiif')
    RunEvent(13605750)
    RunEvent(13605751)
    RunEvent(13605752)
    RunEvent(13605760)
    RunEvent(13605761)
    RunEvent(13605900, slot=0, args=(13605950, 13605960, 13605970, 3602900, 0, 13600995))
    RunEvent(13605900, slot=1, args=(13605951, 13605961, 13605971, 3602910, 3602911, 6001))
    RunEvent(13605900, slot=2, args=(13605952, 13605962, 13605972, 3602920, 0, 6001))
    RunEvent(13605910, slot=0, args=(13605950, 13605960, 13605970, 3602902, 0))
    RunEvent(13605910, slot=1, args=(13605951, 13605961, 13605971, 3602912, 3602913))
    RunEvent(13605910, slot=2, args=(13605952, 13605962, 13605972, 3602922, 0))
    RunEvent(13605920, slot=0, args=(3600900, 13605960, 13605970, 3602904, 3602905, 13605950, 13605980, 3602906))
    RunEvent(13605921, slot=0, args=(3600901, 13605961, 13605971, 3602914, 3602915, 13605951, 13605981, 3602916))
    RunEvent(13605920, slot=2, args=(3600902, 13605962, 13605972, 3602924, 0, 13605952, 13605982, 3602926))
    RunEvent(13605930, slot=0, args=(3600900, 13605960, 13605970, 3602908, 3602909, 13605980))
    RunEvent(13605930, slot=1, args=(3600901, 13605961, 13605971, 3602918, 3602909, 13605981))
    RunEvent(13605930, slot=2, args=(3600902, 13605962, 13605972, 3602928, 0, 13605982))
    RunEvent(13605940, slot=0, args=(3600900, 13605960, 13605970, 43730, 3600910))
    RunEvent(13605940, slot=1, args=(3600901, 13605961, 13605971, 43740, 3600911))
    RunEvent(13605940, slot=2, args=(3600902, 13605962, 13605972, 43720, 3600912))
    RunEvent(13600995)
    RunEvent(13600942, slot=0, args=(6.0, 10.0), arg_types='ff')
    RunEvent(13600943, slot=0, args=(73600300, 43600))
    RunEvent(13600944)
    RunEvent(13600951, slot=0, args=(3600905, 73600520, 1723))
    RunEvent(13600952, slot=0, args=(3600905, 1723, 73600530))
    RunEvent(13600953, slot=0, args=(3600905,))
    RunEvent(13600955)
    RunEvent(13600956, slot=0, args=(3600905, 1723, 73600521))
    RunEvent(13600900, slot=1, args=(3600905, 1710, 1729, 1719, 1713))
    RunEvent(13600954, slot=0, args=(1713, 73600530, 43220))


@NeverRestart
def Preconstructor():
    """ 50: Event 50 """
    RunEvent(13600940, slot=0, args=(3600920,))
    RunEvent(13600950, slot=0, args=(3600905,))
    DisableGravity(3600201)
    DisableCollision(3600201)
    DisableGravity(3600207)
    DisableCollision(3600207)
    DisableGravity(3600212)
    DisableCollision(3600212)
    DisableGravity(3600216)
    DisableCollision(3600216)
    DisableHealthBar(3600330)
    DisableHealthBar(3600331)
    DisableHealthBar(3600332)


@RestartOnRest
def Event13604700(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 13604700: Event 13604700 """
    GotoIfFlagOff(Label.L0, ARG_8_11)
    DisableAI(ARG_0_3)
    ForceAnimation(ARG_0_3, 7010)
    End()
    Label(0)
    EndIfFlagOn(ARG_4_7)
    DisableAI(ARG_0_3)
    ForceAnimation(ARG_0_3, 7010, loop=True)
    IfOnline(1)
    IfFlagOff(1, ARG_8_11)
    IfFlagOff(1, ARG_12_15)
    IfInsideMap(1, game_map=FISHING_HAMLET)
    IfCharacterHuman(2, PLAYER)
    IfPlayerSoulLevelGreaterThanOrEqual(2, 30)
    SkipLinesIfFlagOff(1, ARG_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    SkipLinesIfFlagOff(1, ARG_16_19)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(ARG_0_3, 7011)
    WaitFrames(59)
    EnableAI(ARG_0_3)
    EnableFlag(ARG_4_7)


@RestartOnRest
def Event13604710(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 13604710: Event 13604710 """
    EndIfFlagOn(ARG_8_11)
    IfFlagOn(1, ARG_4_7)
    IfFlagOff(1, ARG_12_15)
    IfFlagOff(1, ARG_8_11)
    IfInsideMap(1, game_map=FISHING_HAMLET)
    IfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, value=0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    IfRandomTimeElapsed(2, min_seconds=10.0, max_seconds=10.0)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(PLAYER, 9020, affect_npc_part_hp=False)
    AddSpecialEffect(ARG_0_3, 9100, affect_npc_part_hp=False)
    ReplanAI(ARG_0_3)
    EnableFlag(ARG_12_15)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    Restart()


@RestartOnRest
def Event13604720(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 13604720: Event 13604720 """
    EndIfFlagOn(ARG_8_11)
    IfFlagOn(1, ARG_4_7)
    IfFlagOn(1, ARG_12_15)
    IfFlagOn(-1, ARG_8_11)
    IfClientTypeCountComparison(-1, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfOutsideMap(-1, game_map=FISHING_HAMLET)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    CancelSpecialEffect(PLAYER, 9020)
    CancelSpecialEffect(ARG_0_3, 9100)
    ReplanAI(ARG_0_3)
    DisableFlag(ARG_12_15)
    Restart()


@RestartOnRest
def Event13604730(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 13604730: Event 13604730 """
    IfFlagOn(-15, ARG_8_11)
    IfFlagOn(-15, ARG_12_15)
    IfFlagOn(-15, ARG_16_19)
    EndIfConditionTrue(-15)
    IfFlagOn(1, ARG_4_7)
    IfFlagOn(1, ARG_24_27)
    IfHealthEqual(2, ARG_0_3, 0.0)
    IfFlagOn(-2, ARG_16_19)
    IfFlagOn(-2, ARG_28_31)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=-2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(ARG_8_11)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-2)
    EnableFlag(ARG_20_23)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()
    Label(0)
    DisableAI(ARG_0_3)
    ForceAnimation(ARG_0_3, 7012)
    WaitFrames(88)
    ForceAnimation(ARG_0_3, 7010)


@RestartOnRest
def Event13604740():
    """ 13604740: Event 13604740 """
    IfCharacterHuman(1, PLAYER)
    IfStandingOnHitbox(-1, 3604000)
    IfStandingOnHitbox(-1, 3604001)
    IfStandingOnHitbox(-1, 3604002)
    IfStandingOnHitbox(-1, 3604003)
    IfStandingOnHitbox(-1, 3604004)
    IfStandingOnHitbox(-1, 3604005)
    IfStandingOnHitbox(-1, 3604006)
    IfStandingOnHitbox(-1, 3604007)
    IfStandingOnHitbox(-1, 3604008)
    IfStandingOnHitbox(-1, 3604009)
    IfStandingOnHitbox(-1, 3604010)
    IfStandingOnHitbox(-1, 3604011)
    IfStandingOnHitbox(-1, 3604012)
    IfStandingOnHitbox(-1, 3604013)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604741)
    IfCharacterHuman(2, PLAYER)
    IfStandingOnHitbox(-2, 3604000)
    IfStandingOnHitbox(-2, 3604001)
    IfStandingOnHitbox(-2, 3604002)
    IfStandingOnHitbox(-2, 3604003)
    IfStandingOnHitbox(-2, 3604004)
    IfStandingOnHitbox(-2, 3604005)
    IfStandingOnHitbox(-2, 3604006)
    IfStandingOnHitbox(-2, 3604007)
    IfStandingOnHitbox(-2, 3604008)
    IfStandingOnHitbox(-2, 3604009)
    IfStandingOnHitbox(-2, 3604010)
    IfStandingOnHitbox(-2, 3604011)
    IfStandingOnHitbox(-2, 3604012)
    IfStandingOnHitbox(-2, 3604013)
    IfConditionFalse(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13604741)
    Restart()


@RestartOnRest
def Event13604742():
    """ 13604742: Event 13604742 """
    IfCharacterHuman(1, PLAYER)
    IfStandingOnHitbox(-1, 3604020)
    IfStandingOnHitbox(-1, 3604021)
    IfStandingOnHitbox(-1, 3604022)
    IfStandingOnHitbox(-1, 3604023)
    IfStandingOnHitbox(-1, 3604024)
    IfStandingOnHitbox(-1, 3604025)
    IfStandingOnHitbox(-1, 3604026)
    IfStandingOnHitbox(-1, 3604027)
    IfStandingOnHitbox(-1, 3604028)
    IfStandingOnHitbox(-1, 3604029)
    IfStandingOnHitbox(-1, 3604030)
    IfStandingOnHitbox(-1, 3604031)
    IfStandingOnHitbox(-1, 3604032)
    IfStandingOnHitbox(-1, 3604033)
    IfStandingOnHitbox(-1, 3604034)
    IfStandingOnHitbox(-1, 3604035)
    IfStandingOnHitbox(-1, 3604110)
    IfStandingOnHitbox(-1, 3604111)
    IfStandingOnHitbox(-1, 3604112)
    IfStandingOnHitbox(-1, 3604113)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604743)
    IfCharacterHuman(2, PLAYER)
    IfStandingOnHitbox(-2, 3604020)
    IfStandingOnHitbox(-2, 3604021)
    IfStandingOnHitbox(-2, 3604022)
    IfStandingOnHitbox(-2, 3604023)
    IfStandingOnHitbox(-2, 3604024)
    IfStandingOnHitbox(-2, 3604025)
    IfStandingOnHitbox(-2, 3604026)
    IfStandingOnHitbox(-2, 3604027)
    IfStandingOnHitbox(-2, 3604028)
    IfStandingOnHitbox(-2, 3604029)
    IfStandingOnHitbox(-2, 3604030)
    IfStandingOnHitbox(-2, 3604031)
    IfStandingOnHitbox(-2, 3604032)
    IfStandingOnHitbox(-2, 3604033)
    IfStandingOnHitbox(-2, 3604034)
    IfStandingOnHitbox(-2, 3604035)
    IfStandingOnHitbox(-2, 3604110)
    IfStandingOnHitbox(-2, 3604111)
    IfStandingOnHitbox(-2, 3604112)
    IfStandingOnHitbox(-2, 3604113)
    IfConditionFalse(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13604743)
    Restart()


@NeverRestart
def Event13600000():
    """ 13600000: Event 13600000 """
    EndIfThisEventOn()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfStandingOnHitbox(0, 3604002)
    RunEvent(9350, slot=0, args=(4,))


@NeverRestart
def Event13600010():
    """ 13600010: Event 13600010 """
    DisableNetworkSync()
    EndIfFlagOn(13601803)
    DisableMapSound(3603001)
    IfStandingOnHitbox(-1, 3604005)
    IfStandingOnHitbox(-1, 3604007)
    IfStandingOnHitbox(-1, 3604012)
    IfStandingOnHitbox(-1, 3604021)
    IfStandingOnHitbox(-1, 3604023)
    IfStandingOnHitbox(-1, 3604026)
    IfStandingOnHitbox(-1, 3604027)
    IfStandingOnHitbox(-1, 3604028)
    IfStandingOnHitbox(-1, 3604029)
    IfStandingOnHitbox(-1, 3604030)
    IfStandingOnHitbox(-1, 3604031)
    IfStandingOnHitbox(-1, 3604032)
    IfStandingOnHitbox(-1, 3604033)
    IfStandingOnHitbox(-1, 3604034)
    IfStandingOnHitbox(-1, 3604035)
    IfStandingOnHitbox(-1, 3604060)
    IfConditionTrue(0, input_condition=-1)
    EnableMapSound(3603001)
    IfStandingOnHitbox(-2, 3604005)
    IfStandingOnHitbox(-2, 3604007)
    IfStandingOnHitbox(-2, 3604012)
    IfStandingOnHitbox(-2, 3604021)
    IfStandingOnHitbox(-2, 3604023)
    IfStandingOnHitbox(-2, 3604026)
    IfStandingOnHitbox(-2, 3604027)
    IfStandingOnHitbox(-2, 3604028)
    IfStandingOnHitbox(-2, 3604029)
    IfStandingOnHitbox(-2, 3604030)
    IfStandingOnHitbox(-2, 3604031)
    IfStandingOnHitbox(-2, 3604032)
    IfStandingOnHitbox(-2, 3604033)
    IfStandingOnHitbox(-2, 3604034)
    IfStandingOnHitbox(-2, 3604035)
    IfStandingOnHitbox(-2, 3604060)
    IfConditionFalse(0, input_condition=-2)
    Restart()


@NeverRestart
def Event13601090():
    """ 13601090: Event 13601090 """
    EndIfFlagOn(9468)
    DisableObject(3601090)
    IfFlagOn(0, 9468)
    EnableObject(3601090)


@NeverRestart
def Event13601100():
    """ 13601100: Event 13601100 """
    EndIfFlagOn(13604100)
    GotoIfFlagOn(Label.L0, 13601108)
    EnableFlag(13601106)
    EnableFlag(13601107)
    EndOfAnimation(3601100, 0)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    Goto(Label.L2)
    Label(0)
    IfFlagOn(1, 13601106)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(13601107)
    EndOfAnimation(3601100, 4)
    EnableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    End()
    Label(1)
    EnableFlag(13601107)
    EndOfAnimation(3601100, 0)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)


@NeverRestart
def Event13601101():
    """ 13601101: Event 13601101 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 13601108)
    IfFlagOn(1, 13604100)
    IfConditionTrue(0, input_condition=1)
    IfFlagOn(2, 13601106)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(13601107)
    SkipLines(1)
    EnableFlag(13601107)
    IfCharacterHuman(3, PLAYER)
    IfFlagOn(3, 13601108)
    IfFlagOff(3, 13604100)
    IfConditionTrue(0, input_condition=3)
    Restart()


@NeverRestart
def Event13601102():
    """ 13601102: Event 13601102 """
    IfFlagOn(3, 13604100)
    IfFlagOn(3, 13601106)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    EndOfAnimation(3601100, 6)
    Goto(Label.L1)
    Label(0)
    IfFlagOn(1, 13601108)
    IfFlagOff(1, 13604100)
    IfFlagOff(1, 13601106)
    IfCharacterInsideRegion(-1, PLAYER, region=3602102)
    IfObjectActivated(-1, obj_act_id=13604101)
    IfFlagChange(2, 13601107)
    IfFlagOn(2, 13601107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604100)
    EnableFlag(13601106)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    ForceAnimation(3601100, 5, wait_for_completion=True)
    ForceAnimation(3601100, 6, wait_for_completion=True)
    Label(1)
    IfAllPlayersOutsideRegion(0, region=3602101)
    ForceAnimation(3601100, 7, wait_for_completion=True)
    DisableFlag(13604100)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)
    Restart()


@NeverRestart
def Event13601103():
    """ 13601103: Event 13601103 """
    IfFlagOn(3, 13604100)
    IfFlagOff(3, 13601106)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    EndOfAnimation(3601100, 2)
    Goto(Label.L1)
    Label(0)
    IfFlagOn(1, 13601108)
    IfFlagOff(1, 13604100)
    IfFlagOn(1, 13601106)
    IfCharacterInsideRegion(-1, PLAYER, region=3602101)
    IfObjectActivated(-1, obj_act_id=13604102)
    IfFlagChange(2, 13601107)
    IfFlagOff(2, 13601107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604100)
    DisableFlag(13601106)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    ForceAnimation(3601100, 1, wait_for_completion=True)
    ForceAnimation(3601100, 2, wait_for_completion=True)
    Label(1)
    IfAllPlayersOutsideRegion(0, region=3602102)
    WaitFrames(1)
    ForceAnimation(3601100, 3, wait_for_completion=True)
    DisableFlag(13604100)
    EnableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    Restart()


@NeverRestart
def Event13601104():
    """ 13601104: Event 13601104 """
    DisableNetworkSync()
    IfFlagOff(1, 13601108)
    IfActionButtonInRegion(1, action_button_id=7100, region=3601101)
    IfFlagOff(2, 13601108)
    IfActionButtonInRegion(2, action_button_id=7100, region=3601102)
    IfFlagOn(3, 13604100)
    IfActionButtonInRegion(3, action_button_id=7100, region=3601101)
    IfFlagOn(4, 13604100)
    IfActionButtonInRegion(4, action_button_id=7100, region=3601102)
    IfFlagOn(5, 13601106)
    IfActionButtonInRegion(5, action_button_id=7100, region=3601101)
    IfFlagOff(6, 13601106)
    IfActionButtonInRegion(6, action_button_id=7100, region=3601102)
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
def Event13601105():
    """ 13601105: Event 13601105 """
    EndIfFlagOn(13601108)
    IfCharacterInsideRegion(0, PLAYER, region=3602100)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)
    EnableFlag(13601108)


@NeverRestart
def Event13601140(ARG_0_3: int, ARG_4_7: int):
    """ 13601140: Event 13601140 """
    IfMovingOnHitbox(0, ARG_4_7)
    ForceAnimation(ARG_0_3, 0, wait_for_completion=True)
    Restart()


@NeverRestart
def Event13601200(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 13601200: Event 13601200 """
    GotoIfThisEventSlotOff(Label.L0)
    EndOfAnimation(ARG_0_3, ARG_8_11)
    DisableObjectActivation(ARG_0_3, obj_act_id=ARG_12_15)
    End()
    Label(0)
    IfObjectActivated(0, obj_act_id=ARG_4_7)
    Wait(0.0)


@NeverRestart
def Event13601312():
    """ 13601312: Event 13601312 """
    GotoIfThisEventOff(Label.L0)
    EndOfAnimation(3601305, 1)
    WaitFrames(1)
    RegisterLadder(start_climbing_flag=13601310, stop_climbing_flag=13601311, obj=3601305)
    End()
    Label(0)
    IfActionButtonInRegion(0, action_button_id=3600000, region=3601305)
    Move(PLAYER, destination=3601305, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 101330)
    ForceAnimation(3601305, 1, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=13601310, stop_climbing_flag=13601311, obj=3601305)


@NeverRestart
def Event13601210(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 13601210: Event 13601210 """
    DisableNetworkSync()
    EndIfFlagOn(ARG_8_11)
    IfActionButtonInRegion(1, action_button_id=ARG_0_3, region=ARG_4_7)
    IfFlagOn(2, ARG_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    DisplayDialog(10010161, anchor_entity=-1, display_distance=3.0, button_type=ButtonType.OK_or_Cancel, number_buttons=NumberButtons.OneButton)
    Restart()


@NeverRestart
def Event13601400():
    """ 13601400: Event 13601400 """
    DisableNetworkSync()
    IfInsideMap(0, game_map=FISHING_HAMLET)
    DeleteFX(3503120, erase_root_only=True)


@RestartOnRest
def Event13604400(ARG_0_3: int):
    """ 13604400: Event 13604400 """
    EndIfThisEventSlotOn()
    RestoreObject(ARG_0_3)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Fire)
    IfDamageType(-1, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.NoType)
    IfConditionTrue(1, input_condition=-1)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Magic)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Lightning)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Blunt)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Slash)
    IfDamageType(-2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Thrust)
    IfConditionTrue(2, input_condition=-2)
    IfObjectHealthValueComparison(2, ARG_0_3, ComparisonType.LessThanOrEqual, 999)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=1)
    ShootProjectile(owner_entity=3600799, projectile_id=ARG_0_3, model_point=-1, behavior_id=6310, launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)
    DestroyObject(ARG_0_3, slot=1)
    PlaySoundEffect(anchor_entity=ARG_0_3, sound_type=SoundType.o_Object, sound_id=299961000)
    End()
    Label(0)
    ShootProjectile(owner_entity=3600799, projectile_id=ARG_0_3, model_point=-1, behavior_id=6310, launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)
    ShootProjectile(owner_entity=3600799, projectile_id=ARG_0_3, model_point=-1, behavior_id=6320, launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)
    DestroyObject(ARG_0_3, slot=1)
    PlaySoundEffect(anchor_entity=ARG_0_3, sound_type=SoundType.o_Object, sound_id=299961000)


@NeverRestart
def Event13601800():
    """ 13601800: Event 13601800 """
    GotoIfThisEventOff(Label.L0)
    DisableCharacter(3600800)
    DisableCharacter(3600801)
    Kill(3600800, award_souls=False)
    Kill(3600801, award_souls=False)
    DisableObject(3601800)
    DeleteFX(3603800, erase_root_only=True)
    End()
    Label(0)
    IfCharacterDead(1, 3600800)
    IfCharacterDead(2, 3600801)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(3601800)
    DisableObject(3601801)
    DeleteFX(3603800, erase_root_only=True)
    DeleteFX(3603801, erase_root_only=True)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, 2)
    KillBoss(3600800)
    SkipLines(1)
    KillBoss(3600801)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    AwardAchievement(35)
    RunEvent(9350, slot=0, args=(5,))
    AwardItemLot(3601800, host_only=False)
    EnableFlag(3600)
    StopPlayLogMeasurement(9360000)
    StopPlayLogMeasurement(9360001)
    StopPlayLogMeasurement(9360010)
    CreatePlayLog(0)
    PlayLogParameterOutput(PlayerPlayLogParameter.PrimaryParameters, 12, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.TemporaryParameters, 12, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Weapon, 12, PlayLogMultiplayerType.HostOnly)
    PlayLogParameterOutput(PlayerPlayLogParameter.Armor, 12, PlayLogMultiplayerType.HostOnly)
    End()
    Label(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


@NeverRestart
def Event13604811():
    """ 13604811: Event 13604811 """
    EndIfFlagOn(13601800)
    EndIfFlagOn(13601801)
    DisableCharacter(3600800)
    IfFlagOff(1, 13601800)
    IfFlagOff(1, 13601801)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3602805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13604810)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    DeleteFX(3603860, erase_root_only=True)
    EnableFlag(9180)


@NeverRestart
def Event13601801():
    """ 13601801: Event 13601801 """
    EndIfFlagOn(13601800)
    EndIfThisEventOn()
    IfCharacterType(1, PLAYER, CharacterType.BlackPhantom)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfFlagOff(2, 13601800)
    IfThisEventOff(2)
    IfFlagOn(2, 13604811)
    IfCharacterHuman(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3602805)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(36000000, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(36000000, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(9180)
    CreateFX(3603860)
    EnableFlag(13604808)
    EnableCharacter(3600800)
    EndIfFlagOn(9347)
    RunEvent(9350, slot=0, args=(5,))
    EnableFlag(9347)
    End()
    Label(0)
    IfFlagOn(0, 6001)
    Wait(0.0)


@NeverRestart
def Event13601802():
    """ 13601802: Event 13601802 """
    DisableAI(3600802)
    DisableHealthBar(3600802)
    DisableGravity(3600802)
    IfCharacterBackreadEnabled(0, 3600802)
    Move(3600802, destination=3601802, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    ForceAnimation(3600802, 7000, loop=True)
    EndIfFlagOn(13601803)
    GotoIfThisEventOff(Label.L0)
    ForceAnimation(3600802, 0, loop=True)
    End()
    Label(0)
    IfFlagOn(0, 13601800)
    ForceAnimation(3600802, 7001)


@NeverRestart
def Event13601803():
    """ 13601803: Event 13601803 """
    GotoIfThisEventOn(Label.L0)
    DisableObject(3601811)
    IfCharacterDead(0, 3600802)
    DisplayBanner(BannerType.Draw)
    Wait(5.0)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    Label(0)
    DisableMapSound(3603000)
    DisableMapSound(3603001)
    DeleteFX(3603810, erase_root_only=True)
    DeleteFX(3603811, erase_root_only=True)
    DeleteFX(3603812, erase_root_only=True)
    DeleteFX(3603813, erase_root_only=True)
    DeleteFX(3603814, erase_root_only=True)
    DeleteFX(3603815, erase_root_only=True)
    DeleteFX(3603816, erase_root_only=True)
    DeleteFX(3603817, erase_root_only=True)
    DeleteFX(3603818, erase_root_only=True)
    DeleteFX(3603819, erase_root_only=True)
    DeleteFX(3603820, erase_root_only=True)
    DeleteFX(3603821, erase_root_only=True)
    DeleteFX(3603822, erase_root_only=True)
    DeleteFX(3603823, erase_root_only=True)
    DeleteFX(3603824, erase_root_only=True)
    DeleteFX(3603825, erase_root_only=True)
    DeleteFX(3603826, erase_root_only=True)
    DeleteFX(3603827, erase_root_only=True)
    DeleteFX(3603828, erase_root_only=True)
    DeleteFX(3603829, erase_root_only=True)
    DeleteFX(3603830, erase_root_only=True)
    DeleteFX(3603831, erase_root_only=True)
    DeleteFX(3603832, erase_root_only=True)
    DeleteFX(3603840, erase_root_only=True)
    DeleteFX(3603841, erase_root_only=True)
    DeleteFX(3603842, erase_root_only=True)
    DeleteFX(3603843, erase_root_only=True)
    DeleteFX(3603844, erase_root_only=True)
    DeleteFX(3603845, erase_root_only=True)
    DeleteFX(3603846, erase_root_only=True)
    DeleteFX(3603847, erase_root_only=True)
    DeleteFX(3603848, erase_root_only=True)
    DeleteFX(3603849, erase_root_only=True)
    DeleteFX(3603850, erase_root_only=True)
    DeleteFX(3603851, erase_root_only=True)
    DeleteFX(3603852, erase_root_only=True)
    DeleteFX(3603860, erase_root_only=True)
    DeleteFX(3603870, erase_root_only=True)
    DeleteFX(3603871, erase_root_only=True)
    DeleteFX(3603872, erase_root_only=True)
    DeleteFX(3603873, erase_root_only=True)
    DeleteFX(3603874, erase_root_only=True)
    SkipLinesIfThisEventOff(2)
    DisableObject(3601810)
    EnableObject(3601811)
    EndIfThisEventOn()
    EnableFlag(9180)
    PlayCutscene(36000010, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObject(3601810)
    EnableObject(3601811)
    DisableFlag(9180)
    EnableFlag(9469)
    RunEvent(9350, slot=0, args=(3,))


@NeverRestart
def Event13601804():
    """ 13601804: Event 13601804 """
    IfCharacterHuman(1, PLAYER)
    IfFlagOn(1, 13604808)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(3600800)
    EnableFlag(13604808)
    EnableFlag(13601801)


@NeverRestart
def Event13604800():
    """ 13604800: Event 13604800 """
    EndIfFlagOn(13601800)
    GotoIfFlagOn(Label.L0, 13601801)
    SkipLinesIfClient(2)
    DisableObject(3601800)
    DeleteFX(3603800, erase_root_only=False)
    IfFlagOff(1, 13601800)
    IfFlagOn(1, 13601801)
    IfConditionTrue(0, input_condition=1)
    EnableObject(3601800)
    EnableObject(3601801)
    CreateFX(3603800)
    CreateFX(3603801)
    Label(0)
    IfFlagOff(2, 13601800)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonInRegion(2, action_button_id=3600800, region=3601800)
    IfFlagOn(3, 13601800)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(3)
    RotateToFaceEntity(PLAYER, 3602800, animation=101130, wait_for_completion=True)
    IfCharacterHuman(4, PLAYER)
    IfCharacterInsideRegion(4, PLAYER, region=3602801)
    IfCharacterHuman(5, PLAYER)
    IfTimeElapsed(5, 2.0)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    SkipLinesIfFinishedConditionTrue(1, 5)
    EnableFlag(13604808)
    Restart()


@NeverRestart
def Event13604801():
    """ 13604801: Event 13604801 """
    DisableNetworkSync()
    EndIfFlagOn(13601800)
    IfFlagOff(1, 13601800)
    IfFlagOn(1, 13601801)
    IfFlagOn(1, 13604808)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonInRegion(1, action_button_id=3600800, region=3601800)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, 3602800, animation=101130, wait_for_completion=True)
    IfCharacterType(2, PLAYER, CharacterType.WhitePhantom)
    IfCharacterInsideRegion(2, PLAYER, region=3602801)
    IfTimeElapsed(3, 2.0)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionTrue(1, 3)
    EnableFlag(13604809)
    Restart()


@NeverRestart
def Event13604802():
    """ 13604802: Event 13604802 """
    EndIfFlagOn(13601800)
    DisableAI(3600800)
    DisableAI(3600801)
    DisableHealthBar(3600800)
    DisableHealthBar(3600801)
    ReferDamageToEntity(3600800, 3600801)
    GotoIfThisEventOn(Label.L0)
    IfFlagOn(0, 13604808)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagOn(1, 13604810)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(3600800, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(3600801, UpdateAuthority.Forced)
    Label(0)
    EnableFlag(13604810)
    EnableFlag(13604808)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)
    Label(1)
    Goto(Label.L4)
    Label(2)
    AddSpecialEffect(3600800, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(3600801, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3600800)
    AdaptSpecialEffectHealthChangeToNPCPart(3600801)
    Goto(Label.L4)
    Label(3)
    AddSpecialEffect(3600800, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(3600801, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(3600800)
    AdaptSpecialEffectHealthChangeToNPCPart(3600801)
    Goto(Label.L4)
    Label(4)
    EnableBossHealthBar(3600801, name=453000, slot=0)
    EnableFlag(13604812)
    GotoIfThisEventOn(Label.L5)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(-2, 10000, 3600800, radius=24.0)
    IfDamageType(-2, attacked_entity=3600800, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Label(5)
    SkipLinesIfFlagOn(4, 13604820)
    EnableAI(3600800)
    SetNetworkUpdateRate(3600800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3600801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLines(3)
    EnableAI(3600801)
    SetNetworkUpdateRate(3600800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(3600801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreatePlayLog(42)
    StartPlayLogMeasurement(3600010, 58, overwrite=True)


@NeverRestart
def Event13604803():
    """ 13604803: Event 13604803 """
    DisableNetworkSync()
    DisableMapSound(3603802)
    DisableMapSound(3603803)
    EndIfFlagOn(13601800)
    GotoIfThisEventOn(Label.L0)
    IfFlagOff(1, 13601800)
    IfFlagOn(1, 13604812)
    SkipLinesIfHost(1)
    IfFlagOn(1, 13604809)
    IfCharacterInsideRegion(1, PLAYER, region=3602802)
    IfConditionTrue(0, input_condition=1)
    SetBossMusicState(3603802, state=True)
    IfFlagOn(2, 13604820)
    Label(0)
    IfFlagOff(2, 13601800)
    IfFlagOn(2, 13604812)
    SkipLinesIfHost(1)
    IfFlagOn(2, 13604809)
    IfCharacterInsideRegion(2, PLAYER, region=3602802)
    IfConditionTrue(0, input_condition=2)
    SetBossMusicState(3603802, state=False)
    WaitFrames(0)
    SetBossMusicState(3603803, state=True)


@NeverRestart
def Event13604804():
    """ 13604804: Event 13604804 """
    DisableNetworkSync()
    EndIfFlagOn(13601800)
    GotoIfFlagOn(Label.L0, 13604820)
    IfCharacterAlive(1, 3600800)
    IfEntityWithinDistance(1, 10000, 3600800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(2, 3600800)
    IfEntityBeyondDistance(2, 10000, 3600800, radius=12.5)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()
    Label(0)
    IfCharacterAlive(3, 3600800)
    IfEntityWithinDistance(3, 10000, 3600801, radius=12.0)
    IfConditionTrue(0, input_condition=3)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(4, 3600800)
    IfEntityBeyondDistance(4, 10000, 3600801, radius=12.5)
    IfConditionTrue(0, input_condition=4)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()


@NeverRestart
def Event13604805():
    """ 13604805: Event 13604805 """
    DisableNetworkSync()
    EndIfFlagOn(13601800)
    IfFlagOn(0, 13601800)
    SetBossMusicState(3603802, state=False)
    SetBossMusicState(3603803, state=False)
    SetBossMusicState(-1, state=False)


@NeverRestart
def Event13604806():
    """ 13604806: Event 13604806 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, 10000, 3601800, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event13604807():
    """ 13604807: Event 13604807 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, 10000, 3601800, radius=6.0)
    IfEntityWithinDistance(1, 10000, 3601800, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


@NeverRestart
def Event13604820():
    """ 13604820: Event 13604820 """
    EndIfFlagOn(13601800)
    GotoIfThisEventOff(Label.L0)
    DisableCharacter(3600800)
    End()
    Label(0)
    DisableGravity(3600801)
    IfHealthLessThan(0, 3600800, 0.5)
    AICommand(3600800, command_id=100, slot=0)
    ReplanAI(3600800)
    IfHasTAEEvent(0, 3600800, tae_event_id=100)
    DisableCharacter(3600800)
    EnableGravity(3600801)
    SetNetworkUpdateRate(3600800, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(3600801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(3600801, destination=3600800, destination_type=CoordEntityType.Character, model_point=203, copy_draw_hitbox=3600800)
    ForceAnimation(3600801, 3031)
    IfHasTAEEvent(0, 3600801, tae_event_id=50)
    CancelSpecialEffect(3600801, 5300)
    AddSpecialEffect(3600801, 5333, affect_npc_part_hp=False)
    EnableAI(3600801)


@NeverRestart
def Event13604830():
    """ 13604830: Event 13604830 """
    EndIfFlagOn(13601800)
    IfHasTAEEvent(0, 3600801, tae_event_id=100)
    AICommand(3600803, command_id=10, slot=0)
    ReplanAI(3600803)
    IfCharacterHasSpecialEffect(0, 3600803, 5020)
    AICommand(3600803, command_id=20, slot=0)
    ReplanAI(3600803)
    IfHasTAEEvent(0, 3600803, tae_event_id=10)
    AICommand(3600803, command_id=-1, slot=0)
    CancelSpecialEffect(3600803, 5020)
    ReplanAI(3600803)
    Restart()


@NeverRestart
def Event13604840():
    """ 13604840: Event 13604840 """
    DisableNetworkSync()
    EndIfFlagOn(13601800)
    IfHasTAEEvent(1, 3600800, tae_event_id=30)
    IfCharacterHasSpecialEffect(1, PLAYER, 8055)
    IfConditionTrue(0, input_condition=1)
    AddSpecialEffect(PLAYER, 8054, affect_npc_part_hp=False)
    IfHasTAEEvent(-1, 3600800, tae_event_id=40)
    IfTimeElapsed(-1, 4.5)
    IfEntityBeyondDistance(-1, 3600800, 10000, radius=20.0)
    IfConditionTrue(0, input_condition=-1)
    CancelSpecialEffect(PLAYER, 8054)
    Restart()


@NeverRestart
def Event13604850():
    """ 13604850: Event 13604850 """
    DisableNetworkSync()
    EndIfFlagOn(13601800)
    IfCharacterHasSpecialEffect(0, 3600801, 5036)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=1)
    IfCharacterDoesNotHaveSpecialEffect(0, 3600801, 5036)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()


@RestartOnRest
def Event13605200(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: float, ARG_20_23: int):
    """ 13605200: Event 13605200 """
    GotoIfThisEventSlotOn(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Wait(ARG_16_19)
    Label(0)
    SkipLinesIfEqual(1, left=ARG_20_23, right=0)
    AddSpecialEffect(ARG_0_3, 5000, affect_npc_part_hp=False)
    ChangePatrolBehavior(ARG_0_3, patrol_information_id=ARG_12_15)
    ReplanAI(ARG_0_3)


@RestartOnRest
def Event13605400(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: float, ARG_28_31: float):
    """ 13605400: Event 13605400 """
    GotoIfThisEventSlotOn(Label.L0)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True)
    SetAIParamID(ARG_0_3, ARG_8_11)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Recognition)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=ARG_24_27, max_seconds=ARG_28_31)
    RotateToFaceEntity(ARG_0_3, 10000, animation=ARG_12_15, wait_for_completion=False)
    Label(0)
    SetAIParamID(ARG_0_3, ARG_16_19)


@RestartOnRest
def Event13605480(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: float, ARG_28_31: int):
    """ 13605480: Event 13605480 """
    GotoIfThisEventSlotOn(Label.L0)
    DisableAI(ARG_0_3)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True)
    SetAIParamID(ARG_0_3, ARG_8_11)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Recognition)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    Wait(ARG_24_27)
    RotateToFaceEntity(ARG_0_3, 10000, animation=ARG_12_15, wait_for_completion=False)
    WaitFrames(ARG_28_31)
    Label(0)
    EnableAI(ARG_0_3)
    SetAIParamID(ARG_0_3, ARG_16_19)


@RestartOnRest
def Event13605490(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: float, ARG_28_31: float):
    """ 13605490: Event 13605490 """
    GotoIfThisEventSlotOn(Label.L0)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True)
    SetAIParamID(ARG_0_3, ARG_8_11)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Recognition)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, ARG_20_23, ai_status=AIStatusType.Recognition)
    IfHasAIStatus(-1, ARG_20_23, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, 10000, ARG_0_3, radius=4.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=ARG_24_27, max_seconds=ARG_28_31)
    RotateToFaceEntity(ARG_0_3, 10000, animation=ARG_12_15, wait_for_completion=False)
    Label(0)
    SetAIParamID(ARG_0_3, ARG_16_19)


@RestartOnRest
def Event13605500(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: float, ARG_28_31: float):
    """ 13605500: Event 13605500 """
    GotoIfThisEventSlotOn(Label.L0)
    DisableGravity(ARG_0_3)
    DisableCollision(ARG_0_3)
    ForceAnimation(ARG_0_3, ARG_4_7, loop=True)
    SetAIParamID(ARG_0_3, ARG_8_11)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Recognition)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=ARG_24_27, max_seconds=ARG_28_31)
    RotateToFaceEntity(ARG_0_3, 10000, animation=ARG_12_15, wait_for_completion=False)
    EnableGravity(ARG_0_3)
    EnableCollision(ARG_0_3)
    Label(0)
    SetAIParamID(ARG_0_3, ARG_16_19)


@RestartOnRest
def Event13605520(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int):
    """ 13605520: Event 13605520 """
    IfAllPlayersOutsideRegion(1, region=ARG_4_7)
    IfConditionFalse(0, input_condition=1)
    SetAIParamID(ARG_0_3, ARG_8_11)
    IfAllPlayersOutsideRegion(0, region=ARG_4_7)
    SetAIParamID(ARG_0_3, ARG_12_15)
    Restart()


@RestartOnRest
def Event13605540(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: int, ARG_16_19: int):
    """ 13605540: Event 13605540 """
    GotoIfThisEventSlotOn(Label.L0)
    SetAIParamID(ARG_0_3, ARG_12_15)
    IfCharacterInsideRegion(1, ARG_0_3, region=ARG_4_7)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    Label(0)
    SetAIParamID(ARG_0_3, ARG_16_19)


@RestartOnRest
def Event13605560(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float):
    """ 13605560: Event 13605560 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=ARG_4_7)
    IfEntityWithinDistance(-2, 10000, ARG_0_3, radius=ARG_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableAI(ARG_0_3)


@RestartOnRest
def Event13605600(ARG_0_3: int, ARG_4_7: int):
    """ 13605600: Event 13605600 """
    DisableGravity(ARG_4_7)
    SkipLinesIfThisEventSlotOn(2)
    IfCharacterBackreadEnabled(0, ARG_0_3)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, ARG_0_3, 0.0)
    SkipLinesIfConditionFalse(2, 1)
    DisableBackread(ARG_4_7)
    End()
    Move(ARG_4_7, destination=ARG_0_3, destination_type=CoordEntityType.Character, model_point=100, set_draw_hitbox=ARG_0_3)
    Restart()


@RestartOnRest
def Event13605605():
    """ 13605605: Event 13605605 """
    DisableNetworkSync()
    IfCharacterHasSpecialEffect(1, PLAYER, 4691)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfCharacterHasSpecialEffect(0, PLAYER, 4690)
    Wait(2.0)
    IfCharacterHasSpecialEffect(2, PLAYER, 4690)
    IfCharacterDoesNotHaveSpecialEffect(3, PLAYER, 4690)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFinishedConditionTrue(3)
    Label(0)
    AddSpecialEffect_WithUnknownEffect(PLAYER, 4691, affect_npc_parts_hp=False)
    Restart()


@RestartOnRest
def Event13605606():
    """ 13605606: Event 13605606 """
    DisableNetworkSync()
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 4690)
    IfCharacterHasSpecialEffect(1, PLAYER, 4691)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(PLAYER, 4691)
    Restart()


@RestartOnRest
def Event13605700(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 13605700: Event 13605700 """
    GotoIfFlagOn(Label.L0, ARG_8_11)
    DisableFlag(ARG_8_11)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Recognition)
    IfHasAIStatus(-1, ARG_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(ARG_8_11)
    RotateToFaceEntity(ARG_0_3, 10000, animation=ARG_4_7, wait_for_completion=True)
    Label(0)
    IfHasAIStatus(0, ARG_0_3, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event13605720(ARG_0_3: int):
    """ 13605720: Event 13605720 """
    IfHasTAEEvent(0, ARG_0_3, tae_event_id=100)
    MoveObjectToCharacter(3601799, character=PLAYER, model_point=-1)
    WaitFrames(1)
    ShootProjectile(owner_entity=3600799, projectile_id=3601799, model_point=200, behavior_id=6300, launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)
    Wait(1.0)
    Restart()


@RestartOnRest
def Event13605730():
    """ 13605730: Event 13605730 """
    DisableNetworkSync()
    IfCharacterType(1, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(1)
    IfCharacterInsideRegion(0, PLAYER, region=3602798)
    MoveObjectToCharacter(3601798, character=PLAYER, model_point=-1)
    WaitFrames(1)
    ShootProjectile(owner_entity=3600799, projectile_id=3601798, model_point=200, behavior_id=6330, launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)
    IfCharacterOutsideRegion(0, PLAYER, region=3602798)
    Restart()


@RestartOnRest
def Event13605740(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: float):
    """ 13605740: Event 13605740 """
    EndIfThisEventOn()
    DisableAI(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=ARG_4_7)
    IfEntityWithinDistance(3, 10000, ARG_0_3, radius=ARG_12_15)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, 3)
    SetCharacterEventTarget(ARG_0_3, ARG_8_11)
    AICommand(ARG_0_3, command_id=100, slot=0)
    EnableAI(ARG_0_3)
    WaitFrames(60)
    AICommand(ARG_0_3, command_id=-1, slot=0)


@RestartOnRest
def Event13605750():
    """ 13605750: Event 13605750 """
    GotoIfThisEventSlotOn(Label.L0)
    DisableGravity(3600201)
    DisableCollision(3600201)
    ForceAnimation(3600201, 7006, loop=True)
    SetAIParamID(3600201, 404003)
    IfHasAIStatus(-1, 3600201, ai_status=AIStatusType.Recognition)
    IfHasAIStatus(-1, 3600201, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    SkipLinesIfFlagOn(2, 53600100)
    IfEntityWithinDistance(1, 10000, 3600201, radius=12.0)
    SkipLines(1)
    IfCharacterInsideRegion(1, PLAYER, region=3602201)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    RotateToFaceEntity(3600201, 10000, animation=7007, wait_for_completion=False)
    EnableGravity(3600201)
    EnableCollision(3600201)
    Label(0)
    SetAIParamID(3600201, 404000)


@RestartOnRest
def Event13605751():
    """ 13605751: Event 13605751 """
    IfHasTAEEvent(0, 3600330, tae_event_id=100)
    SetAIParamID(3600208, 404002)
    SetAIParamID(3600209, 404002)
    MoveObjectToCharacter(3601799, character=PLAYER, model_point=-1)
    WaitFrames(1)
    ShootProjectile(owner_entity=3600799, projectile_id=3601799, model_point=200, behavior_id=6300, launch_angle_x=0, launch_angle_y=0, launch_angle_z=0)


@RestartOnRest
def Event13605752():
    """ 13605752: Event 13605752 """
    EndIfThisEventOn()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3602315)
    IfDamageType(2, attacked_entity=3600315, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    SetNest(3600315, 3602316)
    AICommand(3600315, command_id=10, slot=0)
    ReplanAI(3600315)
    IfCharacterInsideRegion(0, 3600315, region=3602316)
    AICommand(3600315, command_id=-1, slot=0)
    ReplanAI(3600315)


@RestartOnRest
def Event13605760():
    """ 13605760: Event 13605760 """
    EndIfThisEventOn()
    IfHealthLessThan(0, 3600302, 0.5)
    SetNest(3600302, 3602303)
    AICommand(3600302, command_id=10, slot=0)
    ReplanAI(3600302)
    IfCharacterInsideRegion(0, 3600302, region=3602303)
    AICommand(3600302, command_id=-1, slot=0)
    ReplanAI(3600302)


@RestartOnRest
def Event13605761():
    """ 13605761: Event 13605761 """
    EndIfThisEventOn()
    DisableAI(3600303)
    ForceAnimation(3600303, 7004, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3602304)
    IfHealthLessThan(1, 3600302, 0.5)
    IfHealthLessThan(2, 3600302, 0.4000000059604645)
    IfDamageType(3, attacked_entity=3600303, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(3600303, 7005)
    EnableAI(3600303)


@RestartOnRest
def Event13605762():
    """ 13605762: Event 13605762 """
    EndIfFlagOn(53600800)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfCharacterDead(2, 3600302)
    IfCharacterDead(2, 3600303)
    IfConditionTrue(0, input_condition=2)
    AwardItemLot(3601100, host_only=True)


@RestartOnRest
def Event13605770(ARG_0_3: int, ARG_4_7: int, ARG_8_11: float, ARG_12_15: float):
    """ 13605770: Event 13605770 """
    EndIfThisEventSlotOn()
    DisableAI(ARG_0_3)
    DisableGravity(ARG_0_3)
    DisableCollision(ARG_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=ARG_4_7)
    IfDamageType(2, attacked_entity=ARG_0_3, attacking_character=-1, damage_type=DamageType.Unspecified)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    WaitRandomSeconds(min_seconds=ARG_8_11, max_seconds=ARG_12_15)
    EnableAI(ARG_0_3)
    EnableGravity(ARG_0_3)
    EnableCollision(ARG_0_3)


@RestartOnRest
def Event13605799():
    """ 13605799: Event 13605799 """
    CreateSpawner(3600799)


@RestartOnRest
def Event13605900(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 13605900: Event 13605900 """
    EndIfFlagOn(1730)
    EndIfFlagOn(ARG_8_11)
    EndIfFlagOn(ARG_4_7)
    IfFlagOff(1, 1730)
    IfFlagOff(1, ARG_4_7)
    IfFlagOff(1, ARG_8_11)
    IfFlagOff(1, ARG_20_23)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(ARG_0_3)


@RestartOnRest
def Event13605910(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 13605910: Event 13605910 """
    EndIfFlagOn(1730)
    EndIfFlagOn(ARG_8_11)
    EndIfFlagOn(ARG_4_7)
    IfFlagOff(1, 1730)
    IfFlagOff(1, ARG_4_7)
    IfFlagOff(1, ARG_8_11)
    IfFlagOn(1, ARG_0_3)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.s_SFX, sound_id=10306)
    WaitRandomSeconds(min_seconds=2.0, max_seconds=4.0)
    Restart()


@RestartOnRest
def Event13605920(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 13605920: Event 13605920 """
    AICommand(ARG_0_3, command_id=30, slot=0)
    ReplanAI(ARG_0_3)
    EnableInvincibility(ARG_0_3)
    DisableAnimations(ARG_0_3)
    AddSpecialEffect(ARG_0_3, 5560, affect_npc_part_hp=False)
    EndIfFlagOn(1730)
    EndIfFlagOn(ARG_8_11)
    GotoIfFlagOn(Label.L0, ARG_4_7)
    IfFlagOff(1, 1730)
    IfFlagOn(1, ARG_20_23)
    IfFlagOff(1, ARG_8_11)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Move(ARG_0_3, destination=ARG_28_31, destination_type=CoordEntityType.Region, model_point=-1, short_move=True)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    DisableInvincibility(ARG_0_3)
    EnableAnimations(ARG_0_3)
    CancelSpecialEffect(ARG_0_3, 5560)
    AddSpecialEffect(ARG_0_3, 8060, affect_npc_part_hp=False)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.s_SFX, sound_id=777777777)
    ForceAnimation(ARG_0_3, 101203)
    Label(0)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    DisableInvincibility(ARG_0_3)
    EnableAnimations(ARG_0_3)
    CancelSpecialEffect(ARG_0_3, 5560)
    EnableFlag(ARG_4_7)
    DisableFlag(ARG_24_27)
    IfFlagOn(0, ARG_24_27)
    Restart()


@RestartOnRest
def Event13605921(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int, ARG_24_27: int, ARG_28_31: int):
    """ 13605921: Event 13605921 """
    AICommand(ARG_0_3, command_id=30, slot=0)
    ReplanAI(ARG_0_3)
    EnableInvincibility(ARG_0_3)
    DisableAnimations(ARG_0_3)
    AddSpecialEffect(ARG_0_3, 5560, affect_npc_part_hp=False)
    EndIfFlagOn(1730)
    EndIfFlagOn(ARG_8_11)
    GotoIfFlagOn(Label.L0, ARG_4_7)
    IfFlagOff(1, 1730)
    IfFlagOn(1, ARG_20_23)
    IfFlagOff(1, ARG_8_11)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=ARG_12_15)
    IfConditionTrue(-1, input_condition=2)
    IfCharacterInsideRegion(3, PLAYER, region=ARG_16_19)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, 3)
    Move(ARG_0_3, destination=ARG_28_31, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=3604027)
    SkipLines(1)
    Move(ARG_0_3, destination=3602917, destination_type=CoordEntityType.Region, model_point=-1, set_draw_hitbox=3604027)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    DisableInvincibility(ARG_0_3)
    EnableAnimations(ARG_0_3)
    CancelSpecialEffect(ARG_0_3, 5560)
    AddSpecialEffect(ARG_0_3, 8060, affect_npc_part_hp=False)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.s_SFX, sound_id=777777777)
    ForceAnimation(ARG_0_3, 101203)
    Label(0)
    AICommand(ARG_0_3, command_id=-1, slot=0)
    ReplanAI(ARG_0_3)
    DisableInvincibility(ARG_0_3)
    EnableAnimations(ARG_0_3)
    CancelSpecialEffect(ARG_0_3, 5560)
    EnableFlag(ARG_4_7)
    DisableFlag(ARG_24_27)
    IfFlagOn(0, ARG_24_27)
    Restart()


@RestartOnRest
def Event13605930(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int, ARG_20_23: int):
    """ 13605930: Event 13605930 """
    EndIfFlagOn(1730)
    EndIfFlagOn(ARG_8_11)
    IfFlagOn(1, ARG_4_7)
    IfHealthGreaterThan(1, ARG_0_3, 0.0)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=ARG_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AICommand(ARG_0_3, command_id=30, slot=0)
    ReplanAI(ARG_0_3)
    Wait(2.0)
    EnableInvincibility(ARG_0_3)
    DisableAnimations(ARG_0_3)
    AddSpecialEffect(ARG_0_3, 5560, affect_npc_part_hp=False)
    CancelSpecialEffect(ARG_0_3, 8060)
    CancelSpecialEffect(ARG_0_3, 1130)
    CancelSpecialEffect(ARG_0_3, 1150)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.s_SFX, sound_id=122)
    Wait(4.0)
    EnableFlag(ARG_20_23)
    DisableFlag(ARG_4_7)
    IfFlagOn(0, ARG_4_7)
    Restart()


@RestartOnRest
def Event13605940(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 13605940: Event 13605940 """
    DisableBackread(ARG_16_19)
    GotoIfFlagOff(Label.L0, 1730)
    DropMandatoryTreasure(ARG_16_19)
    End()
    Label(0)
    EndIfFlagOn(ARG_8_11)
    IfFlagOn(1, ARG_4_7)
    IfCharacterDead(1, ARG_0_3)
    IfConditionTrue(0, input_condition=1)
    CancelSpecialEffect(ARG_0_3, 8060)
    CancelSpecialEffect(ARG_0_3, 1130)
    CancelSpecialEffect(ARG_0_3, 1150)
    PlaySoundEffect(anchor_entity=10000, sound_type=SoundType.s_SFX, sound_id=122)
    EnableFlag(ARG_8_11)
    IfCharacterHuman(2, PLAYER)
    SkipLinesIfConditionFalse(1, 2)
    AwardItemLot(ARG_12_15, host_only=True)


@NeverRestart
def Event13600900(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int, ARG_12_15: int, ARG_16_19: int):
    """ 13600900: Event 13600900 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyOn((ARG_4_7, ARG_12_15))
    IfCharacterDead(1, ARG_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((ARG_4_7, ARG_8_11))
    EnableFlag(ARG_16_19)
    SaveRequest()


@NeverRestart
def Event13600940(ARG_0_3: int):
    """ 13600940: Event 13600940 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    DisableFlagRange((1770, 1789))
    EnableFlag(1780)
    Label(0)
    GotoIfFlagOn(Label.L0, 1770)
    GotoIfFlagOn(Label.L1, 1780)
    DisableBackread(ARG_0_3)
    DisableCharacter(ARG_0_3)
    End()
    Label(0)
    Label(1)
    DisableFlag(73600310)
    DisableFlag(73600314)
    EnableBackread(ARG_0_3)
    EnableCharacter(ARG_0_3)
    EnableImmortality(ARG_0_3)
    SetDistanceLimitForConversationStateChanges(ARG_0_3, distance=35.0)
    End()


@NeverRestart
def Event13600943(ARG_0_3: int, ARG_4_7: int):
    """ 13600943: Event 13600943 """
    EndIfFlagOn(ARG_0_3)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagOn(0, ARG_0_3)
    AwardItemLot(ARG_4_7, host_only=False)


@NeverRestart
def Event13600941(ARG_0_3: int, ARG_4_7: int):
    """ 13600941: Event 13600941 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagOff(-1, ARG_0_3)
    IfFlagOn(-1, ARG_4_7)
    IfConditionTrue(0, input_condition=-1)
    IfFlagOn(1, ARG_0_3)
    IfFlagOff(1, ARG_4_7)
    IfConditionTrue(0, input_condition=1)
    Restart()


@NeverRestart
def Event13600942(ARG_0_3: float, ARG_4_7: float):
    """ 13600942: Event 13600942 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagOn(0, 73600310)
    WaitRandomSeconds(min_seconds=ARG_0_3, max_seconds=ARG_4_7)
    SkipLinesIfFlagOff(3, 73600313)
    IfFlagOff(0, 73600314)
    DisableFlag(73600313)
    Restart()
    DisableFlag(73600310)
    Restart()


@NeverRestart
def Event13600944():
    """ 13600944: Event 13600944 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(73600318)
    IfCharacterInsideRegion(0, PLAYER, region=3602941)
    EnableFlag(73600318)
    IfCharacterOutsideRegion(0, PLAYER, region=3602941)
    Restart()


@NeverRestart
def Event13600950(ARG_0_3: int):
    """ 13600950: Event 13600950 """
    IfCharacterHuman(-15, PLAYER)
    GotoIfConditionFalse(Label.L8, input_condition=-15)
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1710, 1729))
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)
    Label(0)
    IfFlagRangeAnyOn(1, (1720, 1722))
    IfFlagOn(1, 73400403)
    IfFlagOn(1, 1650)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)
    Label(1)
    IfFlagOn(2, 1722)
    IfFlagOn(-2, 1660)
    IfFlagOn(-2, 1651)
    IfConditionTrue(2, input_condition=-2)
    IfFlagOn(2, 73500602)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)
    Label(2)
    IfFlagOn(3, 1723)
    IfFlagOn(3, 73600501)
    GotoIfConditionFalse(Label.L3, input_condition=3)
    DisableFlagRange((1710, 1729))
    EnableFlag(1713)
    Label(3)
    GotoIfFlagRangeState(Label.L4, RangeState.AnyOn, FlagType.Absolute, (1710, 1712))
    GotoIfFlagOn(Label.L4, 1720)
    DisableObject(3600906)
    DisableTreasure(3600906)
    Goto(Label.L9)
    Label(4)
    EnableObject(3600906)
    EnableTreasure(3600906)
    Goto(Label.L9)
    Label(8)
    DisableTreasure(3600906)
    GotoIfFlagRangeState(Label.L5, RangeState.AnyOn, FlagType.Absolute, (1710, 1712))
    GotoIfFlagOn(Label.L5, 1720)
    DisableObject(3600906)
    Goto(Label.L9)
    Label(5)
    EnableObject(3600906)
    Label(9)
    GotoIfFlagOn(Label.L0, 1723)
    GotoIfFlagOn(Label.L1, 1713)
    DisableCharacter(ARG_0_3)
    DisableBackread(ARG_0_3)
    End()
    Label(0)
    SetTeamType(ARG_0_3, TeamType.Ally)
    ForceAnimation(ARG_0_3, 103151)
    EnableImmortality(ARG_0_3)
    End()
    Label(1)
    DisableAnimations(ARG_0_3)
    ForceAnimation(ARG_0_3, 103157, skip_transition=True)
    End()


@NeverRestart
def Event13600951(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 13600951: Event 13600951 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(ARG_4_7)
    IfFlagOn(1, ARG_8_11)
    IfFlagOn(1, ARG_4_7)
    IfHealthNotEqual(1, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, 103152)
    IfFlagOn(2, ARG_8_11)
    IfFlagOff(2, ARG_4_7)
    IfHealthNotEqual(2, ARG_0_3, 0.0)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(ARG_0_3, 103151)
    Restart()


@NeverRestart
def Event13600952(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 13600952: Event 13600952 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagOn(1, ARG_4_7)
    IfDamageType(1, attacked_entity=ARG_0_3, attacking_character=PLAYER, damage_type=DamageType.Unspecified)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(ARG_0_3, 103153)
    Kill(ARG_0_3, award_souls=True)
    EnableFlag(ARG_8_11)


@NeverRestart
def Event13600953(ARG_0_3: int):
    """ 13600953: Event 13600953 """
    IfFlagOn(-1, 1724)
    IfFlagRangeAnyOn(-1, (1720, 1722))
    EndIfConditionFalse(-1)
    IfFlagOn(0, 1723)
    EnableCharacter(ARG_0_3)
    EnableBackread(ARG_0_3)
    ForceAnimation(ARG_0_3, 103151)
    EnableImmortality(ARG_0_3)
    DisableObject(3600906)
    DisableTreasure(3600906)


@NeverRestart
def Event13600954(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 13600954: Event 13600954 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    GotoIfFlagOff(Label.L0, ARG_0_3)
    GotoIfFlagOff(Label.L1, ARG_4_7)
    End()
    Label(1)
    EnableFlag(ARG_4_7)
    Label(0)
    IfFlagOn(1, ARG_4_7)
    IfCharacterDead(1, 3600905)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(ARG_8_11, host_only=False)


@NeverRestart
def Event13600955():
    """ 13600955: Event 13600955 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagOn(1, 1723)
    IfFlagOff(1, 73600502)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(73600500)
    IfCharacterInsideRegion(0, PLAYER, region=3602850)
    DisableFlag(73600500)
    EnableFlag(73600502)


@NeverRestart
def Event13600956(ARG_0_3: int, ARG_4_7: int, ARG_8_11: int):
    """ 13600956: Event 13600956 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(ARG_8_11)
    IfFlagOn(1, ARG_4_7)
    IfFlagOn(1, ARG_8_11)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(ARG_8_11)
    Kill(ARG_0_3, award_souls=False)
    EnableFlag(73600530)
    ForceAnimation(ARG_0_3, 103156, wait_for_completion=True, skip_transition=True)
    ForceAnimation(ARG_0_3, 103157, skip_transition=True)


@NeverRestart
def Event13600995():
    """ 13600995: Event 13600995 """
    EndIfThisEventOn()
    IfFlagOn(0, 13605952)
    DisableFlag(13605940)
