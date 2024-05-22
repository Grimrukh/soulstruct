"""
Painted World of Ariandel

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
    CommonFunc_20005500(0, flag=14500800, bonfire_flag=14500000, character=4500950, obj=4501950)
    CommonFunc_20005500(0, flag=14500860, bonfire_flag=14500006, character=4500956, obj=4501956)
    RegisterBonfire(bonfire_flag=14500001, obj=4501951, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500002, obj=4501952, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500003, obj=4501953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500004, obj=4501954, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500005, obj=4501955, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500007, obj=4501957, reaction_distance=5.0)
    CommonFunc_20005270(0, character=4500212, animation_id=700, animation_id_1=1700, special_effect=13034)
    CommonFunc_20005270(0, character=4500240, animation_id=700, animation_id_1=1700, special_effect=13034)
    CommonFunc_20005270(0, character=4500241, animation_id=701, animation_id_1=1701, special_effect=13034)
    CommonFunc_20005360(0, character=4500212, entity=10000, special_effect=13034)
    CommonFunc_20005360(0, character=4500240, entity=10000, special_effect=13034)
    CommonFunc_20005360(0, character=4500241, entity=10000, special_effect=13034)
    Event_14505240(0, character=4500212, special_effect=5024)
    Event_14505240(1, character=4500240, special_effect=5024)
    Event_14505280()
    Event_14505281()
    CommonFunc_20005270(0, character=4500242, animation_id=700, animation_id_1=1700, special_effect=13022)
    CommonFunc_20005270(0, character=4500243, animation_id=700, animation_id_1=1700, special_effect=13022)
    CommonFunc_20005270(0, character=4500244, animation_id=700, animation_id_1=1700, special_effect=13022)
    CommonFunc_20005270(0, character=4500211, animation_id=701, animation_id_1=1701, special_effect=13022)
    Event_14505290(0, character=4500242, region=4502231, special_effect=13031)
    Event_14505290(1, character=4500243, region=4502231, special_effect=13031)
    Event_14505290(2, character=4500244, region=4502231, special_effect=13031)
    Event_14505290(3, character=4500211, region=4502231, special_effect=13031)
    Event_14505282(0, character=4500242, region=4502232)
    Event_14505282(1, character=4500243, region=4502232)
    Event_14505282(2, character=4500244, region=4502232)
    Event_14505282(3, character=4500211, region=4502232)
    CommonFunc_20005360(0, character=4500242, entity=10000, special_effect=13022)
    CommonFunc_20005360(0, character=4500243, entity=10000, special_effect=13022)
    CommonFunc_20005360(0, character=4500244, entity=10000, special_effect=13022)
    CommonFunc_20005360(0, character=4500211, entity=10000, special_effect=13022)
    CommonFunc_20005221(0, character=4500210, animation_id=701, animation_id_1=1701, radius=30.0)
    Event_14505270(
        0,
        character=4500247,
        animation_id=700,
        animation_id_1=1700,
        seconds=1.0,
        region=4502236,
        animation_id_2=20000,
        seconds_1=0.5,
        region_1=4502235,
    )
    Event_14505270(
        1,
        character=4500248,
        animation_id=700,
        animation_id_1=1700,
        seconds=0.5,
        region=4502236,
        animation_id_2=20000,
        seconds_1=0.0,
        region_1=4502235,
    )
    Event_14505270(
        2,
        character=4500249,
        animation_id=700,
        animation_id_1=1700,
        seconds=0.0,
        region=4502236,
        animation_id_2=20000,
        seconds_1=1.0,
        region_1=4502235,
    )
    CommonFunc_20005360(0, character=4500247, entity=10000, special_effect=13022)
    CommonFunc_20005360(0, character=4500248, entity=10000, special_effect=13022)
    CommonFunc_20005360(0, character=4500249, entity=10000, special_effect=13022)
    CommonFunc_20005220(0, character=4500214, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500215, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500216, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500245, animation_id=701, animation_id_1=1701)
    CommonFunc_20005220(0, character=4500246, animation_id=700, animation_id_1=1700)
    CommonFunc_20005219(
        0,
        character=4500218,
        animation_id=701,
        animation_id_1=1701,
        radius=2.0,
        region=4502285,
        seconds=0.5,
    )
    CommonFunc_20005219(
        0,
        character=4500251,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=4502285,
        seconds=1.0,
    )
    CommonFunc_20005219(
        0,
        character=4500252,
        animation_id=700,
        animation_id_1=1700,
        radius=2.0,
        region=4502285,
        seconds=0.0,
    )
    Event_14505260(
        0,
        character=4500219,
        animation_id=30001,
        animation_id_1=20000,
        seconds=0.5,
        seconds_1=0.0,
        animation_id_2=3006,
    )
    Event_14505260(
        1,
        character=4500253,
        animation_id=30001,
        animation_id_1=20000,
        seconds=1.2000000476837158,
        seconds_1=15.0,
        animation_id_2=3006,
    )
    Event_14505260(
        2,
        character=4500254,
        animation_id=30001,
        animation_id_1=20000,
        seconds=0.0,
        seconds_1=21.5,
        animation_id_2=3009,
    )
    Event_14505260(
        3,
        character=4500255,
        animation_id=30001,
        animation_id_1=20000,
        seconds=0.699999988079071,
        seconds_1=20.899999618530273,
        animation_id_2=3009,
    )
    Event_14505260(
        4,
        character=4500256,
        animation_id=30001,
        animation_id_1=20000,
        seconds=0.20000000298023224,
        seconds_1=6.5,
        animation_id_2=3009,
    )
    Event_14505260(
        5,
        character=4500257,
        animation_id=30001,
        animation_id_1=20000,
        seconds=1.2000000476837158,
        seconds_1=5.900000095367432,
        animation_id_2=3009,
    )
    CommonFunc_20006040(0, character=4500219, destination=4502221, special_effect=5450)
    CommonFunc_20006040(0, character=4500253, destination=4502222, special_effect=5450)
    CommonFunc_20006040(0, character=4500254, destination=4502223, special_effect=5450)
    CommonFunc_20006040(0, character=4500255, destination=4502224, special_effect=5450)
    CommonFunc_20006040(0, character=4500256, destination=4502225, special_effect=5450)
    CommonFunc_20006040(0, character=4500257, destination=4502226, special_effect=5450)
    CommonFunc_20005110(0, character=4500594, region=4502455)
    CommonFunc_20005110(0, character=4500220, region=4502455)
    CommonFunc_20005110(0, character=4500259, region=4502455)
    CommonFunc_20005213(0, character=4500260, animation_id=700, animation_id_1=1700, radius=2.0, region=4502460)
    CommonFunc_20005111(0, character=4500258, animation_id=3001, region=4502456)
    CommonFunc_20005220(0, character=4500250, animation_id=701, animation_id_1=1701)
    CommonFunc_20005270(0, character=4500261, animation_id=700, animation_id_1=1700, special_effect=13022)
    CommonFunc_20005270(0, character=4500262, animation_id=701, animation_id_1=1701, special_effect=13022)
    CommonFunc_20005360(0, character=4500261, entity=10000, special_effect=13022)
    CommonFunc_20005360(0, character=4500262, entity=10000, special_effect=13022)
    Event_14505200()
    Event_14505201()
    Event_14505202()
    Event_14505203()
    Event_14505204()
    Event_14505210()
    Event_14505211()
    Event_14505213()
    CommonFunc_20005210(0, character=4500307, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=4500317, animation_id=700, animation_id_1=1700, radius=4.0)
    CommonFunc_20005210(0, character=4500318, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005223(0, character=4500320, animation_id=700, animation_id_1=1700, seconds=1.0)
    CommonFunc_20005221(0, character=4500322, animation_id=700, animation_id_1=1700, radius=9.0)
    CommonFunc_20005265(0, character=4500329, animation_id=700, animation_id_1=1700, character_1=4500567)
    CommonFunc_20005265(0, character=4500330, animation_id=700, animation_id_1=1700, character_1=4500567)
    CommonFunc_20005265(0, character=4500331, animation_id=700, animation_id_1=1700, character_1=4500567)
    CommonFunc_20005222(0, character=4500334, animation_id=700, animation_id_1=1700, radius=6.0, seconds=1.5)
    CommonFunc_20005265(0, character=4500335, animation_id=700, animation_id_1=1700, character_1=4500337)
    CommonFunc_20005265(0, character=4500336, animation_id=700, animation_id_1=1700, character_1=4500337)
    CommonFunc_20005217(0, character=4500337, animation_id=700, animation_id_1=1700, radius=3.0, region=4502300)
    CommonFunc_20005217(0, character=4500338, animation_id=700, animation_id_1=1700, radius=3.0, region=4502300)
    CommonFunc_20005217(0, character=4500339, animation_id=700, animation_id_1=1700, radius=3.0, region=4502300)
    CommonFunc_20005221(0, character=4500340, animation_id=700, animation_id_1=1700, radius=18.0)
    CommonFunc_20005265(0, character=4500341, animation_id=700, animation_id_1=1700, character_1=4500337)
    CommonFunc_20005210(0, character=4500344, animation_id=700, animation_id_1=1700, radius=5.400000095367432)
    CommonFunc_20005212(0, character=4500347, animation_id=700, animation_id_1=1700, radius=6.0, region=4502320)
    CommonFunc_20005212(0, character=4500348, animation_id=700, animation_id_1=1700, radius=6.0, region=4502320)
    Event_14505300(3, character=4500350, other_entity=4500350, radius=8.0)
    CommonFunc_20005221(0, character=4500350, animation_id=701, animation_id_1=1701, radius=6.0)
    CommonFunc_20005221(0, character=4500351, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005221(0, character=4500352, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005221(0, character=4500353, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005221(0, character=4500354, animation_id=700, animation_id_1=1700, radius=16.0)
    Event_14505400(1, character=4500401, animation_id=30001, animation_id_1=20001, region=4502401, seconds=0.0)
    CommonFunc_20005119(
        0,
        character=4500403,
        region=4502423,
        region_1=4502424,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005132(0, character=4500404, radius=5.0, region=4502405)
    CommonFunc_20005110(0, character=4500405, region=4502405)
    Event_14505400(7, character=4500407, animation_id=30001, animation_id_1=20001, region=4502407, seconds=0.0)
    Event_14505410()
    Event_14505411()
    Event_14505412()
    CommonFunc_20005210(0, character=4500410, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500411, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500412, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500413, animation_id=704, animation_id_1=1704, radius=3.0)
    CommonFunc_20005201(0, character=4500414, animation_id=700, animation_id_1=1700, region=4502440, seconds=3.0)
    CommonFunc_20005210(0, character=4500415, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005201(0, character=4500416, animation_id=700, animation_id_1=1700, region=4502440, seconds=0.5)
    CommonFunc_20005201(
        0,
        character=4500417,
        animation_id=700,
        animation_id_1=1700,
        region=4502440,
        seconds=0.20000000298023224,
    )
    CommonFunc_20005201(0, character=4500418, animation_id=700, animation_id_1=1700, region=4502440, seconds=0.5)
    CommonFunc_20005201(0, character=4500419, animation_id=700, animation_id_1=1700, region=4502440, seconds=0.5)
    CommonFunc_20005201(
        0,
        character=4500420,
        animation_id=701,
        animation_id_1=1701,
        region=4502440,
        seconds=0.10000000149011612,
    )
    CommonFunc_20005201(0, character=4500421, animation_id=701, animation_id_1=1701, region=4502440, seconds=1.5)
    CommonFunc_20005210(0, character=4500422, animation_id=701, animation_id_1=1701, radius=4.0)
    CommonFunc_20005201(0, character=4500423, animation_id=701, animation_id_1=1701, region=4502440, seconds=2.0)
    CommonFunc_20005210(0, character=4500424, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500425, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500426, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500427, animation_id=701, animation_id_1=1701, radius=3.0)
    CommonFunc_20005210(0, character=4500428, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500429, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500430, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005201(0, character=4500431, animation_id=700, animation_id_1=1700, region=4502440, seconds=0.5)
    CommonFunc_20005201(0, character=4500432, animation_id=700, animation_id_1=1700, region=4502440, seconds=1.0)
    CommonFunc_20005201(
        0,
        character=4500433,
        animation_id=700,
        animation_id_1=1700,
        region=4502440,
        seconds=0.4000000059604645,
    )
    CommonFunc_20005210(0, character=4500434, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500435, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005210(0, character=4500436, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005211(0, character=4500440, animation_id=701, animation_id_1=1701, radius=4.0, seconds=1.0)
    CommonFunc_20005210(0, character=4500441, animation_id=705, animation_id_1=1705, radius=2.0)
    CommonFunc_20005202(0, character=4500442, animation_id=704, animation_id_1=1704, region=4502419)
    CommonFunc_20005133(0, character=4500443, animation_id=3015, radius=1.0, region=4502330)
    CommonFunc_20005133(0, character=4500444, animation_id=3016, radius=1.0, region=4502444)
    CommonFunc_20005220(0, character=4500445, animation_id=705, animation_id_1=1705)
    CommonFunc_20005260(0, character=4500446, animation_id=705, animation_id_1=1705, character_1=4500457)
    CommonFunc_20005210(0, character=4500447, animation_id=705, animation_id_1=1705, radius=2.0)
    CommonFunc_20005119(
        0,
        character=4500448,
        region=4502446,
        region_1=4502447,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005133(0, character=4500449, animation_id=3015, radius=3.0, region=4502426)
    CommonFunc_20005133(0, character=4500451, animation_id=3015, radius=3.0, region=4502442)
    CommonFunc_20005132(0, character=4500452, radius=2.0, region=4502445)
    CommonFunc_20005133(0, character=4500453, animation_id=3015, radius=3.0, region=4502426)
    CommonFunc_20005134(0, character=4500454, animation_id=3010, radius=3.0, region=4502441)
    CommonFunc_20005210(0, character=4500458, animation_id=701, animation_id_1=1701, radius=4.0)
    CommonFunc_20005201(0, character=4500461, animation_id=703, animation_id_1=1703, region=4502449, seconds=2.0)
    CommonFunc_20005132(0, character=4500463, radius=2.0, region=4502428)
    CommonFunc_20005132(0, character=4500464, radius=2.0, region=4502428)
    CommonFunc_20005132(0, character=4500465, radius=2.0, region=4502428)
    CommonFunc_20005132(0, character=4500466, radius=2.0, region=4502428)
    CommonFunc_20005132(0, character=4500468, radius=2.0, region=4502428)
    CommonFunc_20005132(0, character=4500467, radius=2.0, region=4502429)
    CommonFunc_20005132(0, character=4500469, radius=2.0, region=4502429)
    CommonFunc_20005213(0, character=4500474, animation_id=701, animation_id_1=1701, radius=2.0, region=4502421)
    CommonFunc_20005210(0, character=4500475, animation_id=702, animation_id_1=1702, radius=2.0)
    CommonFunc_20005221(0, character=4500476, animation_id=701, animation_id_1=1701, radius=3.0)
    CommonFunc_20005201(0, character=4500482, animation_id=702, animation_id_1=1702, region=4502403, seconds=2.0)
    Event_14505470(0, character=4500460, animation_id=708, animation_id_1=20000, region=4502421, seconds=0.5)
    Event_14505470(2, character=4500477, animation_id=708, animation_id_1=20000, region=4502421, seconds=3.0)
    Event_14505470(3, character=4500478, animation_id=708, animation_id_1=20000, region=4502425, seconds=0.0)
    Event_14505470(4, character=4500450, animation_id=708, animation_id_1=20000, region=4502448, seconds=0.0)
    CommonFunc_20005265(0, character=4500470, animation_id=703, animation_id_1=1703, character_1=4500472)
    CommonFunc_20006040(0, character=4500470, destination=4502413, special_effect=5450)
    CommonFunc_20005265(0, character=4500471, animation_id=702, animation_id_1=1702, character_1=4500472)
    CommonFunc_20005221(0, character=4500472, animation_id=701, animation_id_1=1701, radius=6.0)
    CommonFunc_20005132(0, character=4500480, radius=2.0, region=4502414)
    CommonFunc_20005132(0, character=4500481, radius=2.0, region=4502414)
    CommonFunc_20005132(0, character=4500487, radius=2.0, region=4502414)
    CommonFunc_20005132(0, character=4500488, radius=2.0, region=4502414)
    CommonFunc_20005132(0, character=4500489, radius=2.0, region=4502414)
    CommonFunc_20005132(0, character=4500490, radius=2.0, region=4502414)
    CommonFunc_20005132(0, character=4500491, radius=2.0, region=4502414)
    CommonFunc_20005221(0, character=4500492, animation_id=707, animation_id_1=1707, radius=3.0)
    CommonFunc_20005265(0, character=4500493, animation_id=701, animation_id_1=1701, character_1=4500492)
    CommonFunc_20005222(0, character=4500494, animation_id=700, animation_id_1=1700, radius=7.0, seconds=1.0)
    CommonFunc_20005221(0, character=4500497, animation_id=701, animation_id_1=1701, radius=6.0)
    Event_14505420(
        1,
        character=4500455,
        animation_id=705,
        animation_id_1=1705,
        character_1=4505483,
        region=4502431,
        character_2=4500403,
    )
    Event_14505420(
        2,
        character=4500456,
        animation_id=705,
        animation_id_1=1705,
        character_1=4505483,
        region=4502434,
        character_2=4500403,
    )
    Event_14505420(
        3,
        character=4500456,
        animation_id=705,
        animation_id_1=1705,
        character_1=4505483,
        region=4502435,
        character_2=4500403,
    )
    Event_14505430(0, character=4500480, region=4502430, character_1=4505483, character_2=4500403)
    Event_14505430(1, character=4500481, region=4502431, character_1=4505483, character_2=4500403)
    Event_14505430(2, character=4500483, region=4502434, character_1=4505483, character_2=4500403)
    Event_14505430(3, character=4500484, region=4502435, character_1=4505483, character_2=4500403)
    Event_14505430(4, character=4500485, region=4502431, character_1=4505483, character_2=4500403)
    Event_14505430(5, character=4500486, region=4502435, character_1=4505483, character_2=4500403)
    Event_14505430(6, character=4500487, region=4502434, character_1=4505483, character_2=4500403)
    Event_14505430(7, character=4500488, region=4502433, character_1=4505483, character_2=4500403)
    Event_14505430(8, character=4500489, region=4502431, character_1=4505483, character_2=4500403)
    Event_14505430(9, character=4500490, region=4502432, character_1=4505483, character_2=4500403)
    Event_14505430(10, character=4500491, region=4502430, character_1=4505483, character_2=4500403)
    CommonFunc_20005221(0, character=4500390, animation_id=700, animation_id_1=1700, radius=7.0)
    CommonFunc_20005201(0, character=4500391, animation_id=700, animation_id_1=1700, region=4502350, seconds=1.0)
    CommonFunc_20005290(0, character=4500381, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=4500382, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=4500383, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=4500384, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=4500385, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=4500386, animation_id=700, animation_id_1=1700)
    CommonFunc_20005290(0, character=4500387, animation_id=700, animation_id_1=1700)
    CommonFunc_20005200(0, character=4500670, animation_id=701, animation_id_1=1701, region=4502490)
    CommonFunc_20005205(0, character=4500671, animation_id=702, animation_id_1=1702, region=4502490, seconds=6.0)
    Event_14505490(1, character=4500672, animation_id=702, animation_id_1=1702)
    Event_14505495()
    CommonFunc_20005110(0, character=4500503, region=4502470)
    CommonFunc_20005110(0, character=4500504, region=4502470)
    CommonFunc_20005119(
        0,
        character=4500506,
        region=4502470,
        region_1=4502471,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=4500507,
        region=4502470,
        region_1=4502471,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=4500508,
        region=4502470,
        region_1=4502471,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    Event_14505383()
    CommonFunc_20005110(0, character=4500509, region=4502281)
    CommonFunc_20005110(0, character=4500510, region=4502281)
    CommonFunc_20005120(0, character=4500511, radius=38.0)
    CommonFunc_20005110(0, character=4500512, region=4502282)
    CommonFunc_20005110(0, character=4500217, region=4502282)
    CommonFunc_20005110(0, character=4500513, region=4502283)
    CommonFunc_20005110(0, character=4500595, region=4502282)
    CommonFunc_20005110(0, character=4500516, region=4502390)
    CommonFunc_20005110(0, character=4500517, region=4502392)
    CommonFunc_20005110(0, character=4500518, region=4502284)
    CommonFunc_20005110(0, character=4500519, region=4502284)
    Event_14505380()
    Event_14505381()
    Event_14505382()
    CommonFunc_20005119(
        0,
        character=4500520,
        region=4502450,
        region_1=4502451,
        region_2=4502452,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=4500525,
        region=4502450,
        region_1=4502451,
        region_2=4502452,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=4500590,
        region=4502450,
        region_1=4502452,
        region_2=0,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=4500591,
        region=4502450,
        region_1=4502451,
        region_2=4502452,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005119(
        0,
        character=4500592,
        region=4502450,
        region_1=4502451,
        region_2=4502452,
        region_3=0,
        region_4=0,
        region_5=0,
        region_6=0,
    )
    CommonFunc_20005220(0, character=4500529, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500531, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500535, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500538, animation_id=700, animation_id_1=1700)
    CommonFunc_20005212(0, character=4500539, animation_id=700, animation_id_1=1700, radius=6.0, region=4502458)
    CommonFunc_20005212(0, character=4500540, animation_id=703, animation_id_1=1703, radius=6.0, region=4502458)
    CommonFunc_20005110(0, character=4500543, region=4502454)
    CommonFunc_20005222(0, character=4500545, animation_id=700, animation_id_1=1700, radius=10.0, seconds=2.0)
    CommonFunc_20005222(0, character=4500546, animation_id=700, animation_id_1=1700, radius=10.0, seconds=3.0)
    CommonFunc_20005221(0, character=4500552, animation_id=703, animation_id_1=1703, radius=9.100000381469727)
    CommonFunc_20005220(0, character=4500556, animation_id=701, animation_id_1=1701)
    CommonFunc_20005134(0, character=4500558, animation_id=3007, radius=3.0, region=4502457)
    CommonFunc_20005213(0, character=4500559, animation_id=700, animation_id_1=1700, radius=3.0, region=4502457)
    CommonFunc_20005361(
        0,
        character=4500520,
        character_1=4500521,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500520,
        character_1=4500522,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500520,
        character_1=4500523,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500520,
        character_1=4500524,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500520,
        character_1=4500525,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500520,
        character_1=4500526,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500520,
        character_1=4500527,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500520,
        character_1=4500533,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500520,
        character_1=4500538,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500543,
        character_1=4500541,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500543,
        character_1=4500542,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500543,
        character_1=4500543,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500543,
        character_1=4500544,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005361(
        0,
        character=4500543,
        character_1=4500547,
        entity=10000,
        special_effect=13083,
        special_effect_1=13080,
    )
    CommonFunc_20005218(
        0,
        character=4500566,
        animation_id=700,
        animation_id_1=1700,
        radius=20.0,
        region=4502261,
        seconds=0.5,
    )
    CommonFunc_20005218(
        0,
        character=4500567,
        animation_id=700,
        animation_id_1=1700,
        radius=20.0,
        region=4502261,
        seconds=0.0,
    )
    CommonFunc_20005218(
        0,
        character=4500568,
        animation_id=700,
        animation_id_1=1700,
        radius=20.0,
        region=4502261,
        seconds=1.0,
    )
    CommonFunc_20005218(
        0,
        character=4500569,
        animation_id=700,
        animation_id_1=1700,
        radius=20.0,
        region=4502261,
        seconds=1.2000000476837158,
    )
    CommonFunc_20005120(0, character=4500573, radius=35.0)
    CommonFunc_20005220(0, character=4500574, animation_id=701, animation_id_1=1701)
    CommonFunc_20005213(0, character=4500579, animation_id=700, animation_id_1=1700, radius=5.0, region=4502260)
    Event_14505370(0, character=4500576, animation_id=700, animation_id_1=1700, radius=5.0, seconds=10.0)
    Event_14505360()
    CommonFunc_20005210(0, character=4500581, animation_id=700, animation_id_1=1700, radius=30.0)
    CommonFunc_20005221(0, character=4500585, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005221(0, character=4500586, animation_id=700, animation_id_1=1700, radius=2.0)
    CommonFunc_20005210(0, character=4500600, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005210(0, character=4500603, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005215(0, character=4500605, animation_id=701, animation_id_1=1701, radius=6.0, seconds=0.0)
    CommonFunc_20005215(0, character=4500606, animation_id=701, animation_id_1=1701, radius=4.0, seconds=1.0)
    CommonFunc_20005210(0, character=4500607, animation_id=700, animation_id_1=1700, radius=8.0)
    CommonFunc_20005221(0, character=4500608, animation_id=700, animation_id_1=1700, radius=4.0)
    CommonFunc_20005221(0, character=4500609, animation_id=700, animation_id_1=1700, radius=5.0)
    CommonFunc_20005223(0, character=4500610, animation_id=700, animation_id_1=1700, seconds=5.0)
    CommonFunc_20005220(0, character=4500611, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500612, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500613, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500614, animation_id=700, animation_id_1=1700)
    CommonFunc_20005220(0, character=4500615, animation_id=700, animation_id_1=1700)
    CommonFunc_20005221(0, character=4500616, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005221(0, character=4500617, animation_id=700, animation_id_1=1700, radius=3.0)
    CommonFunc_20005120(0, character=4500618, radius=1.0)
    CommonFunc_20005220(0, character=4500619, animation_id=700, animation_id_1=1700)
    CommonFunc_20005120(0, character=4500620, radius=1.0)
    CommonFunc_20005202(0, character=4500621, animation_id=701, animation_id_1=1701, region=4502370)
    CommonFunc_20005212(0, character=4500622, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500623, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500624, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500625, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500626, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500627, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500628, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500629, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500630, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500631, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500632, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500633, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005205(0, character=4500634, animation_id=701, animation_id_1=1701, region=4502372, seconds=1.5)
    CommonFunc_20005205(0, character=4500635, animation_id=701, animation_id_1=1701, region=4502372, seconds=2.0)
    CommonFunc_20005212(0, character=4500636, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005205(0, character=4500637, animation_id=701, animation_id_1=1701, region=4502372, seconds=1.5)
    CommonFunc_20005212(0, character=4500638, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500639, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500640, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005212(0, character=4500641, animation_id=700, animation_id_1=1700, radius=6.0, region=4502372)
    CommonFunc_20005205(0, character=4500642, animation_id=701, animation_id_1=1701, region=4502372, seconds=6.5)
    CommonFunc_20005205(0, character=4500643, animation_id=701, animation_id_1=1701, region=4502372, seconds=7.5)
    CommonFunc_20005205(0, character=4500644, animation_id=701, animation_id_1=1701, region=4502372, seconds=2.5)
    CommonFunc_20005205(0, character=4500645, animation_id=701, animation_id_1=1701, region=4502372, seconds=4.0)
    CommonFunc_20005205(0, character=4500646, animation_id=701, animation_id_1=1701, region=4502372, seconds=5.0)
    CommonFunc_20005205(0, character=4500647, animation_id=701, animation_id_1=1701, region=4502372, seconds=3.0)
    CommonFunc_20005205(0, character=4500648, animation_id=701, animation_id_1=1701, region=4502372, seconds=3.0)
    CommonFunc_20005205(0, character=4500649, animation_id=701, animation_id_1=1701, region=4502372, seconds=4.0)
    CommonFunc_20005205(0, character=4500650, animation_id=701, animation_id_1=1701, region=4502372, seconds=3.0)
    CommonFunc_20005205(0, character=4500651, animation_id=701, animation_id_1=1701, region=4502372, seconds=2.0)
    CommonFunc_20005205(0, character=4500652, animation_id=701, animation_id_1=1701, region=4502372, seconds=4.0)
    CommonFunc_20005205(0, character=4500653, animation_id=701, animation_id_1=1701, region=4502372, seconds=5.0)
    CommonFunc_20005341(0, flag=14500480, character=4500680, item_lot=21509600)
    CommonFunc_20005341(0, flag=14500482, character=4500682, item_lot=21509620)
    CommonFunc_20005341(0, flag=14500484, character=4500684, item_lot=21509640)
    CommonFunc_20005341(0, flag=14500485, character=4500685, item_lot=21509650)
    CommonFunc_20005341(0, flag=14500487, character=4500687, item_lot=21509670)
    CommonFunc_20005341(0, flag=14500488, character=4500688, item_lot=21509680)
    CommonFunc_20005341(0, flag=14500489, character=4500689, item_lot=21509690)
    CommonFunc_20005110(0, character=4500680, region=4502295)
    CommonFunc_20005120(0, character=4500682, radius=10.0)
    CommonFunc_20005120(0, character=4500683, radius=14.0)
    CommonFunc_20005120(0, character=4500685, radius=8.0)
    Event_14500800()
    Event_14505810()
    Event_14505811()
    Event_14505812()
    Event_14505813()
    Event_14505820()
    Event_14505825()
    Event_14505829()
    CommonFunc_20005840(0, other_entity=4501800)
    CommonFunc_20005841(0, other_entity=4501800)
    CommonFunc_20005840(0, other_entity=4501801)
    CommonFunc_20005841(0, other_entity=4501801)
    Event_14505830()
    Event_14505831()
    Event_14505832()
    Event_14505833()
    Event_14505834()
    Event_14500860()
    Event_14505870()
    Event_14505871()
    Event_14505872()
    Event_14505873()
    Event_14505874()
    Event_14505889()
    CommonFunc_20005223(0, character=4500263, animation_id=701, animation_id_1=1701, seconds=3.0)
    CommonFunc_20005223(0, character=4500264, animation_id=701, animation_id_1=1701, seconds=3.0)
    CommonFunc_20005223(0, character=4500265, animation_id=700, animation_id_1=1700, seconds=3.0)
    Event_14505298()
    CommonFunc_20005840(0, other_entity=4501860)
    CommonFunc_20005841(0, other_entity=4501860)
    Event_14505890()
    CommonFunc_20005620(0, flag=14500510, flag_1=14501510, entity=4501510, obj=4501511, obj_1=4501512, flag_2=14501511)
    CommonFunc_20005628(0, flag=14500511, obj=4501512, region=4502511)
    Event_14505510()
    Event_14505500()
    Event_14505501()
    Event_14505520()
    Event_14505525()
    Event_14505580()
    Event_14505530(0, obj=4501530, region=4502530, seconds=0.75, left=4501260)
    Event_14505530(1, obj=4501531, region=4502531, seconds=0.25, left=0)
    Event_14505530(2, obj=4501532, region=4502532, seconds=0.25, left=0)
    Event_14505533(0, flag=14505530, region=4502535)
    Event_14505533(1, flag=14505531, region=4502536)
    Event_14505533(2, flag=14505532, region=4502537)
    Event_14505536(0, flag=14505530, region=4502535, obj=4501530, sound_id=450000020)
    Event_14505536(1, flag=14505531, region=4502536, obj=4501531, sound_id=450000021)
    Event_14505536(2, flag=14505532, region=4502537, obj=4501532, sound_id=450000021)
    Event_14505540(
        0,
        flag=14500540,
        obj=4501540,
        action_button_id=9370,
        collision=4503540,
        collision_1=4503541,
        obj_flag=14504540,
        obj_flag_1=14504541,
        obj_flag_2=14504543,
        obj_flag_3=14504544,
        obj_flag_4=0,
    )
    Event_14505540(
        1,
        flag=14500542,
        obj=4501542,
        action_button_id=9370,
        collision=4503542,
        collision_1=4503543,
        obj_flag=14504545,
        obj_flag_1=14504546,
        obj_flag_2=14504547,
        obj_flag_3=14504548,
        obj_flag_4=14504549,
    )
    Event_14505544(0, flag=14500540, region=4502540)
    Event_14505544(1, flag=14500542, region=4502542)
    CommonFunc_20005610(0, flag=14500550, region=4502550, region_1=4502551)
    CommonFunc_20005611(0, flag=14500550, obj_act_id=4503550, obj=4501550, obj_act_id_1=450300)
    CommonFunc_20005610(0, flag=14500552, region=4502552, region_1=4502553)
    CommonFunc_20005611(0, flag=14500552, obj_act_id=4503552, obj=4501552, obj_act_id_1=450300)
    CommonFunc_20005610(0, flag=14500554, region=4502554, region_1=4502555)
    CommonFunc_20005611(0, flag=14500554, obj_act_id=4503554, obj=4501554, obj_act_id_1=450300)
    CommonFunc_20005610(0, flag=14500556, region=4502556, region_1=4502557)
    CommonFunc_20005611(0, flag=14500556, obj_act_id=4503556, obj=4501556, obj_act_id_1=450320)
    CommonFunc_20005614(0, entity=4501570, flag=64500570)
    Event_14505580()
    Event_14505600()
    Event_14505610()
    Event_14505611()
    Event_14505620()
    Event_14505630()
    CommonFunc_20005650(0, flag=14500640, obj=4501640)
    CommonFunc_20005650(0, flag=14500641, obj=4501641)
    CommonFunc_20005780(0, obj=4501690, dummy_id=2)
    Event_14505670()
    Event_14505180()
    Event_14505181()
    Event_14505182()
    Event_14505183()
    CommonFunc_20006002(0, character=4500701, flag=1658, first_flag=1655, last_flag=1659)
    Event_14505701(0, character=4500700)
    Event_14500702(0, character=4500700, character_1=4500701)
    Event_14505703()
    CommonFunc_20006002(0, character=4500705, flag=1678, first_flag=1675, last_flag=1679)
    CommonFunc_20006002(0, character=4500706, flag=1678, first_flag=1675, last_flag=1679)
    Event_14505711()
    Event_14505712(0, character=4500705, character_1=4500706, obj=4506705, obj_1=4506706)
    Event_14505713(0, character=4500706)
    Event_14505714(0, other_entity=4500706)
    Event_14505720(0, entity=4500706)
    Event_14505721(0, obj=4506705, flag=1660)
    Event_14505721(1, obj=4506706, flag=1661)
    Event_14505741(0, character=4500710, obj=4501710)
    Event_14505742()
    Event_14500743(0, character=4500710, obj=4501710)
    CommonFunc_20006030(
        0,
        obj=4501711,
        action_button_id=4000,
        right=2,
        item_lot=55500,
        first_flag=50006550,
        last_flag=50006550,
        flag=1718,
    )
    CommonFunc_20006031(0, flag=74500331, region=4502705)
    CommonFunc_20006002(0, character=4500715, flag=1698, first_flag=1695, last_flag=1699)
    CommonFunc_20006002(0, character=4500716, flag=1698, first_flag=1695, last_flag=1699)
    CommonFunc_20006040(0, character=4500715, destination=4502720, special_effect=5450)
    Event_14505731(0, character=4500715, obj=4501715)
    Event_14505732(0, character=4500715, obj=4501715, character_1=4500716)
    Event_14505733()
    CommonFunc_20006030(
        0,
        obj=4501716,
        action_button_id=4000,
        right=2,
        item_lot=55400,
        first_flag=50006540,
        last_flag=50006540,
        flag=14500733,
    )
    CommonFunc_20006002(0, character=4500720, flag=1798, first_flag=1795, last_flag=1799)


@ContinueOnRest(50)
def Preconstructor():
    """Event 50"""
    DisableSoundEvent(sound_id=4504801)
    DisableSoundEvent(sound_id=4504802)
    DisableSoundEvent(sound_id=4504803)
    DisableSoundEvent(sound_id=4504804)
    DisableSoundEvent(sound_id=4504861)
    DisableSoundEvent(sound_id=4504862)
    Event_14505699()
    Event_14505700(0, character=4500700, character_1=4500701)
    Event_14505710(0, character=4500705, character_1=4500706, obj=4506705, obj_1=4506706)
    Event_14505740(0, character=4500710, character_1=4500801, character_2=4500800, obj=4501710)
    Event_14505750(0, character=4500803, character_1=4500802)
    Event_14505730(0, character=4500715, obj=4501715, character_1=4500716)
    Event_14505770(0, character=4500720)
    Event_14505771()
    Event_14505150()
    Event_14505160()
    Event_14505780()


@RestartOnRest(14505150)
def Event_14505150():
    """Event 14505150"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    DeleteVFX(4503150)
    DeleteVFX(4503151)
    DeleteVFX(4503152)
    DeleteVFX(4503153)
    DeleteVFX(4503154)
    DeleteVFX(4503155)
    DeleteVFX(4503156)
    AND_1.Add(FlagEnabled(6952))
    AND_1.Add(FlagEnabled(148))
    AND_1.Add(FlagEnabled(14500800))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    CreateVFX(4503150)
    CreateVFX(4503151)
    CreateVFX(4503152)
    CreateVFX(4503153)
    CreateVFX(4503154)
    CreateVFX(4503155)
    CreateVFX(4503156)


@RestartOnRest(14505160)
def Event_14505160():
    """Event 14505160"""
    DisableObject(4506101)
    GotoIfFlagEnabled(Label.L0, flag=14500162)
    AND_1.Add(FlagEnabled(9322))
    AND_1.Add(FlagEnabled(14500161))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    AND_2.Add(FlagEnabled(9322))
    AND_2.Add(FlagDisabled(14500161))
    if AND_2:
        return
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(FlagEnabled(9322))
    AND_3.Add(FlagEnabled(6952))
    
    MAIN.Await(AND_3)
    
    CreateTemporaryVFX(vfx_id=1060, anchor_entity=4501101, dummy_id=200, anchor_type=CoordEntityType.Object)

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(4506101)
    if PlayerNotInOwnWorld():
        return
    if FlagDisabled(14500162):
        EnableFlag(14500162)
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(LeavingSession())
    AND_4.Add(ActionButtonParamActivated(action_button_id=9344, entity=4501101))
    
    MAIN.Await(AND_4)
    
    BanishPhantoms(unknown=0)
    FaceEntity(PLAYER, 4501101, animation=91040)
    Wait(3.0)
    WarpToMap(game_map=DREG_HEAP, player_start=5002110)
    EnableFlag(14500160)


@RestartOnRest(14505180)
def Event_14505180():
    """Event 14505180"""
    if FlagEnabled(14505186):
        return
    DisableCharacter(4500176)
    DisableAnimations(4500176)


@RestartOnRest(14505181)
def Event_14505181():
    """Event 14505181"""
    EnableFlag(14505180)
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(14500176):
        return
    Wait(0.5)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 490))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4502177))
    
    MAIN.Await(AND_1)
    
    WaitRandomSeconds(min_seconds=1.0, max_seconds=4.0)
    SetNetworkConnectedFlagState(flag=14505185, state=FlagSetting.On)


@RestartOnRest(14505182)
def Event_14505182():
    """Event 14505182"""
    if FlagEnabled(14500176):
        return
    if FlagEnabled(14505186):
        return
    AND_1.Add(FlagEnabled(14505185))
    AND_1.Add(FlagDisabled(14505186))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012700, display_location_index=1)
    SkipLines(5)
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionTrue(2, AND_1)
    DisplayBattlefieldMessage(10012700, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012700, display_location_index=1)
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=30310, anchor_entity=4500176, dummy_id=236, anchor_type=CoordEntityType.Character)
    EnableCharacter(4500176)
    EnableAnimations(4500176)
    SetBackreadStateAlternate(4500176, True)
    SetNetworkUpdateRate(4500176, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(4500176, 63010, unknown2=1.0)
    SetNetworkConnectedFlagState(flag=14505186, state=FlagSetting.On)


@RestartOnRest(14505183)
def Event_14505183():
    """Event 14505183"""
    if FlagEnabled(14500176):
        return
    AND_1.Add(FlagEnabled(14505186))
    AND_1.Add(CharacterDead(4500176))
    
    MAIN.Await(AND_1)
    
    DisplayBanner(BannerType.BlackPhantomDestroyed)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012701, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012701, display_location_index=1)
    Wait(2.0)
    AwardItemLot(59200, host_only=False)
    SetBackreadStateAlternate(4500176, False)
    SetNetworkUpdateRate(4500176, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    SetNetworkConnectedFlagState(flag=14500176, state=FlagSetting.On)


@RestartOnRest(14505200)
def Event_14505200():
    """Event 14505200"""
    if FlagEnabled(14500200):
        return
    if FlagEnabled(14500860):
        return
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502200))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502207))
    AND_2.Add(CharacterBackreadEnabled(4500201))
    AND_2.Add(FlagEnabled(14505202))
    OR_2.Add(AND_2)
    OR_2.Add(HealthRatio(4500201) <= 0.6000000238418579)
    AND_3.Add(CharacterOutsideRegion(character=4500201, region=4502205))
    AND_3.Add(CharacterOutsideRegion(character=4500201, region=4502206))
    OR_2.Add(AND_3)
    AND_4.Add(OR_2)
    AND_4.Add(FlagDisabled(14505207))
    AND_4.Add(FlagEnabled(14505206))
    OR_3.Add(AND_4)
    OR_3.Add(HasAIStatus(4500860, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_3)
    
    AND_5.Add(HealthRatio(4500201) <= 0.6000000238418579)
    GotoIfConditionTrue(Label.L0, input_condition=AND_5)
    AICommand(4500201, command_id=10, command_slot=0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=14505209, state=FlagSetting.On)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(4500201, 3025, skip_transition=True, unknown2=1.0)
    if PlayerNotInOwnWorld():
        return
    Wait(3.0)
    SetNetworkConnectedFlagState(flag=14500200, state=FlagSetting.On)
    AwardItemLot(60300010, host_only=False)
    AddSpecialEffect(4505201, 13032)
    End()


@RestartOnRest(14505201)
def Event_14505201():
    """Event 14505201"""
    GotoIfFlagDisabled(Label.L0, flag=14500860)
    GotoIfFlagDisabled(Label.L0, flag=14500200)
    GotoIfFlagDisabled(Label.L0, flag=14505200)
    DisableCharacter(4500201)
    DisableAI(4500201)
    SetNetworkUpdateRate(4500201, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    AddSpecialEffect(4505201, 13032)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfPlayerInOwnWorld(Label.L1)
    GotoIfFlagDisabled(Label.L2, flag=14505206)
    GotoIfFlagEnabled(Label.L3, flag=14505202)
    DisableAI(4500201)
    DisableGravity(4500201)
    DisableCharacterCollision(4500201)
    EnableImmortality(4500201)

    # --- Label 3 --- #
    DefineLabel(3)
    SetNetworkUpdateRate(4500201, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 1 --- #
    DefineLabel(1)

    # --- Label 2 --- #
    DefineLabel(2)
    DisableAI(4500201)
    DisableGravity(4500201)
    DisableCharacterCollision(4500201)
    EnableImmortality(4500201)
    DisableCharacter(4500201)
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    OR_2.Add(HasAIStatus(4500240, ai_status=AIStatusType.Battle))
    OR_2.Add(HasAIStatus(4500241, ai_status=AIStatusType.Battle))
    OR_3.Add(OR_2)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=4502201))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502203))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502204))
    OR_3.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(OR_3)
    AND_3.Add(CharacterBackreadEnabled(4500201))
    AND_3.Add(FlagDisabled(14500860))
    
    MAIN.Await(AND_3)
    
    if FlagEnabled(14500860):
        return
    if FlagEnabled(14500200):
        return
    if FlagEnabled(14505200):
        return
    if FlagEnabled(14505210):
        return
    if FlagEnabled(14505216):
        return
    if FlagEnabled(14505896):
        return
    EnableFlag(14505206)
    EnableCharacter(4500201)
    EnableAI(4500201)
    SetNetworkUpdateRate(4500201, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ForceAnimation(4500201, 20002, wait_for_completion=True, unknown2=1.0)
    EnableFlag(14505207)
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=4502201))
    if OR_4:
        return
    WaitFrames(frames=1)
    ForceAnimation(4500201, 20007, unknown2=1.0)


@RestartOnRest(14505202)
def Event_14505202():
    """Event 14505202"""
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterBackreadEnabled(4500201))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=4502202))
    OR_2.Add(AND_2)
    OR_2.Add(AttackedWithDamageType(attacked_entity=4500201, attacker=PLAYER))
    AND_3.Add(OR_2)
    AND_3.Add(FlagEnabled(14505207))
    
    MAIN.Await(AND_3)
    
    if FlagEnabled(14500860):
        return
    if FlagEnabled(14500200):
        return
    if FlagEnabled(14505200):
        return
    if FlagEnabled(14505210):
        return
    if FlagEnabled(14505216):
        return
    if FlagEnabled(14505896):
        return
    AddSpecialEffect(4505201, 13024)
    DisableFlag(14505207)
    EnableGravity(4500201)
    EnableCharacterCollision(4500201)
    ForceAnimation(4500201, 20005, wait_for_completion=True, unknown2=1.0)
    ReplanAI(4500201)


@RestartOnRest(14505203)
def Event_14505203():
    """Event 14505203"""
    if FlagEnabled(14500860):
        return
    if FlagEnabled(14500200):
        return
    if ThisEventSlotFlagEnabled():
        return
    if FlagEnabled(14505216):
        return
    OR_1.Add(CharacterHasTAEEvent(4500201, tae_event_id=100))
    OR_1.Add(CharacterDead(4500201))
    OR_1.Add(FlagEnabled(14505216))
    OR_1.Add(FlagEnabled(14505896))
    AND_1.Add(FlagEnabled(14505207))
    AND_1.Add(FlagEnabled(14505209))
    OR_1.Add(AND_1)
    
    MAIN.Await(OR_1)
    
    SetNetworkConnectedFlagState(flag=14505206, state=FlagSetting.Off)
    GotoIfFlagDisabled(Label.L0, flag=14505207)
    AddSpecialEffect(4500201, 13109)
    Wait(3.0)

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkUpdateRate(4500201, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    DisableCharacter(4500201)


@RestartOnRest(14505204)
def Event_14505204():
    """Event 14505204"""
    if FlagEnabled(14500860):
        return
    if FlagEnabled(14500200):
        return
    if ThisEventSlotFlagEnabled():
        return
    if FlagEnabled(14505202):
        return
    AND_1.Add(FlagEnabled(14505206))
    AND_1.Add(FlagDisabled(14505202))
    AND_1.Add(FlagDisabled(14505865))
    AND_1.Add(CharacterAlive(4505212, target_comparison_type=ComparisonType.LessThanOrEqual, target_count=2.0))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(14505202):
        return
    if FlagEnabled(14500860):
        return
    if FlagEnabled(14500200):
        return
    ForceAnimation(4500201, 20007, unknown2=1.0)
    RemoveSpecialEffect(4505240, 5022)
    RemoveSpecialEffect(4505242, 5022)
    RemoveSpecialEffect(4505240, 13024)
    RemoveSpecialEffect(4505242, 13024)
    AddSpecialEffect(4505240, 13020)
    AddSpecialEffect(4505242, 13020)
    AddSpecialEffect(4505242, 13022)
    AddSpecialEffect(4505247, 13022)
    AddSpecialEffect(4505247, 13023)
    AddSpecialEffect(4505247, 13020)
    RemoveSpecialEffect(4505247, 13024)
    RemoveSpecialEffect(4505247, 5022)
    SetCharacterEventTarget(4500247, entity=PLAYER)
    SetCharacterEventTarget(4500248, entity=PLAYER)
    SetCharacterEventTarget(4500249, entity=PLAYER)


@RestartOnRest(14505210)
def Event_14505210():
    """Event 14505210"""
    if FlagEnabled(14500210):
        return
    if FlagEnabled(14500860):
        return
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502210))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502217))
    AND_2.Add(CharacterBackreadEnabled(4500202))
    OR_2.Add(AND_2)
    OR_2.Add(HealthRatio(4500202) <= 0.6000000238418579)
    OR_2.Add(HasAIStatus(4500860, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterOutsideRegion(character=4500202, region=4502215))
    OR_2.Add(CharacterInsideRegion(character=4500202, region=4502216))
    AND_3.Add(OR_2)
    AND_3.Add(FlagEnabled(14505216))
    
    MAIN.Await(AND_3)
    
    AND_4.Add(HealthRatio(4500202) <= 0.6000000238418579)
    GotoIfConditionTrue(Label.L0, input_condition=AND_4)
    AICommand(4500202, command_id=10, command_slot=0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=14505219, state=FlagSetting.On)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(4500202, 3025, unknown2=1.0)
    Wait(4.0)
    if PlayerNotInOwnWorld():
        return
    SetNetworkConnectedFlagState(flag=14500210, state=FlagSetting.On)
    AwardItemLot(60300020, host_only=False)
    AddSpecialEffect(4505202, 13032)


@RestartOnRest(14505211)
def Event_14505211():
    """Event 14505211"""
    GotoIfFlagEnabled(Label.L1, flag=14500860)
    GotoIfFlagEnabled(Label.L1, flag=14500210)
    GotoIfFlagEnabled(Label.L1, flag=14505210)
    GotoIfFlagEnabled(Label.L0, flag=14500216)
    DisableAI(4500202)
    DisableGravity(4500202)
    DisableCharacterCollision(4500202)
    EnableImmortality(4500202)
    ForceAnimation(4500202, 30003, loop=True, unknown2=1.0)
    DisableAnimations(4500202)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=4502211))
    AND_2.Add(CharacterBackreadEnabled(4500202))
    AND_2.Add(FlagDisabled(14500860))
    AND_2.Add(FlagDisabled(14500860))
    
    MAIN.Await(AND_2)
    
    GotoIfFlagEnabled(Label.L0, flag=14505896)
    EnableFlag(14505216)
    SetNetworkUpdateRate(4500202, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(4500202)
    EnableGravity(4500202)
    EnableCharacterCollision(4500202)
    EnableAnimations(4500202)
    WaitFrames(frames=1)
    ForceAnimation(4500202, 20009, wait_for_completion=True, unknown2=1.0)
    ReplanAI(4500202)
    EnableFlag(14505217)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetNetworkUpdateRate(4500202, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableAI(4500202)
    EnableGravity(4500202)
    EnableCharacterCollision(4500202)
    EnableAnimations(4500202)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(4500202)
    DisableAnimations(4500202)
    DisableAI(4500202)
    AddSpecialEffect(4505202, 13032)
    AddSpecialEffect(4505202, 13032)


@RestartOnRest(14505213)
def Event_14505213():
    """Event 14505213"""
    if FlagEnabled(14500860):
        return
    if FlagEnabled(14500210):
        return
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(CharacterHasTAEEvent(4500202, tae_event_id=100))
    OR_1.Add(CharacterDead(4500202))
    OR_1.Add(FlagEnabled(14505896))
    
    MAIN.Await(OR_1)
    
    AND_5.Add(HasAIStatus(4500860, ai_status=AIStatusType.Battle))
    SkipLinesIfConditionFalse(1, AND_1)
    DisableFlag(14505216)
    SetNetworkUpdateRate(4500202, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    DisableCharacter(4500202)
    RemoveSpecialEffect(4505219, 5022)
    DisableFlag(14505216)
    End()


@RestartOnRest(14505240)
def Event_14505240(_, character: int, special_effect: int):
    """Event 14505240"""
    AddSpecialEffect(character, special_effect)


@RestartOnRest(14505245)
def Event_14505245(_, character: int, entity: int):
    """Event 14505245"""
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    SetCharacterEventTarget(character, entity=entity)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    OR_1.Add(TimeElapsed(seconds=60.0))
    OR_1.Add(FlagEnabled(14505206))
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    AddSpecialEffect(character, 5022)


@RestartOnRest(14505250)
def Event_14505250(_, character: int, character_1: int):
    """Event 14505250"""
    if ThisEventSlotFlagEnabled():
        return
    OR_1.Add(CharacterHasSpecialEffect(character, 13022))
    OR_2.Add(CharacterHasSpecialEffect(character, 13023))
    OR_3.Add(OR_1)
    OR_3.Add(OR_2)
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    GotoIfLastConditionResultTrue(Label.L0, input_condition=OR_1)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterEventTarget(character, entity=PLAYER)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(CharacterDead(character_1))
    SkipLinesIfConditionTrue(1, AND_3)
    SetCharacterEventTarget(character, entity=character_1)
    End()


@RestartOnRest(14505260)
def Event_14505260(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    seconds_1: float,
    animation_id_2: int,
):
    """Event 14505260"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_1.Add(FlagEnabled(14505217))
    AND_1.Add(FlagDisabled(14505213))
    OR_1.Add(AND_1)
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=4502211))
    AND_2.Add(FlagEnabled(14505210))
    OR_1.Add(AND_2)
    AND_3.Add(OR_1)
    AND_3.Add(CharacterBackreadEnabled(character))
    AND_3.Add(CharacterHasSpecialEffect(character, 5450))
    OR_2.Add(AND_3)
    OR_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    AND_4.Add(OR_2)
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_3.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_4.Add(OR_3)
    
    MAIN.Await(AND_4)
    
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L1, input_condition=AND_2)
    GotoIfFlagEnabled(Label.L0, flag=14505213)
    Wait(seconds)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, wait_for_completion=True, unknown2=1.0)
    ReplanAI(character)
    AddSpecialEffect(character, 5022)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    Wait(seconds_1)
    ForceAnimation(character, animation_id_2, wait_for_completion=True, unknown2=1.0)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, wait_for_completion=True, unknown2=1.0)
    ReplanAI(character)
    AddSpecialEffect(character, 5022)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)


@RestartOnRest(14505270)
def Event_14505270(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    seconds: float,
    region: int,
    animation_id_2: int,
    seconds_1: float,
    region_1: int,
):
    """Event 14505270"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_1)
    AND_5.Add(CharacterInsideRegion(character=PLAYER, region=region_1))
    OR_4.Add(CharacterInsideRegion(character=PLAYER, region=region))
    OR_4.Add(AND_5)
    AND_3.Add(OR_4)
    OR_3.Add(AND_3)
    AND_4.Add(CharacterHasSpecialEffect(character, 13020))
    OR_3.Add(AND_4)
    AND_1.Add(OR_3)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    OR_2.Add(AND_1)
    OR_2.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_4)
    GotoIfLastConditionResultTrue(Label.L1, input_condition=AND_5)
    Wait(seconds)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ReplanAI(character)
    ForceAnimation(character, animation_id_1, wait_for_completion=True, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(seconds_1)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ReplanAI(character)
    ForceAnimation(character, animation_id_2, wait_for_completion=True, unknown2=1.0)
    AddSpecialEffect(character, 5000)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(14505280)
def Event_14505280():
    """Event 14505280"""
    AddSpecialEffect(4500212, 13027)
    
    MAIN.Await(CharacterHasSpecialEffect(4500212, 13029))
    
    AddSpecialEffect(4500212, 13022)
    AddSpecialEffect(4500213, 13022)
    Wait(1.7999999523162842)
    AddSpecialEffect(4505242, 13022)
    if FlagDisabled(14505281):
        AddSpecialEffect(4505242, 13031)
        End()
    RemoveSpecialEffect(4505242, 13031)
    SetCharacterEventTarget(4505242, entity=PLAYER)


@RestartOnRest(14505281)
def Event_14505281():
    """Event 14505281"""
    AddSpecialEffect(4500210, 13027)
    
    MAIN.Await(CharacterHasSpecialEffect(4500210, 13029))
    
    AddSpecialEffect(4500212, 13034)
    AddSpecialEffect(4500240, 13034)
    AddSpecialEffect(4500241, 13034)
    AddSpecialEffect(4500212, 13022)
    AddSpecialEffect(4500240, 13022)
    AddSpecialEffect(4500241, 13022)
    RemoveSpecialEffect(4500212, 13026)
    AddSpecialEffect(4500240, 5020)
    AddSpecialEffect(4500241, 5020)
    RemoveSpecialEffect(4500212, 13024)
    RemoveSpecialEffect(4500240, 13024)
    RemoveSpecialEffect(4500241, 13024)
    Wait(3.799999952316284)
    GotoIfFlagEnabled(Label.L0, flag=14505280)
    AddSpecialEffect(4505242, 13022)
    AddSpecialEffect(4505242, 13031)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(4505242, 13031)
    SetCharacterEventTarget(4505242, entity=PLAYER)


@RestartOnRest(14505282)
def Event_14505282(_, character: int, region: int):
    """Event 14505282"""
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    AND_1.Add(CharacterHasSpecialEffect(character, 13031))
    
    MAIN.Await(AND_1)
    
    Wait(6.0)
    RemoveSpecialEffect(character, 13022)
    RemoveSpecialEffect(character, 13031)
    ClearTargetList(character)


@RestartOnRest(14505290)
def Event_14505290(_, character: int, region: int, special_effect: int):
    """Event 14505290"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(CharacterHasSpecialEffect(character, special_effect))
    AND_1.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_1)
    
    AddSpecialEffect(character, 13031)
    SetEventPoint(character, region=region, reaction_range=3.0)


@RestartOnRest(14505298)
def Event_14505298():
    """Event 14505298"""
    if FlagEnabled(14500860):
        return
    if PlayerNotInOwnWorld():
        return
    EnableCharacter(4500263)
    EnableCharacter(4500264)
    EnableCharacter(4500265)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=4502298))
    
    DisableCharacter(4500263)
    DisableCharacter(4500264)
    DisableCharacter(4500265)
    
    MAIN.Await(CharacterOutsideRegion(character=PLAYER, region=4502298))
    
    Wait(10.0)
    Restart()


@RestartOnRest(14505300)
def Event_14505300(_, character: int, other_entity: int, radius: float):
    """Event 14505300"""
    if CharacterHasSpecialEffect(character=character, special_effect=5404):
        return
    AND_1.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_1.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_1)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_2.Add(OR_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=radius))
    AND_2.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_2)
    
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    Wait(10.0)
    AICommand(character, command_id=-1, command_slot=0)
    End()


@RestartOnRest(14505310)
def Event_14505310(_, character: int):
    """Event 14505310"""
    EnableInvincibility(character)
    DisableHealthBar(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    DisableAI(character)


@RestartOnRest(14505350)
def Event_14505350(_, character: int):
    """Event 14505350"""
    DisableAnimations(character)
    DisableAI(character)
    DisableHealthBar(character)
    SetLockOnPoint(character=character, lock_on_dummy_id=220, state=False)
    DisableGravity(character)
    AddSpecialEffect(character, 13028)


@RestartOnRest(14505360)
def Event_14505360():
    """Event 14505360"""
    AddSpecialEffect(4500570, 5022)


@RestartOnRest(14505370)
def Event_14505370(_, character: int, animation_id: int, animation_id_1: int, radius: float, seconds: float):
    """Event 14505370"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_9.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_1.Add(AND_9)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    OR_1.Add(CharacterWhitePhantom(PLAYER))
    AND_3.Add(OR_1)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    OR_4.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_4.Add(HasAIStatus(character, ai_status=AIStatusType.Search))
    OR_4.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    AND_3.Add(OR_4)
    OR_3.Add(AND_3)
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Caution))
    OR_2.Add(HasAIStatus(character, ai_status=AIStatusType.Battle))
    OR_3.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    AND_1.Add(OR_3)
    OR_2.Add(AND_1)
    OR_2.Add(Attacked(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_2)
    
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    Wait(0.10000000149011612)
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    AND_4.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=radius))
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_1)
    Wait(seconds)

    # --- Label 1 --- #
    DefineLabel(1)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ReplanAI(character)
    ForceAnimation(character, animation_id_1, wait_for_completion=True, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(14505380)
def Event_14505380():
    """Event 14505380"""
    DisableNetworkSync()
    RemoveSpecialEffect(PLAYER, 4680)
    AND_9.Add(CharacterDead(4500500))
    if AND_9:
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502476))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502475))
    AND_1.Add(OR_1)
    AND_3.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_3.Add(AND_3)
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterHollow(PLAYER))
    OR_3.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_3)
    
    MAIN.Await(AND_1)
    
    AND_9.Add(EntityBeyondDistance(entity=PLAYER, other_entity=4500500, radius=14.0, min_target_count=0))
    AND_9.Add(ThisEventSlotFlagDisabled())
    SkipLinesIfConditionTrue(1, AND_9)
    Wait(5.0)
    AddSpecialEffect(PLAYER, 4680)
    Wait(0.5)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502476))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=4502475))
    OR_2.Add(AND_2)
    
    MAIN.Await(OR_2)
    
    Wait(0.5)
    Restart()


@RestartOnRest(14505381)
def Event_14505381():
    """Event 14505381"""
    DisableNetworkSync()
    
    MAIN.Await(CharacterHasSpecialEffect(PLAYER, 13067))
    
    SetCameraVibration(vibration_id=50, anchor_entity=4502476, anchor_type=CoordEntityType.Region)
    Wait(4.0)
    Restart()


@RestartOnRest(14505382)
def Event_14505382():
    """Event 14505382"""
    AND_3.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_3.Add(AND_3)
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterHollow(PLAYER))
    OR_3.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4502476))
    AND_1.Add(TimeElapsed(seconds=8.0))
    
    MAIN.Await(AND_1)
    
    SetCharacterEventTarget(4500500, entity=PLAYER)
    Restart()


@RestartOnRest(14505383)
def Event_14505383():
    """Event 14505383"""
    DisableCharacter(4500360)
    DisableBackread(4500360)


@RestartOnRest(14505400)
def Event_14505400(_, character: int, animation_id: int, animation_id_1: int, region: int, seconds: float):
    """Event 14505400"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
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
    OR_2.Add(HealthRatio(character) <= 0.9900000095367432)
    
    MAIN.Await(OR_2)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    SkipLinesIfLastConditionResultFalse(1, input_condition=AND_1)
    Wait(seconds)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ReplanAI(character)
    ForceAnimation(character, animation_id_1, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(14505410)
def Event_14505410():
    """Event 14505410"""
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502423))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502424))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterAlive(4500403))
    
    MAIN.Await(AND_1)
    
    SetNest(4500403, region=4502361)
    Wait(0.0)
    AddSpecialEffect(4500403, 13250)
    AICommand(4500403, command_id=200, command_slot=0)
    SetCharacterEventTarget(4500403, entity=4500483)
    ReplanAI(4500403)
    
    MAIN.Await(CharacterDead(4500483))
    
    SetCharacterEventTarget(4500403, entity=4500484)
    End()


@RestartOnRest(14505411)
def Event_14505411():
    """Event 14505411"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    OR_1.Add(CharacterDead(4505483, target_count=2.0))
    OR_1.Add(HasAIStatus(4500403, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)

    # --- Label 0 --- #
    DefineLabel(0)
    RemoveSpecialEffect(4500403, 13253)


@RestartOnRest(14505412)
def Event_14505412():
    """Event 14505412"""
    DisableNetworkSync()
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502423))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502424))
    AND_1.Add(OR_1)
    AND_1.Add(CharacterAlive(4500403))
    
    MAIN.Await(AND_1)
    
    SetNetworkUpdateRate(4500403, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502423))
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502424))
    OR_2.Add(AND_2)
    OR_2.Add(CharacterDead(4500403))
    
    MAIN.Await(OR_2)
    
    SetNetworkUpdateRate(4500403, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    Restart()


@RestartOnRest(14505420)
def Event_14505420(
    _,
    character: int,
    animation_id: int,
    animation_id_1: int,
    character_1: int,
    region: int,
    character_2: int,
):
    """Event 14505420"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_3.Add(HasAIStatus(character_2, ai_status=AIStatusType.Battle))
    AND_3.Add(EntityWithinDistance(entity=character, other_entity=character_2, radius=1.0, min_target_count=0))
    OR_2.Add(AND_3)
    OR_2.Add(CharacterDead(character_1, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    AND_1.Add(OR_2)
    AND_1.Add(CharacterBackreadEnabled(character))
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    OR_1.Add(AND_1)
    OR_1.Add(AttackedWithDamageType(attacked_entity=character, attacker=PLAYER))
    
    MAIN.Await(OR_1)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    ReplanAI(character)
    AddSpecialEffect(character, 5021)
    SetEventPoint(character, region=region, reaction_range=0.5)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(14505430)
def Event_14505430(_, character: int, region: int, character_1: int, character_2: int):
    """Event 14505430"""
    OR_1.Add(CharacterDead(character_1, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    OR_1.Add(HasAIStatus(character_2, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(character, 5021)
    SetEventPoint(character, region=region, reaction_range=0.5)


@RestartOnRest(14505450)
def Event_14505450(_, character: int, region: int, character_1: int):
    """Event 14505450"""
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Caution))
    OR_1.Add(HasAIStatus(character_1, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_1)
    
    AddSpecialEffect(character, 5021)
    SetEventPoint(character, region=region, reaction_range=0.5)
    ReplanAI(character)


@RestartOnRest(14505470)
def Event_14505470(_, character: int, animation_id: int, animation_id_1: int, region: int, seconds: float):
    """Event 14505470"""
    if ThisEventSlotFlagEnabled():
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    AND_9.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
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
    Wait(seconds)
    SetNetworkUpdateRate(character, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableGravity(character)
    EnableCharacterCollision(character)
    ReplanAI(character)
    ForceAnimation(character, animation_id_1, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(character, is_fixed=False, update_rate=CharacterUpdateRate.Always)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableGravity(character)
    EnableCharacterCollision(character)


@RestartOnRest(14505490)
def Event_14505490(_, character: int, animation_id: int, animation_id_1: int):
    """Event 14505490"""
    if FlagEnabled(14505494):
        return
    DisableGravity(character)
    DisableCharacterCollision(character)
    ForceAnimation(character, animation_id, loop=True, unknown2=1.0)
    GotoIfFlagEnabled(Label.L0, flag=14505493)
    OR_1.Add(CharacterHuman(PLAYER))
    OR_1.Add(CharacterHollow(PLAYER))
    AND_2.Add(OR_1)
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=4502490))
    OR_2.Add(CharacterInsideRegion(character=PLAYER, region=4502491))
    AND_2.Add(OR_2)
    AND_2.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_2)
    
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterHollow(PLAYER))
    AND_4.Add(OR_3)
    AND_4.Add(FlagDisabled(14505493))
    AND_4.Add(ThisEventSlotFlagEnabled())
    AND_4.Add(CharacterInsideRegion(character=PLAYER, region=4502491))
    GotoIfConditionTrue(Label.L1, input_condition=AND_4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=14505493, state=FlagSetting.On)
    SkipLines(1)
    EnableFlag(14505493)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterHollow(PLAYER))
    AND_5.Add(OR_3)
    AND_5.Add(CharacterOutsideRegion(character=PLAYER, region=4502490))
    AND_5.Add(CharacterOutsideRegion(character=PLAYER, region=4502491))
    AND_5.Add(CharacterBackreadEnabled(character))
    
    MAIN.Await(AND_5)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=14505493, state=FlagSetting.Off)
    SkipLines(1)
    DisableFlag(14505493)
    Restart()

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=14505494, state=FlagSetting.On)
    EnableCharacterCollision(character)
    ForceAnimation(character, animation_id_1, unknown2=1.0)
    EnableCharacter(character)
    EnableGravity(character)
    ReplanAI(character)


@RestartOnRest(14505495)
def Event_14505495():
    """Event 14505495"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(14500495):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterDead(4500670))
    AND_1.Add(CharacterDead(4500671))
    
    MAIN.Await(AND_1)
    
    EnableFlag(14500495)
    AwardItemLot(61300010, host_only=False)


@RestartOnRest(14505499)
def Event_14505499():
    """Event 14505499"""
    if ThisEventSlotFlagEnabled():
        return
    ClearTargetList(4505499)
    ReplanAI(4505499)


@RestartOnRest(14505500)
def Event_14505500():
    """Event 14505500"""
    ActivateCollisionAndCreateNavmesh(collision=4503505, state=False)
    ActivateCollisionAndCreateNavmesh(collision=4503506, state=False)
    OR_1.Add(ObjectDestroyed(4501503))
    OR_1.Add(ObjectDestroyed(4501504))
    GotoIfConditionTrue(Label.L0, input_condition=OR_1)
    AND_2.Add(ThisEventSlotFlagEnabled())
    AND_2.Add(PlayerNotInOwnWorld())
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    DisableObject(4501501)
    DisableObject(4501502)
    ActivateCollisionAndCreateNavmesh(collision=4503506, state=True)
    OR_2.Add(ObjectDestroyed(4501503))
    OR_2.Add(ObjectDestroyed(4501504))
    
    MAIN.Await(OR_2)
    
    SetNetworkConnectedFlagState(flag=14505500, state=FlagSetting.On)
    ActivateCollisionAndCreateNavmesh(collision=4503506, state=False)
    ActivateCollisionAndCreateNavmesh(collision=4503505, state=True)
    EnableObject(4501501)
    EnableObjectInvulnerability(4501501)
    WaitFrames(frames=1)
    DisableObject(4501503)
    DisableObject(4501504)
    ForceAnimation(4506500, 1, unknown2=1.0)
    Wait(10.0)
    DisableObject(4501501)
    Wait(6.0)
    EnableObject(4501502)
    WaitFrames(frames=1)
    RegisterLadder(start_climbing_flag=14500502, stop_climbing_flag=14500503, obj=4501502)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EndOfAnimation(obj=4501500, animation_id=2)
    DisableObject(4501501)
    EnableObject(4501502)
    DisableObject(4501503)
    DisableObject(4501504)
    RegisterLadder(start_climbing_flag=14500502, stop_climbing_flag=14500503, obj=4501502)
    ActivateCollisionAndCreateNavmesh(collision=4503505, state=True)
    
    MAIN.Await(ObjectBackreadEnabled(obj=4501500))
    
    EndOfAnimation(obj=4501500, animation_id=2)


@ContinueOnRest(14505501)
def Event_14505501():
    """Event 14505501"""
    OR_1.Add(ObjectDestroyed(4501503))
    OR_1.Add(ObjectDestroyed(4501504))
    if OR_1:
        return
    
    MAIN.Await(ObjectBackreadState_Alternate(obj=4506500, state=True))
    
    OR_2.Add(ObjectDestroyed(4501503))
    OR_2.Add(ObjectDestroyed(4501504))
    if OR_2:
        return
    ForceAnimation(4506500, 0, loop=True, unknown2=1.0)


@ContinueOnRest(14505510)
def Event_14505510():
    """Event 14505510"""
    CommonFunc_20005621(
        0,
        flag=14500510,
        flag_1=14501510,
        obj=4501510,
        obj_1=4501511,
        obj_act_id=4504511,
        obj_2=4501512,
        obj_act_id_1=4504512,
        region=4502511,
        region_1=4502512,
        flag_2=14501511,
        flag_3=14504510,
        left=0,
    )


@RestartOnRest(14505520)
def Event_14505520():
    """Event 14505520"""
    DisableNetworkSync()
    DeleteVFX(4503520)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502650))
    AND_1.Add(OR_1)
    AND_1.Add(FlagDisabled(14505521))
    
    MAIN.Await(AND_1)
    
    CreateVFX(4503520)
    AND_2.Add(CharacterOutsideRegion(character=PLAYER, region=4502650))
    OR_2.Add(AND_2)
    OR_2.Add(FlagEnabled(14505521))
    
    MAIN.Await(OR_2)
    
    AND_3.Add(FlagEnabled(14505521))
    GotoIfConditionTrue(Label.L0, input_condition=AND_3)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(4503520, erase_root_only=False)
    Restart()


@RestartOnRest(14505525)
def Event_14505525():
    """Event 14505525"""
    DisableNetworkSync()
    DeleteVFX(4503521)
    AND_1.Add(FlagDisabled(14505521))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502650))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502651))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502652))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502653))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502654))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502655))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502656))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502657))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502658))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502659))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502660))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502661))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502662))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502663))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502664))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502665))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502666))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502667))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502668))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502669))
    
    MAIN.Await(AND_1)
    
    CreateVFX(4503521)
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502650))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502651))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502652))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502653))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502654))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502655))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502656))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502657))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502658))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502659))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502660))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502661))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502662))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502663))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502664))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502665))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502666))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502667))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502668))
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502669))
    OR_1.Add(FlagEnabled(14505521))
    
    MAIN.Await(OR_1)
    
    AND_2.Add(FlagEnabled(14505521))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    Restart()

    # --- Label 0 --- #
    DefineLabel(0)
    DeleteVFX(4503521, erase_root_only=False)
    Restart()


@RestartOnRest(14505530)
def Event_14505530(_, obj: int, region: int, seconds: float, left: int):
    """Event 14505530"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=region))
    
    SetAutogeneratedEventSpecificFlag_1(unknown1=2, unknown2=1)
    Wait(seconds)
    DestroyObject_NoSlot(obj=obj)
    if ValueEqual(left=left, right=0):
        return
    ForceAnimation(left, 301, unknown2=1.0)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObject(obj)
    if ValueEqual(left=left, right=0):
        return
    ForceAnimation(left, 302, unknown2=1.0)


@RestartOnRest(14505533)
def Event_14505533(_, flag: int, region: int):
    """Event 14505533"""
    DisableNetworkSync()
    RemoveSpecialEffect(PLAYER, 4070)
    
    MAIN.Await(FlagEnabled(flag))
    
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=region)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(PLAYER, 4070)
    Wait(8.0)
    RemoveSpecialEffect(PLAYER, 4070)
    End()


@RestartOnRest(14505536)
def Event_14505536(_, flag: int, region: int, obj: int, sound_id: int):
    """Event 14505536"""
    DisableNetworkSync()
    AND_1.Add(ObjectDestroyed(obj))
    if AND_1:
        return
    if ThisEventSlotFlagEnabled():
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    PlaySoundEffect(obj, sound_id, sound_type=SoundType.a_Ambient)
    if CharacterOutsideRegion(character=PLAYER, region=region):
        return
    SetCameraVibration(vibration_id=104, anchor_entity=region, anchor_type=CoordEntityType.Region)
    Wait(5.0)
    End()


@RestartOnRest(14505540)
def Event_14505540(
    _,
    flag: int,
    obj: int,
    action_button_id: int,
    collision: int,
    collision_1: int,
    obj_flag: int,
    obj_flag_1: int,
    obj_flag_2: int,
    obj_flag_3: int,
    obj_flag_4: int,
):
    """Event 14505540"""
    ActivateCollisionAndCreateNavmesh(collision=collision, state=False)
    ActivateCollisionAndCreateNavmesh(collision=collision_1, state=False)
    GotoIfFlagDisabled(Label.L0, flag=flag)
    EndOfAnimation(obj=obj, animation_id=2)
    ActivateCollisionAndCreateNavmesh(collision=collision_1, state=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    ActivateCollisionAndCreateNavmesh(collision=collision, state=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(flag))
    AND_1.Add(ActionButtonParamActivated(action_button_id=action_button_id, entity=obj))
    
    MAIN.Await(AND_1)
    
    EnableFlag(flag)
    ActivateCollisionAndCreateNavmesh(collision=collision, state=False)
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, dummy_id=100, short_move=True)
    ForceAnimation(PLAYER, 60440, unknown2=1.0)
    ForceAnimation(obj, 1, unknown2=1.0)
    Wait(1.5)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        dummy_id=40,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=1.2999999523162842,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        dummy_id=41,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=1.2999999523162842,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        dummy_id=42,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=1.2999999523162842,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_3,
        obj=obj,
        dummy_id=43,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=1.2999999523162842,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_4,
        obj=obj,
        dummy_id=44,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=1.2999999523162842,
        repetition_time=0.0,
    )
    Wait(1.2999999523162842)
    RemoveObjectFlag(obj_flag=obj_flag)
    RemoveObjectFlag(obj_flag=obj_flag_1)
    RemoveObjectFlag(obj_flag=obj_flag_2)
    RemoveObjectFlag(obj_flag=obj_flag_3)
    RemoveObjectFlag(obj_flag=obj_flag_4)
    Wait(2.200000047683716)
    EndOfAnimation(obj=obj, animation_id=2)
    ActivateCollisionAndCreateNavmesh(collision=collision_1, state=True)


@RestartOnRest(14505544)
def Event_14505544(_, flag: int, region: int):
    """Event 14505544"""
    DisableNetworkSync()
    if FlagEnabled(flag):
        return
    
    MAIN.Await(FlagEnabled(flag))
    
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=region))
    if not AND_1:
        return
    Wait(2.640000104904175)
    SetCameraVibration(vibration_id=104, anchor_entity=4502476, anchor_type=CoordEntityType.Region)


@RestartOnRest(14505580)
def Event_14505580():
    """Event 14505580"""
    RegisterLadder(start_climbing_flag=14500580, stop_climbing_flag=14500581, obj=4501580)
    RegisterLadder(start_climbing_flag=14500582, stop_climbing_flag=14500583, obj=4501582)
    RegisterLadder(start_climbing_flag=14500584, stop_climbing_flag=14500585, obj=4501584)
    RegisterLadder(start_climbing_flag=14500586, stop_climbing_flag=14500587, obj=4501586)
    RegisterLadder(start_climbing_flag=14500588, stop_climbing_flag=14500589, obj=4501588)
    RegisterLadder(start_climbing_flag=14500590, stop_climbing_flag=14500591, obj=4501590)
    RegisterLadder(start_climbing_flag=14500592, stop_climbing_flag=14500593, obj=4501592)
    RegisterLadder(start_climbing_flag=14500594, stop_climbing_flag=14500595, obj=4501594)
    RegisterLadder(start_climbing_flag=14500596, stop_climbing_flag=14500597, obj=4501596)
    RegisterLadder(start_climbing_flag=14500598, stop_climbing_flag=14500599, obj=4501598)


@RestartOnRest(14505600)
def Event_14505600():
    """Event 14505600"""
    GotoIfFlagDisabled(Label.L0, flag=14500600)
    EndOfAnimation(obj=4501600, animation_id=2)
    DisableObjectActivation(4501601, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ObjectActivated(obj_act_id=4503601))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=14500600, state=FlagSetting.On)
    DisableObjectActivation(4501601, obj_act_id=-1)
    ForceAnimation(4501600, 1, loop=True, unknown2=1.0)


@RestartOnRest(14505610)
def Event_14505610():
    """Event 14505610"""
    ActivateCollisionAndCreateNavmesh(collision=4503611, state=False)
    ActivateCollisionAndCreateNavmesh(collision=4503612, state=False)
    GotoIfFlagDisabled(Label.L0, flag=14500610)
    PostDestruction(4501610)
    EndOfAnimation(obj=4501610, animation_id=2)
    DisableObjectActivation(4501611, obj_act_id=-1)
    PostDestruction(4506610)
    ActivateCollisionAndCreateNavmesh(collision=4503612, state=True)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableMapCollision(collision=4503610)
    ActivateCollisionAndCreateNavmesh(collision=4503611, state=True)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ObjectActivated(obj_act_id=4503611))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=14500610, state=FlagSetting.On)
    DisableObjectActivation(4501611, obj_act_id=-1)
    Wait(4.0)
    ActivateCollisionAndCreateNavmesh(collision=4503611, state=False)
    CreateHazard(
        obj_flag=14505611,
        obj=4501610,
        dummy_id=41,
        behavior_param_id=6200,
        target_type=DamageTargetType.Character_and_Map,
        radius=2.0,
        life=3.299999952316284,
        repetition_time=0.0,
    )
    ForceAnimation(4501610, 1, loop=True, wait_for_completion=True, unknown2=1.0)
    EnableMapCollision(collision=4503610)
    ActivateCollisionAndCreateNavmesh(collision=4503612, state=True)


@RestartOnRest(14505611)
def Event_14505611():
    """Event 14505611"""
    if FlagEnabled(14500610):
        return
    if PlayerNotInOwnWorld():
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ObjectActivated(obj_act_id=4503611))
    
    MAIN.Await(AND_1)
    
    WaitFrames(frames=1)
    DisplayDialog(text=10010884, anchor_entity=4501611, button_type=ButtonType.Yes_or_No)


@RestartOnRest(14505620)
def Event_14505620():
    """Event 14505620"""
    GotoIfFlagDisabled(Label.L0, flag=14500620)
    DisableObject(4501620)
    EnableObject(4501621)
    DisableObjectActivation(4501622, obj_act_id=-1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    EnableObject(4501620)
    DisableObject(4501621)
    EnableSoundEvent(sound_id=4504803)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(ObjectActivated(obj_act_id=4503622))
    AND_2.Add(PlayerNotInOwnWorld())
    AND_2.Add(FlagEnabled(14505621))
    OR_1.Add(AND_1)
    OR_1.Add(AND_2)
    
    MAIN.Await(OR_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetNetworkConnectedFlagState(flag=14505621, state=FlagSetting.On)
    DisableObjectActivation(4501622, obj_act_id=-1)
    DisableSoundEvent(sound_id=4504803)
    Wait(3.0)
    EnableFlag(14505521)
    WaitFrames(frames=1)
    GotoIfFlagEnabled(Label.L1, flag=14500743)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(45000030, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(45000030, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(45000030, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(45000031, cutscene_flags=0, player_id=10000)
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(45000031, cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut, player_id=10000)
    SkipLines(1)
    PlayCutscene(45000031, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)

    # --- Label 2 --- #
    DefineLabel(2)
    SetNetworkConnectedFlagState(flag=14500620, state=FlagSetting.On)
    DisableFlag(14505521)
    DisableObject(4501620)
    EnableObject(4501621)


@RestartOnRest(14505630)
def Event_14505630():
    """Event 14505630"""
    GotoIfFlagEnabled(Label.L0, flag=64500630)
    OR_1.Add(FlagEnabled(64500630))
    OR_1.Add(ObjectActivated(obj_act_id=4503631))
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)
    
    GotoIfFlagEnabled(Label.L0, flag=64500630)
    EnableFlag(64500630)
    ForceAnimation(4501630, 1, unknown2=1.0)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectActivation(4501630, obj_act_id=-1)
    DisableObjectActivation(4501631, obj_act_id=1456500)


@RestartOnRest(14505670)
def Event_14505670():
    """Event 14505670"""
    DisableNetworkSync()
    AND_1.Add(CharacterDead(4500350))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    RemoveObjectFlag(obj_flag=14505672)
    RemoveObjectFlag(obj_flag=14505673)
    ForceAnimation(4501670, 0, loop=True, unknown2=1.0)
    DisableObject(4501670)
    AND_2.Add(CharacterDead(4500350))
    AND_2.Add(ObjectBackreadEnabled(obj=4501670))
    
    MAIN.Await(AND_2)
    
    Wait(2.0)
    EnableObject(4501670)
    ForceAnimation(4501670, 1, wait_for_completion=True, unknown2=1.0)
    Goto(Label.L1)

    # --- Label 0 --- #
    DefineLabel(0)
    
    MAIN.Await(ObjectBackreadEnabled(obj=4501670))

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(4501670, 2, loop=True, unknown2=1.0)
    RegisterLadder(start_climbing_flag=14505672, stop_climbing_flag=14505673, obj=4501670)


@RestartOnRest(14505680)
def Event_14505680():
    """Event 14505680"""
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4502120))
    GotoIfConditionTrue(Label.L0, input_condition=AND_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetAreaWelcomeMessageState(state=False)


@RestartOnRest(14505699)
def Event_14505699():
    """Event 14505699"""
    if ThisEventSlotFlagEnabled():
        return
    RestoreObject(4501530)
    RestoreObject(4501531)
    RestoreObject(4501532)
    RestoreObject(4501260)


@ContinueOnRest(14500800)
def Event_14500800():
    """Event 14500800"""
    if FlagEnabled(14500800):
        return
    
    MAIN.Await(HealthRatio(4500800) <= 0.0)
    
    if CharacterHasSpecialEffect(character=4500800, special_effect=13146):
        Wait(2.0)
    Wait(1.5)
    PlaySoundEffect(4500800, 777777777, sound_type=SoundType.s_SFX)
    Wait(1.0)
    EnableFlag(14505803)
    Wait(2.7200000286102295)
    DisableCharacter(4500800)
    DisableAnimations(4500800)
    HandleBossDefeatAndDisplayBanner(boss=4500800, banner=BannerType.HeirOfFireDestroyed)
    EnableFlag(14500800)
    EnableFlag(9322)
    EnableFlag(6322)
    EnableSoundEvent(sound_id=4504804)


@RestartOnRest(14505810)
def Event_14505810():
    """Event 14505810"""
    GotoIfFlagDisabled(Label.L0, flag=14500800)
    DisableCharacter(4505800)
    DisableAnimations(4505800)
    Kill(4505800)
    CreateVFX(4503800)
    CreateVFX(4503810)
    CreateVFX(4503811)
    CreateVFX(4503812)
    CreateVFX(4503813)
    CreateVFX(4503814)
    CreateVFX(4503815)
    CreateVFX(4503816)
    CreateVFX(4503817)
    CreateVFX(4503818)
    CreateVFX(4503819)
    CreateVFX(4503820)
    DisableObject(4506800)
    DisableObject(4501810)
    DisableObject(4501820)
    DisableObject(4501821)
    DisableObject(4501822)
    EnableObject(4501823)
    EnableSoundEvent(sound_id=4504804)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(4500800)
    DisableAnimations(4500800)
    DisableAI(4500800)
    DisableAI(4500801)
    SetLockOnPoint(character=4500803, lock_on_dummy_id=220, state=False)
    EnableImmortality(4500803)
    EnableInvincibility(4500803)
    DisableHealthBar(4500803)
    ForceAnimation(4500803, 30000, loop=True, unknown2=1.0)
    DisableCharacter(4500802)
    DisableAnimations(4500802)
    DisableAI(4500802)
    DisableObject(4506801)
    DisableObject(4501821)
    DisableObject(4501822)
    DisableObject(4501823)
    MoveRemains(source_region=4502826, destination_region=4502827)
    MoveRemains(source_region=4502828, destination_region=4502829)
    OR_15.Add(CharacterIsType(PLAYER, character_type=CharacterType.BlackPhantom))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=7))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=21))
    OR_15.Add(CharacterInvadeType(character=PLAYER, invade_type=4))
    if OR_15:
        return
    GotoIfFlagEnabled(Label.L1, flag=14500801)
    DisableCharacter(4500801)
    DisableAnimations(4500801)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(74500300))
    AND_1.Add(ActionButtonParamActivated(action_button_id=9373, entity=4500803))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    EnableFlag(14505521)
    WaitFrames(frames=1)
    DeleteVFX(4503825, erase_root_only=False)
    DeleteVFX(4503826, erase_root_only=False)
    DeleteVFX(4503827, erase_root_only=False)
    DeleteVFX(4503828, erase_root_only=False)
    DeleteVFX(4503829, erase_root_only=False)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        45000000,
        cutscene_flags=0,
        player_id=10000,
        move_to_region=4502810,
        game_map=PAINTED_WORLD_OF_ARIANDEL,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        45000000,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=4502810,
        game_map=PAINTED_WORLD_OF_ARIANDEL,
    )
    SkipLines(1)
    PlayCutscene(45000000, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(14505521)
    CreateVFX(4503825)
    CreateVFX(4503826)
    CreateVFX(4503827)
    CreateVFX(4503828)
    CreateVFX(4503829)
    EnableCharacter(4500801)
    EnableAnimations(4500801)
    Move(4500801, destination=4502811, destination_type=CoordEntityType.Region, copy_draw_parent=4500801)
    SetCharacterEventTarget(4500801, entity=PLAYER)
    ForceAnimation(4500803, 30002, loop=True, unknown2=1.0)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    ForceAnimation(4500803, 30002, loop=True, unknown2=1.0)
    AND_1.Add(FlagEnabled(14505805))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4502800))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableAI(4500801)
    SetNetworkUpdateRate(4500801, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(4500803, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(4500801, name=906020)
    SetNetworkConnectedFlagState(flag=14500801, state=FlagSetting.On)


@RestartOnRest(14505811)
def Event_14505811():
    """Event 14505811"""
    if FlagEnabled(14500800):
        return
    AND_1.Add(FlagEnabled(14505805))
    AND_1.Add(CharacterDead(4500801))
    
    MAIN.Await(AND_1)
    
    DeleteVFX(4503825, erase_root_only=False)
    DeleteVFX(4503826, erase_root_only=False)
    DeleteVFX(4503827, erase_root_only=False)
    DeleteVFX(4503828, erase_root_only=False)
    DeleteVFX(4503829, erase_root_only=False)
    EnableFlag(14505521)
    WaitFrames(frames=1)
    SkipLinesIfTryingToCreateSession(2)
    PlayCutscene(
        45000010,
        cutscene_flags=0,
        player_id=10000,
        move_to_region=4502812,
        game_map=PAINTED_WORLD_OF_ARIANDEL,
    )
    SkipLines(4)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    PlayCutscene(
        45000010,
        cutscene_flags=CutsceneFlags.Unskippable | CutsceneFlags.FadeOut,
        player_id=10000,
        move_to_region=4502812,
        game_map=PAINTED_WORLD_OF_ARIANDEL,
    )
    SkipLines(1)
    PlayCutscene(45000010, cutscene_flags=CutsceneFlags.Unskippable, player_id=10000)
    WaitFrames(frames=1)
    DisableFlag(14505521)
    CreateVFX(4503825)
    CreateVFX(4503826)
    CreateVFX(4503827)
    CreateVFX(4503828)
    CreateVFX(4503829)
    DisableCharacter(4500801)
    DisableAnimations(4500801)
    EnableCharacter(4500800)
    EnableAnimations(4500800)
    EnableAI(4500800)
    SetNetworkUpdateRate(4500800, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    DisableHealthBar(4500800)
    DisableCharacter(4500803)
    DisableAnimations(4500803)
    EnableCharacter(4500802)
    EnableAnimations(4500802)
    EnableAI(4500802)
    SetNetworkUpdateRate(4500802, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableBossHealthBar(4500802, name=906021)
    DisableObject(4501810)
    DisableObject(4501811)
    DisableObject(4506800)
    EnableObject(4506801)
    PostDestruction(4506810)
    DisableObject(4501820)
    EnableObject(4501823)
    CreateVFX(4503800)
    CreateVFX(4503810)
    CreateVFX(4503811)
    CreateVFX(4503812)
    CreateVFX(4503813)
    CreateVFX(4503814)
    CreateVFX(4503815)
    CreateVFX(4503816)
    CreateVFX(4503817)
    CreateVFX(4503818)
    CreateVFX(4503819)
    CreateVFX(4503820)
    SetCharacterEventTarget(4500800, entity=4500802)
    ReferDamageToEntity(4500800, target_entity=4500802)
    SetNetworkConnectedFlagState(flag=14505802, state=FlagSetting.On)


@RestartOnRest(14505812)
def Event_14505812():
    """Event 14505812"""
    if FlagEnabled(14500800):
        return
    
    MAIN.Await(HealthValue(4500802) <= 0)
    
    AddSpecialEffect(4500800, 13133)
    WaitFrames(frames=1)
    if CharacterDoesNotHaveSpecialEffect(character=4500800, special_effect=13134):
        ForceAnimation(4500800, 20003, unknown2=1.0)
    WaitFrames(frames=2)
    PlaySoundEffect(4500800, 777777777, sound_type=SoundType.s_SFX)
    
    MAIN.Await(CharacterDead(4500802))
    
    DisableBossMusic(sound_id=-1)
    DisableBossHealthBar(4500802, name=906021)
    if PlayerNotInOwnWorld():
        return
    Wait(2.5)
    AwardItemLot(4700, host_only=False)
    Wait(6.5)
    SetNetworkConnectedFlagState(flag=74500332, state=FlagSetting.On)


@RestartOnRest(14505813)
def Event_14505813():
    """Event 14505813"""
    if FlagEnabled(14500800):
        return
    AND_1.Add(FlagEnabled(74500332))
    
    MAIN.Await(AND_1)
    
    Wait(1.100000023841858)
    WaitFrames(frames=1)
    if CharacterDoesNotHaveSpecialEffect(character=4500800, special_effect=13136):
        ForceAnimation(4500800, 20001, unknown2=1.0)
    else:
        ForceAnimation(4500800, 20002, unknown2=1.0)
        WaitFrames(frames=1)
    OR_1.Add(CharacterHasTAEEvent(4500800, tae_event_id=10))
    OR_1.Add(TimeElapsed(seconds=6.0))
    
    MAIN.Await(OR_1)
    
    EnableBossHealthBar(4500800, name=906022)
    OR_2.Add(CharacterHasTAEEvent(4500800, tae_event_id=20))
    OR_2.Add(TimeElapsed(seconds=4.199999809265137))
    
    MAIN.Await(OR_2)
    
    EnableBossMusic(sound_id=4504802)
    RemoveSpecialEffect(4500800, 13132)
    End()


@RestartOnRest(14505820)
def Event_14505820():
    """Event 14505820"""
    DisableNetworkSync()
    if FlagEnabled(14500800):
        return
    AND_9.Add(CharacterDead(4500802))
    GotoIfConditionTrue(Label.L9, input_condition=AND_9)
    
    MAIN.Await(FlagEnabled(14505802))
    
    AND_1.Add(EntityBeyondDistance(entity=PLAYER, other_entity=4500802, radius=16.0))
    GotoIfConditionTrue(Label.L1, input_condition=AND_1)
    AND_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=4500802, radius=16.0))
    AND_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=4500802, radius=9.0))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=4500802, radius=9.0))
    GotoIfConditionTrue(Label.L3, input_condition=AND_3)

    # --- Label 1 --- #
    DefineLabel(1)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(0.5)
    OR_1.Add(EntityWithinDistance(entity=PLAYER, other_entity=4500802, radius=16.0))
    OR_1.Add(FlagEnabled(14500800))
    
    MAIN.Await(OR_1)
    
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    ChangeCamera(normal_camera_id=6011, locked_camera_id=6011)
    Wait(0.5)
    OR_2.Add(EntityBeyondDistance(entity=PLAYER, other_entity=4500802, radius=16.0))
    OR_2.Add(EntityWithinDistance(entity=PLAYER, other_entity=4500802, radius=9.0))
    OR_2.Add(FlagEnabled(14500800))
    
    MAIN.Await(OR_2)
    
    Goto(Label.L0)

    # --- Label 3 --- #
    DefineLabel(3)
    ChangeCamera(normal_camera_id=6010, locked_camera_id=6010)
    Wait(0.5)
    OR_3.Add(EntityBeyondDistance(entity=PLAYER, other_entity=4500802, radius=9.0))
    OR_3.Add(FlagEnabled(14500800))
    
    MAIN.Await(OR_3)
    
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L9, flag=14500800)
    Restart()

    # --- Label 9 --- #
    DefineLabel(9)
    ChangeCamera(normal_camera_id=-1, locked_camera_id=-1)
    Wait(0.5)
    End()


@RestartOnRest(14505825)
def Event_14505825():
    """Event 14505825"""
    DisableNetworkSync()
    if FlagEnabled(14500800):
        return
    if FlagEnabled(14505805):
        return
    DisableCharacterCollision(4500803)
    DisableGravity(4500803)
    AND_1.Add(CharacterBackreadEnabled(4500803))
    AND_1.Add(ObjectBackreadEnabled(obj=4501810))
    AND_1.Add(ObjectBackreadEnabled(obj=4501811))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4502824))
    
    MAIN.Await(AND_1)
    
    if FlagEnabled(14505805):
        return
    WaitFrames(frames=1)
    Move(4500803, destination=4502825, destination_type=CoordEntityType.Region, short_move=True)
    OR_1.Add(FlagEnabled(14505805))
    OR_1.Add(CharacterBackreadDisabled(4500803))
    
    MAIN.Await(OR_1)
    
    if FlagEnabled(14505805):
        return
    Restart()


@RestartOnRest(14505829)
def Event_14505829():
    """Event 14505829"""
    CommonFunc_20005800(
        0,
        flag=14500800,
        entity=4501800,
        region=4502800,
        flag_1=14505805,
        action_button_id=4501800,
        character=4505800,
        left=14500801,
        region_1=0,
    )
    CommonFunc_20005801(
        0,
        flag=14500800,
        entity=4501800,
        region=4502800,
        flag_1=14505805,
        action_button_id=4501800,
        flag_2=14505806,
    )
    if FlagDisabled(14500801):
        CommonFunc_20001837(
            0,
            flag=14500800,
            flag_1=14505805,
            flag_2=14505806,
            flag_3=14505810,
            sound_id=4504801,
            sound_id_1=4504802,
            flag_4=14505802,
            flag_5=14505803,
        )
    else:
        CommonFunc_20005832(
            0,
            flag=14500800,
            flag_1=14505805,
            flag_2=14505806,
            region=4502800,
            sound_id=4504801,
            sound_id_1=4504802,
            flag_3=14505802,
            flag_4=14505803,
        )
    CommonFunc_20005825(0, flag=14500800, obj=4501800, dummy_id=3, left=14500801, vfx_id=110)
    CommonFunc_20005820(0, flag=14500800, obj=4501801, dummy_id=0, left=14500801)
    CommonFunc_20005810(0, flag=14500800, entity=4501800, target_entity=4502800, action_button_id=10000)


@RestartOnRest(14505830)
def Event_14505830():
    """Event 14505830"""
    AddSpecialEffect(4500171, 12700)
    DisableAI(4500171)
    DisableAnimations(4500171)
    DisableCharacter(4500171)
    if FlagEnabled(14505841):
        return
    DisableAnimations(4500170)
    DisableCharacter(4500170)


@RestartOnRest(14505831)
def Event_14505831():
    """Event 14505831"""
    DisableNetworkSync()
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(14500800):
        return
    Wait(0.5)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagDisabled(1638))
    AND_1.Add(FlagDisabled(1637))
    AND_1.Add(FlagDisabled(1636))
    AND_1.Add(FlagDisabled(14505840))
    AND_1.Add(FlagDisabled(14505841))
    AND_1.Add(FlagEnabled(14500620))
    AND_1.Add(CharacterBackreadEnabled(4500171))
    
    MAIN.Await(AND_1)
    
    EnableCharacter(4500171)
    Wait(1.5)
    Move(4500171, destination=4502830, destination_type=CoordEntityType.Region, copy_draw_parent=4500171)
    CreateObjectVFX(4501170, vfx_id=0, dummy_id=30001)
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(ActionButtonParamActivated(action_button_id=9334, entity=4501170))
    OR_1.Add(AND_2)
    OR_1.Add(FlagEnabled(14500800))
    
    MAIN.Await(OR_1)
    
    GotoIfFlagDisabled(Label.L0, flag=14500800)
    DeleteObjectVFX(4501170)
    DisableCharacter(4500171)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AwaitDialogResponse(
        message=10012500,
        button_type=ButtonType.Yes_or_No,
        number_buttons=NumberButtons.TwoButton,
        anchor_entity=4501170,
        display_distance=3.0,
        left_flag=14505848,
        right_flag=14505849,
        cancel_flag=14505849,
    )
    if FlagDisabled(14505848):
        return RESTART
    DisplayBattlefieldMessage(10012520, display_location_index=1)
    Wait(5.0)
    DeleteObjectVFX(4501170)
    DisableCharacter(4500171)
    SetNetworkConnectedFlagState(flag=14505840, state=FlagSetting.On)


@RestartOnRest(14505832)
def Event_14505832():
    """Event 14505832"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(14505840))
    AND_1.Add(FlagDisabled(14505841))
    AND_1.Add(FlagEnabled(14505802))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012600, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012610, display_location_index=1)
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=30300, anchor_entity=4500170, dummy_id=236, anchor_type=CoordEntityType.Character)
    EnableCharacter(4500170)
    EnableAnimations(4500170)
    SetBackreadStateAlternate(4500170, True)
    ForceAnimation(4500170, 63010, unknown2=1.0)
    SetCharacterEventTarget(4500170, entity=4500800)
    SetNetworkConnectedFlagState(flag=14505841, state=FlagSetting.On)
    AddSpecialEffect(4500800, 13123)
    AddSpecialEffect(4500802, 13124)


@RestartOnRest(14505833)
def Event_14505833():
    """Event 14505833"""
    if ThisEventSlotFlagEnabled():
        return
    AND_1.Add(FlagEnabled(14505841))
    AND_1.Add(CharacterDead(4500170))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisplayBattlefieldMessage(10012602, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012612, display_location_index=1)
    SetBackreadStateAlternate(4500170, False)
    SetNetworkConnectedFlagState(flag=14505841, state=FlagSetting.Off)


@RestartOnRest(14505834)
def Event_14505834():
    """Event 14505834"""
    if FlagEnabled(14500800):
        return
    AND_1.Add(FlagEnabled(14505841))
    AND_1.Add(FlagEnabled(14500800))
    
    MAIN.Await(AND_1)
    
    Wait(3.0)
    AddSpecialEffect(4500170, 13270)
    Wait(1.0)
    DisableCharacter(4500170)
    DisableAnimations(4500170)
    SetBackreadStateAlternate(4500170, False)
    SetNetworkConnectedFlagState(flag=14505841, state=FlagSetting.Off)


@RestartOnRest(14500860)
def Event_14500860():
    """Event 14500860"""
    if FlagEnabled(14500860):
        return
    AND_1.Add(HealthRatio(4500860) <= 0.0)
    AND_1.Add(HealthRatio(4500861) <= 0.0)
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    PlaySoundEffect(4500800, 777777777, sound_type=SoundType.s_SFX)
    AND_2.Add(CharacterDead(4500860))
    AND_2.Add(CharacterDead(4500861))
    
    MAIN.Await(AND_2)
    
    KillBoss(game_area_param_id=4500860)
    EnableFlag(14500860)
    EnableFlag(9323)
    EnableFlag(6323)
    EnableFlag(14500861)


@RestartOnRest(14505870)
def Event_14505870():
    """Event 14505870"""
    GotoIfFlagDisabled(Label.L0, flag=14500860)
    Kill(4500860)
    DisableCharacter(4500860)
    DisableAnimations(4500860)
    Kill(4505860)
    DisableCharacter(4505860)
    DisableAnimations(4505860)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableAI(4500860)
    ForceAnimation(4500860, 91080, unknown2=1.0)
    AND_9.Add(EntityWithinDistance(entity=PLAYER, other_entity=4500860, radius=30.0))
    AND_9.Add(CharacterInsideRegion(character=PLAYER, region=4502860))
    OR_1.Add(AND_9)
    OR_1.Add(AttackedWithDamageType(attacked_entity=4500860))
    OR_1.Add(HasAIStatus(4505860, ai_status=AIStatusType.Battle, target_comparison_type=ComparisonType.GreaterThanOrEqual))
    
    MAIN.Await(OR_1)
    
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_1.Add(FlagEnabled(14505865))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4502860))
    
    MAIN.Await(AND_1)
    
    Goto(Label.L2)

    # --- Label 2 --- #
    DefineLabel(2)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    BanishInvaders(unknown=0)
    EnableAI(4500860)
    ForceAnimation(4500860, 91090, wait_for_completion=True, unknown2=1.0)
    SetNetworkUpdateRate(4505860, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    SetNetworkUpdateRate(4500860, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    ActivateMultiplayerBuffs(4500860)
    SetDecoratedBossHealthBarState(state=True, character=4500860, slot=0, name=30000, decoration=3)
    FaceEntity(4500860, PLAYER)
    SetNetworkConnectedFlagState(flag=14505861, state=FlagSetting.On)
    if PlayerNotInOwnWorld():
        return
    SetNetworkUpdateAuthority(4500860, authority_level=UpdateAuthority.Forced)


@RestartOnRest(14505871)
def Event_14505871():
    """Event 14505871"""
    if FlagEnabled(14500860):
        return
    DisableAI(4500861)
    DisableGravity(4500861)
    DisableCharacter(4500861)
    OR_3.Add(FlagDisabled(14505206))
    OR_3.Add(FlagEnabled(14505209))
    OR_4.Add(FlagDisabled(14505216))
    OR_4.Add(FlagEnabled(14505219))
    AND_1.Add(OR_3)
    AND_1.Add(OR_4)
    AND_1.Add(HealthRatio(4500860) < 0.44999998807907104)
    
    MAIN.Await(AND_1)
    
    EnableFlag(14505896)
    EnableFlag(14505862)
    SetNetworkUpdateRate(4500861, is_fixed=True, update_rate=CharacterUpdateRate.Always)
    EnableCharacter(4500861)
    EnableGravity(4500861)
    EnableAI(4500861)
    DisableHealthBar(4500861)
    AND_2.Add(FlagEnabled(14500200))
    AND_2.Add(FlagEnabled(14500210))
    GotoIfConditionTrue(Label.L2, input_condition=AND_2)
    OR_2.Add(FlagEnabled(14500200))
    OR_2.Add(FlagEnabled(14500210))
    GotoIfConditionTrue(Label.L1, input_condition=OR_2)
    Goto(Label.L0)

    # --- Label 2 --- #
    DefineLabel(2)
    AddSpecialEffect(4500861, 13108)
    Goto(Label.L0)

    # --- Label 1 --- #
    DefineLabel(1)
    AddSpecialEffect(4500861, 13107)
    Goto(Label.L0)

    # --- Label 0 --- #
    DefineLabel(0)
    ForceAnimation(4500861, 20003, wait_for_completion=True, unknown2=1.0)
    ReplanAI(4500861)
    Wait(1.0)
    EnableBossHealthBar(4500861, name=906030, bar_slot=1)
    AddSpecialEffect(4500860, 13102)
    SetNetworkConnectedFlagState(flag=14505863, state=FlagSetting.On)


@RestartOnRest(14505872)
def Event_14505872():
    """Event 14505872"""
    if FlagEnabled(14500860):
        return
    
    MAIN.Await(HealthRatio(4500860) <= 0.0)
    
    AddSpecialEffect(4500861, 13103)


@RestartOnRest(14505873)
def Event_14505873():
    """Event 14505873"""
    if FlagEnabled(14500860):
        return
    
    MAIN.Await(HealthRatio(4500861) <= 0.0)
    
    RemoveSpecialEffect(4500860, 13102)


@RestartOnRest(14505874)
def Event_14505874():
    """Event 14505874"""
    if FlagEnabled(14500860):
        return
    
    MAIN.Await(CharacterHasSpecialEffect(4500861, 13105))
    
    AddSpecialEffect(4500860, 13106)


@RestartOnRest(14505880)
def Event_14505880():
    """Event 14505880"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(50006910):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterDead(4500860))
    
    MAIN.Await(AND_1)
    
    AwardItemLot(59100, host_only=False)


@RestartOnRest(14505889)
def Event_14505889():
    """Event 14505889"""
    CommonFunc_20005800(
        0,
        flag=14500860,
        entity=4501860,
        region=4502860,
        flag_1=14505865,
        action_button_id=4501860,
        character=4505860,
        left=14505861,
        region_1=0,
    )
    CommonFunc_20005801(
        0,
        flag=14500860,
        entity=4501860,
        region=4502860,
        flag_1=14505865,
        action_button_id=4501860,
        flag_2=14505866,
    )
    if FlagDisabled(14505861):
        CommonFunc_20001836(
            0,
            flag=14500860,
            flag_1=14505865,
            flag_2=14505866,
            flag_3=14505870,
            sound_id=4504861,
            sound_id_1=4504862,
            flag_4=14505863,
        )
    else:
        CommonFunc_20005831(
            0,
            flag=14500860,
            flag_1=14505865,
            flag_2=14505866,
            region=4502860,
            sound_id=4504861,
            sound_id_1=4504862,
            flag_3=14505863,
        )
    CommonFunc_20005820(0, flag=14500860, obj=4501860, dummy_id=5, left=14505861)
    CommonFunc_20005810(0, flag=14500860, entity=4501860, target_entity=4502860, action_button_id=10000)


@RestartOnRest(14505890)
def Event_14505890():
    """Event 14505890"""
    if FlagEnabled(14500890):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(14500800))
    AND_1.Add(FlagEnabled(14500860))
    
    MAIN.Await(AND_1)
    
    EnableFlag(14500890)


@ContinueOnRest(14505700)
def Event_14505700(_, character: int, character_1: int):
    """Event 14505700"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1655, 1659))
    DisableNetworkConnectedFlagRange(flag_range=(1655, 1659))
    SetNetworkConnectedFlagState(flag=1655, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1656))
    AND_1.Add(FlagEnabled(70001052))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1655, 1659))
    SetNetworkConnectedFlagState(flag=1655, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1640, 1654))
    DisableNetworkConnectedFlagRange(flag_range=(1640, 1654))
    SetNetworkConnectedFlagState(flag=1640, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1655)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001052)
    if FlagDisabled(1658):
        DisableFlag(74500120)
        DisableFlag(74500131)
        DisableFlag(74500132)
    if FlagEnabled(1640):
        DisableFlag(74500121)
        DisableFlag(74500122)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1640)
    GotoIfFlagEnabled(Label.L1, flag=1641)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterTalkRange(character=character_1, distance=100.0)
    EnableImmortality(character)
    DisableHealthBar(character)
    ForceAnimation(character, 91100, unknown2=1.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L18, flag=1658)
    SetCharacterTalkRange(character=character_1, distance=100.0)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    End()


@ContinueOnRest(14505701)
def Event_14505701(_, character: int):
    """Event 14505701"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(PlayerInOwnWorld())
    OR_1.Add(FlagEnabled(74500121))
    AND_2.Add(FlagDisabled(74500122))
    AND_2.Add(CharacterHasTAEEvent(character, tae_event_id=90))
    OR_1.Add(AND_2)
    AND_1.Add(OR_1)
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)


@ContinueOnRest(14500702)
def Event_14500702(_, character: int, character_1: int):
    """Event 14500702"""
    if FlagEnabled(1658):
        return
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableFlag(14500702)
    if ThisEventSlotFlagEnabled():
        return
    DisableCharacter(character_1)
    DisableBackread(character_1)
    AND_15.Add(CharacterInsideRegion(character=PLAYER, region=4502700))
    AND_15.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_15)
    
    EnableFlag(74500132)
    EnableFlag(14500702)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    GotoIfPlayerNotInOwnWorld(Label.L10)
    AddSpecialEffect(character_1, 5020)
    if FlagEnabled(1640):
        DisableNetworkConnectedFlagRange(flag_range=(1640, 1654))
        SetNetworkConnectedFlagState(flag=1641, state=FlagSetting.On)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    ForceAnimation(character_1, 63010, unknown2=1.0)
    ReplanAI(character_1)
    
    MAIN.Await(FlagEnabled(74500131))
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    RemoveSpecialEffect(character_1, 5020)


@ContinueOnRest(14505703)
def Event_14505703():
    """Event 14505703"""
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAllEnabled(flag_range=(50006520, 50006521))
    
    MAIN.Await(FlagEnabled(1658))
    
    AwardItemLot(55200, host_only=False)


@ContinueOnRest(14505710)
def Event_14505710(_, character: int, character_1: int, obj: int, obj_1: int):
    """Event 14505710"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1675, 1679))
    DisableNetworkConnectedFlagRange(flag_range=(1675, 1679))
    SetNetworkConnectedFlagState(flag=1675, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1676))
    AND_1.Add(FlagEnabled(70001053))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1675, 1679))
    SetNetworkConnectedFlagState(flag=1675, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1678))
    AND_2.Add(HealthRatio(character) != 0.0)
    AND_2.Add(HealthRatio(character_1) != 0.0)
    SkipLinesIfConditionFalse(3, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1675, 1679))
    SetNetworkConnectedFlagState(flag=1675, state=FlagSetting.On)
    EnableFlag(74500181)
    SkipLinesIfFlagRangeAnyEnabled(2, (1660, 1674))
    DisableNetworkConnectedFlagRange(flag_range=(1660, 1674))
    SetNetworkConnectedFlagState(flag=1660, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1675)
    AND_3.Add(FlagEnabled(1660))
    AND_3.Add(FlagEnabled(14500610))
    AND_3.Add(FlagEnabled(74500182))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1660, 1674))
    SetNetworkConnectedFlagState(flag=1661, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001053)
    DisableFlag(74500185)
    if FlagEnabled(74500155):
        EnableFlag(74500184)
    if FlagEnabled(74500155):
        DisableFlagRange((14505715, 14505719))
        EnableRandomFlagInRange(flag_range=(14505715, 14505719))
        Goto(Label.L10)
    if FlagEnabled(9322):
        DisableFlagRange((14505715, 14505719))
        EnableFlag(14505719)
        Goto(Label.L10)
    DisableFlagRange((14505715, 14505719))
    EnableRandomFlagInRange(flag_range=(14505715, 14505717))

    # --- Label 10 --- #
    DefineLabel(10)
    if FlagEnabled(14500715):
        ForceAnimation(character_1, 20, unknown2=1.0)
        Goto(Label.L20)
    if FlagEnabled(14500716):
        ForceAnimation(character_1, 30001, unknown2=1.0)
        Goto(Label.L20)
    if FlagEnabled(14500717):
        ForceAnimation(character_1, 30002, unknown2=1.0)
        Goto(Label.L20)
    SkipLinesIfFlagRangeAllDisabled(2, (14500718, 14500719))
    ForceAnimation(character_1, 30003, unknown2=1.0)
    Goto(Label.L20)
    if FlagEnabled(14505715):
        ForceAnimation(character_1, 20, unknown2=1.0)
        Goto(Label.L20)
    if FlagEnabled(14505716):
        ForceAnimation(character_1, 30001, unknown2=1.0)
        Goto(Label.L20)
    if FlagEnabled(14505717):
        ForceAnimation(character_1, 30002, unknown2=1.0)
        Goto(Label.L20)
    SkipLinesIfFlagRangeAllDisabled(1, (14505718, 14505719))
    ForceAnimation(character_1, 30003, unknown2=1.0)

    # --- Label 20 --- #
    DefineLabel(20)
    GotoIfFlagEnabled(Label.L0, flag=1660)
    GotoIfFlagEnabled(Label.L1, flag=1661)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L18, flag=1678)
    DisableGravity(character)
    DisableCharacterCollision(character)
    DisableHealthBar(character)
    EnableObjectInvulnerability(obj)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L18, flag=1678)
    DisableHealthBar(character_1)
    DisableGravity(character_1)
    DisableCharacterCollision(character_1)
    RestoreObject(obj_1)
    EnableObjectInvulnerability(obj_1)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    End()


@ContinueOnRest(14505711)
def Event_14505711():
    """Event 14505711"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(74500182):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=4502715))
    
    EnableFlag(74500182)


@ContinueOnRest(14505712)
def Event_14505712(_, character: int, character_1: int, obj: int, obj_1: int):
    """Event 14505712"""
    EndIfFlagRangeAnyEnabled(flag_range=(1661, 1674))
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(1675))
    AND_1.Add(FlagEnabled(1660))
    AND_1.Add(FlagEnabled(14500610))
    AND_1.Add(FlagEnabled(74500182))
    AND_1.Add(CharacterBackreadDisabled(character))
    
    MAIN.Await(AND_1)
    
    GotoIfPlayerNotInOwnWorld(Label.L10)
    DisableNetworkConnectedFlagRange(flag_range=(1660, 1674))
    SetNetworkConnectedFlagState(flag=1661, state=FlagSetting.On)

    # --- Label 10 --- #
    DefineLabel(10)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObjectInvulnerability(obj)
    DisableHealthBar(character_1)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    DisableGravity(character_1)
    DisableCharacterCollision(character_1)
    EnableObjectInvulnerability(obj_1)


@ContinueOnRest(14505713)
def Event_14505713(_, character: int):
    """Event 14505713"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(74500183):
        return
    AND_1.Add(FlagEnabled(1675))
    AND_1.Add(FlagEnabled(1661))
    AND_1.Add(FlagEnabled(74500153))
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4502716))
    
    MAIN.Await(AND_1)
    
    SetCharacterTalkRange(character=character, distance=100.0)
    AND_2.Add(FlagEnabled(1675))
    AND_2.Add(FlagEnabled(1661))
    AND_2.Add(FlagEnabled(74500153))
    AND_2.Add(CharacterInsideRegion(character=PLAYER, region=4502717))
    
    MAIN.Await(AND_2)
    
    EnableFlag(74500183)


@ContinueOnRest(14505714)
def Event_14505714(_, other_entity: int):
    """Event 14505714"""
    if PlayerNotInOwnWorld():
        return
    
    MAIN.Await(EntityWithinDistance(entity=PLAYER, other_entity=other_entity, radius=4.900000095367432))
    
    DisableFlagRange((74500185, 74500189))
    EnableRandomFlagInRange(flag_range=(74500185, 74500189))
    Wait(1.0)
    
    MAIN.Await(EntityBeyondDistance(entity=PLAYER, other_entity=other_entity, radius=5.0))
    
    if FlagEnabled(74500189):
        ForceAnimation(other_entity, 20001, wait_for_completion=True, unknown2=1.0)
    Restart()


@ContinueOnRest(14505720)
def Event_14505720(_, entity: int):
    """Event 14505720"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(9322):
        return
    AND_1.Add(FlagEnabled(9322))
    AND_1.Add(FlagDisabled(1678))
    
    MAIN.Await(AND_1)
    
    DisableFlagRange((14505715, 14505719))
    EnableFlag(14505719)
    ForceAnimation(entity, 30003, unknown2=1.0)


@ContinueOnRest(14505721)
def Event_14505721(_, obj: int, flag: int):
    """Event 14505721"""
    if FlagEnabled(1678):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(1678))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    DisableObjectInvulnerability(obj)


@ContinueOnRest(14505730)
def Event_14505730(_, character: int, obj: int, character_1: int):
    """Event 14505730"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1695, 1699))
    DisableNetworkConnectedFlagRange(flag_range=(1695, 1699))
    SetNetworkConnectedFlagState(flag=1695, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1696))
    AND_1.Add(FlagEnabled(70001054))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1695, 1699))
    SetNetworkConnectedFlagState(flag=1695, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1680, 1694))
    DisableNetworkConnectedFlagRange(flag_range=(1680, 1694))
    SetNetworkConnectedFlagState(flag=1680, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1695)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001054)
    DisableFlag(14500731)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1680)
    GotoIfFlagEnabled(Label.L1, flag=1681)
    DisableCharacter(character)
    DisableBackread(character)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    GotoIfFlagEnabled(Label.L18, flag=1698)
    DisableHealthBar(character)
    ForceAnimation(character, 709, unknown2=1.0)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    GotoIfFlagEnabled(Label.L18, flag=1698)
    DisableHealthBar(character_1)
    ForceAnimation(character_1, 710, unknown2=1.0)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character_1)
    DisableBackread(character_1)
    DropMandatoryTreasure(character_1)
    End()


@ContinueOnRest(14505731)
def Event_14505731(_, character: int, obj: int):
    """Event 14505731"""
    GotoIfFlagEnabled(Label.L0, flag=14500731)
    if FlagDisabled(1680):
        return
    GotoIfPlayerNotInOwnWorld(Label.L1)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasSpecialEffect(character, 5450))
    
    MAIN.Await(AND_1)
    
    AND_2.Add(PlayerInOwnWorld())
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    
    MAIN.Await(AND_2)

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(PlayerInOwnWorld())
    AND_3.Add(EntityWithinDistance(entity=PLAYER, other_entity=character, radius=30.0))
    AND_4.Add(PlayerInOwnWorld())
    AND_4.Add(EntityBeyondDistance(entity=PLAYER, other_entity=character, radius=30.0))
    OR_1.Add(AND_3)
    OR_1.Add(AND_4)
    
    MAIN.Await(OR_1)
    
    RestartIfLastConditionResultTrue(input_condition=AND_4)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectInvulnerability(obj)
    DestroyObject_NoSlot(obj=obj)
    EnableFlag(14500731)


@ContinueOnRest(14505732)
def Event_14505732(_, character: int, obj: int, character_1: int):
    """Event 14505732"""
    EndIfFlagRangeAnyEnabled(flag_range=(1681, 1694))
    if FlagEnabled(1698):
        return
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(FlagEnabled(9322))
    AND_1.Add(FlagEnabled(1680))
    AND_1.Add(FlagEnabled(1695))
    
    MAIN.Await(AND_1)
    
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableNetworkConnectedFlagRange(flag_range=(1680, 1694))
    SetNetworkConnectedFlagState(flag=1681, state=FlagSetting.On)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObjectInvulnerability(obj)
    EnableCharacter(character_1)
    EnableBackread(character_1)
    DisableHealthBar(character_1)
    ForceAnimation(character_1, 710, unknown2=1.0)


@ContinueOnRest(14505733)
def Event_14505733():
    """Event 14505733"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(14500733):
        return
    AND_1.Add(FlagEnabled(1698))
    AND_1.Add(FlagEnabled(9322))
    
    MAIN.Await(AND_1)
    
    SetNetworkConnectedFlagState(flag=14500733, state=FlagSetting.On)


@ContinueOnRest(14505740)
def Event_14505740(_, character: int, character_1: int, character_2: int, obj: int):
    """Event 14505740"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1715, 1719))
    DisableNetworkConnectedFlagRange(flag_range=(1715, 1719))
    SetNetworkConnectedFlagState(flag=1715, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1716))
    AND_1.Add(FlagEnabled(70001055))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1715, 1699))
    SetNetworkConnectedFlagState(flag=1715, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1700, 1714))
    DisableNetworkConnectedFlagRange(flag_range=(1700, 1714))
    SetNetworkConnectedFlagState(flag=1700, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1700))
    AND_2.Add(FlagEnabled(14500801))
    SkipLinesIfConditionFalse(4, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1700, 1714))
    SetNetworkConnectedFlagState(flag=1701, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1715, 1719))
    SetNetworkConnectedFlagState(flag=1718, state=FlagSetting.On)
    AND_3.Add(FlagEnabled(1700))
    AND_3.Add(FlagEnabled(9322))
    SkipLinesIfConditionFalse(2, AND_3)
    DisableNetworkConnectedFlagRange(flag_range=(1700, 1714))
    SetNetworkConnectedFlagState(flag=1702, state=FlagSetting.On)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001055)
    if FlagEnabled(74500251):
        EnableFlag(74500281)
    DisableFlag(14500743)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1700)
    GotoIfFlagEnabled(Label.L1, flag=1701)
    GotoIfFlagEnabled(Label.L2, flag=1702)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacterCollision(character)
    DisableGravity(character)
    ForceAnimation(character, 30000, loop=True, unknown2=1.0)
    EnableImmortality(character)
    DisableHealthBar(character)
    RestoreObject(obj)
    EnableObjectInvulnerability(obj)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetCharacterTalkRange(character=character_1, distance=100.0)
    SetCharacterTalkRange(character=character_2, distance=100.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetCharacterTalkRange(character=character_1, distance=100.0)
    SetCharacterTalkRange(character=character_2, distance=100.0)
    End()

    # --- Label 2 --- #
    DefineLabel(2)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@ContinueOnRest(14505741)
def Event_14505741(_, character: int, obj: int):
    """Event 14505741"""
    if FlagDisabled(1700):
        return
    AND_1.Add(FlagEnabled(14500801))
    AND_1.Add(PlayerInOwnWorld())
    
    MAIN.Await(AND_1)
    
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    DisableObjectInvulnerability(obj)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=4,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    DisableNetworkConnectedFlagRange(flag_range=(1700, 1714))
    SetNetworkConnectedFlagState(flag=1701, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1715, 1719))
    SetNetworkConnectedFlagState(flag=1718, state=FlagSetting.On)
    End()


@ContinueOnRest(14505742)
def Event_14505742():
    """Event 14505742"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(74500282):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=4502710))
    
    EnableFlag(74500282)


@ContinueOnRest(14500743)
def Event_14500743(_, character: int, obj: int):
    """Event 14500743"""
    GotoIfThisEventSlotFlagEnabled(Label.L0)
    AND_1.Add(PlayerInOwnWorld())
    AND_1.Add(CharacterHasTAEEvent(character, tae_event_id=90))
    
    MAIN.Await(AND_1)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableCharacter(character)
    DisableBackread(character)
    DisableObjectInvulnerability(obj)


@ContinueOnRest(14505750)
def Event_14505750(_, character: int, character_1: int):
    """Event 14505750"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1735, 1739))
    DisableNetworkConnectedFlagRange(flag_range=(1735, 1739))
    SetNetworkConnectedFlagState(flag=1735, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1736))
    AND_1.Add(FlagEnabled(70001056))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1735, 1739))
    SetNetworkConnectedFlagState(flag=1735, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1720, 1734))
    DisableNetworkConnectedFlagRange(flag_range=(1720, 1734))
    SetNetworkConnectedFlagState(flag=1720, state=FlagSetting.On)
    AND_2.Add(FlagEnabled(1720))
    AND_2.Add(FlagEnabled(9322))
    SkipLinesIfConditionFalse(4, AND_2)
    DisableNetworkConnectedFlagRange(flag_range=(1720, 1734))
    SetNetworkConnectedFlagState(flag=1721, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1735, 1739))
    SetNetworkConnectedFlagState(flag=1738, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1735)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001056)
    if FlagDisabled(14500801):
        DisableFlag(74500300)
    DisableFlag(74500301)
    DisableFlag(74500332)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1720)
    GotoIfFlagEnabled(Label.L1, flag=1721)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=2,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetCharacterTalkRange(character=character, distance=100.0)
    SetCharacterTalkRange(character=character_1, distance=100.0)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    End()


@ContinueOnRest(14505770)
def Event_14505770(_, character: int):
    """Event 14505770"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1795, 1799))
    DisableNetworkConnectedFlagRange(flag_range=(1795, 1799))
    SetNetworkConnectedFlagState(flag=1795, state=FlagSetting.On)
    AND_1.Add(FlagEnabled(1796))
    AND_1.Add(FlagEnabled(70001059))
    SkipLinesIfConditionFalse(2, AND_1)
    DisableNetworkConnectedFlagRange(flag_range=(1795, 1799))
    SetNetworkConnectedFlagState(flag=1795, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1780, 1794))
    DisableNetworkConnectedFlagRange(flag_range=(1780, 1794))
    SetNetworkConnectedFlagState(flag=1780, state=FlagSetting.On)
    GotoIfFlagDisabled(Label.L9, flag=1795)

    # --- Label 9 --- #
    DefineLabel(9)
    DisableFlag(70001059)
    DisableFlag(74500381)

    # --- Label 10 --- #
    DefineLabel(10)
    GotoIfFlagEnabled(Label.L0, flag=1780)
    DisableCharacter(character)
    DisableBackread(character)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L18, flag=1798)
    ForceAnimation(character, 703, unknown2=1.0)
    DisableHealthBar(character)
    SkipLinesIfClientTypeCountComparison(
        skip_lines=1,
        client_type=ClientType.Invader,
        comparison_type=ComparisonType.Equal,
        value=0,
    )
    SetCharacterTalkRange(character=character, distance=100.0)
    End()

    # --- Label 18 --- #
    DefineLabel(18)
    DisableCharacter(character)
    DisableBackread(character)
    DropMandatoryTreasure(character)
    End()


@ContinueOnRest(14505771)
def Event_14505771():
    """Event 14505771"""
    if PlayerNotInOwnWorld():
        return
    GotoIfFlagEnabled(Label.L0, flag=74500382)
    EnableFlag(74500382)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    GotoIfFlagEnabled(Label.L1, flag=74000013)
    Wait(4.5)
    Goto(Label.L2)

    # --- Label 1 --- #
    DefineLabel(1)
    Wait(5.5)

    # --- Label 2 --- #
    DefineLabel(2)
    EnableFlag(74500381)


@ContinueOnRest(14505780)
def Event_14505780():
    """Event 14505780"""
    GotoIfPlayerNotInOwnWorld(Label.L10)
    SkipLinesIfFlagRangeAnyEnabled(2, (1635, 1639))
    DisableNetworkConnectedFlagRange(flag_range=(1635, 1639))
    SetNetworkConnectedFlagState(flag=1635, state=FlagSetting.On)
    SkipLinesIfFlagRangeAnyEnabled(2, (1620, 1634))
    DisableNetworkConnectedFlagRange(flag_range=(1620, 1634))
    SetNetworkConnectedFlagState(flag=1620, state=FlagSetting.On)
    AND_5.Add(FlagRangeAnyEnabled(flag_range=(1621, 1622)))
    AND_5.Add(FlagEnabled(6952))
    AND_5.Add(FlagEnabled(148))
    SkipLinesIfConditionFalse(4, AND_5)
    DisableNetworkConnectedFlagRange(flag_range=(1620, 1634))
    SetNetworkConnectedFlagState(flag=1625, state=FlagSetting.On)
    DisableNetworkConnectedFlagRange(flag_range=(1635, 1639))
    SetNetworkConnectedFlagState(flag=1638, state=FlagSetting.On)

    # --- Label 10 --- #
    DefineLabel(10)


@RestartOnRest(14505900)
def Event_14505900():
    """Event 14505900"""
    AddSpecialEffect(4500483, 5000)
    AddSpecialEffect(4500484, 5000)
    AddSpecialEffect(4500485, 5000)


@RestartOnRest(14505910)
def Event_14505910():
    """Event 14505910"""
    AddSpecialEffect(4500212, 13027)
