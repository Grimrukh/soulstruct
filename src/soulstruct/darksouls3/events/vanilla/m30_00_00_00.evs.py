"""
High Wall of Lothric

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
    RegisterBonfire(bonfire_flag=13000009, obj=3001950, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13000003, obj=3001959, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13000005, obj=3001955, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=13000008, obj=3001958, reaction_distance=5.0)
    CommonFunc_20005500(0, flag=13000800, bonfire_flag=13000002, character=3000952, obj=3001952)
    CommonFunc_20005500(0, flag=13000830, bonfire_flag=13000001, character=3000951, obj=3001951)
    CommonFunc_20005500(0, flag=13000890, bonfire_flag=13000004, character=3000954, obj=3001954)
    Event_13000210()
    Event_13000200()
    CommonFunc_20005780(0, obj=3001780, dummy_id=2)
    Event_13005350(0, obj=3001890, dummy_id=3)
    Event_13005810()
    Event_13005811()
    Event_13005815()
    Event_13005820()
    Event_13005812()
    Event_13005817()
    CommonFunc_20005840(0, other_entity=3001800)
    CommonFunc_20005841(0, other_entity=3001800)
    Event_13005825(0, flag=13000825, flag_1=13000800, flag_2=13000896, flag_3=13000890, flag_4=711)
    Event_13005830()
    Event_13005831()
    Event_13005840()
    Event_13005835()
    Event_13005836()
    Event_13005837()
    Event_13005838()
    Event_13005595()
    Event_13005850()
    Event_13005890()
    Event_13005895()
    Event_13005891()
    Event_13005892()
    Event_13005893()
    Event_13005889()
    Event_13005899()
    Event_13005880()
    CommonFunc_20005840(0, other_entity=3001890)
    CommonFunc_20005841(0, other_entity=3001890)
    Event_13005280(0, obj=3001316, vfx_id=830078)
    Event_13005280(1, obj=3001300, vfx_id=830077)
    Event_13005280(2, obj=3001301, vfx_id=830077)
    Event_13005280(3, obj=3001302, vfx_id=830077)
    Event_13005280(4, obj=3001303, vfx_id=830077)
    Event_13005280(5, obj=3001304, vfx_id=830077)
    Event_13005280(6, obj=3001305, vfx_id=830077)
    Event_13005280(7, obj=3001306, vfx_id=830077)
    Event_13005280(8, obj=3001307, vfx_id=830077)
    Event_13005280(9, obj=3001308, vfx_id=830077)
    Event_13005280(10, obj=3001309, vfx_id=830077)
    Event_13005280(11, obj=3001310, vfx_id=830077)
    Event_13005280(12, obj=3001311, vfx_id=830077)
    Event_13005280(13, obj=3001312, vfx_id=830077)
    Event_13005280(14, obj=3001313, vfx_id=830077)
    Event_13005280(15, obj=3001314, vfx_id=830077)
    Event_13005280(16, obj=3001315, vfx_id=830077)
    Event_13005480()
    Event_13005485()
    Event_13005486()
    Event_13005487()
    Event_13005488()
    Event_13005489()
    Event_13005481()
    Event_13005490()
    Event_13005493()
    Event_13005494()
    CommonFunc_20005415(
        0,
        flag=13001500,
        character=3000610,
        character_1=3000611,
        animation_id=702,
        animation_id_1=1702,
        region=3002490,
        flag_1=13005501,
        flag_2=13005502,
    )
    CommonFunc_20005417(
        0,
        flag=13001501,
        character=3000612,
        character_1=3000613,
        animation_id=702,
        animation_id_1=1702,
        region=0,
        flag_1=13005503,
        flag_2=13005504,
        region_1=3002365,
    )
    Event_13005510(0, character=3000610, character_1=3000502, animation_id=20000, seconds=0.20000000298023224)
    Event_13005510(1, character=3000610, character_1=3000509, animation_id=20001, seconds=0.0)
    Event_13005510(2, character=3000610, character_1=3000505, animation_id=20002, seconds=0.699999988079071)
    Event_13005510(3, character=3000610, character_1=3000507, animation_id=20000, seconds=1.0)
    Event_13005510(4, character=3000612, character_1=3000423, animation_id=20000, seconds=0.0)
    Event_13005510(5, character=3000612, character_1=3000421, animation_id=20000, seconds=0.20000000298023224)
    Event_13005510(6, character=3000612, character_1=3000410, animation_id=20001, seconds=0.4000000059604645)
    Event_13005510(7, character=3000612, character_1=3000411, animation_id=20002, seconds=0.6000000238418579)
    Event_13005200(
        0,
        character=3000451,
        animation_id=20001,
        seconds=0.8999999761581421,
        attacked_entity=0,
        attacked_entity_1=3000450,
        attacked_entity_2=3000601,
        attacked_entity_3=3000607,
        attacked_entity_4=3000452,
    )
    Event_13005200(
        1,
        character=3000450,
        animation_id=20000,
        seconds=0.20000000298023224,
        attacked_entity=3000451,
        attacked_entity_1=0,
        attacked_entity_2=3000601,
        attacked_entity_3=3000607,
        attacked_entity_4=3000452,
    )
    Event_13005200(
        2,
        character=3000601,
        animation_id=20001,
        seconds=0.4000000059604645,
        attacked_entity=3000451,
        attacked_entity_1=3000450,
        attacked_entity_2=0,
        attacked_entity_3=3000607,
        attacked_entity_4=3000452,
    )
    Event_13005200(
        3,
        character=3000607,
        animation_id=20001,
        seconds=0.0,
        attacked_entity=3000451,
        attacked_entity_1=3000450,
        attacked_entity_2=3000601,
        attacked_entity_3=0,
        attacked_entity_4=3000452,
    )
    Event_13005200(
        4,
        character=3000452,
        animation_id=20002,
        seconds=0.699999988079071,
        attacked_entity=3000451,
        attacked_entity_1=3000450,
        attacked_entity_2=3000601,
        attacked_entity_3=3000607,
        attacked_entity_4=0,
    )
    Event_13005210(
        0,
        character=3000604,
        animation_id=20001,
        seconds=0.5,
        attacked_entity=3000600,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005210(
        1,
        character=3000600,
        animation_id=20000,
        seconds=0.699999988079071,
        attacked_entity=3000604,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005210(
        2,
        character=3000484,
        animation_id=20002,
        seconds=0.5,
        attacked_entity=3000454,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005210(
        3,
        character=3000454,
        animation_id=20001,
        seconds=0.699999988079071,
        attacked_entity=3000484,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005210(
        4,
        character=3000605,
        animation_id=20002,
        seconds=0.699999988079071,
        attacked_entity=0,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005220(
        1,
        character=3000457,
        animation_id=20001,
        seconds=0.30000001192092896,
        attacked_entity=3000456,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005220(
        2,
        character=3000456,
        animation_id=20000,
        seconds=0.10000000149011612,
        attacked_entity=3000457,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005230(
        0,
        character=3000464,
        animation_id=20002,
        seconds=0.800000011920929,
        attacked_entity=3000463,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005230(
        1,
        character=3000463,
        animation_id=20001,
        seconds=0.30000001192092896,
        attacked_entity=3000464,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005240(
        0,
        character=3000592,
        animation_id=20000,
        seconds=0.0,
        attacked_entity=3000596,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005240(
        1,
        character=3000596,
        animation_id=20002,
        seconds=0.0,
        attacked_entity=3000592,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005240(
        2,
        character=3000533,
        animation_id=20001,
        seconds=0.0,
        attacked_entity=0,
        attacked_entity_1=0,
        attacked_entity_2=0,
        attacked_entity_3=0,
        attacked_entity_4=0,
    )
    Event_13005025()
    Event_13005530()
    Event_13005535()
    CommonFunc_20005119(
        0,
        character=3000230,
        region=3002350,
        region_1=3002221,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3000237,
        region=3002222,
        region_1=3002225,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005350(0, character=3000238, item_lot=12800420, flag=53010980)
    CommonFunc_20005119(
        0,
        character=3000254,
        region=3002226,
        region_1=3002221,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005110(0, character=3000255, region=3002360)
    CommonFunc_20005224(0, character=3000280, animation_id=701, animation_id_1=1701)
    CommonFunc_20005224(0, character=3000281, animation_id=701, animation_id_1=1701)
    CommonFunc_20005119(
        0,
        character=3000300,
        region=3002226,
        region_1=3002221,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005220(0, character=3000350, animation_id=702, animation_id_1=1702)
    CommonFunc_20005224(0, character=3000351, animation_id=702, animation_id_1=1702)
    CommonFunc_20005350(0, character=3000352, item_lot=11901120, flag=53010955)
    CommonFunc_20005202(0, character=3000360, animation_id=701, animation_id_1=1701, region=3002655)
    CommonFunc_20005202(0, character=3000361, animation_id=701, animation_id_1=1701, region=3002655)
    CommonFunc_20005210(0, character=3000409, animation_id=706, animation_id_1=1706, radius=3.0)
    CommonFunc_20005290(0, character=3000410, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3000411, animation_id=702, animation_id_1=1702)
    CommonFunc_20005200(0, character=3000412, animation_id=705, animation_id_1=1705, region=3002390)
    CommonFunc_20005110(0, character=3000418, region=3002431)
    CommonFunc_20005110(0, character=3000419, region=3002391)
    CommonFunc_20005110(0, character=3000420, region=3002223)
    CommonFunc_20005290(0, character=3000421, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3000423, animation_id=700, animation_id_1=1700)
    CommonFunc_20005110(0, character=3000424, region=3002224)
    CommonFunc_20005110(0, character=3000425, region=3002224)
    CommonFunc_20005290(0, character=3000426, animation_id=705, animation_id_1=1705)
    CommonFunc_20005110(0, character=3000427, region=3002341)
    CommonFunc_20005220(0, character=3000430, animation_id=703, animation_id_1=1703)
    CommonFunc_20005122(0, character=3000431, animation_id=3003, radius=6.0)
    CommonFunc_20005220(0, character=3000432, animation_id=706, animation_id_1=1706)
    CommonFunc_20005210(0, character=3000432, animation_id=706, animation_id_1=1706, radius=5.0)
    CommonFunc_20005213(0, character=3000433, animation_id=703, animation_id_1=1703, radius=3.0, region=3002650)
    CommonFunc_20005111(0, character=3000434, animation_id=3011, region=3002380)
    CommonFunc_20005213(0, character=3000435, animation_id=703, animation_id_1=1703, radius=3.0, region=3002425)
    CommonFunc_20005213(0, character=3000436, animation_id=706, animation_id_1=1706, radius=3.0, region=3002425)
    CommonFunc_20005119(
        0,
        character=3000440,
        region=3002226,
        region_1=3002221,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005210(0, character=3000441, animation_id=703, animation_id_1=1703, radius=3.0)
    CommonFunc_20005119(
        0,
        character=3000442,
        region=3002226,
        region_1=3002221,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005290(0, character=3000450, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3000451, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3000452, animation_id=702, animation_id_1=1702)
    CommonFunc_20005290(0, character=3000454, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3000456, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3000457, animation_id=701, animation_id_1=1701)
    CommonFunc_20005110(0, character=3000443, region=3002340)
    CommonFunc_20005290(0, character=3000463, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3000464, animation_id=702, animation_id_1=1702)
    CommonFunc_20005192(0, character=3000471, region=3002441)
    CommonFunc_20005290(0, character=3000473, animation_id=700, animation_id_1=1700)
    CommonFunc_20005205(
        0,
        character=3000477,
        animation_id=710,
        animation_id_1=1710,
        region=3002361,
        seconds=1.100000023841858,
    )
    CommonFunc_20005205(0, character=3000478, animation_id=710, animation_id_1=1710, region=3002361, seconds=1.0)
    CommonFunc_20005119(
        0,
        character=3000482,
        region=3002226,
        region_1=3002221,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005110(0, character=3000483, region=3002340)
    CommonFunc_20005290(0, character=3000484, animation_id=702, animation_id_1=1702)
    CommonFunc_20005290(0, character=3000486, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3000487, animation_id=702, animation_id_1=1702)
    CommonFunc_20005205(
        0,
        character=3000490,
        animation_id=710,
        animation_id_1=1710,
        region=3002361,
        seconds=0.800000011920929,
    )
    CommonFunc_20005205(
        0,
        character=3000492,
        animation_id=710,
        animation_id_1=1710,
        region=3002361,
        seconds=0.4000000059604645,
    )
    CommonFunc_20005220(0, character=3000494, animation_id=703, animation_id_1=1703)
    CommonFunc_20005220(0, character=3000495, animation_id=703, animation_id_1=1703)
    CommonFunc_20005210(0, character=3000496, animation_id=710, animation_id_1=1710, radius=4.5)
    CommonFunc_20005290(0, character=3000500, animation_id=703, animation_id_1=1703)
    CommonFunc_20005290(0, character=3000502, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3000504, animation_id=702, animation_id_1=1702)
    CommonFunc_20005290(0, character=3000505, animation_id=702, animation_id_1=1702)
    CommonFunc_20005290(0, character=3000507, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3000509, animation_id=701, animation_id_1=1701)
    CommonFunc_20005122(0, character=3000511, animation_id=3000, radius=5.0)
    CommonFunc_20005210(0, character=3000520, animation_id=706, animation_id_1=1706, radius=5.5)
    CommonFunc_20005202(0, character=3000522, animation_id=710, animation_id_1=1710, region=3002430)
    CommonFunc_20005111(0, character=3000523, animation_id=3003, region=3002220)
    CommonFunc_20005210(0, character=3000525, animation_id=706, animation_id_1=1706, radius=5.0)
    CommonFunc_20005210(0, character=3000526, animation_id=710, animation_id_1=1710, radius=5.0)
    CommonFunc_20005290(0, character=3000533, animation_id=701, animation_id_1=1701)
    CommonFunc_20005119(
        0,
        character=3000537,
        region=3002480,
        region_1=3002350,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3000538,
        region=3002480,
        region_1=3002350,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005210(0, character=3000539, animation_id=706, animation_id_1=1706, radius=3.0)
    CommonFunc_20005210(0, character=3000540, animation_id=706, animation_id_1=1706, radius=3.0)
    CommonFunc_20005213(0, character=3000545, animation_id=703, animation_id_1=1703, radius=3.0, region=3002362)
    CommonFunc_20005290(0, character=3000551, animation_id=703, animation_id_1=1703)
    CommonFunc_20005290(0, character=3000560, animation_id=703, animation_id_1=1703)
    CommonFunc_20005214(0, character=3000568, animation_id=710, animation_id_1=1710, radius=7.5)
    CommonFunc_20005221(0, character=3000570, animation_id=703, animation_id_1=1703, radius=5.0)
    CommonFunc_20005221(0, character=3000571, animation_id=705, animation_id_1=1705, radius=5.0)
    CommonFunc_20005221(0, character=3000572, animation_id=706, animation_id_1=1706, radius=5.0)
    CommonFunc_20005111(0, character=3000579, animation_id=3000, region=3002245)
    CommonFunc_20005202(0, character=3000580, animation_id=710, animation_id_1=1710, region=3002246)
    CommonFunc_20005290(0, character=3000592, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3000596, animation_id=702, animation_id_1=1702)
    CommonFunc_20005290(0, character=3000600, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=3000601, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3000604, animation_id=701, animation_id_1=1701)
    CommonFunc_20005290(0, character=3000605, animation_id=702, animation_id_1=1702)
    CommonFunc_20005290(0, character=3000607, animation_id=701, animation_id_1=1701)
    CommonFunc_20005119(
        0,
        character=3000615,
        region=3002560,
        region_1=3002561,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=3000616,
        region=3002560,
        region_1=3002561,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005400(0, character=3000620)
    CommonFunc_20000343(0, flag=13000358, character=3000620, flag_1=53000960)
    CommonFunc_20005341(0, flag=13000359, character=3000630, item_lot=21500000)
    CommonFunc_20005110(0, character=3000652, region=3002290)
    CommonFunc_20005110(0, character=3000660, region=3002260)
    CommonFunc_20005110(0, character=3000661, region=3002260)
    CommonFunc_20005110(0, character=3005450, region=3002420)
    CommonFunc_20005192(0, character=3005470, region=3002621)
    CommonFunc_20005410(0, character=3000561, animation_id=3005)
    CommonFunc_20005411(0, character=3000561, character_1=3000560, animation_id=703, animation_id_1=1703, seconds=0.5)
    CommonFunc_20005411(
        0,
        character=3000561,
        character_1=3000407,
        animation_id=706,
        animation_id_1=1706,
        seconds=1.2000000476837158,
    )
    CommonFunc_20005411(
        0,
        character=3000561,
        character_1=3000408,
        animation_id=703,
        animation_id_1=1703,
        seconds=0.4000000059604645,
    )
    CommonFunc_20005411(0, character=3000561, character_1=3000428, animation_id=706, animation_id_1=1706, seconds=0.0)
    CommonFunc_20005410(0, character=3000443, animation_id=3005)
    CommonFunc_20005411(0, character=3000443, character_1=3000444, animation_id=705, animation_id_1=1705, seconds=0.0)
    CommonFunc_20005411(
        0,
        character=3000443,
        character_1=3000426,
        animation_id=705,
        animation_id_1=1705,
        seconds=0.4000000059604645,
    )
    CommonFunc_20005410(0, character=3000400, animation_id=3005)
    CommonFunc_20005411(
        0,
        character=3000400,
        character_1=3000401,
        animation_id=703,
        animation_id_1=1703,
        seconds=2.700000047683716,
    )
    CommonFunc_20005411(0, character=3000400, character_1=3000402, animation_id=705, animation_id_1=1705, seconds=1.5)
    CommonFunc_20005411(0, character=3000400, character_1=3000403, animation_id=706, animation_id_1=1706, seconds=1.0)
    CommonFunc_20005411(
        0,
        character=3000400,
        character_1=3000405,
        animation_id=703,
        animation_id_1=1703,
        seconds=2.0999999046325684,
    )
    CommonFunc_20005411(0, character=3000400, character_1=3000406, animation_id=703, animation_id_1=1703, seconds=2.5)
    Event_13000380(0, character=3000660, item_lot=60940, flag=6780)
    CommonFunc_20005340(0, flag=13000381, character=3000661)
    CommonFunc_20005701(
        0,
        left=13000800,
        summon_flag=13005700,
        dismissal_flag=13005701,
        character=3000190,
        region=3002780,
        left_1=13005392,
    )
    Event_13005826(
        0,
        flag=13005700,
        flag_1=13005805,
        flag_2=13005885,
        character=3000190,
        region=3002800,
        region_1=3002896,
        region_2=3002820,
        region_3=3002870,
        flag_3=13000801,
        flag_4=13000896,
    )
    CommonFunc_20005720(0, flag=13005700, flag_1=13005701, flag_2=13000800, character=3000190)
    CommonFunc_20005714(0, flag=13005700, flag_1=13005805, character=3000190, region=3002829, flag_2=13000801)
    Event_13005390()
    Event_13005391()
    CommonFunc_20005701(
        0,
        left=13000800,
        summon_flag=13005705,
        dismissal_flag=13005706,
        character=3000191,
        region=3002781,
        left_1=9500,
    )
    Event_13005826(
        1,
        flag=13005705,
        flag_1=13005805,
        flag_2=13005885,
        character=3000191,
        region=3002800,
        region_1=3002896,
        region_2=3002820,
        region_3=3002870,
        flag_3=13000801,
        flag_4=13000896,
    )
    CommonFunc_20005720(0, flag=13005705, flag_1=13005706, flag_2=13000800, character=3000191)
    CommonFunc_20005714(0, flag=13005705, flag_1=13005805, character=3000191, region=3002829, flag_2=13000801)
    CommonFunc_20005701(
        0,
        left=13000830,
        summon_flag=13005710,
        dismissal_flag=13005711,
        character=3000192,
        region=3002783,
        left_1=70000007,
    )
    CommonFunc_20005710(0, flag=13005710, flag_1=13005855, character=3000192, region=3002831, region_1=3002840)
    CommonFunc_20005720(0, flag=13005710, flag_1=13005711, flag_2=13000830, character=3000192)
    CommonFunc_20005520(0, flag=13000350, obj=3001350, obj_act_id=3004350)
    CommonFunc_20005520(0, flag=13000351, obj=3001351, obj_act_id=3004351)
    CommonFunc_20005520(0, flag=13000352, obj=3001352, obj_act_id=3004352)
    CommonFunc_20005520(0, flag=13000353, obj=3001353, obj_act_id=3004353)
    CommonFunc_20005520(0, flag=13000354, obj=3001354, obj_act_id=3004354)
    CommonFunc_20005521(0, flag=13000420, flag_1=13005420, obj=3001250, obj_1=3001251, item_lot=3000170)
    CommonFunc_20005525(0, flag=53000650, item_lot=3000650, obj=3001260, dummy_id=61)
    CommonFunc_20005526(0, flag=53000950, item_lot__obj=3000950, obj=3001900, dummy_id=61, flag_1=9480)
    CommonFunc_20005620(0, flag=13000300, flag_1=13000301, entity=3001200, obj=3001201, obj_1=3001202, flag_2=13001300)
    CommonFunc_20005624(0, flag=13000310, flag_1=13000311, entity=3001210, obj=3001211, obj_1=3001212, flag_2=13001310)
    CommonFunc_20005620(0, flag=13000320, flag_1=13000321, entity=3001220, obj=3001221, obj_1=3001222, flag_2=13001320)
    CommonFunc_20005622(0, flag=13000330, flag_1=13000331, entity=3001230, obj=3001231, obj_1=3001232, flag_2=13001330)
    CommonFunc_20005650(0, flag=13000990, obj=3001550)
    Event_13005440()
    Event_13005550()
    CommonFunc_20005610(0, flag=13000450, region=3002460, region_1=3002461)
    CommonFunc_20005611(0, flag=13000450, obj_act_id=3003253, obj=3001410, obj_act_id_1=300310)
    DisableObjectActivation(3001410, obj_act_id=-1, event_layers=[0])
    CommonFunc_20005610(0, flag=13000455, region=3002460, region_1=3002461)
    CommonFunc_20005611(0, flag=13000455, obj_act_id=3003254, obj=3001414, obj_act_id_1=300310)
    DisableObjectActivation(3001414, obj_act_id=-1, event_layers=[9])
    CommonFunc_20005610(0, flag=13000451, region=3002450, region_1=3002451)
    CommonFunc_20005611(0, flag=13000451, obj_act_id=3003302, obj=3001400, obj_act_id_1=300320)
    CommonFunc_20005610(0, flag=13000452, region=3002471, region_1=3002470)
    CommonFunc_20005611(0, flag=13000452, obj_act_id=3003304, obj=3001412, obj_act_id_1=300310)
    CommonFunc_20005611(0, flag=13000453, obj_act_id=3003303, obj=3001411, obj_act_id_1=300312)
    CommonFunc_20005613(0, flag=13000405, obj_act_id=3003309, obj=3001413, obj_act_id_1=-1, text=10010861)
    CommonFunc_20005613(0, flag=13000406, obj_act_id=3003310, obj=3001415, obj_act_id_1=300313, text=10010870)
    Event_13005540()
    DeleteObjectVFX(3001885)
    DeleteObjectVFX(3001886)
    DeleteObjectVFX(3001887)
    DeleteObjectVFX(3001888)
    CreateObjectVFX(3001885, vfx_id=200, dummy_id=800023)
    CreateObjectVFX(3001886, vfx_id=200, dummy_id=800023)
    CreateObjectVFX(3001887, vfx_id=200, dummy_id=800023)
    CreateObjectVFX(3001888, vfx_id=200, dummy_id=800023)
    CommonFunc_20005530(0, obj_flag=13005561, obj=3001619)
    CommonFunc_20005530(0, obj_flag=13005562, obj=3001620)
    CommonFunc_20005530(0, obj_flag=13005563, obj=3001621)
    CommonFunc_20005530(0, obj_flag=13005564, obj=3001622)
    CommonFunc_20005530(0, obj_flag=13005565, obj=3001623)
    CommonFunc_20005530(0, obj_flag=13005566, obj=3001624)
    CommonFunc_20005530(0, obj_flag=13005567, obj=3001625)
    CommonFunc_20005530(0, obj_flag=13005568, obj=3001626)
    CommonFunc_20005530(0, obj_flag=13005569, obj=3001627)
    CommonFunc_20005530(0, obj_flag=13005570, obj=3001628)
    CommonFunc_20005530(0, obj_flag=13005571, obj=3001629)
    CommonFunc_20005530(0, obj_flag=13005572, obj=3001630)
    CommonFunc_20005530(0, obj_flag=13005573, obj=3001631)
    CommonFunc_20005530(0, obj_flag=13005574, obj=3001610)
    CommonFunc_20005530(0, obj_flag=13005575, obj=3001611)
    CommonFunc_20005530(0, obj_flag=13005576, obj=3001612)
    CommonFunc_20005530(0, obj_flag=13005577, obj=3001613)
    CommonFunc_20005530(0, obj_flag=13005578, obj=3001614)
    CommonFunc_20005530(0, obj_flag=13005579, obj=3001632)
    CommonFunc_20005530(0, obj_flag=13005580, obj=3001633)
    CommonFunc_20005530(0, obj_flag=13005581, obj=3001634)
    CommonFunc_20005530(0, obj_flag=13005582, obj=3001635)
    CommonFunc_20005530(0, obj_flag=13005583, obj=3001636)
    CommonFunc_20005530(0, obj_flag=13005584, obj=3001637)
    CommonFunc_20005530(0, obj_flag=13005585, obj=3001638)
    CommonFunc_20005530(0, obj_flag=13005586, obj=3001639)
    CommonFunc_20005530(0, obj_flag=13005587, obj=3001640)
    CommonFunc_20005530(0, obj_flag=13005588, obj=3001641)
    CommonFunc_20005530(0, obj_flag=13005360, obj=3001600)
    CommonFunc_20005530(0, obj_flag=13005361, obj=3001601)
    CommonFunc_20005530(0, obj_flag=13005362, obj=3001602)
    CommonFunc_20005530(0, obj_flag=13005363, obj=3001603)
    CommonFunc_20005530(0, obj_flag=13005364, obj=3001604)
    CommonFunc_20005530(0, obj_flag=13005365, obj=3001605)
    CommonFunc_20005530(0, obj_flag=13005366, obj=3001606)
    CommonFunc_20005530(0, obj_flag=13005367, obj=3001607)
    CommonFunc_20005540(
        0,
        obj_flag=13005630,
        obj=3001510,
        dummy_id=200,
        behavior_param_id=5110,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13005631,
        obj=3001511,
        dummy_id=200,
        behavior_param_id=5110,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13005632,
        obj=3001512,
        dummy_id=200,
        behavior_param_id=5110,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    CommonFunc_20005540(
        0,
        obj_flag=13005633,
        obj=3001513,
        dummy_id=200,
        behavior_param_id=5110,
        radius=0.5,
        life=0.0,
        repetition_time=1.0,
    )
    RegisterLadder(start_climbing_flag=13000250, stop_climbing_flag=13000251, obj=3001080)
    RegisterLadder(start_climbing_flag=13000252, stop_climbing_flag=13000253, obj=3001081)
    RegisterLadder(start_climbing_flag=13000254, stop_climbing_flag=13000255, obj=3001082)
    RegisterLadder(start_climbing_flag=13000256, stop_climbing_flag=13000257, obj=3001083)
    RegisterLadder(start_climbing_flag=13000258, stop_climbing_flag=13000259, obj=3001084)
    RegisterLadder(start_climbing_flag=13000260, stop_climbing_flag=13000261, obj=3001085)
    RegisterLadder(start_climbing_flag=13000262, stop_climbing_flag=13000263, obj=3001086)
    Event_13000230()
    CommonFunc_20005523(0, obj=3001270, completion_count=1)
    CommonFunc_20005523(0, obj=3001271, completion_count=1)
    CommonFunc_20005523(0, obj=3001272, completion_count=2)
    CommonFunc_20005523(0, obj=3001273, completion_count=2)
    CommonFunc_20006003(
        0,
        character=3000700,
        flag=73000132,
        flag_1=1215,
        flag_2=1200,
        flag_3=1201,
        first_flag=1200,
        last_flag=1214,
    )
    CommonFunc_20006002(0, character=3000700, flag=1218, first_flag=1215, last_flag=1219)
    CommonFunc_20006000(
        0,
        character=3000700,
        flag=1216,
        flag_1=1217,
        flag_2=73000130,
        value=0.6499999761581421,
        first_flag=1215,
        last_flag=1219,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=3000700, flag=1216, flag_1=1217, flag_2=73000130, right=3)
    Event_13005601(0, flag=73000181)
    Event_13005602(0, entity=3000705, flag=73000180)
    Event_13005603(0, attacked_entity=3000705)
    CommonFunc_20006002(0, character=3000705, flag=1438, first_flag=1435, last_flag=1439)
    Event_13005604()
    Event_13005560()
    Event_13000360()
    Event_13000901(0, obj=3001900)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_13000410()
    Event_13005861()
    Event_13005590()
    SetMultiplayerBuffs_NonBoss(character=3000850, state=True)
    Event_13005620(0, character=3000700)
    Event_13005600(0, character__obj=3000705, obj=3001875, obj_1=3001876)
    Event_13005640(0, character=3000830)
    DisableSoundEvent(sound_id=3002805)
    DisableSoundEvent(sound_id=3002806)
    DisableSoundEvent(sound_id=3002835)
    DisableSoundEvent(sound_id=3002836)
    DisableSoundEvent(sound_id=3002898)
    DisableSoundEvent(sound_id=3002899)


@ContinueOnRest(13000200)
def Event_13000200():
    """Event 13000200"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=3002550))
    
    EnableFlag(13000201)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableFlag(13000201)


@ContinueOnRest(13000210)
def Event_13000210():
    """Event 13000210"""
    if FlagEnabled(13000009):
        return
    
    MAIN.Await(FlagEnabled(13000009))
    
    DisableFlag(13000000)


@ContinueOnRest(13000230)
def Event_13000230():
    """Event 13000230"""
    if ThisEventSlotFlagEnabled():
        return
    DisableSoapstoneMessage(3002280)
    
    MAIN.Await(PlayerHasGood(2117, including_storage=True))
    
    EnableSoapstoneMessage(3002280)


@ContinueOnRest(13000360)
def Event_13000360():
    """Event 13000360"""
    if PlayerNotInOwnWorld():
        return
    DisableNetworkSync()
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(711))
    
    ForceAnimation(PLAYER, 63010, unknown2=1.0)
    CreateTemporaryVFX(vfx_id=30300, anchor_entity=PLAYER, dummy_id=245, anchor_type=CoordEntityType.Character)
    CreateObjectVFX(3001705, vfx_id=90, dummy_id=830095)
    EnableFlag(13000360)
    Wait(10.0)
    DeleteObjectVFX(3001705)


@ContinueOnRest(13000380)
def Event_13000380(_, character: int, item_lot: int, flag: int):
    """Event 13000380"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(ThisEventSlotFlagEnabled())
    AND_1.Add(FlagEnabled(flag))
    if AND_1:
        return
    
    MAIN.Await(CharacterDead(character))
    
    AwardItemLot(item_lot, host_only=True)
    End()


@ContinueOnRest(13000410)
def Event_13000410():
    """Event 13000410"""
    if ThisEventSlotFlagEnabled():
        return
    EnableFlag(13000300)
    EnableFlag(13000310)
    End()


@RestartOnRest(13005025)
def Event_13005025():
    """Event 13005025"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(3000404, 703, loop=True, unknown2=1.0)
    DisableAI(3000404)
    OR_1.Add(ObjectDestroyed(3001250))
    OR_2.Add(Attacked(attacked_entity=3000404, attacker=PLAYER))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    
    MAIN.Await(OR_3)
    
    OR_1.Add(ObjectDestroyed(3001250))
    OR_2.Add(Attacked(attacked_entity=3000404, attacker=PLAYER))
    SkipLinesIfConditionTrue(2, OR_2)
    ForceAnimation(3000404, 1703, wait_for_completion=True, unknown2=1.0)
    EnableAI(3000404)


@RestartOnRest(13005200)
def Event_13005200(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005200"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000427, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000427, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000443, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000443, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000426, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000426, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000483, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000483, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3005500, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_6.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(13005210)
def Event_13005210(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005210"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000427, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000427, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000443, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000443, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000426, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000426, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000483, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000483, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3005500, ai_status=AIStatusType.Battle))
    AND_6.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    AND_7.Add(CharacterHasTAEEvent(3000443, tae_event_id=20))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(13005220)
def Event_13005220(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005220"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000427, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000427, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000443, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000443, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000426, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000426, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000483, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000483, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3000561, ai_status=AIStatusType.Battle))
    AND_6.Add(EntityWithinDistance(entity=3000561, other_entity=character, radius=3.5))
    AND_7.Add(HasAIStatus(3000408, ai_status=AIStatusType.Battle))
    AND_7.Add(EntityWithinDistance(entity=3000408, other_entity=character, radius=3.5))
    AND_8.Add(HasAIStatus(3000560, ai_status=AIStatusType.Battle))
    AND_8.Add(EntityWithinDistance(entity=3000560, other_entity=character, radius=3.5))
    AND_9.Add(HasAIStatus(3000579, ai_status=AIStatusType.Battle))
    AND_9.Add(EntityWithinDistance(entity=3000579, other_entity=character, radius=3.5))
    AND_10.Add(HasAIStatus(3000428, ai_status=AIStatusType.Battle))
    AND_10.Add(EntityWithinDistance(entity=3000428, other_entity=character, radius=3.5))
    AND_11.Add(HasAIStatus(3005501, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_11.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    OR_2.Add(AND_9)
    OR_2.Add(AND_10)
    OR_2.Add(AND_11)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(13005230)
def Event_13005230(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005230"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000418, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000418, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000522, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000522, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000471, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000471, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000494, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000494, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3000488, ai_status=AIStatusType.Battle))
    AND_6.Add(EntityWithinDistance(entity=3000488, other_entity=character, radius=3.5))
    AND_7.Add(HasAIStatus(3000230, ai_status=AIStatusType.Battle))
    AND_7.Add(EntityWithinDistance(entity=3000230, other_entity=character, radius=3.5))
    AND_8.Add(HasAIStatus(3005502, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_8.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    OR_2.Add(AND_8)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(13005240)
def Event_13005240(
    _,
    character: int,
    animation_id: int,
    seconds: float,
    attacked_entity: int,
    attacked_entity_1: int,
    attacked_entity_2: int,
    attacked_entity_3: int,
    attacked_entity_4: int,
):
    """Event 13005240"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(1.0)
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_2, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_3, attacker=PLAYER))
    OR_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity_4, attacker=PLAYER))
    AND_1.Add(EntityWithinDistance(entity=character, other_entity=PLAYER, radius=1.0))
    AND_2.Add(HasAIStatus(3000255, ai_status=AIStatusType.Battle))
    AND_2.Add(EntityWithinDistance(entity=3000255, other_entity=character, radius=3.5))
    AND_3.Add(HasAIStatus(3000520, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=3000520, other_entity=character, radius=3.5))
    AND_4.Add(HasAIStatus(3000253, ai_status=AIStatusType.Battle))
    AND_4.Add(EntityWithinDistance(entity=3000253, other_entity=character, radius=3.5))
    AND_5.Add(HasAIStatus(3000242, ai_status=AIStatusType.Battle))
    AND_5.Add(EntityWithinDistance(entity=3000242, other_entity=character, radius=3.5))
    AND_6.Add(HasAIStatus(3000245, ai_status=AIStatusType.Battle))
    AND_6.Add(EntityWithinDistance(entity=3000245, other_entity=character, radius=3.5))
    AND_7.Add(HasAIStatus(3005503, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_7.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=3.5))
    OR_2.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    OR_2.Add(AND_6)
    OR_2.Add(AND_7)
    
    MAIN.Await(OR_2)
    
    Wait(seconds)
    GotoIfCharacterDoesNotHaveSpecialEffect(Label.L0, character=character, special_effect=5450)
    ForceAnimation(character, animation_id, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@ContinueOnRest(13005280)
def Event_13005280(_, obj: int, vfx_id: int):
    """Event 13005280"""
    AND_1.Add(ObjectBurnState(obj=obj, comparison_type=ComparisonType.GreaterThan, state=False))
    AND_1.Add(FlagEnabled(13000890))
    
    MAIN.Await(AND_1)
    
    CreateTemporaryVFX(vfx_id=vfx_id, anchor_entity=obj, dummy_id=200, anchor_type=CoordEntityType.Object)


@RestartOnRest(13005350)
def Event_13005350(_, obj: int, dummy_id: int):
    """Event 13005350"""
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(13000890))
    
    DisableObject(obj)
    DeleteObjectVFX(obj)
    OR_1.Add(TryingToJoinSession())
    OR_1.Add(TryingToCreateSession())
    
    MAIN.Await(OR_1)
    
    EnableObject(obj)
    CreateObjectVFX(obj, vfx_id=101, dummy_id=dummy_id)
    OR_2.Add(TryingToJoinSession())
    OR_2.Add(TryingToCreateSession())
    
    MAIN.Await(not OR_2)
    
    Restart()


@RestartOnRest(13005390)
def Event_13005390():
    """Event 13005390"""
    if FlagEnabled(13000800):
        return
    AND_1.Add(PlayerHasGood(2117, including_storage=True))
    if AND_1:
        return
    EnableFlag(13005392)
    
    MAIN.Await(PlayerHasGood(2117, including_storage=True))
    
    DisableFlag(13005392)


@RestartOnRest(13005391)
def Event_13005391():
    """Event 13005391"""
    if FlagEnabled(13000800):
        return
    AND_1.Add(PlayerHasGood(2117, including_storage=True))
    if AND_1:
        return
    AND_2.Add(PlayerHasGood(2117, including_storage=True))
    AND_2.Add(FlagEnabled(13005700))
    
    MAIN.Await(AND_2)
    
    ForceAnimation(3000190, 91030, unknown2=1.0)
    Wait(2.0)
    SendNPCSummonHome(character=3000190)


@RestartOnRest(13005480)
def Event_13005480():
    """Event 13005480"""
    DisableCharacter(3000850)
    DisableGravity(3000850)
    DisableAI(3000850)
    SetLockOnPoint(character=3000850, lock_on_dummy_id=220, state=False)
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    GotoIfFlagDisabled(Label.L0, flag=13000480)
    EnableCharacter(3000850)
    Move(3000850, destination=3002600, destination_type=CoordEntityType.Region, short_move=True)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableImmortality(3000850)
    if ThisEventSlotFlagEnabled():
        return
    RemoveSpecialEffect(3000850, 11000)
    AddSpecialEffect(3000850, 11004)
    ForceAnimation(3000850, 30002, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_1.Add(CharacterIsHuman(PLAYER))
    OR_1.Add(CharacterIsHollow(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002620))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    AND_3.Add(FlagEnabled(13000480))
    AND_4.Add(FlagEnabled(13000481))
    AND_5.Add(FlagEnabled(9420))
    OR_2.Add(AND_2)
    OR_2.Add(AND_3)
    OR_2.Add(AND_4)
    OR_2.Add(AND_5)
    
    MAIN.Await(OR_2)
    
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_4)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_5)
    Move(3000850, destination=3002600, destination_type=CoordEntityType.Region, short_move=True)
    EnableCharacter(3000850)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(3000850, 20003, skip_transition=True, unknown2=1.0)
    EnableFlag(13000480)
    EnableImmortality(3000850)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(3000850)
    DisableGravity(3000850)
    DisableAI(3000850)
    SetLockOnPoint(character=3000850, lock_on_dummy_id=220, state=False)


@RestartOnRest(13005481)
def Event_13005481():
    """Event 13005481"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_1.Add(HealthRatio(3000850) <= 0.20000000298023224)
    AND_2.Add(FlagEnabled(9420))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_2)
    GotoIfPlayerNotInOwnWorld(Label.L0)
    AwardItemLot(31410000, host_only=False)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3000850, 20007, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    DisableCharacter(3000850)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Never)
    EnableFlag(13000481)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(3000850)
    SetNetworkUpdateRate(3000850, is_fixed=True, update_rate=CharacterUpdateRate.Never)


@RestartOnRest(13005485)
def Event_13005485():
    """Event 13005485"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    GotoIfFlagEnabled(Label.L0, flag=13000480)
    if ThisEventSlotFlagEnabled():
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsHuman(PLAYER))
    OR_1.Add(CharacterIsHollow(PLAYER))
    OR_1.Add(CharacterIsWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002621))
    AND_2.Add(CharacterHasSpecialEffect(3000850, 11000))
    AND_2.Add(CharacterHasSpecialEffect(3000850, 11001))
    AND_3.Add(OR_1)
    AND_3.Add(AND_1)
    AND_3.Add(AND_2)
    
    MAIN.Await(AND_3)
    
    RemoveSpecialEffect(3000850, 11000)
    ForceAnimation(3000850, 20001, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(3000850, 11000)
    ForceAnimation(3000850, 30002, skip_transition=True, unknown2=1.0)
    End()


@RestartOnRest(13005486)
def Event_13005486():
    """Event 13005486"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsHuman(PLAYER))
    OR_1.Add(CharacterIsHollow(PLAYER))
    OR_1.Add(CharacterIsWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002617))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3000850, 11003)
    Wait(3.0)
    Restart()


@RestartOnRest(13005487)
def Event_13005487():
    """Event 13005487"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsHuman(PLAYER))
    OR_1.Add(CharacterIsHollow(PLAYER))
    OR_1.Add(CharacterIsWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002610))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002611))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3000850, 11004)
    Wait(3.0)
    Restart()


@RestartOnRest(13005488)
def Event_13005488():
    """Event 13005488"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsHuman(PLAYER))
    OR_1.Add(CharacterIsHollow(PLAYER))
    OR_1.Add(CharacterIsWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002615))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002616))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(3000850, 11004)
    Wait(3.0)
    Restart()


@RestartOnRest(13005489)
def Event_13005489():
    """Event 13005489"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsHuman(PLAYER))
    OR_1.Add(CharacterIsHollow(PLAYER))
    OR_1.Add(CharacterIsWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002630))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(3000850, 11005)
    Wait(3.0)
    Restart()


@RestartOnRest(13005490)
def Event_13005490():
    """Event 13005490"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsHuman(PLAYER))
    OR_1.Add(CharacterIsHollow(PLAYER))
    OR_1.Add(CharacterIsWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002640))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002642))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=3002641))
    OR_3.Add(CharacterInsideRegion(character=PLAYER, region=3002643))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3000850, 11006)
    Wait(3.0)
    Restart()


@RestartOnRest(13005493)
def Event_13005493():
    """Event 13005493"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=3000850, attacker=PLAYER))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002644))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002645))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002646))
    AND_2.Add(AND_1)
    AND_2.Add(OR_1)
    
    MAIN.Await(AND_2)
    
    AddSpecialEffect(3000850, 11010)
    Restart()


@RestartOnRest(13005494)
def Event_13005494():
    """Event 13005494"""
    if FlagEnabled(13000481):
        return
    if FlagEnabled(9420):
        return
    AND_1.Add(AttackedWithDamageType(attacked_entity=3000850, attacker=PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002647))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(3000850, 11011)
    Restart()


@RestartOnRest(13005510)
def Event_13005510(_, character: int, character_1: int, animation_id: int, seconds: float):
    """Event 13005510"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterHasTAEEvent(character, tae_event_id=100))
    
    Wait(seconds)
    AND_1.Add(CharacterHasSpecialEffect(character_1, 5450))
    AND_1.Add(CharacterAlive(character_1))
    if not AND_1:
        return
    ForceAnimation(character_1, animation_id, unknown2=1.0)
    ReplanAI(character_1)


@RestartOnRest(13005530)
def Event_13005530():
    """Event 13005530"""
    if ThisEventSlotFlagEnabled():
        return
    Wait(5.0)
    Move(3000496, destination=3002500, destination_type=CoordEntityType.Region, short_move=True)
    Move(3000580, destination=3002501, destination_type=CoordEntityType.Region, short_move=True)
    Move(3000526, destination=3002502, destination_type=CoordEntityType.Region, short_move=True)
    Move(3000522, destination=3002503, destination_type=CoordEntityType.Region, short_move=True)


@RestartOnRest(13005535)
def Event_13005535():
    """Event 13005535"""
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(3000488)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterIsHuman(PLAYER))
    OR_1.Add(CharacterIsHollow(PLAYER))
    OR_1.Add(CharacterIsWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002381))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=3002382))
    OR_3.Add(Attacked(attacked_entity=3000488, attacker=PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    
    MAIN.Await(AND_1)
    
    MAIN.Await(OR_3)
    
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3002381))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=3002382))
    OR_4.Add(Attacked(attacked_entity=3000488, attacker=PLAYER))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    GotoIfConditionTrue(Label.L1, input_condition=OR_4)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3000488, 3004, skip_transition=True, unknown2=1.0)
    EnableAI(3000488)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(3000488)
    End()


@RestartOnRest(13005540)
def Event_13005540():
    """Event 13005540"""
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002510))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=3002511))
    
    MAIN.Await(OR_1)
    
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002510))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3002511))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetAreaWelcomeMessageState(state=False)


@RestartOnRest(13005550)
def Event_13005550():
    """Event 13005550"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=3001810, entity=3001650))
    
    AND_1.Add(PlayerHasGood(2102))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    DisplayDialog(text=10012001)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfLeavingSession(2)
    DisplayDialog(text=10010170)
    Restart()
    if FlagDisabled(13100331):
        PlayCutsceneAndMovePlayerAndSetMapCeremony(
            cutscene=31000010,
            cutscene_flags=0,
            ceremony_id=0,
            unknown=1,
            move_to_region=3102515,
            game_map=UNDEAD_SETTLEMENT,
            player_id=10000,
        )
    else:
        WarpToMap(game_map=UNDEAD_SETTLEMENT, player_start=3100974)
    EnableFlag(13100330)
    WaitFrames(frames=1)
    SetRespawnPoint(respawn_point=3102515)
    SaveRequest()
    Restart()


@RestartOnRest(13005560)
def Event_13005560():
    """Event 13005560"""
    GotoIfFlagEnabled(Label.L0, flag=711)
    DisableObject(3001872)
    DisableObject(3001874)
    EnableObject(3001871)
    EnableObject(3001873)
    
    MAIN.Await(FlagEnabled(711))

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(3001872)
    EnableObject(3001874)
    DisableObject(3001871)
    DisableObject(3001873)


@RestartOnRest(13005590)
def Event_13005590():
    """Event 13005590"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(3006450)


@RestartOnRest(13005595)
def Event_13005595():
    """Event 13005595"""
    OR_1.Add(CharacterIsHuman(PLAYER))
    OR_1.Add(CharacterIsHollow(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002680))
    AND_2.Add(OR_1)
    AND_2.Add(AND_1)
    
    MAIN.Await(AND_2)
    
    PlaySoundEffect(3002681, 300000010, sound_type=SoundType.a_Ambient)


@RestartOnRest(13005440)
def Event_13005440():
    """Event 13005440"""
    CommonFunc_20005621(
        0,
        flag=13000300,
        flag_1=13000301,
        obj=3001200,
        obj_1=3001201,
        obj_act_id=3004201,
        obj_2=3001202,
        obj_act_id_1=3004202,
        region=3002301,
        region_1=3002302,
        flag_2=13001300,
        flag_3=13004300,
        left=0,
    )
    CommonFunc_20005625(
        0,
        flag=13000310,
        flag_1=13000311,
        obj=3001210,
        obj_1=3001211,
        obj_act_id=3004211,
        obj_2=3001212,
        obj_act_id_1=3004212,
        region=3002311,
        region_1=3002312,
        flag_2=13001310,
        flag_3=13004310,
        left=0,
    )
    CommonFunc_20005621(
        0,
        flag=13000320,
        flag_1=13000321,
        obj=3001220,
        obj_1=3001221,
        obj_act_id=3004221,
        obj_2=3001222,
        obj_act_id_1=3004222,
        region=3002321,
        region_1=3002322,
        flag_2=13001320,
        flag_3=13004320,
        left=0,
    )
    CommonFunc_20005623(
        0,
        flag=13000330,
        flag_1=13000331,
        obj=3001230,
        obj_1=3001231,
        obj_act_id=3004231,
        obj_2=3001232,
        obj_act_id_1=3004232,
        region=3002331,
        region_1=3002332,
        flag_2=13001330,
        flag_3=13004330,
        left=0,
    )


@RestartOnRest(13005810)
def Event_13005810():
    """Event 13005810"""
    DisableAI(3000800)
    DisableHealthBar(3000800)
    DisableCharacter(3000800)
    if FlagEnabled(13000800):
        return
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    GotoIfThisEventSlotFlagEnabled(Label.L2)
    GotoIfFlagEnabled(Label.L1, flag=13000801)
    Move(3000800, destination=3002811, destination_type=CoordEntityType.Region, short_move=True)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002815))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_15:
        return

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L2, flag=13000801)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(30000030, cutscene_flags=0, player_id=10000, move_to_region=3002810, game_map=HIGH_WALL_OF_LOTHRIC)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        30000030,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3002810,
        game_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(1)
    PlayCutscene(30000030, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(3000800)
    AND_3.Add(FlagDisabled(13000800))
    AND_3.Add(CharacterInsideRegion(character=PLAYER, region=3002801))
    
    MAIN.Await(AND_3)
    
    ForceAnimation(3000800, 3030, unknown2=1.0)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableCharacter(3000800)
    EnableAI(3000800)
    SetNetworkUpdateRate(3000800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3000800, name=902240)
    SetNetworkConnectedFlagState(flag=13000801, state=FlagSetting.On)


@ContinueOnRest(13005811)
def Event_13005811():
    """Event 13005811"""
    if FlagEnabled(13000800):
        return
    
    MAIN.Await(HealthRatio(3000800) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(3000800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3000800))
    
    Wait(3.5)
    KillBoss(game_area_param_id=3000800)
    DisableSoundEvent(sound_id=3002805)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    EnableFlag(13000800)
    EnableFlag(9301)
    EnableFlag(6301)


@RestartOnRest(13005812)
def Event_13005812():
    """Event 13005812"""
    GotoIfFlagEnabled(Label.L0, flag=13000800)
    
    MAIN.Await(FlagEnabled(13000800))
    
    Wait(2.0)
    ForceAnimation(3001815, 1, skip_transition=True, unknown2=1.0)
    Wait(7.5)
    CreateObjectVFX(3001815, vfx_id=100, dummy_id=830101)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3001815, 2, loop=True, unknown2=1.0)
    CreateObjectVFX(3001815, vfx_id=100, dummy_id=830101)


@RestartOnRest(13005815)
def Event_13005815():
    """Event 13005815"""
    if FlagEnabled(13000800):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000800, tae_event_id=10))
    
    End()


@RestartOnRest(13005817)
def Event_13005817():
    """Event 13005817"""
    if FlagEnabled(13000800):
        return
    DisableNetworkSync()
    AND_1.Add(FlagEnabled(13005805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002801))
    
    MAIN.Await(AND_1)
    
    ChangeCamera(normal_camera_id=3300, locked_camera_id=3300)


@RestartOnRest(13005820)
def Event_13005820():
    """Event 13005820"""
    CommonFunc_20005800(
        0,
        flag=13000800,
        entity=3001800,
        region=3002800,
        flag_1=13005805,
        action_button_id=3001800,
        character=3000800,
        left=13000801,
        region_1=0,
    )
    CommonFunc_20005801(
        0,
        flag=13000800,
        entity=3001800,
        region=3002800,
        flag_1=13005805,
        action_button_id=3001800,
        flag_2=13005806,
    )
    CommonFunc_20005820(0, flag=13000800, obj=3001800, dummy_id=3, left=13000801)
    if FlagDisabled(13000801):
        CommonFunc_20001836(
            0,
            flag=13000800,
            flag_1=13005805,
            flag_2=13005806,
            flag_3=13005810,
            sound_id=3002805,
            sound_id_1=3002806,
            flag_4=13005815,
        )
    else:
        CommonFunc_20005831(
            0,
            flag=13000800,
            flag_1=13005805,
            flag_2=13005806,
            region=3002800,
            sound_id=3002805,
            sound_id_1=3002806,
            flag_3=13005815,
        )
    CommonFunc_20005810(0, flag=13000825, entity=3001800, target_entity=3002800, action_button_id=10000)


@RestartOnRest(13005825)
def Event_13005825(_, flag: int, flag_1: int, flag_2: int, flag_3: int, flag_4: int):
    """Event 13005825"""
    GotoIfThisEventSlotFlagDisabled(Label.L0)
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_1))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_2))
    OR_1.Add(FlagState(FlagSetting.Change, FlagType.Absolute, flag_3))
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(FlagEnabled(flag_1))
    AND_1.Add(FlagEnabled(flag_3))
    GotoIfConditionTrue(Label.L2, input_condition=AND_1)
    AND_2.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagDisabled(flag_2))
    AND_2.Add(FlagDisabled(flag_4))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    AND_3.Add(FlagDisabled(flag_1))
    GotoIfConditionTrue(Label.L1, input_condition=AND_3)
    AND_4.Add(FlagEnabled(flag_1))
    AND_4.Add(FlagEnabled(flag_2))
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)
    AND_5.Add(FlagEnabled(flag_1))
    AND_5.Add(FlagEnabled(flag_4))
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)

    # --- Label 1 --- #
    DefineLabel(1)
    DisableFlag(flag)
    Wait(5.0)
    Restart()

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(flag)
    Wait(5.0)
    Restart()


@RestartOnRest(13005826)
def Event_13005826(
    _,
    flag: int,
    flag_1: int,
    flag_2: int,
    character: int,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    flag_3: int,
    flag_4: int,
):
    """Event 13005826"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(flag_1))
    AND_2.Add(FlagEnabled(flag))
    AND_2.Add(FlagEnabled(flag_2))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=AND_2)
    AICommand(character, command_id=10, command_slot=0)
    ReplanAI(character)
    AND_2.Add(CharacterInsideRegion(character=character, region=region_2))
    AND_2.Add(FlagEnabled(flag_3))
    
    MAIN.Await(AND_2)
    
    FaceEntity(character, region, animation=60060, wait_for_completion=True)
    OR_10.Add(CharacterInsideRegion(character=character, region=region))
    OR_11.Add(TimeElapsed(seconds=3.0))
    OR_10.Add(OR_11)
    
    MAIN.Await(OR_10)
    
    RestartIfLastConditionResultTrue(input_condition=OR_11)
    AICommand(character, command_id=-1, command_slot=0)
    AICommand(character, command_id=50, command_slot=3)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AICommand(character, command_id=11, command_slot=0)
    ReplanAI(character)
    AND_2.Add(CharacterInsideRegion(character=character, region=region_3))
    AND_2.Add(FlagEnabled(flag_4))
    
    MAIN.Await(AND_2)
    
    FaceEntity(character, region_1, animation=60060, wait_for_completion=True)
    OR_12.Add(CharacterInsideRegion(character=character, region=region_1))
    OR_13.Add(TimeElapsed(seconds=3.0))
    OR_12.Add(OR_13)
    
    MAIN.Await(OR_12)
    
    RestartIfLastConditionResultTrue(input_condition=OR_13)
    AICommand(character, command_id=-1, command_slot=0)
    ReplanAI(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()


@RestartOnRest(13005830)
def Event_13005830():
    """Event 13005830"""
    DisableAI(3000830)
    DisableHealthBar(3000830)
    DisableCharacter(3000830)
    DisableSoundEvent(sound_id=3002835)
    if FlagEnabled(13000830):
        return
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    GotoIfFlagEnabled(Label.L0, flag=13000838)
    AND_1.Add(FlagDisabled(13000830))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002830))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=13000838)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(30000040, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(30000040, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(30000040, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacter(3000830)
    AND_2.Add(FlagDisabled(13000830))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=3002830))
    
    MAIN.Await(AND_2)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableCharacter(3000830)
    EnableAI(3000830)
    SetNetworkUpdateRate(3000830, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(3000830, name=902090)
    DisableObjectActivation(3001813, obj_act_id=300371)
    SetNetworkConnectedFlagState(flag=13000838, state=FlagSetting.On)


@ContinueOnRest(13005831)
def Event_13005831():
    """Event 13005831"""
    if FlagEnabled(13000830):
        return
    
    MAIN.Await(HealthRatio(3000830) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(3000830, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3000830))
    
    Wait(3.5)
    KillBoss(game_area_param_id=3000830)
    EnableFlag(13000830)
    EnableFlag(9302)
    EnableFlag(6302)
    WaitFrames(frames=1)
    EnableObjectActivation(3001813, obj_act_id=300371)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)


@RestartOnRest(13005835)
def Event_13005835():
    """Event 13005835"""
    if FlagEnabled(13000830):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000830, tae_event_id=10))
    
    WaitFrames(frames=1)
    End()


@RestartOnRest(13005836)
def Event_13005836():
    """Event 13005836"""
    if FlagEnabled(13000830):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000830, tae_event_id=20))
    
    EnableFlag(73000202)
    WaitFrames(frames=1)
    End()


@RestartOnRest(13005837)
def Event_13005837():
    """Event 13005837"""
    if FlagEnabled(13000830):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000830, tae_event_id=20))
    
    CreateNPCPart(3000830, npc_part_id=10, part_index=NPCPartType.Part6, part_health=193)


@RestartOnRest(13005838)
def Event_13005838():
    """Event 13005838"""
    if FlagEnabled(13000830):
        return
    AND_1.Add(CharacterHasSpecialEffect(3000830, 5404))
    AND_1.Add(CharacterPartHealth(3000830, npc_part_id=10) <= 0)
    AND_1.Add(FlagEnabled(13005837))
    
    MAIN.Await(AND_1)
    
    ForceAnimation(3000830, 20000, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    CreateNPCPart(3000830, npc_part_id=10, part_index=NPCPartType.Part6, part_health=193)
    Restart()


@RestartOnRest(13005840)
def Event_13005840():
    """Event 13005840"""
    CommonFunc_20005800(
        0,
        flag=13000830,
        entity=3001830,
        region=3002831,
        flag_1=13005855,
        action_button_id=3001830,
        character=3000830,
        left=0,
        region_1=3002830,
    )
    CommonFunc_20005801(
        0,
        flag=13000830,
        entity=3001830,
        region=3002831,
        flag_1=13005855,
        action_button_id=3001830,
        flag_2=13005856,
    )
    CommonFunc_20005820(0, flag=13000830, obj=3001830, dummy_id=3, left=0)
    CommonFunc_20001836(
        0,
        flag=13000830,
        flag_1=13005855,
        flag_2=13005856,
        flag_3=13005830,
        sound_id=3002835,
        sound_id_1=3002836,
        flag_4=13005835,
    )
    CommonFunc_20005837(
        0,
        flag=13000830,
        entity=3001830,
        radius=999.0,
        normal_camera_id=2090,
        locked_camera_id=2090,
        flag_1=13005855,
        flag_2=13005856,
    )
    CommonFunc_20005810(0, flag=13000830, entity=3001830, target_entity=3002831, action_button_id=10000)
    CommonFunc_20005810(0, flag=13000825, entity=3001890, target_entity=3002896, action_button_id=10000)


@RestartOnRest(13005850)
def Event_13005850():
    """Event 13005850"""
    if FlagEnabled(13000830):
        return
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3002850))
    
    if FlagEnabled(13000830):
        return
    SetBackgroundMusic(True, music_slot=0, entity=3002850, sound_type=SoundType.a_Ambient, sound_id=300000020)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=3002850))
    
    SetBackgroundMusic(False, music_slot=0, entity=3002850, sound_type=SoundType.a_Ambient, sound_id=300000020)
    Restart()


@RestartOnRest(13005861)
def Event_13005861():
    """Event 13005861"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(13005862)
    
    MAIN.Await(FailedToCreateSession())
    
    EnableFlag(13005862)
    AND_1.Add(FailedToCreateSession())
    
    MAIN.Await(not AND_1)
    
    DisableFlag(13005862)
    Wait(1.0)
    Restart()


@RestartOnRest(13005880)
def Event_13005880():
    """Event 13005880"""
    GotoIfFlagEnabled(Label.L0, flag=13000885)
    ForceAnimation(3001087, 0, loop=True, unknown2=1.0)
    DisableObject(3001870)
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(FlagEnabled(13000890))
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=3001895, entity=3001896))
    
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(30000020, cutscene_flags=0, player_id=10000, move_to_region=3002880, game_map=HIGH_WALL_OF_LOTHRIC)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        30000020,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3002880,
        game_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(1)
    PlayCutscene(30000020, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    RemoveGoodFromPlayer(item=2117, quantity=1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3001087, 10, loop=True, unknown2=1.0)
    EnableObject(3001870)
    RegisterLadder(start_climbing_flag=13000264, stop_climbing_flag=13000265, obj=3001087)
    ForceAnimation(3001896, 2, loop=True, unknown2=1.0)
    EnableFlag(13000885)


@RestartOnRest(13005889)
def Event_13005889():
    """Event 13005889"""
    if FlagEnabled(13000890):
        return
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_1:
        return
    WaitFrames(frames=1)
    
    MAIN.Await(FlagEnabled(13005885))
    
    EnableCharacter(3000899)
    EnableAnimations(3000899)
    EnableAI(3000899)
    ActivateMultiplayerBuffs(3000899)
    EnableFlag(13000896)


@RestartOnRest(13005890)
def Event_13005890():
    """Event 13005890"""
    DisableObject(3001890)
    DisableAI(3000899)
    DisableCharacter(3000899)
    DisableAnimations(3000899)
    DisableSoundEvent(sound_id=3002899)
    DisableSoundEvent(sound_id=3002898)
    ForceAnimation(3001895, 2, loop=True, unknown2=1.0)
    DisableObjectActivation(3001895, obj_act_id=300370)
    CreateObjectVFX(3001360, vfx_id=210, dummy_id=800030)
    CreateObjectVFX(3001360, vfx_id=212, dummy_id=800030)
    CreateObjectVFX(3001360, vfx_id=214, dummy_id=800043)
    CreateObjectVFX(3001361, vfx_id=210, dummy_id=800030)
    CreateObjectVFX(3001361, vfx_id=212, dummy_id=800030)
    CreateObjectVFX(3001361, vfx_id=214, dummy_id=800043)
    CreateObjectVFX(3001362, vfx_id=210, dummy_id=800030)
    CreateObjectVFX(3001362, vfx_id=212, dummy_id=800030)
    CreateObjectVFX(3001362, vfx_id=214, dummy_id=800043)
    CreateObjectVFX(3001363, vfx_id=210, dummy_id=800030)
    CreateObjectVFX(3001363, vfx_id=212, dummy_id=800030)
    CreateObjectVFX(3001363, vfx_id=214, dummy_id=800043)
    DeleteObjectVFX(3001890)
    DeleteObjectVFX(3001899)
    if FlagEnabled(13000890):
        return
    GotoIfFlagEnabled(Label.L1, flag=13000896)
    Move(3000899, destination=3002893, destination_type=CoordEntityType.Region, short_move=True)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    EnableObject(3001890)
    CreateObjectVFX(3001890, vfx_id=101, dummy_id=3)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=13000881, state=FlagSetting.On)
    AND_1.Add(CharacterDead(3000705))
    AND_1.Add(PlayerHasGood(2117))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=3002700))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    AND_2.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_2:
        return
    Wait(1.0)
    DeleteObjectVFX(3001890)
    WaitFrames(frames=1)
    EnableFlag(13004890)
    
    MAIN.Await(FlagEnabled(13005894))
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    NotifyBossBattleStart()
    SkipLinesIfLeavingSession(2)
    EnableObject(3001890)
    CreateObjectVFX(3001890, vfx_id=101, dummy_id=3)
    Goto(Label.L3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableObject(3001890)
    CreateObjectVFX(3001890, vfx_id=101, dummy_id=3)
    EnableCharacter(3000899)
    EnableAnimations(3000899)
    GotoIfPlayerNotInOwnWorld(Label.L2)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=3001890, entity=3001890))
    
    FaceEntity(PLAYER, 3002896, animation=60060, wait_for_completion=True)

    # --- Label 2 --- #
    DefineLabel(2)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=3002895))
    
    EnableFlag(13000880)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    NotifyBossBattleStart()
    BanishInvaders(unknown=0)
    AND_3.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    if AND_3:
        return

    # --- Label 3 --- #
    DefineLabel(3)
    GotoIfPlayerNotInOwnWorld(Label.L4)
    EnableBossMusic(sound_id=3002899)
    Unknown_2010_07(sound_id=3002898)
    EnableBossHealthBar(3000899, name=905270)
    SetNetworkUpdateRate(3000899, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ChangeCamera(normal_camera_id=3000, locked_camera_id=3000)
    SetNetworkUpdateAuthority(3000899, authority_level=UpdateAuthority.Forced)
    SetNetworkConnectedFlagState(flag=13005885, state=FlagSetting.On)

    # --- Label 4 --- #
    DefineLabel(4)


@RestartOnRest(13005891)
def Event_13005891():
    """Event 13005891"""
    if FlagEnabled(13000890):
        return
    
    MAIN.Await(CharacterHasTAEEvent(3000899, tae_event_id=10))
    
    EnableBossMusic(sound_id=3002898)


@RestartOnRest(13005892)
def Event_13005892():
    """Event 13005892"""
    if FlagEnabled(13000890):
        return
    CreateNPCPart(3000899, npc_part_id=10, part_index=NPCPartType.Part5, part_health=400)
    
    MAIN.Await(CharacterPartHealth(3000899, npc_part_id=10) <= 0)
    
    ForceAnimation(3000899, 20000, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    SetNPCPartHealth(3000899, npc_part_id=10, desired_health=400, overwrite_max=True)
    Restart()


@ContinueOnRest(13005893)
def Event_13005893():
    """Event 13005893"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(13005885)
    if PlayerInOwnWorld():
        return
    DisableNetworkSync()
    
    MAIN.Await(FlagEnabled(13000881))
    
    GotoIfFlagEnabled(Label.L0, flag=13005894)
    ForceAnimation(3001895, 2, unknown2=1.0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(3001895, 0, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    
    MAIN.Await(FlagEnabled(13005885))
    
    AND_1.Add(CharacterIsWhitePhantom(PLAYER))
    AND_1.Add(FlagDisabled(13000890))
    AND_1.Add(ActionButtonParamActivated(action_button_id=3001890, entity=3001890))
    
    MAIN.Await(AND_1)
    
    FaceEntity(PLAYER, 3002896, animation=60060, wait_for_completion=True)
    EnableBossMusic(sound_id=3002899)
    EnableBossHealthBar(3000899, name=905270)
    SetNetworkUpdateRate(3000899, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ChangeCamera(normal_camera_id=3000, locked_camera_id=3000)
    EnableFlag(13005886)
    EnableFlag(13000896)
    End()


@RestartOnRest(13005895)
def Event_13005895():
    """Event 13005895"""
    if FlagEnabled(13000890):
        return
    
    MAIN.Await(HealthRatio(3000899) <= 0.0)
    
    Wait(1.0)
    PlaySoundEffect(3000899, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(3000899))
    
    Wait(2.5)
    DisableBossMusic(sound_id=3002899)
    DisableBossMusic(sound_id=3002898)
    DisableBossMusic(sound_id=-1)
    KillBoss(game_area_param_id=3000899)
    ExtinguishBurningObjects()
    DeleteObjectVFX(3001885)
    DeleteObjectVFX(3001886)
    DeleteObjectVFX(3001887)
    DeleteObjectVFX(3001888)
    EnableFlag(13000890)
    EnableFlag(9300)
    EnableFlag(6300)
    DisableObject(3001890)
    DeleteObjectVFX(3001890)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(2.0)
    if FlagDisabled(13000880):
        ForceAnimation(3001895, 1, wait_for_completion=True, unknown2=1.0)
        ForceAnimation(3001895, 2, unknown2=1.0)


@RestartOnRest(13005899)
def Event_13005899():
    """Event 13005899"""
    if FlagEnabled(13000890):
        return
    GotoIfFlagEnabled(Label.L0, flag=13005894)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(13004890))
    
    MAIN.Await(AND_1)
    
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    if OR_15:
        return
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        30000010,
        cutscene_flags=CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3002897,
        game_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        30000010,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=3002897,
        game_map=HIGH_WALL_OF_LOTHRIC,
    )
    SkipLines(1)
    PlayCutscene(30000010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    DeleteObjectVFX(3001360)
    DeleteObjectVFX(3001361)
    DeleteObjectVFX(3001362)
    DeleteObjectVFX(3001363)
    WaitFrames(frames=1)
    ForceAnimation(3001895, 0, unknown2=1.0)
    EnableFlag(13005894)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteObjectVFX(3001360)
    DeleteObjectVFX(3001361)
    DeleteObjectVFX(3001362)
    DeleteObjectVFX(3001363)
    ForceAnimation(3001895, 0, unknown2=1.0)
    EnableFlag(13005894)
    End()


@RestartOnRest(13000901)
def Event_13000901(_, obj: int):
    """Event 13000901"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(6079):
        return
    DisableNetworkSync()
    CreateObjectVFX(obj, vfx_id=90, dummy_id=62)
    
    MAIN.Await(ActionButtonParamActivated(action_button_id=4200, entity=obj))
    
    ForceAnimation(PLAYER, 60070, unknown2=1.0)
    DeleteObjectVFX(obj)
    EnableFlag(13000900)


@ContinueOnRest(13005600)
def Event_13005600(_, character__obj: int, obj: int, obj_1: int):
    """Event 13005600"""
    GotoIfPlayerNotInOwnWorld(Label.L9)
    SkipLinesIfFlagRangeAnyEnabled(2, (1435, 1439))
    DisableNetworkConnectedFlagRange(flag_range=(1435, 1439))
    SetNetworkConnectedFlagState(flag=1435, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1435))
    AND_2.Add(FlagEnabled(50006230))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1435, 1439))
    SetNetworkConnectedFlagState(flag=1438, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1420, 1434))
    DisableNetworkConnectedFlagRange(flag_range=(1420, 1434))
    SetNetworkConnectedFlagState(flag=1420, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(711))
    AND_1.Add(FlagEnabled(1435))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1420, 1434))
    SetNetworkConnectedFlagState(flag=1421, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableGravity(character__obj)
    DisableCharacterCollision(character__obj)
    GotoIfFlagEnabled(Label.L0, flag=1420)
    GotoIfFlagEnabled(Label.L1, flag=1421)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DisableObject(character__obj)
    DisableObject(obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj_1)
    GotoIfFlagEnabled(Label.L10, flag=1438)
    ForceAnimation(character__obj, 20, unknown2=1.0)
    Move(character__obj, destination=3002705, destination_type=CoordEntityType.Region, short_move=True)
    EnableObjectInvulnerability(obj)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DropMandatoryTreasure(character__obj)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableGravity(character__obj)
    DisableCharacterCollision(character__obj)
    Move(character__obj, destination=3002710, destination_type=CoordEntityType.Region, short_move=True)
    DisableObject(obj)
    GotoIfFlagEnabled(Label.L10, flag=1438)
    ForceAnimation(character__obj, 30000, unknown2=1.0)
    DisableHealthBar(character__obj)
    EnableImmortality(character__obj)
    End()

    # --- Label 10 --- #
    DefineLabel(10)
    DisableObject(obj_1)
    DisableCharacter(character__obj)
    DisableBackread(character__obj)
    DropMandatoryTreasure(character__obj)
    End()


@ContinueOnRest(13005601)
def Event_13005601(_, flag: int):
    """Event 13005601"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    AwardItemLot(62320, host_only=False)


@ContinueOnRest(13005602)
def Event_13005602(_, entity: int, flag: int):
    """Event 13005602"""
    if PlayerNotInOwnWorld():
        return
    DisableFlag(flag)
    
    MAIN.Await(FlagEnabled(flag))
    
    ForceAnimation(entity, 20001, unknown2=1.0)


@ContinueOnRest(13005603)
def Event_13005603(_, attacked_entity: int):
    """Event 13005603"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(1421))
    AND_1.Add(AttackedWithDamageType(attacked_entity=attacked_entity, attacker=PLAYER))
    
    MAIN.Await(AND_1)
    
    EnableFlag(73000182)
    ForceAnimation(attacked_entity, 20001, unknown2=1.0)


@ContinueOnRest(13005604)
def Event_13005604():
    """Event 13005604"""
    MAIN.Await(FlagEnabled(1438))
    
    DisableObjectInvulnerability(3001875)


@ContinueOnRest(13005620)
def Event_13005620(_, character: int):
    """Event 13005620"""
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

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70000062)
    if FlagEnabled(1215):
        DisableFlag(73000120)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1200)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=1216)
    GotoIfFlagEnabled(Label.L2, flag=1218)
    ForceAnimation(character, 90360, skip_transition=True, unknown2=1.0)
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


@RestartOnRest(13005640)
def Event_13005640(_, character: int):
    """Event 13005640"""
    if FlagDisabled(13000830):
        SetCharacterTalkRange(character=character, distance=80.0)
        DisableFlag(73000200)
        DisableFlag(73000201)
        DisableFlag(73000202)
