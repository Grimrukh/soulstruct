"""
Farron Keep / Road of Sacrifices

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


@ContinueOnRest(0)
def Constructor():
    """Event 0"""
    RegisterBonfire(bonfire_flag=13300000, obj=3301950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13300003, obj=3301953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13300004, obj=3301954, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13300005, obj=3301955, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13300006, obj=3301956, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13300007, obj=3301957, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13300007, obj=3301958, reaction_distance=5.0)
    CommonFunc_20005500(0, flag=13300800, bonfire_flag=13300001, character=3300951, obj=3301951)
    CommonFunc_20005500(0, flag=13300850, bonfire_flag=13300002, character=3300952, obj=3301952)
    Event_13305100()
    Event_13300110()
    Event_13305201()
    Event_13305209()
    CommonFunc_20005120(0, character=3300210, radius=45.0)
    CommonFunc_20005120(0, character=3300211, radius=40.0)
    CommonFunc_20005120(0, character=3300212, radius=35.0)
    Event_13305202(
        0,
        character=3300200,
        destination=3302270,
        destination_1=3302271,
        first_flag=13304200,
        last_flag=13304201,
        first_flag_1=13304200,
        last_flag_1=13304201,
    )
    Event_13305202(
        1,
        character=3300201,
        destination=3302272,
        destination_1=3302273,
        first_flag=13304202,
        last_flag=13304203,
        first_flag_1=13304202,
        last_flag_1=13304203,
    )
    CommonFunc_20005350(0, character=3300200, item_lot=22700020, flag=53300990)
    CommonFunc_20005220(0, character=3300230, animation_id=700, animation_id_1=1700)
    CommonFunc_20005210(0, character=3300231, animation_id=700, animation_id_1=1700, radius=1.0)
    CommonFunc_20005210(0, character=3300232, animation_id=700, animation_id_1=1700, radius=4.0)
    CommonFunc_20005210(0, character=3300233, animation_id=700, animation_id_1=1700, radius=4.0)
    CommonFunc_20005220(0, character=3300234, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=3300235, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=3300236, animation_id=700, animation_id_1=1700)
    CommonFunc_20005210(0, character=3300250, animation_id=703, animation_id_1=1703, radius=4.0)
    CommonFunc_20005210(0, character=3300252, animation_id=701, animation_id_1=1701, radius=4.0)
    CommonFunc_20005201(0, character=3300256, animation_id=700, animation_id_1=1700, region=3302283, seconds=1.0)
    CommonFunc_20005201(0, character=3300257, animation_id=701, animation_id_1=1701, region=3302283, seconds=4.0)
    CommonFunc_20005210(0, character=3300258, animation_id=701, animation_id_1=1701, radius=3.0)
    CommonFunc_20005200(0, character=3300261, animation_id=700, animation_id_1=1700, region=3302283)
    CommonFunc_20005210(0, character=3300262, animation_id=701, animation_id_1=1701, radius=6.0)
    CommonFunc_20005221(0, character=3300277, animation_id=701, animation_id_1=1701, radius=12.0)
    CommonFunc_20005221(0, character=3300278, animation_id=701, animation_id_1=1701, radius=12.0)
    CommonFunc_20005221(0, character=3300281, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005200(0, character=3300285, animation_id=703, animation_id_1=1703, region=3302241)
    CommonFunc_20005200(0, character=3300286, animation_id=701, animation_id_1=1701, region=3302241)
    CommonFunc_20005119(
        0,
        character=3300309,
        region=3302210,
        region_1=3302214,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005260(0, character=3300312, animation_id=705, animation_id_1=1705, character_1=3300330)
    CommonFunc_20005260(0, character=3300313, animation_id=703, animation_id_1=1703, character_1=3300330)
    CommonFunc_20005132(0, character=3300332, radius=3.0, region=3302223)
    CommonFunc_20005132(0, character=3300333, radius=5.0, region=3302231)
    CommonFunc_20005110(0, character=3300340, region=3302280)
    Event_13305230()
    CommonFunc_20005120(0, character=3300350, radius=3.0)
    CommonFunc_20005120(0, character=3300351, radius=3.0)
    CommonFunc_20005110(0, character=3300398, region=3302298)
    CommonFunc_20005120(0, character=3300175, radius=10.0)
    CommonFunc_20005132(0, character=3300176, radius=5.0, region=3302298)
    CommonFunc_20005132(0, character=3300177, radius=5.0, region=3302260)
    CommonFunc_20005132(0, character=3300178, radius=5.0, region=3302260)
    CommonFunc_20005220(0, character=3300400, animation_id=701, animation_id_1=1701)
    CommonFunc_20005132(0, character=3300401, radius=3.0, region=3302302)
    CommonFunc_20005220(0, character=3300402, animation_id=701, animation_id_1=1701)
    CommonFunc_20005201(
        0,
        character=3300405,
        animation_id=701,
        animation_id_1=1701,
        region=3302301,
        seconds=0.30000001192092896,
    )
    CommonFunc_20005201(
        0,
        character=3300406,
        animation_id=701,
        animation_id_1=1701,
        region=3302301,
        seconds=0.699999988079071,
    )
    CommonFunc_20005110(0, character=3300407, region=3302301)
    CommonFunc_20005210(0, character=3300408, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005221(0, character=3300411, animation_id=701, animation_id_1=1701, radius=10.0)
    CommonFunc_20005221(0, character=3300412, animation_id=701, animation_id_1=1701, radius=8.0)
    CommonFunc_20005220(0, character=3300421, animation_id=701, animation_id_1=1701)
    CommonFunc_20005220(0, character=3300422, animation_id=701, animation_id_1=1701)
    CommonFunc_20005220(0, character=3300423, animation_id=701, animation_id_1=1701)
    CommonFunc_20005220(0, character=3300426, animation_id=701, animation_id_1=1701)
    CommonFunc_20005210(0, character=3300427, animation_id=701, animation_id_1=1701, radius=2.0)
    CommonFunc_20005210(0, character=3300428, animation_id=701, animation_id_1=1701, radius=2.0)
    CommonFunc_20005210(0, character=3300435, animation_id=701, animation_id_1=1701, radius=4.0)
    CommonFunc_20005220(0, character=3300440, animation_id=700, animation_id_1=1700)
    CommonFunc_20005240(0, character=3300441, animation_id=700, animation_id_1=1700, special_effect=12140)
    CommonFunc_20005240(0, character=3300442, animation_id=700, animation_id_1=1700, special_effect=12140)
    CommonFunc_20005240(0, character=3300443, animation_id=700, animation_id_1=1700, special_effect=12140)
    CommonFunc_20005240(0, character=3300444, animation_id=702, animation_id_1=1702, special_effect=12140)
    CommonFunc_20005240(0, character=3300448, animation_id=702, animation_id_1=1702, special_effect=12140)
    CommonFunc_20005240(0, character=3300449, animation_id=702, animation_id_1=1702, special_effect=12140)
    CommonFunc_20005240(0, character=3300440, animation_id=702, animation_id_1=1702, special_effect=12140)
    CommonFunc_20005240(0, character=3300453, animation_id=701, animation_id_1=1701, special_effect=12140)
    CommonFunc_20005240(0, character=3300456, animation_id=700, animation_id_1=1700, special_effect=12140)
    CommonFunc_20005240(0, character=3300459, animation_id=700, animation_id_1=1700, special_effect=12140)
    CommonFunc_20005240(0, character=3300460, animation_id=701, animation_id_1=1701, special_effect=12140)
    CommonFunc_20005240(0, character=3300467, animation_id=702, animation_id_1=1702, special_effect=12140)
    CommonFunc_20005240(0, character=3300468, animation_id=701, animation_id_1=1701, special_effect=12140)
    CommonFunc_20005220(0, character=3300477, animation_id=700, animation_id_1=1700)
    CommonFunc_20005240(0, character=3300482, animation_id=701, animation_id_1=1701, special_effect=12141)
    Event_13305210()
    Event_13305211(
        0,
        character=3300477,
        character_1=3300479,
        special_effect=12142,
        special_effect_id=12141,
        ai_param_id=221002,
    )
    Event_13305211(
        1,
        character=3300477,
        character_1=3305477,
        special_effect=12144,
        special_effect_id=12141,
        ai_param_id=221002,
    )
    Event_13305211(
        2,
        character=3300477,
        character_1=3305478,
        special_effect=12144,
        special_effect_id=12141,
        ai_param_id=221012,
    )
    Event_13305211(
        3,
        character=3300484,
        character_1=3305484,
        special_effect=12144,
        special_effect_id=12141,
        ai_param_id=221002,
    )
    Event_13305211(
        4,
        character=3300484,
        character_1=3305485,
        special_effect=12144,
        special_effect_id=12141,
        ai_param_id=221012,
    )
    CommonFunc_20005350(0, character=3300494, item_lot=31200110, flag=53300995)
    CommonFunc_20005350(0, character=3300495, item_lot=31200210, flag=53300996)
    CommonFunc_20005110(0, character=3300500, region=3302350)
    CommonFunc_20005110(0, character=3300501, region=3302350)
    CommonFunc_20005110(0, character=3300502, region=3302350)
    CommonFunc_20005110(0, character=3300503, region=3302350)
    CommonFunc_20005110(0, character=3300504, region=3302350)
    CommonFunc_20005110(0, character=3300505, region=3302350)
    CommonFunc_20005110(0, character=3300506, region=3302350)
    CommonFunc_20005110(0, character=3300507, region=3302350)
    CommonFunc_20005211(0, character=3300508, animation_id=701, animation_id_1=1701, radius=5.0, seconds=0.0)
    CommonFunc_20005350(0, character=3300510, item_lot=22702010, flag=53300991)
    CommonFunc_20005110(0, character=3300580, region=3302240)
    CommonFunc_20005110(0, character=3300391, region=3302281)
    CommonFunc_20005110(0, character=3300397, region=3302290)
    CommonFunc_20005110(0, character=3300398, region=3302380)
    CommonFunc_20005110(0, character=3300399, region=3302380)
    CommonFunc_20005410(0, character=3300309, animation_id=3005)
    CommonFunc_20005411(
        0,
        character=3300309,
        character_1=3300302,
        animation_id=704,
        animation_id_1=1704,
        seconds=1.2999999523162842,
    )
    CommonFunc_20005411(
        0,
        character=3300309,
        character_1=3300303,
        animation_id=705,
        animation_id_1=1705,
        seconds=1.399999976158142,
    )
    CommonFunc_20005411(0, character=3300309, character_1=3300304, animation_id=705, animation_id_1=1705, seconds=1.0)
    CommonFunc_20005411(
        0,
        character=3300309,
        character_1=3300305,
        animation_id=703,
        animation_id_1=1703,
        seconds=0.800000011920929,
    )
    CommonFunc_20005411(
        0,
        character=3300309,
        character_1=3300306,
        animation_id=703,
        animation_id_1=1703,
        seconds=0.30000001192092896,
    )
    CommonFunc_20005411(0, character=3300309, character_1=3300307, animation_id=706, animation_id_1=1706, seconds=0.0)
    CommonFunc_20005410(0, character=3300556, animation_id=3005)
    CommonFunc_20005411(0, character=3300556, character_1=3300551, animation_id=705, animation_id_1=1705, seconds=0.0)
    CommonFunc_20005411(0, character=3300556, character_1=3300552, animation_id=703, animation_id_1=1703, seconds=0.5)
    CommonFunc_20005411(
        0,
        character=3300556,
        character_1=3300555,
        animation_id=706,
        animation_id_1=1706,
        seconds=0.20000000298023224,
    )
    CommonFunc_20005214(0, character=3300550, animation_id=704, animation_id_1=1704, radius=2.0)
    CommonFunc_20005132(0, character=3300553, radius=4.0, region=3302340)
    CommonFunc_20005132(0, character=3300554, radius=3.0, region=3302340)
    CommonFunc_20005132(0, character=3300556, radius=3.0, region=3302340)
    Event_13305320(0, character=3300551)
    Event_13305320(1, character=3300552)
    Event_13305320(2, character=3300554)
    CommonFunc_20005132(0, character=3300372, radius=5.0, region=3302310)
    CommonFunc_20005132(0, character=3300373, radius=5.0, region=3302310)
    CommonFunc_20005210(0, character=3300384, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005341(0, flag=13300384, character=3300384, item_lot=31000000)
    CommonFunc_20005341(0, flag=13300385, character=3300385, item_lot=21502030)
    CommonFunc_20005341(0, flag=13300386, character=3300386, item_lot=21502040)
    CommonFunc_20005341(0, flag=13300387, character=3300387, item_lot=21502050)
    CommonFunc_20005341(0, flag=13300388, character=3300388, item_lot=21502060)
    CommonFunc_20005341(0, flag=13300389, character=3300389, item_lot=21502000)
    CommonFunc_20005341(0, flag=13300390, character=3300390, item_lot=21502010)
    CommonFunc_20005341(0, flag=13300391, character=3300391, item_lot=21502020)
    Event_13305300()
    CommonFunc_20005900(0, flag=13100900, flag_1=13300560)
    CommonFunc_20005341(0, flag=13300560, character=3300560, item_lot=52000000)
    CommonFunc_20005434(0, character=3300560, character_1=3300561)
    Event_13300310()
    CommonFunc_20005342(0, flag=13300395, character=3300172)
    CommonFunc_20005342(0, flag=13300396, character=3300177)
    CommonFunc_20005342(0, flag=13300397, character=3300178)
    Event_13305800()
    Event_13305810()
    Event_13305811()
    Event_13305812()
    Event_13305814()
    Event_13305829()
    CommonFunc_20005840(0, other_entity=3301800)
    CommonFunc_20005841(0, other_entity=3301800)
    Event_13305860()
    Event_13305850()
    Event_13305900()
    Event_13305861()
    Event_13305862()
    Event_13305863(0, character=3300850, flag=13305891, flag_1=13305892, flag_2=13305893)
    Event_13305870(
        0,
        flag=13304870,
        character=3300850,
        destination=3302876,
        flag_1=13305880,
        source_entity=3302878,
        source_entity_1=3302879,
        source_entity_2=3302880,
    )
    Event_13305870(
        1,
        flag=13304871,
        character=3300850,
        destination=3302871,
        flag_1=13305880,
        source_entity=3302876,
        source_entity_1=3302880,
        source_entity_2=3302879,
    )
    Event_13305870(
        2,
        flag=13304872,
        character=3300850,
        destination=3302874,
        flag_1=13305880,
        source_entity=3302870,
        source_entity_1=3302876,
        source_entity_2=3302875,
    )
    Event_13305870(
        3,
        flag=13304873,
        character=3300850,
        destination=3302874,
        flag_1=13305880,
        source_entity=3302880,
        source_entity_1=3302878,
        source_entity_2=3302872,
    )
    Event_13305870(
        4,
        flag=13304874,
        character=3300850,
        destination=3302873,
        flag_1=13305880,
        source_entity=3302874,
        source_entity_1=3302880,
        source_entity_2=3302876,
    )
    Event_13305870(
        5,
        flag=13304875,
        character=3300850,
        destination=3302877,
        flag_1=13305880,
        source_entity=3302874,
        source_entity_1=3302871,
        source_entity_2=3302881,
    )
    Event_13305870(
        6,
        flag=13304876,
        character=3300850,
        destination=3302872,
        flag_1=13305880,
        source_entity=3302877,
        source_entity_1=3302879,
        source_entity_2=3302874,
    )
    Event_13305870(
        7,
        flag=13304877,
        character=3300850,
        destination=3302875,
        flag_1=13305880,
        source_entity=3302873,
        source_entity_1=3302880,
        source_entity_2=3302878,
    )
    Event_13305870(
        8,
        flag=13304878,
        character=3300850,
        destination=3302873,
        flag_1=13305880,
        source_entity=3302881,
        source_entity_1=3302872,
        source_entity_2=3302879,
    )
    Event_13305870(
        9,
        flag=13304879,
        character=3300850,
        destination=3302870,
        flag_1=13305880,
        source_entity=3302879,
        source_entity_1=3302878,
        source_entity_2=3302871,
    )
    Event_13305870(
        10,
        flag=13304880,
        character=3300850,
        destination=3302875,
        flag_1=13305880,
        source_entity=3302876,
        source_entity_1=3302872,
        source_entity_2=3302878,
    )
    Event_13305870(
        11,
        flag=13304881,
        character=3300850,
        destination=3302876,
        flag_1=13305880,
        source_entity=3302870,
        source_entity_1=3302879,
        source_entity_2=3302872,
    )
    Event_13305870(
        12,
        flag=13304882,
        character=3300850,
        destination=3302872,
        flag_1=13305880,
        source_entity=3302878,
        source_entity_1=3302880,
        source_entity_2=3302879,
    )
    Event_13305870(
        13,
        flag=13304883,
        character=3300850,
        destination=3302871,
        flag_1=13305880,
        source_entity=3302877,
        source_entity_1=3302875,
        source_entity_2=3302870,
    )
    Event_13305870(
        14,
        flag=13304884,
        character=3300850,
        destination=3302877,
        flag_1=13305880,
        source_entity=3302876,
        source_entity_1=3302875,
        source_entity_2=3302874,
    )
    Event_13305864(0, flag=13305880, character=3300850)
    Event_13305885(
        0,
        flag=13304870,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302876,
        source_entity_1=3302878,
        source_entity_2=3302879,
        destination=3302880,
        flag_1=13305890,
        source_entity_3=3302875,
        source_entity_4=3302881,
        source_entity_5=3302872,
        source_entity_6=3302877,
        source_entity_7=3302873,
        source_entity_8=3302871,
        source_entity_9=3302870,
    )
    Event_13305885(
        1,
        flag=13304871,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302871,
        source_entity_1=3302876,
        source_entity_2=3302880,
        destination=3302879,
        flag_1=13305890,
        source_entity_3=3302870,
        source_entity_4=3302873,
        source_entity_5=3302872,
        source_entity_6=3302874,
        source_entity_7=3302875,
        source_entity_8=3302877,
        source_entity_9=3302878,
    )
    Event_13305885(
        2,
        flag=13304872,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302874,
        source_entity_1=3302870,
        source_entity_2=3302876,
        destination=3302875,
        flag_1=13305890,
        source_entity_3=3302881,
        source_entity_4=3302871,
        source_entity_5=3302872,
        source_entity_6=3302873,
        source_entity_7=3302877,
        source_entity_8=3302878,
        source_entity_9=3302879,
    )
    Event_13305885(
        3,
        flag=13304873,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302874,
        source_entity_1=3302880,
        source_entity_2=3302878,
        destination=3302872,
        flag_1=13305890,
        source_entity_3=3302879,
        source_entity_4=3302881,
        source_entity_5=3302870,
        source_entity_6=3302871,
        source_entity_7=3302873,
        source_entity_8=3302875,
        source_entity_9=3302876,
    )
    Event_13305885(
        4,
        flag=13304874,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302873,
        source_entity_1=3302874,
        source_entity_2=3302880,
        destination=3302876,
        flag_1=13305890,
        source_entity_3=3302878,
        source_entity_4=3302879,
        source_entity_5=3302881,
        source_entity_6=3302870,
        source_entity_7=3302871,
        source_entity_8=3302872,
        source_entity_9=3302875,
    )
    Event_13305885(
        5,
        flag=13304875,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302877,
        source_entity_1=3302874,
        source_entity_2=3302871,
        destination=3302881,
        flag_1=13305890,
        source_entity_3=3302876,
        source_entity_4=3302878,
        source_entity_5=3302879,
        source_entity_6=3302880,
        source_entity_7=3302870,
        source_entity_8=3302872,
        source_entity_9=3302873,
    )
    Event_13305885(
        6,
        flag=13304876,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302872,
        source_entity_1=3302877,
        source_entity_2=3302879,
        destination=3302874,
        flag_1=13305890,
        source_entity_3=3302875,
        source_entity_4=3302876,
        source_entity_5=3302878,
        source_entity_6=3302880,
        source_entity_7=3302881,
        source_entity_8=3302870,
        source_entity_9=3302871,
    )
    Event_13305885(
        7,
        flag=13304877,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302875,
        source_entity_1=3302873,
        source_entity_2=3302880,
        destination=3302878,
        flag_1=13305890,
        source_entity_3=3302872,
        source_entity_4=3302874,
        source_entity_5=3302876,
        source_entity_6=3302877,
        source_entity_7=3302879,
        source_entity_8=3302881,
        source_entity_9=3302870,
    )
    Event_13305885(
        8,
        flag=13304878,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302873,
        source_entity_1=3302881,
        source_entity_2=3302872,
        destination=3302879,
        flag_1=13305890,
        source_entity_3=3302871,
        source_entity_4=3302874,
        source_entity_5=3302875,
        source_entity_6=3302876,
        source_entity_7=3302877,
        source_entity_8=3302878,
        source_entity_9=3302880,
    )
    Event_13305885(
        9,
        flag=13304879,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302870,
        source_entity_1=3302879,
        source_entity_2=3302878,
        destination=3302871,
        flag_1=13305890,
        source_entity_3=3302872,
        source_entity_4=3302873,
        source_entity_5=3302874,
        source_entity_6=3302875,
        source_entity_7=3302876,
        source_entity_8=3302877,
        source_entity_9=3302880,
    )
    Event_13305885(
        10,
        flag=13304880,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302875,
        source_entity_1=3302876,
        source_entity_2=3302872,
        destination=3302878,
        flag_1=13305890,
        source_entity_3=3302881,
        source_entity_4=3302870,
        source_entity_5=3302871,
        source_entity_6=3302873,
        source_entity_7=3302874,
        source_entity_8=3302877,
        source_entity_9=3302879,
    )
    Event_13305885(
        11,
        flag=13304881,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302876,
        source_entity_1=3302870,
        source_entity_2=3302879,
        destination=3302872,
        flag_1=13305890,
        source_entity_3=3302880,
        source_entity_4=3302881,
        source_entity_5=3302871,
        source_entity_6=3302873,
        source_entity_7=3302874,
        source_entity_8=3302875,
        source_entity_9=3302877,
    )
    Event_13305885(
        12,
        flag=13304882,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302872,
        source_entity_1=3302878,
        source_entity_2=3302880,
        destination=3302879,
        flag_1=13305890,
        source_entity_3=3302876,
        source_entity_4=3302877,
        source_entity_5=3302881,
        source_entity_6=3302870,
        source_entity_7=3302871,
        source_entity_8=3302873,
        source_entity_9=3302874,
    )
    Event_13305885(
        13,
        flag=13304883,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302871,
        source_entity_1=3302877,
        source_entity_2=3302875,
        destination=3302870,
        flag_1=13305890,
        source_entity_3=3302878,
        source_entity_4=3302879,
        source_entity_5=3302880,
        source_entity_6=3302881,
        source_entity_7=3302872,
        source_entity_8=3302873,
        source_entity_9=3302874,
    )
    Event_13305885(
        14,
        flag=13304884,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        source_entity=3302877,
        source_entity_1=3302876,
        source_entity_2=3302875,
        destination=3302874,
        flag_1=13305890,
        source_entity_3=3302873,
        source_entity_4=3302875,
        source_entity_5=3302878,
        source_entity_6=3302879,
        source_entity_7=3302880,
        source_entity_8=3302870,
        source_entity_9=3302871,
    )
    Event_13305865(
        0,
        flag=13305890,
        character=3300850,
        character_1=3300851,
        character_2=3300852,
        character_3=3300853,
        flag_1=13305891,
        flag_2=13305892,
        flag_3=13305893,
        flag_4=13305894,
        flag_5=13305895,
        flag_6=13305896,
    )
    Event_13305866(0, character=3300851, character_1=3300850, flag=13305894, flag_1=13305891)
    Event_13305866(1, character=3300852, character_1=3300850, flag=13305895, flag_1=13305892)
    Event_13305866(2, character=3300853, character_1=3300850, flag=13305896, flag_1=13305893)
    CommonFunc_20005840(0, other_entity=3301850)
    CommonFunc_20005841(0, other_entity=3301850)
    Event_13305410(0, flag=13300410, flag_1=9410, value=3, obj=3301410)
    Event_13300412(
        0,
        flag=13300410,
        flag_1=9412,
        destination=3301412,
        obj=3301416,
        vfx_id=3303412,
        vfx_id_1=3303416,
        vfx_id_2=3303422,
        cutscene_id=33000020,
        cutscene_id_1=33000030,
        cutscene_id_2=33000040,
        cutscene_id_3=0,
    )
    Event_13300412(
        1,
        flag=13300410,
        flag_1=9413,
        destination=3301413,
        obj=3301417,
        vfx_id=3303413,
        vfx_id_1=3303417,
        vfx_id_2=3303423,
        cutscene_id=33000021,
        cutscene_id_1=33000031,
        cutscene_id_2=33000041,
        cutscene_id_3=0,
    )
    Event_13300412(
        2,
        flag=13300410,
        flag_1=9414,
        destination=3301414,
        obj=3301418,
        vfx_id=3303414,
        vfx_id_1=3303418,
        vfx_id_2=3303424,
        cutscene_id=33000022,
        cutscene_id_1=33000032,
        cutscene_id_2=33000042,
        cutscene_id_3=0,
    )
    Event_13300412(
        3,
        flag=13300410,
        flag_1=9415,
        destination=3301415,
        obj=3301419,
        vfx_id=3303415,
        vfx_id_1=3303419,
        vfx_id_2=3303425,
        cutscene_id=33000023,
        cutscene_id_1=33000033,
        cutscene_id_2=33000043,
        cutscene_id_3=0,
    )
    Event_13305421()
    CommonFunc_20005510(
        0,
        flag=13300580,
        obj=3301580,
        message=61330000,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305580,
    )
    CommonFunc_20005510(
        0,
        flag=13300581,
        obj=3301581,
        message=61330005,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305581,
    )
    CommonFunc_20005510(
        0,
        flag=13300582,
        obj=3301582,
        message=61330010,
        action_button_id=9410,
        action_button_id_1=9411,
        flag_1=13305582,
    )
    CommonFunc_20005510(
        0,
        flag=13300583,
        obj=3301583,
        message=61330015,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305583,
    )
    CommonFunc_20005510(
        0,
        flag=13300584,
        obj=3301584,
        message=61330020,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305584,
    )
    CommonFunc_20005510(
        0,
        flag=13300585,
        obj=3301585,
        message=61330025,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305585,
    )
    CommonFunc_20005510(
        0,
        flag=13300586,
        obj=3301586,
        message=61330030,
        action_button_id=9410,
        action_button_id_1=9411,
        flag_1=13305586,
    )
    CommonFunc_20005510(
        0,
        flag=13300587,
        obj=3301587,
        message=61330035,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305587,
    )
    CommonFunc_20005510(
        0,
        flag=13300588,
        obj=3301588,
        message=61330040,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305588,
    )
    CommonFunc_20005510(
        0,
        flag=13300589,
        obj=3301589,
        message=61330045,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305589,
    )
    CommonFunc_20005510(
        0,
        flag=13300590,
        obj=3301590,
        message=61330050,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305590,
    )
    CommonFunc_20005510(
        0,
        flag=13300591,
        obj=3301591,
        message=61330055,
        action_button_id=9410,
        action_button_id_1=9411,
        flag_1=13305591,
    )
    CommonFunc_20005510(
        0,
        flag=13300592,
        obj=3301592,
        message=61330060,
        action_button_id=9400,
        action_button_id_1=9401,
        flag_1=13305592,
    )
    CommonFunc_20005520(0, flag=13300604, obj=3301304, obj_act_id=3304304)
    Event_13305471()
    CommonFunc_20005523(0, obj=3301310, completion_count=1)
    CommonFunc_20005523(0, obj=3301311, completion_count=1)
    CommonFunc_20005523(0, obj=3301312, completion_count=1)
    CommonFunc_20005523(0, obj=3301313, completion_count=2)
    CommonFunc_20005523(0, obj=3301314, completion_count=2)
    CommonFunc_20005525(0, flag=53300950, item_lot=3300950, obj=3301320, model_point=62)
    CommonFunc_20005525(0, flag=53300960, item_lot=3300960, obj=3301321, model_point=60)
    CommonFunc_20005525(0, flag=53300970, item_lot=3300970, obj=3301322, model_point=60)
    CommonFunc_20005525(0, flag=53300980, item_lot=3300980, obj=3301323, model_point=62)
    CommonFunc_20005524(0, obj=3301330, flag=9481)
    CommonFunc_20005610(0, flag=63300432, region=3302432, region_1=3302433)
    CommonFunc_20005611(0, flag=63300432, obj_act_id=3303432, obj=3301432, obj_act_id_1=332100)
    CommonFunc_20005620(0, flag=13300405, flag_1=13301405, entity=3301405, obj=3301406, obj_1=3301407, flag_2=13301406)
    Event_13305409()
    CommonFunc_20005650(0, flag=13300440, obj=3301440)
    Event_13305470()
    CommonFunc_20005781(0, obj=3301570, model_point=4, flag=13305161)
    CommonFunc_20005541(
        0,
        obj_flag=13305560,
        obj=3301510,
        model_point=200,
        behavior_param_id=5400,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
        model_point_1=800061,
        vfx_id=200,
    )
    CommonFunc_20005541(
        0,
        obj_flag=13305561,
        obj=3301511,
        model_point=200,
        behavior_param_id=5400,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
        model_point_1=800061,
        vfx_id=200,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305562,
        obj=3301520,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305563,
        obj=3301521,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305564,
        obj=3301522,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305565,
        obj=3301523,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305566,
        obj=3301524,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305567,
        obj=3301526,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305568,
        obj=3301527,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305570,
        obj=3301530,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305571,
        obj=3301531,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305572,
        obj=3301532,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305573,
        obj=3301533,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305574,
        obj=3301534,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305575,
        obj=3301535,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305576,
        obj=3301536,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305577,
        obj=3301537,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13305578,
        obj=3301538,
        model_point=200,
        behavior_param_id=5410,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    Event_13305480()
    Event_13305170()
    Event_13305171()
    Event_13305172()
    Event_13305173()
    Event_13305174()
    Event_13305175()
    Event_13305176()
    Event_13305177()
    Event_13305360()
    Event_13305361()
    Event_13305362()
    CommonFunc_20005701(
        0,
        left=13300850,
        summon_flag=13304192,
        dismissal_flag=13305192,
        character=3300192,
        region=3302192,
        left_1=70000017,
    )
    CommonFunc_20005720(0, flag=13304192, flag_1=13305192, flag_2=13300850, character=3300192)
    CommonFunc_20005711(
        0,
        flag=13304192,
        flag_1=13305855,
        character=3300192,
        region=3302850,
        region_1=3302855,
        flag_2=13300852,
    )
    CommonFunc_20005714(0, flag=13304192, flag_1=13305855, character=3300192, region=3302856, flag_2=13300852)
    CommonFunc_20005701(
        0,
        left=13300800,
        summon_flag=13304913,
        dismissal_flag=13305193,
        character=3300193,
        region=3302193,
        left_1=0,
    )
    CommonFunc_20005720(0, flag=13304913, flag_1=13305193, flag_2=13300800, character=3300193)
    CommonFunc_20005711(
        0,
        flag=13304913,
        flag_1=13305805,
        character=3300193,
        region=3302800,
        region_1=3302805,
        flag_2=13300801,
    )
    CommonFunc_20005714(0, flag=13304913, flag_1=13305805, character=3300193, region=3302806, flag_2=13300801)
    CommonFunc_20005701(
        0,
        left=13300800,
        summon_flag=13304194,
        dismissal_flag=13305194,
        character=3300194,
        region=3302194,
        left_1=13304362,
    )
    CommonFunc_20005720(0, flag=13304194, flag_1=13305194, flag_2=13300800, character=3300194)
    CommonFunc_20005711(
        0,
        flag=13304194,
        flag_1=13305805,
        character=3300194,
        region=3302800,
        region_1=3302805,
        flag_2=13300801,
    )
    CommonFunc_20005714(0, flag=13304194, flag_1=13305805, character=3300194, region=3302806, flag_2=13300801)
    CommonFunc_20005701(
        0,
        left=13300800,
        summon_flag=13304195,
        dismissal_flag=13305195,
        character=3300195,
        region=3302195,
        left_1=70000002,
    )
    CommonFunc_20005720(0, flag=13304195, flag_1=13305195, flag_2=13300800, character=3300195)
    CommonFunc_20005711(
        0,
        flag=13304195,
        flag_1=13305805,
        character=3300195,
        region=3302800,
        region_1=3302805,
        flag_2=13300801,
    )
    CommonFunc_20005714(0, flag=13304195, flag_1=13305805, character=3300195, region=3302806, flag_2=13300801)
    CommonFunc_20005701(
        0,
        left=13300800,
        summon_flag=13304196,
        dismissal_flag=13305196,
        character=3300196,
        region=3302196,
        left_1=70000008,
    )
    CommonFunc_20005720(0, flag=13304196, flag_1=13305196, flag_2=13300800, character=3300196)
    CommonFunc_20005711(
        0,
        flag=13304196,
        flag_1=13305805,
        character=3300196,
        region=3302800,
        region_1=3302805,
        flag_2=13300801,
    )
    CommonFunc_20005714(0, flag=13304196, flag_1=13305805, character=3300196, region=3302806, flag_2=13300801)
    CommonFunc_20005750(
        0,
        flag=13300800,
        flag_1=13300180,
        summon_flag=13304180,
        dismissal_flag=13305180,
        character=3300180,
        region=3302180,
        region_1=3302181,
        seconds=0.0,
        left=13304360,
    )
    CommonFunc_20005721(0, flag=13304180, flag_1=13305180, flag_2=13300800, character=3300180)
    CommonFunc_20005760(0, flag=13300180, flag_1=13304180, flag_2=13305180, character=3300180)
    CommonFunc_20005341(0, flag=13300180, character=3300180, item_lot=57800)
    CommonFunc_20005750(
        0,
        flag=13300800,
        flag_1=13300182,
        summon_flag=13304182,
        dismissal_flag=13305182,
        character=3300182,
        region=3302182,
        region_1=3302183,
        seconds=0.0,
        left=13304361,
    )
    CommonFunc_20005721(0, flag=13304182, flag_1=13305182, flag_2=13300800, character=3300182)
    CommonFunc_20005760(0, flag=13300182, flag_1=13304182, flag_2=13305182, character=3300182)
    CommonFunc_20005341(0, flag=13300182, character=3300182, item_lot=57800)
    CommonFunc_20005750(
        0,
        flag=13300800,
        flag_1=13300184,
        summon_flag=13304184,
        dismissal_flag=13305184,
        character=3300184,
        region=3302184,
        region_1=3302185,
        seconds=0.0,
        left=70000004,
    )
    CommonFunc_20005721(0, flag=13304184, flag_1=13305184, flag_2=13300800, character=3300184)
    CommonFunc_20005760(0, flag=13300184, flag_1=13304184, flag_2=13305184, character=3300184)
    CommonFunc_20005341(0, flag=13300184, character=3300184, item_lot=57900)
    CommonFunc_20006000(
        0,
        character=3300700,
        flag=1236,
        flag_1=1237,
        flag_2=73300130,
        value=0.6499999761581421,
        first_flag=1235,
        last_flag=1239,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=3300700, flag=1236, flag_1=1237, flag_2=73300130, right=3)
    CommonFunc_20006002(0, character=3300700, flag=1238, first_flag=1235, last_flag=1239)
    CommonFunc_20006003(
        0,
        character=3300700,
        flag=73300131,
        flag_1=1235,
        flag_2=1220,
        flag_3=1221,
        first_flag=1220,
        last_flag=1234,
    )
    Event_13305741(
        0,
        character=3300705,
        character_1=3300710,
        character_2=3300715,
        flag=73300180,
        flag_1=73300181,
        value=0.6499999761581421,
    )
    Event_13300743(
        0,
        character=3300705,
        character_1=3300710,
        flag=1356,
        flag_1=1357,
        character_2=3300715,
        first_flag=1355,
        last_flag=1359,
        flag_2=1340,
    )
    Event_13305744(0, character=3300705, character_1=3300710, flag=1357, flag_1=1340)
    Event_13300747(0, character=3300705, character_1=3300710, character_2=3300715)
    CommonFunc_20006001(0, attacked_entity=3300705, flag=1356, flag_1=1357, flag_2=73300180, right=3)
    CommonFunc_20006002(0, character=3300705, flag=1358, first_flag=1355, last_flag=1359)
    Event_13300748(0, character=3300705, flag=1340, flag_1=1357)
    CommonFunc_20006040(0, character=3300705, destination=3302705, special_effect=159)
    CommonFunc_20006001(0, attacked_entity=3300710, flag=1356, flag_1=1357, flag_2=73300180, right=3)
    CommonFunc_20006002(0, character=3300710, flag=1358, first_flag=1355, last_flag=1359)
    Event_13300748(1, character=3300710, flag=1340, flag_1=1357)
    CommonFunc_20006040(0, character=3300710, destination=3302705, special_effect=159)
    Event_13300745(
        0,
        character=3300715,
        flag=1496,
        flag_1=1497,
        character_1=3300705,
        character_2=3300710,
        first_flag=1495,
        last_flag=1499,
        flag_2=1480,
    )
    CommonFunc_20006001(0, attacked_entity=3300715, flag=1496, flag_1=1497, flag_2=73300181, right=3)
    CommonFunc_20006002(0, character=3300715, flag=1498, first_flag=1495, last_flag=1499)
    CommonFunc_20005490(
        0,
        owner_entity=3300579,
        character=3300578,
        entity=3301579,
        source_entity=3301578,
        model_point=90,
        behavior_id=5430,
        behavior_id_1=5431,
        behavior_id_2=5432,
        behavior_id_3=5433,
        behavior_id_4=5434,
        behavior_id_5=5435,
        behavior_id_6=5436,
        flag=13305722,
    )
    CommonFunc_20005491(0, character=3300579, character_1=3300578, region=3302579, flag=13305721)
    CommonFunc_20005493(0, character=3300579, character_1=3300578, flag=13300720)
    CommonFunc_20005494()
    CommonFunc_20005496(0, obj=3301579)
    Event_13300761(0, character=3300720)
    Event_13305762()
    CommonFunc_20006002(0, character=3300720, flag=1118, first_flag=1115, last_flag=1119)
    Event_13305763(0, character=3300720)
    CommonFunc_20006010(0, flag=73300952, animation_id=69003)
    CommonFunc_20005900(0, flag=13300560, flag_1=6331)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13300400()
    Event_13305700(0, character=3300700, animation_id=90390)
    Event_13305720(0, obj=3301579)
    CommonFunc_20005495(0, character=3300578, character_1=3300579, flag=13300720)
    Event_13305740(
        0,
        character=3300705,
        character_1=3300710,
        animation_id=90740,
        animation_id_1=90800,
        destination=3302705,
    )
    Event_13305746(0, character=3300715, animation_id=90900)
    Event_13305760(0, character=3300720)
    DisableAnimations(3300790)
    DisableGravity(3300790)
    DisableCharacterCollision(3300790)
    DisableSoundEvent(sound_id=3304801)
    DisableSoundEvent(sound_id=3304802)
    DisableSoundEvent(sound_id=3304805)
    DisableSoundEvent(sound_id=3304851)
    DisableSoundEvent(sound_id=3304852)


@RestartOnRest(13305100)
def Event_13305100():
    """Event 13305100"""
    if PlayerNotInOwnWorld():
        return
    OR_1.Add(PlayerStandingOnCollision(3304213))
    OR_1.Add(PlayerStandingOnCollision(3304214))
    OR_1.Add(PlayerStandingOnCollision(3304215))
    OR_1.Add(PlayerStandingOnCollision(3304216))
    OR_1.Add(PlayerStandingOnCollision(3304217))
    OR_1.Add(PlayerStandingOnCollision(3304218))
    OR_1.Add(PlayerStandingOnCollision(3304219))
    OR_1.Add(PlayerStandingOnCollision(3304220))
    OR_1.Add(PlayerStandingOnCollision(3304221))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 9000)
    Wait(0.800000011920929)
    Restart()


@RestartOnRest(13300110)
def Event_13300110():
    """Event 13300110"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(13300800))
    AND_1.Add(FlagEnabled(13300850))
    
    MAIN.Await(AND_1)
    
    EnableFlag(13300110)


@RestartOnRest(13305170)
def Event_13305170():
    """Event 13305170"""
    AddSpecialEffect(3300191, 12700)
    DisableAI(3300191)
    DisableAnimations(3300191)
    DisableCharacter(3300191)
    if FlagEnabled(13305161):
        return
    DisableCharacter(3300170)
    DisableAnimations(3300170)


@RestartOnRest(13305171)
def Event_13305171():
    """Event 13305171"""
    DisableFlag(13304170)
    DisableFlag(13305170)
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13300160):
        return
    if FlagEnabled(13300850):
        return
    Wait(0.5)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(13305161))
    AND_1.Add(FlagDisabled(13300160))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 490))
    AND_1.Add(CharacterBackreadEnabled(3300191))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(3300191)
    Wait(1.5)
    CreateObjectVFX(3301170, vfx_id=0, model_point=30041)
    Move(
        3300191,
        destination=3300170,
        destination_type=CoordEntityType.Character,
        model_point=236,
        copy_draw_parent=3300191,
    )
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9334, entity=3301170))
    
    MAIN.Await(AND_2)
    
    DisplayDialogAndSetFlags(
        message=2120002,
        button_type=ButtonType.OK_or_Cancel,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=3301170,
        display_distance=3.0,
        left_flag=13304179,
        right_flag=13305179,
        cancel_flag=13305179,
    )
    if FlagDisabled(13304179):
        return RESTART
    DisplayBattlefieldMessage(2300002, display_location_index=1)
    DeleteObjectVFX(3301170)
    DisableCharacter(3300191)
    Wait(5.0)
    SetNetworkConnectedFlagState(flag=13305160, state=FlagSetting.On)


@RestartOnRest(13305172)
def Event_13305172():
    """Event 13305172"""
    if FlagEnabled(13300160):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(13305160))
    AND_1.Add(FlagDisabled(13305161))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012100, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012120, display_location_index=1)
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=30340, anchor_entity=3300170, model_point=236, anchor_type=CoordEntityType.Character)
    EnableCharacter(3300170)
    EnableAnimations(3300170)
    SetBackreadStateAlternate(3300170, True)
    ForceAnimation(3300170, 63010, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=13305161, state=FlagSetting.On)


@RestartOnRest(13305173)
def Event_13305173():
    """Event 13305173"""
    if FlagEnabled(13300160):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(13305161))
    AND_1.Add(CharacterDead(3300170))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012102, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012122, display_location_index=1)
    SetBackreadStateAlternate(3300170, False)
    SetNetworkConnectedFlagState(flag=13305161, state=FlagSetting.Off)
    SetNetworkConnectedFlagState(flag=13300160, state=FlagSetting.On)


@RestartOnRest(13305174)
def Event_13305174():
    """Event 13305174"""
    if FlagEnabled(13300160):
        return
    AND_1.Add(FlagEnabled(13300161))
    AND_1.Add(CharacterDead(PLAYER))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=13305162, state=FlagSetting.On)


@RestartOnRest(13305175)
def Event_13305175():
    """Event 13305175"""
    EnableNetworkSync()
    if FlagEnabled(13300160):
        return
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(13305161))
    
    OR_1.Add(CharacterDead(3300192))
    if OR_1:
        return
    AND_1.Add(CharacterDead(3300192))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=13305162, state=FlagSetting.On)


@RestartOnRest(13305176)
def Event_13305176():
    """Event 13305176"""
    if FlagEnabled(13300160):
        return
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(13305161))
    AND_1.Add(FlagEnabled(13305162))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012101, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012121, display_location_index=1)
    Wait(1.0)
    DisableCharacter(3300170)
    DisableAnimations(3300170)
    SetBackreadStateAlternate(3300170, False)


@RestartOnRest(13305177)
def Event_13305177():
    """Event 13305177"""
    if FlagEnabled(13300160):
        return
    AND_1.Add(FlagEnabled(13305161))
    OR_1.Add(FlagEnabled(13305855))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302850))
    OR_1.Add(PlayerStandingOnCollision(3304170))
    OR_1.Add(PlayerStandingOnCollision(3304171))
    AND_2.Add(OR_1)
    AND_2.Add(PlayerInOwnWorld())
    AND_1.Add(AND_2)
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3300170, 91030, unknown2=1.0)
    Wait(1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012103, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012123, display_location_index=1)
    Wait(1.0)
    DisableCharacter(3300170)
    DisableAnimations(3300170)
    SetBackreadStateAlternate(3300170, False)


@RestartOnRest(13305200)
def Event_13305200():
    """Event 13305200"""
    DisableNetworkSync()
    AND_15.Add(CharacterDead(3300200))
    GotoIfConditionTrue(Label.L0, input_condition=AND_15)
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=3302100))
    AND_1.Add(InsideMap(game_map=FARRON_KEEP))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(3300200, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetBackreadStateAlternate(3300200, True)
    SetNetworkUpdateRate(3300397, is_fixed=True, update_rate=CharacterUpdateRate.EveryFiveFrames)
    SetBackreadStateAlternate(3300397, True)
    Wait(1.0)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302100))
    OR_1.Add(OutsideMap(game_map=FARRON_KEEP))
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(3300200, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    SetBackreadStateAlternate(3300200, False)
    SetNetworkUpdateRate(3300397, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    SetBackreadStateAlternate(3300397, False)
    Wait(1.0)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkUpdateRate(3300200, is_fixed=False, update_rate=CharacterUpdateRate.Never)
    SetBackreadStateAlternate(3300200, False)
    End()


@RestartOnRest(13305201)
def Event_13305201():
    """Event 13305201"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(HasAIStatus(3300200, ai_status=AIStatusType.Battle))

    # --- Label 0 --- #
    DefineLabel(0)
    ChangePatrolBehavior(3300200, patrol_information_id=3303200)


@RestartOnRest(13305202)
def Event_13305202(
    _,
    character: int,
    destination: int,
    destination_1: int,
    first_flag: int,
    last_flag: int,
    first_flag_1: uint,
    last_flag_1: uint,
):
    """Event 13305202"""
    DisableFlagRange((first_flag, last_flag))
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=10))
    
    EnableRandomFlagInRange(flag_range=(first_flag_1, last_flag_1))
    GotoIfFlagEnabled(Label.L0, flag=first_flag)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    Move(character, destination=destination_1, destination_type=CoordEntityType.Region, copy_draw_parent=character)

    # --- Label 1 --- #
    DefineLabel(1)
    Restart()


@ContinueOnRest(13305209)
def Event_13305209():
    """Event 13305209"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302500))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302501))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302502))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302503))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302504))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302505))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302506))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302507))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302508))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302509))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302510))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302511))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302512))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302513))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302514))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302515))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302516))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302517))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302518))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302519))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302520))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302521))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302522))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302523))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302524))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302525))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302526))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3302527))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(PLAYER, 4310)
    Wait(2.4000000953674316)
    Restart()


@ContinueOnRest(13305210)
def Event_13305210():
    """Event 13305210"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(HasAIStatus(3300484, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(3300484, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(3300484, 12140)
    ReplanAI(3300484)


@RestartOnRest(13305211)
def Event_13305211(_, character: int, character_1: int, special_effect: int, special_effect_id: int, ai_param_id: int):
    """Event 13305211"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(character_1, special_effect_id)
    if ValueEqual(left=ai_param_id, right=0):
        return
    SetAIParamID(character_1, ai_param_id=ai_param_id)
    ReplanAI(character_1)


@RestartOnRest(13305230)
def Event_13305230():
    """Event 13305230"""
    if ThisEventSlotFlagEnabled():
        return
    GotoIfFlagEnabled(Label.L0, flag=13304230)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3302281))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3302282))
    AND_2.Add(OR_1)
    AND_2.Add(OR_2)
    OR_3.Add(AND_2)
    OR_3.Add(HasAIStatus(3300341, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(3300341, 5000)
    ChangePatrolBehavior(3300341, patrol_information_id=3303280)
    
    MAIN.Await(HasAIStatus(3300341, ai_status=AIStatusType.Battle))
    
    RemoveSpecialEffect(3300341, 5000)
    End()


@RestartOnRest(13305300)
def Event_13305300():
    """Event 13305300"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3302360))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3302361))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=3302361))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    AND_4.Add(OR_1)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    AND_4.Add(not AND_9)
    
    MAIN.Await(AND_4)
    
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_1)
    GotoIfFinishedConditionTrue(Label.L2, input_condition=AND_2)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    Move(3300388, destination=3302363, destination_type=CoordEntityType.Region, copy_draw_parent=3300388)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    Move(3300388, destination=3302363, destination_type=CoordEntityType.Region, copy_draw_parent=3300388)
    End()


@ContinueOnRest(13300310)
def Event_13300310():
    """Event 13300310"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    GotoIfFlagEnabled(Label.L0, flag=13300560)
    
    MAIN.Await(CharacterDead(3300560))
    
    Wait(3.5)
    AddSpecialEffect(3300561, 4630)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(3300561)
    DisableAnimations(3300561)


@RestartOnRest(13305320)
def Event_13305320(_, character: int):
    """Event 13305320"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 5000)
    
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    RemoveSpecialEffect(character, 5000)


@RestartOnRest(13305360)
def Event_13305360():
    """Event 13305360"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DisableFlag(13304360)
    AND_1.Add(FlagDisabled(13304182))
    AND_1.Add(FlagDisabled(13305182))
    AND_2.Add(FlagEnabled(13304182))
    AND_2.Add(FlagEnabled(13305182))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    AND_3.Add(FlagDisabled(13304194))
    AND_3.Add(FlagDisabled(13305194))
    AND_4.Add(FlagEnabled(13304194))
    AND_4.Add(FlagEnabled(13305194))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    AND_5.Add(OR_1)
    AND_5.Add(OR_2)
    
    MAIN.Await(AND_5)
    
    EnableFlag(13304360)
    AND_8.Add(FlagEnabled(13304182))
    AND_8.Add(FlagDisabled(13305182))
    AND_9.Add(FlagDisabled(13304182))
    AND_9.Add(FlagEnabled(13305182))
    OR_8.Add(AND_8)
    OR_8.Add(AND_9)
    AND_10.Add(FlagEnabled(13304194))
    AND_10.Add(FlagDisabled(13305194))
    AND_11.Add(FlagDisabled(13304194))
    AND_11.Add(FlagEnabled(13305194))
    OR_9.Add(AND_10)
    OR_9.Add(AND_10)
    OR_10.Add(OR_8)
    OR_10.Add(OR_9)
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(13305361)
def Event_13305361():
    """Event 13305361"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DisableFlag(13304361)
    AND_1.Add(FlagDisabled(13304180))
    AND_1.Add(FlagDisabled(13305180))
    AND_2.Add(FlagEnabled(13304180))
    AND_2.Add(FlagEnabled(13305180))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    AND_3.Add(FlagDisabled(13304194))
    AND_3.Add(FlagDisabled(13305194))
    AND_4.Add(FlagEnabled(13304194))
    AND_4.Add(FlagEnabled(13305194))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    AND_5.Add(FlagDisabled(73500150))
    AND_5.Add(OR_1)
    AND_5.Add(OR_2)
    
    MAIN.Await(AND_5)
    
    EnableFlag(13304361)
    AND_8.Add(FlagEnabled(13304180))
    AND_8.Add(FlagDisabled(13305180))
    AND_9.Add(FlagDisabled(13304180))
    AND_9.Add(FlagEnabled(13305180))
    OR_8.Add(AND_8)
    OR_8.Add(AND_9)
    AND_10.Add(FlagEnabled(13304194))
    AND_10.Add(FlagDisabled(13305194))
    AND_11.Add(FlagDisabled(13304194))
    AND_11.Add(FlagEnabled(13305194))
    OR_9.Add(AND_10)
    OR_9.Add(AND_10)
    OR_10.Add(FlagEnabled(73500150))
    OR_10.Add(OR_8)
    OR_10.Add(OR_9)
    
    MAIN.Await(OR_10)
    
    Restart()


@RestartOnRest(13305362)
def Event_13305362():
    """Event 13305362"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    DisableFlag(13304362)
    AND_1.Add(FlagDisabled(13304180))
    AND_1.Add(FlagDisabled(13305180))
    AND_2.Add(FlagEnabled(13304180))
    AND_2.Add(FlagEnabled(13305180))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    AND_3.Add(FlagDisabled(13304182))
    AND_3.Add(FlagDisabled(13305182))
    AND_4.Add(FlagEnabled(13304182))
    AND_4.Add(FlagEnabled(13305182))
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    AND_5.Add(FlagEnabled(73500150))
    AND_5.Add(OR_1)
    AND_5.Add(OR_2)
    
    MAIN.Await(AND_5)
    
    EnableFlag(13304362)
    AND_8.Add(FlagEnabled(13304180))
    AND_8.Add(FlagDisabled(13305180))
    AND_9.Add(FlagDisabled(13304180))
    AND_9.Add(FlagEnabled(13305180))
    OR_8.Add(AND_8)
    OR_8.Add(AND_9)
    AND_10.Add(FlagEnabled(13304182))
    AND_10.Add(FlagDisabled(13305182))
    AND_11.Add(FlagDisabled(13304182))
    AND_11.Add(FlagEnabled(13305182))
    OR_9.Add(AND_10)
    OR_9.Add(AND_10)
    OR_10.Add(FlagDisabled(73500150))
    OR_10.Add(OR_8)
    OR_10.Add(OR_9)
    
    MAIN.Await(OR_10)
    
    Restart()


@ContinueOnRest(13300400)
def Event_13300400():
    """Event 13300400"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13300405)


@RestartOnRest(13305408)
def Event_13305408():
    """Event 13305408"""
    GotoIfFlagEnabled(Label.L0, flag=13300405)
    ForceAnimation(3301405, 20, skip_transition=True, unknown2=1.0)
    DisableFlag(13305405)
    DisableObjectActivation(3301407, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3301405, 10, skip_transition=True, unknown2=1.0)
    EnableFlag(13305405)
    DisableObjectActivation(3301406, obj_act_id=-1)
    End()


@RestartOnRest(13305409)
def Event_13305409():
    """Event 13305409"""
    CommonFunc_20005621(
        0,
        flag=13300405,
        flag_1=13301405,
        obj=3301405,
        obj_1=3301406,
        obj_act_id=3304406,
        obj_2=3301407,
        obj_act_id_1=3304407,
        region=3302406,
        region_1=3302407,
        flag_2=13301406,
        flag_3=13304405,
        left=0,
    )


@ContinueOnRest(13305410)
def Event_13305410(_, flag: int, flag_1: int, value: uint, obj: int):
    """Event 13305410"""
    MAIN.Await(EventValue(flag=flag, bit_count=2) >= value)
    
    EndOfAnimation(obj=obj, animation_id=0)
    if FlagEnabled(flag_1):
        return
    EnableFlag(flag_1)


@ContinueOnRest(13300412)
def Event_13300412(
    _,
    flag: int,
    flag_1: int,
    destination: int,
    obj: int,
    vfx_id: int,
    vfx_id_1: int,
    vfx_id_2: int,
    cutscene_id: int,
    cutscene_id_1: int,
    cutscene_id_2: int,
    cutscene_id_3: int,
):
    """Event 13300412"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    DeleteVFX(vfx_id)
    DeleteVFX(vfx_id_1)
    CreateVFX(vfx_id_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CreateVFX(vfx_id_1)
    DeleteVFX(vfx_id_2)
    DeleteObjectVFX(obj, erase_root=False)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ActionButtonParamActivated(action_button_id=9330, entity=destination))
    
    MAIN.Await(AND_1)
    
    Move(PLAYER, destination=destination, destination_type=CoordEntityType.Object, model_point=120, short_move=True)
    ForceAnimation(PLAYER, 60380, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    DeleteVFX(vfx_id_1)
    Wait(2.4000000953674316)
    DeleteVFX(vfx_id)
    OR_1.Add(EventValue(flag=flag, bit_count=2) == 0)
    OR_2.Add(EventValue(flag=flag, bit_count=2) == 1)
    OR_3.Add(EventValue(flag=flag, bit_count=2) == 2)
    OR_4.Add(EventValue(flag=flag, bit_count=2) == 3)
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)
    GotoIfConditionTrue(Label.L2, input_condition=OR_2)
    GotoIfConditionTrue(Label.L3, input_condition=OR_3)
    GotoIfConditionTrue(Label.L4, input_condition=OR_4)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(cutscene_id, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(cutscene_id, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(cutscene_id, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(cutscene_id_1, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(cutscene_id_1, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(cutscene_id_1, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    Goto(Label.L5)

    # --- Label 3 --- #
    DefineLabel(3)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(cutscene_id_2, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(cutscene_id_2, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(cutscene_id_2, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(cutscene_id_3, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(cutscene_id_3, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(cutscene_id_3, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    WaitFrames(frames=1)
    CreateVFX(vfx_id_2)
    IncrementEventValue(flag, bit_count=2, max_value=3)
    End()


@RestartOnRest(13305421)
def Event_13305421():
    """Event 13305421"""
    GotoIfFlagDisabled(Label.L0, flag=13300421)
    EndOfAnimation(obj=3301421, animation_id=1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(13300800))
    AND_1.Add(EntityWithinDistance(entity=3301421, other_entity=PLAYER, radius=12.0))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3301421, 1, skip_transition=True, unknown2=1.0)
    EnableFlag(13300421)
    End()


@RestartOnRest(13305470)
def Event_13305470():
    """Event 13305470"""
    if PlayerNotInOwnWorld():
        return
    if ThisEventSlotFlagEnabled():
        return
    DeleteObjectVFX(3301470)
    CreateObjectVFX(3301470, vfx_id=200, model_point=831023)
    CreateObjectVFX(3301470, vfx_id=200, model_point=60)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=9333, entity=3301470))
    
    ForceAnimation(PLAYER, 60070, unknown2=1.0)
    Wait(0.20000000298023224)
    CreateTemporaryVFX(vfx_id=301002, anchor_entity=PLAYER, model_point=220, anchor_type=CoordEntityType.Character)
    PlaySoundEffect(PLAYER, 999999988, sound_type=SoundType.c_CharacterMotion)
    AddSpecialEffect(PLAYER, 2005)
    DeleteObjectVFX(3301470)


@RestartOnRest(13305471)
def Event_13305471():
    """Event 13305471"""
    EndOfAnimation(obj=3301305, animation_id=1)


@ContinueOnRest(13305480)
def Event_13305480():
    """Event 13305480"""
    RegisterLadder(start_climbing_flag=13300480, stop_climbing_flag=13300481, obj=3301480)
    RegisterLadder(start_climbing_flag=13300482, stop_climbing_flag=13300483, obj=3301482)


@ContinueOnRest(13305800)
def Event_13305800():
    """Event 13305800"""
    if FlagEnabled(13300800):
        return
    AND_1.Add(HealthRatio(3300801) <= 0.0)
    
    MAIN.Await(AND_1)
    
    PlaySoundEffect(3300801, 777777777, sound_type=SoundType.s_SFX)
    AND_1.Add(CharacterDead(3300801))
    
    MAIN.Await(AND_1)
    
    HandleBossDefeatAndDisplayBanner(boss=3300801, banner=BannerType.UnknownBossDefeat)
    EnableFlag(13300800)
    EnableFlag(9307)
    EnableFlag(6307)


@RestartOnRest(13305810)
def Event_13305810():
    """Event 13305810"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(13304810)
    GotoIfFlagDisabled(Label.L0, flag=13300800)
    DisableCharacter(3305800)
    Kill(3305800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(3300801)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=13300801)
    EnableSoundEvent(sound_id=3304805)
    DisableCharacter(3300801)
    DisableAnimations(3300801)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(13305805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3302800))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    GotoIfFlagEnabled(Label.L2, flag=13300801)
    DisableSoundEvent(sound_id=3304805)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(33000010, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(33000010, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(33000010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(3300801)
    EnableAnimations(3300801)
    EnableAI(3300801)
    EnableSpawner(entity=3303800)
    SetNetworkUpdateRate(3300801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3300802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3300803, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3300801, name=903040)
    SetNetworkConnectedFlagState(flag=13300801, state=FlagSetting.On)
    EnableFlag(13304810)


@RestartOnRest(13305811)
def Event_13305811():
    """Event 13305811"""
    if FlagEnabled(13300800):
        return
    AND_9.Add(ThisEventSlotFlagEnabled())
    AND_9.Add(FlagEnabled(13304810))
    GotoIfConditionTrue(Label.L0, input_condition=AND_9)
    ForceAnimation(3300802, 30000, unknown2=1.0)
    
    MAIN.Await(FlagEnabled(13304810))
    
    OR_1.Add(HealthRatio(3300801) <= 0.800000011920929)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(TimeElapsed(seconds=20.0))
    AND_2.Add(OR_1)
    AND_2.Add(FlagDisabled(13305801))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3302806))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(3300802, 12245)
    WaitFrames(frames=1)
    if CharacterDoesNotHaveSpecialEffect(character=3300802, special_effect=12243):
        ForceAnimation(3300802, 20001, unknown2=1.0)
    else:
        ForceAnimation(3300802, 20000, unknown2=1.0)
    EnableAI(3300802)
    OR_2.Add(HealthValue(3300801) <= 1)
    OR_3.Add(OR_2)
    OR_3.Add(HealthValue(3300802) == 1)
    
    MAIN.Await(OR_3)
    
    RestartIfFinishedConditionFalse(input_condition=OR_2)
    Kill(3300802)
    End()


@RestartOnRest(13305812)
def Event_13305812():
    """Event 13305812"""
    if FlagEnabled(13300800):
        return
    AND_9.Add(ThisEventSlotFlagEnabled())
    AND_9.Add(FlagEnabled(13304810))
    GotoIfConditionTrue(Label.L0, input_condition=AND_9)
    ForceAnimation(3300803, 30001, unknown2=1.0)
    
    MAIN.Await(FlagEnabled(13304810))
    
    OR_1.Add(HealthRatio(3300801) <= 0.6000000238418579)
    OR_1.Add(TimeElapsed(seconds=40.0))
    SkipLines(2)

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(TimeElapsed(seconds=20.0))
    AND_2.Add(OR_1)
    AND_2.Add(FlagDisabled(13305801))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3302806))
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(3300803, 12245)
    WaitFrames(frames=1)
    if CharacterDoesNotHaveSpecialEffect(character=3300803, special_effect=12243):
        ForceAnimation(3300803, 20001, unknown2=1.0)
    else:
        ForceAnimation(3300803, 20000, unknown2=1.0)
    EnableAI(3300803)
    OR_2.Add(HealthValue(3300801) <= 1)
    OR_3.Add(OR_2)
    OR_3.Add(HealthValue(3300803) == 1)
    
    MAIN.Await(OR_3)
    
    RestartIfFinishedConditionFalse(input_condition=OR_2)
    Kill(3300803)
    End()


@RestartOnRest(13305813)
def Event_13305813():
    """Event 13305813"""
    if FlagEnabled(13300800):
        return
    AND_1.Add(FlagEnabled(13305812))
    
    MAIN.Await(AND_1)
    
    Wait(20.0)
    EnableCharacter(3300804)
    EnableAnimations(3300804)
    EnableAI(3300804)


@ContinueOnRest(13305814)
def Event_13305814():
    """Event 13305814"""
    if FlagEnabled(13300800):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(3300801, 12246))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(3305801, 6060)
    Kill(3305801)
    DisableCharacter(3305801)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(33000000, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(33000000, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(33000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    Move(3300801, destination=3302802, destination_type=CoordEntityType.Region, copy_draw_parent=3300801)
    SetAIParamID(3300801, ai_param_id=304010)
    AddSpecialEffect(3300801, 12240)
    AddSpecialEffect(3300801, 12241)
    AddSpecialEffect(3300801, 5404)
    AddSpecialEffect(3300801, 12245)
    Wait(0.30000001192092896)
    RemoveSpecialEffect(3300801, 6060)
    ForceAnimation(3300801, 20, unknown2=1.0)
    EnableFlag(13305802)


@RestartOnRest(13305828)
def Event_13305828(_, flag: int, flag_1: int, flag_2: int, region: int, sound_id: int, sound_id_1: int, flag_3: int):
    """Event 13305828"""
    DisableNetworkSync()
    DisableSoundEvent(sound_id=sound_id)
    DisableSoundEvent(sound_id=sound_id_1)
    if FlagEnabled(flag):
        return
    AND_1.Add(FlagEnabled(flag_1))
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    AND_1.Add(FlagEnabled(flag_2))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    
    MAIN.Await(AND_1)
    
    Unknown_2010_07(sound_id=sound_id_1)
    WaitFrames(frames=1)
    EnableBossMusic(sound_id=sound_id)
    OR_1.Add(FlagEnabled(flag_3))
    OR_1.Add(FlagEnabled(flag))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagEnabled(Label.L0, flag=flag)
    EnableBossMusic(sound_id=sound_id_1)
    
    MAIN.Await(FlagEnabled(flag))

    # --- Label 0 --- #
    DefineLabel(0)
    DisableBossMusic(sound_id=-1)


@RestartOnRest(13305829)
def Event_13305829():
    """Event 13305829"""
    CommonFunc_20005800(
        0,
        flag=13300800,
        entity=3301800,
        region=3302800,
        flag_1=13305805,
        action_button_id=3301800,
        character=3305800,
        left=13300801,
        region_1=3302801,
    )
    CommonFunc_20005801(
        0,
        flag=13300800,
        entity=3301800,
        region=3302800,
        flag_1=13305805,
        action_button_id=3301800,
        flag_2=13305806,
    )
    Event_13305828(
        0,
        flag=13300800,
        flag_1=13305805,
        flag_2=13305806,
        region=3302800,
        sound_id=3304801,
        sound_id_1=3304802,
        flag_3=13305802,
    )
    CommonFunc_20005820(0, flag=13300800, obj=3301800, model_point=3, left=13300801)
    DisableObject(3301801)
    CommonFunc_20005810(0, flag=13300800, entity=3301800, target_entity=3302800, action_button_id=10000)


@ContinueOnRest(13305850)
def Event_13305850():
    """Event 13305850"""
    if FlagEnabled(13300850):
        return
    
    MAIN.Await(HealthRatio(3300850) <= 0.0)
    
    Kill(3305851)
    Wait(1.0)
    PlaySoundEffect(3300850, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3300850))
    
    KillBoss(game_area_param_id=3300850)
    EnableFlag(13300850)
    EnableFlag(9306)
    EnableFlag(6306)


@RestartOnRest(13305860)
def Event_13305860():
    """Event 13305860"""
    GotoIfFlagDisabled(Label.L0, flag=13300850)
    DisableCharacter(3305850)
    Kill(3305850)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(3305850)
    DisableCharacter(3305850)
    DisableAnimations(3305850)
    EnableImmortality(3305851)
    DisableHealthBar(3305851)
    AND_1.Add(FlagEnabled(13305855))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3302850))
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L1, flag=13300802)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(13300852)
    EnableCharacter(3300850)
    EnableAnimations(3300850)
    EnableAI(3300850)
    SetNetworkUpdateRate(3300850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3300851, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3300852, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(3300853, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3300850, 20001, wait_for_completion=True, unknown2=1.0)
    EnableBossHealthBar(3300850, name=901320)


@RestartOnRest(13305861)
def Event_13305861():
    """Event 13305861"""
    MAIN.Await(CharacterHasTAEEvent(3300850, tae_event_id=20))
    
    EnableFlag(13305851)


@RestartOnRest(13305862)
def Event_13305862():
    """Event 13305862"""
    DisableNetworkSync()
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 10553))
    AND_1.Add(CharacterHasTAEEvent(3300850, tae_event_id=300))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=6000, locked_camera_id=-1)
    
    MAIN.Await(CharacterHasTAEEvent(3300850, tae_event_id=400))
    
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Restart()


@RestartOnRest(13305863)
def Event_13305863(_, character: int, flag: int, flag_1: int, flag_2: int):
    """Event 13305863"""
    OR_1.Add(CharacterHasTAEEvent(character, tae_event_id=10))
    OR_2.Add(CharacterHasTAEEvent(character, tae_event_id=20))
    OR_3.Add(CharacterHasTAEEvent(character, tae_event_id=30))
    OR_4.Add(OR_1)
    OR_4.Add(OR_2)
    OR_4.Add(OR_3)
    
    MAIN.Await(OR_4)
    
    DisableCharacter(character)
    GotoIfFinishedConditionFalse(Label.L9, input_condition=OR_3)
    AND_9.Add(FlagEnabled(flag))
    AND_9.Add(FlagEnabled(flag_1))
    AND_9.Add(FlagEnabled(flag_2))
    
    MAIN.Await(AND_9)

    # --- Label 9 --- #
    DefineLabel(9)
    WaitFrames(frames=1)
    GotoIfPlayerNotInOwnWorld(Label.L5)
    GotoIfCharacterInsideRegion(Label.L1, character=PLAYER, region=3302861)
    GotoIfCharacterInsideRegion(Label.L2, character=PLAYER, region=3302862)
    GotoIfCharacterInsideRegion(Label.L3, character=PLAYER, region=3302863)
    GotoIfCharacterInsideRegion(Label.L4, character=PLAYER, region=3302864)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableRandomFlagInRange(flag_range=(13304870, 13304884))
    Goto(Label.L5)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableRandomFlagInRange(flag_range=(13304870, 13304872))
    Goto(Label.L5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableRandomFlagInRange(flag_range=(13304873, 13304875))
    Goto(Label.L5)

    # --- Label 3 --- #
    DefineLabel(3)
    EnableRandomFlagInRange(flag_range=(13304876, 13304878))
    Goto(Label.L5)

    # --- Label 4 --- #
    DefineLabel(4)
    EnableRandomFlagInRange(flag_range=(13304879, 13304881))
    Goto(Label.L5)

    # --- Label 5 --- #
    DefineLabel(5)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=80))
    
    Restart()


@RestartOnRest(13305864)
def Event_13305864(_, flag: int, character: int):
    """Event 13305864"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    EnableCharacter(character)
    ForceAnimation(character, 20001, unknown2=1.0)
    ReplanAI(character)
    Restart()


@RestartOnRest(13305865)
def Event_13305865(
    _,
    flag: int,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    flag_1: int,
    flag_2: int,
    flag_3: int,
    flag_4: int,
    flag_5: int,
    flag_6: int,
):
    """Event 13305865"""
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(13305851))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    EnableCharacter(character)
    EnableCharacter(character_1)
    EnableCharacter(character_2)
    EnableCharacter(character_3)
    EnableAI(character_1)
    EnableAI(character_2)
    EnableAI(character_3)
    EnableAnimations(character_1)
    EnableAnimations(character_2)
    EnableAnimations(character_3)
    ForceAnimation(character, 20001, unknown2=1.0)
    ReplanAI(character)
    ForceAnimation(character_1, 20001, unknown2=1.0)
    ReplanAI(character_1)
    ForceAnimation(character_2, 20001, unknown2=1.0)
    ReplanAI(character_2)
    ForceAnimation(character_3, 20001, unknown2=1.0)
    ReplanAI(character_3)
    DisableFlag(flag_1)
    DisableFlag(flag_2)
    DisableFlag(flag_3)
    EnableFlag(flag_4)
    EnableFlag(flag_5)
    EnableFlag(flag_6)
    Restart()


@RestartOnRest(13305866)
def Event_13305866(_, character: int, character_1: int, flag: int, flag_1: int):
    """Event 13305866"""
    MAIN.Await(FlagEnabled(flag))
    
    AND_1.Add(AttackedWithDamageType(attacked_entity=character))
    AND_2.Add(CharacterHasTAEEvent(character_1, tae_event_id=40))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    WaitFrames(frames=1)
    GotoIfFinishedConditionFalse(Label.L0, input_condition=AND_1)
    ForceAnimation(character, 3013, unknown2=1.0)
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=50))
    
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(character, 20000, wait_for_completion=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableFlag(flag)
    EnableFlag(flag_1)
    Restart()


@RestartOnRest(13305870)
def Event_13305870(
    _,
    flag: int,
    character: int,
    destination: int,
    flag_1: int,
    source_entity: int,
    source_entity_1: int,
    source_entity_2: int,
):
    """Event 13305870"""
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(13305851))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(5.0)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    EnableFlag(flag_1)
    Restart()


@RestartOnRest(13305885)
def Event_13305885(
    _,
    flag: int,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    source_entity: int,
    source_entity_1: int,
    source_entity_2: int,
    destination: int,
    flag_1: int,
    source_entity_3: int,
    source_entity_4: int,
    source_entity_5: int,
    source_entity_6: int,
    source_entity_7: int,
    source_entity_8: int,
    source_entity_9: int,
):
    """Event 13305885"""
    if FlagEnabled(13300850):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(13305851))
    
    MAIN.Await(AND_1)
    
    DisableFlag(flag)
    AND_2.Add(HealthRatio(3300850) <= 0.20000000298023224)
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_3.Add(HealthRatio(3300850) <= 0.4000000059604645)
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    Goto(Label.L2)

    # --- Label 0 --- #
    DefineLabel(0)
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_2,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_7,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_8,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_9,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 1 --- #
    DefineLabel(1)
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_1,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_6,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )

    # --- Label 2 --- #
    DefineLabel(2)
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_3,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_4,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    ShootProjectile(
        owner_entity=character,
        source_entity=source_entity_5,
        model_point=-1,
        behavior_id=213200010,
        launch_angle_x=0,
        launch_angle_y=0,
        launch_angle_z=0,
    )
    Wait(5.0)
    Move(character, destination=source_entity, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Move(
        character_1,
        destination=source_entity_1,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=character_1,
    )
    Move(
        character_2,
        destination=source_entity_2,
        destination_type=CoordEntityType.Region,
        copy_draw_parent=character_2,
    )
    Move(character_3, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character_3)
    EnableFlag(flag_1)
    Restart()


@RestartOnRest(13305900)
def Event_13305900():
    """Event 13305900"""
    CommonFunc_20005800(
        0,
        flag=13300850,
        entity=3301850,
        region=3302850,
        flag_1=13305855,
        action_button_id=3301850,
        character=3305850,
        left=13300852,
        region_1=3302851,
    )
    CommonFunc_20005801(
        0,
        flag=13300850,
        entity=3301850,
        region=3302850,
        flag_1=13305855,
        action_button_id=3301850,
        flag_2=13305856,
    )
    CommonFunc_20005831(
        0,
        flag=13300850,
        flag_1=13305855,
        flag_2=13305856,
        region=3302850,
        sound_id=3304851,
        sound_id_1=3304852,
        flag_3=13305851,
    )
    CommonFunc_20005820(0, flag=13300850, obj=3301850, model_point=3, left=13300852)
    CommonFunc_20005820(0, flag=13300850, obj=3301851, model_point=3, left=0)
    CommonFunc_20005810(0, flag=13300110, entity=3301850, target_entity=3302850, action_button_id=10000)


@ContinueOnRest(13305700)
def Event_13305700(_, character: int, animation_id: int):
    """Event 13305700"""
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

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000063)
    if FlagEnabled(1235):
        DisableFlag(73300120)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1220)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
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
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@ContinueOnRest(13305720)
def Event_13305720(_, obj: int):
    """Event 13305720"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1475, 1479))
    DisableNetworkConnectedFlagRange(flag_range=(1475, 1479))
    SetNetworkConnectedFlagState(flag=1475, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(70000075))
    AND_1.Add(FlagEnabled(1476))
    SkipLinesIfConditionFalse(6, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1475, 1479))
    SetNetworkConnectedFlagState(flag=1475, state=FlagSetting.On)
    SetTeamType(3100715, TeamType.FriendlyNPC)
    if FlagEnabled(13100660):
        SetTeamType(3100195, TeamType.CoopNPC)
        SetTeamType(3100196, TeamType.CoopNPC)
    GotoIfFlagDisabled(Label.L9, flag=1475)
    SkipLinesIfFlagRangeAnyEnabled(2, (1460, 1474))
    DisableNetworkConnectedFlagRange(flag_range=(1460, 1474))
    SetNetworkConnectedFlagState(flag=1460, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000075)
    OR_1.Add(PlayerHasGood(462))
    OR_1.Add(PlayerHasGood(463))
    SkipLinesIfConditionTrue(3, OR_1)
    DisableFlag(50006250)
    SetNetworkConnectedFlagState(flag=13300720, state=FlagSetting.Off)
    SkipLines(2)
    EnableFlag(50006250)
    SetNetworkConnectedFlagState(flag=13300720, state=FlagSetting.On)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1460)
    GotoIfFlagEnabled(Label.L0, flag=1462)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L10, flag=1476)
    GotoIfFlagEnabled(Label.L11, flag=1478)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    End()

    # --- Label 11 --- #
    DefineLabel(11)
    DisableObject(obj)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    GotoIfFlagEnabled(Label.L10, flag=1476)
    GotoIfFlagEnabled(Label.L11, flag=1478)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    End()

    # --- Label 11 --- #
    DefineLabel(11)
    DisableObject(obj)
    End()


@ContinueOnRest(13305740)
def Event_13305740(_, character: int, character_1: int, animation_id: int, animation_id_1: int, destination: int):
    """Event 13305740"""
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

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000069)
    if FlagEnabled(1355):
        DisableFlag(73300170)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1340)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1356)
    GotoIfFlagEnabled(Label.L2, flag=1357)
    GotoIfFlagEnabled(Label.L3, flag=1358)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
    ForceAnimation(character, animation_id, unknown2=1.0)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    Move(character_1, destination=destination, destination_type=CoordEntityType.Region, short_move=True)
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
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    SetTeamType(character_1, TeamType.HostileNPC)
    ForceAnimation(character_1, animation_id_1, unknown2=1.0)
    End()

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfFlagDisabled(Label.L20, flag=9013)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 20 --- #
    DefineLabel(20)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character_1)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()


@ContinueOnRest(13305741)
def Event_13305741(_, character: int, character_1: int, character_2: int, flag: int, flag_1: int, value: float):
    """Event 13305741"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    DisableFlag(flag_1)
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(HealthRatio(character_1) > 0.0)
    AND_1.Add(FlagRangeAllDisabled(flag_range=(1356, 1357)))
    AND_1.Add(FlagEnabled(1340))
    AND_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    AND_2.Add(HealthRatio(character) < value)
    OR_1.Add(AND_2)
    AND_3.Add(AttackedWithDamageType(attacked_entity=character_1, attacker=PLAYER))
    AND_3.Add(HealthRatio(character_1) < value)
    OR_1.Add(AND_3)
    OR_1.Add(FlagEnabled(flag))
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    AND_4.Add(HealthRatio(character_2) > 0.0)
    AND_4.Add(FlagRangeAllDisabled(flag_range=(1496, 1497)))
    AND_4.Add(FlagEnabled(1480))
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
    if CharacterHasSpecialEffect(character=character, special_effect=159):
        ForceAnimation(character, 0, unknown2=1.0)
    if CharacterHasSpecialEffect(character=character_1, special_effect=159):
        ForceAnimation(character_1, 0, unknown2=1.0)
    if CharacterHasSpecialEffect(character=character_2, special_effect=159):
        ForceAnimation(character_2, 0, unknown2=1.0)


@ContinueOnRest(13305742)
def Event_13305742(
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
    """Event 13305742"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag_2)
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(FlagDisabled(flag_1))
    AND_1.Add(FlagEnabled(flag_4))
    AND_1.Add(HealthRatio(character) > 0.0)
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


@ContinueOnRest(13300743)
def Event_13300743(
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
    """Event 13300743"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(first_flag))
    OR_1.Add(FlagEnabled(flag))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterDead(character_2))
    AND_1.Add(HealthRatio(character) > 0.0)
    AND_1.Add(HealthRatio(character_1) > 0.0)
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    SetTeamType(character_1, TeamType.HostileNPC)
    AICommand(character, command_id=20, command_slot=1)
    ReplanAI(character)
    AICommand(character_1, command_id=20, command_slot=1)
    ReplanAI(character_1)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    SaveRequest()
    WaitFrames(frames=1)
    AND_2.Add(CharacterHasSpecialEffect(character, 159))
    SkipLinesIfConditionFalse(1, AND_2)
    ForceAnimation(character, 0, unknown2=1.0)
    AND_3.Add(CharacterHasSpecialEffect(character_1, 159))
    SkipLinesIfConditionFalse(1, AND_3)
    ForceAnimation(character_1, 0, unknown2=1.0)


@ContinueOnRest(13305744)
def Event_13305744(_, character: int, character_1: int, flag: int, flag_1: int):
    """Event 13305744"""
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


@ContinueOnRest(13300745)
def Event_13300745(
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
    """Event 13300745"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag_2))
    OR_1.Add(FlagEnabled(first_flag))
    OR_1.Add(FlagEnabled(flag))
    AND_1.Add(OR_1)
    OR_2.Add(CharacterDead(character_1))
    OR_2.Add(CharacterDead(character_2))
    AND_1.Add(OR_2)
    AND_1.Add(HealthRatio(character) > 0.0)
    
    MAIN.Await(AND_1)
    
    SetTeamType(character, TeamType.HostileNPC)
    DisableNetworkConnectedFlagRange(flag_range=(first_flag, last_flag))
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    SaveRequest()
    WaitFrames(frames=1)
    OR_15.Add(CharacterHasSpecialEffect(character, 159))
    SkipLinesIfConditionFalse(1, OR_15)
    ForceAnimation(character, 0, unknown2=1.0)


@ContinueOnRest(13305746)
def Event_13305746(_, character: int, animation_id: int):
    """Event 13305746"""
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

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000091)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1480)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
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
    DropMandatoryTreasure(character)
    DisableCharacter(character)
    DisableBackread(character)
    End()


@ContinueOnRest(13300747)
def Event_13300747(_, character: int, character_1: int, character_2: int):
    """Event 13300747"""
    if ThisEventFlagEnabled():
        return
    EndIfFlagRangeAnyEnabled(flag_range=(1341, 1354))
    AND_1.Add(FlagEnabled(1340))
    AND_1.Add(FlagEnabled(1355))
    AND_1.Add(FlagEnabled(1480))
    AND_1.Add(FlagEnabled(1495))
    AND_1.Add(FlagEnabled(73300151))
    AND_1.Add(CharacterBackreadDisabled(character))
    AND_1.Add(CharacterBackreadDisabled(character_1))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=4,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableNetworkConnectedFlagRange(flag_range=(1340, 1354))
    SetNetworkConnectedFlagState(flag=1341, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1480, 1494))
    SetNetworkConnectedFlagState(flag=1481, state=FlagSetting.On)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    if PlayerNotInOwnWorld():
        return
    SaveRequest()


@RestartOnRest(13300748)
def Event_13300748(_, character: int, flag: int, flag_1: int):
    """Event 13300748"""
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


@ContinueOnRest(13305760)
def Event_13305760(_, character: int):
    """Event 13305760"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1115, 1119))
    DisableNetworkConnectedFlagRange(flag_range=(1115, 1119))
    SetNetworkConnectedFlagState(flag=1115, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1102))
    AND_5.Add(FlagEnabled(74000705))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1100, 1114))
    SetNetworkConnectedFlagState(flag=1103, state=FlagSetting.On)
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

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1118)
    GotoIfFlagEnabled(Label.L1, flag=1104)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    SetTeamType(character, TeamType.HostileNPC)
    DisableFlag(73300200)
    ForceAnimation(character, 90690, skip_transition=True, unknown2=1.0)
    ReplanAI(character)
    DisableAI(character)
    End()


@RestartOnRest(13300761)
def Event_13300761(_, character: int):
    """Event 13300761"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(13300761):
        return
    AND_1.Add(HealthRatio(3300720) != 0.0)
    AND_1.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_1.Add(HealthRatio(PLAYER) == 0.0)
    AND_1.Add(PlayerHasGood(388))
    
    MAIN.Await(AND_1)
    
    DisableFlag(50006071)
    RemoveGoodFromPlayer(item=388, quantity=1)


@RestartOnRest(13305762)
def Event_13305762():
    """Event 13305762"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1118))
    AND_1.Add(FlagEnabled(1104))
    AND_1.Add(FlagDisabled(50006072))
    if not AND_1:
        return
    AwardItemLot(60710, host_only=False)


@RestartOnRest(13305763)
def Event_13305763(_, character: int):
    """Event 13305763"""
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(1104):
        return
    SetCharacterTalkRange(character=character, distance=30.0)
    DisableFlag(73300207)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=7.0))
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    OR_1.Add(FlagEnabled(73300207))
    
    MAIN.Await(OR_1)
    
    EnableAI(character)
    ReplanAI(character)
    WaitFrames(frames=1)
    AND_1.Add(CharacterHasSpecialEffect(character, 159))
    SkipLinesIfConditionFalse(2, AND_1)
    ForceAnimation(character, 0, unknown2=1.0)
    WaitFrames(frames=1)
    AND_2.Add(HasAIStatus(character, ai_status=AIStatusType.Normal))
    SkipLinesIfConditionFalse(1, AND_2)
    RotateToFaceEntity(character, PLAYER)
