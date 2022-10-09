"""FISHING HAMLET

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
from soulstruct.bloodborne.events import *
from .common_entities import *
from m36_00_entities import *


def Constructor():
    """ 0: Event 0 """
    RunEvent(7000, slot=65, args=(3600950, 3601950, 999, 13607800))
    RunEvent(7000, slot=66, args=(3600951, 3601951, 999, 13607820))
    RunEvent(7000, slot=67, args=(3600952, 3601952, Flags.OrphanDead, 13607840))
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
    Event13604740()
    Event13604742()
    Event13600000()
    Event13600010()
    Event13601090()
    Event13601100()
    Event13601101()
    Event13601102()
    Event13601103()
    Event13601104()
    Event13601105()
    RunEvent(13601200, slot=0, args=(3601200, 13604200, 1, 10))
    RunEvent(13601200, slot=1, args=(3601201, 13604201, 1, 10))
    RunEvent(13601210, slot=0, args=(7030, 3601200, 13601200))
    RunEvent(13601210, slot=1, args=(7030, 3601201, 13601201))
    RegisterLadder(start_climbing_flag=13601300, stop_climbing_flag=13601301, obj=3601300)
    RegisterLadder(start_climbing_flag=13601302, stop_climbing_flag=13601303, obj=3601301)
    RegisterLadder(start_climbing_flag=13601304, stop_climbing_flag=13601305, obj=3601302)
    RegisterLadder(start_climbing_flag=13601306, stop_climbing_flag=13601307, obj=3601303)
    RegisterLadder(start_climbing_flag=13601308, stop_climbing_flag=13601309, obj=3601304)
    Event13601312()
    RunEvent(13601140, slot=0, args=(3601110, 3604110))
    RunEvent(13601140, slot=1, args=(3601111, 3604111))
    RunEvent(13601140, slot=2, args=(3601112, 3604112))
    RunEvent(13601140, slot=3, args=(3601113, 3604113))
    Event13601400()
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

    # ORPHAN OF KOS
    OrphanDies()
    OrphanFirstTimeTrigger()
    OrphanFirstTimeCutscene()
    EnterOrphanFog()
    EnterOrphanFogAsSummon()
    StartOrphanBattle()
    ControlOrphanMusic()
    StopOrphanMusic()
    Event13604806()
    Event13604807()
    OrphanPhaseTwoTrigger()
    OrphanPhaseTwoLightning()
    ApplyOrphanCrushEffect()
    ControlOrphanPhaseTwoLightningCamera()
    ControlOrphanSpirit()
    OrphanSpiritDies()
    SummonStartOrphanBattle()

    RunEvent(13605200, slot=0, args=(3600200, 3602200, 0, 3603200, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=1, args=(3600202, 3602202, 0, 3603202, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=2, args=(3600203, 3602202, 3602203, 3603203, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=3, args=(3600204, 3602202, 3602203, 3603204, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=4, args=(3600208, 3602208, 0, 3603208, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=5, args=(3600209, 3602208, 0, 3603209, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=6, args=(3600210, 3602210, 0, 3603210, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=7, args=(3600300, 3602300, 0, 3603300, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=8, args=(3600213, 3602213, 0, 3603213, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=9, args=(3600214, 3602213, 0, 3603214, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=10, args=(3600217, 3602215, 0, 3603217, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=11, args=(3600229, 3602229, 0, 3603229, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=12, args=(3600231, 3602231, 3602232, 3603231, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=13, args=(3600232, 3602231, 3602232, 3603232, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=14, args=(3600233, 3602231, 3602232, 3603233, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=15, args=(3600610, 3602610, 0, 3603610, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=16, args=(3600611, 3602231, 3602232, 3603611, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=17, args=(3600301, 3602301, 0, 3603301, 0.0, 1), arg_types="iiiifi")
    RunEvent(13605200, slot=18, args=(3600310, 3602310, 0, 3603310, 0.0, 1), arg_types="iiiifi")
    RunEvent(13605200, slot=19, args=(3600700, 3602700, 0, 3603700, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=20, args=(3600710, 3602710, 0, 3603710, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=21, args=(3600251, 3602251, 0, 3603251, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=23, args=(3600253, 3602252, 0, 3603253, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=25, args=(3600314, 3602314, 0, 3603314, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=26, args=(3600455, 3602455, 0, 3603455, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=27, args=(3600456, 3602455, 0, 3603456, 1.0, 1), arg_types="iiiifi")
    RunEvent(13605200, slot=28, args=(3600474, 3602474, 0, 3603474, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=29, args=(3600475, 3602474, 0, 3603475, 1.0, 1), arg_types="iiiifi")
    RunEvent(13605200, slot=30, args=(3600302, 3602302, 0, 3603302, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=31, args=(3600312, 3602312, 0, 3603312, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=32, args=(3600470, 3602470, 0, 3603470, 0.0, 1), arg_types="iiiifi")
    RunEvent(13605200, slot=33, args=(3600500, 3602470, 0, 3603500, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=34, args=(3600501, 3602501, 0, 3603501, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605200, slot=35, args=(3600920, 3602940, 0, 3603920, 0.0, 0), arg_types="iiiifi")
    RunEvent(13605400, slot=0, args=(3600206, 7004, 404002, 7005, 404002, 3602206, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=1, args=(3600211, 7012, 404000, 7013, 404000, 3602211, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=2, args=(3600218, 0, 404011, 3005, 404010, 3602218, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=3, args=(3600222, 7016, 404031, 7017, 404030, 3602222, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=4, args=(3600230, 7004, 404000, 7005, 404000, 3602230, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=5, args=(3600239, 7012, 404008, 7013, 404008, 3602240, 0.75, 0.75), arg_types="iiiiiiff")
    RunEvent(13605400, slot=6, args=(3600240, 7012, 404004, 7013, 404004, 3602240, 0.25, 0.25), arg_types="iiiiiiff")
    RunEvent(13605400, slot=7, args=(3600241, 7012, 404008, 7013, 404008, 3602240, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=8, args=(3600242, 7012, 404004, 7013, 404004, 3602240, 0.5, 0.5), arg_types="iiiiiiff")
    RunEvent(13605400, slot=9, args=(3600244, 7014, 404014, 7015, 404014, 3602244, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=10, args=(3600245, 0, 404035, 3026, 404034, 3602245, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=11, args=(3600246, 7018, 404034, 7019, 404034, 3602246, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=12, args=(3600247, 7018, 404014, 7019, 404014, 3602246, 0.5, 0.5), arg_types="iiiiiiff")
    RunEvent(13605400, slot=13, args=(3600260, 7012, 404018, 7013, 404019, 3602260, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=14, args=(3600261, 7012, 404018, 7013, 404019, 3602261, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=15, args=(3600262, 7012, 404018, 7013, 404019, 3602262, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=16, args=(3600265, 7012, 404018, 7013, 404019, 3602265, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=17, args=(3600400, 7010, 407022, 3001, 407020, 3602400, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=18, args=(3600401, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=19, args=(3600402, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=20, args=(3600403, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=21, args=(3600404, 7010, 407022, 3001, 407020, 3602400, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=22, args=(3600405, 7010, 407012, 7001, 407010, 3602400, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=25, args=(3600408, 7010, 407022, 3001, 407020, 3602408, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=26, args=(3600409, 7010, 407012, 7001, 407010, 3602408, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=27, args=(3600410, 7010, 407022, 3001, 407020, 3602408, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=28, args=(3600411, 7010, 407012, 7001, 407010, 3602408, 0.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=29, args=(3600412, 7010, 407012, 7001, 407010, 3602412, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=30, args=(3600413, 7010, 407012, 7001, 407010, 3602412, 1.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=33, args=(3600416, 7010, 407022, 3001, 407020, 3602416, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=34, args=(3600417, 7010, 407012, 7001, 407010, 3602416, 1.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=35, args=(3600418, 7010, 407012, 7001, 407010, 3602416, 0.5, 0.5), arg_types="iiiiiiff")
    RunEvent(13605400, slot=36, args=(3600419, 7010, 407012, 7001, 407010, 3602419, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=37, args=(3600424, 7010, 407022, 3001, 407020, 3602424, 0.5, 0.5), arg_types="iiiiiiff")
    RunEvent(13605400, slot=38, args=(3600425, 7010, 407012, 7001, 407010, 3602424, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=39, args=(3600426, 7010, 407012, 7001, 407010, 3602424, 1.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=40, args=(3600440, 7010, 407022, 7001, 407020, 3602440, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605400, slot=41, args=(3600441, 7010, 407022, 3001, 407020, 3602440, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605480, slot=0, args=(3600223, 7008, 404032, 7009, 404030, 3602223, 0.0, 33), arg_types="iiiiiifi")
    RunEvent(13605480, slot=1, args=(3600476, 7012, 407000, 7013, 407000, 3602476, 0.0, 30), arg_types="iiiiiifi")
    RunEvent(13605480, slot=2, args=(3600477, 7014, 407000, 7015, 407000, 3602476, 0.5, 30), arg_types="iiiiiifi")
    RunEvent(13605480, slot=3, args=(3600478, 7016, 407000, 7017, 407000, 3602478, 0.0, 30), arg_types="iiiiiifi")
    RunEvent(13605490, slot=0, args=(3600313, 9000, 405003, 9060, 405003, 3600314, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605490, slot=1, args=(3600266, 7012, 404018, 7013, 404019, 3600314, 0.5, 0.5), arg_types="iiiiiiff")
    RunEvent(13605490, slot=2, args=(3600267, 7014, 404018, 7015, 404019, 3600314, 1.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605490, slot=3, args=(3600263, 7012, 404018, 7013, 404019, 3600265, 0.5, 0.5), arg_types="iiiiiiff")
    RunEvent(13605490, slot=4, args=(3600264, 7012, 404018, 7013, 404019, 3600265, 1.0, 1.0), arg_types="iiiiiiff")
    RunEvent(13605500, slot=1, args=(3600207, 7006, 404002, 7007, 404002, 3602206, 4.0, 4.0), arg_types="iiiiiiff")
    RunEvent(13605500, slot=2, args=(3600212, 7006, 404016, 7007, 404010, 3602211, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605500, slot=3, args=(3600216, 7006, 404003, 7007, 404000, 3602215, 0.0, 0.0), arg_types="iiiiiiff")
    RunEvent(13605520, slot=1, args=(3600310, 3602310, 405001, 405000))
    RunEvent(13605540, slot=0, args=(3600210, 0, 8.0, 404040, 404000), arg_types="iifii")
    RunEvent(13605540, slot=1, args=(3600300, 0, 8.0, 406001, 406000), arg_types="iifii")
    RunEvent(13605540, slot=2, args=(3600500, 3602470, 4.0, 256901, 256900), arg_types="iifii")
    RunEvent(13605540, slot=3, args=(3600501, 3602470, 4.0, 256901, 256900), arg_types="iifii")
    RunEvent(13605540, slot=4, args=(3600218, 0, 1.0, 404011, 404010), arg_types="iifii")
    RunEvent(13605540, slot=5, args=(3600220, 0, 4.0, 404011, 404010), arg_types="iifii")
    RunEvent(13605540, slot=6, args=(3600221, 0, 4.0, 404011, 404010), arg_types="iifii")
    RunEvent(13605560, slot=0, args=(3600331, 3602331, 4.0), arg_types="iif")
    RunEvent(13605600, slot=0, args=(3600500, 3600510))
    RunEvent(13605600, slot=1, args=(3600501, 3600511))
    Event13605605()
    Event13605606()
    Event13605799()
    RunEvent(13605720, slot=0, args=(3600206,))
    RunEvent(13605720, slot=1, args=(3600314,))
    RunEvent(13605740, slot=0, args=(3600215, 3602215, 3600720, 2.0), arg_types="iiif")
    RunEvent(13605740, slot=1, args=(3600219, 3602218, 3600721, 2.0), arg_types="iiif")
    RunEvent(13605740, slot=2, args=(3600250, 3602250, 3600722, 2.0), arg_types="iiif")
    Event13605750()
    Event13605751()
    Event13605752()
    Event13605760()
    Event13605761()
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
    Event13600995()
    RunEvent(13600942, slot=0, args=(6.0, 10.0), arg_types="ff")
    RunEvent(13600943, slot=0, args=(73600300, 43600))
    Event13600944()
    RunEvent(13600951, slot=0, args=(3600905, 73600520, 1723))
    RunEvent(13600952, slot=0, args=(3600905, 1723, 73600530))
    RunEvent(13600953, slot=0, args=(3600905,))
    Event13600955()
    RunEvent(13600956, slot=0, args=(3600905, 1723, 73600521))
    RunEvent(13600900, slot=1, args=(3600905, 1710, 1729, 1719, 1713))
    RunEvent(13600954, slot=0, args=(1713, 73600530, 43220))


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(13600940, slot=0, args=(3600920,))
    RunEvent(13600950, slot=0, args=(3600905,))
    DisableGravity(3600201)
    DisableCharacterCollision(3600201)
    DisableGravity(3600207)
    DisableCharacterCollision(3600207)
    DisableGravity(3600212)
    DisableCharacterCollision(3600212)
    DisableGravity(3600216)
    DisableCharacterCollision(3600216)
    DisableHealthBar(3600330)
    DisableHealthBar(3600331)
    DisableHealthBar(3600332)


@RestartOnRest
def Event13604700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13604700: Event 13604700 """
    GotoIfFlagDisabled(Label.L0, arg_8_11)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(arg_4_7)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7010, loop=True)
    IfOnline(1)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_12_15)
    IfInsideMap(1, game_map=FISHING_HAMLET)
    IfCharacterHuman(2, PLAYER)
    IfPlayerLevelGreaterThanOrEqual(2, 30)
    SkipLinesIfFlagDisabled(1, arg_16_19)
    IfClientTypeCountComparison(2, ClientType.Coop, ComparisonType.GreaterThanOrEqual, value=1)
    IfCharacterHasSpecialEffect(3, PLAYER, 9025)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfRandomTimeElapsed(0, min_seconds=10.0, max_seconds=10.0)
    SkipLinesIfFlagDisabled(1, arg_16_19)
    DisplayBattlefieldMessage(109000, display_location_index=0)
    ForceAnimation(arg_0_3, 7011)
    WaitFrames(59)
    EnableAI(arg_0_3)
    EnableFlag(arg_4_7)


@RestartOnRest
def Event13604710(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13604710: Event 13604710 """
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfFlagDisabled(1, arg_12_15)
    IfFlagDisabled(1, arg_8_11)
    IfInsideMap(1, game_map=FISHING_HAMLET)
    IfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, value=0)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(2, PLAYER)
    IfRandomTimeElapsed(2, min_seconds=10.0, max_seconds=10.0)
    IfConditionTrue(0, input_condition=2)
    AddSpecialEffect(PLAYER, 9020, affect_npc_part_hp=False)
    AddSpecialEffect(arg_0_3, 9100, affect_npc_part_hp=False)
    ReplanAI(arg_0_3)
    EnableFlag(arg_12_15)
    DisplayBattlefieldMessage(100002, display_location_index=0)
    Restart()


@RestartOnRest
def Event13604720(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13604720: Event 13604720 """
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_12_15)
    IfFlagEnabled(-1, arg_8_11)
    IfClientTypeCountComparison(-1, ClientType.Invader, ComparisonType.GreaterThanOrEqual, value=1)
    IfOutsideMap(-1, game_map=FISHING_HAMLET)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    IfCharacterHuman(0, PLAYER)
    RemoveSpecialEffect(PLAYER, 9020)
    RemoveSpecialEffect(arg_0_3, 9100)
    ReplanAI(arg_0_3)
    DisableFlag(arg_12_15)
    Restart()


@RestartOnRest
def Event13604730(
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
    """ 13604730: Event 13604730 """
    IfFlagEnabled(-15, arg_8_11)
    IfFlagEnabled(-15, arg_12_15)
    IfFlagEnabled(-15, arg_16_19)
    EndIfConditionTrue(-15)
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_24_27)
    IfHealthEqual(2, arg_0_3, 0.0)
    IfFlagEnabled(-2, arg_16_19)
    IfFlagEnabled(-2, arg_28_31)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=-2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_8_11)
    GotoIfFinishedConditionTrue(Label.L0, input_condition=-2)
    EnableFlag(arg_20_23)
    Wait(5.0)
    DisplayBattlefieldMessage(109001, display_location_index=0)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, 7012)
    WaitFrames(88)
    ForceAnimation(arg_0_3, 7010)


@RestartOnRest
def Event13604740():
    """ 13604740: Event 13604740 """
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 3604000)
    IfPlayerStandingOnCollision(-1, 3604001)
    IfPlayerStandingOnCollision(-1, 3604002)
    IfPlayerStandingOnCollision(-1, 3604003)
    IfPlayerStandingOnCollision(-1, 3604004)
    IfPlayerStandingOnCollision(-1, 3604005)
    IfPlayerStandingOnCollision(-1, 3604006)
    IfPlayerStandingOnCollision(-1, 3604007)
    IfPlayerStandingOnCollision(-1, 3604008)
    IfPlayerStandingOnCollision(-1, 3604009)
    IfPlayerStandingOnCollision(-1, 3604010)
    IfPlayerStandingOnCollision(-1, 3604011)
    IfPlayerStandingOnCollision(-1, 3604012)
    IfPlayerStandingOnCollision(-1, 3604013)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604741)
    IfCharacterHuman(2, PLAYER)
    IfPlayerStandingOnCollision(-2, 3604000)
    IfPlayerStandingOnCollision(-2, 3604001)
    IfPlayerStandingOnCollision(-2, 3604002)
    IfPlayerStandingOnCollision(-2, 3604003)
    IfPlayerStandingOnCollision(-2, 3604004)
    IfPlayerStandingOnCollision(-2, 3604005)
    IfPlayerStandingOnCollision(-2, 3604006)
    IfPlayerStandingOnCollision(-2, 3604007)
    IfPlayerStandingOnCollision(-2, 3604008)
    IfPlayerStandingOnCollision(-2, 3604009)
    IfPlayerStandingOnCollision(-2, 3604010)
    IfPlayerStandingOnCollision(-2, 3604011)
    IfPlayerStandingOnCollision(-2, 3604012)
    IfPlayerStandingOnCollision(-2, 3604013)
    IfConditionFalse(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13604741)
    Restart()


@RestartOnRest
def Event13604742():
    """ 13604742: Event 13604742 """
    IfCharacterHuman(1, PLAYER)
    IfPlayerStandingOnCollision(-1, 3604020)
    IfPlayerStandingOnCollision(-1, 3604021)
    IfPlayerStandingOnCollision(-1, 3604022)
    IfPlayerStandingOnCollision(-1, 3604023)
    IfPlayerStandingOnCollision(-1, 3604024)
    IfPlayerStandingOnCollision(-1, 3604025)
    IfPlayerStandingOnCollision(-1, 3604026)
    IfPlayerStandingOnCollision(-1, 3604027)
    IfPlayerStandingOnCollision(-1, 3604028)
    IfPlayerStandingOnCollision(-1, 3604029)
    IfPlayerStandingOnCollision(-1, 3604030)
    IfPlayerStandingOnCollision(-1, 3604031)
    IfPlayerStandingOnCollision(-1, 3604032)
    IfPlayerStandingOnCollision(-1, 3604033)
    IfPlayerStandingOnCollision(-1, 3604034)
    IfPlayerStandingOnCollision(-1, 3604035)
    IfPlayerStandingOnCollision(-1, 3604110)
    IfPlayerStandingOnCollision(-1, 3604111)
    IfPlayerStandingOnCollision(-1, 3604112)
    IfPlayerStandingOnCollision(-1, 3604113)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604743)
    IfCharacterHuman(2, PLAYER)
    IfPlayerStandingOnCollision(-2, 3604020)
    IfPlayerStandingOnCollision(-2, 3604021)
    IfPlayerStandingOnCollision(-2, 3604022)
    IfPlayerStandingOnCollision(-2, 3604023)
    IfPlayerStandingOnCollision(-2, 3604024)
    IfPlayerStandingOnCollision(-2, 3604025)
    IfPlayerStandingOnCollision(-2, 3604026)
    IfPlayerStandingOnCollision(-2, 3604027)
    IfPlayerStandingOnCollision(-2, 3604028)
    IfPlayerStandingOnCollision(-2, 3604029)
    IfPlayerStandingOnCollision(-2, 3604030)
    IfPlayerStandingOnCollision(-2, 3604031)
    IfPlayerStandingOnCollision(-2, 3604032)
    IfPlayerStandingOnCollision(-2, 3604033)
    IfPlayerStandingOnCollision(-2, 3604034)
    IfPlayerStandingOnCollision(-2, 3604035)
    IfPlayerStandingOnCollision(-2, 3604110)
    IfPlayerStandingOnCollision(-2, 3604111)
    IfPlayerStandingOnCollision(-2, 3604112)
    IfPlayerStandingOnCollision(-2, 3604113)
    IfConditionFalse(2, input_condition=-2)
    IfConditionTrue(0, input_condition=2)
    DisableFlag(13604743)
    Restart()


def Event13600000():
    """ 13600000: Event 13600000 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfPlayerStandingOnCollision(0, 3604002)
    RunEvent(9350, 0, args=(4,))


def Event13600010():
    """ 13600010: Event 13600010 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.OrphanSpiritDead)
    DisableSoundEvent(3603001)
    IfPlayerStandingOnCollision(-1, 3604005)
    IfPlayerStandingOnCollision(-1, 3604007)
    IfPlayerStandingOnCollision(-1, 3604012)
    IfPlayerStandingOnCollision(-1, 3604021)
    IfPlayerStandingOnCollision(-1, 3604023)
    IfPlayerStandingOnCollision(-1, 3604026)
    IfPlayerStandingOnCollision(-1, 3604027)
    IfPlayerStandingOnCollision(-1, 3604028)
    IfPlayerStandingOnCollision(-1, 3604029)
    IfPlayerStandingOnCollision(-1, 3604030)
    IfPlayerStandingOnCollision(-1, 3604031)
    IfPlayerStandingOnCollision(-1, 3604032)
    IfPlayerStandingOnCollision(-1, 3604033)
    IfPlayerStandingOnCollision(-1, 3604034)
    IfPlayerStandingOnCollision(-1, 3604035)
    IfPlayerStandingOnCollision(-1, 3604060)
    IfConditionTrue(0, input_condition=-1)
    EnableSoundEvent(3603001)
    IfPlayerStandingOnCollision(-2, 3604005)
    IfPlayerStandingOnCollision(-2, 3604007)
    IfPlayerStandingOnCollision(-2, 3604012)
    IfPlayerStandingOnCollision(-2, 3604021)
    IfPlayerStandingOnCollision(-2, 3604023)
    IfPlayerStandingOnCollision(-2, 3604026)
    IfPlayerStandingOnCollision(-2, 3604027)
    IfPlayerStandingOnCollision(-2, 3604028)
    IfPlayerStandingOnCollision(-2, 3604029)
    IfPlayerStandingOnCollision(-2, 3604030)
    IfPlayerStandingOnCollision(-2, 3604031)
    IfPlayerStandingOnCollision(-2, 3604032)
    IfPlayerStandingOnCollision(-2, 3604033)
    IfPlayerStandingOnCollision(-2, 3604034)
    IfPlayerStandingOnCollision(-2, 3604035)
    IfPlayerStandingOnCollision(-2, 3604060)
    IfConditionFalse(0, input_condition=-2)
    Restart()


def Event13601090():
    """ 13601090: Event 13601090 """
    EndIfFlagEnabled(9468)
    DisableObject(3601090)
    IfFlagEnabled(0, 9468)
    EnableObject(3601090)


def Event13601100():
    """ 13601100: Event 13601100 """
    EndIfFlagEnabled(13604100)
    GotoIfFlagEnabled(Label.L0, 13601108)
    EnableFlag(13601106)
    EnableFlag(13601107)
    EndOfAnimation(3601100, 0)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    Goto(Label.L2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13601106)
    GotoIfConditionTrue(Label.L1, input_condition=1)
    DisableFlag(13601107)
    EndOfAnimation(3601100, 4)
    EnableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(13601107)
    EndOfAnimation(3601100, 0)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)


def Event13601101():
    """ 13601101: Event 13601101 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, 13601108)
    IfFlagEnabled(1, 13604100)
    IfConditionTrue(0, input_condition=1)
    IfFlagEnabled(2, 13601106)
    SkipLinesIfConditionTrue(2, 2)
    DisableFlag(13601107)
    SkipLines(1)
    EnableFlag(13601107)
    IfCharacterHuman(3, PLAYER)
    IfFlagEnabled(3, 13601108)
    IfFlagDisabled(3, 13604100)
    IfConditionTrue(0, input_condition=3)
    Restart()


def Event13601102():
    """ 13601102: Event 13601102 """
    IfFlagEnabled(3, 13604100)
    IfFlagEnabled(3, 13601106)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    EndOfAnimation(3601100, 6)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13601108)
    IfFlagDisabled(1, 13604100)
    IfFlagDisabled(1, 13601106)
    IfCharacterInsideRegion(-1, PLAYER, region=3602102)
    IfObjectActivated(-1, obj_act_id=13604101)
    IfFlagChange(2, 13601107)
    IfFlagEnabled(2, 13601107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604100)
    EnableFlag(13601106)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    ForceAnimation(3601100, 5, wait_for_completion=True)
    ForceAnimation(3601100, 6, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3602101)
    ForceAnimation(3601100, 7, wait_for_completion=True)
    DisableFlag(13604100)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)
    Restart()


def Event13601103():
    """ 13601103: Event 13601103 """
    IfFlagEnabled(3, 13604100)
    IfFlagDisabled(3, 13601106)
    GotoIfConditionFalse(Label.L0, input_condition=3)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    EndOfAnimation(3601100, 2)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, 13601108)
    IfFlagDisabled(1, 13604100)
    IfFlagEnabled(1, 13601106)
    IfCharacterInsideRegion(-1, PLAYER, region=3602101)
    IfObjectActivated(-1, obj_act_id=13604102)
    IfFlagChange(2, 13601107)
    IfFlagDisabled(2, 13601107)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(13604100)
    DisableFlag(13601106)
    DisableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    ForceAnimation(3601100, 1, wait_for_completion=True)
    ForceAnimation(3601100, 2, wait_for_completion=True)

    # --- 1 --- #
    DefineLabel(1)
    IfAllPlayersOutsideRegion(0, region=3602102)
    WaitFrames(1)
    ForceAnimation(3601100, 3, wait_for_completion=True)
    DisableFlag(13604100)
    EnableObjectActivation(3601101, obj_act_id=100)
    DisableObjectActivation(3601102, obj_act_id=100)
    Restart()


def Event13601104():
    """ 13601104: Event 13601104 """
    DisableNetworkSync()
    IfFlagDisabled(1, 13601108)
    IfActionButtonParamActivated(1, action_button_id=7100, entity=3601101)
    IfFlagDisabled(2, 13601108)
    IfActionButtonParamActivated(2, action_button_id=7100, entity=3601102)
    IfFlagEnabled(3, 13604100)
    IfActionButtonParamActivated(3, action_button_id=7100, entity=3601101)
    IfFlagEnabled(4, 13604100)
    IfActionButtonParamActivated(4, action_button_id=7100, entity=3601102)
    IfFlagEnabled(5, 13601106)
    IfActionButtonParamActivated(5, action_button_id=7100, entity=3601101)
    IfFlagDisabled(6, 13601106)
    IfActionButtonParamActivated(6, action_button_id=7100, entity=3601102)
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


def Event13601105():
    """ 13601105: Event 13601105 """
    EndIfFlagEnabled(13601108)
    IfCharacterInsideRegion(0, PLAYER, region=3602100)
    DisableObjectActivation(3601101, obj_act_id=100)
    EnableObjectActivation(3601102, obj_act_id=100)
    EnableFlag(13601108)


def Event13601140(_, arg_0_3: int, arg_4_7: int):
    """ 13601140: Event 13601140 """
    IfPlayerMovingOnCollision(0, arg_4_7)
    ForceAnimation(arg_0_3, 0, wait_for_completion=True)
    Restart()


def Event13601200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13601200: Event 13601200 """
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    EndOfAnimation(arg_0_3, arg_8_11)
    DisableObjectActivation(arg_0_3, obj_act_id=arg_12_15)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfObjectActivated(0, obj_act_id=arg_4_7)
    Wait(0.0)


def Event13601312():
    """ 13601312: Event 13601312 """
    GotoIfThisEventFlagDisabled(Label.L0)
    EndOfAnimation(3601305, 1)
    WaitFrames(1)
    RegisterLadder(start_climbing_flag=13601310, stop_climbing_flag=13601311, obj=3601305)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfActionButtonParamActivated(0, action_button_id=3600000, entity=3601305)
    Move(PLAYER, destination=3601305, destination_type=CoordEntityType.Object, model_point=192, short_move=True)
    ForceAnimation(PLAYER, 101330)
    ForceAnimation(3601305, 1, wait_for_completion=True)
    RegisterLadder(start_climbing_flag=13601310, stop_climbing_flag=13601311, obj=3601305)


def Event13601210(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13601210: Event 13601210 """
    DisableNetworkSync()
    EndIfFlagEnabled(arg_8_11)
    IfActionButtonParamActivated(1, action_button_id=arg_0_3, entity=arg_4_7)
    IfFlagEnabled(2, arg_8_11)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    EndIfFinishedConditionTrue(2)
    DisplayDialog(
        10010161,
        anchor_entity=-1,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Restart()


def Event13601400():
    """ 13601400: Event 13601400 """
    DisableNetworkSync()
    IfInsideMap(0, game_map=FISHING_HAMLET)
    DeleteVFX(3503120, erase_root_only=True)


@RestartOnRest
def Event13604400(_, arg_0_3: int):
    """ 13604400: Event 13604400 """
    EndIfThisEventSlotFlagEnabled()
    RestoreObject(arg_0_3)
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
        owner_entity=3600799,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)
    End()

    # --- 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6310,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=arg_0_3,
        model_point=-1,
        behavior_id=6320,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    DestroyObject(arg_0_3)
    PlaySoundEffect(anchor_entity=arg_0_3, sound_type=SoundType.o_Object, sound_id=299961000)


def OrphanDies():
    """ 13601800: Event 13601800 """
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(Characters.Orphan)
    DisableCharacter(Characters.OrphanWinged)
    Kill(Characters.Orphan, award_souls=False)
    Kill(Characters.OrphanWinged, award_souls=False)
    DisableObject(Objects.OrphanFog1)
    DeleteVFX(VFX.OrphanFog1, erase_root_only=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterDead(1, Characters.Orphan)
    IfCharacterDead(2, Characters.OrphanWinged)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(0, input_condition=-1)
    DisplayBanner(BannerType.PreySlaughtered)
    DisableObject(Objects.OrphanFog1)
    DisableObject(Objects.OrphanFog2)
    DeleteVFX(VFX.OrphanFog1, erase_root_only=True)
    DeleteVFX(VFX.OrphanFog2, erase_root_only=True)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Wait(3.0)
    SkipLinesIfFinishedConditionTrue(2, 2)
    KillBoss(Characters.Orphan)
    SkipLines(1)
    KillBoss(Characters.OrphanWinged)
    DisableNetworkSync()
    GotoIfClient(Label.L1)
    IfCharacterHuman(0, PLAYER)
    AwardAchievement(35)
    RunEvent(9350, 0, args=(5,))
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

    # --- 1 --- #
    DefineLabel(1)
    IfCharacterType(0, PLAYER, CharacterType.WhitePhantom)
    Wait(0.0)


def OrphanFirstTimeTrigger():
    """ 13604811: Event 13604811 """
    EndIfFlagEnabled(Flags.OrphanDead)
    EndIfFlagEnabled(Flags.OrphanFirstTimeDone)
    DisableCharacter(Characters.Orphan)
    IfFlagDisabled(1, Flags.OrphanDead)
    IfFlagDisabled(1, Flags.OrphanFirstTimeDone)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(1, PLAYER, region=3602805)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfClient(1)
    NotifyBossBattleStart()
    EnableFlag(13604810)
    IfCharacterType(2, PLAYER, CharacterType.BlackPhantom)
    EndIfConditionTrue(2)
    DeleteVFX(3603860, erase_root_only=True)
    EnableFlag(CommonFlags.CutsceneActive)


def OrphanFirstTimeCutscene():
    """ 13601801: Event 13601801 """
    EndIfFlagEnabled(Flags.OrphanDead)
    EndIfThisEventFlagEnabled()
    IfCharacterType(1, PLAYER, CharacterType.BlackPhantom)
    GotoIfConditionTrue(Label.L0, input_condition=1)
    IfFlagDisabled(2, Flags.OrphanDead)
    IfThisEventFlagDisabled(2)
    IfFlagEnabled(2, 13604811)
    IfCharacterHuman(2, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=3602805)
    IfConditionTrue(0, input_condition=2)
    SkipLinesIfMultiplayer(2)
    PlayCutscene(Cutscenes.OrphanBirth, skippable=True, fade_out=False, player_id=PLAYER)
    SkipLines(1)
    PlayCutscene(Cutscenes.OrphanBirth, skippable=False, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableFlag(CommonFlags.CutsceneActive)
    CreateVFX(3603860)
    EnableFlag(Flags.OrphanFogEntered)
    EnableCharacter(Characters.Orphan)
    EndIfFlagEnabled(9347)
    RunEvent(9350, 0, args=(5,))
    EnableFlag(9347)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, 6001)
    Wait(0.0)


def ControlOrphanSpirit():
    """ 13601802: Event 13601802 """
    DisableAI(Characters.OrphanSpirit)
    DisableHealthBar(Characters.OrphanSpirit)
    DisableGravity(Characters.OrphanSpirit)
    IfCharacterBackreadEnabled(0, Characters.OrphanSpirit)
    Move(Characters.OrphanSpirit, destination=Objects.KosCorpse, model_point=100, short_move=True)
    ForceAnimation(Characters.OrphanSpirit, 7000, loop=True)
    EndIfFlagEnabled(Flags.OrphanSpiritDead)
    GotoIfThisEventFlagDisabled(Label.L0)
    ForceAnimation(Characters.OrphanSpirit, 0, loop=True)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(0, Flags.OrphanDead)
    ForceAnimation(Characters.OrphanSpirit, 7001)


def OrphanSpiritDies():
    """ 13601803: Trigger banner, cutscene, and moon swap when Orphan's immobile spirit is killed. """
    GotoIfThisEventFlagEnabled(Label.L0)
    DisableObject(Objects.MoonOrphanDead)
    IfCharacterDead(0, Characters.OrphanSpirit)
    DisplayBanner(BannerType.NightmareSlain)
    Wait(5.0)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)

    # --- 0 --- #
    DefineLabel(0)
    DisableSoundEvent(3603000)
    DisableSoundEvent(3603001)
    DeleteVFX(3603810, erase_root_only=True)
    DeleteVFX(3603811, erase_root_only=True)
    DeleteVFX(3603812, erase_root_only=True)
    DeleteVFX(3603813, erase_root_only=True)
    DeleteVFX(3603814, erase_root_only=True)
    DeleteVFX(3603815, erase_root_only=True)
    DeleteVFX(3603816, erase_root_only=True)
    DeleteVFX(3603817, erase_root_only=True)
    DeleteVFX(3603818, erase_root_only=True)
    DeleteVFX(3603819, erase_root_only=True)
    DeleteVFX(3603820, erase_root_only=True)
    DeleteVFX(3603821, erase_root_only=True)
    DeleteVFX(3603822, erase_root_only=True)
    DeleteVFX(3603823, erase_root_only=True)
    DeleteVFX(3603824, erase_root_only=True)
    DeleteVFX(3603825, erase_root_only=True)
    DeleteVFX(3603826, erase_root_only=True)
    DeleteVFX(3603827, erase_root_only=True)
    DeleteVFX(3603828, erase_root_only=True)
    DeleteVFX(3603829, erase_root_only=True)
    DeleteVFX(3603830, erase_root_only=True)
    DeleteVFX(3603831, erase_root_only=True)
    DeleteVFX(3603832, erase_root_only=True)
    DeleteVFX(3603840, erase_root_only=True)
    DeleteVFX(3603841, erase_root_only=True)
    DeleteVFX(3603842, erase_root_only=True)
    DeleteVFX(3603843, erase_root_only=True)
    DeleteVFX(3603844, erase_root_only=True)
    DeleteVFX(3603845, erase_root_only=True)
    DeleteVFX(3603846, erase_root_only=True)
    DeleteVFX(3603847, erase_root_only=True)
    DeleteVFX(3603848, erase_root_only=True)
    DeleteVFX(3603849, erase_root_only=True)
    DeleteVFX(3603850, erase_root_only=True)
    DeleteVFX(3603851, erase_root_only=True)
    DeleteVFX(3603852, erase_root_only=True)
    DeleteVFX(3603860, erase_root_only=True)
    DeleteVFX(3603870, erase_root_only=True)
    DeleteVFX(3603871, erase_root_only=True)
    DeleteVFX(3603872, erase_root_only=True)
    DeleteVFX(3603873, erase_root_only=True)
    DeleteVFX(3603874, erase_root_only=True)
    SkipLinesIfThisEventFlagDisabled(2)
    DisableObject(Objects.MoonOrphanAlive)
    EnableObject(Objects.MoonOrphanDead)
    EndIfThisEventFlagEnabled()
    EnableFlag(CommonFlags.CutsceneActive)
    PlayCutscene(Cutscenes.OrphanSpiritDeath, skippable=True, fade_out=False, player_id=PLAYER)
    WaitFrames(1)
    DisableObject(Objects.MoonOrphanAlive)
    EnableObject(Objects.MoonOrphanDead)
    DisableFlag(CommonFlags.CutsceneActive)
    EnableFlag(9469)
    RunEvent(9350, 0, args=(3,))


def SummonStartOrphanBattle():
    """ 13601804: Event 13601804 """
    IfCharacterHuman(1, PLAYER)
    IfFlagEnabled(1, Flags.OrphanFogEntered)
    IfConditionTrue(0, input_condition=1)
    EndIfHost()
    EnableCharacter(Characters.Orphan)
    EnableFlag(Flags.OrphanFogEntered)
    EnableFlag(Flags.OrphanFirstTimeDone)


def EnterOrphanFog():
    """ 13604800: Event 13604800 """
    EndIfFlagEnabled(Flags.OrphanDead)
    GotoIfFlagEnabled(Label.L0, Flags.OrphanFirstTimeDone)
    SkipLinesIfClient(2)
    DisableObject(Objects.OrphanFog1)
    DeleteVFX(VFX.OrphanFog1, erase_root_only=False)
    IfFlagDisabled(1, Flags.OrphanDead)
    IfFlagEnabled(1, Flags.OrphanFirstTimeDone)
    IfConditionTrue(0, input_condition=1)
    EnableObject(Objects.OrphanFog1)
    EnableObject(Objects.OrphanFog2)
    CreateVFX(VFX.OrphanFog1)
    CreateVFX(VFX.OrphanFog2)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.OrphanDead)
    IfCharacterHuman(2, PLAYER)
    IfActionButtonParamActivated(2, action_button_id=3600800, entity=Objects.OrphanFog1)
    IfFlagEnabled(3, Flags.OrphanDead)
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
    EnableFlag(Flags.OrphanFogEntered)
    Restart()


def EnterOrphanFogAsSummon():
    """ 13604801: Event 13604801 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.OrphanDead)
    IfFlagDisabled(1, Flags.OrphanDead)
    IfFlagEnabled(1, Flags.OrphanFirstTimeDone)
    IfFlagEnabled(1, Flags.OrphanFogEntered)
    IfCharacterType(1, PLAYER, CharacterType.WhitePhantom)
    IfActionButtonParamActivated(1, action_button_id=3600800, entity=Objects.OrphanFog1)
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


def StartOrphanBattle():
    """ 13604802: Event 13604802 """
    EndIfFlagEnabled(Flags.OrphanDead)
    DisableAI(Characters.Orphan)
    DisableAI(Characters.OrphanWinged)
    DisableHealthBar(Characters.Orphan)
    DisableHealthBar(Characters.OrphanWinged)
    ReferDamageToEntity(Characters.Orphan, Characters.OrphanWinged)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagEnabled(0, Flags.OrphanFogEntered)
    GotoIfClient(Label.L0)
    SkipLinesIfFlagEnabled(1, 13604810)
    NotifyBossBattleStart()
    SetNetworkUpdateAuthority(Characters.Orphan, UpdateAuthority.Forced)
    SetNetworkUpdateAuthority(Characters.OrphanWinged, UpdateAuthority.Forced)

    # --- 0 --- #
    DefineLabel(0)
    EnableFlag(13604810)
    EnableFlag(Flags.OrphanFogEntered)
    GotoIfCoopClientCountComparison(Label.L1, ComparisonType.Equal, 0)
    GotoIfCoopClientCountComparison(Label.L2, ComparisonType.Equal, 1)
    GotoIfCoopClientCountComparison(Label.L3, ComparisonType.Equal, 2)

    # --- 1 --- #
    DefineLabel(1)
    Goto(Label.L4)

    # --- 2 --- #
    DefineLabel(2)
    AddSpecialEffect(Characters.Orphan, 7500, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.OrphanWinged, 7500, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Orphan)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OrphanWinged)
    Goto(Label.L4)

    # --- 3 --- #
    DefineLabel(3)
    AddSpecialEffect(Characters.Orphan, 7501, affect_npc_part_hp=True)
    AddSpecialEffect(Characters.OrphanWinged, 7501, affect_npc_part_hp=True)
    WaitFrames(1)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.Orphan)
    AdaptSpecialEffectHealthChangeToNPCPart(Characters.OrphanWinged)
    Goto(Label.L4)

    # --- 4 --- #
    DefineLabel(4)
    EnableBossHealthBar(Characters.OrphanWinged, name=453000, slot=0)
    EnableFlag(13604812)
    GotoIfThisEventFlagEnabled(Label.L5)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfEntityWithinDistance(-2, PLAYER, Characters.Orphan, radius=24.0)
    IfAttackedWithDamageType(-2, attacked_entity=Characters.Orphan, attacker=-1)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)

    # --- 5 --- #
    DefineLabel(5)
    SkipLinesIfFlagEnabled(4, 13604820)
    EnableAI(Characters.Orphan)
    SetNetworkUpdateRate(Characters.Orphan, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(Characters.OrphanWinged, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SkipLines(3)
    EnableAI(Characters.OrphanWinged)
    SetNetworkUpdateRate(Characters.Orphan, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(Characters.OrphanWinged, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    CreatePlayLog(42)
    StartPlayLogMeasurement(3600010, 58, overwrite=True)


def ControlOrphanMusic():
    """ 13604803: Event 13604803 """
    DisableNetworkSync()
    DisableSoundEvent(3603802)
    DisableSoundEvent(3603803)
    EndIfFlagEnabled(Flags.OrphanDead)
    GotoIfThisEventFlagEnabled(Label.L0)
    IfFlagDisabled(1, Flags.OrphanDead)
    IfFlagEnabled(1, 13604812)
    SkipLinesIfHost(1)
    IfFlagEnabled(1, 13604809)
    IfCharacterInsideRegion(1, PLAYER, region=3602802)
    IfConditionTrue(0, input_condition=1)
    EnableBossMusic(3603802)
    IfFlagEnabled(2, Flags.OrphanPhaseTwo)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagDisabled(2, Flags.OrphanDead)
    IfFlagEnabled(2, 13604812)
    SkipLinesIfHost(1)
    IfFlagEnabled(2, 13604809)
    IfCharacterInsideRegion(2, PLAYER, region=3602802)
    IfConditionTrue(0, input_condition=2)
    DisableBossMusic(3603802)
    WaitFrames(0)
    EnableBossMusic(3603803)


def ControlOrphanCamera():
    """ 13604804: Event 13604804 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.OrphanDead)
    GotoIfFlagEnabled(Label.L0, Flags.OrphanPhaseTwo)
    IfCharacterAlive(1, Characters.Orphan)
    IfEntityWithinDistance(1, PLAYER, Characters.Orphan, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(2, Characters.Orphan)
    IfEntityBeyondDistance(2, PLAYER, Characters.Orphan, radius=12.5)
    IfConditionTrue(0, input_condition=2)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    IfCharacterAlive(3, Characters.Orphan)
    IfEntityWithinDistance(3, PLAYER, Characters.OrphanWinged, radius=12.0)
    IfConditionTrue(0, input_condition=3)
    SetLockedCameraSlot(game_map=HUNTERS_NIGHTMARE, camera_slot=1)
    IfCharacterAlive(4, Characters.Orphan)
    IfEntityBeyondDistance(4, PLAYER, Characters.OrphanWinged, radius=12.5)
    IfConditionTrue(0, input_condition=4)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()


def StopOrphanMusic():
    """ 13604805: Event 13604805 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.OrphanDead)
    IfFlagEnabled(0, Flags.OrphanDead)
    DisableBossMusic(3603802)
    DisableBossMusic(3603803)
    DisableBossMusic(-1)


def Event13604806():
    """ 13604806: Event 13604806 """
    IfCharacterHuman(1, PLAYER)
    IfEntityWithinDistance(1, PLAYER, Objects.OrphanFog1, radius=6.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, False)
    WaitFrames(6)
    Restart()


def Event13604807():
    """ 13604807: Event 13604807 """
    IfCharacterHuman(1, PLAYER)
    IfEntityBeyondDistance(1, PLAYER, Objects.OrphanFog1, radius=6.0)
    IfEntityWithinDistance(1, PLAYER, Objects.OrphanFog1, radius=12.0)
    IfConditionTrue(0, input_condition=1)
    SetGravityAndCollisionExcludingOwnWorld(PLAYER, True)
    WaitFrames(6)
    Restart()


def OrphanPhaseTwoTrigger():
    """ 13604820: Event 13604820 """
    EndIfFlagEnabled(Flags.OrphanDead)
    GotoIfThisEventFlagDisabled(Label.L0)
    DisableCharacter(Characters.Orphan)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(Characters.OrphanWinged)
    IfHealthLessThan(0, Characters.Orphan, 0.5)
    AICommand(Characters.Orphan, command_id=100, slot=0)
    ReplanAI(Characters.Orphan)
    IfCharacterHasTAEEvent(0, Characters.Orphan, tae_event_id=100)
    DisableCharacter(Characters.Orphan)
    EnableGravity(Characters.OrphanWinged)
    SetNetworkUpdateRate(Characters.Orphan, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    SetNetworkUpdateRate(Characters.OrphanWinged, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        Characters.OrphanWinged,
        destination=Characters.Orphan,
        destination_type=CoordEntityType.Character,
        model_point=203,
        copy_draw_parent=Characters.Orphan,
    )
    ForceAnimation(Characters.OrphanWinged, 3031)
    IfCharacterHasTAEEvent(0, Characters.OrphanWinged, tae_event_id=50)
    RemoveSpecialEffect(Characters.OrphanWinged, 5300)
    AddSpecialEffect(Characters.OrphanWinged, 5333, affect_npc_part_hp=False)
    EnableAI(Characters.OrphanWinged)


def OrphanPhaseTwoLightning():
    """ 13604830: Event 13604830 """
    EndIfFlagEnabled(Flags.OrphanDead)
    IfCharacterHasTAEEvent(0, Characters.OrphanWinged, tae_event_id=100)
    AICommand(3600803, command_id=10, slot=0)
    ReplanAI(3600803)
    IfCharacterHasSpecialEffect(0, 3600803, 5020)
    AICommand(3600803, command_id=20, slot=0)
    ReplanAI(3600803)
    IfCharacterHasTAEEvent(0, 3600803, tae_event_id=10)
    AICommand(3600803, command_id=-1, slot=0)
    RemoveSpecialEffect(3600803, 5020)
    ReplanAI(3600803)
    Restart()


def ApplyOrphanCrushEffect():
    """ 13604840: Combination of TAE events and existing player effect 8055 gives the player effect 8054.

    I can't find any Orphan attacks that give the player either of these effects, and can't find TAE events 30 or 40
    (though I may be missing them), and I have no knowledge of any Orphan attacks that affect player healing like effect
    8054 seems to do. So I suspect this was cut.
    """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.OrphanDead)

    IfCharacterHasTAEEvent(1, Characters.Orphan, tae_event_id=30)
    IfCharacterHasSpecialEffect(1, PLAYER, 8055)
    IfConditionTrue(0, input_condition=1)

    AddSpecialEffect(PLAYER, 8054, affect_npc_part_hp=False)

    IfCharacterHasTAEEvent(-1, Characters.Orphan, tae_event_id=40)
    IfTimeElapsed(-1, 4.5)
    IfEntityBeyondDistance(-1, Characters.Orphan, PLAYER, radius=20.0)
    IfConditionTrue(0, input_condition=-1)

    RemoveSpecialEffect(PLAYER, 8054)

    Restart()


def ControlOrphanPhaseTwoLightningCamera():
    """ 13604850: Event 13604850 """
    DisableNetworkSync()
    EndIfFlagEnabled(Flags.OrphanDead)
    IfCharacterHasSpecialEffect(0, Characters.OrphanWinged, 5036)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=1)
    IfCharacterDoesNotHaveSpecialEffect(0, Characters.OrphanWinged, 5036)
    SetLockedCameraSlot(game_map=FISHING_HAMLET, camera_slot=0)
    Restart()


@RestartOnRest
def Event13605200(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: float, arg_20_23: int):
    """ 13605200: Event 13605200 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    Wait(arg_16_19)

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfValueEqual(1, left=arg_20_23, right=0)
    AddSpecialEffect(arg_0_3, 5000, affect_npc_part_hp=False)
    ChangePatrolBehavior(arg_0_3, patrol_information_id=arg_12_15)
    ReplanAI(arg_0_3)


@RestartOnRest
def Event13605400(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: float,
    arg_28_31: float,
):
    """ 13605400: Event 13605400 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=arg_24_27, max_seconds=arg_28_31)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event13605480(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: float,
    arg_28_31: int,
):
    """ 13605480: Event 13605480 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableAI(arg_0_3)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    Wait(arg_24_27)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)
    WaitFrames(arg_28_31)

    # --- 0 --- #
    DefineLabel(0)
    EnableAI(arg_0_3)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event13605490(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: float,
    arg_28_31: float,
):
    """ 13605490: Event 13605490 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfHasAIStatus(-1, arg_20_23, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_20_23, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=4.0)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=arg_24_27, max_seconds=arg_28_31)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event13605500(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: float,
    arg_28_31: float,
):
    """ 13605500: Event 13605500 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    ForceAnimation(arg_0_3, arg_4_7, loop=True)
    SetAIParamID(arg_0_3, arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    IfCharacterInsideRegion(1, PLAYER, region=arg_20_23)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    WaitRandomSeconds(min_seconds=arg_24_27, max_seconds=arg_28_31)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_12_15, wait_for_completion=False)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event13605520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 13605520: Event 13605520 """
    IfAllPlayersOutsideRegion(1, region=arg_4_7)
    IfConditionFalse(0, input_condition=1)
    SetAIParamID(arg_0_3, arg_8_11)
    IfAllPlayersOutsideRegion(0, region=arg_4_7)
    SetAIParamID(arg_0_3, arg_12_15)
    Restart()


@RestartOnRest
def Event13605540(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: int, arg_16_19: int):
    """ 13605540: Event 13605540 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    SetAIParamID(arg_0_3, arg_12_15)
    IfCharacterInsideRegion(1, arg_0_3, region=arg_4_7)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(2, input_condition=-1)
    IfEntityWithinDistance(2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(arg_0_3, arg_16_19)


@RestartOnRest
def Event13605560(_, arg_0_3: int, arg_4_7: int, arg_8_11: float):
    """ 13605560: Event 13605560 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(-2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(-2, PLAYER, arg_0_3, radius=arg_8_11)
    IfConditionTrue(1, input_condition=-2)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-3, input_condition=1)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    EnableAI(arg_0_3)


@RestartOnRest
def Event13605600(_, arg_0_3: int, arg_4_7: int):
    """ 13605600: Event 13605600 """
    DisableGravity(arg_4_7)
    SkipLinesIfThisEventSlotFlagEnabled(2)
    IfCharacterBackreadEnabled(0, arg_0_3)
    Wait(1.0)
    IfHealthLessThanOrEqual(1, arg_0_3, 0.0)
    SkipLinesIfConditionFalse(2, 1)
    DisableBackread(arg_4_7)
    End()
    Move(
        arg_4_7,
        destination=arg_0_3,
        destination_type=CoordEntityType.Character,
        model_point=100,
        set_draw_parent=arg_0_3,
    )
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

    # --- 0 --- #
    DefineLabel(0)
    AddSpecialEffect_WithUnknownEffect(PLAYER, 4691, affect_npc_parts_hp=False)
    Restart()


@RestartOnRest
def Event13605606():
    """ 13605606: Event 13605606 """
    DisableNetworkSync()
    IfCharacterDoesNotHaveSpecialEffect(1, PLAYER, 4690)
    IfCharacterHasSpecialEffect(1, PLAYER, 4691)
    IfConditionTrue(0, input_condition=1)
    RemoveSpecialEffect(PLAYER, 4691)
    Restart()


@RestartOnRest
def Event13605700(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13605700: Event 13605700 """
    GotoIfFlagEnabled(Label.L0, arg_8_11)
    DisableFlag(arg_8_11)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, arg_0_3, ai_status=AIStatusType.Battle)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(arg_8_11)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=arg_4_7, wait_for_completion=True)

    # --- 0 --- #
    DefineLabel(0)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Normal)
    Restart()


@RestartOnRest
def Event13605720(_, arg_0_3: int):
    """ 13605720: Event 13605720 """
    IfCharacterHasTAEEvent(0, arg_0_3, tae_event_id=100)
    MoveObjectToCharacter(3601799, character=PLAYER, model_point=-1)
    WaitFrames(1)
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=3601799,
        model_point=200,
        behavior_id=6300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
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
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=3601798,
        model_point=200,
        behavior_id=6330,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    IfCharacterOutsideRegion(0, PLAYER, region=3602798)
    Restart()


@RestartOnRest
def Event13605740(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: float):
    """ 13605740: Event 13605740 """
    EndIfThisEventFlagEnabled()
    DisableAI(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(2, PLAYER, region=arg_4_7)
    IfEntityWithinDistance(3, PLAYER, arg_0_3, radius=arg_12_15)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, 3)
    SetCharacterEventTarget(arg_0_3, arg_8_11)
    AICommand(arg_0_3, command_id=100, slot=0)
    EnableAI(arg_0_3)
    WaitFrames(60)
    AICommand(arg_0_3, command_id=-1, slot=0)


@RestartOnRest
def Event13605750():
    """ 13605750: Event 13605750 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DisableGravity(3600201)
    DisableCharacterCollision(3600201)
    ForceAnimation(3600201, 7006, loop=True)
    SetAIParamID(3600201, 404003)
    IfHasAIStatus(-1, 3600201, ai_status=AIStatusType.Caution)
    IfHasAIStatus(-1, 3600201, ai_status=AIStatusType.Battle)
    IfCharacterHuman(-2, PLAYER)
    IfCharacterType(-2, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-2)
    SkipLinesIfFlagEnabled(2, 53600100)
    IfEntityWithinDistance(1, PLAYER, 3600201, radius=12.0)
    SkipLines(1)
    IfCharacterInsideRegion(1, PLAYER, region=3602201)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    RotateToFaceEntity(3600201, PLAYER, animation=7007, wait_for_completion=False)
    EnableGravity(3600201)
    EnableCharacterCollision(3600201)

    # --- 0 --- #
    DefineLabel(0)
    SetAIParamID(3600201, 404000)


@RestartOnRest
def Event13605751():
    """ 13605751: Event 13605751 """
    IfCharacterHasTAEEvent(0, 3600330, tae_event_id=100)
    SetAIParamID(3600208, 404002)
    SetAIParamID(3600209, 404002)
    MoveObjectToCharacter(3601799, character=PLAYER, model_point=-1)
    WaitFrames(1)
    ShootProjectile(
        owner_entity=3600799,
        projectile_id=3601799,
        model_point=200,
        behavior_id=6300,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )


@RestartOnRest
def Event13605752():
    """ 13605752: Event 13605752 """
    EndIfThisEventFlagEnabled()
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3602315)
    IfAttackedWithDamageType(2, attacked_entity=3600315, attacker=-1)
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
    EndIfThisEventFlagEnabled()
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
    EndIfThisEventFlagEnabled()
    DisableAI(3600303)
    ForceAnimation(3600303, 7004, loop=True)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=3602304)
    IfHealthLessThan(1, 3600302, 0.5)
    IfHealthLessThan(2, 3600302, 0.4000000059604645)
    IfAttackedWithDamageType(3, attacked_entity=3600303, attacker=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(-2, input_condition=3)
    IfConditionTrue(0, input_condition=-2)
    ForceAnimation(3600303, 7005)
    EnableAI(3600303)


@RestartOnRest
def Event13605762():
    """ 13605762: Event 13605762 """
    EndIfFlagEnabled(53600800)
    IfCharacterHuman(1, PLAYER)
    EndIfConditionFalse(1)
    IfCharacterDead(2, 3600302)
    IfCharacterDead(2, 3600303)
    IfConditionTrue(0, input_condition=2)
    AwardItemLot(3601100, host_only=True)


@RestartOnRest
def Event13605770(_, arg_0_3: int, arg_4_7: int, arg_8_11: float, arg_12_15: float):
    """ 13605770: Event 13605770 """
    EndIfThisEventSlotFlagEnabled()
    DisableAI(arg_0_3)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    IfCharacterHuman(-1, PLAYER)
    IfCharacterType(-1, PLAYER, CharacterType.WhitePhantom)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterInsideRegion(1, PLAYER, region=arg_4_7)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=-1)
    IfConditionTrue(-2, input_condition=1)
    IfConditionTrue(-2, input_condition=2)
    IfConditionTrue(0, input_condition=-2)
    WaitRandomSeconds(min_seconds=arg_8_11, max_seconds=arg_12_15)
    EnableAI(arg_0_3)
    EnableGravity(arg_0_3)
    EnableCharacterCollision(arg_0_3)


@RestartOnRest
def Event13605799():
    """ 13605799: Event 13605799 """
    CreateProjectileOwner(3600799)


@RestartOnRest
def Event13605900(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13605900: Event 13605900 """
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_4_7)
    IfFlagDisabled(1, 1730)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfFlagDisabled(1, arg_20_23)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)


@RestartOnRest
def Event13605910(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13605910: Event 13605910 """
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(arg_8_11)
    EndIfFlagEnabled(arg_4_7)
    IfFlagDisabled(1, 1730)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfFlagEnabled(1, arg_0_3)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=10306)
    WaitRandomSeconds(min_seconds=2.0, max_seconds=4.0)
    Restart()


@RestartOnRest
def Event13605920(
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
    """ 13605920: Event 13605920 """
    AICommand(arg_0_3, command_id=30, slot=0)
    ReplanAI(arg_0_3)
    EnableInvincibility(arg_0_3)
    DisableAnimations(arg_0_3)
    AddSpecialEffect(arg_0_3, 5560, affect_npc_part_hp=False)
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(arg_8_11)
    GotoIfFlagEnabled(Label.L0, arg_4_7)
    IfFlagDisabled(1, 1730)
    IfFlagEnabled(1, arg_20_23)
    IfFlagDisabled(1, arg_8_11)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    Move(arg_0_3, destination=arg_28_31, destination_type=CoordEntityType.Region, short_move=True)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    DisableInvincibility(arg_0_3)
    EnableAnimations(arg_0_3)
    RemoveSpecialEffect(arg_0_3, 5560)
    AddSpecialEffect(arg_0_3, 8060, affect_npc_part_hp=False)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    ForceAnimation(arg_0_3, 101203)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    DisableInvincibility(arg_0_3)
    EnableAnimations(arg_0_3)
    RemoveSpecialEffect(arg_0_3, 5560)
    EnableFlag(arg_4_7)
    DisableFlag(arg_24_27)
    IfFlagEnabled(0, arg_24_27)
    Restart()


@RestartOnRest
def Event13605921(
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
    """ 13605921: Event 13605921 """
    AICommand(arg_0_3, command_id=30, slot=0)
    ReplanAI(arg_0_3)
    EnableInvincibility(arg_0_3)
    DisableAnimations(arg_0_3)
    AddSpecialEffect(arg_0_3, 5560, affect_npc_part_hp=False)
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(arg_8_11)
    GotoIfFlagEnabled(Label.L0, arg_4_7)
    IfFlagDisabled(1, 1730)
    IfFlagEnabled(1, arg_20_23)
    IfFlagDisabled(1, arg_8_11)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(2, PLAYER, region=arg_12_15)
    IfConditionTrue(-1, input_condition=2)
    IfCharacterInsideRegion(3, PLAYER, region=arg_16_19)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFinishedConditionTrue(2, 3)
    Move(
        arg_0_3, destination=arg_28_31, destination_type=CoordEntityType.Region, set_draw_parent=3604027
    )
    SkipLines(1)
    Move(arg_0_3, destination=3602917, destination_type=CoordEntityType.Region, set_draw_parent=3604027)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    DisableInvincibility(arg_0_3)
    EnableAnimations(arg_0_3)
    RemoveSpecialEffect(arg_0_3, 5560)
    AddSpecialEffect(arg_0_3, 8060, affect_npc_part_hp=False)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=777777777)
    ForceAnimation(arg_0_3, 101203)

    # --- 0 --- #
    DefineLabel(0)
    AICommand(arg_0_3, command_id=-1, slot=0)
    ReplanAI(arg_0_3)
    DisableInvincibility(arg_0_3)
    EnableAnimations(arg_0_3)
    RemoveSpecialEffect(arg_0_3, 5560)
    EnableFlag(arg_4_7)
    DisableFlag(arg_24_27)
    IfFlagEnabled(0, arg_24_27)
    Restart()


@RestartOnRest
def Event13605930(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 13605930: Event 13605930 """
    EndIfFlagEnabled(1730)
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfCharacterHuman(1, PLAYER)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_12_15)
    IfCharacterInsideRegion(-1, PLAYER, region=arg_16_19)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    AICommand(arg_0_3, command_id=30, slot=0)
    ReplanAI(arg_0_3)
    Wait(2.0)
    EnableInvincibility(arg_0_3)
    DisableAnimations(arg_0_3)
    AddSpecialEffect(arg_0_3, 5560, affect_npc_part_hp=False)
    RemoveSpecialEffect(arg_0_3, 8060)
    RemoveSpecialEffect(arg_0_3, 1130)
    RemoveSpecialEffect(arg_0_3, 1150)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=122)
    Wait(4.0)
    EnableFlag(arg_20_23)
    DisableFlag(arg_4_7)
    IfFlagEnabled(0, arg_4_7)
    Restart()


@RestartOnRest
def Event13605940(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13605940: Event 13605940 """
    DisableBackread(arg_16_19)
    GotoIfFlagDisabled(Label.L0, 1730)
    DropMandatoryTreasure(arg_16_19)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EndIfFlagEnabled(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    RemoveSpecialEffect(arg_0_3, 8060)
    RemoveSpecialEffect(arg_0_3, 1130)
    RemoveSpecialEffect(arg_0_3, 1150)
    PlaySoundEffect(anchor_entity=PLAYER, sound_type=SoundType.s_SFX, sound_id=122)
    EnableFlag(arg_8_11)
    IfCharacterHuman(2, PLAYER)
    SkipLinesIfConditionFalse(1, 2)
    AwardItemLot(arg_12_15, host_only=True)


def Event13600900(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 13600900: Event 13600900 """
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    EndIfFlagRangeAnyEnabled((arg_4_7, arg_12_15))
    IfCharacterDead(1, arg_0_3)
    IfConditionTrue(-1, input_condition=1)
    IfConditionTrue(0, input_condition=-1)
    DisableFlagRange((arg_4_7, arg_8_11))
    EnableFlag(arg_16_19)
    SaveRequest()


def Event13600940(_, arg_0_3: int):
    """ 13600940: Event 13600940 """
    IfCharacterHuman(15, PLAYER)
    GotoIfConditionFalse(Label.L0, input_condition=15)
    DisableFlagRange((1770, 1789))
    EnableFlag(1780)

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L0, 1770)
    GotoIfFlagEnabled(Label.L1, 1780)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)

    # --- 1 --- #
    DefineLabel(1)
    DisableFlag(73600310)
    DisableFlag(73600314)
    EnableBackread(arg_0_3)
    EnableCharacter(arg_0_3)
    EnableImmortality(arg_0_3)
    SetDistanceLimitForConversationStateChanges(arg_0_3, distance=35.0)
    End()


def Event13600943(_, arg_0_3: int, arg_4_7: int):
    """ 13600943: Event 13600943 """
    EndIfFlagEnabled(arg_0_3)
    IfCharacterHuman(15, PLAYER)
    EndIfConditionFalse(15)
    IfFlagEnabled(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)


def Event13600941(_, arg_0_3: int, arg_4_7: int):
    """ 13600941: Event 13600941 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagDisabled(-1, arg_0_3)
    IfFlagEnabled(-1, arg_4_7)
    IfConditionTrue(0, input_condition=-1)
    IfFlagEnabled(1, arg_0_3)
    IfFlagDisabled(1, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    Restart()


def Event13600942(_, arg_0_3: float, arg_4_7: float):
    """ 13600942: Event 13600942 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagEnabled(0, 73600310)
    WaitRandomSeconds(min_seconds=arg_0_3, max_seconds=arg_4_7)
    SkipLinesIfFlagDisabled(3, 73600313)
    IfFlagDisabled(0, 73600314)
    DisableFlag(73600313)
    Restart()
    DisableFlag(73600310)
    Restart()


def Event13600944():
    """ 13600944: Event 13600944 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(73600318)
    IfCharacterInsideRegion(0, PLAYER, region=3602941)
    EnableFlag(73600318)
    IfCharacterOutsideRegion(0, PLAYER, region=3602941)
    Restart()


def Event13600950(_, arg_0_3: int):
    """ 13600950: Event 13600950 """
    IfCharacterHuman(-15, PLAYER)
    GotoIfConditionFalse(Label.L8, input_condition=-15)
    GotoIfFlagRangeState(Label.L0, RangeState.AnyOn, FlagType.Absolute, (1710, 1729))
    DisableFlagRange((1710, 1729))
    EnableFlag(1720)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagRangeAnyEnabled(1, (1720, 1722))
    IfFlagEnabled(1, 73400403)
    IfFlagEnabled(1, 1650)
    GotoIfConditionFalse(Label.L1, input_condition=1)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(2, 1722)
    IfFlagEnabled(-2, 1660)
    IfFlagEnabled(-2, 1651)
    IfConditionTrue(2, input_condition=-2)
    IfFlagEnabled(2, 73500602)
    GotoIfConditionFalse(Label.L2, input_condition=2)
    DisableFlagRange((1710, 1729))
    EnableFlag(1723)

    # --- 2 --- #
    DefineLabel(2)
    IfFlagEnabled(3, 1723)
    IfFlagEnabled(3, 73600501)
    GotoIfConditionFalse(Label.L3, input_condition=3)
    DisableFlagRange((1710, 1729))
    EnableFlag(1713)

    # --- 3 --- #
    DefineLabel(3)
    GotoIfFlagRangeState(Label.L4, RangeState.AnyOn, FlagType.Absolute, (1710, 1712))
    GotoIfFlagEnabled(Label.L4, 1720)
    DisableObject(3600906)
    DisableTreasure(3600906)
    Goto(Label.L9)

    # --- 4 --- #
    DefineLabel(4)
    EnableObject(3600906)
    EnableTreasure(3600906)
    Goto(Label.L9)

    # --- 8 --- #
    DefineLabel(8)
    DisableTreasure(3600906)
    GotoIfFlagRangeState(Label.L5, RangeState.AnyOn, FlagType.Absolute, (1710, 1712))
    GotoIfFlagEnabled(Label.L5, 1720)
    DisableObject(3600906)
    Goto(Label.L9)

    # --- 5 --- #
    DefineLabel(5)
    EnableObject(3600906)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, 1723)
    GotoIfFlagEnabled(Label.L1, 1713)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SetTeamType(arg_0_3, TeamType.Ally)
    ForceAnimation(arg_0_3, 103151)
    EnableImmortality(arg_0_3)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableAnimations(arg_0_3)
    ForceAnimation(arg_0_3, 103157, skip_transition=True)
    End()


def Event13600951(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13600951: Event 13600951 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(arg_4_7)
    IfFlagEnabled(1, arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 103152)
    IfFlagEnabled(2, arg_8_11)
    IfFlagDisabled(2, arg_4_7)
    IfHealthNotEqual(2, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=2)
    ForceAnimation(arg_0_3, 103151)
    Restart()


def Event13600952(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13600952: Event 13600952 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagEnabled(1, arg_4_7)
    IfAttackedWithDamageType(1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, 103153)
    Kill(arg_0_3, award_souls=True)
    EnableFlag(arg_8_11)


def Event13600953(_, arg_0_3: int):
    """ 13600953: Event 13600953 """
    IfFlagEnabled(-1, 1724)
    IfFlagRangeAnyEnabled(-1, (1720, 1722))
    EndIfConditionFalse(-1)
    IfFlagEnabled(0, 1723)
    EnableCharacter(arg_0_3)
    EnableBackread(arg_0_3)
    ForceAnimation(arg_0_3, 103151)
    EnableImmortality(arg_0_3)
    DisableObject(3600906)
    DisableTreasure(3600906)


def Event13600954(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13600954: Event 13600954 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    GotoIfFlagDisabled(Label.L0, arg_0_3)
    GotoIfFlagDisabled(Label.L1, arg_4_7)
    End()

    # --- 1 --- #
    DefineLabel(1)
    EnableFlag(arg_4_7)

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(1, arg_4_7)
    IfCharacterDead(1, 3600905)
    IfConditionTrue(0, input_condition=1)
    AwardItemLot(arg_8_11, host_only=False)


def Event13600955():
    """ 13600955: Event 13600955 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    IfFlagEnabled(1, 1723)
    IfFlagDisabled(1, 73600502)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(73600500)
    IfCharacterInsideRegion(0, PLAYER, region=3602850)
    DisableFlag(73600500)
    EnableFlag(73600502)


def Event13600956(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 13600956: Event 13600956 """
    IfCharacterHuman(-15, PLAYER)
    EndIfConditionFalse(-15)
    DisableFlag(arg_8_11)
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_8_11)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(arg_8_11)
    Kill(arg_0_3, award_souls=False)
    EnableFlag(73600530)
    ForceAnimation(arg_0_3, 103156, wait_for_completion=True, skip_transition=True)
    ForceAnimation(arg_0_3, 103157, skip_transition=True)


def Event13600995():
    """ 13600995: Event 13600995 """
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, 13605952)
    DisableFlag(13605940)
