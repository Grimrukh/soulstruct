"""
Firelink Shrine / Cemetery of Ash

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
# [COMMON_FUNC]
from .common_func import *
from soulstruct.darksouls3.events import *
from soulstruct.darksouls3.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=14000000, obj=4001950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14000001, obj=4001951, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14000003, obj=4001953, reaction_distance=5.0)
    CommonFunc_20005500(0, flag=14000800, bonfire_flag=14000002, character=4000952, obj=4001952)
    CommonFunc_20005500(0, flag=14000830, bonfire_flag=14000004, character=4000954, obj=4001954)
    Event_14005480(0, flag=74000012)
    Event_14005481()
    Event_14005101()
    Event_14005110()
    Event_14000130()
    Event_14005102()
    Event_14000120(0, flag=9210, flag_1=9211, flag_2=9212, flag_3=9213, flag_4=9214, flag_5=9215)
    Event_14000121(0, flag=9211, item=2126, obj=4001111, target_entity=4001121, action_button_id=9353, animation=69050)
    Event_14000121(2, flag=9212, item=2124, obj=4001112, target_entity=4001122, action_button_id=9353, animation=69040)
    Event_14000121(4, flag=9213, item=2123, obj=4001113, target_entity=4001123, action_button_id=9353, animation=69040)
    Event_14000121(6, flag=9214, item=2125, obj=4001114, target_entity=4001124, action_button_id=9353, animation=69050)
    CommonFunc_20005120(0, character=4000202, radius=8.5)
    CommonFunc_20005210(0, character=4000204, animation_id=703, animation_id_1=1703, radius=8.5)
    CommonFunc_20005132(0, character=4000205, radius=10.0, region=4002205)
    CommonFunc_20005132(0, character=4000207, radius=1.0, region=4002207)
    CommonFunc_20005130(0, character=4000209, radius=16.0, region=4002207)
    CommonFunc_20005213(0, character=4000210, animation_id=705, animation_id_1=1705, radius=2.5, region=4002210)
    CommonFunc_20005110(0, character=4000211, region=4002248)
    CommonFunc_20005210(0, character=4000212, animation_id=703, animation_id_1=1703, radius=4.0)
    CommonFunc_20005200(0, character=4000213, animation_id=705, animation_id_1=1705, region=4002213)
    CommonFunc_20005210(0, character=4000214, animation_id=703, animation_id_1=1703, radius=3.0)
    CommonFunc_20005150(0, character=4000215)
    CommonFunc_20005200(0, character=4000216, animation_id=703, animation_id_1=1703, region=4002216)
    CommonFunc_20005200(0, character=4000217, animation_id=703, animation_id_1=1703, region=4002216)
    CommonFunc_20005200(0, character=4000218, animation_id=706, animation_id_1=1706, region=4002218)
    CommonFunc_20005200(0, character=4000219, animation_id=706, animation_id_1=1706, region=4002216)
    CommonFunc_20005201(0, character=4000220, animation_id=703, animation_id_1=1703, region=4002220, seconds=1.0)
    CommonFunc_20005201(0, character=4000221, animation_id=706, animation_id_1=1706, region=4002220, seconds=1.5)
    CommonFunc_20005210(0, character=4000239, animation_id=703, animation_id_1=1703, radius=4.0)
    CommonFunc_20005120(0, character=4000240, radius=15.0)
    CommonFunc_20005220(0, character=4000241, animation_id=706, animation_id_1=1706)
    CommonFunc_20005290(0, character=4000242, animation_id=705, animation_id_1=1705)
    CommonFunc_20005220(0, character=4000243, animation_id=703, animation_id_1=1703)
    CommonFunc_20005110(0, character=4000244, region=4002244)
    CommonFunc_20005292(0, character=4000245, animation_id=703, animation_id_1=1703)
    CommonFunc_20005290(0, character=4000246, animation_id=703, animation_id_1=1703)
    CommonFunc_20005110(0, character=4000247, region=4002248)
    CommonFunc_20005220(0, character=4000251, animation_id=703, animation_id_1=1703)
    CommonFunc_20005210(0, character=4000252, animation_id=705, animation_id_1=1705, radius=2.0)
    CommonFunc_20005210(0, character=4000253, animation_id=703, animation_id_1=1703, radius=13.0)
    CommonFunc_20005211(0, character=4000255, animation_id=703, animation_id_1=1703, radius=5.0, seconds=1.0)
    CommonFunc_20005213(0, character=4000256, animation_id=705, animation_id_1=1705, radius=2.5, region=4002210)
    CommonFunc_20005211(0, character=4000260, animation_id=703, animation_id_1=1703, radius=5.0, seconds=1.5)
    CommonFunc_20005200(0, character=4000261, animation_id=703, animation_id_1=1703, region=4002261)
    CommonFunc_20005200(0, character=4000262, animation_id=703, animation_id_1=1703, region=4002261)
    CommonFunc_20005200(0, character=4000263, animation_id=703, animation_id_1=1703, region=4002261)
    CommonFunc_20005140(0, character=4000265, region=4002207, character_1=4000254)
    CommonFunc_20005223(0, character=4000280, animation_id=703, animation_id_1=1703, seconds=1.0)
    CommonFunc_20005210(0, character=4000281, animation_id=703, animation_id_1=1703, radius=22.0)
    CommonFunc_20005210(0, character=4000282, animation_id=705, animation_id_1=1705, radius=12.0)
    CommonFunc_20005213(0, character=4000284, animation_id=705, animation_id_1=1705, radius=2.5, region=4002284)
    CommonFunc_20005220(0, character=4000285, animation_id=703, animation_id_1=1703)
    CommonFunc_20005223(0, character=4000287, animation_id=703, animation_id_1=1703, seconds=1.0)
    CommonFunc_20005201(0, character=4000288, animation_id=703, animation_id_1=1703, region=4002207, seconds=4.0)
    CommonFunc_20005120(0, character=4000289, radius=3.0)
    CommonFunc_20005415(
        0,
        14000290,
        4000250,
        4000290,
        703,
        1703,
        4002290,
        14004290,
        14005290,
        event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    )
    CommonFunc_20005416(0, 14000290, 4000250, 4000290, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    CommonFunc_20005120(0, 4000301, 32.0, event_layers=[1])
    CommonFunc_20005132(0, 4000303, 1.0, 4002303, event_layers=[1])
    CommonFunc_20005110(0, 4000320, 4002320, event_layers=[1])
    CommonFunc_20005110(0, 4000330, 4002330, event_layers=[1])
    CommonFunc_20005110(0, 4000331, 4002330, event_layers=[1])
    Event_14005300(0, character=4000330, region=4002360)
    CommonFunc_20005240(0, 4000341, 702, 1702, 12140, event_layers=[1])
    CommonFunc_20005240(0, 4000342, 702, 1702, 12140, event_layers=[1])
    CommonFunc_20005240(0, 4000343, 701, 1701, 12140, event_layers=[1])
    CommonFunc_20005120(0, 4000346, 6.5, event_layers=[1])
    CommonFunc_20005240(0, 4000349, 700, 1700, 12140, event_layers=[1])
    CommonFunc_20005240(0, 4000350, 700, 1700, 12140, event_layers=[1])
    CommonFunc_20005240(0, 4000351, 700, 1700, 12140, event_layers=[1])
    CommonFunc_20005223(0, 4000352, 700, 1700, 2.0, event_layers=[1])
    CommonFunc_20005210(0, 4000355, 700, 1700, 6.0, event_layers=[1])
    CommonFunc_20005240(0, 4000356, 700, 1700, 12140, event_layers=[1])
    CommonFunc_20005240(0, 4000357, 700, 1700, 12140, event_layers=[1])
    CommonFunc_20005211(0, 4000360, 701, 1701, 5.0, 0.0, event_layers=[1])
    CommonFunc_20005211(0, 4000361, 701, 1701, 5.0, 0.0, event_layers=[1])
    CommonFunc_20005211(0, 4000362, 701, 1701, 5.0, 0.0, event_layers=[1])
    CommonFunc_20005211(0, 4000363, 701, 1701, 5.0, 0.0, event_layers=[1])
    CommonFunc_20005211(0, 4000364, 701, 1701, 5.0, 0.0, event_layers=[1])
    CommonFunc_20005211(0, 4000365, 701, 1701, 5.0, 0.0, event_layers=[1])
    CommonFunc_20005341(0, flag=14000380, character=4000380, item_lot_param_id=31002000)
    CommonFunc_20005341(0, flag=14000381, character=4000381, item_lot_param_id=31004000)
    CommonFunc_20005341(0, flag=14000382, character=4000382, item_lot_param_id=31004000)
    CommonFunc_20005341(0, flag=14000390, character=4000390, item_lot_param_id=21509500)
    CommonFunc_20005342(0, flag=9500, character=4000500)
    CommonFunc_20005620(0, flag=14000400, flag_1=14001400, entity=4001400, obj=4001401, obj_1=4001402, flag_2=14001401)
    Event_14005401()
    Event_14005420()
    CommonFunc_20005640(0, flag=14000426, obj=4001426, start_climbing_flag=14005426, stop_climbing_flag=14005427)
    Event_14005460()
    Event_14005461()
    Event_14005450()
    Event_1405451(event_layers=[1])
    DisableObject(4001801)
    Event_14005470(event_layers=[1])
    Event_14005471(event_layers=[1])
    Event_14005472(event_layers=[1])
    Event_14005473(event_layers=[1])
    Event_14005474(event_layers=[1])
    Event_14005445()
    CommonFunc_20005610(0, flag=14000410, region=4002410, region_1=4002411)
    CommonFunc_20005611(0, flag=14000410, obj_act_id=4003252, obj=4001252, obj_act_id_1=1400340)
    CommonFunc_20005613(0, flag=14000425, obj_act_id=4003250, obj=4001250, obj_act_id_1=3400340, text=10010873)
    Event_14005442(event_layers=[1])
    Event_14005440(event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    Event_14005441()
    CommonFunc_20005650(0, flag=14000430, obj=4001430)
    CommonFunc_20005650(0, flag=14000431, obj=4001431)
    CommonFunc_20005650(0, flag=14000432, obj=4001432)
    CommonFunc_20005650(0, flag=14000433, obj=4001433)
    CommonFunc_20005650(0, flag=14000434, obj=4001434)
    CommonFunc_20005650(0, flag=14000435, obj=4001435)
    CommonFunc_20005520(0, flag=14000600, obj=4001600, obj_act_id=4004600)
    CommonFunc_20005520(0, flag=14000601, obj=4001601, obj_act_id=4004601)
    CommonFunc_20005523(0, obj=4001210, completion_count=2)
    CommonFunc_20005523(0, obj=4001211, completion_count=1)
    CommonFunc_20005523(0, obj=4001212, completion_count=1)
    CommonFunc_20005523(0, obj=4001213, completion_count=2)
    CommonFunc_20005524(0, obj=4001218, flag=9512)
    CommonFunc_20005525(0, 54000300, 4000300, 4001728, 62, event_layers=[1])
    CommonFunc_20005526(0, 54000330, 4000330, 4001221, 62, 13300800, event_layers=[1])
    CommonFunc_20005525(0, 54000340, 4000340, 4001222, 62, event_layers=[1])
    Event_14005484(1, text=10012051, anchor_entity=4001141)
    Event_14005484(2, text=10012052, anchor_entity=4001142)
    Event_14005484(3, text=10012053, anchor_entity=4001143)
    Event_14005484(4, text=10012054, anchor_entity=4001144)
    Event_14005484(5, text=10012055, anchor_entity=4001145)
    Event_14005800()
    Event_14005810()
    Event_14005811()
    Event_14005812()
    Event_14000816()
    Event_14005813()
    Event_14005820()
    Event_14005830(event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    Event_14005840(event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    Event_14005841(event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    Event_14000842(event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    Event_14000859(event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    CommonFunc_20005840(0, 4001800, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    CommonFunc_20005841(0, 4001800, event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    CommonFunc_20005701(0, 14000830, 14004190, 14005190, 4000190, 4002190, 9500, event_layers=[1, 3, 4, 5, 6, 7, 8, 9])
    CommonFunc_20005711(
        0,
        14004190,
        14005835,
        4000190,
        4002800,
        4002805,
        14000831,
        event_layers=[1, 3, 4, 5, 6, 7, 8, 9],
    )
    CommonFunc_20005720(0, 14004190, 14005190, 14000830, 4000190, event_layers=[1, 3, 4, 5, 6, 7, 8, 9])
    CommonFunc_20005714(0, 14004190, 14005835, 4000190, 4002806, 14000831, event_layers=[1, 3, 4, 5, 6, 7, 8, 9])
    CommonFunc_20005750(
        0,
        14000830,
        14000197,
        14004197,
        14005197,
        4000197,
        4002197,
        4002198,
        0.0,
        0,
        event_layers=[1, 3, 4, 5, 6, 7, 8, 9],
    )
    CommonFunc_20005721(0, 14004197, 14005197, 14000197, 4000197, event_layers=[1, 3, 4, 5, 6, 7, 8, 9])
    CommonFunc_20005760(0, 14000197, 14004197, 14005197, 4000197, event_layers=[1, 3, 4, 5, 6, 7, 8, 9])
    Event_14005619()
    CommonFunc_20006002(0, character=4000700, flag=1018, first_flag=1015, last_flag=1019)
    Event_14005602(0, character=4000700, item_lot_param_id=60200)
    Event_14000603(0, flag=14000410, flag_1=74000132)
    Event_14005604(0, character=4000700, region=4002702)
    Event_14005605(0, character=4000700, special_effect=12500, animation_id=20005)
    Event_14005605(1, character=4000700, special_effect=12501, animation_id=20006)
    Event_14005605(2, character=4000700, special_effect=12502, animation_id=20007)
    Event_14005605(3, character=4000700, special_effect=12503, animation_id=20008)
    Event_14005615(0, character=4000700)
    Event_14005616(0, character=4000700)
    CommonFunc_20006005(
        0,
        target_entity=4000700,
        flag=74000135,
        flag_1=74000137,
        region=0,
        radius=1.2000000476837158,
        animation=90250,
        animation_id=90260,
        special_effect=155,
    )
    CommonFunc_20006006(
        0,
        character=4000700,
        flag=74000136,
        flag_1=74000138,
        animation__animation_id=20000,
        animation_id=20001,
        left=1,
        seconds=0.0,
    )
    CommonFunc_20006040(0, character=4000700, destination=4002703, special_effect=153)
    CommonFunc_20006040(0, character=4000700, destination=4002700, special_effect=151)
    CommonFunc_20006002(0, character=4000705, flag=1038, first_flag=1035, last_flag=1039)
    CommonFunc_20006002(0, character=4000710, flag=1178, first_flag=1175, last_flag=1179)
    Event_14005661(0, character=4000710)
    Event_14005682(0, character=4000715, flag=1198, first_flag=1195, last_flag=1199)
    Event_14005681()
    Event_14005684(0, flag=70000119)
    CommonFunc_20006020(0, flag=70000125, flag_1=70000102)
    CommonFunc_20006020(0, flag=70000126, flag_1=70000106)
    CommonFunc_20006020(0, flag=70000127, flag_1=70000104)
    CommonFunc_20006020(0, flag=70000128, flag_1=70000175)
    CommonFunc_20006020(0, flag=70000129, flag_1=70000110)
    CommonFunc_20006020(0, flag=70000130, flag_1=70000115)
    CommonFunc_20006020(0, flag=70000131, flag_1=70000103)
    CommonFunc_20006020(0, flag=70000107, flag_1=70000116)
    CommonFunc_20006020(0, flag=70000132, flag_1=70000108)
    CommonFunc_20006020(0, flag=70000133, flag_1=70000115)
    CommonFunc_20006002(0, character=4000716, flag=1618, first_flag=1615, last_flag=1619)
    CommonFunc_20006002(0, character=4000720, flag=1218, first_flag=1215, last_flag=1219)
    CommonFunc_20006000(
        0,
        character=4000720,
        flag=1216,
        flag_1=1217,
        flag_2=74000330,
        value=0.6499999761581421,
        first_flag=1215,
        last_flag=1219,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=4000720, flag=1216, flag_1=1217, flag_2=74000330, right=3)
    CommonFunc_20006020(0, flag=70000153, flag_1=70000152)
    CommonFunc_20006002(0, character=4000725, flag=1298, first_flag=1295, last_flag=1299)
    CommonFunc_20006002(0, character=4000726, flag=1298, first_flag=1295, last_flag=1299)
    CommonFunc_20006002(0, character=4000727, flag=1298, first_flag=1295, last_flag=1299)
    Event_14005721()
    CommonFunc_20006005(0, 4000725, 74000383, 74000384, 0, 1.0, 90280, 90291, -1)
    Event_14005722(0, entity=4000726, animation_id=90641)
    CommonFunc_20006005(0, 4000726, 74000386, 74000387, 0, 1.0, 90280, 90291, -1)
    Event_14005723(
        0,
        character=4000726,
        flag=74000381,
        flag_1=1295,
        flag_2=1284,
        flag_3=1282,
        first_flag=1280,
        last_flag=1294,
        character_1=4000725,
        animation_id=90550,
    )
    Event_14005723(
        1,
        character=4000726,
        flag=74000382,
        flag_1=1295,
        flag_2=1285,
        flag_3=1283,
        first_flag=1280,
        last_flag=1294,
        character_1=4000725,
        animation_id=90550,
    )
    CommonFunc_20006030(
        0,
        obj=4001727,
        action_button_id=4000,
        right=2,
        item_lot_param_id=61610,
        first_flag=50006162,
        last_flag=50006163,
        flag=1286,
    )
    CommonFunc_20006031(0, flag=74000393, region=4002727)
    CommonFunc_20006005(
        0,
        target_entity=4000727,
        flag=74000389,
        flag_1=74000391,
        region=4002728,
        radius=0.0,
        animation=90250,
        animation_id=90260,
        special_effect=155,
    )
    CommonFunc_20006006(
        0,
        character=4000727,
        flag=74000390,
        flag_1=74000392,
        animation__animation_id=90610,
        animation_id=90620,
        left=0,
        seconds=0.0,
    )
    CommonFunc_20006002(0, character=4000730, flag=1078, first_flag=1075, last_flag=1079)
    CommonFunc_20006005(
        0,
        target_entity=4000730,
        flag=74000430,
        flag_1=74000432,
        region=0,
        radius=2.299999952316284,
        animation=90250,
        animation_id=90260,
        special_effect=155,
    )
    CommonFunc_20006006(
        0,
        character=4000730,
        flag=74000431,
        flag_1=74000433,
        animation__animation_id=20001,
        animation_id=20002,
        left=1,
        seconds=0.699999988079071,
    )
    CommonFunc_20006002(0, character=4000735, flag=1258, first_flag=1255, last_flag=1259)
    CommonFunc_20006000(
        0,
        character=4000735,
        flag=1256,
        flag_1=1257,
        flag_2=74000470,
        value=0.6499999761581421,
        first_flag=1255,
        last_flag=1259,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=4000735, flag=1256, flag_1=1257, flag_2=74000470, right=3)
    CommonFunc_20006002(0, character=4000740, flag=1278, first_flag=1275, last_flag=1279)
    Event_14005781()
    Event_14005782()
    CommonFunc_20006002(0, character=4000745, flag=1238, first_flag=1235, last_flag=1239)
    CommonFunc_20006000(
        0,
        character=4000745,
        flag=1236,
        flag_1=1237,
        flag_2=74000580,
        value=0.6499999761581421,
        first_flag=1235,
        last_flag=1239,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=4000745, flag=1236, flag_1=1237, flag_2=74000580, right=3)
    Event_14005501(0, flag=74000582, flag_1=74000584, bit_count=3, bit_count_1=3, max_value__value=3)
    Event_14005503(0, flag=74000583)
    CommonFunc_20006002(0, character=4000750, flag=1058, first_flag=1055, last_flag=1059)
    Event_14005521(
        0,
        character=4000750,
        flag=1056,
        flag_1=1057,
        flag_2=74000630,
        value=0.6499999761581421,
        first_flag=1055,
        last_flag=1059,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=4000750, flag=1056, flag_1=1057, flag_2=74000630, right=3)
    Event_14000522()
    CommonFunc_20006030(
        0,
        obj=4001750,
        action_button_id=4000,
        right=3,
        item_lot_param_id=60410,
        first_flag=50006041,
        last_flag=50006042,
        flag=1045,
    )
    CommonFunc_20006002(0, character=4000755, flag=1318, first_flag=1315, last_flag=1319)
    CommonFunc_20006000(
        0,
        character=4000755,
        flag=1316,
        flag_1=1317,
        flag_2=74000680,
        value=0.6499999761581421,
        first_flag=1315,
        last_flag=1319,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=4000755, flag=1316, flag_1=1317, flag_2=74000680, right=3)
    CommonFunc_20006002(0, character=4000756, flag=1318, first_flag=1315, last_flag=1319)
    Event_14005541(
        0,
        character=4000755,
        flag=1316,
        flag_1=1317,
        first_flag=1281,
        last_flag=1284,
        flag_2=1298,
        first_flag_1=1315,
        last_flag_1=1319,
        flag_3=1302,
    )
    Event_14005542(
        0,
        character=4000755,
        character_1=4000756,
        character_2=4000725,
        character_3=4000726,
        animation_id=90640,
    )
    Event_14005543(0, character=4000756)
    Event_14000490()
    Event_14000491()
    Event_14005581(
        0,
        character=4000765,
        character_1=4000770,
        character_2=4000775,
        flag=74000730,
        flag_1=74000731,
        value=0.6499999761581421,
    )
    Event_14000583(
        0,
        character=4000765,
        character_1=4000770,
        flag=1356,
        flag_1=1357,
        character_2=4000775,
        first_flag=1355,
        last_flag=1359,
        flag_2=1342,
    )
    Event_14005584(0, character=4000765, character_1=4000770, flag=1357, flag_1=1342)
    CommonFunc_20006001(0, attacked_entity=4000765, flag=1356, flag_1=1357, flag_2=74000730, right=3)
    CommonFunc_20006002(0, character=4000765, flag=1358, first_flag=1355, last_flag=1359)
    Event_14005587(0, character=4000765, flag=1342, flag_1=1357)
    CommonFunc_20006001(0, attacked_entity=4000770, flag=1356, flag_1=1357, flag_2=74000730, right=3)
    CommonFunc_20006002(0, character=4000770, flag=1358, first_flag=1355, last_flag=1359)
    Event_14005587(1, character=4000770, flag=1342, flag_1=1357)
    CommonFunc_20006001(0, attacked_entity=4000775, flag=1496, flag_1=1497, flag_2=74000731, right=3)
    CommonFunc_20006002(0, character=4000775, flag=1498, first_flag=1495, last_flag=1499)
    Event_14000585(
        0,
        character=4000775,
        flag=1496,
        flag_1=1497,
        character_1=4000765,
        character_2=4000770,
        first_flag=1495,
        last_flag=1499,
        flag_2=1482,
    )
    CommonFunc_20006002(0, character=4000760, flag=1118, first_flag=1115, last_flag=1119)
    CommonFunc_20006000(
        0,
        character=4000760,
        flag=1116,
        flag_1=1117,
        flag_2=74000830,
        value=0.6499999761581421,
        first_flag=1115,
        last_flag=1119,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=4000760, flag=1116, flag_1=1117, flag_2=74000830, right=3)
    CommonFunc_20006030(
        0,
        obj=4001760,
        action_button_id=4000,
        right=2,
        item_lot_param_id=60730,
        first_flag=50006074,
        last_flag=50006074,
        flag=74000825,
    )
    CommonFunc_20006002(0, character=4000761, flag=1118, first_flag=1115, last_flag=1119)
    CommonFunc_20006000(
        0,
        character=4000761,
        flag=1116,
        flag_1=1117,
        flag_2=74000831,
        value=0.6499999761581421,
        first_flag=1115,
        last_flag=1119,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=4000761, flag=1116, flag_1=1117, flag_2=74000831, right=3)
    CommonFunc_20006002(0, character=4000780, flag=1138, first_flag=1135, last_flag=1139)
    CommonFunc_20006030(
        0,
        obj=4001780,
        action_button_id=4000,
        right=1,
        item_lot_param_id=60810,
        first_flag=50006081,
        last_flag=50006081,
        flag=74000790,
    )
    CommonFunc_20006002(0, character=4000785, flag=1158, first_flag=1155, last_flag=1159)
    CommonFunc_20006000(
        0,
        character=4000785,
        flag=1156,
        flag_1=1157,
        flag_2=74000880,
        value=0.6499999761581421,
        first_flag=1155,
        last_flag=1159,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=4000785, flag=1156, flag_1=1157, flag_2=74000880, right=3)
    CommonFunc_20006002(0, character=4000791, flag=1378, first_flag=1375, last_flag=1379)
    CommonFunc_20006000(
        0,
        character=4000791,
        flag=1376,
        flag_1=1377,
        flag_2=73500290,
        value=0.6499999761581421,
        first_flag=1375,
        last_flag=1379,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=4000791, flag=1376, flag_1=1377, flag_2=73500290, right=3)
    CommonFunc_20006032(0, character=4000791, obj=4001790)
    Event_14000621(0, character=4000790)
    Event_14000622(0, character=4000790, character_1=4000791, destination=4004791)
    Event_14000624(0, 4000791)


@NeverRestart(50)
def Preconstructor():
    """Event 50"""
    Event_14005103(event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005104(event_layers=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    Event_14005618(event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005600(0, 4000700, 4002701, 4002703, 4002700, 4002702, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005640(0, 4000705, 4001115, 4000706, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005660(0, 4000710, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005680(0, 4000715, 4002715, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005683(0, character=4000716, destination=4002715)
    Event_14005720(
        0,
        4000725,
        4000726,
        4000727,
        90550,
        90640,
        90730,
        4004725,
        4004726,
        4004727,
        event_layers=[0, 3, 4, 5, 6, 7, 8, 9],
    )
    Event_14005740(0, 4000730, 2160, 4004730, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005760(0, 4000735, 4006735, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005780(0, 4000740, 90460, 4001740, 4004740, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005500(0, 4000745, 90420, 4001745, 4004745, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005520(0, character=4000750, animation_id=90300, destination=4004750, obj=4001751)
    Event_14005540(0, 4000755, 4000756, 90660, 4004755, 4004756, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005560(0, 4000760, 4000761, 4004760, 4004761, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005580(0, 4000765, 4000770, 90750, 90800, 4004765, 4004770, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005586(0, 4000775, 90900, 4004775, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005570(0, 4000780, 4000781, 4004780, 4004781, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005750(0, 4000785, 90710, 4004785, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005620(0, 4000790, 4000791, 4004791, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005701(event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14005700(0, 4000720, 4004720, event_layers=[0, 3, 4, 5, 6, 7, 8, 9])
    Event_14000401()
    Event_14000100(event_layers=[0, 2, 3, 4, 5, 6, 7, 8, 9])
    DisableSoundEvent(sound_id=4004800)
    DisableSoundEvent(sound_id=4004801)
    DisableSoundEvent(sound_id=4004830)
    DisableSoundEvent(sound_id=4004831)
    DisableSoundEvent(sound_id=4004450)
    DisableSoundEvent(sound_id=4004460)
    DisableSoundEvent(sound_id=4003700)
    DisableSoundEvent(sound_id=4003701)


@NeverRestart(14000100)
def Event_14000100():
    """Event 14000100"""
    if ThisEventSlotFlagEnabled():
        return
    if PlayerNotInOwnWorld():
        return
    if OutsideMap(game_map=FIRELINK_SHRINE):
        return
    AND_1.Add(MapInCeremony(game_map=FIRELINK_SHRINE, ceremony_id=0))
    if not AND_1:
        return
    AddSpecialEffect(PLAYER, 4610)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    DisableObject(4006440)
    PlayCutsceneAndMoveSpecificPlayer_WithUnknowns(
        cutscene_id=40000040,
        cutscene_flags=0,
        move_to_region=4002110,
        game_map=FIRELINK_SHRINE,
        player_id=10000,
        unknown1=1,
        unknown2=0,
    )
    WaitFrames(frames=1)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    EnableObject(4006440)
    
    MAIN.Await(OngoingCutsceneFinished(cutscene_id=40000040))
    
    SetNetworkInteractionState(state=True)
    WaitFrames(frames=1)
    RemoveSpecialEffect(PLAYER, 4610)
    SetRespawnPoint(respawn_point=4002959)
    SaveRequest()
    EnableFlag(14000100)


@NeverRestart(14005101)
def Event_14005101():
    """Event 14005101"""
    if FlagEnabled(14000101):
        return
    
    MAIN.Await(ObjectBackreadEnabled(obj=4001950))
    
    WaitFrames(frames=1)
    ForceAnimation(4001950, 100000, loop=True, unknown2=1.0)
    EnableFlag(74000010)
    AND_1.Add(ObjectBackreadDisabled(obj=4001950))
    OR_1.Add(AND_1)
    OR_1.Add(ActionButtonParamActivated(action_button_id=9351, entity=4001950))
    
    MAIN.Await(OR_1)
    
    RestartIfFinishedConditionTrue(input_condition=AND_1)
    Move(PLAYER, destination=4001950, destination_type=CoordEntityType.Object, model_point=1, short_move=True)
    ForceAnimation(4001950, 60430, unknown2=1.0)
    EnableBonfireWarping(bonfire_obj=4001950, animation=60430)
    DisableFlag(74000010)
    EnableFlag(14000101)
    RemoveGoodFromPlayer(item=2137, quantity=1)


@NeverRestart(14005102)
def Event_14005102():
    """Event 14005102"""
    if PlayerNotInOwnWorld():
        return
    DisableObject(4001101)
    DisableObject(4001102)
    AND_1.Add(PlayerStandingOnCollision(4004100))
    AND_10.Add(FlagDisabled(131))
    AND_10.Add(FlagEnabled(2051))
    OR_10.Add(AND_1)
    OR_10.Add(AND_10)
    
    MAIN.Await(OR_10)
    
    DeleteObjectVFX(4001101)
    DeleteObjectVFX(4001102)
    EnableObject(4001101)
    EnableObject(4001102)
    CreateObjectVFX(4001101, vfx_id=101, model_point=840080)
    CreateObjectVFX(4001102, vfx_id=101, model_point=4)
    AND_1.Add(FlagDisabled(2051))
    AND_1.Add(LeavingSession())
    SkipLinesIfFinishedConditionTrue(1, input_condition=AND_10)
    AND_1.Add(PlayerStandingOnCollision(4004101))
    
    MAIN.Await(AND_1)
    
    OR_9.Add(FlagDisabled(131))
    OR_9.Add(MapInCeremony(game_map=FIRELINK_SHRINE, ceremony_id=10))
    SkipLinesIfConditionFalse(2, OR_9)
    AND_2.Add(TimeElapsed(seconds=18.0))
    SkipLines(1)
    AND_2.Add(TimeElapsed(seconds=20.0))
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_10)
    AND_3.Add(PlayerStandingOnCollision(4004100))
    SkipLines(1)
    AND_3.Add(FlagEnabled(2051))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    RestartIfFinishedConditionTrue(input_condition=AND_3)
    DeleteObjectVFX(4001101)
    DeleteObjectVFX(4001102)
    AND_4.Add(TimeElapsed(seconds=2.0))
    SkipLinesIfFinishedConditionTrue(2, input_condition=AND_10)
    AND_5.Add(PlayerStandingOnCollision(4004100))
    SkipLines(1)
    AND_5.Add(FlagEnabled(2051))
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    RestartIfFinishedConditionTrue(input_condition=AND_5)
    DisableObject(4001101)
    DisableObject(4001102)
    Restart()


@NeverRestart(14005103)
def Event_14005103():
    """Event 14005103"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(131))
    
    MAIN.Await(AND_1)
    
    EnableMapCollision(collision=4004109)
    DisableMapCollision(collision=4004100)


@NeverRestart(14005104)
def Event_14005104():
    """Event 14005104"""
    EnableMapCollision(collision=4004109)
    DisableMapCollision(collision=4004100)


@NeverRestart(14005110)
def Event_14005110():
    """Event 14005110"""
    SetCollisionResState(collision=4004100, state=False)
    if FlagEnabled(14000110):
        return
    if PlayerNotInOwnWorld():
        return
    DisableFlag(74000010)
    OR_1.Add(FlagEnabled(9210))
    OR_1.Add(FlagEnabled(74000123))
    AND_1.Add(OR_1)
    AND_1.Add(HealthRatio(4000700) != 0.0)
    
    MAIN.Await(AND_1)
    
    SetCollisionResState(collision=4004100, state=True)
    GotoIfFlagEnabled(Label.L0, flag=74000123)
    EnableFlag(74000010)
    AND_15.Add(HealthRatio(4000700) == 0.0)
    OR_2.Add(AND_15)
    OR_2.Add(ActionButtonParamActivated(action_button_id=9101, entity=4001950))
    OR_2.Add(FlagEnabled(74000123))
    
    MAIN.Await(OR_2)
    
    RestartIfFinishedConditionTrue(input_condition=AND_15)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(4003500, erase_root_only=False)
    DeleteVFX(4003501, erase_root_only=False)
    DeleteVFX(4003502, erase_root_only=False)
    DeleteVFX(4003503, erase_root_only=False)
    DeleteVFX(4003504, erase_root_only=False)
    DisableFlag(74000010)
    EnableFlag(14000110)
    EnableFlag(14100000)
    if FlagDisabled(1038):
        PlayCutscene(
            40000020,
            cutscene_flags=0,
            player_id=10000,
            move_to_region=4102100,
            game_map=KILN_OF_THE_FIRST_FLAME,
        )
    else:
        PlayCutscene(
            40000021,
            cutscene_flags=0,
            player_id=10000,
            move_to_region=4102100,
            game_map=KILN_OF_THE_FIRST_FLAME,
        )
    DeleteObjectVFX(4001500)
    DeleteObjectVFX(4001501)
    DeleteObjectVFX(4001502)
    DeleteObjectVFX(4001503)
    DeleteObjectVFX(4001510)
    DeleteObjectVFX(4001511)
    DeleteObjectVFX(4001512)
    DeleteObjectVFX(4001513)
    DeleteObjectVFX(4001514)
    DeleteObjectVFX(4001515)
    DeleteObjectVFX(4001516)
    DeleteObjectVFX(4001517)
    DeleteObjectVFX(4001518)
    DeleteObjectVFX(4001519)
    DeleteObjectVFX(4001520)
    DeleteObjectVFX(4001521)
    DeleteObjectVFX(4001522)
    DeleteObjectVFX(4001523)
    DeleteObjectVFX(4001524)
    DeleteObjectVFX(4001525)
    DeleteObjectVFX(4001526)
    DeleteObjectVFX(4001527)
    DeleteObjectVFX(4001528)
    DeleteObjectVFX(4001529)
    DeleteObjectVFX(4001530)
    DeleteObjectVFX(4001531)
    DeleteObjectVFX(4001532)
    DeleteObjectVFX(4001533)
    DeleteObjectVFX(4001534)
    DeleteObjectVFX(4001535)
    DeleteObjectVFX(4001536)
    DeleteObjectVFX(4001537)
    DeleteObjectVFX(4001538)
    DeleteObjectVFX(4001539)
    DeleteObjectVFX(4001540)
    DeleteObjectVFX(4001541)
    DeleteObjectVFX(4001542)
    DeleteObjectVFX(4001543)
    DeleteObjectVFX(4001544)
    DeleteObjectVFX(4001545)
    DeleteObjectVFX(4001546)
    DeleteObjectVFX(4001547)
    DeleteObjectVFX(4001548)
    DeleteObjectVFX(4001549)
    DeleteObjectVFX(4001550)
    DeleteObjectVFX(4001551)
    DeleteObjectVFX(4001552)
    DeleteObjectVFX(4001553)
    DeleteObjectVFX(4001554)
    DeleteObjectVFX(4001555)
    DeleteObjectVFX(4001556)
    DeleteObjectVFX(4001557)
    DeleteObjectVFX(4001558)
    DeleteObjectVFX(4001559)
    DeleteObjectVFX(4001560)
    DeleteObjectVFX(4001561)
    DeleteObjectVFX(4001562)
    DeleteObjectVFX(4001563)
    DeleteObjectVFX(4001564)
    DeleteObjectVFX(4001565)
    DeleteObjectVFX(4001566)
    DeleteObjectVFX(4001567)
    DeleteObjectVFX(4001568)
    DeleteObjectVFX(4001569)
    SetRespawnPoint(respawn_point=4102100)
    SaveRequest()
    WaitFrames(frames=1)


@NeverRestart(14000120)
def Event_14000120(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int, flag_5: int):
    """Event 14000120"""
    if FlagEnabled(flag):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(FlagEnabled(flag_3))
    AND_1.Add(FlagEnabled(flag_4))
    AND_1.Add(FlagEnabled(flag_5))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@RestartOnRest(14000121)
def Event_14000121(_, flag: int, item: int, obj: int, target_entity: int, action_button_id: int, animation: int):
    """Event 14000121"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DeleteObjectVFX(obj, erase_root=False)
    CreateObjectVFX(obj, vfx_id=201, model_point=840066)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)
    AND_1.Add(FlagDisabled(2051))
    AND_1.Add(LeavingSession())
    AND_1.Add(PlayerHasGood(item))
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=target_entity))
    
    MAIN.Await(AND_1)
    
    RotateToFaceEntity(PLAYER, target_entity, animation=animation, wait_for_completion=True)
    if ValueNotEqual(left=animation, right=69050):
        Wait(0.8999999761581421)
    else:
        Wait(2.0)
    EnableFlag(flag)
    RemoveGoodFromPlayer(item=item, quantity=1)
    EnableObject(obj)
    CreateTemporaryVFX(vfx_id=840065, anchor_entity=obj, model_point=201, anchor_type=CoordEntityType.Object)
    CreateObjectVFX(obj, vfx_id=201, model_point=840066)


@RestartOnRest(14000130)
def Event_14000130():
    """Event 14000130"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(6010):
        return
    CreateObjectVFX(4001200, vfx_id=90, model_point=63)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9355, entity=4001200))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(PLAYER, 60070, unknown2=1.0)
    GotoIfFlagEnabled(Label.L10, flag=6030)
    GotoIfFlagEnabled(Label.L9, flag=6029)
    GotoIfFlagEnabled(Label.L8, flag=6028)
    GotoIfFlagEnabled(Label.L7, flag=6027)
    GotoIfFlagEnabled(Label.L6, flag=6026)
    GotoIfFlagEnabled(Label.L5, flag=6025)
    GotoIfFlagEnabled(Label.L4, flag=6024)
    GotoIfFlagEnabled(Label.L3, flag=6023)
    GotoIfFlagEnabled(Label.L2, flag=6022)
    GotoIfFlagEnabled(Label.L1, flag=6021)
    AwardItemLot(4000505, host_only=False)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    AwardItemLot(4000515, host_only=False)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    AwardItemLot(4000525, host_only=False)
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    AwardItemLot(4000535, host_only=False)
    Goto(Label.L0)

    # --- Label 4 --- #
    DefineLabel(4)
    AwardItemLot(4000545, host_only=False)
    Goto(Label.L0)

    # --- Label 5 --- #
    DefineLabel(5)
    AwardItemLot(4000555, host_only=False)
    Goto(Label.L0)

    # --- Label 6 --- #
    DefineLabel(6)
    AwardItemLot(4000565, host_only=False)
    Goto(Label.L0)

    # --- Label 7 --- #
    DefineLabel(7)
    AwardItemLot(4000575, host_only=False)
    Goto(Label.L0)

    # --- Label 8 --- #
    DefineLabel(8)
    AwardItemLot(4000585, host_only=False)
    Goto(Label.L0)

    # --- Label 9 --- #
    DefineLabel(9)
    AwardItemLot(4000595, host_only=False)
    Goto(Label.L0)

    # --- Label 10 --- #
    DefineLabel(10)
    AwardItemLot(4000605, host_only=False)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(4001200)
    EnableFlag(6010)


@RestartOnRest(14005300)
def Event_14005300(_, character: int, region: int):
    """Event 14005300"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))

    # --- Label 0 --- #
    DefineLabel(0)
    SetNest(character, region=region)


@NeverRestart(14000401)
def Event_14000401():
    """Event 14000401"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(14000400)
    End()


@RestartOnRest(14005401)
def Event_14005401():
    """Event 14005401"""
    CommonFunc_20005621(
        0,
        14000400,
        14001400,
        4001400,
        4001401,
        4003401,
        4001402,
        4003402,
        4002401,
        4002402,
        14001401,
        14004400,
        0,
    )


@RestartOnRest(14005420)
def Event_14005420():
    """Event 14005420"""
    RegisterLadder(start_climbing_flag=14000420, stop_climbing_flag=14000421, obj=4001420)


@RestartOnRest(14005440)
def Event_14005440():
    """Event 14005440"""
    MAIN.Await(ObjectBackreadEnabled(obj=4001955))
    
    WaitFrames(frames=1)
    ForceAnimation(4001955, 100000, unknown2=1.0)


@RestartOnRest(14005441)
def Event_14005441():
    """Event 14005441"""
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
    CreateObjectVFX(4001500, vfx_id=200, model_point=800022)
    CreateObjectVFX(4001501, vfx_id=200, model_point=800022)
    CreateObjectVFX(4001502, vfx_id=200, model_point=800022)
    CreateObjectVFX(4001503, vfx_id=200, model_point=800022)
    CreateObjectVFX(4001510, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001511, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001512, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001513, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001514, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001515, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001516, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001517, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001518, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001519, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001520, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001521, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001522, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001523, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001524, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001525, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001526, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001527, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001528, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001529, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001530, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001531, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001532, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001533, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001534, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001535, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001536, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001537, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001538, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001539, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001540, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001541, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001542, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001543, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001544, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001545, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001546, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001547, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001548, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001549, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001550, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001551, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001552, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001553, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001554, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001555, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001556, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001557, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001558, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001559, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001560, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001561, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001562, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001563, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001564, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001565, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001566, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001567, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001568, vfx_id=200, model_point=839010)
    CreateObjectVFX(4001569, vfx_id=200, model_point=839010)


@RestartOnRest(14005442)
def Event_14005442():
    """Event 14005442"""
    DisableObjectActivation(4001252, obj_act_id=-1)


@RestartOnRest(14005445)
def Event_14005445():
    """Event 14005445"""
    if FlagDisabled(131):
        return
    DisableSoapstoneMessage(4004222)


@NeverRestart(14005450)
def Event_14005450():
    """Event 14005450"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DisableSoundEventWithFade(sound_id=4004450, fade_duration=5.0)
    DisableSoundEventWithFade(sound_id=4004460, fade_duration=5.0)
    Wait(0.5)
    OR_1.Add(PlayerStandingOnCollision(4004100))
    OR_1.Add(PlayerStandingOnCollision(4004101))
    OR_1.Add(PlayerStandingOnCollision(4004102))
    OR_1.Add(PlayerStandingOnCollision(4004103))
    OR_1.Add(PlayerStandingOnCollision(4004104))
    OR_1.Add(PlayerStandingOnCollision(4004109))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(74000122))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(50006020):
        EnableSoundEventWithFade(sound_id=4004450, fade_duration=5.0)
    else:
        EnableSoundEventWithFade(sound_id=4004460, fade_duration=5.0)
    Wait(0.5)
    OR_2.Add(PlayerStandingOnCollision(4004100))
    OR_2.Add(PlayerStandingOnCollision(4004101))
    OR_2.Add(PlayerStandingOnCollision(4004102))
    OR_2.Add(PlayerStandingOnCollision(4004103))
    OR_2.Add(PlayerStandingOnCollision(4004104))
    OR_2.Add(PlayerStandingOnCollision(4004109))
    OR_3.Add(not OR_2)
    AND_2.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 50006020))
    OR_3.Add(AND_2)
    
    MAIN.Await(OR_3)
    
    RestartIfFinishedConditionFalse(input_condition=AND_2)
    DisableSoundEventWithFade(sound_id=4004450, fade_duration=5.0)
    DisableSoundEventWithFade(sound_id=4004460, fade_duration=5.0)
    Wait(3.0)
    Restart()


@RestartOnRest(1405451)
def Event_1405451():
    """Event 1405451"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=4004450)
    DisableSoundEvent(sound_id=4004460)


@NeverRestart(14005460)
def Event_14005460():
    """Event 14005460"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    GotoIfFlagDisabled(Label.L0, flag=9400)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9350, entity=4001460))
    
    RotateToFaceEntity(PLAYER, 4001460, animation=60070, wait_for_completion=True)
    AwardItemLot(4000, host_only=False)
    DisableFlag(9400)
    Wait(3.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9350, entity=4001460))
    
    DisplayDialog(text=10012010, anchor_entity=4001460, number_buttons=NumberButtons.OneButton)
    Wait(3.0)
    Restart()


@RestartOnRest(14005461)
def Event_14005461():
    """Event 14005461"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DeleteObjectVFX(4001461)
    OR_1.Add(PlayerHasGood(119))
    OR_1.Add(MultiplayerNetworkPenalized())
    if OR_1:
        return
    CreateObjectVFX(4001461, vfx_id=90, model_point=62)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=4000, entity=4001461))
    
    RotateToFaceEntity(PLAYER, 4001461, animation=60070, wait_for_completion=True)
    AwardItemLot(4020, host_only=False)
    DeleteObjectVFX(4001461)


@NeverRestart(14005470)
def Event_14005470():
    """Event 14005470"""
    DisableNetworkSync()
    AND_1.Add(PlayerStandingOnCollision(4004120))
    AND_2.Add(not AND_1)
    AND_2.Add(InsideMap(game_map=FIRELINK_SHRINE))
    
    MAIN.Await(AND_2)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AND_3.Add(FlagEnabled(743))
    if not AND_3:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    SetAreaWelcomeMessageState(state=False)
    DisplayAreaWelcomeMessage(message=4010)
    DisableFlag(743)


@RestartOnRest(14005471)
def Event_14005471():
    """Event 14005471"""
    DisableNetworkSync()
    AND_1.Add(FlagDisabled(74000013))
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    OR_1.Add(PlayerStandingOnCollision(4004120))
    AND_1.Add(not OR_1)
    AND_1.Add(CharacterAlive(PLAYER))
    
    MAIN.Await(AND_1)
    
    SetAreaWelcomeMessageState(state=False)
    Wait(3.0)
    Restart()


@RestartOnRest(14005472)
def Event_14005472():
    """Event 14005472"""
    DisableNetworkSync()
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    AND_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    SetAreaWelcomeMessageState(state=True)
    EnableFlag(743)


@RestartOnRest(14005473)
def Event_14005473():
    """Event 14005473"""
    DisableNetworkSync()
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3220))
    
    MAIN.Await(AND_1)
    
    SetAreaWelcomeMessageState(state=True)
    EnableFlag(743)


@RestartOnRest(14005474)
def Event_14005474():
    """Event 14005474"""
    DisableNetworkSync()
    AND_1.Add(InsideMap(game_map=FIRELINK_SHRINE))
    AND_1.Add(FlagEnabled(74000013))
    
    MAIN.Await(AND_1)
    
    SetAreaWelcomeMessageState(state=True)
    EnableFlag(743)


@NeverRestart(14005480)
def Event_14005480(_, flag: int):
    """Event 14005480"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    DisableFlag(flag)
    DisableLoadingScreenTips()
    EnableFlag(30)


@RestartOnRest(14005481)
def Event_14005481():
    """Event 14005481"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(InsideMap(game_map=FIRELINK_SHRINE))
    
    EnableLoadingScreenTips()


@RestartOnRest(14005484)
def Event_14005484(_, text: int, anchor_entity: int):
    """Event 14005484"""
    DisableNetworkSync()
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9356, entity=anchor_entity))
    
    DisplayDialog(text=text, anchor_entity=anchor_entity, number_buttons=NumberButtons.OneButton)
    Wait(3.0)
    Restart()


@NeverRestart(14000490)
def Event_14000490():
    """Event 14000490"""
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
    InitializeCrowTradeRegion(region=4002796)
    InitializeCrowTradeRegion(region=4002797)
    DisableFlag(2040)
    DisableFlag(2041)
    DisableFlag(2042)
    DisableFlag(74000990)


@NeverRestart(14000491)
def Event_14000491():
    """Event 14000491"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(74000995)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=4002795))
    
    EnableFlag(74000995)
    Wait(1.0)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=4002795))
    
    DisableFlag(74000995)
    Wait(1.0)
    Restart()


@NeverRestart(14005800)
def Event_14005800():
    """Event 14005800"""
    if FlagEnabled(14000800):
        return
    
    MAIN.Await(HealthRatio(4000800) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(4000800, 777777777, sound_type=SoundType.s_SFX)
    Wait(4.0)
    KillBoss(game_area_param_id=4000800)
    EnableFlag(14000800)
    EnableFlag(9319)
    EnableFlag(6319)


@RestartOnRest(14005810)
def Event_14005810():
    """Event 14005810"""
    GotoIfFlagDisabled(Label.L0, flag=14000800)
    Kill(4000800)
    DisableCharacter(4000800)
    DisableAnimations(4000800)
    DisableMapCollision(collision=4004150)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(4000800)
    DisableHealthBar(4000800)
    EnableInvincibility(4000800)
    SetLockOnPoint(character=4000800, lock_on_model_point=221, state=False)
    SetCollisionMask(4000800, bit_index=0, switch_type=OnOffChange.Off)
    ForceAnimation(4000800, 30002, loop=True, unknown2=1.0)
    GotoIfFlagEnabled(Label.L1, flag=14000802)
    
    MAIN.Await(FlagEnabled(14000802))
    
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(14005805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4002800))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(4000800, 20002, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableInvincibility(4000800)
    SetCollisionMask(4000800, bit_index=0, switch_type=OnOffChange.Off)
    OR_1.Add(CharacterHasTAEEvent(4000800, tae_event_id=40))
    OR_1.Add(ThisEventSlotFlagEnabled())
    
    MAIN.Await(OR_1)
    
    EnableAI(4000800)
    AddSpecialEffect(4000800, 5800)
    EnableHealthBar(4000800)
    SetNetworkUpdateRate(4000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(4000800, name=905110)
    EnableFlag(14000801)
    End()


@NeverRestart(14005811)
def Event_14005811():
    """Event 14005811"""
    if FlagEnabled(14000800):
        return
    GotoIfFlagDisabled(Label.L0, flag=14000802)
    
    MAIN.Await(CharacterBackreadEnabled(4000800))
    
    SetDisplayMask(4000800, bit_index=0, switch_type=OnOffChange.Off)
    SetDisplayMask(4000800, bit_index=2, switch_type=OnOffChange.On)
    SetDisplayMask(4000800, bit_index=3, switch_type=OnOffChange.Off)
    SetDisplayMask(4000800, bit_index=4, switch_type=OnOffChange.Off)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(FlagEnabled(14000802))
    OR_1.Add(ActionButtonParamActivated(action_button_id=8900, entity=4000800))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(14000802):
        return
    Move(PLAYER, destination=4000800, destination_type=CoordEntityType.Character, model_point=100, short_move=True)
    ForceAnimation(PLAYER, 60750, unknown2=1.0)
    ForceAnimation(4000800, 20003, unknown2=1.0)
    OR_1.Add(FlagEnabled(14000802))
    OR_1.Add(CharacterHasTAEEvent(4000800, tae_event_id=20))
    
    MAIN.Await(OR_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=14000802, state=FlagSetting.On)


@RestartOnRest(14005812)
def Event_14005812():
    """Event 14005812"""
    if FlagEnabled(14000800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(4000800, tae_event_id=10))
    
    SetCollisionMask(4000800, bit_index=0, switch_type=OnOffChange.On)
    SetLockOnPoint(character=4000800, lock_on_model_point=221, state=True)
    EnableFlag(14005802)


@RestartOnRest(14005813)
def Event_14005813():
    """Event 14005813"""
    DisableNetworkSync()
    if FlagEnabled(14000800):
        return
    AND_1.Add(FlagEnabled(14005805))
    AND_1.Add(FlagEnabled(14005802))
    
    MAIN.Await(AND_1)
    
    Wait(1.5)
    ChangeCamera(normal_camera_id=5110, locked_camera_id=5110)
    
    MAIN.Await(HealthRatio(4000800) <= 0.0)
    
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest(14000816)
def Event_14000816():
    """Event 14000816"""
    DisableObjectActivation(4001260, obj_act_id=-1)
    DisableObjectActivation(4001261, obj_act_id=-1)
    if FlagEnabled(64000260):
        return
    
    MAIN.Await(FlagEnabled(14000800))
    
    EnableObjectActivation(4001260, obj_act_id=400005)


@RestartOnRest(14005820)
def Event_14005820():
    """Event 14005820"""
    CommonFunc_20005800(
        0,
        flag=14000800,
        entity=4001800,
        region=4002800,
        flag_1=14005805,
        action_button_id=4001800,
        character=4000800,
        left=14000801,
        region_1=4002800,
    )
    CommonFunc_20005801(
        0,
        flag=14000800,
        entity=4001800,
        region=4002800,
        flag_1=14005805,
        action_button_id=4001800,
        flag_2=14005822,
    )
    CommonFunc_20005820(0, flag=14000800, obj=4001800, model_point=3, left=14000801)
    if FlagEnabled(14000801):
        CommonFunc_20005831(
            0,
            flag=14000800,
            flag_1=14005805,
            flag_2=14005822,
            region=4002800,
            sound_id=4004800,
            sound_id_1=4004801,
            flag_3=14005802,
        )
        End()
    CommonFunc_20001836(0, 14000800, 14005805, 14005822, 14000801, 4004800, 4004801, 14005802)


@NeverRestart(14005830)
def Event_14005830():
    """Event 14005830"""
    if FlagEnabled(14000830):
        return
    
    MAIN.Await(HealthRatio(4000830) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(4000830, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(4000830))
    
    KillBoss(game_area_param_id=4000830)
    EnableFlag(14000830)
    EnableFlag(9320)
    EnableFlag(6320)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest(14005840)
def Event_14005840():
    """Event 14005840"""
    GotoIfFlagDisabled(Label.L0, flag=14000830)
    Kill(4000830)
    DisableAnimations(4000830)
    DisableCharacter(4000830)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableInvincibility(4000830)
    DisableAI(4000830)
    SetLockOnPoint(character=4000830, lock_on_model_point=221, state=False)
    SetCollisionMask(4000830, bit_index=0, switch_type=OnOffChange.Off)
    ForceAnimation(4000830, 30002, loop=True, unknown2=1.0)
    GotoIfFlagEnabled(Label.L1, flag=14000831)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4002831))
    
    MAIN.Await(AND_1)
    
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(14005835))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4002800))
    
    MAIN.Await(AND_1)

    # --- Label 2 --- #
    DefineLabel(2)
    ForceAnimation(4000830, 20002, unknown2=1.0)
    EnableAI(4000830)
    DisableImmortality(4000830)
    DisableInvincibility(4000830)
    SetNetworkUpdateRate(4000830, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(4000830, name=905115)
    EnableFlag(14000831)


@NeverRestart(14005841)
def Event_14005841():
    """Event 14005841"""
    if FlagEnabled(14000830):
        return
    
    MAIN.Await(HealthRatio(4000830) <= 0.5)
    
    EnableFlag(14005832)


@RestartOnRest(14000842)
def Event_14000842():
    """Event 14000842"""
    WaitFrames(frames=1)
    DisableObjectActivation(4001260, obj_act_id=-1)
    DisableObjectActivation(4001261, obj_act_id=-1)
    if FlagEnabled(64000261):
        return
    
    MAIN.Await(FlagEnabled(14000830))
    
    EnableObjectActivation(4001261, obj_act_id=400005)


@RestartOnRest(14000859)
def Event_14000859():
    """Event 14000859"""
    CommonFunc_20005800(
        0,
        flag=14000830,
        entity=4001800,
        region=4002800,
        flag_1=14005835,
        action_button_id=4001830,
        character=4000830,
        left=14000831,
        region_1=4002831,
    )
    CommonFunc_20005801(
        0,
        flag=14000830,
        entity=4001800,
        region=4002800,
        flag_1=14005835,
        action_button_id=4001830,
        flag_2=14005836,
    )
    CommonFunc_20005820(0, flag=14000830, obj=4001800, model_point=3, left=14000831)
    CommonFunc_20005810(0, flag=14000830, entity=4001800, target_entity=4002800, action_button_id=10000)
    if FlagEnabled(14000831):
        CommonFunc_20005831(
            0,
            flag=14000830,
            flag_1=14005835,
            flag_2=14005836,
            region=4002800,
            sound_id=4004830,
            sound_id_1=4004831,
            flag_3=14005832,
        )
        End()
    CommonFunc_20001836(0, 14000830, 14005835, 14005836, 14000831, 4004830, 4004831, 14005832)


@NeverRestart(14005500)
def Event_14005500(_, character: int, animation_id: int, obj: int, destination: int):
    """Event 14005500"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1235, 1239))
    DisableNetworkConnectedFlagRange(flag_range=(1235, 1239))
    SetNetworkConnectedFlagState(flag=1235, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1236))
    AND_1.Add(FlagEnabled(70000063))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1235, 1239))
    SetNetworkConnectedFlagState(flag=1235, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1220, 1234))
    DisableNetworkConnectedFlagRange(flag_range=(1220, 1234))
    SetNetworkConnectedFlagState(flag=1220, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1235)
    AND_2.Add(FlagEnabled(1221))
    AND_2.Add(FlagEnabled(74000553))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1220, 1234))
    SetNetworkConnectedFlagState(flag=1222, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1221))
    AND_3.Add(FlagEnabled(74000583))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1220, 1234))
    SetNetworkConnectedFlagState(flag=1223, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000063)
    DisableFlag(74000551)
    if FlagEnabled(1235):
        DisableFlag(74000570)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1221)
    GotoIfFlagRangeAnyEnabled(Label.L3, flag_range=(1222, 1234))
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    GotoIfFlagEnabled(Label.L1, flag=1236)
    GotoIfFlagEnabled(Label.L2, flag=1238)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@NeverRestart(14005501)
def Event_14005501(_, flag: int, flag_1: int, bit_count: uint, bit_count_1: uchar, max_value__value: uint):
    """Event 14005501"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301100))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301110))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301120))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301130))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301140))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301150))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301160))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301170))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301180))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301190))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301200))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301210))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301220))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301230))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73301240))
    AND_1.Add(FlagEnabled(73301250))
    AND_1.Add(FlagEnabled(73301260))
    AND_1.Add(FlagEnabled(73301270))
    AND_1.Add(FlagEnabled(73301280))
    AND_1.Add(FlagEnabled(73301290))
    AND_1.Add(FlagEnabled(73301300))
    AND_1.Add(FlagEnabled(73301310))
    AND_1.Add(FlagEnabled(73301320))
    AND_1.Add(FlagEnabled(73301330))
    
    MAIN.Await(OR_1)
    
    IncrementEventValue(flag_1, bit_count=bit_count, max_value=max_value__value)
    OR_2.Add(EventValue(flag=flag_1, bit_count=bit_count_1) < max_value__value)
    if OR_2:
        return RESTART
    EnableFlag(flag)


@NeverRestart(14005503)
def Event_14005503(_, flag: int):
    """Event 14005503"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(73301100))
    AND_1.Add(FlagEnabled(73301110))
    AND_1.Add(FlagEnabled(73301120))
    AND_1.Add(FlagEnabled(73301130))
    AND_1.Add(FlagEnabled(73301140))
    AND_1.Add(FlagEnabled(73301150))
    AND_1.Add(FlagEnabled(73301160))
    AND_1.Add(FlagEnabled(73301170))
    AND_1.Add(FlagEnabled(73301180))
    AND_1.Add(FlagEnabled(73301190))
    AND_1.Add(FlagEnabled(73301200))
    AND_1.Add(FlagEnabled(73301210))
    AND_1.Add(FlagEnabled(73301220))
    AND_1.Add(FlagEnabled(73301230))
    AND_1.Add(FlagEnabled(73301240))
    AND_1.Add(FlagEnabled(73301250))
    AND_1.Add(FlagEnabled(73301260))
    AND_1.Add(FlagEnabled(73301270))
    AND_1.Add(FlagEnabled(73301280))
    AND_1.Add(FlagEnabled(73301290))
    AND_1.Add(FlagEnabled(73301300))
    AND_1.Add(FlagEnabled(73301310))
    AND_1.Add(FlagEnabled(73301320))
    AND_1.Add(FlagEnabled(73301330))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)


@NeverRestart(14005520)
def Event_14005520(_, character: int, animation_id: int, destination: int, obj: int):
    """Event 14005520"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1055, 1059))
    DisableNetworkConnectedFlagRange(flag_range=(1055, 1059))
    SetNetworkConnectedFlagState(flag=1055, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1056))
    AND_1.Add(FlagEnabled(70000054))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1055, 1059))
    SetNetworkConnectedFlagState(flag=1055, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1040, 1054))
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1040, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1055)
    AND_2.Add(FlagEnabled(700))
    AND_2.Add(FlagEnabled(1040))
    AND_2.Add(PlayerRemainingYoelLevelComparison(comparison_type=ComparisonType.LessThanOrEqual, value=0))
    AND_2.Add(FlagDisabled(74000124))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1041, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1041))
    AND_3.Add(FlagEnabled(50006193))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1042, state=FlagSetting.On)
    AND_9.Add(FlagEnabled(1042))
    AND_9.Add(FlagEnabled(74000640))
    SkipLinesIfConditionFalse(2, AND_9)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1045, state=FlagSetting.On)
    AND_4.Add(FlagRangeAnyEnabled(flag_range=(1040, 1042)))
    AND_5.Add(PlayerRemainingYoelLevelComparison(comparison_type=ComparisonType.GreaterThan, value=0))
    AND_5.Add(FlagEnabled(1078))
    OR_4.Add(AND_5)
    OR_4.Add(FlagEnabled(74000124))
    AND_4.Add(OR_4)
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1044, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1041))
    AND_6.Add(FlagRangeAnyEnabled(flag_range=(1340, 1347)))
    AND_6.Add(FlagEnabled(1358))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1044, state=FlagSetting.On)
    AND_7.Add(FlagRangeAnyEnabled(flag_range=(1041, 1042)))
    AND_7.Add(FlagEnabled(1561))
    AND_7.Add(FlagEnabled(1578))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1043, state=FlagSetting.On)
    AND_8.Add(FlagEnabled(1043))
    OR_8.Add(FlagEnabled(74000619))
    OR_8.Add(FlagDisabled(74000600))
    AND_8.Add(OR_8)
    SkipLinesIfConditionFalse(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1044, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000054)
    if FlagEnabled(1055):
        DisableFlag(74000620)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L1, flag=1041)
    GotoIfFlagEnabled(Label.L1, flag=1042)
    GotoIfFlagEnabled(Label.L1, flag=1043)
    GotoIfFlagEnabled(Label.L2, flag=1044)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableObject(obj)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    GotoIfFlagEnabled(Label.L16, flag=1056)
    GotoIfFlagEnabled(Label.L18, flag=1058)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    EnableTreasure(obj=obj)
    End()


@NeverRestart(14005521)
def Event_14005521(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    value: float,
    first_flag: int,
    last_flag: int,
    right: int,
):
    """Event 14005521"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_2)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(HealthRatio(character) < value)
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(flag_2))
    AND_1.Add(OR_2)
    OR_3.Add(FlagEnabled(1041))
    OR_3.Add(FlagEnabled(1043))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    GotoIfValueComparison(Label.L0, comparison_type=ComparisonType.Equal, left=1, right=right)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    Goto(Label.L9)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    SaveRequest()
    WaitFrames(frames=1)
    AND_3.Add(CharacterHasSpecialEffect(character, 159))
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(character, 0, unknown2=1.0)


@NeverRestart(14000522)
def Event_14000522():
    """Event 14000522"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(FlagEnabled(1055))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1041, 1042)))
    AND_1.Add(FlagEnabled(74000124))
    
    MAIN.Await(AND_1)
    
    DisableNetworkConnectedFlagRange(flag_range=(1040, 1054))
    SetNetworkConnectedFlagState(flag=1043, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=74000630, state=FlagSetting.Off)
    SaveRequest()


@NeverRestart(14005540)
def Event_14005540(_, character: int, character_1: int, animation_id: int, destination: int, destination_1: int):
    """Event 14005540"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1315, 1319))
    DisableNetworkConnectedFlagRange(flag_range=(1315, 1319))
    SetNetworkConnectedFlagState(flag=1315, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1316))
    AND_1.Add(FlagEnabled(70000067))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1315, 1319))
    SetNetworkConnectedFlagState(flag=1315, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1300, 1314))
    DisableNetworkConnectedFlagRange(flag_range=(1300, 1314))
    SetNetworkConnectedFlagState(flag=1300, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L10, flag=1315)
    AND_2.Add(FlagEnabled(1300))
    AND_2.Add(FlagEnabled(73100304))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1300, 1314))
    SetNetworkConnectedFlagState(flag=1301, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1301))
    AND_3.Add(FlagEnabled(9307))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1300, 1314))
    SetNetworkConnectedFlagState(flag=1302, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1302))
    AND_4.Add(FlagEnabled(74000650))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1300, 1314))
    SetNetworkConnectedFlagState(flag=1303, state=FlagSetting.On)
    AND_6.Add(FlagRangeAnyEnabled(flag_range=(1301, 1303)))
    AND_6.Add(FlagEnabled(1298))
    SkipLinesIfConditionFalse(5, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1300, 1314))
    SetNetworkConnectedFlagState(flag=1302, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1315, 1319))
    SetNetworkConnectedFlagState(flag=1317, state=FlagSetting.On)
    Goto(Label.L9)
    AND_5.Add(FlagEnabled(1303))
    AND_5.Add(FlagEnabled(9308))
    AND_5.Add(FlagDisabled(73101710))
    AND_5.Add(FlagDisabled(73101720))
    AND_5.Add(FlagDisabled(73101730))
    AND_5.Add(FlagDisabled(73101740))
    AND_5.Add(FlagDisabled(73101750))
    SkipLinesIfConditionFalse(4, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1300, 1314))
    SetNetworkConnectedFlagState(flag=1305, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1315, 1319))
    SetNetworkConnectedFlagState(flag=1318, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000067)
    if FlagEnabled(1315):
        DisableFlag(74000670)

    # --- Label 10 --- #
    DefineLabel(10)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Move(character_1, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    GotoIfFlagEnabled(Label.L2, flag=1302)
    GotoIfFlagEnabled(Label.L4, flag=1304)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L16, flag=1316)
    GotoIfFlagEnabled(Label.L17, flag=1317)
    GotoIfFlagEnabled(Label.L18, flag=1318)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)

    # --- Label 17 --- #
    DefineLabel(17)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L18, flag=1318)
    DisableAI(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character_1)
    End()


@NeverRestart(14005541)
def Event_14005541(
    _,
    character: int,
    flag: int,
    flag_1: int,
    first_flag: int,
    last_flag: int,
    flag_2: int,
    first_flag_1: int,
    last_flag_1: int,
    flag_3: int,
):
    """Event 14005541"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_3))
    OR_1.Add(FlagEnabled(first_flag_1))
    OR_1.Add(FlagEnabled(flag))
    AND_1.Add(OR_1)
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(first_flag, last_flag)))
    AND_1.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag_1, last_flag_1))
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    SaveRequest()
    WaitFrames(frames=1)
    OR_15.Add(CharacterHasSpecialEffect(character, 159))
    SkipLinesIfConditionFalse(2, OR_15)
    ForceAnimation(character, 0, unknown2=1.0)


@NeverRestart(14005542)
def Event_14005542(_, character: int, character_1: int, character_2: int, character_3: int, animation_id: int):
    """Event 14005542"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1301, 1303)))
    AND_1.Add(FlagEnabled(1315))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1282, 1283)))
    AND_1.Add(FlagEnabled(1295))
    AND_1.Add(FlagEnabled(74000351))
    AND_1.Add(PlayerInOwnWorld())
    if not AND_1:
        return
    GotoIfPlayerNotInOwnWorld(Label.L10)
    DisableNetworkConnectedFlagRange(flag_range=(1300, 1314))
    SetNetworkConnectedFlagState(flag=1304, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1315, 1319))
    SetNetworkConnectedFlagState(flag=1317, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L0, flag=1282)
    DisableNetworkConnectedFlagRange(flag_range=(1280, 1294))
    SetNetworkConnectedFlagState(flag=1284, state=FlagSetting.On)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableNetworkConnectedFlagRange(flag_range=(1280, 1294))
    SetNetworkConnectedFlagState(flag=1285, state=FlagSetting.On)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    SetTeamType(character_1, TeamType.HostileNPC)
    DisableAI(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    EnableCharacter(character_3)
    EnableBackread(character_3)
    SetTeamType(character_3, TeamType.NoTeam)
    ForceAnimation(character_3, animation_id, loop=True, unknown2=1.0)


@NeverRestart(14005543)
def Event_14005543(_, character: int):
    """Event 14005543"""
    AND_1.Add(FlagEnabled(1304))
    AND_1.Add(FlagDisabled(1318))
    AND_2.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=10.0))
    OR_1.Add(AND_2)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    EnableAI(character)
    ReplanAI(character)
    WaitFrames(frames=1)
    OR_2.Add(CharacterHasSpecialEffect(character, 159))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    SkipLinesIfConditionFalse(1, OR_2)
    RotateToFaceEntity(character, PLAYER, wait_for_completion=True)


@NeverRestart(14005560)
def Event_14005560(_, character: int, character_1: int, destination: int, destination_1: int):
    """Event 14005560"""
    DisableAnimations(4000762)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1115, 1119))
    DisableNetworkConnectedFlagRange(flag_range=(1115, 1119))
    SetNetworkConnectedFlagState(flag=1115, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1116))
    AND_1.Add(FlagEnabled(70000057))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1115, 1119))
    SetNetworkConnectedFlagState(flag=1115, state=FlagSetting.On)
    DisableFlagRange((74000848, 74000849))
    SkipLinesIfFlagRangeAnyEnabled(2, (1100, 1114))
    DisableNetworkConnectedFlagRange(flag_range=(1100, 1114))
    SetNetworkConnectedFlagState(flag=1100, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1115)
    AND_2.Add(FlagEnabled(1100))
    OR_1.Add(FlagEnabled(9303))
    OR_1.Add(FlagEnabled(9306))
    AND_2.Add(OR_1)
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1100, 1114))
    SetNetworkConnectedFlagState(flag=1101, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1101))
    AND_3.Add(FlagEnabled(9307))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1100, 1114))
    SetNetworkConnectedFlagState(flag=1102, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1102))
    AND_5.Add(FlagEnabled(74000808))
    SkipLinesIfConditionFalse(3, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1100, 1114))
    SetNetworkConnectedFlagState(flag=1103, state=FlagSetting.On)
    EnableFlag(74000825)
    AND_6.Add(FlagEnabled(1103))
    AND_6.Add(PlayerHasGood(388))
    AND_6.Add(FlagEnabled(53200900))
    SkipLinesIfConditionFalse(6, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1100, 1114))
    SetNetworkConnectedFlagState(flag=1104, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1115, 1119))
    SetNetworkConnectedFlagState(flag=1117, state=FlagSetting.On)
    EnableFlag(50006071)
    EnableFlag(74000201)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000057)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1100)
    GotoIfFlagEnabled(Label.L0, flag=1101)
    GotoIfFlagEnabled(Label.L0, flag=1102)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfFlagRangeAnyEnabled(4, (1116, 1118))
    DisableFlagRange((74000810, 74000813))
    OR_2.Add(FlagDisabled(74000801))
    GotoIfConditionTrue(Label.L1, input_condition=OR_2)
    EnableRandomFlagInRange(flag_range=(74000810, 74000813))
    if FlagEnabled(74000820):
        EnableFlag(74000810)
    GotoIfFlagDisabled(Label.L1, flag=74000810)
    DisableCharacter(character)
    DisableBackread(character)
    Move(character_1, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    DisableCharacter(4000366)
    DisableBackread(4000366)
    SkipLinesIfFlagRangeAnyEnabled(1, (1116, 1118))
    ForceAnimation(character_1, 90960, skip_transition=True, unknown2=1.0)
    Goto(Label.L17)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    SkipLinesIfFlagRangeAnyEnabled(1, (1116, 1118))
    ForceAnimation(character, 90680, skip_transition=True, unknown2=1.0)

    # --- Label 17 --- #
    DefineLabel(17)
    GotoIfFlagEnabled(Label.L19, flag=1116)
    GotoIfFlagEnabled(Label.L19, flag=1117)
    GotoIfFlagEnabled(Label.L20, flag=1118)
    End()

    # --- Label 19 --- #
    DefineLabel(19)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    WaitFrames(frames=1)
    if FlagDisabled(74000810):
        DropMandatoryTreasure(character)
        End()
    DropMandatoryTreasure(character_1)
    End()


@NeverRestart(14005570)
def Event_14005570(_, character: int, character_1: int, destination: int, destination_1: int):
    """Event 14005570"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    SkipLinesIfFlagRangeAnyEnabled(2, (1135, 1139))
    DisableNetworkConnectedFlagRange(flag_range=(1135, 1139))
    SetNetworkConnectedFlagState(flag=1135, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1136))
    AND_1.Add(FlagEnabled(70000058))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1135, 1139))
    SetNetworkConnectedFlagState(flag=1135, state=FlagSetting.On)
    DisableFlag(74000799)
    SkipLinesIfFlagRangeAnyEnabled(2, (1120, 1134))
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1120, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L19, flag=1135)
    AND_3.Add(FlagEnabled(1120))
    AND_3.Add(FlagEnabled(133))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1121, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1121))
    AND_4.Add(FlagEnabled(74000750))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1122, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1122))
    AND_5.Add(FlagEnabled(74000253))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1123, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1123))
    AND_6.Add(FlagEnabled(74000751))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1124, state=FlagSetting.On)
    AND_7.Add(FlagEnabled(1124))
    AND_7.Add(FlagEnabled(8200))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1125, state=FlagSetting.On)
    AND_8.Add(FlagEnabled(1125))
    AND_8.Add(FlagEnabled(74000752))
    SkipLinesIfConditionFalse(2, AND_8)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1126, state=FlagSetting.On)
    OR_1.Add(FlagEnabled(1124))
    OR_1.Add(FlagEnabled(1126))
    AND_9.Add(OR_1)
    AND_9.Add(FlagEnabled(8220))
    SkipLinesIfConditionFalse(3, AND_9)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1127, state=FlagSetting.On)
    EnableFlag(74000790)
    AND_10.Add(FlagEnabled(1127))
    AND_10.Add(FlagEnabled(74000755))
    SkipLinesIfConditionFalse(2, AND_10)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1128, state=FlagSetting.On)
    AND_11.Add(FlagEnabled(1127))
    AND_11.Add(FlagEnabled(74000760))
    AND_11.Add(FlagEnabled(74000756))
    SkipLinesIfConditionFalse(3, AND_11)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1139))
    SetNetworkConnectedFlagState(flag=1130, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=1137, state=FlagSetting.On)
    AND_12.Add(FlagEnabled(1128))
    AND_12.Add(FlagEnabled(9309))
    SkipLinesIfConditionFalse(3, AND_12)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1139))
    SetNetworkConnectedFlagState(flag=1129, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=1138, state=FlagSetting.On)
    OR_2.Add(FlagEnabled(1120))
    OR_2.Add(FlagEnabled(1121))
    AND_13.Add(OR_2)
    AND_13.Add(FlagEnabled(73500150))
    SkipLinesIfConditionFalse(2, AND_13)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1134, state=FlagSetting.On)
    AND_14.Add(FlagRangeAnyEnabled(flag_range=(1122, 1128)))
    AND_14.Add(FlagEnabled(73500150))
    SkipLinesIfConditionFalse(2, AND_14)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1133, state=FlagSetting.On)
    AND_15.Add(FlagEnabled(1133))
    AND_15.Add(FlagEnabled(74000753))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(1120, 1134))
    SetNetworkConnectedFlagState(flag=1134, state=FlagSetting.On)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(70000058)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L0, flag=1121)
    GotoIfFlagEnabled(Label.L1, flag=1123)
    GotoIfFlagEnabled(Label.L2, flag=1125)
    GotoIfFlagEnabled(Label.L3, flag=1127)
    GotoIfFlagEnabled(Label.L4, flag=1129)
    GotoIfFlagEnabled(Label.L5, flag=1133)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 3 --- #
    DefineLabel(3)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    SkipLinesIfFlagRangeAnyEnabled(1, (1136, 1138))
    ForceAnimation(character, 90340, skip_transition=True, unknown2=1.0)
    Goto(Label.L18)

    # --- Label 5 --- #
    DefineLabel(5)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    if FlagDisabled(1127):
        CommonFunc_20006000(
            0,
            character=4000780,
            flag=1136,
            flag_1=1137,
            flag_2=74000770,
            value=0.699999988079071,
            first_flag=1135,
            last_flag=1139,
            right=0,
        )
        CommonFunc_20006001(0, attacked_entity=4000780, flag=1136, flag_1=1137, flag_2=74000770, right=3)
    GotoIfFlagEnabled(Label.L19, flag=1136)
    GotoIfFlagEnabled(Label.L19, flag=1137)
    GotoIfFlagEnabled(Label.L20, flag=1138)
    End()

    # --- Label 4 --- #
    DefineLabel(4)
    DisableCharacter(character)
    DisableBackread(character)
    Move(character_1, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character_1)
    EzstateAIRequest(character_1, command_id=800, command_slot=1)
    End()

    # --- Label 19 --- #
    DefineLabel(19)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()


@RestartOnRest(14005571)
def Event_14005571():
    """Event 14005571"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(70000116):
        return
    AND_1.Add(FlagEnabled(1124))
    AND_1.Add(FlagEnabled(9303))
    AND_1.Add(FlagEnabled(9314))
    SkipLinesIfConditionFalse(1, AND_1)
    EnableFlag(70000118)


@NeverRestart(14005580)
def Event_14005580(
    _,
    character: int,
    character_1: int,
    animation_id: int,
    animation_id_1: int,
    destination: int,
    destination_1: int,
):
    """Event 14005580"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1355, 1359))
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1355, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1356))
    AND_1.Add(FlagEnabled(70000069))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1355, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1340, 1354))
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1340, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1355)
    AND_2.Add(FlagEnabled(1340))
    AND_2.Add(FlagEnabled(73300151))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1341, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1341))
    AND_3.Add(FlagEnabled(9311))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1342, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1342))
    AND_4.Add(FlagEnabled(74000700))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1344, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1350))
    AND_5.Add(FlagEnabled(8260))
    SkipLinesIfConditionFalse(3, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1351, state=FlagSetting.On)
    EnableFlag(74000180)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000069)
    if FlagEnabled(1355):
        DisableFlag(74000720)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1342)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Move(character_1, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    GotoIfFlagEnabled(Label.L1, flag=1356)
    GotoIfFlagEnabled(Label.L2, flag=1357)
    GotoIfFlagEnabled(Label.L3, flag=1358)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    ForceAnimation(character, animation_id, unknown2=1.0)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    ForceAnimation(character_1, animation_id, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    SetTeamType(character, TeamType.HostileNPC)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    DisableAI(character)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    SetTeamType(character_1, TeamType.HostileNPC)
    ForceAnimation(character_1, animation_id_1, unknown2=1.0)
    DisableAI(character_1)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character_1)
    End()


@NeverRestart(14005581)
def Event_14005581(_, character: int, character_1: int, character_2: int, flag: int, flag_1: int, value: float):
    """Event 14005581"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    AND_1.Add(FlagRangeAllDisabled(flag_range=(1356, 1357)))
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(HealthRatio(character_1) > 0.0)
    AND_1.Add(FlagEnabled(1342))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(HealthRatio(character) < value)
    OR_1.Add(AND_2)
    AND_3.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=PLAYER))
    AND_3.Add(HealthRatio(character_1) < value)
    OR_1.Add(AND_3)
    OR_1.Add(FlagEnabled(flag))
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    AND_4.Add(FlagRangeAllDisabled(flag_range=(1496, 1497)))
    AND_4.Add(HealthRatio(character_2) > 0.0)
    AND_4.Add(FlagEnabled(1482))
    AND_5.Add(AttackedWithDamageType(attacked_entity=character_2, attacker=PLAYER))
    AND_5.Add(HealthRatio(character_2) < value)
    OR_2.Add(AND_5)
    OR_2.Add(FlagEnabled(flag_1))
    AND_4.Add(OR_2)
    OR_3.Add(AND_4)
    
    MAIN.Await(OR_3)
    
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    SetTeamType(character_2, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(1355, 1359))
    SetNetworkConnectedFlagState(flag=1356, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1495, 1499))
    SetNetworkConnectedFlagState(flag=1496, state=FlagSetting.On)
    SaveRequest()
    WaitFrames(frames=1)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=159)
    ForceAnimation(character, 0, unknown2=1.0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character_1, special_effect=159)
    ForceAnimation(character_1, 0, unknown2=1.0)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character_2, special_effect=159)
    ForceAnimation(character_2, 0, unknown2=1.0)


@NeverRestart(14005582)
def Event_14005582(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    value: float,
    first_flag: int,
    last_flag: int,
    flag_3: int,
    flag_4: int,
):
    """Event 14005582"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_2)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(FlagEnabled(flag_4))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(HealthRatio(character) < value)
    OR_1.Add(AND_2)
    OR_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(flag_3))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    SaveRequest()
    WaitFrames(frames=1)
    AND_3.Add(CharacterHasSpecialEffect(character, 159))
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(character, 0, unknown2=1.0)


@NeverRestart(14000583)
def Event_14000583(
    _,
    character: int,
    character_1: int,
    flag: int,
    flag_1: int,
    character_2: int,
    first_flag: int,
    last_flag: int,
    flag_2: int,
):
    """Event 14000583"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(HealthRatio(character_1) > 0.0)
    AND_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(first_flag))
    OR_1.Add(FlagEnabled(flag))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterDead(character_2))
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    OR_15.Add(CharacterHasSpecialEffect(character, 150))
    SkipLinesIfConditionFalse(1, MAIN)
    ForceAnimation(character, 0, unknown2=1.0)
    OR_14.Add(CharacterHasSpecialEffect(character, 150))
    SkipLinesIfConditionFalse(1, MAIN)
    ForceAnimation(character_1, 0, unknown2=1.0)
    AICommand(character, command_id=20, command_slot=1)
    ReplanAI(character)
    AICommand(character_1, command_id=20, command_slot=1)
    ReplanAI(character_1)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    SaveRequest()


@NeverRestart(14005584)
def Event_14005584(_, character: int, character_1: int, flag: int, flag_1: int):
    """Event 14005584"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(CharacterHasSpecialEffect(character, 150))
    OR_1.Add(CharacterHasSpecialEffect(character, 151))
    OR_1.Add(CharacterHasSpecialEffect(character_1, 150))
    OR_1.Add(CharacterHasSpecialEffect(character_1, 151))
    if OR_1:
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    
    MAIN.Await(AND_1)
    
    EzstateAIRequest(character, command_id=1903, command_slot=1)
    EzstateAIRequest(character_1, command_id=1903, command_slot=1)
    WaitFrames(frames=10)
    Restart()


@NeverRestart(14000585)
def Event_14000585(
    _,
    character: int,
    flag: int,
    flag_1: int,
    character_1: int,
    character_2: int,
    first_flag: int,
    last_flag: int,
    flag_2: int,
):
    """Event 14000585"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventFlagEnabled():
        return
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(first_flag))
    OR_1.Add(FlagEnabled(flag))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterDead(character_1))
    OR_2.Add(CharacterDead(character_2))
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    OR_15.Add(CharacterHasSpecialEffect(character, 150))
    SkipLinesIfConditionFalse(2, MAIN)
    ForceAnimation(character, 0, unknown2=1.0)
    ReplanAI(character)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    SaveRequest()


@NeverRestart(14005586)
def Event_14005586(_, character: int, animation_id: int, destination: int):
    """Event 14005586"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1495, 1499))
    DisableNetworkConnectedFlagRange(flag_range=(1495, 1499))
    SetNetworkConnectedFlagState(flag=1495, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1496))
    AND_1.Add(FlagEnabled(70000076))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1495, 1499))
    SetNetworkConnectedFlagState(flag=1495, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1480, 1494))
    DisableNetworkConnectedFlagRange(flag_range=(1480, 1494))
    SetNetworkConnectedFlagState(flag=1480, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1495)
    AND_2.Add(FlagEnabled(1480))
    AND_2.Add(FlagEnabled(73300151))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1480, 1494))
    SetNetworkConnectedFlagState(flag=1481, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1481))
    AND_3.Add(FlagEnabled(9311))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1480, 1494))
    SetNetworkConnectedFlagState(flag=1482, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1482))
    AND_4.Add(FlagEnabled(74000700))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1480, 1494))
    SetNetworkConnectedFlagState(flag=1484, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000076)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1482)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    GotoIfFlagEnabled(Label.L1, flag=1496)
    GotoIfFlagEnabled(Label.L1, flag=1497)
    GotoIfFlagEnabled(Label.L3, flag=1498)
    ForceAnimation(character, animation_id, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()


@RestartOnRest(14005587)
def Event_14005587(_, character: int, flag: int, flag_1: int):
    """Event 14005587"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 151))
    
    MAIN.Await(AND_1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    WaitFrames(frames=1)
    
    MAIN.Await(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    Kill(character, award_souls=True)


@NeverRestart(14005600)
def Event_14005600(_, character: int, destination: int, destination_1: int, destination_2: int, destination_3: int):
    """Event 14005600"""
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(2, (1015, 1019))
    DisableNetworkConnectedFlagRange(flag_range=(1015, 1019))
    SetNetworkConnectedFlagState(flag=1015, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1018))
    AND_1.Add(CharacterAlive(character))
    SkipLinesIfConditionFalse(4, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1015, 1019))
    SetNetworkConnectedFlagState(flag=1015, state=FlagSetting.On)
    EnableFlag(74000121)
    EnableFlag(74000100)
    SkipLinesIfFlagRangeAnyEnabled(2, (1000, 1014))
    DisableNetworkConnectedFlagRange(flag_range=(1000, 1014))
    SetNetworkConnectedFlagState(flag=1000, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1001))
    AND_2.Add(FlagEnabled(145))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1000, 1014))
    SetNetworkConnectedFlagState(flag=1002, state=FlagSetting.On)
    DisableFlagRange((74000135, 74000138))
    DisableFlagRange((74000103, 74000109))

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L16, flag=74000147)
    GotoIfFlagEnabled(Label.L15, flag=74000148)
    GotoIfFlagEnabled(Label.L17, flag=74000149)
    AND_3.Add(FlagEnabled(1000))
    AND_3.Add(FlagEnabled(131))
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    GotoIfFlagEnabled(Label.L0, flag=1000)
    GotoIfFlagEnabled(Label.L2, flag=1001)
    GotoIfFlagEnabled(Label.L1, flag=1002)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L10, flag=1018)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(character, destination=destination_3, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L10, flag=1018)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L10, flag=1018)
    EnableRandomFlagInRange(flag_range=(74000103, 74000109))
    GotoIfFlagEnabled(Label.L16, flag=74000103)
    GotoIfFlagEnabled(Label.L16, flag=74000104)
    AND_5.Add(FlagEnabled(74000105))
    AND_5.Add(FlagDisabled(50006020))
    GotoIfConditionTrue(Label.L17, input_condition=AND_5)

    # --- Label 15 --- #
    DefineLabel(15)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    ForceAnimation(character, 700, loop=True, skip_transition=True, unknown2=1.0)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 17 --- #
    DefineLabel(17)
    ForceAnimation(character, 30001, unknown2=1.0)
    Move(character, destination=destination_2, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(14000601)
def Event_14000601(_, flag: int):
    """Event 14000601"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventFlagEnabled():
        return
    EnableFlag(flag)


@NeverRestart(14005602)
def Event_14005602(_, character: int, item_lot_param_id: int):
    """Event 14005602"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(CharacterDead(character))
    
    AwardItemLot(item_lot_param_id, host_only=False)
    DisableFlag(74000130)
    DisableFlag(74000131)


@NeverRestart(14000603)
def Event_14000603(_, flag: int, flag_1: int):
    """Event 14000603"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    EnableFlag(flag_1)


@NeverRestart(14005604)
def Event_14005604(_, character: int, region: int):
    """Event 14005604"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1000))
    AND_1.Add(FlagEnabled(9210))
    
    MAIN.Await(AND_1)
    
    SetNest(character, region=region)
    WaitFrames(frames=1)
    DisableNetworkConnectedFlagRange(flag_range=(1000, 1014))
    SetNetworkConnectedFlagState(flag=1001, state=FlagSetting.On)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=2, character=character, special_effect=151)
    ForceAnimation(character, 20017, wait_for_completion=True, unknown2=1.0)
    SkipLines(2)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=153)
    ForceAnimation(character, 20019, wait_for_completion=True, unknown2=1.0)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 154))
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 154))
    
    AICommand(character, command_id=-1, command_slot=0)


@NeverRestart(14005605)
def Event_14005605(_, character: int, special_effect: int, animation_id: int):
    """Event 14005605"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=5.0))
    AND_1.Add(CharacterHasSpecialEffect(character, 150))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, special_effect))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(character, animation_id, wait_for_completion=True, unknown2=1.0)
    Restart()


@RestartOnRest(14005615)
def Event_14005615(_, character: int):
    """Event 14005615"""
    if PlayerNotInOwnWorld():
        return
    DisableSoundEvent(sound_id=4003700)
    DisableSoundEvent(sound_id=4003701)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 155))
    
    AND_1.Add(PlayerGender(gender=Gender.Male))
    SkipLinesIfConditionFalse(2, AND_1)
    EnableSoundEvent(sound_id=4003700)
    SkipLines(1)
    EnableSoundEvent(sound_id=4003701)
    
    MAIN.Await(CharacterDoesNotHaveSpecialEffect(character, 155))
    
    Restart()


@RestartOnRest(14005616)
def Event_14005616(_, character: int):
    """Event 14005616"""
    DisableFlag(74000139)
    
    MAIN.Await(FlagEnabled(74000139))
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=153)
    ForceAnimation(character, 20018, unknown2=1.0)
    Restart()


@NeverRestart(14005618)
def Event_14005618():
    """Event 14005618"""
    if FlagDisabled(14005617):
        return
    EnableFlag(14000618)


@NeverRestart(14005619)
def Event_14005619():
    """Event 14005619"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(6500):
        return
    
    MAIN.Await(FlagEnabled(6500))
    
    if FlagEnabled(74000015):
        ForceAnimation(4001950, 10, unknown2=1.0)
        End()
    if FlagEnabled(74000016):
        ForceAnimation(4001950, 20, unknown2=1.0)
        End()
    if FlagEnabled(74000017):
        ForceAnimation(4001950, 30, unknown2=1.0)
        End()
    if FlagEnabled(74000018):
        ForceAnimation(4001950, 40, unknown2=1.0)
        End()
    if FlagEnabled(74000019):
        ForceAnimation(4001950, 50, unknown2=1.0)
        End()
    if FlagEnabled(74000020):
        ForceAnimation(4001950, 60, unknown2=1.0)
        End()
    if FlagEnabled(74000021):
        ForceAnimation(4001950, 70, unknown2=1.0)
        End()
    if FlagEnabled(74000022):
        ForceAnimation(4001950, 80, unknown2=1.0)
        End()
    if FlagEnabled(74000023):
        ForceAnimation(4001950, 90, unknown2=1.0)
        End()
    if FlagEnabled(74000024):
        ForceAnimation(4001950, 100, unknown2=1.0)
        End()
    ForceAnimation(4001950, 9900, unknown2=1.0)
    End()


@NeverRestart(14005620)
def Event_14005620(_, character: int, character_1: int, destination: int):
    """Event 14005620"""
    GotoIfPlayerNotInOwnWorld(Label.L20)
    EnableFlag(64001251)
    DisableFlag(74000919)
    SkipLinesIfFlagRangeAnyEnabled(2, (1375, 1379))
    DisableNetworkConnectedFlagRange(flag_range=(1375, 1379))
    SetNetworkConnectedFlagState(flag=1375, state=FlagSetting.On)
    AND_15.Add(FlagEnabled(1376))
    AND_15.Add(FlagEnabled(70000070))
    SkipLinesIfConditionFalse(2, AND_15)
    DisableNetworkConnectedFlagRange(flag_range=(1375, 1379))
    SetNetworkConnectedFlagState(flag=1375, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1360, 1374))
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1360, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L19, flag=1375)
    AND_1.Add(FlagEnabled(1365))
    AND_1.Add(FlagEnabled(1204))
    AND_1.Add(FlagEnabled(74000920))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1366, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1366))
    AND_2.Add(FlagEnabled(1206))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1365, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1365))
    AND_3.Add(FlagEnabled(1207))
    AND_3.Add(FlagEnabled(74000921))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1367, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1367))
    AND_4.Add(FlagEnabled(74000925))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1365, state=FlagSetting.On)
    EnableFlag(74000914)
    EnableFlag(70000401)

    # --- Label 19 --- #
    DefineLabel(19)
    DisableFlag(70000070)
    if FlagEnabled(1375):
        DisableFlag(74000949)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L0, flag=1364)
    GotoIfFlagEnabled(Label.L1, flag=1365)
    GotoIfFlagEnabled(Label.L2, flag=1370)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableAnimations(character)
    GotoIfFlagEnabled(Label.L18, flag=1378)
    GotoIfFlagRangeAnyEnabled(Label.L17, flag_range=(1376, 1377))
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    SkipLinesIfFlagDisabled(3, 74000916)
    SkipLinesIfFlagRangeAnyEnabled(2, (1376, 1378))
    ForceAnimation(character_1, 90810, skip_transition=True, unknown2=1.0)
    EnableFlag(74000917)
    GotoIfFlagEnabled(Label.L18, flag=1378)
    GotoIfFlagRangeAnyEnabled(Label.L17, flag_range=(1376, 1377))
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    GotoIfFlagEnabled(Label.L18, flag=1378)
    SetTeamType(character_1, TeamType.HostileNPC)
    WaitFrames(frames=1)
    Move(character_1, destination=4002714, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    SetNest(character_1, region=4002714)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character_1)
    End()

    # --- Label 17 --- #
    DefineLabel(17)
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()


@RestartOnRest(14000621)
def Event_14000621(_, character: int):
    """Event 14000621"""
    GotoIfFlagEnabled(Label.L1, flag=1364)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableFlag(64001251)
    EnableFlag(14000623)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=0)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=1)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=2)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=3)
    EndOfAnimation(obj=4001251, animation_id=0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EndOfAnimation(obj=4001251, animation_id=1)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=0)
    EnableObjectActivation(4001251, obj_act_id=1400340, relative_index=1)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=2)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=3)

    # --- Label 2 --- #
    DefineLabel(2)
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4002710))
    AND_1.Add(FlagRangeAnyEnabled(flag_range=(1360, 1363)))
    AND_1.Add(FlagEnabled(1375))
    AND_2.Add(FlagEnabled(138))
    AND_2.Add(FlagEnabled(9311))
    OR_1.Add(FlagEnabled(1363))
    OR_1.Add(FlagEnabled(73500262))
    OR_1.Add(FlagEnabled(73500263))
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1364, state=FlagSetting.On)
    DisableFlag(64001251)
    DisableFlag(14000623)
    PlaySoundEffect(4001251, 400100000, sound_type=SoundType.a_Ambient)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(character)
    EnableBackread(character)
    DisableAnimations(character)
    EnableObjectActivation(4001251, obj_act_id=1400340, relative_index=1)
    ForceAnimation(4001251, 1, unknown2=1.0)
    CommonFunc_20005610(0, flag=14000623, region=4002713, region_1=4002712)
    CommonFunc_20005611(0, 14000623, 4003251, 4001251, 1400340)


@RestartOnRest(14000622)
def Event_14000622(_, character: int, character_1: int, destination: int):
    """Event 14000622"""
    if ThisEventFlagEnabled():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4002711))
    AND_1.Add(FlagEnabled(1364))
    AND_1.Add(FlagEnabled(1375))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1365, state=FlagSetting.On)
    EnableFlag(70000400)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    EnableObjectActivation(4001251, obj_act_id=1400340, relative_index=0)
    DisableObjectActivation(4001251, obj_act_id=1400340, relative_index=1)
    CommonFunc_20005610(0, flag=14000623, region=4002713, region_1=4002712)
    CommonFunc_20005611(0, 14000623, 4003251, 4001251, 1400340)


@RestartOnRest(14000624)
def Event_14000624(_, character: int):
    """Event 14000624"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(14000624):
        return
    
    MAIN.Await(CharacterDead(4000720))
    
    if FlagDisabled(1365):
        return
    if FlagEnabled(1378):
        return
    DisableNetworkConnectedFlagRange(flag_range=(1360, 1374))
    SetNetworkConnectedFlagState(flag=1370, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1375, 1379))
    SetNetworkConnectedFlagState(flag=1377, state=FlagSetting.On)
    SetTeamType(character, TeamType.HostileNPC)
    SetNest(character, region=4002714)
    AND_1.Add(CharacterHasSpecialEffect(character, 159))
    SkipLinesIfConditionFalse(2, AND_1)
    ForceAnimation(character, 0, unknown2=1.0)


@RestartOnRest(14005625)
def Event_14005625(_, region: int):
    """Event 14005625"""
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(PLAYER, 4150)
    Wait(3.0)
    Restart()


@NeverRestart(14005640)
def Event_14005640(_, character: int, obj: int, character_1: int):
    """Event 14005640"""
    GotoIfPlayerNotInOwnWorld(Label.L9)
    DisableFlag(74000190)
    SkipLinesIfFlagRangeAnyEnabled(2, (1020, 1034))
    DisableNetworkConnectedFlagRange(flag_range=(1020, 1034))
    SetNetworkConnectedFlagState(flag=1020, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1020))
    AND_1.Add(FlagEnabled(14000110))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1020, 1034))
    SetNetworkConnectedFlagState(flag=1021, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1035, 1039))
    DisableNetworkConnectedFlagRange(flag_range=(1035, 1039))
    SetNetworkConnectedFlagState(flag=1035, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1038))
    AND_2.Add(FlagEnabled(1020))
    AND_2.Add(CharacterAlive(character))
    SkipLinesIfConditionFalse(4, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1035, 1039))
    SetNetworkConnectedFlagState(flag=1035, state=FlagSetting.On)
    EnableFlag(74000190)
    EnableFlag(74000150)
    AND_3.Add(FlagEnabled(1021))
    AND_3.Add(FlagEnabled(14000110))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1035, 1039))
    SetNetworkConnectedFlagState(flag=1038, state=FlagSetting.On)
    DisableFlag(74000160)
    DisableFlag(74000170)
    DisableFlag(74000053)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableObject(obj)
    DisableGravity(character)
    DisableCharacterCollision(character)
    GotoIfFlagEnabled(Label.L0, flag=1020)
    GotoIfFlagEnabled(Label.L1, flag=1021)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    GotoIfFlagEnabled(Label.L10, flag=1038)
    Move(character, destination=4004705, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L15, flag=74000190)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 20, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 15 --- #
    DefineLabel(15)
    EnableFlag(74000170)
    SetTeamType(character, TeamType.FriendlyNPC)
    ForceAnimation(character, 700, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DropMandatoryTreasure(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    EnableObject(obj)
    End()


@NeverRestart(14005660)
def Event_14005660(_, character: int):
    """Event 14005660"""
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(2, (1175, 1179))
    DisableNetworkConnectedFlagRange(flag_range=(1175, 1179))
    SetNetworkConnectedFlagState(flag=1175, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1176))
    AND_1.Add(FlagEnabled(70000060))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1175, 1179))
    SetNetworkConnectedFlagState(flag=1175, state=FlagSetting.On)
    EnableFlag(74000200)
    AND_2.Add(FlagEnabled(1178))
    AND_2.Add(CharacterAlive(character))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1175, 1179))
    SetNetworkConnectedFlagState(flag=1176, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1160, 1174))
    DisableNetworkConnectedFlagRange(flag_range=(1160, 1174))
    SetNetworkConnectedFlagState(flag=1160, state=FlagSetting.On)
    DisableFlag(70000060)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableGravity(character)
    DisableCharacterCollision(character)
    GotoIfFlagEnabled(Label.L0, flag=1160)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L2, flag=1178)

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.FriendlyNPC)
    Move(character, destination=4004710, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, 700, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(14005661)
def Event_14005661(_, character: int):
    """Event 14005661"""
    OR_1.Add(PlayerStandingOnCollision(4004100))
    OR_1.Add(PlayerStandingOnCollision(4004101))
    OR_1.Add(PlayerStandingOnCollision(4004102))
    OR_1.Add(PlayerStandingOnCollision(4004103))
    OR_1.Add(PlayerStandingOnCollision(4004104))
    OR_1.Add(PlayerStandingOnCollision(4004109))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4002709))
    AND_1.Add(OR_1)
    AND_2.Add(not AND_1)
    AND_2.Add(HealthRatio(character) != 0.0)
    AND_2.Add(FlagEnabled(1160))
    
    MAIN.Await(AND_2)
    
    DisableCharacter(character)
    Wait(1.0)
    ClearMainCondition()
    OR_1.Add(PlayerStandingOnCollision(4004100))
    OR_1.Add(PlayerStandingOnCollision(4004101))
    OR_1.Add(PlayerStandingOnCollision(4004102))
    OR_1.Add(PlayerStandingOnCollision(4004103))
    OR_1.Add(PlayerStandingOnCollision(4004104))
    OR_1.Add(PlayerStandingOnCollision(4004109))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4002709))
    AND_1.Add(OR_1)
    AND_2.Add(AND_1)
    AND_2.Add(HealthRatio(character) != 0.0)
    AND_2.Add(FlagEnabled(1160))
    
    MAIN.Await(AND_2)
    
    EnableCharacter(4000710)
    ForceAnimation(4000710, 700, unknown2=1.0)
    Wait(1.0)
    Restart()


@NeverRestart(14005680)
def Event_14005680(_, character: int, destination: int):
    """Event 14005680"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1195, 1199))
    DisableNetworkConnectedFlagRange(flag_range=(1195, 1199))
    SetNetworkConnectedFlagState(flag=1195, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1198))
    AND_2.Add(CharacterAlive(character))
    SkipLinesIfConditionFalse(3, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1195, 1199))
    SetNetworkConnectedFlagState(flag=1196, state=FlagSetting.On)
    EnableFlag(74000251)
    SkipLinesIfFlagRangeAnyEnabled(2, (1180, 1194))
    DisableNetworkConnectedFlagRange(flag_range=(1180, 1194))
    SetNetworkConnectedFlagState(flag=1180, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1195)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000061)
    if FlagEnabled(1195):
        DisableFlag(74000251)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1180)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableGravity(character)
    DisableCharacterCollision(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    GotoIfFlagEnabled(Label.L1, flag=1196)
    GotoIfFlagEnabled(Label.L2, flag=1198)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    if FlagEnabled(74000295):
        AddSpecialEffect(character, 12605)
        End()
    if FlagEnabled(74000294):
        AddSpecialEffect(character, 12604)
        End()
    if FlagEnabled(74000293):
        AddSpecialEffect(character, 12603)
        End()
    if FlagEnabled(74000292):
        AddSpecialEffect(character, 12602)
        End()
    if FlagEnabled(74000291):
        AddSpecialEffect(character, 12601)
        End()
    if FlagEnabled(74000290):
        AddSpecialEffect(character, 12600)
        End()
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(14005681)
def Event_14005681():
    """Event 14005681"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(74000280)
    AND_1.Add(FlagRangeAllEnabled(flag_range=(70000100, 70000106)))
    AND_1.Add(FlagRangeAllEnabled(flag_range=(70000108, 70000110)))
    AND_1.Add(FlagRangeAllEnabled(flag_range=(70000112, 70000115)))
    OR_1.Add(FlagEnabled(70000107))
    OR_1.Add(FlagEnabled(70000116))
    AND_1.Add(OR_1)
    OR_2.Add(FlagEnabled(70000111))
    OR_2.Add(FlagEnabled(74000603))
    AND_1.Add(OR_2)
    if FlagEnabled(6951):
        AND_1.Add(FlagEnabled(70000120))
    if FlagEnabled(6952):
        AND_1.Add(FlagEnabled(70000121))
    
    MAIN.Await(AND_1)
    
    EnableFlag(74000280)


@NeverRestart(14005682)
def Event_14005682(_, character: int, flag: int, first_flag: int, last_flag: int):
    """Event 14005682"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(CharacterDead(character))
    
    MAIN.Await(AND_1)
    
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    if FlagDisabled(74000290):
        EnableFlag(74000290)
        Goto(Label.L20)
    if FlagDisabled(74000291):
        EnableFlag(74000291)
        Goto(Label.L20)
    if FlagDisabled(74000292):
        EnableFlag(74000292)
        Goto(Label.L20)
    if FlagDisabled(74000293):
        EnableFlag(74000293)
        Goto(Label.L20)
    if FlagDisabled(74000294):
        EnableFlag(74000294)
        Goto(Label.L20)
    if FlagDisabled(74000295):
        EnableFlag(74000295)
        Goto(Label.L20)

    # --- Label 20 --- #
    DefineLabel(20)
    SaveRequest()


@NeverRestart(14005683)
def Event_14005683(_, character: int, destination: int):
    """Event 14005683"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1615, 1619))
    DisableNetworkConnectedFlagRange(flag_range=(1615, 1619))
    SetNetworkConnectedFlagState(flag=1615, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1600, 1614))
    DisableNetworkConnectedFlagRange(flag_range=(1600, 1614))
    SetNetworkConnectedFlagState(flag=1600, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1615)

    # --- Label 9 --- #
    DefineLabel(9)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1600)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L2, flag=1618)
    DisableGravity(character)
    DisableCharacterCollision(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@NeverRestart(14005684)
def Event_14005684(_, flag: int):
    """Event 14005684"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagRangeAllEnabled(flag_range=(13300396, 13300397)))
    
    EnableFlag(flag)


@NeverRestart(14005700)
def Event_14005700(_, character: int, destination: int):
    """Event 14005700"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1215, 1219))
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1215, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1216))
    AND_1.Add(FlagEnabled(70000062))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1215, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1200, 1214))
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1200, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1215)
    AND_2.Add(FlagEnabled(1201))
    AND_2.Add(FlagEnabled(74000303))
    SkipLinesIfConditionFalse(4, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1202, state=FlagSetting.On)
    EnableFlag(70000150)
    EnableFlag(70000153)
    AND_3.Add(FlagEnabled(1202))
    AND_3.Add(FlagEnabled(74000316))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1203, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1203))
    AND_4.Add(FlagEnabled(74000306))
    SkipLinesIfConditionFalse(3, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1204, state=FlagSetting.On)
    EnableFlag(70000151)
    AND_5.Add(FlagEnabled(1204))
    AND_5.Add(FlagEnabled(74000318))
    AND_5.Add(FlagDisabled(1385))
    AND_5.Add(FlagDisabled(1366))
    SkipLinesIfConditionFalse(5, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1205, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1218, state=FlagSetting.On)
    Goto(Label.L9)
    AND_6.Add(FlagEnabled(1204))
    AND_6.Add(FlagEnabled(74000318))
    OR_1.Add(FlagEnabled(1385))
    OR_1.Add(FlagEnabled(1366))
    AND_6.Add(OR_1)
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1206, state=FlagSetting.On)
    AND_7.Add(FlagEnabled(1206))
    AND_7.Add(FlagEnabled(74000309))
    SkipLinesIfConditionFalse(6, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1200, 1214))
    SetNetworkConnectedFlagState(flag=1207, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1215, 1219))
    SetNetworkConnectedFlagState(flag=1218, state=FlagSetting.On)
    EnableFlag(70000152)
    Goto(Label.L9)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000062)
    if FlagEnabled(1215):
        DisableFlag(74000320)

    # --- Label 10 --- #
    DefineLabel(10)
    if FlagEnabled(1200):
        DisableObject(4006720)
    GotoIfFlagEnabled(Label.L0, flag=1201)
    GotoIfFlagEnabled(Label.L0, flag=1203)
    GotoIfFlagEnabled(Label.L0, flag=1206)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    GotoIfFlagEnabled(Label.L1, flag=1216)
    GotoIfFlagEnabled(Label.L2, flag=1218)
    DisableFlag(74000324)
    AND_15.Add(FlagEnabled(74000301))
    AND_15.Add(FlagDisabled(74000325))
    SkipLinesIfConditionFalse(3, AND_15)
    ForceAnimation(character, 91020, loop=True, skip_transition=True, unknown2=1.0)
    EnableFlag(74000324)
    End()
    ForceAnimation(character, 90970, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(14005701)
def Event_14005701():
    """Event 14005701"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1383))
    AND_1.Add(FlagEnabled(73500105))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1384, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1384))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1380, 1394))
    SetNetworkConnectedFlagState(flag=1385, state=FlagSetting.On)


@NeverRestart(14005720)
def Event_14005720(
    _,
    character: int,
    character_1: int,
    character_2: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
    destination: int,
    destination_1: int,
    destination_2: int,
):
    """Event 14005720"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1295, 1299))
    DisableNetworkConnectedFlagRange(flag_range=(1295, 1299))
    SetNetworkConnectedFlagState(flag=1295, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1296))
    AND_1.Add(FlagEnabled(70000066))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1295, 1299))
    SetNetworkConnectedFlagState(flag=1295, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1280, 1294))
    DisableNetworkConnectedFlagRange(flag_range=(1280, 1294))
    SetNetworkConnectedFlagState(flag=1280, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1295)
    AND_2.Add(FlagEnabled(1281))
    OR_2.Add(FlagEnabled(73101710))
    OR_2.Add(FlagEnabled(73101720))
    OR_2.Add(FlagEnabled(73101730))
    OR_2.Add(FlagEnabled(73101740))
    OR_2.Add(FlagEnabled(73101750))
    AND_2.Add(OR_2)
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1280, 1294))
    SetNetworkConnectedFlagState(flag=1282, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1282))
    AND_3.Add(FlagEnabled(74000351))
    AND_3.Add(FlagEnabled(73101710))
    AND_3.Add(FlagEnabled(73101720))
    AND_3.Add(FlagEnabled(73101730))
    AND_3.Add(FlagEnabled(73101740))
    AND_3.Add(FlagEnabled(73101750))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1280, 1294))
    SetNetworkConnectedFlagState(flag=1283, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1281))
    AND_4.Add(FlagEnabled(74000380))
    AND_4.Add(FlagDisabled(73101710))
    AND_4.Add(FlagDisabled(73101720))
    AND_4.Add(FlagDisabled(73101730))
    AND_4.Add(FlagDisabled(73101740))
    AND_4.Add(FlagDisabled(73101750))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1280, 1294))
    SetNetworkConnectedFlagState(flag=1286, state=FlagSetting.On)
    DisableFlag(70000353)
    DisableFlag(70000354)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000066)
    DisableFlag(74000352)
    DisableFlagRange((74000383, 74000392))

    # --- Label 10 --- #
    DefineLabel(10)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Move(character_1, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character_1)
    Move(character_2, destination=destination_2, destination_type=CoordEntityType.Region, copy_draw_parent=character_2)
    GotoIfFlagEnabled(Label.L1, flag=1281)
    GotoIfFlagEnabled(Label.L2, flag=1282)
    GotoIfFlagEnabled(Label.L3, flag=1283)
    GotoIfFlagEnabled(Label.L4, flag=1284)
    GotoIfFlagEnabled(Label.L5, flag=1285)
    GotoIfFlagEnabled(Label.L6, flag=1286)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    End()

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 3 --- #
    DefineLabel(3)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    GotoIfFlagEnabled(Label.L18, flag=1298)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()

    # --- Label 4 --- #
    DefineLabel(4)

    # --- Label 5 --- #
    DefineLabel(5)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    GotoIfFlagEnabled(Label.L18, flag=1298)
    if FlagDisabled(14000722):
        ForceAnimation(character_1, animation_id_1, loop=True, skip_transition=True, unknown2=1.0)
        End()
    ForceAnimation(character_1, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character_1)
    End()

    # --- Label 6 --- #
    DefineLabel(6)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L18, flag=1298)
    ForceAnimation(character_2, animation_id_2, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character_2)
    End()


@NeverRestart(14005721)
def Event_14005721():
    """Event 14005721"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(74000380):
        return
    AND_1.Add(FlagEnabled(73101610))
    AND_1.Add(FlagEnabled(73101620))
    AND_1.Add(FlagEnabled(73101630))
    AND_1.Add(FlagEnabled(73101640))
    AND_1.Add(FlagEnabled(73101650))
    AND_1.Add(FlagEnabled(73101660))
    AND_1.Add(FlagEnabled(73101670))
    AND_1.Add(FlagEnabled(73101680))
    AND_1.Add(FlagEnabled(73101690))
    AND_1.Add(FlagEnabled(73101700))
    
    MAIN.Await(AND_1)
    
    EnableFlag(74000380)


@NeverRestart(14005722)
def Event_14005722(_, entity: int, animation_id: int):
    """Event 14005722"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(14000722):
        return
    
    MAIN.Await(FlagEnabled(14000722))
    
    ForceAnimation(entity, animation_id, wait_for_completion=True, unknown2=1.0)
    EnableFlag(14005722)


@NeverRestart(14005723)
def Event_14005723(
    _,
    character: int,
    flag: int,
    flag_1: int,
    flag_2: int,
    flag_3: int,
    first_flag: int,
    last_flag: int,
    character_1: int,
    animation_id: int,
):
    """Event 14005723"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(HealthRatio(character) != 0.0)
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag_3, state=FlagSetting.On)
    EnableInvincibility(character)
    DisableAnimations(character)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    ForceAnimation(character_1, animation_id, unknown2=1.0)
    SaveRequest()
    AddSpecialEffect(character, 4640)
    Wait(5.0)
    DisableCharacter(character)
    DisableBackread(character)


@NeverRestart(14005725)
def Event_14005725():
    """Event 14005725"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(0))
    
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=0))
    GotoIfConditionTrue(Label.L20, input_condition=AND_1)
    RotateToFaceEntity(PLAYER, 0, animation=69070)
    WaitFrames(frames=1)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=0))
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 150))
    OR_1.Add(AND_2)
    OR_2.Add(FlagDisabled(0))
    OR_2.Add(FramesElapsed(frames=89))
    OR_1.Add(OR_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfFinishedConditionFalse(2, input_condition=AND_2)
    DisableFlag(0)
    Restart()
    SkipLinesIfFinishedConditionFalse(3, input_condition=OR_2)
    ForceAnimation(PLAYER, 0, unknown2=1.0)
    DisableFlag(0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    RotateToFaceEntity(PLAYER, 0, animation=0, wait_for_completion=True)
    WaitFrames(frames=1)
    EnableFlag(0)
    OR_3.Add(FlagDisabled(0))
    AND_3.Add(CharacterDoesNotHaveSpecialEffect(PLAYER, 150))
    OR_3.Add(AND_3)
    
    MAIN.Await(OR_3)
    
    SkipLinesIfFinishedConditionFalse(3, input_condition=AND_3)
    DisableFlag(0)
    DisableFlag(0)
    Restart()
    DisableFlag(0)
    ForceAnimation(PLAYER, 0, wait_for_completion=True, unknown2=1.0)
    Restart()


@NeverRestart(14005740)
def Event_14005740(_, character: int, command_id: int, destination: int):
    """Event 14005740"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1075, 1079))
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1075, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1076))
    AND_1.Add(FlagEnabled(70000055))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1075, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1060, 1074))
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1060, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1075)
    AND_2.Add(FlagEnabled(1060))
    AND_2.Add(FlagEnabled(73100152))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1061, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1061))
    AND_3.Add(PlayerRemainingYoelLevelComparison(comparison_type=ComparisonType.LessThanOrEqual, value=0))
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1062, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1078, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1061))
    AND_4.Add(FlagEnabled(138))
    SkipLinesIfConditionFalse(4, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1064, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1078, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1060))
    AND_5.Add(FlagEnabled(138))
    SkipLinesIfConditionFalse(4, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1060, 1074))
    SetNetworkConnectedFlagState(flag=1063, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1075, 1079))
    SetNetworkConnectedFlagState(flag=1078, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000055)
    DisableFlagRange((74000430, 74000433))

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1061)
    GotoIfFlagEnabled(Label.L2, flag=1062)
    GotoIfFlagEnabled(Label.L2, flag=1064)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    GotoIfFlagEnabled(Label.L1, flag=1078)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EzstateAIRequest(character, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(14005750)
def Event_14005750(_, character: int, animation_id: int, destination: int):
    """Event 14005750"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1155, 1159))
    DisableNetworkConnectedFlagRange(flag_range=(1155, 1159))
    SetNetworkConnectedFlagState(flag=1155, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1156))
    AND_1.Add(FlagEnabled(70000059))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1155, 1159))
    SetNetworkConnectedFlagState(flag=1155, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1140, 1154))
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1140, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1155)
    AND_2.Add(FlagEnabled(1140))
    OR_2.Add(FlagEnabled(13000005))
    OR_2.Add(FlagEnabled(9301))
    AND_2.Add(OR_2)
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1141, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1141))
    AND_3.Add(FlagEnabled(74000850))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1142, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1142))
    AND_4.Add(PlayerHasGood(373))
    OR_4.Add(FlagEnabled(13100002))
    OR_4.Add(FlagEnabled(9303))
    AND_4.Add(OR_4)
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1143, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1143))
    AND_5.Add(FlagEnabled(74000851))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1144, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1144))
    AND_6.Add(FlagEnabled(13000380))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1140, 1154))
    SetNetworkConnectedFlagState(flag=1145, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000059)
    if FlagEnabled(1155):
        DisableFlag(74000870)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1141)
    GotoIfFlagEnabled(Label.L0, flag=1143)
    GotoIfFlagEnabled(Label.L0, flag=1145)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    GotoIfFlagEnabled(Label.L16, flag=1156)
    GotoIfFlagEnabled(Label.L18, flag=1158)
    ForceAnimation(character, animation_id, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(14005760)
def Event_14005760(_, character: int, obj: int):
    """Event 14005760"""
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(2, (1255, 1259))
    DisableNetworkConnectedFlagRange(flag_range=(1255, 1259))
    SetNetworkConnectedFlagState(flag=1255, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1256))
    AND_1.Add(FlagEnabled(70000064))
    SkipLinesIfConditionFalse(3, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1255, 1259))
    SetNetworkConnectedFlagState(flag=1255, state=FlagSetting.On)
    DisableFlag(74000460)
    SkipLinesIfFlagRangeAnyEnabled(2, (1240, 1254))
    DisableNetworkConnectedFlagRange(flag_range=(1240, 1254))
    SetNetworkConnectedFlagState(flag=1240, state=FlagSetting.On)
    DisableFlag(70000064)

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagEnabled(Label.L0, flag=1241)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=4004735, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    GotoIfFlagEnabled(Label.L10, flag=1256)
    GotoIfFlagEnabled(Label.L11, flag=1258)
    ForceAnimation(character, 90450, unknown2=1.0)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 11 --- #
    DefineLabel(11)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()


@NeverRestart(14005780)
def Event_14005780(_, character: int, animation_id: int, obj: int, destination: int):
    """Event 14005780"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1275, 1279))
    DisableNetworkConnectedFlagRange(flag_range=(1275, 1279))
    SetNetworkConnectedFlagState(flag=1275, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1276))
    AND_1.Add(FlagEnabled(70000065))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1275, 1279))
    SetNetworkConnectedFlagState(flag=1275, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1260, 1274))
    DisableNetworkConnectedFlagRange(flag_range=(1260, 1274))
    SetNetworkConnectedFlagState(flag=1260, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1275)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000065)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1261)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    GotoIfFlagEnabled(Label.L1, flag=1278)
    ForceAnimation(character, animation_id, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    WaitFrames(frames=1)
    DropMandatoryTreasure(character)
    End()


@RestartOnRest(14005781)
def Event_14005781():
    """Event 14005781"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(74000531):
        return
    OR_1.Add(FlagEnabled(73901140))
    OR_1.Add(FlagEnabled(73901150))
    OR_1.Add(FlagEnabled(73901160))
    OR_1.Add(FlagEnabled(73901170))
    OR_1.Add(FlagEnabled(73901180))
    
    MAIN.Await(OR_1)
    
    EnableFlag(74000531)


@RestartOnRest(14005782)
def Event_14005782():
    """Event 14005782"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73901140))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73901150))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73901160))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73901170))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, 73901180))
    
    MAIN.Await(OR_1)
    
    EnableFlag(74000532)
    Restart()


@NeverRestart(14005900)
def Event_14005900():
    """Event 14005900"""
    DisableNetworkSync()
    if CharacterOutsideRegion(character=PLAYER, region=4002901):
        return
    Move(PLAYER, destination=4002900, destination_type=CoordEntityType.Region, copy_draw_parent=PLAYER)
