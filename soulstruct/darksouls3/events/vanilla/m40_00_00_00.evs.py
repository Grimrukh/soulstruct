"""
linked:
0

strings:
0: N:\\FDP\\data\\Param\\event\\common_func.emevd
84: 
86: 
88: 
90: 
92: 
94: 
"""
from soulstruct.darksouls3.events import *


def Constructor():
    """ 0: Event 0 """
    RegisterBonfire(14000000, obj=4001950, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(14000001, obj=4001951, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RegisterBonfire(14000003, obj=4001953, reaction_distance=5.0, reaction_angle=180.0, initial_kindle_level=0)
    RunCommonEvent(20005500, args=(14000800, 14000002, 4000952, 4001952))
    RunCommonEvent(20005500, args=(14000830, 14000004, 4000954, 4001954))
    RunEvent(14005480, slot=0, args=(74000012,))
    RunEvent(14005481)
    RunEvent(14005101)
    RunEvent(14005110)
    RunEvent(14000130)
    RunEvent(14005102)
    RunEvent(14000120, slot=0, args=(9210, 9211, 9212, 9213, 9214, 9215))
    RunEvent(14000121, slot=0, args=(9211, 2126, 4001111, 4001121, 9353, 69050))
    RunEvent(14000121, slot=2, args=(9212, 2124, 4001112, 4001122, 9353, 69040))
    RunEvent(14000121, slot=4, args=(9213, 2123, 4001113, 4001123, 9353, 69040))
    RunEvent(14000121, slot=6, args=(9214, 2125, 4001114, 4001124, 9353, 69050))
    RunCommonEvent(20005120, args=(4000202, 1091043328))
    RunCommonEvent(20005210, args=(4000204, 703, 1703, 1091043328))
    RunCommonEvent(20005132, args=(4000205, 1092616192, 4002205))
    RunCommonEvent(20005132, args=(4000207, 1065353216, 4002207))
    RunCommonEvent(20005130, args=(4000209, 1098907648, 4002207))
    RunCommonEvent(20005213, args=(4000210, 705, 1705, 1075838976, 4002210))
    RunCommonEvent(20005110, args=(4000211, 4002248))
    RunCommonEvent(20005210, args=(4000212, 703, 1703, 1082130432))
    RunCommonEvent(20005200, args=(4000213, 705, 1705, 4002213))
    RunCommonEvent(20005210, args=(4000214, 703, 1703, 1077936128))
    RunCommonEvent(20005150, args=(4000215,))
    RunCommonEvent(20005200, args=(4000216, 703, 1703, 4002216))
    RunCommonEvent(20005200, args=(4000217, 703, 1703, 4002216))
    RunCommonEvent(20005200, args=(4000218, 706, 1706, 4002218))
    RunCommonEvent(20005200, args=(4000219, 706, 1706, 4002216))
    RunCommonEvent(20005201, args=(4000220, 703, 1703, 4002220, 1065353216))
    RunCommonEvent(20005201, args=(4000221, 706, 1706, 4002220, 1069547520))
    RunCommonEvent(20005210, args=(4000239, 703, 1703, 1082130432))
    RunCommonEvent(20005120, args=(4000240, 1097859072))
    RunCommonEvent(20005220, args=(4000241, 706, 1706))
    RunCommonEvent(20005290, args=(4000242, 705, 1705))
    RunCommonEvent(20005220, args=(4000243, 703, 1703))
    RunCommonEvent(20005110, args=(4000244, 4002244))
    RunCommonEvent(20005292, args=(4000245, 703, 1703))
    RunCommonEvent(20005290, args=(4000246, 703, 1703))
    RunCommonEvent(20005110, args=(4000247, 4002248))
    RunCommonEvent(20005220, args=(4000251, 703, 1703))
    RunCommonEvent(20005210, args=(4000252, 705, 1705, 1073741824))
    RunCommonEvent(20005210, args=(4000253, 703, 1703, 1095761920))
    RunCommonEvent(20005211, args=(4000255, 703, 1703, 1084227584, 1065353216))
    RunCommonEvent(20005213, args=(4000256, 705, 1705, 1075838976, 4002210))
    RunCommonEvent(20005211, args=(4000260, 703, 1703, 1084227584, 1069547520))
    RunCommonEvent(20005200, args=(4000261, 703, 1703, 4002261))
    RunCommonEvent(20005200, args=(4000262, 703, 1703, 4002261))
    RunCommonEvent(20005200, args=(4000263, 703, 1703, 4002261))
    RunCommonEvent(20005140, args=(4000265, 4002207, 4000254))
    RunCommonEvent(20005223, args=(4000280, 703, 1703, 1065353216))
    RunCommonEvent(20005210, args=(4000281, 703, 1703, 1102053376))
    RunCommonEvent(20005210, args=(4000282, 705, 1705, 1094713344))
    RunCommonEvent(20005213, args=(4000284, 705, 1705, 1075838976, 4002284))
    RunCommonEvent(20005220, args=(4000285, 703, 1703))
    RunCommonEvent(20005223, args=(4000287, 703, 1703, 1065353216))
    RunCommonEvent(20005201, args=(4000288, 703, 1703, 4002207, 1082130432))
    RunCommonEvent(20005120, args=(4000289, 1077936128))
    RunCommonEvent(
        20005415,
        args=(14000290, 4000250, 4000290, 703, 1703, 4002290, 14004290, 14005290),
        event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    )
    RunCommonEvent(20005416, args=(14000290, 4000250, 4000290), event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunCommonEvent(20005120, args=(4000301, 1107296256), event_layers=[1])
    RunCommonEvent(20005132, args=(4000303, 1065353216, 4002303), event_layers=[1])
    RunCommonEvent(20005110, args=(4000320, 4002320), event_layers=[1])
    RunCommonEvent(20005110, args=(4000330, 4002330), event_layers=[1])
    RunCommonEvent(20005110, args=(4000331, 4002330), event_layers=[1])
    RunEvent(14005300, slot=0, args=(4000330, 4002360))
    RunCommonEvent(20005240, args=(4000341, 702, 1702, 12140), event_layers=[1])
    RunCommonEvent(20005240, args=(4000342, 702, 1702, 12140), event_layers=[1])
    RunCommonEvent(20005240, args=(4000343, 701, 1701, 12140), event_layers=[1])
    RunCommonEvent(20005120, args=(4000346, 1087373312), event_layers=[1])
    RunCommonEvent(20005240, args=(4000349, 700, 1700, 12140), event_layers=[1])
    RunCommonEvent(20005240, args=(4000350, 700, 1700, 12140), event_layers=[1])
    RunCommonEvent(20005240, args=(4000351, 700, 1700, 12140), event_layers=[1])
    RunCommonEvent(20005223, args=(4000352, 700, 1700, 1073741824), event_layers=[1])
    RunCommonEvent(20005210, args=(4000355, 700, 1700, 1086324736), event_layers=[1])
    RunCommonEvent(20005240, args=(4000356, 700, 1700, 12140), event_layers=[1])
    RunCommonEvent(20005240, args=(4000357, 700, 1700, 12140), event_layers=[1])
    RunCommonEvent(20005211, args=(4000360, 701, 1701, 1084227584, 0), event_layers=[1])
    RunCommonEvent(20005211, args=(4000361, 701, 1701, 1084227584, 0), event_layers=[1])
    RunCommonEvent(20005211, args=(4000362, 701, 1701, 1084227584, 0), event_layers=[1])
    RunCommonEvent(20005211, args=(4000363, 701, 1701, 1084227584, 0), event_layers=[1])
    RunCommonEvent(20005211, args=(4000364, 701, 1701, 1084227584, 0), event_layers=[1])
    RunCommonEvent(20005211, args=(4000365, 701, 1701, 1084227584, 0), event_layers=[1])
    RunCommonEvent(20005341, args=(14000380, 4000380, 31002000))
    RunCommonEvent(20005341, args=(14000381, 4000381, 31004000))
    RunCommonEvent(20005341, args=(14000382, 4000382, 31004000))
    RunCommonEvent(20005341, args=(14000390, 4000390, 21509500))
    RunCommonEvent(20005342, args=(9500, 4000500))
    RunCommonEvent(20005620, args=(14000400, 14001400, 4001400, 4001401, 4001402, 14001401))
    RunEvent(14005401)
    RunEvent(14005420)
    RunCommonEvent(20005640, args=(14000426, 4001426, 14005426, 14005427))
    RunEvent(14005460)
    RunEvent(14005461)
    RunEvent(14005450)
    RunEvent(1405451, event_layers=[1])
    DisableObject(4001801)
    RunEvent(14005470, event_layers=[1])
    RunEvent(14005471, event_layers=[1])
    RunEvent(14005472, event_layers=[1])
    RunEvent(14005473, event_layers=[1])
    RunEvent(14005474, event_layers=[1])
    RunEvent(14005445)
    RunCommonEvent(20005610, args=(14000410, 4002410, 4002411))
    RunCommonEvent(20005611, args=(14000410, 4003252, 4001252, 1400340))
    RunCommonEvent(20005613, args=(14000425, 4003250, 4001250, 3400340, 10010873))
    RunEvent(14005442, event_layers=[1])
    RunEvent(14005440, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005441)
    RunCommonEvent(20005650, args=(14000430, 4001430))
    RunCommonEvent(20005650, args=(14000431, 4001431))
    RunCommonEvent(20005650, args=(14000432, 4001432))
    RunCommonEvent(20005650, args=(14000433, 4001433))
    RunCommonEvent(20005650, args=(14000434, 4001434))
    RunCommonEvent(20005650, args=(14000435, 4001435))
    RunCommonEvent(20005520, args=(14000600, 4001600, 4004600))
    RunCommonEvent(20005520, args=(14000601, 4001601, 4004601))
    RunCommonEvent(20005523, args=(4001210, 2))
    RunCommonEvent(20005523, args=(4001211, 1))
    RunCommonEvent(20005523, args=(4001212, 1))
    RunCommonEvent(20005523, args=(4001213, 2))
    RunCommonEvent(20005524, args=(4001218, 9512))
    RunCommonEvent(20005525, args=(54000300, 4000300, 4001728, 62), event_layers=[1])
    RunCommonEvent(20005526, args=(54000330, 4000330, 4001221, 62, 13300800), event_layers=[1])
    RunCommonEvent(20005525, args=(54000340, 4000340, 4001222, 62), event_layers=[1])
    RunEvent(14005484, slot=1, args=(10012051, 4001141))
    RunEvent(14005484, slot=2, args=(10012052, 4001142))
    RunEvent(14005484, slot=3, args=(10012053, 4001143))
    RunEvent(14005484, slot=4, args=(10012054, 4001144))
    RunEvent(14005484, slot=5, args=(10012055, 4001145))
    RunEvent(14005800)
    RunEvent(14005810)
    RunEvent(14005811)
    RunEvent(14005812)
    RunEvent(14000816)
    RunEvent(14005813)
    RunEvent(14005820)
    RunEvent(14005830, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005840, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005841, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14000842, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14000859, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunCommonEvent(20005840, args=(4001800,), event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunCommonEvent(20005841, args=(4001800,), event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunCommonEvent(
        20005701,
        args=(14000830, 14004190, 14005190, 4000190, 4002190, 9500),
        event_layers=[1, 3, 4, 5, 6, 7, 8, 9],
    )
    RunCommonEvent(
        20005711,
        args=(14004190, 14005835, 4000190, 4002800, 4002805, 14000831),
        event_layers=[1, 3, 4, 5, 6, 7, 8, 9],
    )
    RunCommonEvent(20005720, args=(14004190, 14005190, 14000830, 4000190), event_layers=[1, 3, 4, 5, 6, 7, 8, 9])
    RunCommonEvent(
        20005714,
        args=(14004190, 14005835, 4000190, 4002806, 14000831),
        event_layers=[1, 3, 4, 5, 6, 7, 8, 9],
    )
    RunCommonEvent(
        20005750,
        args=(14000830, 14000197, 14004197, 14005197, 4000197, 4002197, 4002198, 0, 0),
        event_layers=[1, 3, 4, 5, 6, 7, 8, 9],
    )
    RunCommonEvent(20005721, args=(14004197, 14005197, 14000197, 4000197), event_layers=[1, 3, 4, 5, 6, 7, 8, 9])
    RunCommonEvent(20005760, args=(14000197, 14004197, 14005197, 4000197), event_layers=[1, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005619)
    RunCommonEvent(20006002, args=(4000700, 1018, 1015, 1019))
    RunEvent(14005602, slot=0, args=(4000700, 60200))
    RunEvent(14000603, slot=0, args=(14000410, 74000132))
    RunEvent(14005604, slot=0, args=(4000700, 4002702))
    RunEvent(14005605, slot=0, args=(4000700, 12500, 20005))
    RunEvent(14005605, slot=1, args=(4000700, 12501, 20006))
    RunEvent(14005605, slot=2, args=(4000700, 12502, 20007))
    RunEvent(14005605, slot=3, args=(4000700, 12503, 20008))
    RunEvent(14005615, slot=0, args=(4000700,))
    RunEvent(14005616, slot=0, args=(4000700,))
    RunCommonEvent(20006005, args=(4000700, 74000135, 74000137, 0, 1067030938, 90250, 90260, 155))
    RunCommonEvent(20006006, args=(4000700, 74000136, 74000138, 20000, 20001, 1, 0))
    RunCommonEvent(20006040, args=(4000700, 4002703, 153))
    RunCommonEvent(20006040, args=(4000700, 4002700, 151))
    RunCommonEvent(20006002, args=(4000705, 1038, 1035, 1039))
    RunCommonEvent(20006002, args=(4000710, 1178, 1175, 1179))
    RunEvent(14005661, slot=0, args=(4000710,))
    RunEvent(14005682, slot=0, args=(4000715, 1198, 1195, 1199))
    RunEvent(14005681)
    RunEvent(14005684, slot=0, args=(70000119,))
    RunCommonEvent(20006020, args=(70000125, 70000102))
    RunCommonEvent(20006020, args=(70000126, 70000106))
    RunCommonEvent(20006020, args=(70000127, 70000104))
    RunCommonEvent(20006020, args=(70000128, 70000175))
    RunCommonEvent(20006020, args=(70000129, 70000110))
    RunCommonEvent(20006020, args=(70000130, 70000115))
    RunCommonEvent(20006020, args=(70000131, 70000103))
    RunCommonEvent(20006020, args=(70000107, 70000116))
    RunCommonEvent(20006020, args=(70000132, 70000108))
    RunCommonEvent(20006020, args=(70000133, 70000115))
    RunCommonEvent(20006002, args=(4000716, 1618, 1615, 1619))
    RunCommonEvent(20006002, args=(4000720, 1218, 1215, 1219))
    RunCommonEvent(20006000, args=(4000720, 1216, 1217, 74000330, 1059481190, 1215, 1219, 0))
    RunCommonEvent(20006001, args=(4000720, 1216, 1217, 74000330, 3))
    RunCommonEvent(20006020, args=(70000153, 70000152))
    RunCommonEvent(20006002, args=(4000725, 1298, 1295, 1299))
    RunCommonEvent(20006002, args=(4000726, 1298, 1295, 1299))
    RunCommonEvent(20006002, args=(4000727, 1298, 1295, 1299))
    RunEvent(14005721)
    RunCommonEvent(20006005, args=(4000725, 74000383, 74000384, 0, 1065353216, 90280, 90291, 4294967295))
    RunEvent(14005722, slot=0, args=(4000726, 90641))
    RunCommonEvent(20006005, args=(4000726, 74000386, 74000387, 0, 1065353216, 90280, 90291, 4294967295))
    RunEvent(14005723, slot=0, args=(4000726, 74000381, 1295, 1284, 1282, 1280, 1294, 4000725, 90550))
    RunEvent(14005723, slot=1, args=(4000726, 74000382, 1295, 1285, 1283, 1280, 1294, 4000725, 90550))
    RunCommonEvent(20006030, args=(4001727, 4000, 2, 61610, 50006162, 50006163, 1286))
    RunCommonEvent(20006031, args=(74000393, 4002727))
    RunCommonEvent(20006005, args=(4000727, 74000389, 74000391, 4002728, 0, 90250, 90260, 155))
    RunCommonEvent(20006006, args=(4000727, 74000390, 74000392, 90610, 90620, 0, 0))
    RunCommonEvent(20006002, args=(4000730, 1078, 1075, 1079))
    RunCommonEvent(20006005, args=(4000730, 74000430, 74000432, 0, 1075000115, 90250, 90260, 155))
    RunCommonEvent(20006006, args=(4000730, 74000431, 74000433, 20001, 20002, 1, 1060320051))
    RunCommonEvent(20006002, args=(4000735, 1258, 1255, 1259))
    RunCommonEvent(20006000, args=(4000735, 1256, 1257, 74000470, 1059481190, 1255, 1259, 0))
    RunCommonEvent(20006001, args=(4000735, 1256, 1257, 74000470, 3))
    RunCommonEvent(20006002, args=(4000740, 1278, 1275, 1279))
    RunEvent(14005781)
    RunEvent(14005782)
    RunCommonEvent(20006002, args=(4000745, 1238, 1235, 1239))
    RunCommonEvent(20006000, args=(4000745, 1236, 1237, 74000580, 1059481190, 1235, 1239, 0))
    RunCommonEvent(20006001, args=(4000745, 1236, 1237, 74000580, 3))
    RunEvent(14005501, slot=0, args=(74000582, 74000584, 3, 3, 3), arg_types="iiIBI")
    RunEvent(14005503, slot=0, args=(74000583,))
    RunCommonEvent(20006002, args=(4000750, 1058, 1055, 1059))
    RunEvent(
        14005521,
        slot=0,
        args=(4000750, 1056, 1057, 74000630, 0.6499999761581421, 1055, 1059, 0),
        arg_types="iiiifiii",
    )
    RunCommonEvent(20006001, args=(4000750, 1056, 1057, 74000630, 3))
    RunEvent(14000522)
    RunCommonEvent(20006030, args=(4001750, 4000, 3, 60410, 50006041, 50006042, 1045))
    RunCommonEvent(20006002, args=(4000755, 1318, 1315, 1319))
    RunCommonEvent(20006000, args=(4000755, 1316, 1317, 74000680, 1059481190, 1315, 1319, 0))
    RunCommonEvent(20006001, args=(4000755, 1316, 1317, 74000680, 3))
    RunCommonEvent(20006002, args=(4000756, 1318, 1315, 1319))
    RunEvent(14005541, slot=0, args=(4000755, 1316, 1317, 1281, 1284, 1298, 1315, 1319, 1302))
    RunEvent(14005542, slot=0, args=(4000755, 4000756, 4000725, 4000726, 90640))
    RunEvent(14005543, slot=0, args=(4000756,))
    RunEvent(14000490)
    RunEvent(14000491)
    RunEvent(
        14005581,
        slot=0,
        args=(4000765, 4000770, 4000775, 74000730, 74000731, 0.6499999761581421),
        arg_types="iiiiif",
    )
    RunEvent(14000583, slot=0, args=(4000765, 4000770, 1356, 1357, 4000775, 1355, 1359, 1342))
    RunEvent(14005584, slot=0, args=(4000765, 4000770, 1357, 1342))
    RunCommonEvent(20006001, args=(4000765, 1356, 1357, 74000730, 3))
    RunCommonEvent(20006002, args=(4000765, 1358, 1355, 1359))
    RunEvent(14005587, slot=0, args=(4000765, 1342, 1357))
    RunCommonEvent(20006001, args=(4000770, 1356, 1357, 74000730, 3))
    RunCommonEvent(20006002, args=(4000770, 1358, 1355, 1359))
    RunEvent(14005587, slot=1, args=(4000770, 1342, 1357))
    RunCommonEvent(20006001, args=(4000775, 1496, 1497, 74000731, 3))
    RunCommonEvent(20006002, args=(4000775, 1498, 1495, 1499))
    RunEvent(14000585, slot=0, args=(4000775, 1496, 1497, 4000765, 4000770, 1495, 1499, 1482))
    RunCommonEvent(20006002, args=(4000760, 1118, 1115, 1119))
    RunCommonEvent(20006000, args=(4000760, 1116, 1117, 74000830, 1059481190, 1115, 1119, 0))
    RunCommonEvent(20006001, args=(4000760, 1116, 1117, 74000830, 3))
    RunCommonEvent(20006030, args=(4001760, 4000, 2, 60730, 50006074, 50006074, 74000825))
    RunCommonEvent(20006002, args=(4000761, 1118, 1115, 1119))
    RunCommonEvent(20006000, args=(4000761, 1116, 1117, 74000831, 1059481190, 1115, 1119, 0))
    RunCommonEvent(20006001, args=(4000761, 1116, 1117, 74000831, 3))
    RunCommonEvent(20006002, args=(4000780, 1138, 1135, 1139))
    RunCommonEvent(20006030, args=(4001780, 4000, 1, 60810, 50006081, 50006081, 74000790))
    RunCommonEvent(20006002, args=(4000785, 1158, 1155, 1159))
    RunCommonEvent(20006000, args=(4000785, 1156, 1157, 74000880, 1059481190, 1155, 1159, 0))
    RunCommonEvent(20006001, args=(4000785, 1156, 1157, 74000880, 3))
    RunCommonEvent(20006002, args=(4000791, 1378, 1375, 1379))
    RunCommonEvent(20006000, args=(4000791, 1376, 1377, 73500290, 1059481190, 1375, 1379, 0))
    RunCommonEvent(20006001, args=(4000791, 1376, 1377, 73500290, 3))
    RunCommonEvent(20006032, args=(4000791, 4001790))
    RunEvent(14000621, slot=0, args=(4000790,))
    RunEvent(14000622, slot=0, args=(4000790, 4000791, 4004791))
    RunEvent(14000624, slot=0, args=(4000791,))


def Preconstructor():
    """ 50: Event 50 """
    RunEvent(14005103, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005104, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005618, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(
        14005600,
        slot=0,
        args=(4000700, 4002701, 4002703, 4002700, 4002702),
        event_layers=[0, 3, 4, 5, 6, 7, 8, 9],
    )
    RunEvent(14005640, slot=0, args=(4000705, 4001115, 4000706), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005660, slot=0, args=(4000710,), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005680, slot=0, args=(4000715, 4002715), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005683, slot=0, args=(4000716, 4002715))
    RunEvent(
        14005720,
        slot=0,
        args=(4000725, 4000726, 4000727, 90550, 90640, 90730, 4004725, 4004726, 4004727),
        event_layers=[0, 3, 4, 5, 6, 7, 8, 9],
    )
    RunEvent(14005740, slot=0, args=(4000730, 2160, 4004730), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005760, slot=0, args=(4000735, 4006735), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005780, slot=0, args=(4000740, 90460, 4001740, 4004740), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005500, slot=0, args=(4000745, 90420, 4001745, 4004745), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005520, slot=0, args=(4000750, 90300, 4004750, 4001751))
    RunEvent(14005540, slot=0, args=(4000755, 4000756, 90660, 4004755, 4004756), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005560, slot=0, args=(4000760, 4000761, 4004760, 4004761), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(
        14005580,
        slot=0,
        args=(4000765, 4000770, 90750, 90800, 4004765, 4004770),
        event_layers=[0, 3, 4, 5, 6, 7, 8, 9],
    )
    RunEvent(14005586, slot=0, args=(4000775, 90900, 4004775), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005570, slot=0, args=(4000780, 4000781, 4004780, 4004781), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005750, slot=0, args=(4000785, 90710, 4004785), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005620, slot=0, args=(4000790, 4000791, 4004791), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005701, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14005700, slot=0, args=(4000720, 4004720), event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    RunEvent(14000401)
    RunEvent(14000100, event_layers=[0, 2, 3, 4, 5, 6, 7, 8, 9])
    DisableSoundEvent(4004800)
    DisableSoundEvent(4004801)
    DisableSoundEvent(4004830)
    DisableSoundEvent(4004831)
    DisableSoundEvent(4004450)
    DisableSoundEvent(4004460)
    DisableSoundEvent(4003700)
    DisableSoundEvent(4003701)


def Event14000100():
    """ 14000100: Event 14000100 """
    EndIfThisEventSlotFlagEnabled()
    EndIfPlayerNotInOwnWorld()
    EndIfOutsideMap(game_map=FIRELINK_SHRINE)
    IfMapInCeremony(1, game_map=FIRELINK_SHRINE, ceremony_id=0)
    EndIfConditionFalse(1)
    AddSpecialEffect(PLAYER, 4610)
    ForceAnimation(PLAYER, 0)
    DisableObject(4006440)
    PlayCutsceneAndMovePlayer_WithUnknowns(
        40000040,
        CutsceneFlags.Skippable,
        move_to_region=4002110,
        move_to_map=FIRELINK_SHRINE,
        player_id=PLAYER,
        unknown1=1,
        unknown2=0,
    )
    WaitFrames(1)
    ForceAnimation(PLAYER, 0)
    EnableObject(4006440)
    IfOngoingCutsceneFinished(0, 40000040)
    SetNetworkInteractionState(True)
    WaitFrames(1)
    CancelSpecialEffect(PLAYER, 4610)
    SetRespawnPoint(4002959)
    SaveRequest()
    EnableFlag(14000100)


def Event14005101():
    """ 14005101: Event 14005101 """
    EndIfFlagEnabled(14000101)
    IfObjectBackreadEnabled(0, obj=4001950)
    WaitFrames(1)
    ForceAnimation(4001950, 100000, loop=True)
    EnableFlag(74000010)
    IfObjectBackreadDisabled(1, obj=4001950)
    IfConditionTrue(-1, input_condition=1)
    IfActionButtonParam(-1, action_button_id=9351, entity=4001950)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFinishedConditionTrue(1)
    Move(PLAYER, destination=4001950, destination_type=CoordEntityType.Object, model_point=1, short_move=True)
    ForceAnimation(4001950, 60430)
    EnableBonfireWarping(bonfire_obj=4001950, animation=60430)
    DisableFlag(74000010)
    EnableFlag(14000101)
    RemoveGoodFromPlayer(2137, quantity=1)


def Event14005102():
    """ 14005102: Event 14005102 """
    EndIfPlayerNotInOwnWorld()
    DisableObject(4001101)
    DisableObject(4001102)
    IfStandingOnCollision(1, 4004100)
    IfFlagDisabled(10, 131)
    IfFlagEnabled(10, 2051)
    IfConditionTrue(-10, input_condition=1)
    IfConditionTrue(-10, input_condition=10)
    IfConditionTrue(0, input_condition=-10)
    DeleteObjectVFX(4001101, erase_root=True)
    DeleteObjectVFX(4001102, erase_root=True)
    EnableObject(4001101)
    EnableObject(4001102)
    CreateObjectVFX(840080, obj=4001101, model_point=101)
    CreateObjectVFX(4, obj=4001102, model_point=101)
    IfFlagDisabled(1, 2051)
    IfLeavingSession(1)
    SkipLinesIfFinishedConditionTrue(1, 10)
    IfStandingOnCollision(1, 4004101)
    IfConditionTrue(0, input_condition=1)
    IfFlagDisabled(-9, 131)
    IfMapInCeremony(-9, game_map=FIRELINK_SHRINE, ceremony_id=10)
    SkipLinesIfConditionFalse(2, -9)
    IfTimeElapsed(2, 18.0)
    SkipLines(1)
    IfTimeElapsed(2, 20.0)
    SkipLinesIfFinishedConditionTrue(2, 10)
    IfStandingOnCollision(3, 4004100)
    SkipLines(1)
    IfFlagEnabled(3, 2051)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(-1, input_condition=3)
    IfConditionTrue(0, input_condition=-1)
    RestartIfFinishedConditionTrue(3)
    DeleteObjectVFX(4001101, erase_root=True)
    DeleteObjectVFX(4001102, erase_root=True)
    IfTimeElapsed(4, 2.0)
    SkipLinesIfFinishedConditionTrue(2, 10)
    IfStandingOnCollision(5, 4004100)
    SkipLines(1)
    IfFlagEnabled(5, 2051)
    IfConditionTrue(-2, input_condition=4)
    IfConditionTrue(-2, input_condition=5)
    IfConditionTrue(0, input_condition=-2)
    RestartIfFinishedConditionTrue(5)
    DisableObject(4001101)
    DisableObject(4001102)
    Restart()


def Event14005103():
    """ 14005103: Event 14005103 """
    IfPlayerInOwnWorld(1)
    IfFlagDisabled(1, 131)
    IfConditionTrue(0, input_condition=1)
    EnableMapCollision(4004109)
    DisableMapCollision(4004100)


def Event14005104():
    """ 14005104: Event 14005104 """
    EnableMapCollision(4004109)
    DisableMapCollision(4004100)


def Event14005110():
    """ 14005110: Event 14005110 """
    SetCollisionResState(collision=4004100, state=False)
    EndIfFlagEnabled(14000110)
    EndIfPlayerNotInOwnWorld()
    DisableFlag(74000010)
    IfFlagEnabled(-1, 9210)
    IfFlagEnabled(-1, 74000123)
    IfConditionTrue(1, input_condition=-1)
    IfHealthNotEqual(1, 4000700, 0.0)
    IfConditionTrue(0, input_condition=1)
    SetCollisionResState(collision=4004100, state=True)
    GotoIfFlagEnabled(Label.L0, 74000123)
    EnableFlag(74000010)
    IfHealthEqual(15, 4000700, 0.0)
    IfConditionTrue(-2, input_condition=15)
    IfActionButtonParam(-2, action_button_id=9101, entity=4001950)
    IfFlagEnabled(-2, 74000123)
    IfConditionTrue(0, input_condition=-2)
    RestartIfFinishedConditionTrue(15)

    # --- 0 --- #
    DefineLabel(0)
    DeleteVFX(4003500, erase_root_only=False)
    DeleteVFX(4003501, erase_root_only=False)
    DeleteVFX(4003502, erase_root_only=False)
    DeleteVFX(4003503, erase_root_only=False)
    DeleteVFX(4003504, erase_root_only=False)
    DisableFlag(74000010)
    EnableFlag(14000110)
    EnableFlag(14100000)
    SkipLinesIfFlagEnabled(2, 1038)
    PlayCutscene(
        40000020,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=4102100,
        move_to_map=KILN_OF_THE_FIRST_FLAME,
    )
    SkipLines(1)
    PlayCutscene(
        40000021,
        skippable=True,
        fade_out=False,
        player_id=PLAYER,
        move_to_region=4102100,
        move_to_map=KILN_OF_THE_FIRST_FLAME,
    )
    DeleteObjectVFX(4001500, erase_root=True)
    DeleteObjectVFX(4001501, erase_root=True)
    DeleteObjectVFX(4001502, erase_root=True)
    DeleteObjectVFX(4001503, erase_root=True)
    DeleteObjectVFX(4001510, erase_root=True)
    DeleteObjectVFX(4001511, erase_root=True)
    DeleteObjectVFX(4001512, erase_root=True)
    DeleteObjectVFX(4001513, erase_root=True)
    DeleteObjectVFX(4001514, erase_root=True)
    DeleteObjectVFX(4001515, erase_root=True)
    DeleteObjectVFX(4001516, erase_root=True)
    DeleteObjectVFX(4001517, erase_root=True)
    DeleteObjectVFX(4001518, erase_root=True)
    DeleteObjectVFX(4001519, erase_root=True)
    DeleteObjectVFX(4001520, erase_root=True)
    DeleteObjectVFX(4001521, erase_root=True)
    DeleteObjectVFX(4001522, erase_root=True)
    DeleteObjectVFX(4001523, erase_root=True)
    DeleteObjectVFX(4001524, erase_root=True)
    DeleteObjectVFX(4001525, erase_root=True)
    DeleteObjectVFX(4001526, erase_root=True)
    DeleteObjectVFX(4001527, erase_root=True)
    DeleteObjectVFX(4001528, erase_root=True)
    DeleteObjectVFX(4001529, erase_root=True)
    DeleteObjectVFX(4001530, erase_root=True)
    DeleteObjectVFX(4001531, erase_root=True)
    DeleteObjectVFX(4001532, erase_root=True)
    DeleteObjectVFX(4001533, erase_root=True)
    DeleteObjectVFX(4001534, erase_root=True)
    DeleteObjectVFX(4001535, erase_root=True)
    DeleteObjectVFX(4001536, erase_root=True)
    DeleteObjectVFX(4001537, erase_root=True)
    DeleteObjectVFX(4001538, erase_root=True)
    DeleteObjectVFX(4001539, erase_root=True)
    DeleteObjectVFX(4001540, erase_root=True)
    DeleteObjectVFX(4001541, erase_root=True)
    DeleteObjectVFX(4001542, erase_root=True)
    DeleteObjectVFX(4001543, erase_root=True)
    DeleteObjectVFX(4001544, erase_root=True)
    DeleteObjectVFX(4001545, erase_root=True)
    DeleteObjectVFX(4001546, erase_root=True)
    DeleteObjectVFX(4001547, erase_root=True)
    DeleteObjectVFX(4001548, erase_root=True)
    DeleteObjectVFX(4001549, erase_root=True)
    DeleteObjectVFX(4001550, erase_root=True)
    DeleteObjectVFX(4001551, erase_root=True)
    DeleteObjectVFX(4001552, erase_root=True)
    DeleteObjectVFX(4001553, erase_root=True)
    DeleteObjectVFX(4001554, erase_root=True)
    DeleteObjectVFX(4001555, erase_root=True)
    DeleteObjectVFX(4001556, erase_root=True)
    DeleteObjectVFX(4001557, erase_root=True)
    DeleteObjectVFX(4001558, erase_root=True)
    DeleteObjectVFX(4001559, erase_root=True)
    DeleteObjectVFX(4001560, erase_root=True)
    DeleteObjectVFX(4001561, erase_root=True)
    DeleteObjectVFX(4001562, erase_root=True)
    DeleteObjectVFX(4001563, erase_root=True)
    DeleteObjectVFX(4001564, erase_root=True)
    DeleteObjectVFX(4001565, erase_root=True)
    DeleteObjectVFX(4001566, erase_root=True)
    DeleteObjectVFX(4001567, erase_root=True)
    DeleteObjectVFX(4001568, erase_root=True)
    DeleteObjectVFX(4001569, erase_root=True)
    SetRespawnPoint(4102100)
    SaveRequest()
    WaitFrames(1)


def Event14000120(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 14000120: Event 14000120 """
    EndIfFlagEnabled(arg_0_3)
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_8_11)
    IfFlagEnabled(1, arg_12_15)
    IfFlagEnabled(1, arg_16_19)
    IfFlagEnabled(1, arg_20_23)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)


@RestartOnRest
def Event14000121(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 14000121: Event 14000121 """
    EndIfPlayerNotInOwnWorld()
    GotoIfFlagDisabled(Label.L0, arg_0_3)
    DeleteObjectVFX(arg_8_11, erase_root=False)
    CreateObjectVFX(840066, obj=arg_8_11, model_point=201)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableObject(arg_8_11)
    IfFlagDisabled(1, 2051)
    IfLeavingSession(1)
    IfPlayerHasGood(1, arg_4_7, including_box=False)
    IfFlagDisabled(1, arg_0_3)
    IfActionButtonParam(1, action_button_id=arg_16_19, entity=arg_12_15)
    IfConditionTrue(0, input_condition=1)
    RotateToFaceEntity(PLAYER, arg_12_15, animation=arg_20_23, wait_for_completion=True)
    SkipLinesIfEqual(2, left=arg_20_23, right=69050)
    Wait(0.8999999761581421)
    SkipLines(1)
    Wait(2.0)
    EnableFlag(arg_0_3)
    RemoveGoodFromPlayer(arg_4_7, quantity=1)
    EnableObject(arg_8_11)
    CreateTemporaryVFX(840065, anchor_entity=arg_8_11, anchor_type=CoordEntityType.Object, model_point=201)
    CreateObjectVFX(840066, obj=arg_8_11, model_point=201)


@RestartOnRest
def Event14000130():
    """ 14000130: Event 14000130 """
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(6010)
    CreateObjectVFX(63, obj=4001200, model_point=90)
    IfPlayerInOwnWorld(1)
    IfActionButtonParam(1, action_button_id=9355, entity=4001200)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(PLAYER, 60070)
    GotoIfFlagEnabled(Label.L10, 6030)
    GotoIfFlagEnabled(Label.L9, 6029)
    GotoIfFlagEnabled(Label.L8, 6028)
    GotoIfFlagEnabled(Label.L7, 6027)
    GotoIfFlagEnabled(Label.L6, 6026)
    GotoIfFlagEnabled(Label.L5, 6025)
    GotoIfFlagEnabled(Label.L4, 6024)
    GotoIfFlagEnabled(Label.L3, 6023)
    GotoIfFlagEnabled(Label.L2, 6022)
    GotoIfFlagEnabled(Label.L1, 6021)
    AwardItemLot(4000505, host_only=False)
    Goto(Label.L0)

    # --- 1 --- #
    DefineLabel(1)
    AwardItemLot(4000515, host_only=False)
    Goto(Label.L0)

    # --- 2 --- #
    DefineLabel(2)
    AwardItemLot(4000525, host_only=False)
    Goto(Label.L0)

    # --- 3 --- #
    DefineLabel(3)
    AwardItemLot(4000535, host_only=False)
    Goto(Label.L0)

    # --- 4 --- #
    DefineLabel(4)
    AwardItemLot(4000545, host_only=False)
    Goto(Label.L0)

    # --- 5 --- #
    DefineLabel(5)
    AwardItemLot(4000555, host_only=False)
    Goto(Label.L0)

    # --- 6 --- #
    DefineLabel(6)
    AwardItemLot(4000565, host_only=False)
    Goto(Label.L0)

    # --- 7 --- #
    DefineLabel(7)
    AwardItemLot(4000575, host_only=False)
    Goto(Label.L0)

    # --- 8 --- #
    DefineLabel(8)
    AwardItemLot(4000585, host_only=False)
    Goto(Label.L0)

    # --- 9 --- #
    DefineLabel(9)
    AwardItemLot(4000595, host_only=False)
    Goto(Label.L0)

    # --- 10 --- #
    DefineLabel(10)
    AwardItemLot(4000605, host_only=False)
    Goto(Label.L0)

    # --- 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(4001200, erase_root=True)
    EnableFlag(6010)


@RestartOnRest
def Event14005300(_, arg_0_3: int, arg_4_7: int):
    """ 14005300: Event 14005300 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    IfHasAIStatus(0, arg_0_3, ai_status=AIStatusType.Battle)

    # --- 0 --- #
    DefineLabel(0)
    SetNest(arg_0_3, arg_4_7)


def Event14000401():
    """ 14000401: Event 14000401 """
    EndIfThisEventSlotFlagEnabled()
    EnableFlag(14000400)
    End()


@RestartOnRest
def Event14005401():
    """ 14005401: Event 14005401 """
    RunCommonEvent(
        20005621,
        args=(14000400, 14001400, 4001400, 4001401, 4003401, 4001402, 4003402, 4002401, 4002402, 14001401, 14004400, 0),
    )


@RestartOnRest
def Event14005420():
    """ 14005420: Event 14005420 """
    RegisterLadder(start_climbing_flag=14000420, stop_climbing_flag=14000421, obj=4001420)


@RestartOnRest
def Event14005440():
    """ 14005440: Event 14005440 """
    IfObjectBackreadEnabled(0, obj=4001955)
    WaitFrames(1)
    ForceAnimation(4001955, 100000)


@RestartOnRest
def Event14005441():
    """ 14005441: Event 14005441 """
    DeleteObjectVFX(4001500, erase_root=False)
    DeleteObjectVFX(4001501, erase_root=False)
    DeleteObjectVFX(4001502, erase_root=False)
    DeleteObjectVFX(4001503, erase_root=False)
    DeleteObjectVFX(4001510, erase_root=False)
    DeleteObjectVFX(4001511, erase_root=False)
    DeleteObjectVFX(4001512, erase_root=False)
    DeleteObjectVFX(4001513, erase_root=False)
    DeleteObjectVFX(4001514, erase_root=False)
    DeleteObjectVFX(4001515, erase_root=False)
    DeleteObjectVFX(4001516, erase_root=False)
    DeleteObjectVFX(4001517, erase_root=False)
    DeleteObjectVFX(4001518, erase_root=False)
    DeleteObjectVFX(4001519, erase_root=False)
    DeleteObjectVFX(4001520, erase_root=False)
    DeleteObjectVFX(4001521, erase_root=False)
    DeleteObjectVFX(4001522, erase_root=False)
    DeleteObjectVFX(4001523, erase_root=False)
    DeleteObjectVFX(4001524, erase_root=False)
    DeleteObjectVFX(4001525, erase_root=False)
    DeleteObjectVFX(4001526, erase_root=False)
    DeleteObjectVFX(4001527, erase_root=False)
    DeleteObjectVFX(4001528, erase_root=False)
    DeleteObjectVFX(4001529, erase_root=False)
    DeleteObjectVFX(4001530, erase_root=False)
    DeleteObjectVFX(4001531, erase_root=False)
    DeleteObjectVFX(4001532, erase_root=False)
    DeleteObjectVFX(4001533, erase_root=False)
    DeleteObjectVFX(4001534, erase_root=False)
    DeleteObjectVFX(4001535, erase_root=False)
    DeleteObjectVFX(4001536, erase_root=False)
    DeleteObjectVFX(4001537, erase_root=False)
    DeleteObjectVFX(4001538, erase_root=False)
    DeleteObjectVFX(4001539, erase_root=False)
    DeleteObjectVFX(4001540, erase_root=False)
    DeleteObjectVFX(4001541, erase_root=False)
    DeleteObjectVFX(4001542, erase_root=False)
    DeleteObjectVFX(4001543, erase_root=False)
    DeleteObjectVFX(4001544, erase_root=False)
    DeleteObjectVFX(4001545, erase_root=False)
    DeleteObjectVFX(4001546, erase_root=False)
    DeleteObjectVFX(4001547, erase_root=False)
    DeleteObjectVFX(4001548, erase_root=False)
    DeleteObjectVFX(4001549, erase_root=False)
    DeleteObjectVFX(4001550, erase_root=False)
    DeleteObjectVFX(4001551, erase_root=False)
    DeleteObjectVFX(4001552, erase_root=False)
    DeleteObjectVFX(4001553, erase_root=False)
    DeleteObjectVFX(4001554, erase_root=False)
    DeleteObjectVFX(4001555, erase_root=False)
    DeleteObjectVFX(4001556, erase_root=False)
    DeleteObjectVFX(4001557, erase_root=False)
    DeleteObjectVFX(4001558, erase_root=False)
    DeleteObjectVFX(4001559, erase_root=False)
    DeleteObjectVFX(4001560, erase_root=False)
    DeleteObjectVFX(4001561, erase_root=False)
    DeleteObjectVFX(4001562, erase_root=False)
    DeleteObjectVFX(4001563, erase_root=False)
    DeleteObjectVFX(4001564, erase_root=False)
    DeleteObjectVFX(4001565, erase_root=False)
    DeleteObjectVFX(4001566, erase_root=False)
    DeleteObjectVFX(4001567, erase_root=False)
    DeleteObjectVFX(4001568, erase_root=False)
    DeleteObjectVFX(4001569, erase_root=False)
    CreateObjectVFX(800022, obj=4001500, model_point=200)
    CreateObjectVFX(800022, obj=4001501, model_point=200)
    CreateObjectVFX(800022, obj=4001502, model_point=200)
    CreateObjectVFX(800022, obj=4001503, model_point=200)
    CreateObjectVFX(839010, obj=4001510, model_point=200)
    CreateObjectVFX(839010, obj=4001511, model_point=200)
    CreateObjectVFX(839010, obj=4001512, model_point=200)
    CreateObjectVFX(839010, obj=4001513, model_point=200)
    CreateObjectVFX(839010, obj=4001514, model_point=200)
    CreateObjectVFX(839010, obj=4001515, model_point=200)
    CreateObjectVFX(839010, obj=4001516, model_point=200)
    CreateObjectVFX(839010, obj=4001517, model_point=200)
    CreateObjectVFX(839010, obj=4001518, model_point=200)
    CreateObjectVFX(839010, obj=4001519, model_point=200)
    CreateObjectVFX(839010, obj=4001520, model_point=200)
    CreateObjectVFX(839010, obj=4001521, model_point=200)
    CreateObjectVFX(839010, obj=4001522, model_point=200)
    CreateObjectVFX(839010, obj=4001523, model_point=200)
    CreateObjectVFX(839010, obj=4001524, model_point=200)
    CreateObjectVFX(839010, obj=4001525, model_point=200)
    CreateObjectVFX(839010, obj=4001526, model_point=200)
    CreateObjectVFX(839010, obj=4001527, model_point=200)
    CreateObjectVFX(839010, obj=4001528, model_point=200)
    CreateObjectVFX(839010, obj=4001529, model_point=200)
    CreateObjectVFX(839010, obj=4001530, model_point=200)
    CreateObjectVFX(839010, obj=4001531, model_point=200)
    CreateObjectVFX(839010, obj=4001532, model_point=200)
    CreateObjectVFX(839010, obj=4001533, model_point=200)
    CreateObjectVFX(839010, obj=4001534, model_point=200)
    CreateObjectVFX(839010, obj=4001535, model_point=200)
    CreateObjectVFX(839010, obj=4001536, model_point=200)
    CreateObjectVFX(839010, obj=4001537, model_point=200)
    CreateObjectVFX(839010, obj=4001538, model_point=200)
    CreateObjectVFX(839010, obj=4001539, model_point=200)
    CreateObjectVFX(839010, obj=4001540, model_point=200)
    CreateObjectVFX(839010, obj=4001541, model_point=200)
    CreateObjectVFX(839010, obj=4001542, model_point=200)
    CreateObjectVFX(839010, obj=4001543, model_point=200)
    CreateObjectVFX(839010, obj=4001544, model_point=200)
    CreateObjectVFX(839010, obj=4001545, model_point=200)
    CreateObjectVFX(839010, obj=4001546, model_point=200)
    CreateObjectVFX(839010, obj=4001547, model_point=200)
    CreateObjectVFX(839010, obj=4001548, model_point=200)
    CreateObjectVFX(839010, obj=4001549, model_point=200)
    CreateObjectVFX(839010, obj=4001550, model_point=200)
    CreateObjectVFX(839010, obj=4001551, model_point=200)
    CreateObjectVFX(839010, obj=4001552, model_point=200)
    CreateObjectVFX(839010, obj=4001553, model_point=200)
    CreateObjectVFX(839010, obj=4001554, model_point=200)
    CreateObjectVFX(839010, obj=4001555, model_point=200)
    CreateObjectVFX(839010, obj=4001556, model_point=200)
    CreateObjectVFX(839010, obj=4001557, model_point=200)
    CreateObjectVFX(839010, obj=4001558, model_point=200)
    CreateObjectVFX(839010, obj=4001559, model_point=200)
    CreateObjectVFX(839010, obj=4001560, model_point=200)
    CreateObjectVFX(839010, obj=4001561, model_point=200)
    CreateObjectVFX(839010, obj=4001562, model_point=200)
    CreateObjectVFX(839010, obj=4001563, model_point=200)
    CreateObjectVFX(839010, obj=4001564, model_point=200)
    CreateObjectVFX(839010, obj=4001565, model_point=200)
    CreateObjectVFX(839010, obj=4001566, model_point=200)
    CreateObjectVFX(839010, obj=4001567, model_point=200)
    CreateObjectVFX(839010, obj=4001568, model_point=200)
    CreateObjectVFX(839010, obj=4001569, model_point=200)


@RestartOnRest
def Event14005442():
    """ 14005442: Event 14005442 """
    DisableObjectActivation(4001252, obj_act_id=-1)


@RestartOnRest
def Event14005445():
    """ 14005445: Event 14005445 """
    EndIfFlagDisabled(131)
    DisableSoapstoneMessage(4004222)


def Event14005450():
    """ 14005450: Event 14005450 """
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    DisableSoundEventWithFade(sound_id=4004450, fade_duration=5.0)
    DisableSoundEventWithFade(sound_id=4004460, fade_duration=5.0)
    Wait(0.5)
    IfStandingOnCollision(-1, 4004100)
    IfStandingOnCollision(-1, 4004101)
    IfStandingOnCollision(-1, 4004102)
    IfStandingOnCollision(-1, 4004103)
    IfStandingOnCollision(-1, 4004104)
    IfStandingOnCollision(-1, 4004109)
    IfConditionTrue(1, input_condition=-1)
    IfFlagDisabled(1, 74000122)
    IfConditionTrue(0, input_condition=1)
    SkipLinesIfFlagDisabled(2, 50006020)
    EnableSoundEventWithFade(sound_id=4004450, fade_duration=5.0)
    SkipLines(1)
    EnableSoundEventWithFade(sound_id=4004460, fade_duration=5.0)
    Wait(0.5)
    IfStandingOnCollision(-2, 4004100)
    IfStandingOnCollision(-2, 4004101)
    IfStandingOnCollision(-2, 4004102)
    IfStandingOnCollision(-2, 4004103)
    IfStandingOnCollision(-2, 4004104)
    IfStandingOnCollision(-2, 4004109)
    IfConditionFalse(-3, input_condition=-2)
    IfFlagChange(2, 50006020)
    IfConditionTrue(-3, input_condition=2)
    IfConditionTrue(0, input_condition=-3)
    RestartIfFinishedConditionFalse(2)
    DisableSoundEventWithFade(sound_id=4004450, fade_duration=5.0)
    DisableSoundEventWithFade(sound_id=4004460, fade_duration=5.0)
    Wait(3.0)
    Restart()


@RestartOnRest
def Event1405451():
    """ 1405451: Event 1405451 """
    DisableNetworkSync()
    DisableSoundEvent(4004450)
    DisableSoundEvent(4004460)


def Event14005460():
    """ 14005460: Event 14005460 """
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    GotoIfFlagDisabled(Label.L0, 9400)
    IfActionButtonParam(0, action_button_id=9350, entity=4001460)
    RotateToFaceEntity(PLAYER, 4001460, animation=60070, wait_for_completion=True)
    AwardItemLot(4000, host_only=False)
    DisableFlag(9400)
    Wait(3.0)
    Restart()

    # --- 0 --- #
    DefineLabel(0)
    IfActionButtonParam(0, action_button_id=9350, entity=4001460)
    DisplayDialog(
        10012010,
        anchor_entity=4001460,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(3.0)
    Restart()


@RestartOnRest
def Event14005461():
    """ 14005461: Event 14005461 """
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    DeleteObjectVFX(4001461, erase_root=True)
    IfPlayerHasGood(-1, 119, including_box=False)
    IfMultiplayerNetworkPenalized(-1)
    EndIfConditionTrue(-1)
    CreateObjectVFX(62, obj=4001461, model_point=90)
    IfActionButtonParam(0, action_button_id=4000, entity=4001461)
    RotateToFaceEntity(PLAYER, 4001461, animation=60070, wait_for_completion=True)
    AwardItemLot(4020, host_only=False)
    DeleteObjectVFX(4001461, erase_root=True)


def Event14005470():
    """ 14005470: Event 14005470 """
    DisableNetworkSync()
    IfStandingOnCollision(1, 4004120)
    IfConditionFalse(2, input_condition=1)
    IfInsideMap(2, game_map=FIRELINK_SHRINE)
    IfConditionTrue(0, input_condition=2)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    IfFlagEnabled(3, 743)
    EndIfConditionFalse(3)

    # --- 0 --- #
    DefineLabel(0)
    DisableAreaWelcomeMessage()
    DisplayAreaWelcomeMessage(4010)
    DisableFlag(743)


@RestartOnRest
def Event14005471():
    """ 14005471: Event 14005471 """
    DisableNetworkSync()
    IfFlagDisabled(1, 74000013)
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfStandingOnCollision(-1, 4004120)
    IfConditionFalse(1, input_condition=-1)
    IfCharacterAlive(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    DisableAreaWelcomeMessage()
    Wait(3.0)
    Restart()


@RestartOnRest
def Event14005472():
    """ 14005472: Event 14005472 """
    DisableNetworkSync()
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfCharacterDead(1, PLAYER)
    IfConditionTrue(0, input_condition=1)
    WaitFrames(1)
    EnableAreaWelcomeMessage()
    EnableFlag(743)


@RestartOnRest
def Event14005473():
    """ 14005473: Event 14005473 """
    DisableNetworkSync()
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfCharacterHasSpecialEffect(1, PLAYER, 3220)
    IfConditionTrue(0, input_condition=1)
    EnableAreaWelcomeMessage()
    EnableFlag(743)


@RestartOnRest
def Event14005474():
    """ 14005474: Event 14005474 """
    DisableNetworkSync()
    IfInsideMap(1, game_map=FIRELINK_SHRINE)
    IfFlagEnabled(1, 74000013)
    IfConditionTrue(0, input_condition=1)
    EnableAreaWelcomeMessage()
    EnableFlag(743)


def Event14005480(_, arg_0_3: int):
    """ 14005480: Event 14005480 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_0_3)
    IfFlagEnabled(0, arg_0_3)
    DisableFlag(arg_0_3)
    DisableLoadingScreenTips()
    EnableFlag(30)


@RestartOnRest
def Event14005481():
    """ 14005481: Event 14005481 """
    EndIfPlayerNotInOwnWorld()
    IfInsideMap(0, game_map=FIRELINK_SHRINE)
    EnableLoadingScreenTips()


@RestartOnRest
def Event14005484(_, arg_0_3: int, arg_4_7: int):
    """ 14005484: Event 14005484 """
    DisableNetworkSync()
    IfActionButtonParam(0, action_button_id=9356, entity=arg_4_7)
    DisplayDialog(
        arg_0_3,
        anchor_entity=arg_4_7,
        display_distance=3.0,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.OneButton,
    )
    Wait(3.0)
    Restart()


def Event14000490():
    """ 14000490: Event 14000490 """
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=350,
        item_lot_id=4300,
        trade_completed_flag=70001000,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=2118,
        item_lot_id=4301,
        trade_completed_flag=70001007,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=2143,
        item_lot_id=4302,
        trade_completed_flag=70001001,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=374,
        item_lot_id=4303,
        trade_completed_flag=70001002,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=240,
        item_lot_id=4304,
        trade_completed_flag=6792,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=241,
        item_lot_id=4305,
        trade_completed_flag=6791,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=1250,
        item_lot_id=4306,
        trade_completed_flag=6793,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=13080000,
        item_lot_id=4307,
        trade_completed_flag=70001003,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=7130000,
        item_lot_id=4308,
        trade_completed_flag=70001004,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=14090000,
        item_lot_id=4309,
        trade_completed_flag=70001005,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=13140000,
        item_lot_id=4310,
        trade_completed_flag=6794,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=13210000,
        item_lot_id=4310,
        trade_completed_flag=6794,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=13220000,
        item_lot_id=4310,
        trade_completed_flag=6794,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=13230000,
        item_lot_id=4310,
        trade_completed_flag=6794,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=13240000,
        item_lot_id=4310,
        trade_completed_flag=6794,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=13250000,
        item_lot_id=4310,
        trade_completed_flag=6794,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=351,
        item_lot_id=4311,
        trade_completed_flag=70001006,
        crow_response_flag=74000996,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=294,
        item_lot_id=4320,
        trade_completed_flag=6790,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=456,
        item_lot_id=4321,
        trade_completed_flag=70001020,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=292,
        item_lot_id=4322,
        trade_completed_flag=70001021,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=299,
        item_lot_id=4322,
        trade_completed_flag=70001021,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=297,
        item_lot_id=4323,
        trade_completed_flag=70001022,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=302,
        item_lot_id=4323,
        trade_completed_flag=70001022,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=300,
        item_lot_id=4324,
        trade_completed_flag=70001023,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=370,
        item_lot_id=4325,
        trade_completed_flag=70001024,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Good,
        item_id=440,
        item_lot_id=4326,
        trade_completed_flag=70001025,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Armor,
        item_id=23500000,
        item_lot_id=4327,
        trade_completed_flag=70001026,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=20040000,
        item_lot_id=4328,
        trade_completed_flag=70001027,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=22050000,
        item_lot_id=4329,
        trade_completed_flag=70001028,
        crow_response_flag=74000997,
    )
    InitializeCrowTrade(
        item_type=ItemType.Weapon,
        item_id=8280000,
        item_lot_id=4330,
        trade_completed_flag=70001029,
        crow_response_flag=74000997,
    )
    InitializeCrowTradeRegion(4002796)
    InitializeCrowTradeRegion(4002797)
    DisableFlag(2040)
    DisableFlag(2041)
    DisableFlag(2042)
    DisableFlag(74000990)


def Event14000491():
    """ 14000491: Event 14000491 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(74000995)
    IfCharacterInsideRegion(0, PLAYER, region=4002795)
    EnableFlag(74000995)
    Wait(1.0)
    IfCharacterOutsideRegion(0, PLAYER, region=4002795)
    DisableFlag(74000995)
    Wait(1.0)
    Restart()


def Event14005800():
    """ 14005800: Event 14005800 """
    EndIfFlagEnabled(14000800)
    IfHealthLessThanOrEqual(0, 4000800, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=4000800, sound_type=SoundType.s_SFX, sound_id=777777777)
    Wait(4.0)
    KillBoss(4000800)
    EnableFlag(14000800)
    EnableFlag(9319)
    EnableFlag(6319)


@RestartOnRest
def Event14005810():
    """ 14005810: Event 14005810 """
    GotoIfFlagDisabled(Label.L0, 14000800)
    Kill(4000800, award_souls=False)
    DisableCharacter(4000800)
    DisableAnimations(4000800)
    DisableMapCollision(4004150)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableAI(4000800)
    DisableHealthBar(4000800)
    EnableInvincibility(4000800)
    SetLockOnPoint(4000800, lock_on_model_point=221, state=False)
    SetCollisionMask(4000800, bit_index=0, switch_type=OnOffChange.Off)
    ForceAnimation(4000800, 30002, loop=True)
    GotoIfFlagEnabled(Label.L1, 14000802)
    IfFlagEnabled(0, 14000802)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(1, 14005805)
    IfCharacterInsideRegion(1, PLAYER, region=4002800)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(4000800, 20002)

    # --- 2 --- #
    DefineLabel(2)
    DisableInvincibility(4000800)
    SetCollisionMask(4000800, bit_index=0, switch_type=OnOffChange.Off)
    IfCharacterHasTAEEvent(-1, 4000800, tae_event_id=40)
    IfThisEventSlotFlagEnabled(-1)
    IfConditionTrue(0, input_condition=-1)
    EnableAI(4000800)
    AddSpecialEffect(4000800, 5800)
    EnableHealthBar(4000800)
    SetNetworkUpdateRate(4000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(4000800, name=905110)
    EnableFlag(14000801)
    End()


def Event14005811():
    """ 14005811: Event 14005811 """
    EndIfFlagEnabled(14000800)
    GotoIfFlagDisabled(Label.L0, 14000802)
    IfCharacterBackreadEnabled(0, 4000800)
    SetDisplayMask(4000800, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(4000800, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(4000800, bit_index=3, switch_type=OnOffChange.Off)
    SetDisplayMask(4000800, bit_index=4, switch_type=OnOffChange.Off)
    End()

    # --- 0 --- #
    DefineLabel(0)
    IfFlagEnabled(-1, 14000802)
    IfActionButtonParam(-1, action_button_id=8900, entity=4000800)
    IfConditionTrue(0, input_condition=-1)
    EndIfFlagEnabled(14000802)
    Move(PLAYER, destination=4000800, destination_type=CoordEntityType.Character, model_point=100, short_move=True)
    ForceAnimation(PLAYER, 60750)
    ForceAnimation(4000800, 20003)
    IfFlagEnabled(-1, 14000802)
    IfCharacterHasTAEEvent(-1, 4000800, tae_event_id=20)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfClientTypeCountComparison(1, ClientType.Invader, ComparisonType.Equal, 0)
    SetNetworkConnectedFlagState(flag=14000802, state=FlagState.On)


@RestartOnRest
def Event14005812():
    """ 14005812: Event 14005812 """
    EndIfFlagEnabled(14000800)
    IfCharacterHasTAEEvent(0, 4000800, tae_event_id=10)
    SetCollisionMask(4000800, bit_index=0, switch_type=OnOffChange.On)
    SetLockOnPoint(4000800, lock_on_model_point=221, state=True)
    EnableFlag(14005802)


@RestartOnRest
def Event14005813():
    """ 14005813: Event 14005813 """
    DisableNetworkSync()
    EndIfFlagEnabled(14000800)
    IfFlagEnabled(1, 14005805)
    IfFlagEnabled(1, 14005802)
    IfConditionTrue(0, input_condition=1)
    Wait(1.5)
    ChangeCamera(normal_camera_id=5110, locked_camera_id=5110)
    IfHealthLessThanOrEqual(0, 4000800, 0.0)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest
def Event14000816():
    """ 14000816: Event 14000816 """
    DisableObjectActivation(4001260, obj_act_id=-1)
    DisableObjectActivation(4001261, obj_act_id=-1)
    EndIfFlagEnabled(64000260)
    IfFlagEnabled(0, 14000800)
    EnableObjectActivation(4001260, obj_act_id=400005)


@RestartOnRest
def Event14005820():
    """ 14005820: Event 14005820 """
    RunCommonEvent(20005800, args=(14000800, 4001800, 4002800, 14005805, 4001800, 4000800, 14000801, 4002800))
    RunCommonEvent(20005801, args=(14000800, 4001800, 4002800, 14005805, 4001800, 14005822))
    RunCommonEvent(20005820, args=(14000800, 4001800, 3, 14000801))
    SkipLinesIfFlagDisabled(2, 14000801)
    RunCommonEvent(20005831, args=(14000800, 14005805, 14005822, 4002800, 4004800, 4004801, 14005802))
    End()
    RunCommonEvent(20001836, args=(14000800, 14005805, 14005822, 14000801, 4004800, 4004801, 14005802))


def Event14005830():
    """ 14005830: Event 14005830 """
    EndIfFlagEnabled(14000830)
    IfHealthLessThanOrEqual(0, 4000830, 0.0)
    Wait(1.0)
    PlaySoundEffect(anchor_entity=4000830, sound_type=SoundType.s_SFX, sound_id=777777777)
    IfCharacterDead(0, 4000830)
    KillBoss(4000830)
    EnableFlag(14000830)
    EnableFlag(9320)
    EnableFlag(6320)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest
def Event14005840():
    """ 14005840: Event 14005840 """
    GotoIfFlagDisabled(Label.L0, 14000830)
    Kill(4000830, award_souls=False)
    DisableAnimations(4000830)
    DisableCharacter(4000830)
    End()

    # --- 0 --- #
    DefineLabel(0)
    EnableInvincibility(4000830)
    DisableAI(4000830)
    SetLockOnPoint(4000830, lock_on_model_point=221, state=False)
    SetCollisionMask(4000830, bit_index=0, switch_type=OnOffChange.Off)
    ForceAnimation(4000830, 30002, loop=True)
    GotoIfFlagEnabled(Label.L1, 14000831)
    IfCharacterInsideRegion(1, PLAYER, region=4002831)
    IfConditionTrue(0, input_condition=1)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    IfFlagEnabled(1, 14005835)
    IfCharacterInsideRegion(1, PLAYER, region=4002800)
    IfConditionTrue(0, input_condition=1)

    # --- 2 --- #
    DefineLabel(2)
    ForceAnimation(4000830, 20002)
    EnableAI(4000830)
    DisableImmortality(4000830)
    DisableInvincibility(4000830)
    SetNetworkUpdateRate(4000830, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(4000830, name=905115)
    EnableFlag(14000831)


def Event14005841():
    """ 14005841: Event 14005841 """
    EndIfFlagEnabled(14000830)
    IfHealthLessThanOrEqual(0, 4000830, 0.5)
    EnableFlag(14005832)


@RestartOnRest
def Event14000842():
    """ 14000842: Event 14000842 """
    WaitFrames(1)
    DisableObjectActivation(4001260, obj_act_id=-1)
    DisableObjectActivation(4001261, obj_act_id=-1)
    EndIfFlagEnabled(64000261)
    IfFlagEnabled(0, 14000830)
    EnableObjectActivation(4001261, obj_act_id=400005)


@RestartOnRest
def Event14000859():
    """ 14000859: Event 14000859 """
    RunCommonEvent(20005800, args=(14000830, 4001800, 4002800, 14005835, 4001830, 4000830, 14000831, 4002831))
    RunCommonEvent(20005801, args=(14000830, 4001800, 4002800, 14005835, 4001830, 14005836))
    RunCommonEvent(20005820, args=(14000830, 4001800, 3, 14000831))
    RunCommonEvent(20005810, args=(14000830, 4001800, 4002800, 10000))
    SkipLinesIfFlagDisabled(2, 14000831)
    RunCommonEvent(20005831, args=(14000830, 14005835, 14005836, 4002800, 4004830, 4004831, 14005832))
    End()
    RunCommonEvent(20001836, args=(14000830, 14005835, 14005836, 14000831, 4004830, 4004831, 14005832))


def Event14005500(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 14005500: Event 14005500 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1235, 1239))
    SetNetworkConnectedFlagRangeState((1235, 1239), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1235, state=FlagState.On)
    IfFlagEnabled(1, 1236)
    IfFlagEnabled(1, 70000063)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1235, 1239), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1235, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1220, 1234))
    SetNetworkConnectedFlagRangeState((1220, 1234), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1220, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1235)
    IfFlagEnabled(2, 1221)
    IfFlagEnabled(2, 74000553)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1220, 1234), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1222, state=FlagState.On)
    IfFlagEnabled(3, 1221)
    IfFlagEnabled(3, 74000583)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1220, 1234), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1223, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000063)
    DisableFlag(74000551)
    SkipLinesIfFlagDisabled(1, 1235)
    DisableFlag(74000570)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1221)
    GotoIfFlagRangeAnyEnabled(Label.L3, (1222, 1234))
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableObject(arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    GotoIfFlagEnabled(Label.L1, 1236)
    GotoIfFlagEnabled(Label.L2, 1238)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()


def Event14005501(_, arg_0_3: int, arg_4_7: int, arg_8_11: uint, arg_12_12: uchar, arg_16_19: uint):
    """ 14005501: Event 14005501 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(arg_0_3)
    IfFlagChange(-1, 73301100)
    IfFlagChange(-1, 73301110)
    IfFlagChange(-1, 73301120)
    IfFlagChange(-1, 73301130)
    IfFlagChange(-1, 73301140)
    IfFlagChange(-1, 73301150)
    IfFlagChange(-1, 73301160)
    IfFlagChange(-1, 73301170)
    IfFlagChange(-1, 73301180)
    IfFlagChange(-1, 73301190)
    IfFlagChange(-1, 73301200)
    IfFlagChange(-1, 73301210)
    IfFlagChange(-1, 73301220)
    IfFlagChange(-1, 73301230)
    IfFlagChange(-1, 73301240)
    IfFlagEnabled(1, 73301250)
    IfFlagEnabled(1, 73301260)
    IfFlagEnabled(1, 73301270)
    IfFlagEnabled(1, 73301280)
    IfFlagEnabled(1, 73301290)
    IfFlagEnabled(1, 73301300)
    IfFlagEnabled(1, 73301310)
    IfFlagEnabled(1, 73301320)
    IfFlagEnabled(1, 73301330)
    IfConditionTrue(0, input_condition=-1)
    IncrementEventValue(arg_4_7, bit_count=arg_8_11, max_value=arg_16_19)
    IfEventValueComparison(-2, arg_4_7, bit_count=arg_12_12, comparison_type=ComparisonType.LessThan, value=arg_16_19)
    RestartIfConditionTrue(-2)
    EnableFlag(arg_0_3)


def Event14005503(_, arg_0_3: int):
    """ 14005503: Event 14005503 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(arg_0_3)
    IfFlagEnabled(1, 73301100)
    IfFlagEnabled(1, 73301110)
    IfFlagEnabled(1, 73301120)
    IfFlagEnabled(1, 73301130)
    IfFlagEnabled(1, 73301140)
    IfFlagEnabled(1, 73301150)
    IfFlagEnabled(1, 73301160)
    IfFlagEnabled(1, 73301170)
    IfFlagEnabled(1, 73301180)
    IfFlagEnabled(1, 73301190)
    IfFlagEnabled(1, 73301200)
    IfFlagEnabled(1, 73301210)
    IfFlagEnabled(1, 73301220)
    IfFlagEnabled(1, 73301230)
    IfFlagEnabled(1, 73301240)
    IfFlagEnabled(1, 73301250)
    IfFlagEnabled(1, 73301260)
    IfFlagEnabled(1, 73301270)
    IfFlagEnabled(1, 73301280)
    IfFlagEnabled(1, 73301290)
    IfFlagEnabled(1, 73301300)
    IfFlagEnabled(1, 73301310)
    IfFlagEnabled(1, 73301320)
    IfFlagEnabled(1, 73301330)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(arg_0_3)


def Event14005520(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 14005520: Event 14005520 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1055, 1059))
    SetNetworkConnectedFlagRangeState((1055, 1059), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1055, state=FlagState.On)
    IfFlagEnabled(1, 1056)
    IfFlagEnabled(1, 70000054)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1055, 1059), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1055, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1040, 1054))
    SetNetworkConnectedFlagRangeState((1040, 1054), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1040, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1055)
    IfFlagEnabled(2, 700)
    IfFlagEnabled(2, 1040)
    IfPlayerRemainingYoelLevelComparison(2, comparison_type=ComparisonType.LessThanOrEqual, value=0)
    IfFlagDisabled(2, 74000124)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1040, 1054), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1041, state=FlagState.On)
    IfFlagEnabled(3, 1041)
    IfFlagEnabled(3, 50006193)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1040, 1054), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1042, state=FlagState.On)
    IfFlagEnabled(9, 1042)
    IfFlagEnabled(9, 74000640)
    SkipLinesIfConditionFalse(2, 9)
    SetNetworkConnectedFlagRangeState((1040, 1054), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1045, state=FlagState.On)
    IfFlagRangeAnyEnabled(4, (1040, 1042))
    IfPlayerRemainingYoelLevelComparison(5, comparison_type=ComparisonType.GreaterThan, value=0)
    IfFlagEnabled(5, 1078)
    IfConditionTrue(-4, input_condition=5)
    IfFlagEnabled(-4, 74000124)
    IfConditionTrue(4, input_condition=-4)
    SkipLinesIfConditionFalse(2, 4)
    SetNetworkConnectedFlagRangeState((1040, 1054), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1044, state=FlagState.On)
    IfFlagEnabled(6, 1041)
    IfFlagRangeAnyEnabled(6, (1340, 1347))
    IfFlagEnabled(6, 1358)
    SkipLinesIfConditionFalse(2, 6)
    SetNetworkConnectedFlagRangeState((1040, 1054), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1044, state=FlagState.On)
    IfFlagRangeAnyEnabled(7, (1041, 1042))
    IfFlagEnabled(7, 1561)
    IfFlagEnabled(7, 1578)
    SkipLinesIfConditionFalse(2, 7)
    SetNetworkConnectedFlagRangeState((1040, 1054), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1043, state=FlagState.On)
    IfFlagEnabled(8, 1043)
    IfFlagEnabled(-8, 74000619)
    IfFlagDisabled(-8, 74000600)
    IfConditionTrue(8, input_condition=-8)
    SkipLinesIfConditionFalse(2, 8)
    SetNetworkConnectedFlagRangeState((1040, 1054), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1044, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000054)
    SkipLinesIfFlagDisabled(1, 1055)
    DisableFlag(74000620)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L1, 1041)
    GotoIfFlagEnabled(Label.L1, 1042)
    GotoIfFlagEnabled(Label.L1, 1043)
    GotoIfFlagEnabled(Label.L2, 1044)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableObject(arg_12_15)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableObject(arg_12_15)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    GotoIfFlagEnabled(Label.L16, 1056)
    GotoIfFlagEnabled(Label.L18, 1058)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    End()

    # --- 16 --- #
    DefineLabel(16)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    EnableTreasure(arg_12_15)
    End()


def Event14005521(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: float,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
):
    """ 14005521: Event 14005521 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_12_15)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfHealthLessThan(2, arg_0_3, arg_16_19)
    IfConditionTrue(-2, input_condition=2)
    IfFlagEnabled(-2, arg_12_15)
    IfConditionTrue(1, input_condition=-2)
    IfFlagEnabled(-3, 1041)
    IfFlagEnabled(-3, 1043)
    IfConditionTrue(1, input_condition=-3)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    GotoIfValueComparison(Label.L0, ComparisonType.Equal, left=1, right=arg_28_31)
    SetNetworkConnectedFlagRangeState((arg_20_23, arg_24_27), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=arg_4_7, state=FlagState.On)
    Goto(Label.L9)

    # --- 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagRangeState((arg_20_23, arg_24_27), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=arg_8_11, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    SaveRequest()
    WaitFrames(1)
    IfCharacterHasSpecialEffect(3, arg_0_3, 159)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(arg_0_3, 0)


def Event14000522():
    """ 14000522: Event 14000522 """
    EndIfPlayerNotInOwnWorld()
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(1, 1055)
    IfFlagRangeAnyEnabled(1, (1041, 1042))
    IfFlagEnabled(1, 74000124)
    IfConditionTrue(0, input_condition=1)
    SetNetworkConnectedFlagRangeState((1040, 1054), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1043, state=FlagState.On)
    SetNetworkConnectedFlagState(flag=74000630, state=FlagState.Off)
    SaveRequest()


def Event14005540(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 14005540: Event 14005540 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1315, 1319))
    SetNetworkConnectedFlagRangeState((1315, 1319), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1315, state=FlagState.On)
    IfFlagEnabled(1, 1316)
    IfFlagEnabled(1, 70000067)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1315, 1319), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1315, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1300, 1314))
    SetNetworkConnectedFlagRangeState((1300, 1314), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1300, state=FlagState.On)
    GotoIfFlagDisabled(Label.L10, 1315)
    IfFlagEnabled(2, 1300)
    IfFlagEnabled(2, 73100304)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1300, 1314), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1301, state=FlagState.On)
    IfFlagEnabled(3, 1301)
    IfFlagEnabled(3, 9307)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1300, 1314), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1302, state=FlagState.On)
    IfFlagEnabled(4, 1302)
    IfFlagEnabled(4, 74000650)
    SkipLinesIfConditionFalse(2, 4)
    SetNetworkConnectedFlagRangeState((1300, 1314), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1303, state=FlagState.On)
    IfFlagRangeAnyEnabled(6, (1301, 1303))
    IfFlagEnabled(6, 1298)
    SkipLinesIfConditionFalse(5, 6)
    SetNetworkConnectedFlagRangeState((1300, 1314), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1302, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1315, 1319), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1317, state=FlagState.On)
    Goto(Label.L9)
    IfFlagEnabled(5, 1303)
    IfFlagEnabled(5, 9308)
    IfFlagDisabled(5, 73101710)
    IfFlagDisabled(5, 73101720)
    IfFlagDisabled(5, 73101730)
    IfFlagDisabled(5, 73101740)
    IfFlagDisabled(5, 73101750)
    SkipLinesIfConditionFalse(4, 5)
    SetNetworkConnectedFlagRangeState((1300, 1314), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1305, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1315, 1319), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1318, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000067)
    SkipLinesIfFlagDisabled(1, 1315)
    DisableFlag(74000670)

    # --- 10 --- #
    DefineLabel(10)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    Move(arg_4_7, destination=arg_16_19, destination_type=CoordEntityType.Region, copy_draw_parent=arg_4_7)
    GotoIfFlagEnabled(Label.L2, 1302)
    GotoIfFlagEnabled(Label.L4, 1304)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    GotoIfFlagEnabled(Label.L16, 1316)
    GotoIfFlagEnabled(Label.L17, 1317)
    GotoIfFlagEnabled(Label.L18, 1318)
    ForceAnimation(arg_0_3, arg_8_11, loop=True, skip_transition=True)
    End()

    # --- 16 --- #
    DefineLabel(16)

    # --- 17 --- #
    DefineLabel(17)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 4 --- #
    DefineLabel(4)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    GotoIfFlagEnabled(Label.L18, 1318)
    DisableAI(arg_4_7)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    WaitFrames(1)
    DropMandatoryTreasure(arg_4_7)
    End()


def Event14005541(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
    arg_32_35: int,
):
    """ 14005541: Event 14005541 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, arg_32_35)
    IfFlagEnabled(-1, arg_24_27)
    IfFlagEnabled(-1, arg_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfFlagRangeAnyEnabled(1, (arg_12_15, arg_16_19))
    IfFlagEnabled(1, arg_20_23)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    SetNetworkConnectedFlagRangeState((arg_24_27, arg_28_31), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=arg_8_11, state=FlagState.On)
    SaveRequest()
    WaitFrames(1)
    IfCharacterHasSpecialEffect(-15, arg_0_3, 159)
    SkipLinesIfConditionFalse(2, -15)
    ForceAnimation(arg_0_3, 0)


def Event14005542(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 14005542: Event 14005542 """
    EndIfPlayerNotInOwnWorld()
    IfFlagRangeAnyEnabled(1, (1301, 1303))
    IfFlagEnabled(1, 1315)
    IfFlagRangeAnyEnabled(1, (1282, 1283))
    IfFlagEnabled(1, 1295)
    IfFlagEnabled(1, 74000351)
    IfPlayerInOwnWorld(1)
    EndIfConditionFalse(1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SetNetworkConnectedFlagRangeState((1300, 1314), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1304, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1315, 1319), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1317, state=FlagState.On)
    GotoIfFlagDisabled(Label.L0, 1282)
    SetNetworkConnectedFlagRangeState((1280, 1294), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1284, state=FlagState.On)
    Goto(Label.L1)

    # --- 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagRangeState((1280, 1294), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1285, state=FlagState.On)

    # --- 1 --- #
    DefineLabel(1)

    # --- 10 --- #
    DefineLabel(10)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    EnableCharacter(arg_4_7)
    EnableBackread(arg_4_7)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    DisableAI(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableBackread(arg_8_11)
    EnableCharacter(arg_12_15)
    EnableBackread(arg_12_15)
    SetTeamType(arg_12_15, TeamType.NoTeam)
    ForceAnimation(arg_12_15, arg_16_19, loop=True)


def Event14005543(_, arg_0_3: int):
    """ 14005543: Event 14005543 """
    IfFlagEnabled(1, 1304)
    IfFlagDisabled(1, 1318)
    IfEntityWithinDistance(2, arg_0_3, PLAYER, radius=10.0)
    IfConditionTrue(-1, input_condition=2)
    IfAttackedWithDamageType(-1, attacked_entity=arg_0_3, attacker=PLAYER)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    EnableAI(arg_0_3)
    ReplanAI(arg_0_3)
    WaitFrames(1)
    IfCharacterHasSpecialEffect(-2, arg_0_3, 159)
    IfHasAIStatus(-2, arg_0_3, ai_status=AIStatusType.Normal)
    SkipLinesIfConditionFalse(1, -2)
    RotateToFaceEntity(arg_0_3, PLAYER, animation=-1, wait_for_completion=True)


def Event14005560(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 14005560: Event 14005560 """
    DisableAnimations(4000762)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1115, 1119))
    SetNetworkConnectedFlagRangeState((1115, 1119), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1115, state=FlagState.On)
    IfFlagEnabled(1, 1116)
    IfFlagEnabled(1, 70000057)
    SkipLinesIfConditionFalse(3, 1)
    SetNetworkConnectedFlagRangeState((1115, 1119), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1115, state=FlagState.On)
    DisableFlagRange((74000848, 74000849))
    SkipLinesIfFlagRangeAnyEnabled(2, (1100, 1114))
    SetNetworkConnectedFlagRangeState((1100, 1114), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1100, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1115)
    IfFlagEnabled(2, 1100)
    IfFlagEnabled(-1, 9303)
    IfFlagEnabled(-1, 9306)
    IfConditionTrue(2, input_condition=-1)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1100, 1114), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1101, state=FlagState.On)
    IfFlagEnabled(3, 1101)
    IfFlagEnabled(3, 9307)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1100, 1114), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1102, state=FlagState.On)
    IfFlagEnabled(5, 1102)
    IfFlagEnabled(5, 74000808)
    SkipLinesIfConditionFalse(3, 5)
    SetNetworkConnectedFlagRangeState((1100, 1114), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1103, state=FlagState.On)
    EnableFlag(74000825)
    IfFlagEnabled(6, 1103)
    IfPlayerHasGood(6, 388, including_box=False)
    IfFlagEnabled(6, 53200900)
    SkipLinesIfConditionFalse(6, 6)
    SetNetworkConnectedFlagRangeState((1100, 1114), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1104, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1115, 1119), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1117, state=FlagState.On)
    EnableFlag(50006071)
    EnableFlag(74000201)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000057)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1100)
    GotoIfFlagEnabled(Label.L0, 1101)
    GotoIfFlagEnabled(Label.L0, 1102)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagRangeAnyEnabled(4, (1116, 1118))
    DisableFlagRange((74000810, 74000813))
    IfFlagDisabled(-2, 74000801)
    GotoIfConditionTrue(Label.L1, input_condition=-2)
    EnableRandomFlagInRange((74000810, 74000813))
    SkipLinesIfFlagDisabled(1, 74000820)
    EnableFlag(74000810)
    GotoIfFlagDisabled(Label.L1, 74000810)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    Move(arg_4_7, destination=arg_12_15, destination_type=CoordEntityType.Region, copy_draw_parent=arg_4_7)
    DisableCharacter(4000366)
    DisableBackread(4000366)
    SkipLinesIfFlagRangeAnyEnabled(1, (1116, 1118))
    ForceAnimation(arg_4_7, 90960, skip_transition=True)
    Goto(Label.L17)

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    SkipLinesIfFlagRangeAnyEnabled(1, (1116, 1118))
    ForceAnimation(arg_0_3, 90680, skip_transition=True)

    # --- 17 --- #
    DefineLabel(17)
    GotoIfFlagEnabled(Label.L19, 1116)
    GotoIfFlagEnabled(Label.L19, 1117)
    GotoIfFlagEnabled(Label.L20, 1118)
    End()

    # --- 19 --- #
    DefineLabel(19)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    End()

    # --- 20 --- #
    DefineLabel(20)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    WaitFrames(1)
    SkipLinesIfFlagEnabled(2, 74000810)
    DropMandatoryTreasure(arg_0_3)
    End()
    DropMandatoryTreasure(arg_4_7)
    End()


def Event14005570(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 14005570: Event 14005570 """
    GotoIfPlayerNotInOwnWorld(Label.L20)
    SkipLinesIfFlagRangeAnyEnabled(2, (1135, 1139))
    SetNetworkConnectedFlagRangeState((1135, 1139), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1135, state=FlagState.On)
    IfFlagEnabled(1, 1136)
    IfFlagEnabled(1, 70000058)
    SkipLinesIfConditionFalse(3, 1)
    SetNetworkConnectedFlagRangeState((1135, 1139), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1135, state=FlagState.On)
    DisableFlag(74000799)
    SkipLinesIfFlagRangeAnyEnabled(2, (1120, 1134))
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1120, state=FlagState.On)
    GotoIfFlagDisabled(Label.L19, 1135)
    IfFlagEnabled(3, 1120)
    IfFlagEnabled(3, 133)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1121, state=FlagState.On)
    IfFlagEnabled(4, 1121)
    IfFlagEnabled(4, 74000750)
    SkipLinesIfConditionFalse(2, 4)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1122, state=FlagState.On)
    IfFlagEnabled(5, 1122)
    IfFlagEnabled(5, 74000253)
    SkipLinesIfConditionFalse(2, 5)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1123, state=FlagState.On)
    IfFlagEnabled(6, 1123)
    IfFlagEnabled(6, 74000751)
    SkipLinesIfConditionFalse(2, 6)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1124, state=FlagState.On)
    IfFlagEnabled(7, 1124)
    IfFlagEnabled(7, 8200)
    SkipLinesIfConditionFalse(2, 7)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1125, state=FlagState.On)
    IfFlagEnabled(8, 1125)
    IfFlagEnabled(8, 74000752)
    SkipLinesIfConditionFalse(2, 8)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1126, state=FlagState.On)
    IfFlagEnabled(-1, 1124)
    IfFlagEnabled(-1, 1126)
    IfConditionTrue(9, input_condition=-1)
    IfFlagEnabled(9, 8220)
    SkipLinesIfConditionFalse(3, 9)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1127, state=FlagState.On)
    EnableFlag(74000790)
    IfFlagEnabled(10, 1127)
    IfFlagEnabled(10, 74000755)
    SkipLinesIfConditionFalse(2, 10)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1128, state=FlagState.On)
    IfFlagEnabled(11, 1127)
    IfFlagEnabled(11, 74000760)
    IfFlagEnabled(11, 74000756)
    SkipLinesIfConditionFalse(3, 11)
    SetNetworkConnectedFlagRangeState((1120, 1139), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1130, state=FlagState.On)
    SetNetworkConnectedFlagState(flag=1137, state=FlagState.On)
    IfFlagEnabled(12, 1128)
    IfFlagEnabled(12, 9309)
    SkipLinesIfConditionFalse(3, 12)
    SetNetworkConnectedFlagRangeState((1120, 1139), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1129, state=FlagState.On)
    SetNetworkConnectedFlagState(flag=1138, state=FlagState.On)
    IfFlagEnabled(-2, 1120)
    IfFlagEnabled(-2, 1121)
    IfConditionTrue(13, input_condition=-2)
    IfFlagEnabled(13, 73500150)
    SkipLinesIfConditionFalse(2, 13)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1134, state=FlagState.On)
    IfFlagRangeAnyEnabled(14, (1122, 1128))
    IfFlagEnabled(14, 73500150)
    SkipLinesIfConditionFalse(2, 14)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1133, state=FlagState.On)
    IfFlagEnabled(15, 1133)
    IfFlagEnabled(15, 74000753)
    SkipLinesIfConditionFalse(2, 15)
    SetNetworkConnectedFlagRangeState((1120, 1134), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1134, state=FlagState.On)

    # --- 19 --- #
    DefineLabel(19)
    DisableFlag(70000058)

    # --- 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L0, 1121)
    GotoIfFlagEnabled(Label.L1, 1123)
    GotoIfFlagEnabled(Label.L2, 1125)
    GotoIfFlagEnabled(Label.L3, 1127)
    GotoIfFlagEnabled(Label.L4, 1129)
    GotoIfFlagEnabled(Label.L5, 1133)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)

    # --- 1 --- #
    DefineLabel(1)

    # --- 2 --- #
    DefineLabel(2)

    # --- 3 --- #
    DefineLabel(3)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    SkipLinesIfFlagRangeAnyEnabled(1, (1136, 1138))
    ForceAnimation(arg_0_3, 90340, skip_transition=True)
    Goto(Label.L18)

    # --- 5 --- #
    DefineLabel(5)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    SkipLinesIfFlagEnabled(2, 1127)
    RunCommonEvent(20006000, args=(4000780, 1136, 1137, 74000770, 1060320051, 1135, 1139, 0))
    RunCommonEvent(20006001, args=(4000780, 1136, 1137, 74000770, 3))
    GotoIfFlagEnabled(Label.L19, 1136)
    GotoIfFlagEnabled(Label.L19, 1137)
    GotoIfFlagEnabled(Label.L20, 1138)
    End()

    # --- 4 --- #
    DefineLabel(4)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    Move(arg_4_7, destination=arg_12_15, destination_type=CoordEntityType.Region, copy_draw_parent=arg_4_7)
    WaitFrames(1)
    DropMandatoryTreasure(arg_4_7)
    EzstateAIRequest(arg_4_7, command_id=800, slot=1)
    End()

    # --- 19 --- #
    DefineLabel(19)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 20 --- #
    DefineLabel(20)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()


@RestartOnRest
def Event14005571():
    """ 14005571: Event 14005571 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(70000116)
    IfFlagEnabled(1, 1124)
    IfFlagEnabled(1, 9303)
    IfFlagEnabled(1, 9314)
    SkipLinesIfConditionFalse(1, 1)
    EnableFlag(70000118)


def Event14005580(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: int):
    """ 14005580: Event 14005580 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1355, 1359))
    SetNetworkConnectedFlagRangeState((1355, 1359), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1355, state=FlagState.On)
    IfFlagEnabled(1, 1356)
    IfFlagEnabled(1, 70000069)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1355, 1359), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1355, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1340, 1354))
    SetNetworkConnectedFlagRangeState((1340, 1354), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1340, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1355)
    IfFlagEnabled(2, 1340)
    IfFlagEnabled(2, 73300151)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1340, 1354), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1341, state=FlagState.On)
    IfFlagEnabled(3, 1341)
    IfFlagEnabled(3, 9311)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1340, 1354), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1342, state=FlagState.On)
    IfFlagEnabled(4, 1342)
    IfFlagEnabled(4, 74000700)
    SkipLinesIfConditionFalse(2, 4)
    SetNetworkConnectedFlagRangeState((1340, 1354), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1344, state=FlagState.On)
    IfFlagEnabled(5, 1350)
    IfFlagEnabled(5, 8260)
    SkipLinesIfConditionFalse(3, 5)
    SetNetworkConnectedFlagRangeState((1340, 1354), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1351, state=FlagState.On)
    EnableFlag(74000180)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000069)
    SkipLinesIfFlagDisabled(1, 1355)
    DisableFlag(74000720)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1342)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=arg_16_19, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    Move(arg_4_7, destination=arg_20_23, destination_type=CoordEntityType.Region, copy_draw_parent=arg_4_7)
    GotoIfFlagEnabled(Label.L1, 1356)
    GotoIfFlagEnabled(Label.L2, 1357)
    GotoIfFlagEnabled(Label.L3, 1358)
    GotoIfFlagDisabled(Label.L20, 9013)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    ForceAnimation(arg_0_3, arg_8_11)
    End()

    # --- 20 --- #
    DefineLabel(20)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    ForceAnimation(arg_4_7, arg_8_11)
    End()

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L20, 9013)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 20 --- #
    DefineLabel(20)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L20, 9013)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    ForceAnimation(arg_0_3, arg_12_15)
    DisableAI(arg_0_3)
    End()

    # --- 20 --- #
    DefineLabel(20)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    ForceAnimation(arg_4_7, arg_12_15)
    DisableAI(arg_4_7)
    End()

    # --- 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L20, 9013)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 20 --- #
    DefineLabel(20)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    WaitFrames(1)
    DropMandatoryTreasure(arg_4_7)
    End()


def Event14005581(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int, arg_20_23: float):
    """ 14005581: Event 14005581 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_12_15)
    DisableFlag(arg_16_19)
    IfFlagRangeAllDisabled(1, (1356, 1357))
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfHealthGreaterThan(1, arg_4_7, 0.0)
    IfFlagEnabled(1, 1342)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfHealthLessThan(2, arg_0_3, arg_20_23)
    IfConditionTrue(-1, input_condition=2)
    IfAttackedWithDamageType(3, attacked_entity=arg_4_7, attacker=PLAYER)
    IfHealthLessThan(3, arg_4_7, arg_20_23)
    IfConditionTrue(-1, input_condition=3)
    IfFlagEnabled(-1, arg_12_15)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(-3, input_condition=1)
    IfFlagRangeAllDisabled(4, (1496, 1497))
    IfHealthGreaterThan(4, arg_8_11, 0.0)
    IfFlagEnabled(4, 1482)
    IfAttackedWithDamageType(5, attacked_entity=arg_8_11, attacker=PLAYER)
    IfHealthLessThan(5, arg_8_11, arg_20_23)
    IfConditionTrue(-2, input_condition=5)
    IfFlagEnabled(-2, arg_16_19)
    IfConditionTrue(4, input_condition=-2)
    IfConditionTrue(-3, input_condition=4)
    IfConditionTrue(0, input_condition=-3)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    SetTeamType(arg_8_11, TeamType.HostileNPC)
    SetNetworkConnectedFlagRangeState((1355, 1359), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1356, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1495, 1499), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1496, state=FlagState.On)
    SaveRequest()
    WaitFrames(1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, special_effect=159)
    ForceAnimation(arg_0_3, 0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(1, arg_4_7, special_effect=159)
    ForceAnimation(arg_4_7, 0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(1, arg_8_11, special_effect=159)
    ForceAnimation(arg_8_11, 0)


def Event14005582(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: float,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
    arg_32_35: int,
):
    """ 14005582: Event 14005582 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_12_15)
    IfFlagDisabled(1, arg_4_7)
    IfFlagDisabled(1, arg_8_11)
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfFlagEnabled(1, arg_32_35)
    IfAttackedWithDamageType(2, attacked_entity=arg_0_3, attacker=PLAYER)
    IfHealthLessThan(2, arg_0_3, arg_16_19)
    IfConditionTrue(-1, input_condition=2)
    IfFlagEnabled(-1, arg_12_15)
    IfFlagEnabled(-1, arg_28_31)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    SetNetworkConnectedFlagRangeState((arg_20_23, arg_24_27), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=arg_4_7, state=FlagState.On)
    SaveRequest()
    WaitFrames(1)
    IfCharacterHasSpecialEffect(3, arg_0_3, 159)
    SkipLinesIfConditionFalse(1, 3)
    ForceAnimation(arg_0_3, 0)


def Event14000583(
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
    """ 14000583: Event 14000583 """
    EndIfPlayerNotInOwnWorld()
    EndIfThisEventFlagEnabled()
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfHealthGreaterThan(1, arg_4_7, 0.0)
    IfFlagEnabled(1, arg_28_31)
    IfFlagEnabled(-1, arg_20_23)
    IfFlagEnabled(-1, arg_8_11)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterDead(1, arg_16_19)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    IfCharacterHasSpecialEffect(-15, arg_0_3, 150)
    SkipLinesIfConditionFalse(1, 0)
    ForceAnimation(arg_0_3, 0)
    IfCharacterHasSpecialEffect(-14, arg_0_3, 150)
    SkipLinesIfConditionFalse(1, 0)
    ForceAnimation(arg_4_7, 0)
    AICommand(arg_0_3, command_id=20, slot=1)
    ReplanAI(arg_0_3)
    AICommand(arg_4_7, command_id=20, slot=1)
    ReplanAI(arg_4_7)
    SetNetworkConnectedFlagRangeState((arg_20_23, arg_24_27), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=arg_12_15, state=FlagState.On)
    SaveRequest()


def Event14005584(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 14005584: Event 14005584 """
    EndIfPlayerNotInOwnWorld()
    IfCharacterHasSpecialEffect(-1, arg_0_3, 150)
    IfCharacterHasSpecialEffect(-1, arg_0_3, 151)
    IfCharacterHasSpecialEffect(-1, arg_4_7, 150)
    IfCharacterHasSpecialEffect(-1, arg_4_7, 151)
    EndIfConditionTrue(-1)
    IfFlagEnabled(1, arg_8_11)
    IfFlagEnabled(1, arg_12_15)
    IfConditionTrue(0, input_condition=1)
    EzstateAIRequest(arg_0_3, command_id=1903, slot=1)
    EzstateAIRequest(arg_4_7, command_id=1903, slot=1)
    WaitFrames(10)
    Restart()


def Event14000585(
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
    """ 14000585: Event 14000585 """
    EndIfPlayerNotInOwnWorld()
    EndIfThisEventFlagEnabled()
    IfHealthGreaterThan(1, arg_0_3, 0.0)
    IfFlagEnabled(1, arg_28_31)
    IfFlagEnabled(-1, arg_20_23)
    IfFlagEnabled(-1, arg_4_7)
    IfConditionTrue(1, input_condition=-1)
    IfCharacterDead(-2, arg_12_15)
    IfCharacterDead(-2, arg_16_19)
    IfConditionTrue(1, input_condition=-2)
    IfConditionTrue(0, input_condition=1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    IfCharacterHasSpecialEffect(-15, arg_0_3, 150)
    SkipLinesIfConditionFalse(2, 0)
    ForceAnimation(arg_0_3, 0)
    ReplanAI(arg_0_3)
    SetNetworkConnectedFlagRangeState((arg_20_23, arg_24_27), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=arg_8_11, state=FlagState.On)
    SaveRequest()


def Event14005586(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 14005586: Event 14005586 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1495, 1499))
    SetNetworkConnectedFlagRangeState((1495, 1499), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1495, state=FlagState.On)
    IfFlagEnabled(1, 1496)
    IfFlagEnabled(1, 70000076)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1495, 1499), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1495, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1480, 1494))
    SetNetworkConnectedFlagRangeState((1480, 1494), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1480, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1495)
    IfFlagEnabled(2, 1480)
    IfFlagEnabled(2, 73300151)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1480, 1494), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1481, state=FlagState.On)
    IfFlagEnabled(3, 1481)
    IfFlagEnabled(3, 9311)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1480, 1494), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1482, state=FlagState.On)
    IfFlagEnabled(4, 1482)
    IfFlagEnabled(4, 74000700)
    SkipLinesIfConditionFalse(2, 4)
    SetNetworkConnectedFlagRangeState((1480, 1494), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1484, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000076)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1482)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    GotoIfFlagEnabled(Label.L1, 1496)
    GotoIfFlagEnabled(Label.L1, 1497)
    GotoIfFlagEnabled(Label.L3, 1498)
    ForceAnimation(arg_0_3, arg_4_7)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()


@RestartOnRest
def Event14005587(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 14005587: Event 14005587 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_8_11)
    IfCharacterHasSpecialEffect(1, arg_0_3, 151)
    IfConditionTrue(0, input_condition=1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    WaitFrames(1)
    IfAttackedWithDamageType(0, attacked_entity=arg_0_3, attacker=PLAYER)
    Kill(arg_0_3, award_souls=True)


def Event14005600(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int, arg_16_19: int):
    """ 14005600: Event 14005600 """
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(2, (1015, 1019))
    SetNetworkConnectedFlagRangeState((1015, 1019), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1015, state=FlagState.On)
    IfFlagEnabled(1, 1018)
    IfCharacterAlive(1, arg_0_3)
    SkipLinesIfConditionFalse(4, 1)
    SetNetworkConnectedFlagRangeState((1015, 1019), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1015, state=FlagState.On)
    EnableFlag(74000121)
    EnableFlag(74000100)
    SkipLinesIfFlagRangeAnyEnabled(2, (1000, 1014))
    SetNetworkConnectedFlagRangeState((1000, 1014), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1000, state=FlagState.On)
    IfFlagEnabled(2, 1001)
    IfFlagEnabled(2, 145)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1000, 1014), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1002, state=FlagState.On)
    DisableFlagRange((74000135, 74000138))
    DisableFlagRange((74000103, 74000109))

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L16, 74000147)
    GotoIfFlagEnabled(Label.L15, 74000148)
    GotoIfFlagEnabled(Label.L17, 74000149)
    IfFlagEnabled(3, 1000)
    IfFlagEnabled(3, 131)
    GotoIfConditionTrue(Label.L1, input_condition=3)
    GotoIfFlagEnabled(Label.L0, 1000)
    GotoIfFlagEnabled(Label.L2, 1001)
    GotoIfFlagEnabled(Label.L1, 1002)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L10, 1018)
    End()

    # --- 10 --- #
    DefineLabel(10)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 2 --- #
    DefineLabel(2)
    Move(arg_0_3, destination=arg_16_19, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L10, 1018)
    End()

    # --- 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L10, 1018)
    EnableRandomFlagInRange((74000103, 74000109))
    GotoIfFlagEnabled(Label.L16, 74000103)
    GotoIfFlagEnabled(Label.L16, 74000104)
    IfFlagEnabled(5, 74000105)
    IfFlagDisabled(5, 50006020)
    GotoIfConditionTrue(Label.L17, input_condition=5)

    # --- 15 --- #
    DefineLabel(15)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 16 --- #
    DefineLabel(16)
    ForceAnimation(arg_0_3, 700, loop=True, skip_transition=True)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 17 --- #
    DefineLabel(17)
    ForceAnimation(arg_0_3, 30001)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 10 --- #
    DefineLabel(10)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()


def Event14000601(_, arg_0_3: int):
    """ 14000601: Event 14000601 """
    EndIfPlayerNotInOwnWorld()
    EndIfThisEventFlagEnabled()
    EnableFlag(arg_0_3)


def Event14005602(_, arg_0_3: int, arg_4_7: int):
    """ 14005602: Event 14005602 """
    EndIfPlayerNotInOwnWorld()
    IfCharacterDead(0, arg_0_3)
    AwardItemLot(arg_4_7, host_only=False)
    DisableFlag(74000130)
    DisableFlag(74000131)


def Event14000603(_, arg_0_3: int, arg_4_7: int):
    """ 14000603: Event 14000603 """
    EndIfPlayerNotInOwnWorld()
    EndIfThisEventFlagEnabled()
    IfFlagEnabled(0, arg_0_3)
    EnableFlag(arg_4_7)


def Event14005604(_, arg_0_3: int, arg_4_7: int):
    """ 14005604: Event 14005604 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, 1000)
    IfFlagEnabled(1, 9210)
    IfConditionTrue(0, input_condition=1)
    SetNest(arg_0_3, arg_4_7)
    WaitFrames(1)
    SetNetworkConnectedFlagRangeState((1000, 1014), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1001, state=FlagState.On)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(2, arg_0_3, special_effect=151)
    ForceAnimation(arg_0_3, 20017, wait_for_completion=True)
    SkipLines(2)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, special_effect=153)
    ForceAnimation(arg_0_3, 20019, wait_for_completion=True)
    AICommand(arg_0_3, command_id=100, slot=0)
    ReplanAI(arg_0_3)
    IfCharacterHasSpecialEffect(0, arg_0_3, 154)
    IfCharacterDoesNotHaveSpecialEffect(0, arg_0_3, 154)
    AICommand(arg_0_3, command_id=-1, slot=0)


def Event14005605(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 14005605: Event 14005605 """
    EndIfPlayerNotInOwnWorld()
    IfEntityWithinDistance(1, PLAYER, arg_0_3, radius=5.0)
    IfCharacterHasSpecialEffect(1, arg_0_3, 150)
    IfCharacterHasSpecialEffect(1, PLAYER, arg_4_7)
    IfConditionTrue(0, input_condition=1)
    ForceAnimation(arg_0_3, arg_8_11, wait_for_completion=True)
    Restart()


@RestartOnRest
def Event14005615(_, arg_0_3: int):
    """ 14005615: Event 14005615 """
    EndIfPlayerNotInOwnWorld()
    DisableSoundEvent(4003700)
    DisableSoundEvent(4003701)
    IfCharacterHasSpecialEffect(0, arg_0_3, 155)
    IfPlayerGender(1, Gender.Male)
    SkipLinesIfConditionFalse(2, 1)
    EnableSoundEvent(4003700)
    SkipLines(1)
    EnableSoundEvent(4003701)
    IfCharacterDoesNotHaveSpecialEffect(0, arg_0_3, 155)
    Restart()


@RestartOnRest
def Event14005616(_, arg_0_3: int):
    """ 14005616: Event 14005616 """
    DisableFlag(74000139)
    IfFlagEnabled(0, 74000139)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(1, arg_0_3, special_effect=153)
    ForceAnimation(arg_0_3, 20018)
    Restart()


def Event14005618():
    """ 14005618: Event 14005618 """
    EndIfFlagDisabled(14005617)
    EnableFlag(14000618)


def Event14005619():
    """ 14005619: Event 14005619 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(6500)
    IfFlagEnabled(0, 6500)
    SkipLinesIfFlagDisabled(2, 74000015)
    ForceAnimation(4001950, 10)
    End()
    SkipLinesIfFlagDisabled(2, 74000016)
    ForceAnimation(4001950, 20)
    End()
    SkipLinesIfFlagDisabled(2, 74000017)
    ForceAnimation(4001950, 30)
    End()
    SkipLinesIfFlagDisabled(2, 74000018)
    ForceAnimation(4001950, 40)
    End()
    SkipLinesIfFlagDisabled(2, 74000019)
    ForceAnimation(4001950, 50)
    End()
    SkipLinesIfFlagDisabled(2, 74000020)
    ForceAnimation(4001950, 60)
    End()
    SkipLinesIfFlagDisabled(2, 74000021)
    ForceAnimation(4001950, 70)
    End()
    SkipLinesIfFlagDisabled(2, 74000022)
    ForceAnimation(4001950, 80)
    End()
    SkipLinesIfFlagDisabled(2, 74000023)
    ForceAnimation(4001950, 90)
    End()
    SkipLinesIfFlagDisabled(2, 74000024)
    ForceAnimation(4001950, 100)
    End()
    ForceAnimation(4001950, 9900)
    End()


def Event14005620(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 14005620: Event 14005620 """
    GotoIfPlayerNotInOwnWorld(Label.L20)
    EnableFlag(64001251)
    DisableFlag(74000919)
    SkipLinesIfFlagRangeAnyEnabled(2, (1375, 1379))
    SetNetworkConnectedFlagRangeState((1375, 1379), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1375, state=FlagState.On)
    IfFlagEnabled(15, 1376)
    IfFlagEnabled(15, 70000070)
    SkipLinesIfConditionFalse(2, 15)
    SetNetworkConnectedFlagRangeState((1375, 1379), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1375, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1360, 1374))
    SetNetworkConnectedFlagRangeState((1360, 1374), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1360, state=FlagState.On)
    GotoIfFlagDisabled(Label.L19, 1375)
    IfFlagEnabled(1, 1365)
    IfFlagEnabled(1, 1204)
    IfFlagEnabled(1, 74000920)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1360, 1374), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1366, state=FlagState.On)
    IfFlagEnabled(2, 1366)
    IfFlagEnabled(2, 1206)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1360, 1374), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1365, state=FlagState.On)
    IfFlagEnabled(3, 1365)
    IfFlagEnabled(3, 1207)
    IfFlagEnabled(3, 74000921)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1360, 1374), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1367, state=FlagState.On)
    IfFlagEnabled(4, 1367)
    IfFlagEnabled(4, 74000925)
    SkipLinesIfConditionFalse(4, 4)
    SetNetworkConnectedFlagRangeState((1360, 1374), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1365, state=FlagState.On)
    EnableFlag(74000914)
    EnableFlag(70000401)

    # --- 19 --- #
    DefineLabel(19)
    DisableFlag(70000070)
    SkipLinesIfFlagDisabled(1, 1375)
    DisableFlag(74000949)

    # --- 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L0, 1364)
    GotoIfFlagEnabled(Label.L1, 1365)
    GotoIfFlagEnabled(Label.L2, 1370)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    DisableAnimations(arg_0_3)
    GotoIfFlagEnabled(Label.L18, 1378)
    GotoIfFlagRangeAnyEnabled(Label.L17, (1376, 1377))
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_4_7)
    SkipLinesIfFlagDisabled(3, 74000916)
    SkipLinesIfFlagRangeAnyEnabled(2, (1376, 1378))
    ForceAnimation(arg_4_7, 90810, skip_transition=True)
    EnableFlag(74000917)
    GotoIfFlagEnabled(Label.L18, 1378)
    GotoIfFlagRangeAnyEnabled(Label.L17, (1376, 1377))
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_4_7)
    GotoIfFlagEnabled(Label.L18, 1378)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    WaitFrames(1)
    Move(arg_4_7, destination=4002714, destination_type=CoordEntityType.Region, copy_draw_parent=arg_4_7)
    SetNest(arg_4_7, 4002714)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    WaitFrames(1)
    DropMandatoryTreasure(arg_4_7)
    End()

    # --- 17 --- #
    DefineLabel(17)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    SetTeamType(arg_4_7, TeamType.HostileNPC)
    End()


@RestartOnRest
def Event14000621(_, arg_0_3: int):
    """ 14000621: Event 14000621 """
    GotoIfFlagEnabled(Label.L1, 1364)
    SkipLinesIfClientTypeCountComparison(2, ClientType.Invader, ComparisonType.Equal, 0)
    EnableFlag(64001251)
    EnableFlag(14000623)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=0)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=1)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=2)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=3)
    EndOfAnimation(4001251, 0)
    Goto(Label.L2)

    # --- 1 --- #
    DefineLabel(1)
    EndOfAnimation(4001251, 1)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=0)
    EnableObjectActivation(4001251, obj_act_id=1400340, relative_index=1)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=2)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=3)

    # --- 2 --- #
    DefineLabel(2)
    EndIfThisEventFlagEnabled()
    IfPlayerInOwnWorld(1)
    IfCharacterInsideRegion(1, PLAYER, region=4002710)
    IfFlagRangeAnyEnabled(1, (1360, 1363))
    IfFlagEnabled(1, 1375)
    IfFlagEnabled(2, 138)
    IfFlagEnabled(2, 9311)
    IfFlagEnabled(-1, 1363)
    IfFlagEnabled(-1, 73500262)
    IfFlagEnabled(-1, 73500263)
    IfConditionTrue(-1, input_condition=2)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(0, input_condition=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    SetNetworkConnectedFlagRangeState((1360, 1374), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1364, state=FlagState.On)
    DisableFlag(64001251)
    DisableFlag(14000623)
    PlaySoundEffect(anchor_entity=4001251, sound_type=SoundType.a_Ambient, sound_id=400100000)

    # --- 0 --- #
    DefineLabel(0)
    EnableCharacter(arg_0_3)
    EnableBackread(arg_0_3)
    DisableAnimations(arg_0_3)
    EnableObjectActivation(4001251, obj_act_id=1400340, relative_index=1)
    ForceAnimation(4001251, 1)
    RunCommonEvent(20005610, args=(14000623, 4002713, 4002712))
    RunCommonEvent(20005611, args=(14000623, 4003251, 4001251, 1400340))


@RestartOnRest
def Event14000622(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 14000622: Event 14000622 """
    EndIfThisEventFlagEnabled()
    IfPlayerInOwnWorld(1)
    IfCharacterOutsideRegion(1, PLAYER, region=4002711)
    IfFlagEnabled(1, 1364)
    IfFlagEnabled(1, 1375)
    IfConditionTrue(0, input_condition=1)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    SetNetworkConnectedFlagRangeState((1360, 1374), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1365, state=FlagState.On)
    EnableFlag(70000400)

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    EnableCharacter(arg_4_7)
    EnableBackread(arg_4_7)
    Move(arg_4_7, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_4_7)
    EnableObjectActivation(4001251, obj_act_id=1400340, relative_index=0)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=1)
    RunCommonEvent(20005610, args=(14000623, 4002713, 4002712))
    RunCommonEvent(20005611, args=(14000623, 4003251, 4001251, 1400340))


@RestartOnRest
def Event14000624(_, arg_0_3: int):
    """ 14000624: Event 14000624 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(14000624)
    IfCharacterDead(0, 4000720)
    EndIfFlagDisabled(1365)
    EndIfFlagEnabled(1378)
    SetNetworkConnectedFlagRangeState((1360, 1374), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1370, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1375, 1379), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1377, state=FlagState.On)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    SetNest(arg_0_3, 4002714)
    IfCharacterHasSpecialEffect(1, arg_0_3, 159)
    SkipLinesIfConditionFalse(2, 1)
    ForceAnimation(arg_0_3, 0)


@RestartOnRest
def Event14005625(_, arg_0_3: int):
    """ 14005625: Event 14005625 """
    IfCharacterInsideRegion(0, PLAYER, region=arg_0_3)
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


def Event14005640(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 14005640: Event 14005640 """
    GotoIfPlayerNotInOwnWorld(Label.L9)
    DisableFlag(74000190)
    SkipLinesIfFlagRangeAnyEnabled(2, (1020, 1034))
    SetNetworkConnectedFlagRangeState((1020, 1034), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1020, state=FlagState.On)
    IfFlagEnabled(1, 1020)
    IfFlagEnabled(1, 14000110)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1020, 1034), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1021, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1035, 1039))
    SetNetworkConnectedFlagRangeState((1035, 1039), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1035, state=FlagState.On)
    IfFlagEnabled(2, 1038)
    IfFlagEnabled(2, 1020)
    IfCharacterAlive(2, arg_0_3)
    SkipLinesIfConditionFalse(4, 2)
    SetNetworkConnectedFlagRangeState((1035, 1039), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1035, state=FlagState.On)
    EnableFlag(74000190)
    EnableFlag(74000150)
    IfFlagEnabled(3, 1021)
    IfFlagEnabled(3, 14000110)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1035, 1039), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1038, state=FlagState.On)
    DisableFlag(74000160)
    DisableFlag(74000170)
    DisableFlag(74000053)

    # --- 9 --- #
    DefineLabel(9)
    DisableObject(arg_4_7)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    GotoIfFlagEnabled(Label.L0, 1020)
    GotoIfFlagEnabled(Label.L1, 1021)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableCharacter(arg_8_11)
    GotoIfFlagEnabled(Label.L10, 1038)
    Move(arg_0_3, destination=4004705, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L15, 74000190)
    SetTeamType(arg_0_3, TeamType.FriendlyNPC)
    ForceAnimation(arg_0_3, 20, loop=True, skip_transition=True)
    End()

    # --- 15 --- #
    DefineLabel(15)
    EnableFlag(74000170)
    SetTeamType(arg_0_3, TeamType.FriendlyNPC)
    ForceAnimation(arg_0_3, 700, loop=True, skip_transition=True)
    End()

    # --- 10 --- #
    DefineLabel(10)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    EnableObject(arg_4_7)
    End()


def Event14005660(_, arg_0_3: int):
    """ 14005660: Event 14005660 """
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(2, (1175, 1179))
    SetNetworkConnectedFlagRangeState((1175, 1179), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1175, state=FlagState.On)
    IfFlagEnabled(1, 1176)
    IfFlagEnabled(1, 70000060)
    SkipLinesIfConditionFalse(3, 1)
    SetNetworkConnectedFlagRangeState((1175, 1179), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1175, state=FlagState.On)
    EnableFlag(74000200)
    IfFlagEnabled(2, 1178)
    IfCharacterAlive(2, arg_0_3)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1175, 1179), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1176, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1160, 1174))
    SetNetworkConnectedFlagRangeState((1160, 1174), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1160, state=FlagState.On)
    DisableFlag(70000060)

    # --- 9 --- #
    DefineLabel(9)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    GotoIfFlagEnabled(Label.L0, 1160)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L2, 1178)

    # --- 1 --- #
    DefineLabel(1)
    SetTeamType(arg_0_3, TeamType.FriendlyNPC)
    Move(arg_0_3, destination=4004710, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(arg_0_3, 700, loop=True, skip_transition=True)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()


def Event14005661(_, arg_0_3: int):
    """ 14005661: Event 14005661 """
    IfStandingOnCollision(-1, 4004100)
    IfStandingOnCollision(-1, 4004101)
    IfStandingOnCollision(-1, 4004102)
    IfStandingOnCollision(-1, 4004103)
    IfStandingOnCollision(-1, 4004104)
    IfStandingOnCollision(-1, 4004109)
    IfCharacterOutsideRegion(1, PLAYER, region=4002709)
    IfConditionTrue(1, input_condition=-1)
    IfConditionFalse(2, input_condition=1)
    IfHealthNotEqual(2, arg_0_3, 0.0)
    IfFlagEnabled(2, 1160)
    IfConditionTrue(0, input_condition=2)
    DisableCharacter(arg_0_3)
    Wait(1.0)
    ClearMainCondition(0)
    IfStandingOnCollision(-1, 4004100)
    IfStandingOnCollision(-1, 4004101)
    IfStandingOnCollision(-1, 4004102)
    IfStandingOnCollision(-1, 4004103)
    IfStandingOnCollision(-1, 4004104)
    IfStandingOnCollision(-1, 4004109)
    IfCharacterOutsideRegion(1, PLAYER, region=4002709)
    IfConditionTrue(1, input_condition=-1)
    IfConditionTrue(2, input_condition=1)
    IfHealthNotEqual(2, arg_0_3, 0.0)
    IfFlagEnabled(2, 1160)
    IfConditionTrue(0, input_condition=2)
    EnableCharacter(4000710)
    ForceAnimation(4000710, 700)
    Wait(1.0)
    Restart()


def Event14005680(_, arg_0_3: int, arg_4_7: int):
    """ 14005680: Event 14005680 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1195, 1199))
    SetNetworkConnectedFlagRangeState((1195, 1199), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1195, state=FlagState.On)
    IfFlagEnabled(2, 1198)
    IfCharacterAlive(2, arg_0_3)
    SkipLinesIfConditionFalse(3, 2)
    SetNetworkConnectedFlagRangeState((1195, 1199), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1196, state=FlagState.On)
    EnableFlag(74000251)
    SkipLinesIfFlagRangeAnyEnabled(2, (1180, 1194))
    SetNetworkConnectedFlagRangeState((1180, 1194), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1180, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1195)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000061)
    SkipLinesIfFlagDisabled(1, 1195)
    DisableFlag(74000251)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1180)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L1, 1196)
    GotoIfFlagEnabled(Label.L2, 1198)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SkipLinesIfFlagDisabled(2, 74000295)
    AddSpecialEffect(arg_0_3, 12605)
    End()
    SkipLinesIfFlagDisabled(2, 74000294)
    AddSpecialEffect(arg_0_3, 12604)
    End()
    SkipLinesIfFlagDisabled(2, 74000293)
    AddSpecialEffect(arg_0_3, 12603)
    End()
    SkipLinesIfFlagDisabled(2, 74000292)
    AddSpecialEffect(arg_0_3, 12602)
    End()
    SkipLinesIfFlagDisabled(2, 74000291)
    AddSpecialEffect(arg_0_3, 12601)
    End()
    SkipLinesIfFlagDisabled(2, 74000290)
    AddSpecialEffect(arg_0_3, 12600)
    End()
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DropMandatoryTreasure(arg_0_3)
    End()


def Event14005681():
    """ 14005681: Event 14005681 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(74000280)
    IfFlagRangeAllEnabled(1, (70000100, 70000106))
    IfFlagRangeAllEnabled(1, (70000108, 70000110))
    IfFlagRangeAllEnabled(1, (70000112, 70000115))
    IfFlagEnabled(-1, 70000107)
    IfFlagEnabled(-1, 70000116)
    IfConditionTrue(1, input_condition=-1)
    IfFlagEnabled(-2, 70000111)
    IfFlagEnabled(-2, 74000603)
    IfConditionTrue(1, input_condition=-2)
    SkipLinesIfFlagDisabled(1, 6951)
    IfFlagEnabled(1, 70000120)
    SkipLinesIfFlagDisabled(1, 6952)
    IfFlagEnabled(1, 70000121)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(74000280)


def Event14005682(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 14005682: Event 14005682 """
    EndIfPlayerNotInOwnWorld()
    IfFlagDisabled(1, arg_4_7)
    IfCharacterDead(1, arg_0_3)
    IfConditionTrue(0, input_condition=1)
    SetNetworkConnectedFlagRangeState((arg_8_11, arg_12_15), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=arg_4_7, state=FlagState.On)
    SkipLinesIfFlagEnabled(2, 74000290)
    EnableFlag(74000290)
    Goto(Label.L20)
    SkipLinesIfFlagEnabled(2, 74000291)
    EnableFlag(74000291)
    Goto(Label.L20)
    SkipLinesIfFlagEnabled(2, 74000292)
    EnableFlag(74000292)
    Goto(Label.L20)
    SkipLinesIfFlagEnabled(2, 74000293)
    EnableFlag(74000293)
    Goto(Label.L20)
    SkipLinesIfFlagEnabled(2, 74000294)
    EnableFlag(74000294)
    Goto(Label.L20)
    SkipLinesIfFlagEnabled(2, 74000295)
    EnableFlag(74000295)
    Goto(Label.L20)

    # --- 20 --- #
    DefineLabel(20)
    SaveRequest()


def Event14005683(_, arg_0_3: int, arg_4_7: int):
    """ 14005683: Event 14005683 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1615, 1619))
    SetNetworkConnectedFlagRangeState((1615, 1619), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1615, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1600, 1614))
    SetNetworkConnectedFlagRangeState((1600, 1614), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1600, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1615)

    # --- 9 --- #
    DefineLabel(9)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1600)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L2, 1618)
    DisableGravity(arg_0_3)
    DisableCharacterCollision(arg_0_3)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(arg_0_3)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()


def Event14005684(_, arg_0_3: int):
    """ 14005684: Event 14005684 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(arg_0_3)
    IfFlagRangeAllEnabled(0, (13300396, 13300397))
    EnableFlag(arg_0_3)


def Event14005700(_, arg_0_3: int, arg_4_7: int):
    """ 14005700: Event 14005700 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1215, 1219))
    SetNetworkConnectedFlagRangeState((1215, 1219), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1215, state=FlagState.On)
    IfFlagEnabled(1, 1216)
    IfFlagEnabled(1, 70000062)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1215, 1219), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1215, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1200, 1214))
    SetNetworkConnectedFlagRangeState((1200, 1214), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1200, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1215)
    IfFlagEnabled(2, 1201)
    IfFlagEnabled(2, 74000303)
    SkipLinesIfConditionFalse(4, 2)
    SetNetworkConnectedFlagRangeState((1200, 1214), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1202, state=FlagState.On)
    EnableFlag(70000150)
    EnableFlag(70000153)
    IfFlagEnabled(3, 1202)
    IfFlagEnabled(3, 74000316)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1200, 1214), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1203, state=FlagState.On)
    IfFlagEnabled(4, 1203)
    IfFlagEnabled(4, 74000306)
    SkipLinesIfConditionFalse(3, 4)
    SetNetworkConnectedFlagRangeState((1200, 1214), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1204, state=FlagState.On)
    EnableFlag(70000151)
    IfFlagEnabled(5, 1204)
    IfFlagEnabled(5, 74000318)
    IfFlagDisabled(5, 1385)
    IfFlagDisabled(5, 1366)
    SkipLinesIfConditionFalse(5, 5)
    SetNetworkConnectedFlagRangeState((1200, 1214), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1205, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1215, 1219), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1218, state=FlagState.On)
    Goto(Label.L9)
    IfFlagEnabled(6, 1204)
    IfFlagEnabled(6, 74000318)
    IfFlagEnabled(-1, 1385)
    IfFlagEnabled(-1, 1366)
    IfConditionTrue(6, input_condition=-1)
    SkipLinesIfConditionFalse(2, 6)
    SetNetworkConnectedFlagRangeState((1200, 1214), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1206, state=FlagState.On)
    IfFlagEnabled(7, 1206)
    IfFlagEnabled(7, 74000309)
    SkipLinesIfConditionFalse(6, 7)
    SetNetworkConnectedFlagRangeState((1200, 1214), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1207, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1215, 1219), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1218, state=FlagState.On)
    EnableFlag(70000152)
    Goto(Label.L9)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000062)
    SkipLinesIfFlagDisabled(1, 1215)
    DisableFlag(74000320)

    # --- 10 --- #
    DefineLabel(10)
    SkipLinesIfFlagDisabled(1, 1200)
    DisableObject(4006720)
    GotoIfFlagEnabled(Label.L0, 1201)
    GotoIfFlagEnabled(Label.L0, 1203)
    GotoIfFlagEnabled(Label.L0, 1206)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=arg_4_7, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    GotoIfFlagEnabled(Label.L1, 1216)
    GotoIfFlagEnabled(Label.L2, 1218)
    DisableFlag(74000324)
    IfFlagEnabled(15, 74000301)
    IfFlagDisabled(15, 74000325)
    SkipLinesIfConditionFalse(3, 15)
    ForceAnimation(arg_0_3, 91020, loop=True, skip_transition=True)
    EnableFlag(74000324)
    End()
    ForceAnimation(arg_0_3, 90970)
    End()

    # --- 1 --- #
    DefineLabel(1)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 2 --- #
    DefineLabel(2)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()


def Event14005701():
    """ 14005701: Event 14005701 """
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(1, 1383)
    IfFlagEnabled(1, 73500105)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1380, 1394), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1384, state=FlagState.On)
    IfFlagEnabled(2, 1384)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1380, 1394), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1385, state=FlagState.On)


def Event14005720(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
    arg_32_35: int,
):
    """ 14005720: Event 14005720 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1295, 1299))
    SetNetworkConnectedFlagRangeState((1295, 1299), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1295, state=FlagState.On)
    IfFlagEnabled(1, 1296)
    IfFlagEnabled(1, 70000066)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1295, 1299), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1295, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1280, 1294))
    SetNetworkConnectedFlagRangeState((1280, 1294), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1280, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1295)
    IfFlagEnabled(2, 1281)
    IfFlagEnabled(-2, 73101710)
    IfFlagEnabled(-2, 73101720)
    IfFlagEnabled(-2, 73101730)
    IfFlagEnabled(-2, 73101740)
    IfFlagEnabled(-2, 73101750)
    IfConditionTrue(2, input_condition=-2)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1280, 1294), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1282, state=FlagState.On)
    IfFlagEnabled(3, 1282)
    IfFlagEnabled(3, 74000351)
    IfFlagEnabled(3, 73101710)
    IfFlagEnabled(3, 73101720)
    IfFlagEnabled(3, 73101730)
    IfFlagEnabled(3, 73101740)
    IfFlagEnabled(3, 73101750)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1280, 1294), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1283, state=FlagState.On)
    IfFlagEnabled(4, 1281)
    IfFlagEnabled(4, 74000380)
    IfFlagDisabled(4, 73101710)
    IfFlagDisabled(4, 73101720)
    IfFlagDisabled(4, 73101730)
    IfFlagDisabled(4, 73101740)
    IfFlagDisabled(4, 73101750)
    SkipLinesIfConditionFalse(4, 4)
    SetNetworkConnectedFlagRangeState((1280, 1294), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1286, state=FlagState.On)
    DisableFlag(70000353)
    DisableFlag(70000354)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000066)
    DisableFlag(74000352)
    DisableFlagRange((74000383, 74000392))

    # --- 10 --- #
    DefineLabel(10)
    Move(arg_0_3, destination=arg_24_27, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    Move(arg_4_7, destination=arg_28_31, destination_type=CoordEntityType.Region, copy_draw_parent=arg_4_7)
    Move(arg_8_11, destination=arg_32_35, destination_type=CoordEntityType.Region, copy_draw_parent=arg_8_11)
    GotoIfFlagEnabled(Label.L1, 1281)
    GotoIfFlagEnabled(Label.L2, 1282)
    GotoIfFlagEnabled(Label.L3, 1283)
    GotoIfFlagEnabled(Label.L4, 1284)
    GotoIfFlagEnabled(Label.L5, 1285)
    GotoIfFlagEnabled(Label.L6, 1286)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableBackread(arg_8_11)
    End()

    # --- 1 --- #
    DefineLabel(1)

    # --- 2 --- #
    DefineLabel(2)

    # --- 3 --- #
    DefineLabel(3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    DisableCharacter(arg_8_11)
    DisableBackread(arg_8_11)
    GotoIfFlagEnabled(Label.L18, 1298)
    ForceAnimation(arg_0_3, arg_12_15, loop=True, skip_transition=True)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()

    # --- 4 --- #
    DefineLabel(4)

    # --- 5 --- #
    DefineLabel(5)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_8_11)
    DisableBackread(arg_8_11)
    GotoIfFlagEnabled(Label.L18, 1298)
    SkipLinesIfFlagEnabled(2, 14000722)
    ForceAnimation(arg_4_7, arg_16_19, loop=True, skip_transition=True)
    End()
    ForceAnimation(arg_4_7, arg_12_15, loop=True, skip_transition=True)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    WaitFrames(1)
    DropMandatoryTreasure(arg_4_7)
    End()

    # --- 6 --- #
    DefineLabel(6)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableCharacter(arg_4_7)
    DisableBackread(arg_4_7)
    GotoIfFlagEnabled(Label.L18, 1298)
    ForceAnimation(arg_8_11, arg_20_23, loop=True, skip_transition=True)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_8_11)
    DisableBackread(arg_8_11)
    WaitFrames(1)
    DropMandatoryTreasure(arg_8_11)
    End()


def Event14005721():
    """ 14005721: Event 14005721 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(74000380)
    IfFlagEnabled(1, 73101610)
    IfFlagEnabled(1, 73101620)
    IfFlagEnabled(1, 73101630)
    IfFlagEnabled(1, 73101640)
    IfFlagEnabled(1, 73101650)
    IfFlagEnabled(1, 73101660)
    IfFlagEnabled(1, 73101670)
    IfFlagEnabled(1, 73101680)
    IfFlagEnabled(1, 73101690)
    IfFlagEnabled(1, 73101700)
    IfConditionTrue(0, input_condition=1)
    EnableFlag(74000380)


def Event14005722(_, arg_0_3: int, arg_4_7: int):
    """ 14005722: Event 14005722 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(14000722)
    IfFlagEnabled(0, 14000722)
    ForceAnimation(arg_0_3, arg_4_7, wait_for_completion=True)
    EnableFlag(14005722)


def Event14005723(
    _,
    arg_0_3: int,
    arg_4_7: int,
    arg_8_11: int,
    arg_12_15: int,
    arg_16_19: int,
    arg_20_23: int,
    arg_24_27: int,
    arg_28_31: int,
    arg_32_35: int,
):
    """ 14005723: Event 14005723 """
    EndIfPlayerNotInOwnWorld()
    DisableFlag(arg_4_7)
    IfFlagEnabled(1, arg_4_7)
    IfFlagEnabled(1, arg_8_11)
    IfFlagEnabled(1, arg_12_15)
    IfHealthNotEqual(1, arg_0_3, 0.0)
    IfConditionTrue(0, input_condition=1)
    DisableFlag(arg_4_7)
    SetNetworkConnectedFlagRangeState((arg_20_23, arg_24_27), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=arg_16_19, state=FlagState.On)
    EnableInvincibility(arg_0_3)
    DisableAnimations(arg_0_3)
    EnableCharacter(arg_28_31)
    EnableBackread(arg_28_31)
    ForceAnimation(arg_28_31, arg_32_35)
    SaveRequest()
    AddSpecialEffect(arg_0_3, 4640)
    Wait(5.0)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)


def Event14005725():
    """ 14005725: Event 14005725 """
    DisableNetworkSync()
    EndIfPlayerNotInOwnWorld()
    IfFlagEnabled(0, 0)
    IfCharacterInsideRegion(1, PLAYER, region=0)
    GotoIfConditionTrue(Label.L20, input_condition=1)
    RotateToFaceEntity(PLAYER, 0, animation=69070, wait_for_completion=False)
    WaitFrames(1)
    IfCharacterInsideRegion(-1, PLAYER, region=0)
    IfCharacterDoesNotHaveSpecialEffect(2, PLAYER, 150)
    IfConditionTrue(-1, input_condition=2)
    IfFlagDisabled(-2, 0)
    IfFramesElapsed(-2, 89)
    IfConditionTrue(-1, input_condition=-2)
    IfConditionTrue(0, input_condition=-1)
    SkipLinesIfFinishedConditionFalse(2, 2)
    DisableFlag(0)
    Restart()
    SkipLinesIfFinishedConditionFalse(3, -2)
    ForceAnimation(PLAYER, 0)
    DisableFlag(0)
    Restart()

    # --- 20 --- #
    DefineLabel(20)
    RotateToFaceEntity(PLAYER, 0, animation=0, wait_for_completion=True)
    WaitFrames(1)
    EnableFlag(0)
    IfFlagDisabled(-3, 0)
    IfCharacterDoesNotHaveSpecialEffect(3, PLAYER, 150)
    IfConditionTrue(-3, input_condition=3)
    IfConditionTrue(0, input_condition=-3)
    SkipLinesIfFinishedConditionFalse(3, 3)
    DisableFlag(0)
    DisableFlag(0)
    Restart()
    DisableFlag(0)
    ForceAnimation(PLAYER, 0, wait_for_completion=True)
    Restart()


def Event14005740(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 14005740: Event 14005740 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1075, 1079))
    SetNetworkConnectedFlagRangeState((1075, 1079), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1075, state=FlagState.On)
    IfFlagEnabled(1, 1076)
    IfFlagEnabled(1, 70000055)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1075, 1079), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1075, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1060, 1074))
    SetNetworkConnectedFlagRangeState((1060, 1074), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1060, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1075)
    IfFlagEnabled(2, 1060)
    IfFlagEnabled(2, 73100152)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1060, 1074), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1061, state=FlagState.On)
    IfFlagEnabled(3, 1061)
    IfPlayerRemainingYoelLevelComparison(3, comparison_type=ComparisonType.LessThanOrEqual, value=0)
    SkipLinesIfConditionFalse(4, 3)
    SetNetworkConnectedFlagRangeState((1060, 1074), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1062, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1075, 1079), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1078, state=FlagState.On)
    IfFlagEnabled(4, 1061)
    IfFlagEnabled(4, 138)
    SkipLinesIfConditionFalse(4, 4)
    SetNetworkConnectedFlagRangeState((1060, 1074), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1064, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1075, 1079), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1078, state=FlagState.On)
    IfFlagEnabled(5, 1060)
    IfFlagEnabled(5, 138)
    SkipLinesIfConditionFalse(4, 5)
    SetNetworkConnectedFlagRangeState((1060, 1074), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1063, state=FlagState.On)
    SetNetworkConnectedFlagRangeState((1075, 1079), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1078, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000055)
    DisableFlagRange((74000430, 74000433))

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1061)
    GotoIfFlagEnabled(Label.L2, 1062)
    GotoIfFlagEnabled(Label.L2, 1064)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    GotoIfFlagEnabled(Label.L1, 1078)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DropMandatoryTreasure(arg_0_3)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 2 --- #
    DefineLabel(2)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    EzstateAIRequest(arg_0_3, command_id=arg_4_7, slot=1)
    DropMandatoryTreasure(arg_0_3)
    End()


def Event14005750(_, arg_0_3: int, arg_4_7: int, arg_8_11: int):
    """ 14005750: Event 14005750 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1155, 1159))
    SetNetworkConnectedFlagRangeState((1155, 1159), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1155, state=FlagState.On)
    IfFlagEnabled(1, 1156)
    IfFlagEnabled(1, 70000059)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1155, 1159), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1155, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1140, 1154))
    SetNetworkConnectedFlagRangeState((1140, 1154), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1140, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1155)
    IfFlagEnabled(2, 1140)
    IfFlagEnabled(-2, 13000005)
    IfFlagEnabled(-2, 9301)
    IfConditionTrue(2, input_condition=-2)
    SkipLinesIfConditionFalse(2, 2)
    SetNetworkConnectedFlagRangeState((1140, 1154), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1141, state=FlagState.On)
    IfFlagEnabled(3, 1141)
    IfFlagEnabled(3, 74000850)
    SkipLinesIfConditionFalse(2, 3)
    SetNetworkConnectedFlagRangeState((1140, 1154), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1142, state=FlagState.On)
    IfFlagEnabled(4, 1142)
    IfPlayerHasGood(4, 373, including_box=False)
    IfFlagEnabled(-4, 13100002)
    IfFlagEnabled(-4, 9303)
    IfConditionTrue(4, input_condition=-4)
    SkipLinesIfConditionFalse(2, 4)
    SetNetworkConnectedFlagRangeState((1140, 1154), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1143, state=FlagState.On)
    IfFlagEnabled(5, 1143)
    IfFlagEnabled(5, 74000851)
    SkipLinesIfConditionFalse(2, 5)
    SetNetworkConnectedFlagRangeState((1140, 1154), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1144, state=FlagState.On)
    IfFlagEnabled(6, 1144)
    IfFlagEnabled(6, 13000380)
    SkipLinesIfConditionFalse(2, 6)
    SetNetworkConnectedFlagRangeState((1140, 1154), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1145, state=FlagState.On)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000059)
    SkipLinesIfFlagDisabled(1, 1155)
    DisableFlag(74000870)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1141)
    GotoIfFlagEnabled(Label.L0, 1143)
    GotoIfFlagEnabled(Label.L0, 1145)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=arg_8_11, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    GotoIfFlagEnabled(Label.L16, 1156)
    GotoIfFlagEnabled(Label.L18, 1158)
    ForceAnimation(arg_0_3, arg_4_7, loop=True, skip_transition=True)
    End()

    # --- 16 --- #
    DefineLabel(16)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 18 --- #
    DefineLabel(18)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()


def Event14005760(_, arg_0_3: int, arg_4_7: int):
    """ 14005760: Event 14005760 """
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(2, (1255, 1259))
    SetNetworkConnectedFlagRangeState((1255, 1259), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1255, state=FlagState.On)
    IfFlagEnabled(1, 1256)
    IfFlagEnabled(1, 70000064)
    SkipLinesIfConditionFalse(3, 1)
    SetNetworkConnectedFlagRangeState((1255, 1259), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1255, state=FlagState.On)
    DisableFlag(74000460)
    SkipLinesIfFlagRangeAnyEnabled(2, (1240, 1254))
    SetNetworkConnectedFlagRangeState((1240, 1254), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1240, state=FlagState.On)
    DisableFlag(70000064)

    # --- 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, 1241)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableObject(arg_4_7)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=4004735, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    GotoIfFlagEnabled(Label.L10, 1256)
    GotoIfFlagEnabled(Label.L11, 1258)
    ForceAnimation(arg_0_3, 90450)
    End()

    # --- 10 --- #
    DefineLabel(10)
    SetTeamType(arg_0_3, TeamType.HostileNPC)
    End()

    # --- 11 --- #
    DefineLabel(11)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()


def Event14005780(_, arg_0_3: int, arg_4_7: int, arg_8_11: int, arg_12_15: int):
    """ 14005780: Event 14005780 """
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1275, 1279))
    SetNetworkConnectedFlagRangeState((1275, 1279), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1275, state=FlagState.On)
    IfFlagEnabled(1, 1276)
    IfFlagEnabled(1, 70000065)
    SkipLinesIfConditionFalse(2, 1)
    SetNetworkConnectedFlagRangeState((1275, 1279), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1275, state=FlagState.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1260, 1274))
    SetNetworkConnectedFlagRangeState((1260, 1274), state=RangeState.AllOn)
    SetNetworkConnectedFlagState(flag=1260, state=FlagState.On)
    GotoIfFlagDisabled(Label.L9, 1275)

    # --- 9 --- #
    DefineLabel(9)
    DisableFlag(70000065)

    # --- 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, 1261)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    DisableObject(arg_8_11)
    End()

    # --- 0 --- #
    DefineLabel(0)
    Move(arg_0_3, destination=arg_12_15, destination_type=CoordEntityType.Region, copy_draw_parent=arg_0_3)
    GotoIfFlagEnabled(Label.L1, 1278)
    ForceAnimation(arg_0_3, arg_4_7)
    End()

    # --- 1 --- #
    DefineLabel(1)
    DisableCharacter(arg_0_3)
    DisableBackread(arg_0_3)
    WaitFrames(1)
    DropMandatoryTreasure(arg_0_3)
    End()


@RestartOnRest
def Event14005781():
    """ 14005781: Event 14005781 """
    EndIfPlayerNotInOwnWorld()
    EndIfFlagEnabled(74000531)
    IfFlagEnabled(-1, 73901140)
    IfFlagEnabled(-1, 73901150)
    IfFlagEnabled(-1, 73901160)
    IfFlagEnabled(-1, 73901170)
    IfFlagEnabled(-1, 73901180)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(74000531)


@RestartOnRest
def Event14005782():
    """ 14005782: Event 14005782 """
    EndIfPlayerNotInOwnWorld()
    IfFlagChange(-1, 73901140)
    IfFlagChange(-1, 73901150)
    IfFlagChange(-1, 73901160)
    IfFlagChange(-1, 73901170)
    IfFlagChange(-1, 73901180)
    IfConditionTrue(0, input_condition=-1)
    EnableFlag(74000532)
    Restart()


def Event14005900():
    """ 14005900: Event 14005900 """
    DisableNetworkSync()
    EndIfCharacterOutsideRegion(PLAYER, 4002901)
    Move(PLAYER, destination=4002900, destination_type=CoordEntityType.Region, copy_draw_parent=PLAYER)
