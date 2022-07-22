"""
Dreg Heap

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
    CommonFunc_20005500(0, flag=15000800, bonfire_flag=15000000, character=5000950, obj=5001950)
    RegisterBonfire(bonfire_flag=15000001, obj=5001951, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15000002, obj=5001952, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15000003, obj=5001953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=15000004, obj=5001954, reaction_distance=5.0)
    Event_15005100()
    Event_15005800()
    Event_15005810()
    Event_15005811()
    Event_15005812()
    Event_15005813()
    Event_15005800()
    Event_15005849()
    Event_15005850(0, region=5002850, vfx_id=5003850, seconds=0.5, right=1)
    Event_15005850(1, region=5002851, vfx_id=5003851, seconds=0.10000000149011612, right=1)
    Event_15005850(2, region=5002852, vfx_id=5003852, seconds=0.0, right=1)
    Event_15005850(3, region=5002853, vfx_id=5003853, seconds=0.20000000298023224, right=1)
    Event_15005850(4, region=5002854, vfx_id=5003854, seconds=0.0, right=1)
    Event_15005850(5, region=5002855, vfx_id=5003855, seconds=0.4000000059604645, right=1)
    Event_15005850(6, region=5002856, vfx_id=5003856, seconds=0.5, right=1)
    Event_15005850(7, region=5002857, vfx_id=5003857, seconds=0.699999988079071, right=1)
    Event_15005850(8, region=5002858, vfx_id=5003858, seconds=0.8999999761581421, right=1)
    Event_15005850(9, region=5002859, vfx_id=5003859, seconds=0.800000011920929, right=1)
    Event_15005850(10, region=5002860, vfx_id=5003860, seconds=0.10000000149011612, right=1)
    Event_15005850(11, region=5002861, vfx_id=5003861, seconds=0.20000000298023224, right=1)
    Event_15005850(12, region=5002862, vfx_id=5003862, seconds=0.6000000238418579, right=1)
    Event_15005850(13, region=5002863, vfx_id=5003863, seconds=0.9800000190734863, right=1)
    Event_15005850(14, region=5002864, vfx_id=5003864, seconds=0.5, right=1)
    Event_15005850(15, region=5002865, vfx_id=5003865, seconds=0.6000000238418579, right=1)
    Event_15005850(16, region=5002866, vfx_id=5003866, seconds=0.699999988079071, right=1)
    Event_15005850(17, region=5002867, vfx_id=5003867, seconds=0.6899999976158142, right=1)
    Event_15005850(18, region=5002868, vfx_id=5003868, seconds=0.20000000298023224, right=1)
    Event_15005850(19, region=5002869, vfx_id=5003869, seconds=0.4000000059604645, right=1)
    Event_15005850(20, region=5002870, vfx_id=5003870, seconds=0.30000001192092896, right=1)
    Event_15005850(21, region=5002871, vfx_id=5003871, seconds=1.0, right=1)
    Event_15005850(22, region=5002872, vfx_id=5003872, seconds=0.0, right=1)
    Event_15005850(23, region=5002873, vfx_id=5003873, seconds=0.8999999761581421, right=1)
    Event_15005220(
        0,
        character=5000200,
        flag=15005230,
        flag_1=15005215,
        character_1=5000210,
        special_effect_id=16620,
        special_effect_id_1=16640,
    )
    CommonFunc_20005203(
        0,
        character=5000200,
        animation_id=30000,
        animation_id_1=20000,
        region=5002200,
        region_1=5002201,
        region_2=5002202,
        region_3=0,
        region_4=0,
        region_5=0,
    )
    Event_15005210(0, character=5000210, special_effect=16256, character_1=5004200, character_2=5000200, flag=15005215)
    Event_15005250(0, character=5000210, character_1=5000200)
    Event_15005260()
    Event_15005270(0, character=5000200)
    Event_15005290(0, character=5000200)
    Event_15005285(0, flag=15000235, character=5000200, character_1=5000210)
    DisableFlag(15005215)
    Event_15005261()
    Event_15005220(
        1,
        character=5000201,
        flag=15005231,
        flag_1=15005216,
        character_1=5000211,
        special_effect_id=16621,
        special_effect_id_1=16641,
    )
    Event_15005240(0, character=5000201, region=5002228, special_effect_id=16255)
    Event_15005210(1, character=5000211, special_effect=16256, character_1=5004201, character_2=5000201, flag=15005216)
    Event_15005250(1, character=5000211, character_1=5000201)
    Event_15005270(1, character=5000201)
    Event_15005266(
        1,
        character=5000211,
        animation_id=20001,
        region=5002220,
        region_1=5002221,
        region_2=5002222,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    Event_15005280(0, character=5000201, animation_id=30000, animation_id_1=20000)
    Event_15005290(1, character=5000201)
    Event_15005285(1, flag=15000236, character=5000201, character_1=5000211)
    DisableFlag(15005216)
    Event_15005265(
        0,
        character=5000212,
        animation_id=20000,
        region=5002240,
        region_1=5002241,
        region_2=5002242,
        region_3=5002243,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    Event_15005220(
        2,
        character=5000202,
        flag=15005232,
        flag_1=15005217,
        character_1=5000212,
        special_effect_id=16622,
        special_effect_id_1=16642,
    )
    Event_15005210(2, character=5000212, special_effect=16256, character_1=5004202, character_2=5000202, flag=15005217)
    Event_15005250(2, character=5000212, character_1=5000202)
    Event_15005270(2, character=5000202)
    Event_15005290(2, character=5000202)
    Event_15005285(2, flag=15000237, character=5000202, character_1=5000212)
    Event_15005460(
        1,
        character=5000223,
        animation_id=700,
        animation_id_1=1700,
        region=5002401,
        attacked_entity=5000222,
        special_effect=16005,
        seconds=0.30000001192092896,
        attacked_entity_1=5000220,
    )
    CommonFunc_20005132(0, character=5000222, radius=5.0, region=5002400)
    CommonFunc_20005210(0, character=5000224, animation_id=700, animation_id_1=1700, radius=12.0)
    CommonFunc_20005132(0, character=5000226, radius=5.0, region=5002402)
    CommonFunc_20005206(
        0,
        character=5000232,
        animation_id=701,
        animation_id_1=1701,
        region=5002250,
        region_1=5002251,
        region_2=5002252,
        region_3=0,
        region_4=0,
        region_5=0,
    )
    CommonFunc_20005203(
        0,
        character=5000233,
        animation_id=701,
        animation_id_1=1701,
        region=2,
        region_1=5002253,
        region_2=5002254,
        region_3=0,
        region_4=0,
        region_5=0,
    )
    CommonFunc_20005213(0, character=5000236, animation_id=700, animation_id_1=1700, radius=6.0, region=5002256)
    CommonFunc_20005213(0, character=5000237, animation_id=701, animation_id_1=1701, radius=5.0, region=5002257)
    Event_15005470()
    CommonFunc_20005213(0, character=5000300, animation_id=700, animation_id_1=1700, radius=2.0, region=5002301)
    CommonFunc_20005219(
        0,
        character=5000301,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5002302,
        seconds=3.0,
    )
    CommonFunc_20005243(
        0,
        character=5000400,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=6.5,
    )
    CommonFunc_20005243(
        0,
        character=5000401,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=7.199999809265137,
    )
    CommonFunc_20005243(
        0,
        character=5000402,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=3.9000000953674316,
    )
    CommonFunc_20005243(
        0,
        character=5000403,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=5.800000190734863,
    )
    CommonFunc_20005243(
        0,
        character=5000404,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=4.400000095367432,
    )
    CommonFunc_20005243(
        0,
        character=5000405,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=1.899999976158142,
    )
    CommonFunc_20005243(
        0,
        character=5000406,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=0.800000011920929,
    )
    CommonFunc_20005243(
        0,
        character=5000407,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=0.0,
    )
    CommonFunc_20005243(
        0,
        character=5000408,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=3.799999952316284,
    )
    CommonFunc_20005243(
        0,
        character=5000409,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=2.5,
    )
    CommonFunc_20005243(
        0,
        character=5000410,
        animation_id=700,
        animation_id_1=1700,
        character_1=5000300,
        special_effect=16220,
        seconds=1.0,
    )
    CommonFunc_20005212(0, character=5000310, animation_id=700, animation_id_1=1700, radius=5.0, region=5002315)
    CommonFunc_20005212(0, character=5000311, animation_id=700, animation_id_1=1700, radius=20.0, region=5002315)
    CommonFunc_20005219(
        0,
        character=5000315,
        animation_id=700,
        animation_id_1=1700,
        radius=3.0,
        region=5002317,
        seconds=1.0,
    )
    CommonFunc_20005219(
        0,
        character=5000420,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5002310,
        seconds=0.0,
    )
    CommonFunc_20005219(
        0,
        character=5000421,
        animation_id=701,
        animation_id_1=1701,
        radius=1.0,
        region=5002316,
        seconds=0.0,
    )
    CommonFunc_20005219(
        0,
        character=5000422,
        animation_id=702,
        animation_id_1=20000,
        radius=2.0,
        region=5002311,
        seconds=0.10000000149011612,
    )
    CommonFunc_20005219(
        0,
        character=5000423,
        animation_id=701,
        animation_id_1=1701,
        radius=2.0,
        region=5002312,
        seconds=0.0,
    )
    CommonFunc_20005219(
        0,
        character=5000424,
        animation_id=702,
        animation_id_1=20000,
        radius=2.0,
        region=5002312,
        seconds=0.30000001192092896,
    )
    CommonFunc_20005219(
        0,
        character=5000425,
        animation_id=702,
        animation_id_1=20000,
        radius=2.0,
        region=5002314,
        seconds=0.0,
    )
    CommonFunc_20005219(
        0,
        character=5000426,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5002312,
        seconds=0.800000011920929,
    )
    CommonFunc_20005219(
        0,
        character=5000427,
        animation_id=701,
        animation_id_1=1701,
        radius=1.0,
        region=5002318,
        seconds=1.5,
    )
    CommonFunc_20005219(
        0,
        character=5000428,
        animation_id=700,
        animation_id_1=1700,
        radius=1.0,
        region=5002319,
        seconds=0.5,
    )
    CommonFunc_20005219(
        0,
        character=5000316,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5002320,
        seconds=1.2999999523162842,
    )
    CommonFunc_20005219(
        0,
        character=5000317,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5002320,
        seconds=0.0,
    )
    Event_15005410(
        0,
        character=5000319,
        animation_id=700,
        animation_id_1=1700,
        region=5002322,
        flag=15005392,
        seconds=0.10000000149011612,
    )
    CommonFunc_20005205(
        0,
        character=5000448,
        animation_id=701,
        animation_id_1=1701,
        region=5002328,
        seconds=0.10000000149011612,
    )
    CommonFunc_20005132(0, character=5000449, radius=3.0, region=5002329)
    CommonFunc_20005205(0, character=5000331, animation_id=700, animation_id_1=1700, region=5002332, seconds=5.0)
    CommonFunc_20005205(0, character=5000456, animation_id=702, animation_id_1=20000, region=5002332, seconds=9.0)
    CommonFunc_20005205(0, character=5000457, animation_id=702, animation_id_1=20000, region=5002334, seconds=0.0)
    CommonFunc_20005205(0, character=5000458, animation_id=700, animation_id_1=1700, region=5002333, seconds=2.0)
    CommonFunc_20005205(0, character=5000459, animation_id=701, animation_id_1=1701, region=5002335, seconds=5.0)
    CommonFunc_20005219(
        0,
        character=5000335,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=5002340,
        seconds=0.0,
    )
    CommonFunc_20005201(0, character=5000460, animation_id=700, animation_id_1=1700, region=5002340, seconds=3.0)
    CommonFunc_20005201(
        0,
        character=5000461,
        animation_id=700,
        animation_id_1=1700,
        region=5002340,
        seconds=1.2000000476837158,
    )
    CommonFunc_20005201(0, character=5000462, animation_id=700, animation_id_1=1700, region=5002340, seconds=1.5)
    CommonFunc_20005201(0, character=5000463, animation_id=700, animation_id_1=1700, region=5002340, seconds=5.5)
    CommonFunc_20005201(
        0,
        character=5000464,
        animation_id=700,
        animation_id_1=1700,
        region=5002340,
        seconds=5.800000190734863,
    )
    Event_15005400(
        0,
        character=5000335,
        character_1=5000460,
        character_2=5003340,
        character_3=5000520,
        character_4=5003345,
        seconds=0.0,
    )
    Event_15005400(
        1,
        character=5000335,
        character_1=5000461,
        character_2=5003341,
        character_3=5000521,
        character_4=5003346,
        seconds=0.10000000149011612,
    )
    Event_15005400(
        2,
        character=5000335,
        character_1=5000462,
        character_2=5003342,
        character_3=5000522,
        character_4=5003347,
        seconds=0.30000001192092896,
    )
    CommonFunc_20005201(0, character=5000337, animation_id=700, animation_id_1=1700, region=5002356, seconds=0.0)
    CommonFunc_20005201(0, character=5000475, animation_id=700, animation_id_1=1700, region=5002355, seconds=3.0)
    CommonFunc_20005201(
        0,
        character=5000476,
        animation_id=700,
        animation_id_1=1700,
        region=5002355,
        seconds=3.700000047683716,
    )
    CommonFunc_20005201(
        0,
        character=5000477,
        animation_id=700,
        animation_id_1=1700,
        region=5002355,
        seconds=3.799999952316284,
    )
    CommonFunc_20005201(0, character=5000478, animation_id=700, animation_id_1=1700, region=5002355, seconds=5.0)
    CommonFunc_20005201(0, character=5000479, animation_id=700, animation_id_1=1700, region=5002355, seconds=5.5)
    Event_15005340(0, character=5000316, character_1=5000500)
    Event_15005340(1, character=5000319, character_1=5000503)
    Event_15005340(2, character=5000315, character_1=5000501)
    Event_15005340(3, character=5000426, character_1=5000502)
    Event_15005340(4, character=5000337, character_1=5000530)
    Event_15005340(7, character=5000454, character_1=5000506)
    Event_15005340(8, character=5000455, character_1=5000507)
    Event_15005340(9, character=5000457, character_1=5000508)
    Event_15005340(10, character=5000458, character_1=5000509)
    Event_15005340(11, character=5000463, character_1=5000523)
    Event_15005340(12, character=5000464, character_1=5000524)
    Event_15005360(0, character=5000460, character_1=5000520)
    Event_15005360(1, character=5000461, character_1=5000521)
    Event_15005360(2, character=5000462, character_1=5000522)
    Event_15005340(13, character=5000463, character_1=5000523)
    Event_15005340(14, character=5000464, character_1=5000524)
    Event_15005365(0, character=5000520)
    Event_15005365(1, character=5000521)
    Event_15005365(2, character=5000522)
    Event_15005310(12, character=5000335, character_1=5000460)
    Event_15005310(13, character=5000335, character_1=5000461)
    Event_15005310(14, character=5000335, character_1=5000462)
    Event_15005310(15, character=5000336, character_1=5000463)
    Event_15005310(16, character=5000336, character_1=5000464)
    Event_15005390(0, character=5000324, region=5002325, entity=5003320)
    Event_15005390(1, character=5000324, region=5002326, entity=5003321)
    Event_15005390(2, character=5000324, region=5002327, entity=5003322)
    Event_15005390(3, character=5000324, region=5002342, entity=5003323)
    Event_15005390(4, character=5000324, region=5002343, entity=5003324)
    Event_15005390(5, character=5000332, region=5002350, entity=5003350)
    Event_15005390(6, character=5000332, region=5002350, entity=5003351)
    CommonFunc_20005114(0, character=5000270, region=5002270, seconds=1.0)
    CommonFunc_20005114(0, character=5000271, region=5002270, seconds=1.5)
    CommonFunc_20005120(0, character=5000272, radius=12.0)
    CommonFunc_20005331(0, character=5000270)
    CommonFunc_20005331(0, character=5000271)
    CommonFunc_20005331(0, character=5000272)
    Event_15005444()
    Event_15005447()
    Event_15005448(1, character=5000273, animation_id=701, animation_id_1=1701, region=5002272, seconds=0.5)
    Event_15005448(2, character=5000274, animation_id=701, animation_id_1=1701, region=5002272, seconds=0.0)
    Event_15005448(3, character=5000275, animation_id=700, animation_id_1=1700, region=5002271, seconds=2.0)
    CommonFunc_20005132(0, character=5000275, radius=3.0, region=5002274)
    CommonFunc_20005132(0, character=5000279, radius=3.0, region=5002276)
    CommonFunc_20005132(0, character=5000280, radius=3.0, region=5002277)
    CommonFunc_20005132(0, character=5000281, radius=3.0, region=5002277)
    CommonFunc_20005205(0, character=5000283, animation_id=701, animation_id_1=1701, region=5002279, seconds=0.5)
    CommonFunc_20005205(0, character=5000284, animation_id=701, animation_id_1=1701, region=5002280, seconds=0.5)
    CommonFunc_20005134(0, character=5000285, animation_id=3006, radius=3.0, region=5002281)
    CommonFunc_20005205(0, character=5000286, animation_id=701, animation_id_1=1701, region=5002282, seconds=4.0)
    CommonFunc_20005132(0, character=5000287, radius=5.0, region=5002286)
    CommonFunc_20005132(0, character=5000288, radius=5.0, region=5002286)
    Event_15005440(0, character=5000288, attacker=5000200, region=5002287, region_1=5000287)
    Event_15005500()
    Event_15005502()
    Event_15005510()
    Event_15005520(0, region=5002520, obj=5001520)
    Event_15005520(1, region=5002521, obj=5001521)
    Event_15005530(0, region=5002530)
    Event_15005530(1, region=5002531)
    Event_15005530(2, region=5002532)
    Event_15005530(3, region=5002533)
    Event_15005530(4, region=5002534)
    Event_15005550(0, region=5002550)
    RunEvent(20005640, slot=0, args=(15000580, 5001580, 15000581, 15000582))
    Event_15005590()
    CommonFunc_20005650(0, flag=15000560, obj=5001560)
    Event_15005120(0, flag=15000120, character=5000120)
    Event_15005120(1, flag=15000121, character=5000121)
    Event_15005120(2, flag=15000122, character=5000122)
    Event_15005120(3, flag=15000123, character=5000123)
    Event_15005120(4, flag=15000124, character=5000124)
    Event_15005120(5, flag=15000125, character=5000125)
    Event_15005120(6, flag=15000126, character=5000126)
    Event_15005120(7, flag=15000127, character=5000127)
    CommonFunc_20005701(
        0,
        left=15000800,
        summon_flag=15004170,
        dismissal_flag=15005170,
        character=5000170,
        region=5002170,
        left_1=70000030,
    )
    CommonFunc_20005720(0, flag=15004170, flag_1=15005170, flag_2=15000800, character=5000170)
    CommonFunc_20005716(
        0,
        flag=15004170,
        flag_1=15005805,
        character=5000170,
        region=5002801,
        region_1=5002805,
        flag_2=15005801,
    )
    CommonFunc_20005715(
        0,
        flag=15004170,
        flag_1=15005805,
        character=5000170,
        region=5002806,
        flag_2=15005801,
        region_1=5002807,
        region_2=0,
    )
    Event_15005540(0, region=5002534, character=5000170)
    CommonFunc_20005701(
        0,
        left=15000800,
        summon_flag=15004174,
        dismissal_flag=15005174,
        character=5000174,
        region=5002174,
        left_1=0,
    )
    CommonFunc_20005720(0, flag=15004174, flag_1=15005174, flag_2=15000800, character=5000174)
    CommonFunc_20005716(
        0,
        flag=15004174,
        flag_1=15005805,
        character=5000174,
        region=5002801,
        region_1=5002805,
        flag_2=15005801,
    )
    CommonFunc_20005715(
        0,
        flag=15004174,
        flag_1=15005805,
        character=5000174,
        region=5002806,
        flag_2=15005801,
        region_1=5002807,
        region_2=0,
    )
    Event_15005540(1, region=5002534, character=5000174)
    CommonFunc_20005342(0, flag=15000180, character=5000180)
    CommonFunc_20005132(0, character=5000180, radius=6.0, region=5002270)
    Event_15005480(
        0,
        character=5000190,
        radius=6.0,
        region=5002270,
        region_1=5000180,
        flag=15000180,
        character_1=5005190,
    )
    CommonFunc_20006002(0, character=5000700, flag=1818, first_flag=1815, last_flag=1819)
    CommonFunc_20006002(0, character=5000701, flag=1818, first_flag=1815, last_flag=1819)
    CommonFunc_20006002(0, character=5000702, flag=1818, first_flag=1815, last_flag=1819)
    CommonFunc_20006000(
        0,
        character=5000700,
        flag=1816,
        flag_1=1817,
        flag_2=75000140,
        value=0.6499999761581421,
        first_flag=1815,
        last_flag=1819,
        right=0,
    )
    CommonFunc_20006000(
        0,
        character=5000701,
        flag=1816,
        flag_1=1817,
        flag_2=75000141,
        value=0.6499999761581421,
        first_flag=1815,
        last_flag=1819,
        right=0,
    )
    CommonFunc_20006000(
        0,
        character=5000702,
        flag=1816,
        flag_1=1817,
        flag_2=75000142,
        value=0.6499999761581421,
        first_flag=1815,
        last_flag=1819,
        right=0,
    )
    CommonFunc_20006001(0, attacked_entity=5000700, flag=1816, flag_1=1817, flag_2=75000140, right=3)
    CommonFunc_20006001(0, attacked_entity=5000701, flag=1816, flag_1=1817, flag_2=75000141, right=3)
    CommonFunc_20006001(0, attacked_entity=5000702, flag=1816, flag_1=1817, flag_2=75000142, right=3)
    CommonFunc_20006030(
        0,
        obj=5001700,
        action_button_id=4000,
        right=0,
        item_lot=66200,
        first_flag=50006620,
        last_flag=50006620,
        flag=75000135,
    )
    Event_15005702(0, character=5000701, character_1=5000170, flag=1801, flag_1=1803)
    Event_15005702(1, character=5000702, character_1=5000170, flag=1802, flag_1=1804)
    CommonFunc_20006002(0, character=5000705, flag=1878, first_flag=1875, last_flag=1879)
    CommonFunc_20006040(0, character=5000705, destination=5002705, special_effect=5450)
    Event_15005721(0, 5000705, 5001705)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    Event_15005200(0, character=5000200, region=5002200, region_1=0, region_2=0)
    Event_15005200(1, character=5000201, region=5002220, region_1=5002221, region_2=5002222)
    Event_15005200(2, character=5000202, region=5002240, region_1=5002241, region_2=5002242)
    Event_15005570()
    Event_15005575()
    DisableSoundEvent(sound_id=5004801)
    DisableSoundEvent(sound_id=5004802)
    Event_15005700(
        0,
        character=5000700,
        character_1=5000701,
        character_2=5000702,
        animation_id=91180,
        animation_id_1=91180,
        animation_id_2=91170,
    )
    Event_15005701(0, obj=5001345, character=5000230, obj_1=5001230)
    Event_15005720(0, character=5000705, animation_id=30004, command_id=2160, obj=5001705, destination=5002705)
    Event_15005722(0, 5000203)


@RestartOnRest(15005100)
def Event_15005100():
    """Event 15005100"""
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(FlagEnabled(15000800))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9380, entity=5001100))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(PlayerHasGood(2156))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    DisplayDialog(text=10012800)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    SetRespawnPoint(respawn_point=5102110)
    SaveRequest()
    PlayCutscene(51000000, cutscene_flags=0, player_id=10000, move_to_region=5102110, game_map=RINGED_CITY)
    WaitFrames(frames=1)
    Restart()


@ContinueOnRest(15005120)
def Event_15005120(_, flag: int, character: int):
    """Event 15005120"""
    AddSpecialEffect(character, 17500)
    DisableAI(character)
    DisableAnimations(character)
    ForceAnimation(character, 91230, unknown2=1.0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(flag)
    End()


@RestartOnRest(15005200)
def Event_15005200(_, character: int, region: int, region_1: int, region_2: int):
    """Event 15005200"""
    DisableGravity(character)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    
    MAIN.Await(OR_1)
    
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(15005210)
def Event_15005210(_, character: int, special_effect: int, character_1: int, character_2: int, flag: int):
    """Event 15005210"""
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    MakeEnemyAppear(character=character_1)
    DisableFlag(flag)
    WaitFrames(frames=1)
    ReplanAI(character_2)
    SetNetworkUpdateRate(character_2, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableGravity(character_2)
    Restart()


@RestartOnRest(15005220)
def Event_15005220(
    _,
    character: int,
    flag: int,
    flag_1: int,
    character_1: int,
    special_effect_id: int,
    special_effect_id_1: int,
):
    """Event 15005220"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    AND_2.Add(CharacterDead(character))
    AND_2.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_2)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=3,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)
    AddSpecialEffect(character_1, special_effect_id)
    SetNetworkUpdateRate(character_1, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AND_3.Add(CharacterAlive(character))
    AND_3.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_3)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    AddSpecialEffect(character_1, special_effect_id_1)
    SetNetworkUpdateRate(character_1, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest(15005240)
def Event_15005240(_, character: int, region: int, special_effect_id: int):
    """Event 15005240"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, special_effect_id)
    SetCharacterEventTarget(character, region=PLAYER)
    Wait(3.0)
    Restart()


@RestartOnRest(15005250)
def Event_15005250(_, character: int, character_1: int):
    """Event 15005250"""
    MAIN.Await(CharacterDead(character))
    
    AddSpecialEffect(character_1, 16258)


@RestartOnRest(15005260)
def Event_15005260():
    """Event 15005260"""
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5002202))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=5002221))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterHasSpecialEffect(5000200, 16259))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(5000200, 16259)
    Restart()


@RestartOnRest(15005261)
def Event_15005261():
    """Event 15005261"""
    AND_15.Add(CharacterDead(5000287))
    if AND_15:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5002286))
    
    MAIN.Await(AND_1)
    
    Wait(2.9000000953674316)
    AddSpecialEffect(5000200, 16611)
    SetCharacterEventTarget(5000200, region=5000287)
    
    MAIN.Await(CharacterDead(5000287))
    
    RemoveSpecialEffect(5000200, 16611)


@RestartOnRest(15005265)
def Event_15005265(
    _,
    character: int,
    animation_id: int,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    region_4: int,
    region_5: int,
    region_6: int,
):
    """Event 15005265"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    EnableFlag(15005217)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    if ValueNotEqual(left=region_4, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    if ValueNotEqual(left=region_5, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_5))
    if ValueNotEqual(left=region_6, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_6))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    ForceAnimation(character, animation_id, skip_transition=True, unknown2=1.0)
    EnableAI(character)


@RestartOnRest(15005266)
def Event_15005266(
    _,
    character: int,
    animation_id: int,
    region: int,
    region_1: int,
    region_2: int,
    region_3: int,
    region_4: int,
    region_5: int,
    region_6: int,
):
    """Event 15005266"""
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Coop,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    if ThisEventSlotFlagEnabled():
        return
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if ValueNotEqual(left=region_1, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    if ValueNotEqual(left=region_2, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_2))
    if ValueNotEqual(left=region_3, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_3))
    if ValueNotEqual(left=region_4, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_4))
    if ValueNotEqual(left=region_5, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_5))
    if ValueNotEqual(left=region_6, right=0):
        OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region_6))
    AND_1.Add(OR_1)
    AND_1.Add(OR_2)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    ForceAnimation(character, animation_id, skip_transition=True, unknown2=1.0)
    EnableAI(character)


@RestartOnRest(15005270)
def Event_15005270(_, character: int):
    """Event 15005270"""
    AND_1.Add(PlayerNotInOwnWorld())
    if AND_1:
        return
    AND_2.Add(CharacterBackreadEnabled(character))
    AND_2.Add(CharacterAlive(character))
    
    MAIN.Await(AND_2)
    
    SetNetworkUpdateAuthority(character, authority_level=UpdateAuthority.Forced)
    
    MAIN.Await(CharacterDead(character))
    
    Restart()


@RestartOnRest(15005280)
def Event_15005280(_, character: int, animation_id: int, animation_id_1: int):
    """Event 15005280"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_1.Add(CharacterHasSpecialEffect(5000211, 16610))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_1)
    OR_3.Add(AND_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    Wait(0.10000000149011612)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    if AND_2:
        return
    AND_8.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    GotoIfConditionTrue(Label.L1, input_condition=AND_8)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(character, 20002, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    ReplanAI(character)


@RestartOnRest(15005285)
def Event_15005285(_, flag: int, character: int, character_1: int):
    """Event 15005285"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAnimations(character)
    DisableAnimations(character_1)
    DisableCharacter(character)
    DisableCharacter(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(CharacterDead(character_1))
    
    EnableFlag(flag)


@RestartOnRest(15005290)
def Event_15005290(_, character: int):
    """Event 15005290"""
    MAIN.Await(CharacterHasSpecialEffect(character, 5031))
    
    ClearTargetList(character)
    Restart()


@RestartOnRest(15005300)
def Event_15005300(_, character: int, character_1: int, character_2: int):
    """Event 15005300"""
    RemoveSpecialEffect(character, 16240)
    if ThisEventSlotFlagEnabled():
        AND_1.Add(CharacterDead(character_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 16240))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    MakeEnemyAppear(character=character_2)
    WaitFrames(frames=1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=8,
        copy_draw_parent=character,
    )
    Restart()


@RestartOnRest(15005310)
def Event_15005310(_, character: int, character_1: int):
    """Event 15005310"""
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterDoesNotHaveSpecialEffect(character, 16245))
    AND_1.Add(CharacterDead(character_1))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(CharacterAlive(character_1))
    if AND_2:
        return RESTART
    AddSpecialEffect(character, 16245)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(15005340)
def Event_15005340(_, character: int, character_1: int):
    """Event 15005340"""
    AND_1.Add(CharacterDead(character_1))
    GotoIfConditionFalse(Label.L0, input_condition=AND_1)
    DisableCharacter(character)
    DisableAnimations(character)
    DisableAI(character)
    DisableCharacter(character_1)
    DisableAI(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfThisEventSlotFlagDisabled(Label.L1)
    DisableCharacter(character)
    DisableAnimations(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character_1)
    DisableAnimations(character_1)
    DisableAI(character_1)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16247))
    
    EnableCharacter(character_1)
    EnableAI(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=character,
    )
    WaitFrames(frames=1)
    ReplanAI(character_1)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16249))
    
    DisableCharacter(character)
    DisableAnimations(character)
    End()


@RestartOnRest(15005360)
def Event_15005360(_, character: int, character_1: int):
    """Event 15005360"""
    if ThisEventSlotFlagDisabled():
        DisableCharacter(character_1)
        DisableAnimations(character_1)
    DisableAI(character_1)
    AND_1.Add(CharacterHasSpecialEffect(character, 16247))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(character_1)
    EnableAI(character_1)
    Move(
        character_1,
        destination=character,
        destination_type=CoordEntityType.Character,
        model_point=50,
        copy_draw_parent=character,
    )
    WaitFrames(frames=1)
    ReplanAI(character_1)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    RemoveSpecialEffect(character, 16247)
    
    MAIN.Await(CharacterHasSpecialEffect(character, 16249))
    
    Move(character, destination=5002390, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    Kill(character)
    Wait(1.0)
    Restart()


@RestartOnRest(15005365)
def Event_15005365(_, character: int):
    """Event 15005365"""
    AND_1.Add(HealthValue(character) >= 1)
    AND_1.Add(CharacterHasSpecialEffect(character, 16901))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    Kill(character)
    Wait(1.0)
    Restart()


@RestartOnRest(15005370)
def Event_15005370(_, character: int, character_1: int, special_effect: int):
    """Event 15005370"""
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(character, 16229)
    AND_1.Add(CharacterHasSpecialEffect(character_1, special_effect))
    
    MAIN.Await(AND_1)
    
    RemoveSpecialEffect(character, 16229)


@RestartOnRest(15005380)
def Event_15005380(_, character: int, character_1: int):
    """Event 15005380"""
    RemoveSpecialEffect(character, 16240)
    AND_1.Add(CharacterHasSpecialEffect(character, 16240))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    MakeEnemyAppear(character=character_1)
    Wait(1.0)
    Restart()


@RestartOnRest(15005390)
def Event_15005390(_, character: int, region: int, entity: int):
    """Event 15005390"""
    DisableSpawner(entity=entity)
    AND_1.Add(CharacterDead(character))
    if AND_1:
        return
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_2.Add(CharacterAlive(character))
    
    MAIN.Await(AND_2)
    
    EnableSpawner(entity=entity)
    Wait(0.20000000298023224)
    AND_3.Add(AllPlayersOutsideRegion(region=region))
    OR_3.Add(AND_3)
    OR_3.Add(CharacterDead(character))
    
    MAIN.Await(OR_3)
    
    Restart()


@RestartOnRest(15005400)
def Event_15005400(
    _,
    character: int,
    character_1: int,
    character_2: int,
    character_3: int,
    character_4: int,
    seconds: float,
):
    """Event 15005400"""
    RemoveSpecialEffect(character, 16240)
    if ThisEventSlotFlagEnabled():
        AND_1.Add(CharacterDead(character_1))
    AND_1.Add(CharacterHasSpecialEffect(character, 16240))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    AND_3.Add(CharacterAlive(character_1))
    SkipLinesIfConditionTrue(1, AND_3)
    MakeEnemyAppear(character=character_2)
    SkipLinesIfThisEventSlotFlagDisabled(2)
    AND_2.Add(CharacterAlive(character_3))
    SkipLinesIfConditionTrue(1, AND_2)
    MakeEnemyAppear(character=character_4)
    WaitFrames(frames=1)
    DisableAI(character_3)
    DisableCharacter(character_3)
    DisableAnimations(character_3)
    Wait(1.0)
    Restart()


@RestartOnRest(15005410)
def Event_15005410(_, character: int, animation_id: int, animation_id_1: int, region: int, flag: int, seconds: float):
    """Event 15005410"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(FlagEnabled(flag))
    OR_3.Add(AND_1)
    OR_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Wait(seconds)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    End()


@RestartOnRest(15005440)
def Event_15005440(_, character: int, attacker: int, region: int, region_1: int):
    """Event 15005440"""
    SkipLinesIfFlagEnabled(1, 0)
    SkipLinesIfValueEqual(1, left=0, right=region_1)
    OR_1.Add(Attacked(attacked_entity=region_1, attacker=attacker))
    OR_1.Add(Attacked(attacked_entity=character, attacker=attacker))
    OR_1.Add(CharacterInsideRegion(character=character, region=region))
    
    MAIN.Await(OR_1)
    
    AND_2.Add(CharacterInsideRegion(character=character, region=region))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AddSpecialEffect(character, 5000)
    OR_3.Add(CharacterInsideRegion(character=character, region=region_1))
    
    MAIN.Await(OR_3)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(character, 5000)


@RestartOnRest(15005444)
def Event_15005444():
    """Event 15005444"""
    GotoIfPlayerInOwnWorld(Label.L9)
    GotoIfFlagEnabled(Label.L0, flag=15005445)
    Goto(Label.L1)

    # --- Label 9 --- #
    DefineLabel(9)
    GotoIfFlagDisabled(Label.L0, flag=15000180)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(5000290)
    DisableAnimations(5000290)
    DisableCharacter(5000291)
    DisableAnimations(5000291)
    DisableCharacter(5000292)
    DisableAnimations(5000292)
    if PlayerNotInOwnWorld():
        return
    SetNetworkConnectedFlagState(flag=15005445, state=FlagSetting.On)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(5000270)
    DisableAnimations(5000270)
    DisableCharacter(5000271)
    DisableAnimations(5000271)
    DisableCharacter(5000272)
    DisableAnimations(5000272)
    End()


@RestartOnRest(15005447)
def Event_15005447():
    """Event 15005447"""
    if FlagEnabled(15000180):
        return
    if ThisEventSlotFlagEnabled():
        return
    AddSpecialEffect(5000272, 16805)
    
    MAIN.Await(EntityWithinDistance(entity=5000272, other_entity=5000180, radius=5.0))
    
    RemoveSpecialEffect(5000272, 16805)


@RestartOnRest(15005448)
def Event_15005448(_, character: int, animation_id: int, animation_id_1: int, region: int, seconds: float):
    """Event 15005448"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_1)
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    Wait(seconds)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(15005460)
def Event_15005460(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    region: int,
    attacked_entity: int,
    special_effect: int,
    seconds: float,
    attacked_entity_1: int,
):
    """Event 15005460"""
    if ThisEventSlotFlagEnabled():
        return
    ForceAnimation(character, animation_id, unknown2=1.0)
    DisableGravity(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterHasSpecialEffect(character, special_effect))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity))
    OR_2.Add(AttackedWithDamageType(attacked_entity=attacked_entity_1))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    OR_3.Add(AND_1)
    OR_3.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_3)
    
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=character, special_effect=special_effect)
    Wait(0.5)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
    Wait(seconds)
    EnableGravity(character)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    End()


@RestartOnRest(15005470)
def Event_15005470():
    """Event 15005470"""
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(CharacterInsideRegion(character=5000236, region=5002260))
    
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=5002261))
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000236, radius=3.0))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkUpdateRate(5000236, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(5000236, 3011, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(5000236, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(15005480)
def Event_15005480(_, character: int, radius: float, region: int, region_1: int, flag: int, character_1: int):
    """Event 15005480"""
    GotoIfFlagDisabled(Label.L0, flag=flag)
    DisableAI(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfThisEventSlotFlagEnabled(Label.L1)
    DisableAI(character)
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=region))
    AND_1.Add(OR_2)
    AND_1.Add(OR_1)
    OR_3.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    OR_3.Add(AND_1)
    AND_3.Add(OR_3)
    AND_3.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_3)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableAI(character)
    if ValueNotEqual(left=0, right=0):
        AddSpecialEffect(character_1, 5000)
    AICommand(character, command_id=100, command_slot=0)
    SetCharacterEventTarget(character, region=region_1)


@RestartOnRest(15005500)
def Event_15005500():
    """Event 15005500"""
    ActivateCollisionAndCreateNavmesh(collision=5001505, state=False)
    ActivateCollisionAndCreateNavmesh(collision=5001506, state=False)
    GotoIfFlagDisabled(Label.L0, flag=15000500)
    EndOfAnimation(obj=5001500, animation_id=2)
    DisableObject(5001501)
    DisableObject(5001502)
    DisableObject(5001503)
    EnableObject(5001504)
    CreateVFX(5003500)
    CreateVFX(5003501)
    ActivateCollisionAndCreateNavmesh(collision=5001506, state=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ActivateCollisionAndCreateNavmesh(collision=5001505, state=True)
    DisableObject(5001504)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5002500))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=5002501))
    AND_1.Add(OR_1)
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    EnableFlag(15000500)
    EnableFlag(15005500)
    ActivateCollisionAndCreateNavmesh(collision=5001505, state=False)
    ForceAnimation(5001500, 1, unknown2=1.0)
    Wait(1.5)
    CreateHazard(
        obj_flag=15005500,
        obj=5001500,
        model_point=40,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=6.0,
        repetition_time=0.0,
    )
    Wait(1.7000000476837158)
    CreateHazard(
        obj_flag=15005501,
        obj=5001500,
        model_point=41,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=2.0,
        life=0.5,
        repetition_time=0.0,
    )
    DestroyObject_NoSlot(obj=5001501)
    DestroyObject_NoSlot(obj=5001502)
    DestroyObject_NoSlot(obj=5001503)
    EnableObject(5001504)
    CreateVFX(5003500)
    CreateVFX(5003501)
    Wait(0.5)
    RemoveObjectFlag(obj_flag=15005500)
    RemoveObjectFlag(obj_flag=15005501)
    Wait(2.200000047683716)
    ActivateCollisionAndCreateNavmesh(collision=5001506, state=True)


@RestartOnRest(15005502)
def Event_15005502():
    """Event 15005502"""
    DisableNetworkSync()
    if FlagEnabled(15000500):
        return
    
    MAIN.Await(FlagEnabled(15000500))
    
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5002502))
    if not AND_1:
        return
    Wait(0.4000000059604645)
    SetCameraVibration(vibration_id=105, anchor_entity=5002502, anchor_type=CoordEntityType.Region)
    Wait(1.600000023841858)
    SetCameraVibration(vibration_id=105, anchor_entity=5002502, anchor_type=CoordEntityType.Region)
    Wait(1.600000023841858)
    SetCameraVibration(vibration_id=104, anchor_entity=5002502, anchor_type=CoordEntityType.Region)


@RestartOnRest(15005510)
def Event_15005510():
    """Event 15005510"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    ForceAnimation(5001301, 310, loop=True, skip_transition=True, unknown2=1.0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=5002510))
    
    DestroyObject_NoSlot(obj=5001510)
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    ForceAnimation(5001301, 311, wait_for_completion=True, skip_transition=True, unknown2=1.0)
    ForceAnimation(5001301, 312, loop=True, skip_transition=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(5001510)
    ForceAnimation(5001301, 312, loop=True, skip_transition=True, unknown2=1.0)


@RestartOnRest(15005520)
def Event_15005520(_, region: int, obj: int):
    """Event 15005520"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    DestroyObject_NoSlot(obj=obj)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)


@RestartOnRest(15005530)
def Event_15005530(_, region: int):
    """Event 15005530"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(PLAYER, 4050)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=region))
    
    RemoveSpecialEffect(PLAYER, 4050)
    Restart()


@RestartOnRest(15005540)
def Event_15005540(_, region: int, character: int):
    """Event 15005540"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=character, region=region))
    
    AddSpecialEffect(character, 4050)
    
    MAIN.Await(CharacterOutsideRegion(character=character, region=region))
    
    RemoveSpecialEffect(character, 4050)
    Restart()


@RestartOnRest(15005550)
def Event_15005550(_, region: int):
    """Event 15005550"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    AddSpecialEffect(PLAYER, 4070)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=region))
    
    RemoveSpecialEffect(PLAYER, 4070)
    Restart()


@RestartOnRest(15005570)
def Event_15005570():
    """Event 15005570"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(5001510)
    RestoreObject(5001520)
    RestoreObject(5001521)


@RestartOnRest(15005575)
def Event_15005575():
    """Event 15005575"""
    EnableObjectInvulnerability(5001411)


@RestartOnRest(15005580)
def Event_15005580():
    """Event 15005580"""
    RegisterLadder(start_climbing_flag=15001580, stop_climbing_flag=15001581, obj=5001580)


@RestartOnRest(15005590)
def Event_15005590():
    """Event 15005590"""
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5002590))
    AND_1.Add(FlagDisabled(15000590))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetAreaWelcomeMessageState(state=False)
    EnableFlag(15000590)


@RestartOnRest(15005800)
def Event_15005800():
    """Event 15005800"""
    if FlagEnabled(15000800):
        return
    AND_1.Add(FlagEnabled(15005803))
    AND_1.Add(HealthRatio(5000801) <= 0.0)
    AND_2.Add(FlagEnabled(15005804))
    AND_2.Add(HealthRatio(5000802) <= 0.0)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    Wait(3.0)
    PlaySoundEffect(5000801, 777777777, sound_type=SoundType.s_SFX)
    Wait(3.0)
    HandleBossDefeatAndDisplayBanner(boss=5000801, banner=BannerType.HeirOfFireDestroyed)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    Kill(5005803)
    Wait(3.0)
    PlaySoundEffect(5000802, 777777777, sound_type=SoundType.s_SFX)
    Wait(3.0)
    HandleBossDefeatAndDisplayBanner(boss=5000802, banner=BannerType.HeirOfFireDestroyed)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableFlag(15000800)
    EnableFlag(9324)
    EnableFlag(6324)


@RestartOnRest(15005810)
def Event_15005810():
    """Event 15005810"""
    GotoIfFlagDisabled(Label.L0, flag=15000800)
    DisableCharacter(5005800)
    DisableAnimations(5005800)
    Kill(5005800)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableImmortality(5000800)
    DisableHealthBar(5000800)
    SetLockOnPoint(character=5000800, lock_on_model_point=220, state=False)
    DisableAI(5005800)
    EnableImmortality(5000801)
    DisableAI(5005801)
    DisableHealthBar(5000801)
    SetCollisionMask(5000801, bit_index=1, switch_type=OnOffChange.Off)
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    if OR_15:
        return
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=5002800))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=5000801))
    
    MAIN.Await(OR_1)
    
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_9.Add(FlagEnabled(15005805))
    AND_9.Add(CharacterInsideRegion(character=PLAYER, region=5002800))
    
    MAIN.Await(AND_9)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    SetNetworkUpdateRate(5005801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ReferDamageToEntity(5000801, target_entity=5000800)
    Wait(0.30000001192092896)
    EnableAI(5005801)
    if FlagDisabled(15005810):
        Wait(3.0)
    EnableBossHealthBar(5000801, name=905020)
    EnableBossHealthBar(5000802, name=905021, bar_slot=1)
    EnableFlag(15005810)
    SetNetworkConnectedFlagState(flag=15005801, state=FlagSetting.On)
    if PlayerNotInOwnWorld():
        return
    Wait(0.0)
    SetNetworkConnectedFlagState(flag=15005809, state=FlagSetting.On)


@RestartOnRest(15005811)
def Event_15005811():
    """Event 15005811"""
    if FlagEnabled(15000800):
        return
    EnableImmortality(5000802)
    DisableAI(5005802)
    DisableHealthBar(5000802)
    SetCollisionMask(5000802, bit_index=1, switch_type=OnOffChange.Off)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(15005809))
    OR_1.Add(AND_1)
    OR_1.Add(FlagEnabled(15005811))
    OR_1.Add(AttackedWithDamageType(attacked_entity=5000802))
    OR_1.Add(HealthRatio(5000801) <= 0.6499999761581421)
    OR_1.Add(CharacterHasSpecialEffect(5000801, 15025))
    
    MAIN.Await(OR_1)
    
    EnableAI(5005802)
    SetNetworkUpdateRate(5005802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Wait(0.0)
    EnableBossHealthBar(5000802, name=905021, bar_slot=1)


@RestartOnRest(15005812)
def Event_15005812():
    """Event 15005812"""
    if FlagEnabled(15000800):
        return
    AND_2.Add(CharacterHasSpecialEffect(5000801, 15202))
    AND_3.Add(CharacterHasSpecialEffect(5000802, 15202))
    OR_1.Add(AND_2)
    OR_1.Add(AND_3)
    
    MAIN.Await(OR_1)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_3)
    SetNetworkConnectedFlagState(flag=15005803, state=FlagSetting.On)
    Wait(6.0)
    DisableBossHealthBar(5000802, name=905023, bar_slot=1)
    Wait(12.0)
    EnableBossHealthBar(5000801, name=905022)
    DisableImmortality(5000801)
    SetCollisionMask(5000801, bit_index=1, switch_type=OnOffChange.On)
    GotoIfPlayerNotInOwnWorld(Label.L11)
    AND_11.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.GreaterThanOrEqual, value=2))
    GotoIfConditionTrue(Label.L11, input_condition=AND_11)
    AddSpecialEffect(5000801, 15150)

    # --- Label 11 --- #
    DefineLabel(11)
    DisableCharacter(5000802)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkConnectedFlagState(flag=15005804, state=FlagSetting.On)
    Wait(6.0)
    DisableBossHealthBar(5000801, name=905022)
    Wait(12.0)
    EnableBossHealthBar(5000802, name=905023)
    DisableImmortality(5000802)
    SetCollisionMask(5000802, bit_index=1, switch_type=OnOffChange.On)
    GotoIfPlayerNotInOwnWorld(Label.L12)
    AND_12.Add(AllyPhantomCountComparison(comparison_state=True, comparison_type=ComparisonType.GreaterThanOrEqual, value=2))
    GotoIfConditionTrue(Label.L12, input_condition=AND_12)
    AddSpecialEffect(5000802, 15150)

    # --- Label 12 --- #
    DefineLabel(12)
    DisableCharacter(5000801)
    Goto(Label.L1)

    # --- Label 1 --- #
    DefineLabel(1)
    SetNetworkConnectedFlagState(flag=15005802, state=FlagSetting.On)


@RestartOnRest(15005813)
def Event_15005813():
    """Event 15005813"""
    if FlagEnabled(15000800):
        return
    AND_1.Add(HealthValue(5000801) == 1)
    AND_2.Add(HealthValue(5000802) == 1)
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_3)
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=AND_2)
    AddSpecialEffect(5000801, 15100)
    AddSpecialEffect(5000801, 15204)
    AddSpecialEffect(5000802, 15204)
    AddSpecialEffect(5000802, 15201)
    Wait(3.0)
    RemoveSpecialEffect(5000801, 15040)
    RemoveSpecialEffect(5000801, 15026)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(5000802, 15100)
    AddSpecialEffect(5000802, 15204)
    AddSpecialEffect(5000801, 15204)
    AddSpecialEffect(5000801, 15201)
    Wait(3.0)
    RemoveSpecialEffect(5000802, 15040)
    RemoveSpecialEffect(5000802, 15026)


@RestartOnRest(15005820)
def Event_15005820(_, character: int, character_1: int, flag: int):
    """Event 15005820"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(15000800):
        return
    if FlagEnabled(15005803):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterAlive(character))
    AND_1.Add(CharacterDead(character_1))
    AND_1.Add(FlagEnabled(flag))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.Off)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(15005825)
def Event_15005825(
    _,
    character__region: int,
    character: int,
    flag: int,
    special_effect: int,
    character_1: int,
    model_point: int,
    right: int,
):
    """Event 15005825"""
    if FlagEnabled(15000800):
        return
    if FlagEnabled(15005803):
        return
    DisableGravity(character)
    AND_1.Add(CharacterHasSpecialEffect(character__region, special_effect))
    AND_1.Add(FlagDisabled(flag))
    
    MAIN.Await(AND_1)
    
    MakeEnemyAppear(character=character_1)
    WaitFrames(frames=1)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    Move(
        character,
        destination=character__region,
        destination_type=CoordEntityType.Character,
        model_point=model_point,
        copy_draw_parent=character__region,
    )
    SetNetworkConnectedFlagState(flag=flag, state=FlagSetting.On)
    ReplanAI(character)
    if ValueEqual(left=1, right=right):
        SetCharacterEventTarget(character, region=character__region)
    WaitFrames(frames=1)
    Restart()


@RestartOnRest(15005830)
def Event_15005830(_, character: int):
    """Event 15005830"""
    if FlagEnabled(15000800):
        return
    DisableNetworkSync()
    OR_5.Add(HealthValue(5000801) <= 0)
    OR_5.Add(HealthValue(5000802) <= 0)
    GotoIfConditionTrue(Label.L9, input_condition=OR_5)
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=18.0))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=18.0))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(character, 15041)
    OR_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=18.0))
    
    MAIN.Await(OR_1)
    
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(character, 15040)
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=18.0))
    
    MAIN.Await(OR_2)
    
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    AND_10.Add(CharacterHasSpecialEffect(character, 15042))
    SkipLinesIfConditionTrue(1, AND_10)
    AddSpecialEffect(character, 15040)
    Wait(0.20000000298023224)
    End()


@RestartOnRest(15005835)
def Event_15005835():
    """Event 15005835"""
    if FlagEnabled(15000800):
        return
    DisableNetworkSync()
    AND_13.Add(CharacterInsideRegion(character=PLAYER, region=5002800))
    AND_13.Add(FlagEnabled(15005810))
    
    MAIN.Await(AND_13)
    
    AND_14.Add(FlagEnabled(15005803))
    AND_14.Add(CharacterDead(5000801))
    AND_15.Add(FlagEnabled(15005804))
    AND_15.Add(CharacterDead(5000802))
    OR_15.Add(AND_14)
    OR_15.Add(AND_15)
    GotoIfConditionTrue(Label.L20, input_condition=OR_15)
    AND_5.Add(CharacterHasSpecialEffect(5000802, 15100))
    GotoIfConditionTrue(Label.L5, input_condition=AND_5)
    AND_10.Add(CharacterHasSpecialEffect(5000801, 15100))
    GotoIfConditionTrue(Label.L10, input_condition=AND_10)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    GotoIfConditionTrue(Label.L1, input_condition=OR_1)
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    GotoIfConditionTrue(Label.L2, input_condition=AND_1)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangeCamera(normal_camera_id=5020, locked_camera_id=5020)
    Wait(0.5)
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    AND_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    OR_3.Add(AND_3)
    OR_3.Add(CharacterHasSpecialEffect(5000801, 15100))
    OR_3.Add(CharacterHasSpecialEffect(5000802, 15100))
    
    MAIN.Await(OR_3)
    
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    ChangeCamera(normal_camera_id=5021, locked_camera_id=5021)
    Wait(0.5)
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    OR_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    OR_4.Add(CharacterHasSpecialEffect(5000801, 15100))
    OR_4.Add(CharacterHasSpecialEffect(5000802, 15100))
    
    MAIN.Await(OR_4)
    
    Goto(Label.L0)

    # --- Label 5 --- #
    DefineLabel(5)
    AND_6.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    GotoIfConditionTrue(Label.L6, input_condition=AND_6)
    AND_7.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    GotoIfConditionTrue(Label.L7, input_condition=AND_7)

    # --- Label 6 --- #
    DefineLabel(6)
    ChangeCamera(normal_camera_id=5020, locked_camera_id=5020)
    Wait(0.5)
    OR_6.Add(CharacterDead(5000801))
    OR_6.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    
    MAIN.Await(OR_6)
    
    Goto(Label.L0)

    # --- Label 7 --- #
    DefineLabel(7)
    ChangeCamera(normal_camera_id=5021, locked_camera_id=5021)
    Wait(0.5)
    OR_7.Add(CharacterDead(5000801))
    OR_7.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000801, radius=8.0))
    
    MAIN.Await(OR_7)
    
    Goto(Label.L0)

    # --- Label 10 --- #
    DefineLabel(10)
    AND_11.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    GotoIfConditionTrue(Label.L11, input_condition=AND_11)
    AND_12.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    GotoIfConditionTrue(Label.L12, input_condition=AND_12)

    # --- Label 11 --- #
    DefineLabel(11)
    ChangeCamera(normal_camera_id=5020, locked_camera_id=5020)
    Wait(0.5)
    OR_11.Add(CharacterDead(5000802))
    OR_11.Add(EntityBeyondDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    
    MAIN.Await(OR_11)
    
    Goto(Label.L0)

    # --- Label 12 --- #
    DefineLabel(12)
    ChangeCamera(normal_camera_id=5021, locked_camera_id=5021)
    Wait(0.5)
    OR_12.Add(CharacterDead(5000802))
    OR_12.Add(EntityWithinDistance(entity=PLAYER, other_entity=5000802, radius=8.0))
    
    MAIN.Await(OR_12)
    
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    Restart()

    # --- Label 20 --- #
    DefineLabel(20)
    Wait(3.0)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(0.5)
    End()


@RestartOnRest(15005850)
def Event_15005850(_, region: int, vfx_id: int, seconds: float, right: int):
    """Event 15005850"""
    if FlagEnabled(15000800):
        return
    DeleteVFX(vfx_id)
    if ValueNotEqual(left=1, right=right):
        OR_1.Add(CharacterInsideRegion(character=5000801, region=region))
        OR_1.Add(CharacterInsideRegion(character=5000802, region=region))
    else:
        OR_1.Add(CharacterHasSpecialEffect(5000801, 5404))
        OR_1.Add(CharacterHasSpecialEffect(5000802, 5404))
    AND_1.Add(OR_1)
    AND_1.Add(FlagEnabled(15005802))
    
    MAIN.Await(AND_1)
    
    Wait(seconds)
    CreateVFX(vfx_id)


@RestartOnRest(15005849)
def Event_15005849():
    """Event 15005849"""
    CommonFunc_20005800(
        0,
        flag=15000800,
        entity=5001800,
        region=5002800,
        flag_1=15005805,
        action_button_id=5001800,
        character=5005800,
        left=15005801,
        region_1=0,
    )
    CommonFunc_20005801(
        0,
        flag=15000800,
        entity=5001800,
        region=5002801,
        flag_1=15005805,
        action_button_id=5001800,
        flag_2=15005806,
    )
    if FlagDisabled(15005801):
        CommonFunc_20001836(
            0,
            flag=15000800,
            flag_1=15005805,
            flag_2=15005806,
            flag_3=15005810,
            sound_id=5004801,
            sound_id_1=5004802,
            flag_4=15005802,
        )
    else:
        CommonFunc_20005831(
            0,
            flag=15000800,
            flag_1=15005805,
            flag_2=15005806,
            region=5002800,
            sound_id=5004801,
            sound_id_1=5004802,
            flag_3=15005802,
        )
    CommonFunc_20005820(0, flag=15000800, obj=5001800, model_point=3, left=15005801)
    CommonFunc_20005820(0, flag=15000800, obj=5001801, model_point=2, left=15005801)
    CommonFunc_20005810(0, flag=15000800, entity=5001800, target_entity=5002801, action_button_id=10000)
    Event_15005820(0, character=5000802, character_1=5000810, flag=15005840)
    Event_15005820(1, character=5000802, character_1=5000811, flag=15005841)
    Event_15005820(2, character=5000802, character_1=5000812, flag=15005842)
    Event_15005820(3, character=5000802, character_1=5000813, flag=15005843)
    Event_15005820(4, character=5000802, character_1=5000814, flag=15005844)
    Event_15005825(
        0,
        character__region=5000802,
        character=5000810,
        flag=15005840,
        special_effect=15020,
        character_1=5004810,
        model_point=100,
        right=0,
    )
    Event_15005825(
        1,
        character__region=5000802,
        character=5000811,
        flag=15005841,
        special_effect=15021,
        character_1=5004811,
        model_point=1,
        right=0,
    )
    Event_15005825(
        2,
        character__region=5000802,
        character=5000812,
        flag=15005842,
        special_effect=15022,
        character_1=5004812,
        model_point=2,
        right=0,
    )
    Event_15005825(
        3,
        character__region=5000802,
        character=5000813,
        flag=15005843,
        special_effect=15027,
        character_1=5004813,
        model_point=1,
        right=1,
    )
    Event_15005825(
        4,
        character__region=5000802,
        character=5000814,
        flag=15005844,
        special_effect=15028,
        character_1=5004814,
        model_point=2,
        right=1,
    )
    Event_15005835()
    CommonFunc_20005840(0, other_entity=5001800)
    CommonFunc_20005841(0, 5001800)


@ContinueOnRest(15005700)
def Event_15005700(
    _,
    character: int,
    character_1: int,
    character_2: int,
    animation_id: int,
    animation_id_1: int,
    animation_id_2: int,
):
    """Event 15005700"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1815, 1819))
    DisableNetworkConnectedFlagRange(flag_range=(1815, 1819))
    SetNetworkConnectedFlagState(flag=1815, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1816))
    AND_1.Add(FlagEnabled(70001073))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1815, 1819))
    SetNetworkConnectedFlagState(flag=1815, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1800, 1814))
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1800, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1815)
    AND_2.Add(FlagEnabled(1800))
    AND_2.Add(FlagEnabled(75000101))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1801, state=FlagSetting.On)
    if FlagEnabled(1803):
        DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
        SetNetworkConnectedFlagState(flag=1801, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1801))
    AND_3.Add(FlagEnabled(9324))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1805, state=FlagSetting.On)
    AND_4.Add(FlagEnabled(1801))
    AND_4.Add(FlagEnabled(75000131))
    AND_4.Add(FlagDisabled(55000450))
    AND_4.Add(FlagEnabled(1875))
    SkipLinesIfConditionFalse(2, AND_4)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1802, state=FlagSetting.On)
    if FlagEnabled(1804):
        DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
        SetNetworkConnectedFlagState(flag=1802, state=FlagSetting.On)
    AND_5.Add(FlagEnabled(1802))
    AND_5.Add(FlagEnabled(9324))
    SkipLinesIfConditionFalse(2, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1806, state=FlagSetting.On)
    AND_6.Add(FlagEnabled(1805))
    AND_6.Add(FlagEnabled(75000131))
    AND_6.Add(FlagDisabled(55000450))
    AND_6.Add(FlagEnabled(1875))
    SkipLinesIfConditionFalse(2, AND_6)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1806, state=FlagSetting.On)
    AND_7.Add(FlagRangeAnyEnabled(flag_range=(1805, 1806)))
    AND_7.Add(FlagEnabled(75000104))
    SkipLinesIfConditionFalse(2, AND_7)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=1807, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001073)
    if FlagEnabled(1815):
        DisableFlag(75000120)
    OR_1.Add(FlagEnabled(1802))
    OR_1.Add(FlagEnabled(1806))
    SkipLinesIfConditionFalse(1, OR_1)
    EnableFlag(15000703)
    SkipLinesIfFlagRangeAllDisabled(1, (1807, 1814))
    EnableFlag(75000135)
    OR_2.Add(FlagEnabled(1801))
    OR_2.Add(FlagEnabled(1803))
    OR_2.Add(FlagEnabled(1805))
    AND_8.Add(FlagEnabled(75000130))
    AND_8.Add(FlagDisabled(55000450))
    AND_8.Add(FlagEnabled(1875))
    AND_8.Add(OR_2)
    SkipLinesIfConditionFalse(1, AND_8)
    EnableFlag(75000131)
    OR_3.Add(FlagEnabled(1801))
    OR_3.Add(FlagEnabled(1803))
    OR_3.Add(FlagEnabled(1805))
    AND_9.Add(FlagEnabled(75000103))
    AND_9.Add(FlagDisabled(55000450))
    AND_9.Add(FlagEnabled(1875))
    AND_9.Add(OR_3)
    SkipLinesIfConditionFalse(1, AND_9)
    EnableFlag(75000130)
    OR_4.Add(PlayerHasGood(2153))
    OR_4.Add(FlagEnabled(6500))
    SkipLinesIfConditionFalse(1, OR_4)
    EnableFlag(50006623)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1800)
    GotoIfFlagEnabled(Label.L1, flag=1801)
    GotoIfFlagEnabled(Label.L2, flag=1802)
    GotoIfFlagEnabled(Label.L5, flag=1805)
    GotoIfFlagEnabled(Label.L6, flag=1806)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    GotoIfFlagEnabled(Label.L16, flag=1816)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    ForceAnimation(character, animation_id, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 5 --- #
    DefineLabel(5)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    GotoIfFlagEnabled(Label.L16, flag=1816)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    ForceAnimation(character_1, animation_id_1, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character_1, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    End()

    # --- Label 2 --- #
    DefineLabel(2)

    # --- Label 6 --- #
    DefineLabel(6)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L16, flag=1816)
    GotoIfFlagEnabled(Label.L18, flag=1818)
    ForceAnimation(character_2, animation_id_2, unknown2=1.0)
    End()

    # --- Label 16 --- #
    DefineLabel(16)
    SetTeamType(character_2, TeamType.HostileNPC)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_2)
    DisableBackread(character_2)
    DropMandatoryTreasure(character_2)
    End()


@RestartOnRest(15005701)
def Event_15005701(_, obj: int, character: int, obj_1: int):
    """Event 15005701"""
    DisableObject(obj_1)
    
    MAIN.Await(FlagEnabled(15000703))
    
    DisableTreasure(obj=obj)
    DisableCharacter(character)
    DisableBackread(character)
    EnableObject(obj_1)


@ContinueOnRest(15005702)
def Event_15005702(_, character: int, character_1: int, flag: int, flag_1: int):
    """Event 15005702"""
    EndIfFlagRangeAnyEnabled(flag_range=(1805, 1814))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1815))
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagDisabled(9324))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 490))
    AND_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=character_1, radius=10.0))
    AND_1.Add(CharacterBackreadEnabled(character_1))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L0)
    DisableNetworkConnectedFlagRange(flag_range=(1800, 1814))
    SetNetworkConnectedFlagState(flag=flag_1, state=FlagSetting.On)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)


@ContinueOnRest(15005720)
def Event_15005720(_, character: int, animation_id: int, command_id: int, obj: int, destination: int):
    """Event 15005720"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1875, 1879))
    DisableNetworkConnectedFlagRange(flag_range=(1875, 1879))
    SetNetworkConnectedFlagState(flag=1875, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1876))
    AND_1.Add(FlagEnabled(70001076))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1875, 1879))
    SetNetworkConnectedFlagState(flag=1875, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1860, 1874))
    DisableNetworkConnectedFlagRange(flag_range=(1860, 1874))
    SetNetworkConnectedFlagState(flag=1860, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1860))
    AND_2.Add(FlagEnabled(1878))
    SkipLinesIfConditionFalse(2, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1860, 1874))
    SetNetworkConnectedFlagState(flag=1861, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1860))
    AND_3.Add(FlagEnabled(1875))
    AND_3.Add(FlagEnabled(15100500))
    SkipLinesIfConditionFalse(4, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1860, 1874))
    SetNetworkConnectedFlagState(flag=1862, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1875, 1879))
    SetNetworkConnectedFlagState(flag=1878, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001076)
    DisableFlag(15000721)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1860)
    GotoIfFlagEnabled(Label.L1, flag=1861)
    GotoIfFlagEnabled(Label.L2, flag=1862)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L18, flag=1878)
    DisableHealthBar(character)
    ForceAnimation(character, animation_id, unknown2=1.0)
    DisableCharacterCollision(character)
    DisableGravity(character)
    Move(character, destination=destination, destination_type=CoordEntityType.Region, copy_draw_parent=character)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    DestroyObject(obj, request_slot=0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    EzstateAIRequest(character, command_id=command_id, command_slot=1)
    DropMandatoryTreasure(character)
    DestroyObject(obj)
    End()


@ContinueOnRest(15005721)
def Event_15005721(_, character: int, obj: int):
    """Event 15005721"""
    GotoIfFlagEnabled(Label.L0, flag=15000721)
    if FlagDisabled(1860):
        return
    GotoIfPlayerNotInOwnWorld(Label.L1)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    
    MAIN.Await(AND_2)
    
    WaitFrames(frames=1)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(CharacterBackreadDisabled(character))
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    RestartIfFinishedConditionTrue(input_condition=AND_4)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableCharacterCollision(character)
    EnableGravity(character)
    DisableObjectInvulnerability(obj)
    DestroyObject_NoSlot(obj=obj)
    EnableFlag(15000721)


@RestartOnRest(15005722)
def Event_15005722(_, character: int):
    """Event 15005722"""
    DisableCharacter(character)
    DisableBackread(character)
    
    MAIN.Await(FlagRangeAnyEnabled(flag_range=(1861, 1862)))
    
    EnableCharacter(character)
    EnableBackread(character)
    DisableGravity(character)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(15005900)
def Event_15005900():
    """Event 15005900"""
    SetBackreadStateAlternate(5000202, True)
    SetBackreadStateAlternate(5000212, True)
    SetNetworkUpdateRate(5000212, is_fixed=True, update_rate=CharacterUpdateRate.Always)
