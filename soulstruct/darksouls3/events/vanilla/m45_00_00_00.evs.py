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
from soulstruct.darksouls3.events.instructions import *


@NeverRestart(0)
def Constructor():
    """Event 0"""
    RunCommonEvent(20005500, args=(14500800, 14500000, 4500950, 4501950))
    RunCommonEvent(20005500, args=(14500860, 14500006, 4500956, 4501956))
    RegisterBonfire(bonfire_flag=14500001, obj=4501951, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500002, obj=4501952, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500003, obj=4501953, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500004, obj=4501954, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500005, obj=4501955, reaction_distance=5.0)
    RegisterBonfire(bonfire_flag=14500007, obj=4501957, reaction_distance=5.0)
    RunCommonEvent(20005270, args=(4500212, 700, 1700, 13034))
    RunCommonEvent(20005270, args=(4500240, 700, 1700, 13034))
    RunCommonEvent(20005270, args=(4500241, 701, 1701, 13034))
    RunCommonEvent(20005360, args=(4500212, 10000, 13034))
    RunCommonEvent(20005360, args=(4500240, 10000, 13034))
    RunCommonEvent(20005360, args=(4500241, 10000, 13034))
    Event_14505240(0, character=4500212, special_effect_id=5024)
    Event_14505240(1, character=4500240, special_effect_id=5024)
    Event_14505280()
    Event_14505281()
    RunCommonEvent(20005270, args=(4500242, 700, 1700, 13022))
    RunCommonEvent(20005270, args=(4500243, 700, 1700, 13022))
    RunCommonEvent(20005270, args=(4500244, 700, 1700, 13022))
    RunCommonEvent(20005270, args=(4500211, 701, 1701, 13022))
    Event_14505290(0, character=4500242, region=4502231, special_effect=13031)
    Event_14505290(1, character=4500243, region=4502231, special_effect=13031)
    Event_14505290(2, character=4500244, region=4502231, special_effect=13031)
    Event_14505290(3, character=4500211, region=4502231, special_effect=13031)
    Event_14505282(0, character=4500242, region=4502232)
    Event_14505282(1, character=4500243, region=4502232)
    Event_14505282(2, character=4500244, region=4502232)
    Event_14505282(3, character=4500211, region=4502232)
    RunCommonEvent(20005360, args=(4500242, 10000, 13022))
    RunCommonEvent(20005360, args=(4500243, 10000, 13022))
    RunCommonEvent(20005360, args=(4500244, 10000, 13022))
    RunCommonEvent(20005360, args=(4500211, 10000, 13022))
    RunCommonEvent(20005221, args=(4500210, 701, 1701, 30.0), arg_types="iiif")
    Event_14505270(0, 4500247, 700, 1700, 1.0, 4502236, 20000, 0.5, 4502235)
    Event_14505270(1, 4500248, 700, 1700, 0.5, 4502236, 20000, 0.0, 4502235)
    Event_14505270(2, 4500249, 700, 1700, 0.0, 4502236, 20000, 1.0, 4502235)
    RunCommonEvent(20005360, args=(4500247, 10000, 13022))
    RunCommonEvent(20005360, args=(4500248, 10000, 13022))
    RunCommonEvent(20005360, args=(4500249, 10000, 13022))
    RunCommonEvent(20005220, args=(4500214, 700, 1700))
    RunCommonEvent(20005220, args=(4500215, 700, 1700))
    RunCommonEvent(20005220, args=(4500216, 700, 1700))
    RunCommonEvent(20005220, args=(4500245, 701, 1701))
    RunCommonEvent(20005220, args=(4500246, 700, 1700))
    RunCommonEvent(20005219, args=(4500218, 701, 1701, 2.0, 4502285, 0.5), arg_types="iiifif")
    RunCommonEvent(20005219, args=(4500251, 700, 1700, 2.0, 4502285, 1.0), arg_types="iiifif")
    RunCommonEvent(20005219, args=(4500252, 700, 1700, 2.0, 4502285, 0.0), arg_types="iiifif")
    Event_14505260(0, 4500219, 30001, 20000, 0.5, 0.0, 3006)
    Event_14505260(1, 4500253, 30001, 20000, 1.2000000476837158, 15.0, 3006)
    Event_14505260(2, 4500254, 30001, 20000, 0.0, 21.5, 3009)
    Event_14505260(3, 4500255, 30001, 20000, 0.699999988079071, 20.899999618530273, 3009)
    Event_14505260(4, 4500256, 30001, 20000, 0.20000000298023224, 6.5, 3009)
    Event_14505260(5, 4500257, 30001, 20000, 1.2000000476837158, 5.900000095367432, 3009)
    RunCommonEvent(20006040, args=(4500219, 4502221, 5450))
    RunCommonEvent(20006040, args=(4500253, 4502222, 5450))
    RunCommonEvent(20006040, args=(4500254, 4502223, 5450))
    RunCommonEvent(20006040, args=(4500255, 4502224, 5450))
    RunCommonEvent(20006040, args=(4500256, 4502225, 5450))
    RunCommonEvent(20006040, args=(4500257, 4502226, 5450))
    RunCommonEvent(20005110, args=(4500594, 4502455))
    RunCommonEvent(20005110, args=(4500220, 4502455))
    RunCommonEvent(20005110, args=(4500259, 4502455))
    RunCommonEvent(20005213, args=(4500260, 700, 1700, 2.0, 4502460), arg_types="iiifi")
    RunCommonEvent(20005111, args=(4500258, 3001, 4502456))
    RunCommonEvent(20005220, args=(4500250, 701, 1701))
    RunCommonEvent(20005270, args=(4500261, 700, 1700, 13022))
    RunCommonEvent(20005270, args=(4500262, 701, 1701, 13022))
    RunCommonEvent(20005360, args=(4500261, 10000, 13022))
    RunCommonEvent(20005360, args=(4500262, 10000, 13022))
    Event_14505200()
    Event_14505201()
    Event_14505202()
    Event_14505203()
    Event_14505204()
    Event_14505210()
    Event_14505211()
    Event_14505213()
    RunCommonEvent(20005210, args=(4500307, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500317, 700, 1700, 4.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500318, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005223, args=(4500320, 700, 1700, 1.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500322, 700, 1700, 9.0), arg_types="iiif")
    RunCommonEvent(20005265, args=(4500329, 700, 1700, 4500567))
    RunCommonEvent(20005265, args=(4500330, 700, 1700, 4500567))
    RunCommonEvent(20005265, args=(4500331, 700, 1700, 4500567))
    RunCommonEvent(20005222, args=(4500334, 700, 1700, 6.0, 1.5), arg_types="iiiff")
    RunCommonEvent(20005265, args=(4500335, 700, 1700, 4500337))
    RunCommonEvent(20005265, args=(4500336, 700, 1700, 4500337))
    RunCommonEvent(20005217, args=(4500337, 700, 1700, 3.0, 4502300), arg_types="iiifi")
    RunCommonEvent(20005217, args=(4500338, 700, 1700, 3.0, 4502300), arg_types="iiifi")
    RunCommonEvent(20005217, args=(4500339, 700, 1700, 3.0, 4502300), arg_types="iiifi")
    RunCommonEvent(20005221, args=(4500340, 700, 1700, 18.0), arg_types="iiif")
    RunCommonEvent(20005265, args=(4500341, 700, 1700, 4500337))
    RunCommonEvent(20005210, args=(4500344, 700, 1700, 5.400000095367432), arg_types="iiif")
    RunCommonEvent(20005212, args=(4500347, 700, 1700, 6.0, 4502320), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500348, 700, 1700, 6.0, 4502320), arg_types="iiifi")
    Event_14505300(3, 4500350, 4500350, 8.0)
    RunCommonEvent(20005221, args=(4500350, 701, 1701, 6.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500351, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500352, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500353, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500354, 700, 1700, 16.0), arg_types="iiif")
    Event_14505400(1, 4500401, 30001, 20001, 4502401, 0.0)
    RunCommonEvent(20005119, args=(4500403, 4502423, 4502424, 0, 0, 0, 0, 0))
    RunCommonEvent(20005132, args=(4500404, 5.0, 4502405), arg_types="ifi")
    RunCommonEvent(20005110, args=(4500405, 4502405))
    Event_14505400(7, 4500407, 30001, 20001, 4502407, 0.0)
    Event_14505410()
    Event_14505411()
    Event_14505412()
    RunCommonEvent(20005210, args=(4500410, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500411, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500412, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500413, 704, 1704, 3.0), arg_types="iiif")
    RunCommonEvent(20005201, args=(4500414, 700, 1700, 4502440, 3.0), arg_types="iiiif")
    RunCommonEvent(20005210, args=(4500415, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005201, args=(4500416, 700, 1700, 4502440, 0.5), arg_types="iiiif")
    RunCommonEvent(20005201, args=(4500417, 700, 1700, 4502440, 0.20000000298023224), arg_types="iiiif")
    RunCommonEvent(20005201, args=(4500418, 700, 1700, 4502440, 0.5), arg_types="iiiif")
    RunCommonEvent(20005201, args=(4500419, 700, 1700, 4502440, 0.5), arg_types="iiiif")
    RunCommonEvent(20005201, args=(4500420, 701, 1701, 4502440, 0.10000000149011612), arg_types="iiiif")
    RunCommonEvent(20005201, args=(4500421, 701, 1701, 4502440, 1.5), arg_types="iiiif")
    RunCommonEvent(20005210, args=(4500422, 701, 1701, 4.0), arg_types="iiif")
    RunCommonEvent(20005201, args=(4500423, 701, 1701, 4502440, 2.0), arg_types="iiiif")
    RunCommonEvent(20005210, args=(4500424, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500425, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500426, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500427, 701, 1701, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500428, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500429, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500430, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005201, args=(4500431, 700, 1700, 4502440, 0.5), arg_types="iiiif")
    RunCommonEvent(20005201, args=(4500432, 700, 1700, 4502440, 1.0), arg_types="iiiif")
    RunCommonEvent(20005201, args=(4500433, 700, 1700, 4502440, 0.4000000059604645), arg_types="iiiif")
    RunCommonEvent(20005210, args=(4500434, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500435, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500436, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005211, args=(4500440, 701, 1701, 4.0, 1.0), arg_types="iiiff")
    RunCommonEvent(20005210, args=(4500441, 705, 1705, 2.0), arg_types="iiif")
    RunCommonEvent(20005202, args=(4500442, 704, 1704, 4502419))
    RunCommonEvent(20005133, args=(4500443, 3015, 1.0, 4502330), arg_types="iifi")
    RunCommonEvent(20005133, args=(4500444, 3016, 1.0, 4502444), arg_types="iifi")
    RunCommonEvent(20005220, args=(4500445, 705, 1705))
    RunCommonEvent(20005260, args=(4500446, 705, 1705, 4500457))
    RunCommonEvent(20005210, args=(4500447, 705, 1705, 2.0), arg_types="iiif")
    RunCommonEvent(20005119, args=(4500448, 4502446, 4502447, 0, 0, 0, 0, 0))
    RunCommonEvent(20005133, args=(4500449, 3015, 3.0, 4502426), arg_types="iifi")
    RunCommonEvent(20005133, args=(4500451, 3015, 3.0, 4502442), arg_types="iifi")
    RunCommonEvent(20005132, args=(4500452, 2.0, 4502445), arg_types="ifi")
    RunCommonEvent(20005133, args=(4500453, 3015, 3.0, 4502426), arg_types="iifi")
    RunCommonEvent(20005134, args=(4500454, 3010, 3.0, 4502441), arg_types="iifi")
    RunCommonEvent(20005210, args=(4500458, 701, 1701, 4.0), arg_types="iiif")
    RunCommonEvent(20005201, args=(4500461, 703, 1703, 4502449, 2.0), arg_types="iiiif")
    RunCommonEvent(20005132, args=(4500463, 2.0, 4502428), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500464, 2.0, 4502428), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500465, 2.0, 4502428), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500466, 2.0, 4502428), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500468, 2.0, 4502428), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500467, 2.0, 4502429), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500469, 2.0, 4502429), arg_types="ifi")
    RunCommonEvent(20005213, args=(4500474, 701, 1701, 2.0, 4502421), arg_types="iiifi")
    RunCommonEvent(20005210, args=(4500475, 702, 1702, 2.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500476, 701, 1701, 3.0), arg_types="iiif")
    RunCommonEvent(20005201, args=(4500482, 702, 1702, 4502403, 2.0), arg_types="iiiif")
    Event_14505470(0, 4500460, 708, 20000, 4502421, 0.5)
    Event_14505470(2, 4500477, 708, 20000, 4502421, 3.0)
    Event_14505470(3, 4500478, 708, 20000, 4502425, 0.0)
    Event_14505470(4, 4500450, 708, 20000, 4502448, 0.0)
    RunCommonEvent(20005265, args=(4500470, 703, 1703, 4500472))
    RunCommonEvent(20006040, args=(4500470, 4502413, 5450))
    RunCommonEvent(20005265, args=(4500471, 702, 1702, 4500472))
    RunCommonEvent(20005221, args=(4500472, 701, 1701, 6.0), arg_types="iiif")
    RunCommonEvent(20005132, args=(4500480, 2.0, 4502414), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500481, 2.0, 4502414), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500487, 2.0, 4502414), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500488, 2.0, 4502414), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500489, 2.0, 4502414), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500490, 2.0, 4502414), arg_types="ifi")
    RunCommonEvent(20005132, args=(4500491, 2.0, 4502414), arg_types="ifi")
    RunCommonEvent(20005221, args=(4500492, 707, 1707, 3.0), arg_types="iiif")
    RunCommonEvent(20005265, args=(4500493, 701, 1701, 4500492))
    RunCommonEvent(20005222, args=(4500494, 700, 1700, 7.0, 1.0), arg_types="iiiff")
    RunCommonEvent(20005221, args=(4500497, 701, 1701, 6.0), arg_types="iiif")
    Event_14505420(
        1,
        character=4500455,
        animation_id=705,
        animation_id_1=1705,
        character_1=4505483,
        region=4502431,
        character_2=4500403
    )
    Event_14505420(
        2,
        character=4500456,
        animation_id=705,
        animation_id_1=1705,
        character_1=4505483,
        region=4502434,
        character_2=4500403
    )
    Event_14505420(
        3,
        character=4500456,
        animation_id=705,
        animation_id_1=1705,
        character_1=4505483,
        region=4502435,
        character_2=4500403
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
    RunCommonEvent(20005221, args=(4500390, 700, 1700, 7.0), arg_types="iiif")
    RunCommonEvent(20005201, args=(4500391, 700, 1700, 4502350, 1.0), arg_types="iiiif")
    RunCommonEvent(20005290, args=(4500381, 700, 1700))
    RunCommonEvent(20005290, args=(4500382, 700, 1700))
    RunCommonEvent(20005290, args=(4500383, 700, 1700))
    RunCommonEvent(20005290, args=(4500384, 700, 1700))
    RunCommonEvent(20005290, args=(4500385, 700, 1700))
    RunCommonEvent(20005290, args=(4500386, 700, 1700))
    RunCommonEvent(20005290, args=(4500387, 700, 1700))
    RunCommonEvent(20005200, args=(4500670, 701, 1701, 4502490))
    RunCommonEvent(20005205, args=(4500671, 702, 1702, 4502490, 6.0), arg_types="iiiif")
    Event_14505490(1, character=4500672, animation_id=702, animation_id_1=1702)
    Event_14505495()
    RunCommonEvent(20005110, args=(4500503, 4502470))
    RunCommonEvent(20005110, args=(4500504, 4502470))
    RunCommonEvent(20005119, args=(4500506, 4502470, 4502471, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(4500507, 4502470, 4502471, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(4500508, 4502470, 4502471, 0, 0, 0, 0, 0))
    Event_14505383()
    RunCommonEvent(20005110, args=(4500509, 4502281))
    RunCommonEvent(20005110, args=(4500510, 4502281))
    RunCommonEvent(20005120, args=(4500511, 38.0), arg_types="if")
    RunCommonEvent(20005110, args=(4500512, 4502282))
    RunCommonEvent(20005110, args=(4500217, 4502282))
    RunCommonEvent(20005110, args=(4500513, 4502283))
    RunCommonEvent(20005110, args=(4500595, 4502282))
    RunCommonEvent(20005110, args=(4500516, 4502390))
    RunCommonEvent(20005110, args=(4500517, 4502392))
    RunCommonEvent(20005110, args=(4500518, 4502284))
    RunCommonEvent(20005110, args=(4500519, 4502284))
    Event_14505380()
    Event_14505381()
    Event_14505382()
    RunCommonEvent(20005119, args=(4500520, 4502450, 4502451, 4502452, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(4500525, 4502450, 4502451, 4502452, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(4500590, 4502450, 4502452, 0, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(4500591, 4502450, 4502451, 4502452, 0, 0, 0, 0))
    RunCommonEvent(20005119, args=(4500592, 4502450, 4502451, 4502452, 0, 0, 0, 0))
    RunCommonEvent(20005220, args=(4500529, 700, 1700))
    RunCommonEvent(20005220, args=(4500531, 700, 1700))
    RunCommonEvent(20005220, args=(4500535, 700, 1700))
    RunCommonEvent(20005220, args=(4500538, 700, 1700))
    RunCommonEvent(20005212, args=(4500539, 700, 1700, 6.0, 4502458), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500540, 703, 1703, 6.0, 4502458), arg_types="iiifi")
    RunCommonEvent(20005110, args=(4500543, 4502454))
    RunCommonEvent(20005222, args=(4500545, 700, 1700, 10.0, 2.0), arg_types="iiiff")
    RunCommonEvent(20005222, args=(4500546, 700, 1700, 10.0, 3.0), arg_types="iiiff")
    RunCommonEvent(20005221, args=(4500552, 703, 1703, 9.100000381469727), arg_types="iiif")
    RunCommonEvent(20005220, args=(4500556, 701, 1701))
    RunCommonEvent(20005134, args=(4500558, 3007, 3.0, 4502457), arg_types="iifi")
    RunCommonEvent(20005213, args=(4500559, 700, 1700, 3.0, 4502457), arg_types="iiifi")
    RunCommonEvent(20005361, args=(4500520, 4500521, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500520, 4500522, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500520, 4500523, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500520, 4500524, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500520, 4500525, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500520, 4500526, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500520, 4500527, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500520, 4500533, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500520, 4500538, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500543, 4500541, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500543, 4500542, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500543, 4500543, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500543, 4500544, 10000, 13083, 13080))
    RunCommonEvent(20005361, args=(4500543, 4500547, 10000, 13083, 13080))
    RunCommonEvent(20005218, args=(4500566, 700, 1700, 20.0, 4502261, 0.5), arg_types="iiifif")
    RunCommonEvent(20005218, args=(4500567, 700, 1700, 20.0, 4502261, 0.0), arg_types="iiifif")
    RunCommonEvent(20005218, args=(4500568, 700, 1700, 20.0, 4502261, 1.0), arg_types="iiifif")
    RunCommonEvent(20005218, args=(4500569, 700, 1700, 20.0, 4502261, 1.2000000476837158), arg_types="iiifif")
    RunCommonEvent(20005120, args=(4500573, 35.0), arg_types="if")
    RunCommonEvent(20005220, args=(4500574, 701, 1701))
    RunCommonEvent(20005213, args=(4500579, 700, 1700, 5.0, 4502260), arg_types="iiifi")
    Event_14505370(0, 4500576, 700, 1700, 5.0, 10.0)
    Event_14505360()
    RunCommonEvent(20005210, args=(4500581, 700, 1700, 30.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500585, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500586, 700, 1700, 2.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500600, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005210, args=(4500603, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005215, args=(4500605, 701, 1701, 6.0, 0.0), arg_types="iiiff")
    RunCommonEvent(20005215, args=(4500606, 701, 1701, 4.0, 1.0), arg_types="iiiff")
    RunCommonEvent(20005210, args=(4500607, 700, 1700, 8.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500608, 700, 1700, 4.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500609, 700, 1700, 5.0), arg_types="iiif")
    RunCommonEvent(20005223, args=(4500610, 700, 1700, 5.0), arg_types="iiif")
    RunCommonEvent(20005220, args=(4500611, 700, 1700))
    RunCommonEvent(20005220, args=(4500612, 700, 1700))
    RunCommonEvent(20005220, args=(4500613, 700, 1700))
    RunCommonEvent(20005220, args=(4500614, 700, 1700))
    RunCommonEvent(20005220, args=(4500615, 700, 1700))
    RunCommonEvent(20005221, args=(4500616, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005221, args=(4500617, 700, 1700, 3.0), arg_types="iiif")
    RunCommonEvent(20005120, args=(4500618, 1.0), arg_types="if")
    RunCommonEvent(20005220, args=(4500619, 700, 1700))
    RunCommonEvent(20005120, args=(4500620, 1.0), arg_types="if")
    RunCommonEvent(20005202, args=(4500621, 701, 1701, 4502370))
    RunCommonEvent(20005212, args=(4500622, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500623, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500624, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500625, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500626, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500627, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500628, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500629, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500630, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500631, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500632, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500633, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005205, args=(4500634, 701, 1701, 4502372, 1.5), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500635, 701, 1701, 4502372, 2.0), arg_types="iiiif")
    RunCommonEvent(20005212, args=(4500636, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005205, args=(4500637, 701, 1701, 4502372, 1.5), arg_types="iiiif")
    RunCommonEvent(20005212, args=(4500638, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500639, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500640, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005212, args=(4500641, 700, 1700, 6.0, 4502372), arg_types="iiifi")
    RunCommonEvent(20005205, args=(4500642, 701, 1701, 4502372, 6.5), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500643, 701, 1701, 4502372, 7.5), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500644, 701, 1701, 4502372, 2.5), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500645, 701, 1701, 4502372, 4.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500646, 701, 1701, 4502372, 5.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500647, 701, 1701, 4502372, 3.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500648, 701, 1701, 4502372, 3.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500649, 701, 1701, 4502372, 4.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500650, 701, 1701, 4502372, 3.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500651, 701, 1701, 4502372, 2.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500652, 701, 1701, 4502372, 4.0), arg_types="iiiif")
    RunCommonEvent(20005205, args=(4500653, 701, 1701, 4502372, 5.0), arg_types="iiiif")
    RunCommonEvent(20005341, args=(14500480, 4500680, 21509600))
    RunCommonEvent(20005341, args=(14500482, 4500682, 21509620))
    RunCommonEvent(20005341, args=(14500484, 4500684, 21509640))
    RunCommonEvent(20005341, args=(14500485, 4500685, 21509650))
    RunCommonEvent(20005341, args=(14500487, 4500687, 21509670))
    RunCommonEvent(20005341, args=(14500488, 4500688, 21509680))
    RunCommonEvent(20005341, args=(14500489, 4500689, 21509690))
    RunCommonEvent(20005110, args=(4500680, 4502295))
    RunCommonEvent(20005120, args=(4500682, 10.0), arg_types="if")
    RunCommonEvent(20005120, args=(4500683, 14.0), arg_types="if")
    RunCommonEvent(20005120, args=(4500685, 8.0), arg_types="if")
    Event_14500800()
    Event_14505810()
    Event_14505811()
    Event_14505812()
    Event_14505813()
    Event_14505820()
    Event_14505825()
    Event_14505829()
    RunCommonEvent(20005840, args=(4501800,))
    RunCommonEvent(20005841, args=(4501800,))
    RunCommonEvent(20005840, args=(4501801,))
    RunCommonEvent(20005841, args=(4501801,))
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
    RunCommonEvent(20005223, args=(4500263, 701, 1701, 3.0), arg_types="iiif")
    RunCommonEvent(20005223, args=(4500264, 701, 1701, 3.0), arg_types="iiif")
    RunCommonEvent(20005223, args=(4500265, 700, 1700, 3.0), arg_types="iiif")
    Event_14505298()
    RunCommonEvent(20005840, args=(4501860,))
    RunCommonEvent(20005841, args=(4501860,))
    Event_14505890()
    RunCommonEvent(20005620, args=(14500510, 14501510, 4501510, 4501511, 4501512, 14501511))
    RunCommonEvent(20005628, args=(14500511, 4501512, 4502511))
    Event_14505510()
    Event_14505500()
    Event_14505501()
    Event_14505520()
    Event_14505525()
    Event_14505580()
    Event_14505530(0, 4501530, 4502530, 0.75, 4501260)
    Event_14505530(1, 4501531, 4502531, 0.25, 0)
    Event_14505530(2, 4501532, 4502532, 0.25, 0)
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
        obj_flag_4=0
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
        obj_flag_4=14504549
    )
    Event_14505544(0, flag=14500540, region=4502540)
    Event_14505544(1, flag=14500542, region=4502542)
    RunCommonEvent(20005610, args=(14500550, 4502550, 4502551))
    RunCommonEvent(20005611, args=(14500550, 4503550, 4501550, 450300))
    RunCommonEvent(20005610, args=(14500552, 4502552, 4502553))
    RunCommonEvent(20005611, args=(14500552, 4503552, 4501552, 450300))
    RunCommonEvent(20005610, args=(14500554, 4502554, 4502555))
    RunCommonEvent(20005611, args=(14500554, 4503554, 4501554, 450300))
    RunCommonEvent(20005610, args=(14500556, 4502556, 4502557))
    RunCommonEvent(20005611, args=(14500556, 4503556, 4501556, 450320))
    RunCommonEvent(20005614, args=(4501570, 64500570))
    Event_14505580()
    Event_14505600()
    Event_14505610()
    Event_14505611()
    Event_14505620()
    Event_14505630()
    RunCommonEvent(20005650, args=(14500640, 4501640))
    RunCommonEvent(20005650, args=(14500641, 4501641))
    RunCommonEvent(20005780, args=(4501690, 2))
    Event_14505670()
    Event_14505180()
    Event_14505181()
    Event_14505182()
    Event_14505183()
    RunCommonEvent(20006002, args=(4500701, 1658, 1655, 1659))
    Event_14505701(0, character=4500700)
    Event_14500702(0, character=4500700, character_1=4500701)
    Event_14505703()
    RunCommonEvent(20006002, args=(4500705, 1678, 1675, 1679))
    RunCommonEvent(20006002, args=(4500706, 1678, 1675, 1679))
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
    RunCommonEvent(20006030, args=(4501711, 4000, 2, 55500, 50006550, 50006550, 1718))
    RunCommonEvent(20006031, args=(74500331, 4502705))
    RunCommonEvent(20006002, args=(4500715, 1698, 1695, 1699))
    RunCommonEvent(20006002, args=(4500716, 1698, 1695, 1699))
    RunCommonEvent(20006040, args=(4500715, 4502720, 5450))
    Event_14505731(0, character=4500715, obj=4501715)
    Event_14505732(0, character=4500715, obj=4501715, character_1=4500716)
    Event_14505733()
    RunCommonEvent(20006030, args=(4501716, 4000, 2, 55400, 50006540, 50006540, 14500733))
    RunCommonEvent(20006002, args=(4500720, 1798, 1795, 1799))


@NeverRestart(50)
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
    
    CreateTemporaryVFX(vfx_id=1060, anchor_entity=4501101, model_point=200, anchor_type=CoordEntityType.Object)

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
    RotateToFaceEntity(PLAYER, 4501101, animation=91040)
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
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    SkipLinesIfConditionTrue(2, AND_1)
    DisplayBattlefieldMessage(10012700, display_location_index=1)
    SkipLines(1)
    DisplayBattlefieldMessage(10012700, display_location_index=1)
    WaitFrames(frames=1)
    CreateTemporaryVFX(vfx_id=30310, anchor_entity=4500176, model_point=236, anchor_type=CoordEntityType.Character)
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
    OR_2.Add(HealthRatioLessThanOrEqual(4500201, value=0.6000000238418579))
    AND_3.Add(CharacterOutsideRegion(character=4500201, region=4502205))
    AND_3.Add(CharacterOutsideRegion(character=4500201, region=4502206))
    OR_2.Add(AND_3)
    AND_4.Add(OR_2)
    AND_4.Add(FlagDisabled(14505207))
    AND_4.Add(FlagEnabled(14505206))
    OR_3.Add(AND_4)
    OR_3.Add(HasAIStatus(4500860, ai_status=AIStatusType.Battle))
    
    MAIN.Await(OR_3)
    
    AND_5.Add(HealthRatioLessThanOrEqual(4500201, value=0.6000000238418579))
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
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
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
    CancelSpecialEffect(4505240, 5022)
    CancelSpecialEffect(4505242, 5022)
    CancelSpecialEffect(4505240, 13024)
    CancelSpecialEffect(4505242, 13024)
    AddSpecialEffect(4505240, 13020)
    AddSpecialEffect(4505242, 13020)
    AddSpecialEffect(4505242, 13022)
    AddSpecialEffect(4505247, 13022)
    AddSpecialEffect(4505247, 13023)
    AddSpecialEffect(4505247, 13020)
    CancelSpecialEffect(4505247, 13024)
    CancelSpecialEffect(4505247, 5022)
    SetCharacterEventTarget(4500247, region=PLAYER)
    SetCharacterEventTarget(4500248, region=PLAYER)
    SetCharacterEventTarget(4500249, region=PLAYER)


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
    OR_2.Add(HealthRatioLessThanOrEqual(4500202, value=0.6000000238418579))
    OR_2.Add(HasAIStatus(4500860, ai_status=AIStatusType.Battle))
    OR_2.Add(CharacterOutsideRegion(character=4500202, region=4502215))
    OR_2.Add(CharacterInsideRegion(character=4500202, region=4502216))
    AND_3.Add(OR_2)
    AND_3.Add(FlagEnabled(14505216))
    
    MAIN.Await(AND_3)
    
    AND_4.Add(HealthRatioLessThanOrEqual(4500202, value=0.6000000238418579))
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
    CancelSpecialEffect(4505219, 5022)
    DisableFlag(14505216)
    End()


@RestartOnRest(14505240)
def Event_14505240(_, character: int, special_effect_id: int):
    """Event 14505240"""
    AddSpecialEffect(character, special_effect_id)


@RestartOnRest(14505245)
def Event_14505245(_, character: int, region: int):
    """Event 14505245"""
    MAIN.Await(HasAIStatus(character, ai_status=AIStatusType.Battle))
    
    SetCharacterEventTarget(character, region=region)
    AICommand(character, command_id=100, command_slot=0)
    ReplanAI(character)
    OR_1.Add(TimeElapsed(seconds=60.0))
    OR_1.Add(FlagEnabled(14505206))
    
    MAIN.Await(OR_1)
    
    AICommand(character, command_id=-1, command_slot=0)
    AddSpecialEffect(character, 5022)


@RestartOnRest(14505250)
def Event_14505250(_, character: int, character__region: int):
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
    
    GotoIfFinishedConditionTrue(Label.L0, input_condition=OR_1)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=OR_2)

    # --- Label 0 --- #
    DefineLabel(0)
    SetCharacterEventTarget(character, region=PLAYER)
    End()

    # --- Label 1 --- #
    DefineLabel(1)
    AND_3.Add(CharacterDead(character__region))
    SkipLinesIfConditionTrue(1, AND_3)
    SetCharacterEventTarget(character, region=character__region)
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
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
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
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_4)
    GotoIfFinishedConditionTrue(Label.L1, input_condition=AND_5)
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
    CancelSpecialEffect(4505242, 13031)
    SetCharacterEventTarget(4505242, region=PLAYER)


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
    CancelSpecialEffect(4500212, 13026)
    AddSpecialEffect(4500240, 5020)
    AddSpecialEffect(4500241, 5020)
    CancelSpecialEffect(4500212, 13024)
    CancelSpecialEffect(4500240, 13024)
    CancelSpecialEffect(4500241, 13024)
    Wait(3.799999952316284)
    GotoIfFlagEnabled(Label.L0, flag=14505280)
    AddSpecialEffect(4505242, 13022)
    AddSpecialEffect(4505242, 13031)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    CancelSpecialEffect(4505242, 13031)
    SetCharacterEventTarget(4505242, region=PLAYER)


@RestartOnRest(14505282)
def Event_14505282(_, character: int, region: int):
    """Event 14505282"""
    AND_1.Add(CharacterInsideRegion(character=character, region=region))
    AND_1.Add(CharacterHasSpecialEffect(character, 13031))
    
    MAIN.Await(AND_1)
    
    Wait(6.0)
    CancelSpecialEffect(character, 13022)
    CancelSpecialEffect(character, 13031)
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
    AND_1.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
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
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
    DisableAI(character)


@RestartOnRest(14505350)
def Event_14505350(_, character: int):
    """Event 14505350"""
    DisableAnimations(character)
    DisableAI(character)
    DisableHealthBar(character)
    SetLockOnPoint(character=character, lock_on_model_point=220, state=False)
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
    AND_9.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
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
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
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
    CancelSpecialEffect(PLAYER, 4680)
    AND_9.Add(CharacterDead(4500500))
    if AND_9:
        return
    OR_1.Add(CharacterInsideRegion(character=PLAYER, region=4502476))
    AND_1.Add(CharacterOutsideRegion(character=PLAYER, region=4502475))
    AND_1.Add(OR_1)
    AND_3.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
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
    AND_3.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
    AND_3.Add(CharacterHasSpecialEffect(PLAYER, 3710))
    OR_3.Add(AND_3)
    OR_3.Add(CharacterHuman(PLAYER))
    OR_3.Add(CharacterHollow(PLAYER))
    OR_3.Add(CharacterWhitePhantom(PLAYER))
    AND_1.Add(OR_3)
    AND_1.Add(CharacterInsideRegion(character=PLAYER, region=4502476))
    AND_1.Add(TimeElapsed(seconds=8.0))
    
    MAIN.Await(AND_1)
    
    SetCharacterEventTarget(4500500, region=PLAYER)
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
    OR_2.Add(HealthRatioLessThanOrEqual(character, value=0.9900000095367432))
    
    MAIN.Await(OR_2)
    
    AND_2.Add(CharacterDoesNotHaveSpecialEffect(character, 5450))
    GotoIfConditionTrue(Label.L0, input_condition=AND_2)
    SetAutogeneratedEventSpecificFlag_2(unknown1=2, unknown2=1)
    SkipLinesIfFinishedConditionFalse(1, input_condition=AND_1)
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
    SetCharacterEventTarget(4500403, region=4500483)
    ReplanAI(4500403)
    
    MAIN.Await(CharacterDead(4500483))
    
    SetCharacterEventTarget(4500403, region=4500484)
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
    CancelSpecialEffect(4500403, 13253)


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


@NeverRestart(14505501)
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


@NeverRestart(14505510)
def Event_14505510():
    """Event 14505510"""
    RunCommonEvent(
        20005621,
        args=(14500510, 14501510, 4501510, 4501511, 4504511, 4501512, 4504512, 4502511, 4502512, 14501511, 14504510, 0),
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
    CancelSpecialEffect(PLAYER, 4070)
    
    MAIN.Await(FlagEnabled(flag))
    
    GotoIfCharacterInsideRegion(Label.L0, character=PLAYER, region=region)
    End()

    # --- Label 0 --- #
    DefineLabel(0)
    AddSpecialEffect(PLAYER, 4070)
    Wait(8.0)
    CancelSpecialEffect(PLAYER, 4070)
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
    Move(PLAYER, destination=obj, destination_type=CoordEntityType.Object, model_point=100, short_move=True)
    ForceAnimation(PLAYER, 60440, unknown2=1.0)
    ForceAnimation(obj, 1, unknown2=1.0)
    Wait(1.5)
    CreateHazard(
        obj_flag=obj_flag,
        obj=obj,
        model_point=40,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=1.2999999523162842,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_1,
        obj=obj,
        model_point=41,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=1.2999999523162842,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_2,
        obj=obj,
        model_point=42,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=1.2999999523162842,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_3,
        obj=obj,
        model_point=43,
        behavior_param_id=6210,
        target_type=DamageTargetType.Character,
        radius=1.0,
        life=1.2999999523162842,
        repetition_time=0.0,
    )
    CreateHazard(
        obj_flag=obj_flag_4,
        obj=obj,
        model_point=44,
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
        model_point=41,
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


@NeverRestart(14500800)
def Event_14500800():
    """Event 14500800"""
    if FlagEnabled(14500800):
        return
    
    MAIN.Await(HealthRatioLessThanOrEqual(4500800, value=0.0))
    
    SkipLinesIfCharacterDoesNotHaveSpecialEffect(line_count=1, character=4500800, special_effect=13146)
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
    SetLockOnPoint(character=4500803, lock_on_model_point=220, state=False)
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
    OR_15.Add(CharacterType(PLAYER, character_type=CharacterType.BlackPhantom))
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
    SetCharacterEventTarget(4500801, region=PLAYER)
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
    SetCharacterEventTarget(4500800, region=4500802)
    ReferDamageToEntity(4500800, target_entity=4500802)
    SetNetworkConnectedFlagState(flag=14505802, state=FlagSetting.On)


@RestartOnRest(14505812)
def Event_14505812():
    """Event 14505812"""
    if FlagEnabled(14500800):
        return
    
    MAIN.Await(HealthValueLessThanOrEqual(4500802, value=0))
    
    AddSpecialEffect(4500800, 13133)
    WaitFrames(frames=1)
    SkipLinesIfCharacterHasSpecialEffect(line_count=1, character=4500800, special_effect=13134)
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
    SkipLinesIfCharacterHasSpecialEffect(line_count=2, character=4500800, special_effect=13136)
    ForceAnimation(4500800, 20001, unknown2=1.0)
    SkipLines(2)
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
    CancelSpecialEffect(4500800, 13132)
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
    RunCommonEvent(20005800, args=(14500800, 4501800, 4502800, 14505805, 4501800, 4505800, 14500801, 0))
    RunCommonEvent(20005801, args=(14500800, 4501800, 4502800, 14505805, 4501800, 14505806))
    if FlagDisabled(14500801):
        RunCommonEvent(20001837, args=(14500800, 14505805, 14505806, 14505810, 4504801, 4504802, 14505802, 14505803))
    else:
        RunCommonEvent(20005832, args=(14500800, 14505805, 14505806, 4502800, 4504801, 4504802, 14505802, 14505803))
    RunCommonEvent(20005825, args=(14500800, 4501800, 3, 14500801, 110))
    RunCommonEvent(20005820, args=(14500800, 4501801, 0, 14500801))
    RunCommonEvent(20005810, args=(14500800, 4501800, 4502800, 10000))


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
    CreateObjectVFX(4501170, vfx_id=0, model_point=30001)
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
    DisplayDialogAndSetFlags(
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
    CreateTemporaryVFX(vfx_id=30300, anchor_entity=4500170, model_point=236, anchor_type=CoordEntityType.Character)
    EnableCharacter(4500170)
    EnableAnimations(4500170)
    SetBackreadStateAlternate(4500170, True)
    ForceAnimation(4500170, 63010, unknown2=1.0)
    SetCharacterEventTarget(4500170, region=4500800)
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
    AND_1.Add(HealthRatioLessThanOrEqual(4500860, value=0.0))
    AND_1.Add(HealthRatioLessThanOrEqual(4500861, value=0.0))
    
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
    RotateToFaceEntity(4500860, PLAYER)
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
    AND_1.Add(HealthRatioLessThan(4500860, value=0.44999998807907104))
    
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
    
    MAIN.Await(HealthRatioLessThanOrEqual(4500860, value=0.0))
    
    AddSpecialEffect(4500861, 13103)


@RestartOnRest(14505873)
def Event_14505873():
    """Event 14505873"""
    if FlagEnabled(14500860):
        return
    
    MAIN.Await(HealthRatioLessThanOrEqual(4500861, value=0.0))
    
    CancelSpecialEffect(4500860, 13102)


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
    RunCommonEvent(20005800, args=(14500860, 4501860, 4502860, 14505865, 4501860, 4505860, 14505861, 0))
    RunCommonEvent(20005801, args=(14500860, 4501860, 4502860, 14505865, 4501860, 14505866))
    if FlagDisabled(14505861):
        RunCommonEvent(20001836, args=(14500860, 14505865, 14505866, 14505870, 4504861, 4504862, 14505863))
    else:
        RunCommonEvent(20005831, args=(14500860, 14505865, 14505866, 4502860, 4504861, 4504862, 14505863))
    RunCommonEvent(20005820, args=(14500860, 4501860, 5, 14505861))
    RunCommonEvent(20005810, args=(14500860, 4501860, 4502860, 10000))


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


@NeverRestart(14505700)
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


@NeverRestart(14505701)
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


@NeverRestart(14500702)
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
    CancelSpecialEffect(character_1, 5020)


@NeverRestart(14505703)
def Event_14505703():
    """Event 14505703"""
    if PlayerNotInOwnWorld():
        return
    EndIfFlagRangeAllEnabled(flag_range=(50006520, 50006521))
    
    MAIN.Await(FlagEnabled(1658))
    
    AwardItemLot(55200, host_only=False)


@NeverRestart(14505710)
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
    AND_2.Add(HealthRatioNotEqual(character, value=0.0))
    AND_2.Add(HealthRatioNotEqual(character_1, value=0.0))
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


@NeverRestart(14505711)
def Event_14505711():
    """Event 14505711"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(74500182):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=4502715))
    
    EnableFlag(74500182)


@NeverRestart(14505712)
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


@NeverRestart(14505713)
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


@NeverRestart(14505714)
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


@NeverRestart(14505720)
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


@NeverRestart(14505721)
def Event_14505721(_, obj: int, flag: int):
    """Event 14505721"""
    if FlagEnabled(1678):
        return
    AND_1.Add(FlagEnabled(flag))
    AND_1.Add(FlagEnabled(1678))
    
    MAIN.Await(AND_1)
    
    Wait(2.0)
    DisableObjectInvulnerability(obj)


@NeverRestart(14505730)
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


@NeverRestart(14505731)
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
    
    RestartIfFinishedConditionTrue(input_condition=AND_4)

    # --- Label 0 --- #
    DefineLabel(0)
    DisableObjectInvulnerability(obj)
    DestroyObject_NoSlot(obj=obj)
    EnableFlag(14500731)


@NeverRestart(14505732)
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


@NeverRestart(14505733)
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


@NeverRestart(14505740)
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


@NeverRestart(14505741)
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


@NeverRestart(14505742)
def Event_14505742():
    """Event 14505742"""
    if PlayerNotInOwnWorld():
        return
    if FlagEnabled(74500282):
        return
    
    MAIN.Await(CharacterInsideRegion(character=PLAYER, region=4502710))
    
    EnableFlag(74500282)


@NeverRestart(14500743)
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


@NeverRestart(14505750)
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


@NeverRestart(14505770)
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


@NeverRestart(14505771)
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


@NeverRestart(14505780)
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
